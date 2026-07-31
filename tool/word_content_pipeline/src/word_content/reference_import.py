"""Импорт уровней референса без потерь и backfill недостающих элементов.

Две команды, разделённые намеренно.

``plan-reference-backfill``
    Считает, каких элементов базе не хватает, чтобы уровни записи вообще
    существовали: слов, правил группировки, надписей, связей, четвёрок.
    Пишет их в ``data/reference/backfill/*.jsonl`` — это и есть источник
    правды. Правки только в SQLite запрещены: база обязана пересобираться
    из текстовых файлов, иначе через месяц никто не скажет, откуда взялась
    связь ``cow -> farm animals``.

``import-reference-levels``
    Кладёт сами уровни: группы, токены, формы, мета-зависимости, авторские
    назначения и провенанс. Импорт **не имеет права** отбросить группу из-за
    того, что онтология её не классифицирует: сначала запись сохраняется без
    потерь, нормализуется потом.

Обе идемпотентны и детерминированы: повторный прогон даёт тот же результат.

Почему backfill не строится как diff. Планировщик смотрит на базу **без**
элементов с ``origin = 'reference_backfill'``. Поэтому патч одинаков и на
пустой базе, и на уже заполненной: он описывает не «чего не хватает сейчас»,
а «что запись требует от базы». Иначе повторный прогон выдавал бы пустые
файлы, и чистая сборка молча теряла бы половину контента.
"""

from __future__ import annotations

import csv
import json
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from . import familiarity as familiarity_mod
from .db import utc_now
from .normalization import normalize_word
from .reference_fixtures import (
    FixtureGroup,
    FixtureLevel,
    ReferenceFixtures,
    normalize_name,
    normalize_token,
)
from .reference_resolve import (
    REFERENCE_ORIGIN,
    BaseIndex,
    GroupResolution,
    load_index,
    resolve_group,
)

IMPORTER_VERSION = "reference-import/1.0"
REFERENCE_LEVEL_ORIGIN = "reference_video"
SOURCE_KIND = "reference_video"

# Имена, для которых тип правила виден из самого имени. Всё, что сюда не
# попало, разбирается запасной эвристикой, а спорное — таблицей решений
# в data/reference/group_overrides.csv.
_SEQUENCES = {"days of the week", "months", "calendar", "time periods", "stages of life"}
_CLOSED_SETS = {
    "compass", "numbers", "odd numbers", "card suits", "zodiac signs",
    "senses", "polygons", "shapes",
}
_COMPONENT_NAMES = {"body parts", "face", "organs", "shoe", "shoes", "tree", "band"}
_CONTEXT_HUBS = {
    "school", "sleep", "driving", "baking", "house", "bathroom", "bedroom",
    "laundry", "gardening", "construction", "halloween", "easter", "forest",
    "health", "fire", "illness", "menu", "movie theater", "gym", "spring",
    "beauty care", "healthy lifestyle", "facial care", "astronomy",
}

# Порядок файлов патча = порядок применения: слова, потом правила, потом всё,
# что на них ссылается. Менять порядок нельзя.
PATCH_FILES = (
    "words.jsonl",
    "senses.jsonl",
    "group_rules.jsonl",
    "labels.jsonl",
    "memberships.jsonl",
    "quartets.jsonl",
    "token_forms.jsonl",
    "meta_dependencies.jsonl",
)


class ReferenceImportError(RuntimeError):
    pass


# --------------------------------------------------------------- тип правила


@dataclass(frozen=True)
class GroupOverride:
    """Ручное решение по одной группе записи.

    Автоматический резолвер ошибается предсказуемым образом: он цепляется за
    правило, которое случайно держит три слова из четырёх. `bed, chair, table,
    door` действительно все деревянные, но авторская группа здесь — HOUSE, а не
    «предметы из дерева». Такие случаи разбираются глазами один раз и живут в
    CSV, а не в коде.
    """

    decision: str          # reuse | new_rule | "" (только уточнить rule_type)
    rule_key: str | None
    rule_type: str | None
    note: str = ""


def default_overrides_path() -> Path:
    """Курируемые решения по группам записи. Один путь на весь проект.

    Отдельная функция, потому что расхождение уже стреляло: gate из CLI читал
    таблицу решений, а gate внутри генератора — нет, и одни и те же уровни
    давали 95/95 и 93/95 в соседних шагах одной сборки.
    """
    return Path(__file__).resolve().parents[2] / "data/reference/group_overrides.csv"


def default_sense_choices_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data/reference/sense_choices.csv"


def load_overrides(path: Path | None) -> dict[tuple[int, int], GroupOverride]:
    """Курируемые решения: (уровень, номер группы) -> что делать."""
    if path is None or not path.exists():
        return {}
    overrides: dict[tuple[int, int], GroupOverride] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if not (row.get("level") or "").strip():
                continue
            overrides[(int(row["level"]), int(row["group_index"]))] = GroupOverride(
                decision=(row.get("decision") or "").strip(),
                rule_key=(row.get("rule_key") or "").strip() or None,
                rule_type=(row.get("rule_type") or "").strip() or None,
                note=(row.get("note") or "").strip(),
            )
    return overrides


def load_sense_choices(path: Path | None) -> dict[tuple[str, str], str]:
    """Курируемые значения многозначных слов: (правило, слово) -> sense_key.

    Многозначное слово без выбранного значения — не мелочь: solver отказывается
    разбирать такой уровень, потому что пустое значение скрывает пропуск.
    Выбор делается один раз и живёт в CSV.
    """
    if path is None or not path.exists():
        return {}
    choices: dict[tuple[str, str], str] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if not (row.get("word") or "").strip():
                continue
            choices[(row["category_key"].strip(), normalize_token(row["word"]))] = (
                row["sense_key"].strip()
            )
    return choices


def _looks_plural(name: str) -> bool:
    if not name.endswith("s") or name.endswith("ss"):
        return False
    return not name.endswith("us")


def classify_rule_type(
    group: FixtureGroup, level_number: int,
    overrides: dict[tuple[int, int], GroupOverride],
) -> str:
    """Тип правила по записи. Детерминировано; спорное решается overrides."""
    override = overrides.get((level_number, group.index))
    if override is not None and override.rule_type:
        return override.rule_type
    if all(slot.is_meta for slot in group.slots):
        return "meta_collector"
    name = normalize_name(group.name)
    if name in _SEQUENCES:
        return "sequence"
    if name in _CLOSED_SETS:
        return "structured_set"
    if name.endswith(" parts") or name in _COMPONENT_NAMES:
        return "components"
    if name in _CONTEXT_HUBS:
        return "context_hub"
    if _looks_plural(name):
        return "taxonomy_instances"
    return "association_hub"


# ------------------------------------------------------------------- планирование


@dataclass
class BackfillPlan:
    """Машиночитаемый патч: что запись требует от базы."""

    words: list[dict] = field(default_factory=list)
    senses: list[dict] = field(default_factory=list)
    group_rules: list[dict] = field(default_factory=list)
    labels: list[dict] = field(default_factory=list)
    memberships: list[dict] = field(default_factory=list)
    quartets: list[dict] = field(default_factory=list)
    token_forms: list[dict] = field(default_factory=list)
    meta_dependencies: list[dict] = field(default_factory=list)
    decisions: list[dict] = field(default_factory=list)

    def counts(self) -> dict[str, int]:
        return {
            "missing_word": len(self.words),
            "missing_sense": len(self.senses),
            "missing_group_rule": len(self.group_rules),
            "missing_label": len(self.labels),
            "missing_membership": len(self.memberships),
            "missing_quartet": len(self.quartets),
            "missing_token_form": len(self.token_forms),
            "missing_meta_dependency": len(self.meta_dependencies),
        }

    def as_files(self) -> dict[str, list[dict]]:
        return {
            "words.jsonl": self.words,
            "senses.jsonl": self.senses,
            "group_rules.jsonl": self.group_rules,
            "labels.jsonl": self.labels,
            "memberships.jsonl": self.memberships,
            "quartets.jsonl": self.quartets,
            "token_forms.jsonl": self.token_forms,
            "meta_dependencies.jsonl": self.meta_dependencies,
        }


def quartet_key_for(level_number: int, group: FixtureGroup) -> str:
    return f"ref_l{level_number:02d}_g{group.index:02d}"


def resolve_all(
    conn: sqlite3.Connection,
    fixtures: ReferenceFixtures,
    *,
    max_level: int | None = None,
    overrides: dict[tuple[int, int], GroupOverride] | None = None,
    index: BaseIndex | None = None,
) -> tuple[BaseIndex, dict[tuple[int, int], GroupResolution]]:
    """Решение по каждой группе записи. Ключ — (уровень, номер группы)."""
    overrides = overrides or {}
    index = index or load_index(conn)
    taken: set[str] = set()
    resolutions: dict[tuple[int, int], GroupResolution] = {}
    for level in fixtures.upto(max_level):
        used_rules: set[str] = set()
        for group in level.groups:
            rule_type = classify_rule_type(group, level.number, overrides)
            override = overrides.get((level.number, group.index))
            if override is not None and override.decision:
                resolution = _forced(group, level.number, index, override, rule_type, taken)
            else:
                resolution = resolve_group(
                    group, level.number, index, rule_type=rule_type, taken_keys=taken
                )
            # Две группы одного уровня не могут быть одним правилом: в уровне
            # категория встречается ровно один раз, иначе это не разбиение.
            if resolution.rule_key is not None and resolution.rule_key in used_rules:
                resolution = GroupResolution(
                    group=group,
                    level_number=level.number,
                    rule_key=None,
                    decision="new_rule",
                    name_rank=resolution.name_rank,
                    members_missing=tuple(slot.normalized for slot in group.slots),
                    new_rule_key=_free_key(group, index, taken),
                    rule_type=rule_type,
                    candidates=resolution.candidates,
                )
            if resolution.is_new:
                taken.add(resolution.new_rule_key or "")
            used_rules.add(resolution.target_rule_key)
            resolutions[(level.number, group.index)] = resolution
    return index, resolutions


def _free_key(group: FixtureGroup, index: BaseIndex, taken: set[str]) -> str:
    from .reference_resolve import _new_rule_key

    return _new_rule_key(group, 0, index, taken)


def _forced(
    group: FixtureGroup, level_number: int, index: BaseIndex,
    override: GroupOverride, rule_type: str, taken: set[str],
) -> GroupResolution:
    """Решение, принятое человеком: резолвер здесь не участвует."""
    if override.decision == "reuse":
        if not override.rule_key:
            raise ReferenceImportError(
                f"L{level_number}, группа {group.index}: decision=reuse без rule_key"
            )
        if override.rule_key not in index.rules:
            raise ReferenceImportError(
                f"L{level_number}, группа {group.index}: правила "
                f"{override.rule_key} в базе нет"
            )
        pool = index.pools.get(override.rule_key, set())
        tokens = [slot.normalized for slot in group.slots]
        return GroupResolution(
            group=group, level_number=level_number, rule_key=override.rule_key,
            decision="reuse", name_rank=0,
            members_present=tuple(t for t in tokens if t in pool),
            members_missing=tuple(t for t in tokens if t not in pool),
            rule_type=index.rules[override.rule_key]["rule_type"] or rule_type,
        )
    key = override.rule_key or _free_key(group, index, taken)
    return GroupResolution(
        group=group, level_number=level_number, rule_key=None, decision="new_rule",
        name_rank=0, members_missing=tuple(slot.normalized for slot in group.slots),
        new_rule_key=key, rule_type=rule_type,
    )


def plan_backfill(
    conn: sqlite3.Connection,
    fixtures: ReferenceFixtures,
    *,
    max_level: int | None = None,
    overrides: dict[tuple[int, int], GroupOverride] | None = None,
    sense_choices: dict[tuple[str, str], str] | None = None,
) -> BackfillPlan:
    """Считает патч. База читается без элементов, созданных прошлым backfill'ом."""
    sense_choices = sense_choices or {}
    index, resolutions = resolve_all(
        conn, fixtures, max_level=max_level, overrides=overrides
    )
    plan = BackfillPlan()

    seen_words: set[str] = set()
    seen_rules: set[str] = set()
    seen_labels: set[str] = set()
    seen_memberships: set[tuple[str, str]] = set()

    for level in fixtures.upto(max_level):
        for group in level.groups:
            resolution = resolutions[(level.number, group.index)]
            rule_key = resolution.target_rule_key
            label_key = normalize_name(group.name)

            if resolution.is_new and rule_key not in seen_rules:
                seen_rules.add(rule_key)
                plan.group_rules.append(
                    {
                        "rule_key": rule_key,
                        "label": group.name,
                        "rule": _rule_text(group, resolution.rule_type),
                        "rule_type": resolution.rule_type,
                        "relation_type": _relation_for(resolution.rule_type),
                        "theme": "reference",
                        "origin": REFERENCE_ORIGIN,
                        "evidence": f"reference_level:{level.number}",
                        "first_seen_level": level.number,
                        "words": [slot.text for slot in group.slots],
                    }
                )

            if label_key and label_key not in seen_labels:
                seen_labels.add(label_key)
                plan.labels.append(
                    {
                        "label_key": label_key,
                        "display_text": group.name,
                        "scope": _label_scope(group.name),
                        "origin": REFERENCE_ORIGIN,
                        "label_source": group.label_source,
                        "first_seen_level": level.number,
                    }
                )

            for slot in group.slots:
                normalized = slot.normalized
                if normalized not in index.words and normalized not in seen_words:
                    seen_words.add(normalized)
                    plan.words.append(
                        {
                            "text": slot.text,
                            "normalized": normalized,
                            "token_kind": slot.token_kind,
                            "origin": REFERENCE_ORIGIN,
                            "evidence": f"reference_level:{level.number}",
                        }
                    )
                pool = index.pools.get(rule_key, set())
                pair = (rule_key, normalized)
                if normalized not in pool and pair not in seen_memberships:
                    seen_memberships.add(pair)
                    plan.memberships.append(
                        {
                            "word": slot.text,
                            "category_key": rule_key,
                            "relation_type": _relation_for(resolution.rule_type),
                            "reason": (
                                f"подтверждено записью референса, уровень {level.number}, "
                                f"группа «{group.name}»"
                            ),
                            "fit_score": 0.9,
                            "obviousness_score": 0.8,
                            "source": REFERENCE_ORIGIN,
                            "review_status": "approved",
                            "semantic_status": "unreviewed",
                            "evidence": f"reference_level:{level.number}",
                        }
                    )
                # Значение слова: если слово многозначно, а связь значения не
                # называет, это не ошибка импорта, а очередь на разведение.
                if index.sense_count(slot.text) > 1:
                    chosen = index.membership_senses.get((rule_key, normalized))
                    curated = sense_choices.get((rule_key, normalized))
                    plan.senses.append(
                        {
                            "word": slot.text,
                            "category_key": rule_key,
                            "sense_key": chosen or curated,
                            "status": (
                                "resolved" if chosen
                                else "curated" if curated
                                else "needs_sense_split"
                            ),
                            "evidence": f"reference_level:{level.number}",
                        }
                    )

                if slot.token_form != "word" or slot.token_kind != "lexical_word":
                    plan.token_forms.append(
                        {
                            "level": level.number,
                            "group_index": group.index,
                            "group_name": group.name,
                            "token": slot.text,
                            "token_kind": slot.token_kind,
                            "token_form": slot.token_form,
                            "pieces": list(slot.pieces),
                            "observability": slot.observability,
                            "emitted_by": slot.emitted_by,
                        }
                    )

            signature = group.quartet_signature
            plan.quartets.append(
                {
                    "quartet_key": quartet_key_for(level.number, group),
                    "category_key": rule_key,
                    "rule_type": resolution.rule_type,
                    "label_key": label_key,
                    "words": [slot.text for slot in group.slots],
                    "tier": "normal",
                    "origin": REFERENCE_ORIGIN,
                    "already_in_base": bool(index.quartets.get(signature)),
                    "evidence": f"reference_level:{level.number}",
                }
            )

            plan.decisions.append(
                {
                    "level": level.number,
                    "group_index": group.index,
                    "reference_name": group.name,
                    "label_source": group.label_source,
                    "decision": resolution.decision,
                    "rule_key": rule_key,
                    "rule_type": resolution.rule_type,
                    "name_rank": resolution.name_rank,
                    "members_present": len(resolution.members_present),
                    "members_missing": len(resolution.members_missing),
                    "candidates": "; ".join(
                        f"{key}:{rank}/{present}" for key, rank, present in resolution.candidates
                    ),
                }
            )

        for link in level.meta_links:
            plan.meta_dependencies.append(
                {
                    "level": level.number,
                    "token": link.token,
                    "form": link.form,
                    "source_group": link.source_group,
                    "target_group": link.target_group,
                }
            )

    return plan


def _rule_text(group: FixtureGroup, rule_type: str) -> str:
    words = ", ".join(slot.text for slot in group.slots)
    return (
        f"{rule_type}: авторская группа записи референса «{group.name}» ({words})"
    )


def _relation_for(rule_type: str) -> str:
    return {
        "taxonomy_instances": "is_a",
        "components": "part_of",
        "association_hub": "associated_with",
        "context_hub": "found_in",
        "property_group": "has_property",
        "functional_group": "used_in",
        "structured_set": "member_of_set",
        "sequence": "member_of_set",
        "meta_collector": "associated_with",
    }.get(rule_type, "associated_with")


def _label_scope(name: str) -> str:
    """Охват надписи — характеристика, а не оценка. Считается по форме имени."""
    words = normalize_name(name).split()
    if len(words) == 1:
        return "broad"
    if len(words) == 2:
        return "medium"
    return "narrow"


# --------------------------------------------------------------- запись/чтение патча


def write_plan(plan: BackfillPlan, directory: Path) -> dict[str, int]:
    directory.mkdir(parents=True, exist_ok=True)
    written: dict[str, int] = {}
    for name, rows in plan.as_files().items():
        path = directory / name
        with path.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        written[name] = len(rows)
    decisions = directory / "resolution_decisions.csv"
    if plan.decisions:
        with decisions.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(plan.decisions[0]))
            writer.writeheader()
            writer.writerows(plan.decisions)
        written["resolution_decisions.csv"] = len(plan.decisions)
    return written


def read_plan(directory: Path) -> BackfillPlan:
    if not directory.exists():
        raise ReferenceImportError(
            f"патча референса нет: {directory}. "
            "Сначала выполните plan-reference-backfill."
        )
    plan = BackfillPlan()
    mapping = {
        "words.jsonl": plan.words,
        "senses.jsonl": plan.senses,
        "group_rules.jsonl": plan.group_rules,
        "labels.jsonl": plan.labels,
        "memberships.jsonl": plan.memberships,
        "quartets.jsonl": plan.quartets,
        "token_forms.jsonl": plan.token_forms,
        "meta_dependencies.jsonl": plan.meta_dependencies,
    }
    for name, target in mapping.items():
        path = directory / name
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                target.append(json.loads(line))
    return plan


# ------------------------------------------------------------------- применение патча


def apply_backfill(conn: sqlite3.Connection, plan: BackfillPlan) -> dict[str, int]:
    """Вставляет недостающее. Ничего не перетирает: решения seed остаются."""
    now = utc_now()
    stats = dict.fromkeys(
        ("words", "senses_flagged", "senses_resolved", "group_rules", "labels",
         "label_links", "memberships", "quartets", "skipped_existing"), 0
    )

    for row in plan.words:
        normalized = row["normalized"]
        existing = conn.execute(
            "SELECT id FROM words WHERE normalized = ? AND language = 'en'", (normalized,)
        ).fetchone()
        if existing is not None:
            stats["skipped_existing"] += 1
            continue
        # Частотность считается сразу: связь со словом без familiarity_score
        # блокируется проверкой целостности — отсутствующие данные обязаны
        # закрывать связь, а не проходить как подтверждённые.
        conn.execute(
            """
            INSERT INTO words (text, normalized, language, is_proper_noun,
                               familiarity_score, status, created_at, updated_at)
            VALUES (?, ?, 'en', 0, ?, 'active', ?, ?)
            """,
            (row["text"], normalized, familiarity_mod.familiarity(normalized), now, now),
        )
        stats["words"] += 1

    stats["senses_flagged"] = sum(
        1 for row in plan.senses if row.get("status") == "needs_sense_split"
    )

    for row in plan.group_rules:
        key = row["rule_key"]
        if conn.execute(
            "SELECT 1 FROM categories WHERE category_key = ?", (key,)
        ).fetchone():
            stats["skipped_existing"] += 1
            continue
        concept = conn.execute(
            "SELECT id FROM category_concepts WHERE concept_key = ?", (key,)
        ).fetchone()
        if concept is None:
            cur = conn.execute(
                """
                INSERT INTO category_concepts
                    (concept_key, label, theme, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (key, row["label"], row["theme"], row.get("evidence"), now, now),
            )
            concept_id = int(cur.lastrowid)
        else:
            concept_id = int(concept["id"])
        conn.execute(
            """
            INSERT INTO categories
                (category_key, label, rule, relation_type, rule_type, theme, status,
                 origin, concept_id, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, 'active', ?, ?, ?, ?)
            """,
            (
                key, row["label"], row["rule"], row["relation_type"], row["rule_type"],
                row["theme"], row["origin"], concept_id, now, now,
            ),
        )
        stats["group_rules"] += 1

    for row in plan.labels:
        label_id = _ensure_label(conn, row["label_key"], row["display_text"],
                                 row.get("scope", "unknown"), row["origin"], now)
        stats["labels"] += 1 if label_id[1] else 0

    for row in plan.memberships:
        word_id = _word_id(conn, row["word"])
        category = conn.execute(
            "SELECT id FROM categories WHERE category_key = ?", (row["category_key"],)
        ).fetchone()
        if word_id is None or category is None:
            raise ReferenceImportError(
                f"связь {row['word']} -> {row['category_key']}: "
                "нет слова или правила. Патч применяется целиком и по порядку."
            )
        exists = conn.execute(
            """
            SELECT 1 FROM memberships
             WHERE word_id = ? AND category_id = ? AND review_status <> 'rejected'
            """,
            (word_id, int(category["id"])),
        ).fetchone()
        if exists is not None:
            stats["skipped_existing"] += 1
            continue
        conn.execute(
            """
            INSERT INTO memberships
                (word_id, sense_id, category_id, relation_type, reason, fit_score,
                 obviousness_score, source, review_status, semantic_status,
                 created_at, updated_at)
            VALUES (?, NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                word_id, int(category["id"]), row["relation_type"], row["reason"],
                row["fit_score"], row["obviousness_score"], row["source"],
                row["review_status"], row["semantic_status"], now, now,
            ),
        )
        stats["memberships"] += 1

    # Значения многозначных слов. Проставляются только там, где значение не
    # выбрано: решение seed не перетирается.
    for row in plan.senses:
        sense_key = row.get("sense_key")
        if not sense_key:
            continue
        word_id = _word_id(conn, row["word"])
        category = conn.execute(
            "SELECT id FROM categories WHERE category_key = ?", (row["category_key"],)
        ).fetchone()
        sense = conn.execute(
            "SELECT id FROM word_senses WHERE word_id = ? AND sense_key = ?",
            (word_id, sense_key),
        ).fetchone()
        if word_id is None or category is None or sense is None:
            raise ReferenceImportError(
                f"значение {row['word']}#{sense_key} для {row['category_key']}: "
                "нет слова, правила или такого значения"
            )
        cur = conn.execute(
            """
            UPDATE memberships SET sense_id = ?, updated_at = ?
             WHERE word_id = ? AND category_id = ? AND sense_id IS NULL
            """,
            (int(sense["id"]), now, word_id, int(category["id"])),
        )
        stats["senses_resolved"] += cur.rowcount or 0

    for row in plan.quartets:
        if conn.execute(
            "SELECT 1 FROM quartets WHERE quartet_key = ?", (row["quartet_key"],)
        ).fetchone():
            stats["skipped_existing"] += 1
            continue
        category = conn.execute(
            "SELECT id FROM categories WHERE category_key = ?", (row["category_key"],)
        ).fetchone()
        if category is None:
            raise ReferenceImportError(f"четвёрка {row['quartet_key']}: нет правила")
        label_row = conn.execute(
            "SELECT id FROM category_labels WHERE label_key = ?", (row.get("label_key"),)
        ).fetchone()
        cur = conn.execute(
            """
            INSERT INTO quartets
                (category_id, quartet_key, tier, validation_state, local_check,
                 origin, rule_type, display_label_id, validator_version,
                 note, created_at, updated_at)
            VALUES (?, ?, ?, 'auto_validated', 'unchecked', ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(category["id"]), row["quartet_key"], row.get("tier", "normal"),
                row["origin"], row.get("rule_type"),
                int(label_row["id"]) if label_row else None,
                IMPORTER_VERSION, row.get("evidence"), now, now,
            ),
        )
        quartet_id = int(cur.lastrowid)
        for slot, text in enumerate(row["words"], start=1):
            word_id = _word_id(conn, text)
            if word_id is None:
                raise ReferenceImportError(f"четвёрка {row['quartet_key']}: нет слова {text}")
            member = conn.execute(
                """
                SELECT m.sense_id AS sense_id, s.sense_key AS sense_key,
                       m.fit_score AS fit, m.obviousness_score AS obviousness
                  FROM memberships m
                  LEFT JOIN word_senses s ON s.id = m.sense_id
                 WHERE m.word_id = ? AND m.category_id = ?
                   AND m.review_status <> 'rejected'
                 ORDER BY m.id LIMIT 1
                """,
                (word_id, int(category["id"])),
            ).fetchone()
            conn.execute(
                """
                INSERT INTO quartet_words
                    (quartet_id, word_id, sense_id, slot, sense_mode, relation_type,
                     relation_strength, obviousness, intended_sense_key, created_at)
                VALUES (?, ?, ?, ?, 'lexical', ?, ?, ?, ?, ?)
                """,
                (
                    quartet_id, word_id,
                    member["sense_id"] if member else None, slot,
                    _relation_for(row.get("rule_type") or ""),
                    member["fit"] if member else None,
                    member["obviousness"] if member else None,
                    member["sense_key"] if member else None,
                    now,
                ),
            )
        # Надпись правила: реферальное имя становится допустимой надписью.
        if label_row is not None:
            conn.execute(
                """
                INSERT OR IGNORE INTO group_rule_labels
                    (category_id, label_id, is_primary, origin, note, created_at)
                VALUES (?, ?, 0, ?, ?, ?)
                """,
                (int(category["id"]), int(label_row["id"]), REFERENCE_ORIGIN,
                 row.get("evidence"), now),
            )
            stats["label_links"] += 1
        stats["quartets"] += 1

    # Локальная проверка для fixture-четвёрок: результат записывается честно,
    # но браком не считается. `pentagon, hexagon, octagon, square` целиком лежит
    # в пуле SHAPES — и это работающий уровень оригинала, а не дефект.
    stats["locally_ambiguous"] = _mark_local_check(conn)
    return stats


def _mark_local_check(conn: sqlite3.Connection) -> int:
    from .solver import category_pools, quartet_locally_unique

    pools = category_pools(conn)
    ambiguous = 0
    rows = list(
        conn.execute(
            """
            SELECT q.id AS id, c.category_key AS category_key,
                   GROUP_CONCAT(w.normalized) AS words
              FROM quartets q
              JOIN categories c     ON c.id = q.category_id
              JOIN quartet_words qw ON qw.quartet_id = q.id
              JOIN words w          ON w.id = qw.word_id
             WHERE q.origin = ?
             GROUP BY q.id ORDER BY q.quartet_key
            """,
            (REFERENCE_ORIGIN,),
        )
    )
    for row in rows:
        words = (row["words"] or "").split(",")
        result = quartet_locally_unique(conn, row["category_key"], words, pools=pools)
        state = "local_unique" if result.unique else "local_ambiguous"
        if not result.unique:
            ambiguous += 1
        conn.execute(
            "UPDATE quartets SET local_check = ?, note = COALESCE(note, '') || ? "
            " WHERE id = ?",
            (state, "" if result.unique else f" | {result.reason}", int(row["id"])),
        )
    return ambiguous


def _ensure_label(
    conn: sqlite3.Connection, label_key: str, display: str, scope: str,
    origin: str, now: str,
) -> tuple[int, bool]:
    row = conn.execute(
        "SELECT id FROM category_labels WHERE label_key = ?", (label_key,)
    ).fetchone()
    if row is not None:
        return int(row["id"]), False
    cur = conn.execute(
        """
        INSERT INTO category_labels
            (label_key, display_text, scope, origin, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (label_key, display, scope, origin, now, now),
    )
    return int(cur.lastrowid), True


def _word_id(conn: sqlite3.Connection, text: str) -> int | None:
    row = conn.execute(
        "SELECT id FROM words WHERE normalized = ? AND language = 'en'",
        (normalize_word(text),),
    ).fetchone()
    return int(row["id"]) if row else None


# ---------------------------------------------------------------- импорт уровней


@dataclass
class LevelImportReport:
    levels: int = 0
    groups: int = 0
    tokens: int = 0
    meta_edges: int = 0
    assignments: int = 0
    decoys: int = 0
    provenance_rows: int = 0
    created_entities: dict[str, int] = field(default_factory=dict)
    unresolved: list[str] = field(default_factory=list)
    # Пробелы самой записи, а не импорта: уровень 18 снят с середины.
    partial_gaps: list[str] = field(default_factory=list)


def import_levels(
    conn: sqlite3.Connection,
    fixtures: ReferenceFixtures,
    *,
    max_level: int | None = None,
    overrides: dict[tuple[int, int], GroupOverride] | None = None,
) -> LevelImportReport:
    """Кладёт уровни записи в базу. Идемпотентно: старая версия уровня удаляется."""
    now = utc_now()
    report = LevelImportReport()
    # Индекс с учётом backfill: к этому моменту патч уже применён.
    index = load_index(conn, include_reference=True)
    _, resolutions = resolve_all(
        conn, fixtures, max_level=max_level, overrides=overrides,
        index=load_index(conn),
    )

    for level in fixtures.upto(max_level):
        _delete_level(conn, level.level_key, level.number)
        level_id = _insert_level(conn, level, now)
        report.levels += 1

        group_ids: dict[str, int] = {}
        token_ids: dict[str, int] = {}

        for group in level.groups:
            resolution = resolutions[(level.number, group.index)]
            rule = conn.execute(
                "SELECT id FROM categories WHERE category_key = ?",
                (resolution.target_rule_key,),
            ).fetchone()
            if rule is None:
                report.unresolved.append(
                    f"L{level.number} «{group.name}»: нет правила "
                    f"{resolution.target_rule_key} — примените backfill"
                )
                continue
            quartet = conn.execute(
                "SELECT id FROM quartets WHERE quartet_key = ?",
                (quartet_key_for(level.number, group),),
            ).fetchone()
            label_id, _created = _ensure_label(
                conn, normalize_name(group.name), group.name,
                _label_scope(group.name), REFERENCE_ORIGIN, now,
            )
            cur = conn.execute(
                """
                INSERT INTO level_groups
                    (level_id, position, category_id, quartet_id, display_label_id,
                     label_source, reference_name, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    level_id, group.index, int(rule["id"]),
                    int(quartet["id"]) if quartet else None,
                    label_id, group.label_source, group.name, now,
                ),
            )
            group_id = int(cur.lastrowid)
            group_ids[group.normalized_name] = group_id
            report.groups += 1

            for slot in group.slots:
                word_id = _word_id(conn, slot.text)
                sense_key = index.membership_senses.get(
                    (resolution.target_rule_key, slot.normalized)
                )
                sense_id = _sense_id(conn, word_id, sense_key)
                cur = conn.execute(
                    """
                    INSERT INTO level_tokens
                        (level_id, group_id, slot, token_kind, token_form, word_id,
                         sense_id, sense_mode, display_text, pieces, picture_subject,
                         observability, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, 'lexical', ?, ?, ?, ?, ?)
                    """,
                    (
                        level_id, group_id, slot.position, slot.token_kind,
                        slot.token_form, word_id, sense_id, slot.text,
                        json.dumps(list(slot.pieces), ensure_ascii=False)
                        if slot.pieces else None,
                        slot.text if slot.token_form == "picture" else None,
                        slot.observability, now,
                    ),
                )
                token_id = int(cur.lastrowid)
                token_ids[slot.normalized] = token_id
                report.tokens += 1

                conn.execute(
                    """
                    INSERT INTO level_assignments
                        (level_id, token_id, home_group_id, authority, confidence,
                         note, created_at)
                    VALUES (?, ?, ?, 'reference', 1.0, ?, ?)
                    """,
                    (level_id, token_id, group_id,
                     f"запись референса, уровень {level.number}", now),
                )
                report.assignments += 1

                _provenance(
                    conn, level.number, group.index, "token",
                    f"L{level.number}:{group.index}:{slot.normalized}",
                    slot.observability, fixtures.source_file,
                    json.dumps(slot.as_dict(), ensure_ascii=False), now,
                )
                report.provenance_rows += 1

            _provenance(
                conn, level.number, group.index, "group",
                f"L{level.number}:{group.index}:{group.normalized_name}",
                "observed" if group.observed_label else "inferred",
                fixtures.source_file,
                json.dumps({"name": group.name, "rule": resolution.target_rule_key,
                            "decision": resolution.decision}, ensure_ascii=False),
                now,
            )
            report.provenance_rows += 1

        # Мета-зависимости: собранная категория выпускает токен другой категории.
        for link in level.meta_links:
            source_id = group_ids.get(normalize_name(link.source_group))
            target_token = token_ids.get(normalize_token(link.token))
            if source_id is None or target_token is None:
                # На частично снятом уровне источник ссылки может быть одной из
                # групп, не попавших в кадр. Это не дефект импорта, а честный
                # предел записи, и объявлять такую ссылку восстановленной нельзя.
                where = (
                    report.partial_gaps
                    if level.completeness == "partial"
                    else report.unresolved
                )
                where.append(
                    f"L{level.number}: мета-ссылка {link.token} -> {link.target_group} "
                    f"(источник «{link.source_group}» в кадр не попал)"
                    if level.completeness == "partial"
                    else f"L{level.number}: мета-ссылка {link.token} -> "
                         f"{link.target_group} не разрешилась"
                )
                continue
            conn.execute(
                """
                INSERT OR IGNORE INTO level_dependencies
                    (level_id, from_group_id, to_token_id, depth, created_at)
                VALUES (?, ?, ?, 1, ?)
                """,
                (level_id, source_id, target_token, now),
            )
            conn.execute(
                "UPDATE level_tokens SET source_group_id = ? WHERE id = ?",
                (source_id, target_token),
            )
            conn.execute(
                "UPDATE level_groups SET emits_token_id = ? WHERE id = ?",
                (target_token, source_id),
            )
            report.meta_edges += 1
            _provenance(
                conn, level.number, None, "meta_link",
                f"L{level.number}:{normalize_token(link.token)}",
                "unseen" if link.form == "unseen" else "observed",
                fixtures.source_file,
                json.dumps(link.as_dict(), ensure_ascii=False), now,
            )
            report.provenance_rows += 1

        report.decoys += _record_decoys(conn, level, level_id, now)

        _provenance(
            conn, level.number, None, "level", f"L{level.number}",
            "observed" if level.completeness == "full" else "inferred",
            fixtures.source_file,
            json.dumps({"completeness": level.completeness,
                        "groups_expected": level.groups_expected,
                        "groups_recorded": len(level.groups),
                        "modifiers": list(level.modifiers)}, ensure_ascii=False),
            now,
        )
        report.provenance_rows += 1

    return report


def _insert_level(conn: sqlite3.Connection, level: FixtureLevel, now: str) -> int:
    payload = json.dumps(level.as_dict(), ensure_ascii=False, sort_keys=True)
    import hashlib

    cur = conn.execute(
        """
        INSERT INTO level_instances
            (level_key, tier, status, content_hash, origin, fixture_status,
             reference_level, recorded_completeness, groups_expected,
             generator_version, created_at, updated_at)
        VALUES (?, ?, 'candidate', ?, ?, 'golden', ?, ?, ?, ?, ?, ?)
        """,
        (
            level.level_key,
            "hard" if "hard" in level.modifiers else "normal",
            hashlib.sha256(payload.encode("utf-8")).hexdigest(),
            REFERENCE_LEVEL_ORIGIN,
            level.number,
            level.completeness,
            level.groups_expected,
            IMPORTER_VERSION,
            now,
            now,
        ),
    )
    return int(cur.lastrowid)


def _delete_level(conn: sqlite3.Connection, level_key: str, number: int) -> None:
    conn.execute(
        "DELETE FROM reference_sources WHERE source_kind = ? AND level_number = ?",
        (SOURCE_KIND, number),
    )
    row = conn.execute(
        "SELECT id FROM level_instances WHERE level_key = ?", (level_key,)
    ).fetchone()
    if row is None:
        return
    conn.execute("DELETE FROM level_instances WHERE id = ?", (int(row["id"]),))


def _sense_id(conn: sqlite3.Connection, word_id: int | None, sense_key: str | None) -> int | None:
    if word_id is None or not sense_key:
        return None
    row = conn.execute(
        "SELECT id FROM word_senses WHERE word_id = ? AND sense_key = ?",
        (word_id, sense_key),
    ).fetchone()
    return int(row["id"]) if row else None


def _record_decoys(
    conn: sqlite3.Connection, level: FixtureLevel, level_id: int, now: str
) -> int:
    """Правдоподобные чужие дома токенов уровня.

    Для записи оригинала любое такое пересечение — авторское решение: игра
    вышла и работает. Отмеченные в разборе ловушки помечаются planned = 1,
    остальные остаются диагностикой, а не браком.
    """
    traps_text = " ".join(level.traps).lower()
    rows = list(
        conn.execute(
            """
            SELECT t.id AS token_id, t.group_id AS group_id, w.normalized AS word
              FROM level_tokens t
              LEFT JOIN words w ON w.id = t.word_id
             WHERE t.level_id = ?
            """,
            (level_id,),
        )
    )
    groups = {
        int(row["id"]): row["category_key"]
        for row in conn.execute(
            """
            SELECT g.id AS id, c.category_key AS category_key
              FROM level_groups g JOIN categories c ON c.id = g.category_id
             WHERE g.level_id = ?
            """,
            (level_id,),
        )
    }
    from .reference_resolve import PLAYABLE_STATUSES

    placeholders = ",".join("?" for _ in PLAYABLE_STATUSES)
    created = 0
    for row in rows:
        word = row["word"]
        if not word:
            continue
        accepting = {
            item["category_key"]
            for item in conn.execute(
                f"""
                SELECT c.category_key AS category_key
                  FROM memberships m
                  JOIN categories c ON c.id = m.category_id
                  JOIN words w      ON w.id = m.word_id
                 WHERE w.normalized = ?
                   AND m.review_status IN ({placeholders})
                   AND m.semantic_status <> 'incorrect'
                """,
                (word, *PLAYABLE_STATUSES),
            )
        }
        home = groups.get(int(row["group_id"]))
        for group_id, category_key in groups.items():
            if group_id == int(row["group_id"]) or category_key not in accepting:
                continue
            planned = 1 if word in traps_text else 0
            conn.execute(
                """
                INSERT OR IGNORE INTO level_decoys
                    (level_id, token_id, decoy_group_id, decoy_category_id, planned,
                     plausibility, note, created_at)
                VALUES (?, ?, ?, NULL, ?, NULL, ?, ?)
                """,
                (level_id, int(row["token_id"]), group_id, planned,
                 f"дом по записи: {home}", now),
            )
            created += 1
    counts = conn.execute(
        "SELECT SUM(planned) AS planned, SUM(1 - planned) AS unplanned "
        "  FROM level_decoys WHERE level_id = ?",
        (level_id,),
    ).fetchone()
    conn.execute(
        "UPDATE level_instances SET planned_decoy_count = ?, unplanned_decoy_count = ? "
        " WHERE id = ?",
        (int(counts["planned"] or 0), int(counts["unplanned"] or 0), level_id),
    )
    return created


def _provenance(
    conn: sqlite3.Connection, level_number: int, group_index: int | None,
    entity_type: str, entity_key: str, observability: str, source_file: str,
    detail: str, now: str,
) -> None:
    conn.execute(
        """
        INSERT INTO reference_sources
            (source_kind, source_file, level_number, group_index, entity_type,
             entity_key, observability, detail, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT (source_kind, entity_type, entity_key) DO UPDATE SET
            observability = excluded.observability,
            detail = excluded.detail
        """,
        (SOURCE_KIND, source_file, level_number, group_index, entity_type,
         entity_key, observability, detail, now),
    )


# ------------------------------------------------------------------------ экспорт


def export_level(conn: sqlite3.Connection, number: int) -> dict:
    """Нормализованный уровень из базы — то, что сравнивается с записью."""
    level = conn.execute(
        "SELECT id, reference_level, recorded_completeness, groups_expected "
        "  FROM level_instances WHERE level_key = ?",
        (f"REF{number:03d}",),
    ).fetchone()
    if level is None:
        return {}
    level_id = int(level["id"])
    groups = []
    for group in conn.execute(
        """
        SELECT g.id AS id, g.position AS position, g.label_source AS label_source,
               COALESCE(l.display_text, g.reference_name) AS name
          FROM level_groups g
          LEFT JOIN category_labels l ON l.id = g.display_label_id
         WHERE g.level_id = ?
         ORDER BY g.position
        """,
        (level_id,),
    ):
        slots = []
        for token in conn.execute(
            """
            SELECT t.slot, t.display_text, t.token_kind, t.token_form, t.pieces,
                   t.observability, sg.reference_name AS emitted_by
              FROM level_tokens t
              LEFT JOIN level_groups sg ON sg.id = t.source_group_id
             WHERE t.group_id = ? ORDER BY t.slot
            """,
            (int(group["id"]),),
        ):
            slots.append(
                {
                    "position": int(token["slot"]),
                    "text": token["display_text"],
                    "token_kind": token["token_kind"],
                    "token_form": token["token_form"],
                    "observability": token["observability"],
                    "pieces": json.loads(token["pieces"]) if token["pieces"] else [],
                    "emitted_by": token["emitted_by"],
                }
            )
        groups.append(
            {
                "index": int(group["position"]),
                "name": group["name"],
                "label_source": group["label_source"],
                "slots": slots,
            }
        )
    meta = []
    for row in conn.execute(
        """
        SELECT src.reference_name AS source_group, tgt.reference_name AS target_group,
               t.display_text AS token, t.token_form AS form
          FROM level_dependencies d
          JOIN level_groups src ON src.id = d.from_group_id
          JOIN level_tokens t   ON t.id = d.to_token_id
          JOIN level_groups tgt ON tgt.id = t.group_id
         WHERE d.level_id = ?
         ORDER BY t.display_text
        """,
        (level_id,),
    ):
        meta.append(
            {
                "token": row["token"],
                "form": row["form"],
                "target_group": row["target_group"],
                "source_group": row["source_group"],
            }
        )
    return {
        "level": number,
        "completeness": level["recorded_completeness"],
        "groups_expected": int(level["groups_expected"] or 0),
        "groups": groups,
        "meta_links": meta,
    }


def _normalized_fixture(level: FixtureLevel) -> dict:
    payload = level.as_dict()
    for link in payload["meta_links"]:
        # В экспорте форма берётся с самого токена, а в записи она продублирована
        # в meta_links; сравниваем по токену, чтобы дубль не считался расхождением.
        slot_form = next(
            (
                slot["token_form"]
                for group in payload["groups"]
                for slot in group["slots"]
                if normalize_name(slot["text"]) == normalize_name(link["token"])
            ),
            link["form"],
        )
        link["form"] = slot_form
    payload["meta_links"].sort(key=lambda item: item["token"])
    payload.pop("modifiers", None)
    return payload


def diff_level(conn: sqlite3.Connection, level: FixtureLevel) -> list[str]:
    """Расхождения «запись против базы». Пустой список = уровень воспроизведён."""
    expected = _normalized_fixture(level)
    actual = export_level(conn, level.number)
    if not actual:
        return [f"уровень {level.number} в базе отсутствует"]
    actual.pop("modifiers", None)
    problems: list[str] = []
    if expected["completeness"] != actual["completeness"]:
        problems.append(
            f"полнота записи: {expected['completeness']} != {actual['completeness']}"
        )
    if expected["groups_expected"] != actual["groups_expected"]:
        problems.append("число категорий уровня не совпало")
    if len(expected["groups"]) != len(actual["groups"]):
        problems.append(
            f"групп записано {len(expected['groups'])}, в базе {len(actual['groups'])}"
        )
        return problems
    for want, got in zip(expected["groups"], actual["groups"], strict=True):
        prefix = f"группа {want['index']} «{want['name']}»"
        if normalize_name(want["name"]) != normalize_name(got["name"]):
            problems.append(f"{prefix}: имя в базе «{got['name']}»")
        if want["label_source"] != got["label_source"]:
            problems.append(f"{prefix}: источник имени {got['label_source']}")
        if len(want["slots"]) != len(got["slots"]):
            problems.append(f"{prefix}: слотов {len(got['slots'])}")
            continue
        for want_slot, got_slot in zip(want["slots"], got["slots"], strict=True):
            for field_name in ("text", "token_kind", "token_form", "observability",
                               "pieces", "emitted_by"):
                a, b = want_slot[field_name], got_slot[field_name]
                if field_name == "text":
                    a, b = normalize_name(str(a)), normalize_name(str(b))
                if field_name == "emitted_by":
                    a = normalize_name(str(a or ""))
                    b = normalize_name(str(b or ""))
                if a != b:
                    problems.append(
                        f"{prefix}, слот {want_slot['position']} "
                        f"«{want_slot['text']}»: {field_name} = {b!r}, ожидалось {a!r}"
                    )
    if len(expected["meta_links"]) != len(actual["meta_links"]):
        problems.append(
            f"мета-ссылок записано {len(expected['meta_links'])}, "
            f"в базе {len(actual['meta_links'])}"
        )
    else:
        for want, got in zip(expected["meta_links"], actual["meta_links"], strict=True):
            for field_name in ("token", "form", "target_group", "source_group"):
                if normalize_name(str(want[field_name])) != normalize_name(
                    str(got[field_name])
                ):
                    problems.append(
                        f"мета-ссылка «{want['token']}»: {field_name} = "
                        f"{got[field_name]!r}, ожидалось {want[field_name]!r}"
                    )
    return problems
