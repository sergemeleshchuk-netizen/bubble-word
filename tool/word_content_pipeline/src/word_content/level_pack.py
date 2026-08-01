"""Выгрузка готового пакета уровней наружу из базы.

База — источник правды, но читать её глазами нельзя, а пакет уровней должен
быть виден в репозитории и на сайте. Здесь ровно одно: собрать уровни с общим
префиксом ключа в один JSON, ничего не досочиняя.

Отличие от `level_review`: тот пакет — про приёмку человеком (бланк решений,
предупреждения, смена статуса на `review_pending`). Этот — про содержимое:
что игрок увидит на поле и как это соотносится с записью оригинала.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from . import composition as composition_mod

PACK_FORMAT = "bubble-level-pack/1.0"


def build(conn: sqlite3.Connection, prefix: str) -> dict:
    """Собирает пакет уровней с ключами `<prefix>NNN`."""
    levels: list[dict] = []
    rows = list(
        conn.execute(
            """
            SELECT id, level_key, status, difficulty_score, difficulty_explanation,
                   solution_count, partition_margin, intended_partition_score,
                   best_alternative_score, planned_decoy_count, unplanned_decoy_count,
                   content_hash, generator_version, random_seed, tier
              FROM level_instances
             WHERE level_key LIKE ? || '%'
             ORDER BY level_key
            """,
            (prefix,),
        )
    )
    for number, row in enumerate(rows, start=1):
        level_id = int(row["id"])
        groups = _groups(conn, level_id)
        meta_links = _meta_links(conn, level_id)
        recorded = composition_mod.for_level(number)
        levels.append(
            {
                "level": number,
                "level_key": row["level_key"],
                "status": row["status"],
                "tier": row["tier"],
                "difficulty": {
                    "score": row["difficulty_score"],
                    "explanation": row["difficulty_explanation"],
                },
                "solver": {
                    "solution_count": row["solution_count"],
                    "intended_partition_score": row["intended_partition_score"],
                    "best_alternative_score": row["best_alternative_score"],
                    "partition_margin": row["partition_margin"],
                    "planned_decoys": row["planned_decoy_count"],
                    "unplanned_decoys": row["unplanned_decoy_count"],
                },
                # Состав рядом с записью оригинала: пакет заявлен как повтор её
                # кривой, и расхождение должно быть видно без пересчёта.
                "composition": {
                    "categories": {"pack": len(groups), "recorded": recorded.categories},
                    "meta_links": {"pack": len(meta_links), "recorded": recorded.meta_links},
                    "recorded_source": recorded.source,
                },
                "groups": groups,
                "meta_links": meta_links,
                "content_hash": row["content_hash"],
                "generator_version": row["generator_version"],
                "random_seed": row["random_seed"],
            }
        )

    return {
        "format": PACK_FORMAT,
        "prefix": prefix,
        "levels": levels,
        "totals": _totals(levels),
    }


def _groups(conn: sqlite3.Connection, level_id: int) -> list[dict]:
    groups: list[dict] = []
    for row in conn.execute(
        """
        SELECT g.id AS id, g.position AS position,
               COALESCE(l.display_text, c.label) AS label,
               c.category_key AS rule_key, c.rule AS rule, c.rule_type AS rule_type
          FROM level_groups g
          JOIN categories c ON c.id = g.category_id
          LEFT JOIN category_labels l ON l.id = g.display_label_id
         WHERE g.level_id = ? ORDER BY g.position
        """,
        (level_id,),
    ):
        words = [
            {
                "text": token["display_text"],
                "kind": token["token_kind"],
                **(
                    {"emitted_by": token["source_label"]}
                    if token["token_kind"] == "category_output"
                    else {}
                ),
            }
            for token in conn.execute(
                """
                SELECT t.display_text AS display_text, t.token_kind AS token_kind,
                       COALESCE(sl.display_text, sc.label) AS source_label
                  FROM level_tokens t
                  LEFT JOIN level_groups sg ON sg.id = t.source_group_id
                  LEFT JOIN categories sc   ON sc.id = sg.category_id
                  LEFT JOIN category_labels sl ON sl.id = sg.display_label_id
                 WHERE t.group_id = ? ORDER BY t.slot
                """,
                (int(row["id"]),),
            )
        ]
        groups.append(
            {
                "position": int(row["position"]),
                "label": row["label"],
                "rule_key": row["rule_key"],
                "rule": row["rule"],
                "rule_type": row["rule_type"],
                "words": words,
            }
        )
    return groups


def _meta_links(conn: sqlite3.Connection, level_id: int) -> list[dict]:
    return [
        {
            "token": row["token"],
            "source_group": row["source_label"],
            "target_group": row["target_label"],
            "depth": int(row["depth"]),
        }
        for row in conn.execute(
            """
            SELECT t.display_text AS token, d.depth AS depth,
                   COALESCE(sl.display_text, sc.label) AS source_label,
                   COALESCE(tl.display_text, tc.label) AS target_label
              FROM level_dependencies d
              JOIN level_tokens t  ON t.id = d.to_token_id
              JOIN level_groups sg ON sg.id = d.from_group_id
              JOIN categories sc   ON sc.id = sg.category_id
              LEFT JOIN category_labels sl ON sl.id = sg.display_label_id
              JOIN level_groups tg ON tg.id = t.group_id
              JOIN categories tc   ON tc.id = tg.category_id
              LEFT JOIN category_labels tl ON tl.id = tg.display_label_id
             WHERE d.level_id = ? ORDER BY t.display_text
            """,
            (level_id,),
        )
    ]


def _totals(levels: list[dict]) -> dict:
    words = [
        word["text"].strip().lower()
        for level in levels
        for group in level["groups"]
        for word in group["words"]
    ]
    return {
        "levels": len(levels),
        "groups": sum(len(level["groups"]) for level in levels),
        "bubbles": len(words),
        "distinct_words": len(set(words)),
        "meta_links": sum(len(level["meta_links"]) for level in levels),
        "levels_with_meta": sum(1 for level in levels if level["meta_links"]),
        "recorded_groups": sum(
            level["composition"]["categories"]["recorded"] for level in levels
        ),
        "recorded_meta_links": sum(
            level["composition"]["meta_links"]["recorded"] for level in levels
        ),
        "solver_valid": sum(1 for level in levels if level["status"] == "solver_valid"),
    }


def write(path: Path, pack: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return path
