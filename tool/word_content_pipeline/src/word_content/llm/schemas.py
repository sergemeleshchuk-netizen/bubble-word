"""Pydantic-схемы для строго структурированных ответов модели."""

from __future__ import annotations

import json
import re
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..models import RISK_FLAGS

Score = Annotated[float, Field(ge=0.0, le=1.0)]

_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def parse_json_response(raw: str) -> dict:
    """Снимает markdown-обёртку, если модель её всё-таки добавила, и парсит JSON."""
    text = (raw or "").strip()
    if text.startswith("```"):
        text = _FENCE_RE.sub("", text).strip()
    if not text:
        raise ValueError("Пустой ответ модели")
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError(f"Ожидался JSON-объект, получен {type(payload).__name__}")
    return payload


class _FlagsMixin(BaseModel):
    @field_validator("risk_flags", check_fields=False)
    @classmethod
    def _known_flags(cls, value: list[str]) -> list[str]:
        return [flag for flag in value if flag in RISK_FLAGS]


class CategoryCandidate(_FlagsMixin):
    """Один кандидат из прохода category expansion."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    word: str = Field(min_length=1)
    part_of_speech: str | None = None
    is_proper_noun: bool = False
    sense_key: str | None = None
    sense_definition: str | None = None
    relation_type: str | None = None
    reason: str = Field(min_length=1)
    fit_score: Score
    obviousness_score: Score
    possible_other_category_keys: list[str] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)


class CategoryExpansionOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    category_key: str
    candidates: list[CategoryCandidate] = Field(default_factory=list)


class WordMembershipSuggestion(_FlagsMixin):
    """Одна предложенная связь из reverse-прохода."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    category_key: str = Field(min_length=1)
    sense_key: str | None = None
    sense_definition: str | None = None
    relation_type: str | None = None
    reason: str = Field(min_length=1)
    fit_score: Score
    obviousness_score: Score
    risk_flags: list[str] = Field(default_factory=list)


class WordMemberships(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    word: str = Field(min_length=1)
    memberships: list[WordMembershipSuggestion] = Field(default_factory=list)


class ReverseExpansionOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    words: list[WordMemberships] = Field(default_factory=list)


class AdversarialVerdict(BaseModel):
    """Вердикт критика по одной связи. Ничего в базе не меняет."""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    membership_id: int
    recommended_decision: Literal[
        "approve", "alternative", "hard_only", "reject", "manual_review"
    ]
    corrected_fit_score: Score | None = None
    corrected_obviousness_score: Score | None = None
    issues: list[str] = Field(default_factory=list)
    explanation: str = ""


class AdversarialReviewOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    verdicts: list[AdversarialVerdict] = Field(default_factory=list)
