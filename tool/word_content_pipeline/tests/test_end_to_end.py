"""Сквозной прогон через CLI: от текстовых источников до принятого уровня.

Тест повторяет реальный порядок работы и потому ловит то, что не видят
модульные тесты: несогласованность команд между собой, забытый шаг миграции,
неверный код возврата. Каждая команда вызывается так же, как её вызывает
человек, и обязана вернуть ноль.
"""

from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path

import pytest
from typer.testing import CliRunner

from word_content.cli import app

runner = CliRunner()

CATEGORIES = [
    ("trees", "TREES", "Common trees of temperate forests"),
    ("birds", "BIRDS", "Small birds seen in gardens and parks"),
    ("tools", "HAND TOOLS", "Tools used by hand in a workshop"),
    ("cheeses", "CHEESES", "Cheeses sold in an ordinary supermarket"),
    ("rivers", "RIVERS", "Major rivers known around the world"),
]
WORDS = {
    "trees": ["oak", "maple", "birch", "pine", "cedar", "willow"],
    "birds": ["robin", "sparrow", "finch", "wren", "magpie", "heron"],
    "tools": ["hammer", "wrench", "pliers", "chisel", "mallet", "clamp"],
    "cheeses": ["cheddar", "brie", "gouda", "feta", "edam", "colby"],
    "rivers": ["nile", "amazon", "danube", "volga", "seine", "rhine"],
}


def run(*args: str) -> object:
    result = runner.invoke(app, list(args))
    assert result.exit_code == 0, f"{' '.join(args)}\n{result.output}\n{result.exception}"
    return result


@pytest.fixture
def workspace(tmp_path: Path) -> Path:
    (tmp_path / "categories.jsonl").write_text(
        "\n".join(
            json.dumps(
                {
                    "category_key": key,
                    "label": label,
                    "rule": rule,
                    "relation_type": "is_a",
                    "theme": "test",
                    "base_difficulty": 0.3,
                },
                ensure_ascii=False,
            )
            for key, label, rule in CATEGORIES
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
                    "source": "seed_manual",
                    "review_status": "approved",
                },
                ensure_ascii=False,
            )
            for key, words in WORDS.items()
            for word in words
        )
        + "\n",
        encoding="utf-8",
    )
    return tmp_path


def test_full_pipeline_from_sources_to_accepted_level(workspace: Path):
    db = workspace / "content.sqlite"

    run("init-db", "--db", str(db))
    run("migrate-content-schema", "--db", str(db))
    run("import-categories", "--db", str(db), "--input", str(workspace / "categories.jsonl"))
    run("import-memberships", "--db", str(db), "--input", str(workspace / "memberships.jsonl"))
    run("derive-readiness", "--db", str(db))
    run("derive-conflicts", "--db", str(db), "--output", str(workspace / "conflicts.csv"))
    run("build-quartet-candidates", "--db", str(db), "--output", str(workspace / "quartets.csv"))
    run("validate-quartets", "--db", str(db))
    run(
        "generate-level-candidates",
        "--db", str(db), "--limit", "2", "--categories", "3", "--seed", "42",
        # Синтетическая мини-база уровни оригинала воспроизвести не может и не
        # должна: здесь проверяется пайплайн, а не воспроизводимость записи.
        # Барьер снимается явным флагом — молча его обходить нельзя.
        "--skip-reference-gate",
    )
    run("validate-levels", "--db", str(db))
    pack = workspace / "review"
    run("export-level-review-pack", "--db", str(db), "--output", str(pack))

    assert (pack / "LEVELS.md").exists()
    assert (pack / "levels.json").exists()
    decisions = pack / "level_decisions.csv"
    assert decisions.exists()

    packages = json.loads((pack / "levels.json").read_text(encoding="utf-8"))
    assert packages and all(p["solution_count"] == 1 for p in packages)

    rows = list(csv.DictReader(decisions.open(encoding="utf-8")))
    rows[0]["decision"] = "accept"
    rows[0]["review_note"] = "категории читаются, первый ход очевиден"
    with decisions.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    run("apply-level-decisions", "--db", str(db), "--input", str(decisions))
    run("check-integrity", "--db", str(db))
    run("baseline-report", "--db", str(db), "--output", str(workspace / "metrics.json"))

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    try:
        accepted = conn.execute(
            "SELECT COUNT(*) FROM level_instances WHERE status = 'accepted'"
        ).fetchone()[0]
        assert accepted == 1
        used = conn.execute(
            "SELECT COUNT(DISTINCT g.quartet_id) FROM level_groups g "
            "JOIN level_instances l ON l.id = g.level_id WHERE l.status = 'accepted'"
        ).fetchone()[0]
        assert used == 3
    finally:
        conn.close()

    metrics = json.loads((workspace / "metrics.json").read_text(encoding="utf-8"))
    assert metrics["levels_solver_valid"] >= 1
    assert metrics["quartets_in_accepted_levels"] == 3
    assert metrics["schema_version"] >= 4


def test_unsolvable_level_fails_solve_level_with_nonzero_exit(workspace: Path):
    """Команда обязана возвращать ненулевой код при блокирующей проблеме."""
    db = workspace / "content.sqlite"
    run("init-db", "--db", str(db))
    run("import-categories", "--db", str(db), "--input", str(workspace / "categories.jsonl"))
    run("import-memberships", "--db", str(db), "--input", str(workspace / "memberships.jsonl"))

    result = runner.invoke(
        app,
        [
            "solve-level", "--db", str(db),
            # По два слова из четырёх разных категорий: ни одна четвёрка не собирается.
            "--words", "oak,maple,robin,sparrow,hammer,wrench,cheddar,brie",
        ],
    )
    assert result.exit_code == 1
    assert "Отклонён" in result.output


def test_clean_rebuild_gives_the_same_content_hash(workspace: Path):
    """Две сборки из одних и тех же источников дают одинаковые уровни."""
    hashes = []
    for name in ("first", "second"):
        db = workspace / f"{name}.sqlite"
        run("init-db", "--db", str(db))
        run("import-categories", "--db", str(db), "--input", str(workspace / "categories.jsonl"))
        run("import-memberships", "--db", str(db), "--input", str(workspace / "memberships.jsonl"))
        run("derive-readiness", "--db", str(db))
        run("derive-conflicts", "--db", str(db), "--output", str(workspace / f"{name}.csv"))
        run("build-quartet-candidates", "--db", str(db))
        run(
            "generate-level-candidates",
            "--db", str(db), "--limit", "2", "--categories", "3", "--seed", "42",
            "--skip-reference-gate",
        )
        conn = sqlite3.connect(db)
        try:
            hashes.append(
                [
                    row[0]
                    for row in conn.execute(
                        "SELECT content_hash FROM level_instances ORDER BY level_key"
                    )
                ]
            )
        finally:
            conn.close()
    assert hashes[0] == hashes[1] and hashes[0]
