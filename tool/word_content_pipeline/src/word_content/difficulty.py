"""Модель сложности уровня: объяснимая эвристика, а не чёрный ящик.

Оценка нужна, чтобы раскладывать уровни по кривой прогрессии. Поэтому важнее
не точность до десятой доли, а объяснение: почему именно столько. Каждый
компонент считается отдельно и печатается в отчёте — уровень, получивший 8,
обязан уметь показать, за что.

Шкала 1–10 та же, что у ручной оценки в `levels/EVAL.md`, и компоненты названы
так же, где совпадают. Это не прогноз win rate: телеметрии нет, и называть
эвристику прогнозом было бы враньём.
"""

from __future__ import annotations

from dataclasses import dataclass, field

MODEL_VERSION = "difficulty-heuristic/1.0"

# Частотность ниже этого порога считается редким словом. 0.357 = zipf 2.5 / 7.
RARE_FAMILIARITY = 0.43  # ~zipf 3.0, как F4 в levels/EVAL.md


@dataclass
class LevelFacts:
    """Всё, что модель знает об уровне. Считается один раз при сборке."""

    category_count: int
    total_tokens: int
    familiarity_scores: list[float] = field(default_factory=list)
    # сколько токенов уровня имеют более одного значения в базе
    ambiguous_tokens: int = 0
    # пары категорий уровня, чьи пулы пересекаются, и размер пересечения
    pairwise_overlaps: list[int] = field(default_factory=list)
    # сколько альтернативных четвёрок нашёл solver помимо задуманных
    alternative_interpretations: int = 0
    # сколько групп игрок может собрать «с ходу» — из четырёх самых частотных слов
    plausible_first_groups: int = 0
    structured_categories: int = 0
    max_phrase_length: int = 1
    meta_depth: int = 0

    @property
    def average_familiarity(self) -> float:
        return (
            sum(self.familiarity_scores) / len(self.familiarity_scores)
            if self.familiarity_scores
            else 0.0
        )

    @property
    def rare_word_count(self) -> int:
        return sum(1 for value in self.familiarity_scores if value < RARE_FAMILIARITY)


@dataclass
class DifficultyScore:
    total_score: float
    component_scores: dict[str, float]
    model_version: str
    short_explanation: str


def score(facts: LevelFacts) -> DifficultyScore:
    """Складывает компоненты в оценку 1–10 и объясняет вклад каждого."""
    components: dict[str, float] = {}

    # Масштаб: чем больше категорий, тем больше держать в голове.
    count = facts.category_count
    components["category_count"] = (
        0.0 if count <= 6 else 1.0 if count <= 8 else 1.5 if count <= 10 else 2.5
    )

    # Незнакомые слова: игрок не может проверить догадку.
    components["rare_words"] = min(1.0, 0.5 * facts.rare_word_count)
    average = facts.average_familiarity
    components["average_familiarity"] = (
        1.0 if average and average < 0.45 else 0.5 if average and average < 0.55 else 0.0
    )

    # Многозначность: одно и то же слово тянет в две стороны.
    components["sense_ambiguity"] = min(1.5, 0.5 * facts.ambiguous_tokens)

    # Смежные категории: пересекающиеся пулы заставляют сомневаться на границе.
    close_pairs = sum(1 for overlap in facts.pairwise_overlaps if overlap >= 2)
    components["pairwise_category_overlap"] = min(1.5, 0.75 * close_pairs)

    # Давление альтернативных разбиений: сколько ложных ходов доступно игроку.
    components["alternative_partition_pressure"] = min(1.5, 0.25 * facts.alternative_interpretations)

    # Доступный первый ход: уровень без очевидного входа ощущается тяжелее.
    first = facts.plausible_first_groups
    components["number_of_plausible_first_groups"] = (
        1.0 if first == 0 else 0.5 if first == 1 else 0.0
    )

    components["structured_category_complexity"] = min(1.0, 0.5 * facts.structured_categories)
    components["phrase_length_pressure"] = 0.5 if facts.max_phrase_length > 2 else 0.0
    components["meta_depth"] = min(1.5, 0.75 * facts.meta_depth)

    total = 1.0 + sum(components.values())
    total = max(1.0, min(10.0, round(total * 2) / 2))

    top = sorted(components.items(), key=lambda item: -item[1])[:3]
    reasons = [f"{name} +{value}" for name, value in top if value > 0]
    explanation = (
        f"{count} категорий, {facts.total_tokens} слов; "
        + ("главный вклад: " + ", ".join(reasons) if reasons else "все компоненты нулевые")
    )
    return DifficultyScore(
        total_score=total,
        component_scores={k: round(v, 3) for k, v in components.items()},
        model_version=MODEL_VERSION,
        short_explanation=explanation,
    )
