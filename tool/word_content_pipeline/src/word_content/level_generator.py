"""Сборка уровней-кандидатов из готовых четвёрок.

Уровень не собирается из пулов. Он собирается из конкретных quartet variants:
пул отвечает на вопрос «какие слова вообще подходят категории», а уровню нужен
ответ «какие ровно четыре слова показать». Случайный `sample(4)` во время игры
запрещён — именно он даёт уровни с двумя правильными ответами.

Порядок сборки:

    заложить мета-ядро (кто чей результат выпускает)
    -> добрать категории (не конфликтующие, не нарушающие cooldown)
    -> взять их четвёрки
    -> собрать токены со значениями и надписями
    -> проверить мета-граф симуляцией прохождения
    -> прогнать exact-cover solver полного уровня
    -> посчитать сложность
    -> сохранить уровень, группы, токены, мета-зависимости и отчёт solver'а

Мета-ядро закладывается первым, а не дописывается к готовому набору. Причина
арифметическая: мета-пара — это совпадение слова одной четвёрки с надписью
другого правила, и таких совпадений на всю базу 162. Вероятность, что они
сами найдутся внутри случайно выбранной восьмёрки категорий, околонулевая —
именно поэтому предыдущая версия генератора выдавала ровно ноль мета-связей
при 52 в записи оригинала.

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
from pathlib import Path

from . import composition as composition_mod
from . import cooldown as cooldown_mod
from . import difficulty as difficulty_mod
from . import level_solver
from . import meta_pairs as meta_pairs_mod
from . import meta_validation
from . import profiles as profiles_mod
from . import structured
from .db import utc_now

GENERATOR_VERSION = "level-generator/1.1"
DEFAULT_CATEGORY_COUNT = 5
# Сколько наборов категорий пробовать на один уровень, прежде чем сдаться.
# Неоднозначные наборы отсеиваются solver'ом, и без потолка генератор может
# долго перебирать соседние темы.
MAX_ATTEMPTS_PER_LEVEL = 40
# Сколько четвёрок одного правила перебрать при доборе, прежде чем идти
# к следующему правилу: первая попавшаяся часто занята перезарядкой.
FILLER_TRIES_PER_RULE = 5


@dataclass
class GroupPlan:
    category_id: int
    category_key: str
    label: str
    quartet_id: int
    concept_id: int | None
    tokens: list[tuple[int, int | None, str, str, str | None]]
    # (word_id, sense_id, display, sense_key|'', role)
    # Надпись, под которой группа показана на этом уровне. Заполняется только
    # у источника мета-связи: его имя обязано совпасть с выпущенным пузырём.
    display_label_id: int | None = None


@dataclass(frozen=True)
class MetaLink:
    """Связь уровня: собранная группа-источник оставляет пузырь потребителю."""

    source_key: str
    consumer_key: str
    token_display: str
    source_label: str
    source_label_id: int
    depth: int = 1

    def as_dict(self) -> dict[str, object]:
        return {
            "token": self.token_display,
            "source_group": self.source_key,
            "target_group": self.consumer_key,
            "source_label": self.source_label,
            "depth": self.depth,
        }


@dataclass
class LevelCandidate:
    level_key: str
    groups: list[GroupPlan]
    solver: level_solver.LevelSolverResult
    difficulty: difficulty_mod.DifficultyScore
    assessment: level_solver.PartitionAssessment | None = None
    meta: meta_validation.MetaValidation | None = None
    meta_links: list[MetaLink] = field(default_factory=list)
    composition: composition_mod.Composition | None = None
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


@dataclass(frozen=True)
class _QuartetPool:
    """Годные четвёрки под один профиль качества, разложенные по входам."""

    by_category: dict[int, list[dict]]
    by_quartet_id: dict[int, dict]
    category_ids: list[int]
    concept_by_category: dict[int, int]
    stats: dict[str, int]


class _PoolCache:
    """Пулы четвёрок по профилям: у каждого профиля свой отбор.

    Профиль задаётся не на прогон, а на уровень: первые уровни кампании берут
    только знакомые слова, поздние — знание предметной области. Отбор четвёрок
    под каждый профиль считается один раз и переиспользуется.
    """

    def __init__(
        self,
        conn: sqlite3.Connection,
        *,
        tier: str,
        rare_familiarity: float,
    ) -> None:
        self._conn = conn
        self._tier = tier
        self._rare = rare_familiarity
        self._pools: dict[str, _QuartetPool] = {}

    def get(self, profile: profiles_mod.Profile | None) -> _QuartetPool:
        key = profile.name if profile else ""
        if key not in self._pools:
            by_category, stats = _usable_quartets(
                self._conn, self._tier, profile=profile, rare_familiarity=self._rare
            )
            self._pools[key] = _QuartetPool(
                by_category=by_category,
                by_quartet_id={
                    entry["quartet_id"]: entry
                    for entries in by_category.values()
                    for entry in entries
                },
                category_ids=sorted(by_category),
                concept_by_category={
                    category_id: entries[0]["concept_id"]
                    for category_id, entries in by_category.items()
                    if entries and entries[0]["concept_id"] is not None
                },
                stats=stats,
            )
        return self._pools[key]


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
    category_count: int | None = DEFAULT_CATEGORY_COUNT,
    seed: int = 20260731,
    tier: str = "normal",
    target_difficulty: float | None = None,
    config: dict[str, int] | None = None,
    timeout_ms: int = level_solver.DEFAULT_TIMEOUT_MS,
    profile: profiles_mod.Profile | None = None,
    rare_familiarity: float = 0.43,
    use_meta: bool = True,
    meta_target: int | None = None,
    key_prefix: str = "L",
    auto_profile: bool = False,
    profiles_config: Path | None = None,
) -> tuple[list[LevelCandidate], dict[str, int]]:
    """Собирает `count` уровней-кандидатов. Детерминирована при одинаковом seed.

    ``category_count``  сколько категорий в уровне; ``None`` означает «по записи»:
                        состав каждого номера берётся из профиля композиции,
                        то есть 5 категорий на первом уровне и 12 на седьмом;
    ``use_meta``        собирать ли мета-связи; выключение оставляет плоские уровни;
    ``meta_target``     сколько связей просить на уровень вместо профиля композиции;
    ``key_prefix``      префикс ключей уровней. Отдельный пакет живёт под своим
                        префиксом и не затирается дымовым прогоном сборки,
                        который каждый раз пересобирает `L001..L005`;
    ``auto_profile``    брать профиль качества по номеру уровня: первые уровни
                        только из знакомых слов, поздние — со знанием. Явный
                        ``profile`` сильнее и отменяет это.
    """
    config = config or cooldown_mod.load_config()
    pools = _PoolCache(conn, tier=tier, rare_familiarity=rare_familiarity)
    base_pool = pools.get(profile)
    conflicts = _conflict_map(conn)
    meta_index = meta_pairs_mod.load(conn, tier=tier) if use_meta else meta_pairs_mod.MetaIndex()
    index = level_solver.load_memberships(conn)
    structures = structured.load(conn)
    history = cooldown_mod.load_history(conn)

    rng = random.Random(seed)
    stats = {
        "профиль": profile.name if profile else (
            "по номеру уровня" if auto_profile else "без профиля"
        ),
        **base_pool.stats,
        "мета-пар в базе": len(meta_index.distinct_pairs()),
        "уровней запрошено": count,
        "уровней собрано": 0,
        "solver: unique": 0,
        "solver: ambiguous": 0,
        "solver: timeout": 0,
        "solver: прочее": 0,
        "отклонено по cooldown": 0,
        "отклонено бюджетом уровня": 0,
        "четвёрок пропущено по повтору слова": 0,
        "четвёрок пропущено по перезарядке": 0,
        "мета-связей поставлено": 0,
        "уровней с мета": 0,
        "мета: недобор до профиля": 0,
        "отклонено мета-проверкой": 0,
        "попыток": 0,
    }
    if len(base_pool.category_ids) < (
        category_count or composition_mod.MAX_RECORDED_CATEGORIES
    ):
        return [], stats

    levels: list[LevelCandidate] = []
    accepted_positions = len(
        list(conn.execute("SELECT 1 FROM level_instances WHERE status = 'accepted'"))
    )

    for number in range(1, count + 1):
        candidate: LevelCandidate | None = None
        position = accepted_positions + number
        plan = composition_mod.for_level(position)
        # Без явного числа категорий уровень повторяет состав записи: пять
        # категорий на первом, двенадцать на седьмом, семь на пятнадцатом.
        level_categories = category_count or plan.categories
        level_profile = profile
        if level_profile is None and auto_profile:
            level_profile = profiles_mod.get(plan.profile, profiles_config)
        pool = pools.get(level_profile)
        wanted_meta = (
            meta_target if meta_target is not None else plan.meta_target(level_categories)
        )
        if not use_meta:
            wanted_meta = 0
        for attempt in range(MAX_ATTEMPTS_PER_LEVEL):
            stats["попыток"] += 1
            cooling = _cooling_categories(
                history, config, position=position,
                concept_by_category=pool.concept_by_category,
            )
            built_plan = _plan_level(
                rng,
                by_category=pool.by_category,
                by_quartet_id=pool.by_quartet_id,
                category_ids=pool.category_ids,
                conflicts=conflicts,
                cooling=cooling,
                hot=_cooling_content(history, config, position=position),
                category_count=level_categories,
                meta_index=meta_index,
                meta_target=wanted_meta,
                index=index,
                stats=stats,
            )
            if built_plan is None:
                continue
            groups, links = built_plan
            # Бюджет уровня тратится по мере набора групп: одно менее очевидное
            # слово делает уровень интереснее, четыре редких — непроходимым.
            budget = (
                profiles_mod.LevelBudget.for_profile(level_profile)
                if level_profile else None
            )
            over_budget = False
            if budget is not None:
                for group in groups:
                    facts = pool.by_quartet_id[group.quartet_id].get("facts")
                    if facts is None:
                        continue
                    if budget.fits(facts):
                        over_budget = True
                        break
                    budget.spend(facts)
            if over_budget:
                stats["отклонено бюджетом уровня"] += 1
                continue
            level_key = f"{key_prefix}{number:03d}"
            built = _evaluate(
                groups,
                links,
                level_key=level_key,
                index=index,
                structures=structures,
                history=history,
                config=config,
                position=position,
                timeout_ms=timeout_ms,
                seed=seed,
                tier=tier,
                target_difficulty=target_difficulty,
                composition=plan,
            )
            if built.meta is not None and not built.meta.ok:
                stats["отклонено мета-проверкой"] += 1
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
        stats["мета-связей поставлено"] += len(candidate.meta_links)
        if candidate.meta_links:
            stats["уровней с мета"] += 1
        if len(candidate.meta_links) < wanted_meta:
            stats["мета: недобор до профиля"] += 1
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


def _cooling_categories(
    history: cooldown_mod.UsageHistory,
    config: dict[str, int],
    *,
    position: int,
    concept_by_category: dict[int, int],
) -> set[int]:
    """Правила, которые сейчас нельзя брать: слишком недавно использовались.

    Без этого множества генератор узнавал о перезарядке слишком поздно: он
    собирал уровень целиком, прогонял solver и только потом выяснял, что одно
    из восьми правил встречалось десять уровней назад. На сотом уровне почти
    любая случайная восьмёрка содержала такое правило, сорок попыток
    заканчивались ничем, и уровень сохранялся с нарушением. Замер: из 600
    уровней проверки проходили 343, при этом solver у 161 из отклонённых писал
    «разбиение единственное» — то есть уровни были правильные.
    """
    cooling: set[int] = set()
    variant_gap = config.get("same_category_variant", 0)
    concept_gap = config.get("same_category_concept", 0)
    for category_id, last in history.category_variant.items():
        if variant_gap and position - last < variant_gap:
            cooling.add(category_id)
    if concept_gap:
        hot_concepts = {
            concept_id
            for concept_id, last in history.category_concept.items()
            if position - last < concept_gap
        }
        cooling.update(
            category_id
            for category_id, concept_id in concept_by_category.items()
            if concept_id in hot_concepts
        )
    return cooling


@dataclass(frozen=True)
class _HotContent:
    """Что сейчас на перезарядке: слова и четвёрки, повтор которых ещё рано."""

    word_senses: frozenset[tuple[int, int | None]] = frozenset()
    quartets: frozenset[int] = frozenset()

    def blocks(self, entry: dict) -> bool:
        if entry["quartet_id"] in self.quartets:
            return True
        return any(
            (word_id, sense_id) in self.word_senses
            for word_id, sense_id, _d, _sk, _r in entry["tokens"]
        )


def _cooling_content(
    history: cooldown_mod.UsageHistory,
    config: dict[str, int],
    *,
    position: int,
) -> _HotContent:
    """Слова и четвёрки, которые на этой позиции повторять ещё нельзя.

    Раньше повтор слова ловился только постфактум: генератор собирал уровень
    целиком, считал solver и лишь потом узнавал, что слово встречалось восемь
    уровней назад при требуемых двадцати. На пакете из двадцати уровней по
    десять категорий так отбраковывалась почти каждая вторая попытка, и часть
    уровней сохранялась прямо с нарушением. Дешевле не брать такую четвёрку.
    """
    word_gap = config.get("same_word_sense", 0)
    quartet_gap = config.get("same_quartet", 0)
    return _HotContent(
        word_senses=frozenset(
            key
            for key, last in history.word_sense.items()
            if word_gap and position - last < word_gap
        ),
        quartets=frozenset(
            quartet_id
            for quartet_id, last in history.quartet.items()
            if quartet_gap and position - last < quartet_gap
        ),
    )


def _plan_level(
    rng: random.Random,
    *,
    by_category: dict[int, list[dict]],
    by_quartet_id: dict[int, dict],
    category_ids: list[int],
    conflicts: dict[int, set[int]],
    cooling: set[int],
    hot: _HotContent | None = None,
    category_count: int,
    meta_index: meta_pairs_mod.MetaIndex,
    meta_target: int,
    index: level_solver.MembershipIndex | None = None,
    stats: dict[str, int] | None = None,
) -> tuple[list[GroupPlan], list[MetaLink]] | None:
    """Набирает состав уровня: сначала мета-ядро, потом обычные группы.

    Порядок обязателен. Мета-пара — редкое совпадение: 162 пары, 330 четвёрок
    из 14 184. Искать её внутри уже выбранного набора значит не находить.

    Глубина цепочки держится на одном правиле: **источник не может быть
    потребителем**. Тогда любая цепочка ровно двухшаговая — как в оригинале,
    где третьего порядка нет ни на одном из двадцати уровней. Обратное
    (несколько источников на одного потребителя) разрешено: именно так устроен
    уровень 7 записи, где `measurements` собирается из четырёх чужих
    результатов.
    """
    chosen: dict[int, GroupPlan] = {}
    links: list[MetaLink] = []
    sources: set[int] = set()
    consumers: set[int] = set()
    used_displays: set[str] = set()
    hot = hot or _HotContent()

    def blocked(category_id: int) -> bool:
        if category_id in chosen:
            return True
        return any(category_id in conflicts.get(picked, ()) for picked in chosen)

    def take(
        entry: dict,
        *,
        display_label_id: int | None = None,
        display_label: str | None = None,
    ) -> GroupPlan | None:
        """Ставит четвёрку в уровень, если она не повторяет уже занятое слово.

        Повтор отсекается здесь, а не проверкой готового уровня: одно общее
        слово у двух групп — это два пузыря с одной надписью, игрок их не
        различит, а база не сохранит. На пяти категориях совпадение почти не
        встречалось, на восьми ломало сборку.
        """
        displays = {
            display.strip().lower() for _w, _s, display, _sk, _r in entry["tokens"]
        }
        if len(displays) != level_solver.QUARTET_SIZE or displays & used_displays:
            if stats is not None:
                stats["четвёрок пропущено по повтору слова"] += 1
            return None
        if hot.blocks(entry):
            if stats is not None:
                stats["четвёрок пропущено по перезарядке"] += 1
            return None
        plan = _plan_from_entry(
            entry, display_label_id=display_label_id, display_label=display_label
        )
        chosen[plan.category_id] = plan
        used_displays.update(displays)
        return plan

    if meta_target > 0 and len(meta_index) > 0:
        quartet_ids = [
            quartet_id
            for quartet_id in meta_index.by_quartet
            if quartet_id in by_quartet_id
        ]
        rng.shuffle(quartet_ids)
        for quartet_id in quartet_ids:
            if len(links) >= meta_target or len(chosen) >= category_count - 1:
                break
            consumer_entry = by_quartet_id[quartet_id]
            consumer_id = consumer_entry["category_id"]
            if consumer_id in sources or consumer_id in cooling or blocked(consumer_id):
                continue
            pairs = [
                pair
                for pair in meta_index.for_quartet(quartet_id)
                if _pair_pools_are_clean(pair, consumer_entry, by_category, index)
            ]
            rng.shuffle(pairs)
            taken = _attach_sources(
                rng, pairs,
                consumer_entry=consumer_entry,
                by_category=by_category,
                conflicts=conflicts,
                cooling=cooling,
                chosen=chosen,
                sources=sources,
                consumers=consumers,
                links=links,
                take=take,
                blocked=blocked,
                index=index,
                category_count=category_count,
                remaining=meta_target - len(links),
            )
            if taken:
                consumers.add(consumer_id)

    # Добор обычными группами. Правила на перезарядке не берутся, но если
    # свободных не хватает, лучше собрать уровень и показать нарушение, чем
    # молча вернуть ничего.
    pool = [
        category_id
        for category_id in category_ids
        if category_id not in chosen and category_id not in cooling
    ]
    if len(pool) < category_count - len(chosen):
        pool = [category_id for category_id in category_ids if category_id not in chosen]
    rng.shuffle(pool)
    for category_id in pool:
        if len(chosen) >= category_count:
            break
        if blocked(category_id):
            continue
        entries = by_category[category_id]
        # Несколько попыток на правило: у категории обычно много четвёрок, и
        # первая попавшаяся часто занята перезарядкой или уже занятым словом.
        for _ in range(min(FILLER_TRIES_PER_RULE, len(entries))):
            if take(entries[rng.randrange(len(entries))]) is not None:
                break

    if len(chosen) < category_count:
        return None
    groups = [chosen[category_id] for category_id in sorted(chosen)]
    return groups, links


def _pair_pools_are_clean(
    pair: meta_pairs_mod.MetaPair,
    consumer_entry: dict,
    by_category: dict[int, list[dict]],
    index: level_solver.MembershipIndex | None,
) -> bool:
    """Не тянет ли мета-пара за собой чужое слово.

    Правила мета-пары близки по смыслу по построению: надпись одного является
    словом другого. Поэтому их пулы пересекаются чаще обычного, и пересечение
    приходит не в самой связи, а в соседнем слове. Замеренный случай: TURTLES
    выпускает «turtles» для REPTILES, но в четвёрке TURTLES стоит `tortoise`,
    который тянет в REPTILES сильнее (0.87 против 0.82). Solver такой уровень
    отклоняет — правильно, но уже после сборки, и два уровня пакета из двадцати
    уходили в брак по одной и той же паре.

    Проверяются оба направления: слово источника, годное потребителю, и слово
    потребителя, годное источнику. Сам мета-токен исключён — он и должен быть
    словом потребителя.
    """
    if index is None:
        return True
    if not _entry_free_of(consumer_entry, pair.source_key, index, skip=pair.token_display):
        return False
    return any(
        _entry_free_of(entry, pair.consumer_key, index)
        for entry in by_category.get(pair.source_id, ())
    )


def _entry_free_of(
    entry: dict,
    rule_key: str,
    index: level_solver.MembershipIndex,
    *,
    skip: str | None = None,
) -> bool:
    """Нет ли в четвёрке слова, которое годится и чужому правилу."""
    return not any(
        index.matches(
            rule_key,
            level_solver.Token(
                word=display.strip().lower(), sense_key=sense or None, display=display
            ),
        )
        for _w, _s, display, sense, _r in entry["tokens"]
        if display != skip
    )


def _attach_sources(
    rng: random.Random,
    pairs: list[meta_pairs_mod.MetaPair],
    *,
    consumer_entry: dict,
    by_category: dict[int, list[dict]],
    conflicts: dict[int, set[int]],
    cooling: set[int],
    chosen: dict[int, GroupPlan],
    sources: set[int],
    consumers: set[int],
    links: list[MetaLink],
    take,
    blocked,
    index: level_solver.MembershipIndex | None,
    category_count: int,
    remaining: int,
) -> bool:
    """Ставит потребителя и его источники. Возвращает, получилось ли хоть что-то."""
    consumer_id = consumer_entry["category_id"]
    consumer_plan: GroupPlan | None = None
    added = 0
    for pair in pairs:
        if added >= remaining:
            break
        room = category_count - len(chosen)
        source_id = pair.source_id
        if source_id == consumer_id or source_id in consumers:
            continue
        if source_id in cooling and source_id not in chosen:
            continue
        if source_id in conflicts.get(consumer_id, ()):
            continue
        already = chosen.get(source_id)
        if already is not None:
            # Источник уже стоит на уровне: годится, только если он показан под
            # той же надписью — у группы одно имя, а не список синонимов.
            if source_id not in sources or already.display_label_id != pair.source_label_id:
                continue
        elif blocked(source_id):
            continue
        need = (1 if consumer_plan is None else 0) + (1 if already is None else 0)
        if room < need:
            break
        if consumer_plan is None:
            consumer_plan = take(consumer_entry)
            if consumer_plan is None:
                return False
        if already is None:
            entries = [
                entry
                for entry in (by_category.get(source_id) or [])
                if index is None or _entry_free_of(entry, pair.consumer_key, index)
            ]
            source_plan = None
            for _ in range(min(4, len(entries))):
                candidate = entries[rng.randrange(len(entries))]
                source_plan = take(
                    candidate,
                    display_label_id=pair.source_label_id,
                    display_label=pair.source_label,
                )
                if source_plan is not None:
                    break
            if source_plan is None:
                continue
        links.append(
            MetaLink(
                source_key=pair.source_key,
                consumer_key=pair.consumer_key,
                token_display=pair.token_display,
                source_label=pair.source_label,
                source_label_id=pair.source_label_id,
            )
        )
        sources.add(source_id)
        added += 1
    return added > 0


def _plan_from_entry(
    entry: dict,
    *,
    display_label_id: int | None = None,
    display_label: str | None = None,
) -> GroupPlan:
    """Группа уровня из конкретной четвёрки.

    Надпись берётся не всегда из правила: источник мета-связи показан под той
    надписью, которая совпадает с выпущенным пузырём, иначе связь на экране не
    читается. Правило при этом остаётся тем же — разделение надписи и правила
    ради этого и делалось.
    """
    return GroupPlan(
        category_id=entry["category_id"],
        category_key=entry["category_key"],
        label=display_label or entry["label"],
        quartet_id=entry["quartet_id"],
        concept_id=entry["concept_id"],
        tokens=list(entry["tokens"]),
        display_label_id=display_label_id,
    )


def _evaluate(
    groups: list[GroupPlan],
    links: list[MetaLink],
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
    composition: composition_mod.Composition | None = None,
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
        {link.token_display: link.source_key for link in links},
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
    facts = _facts(groups, tokens, index, result, meta=meta)
    reject: list[str] = list(assessment.hard_reject)
    return LevelCandidate(
        level_key=level_key,
        groups=groups,
        solver=result,
        assessment=assessment,
        meta=meta,
        meta_links=list(links),
        composition=composition,
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
    *,
    meta: meta_validation.MetaValidation | None = None,
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
        # Плоский уровень собирается в один слой, и его глубина в симуляции
        # равна 1. Сложность добавляет только надстройка над этим слоем.
        meta_depth=max(0, (meta.max_depth if meta else 1) - 1),
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

        group_ids: dict[str, int] = {}
        token_ids: dict[tuple[str, str], int] = {}
        for position, group in enumerate(level.groups, start=1):
            group_cur = conn.execute(
                """
                INSERT INTO level_groups
                    (level_id, position, category_id, quartet_id, display_label_id,
                     created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    level_id, position, group.category_id, group.quartet_id,
                    group.display_label_id, now,
                ),
            )
            group_id = int(group_cur.lastrowid)
            group_ids[group.category_key] = group_id
            for slot, (word_id, sense_id, display, sense_key, role) in enumerate(
                group.tokens, start=1
            ):
                token_cur = conn.execute(
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
                token_ids[(group.category_key, display)] = int(token_cur.lastrowid)

        # Мета-связи: пузырь перестаёт быть обычным словом и становится
        # результатом другой группы. Пишем обе стороны — и роль токена, и
        # ребро зависимости, — иначе `validate-meta` увидит плоский уровень.
        for link in level.meta_links:
            token_id = token_ids.get((link.consumer_key, link.token_display))
            source_group_id = group_ids.get(link.source_key)
            if token_id is None or source_group_id is None:
                continue
            conn.execute(
                """
                UPDATE level_tokens
                   SET token_kind = 'category_output', token_form = 'word',
                       source_group_id = ?
                 WHERE id = ?
                """,
                (source_group_id, token_id),
            )
            conn.execute(
                """
                INSERT OR IGNORE INTO level_dependencies
                    (level_id, from_group_id, to_token_id, depth, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (level_id, source_group_id, token_id, link.depth, now),
            )
            conn.execute(
                "UPDATE level_groups SET emits_token_id = ? WHERE id = ?",
                (token_id, source_group_id),
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
