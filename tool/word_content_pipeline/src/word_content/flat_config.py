"""Строгий разбор плоских конфигов вида `ключ: число`.

Зачем свой парсер, а не зависимость. Все конфиги проекта плоские: пороги
повторов, веса формул, ограничения профилей. Полноценный YAML принёс бы
возможность вложенности, которой здесь неоткуда взяться, и вместе с ней —
тихую полуработающую загрузку: неизвестный ключ прочитался бы и был бы
проигнорирован.

Поэтому парсер намеренно строгий. Он падает на неизвестном ключе, на
нечисловом значении, на любой вложенности. Частично прочитанный конфиг
опаснее непрочитанного: он молча меняет правила.

Секции задаются префиксом в самом ключе: `easy_accessible.max_word_chars`.
Так один файл держит несколько профилей, оставаясь плоским.
"""

from __future__ import annotations

from pathlib import Path


class ConfigError(ValueError):
    """Конфиг нельзя прочитать однозначно."""


def parse(
    text: str,
    defaults: dict[str, float],
    *,
    source: str = "<config>",
    allow_prefixes: bool = False,
) -> dict[str, float]:
    """Разбирает плоский конфиг поверх значений по умолчанию.

    `allow_prefixes` разрешает ключи вида `профиль.параметр`: имя после точки
    обязано быть известным, сам префикс — произвольным.
    """
    values = dict(defaults)
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line != line.lstrip():
            raise ConfigError(
                f"{source}:{number}: вложенность не поддерживается — конфиг плоский"
            )
        if ":" not in line:
            raise ConfigError(f"{source}:{number}: ожидалось «ключ: число», получено {raw!r}")

        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if not value:
            raise ConfigError(f"{source}:{number}: у ключа {key!r} нет значения")

        base = key.split(".", 1)[1] if (allow_prefixes and "." in key) else key
        if base not in defaults:
            raise ConfigError(
                f"{source}:{number}: неизвестный параметр {base!r}. "
                f"Разрешены: {', '.join(sorted(defaults))}"
            )
        try:
            values[key] = float(value)
        except ValueError as exc:
            raise ConfigError(f"{source}:{number}: {value!r} — не число") from exc
    return values


def load(
    path: Path | str | None,
    defaults: dict[str, float],
    *,
    allow_prefixes: bool = False,
) -> dict[str, float]:
    """Читает конфиг с диска. Отсутствие пути — значения по умолчанию."""
    if path is None:
        return dict(defaults)
    file_path = Path(path)
    if not file_path.exists():
        raise ConfigError(f"Конфиг не найден: {file_path}")
    return parse(
        file_path.read_text(encoding="utf-8"),
        defaults,
        source=str(file_path),
        allow_prefixes=allow_prefixes,
    )


def find_upwards(relative: str) -> Path | None:
    """Ищет файл конфига вверх по дереву от пакета до корня проекта."""
    for parent in Path(__file__).resolve().parents:
        candidate = parent / relative
        if candidate.exists():
            return candidate
    return None


def sections(values: dict[str, float], known: dict[str, float]) -> dict[str, dict[str, float]]:
    """Разбирает `профиль.параметр` в {профиль: {параметр: значение}}.

    Каждая секция получает полный набор параметров: сначала значения по
    умолчанию, поверх — общие ключи без префикса, поверх — свои.
    """
    common = {key: value for key, value in values.items() if "." not in key}
    names = sorted({key.split(".", 1)[0] for key in values if "." in key})
    result: dict[str, dict[str, float]] = {}
    for name in names:
        merged = dict(known)
        merged.update(common)
        for key, value in values.items():
            prefix, _, base = key.partition(".")
            if prefix == name:
                merged[base] = value
        result[name] = merged
    return result
