"""Отчёт покрытия референса и обязательный Reference Reproduction Gate.

Старый замер отвечал на три вопроса: есть ли слово, есть ли концепт, есть ли
связь. Этого мало и в одном месте прямо неверно.

Неверно вот что. Для inferred-категории (71 из 95 на первых десяти уровнях)
сравнение по точному имени измеряет совпадение базы **с нашей же догадкой**, а
не с оригиналом. Имя такой категории не ground truth; ground truth — четвёрка.
Поэтому проверка разная:

    observed label   имя прочитано с пузыря -> требуем совпадения надписи
    inferred label   имя наше -> требуем точную четвёрку + верное правило
                                  + допустимую надпись, текст имени не блокирует

Метрики считаются отдельно и не складываются в одно число: «слова есть на 98%»
и «уровень не собирается» — это одновременно правда, и усреднять их нельзя.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict, dataclass, field
from pathlib import Path

from . import reference_import
from .reference_fixtures import FixtureLevel, ReferenceFixtures, normalize_name, normalize_token
from .reference_resolve import PLAYABLE_STATUSES, load_index

COVERAGE_VERSION = "reference-coverage/2.0"

# Определение готовности для уровней 1-10 (раздел 6 задания).
GATE_MAX_LEVEL = 10


@dataclass
class Metric:
    """Одна проверка: сколько из скольких и что именно не сошлось."""

    name: str
    done: int = 0
    total: int = 0
    misses: list[str] = field(default_factory=list)

    def add(self, ok: bool, miss: str = "") -> None:
        self.total += 1
        if ok:
            self.done += 1
        elif miss:
            self.misses.append(miss)

    @property
    def ratio(self) -> float:
        return round(self.done / self.total, 4) if self.total else 1.0

    @property
    def complete(self) -> bool:
        return self.done == self.total

    def as_dict(self, *, miss_limit: int = 40) -> dict:
        return {
            "done": self.done,
            "total": self.total,
            "ratio": self.ratio,
            "complete": self.complete,
            "misses": self.misses[:miss_limit],
            "misses_total": len(self.misses),
        }


@dataclass
class LevelReport:
    level: int
    completeness: str
    groups_expected: int
    groups_recorded: int
    reconstructable: bool
    diff: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "level": self.level,
            "completeness": self.completeness,
            "groups_expected": self.groups_expected,
            "groups_recorded": self.groups_recorded,
            "reconstructable": self.reconstructable,
            "diff": self.diff[:20],
            "diff_total": len(self.diff),
        }


@dataclass
class CoverageReport:
    version: str
    max_level: int | None
    metrics: dict[str, Metric]
    levels: list[LevelReport]
    totals: dict[str, int]

    def metric(self, name: str) -> Metric:
        return self.metrics[name]

    def as_dict(self) -> dict:
        return {
            "version": self.version,
            "max_level": self.max_level,
            "fixture_totals": self.totals,
            "metrics": {name: metric.as_dict() for name, metric in self.metrics.items()},
            "levels": [level.as_dict() for level in self.levels],
            "summary": self.summary(),
        }

    def summary(self) -> dict:
        return {
            "reference_word_slot_coverage": self.metrics["word_slot"].ratio,
            "reference_sense_coverage": self.metrics["sense_slot"].ratio,
            "reference_group_rule_coverage": self.metrics["group_rule"].ratio,
            "reference_membership_coverage": self.metrics["slot_membership"].ratio,
            "reference_exact_quartet_coverage": self.metrics["exact_quartet"].ratio,
            "reference_meta_edge_coverage": self.metrics["meta_dependency"].ratio,
            "reference_token_form_coverage": self.metrics["form_match"].ratio,
            "fully_reconstructable_reference_levels": sum(
                1 for level in self.levels if level.reconstructable
            ),
            "observed_label_match": self.metrics["observed_label"].ratio,
            "inferred_label_resolution": self.metrics["inferred_label"].ratio,
            "normalized_export_diff": sum(len(level.diff) for level in self.levels),
        }


METRIC_ORDER = (
    ("word_slot", "слот -> слово в базе"),
    ("sense_slot", "слот -> однозначное значение"),
    ("group_rule", "группа -> внутреннее правило с этой четвёркой"),
    ("slot_membership", "слот -> связь с правилом группы"),
    ("exact_quartet", "точная авторская четвёрка в базе"),
    ("observed_label", "прочитанная надпись совпадает"),
    ("inferred_label", "наша формулировка разрешается правилом"),
    ("meta_dependency", "мета-зависимость записана"),
    ("form_match", "форма токена записана"),
    ("level_reconstructable", "уровень воспроизводится целиком"),
)


def measure(
    conn: sqlite3.Connection,
    fixtures: ReferenceFixtures,
    *,
    max_level: int | None = None,
    overrides: dict | None = None,
) -> CoverageReport:
    """Полный отчёт. Ничего не пишет в базу."""
    from .reference_fixtures import totals as fixture_totals

    levels = fixtures.upto(max_level)
    index = load_index(conn, include_reference=True)
    _, resolutions = reference_import.resolve_all(
        conn, fixtures, max_level=max_level, overrides=overrides,
        index=load_index(conn),
    )
    labels_by_rule = _labels_by_rule(conn)
    quartets_by_signature = _quartets_by_signature(conn)

    metrics = {name: Metric(name=title) for name, title in METRIC_ORDER}
    level_reports: list[LevelReport] = []

    for level in levels:
        for group in level.groups:
            resolution = resolutions[(level.number, group.index)]
            rule_key = resolution.target_rule_key
            pool = index.pools.get(rule_key, set())
            tokens = [slot.normalized for slot in group.slots]
            where = f"L{level.number} «{group.name}»"

            for slot in group.slots:
                metrics["word_slot"].add(
                    slot.normalized in index.words,
                    f"{where}: слова «{slot.text}» нет в базе",
                )
                sense_count = index.sense_count(slot.text)
                resolved_sense = index.membership_senses.get((rule_key, slot.normalized))
                metrics["sense_slot"].add(
                    sense_count <= 1 or bool(resolved_sense),
                    f"{where}: «{slot.text}» многозначно, значение для правила не выбрано",
                )
                metrics["slot_membership"].add(
                    slot.normalized in pool,
                    f"{where}: нет связи «{slot.text}» -> {rule_key}",
                )
                expected_form = (slot.token_kind, slot.token_form, tuple(slot.pieces))
                metrics["form_match"].add(
                    _form_recorded(conn, level.number, group.index, slot, expected_form),
                    f"{where}: форма токена «{slot.text}» не записана",
                )

            all_present = all(token in pool for token in tokens)
            metrics["group_rule"].add(
                all_present,
                f"{where}: правило {rule_key} не держит всю четвёрку "
                f"({len([t for t in tokens if t in pool])}/4)",
            )

            signature = group.quartet_signature
            variants = quartets_by_signature.get(signature, [])
            metrics["exact_quartet"].add(
                any(item["category_key"] == rule_key for item in variants),
                f"{where}: точной четвёрки в правиле {rule_key} нет",
            )

            admissible = labels_by_rule.get(rule_key, set())
            label_key = normalize_name(group.name)
            if group.observed_label:
                metrics["observed_label"].add(
                    label_key in admissible,
                    f"{where}: прочитанная надпись не значится у правила {rule_key}",
                )
            else:
                metrics["inferred_label"].add(
                    all_present
                    and any(item["category_key"] == rule_key for item in variants)
                    and bool(admissible),
                    f"{where}: наша формулировка не разрешается "
                    f"(четвёрка/правило/надпись у {rule_key})",
                )

        for link in level.meta_links:
            metrics["meta_dependency"].add(
                _meta_recorded(conn, level.number, link),
                f"L{level.number}: мета-ссылка «{link.token}» "
                f"({link.source_group} -> {link.target_group}) не записана",
            )

        diff = reference_import.diff_level(conn, level)
        reconstructable = not diff
        metrics["level_reconstructable"].add(
            reconstructable, f"L{level.number}: расхождений {len(diff)}"
        )
        level_reports.append(
            LevelReport(
                level=level.number,
                completeness=level.completeness,
                groups_expected=level.groups_expected,
                groups_recorded=len(level.groups),
                reconstructable=reconstructable,
                diff=diff,
            )
        )

    return CoverageReport(
        version=COVERAGE_VERSION,
        max_level=max_level,
        metrics=metrics,
        levels=level_reports,
        totals=fixture_totals(levels),
    )


def _labels_by_rule(conn: sqlite3.Connection) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for row in conn.execute(
        """
        SELECT c.category_key AS category_key, l.label_key AS label_key
          FROM group_rule_labels g
          JOIN categories c      ON c.id = g.category_id
          JOIN category_labels l ON l.id = g.label_id
        """
    ):
        out.setdefault(row["category_key"], set()).add(row["label_key"])
    return out


def _quartets_by_signature(conn: sqlite3.Connection) -> dict[tuple[str, ...], list[dict]]:
    rows = conn.execute(
        """
        SELECT q.quartet_key AS quartet_key, c.category_key AS category_key,
               w.normalized AS word
          FROM quartets q
          JOIN categories c     ON c.id = q.category_id
          JOIN quartet_words qw ON qw.quartet_id = q.id
          JOIN words w          ON w.id = qw.word_id
         ORDER BY q.quartet_key, qw.slot
        """
    )
    grouped: dict[str, dict] = {}
    for row in rows:
        entry = grouped.setdefault(
            row["quartet_key"],
            {"category_key": row["category_key"], "words": []},
        )
        entry["words"].append(row["word"])
    out: dict[tuple[str, ...], list[dict]] = {}
    for quartet_key, entry in grouped.items():
        signature = tuple(sorted(entry["words"]))
        out.setdefault(signature, []).append(
            {"quartet_key": quartet_key, "category_key": entry["category_key"]}
        )
    return out


def _form_recorded(
    conn: sqlite3.Connection, level_number: int, group_index: int, slot, expected
) -> bool:
    row = conn.execute(
        """
        SELECT t.token_kind, t.token_form, t.pieces, t.observability
          FROM level_tokens t
          JOIN level_groups g ON g.id = t.group_id
          JOIN level_instances i ON i.id = t.level_id
         WHERE i.level_key = ? AND g.position = ? AND t.slot = ?
        """,
        (f"REF{level_number:03d}", group_index, slot.position),
    ).fetchone()
    if row is None:
        return False
    pieces = tuple(json.loads(row["pieces"])) if row["pieces"] else ()
    return (
        row["token_kind"] == expected[0]
        and row["token_form"] == expected[1]
        and pieces == expected[2]
        and row["observability"] == slot.observability
    )


def _meta_recorded(conn: sqlite3.Connection, level_number: int, link) -> bool:
    row = conn.execute(
        """
        SELECT 1
          FROM level_dependencies d
          JOIN level_instances i ON i.id = d.level_id
          JOIN level_groups src  ON src.id = d.from_group_id
          JOIN level_tokens t    ON t.id = d.to_token_id
          JOIN level_groups tgt  ON tgt.id = t.group_id
         WHERE i.level_key = ?
           AND LOWER(t.display_text) = LOWER(?)
           AND LOWER(src.reference_name) = LOWER(?)
           AND LOWER(tgt.reference_name) = LOWER(?)
        """,
        (f"REF{level_number:03d}", link.token, link.source_group, link.target_group),
    ).fetchone()
    return row is not None


# ------------------------------------------------------------------------- gate


@dataclass
class GateResult:
    passed: bool
    checks: list[tuple[str, bool, str]]
    report: CoverageReport

    def failures(self) -> list[tuple[str, bool, str]]:
        return [item for item in self.checks if not item[1]]


def gate(
    conn: sqlite3.Connection,
    fixtures: ReferenceFixtures,
    *,
    max_level: int = GATE_MAX_LEVEL,
    overrides: dict | None = None,
) -> GateResult:
    """Definition of Done для уровней 1-10. Ниже порога генерация запрещена."""
    report = measure(conn, fixtures, max_level=max_level, overrides=overrides)
    totals = report.totals
    checks: list[tuple[str, bool, str]] = []

    def require(title: str, metric_name: str) -> None:
        metric = report.metric(metric_name)
        checks.append(
            (title, metric.complete, f"{metric.done}/{metric.total}")
        )

    require("слоты слов", "word_slot")
    require("значения слов", "sense_slot")
    require("правила группировки", "group_rule")
    require("связи слот -> правило", "slot_membership")
    require("точные четвёрки", "exact_quartet")
    require("прочитанные надписи", "observed_label")
    require("наши формулировки разрешаются", "inferred_label")
    require("мета-зависимости", "meta_dependency")
    require("формы токенов", "form_match")
    require("уровни воспроизводятся", "level_reconstructable")

    diff_total = sum(len(level.diff) for level in report.levels)
    checks.append(("нулевой diff экспорта", diff_total == 0, str(diff_total)))

    # Отдельная проверка: частично записанный уровень не объявляется полным.
    honest = all(
        level.groups_recorded == level.groups_expected or not level.reconstructable
        or level.completeness == "partial"
        for level in report.levels
    )
    checks.append(
        ("частичная запись не выдаётся за полную", honest,
         ", ".join(
             f"L{level.level}:{level.groups_recorded}/{level.groups_expected}"
             for level in report.levels
             if level.groups_recorded != level.groups_expected
         ) or "нет частичных")
    )
    checks.append(
        ("контрольные числа записи", totals["slots"] > 0,
         f"групп {totals['groups_recorded']}, слотов {totals['slots']}, "
         f"мета {totals['meta_links']}, прочитанных надписей {totals['observed_labels']}")
    )

    return GateResult(
        passed=all(ok for _title, ok, _detail in checks), checks=checks, report=report
    )


class ReferenceGateError(RuntimeError):
    """Reference gate не пройден: массовая генерация запрещена."""


def require_gate(
    conn: sqlite3.Connection,
    *,
    fixtures: ReferenceFixtures | None = None,
    max_level: int = GATE_MAX_LEVEL,
    overrides: dict | None = None,
) -> GateResult:
    """Вызывается перед любой массовой генерацией. Не прошёл — исключение."""
    from . import reference_fixtures as fixtures_mod

    fixtures = fixtures or fixtures_mod.load()
    if overrides is None:
        overrides = reference_import.load_overrides(
            reference_import.default_overrides_path()
        )
    result = gate(conn, fixtures, max_level=max_level, overrides=overrides)
    if not result.passed:
        broken = "; ".join(
            f"{title} ({detail})" for title, ok, detail in result.checks if not ok
        )
        raise ReferenceGateError(
            "Reference Reproduction Gate не пройден, генерация нового контента "
            f"запрещена: {broken}. "
            "Пока система не может повторить то, что мы точно видели, её "
            "способность создавать «лучше» не подтверждена."
        )
    return result


def write_report(report: CoverageReport, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report.as_dict(), ensure_ascii=False, indent=2, sort_keys=False)
        + "\n",
        encoding="utf-8",
    )
    return path


def baseline_snapshot(report: CoverageReport) -> dict:
    """Именно те восемь чисел, которые требует раздел 1 задания."""
    summary = report.summary()
    return {
        "version": report.version,
        "max_level": report.max_level,
        **{key: summary[key] for key in (
            "reference_word_slot_coverage",
            "reference_sense_coverage",
            "reference_group_rule_coverage",
            "reference_membership_coverage",
            "reference_exact_quartet_coverage",
            "reference_meta_edge_coverage",
            "reference_token_form_coverage",
            "fully_reconstructable_reference_levels",
        )},
        "counts": {
            name: {"done": metric.done, "total": metric.total}
            for name, metric in report.metrics.items()
        },
    }


__all__ = [
    "COVERAGE_VERSION",
    "CoverageReport",
    "GateResult",
    "Metric",
    "ReferenceGateError",
    "asdict",
    "baseline_snapshot",
    "gate",
    "measure",
    "require_gate",
    "write_report",
]
