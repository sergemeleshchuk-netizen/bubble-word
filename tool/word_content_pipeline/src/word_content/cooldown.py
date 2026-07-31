"""Cooldown: через сколько уровней элемент можно повторить.

Зачем это в базе, а не в голове дизайнера. Кампания на тысячу уровней собирается
из полутора тысяч категорий. Без учёта повторов генератор честно выберет самые
удобные категории и поставит `FRUITS` в каждый пятый уровень: формально всё
корректно, играть невозможно.

Модуль отвечает на два вопроса:
  * когда элемент использовался в последний раз (по истории уровней);
  * не нарушает ли уровень-кандидат правила повторов.

Полная кампания здесь не собирается — для этого нужен планировщик. Здесь
схема, конфиг, валидатор и история использования.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

DEFAULTS: dict[str, int] = {
    "same_word_sense": 20,
    "same_category_variant": 60,
    "same_category_concept": 40,
    "same_quartet": 120,
    "forbid_duplicate_display_in_level": 1,
    "forbid_duplicate_category_label_in_level": 1,
    "forbid_conflicting_categories_in_level": 1,
}


class ConfigError(ValueError):
    """Конфиг cooldown нельзя прочитать однозначно."""


def default_path() -> Path | None:
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "data" / "content" / "cooldown_config.yaml"
        if candidate.exists():
            return candidate
    return None


def load_config(path: Path | str | None = None) -> dict[str, int]:
    """Читает плоский конфиг `ключ: число`.

    Парсер намеренно строгий и не тянет зависимость: конфиг плоский, а частично
    прочитанный конфиг опаснее непрочитанного — он молча меняет правила.
    """
    file_path = Path(path) if path else default_path()
    values = dict(DEFAULTS)
    if file_path is None:
        return values
    if not file_path.exists():
        raise ConfigError(f"Конфиг cooldown не найден: {file_path}")

    for number, raw in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            raise ConfigError(f"{file_path}:{number}: ожидалось «ключ: число», получено {raw!r}")
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if key not in DEFAULTS:
            raise ConfigError(
                f"{file_path}:{number}: неизвестный ключ {key!r}. "
                f"Разрешены: {', '.join(sorted(DEFAULTS))}"
            )
        try:
            values[key] = int(value)
        except ValueError as exc:
            raise ConfigError(f"{file_path}:{number}: {value!r} — не целое число") from exc
        if values[key] < 0:
            raise ConfigError(f"{file_path}:{number}: отрицательный cooldown у {key!r}")
    return values


@dataclass
class UsageHistory:
    """Когда элемент использовался последний раз. Ключ — порядковый номер уровня."""

    word_sense: dict[tuple[int, int | None], int] = field(default_factory=dict)
    category_variant: dict[int, int] = field(default_factory=dict)
    category_concept: dict[int, int] = field(default_factory=dict)
    quartet: dict[int, int] = field(default_factory=dict)
    counts: dict[str, int] = field(default_factory=dict)

    def remember(
        self,
        position: int,
        *,
        word_senses: list[tuple[int, int | None]],
        category_ids: list[int],
        concept_ids: list[int],
        quartet_ids: list[int],
    ) -> None:
        for key in word_senses:
            self.word_sense[key] = position
            self.counts[f"word:{key}"] = self.counts.get(f"word:{key}", 0) + 1
        for category_id in category_ids:
            self.category_variant[category_id] = position
        for concept_id in concept_ids:
            self.category_concept[concept_id] = position
        for quartet_id in quartet_ids:
            self.quartet[quartet_id] = position


def load_history(conn: sqlite3.Connection) -> UsageHistory:
    """История по принятым уровням: отклонённые ничего не занимают."""
    history = UsageHistory()
    levels = list(
        conn.execute(
            "SELECT id FROM level_instances WHERE status = 'accepted' ORDER BY id"
        )
    )
    for position, level in enumerate(levels, start=1):
        rows = list(
            conn.execute(
                """
                SELECT t.word_id AS word_id, t.sense_id AS sense_id,
                       g.category_id AS category_id, g.quartet_id AS quartet_id,
                       c.concept_id AS concept_id
                  FROM level_tokens t
                  JOIN level_groups g ON g.id = t.group_id
                  JOIN categories c   ON c.id = g.category_id
                 WHERE t.level_id = ?
                """,
                (level["id"],),
            )
        )
        history.remember(
            position,
            word_senses=[(int(r["word_id"]), r["sense_id"]) for r in rows],
            category_ids=[int(r["category_id"]) for r in rows],
            concept_ids=[int(r["concept_id"]) for r in rows if r["concept_id"] is not None],
            quartet_ids=[int(r["quartet_id"]) for r in rows if r["quartet_id"] is not None],
        )
    return history


@dataclass(frozen=True)
class Violation:
    kind: str
    detail: str
    since: int
    required: int

    def __str__(self) -> str:
        return f"{self.kind}: {self.detail} — повтор через {self.since} уровней, нужно {self.required}"


def check(
    *,
    position: int,
    history: UsageHistory,
    config: dict[str, int],
    word_senses: list[tuple[int, int | None]],
    category_ids: list[int],
    concept_ids: list[int],
    quartet_ids: list[int],
    labels: list[str],
    displays: list[str],
) -> list[Violation]:
    """Проверяет уровень-кандидат на нарушения правил повторов."""
    violations: list[Violation] = []

    def gap(last: int | None) -> int | None:
        return None if last is None else position - last

    for key in word_senses:
        distance = gap(history.word_sense.get(key))
        if distance is not None and distance < config["same_word_sense"]:
            violations.append(
                Violation("same_word_sense", f"word_id={key[0]} sense_id={key[1]}",
                          distance, config["same_word_sense"])
            )
    for category_id in category_ids:
        distance = gap(history.category_variant.get(category_id))
        if distance is not None and distance < config["same_category_variant"]:
            violations.append(
                Violation("same_category_variant", f"category_id={category_id}",
                          distance, config["same_category_variant"])
            )
    for concept_id in concept_ids:
        distance = gap(history.category_concept.get(concept_id))
        if distance is not None and distance < config["same_category_concept"]:
            violations.append(
                Violation("same_category_concept", f"concept_id={concept_id}",
                          distance, config["same_category_concept"])
            )
    for quartet_id in quartet_ids:
        distance = gap(history.quartet.get(quartet_id))
        if distance is not None and distance < config["same_quartet"]:
            violations.append(
                Violation("same_quartet", f"quartet_id={quartet_id}",
                          distance, config["same_quartet"])
            )

    if config["forbid_duplicate_display_in_level"]:
        lowered = [value.strip().lower() for value in displays]
        for value in sorted({v for v in lowered if lowered.count(v) > 1}):
            violations.append(Violation("duplicate_display_in_level", value, 0, 1))
    if config["forbid_duplicate_category_label_in_level"]:
        lowered = [value.strip().lower() for value in labels]
        for value in sorted({v for v in lowered if lowered.count(v) > 1}):
            violations.append(Violation("duplicate_category_label_in_level", value, 0, 1))

    return violations
