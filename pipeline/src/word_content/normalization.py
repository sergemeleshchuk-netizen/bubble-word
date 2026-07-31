"""Нормализация слов и ключей категорий."""

from __future__ import annotations

import re
import unicodedata

MAX_WORD_LENGTH = 50

# Типографские апострофы -> обычный ', типографские тире/дефисы -> обычный -
APOSTROPHES = "‘’‛ʼ′´`"
HYPHENS = "‐‑‒–—―−­"

_TRANSLATION = {ord(ch): "'" for ch in APOSTROPHES}
_TRANSLATION.update({ord(ch): "-" for ch in HYPHENS})

_WHITESPACE_RE = re.compile(r"\s+")
CATEGORY_KEY_RE = re.compile(r"^[a-z_][a-z0-9_]*$")


class NormalizationError(ValueError):
    """Слово нельзя привести к валидной нормальной форме."""


def normalize_word(raw: str) -> str:
    """Приводит слово к канонической форме для сравнения и дедупликации.

    Unicode NFKC -> унификация апострофов и дефисов -> trim -> lowercase ->
    схлопывание пробелов. Апострофы и дефисы сохраняются.
    """
    if raw is None:
        raise NormalizationError("Слово не может быть None")
    if not isinstance(raw, str):
        raise NormalizationError(f"Ожидалась строка, получено {type(raw).__name__}")

    text = unicodedata.normalize("NFKC", raw)
    text = text.translate(_TRANSLATION)
    text = _WHITESPACE_RE.sub(" ", text).strip().lower()

    if not text:
        raise NormalizationError("Пустое слово после нормализации")
    if len(text) > MAX_WORD_LENGTH:
        raise NormalizationError(
            f"Слово длиннее {MAX_WORD_LENGTH} символов: {text[:60]!r}"
        )
    return text


def clean_display_text(raw: str) -> str:
    """Исходное написание слова: только NFKC, унификация знаков и trim (регистр сохраняем)."""
    text = unicodedata.normalize("NFKC", raw or "")
    text = text.translate(_TRANSLATION)
    return _WHITESPACE_RE.sub(" ", text).strip()


def is_valid_category_key(key: str) -> bool:
    """lowercase, латиница/цифры/подчёркивание, не начинается с цифры, без пробелов."""
    return bool(key) and bool(CATEGORY_KEY_RE.match(key))


def normalize_sense_key(raw: str) -> str:
    """Ключ значения: нижний регистр, пробелы и дефисы -> подчёркивание."""
    text = unicodedata.normalize("NFKC", raw).translate(_TRANSLATION).strip().lower()
    text = _WHITESPACE_RE.sub("_", text)
    return text.replace("-", "_")
