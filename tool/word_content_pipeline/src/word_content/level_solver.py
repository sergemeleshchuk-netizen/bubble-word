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

    def matches(self, category_key: str, token: Token) -> bool:
        senses = self.accepts.get((category_key, token.word))
        if not senses:
            return False
        if None in senses:
            return True  # написание, значение не важно
        return token.sense_key in senses


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
               {sense_mode_expr} AS sense_mode
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
    for row in rows:
        labels[row["category_key"]] = row["label"]
        key = (row["category_key"], row["word"])
        if row["sense_mode"] in SURFACE_MODES or row["sense_key"] is None:
            # Написание, либо у слова одно значение: подходит любой токен слова.
            accepts.setdefault(key, set()).add(None)
        else:
            accepts.setdefault(key, set()).add(row["sense_key"])

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
        labels=labels, accepts=accepts, polysemous=polysemous, by_word=by_word
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
