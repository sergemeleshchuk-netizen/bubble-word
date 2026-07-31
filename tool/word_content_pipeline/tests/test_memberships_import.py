from __future__ import annotations

from pathlib import Path

from conftest import MEMBERSHIPS, write_jsonl

from word_content.importers import import_categories, import_memberships
from word_content.repositories import get_word, list_senses, memberships_for_word
from word_content.sense_map import SenseMap


def test_word_is_created_automatically(seeded):
    assert get_word(seeded, "apple") is not None


def test_existing_word_is_reused_across_cases(seeded):
    """Apple и apple — одна запись в words, различие значений живёт в word_senses."""
    rows = list(seeded.execute("SELECT * FROM words WHERE normalized = 'apple'"))
    assert len(rows) == 1
    senses = {row["sense_key"] for row in list_senses(seeded, int(rows[0]["id"]))}
    assert senses == {"apple_fruit", "apple_company"}


def test_word_belongs_to_several_categories(seeded):
    categories = {row["category_key"] for row in memberships_for_word(seeded, "apple")}
    assert categories == {"fruits", "pie_ingredients", "tech_companies"}


def test_two_senses_of_one_spelling(seeded):
    rows = memberships_for_word(seeded, "bank")
    senses = {row["sense_key"] for row in rows}
    assert senses == {"bank_river", "bank_finance"}


def test_repeated_import_creates_no_duplicates(seeded, memberships_file: Path):
    before = seeded.execute("SELECT COUNT(*) FROM memberships").fetchone()[0]
    report = import_memberships(seeded, memberships_file)
    after = seeded.execute("SELECT COUNT(*) FROM memberships").fetchone()[0]

    assert before == after
    assert (report.inserted, report.updated, report.rejected) == (0, len(MEMBERSHIPS), 0)


def test_idempotent_entity_counts(conn, categories_file: Path, memberships_file: Path):
    def counts() -> tuple[int, int, int, int]:
        return tuple(
            conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in ("words", "word_senses", "categories", "memberships")
        )

    import_categories(conn, categories_file)
    import_memberships(conn, memberships_file)
    first = counts()

    import_categories(conn, categories_file)
    import_memberships(conn, memberships_file)
    assert counts() == first


def test_unknown_category_is_rejected(seeded, tmp_path: Path):
    rows = [dict(MEMBERSHIPS[0], category_key="no_such_category")]
    report = import_memberships(seeded, write_jsonl(tmp_path / "bad.jsonl", rows))

    assert (report.inserted, report.rejected) == (0, 1)
    assert "no_such_category" in report.errors[0]["error"]


def test_score_out_of_range_is_rejected(seeded, tmp_path: Path):
    rows = [dict(MEMBERSHIPS[0], fit_score=1.5), dict(MEMBERSHIPS[1], obviousness_score=-0.2)]
    report = import_memberships(seeded, write_jsonl(tmp_path / "scores.jsonl", rows))

    assert report.rejected == 2
    assert report.inserted == 0


def test_sense_key_without_definition_is_rejected(seeded, tmp_path: Path):
    broken = dict(MEMBERSHIPS[0])
    broken.pop("sense_definition")
    report = import_memberships(seeded, write_jsonl(tmp_path / "sense.jsonl", broken and [broken]))

    assert report.rejected == 1
    assert "sense_definition" in report.errors[0]["error"]


def test_definition_without_sense_key_is_rejected(seeded, tmp_path: Path):
    broken = dict(MEMBERSHIPS[0])
    broken.pop("sense_key")
    report = import_memberships(seeded, write_jsonl(tmp_path / "sense2.jsonl", [broken]))

    assert report.rejected == 1
    assert "sense_key" in report.errors[0]["error"]


def test_one_bad_line_does_not_stop_the_rest(seeded, tmp_path: Path):
    rows = [
        dict(MEMBERSHIPS[0], category_key="ghost"),
        dict(MEMBERSHIPS[0], word="pear", reason="A pear is a common edible fruit"),
    ]
    report = import_memberships(seeded, write_jsonl(tmp_path / "mixed.jsonl", rows))

    assert (report.inserted, report.rejected) == (1, 1)
    assert get_word(seeded, "pear") is not None


def test_errors_are_stored_in_import_run(seeded, tmp_path: Path):
    rows = [dict(MEMBERSHIPS[0], category_key="ghost")]
    import_memberships(seeded, write_jsonl(tmp_path / "err.jsonl", rows))

    row = seeded.execute("SELECT * FROM import_runs ORDER BY id DESC LIMIT 1").fetchone()
    assert row["records_rejected"] == 1
    assert "ghost" in row["errors_json"]


def test_membership_without_sense_is_allowed(seeded, tmp_path: Path):
    row = dict(MEMBERSHIPS[0], word="peach", reason="A peach is a common edible fruit")
    row.pop("sense_key")
    row.pop("sense_definition")
    report = import_memberships(seeded, write_jsonl(tmp_path / "nosense.jsonl", [row]))

    assert report.inserted == 1
    assert memberships_for_word(seeded, "peach")[0]["sense_key"] is None


# --------------------------------------------------------------------------- #
# карта значений как общий источник для всех путей импорта
# --------------------------------------------------------------------------- #
def test_sense_comes_from_map_when_source_omits_it(seeded, tmp_path: Path):
    """Прогон AI не принёс значение — оно берётся из карты проекта.

    Регрессия из жизни: прогон мета-хабов принёс `atlas -> GEOGRAPHY CLASS` без
    sense_key, и многозначное слово заехало в категорию без смысла. Проверка
    приёмки это ловила, но уже после сборки базы.
    """
    sense_map = SenseMap(
        senses={"apple": {"apple_fruit": {"definition": "The round edible fruit of an apple tree"}}},
        assignments={"apple": {"river_features": "apple_fruit"}},
    )
    path = write_jsonl(tmp_path / "run.jsonl", [{
        "word": "apple", "category_key": "river_features", "relation_type": "found_in",
        "reason": "Проверочная связь без sense_key", "fit_score": 0.8,
        "obviousness_score": 0.7, "source": "test_run",
    }])
    import_memberships(seeded, path, sense_map=sense_map)

    row = seeded.execute(
        "SELECT s.sense_key FROM memberships m "
        "  JOIN words w ON w.id = m.word_id "
        "  JOIN categories c ON c.id = m.category_id "
        "  LEFT JOIN word_senses s ON s.id = m.sense_id "
        " WHERE w.normalized = 'apple' AND c.category_key = 'river_features'"
    ).fetchone()
    assert row["sense_key"] == "apple_fruit"


def test_sense_map_reuses_definition_already_in_base(seeded, tmp_path: Path):
    """Карта может только назначать: определение берётся из базы, если его нет в карте."""
    sense_map = SenseMap(assignments={"apple": {"town_places": "apple_company"}})
    path = write_jsonl(tmp_path / "run.jsonl", [{
        "word": "apple", "category_key": "town_places", "relation_type": "found_in",
        "reason": "Магазин Apple в городе", "fit_score": 0.8,
        "obviousness_score": 0.7, "source": "test_run",
    }])
    import_memberships(seeded, path, sense_map=sense_map)

    row = seeded.execute(
        "SELECT s.sense_key, s.definition FROM memberships m "
        "  JOIN words w ON w.id = m.word_id "
        "  JOIN categories c ON c.id = m.category_id "
        "  LEFT JOIN word_senses s ON s.id = m.sense_id "
        " WHERE w.normalized = 'apple' AND c.category_key = 'town_places'"
    ).fetchone()
    assert row["sense_key"] == "apple_company"
    assert row["definition"]


def test_membership_without_map_entry_keeps_no_sense(seeded, tmp_path: Path):
    """Пустая карта ничего не выдумывает: связь остаётся без значения."""
    path = write_jsonl(tmp_path / "run.jsonl", [{
        "word": "apple", "category_key": "town_places", "relation_type": "found_in",
        "reason": "Проверка отсутствия значения", "fit_score": 0.8,
        "obviousness_score": 0.7, "source": "test_run",
    }])
    import_memberships(seeded, path, sense_map=SenseMap())

    row = seeded.execute(
        "SELECT m.sense_id FROM memberships m "
        "  JOIN words w ON w.id = m.word_id "
        "  JOIN categories c ON c.id = m.category_id "
        " WHERE w.normalized = 'apple' AND c.category_key = 'town_places'"
    ).fetchone()
    assert row["sense_id"] is None
