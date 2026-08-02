"""Семантика собранного пакета: чем новая двадцатка отличается от старой.

Оценщик уровней (`level_eval`) меряет сложность и фан. Он не отвечает на вопрос,
из чего эта сложность сделана: уровень, где каждое второе слово стоит нишевым
значением, и уровень, где все слова читаются сразу, могут получить одинаковую D.
Разницу видно только здесь.

Метрика связности по SWOW считается той же формулой, которой получены 52% у
первой сборки двадцатки и 22% у записи оригинала. Формулу трогать нельзя: на
ней держится всё сравнение before/after. Поэтому здесь она названа явно —
группа считается несвязной, если ни одна пара её слов не дала связи, — а
отдельно показано, сколько групп вообще было чем измерить.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from itertools import combinations

from . import quartet_semantics

# Виды токенов, от которых база обязана знать значение. Результат другой
# категории сюда не входит: он проверяется мета-графом, а не словарём.
LEXICAL_KINDS = ("lexical_word", "chunked_word", "picture_token")


@dataclass
class GroupSemantics:
    level_key: str
    category_key: str
    label: str
    mode: str
    lexical_slots: int = 0
    unresolved: int = 0
    primary: int = 0
    common_secondary: int = 0
    specialist: int = 0
    obscure: int = 0
    anchors: int = 0
    meta_outputs: int = 0
    swow_observed_pairs: int = 0
    swow_positive_pairs: int = 0
    words: tuple[str, ...] = ()

    @property
    def anchorless(self) -> bool:
        if self.mode in quartet_semantics.ANCHOR_EXEMPT:
            return False
        return self.lexical_slots > 0 and self.anchors == 0

    @property
    def swow_measurable(self) -> bool:
        return self.swow_observed_pairs > 0

    @property
    def swow_disconnected(self) -> bool:
        """Формула пакета: ни одной положительной пары. Не менять."""
        return self.swow_positive_pairs == 0


@dataclass
class PackSemantics:
    prefix: str
    groups: list[GroupSemantics] = field(default_factory=list)
    swow_source: str = "swow"

    # ---- слоты
    @property
    def lexical_slots(self) -> int:
        return sum(g.lexical_slots for g in self.groups)

    @property
    def unresolved_slots(self) -> int:
        return sum(g.unresolved for g in self.groups)

    @property
    def resolved_ratio(self) -> float:
        return 1.0 if not self.lexical_slots else (
            (self.lexical_slots - self.unresolved_slots) / self.lexical_slots
        )

    @property
    def primary_slots(self) -> int:
        return sum(g.primary for g in self.groups)

    @property
    def common_secondary_slots(self) -> int:
        return sum(g.common_secondary for g in self.groups)

    @property
    def specialist_slots(self) -> int:
        return sum(g.specialist for g in self.groups)

    @property
    def obscure_slots(self) -> int:
        return sum(g.obscure for g in self.groups)

    # ---- якоря
    @property
    def anchorless_groups(self) -> int:
        return sum(1 for g in self.groups if g.anchorless)

    @property
    def min_anchors_in_group(self) -> int:
        lexical = [g for g in self.groups if g.lexical_slots and g.mode
                   not in quartet_semantics.ANCHOR_EXEMPT]
        return min((g.anchors for g in lexical), default=0)

    # ---- SWOW
    @property
    def swow_scored_groups(self) -> int:
        return len(self.groups)

    @property
    def swow_measurable_groups(self) -> int:
        return sum(1 for g in self.groups if g.swow_measurable)

    @property
    def swow_exempt_groups(self) -> int:
        """Группы, для которых попарные ассоциации ничего не измеряют."""
        return sum(
            1 for g in self.groups if g.mode not in quartet_semantics.SWOW_MEANINGFUL
        )

    @property
    def swow_disconnected_groups(self) -> int:
        return sum(1 for g in self.groups if g.swow_disconnected)

    @property
    def swow_disconnected_ratio(self) -> float:
        return (
            0.0 if not self.groups
            else self.swow_disconnected_groups / len(self.groups)
        )

    @property
    def meta_outputs(self) -> int:
        return sum(g.meta_outputs for g in self.groups)

    def lines(self) -> list[str]:
        return [
            f"лексических слотов:            {self.lexical_slots}",
            f"  без разрешённого значения:   {self.unresolved_slots} "
            f"(доля разрешённых {self.resolved_ratio:.1%})",
            f"  главным значением:           {self.primary_slots}",
            f"  вторым, но известным:        {self.common_secondary_slots}",
            f"  узким значением:             {self.specialist_slots}",
            f"  редким значением:            {self.obscure_slots}",
            f"групп без ясного якоря:        {self.anchorless_groups}",
            f"минимум якорей в группе:       {self.min_anchors_in_group}",
            f"групп всего:                   {len(self.groups)}",
            f"  SWOW было чем измерить:      {self.swow_measurable_groups}",
            f"  режим без попарных связей:   {self.swow_exempt_groups} "
            f"(структура, части, мета, игра слов)",
            f"  SWOW не нашёл ни одной связи:{self.swow_disconnected_groups} "
            f"({self.swow_disconnected_ratio:.1%})",
            f"токенов-результатов категорий: {self.meta_outputs}",
            f"источник ассоциаций:           {self.swow_source}",
        ]

    def as_dict(self) -> dict[str, object]:
        return {
            "lexical_slots": self.lexical_slots,
            "unresolved_slots": self.unresolved_slots,
            "resolved_ratio": round(self.resolved_ratio, 4),
            "primary_slots": self.primary_slots,
            "common_secondary_slots": self.common_secondary_slots,
            "specialist_slots": self.specialist_slots,
            "obscure_slots": self.obscure_slots,
            "anchorless_groups": self.anchorless_groups,
            "min_anchors_in_group": self.min_anchors_in_group,
            "groups": len(self.groups),
            "swow_measurable_groups": self.swow_measurable_groups,
            "swow_exempt_groups": self.swow_exempt_groups,
            "swow_disconnected_groups": self.swow_disconnected_groups,
            "swow_disconnected_ratio": round(self.swow_disconnected_ratio, 4),
            "meta_outputs": self.meta_outputs,
            "swow_source": self.swow_source,
        }


def evaluate(
    conn: sqlite3.Connection,
    prefix: str,
    *,
    associations,
    anchor_recognition_min: float = 0.75,
    anchor_activation_min: float = 0.60,
) -> PackSemantics:
    """Семантический профиль пакета уровней по префиксу ключа."""
    pack = PackSemantics(prefix=prefix, swow_source=getattr(associations, "source", "swow"))
    rows = conn.execute(
        """
        SELECT lg.id AS group_id, li.level_key AS level_key,
               c.category_key AS category_key, c.rule_type AS rule_type,
               COALESCE(c.label, '') AS label
          FROM level_groups lg
          JOIN level_instances li ON li.id = lg.level_id
          JOIN categories c       ON c.id = lg.category_id
         WHERE li.level_key LIKE ? || '%'
         ORDER BY li.id, lg.position
        """,
        (prefix,),
    ).fetchall()

    for row in rows:
        tokens = conn.execute(
            """
            SELECT t.token_kind AS token_kind, t.sense_mode AS sense_mode,
                   t.sense_id AS sense_id, w.normalized AS normalized,
                   COALESCE(s.accessibility_class, 'unresolved') AS accessibility_class,
                   s.recognition_score AS recognition_score,
                   s.activation_score AS activation_score
              FROM level_tokens t
              LEFT JOIN words w       ON w.id = t.word_id
              LEFT JOIN word_senses s ON s.id = t.sense_id
             WHERE t.group_id = ?
             ORDER BY t.slot
            """,
            (row["group_id"],),
        ).fetchall()

        all_surface = bool(tokens) and all(
            (token["sense_mode"] or "lexical") == "surface_form" for token in tokens
        )
        group = GroupSemantics(
            level_key=row["level_key"],
            category_key=row["category_key"],
            label=row["label"],
            mode=quartet_semantics.coherence_mode(
                row["rule_type"], all_surface_form=all_surface
            ),
            words=tuple(t["normalized"] for t in tokens if t["normalized"]),
        )
        for token in tokens:
            kind = token["token_kind"] or "lexical_word"
            if kind == "category_output":
                group.meta_outputs += 1
                continue
            if kind not in LEXICAL_KINDS:
                continue
            if (token["sense_mode"] or "lexical") == "surface_form":
                continue
            group.lexical_slots += 1
            access = token["accessibility_class"]
            if token["sense_id"] is None or access == "unresolved":
                group.unresolved += 1
            elif access == "primary":
                group.primary += 1
            elif access == "common_secondary":
                group.common_secondary += 1
            elif access == "specialist":
                group.specialist += 1
            elif access == "obscure":
                group.obscure += 1
            slot = quartet_semantics.SlotSemantics(
                word=token["normalized"] or "",
                token_kind=kind,
                sense_mode=token["sense_mode"] or "lexical",
                sense_id=token["sense_id"],
                accessibility_class=access,
                recognition_score=token["recognition_score"],
                activation_score=token["activation_score"],
            )
            if slot.is_anchor(
                recognition_min=anchor_recognition_min,
                activation_min=anchor_activation_min,
            ):
                group.anchors += 1

        # Связность считается по видимым на поле словам, включая те, что стоят
        # кусочками: игрок ассоциирует пузыри, а не строки базы.
        words = [word for word in group.words if word]
        for first, second in combinations(words, 2):
            measurable = associations.observed(first, second) \
                if hasattr(associations, "observed") else True
            if not measurable:
                continue
            group.swow_observed_pairs += 1
            if associations.sym(first, second) > 0:
                group.swow_positive_pairs += 1
        pack.groups.append(group)

    return pack
