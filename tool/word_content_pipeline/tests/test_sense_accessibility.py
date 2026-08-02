"""Приёмка слоя доступности значений.

Главный вопрос всего слоя: чем `Trouble` в BOARD GAMES отличается от `orange`
в COLORS. Обе связи верны, обе используют не главное значение слова. Разница в
том, что цвет знают все, а игру почти никто, — и если система этой разницы не
видит, она либо пропускает неиграбельные группы, либо запрещает честные ловушки.

Поэтому фикстуры идут парами: рядом с плохим случаем всегда стоит похожий на
него хороший, который обязан пройти.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest

from word_content import profiles, quartet_semantics, sense_layer, sense_quality
from word_content.db import connect, init_db
from word_content.importers import import_categories, import_memberships
from word_content.sense_map import SenseMap

AUDIENCE = "general_en_us_adult"


def review(
    definition: str,
    *,
    rank: int,
    access: str,
    recognition: float,
    activation: float,
    kind: str = "lexical",
) -> dict:
    return {
        "definition": definition,
        "sense_kind": kind,
        "dominance_rank": rank,
        "accessibility_class": access,
        "recognition_score": recognition,
        "activation_score": activation,
        "audience_profile": AUDIENCE,
        "quality_source": "sense_review",
        "quality_confidence": 0.9,
    }


CATEGORIES = [
    # Категория названий: слова внутри неё — заголовки, а не слова.
    {"category_key": "board_games", "label": "BOARD GAMES",
     "rule": "Games played on a printed board with pieces", "relation_type": "is_a",
     "theme": "entertainment", "base_difficulty": 0.25, "names_titles": True},
    {"category_key": "colors", "label": "COLORS",
     "rule": "Basic colour words known to any English speaker",
     "relation_type": "is_a", "theme": "descriptive", "base_difficulty": 0.1},
    {"category_key": "fruits", "label": "FRUITS",
     "rule": "Common edible fruits familiar to an average American adult",
     "relation_type": "is_a", "theme": "food", "base_difficulty": 0.1},
    {"category_key": "directions", "label": "DIRECTIONS",
     "rule": "The four cardinal points of the compass",
     "relation_type": "is_a", "theme": "geography", "base_difficulty": 0.15},
    {"category_key": "words_before_time", "label": "___ TIME",
     "rule": "Words that form a familiar English compound before the word time",
     "relation_type": "phrase_before", "theme": "language", "base_difficulty": 0.4},
]

# Значения и привязки — ровно тот формат, что лежит в data/seed/_sense_map.json.
SENSE_MAP = {
    "audience_profile": AUDIENCE,
    "senses": {
        "trouble": {
            "trouble_problem": review("A problem or difficulty.", rank=1,
                                      access="primary", recognition=0.99, activation=0.97),
            "trouble_board_game": review("Trouble, an American board game.", rank=2,
                                         access="specialist", recognition=0.42,
                                         activation=0.04, kind="title"),
        },
        "life": {
            "life_existence": review("Being alive.", rank=1, access="primary",
                                     recognition=0.99, activation=0.98),
            "life_game": review("The Game of Life, a board game.", rank=2,
                                access="specialist", recognition=0.46,
                                activation=0.05, kind="title"),
        },
        "risk": {
            "risk_danger": review("Exposure to danger.", rank=1, access="primary",
                                  recognition=0.99, activation=0.96),
            "risk_board_game": review("Risk, a board game of conquest.", rank=2,
                                      access="specialist", recognition=0.48,
                                      activation=0.06, kind="title"),
        },
        "sorry": {
            "sorry_apology": review("The word said to apologise.", rank=1,
                                    access="primary", recognition=0.99, activation=0.98),
            "sorry_board_game": review("Sorry!, a board game.", rank=2,
                                       access="specialist", recognition=0.44,
                                       activation=0.05, kind="title"),
        },
        "chess": {"chess_game": review("The strategy game on a chequered board.", rank=1,
                                       access="primary", recognition=0.98, activation=0.96)},
        "monopoly": {"monopoly_game": review("Monopoly, the property board game.", rank=1,
                                             access="primary", recognition=0.96,
                                             activation=0.88, kind="title")},
        "scrabble": {"scrabble_game": review("Scrabble, the word board game.", rank=1,
                                             access="primary", recognition=0.95,
                                             activation=0.90, kind="title")},
        "checkers": {"checkers_game": review("Checkers, the board game.", rank=1,
                                             access="primary", recognition=0.96,
                                             activation=0.92)},
        "orange": {
            "orange_fruit": review("A round citrus fruit.", rank=1, access="primary",
                                   recognition=0.99, activation=0.92),
            "orange_color": review("The colour between red and yellow.", rank=2,
                                   access="common_secondary", recognition=0.99,
                                   activation=0.72),
        },
    },
    "assignments": {
        "trouble": {"board_games": "trouble_board_game"},
        "life": {"board_games": "life_game"},
        "risk": {"board_games": "risk_board_game"},
        "sorry": {"board_games": "sorry_board_game"},
        "chess": {"board_games": "chess_game"},
        "monopoly": {"board_games": "monopoly_game"},
        "scrabble": {"board_games": "scrabble_game"},
        "checkers": {"board_games": "checkers_game"},
        "orange": {"colors": "orange_color", "fruits": "orange_fruit"},
    },
}


def membership(word: str, category: str, **extra) -> dict:
    row = {
        "word": word,
        "category_key": category,
        "relation_type": "is_a",
        "reason": f"{word} belongs to {category}",
        "fit_score": 0.97,
        "obviousness_score": 0.85,
        "source": "seed_manual",
        "review_status": "approved",
    }
    row.update(extra)
    return row


MEMBERSHIPS = [
    *(membership(word, "board_games") for word in
      ("life", "risk", "sorry", "trouble", "chess", "monopoly", "scrabble", "checkers")),
    *(membership(word, "colors") for word in ("red", "blue", "green", "orange")),
    *(membership(word, "fruits") for word in ("apple", "banana", "orange", "grape")),
    *(membership(word, "directions") for word in ("north", "south", "east", "west")),
    # Настоящее правило про написание: значение здесь не участвует.
    *(membership(word, "words_before_time", relation_type="phrase_before")
      for word in ("bed", "lunch", "half", "prime")),
]


@pytest.fixture
def sense_db(tmp_path: Path) -> sqlite3.Connection:
    path = tmp_path / "senses.sqlite"
    init_db(path)
    conn = connect(path)

    categories = tmp_path / "categories.jsonl"
    categories.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in CATEGORIES) + "\n",
        encoding="utf-8",
    )
    memberships = tmp_path / "memberships.jsonl"
    memberships.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in MEMBERSHIPS) + "\n",
        encoding="utf-8",
    )
    map_path = tmp_path / "_sense_map.json"
    map_path.write_text(json.dumps(SENSE_MAP, ensure_ascii=False), encoding="utf-8")
    homonyms = tmp_path / "_not_homonyms.txt"
    homonyms.write_text(
        "\n".join(
            ("red", "blue", "green", "apple", "banana", "grape",
             "north", "south", "east", "west")
        ) + "\n",
        encoding="utf-8",
    )

    import_categories(conn, categories)
    import_memberships(conn, memberships, sense_map=SenseMap.load(map_path))
    # Тип правила в рабочей базе проставляет `derive-rule-types`; здесь он
    # задаётся явно — от него зависит режим связности группы.
    conn.execute(
        "UPDATE categories SET rule_type = 'structured_set' WHERE category_key = 'directions'"
    )
    conn.execute(
        "UPDATE categories SET rule_type = 'taxonomy_instances' "
        "WHERE category_key IN ('board_games', 'fruits')"
    )
    conn.execute(
        "UPDATE categories SET rule_type = 'property_group' WHERE category_key = 'colors'"
    )
    conn.commit()
    sense_layer.apply(
        conn, sense_map=SenseMap.load(map_path), not_homonyms_path=homonyms
    )
    yield conn
    conn.close()


def group(conn: sqlite3.Connection, category_key: str, words: list[str]) -> quartet_semantics.QuartetSemantics:
    """Семантика четвёрки, собранной вручную из связей базы."""
    rows = []
    for word in words:
        row = conn.execute(
            """
            SELECT v.sense_id, v.sense_mode, v.accessibility_class, v.risk_class,
                   v.uses_non_dominant, v.semantic_status,
                   s.recognition_score, s.activation_score, w.normalized AS word
              FROM v_membership_semantics v
              JOIN words w ON w.id = v.word_id
              JOIN categories c ON c.id = v.category_id
              LEFT JOIN word_senses s ON s.id = v.sense_id
             WHERE w.normalized = ? AND c.category_key = ?
            """,
            (word, category_key),
        ).fetchone()
        assert row is not None, f"нет связи {word} -> {category_key}"
        rows.append(row)
    rule_type = conn.execute(
        "SELECT rule_type FROM categories WHERE category_key = ?", (category_key,)
    ).fetchone()[0]
    slots = quartet_semantics.slots_from_rows(rows)
    all_surface = all(slot.sense_mode == "surface_form" for slot in slots)
    return quartet_semantics.QuartetSemantics(
        slots=slots,
        mode=quartet_semantics.coherence_mode(rule_type, all_surface_form=all_surface),
        anchor_recognition_min=0.75,
        anchor_activation_min=0.60,
    )


@pytest.fixture
def first_lineup() -> profiles.Profile:
    return profiles.get("first_lineup")


def codes(reasons: list[str]) -> set[str]:
    return {code for code in (quartet_semantics.code_of(r) for r in reasons) if code}


# ------------------------------------------------------------------ 16.1 плохая группа


def test_bad_board_games_rejected(sense_db, first_lineup):
    """Life / Risk / Sorry / Trouble не проходит вход в игру.

    И причин ровно две, обе содержательные: значения известны узкому кругу и
    ясных якорей в группе нет. Ни одна из них не является списком слов.
    """
    semantics = group(sense_db, "board_games", ["life", "risk", "sorry", "trouble"])
    assert semantics.specialist_sense_count == 4
    assert semantics.clear_anchor_count == 0
    assert semantics.uses_non_dominant_count == 4

    reasons = quartet_semantics.check(semantics, first_lineup.values)
    assert quartet_semantics.SPECIALIST_SENSE in codes(reasons)
    assert quartet_semantics.INSUFFICIENT_CLEAR_ANCHORS in codes(reasons)


def test_bad_board_games_not_rejected_by_blocklist(sense_db, first_lineup):
    """Отклонение держится на составе значений, а не на самих словах.

    Проверяется прямо: если тем же четырём словам поставить доступные значения,
    группа проходит. Значит отклоняет её правило, а не имя слова.
    """
    sense_db.executemany(
        "UPDATE word_senses SET accessibility_class = 'primary', "
        "recognition_score = 0.95, activation_score = 0.90 WHERE sense_key = ?",
        [("trouble_board_game",), ("life_game",), ("risk_board_game",),
         ("sorry_board_game",)],
    )
    semantics = group(sense_db, "board_games", ["life", "risk", "sorry", "trouble"])
    assert quartet_semantics.check(semantics, first_lineup.values) == []


# ------------------------------------------------------------- 16.2 очевидная группа


def test_obvious_board_games_eligible(sense_db, first_lineup):
    """chess / monopoly / scrabble / checkers — те же BOARD GAMES, и они проходят."""
    semantics = group(
        sense_db, "board_games", ["chess", "monopoly", "scrabble", "checkers"]
    )
    assert semantics.specialist_sense_count == 0
    assert semantics.clear_anchor_count == 4
    assert quartet_semantics.check(semantics, first_lineup.values) == []


# ------------------------------------------------------ 16.3 честное второе значение


def test_fair_secondary_sense_allowed(sense_db, first_lineup):
    """red / blue / green / orange проходит: `orange` — ловушка, а не подвох."""
    semantics = group(sense_db, "colors", ["red", "blue", "green", "orange"])
    assert semantics.common_secondary_sense_count == 1
    assert semantics.specialist_sense_count == 0
    assert semantics.clear_anchor_count >= 3
    assert quartet_semantics.check(semantics, first_lineup.values) == []


def test_orange_color_is_fair_secondary_not_specialist(sense_db):
    """`orange` в COLORS и `trouble` в BOARD GAMES: оба не главное значение.

    Именно эту пару система обязана различать. Булев признак «использует не
    главное значение» у них одинаковый, класс риска — разный.
    """
    color = sense_db.execute(
        """
        SELECT v.risk_class, v.uses_non_dominant, v.accessibility_class
          FROM v_membership_semantics v
          JOIN words w ON w.id = v.word_id
          JOIN categories c ON c.id = v.category_id
         WHERE w.normalized = 'orange' AND c.category_key = 'colors'
        """
    ).fetchone()
    game = sense_db.execute(
        """
        SELECT v.risk_class, v.uses_non_dominant, v.accessibility_class
          FROM v_membership_semantics v
          JOIN words w ON w.id = v.word_id
          JOIN categories c ON c.id = v.category_id
         WHERE w.normalized = 'trouble' AND c.category_key = 'board_games'
        """
    ).fetchone()

    assert color["uses_non_dominant"] == 1
    assert game["uses_non_dominant"] == 1
    assert color["risk_class"] == "fair_secondary"
    assert game["risk_class"] == "specialist_trick"
    assert color["accessibility_class"] == "common_secondary"
    assert game["accessibility_class"] == "specialist"


# ----------------------------------------------------- 16.4 главное значение того же слова


def test_primary_alternative_of_same_word(sense_db, first_lineup):
    """apple / banana / orange / grape: здесь `orange` стоит главным значением."""
    semantics = group(sense_db, "fruits", ["apple", "banana", "orange", "grape"])
    assert semantics.primary_sense_count == 4
    assert semantics.uses_non_dominant_count == 0
    assert quartet_semantics.check(semantics, first_lineup.values) == []


# ----------------------------------------------------------- 16.5 структурный набор


def test_structured_set_without_swow(sense_db, first_lineup):
    """north / south / east / west проходит без единой попарной ассоциации.

    Стороны света держатся правилом набора, а не ассоциациями. Одинаковый
    порог SWOW для них и для ассоциативной группы выбросил бы весь класс
    структурного контента.
    """
    semantics = group(sense_db, "directions", ["north", "south", "east", "west"])
    semantics.swow = quartet_semantics.SwowMetrics(
        observed_nodes=4, observed_pairs=6, positive_pairs=0
    )
    assert semantics.mode == quartet_semantics.STRUCTURED_SET
    assert semantics.swow_exempt is True

    strict = dict(first_lineup.values)
    strict["forbid_swow_disconnected_associative"] = 1.0
    assert quartet_semantics.check(semantics, strict) == []


def test_associative_group_is_not_exempt_from_swow():
    """А вот ассоциативная группа без единой связи по SWOW отклоняется."""
    slots = tuple(
        quartet_semantics.SlotSemantics(
            word=word, sense_id=1, accessibility_class="primary",
            risk_class="primary", recognition_score=0.9, activation_score=0.9,
        )
        for word in ("alpha", "beta", "gamma", "delta")
    )
    semantics = quartet_semantics.QuartetSemantics(
        slots=slots,
        mode=quartet_semantics.ASSOCIATIVE,
        swow=quartet_semantics.SwowMetrics(
            observed_nodes=4, observed_pairs=6, positive_pairs=0
        ),
        anchor_recognition_min=0.75,
        anchor_activation_min=0.60,
    )
    reasons = quartet_semantics.check(
        semantics, {"forbid_swow_disconnected_associative": 1.0}
    )
    assert quartet_semantics.LOW_COHERENCE in codes(reasons)


def test_swow_absence_of_data_is_not_disconnected():
    """Пары, которую нечем измерить, не существует для проверки связности."""
    empty = quartet_semantics.SwowMetrics(observed_nodes=0, observed_pairs=0)
    assert empty.has_data is False
    assert empty.disconnected is False
    # Метрика пакета считает иначе и это намеренно: формула, которой получены
    # 52% и 22%, смотрит только на наличие положительных рёбер.
    assert empty.no_positive_edges is True


# ------------------------------------------------------------------ 16.6 мета-коллектор


def test_meta_collector_needs_no_lexical_anchors(first_lineup):
    """Группа из результатов других категорий не обязана иметь три якоря."""
    slots = tuple(
        quartet_semantics.SlotSemantics(word=word, token_kind="category_output")
        for word in ("cat", "coffee", "doctor", "music")
    )
    semantics = quartet_semantics.QuartetSemantics(
        slots=slots,
        mode=quartet_semantics.META_COLLECTOR,
        anchor_recognition_min=0.75,
        anchor_activation_min=0.60,
    )
    assert semantics.lexical_slot_count == 0
    assert semantics.meta_output_count == 4
    assert semantics.anchorless is False
    assert quartet_semantics.check(semantics, first_lineup.values) == []


def test_meta_collector_with_two_words_is_not_asked_for_three_anchors(first_lineup):
    """Смешанная мета-группа: требование якорей не может превышать число слов."""
    slots = (
        quartet_semantics.SlotSemantics(word="cat", token_kind="category_output"),
        quartet_semantics.SlotSemantics(word="dog", token_kind="category_output"),
        quartet_semantics.SlotSemantics(
            word="milk", sense_id=1, accessibility_class="primary",
            recognition_score=0.95, activation_score=0.92),
        quartet_semantics.SlotSemantics(
            word="bowl", sense_id=2, accessibility_class="primary",
            recognition_score=0.94, activation_score=0.90),
    )
    semantics = quartet_semantics.QuartetSemantics(
        slots=slots, mode=quartet_semantics.ASSOCIATIVE,
        anchor_recognition_min=0.75, anchor_activation_min=0.60,
    )
    assert semantics.lexical_slot_count == 2
    assert semantics.clear_anchor_count == 2
    assert quartet_semantics.INSUFFICIENT_CLEAR_ANCHORS not in codes(
        quartet_semantics.check(semantics, first_lineup.values)
    )


# ----------------------------------------------------------- 16.7 неизвестное значение


def test_unresolved_sense_rejected(first_lineup):
    """Слот без значения отклоняется кодом UNRESOLVED_SENSE, а не проходит молча."""
    slots = (
        quartet_semantics.SlotSemantics(
            word="mystery", sense_id=None, accessibility_class="unresolved"),
        *(
            quartet_semantics.SlotSemantics(
                word=word, sense_id=index, accessibility_class="primary",
                recognition_score=0.95, activation_score=0.92)
            for index, word in enumerate(("alpha", "beta", "gamma"), start=1)
        ),
    )
    semantics = quartet_semantics.QuartetSemantics(
        slots=slots, mode=quartet_semantics.TAXONOMIC,
        anchor_recognition_min=0.75, anchor_activation_min=0.60,
    )
    assert semantics.unresolved_sense_count == 1
    assert quartet_semantics.UNRESOLVED_SENSE in codes(
        quartet_semantics.check(semantics, first_lineup.values)
    )


def test_unknown_sense_is_not_treated_as_primary():
    """Неизвестность не повышается до главного значения ни при каких условиях."""
    result = sense_quality.classify(
        sense_mode="lexical", sense_id=None, semantic_status="unreviewed",
        dominant_sense_id=None, sense=None,
    )
    assert result.risk_class == "unresolved"
    assert result.production_eligible is False
    assert result.is_anchor_class is False


# ------------------------------------------------------------ 16.8 исключение написания


def test_surface_form_exception(sense_db, first_lineup):
    """Правило про написание проходит без значений — и только оно."""
    semantics = group(
        sense_db, "words_before_time", ["bed", "lunch", "half", "prime"]
    )
    assert semantics.mode == quartet_semantics.SURFACE_FORM
    assert semantics.surface_form_count == 4
    assert semantics.unresolved_sense_count == 0
    assert semantics.anchorless is False
    assert quartet_semantics.check(semantics, first_lineup.values) == []


def test_surface_form_membership_is_production_eligible(sense_db):
    """Связь про написание пригодна для продакшена без значения."""
    row = sense_db.execute(
        """
        SELECT v.risk_class, v.production_eligible
          FROM v_membership_semantics v
          JOIN words w ON w.id = v.word_id
          JOIN categories c ON c.id = v.category_id
         WHERE w.normalized = 'bed' AND c.category_key = 'words_before_time'
        """
    ).fetchone()
    assert row["risk_class"] == "surface_form"
    assert row["production_eligible"] == 1


# ------------------------------------------------------------------ автовывод значений


def test_title_category_word_is_never_auto_resolved(tmp_path):
    """Слово из категории названий автоматически значение не получает.

    Это то место, где детектор обязан сработать без списка слов: `trouble`
    имеет ровно одну связь и по разбросу тем не подозрителен вовсе. Ловит его
    признак категории.
    """
    path = tmp_path / "auto.sqlite"
    init_db(path)
    conn = connect(path)
    categories = tmp_path / "c.jsonl"
    categories.write_text(json.dumps(CATEGORIES[0], ensure_ascii=False) + "\n",
                          encoding="utf-8")
    memberships = tmp_path / "m.jsonl"
    memberships.write_text(
        json.dumps(membership("trouble", "board_games"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    empty_map = tmp_path / "empty.json"
    empty_map.write_text('{"senses": {}, "assignments": {}}', encoding="utf-8")
    homonyms = tmp_path / "none.txt"
    homonyms.write_text("", encoding="utf-8")

    import_categories(conn, categories)
    # Пустая карта намеренно: проверяется поведение БЕЗ разбора, а проектная
    # карта `trouble` уже разобрала и подставила бы значение сама.
    import_memberships(conn, memberships, sense_map=SenseMap.load(empty_map))
    sense_layer.apply(
        conn, sense_map=SenseMap.load(empty_map), not_homonyms_path=homonyms
    )

    row = conn.execute(
        "SELECT sense_id FROM memberships m JOIN words w ON w.id = m.word_id "
        "WHERE w.normalized = 'trouble'"
    ).fetchone()
    assert row["sense_id"] is None, "значение подставлено автоматически в категории названий"
    conn.close()


def test_derived_scores_vary_with_familiarity():
    """Производные оценки разные у разных слов, а не общий default.

    История, ради которой проверка существует: 17 505 связей из 18 882 имели
    `fit_score = 0.97`. Одинаковое число не измеряет ничего.
    """
    low = sense_layer.derived_scores(0.1)
    high = sense_layer.derived_scores(0.9)
    assert low != high
    assert all(0.0 <= value <= 1.0 for value in low + high)
    assert low[1] < high[1]


def test_missing_familiarity_does_not_become_high_score():
    """Неизвестная знакомость даёт середину шкалы, а не награду."""
    unknown = sense_layer.derived_scores(None)
    best = sense_layer.derived_scores(1.0)
    assert unknown[1] < best[1]


# ---------------------------------------------------------------- классификация связи


@pytest.mark.parametrize(
    "access,expected",
    [
        ("primary", "primary"),
        ("common_secondary", "fair_secondary"),
        ("specialist", "specialist_trick"),
        ("obscure", "obscure_trick"),
        ("unresolved", "unresolved"),
    ],
)
def test_risk_class_mapping(access, expected):
    result = sense_quality.classify(
        sense_mode="lexical", sense_id=7, semantic_status="correct",
        dominant_sense_id=1,
        sense=sense_quality.SenseFacts(sense_id=7, accessibility_class=access),
    )
    assert result.risk_class == expected
    assert result.uses_non_dominant is True


def test_view_and_function_agree(sense_db):
    """Витрина базы и функция в коде обязаны давать один и тот же класс.

    Две реализации одного правила разошлись бы на первой же правке, поэтому
    их держит тест, а не договорённость.
    """
    rows = sense_db.execute(
        """
        SELECT v.membership_id, v.sense_mode, v.sense_id, v.semantic_status,
               v.dominant_sense_id, v.risk_class, v.uses_non_dominant,
               v.production_eligible, v.accessibility_class
          FROM v_membership_semantics v
        """
    ).fetchall()
    assert rows
    for row in rows:
        facts = (
            None if row["sense_id"] is None
            else sense_quality.SenseFacts(
                sense_id=row["sense_id"],
                accessibility_class=row["accessibility_class"],
            )
        )
        computed = sense_quality.classify(
            sense_mode=row["sense_mode"],
            sense_id=row["sense_id"],
            semantic_status=row["semantic_status"],
            dominant_sense_id=row["dominant_sense_id"],
            sense=facts,
        )
        assert computed.risk_class == row["risk_class"], row["membership_id"]
        assert int(computed.uses_non_dominant) == row["uses_non_dominant"]
        assert int(computed.production_eligible) == row["production_eligible"]


def test_reason_codes_are_declared():
    """Каждый код отказа объявлен в списке: тесты и CLI ищут их по имени."""
    for name in (
        quartet_semantics.UNRESOLVED_SENSE,
        quartet_semantics.SPECIALIST_SENSE,
        quartet_semantics.OBSCURE_SENSE,
        quartet_semantics.TOO_MANY_COMMON_SECONDARY_SENSES,
        quartet_semantics.INSUFFICIENT_CLEAR_ANCHORS,
        quartet_semantics.LOW_SENSE_ACCESSIBILITY,
        quartet_semantics.LOW_COHERENCE,
        quartet_semantics.PROFILE_RULE_MISMATCH,
        quartet_semantics.META_DEPENDENCY_INVALID,
        quartet_semantics.PACK_SWOW_DISCONNECTED_RATIO,
    ):
        assert name in quartet_semantics.REASON_CODES
        assert quartet_semantics.code_of(f"{name}: пояснение") == name


def test_profile_without_semantics_fails_closed():
    """Профиль, требующий значений, не пропускает четвёрку без посчитанной семантики."""
    profile = profiles.get("first_lineup")
    facts = profiles.QuartetFacts(
        quartet_key="x", label_text="ANYTHING", min_familiarity=1.0,
        avg_familiarity=1.0, min_accessibility=1.0, max_word_chars=4,
        max_word_tokens=1, label_chars=8, label_tokens=1, label_quality=1.0,
        quartet_quality=1.0, quartet_interest=1.0, ambiguity=0.0,
        rare_words=0, long_phrases=0, semantics=None,
    )
    assert quartet_semantics.UNRESOLVED_SENSE in codes(
        profiles.check_quartet(profile, facts)
    )
