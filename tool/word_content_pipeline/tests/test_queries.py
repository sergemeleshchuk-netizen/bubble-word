from __future__ import annotations

from word_content.repositories import (
    collect_stats,
    memberships_for_category,
    memberships_for_word,
    words_with_status,
)


def test_word_info_returns_several_categories(seeded):
    rows = memberships_for_word(seeded, "APPLE")
    assert len(rows) == 3
    assert {r["category_key"] for r in rows} == {"fruits", "pie_ingredients", "tech_companies"}


def test_word_info_respects_statuses(seeded):
    rows = memberships_for_word(seeded, "apple", ["approved"])
    assert {r["category_key"] for r in rows} == {"fruits", "pie_ingredients"}


def test_category_info_returns_only_requested_statuses(seeded):
    approved = memberships_for_category(seeded, "tech_companies", ["approved"])
    candidates = memberships_for_category(seeded, "tech_companies", ["candidate"])
    assert approved == []
    assert [r["word"] for r in candidates] == ["apple"]


def test_category_info_returns_words(seeded):
    rows = memberships_for_category(seeded, "fruits")
    assert [r["normalized"] for r in rows] == ["apple"]


def test_words_with_status(seeded):
    words = words_with_status(seeded, ["approved"])
    assert sorted(words) == ["apple", "bank"]


def test_stats_counts_categories_per_word(seeded):
    stats = collect_stats(seeded)

    assert stats["words"] == 2
    assert stats["categories"] == 5
    assert stats["memberships"] == 5
    assert stats["senses"] == 4
    assert stats["by_status"] == {"approved": 3, "candidate": 2}
    # apple -> 3 категории, bank -> 2
    assert stats["words_by_category_count"]["3"] == 1
    assert stats["words_by_category_count"]["2"] == 1
    assert stats["avg_categories_per_word"] == 2.5


def test_stats_thin_categories_and_tops(seeded):
    stats = collect_stats(seeded)
    thin = dict(stats["thin_categories"])
    assert thin["fruits"] == 1  # одна approved-связь, порог 8
    assert stats["top_words"][0] == ("apple", 2)
