"""Ловушки: генератор ставит их нарочно, а валидатор отличает замысел от брака.

До этого слоя генератор пересечения только избегал: любое слово, подходящее
двум правилам уровня, отсеивалось. Замер двадцатки показал цену — 4 ловушки
против 25 в записи и ноль ага-моментов против двадцати.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from word_content import decoy_pairs, level_generator, level_solver, quartet_builder
from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships
from word_content.models import QuartetInput
from word_content.readiness import derive
from word_content.repositories import upsert_quartet
from word_content.sense_map import SenseMap

# `gold` живёт и в цветах, и в металлах: в цветах увереннее — значит из цветов
# в металлы получается ловушка, а не брак. `robin` в птицах и в именах — так же.
POOLS: dict[str, list[tuple[str, float, float]]] = {
    "colors": [
        ("red", 0.95, 0.95), ("green", 0.95, 0.95), ("blue", 0.95, 0.95),
        ("gold", 0.95, 0.95), ("silver", 0.95, 0.95), ("brown", 0.95, 0.95),
        ("purple", 0.95, 0.95), ("orange", 0.95, 0.95), ("yellow", 0.95, 0.95),
    ],
    "metals": [
        ("iron", 0.95, 0.95), ("copper", 0.95, 0.95), ("zinc", 0.95, 0.95),
        ("nickel", 0.95, 0.95), ("gold", 0.80, 0.75), ("tin", 0.95, 0.95),
        ("lead", 0.95, 0.95), ("steel", 0.95, 0.95), ("brass", 0.95, 0.95),
    ],
    "birds": [
        ("robin", 0.95, 0.95), ("sparrow", 0.95, 0.95), ("finch", 0.95, 0.95),
        ("wren", 0.95, 0.95), ("magpie", 0.95, 0.95), ("heron", 0.95, 0.95),
        ("crow", 0.95, 0.95), ("swallow", 0.95, 0.95), ("thrush", 0.95, 0.95),
    ],
    "names": [
        ("peter", 0.95, 0.95), ("mary", 0.95, 0.95), ("john", 0.95, 0.95),
        ("susan", 0.95, 0.95), ("robin", 0.80, 0.75), ("alice", 0.95, 0.95),
        ("david", 0.95, 0.95), ("laura", 0.95, 0.95), ("simon", 0.95, 0.95),
    ],
    "tools": [
        ("hammer", 0.95, 0.95), ("wrench", 0.95, 0.95), ("pliers", 0.95, 0.95),
        ("chisel", 0.95, 0.95), ("mallet", 0.95, 0.95), ("clamp", 0.95, 0.95),
        ("rasp", 0.95, 0.95), ("awl", 0.95, 0.95), ("file", 0.95, 0.95),
    ],
    "trees": [
        ("oak", 0.95, 0.95), ("maple", 0.95, 0.95), ("birch", 0.95, 0.95),
        ("pine", 0.95, 0.95), ("cedar", 0.95, 0.95), ("willow", 0.95, 0.95),
        ("aspen", 0.95, 0.95), ("elm", 0.95, 0.95), ("beech", 0.95, 0.95),
    ],
}
LABELS = {
    "colors": "COLORS", "metals": "METALS", "birds": "BIRDS",
    "names": "FIRST NAMES", "tools": "HAND TOOLS", "trees": "TREES",
}


@pytest.fixture
def decoy_db(tmp_path: Path):
    path = tmp_path / "decoys.sqlite"
    init_db(path)
    conn = connect(path)
    (tmp_path / "categories.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "category_key": key,
                    "label": LABELS[key],
                    "rule": f"Words that belong to {key}",
                    "relation_type": "is_a",
                    "theme": key,
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
                    "fit_score": fit,
                    "obviousness_score": obvious,
                    "source": "test_fixture",
                    "review_status": "approved",
                },
                ensure_ascii=False,
            )
            for key, words in POOLS.items()
            for word, fit, obvious in words
        )
        + "\n",
        encoding="utf-8",
    )
    import_categories(conn, tmp_path / "categories.jsonl")
    import_memberships(conn, tmp_path / "memberships.jsonl", sense_map=SenseMap())
    derive(conn, {})
    conn.commit()
    built, _stats = quartet_builder.build(conn, max_per_category=8)
    for row in quartet_builder.to_rows(built):
        upsert_quartet(conn, QuartetInput.model_validate(row))
    conn.commit()
    yield conn
    conn.close()


def _pool(conn):
    by_category, _stats = level_generator._usable_quartets(conn, "normal")
    return by_category


# ------------------------------------------------------------------------ индекс


def test_index_finds_a_pair_where_home_is_stronger(decoy_db):
    by_category = _pool(decoy_db)
    index = level_solver.load_memberships(decoy_db)
    found = decoy_pairs.build(
        (entry for entries in by_category.values() for entry in entries),
        index,
        available=set(by_category),
    )
    pairs = {(pair.token_norm, pair.home_key, pair.rival_key) for pair in found.pairs}
    assert ("gold", "colors", "metals") in pairs
    assert ("robin", "birds", "names") in pairs


def test_index_refuses_a_pair_where_rival_is_stronger(decoy_db):
    """Соперник сильнее дома — это не ловушка, а сломанное разбиение.

    Такой уровень отклонит `assess_partition`, и правильно сделает: игрок не
    ошибётся, он окажется прав, а засчитают ему поражение.
    """
    by_category = _pool(decoy_db)
    index = level_solver.load_memberships(decoy_db)
    found = decoy_pairs.build(
        (entry for entries in by_category.values() for entry in entries),
        index,
        available=set(by_category),
    )
    assert all(pair.home_strength > pair.rival_strength for pair in found.pairs)
    assert ("gold", "metals", "colors") not in {
        (pair.token_norm, pair.home_key, pair.rival_key) for pair in found.pairs
    }


def test_index_skips_a_rival_without_quartets(decoy_db):
    """Соперника, которого нельзя поставить на поле, соблазном считать нельзя."""
    by_category = _pool(decoy_db)
    index = level_solver.load_memberships(decoy_db)
    metals_id = next(
        cid for cid, entries in by_category.items()
        if entries[0]["category_key"] == "metals"
    )
    found = decoy_pairs.build(
        (entry for entries in by_category.values() for entry in entries),
        index,
        available=set(by_category) - {metals_id},
    )
    assert all(pair.rival_key != "metals" for pair in found.pairs)


def test_index_respects_forbidden_pairs(decoy_db):
    """Пара `do_not_pair` остаётся запрещённой: ловушка её не отменяет."""
    by_category = _pool(decoy_db)
    index = level_solver.load_memberships(decoy_db)
    ids = {
        entries[0]["category_key"]: cid for cid, entries in by_category.items()
    }
    conflicts = {ids["colors"]: {ids["metals"]}, ids["metals"]: {ids["colors"]}}
    found = decoy_pairs.build(
        (entry for entries in by_category.values() for entry in entries),
        index,
        available=set(by_category),
        conflicts=conflicts,
    )
    assert ("colors", "metals") not in {
        (pair.home_key, pair.rival_key) for pair in found.pairs
    }


# -------------------------------------------------------------------- генератор


def test_generator_places_a_planned_decoy(decoy_db):
    levels, stats = level_generator.generate(
        decoy_db, count=1, category_count=4, seed=17,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    assert levels, "уровень не собрался"
    level = levels[0]
    assert level.planned_decoys, "ловушка не поставлена"
    assert stats["ловушек поставлено"] == len(level.planned_decoys)
    keys = {group.category_key for group in level.groups}
    for decoy in level.planned_decoys:
        assert decoy.home_key in keys and decoy.rival_key in keys
        assert decoy.home_strength > decoy.rival_strength


def test_planned_decoy_does_not_break_the_level(decoy_db):
    """Объявленная ловушка проходит автоприёмку, незапланированная — нет."""
    levels, _stats = level_generator.generate(
        decoy_db, count=1, category_count=4, seed=17,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    level = levels[0]
    assert level.planned_decoys
    assert level.is_valid, level.reject_reasons
    assert level.assessment is not None
    assert level.assessment.planned_decoy_count >= len(level.planned_decoys)


def test_rival_group_never_shows_the_same_bubble(decoy_db):
    """Два одинаковых пузыря на поле — брак, а не ловушка."""
    levels, _stats = level_generator.generate(
        decoy_db, count=1, category_count=4, seed=17,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    level = levels[0]
    by_key = {group.category_key: group for group in level.groups}
    for decoy in level.planned_decoys:
        rival = by_key[decoy.rival_key]
        shown = {display.strip().lower() for _w, _s, display, _sk, _r in rival.tokens}
        assert decoy.token_display.strip().lower() not in shown


def test_decoys_are_saved_as_planned(decoy_db):
    """Замысел живёт в базе: без записи `assess-levels` отклонит уровень."""
    levels, _stats = level_generator.generate(
        decoy_db, count=1, category_count=4, seed=17,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    with decoy_db:
        level_generator.save(decoy_db, levels)
    rows = list(
        decoy_db.execute(
            "SELECT planned, plausibility FROM level_decoys WHERE planned = 1"
        )
    )
    assert len(rows) == len(levels[0].planned_decoys)
    assert all(row["plausibility"] is not None for row in rows)


def test_no_decoys_when_switched_off(decoy_db):
    levels, stats = level_generator.generate(
        decoy_db, count=1, category_count=4, seed=17,
        use_meta=False, use_decoys=False, key_prefix="D",
    )
    assert levels and not levels[0].planned_decoys
    assert stats["ловушек поставлено"] == 0


def test_generation_with_decoys_is_deterministic(decoy_db):
    first, _ = level_generator.generate(
        decoy_db, count=2, category_count=4, seed=23,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    second, _ = level_generator.generate(
        decoy_db, count=2, category_count=4, seed=23,
        use_meta=False, decoy_target=2, key_prefix="D",
    )
    assert [level.content_hash() for level in first] == [
        level.content_hash() for level in second
    ]
    assert [
        [decoy.as_dict() for decoy in level.planned_decoys] for level in first
    ] == [
        [decoy.as_dict() for decoy in level.planned_decoys] for level in second
    ]
