"""Сборка проверенных четвёрок.

База хранит пулы, а игре нужны решения: категория в уровне — ровно четыре слова.
Четыре случайных слова из пула не годятся, потому что могут целиком лежать
в другой категории — тогда у уровня два корректных ответа.

Отбор идёт так:
  1. берём категории, готовые к обычным уровням (readiness ready/constrained);
  2. слова сортируем по игровой сложности: сначала самые заметные;
  3. каждую четвёрку-кандидата проверяем solver'ом;
  4. слова, уже занятые в другой четвёрке этой категории, не переиспользуем —
     иначе один уровень нельзя будет собрать из двух четвёрок одной темы.

Результат — `auto_validated`: solver прошёл, человек не смотрел. Статус
`human_approved` ставится только вручную.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from itertools import combinations

from .readiness import NORMAL_READY, NORMAL_STATUSES, QUARTET_SIZE
from .solver import category_pools, quartet_locally_unique

# Сколько четвёрок пытаться собрать на категорию: больше редко нужно, а перебор
# сочетаний растёт быстро
MAX_PER_CATEGORY = 3
# Ограничение перебора: из пула берём только самые заметные слова
CANDIDATE_POOL = 12


@dataclass(frozen=True)
class BuiltQuartet:
    category_key: str
    quartet_key: str
    words: tuple[str, ...]
    tier: str
    difficulty: float | None
    note: str


def _pool_for_category(conn: sqlite3.Connection, category_key: str) -> list[sqlite3.Row]:
    placeholders = ",".join("?" for _ in NORMAL_STATUSES)
    return list(
        conn.execute(
            f"""
            SELECT w.normalized AS normalized, s.sense_key AS sense_key,
                   m.gameplay_difficulty AS difficulty, m.obviousness_score AS obviousness
              FROM memberships m
              JOIN categories c ON c.id = m.category_id
              JOIN words w      ON w.id = m.word_id
              LEFT JOIN word_senses s ON s.id = m.sense_id
             WHERE c.category_key = ?
               AND m.review_status IN ({placeholders})
               AND m.semantic_status <> 'incorrect'
             ORDER BY COALESCE(m.gameplay_difficulty, 1.0), m.obviousness_score DESC,
                      w.normalized
            """,
            (category_key, *NORMAL_STATUSES),
        )
    )


def build(
    conn: sqlite3.Connection,
    *,
    max_per_category: int = MAX_PER_CATEGORY,
    only_category: str | None = None,
) -> tuple[list[BuiltQuartet], dict[str, int]]:
    """Собирает четвёрки по всем готовым категориям. Возвращает (четвёрки, статистика)."""
    pools = category_pools(conn)  # включая hard_only: чужая категория опасна любая
    placeholders = ",".join("?" for _ in NORMAL_READY)
    sql = f"SELECT category_key FROM categories WHERE readiness IN ({placeholders})"
    params: list[object] = list(NORMAL_READY)
    if only_category:
        sql += " AND category_key = ?"
        params.append(only_category)
    keys = [row["category_key"] for row in conn.execute(sql + " ORDER BY category_key", params)]

    built: list[BuiltQuartet] = []
    stats = {"категорий рассмотрено": 0, "категорий без четвёрок": 0, "четвёрок": 0}

    for category_key in keys:
        stats["категорий рассмотрено"] += 1
        rows = _pool_for_category(conn, category_key)[:CANDIDATE_POOL]
        senses = {row["normalized"]: row["sense_key"] for row in rows}
        difficulty = {
            row["normalized"]: row["difficulty"]
            for row in rows
            if row["difficulty"] is not None
        }
        available = [row["normalized"] for row in rows]
        used: set[str] = set()
        found = 0

        for group in combinations(available, QUARTET_SIZE):
            if found >= max_per_category:
                break
            if used & set(group):
                continue
            result = quartet_locally_unique(conn, category_key, list(group), pools=pools)
            if not result.unique:
                continue
            found += 1
            used.update(group)
            values = [difficulty[word] for word in group if word in difficulty]
            built.append(
                BuiltQuartet(
                    category_key=category_key,
                    quartet_key=f"{category_key}__{found}",
                    words=tuple(
                        f"{word}#{senses[word]}" if senses.get(word) else word for word in group
                    ),
                    tier="normal",
                    difficulty=round(sum(values) / len(values), 3) if values else None,
                    note=result.reason,
                )
            )
        if found == 0:
            stats["категорий без четвёрок"] += 1

    stats["четвёрок"] = len(built)
    return built, stats


def to_rows(built: list[BuiltQuartet]) -> list[dict[str, object]]:
    """Строки для data/quartets.csv."""
    return [
        {
            "quartet_key": item.quartet_key,
            "category_key": item.category_key,
            "tier": item.tier,
            "validation_state": "auto_validated",
            "local_check": "local_unique",
            # None, а не "": эти же строки идут и в валидацию QuartetInput, а пустая
            # строка не парсится как число — четвёрка молча уезжала в «пропущено».
            # В CSV None всё равно печатается пустой ячейкой (csv.DictWriter).
            "difficulty": item.difficulty,
            "words": " | ".join(item.words),
            "note": item.note,
        }
        for item in built
    ]
