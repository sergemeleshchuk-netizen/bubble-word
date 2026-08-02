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

from . import sense_quality
from .db import utc_now

# Текущая целевая версия схемы: номер последнего шага в MIGRATIONS.
TARGET_VERSION = 10


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


# --------------------------------------------------------------------------- 005


def _migrate_005_quality_scores(conn: sqlite3.Connection) -> list[str]:
    """Рейтинги качества: параметры слова, названия категории и четвёрки.

    Слово и название получают собственные таблицы производных значений, а не
    колонки в `words` и `categories`. Причина простая: это кэш, целиком
    пересчитываемый командой `score-*`. Лежи он рядом с источником правды —
    его начали бы править руками, и через месяц было бы непонятно, какая
    цифра посчитана, а какая написана.

    У четвёрки, наоборот, три нужных поля уже есть (`cohesion_score`,
    `familiarity_score`, `ambiguity_pressure`), поэтому недостающие
    добавляются рядом, а не заводится вторая таблица с теми же смыслами.
    Сопоставление целиком — `docs/scoring_mapping.md`.
    """
    changes: list[str] = []

    if not _table_exists(conn, "word_scores"):
        conn.executescript(_SQL_005)
        changes.append("созданы: word_scores, category_label_scores")

    for column, definition in (
        ("min_word_familiarity", "REAL NULL"),
        ("avg_word_accessibility", "REAL NULL"),
        ("min_word_accessibility", "REAL NULL"),
        ("avg_word_length", "REAL NULL"),
        ("max_word_length", "INTEGER NULL"),
        ("quartet_clarity_score", "REAL NULL"),
        ("quartet_novelty_score", "REAL NULL"),
        ("quartet_interest_score", "REAL NULL"),
        ("quartet_quality_score", "REAL NULL"),
        ("label_quality_score", "REAL NULL"),
        ("scoring_version", "TEXT NULL"),
    ):
        added = _add_column(conn, "quartets", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    return changes


_SQL_005 = """
-- Метрики одной игровой надписи. Единица — не слово, а display form:
-- `rose` (цветок) и `Rose` (имя) живут в одной строке words, но выглядят
-- по-разному и имеют разную знакомость.
--
-- Таблица целиком производная: DELETE + пересчёт командой score-words.
CREATE TABLE IF NOT EXISTS word_scores (
    id                        INTEGER PRIMARY KEY,
    word_id                   INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    sense_id                  INTEGER NULL REFERENCES word_senses (id) ON DELETE CASCADE,
    display_text              TEXT    NOT NULL,
    char_count                INTEGER NOT NULL,
    token_count               INTEGER NOT NULL,
    display_width_score       REAL    NOT NULL,
    spelling_difficulty_score REAL    NOT NULL,
    ambiguity_score           REAL    NOT NULL,
    novelty_score             REAL    NOT NULL,
    accessibility_score       REAL    NOT NULL,
    word_quality_score        REAL    NOT NULL,
    scoring_version           TEXT    NOT NULL,
    updated_at                TEXT    NOT NULL
);

-- sense_id NULL в UNIQUE не сравнивается, поэтому ключ через COALESCE.
CREATE UNIQUE INDEX IF NOT EXISTS ux_word_scores
    ON word_scores (word_id, COALESCE(sense_id, 0));

-- Качество игровой формулировки категории. Тоже производная таблица.
CREATE TABLE IF NOT EXISTS category_label_scores (
    id                        INTEGER PRIMARY KEY,
    category_id               INTEGER NOT NULL UNIQUE
                                      REFERENCES categories (id) ON DELETE CASCADE,
    label_char_count          INTEGER NOT NULL,
    label_token_count         INTEGER NOT NULL,
    label_display_width_score REAL    NOT NULL,
    label_familiarity_score   REAL    NOT NULL,
    label_naturalness_score   REAL    NOT NULL,
    label_clarity_score       REAL    NOT NULL,
    label_specificity_score   REAL    NOT NULL,
    label_novelty_score       REAL    NOT NULL,
    label_quality_score       REAL    NOT NULL,
    scoring_version           TEXT    NOT NULL,
    updated_at                TEXT    NOT NULL
);

-- Витрина для генератора и экспорта: слово, надпись и все её метрики разом.
CREATE VIEW IF NOT EXISTS v_word_display_metrics AS
    SELECT ws.word_id, ws.sense_id, ws.display_text, ws.char_count, ws.token_count,
           w.normalized, w.familiarity_score, ws.accessibility_score,
           ws.novelty_score, ws.ambiguity_score, ws.display_width_score,
           ws.word_quality_score, ws.scoring_version
      FROM word_scores ws JOIN words w ON w.id = ws.word_id;
"""


# --------------------------------------------------------------------------- 006


# Внутренний принцип группировки. Отвечает на вопрос «почему эти четыре слова
# вместе», и это не то же самое, что надпись на оранжевом пузыре.
RULE_TYPES = (
    "taxonomy_instances",  # экземпляры класса: tulip, rose, lily -> FLOWERS
    "components",          # части целого: trunk, branch, root, bark -> TREE
    "association_hub",     # ассоциации вокруг сущности: meow, purr, whiskers -> CAT
    "context_hub",         # ассоциации вокруг ситуации: bed, blanket, dream -> SLEEP
    "property_group",      # общее свойство: red, blue, green -> COLORS
    "functional_group",    # общая функция: hammer, saw, drill -> TOOLS
    "structured_set",      # закрытый список: north, south, east, west -> COMPASS
    "sequence",            # порядок важен: monday, tuesday... -> DAYS
    "meta_collector",      # четвёрка из результатов других категорий
    "unclassified",        # тип не проставлен
)

# relation_type категории -> тип правила. Соответствие однозначное и
# детерминированное: миграция не угадывает, а переносит уже принятое решение.
_RELATION_TO_RULE_TYPE = {
    "is_a": "taxonomy_instances",
    "part_of": "components",
    "made_of": "components",
    "found_in": "context_hub",
    "used_in": "functional_group",
    "used_for": "functional_group",
    "does_action": "functional_group",
    "has_property": "property_group",
    "associated_with": "association_hub",
    "member_of_set": "structured_set",
}


def _migrate_006_reference_reproduction(conn: sqlite3.Connection) -> list[str]:
    """Библиотека авторских групп вместо онтологии слов.

    Три вещи, которые до этого шага были одной, и из-за этого генератор не мог
    воспроизвести ни одного уровня референса.

    1. **Внутреннее правило** (`categories` + новая колонка `rule_type`) —
       точный принцип: `music genres`, `musical instruments`. Нужен машине,
       чтобы доказывать связи.
    2. **Надпись** (`category_labels`) — короткое `MUSIC`, которое игрок видит
       после сборки. Одна надпись обслуживает разные правила: на уровне 3
       MUSIC — это жанры, на уровне 6 — инструменты. Раньше надпись и была
       идентификатором принципа, поэтому одно исключало другое.
    3. **Связка** (`group_rule_labels`) — какие надписи допустимы для правила.

    Дальше — то, без чего уровень референса не записывается без потерь:
    типы токенов (картинка и результат другой категории не притворяются
    словами), авторское назначение токена (`level_assignments`), спроектированные
    ловушки (`level_decoys`) и провенанс (`reference_sources`).
    """
    changes: list[str] = []

    if not _table_exists(conn, "category_labels"):
        conn.executescript(_SQL_006)
        changes.append(
            "созданы: category_labels, group_rule_labels, level_assignments, "
            "level_decoys, reference_sources, v_group_rules"
        )

    rule_check = " ".join(f"'{name}'," for name in RULE_TYPES).rstrip(",")
    for column, definition in (
        ("rule_type", f"TEXT NOT NULL DEFAULT 'unclassified' "
                      f"CHECK (rule_type IN ({rule_check}))"),
        # seed | reference_backfill. Правило, заведённое по записи оригинала,
        # остаётся в семантическом графе (cow действительно farm animal), но в
        # генерацию нового контента не идёт: это чужая авторская группа.
        ("origin", "TEXT NOT NULL DEFAULT 'seed'"),
    ):
        added = _add_column(conn, "categories", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        # Слот четвёрки — не просто слово: у него своя связь с правилом.
        ("relation_type", "TEXT NULL"),
        ("relation_strength", "REAL NULL"),
        ("obviousness", "REAL NULL"),
        ("intended_sense_key", "TEXT NULL"),
    ):
        added = _add_column(conn, "quartet_words", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("display_label_id", "INTEGER NULL REFERENCES category_labels (id) ON DELETE SET NULL"),
        ("rule_type", "TEXT NULL"),
        ("weakest_link_score", "REAL NULL"),
        ("label_retrospective_fit", "REAL NULL"),
        ("alternative_membership_count", "INTEGER NULL"),
    ):
        added = _add_column(conn, "quartets", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("origin", "TEXT NOT NULL DEFAULT 'generated'"),
        ("fixture_status", "TEXT NOT NULL DEFAULT 'none'"),
        ("reference_level", "INTEGER NULL"),
        ("recorded_completeness", "TEXT NULL"),
        ("groups_expected", "INTEGER NULL"),
        ("intended_partition_score", "REAL NULL"),
        ("best_alternative_score", "REAL NULL"),
        ("partition_margin", "REAL NULL"),
        ("planned_decoy_count", "INTEGER NOT NULL DEFAULT 0"),
        ("unplanned_decoy_count", "INTEGER NOT NULL DEFAULT 0"),
        ("meta_state", "TEXT NULL"),
    ):
        added = _add_column(conn, "level_instances", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("display_label_id", "INTEGER NULL REFERENCES category_labels (id) ON DELETE SET NULL"),
        ("label_source", "TEXT NOT NULL DEFAULT 'inferred'"),
        ("reference_name", "TEXT NULL"),
        ("emits_token_id", "INTEGER NULL"),
    ):
        added = _add_column(conn, "level_groups", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("intended_partition_score", "REAL NULL"),
        ("best_alternative_score", "REAL NULL"),
        ("partition_margin", "REAL NULL"),
        ("planned_decoy_count", "INTEGER NOT NULL DEFAULT 0"),
        ("unplanned_decoy_count", "INTEGER NOT NULL DEFAULT 0"),
        ("intended_is_best", "INTEGER NULL"),
    ):
        added = _add_column(conn, "level_solver_runs", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    for column, definition in (
        ("label_retrospective_fit", "REAL NOT NULL DEFAULT 0"),
        ("label_reveal_satisfaction", "REAL NOT NULL DEFAULT 0"),
        ("label_display_fitness", "REAL NOT NULL DEFAULT 0"),
        # label_scope — описательная характеристика, а не штраф.
        ("label_scope", "TEXT NOT NULL DEFAULT 'unknown'"),
    ):
        added = _add_column(conn, "category_label_scores", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    if _rebuild_level_tokens(conn):
        changes.append("level_tokens: word_id стал необязательным, добавлены token_kind, "
                       "token_form, pieces, picture_subject, source_group_id, observability")

    # Backfill rule_type из уже принятого relation_type. Значения по умолчанию
    # не угадываются: чего нет в таблице соответствий — остаётся unclassified.
    updated = 0
    for relation, rule_type in sorted(_RELATION_TO_RULE_TYPE.items()):
        cur = conn.execute(
            "UPDATE categories SET rule_type = ? "
            " WHERE relation_type = ? AND rule_type = 'unclassified'",
            (rule_type, relation),
        )
        updated += cur.rowcount or 0
    # Структура важнее типа связи: пары и последовательности видны явно.
    if _table_exists(conn, "structured_relations"):
        for structure, rule_type in (("pairs", "structured_set"), ("sequence", "sequence")):
            cur = conn.execute(
                "UPDATE categories SET rule_type = ? WHERE id IN "
                "(SELECT category_id FROM structured_relations WHERE structure = ?)",
                (rule_type, structure),
            )
            updated += cur.rowcount or 0
    if updated:
        changes.append(f"rule_type проставлен у {updated} правил группировки")

    # Backfill надписей: у каждого правила есть его собственная надпись.
    # Это не разделение «широкая/узкая» — это только перенос того, что уже есть,
    # чтобы новая связка не была пустой.
    if _table_exists(conn, "category_labels"):
        created = _backfill_labels(conn)
        if created:
            changes.append(f"надписей заведено: {created}")

    return changes


def _rebuild_level_tokens(conn: sqlite3.Connection) -> bool:
    """Пересобирает level_tokens: word_id больше не обязателен.

    Токен уровня перестал быть синонимом слова. Пузырь-картинка и результат
    другой категории — не lexical word, и подсовывать им какое-нибудь слово,
    лишь бы NOT NULL не ругался, значит потерять ровно ту информацию, ради
    которой всё затевалось. ALTER TABLE в SQLite снять NOT NULL не умеет,
    поэтому таблица пересобирается.
    """
    columns = _columns(conn, "level_tokens")
    if not columns or "token_kind" in columns:
        return False
    conn.executescript(
        """
        PRAGMA foreign_keys = OFF;

        CREATE TABLE level_tokens__new (
            id          INTEGER PRIMARY KEY,
            level_id    INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
            group_id    INTEGER NOT NULL REFERENCES level_groups (id) ON DELETE CASCADE,
            slot        INTEGER NOT NULL CHECK (slot BETWEEN 1 AND 4),
            -- lexical_word    — обычный пузырь со словом
            -- picture_token   — пузырь с картинкой; что на ней, в picture_subject
            -- chunked_word    — слово приходит кусочками, они в pieces
            -- category_output — результат другой категории этого уровня
            token_kind  TEXT    NOT NULL DEFAULT 'lexical_word'
                                CHECK (token_kind IN ('lexical_word', 'picture_token',
                                                      'chunked_word', 'category_output')),
            -- Форма пузыря отдельно от роли: мета-токен бывает и словом, и картинкой.
            token_form  TEXT    NOT NULL DEFAULT 'word'
                                CHECK (token_form IN ('word', 'picture', 'chunks', 'unknown')),
            word_id     INTEGER NULL     REFERENCES words (id) ON DELETE RESTRICT,
            sense_id    INTEGER NULL     REFERENCES word_senses (id) ON DELETE RESTRICT,
            sense_mode  TEXT    NOT NULL DEFAULT 'lexical',
            display_text TEXT   NOT NULL,
            role        TEXT    NULL,
            pieces      TEXT    NULL,
            picture_subject TEXT NULL,
            -- Для category_output: группа, которая выпускает этот токен.
            source_group_id INTEGER NULL REFERENCES level_groups (id) ON DELETE SET NULL,
            -- observed — пузырь виден в записи; unseen — не попал в кадр и
            -- наблюдением не является; generated — наш собственный токен.
            observability TEXT  NOT NULL DEFAULT 'generated'
                                CHECK (observability IN ('observed', 'unseen', 'generated')),
            created_at  TEXT    NOT NULL,
            UNIQUE (group_id, slot),
            UNIQUE (level_id, display_text)
        );

        INSERT INTO level_tokens__new
            (id, level_id, group_id, slot, word_id, sense_id, sense_mode,
             display_text, role, created_at)
        SELECT id, level_id, group_id, slot, word_id, sense_id, sense_mode,
               display_text, role, created_at
          FROM level_tokens;

        DROP TABLE level_tokens;
        ALTER TABLE level_tokens__new RENAME TO level_tokens;

        CREATE INDEX IF NOT EXISTS ix_level_tokens_level ON level_tokens (level_id);
        CREATE INDEX IF NOT EXISTS ix_level_tokens_group ON level_tokens (group_id);

        PRAGMA foreign_keys = ON;
        """
    )
    return True


def _backfill_labels(conn: sqlite3.Connection) -> int:
    """Заводит надпись для каждого правила, у которого её ещё нет."""
    import re as _re

    now = utc_now()
    created = 0
    rows = list(
        conn.execute(
            """
            SELECT c.id AS id, c.label AS label
              FROM categories c
             WHERE NOT EXISTS (
                   SELECT 1 FROM group_rule_labels g WHERE g.category_id = c.id)
             ORDER BY c.id
            """
        )
    )
    for row in rows:
        display = str(row["label"])
        key = _re.sub(r"[^a-z0-9]+", " ", display.lower()).strip()
        if not key:
            continue
        existing = conn.execute(
            "SELECT id FROM category_labels WHERE label_key = ?", (key,)
        ).fetchone()
        if existing is None:
            cur = conn.execute(
                """
                INSERT INTO category_labels
                    (label_key, display_text, scope, origin, created_at, updated_at)
                VALUES (?, ?, 'unknown', 'derived', ?, ?)
                """,
                (key, display, now, now),
            )
            label_id = int(cur.lastrowid)
            created += 1
        else:
            label_id = int(existing["id"])
        conn.execute(
            """
            INSERT OR IGNORE INTO group_rule_labels
                (category_id, label_id, is_primary, origin, created_at)
            VALUES (?, ?, 1, 'derived', ?)
            """,
            (int(row["id"]), label_id, now),
        )
    return created


_SQL_006 = """
-- Короткая надпись на оранжевом пузыре: то, что игрок видит ПОСЛЕ сборки.
-- Это не подсказка и не описание правила, а финальный reveal. Поэтому она
-- имеет право быть широкой: FOOD, SCHOOL, DOCTOR, BIRD.
CREATE TABLE IF NOT EXISTS category_labels (
    id           INTEGER PRIMARY KEY,
    label_key    TEXT NOT NULL UNIQUE,
    display_text TEXT NOT NULL,
    -- Описательная характеристика охвата, НЕ штраф. Широкая надпись для этой
    -- игры часто достоинство: короткое слово, под которое игрок мгновенно
    -- подставляет четвёрку.
    scope        TEXT NOT NULL DEFAULT 'unknown'
                 CHECK (scope IN ('unknown', 'broad', 'medium', 'narrow')),
    origin       TEXT NOT NULL DEFAULT 'derived',
    note         TEXT NULL,
    created_at   TEXT NOT NULL,
    updated_at   TEXT NOT NULL
);

-- Какие надписи допустимы для внутреннего правила. Связь многие-ко-многим
-- намеренно: MUSIC обслуживает и жанры, и инструменты; fast_food_dishes
-- показывается и как FOOD, и как FAST FOOD.
CREATE TABLE IF NOT EXISTS group_rule_labels (
    id          INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    label_id    INTEGER NOT NULL REFERENCES category_labels (id) ON DELETE CASCADE,
    is_primary  INTEGER NOT NULL DEFAULT 0,
    origin      TEXT    NOT NULL DEFAULT 'derived',
    note        TEXT    NULL,
    created_at  TEXT    NOT NULL,
    UNIQUE (category_id, label_id)
);

CREATE INDEX IF NOT EXISTS ix_group_rule_labels_label ON group_rule_labels (label_id);

-- Авторское назначение токена: в ЭТОМ уровне слово принадлежит вот этой группе,
-- даже если семантически подходит ещё куда-то. Семантическая правда и авторская
-- правда — разные вещи, и именно их смешение делало solver слишком строгим.
CREATE TABLE IF NOT EXISTS level_assignments (
    id            INTEGER PRIMARY KEY,
    level_id      INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    token_id      INTEGER NOT NULL REFERENCES level_tokens (id) ON DELETE CASCADE,
    home_group_id INTEGER NOT NULL REFERENCES level_groups (id) ON DELETE CASCADE,
    authority     TEXT    NOT NULL DEFAULT 'authored'
                          CHECK (authority IN ('authored', 'reference', 'derived')),
    confidence    REAL    NULL,
    note          TEXT    NULL,
    created_at    TEXT    NOT NULL,
    UNIQUE (level_id, token_id)
);

-- Правдоподобная, но не авторская связь токена. planned = 1 — спроектированная
-- ловушка (orange: fruit/color), она разрешена и хранится явно. planned = 0 —
-- незапланированная двусмысленность, повод для предупреждения.
CREATE TABLE IF NOT EXISTS level_decoys (
    id                INTEGER PRIMARY KEY,
    level_id          INTEGER NOT NULL REFERENCES level_instances (id) ON DELETE CASCADE,
    token_id          INTEGER NOT NULL REFERENCES level_tokens (id) ON DELETE CASCADE,
    decoy_group_id    INTEGER NULL REFERENCES level_groups (id) ON DELETE CASCADE,
    decoy_category_id INTEGER NULL REFERENCES categories (id) ON DELETE SET NULL,
    planned           INTEGER NOT NULL DEFAULT 0,
    plausibility      REAL    NULL,
    note              TEXT    NULL,
    created_at        TEXT    NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_level_decoys
    ON level_decoys (level_id, token_id,
                     COALESCE(decoy_group_id, 0), COALESCE(decoy_category_id, 0));

-- Провенанс: откуда взялся каждый элемент референса и был ли он реально виден.
CREATE TABLE IF NOT EXISTS reference_sources (
    id            INTEGER PRIMARY KEY,
    source_kind   TEXT    NOT NULL,
    source_file   TEXT    NOT NULL,
    level_number  INTEGER NULL,
    group_index   INTEGER NULL,
    entity_type   TEXT    NOT NULL
                          CHECK (entity_type IN ('level', 'group', 'token', 'meta_link',
                                                 'label')),
    entity_key    TEXT    NOT NULL,
    observability TEXT    NOT NULL
                          CHECK (observability IN ('observed', 'inferred', 'unseen')),
    detail        TEXT    NULL,
    created_at    TEXT    NOT NULL,
    UNIQUE (source_kind, entity_type, entity_key)
);

CREATE INDEX IF NOT EXISTS ix_reference_sources_level ON reference_sources (level_number);

-- Витрина: categories и есть внутреннее правило группировки. Отдельную таблицу
-- group_rules не заводим — на categories.id ссылаются восемнадцать тысяч связей,
-- и параллельная модель означала бы две правды вместо одной.
CREATE VIEW IF NOT EXISTS v_group_rules AS
    SELECT c.id             AS group_rule_id,
           c.category_key   AS rule_key,
           c.rule           AS rule_text,
           c.rule_type      AS rule_type,
           c.relation_type  AS relation_type,
           c.theme          AS theme,
           c.concept_id     AS concept_id,
           c.status         AS status,
           c.readiness      AS readiness,
           l.id             AS primary_label_id,
           COALESCE(l.display_text, c.label) AS primary_label
      FROM categories c
      LEFT JOIN group_rule_labels grl ON grl.category_id = c.id AND grl.is_primary = 1
      LEFT JOIN category_labels l     ON l.id = grl.label_id;
"""


# --------------------------------------------------------------------------- 007


_SQL_007 = """
-- Производные метрики SWOW по четвёрке. Считаются отдельной research-командой
-- по локальному датасету и попадают сюда снимком: обычная пересборка не должна
-- требовать 144 МБ сырых данных с research-only лицензией.
--
-- Различать «пара наблюдалась и связи нет» и «пары в датасете нет» обязательно.
-- Нуль второго рода — это отсутствие наблюдения, а не отсутствие смысла, и
-- отклонять по нему четвёрку значит наказывать за пробел в чужом датасете.
CREATE TABLE IF NOT EXISTS quartet_association_metrics (
    id                INTEGER PRIMARY KEY,
    quartet_key       TEXT    NOT NULL UNIQUE,
    metric_version    TEXT    NOT NULL,
    source_version    TEXT    NOT NULL,
    source_hash       TEXT    NOT NULL,
    -- сколько слов четвёрки вообще есть в датасете как стимул или как ответ
    observed_nodes    INTEGER NOT NULL,
    -- сколько из шести пар можно было измерить (хотя бы одно слово — стимул)
    observed_pairs    INTEGER NOT NULL,
    -- сколько измеримых пар дали ненулевую связь
    positive_pairs    INTEGER NOT NULL,
    strongest_edge    REAL    NOT NULL DEFAULT 0,
    median_edge       REAL    NOT NULL DEFAULT 0,
    -- 1 — ни одна измеримая пара не дала связи; NULL-эквивалент отсутствия
    -- данных выражен через observed_pairs = 0, а не через этот флаг
    disconnected      INTEGER NOT NULL DEFAULT 0,
    created_at        TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_quartet_assoc_key ON quartet_association_metrics (quartet_key);

-- Витрина семантики связи. Одно правило на всех: генератор, проверка
-- целостности, оценщик и CLI читают отсюда, а не считают каждый по-своему.
-- Логика продублирована в sense_quality.classify для путей, где связи в базе
-- ещё нет (фикстуры, проверка кандидата до вставки); тест держит их вместе.
CREATE VIEW IF NOT EXISTS v_membership_semantics AS
    SELECT m.id                       AS membership_id,
           m.word_id                  AS word_id,
           m.category_id              AS category_id,
           m.sense_id                 AS sense_id,
           m.sense_mode               AS sense_mode,
           m.semantic_status          AS semantic_status,
           w.dominant_sense_id        AS dominant_sense_id,
           s.sense_key                AS sense_key,
           s.sense_kind               AS sense_kind,
           COALESCE(s.accessibility_class, 'unresolved') AS accessibility_class,
           s.recognition_score        AS recognition_score,
           s.activation_score         AS activation_score,
           CASE
               WHEN m.sense_mode = 'surface_form' THEN 'surface_form'
               WHEN m.sense_id IS NULL            THEN 'unresolved'
               WHEN s.accessibility_class = 'primary'          THEN 'primary'
               WHEN s.accessibility_class = 'common_secondary' THEN 'fair_secondary'
               WHEN s.accessibility_class = 'specialist'       THEN 'specialist_trick'
               WHEN s.accessibility_class = 'obscure'          THEN 'obscure_trick'
               ELSE 'unresolved'
           END                        AS risk_class,
           CASE
               WHEN m.sense_mode = 'surface_form'    THEN 0
               WHEN m.sense_id IS NULL               THEN 0
               WHEN w.dominant_sense_id IS NULL      THEN 0
               WHEN m.sense_id <> w.dominant_sense_id THEN 1
               ELSE 0
           END                        AS uses_non_dominant,
           CASE
               WHEN m.semantic_status = 'incorrect' THEN 0
               WHEN m.sense_mode = 'surface_form'   THEN 1
               WHEN m.sense_id IS NULL              THEN 0
               WHEN COALESCE(s.accessibility_class, 'unresolved') = 'unresolved' THEN 0
               ELSE 1
           END                        AS production_eligible
      FROM memberships m
      JOIN words w            ON w.id = m.word_id
      LEFT JOIN word_senses s ON s.id = m.sense_id;
"""


def _migrate_007_sense_accessibility(conn: sqlite3.Connection) -> list[str]:
    """Слой доступности значений: чем `Trouble` в BOARD GAMES отличается от
    `orange` в COLORS.

    До этого шага база хранила «написание слова -> формально возможная
    категория» и одно число `fit_score`, у 92% связей равное 0.97. Ответить,
    какое значение используется и вспомнит ли его игрок, она не могла — поэтому
    четвёрка `Life / risk / sorry / trouble` проходила все проверки.

    Шаг разделяет три вещи, которые раньше были одной:

    1. **какое значение** — `words.dominant_sense_id` и `word_senses.dominance_rank`
       говорят, чем слово читается по умолчанию;
    2. **насколько оно доступно** — `accessibility_class` (дискретный шлюз) плюс
       `recognition_score` (узнает, если объяснить) и `activation_score`
       (вспомнит сам, увидев слово без категории). Для названия игры первое
       заметно выше второго, и одним числом это не записывается;
    3. **откуда оценка** — `quality_source` и `quality_confidence`: экспертное
       решение и производная от знакомости слова калибруются порознь.

    Отдельно появляется `categories.names_titles`. Категория BOARD GAMES держит
    не слова, а названия; обычное английское слово внутри неё почти всегда
    использует не своё главное значение. Признак нужен именно категории — иначе
    единственный способ поймать `trouble` это список слов, то есть blocklist.
    """
    changes: list[str] = []

    kinds = ", ".join(f"'{name}'" for name in sense_quality.SENSE_KINDS)
    classes = ", ".join(f"'{name}'" for name in sense_quality.ACCESSIBILITY_CLASSES)

    for column, definition in (
        ("sense_kind", f"TEXT NOT NULL DEFAULT 'lexical' CHECK (sense_kind IN ({kinds}))"),
        # 1 — значение, которым слово читается без контекста. Пусто — порядок
        # не установлен; такое слово не имеет доминантного значения, и признак
        # uses_non_dominant для него честно не считается.
        ("dominance_rank", "INTEGER NULL CHECK (dominance_rank IS NULL OR dominance_rank >= 1)"),
        ("accessibility_class", f"TEXT NOT NULL DEFAULT 'unresolved' "
                                f"CHECK (accessibility_class IN ({classes}))"),
        ("recognition_score", "REAL NULL CHECK (recognition_score IS NULL "
                              "OR recognition_score BETWEEN 0 AND 1)"),
        ("activation_score", "REAL NULL CHECK (activation_score IS NULL "
                             "OR activation_score BETWEEN 0 AND 1)"),
        ("audience_profile", "TEXT NULL"),
        ("quality_source", "TEXT NULL"),
        ("quality_confidence", "REAL NULL CHECK (quality_confidence IS NULL "
                               "OR quality_confidence BETWEEN 0 AND 1)"),
    ):
        added = _add_column(conn, "word_senses", column, definition)
        if added:
            changes.append(f"добавлена колонка {added}")

    # Ссылка на word_senses без FK: SQLite не умеет добавлять FK через
    # ALTER TABLE, а перестраивать таблицу слов ради этого дороже, чем проверить
    # ссылку в check-integrity. Проверка «доминантное значение принадлежит этому
    # же слову» там есть и является блокирующей.
    added = _add_column(conn, "words", "dominant_sense_id", "INTEGER NULL")
    if added:
        changes.append(f"добавлена колонка {added}")

    added = _add_column(conn, "categories", "names_titles", "INTEGER NOT NULL DEFAULT 0")
    if added:
        changes.append(f"добавлена колонка {added}")

    conn.executescript(_SQL_007)
    changes.append("созданы: quartet_association_metrics, v_membership_semantics")

    conn.execute(
        "CREATE INDEX IF NOT EXISTS ix_word_senses_dominance "
        "ON word_senses (word_id, dominance_rank)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS ix_word_senses_access "
        "ON word_senses (accessibility_class)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS ix_words_dominant_sense ON words (dominant_sense_id)"
    )
    changes.append("индексы: ix_word_senses_dominance, ix_word_senses_access, "
                   "ix_words_dominant_sense")

    return changes


def _migrate_008_derived_category_difficulty(conn: sqlite3.Connection) -> list[str]:
    """Сложность категории, выведенная из пула, отдельно от авторской.

    `categories.base_difficulty` заполняет источник контента одним числом на
    глаз, и замер 02.08 показал, что с содержимым категории оно не связано:
    корреляция со знакомостью слов пула −0.25, с долей имён собственных +0.03.
    Генератор фильтрует туториал и предпочитает простые категории по этому полю,
    то есть по шуму — отсюда THE MIND (0.5) в первом уровне сданного пакета при
    наличии COLORS и FRUITS. Считает новые значения `category_difficulty.derive`,
    авторское поле остаётся нетронутым как вход источника.

    Почему шаг появился только сейчас. Сначала колонки добавлялись прямо из
    модуля, в обход этого файла: на 02.08 база стояла на версии 6, а шаг 007 был
    неприменён, и запускать `migrate` ради двух колонок значило протащить
    перестройку слоя значений заодно. Шаг 007 применили — и он пересобрал
    таблицу `categories`, вместе с ней потеряв колонки, добавленные снаружи.
    Урок записан здесь: аддитивная колонка тоже обязана идти шагом.
    """
    changes: list[str] = []
    for column, definition in (
        ("derived_difficulty", "REAL NULL"),
        ("derived_difficulty_raw", "REAL NULL"),
        ("derived_difficulty_reason", "TEXT NULL"),
        ("derived_difficulty_version", "TEXT NULL"),
    ):
        added = _add_column(conn, "categories", column, definition)
        if added:
            changes.append(added)
    if not changes:
        changes.append("колонки уже на месте")
    changes.append("значения пересчитываются командой derive-category-difficulty")
    return changes


def _migrate_009_graded_obviousness(conn: sqlite3.Connection) -> list[str]:
    """Очевидность связи, отранжированная внутри категории.

    `memberships.obviousness_score` заполнял сид, и заполнял он его ПО
    КАТЕГОРИИ, а не по слову: замер 02.08 показал, что в 960 категориях из 1296
    (74%) на весь пул стоит одно значение, это 14 584 связи из 18 815 (78% базы).
    Из них 681 категория в статусе `ready`, то есть прямо сейчас идёт в уровни.

    Чем это плохо на практике. В SCHOOL SUBJECTS все 25 слов получили ровно 0.9
    — от `math` до `gym`. То есть база утверждает, что «физкультура» так же
    очевидно школьный предмет, как математика. По записанным числам `gym` в
    предметах (0.9) выходит очевиднее, чем `smile` в выражениях лица (0.75).
    Отбор слов в генераторе с 1.6.0 это поле читает, и на плоской категории ему
    нечего предпочитать.

    Точная мера объёма работы: в 878 из 960 плоских категорий есть слово, у
    которого В ДРУГОМ МЕСТЕ базы записана более высокая очевидность. Таких слов
    6116. Там плоское число не просто грубое — оно спорит с тем, что база сама
    же знает про это слово.

    Почему отдельная колонка, а не правка на месте. Тот же довод, что и у шага
    008: исходное значение остаётся входом источника, пересчёт обратим, а
    расхождение видно в любой момент. Экспорт снимка предпочитает
    `graded_obviousness`, когда она есть.

    Почему это НЕ выводится формулой. Очевидность — вопрос «вспомнит ли игрок
    это значение слова первым», и вывести её из остальных полей базы нельзя:
    все кандидаты в предикторы (частотность, число домов, fit) либо не про то,
    либо залиты так же оптом. Число домов особенно обманчиво: у `apple` их 11,
    у `orange` 6, у `star` 13 — и все трое безупречны для первых уровней, а у
    `shop` и `health` дом ровно один, и это тот самый «американская школа».
    Значит источник значений — суждение, то есть прогон модели по категории
    целиком, где слова ранжируются друг против друга.
    """
    changes: list[str] = []
    for column, definition in (
        ("graded_obviousness", "REAL NULL"),
        ("graded_obviousness_reason", "TEXT NULL"),
        ("graded_obviousness_version", "TEXT NULL"),
    ):
        added = _add_column(conn, "memberships", column, definition)
        if added:
            changes.append(added)
    if not changes:
        changes.append("колонки уже на месте")
    changes.append("значения проставляются командой grade-obviousness")
    return changes


def _migrate_010_word_register(conn: sqlite3.Connection) -> list[str]:
    """Регистр слова: бытовое, пассивное или специальное.

    Зачем понадобилось. Пол частотности (`minWordZipf` в генераторе, 02.08)
    убрал с поля `quail`, `obituary` и `congestion` — и вместе с ними всё, что
    лежит ниже 3.75. Замер показал, что порогом эти группы не разделяются
    вообще:

        congestion 3.66 (отвергнуто)   carrot 3.62 (безупречно)
        obituary   3.41 (отвергнуто)   mop    3.39 (безупречно)
        quail      3.13 (отвергнуто)   bagel  3.18, sneeze 3.19

    Слова, названные неприемлемыми, ЧАСТОТНЕЕ очевидно бытовых. Значит частотность
    измеряет не то: `omelet` (2.63) и `radish` (2.78) — слова, которые знает
    каждый, просто их редко пишут. `familiarity_score` в базе тоже не помогает,
    это тот же zipf, поделённый на 7.

    Поэтому признак не выводится, а проставляется суждением — по тому же доводу,
    что и `graded_obviousness` шагом 009:
      everyday   — вещь из повседневной жизни игрока (carrot, mop, bagel, sneeze)
      passive    — узнаёт, но сам не употребляет; на поле читается как викторина
                   (quail, obituary, congestion, basilica)
      specialist — требует знания области (tungsten, epoxy, pancreas)

    Колонка на слове, а не на связи: регистр — свойство слова, он не меняется от
    того, в какую категорию слово положили. Исходные поля не трогаются, пересчёт
    обратим, расхождение с частотностью видно в любой момент.
    """
    changes: list[str] = []
    added = _add_column(
        conn, "words", "everyday_class",
        "TEXT NULL CHECK (everyday_class IS NULL OR "
        "everyday_class IN ('everyday', 'passive', 'specialist'))",
    )
    if added:
        changes.append(added)
    for column, definition in (
        ("everyday_source", "TEXT NULL"),
        ("everyday_note", "TEXT NULL"),
    ):
        added = _add_column(conn, "words", column, definition)
        if added:
            changes.append(added)
    if not changes:
        changes.append("колонки уже на месте")
    changes.append("значения проставляются командой import-word-register")
    return changes


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
    Migration(
        version=5,
        name="quality_scores",
        description="метрики слова, названия категории и четвёрки для управляемой генерации",
        apply=_migrate_005_quality_scores,
    ),
    Migration(
        version=6,
        name="reference_reproduction",
        description="правило группировки отдельно от надписи, типы токенов, "
                    "авторские назначения и провенанс референса",
        apply=_migrate_006_reference_reproduction,
    ),
    Migration(
        version=7,
        name="sense_accessibility",
        description="доступность значения отдельно от семантической верности; "
                    "доминантное значение слова; снимок метрик SWOW по четвёрке",
        apply=_migrate_007_sense_accessibility,
    ),
    Migration(
        version=8,
        name="derived_category_difficulty",
        description="сложность категории, выведенная из пула, отдельно от авторской оценки",
        apply=_migrate_008_derived_category_difficulty,
    ),
    Migration(
        version=9,
        name="graded_obviousness",
        description="очевидность связи, отранжированная внутри категории, "
                    "отдельно от залитой оптом авторской",
        apply=_migrate_009_graded_obviousness,
    ),
    Migration(
        version=10,
        name="word_register",
        description="регистр слова: бытовое / пассивное / специальное, отдельно от частотности",
        apply=_migrate_010_word_register,
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
