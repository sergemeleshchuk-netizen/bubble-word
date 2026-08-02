"""Карта «связь -> значение слова»: один источник для всех путей импорта.

Аудит закрыл дыру «многозначное слово лежит в категории без указанного значения»
для seed-контента: `scripts/build_seed.py` подставляет значение из
`data/seed/_sense_map.json` ещё до импорта. Но импорт AI-прогонов идёт мимо
build_seed, и та же дыра открывалась заново: прогон мета-хабов принёс
`atlas -> GEOGRAPHY CLASS`, `scale -> MAP LEGEND`, `stamp -> GREETING CARD`,
`toast -> DINNER PARTY` без значений — четыре слова, у каждого в базе по 2-5
разных смыслов. Проверка приёмки это поймала и не дала собрать базу.

Поэтому карта читается здесь, в общем коде импорта: любой источник, который
не принёс `sense_key` сам, получает значение из объявленной карты.

Статус связи карта здесь НЕ навязывает. Для seed это делает build_seed
(там карта — часть источника), а связи прогонов получают статус из
`review_decisions.csv` прогона, то есть из ревью, а не из карты.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .normalization import normalize_word


def default_path() -> Path | None:
    """Штатная карта проекта: data/seed/_sense_map.json рядом с корнем пакета."""
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "data" / "seed" / "_sense_map.json"
        if candidate.exists():
            return candidate
    return None


@dataclass(frozen=True)
class SenseAssignment:
    sense_key: str
    definition: str | None
    # Надпись на пузыре для этого значения: `Rose` (имя) против `rose` (цветок).
    # Пусто — значит написание слова от значения не зависит.
    display_text: str | None = None
    is_proper_noun: bool = False
    part_of_speech: str | None = None


@dataclass(frozen=True)
class SenseSpec:
    """Объявленное значение целиком, включая доступность.

    Расширение формата обратно совместимо: файл, где у значения есть только
    `definition`, читается по-прежнему, а незаполненная доступность честно
    становится `unresolved` — то есть в продакшен такое значение не пойдёт,
    пока его не разберут. Молчаливого повышения до `primary` здесь нет.
    """

    sense_key: str
    definition: str | None = None
    part_of_speech: str | None = None
    display_text: str | None = None
    is_proper_noun: bool = False
    sense_kind: str = "lexical"
    dominance_rank: int | None = None
    accessibility_class: str = "unresolved"
    recognition_score: float | None = None
    activation_score: float | None = None
    audience_profile: str | None = None
    quality_source: str | None = None
    quality_confidence: float | None = None


def _spec(sense_key: str, entry: dict) -> SenseSpec:
    rank = entry.get("dominance_rank")
    return SenseSpec(
        sense_key=sense_key,
        definition=entry.get("definition"),
        part_of_speech=entry.get("part_of_speech"),
        display_text=entry.get("display"),
        is_proper_noun=bool(entry.get("is_proper_noun")),
        sense_kind=entry.get("sense_kind") or "lexical",
        dominance_rank=int(rank) if rank is not None else None,
        accessibility_class=entry.get("accessibility_class") or "unresolved",
        recognition_score=entry.get("recognition_score"),
        activation_score=entry.get("activation_score"),
        audience_profile=entry.get("audience_profile"),
        quality_source=entry.get("quality_source"),
        quality_confidence=entry.get("quality_confidence"),
    )


class SenseMap:
    """Значения слов и привязка «слово + категория -> значение»."""

    def __init__(
        self,
        senses: dict[str, dict[str, dict]] | None = None,
        assignments: dict[str, dict[str, str]] | None = None,
        audience_profile: str = "general_en_us_adult",
    ) -> None:
        self._senses = senses or {}
        self._assignments = assignments or {}
        self.audience_profile = audience_profile

    @classmethod
    def load(cls, path: Path | str | None = None) -> SenseMap:
        file_path = Path(path) if path else default_path()
        if file_path is None or not file_path.exists():
            return cls()
        raw = json.loads(file_path.read_text(encoding="utf-8"))

        senses = {
            normalize_word(word): dict(entries)
            for word, entries in (raw.get("senses") or {}).items()
        }
        assignments: dict[str, dict[str, str]] = {}
        for word, by_category in (raw.get("assignments") or {}).items():
            bucket = assignments.setdefault(normalize_word(word), {})
            for category_key, value in by_category.items():
                # в файле допустимы обе формы: "sense_key" и {"sense": ..., ...}
                bucket[category_key] = value if isinstance(value, str) else value["sense"]
        return cls(
            senses,
            assignments,
            audience_profile=raw.get("audience_profile") or "general_en_us_adult",
        )

    def declared_senses(self) -> dict[str, dict[str, SenseSpec]]:
        """Все объявленные значения с оценками доступности."""
        return {
            word: {key: _spec(key, entry) for key, entry in entries.items()}
            for word, entries in self._senses.items()
        }

    def declared_assignments(self) -> dict[str, dict[str, str]]:
        return {word: dict(items) for word, items in self._assignments.items()}

    def lookup(self, word: str, category_key: str) -> SenseAssignment | None:
        """Объявленное значение слова в этой категории, если оно есть."""
        sense_key = self._assignments.get(normalize_word(word), {}).get(category_key)
        if not sense_key:
            return None
        entry = self._senses.get(normalize_word(word), {}).get(sense_key) or {}
        return SenseAssignment(
            sense_key=sense_key,
            definition=entry.get("definition"),
            display_text=entry.get("display"),
            is_proper_noun=bool(entry.get("is_proper_noun")),
            part_of_speech=entry.get("part_of_speech"),
        )

    def senses_for(self, word: str) -> dict[str, dict]:
        """Все объявленные значения слова: нужно для проверки полноты карты."""
        return dict(self._senses.get(normalize_word(word), {}))

    def describe(self, word: str, sense_key: str) -> SenseAssignment | None:
        """Свойства значения по его ключу, без привязки к категории.

        Надпись на пузыре принадлежит значению, а не паре «слово + категория»:
        `Rose` выглядит одинаково в NATURE NAMES и в SHORT NAMES. Поэтому
        источник, принёсший значение сам, всё равно должен получить отсюда
        написание — иначе `display_text` доезжает до базы только у тех связей,
        где значение подставила карта.
        """
        entry = self._senses.get(normalize_word(word), {}).get(sense_key)
        if entry is None:
            return None
        return SenseAssignment(
            sense_key=sense_key,
            definition=entry.get("definition"),
            display_text=entry.get("display"),
            is_proper_noun=bool(entry.get("is_proper_noun")),
            part_of_speech=entry.get("part_of_speech"),
        )


@lru_cache(maxsize=1)
def default_sense_map() -> SenseMap:
    """Карта проекта, прочитанная один раз за процесс."""
    return SenseMap.load()
