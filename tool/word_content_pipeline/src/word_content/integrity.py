"""Проверки готовности базы — критерии приёмки из аудита в виде кода.

Каждая проверка отвечает на один вопрос «да/нет» и, если ответ «нет», показывает
примеры. Проверка со severity `blocker` роняет `check-integrity` ненулевым кодом:
такую базу нельзя отдавать генератору уровней.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Callable
from dataclasses import dataclass, field

from .readiness import NORMAL_READY, QUARTET_SIZE, category_pools

# Категории игры слов работают с написанием слова, а не со значением: 'starboard'
# не происходит от звезды. Пустой sense_id у них — осознанное решение, не пробел.
WORDPLAY_RELATIONS = ("phrase_before", "phrase_after")


@dataclass
class CheckResult:
    name: str
    question: str
    severity: str  # blocker | warning | info
    count: int
    examples: list[str] = field(default_factory=list)
    note: str = ""

    @property
    def ok(self) -> bool:
        return self.count == 0

    @property
    def failed(self) -> bool:
        return self.severity == "blocker" and not self.ok


def _examples(rows: list[sqlite3.Row], render: Callable[[sqlite3.Row], str], limit: int = 10):
    return [render(row) for row in rows[:limit]]


# --------------------------------------------------------------------------- проверки


def check_sqlite_integrity(conn: sqlite3.Connection) -> CheckResult:
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    violations = list(conn.execute("PRAGMA foreign_key_check"))
    problems = ([] if integrity == "ok" else [f"integrity_check: {integrity}"]) + [
        f"нарушение внешнего ключа в {row[0]}" for row in violations[:10]
    ]
    return CheckResult(
        name="sqlite_integrity",
        question="Файл базы цел, внешние ключи не нарушены",
        severity="blocker",
        count=len(problems),
        examples=problems,
    )


def check_familiarity_gate(conn: sqlite3.Connection) -> CheckResult:
    """P0: связь не может быть играбельной, если частотность слова неизвестна."""
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key, m.review_status AS status
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE w.familiarity_score IS NULL
               AND m.review_status IN ('approved', 'alternative', 'hard_only')
             ORDER BY w.normalized
            """
        )
    )
    return CheckResult(
        name="familiarity_gate",
        question="Нет играбельных связей со словом без частотности",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']} -> {r['category_key']} ({r['status']})"),
        note="Отсутствующие данные должны закрывать связь, а не проходить как подтверждённые.",
    )


def check_sense_assignment(conn: sqlite3.Connection) -> CheckResult:
    """P0: у слова с двумя и более значениями каждая связь знает своё значение."""
    placeholders = ",".join("?" for _ in WORDPLAY_RELATIONS)
    rows = list(
        conn.execute(
            f"""
            SELECT w.text AS word, c.category_key AS category_key,
                   (SELECT COUNT(*) FROM word_senses s WHERE s.word_id = w.id) AS senses
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.sense_id IS NULL
               AND m.review_status <> 'rejected'
               AND m.relation_type NOT IN ({placeholders})
               AND senses > 1
             ORDER BY w.normalized, c.category_key
            """,
            WORDPLAY_RELATIONS,
        )
    )
    return CheckResult(
        name="sense_assignment",
        question="Нет связей многозначных слов без указанного значения",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['word']} -> {r['category_key']} (значений у слова: {r['senses']})"
        ),
        note="Исключение — категории игры слов: там участвует написание, а не значение.",
    )


def check_wordplay_sense_exemption(conn: sqlite3.Connection) -> CheckResult:
    """Информационная: сколько связей пользуется исключением для игры слов."""
    placeholders = ",".join("?" for _ in WORDPLAY_RELATIONS)
    rows = list(
        conn.execute(
            f"""
            SELECT w.text AS word, c.category_key AS category_key
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.sense_id IS NULL
               AND m.relation_type IN ({placeholders})
               AND (SELECT COUNT(*) FROM word_senses s WHERE s.word_id = w.id) > 1
             ORDER BY w.normalized
            """,
            WORDPLAY_RELATIONS,
        )
    )
    return CheckResult(
        name="wordplay_sense_exemption",
        question="Связи игры слов без значения (осознанное исключение)",
        severity="info",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']} -> {r['category_key']}"),
        note="Компаунд не наследует значение слова: 'starboard' не от звезды, 'keystone' не от ключа.",
    )


def check_normal_quartet_capability(conn: sqlite3.Connection) -> CheckResult:
    """P0: включённая для обычных уровней категория обязана собирать четвёрку."""
    bad = [
        pools
        for pools in category_pools(conn)
        if pools.normal_pool < QUARTET_SIZE
        and _readiness(conn, pools.category_key) in NORMAL_READY
    ]
    return CheckResult(
        name="normal_quartet_capability",
        question="Нет включённых normal-категорий с пулом меньше четырёх слов уровня",
        severity="blocker",
        count=len(bad),
        examples=[
            f"{pools.label} ({pools.category_key}): слов уровня {pools.normal_pool}"
            for pools in bad[:10]
        ],
    )


def _readiness(conn: sqlite3.Connection, category_key: str) -> str:
    row = conn.execute(
        "SELECT readiness FROM categories WHERE category_key = ?", (category_key,)
    ).fetchone()
    return "unknown" if row is None else row["readiness"]


def check_readiness_derived(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute("SELECT category_key FROM categories WHERE readiness = 'unknown'")
    )
    return CheckResult(
        name="readiness_derived",
        question="У всех категорий посчитан readiness",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: r["category_key"]),
        note="Считается командой derive-readiness.",
    )


def check_semantic_incorrect_not_playable(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key, m.review_status AS status
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.semantic_status = 'incorrect'
               AND m.review_status <> 'rejected'
            """
        )
    )
    return CheckResult(
        name="semantic_incorrect_not_playable",
        question="Семантически неверные связи не идут в игру",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']} -> {r['category_key']} ({r['status']})"),
    )


def check_quartets_unique(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT q.quartet_key AS quartet_key, c.category_key AS category_key,
                   q.solver_state AS solver_state
              FROM quartets q JOIN categories c ON c.id = q.category_id
             WHERE q.review_state <> 'rejected' AND q.solver_state <> 'unique'
            """
        )
    )
    return CheckResult(
        name="quartets_unique",
        question="Все действующие четвёрки прошли solver единственности",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['quartet_key']} ({r['category_key']}): {r['solver_state']}"
        ),
    )


def check_quartet_size(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT q.quartet_key AS quartet_key, COUNT(qw.id) AS n
              FROM quartets q LEFT JOIN quartet_words qw ON qw.quartet_id = q.id
             GROUP BY q.id HAVING n <> 4
            """
        )
    )
    return CheckResult(
        name="quartet_size",
        question="В каждой четвёрке ровно четыре слова",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['quartet_key']}: слов {r['n']}"),
    )


def check_conflicts_present(conn: sqlite3.Connection) -> CheckResult:
    """P0: слой конфликтов должен быть посчитан, иначе генератор не знает запретов."""
    total = int(conn.execute("SELECT COUNT(*) FROM category_conflicts").fetchone()[0])
    return CheckResult(
        name="conflicts_present",
        question="Слой конфликтов категорий заполнен",
        severity="blocker",
        count=0 if total else 1,
        examples=[] if total else ["в category_conflicts нет ни одной записи"],
        note=f"Записей: {total}. Считается командой derive-conflicts.",
    )


def check_schema_version(conn: sqlite3.Connection) -> CheckResult:
    user_version = int(conn.execute("PRAGMA user_version").fetchone()[0])
    meta = {row["key"] for row in conn.execute("SELECT key FROM schema_meta")}
    required = {"schema_version", "content_version", "git_commit", "built_at"}
    missing = sorted(required - meta)
    problems = ([] if user_version else ["PRAGMA user_version = 0"]) + [
        f"нет schema_meta.{key}" for key in missing
    ]
    return CheckResult(
        name="schema_version",
        question="У снимка есть версия схемы и контента",
        severity="warning",
        count=len(problems),
        examples=problems,
    )


def check_risk_flags_reviewed(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key, m.risk_flags AS flags
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.risk_flags LIKE '%outdated_term%'
               AND m.review_status <> 'rejected'
            """
        )
    )
    return CheckResult(
        name="risk_flags_reviewed",
        question="Нет играбельных связей с устаревшей терминологией",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']} -> {r['category_key']} {r['flags']}"),
    )


def check_candidate_queue(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.review_status = 'candidate'
             ORDER BY w.normalized
            """
        )
    )
    return CheckResult(
        name="candidate_queue",
        question="Очередь на ручную проверку (candidate)",
        severity="warning",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']} -> {r['category_key']}"),
        note="Это не ошибка: candidate означает «в игру не идёт, ждёт человека».",
    )


CHECKS: tuple[Callable[[sqlite3.Connection], CheckResult], ...] = (
    check_sqlite_integrity,
    check_familiarity_gate,
    check_sense_assignment,
    check_readiness_derived,
    check_normal_quartet_capability,
    check_semantic_incorrect_not_playable,
    check_conflicts_present,
    check_quartet_size,
    check_quartets_unique,
    check_risk_flags_reviewed,
    check_schema_version,
    check_wordplay_sense_exemption,
    check_candidate_queue,
)


def run_all(conn: sqlite3.Connection) -> list[CheckResult]:
    return [check(conn) for check in CHECKS]
