from __future__ import annotations

from pathlib import Path

from conftest import CATEGORIES, write_jsonl

from word_content.importers import import_categories
from word_content.repositories import get_category


def test_new_categories_are_created(conn, categories_file: Path):
    report = import_categories(conn, categories_file)
    assert (report.total, report.inserted, report.updated, report.rejected) == (5, 5, 0, 0)
    assert get_category(conn, "fruits")["label"] == "FRUITS"


def test_repeated_import_updates_category(conn, categories_file: Path, tmp_path: Path):
    import_categories(conn, categories_file)

    changed = [dict(CATEGORIES[0], label="EDIBLE FRUITS", base_difficulty=0.2)]
    report = import_categories(conn, write_jsonl(tmp_path / "again.jsonl", changed))

    assert (report.inserted, report.updated) == (0, 1)
    row = get_category(conn, "fruits")
    assert row["label"] == "EDIBLE FRUITS"
    assert row["base_difficulty"] == 0.2


def test_invalid_category_key_is_rejected(conn, tmp_path: Path):
    rows = [dict(CATEGORIES[0], category_key="Pie Ingredients")]
    report = import_categories(conn, write_jsonl(tmp_path / "bad.jsonl", rows))

    assert (report.total, report.inserted, report.rejected) == (1, 0, 1)
    assert "category_key" in report.errors[0]["error"]


def test_broken_json_line_does_not_stop_import(conn, tmp_path: Path):
    path = tmp_path / "mixed.jsonl"
    good = CATEGORIES[0]
    path.write_text(
        '{"category_key": "broken", "label":\n' + __import__("json").dumps(good) + "\n",
        encoding="utf-8",
    )
    report = import_categories(conn, path)

    assert report.rejected == 1
    assert report.inserted == 1
    assert get_category(conn, "fruits") is not None


def test_import_run_is_recorded(conn, categories_file: Path):
    import_categories(conn, categories_file)
    row = conn.execute("SELECT * FROM import_runs ORDER BY id DESC LIMIT 1").fetchone()
    assert row["import_type"] == "categories"
    assert row["records_inserted"] == 5
