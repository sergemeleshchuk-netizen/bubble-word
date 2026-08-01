"""Мета-пары: чья надпись годится в чужую четвёрку.

Мета-механика оригинала устроена просто и от этого работает: собранная
категория лопается и оставляет на поле пузырь, который нужен другой категории
того же уровня. На уровне 4 записи группа `doctor` выпускает слово «doctor»,
и оно оказывается четвёртым пузырём группы `jobs`.

Из 56 разобранных мета-связей записи **52 устроены именно так**: текст пузыря
совпадает с именем категории-источника. Остальные четыре (`ruler` из `length`,
`scales` из `weight`, `thermometer` из `temperature`, `cards` из `card suits`)
требуют знания «какой предмет представляет эту категорию» — это отдельная
задача, и здесь она не решается.

Отсюда определение мета-пары, которое умеет считать машина:

    правило A имеет готовую четвёрку, одно из слов которой является
    НАДПИСЬЮ правила B  ->  на уровне B выпускает этот пузырь для A.

Четвёрка A при этом не пересобирается: берётся та, что уже прошла валидаторы.
Замер показал, что пересборка почти ничего не добавляет (471 пара против 451),
то есть платить за неё нечем.

Чего здесь намеренно нет:

``надписи оригинала``
    Надпись с ``origin = 'reference_backfill'`` — авторский текст записи
    («compass», «doctor», «clothes»), привязанный к нашему правилу при разборе
    видео. Взять его как имя нашей группы значит выдать чужую формулировку за
    свою. Поэтому источник обязан иметь собственную надпись. Цена запрета
    видна в счётчиках: 451 пара до него, 163 после.

``цепочки глубже второго порядка``
    Ограничение живёт не здесь, а в генераторе (правило-источник не может быть
    одновременно потребителем). В оригинале глубина не превышает 2.
"""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field

from .level_solver import INTERPRETATION_STATUSES
from .normalization import normalize_word

# Пулы, пересекающиеся сильнее чем наполовину, парой не считаются: если пул B
# почти лежит внутри пула A, группа B на уровне неотличима от куска группы A,
# и мета-связь превращается в неоднозначность.
DEFAULT_MAX_POOL_OVERLAP = 0.5


@dataclass(frozen=True)
class MetaPair:
    """Одна готовая связь «B выпускает токен для A»."""

    consumer_id: int
    consumer_key: str
    quartet_id: int
    token_display: str
    token_norm: str
    source_id: int
    source_key: str
    source_label_id: int
    source_label: str
    pool_overlap: float


@dataclass
class MetaIndex:
    """Все мета-пары базы, разложенные по трём входам."""

    pairs: tuple[MetaPair, ...] = ()
    by_quartet: dict[int, list[MetaPair]] = field(default_factory=dict)
    by_consumer: dict[int, list[MetaPair]] = field(default_factory=dict)
    by_source: dict[int, list[MetaPair]] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=dict)

    def __len__(self) -> int:
        return len(self.pairs)

    def for_quartet(self, quartet_id: int) -> list[MetaPair]:
        return self.by_quartet.get(quartet_id, [])

    def distinct_pairs(self) -> set[tuple[int, int]]:
        return {(pair.consumer_id, pair.source_id) for pair in self.pairs}


def load(
    conn: sqlite3.Connection,
    *,
    max_pool_overlap: float = DEFAULT_MAX_POOL_OVERLAP,
    tier: str = "normal",
) -> MetaIndex:
    """Собирает индекс мета-пар. Порядок стабильный, случайности нет."""
    rules = {
        int(row["id"]): row
        for row in conn.execute(
            """
            SELECT id, category_key, label, concept_id, rule_type
              FROM categories
             WHERE status = 'active' AND origin <> 'reference_backfill'
            """
        )
    }

    # Надписи-кандидаты: только собственные, чужие авторские не берём.
    labels_by_norm: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
    for row in conn.execute(
        """
        SELECT grl.category_id AS category_id, l.id AS label_id,
               l.display_text AS display_text
          FROM group_rule_labels grl
          JOIN category_labels l ON l.id = grl.label_id
          JOIN categories c      ON c.id = grl.category_id
         WHERE c.status = 'active'
           AND c.origin <> 'reference_backfill'
           AND l.origin <> 'reference_backfill'
         ORDER BY grl.category_id, grl.is_primary DESC, l.id
        """
    ):
        key = normalize_word(row["display_text"])
        if key:
            labels_by_norm[key].append(
                (int(row["category_id"]), int(row["label_id"]), row["display_text"])
            )

    # Слова годных четвёрок. Условия ровно те же, что в генераторе: индекс,
    # обещающий пару на четвёрке, которую генератор не возьмёт, бесполезен.
    quartet_rows = conn.execute(
        """
        SELECT q.id AS quartet_id, q.category_id AS category_id,
               COALESCE(s.display_text, w.text) AS display
          FROM quartets q
          JOIN categories c     ON c.id = q.category_id
          JOIN quartet_words qw ON qw.quartet_id = q.id
          JOIN words w          ON w.id = qw.word_id
          LEFT JOIN word_senses s ON s.id = qw.sense_id
         WHERE q.validation_state IN ('auto_validated', 'warning')
           AND q.local_check = 'local_unique'
           AND c.status = 'active'
           AND c.origin <> 'reference_backfill'
           AND q.origin <> 'reference_backfill'
           AND (q.tier = ? OR ? = 'hard')
         ORDER BY q.id
        """,
        (tier, tier),
    )
    raw: list[tuple[int, int, str, str, int, int, str]] = []
    for row in quartet_rows:
        display = row["display"]
        token_norm = normalize_word(display)
        for source_id, label_id, label_text in labels_by_norm.get(token_norm, ()):
            consumer_id = int(row["category_id"])
            if source_id == consumer_id:
                continue
            raw.append(
                (
                    consumer_id,
                    int(row["quartet_id"]),
                    display,
                    token_norm,
                    source_id,
                    label_id,
                    label_text,
                )
            )

    stats = {
        "надписей своих": len(labels_by_norm),
        "пар до фильтров": len({(item[0], item[4]) for item in raw}),
    }
    if not raw:
        return MetaIndex(stats=stats)

    involved = {item[0] for item in raw} | {item[4] for item in raw}
    conflicts = _conflicts(conn, involved)
    pools = _pools(conn, involved)
    sources_with_quartet = _categories_with_quartets(conn, tier)

    dropped = defaultdict(int)
    pairs: list[MetaPair] = []
    for consumer_id, quartet_id, display, token_norm, source_id, label_id, label_text in raw:
        consumer, source = rules.get(consumer_id), rules.get(source_id)
        if consumer is None or source is None:
            continue
        if source_id not in sources_with_quartet:
            # Источник, которому нечем собраться, на уровень не поставить.
            dropped["у источника нет четвёрки"] += 1
            continue
        if source_id in conflicts.get(consumer_id, ()):
            dropped["конфликт правил"] += 1
            continue
        if consumer["concept_id"] and consumer["concept_id"] == source["concept_id"]:
            dropped["один концепт"] += 1
            continue
        if token_norm in pools.get(source_id, ()):
            # Группа не должна принимать собственный результат: пузырь окажется
            # верным и для источника, и для потребителя.
            dropped["источник принимает свой же токен"] += 1
            continue
        overlap = _overlap(pools.get(consumer_id, set()), pools.get(source_id, set()))
        if overlap > max_pool_overlap:
            dropped["пулы почти совпадают"] += 1
            continue
        pairs.append(
            MetaPair(
                consumer_id=consumer_id,
                consumer_key=consumer["category_key"],
                quartet_id=quartet_id,
                token_display=display,
                token_norm=token_norm,
                source_id=source_id,
                source_key=source["category_key"],
                source_label_id=label_id,
                source_label=label_text,
                pool_overlap=round(overlap, 4),
            )
        )

    by_quartet: dict[int, list[MetaPair]] = defaultdict(list)
    by_consumer: dict[int, list[MetaPair]] = defaultdict(list)
    by_source: dict[int, list[MetaPair]] = defaultdict(list)
    for pair in pairs:
        by_quartet[pair.quartet_id].append(pair)
        by_consumer[pair.consumer_id].append(pair)
        by_source[pair.source_id].append(pair)

    # Счётчики отсева считают связки «четвёрка-надпись», а не пары правил:
    # одна пара живёт в нескольких четвёрках, и складывать их нельзя.
    stats.update(
        {f"отсеяно связок: {reason}": count for reason, count in sorted(dropped.items())}
    )
    stats.update(
        {
            "пар готово": len({(pair.consumer_id, pair.source_id) for pair in pairs}),
            "четвёрок-потребителей": len(by_quartet),
            "правил-потребителей": len(by_consumer),
            "правил-источников": len(by_source),
        }
    )
    return MetaIndex(
        pairs=tuple(pairs),
        by_quartet=dict(by_quartet),
        by_consumer=dict(by_consumer),
        by_source=dict(by_source),
        stats=stats,
    )


def _conflicts(conn: sqlite3.Connection, involved: set[int]) -> dict[int, set[int]]:
    conflicts: dict[int, set[int]] = defaultdict(set)
    for row in conn.execute("SELECT category_a_id, category_b_id FROM category_conflicts"):
        a, b = int(row["category_a_id"]), int(row["category_b_id"])
        if a in involved or b in involved:
            conflicts[a].add(b)
            conflicts[b].add(a)
    return conflicts


def _pools(conn: sqlite3.Connection, involved: set[int]) -> dict[int, set[str]]:
    """Что правило принимает — глазами solver'а, а не глазами сборщика четвёрок.

    Статусы берутся те же, по которым solver ищет альтернативные разбиения,
    включая `hard_only`. Иначе получилась бы пара, которую индекс считает
    чистой, а solver — двусмысленной: правило-источник принимает собственный
    выпущенный пузырь по «трудной» связи, и уровень отклоняется уже после
    сборки.
    """
    placeholders = ",".join("?" for _ in INTERPRETATION_STATUSES)
    pools: dict[int, set[str]] = defaultdict(set)
    for row in conn.execute(
        f"""
        SELECT m.category_id AS category_id, w.normalized AS normalized
          FROM memberships m
          JOIN words w ON w.id = m.word_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'
        """,
        INTERPRETATION_STATUSES,
    ):
        category_id = int(row["category_id"])
        if category_id in involved:
            pools[category_id].add(row["normalized"])
    return pools


def _categories_with_quartets(conn: sqlite3.Connection, tier: str) -> set[int]:
    return {
        int(row["category_id"])
        for row in conn.execute(
            """
            SELECT DISTINCT q.category_id AS category_id
              FROM quartets q
              JOIN categories c ON c.id = q.category_id
             WHERE q.validation_state IN ('auto_validated', 'warning')
               AND q.local_check = 'local_unique'
               AND c.status = 'active'
               AND c.origin <> 'reference_backfill'
               AND q.origin <> 'reference_backfill'
               AND (q.tier = ? OR ? = 'hard')
            """,
            (tier, tier),
        )
    }


def _overlap(first: set[str], second: set[str]) -> float:
    """Доля пересечения относительно меньшего пула."""
    if not first or not second:
        return 0.0
    return len(first & second) / min(len(first), len(second))
