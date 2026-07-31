"""Готовность категории к сборке уровней.

Категория в уровне — ровно четыре слова. Пул из двадцати связей ещё не значит,
что четвёрку можно собрать: пул может быть целиком из `hard_only`, может быть
короче четырёх слов уровня, а правило может быть парным или субъективным.

Аудит требовал два разных ответа:
  * можно ли из этой категории собрать нормальную четвёрку (P0);
  * насколько категория вообще готова к автоматической генерации (P1).

Оба выводятся из данных, руками не пишутся. Единственный ручной вход —
`curated_only` в `data/seed/_category_meta.json`.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass

# Слова уровня: связи, которые игрок увидит в обычном уровне
NORMAL_STATUSES = ("approved", "alternative")
PLAYABLE_STATUSES = ("approved", "alternative", "hard_only")

QUARTET_SIZE = 4
# Ниже этого пула категория начнёт повторяться уже через несколько уровней
THIN_PLAYABLE = 12
# Перекос в hard_only: категория формально играбельна, но лёгкий уровень из неё не собрать
MAX_HARD_SHARE = 0.5

# Статусы готовности, при которых категория идёт в обычные уровни
NORMAL_READY = ("ready", "constrained")


@dataclass(frozen=True)
class CategoryPools:
    category_key: str
    label: str
    approved: int
    alternative: int
    hard_only: int
    rejected: int

    @property
    def normal_pool(self) -> int:
        return self.approved + self.alternative

    @property
    def playable(self) -> int:
        return self.normal_pool + self.hard_only

    @property
    def hard_share(self) -> float:
        return self.hard_only / self.playable if self.playable else 0.0


def category_pools(conn: sqlite3.Connection) -> list[CategoryPools]:
    rows = conn.execute(
        """
        SELECT c.category_key AS category_key, c.label AS label,
               COUNT(m.id) FILTER (WHERE m.review_status = 'approved')    AS approved,
               COUNT(m.id) FILTER (WHERE m.review_status = 'alternative') AS alternative,
               COUNT(m.id) FILTER (WHERE m.review_status = 'hard_only')   AS hard_only,
               COUNT(m.id) FILTER (WHERE m.review_status = 'rejected')    AS rejected
          FROM categories c
          LEFT JOIN memberships m ON m.category_id = c.id
         GROUP BY c.id
         ORDER BY c.category_key
        """
    )
    return [
        CategoryPools(
            category_key=row["category_key"],
            label=row["label"],
            approved=int(row["approved"]),
            alternative=int(row["alternative"]),
            hard_only=int(row["hard_only"]),
            rejected=int(row["rejected"]),
        )
        for row in rows
    ]


def classify(pools: CategoryPools, curated_only: dict[str, str]) -> tuple[str, str]:
    """Возвращает (readiness, причина человекочитаемым текстом)."""
    manual = curated_only.get(pools.category_key)
    if manual:
        return "curated_only", manual

    if pools.playable < QUARTET_SIZE:
        return (
            "blocked",
            f"четвёрку не собрать: играбельных слов {pools.playable} из нужных {QUARTET_SIZE}",
        )
    if pools.normal_pool < QUARTET_SIZE:
        return (
            "hard_only",
            f"нормальную четвёрку не собрать: слов уровня {pools.normal_pool}, "
            f"весь остальной пул hard_only ({pools.hard_only})",
        )

    reasons: list[str] = []
    if pools.playable < THIN_PLAYABLE:
        reasons.append(f"тонкий пул: {pools.playable} играбельных слов, повторы начнутся быстро")
    if pools.hard_share > MAX_HARD_SHARE:
        reasons.append(f"перевес hard_only: {pools.hard_only} из {pools.playable}")
    if pools.approved < QUARTET_SIZE:
        reasons.append(f"approved-слов меньше четырёх ({pools.approved})")
    if reasons:
        return "constrained", "; ".join(reasons)
    return "ready", (
        f"слов уровня {pools.normal_pool} (approved {pools.approved}), "
        f"играбельных {pools.playable}"
    )


def derive(conn: sqlite3.Connection, curated_only: dict[str, str]) -> dict[str, int]:
    """Пересчитывает readiness всем категориям. Возвращает сводку по статусам."""
    from .repositories import set_category_readiness

    summary: dict[str, int] = {}
    for pools in category_pools(conn):
        readiness, reason = classify(pools, curated_only)
        row = conn.execute(
            "SELECT id FROM categories WHERE category_key = ?", (pools.category_key,)
        ).fetchone()
        set_category_readiness(conn, int(row["id"]), readiness, reason)
        summary[readiness] = summary.get(readiness, 0) + 1
    return summary
