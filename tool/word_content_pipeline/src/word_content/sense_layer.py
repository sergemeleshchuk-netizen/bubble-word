"""Сборка слоя значений: кто получает значение автоматически, а кто — только руками.

Задача шага — закрыть дыру «база хранит написание слова, а не значение», но
закрыть её честно. Автоматически расставить значения всем 18 882 связям нельзя:
это заменит отсутствие значений на большое количество неверных значений, и
проверить их будет уже нечем.

Поэтому слой делится надвое.

**Разбирается вручную** (`data/seed/_sense_map.json`) — слова, у которых
значение выбирать надо: многозначные, имена, названия. Там же лежат оценки
доступности, и только там; в коде оценок нет.

**Выводится автоматически** — слова, у которых значение одно. Для такого слова
значение и есть слово: если игрок знает `moat`, он знает ров, другого чтения
нет. Такому значению ставится `primary`, а числа берутся из уже измеренной
знакомости слова, поэтому они разные у разных слов, а не общий default.

Между двумя половинами стоит детектор риска. Он не решает, какое значение
верное; он решает, можно ли слову доверять без разбора. Слово попадает в ручную
очередь, если:

* у него уже заведено больше одного значения;
* оно стоит в категории названий (`categories.names_titles`) — ровно случай
  `trouble` в BOARD GAMES: обычное английское слово внутри списка названий
  почти всегда стоит не своим главным значением;
* оно имя собственное;
* оно растащено по многим темам (порог из `sense_gaps`).

Явное решение человека сильнее детектора: слово из `_not_homonyms.txt` признано
однозначным вручную и разбирается автоматически даже при широком разбросе тем.

Чего здесь намеренно нет: догадок по частотности. Zipf измеряет написание, а не
значение, и `Trouble` как игра имеет ровно ту же частотность, что и `trouble`
как неприятность.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from . import sense_quality
from .db import utc_now
from .normalization import normalize_word
from .readiness import PLAYABLE_STATUSES
from .sense_gaps import MIN_CATEGORIES, MIN_THEMES, load_not_homonyms
from .sense_map import SenseMap, default_sense_map

# Ключ автоматически выведенного значения. Суффикс отличает его от разобранных
# руками (`orange_fruit`, `bark_tree`) в любом отчёте и в самой базе.
DERIVED_SUFFIX = "_main"

# Границы производных оценок. Нижняя граница не нулевая: слово с одним значением
# нельзя объявить недоступным только потому, что оно редкое — редкость уже
# посчитана отдельным фактором и штрафовать за неё дважды нечестно.
_RECOGNITION_BASE, _RECOGNITION_SPAN = 0.80, 0.19
_ACTIVATION_BASE, _ACTIVATION_SPAN = 0.70, 0.29
_CONFIDENCE_BASE, _CONFIDENCE_SPAN = 0.55, 0.20

# Знакомость, подставляемая, если её не посчитали. Ровно середина шкалы: не
# награда и не наказание. Ставить сюда высокое значение запрещено — так
# неизвестность превращается в мнимое качество.
_FAMILIARITY_FALLBACK = 0.50


def _round(value: float) -> float:
    return round(value, 4)


def derived_scores(familiarity: float | None) -> tuple[float, float, float]:
    """Оценки однозначного значения: узнаваемость, активация, уверенность.

    Для однозначного слова активация почти равна узнаваемости: вспоминать
    нечего, кроме единственного значения. Разрыв между ними остаётся только
    из-за знакомости самого написания — слово, которого игрок не знает, он и
    не активирует.
    """
    known = _FAMILIARITY_FALLBACK if familiarity is None else max(0.0, min(1.0, familiarity))
    return (
        _round(_RECOGNITION_BASE + _RECOGNITION_SPAN * known),
        _round(_ACTIVATION_BASE + _ACTIVATION_SPAN * known),
        _round(_CONFIDENCE_BASE + _CONFIDENCE_SPAN * known),
    )


@dataclass
class SenseLayerReport:
    declared_words: int = 0
    declared_senses: int = 0
    enriched_senses: int = 0
    derived_senses: int = 0
    dominant_set: int = 0
    memberships_assigned: int = 0
    memberships_from_map: int = 0
    blocked_words: int = 0
    blocked_reasons: dict[str, int] = field(default_factory=dict)

    def lines(self) -> list[str]:
        return [
            f"слов с объявленными значениями: {self.declared_words}",
            f"значений объявлено/создано:     {self.declared_senses}",
            f"значений дополнено оценками:    {self.enriched_senses}",
            f"значений выведено автоматически:{self.derived_senses}",
            f"доминантных значений выставлено:{self.dominant_set}",
            f"связей получило значение:       {self.memberships_assigned} "
            f"(из карты {self.memberships_from_map})",
            f"слов оставлено на ручной разбор:{self.blocked_words} "
            + (
                "(" + ", ".join(f"{k} {v}" for k, v in sorted(self.blocked_reasons.items())) + ")"
                if self.blocked_reasons
                else ""
            ),
        ]


# ------------------------------------------------------------------ детектор риска


@dataclass(frozen=True)
class WordRisk:
    """Почему слову нельзя вывести значение автоматически. Пусто — можно."""

    reasons: tuple[str, ...]

    def __bool__(self) -> bool:
        return bool(self.reasons)


def _risk_index(conn: sqlite3.Connection) -> dict[int, tuple[str, ...]]:
    """Причины ручного разбора по каждому слову-кандидату."""
    placeholders = ",".join("?" for _ in PLAYABLE_STATUSES)
    spread: dict[int, tuple[set[str], set[str]]] = {}
    titles: set[int] = set()
    for row in conn.execute(
        f"""
        SELECT m.word_id AS word_id, c.category_key AS category_key,
               c.theme AS theme, c.names_titles AS names_titles
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
         WHERE m.review_status IN ({placeholders})
           AND m.sense_mode <> 'surface_form'
        """,
        PLAYABLE_STATUSES,
    ):
        word_id = int(row["word_id"])
        cats, themes = spread.setdefault(word_id, (set(), set()))
        cats.add(row["category_key"])
        themes.add(row["theme"])
        if row["names_titles"]:
            titles.add(word_id)

    multi_sense = {
        int(row[0])
        for row in conn.execute(
            "SELECT word_id FROM word_senses GROUP BY word_id HAVING COUNT(*) > 1"
        )
    }
    proper = {
        int(row[0]) for row in conn.execute("SELECT id FROM words WHERE is_proper_noun = 1")
    }

    index: dict[int, tuple[str, ...]] = {}
    for word_id, (cats, themes) in spread.items():
        reasons: list[str] = []
        if word_id in multi_sense:
            reasons.append("значений больше одного")
        if word_id in titles:
            reasons.append("стоит в категории названий")
        if word_id in proper:
            reasons.append("имя собственное")
        if len(cats) >= MIN_CATEGORIES and len(themes) >= MIN_THEMES:
            reasons.append("разброс по темам")
        if reasons:
            index[word_id] = tuple(reasons)
    return index


# ------------------------------------------------------------------------ применение


def _upsert_sense(
    conn: sqlite3.Connection,
    *,
    word_id: int,
    sense_key: str,
    definition: str | None,
    part_of_speech: str | None,
    display_text: str | None,
    is_proper_noun: bool,
    sense_kind: str,
    dominance_rank: int | None,
    accessibility_class: str,
    recognition_score: float | None,
    activation_score: float | None,
    audience_profile: str | None,
    quality_source: str | None,
    quality_confidence: float | None,
) -> tuple[int, str]:
    """Заводит значение или дополняет существующее. Возвращает (id, что сделали)."""
    sense_quality.validate_kind(sense_kind)
    sense_quality.validate_class(accessibility_class)
    sense_quality.validate_score(recognition_score, field="recognition_score")
    sense_quality.validate_score(activation_score, field="activation_score")
    sense_quality.validate_score(quality_confidence, field="quality_confidence")

    row = conn.execute(
        "SELECT id, definition FROM word_senses WHERE word_id = ? AND sense_key = ?",
        (word_id, sense_key),
    ).fetchone()
    now = utc_now()
    if row is None:
        cursor = conn.execute(
            """
            INSERT INTO word_senses
                (word_id, sense_key, definition, part_of_speech, created_at,
                 display_text, is_proper_noun, sense_kind, dominance_rank,
                 accessibility_class, recognition_score, activation_score,
                 audience_profile, quality_source, quality_confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                word_id,
                sense_key,
                definition or "",
                part_of_speech,
                now,
                display_text,
                int(is_proper_noun),
                sense_kind,
                dominance_rank,
                accessibility_class,
                recognition_score,
                activation_score,
                audience_profile,
                quality_source,
                quality_confidence,
            ),
        )
        return int(cursor.lastrowid), "created"

    # Значение уже есть — например, пришло из `_ambiguous.json` вместе со связью.
    # Определение оттуда не перетираем: карта отвечает за качество значения,
    # а не за его формулировку.
    conn.execute(
        """
        UPDATE word_senses
           SET definition = COALESCE(NULLIF(?, ''), definition),
               part_of_speech = COALESCE(?, part_of_speech),
               display_text = COALESCE(?, display_text),
               sense_kind = ?, dominance_rank = ?,
               accessibility_class = ?, recognition_score = ?, activation_score = ?,
               audience_profile = ?, quality_source = ?, quality_confidence = ?
         WHERE id = ?
        """,
        (
            definition or "",
            part_of_speech,
            display_text,
            sense_kind,
            dominance_rank,
            accessibility_class,
            recognition_score,
            activation_score,
            audience_profile,
            quality_source,
            quality_confidence,
            int(row["id"]),
        ),
    )
    return int(row["id"]), "enriched"


def apply(
    conn: sqlite3.Connection,
    *,
    sense_map: SenseMap | None = None,
    not_homonyms_path: Path | None = None,
) -> SenseLayerReport:
    """Раскладывает объявленные значения по базе и выводит остальные.

    Идемпотентна: повторный запуск на готовой базе не меняет ничего.
    """
    smap = sense_map or default_sense_map()
    audience = smap.audience_profile
    homonym_path = not_homonyms_path or _default_not_homonyms()
    not_homonyms = load_not_homonyms(homonym_path) if homonym_path else set()

    report = SenseLayerReport()
    words = {
        row["normalized"]: (int(row["id"]), row["familiarity_score"])
        for row in conn.execute("SELECT id, normalized, familiarity_score FROM words")
    }
    sense_ids: dict[tuple[int, str], int] = {}

    # 1. Значения, объявленные в карте. Источник правды на этом шаге один.
    for word, entries in smap.declared_senses().items():
        found = words.get(word)
        if found is None:
            continue
        word_id = found[0]
        report.declared_words += 1
        for sense_key, spec in entries.items():
            sense_id, action = _upsert_sense(
                conn,
                word_id=word_id,
                sense_key=sense_key,
                definition=spec.definition,
                part_of_speech=spec.part_of_speech,
                display_text=spec.display_text,
                is_proper_noun=spec.is_proper_noun,
                sense_kind=spec.sense_kind,
                dominance_rank=spec.dominance_rank,
                accessibility_class=spec.accessibility_class,
                recognition_score=spec.recognition_score,
                activation_score=spec.activation_score,
                audience_profile=spec.audience_profile or audience,
                # `sense_review` ставится только там, где доступность реально
                # объявлена. Запись без класса — это унаследованное значение из
                # `_ambiguous.json`, и выдавать его за разобранное нельзя.
                quality_source=spec.quality_source
                or ("sense_review" if spec.accessibility_class != "unresolved" else None),
                quality_confidence=spec.quality_confidence,
            )
            sense_ids[(word_id, sense_key)] = sense_id
            if action == "created":
                report.declared_senses += 1
            else:
                report.enriched_senses += 1

    # 2. Привязка «слово + категория -> значение» из карты.
    for word, by_category in smap.declared_assignments().items():
        found = words.get(word)
        if found is None:
            continue
        word_id = found[0]
        for category_key, sense_key in by_category.items():
            sense_id = sense_ids.get((word_id, sense_key))
            if sense_id is None:
                row = conn.execute(
                    "SELECT id FROM word_senses WHERE word_id = ? AND sense_key = ?",
                    (word_id, sense_key),
                ).fetchone()
                if row is None:
                    continue
                sense_id = int(row["id"])
            changed = conn.execute(
                """
                UPDATE memberships
                   SET sense_id = ?, updated_at = ?
                 WHERE word_id = ?
                   AND sense_mode <> 'surface_form'
                   AND category_id = (SELECT id FROM categories WHERE category_key = ?)
                   AND COALESCE(sense_id, -1) <> ?
                """,
                (sense_id, utc_now(), word_id, category_key, sense_id),
            ).rowcount
            report.memberships_from_map += changed
            report.memberships_assigned += changed

    # 2b. Слово, у которого разбор объявил ровно одно значение, получает его во
    #     все свои лексические связи. Выбирать не из чего: ревью сказало, что
    #     смысл у слова один, и переписывать это правило в каждой строке
    #     привязок значило бы плодить сотни строк ради одного факта.
    for word, entries in smap.declared_senses().items():
        if len(entries) != 1:
            continue
        found = words.get(word)
        if found is None:
            continue
        word_id = found[0]
        sense_key = next(iter(entries))
        sense_id = sense_ids.get((word_id, sense_key))
        if sense_id is None:
            continue
        report.memberships_assigned += conn.execute(
            """
            UPDATE memberships
               SET sense_id = ?, updated_at = ?
             WHERE word_id = ? AND sense_id IS NULL AND sense_mode <> 'surface_form'
            """,
            (sense_id, utc_now(), word_id),
        ).rowcount

    # 3. Автовывод для однозначных слов.
    risk = _risk_index(conn)
    declared = set(smap.declared_senses())
    has_sense = {
        int(row[0]) for row in conn.execute("SELECT DISTINCT word_id FROM word_senses")
    }
    candidates = conn.execute(
        """
        SELECT DISTINCT m.word_id AS word_id
          FROM memberships m
         WHERE m.sense_id IS NULL AND m.sense_mode <> 'surface_form'
        """
    ).fetchall()
    by_id = {value[0]: (word, value[1]) for word, value in words.items()}

    for row in candidates:
        word_id = int(row["word_id"])
        word, familiarity = by_id.get(word_id, (None, None))
        if word is None:
            continue
        if word in declared or word_id in has_sense:
            # Значения у слова уже есть: какое из них верно в этой категории —
            # решение карты, а не автовывода. Молча взять первое нельзя.
            report.blocked_words += 1
            report.blocked_reasons["значения есть, привязки нет"] = (
                report.blocked_reasons.get("значения есть, привязки нет", 0) + 1
            )
            continue
        reasons = risk.get(word_id, ())
        if reasons and word not in not_homonyms:
            report.blocked_words += 1
            for reason in reasons:
                report.blocked_reasons[reason] = report.blocked_reasons.get(reason, 0) + 1
            continue

        recognition, activation, confidence = derived_scores(familiarity)
        sense_id, action = _upsert_sense(
            conn,
            word_id=word_id,
            sense_key=f"{word}{DERIVED_SUFFIX}",
            definition=f"The everyday meaning of the English word “{word}”.",
            part_of_speech=None,
            display_text=None,
            is_proper_noun=False,
            sense_kind="lexical",
            dominance_rank=1,
            accessibility_class="primary",
            recognition_score=recognition,
            activation_score=activation,
            audience_profile=audience,
            quality_source="derived_monosemous",
            quality_confidence=confidence,
        )
        if action == "created":
            report.derived_senses += 1
        report.memberships_assigned += conn.execute(
            """
            UPDATE memberships
               SET sense_id = ?, updated_at = ?
             WHERE word_id = ? AND sense_id IS NULL AND sense_mode <> 'surface_form'
            """,
            (sense_id, utc_now(), word_id),
        ).rowcount

    # 4. Доминантное значение слова. Ранг 1 — источник правды; если ранга нет
    #    ни у одного значения, доминантного значения у слова нет, и признак
    #    uses_non_dominant для него честно не считается.
    report.dominant_set = conn.execute(
        """
        UPDATE words
           SET dominant_sense_id = (
                   SELECT s.id FROM word_senses s
                    WHERE s.word_id = words.id AND s.dominance_rank = 1
                    ORDER BY s.id LIMIT 1
               )
         WHERE COALESCE(dominant_sense_id, -1) <> COALESCE((
                   SELECT s.id FROM word_senses s
                    WHERE s.word_id = words.id AND s.dominance_rank = 1
                    ORDER BY s.id LIMIT 1
               ), -1)
        """
    ).rowcount
    conn.commit()
    return report


def _default_not_homonyms() -> Path | None:
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "data" / "seed" / "_not_homonyms.txt"
        if candidate.exists():
            return candidate
    return None


def normalized(word: str) -> str:
    return normalize_word(word)
