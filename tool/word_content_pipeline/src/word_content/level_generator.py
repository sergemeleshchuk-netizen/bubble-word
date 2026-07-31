"""Сборка уровней-кандидатов из готовых четвёрок.

Уровень не собирается из пулов. Он собирается из конкретных quartet variants:
пул отвечает на вопрос «какие слова вообще подходят категории», а уровню нужен
ответ «какие ровно четыре слова показать». Случайный `sample(4)` во время игры
запрещён — именно он даёт уровни с двумя правильными ответами.

Порядок сборки:

    выбрать категории (не конфликтующие, не нарушающие cooldown)
    -> взять их четвёрки
    -> собрать токены со значениями и надписями
    -> прогнать exact-cover solver полного уровня
    -> посчитать сложность
    -> сохранить уровень, группы, токены и отчёт solver'а

Уровень принимается автоматически только при `solution_count == 1`. Всё
остальное — включая таймаут — сохраняется как отклонённый кандидат с причиной.
Дальше уровень идёт человеку целиком.
"""

from __future__ import annotations

import hashlib
import json
import random
import sqlite3
from dataclasses import dataclass, field

from . import cooldown as cooldown_mod
from . import difficulty as difficulty_mod
from . import level_solver
from . import meta_validation
from . import profiles as profiles_mod
from . import structured
from .db import utc_now

GENERATOR_VERSION = "level-generator/1.0"
DEFAULT_CATEGORY_COUNT = 5
# Сколько наборов категорий пробовать на один уровень, прежде чем сдаться.
# Неоднозначные наборы отсеиваются solver'ом, и без потолка генератор может
# долго перебирать соседние темы.
MAX_ATTEMPTS_PER_LEVEL = 40


@dataclass
class GroupPlan:
    category_id: int
    category_key: str
    label: str
    quartet_id: int
    concept_id: int | None
    tokens: list[tuple[int, int | None, str, str, str | None]]
    # (word_id, sense_id, display, sense_key|'', role)


@dataclass
class LevelCandidate:
    level_key: str
    groups: list[GroupPlan]
    solver: level_solver.LevelSolverResult
    difficulty: difficulty_mod.DifficultyScore
    assessment: level_solver.PartitionAssessment | None = None
    meta: meta_validation.MetaValidation | None = None
    cooldown_violations: list[cooldown_mod.Violation] = field(default_factory=list)
    reject_reasons: list[str] = field(default_factory=list)
    random_seed: int = 0
    tier: str = "normal"
    target_difficulty: float | None = None

    @property
    def status(self) -> str:
        return "solver_valid" if self.is_valid else "candidate"

    @property
    def is_valid(self) -> bool:
        """Годен, если авторское разбиение уверенно сильнее альтернатив.

        Уровень с единственным разбиением проходит как и раньше. Уровень с
        альтернативой больше не отклоняется автоматически: он проходит, если
        авторский ответ заметно естественнее, а все пересечения либо
        спроектированы, либо слабее авторского дома.
        """
        if self.reject_reasons or self.cooldown_violations:
            return False
        if self.assessment is not None:
            return self.assessment.accepted
        return self.solver.unique

    @property
    def tokens(self) -> list[level_solver.Token]:
        return [
            level_solver.Token(word=display.strip().lower(), sense_key=sense or None,
                               display=display)
            for group in self.groups
            for _word_id, _sense_id, display, sense, _role in group.tokens
        ]

    def content_hash(self) -> str:
        payload = {
            "groups": sorted(
                {
                    "category": group.category_key,
                    "tokens": sorted(
                        f"{display}#{sense}" for _w, _s, display, sense, _r in group.tokens
                    ),
                }.__repr__()
                for group in self.groups
            )
        }
        blob = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()


# --------------------------------------------------------------------- источник четвёрок


def _usable_quartets(
    conn: sqlite3.Connection,
    tier: str,
    *,
    profile: profiles_mod.Profile | None = None,
    rare_familiarity: float = 0.43,
) -> tuple[dict[int, list[dict]], dict[str, int]]:
    """Годные четвёрки по категориям и статистика отсева профилем.

    Выключенная точечным feedback четвёрка (`disabled`) и провалившая валидаторы
    (`invalid`) в генерацию не попадают — ровно для этого их и выключали.
    Дальше, если задан профиль, четвёрка проверяется на пороги качества:
    без этого генератор берёт самые удобные и делает скучные уровни.
    """
    rows = list(
        conn.execute(
            """
            SELECT q.id AS quartet_id, q.category_id AS category_id,
                   c.category_key AS category_key, c.label AS label,
                   c.concept_id AS concept_id, q.difficulty AS difficulty,
                   q.quartet_key AS quartet_key,
                   q.min_word_familiarity AS min_familiarity,
                   q.familiarity_score AS avg_familiarity,
                   q.min_word_accessibility AS min_accessibility,
                   q.label_quality_score AS label_quality,
                   q.quartet_quality_score AS quartet_quality,
                   q.quartet_interest_score AS quartet_interest,
                   q.ambiguity_pressure AS ambiguity,
                   ls.label_char_count AS label_chars, ls.label_token_count AS label_tokens,
                   qw.slot AS slot, qw.word_id AS word_id, qw.sense_id AS sense_id,
                   qw.role AS role,
                   COALESCE(s.display_text, w.text) AS display,
                   COALESCE(s.sense_key, '') AS sense_key,
                   w.familiarity_score AS word_familiarity,
                   ws.char_count AS char_count, ws.token_count AS token_count
              FROM quartets q
              JOIN categories c     ON c.id = q.category_id
              JOIN quartet_words qw ON qw.quartet_id = q.id
              JOIN words w          ON w.id = qw.word_id
              LEFT JOIN word_senses s ON s.id = qw.sense_id
              LEFT JOIN category_label_scores ls ON ls.category_id = c.id
              LEFT JOIN word_scores ws
                     ON ws.word_id = qw.word_id
                    AND COALESCE(ws.sense_id, 0) = COALESCE(qw.sense_id, 0)
             WHERE q.validation_state IN ('auto_validated', 'warning')
               AND q.local_check = 'local_unique'
               AND c.status = 'active'
               -- Чужие авторские группы из записи оригинала в генерацию нового
               -- контента не идут: они здесь как измерительный эталон.
               AND c.origin <> 'reference_backfill'
               AND q.origin <> 'reference_backfill'
               AND (q.tier = ? OR ? = 'hard')
             ORDER BY c.category_key, q.quartet_key, qw.slot
            """,
            (tier, tier),
        )
    )
    quartets: dict[int, dict] = {}
    for row in rows:
        entry = quartets.setdefault(
            int(row["quartet_id"]),
            {
                "quartet_id": int(row["quartet_id"]),
                "quartet_key": row["quartet_key"],
                "category_id": int(row["category_id"]),
                "category_key": row["category_key"],
                "label": row["label"],
                "concept_id": row["concept_id"],
                "difficulty": row["difficulty"],
                "tokens": [],
                "facts_rows": [],
                "scores": {
                    "min_familiarity": row["min_familiarity"],
                    "avg_familiarity": row["avg_familiarity"],
                    "min_accessibility": row["min_accessibility"],
                    "label_quality": row["label_quality"],
                    "quartet_quality": row["quartet_quality"],
                    "quartet_interest": row["quartet_interest"],
                    "ambiguity": row["ambiguity"],
                    "label_chars": row["label_chars"] or len(row["label"]),
                    "label_tokens": row["label_tokens"] or len(row["label"].split()),
                },
            },
        )
        entry["tokens"].append(
            (
                int(row["word_id"]),
                row["sense_id"],
                row["display"],
                row["sense_key"],
                row["role"],
            )
        )
        entry["facts_rows"].append(row)

    stats = {"четвёрок доступно": 0, "отсеяно профилем": 0}
    by_category: dict[int, list[dict]] = {}
    for entry in quartets.values():
        if len(entry["tokens"]) != level_solver.QUARTET_SIZE:
            continue
        entry["facts"] = _quartet_facts(entry, rare_familiarity)
        if profile is not None and profiles_mod.check_quartet(profile, entry["facts"]):
            entry["profile_reasons"] = profiles_mod.check_quartet(profile, entry["facts"])
            stats["отсеяно профилем"] += 1
            continue
        stats["четвёрок доступно"] += 1
        by_category.setdefault(entry["category_id"], []).append(entry)
    return by_category, stats


def _quartet_facts(entry: dict, rare_familiarity: float) -> profiles_mod.QuartetFacts:
    rows = entry["facts_rows"]
    scores = entry["scores"]
    chars = [int(row["char_count"] or len(row["display"])) for row in rows]
    tokens = [int(row["token_count"] or len(str(row["display"]).split())) for row in rows]
    familiarity = [row["word_familiarity"] for row in rows if row["word_familiarity"] is not None]
    return profiles_mod.QuartetFacts(
        quartet_key=entry["quartet_key"],
        min_familiarity=scores["min_familiarity"]
        if scores["min_familiarity"] is not None
        else (min(familiarity) if len(familiarity) == len(rows) else None),
        avg_familiarity=scores["avg_familiarity"],
        min_accessibility=scores["min_accessibility"],
        max_word_chars=max(chars) if chars else 0,
        max_word_tokens=max(tokens) if tokens else 0,
        label_chars=int(scores["label_chars"]),
        label_tokens=int(scores["label_tokens"]),
        label_quality=scores["label_quality"],
        quartet_quality=scores["quartet_quality"],
        quartet_interest=scores["quartet_interest"],
        ambiguity=scores["ambiguity"],
        rare_words=sum(1 for value in familiarity if value < rare_familiarity),
        long_phrases=sum(1 for value in tokens if value >= 3),
    )


def _conflict_map(conn: sqlite3.Connection) -> dict[int, set[int]]:
    conflicts: dict[int, set[int]] = {}
    for row in conn.execute(
        "SELECT category_a_id, category_b_id FROM category_conflicts"
    ):
        a, b = int(row["category_a_id"]), int(row["category_b_id"])
        conflicts.setdefault(a, set()).add(b)
        conflicts.setdefault(b, set()).add(a)
    return conflicts


# ------------------------------------------------------------------------- генерация


def generate(
    conn: sqlite3.Connection,
    *,
    count: int = 5,
    category_count: int = DEFAULT_CATEGORY_COUNT,
    seed: int = 20260731,
    tier: str = "normal",
    target_difficulty: float | None = None,
    config: dict[str, int] | None = None,
    timeout_ms: int = level_solver.DEFAULT_TIMEOUT_MS,
    profile: profiles_mod.Profile | None = None,
    rare_familiarity: float = 0.43,
) -> tuple[list[LevelCandidate], dict[str, int]]:
    """Собирает `count` уровней-кандидатов. Детерминирована при одинаковом seed."""
    config = config or cooldown_mod.load_config()
    by_category, profile_stats = _usable_quartets(
        conn, tier, profile=profile, rare_familiarity=rare_familiarity
    )
    conflicts = _conflict_map(conn)
    index = level_solver.load_memberships(conn)
    structures = structured.load(conn)
    history = cooldown_mod.load_history(conn)

    rng = random.Random(seed)
    category_ids = sorted(by_category)
    stats = {
        "профиль": profile.name if profile else "без профиля",
        **profile_stats,
        "уровней запрошено": count,
        "уровней собрано": 0,
        "solver: unique": 0,
        "solver: ambiguous": 0,
        "solver: timeout": 0,
        "solver: прочее": 0,
        "отклонено по cooldown": 0,
        "отклонено бюджетом уровня": 0,
        "попыток": 0,
    }
    if len(category_ids) < category_count:
        return [], stats

    levels: list[LevelCandidate] = []
    accepted_positions = len(
        list(conn.execute("SELECT 1 FROM level_instances WHERE status = 'accepted'"))
    )

    for number in range(1, count + 1):
        candidate: LevelCandidate | None = None
        for attempt in range(MAX_ATTEMPTS_PER_LEVEL):
            stats["попыток"] += 1
            chosen = _pick_categories(rng, category_ids, conflicts, category_count)
            if chosen is None:
                continue
            # Бюджет уровня тратится по мере набора групп: одно менее очевидное
            # слово делает уровень интереснее, четыре редких — непроходимым.
            budget = profiles_mod.LevelBudget.for_profile(profile) if profile else None
            groups = []
            over_budget = False
            for category_id in chosen:
                group, facts = _group_from(by_category[category_id], rng)
                if budget is not None and facts is not None:
                    problem = budget.fits(facts)
                    if problem:
                        over_budget = True
                        break
                    budget.spend(facts)
                groups.append(group)
            if over_budget:
                stats["отклонено бюджетом уровня"] += 1
                continue
            level_key = f"L{number:03d}"
            built = _evaluate(
                groups,
                level_key=level_key,
                index=index,
                structures=structures,
                history=history,
                config=config,
                position=accepted_positions + number,
                timeout_ms=timeout_ms,
                seed=seed,
                tier=tier,
                target_difficulty=target_difficulty,
            )
            outcome = built.solver.outcome
            stats[
                {
                    "unique": "solver: unique",
                    "ambiguous": "solver: ambiguous",
                    "timeout": "solver: timeout",
                }.get(outcome, "solver: прочее")
            ] += 1
            if built.cooldown_violations:
                stats["отклонено по cooldown"] += 1
            if built.is_valid:
                candidate = built
                break
            # Последняя попытка сохраняется как есть: отклонённый кандидат
            # с причиной полезнее, чем молчание генератора.
            candidate = built
        if candidate is None:
            continue
        levels.append(candidate)
        stats["уровней собрано"] += 1
        if candidate.is_valid:
            history.remember(
                accepted_positions + number,
                word_senses=[
                    (word_id, sense_id)
                    for group in candidate.groups
                    for word_id, sense_id, _d, _s, _r in group.tokens
                ],
                category_ids=[group.category_id for group in candidate.groups],
                concept_ids=[
                    group.concept_id for group in candidate.groups if group.concept_id
                ],
                quartet_ids=[group.quartet_id for group in candidate.groups],
            )
    return levels, stats


def _pick_categories(
    rng: random.Random,
    category_ids: list[int],
    conflicts: dict[int, set[int]],
    category_count: int,
) -> list[int] | None:
    """Выбирает непротиворечивый набор категорий.

    Конфликты — это предварительно посчитанные пары, чьи пулы пересекаются
    настолько, что четвёрка одной лежит в другой. Они ускоряют отбор, но
    не заменяют solver: неоднозначность бывает и при пересечении в одно слово.
    """
    chosen: list[int] = []
    pool = category_ids[:]
    rng.shuffle(pool)
    for category_id in pool:
        if any(category_id in conflicts.get(picked, ()) for picked in chosen):
            continue
        chosen.append(category_id)
        if len(chosen) == category_count:
            return sorted(chosen)
    return None


def _group_from(
    quartets: list[dict], rng: random.Random
) -> tuple[GroupPlan, profiles_mod.QuartetFacts | None]:
    entry = quartets[rng.randrange(len(quartets))]
    plan = GroupPlan(
        category_id=entry["category_id"],
        category_key=entry["category_key"],
        label=entry["label"],
        quartet_id=entry["quartet_id"],
        concept_id=entry["concept_id"],
        tokens=list(entry["tokens"]),
    )
    return plan, entry.get("facts")


def _evaluate(
    groups: list[GroupPlan],
    *,
    level_key: str,
    index: level_solver.MembershipIndex,
    structures: structured.StructureIndex,
    history: cooldown_mod.UsageHistory,
    config: dict[str, int],
    position: int,
    timeout_ms: int,
    seed: int,
    tier: str,
    target_difficulty: float | None,
) -> LevelCandidate:
    tokens = [
        level_solver.Token(
            word=display.strip().lower(), sense_key=sense or None, display=display
        )
        for group in groups
        for _word_id, _sense_id, display, sense, _role in group.tokens
    ]
    homes = {
        display.strip().lower(): group.category_key
        for group in groups
        for _word_id, _sense_id, display, _sense, _role in group.tokens
    }
    # Мета-механика проверяется до solver'а: непроходимый уровень не спасает
    # никакая единственность разбиения.
    meta = meta_validation.validate(
        {
            group.category_key: [display for _w, _s, display, _sk, _r in group.tokens]
            for group in groups
        },
        {},
    )
    assessment = level_solver.assess_partition(
        tokens, homes, index, structures, timeout_ms=timeout_ms,
        meta_ok=meta.ok, meta_problems=meta.problems,
    )
    result = assessment.solver or level_solver.solve_level(
        tokens, index, structures, timeout_ms=timeout_ms
    )
    violations = cooldown_mod.check(
        position=position,
        history=history,
        config=config,
        word_senses=[
            (word_id, sense_id)
            for group in groups
            for word_id, sense_id, _d, _s, _r in group.tokens
        ],
        category_ids=[group.category_id for group in groups],
        concept_ids=[group.concept_id for group in groups if group.concept_id],
        quartet_ids=[group.quartet_id for group in groups],
        labels=[group.label for group in groups],
        displays=[token.display_text for token in tokens],
    )
    facts = _facts(groups, tokens, index, result)
    reject: list[str] = list(assessment.hard_reject)
    return LevelCandidate(
        level_key=level_key,
        groups=groups,
        solver=result,
        assessment=assessment,
        meta=meta,
        difficulty=difficulty_mod.score(facts),
        cooldown_violations=violations,
        reject_reasons=reject,
        random_seed=seed,
        tier=tier,
        target_difficulty=target_difficulty,
    )


def _facts(
    groups: list[GroupPlan],
    tokens: list[level_solver.Token],
    index: level_solver.MembershipIndex,
    result: level_solver.LevelSolverResult,
) -> difficulty_mod.LevelFacts:
    """Всё, что модель сложности знает об уровне."""
    own = {group.category_key for group in groups}
    competing = 0
    for token in tokens:
        others = [
            key
            for key in index.by_word.get(token.word, ())
            if key not in own and index.matches(key, token)
        ]
        if others:
            competing += 1
    overlaps: list[int] = []
    for i, first in enumerate(groups):
        for second in groups[i + 1:]:
            shared = sum(
                1
                for token in tokens
                if index.matches(first.category_key, token)
                and index.matches(second.category_key, token)
            )
            if shared:
                overlaps.append(shared)
    return difficulty_mod.LevelFacts(
        category_count=len(groups),
        total_tokens=len(tokens),
        familiarity_scores=[],  # заполняется вызывающей стороной при наличии данных
        ambiguous_tokens=sum(1 for token in tokens if token.word in index.polysemous),
        pairwise_overlaps=overlaps,
        alternative_interpretations=competing,
        plausible_first_groups=len(groups),
        structured_categories=0,
        max_phrase_length=max((len(token.display_text.split()) for token in tokens), default=1),
        meta_depth=0,
    )


# --------------------------------------------------------------------------- сохранение


def save(
    conn: sqlite3.Connection, levels: list[LevelCandidate], *, run_id: int | None = None
) -> int:
    """Пишет уровни, группы, токены и отчёты solver'а. Повторный запуск перезаписывает."""
    now = utc_now()
    saved = 0
    for level in levels:
        existing = conn.execute(
            "SELECT id, status FROM level_instances WHERE level_key = ?", (level.level_key,)
        ).fetchone()
        if existing is not None and existing["status"] in ("accepted", "rejected", "needs_changes"):
            # Решение человека по уровню не затирается пересборкой кандидата.
            continue
        if existing is not None:
            conn.execute("DELETE FROM level_instances WHERE id = ?", (existing["id"],))

        cur = conn.execute(
            """
            INSERT INTO level_instances
                (level_key, target_difficulty, difficulty_score, difficulty_components,
                 difficulty_model_version, difficulty_explanation, tier, status,
                 solution_count, content_hash, generator_version, random_seed,
                 source_run_id, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                level.level_key,
                level.target_difficulty,
                level.difficulty.total_score,
                json.dumps(level.difficulty.component_scores, ensure_ascii=False),
                level.difficulty.model_version,
                level.difficulty.short_explanation,
                level.tier,
                level.status,
                level.solver.solution_count,
                level.content_hash(),
                GENERATOR_VERSION,
                level.random_seed,
                run_id,
                now,
                now,
            ),
        )
        level_id = int(cur.lastrowid)

        for position, group in enumerate(level.groups, start=1):
            group_cur = conn.execute(
                """
                INSERT INTO level_groups
                    (level_id, position, category_id, quartet_id, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (level_id, position, group.category_id, group.quartet_id, now),
            )
            group_id = int(group_cur.lastrowid)
            for slot, (word_id, sense_id, display, sense_key, role) in enumerate(
                group.tokens, start=1
            ):
                conn.execute(
                    """
                    INSERT INTO level_tokens
                        (level_id, group_id, slot, word_id, sense_id, sense_mode,
                         display_text, role, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        level_id,
                        group_id,
                        slot,
                        word_id,
                        sense_id,
                        "lexical" if sense_key else "surface_form",
                        display,
                        role,
                        now,
                    ),
                )

        alternative = level.solver.alternative_partition
        assessment = level.assessment
        conn.execute(
            """
            INSERT INTO level_solver_runs
                (level_id, solver_version, input_hash, parameters, outcome,
                 solution_count, alternative_partition, reason, duration_ms, checked_at,
                 intended_partition_score, best_alternative_score, partition_margin,
                 planned_decoy_count, unplanned_decoy_count, intended_is_best)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                level_id,
                level.solver.solver_version,
                level.solver.input_hash,
                json.dumps(level.solver.parameters, ensure_ascii=False),
                level.solver.outcome,
                level.solver.solution_count,
                level_solver.format_solution(alternative) if alternative else None,
                "; ".join(level.reject_reasons) or level.solver.reason,
                level.solver.duration_ms,
                now,
                assessment.intended_partition_score if assessment else None,
                assessment.best_alternative_score if assessment else None,
                assessment.partition_margin if assessment else None,
                assessment.planned_decoy_count if assessment else 0,
                assessment.unplanned_decoy_count if assessment else 0,
                (1 if assessment.intended_is_best else 0) if assessment else None,
            ),
        )
        if assessment is not None:
            conn.execute(
                """
                UPDATE level_instances
                   SET intended_partition_score = ?, best_alternative_score = ?,
                       partition_margin = ?, planned_decoy_count = ?,
                       unplanned_decoy_count = ?, meta_state = ?
                 WHERE id = ?
                """,
                (
                    assessment.intended_partition_score,
                    assessment.best_alternative_score,
                    assessment.partition_margin,
                    assessment.planned_decoy_count,
                    assessment.unplanned_decoy_count,
                    json.dumps(level.meta.as_dict(), ensure_ascii=False)
                    if level.meta else None,
                    level_id,
                ),
            )
        saved += 1
    return saved


def record_run(
    conn: sqlite3.Connection,
    *,
    run_kind: str,
    parameters: dict[str, object],
    records_out: int,
    random_seed: int | None = None,
    source_commit: str | None = None,
    note: str | None = None,
) -> int:
    cur = conn.execute(
        """
        INSERT INTO content_runs
            (run_kind, tool_version, source_commit, random_seed, parameters,
             records_out, status, note, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'ok', ?, ?)
        """,
        (
            run_kind,
            GENERATOR_VERSION,
            source_commit,
            random_seed,
            json.dumps(parameters, ensure_ascii=False, sort_keys=True),
            records_out,
            note,
            utc_now(),
        ),
    )
    return int(cur.lastrowid)
