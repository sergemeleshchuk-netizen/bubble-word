"""Поиск слов, которым нужны дополнительные значения.

Замечание аудита (P0): 736 часто переиспользуемых слов встречаются минимум
в четырёх играбельных категориях из нескольких тем, но значений у них нет вообще —
`bell`, `rose`, `siren`, `cricket`, `iris`. База не может ответить, в каком смысле
слово стоит в категории, значит генератор соберёт четвёрку из разных смыслов.

Механизм не принимает решений: он выдаёт очередь работы. Слово попадает в очередь,
если живёт в разных ассоциативных областях, и не попадает, если уже разобрано
(значения есть) или признано однозначным вручную (`_not_homonyms.txt`).
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .normalization import normalize_word
from .readiness import PLAYABLE_STATUSES

MIN_CATEGORIES = 4
MIN_THEMES = 3


@dataclass(frozen=True)
class SenseGap:
    word: str
    normalized: str
    is_proper_noun: bool
    familiarity_score: float | None
    category_count: int
    theme_count: int
    categories: tuple[str, ...]
    themes: tuple[str, ...]

    @property
    def priority(self) -> str:
        """P0 — слово растащено по многим темам, ошибка почти гарантирована."""
        if self.theme_count >= 6 or self.category_count >= 10:
            return "P0"
        if self.theme_count >= 4:
            return "P1"
        return "P2"


def load_not_homonyms(path: Path) -> set[str]:
    """Слова, вручную признанные однозначными: детектор их не предлагает повторно."""
    if not path.exists():
        return set()
    words: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if line:
            words.add(normalize_word(line))
    return words


def find(
    conn: sqlite3.Connection,
    *,
    not_homonyms: set[str] | None = None,
    min_categories: int = MIN_CATEGORIES,
    min_themes: int = MIN_THEMES,
) -> list[SenseGap]:
    not_homonyms = not_homonyms or set()
    placeholders = ",".join("?" for _ in PLAYABLE_STATUSES)
    rows = conn.execute(
        f"""
        SELECT w.id AS word_id, w.text AS word, w.normalized AS normalized,
               w.is_proper_noun AS is_proper_noun, w.familiarity_score AS familiarity_score,
               c.category_key AS category_key, c.theme AS theme
          FROM memberships m
          JOIN words w      ON w.id = m.word_id
          JOIN categories c ON c.id = m.category_id
         WHERE m.review_status IN ({placeholders})
           AND NOT EXISTS (SELECT 1 FROM word_senses s WHERE s.word_id = w.id)
        """,
        PLAYABLE_STATUSES,
    )

    grouped: dict[str, dict] = {}
    for row in rows:
        bucket = grouped.setdefault(
            row["normalized"],
            {
                "word": row["word"],
                "is_proper_noun": bool(row["is_proper_noun"]),
                "familiarity_score": row["familiarity_score"],
                "categories": set(),
                "themes": set(),
            },
        )
        bucket["categories"].add(row["category_key"])
        bucket["themes"].add(row["theme"])

    gaps = [
        SenseGap(
            word=data["word"],
            normalized=normalized,
            is_proper_noun=data["is_proper_noun"],
            familiarity_score=data["familiarity_score"],
            category_count=len(data["categories"]),
            theme_count=len(data["themes"]),
            categories=tuple(sorted(data["categories"])),
            themes=tuple(sorted(data["themes"])),
        )
        for normalized, data in grouped.items()
        if normalized not in not_homonyms
        and len(data["categories"]) >= min_categories
        and len(data["themes"]) >= min_themes
    ]
    gaps.sort(key=lambda gap: (-gap.theme_count, -gap.category_count, gap.normalized))
    return gaps


def to_rows(gaps: list[SenseGap]) -> list[dict[str, object]]:
    """Строки для data/sense_review_queue.csv."""
    return [
        {
            "priority": gap.priority,
            "word": gap.word,
            "normalized": gap.normalized,
            "is_proper_noun": int(gap.is_proper_noun),
            "familiarity": gap.familiarity_score if gap.familiarity_score is not None else "",
            "category_count": gap.category_count,
            "theme_count": gap.theme_count,
            "themes": " | ".join(gap.themes),
            "categories": " | ".join(gap.categories),
            "decision": "",
            "note": "",
        }
        for gap in gaps
    ]
