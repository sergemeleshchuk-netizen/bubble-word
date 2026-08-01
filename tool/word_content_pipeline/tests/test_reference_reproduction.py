"""Регрессия воспроизведения референса.

Двенадцать проверок из раздела 11 задания. Часть из них — чистая логика и
работает на синтетике; часть требует реальной базы, потому что проверяет именно
её содержимое. Вторые пропускаются, если базы нет: тест, который молча
превращается в «ок» без данных, хуже отсутствующего.

Главное, что здесь закреплено: пока уровни записи не воспроизводятся, генерация
нового контента обязана падать. Это единственная защита от повторения того, что
уже случилось — система научилась строить собственную модель контента, так и не
научившись повторять саму игру.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest
from typer.testing import CliRunner

from word_content import (
    composition,
    level_generator,
    meta_pairs,
    meta_validation,
    normalization,
    reference_coverage,
    reference_fixtures,
    reference_import,
)
from word_content.cli import app

runner = CliRunner()

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DB = PIPELINE_ROOT / "database/content.sqlite"

requires_db = pytest.mark.skipif(
    not PROJECT_DB.exists(),
    reason="нет собранной базы: bash scripts/rebuild_all.sh",
)


@pytest.fixture(scope="module")
def fixtures() -> reference_fixtures.ReferenceFixtures:
    return reference_fixtures.load()


@pytest.fixture(scope="module")
def overrides() -> dict:
    return reference_import.load_overrides(reference_import.default_overrides_path())


@pytest.fixture(scope="module")
def db() -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{PROJECT_DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


# ------------------------------------------------------- 1-4: точное восстановление


@requires_db
def test_1_level_1_reconstructed_exactly(db, fixtures, overrides):
    """Уровень 1 собирается из базы ровно таким, каким он записан."""
    level = fixtures.get(1)
    assert reference_import.diff_level(db, level) == []
    exported = reference_import.export_level(db, 1)
    assert [group["name"] for group in exported["groups"]] == [
        "farm animals", "colors", "vehicles", "compass", "days of the week"
    ]
    assert [slot["text"] for slot in exported["groups"][0]["slots"]] == [
        "cow", "horse", "goat", "pig"
    ]


@requires_db
def test_2_level_3_reconstructed_with_first_meta_link(db, fixtures):
    """Уровень 3 — первая мета-ссылка за всю игру, и она должна быть в базе."""
    assert reference_import.diff_level(db, fixtures.get(3)) == []
    exported = reference_import.export_level(db, 3)
    meta = exported["meta_links"]
    assert len(meta) == 1
    assert meta[0]["token"] == "school subjects"
    assert meta[0]["source_group"] == "school subjects"
    assert meta[0]["target_group"] == "school"
    assert meta[0]["form"] == "picture"
    school = next(g for g in exported["groups"] if g["name"] == "school")
    token = next(s for s in school["slots"] if s["text"] == "school subjects")
    # Результат другой категории не притворяется обычным словом.
    assert token["token_kind"] == "category_output"


@requires_db
def test_3_level_7_meta_collector(db, fixtures):
    """Уровень 7: категория measurements целиком собрана из чужих результатов."""
    assert reference_import.diff_level(db, fixtures.get(7)) == []
    exported = reference_import.export_level(db, 7)
    measurements = next(g for g in exported["groups"] if g["name"] == "measurements")
    assert all(slot["token_kind"] == "category_output" for slot in measurements["slots"])
    rule_type = db.execute(
        """
        SELECT c.rule_type FROM level_groups g
          JOIN categories c ON c.id = g.category_id
          JOIN level_instances l ON l.id = g.level_id
         WHERE l.level_key = 'REF007' AND g.reference_name = 'measurements'
        """
    ).fetchone()[0]
    assert rule_type == "meta_collector"


@requires_db
def test_4_level_10_chunks(db, fixtures):
    """Уровень 10 вводит кусочки: слово приходит по частям, и части записаны."""
    assert reference_import.diff_level(db, fixtures.get(10)) == []
    chunked = list(
        db.execute(
            """
            SELECT t.display_text AS text, t.pieces AS pieces
              FROM level_tokens t JOIN level_instances l ON l.id = t.level_id
             WHERE l.level_key = 'REF010' AND t.token_kind = 'chunked_word'
             ORDER BY t.display_text
            """
        )
    )
    assert len(chunked) == 5
    by_word = {row["text"]: json.loads(row["pieces"]) for row in chunked}
    assert by_word["elephant"] == ["ele", "phant"]
    assert by_word["sword"] == ["sw", "ord"]


# --------------------------------------------- 5-8: надписи, значения, авторский дом


@requires_db
def test_5_same_display_label_serves_different_group_rules(db):
    """MUSIC на уровне 3 — жанры, на уровне 6 — инструменты. Одна надпись, разные правила."""
    rows = list(
        db.execute(
            """
            SELECT l.level_key AS level_key, c.category_key AS rule,
                   lb.label_key AS label
              FROM level_groups g
              JOIN level_instances l  ON l.id = g.level_id
              JOIN categories c       ON c.id = g.category_id
              JOIN category_labels lb ON lb.id = g.display_label_id
             WHERE lb.label_key = 'music' AND l.level_key IN ('REF003', 'REF006')
             ORDER BY l.level_key
            """
        )
    )
    assert len(rows) == 2
    assert rows[0]["rule"] != rows[1]["rule"], "две разные четвёрки уехали в одно правило"
    assert {row["label"] for row in rows} == {"music"}
    # Обе связки надписи с правилом действительно записаны.
    for row in rows:
        assert db.execute(
            """
            SELECT 1 FROM group_rule_labels grl
              JOIN categories c       ON c.id = grl.category_id
              JOIN category_labels lb ON lb.id = grl.label_id
             WHERE c.category_key = ? AND lb.label_key = 'music'
            """,
            (row["rule"],),
        ).fetchone()


@requires_db
def test_6_one_word_lives_in_several_memberships(db):
    """Слово имеет право принадлежать нескольким правилам: на этом держится интерес."""
    rules = [
        row[0]
        for row in db.execute(
            """
            SELECT c.category_key FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE w.normalized = 'orange'
               AND m.review_status IN ('approved', 'alternative', 'hard_only')
            """
        )
    ]
    assert len(rules) >= 2, "orange обязан быть и фруктом, и цветом"


@requires_db
def test_7_authored_home_differs_from_plausible_decoy(db):
    """У токена есть авторский дом, даже когда он подходит и соседней группе."""
    row = db.execute(
        """
        SELECT t.display_text AS token,
               home.reference_name AS home,
               rival.reference_name AS rival
          FROM level_decoys d
          JOIN level_tokens t     ON t.id = d.token_id
          JOIN level_assignments a ON a.token_id = t.id
          JOIN level_groups home  ON home.id = a.home_group_id
          JOIN level_groups rival ON rival.id = d.decoy_group_id
         LIMIT 1
        """
    ).fetchone()
    assert row is not None, "ни одной ловушки не записано — проверка бессмысленна"
    assert row["home"] != row["rival"]
    # Авторское назначение есть у каждого токена каждого уровня записи.
    missing = db.execute(
        """
        SELECT COUNT(*) FROM level_tokens t
          JOIN level_instances l ON l.id = t.level_id
         WHERE l.origin = 'reference_video'
           AND NOT EXISTS (SELECT 1 FROM level_assignments a WHERE a.token_id = t.id)
        """
    ).fetchone()[0]
    assert missing == 0


def test_8_observed_and_inferred_labels_are_not_mixed(fixtures):
    """Прочитанное имя и наша формулировка — разные вещи и разные проверки."""
    levels = fixtures.upto(10)
    observed = [g for level in levels for g in level.groups if g.observed_label]
    inferred = [g for level in levels for g in level.groups if not g.observed_label]
    assert len(observed) == 24
    assert len(inferred) == 71
    compass = fixtures.get(1).group_by_name("compass")
    assert compass.label_source == "observed"
    farm = fixtures.get(1).group_by_name("farm animals")
    assert farm.label_source == "inferred"
    # Четвёрка ground truth в обоих случаях, имя — только у observed.
    assert farm.words == ("cow", "horse", "goat", "pig")


@requires_db
def test_8b_inferred_label_resolves_without_exact_string_match(db, fixtures, overrides):
    """Наша формулировка не обязана совпадать с именем правила буквально."""
    report = reference_coverage.measure(
        db, fixtures, max_level=10, overrides=overrides
    )
    assert report.metric("inferred_label").complete
    assert report.metric("observed_label").complete
    # При этом внутренние правила у большинства групп названы иначе, чем в записи:
    # именно поэтому проверка по точной строке была бы проверкой наших догадок.
    differing = db.execute(
        """
        SELECT COUNT(*) FROM level_groups g
          JOIN categories c       ON c.id = g.category_id
          JOIN level_instances l  ON l.id = g.level_id
         WHERE l.reference_level BETWEEN 1 AND 10
           AND LOWER(c.label) <> LOWER(g.reference_name)
        """
    ).fetchone()[0]
    assert differing > 0


# ------------------------------------------------- 9-10: мета-циклы и частичная запись


def test_9_meta_cycle_is_rejected():
    """Две категории, ждущие результата друг друга, — непроходимый уровень."""
    result = meta_validation.validate(
        {
            "A": ["a1", "a2", "a3", "from_b"],
            "B": ["b1", "b2", "b3", "from_a"],
        },
        {"from_b": "B", "from_a": "A"},
    )
    assert not result.ok
    assert not result.is_dag
    assert result.cycles
    assert sorted(result.deadlocked) == ["A", "B"]
    assert any("цикл" in problem for problem in result.problems)


def test_9b_valid_meta_chain_is_accepted():
    """Нормальная цепочка проходит и получает порядок сборки."""
    result = meta_validation.validate(
        {
            "school subjects": ["science", "math", "history", "art"],
            "school": ["desk", "book", "pen", "school subjects"],
        },
        {"school subjects": "school subjects"},
    )
    assert result.ok and result.is_dag
    assert result.order == ["school subjects", "school"]
    assert result.max_depth == 2


def test_9c_deadlock_without_cycle_is_caught():
    """Токена ждут, но его никто не выпускает: цикла нет, уровень непроходим."""
    result = meta_validation.validate(
        {"A": ["a1", "a2", "a3", "ghost"]},
        {"ghost": "B"},
    )
    assert not result.ok
    assert result.orphan_tokens == ["ghost"]
    assert result.deadlocked == ["A"]


@requires_db
def test_10_partial_level_18_is_not_declared_complete(db, fixtures, overrides):
    """Четыре не попавшие в кадр группы уровня 18 нельзя считать восстановленными."""
    level = fixtures.get(18)
    assert level.completeness == "partial"
    assert len(level.groups) == 7
    assert level.groups_expected == 11

    row = db.execute(
        "SELECT recorded_completeness, groups_expected FROM level_instances "
        " WHERE level_key = 'REF018'"
    ).fetchone()
    assert row["recorded_completeness"] == "partial"
    assert row["groups_expected"] == 11
    assert db.execute(
        "SELECT COUNT(*) FROM level_groups g JOIN level_instances l ON l.id = g.level_id "
        " WHERE l.level_key = 'REF018'"
    ).fetchone()[0] == 7

    report = reference_coverage.measure(db, fixtures, overrides=overrides)
    eighteen = next(item for item in report.levels if item.level == 18)
    assert not eighteen.reconstructable, "частичная запись не может быть «воспроизведена»"
    others = [item for item in report.levels if item.level != 18]
    assert all(item.reconstructable for item in others)


@requires_db
def test_10b_unseen_slots_are_not_passed_off_as_observed(db):
    """Пузырь, не попавший в кадр, помечен unseen и наблюдением не считается."""
    unseen = list(
        db.execute(
            "SELECT display_text FROM level_tokens WHERE observability = 'unseen' "
            " ORDER BY display_text"
        )
    )
    assert [row[0] for row in unseen] == ["grains", "guitar", "peat", "planets"]


# ----------------------------------------- 11-12: детерминизм сборки и барьер генерации


@requires_db
def test_11_clean_rebuild_gives_the_same_reference_export(tmp_path, fixtures, overrides):
    """Экспорт уровней записи детерминирован: повторный импорт даёт то же самое."""
    import shutil

    from word_content.db import connect

    copy = tmp_path / "content.sqlite"
    shutil.copy(PROJECT_DB, copy)
    before = {
        number: reference_import.export_level(sqlite3_ro(copy), number)
        for number in range(1, 21)
    }
    conn = connect(copy)
    try:
        with conn:
            reference_import.import_levels(conn, fixtures, overrides=overrides)
    finally:
        conn.close()
    after = {
        number: reference_import.export_level(sqlite3_ro(copy), number)
        for number in range(1, 21)
    }
    assert before == after


def sqlite3_ro(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def test_12_generation_is_disabled_when_reference_gate_fails(tmp_path):
    """Массовая генерация обязана падать, пока референс не воспроизводится.

    Это и есть смена центра системы: способность создавать «лучше» не
    подтверждена, пока не доказана способность повторить известное.
    """
    db = tmp_path / "empty.sqlite"
    assert runner.invoke(app, ["init-db", "--db", str(db)]).exit_code == 0
    result = runner.invoke(
        app,
        ["generate-level-candidates", "--db", str(db), "--limit", "1", "--categories", "3"],
    )
    assert result.exit_code == 1
    assert "Reference Reproduction Gate не пройден" in result.output

    # С явным флагом отладки команда работает: барьер снимается осознанно,
    # а не обходится молча.
    bypass = runner.invoke(
        app,
        [
            "generate-level-candidates", "--db", str(db), "--limit", "1",
            "--categories", "3", "--skip-reference-gate",
        ],
    )
    assert bypass.exit_code == 0


@requires_db
def test_12b_gate_passes_on_the_built_base(db, fixtures, overrides):
    """Definition of Done уровней 1-10 целиком."""
    result = reference_coverage.gate(db, fixtures, max_level=10, overrides=overrides)
    assert result.passed, result.failures()
    summary = result.report.summary()
    assert summary["fully_reconstructable_reference_levels"] == 10
    assert summary["normalized_export_diff"] == 0
    counts = {name: (m.done, m.total) for name, m in result.report.metrics.items()}
    assert counts["word_slot"] == (380, 380)
    assert counts["group_rule"] == (95, 95)
    assert counts["exact_quartet"] == (95, 95)
    assert counts["slot_membership"] == (380, 380)
    assert counts["meta_dependency"] == (17, 17)
    assert counts["observed_label"] == (24, 24)
    assert counts["form_match"] == (380, 380)


# ------------------------------------------------- 13-18: мета-механика в генерации
#
# Запись оригинала вводит мета на третьем уровне и держит её в 17 уровнях из 20.
# Генератор до этой работы выдавал ровно ноль мета-связей — уровни были плоские
# при формально верном solver'е. Проверки ниже закрывают именно этот разрыв.

GENERATED_SEED = 11
GENERATED_CATEGORIES = 8
GENERATED_COUNT = 6


@pytest.fixture(scope="module")
def generated(db) -> list:
    """Один прогон генератора на всю группу тестов: он не бесплатный."""
    levels, _stats = level_generator.generate(
        db,
        count=GENERATED_COUNT,
        category_count=GENERATED_CATEGORIES,
        seed=GENERATED_SEED,
    )
    return levels


@requires_db
def test_13_meta_pairs_never_borrow_reference_content(db):
    """Мета-пары собираются только из своего: чужие правила, четвёрки и надписи.

    Надпись оригинала («compass», «doctor», «clothes»), привязанная к нашему
    правилу при разборе видео, дала бы втрое больше пар — 451 против 162.
    Это и есть цена честности, и платить её обязательно: имя группы на экране
    было бы авторским текстом записи.
    """
    index = meta_pairs.load(db)
    assert len(index) > 0, "мета-пар нет — генератору нечем строить мета-уровни"

    consumers = {pair.consumer_id for pair in index.pairs}
    sources = {pair.source_id for pair in index.pairs}
    borrowed = list(
        db.execute(
            f"""
            SELECT COUNT(*) AS n FROM categories
             WHERE origin = 'reference_backfill'
               AND id IN ({','.join('?' * len(consumers | sources))})
            """,
            tuple(consumers | sources),
        )
    )[0]["n"]
    assert borrowed == 0

    label_ids = {pair.source_label_id for pair in index.pairs}
    borrowed_labels = list(
        db.execute(
            f"""
            SELECT COUNT(*) AS n FROM category_labels
             WHERE origin = 'reference_backfill'
               AND id IN ({','.join('?' * len(label_ids))})
            """,
            tuple(label_ids),
        )
    )[0]["n"]
    assert borrowed_labels == 0

    quartet_ids = {pair.quartet_id for pair in index.pairs}
    borrowed_quartets = list(
        db.execute(
            f"""
            SELECT COUNT(*) AS n FROM quartets
             WHERE origin = 'reference_backfill'
               AND id IN ({','.join('?' * len(quartet_ids))})
            """,
            tuple(quartet_ids),
        )
    )[0]["n"]
    assert borrowed_quartets == 0


@requires_db
def test_14_meta_pair_is_a_real_word_of_a_real_quartet(db):
    """Пара — не догадка: слово стоит в четвёрке, а надпись принадлежит источнику."""
    index = meta_pairs.load(db)
    for pair in index.pairs[:200]:
        words = {
            normalization.normalize_word(row["display"])
            for row in db.execute(
                """
                SELECT COALESCE(s.display_text, w.text) AS display
                  FROM quartet_words qw
                  JOIN words w ON w.id = qw.word_id
                  LEFT JOIN word_senses s ON s.id = qw.sense_id
                 WHERE qw.quartet_id = ?
                """,
                (pair.quartet_id,),
            )
        }
        assert pair.token_norm in words
        label = db.execute(
            """
            SELECT l.display_text AS text FROM group_rule_labels grl
              JOIN category_labels l ON l.id = grl.label_id
             WHERE grl.category_id = ? AND l.id = ?
            """,
            (pair.source_id, pair.source_label_id),
        ).fetchone()
        assert label is not None
        assert normalization.normalize_word(label["text"]) == pair.token_norm


@requires_db
def test_15_generator_builds_meta_levels(generated):
    """Генератор больше не плоский: мета-связи есть и их не больше, чем просили."""
    assert len(generated) == GENERATED_COUNT
    with_meta = [level for level in generated if level.meta_links]
    assert len(with_meta) >= 3, "мета-уровней почти нет — сборка мета-ядра не работает"
    assert sum(len(level.meta_links) for level in generated) >= 4

    for level in generated:
        target = level.composition.meta_target(GENERATED_CATEGORIES)
        assert len(level.meta_links) <= target, (
            f"{level.level_key}: связей больше, чем просил профиль композиции"
        )
        # Слово внутри уровня не повторяется — правило записи без исключений.
        displays = [
            display.strip().lower()
            for group in level.groups
            for _w, _s, display, _sk, _r in group.tokens
        ]
        assert len(set(displays)) == len(displays)


@requires_db
def test_16_meta_levels_pass_both_checks(generated):
    """Уровень с мета обязан пройти и симуляцию прохождения, и оценку разбиения."""
    for level in [item for item in generated if item.meta_links]:
        assert level.meta is not None and level.meta.ok, level.meta.problems
        assert level.meta.is_dag
        assert len(level.meta.order) == len(level.groups)
        assert level.assessment is not None
        assert [reason for reason in level.reject_reasons if reason.startswith("мета")] == []
        # Токен-результат действительно принадлежит потребителю, а не источнику.
        homes = {
            display.strip().lower(): group.category_key
            for group in level.groups
            for _w, _s, display, _sk, _r in group.tokens
        }
        for link in level.meta_links:
            assert homes[link.token_display.strip().lower()] == link.consumer_key


@requires_db
def test_17_meta_depth_never_exceeds_the_original(generated):
    """Глубина цепочки не больше 2: источник не бывает потребителем.

    Третий порядок — девять ходов ради одного пузыря. В записи оригинала его
    нет ни на одном из двадцати уровней.
    """
    for level in generated:
        sources = {link.source_key for link in level.meta_links}
        consumers = {link.consumer_key for link in level.meta_links}
        assert sources & consumers == set()
        assert level.meta.max_depth <= 2


@requires_db
def test_18_meta_survives_the_write_to_base(tmp_path, generated):
    """Сохранённый уровень остаётся мета-уровнем: и роль токена, и ребро графа."""
    import shutil

    from word_content.db import connect

    copy = tmp_path / "content.sqlite"
    shutil.copy(PROJECT_DB, copy)
    conn = connect(copy)
    try:
        with conn:
            level_generator.save(conn, generated)
        for level in generated:
            row = conn.execute(
                "SELECT id FROM level_instances WHERE level_key = ?", (level.level_key,)
            ).fetchone()
            assert row is not None
            level_id = int(row["id"])
            deps = list(
                conn.execute(
                    "SELECT COUNT(*) AS n FROM level_dependencies WHERE level_id = ?",
                    (level_id,),
                )
            )[0]["n"]
            outputs = list(
                conn.execute(
                    "SELECT COUNT(*) AS n FROM level_tokens "
                    " WHERE level_id = ? AND token_kind = 'category_output'",
                    (level_id,),
                )
            )[0]["n"]
            assert deps == len(level.meta_links)
            assert outputs == len(level.meta_links)
            # Источник показан под той надписью, которую он выпускает.
            for link in level.meta_links:
                shown = conn.execute(
                    """
                    SELECT l.display_text AS text
                      FROM level_dependencies d
                      JOIN level_groups g ON g.id = d.from_group_id
                      JOIN category_labels l ON l.id = g.display_label_id
                      JOIN level_tokens t ON t.id = d.to_token_id
                     WHERE d.level_id = ? AND t.display_text = ?
                    """,
                    (level_id, link.token_display),
                ).fetchone()
                assert shown is not None and shown["text"] == link.source_label
            stored = meta_validation.validate_level_in_db(conn, level_id)
            assert stored.ok, stored.problems
            assert stored.max_depth == (2 if level.meta_links else 1)
    finally:
        conn.close()


@requires_db
def test_18b_meta_can_be_switched_off(db):
    """Флаг `--no-meta` возвращает плоскую сборку: механика включается осознанно."""
    levels, stats = level_generator.generate(
        db, count=2, category_count=GENERATED_CATEGORIES, seed=GENERATED_SEED,
        use_meta=False,
    )
    assert stats["мета-связей поставлено"] == 0
    assert all(not level.meta_links for level in levels)


def test_19_composition_profile_is_taken_from_the_recording(fixtures):
    """Профиль композиции — это запись, а не выдумка про кривую сложности."""
    recorded = composition.table()
    assert len(recorded) == 20
    assert all(item.recorded for item in recorded.values())

    # Опорные точки записи: первая мета, пик первой десятки, передышка.
    assert (recorded[1].categories, recorded[1].meta_links) == (5, 0)
    assert (recorded[3].categories, recorded[3].meta_links) == (8, 1)
    assert (recorded[7].categories, recorded[7].meta_links) == (12, 6)
    assert (recorded[10].categories, recorded[10].meta_links) == (8, 0)
    assert (recorded[17].categories, recorded[17].meta_links) == (11, 6)
    # Уровень 18 снят частично, но одиннадцатикатегорийным он был целиком.
    assert recorded[18].categories == 18 - 7

    totals = reference_fixtures.totals(fixtures.upto(None))
    assert sum(item.meta_links for item in recorded.values()) == totals["meta_links"]

    beyond = composition.for_level(21)
    assert beyond.source == "extrapolated"
    assert beyond.categories == 10 and beyond.meta_links == 4


def test_19b_meta_target_keeps_the_share_but_not_the_count():
    """На меньшем числе категорий доля мета сохраняется, а не переносится числом."""
    level_seven = composition.for_level(7)  # 12 категорий, 6 мета
    assert level_seven.meta_target(12) == 6
    assert level_seven.meta_target(5) == 2
    assert composition.for_level(1).meta_target(12) == 0
    # Потолок держится даже при нелепом запросе.
    assert composition.for_level(7).meta_target(3) <= 3


# --------------------------------------------------------------- разбор записи как есть


def test_fixture_totals_match_the_recording(fixtures):
    """Контрольные числа записи. Меняются только вместе с самой записью."""
    ten = reference_fixtures.totals(fixtures.upto(10))
    assert ten["groups_recorded"] == 95
    assert ten["slots"] == 380
    assert ten["meta_links"] == 17
    assert ten["observed_labels"] == 24
    assert ten["distinct_quartets"] == 95

    every = reference_fixtures.totals(fixtures.upto(None))
    assert every["groups_recorded"] == 188
    assert every["slots"] == 752
    assert every["meta_links"] == 56
    assert every["distinct_labels"] == 168
    assert every["distinct_tokens"] == 660
    assert every["levels_fully_recorded"] == 19


def test_repeated_label_hides_different_quartets(fixtures):
    """Одинаковая надпись — не одинаковое правило. Ради этого всё и переделано."""
    music_3 = fixtures.get(3).group_by_name("music")
    music_6 = fixtures.get(6).group_by_name("music")
    assert music_3.words == ("pop", "rock", "jazz", "rap")
    assert music_6.words == ("piano", "drum", "flute", "guitar")
    assert music_3.quartet_signature != music_6.quartet_signature
