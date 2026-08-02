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


# --------------------------------------------------------------- очередь по связям


@dataclass(frozen=True)
class UnresolvedMembership:
    """Связь без разрешённого значения — с контекстом, по которому видно срочность."""

    membership_id: int
    word: str
    normalized: str
    category_key: str
    sense_id: int | None
    accessibility_class: str
    membership_count: int
    used_in_levels: int
    used_in_quartets: int
    names_titles: bool
    is_proper_noun: bool

    @property
    def suspected_title_sense(self) -> bool:
        """Обычное слово внутри категории названий: `trouble` в BOARD GAMES."""
        return self.names_titles and not self.is_proper_noun

    @property
    def priority(self) -> str:
        """P0 — уже стоит в собранном уровне: база отдаёт игроку то, чего не знает."""
        if self.used_in_levels:
            return "P0"
        if self.used_in_quartets:
            return "P1"
        if self.suspected_title_sense or self.membership_count >= 4:
            return "P2"
        return "P3"

    @property
    def priority_score(self) -> int:
        return (
            1000 * self.used_in_levels
            + 100 * self.used_in_quartets
            + 20 * int(self.suspected_title_sense)
            + 5 * self.membership_count
            + int(self.is_proper_noun)
        )


def unresolved(conn: sqlite3.Connection) -> list[UnresolvedMembership]:
    """Связи, которым значение нужно, но его нет. Отсортированы по срочности.

    Игра слов сюда не попадает намеренно: правило `words_before_time` держит
    `life` за буквы, значение ему не нужно и никогда не понадобится.
    """
    rows = conn.execute(
        """
        SELECT m.id AS membership_id, w.text AS word, w.normalized AS normalized,
               w.is_proper_noun AS is_proper_noun,
               c.category_key AS category_key, c.names_titles AS names_titles,
               m.sense_id AS sense_id,
               COALESCE(s.accessibility_class, 'unresolved') AS accessibility_class,
               (SELECT COUNT(*) FROM memberships m2
                 WHERE m2.word_id = m.word_id AND m2.sense_mode <> 'surface_form')
                   AS membership_count,
               (SELECT COUNT(*) FROM level_tokens t
                  JOIN level_groups g ON g.id = t.group_id
                 WHERE t.word_id = m.word_id AND g.category_id = m.category_id)
                   AS used_in_levels,
               (SELECT COUNT(*) FROM quartet_words qw
                  JOIN quartets q ON q.id = qw.quartet_id
                 WHERE qw.word_id = m.word_id AND q.category_id = m.category_id
                   AND q.validation_state IN ('auto_validated', 'warning'))
                   AS used_in_quartets
          FROM memberships m
          JOIN words w      ON w.id = m.word_id
          JOIN categories c ON c.id = m.category_id
          LEFT JOIN word_senses s ON s.id = m.sense_id
         WHERE m.sense_mode <> 'surface_form'
           AND m.semantic_status <> 'incorrect'
           AND (m.sense_id IS NULL
                OR COALESCE(s.accessibility_class, 'unresolved') = 'unresolved')
        """
    )
    items = [
        UnresolvedMembership(
            membership_id=int(row["membership_id"]),
            word=row["word"],
            normalized=row["normalized"],
            category_key=row["category_key"],
            sense_id=row["sense_id"],
            accessibility_class=row["accessibility_class"],
            membership_count=int(row["membership_count"]),
            used_in_levels=int(row["used_in_levels"]),
            used_in_quartets=int(row["used_in_quartets"]),
            names_titles=bool(row["names_titles"]),
            is_proper_noun=bool(row["is_proper_noun"]),
        )
        for row in rows
    ]
    items.sort(key=lambda item: (-item.priority_score, item.normalized, item.category_key))
    return items


def unresolved_rows(items: list[UnresolvedMembership]) -> list[dict[str, object]]:
    """Машиночитаемая очередь: одна строка на связь."""
    return [
        {
            "priority": item.priority,
            "priority_score": item.priority_score,
            "word": item.word,
            "normalized": item.normalized,
            "category_key": item.category_key,
            "sense_id": item.sense_id if item.sense_id is not None else "",
            "accessibility_class": item.accessibility_class,
            "membership_count": item.membership_count,
            "used_in_levels": item.used_in_levels,
            "used_in_quartets": item.used_in_quartets,
            "suspected_title_sense": int(item.suspected_title_sense),
            "is_proper_noun": int(item.is_proper_noun),
        }
        for item in items
    ]


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
