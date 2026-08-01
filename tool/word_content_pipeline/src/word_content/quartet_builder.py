"""Сборка четвёрок-кандидатов.

База хранит пулы, а игре нужны решения: категория в уровне — ровно четыре
слова. Четыре случайных слова из пула не годятся по двум причинам. Во-первых,
они могут целиком лежать в другой категории — тогда у уровня два ответа.
Во-вторых, случайный выбор регулярно даёт четвёрку из четырёх редких слов:
формально корректную и невозможную для игрока.

Поэтому все `C(N,4)` сочетания не сохраняются. Из пула отбирается ограниченный
разнообразный набор по объяснимым признакам:

  * связность — насколько уверенно слова принадлежат категории;
  * узнаваемость — средняя частотность слов;
  * якоря — одно-два слова, по которым игрок узнаёт категорию сразу;
  * управляемая двусмысленность — слова, которые тянут в соседнюю категорию,
    но здесь у них ровно один дом (материал для ловушек);
  * непохожесть на другие четвёрки этой же категории;
  * риски — служебные пометки связи;
  * пригодность к обычному или сложному уровню.

Итог — `validation_state = auto_validated`: машинные проверки пройдены.
Человек оценивает не четвёрку, а собранный уровень целиком.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, replace
from itertools import combinations

from . import scoring
from .readiness import NORMAL_READY, NORMAL_STATUSES, QUARTET_SIZE
from .solver import category_pools, quartet_locally_unique

VALIDATOR_VERSION = "quartet-candidates/1.0"

# Сколько четвёрок оставлять на правило. Уровень берёт одну, но кампании нужен
# запас: при трёх четвёрках на правило генератор упирался в повторы к трёхсотому
# уровню, потому что свободных правил не оставалось.
#
# Замер на копии базы, 2500 запрошенных уровней по 8 категорий:
#   было  (пул 12, пересечений 0, 3 на правило):  323 уровня,  74% слов в деле
#   стало (пул 40, пересечение 1, 20 на правило): 2238 уровней, 93% слов в деле
MAX_PER_CATEGORY = 20
# Сколько слов пула рассматривать. Это защита от перебора, а не фильтр качества.
#
# Раньше здесь стояло 12, и это стоило 2035 годных слов: их единственной виной
# было тринадцатое место в своём пуле (ostrich, hangar, baggage — нормальный
# игровой материал). Самый большой пул в базе сегодня 34 слова, так что 40
# означает «не отсекаем никого»; число остаётся на случай, если когда-нибудь
# появится пул на сотню слов — C(100,4) это четыре миллиона сочетаний на одно
# правило, и перебор встанет.
#
# Цена измерена: сборка четвёрок 64 с -> 355 с, один раз при пересборке базы.
# Отдача: 3205 -> 14184 четвёрки, слов в деле 74% -> 93%.
CANDIDATE_POOL = 40

# Сколько слов две четвёрки одного правила могут делить.
#
# Ноль означает «полностью непересекающиеся», и это главная причина, по которой
# правило с пулом в 20 слов даёт всего три четвёрки. Единица даёт кратно больше
# вариантов, оставаясь далеко от «те же слова, переставленные местами»: две
# четвёрки FARM ANIMALS с общей `cow` — разные игровые группы, а с тремя общими
# словами — одна и та же.
MAX_SHARED_WORDS = 1
# Слово считается якорем, если средний игрок его точно знает (zipf ~4.2 и выше).
ANCHOR_FAMILIARITY = 0.6


@dataclass(frozen=True)
class QuartetCandidate:
    category_key: str
    quartet_key: str
    words: tuple[str, ...]
    tier: str
    difficulty: float | None
    note: str
    cohesion_score: float
    familiarity_score: float
    ambiguity_pressure: float
    anchor_count: int
    risk_state: str
    intended_relation: str
    origin: str = "derived"
    validation_state: str = "auto_validated"
    local_check: str = "local_unique"
    validator_version: str = VALIDATOR_VERSION

    @property
    def selection_score(self) -> float:
        """Композитная оценка отбора.

        Веса подобраны так, чтобы связность и узнаваемость перевешивали, а
        двусмысленность оставалась приправой: четвёрка, где все четыре слова
        спорные, — это не интересная ловушка, а неприятный уровень.
        """
        return (
            0.45 * self.cohesion_score
            + 0.35 * self.familiarity_score
            + 0.10 * min(self.anchor_count, 2) / 2
            + 0.10 * min(self.ambiguity_pressure, 0.5) / 0.5
        )


def _pool_rows(conn: sqlite3.Connection, category_key: str) -> list[sqlite3.Row]:
    placeholders = ",".join("?" for _ in NORMAL_STATUSES)
    return list(
        conn.execute(
            f"""
            SELECT w.normalized AS normalized, w.familiarity_score AS familiarity,
                   s.sense_key AS sense_key,
                   m.gameplay_difficulty AS difficulty, m.obviousness_score AS obviousness,
                   m.fit_score AS fit, m.risk_flags AS risk_flags,
                   m.relation_type AS relation_type
              FROM memberships m
              JOIN categories c ON c.id = m.category_id
              JOIN words w      ON w.id = m.word_id
              LEFT JOIN word_senses s ON s.id = m.sense_id
             WHERE c.category_key = ?
               AND m.review_status IN ({placeholders})
               AND m.semantic_status <> 'incorrect'
               AND m.validation_state <> 'invalid'
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
    candidate_pool: int = CANDIDATE_POOL,
    max_shared_words: int = MAX_SHARED_WORDS,
) -> tuple[list[QuartetCandidate], dict[str, int]]:
    """Собирает четвёрки по готовым категориям. Возвращает (кандидаты, статистика)."""
    pools = category_pools(conn)  # включая hard_only: чужая категория опасна любая
    scoring_config = scoring.load_config()
    placeholders = ",".join("?" for _ in NORMAL_READY)
    # Правила, выведенные из записи оригинала, четвёрок-кандидатов не дают:
    # их пул — ровно чужая авторская четвёрка, и генератор повторил бы её.
    sql = (
        f"SELECT category_key FROM categories WHERE readiness IN ({placeholders})"
        " AND origin <> 'reference_backfill'"
    )
    params: list[object] = list(NORMAL_READY)
    if only_category:
        sql += " AND category_key = ?"
        params.append(only_category)
    keys = [row["category_key"] for row in conn.execute(sql + " ORDER BY category_key", params)]

    built: list[QuartetCandidate] = []
    stats = {
        "категорий рассмотрено": 0,
        "категорий без четвёрок": 0,
        "четвёрок": 0,
        "отклонено локальной проверкой": 0,
        "отклонено по рискам": 0,
    }

    for category_key in keys:
        stats["категорий рассмотрено"] += 1
        rows = _pool_rows(conn, category_key)[:candidate_pool]
        by_word = {row["normalized"]: row for row in rows}
        available = [row["normalized"] for row in rows]

        scored: list[QuartetCandidate] = []
        for group in combinations(available, QUARTET_SIZE):
            members = [by_word[word] for word in group]
            if any(m["risk_flags"] and "sensitive" in m["risk_flags"] for m in members):
                stats["отклонено по рискам"] += 1
                continue
            result = quartet_locally_unique(conn, category_key, list(group), pools=pools)
            if not result.unique:
                stats["отклонено локальной проверкой"] += 1
                continue

            familiarity = [m["familiarity"] for m in members if m["familiarity"] is not None]
            difficulties = [m["difficulty"] for m in members if m["difficulty"] is not None]
            scored.append(
                QuartetCandidate(
                    category_key=category_key,
                    quartet_key="",  # присваивается после отбора
                    words=tuple(
                        f"{word}#{by_word[word]['sense_key']}"
                        if by_word[word]["sense_key"]
                        else word
                        for word in group
                    ),
                    tier="normal",
                    difficulty=(
                        round(sum(difficulties) / len(difficulties), 3) if difficulties else None
                    ),
                    note=result.reason,
                    cohesion_score=scoring.cohesion(
                        [m["fit"] for m in members], scoring_config
                    ).rounded(),
                    familiarity_score=(
                        round(sum(familiarity) / len(familiarity), 3) if familiarity else 0.0
                    ),
                    ambiguity_pressure=scoring.foreign_pressure(pools, category_key, group),
                    anchor_count=sum(1 for value in familiarity if value >= ANCHOR_FAMILIARITY),
                    risk_state="flagged" if any(m["risk_flags"] for m in members) else "clear",
                    intended_relation=members[0]["relation_type"],
                )
            )

        # Жадный отбор: лучший кандидат, затем лучший из достаточно непохожих.
        # Похожесть меряется попарно, а не по общему мешку слов: иначе третья
        # четвёрка отвергается за слово, взятое первой, хотя со второй у неё
        # нет ничего общего.
        scored.sort(key=lambda item: (-item.selection_score, item.words))
        accepted: list[set[str]] = []
        found = 0
        for candidate in scored:
            if found >= max_per_category:
                break
            plain = {word.split("#")[0] for word in candidate.words}
            if any(len(plain & taken) > max_shared_words for taken in accepted):
                continue
            found += 1
            accepted.append(plain)
            built.append(replace(candidate, quartet_key=f"{category_key}__{found}"))
        if found == 0:
            stats["категорий без четвёрок"] += 1

    stats["четвёрок"] = len(built)
    return built, stats


def to_rows(built: list[QuartetCandidate]) -> list[dict[str, object]]:
    """Строки для data/quartets.csv — текстового источника правды по четвёркам."""
    return [
        {
            "quartet_key": item.quartet_key,
            "category_key": item.category_key,
            "tier": item.tier,
            "validation_state": item.validation_state,
            "local_check": item.local_check,
            # None, а не "": эти же строки идут в валидацию QuartetInput, а пустая
            # строка не парсится как число — четвёрка молча уезжала в «пропущено».
            "difficulty": item.difficulty,
            "cohesion_score": item.cohesion_score,
            "familiarity_score": item.familiarity_score,
            "ambiguity_pressure": item.ambiguity_pressure,
            "risk_state": item.risk_state,
            "intended_relation": item.intended_relation,
            "origin": item.origin,
            "validator_version": item.validator_version,
            "words": " | ".join(item.words),
            "note": item.note,
        }
        for item in built
    ]
