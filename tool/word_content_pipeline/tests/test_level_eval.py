"""Оценка уровня по D и F: то, чем меряется «наш пакет лучше записи».

Проверяется не «числа не изменились», а свойства модели: что она видит
психологическую ловушку и не считает ею объявленную мета-связь, что натужная
надпись и нечитаемый пузырь роняют фан, и что округление идёт по EVAL.md.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from word_content import level_eval, level_generator, quartet_builder
from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships
from word_content.models import QuartetInput
from word_content.readiness import derive
from word_content.repositories import upsert_quartet
from word_content.sense_map import SenseMap

POOLS = {
    "fruits": ["apple", "pear", "plum", "peach", "cherry", "melon"],
    "colors": ["red", "green", "blue", "yellow", "purple", "brown"],
    "tools": ["hammer", "wrench", "pliers", "chisel", "mallet", "clamp"],
    "birds": ["robin", "sparrow", "finch", "wren", "magpie", "heron"],
    "trees": ["oak", "maple", "birch", "pine", "cedar", "willow"],
}
LABELS = {
    "fruits": ("FRUITS", "food"),
    "colors": ("COLORS", "abstract"),
    "tools": ("HAND TOOLS", "work"),
    "birds": ("BIRDS", "nature"),
    "trees": ("TREES", "nature"),
}


@pytest.fixture
def eval_db(tmp_path: Path):
    path = tmp_path / "eval.sqlite"
    init_db(path)
    conn = connect(path)
    (tmp_path / "categories.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "category_key": key,
                    "label": LABELS[key][0],
                    "rule": f"Words that belong to {key}",
                    "relation_type": "is_a",
                    "theme": LABELS[key][1],
                    "base_difficulty": 0.2,
                },
                ensure_ascii=False,
            )
            for key in POOLS
        )
        + "\n",
        encoding="utf-8",
    )
    (tmp_path / "memberships.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "word": word,
                    "category_key": key,
                    "relation_type": "is_a",
                    "reason": f"{word} в {key}",
                    "fit_score": 0.95,
                    "obviousness_score": 0.9,
                    "source": "test_fixture",
                    "review_status": "approved",
                },
                ensure_ascii=False,
            )
            for key, words in POOLS.items()
            for word in words
        )
        + "\n",
        encoding="utf-8",
    )
    import_categories(conn, tmp_path / "categories.jsonl")
    import_memberships(conn, tmp_path / "memberships.jsonl", sense_map=SenseMap())
    derive(conn, {})
    conn.commit()
    built, _stats = quartet_builder.build(conn, max_per_category=2)
    for row in quartet_builder.to_rows(built):
        upsert_quartet(conn, QuartetInput.model_validate(row))
    conn.commit()
    yield conn
    conn.close()


def _no_swow(tmp_path: Path) -> Path:
    """Путь, которого нет: модуль обязан честно перейти на пулы базы."""
    return tmp_path / "нет-такого-файла.pkl"


# ------------------------------------------------------------------- надписи


@pytest.mark.parametrize(
    "label, vague",
    [
        ("FRUITS", False),
        ("FARM ANIMALS", False),
        ("ROOMS IN A HOUSE", False),
        ("DAYS OF THE WEEK", False),
        ("STRETCHY THINGS", True),
        ("THINKING ACTIONS", True),
        ("PLUMBING WORDS", True),
        ("OFFICE SKILLS", True),
        ("KINDS OF PLANTS", True),
        ("SAILING TERMS", True),
    ],
)
def test_vague_label_is_recognised(label: str, vague: bool):
    """Надпись, которая называет признак вместо темы, помечается натужной.

    Игрок не угадывает STRETCHY THINGS по четырём словам — он добирает эту
    группу последней по остатку. По шкале фана это минус балл.
    """
    group = level_eval.Group(
        group_id=1, position=1, category_id=1, category_key="x", concept_id=None,
        theme=None, label=label, words=(), displays=(), senses=(),
    )
    assert group.vague_label is vague


# ------------------------------------------------------------------ округление


@pytest.mark.parametrize(
    "value, expected",
    [(1.0, 1.0), (5.2, 5.0), (5.25, 5.5), (5.24, 5.0), (5.74, 5.5), (5.75, 6.0)],
)
def test_rounding_matches_eval_md(value: float, expected: float):
    """Округление до 0.5, ровно .25 вверх — как записано в EVAL.md."""
    assert level_eval._round_half(value) == expected


# ------------------------------------------------------------------ притяжение


def test_meta_pair_is_not_a_trap(eval_db, tmp_path: Path):
    """Мета-связь — объявленная механика, а не ловушка.

    Собранная группа COFFEE оставляет пузырь «coffee» для BEVERAGES. Слово
    неизбежно тянет к своей группе-источнику; если считать это ловушкой,
    любой мета-уровень получит фан за то, что просто работает.
    """
    associations = level_eval.Associations(eval_db, swow=_no_swow(tmp_path))
    groups = [
        level_eval.Group(
            group_id=1, position=1, category_id=1, category_key="fruits",
            concept_id=None, theme="food", label="FRUITS",
            words=("apple", "pear", "plum", "peach"),
            displays=("apple", "pear", "plum", "peach"), senses=(None,) * 4,
        ),
        level_eval.Group(
            group_id=2, position=2, category_id=2, category_key="colors",
            concept_id=None, theme="abstract", label="COLORS",
            words=("red", "green", "blue", "cherry"),
            displays=("red", "green", "blue", "cherry"), senses=(None,) * 4,
        ),
    ]
    without_meta = level_eval.temptations(groups, associations, meta=set())
    with_meta = level_eval.temptations(groups, associations, meta={frozenset({1, 2})})
    assert without_meta, "фикстура не даёт ни одного притяжения — тест бесполезен"
    assert with_meta == []


def test_associations_fall_back_to_pools_without_swow(eval_db, tmp_path: Path):
    """Без локального SWOW модуль считает по пулам и говорит об этом."""
    associations = level_eval.Associations(eval_db, swow=_no_swow(tmp_path))
    assert associations.source == "pools"
    assert associations.sym("apple", "pear") > 0
    assert associations.sym("apple", "hammer") == 0


# ------------------------------------------------------------------ оценка целиком


def test_evaluation_has_both_scales_and_all_factors(eval_db, tmp_path: Path):
    levels, _stats = level_generator.generate(
        eval_db, count=1, category_count=4, seed=5, use_meta=False, key_prefix="T"
    )
    assert levels, "генератор не собрал уровень для оценки"
    with eval_db:
        level_generator.save(eval_db, levels)

    results = level_eval.evaluate_pack(eval_db, "T", swow=_no_swow(tmp_path))
    assert len(results) == 1
    item = results[0]
    assert 1.0 <= item.difficulty <= 10.0
    assert 1.0 <= item.fun <= 10.0
    assert set(item.d_factors) == {
        "F1 масштаб", "F2 ловушки", "F3 близость", "F4 редкость",
        "F5 лимит", "F6 память", "F7 спорность",
    }
    assert len(item.f_factors) == 9
    assert item.facts["источник ассоциаций"] == "pools"
    assert item.facts["категорий"] == 4


def test_summary_counts_whole_pack(eval_db, tmp_path: Path):
    levels, _stats = level_generator.generate(
        eval_db, count=2, category_count=3, seed=9, use_meta=False, key_prefix="T"
    )
    with eval_db:
        level_generator.save(eval_db, levels)
    results = level_eval.evaluate_pack(eval_db, "T", swow=_no_swow(tmp_path))
    summary = level_eval.summarise(results)
    assert summary["уровней"] == len(results)
    assert summary["D среднее"] >= 1.0
    assert summary["F среднее"] >= 1.0
