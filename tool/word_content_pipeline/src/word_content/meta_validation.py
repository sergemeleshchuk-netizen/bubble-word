"""Проверка мета-механики уровня: состояние, а не статика.

Мета-ссылка — не «ещё одно слово в категории». Это зависимость: пузырь
появляется на поле только после того, как собрана другая категория. На уровне 3
референса собранные `school subjects` лопаются и оставляют картинку учебников,
которая и есть четвёртый пузырь категории `school`. К уровню 7 такие ссылки
образуют целые цепочки, а на 17-м категория `healthy eating` целиком состоит из
результатов четырёх других групп.

Из этого следует, что уровень нельзя проверять как плоский набор слов. Нужна
симуляция:

    доступные токены -> какие группы можно собрать -> что они выпускают ->
    снова доступные токены

Если симуляция не доходит до конца, уровень непроходим — независимо от того,
что говорит exact-cover solver. Поэтому проверка обязательная, а не «фаза 4».

Ловим три разные болезни, и путать их нельзя:

``cycle``     A выпускает токен для B, B — для A. Ни одна из них не стартует.
``deadlock``  цикла нет, но группа ждёт токен, который никто не выпускает.
``orphan``    токен объявлен результатом группы, которой на уровне нет.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field


@dataclass
class MetaValidation:
    """Итог симуляции. `ok` означает «уровень проходим из стартового состояния»."""

    ok: bool
    is_dag: bool
    order: list[str] = field(default_factory=list)
    cycles: list[list[str]] = field(default_factory=list)
    deadlocked: list[str] = field(default_factory=list)
    orphan_tokens: list[str] = field(default_factory=list)
    self_loops: list[str] = field(default_factory=list)
    max_depth: int = 0
    problems: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "ok": self.ok,
            "is_dag": self.is_dag,
            "order": self.order,
            "cycles": self.cycles,
            "deadlocked": self.deadlocked,
            "orphan_tokens": self.orphan_tokens,
            "self_loops": self.self_loops,
            "max_depth": self.max_depth,
            "problems": self.problems,
        }


def validate(
    group_tokens: dict[str, list[str]],
    emitted_by: dict[str, str],
) -> MetaValidation:
    """Симулирует прохождение уровня.

    ``group_tokens``  группа -> её четыре токена;
    ``emitted_by``    токен -> группа, которая его выпускает.
    """
    problems: list[str] = []
    orphans = sorted(
        token for token, source in emitted_by.items() if source not in group_tokens
    )
    for token in orphans:
        problems.append(
            f"токен «{token}» объявлен результатом группы «{emitted_by[token]}», "
            "которой на уровне нет"
        )

    token_owner = {
        token: group for group, tokens in group_tokens.items() for token in tokens
    }
    self_loops = sorted(
        token
        for token, source in emitted_by.items()
        if token_owner.get(token) == source
    )
    for token in self_loops:
        problems.append(
            f"группа «{emitted_by[token]}» выпускает токен «{token}» для самой себя: "
            "собрать её нельзя, пока она не собрана"
        )

    # Граф зависимостей между группами: источник -> потребитель.
    edges: dict[str, set[str]] = {group: set() for group in group_tokens}
    for token, source in emitted_by.items():
        target = token_owner.get(token)
        if target is None or source not in edges:
            continue
        edges[source].add(target)

    cycles = _find_cycles(edges)
    for cycle in cycles:
        problems.append("цикл мета-зависимостей: " + " -> ".join([*cycle, cycle[0]]))

    # Симуляция из стартового состояния.
    available = {
        token
        for tokens in group_tokens.values()
        for token in tokens
        if token not in emitted_by
    }
    pending = dict(group_tokens)
    order: list[str] = []
    depth_of: dict[str, int] = {}
    while pending:
        ready = sorted(
            group
            for group, tokens in pending.items()
            if all(token in available for token in tokens)
        )
        if not ready:
            break
        for group in ready:
            depth_of[group] = 1 + max(
                (
                    depth_of.get(emitted_by[token], 0)
                    for token in pending[group]
                    if token in emitted_by
                ),
                default=0,
            )
            order.append(group)
            del pending[group]
            for token, source in emitted_by.items():
                if source == group:
                    available.add(token)

    deadlocked = sorted(pending)
    for group in deadlocked:
        missing = [token for token in group_tokens[group] if token not in available]
        problems.append(
            f"группа «{group}» не собирается: не появляются токены "
            + ", ".join(f"«{token}»" for token in missing)
        )

    return MetaValidation(
        ok=not problems,
        is_dag=not cycles,
        order=order,
        cycles=cycles,
        deadlocked=deadlocked,
        orphan_tokens=orphans,
        self_loops=self_loops,
        max_depth=max(depth_of.values(), default=0),
        problems=problems,
    )


def _find_cycles(edges: dict[str, set[str]]) -> list[list[str]]:
    """Все простые циклы графа зависимостей. Порядок стабильный."""
    cycles: list[list[str]] = []
    seen_signatures: set[frozenset[str]] = set()
    colour: dict[str, int] = dict.fromkeys(edges, 0)  # 0 бел, 1 сер, 2 чёрн
    stack: list[str] = []

    def walk(node: str) -> None:
        colour[node] = 1
        stack.append(node)
        for nxt in sorted(edges.get(node, ())):
            if colour.get(nxt, 0) == 0:
                walk(nxt)
            elif colour.get(nxt) == 1:
                cycle = stack[stack.index(nxt):]
                signature = frozenset(cycle)
                if signature not in seen_signatures:
                    seen_signatures.add(signature)
                    cycles.append(list(cycle))
        stack.pop()
        colour[node] = 2

    for node in sorted(edges):
        if colour.get(node, 0) == 0:
            walk(node)
    return cycles


def validate_level_in_db(conn: sqlite3.Connection, level_id: int) -> MetaValidation:
    """Та же проверка, но для уже сохранённого уровня."""
    group_tokens: dict[str, list[str]] = {}
    names: dict[int, str] = {}
    for row in conn.execute(
        """
        SELECT g.id AS id, g.position AS position,
               COALESCE(g.reference_name, c.label) AS name
          FROM level_groups g JOIN categories c ON c.id = g.category_id
         WHERE g.level_id = ? ORDER BY g.position
        """,
        (level_id,),
    ):
        names[int(row["id"])] = f"{row['position']}:{row['name']}"
        group_tokens[names[int(row["id"])]] = []

    token_names: dict[int, str] = {}
    for row in conn.execute(
        "SELECT id, group_id, display_text FROM level_tokens "
        " WHERE level_id = ? ORDER BY group_id, slot",
        (level_id,),
    ):
        group_name = names.get(int(row["group_id"]))
        if group_name is None:
            continue
        token_names[int(row["id"])] = row["display_text"]
        group_tokens[group_name].append(row["display_text"])

    emitted_by: dict[str, str] = {}
    for row in conn.execute(
        "SELECT from_group_id, to_token_id FROM level_dependencies WHERE level_id = ?",
        (level_id,),
    ):
        token = token_names.get(int(row["to_token_id"]))
        source = names.get(int(row["from_group_id"]))
        if token is not None and source is not None:
            emitted_by[token] = source

    return validate(group_tokens, emitted_by)
