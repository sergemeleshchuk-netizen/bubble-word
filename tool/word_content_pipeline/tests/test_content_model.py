"""Тесты слоя concept / variant / alias и структурных категорий."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from word_content import dedupe, structured
from word_content.db import connect, init_db, utc_now
from word_content.importers import import_categories, import_memberships
from word_content.sense_map import SenseMap

CATEGORIES = [
    ("birds_of_prey", "BIRDS OF PREY", "Birds that hunt other animals for food", "is_a", "nature"),
    ("raptors", "RAPTORS", "Birds that hunt other animals for food", "is_a", "nature"),
    ("birds", "BIRDS", "Birds of any kind known to an average adult", "is_a", "nature"),
    ("words_before_house", "___ HOUSE", "Words that form a compound before house",
     "phrase_before", "language"),
    ("house_words", "HOUSE WORDS", "Words that form a compound before house", "is_a", "language"),
    ("opposites", "OPPOSITES", "Pairs of words with opposite meanings", "has_property",
     "descriptive"),
]

POOLS = {
    "birds_of_prey": ["eagle", "hawk", "falcon", "owl"],
    "raptors": ["eagle", "hawk", "falcon", "kite"],
    "birds": ["eagle", "hawk", "falcon", "owl", "robin", "sparrow", "finch", "wren", "crow"],
    "words_before_house": ["boat", "green", "light", "farm"],
    "house_words": ["roof", "door", "window", "wall"],
    "opposites": ["hot", "cold", "up", "down", "fast", "slow"],
}


@pytest.fixture
def content_db(tmp_path: Path):
    path = tmp_path / "content.sqlite"
    init_db(path)
    conn = connect(path)
    (tmp_path / "categories.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "category_key": key,
                    "label": label,
                    "rule": rule,
                    "relation_type": relation,
                    "theme": theme,
                },
                ensure_ascii=False,
            )
            for key, label, rule, relation, theme in CATEGORIES
        )
        + "\n",
        encoding="utf-8",
    )
    (tmp_path / "memberships.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "word": word,
                    "category_key": category_key,
                    "relation_type": "phrase_before" if category_key.startswith("words_") else "is_a",
                    "reason": f"{word} в категории {category_key}",
                    "fit_score": 0.9,
                    "obviousness_score": 0.9,
                    "source": "test_fixture",
                    "review_status": "approved",
                },
                ensure_ascii=False,
            )
            for category_key, words in POOLS.items()
            for word in words
        )
        + "\n",
        encoding="utf-8",
    )
    import_categories(conn, tmp_path / "categories.jsonl")
    import_memberships(conn, tmp_path / "memberships.jsonl", sense_map=SenseMap())
    yield conn
    conn.close()


# ------------------------------------------------------------------ concept / variant


def test_every_variant_gets_a_concept(content_db):
    missing = content_db.execute(
        "SELECT COUNT(*) FROM categories WHERE concept_id IS NULL"
    ).fetchone()[0]
    assert missing == 0


def test_alias_detected_and_merged(content_db):
    """RAPTORS и BIRDS OF PREY — одно правило и общий пул: это алиас."""
    pairs = dedupe.find(content_db)
    alias = [p for p in pairs if {p.category_a, p.category_b} == {"birds_of_prey", "raptors"}]
    assert alias and alias[0].verdict == "alias"

    merged, _notes = dedupe.merge_into_concepts(content_db, pairs)
    content_db.commit()
    assert merged >= 1
    concepts = {
        row["category_key"]: row["concept_id"]
        for row in content_db.execute(
            "SELECT category_key, concept_id FROM categories "
            "WHERE category_key IN ('birds_of_prey', 'raptors')"
        )
    }
    assert concepts["birds_of_prey"] == concepts["raptors"]


def test_parent_child_is_never_merged(content_db):
    """BIRDS и BIRDS OF PREY — родитель и ребёнок: слить значит потерять слой сложности."""
    pairs = dedupe.find(content_db)
    parent = [p for p in pairs if {p.category_a, p.category_b} == {"birds", "birds_of_prey"}]
    assert parent and parent[0].verdict == "parent_child"
    assert not parent[0].mergeable

    dedupe.merge_into_concepts(content_db, pairs)
    content_db.commit()
    concepts = {
        row["category_key"]: row["concept_id"]
        for row in content_db.execute(
            "SELECT category_key, concept_id FROM categories "
            "WHERE category_key IN ('birds', 'birds_of_prey')"
        )
    }
    assert concepts["birds"] != concepts["birds_of_prey"]


def test_wordplay_is_not_an_alias_of_semantic_category(content_db):
    """У ___ HOUSE и HOUSE WORDS одинаковое правило, но принцип разный."""
    pairs = dedupe.find(content_db)
    pair = [p for p in pairs if {p.category_a, p.category_b} == {"words_before_house", "house_words"}]
    assert pair and pair[0].verdict == "legitimate_distinct"


def test_label_key_handles_plural_and_punctuation():
    assert dedupe.label_key("FAIRY TALES") == dedupe.label_key("Fairy-tale")
    assert dedupe.label_key("BIRDS OF PREY") == dedupe.label_key("prey birds")


# ------------------------------------------------------------------ структурные категории


def _add_pairs(conn, category_key: str, pairs: list[tuple[str, str]]) -> None:
    now = utc_now()
    category_id = conn.execute(
        "SELECT id FROM categories WHERE category_key = ?", (category_key,)
    ).fetchone()["id"]
    for index, (first, second) in enumerate(pairs, start=1):
        for slot, word in ((1, first), (2, second)):
            word_id = conn.execute(
                "SELECT id FROM words WHERE normalized = ?", (word,)
            ).fetchone()["id"]
            conn.execute(
                """
                INSERT INTO structured_relations
                    (category_id, structure, group_key, word_id, role, position, created_at)
                VALUES (?, 'pairs', ?, ?, ?, ?, ?)
                """,
                (category_id, f"{category_key}__pair{index}", word_id,
                 "a" if slot == 1 else "b", slot, now),
            )
    conn.commit()


def test_pairs_structure_requires_whole_pairs(content_db):
    """OPPOSITES собирается только как две полные пары."""
    _add_pairs(content_db, "opposites", [("hot", "cold"), ("up", "down"), ("fast", "slow")])
    index = structured.load(content_db)
    assert "opposites" in index.structured_keys

    ok, _ = index.allows("opposites", frozenset({"hot", "cold", "up", "down"}))
    assert ok
    bad, reason = index.allows("opposites", frozenset({"hot", "cold", "up", "fast"}))
    assert not bad and "пар" in reason


def test_free_category_allows_any_four(content_db):
    index = structured.load(content_db)
    ok, _ = index.allows("birds", frozenset({"robin", "sparrow", "finch", "wren"}))
    assert ok


def test_sequence_structure_requires_consecutive_words(content_db):
    now = utc_now()
    category_id = content_db.execute(
        "SELECT id FROM categories WHERE category_key = 'birds'"
    ).fetchone()["id"]
    order = ["robin", "sparrow", "finch", "wren", "crow"]
    for position, word in enumerate(order, start=1):
        word_id = content_db.execute(
            "SELECT id FROM words WHERE normalized = ?", (word,)
        ).fetchone()["id"]
        content_db.execute(
            """
            INSERT INTO structured_relations
                (category_id, structure, group_key, word_id, role, position, created_at)
            VALUES (?, 'sequence', 'birds__seq', ?, ?, ?, ?)
            """,
            (category_id, word_id, f"pos{position}", position, now),
        )
    content_db.commit()

    index = structured.load(content_db)
    ok, _ = index.allows("birds", frozenset({"robin", "sparrow", "finch", "wren"}))
    assert ok
    bad, reason = index.allows("birds", frozenset({"robin", "sparrow", "finch", "crow"}))
    assert not bad and "подряд" in reason
