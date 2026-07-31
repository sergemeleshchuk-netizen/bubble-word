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
)


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
    category_key: str
    relation_type: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    fit_score: Score
    obviousness_score: Score
    source: str = "ai"
    review_status: ReviewStatus = "candidate"
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
    """Строка review-CSV с решением человека."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    membership_id: int = Field(gt=0)
    decision: ReviewStatus
    review_comment: str | None = None

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
