#!/usr/bin/env python3
"""Выгрузка уровней оригинала с bubblewordjam.org (фанатский сайт ответов).

Зачем: наша прежняя выгрузка (`reference/bwj-answers/`, источник
puzzlegamemaster.com) кончается на уровне 199. Этот сайт покрывает 1-1025 и,
что важнее, отдаёт СТРУКТУРУ категорий: вложенность размечена в data-id узлов,
то есть мета-цепи («MEDIA содержит RADIO») видны явно, а не выводятся догадкой.

Разметка страницы /level/N (react-flow):

    category__media                       категория верхнего уровня
    category__media__radio                вложенная категория (мета-ребёнок)
    word__media__radio__0__station        слово в этой вложенной категории
    word__media__0__television            слово в категории верхнего уровня

Соглашения слага: `__` разделяет уровни, `-` внутри сегмента = пробел
(`farm-animals` -> «farm animals», `taylor-swift` -> «taylor swift»). Слова
с настоящим дефисом (`8-ball`, `first-person`) от пробела не отличить — они
чинятся сверкой со прежней выгрузкой, см. `--fix-hyphens`.

Вежливость: robots.txt сайта разрешает обход целиком (Allow: /), но сайт мелкий,
поэтому запросы идут по одному с задержкой и с честным User-Agent. Есть чекпоинт:
прерванный прогон продолжается с того же места, а не начинает заново.

Запуск:
    python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025
    python3 tool/scripts/scrape_bwj_org.py --report      # только сводка по готовому
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "reference" / "bwj-org"
RAW = OUT_DIR / "levels.jsonl"          # по одной строке на уровень: чекпоинт и он же данные
FLAT = OUT_DIR / "bwj_levels.json"      # формат прежней выгрузки: уровень -> категории -> слова
REPORT = OUT_DIR / "bwj_org_report.md"
OLD_DUMP = ROOT / "reference" / "bwj-answers" / "bwj_levels.json"

BASE_URL = "https://bubblewordjam.org/level/{n}"
UA = "BB-research-bot/1.0 (level curve measurement; contact via repo owner)"

NODE_RE = re.compile(r'data-id="([^"]+)"')

# --------------------------------------------------------------------------- #
# кусочки слова
# --------------------------------------------------------------------------- #
# `data-id` в разметке несёт только путь категории, индекс и слаг слова. Всё
# остальное про слово живёт в payload'е Next.js, который страница отдаёт
# React-приложению, — и там есть поле, которого у нас не было: `chunks`.
#
# Распиленное слово приходит на поле ДВУМЯ пузырями («august» = «Au» + «gust»).
# Для нас это не косметика: поле держит 24 пузыря независимо от размера уровня,
# поэтому каждый распил уменьшает видимую долю уровня на старте. Без chunks
# уровень оригинала невозможно воспроизвести по числу пузырей — до этой правки
# они были известны ровно для одного уровня, снятого руками с видеозаписи.
#
# Оттуда же берётся `text` — форма слова, как её печатает сайт. Слаг между
# дефисом и пробелом не различает (`8-ball` и `hot air balloon` выглядят
# одинаково), а `text` различает. Регистру доверять нельзя: на L1 соседние
# слова приходят как «Cow» и «goat», то есть заполнялось руками.
PAYLOAD_RE = re.compile(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', re.S)
WORD_NODE_RE = re.compile(
    r'"id":"(word__[^"]+)","type":"wordNode","position":\{[^}]*\},'
    r'"data":\{"label":"[^"]*","text":"((?:[^"\\]|\\.)*)","chunks":\[([^\]]*)\]')
CHUNK_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def word_extras(html: str) -> dict[str, dict]:
    """`id узла слова -> {text, chunks}` из payload'а Next.js.

    Payload склеен из строковых кусков и экранирован дважды. Если разбор не
    удался, возвращается пустой словарь: страница всё равно разбирается по
    `data-id`, просто без кусочков — так выгрузка деградирует, а не падает.
    """
    parts = PAYLOAD_RE.findall(html)
    if not parts:
        return {}
    try:
        payload = "".join(parts).encode().decode("unicode_escape", errors="replace")
    except UnicodeDecodeError:
        return {}
    extras: dict[str, dict] = {}
    for node_id, text, chunks in WORD_NODE_RE.findall(payload):
        pieces = CHUNK_RE.findall(chunks)
        extras[node_id] = {"text": text, "chunks": pieces}
    return extras


def unslug(segment: str) -> str:
    return segment.replace("-", " ").strip()


def parse_level(html: str) -> list[dict]:
    """Разбирает страницу в список категорий с путём вложенности и словами.

    Ключевая деталь механики, которую сайт размечает явно: у категории-родителя
    один из четырёх пузырей — это ИМЯ вложенной категории (мета-пузырь). В
    разметке такое слово живёт не узлом слова, а узлом категории:

        category__measurements                        4 «слова» = 4 вложенных
        category__measurements__time                  категории, своих слов нет
        category__landmass + word__landmass__0__asia  3 своих слова + ребёнок

    Поэтому пул родителя собирается из своих слов ПЛЮС имён прямых детей.
    Порядок мета-слова в четвёрке разметка не сообщает — оно дописывается в
    конец, в порядке появления в DOM. Для словаря и структуры это неважно,
    для точного воспроизведения раскладки — важно, и это ограничение осознанное.
    """
    ids = [i for i in NODE_RE.findall(html) if not i.startswith("1-")]
    extras = word_extras(html)
    categories: dict[tuple[str, ...], dict] = {}
    order: list[tuple[str, ...]] = []

    def ensure(path: tuple[str, ...]) -> dict:
        if path not in categories:
            categories[path] = {"path": [unslug(p) for p in path],
                                "name": unslug(path[-1]), "own": [], "meta": []}
            order.append(path)
        return categories[path]

    for node in ids:
        if node.startswith("category__"):
            ensure(tuple(node[len("category__"):].split("__")))
        elif node.startswith("word__"):
            parts = node[len("word__"):].split("__")
            if len(parts) < 3 or not parts[-2].isdigit():
                continue
            path, index, slug = tuple(parts[:-2]), int(parts[-2]), parts[-1]
            extra = extras.get(node, {})
            ensure(path)["own"].append(
                (index, unslug(slug), slug, extra.get("text", ""),
                 extra.get("chunks", [])))

    # имя ребёнка занимает слот слова у родителя
    for path in order:
        if len(path) > 1 and path[:-1] in categories:
            categories[path[:-1]]["meta"].append(categories[path]["name"])

    result = []
    for path in order:
        cat = categories[path]
        own_sorted = sorted(cat["own"])
        own = [w for _, w, _, _, _ in own_sorted]
        own_raw = [raw for _, _, raw, _, _ in own_sorted]
        own_text = [text for _, _, _, text, _ in own_sorted]
        # кусочки только у тех слов, у которых они есть: пустые списки в файл не
        # пишем, иначе выгрузка распухнет на 15 тысяч пустых полей
        chunked = [{"word": w, "pieces": pieces}
                   for (_, w, _, _, pieces) in own_sorted if pieces]
        result.append({
            "path": cat["path"],
            "name": cat["name"],
            "words": own + cat["meta"],
            # сырые слаги: дефис от пробела в слаге не отличить (`hot-air balloon`),
            # поэтому исходная форма сохраняется рядом и решает потребитель
            "words_raw": own_raw + [m.replace(" ", "-") for m in cat["meta"]],
            # форма слова с сайта: дефис от пробела отличает, в отличие от слага.
            # Регистр здесь бытовой, а не смысловой — заполнялось руками
            "words_text": own_text + list(cat["meta"]),
            # какие из слов — мета-пузыри (имена других категорий этого уровня)
            "meta_words": list(cat["meta"]),
            # слова, приходящие на поле ДВУМЯ пузырями, и место распила
            "chunked_words": chunked,
            "depth": len(path) - 1,
            "parent": " ".join(cat["path"][:-1]) or None,
        })
    return result


def fetch(url: str, attempts: int = 3, timeout: int = 30) -> str | None:
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            wait = 2 ** attempt
        except (urllib.error.URLError, TimeoutError, OSError):
            wait = 2 ** attempt
        if attempt < attempts:
            time.sleep(wait)
    return None


def done_levels() -> set[int]:
    if not RAW.exists():
        return set()
    seen = set()
    for line in RAW.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                seen.add(json.loads(line)["level"])
            except (json.JSONDecodeError, KeyError):
                continue
    return seen


def scrape(first: int, last: int, delay: float) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    already = done_levels()
    todo = [n for n in range(first, last + 1) if n not in already]
    print(f"уровней к выгрузке: {len(todo)} (уже есть {len(already)})", flush=True)

    empty_streak = 0
    with RAW.open("a", encoding="utf-8") as sink:
        for i, n in enumerate(todo, start=1):
            html = fetch(BASE_URL.format(n=n))
            if html is None:
                empty_streak += 1
                print(f"  L{n}: страницы нет", flush=True)
                if empty_streak >= 10:
                    print("  10 отсутствующих подряд — считаю, что уровни кончились",
                          flush=True)
                    break
                time.sleep(delay)
                continue
            cats = parse_level(html)
            if not cats:
                empty_streak += 1
                print(f"  L{n}: разметка не разобрана", flush=True)
            else:
                empty_streak = 0
            sink.write(json.dumps({"level": n, "categories": cats},
                                  ensure_ascii=False) + "\n")
            sink.flush()
            if i % 25 == 0:
                print(f"  ... {i}/{len(todo)} (последний L{n}, категорий {len(cats)})",
                      flush=True)
            time.sleep(delay)


def load_all() -> list[dict]:
    levels = []
    for line in RAW.read_text(encoding="utf-8").splitlines():
        if line.strip():
            levels.append(json.loads(line))
    return sorted(levels, key=lambda x: x["level"])


def write_flat(levels: list[dict]) -> None:
    """Формат прежней выгрузки: имя категории + 4 слова, без вложенности."""
    flat = [{"level": lvl["level"],
             "categories": [{"name": c["name"], "words": c["words"]}
                            for c in lvl["categories"]]}
            for lvl in levels]
    FLAT.write_text(json.dumps(flat, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")


def report(levels: list[dict]) -> str:
    words = Counter()
    names = Counter()
    depth_hist = Counter()
    per_level = []
    bad = []
    for lvl in levels:
        cats = lvl["categories"]
        per_level.append((lvl["level"], len(cats)))
        for c in cats:
            names[c["name"]] += 1
            depth_hist[c["depth"]] += 1
            for w in c["words"]:
                words[w] += 1
            if len(c["words"]) != 4:
                bad.append((lvl["level"], c["name"], len(c["words"])))

    lines = ["# Выгрузка bubblewordjam.org", ""]
    lines.append(f"- уровней: {len(levels)} "
                 f"(с {levels[0]['level']} по {levels[-1]['level']})")
    lines.append(f"- категорий-вхождений: {sum(n for _, n in per_level)}")
    lines.append(f"- уникальных имён категорий: {len(names)}")
    lines.append(f"- уникальных слов: {len(words)}")
    lines.append(f"- категорий не по 4 слова: {len(bad)}")
    lines.append("")
    lines.append("## Вложенность категорий (мета-цепи размечены на сайте)")
    for depth in sorted(depth_hist):
        lines.append(f"- глубина {depth}: {depth_hist[depth]} категорий")
    lines.append("")
    lines.append("## Категорий на уровень по декадам")
    by_decade = defaultdict(list)
    for level, count in per_level:
        by_decade[(level - 1) // 10 * 10 + 1].append(count)
    for start in sorted(by_decade):
        counts = by_decade[start]
        lines.append(f"- L{start}-{start + 9}: среднее {sum(counts) / len(counts):.1f}, "
                     f"мин {min(counts)}, макс {max(counts)}")

    # сверка со прежней выгрузкой на пересечении
    if OLD_DUMP.exists():
        old = {lvl["level"]: lvl
               for lvl in json.loads(OLD_DUMP.read_text(encoding="utf-8"))}
        agree = differ = 0
        examples = []
        for lvl in levels:
            other = old.get(lvl["level"])
            if not other:
                continue
            mine = {(c["name"], tuple(sorted(c["words"]))) for c in lvl["categories"]}
            theirs = {(c["name"], tuple(sorted(w.lower() for w in c["words"])))
                      for c in other["categories"]}
            if mine == theirs:
                agree += 1
            else:
                differ += 1
                if len(examples) < 5:
                    examples.append((lvl["level"], sorted(mine - theirs)[:2],
                                     sorted(theirs - mine)[:2]))
        lines.append("")
        lines.append("## Сверка с прежней выгрузкой (puzzlegamemaster.com, L1-199)")
        lines.append(f"- уровней совпало полностью: {agree}")
        lines.append(f"- уровней с расхождениями: {differ}")
        for level, only_new, only_old in examples:
            lines.append(f"  - L{level}: тут {only_new}; там {only_old}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="first", type=int, default=1)
    parser.add_argument("--to", dest="last", type=int, default=1025)
    parser.add_argument("--delay", type=float, default=0.6, help="пауза между запросами, с")
    parser.add_argument("--report", action="store_true", help="не качать, только сводка")
    parser.add_argument("--raw", type=Path, default=None,
                        help="другой файл выгрузки: перекачать заново, не трогая старый")
    args = parser.parse_args()

    # Перекачка в отдельный файл, а не поверх: `levels.jsonl` — одновременно
    # данные и чекпоинт, и если парсер научился новому полю, дописать его в
    # старые строки нельзя, а затирать готовую выгрузку до конца прогона нельзя
    # тем более. Новый файл сверяется со старым и подменяет его руками.
    # resolve() обязателен: путь с командной строки приходит относительным, а
    # итоговый отчёт печатает его через relative_to(ROOT) и на относительном падает
    if args.raw is not None:
        globals()["RAW"] = args.raw.resolve()

    if not args.report:
        scrape(args.first, args.last, args.delay)

    if not RAW.exists():
        print("нечего сводить: файл выгрузки не создан", file=sys.stderr)
        return 1
    levels = load_all()
    write_flat(levels)
    text = report(levels)
    REPORT.write_text(text, encoding="utf-8")
    print()
    print(text)
    print(f"→ {RAW.relative_to(ROOT)}, {FLAT.relative_to(ROOT)}, {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
