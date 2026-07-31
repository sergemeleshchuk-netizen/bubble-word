"""Тесты миграций схемы.

Главный тест здесь — сохранность состава четвёрок. Первый заход на миграцию 003
пересобирал таблицу `quartets` и молча удалил все 12 800 слов четвёрок:
`PRAGMA foreign_keys = OFF` внутри открытой транзакции ничего не отключает,
и `DROP TABLE` ушёл каскадом. Тест воспроизводит ровно ту ситуацию — база с
данными и открытая транзакция перед миграцией.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from word_content import migrations
from word_content.db import connect, utc_now

SCHEMA_V2 = Path(__file__).resolve().parents[1] / "src" / "word_content" / "schema.sql"


def _legacy_db(path: Path) -> sqlite3.Connection:
    """База версии 2: старые имена колонок четвёрки, без sense_mode."""
    conn = connect(path)
    conn.executescript(
        """
        CREATE TABLE words (
            id INTEGER PRIMARY KEY, text TEXT NOT NULL, normalized TEXT NOT NULL,
            language TEXT NOT NULL DEFAULT 'en', part_of_speech TEXT NULL,
            familiarity_score REAL NULL, is_proper_noun INTEGER NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'active', created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL, UNIQUE (normalized, language));
        CREATE TABLE word_senses (
            id INTEGER PRIMARY KEY,
            word_id INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
            sense_key TEXT NOT NULL, definition TEXT NOT NULL,
            part_of_speech TEXT NULL, created_at TEXT NOT NULL,
            UNIQUE (word_id, sense_key));
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY, category_key TEXT NOT NULL UNIQUE, label TEXT NOT NULL,
            rule TEXT NOT NULL, relation_type TEXT NOT NULL, theme TEXT NOT NULL,
            base_difficulty REAL NULL, status TEXT NOT NULL DEFAULT 'active',
            readiness TEXT NOT NULL DEFAULT 'unknown', readiness_reason TEXT NULL,
            created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE TABLE memberships (
            id INTEGER PRIMARY KEY,
            word_id INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
            sense_id INTEGER NULL REFERENCES word_senses (id) ON DELETE SET NULL,
            category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
            relation_type TEXT NOT NULL, reason TEXT NOT NULL,
            fit_score REAL NOT NULL, obviousness_score REAL NOT NULL, source TEXT NOT NULL,
            review_status TEXT NOT NULL DEFAULT 'candidate',
            semantic_status TEXT NOT NULL DEFAULT 'unreviewed',
            gameplay_difficulty REAL NULL, review_comment TEXT NULL, risk_flags TEXT NULL,
            created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE TABLE quartets (
            id INTEGER PRIMARY KEY,
            category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
            quartet_key TEXT NOT NULL UNIQUE,
            tier TEXT NOT NULL CHECK (tier IN ('normal', 'hard')),
            review_state TEXT NOT NULL DEFAULT 'auto_validated'
                CHECK (review_state IN ('auto_validated', 'human_approved', 'rejected')),
            solver_state TEXT NOT NULL DEFAULT 'unchecked'
                CHECK (solver_state IN ('unchecked', 'unique', 'ambiguous')),
            difficulty REAL NULL, note TEXT NULL,
            created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE TABLE quartet_words (
            id INTEGER PRIMARY KEY,
            quartet_id INTEGER NOT NULL REFERENCES quartets (id) ON DELETE CASCADE,
            word_id INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
            sense_id INTEGER NULL REFERENCES word_senses (id) ON DELETE SET NULL,
            slot INTEGER NOT NULL CHECK (slot BETWEEN 1 AND 4), created_at TEXT NOT NULL,
            UNIQUE (quartet_id, slot), UNIQUE (quartet_id, word_id));
        CREATE TABLE category_pair_groups (
            id INTEGER PRIMARY KEY,
            category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
            group_key TEXT NOT NULL,
            word_id INTEGER NOT NULL REFERENCES words (id) ON DELETE CASCADE,
            slot INTEGER NOT NULL, created_at TEXT NOT NULL,
            UNIQUE (category_id, group_key, word_id));
        PRAGMA user_version = 2;
        """
    )
    now = utc_now()
    conn.execute(
        "INSERT INTO categories (id, category_key, label, rule, relation_type, theme,"
        " created_at, updated_at) VALUES (1, 'trees', 'TREES', 'Common trees', 'is_a',"
        " 'nature', ?, ?)",
        (now, now),
    )
    for index, word in enumerate(("oak", "maple", "birch", "pine"), start=1):
        conn.execute(
            "INSERT INTO words (id, text, normalized, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?)",
            (index, word, word, now, now),
        )
        conn.execute(
            "INSERT INTO memberships (word_id, category_id, relation_type, reason,"
            " fit_score, obviousness_score, source, review_status, created_at, updated_at)"
            " VALUES (?, 1, 'is_a', 'дерево', 0.9, 0.9, 'seed', 'approved', ?, ?)",
            (index, now, now),
        )
    conn.execute(
        "INSERT INTO quartets (id, category_id, quartet_key, tier, review_state,"
        " solver_state, created_at, updated_at)"
        " VALUES (1, 1, 'trees__1', 'normal', 'auto_validated', 'unique', ?, ?)",
        (now, now),
    )
    for slot in range(1, 5):
        conn.execute(
            "INSERT INTO quartet_words (quartet_id, word_id, slot, created_at)"
            " VALUES (1, ?, ?, ?)",
            (slot, slot, now),
        )
    conn.commit()
    return conn


@pytest.fixture
def legacy(tmp_path: Path):
    conn = _legacy_db(tmp_path / "legacy.sqlite")
    yield conn
    conn.close()


def test_migration_preserves_quartet_tokens(legacy):
    """Состав четвёрок не должен теряться при пересборке таблицы."""
    before = list(legacy.execute("SELECT quartet_id, word_id, slot FROM quartet_words ORDER BY slot"))
    migrations.migrate(legacy)
    after = list(legacy.execute("SELECT quartet_id, word_id, slot FROM quartet_words ORDER BY slot"))
    assert [tuple(row) for row in after] == [tuple(row) for row in before]
    assert len(after) == 4


def test_migration_survives_open_transaction(legacy):
    """Ровно та ошибка, что была: открытая транзакция глушит PRAGMA foreign_keys."""
    legacy.execute("UPDATE memberships SET review_comment = 'открыли транзакцию'")
    assert legacy.in_transaction
    migrations.migrate(legacy)
    count = legacy.execute("SELECT COUNT(*) FROM quartet_words").fetchone()[0]
    assert count == 4


def test_migration_keeps_stable_ids(legacy):
    migrations.migrate(legacy)
    row = legacy.execute("SELECT id, quartet_key FROM quartets").fetchone()
    assert row["id"] == 1
    assert row["quartet_key"] == "trees__1"


def test_migration_renames_states(legacy):
    migrations.migrate(legacy)
    row = legacy.execute("SELECT validation_state, local_check FROM quartets").fetchone()
    assert row["validation_state"] == "auto_validated"
    assert row["local_check"] == "local_unique"
    columns = {r["name"] for r in legacy.execute("PRAGMA table_info(quartets)")}
    assert "review_state" not in columns and "solver_state" not in columns


def test_no_human_approved_anywhere(legacy):
    """Ручного подтверждения на базовых сущностях в схеме быть не должно."""
    migrations.migrate(legacy)
    sql = "\n".join(
        row[0] or "" for row in legacy.execute("SELECT sql FROM sqlite_master")
    )
    assert "human_approved" not in sql


def test_migration_is_idempotent(legacy):
    migrations.migrate(legacy)
    version = migrations.current_version(legacy)
    assert migrations.migrate(legacy) == []
    assert migrations.current_version(legacy) == version


def test_wordplay_relations_get_surface_mode(legacy):
    legacy.execute(
        "INSERT INTO memberships (word_id, category_id, relation_type, reason, fit_score,"
        " obviousness_score, source, review_status, created_at, updated_at)"
        " VALUES (1, 1, 'phrase_before', 'игра слов', 0.8, 0.8, 'seed', 'approved',"
        " '2026-01-01T00:00:00+00:00', '2026-01-01T00:00:00+00:00')"
    )
    legacy.commit()
    migrations.migrate(legacy)
    row = legacy.execute(
        "SELECT sense_mode FROM memberships WHERE relation_type = 'phrase_before'"
    ).fetchone()
    assert row["sense_mode"] == "surface_form"
