#!/usr/bin/env python3
"""Собирает data/categories.jsonl и data/membership_candidates.jsonl из data/seed/.

Источник правды для seed-контента — каталог `data/seed/`:

  data/seed/<theme>.json   категории одной темы + пулы слов
  data/seed/_ambiguous.json  многозначные слова: значения разведены через sense_key

Добавить контент = отредактировать или создать файл темы, затем запустить:

    python scripts/build_seed.py

Формат файла темы:

{
  "theme": "food",
  "categories": [
    {
      "category_key": "fruits",
      "label": "FRUITS",
      "rule": "Common edible fruits familiar to an average American adult",
      "relation_type": "is_a",
      "theme": "food",
      "base_difficulty": 0.1,
      "obviousness": 0.95,          // очевидность связей этой категории
      "approve": true,              // можно ли ставить approved без ручной проверки
      "reason_template": "$W is a common edible fruit",   // $W — слово с заглавной, $w — как есть
      "is_proper_noun": false,      // необязательно
      "words": ["apple", "banana"]
    }
  ]
}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from word_content.blocklist import Blocklist  # noqa: E402
from word_content.familiarity import zipf  # noqa: E402
from word_content.normalization import normalize_word  # noqa: E402

SEED_DIR = ROOT / "data" / "seed"
SOURCE = "seed_manual"
DEFAULT_FIT = 0.97
RARE_ZIPF = 2.5  # ниже этого слово помечается в отчёте как редкое


def load_seed() -> tuple[list[dict], list[dict]]:
    """Читает все файлы тем и файл многозначных слов."""
    if not SEED_DIR.is_dir():
        raise SystemExit(f"Нет каталога с сидом: {SEED_DIR}")

    categories: list[dict] = []
    for path in sorted(SEED_DIR.glob("*.json")):
        if path.name.startswith("_"):
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        theme = payload.get("theme") or path.stem
        for item in payload["categories"]:
            item.setdefault("theme", theme)
            item["_source_file"] = path.name
            categories.append(item)

    ambiguous_path = SEED_DIR / "_ambiguous.json"
    ambiguous = (
        json.loads(ambiguous_path.read_text(encoding="utf-8"))["memberships"]
        if ambiguous_path.exists()
        else []
    )
    return categories, ambiguous


def capitalize(word: str) -> str:
    return word[0].upper() + word[1:] if word else word


def render(template: str, word: str) -> str:
    return template.replace("$W", capitalize(word)).replace("${w}", word).replace("$w", word)


def build_categories(specs: list[dict]) -> list[dict]:
    return [
        {
            "category_key": spec["category_key"],
            "label": spec["label"],
            "rule": spec["rule"],
            "relation_type": spec["relation_type"],
            "theme": spec["theme"],
            "base_difficulty": spec.get("base_difficulty"),
        }
        for spec in specs
    ]


def build_memberships(specs: list[dict], ambiguous: list[dict]) -> list[dict]:
    records: list[dict] = []
    explicit = {(normalize_word(row["word"]), row["category_key"]) for row in ambiguous}

    for row in ambiguous:
        records.append(
            {
                "word": row["word"],
                "language": "en",
                "part_of_speech": row.get("part_of_speech"),
                "is_proper_noun": bool(row.get("is_proper_noun")),
                "sense_key": row["sense_key"],
                "sense_definition": row["sense_definition"],
                "category_key": row["category_key"],
                "relation_type": row["relation_type"],
                "reason": row["reason"],
                "fit_score": row["fit_score"],
                "obviousness_score": row["obviousness_score"],
                "source": SOURCE,
                "review_status": row.get("review_status", "candidate"),
            }
        )

    for spec in specs:
        proper = bool(spec.get("is_proper_noun"))
        for word in spec["words"]:
            if (normalize_word(word), spec["category_key"]) in explicit:
                continue  # связь описана вручную вместе со значением слова
            records.append(
                {
                    "word": word,
                    "language": "en",
                    "part_of_speech": "proper_noun" if proper else "noun",
                    "is_proper_noun": proper,
                    "category_key": spec["category_key"],
                    "relation_type": spec["relation_type"],
                    "reason": render(spec["reason_template"], word),
                    "fit_score": spec.get("fit_score", DEFAULT_FIT),
                    "obviousness_score": spec["obviousness"],
                    "source": SOURCE,
                    # approved только для очевидных вручную выверенных пулов
                    "review_status": "approved" if spec.get("approve") else "candidate",
                }
            )
    return records


def validate(categories: list[dict], memberships: list[dict], specs: list[dict]) -> list[str]:
    """Проверки перед записью: дубли, битые ссылки, блок-лист."""
    problems: list[str] = []

    seen_keys: dict[str, str] = {}
    for spec in specs:
        key = spec["category_key"]
        if key in seen_keys:
            problems.append(f"дубль category_key {key!r} ({seen_keys[key]} и {spec['_source_file']})")
        seen_keys[key] = spec["_source_file"]

    keys = {c["category_key"] for c in categories}
    for membership in memberships:
        if membership["category_key"] not in keys:
            problems.append(f"связь на несуществующую категорию: {membership['category_key']}")

    identity: dict[tuple, int] = {}
    for membership in memberships:
        key = (
            normalize_word(membership["word"]),
            membership["category_key"],
            membership.get("sense_key") or "",
        )
        identity[key] = identity.get(key, 0) + 1
    for key, count in identity.items():
        if count > 1:
            problems.append(f"дубль связи: {key[0]} -> {key[1]} (значение {key[2] or '-'})")

    blocklist = Blocklist.load(ROOT / "data" / "blocklist.txt")
    for membership in memberships:
        hit = blocklist.check(membership["word"])
        if hit:
            problems.append(f"слово из блок-листа: {membership['word']} (совпадение {hit})")

    return problems


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    specs, ambiguous = load_seed()
    categories = build_categories(specs)
    memberships = build_memberships(specs, ambiguous)

    problems = validate(categories, memberships, specs)
    if problems:
        print(f"Найдено проблем: {len(problems)}")
        for problem in problems[:20]:
            print(f"  - {problem}")
        raise SystemExit(1)

    write_jsonl(ROOT / "data" / "categories.jsonl", categories)
    write_jsonl(ROOT / "data" / "membership_candidates.jsonl", memberships)

    themes = {c["theme"] for c in categories}
    words = {normalize_word(m["word"]) for m in memberships}
    multi: dict[str, set[str]] = {}
    for membership in memberships:
        multi.setdefault(normalize_word(membership["word"]), set()).add(membership["category_key"])
    multi_words = sum(1 for keys in multi.values() if len(keys) > 1)

    rare = sorted(
        (word for word in words if (z := zipf(word)) is not None and z < RARE_ZIPF),
        key=lambda w: zipf(w) or 0,
    )

    print(f"категорий: {len(categories)} в {len(themes)} темах")
    print(f"связей:    {len(memberships)}")
    print(f"слов:      {len(words)} (в двух и более категориях: {multi_words})")
    print(f"approved:  {sum(1 for m in memberships if m['review_status'] == 'approved')}")
    if rare:
        print(f"редких слов (zipf < {RARE_ZIPF}): {len(rare)} -> {', '.join(rare[:15])}")


if __name__ == "__main__":
    main()
