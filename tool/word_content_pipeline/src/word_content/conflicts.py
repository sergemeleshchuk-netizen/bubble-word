"""Конфликты категорий: какие пары нельзя ставить в один уровень.

Замечание аудита: 516 пар категорий делят четыре и больше играбельных слов
(`JEWELRY STONES` и `GEMSTONES` — пятнадцать). Значит четвёрка из одной может
целиком лежать в другой, и у уровня появляется второй корректный ответ.

Конфликты считаются из данных, а не пишутся руками. Ручной слой (`do_not_pair`
в `data/seed/_category_meta.json`) только дополняет: там пары, где пересечение
меньше порога, но категории всё равно неотличимы для игрока.
"""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from dataclasses import dataclass

from .readiness import PLAYABLE_STATUSES, QUARTET_SIZE

# Порог: пересечение из четырёх слов уже даёт целую четвёрку в обеих категориях
MIN_OVERLAP = QUARTET_SIZE
EXAMPLES_IN_NOTE = 20


@dataclass(frozen=True)
class Overlap:
    category_a: str
    category_b: str
    pool_a: int
    pool_b: int
    words: tuple[str, ...]

    @property
    def count(self) -> int:
        return len(self.words)

    @property
    def severity(self) -> str:
        """P0 — четвёрка почти наверняка соберётся в обеих; P1 — риск ниже."""
        share = max(self.count / self.pool_a, self.count / self.pool_b)
        if self.count >= 8 or share >= 0.6:
            return "P0"
        return "P1"


def find_overlaps(
    conn: sqlite3.Connection, min_overlap: int = MIN_OVERLAP
) -> list[Overlap]:
    """Все пары категорий с пересечением не меньше порога.

    Считаем через инвертированный индекс слово -> категории: пар категорий
    полмиллиона, а слов, живущих в нескольких категориях, три с половиной тысячи.
    """
    placeholders = ",".join("?" for _ in PLAYABLE_STATUSES)
    rows = conn.execute(
        f"""
        SELECT c.category_key AS category_key, w.normalized AS normalized
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
          JOIN words w      ON w.id = m.word_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'
        """,
        PLAYABLE_STATUSES,
    )

    pools: dict[str, set[str]] = defaultdict(set)
    by_word: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        pools[row["category_key"]].add(row["normalized"])
        by_word[row["normalized"]].add(row["category_key"])

    shared: dict[tuple[str, str], set[str]] = defaultdict(set)
    for word, keys in by_word.items():
        if len(keys) < 2:
            continue
        ordered = sorted(keys)
        for i, left in enumerate(ordered):
            for right in ordered[i + 1 :]:
                shared[(left, right)].add(word)

    result = [
        Overlap(
            category_a=left,
            category_b=right,
            pool_a=len(pools[left]),
            pool_b=len(pools[right]),
            words=tuple(sorted(words)),
        )
        for (left, right), words in shared.items()
        if len(words) >= min_overlap
    ]
    result.sort(key=lambda item: (-item.count, item.category_a, item.category_b))
    return result


def to_rows(overlaps: list[Overlap]) -> list[dict[str, object]]:
    """Строки для data/category_conflicts.csv."""
    return [
        {
            "category_a": item.category_a,
            "category_b": item.category_b,
            "conflict_type": "do_not_pair",
            "origin": "derived",
            "overlap_count": item.count,
            "overlap_words": " | ".join(item.words[:EXAMPLES_IN_NOTE]),
            "severity": item.severity,
            "note": (
                f"общих играбельных слов {item.count}; "
                f"пулы {item.pool_a} и {item.pool_b}"
            ),
        }
        for item in overlaps
    ]
