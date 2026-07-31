"""Путь от четвёрок до принятого уровня.

Проверяется вся цепочка: сборка кандидата, полная автопроверка, пакет на
приёмку, применение решения человека и точечный возврат дефекта в базу.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from word_content import cooldown, integrity, level_generator, level_review, quartet_builder
from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships
from word_content.models import QuartetInput
from word_content.readiness import derive
from word_content.repositories import upsert_quartet
from word_content.sense_map import SenseMap

# Шесть непересекающихся категорий по восемь слов: материал на несколько уровней.
POOLS = {
    "trees": ["oak", "maple", "birch", "pine", "cedar", "willow", "aspen", "elm"],
    "birds": ["robin", "sparrow", "finch", "wren", "magpie", "starling", "swift", "heron"],
    "tools": ["hammer", "wrench", "pliers", "chisel", "mallet", "clamp", "rasp", "awl"],
    "cheeses": ["cheddar", "brie", "gouda", "feta", "edam", "colby", "havarti", "asiago"],
    "planets": ["mercury", "venus", "mars", "jupiter", "saturn", "neptune", "uranus", "pluto"],
    "rivers": ["nile", "amazon", "danube", "volga", "seine", "rhine", "thames", "congo"],
}
LABELS = {
    "trees": ("TREES", "Common trees of temperate forests"),
    "birds": ("BIRDS", "Small birds seen in gardens and parks"),
    "tools": ("HAND TOOLS", "Tools used by hand in a workshop"),
    "cheeses": ("CHEESES", "Cheeses sold in an ordinary supermarket"),
    "planets": ("PLANETS", "Planets and dwarf planets of the solar system"),
    "rivers": ("RIVERS", "Major rivers known around the world"),
}


@pytest.fixture
def flow_db(tmp_path: Path):
    path = tmp_path / "flow.sqlite"
    init_db(path)
    conn = connect(path)

    (tmp_path / "categories.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "category_key": key,
                    "label": LABELS[key][0],
                    "rule": LABELS[key][1],
                    "relation_type": "is_a",
                    "theme": "test",
                    "base_difficulty": 0.3,
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
                    "reason": f"{word} принадлежит {key}",
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


# --------------------------------------------------------------------- четвёрки


def test_quartet_candidates_are_scored_and_limited(flow_db):
    """На категорию сохраняется ограниченный набор с объяснимыми оценками."""
    rows = list(
        flow_db.execute(
            "SELECT c.category_key AS key, COUNT(*) AS n FROM quartets q "
            "JOIN categories c ON c.id = q.category_id GROUP BY 1"
        )
    )
    assert rows and all(row["n"] <= 2 for row in rows)
    scored = flow_db.execute(
        "SELECT cohesion_score, familiarity_score, ambiguity_pressure, validator_version, origin "
        "FROM quartets LIMIT 1"
    ).fetchone()
    assert scored["cohesion_score"] is not None
    assert scored["validator_version"]
    assert scored["origin"] == "derived"


def test_no_human_approved_state_on_quartets(flow_db):
    states = {row[0] for row in flow_db.execute("SELECT DISTINCT validation_state FROM quartets")}
    assert states <= {"proposed", "auto_validated", "warning", "invalid", "disabled"}


# --------------------------------------------------------------------- сборка уровней


def test_generate_saves_level_with_solver_run(flow_db):
    levels, stats = level_generator.generate(flow_db, count=2, category_count=3, seed=7)
    assert levels and stats["уровней собрано"] == 2
    assert all(level.solver.unique for level in levels)

    with flow_db:
        saved = level_generator.save(flow_db, levels)
    assert saved == 2

    row = flow_db.execute(
        "SELECT status, solution_count, content_hash, generator_version, random_seed "
        "FROM level_instances ORDER BY level_key LIMIT 1"
    ).fetchone()
    assert row["status"] == "solver_valid"
    assert row["solution_count"] == 1
    assert row["content_hash"] and row["generator_version"] and row["random_seed"] == 7

    run = flow_db.execute("SELECT * FROM level_solver_runs LIMIT 1").fetchone()
    assert run["outcome"] == "unique"
    assert run["input_hash"] and run["solver_version"] and json.loads(run["parameters"])


def test_generation_is_deterministic_for_same_seed(flow_db):
    first, _ = level_generator.generate(flow_db, count=2, category_count=3, seed=11)
    second, _ = level_generator.generate(flow_db, count=2, category_count=3, seed=11)
    assert [level.content_hash() for level in first] == [
        level.content_hash() for level in second
    ]


def test_level_groups_reference_exact_quartets(flow_db):
    """Уровень ссылается на конкретную четвёрку, а не на категорию целиком."""
    levels, _ = level_generator.generate(flow_db, count=1, category_count=3, seed=3)
    with flow_db:
        level_generator.save(flow_db, levels)
    missing = flow_db.execute(
        "SELECT COUNT(*) FROM level_groups WHERE quartet_id IS NULL"
    ).fetchone()[0]
    assert missing == 0


def test_level_checks_pass_for_generated_levels(flow_db):
    levels, _ = level_generator.generate(flow_db, count=3, category_count=3, seed=5)
    with flow_db:
        level_generator.save(flow_db, levels)
    failed = [r for r in integrity.run_level_checks(flow_db) if r.failed]
    assert not failed, [r.question for r in failed]


# --------------------------------------------------------------------- приёмка уровня


def _decisions_file(path: Path, rows: list[dict[str, str]]) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=level_review.DECISION_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in level_review.DECISION_COLUMNS})
    return path


@pytest.fixture
def with_levels(flow_db):
    levels, _ = level_generator.generate(flow_db, count=3, category_count=3, seed=13)
    with flow_db:
        level_generator.save(flow_db, levels)
    return flow_db


def test_review_package_has_everything_for_a_decision(with_levels):
    packages = level_review.build(with_levels)
    assert packages
    package = packages[0]
    assert package.solution_count == 1
    assert package.solver["outcome"] == "unique"
    assert package.difficulty_score and package.difficulty_components
    assert len(package.groups) == 3
    assert all(len(group["tokens"]) == 4 for group in package.groups)
    assert package.content_hash


def test_accept_marks_level_and_counts_quartet_use(with_levels, tmp_path):
    package = level_review.build(with_levels)[0]
    path = _decisions_file(
        tmp_path / "decisions.csv",
        [{"level_key": package.level_key, "decision": "accept", "review_note": "хороший вход"}],
    )
    with with_levels:
        report = level_review.apply_decisions(with_levels, path)
    assert report.applied == 1

    row = with_levels.execute(
        "SELECT status, review_note, accepted_version FROM level_instances WHERE level_key = ?",
        (package.level_key,),
    ).fetchone()
    assert row["status"] == "accepted"
    assert row["review_note"] == "хороший вход"
    assert row["accepted_version"] == 1

    used = with_levels.execute(
        "SELECT SUM(accepted_level_use_count) FROM quartets"
    ).fetchone()[0]
    assert used == 3


def test_reject_with_weak_quartet_disables_that_quartet(with_levels, tmp_path):
    package = level_review.build(with_levels)[0]
    quartet_key = package.groups[0]["quartet_key"]
    path = _decisions_file(
        tmp_path / "decisions.csv",
        [
            {
                "level_key": package.level_key,
                "decision": "reject",
                "review_note": "четвёрка натянута",
                "rejection_reason_codes": "weak_quartet",
                "target_kind": "quartet",
                "target_ref": quartet_key,
            }
        ],
    )
    with with_levels:
        report = level_review.apply_decisions(with_levels, path)
    assert report.applied == 1
    assert any("выключена" in note for note in report.feedback)

    state = with_levels.execute(
        "SELECT validation_state, last_rejection_reason FROM quartets WHERE quartet_key = ?",
        (quartet_key,),
    ).fetchone()
    assert state["validation_state"] == "disabled"
    assert state["last_rejection_reason"] == "weak_quartet"


def test_disabled_quartet_leaves_generation_pool(with_levels, tmp_path):
    package = level_review.build(with_levels)[0]
    quartet_key = package.groups[0]["quartet_key"]
    with with_levels:
        level_review.apply_decisions(
            with_levels,
            _decisions_file(
                tmp_path / "decisions.csv",
                [
                    {
                        "level_key": package.level_key,
                        "decision": "reject",
                        "rejection_reason_codes": "weak_quartet",
                        "target_kind": "quartet",
                        "target_ref": quartet_key,
                    }
                ],
            ),
        )
    usable = level_generator._usable_quartets(with_levels, "normal")
    keys = {
        entry["quartet_id"]
        for entries in usable.values()
        for entry in entries
    }
    disabled_id = with_levels.execute(
        "SELECT id FROM quartets WHERE quartet_key = ?", (quartet_key,)
    ).fetchone()["id"]
    assert disabled_id not in keys


def test_level_only_conflict_changes_nothing_in_base(with_levels, tmp_path):
    """Дефект комбинации не должен вычёркивать нормальные слова из базы."""
    package = level_review.build(with_levels)[0]
    before = with_levels.execute(
        "SELECT COUNT(*) FROM memberships WHERE review_status = 'rejected'"
    ).fetchone()[0]
    with with_levels:
        report = level_review.apply_decisions(
            with_levels,
            _decisions_file(
                tmp_path / "decisions.csv",
                [
                    {
                        "level_key": package.level_key,
                        "decision": "reject",
                        "rejection_reason_codes": "level_only_conflict",
                        "target_kind": "level",
                        "target_ref": package.level_key,
                    }
                ],
            ),
        )
    after = with_levels.execute(
        "SELECT COUNT(*) FROM memberships WHERE review_status = 'rejected'"
    ).fetchone()[0]
    assert before == after
    assert report.feedback == []
    reason = with_levels.execute(
        "SELECT applied, note FROM level_decision_reasons LIMIT 1"
    ).fetchone()
    assert reason["applied"] == 0


def test_accepted_level_is_not_overwritten_by_regeneration(with_levels, tmp_path):
    package = level_review.build(with_levels)[0]
    with with_levels:
        level_review.apply_decisions(
            with_levels,
            _decisions_file(
                tmp_path / "decisions.csv",
                [{"level_key": package.level_key, "decision": "accept"}],
            ),
        )
    levels, _ = level_generator.generate(with_levels, count=3, category_count=3, seed=99)
    with with_levels:
        level_generator.save(with_levels, levels)
    row = with_levels.execute(
        "SELECT status FROM level_instances WHERE level_key = ?", (package.level_key,)
    ).fetchone()
    assert row["status"] == "accepted"


def test_unknown_reason_code_is_reported(with_levels, tmp_path):
    package = level_review.build(with_levels)[0]
    with with_levels:
        report = level_review.apply_decisions(
            with_levels,
            _decisions_file(
                tmp_path / "decisions.csv",
                [
                    {
                        "level_key": package.level_key,
                        "decision": "reject",
                        "rejection_reason_codes": "потому_что",
                    }
                ],
            ),
        )
    assert any("неизвестный код" in error for error in report.errors)


# --------------------------------------------------------------------- cooldown


def test_cooldown_config_is_strict(tmp_path):
    good = tmp_path / "ok.yaml"
    good.write_text("same_word_sense: 5\n# комментарий\n", encoding="utf-8")
    assert cooldown.load_config(good)["same_word_sense"] == 5

    bad = tmp_path / "bad.yaml"
    bad.write_text("nested:\n  key: 1\n", encoding="utf-8")
    with pytest.raises(cooldown.ConfigError):
        cooldown.load_config(bad)

    unknown = tmp_path / "unknown.yaml"
    unknown.write_text("same_word: 5\n", encoding="utf-8")
    with pytest.raises(cooldown.ConfigError):
        cooldown.load_config(unknown)


def test_cooldown_blocks_repeat_of_recent_category():
    history = cooldown.UsageHistory()
    history.remember(1, word_senses=[(1, None)], category_ids=[10], concept_ids=[100],
                     quartet_ids=[1000])
    config = dict(cooldown.DEFAULTS)
    violations = cooldown.check(
        position=2,
        history=history,
        config=config,
        word_senses=[(1, None)],
        category_ids=[10],
        concept_ids=[100],
        quartet_ids=[1000],
        labels=["TREES"],
        displays=["oak"],
    )
    kinds = {v.kind for v in violations}
    assert {"same_word_sense", "same_category_variant", "same_quartet"} <= kinds


def test_duplicate_display_in_level_is_a_violation():
    violations = cooldown.check(
        position=1,
        history=cooldown.UsageHistory(),
        config=dict(cooldown.DEFAULTS),
        word_senses=[],
        category_ids=[],
        concept_ids=[],
        quartet_ids=[],
        labels=["TREES", "BIRDS"],
        displays=["oak", "Oak"],
    )
    assert [v.kind for v in violations] == ["duplicate_display_in_level"]
