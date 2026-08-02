"""Семантика четвёрки целиком: хватает ли ей якорей, чтобы тему можно было прочитать.

Фильтра по одной связи мало. Каждая из четырёх связей
`Life / risk / sorry / trouble -> BOARD GAMES` по отдельности верна; неиграбельна
именно четвёрка, потому что в ней нет ни одного слова, которое называет тему.
Игрок вынужден собрать три остальные группы и взять оставшееся — а это не
разгадка, а вычитание.

Поэтому здесь считается не сумма оценок слов, а состав четвёрки:

* **якоря** — слоты, по которым тему видно;
* **ловушки** — слоты со вторым, но доступным значением (`orange` в COLORS);
* **подвохи** — слоты со значением, которого игрок не вспомнит (`Trouble`);
* **режим связности** — по какому принципу четвёрка вообще держится.

Режим связности нужен, потому что одна мерка на все группы ломает половину
контента. `north / south / east / west` — закрытый набор: у него нет и не должно
быть сильных попарных ассоциаций, и требовать их значит выбросить структурные
наборы. Мета-коллектор состоит из результатов других категорий, у него вообще
нет лексических якорей по устройству. Тип берётся из уже существующего
`categories.rule_type`, новой онтологии здесь не заводится.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from statistics import median

from . import sense_quality

# --------------------------------------------------------------------- коды отказов

# Коды, которыми объясняется отклонение четвёрки. Ими пользуются CLI, тесты и
# диагностика нехватки контента; человеческий текст идёт следом за кодом.
UNRESOLVED_SENSE = "UNRESOLVED_SENSE"
SPECIALIST_SENSE = "SPECIALIST_SENSE"
OBSCURE_SENSE = "OBSCURE_SENSE"
TOO_MANY_COMMON_SECONDARY_SENSES = "TOO_MANY_COMMON_SECONDARY_SENSES"
INSUFFICIENT_CLEAR_ANCHORS = "INSUFFICIENT_CLEAR_ANCHORS"
LOW_SENSE_ACCESSIBILITY = "LOW_SENSE_ACCESSIBILITY"
LOW_COHERENCE = "LOW_COHERENCE"
PROFILE_RULE_MISMATCH = "PROFILE_RULE_MISMATCH"
META_DEPENDENCY_INVALID = "META_DEPENDENCY_INVALID"
PACK_SWOW_DISCONNECTED_RATIO = "PACK_SWOW_DISCONNECTED_RATIO"

REASON_CODES: tuple[str, ...] = (
    UNRESOLVED_SENSE,
    SPECIALIST_SENSE,
    OBSCURE_SENSE,
    TOO_MANY_COMMON_SECONDARY_SENSES,
    INSUFFICIENT_CLEAR_ANCHORS,
    LOW_SENSE_ACCESSIBILITY,
    LOW_COHERENCE,
    PROFILE_RULE_MISMATCH,
    META_DEPENDENCY_INVALID,
    PACK_SWOW_DISCONNECTED_RATIO,
)


def code_of(reason: str) -> str | None:
    """Код из строки причины. Причины хранятся как «КОД: человеческий текст»."""
    head = reason.split(":", 1)[0].strip()
    return head if head in REASON_CODES else None


# ------------------------------------------------------------------ режимы связности

ASSOCIATIVE = "associative"
TAXONOMIC = "taxonomic"
STRUCTURED_SET = "structured_set"
COMPONENTS = "components"
FUNCTIONAL = "functional"
META_COLLECTOR = "meta_collector"
SURFACE_FORM = "surface_form"

COHERENCE_MODES: tuple[str, ...] = (
    ASSOCIATIVE, TAXONOMIC, STRUCTURED_SET, COMPONENTS,
    FUNCTIONAL, META_COLLECTOR, SURFACE_FORM,
)

# Тип правила базы -> режим связности. Соответствие однозначное: своей онтологии
# здесь нет, есть перевод уже принятой классификации на язык проверок.
_RULE_TYPE_TO_MODE: dict[str, str] = {
    "taxonomy_instances": TAXONOMIC,
    "property_group": TAXONOMIC,
    "components": COMPONENTS,
    "association_hub": ASSOCIATIVE,
    "context_hub": ASSOCIATIVE,
    "functional_group": FUNCTIONAL,
    "structured_set": STRUCTURED_SET,
    "sequence": STRUCTURED_SET,
    "meta_collector": META_COLLECTOR,
    "unclassified": ASSOCIATIVE,
}

# Режимы, для которых SWOW — осмысленный сигнал связности. Закрытый набор
# (стороны света), части целого и мета-коллектор попарными ассоциациями не
# держатся, и отсутствие рёбер у них ничего не значит.
SWOW_MEANINGFUL: frozenset[str] = frozenset({ASSOCIATIVE, FUNCTIONAL})

# Режимы, от которых не требуется лексических якорей: якорей там нет по
# устройству правила, а не по недосмотру.
ANCHOR_EXEMPT: frozenset[str] = frozenset({META_COLLECTOR, SURFACE_FORM})


def coherence_mode(rule_type: str | None, *, all_surface_form: bool = False) -> str:
    if all_surface_form:
        return SURFACE_FORM
    return _RULE_TYPE_TO_MODE.get(rule_type or "unclassified", ASSOCIATIVE)


# ------------------------------------------------------------------------ слот и группа


@dataclass(frozen=True)
class SlotSemantics:
    """Один слот четвёрки глазами слоя доступности."""

    word: str
    token_kind: str = "lexical_word"
    sense_mode: str = "lexical"
    sense_id: int | None = None
    accessibility_class: str = "unresolved"
    risk_class: str = "unresolved"
    recognition_score: float | None = None
    activation_score: float | None = None
    uses_non_dominant: bool = False
    semantic_status: str = "unreviewed"

    @property
    def is_lexical(self) -> bool:
        """Слот, от которого база обязана знать значение.

        Кусочки слова (`chunked_word`) — форма показа одного и того же слова,
        значение им нужно так же, как обычному пузырю. Результат другой
        категории (`category_output`) лексическим словом не является и
        проверяется мета-графом, а не словарём.
        """
        return self.token_kind in ("lexical_word", "chunked_word", "picture_token")

    def is_anchor(self, *, recognition_min: float, activation_min: float) -> bool:
        """Ясный якорь: слово, по которому тему видно, а не только подтверждают.

        Пустая оценка якорем не делает. Неизвестность — это не «хорошо»;
        именно так `fit_score = 0.97` у 92% связей когда-то стал доказательством
        качества, которого никто не измерял.
        """
        if self.sense_mode in sense_quality.SENSE_EXEMPT_MODES:
            return False
        if self.sense_id is None:
            return False
        if self.semantic_status == "incorrect":
            return False
        if self.accessibility_class not in sense_quality.ANCHOR_CLASSES:
            return False
        if self.recognition_score is None or self.activation_score is None:
            return False
        return (
            self.recognition_score >= recognition_min
            and self.activation_score >= activation_min
        )


@dataclass(frozen=True)
class SwowMetrics:
    """Снимок связности четвёрки по SWOW. Отсутствие данных — не ноль."""

    observed_nodes: int = 0
    observed_pairs: int = 0
    positive_pairs: int = 0
    strongest_edge: float = 0.0
    median_edge: float = 0.0

    @property
    def has_data(self) -> bool:
        return self.observed_pairs > 0

    @property
    def no_positive_edges(self) -> bool:
        """Ни одна пара четвёрки не дала связи.

        Метрика пакета, по которой считались 52% первой сборки и 22% записи
        оригинала. Формулу трогать нельзя: сравнение before/after держится
        именно на ней.
        """
        return self.positive_pairs == 0

    @property
    def disconnected(self) -> bool:
        """Пары БЫЛО чем измерить, и ни одна не дала связи.

        Строже предыдущей и годится для отклонения конкретной четвёрки: нуль
        от того, что слова нет в датасете, — это пробел в чужих данных, а не
        отсутствие смысла, и наказывать за него нельзя.
        """
        return self.observed_pairs > 0 and self.positive_pairs == 0


@dataclass
class QuartetSemantics:
    """Полный семантический профиль четвёрки."""

    slots: tuple[SlotSemantics, ...]
    mode: str = ASSOCIATIVE
    swow: SwowMetrics = field(default_factory=SwowMetrics)
    anchor_recognition_min: float = 0.0
    anchor_activation_min: float = 0.0

    # ---- состав слотов
    @property
    def lexical_slots(self) -> list[SlotSemantics]:
        return [slot for slot in self.slots if slot.is_lexical]

    @property
    def lexical_slot_count(self) -> int:
        return len(self.lexical_slots)

    @property
    def meta_output_count(self) -> int:
        return sum(1 for slot in self.slots if slot.token_kind == "category_output")

    @property
    def picture_count(self) -> int:
        return sum(1 for slot in self.slots if slot.token_kind == "picture_token")

    @property
    def chunked_word_count(self) -> int:
        return sum(1 for slot in self.slots if slot.token_kind == "chunked_word")

    @property
    def surface_form_count(self) -> int:
        return sum(
            1 for slot in self.slots
            if slot.sense_mode in sense_quality.SENSE_EXEMPT_MODES
        )

    # ---- значения
    def _class_count(self, name: str) -> int:
        return sum(
            1 for slot in self.lexical_slots
            if slot.sense_mode not in sense_quality.SENSE_EXEMPT_MODES
            and slot.accessibility_class == name
        )

    @property
    def resolved_sense_count(self) -> int:
        return sum(
            1 for slot in self.lexical_slots
            if slot.sense_mode not in sense_quality.SENSE_EXEMPT_MODES
            and slot.sense_id is not None
            and slot.accessibility_class in sense_quality.RESOLVED_CLASSES
        )

    @property
    def unresolved_sense_count(self) -> int:
        return sum(
            1 for slot in self.lexical_slots
            if slot.sense_mode not in sense_quality.SENSE_EXEMPT_MODES
            and (
                slot.sense_id is None
                or slot.accessibility_class not in sense_quality.RESOLVED_CLASSES
            )
        )

    @property
    def primary_sense_count(self) -> int:
        return self._class_count("primary")

    @property
    def common_secondary_sense_count(self) -> int:
        return self._class_count("common_secondary")

    @property
    def specialist_sense_count(self) -> int:
        return self._class_count("specialist")

    @property
    def obscure_sense_count(self) -> int:
        return self._class_count("obscure")

    @property
    def uses_non_dominant_count(self) -> int:
        return sum(1 for slot in self.lexical_slots if slot.uses_non_dominant)

    # ---- якоря
    @property
    def anchors(self) -> list[SlotSemantics]:
        return [
            slot for slot in self.lexical_slots
            if slot.is_anchor(
                recognition_min=self.anchor_recognition_min,
                activation_min=self.anchor_activation_min,
            )
        ]

    @property
    def clear_anchor_count(self) -> int:
        return len(self.anchors)

    @property
    def anchorless(self) -> bool:
        """Группа без единого ясного якоря. Для мета и игры слов — не порок."""
        if self.mode in ANCHOR_EXEMPT:
            return False
        if not self.lexical_slots:
            return False
        return self.clear_anchor_count == 0

    def _accessibility_values(self) -> list[float]:
        return [
            min(slot.recognition_score, slot.activation_score)
            for slot in self.lexical_slots
            if slot.recognition_score is not None and slot.activation_score is not None
        ]

    @property
    def weakest_accessibility_score(self) -> float | None:
        values = self._accessibility_values()
        return min(values) if values else None

    @property
    def median_accessibility_score(self) -> float | None:
        values = self._accessibility_values()
        return median(values) if values else None

    @property
    def swow_exempt(self) -> bool:
        """Режим, для которого попарные ассоциации ничего не измеряют."""
        return self.mode not in SWOW_MEANINGFUL

    @property
    def swow_disconnected(self) -> bool:
        return self.swow.disconnected

    def as_dict(self) -> dict[str, object]:
        return {
            "coherence_mode": self.mode,
            "lexical_slot_count": self.lexical_slot_count,
            "resolved_sense_count": self.resolved_sense_count,
            "unresolved_sense_count": self.unresolved_sense_count,
            "primary_sense_count": self.primary_sense_count,
            "common_secondary_sense_count": self.common_secondary_sense_count,
            "specialist_sense_count": self.specialist_sense_count,
            "obscure_sense_count": self.obscure_sense_count,
            "clear_anchor_count": self.clear_anchor_count,
            "weakest_accessibility_score": self.weakest_accessibility_score,
            "median_accessibility_score": self.median_accessibility_score,
            "uses_non_dominant_count": self.uses_non_dominant_count,
            "swow_has_data": self.swow.has_data,
            "swow_observed_pairs": self.swow.observed_pairs,
            "swow_positive_pairs": self.swow.positive_pairs,
            "swow_median_edge": self.swow.median_edge,
            "swow_disconnected": self.swow_disconnected,
            "swow_exempt": self.swow_exempt,
            "meta_output_count": self.meta_output_count,
            "picture_count": self.picture_count,
            "chunked_word_count": self.chunked_word_count,
        }


# --------------------------------------------------------------------------- проверки


def check(semantics: QuartetSemantics, limits: dict[str, float]) -> list[str]:
    """Причины, по которым четвёрка не годится профилю. Пусто — годится.

    Порядок проверок — от «данных нет» к «данные есть и они плохие»: первая
    причина в списке должна объяснять главное, а не первое попавшееся.
    """
    reasons: list[str] = []

    def limit(key: str, default: float) -> float:
        return float(limits.get(key, default))

    if limit("require_resolved_senses", 0) >= 1 and semantics.unresolved_sense_count:
        reasons.append(
            f"{UNRESOLVED_SENSE}: слотов без разрешённого значения "
            f"{semantics.unresolved_sense_count}"
        )

    allowed = limit("max_specialist_senses_per_group", 4)
    if semantics.specialist_sense_count > allowed:
        reasons.append(
            f"{SPECIALIST_SENSE}: значений, известных узкому кругу, "
            f"{semantics.specialist_sense_count} > {int(allowed)}"
        )

    allowed = limit("max_obscure_senses_per_group", 4)
    if semantics.obscure_sense_count > allowed:
        reasons.append(
            f"{OBSCURE_SENSE}: редких значений {semantics.obscure_sense_count} > {int(allowed)}"
        )

    allowed = limit("max_common_secondary_senses_per_group", 4)
    if semantics.common_secondary_sense_count > allowed:
        reasons.append(
            f"{TOO_MANY_COMMON_SECONDARY_SENSES}: вторых, но известных значений "
            f"{semantics.common_secondary_sense_count} > {int(allowed)}"
        )

    required = limit("min_clear_anchors_per_lexical_group", 0)
    if required > 0 and semantics.mode not in ANCHOR_EXEMPT and semantics.lexical_slots:
        # Требовать больше якорей, чем в группе лексических слотов, бессмысленно:
        # мета-группа с двумя словами и двумя результатами категорий физически
        # не наберёт три.
        need = min(int(required), semantics.lexical_slot_count)
        if semantics.clear_anchor_count < need:
            reasons.append(
                f"{INSUFFICIENT_CLEAR_ANCHORS}: ясных якорей "
                f"{semantics.clear_anchor_count} < {need}"
            )

    floor = limit("group_accessibility_min", 0)
    if floor > 0 and semantics.lexical_slots:
        weakest = semantics.weakest_accessibility_score
        if weakest is None:
            reasons.append(
                f"{LOW_SENSE_ACCESSIBILITY}: доступность значений не посчитана, "
                f"порог {floor}"
            )
        elif weakest < floor:
            reasons.append(
                f"{LOW_SENSE_ACCESSIBILITY}: слабейшее значение {weakest:.2f} < {floor}"
            )

    # SWOW — сигнал, а не приговор, и только там, где он вообще что-то измеряет.
    # Порог применяется к ассоциативным и функциональным группам: закрытый набор
    # и части целого попарными ассоциациями не держатся.
    if limit("forbid_swow_disconnected_associative", 0) >= 1 and not semantics.swow_exempt:
        if semantics.swow_disconnected:
            reasons.append(
                f"{LOW_COHERENCE}: ассоциативная группа, у которой ни одна "
                f"из {semantics.swow.observed_pairs} измеримых пар не связана"
            )

    return reasons


# ------------------------------------------------------------------------ чтение базы


def load_swow(conn: sqlite3.Connection) -> dict[str, SwowMetrics]:
    """Снимок метрик SWOW по ключу четвёрки. Пусто — метрики не импортированы."""
    try:
        rows = conn.execute(
            """
            SELECT quartet_key, observed_nodes, observed_pairs, positive_pairs,
                   strongest_edge, median_edge
              FROM quartet_association_metrics
            """
        )
    except sqlite3.OperationalError:
        return {}
    return {
        row["quartet_key"]: SwowMetrics(
            observed_nodes=int(row["observed_nodes"]),
            observed_pairs=int(row["observed_pairs"]),
            positive_pairs=int(row["positive_pairs"]),
            strongest_edge=float(row["strongest_edge"]),
            median_edge=float(row["median_edge"]),
        )
        for row in rows
    }


def slots_from_rows(rows: list[sqlite3.Row]) -> tuple[SlotSemantics, ...]:
    """Слоты из строк выборки генератора: одна форма чтения на всех.

    Ожидаемые колонки: normalized/display, token_kind (может отсутствовать —
    тогда обычное слово), sense_mode, sense_id, accessibility_class, risk_class,
    recognition_score, activation_score, uses_non_dominant, semantic_status.
    """
    slots: list[SlotSemantics] = []
    for row in rows:
        keys = row.keys()
        slots.append(
            SlotSemantics(
                word=str(row["word"] if "word" in keys else row["display"]),
                token_kind=(row["token_kind"] if "token_kind" in keys else None)
                or "lexical_word",
                sense_mode=(row["sense_mode"] if "sense_mode" in keys else None) or "lexical",
                sense_id=row["sense_id"] if "sense_id" in keys else None,
                accessibility_class=(
                    row["accessibility_class"] if "accessibility_class" in keys else None
                )
                or "unresolved",
                risk_class=(row["risk_class"] if "risk_class" in keys else None)
                or "unresolved",
                recognition_score=row["recognition_score"]
                if "recognition_score" in keys
                else None,
                activation_score=row["activation_score"] if "activation_score" in keys else None,
                uses_non_dominant=bool(
                    row["uses_non_dominant"] if "uses_non_dominant" in keys else 0
                ),
                semantic_status=(row["semantic_status"] if "semantic_status" in keys else None)
                or "unreviewed",
            )
        )
    return tuple(slots)
