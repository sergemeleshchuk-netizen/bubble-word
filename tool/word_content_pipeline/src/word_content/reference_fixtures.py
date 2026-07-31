"""Уровни референса как неизменяемые fixtures.

Единственное место в проекте, где ответ известен заранее: двадцать уровней
оригинала, снятых с собственных записей геймплея и разобранных покадрово
(`reference/video-levels-20.json`). Всё остальное — наши предположения.

Модуль читает запись **без потерь** и без нормализации под текущую онтологию.
Это принципиально: если разбор начнёт «чинить» запись под базу, измерять станет
нечем. Поэтому здесь нет ни одного обращения к SQLite.

Что различается и никогда не смешивается:

``label_source``
    ``observed``  — имя прочитано с оранжевого пузыря, это ground truth;
    ``inferred``  — наша формулировка по четвёрке слов. Четвёрка при этом
                    ground truth, а имя — нет.

``observability`` слота
    ``observed``  — пузырь виден в кадре;
    ``unseen``    — категория собралась между кадрами, сам пузырь не снят.
                    Такой слот нельзя выдавать за наблюдение.

``token_kind``
    ``lexical_word`` | ``picture_token`` | ``chunked_word`` | ``category_output``.
    ``category_output`` — не слово, а результат другой категории этого уровня:
    он появляется на поле только после того, как та категория собрана.
    Форма (слово или картинка) хранится отдельно в ``token_form``.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .normalization import normalize_word

# Значение поля name_source в записи, означающее прочитанное имя категории.
OBSERVED_NAME_SOURCE = "видно на оранжевом пузыре"

TOKEN_KINDS = ("lexical_word", "picture_token", "chunked_word", "category_output")
TOKEN_FORMS = ("word", "picture", "chunks", "unknown")
OBSERVABILITY = ("observed", "unseen")
LABEL_SOURCES = ("observed", "inferred")

QUARTET_SIZE = 4


def normalize_name(value: str | None) -> str:
    """Нормализация ИМЕНИ категории для сравнения: только буквы, цифры и пробел."""
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def normalize_token(value: str) -> str:
    """Нормализация ТОКЕНА — ровно та же, по которой живут слова в базе.

    Разные нормализации для одного и того же слова уже стоили одного сорванного
    импорта: `hot-air balloon` в базе хранится с дефисом, а имя категории
    сравнивается без него. Токен нормализуется только этой функцией.
    """
    return normalize_word(value)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (value or "").lower()).strip("_")


@dataclass(frozen=True)
class FixtureSlot:
    """Один пузырь категории ровно так, как он записан."""

    position: int
    text: str
    token_kind: str
    token_form: str
    observability: str
    pieces: tuple[str, ...] = ()
    # Имя категории того же уровня, которая выпускает этот токен (для category_output).
    emitted_by: str | None = None

    @property
    def normalized(self) -> str:
        return normalize_token(self.text)

    @property
    def is_meta(self) -> bool:
        return self.token_kind == "category_output"

    def as_dict(self) -> dict[str, object]:
        return {
            "position": self.position,
            "text": self.text,
            "token_kind": self.token_kind,
            "token_form": self.token_form,
            "observability": self.observability,
            "pieces": list(self.pieces),
            "emitted_by": self.emitted_by,
        }


@dataclass(frozen=True)
class FixtureGroup:
    """Категория уровня: точная четвёрка + имя с указанием, откуда имя взято."""

    index: int
    name: str
    label_source: str
    slots: tuple[FixtureSlot, ...]

    @property
    def normalized_name(self) -> str:
        return normalize_name(self.name)

    @property
    def observed_label(self) -> bool:
        return self.label_source == "observed"

    @property
    def words(self) -> tuple[str, ...]:
        return tuple(slot.text for slot in self.slots)

    @property
    def quartet_signature(self) -> tuple[str, ...]:
        """Отпечаток четвёрки: отсортированные нормализованные токены."""
        return tuple(sorted(slot.normalized for slot in self.slots))

    def as_dict(self) -> dict[str, object]:
        return {
            "index": self.index,
            "name": self.name,
            "label_source": self.label_source,
            "slots": [slot.as_dict() for slot in self.slots],
        }


@dataclass(frozen=True)
class FixtureMetaLink:
    """Ссылка «собранная категория выпускает токен для другой категории»."""

    token: str
    form: str
    target_group: str  # категория, которой этот токен нужен (belongs_to)
    source_group: str  # категория, которая его выпускает (also_category_on_level)

    def as_dict(self) -> dict[str, object]:
        return {
            "token": self.token,
            "form": self.form,
            "target_group": self.target_group,
            "source_group": self.source_group,
        }


@dataclass(frozen=True)
class FixtureLevel:
    number: int
    completeness: str  # full | partial
    groups_expected: int
    groups: tuple[FixtureGroup, ...]
    meta_links: tuple[FixtureMetaLink, ...]
    board: dict[str, object] = field(default_factory=dict)
    modifiers: tuple[str, ...] = ()
    traps: tuple[str, ...] = ()
    notes: str = ""

    @property
    def level_key(self) -> str:
        return f"REF{self.number:03d}"

    @property
    def slots(self) -> list[FixtureSlot]:
        return [slot for group in self.groups for slot in group.slots]

    @property
    def fully_recorded(self) -> bool:
        return self.completeness == "full" and len(self.groups) == self.groups_expected

    def group_by_name(self, name: str) -> FixtureGroup | None:
        target = normalize_name(name)
        for group in self.groups:
            if group.normalized_name == target:
                return group
        return None

    def as_dict(self) -> dict[str, object]:
        return {
            "level": self.number,
            "completeness": self.completeness,
            "groups_expected": self.groups_expected,
            "groups": [group.as_dict() for group in self.groups],
            "meta_links": [link.as_dict() for link in self.meta_links],
            "modifiers": list(self.modifiers),
        }


@dataclass(frozen=True)
class ReferenceFixtures:
    source_file: str
    levels: tuple[FixtureLevel, ...]

    def upto(self, max_level: int | None) -> list[FixtureLevel]:
        if max_level is None:
            return list(self.levels)
        return [level for level in self.levels if level.number <= max_level]

    def get(self, number: int) -> FixtureLevel:
        for level in self.levels:
            if level.number == number:
                return level
        raise KeyError(f"уровня {number} нет в записи")


class FixtureError(RuntimeError):
    """Запись не разбирается. Чинить надо запись, а не подгонять разбор."""


def default_path() -> Path:
    """Канонический путь записи.

    Раньше файл лежал рядом с видео в `/reference/`, а эта папка целиком в
    `.gitignore` — то есть обязательный regression dataset был невидим для
    репозитория. Файл, от которого зависит приёмка, обязан коммититься,
    поэтому канонический путь теперь внутри `data/`.
    """
    here = Path(__file__).resolve()
    canonical = here.parents[2] / "data" / "reference" / "video-levels-20.json"
    if canonical.exists():
        return canonical
    for parent in here.parents:  # исторический путь, на случай старых копий
        candidate = parent / "reference" / "video-levels-20.json"
        if candidate.exists():
            return candidate
    return canonical


def load(path: Path | str | None = None) -> ReferenceFixtures:
    """Читает запись целиком. Ни одна наблюдавшаяся группа не теряется."""
    source = Path(path) if path is not None else default_path()
    if not source.exists():
        raise FixtureError(
            f"записи референса нет: {source}. "
            "Это обязательный regression dataset, без него нечем измерять."
        )
    raw = json.loads(source.read_text(encoding="utf-8"))
    coverage = raw.get("coverage") or {}
    partial: dict[str, str] = coverage.get("partially_recorded") or {}

    levels: list[FixtureLevel] = []
    for entry in raw.get("levels") or []:
        levels.append(_parse_level(entry, partial_note=partial.get(str(entry.get("level")))))
    levels.sort(key=lambda level: level.number)
    return ReferenceFixtures(source_file=source.name, levels=tuple(levels))


def _parse_level(entry: dict, *, partial_note: str | None) -> FixtureLevel:
    number = int(entry["level"])
    expected = int(entry.get("categories_count") or len(entry.get("categories") or []))
    recorded = int(entry.get("categories_recorded") or len(entry.get("categories") or []))

    meta_links = tuple(
        FixtureMetaLink(
            token=str(link["token"]),
            form=str(link.get("form") or "word"),
            target_group=str(link["belongs_to"]),
            source_group=str(link.get("also_category_on_level") or link["token"]),
        )
        for link in entry.get("meta_links") or []
    )
    # Токен уровня -> кто его выпускает. Ключ нормализован: в записи имена
    # категорий и текст токена пишутся одинаково, но регистр не гарантирован.
    meta_by_token = {normalize_token(link.token): link for link in meta_links}

    pieces_by_word = {
        normalize_token(item["word"]): tuple(str(piece) for piece in item.get("pieces") or ())
        for item in entry.get("chunked_words") or []
    }

    groups: list[FixtureGroup] = []
    for index, category in enumerate(entry.get("categories") or [], start=1):
        words = list(category.get("words") or [])
        if len(words) != QUARTET_SIZE:
            raise FixtureError(
                f"уровень {number}, категория {category.get('name')!r}: "
                f"{len(words)} слов вместо {QUARTET_SIZE}. "
                "Запись не подгоняется — правится сама запись."
            )
        forms = category.get("forms") or {}
        slots: list[FixtureSlot] = []
        for position, word in enumerate(words, start=1):
            raw_form = str(forms.get(word) or "word")
            key = normalize_token(word)
            meta = meta_by_token.get(key)
            observability = "unseen" if raw_form == "unseen" else "observed"
            if raw_form == "unseen":
                token_form = "unknown"
            elif raw_form in TOKEN_FORMS:
                token_form = raw_form
            else:
                raise FixtureError(
                    f"уровень {number}: неизвестная форма {raw_form!r} у слова {word!r}"
                )
            # meta-форма записана и в meta_links, и в forms; при расхождении
            # верим forms — это то, что видно на пузыре.
            if meta is not None and token_form == "word" and meta.form == "picture":
                token_form = "picture"
            if meta is not None:
                token_kind = "category_output"
            elif token_form == "picture":
                token_kind = "picture_token"
            elif token_form == "chunks":
                token_kind = "chunked_word"
            else:
                token_kind = "lexical_word"
            pieces = pieces_by_word.get(key, ()) if token_form == "chunks" else ()
            if token_form == "chunks" and not pieces:
                raise FixtureError(
                    f"уровень {number}: слово {word!r} помечено chunks, но кусочков нет"
                )
            slots.append(
                FixtureSlot(
                    position=position,
                    text=str(word),
                    token_kind=token_kind,
                    token_form=token_form,
                    observability=observability,
                    pieces=pieces,
                    emitted_by=meta.source_group if meta is not None else None,
                )
            )
        name_source = str(category.get("name_source") or "")
        groups.append(
            FixtureGroup(
                index=index,
                name=str(category["name"]),
                label_source=(
                    "observed" if name_source == OBSERVED_NAME_SOURCE else "inferred"
                ),
                slots=tuple(slots),
            )
        )

    if len(groups) != recorded:
        raise FixtureError(
            f"уровень {number}: записано {len(groups)} категорий, "
            f"а categories_recorded говорит {recorded}"
        )
    completeness = "partial" if (partial_note or recorded < expected) else "full"

    return FixtureLevel(
        number=number,
        completeness=completeness,
        groups_expected=expected,
        groups=tuple(groups),
        meta_links=meta_links,
        board=dict(entry.get("board") or {}),
        modifiers=tuple(str(item) for item in entry.get("modifiers") or ()),
        traps=tuple(str(item) for item in entry.get("traps") or ()),
        notes=str(entry.get("notes") or ""),
    )


def totals(levels: list[FixtureLevel]) -> dict[str, int]:
    """Счётчики записи. Именно с ними сравнивается всё, что делает база."""
    groups = [group for level in levels for group in level.groups]
    slots = [slot for group in groups for slot in group.slots]
    return {
        "levels": len(levels),
        "levels_fully_recorded": sum(1 for level in levels if level.fully_recorded),
        "groups_expected": sum(level.groups_expected for level in levels),
        "groups_recorded": len(groups),
        "slots": len(slots),
        "observed_labels": sum(1 for group in groups if group.observed_label),
        "inferred_labels": sum(1 for group in groups if not group.observed_label),
        "meta_links": sum(len(level.meta_links) for level in levels),
        "unseen_slots": sum(1 for slot in slots if slot.observability == "unseen"),
        "picture_tokens": sum(1 for slot in slots if slot.token_form == "picture"),
        "chunked_tokens": sum(1 for slot in slots if slot.token_form == "chunks"),
        "category_output_tokens": sum(1 for slot in slots if slot.is_meta),
        "distinct_quartets": len({group.quartet_signature for group in groups}),
        "distinct_labels": len({group.normalized_name for group in groups}),
        "distinct_tokens": len({slot.normalized for slot in slots}),
    }
