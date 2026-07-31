from __future__ import annotations

import csv
from pathlib import Path

from conftest import MEMBERSHIPS, write_jsonl

from word_content.exporters import export_review_csv
from word_content.importers import REVIEW_CSV_COLUMNS, import_memberships, import_review_csv
from word_content.repositories import memberships_for_word


def _read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_export_has_expected_columns(seeded, tmp_path: Path):
    path = tmp_path / "review.csv"
    count = export_review_csv(seeded, path, ["candidate"])

    rows = _read_csv(path)
    assert count == len(rows) == 2  # два candidate в фикстуре
    assert list(rows[0].keys()) == REVIEW_CSV_COLUMNS
    assert rows[0]["decision"] == ""
    assert rows[0]["review_comment"] == ""


def test_import_review_updates_status(seeded, tmp_path: Path):
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    rows = _read_csv(path)
    for row in rows:
        row["decision"] = "approved"
        row["review_comment"] = "ок"
    _write_csv(path, rows)

    report = import_review_csv(seeded, path)
    assert (report.total, report.updated, report.rejected) == (2, 2, 0)

    statuses = {r["review_status"] for r in memberships_for_word(seeded, "apple")}
    assert statuses == {"approved"}


def test_empty_decision_is_skipped(seeded, tmp_path: Path):
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    report = import_review_csv(seeded, path)
    assert (report.total, report.updated) == (0, 0)


def test_alternative_status_is_accepted(seeded, tmp_path: Path):
    """alternative — верное, но не первое значение: ловушка для обычного уровня."""
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    rows = _read_csv(path)
    target = next(r for r in rows if r["category_key"] == "tech_companies")
    target["decision"] = "alternative"
    _write_csv(path, rows)

    report = import_review_csv(seeded, path)
    assert report.rejected == 0

    row = next(
        r for r in memberships_for_word(seeded, "apple") if r["category_key"] == "tech_companies"
    )
    assert row["review_status"] == "alternative"


def test_alternative_is_filterable(seeded, tmp_path: Path):
    """Генератор уровней должен уметь выбрать только ловушки."""
    seeded.execute(
        "UPDATE memberships SET review_status = 'alternative' WHERE id = "
        "(SELECT m.id FROM memberships m JOIN categories c ON c.id = m.category_id "
        " WHERE c.category_key = 'tech_companies')"
    )
    seeded.commit()

    rows = memberships_for_word(seeded, "apple", ["alternative"])
    assert [r["category_key"] for r in rows] == ["tech_companies"]


def test_decision_survives_shifted_membership_id(seeded, tmp_path: Path):
    """id зависит от порядка вставки; решение должно найтись по слову и категории."""
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    rows = _read_csv(path)
    target = next(r for r in rows if r["category_key"] == "tech_companies")
    target["membership_id"] = "4242"  # id уехал после пересборки базы
    target["decision"] = "hard_only"
    _write_csv(path, rows)

    report = import_review_csv(seeded, path)
    assert report.rejected == 0

    row = next(
        r for r in memberships_for_word(seeded, "apple") if r["category_key"] == "tech_companies"
    )
    assert row["review_status"] == "hard_only"


def test_wrong_id_without_word_columns_is_rejected(seeded, tmp_path: Path):
    """Если в CSV нет слова и категории, довериться нечему — строка отклоняется."""
    path = tmp_path / "minimal.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["membership_id", "decision", "review_comment"])
        writer.writeheader()
        writer.writerow({"membership_id": "99999", "decision": "approved", "review_comment": ""})

    report = import_review_csv(seeded, path)
    assert report.rejected == 1


def test_unknown_membership_is_rejected(seeded, tmp_path: Path):
    """Ни id, ни пара слово+категория не находятся — строку отклоняем."""
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    rows = _read_csv(path)
    rows[0]["membership_id"] = "99999"
    rows[0]["normalized"] = "no_such_word"
    rows[0]["category_key"] = "no_such_category"
    rows[0]["decision"] = "approved"
    _write_csv(path, rows)

    report = import_review_csv(seeded, path)
    assert report.rejected == 1
    assert "99999" in report.errors[0]["error"]


def test_unknown_decision_is_rejected(seeded, tmp_path: Path):
    path = tmp_path / "review.csv"
    export_review_csv(seeded, path, ["candidate"])
    rows = _read_csv(path)
    rows[0]["decision"] = "maybe_later"
    _write_csv(path, rows)

    report = import_review_csv(seeded, path)
    assert report.rejected == 1
    assert "decision" in report.errors[0]["error"]


def test_reimport_of_ai_candidate_does_not_reset_approved(seeded, tmp_path: Path):
    """Ручное решение не сбрасывается повторным импортом AI-кандидата."""
    ai_row = dict(
        MEMBERSHIPS[2],  # Apple -> tech_companies, в фикстуре candidate
        source="ai",
        review_status="candidate",
        reason="Apple is a technology company",
    )
    path = write_jsonl(tmp_path / "ai.jsonl", [ai_row])
    import_memberships(seeded, path)

    membership_id = next(
        r["membership_id"]
        for r in memberships_for_word(seeded, "apple")
        if r["category_key"] == "tech_companies"
    )
    seeded.execute(
        "UPDATE memberships SET review_status = 'approved' WHERE id = ?", (membership_id,)
    )
    seeded.commit()

    import_memberships(seeded, path)
    row = seeded.execute(
        "SELECT review_status FROM memberships WHERE id = ?", (membership_id,)
    ).fetchone()
    assert row["review_status"] == "approved"

    # но с флагом --overwrite-review-status статус можно вернуть принудительно
    import_memberships(seeded, path, overwrite_review_status=True)
    row = seeded.execute(
        "SELECT review_status FROM memberships WHERE id = ?", (membership_id,)
    ).fetchone()
    assert row["review_status"] == "candidate"


def _write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
