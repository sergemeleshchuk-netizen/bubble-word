from __future__ import annotations

import pytest

from word_content.normalization import (
    NormalizationError,
    is_valid_category_key,
    normalize_word,
)


def test_case_is_ignored():
    assert normalize_word("Apple") == normalize_word("apple") == "apple"
    assert normalize_word(" APPLE ") == "apple"


def test_multiple_spaces_collapse():
    assert normalize_word("ICE   CREAM") == "ice cream"
    assert normalize_word("\tice\n cream ") == "ice cream"


def test_typographic_apostrophe():
    assert normalize_word("Mother’s") == "mother's"
    assert normalize_word("motherʼs") == "mother's"


def test_typographic_hyphen():
    assert normalize_word("X–RAY") == "x-ray"
    assert normalize_word("x‑ray") == "x-ray"


def test_apostrophes_and_hyphens_are_kept():
    assert normalize_word("flip-flop") == "flip-flop"
    assert normalize_word("New Year's Eve") == "new year's eve"


def test_empty_string_is_rejected():
    with pytest.raises(NormalizationError):
        normalize_word("")
    with pytest.raises(NormalizationError):
        normalize_word("   ")


def test_too_long_word_is_rejected():
    with pytest.raises(NormalizationError):
        normalize_word("a" * 51)


def test_nfkc_normalization():
    # составной символ é и предсоставленный é должны совпасть
    assert normalize_word("café") == normalize_word("café")


def test_category_key_rules():
    assert is_valid_category_key("pie_ingredients")
    assert is_valid_category_key("words_before_sauce2")
    assert not is_valid_category_key("Pie_Ingredients")
    assert not is_valid_category_key("2fruits")
    assert not is_valid_category_key("pie ingredients")
    assert not is_valid_category_key("pie-ingredients")
    assert not is_valid_category_key("")
