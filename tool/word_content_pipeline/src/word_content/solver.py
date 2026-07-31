"""Solver единственности решения уровня.

Задача. Уровень — это N скрытых категорий по четыре слова. Игрок видит только
слова. Уровень корректен, только если слова раскладываются на четвёрки-категории
ровно одним способом: иначе игрок соберёт «правильный» с его точки зрения ответ,
а игра его не примет.

Почему это отдельный слой. База хранит пулы, а не решения. 516 пар категорий
делят четыре и больше играбельных слов (`JEWELRY STONES` и `GEMSTONES` — пятнадцать),
поэтому четвёрка из одной категории может целиком лежать в другой.

Реализация — exact cover перебором с отсечением: слов в уровне 4N (обычно 16–32),
кандидатных категорий на слово единицы, поэтому полный перебор дешевле любой эвристики.
Считаем максимум MAX_SOLUTIONS решений: чтобы отклонить уровень, достаточно двух.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field

from .normalization import normalize_word
from .readiness import NORMAL_STATUSES, PLAYABLE_STATUSES

QUARTET_SIZE = 4
MAX_SOLUTIONS = 2  # больше одного решения уже делает уровень непригодным


@dataclass
class SolverResult:
    unique: bool
    solutions: list[list[tuple[str, tuple[str, ...]]]] = field(default_factory=list)
    reason: str = ""

    @property
    def solution_count(self) -> int:
        return len(self.solutions)


def category_pools(
    conn: sqlite3.Connection, statuses: tuple[str, ...] = PLAYABLE_STATUSES
) -> dict[str, set[str]]:
    """category_key -> множество нормализованных слов, доступных в этом статусе."""
    placeholders = ",".join("?" for _ in statuses)
    rows = conn.execute(
        f"""
        SELECT c.category_key AS category_key, w.normalized AS normalized
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
          JOIN words w      ON w.id = m.word_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'
        """,
        statuses,
    )
    pools: dict[str, set[str]] = {}
    for row in rows:
        pools.setdefault(row["category_key"], set()).add(row["normalized"])
    return pools


def solve(
    words: list[str],
    pools: dict[str, set[str]],
    *,
    max_solutions: int = MAX_SOLUTIONS,
) -> SolverResult:
    """Ищет все разбиения слов уровня на четвёрки, лежащие целиком в одной категории."""
    normalized = [normalize_word(word) for word in words]
    if len(set(normalized)) != len(normalized):
        return SolverResult(unique=False, reason="в уровне есть повторяющиеся слова")
    if len(normalized) % QUARTET_SIZE != 0:
        return SolverResult(
            unique=False,
            reason=f"число слов {len(normalized)} не делится на {QUARTET_SIZE}",
        )

    level_words = set(normalized)
    # Кандидаты: категории, у которых в уровне есть хотя бы четыре своих слова
    candidates: list[tuple[str, frozenset[str]]] = []
    for category_key, pool in pools.items():
        shared = pool & level_words
        if len(shared) >= QUARTET_SIZE:
            candidates.append((category_key, frozenset(shared)))

    by_word: dict[str, list[int]] = {word: [] for word in normalized}
    for index, (_, shared) in enumerate(candidates):
        for word in shared:
            by_word[word].append(index)

    solutions: list[list[tuple[str, tuple[str, ...]]]] = []

    def search(
        remaining: frozenset[str],
        used_categories: frozenset[str],
        chosen: list[tuple[str, tuple[str, ...]]],
    ) -> None:
        if len(solutions) >= max_solutions:
            return
        if not remaining:
            solutions.append(list(chosen))
            return

        # Ветвимся по слову с наименьшим числом вариантов — стандартное отсечение
        # для exact cover: если у слова нет ни одной категории, ветка мертва сразу.
        pivot = min(remaining, key=lambda word: len(by_word[word]))
        for index in by_word[pivot]:
            category_key, shared = candidates[index]
            # Категория в уровне встречается один раз: две четвёрки одной категории —
            # это не разбиение уровня, а один и тот же ответ дважды.
            if category_key in used_categories:
                continue
            available = shared & remaining
            if len(available) < QUARTET_SIZE:
                continue
            for group in _combinations_with(available, pivot):
                chosen.append((category_key, tuple(sorted(group))))
                search(remaining - group, used_categories | {category_key}, chosen)
                chosen.pop()
                if len(solutions) >= max_solutions:
                    return

    search(frozenset(normalized), frozenset(), [])

    if not solutions:
        return SolverResult(unique=False, reason="уровень не раскладывается ни одним способом")
    if len(solutions) > 1:
        return SolverResult(
            unique=False,
            solutions=solutions,
            reason=f"найдено разбиений: {len(solutions)} и более — у уровня несколько ответов",
        )
    return SolverResult(unique=True, solutions=solutions, reason="разбиение единственное")


def _combinations_with(available: frozenset[str], pivot: str) -> list[frozenset[str]]:
    """Все четвёрки из available, обязательно включающие pivot."""
    rest = sorted(available - {pivot})
    result: list[frozenset[str]] = []
    n = len(rest)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                result.append(frozenset((pivot, rest[i], rest[j], rest[k])))
    return result


def quartet_is_unique(
    conn: sqlite3.Connection,
    category_key: str,
    words: list[str],
    *,
    pools: dict[str, set[str]] | None = None,
) -> SolverResult:
    """Проверяет одну четвёрку: не лежит ли она целиком в другой категории.

    Это условие уровня из одной категории. Уровень из нескольких категорий
    проверяется через solve() — там появляются перекрёстные разбиения.
    """
    pools = pools if pools is not None else category_pools(conn)
    normalized = {normalize_word(word) for word in words}
    owners = sorted(key for key, pool in pools.items() if normalized <= pool)
    if category_key not in owners:
        return SolverResult(
            unique=False,
            reason=f"четвёрка не лежит целиком в пуле категории {category_key}",
        )
    others = [key for key in owners if key != category_key]
    if others:
        return SolverResult(
            unique=False,
            reason="четвёрка целиком лежит также в: " + ", ".join(others),
        )
    return SolverResult(
        unique=True,
        solutions=[[(category_key, tuple(sorted(normalized)))]],
        reason="четвёрка однозначна: другой категории с этими четырьмя словами нет",
    )


def normal_pools(conn: sqlite3.Connection) -> dict[str, set[str]]:
    """Пулы для обычных уровней: без hard_only."""
    return category_pools(conn, NORMAL_STATUSES)
