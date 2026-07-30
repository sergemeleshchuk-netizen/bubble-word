from __future__ import annotations

from pathlib import Path

import pytest
from conftest import MEMBERSHIPS, write_jsonl

from word_content.blocklist import Blocklist, default_path
from word_content.familiarity import familiarity, is_rare, zipf
from word_content.importers import import_memberships
from word_content.repositories import collect_stats, coverage_report, get_word
from word_content.validators import ContentFilter, ValidationIssue

HAS_WORDFREQ = zipf("apple") is not None
needs_wordfreq = pytest.mark.skipif(not HAS_WORDFREQ, reason="wordfreq не установлен")


# ------------------------------------------------------------------------- блок-лист


@pytest.fixture
def blocklist(tmp_path: Path) -> Blocklist:
    path = tmp_path / "block.txt"
    path.write_text("# комментарий\nshit\nass\n\ncocaine\n", encoding="utf-8")
    return Blocklist.load(path)


def test_blocklist_matches_exact_word(blocklist: Blocklist):
    assert blocklist.check("shit") == "shit"
    assert blocklist.check("SHIT") == "shit"
    assert blocklist.check("apple") is None


def test_blocklist_does_not_match_substring(blocklist: Blocklist):
    """'ass' не должен блокировать 'grass' или 'glass'."""
    assert blocklist.check("grass") is None
    assert blocklist.check("glass") is None
    assert blocklist.check("class") is None


def test_blocklist_matches_word_inside_phrase(blocklist: Blocklist):
    assert blocklist.check("cocaine powder") == "cocaine"
    assert blocklist.check("ice cream") is None


def test_empty_blocklist_allows_everything():
    empty = Blocklist.load(None)
    assert not empty
    assert empty.check("shit") is None


def test_project_blocklist_exists_and_is_loaded():
    path = default_path()
    assert path is not None and path.name == "blocklist.txt"
    loaded = Blocklist.load(path)
    assert len(loaded) > 100
    assert loaded.check("fuck") is not None


def test_blocked_word_is_rejected_on_import(seeded, tmp_path: Path, blocklist: Blocklist):
    row = dict(MEMBERSHIPS[0], word="shit", reason="плохое слово")
    report = import_memberships(
        seeded,
        write_jsonl(tmp_path / "bad.jsonl", [row]),
        content_filter=ContentFilter(blocklist=blocklist),
    )

    assert (report.inserted, report.rejected) == (0, 1)
    assert "блок-лист" in report.errors[0]["error"]
    assert get_word(seeded, "shit") is None


# ----------------------------------------------------------------------- частотность


@needs_wordfreq
def test_zipf_orders_words_by_frequency():
    assert zipf("apple") > zipf("nutmeg") > zipf("oxbow")


@needs_wordfreq
def test_familiarity_is_normalized_to_unit_range():
    value = familiarity("apple")
    assert 0.0 < value < 1.0
    assert familiarity("the") > familiarity("apple")


@needs_wordfreq
def test_phrase_frequency_falls_back_to_rarest_part():
    assert zipf("ice cream") is not None
    assert zipf("qwertyuiop zzzzz") in (None, 0.0) or zipf("qwertyuiop zzzzz") < 2.0


@needs_wordfreq
def test_is_rare_uses_threshold():
    assert is_rare("oxbow", min_zipf=2.5)
    assert not is_rare("apple", min_zipf=2.5)


def test_unknown_frequency_is_not_treated_as_rare(monkeypatch):
    monkeypatch.setattr("word_content.familiarity.zipf", lambda word: None)
    from word_content import familiarity as module

    assert module.is_rare("что угодно") is False


@needs_wordfreq
def test_rare_word_is_rejected_with_min_zipf(seeded, tmp_path: Path):
    rows = [
        dict(MEMBERSHIPS[0], word="oxbow", reason="редкое слово"),
        dict(MEMBERSHIPS[0], word="pear", reason="A pear is a common edible fruit"),
    ]
    report = import_memberships(
        seeded, write_jsonl(tmp_path / "rare.jsonl", rows), content_filter=ContentFilter(min_zipf=3.0)
    )

    assert (report.inserted, report.rejected) == (1, 1)
    assert "слишком редкое" in report.errors[0]["error"]
    assert get_word(seeded, "pear") is not None


@needs_wordfreq
def test_familiarity_score_is_written_on_import(seeded, tmp_path: Path):
    row = dict(MEMBERSHIPS[0], word="pear", reason="A pear is a common edible fruit")
    import_memberships(
        seeded, write_jsonl(tmp_path / "f.jsonl", [row]), content_filter=ContentFilter()
    )

    assert get_word(seeded, "pear")["familiarity_score"] > 0


@needs_wordfreq
def test_stats_report_rare_words(seeded, tmp_path: Path):
    row = dict(MEMBERSHIPS[0], word="oxbow", reason="редкое слово")
    import_memberships(
        seeded, write_jsonl(tmp_path / "r.jsonl", [row]), content_filter=ContentFilter()
    )

    stats = collect_stats(seeded)
    assert stats["rare_words_total"] >= 1
    assert "oxbow" in [text for text, _ in stats["rare_words"]]


# -------------------------------------------------------------------------- coverage


def test_coverage_counts_missing_words(seeded):
    report = coverage_report(seeded, target_depth=10)

    per_key = {item["category_key"]: item for item in report["per_category"]}
    assert per_key["fruits"]["have"] == 1
    assert per_key["fruits"]["need"] == 9
    assert report["categories"] == 5
    assert report["memberships_needed"] == 10 * 5 - 5


def test_coverage_tracks_multi_category_words(seeded):
    report = coverage_report(seeded, target_depth=10)
    assert report["multi_category_words"] == 2  # apple и bank
    assert report["multi_category_share"] == 1.0


def test_coverage_respects_statuses(seeded):
    report = coverage_report(seeded, target_depth=10, statuses=["approved"])
    per_key = {item["category_key"]: item for item in report["per_category"]}
    assert per_key["tech_companies"]["have"] == 0  # там только candidate


def test_coverage_groups_by_theme(seeded):
    report = coverage_report(seeded, target_depth=10)
    assert report["by_theme"]["food"]["categories"] == 2
    assert report["by_theme"]["food"]["have"] == 2


# ------------------------------------------------------------- выбор целей генерации


def test_generation_targets_only_thin(seeded, tmp_path: Path):
    from word_content.cli import _generation_targets

    targets = _generation_targets(seeded, None, False, 2, None)
    assert "fruits" in targets  # одна связь, порог 2

    checkpoint = tmp_path / "done.txt"
    checkpoint.write_text("fruits\n", encoding="utf-8")
    targets_after = _generation_targets(seeded, None, False, 2, checkpoint)
    assert "fruits" not in targets_after


def test_generation_targets_requires_a_selector(seeded):
    from word_content.cli import _generation_targets

    with pytest.raises(ValidationIssue):
        _generation_targets(seeded, None, False, None, None)
    with pytest.raises(ValidationIssue):
        _generation_targets(seeded, "fruits", True, None, None)
