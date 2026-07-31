"""Поиск дублей среди категорий.

Зачем. Категория в базе — это игровая формулировка (variant). Один и тот же
семантический принцип легко разъезжается на несколько формулировок:
`BIRDS OF PREY`, `RAPTORS`, `PREDATORY BIRDS`. Пока они считаются разными
категориями, генератор имеет полное право поставить две из них в один уровень —
и получить уровень с двумя одинаковыми ответами.

Модуль ничего не сливает молча. Он классифицирует пары и объясняет решение,
а слияние применяется отдельной командой и только для безопасных классов.
`parent_child` не сливается никогда: `BIRDS` и `BIRDS OF PREY` — разные
категории, и потерять родителя означает потерять целый слой сложности.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass

# Классы, которые можно сливать автоматически: формулировка разная, принцип один.
MERGEABLE = ("exact_duplicate", "alias")
# Классы, требующие человека либо не требующие ничего.
CLASSES = (
    "exact_duplicate",
    "alias",
    "near_duplicate",
    "parent_child",
    "legitimate_distinct",
    "warning",
)

_PUNCT_RE = re.compile(r"[^a-z0-9 ]+")
_SPACE_RE = re.compile(r"\s+")

# Слова-связки, которые не несут смысла при сравнении формулировок.
STOPWORDS = frozenset({"the", "a", "an", "of", "and", "or", "in", "on", "at", "for", "with"})


def normalize_label(label: str) -> str:
    """Формулировка без пунктуации, регистра и служебных слов."""
    text = _PUNCT_RE.sub(" ", label.lower())
    words = [word for word in _SPACE_RE.split(text) if word and word not in STOPWORDS]
    return " ".join(words)


def singularize(word: str) -> str:
    """Грубая нормализация числа. Задача — сравнить формулировки, не построить лемматизатор."""
    for suffix, replacement in (("ies", "y"), ("ches", "ch"), ("shes", "sh"), ("ses", "s")):
        if word.endswith(suffix) and len(word) > len(suffix) + 1:
            return word[: -len(suffix)] + replacement
    if word.endswith("s") and not word.endswith("ss") and len(word) > 3:
        return word[:-1]
    return word


def label_key(label: str) -> str:
    """Ключ сравнения: формулировка без пунктуации, служебных слов и множественного числа."""
    return " ".join(sorted(singularize(word) for word in normalize_label(label).split()))


@dataclass(frozen=True)
class DuplicatePair:
    category_a: str
    category_b: str
    label_a: str
    label_b: str
    verdict: str
    reason: str
    shared_words: int
    pool_a: int
    pool_b: int

    @property
    def mergeable(self) -> bool:
        return self.verdict in MERGEABLE


# Категории игры слов работают с написанием слова. Семантическим принципом
# они не являются и алиасом семантической категории быть не могут.
WORDPLAY_RELATIONS = ("phrase_before", "phrase_after", "wordplay")


def _is_wordplay(row: sqlite3.Row) -> bool:
    return row["relation_type"] in WORDPLAY_RELATIONS


def _pools(conn: sqlite3.Connection) -> dict[str, set[str]]:
    pools: dict[str, set[str]] = {}
    for row in conn.execute(
        """
        SELECT c.category_key AS category_key, w.normalized AS word
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
          JOIN words w      ON w.id = m.word_id
         WHERE m.review_status IN ('approved', 'alternative', 'hard_only')
        """
    ):
        pools.setdefault(row["category_key"], set()).add(row["word"])
    return pools


def _quartet_sets(conn: sqlite3.Connection) -> dict[str, set[frozenset[str]]]:
    """Составы четвёрок по категориям: одинаковые четвёрки под разными вывесками."""
    by_quartet: dict[int, tuple[str, set[str]]] = {}
    for row in conn.execute(
        """
        SELECT q.id AS quartet_id, c.category_key AS category_key, w.normalized AS word
          FROM quartets q
          JOIN categories c    ON c.id = q.category_id
          JOIN quartet_words qw ON qw.quartet_id = q.id
          JOIN words w         ON w.id = qw.word_id
        """
    ):
        key, words = by_quartet.setdefault(int(row["quartet_id"]), (row["category_key"], set()))
        words.add(row["word"])
    result: dict[str, set[frozenset[str]]] = {}
    for category_key, words in by_quartet.values():
        result.setdefault(category_key, set()).add(frozenset(words))
    return result


def find(conn: sqlite3.Connection, *, min_overlap: float = 0.7) -> list[DuplicatePair]:
    """Ищет пары категорий, которые могут быть одним и тем же принципом."""
    rows = list(
        conn.execute(
            "SELECT category_key, label, rule, theme, relation_type FROM categories "
            "ORDER BY category_key"
        )
    )
    pools = _pools(conn)
    quartets = _quartet_sets(conn)

    by_label_key: dict[str, list[sqlite3.Row]] = {}
    for row in rows:
        by_label_key.setdefault(label_key(row["label"]), []).append(row)

    pairs: list[DuplicatePair] = []
    seen: set[tuple[str, str]] = set()

    def add(a: sqlite3.Row, b: sqlite3.Row, verdict: str, reason: str) -> None:
        key = tuple(sorted((a["category_key"], b["category_key"])))
        if key in seen:
            return
        seen.add(key)
        pool_a = pools.get(a["category_key"], set())
        pool_b = pools.get(b["category_key"], set())
        pairs.append(
            DuplicatePair(
                category_a=key[0],
                category_b=key[1],
                label_a=a["label"] if a["category_key"] == key[0] else b["label"],
                label_b=b["label"] if b["category_key"] == key[1] else a["label"],
                verdict=verdict,
                reason=reason,
                shared_words=len(pool_a & pool_b),
                pool_a=len(pool_a),
                pool_b=len(pool_b),
            )
        )

    def label_verdict(first: sqlite3.Row, second: sqlite3.Row) -> tuple[str, str]:
        """Похожая формулировка ещё не значит один принцип.

        Два ложных срабатывания, которые ловятся здесь. `BERRIES` и `___ BERRY`
        нормализуются в одно и то же, но вторая категория — игра слов: там
        участвует написание, а не смысл. `SALADS` и `IN A SALAD` тоже похожи,
        но их пулы не пересекаются ни одним словом — значит это разные наборы,
        как бы ни выглядели вывески.
        """
        if _is_wordplay(first) != _is_wordplay(second):
            return "legitimate_distinct", "одна из категорий — игра слов, принцип другой"
        shared = pools.get(first["category_key"], set()) & pools.get(second["category_key"], set())
        if not shared:
            return "legitimate_distinct", "формулировки похожи, но пулы не пересекаются"
        if first["label"].strip().lower() == second["label"].strip().lower():
            return "exact_duplicate", "формулировки совпадают дословно"
        return "alias", "формулировки совпадают после нормализации"

    # 1. Одинаковые формулировки с точностью до пунктуации и числа.
    for group in by_label_key.values():
        for i, first in enumerate(group):
            for second in group[i + 1:]:
                verdict, reason = label_verdict(first, second)
                add(first, second, verdict, reason)

    # 2. Одинаковые правила.
    by_rule: dict[str, list[sqlite3.Row]] = {}
    for row in rows:
        by_rule.setdefault(normalize_label(row["rule"]), []).append(row)
    for group in by_rule.values():
        for i, first in enumerate(group):
            for second in group[i + 1:]:
                verdict, reason = label_verdict(first, second)
                if verdict == "legitimate_distinct":
                    add(first, second, verdict, reason)
                else:
                    add(first, second, "alias", "правила категорий совпадают дословно")

    # 3. Одинаковый состав четвёрок под разными вывесками.
    quartet_owner: dict[frozenset[str], str] = {}
    by_key = {row["category_key"]: row for row in rows}
    for category_key, sets in sorted(quartets.items()):
        for words in sets:
            other = quartet_owner.get(words)
            if other is None:
                quartet_owner[words] = category_key
            elif other != category_key:
                add(
                    by_key[other],
                    by_key[category_key],
                    "near_duplicate",
                    "одна и та же четвёрка собрана под двумя вывесками: "
                    + ", ".join(sorted(words)),
                )

    # 4. Сильно перекрывающиеся пулы: либо родитель-ребёнок, либо почти дубль.
    keys = sorted(pools)
    for i, first_key in enumerate(keys):
        pool_a = pools[first_key]
        if len(pool_a) < 4:
            continue
        for second_key in keys[i + 1:]:
            pool_b = pools[second_key]
            if len(pool_b) < 4:
                continue
            shared = pool_a & pool_b
            if not shared:
                continue
            share_a = len(shared) / len(pool_a)
            share_b = len(shared) / len(pool_b)
            if max(share_a, share_b) < min_overlap:
                continue
            first, second = by_key[first_key], by_key[second_key]
            if share_a >= 0.95 and share_b >= 0.95:
                verdict, reason = "near_duplicate", "пулы совпадают почти полностью"
            elif abs(len(pool_a) - len(pool_b)) >= 4:
                verdict = "parent_child"
                reason = (
                    "пул одной категории вложен в другую: похоже на родителя и ребёнка, "
                    "сливать нельзя"
                )
            else:
                verdict, reason = "warning", "пулы пересекаются сильнее порога"
            add(first, second, verdict, f"{reason} ({len(shared)} общих слов)")

    return sorted(pairs, key=lambda p: (CLASSES.index(p.verdict), p.category_a, p.category_b))


def to_rows(pairs: list[DuplicatePair]) -> list[dict[str, object]]:
    return [
        {
            "category_a": pair.category_a,
            "category_b": pair.category_b,
            "label_a": pair.label_a,
            "label_b": pair.label_b,
            "verdict": pair.verdict,
            "shared_words": pair.shared_words,
            "pool_a": pair.pool_a,
            "pool_b": pair.pool_b,
            "reason": pair.reason,
        }
        for pair in pairs
    ]


def merge_into_concepts(
    conn: sqlite3.Connection, pairs: list[DuplicatePair]
) -> tuple[int, list[str]]:
    """Сводит сливаемые пары к одному concept, оставляя обе игровые формулировки.

    Категории не удаляются: формулировка `RAPTORS` может быть нужна как вариант.
    Меняется только принцип, на который они ссылаются, — и после этого генератор
    не поставит два варианта одного принципа в один уровень.
    """
    from .db import utc_now

    merged = 0
    notes: list[str] = []
    now = utc_now()
    for pair in pairs:
        if not pair.mergeable:
            continue
        rows = list(
            conn.execute(
                "SELECT id, category_key, label, concept_id FROM categories "
                "WHERE category_key IN (?, ?) ORDER BY category_key",
                (pair.category_a, pair.category_b),
            )
        )
        if len(rows) != 2:
            continue
        keep, drop = rows[0], rows[1]
        if keep["concept_id"] == drop["concept_id"]:
            continue
        conn.execute(
            "UPDATE categories SET concept_id = ?, updated_at = ? WHERE id = ?",
            (keep["concept_id"], now, drop["id"]),
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO category_aliases (concept_id, alias, kind, note, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (keep["concept_id"], drop["label"], pair.verdict, pair.reason, now),
        )
        merged += 1
        notes.append(f"{drop['category_key']} -> принцип категории {keep['category_key']}")
    return merged, notes
