"""Профиль композиции уровня: чем уровень N отличается от уровня N+1.

Плоский генератор собирает любой уровень одинаково: N независимых четвёрок.
Запись оригинала так не устроена — состав меняется по номеру уровня:

    уровень  1:  5 категорий, 0 мета, 0 ловушек   — обучение правилам
    уровень  3:  8 категорий, 1 мета, 3 ловушки   — первая мета за всю игру
    уровень  7: 12 категорий, 6 мета, 4 ловушки   — пик первой десятки
    уровень 10:  8 категорий, 0 мета, 3 ловушки   — передышка перед второй
    уровень 17: 11 категорий, 6 мета, 6 ловушек

Числа не выдуманы: они снимаются прямо с `data/reference/video-levels-20.json`
через `reference_fixtures`. Своей таблицы-копии здесь нет намеренно — копия
разошлась бы с записью на первой же правке разбора.

За двадцатым уровнем запись кончается, и профиль честно помечает себя как
`extrapolated`: берётся среднее последних пяти уровней. Выдавать продолжение
кривой за наблюдение нельзя — это ровно та подмена, ради запрета которой
разделены `observed` и `inferred` во всём остальном проекте.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from . import reference_fixtures

# Сколько последних записанных уровней усредняется для продолжения кривой.
TAIL_WINDOW = 5
# Потолок доли мета-связей: больше половины групп в связке не встречается
# и в записи (максимум — уровень 14: 6 связей на 10 категорий).
MAX_META_SHARE = 0.6
# Самый населённый уровень записи: 12 категорий (уровни 7, 8, 11, 12).
MAX_RECORDED_CATEGORIES = 12

# Профиль качества по номеру уровня. Границы полос сняты замером: средняя
# знакомость слов записи по уровням падает с 0.691 на первом до 0.52-0.55 на
# 14-17, и минимальная — с 0.569 (на первом уровне нет ни одного трудного
# слова) до 0.19 на четвёртом.
#
#   уровни  1-3   avg 0.62-0.69  ->  easy_accessible (порог средней 0.64)
#   уровни  4-13  avg 0.54-0.64  ->  accessible_fun  (порог средней 0.58)
#   уровни 14+    avg 0.52-0.55  ->  hard_knowledge  (порог средней 0.42)
#
# Кривая записи не строго монотонна — на 18-20 знакомость снова растёт до 0.59.
# Здесь она сделана монотонной сознательно: кампания идёт дальше двадцатого
# уровня, а хвост записи снят частично (L18 — семь групп из одиннадцати).
PROFILE_BANDS: tuple[tuple[int, str], ...] = (
    (3, "easy_accessible"),
    (13, "accessible_fun"),
)
LATE_PROFILE = "hard_knowledge"


@dataclass(frozen=True)
class Composition:
    """Опорный состав одного уровня."""

    number: int
    categories: int
    meta_links: int
    traps: int
    source: str  # recorded | extrapolated

    @property
    def recorded(self) -> bool:
        return self.source == "recorded"

    @property
    def profile(self) -> str:
        """Профиль качества слов для этого номера уровня."""
        for last_number, name in PROFILE_BANDS:
            if self.number <= last_number:
                return name
        return LATE_PROFILE

    def meta_target(self, categories: int) -> int:
        """Сколько мета-связей просить, если категорий в уровне столько-то.

        Генератор часто зовут с меньшим числом категорий, чем в записи, — на
        пяти категориях шесть мета-связей означали бы уровень, который весь
        состоит из ожидания. Доля сохраняется, потолок остаётся.
        """
        if self.meta_links <= 0 or categories < 3 or self.categories <= 0:
            return 0
        scaled = round(self.meta_links * categories / self.categories)
        return max(1, min(scaled, int(categories * MAX_META_SHARE)))

    def as_dict(self) -> dict[str, object]:
        return {
            "number": self.number,
            "categories": self.categories,
            "meta_links": self.meta_links,
            "traps": self.traps,
            "profile": self.profile,
            "source": self.source,
        }


@lru_cache(maxsize=4)
def _recorded(path: str | None = None) -> dict[int, Composition]:
    fixtures = reference_fixtures.load(Path(path) if path else None)
    table: dict[int, Composition] = {}
    for level in fixtures.levels:
        table[level.number] = Composition(
            number=level.number,
            # Именно `groups_expected`: на уровне 18 в кадр попали семь групп
            # из одиннадцати, но уровень был одиннадцатикатегорийным.
            categories=level.groups_expected,
            meta_links=len(level.meta_links),
            traps=len(level.traps),
            source="recorded",
        )
    return table


def table(path: str | Path | None = None) -> dict[int, Composition]:
    """Записанная часть кривой: номер уровня -> состав."""
    return dict(_recorded(str(path) if path else None))


def for_level(number: int, path: str | Path | None = None) -> Composition:
    """Состав уровня по его номеру в кривой. За записью — продолжение."""
    recorded = _recorded(str(path) if path else None)
    if number in recorded:
        return recorded[number]
    if not recorded:
        raise reference_fixtures.FixtureError(
            "профиль композиции не построить: запись референса пуста"
        )
    last = sorted(recorded)[-TAIL_WINDOW:]
    tail = [recorded[key] for key in last]
    return Composition(
        number=number,
        categories=round(sum(item.categories for item in tail) / len(tail)),
        meta_links=round(sum(item.meta_links for item in tail) / len(tail)),
        traps=round(sum(item.traps for item in tail) / len(tail)),
        source="extrapolated",
    )
