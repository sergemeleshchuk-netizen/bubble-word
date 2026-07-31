#!/usr/bin/env python3
"""Выгрузка bubblewordjam.org -> прогон-источник для контентного пайплайна.

Что делает: превращает `reference/bwj-org/levels.jsonl` в пару файлов, которые
пайплайн умеет импортировать наравне с seed-контентом и AI-прогонами:

    tool/word_content_pipeline/data/runs/run-002-bwj-org/categories.jsonl
    tool/word_content_pipeline/data/runs/run-002-bwj-org/memberships.jsonl

Почему через прогон, а не прямо в базу. У прогона сохраняется провенанс
(`source: bwj_reference_v1`), связи заезжают статусом `candidate` — то есть
в игру не идут, пока статус не назначит общая политика (`swow_status.py`), —
и на них действуют те же гейты приёмки, что на всё остальное: частотность,
блок-лист, обязательное значение у многозначного слова.

Что берём и чего не берём:

  * слова категории — берём, это словарь;
  * структуру вложенности (MEASUREMENTS содержит TIME/LENGTH/WEIGHT) — берём,
    это самое ценное: имя вложенной категории является словом в родителе, а
    значит у нас появляется материал для мета-пузырей, которого в базе почти
    нет (178 рёбер на 1120 категорий);
  * готовые четвёрки — НЕ берём. Четвёрка это раскладка уровня, а не контент;
    выдавать чужую раскладку запрещает проверка REFERENCE_NOVELTY в валидаторе.
    Наш генератор пересобирает слова заново.

Категории оригинала считаем «прозрачными» (флаг approve): это категории живой
игры, где игроки их фактически разгадывают, — их очевидность подтверждена
практикой лучше, чем у придуманных нами. Базовая сложность выводится из
частотности пула, а не назначается на глаз.

Запуск:  python3 tool/scripts/bwj_to_run.py [--min-pool 4] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRAPE = ROOT / "reference" / "bwj-org" / "levels.jsonl"
RUN_DIR = ROOT / "tool" / "word_content_pipeline" / "data" / "runs" / "run-002-bwj-org"
PIPE = ROOT / "tool" / "word_content_pipeline"
BASE_JSON = ROOT / "tool" / "data" / "categories.json"

SOURCE = "bwj_reference_v1"
RUN_META = RUN_DIR / "run_meta.json"

# Слова, которые в игру не идут ни при каких условиях: служебные части речи.
# В оригинале они живут в категориях игры слов («местоимения», «слова-глаголы»),
# и как ассоциативный контент бесполезны.
FUNCTION_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "of", "to", "in", "on", "at", "by",
    "for", "with", "as", "is", "am", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had", "will", "would", "shall", "should",
    "can", "could", "may", "might", "must", "i", "you", "he", "she", "it", "we",
    "they", "me", "him", "her", "us", "them", "my", "your", "his", "its", "our",
    "their", "this", "that", "these", "those", "not", "no", "yes", "so", "than",
    "then", "there", "here", "what", "which", "who", "whom", "whose", "when",
    "where", "why", "how",
}

APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


def category_key(name: str) -> str:
    key = re.sub(r"[^a-z0-9]+", "_", normalize(name)).strip("_")
    return key or "unnamed"


def load_scrape() -> list[dict]:
    levels = []
    for line in SCRAPE.read_text(encoding="utf-8").splitlines():
        if line.strip():
            levels.append(json.loads(line))
    return sorted(levels, key=lambda x: x["level"])


def load_existing_keys() -> set[str]:
    """Ключи категорий ДРУГИХ источников: их описание не перезаписываем.

    Сверяемся именно с источниками пайплайна (seed и прогон мета-хабов), а не с
    выгрузкой `tool/data/categories.json`. Выгрузка собирается ИЗ базы, в которой
    уже лежит наш собственный импорт, — и на втором запуске конвертер решал, что
    все 5726 его категорий «уже есть», выдавал 134 штуки и правки до базы не
    доезжали. Классическая петля: сверяться с результатом своей же работы.

    Зачем сверка вообще: у seed-категории сложность, правило и тема выставлены
    руками, а у нас они эвристические. `import-categories` делает upsert по
    ключу, то есть без этой проверки импорт затирал бы курированное описание.
    """
    keys: set[str] = set()
    sources = [
        PIPE / "data" / "categories.jsonl",
        PIPE / "data" / "runs" / "run-001-meta-hubs" / "categories.jsonl",
    ]
    for path in sources:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            cat = json.loads(line)
            keys.add(cat["category_key"])
            keys.add(category_key(cat["label"]))
    return keys


def polysemous_words() -> set[str]:
    """Слова, у которых в базе разведено 2+ значения.

    Такое слово нельзя влить в новую категорию, не сказав, В КАКОМ значении:
    `scale` в MAP LEGEND и в BATHROOM ITEMS — разные слова, и приёмка базы это
    проверяет блокирующе. Значение из выгрузки не восстановить (сайт отдаёт
    написание), поэтому такие связи уезжают в отдельный файл на разведение
    значений, а не в базу. Слово при этом уже в базе есть — теряем только новую
    привязку, не словарь.
    """
    import sqlite3

    # База одна и лежит в git; запасной путь на копию в БАЗА-СЛОВ убран.
    db = PIPE / "database" / "content.sqlite"
    if not db.exists():
        return set()
    # База живёт в режиме WAL: при существующих -wal/-shm файлах mode=ro её не
    # открывает, поэтому обычное соединение как запасной путь (ничего не пишем).
    try:
        conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        conn.execute("select 1 from sqlite_master limit 1")
    except sqlite3.OperationalError:
        conn = sqlite3.connect(str(db))
    rows = conn.execute(
        "select w.normalized from word_senses s join words w on w.id = s.word_id "
        "group by w.normalized having count(distinct s.sense_key) >= 2"
    ).fetchall()
    conn.close()
    return {r[0] for r in rows}


def blocklist():
    sys.path.insert(0, str(PIPE / "src"))
    from word_content.blocklist import Blocklist  # noqa: E402

    return Blocklist.load(None)


def zipf_of():
    from wordfreq import zipf_frequency

    def resolve(word: str) -> float:
        parts = [p for p in re.split(r"[ \-']+", word) if p]
        if not parts:
            return 0.0
        values = [zipf_frequency(p, "en") for p in parts]
        return round(min(values) if len(parts) > 1 else values[0], 2)

    return resolve


def theme_of(name: str) -> str:
    """Тема категории: грубая эвристика по ключевым словам имени.

    Точность здесь не критична — тема нужна генератору только чтобы не ставить
    на уровень пять категорий одной сферы. Неопознанное уезжает в `misc`, и это
    честнее, чем выдумывать сходство.
    """
    n = normalize(name)
    buckets = {
        "food": ("food", "fruit", "vegetable", "meat", "dish", "cook", "bake", "drink",
                 "snack", "dessert", "sauce", "cheese", "bread", "candy", "soup", "pizza"),
        "animals": ("animal", "bird", "fish", "insect", "dog", "cat", "pet", "reptile",
                    "mammal", "sea creature", "bug", "breed"),
        "nature": ("tree", "flower", "plant", "weather", "ocean", "mountain", "river",
                   "forest", "season", "sky", "rock", "stone", "garden"),
        "geography": ("country", "city", "capital", "continent", "landmark", "state",
                      "island", "place", "flag", "map"),
        "sports": ("sport", "game", "team", "ball", "olympic", "athlet", "fitness"),
        "entertainment": ("movie", "film", "music", "song", "singer", "band", "tv",
                          "show", "actor", "cartoon", "instrument", "dance", "art"),
        "home": ("house", "home", "room", "kitchen", "furniture", "bathroom", "bedroom",
                 "cleaning", "laundry", "tool"),
        "jobs": ("job", "profession", "worker", "career", "office", "doctor", "school",
                 "teacher", "police", "military"),
        "body": ("body", "organ", "bone", "muscle", "face", "hand", "health", "medical",
                 "illness", "disease"),
        "clothing": ("cloth", "wear", "shoe", "hat", "dress", "fashion", "accessor",
                     "fabric", "jewel"),
        "transport": ("transport", "vehicle", "car", "plane", "train", "boat", "ship",
                      "road", "travel"),
        "science": ("science", "space", "planet", "star", "chemi", "physic", "math",
                    "number", "element", "biolog", "computer", "tech"),
        "language": ("word", "letter", "language", "grammar", "verb", "noun", "phrase",
                     "rhyme", "spell", "opposite", "synonym"),
    }
    for theme, needles in buckets.items():
        if any(needle in n for needle in needles):
            return theme
    return "misc"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-pool", type=int, default=4,
                        help="минимум слов в пуле, иначе категория не создаётся")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not SCRAPE.exists():
        print(f"ОШИБКА: нет выгрузки {SCRAPE}", file=sys.stderr)
        return 1

    levels = load_scrape()
    existing = load_existing_keys()
    blocked = blocklist()
    zipf = zipf_of()
    ambiguous = polysemous_words()
    needs_sense = []

    # 1. Собираем пулы: имя категории -> слова (по всем уровням, где она встречалась)
    pools: dict[str, set[str]] = defaultdict(set)
    labels: dict[str, str] = {}
    # 2. Иерархия: родитель -> дети (имя ребёнка = слово-мета в родителе)
    children: dict[str, set[str]] = defaultdict(set)
    meta_words: dict[str, set[str]] = defaultdict(set)
    levels_seen: dict[str, list[int]] = defaultdict(list)

    for level in levels:
        for cat in level["categories"]:
            key = category_key(cat["name"])
            labels.setdefault(key, cat["name"].upper())
            levels_seen[key].append(level["level"])
            for word in cat["words"]:
                pools[key].add(normalize(word))
            for meta in cat.get("meta_words", []):
                meta_words[key].add(normalize(meta))
                children[key].add(category_key(meta))

    stats = defaultdict(int)
    categories_out = []
    memberships_out = []

    for key, words in sorted(pools.items()):
        if key in existing:
            stats["категория уже в базе"] += 1
            # слова всё равно предлагаем: пул существующей категории расширяется
            new_key = key
        else:
            new_key = key
        clean = []
        for word in sorted(words):
            if word in FUNCTION_WORDS:
                stats["служебное слово"] += 1
                continue
            if blocked.check(word) is not None:
                stats["блок-лист"] += 1
                continue
            if len(word) > 24:
                stats["слишком длинное"] += 1
                continue
            z = zipf(word)
            if z <= 0:
                stats["нет частотности"] += 1
                continue
            if word in ambiguous:
                stats["нужно значение слова"] += 1
                needs_sense.append({"word": word, "category_key": key,
                                    "label": labels[key]})
                continue
            clean.append((word, z))

        if len(clean) < args.min_pool:
            stats["пул меньше минимума"] += 1
            continue

        zs = [z for _, z in clean]
        # Базовая сложность из частотности пула: медиана zipf 5.0 -> 0.1,
        # медиана 3.0 -> 0.6. Та же шкала, что у seed-категорий (0.1-0.6).
        #
        # Пол 0.3 — важнее самой формулы. Частотность слов говорит о словах, а не
        # о том, насколько прозрачно ПРАВИЛО категории. Проверено на живом
        # примере: у категории CARDINAL пул `robin, bird, direction, vatican` из
        # частотных слов, формула дала d=0.15, и она уехала на уровень-туториал —
        # хотя это загадка на омонимах, которую оригинал вводит гораздо позже.
        # Пока категорию не посмотрел человек, считаем её не проще средней:
        # содержимое доступно генератору, но на туториал и в лёгкие декады
        # первыми идут курированные категории с честно выставленной сложностью.
        IMPORT_DIFFICULTY_FLOOR = 0.3
        median = statistics.median(zs)
        difficulty = round(min(0.6, max(IMPORT_DIFFICULTY_FLOOR,
                                        0.1 + (5.0 - median) * 0.25)), 2)

        if key not in existing:
            categories_out.append({
                "category_key": new_key,
                "label": labels[key],
                "rule": f"What belongs to the group «{labels[key].title()}» "
                        f"as used in the original game",
                "relation_type": "associated_with",
                "theme": theme_of(labels[key]),
                "base_difficulty": difficulty,
            })
            stats["новых категорий"] += 1

        for word, z in clean:
            memberships_out.append({
                "word": word,
                "language": "en",
                "part_of_speech": "noun",
                "is_proper_noun": bool(re.match(r"^[A-Z]", labels[key])) and False,
                "category_key": new_key,
                "relation_type": "associated_with",
                "reason": f"В оригинале «{word}» стоит в группе «{labels[key].title()}» "
                          f"(уровни {', '.join(map(str, levels_seen[key][:3]))})",
                "fit_score": 0.95,
                # очевидность из частотности: политика статусов её использует
                "obviousness_score": round(min(0.95, max(0.2, (z - 1.5) / 4.0)), 2),
                "source": SOURCE,
                "review_status": "candidate",
            })
            stats["связей"] += 1

    print("СВОДКА КОНВЕРТАЦИИ")
    for k in sorted(stats):
        print(f"   {k:26} {stats[k]}")
    print(f"   {'категорий на выходе':26} {len(categories_out)}")
    print(f"   {'связей на выходе':26} {len(memberships_out)}")
    print(f"   {'мета-связей (родитель-ребёнок)':26} {sum(len(v) for v in children.values())}")

    if args.dry_run:
        print("\n--dry-run: файлы не записаны")
        return 0

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    (RUN_DIR / "categories.jsonl").write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in categories_out),
        encoding="utf-8")
    (RUN_DIR / "memberships.jsonl").write_text(
        "".join(json.dumps(m, ensure_ascii=False) + "\n" for m in memberships_out),
        encoding="utf-8")
    if needs_sense:
        (RUN_DIR / "needs_sense.jsonl").write_text(
            "".join(json.dumps(n, ensure_ascii=False) + "\n" for n in needs_sense),
            encoding="utf-8")
    RUN_META.write_text(json.dumps({
        "source": SOURCE,
        "origin": "bubblewordjam.org (фанатская расшифровка ответов оригинала)",
        "levels": [levels[0]["level"], levels[-1]["level"]],
        "levels_count": len(levels),
        "note": "Взяты словарь и структура категорий. Готовые четвёрки НЕ переносятся: "
                "раскладку собирает наш генератор, проверка REFERENCE_NOVELTY "
                "не даёт выдать чужую четвёрку.",
        "hierarchy": {parent: sorted(kids) for parent, kids in sorted(children.items())
                      if kids},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"\n→ {RUN_DIR.relative_to(ROOT)}/")
    print("Дальше: политика статусов и пересборка базы")
    print(f"   cd {PIPE.relative_to(ROOT)}")
    print("   .venv/bin/python scripts/swow_status.py \\")
    print("       --memberships data/runs/run-002-bwj-org/memberships.jsonl \\")
    print("       --output data/runs/run-002-bwj-org/review_decisions.csv")
    print("   bash scripts/rebuild_all.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
