"""Тесты на исправления по внешнему аудиту базы (31.07.2026).

Каждый тест закрывает конкретное замечание, чтобы регресс был виден сразу.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from word_content import conflicts, integrity, readiness, sense_gaps, solver
from word_content.importers import import_memberships, import_review_csv
from word_content.models import CategoryConflictInput, QuartetInput, familiarity_gate
from word_content.readiness import CategoryPools, classify
from word_content.repositories import (
    clear_category_conflicts,
    conflicting_categories,
    replace_pair_groups,
    upsert_category_conflict,
    upsert_quartet,
)

from conftest import write_jsonl

# ------------------------------------------------------ P0: гейт частотности


def test_familiarity_gate_closes_playable_statuses():
    """Нет частотности — играбельный статус запрещён, а candidate/rejected не трогаем."""
    for status in ("approved", "alternative", "hard_only"):
        result, reason = familiarity_gate(status, None)
        assert result == "candidate"
        assert reason and status in reason
    assert familiarity_gate("rejected", None) == ("rejected", None)
    assert familiarity_gate("candidate", None) == ("candidate", None)
    assert familiarity_gate("approved", 0.5) == ("approved", None)


def test_import_downgrades_approved_without_familiarity(conn, categories_file, tmp_path):
    """calfling приходил в базу как approved — так больше нельзя."""
    from word_content.importers import import_categories

    import_categories(conn, categories_file)
    path = write_jsonl(
        tmp_path / "no_familiarity.jsonl",
        [
            {
                "word": "zzqxrblorp",  # выдуманное слово: wordfreq его не знает
                "category_key": "fruits",
                "relation_type": "is_a",
                "reason": "Zzqxrblorp is a common edible fruit",
                "fit_score": 0.97,
                "obviousness_score": 0.9,
                "review_status": "approved",
            }
        ],
    )
    import_memberships(conn, path)

    row = conn.execute(
        "SELECT m.review_status st, m.risk_flags flags, w.familiarity_score fam "
        "FROM memberships m JOIN words w ON w.id = m.word_id"
    ).fetchone()
    assert row["fam"] is None
    assert row["st"] == "candidate"
    assert "no_familiarity" in row["flags"]


def test_review_csv_cannot_approve_without_familiarity(conn, categories_file, tmp_path):
    """Гейт работает и на слое решений reviewer, а не только на импорте связей."""
    from word_content.importers import import_categories

    import_categories(conn, categories_file)
    import_memberships(
        conn,
        write_jsonl(
            tmp_path / "m.jsonl",
            [
                {
                    "word": "zzqxrblorp",
                    "category_key": "fruits",
                    "relation_type": "is_a",
                    "reason": "Zzqxrblorp is a common edible fruit",
                    "fit_score": 0.97,
                    "obviousness_score": 0.9,
                }
            ],
        ),
    )
    csv_path = tmp_path / "decisions.csv"
    csv_path.write_text(
        "membership_id,word,normalized,category_key,decision,review_comment\n"
        ",zzqxrblorp,zzqxrblorp,fruits,approved,вручную\n",
        encoding="utf-8",
    )
    import_review_csv(conn, csv_path)

    row = conn.execute("SELECT review_status st, review_comment c FROM memberships").fetchone()
    assert row["st"] == "candidate"
    assert "частотность" in row["c"]


def test_integrity_check_catches_familiarity_violation(seeded):
    """Проверка ловит нарушение, если оно всё-таки попало в базу напрямую."""
    seeded.execute("UPDATE words SET familiarity_score = NULL")
    seeded.execute("UPDATE memberships SET review_status = 'approved'")
    result = integrity.check_familiarity_gate(seeded)
    assert not result.ok
    assert result.severity == "blocker"


# ------------------------------------------------- P0: значения многозначных слов


def test_sense_assignment_check_finds_null_sense(seeded, tmp_path):
    """Слово с двумя значениями и связью без значения — блокирующая ошибка."""
    assert integrity.check_sense_assignment(seeded).ok

    import_memberships(
        seeded,
        write_jsonl(
            tmp_path / "extra.jsonl",
            [
                {
                    "word": "apple",  # у apple уже два значения
                    "category_key": "town_places",
                    "relation_type": "found_in",
                    "reason": "Apple is found in a town",
                    "fit_score": 0.9,
                    "obviousness_score": 0.6,
                    "review_status": "alternative",
                }
            ],
        ),
    )
    result = integrity.check_sense_assignment(seeded)
    assert not result.ok
    assert "apple" in result.examples[0]


def test_wordplay_relations_are_exempt_from_sense_rule(seeded, tmp_path):
    """'starboard' не происходит от звезды: у категорий игры слов значения нет осознанно."""
    from word_content.importers import import_categories

    import_categories(
        seeded,
        write_jsonl(
            tmp_path / "cats.jsonl",
            [
                {
                    "category_key": "words_before_sauce",
                    "label": "___ SAUCE",
                    "rule": "Words that form a familiar compound before the word sauce",
                    "relation_type": "phrase_before",
                    "theme": "language",
                    "base_difficulty": 0.5,
                }
            ],
        ),
    )
    import_memberships(
        seeded,
        write_jsonl(
            tmp_path / "wordplay.jsonl",
            [
                {
                    "word": "apple",
                    "category_key": "words_before_sauce",
                    "relation_type": "phrase_before",
                    "reason": "apple forms the familiar compound apple sauce",
                    "fit_score": 0.98,
                    "obviousness_score": 0.6,
                    "review_status": "alternative",
                }
            ],
        ),
    )
    assert integrity.check_sense_assignment(seeded).ok
    exemption = integrity.check_wordplay_sense_exemption(seeded)
    assert exemption.count == 1
    assert exemption.severity == "info"


# ------------------------------------------------------------- P0: readiness


@pytest.mark.parametrize(
    "approved, alternative, hard, expected",
    [
        (8, 6, 2, "ready"),
        (2, 6, 2, "constrained"),  # approved меньше четырёх
        (6, 2, 12, "constrained"),  # перевес hard_only
        (1, 2, 9, "hard_only"),  # нормальную четвёрку не собрать
        (0, 1, 2, "blocked"),  # четвёрку не собрать вообще
    ],
)
def test_readiness_classification(approved, alternative, hard, expected):
    pools = CategoryPools("k", "LABEL", approved, alternative, hard, 0)
    assert classify(pools, {})[0] == expected


def test_curated_only_override_wins():
    pools = CategoryPools("opposites", "OPPOSITES", 20, 6, 0, 0)
    result, reason = classify(pools, {"opposites": "правило парное"})
    assert result == "curated_only"
    assert reason == "правило парное"


def test_derive_readiness_disables_blocked_category(seeded):
    """Категория, из которой четвёрку не собрать, отключается (status=disabled)."""
    summary = readiness.derive(seeded, {})
    assert summary  # что-то посчитали
    blocked = list(
        seeded.execute("SELECT status FROM categories WHERE readiness = 'blocked'")
    )
    assert blocked, "в фикстуре пулы по 1-2 слова, значит blocked обязан быть"
    assert all(row["status"] == "disabled" for row in blocked)
    assert integrity.check_readiness_derived(seeded).ok
    assert integrity.check_normal_quartet_capability(seeded).ok


# --------------------------------------------------- P0/P1: конфликты категорий


def test_overlap_detection_finds_shared_pool(seeded):
    """apple лежит и в FRUITS, и в PIE INGREDIENTS — при пороге 1 это конфликт."""
    overlaps = conflicts.find_overlaps(seeded, min_overlap=1)
    pairs = {(o.category_a, o.category_b) for o in overlaps}
    assert ("fruits", "pie_ingredients") in pairs


def test_conflict_pair_stored_once_in_any_order(seeded):
    clear_category_conflicts(seeded)
    upsert_category_conflict(
        seeded,
        CategoryConflictInput(category_a="pie_ingredients", category_b="fruits", overlap_count=4),
    )
    upsert_category_conflict(
        seeded,
        CategoryConflictInput(category_a="fruits", category_b="pie_ingredients", overlap_count=5),
    )
    rows = list(seeded.execute("SELECT overlap_count FROM category_conflicts"))
    assert len(rows) == 1, "порядок категорий в паре не должен создавать вторую запись"
    assert rows[0]["overlap_count"] == 5
    assert conflicting_categories(seeded, "fruits") == {"pie_ingredients"}


def test_conflict_rejects_self_pair():
    with pytest.raises(ValueError):
        CategoryConflictInput(category_a="fruits", category_b="fruits")


# ---------------------------------------------------------------- P1: solver


def _pools(**kwargs) -> dict[str, set[str]]:
    return {key: set(words) for key, words in kwargs.items()}


def test_solver_accepts_single_partition():
    pools = _pools(
        seasons=["spring", "summer", "fall", "winter"],
        instruments=["guitar", "piano", "drum", "flute"],
    )
    result = solver.solve(
        ["spring", "summer", "fall", "winter", "guitar", "piano", "drum", "flute"], pools
    )
    assert result.unique
    assert result.solution_count == 1


def test_solver_rejects_overlapping_categories():
    """JEWELRY STONES и GEMSTONES делят пул — у уровня появляется второй ответ."""
    stones = ["diamond", "ruby", "opal", "topaz", "jade", "onyx", "pearl", "garnet"]
    pools = _pools(gemstones=stones, jewelry_stones=stones)
    result = solver.solve(stones, pools)
    assert not result.unique
    assert result.solution_count >= 2


def test_solver_uses_each_category_once():
    """Две четвёрки одной категории — это не разбиение уровня, а один ответ дважды."""
    stones = ["diamond", "ruby", "opal", "topaz", "jade", "onyx", "pearl", "garnet"]
    result = solver.solve(stones, _pools(gemstones=stones))
    assert not result.unique
    assert result.solution_count == 0
    assert "не раскладывается" in result.reason


def test_solver_rejects_duplicate_and_wrong_size():
    pools = _pools(seasons=["spring", "summer", "fall", "winter"])
    assert not solver.solve(["spring", "spring", "fall", "winter"], pools).unique
    assert "повторяющиеся" in solver.solve(["spring", "spring", "fall", "winter"], pools).reason
    assert "не делится" in solver.solve(["spring", "fall", "winter"], pools).reason


def test_quartet_locally_unique_detects_second_owner(seeded):
    pools = _pools(
        gemstones=["diamond", "ruby", "opal", "topaz"],
        jewelry_stones=["diamond", "ruby", "opal", "topaz", "jade"],
    )
    good = solver.quartet_locally_unique(
        seeded, "jewelry_stones", ["diamond", "ruby", "opal", "jade"], pools=pools
    )
    assert good.unique
    bad = solver.quartet_locally_unique(
        seeded, "gemstones", ["diamond", "ruby", "opal", "topaz"], pools=pools
    )
    assert not bad.unique
    assert "jewelry_stones" in bad.reason


def test_solver_pool_excludes_semantically_incorrect(seeded):
    before = solver.category_pools(seeded)
    assert "apple" in before["fruits"]
    seeded.execute("UPDATE memberships SET semantic_status = 'incorrect'")
    after = solver.category_pools(seeded)
    assert not after


# -------------------------------------------------------------- P1: четвёрки


def test_quartet_requires_exactly_four_distinct_words():
    base = {"quartet_key": "k", "category_key": "fruits"}
    with pytest.raises(ValueError):
        QuartetInput(**base, words="apple | pear | plum")
    with pytest.raises(ValueError):
        QuartetInput(**base, words="apple | apple | pear | plum")
    item = QuartetInput(**base, words="apple | pear | plum | fig")
    assert [word for word, _ in item.word_items] == ["apple", "pear", "plum", "fig"]


def test_quartet_word_can_pin_a_sense():
    item = QuartetInput(
        quartet_key="fruits__1",
        category_key="fruits",
        words="apple#apple_fruit | pear | plum | fig",
    )
    assert item.word_items[0] == ("apple", "apple_fruit")
    assert item.word_items[1] == ("pear", None)

    # Одно слово дважды запрещено даже с разными значениями: игрок видит один пузырь,
    # и четвёрка из двух значений одного написания решается неоднозначно.
    with pytest.raises(ValueError):
        QuartetInput(
            quartet_key="x",
            category_key="fruits",
            words="apple#apple_fruit | apple#apple_company | pear | plum",
        )


def test_quartet_upsert_rejects_unknown_sense(seeded):
    with pytest.raises(Exception):
        upsert_quartet(
            seeded,
            QuartetInput(
                quartet_key="fruits__1",
                category_key="fruits",
                words="apple#no_such_sense | bank | Apple | pear",
            ),
        )


# ------------------------------------------------- P0: очередь значений и пары


def test_sense_gaps_skips_words_that_already_have_senses(seeded):
    """apple и bank значения имеют, поэтому в очередь на разведение не попадают."""
    gaps = sense_gaps.find(seeded, min_categories=1, min_themes=1)
    assert [gap.normalized for gap in gaps] == []


def test_sense_gaps_respects_not_homonyms(tmp_path):
    path = tmp_path / "_not_homonyms.txt"
    path.write_text("turtle  # одна и та же черепаха\n\n# комментарий\nsun\n", encoding="utf-8")
    assert sense_gaps.load_not_homonyms(path) == {"turtle", "sun"}
    assert sense_gaps.load_not_homonyms(tmp_path / "missing.txt") == set()


def test_pair_groups_replace_is_idempotent(seeded):
    written, missing = replace_pair_groups(seeded, "fruits", [["apple", "bank"]])
    assert (written, missing) == (1, [])
    written, _ = replace_pair_groups(seeded, "fruits", [["apple", "bank"]])
    assert written == 1
    rows = list(seeded.execute("SELECT COUNT(*) n FROM category_pair_groups"))
    assert rows[0]["n"] == 2, "перезапись не должна дублировать пары"


def test_pair_groups_report_missing_words(seeded):
    written, missing = replace_pair_groups(seeded, "fruits", [["apple", "nosuchword"]])
    assert written == 0
    assert missing == ["nosuchword (fruits)"]


# ----------------------------------------------------------- сводная проверка


def test_run_all_returns_every_check(seeded):
    readiness.derive(seeded, {})
    results = integrity.run_all(seeded)
    assert len(results) == len(integrity.CHECKS)
    names = {result.name for result in results}
    assert "familiarity_gate" in names
    assert "sense_assignment" in names
    assert "quartets_local_check" in names
    # Пустой слой конфликтов сам по себе не ошибка: у этой фикстуры категории
    # не пересекаются, и запрещать нечего. Ошибка — когда пересечение есть,
    # а запрета нет; это проверяется отдельно.
    assert integrity.check_conflicts_present(seeded).ok


def test_conflicts_check_catches_unhandled_overlap(seeded, tmp_path):
    """Четыре общих слова у двух категорий без записи в слое конфликтов — блокер."""
    from word_content.importers import import_memberships

    overlap = [
        {
            "word": word,
            "category_key": category_key,
            "relation_type": "is_a",
            "reason": f"{word} в {category_key}",
            "fit_score": 0.9,
            "obviousness_score": 0.9,
            "review_status": "approved",
        }
        for word in ("plum", "peach", "quince", "apricot")
        for category_key in ("fruits", "pie_ingredients")
    ]
    import_memberships(seeded, write_jsonl(tmp_path / "overlap.jsonl", overlap))
    result = integrity.check_conflicts_present(seeded)
    assert not result.ok
    assert any("fruits" in example for example in result.examples)
