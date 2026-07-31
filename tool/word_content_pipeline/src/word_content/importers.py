"""Импорт JSONL/CSV в SQLite. Ошибка одной строки не останавливает импорт."""

from __future__ import annotations

import csv
import json
import sqlite3
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from .db import transaction
from .models import CategoryInput, MembershipCandidateInput, ReviewDecisionInput
from .repositories import (
    find_membership,
    record_import_run,
    set_review_status,
    upsert_category,
    upsert_membership,
    upsert_sense,
    upsert_word,
)
from .sense_map import SenseMap, default_sense_map
from .validators import (
    ContentFilter,
    ValidationIssue,
    familiarity_gate,
    require_category,
    resolve_sense_key,
    word_familiarity,
)

REVIEW_CSV_COLUMNS = [
    "membership_id",
    "word",
    "normalized",
    "familiarity",
    "sense_key",
    "sense_definition",
    "category_key",
    "category_label",
    "category_rule",
    "relation_type",
    "reason",
    "fit_score",
    "obviousness_score",
    "source",
    "current_status",
    "decision",
    "review_comment",
]


@dataclass
class ImportReport:
    """Итог одного импорта."""

    import_type: str
    source_file: str
    total: int = 0
    inserted: int = 0
    updated: int = 0
    rejected: int = 0
    errors: list[dict[str, Any]] = field(default_factory=list)

    def add_error(self, line_no: int | str, message: str, payload: str | None = None) -> None:
        self.rejected += 1
        self.errors.append(
            {"line": line_no, "error": message, "payload": (payload or "")[:400]}
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "total": self.total,
            "inserted": self.inserted,
            "updated": self.updated,
            "rejected": self.rejected,
            "errors": self.errors,
        }


def iter_jsonl(path: Path) -> Iterator[tuple[int, str]]:
    """Отдаёт (номер строки, сырой текст) для непустых строк файла."""
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if stripped and not stripped.startswith("//"):
                yield line_no, stripped


def _format_validation_error(exc: ValidationError) -> str:
    parts = []
    for err in exc.errors():
        loc = ".".join(str(x) for x in err["loc"]) or "-"
        parts.append(f"{loc}: {err['msg']}")
    return "; ".join(parts)


# ------------------------------------------------------------------------- categories


def import_categories(conn: sqlite3.Connection, path: Path) -> ImportReport:
    report = ImportReport(import_type="categories", source_file=str(path))
    with transaction(conn):
        for line_no, raw in iter_jsonl(path):
            report.total += 1
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as exc:
                report.add_error(line_no, f"Некорректный JSON: {exc}", raw)
                continue
            try:
                item = CategoryInput.model_validate(payload)
            except ValidationError as exc:
                report.add_error(line_no, _format_validation_error(exc), raw)
                continue

            try:
                result = upsert_category(conn, item)
            except sqlite3.Error as exc:
                report.add_error(line_no, f"Ошибка SQLite: {exc}", raw)
                continue
            if result == "inserted":
                report.inserted += 1
            else:
                report.updated += 1

        record_import_run(
            conn,
            import_type=report.import_type,
            source_file=report.source_file,
            total=report.total,
            inserted=report.inserted,
            updated=report.updated,
            rejected=report.rejected,
            errors=report.errors,
        )
    return report


# ------------------------------------------------------------------------ memberships


def sense_from_map(
    conn: sqlite3.Connection,
    *,
    word_id: int,
    word: str,
    category_key: str,
    part_of_speech: str | None,
    sense_map: SenseMap | None,
) -> int | None:
    """Значение связи из карты проекта: сначала определение из карты, иначе уже
    известное базе значение с тем же ключом (карта может только назначать)."""
    mapping = (sense_map or default_sense_map()).lookup(word, category_key)
    if mapping is None:
        return None
    definition = mapping.definition
    if definition is None:
        row = conn.execute(
            "SELECT id FROM word_senses WHERE word_id = ? AND sense_key = ?",
            (word_id, mapping.sense_key),
        ).fetchone()
        return int(row["id"]) if row else None
    return upsert_sense(
        conn,
        word_id=word_id,
        sense_key=mapping.sense_key,
        definition=definition,
        part_of_speech=mapping.part_of_speech or part_of_speech,
        display_text=mapping.display_text,
        is_proper_noun=mapping.is_proper_noun,
    )


# Типы связей, которые работают с написанием слова, а не с его значением.
SURFACE_RELATIONS = ("phrase_before", "phrase_after", "wordplay")


def derive_sense_mode(relation_type: str, sense_id: int | None) -> str:
    """Как связь обращается со словом, если источник не сказал этого явно.

    `starboard` не происходит от звезды — там участвует написание
    (`surface_form`). А `moonlight` именно от луны — там значение работает
    и должно быть указано (`compound`). Разница видна по тому, нашлось ли
    для связи значение.
    """
    if relation_type not in SURFACE_RELATIONS:
        return "lexical"
    return "compound" if sense_id is not None else "surface_form"


def apply_membership(
    conn: sqlite3.Connection,
    item: MembershipCandidateInput,
    *,
    overwrite_review_status: bool = False,
    content_filter: ContentFilter | None = None,
    sense_map: SenseMap | None = None,
) -> str:
    """Создаёт/обновляет слово, значение и связь. Бросает ValidationIssue при проблеме данных."""
    category = require_category(conn, item.category_key)

    filters = content_filter or ContentFilter()
    filters.check(item.word)

    familiarity_score = filters.score(item.word)
    word_id = upsert_word(
        conn,
        text=item.word,
        language=item.language,
        part_of_speech=item.part_of_speech,
        is_proper_noun=item.is_proper_noun,
        familiarity_score=familiarity_score,
    )

    # Гейт частотности: слово без familiarity_score не может прийти в базу
    # играбельным, даже если в файле стоит approved (P0 аудита).
    review_status, downgrade = familiarity_gate(
        item.review_status, word_familiarity(conn, word_id)
    )
    risk_flags = list(item.risk_flags)
    if downgrade and "no_familiarity" not in risk_flags:
        risk_flags.append("no_familiarity")

    sense_id: int | None = None
    if item.sense_key and item.sense_definition:
        sense_key = resolve_sense_key(conn, item) or item.sense_key
        sense_id = upsert_sense(
            conn,
            word_id=word_id,
            sense_key=sense_key,
            definition=item.sense_definition,
            part_of_speech=item.part_of_speech,
        )
    else:
        # Источник значение не принёс — берём объявленное в карте проекта.
        # Иначе многозначное слово заезжает в категорию без смысла: seed от этого
        # защищён на этапе build_seed, а импорт прогонов был не защищён вовсе.
        sense_id = sense_from_map(
            conn, word_id=word_id, word=item.word, category_key=item.category_key,
            part_of_speech=item.part_of_speech, sense_map=sense_map,
        )

    return upsert_membership(
        conn,
        word_id=word_id,
        sense_id=sense_id,
        sense_mode=item.sense_mode or derive_sense_mode(item.relation_type, sense_id),
        category_id=int(category["id"]),
        relation_type=item.relation_type,
        reason=item.reason,
        fit_score=item.fit_score,
        obviousness_score=item.obviousness_score,
        source=item.source,
        review_status=review_status,
        semantic_status=item.semantic_status,
        gameplay_difficulty=item.gameplay_difficulty,
        risk_flags=risk_flags,
        review_comment=downgrade,
        overwrite_review_status=overwrite_review_status,
    )


def import_membership_records(
    conn: sqlite3.Connection,
    records: Iterable[tuple[int | str, dict[str, Any] | str]],
    *,
    source_file: str,
    overwrite_review_status: bool = False,
    import_type: str = "memberships",
    content_filter: ContentFilter | None = None,
    sense_map: SenseMap | None = None,
) -> ImportReport:
    """Общий импорт связей: принимает как готовые dict, так и сырые JSON-строки."""
    report = ImportReport(import_type=import_type, source_file=source_file)
    with transaction(conn):
        for line_no, entry in records:
            report.total += 1
            if isinstance(entry, str):
                try:
                    payload = json.loads(entry)
                except json.JSONDecodeError as exc:
                    report.add_error(line_no, f"Некорректный JSON: {exc}", entry)
                    continue
            else:
                payload = entry

            raw_repr = json.dumps(payload, ensure_ascii=False)
            try:
                item = MembershipCandidateInput.model_validate(payload)
            except ValidationError as exc:
                report.add_error(line_no, _format_validation_error(exc), raw_repr)
                continue

            try:
                result = apply_membership(
                    conn,
                    item,
                    overwrite_review_status=overwrite_review_status,
                    content_filter=content_filter,
                    sense_map=sense_map,
                )
            except ValidationIssue as exc:
                report.add_error(line_no, str(exc), raw_repr)
                continue
            except sqlite3.Error as exc:
                report.add_error(line_no, f"Ошибка SQLite: {exc}", raw_repr)
                continue

            if result == "inserted":
                report.inserted += 1
            else:
                report.updated += 1

        record_import_run(
            conn,
            import_type=report.import_type,
            source_file=report.source_file,
            total=report.total,
            inserted=report.inserted,
            updated=report.updated,
            rejected=report.rejected,
            errors=report.errors,
        )
    return report


def import_memberships(
    conn: sqlite3.Connection,
    path: Path,
    *,
    overwrite_review_status: bool = False,
    content_filter: ContentFilter | None = None,
    sense_map: SenseMap | None = None,
) -> ImportReport:
    return import_membership_records(
        conn,
        iter_jsonl(path),
        source_file=str(path),
        overwrite_review_status=overwrite_review_status,
        content_filter=content_filter,
        sense_map=sense_map,
    )


# ----------------------------------------------------------------------------- review


def _resolve_membership_id(
    conn: sqlite3.Connection, membership_id: int | None, row: dict[str, Any]
) -> int | None:
    """Проверяет, что id указывает на ту же связь; иначе ищет по слову и категории.

    Нужно потому, что membership_id зависит от порядка вставки: после пересборки
    базы из изменившегося JSONL старые id могут указывать на другие связи.
    """
    normalized = (row.get("normalized") or "").strip().lower()
    category_key = (row.get("category_key") or "").strip()
    if not normalized or not category_key:
        return membership_id  # старый формат CSV — доверяем id

    sense_key = (row.get("sense_key") or "").strip() or None
    if membership_id is None:
        found = find_membership(conn, normalized, category_key, sense_key)
        return int(found["id"]) if found else None

    current = conn.execute(
        """
        SELECT w.normalized AS normalized, c.category_key AS category_key
          FROM memberships m
          JOIN words w ON w.id = m.word_id
          JOIN categories c ON c.id = m.category_id
         WHERE m.id = ?
        """,
        (membership_id,),
    ).fetchone()
    if current and current["normalized"] == normalized and current["category_key"] == category_key:
        return membership_id

    found = find_membership(conn, normalized, category_key, sense_key)
    return int(found["id"]) if found else None


def import_review_csv(conn: sqlite3.Connection, path: Path) -> ImportReport:
    """Читает CSV решений reviewer и обновляет review_status/review_comment."""
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    report = ImportReport(import_type="review", source_file=str(path))
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    with transaction(conn):
        for line_no, row in enumerate(rows, start=2):  # строка 1 — заголовок
            decision = (row.get("decision") or "").strip()
            if not decision:
                continue  # пустое решение = reviewer пропустил строку
            report.total += 1
            try:
                item = ReviewDecisionInput.model_validate(
                    {
                        "membership_id": row.get("membership_id"),
                        "decision": decision,
                        "review_comment": row.get("review_comment"),
                        "semantic_status": row.get("semantic_status"),
                        "gameplay_difficulty": row.get("gameplay_difficulty"),
                    }
                )
            except ValidationError as exc:
                report.add_error(line_no, _format_validation_error(exc), json.dumps(row))
                continue

            membership_id = _resolve_membership_id(conn, item.membership_id, row)
            if membership_id is not None and set_review_status(
                conn,
                membership_id,
                item.decision,
                item.review_comment,
                semantic_status=item.semantic_status,
                gameplay_difficulty=item.gameplay_difficulty,
            ):
                report.updated += 1
            else:
                report.add_error(
                    line_no,
                    f"membership_id={item.membership_id} не найден в базе",
                    json.dumps(row),
                )

        record_import_run(
            conn,
            import_type=report.import_type,
            source_file=report.source_file,
            total=report.total,
            inserted=report.inserted,
            updated=report.updated,
            rejected=report.rejected,
            errors=report.errors,
        )
    return report
