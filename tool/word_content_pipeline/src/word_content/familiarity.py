"""Оценка известности слова через частотность (zipf).

Зачем: на масштабе AI и ручная генерация тащат редкие слова (okra, oxbow, thimble).
Средний игрок их не узнает, а формально связь корректна — фильтр по частотности
ловит это раньше, чем контент попадёт в уровень.

Шкала zipf (wordfreq): 7 — "the", 5 — "apple" уровня очень частых, 4 — обычное слово,
3 — заметно реже, ниже 2.5 — редкое. Частотность != узнаваемость (jackhammer знают все,
а zipf у него 2.3), поэтому по умолчанию это предупреждение, а не запрет.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from .normalization import normalize_word

ZIPF_MAX = 7.0
DEFAULT_MIN_ZIPF = 2.5  # значение по умолчанию для флага --min-zipf

_SPLIT_RE = re.compile(r"[ \-']+")
_cache: dict[str, float] | None = None


@lru_cache(maxsize=1)
def _wordfreq_zipf():
    """wordfreq — необязательная зависимость: без неё работает кэш частотностей."""
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        return None
    return zipf_frequency


def load_cache(path: Path | None) -> None:
    """Подключает заранее посчитанный файл частотностей (когда wordfreq не установлен)."""
    global _cache
    if path is None or not Path(path).exists():
        _cache = None
        return
    _cache = json.loads(Path(path).read_text(encoding="utf-8"))


def zipf(word: str) -> float | None:
    """Частотность слова или фразы. None, если посчитать нечем."""
    try:
        normalized = normalize_word(word)
    except Exception:
        return None

    if _cache is not None and normalized in _cache:
        return float(_cache[normalized])

    zipf_frequency = _wordfreq_zipf()
    if zipf_frequency is None:
        return None

    value = float(zipf_frequency(normalized, "en"))
    if value > 0:
        return value

    # Фраза целиком не найдена — оцениваем по самому редкому слову в ней.
    parts = [p for p in _SPLIT_RE.split(normalized) if p]
    if len(parts) > 1:
        values = [float(zipf_frequency(part, "en")) for part in parts]
        values = [v for v in values if v > 0]
        if values:
            return min(values)
    return value or None


def familiarity(word: str) -> float | None:
    """Частотность, приведённая к диапазону 0..1 для поля familiarity_score."""
    value = zipf(word)
    if value is None:
        return None
    return round(min(max(value, 0.0), ZIPF_MAX) / ZIPF_MAX, 3)


def is_rare(word: str, min_zipf: float = DEFAULT_MIN_ZIPF) -> bool:
    """True, если слово реже порога. Неизвестная частотность редкой не считается."""
    value = zipf(word)
    return value is not None and value < min_zipf


def build_cache(words: list[str]) -> dict[str, float]:
    """Считает частотности для списка слов (для выгрузки в файл кэша)."""
    result: dict[str, float] = {}
    for word in words:
        value = zipf(word)
        if value is not None:
            result[normalize_word(word)] = round(value, 3)
    return result
