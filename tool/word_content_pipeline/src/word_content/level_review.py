"""Пакет на приёмку уровня и применение решений.

Это единственное место во всей системе, где появляется мнение человека.
Он не подтверждает слова, связи, категории и четвёрки по одной — он смотрит
собранный уровень целиком и говорит «беру», «не беру» или «почти».

Пакет отвечает на вопросы, которые возникают при такой оценке:
понятны ли категории, естественны ли конкретные четыре слова, есть ли спорная
связь, единственно ли решение, с чего игрок начнёт, не повторяется ли уровень
с соседними, не длинные ли надписи, нет ли рисков.

Обратная связь точечная. Уровень отклоняют целиком, но причина, если она
названа, возвращается на конкретный объект: плохая связь выключается, слабая
четвёрка отключается, спорная категория уходит из генерации. Три кода из
девяти намеренно не пишут в базу ничего: дефект принадлежит комбинации,
а не контенту, и вычёркивать из-за него нормальные слова нельзя.
"""

from __future__ import annotations

import csv
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .db import utc_now

# Код причины -> что с ним делать в базе. None означает «ничего»:
# дефект есть только у этой комбинации.
REASON_TARGETS: dict[str, str | None] = {
    "bad_membership": "membership",
    "bad_sense": "membership",
    "weak_category_variant": "category",
    "weak_quartet": "quartet",
    "level_only_conflict": None,
    "ui_text_problem": None,
    "risk_problem": "membership",
    "campaign_repeat": None,
    "wrong_difficulty": None,
}

DECISIONS = ("accept", "reject", "needs_changes")
STATUS_BY_DECISION = {
    "accept": "accepted",
    "reject": "rejected",
    "needs_changes": "needs_changes",
}

# Надпись длиннее этого числа символов не влезает в пузырь на телефоне.
MAX_DISPLAY_LENGTH = 14
MAX_LABEL_LENGTH = 22


@dataclass
class LevelPackage:
    level_key: str
    status: str
    tier: str
    solution_count: int | None
    difficulty_score: float | None
    difficulty_components: dict[str, float]
    difficulty_explanation: str
    generator_version: str
    random_seed: int | None
    content_hash: str
    solver: dict[str, object]
    groups: list[dict[str, object]]
    competing: list[dict[str, object]]
    cooldowns: list[dict[str, object]]
    ui_warnings: list[str]
    risk_warnings: list[str]

    def as_dict(self) -> dict[str, object]:
        return {
            "level_key": self.level_key,
            "status": self.status,
            "tier": self.tier,
            "solution_count": self.solution_count,
            "difficulty": {
                "score": self.difficulty_score,
                "components": self.difficulty_components,
                "explanation": self.difficulty_explanation,
            },
            "solver": self.solver,
            "groups": self.groups,
            "plausible_competing_memberships": self.competing,
            "cooldowns": self.cooldowns,
            "ui_warnings": self.ui_warnings,
            "risk_warnings": self.risk_warnings,
            "generator_version": self.generator_version,
            "random_seed": self.random_seed,
            "content_hash": self.content_hash,
        }


def build(conn: sqlite3.Connection, *, statuses: tuple[str, ...] = ("solver_valid", "candidate"),
          limit: int | None = None) -> list[LevelPackage]:
    """Собирает пакеты по уровням в указанных статусах."""
    placeholders = ",".join("?" for _ in statuses)
    sql = (
        f"SELECT * FROM level_instances WHERE status IN ({placeholders}) ORDER BY level_key"
    )
    if limit:
        sql += f" LIMIT {int(limit)}"
    return [_package(conn, row) for row in conn.execute(sql, statuses)]


def _package(conn: sqlite3.Connection, level: sqlite3.Row) -> LevelPackage:
    level_id = int(level["id"])
    groups: list[dict[str, object]] = []
    own_categories: set[str] = set()
    ui_warnings: list[str] = []
    risk_warnings: list[str] = []

    for group in conn.execute(
        """
        SELECT g.id AS group_id, g.position AS position, c.category_key AS category_key,
               c.label AS label, c.rule AS rule, c.relation_type AS relation_type,
               q.quartet_key AS quartet_key, q.cohesion_score AS cohesion,
               q.familiarity_score AS familiarity, q.ambiguity_pressure AS ambiguity,
               q.risk_state AS risk_state
          FROM level_groups g
          JOIN categories c ON c.id = g.category_id
          LEFT JOIN quartets q ON q.id = g.quartet_id
         WHERE g.level_id = ? ORDER BY g.position
        """,
        (level_id,),
    ):
        own_categories.add(group["category_key"])
        tokens = [
            {
                "slot": int(row["slot"]),
                "display": row["display_text"],
                "sense_key": row["sense_key"],
                "definition": row["definition"],
                "sense_mode": row["sense_mode"],
                "familiarity": row["familiarity_score"],
                "role": row["role"],
            }
            for row in conn.execute(
                """
                SELECT t.slot AS slot, t.display_text AS display_text, t.sense_mode AS sense_mode,
                       t.role AS role, s.sense_key AS sense_key, s.definition AS definition,
                       w.familiarity_score AS familiarity_score
                  FROM level_tokens t
                  JOIN words w ON w.id = t.word_id
                  LEFT JOIN word_senses s ON s.id = t.sense_id
                 WHERE t.group_id = ? ORDER BY t.slot
                """,
                (group["group_id"],),
            )
        ]
        if len(group["label"]) > MAX_LABEL_LENGTH:
            ui_warnings.append(
                f"длинная надпись категории: {group['label']} ({len(group['label'])} символов)"
            )
        for token in tokens:
            if len(str(token["display"])) > MAX_DISPLAY_LENGTH:
                ui_warnings.append(
                    f"длинный пузырь: {token['display']} ({len(str(token['display']))} символов)"
                )
        if group["risk_state"] and group["risk_state"] != "clear":
            risk_warnings.append(f"{group['category_key']}: риск-статус {group['risk_state']}")

        groups.append(
            {
                "position": int(group["position"]),
                "category_key": group["category_key"],
                "label": group["label"],
                "rule": group["rule"],
                "intended_relation": group["relation_type"],
                "quartet_key": group["quartet_key"],
                "scores": {
                    "cohesion": group["cohesion"],
                    "familiarity": group["familiarity"],
                    "ambiguity_pressure": group["ambiguity"],
                },
                "tokens": tokens,
            }
        )

    competing = [
        {
            "display": row["display_text"],
            "home_category": row["home"],
            "also_fits": row["others"],
        }
        for row in conn.execute(
            """
            SELECT t.display_text AS display_text, home.category_key AS home,
                   GROUP_CONCAT(DISTINCT other.category_key) AS others
              FROM level_tokens t
              JOIN level_groups g   ON g.id = t.group_id
              JOIN categories home  ON home.id = g.category_id
              JOIN memberships m    ON m.word_id = t.word_id
              JOIN categories other ON other.id = m.category_id
             WHERE t.level_id = ?
               AND other.id <> home.id
               AND m.review_status IN ('approved', 'alternative', 'hard_only')
               AND m.semantic_status <> 'incorrect'
               AND (m.sense_id IS NULL OR t.sense_id IS NULL OR m.sense_id = t.sense_id)
             GROUP BY t.id ORDER BY t.slot
            """,
            (level_id,),
        )
    ]

    cooldowns = [
        {
            "kind": row["kind"],
            "item": row["item"],
            "last_used_in": row["level_key"],
        }
        for row in conn.execute(
            """
            SELECT 'word' AS kind, t.display_text AS item, prev.level_key AS level_key
              FROM level_tokens t
              JOIN level_tokens other ON other.word_id = t.word_id AND other.level_id <> t.level_id
              JOIN level_instances prev ON prev.id = other.level_id
             WHERE t.level_id = ? AND prev.status = 'accepted'
             GROUP BY t.id
            UNION ALL
            SELECT 'category', c.category_key, prev.level_key
              FROM level_groups g
              JOIN categories c ON c.id = g.category_id
              JOIN level_groups other ON other.category_id = g.category_id
                                     AND other.level_id <> g.level_id
              JOIN level_instances prev ON prev.id = other.level_id
             WHERE g.level_id = ? AND prev.status = 'accepted'
             GROUP BY g.id
            """,
            (level_id, level_id),
        )
    ]

    run = conn.execute(
        "SELECT * FROM level_solver_runs WHERE level_id = ? ORDER BY id DESC LIMIT 1",
        (level_id,),
    ).fetchone()

    return LevelPackage(
        level_key=level["level_key"],
        status=level["status"],
        tier=level["tier"],
        solution_count=level["solution_count"],
        difficulty_score=level["difficulty_score"],
        difficulty_components=json.loads(level["difficulty_components"] or "{}"),
        difficulty_explanation=level["difficulty_explanation"] or "",
        generator_version=level["generator_version"] or "",
        random_seed=level["random_seed"],
        content_hash=level["content_hash"],
        solver=(
            {
                "outcome": run["outcome"],
                "solution_count": run["solution_count"],
                "reason": run["reason"],
                "alternative_partition": run["alternative_partition"],
                "solver_version": run["solver_version"],
                "input_hash": run["input_hash"],
                "duration_ms": run["duration_ms"],
                "checked_at": run["checked_at"],
            }
            if run
            else {}
        ),
        groups=groups,
        competing=competing,
        cooldowns=cooldowns,
        ui_warnings=sorted(set(ui_warnings)),
        risk_warnings=sorted(set(risk_warnings)),
    )


# ------------------------------------------------------------------------- выгрузка


def write_json(path: Path, packages: list[LevelPackage]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([p.as_dict() for p in packages], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def write_markdown(path: Path, packages: list[LevelPackage]) -> Path:
    lines: list[str] = [
        "# Уровни на приёмку",
        "",
        "Оценивается уровень целиком: понятны ли категории, естественны ли именно",
        "эти четыре слова, единственно ли решение, есть ли доступный первый ход.",
        "Решения вносятся в `level_decisions.csv` и применяются командой",
        "`apply-level-decisions`.",
        "",
        f"Уровней в пакете: {len(packages)}",
        "",
    ]
    for package in packages:
        lines.append(f"## {package.level_key} — {package.status}")
        lines.append("")
        lines.append(
            f"Сложность {package.difficulty_score} ({package.difficulty_explanation}). "
            f"Разбиений: {package.solution_count}. "
            f"Solver: {package.solver.get('outcome', '?')} "
            f"за {package.solver.get('duration_ms', '?')} мс."
        )
        lines.append("")
        lines.append("| # | категория | правило | четыре слова |")
        lines.append("|---|---|---|---|")
        for group in package.groups:
            words = ", ".join(
                f"{t['display']}" + (f" ({t['sense_key']})" if t["sense_key"] else "")
                for t in group["tokens"]
            )
            lines.append(
                f"| {group['position']} | {group['label']} | {group['rule']} | {words} |"
            )
        lines.append("")
        if package.competing:
            lines.append("Слова, которые подходят и другим категориям базы:")
            for item in package.competing:
                lines.append(
                    f"- {item['display']} (дом {item['home_category']}) — также {item['also_fits']}"
                )
            lines.append("")
        if package.solver.get("alternative_partition"):
            lines.append(f"Альтернативное разбиение: {package.solver['alternative_partition']}")
            lines.append("")
        for title, items in (
            ("Повторы относительно принятых уровней", [
                f"{c['kind']} {c['item']} — был в {c['last_used_in']}" for c in package.cooldowns
            ]),
            ("Предупреждения по тексту", package.ui_warnings),
            ("Риски", package.risk_warnings),
        ):
            if items:
                lines.append(f"{title}:")
                lines.extend(f"- {item}" for item in items)
                lines.append("")
        lines.append(
            f"Версия генератора {package.generator_version}, seed {package.random_seed}, "
            f"хеш содержимого {package.content_hash[:12]}."
        )
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


DECISION_COLUMNS = [
    "level_key",
    "decision",
    "review_note",
    "rejection_reason_codes",
    "target_kind",
    "target_ref",
]


def write_decisions_template(path: Path, packages: list[LevelPackage]) -> Path:
    """Пустой бланк решений. Существующий файл не затирается: в нём чужая работа."""
    if path.exists():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_COLUMNS)
        writer.writeheader()
        for package in packages:
            writer.writerow({"level_key": package.level_key, "decision": ""})
    return path


# ------------------------------------------------------------------ применение решений


@dataclass
class DecisionReport:
    applied: int = 0
    skipped: int = 0
    feedback: list[str] = None  # type: ignore[assignment]
    errors: list[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        self.feedback = self.feedback or []
        self.errors = self.errors or []


def apply_decisions(conn: sqlite3.Connection, path: Path) -> DecisionReport:
    """Применяет решения по уровням и точечно возвращает причины в базу."""
    report = DecisionReport()
    now = utc_now()
    with path.open(encoding="utf-8", newline="") as handle:
        for number, row in enumerate(csv.DictReader(handle), start=2):
            level_key = (row.get("level_key") or "").strip()
            decision = (row.get("decision") or "").strip().lower()
            if not level_key or not decision:
                report.skipped += 1
                continue
            if decision not in DECISIONS:
                report.errors.append(
                    f"строка {number}: неизвестное решение {decision!r}, "
                    f"допустимы {', '.join(DECISIONS)}"
                )
                continue
            level = conn.execute(
                "SELECT id, status FROM level_instances WHERE level_key = ?", (level_key,)
            ).fetchone()
            if level is None:
                report.errors.append(f"строка {number}: уровень {level_key} не найден")
                continue

            status = STATUS_BY_DECISION[decision]
            version = 1 if status == "accepted" else None
            conn.execute(
                """
                UPDATE level_instances
                   SET status = ?, review_note = ?, accepted_version = ?, updated_at = ?
                 WHERE id = ?
                """,
                (status, (row.get("review_note") or "").strip() or None, version, now,
                 int(level["id"])),
            )
            decision_id = int(
                conn.execute(
                    """
                    INSERT INTO level_decisions (level_id, decision, review_note, applied_at)
                    VALUES (?, ?, ?, ?)
                    """,
                    (int(level["id"]), decision, (row.get("review_note") or "").strip() or None,
                     now),
                ).lastrowid
            )
            report.applied += 1

            codes = [
                code.strip()
                for code in (row.get("rejection_reason_codes") or "").split(";")
                if code.strip()
            ]
            for code in codes:
                if code not in REASON_TARGETS:
                    report.errors.append(f"строка {number}: неизвестный код причины {code!r}")
                    continue
                note = _propagate(
                    conn,
                    code=code,
                    target_kind=(row.get("target_kind") or "").strip() or None,
                    target_ref=(row.get("target_ref") or "").strip() or None,
                    level_id=int(level["id"]),
                )
                conn.execute(
                    """
                    INSERT INTO level_decision_reasons
                        (decision_id, reason_code, target_kind, target_ref, applied, note, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        decision_id,
                        code,
                        (row.get("target_kind") or "").strip() or None,
                        (row.get("target_ref") or "").strip() or None,
                        1 if note else 0,
                        note or "точечных изменений в базе не требуется",
                        now,
                    ),
                )
                if note:
                    report.feedback.append(f"{level_key}: {note}")

            _update_quartet_usage(conn, int(level["id"]), status)
    return report


def _propagate(
    conn: sqlite3.Connection,
    *,
    code: str,
    target_kind: str | None,
    target_ref: str | None,
    level_id: int,
) -> str | None:
    """Возвращает дефект на конкретный объект. None — если возвращать некуда."""
    expected = REASON_TARGETS[code]
    if expected is None:
        return None
    if not target_ref:
        return None
    kind = target_kind or expected

    if kind == "quartet":
        changed = conn.execute(
            "UPDATE quartets SET validation_state = 'disabled', last_rejection_reason = ?, "
            "updated_at = ? WHERE quartet_key = ?",
            (code, utc_now(), target_ref),
        ).rowcount
        return f"четвёрка {target_ref} выключена ({code})" if changed else None

    if kind == "category":
        changed = conn.execute(
            "UPDATE categories SET status = 'disabled', updated_at = ? WHERE category_key = ?",
            (utc_now(), target_ref),
        ).rowcount
        return f"категория {target_ref} выключена ({code})" if changed else None

    if kind == "membership":
        # Формат ссылки: слово>категория, например `rose>colors`.
        word, _, category_key = target_ref.partition(">")
        if not category_key:
            return None
        if code == "bad_sense":
            changed = conn.execute(
                """
                UPDATE memberships
                   SET validation_state = 'invalid',
                       validation_reasons = COALESCE(validation_reasons || ';', '') || ?,
                       updated_at = ?
                 WHERE word_id = (SELECT id FROM words WHERE normalized = ?)
                   AND category_id = (SELECT id FROM categories WHERE category_key = ?)
                """,
                (code, utc_now(), word.strip().lower(), category_key.strip()),
            ).rowcount
            return f"связь {target_ref} помечена invalid ({code})" if changed else None
        changed = conn.execute(
            """
            UPDATE memberships
               SET review_status = 'rejected', review_comment = ?, updated_at = ?
             WHERE word_id = (SELECT id FROM words WHERE normalized = ?)
               AND category_id = (SELECT id FROM categories WHERE category_key = ?)
            """,
            (f"отклонено по уровню: {code}", utc_now(), word.strip().lower(),
             category_key.strip()),
        ).rowcount
        return f"связь {target_ref} отклонена ({code})" if changed else None

    return None


def _update_quartet_usage(conn: sqlite3.Connection, level_id: int, status: str) -> None:
    """Счётчики использования четвёрок — агрегат из истории уровней, не ручное поле."""
    column = (
        "accepted_level_use_count"
        if status == "accepted"
        else "rejected_level_use_count"
        if status == "rejected"
        else None
    )
    if column is None:
        return
    conn.execute(
        f"""
        UPDATE quartets SET {column} = {column} + 1, updated_at = ?
         WHERE id IN (SELECT quartet_id FROM level_groups
                       WHERE level_id = ? AND quartet_id IS NOT NULL)
        """,
        (utc_now(), level_id),
    )
