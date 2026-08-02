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
from . import decoy_pairs as decoy_pairs_mod
from . import difficulty as difficulty_mod
from . import labels as labels_mod
from . import level_solver
from . import meta_pairs as meta_pairs_mod
from . import meta_validation
from . import profiles as profiles_mod
from . import quartet_semantics
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
class PlannedDecoy:
    """Объявленная ловушка уровня: пузырь группы A, который просится в B."""

    token_display: str
    home_key: str
    rival_key: str
    home_strength: float
    rival_strength: float

    def as_dict(self) -> dict[str, object]:
        return {
            "token": self.token_display,
            "home": self.home_key,
            "rival": self.rival_key,
            "home_strength": round(self.home_strength, 3),
            "rival_strength": round(self.rival_strength, 3),
        }


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
    planned_decoys: list[PlannedDecoy] = field(default_factory=list)
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
                   c.rule_type AS rule_type,
                   qw.sense_mode AS sense_mode,
                   w.normalized AS normalized,
                   -- Слой доступности значения: чем `Trouble` в BOARD GAMES
                   -- отличается от `orange` в COLORS. Читается прямо со слота
                   -- четвёрки, а не со связи: значение выбрано именно здесь.
                   COALESCE(s.accessibility_class, 'unresolved') AS accessibility_class,
                   CASE
                       WHEN qw.sense_mode = 'surface_form' THEN 'surface_form'
                       WHEN qw.sense_id IS NULL            THEN 'unresolved'
                       WHEN s.accessibility_class = 'primary'          THEN 'primary'
                       WHEN s.accessibility_class = 'common_secondary' THEN 'fair_secondary'
                       WHEN s.accessibility_class = 'specialist'       THEN 'specialist_trick'
                       WHEN s.accessibility_class = 'obscure'          THEN 'obscure_trick'
                       ELSE 'unresolved'
                   END AS risk_class,
                   s.recognition_score AS recognition_score,
                   s.activation_score AS activation_score,
                   CASE
                       WHEN qw.sense_id IS NULL OR w.dominant_sense_id IS NULL THEN 0
                       WHEN qw.sense_id <> w.dominant_sense_id THEN 1
                       ELSE 0
                   END AS uses_non_dominant,
                   COALESCE((SELECT mm.semantic_status FROM memberships mm
                              WHERE mm.category_id = q.category_id
                                AND mm.word_id = qw.word_id
                                AND COALESCE(mm.sense_id, -1) = COALESCE(qw.sense_id, -1)
                              LIMIT 1), 'unreviewed') AS semantic_status,
                   COALESCE(s.display_text, w.text) AS display,
                   COALESCE(s.sense_key, '') AS sense_key,
                   w.familiarity_score AS word_familiarity,
                   COALESCE(sn.is_proper_noun, w.is_proper_noun, 0) AS is_proper_noun,
                   -- Слово стоит в этой категории первым значением или вторым.
                   -- `alternative` — законный статус (bark у собаки и у дерева),
                   -- но четвёрка целиком из вторых значений читается как подвох.
                   (SELECT COUNT(*) FROM memberships mm
                     WHERE mm.category_id = q.category_id
                       AND mm.word_id = qw.word_id
                       AND mm.review_status IN ('approved', 'auto_approved')
                       AND mm.semantic_status <> 'incorrect') AS primary_membership,
                   ws.char_count AS char_count, ws.token_count AS token_count
              FROM quartets q
              JOIN categories c     ON c.id = q.category_id
              JOIN quartet_words qw ON qw.quartet_id = q.id
              JOIN words w          ON w.id = qw.word_id
              LEFT JOIN word_senses s ON s.id = qw.sense_id
              LEFT JOIN word_senses sn ON sn.id = qw.sense_id
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

    swow = quartet_semantics.load_swow(conn)
    stats = {"четвёрок доступно": 0, "отсеяно профилем": 0}
    rejected: dict[str, int] = {}
    by_category: dict[int, list[dict]] = {}
    for entry in quartets.values():
        if len(entry["tokens"]) != level_solver.QUARTET_SIZE:
            continue
        entry["semantics"] = _quartet_semantics(entry, profile, swow)
        entry["facts"] = _quartet_facts(entry, rare_familiarity)
        reasons = (
            profiles_mod.check_quartet(profile, entry["facts"]) if profile is not None else []
        )
        if reasons:
            entry["profile_reasons"] = reasons
            stats["отсеяно профилем"] += 1
            for reason in reasons:
                code = quartet_semantics.code_of(reason)
                if code:
                    rejected[code] = rejected.get(code, 0) + 1
            continue
        stats["четвёрок доступно"] += 1
        by_category.setdefault(entry["category_id"], []).append(entry)
    # Связные четвёрки идут первыми: генератор берёт их, пока они есть, и
    # доходит до несвязных только когда выбора не осталось. Это предпочтение,
    # а не запрет — иначе `north / south / east / west` и части целого,
    # которые попарными ассоциациями не держатся вовсе, вылетели бы классом.
    for entries in by_category.values():
        entries.sort(
            key=lambda item: (
                item["semantics"].swow.no_positive_edges,
                item["quartet_key"],
            )
        )
    for code, count in sorted(rejected.items(), key=lambda item: -item[1]):
        stats[f"отсеяно: {code}"] = count
    return by_category, stats


def _quartet_semantics(
    entry: dict,
    profile: profiles_mod.Profile | None,
    swow: dict[str, quartet_semantics.SwowMetrics],
) -> quartet_semantics.QuartetSemantics:
    """Семантический профиль четвёрки: значения, якоря, режим связности."""
    rows = entry["facts_rows"]
    slots = quartet_semantics.slots_from_rows(
        [_SlotRow(row) for row in rows]  # type: ignore[arg-type]
    )
    all_surface = bool(slots) and all(
        slot.sense_mode in ("surface_form",) for slot in slots
    )
    return quartet_semantics.QuartetSemantics(
        slots=slots,
        mode=quartet_semantics.coherence_mode(
            rows[0]["rule_type"] if rows else None, all_surface_form=all_surface
        ),
        swow=swow.get(entry["quartet_key"], quartet_semantics.SwowMetrics()),
        anchor_recognition_min=profile["anchor_recognition_min"] if profile else 0.0,
        anchor_activation_min=profile["anchor_activation_min"] if profile else 0.0,
    )


class _SlotRow:
    """Адаптер строки выборки под форму, которую читает `quartet_semantics`.

    Нужен, потому что колонка слова здесь называется `normalized`, а слой
    значений ждёт `word`: подменять имя в SQL значило бы ломать остальные
    двадцать мест, которые читают ту же выборку.
    """

    __slots__ = ("_row",)

    def __init__(self, row: sqlite3.Row) -> None:
        self._row = row

    def __getitem__(self, key: str) -> object:
        return self._row["normalized"] if key == "word" else self._row[key]

    def keys(self) -> list[str]:
        return ["word", *self._row.keys()]


def _quartet_facts(entry: dict, rare_familiarity: float) -> profiles_mod.QuartetFacts:
    rows = entry["facts_rows"]
    scores = entry["scores"]
    chars = [int(row["char_count"] or len(row["display"])) for row in rows]
    tokens = [int(row["token_count"] or len(str(row["display"]).split())) for row in rows]
    familiarity = [row["word_familiarity"] for row in rows if row["word_familiarity"] is not None]
    return profiles_mod.QuartetFacts(
        quartet_key=entry["quartet_key"],
        label_text=entry["label"],
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
        proper_nouns=sum(1 for row in rows if row["is_proper_noun"]),
        secondary_senses=sum(1 for row in rows if not row["primary_membership"]),
        semantics=entry.get("semantics"),
    )


@dataclass(frozen=True)
class _QuartetPool:
    """Годные четвёрки под один профиль качества, разложенные по входам."""

    by_category: dict[int, list[dict]]
    by_quartet_id: dict[int, dict]
    category_ids: list[int]
    concept_by_category: dict[int, int]
    decoys: decoy_pairs_mod.DecoyIndex
    stats: dict[str, int]


class _PoolCache:
    """Пулы четвёрок по профилям: у каждого профиля свой отбор.

    Профиль задаётся не на прогон, а на уровень: первые уровни кампании берут
    только знакомые слова, поздние — знание предметной области. Отбор четвёрок
    под каждый профиль считается один раз и переиспользуется.

    Индекс ловушек живёт здесь же, а не рядом: ловушка ставится парой групп, и
    обе группы обязаны быть годными по одному и тому же профилю. Считать его
    один раз на всю базу значило бы предлагать генератору соперников, которых
    он взять не может.
    """

    def __init__(
        self,
        conn: sqlite3.Connection,
        *,
        tier: str,
        rare_familiarity: float,
        index: level_solver.MembershipIndex,
        conflicts: dict[int, set[int]],
    ) -> None:
        self._conn = conn
        self._tier = tier
        self._rare = rare_familiarity
        self._index = index
        self._conflicts = conflicts
        self._pools: dict[str, _QuartetPool] = {}

    def semantics_of(self, quartet_id: int) -> quartet_semantics.QuartetSemantics | None:
        """Семантика четвёрки из любого уже посчитанного пула.

        Уровень мог собраться под своим профилем, а проверка пакета идёт по
        главному: искать по всем посчитанным пулам дешевле, чем тащить ссылку
        на семантику через десять слоёв структур уровня.
        """
        for pool in self._pools.values():
            entry = pool.by_quartet_id.get(quartet_id)
            if entry is not None and entry.get("semantics") is not None:
                return entry["semantics"]
        return None

    def get(self, profile: profiles_mod.Profile | None) -> _QuartetPool:
        key = profile.name if profile else ""
        if key not in self._pools:
            by_category, stats = _usable_quartets(
                self._conn, self._tier, profile=profile, rare_familiarity=self._rare
            )
            decoys = decoy_pairs_mod.build(
                (entry for entries in by_category.values() for entry in entries),
                self._index,
                available=set(by_category),
                conflicts=self._conflicts,
            )
            stats = dict(stats)
            stats["ловушек доступно"] = decoys.stats.get("ловушек доступно", 0)
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
                decoys=decoys,
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
    use_decoys: bool = True,
    decoy_target: int | None = None,
    obvious_until: int = 0,
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
    ``use_decoys``      ставить ли ловушки — пары групп вокруг общего слова;
    ``decoy_target``    сколько ловушек просить вместо профиля композиции;
    ``obvious_until``   до какого номера уровня брать самые очевидные правила
                        пула, а не случайные: вход в игру объясняет правила,
                        и случайный набор годных тем делает это плохо;
    ``key_prefix``      префикс ключей уровней. Отдельный пакет живёт под своим
                        префиксом и не затирается дымовым прогоном сборки,
                        который каждый раз пересобирает `L001..L005`;
    ``auto_profile``    брать профиль качества по номеру уровня: первые уровни
                        только из знакомых слов, поздние — со знанием. Явный
                        ``profile`` сильнее и отменяет это.
    """
    config = config or cooldown_mod.load_config()
    conflicts = _conflict_map(conn)
    index = level_solver.load_memberships(conn)
    pools = _PoolCache(
        conn, tier=tier, rare_familiarity=rare_familiarity,
        index=index, conflicts=conflicts,
    )
    base_pool = pools.get(profile)
    meta_index = meta_pairs_mod.load(conn, tier=tier) if use_meta else meta_pairs_mod.MetaIndex()
    structures = structured.load(conn)
    recorded_decoys = (
        decoy_pairs_mod.recorded_targets(conn, index)
        if use_decoys and decoy_target is None
        else {}
    )
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
        "четвёрок пропущено по имени чужой группы": 0,
        "четвёрок пропущено по перезарядке": 0,
        "мета-связей поставлено": 0,
        "уровней с мета": 0,
        "мета: недобор до профиля": 0,
        "отклонено мета-проверкой": 0,
        "ловушек поставлено": 0,
        "уровней с ловушками": 0,
        "ловушки: недобор до профиля": 0,
        "отклонено пересечением на чистом уровне": 0,
        "отклонено взаимной парой групп": 0,
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
        # Ловушек столько, сколько их на уровне записи того же номера, — и это
        # число снимается с самих уровней записи, а не берётся из строки
        # «ловушки» ручного разбора видео. Разница принципиальная: в разборе
        # смешаны три разных вида (память между уровнями, соседство тем,
        # пересечение на поле), а планировщик умеет только третий. Пока цель
        # бралась оттуда, генератор ставил 5.2 пересечения на уровень против
        # 0.2 в записи — см. `decoy_pairs.recorded_targets`.
        wanted_decoys = (
            decoy_target if decoy_target is not None
            else (recorded_decoys.get(position, 0) if use_decoys else 0)
        )
        if not use_decoys:
            wanted_decoys = 0
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
                decoy_index=pool.decoys,
                decoy_target=wanted_decoys,
                obvious_first=position <= obvious_until,
                index=index,
                stats=stats,
            )
            if built_plan is None:
                continue
            groups, links, planned_decoys = built_plan
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
                    exceeded = budget.fits(facts)
                    if exceeded:
                        over_budget = True
                        code = quartet_semantics.code_of(exceeded) or "прочее"
                        key = f"бюджет уровня: {code}"
                        stats[key] = stats.get(key, 0) + 1
                        break
                    budget.spend(facts)
            if over_budget:
                stats["отклонено бюджетом уровня"] += 1
                continue
            level_key = f"{key_prefix}{number:03d}"
            built = _evaluate(
                groups,
                links,
                planned_decoys,
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
            # Уровень, которому по записи ловушки не положены, обязан обойтись
            # без пересечений вообще. Иначе туториал, где игрок ещё учит
            # правила, приходит со случайным двусмысленным пузырём: сложность
            # первого уровня записи 1.0, а у первой нашей сборки выходило 4.0.
            if (
                wanted_decoys == 0
                and built.assessment is not None
                and built.assessment.decoys
                and attempt < MAX_ATTEMPTS_PER_LEVEL - 1
            ):
                stats["отклонено пересечением на чистом уровне"] += 1
                candidate = built
                continue
            if _mutual_pairs(built) and attempt < MAX_ATTEMPTS_PER_LEVEL - 1:
                stats["отклонено взаимной парой групп"] += 1
                candidate = built
                continue
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
        stats["ловушек поставлено"] += len(candidate.planned_decoys)
        if candidate.planned_decoys:
            stats["уровней с ловушками"] += 1
        if len(candidate.planned_decoys) < wanted_decoys:
            stats["ловушки: недобор до профиля"] += 1
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

    if profile is not None:
        stats.update(_pack_gate(levels, profile, pools))
    return levels, stats


class PackGateError(RuntimeError):
    """Пакет собрался, но не проходит проверку целиком.

    Отдельный тип, потому что реакция на него другая: уровни собраны и валидны,
    проблема в их составе. Молча отдать такой пакет нельзя, тихо ослабить
    пороги — тем более: ровно так неиграбельная двадцатка и уезжает в сборку.
    """


def _pack_gate(
    levels: list[LevelCandidate],
    profile: profiles_mod.Profile,
    pools: _PoolCache,
) -> dict[str, object]:
    """Проверки, которые имеют смысл только для пакета целиком.

    Доля несвязных групп — свойство подборки, а не отдельной четвёрки: одна
    структурная группа без попарных ассоциаций это норма, двадцать подряд —
    пакет, в котором нечего чувствовать. Считается той же формулой, которой
    получены 52% у первой сборки и 22% у записи оригинала.
    """
    groups = [
        pools.semantics_of(group.quartet_id)
        for level in levels
        if level.is_valid
        for group in level.groups
    ]
    groups = [item for item in groups if item is not None]
    if not groups:
        return {}

    dead = [item for item in groups if item.swow.no_positive_edges]
    measurable = [item for item in groups if item.swow.has_data]
    exempt = [item for item in groups if item.swow_exempt]
    anchorless = [item for item in groups if item.anchorless]
    ratio = len(dead) / len(groups)

    stats: dict[str, object] = {
        "групп в пакете": len(groups),
        "SWOW было чем измерить": len(measurable),
        "SWOW не применим по типу правила": len(exempt),
        "SWOW без единой связи": f"{len(dead)} ({ratio:.1%})",
        "групп без ясного якоря": len(anchorless),
    }

    problems: list[str] = []
    limit = profile["max_swow_disconnected_group_ratio"]
    if limit < 1.0 and ratio > limit:
        problems.append(
            f"{quartet_semantics.PACK_SWOW_DISCONNECTED_RATIO}: несвязных групп "
            f"{len(dead)} из {len(groups)} ({ratio:.1%}) при потолке {limit:.0%}"
        )
    allowed = profile["max_anchorless_groups_per_pack"]
    if len(anchorless) > allowed:
        problems.append(
            f"{quartet_semantics.INSUFFICIENT_CLEAR_ANCHORS}: групп без якоря "
            f"{len(anchorless)} при потолке {int(allowed)}"
        )
    if problems:
        stats["пакет не прошёл проверку"] = "; ".join(problems)
    return stats


def _has_connected(entries: list[dict]) -> bool:
    """Есть ли у правила четвёрка хоть с одной живой ассоциацией по SWOW."""
    return any(
        entry.get("semantics") is not None
        and not entry["semantics"].swow.no_positive_edges
        for entry in entries
    )


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
    decoy_index: decoy_pairs_mod.DecoyIndex | None = None,
    decoy_target: int = 0,
    obvious_first: bool = False,
    index: level_solver.MembershipIndex | None = None,
    stats: dict[str, int] | None = None,
) -> tuple[list[GroupPlan], list[MetaLink], list[PlannedDecoy]] | None:
    """Набирает состав уровня: сначала мета-ядро, потом обычные группы.

    Порядок обязателен. Мета-пара — редкое совпадение: 162 пары, 330 четвёрок
    из 14 184. Искать её внутри уже выбранного набора значит не находить.

    Глубина цепочки держится на одном правиле: **источник не может быть
    потребителем**. Тогда любая цепочка ровно двухшаговая — как в оригинале,
    где третьего порядка нет ни на одном из двадцати уровней. Обратное
    (несколько источников на одного потребителя) разрешено: именно так устроен
    уровень 7 записи, где `measurements` собирается из четырёх чужих
    результатов.

    Третьим слоем идут ловушки — по той же причине, что и мета: пара «дом плюс
    соперник вокруг общего слова» внутри случайного набора категорий не
    находится. До появления этого слоя генератор ставил 0-1 ловушку на уровень
    против 3-6 в записи, и весь балл фана уходил туда.
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
        allow_label_clash: bool = False,
    ) -> GroupPlan | None:
        """Ставит четвёрку в уровень, если она не повторяет уже занятое слово.

        Повтор отсекается здесь, а не проверкой готового уровня: одно общее
        слово у двух групп — это два пузыря с одной надписью, игрок их не
        различит, а база не сохранит. На пяти категориях совпадение почти не
        встречалось, на восьми ломало сборку.

        Вторая проверка — столкновение пузыря с именем чужой группы. Такое
        совпадение бывает только объявленной мета-связью; незаявленное читается
        игроком как ошибка сборки. Поэтому мета-путь зовёт `take` с
        `allow_label_clash`, а все остальные — нет.
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
        label = display_label or entry["label"]
        if not allow_label_clash and _clashes_with_labels(
            displays, label, chosen, used_displays
        ):
            if stats is not None:
                stats["четвёрок пропущено по имени чужой группы"] = (
                    stats.get("четвёрок пропущено по имени чужой группы", 0) + 1
                )
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

    # Ловушки ставятся после мета и до добора. Порядок такой же и по той же
    # причине: пара «дом плюс соперник» — совпадение куда более редкое, чем
    # свободная категория, и внутри уже набранного состава она не находится.
    decoys: list[PlannedDecoy] = []
    if decoy_target > 0 and decoy_index is not None and len(decoy_index) > 0:
        _attach_decoys(
            rng, decoy_index,
            by_category=by_category,
            by_quartet_id=by_quartet_id,
            conflicts=conflicts,
            cooling=cooling,
            chosen=chosen,
            decoys=decoys,
            take=take,
            blocked=blocked,
            index=index,
            category_count=category_count,
            target=decoy_target,
        )

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
    if obvious_first:
        # Туториал не выбирается наугад. В записи первый уровень — это FARM
        # ANIMALS, COLORS, VEHICLES, COMPASS, DAYS OF THE WEEK: самое понятное,
        # что вообще бывает. Случайная выборка из двухсот годных правил даёт
        # вместо этого ANIMAL GENDERS и GEM CUTS — формально годные, а на входе
        # в игру объясняющие правила хуже некуда.
        #
        # Берётся не строгий топ, а короткий список самых очевидных, и он
        # перемешивается. Строгий порядок сделал бы все попытки сборки
        # одинаковыми, и правило «на чистом уровне пересечений быть не должно»
        # не смогло бы ничего исправить: генератор сорок раз собирал бы тот же
        # набор с тем же случайным двусмысленным пузырём.
        pool.sort(key=lambda category_id: (-_obviousness(by_category[category_id]),
                                           by_category[category_id][0]["category_key"]))
        shortlist = pool[: max(category_count * 3, category_count + 6)]
        rng.shuffle(shortlist)
        pool = shortlist + pool[len(shortlist):]
    else:
        rng.shuffle(pool)
        # Правила, у которых есть хоть одна связная четвёрка, идут первыми.
        # Без этого генератор одинаково охотно берёт правило, все четвёрки
        # которого мертвы по SWOW, и упирается в бюджет уровня на середине
        # набора: 584 отклонённые попытки против семи собранных уровней.
        # Это порядок, а не фильтр — мёртвые правила остаются доступны хвостом.
        pool.sort(key=lambda category_id: not _has_connected(by_category[category_id]))
    for category_id in pool:
        if len(chosen) >= category_count:
            break
        if blocked(category_id):
            continue
        entries = by_category[category_id]
        if obvious_first:
            for entry in sorted(entries, key=_entry_obviousness, reverse=True):
                if take(entry) is not None:
                    break
            continue
        # Несколько попыток на правило: у категории обычно много четвёрок, и
        # первая попавшаяся часто занята перезарядкой или уже занятым словом.
        # Выбор внутри правила случайный, но из связного префикса, если он есть:
        # список уже отсортирован связными вперёд.
        connected = sum(
            1 for entry in entries if not entry["semantics"].swow.no_positive_edges
        ) if entries and entries[0].get("semantics") is not None else len(entries)
        span = connected or len(entries)
        for _ in range(min(FILLER_TRIES_PER_RULE, len(entries))):
            if take(entries[rng.randrange(span)]) is not None:
                break

    if len(chosen) < category_count:
        return None
    groups = [chosen[category_id] for category_id in sorted(chosen)]
    # Ловушка, чей соперник не дожил до финального состава, ловушкой не
    # является: объявить пересечение с группой, которой на поле нет, значит
    # соврать валидатору.
    on_field = {plan.category_key for plan in chosen.values()}
    decoys = [
        decoy for decoy in decoys
        if decoy.home_key in on_field and decoy.rival_key in on_field
    ]
    return groups, links, decoys


def _attach_decoys(
    rng: random.Random,
    decoy_index: decoy_pairs_mod.DecoyIndex,
    *,
    by_category: dict[int, list[dict]],
    by_quartet_id: dict[int, dict],
    conflicts: dict[int, set[int]],
    cooling: set[int],
    chosen: dict[int, GroupPlan],
    decoys: list[PlannedDecoy],
    take,
    blocked,
    index: level_solver.MembershipIndex | None,
    category_count: int,
    target: int,
) -> None:
    """Ставит на уровень пары «дом плюс соперник» вокруг общего слова.

    Дом обязан стоять именно той четвёркой, в которой лежит слово-ловушка, —
    иначе соблазна не будет. У соперника четвёрка любая, кроме содержащей то же
    слово: два одинаковых пузыря на поле это брак, а не ловушка.
    """
    quartet_ids = [
        quartet_id for quartet_id in decoy_index.by_quartet if quartet_id in by_quartet_id
    ]
    rng.shuffle(quartet_ids)
    placed_tokens: set[str] = set()
    for quartet_id in quartet_ids:
        if len(decoys) >= target or len(chosen) >= category_count:
            break
        home_entry = by_quartet_id[quartet_id]
        home_id = int(home_entry["category_id"])
        home_plan = chosen.get(home_id)
        if home_plan is not None and home_plan.quartet_id != quartet_id:
            continue  # категория уже стоит, но другой четвёркой — слова нет на поле
        if home_plan is None and (home_id in cooling or blocked(home_id)):
            continue
        candidates = list(decoy_index.for_quartet(quartet_id))
        rng.shuffle(candidates)
        for pair in candidates:
            if len(decoys) >= target:
                break
            if pair.token_norm in placed_tokens:
                continue
            rival_id = pair.rival_id
            if rival_id == home_id:
                continue
            rival_plan = chosen.get(rival_id)
            if rival_plan is None:
                if rival_id in cooling or blocked(rival_id):
                    continue
                if rival_id in conflicts.get(home_id, ()):
                    continue
            need = (1 if home_plan is None else 0) + (1 if rival_plan is None else 0)
            if category_count - len(chosen) < need:
                continue
            if home_plan is None:
                home_plan = take(home_entry)
                if home_plan is None:
                    break
            if rival_plan is None:
                rival_plan = _take_rival(
                    rng, by_category.get(rival_id) or [], pair.token_norm, take,
                    index=index, home_key=pair.home_key,
                )
                if rival_plan is None:
                    continue
            elif _entry_has_word(rival_plan.tokens, pair.token_norm):
                continue
            decoys.append(
                PlannedDecoy(
                    token_display=pair.token_display,
                    home_key=pair.home_key,
                    rival_key=pair.rival_key,
                    home_strength=pair.home_strength,
                    rival_strength=pair.rival_strength,
                )
            )
            placed_tokens.add(pair.token_norm)


def _take_rival(
    rng: random.Random,
    entries: list[dict],
    token_norm: str,
    take,
    *,
    index: level_solver.MembershipIndex | None = None,
    home_key: str = "",
):
    """Четвёрка соперника без слова-ловушки и без слов, годных дому.

    Первое — чтобы на поле не было двух одинаковых пузырей. Второе — чтобы
    ловушка осталась односторонней: если соперник отдаёт слова обратно в дом,
    две группы становятся неразличимы и решаются только перебором.
    """
    clean = [entry for entry in entries if not _entry_has_word(entry["tokens"], token_norm)]
    if index is not None and home_key:
        clean = [entry for entry in clean if _entry_free_of(entry, home_key, index)]
    for _ in range(min(FILLER_TRIES_PER_RULE, len(clean))):
        plan = take(clean[rng.randrange(len(clean))])
        if plan is not None:
            return plan
    return None


def _entry_has_word(tokens: list, token_norm: str) -> bool:
    return any(display.strip().lower() == token_norm for _w, _s, display, _sk, _r in tokens)


def _clashes_with_labels(
    displays: set[str],
    label: str,
    chosen: dict[int, GroupPlan],
    used_displays: set[str],
) -> bool:
    """Столкнётся ли новая группа с именем уже стоящей — или своим именем с её пузырём.

    Проверяются обе стороны. Слово новой четвёрки, читающееся как имя стоящей
    группы, и имя новой группы, читающееся как уже выложенный пузырь, — это
    одна и та же беда с разных концов.
    """
    placed_labels = [plan.label for plan in chosen.values()]
    for display in displays:
        if any(labels_mod.reads_as(display, name) for name in placed_labels):
            return True
    return any(labels_mod.reads_as(display, label) for display in used_displays)


def _mutual_pairs(candidate: LevelCandidate) -> list[tuple[str, str]]:
    """Пары групп, которые обмениваются словами в обе стороны.

    Односторонняя ловушка решается: игрок кладёт `orange` во фрукты, потому что
    ни одно слово цветов во фрукты не просится, и цвета собираются сами. Пара,
    которая тянет в обе стороны, не решается по частям вовсе — только
    одновременным перебором обеих групп.

    Живой пример, ради которого правило появилось (уровень 2 сданной сборки):

        shape   FIRST LESSONS -> SHAPES
        Square  SHAPES        -> FIRST LESSONS
        circle  SHAPES        -> FIRST LESSONS

    Формально каждое пересечение честное — авторский дом сильнее соперника, —
    а на поле это две неразличимые группы. В записи оригинала такой пары нет
    ни одной на двадцать уровней.
    """
    if candidate.assessment is None:
        return []
    directed = {(decoy.home, decoy.rival) for decoy in candidate.assessment.decoys}
    return sorted(
        (home, rival)
        for home, rival in directed
        if home < rival and (rival, home) in directed
    )


def _entry_obviousness(entry: dict) -> float:
    """Насколько четвёрка очевидна: знакомость слов плюс качество надписи.

    Обе величины уже посчитаны скорингом; здесь они только складываются, чтобы
    у сортировки был один ключ. Половинный вес надписи не подобран, а взят из
    смысла: игрок сначала узнаёт слова и только потом проверяет догадку именем.
    """
    scores = entry.get("scores") or {}
    familiarity = scores.get("avg_familiarity") or 0.0
    label = scores.get("label_quality") or 0.0
    return float(familiarity) + 0.5 * float(label)


def _obviousness(entries: list[dict]) -> float:
    return max((_entry_obviousness(entry) for entry in entries), default=0.0)


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
                    allow_label_clash=True,
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
    planned_decoys: list[PlannedDecoy],
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
        planned_decoys={
            (decoy.token_display.strip().lower(), decoy.rival_key)
            for decoy in planned_decoys
        },
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
        planned_decoys=list(planned_decoys),
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
    # Режим слота — свойство четвёрки, а не следствие того, нашлось ли значение.
    # Читается один раз на сохранение: иначе подзапрос на каждый из восьмисот
    # токенов пакета.
    sense_modes = {
        (int(row["quartet_id"]), int(row["word_id"])): row["sense_mode"]
        for row in conn.execute(
            "SELECT quartet_id, word_id, sense_mode FROM quartet_words"
        )
    }
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
                        # Режим берётся у слота четвёрки, а не выводится из
                        # наличия значения. Прежняя формула
                        # («значения нет -> surface_form») превращала пробел в
                        # объявленное исключение: у пакета TOP001..020 так
                        # получилось 694 обычных слова, записанных в базу как
                        # игра слов, и ни одна проверка значений их не видела.
                        sense_modes.get((group.quartet_id, word_id), "lexical"),
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

        # Объявленные ловушки пишутся вместе с уровнем, а не выводятся заново.
        # Различие «спроектировано / вылезло само» существует только как запись
        # решения автора: `assess-levels` перечитывает эту таблицу и без неё
        # отклонит ровно то, ради чего уровень собирался.
        for decoy in level.planned_decoys:
            token_id = token_ids.get((decoy.home_key, decoy.token_display))
            rival_group_id = group_ids.get(decoy.rival_key)
            if token_id is None or rival_group_id is None:
                continue
            conn.execute(
                """
                INSERT INTO level_decoys
                    (level_id, token_id, decoy_group_id, decoy_category_id, planned,
                     plausibility, note, created_at)
                VALUES (?, ?, ?, NULL, 1, ?, ?, ?)
                ON CONFLICT (level_id, token_id,
                             COALESCE(decoy_group_id, 0), COALESCE(decoy_category_id, 0))
                DO UPDATE SET planned = 1, plausibility = excluded.plausibility,
                              note = excluded.note
                """,
                (
                    level_id, token_id, rival_group_id, decoy.rival_strength,
                    f"дом «{decoy.home_key}» {decoy.home_strength:.2f}", now,
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
