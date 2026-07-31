-- Схема контентной базы: слова, значения слов, категории и связи word <-> category.
-- Все DDL идемпотентны: повторный init-db безопасен.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS words (
    id                INTEGER PRIMARY KEY,
    text              TEXT    NOT NULL,
    normalized        TEXT    NOT NULL,
    language          TEXT    NOT NULL DEFAULT 'en',
    part_of_speech    TEXT    NULL,
    familiarity_score REAL    NULL,
    is_proper_noun    INTEGER NOT NULL DEFAULT 0,
    status            TEXT    NOT NULL DEFAULT 'active',
    created_at        TEXT    NOT NULL,
    updated_at        TEXT    NOT NULL,
    UNIQUE (normalized, language)
);

CREATE TABLE IF NOT EXISTS word_senses (
    id             INTEGER PRIMARY KEY,
    word_id        INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    sense_key      TEXT    NOT NULL,
    definition     TEXT    NOT NULL,
    part_of_speech TEXT    NULL,
    created_at     TEXT    NOT NULL,
    UNIQUE (word_id, sense_key)
);

CREATE TABLE IF NOT EXISTS categories (
    id              INTEGER PRIMARY KEY,
    category_key    TEXT    NOT NULL UNIQUE,
    label           TEXT    NOT NULL,
    rule            TEXT    NOT NULL,
    relation_type   TEXT    NOT NULL,
    theme           TEXT    NOT NULL,
    base_difficulty REAL    NULL,
    -- active   — годится для автоматической сборки уровней
    -- disabled — отключена: пул не собирает нормальную четвёрку
    status          TEXT    NOT NULL DEFAULT 'active',
    -- Готовность категории к генерации уровней. Выводится из пулов
    -- командой derive-readiness, руками не правится.
    --   ready         — 4+ слов уровня approved/alternative, пул не перекошен
    --   constrained   — годится, но пул тонкий или перекошен в hard_only
    --   curated_only  — только вручную собранные четвёрки (парное или субъективное правило)
    --   hard_only     — нормальных слов нет вообще, только сложные уровни
    --   blocked       — четвёрку не собрать даже со hard_only
    readiness       TEXT    NOT NULL DEFAULT 'unknown'
                            CHECK (readiness IN
                                   ('unknown', 'ready', 'constrained', 'curated_only',
                                    'hard_only', 'blocked')),
    readiness_reason TEXT   NULL,
    created_at      TEXT    NOT NULL,
    updated_at      TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS memberships (
    id                INTEGER PRIMARY KEY,
    word_id           INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    sense_id          INTEGER NULL     REFERENCES word_senses (id) ON DELETE SET NULL,
    category_id       INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    relation_type     TEXT    NOT NULL,
    reason            TEXT    NOT NULL,
    fit_score         REAL    NOT NULL CHECK (fit_score BETWEEN 0 AND 1),
    obviousness_score REAL    NOT NULL CHECK (obviousness_score BETWEEN 0 AND 1),
    source            TEXT    NOT NULL,
    -- candidate   — ждёт проверки
    -- approved    — значение, которое игрок вспоминает первым; годится куда угодно
    -- alternative — верное и узнаваемое, но не первое значение: материал для ловушек
    -- hard_only   — верно, но игрок сам не догадается: только сложные уровни
    -- rejected    — в игру не идёт
    review_status     TEXT    NOT NULL DEFAULT 'candidate'
                              CHECK (review_status IN
                                     ('candidate', 'approved', 'alternative', 'hard_only', 'rejected')),
    -- Семантическая корректность — отдельная ось от игровой пригодности.
    -- Связь может быть correct и при этом hard_only, или approved и disputed.
    --   unreviewed — никто не смотрел глазами
    --   correct    — проверено, слово удовлетворяет правилу категории
    --   disputed   — замечание есть, решение не принято (см. manual_decisions)
    --   incorrect  — правилу не удовлетворяет; в игру не идёт независимо от review_status
    semantic_status   TEXT    NOT NULL DEFAULT 'unreviewed'
                              CHECK (semantic_status IN
                                     ('unreviewed', 'correct', 'disputed', 'incorrect')),
    -- Игровая сложность связи: производная от знакомости слова, очевидности
    -- значения и базовой сложности категории. Не путать с obviousness_score.
    gameplay_difficulty REAL  NULL CHECK (gameplay_difficulty IS NULL
                                          OR gameplay_difficulty BETWEEN 0 AND 1),
    review_comment    TEXT    NULL,
    risk_flags        TEXT    NULL,
    created_at        TEXT    NOT NULL,
    updated_at        TEXT    NOT NULL
);

-- Защита от дублей. sense_id NULL в UNIQUE-констрейнте SQLite не сравнивается,
-- поэтому нужен expression index с COALESCE.
CREATE UNIQUE INDEX IF NOT EXISTS ux_memberships_identity
    ON memberships (word_id, category_id, relation_type, COALESCE(sense_id, 0));

CREATE INDEX IF NOT EXISTS ix_memberships_category ON memberships (category_id);
CREATE INDEX IF NOT EXISTS ix_memberships_word ON memberships (word_id);
CREATE INDEX IF NOT EXISTS ix_memberships_status ON memberships (review_status);
CREATE INDEX IF NOT EXISTS ix_words_normalized ON words (normalized, language);

CREATE TABLE IF NOT EXISTS import_runs (
    id                INTEGER PRIMARY KEY,
    import_type       TEXT    NOT NULL,
    source_file       TEXT    NOT NULL,
    records_total     INTEGER NOT NULL,
    records_inserted  INTEGER NOT NULL,
    records_updated   INTEGER NOT NULL,
    records_rejected  INTEGER NOT NULL,
    errors_json       TEXT    NULL,
    created_at        TEXT    NOT NULL
);

-- Категории, которые нельзя ставить в один уровень: их пулы пересекаются настолько,
-- что четвёрка из одной может целиком лежать в другой — у уровня появляется второй
-- корректный ответ. derived — посчитано по пересечению пулов, manual — решение человека.
CREATE TABLE IF NOT EXISTS category_conflicts (
    id             INTEGER PRIMARY KEY,
    category_a_id  INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    category_b_id  INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    conflict_type  TEXT    NOT NULL
                           CHECK (conflict_type IN ('do_not_pair', 'needs_disjoint_words')),
    origin         TEXT    NOT NULL CHECK (origin IN ('derived', 'manual')),
    overlap_count  INTEGER NOT NULL DEFAULT 0,
    overlap_words  TEXT    NULL,
    severity       TEXT    NULL,
    note           TEXT    NULL,
    created_at     TEXT    NOT NULL,
    -- пара хранится один раз, порядок нормализован (a_id < b_id)
    CHECK (category_a_id < category_b_id),
    UNIQUE (category_a_id, category_b_id, conflict_type)
);

CREATE INDEX IF NOT EXISTS ix_conflicts_a ON category_conflicts (category_a_id);
CREATE INDEX IF NOT EXISTS ix_conflicts_b ON category_conflicts (category_b_id);

-- Структура парных категорий: OPPOSITES это не пул из 24 слов, а 12 пар.
-- Четвёрка для такой категории собирается только как две полные пары.
CREATE TABLE IF NOT EXISTS category_pair_groups (
    id          INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    group_key   TEXT    NOT NULL,
    word_id     INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    slot        INTEGER NOT NULL,
    created_at  TEXT    NOT NULL,
    UNIQUE (category_id, group_key, word_id)
);

-- Проверенная игровая четвёрка: ровно четыре слова одной категории, у которых
-- проверена единственность разбиения. База хранит пулы, уровни собираются отсюда.
CREATE TABLE IF NOT EXISTS quartets (
    id            INTEGER PRIMARY KEY,
    category_id   INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    quartet_key   TEXT    NOT NULL UNIQUE,
    tier          TEXT    NOT NULL CHECK (tier IN ('normal', 'hard')),
    -- auto_validated — прошла solver, человек не смотрел
    -- human_approved — подтверждена человеком
    -- rejected       — забракована
    review_state  TEXT    NOT NULL DEFAULT 'auto_validated'
                          CHECK (review_state IN ('auto_validated', 'human_approved', 'rejected')),
    solver_state  TEXT    NOT NULL DEFAULT 'unchecked'
                          CHECK (solver_state IN ('unchecked', 'unique', 'ambiguous')),
    difficulty    REAL    NULL,
    note          TEXT    NULL,
    created_at    TEXT    NOT NULL,
    updated_at    TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS quartet_words (
    id         INTEGER PRIMARY KEY,
    quartet_id INTEGER NOT NULL REFERENCES quartets (id) ON DELETE CASCADE,
    word_id    INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
    sense_id   INTEGER NULL     REFERENCES word_senses (id) ON DELETE SET NULL,
    slot       INTEGER NOT NULL CHECK (slot BETWEEN 1 AND 4),
    created_at TEXT    NOT NULL,
    UNIQUE (quartet_id, slot),
    UNIQUE (quartet_id, word_id)
);

CREATE INDEX IF NOT EXISTS ix_quartets_category ON quartets (category_id);

-- Версия схемы и контента: без неё снимок нельзя привязать к коммиту и источникам.
CREATE TABLE IF NOT EXISTS schema_meta (
    key        TEXT PRIMARY KEY,
    value      TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS generation_runs (
    id                 INTEGER PRIMARY KEY,
    generation_type    TEXT NOT NULL,
    model              TEXT NOT NULL,
    prompt_version     TEXT NOT NULL,
    input_json         TEXT NULL,
    raw_output_json    TEXT NULL,
    parsed_output_json TEXT NULL,
    status             TEXT NOT NULL,
    error_message      TEXT NULL,
    created_at         TEXT NOT NULL
);

-- Версия схемы: меняется при любом изменении структуры таблиц.
PRAGMA user_version = 2;
