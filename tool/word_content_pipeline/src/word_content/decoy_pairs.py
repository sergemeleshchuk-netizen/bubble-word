"""Ловушки: какое слово можно нарочно поставить между двумя группами уровня.

Мета-пары научили генератор строить связи между группами. Ловушек он до сих пор
не строил вовсе — наоборот, старательно их избегал: любое слово, подходящее
сразу двум правилам уровня, отклонялось валидатором как незапланированное
пересечение. Формально правильно, по игре — катастрофа. Замер двадцатки:
25 честных ловушек в записи оригинала против 4 у нас, 20 ага-моментов против
нуля, и полный балл фана разницы (`levels/eval/reference-vs-remake.md`).

Оригинал на пересечениях держится. `orange` — фрукт рядом с овощами, `cold` —
болезнь рядом с температурой, `bark` — собачий лай рядом с деревьями. Игрок
тянет пузырь не туда, ошибается, понимает почему — и это лучшее, что случается
за уровень.

Отсюда определение ловушки, которое умеет считать машина:

    у правила A есть готовая четвёрка, одно из слов которой правило B тоже
    принимает, причём A принимает его СИЛЬНЕЕ  ->  на уровне с A и B этот
    пузырь соблазняет уйти в B, но авторский дом всё равно выигрывает.

Три условия, и каждое обязательно:

``A сильнее B``
    Иначе это не ловушка, а брак: разбиение перестанет быть однозначным, и
    `assess_partition` отклонит уровень — правильно сделает.
``B достаточно силён``
    Связь на 0.3 против 0.88 игрок не заметит: это не соблазн, а шум базы.
``B — живое правило пула``
    Ловушка ставится парой групп. Если у B нет своей четвёрки в том же
    профиле качества, ставить нечего.

Поставленная ловушка объявляется явно: пара (токен, правило-соперник)
записывается в `level_decoys` с `planned = 1`, и дальше валидатор её пропускает
как замысел, а не как дефект. Незапланированное пересечение по-прежнему брак —
разница между «я так и хотел» и «так вышло» здесь и проходит.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .level_solver import MembershipIndex, Token

# Насколько сильной должна быть связь со слабой стороной, чтобы игрок вообще
# задумался. Сила связи в базе — статус x уверенность x очевидность, обычная
# рабочая связь около 0.8, натянутая около 0.4.
DEFAULT_MIN_RIVAL_STRENGTH = 0.55
# И насколько она должна быть сопоставима с домом. 0.7 значит «соперник почти
# так же убедителен»: ровно та зона, где ошибиться легко, а понять — приятно.
DEFAULT_MIN_RATIO = 0.7


@dataclass(frozen=True)
class DecoyPair:
    """Один готовый соблазн: токен группы A, который просится в группу B."""

    home_id: int
    home_key: str
    quartet_id: int
    token_display: str
    token_norm: str
    sense_key: str | None
    rival_id: int
    rival_key: str
    home_strength: float
    rival_strength: float

    @property
    def ratio(self) -> float:
        return self.rival_strength / self.home_strength if self.home_strength else 0.0


@dataclass
class DecoyIndex:
    """Все ловушки, которые собираются из наличного пула четвёрок."""

    pairs: tuple[DecoyPair, ...] = ()
    by_quartet: dict[int, list[DecoyPair]] = field(default_factory=dict)
    by_home: dict[int, list[DecoyPair]] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=dict)

    def __len__(self) -> int:
        return len(self.pairs)

    def for_quartet(self, quartet_id: int) -> list[DecoyPair]:
        return self.by_quartet.get(quartet_id, [])

    def distinct_pairs(self) -> set[tuple[int, int]]:
        return {(pair.home_id, pair.rival_id) for pair in self.pairs}


def build(
    entries: Iterable[dict],
    index: MembershipIndex,
    *,
    available: set[int],
    conflicts: dict[int, set[int]] | None = None,
    min_rival_strength: float = DEFAULT_MIN_RIVAL_STRENGTH,
    min_ratio: float = DEFAULT_MIN_RATIO,
) -> DecoyIndex:
    """Индекс ловушек по четвёркам пула. Порядок стабильный, случайности нет.

    ``entries``    четвёрки профиля: те же словари, что перебирает генератор;
    ``available``  категории, у которых в этом же пуле есть своя четвёрка —
                   соперник без четвёрки на поле не появится;
    ``conflicts``  пары `do_not_pair`: их и без ловушек нельзя ставить рядом.
    """
    conflicts = conflicts or {}
    key_by_id: dict[int, str] = {}
    pairs: list[DecoyPair] = []
    stats = {
        "четвёрок просмотрено": 0,
        "соперник слабоват": 0,
        "соперник сильнее дома": 0,
        "соперник вне пула": 0,
        "пара запрещена": 0,
    }
    for entry in entries:
        stats["четвёрок просмотрено"] += 1
        home_id = int(entry["category_id"])
        home_key = entry["category_key"]
        key_by_id[home_id] = home_key
        for _word_id, _sense_id, display, sense_key, _role in entry["tokens"]:
            token = Token(
                word=display.strip().lower(),
                sense_key=sense_key or None,
                display=display,
            )
            home_strength = index.strength_of(home_key, token)
            if home_strength <= 0:
                continue
            for rival_key in index.by_word.get(token.word, ()):
                if rival_key == home_key or not index.matches(rival_key, token):
                    continue
                rival_strength = index.strength_of(rival_key, token)
                if rival_strength >= home_strength:
                    stats["соперник сильнее дома"] += 1
                    continue
                if (
                    rival_strength < min_rival_strength
                    or rival_strength / home_strength < min_ratio
                ):
                    stats["соперник слабоват"] += 1
                    continue
                pairs.append(
                    DecoyPair(
                        home_id=home_id,
                        home_key=home_key,
                        quartet_id=int(entry["quartet_id"]),
                        token_display=display,
                        token_norm=token.word,
                        sense_key=token.sense_key,
                        rival_id=-1,  # проставляется ниже, когда известны id пула
                        rival_key=rival_key,
                        home_strength=home_strength,
                        rival_strength=rival_strength,
                    )
                )

    # Идентификаторы соперников: сопоставляются по ключу уже после обхода, иначе
    # пришлось бы держать обратный индекс всей базы ради нескольких сотен пар.
    id_by_key = {key: cid for cid, key in key_by_id.items()}
    resolved: list[DecoyPair] = []
    for pair in pairs:
        rival_id = id_by_key.get(pair.rival_key)
        if rival_id is None or rival_id not in available:
            stats["соперник вне пула"] += 1
            continue
        if rival_id in conflicts.get(pair.home_id, ()):
            stats["пара запрещена"] += 1
            continue
        resolved.append(
            DecoyPair(
                home_id=pair.home_id,
                home_key=pair.home_key,
                quartet_id=pair.quartet_id,
                token_display=pair.token_display,
                token_norm=pair.token_norm,
                sense_key=pair.sense_key,
                rival_id=rival_id,
                rival_key=pair.rival_key,
                home_strength=pair.home_strength,
                rival_strength=pair.rival_strength,
            )
        )

    resolved.sort(
        key=lambda item: (item.home_key, item.rival_key, item.token_norm, item.quartet_id)
    )
    by_quartet: dict[int, list[DecoyPair]] = {}
    by_home: dict[int, list[DecoyPair]] = {}
    for pair in resolved:
        by_quartet.setdefault(pair.quartet_id, []).append(pair)
        by_home.setdefault(pair.home_id, []).append(pair)
    stats["ловушек доступно"] = len(resolved)
    stats["пар правил"] = len({(pair.home_id, pair.rival_id) for pair in resolved})
    return DecoyIndex(
        pairs=tuple(resolved), by_quartet=by_quartet, by_home=by_home, stats=stats
    )
