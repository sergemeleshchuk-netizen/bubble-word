"""Pydantic-модели входных данных (JSONL/CSV)."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .normalization import (
    NormalizationError,
    clean_display_text,
    is_valid_category_key,
    normalize_sense_key,
    normalize_word,
)

Score = Annotated[float, Field(ge=0.0, le=1.0)]

# Лестница пригодности связи для уровня:
#   approved    — значение, которое игрок вспоминает первым (monitor -> COMPUTER PARTS)
#   alternative — верное и узнаваемое, но не первое (monitor -> HOSPITAL THINGS): ловушка
#   hard_only   — верно, но сам игрок не догадается (monitor -> LIZARDS)
REVIEW_STATUSES = ("candidate", "approved", "alternative", "hard_only", "rejected")
ReviewStatus = Literal["candidate", "approved", "alternative", "hard_only", "rejected"]

# Статусы, означающие «связь идёт в игру». Для них частотность слова обязательна:
# без неё нельзя утверждать, что средний игрок это слово знает.
PLAYABLE_STATUSES = ("approved", "alternative", "hard_only")

# Куда падает связь, когда данных для решения нет. Правило аудита: отсутствующие
# данные должны закрывать связь, а не проходить как подтверждённые.
FAIL_CLOSED_STATUS = "candidate"


def familiarity_gate(
    review_status: str, familiarity_score: float | None
) -> tuple[str, str | None]:
    """Запрещает играбельный статус при неизвестной частотности.

    Возвращает (статус, причина понижения). Причина не None только если статус изменён.
    `rejected` и `candidate` не трогаем: им частотность не нужна.
    """
    if familiarity_score is not None or review_status not in PLAYABLE_STATUSES:
        return review_status, None
    return (
        FAIL_CLOSED_STATUS,
        f"частотность слова неизвестна: статус {review_status} понижен "
        f"до {FAIL_CLOSED_STATUS} до ручной проверки",
    )

RISK_FLAGS = (
    "obscure",
    "regional",
    "proper_noun",
    "multiword",
    "culturally_specific",
    "weak_relation",
    "highly_ambiguous",
    "sensitive",
    "possible_duplicate",
    # добавлено по аудиту: терминологические и правовые риски
    "outdated_term",  # устаревшее название, есть современная замена (gypsy moth -> spongy moth)
    "trademark",  # товарный знак: написание и правовой статус нужно проверять
    "no_familiarity",  # частотность посчитать не удалось: связь не может быть approved
    "needs_sense",  # слово переиспользуется в разных смыслах, значения не разведены
)

# Семантическая корректность связи — отдельная ось от игровой пригодности
# (review_status). Связь бывает correct и hard_only одновременно.
SEMANTIC_STATUSES = ("unreviewed", "correct", "disputed", "incorrect")
SemanticStatus = Literal["unreviewed", "correct", "disputed", "incorrect"]

# Готовность категории к автоматической сборке уровней
CATEGORY_READINESS = ("unknown", "ready", "constrained", "curated_only", "hard_only", "blocked")


class CategoryInput(BaseModel):
    """Строка categories.jsonl."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    category_key: str
    label: str = Field(min_length=1)
    rule: str = Field(min_length=10)
    relation_type: str = Field(min_length=1)
    theme: str = Field(min_length=1)
    base_difficulty: float | None = Field(default=None, ge=0.0, le=1.0)
    status: str = "active"

    @field_validator("category_key")
    @classmethod
    def _check_key(cls, value: str) -> str:
        if not is_valid_category_key(value):
            raise ValueError(
                f"Неверный category_key {value!r}: разрешены только строчные латинские "
                "буквы, цифры и подчёркивание; ключ не может начинаться с цифры "
                "и содержать пробелы"
            )
        return value


class MembershipCandidateInput(BaseModel):
    """Строка membership_candidates.jsonl (связь слово -> категория)."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    word: str
    language: str = "en"
    part_of_speech: str | None = None
    is_proper_noun: bool = False
    sense_key: str | None = None
    sense_definition: str | None = None
    # Как связь обращается со словом. Пусто — выводится из типа связи при импорте
    # (см. importers.derive_sense_mode); задаётся явно там, где вывод неверен.
    sense_mode: Literal["lexical", "surface_form", "compound", "phrase_pattern"] | None = None
    category_key: str
    relation_type: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    fit_score: Score
    obviousness_score: Score
    source: str = "ai"
    review_status: ReviewStatus = "candidate"
    semantic_status: SemanticStatus = "unreviewed"
    gameplay_difficulty: Score | None = None
    risk_flags: list[str] = Field(default_factory=list)

    @field_validator("word")
    @classmethod
    def _check_word(cls, value: str) -> str:
        try:
            normalize_word(value)
        except NormalizationError as exc:
            raise ValueError(str(exc)) from exc
        return clean_display_text(value)

    @field_validator("category_key")
    @classmethod
    def _check_key(cls, value: str) -> str:
        if not is_valid_category_key(value):
            raise ValueError(f"Неверный category_key: {value!r}")
        return value

    @field_validator("sense_key")
    @classmethod
    def _check_sense_key(cls, value: str | None) -> str | None:
        if value is None or value == "":
            return None
        return normalize_sense_key(value)

    @field_validator("sense_definition", "part_of_speech")
    @classmethod
    def _empty_to_none(cls, value: str | None) -> str | None:
        return value or None

    @field_validator("risk_flags")
    @classmethod
    def _check_flags(cls, value: list[str]) -> list[str]:
        unknown = [flag for flag in value if flag not in RISK_FLAGS]
        if unknown:
            raise ValueError(
                f"Неизвестные risk_flags: {unknown}. Разрешены: {list(RISK_FLAGS)}"
            )
        return value

    @model_validator(mode="after")
    def _sense_pair(self) -> MembershipCandidateInput:
        if self.sense_key and not self.sense_definition:
            raise ValueError("sense_key передан без sense_definition")
        if self.sense_definition and not self.sense_key:
            raise ValueError("sense_definition передан без sense_key")
        return self

    @property
    def normalized(self) -> str:
        return normalize_word(self.word)


class ReviewDecisionInput(BaseModel):
    """Строка review-CSV с решением человека.

    membership_id необязателен: связь можно указать парой слово + категория,
    и это надёжнее — id зависит от порядка вставки и меняется при пересборке.
    """

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    membership_id: int | None = Field(default=None, gt=0)
    decision: ReviewStatus
    review_comment: str | None = None
    # необязательная колонка: reviewer может отдельно отметить семантику
    semantic_status: SemanticStatus | None = None
    gameplay_difficulty: Score | None = None

    @field_validator("membership_id", mode="before")
    @classmethod
    def _blank_to_none(cls, value: object) -> object:
        if isinstance(value, str) and not value.strip():
            return None
        return value

    @field_validator("decision", mode="before")
    @classmethod
    def _normalize_decision(cls, value: object) -> object:
        if isinstance(value, str):
            lowered = value.strip().lower()
            # синонимы из CSV: approve/reject -> approved/rejected
            return {"approve": "approved", "reject": "rejected"}.get(lowered, lowered)
        return value

    @field_validator("review_comment")
    @classmethod
    def _empty_to_none(cls, value: str | None) -> str | None:
        return value or None

    @field_validator("semantic_status", "gameplay_difficulty", mode="before")
    @classmethod
    def _blank_optional(cls, value: object) -> object:
        if isinstance(value, str) and not value.strip():
            return None
        return value


class CategoryConflictInput(BaseModel):
    """Строка category_conflicts.csv: две категории, которые нельзя ставить в один уровень."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    category_a: str
    category_b: str
    conflict_type: Literal["do_not_pair", "needs_disjoint_words"] = "do_not_pair"
    origin: Literal["derived", "manual"] = "derived"
    overlap_count: int = Field(default=0, ge=0)
    overlap_words: str | None = None
    severity: str | None = None
    note: str | None = None

    @field_validator("category_a", "category_b")
    @classmethod
    def _check_key(cls, value: str) -> str:
        if not is_valid_category_key(value):
            raise ValueError(f"Неверный category_key: {value!r}")
        return value

    @model_validator(mode="after")
    def _distinct(self) -> CategoryConflictInput:
        if self.category_a == self.category_b:
            raise ValueError("Категория не может конфликтовать сама с собой")
        return self


class QuartetInput(BaseModel):
    """Строка quartets.csv: проверенная четвёрка слов одной категории."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    quartet_key: str = Field(min_length=1)
    category_key: str
    tier: Literal["normal", "hard"] = "normal"
    # Состояние машинных валидаторов. `human_approved` здесь нет намеренно:
    # человек принимает собранный уровень, а не отдельную четвёрку.
    validation_state: Literal[
        "proposed", "auto_validated", "warning", "invalid", "disabled"
    ] = "proposed"
    # Локальная проверка: не лежит ли четвёрка целиком в чужом пуле. Единственность
    # уровня этим не доказывается — она живёт в level_instances.solution_count.
    local_check: Literal["unchecked", "local_unique", "local_ambiguous"] = "unchecked"
    difficulty: Score | None = None
    note: str | None = None
    # четыре слова через "|", по желанию с значением: "ring#ring_arena"
    words: str

    @field_validator("category_key")
    @classmethod
    def _check_key(cls, value: str) -> str:
        if not is_valid_category_key(value):
            raise ValueError(f"Неверный category_key: {value!r}")
        return value

    @property
    def word_items(self) -> list[tuple[str, str | None]]:
        items: list[tuple[str, str | None]] = []
        for chunk in self.words.split("|"):
            chunk = chunk.strip()
            if not chunk:
                continue
            word, _, sense = chunk.partition("#")
            items.append((word.strip(), sense.strip() or None))
        return items

    @model_validator(mode="after")
    def _exactly_four(self) -> QuartetInput:
        items = self.word_items
        if len(items) != 4:
            raise ValueError(f"В четвёрке должно быть ровно 4 слова, получено {len(items)}")
        normalized = {normalize_word(word) for word, _ in items}
        if len(normalized) != 4:
            raise ValueError("В четвёрке есть повторяющиеся слова")
        return self
