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
TARGET_VERSION = 3


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


MIGRATIONS: tuple[Migration, ...] = (
    Migration(
        version=3,
        name="sense_and_quartet_states",
        description="sense_mode и validation_state у связей; честные имена состояний четвёрки",
        apply=_migrate_003_sense_and_quartet_states,
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
