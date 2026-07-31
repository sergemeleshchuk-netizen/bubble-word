"""Подключение к SQLite и создание схемы."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def utc_now() -> str:
    """Единый формат времени для всех created_at/updated_at."""
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def connect(db_path: Path | str) -> sqlite3.Connection:
    """Открывает соединение с включёнными foreign keys и доступом к колонкам по имени."""
    path = Path(db_path)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


# Колонки, добавленные после первой версии схемы. CREATE TABLE IF NOT EXISTS
# не догоняет старую базу, поэтому недостающие колонки добавляются явно.
ADDED_COLUMNS: dict[str, list[tuple[str, str]]] = {
    "categories": [
        ("readiness", "TEXT NOT NULL DEFAULT 'unknown'"),
        ("readiness_reason", "TEXT NULL"),
    ],
    "memberships": [
        ("semantic_status", "TEXT NOT NULL DEFAULT 'unreviewed'"),
        ("gameplay_difficulty", "REAL NULL"),
    ],
}


def _add_missing_columns(conn: sqlite3.Connection) -> list[str]:
    """Догоняет базу, созданную предыдущей версией схемы. Возвращает список правок."""
    applied: list[str] = []
    for table, columns in ADDED_COLUMNS.items():
        existing = {row["name"] for row in conn.execute(f"PRAGMA table_info({table})")}
        if not existing:
            continue  # таблицы ещё нет — её создаст schema.sql
        for name, definition in columns:
            if name not in existing:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {definition}")
                applied.append(f"{table}.{name}")
    return applied


def init_db(db_path: Path | str) -> Path:
    """Создаёт файл базы, все таблицы и докатывает миграции. Повторный запуск безопасен.

    Порядок важен: `schema.sql` создаёт скелет версии 2, дальше пронумерованные
    шаги из `migrations.py` доводят его до текущей версии. Так у чистой сборки
    и у существующей базы получается ровно одна и та же схема — иначе снимок,
    собранный с нуля, тихо отличался бы от рабочей базы.
    """
    from .migrations import BASE_VERSION, migrate  # локальный импорт: migrations импортирует db

    path = Path(db_path)
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn = connect(path)
    try:
        with conn:
            conn.executescript(schema_sql)
            _add_missing_columns(conn)
            if int(conn.execute("PRAGMA user_version").fetchone()[0]) == 0:
                conn.execute(f"PRAGMA user_version = {BASE_VERSION}")
        migrate(conn)
    finally:
        conn.close()
    return path


def open_existing(db_path: Path | str) -> sqlite3.Connection:
    """Открывает существующую базу; если файла или таблиц нет — понятная ошибка."""
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(
            f"База не найдена: {path}. Сначала выполните: init-db --db {path}"
        )
    conn = connect(path)
    row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='memberships'"
    ).fetchone()
    if row is None:
        conn.close()
        raise RuntimeError(
            f"В файле {path} нет таблиц пайплайна. Выполните: init-db --db {path}"
        )
    return conn


@contextmanager
def transaction(conn: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    """Явная транзакция: commit при успехе, rollback при исключении."""
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()
