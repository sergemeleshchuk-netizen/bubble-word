"""Пронумерованные миграции схемы.

Зачем отдельный модуль, если есть `schema.sql`. `CREATE TABLE IF NOT EXISTS`
создаёт таблицу, которой нет, но ничего не делает с таблицей, которая уже есть
и устарела. Пока правки были аддитивными, хватало списка недостающих колонок в
`db.ADDED_COLUMNS`. Как только понадобилось переименовать колонку и сменить
набор допустимых значений, понадобился честный механизм: шаг с номером,
условием применимости и записью факта применения.

Номер схемы живёт в `PRAGMA user_version`. Шаг применяется, только если номер
базы меньше номера шага, и поднимает номер до своего.

Каждый шаг обязан быть идемпотентным по факту: повторный `migrate` на уже
поднятой базе ничего не делает.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Callable
from dataclasses import dataclass

from .db import utc_now

# Текущая целевая версия схемы: номер последнего шага в MIGRATIONS.
TARGET_VERSION = 4


@dataclass(frozen=True)
class Migration:
    version: int
    name: str
    description: str
    apply: Callable[[sqlite3.Connection], list[str]]


def _columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row["name"] for row in conn.execute(f"PRAGMA table_info({table})")}


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return (
        conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type IN ('table','view') AND name = ?", (name,)
        ).fetchone()
        is not None
    )


def _add_column(conn: sqlite3.Connection, table: str, column: str, definition: str) -> str | None:
    if column in _columns(conn, table):
        return None
    conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
    return f"{table}.{column}"


# --------------------------------------------------------------------------- 003


def _migrate_003_sense_and_quartet_states(conn: sqlite3.Connection) -> list[str]:
    """Явный режим значения у связи и честные имена состояний четвёрки.

    Две правки, обе про то, что поле называлось не тем, чем было.

    1. `sense_id IS NULL` означало сразу две вещи: «значение не проставили» и
       «значение здесь неприменимо, связь про написание». Разводим колонкой
       `sense_mode`.
    2. `quartets.solver_state = 'unique'` читалось как «уровень с этой четвёркой
       однозначен», а проверялось совсем другое: четвёрка не лежит целиком
       в чужом пуле. Это локальная проверка одной группы. Колонка становится
       `local_check` со значениями `local_unique` / `local_ambiguous`,
       а `review_state` — `validation_state` без `human_approved`:
       стадии ручного подтверждения четвёрок в процессе нет.
    """
    changes: list[str] = []

    for column, definition in (
        # lexical | surface_form | compound | phrase_pattern (см. docs/status_semantics.md)
        ("sense_mode", "TEXT NOT NULL DEFAULT 'lexical'"),
        # valid | warning | invalid — результат машинных валидаторов, не мнение человека
        ("validation_state", "TEXT NOT NULL DEFAULT 'valid'"),
        ("validation_reasons", "TEXT NULL"),
    ):
        added = _add_column(conn, "memberships", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    # Значение бывает у слова, а написание — у пузыря. `Rose` и `rose` — одна
    # строка в words, но разные надписи на экране, и решает это значение.
    for column, definition in (
        ("display_text", "TEXT NULL"),
        ("is_proper_noun", "INTEGER NOT NULL DEFAULT 0"),
    ):
        added = _add_column(conn, "word_senses", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    # Категории игры слов работают с написанием, а не со значением слова:
    # 'starboard' не от звезды. Но `moon -> ___LIGHT` — именно от луны,
    # и такие связи значение как раз несут. Отсюда два разных режима.
    updated = conn.execute(
        """
        UPDATE memberships SET sense_mode = 'surface_form'
         WHERE relation_type IN ('phrase_before', 'phrase_after', 'wordplay')
           AND sense_mode = 'lexical' AND sense_id IS NULL
        """
    ).rowcount
    if updated:
        changes.append(f"sense_mode = surface_form у связей игры слов: {updated}")
    updated = conn.execute(
        """
        UPDATE memberships SET sense_mode = 'compound'
         WHERE relation_type IN ('phrase_before', 'phrase_after', 'wordplay')
           AND sense_mode = 'lexical' AND sense_id IS NOT NULL
        """
    ).rowcount
    if updated:
        changes.append(f"sense_mode = compound у составных со значением: {updated}")

    if "review_state" in _columns(conn, "quartets"):
        changes.extend(_rebuild_quartets(conn))

    return changes


def _rebuild_quartets(conn: sqlite3.Connection) -> list[str]:
    """Пересоздаёт quartets с новыми именами состояний, сохраняя id и состав.

    Колонку с CHECK-констрейнтом в SQLite не переименовать вместе со значениями:
    старый CHECK запретит новое значение. Поэтому документированная процедура —
    новая таблица, копирование, подмена имени.

    Тонкое место, на котором первый заход снёс все 12 800 слов четвёрок:
    `PRAGMA foreign_keys = OFF` внутри открытой транзакции — молчаливый no-op,
    и `DROP TABLE quartets` каскадом вычистил `quartet_words`. Поэтому состав
    четвёрок сохраняется во временную таблицу и восстанавливается явно: так шаг
    отработает одинаково независимо от того, включены внешние ключи или нет.
    """
    conn.commit()  # PRAGMA foreign_keys действует только вне транзакции
    conn.execute("PRAGMA foreign_keys = OFF")
    try:
        conn.execute("CREATE TEMP TABLE quartet_words_backup AS SELECT * FROM quartet_words")
        before = int(conn.execute("SELECT COUNT(*) FROM quartet_words_backup").fetchone()[0])
        conn.execute(
            """
            CREATE TABLE quartets_new (
                id               INTEGER PRIMARY KEY,
                category_id      INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
                quartet_key      TEXT    NOT NULL UNIQUE,
                tier             TEXT    NOT NULL CHECK (tier IN ('normal', 'hard')),
                validation_state TEXT    NOT NULL DEFAULT 'proposed'
                                 CHECK (validation_state IN
                                        ('proposed', 'auto_validated', 'warning',
                                         'invalid', 'disabled')),
                local_check      TEXT    NOT NULL DEFAULT 'unchecked'
                                 CHECK (local_check IN
                                        ('unchecked', 'local_unique', 'local_ambiguous')),
                difficulty       REAL    NULL,
                note             TEXT    NULL,
                created_at       TEXT    NOT NULL,
                updated_at       TEXT    NOT NULL
            )
            """
        )
        conn.execute(
            """
            INSERT INTO quartets_new
                (id, category_id, quartet_key, tier, validation_state, local_check,
                 difficulty, note, created_at, updated_at)
            SELECT id, category_id, quartet_key, tier,
                   CASE review_state
                       WHEN 'rejected' THEN 'invalid'
                       ELSE 'auto_validated'
                   END,
                   CASE solver_state
                       WHEN 'unique'    THEN 'local_unique'
                       WHEN 'ambiguous' THEN 'local_ambiguous'
                       ELSE 'unchecked'
                   END,
                   difficulty, note, created_at, updated_at
              FROM quartets
            """
        )
        moved = int(conn.execute("SELECT COUNT(*) FROM quartets_new").fetchone()[0])
        conn.execute("DROP TABLE quartets")
        conn.execute("ALTER TABLE quartets_new RENAME TO quartets")
        conn.execute("CREATE INDEX IF NOT EXISTS ix_quartets_category ON quartets (category_id)")

        conn.execute("DELETE FROM quartet_words")
        conn.execute("INSERT INTO quartet_words SELECT * FROM quartet_words_backup")
        after = int(conn.execute("SELECT COUNT(*) FROM quartet_words").fetchone()[0])
        conn.execute("DROP TABLE quartet_words_backup")
        if after != before:
            raise RuntimeError(
                f"состав четвёрок изменился при миграции: было {before}, стало {after}"
            )

        violations = list(conn.execute("PRAGMA foreign_key_check"))
        if violations:
            raise RuntimeError(
                f"после пересборки quartets нарушены внешние ключи: {violations[:3]}"
            )
        conn.commit()
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
    return [
        f"quartets пересобрана: review_state -> validation_state, "
        f"solver_state -> local_check ({moved} четвёрок, {before} слов в них)"
    ]


# --------------------------------------------------------------------------- 004


def _migrate_004_content_model(conn: sqlite3.Connection) -> list[str]:
    """Concept/variant/alias, полная модель четвёрки, структуры и уровень как сущность.

    Категория в базе всегда была игровой формулировкой — то есть variant.
    Поэтому `categories` не переименовывается и не переезжает: у неё стабильные
    id, на которые ссылаются восемнадцать тысяч связей. Над ней надстраивается
    `category_concepts` (семантический принцип) и `category_aliases`
    (другие формулировки того же принципа).
    """
    changes: list[str] = []

    if not _table_exists(conn, "category_concepts"):
        conn.executescript(_SQL_004)
        changes.append(
            "созданы: category_concepts, category_aliases, structured_relations, "
            "level_instances, level_groups, level_tokens, level_solver_runs, "
            "level_decisions, level_decision_reasons, level_dependencies, content_runs"
        )

    added = _add_column(conn, "categories", "concept_id",
                        "INTEGER NULL REFERENCES category_concepts (id) ON DELETE SET NULL")
    if added:
        changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("intended_relation", "TEXT NULL"),
        ("difficulty_tier", "TEXT NOT NULL DEFAULT 'normal'"),
        ("origin", "TEXT NOT NULL DEFAULT 'derived'"),
        ("cohesion_score", "REAL NULL"),
        ("familiarity_score", "REAL NULL"),
        ("ambiguity_pressure", "REAL NULL"),
        ("risk_state", "TEXT NOT NULL DEFAULT 'clear'"),
        ("validator_version", "TEXT NULL"),
        ("source_run_id", "INTEGER NULL"),
        ("input_hash", "TEXT NULL"),
        ("accepted_level_use_count", "INTEGER NOT NULL DEFAULT 0"),
        ("rejected_level_use_count", "INTEGER NOT NULL DEFAULT 0"),
        ("last_rejection_reason", "TEXT NULL"),
    ):
        added = _add_column(conn, "quartets", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("sense_mode", "TEXT NOT NULL DEFAULT 'lexical'"),
        ("role", "TEXT NULL"),
    ):
        added = _add_column(conn, "quartet_words", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    # Backfill: у каждой категории свой concept, пока не доказано обратное.
    # Слияние вариантов в общий concept — отдельная команда dedupe-concepts,
    # автоматически parent_child не сливается (раздел 8 задания).
    missing = int(
        conn.execute("SELECT COUNT(*) FROM categories WHERE concept_id IS NULL").fetchone()[0]
    )
    if missing:
        now = utc_now()
        rows = list(
            conn.execute(
                "SELECT id, category_key, label, theme FROM categories "
                "WHERE concept_id IS NULL ORDER BY category_key"
            )
        )
        for row in rows:
            cur = conn.execute(
                """
                INSERT INTO category_concepts (concept_key, label, theme, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT (concept_key) DO UPDATE SET updated_at = excluded.updated_at
                """,
                (row["category_key"], row["label"], row["theme"],
                 "backfill: вариант был единственным для этого принципа", now, now),
            )
            concept_id = cur.lastrowid or int(
                conn.execute(
                    "SELECT id FROM category_concepts WHERE concept_key = ?",
                    (row["category_key"],),
                ).fetchone()[0]
            )
            conn.execute(
                "UPDATE categories SET concept_id = ? WHERE id = ?", (concept_id, row["id"])
            )
        changes.append(f"backfill concept_id: {len(rows)} категорий")

    # Структуры пар переезжают в общий слой с ролями, старый слой остаётся
    # источником данных до следующей пересборки.
    moved = int(conn.execute("SELECT COUNT(*) FROM structured_relations").fetchone()[0])
    if not moved:
        now = utc_now()
        rows = list(
            conn.execute(
                "SELECT category_id, group_key, word_id, slot FROM category_pair_groups "
                "ORDER BY category_id, group_key, slot"
            )
        )
        for row in rows:
            conn.execute(
                """
                INSERT OR IGNORE INTO structured_relations
                    (category_id, structure, group_key, word_id, role, position, created_at)
                VALUES (?, 'pairs', ?, ?, ?, ?, ?)
                """,
                (row["category_id"], row["group_key"], row["word_id"],
                 "a" if int(row["slot"]) == 1 else "b", int(row["slot"]), now),
            )
        if rows:
            changes.append(f"структуры пар перенесены в structured_relations: {len(rows)} строк")

    return changes


_SQL_004 = """
-- Семантический принцип группировки. Формулировок у принципа может быть несколько
-- (BIRDS OF PREY / RAPTORS / PREDATORY BIRDS), принцип один.
CREATE TABLE IF NOT EXISTS category_concepts (
    id          INTEGER PRIMARY KEY,
    concept_key TEXT    NOT NULL UNIQUE,
    label       TEXT    NOT NULL,
    theme       TEXT    NOT NULL,
    parent_id   INTEGER NULL REFERENCES category_concepts (id) ON DELETE SET NULL,
    note        TEXT    NULL,
    created_at  TEXT    NOT NULL,
    updated_at  TEXT    NOT NULL
);

-- Другая формулировка того же принципа. Алиас НЕ становится отдельным concept:
-- иначе одна и та же тема разъезжается на пять категорий и попадает в один уровень.
CREATE TABLE IF NOT EXISTS category_aliases (
    id          INTEGER PRIMARY KEY,
    concept_id  INTEGER NOT NULL REFERENCES category_concepts (id) ON DELETE CASCADE,
    alias       TEXT    NOT NULL,
    kind        TEXT    NOT NULL DEFAULT 'alias'
                        CHECK (kind IN ('alias', 'exact_duplicate', 'near_duplicate')),
    note        TEXT    NULL,
    created_at  TEXT    NOT NULL,
    UNIQUE (concept_id, alias)
);

-- Структура категории с ролями: пары, ключ-значение, последовательности.
CREATE TABLE IF NOT EXISTS structured_relations (
    id          INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    structure   TEXT    NOT NULL CHECK (structure IN ('pairs', 'sequence')),
    group_key   TEXT    NOT NULL,
    word_id     INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    role        TEXT    NOT NULL,
    position    INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT    NOT NULL,
    UNIQUE (category_id, group_key, word_id)
);

-- Уровень — самостоятельная сущность, а не отчёт о запуске генератора.
-- Ручное решение живёт здесь и больше нигде.
CREATE TABLE IF NOT EXISTS level_instances (
    id                INTEGER PRIMARY KEY,
    level_key         TEXT    NOT NULL UNIQUE,
    target_difficulty REAL    NULL,
    difficulty_score  REAL    NULL,
    difficulty_components TEXT NULL,
    difficulty_model_version TEXT NULL,
    difficulty_explanation   TEXT NULL,
    tier              TEXT    NOT NULL DEFAULT 'normal' CHECK (tier IN ('normal', 'hard')),
    -- candidate     — собран, полная проверка не пройдена
    -- solver_valid  — solution_count == 1 и автопроверки пройдены
    -- review_pending— выгружен человеку
    -- accepted      — человек принял уровень целиком
    -- rejected      — человек отклонил
    -- needs_changes — назван конкретный дефект
    status            TEXT    NOT NULL DEFAULT 'candidate'
                              CHECK (status IN ('candidate', 'solver_valid', 'review_pending',
                                                'accepted', 'rejected', 'needs_changes')),
    solution_count    INTEGER NULL,
    review_note       TEXT    NULL,
    accepted_version  INTEGER NULL,
    content_hash      TEXT    NOT NULL,
    generator_version TEXT    NULL,
    random_seed       INTEGER NULL,
    source_run_id     INTEGER NULL,
    created_at        TEXT    NOT NULL,
    updated_at        TEXT    NOT NULL
);

-- Группа уровня ссылается на конкретную четвёрку, а не на категорию:
-- случайные четыре слова из пула в production-уровень не попадают.
CREATE TABLE IF NOT EXISTS level_groups (
    id          INTEGER PRIMARY KEY,
    level_id    INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    position    INTEGER NOT NULL,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE RESTRICT,
    quartet_id  INTEGER NULL     REFERENCES quartets (id) ON DELETE RESTRICT,
    created_at  TEXT    NOT NULL,
    UNIQUE (level_id, position),
    UNIQUE (level_id, category_id)
);

CREATE TABLE IF NOT EXISTS level_tokens (
    id          INTEGER PRIMARY KEY,
    level_id    INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    group_id    INTEGER NOT NULL REFERENCES level_groups (id) ON DELETE CASCADE,
    slot        INTEGER NOT NULL CHECK (slot BETWEEN 1 AND 4),
    word_id     INTEGER NOT NULL REFERENCES words (id) ON DELETE RESTRICT,
    sense_id    INTEGER NULL     REFERENCES word_senses (id) ON DELETE RESTRICT,
    sense_mode  TEXT    NOT NULL DEFAULT 'lexical',
    display_text TEXT   NOT NULL,
    role        TEXT    NULL,
    created_at  TEXT    NOT NULL,
    UNIQUE (group_id, slot),
    UNIQUE (level_id, display_text)
);

-- Каждый запуск solver'а сохраняется целиком: версия, вход, параметры, время.
-- Без этого «уровень проверен» — утверждение без доказательства.
CREATE TABLE IF NOT EXISTS level_solver_runs (
    id             INTEGER PRIMARY KEY,
    level_id       INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    solver_version TEXT    NOT NULL,
    input_hash     TEXT    NOT NULL,
    parameters     TEXT    NOT NULL,
    outcome        TEXT    NOT NULL
                           CHECK (outcome IN ('unique', 'ambiguous', 'unsolvable',
                                              'invalid_input', 'timeout', 'error')),
    solution_count INTEGER NOT NULL DEFAULT 0,
    alternative_partition TEXT NULL,
    reason         TEXT    NULL,
    duration_ms    INTEGER NOT NULL DEFAULT 0,
    checked_at     TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS level_decisions (
    id          INTEGER PRIMARY KEY,
    level_id    INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    decision    TEXT    NOT NULL CHECK (decision IN ('accept', 'reject', 'needs_changes')),
    review_note TEXT    NULL,
    applied_at  TEXT    NOT NULL
);

-- Точечная причина: дефект возвращается на конкретный объект, а не на всю базу.
CREATE TABLE IF NOT EXISTS level_decision_reasons (
    id           INTEGER PRIMARY KEY,
    decision_id  INTEGER NOT NULL REFERENCES level_decisions (id) ON DELETE CASCADE,
    reason_code  TEXT    NOT NULL,
    target_kind  TEXT    NULL CHECK (target_kind IN
                          ('membership', 'quartet', 'category', 'word', 'level')),
    target_ref   TEXT    NULL,
    applied      INTEGER NOT NULL DEFAULT 0,
    note         TEXT    NULL,
    created_at   TEXT    NOT NULL
);

-- Мета-цепи: решённая категория становится словом следующего уровня.
-- Таблица заведена как точка расширения, текущая playable-версия механику не умеет.
CREATE TABLE IF NOT EXISTS level_dependencies (
    id            INTEGER PRIMARY KEY,
    level_id      INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    from_group_id INTEGER NOT NULL REFERENCES level_groups (id) ON DELETE CASCADE,
    to_token_id   INTEGER NOT NULL REFERENCES level_tokens (id) ON DELETE CASCADE,
    depth         INTEGER NOT NULL DEFAULT 1,
    created_at    TEXT    NOT NULL,
    UNIQUE (level_id, from_group_id, to_token_id)
);

-- Происхождение любой автоматической генерации: чем собрано, с каким seed,
-- на каком коммите. Без этого «пересоберите и получите то же» — обещание.
CREATE TABLE IF NOT EXISTS content_runs (
    id             INTEGER PRIMARY KEY,
    run_kind       TEXT    NOT NULL,
    tool_version   TEXT    NOT NULL,
    source_commit  TEXT    NULL,
    random_seed    INTEGER NULL,
    parameters     TEXT    NULL,
    input_hash     TEXT    NULL,
    records_out    INTEGER NOT NULL DEFAULT 0,
    status         TEXT    NOT NULL DEFAULT 'ok',
    note           TEXT    NULL,
    created_at     TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_level_groups_level ON level_groups (level_id);
CREATE INDEX IF NOT EXISTS ix_level_tokens_level ON level_tokens (level_id);
CREATE INDEX IF NOT EXISTS ix_solver_runs_level ON level_solver_runs (level_id);
CREATE INDEX IF NOT EXISTS ix_structured_category ON structured_relations (category_id);

-- Проекция игровой пригодности связи на словарь задания. Именно представление,
-- а не колонка: два источника правды об одном факте рано или поздно разъедутся.
CREATE VIEW IF NOT EXISTS v_membership_eligibility AS
    SELECT m.id AS membership_id,
           CASE
               WHEN m.review_status IN ('approved', 'alternative') THEN 'normal'
               WHEN m.review_status = 'hard_only' THEN 'hard'
               ELSE 'blocked'
           END AS eligibility_tier
      FROM memberships m;
"""


MIGRATIONS: tuple[Migration, ...] = (
    Migration(
        version=3,
        name="sense_and_quartet_states",
        description="sense_mode и validation_state у связей; честные имена состояний четвёрки",
        apply=_migrate_003_sense_and_quartet_states,
    ),
    Migration(
        version=4,
        name="content_model",
        description="concept/variant/alias, полная модель четвёрки, структуры, уровень как сущность",
        apply=_migrate_004_content_model,
    ),
)


# Версия скелета из schema.sql: с неё начинается отсчёт для чистой базы.
BASE_VERSION = 2


def current_version(conn: sqlite3.Connection) -> int:
    return int(conn.execute("PRAGMA user_version").fetchone()[0])


def pending(conn: sqlite3.Connection) -> list[Migration]:
    version = current_version(conn)
    return [m for m in MIGRATIONS if m.version > version]


def migrate(conn: sqlite3.Connection, *, dry_run: bool = False) -> list[tuple[Migration, list[str]]]:
    """Применяет недостающие шаги по порядку. Возвращает [(шаг, что сделано)]."""
    applied: list[tuple[Migration, list[str]]] = []
    for migration in pending(conn):
        if dry_run:
            applied.append((migration, ["(dry-run, не применялось)"]))
            continue
        changes = migration.apply(conn)
        conn.execute(f"PRAGMA user_version = {migration.version}")
        conn.commit()
        applied.append((migration, changes))
    return applied
