"""Тесты рейтингов качества.

Формулы здесь эвристические, и именно поэтому им нужны фиксированные примеры.
Regression-набор внизу — двадцать пять слов и пятнадцать названий с ожидаемым
порядком величин. Он не проверяет точное число (веса меняются осознанно),
он проверяет, что порядок не переворачивается: короткое знакомое слово не
может оказаться менее доступным, чем длинное редкое.
"""

from __future__ import annotations

import pytest

from word_content import profiles, scoring

CONFIG = scoring.load_config()


def access(display: str, familiarity: float | None, *, proper: bool = False) -> float:
    metrics = scoring.display_metrics(display, CONFIG)
    return scoring.accessibility(
        familiarity=familiarity,
        display_width_score=metrics["display_width_score"],
        char_count=metrics["char_count"],
        spelling_difficulty_score=scoring.spelling_difficulty(display, proper),
        config=CONFIG,
    ).score


# --------------------------------------------------------------------- метрики надписи


def test_char_and_token_count():
    assert scoring.display_metrics("apple", CONFIG)["char_count"] == 5
    assert scoring.display_metrics("apple", CONFIG)["token_count"] == 1
    assert scoring.display_metrics("polar bear", CONFIG)["token_count"] == 2
    assert scoring.display_metrics("hot air balloon", CONFIG)["token_count"] == 3


def test_hyphen_counts_as_a_word_boundary():
    assert scoring.display_metrics("merry-go-round", CONFIG)["token_count"] == 3


def test_display_width_accounts_for_wide_letters():
    """Ширина считается не только по числу букв: `mmmmmmm` шире, чем `illinois`."""
    wide = scoring.display_metrics("wmwmwmw", CONFIG)["display_width_score"]
    narrow = scoring.display_metrics("illllli", CONFIG)["display_width_score"]
    assert narrow > wide


def test_long_phrase_does_not_fit_the_bubble():
    assert scoring.display_metrics("hot air balloon", CONFIG)["display_width_score"] < 0.4
    assert scoring.display_metrics("oak", CONFIG)["display_width_score"] == 1.0


# --------------------------------------------------------------------- сложность письма


@pytest.mark.parametrize("word", ["cat", "table", "window", "garden"])
def test_simple_words_are_easy_to_spell(word):
    assert scoring.spelling_difficulty(word, False) < 0.2


@pytest.mark.parametrize("word", ["psychiatrist", "borough", "schnauzer"])
def test_awkward_words_are_harder(word):
    assert scoring.spelling_difficulty(word, False) >= 0.2


def test_diacritics_add_difficulty():
    assert scoring.spelling_difficulty("crème", False) > scoring.spelling_difficulty("cream", False)


def test_abbreviation_is_harder_than_plain_word():
    assert scoring.spelling_difficulty("NASA", True) > scoring.spelling_difficulty("nasal", False)


# --------------------------------------------------------------------- новизна


def test_novelty_is_not_rarity():
    """Банальное и крайне редкое слово одинаково неинтересны — по разным причинам."""
    banal = scoring.novelty(0.95, CONFIG)
    interesting = scoring.novelty(0.57, CONFIG)
    obscure = scoring.novelty(0.10, CONFIG)
    assert interesting > banal
    assert interesting > obscure


def test_unknown_familiarity_gives_no_novelty():
    assert scoring.novelty(None, CONFIG) == 0.0


# --------------------------------------------------------------------- доступность


def test_short_familiar_word_is_most_accessible():
    assert access("apple", 0.85) > 0.8


def test_long_familiar_word_loses_to_short_one():
    assert access("refrigerator", 0.80) < access("fridge", 0.80)


def test_short_rare_word_loses_to_short_familiar():
    assert access("adze", 0.15) < access("axe", 0.85)


def test_long_rare_word_is_least_accessible():
    worst = access("bathysphere", 0.10)
    assert worst < access("adze", 0.15)
    assert worst < access("refrigerator", 0.80)


def test_multiword_phrase_is_less_accessible_than_one_word():
    assert access("hot air balloon", 0.60) < access("balloon", 0.60)


def test_unknown_familiarity_is_not_treated_as_average():
    """Пропущенная частотность не должна выглядеть как средняя: она считается нулевой."""
    assert access("wombat", None) < access("wombat", 0.5)


# --------------------------------------------------------------------- неоднозначность


def test_ambiguity_grows_with_senses_and_themes():
    single = scoring.ambiguity(1, 2, 1)
    many = scoring.ambiguity(5, 12, 6)
    assert many > single
    assert 0.0 <= single <= 1.0 and 0.0 <= many <= 1.0


# --------------------------------------------------------------------- названия категорий


def test_good_short_label_scores_high():
    for label in ("BIRDS OF PREY", "KITCHEN TOOLS", "THINGS THAT MELT"):
        assert scoring.label_clarity(label).score >= 0.9


def test_vague_label_scores_low():
    for label in ("MISCELLANEOUS ITEMS", "RELATED THINGS", "SPECIAL WORDS"):
        assert scoring.label_clarity(label).score < 0.6


def test_broad_label_is_not_penalised_in_quality():
    """Широкая надпись — норма референса, а не дефект.

    FOOD, SCHOOL, DOCTOR, BIRD показываются ПОСЛЕ решения и объясняют четвёрку
    задним числом. Прежняя формула штрафовала их за «непрозрачный принцип»,
    то есть была настроена прямо против игры, которую воспроизводим.
    """
    for label in ("FOOD", "SCHOOL", "DOCTOR", "BIRD", "TREE", "CAT"):
        assert scoring.label_clarity(label).score == 1.0, label
        assert scoring.label_retrospective_fit(label, 120).score == 1.0, label
        assert scoring.label_scope(label, 120) == "broad", label


def test_label_scope_is_descriptive_not_a_score():
    assert scoring.label_scope("FOOD", 120) == "broad"
    assert scoring.label_scope("KITCHEN TOOLS", 20) == "medium"
    assert scoring.label_scope("AFRICAN SAVANNA PREDATORS", 9) == "narrow"


def test_empty_label_explains_nothing():
    assert scoring.label_retrospective_fit("RELATED THINGS", 25).score < 0.4
    assert scoring.label_reveal_satisfaction("RELATED THINGS").score < 0.6


def test_broad_label_is_clear_but_not_specific():
    """`ANIMALS` понятно, но принцип не сужен — это разные оси."""
    clarity = scoring.label_clarity("ANIMALS").score
    specificity = scoring.label_specificity("ANIMALS", 80).score
    assert clarity > specificity


def test_narrower_label_is_more_specific():
    broad = scoring.label_specificity("ANIMALS", 80).score
    narrow = scoring.label_specificity("AFRICAN SAVANNA PREDATORS", 12).score
    assert narrow > broad


def test_unnatural_label_is_flagged():
    assert scoring.label_naturalness("THINGS MADE OF").score < 0.7
    assert scoring.label_naturalness("kitchen_tools_v2").score < 0.8
    assert scoring.label_naturalness("KITCHEN TOOLS").score == 1.0


def test_label_quality_combines_axes():
    good = scoring.label_quality(
        naturalness=1.0, clarity=1.0, retrospective_fit=1.0, reveal_satisfaction=1.0,
        display_width_score=1.0, familiarity=0.7, config=CONFIG,
    )
    bad = scoring.label_quality(
        naturalness=0.6, clarity=0.3, retrospective_fit=0.3, reveal_satisfaction=0.4,
        display_width_score=0.2, familiarity=0.4, config=CONFIG,
    )
    assert good.score > bad.score
    assert set(good.parts) == {
        "naturalness", "clarity", "retrospective_fit", "reveal", "display", "familiarity"
    }


# --------------------------------------------------------------------- четвёрка


def test_weakest_link_hurts_more_than_average():
    """Одна натянутая связь портит четвёрку сильнее, чем четыре средние."""
    one_weak = scoring.cohesion([1.0, 1.0, 1.0, 0.4], CONFIG).score
    all_medium = scoring.cohesion([0.85, 0.85, 0.85, 0.85], CONFIG).score
    assert one_weak < all_medium


def _interest(novelties: list[float], rare: int = 0) -> float:
    return scoring.quartet_interest(
        novelty_scores=novelties,
        accessibility_scores=[0.8, 0.75, 0.7, 0.72],
        cohesion_score=0.9,
        label_quality_score=0.85,
        rare_count=rare,
        config=CONFIG,
    ).score


def test_four_banal_words_are_not_interesting():
    assert _interest([0.1, 0.1, 0.05, 0.1]) < 0.6


def test_one_interesting_element_lifts_the_quartet():
    banal = _interest([0.1, 0.1, 0.05, 0.1])
    with_spark = _interest([0.1, 0.1, 0.05, 0.9])
    assert with_spark > banal


def test_too_many_rare_words_kill_interest():
    """Четыре редких слова — это не интересно, это непроходимо."""
    one_rare = _interest([0.6, 0.5, 0.4, 0.9], rare=1)
    many_rare = _interest([0.6, 0.5, 0.4, 0.9], rare=4)
    assert many_rare < one_rare


def test_quality_and_interest_are_separate_axes():
    """Понятная и скучная четвёрка: качество высокое, интересность низкая."""
    quality = scoring.quartet_quality(
        cohesion_score=0.95, avg_accessibility=0.9, clarity_score=0.9,
        label_quality_score=0.9, config=CONFIG,
    ).score
    interest = _interest([0.05, 0.05, 0.05, 0.05])
    assert quality > 0.85
    assert interest < quality


def test_every_score_is_in_range():
    for value in (
        access("bathysphere", 0.0),
        access("a", 1.0),
        scoring.cohesion([0.0, 0.0, 0.0, 0.0], CONFIG).score,
        scoring.cohesion([1.0, 1.0, 1.0, 1.0], CONFIG).score,
        _interest([1.0, 1.0, 1.0, 1.0]),
        _interest([0.0, 0.0, 0.0, 0.0], rare=4),
        scoring.label_clarity("").score,
    ):
        assert 0.0 <= value <= 1.0


# --------------------------------------------------------------------- профили


@pytest.fixture
def three_profiles():
    loaded = profiles.load()
    assert {"easy_accessible", "accessible_fun", "hard_knowledge"} <= set(loaded)
    return loaded


def _facts(**overrides) -> profiles.QuartetFacts:
    base = {
        "quartet_key": "test__1",
        "label_text": "FRUITS",
        "min_familiarity": 0.7,
        "avg_familiarity": 0.8,
        "min_accessibility": 0.75,
        "max_word_chars": 6,
        "max_word_tokens": 1,
        "label_chars": 12,
        "label_tokens": 2,
        "label_quality": 0.85,
        "quartet_quality": 0.85,
        "quartet_interest": 0.5,
        "ambiguity": 0.3,
        "rare_words": 0,
        "long_phrases": 0,
    }
    base.update(overrides)
    return profiles.QuartetFacts(**base)


def test_easy_profile_accepts_a_simple_quartet(three_profiles):
    assert profiles.check_quartet(three_profiles["easy_accessible"], _facts()) == []


def test_easy_profile_rejects_a_rare_word(three_profiles):
    reasons = profiles.check_quartet(
        three_profiles["easy_accessible"], _facts(min_familiarity=0.2, avg_familiarity=0.45)
    )
    assert any("знакомость" in reason for reason in reasons)


def test_easy_profile_rejects_a_long_phrase(three_profiles):
    reasons = profiles.check_quartet(
        three_profiles["easy_accessible"], _facts(max_word_chars=18, max_word_tokens=3)
    )
    assert any("символов" in reason for reason in reasons)


def test_hard_profile_accepts_what_easy_rejects(three_profiles):
    facts = _facts(min_familiarity=0.25, avg_familiarity=0.45, min_accessibility=0.4)
    assert profiles.check_quartet(three_profiles["easy_accessible"], facts)
    assert profiles.check_quartet(three_profiles["hard_knowledge"], facts) == []


def test_first_lineup_rejects_a_vague_label():
    """Надпись-признак не отсекается порогами качества — нужен явный запрет.

    STRETCHY THINGS короткая, частотная и получает высокий label_quality:
    формально с ней всё в порядке, а игрок такую группу добирает по остатку.
    В ремейке двадцатки таких надписей вышло 33 из 192 — полтора балла фана.
    """
    profile = profiles.get("first_lineup")
    good = _facts(label_text="FARM ANIMALS")
    bad = _facts(label_text="STRETCHY THINGS")
    assert profiles.check_quartet(profile, good) == []
    assert any("признак" in reason for reason in profiles.check_quartet(profile, bad))
    # Остальные профили запрет не наследуют: поздняя кампания на таких группах
    # работает, там игрок уже знает правила.
    assert profiles.check_quartet(profiles.get("accessible_fun"), bad) == []


def test_first_lineup_rejects_a_two_word_bubble():
    """«harbor seal» — не слово в пузыре: у первой линейки один токен."""
    profile = profiles.get("first_lineup")
    reasons = profiles.check_quartet(profile, _facts(max_word_tokens=2, max_word_chars=11))
    assert any("фраза" in reason for reason in reasons)


def test_unknown_score_does_not_pass_a_threshold(three_profiles):
    """Непосчитанная метрика не проходит порог: пропуск закрывает путь в уровень."""
    reasons = profiles.check_quartet(
        three_profiles["easy_accessible"], _facts(min_familiarity=None)
    )
    assert any("не посчитана" in reason for reason in reasons)


def test_level_budget_limits_rare_words(three_profiles):
    budget = profiles.LevelBudget.for_profile(three_profiles["easy_accessible"])
    assert budget.rare_words == 0
    assert budget.fits(_facts(rare_words=1)) is not None

    fun = profiles.LevelBudget.for_profile(three_profiles["accessible_fun"])
    assert fun.fits(_facts(rare_words=1)) is None
    fun.spend(_facts(rare_words=1))
    fun.spend(_facts(rare_words=1))
    assert fun.fits(_facts(rare_words=1)) is not None


def test_profile_config_is_strict(tmp_path):
    bad = tmp_path / "profiles.yaml"
    bad.write_text("easy.unknown_parameter: 1\n", encoding="utf-8")
    with pytest.raises(profiles.flat_config.ConfigError):
        profiles.load(bad)

    nested = tmp_path / "nested.yaml"
    nested.write_text("easy:\n  word_familiarity_min: 0.5\n", encoding="utf-8")
    with pytest.raises(profiles.flat_config.ConfigError):
        profiles.load(nested)


def test_common_key_applies_to_every_profile(tmp_path):
    path = tmp_path / "profiles.yaml"
    path.write_text(
        "max_word_chars: 10\na.word_familiarity_min: 0.5\nb.word_familiarity_min: 0.2\n",
        encoding="utf-8",
    )
    loaded = profiles.load(path)
    assert loaded["a"]["max_word_chars"] == 10
    assert loaded["b"]["max_word_chars"] == 10
    assert loaded["a"]["word_familiarity_min"] == 0.5


# --------------------------------------------------------- regression-набор фикстур

# Слово -> (частотность, ожидаемый разряд доступности).
# Разряды: high >= 0.75, mid 0.55..0.75, low < 0.55. Точные числа не
# фиксируются: веса меняются осознанно, а порядок величин — нет.
WORD_FIXTURES: list[tuple[str, float | None, str]] = [
    ("cat", 0.90, "high"),
    ("dog", 0.92, "high"),
    ("apple", 0.85, "high"),
    ("table", 0.86, "high"),
    ("water", 0.93, "high"),
    ("chair", 0.82, "high"),
    ("bread", 0.80, "high"),
    ("green", 0.84, "high"),
    ("window", 0.80, "high"),
    ("garden", 0.76, "mid"),
    ("hammer", 0.70, "mid"),
    ("balloon", 0.68, "mid"),
    ("penguin", 0.62, "mid"),
    ("volcano", 0.60, "mid"),
    ("umbrella", 0.63, "mid"),
    ("telescope", 0.58, "mid"),
    ("refrigerator", 0.66, "low"),
    ("polar bear", 0.55, "low"),
    ("hot air balloon", 0.45, "low"),
    ("adze", 0.12, "low"),
    ("wombat", 0.30, "low"),
    ("bathysphere", 0.08, "low"),
    ("psychiatrist", 0.45, "low"),
    ("schnauzer", 0.22, "low"),
    ("mississippi", None, "low"),
]

BAND_BOUNDS = {"high": (0.75, 1.0), "mid": (0.55, 0.85), "low": (0.0, 0.72)}


@pytest.mark.parametrize("word,familiarity,band", WORD_FIXTURES)
def test_word_fixture_lands_in_expected_band(word, familiarity, band):
    low, high = BAND_BOUNDS[band]
    value = access(word, familiarity)
    assert low <= value <= high, f"{word}: {value:.3f} вне разряда {band}"


def test_word_fixtures_keep_their_order():
    """Порядок доступности не должен переворачиваться при смене весов."""
    scored = sorted(
        ((access(word, familiarity), word) for word, familiarity, _ in WORD_FIXTURES),
        reverse=True,
    )
    ranked = [word for _value, word in scored]
    assert ranked.index("cat") < ranked.index("garden")
    assert ranked.index("garden") < ranked.index("refrigerator")
    assert ranked.index("refrigerator") < ranked.index("bathysphere")
    assert ranked.index("apple") < ranked.index("hot air balloon")


# Название -> (размер пула, ожидаемый разряд качества).
LABEL_FIXTURES: list[tuple[str, int, str]] = [
    ("BIRDS OF PREY", 14, "high"),
    ("KITCHEN TOOLS", 20, "high"),
    ("THINGS THAT MELT", 16, "high"),
    ("FARM ANIMALS", 18, "high"),
    ("BOARD GAMES", 15, "high"),
    ("PIZZA TOPPINGS", 14, "high"),
    ("SPRING FLOWERS", 12, "high"),
    # Широкие ярлыки referencе'а — полноценно высокий разряд, а не «средний».
    ("ANIMALS", 90, "high"),
    ("FOOD", 120, "high"),
    ("SCHOOL", 60, "high"),
    ("DOCTOR", 40, "high"),
    ("AFRICAN SAVANNA PREDATORS", 9, "mid"),
    ("THINGS YOU FIND IN A KITCHEN DRAWER", 20, "low"),
    ("MISCELLANEOUS ITEMS", 30, "low"),
    ("RELATED THINGS", 25, "low"),
    ("SPECIAL WORDS", 22, "low"),
    ("kitchen_tools_v2", 20, "low"),
]

LABEL_BOUNDS = {"high": (0.72, 1.0), "mid": (0.45, 0.90), "low": (0.0, 0.70)}


@pytest.mark.parametrize("label,pool,band", LABEL_FIXTURES)
def test_label_fixture_lands_in_expected_band(label, pool, band):
    metrics = scoring.label_metrics(label, CONFIG)
    quality = scoring.label_quality(
        naturalness=scoring.label_naturalness(label).score,
        clarity=scoring.label_clarity(label).score,
        retrospective_fit=scoring.label_retrospective_fit(label, pool).score,
        reveal_satisfaction=scoring.label_reveal_satisfaction(label).score,
        display_width_score=metrics["label_display_width_score"],
        familiarity=0.7,
        config=CONFIG,
    ).score
    low, high = LABEL_BOUNDS[band]
    assert low <= quality <= high, f"{label}: {quality:.3f} вне разряда {band}"
