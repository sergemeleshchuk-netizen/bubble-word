from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest

from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships

CATEGORIES = [
    {
        "category_key": "fruits",
        "label": "FRUITS",
        "rule": "Common edible fruits familiar to an average American adult",
        "relation_type": "is_a",
        "theme": "food",
        "base_difficulty": 0.1,
    },
    {
        "category_key": "pie_ingredients",
        "label": "PIE INGREDIENTS",
        "rule": "Ingredients commonly used in pie fillings or pie preparation",
        "relation_type": "used_in",
        "theme": "food",
        "base_difficulty": 0.25,
    },
    {
        "category_key": "tech_companies",
        "label": "TECH COMPANIES",
        "rule": "Well-known technology companies or consumer technology brands",
        "relation_type": "is_a",
        "theme": "business",
        "base_difficulty": 0.25,
    },
    {
        "category_key": "river_features",
        "label": "RIVER FEATURES",
        "rule": "Parts and features of a river described in everyday English",
        "relation_type": "part_of",
        "theme": "nature",
        "base_difficulty": 0.35,
    },
    {
        "category_key": "town_places",
        "label": "PLACES IN A TOWN",
        "rule": "Public buildings and places found in an ordinary American town",
        "relation_type": "found_in",
        "theme": "geography",
        "base_difficulty": 0.15,
    },
]

APPLE_FRUIT = {
    "sense_key": "apple_fruit",
    "sense_definition": "The round edible fruit of an apple tree",
}

MEMBERSHIPS = [
    {
        "word": "apple",
        "part_of_speech": "noun",
        **APPLE_FRUIT,
        "category_key": "fruits",
        "relation_type": "is_a",
        "reason": "An apple is a common edible fruit",
        "fit_score": 1.0,
        "obviousness_score": 1.0,
        "source": "seed_manual",
        "review_status": "approved",
    },
    {
        "word": "apple",
        "part_of_speech": "noun",
        **APPLE_FRUIT,
        "category_key": "pie_ingredients",
        "relation_type": "used_in",
        "reason": "Apples are commonly used as pie filling",
        "fit_score": 0.99,
        "obviousness_score": 0.95,
        "source": "seed_manual",
        "review_status": "approved",
    },
    {
        "word": "Apple",
        "part_of_speech": "proper_noun",
        "is_proper_noun": True,
        "sense_key": "apple_company",
        "sense_definition": "The American technology company Apple Inc.",
        "category_key": "tech_companies",
        "relation_type": "is_a",
        "reason": "Apple is a well-known technology company",
        "fit_score": 1.0,
        "obviousness_score": 0.99,
        "source": "seed_manual",
        "review_status": "candidate",
    },
    {
        "word": "bank",
        "sense_key": "bank_river",
        "sense_definition": "The sloping land along the side of a river",
        "category_key": "river_features",
        "relation_type": "part_of",
        "reason": "The bank is the land along the side of a river",
        "fit_score": 0.99,
        "obviousness_score": 0.7,
        "source": "seed_manual",
        "review_status": "approved",
    },
    {
        "word": "bank",
        "sense_key": "bank_finance",
        "sense_definition": "A business that keeps and lends money",
        "category_key": "town_places",
        "relation_type": "found_in",
        "reason": "A bank is a public place found in almost every town",
        "fit_score": 0.97,
        "obviousness_score": 0.9,
        "source": "seed_manual",
        "review_status": "candidate",
    },
]


def write_jsonl(path: Path, rows: list[dict]) -> Path:
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )
    return path


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    path = tmp_path / "test.sqlite"
    init_db(path)
    return path


@pytest.fixture
def conn(db_path: Path) -> sqlite3.Connection:
    connection = connect(db_path)
    yield connection
    connection.close()


@pytest.fixture
def categories_file(tmp_path: Path) -> Path:
    return write_jsonl(tmp_path / "categories.jsonl", CATEGORIES)


@pytest.fixture
def memberships_file(tmp_path: Path) -> Path:
    return write_jsonl(tmp_path / "memberships.jsonl", MEMBERSHIPS)


@pytest.fixture
def seeded(conn, categories_file: Path, memberships_file: Path):
    """База с категориями и связями из фикстур."""
    import_categories(conn, categories_file)
    import_memberships(conn, memberships_file)
    return conn
