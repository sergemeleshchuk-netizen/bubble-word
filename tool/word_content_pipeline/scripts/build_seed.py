#!/usr/bin/env python3
"""Собирает data/categories.jsonl и data/membership_candidates.jsonl из data/seed/.

Источник правды для seed-контента — каталог `data/seed/`:

  data/seed/<theme>.txt      категории одной темы + пулы слов (компактный формат)
  data/seed/_ambiguous.json  многозначные слова: значения разведены через sense_key

Добавить контент = отредактировать или создать файл темы, затем запустить:

    python scripts/build_seed.py

Формат файла темы: две строки на категорию.

  key | LABEL | relation_type | difficulty | obviousness | flags | rule | reason_template
  слово, слово, слово, ...

  flags: A — связи можно ставить approved, C — только candidate; добавьте P
         для категорий из имён собственных (US STATES, TECH COMPANIES); T —
         категория держит названия, неотличимые от обычных слов (BOARD GAMES:
         Risk, Sorry, Trouble). P и T оба означают «здесь названия», но P ещё
         и ставит заглавную букву в пузыре.
  reason_template: $W — слово с заглавной буквы, $w — слово как есть.

Строки, начинающиеся с #, и пустые строки игнорируются.
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


HEADER_FIELDS = 8


def parse_theme_file(path: Path) -> list[dict]:
    """Разбирает компактный файл темы: заголовок категории + строка слов."""
    theme = path.stem
    categories: list[dict] = []
    pending: dict | None = None

    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if "|" in line:
            if pending is not None:
                raise SystemExit(f"{path.name}:{line_no}: у категории {pending['category_key']} нет строки со словами")
            parts = [part.strip() for part in line.split("|")]
            if len(parts) != HEADER_FIELDS:
                raise SystemExit(
                    f"{path.name}:{line_no}: ожидалось {HEADER_FIELDS} полей через |, получено {len(parts)}"
                )
            key, label, relation, difficulty, obviousness, flags, rule, template = parts
            pending = {
                "category_key": key,
                "label": label,
                "relation_type": relation,
                "base_difficulty": float(difficulty),
                "obviousness": float(obviousness),
                "approve": "A" in flags.upper(),
                "is_proper_noun": "P" in flags.upper(),
                # T — категория держит НАЗВАНИЯ, а не слова: BOARD GAMES,
                # TEAM NAMES, CEREAL BRANDS. P означает то же самое плюс
                # заглавную букву в пузыре; T нужен там, где название
                # неотличимо от обычного слова (`Risk`, `Sorry`, `Trouble`)
                # и заглавной буквы у него нет.
                "names_titles": ("P" in flags.upper()) or ("T" in flags.upper()),
                "rule": rule,
                "reason_template": template,
                "theme": theme,
                "_source_file": path.name,
                "_line": line_no,
            }
        else:
            if pending is None:
                raise SystemExit(f"{path.name}:{line_no}: строка со словами без заголовка категории")
            pending["words"] = [word.strip() for word in line.split(",") if word.strip()]
            categories.append(pending)
            pending = None

    if pending is not None:
        raise SystemExit(f"{path.name}: у категории {pending['category_key']} нет строки со словами")
    return categories


def load_seed() -> tuple[list[dict], list[dict]]:
    """Читает все файлы тем и файл многозначных слов."""
    if not SEED_DIR.is_dir():
        raise SystemExit(f"Нет каталога с сидом: {SEED_DIR}")

    categories: list[dict] = []
    for path in sorted(SEED_DIR.glob("*.txt")):
        if path.name.startswith("_"):
            continue
        categories.extend(parse_theme_file(path))

    ambiguous_path = SEED_DIR / "_ambiguous.json"
    ambiguous = (
        json.loads(ambiguous_path.read_text(encoding="utf-8"))["memberships"]
        if ambiguous_path.exists()
        else []
    )
    return categories, ambiguous


def load_sense_map() -> tuple[dict[str, dict[str, dict]], dict[str, dict[str, dict]]]:
    """Читает _sense_map.json: дополнительные значения и карту связь -> значение.

    Возвращает (senses, assignments), где
      senses[word][sense_key]      = {"definition": ..., "part_of_speech": ...}
      assignments[word][cat_key]   = {"sense": ..., "review_status": ... | None}
    """
    path = SEED_DIR / "_sense_map.json"
    if not path.exists():
        return {}, {}
    raw = json.loads(path.read_text(encoding="utf-8"))

    senses = {
        normalize_word(word): dict(entries)
        for word, entries in (raw.get("senses") or {}).items()
    }
    assignments: dict[str, dict[str, dict]] = {}
    for word, by_category in (raw.get("assignments") or {}).items():
        bucket = assignments.setdefault(normalize_word(word), {})
        for category_key, value in by_category.items():
            if isinstance(value, str):
                bucket[category_key] = {"sense": value, "review_status": None}
            else:
                bucket[category_key] = {
                    "sense": value["sense"],
                    "review_status": value.get("review_status"),
                }
    return senses, assignments


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
            "names_titles": bool(spec.get("names_titles")),
        }
        for spec in specs
    ]


def _needs_review(word: str) -> bool:
    """True, если слово нельзя ставить approved автоматически.

    Два случая: слово редкое или частотность посчитать не удалось. Второй случай —
    P0 аудита: отсутствующие данные должны закрывать связь, а не проходить как
    подтверждённые (calfling, WD40, Barqs приходили в базу как approved).
    """
    value = zipf(word)
    return value is None or value < RARE_ZIPF


# Темы, в которых слова — товарные знаки: написание и правовой статус нужно проверять
TRADEMARK_THEMES = {"brands"}
# Темы и приставки категорий, привязанных к конкретной культуре
CULTURAL_THEMES = {"world_food", "world_more", "names_world", "religion", "culture"}
CULTURAL_PREFIXES = ("world_", "traditional_")
_MULTIWORD_RE = None


def load_risk_flags() -> dict[tuple[str, str], dict[str, str]]:
    """Читает _risk_flags.csv: ручные пометки рисков. Ключ — (слово или *, категория или *)."""
    path = SEED_DIR / "_risk_flags.csv"
    if not path.exists():
        return {}
    import csv

    lines = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    result: dict[tuple[str, str], dict[str, str]] = {}
    for row in csv.DictReader(lines):
        word = (row["word"] or "").strip()
        key = word if word == "*" else normalize_word(word)
        result[(key, (row["category_key"] or "*").strip())] = {
            "flags": (row["flags"] or "").split(),
            "note": (row.get("note") or "").strip(),
        }
    return result


def risk_flags_for(
    word: str, spec: dict, manual: dict[tuple[str, str], dict[str, str]]
) -> list[str]:
    """Флаги риска связи: механические плюс ручные.

    Аудит: поле risk_flags было пустым у всех 17 550 связей, то есть слоя
    культурных и терминологических рисков не существовало.
    """
    flags: list[str] = []
    normalized = normalize_word(word)
    value = zipf(word)

    if " " in normalized or "-" in normalized:
        flags.append("multiword")
    if spec.get("is_proper_noun"):
        flags.append("proper_noun")
    if value is None:
        flags.append("no_familiarity")
    elif value < RARE_ZIPF:
        flags.append("obscure")
    if spec["theme"] in TRADEMARK_THEMES:
        flags.append("trademark")
    if spec["theme"] in CULTURAL_THEMES or spec["category_key"].startswith(CULTURAL_PREFIXES):
        flags.append("culturally_specific")

    for key in (
        (normalized, spec["category_key"]),
        (normalized, "*"),
        ("*", spec["category_key"]),
    ):
        entry = manual.get(key)
        if entry:
            flags.extend(entry["flags"])

    seen: dict[str, None] = {}
    for flag in flags:
        seen[flag] = None
    return list(seen)


# Категории игры слов работают с написанием слова, а не с его значением:
# 'starboard' не происходит от звезды. Приписывать таким связям значение — вносить
# в базу ложь, поэтому у них sense_id остаётся пустым осознанно.
WORDPLAY_RELATIONS = {"phrase_before", "phrase_after"}


def build_memberships(
    specs: list[dict],
    ambiguous: list[dict],
    extra_senses: dict[str, dict[str, dict]] | None = None,
    assignments: dict[str, dict[str, dict]] | None = None,
) -> list[dict]:
    records: list[dict] = []
    explicit = {(normalize_word(row["word"]), row["category_key"]) for row in ambiguous}
    extra_senses = extra_senses or {}
    assignments = assignments or {}
    manual_risks = load_risk_flags()

    # Все известные значения слова: из _ambiguous.json плюс из _sense_map.json
    definitions: dict[str, dict[str, dict]] = {}
    for row in ambiguous:
        definitions.setdefault(normalize_word(row["word"]), {})[row["sense_key"]] = {
            "definition": row["sense_definition"],
            "part_of_speech": row.get("part_of_speech"),
        }
    for word, entries in extra_senses.items():
        bucket = definitions.setdefault(word, {})
        for sense_key, entry in entries.items():
            # Слияние, а не замена. Запись в `_sense_map.json` может добавлять
            # только доступность значения — формулировка при этом остаётся
            # той, что пришла из `_ambiguous.json`, и затирать её пустотой
            # нельзя.
            merged = {**bucket.get(sense_key, {}), **entry}
            merged.setdefault("definition", bucket.get(sense_key, {}).get("definition"))
            bucket[sense_key] = merged

    by_key = {spec["category_key"]: spec for spec in specs}
    for row in ambiguous:
        spec = by_key.get(row["category_key"])
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
                # у омонима значение разведено, поэтому многозначность не риск,
                # а разобранный факт: флаг highly_ambiguous здесь не ставится
                "risk_flags": risk_flags_for(row["word"], spec, manual_risks) if spec else [],
            }
        )

    for spec in specs:
        proper = bool(spec.get("is_proper_noun"))
        for word in spec["words"]:
            normalized = normalize_word(word)
            if (normalized, spec["category_key"]) in explicit:
                continue  # связь описана вручную вместе со значением слова

            record = {
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
                # approved только для очевидных вручную выверенных пулов;
                # редкое слово и слово без частотности уходят на ручную проверку
                "review_status": "approved"
                if spec.get("approve") and not _needs_review(word)
                else "candidate",
                "risk_flags": risk_flags_for(word, spec, manual_risks),
            }

            assigned = assignments.get(normalized, {}).get(spec["category_key"])
            if assigned:
                sense_key = assigned["sense"]
                known = definitions.get(normalized, {}).get(sense_key)
                if known is None or not known.get("definition"):
                    raise SystemExit(
                        f"_sense_map.json: у слова {word!r} нет значения {sense_key!r} — "
                        "опишите его в блоке senses или в _ambiguous.json"
                    )
                record["sense_key"] = sense_key
                record["sense_definition"] = known["definition"]
                if known.get("part_of_speech"):
                    record["part_of_speech"] = known["part_of_speech"]
                if assigned["review_status"]:
                    record["review_status"] = assigned["review_status"]

            records.append(record)
    return records


# Слова-связки не считаются значимыми: "PARTS OF A CAR" — это два слова, а не четыре
LABEL_CONNECTORS = {
    "OF", "THE", "A", "AN", "IN", "ON", "AND", "&", "+", "___",
    "TO", "FOR", "AT", "WITH", "BEFORE", "AFTER", "FROM",
}
MAX_LABEL_WORDS = 2
MAX_LABEL_CONNECTORS = 1  # "___ SAUCE" можно, "PARTS OF A CAR" — уже длинно
MAX_LABEL_CHARS = 22


def significant_words(label: str) -> list[str]:
    return [w for w in label.split() if w.upper() not in LABEL_CONNECTORS]


def connector_count(label: str) -> int:
    return sum(1 for w in label.split() if w.upper() in LABEL_CONNECTORS)


def validate(categories: list[dict], memberships: list[dict], specs: list[dict]) -> list[str]:
    """Проверки перед записью: длина названий, дубли, битые ссылки, блок-лист."""
    problems: list[str] = []

    # Название категории показывается игроку на пузыре — оно должно быть коротким
    seen_labels: dict[str, str] = {}
    for category in categories:
        label = category["label"]
        words = significant_words(label)
        if len(words) > MAX_LABEL_WORDS:
            problems.append(
                f"длинное название {label!r} ({category['category_key']}): "
                f"{len(words)} значимых слова, разрешено {MAX_LABEL_WORDS}"
            )
        if connector_count(label) > MAX_LABEL_CONNECTORS:
            problems.append(
                f"название {label!r} ({category['category_key']}): больше одного слова-связки"
            )
        if len(label) > MAX_LABEL_CHARS:
            problems.append(
                f"название {label!r} ({category['category_key']}) длиннее {MAX_LABEL_CHARS} символов"
            )
        if label in seen_labels:
            problems.append(
                f"дубль названия {label!r}: {seen_labels[label]} и {category['category_key']}"
            )
        seen_labels[label] = category["category_key"]

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

    problems.extend(check_sense_coverage(memberships))
    return problems


def check_sense_coverage(memberships: list[dict]) -> list[str]:
    """Инвариант из аудита: у слова с двумя и более значениями каждая связь знает значение.

    Иначе база не может ответить, в каком смысле слово стоит в категории, и
    генератор уровней собирает четвёрку из разных значений одного слова.
    Исключение — категории игры слов: там слово участвует написанием.
    """
    senses: dict[str, set[str]] = {}
    for membership in memberships:
        if membership.get("sense_key"):
            senses.setdefault(normalize_word(membership["word"]), set()).add(
                membership["sense_key"]
            )

    problems: list[str] = []
    for membership in memberships:
        word = normalize_word(membership["word"])
        if len(senses.get(word, ())) < 2 or membership.get("sense_key"):
            continue
        if membership["relation_type"] in WORDPLAY_RELATIONS:
            continue  # осознанное исключение, см. комментарий у WORDPLAY_RELATIONS
        problems.append(
            f"связь многозначного слова без значения: {word} -> "
            f"{membership['category_key']} (значения: {', '.join(sorted(senses[word]))}). "
            "Добавьте её в data/seed/_sense_map.json"
        )
    return problems


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    specs, ambiguous = load_seed()
    extra_senses, assignments = load_sense_map()
    categories = build_categories(specs)
    memberships = build_memberships(specs, ambiguous, extra_senses, assignments)

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
