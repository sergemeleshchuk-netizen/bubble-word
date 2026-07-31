"""Regression-набор solver'а полного уровня.

Каждый тест — это уровень, который либо обязан пройти, либо обязан быть
отклонён. Кейсы взяты из требований задания (раздел 5.2) и из реальных
ошибок: локально корректные четвёрки, дающие вместе два ответа.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships
from word_content.level_solver import (
    Token,
    load_memberships,
    parse_tokens,
    solve_level,
)
from word_content.sense_map import SenseMap
from word_content.structured import StructureIndex

# --------------------------------------------------------------------------- фикстура

CATEGORIES = [
    ("flowers", "FLOWERS", "Common garden and wild flowers known to any adult", "is_a", "nature"),
    ("colours", "COLOURS", "Basic colour names used in everyday English", "is_a", "descriptive"),
    ("fruits", "FRUITS", "Common edible fruits familiar to an average adult", "is_a", "food"),
    ("trees", "TREES", "Common trees of temperate forests and city streets", "is_a", "nature"),
    ("birds", "BIRDS", "Small birds seen in gardens and parks of Europe", "is_a", "nature"),
    ("river_parts", "RIVER PARTS", "Parts and features of a river in plain English",
     "part_of", "nature"),
    ("town_places", "PLACES IN A TOWN", "Public places found in an ordinary town",
     "found_in", "geography"),
]

# Слово -> категория. Набор подобран так, чтобы пересечения были настоящими:
# rose и violet — и цветы, и цвета; cherry, plum, orange, lemon — и фрукты, и цвета.
POOLS: dict[str, list[str]] = {
    "flowers": ["rose", "tulip", "lily", "daisy", "violet", "iris"],
    "colours": ["red", "blue", "green", "rose", "violet", "cherry", "plum", "orange", "lemon"],
    "fruits": ["apple", "pear", "cherry", "plum", "orange", "lemon"],
    "trees": ["oak", "maple", "birch", "pine"],
    "birds": ["robin", "sparrow", "finch", "wren"],
    "river_parts": ["mouth", "delta", "source", "bed"],
    "town_places": ["school", "library", "market", "station"],
}

# Многозначные слова: у токена уровня обязано быть указано значение.
SENSES = {
    "bank": [
        ("bank_river", "The sloping land along the side of a river", "river_parts"),
        ("bank_finance", "A business that keeps and lends money", "town_places"),
    ],
}


def _membership(word: str, category_key: str, **extra) -> dict:
    row = {
        "word": word,
        "category_key": category_key,
        "relation_type": "is_a",
        "reason": f"{word} принадлежит категории {category_key}",
        "fit_score": 0.95,
        "obviousness_score": 0.9,
        "source": "test_fixture",
        "review_status": "approved",
    }
    row.update(extra)
    return row


@pytest.fixture
def level_db(tmp_path: Path):
    """База с пересекающимися пулами: на ней ловятся реальные неоднозначности."""
    path = tmp_path / "levels.sqlite"
    init_db(path)
    conn = connect(path)

    categories = [
        {
            "category_key": key,
            "label": label,
            "rule": rule,
            "relation_type": relation,
            "theme": theme,
            "base_difficulty": 0.2,
        }
        for key, label, rule, relation, theme in CATEGORIES
    ]
    memberships = [
        _membership(word, category_key)
        for category_key, words in POOLS.items()
        for word in words
    ]
    for word, senses in SENSES.items():
        for sense_key, definition, category_key in senses:
            memberships.append(
                _membership(
                    word,
                    category_key,
                    sense_key=sense_key,
                    sense_definition=definition,
                    relation_type="part_of" if category_key == "river_parts" else "found_in",
                )
            )

    (tmp_path / "categories.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in categories) + "\n",
        encoding="utf-8",
    )
    (tmp_path / "memberships.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in memberships) + "\n",
        encoding="utf-8",
    )
    import_categories(conn, tmp_path / "categories.jsonl")
    # Пустая карта значений: фикстура объявляет значения сама. Иначе проектная
    # карта из data/seed/ подмешивала бы сюда настоящие значения rose и iris,
    # и тест проверял бы содержимое базы, а не логику solver'а.
    import_memberships(conn, tmp_path / "memberships.jsonl", sense_map=SenseMap())
    yield conn
    conn.close()


def _solve(conn, words: str, **kwargs):
    return solve_level(parse_tokens(words), load_memberships(conn), StructureIndex(), **kwargs)


# --------------------------------------------------------------------------- кейсы


def test_unique_level_passes(level_db):
    """Непересекающиеся категории: разбиение единственное."""
    result = _solve(level_db, "oak, maple, birch, pine, robin, sparrow, finch, wren")
    assert result.outcome == "unique"
    assert result.solution_count == 1
    assert result.unique
    assert result.input_hash and result.solver_version


def test_two_fully_alternative_groups_rejected(level_db):
    """Восемь слов делятся на четвёрки двумя разными способами целиком."""
    result = _solve(
        level_db, "apple, pear, cherry, plum, orange, lemon, red, blue"
    )
    assert result.outcome == "ambiguous"
    assert result.solution_count >= 2
    assert not result.unique
    assert result.alternative_partition is not None


def test_one_word_swap_ambiguity_rejected(level_db):
    """Классика: rose и violet — и цветок, и цвет. Уровень собирается двумя способами.

    FLOWERS: rose, tulip, lily, daisy + COLOURS: red, blue, green, violet
    FLOWERS: violet, tulip, lily, daisy + COLOURS: red, blue, green, rose
    """
    result = _solve(level_db, "rose, tulip, lily, daisy, red, blue, green, violet")
    assert result.outcome == "ambiguous"
    assert result.solution_count == 2
    partitions = {
        tuple(sorted((key, words) for key, words in solution)) for solution in result.solutions
    }
    assert len(partitions) == 2


def test_multi_word_swap_ambiguity_rejected(level_db):
    """Меняются местами сразу две пары слов — одиночная проверка четвёрки это пропускает."""
    result = _solve(level_db, "apple, pear, cherry, plum, red, blue, green, lemon")
    assert result.outcome == "ambiguous"
    assert not result.unique


def test_duplicate_token_is_invalid_input(level_db):
    result = _solve(level_db, "oak, maple, birch, pine, robin, sparrow, finch, oak")
    assert result.outcome == "invalid_input"
    assert "одинаковые пузыри" in result.reason
    assert not result.unique


def test_unresolved_sense_is_invalid_input(level_db):
    """Пустое значение у многозначного слова не должно проходить как «значение не нужно»."""
    result = _solve(level_db, "bank, mouth, delta, source, school, library, market, station")
    assert result.outcome == "invalid_input"
    assert "не указано значение" in result.reason


def test_resolved_sense_passes(level_db):
    """То же слово с явным значением решается однозначно."""
    result = _solve(
        level_db,
        "bank#bank_river, mouth, delta, source, school, library, market, station",
    )
    assert result.outcome == "unique"
    assert result.unique


def test_token_count_not_multiple_of_four(level_db):
    result = _solve(level_db, "oak, maple, birch, pine, robin")
    assert result.outcome == "invalid_input"
    assert not result.unique


def test_timeout_is_not_unique(level_db):
    """Таймаут — это «не знаю», а не «уникально». Уровень с таким исходом не принимается."""
    result = _solve(
        level_db, "oak, maple, birch, pine, robin, sparrow, finch, wren", timeout_ms=0
    )
    assert result.outcome == "timeout"
    assert not result.unique
    assert "не уложился" in result.reason


def test_blocked_membership_does_not_create_ambiguity(level_db):
    """Отклонённая связь не участвует в разборе уровня.

    Добавляем rose в TREES как rejected: если бы solver её учитывал,
    у уровня появился бы второй ответ.
    """
    level_db.execute(
        """
        INSERT INTO memberships
            (word_id, category_id, relation_type, reason, fit_score, obviousness_score,
             source, review_status, semantic_status, created_at, updated_at)
        SELECT w.id, c.id, 'is_a', 'заведомо мусорная связь для теста', 0.5, 0.5,
               'test_fixture', 'rejected', 'incorrect', '2026-01-01T00:00:00+00:00',
               '2026-01-01T00:00:00+00:00'
          FROM words w, categories c
         WHERE w.normalized = 'oak' AND c.category_key = 'colours'
        """
    )
    level_db.commit()
    result = _solve(level_db, "oak, maple, birch, pine, robin, sparrow, finch, wren")
    assert result.outcome == "unique"


def _set_status(conn, word: str, category_key: str, status: str) -> None:
    conn.execute(
        """
        UPDATE memberships SET review_status = ?
         WHERE word_id = (SELECT id FROM words WHERE normalized = ?)
           AND category_id = (SELECT id FROM categories WHERE category_key = ?)
        """,
        (status, word, category_key),
    )
    conn.commit()


def test_hard_only_membership_still_creates_ambiguity(level_db):
    """hard_only игрок тоже может увидеть: такая связь обязана ломать единственность.

    Статусы — наша внутренняя лестница, игрок о ней не знает. Если он способен
    собрать альтернативный ответ, уровень неоднозначен независимо от того,
    каким статусом мы пометили связь у себя.
    """
    level = "rose, tulip, lily, daisy, red, blue, green, violet"
    _set_status(level_db, "violet", "flowers", "hard_only")
    assert _solve(level_db, level).outcome == "ambiguous"


def test_rejected_membership_removes_ambiguity(level_db):
    """Та же пара слов, но связь отклонена: альтернативного ответа больше нет."""
    level = "rose, tulip, lily, daisy, red, blue, green, violet"
    _set_status(level_db, "violet", "flowers", "rejected")
    result = _solve(level_db, level)
    assert result.outcome == "unique"
    assert result.unique


def test_intended_groups_cover_full_token_set(level_db):
    """Найденное разбиение обязано покрывать ровно все слова уровня, без остатка."""
    words = "oak, maple, birch, pine, robin, sparrow, finch, wren"
    result = _solve(level_db, words)
    covered = [word for _key, group in result.solutions[0] for word in group]
    assert sorted(covered) == sorted(w.strip() for w in words.split(","))
    assert len(covered) == len(set(covered))


def test_unsolvable_level(level_db):
    """Слова, не собирающиеся ни в одну категорию, — это не «уникально»."""
    result = _solve(level_db, "oak, maple, robin, sparrow, red, blue, school, library")
    assert result.outcome in ("unsolvable", "ambiguous")
    assert not result.unique


def test_input_hash_is_stable_and_sensitive(level_db):
    index = load_memberships(level_db)
    a = solve_level(parse_tokens("oak, maple, birch, pine"), index)
    b = solve_level(parse_tokens("pine, birch, maple, oak"), index)
    c = solve_level(parse_tokens("oak, maple, birch, robin"), index)
    assert a.input_hash == b.input_hash  # порядок слов не меняет уровень
    assert a.input_hash != c.input_hash


def test_sense_aware_matching(level_db):
    """Токен с одним значением не подходит категории, которая ждёт другое значение."""
    index = load_memberships(level_db)
    assert index.matches("river_parts", Token(word="bank", sense_key="bank_river"))
    assert not index.matches("river_parts", Token(word="bank", sense_key="bank_finance"))
    assert index.matches("town_places", Token(word="bank", sense_key="bank_finance"))
