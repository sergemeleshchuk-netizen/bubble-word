"""Тесты ранжирования пула категории.

Ранжирование существует ради одного обещания: у широкой категории всегда есть
и лёгкая четвёрка, и трудная, и лёгкая собрана из более расхожих слов. Всё
остальное здесь — защита от способов это обещание потерять: недетерминированный
порядок при равной популярности, тир, которого нет в собственном наборе, и
ранжирование категории, где выбирать не из чего.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from word_content import migrations, pool_rank
from word_content.db import connect, init_db, utc_now


def _db(tmp_path: Path) -> sqlite3.Connection:
    path = tmp_path / "content.sqlite"
    init_db(path)                       # создаёт скелет и докатывает все миграции
    return connect(path)


def _category(conn: sqlite3.Connection, key: str) -> int:
    now = utc_now()
    cur = conn.execute(
        "INSERT INTO categories (category_key, label, rule, relation_type, theme, "
        "created_at, updated_at) VALUES (?, ?, ?, 'is_a', 'test', ?, ?)",
        (key, key.upper(), f"rule for {key}", now, now),
    )
    return int(cur.lastrowid)


def _word(conn: sqlite3.Connection, text: str, familiarity: float | None) -> int:
    now = utc_now()
    cur = conn.execute(
        "INSERT INTO words (text, normalized, familiarity_score, created_at, updated_at) "
        "VALUES (?, ?, ?, ?, ?)",
        (text, text.lower(), familiarity, now, now),
    )
    return int(cur.lastrowid)


def _member(conn: sqlite3.Connection, word: int, category: int,
            status: str = "approved") -> None:
    now = utc_now()
    conn.execute(
        "INSERT INTO memberships (word_id, category_id, relation_type, reason, "
        "fit_score, obviousness_score, source, review_status, created_at, updated_at) "
        "VALUES (?, ?, 'is_a', 'test', 1.0, 0.8, 'test', ?, ?, ?)",
        (word, category, status, now, now),
    )


def _quartet(conn: sqlite3.Connection, category: int, words: list[int], key: str) -> int:
    now = utc_now()
    cur = conn.execute(
        "INSERT INTO quartets (category_id, quartet_key, tier, validation_state, "
        "local_check, created_at, updated_at) "
        "VALUES (?, ?, 'normal', 'auto_validated', 'local_unique', ?, ?)",
        (category, key, now, now),
    )
    quartet_id = int(cur.lastrowid)
    for slot, word in enumerate(words, start=1):
        conn.execute(
            "INSERT INTO quartet_words (quartet_id, word_id, slot, created_at) "
            "VALUES (?, ?, ?, ?)", (quartet_id, word, slot, now))
    return quartet_id


@pytest.fixture()
def wide(tmp_path: Path) -> tuple[sqlite3.Connection, int, dict[str, int]]:
    """Категория из восьми слов: популярность убывает ровно по алфавиту a…h."""
    conn = _db(tmp_path)
    category = _category(conn, "wide")
    words = {}
    for index, letter in enumerate("abcdefgh"):
        word = _word(conn, letter, 0.9 - index * 0.1)
        _member(conn, word, category)
        words[letter] = word
    conn.commit()
    return conn, category, words


def test_ранг_слова_идёт_от_самого_популярного(wide) -> None:
    conn, category, words = wide
    pool_rank.rank(conn)
    rows = dict(conn.execute(
        "SELECT w.text, m.pool_rank FROM memberships m JOIN words w ON w.id = m.word_id "
        "WHERE m.category_id = ?", (category,)))
    assert rows["a"] == 1, "самое популярное слово стоит первым"
    assert rows["h"] == 8, "самое редкое — последним"
    assert [rows[letter] for letter in "abcdefgh"] == list(range(1, 9))


def test_пул_до_четырёх_слов_не_ранжируется(tmp_path: Path) -> None:
    """Категория ровно из четырёх слов даёт одну четвёрку — выбирать не из чего."""
    conn = _db(tmp_path)
    category = _category(conn, "narrow")
    words = []
    for index, letter in enumerate("abcd"):
        word = _word(conn, letter, 0.9 - index * 0.1)
        _member(conn, word, category)
        words.append(word)
    quartet = _quartet(conn, category, words, "narrow:abcd")
    conn.commit()

    pool_rank.rank(conn)
    row = conn.execute(
        "SELECT difficulty_tier, pool_position, pool_tiers FROM quartets WHERE id = ?",
        (quartet,)).fetchone()
    assert row["difficulty_tier"] == pool_rank.UNRANKED
    assert row["pool_position"] is None
    assert row["pool_tiers"] is None
    ranks = [r[0] for r in conn.execute(
        "SELECT pool_rank FROM memberships WHERE category_id = ?", (category,))]
    assert ranks == [None] * 4, "слова узкого пула места не получают"


def test_лёгкая_четвёрка_популярнее_трудной(wide) -> None:
    conn, category, words = wide
    easy = _quartet(conn, category, [words[x] for x in "abcd"], "wide:abcd")
    middle = _quartet(conn, category, [words[x] for x in "bcdf"], "wide:bcdf")
    hard = _quartet(conn, category, [words[x] for x in "efgh"], "wide:efgh")
    conn.commit()

    pool_rank.rank(conn)
    tiers = dict(conn.execute("SELECT id, difficulty_tier FROM quartets"))
    assert tiers[easy] == "easy"
    assert tiers[hard] == "hard"
    avg = dict(conn.execute("SELECT id, pool_rank_avg FROM quartets"))
    assert avg[easy] < avg[middle] < avg[hard], "средний ранг растёт от лёгкой к трудной"


def test_первичный_тир_всегда_входит_в_свой_набор(wide) -> None:
    """Иначе выгрузка и человек читали бы про одну четвёрку разное."""
    conn, category, words = wide
    letters = ["abcd", "abce", "abcf", "abcg", "abch", "bcde", "cdef", "defg", "efgh"]
    for combo in letters:
        _quartet(conn, category, [words[x] for x in combo], f"wide:{combo}")
    conn.commit()

    pool_rank.rank(conn)
    for row in conn.execute(
            "SELECT difficulty_tier, pool_tiers FROM quartets WHERE pool_tiers IS NOT NULL"):
        assert row["difficulty_tier"] in row["pool_tiers"].split(",")


def test_пересчёт_идемпотентен(wide) -> None:
    """Порядок при равной популярности задан явно, иначе каждый прогон тасовал бы тиры."""
    conn, category, words = wide
    # два слова с ОДИНАКОВОЙ популярностью: развязка обязана быть детерминированной
    same = _word(conn, "aa", 0.9)
    _member(conn, same, category)
    for combo in ("abcd", "bcde", "cdef", "defg"):
        _quartet(conn, category, [words[x] for x in combo], f"wide:{combo}")
    conn.commit()

    pool_rank.rank(conn)
    first = sorted(tuple(row) for row in conn.execute(
        "SELECT id, difficulty_tier, pool_position FROM quartets"))
    pool_rank.rank(conn)
    second = sorted(tuple(row) for row in conn.execute(
        "SELECT id, difficulty_tier, pool_position FROM quartets"))
    assert first == second


def test_слово_вне_approved_пула_считается_самым_редким(wide) -> None:
    """`alternative` и `hard_only` в пул отбора не входят — поблажки им нет."""
    conn, category, words = wide
    outsider = _word(conn, "z", 0.95)          # популярнее всех, но статус не approved
    _member(conn, outsider, category, status="alternative")
    plain = _quartet(conn, category, [words[x] for x in "abcd"], "wide:abcd")
    withalt = _quartet(conn, category, [words["a"], words["b"], words["c"], outsider],
                       "wide:abc+z")
    conn.commit()

    pool_rank.rank(conn)
    avg = dict(conn.execute("SELECT id, pool_rank_avg FROM quartets"))
    assert avg[withalt] > avg[plain]
