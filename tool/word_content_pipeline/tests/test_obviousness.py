"""Ранжирование очевидности внутри категории.

Что здесь важно проверить, помимо «работает». Шаг существует ровно потому, что
предыдущий источник залил очевидность одним числом на всю категорию. Значит
главная опасность — тихо заменить одну заливку другой: модель вернёт снова
плоский ответ, шаг его запишет, и отличить «оценено» от «не оценено» станет
невозможно. Поэтому отсутствие разброса обязано быть отказом, а не записью.
"""

from __future__ import annotations

import sqlite3

import pytest

from word_content import obviousness
from word_content.llm.mock import MockLLMProvider
from word_content.migrations import migrate


@pytest.fixture
def graded_db(seeded: sqlite3.Connection) -> sqlite3.Connection:
    """Сид + колонки шага 009 + плоская категория, достаточно большая для оценки."""
    migrate(seeded)
    category_id = seeded.execute(
        "SELECT id FROM categories WHERE category_key = 'fruits'"
    ).fetchone()["id"]
    # Пул сида мал для MIN_POOL — добираем словами с одинаковой очевидностью,
    # то есть воспроизводим ровно ту заливку, ради которой шаг и написан.
    for word in ("pear", "plum", "grape", "lemon", "mango"):
        cur = seeded.execute(
            "INSERT INTO words (text, normalized, part_of_speech, is_proper_noun, "
            "created_at, updated_at) VALUES (?, ?, 'noun', 0, '2026-08-02', '2026-08-02')",
            (word, word),
        )
        seeded.execute(
            "INSERT INTO memberships (word_id, category_id, relation_type, reason, "
            "fit_score, obviousness_score, source, review_status, semantic_status, "
            "created_at, updated_at) VALUES (?, ?, 'is_a', ?, 0.95, 0.8, 'seed_manual', "
            "'approved', 'correct', '2026-08-02', '2026-08-02')",
            (cur.lastrowid, category_id, f"{word} is a fruit"),
        )
    # apple в сиде стоит на 1.0 — сделаем категорию честно плоской
    seeded.execute(
        "UPDATE memberships SET obviousness_score = 0.8 WHERE category_id = ?",
        (category_id,),
    )
    seeded.commit()
    return seeded


def response(*pairs: tuple[str, float]) -> dict:
    return {
        "category_key": "fruits",
        "grades": [
            {"word": word, "obviousness_score": score, "reason": f"{word}: причина"}
            for word, score in pairs
        ],
    }


SPREAD = (("apple", 1.0), ("pear", 0.9), ("plum", 0.8), ("grape", 0.75),
          ("lemon", 0.7), ("mango", 0.55))


def test_flat_category_lands_in_queue(graded_db):
    queue = obviousness.targets(graded_db, readiness=())
    keys = [t.category_key for t in queue]
    assert "fruits" in keys, "категория с одним значением на весь пул обязана попасть в очередь"
    target = queue[keys.index("fruits")]
    assert target.flat_value == 0.8
    assert target.pool >= obviousness.MIN_POOL


def test_single_alternative_does_not_hide_a_flat_core(graded_db):
    """Одна связь чужого статуса не имеет права закрыть вопрос за весь блок.

    Реальный случай: у BODIES OF WATER двадцать три approved-слова стояли ровно
    на 0.88 — плоско настолько, насколько бывает, — но одна `alternative`-связь
    на 0.55 растягивала общий размах до 0.33, и категория не попадала в очередь.
    В уровни при этом едет именно approved-блок, то есть заливка так и осталась
    бы работать, а сводка показывала бы «очередь пуста».
    """
    category_id = graded_db.execute(
        "SELECT id FROM categories WHERE category_key = 'fruits'"
    ).fetchone()["id"]
    cur = graded_db.execute(
        "INSERT INTO words (text, normalized, part_of_speech, is_proper_noun, "
        "created_at, updated_at) VALUES ('quince', 'quince', 'noun', 0, "
        "'2026-08-02', '2026-08-02')"
    )
    graded_db.execute(
        "INSERT INTO memberships (word_id, category_id, relation_type, reason, "
        "fit_score, obviousness_score, source, review_status, semantic_status, "
        "created_at, updated_at) VALUES (?, ?, 'is_a', 'редкий фрукт', 0.9, 0.4, "
        "'seed_manual', 'alternative', 'correct', '2026-08-02', '2026-08-02')",
        (cur.lastrowid, category_id),
    )
    graded_db.commit()

    keys = [t.category_key for t in obviousness.targets(graded_db, readiness=())]
    assert "fruits" in keys, "выброс из alternative не должен прятать плоский approved-блок"


def test_graded_category_leaves_queue(graded_db):
    obviousness.grade(graded_db, MockLLMProvider([response(*SPREAD)]),
                      readiness=(), apply=True)
    keys = [t.category_key for t in obviousness.targets(graded_db, readiness=())]
    assert "fruits" not in keys, "уже отранжированная категория не должна возвращаться в очередь"


def test_apply_writes_only_graded_column(graded_db):
    result = obviousness.grade(graded_db, MockLLMProvider([response(*SPREAD)]),
                               readiness=(), apply=True)
    assert result.graded_categories == 1
    assert result.graded_memberships == len(SPREAD)

    rows = graded_db.execute(
        "SELECT w.text, m.obviousness_score, m.graded_obviousness, m.graded_obviousness_version "
        "FROM memberships m JOIN words w ON w.id = m.word_id "
        "JOIN categories c ON c.id = m.category_id WHERE c.category_key = 'fruits'"
    ).fetchall()
    by_word = {r["text"]: r for r in rows}
    assert by_word["apple"]["graded_obviousness"] == 1.0
    assert by_word["mango"]["graded_obviousness"] == 0.55
    # исходное значение обязано уцелеть: пересчёт должен оставаться обратимым
    assert {r["obviousness_score"] for r in rows} == {0.8}
    assert by_word["apple"]["graded_obviousness_version"] == obviousness.MODEL_VERSION


def test_dry_run_changes_nothing(graded_db):
    result = obviousness.grade(graded_db, MockLLMProvider([response(*SPREAD)]),
                               readiness=(), apply=False)
    assert result.graded_categories == 1, "сухой прогон обязан посчитать результат"
    written = graded_db.execute(
        "SELECT COUNT(*) n FROM memberships WHERE graded_obviousness IS NOT NULL"
    ).fetchone()["n"]
    assert written == 0, "без --apply в базу не должно уйти ни одной строки"


def test_flat_answer_is_rejected(graded_db):
    """Плоский ответ модели — невыполненная работа, а не результат."""
    flat = response(*[(word, 0.8) for word, _ in SPREAD])
    result = obviousness.grade(graded_db, MockLLMProvider([flat]), readiness=(), apply=True)

    assert result.graded_categories == 0
    assert result.batches_failed == 1
    assert [s["reason"] for s in result.skipped] == ["no_spread"]
    written = graded_db.execute(
        "SELECT COUNT(*) n FROM memberships WHERE graded_obviousness IS NOT NULL"
    ).fetchone()["n"]
    assert written == 0


def test_unknown_word_is_dropped_not_written(graded_db):
    """Слово, которого в запросе не было, в базу не попадает."""
    payload = response(*SPREAD, ("durian", 0.2))
    result = obviousness.grade(graded_db, MockLLMProvider([payload]), readiness=(), apply=True)

    assert result.graded_memberships == len(SPREAD)
    assert any(s["reason"] == "unknown_word" for s in result.skipped)
    assert graded_db.execute(
        "SELECT COUNT(*) n FROM words WHERE text = 'durian'"
    ).fetchone()["n"] == 0


def test_broken_json_fails_the_category_not_the_run(graded_db):
    result = obviousness.grade(graded_db, MockLLMProvider(["не json вовсе"]),
                               readiness=(), apply=True)
    assert result.batches_failed == 1
    assert result.graded_categories == 0
    assert [s["reason"] for s in result.skipped] == ["batch_failed"]
