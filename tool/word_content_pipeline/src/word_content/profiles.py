"""Профили генерации: чем именно управляет генератор.

Без профиля генератор честно возьмёт самые удобные четвёрки — с максимальной
частотностью и максимальной связностью. Уровни получатся понятными и
совершенно скучными: четыре банальных слова в каждой группе.

Профиль задаёт обе оси сразу. Пороги понятности (`*_min`) отсекают то, во что
играть невозможно. Целевая интересность (`quartet_interest_target`) и бюджеты
(`rare_word_budget`, `ambiguity_budget`, `long_phrase_budget`) удерживают
уровень от скатывания в банальность.

Бюджет — это не запрет, а разрешённое количество. Одно менее очевидное слово
в группе делает уровень интереснее; четыре редких делают его непроходимым.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import flat_config

# Параметр -> значение по умолчанию. Профиль, не задавший параметр, получает его.
DEFAULTS: dict[str, float] = {
    "word_familiarity_min": 0.0,
    "word_familiarity_avg_min": 0.0,
    "word_accessibility_min": 0.0,
    "max_word_chars": 99,
    "max_word_tokens": 9,
    "max_label_chars": 99,
    "max_label_tokens": 9,
    "label_quality_min": 0.0,
    "quartet_quality_min": 0.0,
    "quartet_interest_target": 0.0,
    "ambiguity_budget": 1.0,
    "rare_word_budget": 99,
    "long_phrase_budget": 99,
    "novel_words_target_ratio": 0.0,
}


@dataclass(frozen=True)
class Profile:
    name: str
    values: dict[str, float]

    def __getitem__(self, key: str) -> float:
        return self.values[key]

    def as_dict(self) -> dict[str, float]:
        return dict(self.values)


def default_path() -> Path | None:
    return flat_config.find_upwards("data/content/generation_profiles.yaml")


def load(path: Path | str | None = None) -> dict[str, Profile]:
    """Читает все профили из конфига."""
    file_path = Path(path) if path else default_path()
    if file_path is None:
        return {"default": Profile(name="default", values=dict(DEFAULTS))}
    values = flat_config.load(file_path, DEFAULTS, allow_prefixes=True)
    sections = flat_config.sections(values, DEFAULTS)
    if not sections:
        return {"default": Profile(name="default", values=values)}
    return {name: Profile(name=name, values=data) for name, data in sections.items()}


def get(name: str, path: Path | str | None = None) -> Profile:
    profiles = load(path)
    if name not in profiles:
        raise flat_config.ConfigError(
            f"Профиль {name!r} не найден. Есть: {', '.join(sorted(profiles))}"
        )
    return profiles[name]


@dataclass(frozen=True)
class QuartetFacts:
    """Что профиль знает о четвёрке-кандидате."""

    quartet_key: str
    min_familiarity: float | None
    avg_familiarity: float | None
    min_accessibility: float | None
    max_word_chars: int
    max_word_tokens: int
    label_chars: int
    label_tokens: int
    label_quality: float | None
    quartet_quality: float | None
    quartet_interest: float | None
    ambiguity: float | None
    rare_words: int
    long_phrases: int


def check_quartet(profile: Profile, facts: QuartetFacts) -> list[str]:
    """Причины, по которым четвёрка не подходит профилю. Пусто — подходит.

    Неизвестные значения не пропускаются молча: если частотность не посчитана,
    четвёрка не проходит порог знакомости. Пропущенные данные должны закрывать
    путь в уровень, а не считаться нулём и тем более не считаться успехом.
    """
    reasons: list[str] = []

    def below(value: float | None, key: str, label: str) -> None:
        threshold = profile[key]
        if threshold <= 0:
            return
        if value is None:
            reasons.append(f"{label} не посчитана, порог {threshold}")
        elif value < threshold:
            reasons.append(f"{label} {value:.2f} < {threshold}")

    below(facts.min_familiarity, "word_familiarity_min", "минимальная знакомость")
    below(facts.avg_familiarity, "word_familiarity_avg_min", "средняя знакомость")
    below(facts.min_accessibility, "word_accessibility_min", "минимальная доступность")
    below(facts.label_quality, "label_quality_min", "качество названия")
    below(facts.quartet_quality, "quartet_quality_min", "качество четвёрки")

    if facts.max_word_chars > profile["max_word_chars"]:
        reasons.append(
            f"слово в {facts.max_word_chars} символов > {int(profile['max_word_chars'])}"
        )
    if facts.max_word_tokens > profile["max_word_tokens"]:
        reasons.append(
            f"фраза из {facts.max_word_tokens} слов > {int(profile['max_word_tokens'])}"
        )
    if facts.label_chars > profile["max_label_chars"]:
        reasons.append(
            f"название в {facts.label_chars} символов > {int(profile['max_label_chars'])}"
        )
    if facts.label_tokens > profile["max_label_tokens"]:
        reasons.append(
            f"название из {facts.label_tokens} слов > {int(profile['max_label_tokens'])}"
        )
    if facts.ambiguity is not None and facts.ambiguity > profile["ambiguity_budget"]:
        reasons.append(
            f"неоднозначность {facts.ambiguity:.2f} > бюджета {profile['ambiguity_budget']}"
        )
    return reasons


@dataclass
class LevelBudget:
    """Бюджеты уровня: сколько «дорогого» контента ещё можно потратить."""

    rare_words: int
    long_phrases: int

    @classmethod
    def for_profile(cls, profile: Profile) -> LevelBudget:
        return cls(
            rare_words=int(profile["rare_word_budget"]),
            long_phrases=int(profile["long_phrase_budget"]),
        )

    def fits(self, facts: QuartetFacts) -> str | None:
        if facts.rare_words > self.rare_words:
            return (
                f"редких слов {facts.rare_words}, в бюджете уровня осталось {self.rare_words}"
            )
        if facts.long_phrases > self.long_phrases:
            return (
                f"длинных фраз {facts.long_phrases}, "
                f"в бюджете уровня осталось {self.long_phrases}"
            )
        return None

    def spend(self, facts: QuartetFacts) -> None:
        self.rare_words -= facts.rare_words
        self.long_phrases -= facts.long_phrases
