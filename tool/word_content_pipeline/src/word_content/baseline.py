"""Снимок метрик базы: одна команда вместо десятка ручных SQL-запросов.

Зачем отдельный модуль. Любое изменение схемы или пайплайна нужно уметь
показать числами «до» и «после». Пока метрики считались вручную, сравнение
before/after было пересказом, а не замером: цифры брались из разных запусков
и разных фильтров. Здесь один набор запросов, который печатается и в текст,
и в JSON — JSON кладём рядом с отчётом и сравниваем машинно.

Метрик `human-approved quartets` здесь нет намеренно: ручная приёмка живёт
на уровне (`level_instances.status`), а не на словах, связях и четвёрках.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


def _scalar(conn: sqlite3.Connection, sql: str, params: tuple[Any, ...] = ()) -> int:
    row = conn.execute(sql, params).fetchone()
    return 0 if row is None or row[0] is None else int(row[0])


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name = ?", (name,)
    ).fetchone()
    return row is not None


def _grouped(conn: sqlite3.Connection, sql: str) -> dict[str, int]:
    return {str(row[0]): int(row[1]) for row in conn.execute(sql)}


def collect(conn: sqlite3.Connection) -> dict[str, Any]:
    """Полный набор метрик. Ключи стабильны: по ним делается diff before/after."""
    report: dict[str, Any] = {}

    report["words"] = _scalar(conn, "SELECT COUNT(*) FROM words")
    report["words_with_familiarity"] = _scalar(
        conn, "SELECT COUNT(*) FROM words WHERE familiarity_score IS NOT NULL"
    )
    report["words_proper_noun"] = _scalar(
        conn, "SELECT COUNT(*) FROM words WHERE is_proper_noun = 1"
    )
    report["word_senses"] = _scalar(conn, "SELECT COUNT(*) FROM word_senses")
    report["words_polysemous"] = _scalar(
        conn,
        "SELECT COUNT(*) FROM (SELECT word_id FROM word_senses "
        "GROUP BY word_id HAVING COUNT(*) > 1)",
    )

    # Категории. concept появляется в схеме v3: до миграции concepts == variants.
    report["category_variants"] = _scalar(conn, "SELECT COUNT(*) FROM categories")
    report["category_concepts"] = (
        _scalar(conn, "SELECT COUNT(*) FROM category_concepts")
        if _table_exists(conn, "category_concepts")
        else 0
    )
    report["category_aliases"] = (
        _scalar(conn, "SELECT COUNT(*) FROM category_aliases")
        if _table_exists(conn, "category_aliases")
        else 0
    )
    report["categories_by_readiness"] = _grouped(
        conn, "SELECT readiness, COUNT(*) FROM categories GROUP BY 1 ORDER BY 1"
    )
    report["categories_by_status"] = _grouped(
        conn, "SELECT status, COUNT(*) FROM categories GROUP BY 1 ORDER BY 1"
    )

    report["memberships"] = _scalar(conn, "SELECT COUNT(*) FROM memberships")
    report["memberships_by_review_status"] = _grouped(
        conn, "SELECT review_status, COUNT(*) FROM memberships GROUP BY 1 ORDER BY 1"
    )
    report["memberships_by_semantic_status"] = _grouped(
        conn, "SELECT semantic_status, COUNT(*) FROM memberships GROUP BY 1 ORDER BY 1"
    )
    report["memberships_with_sense"] = _scalar(
        conn, "SELECT COUNT(*) FROM memberships WHERE sense_id IS NOT NULL"
    )
    if _column_exists(conn, "memberships", "sense_mode"):
        report["memberships_by_sense_mode"] = _grouped(
            conn, "SELECT sense_mode, COUNT(*) FROM memberships GROUP BY 1 ORDER BY 1"
        )
    if _column_exists(conn, "memberships", "eligibility_tier"):
        report["memberships_by_eligibility_tier"] = _grouped(
            conn, "SELECT eligibility_tier, COUNT(*) FROM memberships GROUP BY 1 ORDER BY 1"
        )

    report["quartets"] = _scalar(conn, "SELECT COUNT(*) FROM quartets")
    report["quartet_tokens"] = _scalar(conn, "SELECT COUNT(*) FROM quartet_words")
    report["quartet_tokens_with_sense"] = _scalar(
        conn, "SELECT COUNT(*) FROM quartet_words WHERE sense_id IS NOT NULL"
    )
    state_column = (
        "validation_state" if _column_exists(conn, "quartets", "validation_state") else "review_state"
    )
    report["quartets_by_validation_state"] = _grouped(
        conn, f"SELECT {state_column}, COUNT(*) FROM quartets GROUP BY 1 ORDER BY 1"
    )
    report["quartets_by_tier"] = _grouped(
        conn, "SELECT tier, COUNT(*) FROM quartets GROUP BY 1 ORDER BY 1"
    )
    if _column_exists(conn, "quartets", "origin"):
        report["quartets_by_origin"] = _grouped(
            conn, "SELECT origin, COUNT(*) FROM quartets GROUP BY 1 ORDER BY 1"
        )
    report["categories_without_quartets"] = _scalar(
        conn,
        "SELECT COUNT(*) FROM categories c WHERE NOT EXISTS "
        "(SELECT 1 FROM quartets q WHERE q.category_id = c.id)",
    )
    report["category_conflicts"] = _scalar(conn, "SELECT COUNT(*) FROM category_conflicts")
    report["structured_groups"] = _scalar(
        conn, "SELECT COUNT(DISTINCT group_key) FROM category_pair_groups"
    )

    # Уровни. Таблиц может ещё не быть — тогда метрики нулевые, но ключи есть.
    if _table_exists(conn, "level_instances"):
        report["level_candidates"] = _scalar(conn, "SELECT COUNT(*) FROM level_instances")
        report["levels_by_status"] = _grouped(
            conn, "SELECT status, COUNT(*) FROM level_instances GROUP BY 1 ORDER BY 1"
        )
        report["levels_solver_valid"] = _scalar(
            conn, "SELECT COUNT(*) FROM level_instances WHERE solution_count = 1"
        )
        report["levels_ambiguous"] = _scalar(
            conn, "SELECT COUNT(*) FROM level_instances WHERE solution_count > 1"
        )
        report["levels_solver_timeout"] = _scalar(
            conn,
            "SELECT COUNT(*) FROM level_solver_runs WHERE outcome = 'timeout'",
        )
        report["quartets_in_accepted_levels"] = _scalar(
            conn,
            "SELECT COUNT(DISTINCT g.quartet_id) FROM level_groups g "
            "JOIN level_instances l ON l.id = g.level_id "
            "WHERE l.status = 'accepted' AND g.quartet_id IS NOT NULL",
        )
        report["level_rejection_reasons"] = _grouped(
            conn,
            "SELECT reason_code, COUNT(*) FROM level_decision_reasons GROUP BY 1 ORDER BY 1",
        ) if _table_exists(conn, "level_decision_reasons") else {}
    else:
        report["level_candidates"] = 0
        report["levels_by_status"] = {}
        report["levels_solver_valid"] = 0
        report["levels_ambiguous"] = 0
        report["levels_solver_timeout"] = 0
        report["quartets_in_accepted_levels"] = 0
        report["level_rejection_reasons"] = {}

    report["schema_version"] = _scalar(conn, "PRAGMA user_version")
    report["schema_meta"] = {
        str(row["key"]): str(row["value"]) for row in conn.execute("SELECT key, value FROM schema_meta")
    }
    return report


def _column_exists(conn: sqlite3.Connection, table: str, column: str) -> bool:
    return any(row["name"] == column for row in conn.execute(f"PRAGMA table_info({table})"))


def render_text(report: dict[str, Any]) -> str:
    """Плоский человекочитаемый вид: ключ = значение, вложенное с отступом."""
    lines: list[str] = []
    for key, value in report.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            for sub_key, sub_value in value.items():
                shown = sub_value if len(str(sub_value)) <= 60 else str(sub_value)[:57] + "…"
                lines.append(f"    {sub_key}: {shown}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)


def write_json(path: Path, report: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
                    encoding="utf-8")
    return path


def diff(before: dict[str, Any], after: dict[str, Any]) -> list[tuple[str, Any, Any]]:
    """Плоский diff двух снимков: (метрика, было, стало). Только изменившееся."""
    flat_before = _flatten(before)
    flat_after = _flatten(after)
    keys = sorted(set(flat_before) | set(flat_after))
    return [
        (key, flat_before.get(key, "—"), flat_after.get(key, "—"))
        for key in keys
        if flat_before.get(key) != flat_after.get(key)
    ]


def _flatten(report: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    flat: dict[str, Any] = {}
    for key, value in report.items():
        full = f"{prefix}{key}"
        if isinstance(value, dict):
            flat.update(_flatten(value, prefix=f"{full}."))
        else:
            flat[full] = value
    return flat
