"""Слой доступа к данным: явный SQL, без ORM."""

from __future__ import annotations

import json
import sqlite3
from typing import Any, Literal

from .db import utc_now
from .models import REVIEW_STATUSES, CategoryInput, MembershipCandidateInput
from .normalization import normalize_word

UpsertResult = Literal["inserted", "updated"]

# familiarity_score = zipf / 7; 2.5 zipf ~= 0.357 — ниже этого слово считается редким
RARE_FAMILIARITY = 0.357


class RepositoryError(RuntimeError):
    """Ошибка уровня данных с понятным для пользователя сообщением."""


# --------------------------------------------------------------------------- categories


def upsert_category(conn: sqlite3.Connection, item: CategoryInput) -> UpsertResult:
    """Создаёт категорию или обновляет существующую по category_key."""
    now = utc_now()
    row = conn.execute(
        "SELECT id FROM categories WHERE category_key = ?", (item.category_key,)
    ).fetchone()
    if row is None:
        conn.execute(
            """
            INSERT INTO categories
                (category_key, label, rule, relation_type, theme,
                 base_difficulty, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item.category_key,
                item.label,
                item.rule,
                item.relation_type,
                item.theme,
                item.base_difficulty,
                item.status,
                now,
                now,
            ),
        )
        return "inserted"

    conn.execute(
        """
        UPDATE categories
           SET label = ?, rule = ?, relation_type = ?, theme = ?,
               base_difficulty = ?, status = ?, updated_at = ?
         WHERE id = ?
        """,
        (
            item.label,
            item.rule,
            item.relation_type,
            item.theme,
            item.base_difficulty,
            item.status,
            now,
            row["id"],
        ),
    )
    return "updated"


def get_category(conn: sqlite3.Connection, category_key: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM categories WHERE category_key = ?", (category_key,)
    ).fetchone()


def list_categories(
    conn: sqlite3.Connection, only_active: bool = True
) -> list[sqlite3.Row]:
    sql = "SELECT * FROM categories"
    if only_active:
        sql += " WHERE status = 'active'"
    sql += " ORDER BY category_key"
    return list(conn.execute(sql))


def category_keys(conn: sqlite3.Connection) -> set[str]:
    return {row["category_key"] for row in conn.execute("SELECT category_key FROM categories")}


# ------------------------------------------------------------------------------- words


def upsert_word(
    conn: sqlite3.Connection,
    *,
    text: str,
    language: str = "en",
    part_of_speech: str | None = None,
    is_proper_noun: bool = False,
    familiarity_score: float | None = None,
) -> int:
    """Возвращает id слова. Ключ — normalized + language, исходный text сохраняется."""
    normalized = normalize_word(text)
    now = utc_now()
    row = conn.execute(
        "SELECT * FROM words WHERE normalized = ? AND language = ?",
        (normalized, language),
    ).fetchone()
    if row is None:
        cur = conn.execute(
            """
            INSERT INTO words
                (text, normalized, language, part_of_speech, familiarity_score,
                 is_proper_noun, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, 'active', ?, ?)
            """,
            (
                text,
                normalized,
                language,
                part_of_speech,
                familiarity_score,
                int(is_proper_noun),
                now,
                now,
            ),
        )
        return int(cur.lastrowid)

    # Слово уже есть: не создаём дубль для Apple/apple, только дозаполняем пустые поля.
    new_pos = row["part_of_speech"] or part_of_speech
    new_fam = row["familiarity_score"] if row["familiarity_score"] is not None else familiarity_score
    # is_proper_noun = "встречается как имя собственное"; разделение значений живёт в word_senses
    new_proper = int(bool(row["is_proper_noun"]) or is_proper_noun)
    if (new_pos, new_fam, new_proper) != (
        row["part_of_speech"],
        row["familiarity_score"],
        row["is_proper_noun"],
    ):
        conn.execute(
            """
            UPDATE words
               SET part_of_speech = ?, familiarity_score = ?, is_proper_noun = ?, updated_at = ?
             WHERE id = ?
            """,
            (new_pos, new_fam, new_proper, now, row["id"]),
        )
    return int(row["id"])


def get_word(
    conn: sqlite3.Connection, word: str, language: str = "en"
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM words WHERE normalized = ? AND language = ?",
        (normalize_word(word), language),
    ).fetchone()


def upsert_sense(
    conn: sqlite3.Connection,
    *,
    word_id: int,
    sense_key: str,
    definition: str,
    part_of_speech: str | None = None,
) -> int:
    """Возвращает id значения слова. Ключ — word_id + sense_key."""
    row = conn.execute(
        "SELECT id, definition FROM word_senses WHERE word_id = ? AND sense_key = ?",
        (word_id, sense_key),
    ).fetchone()
    if row is None:
        cur = conn.execute(
            """
            INSERT INTO word_senses (word_id, sense_key, definition, part_of_speech, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (word_id, sense_key, definition, part_of_speech, utc_now()),
        )
        return int(cur.lastrowid)
    if definition and definition != row["definition"]:
        conn.execute(
            "UPDATE word_senses SET definition = ? WHERE id = ?", (definition, row["id"])
        )
    return int(row["id"])


def find_sense_by_definition(
    conn: sqlite3.Connection, word_id: int, definition: str
) -> sqlite3.Row | None:
    """Схлопывание почти одинаковых sense_key: точное совпадение определения."""
    return conn.execute(
        "SELECT * FROM word_senses WHERE word_id = ? AND lower(definition) = lower(?)",
        (word_id, definition.strip()),
    ).fetchone()


def list_senses(conn: sqlite3.Connection, word_id: int) -> list[sqlite3.Row]:
    return list(
        conn.execute(
            "SELECT * FROM word_senses WHERE word_id = ? ORDER BY sense_key", (word_id,)
        )
    )


# ------------------------------------------------------------------------- memberships


def upsert_membership(
    conn: sqlite3.Connection,
    *,
    word_id: int,
    sense_id: int | None,
    category_id: int,
    relation_type: str,
    reason: str,
    fit_score: float,
    obviousness_score: float,
    source: str,
    review_status: str = "candidate",
    risk_flags: list[str] | None = None,
    overwrite_review_status: bool = False,
) -> UpsertResult:
    """Создаёт связь или обновляет существующую.

    Ручное решение (approved/hard_only/rejected) не сбрасывается обратно в candidate,
    если явно не передан overwrite_review_status.
    """
    now = utc_now()
    flags_json = json.dumps(risk_flags) if risk_flags else None
    row = conn.execute(
        """
        SELECT id, review_status FROM memberships
         WHERE word_id = ? AND category_id = ? AND relation_type = ?
           AND COALESCE(sense_id, 0) = COALESCE(?, 0)
        """,
        (word_id, category_id, relation_type, sense_id),
    ).fetchone()

    if row is None:
        conn.execute(
            """
            INSERT INTO memberships
                (word_id, sense_id, category_id, relation_type, reason, fit_score,
                 obviousness_score, source, review_status, risk_flags, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                word_id,
                sense_id,
                category_id,
                relation_type,
                reason,
                fit_score,
                obviousness_score,
                source,
                review_status,
                flags_json,
                now,
                now,
            ),
        )
        return "inserted"

    current_status: str = row["review_status"]
    if overwrite_review_status:
        next_status = review_status
    elif current_status == "candidate":
        next_status = review_status
    else:
        next_status = current_status

    conn.execute(
        """
        UPDATE memberships
           SET reason = ?, fit_score = ?, obviousness_score = ?, source = ?,
               review_status = ?, risk_flags = COALESCE(?, risk_flags), updated_at = ?
         WHERE id = ?
        """,
        (
            reason,
            fit_score,
            obviousness_score,
            source,
            next_status,
            flags_json,
            now,
            row["id"],
        ),
    )
    return "updated"


def membership_exists(
    conn: sqlite3.Connection,
    *,
    word_id: int,
    category_id: int,
    relation_type: str,
    sense_id: int | None,
) -> bool:
    row = conn.execute(
        """
        SELECT 1 FROM memberships
         WHERE word_id = ? AND category_id = ? AND relation_type = ?
           AND COALESCE(sense_id, 0) = COALESCE(?, 0)
        """,
        (word_id, category_id, relation_type, sense_id),
    ).fetchone()
    return row is not None


def set_review_status(
    conn: sqlite3.Connection, membership_id: int, decision: str, comment: str | None
) -> bool:
    """Возвращает False, если связи с таким id нет."""
    if decision not in REVIEW_STATUSES:
        raise RepositoryError(
            f"Недопустимое решение {decision!r}. Разрешены: {', '.join(REVIEW_STATUSES)}"
        )
    cur = conn.execute(
        "UPDATE memberships SET review_status = ?, review_comment = ?, updated_at = ? WHERE id = ?",
        (decision, comment, utc_now(), membership_id),
    )
    return cur.rowcount > 0


MEMBERSHIP_VIEW_SQL = """
SELECT m.id                AS membership_id,
       w.text              AS word,
       w.normalized        AS normalized,
       w.language          AS language,
       s.sense_key         AS sense_key,
       s.definition        AS sense_definition,
       c.category_key      AS category_key,
       c.label             AS category_label,
       c.rule              AS category_rule,
       c.theme             AS category_theme,
       m.relation_type     AS relation_type,
       m.reason            AS reason,
       m.fit_score         AS fit_score,
       m.obviousness_score AS obviousness_score,
       m.source            AS source,
       m.review_status     AS review_status,
       m.review_comment    AS review_comment,
       m.risk_flags        AS risk_flags
  FROM memberships m
  JOIN words w      ON w.id = m.word_id
  JOIN categories c ON c.id = m.category_id
  LEFT JOIN word_senses s ON s.id = m.sense_id
"""


def _status_filter(statuses: list[str] | None) -> tuple[str, list[Any]]:
    if not statuses:
        return "", []
    placeholders = ",".join("?" for _ in statuses)
    return f" AND m.review_status IN ({placeholders})", list(statuses)


def memberships_for_word(
    conn: sqlite3.Connection,
    word: str,
    statuses: list[str] | None = None,
    language: str = "en",
) -> list[sqlite3.Row]:
    where, params = _status_filter(statuses)
    sql = (
        MEMBERSHIP_VIEW_SQL
        + " WHERE w.normalized = ? AND w.language = ?"
        + where
        + " ORDER BY c.category_key"
    )
    return list(conn.execute(sql, [normalize_word(word), language, *params]))


def memberships_for_category(
    conn: sqlite3.Connection, category_key: str, statuses: list[str] | None = None
) -> list[sqlite3.Row]:
    where, params = _status_filter(statuses)
    sql = (
        MEMBERSHIP_VIEW_SQL
        + " WHERE c.category_key = ?"
        + where
        + " ORDER BY m.obviousness_score DESC, w.normalized"
    )
    return list(conn.execute(sql, [category_key, *params]))


def memberships_by_status(
    conn: sqlite3.Connection, statuses: list[str] | None = None, limit: int | None = None
) -> list[sqlite3.Row]:
    where, params = _status_filter(statuses)
    sql = MEMBERSHIP_VIEW_SQL + " WHERE 1 = 1" + where + " ORDER BY m.id"
    if limit:
        sql += " LIMIT ?"
        params.append(limit)
    return list(conn.execute(sql, params))


def words_with_status(
    conn: sqlite3.Connection, statuses: list[str], limit: int | None = None
) -> list[str]:
    placeholders = ",".join("?" for _ in statuses)
    sql = f"""
        SELECT DISTINCT w.text AS text
          FROM memberships m JOIN words w ON w.id = m.word_id
         WHERE m.review_status IN ({placeholders})
         ORDER BY w.normalized
    """
    params: list[Any] = list(statuses)
    if limit:
        sql += " LIMIT ?"
        params.append(limit)
    return [row["text"] for row in conn.execute(sql, params)]


# ------------------------------------------------------------------------------- runs


def record_import_run(
    conn: sqlite3.Connection,
    *,
    import_type: str,
    source_file: str,
    total: int,
    inserted: int,
    updated: int,
    rejected: int,
    errors: list[dict[str, Any]] | None = None,
) -> int:
    cur = conn.execute(
        """
        INSERT INTO import_runs
            (import_type, source_file, records_total, records_inserted,
             records_updated, records_rejected, errors_json, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            import_type,
            source_file,
            total,
            inserted,
            updated,
            rejected,
            json.dumps(errors, ensure_ascii=False) if errors else None,
            utc_now(),
        ),
    )
    return int(cur.lastrowid)


def record_generation_run(
    conn: sqlite3.Connection,
    *,
    generation_type: str,
    model: str,
    prompt_version: str,
    input_json: Any = None,
    raw_output_json: str | None = None,
    parsed_output_json: Any = None,
    status: str = "ok",
    error_message: str | None = None,
) -> int:
    cur = conn.execute(
        """
        INSERT INTO generation_runs
            (generation_type, model, prompt_version, input_json, raw_output_json,
             parsed_output_json, status, error_message, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            generation_type,
            model,
            prompt_version,
            json.dumps(input_json, ensure_ascii=False) if input_json is not None else None,
            raw_output_json,
            json.dumps(parsed_output_json, ensure_ascii=False)
            if parsed_output_json is not None
            else None,
            status,
            error_message,
            utc_now(),
        ),
    )
    return int(cur.lastrowid)


# ------------------------------------------------------------------------------ stats


def coverage_report(
    conn: sqlite3.Connection, target_depth: int = 25, statuses: list[str] | None = None
) -> dict[str, Any]:
    """План работы по контенту: сколько слов не хватает каждой категории до целевой глубины."""
    where, params = ("", [])
    if statuses:
        placeholders = ",".join("?" for _ in statuses)
        where = f" AND m.review_status IN ({placeholders})"
        params = list(statuses)

    rows = list(
        conn.execute(
            f"""
            SELECT c.category_key AS category_key, c.label AS label, c.theme AS theme,
                   COUNT(m.id) AS n
              FROM categories c
              LEFT JOIN memberships m ON m.category_id = c.id{where}
             GROUP BY c.id
             ORDER BY n, c.category_key
            """,
            params,
        )
    )

    per_category = [
        {
            "category_key": row["category_key"],
            "label": row["label"],
            "theme": row["theme"],
            "have": int(row["n"]),
            "need": max(0, target_depth - int(row["n"])),
        }
        for row in rows
    ]
    by_theme: dict[str, dict[str, int]] = {}
    for item in per_category:
        bucket = by_theme.setdefault(item["theme"], {"categories": 0, "have": 0, "need": 0})
        bucket["categories"] += 1
        bucket["have"] += item["have"]
        bucket["need"] += item["need"]

    multi = int(
        conn.execute(
            """
            SELECT COUNT(*) FROM (
                SELECT word_id FROM memberships
                 GROUP BY word_id HAVING COUNT(DISTINCT category_id) > 1
            )
            """
        ).fetchone()[0]
    )
    words = int(conn.execute("SELECT COUNT(*) FROM words").fetchone()[0])

    return {
        "target_depth": target_depth,
        "categories": len(per_category),
        "words": words,
        "multi_category_words": multi,
        "multi_category_share": round(multi / words, 3) if words else 0.0,
        "memberships_needed": sum(item["need"] for item in per_category),
        "per_category": per_category,
        "by_theme": by_theme,
    }


def collect_stats(conn: sqlite3.Connection) -> dict[str, Any]:
    """Сводка по базе для команды stats."""

    def scalar(sql: str, params: tuple = ()) -> int:
        return int(conn.execute(sql, params).fetchone()[0])

    stats: dict[str, Any] = {
        "words": scalar("SELECT COUNT(*) FROM words"),
        "senses": scalar("SELECT COUNT(*) FROM word_senses"),
        "categories": scalar("SELECT COUNT(*) FROM categories"),
        "memberships": scalar("SELECT COUNT(*) FROM memberships"),
    }

    stats["by_status"] = {
        row["review_status"]: row["n"]
        for row in conn.execute(
            "SELECT review_status, COUNT(*) AS n FROM memberships GROUP BY review_status"
        )
    }

    avg_row = conn.execute(
        """
        SELECT AVG(n) AS avg_n FROM (
            SELECT COUNT(DISTINCT category_id) AS n FROM memberships GROUP BY word_id
        )
        """
    ).fetchone()
    stats["avg_categories_per_word"] = round(avg_row["avg_n"] or 0.0, 2)

    buckets = {"1": 0, "2": 0, "3": 0, "4": 0, "5+": 0}
    for row in conn.execute(
        "SELECT COUNT(DISTINCT category_id) AS n FROM memberships GROUP BY word_id"
    ):
        n = int(row["n"])
        buckets["5+" if n >= 5 else str(n)] += 1
    stats["words_by_category_count"] = buckets

    stats["thin_categories"] = [
        (row["category_key"], int(row["n"]))
        for row in conn.execute(
            """
            SELECT c.category_key AS category_key,
                   COUNT(m.id) FILTER (WHERE m.review_status = 'approved') AS n
              FROM categories c
              LEFT JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id
            HAVING n < 8
             ORDER BY n, c.category_key
            """
        )
    ]

    stats["top_words"] = [
        (row["text"], int(row["n"]))
        for row in conn.execute(
            """
            SELECT w.text AS text, COUNT(DISTINCT m.category_id) AS n
              FROM memberships m JOIN words w ON w.id = m.word_id
             WHERE m.review_status = 'approved'
             GROUP BY w.id ORDER BY n DESC, w.normalized LIMIT 20
            """
        )
    ]

    stats["rare_words"] = [
        (row["text"], row["familiarity_score"])
        for row in conn.execute(
            """
            SELECT text, familiarity_score FROM words
             WHERE familiarity_score IS NOT NULL AND familiarity_score < ?
             ORDER BY familiarity_score, normalized LIMIT 30
            """,
            (RARE_FAMILIARITY,),
        )
    ]
    stats["rare_words_total"] = int(
        conn.execute(
            "SELECT COUNT(*) FROM words WHERE familiarity_score IS NOT NULL AND familiarity_score < ?",
            (RARE_FAMILIARITY,),
        ).fetchone()[0]
    )
    stats["words_without_familiarity"] = int(
        conn.execute("SELECT COUNT(*) FROM words WHERE familiarity_score IS NULL").fetchone()[0]
    )

    stats["top_categories"] = [
        (row["category_key"], int(row["n"]))
        for row in conn.execute(
            """
            SELECT c.category_key AS category_key, COUNT(DISTINCT m.word_id) AS n
              FROM memberships m JOIN categories c ON c.id = m.category_id
             WHERE m.review_status = 'approved'
             GROUP BY c.id ORDER BY n DESC, c.category_key LIMIT 20
            """
        )
    ]
    return stats
