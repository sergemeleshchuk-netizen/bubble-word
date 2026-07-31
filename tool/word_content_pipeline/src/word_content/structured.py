"""Структурные категории: где четвёрка — не любые четыре слова из пула.

OPPOSITES — это не пул из двадцати четырёх слов, а двенадцать пар. Четвёрка
для такой категории собирается только как две полные пары: `hot/cold` +
`up/down`, но никогда `hot/cold/up/left`. То же самое у последовательностей
(DAYS OF THE WEEK — подряд идущие дни) и у отношений ключ-значение
(COUNTRY–CAPITAL — целые пары «страна + её столица»).

Модуль отвечает на один вопрос: допустима ли конкретная четвёрка слов для
конкретной категории с точки зрения её структуры. Для обычных категорий ответ
всегда «да» — структуры нет, ограничивает только пул.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field

QUARTET_SIZE = 4

# free      — обычная категория: годятся любые четыре слова пула
# pairs     — четвёрка = две полные пары (OPPOSITES, COUNTRY–CAPITAL)
# sequence  — четвёрка = четыре подряд идущих элемента (DAYS, MONTHS, SCALE)
STRUCTURES = ("free", "pairs", "sequence")


@dataclass(frozen=True)
class StructuredGroup:
    """Одна связка внутри категории: пара, тройка или элемент последовательности."""

    group_key: str
    # слово -> роль в связке. Роли осмысленные: 'a'/'b' у пары,
    # 'country'/'capital' у ключ-значение, номер позиции у последовательности.
    roles: dict[str, str]

    @property
    def words(self) -> frozenset[str]:
        return frozenset(self.roles)


@dataclass
class CategoryStructure:
    category_key: str
    structure: str = "free"
    groups: list[StructuredGroup] = field(default_factory=list)
    # для sequence: слова в каноническом порядке
    order: list[str] = field(default_factory=list)

    def allows(self, words: frozenset[str]) -> tuple[bool, str]:
        """Допустима ли четвёрка. Возвращает (да/нет, причина отказа)."""
        if len(words) != QUARTET_SIZE:
            return False, f"в четвёрке должно быть {QUARTET_SIZE} слова, получено {len(words)}"
        if self.structure == "free":
            return True, ""
        if self.structure == "pairs":
            covered: list[StructuredGroup] = [
                group for group in self.groups if group.words <= words
            ]
            union: set[str] = set()
            for group in covered:
                union |= group.words
            if union != set(words):
                return False, "четвёрка не собирается из целых пар категории"
            if len(covered) != 2:
                return False, f"нужны ровно две пары, найдено {len(covered)}"
            return True, ""
        if self.structure == "sequence":
            positions = [self.order.index(word) for word in words if word in self.order]
            if len(positions) != QUARTET_SIZE:
                return False, "не все слова четвёрки есть в последовательности"
            positions.sort()
            if positions[-1] - positions[0] != QUARTET_SIZE - 1:
                return False, "слова не идут подряд в последовательности"
            return True, ""
        return False, f"неизвестная структура {self.structure!r}"


class StructureIndex:
    """Структуры всех категорий базы. Отсутствие записи = обычная категория."""

    def __init__(self, structures: dict[str, CategoryStructure] | None = None) -> None:
        self._by_key = structures or {}

    def get(self, category_key: str) -> CategoryStructure:
        return self._by_key.get(category_key) or CategoryStructure(category_key=category_key)

    def allows(self, category_key: str, words: frozenset[str]) -> tuple[bool, str]:
        return self.get(category_key).allows(words)

    @property
    def structured_keys(self) -> list[str]:
        return sorted(
            key for key, value in self._by_key.items() if value.structure != "free"
        )

    def __len__(self) -> int:
        return len(self._by_key)


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return (
        conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ?", (name,)
        ).fetchone()
        is not None
    )


def load(conn: sqlite3.Connection) -> StructureIndex:
    """Читает структуры из базы.

    Источников два, и это не дубль: `category_pair_groups` — исторический слой
    пар, `structured_relations` — общий слой с ролями и последовательностями.
    Второй перекрывает первый там, где заполнен.
    """
    structures: dict[str, CategoryStructure] = {}

    rows = conn.execute(
        """
        SELECT c.category_key AS category_key, g.group_key AS group_key,
               w.normalized AS word, g.slot AS slot
          FROM category_pair_groups g
          JOIN categories c ON c.id = g.category_id
          JOIN words w      ON w.id = g.word_id
         ORDER BY c.category_key, g.group_key, g.slot
        """
    )
    grouped: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        key = (row["category_key"], row["group_key"])
        grouped.setdefault(key, {})[row["word"]] = "a" if int(row["slot"]) == 1 else "b"
    for (category_key, group_key), roles in grouped.items():
        structure = structures.setdefault(
            category_key, CategoryStructure(category_key=category_key, structure="pairs")
        )
        structure.structure = "pairs"
        structure.groups.append(StructuredGroup(group_key=group_key, roles=roles))

    if _table_exists(conn, "structured_relations"):
        rows = conn.execute(
            """
            SELECT c.category_key AS category_key, r.structure AS structure,
                   r.group_key AS group_key, w.normalized AS word,
                   r.role AS role, r.position AS position
              FROM structured_relations r
              JOIN categories c ON c.id = r.category_id
              JOIN words w      ON w.id = r.word_id
             ORDER BY c.category_key, r.position, r.group_key, r.role
            """
        )
        fresh: dict[str, CategoryStructure] = {}
        for row in rows:
            category_key = row["category_key"]
            structure = fresh.setdefault(
                category_key,
                CategoryStructure(category_key=category_key, structure=row["structure"]),
            )
            if structure.structure == "sequence":
                structure.order.append(row["word"])
                continue
            existing = next(
                (g for g in structure.groups if g.group_key == row["group_key"]), None
            )
            if existing is None:
                structure.groups.append(
                    StructuredGroup(group_key=row["group_key"], roles={row["word"]: row["role"]})
                )
            else:
                existing.roles[row["word"]] = row["role"]
        structures.update(fresh)

    return StructureIndex(structures)
