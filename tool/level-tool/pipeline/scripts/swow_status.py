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

from build_seed import load_seed  # noqa: E402
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

    # Ручная разметка второстепенных значений омонимов: SWOW про них часто молчит
    manual = {
        (canon(row["word"]), row["category_key"]): row["review_status"]
        for row in ambiguous
        if row.get("review_status") in ("alternative", "hard_only")
    }

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
        if word_familiarity is not None and word_familiarity < REJECT_FLOOR:
            decision = "rejected"
            source = f"частотность {word_familiarity:.3f}: слово почти не встречается в английском"
        elif m.get("review_status") == "rejected":
            decision, source = "rejected", "оставлено как есть"
        else:
            s = scores[i]
            top = best.get(word)
            if s is None or not top:
                # Запасной путь для слов вне SWOW: та же логика, что и раньше —
                # очевидная категория плюс нередкое слово дают approved,
                # всё прочее уходит в hard_only.
                fam = familiarity(word)
                rare = fam is not None and fam < RARE_FAMILIARITY
                if m.get("review_status") in ("approved", "alternative", "hard_only"):
                    decision = m["review_status"]
                elif obvious_category.get(key, False) and not rare:
                    decision = "approved"
                else:
                    decision = "hard_only"
                source = "нет данных SWOW: решено по правилам категории и частотности"
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

                # потолки: неочевидная категория и редкое слово не дают approved
                if decision == "approved" and not obvious_category.get(key, False):
                    decision, source = "alternative", source + "; категория неочевидная"
                fam = familiarity(word)
                if decision == "approved" and fam is not None and fam < RARE_FAMILIARITY:
                    decision, source = "alternative", source + "; слово редкое"

                # Пол: в прозрачной категории игрок доходит рассудком, даже если
                # ассоциации слабые. Банк ассоциируется с деньгами, а не со школой,
                # но что это здание в городе — сообразит любой.
                if (
                    decision == "hard_only"
                    and obvious_category.get(key, False)
                    and not (fam is not None and fam < RARE_FAMILIARITY)
                    and s >= MIN_SCORE_FLOOR
                ):
                    decision = "alternative"
                    source += "; прозрачная категория, игрок доходит рассудком"

        override = manual.get((word, key))
        if override and override != decision:
            decision = override
            source = "ручная разметка значения (SWOW не различает это значение)"
            stats["ручных переопределений"] += 1

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
