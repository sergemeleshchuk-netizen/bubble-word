"""Проверка сохранённого уровня: мета-граф плюс отрыв авторского разбиения.

Раньше вердикт по уровню был один бит: `solution_count == 1`. Он полезен как
диагностика и вреден как определение качества — по нему пришлось бы отклонить
половину референса, где orange честно принадлежит и фруктам, и цветам.

Здесь вердикт складывается из трёх независимых источников:

    мета-граф        проходим ли уровень из стартового состояния;
    отрыв разбиения  насколько авторский ответ сильнее лучшей альтернативы;
    ловушки          какие пересечения спроектированы, а какие вылезли сами.

Спроектированная ловушка живёт в `level_decoys` с `planned = 1` и браком не
считается. Незапланированная, которая тянет сильнее авторского дома, — брак.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field

from . import level_solver, meta_validation, structured
from .db import utc_now


@dataclass
class LevelAudit:
    level_key: str
    origin: str
    meta: meta_validation.MetaValidation
    assessment: level_solver.PartitionAssessment
    problems: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.problems

    def as_dict(self) -> dict[str, object]:
        return {
            "level_key": self.level_key,
            "origin": self.origin,
            "ok": self.ok,
            "meta": self.meta.as_dict(),
            "partition": self.assessment.as_dict(),
            "problems": self.problems,
        }


def audit_level(
    conn: sqlite3.Connection,
    level_id: int,
    *,
    index: level_solver.MembershipIndex | None = None,
    structures: structured.StructureIndex | None = None,
    margin_threshold: float = level_solver.DEFAULT_MARGIN_THRESHOLD,
    timeout_ms: int = level_solver.DEFAULT_TIMEOUT_MS,
) -> LevelAudit:
    index = index or level_solver.load_memberships(conn)
    structures = structures if structures is not None else structured.load(conn)

    level = conn.execute(
        "SELECT level_key, origin FROM level_instances WHERE id = ?", (level_id,)
    ).fetchone()
    if level is None:
        raise KeyError(f"уровня {level_id} нет")

    rows = list(
        conn.execute(
            """
            SELECT t.id AS token_id, t.display_text AS display, t.group_id AS group_id,
                   s.sense_key AS sense_key, w.normalized AS word,
                   c.category_key AS category_key
              FROM level_tokens t
              JOIN level_groups g ON g.id = t.group_id
              JOIN categories c   ON c.id = g.category_id
              LEFT JOIN words w        ON w.id = t.word_id
              LEFT JOIN word_senses s  ON s.id = t.sense_id
             WHERE t.level_id = ?
             ORDER BY g.position, t.slot
            """,
            (level_id,),
        )
    )
    tokens = [
        level_solver.Token(
            word=(row["word"] or row["display"]).strip().lower(),
            sense_key=row["sense_key"],
            display=row["display"],
        )
        for row in rows
    ]
    homes = {
        row["display"].strip().lower(): row["category_key"] for row in rows
    }
    planned = {
        (row["display"].strip().lower(), row["category_key"])
        for row in conn.execute(
            """
            SELECT t.display_text AS display, c.category_key AS category_key
              FROM level_decoys d
              JOIN level_tokens t ON t.id = d.token_id
              JOIN level_groups g ON g.id = d.decoy_group_id
              JOIN categories c   ON c.id = g.category_id
             WHERE d.level_id = ? AND d.planned = 1
            """,
            (level_id,),
        )
    }

    meta = meta_validation.validate_level_in_db(conn, level_id)
    assessment = level_solver.assess_partition(
        tokens, homes, index, structures,
        planned_decoys=planned,
        margin_threshold=margin_threshold,
        timeout_ms=timeout_ms,
        meta_ok=meta.ok,
        meta_problems=meta.problems,
    )
    return LevelAudit(
        level_key=level["level_key"],
        origin=level["origin"] or "generated",
        meta=meta,
        assessment=assessment,
        problems=list(assessment.hard_reject),
    )


def save_audit(conn: sqlite3.Connection, level_id: int, audit: LevelAudit) -> None:
    """Кладёт числа отрыва и состояние мета-графа рядом с уровнем."""
    now = utc_now()
    assessment = audit.assessment
    conn.execute(
        """
        UPDATE level_instances
           SET intended_partition_score = ?, best_alternative_score = ?,
               partition_margin = ?, planned_decoy_count = ?,
               unplanned_decoy_count = ?, meta_state = ?, updated_at = ?
         WHERE id = ?
        """,
        (
            assessment.intended_partition_score,
            assessment.best_alternative_score,
            assessment.partition_margin,
            assessment.planned_decoy_count,
            assessment.unplanned_decoy_count,
            json.dumps(audit.meta.as_dict(), ensure_ascii=False),
            now,
            level_id,
        ),
    )
    solver = assessment.solver
    if solver is None:
        return
    alternative = solver.alternative_partition
    conn.execute(
        """
        INSERT INTO level_solver_runs
            (level_id, solver_version, input_hash, parameters, outcome, solution_count,
             alternative_partition, reason, duration_ms, checked_at,
             intended_partition_score, best_alternative_score, partition_margin,
             planned_decoy_count, unplanned_decoy_count, intended_is_best)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            level_id,
            solver.solver_version,
            solver.input_hash,
            json.dumps(solver.parameters, ensure_ascii=False),
            solver.outcome,
            solver.solution_count,
            level_solver.format_solution(alternative) if alternative else None,
            "; ".join(assessment.hard_reject) or solver.reason,
            solver.duration_ms,
            now,
            assessment.intended_partition_score,
            assessment.best_alternative_score,
            assessment.partition_margin,
            assessment.planned_decoy_count,
            assessment.unplanned_decoy_count,
            1 if assessment.intended_is_best else 0,
        ),
    )
    # Незапланированные пересечения записываются явно: диагностика должна
    # лежать рядом с уровнем, а не в выводе команды.
    groups = {
        row["category_key"]: int(row["id"])
        for row in conn.execute(
            "SELECT g.id AS id, c.category_key AS category_key "
            "  FROM level_groups g JOIN categories c ON c.id = g.category_id "
            " WHERE g.level_id = ?",
            (level_id,),
        )
    }
    tokens = {
        row["display_text"].strip().lower(): int(row["id"])
        for row in conn.execute(
            "SELECT id, display_text FROM level_tokens WHERE level_id = ?", (level_id,)
        )
    }
    for decoy in assessment.decoys:
        token_id = tokens.get(decoy.token.strip().lower())
        group_id = groups.get(decoy.rival)
        if token_id is None or group_id is None:
            continue
        conn.execute(
            """
            INSERT INTO level_decoys
                (level_id, token_id, decoy_group_id, decoy_category_id, planned,
                 plausibility, note, created_at)
            VALUES (?, ?, ?, NULL, ?, ?, ?, ?)
            ON CONFLICT (level_id, token_id,
                         COALESCE(decoy_group_id, 0), COALESCE(decoy_category_id, 0))
            DO UPDATE SET plausibility = excluded.plausibility, note = excluded.note
            """,
            (
                level_id, token_id, group_id, 1 if decoy.planned else 0,
                decoy.rival_strength,
                f"дом «{decoy.home}» {decoy.home_strength:.2f}", now,
            ),
        )
    counts = conn.execute(
        "SELECT COALESCE(SUM(planned), 0) AS planned, "
        "       COALESCE(SUM(1 - planned), 0) AS unplanned "
        "  FROM level_decoys WHERE level_id = ?",
        (level_id,),
    ).fetchone()
    conn.execute(
        "UPDATE level_instances SET planned_decoy_count = ?, unplanned_decoy_count = ? "
        " WHERE id = ?",
        (int(counts["planned"]), int(counts["unplanned"]), level_id),
    )


def audit_all(
    conn: sqlite3.Connection,
    *,
    origins: tuple[str, ...] | None = None,
    level_keys: tuple[str, ...] | None = None,
    margin_threshold: float = level_solver.DEFAULT_MARGIN_THRESHOLD,
    timeout_ms: int = level_solver.DEFAULT_TIMEOUT_MS,
) -> list[LevelAudit]:
    index = level_solver.load_memberships(conn)
    structures = structured.load(conn)
    sql = "SELECT id, level_key FROM level_instances"
    clauses: list[str] = []
    params: list[object] = []
    if origins:
        clauses.append(f"origin IN ({','.join('?' for _ in origins)})")
        params.extend(origins)
    if level_keys:
        clauses.append(f"level_key IN ({','.join('?' for _ in level_keys)})")
        params.extend(level_keys)
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY level_key"

    audits: list[LevelAudit] = []
    for row in conn.execute(sql, params):
        audit = audit_level(
            conn, int(row["id"]), index=index, structures=structures,
            margin_threshold=margin_threshold, timeout_ms=timeout_ms,
        )
        save_audit(conn, int(row["id"]), audit)
        audits.append(audit)
    return audits
