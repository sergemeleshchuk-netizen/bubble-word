"""Очевидность связи, отранжированная внутри категории.

Зачем шаг существует. `memberships.obviousness_score` заполнял сид, и заполнял
он его ПО КАТЕГОРИИ, а не по слову. Замер 02.08 по снимку b9c962: в 960
категориях из 1296 (74%) на весь пул стоит одно значение — это 14 584 связи из
18 815, то есть 78% базы. Из плоских категорий 681 в статусе `ready`, они прямо
сейчас идут в уровни.

Что это ломает. В SCHOOL SUBJECTS все 25 слов получили ровно 0.9 — от `math` до
`gym`. По записанным числам `gym` в предметах (0.9) выходит очевиднее, чем
`smile` в выражениях лица (0.75), что неправда. Генератор с версии 1.6.0 это
поле при отборе слов читает, и на плоской категории ему нечего предпочитать:
слагаемое вырождается в константу, а решает частотность. Так на поле и приехал
`gym` рядом с physics, chemistry и economics.

Приоритет работы. Не «все 960 подряд», а сначала те, где плоское число спорит с
самой базой. Спор — это слово, у которого ЕСТЬ ДРУГОЙ ДОМ не слабее здешнего:
`gym` заявлен на 0.9 и в SCHOOL SUBJECTS, и в TOWN PLACES, а «первым вспомнится»
может только что-то одно. Считать спором только «в другом месте выше» оказалось
мало: SCHOOL SUBJECTS с его 0.9 — потолок среди домов `gym`, и при таком счёте
самая показательная категория уезжала в хвост очереди. Порядок задаёт
`targets()`.

Почему прогон модели, а не формула. Очевидность — это ответ на вопрос «вспомнит
ли игрок первым именно это значение», и вывести её из остальных полей базы
нельзя. Все кандидаты в предикторы либо не про то, либо залиты так же оптом.
Число домов слова особенно обманчиво: у `apple` их 11, у `orange` 6, у `star`
13, и все трое безупречны для первых уровней; а у `shop` и `health` дом ровно
один — и это тот самый «предмет американской школы». Различает их не счёт, а
то, какое значение приходит первым, — суждение, а не арифметика.

Что шаг НЕ делает. Он не трогает `obviousness_score`: исходное значение
остаётся входом источника, результат пишется в `graded_obviousness`. Пересчёт
обратим, расхождение видно в любой момент, экспорт снимка предпочитает
отранжированное значение, когда оно есть. Тот же уговор, что у шага
`derive-category-difficulty`.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from typing import Any

from pydantic import ValidationError

from .db import transaction, utc_now
from .llm.base import LLMError, LLMProvider
from .llm.prompts import build_grade_obviousness_prompt
from .llm.schemas import ObviousnessGradingOutput, parse_json_response

MODEL_VERSION = "graded-obviousness/1.0"

# Слова, которые игрок реально увидит. `candidate` и `rejected` не ранжируем:
# платить за оценку того, что в уровень не пойдёт, незачем.
GRADED_STATUSES = ("approved", "alternative", "hard_only")

# Разброс, ниже которого ответ считается невыполненной работой.
#
# Смысл шага — расслоить категорию. Если модель вернула тот же плоский ответ,
# записать его значило бы заменить одну заливку другой и потерять возможность
# отличить «оценено» от «не оценено». Порог 0.10 выбран по данным: у категорий,
# где очевидность проставляли пословно, размах составляет 0.20-0.61, а «почти
# плоскими» (размах ≤ 0.05) в замере признаны такие, как COLORS, где
# однородность настоящая. 0.10 проходит между этими двумя случаями.
MIN_SPREAD = 0.10

# Категория меньше этого размера расслоению не подлежит: на трёх словах
# «верх и низ» — это шум, а четвёрка из такой категории всё равно берётся
# целиком, и порядок внутри неё ни на что не влияет.
MIN_POOL = 5

# Размах, ниже которого категория считается плоской ПО СУЩЕСТВУ, даже если
# формально значения в ней разные.
#
# Считается не на глаз, а из формулы отбора в генераторе. Там очевидность
# входит с весом 0.9, а бонус за новое для пакета слово равен 0.15. Значит
# при размахе меньше 0.15/0.9 = 0.167 слагаемое очевидности не способно
# перевесить даже бонус за новизну — то есть на выбор слова оно не влияет
# ни при каком раскладе. Такая категория «отранжирована» только на бумаге.
#
# Замер по базе: 163 категории в автосборке имели размах 0.02-0.19 и в
# прежнюю очередь (строгое равенство min и max) не попадали.
NOMINAL_SPREAD = 0.17


@dataclass
class GradingResult:
    """Итог прогона: что записано, что отброшено и почему."""

    graded_categories: int = 0
    graded_memberships: int = 0
    uniform_categories: int = 0
    """Из них признаны однородными по существу — см. `uniform` в схеме ответа."""
    batches_ok: int = 0
    batches_failed: int = 0
    skipped: list[dict[str, Any]] = field(default_factory=list)
    records: list[dict[str, Any]] = field(default_factory=list)

    def skip(self, reason: str, payload: Any) -> None:
        self.skipped.append({"reason": reason, "payload": payload})


@dataclass(frozen=True)
class Target:
    """Категория-кандидат на ранжирование и причина, по которой она в очереди."""

    category_id: int
    category_key: str
    label: str
    rule: str
    readiness: str
    pool: int
    flat_value: float
    contested: int
    """Сколько слов имеют другой дом не слабее здешнего плоского значения."""


def targets(
    conn: sqlite3.Connection,
    *,
    readiness: tuple[str, ...] = ("ready",),
    limit: int | None = None,
) -> list[Target]:
    """Плоские категории в порядке убывания пользы от ранжирования.

    Плоская — значит размах очевидности внутри категории меньше
    NOMINAL_SPREAD, то есть на отбор слова она влиять не может, даже если
    формально значения в ней разные. Порядок очереди: сначала те, где плоское число спорит с самой
    базой (`contested`), потом крупные пулы — там одно число накрывает больше
    слов.
    """
    # Насколько дом-соперник должен уступать, чтобы спором не считаться.
    #
    # Строгое «больше здешнего» не годится: у `gym` и SCHOOL SUBJECTS, и
    # TOWN PLACES стоят ровно 0.9, спор очевиден, а строгое сравнение его не
    # видит. 0.05 — шаг сетки, которой пользовался сид (0.9 / 0.88 / 0.85),
    # то есть меньшая разница в этих данных ничего не значит.
    RIVAL_EPS = 0.05
    rows = conn.execute(
        f"""
        SELECT m.category_id, c.category_key, c.label, c.rule, c.readiness,
               COUNT(*) AS pool,
               MIN(m.obviousness_score) AS lo,
               MAX(m.obviousness_score) AS hi
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
         WHERE m.review_status IN ({','.join('?' * len(GRADED_STATUSES))})
           AND c.status = 'active'
           AND m.obviousness_score IS NOT NULL
           AND m.graded_obviousness IS NULL
         GROUP BY m.category_id
        HAVING COUNT(*) >= ?
           AND MAX(m.obviousness_score) - MIN(m.obviousness_score) < ?
        """,
        (*GRADED_STATUSES, MIN_POOL, NOMINAL_SPREAD),
    ).fetchall()

    # «Сильнейший ЧУЖОЙ дом слова» считаем один раз на всю базу: на 18 815
    # связях запрос в цикле по категориям обошёлся бы в 960 полных проходов.
    rival: dict[tuple[int, int], float] = {}
    homes: dict[int, list[tuple[int, float]]] = {}
    for row in conn.execute(
        "SELECT word_id, category_id, obviousness_score FROM memberships "
        "WHERE obviousness_score IS NOT NULL"
    ):
        homes.setdefault(row["word_id"], []).append(
            (row["category_id"], float(row["obviousness_score"]))
        )
    for word_id, entries in homes.items():
        for category_id, _ in entries:
            others = [score for cat, score in entries if cat != category_id]
            rival[(word_id, category_id)] = max(others) if others else 0.0

    out: list[Target] = []
    for row in rows:
        if readiness and row["readiness"] not in readiness:
            continue
        flat = float(row["lo"])
        contested = sum(
            1
            for m in conn.execute(
                "SELECT word_id FROM memberships WHERE category_id = ? "
                f"AND review_status IN ({','.join('?' * len(GRADED_STATUSES))})",
                (row["category_id"], *GRADED_STATUSES),
            )
            if rival.get((m["word_id"], row["category_id"]), 0.0) >= flat - RIVAL_EPS
        )
        out.append(
            Target(
                category_id=row["category_id"],
                category_key=row["category_key"],
                label=row["label"],
                rule=row["rule"] or "",
                readiness=row["readiness"],
                pool=int(row["pool"]),
                flat_value=flat,
                contested=contested,
            )
        )

    out.sort(key=lambda t: (-t.contested, -t.pool, t.category_key))
    return out[:limit] if limit else out


def _word_payload(conn: sqlite3.Connection, target: Target) -> list[dict[str, Any]]:
    """Слова категории вместе с их ОСТАЛЬНЫМИ домами.

    Конкурирующие дома идут в промпт не как признак плохого слова, а как то, с
    чем борется первое узнавание: без них модель не отличит `gym`-предмет от
    `gym`-зала. Считать по ним самим ничего нельзя — см. шапку модуля.
    """
    rows = conn.execute(
        f"""
        SELECT m.id AS membership_id, w.id AS word_id, w.text AS word,
               m.relation_type, m.reason, m.review_status, s.definition AS sense_definition
          FROM memberships m
          JOIN words w ON w.id = m.word_id
     LEFT JOIN word_senses s ON s.id = m.sense_id
         WHERE m.category_id = ?
           AND m.review_status IN ({','.join('?' * len(GRADED_STATUSES))})
         ORDER BY w.text
        """,
        (target.category_id, *GRADED_STATUSES),
    ).fetchall()

    payload = []
    for row in rows:
        others = [
            other["label"]
            for other in conn.execute(
                "SELECT c.label FROM memberships m JOIN categories c ON c.id = m.category_id "
                "WHERE m.word_id = ? AND m.category_id != ? AND c.status = 'active' "
                "ORDER BY m.obviousness_score DESC LIMIT 8",
                (row["word_id"], target.category_id),
            )
        ]
        payload.append(
            {
                "word": row["word"],
                "current_status": row["review_status"],
                "relation_type": row["relation_type"],
                "sense_definition": row["sense_definition"],
                "also_lives_in": others,
            }
        )
    return payload


def _membership_ids(conn: sqlite3.Connection, category_id: int) -> dict[str, int]:
    """Нормализованное слово → id связи, для сопоставления ответа модели."""
    return {
        row["word"].strip().lower(): row["membership_id"]
        for row in conn.execute(
            f"""
            SELECT m.id AS membership_id, w.text AS word
              FROM memberships m JOIN words w ON w.id = m.word_id
             WHERE m.category_id = ?
               AND m.review_status IN ({','.join('?' * len(GRADED_STATUSES))})
            """,
            (category_id, *GRADED_STATUSES),
        )
    }


def grade(
    conn: sqlite3.Connection,
    provider: LLMProvider,
    *,
    readiness: tuple[str, ...] = ("ready",),
    limit: int | None = None,
    apply: bool = False,
    max_retries: int = 2,
) -> GradingResult:
    """Ранжирует очевидность внутри плоских категорий, по одной на запрос.

    Без `apply` в базу не пишется ничего — результат возвращается записями,
    как у остальных AI-проходов: сначала посмотреть, потом применять.
    """
    result = GradingResult()
    queue = targets(conn, readiness=readiness, limit=limit)

    for target in queue:
        words = _word_payload(conn, target)
        if len(words) < MIN_POOL:
            result.skip("pool_too_small", target.category_key)
            continue

        prompt = build_grade_obviousness_prompt(
            category={
                "category_key": target.category_key,
                "label": target.label,
                "rule": target.rule,
            },
            words=words,
        )
        try:
            raw = provider.complete_json(prompt, system=_SYSTEM).text
            parsed = ObviousnessGradingOutput.model_validate(parse_json_response(raw))
        except (LLMError, ValueError, ValidationError) as exc:
            result.batches_failed += 1
            result.skip("batch_failed", {"category": target.category_key, "error": str(exc)})
            continue

        by_word = _membership_ids(conn, target.category_id)
        graded: list[tuple[int, float, str, str]] = []
        for item in parsed.grades:
            key = item.word.strip().lower()
            membership_id = by_word.get(key)
            if membership_id is None:
                result.skip("unknown_word", {"category": target.category_key, "word": item.word})
                continue
            graded.append((membership_id, item.obviousness_score, item.reason, item.word))

        if not graded:
            result.batches_failed += 1
            result.skip("nothing_matched", target.category_key)
            continue

        values = [g[1] for g in graded]
        spread = max(values) - min(values)
        if spread < MIN_SPREAD and not parsed.uniform:
            result.batches_failed += 1
            result.skip(
                "no_spread",
                {"category": target.category_key, "spread": round(spread, 3)},
            )
            continue
        if spread < MIN_SPREAD:
            # Однородность заявлена явно — записываем и считаем отдельно, чтобы
            # доля таких категорий была видна: если она поползёт вверх, значит
            # флагом начали затыкать лень, а не описывать контент.
            result.uniform_categories += 1

        result.batches_ok += 1
        result.graded_categories += 1
        result.graded_memberships += len(graded)
        result.records.append(
            {
                "category_key": target.category_key,
                "was": target.flat_value,
                "spread": round(spread, 3),
                "uniform": spread < MIN_SPREAD,
                "grades": [
                    {"word": word, "obviousness_score": score, "reason": reason}
                    for _, score, reason, word in sorted(graded, key=lambda g: -g[1])
                ],
            }
        )

        if apply:
            now = utc_now()
            with transaction(conn):
                conn.executemany(
                    "UPDATE memberships SET graded_obviousness = ?, "
                    "graded_obviousness_reason = ?, graded_obviousness_version = ?, "
                    "updated_at = ? WHERE id = ?",
                    [
                        (score, reason, MODEL_VERSION, now, membership_id)
                        for membership_id, score, reason, _ in graded
                    ],
                )

    return result


_SYSTEM = (
    "You are a careful lexical content editor for an American English word puzzle. "
    "You answer with raw JSON only: no markdown, no commentary, no code fences."
)
