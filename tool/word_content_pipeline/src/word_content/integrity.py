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
    """P0: у слова с двумя и более значениями каждая связь знает своё значение.

    Исключение — связи, которые работают с написанием слова, а не с его смыслом.
    Раньше они опознавались по типу связи, теперь по `sense_mode`: тип связи
    отвечает на вопрос «как слово относится к категории», а не «нужно ли здесь
    значение», и на этом список исключений расползался.
    """
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key,
                   (SELECT COUNT(*) FROM word_senses s WHERE s.word_id = w.id) AS senses
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.sense_id IS NULL
               AND m.review_status <> 'rejected'
               AND m.sense_mode = 'lexical'
               AND senses > 1
             ORDER BY w.normalized, c.category_key
            """
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
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.sense_id IS NULL
               AND m.sense_mode = 'surface_form'
               AND (SELECT COUNT(*) FROM word_senses s WHERE s.word_id = w.id) > 1
             ORDER BY w.normalized
            """
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


def check_quartets_local_check(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT q.quartet_key AS quartet_key, c.category_key AS category_key,
                   q.local_check AS local_check
              FROM quartets q JOIN categories c ON c.id = q.category_id
             WHERE q.validation_state NOT IN ('invalid', 'disabled')
               AND q.local_check <> 'local_unique'
            """
        )
    )
    return CheckResult(
        name="quartets_local_check",
        question="Все действующие четвёрки прошли локальную проверку",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['quartet_key']} ({r['category_key']}): {r['local_check']}"
        ),
    )


def check_surface_mode_has_no_sense(conn: sqlite3.Connection) -> CheckResult:
    """P0: `surface_form` заявляет «значение здесь не при чём» — значит его и не должно быть.

    Если у такой связи стоит sense_id, база утверждает две противоположные вещи
    одновременно. Для составных, которые смысл всё-таки наследуют
    (`moon -> ___LIGHT`), есть отдельный режим `compound`.
    """
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key, s.sense_key AS sense_key
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
              JOIN word_senses s ON s.id = m.sense_id
             WHERE m.sense_mode = 'surface_form'
             ORDER BY w.normalized
            """
        )
    )
    return CheckResult(
        name="surface_mode_has_no_sense",
        question="Связи «про написание» не тащат за собой значение слова",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['word']} -> {r['category_key']} (значение {r['sense_key']})"
        ),
    )


def check_sense_belongs_to_word(conn: sqlite3.Connection) -> CheckResult:
    """P0: значение связи должно принадлежать слову этой связи.

    Проверяется и для связей, и для слов четвёрок: перепутанный sense_id
    ловится только так — внешний ключ на word_senses про это ничего не знает.
    """
    rows = list(
        conn.execute(
            """
            SELECT 'membership' AS kind, w.text AS word, s.sense_key AS sense_key
              FROM memberships m
              JOIN words w ON w.id = m.word_id
              JOIN word_senses s ON s.id = m.sense_id
             WHERE s.word_id <> m.word_id
            UNION ALL
            SELECT 'quartet', w.text, s.sense_key
              FROM quartet_words qw
              JOIN words w ON w.id = qw.word_id
              JOIN word_senses s ON s.id = qw.sense_id
             WHERE s.word_id <> qw.word_id
            """
        )
    )
    return CheckResult(
        name="sense_belongs_to_word",
        question="Значение принадлежит своему слову",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['kind']}: {r['word']} -> {r['sense_key']}"),
    )


def check_action_relation_pos(conn: sqlite3.Connection) -> CheckResult:
    """P0: связь-действие ссылается на существительное, хотя у слова есть глагол.

    `drill -> BUILDING ACTIONS` про то, что человек сверлит, а не про предмет
    в ящике с инструментами. Пока связь указывает на `drill_tool`, база
    утверждает второе.

    Проверка намеренно узкая: она срабатывает только когда у слова уже
    заведено глагольное значение. Категорий вида «предметы, которые издают
    звук» (`bell -> CITY SOUNDS`) она не трогает — там существительное верно.
    """
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, c.category_key AS category_key,
                   s.sense_key AS sense_key,
                   (SELECT GROUP_CONCAT(v.sense_key, ', ') FROM word_senses v
                     WHERE v.word_id = w.id AND v.part_of_speech = 'verb') AS verb_senses
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
              JOIN word_senses s ON s.id = m.sense_id
             WHERE m.relation_type = 'does_action'
               AND m.sense_mode = 'lexical'
               AND m.review_status <> 'rejected'
               AND s.part_of_speech = 'noun'
               AND EXISTS (SELECT 1 FROM word_senses v
                            WHERE v.word_id = w.id AND v.part_of_speech = 'verb')
             ORDER BY w.normalized, c.category_key
            """
        )
    )
    return CheckResult(
        name="action_relation_pos",
        question="Связи «действие» не ссылаются на предмет вместо действия",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows,
            lambda r: f"{r['word']} -> {r['category_key']}: {r['sense_key']} "
                      f"(есть глагольные: {r['verb_senses']})",
        ),
        note="Значение связи задаётся в data/seed/_sense_map.json.",
    )


def check_display_collision(conn: sqlite3.Connection) -> CheckResult:
    """Два значения одного слова с одинаковой надписью на пузыре.

    `Rose` (имя) и `rose` (цветок) обязаны выглядеть по-разному, иначе в одном
    уровне окажутся два одинаковых пузыря с разными правильными ответами.
    """
    rows = list(
        conn.execute(
            """
            SELECT w.text AS word, COUNT(*) AS n,
                   GROUP_CONCAT(s.sense_key, ', ') AS senses
              FROM word_senses s
              JOIN words w ON w.id = s.word_id
             WHERE s.is_proper_noun = 1
             GROUP BY s.word_id, LOWER(COALESCE(s.display_text, w.text))
            HAVING COUNT(*) > 1
               AND COUNT(DISTINCT COALESCE(s.display_text, w.text)) = 1
             ORDER BY w.normalized
            """
        )
    )
    return CheckResult(
        name="display_collision",
        question="Значения-имена собственные с неразличимой надписью",
        severity="warning",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['word']}: {r['senses']}"),
        note="Надпись задаётся полем display в data/seed/_sense_map.json.",
    )


def check_variant_has_concept(conn: sqlite3.Connection) -> CheckResult:
    """P0: у каждой игровой формулировки должен быть семантический принцип.

    Без него две формулировки одного принципа — просто две категории, и ничто
    не мешает поставить их в один уровень.
    """
    rows = list(
        conn.execute(
            "SELECT category_key FROM categories WHERE concept_id IS NULL ORDER BY category_key"
        )
    )
    return CheckResult(
        name="variant_has_concept",
        question="У всех категорий проставлен семантический принцип",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: r["category_key"]),
        note="Проставляется миграцией и командой dedupe-concepts.",
    )


def check_alias_not_a_concept(conn: sqlite3.Connection) -> CheckResult:
    """Формулировка-алиас не должна одновременно быть отдельным принципом.

    Иначе слияние сделано наполовину: варианты сведены, а старый принцип
    остался и продолжает считаться самостоятельной темой.
    """
    rows = list(
        conn.execute(
            """
            SELECT a.alias AS alias, cc.concept_key AS concept_key
              FROM category_aliases a
              JOIN category_concepts cc ON cc.id = a.concept_id
             WHERE EXISTS (
                   SELECT 1 FROM category_concepts other
                    WHERE LOWER(other.label) = LOWER(a.alias)
                      AND other.id <> a.concept_id
                      AND EXISTS (SELECT 1 FROM categories c WHERE c.concept_id = other.id)
             )
            """
        )
    )
    return CheckResult(
        name="alias_not_a_concept",
        question="Алиас не остался отдельным принципом",
        severity="warning",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['alias']} (принцип {r['concept_key']})"),
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
    """P0: слой конфликтов должен быть посчитан, иначе генератор не знает запретов.

    Проверяется не «список непустой», а «нет ненайденных конфликтов». Пустой
    список — законный ответ для базы, где пулы категорий действительно не
    пересекаются; раньше такая база считалась непригодной, хотя с ней всё
    в порядке. Ошибка — когда пересечение есть, а записи о нём нет.
    """
    total = int(conn.execute("SELECT COUNT(*) FROM category_conflicts").fetchone()[0])
    missed = list(
        conn.execute(
            """
            WITH pool AS (
                SELECT m.category_id AS category_id, m.word_id AS word_id
                  FROM memberships m
                 WHERE m.review_status IN ('approved', 'alternative', 'hard_only')
                   AND m.semantic_status <> 'incorrect'
                 GROUP BY m.category_id, m.word_id
            )
            SELECT a.category_key AS a, b.category_key AS b, COUNT(*) AS shared
              FROM pool pa
              JOIN pool pb ON pb.word_id = pa.word_id AND pb.category_id > pa.category_id
              JOIN categories a ON a.id = pa.category_id
              JOIN categories b ON b.id = pb.category_id
             WHERE NOT EXISTS (
                   SELECT 1 FROM category_conflicts cc
                    WHERE cc.category_a_id = pa.category_id
                      AND cc.category_b_id = pb.category_id)
             GROUP BY pa.category_id, pb.category_id
            HAVING shared >= 4
             ORDER BY shared DESC
            """
        )
    )
    return CheckResult(
        name="conflicts_present",
        question="Пересечения категорий разобраны слоем конфликтов",
        severity="blocker",
        count=len(missed),
        examples=_examples(
            missed, lambda r: f"{r['a']} и {r['b']}: общих слов {r['shared']}, запрета нет"
        ),
        note=f"Записей в слое: {total}. Считается командой derive-conflicts.",
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
    check_sense_belongs_to_word,
    check_surface_mode_has_no_sense,
    check_readiness_derived,
    check_normal_quartet_capability,
    check_semantic_incorrect_not_playable,
    check_conflicts_present,
    check_variant_has_concept,
    check_alias_not_a_concept,
    check_quartet_size,
    check_quartets_local_check,
    check_risk_flags_reviewed,
    check_schema_version,
    check_action_relation_pos,
    check_display_collision,
    check_wordplay_sense_exemption,
    check_candidate_queue,
)


def run_all(conn: sqlite3.Connection) -> list[CheckResult]:
    return [check(conn) for check in CHECKS]


# --------------------------------------------------------------------- проверки уровней


def check_level_groups_cover_tokens(conn: sqlite3.Connection) -> CheckResult:
    """P0: задуманные группы обязаны покрывать все слова уровня без остатка."""
    rows = list(
        conn.execute(
            """
            SELECT l.level_key AS level_key,
                   (SELECT COUNT(*) FROM level_tokens t WHERE t.level_id = l.id) AS tokens,
                   (SELECT COUNT(*) FROM level_groups g WHERE g.level_id = l.id) AS groups
              FROM level_instances l
             WHERE tokens <> groups * 4
             ORDER BY l.level_key
            """
        )
    )
    return CheckResult(
        name="level_groups_cover_tokens",
        question="Группы уровня покрывают все слова ровно по четыре",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['level_key']}: групп {r['groups']}, слов {r['tokens']}"
        ),
    )


def check_level_solution_count(conn: sqlite3.Connection) -> CheckResult:
    """P0: уровень в статусе solver_valid и выше обязан иметь ровно одно решение."""
    rows = list(
        conn.execute(
            """
            SELECT level_key, status, COALESCE(solution_count, -1) AS solution_count
              FROM level_instances
             WHERE status IN ('solver_valid', 'review_pending', 'accepted')
               AND COALESCE(solution_count, -1) <> 1
             ORDER BY level_key
            """
        )
    )
    return CheckResult(
        name="level_solution_count",
        question="У проверенных уровней ровно одно решение",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['level_key']} ({r['status']}): решений {r['solution_count']}"
        ),
    )


def check_level_solver_outcome(conn: sqlite3.Connection) -> CheckResult:
    """P0: таймаут и ошибка solver'а не считаются успехом ни при каких условиях."""
    rows = list(
        conn.execute(
            """
            SELECT l.level_key AS level_key, r.outcome AS outcome
              FROM level_instances l
              JOIN level_solver_runs r ON r.id = (
                    SELECT MAX(id) FROM level_solver_runs WHERE level_id = l.id)
             WHERE l.status IN ('solver_valid', 'review_pending', 'accepted')
               AND r.outcome <> 'unique'
             ORDER BY l.level_key
            """
        )
    )
    return CheckResult(
        name="level_solver_outcome",
        question="Проверенные уровни прошли solver с исходом unique",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['level_key']}: {r['outcome']}"),
        note="timeout и error — это «не знаю», а не «уникально».",
    )


def check_level_duplicate_labels(conn: sqlite3.Connection) -> CheckResult:
    """P0: в одном уровне не должно быть двух одинаковых надписей категорий или пузырей."""
    rows = list(
        conn.execute(
            """
            SELECT l.level_key AS level_key, 'категория' AS kind, c.label AS value
              FROM level_groups g
              JOIN level_instances l ON l.id = g.level_id
              JOIN categories c ON c.id = g.category_id
             GROUP BY g.level_id, LOWER(c.label) HAVING COUNT(*) > 1
            UNION ALL
            SELECT l.level_key, 'пузырь', t.display_text
              FROM level_tokens t
              JOIN level_instances l ON l.id = t.level_id
             GROUP BY t.level_id, LOWER(t.display_text) HAVING COUNT(*) > 1
            """
        )
    )
    return CheckResult(
        name="level_duplicate_labels",
        question="В уровне нет повторяющихся надписей",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: f"{r['level_key']}: {r['kind']} {r['value']}"),
    )


def check_level_uses_live_quartets(conn: sqlite3.Connection) -> CheckResult:
    """P0: уровень не должен ссылаться на выключенную или забракованную четвёрку."""
    rows = list(
        conn.execute(
            """
            SELECT l.level_key AS level_key, q.quartet_key AS quartet_key,
                   q.validation_state AS state
              FROM level_groups g
              JOIN level_instances l ON l.id = g.level_id
              JOIN quartets q ON q.id = g.quartet_id
             WHERE l.status IN ('solver_valid', 'review_pending', 'accepted')
               AND q.validation_state IN ('disabled', 'invalid')
             ORDER BY l.level_key
            """
        )
    )
    return CheckResult(
        name="level_uses_live_quartets",
        question="Уровни не используют выключенные четвёрки",
        severity="blocker",
        count=len(rows),
        examples=_examples(
            rows, lambda r: f"{r['level_key']}: {r['quartet_key']} ({r['state']})"
        ),
    )


def check_accepted_level_has_hash(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            "SELECT level_key FROM level_instances "
            "WHERE status = 'accepted' AND (content_hash IS NULL OR content_hash = '')"
        )
    )
    return CheckResult(
        name="accepted_level_has_hash",
        question="У принятых уровней зафиксирован хеш содержимого",
        severity="blocker",
        count=len(rows),
        examples=_examples(rows, lambda r: r["level_key"]),
    )


def check_levels_without_solver_run(conn: sqlite3.Connection) -> CheckResult:
    rows = list(
        conn.execute(
            """
            SELECT level_key FROM level_instances l
             WHERE NOT EXISTS (SELECT 1 FROM level_solver_runs r WHERE r.level_id = l.id)
            """
        )
    )
    return CheckResult(
        name="levels_without_solver_run",
        question="У каждого уровня сохранён отчёт о запуске solver'а",
        severity="warning",
        count=len(rows),
        examples=_examples(rows, lambda r: r["level_key"]),
        note="Без отчёта «уровень проверен» — утверждение без доказательства.",
    )


LEVEL_CHECKS: tuple[Callable[[sqlite3.Connection], CheckResult], ...] = (
    check_level_groups_cover_tokens,
    check_level_solution_count,
    check_level_solver_outcome,
    check_level_duplicate_labels,
    check_level_uses_live_quartets,
    check_accepted_level_has_hash,
    check_levels_without_solver_run,
)


def run_level_checks(conn: sqlite3.Connection) -> list[CheckResult]:
    return [check(conn) for check in LEVEL_CHECKS]
