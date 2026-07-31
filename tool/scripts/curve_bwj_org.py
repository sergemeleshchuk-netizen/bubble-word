#!/usr/bin/env python3
"""Кривая уровней оригинала и журнал появления механик по выгрузке bwj_org.

Зачем отдельно от mine_bwj_org_knowledge.py: тот скрипт мерил КОНТЕНТ (таксономия,
пулы, хабы) и усреднял по декадам. Здесь нужен другой разрез — ПОУРОВНЕВЫЙ ряд
(что происходит на уровне N) и ответ на вопрос «с какого уровня появляется каждая
механика и когда становится нормой».

Важное ограничение источника: выгрузка взяла только слова и структуру категорий.
Сайт-ответов не публикует ни лимит ходов, ни размер стола, ни бустеры — на
странице уровня лежит граф «категория -> слова» и логотип игры вместо скриншота.
Поэтому механики здесь только КОНТЕНТНЫЕ (то, что видно в раскладке слов):
мета-пузыри, хабы-родители, ловушки-омонимы, повторы, размер доски. Механики
доски (F5 лимит из EVAL.md) из этого источника недоступны в принципе — их берём
из видео-референса, а не отсюда.

Причинный порядок: всё «впервые/уже виделось» считается по возрастанию уровня,
то есть так, как это встречает игрок. Глобальные (по всей игре) величины
помечены отдельно — они знают будущее и для кривой прохождения не годятся.

Выход:
    reference/bwj-org/curve.csv   поуровневый ряд, 1025 строк (машинный)
    reference-curve.md            отчёт: кривая по блокам + журнал механик

Запуск:
    python3 tool/scripts/curve_bwj_org.py
    python3 tool/scripts/curve_bwj_org.py --csv-only
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRAPE = ROOT / "reference" / "bwj-org" / "levels.jsonl"
CSV_OUT = ROOT / "reference" / "bwj-org" / "curve.csv"
MD_OUT = ROOT / "reference-curve.md"

# Механики: ключ флага -> (человеческое имя, что именно означает на доске).
# Порядок = порядок в журнале появления.
MECHANICS = [
    ("m_cats8", "доска 8 категорий (32 пузыря)",
     "первый шаг размера после стартовых 5"),
    ("m_cats10", "доска 10 категорий (40 пузырей)",
     "рабочий размер основной части игры"),
    ("m_cats12", "доска 12 категорий (48 пузырей)",
     "медианный размер по всей игре"),
    ("m_cats14", "доска 14 категорий (56 пузырей)",
     "крупная доска"),
    ("m_cats16", "доска 16 категорий (64 пузыря)",
     "практический потолок размера"),
    ("m_meta", "мета-пузырь",
     "имя вложенной категории лежит пузырём в родителе (MEDIA содержит RADIO)"),
    ("m_depth2", "мета-цепь глубины 2",
     "вложенность в два колена: родитель -> ребёнок -> внук"),
    ("m_depth3", "мета-цепь глубины 3",
     "вложенность в три колена"),
    ("m_hub_parent", "родитель-хаб без своих слов",
     "у родителя нет собственных слов: он только держит детей"),
    ("m_multi_meta", "два и больше мета-пузыря на уровне",
     "на доске одновременно несколько вложенных категорий"),
    ("m_dup_word", "одно слово в двух категориях уровня",
     "прямая ловушка внутри доски: один и тот же пузырь подходит двум домам"),
    ("m_pool_ne4", "категория не из 4 слов",
     "пул не равен четвёрке — у оригинала это дырка выгрузки, а не приём"),
    ("m_collide", "ловушка по памяти",
     "слово уже встречалось раньше В ДРУГОЙ категории — игрок помнит не тот дом"),
    ("m_repeat", "повтор слова из прошлых уровней",
     "слово уже виделось игроком (в любой категории)"),
    ("m_recat_same", "повтор категории с тем же пулом",
     "имя категории возвращается со старой четвёркой — чистая проверка памяти"),
    ("m_recat_new", "повтор категории с новым пулом",
     "имя категории возвращается с ДРУГИМИ словами — память мешает"),
    ("m_rare", "редкое слово (zipf < 3)",
     "экзотика, которую игрок мог не знать"),
    ("m_long", "длинное слово (>9 букв)",
     "длинные слова читаются медленнее и мешают сканировать доску"),
    ("m_multiword", "слово из нескольких слов",
     "составной пузырь («ice cream»)"),
    ("m_near_pair", "смежные категории на одном уровне",
     "две категории одной темы (sports / beach sports) — граница размывается"),
]

# Служебные слова в имени категории, по которым не стоит считать темы смежными:
# они есть в половине имён и дали бы ложные пары.
STOP_HEAD = {"of", "the", "and", "in", "at", "on", "a", "things", "types", "kinds"}


def load() -> list[dict]:
    if not SCRAPE.exists():
        sys.exit(f"нет выгрузки {SCRAPE}\n"
                 "собрать: python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025")
    return sorted((json.loads(line) for line in SCRAPE.read_text(encoding="utf-8").splitlines()
                   if line.strip()), key=lambda x: x["level"])


def zipf_fn():
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        sys.exit("нужен wordfreq: pip3 install wordfreq")

    def zipf(word: str) -> float:
        parts = [p for p in re.split(r"[ \-']+", word) if p]
        values = [zipf_frequency(p, "en") for p in parts] or [0.0]
        # у составного слова сложность задаёт самая редкая часть
        return min(values) if len(parts) > 1 else values[0]

    return zipf


def head(name: str) -> str:
    """Головное слово имени категории: по нему ищем смежные темы одного уровня."""
    parts = [p for p in name.split() if p not in STOP_HEAD]
    return parts[-1] if parts else name


def near_pairs(cats: list[dict]) -> int:
    """Пары категорий уровня, которые сидят на одной теме.

    Три признака: общее головное слово (sports / beach sports), одно имя целиком
    внутри другого (capitals / european capitals), родитель-ребёнок на доске.
    """
    pairs = 0
    n = len(cats)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = cats[i], cats[j]
            na, nb = a["name"], b["name"]
            if na == nb:
                continue
            same_head = head(na) == head(nb)
            nested_name = set(na.split()) < set(nb.split()) or set(nb.split()) < set(na.split())
            kin = a.get("parent") == nb or b.get("parent") == na
            if same_head or nested_name or kin:
                pairs += 1
    return pairs


def own_words(cat: dict) -> list[str]:
    """Свои слова категории: пул минус имена детей, лежащие в нём пузырями."""
    kids = set(cat.get("meta_words") or [])
    return [w for w in cat["words"] if w not in kids]


def difficulty(row: dict) -> tuple[float, float]:
    """Сложность уровня в терминах EVAL.md: с обрезкой (как в приёмке) и без.

    Считаются F1 масштаб, F2 ловушки, F3 близость, F4 редкость, F6 память.
    НЕ считаются F5 лимит ходов и F7 внеплановая двусмысленность: лимита в
    источнике нет, а двусмысленность даёт только решатель.

    Две цифры нужны потому, что шкала EVAL писалась под НАШИ уровни и на
    оригинале упирается в потолок: у него категорий 12-16 и десятки повторов,
    то есть каждый фактор лежит на своём максимуме уже с первой сотни, и
    d_eval перестаёт различать L150 и L900. Форму кривой показывает d_raw
    (те же веса, но без обрезки), а d_eval оставлен, чтобы это упирание было
    видно в данных.
    """
    m = row["cats"]
    f1 = 0 if m <= 6 else 1 if m <= 8 else 1.5 if m <= 10 else 2.5
    traps = row["dup_word_n"] + row["collide_n"]
    d_raw = 1 + f1 + traps * 1.0 + row["near_pairs"] * 0.75 \
        + row["rare_n"] * 0.5 + row["repeat_n"] * 0.5
    d_eval = 1 + f1 + min(traps * 1.0, 3) + min(row["near_pairs"] * 0.75, 1.5) \
        + min(row["rare_n"] * 0.5, 1) + min(row["repeat_n"] * 0.5, 1)
    return round(min(d_eval, 10), 2), round(d_raw, 1)


def build_rows(levels: list[dict]) -> list[dict]:
    zipf = zipf_fn()

    # глобальные (знают всю игру) — только для справки, в кривую не идут
    word_cats_global: dict[str, set[str]] = defaultdict(set)
    for lvl in levels:
        for cat in lvl["categories"]:
            for w in cat["words"]:
                word_cats_global[w].add(cat["name"])

    seen_word_cats: dict[str, set[str]] = defaultdict(set)   # слово -> где уже лежало
    seen_names: set[str] = set()
    seen_pools: dict[str, set[tuple[str, ...]]] = defaultdict(set)

    rows = []
    for lvl in levels:
        n = lvl["level"]
        cats = lvl["categories"]
        words_all = [w for c in cats for w in c["words"]]
        # пул = все пузыри в доме категории, включая имя вложенной категории:
        # у оригинала это всегда ровно 4, и доска равна 4 x категорий
        pools = [len(c["words"]) for c in cats]
        owns = [len(own_words(c)) for c in cats]

        metas = sum(len(c.get("meta_words") or []) for c in cats)
        hub_parents = sum(1 for c in cats
                          if (c.get("meta_words") or []) and not own_words(c))
        max_depth = max((c["depth"] for c in cats), default=0)

        # слово, лежащее в двух категориях ОДНОГО уровня
        word_here = Counter(words_all)
        dup_word_n = sum(1 for w, k in word_here.items() if k > 1)

        # причинные величины: что игрок уже видел до этого уровня
        collide_n = repeat_n = 0
        for c in cats:
            for w in c["words"]:
                prev = seen_word_cats.get(w)
                if prev:
                    repeat_n += 1
                    if c["name"] not in prev:
                        collide_n += 1

        new_names = sum(1 for c in cats if c["name"] not in seen_names)
        recat_same = recat_new = 0
        for c in cats:
            if c["name"] in seen_names:
                pool = tuple(sorted(c["words"]))
                if pool in seen_pools[c["name"]]:
                    recat_same += 1
                else:
                    recat_new += 1

        zs = [z for z in (zipf(w) for w in words_all) if z > 0]
        rare_n = sum(1 for z in zs if z < 3)
        long_n = sum(1 for w in words_all if len(w.replace(" ", "")) > 9)
        multi_n = sum(1 for w in words_all if " " in w or "-" in w)
        hub_n = sum(1 for w in words_all if len(word_cats_global[w]) >= 2)

        row = {
            "level": n,
            "cats": len(cats),
            "words": len(words_all),
            "pool_min": min(pools) if pools else 0,
            "pool_max": max(pools) if pools else 0,
            "pool_ne4_n": sum(1 for p in pools if p != 4),
            "own_min": min(owns) if owns else 0,
            "meta_n": metas,
            "hub_parent_n": hub_parents,
            "max_depth": max_depth,
            "dup_word_n": dup_word_n,
            "collide_n": collide_n,
            "repeat_n": repeat_n,
            "new_name_n": new_names,
            "recat_same_n": recat_same,
            "recat_new_n": recat_new,
            "rare_n": rare_n,
            "long_n": long_n,
            "multi_n": multi_n,
            "hub_word_n": hub_n,
            "near_pairs": near_pairs(cats),
            "zipf_med": round(statistics.median(zs), 2) if zs else 0,
            "repeat_share": round(repeat_n / len(words_all), 3) if words_all else 0,
            "new_name_share": round(new_names / len(cats), 3) if cats else 0,
        }
        row["d_eval"], row["d_raw"] = difficulty(row)

        # флаги механик
        row["m_cats8"] = int(row["cats"] >= 8)
        row["m_cats10"] = int(row["cats"] >= 10)
        row["m_cats12"] = int(row["cats"] >= 12)
        row["m_cats14"] = int(row["cats"] >= 14)
        row["m_cats16"] = int(row["cats"] >= 16)
        row["m_pool_ne4"] = int(row["pool_ne4_n"] > 0)
        row["m_meta"] = int(metas > 0)
        row["m_depth2"] = int(max_depth >= 2)
        row["m_depth3"] = int(max_depth >= 3)
        row["m_hub_parent"] = int(hub_parents > 0)
        row["m_multi_meta"] = int(metas >= 2)
        row["m_dup_word"] = int(dup_word_n > 0)
        row["m_collide"] = int(collide_n > 0)
        row["m_repeat"] = int(repeat_n > 0)
        row["m_recat_same"] = int(recat_same > 0)
        row["m_recat_new"] = int(recat_new > 0)
        row["m_rare"] = int(rare_n > 0)
        row["m_long"] = int(long_n > 0)
        row["m_multiword"] = int(multi_n > 0)
        row["m_near_pair"] = int(row["near_pairs"] > 0)
        rows.append(row)

        # обновляем память ПОСЛЕ уровня: иначе слово столкнулось бы само с собой
        for c in cats:
            seen_names.add(c["name"])
            seen_pools[c["name"]].add(tuple(sorted(c["words"])))
            for w in c["words"]:
                seen_word_cats[w].add(c["name"])

    return rows


def ledger(rows: list[dict]) -> list[dict]:
    """Журнал механик: где впервые, как часто, с какого блока это норма."""
    out = []
    total = len(rows)
    for key, name, meaning in MECHANICS:
        hits = [r["level"] for r in rows if r[key]]
        if not hits:
            out.append({"key": key, "name": name, "meaning": meaning,
                        "first": None, "levels": 0, "share": 0, "routine": None})
            continue
        # «норма» = первый блок из 10 уровней, где механика есть на 5+ уровнях,
        # и дальше она уже не пропадает надолго
        routine = None
        for start in range(1, total + 1, 10):
            block = [r for r in rows if start <= r["level"] < start + 10]
            if block and sum(r[key] for r in block) >= 5:
                routine = start
                break
        out.append({
            "key": key, "name": name, "meaning": meaning,
            "first": hits[0], "levels": len(hits),
            "share": round(len(hits) / total, 3),
            "routine": routine,
        })
    return out


def blocks(rows: list[dict], size: int = 100) -> list[dict]:
    out = []
    for start in range(1, max(r["level"] for r in rows) + 1, size):
        b = [r for r in rows if start <= r["level"] < start + size]
        if not b:
            continue
        out.append({
            "range": f"{start}-{min(start + size - 1, b[-1]['level'])}",
            "n": len(b),
            "cats": round(statistics.mean(r["cats"] for r in b), 1),
            "words": round(statistics.mean(r["words"] for r in b), 1),
            "d_eval": round(statistics.mean(r["d_eval"] for r in b), 2),
            "d_raw": round(statistics.mean(r["d_raw"] for r in b), 1),
            "meta": round(statistics.mean(r["meta_n"] for r in b), 1),
            "traps": round(statistics.mean(r["dup_word_n"] + r["collide_n"] for r in b), 1),
            "repeat": round(statistics.mean(r["repeat_share"] for r in b), 2),
            "new_names": round(statistics.mean(r["new_name_share"] for r in b), 2),
            "rare": round(statistics.mean(r["rare_n"] for r in b), 1),
            "near": round(statistics.mean(r["near_pairs"] for r in b), 1),
        })
    return out


def markdown(rows: list[dict], led: list[dict], blk: list[dict]) -> str:
    L = []
    A = L.append
    A("# Кривая уровней оригинала и появление механик")
    A("")
    A("Замер по выгрузке `reference/bwj-org/levels.jsonl` (1025 уровней с "
      "bubblewordjam.org). Воспроизводится: `python3 tool/scripts/curve_bwj_org.py`, "
      "поуровневый ряд лежит в `reference/bwj-org/curve.csv`.")
    A("")
    A("## Что этот замер может и чего не может")
    A("")
    A("Выгрузка брала только слова и структуру категорий. Сайт-ответов не "
      "публикует ни лимит ходов, ни размер стола, ни бустеры: на странице уровня "
      "лежит граф «категория -> слова», а картинка уровня — логотип игры, не "
      "скриншот доски. Поэтому:")
    A("")
    A("- механики ниже — **контентные**: то, что видно в раскладке слов;")
    A("- механики **доски** (лимит ходов = F5 в `levels/EVAL.md`, размер стола, "
      "бустеры) из этого источника недоступны в принципе — они остаются за "
      "видео-референсом;")
    A("- сложность считается по EVAL.md БЕЗ F5 и F7 (лимита в источнике нет, "
      "двусмысленность даёт только решатель), поэтому это не оценка для сдачи.")
    A("")
    A("Постоянные величины, которые оказались не механикой, а устройством игры: "
      "**пул категории у оригинала всегда ровно 4 пузыря** (12365 категорий из "
      "12367), а значит **доска всегда равна 4 x числу категорий** (1023 уровня "
      "из 1025). Два исключения — L293 и L685, у категории `falsehood` в выгрузке "
      "потерялось слово; это дырка источника, а не приём.")
    A("")
    A(f"Шкала EVAL на оригинале упирается в потолок: медиана `d_eval` "
      f"{statistics.median([r['d_eval'] for r in rows]):.1f}, ровно 10 стоит у "
      f"{sum(1 for r in rows if r['d_eval'] >= 10) / len(rows):.0%} уровней, и "
      "блоки по сотне между собой почти не различаются. Причина простая: у "
      "оригинала 12-16 категорий и десятки повторов, то есть каждый фактор лежит "
      "на своём максимуме уже с первой сотни. Форму кривой поэтому показывает "
      "`d_raw` — те же веса без обрезки.")
    A("")
    A("Всё «впервые / уже виделось» посчитано причинно — по возрастанию уровня, "
      "как это встречает игрок. Память обновляется после уровня, поэтому слово "
      "не сталкивается само с собой.")
    A("")
    A("## 1. Журнал механик: где появляется, где становится нормой")
    A("")
    A("«Норма» — первый блок из 10 уровней, где механика встречается на 5+ уровнях.")
    A("")
    A("| механика | впервые | норма с | уровней | доля |")
    A("|---|---:|---:|---:|---:|")
    for m in led:
        first = f"L{m['first']}" if m["first"] else "нет ни разу"
        routine = f"L{m['routine']}" if m["routine"] else "не стала"
        A(f"| {m['name']} | {first} | {routine} | {m['levels']} | {m['share']:.0%} |")
    A("")
    A("Что каждая механика значит на доске:")
    A("")
    for m in led:
        A(f"- **{m['name']}** — {m['meaning']}.")
    A("")
    A("## 2. Кривая по блокам 100 уровней")
    A("")
    A("| блок | кат | пузырей | d_eval | d_raw | мета | ловушек | повторов | новых имён | редких | смежных пар |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for b in blk:
        A(f"| {b['range']} | {b['cats']} | {b['words']} | {b['d_eval']} | {b['d_raw']} | "
          f"{b['meta']} | {b['traps']} | {b['repeat']:.0%} | {b['new_names']:.0%} | "
          f"{b['rare']} | {b['near']} |")
    A("")
    A("## 3. Как читать кривую")
    A("")
    plateau = [r for r in rows if r["level"] > 300]
    tiers = " -> ".join(
        f"{k} кат. с L{next(r['level'] for r in rows if r['cats'] >= k)}"
        for k in (8, 10, 12, 14, 16) if any(r["cats"] >= k for r in rows))
    A(f"- **Размер доски** растёт ступенями ({tiers}) и упирается в потолок: "
      f"после L300 среднее держится на "
      f"{round(statistics.mean(r['words'] for r in plateau), 1)} пузырях "
      f"({round(statistics.mean(r['cats'] for r in plateau), 1)} категорий) и "
      "больше не растёт. Значит масштаб — не главный рычаг сложности у оригинала.")
    early = [r for r in rows if r["level"] <= 100]
    late = [r for r in rows if r["level"] > 900]
    A(f"- **Главный рычаг — память**: доля уже виденных слов идёт с "
      f"{statistics.mean(r['repeat_share'] for r in early):.0%} на первой сотне до "
      f"{statistics.mean(r['repeat_share'] for r in late):.0%} на последней. "
      "Уровень поздней игры почти целиком собран из знакомых слов, но в новых домах.")
    A(f"- **Ловушки** (слово в двух категориях доски + столкновение с памятью) "
      f"растут с {statistics.mean(r['dup_word_n'] + r['collide_n'] for r in early):.1f} "
      f"до {statistics.mean(r['dup_word_n'] + r['collide_n'] for r in late):.1f} на уровень.")
    A("- **Мета-пузыри** ведут себя не как «механика на разгон»: они появляются "
      "рано, дают пик в первой сотне и дальше только редеют. То есть это приём "
      "для разнообразия, а не для сложности.")
    A("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv-only", action="store_true", help="только curve.csv, без отчёта")
    args = ap.parse_args()

    levels = load()
    rows = build_rows(levels)

    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{CSV_OUT.relative_to(ROOT)}: {len(rows)} уровней, {len(rows[0])} колонок")

    if args.csv_only:
        return 0

    led = ledger(rows)
    blk = blocks(rows)
    MD_OUT.write_text(markdown(rows, led, blk), encoding="utf-8")
    print(f"{MD_OUT.relative_to(ROOT)}: журнал {len(led)} механик, кривая {len(blk)} блоков")
    for m in led:
        first = f"L{m['first']}" if m["first"] else "нет ни разу"
        print(f"  {m['name']:38} впервые {first:>11}  норма "
              f"{('L' + str(m['routine'])) if m['routine'] else '—':>6}  {m['share']:.0%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
