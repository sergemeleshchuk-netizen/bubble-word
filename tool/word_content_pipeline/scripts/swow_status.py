#!/usr/bin/env python3
"""Проставляет статусы связей по человеческим ассоциациям SWOW.

Зачем: статус связи должен отвечать на вопрос «вспомнит ли игрок это значение
слова, увидев такую категорию». Раньше на этот вопрос отвечал я. Теперь —
данные Small World of Words: 12 282 стимула, ответы живых людей.

Как считается. Профиль слова — то, что люди отвечают на него, плюс стимулы,
на которые отвечают им. Слова одной категории имеют похожие профили, даже если
напрямую друг с другом не ассоциируются, поэтому профиль слова сравнивается
с профилем категории (без самого слова).

Как назначается статус. У слова из нескольких категорий сравниваются его же
категории между собой: ratio = оценка / лучшая оценка этого слова.

  ratio >= 0.55 и оценка >= 0.05          approved     вспоминает первым
  оценка >= 0.25 (при любом ratio)        approved     сидит в категории плотно
  ratio >= 0.05 и оценка >= 0.02          alternative  узнаёт, но не первым: ловушка
  иначе                                   hard_only    сам не догадается

Порог alternative низкий намеренно. SWOW отвечает на стимул доминирующим значением,
поэтому вторичные значения известных слов он занижает: на "apple" почти никто
не отвечает "Microsoft", хотя компанию знают все. Низкий порог возвращает такие
связи в ловушки, а не в hard_only.

Ручная разметка значений (data/seed/_ambiguous.json) сильнее данных: у омонимов
значение известно точно, а SWOW о нём может молчать (bridge как зубной мост).

Ограничения сверху остаются прежними: неочевидная категория не поднимается выше
alternative, редкое слово не поднимается до approved, rejected не трогается.

Датасет SWOW лежит локально (reference/swow/, research/personal use, в git не идёт).
В репозиторий попадают только производные решения — data/review_decisions.csv.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import pickle
import statistics
import sys
from collections import defaultdict
from pathlib import Path

PIPE = Path(__file__).resolve().parents[1]
REPO = PIPE.parents[1]
SWOW_AGG = REPO / "reference" / "swow" / "swow_agg.pkl"

sys.path.insert(0, str(PIPE / "src"))
sys.path.insert(0, str(PIPE / "scripts"))

from build_seed import load_seed, load_sense_map  # noqa: E402
from word_content.familiarity import familiarity  # noqa: E402
from word_content.normalization import NormalizationError, normalize_word  # noqa: E402


def canon(word: str) -> str:
    """Та же нормализация, что и в базе: иначе слова с типографскими знаками не сойдутся."""
    try:
        return normalize_word(word)
    except NormalizationError:
        return word.strip().lower()


BWD_WEIGHT = 0.5
RATIO_APPROVED = 0.55
RATIO_ALTERNATIVE = 0.05
MIN_SCORE_APPROVED = 0.05
ABS_APPROVED = 0.25  # слово сидит в категории плотно даже при более сильном конкуренте
MIN_SCORE_ALTERNATIVE = 0.02
MIN_SCORE_FLOOR = 0.0  # в прозрачной категории пол действует всегда: игрок доходит рассудком
RARE_FAMILIARITY = 0.357
REJECT_FLOOR = 0.20  # ниже этого слово практически не встречается в письменном английском

# --------------------------------------------------------------- абсолютные пороги
#
# Замечание аудита: SWOW сравнивает категории слова только между собой, поэтому
# объективно очевидная связь редкого слова уезжала в hard_only —
# xylophone -> MUSICAL INSTRUMENTS, Sahara -> DESERTS, key -> KEYCHAIN THINGS.
# Абсолютная оценка считается независимо от других категорий этого слова:
#
#   salience = W_OBVIOUS * очевидность категории + W_FAMILIAR * знакомость слова
#
# Очевидность отвечает за «понятно ли правило категории», знакомость — за «знает ли
# игрок слово». Одно компенсирует другое: xylophone редкое в текстах, но категория
# MUSICAL INSTRUMENTS настолько прозрачна, что игрок соберёт её сразу.
W_OBVIOUS = 0.6
W_FAMILIAR = 0.4
FAMILIAR_FULL = 0.7  # знакомость 0.7 и выше считается полной (это zipf ~4.9)

# Пороги подобраны по спискам аудита: они должны поднимать названные там связи
# (xylophone -> MUSICAL INSTRUMENTS, key -> KEYCHAIN THINGS, camera -> THINGS WITH
# SCREENS) и при этом не превращать всю базу в approved — ловушки `alternative`
# и материал для сложных уровней `hard_only` игре нужны не меньше.
SALIENCE_APPROVED = 0.80
SALIENCE_ALTERNATIVE = 0.60

# Категория, правило которой само себя объясняет (MUSICAL INSTRUMENTS, DESSERTS,
# SEASONS): игрок соберёт её, даже если отдельное слово редко встречается в текстах.
# Частотность измеряет употребимость, а не узнаваемость: xylophone знают все.
SELF_EVIDENT_OBVIOUSNESS = 0.90
SELF_EVIDENT_MIN_FAMILIARITY = 0.28

# Категории игры слов оцениваются только относительно: там играет написание слова,
# а не узнаваемость значения, и абсолютный пол дал бы ложный approved
# ('key' частотное, но категория ___ BOARD — это загадка, а не очевидность).
WORDPLAY_RELATIONS = {"phrase_before", "phrase_after"}


def salience(obviousness: float, word_familiarity: float | None) -> float | None:
    """Абсолютная заметность связи: 0..1. None, если знакомость неизвестна."""
    if word_familiarity is None:
        return None
    familiar = min(word_familiarity / FAMILIAR_FULL, 1.0)
    return W_OBVIOUS * obviousness + W_FAMILIAR * familiar


def absolute_floor(
    value: float | None, obviousness: float, word_familiarity: float | None
) -> str | None:
    """Минимальный статус, ниже которого связь опускать нельзя."""
    if value is None or word_familiarity is None:
        return None
    if value >= SALIENCE_APPROVED:
        return "approved"
    if (
        obviousness >= SELF_EVIDENT_OBVIOUSNESS
        and word_familiarity >= SELF_EVIDENT_MIN_FAMILIARITY
    ):
        return "approved"
    if value >= SALIENCE_ALTERNATIVE:
        return "alternative"
    return None


TIER_ORDER = {"hard_only": 0, "alternative": 1, "approved": 2}


def gameplay_difficulty(value: float | None, base_difficulty: float) -> float | None:
    """Игровая сложность связи: отдельная ось от семантики и от знакомости.

    Складывается из того, насколько связь незаметна, и из базовой сложности
    категории. Нужна генератору уровней, чтобы строить кривую сложности.
    """
    if value is None:
        return None
    return round(min(max(0.5 * (1.0 - value) + 0.5 * base_difficulty, 0.0), 1.0), 3)


SEMANTIC_REVIEW = PIPE / "data" / "seed" / "_semantic_review.csv"


def load_semantic_review() -> dict[tuple[str, str], dict[str, str]]:
    """Читает _semantic_review.csv. Ключ — (слово или '*', category_key)."""
    if not SEMANTIC_REVIEW.exists():
        return {}
    lines = [
        line
        for line in SEMANTIC_REVIEW.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    result: dict[tuple[str, str], dict[str, str]] = {}
    for row in csv.DictReader(lines):
        word = (row["word"] or "").strip()
        key = word if word == "*" else canon(word)
        result[(key, row["category_key"].strip())] = {
            "semantic_status": row["semantic_status"].strip(),
            "note": (row.get("note") or "").strip(),
        }
    return result


def build_vectors(fwd: dict, bwd: dict, words: set[str]) -> dict[str, dict[str, float]]:
    vectors: dict[str, dict[str, float]] = {}
    for word in words:
        vec: dict[str, float] = defaultdict(float)
        for response, strength in fwd.get(word, {}).items():
            vec[response] += strength
        for cue, strength in bwd.get(word, {}).items():
            vec[cue] += strength * BWD_WEIGHT
        vec.pop(word, None)
        if vec:
            norm = math.sqrt(sum(v * v for v in vec.values()))
            vectors[word] = {k: v / norm for k, v in vec.items()}
    return vectors


def category_profiles(vectors: dict, pool: dict[str, list[str]]) -> dict[str, tuple[dict, int]]:
    profiles = {}
    for key, words in pool.items():
        acc: dict[str, float] = defaultdict(float)
        used = 0
        for word in words:
            vec = vectors.get(word)
            if not vec:
                continue
            used += 1
            for k, v in vec.items():
                acc[k] += v
        profiles[key] = (dict(acc), used)
    return profiles


def score(vectors: dict, profiles: dict, word: str, key: str) -> float | None:
    """Косинус между профилем слова и профилем категории без этого слова."""
    vec = vectors.get(word)
    if vec is None:
        return None
    acc, used = profiles.get(key, ({}, 0))
    if used - 1 <= 0:
        return None

    rest = {k: v - vec.get(k, 0.0) for k, v in acc.items()}
    rest = {k: v for k, v in rest.items() if v > 1e-9}
    norm = math.sqrt(sum(v * v for v in rest.values()))
    if norm == 0:
        return None

    # vec уже нормирован, rest нормируем здесь
    dot = sum(v * rest.get(k, 0.0) for k, v in vec.items())
    return dot / norm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memberships", default=str(PIPE / "data" / "membership_candidates.jsonl"))
    parser.add_argument(
        "--categories",
        help="categories.jsonl прогона: метаданные категорий, которых нет в seed. "
             "Без него у импортированной категории неизвестны очевидность и базовая "
             "сложность, и политика роняет её пул в hard_only целиком — ровно та "
             "ошибка, на которую указал аудит.",
    )
    parser.add_argument("--output", default=str(PIPE / "data" / "review_decisions.csv"))
    parser.add_argument("--preview", action="store_true", help="только показать, не писать файл")
    args = parser.parse_args()

    if not SWOW_AGG.exists():
        sys.exit(
            f"Нет агрегата SWOW: {SWOW_AGG}\n"
            "Собрать: python3 tool/scripts/swow_source.py build (датасет локальный)"
        )

    data = pickle.loads(SWOW_AGG.read_bytes())
    fwd, bwd = data["fwd"], data["bwd"]

    mem = [json.loads(line) for line in Path(args.memberships).open(encoding="utf-8")]
    specs, ambiguous = load_seed()
    obvious_category = {s["category_key"]: bool(s.get("approve")) for s in specs}
    category_obviousness = {s["category_key"]: float(s["obviousness"]) for s in specs}
    category_difficulty = {s["category_key"]: float(s["base_difficulty"]) for s in specs}

    # Метаданные категорий прогона. Категории оригинала считаем прозрачными:
    # это группы живой игры, где игроки их фактически разгадывают. Очевидность
    # выводится из базовой сложности (проще группа — очевиднее), а не назначается.
    if args.categories:
        for line in Path(args.categories).open(encoding="utf-8"):
            if not line.strip():
                continue
            cat = json.loads(line)
            key = cat["category_key"]
            difficulty = float(cat.get("base_difficulty") or 0.4)
            category_difficulty.setdefault(key, difficulty)
            category_obviousness.setdefault(key, round(max(0.3, 1.0 - difficulty), 2))
            obvious_category.setdefault(key, True)
    semantic_review = load_semantic_review()

    # Слова с разведёнными значениями: у них абсолютный пол не работает, потому что
    # частотность считается по написанию, а не по значению. 'monitor' частотное слово,
    # но monitor -> LIZARDS игрок сам не назовёт. Такие связи судит ручная разметка.
    senses_per_word: dict[str, set[str]] = defaultdict(set)
    for m in mem:
        if m.get("sense_key"):
            senses_per_word[canon(m["word"])].add(m["sense_key"])
    multi_sense = {word for word, keys in senses_per_word.items() if len(keys) > 1}

    # Ручная разметка значений омонимов сильнее данных: у слова с разведёнными
    # значениями SWOW отвечает доминирующим смыслом и про остальные молчит.
    # Источники — _ambiguous.json и статусы из _sense_map.json.
    manual = {
        (canon(row["word"]), row["category_key"]): row["review_status"]
        for row in ambiguous
        if row.get("review_status") in ("approved", "alternative", "hard_only")
    }
    _, sense_assignments = load_sense_map()
    for word, by_category in sense_assignments.items():
        for category_key, value in by_category.items():
            if value.get("review_status"):
                manual[(word, category_key)] = value["review_status"]

    pool: dict[str, list[str]] = defaultdict(list)
    for m in mem:
        pool[m["category_key"]].append(canon(m["word"]))
    words = {w for ws in pool.values() for w in ws}

    vectors = build_vectors(fwd, bwd, words)
    profiles = category_profiles(vectors, pool)

    scores: dict[int, float | None] = {}
    by_word: dict[str, list[float]] = defaultdict(list)
    for i, m in enumerate(mem):
        s = score(vectors, profiles, canon(m["word"]), m["category_key"])
        scores[i] = s
        if s is not None:
            by_word[canon(m["word"])].append(s)
    best = {w: max(v) for w, v in by_word.items() if v}

    rows = []
    stats = defaultdict(int)
    for i, m in enumerate(mem):
        word = canon(m["word"])
        key = m["category_key"]
        word_familiarity = familiarity(word)
        obviousness = category_obviousness.get(key, m.get("obviousness_score", 0.7))
        abs_score = salience(obviousness, word_familiarity)
        floor = absolute_floor(abs_score, obviousness, word_familiarity)

        # Пул, выверенный вручную (флаг A в файле темы), — сам по себе абсолютный
        # сигнал: если правило категории прозрачно и слово не редкое, игрок соберёт
        # эту связь. Ключевая правка по аудиту: раньше такую связь могло опустить
        # относительное сравнение категорий слова между собой.
        if (
            obvious_category.get(key, False)
            and word_familiarity is not None
            and word_familiarity >= RARE_FAMILIARITY
        ):
            floor = "approved"

        # Пол не применяется там, где частотность написания не отвечает за
        # узнаваемость значения: у многозначного слова судит ручная разметка,
        # у категории игры слов — само правило загадка, а не очевидность.
        if m.get("sense_key") or word in multi_sense or m["relation_type"] in WORDPLAY_RELATIONS:
            floor = None

        if word_familiarity is not None and word_familiarity < REJECT_FLOOR:
            decision = "rejected"
            source = f"частотность {word_familiarity:.3f}: слово почти не встречается в английском"
        elif m.get("review_status") == "rejected":
            decision, source = "rejected", "оставлено как есть"
        elif word_familiarity is None:
            # P0 аудита: нет данных о частотности — связь не может быть играбельной
            decision = "candidate"
            source = "частотность не посчитана: связь закрыта до ручной проверки"
            stats["без частотности"] += 1
        else:
            s = scores[i]
            top = best.get(word)
            if s is None or not top:
                # Слова вне SWOW (многословные, имена собственные, редкие) решаются
                # абсолютной оценкой. Раньше здесь всё, кроме A-категорий, падало
                # в hard_only — отсюда и брались «все пустыни hard_only».
                if m.get("review_status") in ("approved", "alternative", "hard_only"):
                    decision = m["review_status"]
                    source = "нет данных SWOW: сохранена ручная разметка"
                else:
                    decision = floor or "hard_only"
                    source = (
                        f"нет данных SWOW: абсолютная заметность {abs_score:.2f} "
                        f"(очевидность {obviousness:.2f}, знакомость {word_familiarity:.2f})"
                    )
                stats["без SWOW"] += 1
            else:
                ratio = s / top if top > 0 else 0.0
                if (ratio >= RATIO_APPROVED and s >= MIN_SCORE_APPROVED) or s >= ABS_APPROVED:
                    decision = "approved"
                elif ratio >= RATIO_ALTERNATIVE and s >= MIN_SCORE_ALTERNATIVE:
                    decision = "alternative"
                else:
                    decision = "hard_only"
                source = f"SWOW: оценка {s:.3f}, доля от лучшей категории слова {ratio:.2f}"
                stats["по SWOW"] += 1

                # Потолок остался только для многозначных слов: там SWOW отвечает
                # доминирующим значением, и относительная оценка вторичного значения
                # завышена быть не может, а вот занижена — сплошь.
                if (
                    decision == "approved"
                    and not obvious_category.get(key, False)
                    and floor != "approved"
                ):
                    decision, source = "alternative", source + "; категория неочевидная"

                # Абсолютный пол сильнее относительной оценки: категория может быть
                # прозрачной сама по себе, даже если SWOW-ассоциаций почти нет.
                if floor and TIER_ORDER[floor] > TIER_ORDER[decision]:
                    decision = floor
                    source += f"; абсолютная заметность {abs_score:.2f} поднимает до {floor}"

        override = manual.get((word, key))
        if override and override != decision:
            decision = override
            source = "ручная разметка значения (SWOW не различает это значение)"
            stats["ручных переопределений"] += 1

        semantic = semantic_review.get((word, key)) or semantic_review.get(("*", key))
        if semantic and semantic["semantic_status"] == "incorrect" and decision != "rejected":
            decision = "rejected"
            source = f"семантика: {semantic['note']}"
            stats["отклонено по семантике"] += 1

        stats[decision] += 1
        rows.append(
            {
                "membership_id": "",
                "word": m["word"],
                "normalized": word,
                "sense_key": m.get("sense_key") or "",
                "category_key": key,
                "current_status": m.get("review_status", "candidate"),
                "decision": decision,
                "semantic_status": semantic["semantic_status"] if semantic else "unreviewed",
                "gameplay_difficulty": gameplay_difficulty(
                    abs_score, category_difficulty.get(key, 0.5)
                )
                if abs_score is not None
                else "",
                "review_comment": source,
            }
        )

    print(f"связей: {len(rows)}")
    for k in ("approved", "alternative", "hard_only", "rejected", "candidate"):
        if stats.get(k):
            print(f"  {k}: {stats[k]}")
    print(f"  из них решено по SWOW: {stats['по SWOW']}, без данных SWOW: {stats['без SWOW']}")
    if scores:
        vals = [v for v in scores.values() if v is not None]
        print(f"  медиана оценки: {statistics.median(vals):.4f}")

    if args.preview:
        return

    out = Path(args.output)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"записано: {out}")


if __name__ == "__main__":
    main()
