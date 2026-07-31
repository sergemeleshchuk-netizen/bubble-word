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


def init_db(db_path: Path | str) -> Path:
    """Создаёт файл базы и все таблицы. Повторный запуск безопасен."""
    path = Path(db_path)
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn = connect(path)
    try:
        with conn:
            conn.executescript(schema_sql)
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
