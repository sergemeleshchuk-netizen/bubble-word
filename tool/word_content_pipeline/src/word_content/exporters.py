"""Экспорт данных из SQLite в CSV/JSONL."""

from __future__ import annotations

import csv
import json
import sqlite3
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .importers import REVIEW_CSV_COLUMNS
from .repositories import memberships_by_status


def export_review_csv(
    conn: sqlite3.Connection, path: Path, statuses: list[str] | None = None
) -> int:
    """Выгружает связи для ручной проверки. decision и review_comment остаются пустыми."""
    rows = memberships_by_status(conn, statuses)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "membership_id": row["membership_id"],
                    "word": row["word"],
                    "normalized": row["normalized"],
                    "familiarity": row["familiarity_score"]
                    if row["familiarity_score"] is not None
                    else "",
                    "sense_key": row["sense_key"] or "",
                    "sense_definition": row["sense_definition"] or "",
                    "category_key": row["category_key"],
                    "category_label": row["category_label"],
                    "category_rule": row["category_rule"],
                    "relation_type": row["relation_type"],
                    "reason": row["reason"],
                    "fit_score": row["fit_score"],
                    "obviousness_score": row["obviousness_score"],
                    "source": row["source"],
                    "current_status": row["review_status"],
                    "decision": "",
                    "review_comment": "",
                }
            )
    return len(rows)


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> int:
    """Пишет записи как JSONL (одна JSON-запись на строку)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count
