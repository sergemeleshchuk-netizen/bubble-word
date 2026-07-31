"""Exact-cover solver полного уровня.

Что проверяет. Уровень — это N скрытых категорий по четыре слова. Игрок видит
только слова. Уровень корректен, только если весь набор слов раскладывается на
четвёрки ровно одним способом. Иначе игрок соберёт ответ, правильный с его
точки зрения, а игра его не примет — и это худший вид сложности.

Чем отличается от проверки четвёрки. `solver.quartet_locally_unique` отвечает
на вопрос «не лежит ли эта четвёрка целиком в другой категории». Это локальная
проверка одной группы, и она **не** доказывает единственность уровня:
неоднозначность рождается на стыке групп. Хватает одного общего слова.

    ROSE, TULIP, LILY, DAISY        -> FLOWERS
    RED, BLUE, GREEN, ROSE(цвет)    -> COLOURS

Каждая четвёрка по отдельности локально однозначна. Вместе — уровень с двумя
ответами, если `rose` не разведён по значениям.

Что учитывается при поиске интерпретаций:
  * значение слова (`sense`) и режим обращения со словом (`sense_mode`);
  * структура категории (пары, последовательности) — модуль `structured`;
  * пригодность связи: `rejected`/`candidate` и `semantic_status = incorrect`
    в игру не идут и в интерпретациях не участвуют;
  * выключенные категории.

Важное решение: интерпретации ищутся по **широкому** набору статусов, включая
`hard_only`, даже если уровень обычный. Игрок не знает наших статусов. Если он
физически может собрать альтернативную группу — уровень неоднозначен.

Ответ считается пригодным только при `solution_count == 1`. Таймаут, ошибка и
«не знаю» уникальностью не считаются никогда.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from dataclasses import dataclass, field
from itertools import combinations

from .normalization import normalize_word
from .structured import StructureIndex

SOLVER_VERSION = "level-exact-cover/1.0"
QUARTET_SIZE = 4
MAX_SOLUTIONS = 2  # второго решения достаточно, чтобы отклонить уровень
DEFAULT_TIMEOUT_MS = 5_000

# Статусы связей, которые игрок может использовать при разборе уровня.
# Шире, чем набор для генерации: hard_only игрок тоже способен увидеть.
INTERPRETATION_STATUSES = ("approved", "alternative", "hard_only")

# Режимы, в которых связь работает с написанием слова, а не с его значением.
SURFACE_MODES = ("surface_form", "compound", "phrase_pattern")

# Исходы. Пригоден только `unique`.
OUTCOMES = ("unique", "ambiguous", "unsolvable", "invalid_input", "timeout", "error")


@dataclass(frozen=True)
class Token:
    """Пузырь на экране: слово в конкретном значении."""

    word: str  # нормализованная форма
    sense_key: str | None = None
    display: str | None = None

    @property
    def display_text(self) -> str:
        return self.display or self.word

    def as_dict(self) -> dict[str, str | None]:
        return {"word": self.word, "sense_key": self.sense_key, "display": self.display_text}


@dataclass(frozen=True)
class Interpretation:
    """Категория и слова уровня, которые в неё укладываются."""

    category_key: str
    label: str
    token_indices: frozenset[int]


@dataclass
class LevelSolverResult:
    outcome: str
    solution_count: int = 0
    solutions: list[list[tuple[str, tuple[str, ...]]]] = field(default_factory=list)
    reason: str = ""
    duration_ms: int = 0
    input_hash: str = ""
    solver_version: str = SOLVER_VERSION
    parameters: dict[str, object] = field(default_factory=dict)
    nodes_visited: int = 0

    @property
    def unique(self) -> bool:
        """Единственное разбиение. Таймаут и ошибка — не уникальность."""
        return self.outcome == "unique" and self.solution_count == 1

    @property
    def alternative_partition(self) -> list[tuple[str, tuple[str, ...]]] | None:
        """Второе разбиение — то, что покажем при отклонении уровня."""
        return self.solutions[1] if len(self.solutions) > 1 else None


# ------------------------------------------------------------------ загрузка пулов


# Насколько уверенно игрок увидит связь. Не «правда ли это», а «первым ли
# приходит в голову»: hard_only верно, но игрок сам не догадается.
STATUS_WEIGHT = {"approved": 1.0, "alternative": 0.72, "hard_only": 0.40}


@dataclass
class MembershipIndex:
    """Кто из категорий что принимает: (категория, слово) -> допустимые значения.

    `None` во множестве значений означает «связь про написание слова, значение
    не важно». Пустого множества не бывает: категория либо принимает слово,
    либо строки для него нет.
    """

    labels: dict[str, str]
    accepts: dict[tuple[str, str], set[str | None]]
    polysemous: set[str]
    # обратный индекс слово -> категории, которые его принимают: без него поиск
    # интерпретаций перебирал бы все 1276 категорий на каждый пузырь
    by_word: dict[str, list[str]] = field(default_factory=dict)
    # Сила связи: статус x уверенность x очевидность. Нужна не solver'у, а
    # оценке разбиений: «оба разбиения существуют» и «оба одинаково
    # естественны» — разные утверждения.
    strength: dict[tuple[str, str], float] = field(default_factory=dict)

    def matches(self, category_key: str, token: Token) -> bool:
        senses = self.accepts.get((category_key, token.word))
        if not senses:
            return False
        if None in senses:
            return True  # написание, значение не важно
        return token.sense_key in senses

    def strength_of(self, category_key: str, token: Token) -> float:
        if not self.matches(category_key, token):
            return 0.0
        return self.strength.get((category_key, token.word), 0.5)


def load_memberships(
    conn: sqlite3.Connection,
    *,
    statuses: tuple[str, ...] = INTERPRETATION_STATUSES,
) -> MembershipIndex:
    placeholders = ",".join("?" for _ in statuses)
    has_sense_mode = any(
        row["name"] == "sense_mode" for row in conn.execute("PRAGMA table_info(memberships)")
    )
    sense_mode_expr = "m.sense_mode" if has_sense_mode else "'lexical'"
    rows = conn.execute(
        f"""
        SELECT c.category_key AS category_key, c.label AS label,
               w.normalized AS word, s.sense_key AS sense_key,
               {sense_mode_expr} AS sense_mode,
               m.review_status AS review_status,
               m.fit_score AS fit_score, m.obviousness_score AS obviousness_score
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
          JOIN words w      ON w.id = m.word_id
          LEFT JOIN word_senses s ON s.id = m.sense_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'
           AND c.status = 'active'
        """,
        statuses,
    )
    labels: dict[str, str] = {}
    accepts: dict[tuple[str, str], set[str | None]] = {}
    strength: dict[tuple[str, str], float] = {}
    for row in rows:
        labels[row["category_key"]] = row["label"]
        key = (row["category_key"], row["word"])
        if row["sense_mode"] in SURFACE_MODES or row["sense_key"] is None:
            # Написание, либо у слова одно значение: подходит любой токен слова.
            accepts.setdefault(key, set()).add(None)
        else:
            accepts.setdefault(key, set()).add(row["sense_key"])
        value = round(
            STATUS_WEIGHT.get(row["review_status"], 0.4)
            * float(row["fit_score"] or 0.5)
            * (0.5 + 0.5 * float(row["obviousness_score"] or 0.5)),
            4,
        )
        # Одно слово может иметь несколько связей с категорией: берём сильнейшую,
        # потому что игрок увидит именно самую очевидную.
        strength[key] = max(strength.get(key, 0.0), value)

    polysemous = {
        row["normalized"]
        for row in conn.execute(
            """
            SELECT w.normalized AS normalized
              FROM word_senses s JOIN words w ON w.id = s.word_id
             GROUP BY s.word_id HAVING COUNT(*) > 1
            """
        )
    }
    by_word: dict[str, list[str]] = {}
    for category_key, word in accepts:
        by_word.setdefault(word, []).append(category_key)

    return MembershipIndex(
        labels=labels, accepts=accepts, polysemous=polysemous, by_word=by_word,
        strength=strength,
    )


# ------------------------------------------------------------------------- solver


def solve_level(
    tokens: list[Token],
    index: MembershipIndex,
    structures: StructureIndex | None = None,
    *,
    max_solutions: int = MAX_SOLUTIONS,
    timeout_ms: int = DEFAULT_TIMEOUT_MS,
) -> LevelSolverResult:
    """Ищет все разбиения уровня на четвёрки-категории. Останавливается на втором."""
    structures = structures or StructureIndex()
    parameters = {
        "max_solutions": max_solutions,
        "timeout_ms": timeout_ms,
        "quartet_size": QUARTET_SIZE,
        "statuses": list(INTERPRETATION_STATUSES),
    }
    digest = input_hash(tokens, parameters)
    started = time.monotonic()

    def finish(outcome: str, reason: str, solutions=None, nodes: int = 0) -> LevelSolverResult:
        solved = solutions or []
        return LevelSolverResult(
            outcome=outcome,
            solution_count=len(solved),
            solutions=solved,
            reason=reason,
            duration_ms=int((time.monotonic() - started) * 1000),
            input_hash=digest,
            parameters=parameters,
            nodes_visited=nodes,
        )

    problem = _validate_input(tokens, index)
    if problem:
        return finish("invalid_input", problem)

    interpretations = _interpretations(tokens, index, structures)
    if not interpretations:
        return finish("unsolvable", "ни одна категория не набирает четырёх слов уровня")

    by_token: dict[int, list[int]] = {i: [] for i in range(len(tokens))}
    for position, interpretation in enumerate(interpretations):
        for token_index in interpretation.token_indices:
            by_token[token_index].append(position)

    solutions: list[list[tuple[str, tuple[str, ...]]]] = []
    deadline = started + timeout_ms / 1000
    state = {"nodes": 0, "timed_out": False}

    def search(remaining: frozenset[int], used: frozenset[str],
               chosen: list[tuple[str, tuple[str, ...]]]) -> None:
        if len(solutions) >= max_solutions or state["timed_out"]:
            return
        state["nodes"] += 1
        # Считаем с 1, поэтому первая проверка времени приходится на самый первый
        # узел: нулевой таймаут обязан отсекать сразу, а не после 512 узлов.
        if state["nodes"] % 512 == 1 and time.monotonic() > deadline:
            state["timed_out"] = True
            return
        if not remaining:
            solutions.append(list(chosen))
            return

        # Ветвимся по слову с наименьшим числом вариантов: если у слова нет ни
        # одной группы, ветка мертва сразу.
        pivot = min(remaining, key=lambda token_index: len(by_token[token_index]))
        for position in by_token[pivot]:
            interpretation = interpretations[position]
            # Категория встречается в уровне один раз: две её четвёрки — это не
            # разбиение, а один и тот же ответ дважды.
            if interpretation.category_key in used:
                continue
            if not interpretation.token_indices <= remaining:
                continue
            chosen.append(
                (
                    interpretation.category_key,
                    tuple(sorted(tokens[i].display_text for i in interpretation.token_indices)),
                )
            )
            search(remaining - interpretation.token_indices,
                   used | {interpretation.category_key}, chosen)
            chosen.pop()
            if len(solutions) >= max_solutions or state["timed_out"]:
                return

    search(frozenset(range(len(tokens))), frozenset(), [])

    if state["timed_out"]:
        # Найденное до таймаута не доказывает ничего: непросмотренная ветка
        # может содержать второе разбиение.
        return finish(
            "timeout",
            f"solver не уложился в {timeout_ms} мс — уровень не принимается",
            solutions,
            state["nodes"],
        )
    if not solutions:
        return finish("unsolvable", "уровень не раскладывается ни одним способом",
                      nodes=state["nodes"])
    if len(solutions) > 1:
        return finish(
            "ambiguous",
            f"разбиений минимум {len(solutions)}: у уровня несколько правильных ответов",
            solutions,
            state["nodes"],
        )
    return finish("unique", "разбиение единственное", solutions, state["nodes"])


def _validate_input(tokens: list[Token], index: MembershipIndex) -> str:
    """Проверки входа. Возвращает текст проблемы или пустую строку."""
    if not tokens:
        return "в уровне нет слов"
    if len(tokens) % QUARTET_SIZE != 0:
        return f"число слов {len(tokens)} не делится на {QUARTET_SIZE}"

    displays = [token.display_text.strip().lower() for token in tokens]
    duplicates = sorted({value for value in displays if displays.count(value) > 1})
    if duplicates:
        return f"одинаковые пузыри в одном уровне: {', '.join(duplicates)}"

    unresolved = sorted(
        token.word
        for token in tokens
        if token.sense_key is None and token.word in index.polysemous
    )
    if unresolved:
        return (
            "у многозначных слов не указано значение: "
            + ", ".join(unresolved)
            + " — пустое значение не должно скрывать пропуск"
        )
    return ""


def _interpretations(
    tokens: list[Token], index: MembershipIndex, structures: StructureIndex
) -> list[Interpretation]:
    """Все четвёрки слов уровня, допустимые хотя бы для одной категории."""
    by_category: dict[str, list[int]] = {}
    for position, token in enumerate(tokens):
        for category_key in index.by_word.get(token.word, ()):
            if index.matches(category_key, token):
                by_category.setdefault(category_key, []).append(position)

    result: list[Interpretation] = []
    for category_key in sorted(by_category):
        positions = by_category[category_key]
        if len(positions) < QUARTET_SIZE:
            continue
        structure = structures.get(category_key)
        for group in combinations(sorted(positions), QUARTET_SIZE):
            words = frozenset(tokens[i].word for i in group)
            allowed, _reason = structure.allows(words)
            if not allowed:
                continue
            result.append(
                Interpretation(
                    category_key=category_key,
                    label=index.labels.get(category_key, category_key),
                    token_indices=frozenset(group),
                )
            )
    return result


def input_hash(tokens: list[Token], parameters: dict[str, object]) -> str:
    """Отпечаток входа: те же слова и параметры дают тот же хеш."""
    payload = {
        "tokens": sorted(
            (token.word, token.sense_key or "", token.display_text) for token in tokens
        ),
        "parameters": {key: parameters[key] for key in sorted(parameters)},
        "solver_version": SOLVER_VERSION,
    }
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def parse_tokens(raw: str) -> list[Token]:
    """Разбор строки уровня: `rose#rose_flower, tulip, lily, daisy`."""
    tokens: list[Token] = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        display, _, sense = chunk.partition("#")
        display = display.strip()
        tokens.append(
            Token(
                word=normalize_word(display),
                sense_key=sense.strip() or None,
                display=display,
            )
        )
    return tokens


def format_solution(solution: list[tuple[str, tuple[str, ...]]]) -> str:
    return " | ".join(
        f"{category_key}: {', '.join(words)}" for category_key, words in sorted(solution)
    )


# ============================================================ авторское разбиение

# Ниже этого отрыва авторское разбиение перестаёт быть «самым естественным»:
# альтернатива читается почти так же хорошо, и игрок соберёт её первой.
DEFAULT_MARGIN_THRESHOLD = 0.06
# Сколько разбиений искать при оценке. Двух хватает, чтобы отклонить уровень,
# но не хватает, чтобы понять, насколько альтернатива хороша.
ASSESSMENT_MAX_SOLUTIONS = 8


@dataclass
class Decoy:
    """Правдоподобный чужой дом токена внутри этого уровня."""

    token: str
    home: str
    rival: str
    home_strength: float
    rival_strength: float
    planned: bool

    @property
    def stronger_than_home(self) -> bool:
        return self.rival_strength > self.home_strength


@dataclass
class PartitionAssessment:
    """Насколько авторское разбиение сильнее семантических альтернатив.

    Заменяет бинарное `solution_count == 1`. Референс намеренно строит интерес
    на пересечениях: orange — и фрукт, и цвет; bark — и собака, и дерево. Такие
    уровни вышли и работают, потому что у токена есть авторский дом, а
    альтернатива слабее. Запрещать любое пересечение значит запрещать
    ровно то, на чём держится игра.
    """

    intended_partition_score: float
    best_alternative_score: float
    partition_margin: float
    intended_is_best: bool
    alternative_count: int
    planned_decoy_count: int
    unplanned_decoy_count: int
    decoys: list[Decoy] = field(default_factory=list)
    hard_reject: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    solver: LevelSolverResult | None = None

    @property
    def accepted(self) -> bool:
        return not self.hard_reject

    def as_dict(self) -> dict[str, object]:
        return {
            "intended_partition_score": self.intended_partition_score,
            "best_alternative_score": self.best_alternative_score,
            "partition_margin": self.partition_margin,
            "intended_is_best": self.intended_is_best,
            "alternative_count": self.alternative_count,
            "planned_decoy_count": self.planned_decoy_count,
            "unplanned_decoy_count": self.unplanned_decoy_count,
            "hard_reject": self.hard_reject,
            "warnings": self.warnings,
        }


def _partition_score(
    assignment: dict[str, str], tokens: list[Token], index: MembershipIndex
) -> float:
    """Средняя сила связи по всем пузырям разбиения."""
    if not tokens:
        return 0.0
    total = sum(
        index.strength_of(assignment.get(token.display_text.strip().lower(), ""), token)
        for token in tokens
    )
    return round(total / len(tokens), 4)


def assess_partition(
    tokens: list[Token],
    homes: dict[str, str],
    index: MembershipIndex,
    structures: StructureIndex | None = None,
    *,
    planned_decoys: set[tuple[str, str]] | None = None,
    margin_threshold: float = DEFAULT_MARGIN_THRESHOLD,
    max_solutions: int = ASSESSMENT_MAX_SOLUTIONS,
    timeout_ms: int = DEFAULT_TIMEOUT_MS,
    meta_ok: bool = True,
    meta_problems: list[str] | None = None,
) -> PartitionAssessment:
    """Сравнивает авторское разбиение с найденными альтернативами.

    ``homes``          display токена (lowercase) -> category_key авторского дома;
    ``planned_decoys`` пары (display токена, чужой category_key), которые
                       поставлены намеренно и браком не считаются.
    """
    planned_decoys = planned_decoys or set()
    hard_reject: list[str] = []
    warnings: list[str] = []

    missing_home = sorted(
        token.display_text for token in tokens
        if not homes.get(token.display_text.strip().lower())
    )
    for display in missing_home:
        hard_reject.append(f"у токена «{display}» нет авторского дома")

    intended = _partition_score(homes, tokens, index)
    for token in tokens:
        home = homes.get(token.display_text.strip().lower())
        if home and not index.matches(home, token):
            hard_reject.append(
                f"авторский дом «{home}» не принимает токен «{token.display_text}»"
            )

    result = solve_level(
        tokens, index, structures, max_solutions=max_solutions, timeout_ms=timeout_ms
    )
    intended_signature = _signature_from_homes(homes, tokens)
    alternatives: list[float] = []
    for solution in result.solutions:
        assignment = {
            display.strip().lower(): category_key
            for category_key, words in solution
            for display in words
        }
        if _signature(assignment, tokens) == intended_signature:
            continue
        alternatives.append(_partition_score(assignment, tokens, index))

    best_alternative = max(alternatives, default=0.0)
    margin = round(intended - best_alternative, 4)
    intended_is_best = not alternatives or intended > best_alternative

    if result.outcome in ("timeout", "error", "invalid_input"):
        hard_reject.append(f"solver: {result.outcome} — {result.reason}")
    if result.outcome == "unsolvable":
        hard_reject.append("уровень не раскладывается ни одним способом")
    if alternatives and not intended_is_best:
        hard_reject.append(
            f"альтернативное разбиение не слабее авторского "
            f"({best_alternative:.3f} >= {intended:.3f})"
        )
    elif alternatives and margin < margin_threshold:
        hard_reject.append(
            f"отрыв авторского разбиения {margin:.3f} ниже порога {margin_threshold:.3f}"
        )

    # Локальные ловушки: токен, который тянет в соседнюю группу этого уровня.
    own = set(homes.values())
    decoys: list[Decoy] = []
    for token in tokens:
        display = token.display_text.strip().lower()
        home = homes.get(display)
        if not home:
            continue
        home_strength = index.strength_of(home, token)
        for rival in sorted(own):
            if rival == home or not index.matches(rival, token):
                continue
            decoys.append(
                Decoy(
                    token=token.display_text,
                    home=home,
                    rival=rival,
                    home_strength=home_strength,
                    rival_strength=index.strength_of(rival, token),
                    planned=(display, rival) in planned_decoys,
                )
            )

    planned_count = sum(1 for decoy in decoys if decoy.planned)
    unplanned = [decoy for decoy in decoys if not decoy.planned]
    for decoy in unplanned:
        if decoy.stronger_than_home:
            hard_reject.append(
                f"незапланированная ловушка: «{decoy.token}» сильнее тянет "
                f"в «{decoy.rival}» ({decoy.rival_strength:.2f}), "
                f"чем в авторский дом «{decoy.home}» ({decoy.home_strength:.2f})"
            )
        else:
            warnings.append(
                f"пересечение без пометки: «{decoy.token}» подходит и «{decoy.rival}»"
            )

    if not meta_ok:
        for problem in meta_problems or ["мета-граф не проходит проверку"]:
            hard_reject.append(f"мета: {problem}")

    return PartitionAssessment(
        intended_partition_score=intended,
        best_alternative_score=round(best_alternative, 4),
        partition_margin=margin,
        intended_is_best=intended_is_best,
        alternative_count=len(alternatives),
        planned_decoy_count=planned_count,
        unplanned_decoy_count=len(unplanned),
        decoys=decoys,
        hard_reject=hard_reject,
        warnings=warnings,
        solver=result,
    )


def _signature(assignment: dict[str, str], tokens: list[Token]) -> frozenset[frozenset[str]]:
    groups: dict[str, set[str]] = {}
    for token in tokens:
        display = token.display_text.strip().lower()
        groups.setdefault(assignment.get(display, ""), set()).add(display)
    return frozenset(frozenset(members) for members in groups.values())


def _signature_from_homes(
    homes: dict[str, str], tokens: list[Token]
) -> frozenset[frozenset[str]]:
    return _signature(homes, tokens)
