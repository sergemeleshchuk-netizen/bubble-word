"""Доступность значения слова: три разных качества вместо одного `fit_score`.

Генератор собрал группу BOARD GAMES из `Life / risk / sorry / trouble`. Все
четыре связи семантически верны — такие настольные игры существуют. Играть в это
нельзя: `life` читается как жизнь, `risk` как риск, `sorry` как извинение,
`trouble` как неприятность. Ни одно слово не называет тему; категория берётся
полным перебором остальных групп.

База не различала три вопроса и отвечала на все одним числом `fit_score = 0.97`:

1. **Semantic validity** — может ли слово в этом значении принадлежать категории.
   Для `Trouble` как названия игры — да. Это `memberships.semantic_status`.
2. **Sense accessibility** — вспомнит ли обычный игрок именно это значение,
   увидев слово без названия категории. Для `Trouble` — почти никогда.
   Это `word_senses.accessibility_class` и два числа рядом с ним.
3. **Quartet solvability** — хватает ли четвёрке ясных якорей, чтобы тему можно
   было прочитать, а не вычислить исключением. Это `quartet_semantics`.

Здесь живёт второе качество и производная классификация связи.

Почему `accessibility_class` дискретный, а числа вспомогательные. Число легко
поставить «на глаз» и невозможно проверить: ровно так появились 17 505 связей
с `fit_score = 0.97`. Класс — это решение, у него всего пять значений, и каждое
имеет проверяемое определение. Числа нужны ранжированию и диагностике; там, где
числа нет, слот не становится якорем, но и не блокирует базу.

Почему `uses_non_dominant` не приговор. `orange` в COLORS — не главное значение
слова (главное — фрукт), но цвет знают все, и группа red/blue/green/orange
честная. `Trouble` в BOARD GAMES — тоже не главное значение, но игру знает
меньшинство. Разница не в доминантности, а в доступности, поэтому генератор
смотрит на `risk_class`, а не на булев признак.
"""

from __future__ import annotations

from dataclasses import dataclass

# --------------------------------------------------------------------- словари

# Что за сущность стоит за значением. Влияет на то, чего мы ждём от оценок:
# у названия игры узнаваемость может быть высокой при почти нулевой активации.
SENSE_KINDS: tuple[str, ...] = (
    "lexical",       # обычное словарное значение
    "proper_name",   # имя человека, места
    "title",         # название произведения, игры, передачи
    "brand",         # торговая марка
    "abbreviation",  # аббревиатура
)

# Насколько значение доступно широкой аудитории. Основной дискретный шлюз.
#
#   primary          значение, которым слово читается без контекста
#                    (trouble = неприятность, life = жизнь)
#   common_secondary не первое, но массово известное
#                    (orange = цвет, cold = простуда, rock = жанр)
#   specialist       верное значение, известное ограниченной аудитории
#                    (Trouble = конкретная настольная игра)
#   obscure          редкое даже для поздней кампании
#   unresolved       значение заведено, доступность не определена
ACCESSIBILITY_CLASSES: tuple[str, ...] = (
    "primary",
    "common_secondary",
    "specialist",
    "obscure",
    "unresolved",
)

# Классы, у которых доступность считается определённой. `unresolved` сюда не
# входит намеренно: неизвестность — это не «безопасно», это «нельзя в продакшен».
RESOLVED_CLASSES: frozenset[str] = frozenset(
    {"primary", "common_secondary", "specialist", "obscure"}
)

# Классы, пригодные для роли якоря группы. Дальше их ещё проверяют числами.
ANCHOR_CLASSES: frozenset[str] = frozenset({"primary", "common_secondary"})

# Итог классификации связи. Именно это читает генератор.
RISK_CLASSES: tuple[str, ...] = (
    "primary",           # основное значение слова
    "fair_secondary",    # вторичное, но доступное: честная ловушка
    "specialist_trick",  # верно и недоступно: подвох
    "obscure_trick",     # редкое: подвох тяжелее
    "surface_form",      # правило про написание, значение не участвует
    "unresolved",        # значение не разрешено
)

_CLASS_TO_RISK: dict[str, str] = {
    "primary": "primary",
    "common_secondary": "fair_secondary",
    "specialist": "specialist_trick",
    "obscure": "obscure_trick",
    "unresolved": "unresolved",
}

# Аудитория, для которой сейчас оцениваются значения. Мульти-аудиторную модель
# не строим: одна аудитория, но записанная явно, чтобы вторую можно было
# добавить не переписывая оценки.
DEFAULT_AUDIENCE = "general_en_us_adult"

# Откуда взялась оценка. Различать обязательно: экспертное решение и производная
# от знакомости слова — разного качества данные, и калибровать их будут порознь.
QUALITY_SOURCES: tuple[str, ...] = (
    "sense_review",         # человек или AI разобрал значение явно
    "derived_monosemous",   # у слова одно значение, оценка выведена из метрик слова
    "reference_import",     # значение пришло из записи оригинала
)

# Виды связи, которым значение не нужно по устройству правила.
SENSE_EXEMPT_MODES: frozenset[str] = frozenset({"surface_form"})


class SenseQualityError(ValueError):
    """Недопустимое значение в слое доступности."""


def validate_class(value: str | None) -> str:
    if value is None:
        return "unresolved"
    if value not in ACCESSIBILITY_CLASSES:
        raise SenseQualityError(
            f"accessibility_class={value!r}; допустимы: {', '.join(ACCESSIBILITY_CLASSES)}"
        )
    return value


def validate_kind(value: str | None) -> str:
    if value is None:
        return "lexical"
    if value not in SENSE_KINDS:
        raise SenseQualityError(
            f"sense_kind={value!r}; допустимы: {', '.join(SENSE_KINDS)}"
        )
    return value


def validate_score(value: float | None, *, field: str) -> float | None:
    """Пустая оценка допустима, оценка вне 0..1 — нет.

    Пустая означает «не измеряли»: такой слот не станет якорем, но и не будет
    выброшен из базы. Подставлять сюда высокий default запрещено — именно так
    неизвестность превращается в мнимое качество.
    """
    if value is None:
        return None
    number = float(value)
    if not 0.0 <= number <= 1.0:
        raise SenseQualityError(f"{field}={number}; допустим диапазон 0..1")
    return number


# ------------------------------------------------------------------- факты

@dataclass(frozen=True)
class SenseFacts:
    """Значение слова глазами слоя доступности."""

    sense_id: int | None
    sense_key: str | None = None
    sense_kind: str = "lexical"
    accessibility_class: str = "unresolved"
    recognition_score: float | None = None
    activation_score: float | None = None
    dominance_rank: int | None = None

    @property
    def is_resolved(self) -> bool:
        return self.accessibility_class in RESOLVED_CLASSES


@dataclass(frozen=True)
class MembershipSemantics:
    """Классификация связи «слово в категории»: что именно она использует."""

    risk_class: str
    uses_non_dominant: bool
    accessibility_class: str
    production_eligible: bool
    reasons: tuple[str, ...] = ()

    @property
    def is_anchor_class(self) -> bool:
        return self.accessibility_class in ANCHOR_CLASSES


def classify(
    *,
    sense_mode: str,
    sense_id: int | None,
    semantic_status: str,
    dominant_sense_id: int | None,
    sense: SenseFacts | None,
) -> MembershipSemantics:
    """Единственное место, где связь получает свой семантический класс.

    Ею пользуются генератор, проверка целостности, оценщик и диагностика CLI:
    три реализации одного правила разошлись бы на первой же правке.
    """
    if sense_mode in SENSE_EXEMPT_MODES:
        # Правило про написание: `words_before_time` держит `life` за буквы,
        # а не за смысл. Значение здесь не обязано существовать.
        return MembershipSemantics(
            risk_class="surface_form",
            uses_non_dominant=False,
            accessibility_class="surface_form",
            production_eligible=semantic_status != "incorrect",
        )

    if sense_id is None or sense is None:
        return MembershipSemantics(
            risk_class="unresolved",
            uses_non_dominant=False,
            accessibility_class="unresolved",
            production_eligible=False,
            reasons=("значение связи не разрешено",),
        )

    accessibility = validate_class(sense.accessibility_class)
    uses_non_dominant = dominant_sense_id is not None and sense_id != dominant_sense_id

    reasons: list[str] = []
    eligible = True
    if accessibility == "unresolved":
        reasons.append("доступность значения не определена")
        eligible = False
    if semantic_status == "incorrect":
        reasons.append("связь признана семантически неверной")
        eligible = False

    return MembershipSemantics(
        risk_class=_CLASS_TO_RISK[accessibility],
        uses_non_dominant=uses_non_dominant,
        accessibility_class=accessibility,
        production_eligible=eligible,
        reasons=tuple(reasons),
    )
