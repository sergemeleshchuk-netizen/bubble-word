"""Сборка базы слов для генератора уровней.

Вход:  tool/data/categories_seed.json (курированные категории с пулами),
       tool/data/blocklist.txt.
Выход: tool/data/categories.json (аннотировано: zipf, длина, пересечения),
       tool/data/base_report.md (статистика и предупреждения).

Запуск (venv пайплайна, там есть wordfreq):
  level-generator/bubble_jam_pipeline/.venv/bin/python tool/scripts/build_base.py

УСТАРЕЛО (31.07). Этот скрипт собирает ПРЕЖНЮЮ базу на 306 категорий. Источник
правды теперь — SQLite-пайплайн `tool/word_content_pipeline` (1120 категорий,
внешний аудит), а `tool/data/categories.json` создаётся из него скриптом
`export_base_json.py`. Скрипт оставлен, чтобы прежнюю базу можно было пересобрать
и сверить: она лежит рядом как `categories_legacy.json` и нужна для проверки
сданных пакетов, чьи уровни ссылаются на её id категорий.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from wordfreq import zipf_frequency

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "tool" / "data"

MIN_ZIPF_WARN = 2.6   # реже - предупреждение (AGLET в референсе ~2.0, допустимо точечно)
MAX_LEN_WARN = 12     # длиннее - предупреждение (пузырь ограничен по ширине)


def load_blocklist() -> set[str]:
    words = set()
    for line in (DATA / "blocklist.txt").read_text().splitlines():
        line = line.strip().lower()
        if line and not line.startswith("#"):
            words.add(line)
    return words


def main() -> None:
    seed = json.loads((DATA / "categories_seed.json").read_text())
    blocklist = load_blocklist()

    problems: list[str] = []
    warnings: list[str] = []

    ids = [c["id"] for c in seed["categories"]]
    dup_ids = {x for x in ids if ids.count(x) > 1}
    if dup_ids:
        problems.append(f"Дубликаты id категорий: {sorted(dup_ids)}")
    id_set = set(ids)

    word_index: dict[str, list[str]] = defaultdict(list)
    out_categories = []

    for cat in seed["categories"]:
        cid, words = cat["id"], [w.strip().lower() for w in cat["words"]]

        if len(words) != len(set(words)):
            problems.append(f"[{cid}] повторы слов внутри пула")
        if len(words) < 4:
            problems.append(f"[{cid}] в пуле меньше 4 слов ({len(words)}) - уровень не собрать")
        elif len(words) < 6:
            warnings.append(f"[{cid}] пул из {len(words)} слов - генератору мало выбора")

        for rel in cat.get("related", []):
            if rel not in id_set:
                problems.append(f"[{cid}] related указывает на несуществующий id: {rel}")

        annotated = []
        for w in words:
            if w in blocklist:
                problems.append(f"[{cid}] слово из блок-листа: {w}")
            z = round(zipf_frequency(w, "en"), 2)
            if z < MIN_ZIPF_WARN:
                warnings.append(f"[{cid}] редкое слово: {w} (zipf {z})")
            if len(w) > MAX_LEN_WARN:
                warnings.append(f"[{cid}] длинное слово: {w} ({len(w)} букв)")
            word_index[w].append(cid)
            annotated.append({"w": w, "zipf": z, "len": len(w)})
        out_categories.append({
            "id": cid,
            "name": cat["name"],
            "related": cat.get("related", []),
            "words": annotated,
        })

    shared = {w: cats for w, cats in sorted(word_index.items()) if len(cats) > 1}
    for cat in out_categories:
        cat["shared_words"] = {
            item["w"]: [c for c in word_index[item["w"]] if c != cat["id"]]
            for item in cat["words"] if len(word_index[item["w"]]) > 1
        }

    out = {
        "version": seed["version"],
        "language": seed["language"],
        "built_from": "categories_seed.json + blocklist.txt (build_base.py)",
        "categories": out_categories,
    }
    (DATA / "categories.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

    all_words = [i["w"] for c in out_categories for i in c["words"]]
    zipfs = [i["zipf"] for c in out_categories for i in c["words"]]
    lines = [
        "# Отчёт сборки базы слов",
        "",
        f"- Категорий: {len(out_categories)}",
        f"- Слов всего: {len(all_words)}, уникальных: {len(set(all_words))}",
        f"- Слов в двух+ категориях (кандидаты в ловушки): {len(shared)}",
        f"- Средний zipf: {sum(zipfs)/len(zipfs):.2f}, минимум: {min(zipfs):.2f}",
        f"- Записей в блок-листе: {len(blocklist)}",
        "",
        "## Пересечения (слово -> категории)",
        "",
    ]
    lines += [f"- **{w}**: {', '.join(cats)}" for w, cats in shared.items()]
    lines += ["", f"## Ошибки ({len(problems)})", ""]
    lines += [f"- {p}" for p in problems] or ["- нет"]
    lines += ["", f"## Предупреждения ({len(warnings)})", ""]
    lines += [f"- {w}" for w in warnings] or ["- нет"]
    (DATA / "base_report.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({
        "categories": len(out_categories),
        "words": len(all_words),
        "unique_words": len(set(all_words)),
        "shared_words": len(shared),
        "problems": len(problems),
        "warnings": len(warnings),
    }, ensure_ascii=False, indent=2))
    if problems:
        print("ОШИБКИ:")
        for p in problems:
            print(" -", p)


if __name__ == "__main__":
    main()
