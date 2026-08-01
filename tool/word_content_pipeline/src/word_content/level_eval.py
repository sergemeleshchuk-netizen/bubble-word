"""Оценка уровня по двум шкалам `levels/EVAL.md`: сложность D и фан F.

Зачем отдельный модуль, если оценщик уже описан. `levels/EVAL.md` задаёт модель
для человека и для скилла `level-evaluator`, а вход у неё — прогон слепого
решателя на каждый уровень. Для одного уровня это правильно и стоит недорого.
Для сравнения двух пакетов по двадцать уровней — сорок прогонов LLM, каждый со
своей случайностью; числа перестанут быть сравнимыми ровно там, где сравнение и
нужно.

Здесь та же модель, но детерминированная: все семь факторов D и все девять
якорей F считаются по базе, одинаково для записи оригинала и для наших уровней.
Две подстановки названы явно и описаны в `EVAL.md`:

    эмпирика решателя  ->  притяжение к чужой группе по SWOW (живые ассоциации
                           людей: сила связи слова со словами соседней группы);
    «валидная ловушка» ->  авторское разбиение выигрывает exact-cover-солвером
                           (`level_solver.assess_partition`), то есть соблазн
                           есть, а разложить можно только одним способом.

Почему именно SWOW, а не пересечения пулов базы. Ловушки оригинала
психологические, а не словарные: `carrot` в VEGETABLES тянет к FRUITS, потому
что морковь оранжевая, — членом категории FRUITS он при этом не является ни в
одной честной базе. Замер по пулам видит на всей записи 4 пересечения, замер по
SWOW — 12 только на пятом уровне. Первый инструмент меряет корректность базы,
второй — то, что чувствует игрок.

SWOW лежит локально (`reference/swow/swow_agg.pkl`, research-only лицензия, в
git не попадает). Без него модуль считает притяжение по пулам базы и помечает
это в отчёте: заменять инструмент молча нельзя, а сравнение остаётся честным,
пока оба пакета меряются одним и тем же.
"""

from __future__ import annotations

import math
import pickle
import sqlite3
import statistics
from dataclasses import dataclass, field
from pathlib import Path

from . import composition as composition_mod
from . import level_solver, structured

# ------------------------------------------------------------------ пороги модели

# zipf < 3.0 из EVAL.md в шкале familiarity_score (zipf / 7).
RARE_FAMILIARITY = round(3.0 / 7.0, 4)
# Заметное притяжение к чужой группе: ниже этого игрок соседа не замечает.
TRAP_MIN = 0.03
# Ловушка, которая реально кусает, — «ага-момент» по шкале фана.
AHA_MIN = 0.05
# Насколько чужая группа должна перетягивать, чтобы считаться спорностью.
PULL_OVER_HOME = 0.02
# Токен «узнаваемый»: знакомость не ниже, длина не больше.
FAMILIAR_MIN = 0.50
TOKEN_CHARS_MAX = 12
# «Стартовая» группа для темпа: ни одного токена с притяжением на сторону.
STARTER_FAMILIARITY = 0.55

# Головные слова надписи, которые ничего не называют. Надпись STRETCHY THINGS
# описывает не тему, а признак, придуманный ради четвёрки; игрок такую группу
# не угадывает, он её отгадывает последней по остатку.
VAGUE_HEADS = frozenset(
    {
        "THINGS", "STUFF", "WORDS", "TERMS", "ACTIONS", "ACTIVITIES",
        "SKILLS", "ITEMS", "OBJECTS",
    }
)
VAGUE_PREFIXES = ("KINDS OF ", "TYPES OF ", "SORTS OF ")


def _swow_path() -> Path | None:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "reference" / "swow" / "swow_agg.pkl"
        if candidate.exists():
            return candidate
    return None


class Associations:
    """Сила связи слово-слово. SWOW, если он есть локально, иначе пулы базы."""

    def __init__(self, conn: sqlite3.Connection, *, swow: Path | None = None) -> None:
        path = swow if swow is not None else _swow_path()
        self.source = "swow"
        self._fwd: dict[str, dict[str, float]] = {}
        self._pools: dict[str, frozenset[str]] = {}
        if path is not None and path.exists():
            self._fwd = pickle.loads(path.read_bytes())["fwd"]
            return
        # Запасной инструмент: слова считаются связанными, если живут в одной
        # категории базы. Грубее SWOW, но одинаков для обоих пакетов.
        self.source = "pools"
        by_category: dict[int, set[str]] = {}
        for row in conn.execute(
            """
            SELECT m.category_id AS category_id, w.normalized AS word
              FROM memberships m JOIN words w ON w.id = m.word_id
             WHERE m.review_status IN ('approved', 'auto_approved')
               AND m.semantic_status <> 'incorrect'
            """
        ):
            by_category.setdefault(int(row["category_id"]), set()).add(row["word"])
        shared: dict[str, set[str]] = {}
        for pool in by_category.values():
            for word in pool:
                shared.setdefault(word, set()).update(pool)
        self._pools = {word: frozenset(peers - {word}) for word, peers in shared.items()}

    def sym(self, first: str, second: str) -> float:
        if self.source == "swow":
            return (
                self._fwd.get(first, {}).get(second, 0.0)
                + self._fwd.get(second, {}).get(first, 0.0)
            )
        return 0.2 if second in self._pools.get(first, ()) else 0.0

    def pull(self, word: str, pool: list[str]) -> float:
        """Среднее притяжение слова к словам группы: имена групп игрок не видит."""
        others = [item for item in pool if item != word]
        if not others:
            return 0.0
        return sum(self.sym(word, item) for item in others) / len(others)


# ------------------------------------------------------------------ данные уровня


@dataclass(frozen=True)
class Group:
    group_id: int
    position: int
    category_id: int | None
    category_key: str
    concept_id: int | None
    theme: str | None
    label: str
    words: tuple[str, ...]
    displays: tuple[str, ...]
    senses: tuple[str | None, ...]

    @property
    def vague_label(self) -> bool:
        name = self.label.upper().strip()
        if name.startswith(VAGUE_PREFIXES):
            return True
        tail = name.split()
        return bool(tail) and tail[-1] in VAGUE_HEADS


@dataclass(frozen=True)
class Temptation:
    """Один токен, который тянет в соседнюю группу этого же уровня."""

    token: str
    home: str
    rival: str
    home_pull: float
    rival_pull: float

    @property
    def aha(self) -> bool:
        return self.rival_pull >= AHA_MIN

    @property
    def outpulls_home(self) -> bool:
        return self.rival_pull > self.home_pull + PULL_OVER_HOME

    def as_dict(self) -> dict[str, object]:
        return {
            "token": self.token,
            "home": self.home,
            "rival": self.rival,
            "home_pull": round(self.home_pull, 4),
            "rival_pull": round(self.rival_pull, 4),
            "aha": self.aha,
            "outpulls_home": self.outpulls_home,
        }


@dataclass
class Evaluation:
    level_key: str
    number: int
    origin: str
    difficulty: float
    fun: float
    d_factors: dict[str, float]
    f_factors: dict[str, float]
    facts: dict[str, object]
    temptations: list[Temptation] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, object]:
        return {
            "level_key": self.level_key,
            "number": self.number,
            "origin": self.origin,
            "D": self.difficulty,
            "F": self.fun,
            "d_factors": self.d_factors,
            "f_factors": self.f_factors,
            "facts": self.facts,
            "temptations": [item.as_dict() for item in self.temptations],
            "notes": self.notes,
        }


def _round_half(value: float) -> float:
    """До ближайшего 0.5, ровно .25 вверх — как написано в EVAL.md."""
    return math.floor(value * 2 + 0.5) / 2


def load_groups(conn: sqlite3.Connection, level_id: int) -> list[Group]:
    rows = list(
        conn.execute(
            """
            SELECT g.id AS group_id, g.position AS position,
                   g.category_id AS category_id, g.reference_name AS reference_name,
                   c.category_key AS category_key, c.concept_id AS concept_id,
                   c.theme AS theme, c.label AS rule_label,
                   cl.display_text AS display_label
              FROM level_groups g
              LEFT JOIN categories c       ON c.id = g.category_id
              LEFT JOIN category_labels cl ON cl.id = g.display_label_id
             WHERE g.level_id = ?
             ORDER BY g.position
            """,
            (level_id,),
        )
    )
    groups: list[Group] = []
    for row in rows:
        tokens = list(
            conn.execute(
                """
                SELECT t.display_text AS display, w.normalized AS word,
                       s.sense_key AS sense_key
                  FROM level_tokens t
                  LEFT JOIN words w       ON w.id = t.word_id
                  LEFT JOIN word_senses s ON s.id = t.sense_id
                 WHERE t.group_id = ? ORDER BY t.slot
                """,
                (row["group_id"],),
            )
        )
        label = (
            row["display_label"] or row["reference_name"] or row["rule_label"]
            or row["category_key"] or "?"
        )
        groups.append(
            Group(
                group_id=int(row["group_id"]),
                position=int(row["position"]),
                category_id=row["category_id"] and int(row["category_id"]),
                category_key=row["category_key"] or f"group-{row['group_id']}",
                concept_id=row["concept_id"] and int(row["concept_id"]),
                theme=row["theme"],
                label=str(label).upper(),
                words=tuple(
                    (item["word"] or item["display"] or "").strip().lower()
                    for item in tokens
                ),
                displays=tuple(str(item["display"]) for item in tokens),
                senses=tuple(item["sense_key"] for item in tokens),
            )
        )
    return groups


def _meta_pairs(conn: sqlite3.Connection, level_id: int) -> set[frozenset[int]]:
    """Пары групп, связанные мета-механикой: их притяжение не ловушка, а замысел."""
    pairs: set[frozenset[int]] = set()
    for row in conn.execute(
        """
        SELECT d.from_group_id AS source, t.group_id AS consumer
          FROM level_dependencies d JOIN level_tokens t ON t.id = d.to_token_id
         WHERE d.level_id = ?
        """,
        (level_id,),
    ):
        pairs.add(frozenset({int(row["source"]), int(row["consumer"])}))
    return pairs


def temptations(
    groups: list[Group], associations: Associations, meta: set[frozenset[int]]
) -> list[Temptation]:
    """Токены, которые тянет в соседнюю группу того же уровня.

    Мета-связанные пары исключены: то, что собранная группа COFFEE выпускает
    пузырь «coffee» для BEVERAGES, — объявленная механика, а не соблазн.
    """
    found: list[Temptation] = []
    for home in groups:
        pool = list(home.words)
        for word, display in zip(home.words, home.displays):
            if not word:
                continue
            home_pull = associations.pull(word, pool)
            best: tuple[float, Group] | None = None
            for rival in groups:
                if rival.group_id == home.group_id:
                    continue
                if frozenset({home.group_id, rival.group_id}) in meta:
                    continue
                value = associations.pull(word, list(rival.words))
                if best is None or value > best[0]:
                    best = (value, rival)
            if best is None or best[0] < TRAP_MIN:
                continue
            found.append(
                Temptation(
                    token=display,
                    home=home.label,
                    rival=best[1].label,
                    home_pull=home_pull,
                    rival_pull=best[0],
                )
            )
    return sorted(found, key=lambda item: -item.rival_pull)


def evaluate_level(
    conn: sqlite3.Connection,
    level_id: int,
    *,
    associations: Associations,
    index: level_solver.MembershipIndex,
    structures: structured.StructureIndex,
    previous_words: set[str] | None = None,
    timeout_ms: int = 5000,
) -> Evaluation:
    row = conn.execute(
        "SELECT level_key, origin, reference_level FROM level_instances WHERE id = ?",
        (level_id,),
    ).fetchone()
    if row is None:
        raise KeyError(f"уровня {level_id} нет")
    level_key = str(row["level_key"])
    number = int(row["reference_level"] or _number_from_key(level_key))

    groups = load_groups(conn, level_id)
    meta = _meta_pairs(conn, level_id)
    pulls = temptations(groups, associations, meta)
    plan = composition_mod.for_level(number)
    notes: list[str] = []

    # Разбиение: разложить можно одним способом или нет. Ловушка честная, только
    # если авторский дом всё-таки выигрывает.
    tokens = [
        level_solver.Token(word=word, sense_key=sense, display=display)
        for group in groups
        for word, display, sense in zip(group.words, group.displays, group.senses)
        if word
    ]
    homes = {
        display.strip().lower(): group.category_key
        for group in groups
        for display in group.displays
    }
    assessment = level_solver.assess_partition(
        tokens, homes, index, structures, timeout_ms=timeout_ms
    )
    solvable = assessment.intended_is_best and assessment.solver is not None and (
        assessment.solver.outcome in ("unique", "ambiguous")
    )
    if not solvable:
        notes.append(
            f"разбиение не подтверждено солвером: {assessment.solver.outcome if assessment.solver else '—'}"
        )

    # Соблазн и спорность — разные вещи, и разделяет их не сила ассоциации,
    # а правило соседней группы. `carrot` тянет к FRUITS, потому что морковь
    # оранжевая, но правилу FRUITS он не подходит: разложить можно только одним
    # способом, и это ага-момент. `orange` подходит обоим правилам честно —
    # вот это спорность, и её надо либо объявить ловушкой, либо убрать.
    accepting = {
        (decoy.token.strip().lower(), decoy.rival)
        for decoy in assessment.decoys
        if not decoy.planned
    }
    by_label = {group.label: group.category_key for group in groups}
    disputed = sorted(accepting)
    honest = (
        [
            item for item in pulls
            if (item.token.strip().lower(), by_label.get(item.rival, "")) not in accepting
        ]
        if solvable
        else []
    )
    aha = [item for item in honest if item.aha]

    # ---------------------------------------------------------------- сложность D
    count = len(groups)
    if count <= 6:
        f1 = 0.0
    elif count <= 8:
        f1 = 1.0
    elif count <= 10:
        f1 = 1.5
    else:
        f1 = 2.5

    f2 = min(3.0, float(len(honest)))

    same_theme = _same_theme_pairs(groups)
    splits = _concept_splits(groups)
    f3 = min(1.5, 0.75 * len(same_theme)) + min(1.0, float(len(splits)))

    familiarity = _familiarity(conn, groups)
    rare = [word for word, value in familiarity.items() if value is not None
            and value < RARE_FAMILIARITY]
    f4 = min(1.0, 0.5 * len(rare))

    k_value = plan.k_observed
    if k_value is None or k_value >= 1.6:
        f5 = 0.0
    elif k_value >= 1.35:
        f5 = 0.5
    else:
        f5 = 1.0

    repeats = sorted(
        {word for group in groups for word in group.words if word}
        & (previous_words or set())
    )
    f6 = min(1.0, 0.5 * len(repeats))

    f7 = min(1.0, min(0.5, 0.25 * len(disputed)) + (0.5 if len(disputed) >= 3 else 0.0))

    d_factors = {
        "F1 масштаб": f1, "F2 ловушки": f2, "F3 близость": f3, "F4 редкость": f4,
        "F5 лимит": f5, "F6 память": f6, "F7 спорность": f7,
    }
    difficulty = _round_half(min(10.0, max(1.0, 1.0 + sum(d_factors.values()))))

    # --------------------------------------------------------------------- фан F
    vague = [group.label for group in groups if group.vague_label]
    unreadable = [
        display
        for group in groups
        for display in group.displays
        if len(display) > TOKEN_CHARS_MAX or len(display.split()) > 1
    ]
    weak = [
        word for word, value in familiarity.items()
        if value is not None and value < FAMILIAR_MIN
    ]
    recognisable = not vague and not unreadable and len(weak) <= count // 3

    themes = [group.theme for group in groups if group.theme]
    distinct = len(set(themes))
    variety = distinct >= max(2, round(0.6 * count))
    dominant = _dominant_theme(groups)

    starter = any(
        group.theme is not None
        and all(
            familiarity.get(word) is not None
            and familiarity[word] >= STARTER_FAMILIARITY
            for word in group.words if word
        )
        and not any(item.home == group.label for item in pulls)
        for group in groups
    )

    f_factors = {
        "узнаваемость": 1.0 if recognisable else 0.0,
        "натужные надписи": -min(2.0, float(len(vague))),
        "ага-моменты": min(2.0, 0.5 * len(aha)),
        "разнообразие": 0.5 if variety else 0.0,
        "сюжет": 0.5 if len(meta) >= 2 else 0.0,
        "одна сфера без замысла": -1.0 if dominant and not (honest or meta) else 0.0,
        "спорность вне замысла": -min(1.0, 0.25 * len(disputed)),
        "темп": 0.5 if starter else 0.0,
        "пресно": -0.5 if difficulty >= 4 and not aha else 0.0,
    }
    fun = _round_half(min(10.0, max(1.0, 5.0 + sum(f_factors.values()))))
    if not solvable:
        fun = min(fun, 3.0)
        notes.append("уровень не подтверждён разбиением: фан ограничен тройкой")

    facts = {
        "категорий": count,
        "токенов": len(tokens),
        "притяжений": len(pulls),
        "честных ловушек": len(honest),
        "ага-моментов": len(aha),
        "спорных": len(disputed),
        "мета-связей": len(meta),
        "смежных пар": [list(pair) for pair in same_theme],
        "разрезаний темы": splits,
        "редких слов": rare,
        "повторов с прошлого уровня": repeats,
        "натужных надписей": vague,
        "нечитаемых токенов": unreadable,
        "K": k_value,
        "знакомость средняя": round(
            statistics.fmean([v for v in familiarity.values() if v is not None]), 3
        ) if any(v is not None for v in familiarity.values()) else None,
        "разбиение": {
            "отрыв": assessment.partition_margin,
            "исход": assessment.solver.outcome if assessment.solver else None,
        },
        "источник ассоциаций": associations.source,
    }
    return Evaluation(
        level_key=level_key,
        number=number,
        origin=str(row["origin"] or "generated"),
        difficulty=difficulty,
        fun=fun,
        d_factors=d_factors,
        f_factors=f_factors,
        facts=facts,
        temptations=pulls,
        notes=notes,
    )


def _number_from_key(level_key: str) -> int:
    digits = "".join(ch for ch in level_key if ch.isdigit())
    return int(digits) if digits else 1


def _same_theme_pairs(groups: list[Group]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for first in range(len(groups)):
        for second in range(first + 1, len(groups)):
            left, right = groups[first], groups[second]
            if left.theme and left.theme == right.theme:
                pairs.append((left.label, right.label))
    return pairs


def _concept_splits(groups: list[Group]) -> list[list[str]]:
    """Одна тема, разрезанная на несколько правил: MEASUREMENTS на четыре меры."""
    by_concept: dict[int, list[str]] = {}
    for group in groups:
        if group.concept_id:
            by_concept.setdefault(group.concept_id, []).append(group.label)
    return [labels for labels in by_concept.values() if len(labels) > 1]


def _dominant_theme(groups: list[Group]) -> bool:
    themes = [group.theme for group in groups if group.theme]
    if len(themes) < len(groups) / 2:
        return False
    top = statistics.mode(themes) if themes else None
    return bool(top) and themes.count(top) > len(groups) / 2


def _familiarity(conn: sqlite3.Connection, groups: list[Group]) -> dict[str, float | None]:
    words = sorted({word for group in groups for word in group.words if word})
    if not words:
        return {}
    placeholders = ",".join("?" for _ in words)
    known = {
        row["normalized"]: row["familiarity_score"]
        for row in conn.execute(
            f"SELECT normalized, familiarity_score FROM words WHERE normalized IN ({placeholders})",
            words,
        )
    }
    return {word: known.get(word) for word in words}


def evaluate_pack(
    conn: sqlite3.Connection,
    prefix: str,
    *,
    swow: Path | None = None,
    timeout_ms: int = 5000,
) -> list[Evaluation]:
    """Оценивает весь пакет по возрастанию номера, помня слова прошлого уровня."""
    associations = Associations(conn, swow=swow)
    index = level_solver.load_memberships(conn)
    structures = structured.load(conn)
    rows = list(
        conn.execute(
            "SELECT id, level_key FROM level_instances WHERE level_key LIKE ? ORDER BY level_key",
            (f"{prefix}%",),
        )
    )
    results: list[Evaluation] = []
    previous: set[str] = set()
    for row in rows:
        evaluation = evaluate_level(
            conn, int(row["id"]),
            associations=associations, index=index, structures=structures,
            previous_words=previous, timeout_ms=timeout_ms,
        )
        results.append(evaluation)
        previous = {
            word
            for group in load_groups(conn, int(row["id"]))
            for word in group.words if word
        }
    return results


def summarise(results: list[Evaluation]) -> dict[str, object]:
    if not results:
        return {}
    return {
        "уровней": len(results),
        "D среднее": round(statistics.fmean(item.difficulty for item in results), 2),
        "F среднее": round(statistics.fmean(item.fun for item in results), 2),
        "честных ловушек": sum(int(item.facts["честных ловушек"]) for item in results),
        "ага-моментов": sum(int(item.facts["ага-моментов"]) for item in results),
        "спорных": sum(int(item.facts["спорных"]) for item in results),
        "натужных надписей": sum(
            len(item.facts["натужных надписей"]) for item in results  # type: ignore[arg-type]
        ),
        "нечитаемых токенов": sum(
            len(item.facts["нечитаемых токенов"]) for item in results  # type: ignore[arg-type]
        ),
        "мета-связей": sum(int(item.facts["мета-связей"]) for item in results),
        "знакомость средняя": round(
            statistics.fmean(
                float(item.facts["знакомость средняя"])  # type: ignore[arg-type]
                for item in results
                if item.facts["знакомость средняя"] is not None
            ),
            3,
        ),
    }
