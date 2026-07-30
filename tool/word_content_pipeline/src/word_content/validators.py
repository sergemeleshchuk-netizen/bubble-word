"""Проверки, которым нужна база (существование категории и т.п.)."""

from __future__ import annotations

import sqlite3

from .models import REVIEW_STATUSES, MembershipCandidateInput
from .repositories import find_sense_by_definition, get_word


class ValidationIssue(ValueError):
    """Строка не прошла проверку и должна быть отклонена без остановки импорта."""


def require_category(conn: sqlite3.Connection, category_key: str) -> sqlite3.Row:
    row = conn.execute(
        "SELECT * FROM categories WHERE category_key = ?", (category_key,)
    ).fetchone()
    if row is None:
        raise ValidationIssue(
            f"Категория {category_key!r} не найдена в базе. "
            "Сначала импортируйте её через import-categories."
        )
    return row


def parse_statuses(raw: str | None) -> list[str] | None:
    """'approved,hard_only' -> ['approved', 'hard_only']; None/'' -> None (все статусы)."""
    if raw is None or not raw.strip():
        return None
    statuses = [part.strip() for part in raw.split(",") if part.strip()]
    unknown = [s for s in statuses if s not in REVIEW_STATUSES]
    if unknown:
        raise ValidationIssue(
            f"Неизвестные статусы: {unknown}. Разрешены: {', '.join(REVIEW_STATUSES)}"
        )
    return statuses


def resolve_sense_key(
    conn: sqlite3.Connection, item: MembershipCandidateInput
) -> str | None:
    """Дедупликация значений: если определение уже есть у слова, переиспользуем его sense_key."""
    if not item.sense_key or not item.sense_definition:
        return None
    word_row = get_word(conn, item.word, item.language)
    if word_row is None:
        return item.sense_key
    existing = find_sense_by_definition(conn, int(word_row["id"]), item.sense_definition)
    if existing is not None:
        return str(existing["sense_key"])
    return item.sense_key
