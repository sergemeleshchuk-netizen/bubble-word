"""Сопоставление записи референса с содержимым базы.

Одно решение, вокруг которого крутится весь этап: **чем является группа
референса для нашей базы** — уже существующим правилом группировки или новым.

Соблазн решать это по имени максимально велик и максимально неверен. Из 95
групп первых десяти уровней имя прочитано с пузыря только у 24; остальные 71 —
наша формулировка по четвёрке. Проверять «есть ли в базе категория с таким
именем» для них значит измерять совпадение базы с собственными догадками.

Поэтому решает четвёрка, а имя только помогает:

    правило подходит, если оно уже держит >= 3 из 4 токенов
    либо имя совпало (точно или формой числа) и правило держит >= 2

Иначе заводится новое правило, выведенное из записи. Это не «мусор в базе»:
референс и есть библиотека авторских групп, ради перехода к которой всё
затевалось.

Резолвер намеренно **не видит** того, что сам же и создал: элементы с
``origin = 'reference_backfill'`` из индекса исключены. Иначе повторный прогон
планировщика на уже заполненной базе давал бы пустой патч, и патчи перестали бы
быть источником правды для чистой сборки.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass, field

from .reference_fixtures import FixtureGroup, normalize_name, normalize_token

REFERENCE_ORIGIN = "reference_backfill"

# Связи, которыми игра имеет право пользоваться.
PLAYABLE_STATUSES = ("approved", "alternative", "hard_only")

# Насколько уверенно имя референса совпало с нашим.
NAME_RANK_EXACT = 3
NAME_RANK_MORPH = 2      # разошлась только форма числа: color / colors
NAME_RANK_CONTAINED = 1  # наше имя уже: school / school supplies
NAME_RANK_NONE = 0

# Пороги переиспользования существующего правила.
REUSE_MIN_MEMBERS = 3
REUSE_MIN_MEMBERS_WITH_NAME = 2


def number_variants(value: str) -> set[str]:
    """Формы числа. Единственная морфология, которая здесь нужна."""
    base = normalize_name(value)
    out = {base}
    if base.endswith("es"):
        out.add(base[:-2])
    if base.endswith("s"):
        out.add(base[:-1])
    out.update({base + "s", base + "es"})
    return {v for v in out if v}


@dataclass
class BaseIndex:
    """Снимок базы, нужный для сопоставления. Читается один раз."""

    words: dict[str, int]                       # normalized -> word_id
    senses: dict[int, list[tuple[int, str]]]    # word_id -> [(sense_id, sense_key)]
    rules: dict[str, dict]                      # category_key -> строка правила
    rule_names: dict[str, set[str]]             # нормализованное имя -> {category_key}
    pools: dict[str, set[str]]                  # category_key -> {normalized слово}
    membership_senses: dict[tuple[str, str], str | None]  # (rule, слово) -> sense_key
    quartets: dict[tuple[str, ...], list[str]]  # подпись четвёрки -> [quartet_key]
    labels: dict[str, int]                      # label_key -> id

    def word_id(self, text: str) -> int | None:
        return self.words.get(normalize_token(text))

    def sense_count(self, text: str) -> int:
        wid = self.word_id(text)
        return len(self.senses.get(wid, ())) if wid else 0


def load_index(conn: sqlite3.Connection, *, include_reference: bool = False) -> BaseIndex:
    """Индекс базы. По умолчанию без того, что создано самим backfill'ом."""
    origin_filter = "" if include_reference else f" AND c.origin <> '{REFERENCE_ORIGIN}'"
    member_origin = "" if include_reference else f" AND m.source <> '{REFERENCE_ORIGIN}'"

    words = {
        row["normalized"]: int(row["id"])
        for row in conn.execute("SELECT id, normalized FROM words")
    }
    senses: dict[int, list[tuple[int, str]]] = {}
    for row in conn.execute("SELECT id, word_id, sense_key FROM word_senses ORDER BY id"):
        senses.setdefault(int(row["word_id"]), []).append((int(row["id"]), row["sense_key"]))

    rules: dict[str, dict] = {}
    rule_names: dict[str, set[str]] = {}
    for row in conn.execute(
        f"SELECT c.id, c.category_key, c.label, c.rule_type, c.relation_type, c.theme, "
        f"       c.concept_id, c.status, c.origin "
        f"  FROM categories c WHERE 1 = 1{origin_filter}"
    ):
        key = row["category_key"]
        rules[key] = dict(row)
        for name in (normalize_name(row["label"]), normalize_name(key.replace("_", " "))):
            if name:
                rule_names.setdefault(name, set()).add(key)

    # Алиасы концепта тоже дают имя правилу: 'colors' -> 'color'.
    for row in conn.execute(
        f"""
        SELECT a.alias AS alias, c.category_key AS category_key
          FROM category_aliases a
          JOIN categories c ON c.concept_id = a.concept_id
         WHERE 1 = 1{origin_filter}
        """
    ):
        name = normalize_name(row["alias"])
        if name:
            rule_names.setdefault(name, set()).add(row["category_key"])

    placeholders = ",".join("?" for _ in PLAYABLE_STATUSES)
    pools: dict[str, set[str]] = {}
    membership_senses: dict[tuple[str, str], str | None] = {}
    for row in conn.execute(
        f"""
        SELECT c.category_key AS category_key, w.normalized AS word, s.sense_key AS sense_key
          FROM memberships m
          JOIN categories c ON c.id = m.category_id
          JOIN words w      ON w.id = m.word_id
          LEFT JOIN word_senses s ON s.id = m.sense_id
         WHERE m.review_status IN ({placeholders})
           AND m.semantic_status <> 'incorrect'{member_origin}{origin_filter}
        """,
        PLAYABLE_STATUSES,
    ):
        pools.setdefault(row["category_key"], set()).add(row["word"])
        membership_senses.setdefault((row["category_key"], row["word"]), row["sense_key"])

    quartets: dict[tuple[str, ...], list[str]] = {}
    rows = conn.execute(
        """
        SELECT q.quartet_key AS quartet_key, w.normalized AS word
          FROM quartets q
          JOIN quartet_words qw ON qw.quartet_id = q.id
          JOIN words w          ON w.id = qw.word_id
         ORDER BY q.quartet_key, qw.slot
        """
    )
    grouped: dict[str, list[str]] = {}
    for row in rows:
        grouped.setdefault(row["quartet_key"], []).append(row["word"])
    for quartet_key, members in grouped.items():
        quartets.setdefault(tuple(sorted(members)), []).append(quartet_key)

    labels = {
        row["label_key"]: int(row["id"])
        for row in conn.execute("SELECT id, label_key FROM category_labels")
    }

    return BaseIndex(
        words=words,
        senses=senses,
        rules=rules,
        rule_names=rule_names,
        pools=pools,
        membership_senses=membership_senses,
        quartets=quartets,
        labels=labels,
    )


@dataclass
class GroupResolution:
    """Решение по одной группе записи."""

    group: FixtureGroup
    level_number: int
    rule_key: str | None          # существующее правило, если переиспользуем
    decision: str                 # reuse | new_rule
    name_rank: int
    members_present: tuple[str, ...] = ()
    members_missing: tuple[str, ...] = ()
    new_rule_key: str | None = None
    rule_type: str = "unclassified"
    candidates: list[tuple[str, int, int]] = field(default_factory=list)

    @property
    def target_rule_key(self) -> str:
        key = self.rule_key or self.new_rule_key
        assert key is not None
        return key

    @property
    def is_new(self) -> bool:
        return self.decision == "new_rule"


def _name_rank(reference_name: str, index: BaseIndex) -> dict[str, int]:
    """Ранг совпадения имени для каждого правила-кандидата."""
    ranks: dict[str, int] = {}
    target = normalize_name(reference_name)
    for key in index.rule_names.get(target, ()):  # точное совпадение
        ranks[key] = NAME_RANK_EXACT
    for variant in number_variants(reference_name):
        for key in index.rule_names.get(variant, ()):
            ranks.setdefault(key, NAME_RANK_MORPH)
    if target:
        for name, keys in index.rule_names.items():
            if name == target:
                continue
            if re.search(rf"\b{re.escape(target)}\b", name) or re.search(
                rf"\b{re.escape(name)}\b", target
            ):
                for key in keys:
                    ranks.setdefault(key, NAME_RANK_CONTAINED)
    return ranks


def resolve_group(
    group: FixtureGroup,
    level_number: int,
    index: BaseIndex,
    *,
    rule_type: str = "unclassified",
    taken_keys: set[str] | None = None,
) -> GroupResolution:
    """Переиспользовать существующее правило или завести новое. Детерминировано."""
    tokens = [slot.normalized for slot in group.slots]
    ranks = _name_rank(group.name, index)

    scored: list[tuple[str, int, int]] = []
    considered = set(ranks) | {
        key for key, pool in index.pools.items() if pool & set(tokens)
    }
    for key in sorted(considered):
        if key not in index.rules:
            continue
        present = sum(1 for token in tokens if token in index.pools.get(key, ()))
        scored.append((key, ranks.get(key, NAME_RANK_NONE), present))

    # Порядок отбора: сначала полнота четвёрки, потом совпадение имени, потом
    # узость пула (узкое правило точнее широкого), потом ключ — для стабильности.
    scored.sort(
        key=lambda item: (
            -item[2],
            -item[1],
            len(index.pools.get(item[0], ())),
            item[0],
        )
    )

    best_key: str | None = None
    for key, rank, present in scored:
        if present >= REUSE_MIN_MEMBERS or (
            rank >= NAME_RANK_MORPH and present >= REUSE_MIN_MEMBERS_WITH_NAME
        ):
            best_key = key
            break

    if best_key is not None:
        pool = index.pools.get(best_key, set())
        return GroupResolution(
            group=group,
            level_number=level_number,
            rule_key=best_key,
            decision="reuse",
            name_rank=ranks.get(best_key, NAME_RANK_NONE),
            members_present=tuple(t for t in tokens if t in pool),
            members_missing=tuple(t for t in tokens if t not in pool),
            rule_type=index.rules[best_key]["rule_type"] or rule_type,
            candidates=scored[:5],
        )

    new_key = _new_rule_key(group, level_number, index, taken_keys or set())
    return GroupResolution(
        group=group,
        level_number=level_number,
        rule_key=None,
        decision="new_rule",
        name_rank=max(ranks.values(), default=NAME_RANK_NONE),
        members_present=(),
        members_missing=tuple(tokens),
        new_rule_key=new_key,
        rule_type=rule_type,
        candidates=scored[:5],
    )


def _new_rule_key(
    group: FixtureGroup, level_number: int, index: BaseIndex, taken: set[str]
) -> str:
    """Ключ нового правила: ref_<имя>, при коллизии — с номером.

    Коллизия здесь содержательная, а не техническая: MUSIC на уровне 3 — это
    жанры, на уровне 6 — инструменты. Одно имя, разные правила; сливать их
    нельзя, поэтому второе получает суффикс.
    """
    slug = re.sub(r"[^a-z0-9]+", "_", normalize_name(group.name)).strip("_") or "group"
    base = f"ref_{slug}"
    if base not in taken and base not in index.rules:
        return base
    index_suffix = 2
    while f"{base}_{index_suffix}" in taken or f"{base}_{index_suffix}" in index.rules:
        index_suffix += 1
    return f"{base}_{index_suffix}"
