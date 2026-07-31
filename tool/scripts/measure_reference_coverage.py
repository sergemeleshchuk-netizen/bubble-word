#!/usr/bin/env python3
"""Может ли наша база воспроизвести уровни референса, записанные на видео.

Вопрос, на который отвечает скрипт: если попросить генератор собрать уровень 1
ровно таким, каким он был в оригинале, — хватит ли содержимого базы. Ответ
раскладывается на три независимых слоя, и путать их нельзя:

    слово есть в базе          лексика
    категория есть в базе      таксономия
    связь слово -> категория   то, из чего собирается четвёрка

Третий слой и есть настоящий ответ. Слово `cow` может лежать в базе, категория
`farm animals` тоже, но если связи между ними нет, генератор четвёрку не
соберёт: он собирает по связям, а не по догадкам.

Совпадение имён считается по четырём степеням, потому что «категории нет» и
«категория названа иначе» — разные диагнозы с разной ценой починки:

    exact      имя совпало
    morph      разошлась только форма числа (color / colors)
    contained  имя референса входит в наше более узкое (school / school supplies)
    absent     концепта нет вовсе

Запуск:
    python3 tool/scripts/measure_reference_coverage.py --max-level 10
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANSWERS = ROOT / "reference/bwj-answers/bwj_levels.json"
DB = ROOT / "tool/word_content_pipeline/database/content.sqlite"

# Связи, которыми игра имеет право пользоваться. `candidate` и `rejected` не
# играбельны, `incorrect` закрывает связь независимо от статуса пригодности.
PLAYABLE = ("approved", "alternative", "hard_only")


def normalize(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def number_variants(value: str) -> set[str]:
    """Формы числа. Единственная морфология, которая здесь нужна."""
    base = normalize(value)
    out = {base}
    if base.endswith("es"):
        out.add(base[:-2])
    if base.endswith("s"):
        out.add(base[:-1])
    out.update({base + "s", base + "es"})
    return {v for v in out if v}


def load_base(conn: sqlite3.Connection) -> tuple[set[str], dict[str, str], dict[str, set[str]]]:
    words = {row[0] for row in conn.execute("SELECT normalized FROM words")}

    by_name: dict[str, str] = {}
    for key, label in conn.execute("SELECT category_key, label FROM categories"):
        for name in (normalize(label), normalize(key)):
            by_name.setdefault(name, key)

    placeholders = ",".join("?" for _ in PLAYABLE)
    memberships: dict[str, set[str]] = {}
    for word, category in conn.execute(
        f"""
        SELECT w.normalized, c.category_key
          FROM memberships m
          JOIN words w      ON w.id = m.word_id
          JOIN categories c ON c.id = m.category_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'
        """,
        PLAYABLE,
    ):
        memberships.setdefault(word, set()).add(category)
    return words, by_name, memberships


def match_category(name: str, by_name: dict[str, str]) -> tuple[str, str | None]:
    """Возвращает (степень совпадения, наш category_key либо None)."""
    target = normalize(name)
    if target in by_name:
        return "exact", by_name[target]

    for variant in number_variants(name):
        if variant in by_name:
            return "morph", by_name[variant]

    for candidate, key in by_name.items():
        if (candidate.startswith(f"{target} ")
                or candidate.endswith(f" {target}")
                or f" {target} " in f" {candidate} "):
            return "contained", key

    return "absent", None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=10)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    levels = [l for l in json.loads(ANSWERS.read_text(encoding="utf-8"))
              if l["level"] <= args.max_level]
    conn = sqlite3.connect(DB)
    words, by_name, memberships = load_base(conn)

    degrees = {"exact": 0, "morph": 0, "contained": 0, "absent": 0}
    absent: list[dict[str, object]] = []
    renamed: list[dict[str, object]] = []
    per_level: list[dict[str, object]] = []
    word_hits = word_total = link_hits = link_total = 0
    missing_words: list[str] = []

    for level in levels:
        l_words = l_links = 0
        slots = 0
        for category in level["categories"]:
            degree, key = match_category(category["name"], by_name)
            degrees[degree] += 1
            if degree == "absent":
                absent.append({"level": level["level"], "name": category["name"]})
            elif degree != "exact":
                renamed.append({"level": level["level"], "reference": category["name"],
                                "ours": key, "degree": degree})
            for word in category["words"]:
                normalized = word.lower()
                slots += 1
                word_total += 1
                link_total += 1
                if normalized in words:
                    word_hits += 1
                    l_words += 1
                else:
                    missing_words.append(word)
                if key and key in memberships.get(normalized, ()):
                    link_hits += 1
                    l_links += 1
        per_level.append({
            "level": level["level"],
            "categories": len(level["categories"]),
            "word_slots": slots,
            "words_in_base": l_words,
            "links_in_base": l_links,
        })

    categories_total = sum(degrees.values())
    report = {
        "max_level": args.max_level,
        "levels": len(levels),
        "categories_total": categories_total,
        "category_name_match": degrees,
        "concept_present_share": round(
            (categories_total - degrees["absent"]) / categories_total, 4),
        "word_coverage": {"found": word_hits, "total": word_total,
                          "share": round(word_hits / word_total, 4)},
        "membership_coverage": {"found": link_hits, "total": link_total,
                               "share": round(link_hits / link_total, 4)},
        "per_level": per_level,
        "absent_concepts": absent,
        "renamed_concepts": renamed,
        "missing_words": sorted(set(missing_words)),
    }

    print(f"Уровней 1-{args.max_level}, категорий {categories_total}\n")
    print(f"  имя совпало точно        {degrees['exact']:>4}")
    print(f"  разошлась форма числа    {degrees['morph']:>4}")
    print(f"  наше имя уже            {degrees['contained']:>4}")
    print(f"  концепта нет вовсе       {degrees['absent']:>4}")
    print(f"\n  концепт есть в каком-то виде  {100 * report['concept_present_share']:.0f}%")
    print(f"  слова есть в базе             {100 * report['word_coverage']['share']:.0f}%"
          f"  ({word_hits}/{word_total})")
    print(f"  СВЯЗЬ слово->категория есть   {100 * report['membership_coverage']['share']:.0f}%"
          f"  ({link_hits}/{link_total})   <- этим собирается четвёрка")

    if args.output:
        output = args.output if args.output.is_absolute() else Path.cwd() / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nОтчёт: {output}")


if __name__ == "__main__":
    main()
