#!/usr/bin/env python3
"""Второй источник контента для генератора: словарь оригинала (1025 уровней).

    reference/bwj-org/levels.jsonl --(этот скрипт)--> reference.snapshot.json
                                                                |
                                                        статика в браузере

Зачем он существует отдельным файлом, а не влит в базу
--------------------------------------------------------------------------
31.07 выгрузка `bubblewordjam.org` была влита в контентную базу прогоном
`run-002-bwj-org` и **откачена решением владельца**: чужой словарь в нашей базе
не храним. Замер, подтвердивший решение: импорт уронил медиану частотности базы
с 3.58 до 3.45 и поднял долю редких слов с 27% до 33%.

Это решение здесь не отменяется, а исполняется буквально. Выгрузка становится
ВТОРЫМ источником — отдельным снимком, отдельным файлом, отдельной кнопкой в
интерфейсе. Наша база от этого не меняется ни на одну связь: сравните
`content.snapshot.sha256` до и после прогона этого скрипта.

Что даёт второй источник: инструмент можно проверить на словаре, который в
живой игре реально отыгран 1025 уровней. Видно, где генератор упирается в
контент, а где в собственные правила — на нашей базе эти две причины неразличимы.

Что источник ЗНАЕТ и чего НЕ знает
--------------------------------------------------------------------------
Знает (прямо из выгрузки, без домысла):
  * какие слова оригинал считает ответом для категории — это и есть связь;
  * какая категория вложена в какую (`parent`/`depth`) — материал мета-пар;
  * сколько раз категория выходила в уровнях и с каким составом пула.

Не знает, и это влияет на генерацию:
  * СТАТУСОВ связи нет. Все связи приезжают `approved`: выгрузка — ключ ответов,
    в ней нет «верно, но не первая мысль». Значит, ловушки на этом источнике
    рождаются только из слов, живущих в двух категориях сразу (таких 44%),
    а не из размеченного слоя `alternative`.
  * ЗНАЧЕНИЙ слова (senses) нет. `bank` как берег и как учреждение — одно слово,
    и решатель единственности не может их развести.
  * РЕГИСТР слов потерян: в выгрузке всё в нижнем регистре. Поэтому имена
    собственные не размечены (`p = 0`), и гейт `minProperNounZipf` на этом
    источнике не работает — его роль берёт на себя общий пол частотности.
  * ОЧЕВИДНОСТЬ связи никто не оценивал — см. `membership_obviousness` ниже.

Всё это видно в интерфейсе на экране «База контента», а не спрятано в коде:
источник, у которого меньше слоёв, обязан объявлять об этом сам.

Запуск:  python3 scripts/export_reference_snapshot.py
Вывод:   web/src/data/reference.snapshot.json
         data/reference-derived/reference.snapshot.sha256
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DUMP = ROOT.parent.parent / "reference" / "bwj-org" / "levels.jsonl"
OUT_WEB = ROOT / "web" / "src" / "data" / "reference.snapshot.json"
OUT_HASH = ROOT / "data" / "reference-derived" / "reference.snapshot.sha256"

# Константы частотности те же, что у основного снимка: две шкалы узнаваемости
# в одном инструменте означали бы, что оценки двух источников несравнимы.
ZIPF_MAX = 7.0
TOP50K_ZIPF = 2.55
QUICKWIN_ZIPF = 3.0

STATUSES = ["approved", "alternative", "hard_only", "candidate", "rejected"]
RISK_FLAGS = [
    "obscure", "regional", "proper_noun", "multiword", "culturally_specific",
    "weak_relation", "highly_ambiguous", "sensitive", "possible_duplicate",
    "outdated_term", "trademark", "no_familiarity", "needs_sense",
]
CONFLICT_TYPES = ["do_not_pair", "needs_disjoint_words"]
QUARTET_TIERS = ["normal", "hard"]
SNAPSHOT_SCHEMA_VERSION = "snapshot-2.0"

APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


# --------------------------------------------------------------------------- #
# частотность
# --------------------------------------------------------------------------- #
def zipf_resolver():
    """Тот же резолвер, что в export_snapshot.py: частотность фразы — по самому
    редкому её слову. Два разных способа считать zipf сделали бы два источника
    несравнимыми ровно там, где их и хочется сравнить."""
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        print("ОШИБКА: нужен wordfreq (pip install wordfreq)", file=sys.stderr)
        raise

    split_re = re.compile(r"[ \-']+")
    cache: dict[str, tuple[float | None, bool]] = {}

    def resolve(text: str):
        norm = normalize(text)
        if norm in cache:
            return cache[norm]
        parts = [p for p in split_re.split(norm) if p]
        if not parts:
            result = (None, True)
        else:
            values = [zipf_frequency(p, "en") for p in parts]
            if any(v <= 0 for v in values):
                result = (None, True)
            else:
                whole = zipf_frequency(norm, "en") if len(parts) > 1 else values[0]
                result = (round(min(values) if len(parts) > 1 else whole, 2), False)
        cache[norm] = result
        return result

    return resolve


def lexicon_member(text: str) -> bool:
    return text == text.lower() and not re.search(r"[ \-'0-9]", text)


# --------------------------------------------------------------------------- #
# тип правила категории
# --------------------------------------------------------------------------- #
# Тип связи выводится из ИМЕНИ категории — единственного, что о правиле известно.
# Шаблоны продолжают список из tool/scripts/mine_bwj_org_knowledge.py: там они
# использовались для замера, здесь — для разметки. Порядок значим: первый
# сработавший выигрывает.
RELATION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("wordplay", re.compile(r"^(words? (before|after)|___)\b|\b___\b|\bword(s)? that\b")),
    ("part_of", re.compile(r"^(parts?|pieces?|components?) of\b|\bparts\b|\banatomy\b")),
    ("made_of", re.compile(r"^(made of|materials?)\b|\bmaterials\b|\bfabrics\b")),
    ("does_action", re.compile(r"\b(actions?|verbs?|movements?|moves|gestures?|"
                               r"exercises?|dances?)\b")),
    ("used_in", re.compile(r"\b(tools?|equipment|gear|supplies|utensils?|instruments?|"
                           r"gadgets?|accessories)\b")),
    ("has_property", re.compile(r"^(hard|soft|round|cold|hot|sweet|sour|loud|quiet|tall|"
                                r"small|big|long|short|fast|slow|shiny|sticky|flat|sharp|"
                                r"heavy|light|bright|dark|smelly|noisy|frozen|spicy)\b|"
                                r"\bthings that\b")),
    ("found_in", re.compile(r"\b(in|at|on) the\b|^(?:things )?(?:in|at|on)\b|"
                            r"\b(room|kitchen|garage|beach|forest|office|hospital|"
                            r"garden|park|zoo|farm|museum|library)\b")),
    ("associated_with", re.compile(r"\bthings\b|\bassociated\b|\brelated\b|\bwords\b")),
]

# Насколько тип правила добавляет работы игроку сверх узнавания слов.
# Числа взяты один в один из word_content_pipeline/category_difficulty.py:
# два разных прейскуранта на одну и ту же величину развели бы источники.
RELATION_RULE_COST = {
    "is_a": 0.00,
    "part_of": 0.01,
    "made_of": 0.01,
    "used_in": 0.03,
    "does_action": 0.03,
    "has_property": 0.05,
    "found_in": 0.07,
    "associated_with": 0.10,
    "wordplay": 0.12,
}


def relation_of(name: str) -> str:
    for relation, rx in RELATION_PATTERNS:
        if rx.search(name):
            return relation
    return "is_a"


# --------------------------------------------------------------------------- #
# тематическая сфера
# --------------------------------------------------------------------------- #
# Сферы обязаны называться ТАК ЖЕ, как в основной базе: фильтр тем в
# интерфейсе один на оба источника, и «без спорта» должно работать на обоих.
# Ключ ищется по всему имени категории, но решает последнее слово (голова
# имени): «beach sports» — это спорт, а не пляж. Отсюда два прохода.
THEME_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("food", ("food", "dish", "meal", "cuisine", "cooking", "baking", "bread", "cheese",
              "soup", "salad", "sauce", "spice", "herb", "dessert", "candy", "cake",
              "snack", "breakfast", "dinner", "lunch", "pizza", "pasta", "meat", "sushi",
              "drink", "beverage", "coffee", "tea", "cocktail", "wine", "beer", "juice",
              "fruit", "vegetable", "berries", "berry", "nut", "grain", "rice", "flavor")),
    ("animals", ("animal", "bird", "dog", "cat", "horse", "fish", "insect", "bug",
                 "reptile", "mammal", "pet", "wildlife", "dinosaur", "butterfly",
                 "spider", "snake", "frog", "bee", "shark", "whale", "bear")),
    ("plants", ("plant", "flower", "tree", "leaf", "leaves", "garden", "crop", "seed",
                "mushroom", "cactus", "grass", "moss", "vine", "bloom")),
    ("nature", ("nature", "mountain", "river", "lake", "desert", "forest", "weather",
                "storm", "cloud", "rain", "snow", "wind", "season", "volcano",
                "landscape", "rock", "stone", "mineral", "sky", "sunset")),
    ("ocean", ("ocean", "sea", "beach", "coral", "wave", "sailing", "marine", "harbor",
               "boat", "ship", "diving", "island")),
    ("space", ("space", "planet", "star", "galaxy", "astronomy", "moon", "comet",
               "rocket", "orbit", "cosmic", "nasa")),
    ("geography", ("country", "countries", "capital", "city", "cities", "continent",
                   "state", "province", "region", "nation", "border", "map", "flag")),
    ("places", ("place", "location", "town", "village", "street", "building", "room",
                "shop", "store", "market", "restaurant", "hotel", "airport", "station")),
    ("landmarks", ("landmark", "monument", "castle", "temple", "cathedral", "palace",
                   "tower", "bridge", "ruins", "wonders")),
    ("transport", ("transport", "vehicle", "car", "truck", "bus", "train", "plane",
                   "aircraft", "bike", "bicycle", "motorcycle", "driving", "traffic",
                   "engine", "aviation", "railway")),
    ("sports", ("sport", "game", "team", "match", "ball", "soccer", "football",
                "basketball", "baseball", "hockey", "tennis", "golf", "boxing",
                "running", "swimming", "skiing", "surfing", "climbing", "gym",
                "fitness", "yoga", "athlete", "olympic")),
    ("body", ("body", "anatomy", "bone", "muscle", "organ", "skin", "hair", "hand",
              "face", "eye", "tooth", "teeth", "blood", "brain", "heart")),
    ("medicine", ("medicine", "medical", "doctor", "hospital", "disease", "illness",
                  "symptom", "injury", "surgery", "drug", "pharmacy", "nurse",
                  "dental", "therapy", "health", "virus")),
    ("clothing", ("clothing", "clothes", "shirt", "dress", "shoe", "boot", "hat",
                  "coat", "sock", "pants", "jacket", "wear", "outfit", "uniform")),
    ("fashion", ("fashion", "style", "makeup", "cosmetic", "jewelry", "manicure",
                 "hairstyle", "runway", "beauty", "perfume")),
    ("home", ("home", "house", "furniture", "kitchen", "bathroom", "bedroom", "living",
              "cleaning", "laundry", "appliance", "decor", "household", "garage",
              "closet", "chore")),
    ("tools", ("tool", "hardware", "workshop", "hammer", "screw", "nail", "saw",
               "drill", "repair", "construction", "carpentry", "welding")),
    ("materials", ("material", "metal", "plastic", "glass", "wood", "fabric", "cloth",
                   "leather", "paper", "ceramic", "concrete", "alloy")),
    ("technology", ("technology", "tech", "computer", "software", "internet", "phone",
                    "app", "digital", "robot", "code", "coding", "data", "gadget",
                    "electronics", "keyboard", "screen", "network")),
    ("science", ("science", "physics", "chemistry", "biology", "chemical", "element",
                 "experiment", "lab", "atom", "molecule", "energy", "gravity",
                 "genetics", "enzyme", "biochemistry", "math", "geometry", "algebra")),
    ("education", ("school", "class", "classroom", "student", "teacher", "college",
                   "university", "exam", "lesson", "study", "homework", "campus",
                   "education", "subject", "degree")),
    ("jobs", ("job", "profession", "worker", "career", "occupation", "employee",
              "boss", "office", "workplace", "salary", "resume")),
    ("trades", ("trade", "plumber", "electrician", "mechanic", "blacksmith",
                "locksmith", "mason", "builder", "craftsman")),
    ("business", ("business", "money", "bank", "finance", "market", "economy",
                  "company", "corporate", "investment", "stock", "sale", "shopping",
                  "price", "tax", "currency", "coin")),
    ("law", ("law", "legal", "court", "judge", "crime", "police", "prison", "lawyer",
             "trial", "justice", "jury")),
    ("history", ("history", "historical", "ancient", "medieval", "war", "battle",
                 "empire", "revolution", "dynasty", "viking", "pirate", "knight",
                 "castle siege", "century", "era")),
    ("mythology", ("myth", "mythology", "legend", "god", "goddess", "dragon", "fairy",
                   "monster", "folklore", "magic", "wizard", "witch")),
    ("religion", ("religion", "church", "prayer", "bible", "temple", "sacred", "holy",
                  "ritual", "faith", "monk", "saint")),
    ("culture", ("culture", "tradition", "custom", "festival", "ceremony", "holiday",
                 "celebration", "wedding", "funeral", "etiquette")),
    ("art", ("art", "painting", "drawing", "sculpture", "artist", "gallery", "craft",
             "pottery", "sketch", "canvas", "color", "colour", "paint", "design")),
    ("music", ("music", "song", "band", "singer", "guitar", "piano", "drum", "note",
               "melody", "concert", "album", "genre", "orchestra", "opera")),
    ("media", ("media", "movie", "film", "tv", "television", "show", "series", "actor",
               "cinema", "news", "comic", "cartoon", "anime", "podcast", "video")),
    ("entertainment", ("entertainment", "party", "toy", "circus", "carnival", "puzzle",
                       "board game", "card game", "casino", "gambling", "theme park",
                       "amusement", "playground", "fun")),
    ("hobbies", ("hobby", "hobbies", "knitting", "sewing", "fishing", "camping",
                 "hiking", "gardening", "collecting", "scrapbooking", "photography",
                 "birdwatching", "model")),
    ("language", ("language", "word", "letter", "alphabet", "grammar", "spelling",
                  "phrase", "slang", "idiom", "synonym", "verb", "noun", "adjective",
                  "abbreviation", "translation")),
    ("people", ("people", "person", "family", "friend", "child", "baby", "name",
                "celebrity", "famous", "president", "king", "queen", "leader")),
    ("time", ("time", "day", "days", "month", "year", "calendar", "clock", "hour",
              "minute", "week", "date", "schedule", "season")),
    ("properties", ("shape", "shapes", "size", "texture", "pattern", "property",
                    "measurement", "unit", "number", "quantity", "direction",
                    "temperature", "weight", "length", "speed")),
    ("farming", ("farm", "farming", "agriculture", "harvest", "barn", "livestock",
                 "tractor", "ranch", "dairy", "orchard")),
    ("brands", ("brand", "logo", "trademark", "company name", "make", "makes")),
    ("species", ("species", "breed", "variety", "genus", "family tree", "type of")),
]

THEME_FALLBACK = "other"


def theme_of(name: str) -> str:
    """Сфера категории. Сначала по голове имени, затем по всему имени.

    Порядок важен: `beach sports` — спорт, а не океан, и решает это последнее
    слово. Если голова ничего не сказала, ищем ключ где угодно в имени.

    Чего не опознали — уходит в `other/<голова имени>`, а не в общий `other`,
    и вот почему. Словарём наших сфер размечается меньше половины источника:
    у оригинала 6714 категорий с длиннейшим хвостом (`glowing`, `hunch`,
    `pond life`, `stochastic processes`), и таблица ключей его не догонит.
    Но сфера в инструменте работает не только фильтром: по ней считается
    разнообразие уровня — штраф за повтор темы при отборе категорий и
    `themeVariety` в оценке интереса. Свалив половину базы в одно значение,
    мы сказали бы генератору, что `dolphin`, `bowling` и `flu` — одна тема.
    Это неправда, и она бы стоила уровню разнообразия и балла интереса.
    Голова имени грубее нашей сферы, но она различает то, что различимо.
    """
    words = name.split()
    head = words[-1] if words else name
    for theme, keys in THEME_KEYWORDS:
        if head in keys or head.rstrip("s") in keys:
            return theme
    for theme, keys in THEME_KEYWORDS:
        for key in keys:
            if re.search(rf"\b{re.escape(key)}", name):
                return theme
    tail = re.sub(r"[^a-z]", "", head)
    return f"{THEME_FALLBACK}/{tail}" if tail else THEME_FALLBACK


# --------------------------------------------------------------------------- #
# очевидность связи
# --------------------------------------------------------------------------- #
# Выгрузка очевидность НЕ оценивает: она перечисляет ответы, а не ранжирует их.
# Поставить 1.0 было бы враньём в пользу источника — очевидность с весом 0.45
# входит в Clarity, и уровни референса стали бы «понятнее» наших просто потому,
# что данных меньше.
#
# Поэтому берётся нейтральный якорь — медиана approved-связей нашей базы (0.78),
# та же константа, что стоит в generator.ts как OBVIOUSNESS_UNKNOWN, — и
# двигается двумя величинами, которые в выгрузке РЕАЛЬНО измеримы:
#
#   core_share  доля выходов категории, где это слово было в четвёрке. Категория,
#               выходившая один раз, даёт 1.0 всем словам (различать нечем);
#               у выходившей десять раз видно ядро и периферию пула.
#   homes       в скольких категориях слово вообще встречается. Слово из пяти
#               категорий не «вспоминается первым» ни для одной из них.
OBVIOUSNESS_ANCHOR = 0.78
AMBIGUITY_STEP = 0.15
OBVIOUSNESS_FLOOR = 0.30
OBVIOUSNESS_CEILING = 0.90


def membership_obviousness(core_share: float, homes: int) -> float:
    value = OBVIOUSNESS_ANCHOR * core_share / (1 + AMBIGUITY_STEP * (homes - 1))
    return round(min(OBVIOUSNESS_CEILING, max(OBVIOUSNESS_FLOOR, value)), 2)


# --------------------------------------------------------------------------- #
# сложность категории
# --------------------------------------------------------------------------- #
# Шкала обязана совпадать с основной базой (там 0.1-0.7, медиана 0.35, потолок
# туториала 0.2), иначе один и тот же гейт означал бы на двух источниках разное.
#
# Чем считаем. В пайплайне сложность категории складывается из трёх слагаемых:
# очевидность надписи (вес 0.60), знакомость слов (0.25) и тип правила. Главного
# слагаемого здесь нет — очевидность не измерена (см. выше), и подставлять
# вместо неё константу значило бы прибавить всем одно и то же число. Поэтому
# для этого источника сложность держится на знакомости четвёрки, а тип правила
# приезжает надбавкой по тому же прейскуранту.
#
# Якоря линейной шкалы сняты с самой выгрузки, а не назначены: zipf 5.30 — это
# уровень `colors` и `compass` с первого уровня оригинала, 2.90 — уровень
# категорий из последней сотни. Проверка, что шкала не выдумана: корреляция
# полученной сложности с номером уровня, где категория впервые вышла в
# оригинале, +0.31 — то есть шкала независимо согласуется с тем, как сам
# оригинал расставлял категории по кривой.
DIFFICULTY_EASY_ZIPF = 5.30
DIFFICULTY_HARD_ZIPF = 2.90
DIFFICULTY_MIN = 0.10
DIFFICULTY_MAX = 0.70
DIFFICULTY_SPAN = 0.60


def category_difficulty(quartet_zipf: float | None, relation: str, label: str) -> float | None:
    """Сложность категории 0.1-0.7 или None, если считать не из чего."""
    if quartet_zipf is None:
        return None
    span = DIFFICULTY_EASY_ZIPF - DIFFICULTY_HARD_ZIPF
    value = DIFFICULTY_MIN + (DIFFICULTY_EASY_ZIPF - quartet_zipf) / span * DIFFICULTY_SPAN
    value += RELATION_RULE_COST.get(relation, 0.07)
    if "___" in label:
        value += 0.12
    return round(min(DIFFICULTY_MAX, max(DIFFICULTY_MIN, value)), 2)


# --------------------------------------------------------------------------- #
# сборка снимка
# --------------------------------------------------------------------------- #
def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", normalize(name)).strip("_") or "category"


def load_dump(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(
            f"ОШИБКА: нет выгрузки {path}\n"
            "Она не хранится в git (правило /reference/ в .gitignore).\n"
            "Собрать заново: python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025"
        )
    levels = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
              if line.strip()]
    return sorted(levels, key=lambda x: x["level"])


def build(levels: list[dict]) -> dict:
    resolve_zipf = zipf_resolver()

    # ------------------------------------------------------------------ #
    # 1. свод по категориям
    # ------------------------------------------------------------------ #
    pool: dict[str, set[str]] = defaultdict(set)          # категория → слова пула
    appearances: Counter[str] = Counter()                 # категория → выходов в уровнях
    word_hits: dict[str, Counter[str]] = defaultdict(Counter)   # категория → слово → выходов
    first_level: dict[str, int] = {}
    parents: dict[str, set[str]] = defaultdict(set)       # ребёнок → наблюдённые родители
    meta_children: set[str] = set()

    for level in levels:
        for entry in level["categories"]:
            name = normalize(entry["name"])
            appearances[name] += 1
            first_level.setdefault(name, level["level"])
            for raw in entry["words"]:
                word = normalize(raw)
                pool[name].add(word)
                word_hits[name][word] += 1
            if entry.get("parent"):
                parents[name].add(normalize(entry["parent"]))
                meta_children.add(name)

    names = sorted(pool)

    # ------------------------------------------------------------------ #
    # 2. словарь
    # ------------------------------------------------------------------ #
    all_words: set[str] = set()
    for words in pool.values():
        all_words |= words
    # имена вложенных категорий: на поле они такие же пузыри, и в словаре обязаны
    # быть, даже если сами по себе ни в чей пул не попали
    all_words |= {name for name in meta_children}

    word_list = sorted(all_words)
    word_index = {w: i for i, w in enumerate(word_list)}

    out_words = []
    for text in word_list:
        z, unknown = resolve_zipf(text)
        out_words.append({
            "t": text,
            "n": text,
            "z": z,
            "u": 1 if unknown else 0,
            "l": 1 if lexicon_member(text) else 0,
            # регистр в выгрузке потерян, размечать имена собственные нечем:
            # см. шапку файла. Ноль здесь — «не знаем», а не «не бывает».
            "p": 0,
            "tok": len(re.split(r"[ \-']+", text)),
        })

    homes: Counter[str] = Counter()
    for words in pool.values():
        for word in words:
            homes[word] += 1

    # ------------------------------------------------------------------ #
    # 3. категории
    # ------------------------------------------------------------------ #
    used_keys: set[str] = set()
    cats = []
    cat_index: dict[str, int] = {}
    for name in names:
        key = slugify(name)
        if key in used_keys:
            suffix = 2
            while f"{key}_{suffix}" in used_keys:
                suffix += 1
            key = f"{key}_{suffix}"
        used_keys.add(key)

        relation = relation_of(name)
        zs = sorted((z for z in (resolve_zipf(w)[0] for w in pool[name]) if z is not None),
                    reverse=True)
        quartet = zs[:4]
        quartet_zipf = sum(quartet) / len(quartet) if len(quartet) == 4 else None
        size = len(pool[name])

        cat_index[name] = len(cats)
        cats.append({
            "k": key,
            "l": name.upper(),
            # Правила текстом у источника нет — есть факт: вот столько раз
            # категория выходила и вот такой у неё пул. Пустая строка вместо
            # этого читалась бы как «правило неизвестно», а оно известно ровно
            # настолько, насколько его показал оригинал.
            "r": f"Пул оригинала: {size} слов, категория выходила "
                 f"{appearances[name]} раз, впервые на уровне {first_level[name]}",
            "rel": relation,
            "th": theme_of(name),
            "d": category_difficulty(quartet_zipf, relation, name),
            # 4-5 слов — пул, из которого четвёрка собирается единственным
            # способом или почти. Это не «не годится», это «выбора нет».
            "rd": "ready" if size >= 6 else "constrained",
            # поля ниже основного снимка не имеют: они про этот источник
            "ref_levels": appearances[name],
            "ref_first_level": first_level[name],
        })

    # ------------------------------------------------------------------ #
    # 4. связи
    # ------------------------------------------------------------------ #
    out_memberships = []
    for name in names:
        ci = cat_index[name]
        relation = cats[ci]["rel"]
        total = appearances[name]
        for word in sorted(pool[name]):
            core_share = word_hits[name][word] / total if total else 1.0
            out_memberships.append([
                word_index[word], ci,
                0,                                    # approved: выгрузка — ключ ответов
                1.0,                                  # fit: оригинал засчитал это слово
                membership_obviousness(core_share, homes[word]),
                relation,
                None,                                 # значений слова источник не знает
                None,                                 # игровой сложности связи тоже
                0,                                    # risk-флагов нет
            ])

    # ------------------------------------------------------------------ #
    # 5. мета-потенциал
    # ------------------------------------------------------------------ #
    # У оригинала вложенность размечена явно (`parent`), и это сильнее, чем
    # догадка «имя категории существует как слово». Берём и то и другое:
    # наблюдённые пары — как факт, совпадение имени со словом — как возможность.
    memberships_by_word: dict[int, set[int]] = defaultdict(set)
    for wi, ci, *_ in out_memberships:
        memberships_by_word[wi].add(ci)

    meta_capable = []
    for name in names:
        wi = word_index.get(name)
        if wi is None:
            continue
        hosts = set(memberships_by_word.get(wi, set()))
        hosts |= {cat_index[p] for p in parents.get(name, set()) if p in cat_index}
        hosts.discard(cat_index[name])
        if not hosts:
            continue
        meta_capable.append({
            "category": cat_index[name], "word": wi, "hosts": sorted(hosts),
        })

    snapshot = {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "statuses": STATUSES,
        "risk_flags": RISK_FLAGS,
        "conflict_types": CONFLICT_TYPES,
        "quartet_tiers": QUARTET_TIERS,
        "constants": {
            "zipf_max": ZIPF_MAX,
            "top50k_zipf": TOP50K_ZIPF,
            "quickwin_zipf": QUICKWIN_ZIPF,
        },
        "categories": cats,
        "words": out_words,
        # значений слова у источника нет — пустой список честнее выдуманных
        "senses": [],
        "memberships": out_memberships,
        "meta_capable": meta_capable,
        # запретов на пары источник не объявляет; живой фильтр по Жаккару в
        # генераторе работает и без них
        "conflicts": [],
        "quartets": [],
    }

    zs = [w["z"] for w in out_words if w["z"] is not None]
    playable = sum(1 for w in out_words if w["z"] is not None and w["z"] >= 3.75)
    pool_sizes = [len(pool[name]) for name in names]
    snapshot["stats"] = {
        "categories": len(cats),
        "categories_ready": sum(1 for c in cats if c["rd"] == "ready"),
        "categories_constrained": sum(1 for c in cats if c["rd"] == "constrained"),
        "words": len(out_words),
        "senses": 0,
        "memberships": len(out_memberships),
        "conflicts": 0,
        "quartets": 0,
        "approved": len(out_memberships),
        "alternative": 0,
        "hard_only": 0,
        "frequency_unknown_words": sum(w["u"] for w in out_words),
        "words_below_top50k": sum(1 for z in zs if z < TOP50K_ZIPF),
        "words_above_generator_floor": playable,
        "multi_token_words": sum(1 for w in out_words if w["tok"] > 1),
        "meta_capable_categories": len(meta_capable),
        "meta_capable_with_host": len(meta_capable),
        "categories_with_4plus_approved": sum(1 for s in pool_sizes if s >= 4),
        "trap_capable_words": sum(1 for n in homes.values() if n >= 2),
        "themes_mapped": len({c["th"] for c in cats if not c["th"].startswith("other")}),
        "categories_theme_mapped": sum(
            1 for c in cats if not c["th"].startswith("other")),
        "zipf_median_x100": round(statistics.median(zs) * 100) if zs else 0,
        "pool_size_median_x100": round(statistics.median(pool_sizes) * 100),
        # то, чего нет у основного снимка: размер самого источника
        "reference_levels": len(levels),
        "reference_category_occurrences": sum(appearances.values()),
        "reference_meta_children": len(meta_children),
    }
    return snapshot


def canonical(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dump", help="путь к levels.jsonl выгрузки оригинала")
    args = parser.parse_args()

    path = Path(args.dump) if args.dump else DUMP
    levels = load_dump(path)
    print(f"источник: {path} ({len(levels)} уровней)")

    snapshot = build(levels)
    snapshot["content_snapshot_hash"] = hashlib.sha256(
        canonical({k: v for k, v in snapshot.items() if k != "stats"}).encode("utf-8")
    ).hexdigest()

    OUT_WEB.parent.mkdir(parents=True, exist_ok=True)
    OUT_HASH.parent.mkdir(parents=True, exist_ok=True)
    OUT_WEB.write_text(canonical(snapshot) + "\n", encoding="utf-8")
    OUT_HASH.write_text(snapshot["content_snapshot_hash"] + "\n", encoding="utf-8")

    stats = snapshot["stats"]
    print(f"снимок: {OUT_WEB.relative_to(ROOT)}  "
          f"{OUT_WEB.stat().st_size / 1_048_576:.2f} МБ")
    print(f"хеш: {snapshot['content_snapshot_hash'][:16]}…")
    for key in ("categories", "words", "memberships", "meta_capable_categories",
                "trap_capable_words", "words_above_generator_floor",
                "frequency_unknown_words"):
        print(f"  {key}: {stats[key]}")
    print(f"  медиана zipf: {stats['zipf_median_x100'] / 100:.2f}")
    print(f"  медиана пула: {stats['pool_size_median_x100'] / 100:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
