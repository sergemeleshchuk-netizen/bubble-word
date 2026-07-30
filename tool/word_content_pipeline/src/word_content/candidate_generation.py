"""AI-проходы: категория -> слова, слово -> категории, критический review кандидатов.

Модель только предлагает. Всё, что она вернула, попадает в базу со статусом candidate.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from typing import Any

from pydantic import ValidationError

from .db import transaction
from .llm.base import LLMError, LLMProvider, call_with_retries
from .llm.prompts import (
    PROMPT_VERSION,
    SYSTEM_PROMPT,
    build_adversarial_review_prompt,
    build_expand_category_prompt,
    build_expand_words_prompt,
)
from .llm.schemas import (
    AdversarialReviewOutput,
    CategoryExpansionOutput,
    ReverseExpansionOutput,
    parse_json_response,
)
from .normalization import NormalizationError, normalize_sense_key, normalize_word
from .repositories import (
    category_keys,
    get_word,
    list_categories,
    list_senses,
    memberships_for_category,
    memberships_for_word,
    record_generation_run,
)
from .validators import ValidationIssue, require_category

SOURCE_CATEGORY_EXPANSION = "ai_category_expansion"
SOURCE_REVERSE_EXPANSION = "ai_reverse_expansion"


@dataclass
class GenerationResult:
    """Итог AI-прохода: готовые к импорту записи + что и почему отброшено."""

    records: list[dict[str, Any]] = field(default_factory=list)
    skipped: list[dict[str, Any]] = field(default_factory=list)
    run_ids: list[int] = field(default_factory=list)
    batches_ok: int = 0
    batches_failed: int = 0
    hints: dict[str, list[str]] = field(default_factory=dict)

    def skip(self, reason: str, payload: Any) -> None:
        self.skipped.append({"reason": reason, "payload": payload})


def _identity(record: dict[str, Any]) -> tuple[str, str, str]:
    """Ключ дедупликации: нормализованное слово + категория + значение."""
    return (
        normalize_word(record["word"]),
        record["category_key"],
        record.get("sense_key") or "",
    )


def _existing_identities_for_category(
    conn: sqlite3.Connection, category_key: str
) -> set[tuple[str, str, str]]:
    return {
        (row["normalized"], row["category_key"], row["sense_key"] or "")
        for row in memberships_for_category(conn, category_key)
    }


def _existing_identities_for_word(
    conn: sqlite3.Connection, word: str
) -> set[tuple[str, str, str]]:
    return {
        (row["normalized"], row["category_key"], row["sense_key"] or "")
        for row in memberships_for_word(conn, word)
    }


def _call_model(
    provider: LLMProvider, prompt: str, *, max_retries: int, sleep: Any = None
) -> str:
    kwargs: dict[str, Any] = {"max_retries": max_retries}
    if sleep is not None:
        kwargs["sleep"] = sleep
    response = call_with_retries(
        lambda: provider.complete_json(prompt, system=SYSTEM_PROMPT), **kwargs
    )
    return response.text


# ------------------------------------------------------------------ A. category -> words


def expand_category(
    conn: sqlite3.Connection,
    provider: LLMProvider,
    *,
    category_key: str,
    count: int = 30,
    batch_size: int = 15,
    max_retries: int = 2,
    sleep: Any = None,
) -> GenerationResult:
    """Проход A: просит модель предложить слова для одной категории."""
    category = require_category(conn, category_key)
    known_keys = category_keys(conn)
    catalog_keys = sorted(known_keys)

    existing = _existing_identities_for_category(conn, category_key)
    existing_words = sorted({identity[0] for identity in existing})

    result = GenerationResult()
    seen: set[tuple[str, str, str]] = set(existing)
    remaining = count

    while remaining > 0:
        take = min(batch_size, remaining)
        remaining -= take
        prompt = build_expand_category_prompt(
            category=dict(category),
            existing_words=sorted({*existing_words, *(r["word"] for r in result.records)}),
            available_category_keys=catalog_keys,
            count=take,
        )
        raw = ""
        try:
            raw = _call_model(provider, prompt, max_retries=max_retries, sleep=sleep)
            payload = parse_json_response(raw)
            parsed = CategoryExpansionOutput.model_validate(payload)
        except (LLMError, ValueError, ValidationError) as exc:
            result.batches_failed += 1
            result.skip("batch_failed", str(exc))
            _log_run(
                conn,
                generation_type="category_expansion",
                provider=provider,
                input_json={"category_key": category_key, "count": take},
                raw=raw,
                parsed=None,
                status="error",
                error=str(exc)[:2000],
                result=result,
            )
            continue

        accepted: list[dict[str, Any]] = []
        for candidate in parsed.candidates:
            record, problem = _candidate_to_record(
                candidate=candidate,
                category_key=category_key,
                default_relation=str(category["relation_type"]),
                known_keys=known_keys,
            )
            if problem:
                result.skip(problem, candidate.model_dump())
                continue
            identity = _identity(record)
            if identity in seen:
                result.skip("duplicate", record)
                continue
            seen.add(identity)
            accepted.append(record)
            if candidate.possible_other_category_keys:
                hints = [k for k in candidate.possible_other_category_keys if k in known_keys]
                if hints:
                    result.hints.setdefault(record["word"], []).extend(hints)

        result.records.extend(accepted)
        result.batches_ok += 1
        _log_run(
            conn,
            generation_type="category_expansion",
            provider=provider,
            input_json={"category_key": category_key, "count": take},
            raw=raw,
            parsed=[r for r in accepted],
            status="ok",
            error=None,
            result=result,
        )

    return result


def _candidate_to_record(
    *,
    candidate: Any,
    category_key: str,
    default_relation: str,
    known_keys: set[str],
) -> tuple[dict[str, Any], str | None]:
    """Приводит кандидата модели к строке membership_candidates.jsonl."""
    try:
        normalize_word(candidate.word)
    except NormalizationError as exc:
        return {}, f"bad_word: {exc}"

    sense_key = candidate.sense_key
    sense_definition = candidate.sense_definition
    if bool(sense_key) != bool(sense_definition):
        return {}, "incomplete_sense"
    if sense_key:
        sense_key = normalize_sense_key(sense_key)

    record = {
        "word": candidate.word.strip(),
        "language": "en",
        "part_of_speech": candidate.part_of_speech,
        "is_proper_noun": bool(candidate.is_proper_noun),
        "sense_key": sense_key,
        "sense_definition": sense_definition,
        "category_key": category_key,
        "relation_type": candidate.relation_type or default_relation,
        "reason": candidate.reason.strip(),
        "fit_score": candidate.fit_score,
        "obviousness_score": candidate.obviousness_score,
        "source": SOURCE_CATEGORY_EXPANSION,
        "review_status": "candidate",  # AI никогда не выставляет approved
        "risk_flags": candidate.risk_flags,
    }
    if category_key not in known_keys:
        return {}, "unknown_category_key"
    return record, None


# ------------------------------------------------------------------ B. word -> categories


def expand_words(
    conn: sqlite3.Connection,
    provider: LLMProvider,
    *,
    words: list[str],
    batch_size: int = 8,
    catalog_chunk: int = 60,
    max_retries: int = 2,
    sleep: Any = None,
) -> GenerationResult:
    """Проход B: ищет для слов дополнительные категории из существующего каталога."""
    known_keys = category_keys(conn)
    catalog = [
        {
            "category_key": row["category_key"],
            "label": row["label"],
            "rule": row["rule"],
            "relation_type": row["relation_type"],
            "theme": row["theme"],
        }
        for row in list_categories(conn)
    ]
    relation_by_key = {item["category_key"]: item["relation_type"] for item in catalog}

    result = GenerationResult()
    seen: set[tuple[str, str, str]] = set()
    word_context: list[dict[str, Any]] = []

    for word in words:
        try:
            normalized = normalize_word(word)
        except NormalizationError as exc:
            result.skip(f"bad_word: {exc}", word)
            continue
        row = get_word(conn, word)
        senses = (
            [
                {"sense_key": s["sense_key"], "sense_definition": s["definition"]}
                for s in list_senses(conn, int(row["id"]))
            ]
            if row
            else []
        )
        existing = _existing_identities_for_word(conn, word)
        seen |= existing
        word_context.append(
            {
                "word": row["text"] if row else word,
                "normalized": normalized,
                "known_senses": senses,
                "existing_category_keys": sorted({item[1] for item in existing}),
            }
        )

    for start in range(0, len(word_context), batch_size):
        batch = word_context[start : start + batch_size]
        for chunk_start in range(0, len(catalog), catalog_chunk):
            chunk = catalog[chunk_start : chunk_start + catalog_chunk]
            prompt = build_expand_words_prompt(words=batch, catalog=chunk)
            raw = ""
            try:
                raw = _call_model(provider, prompt, max_retries=max_retries, sleep=sleep)
                payload = parse_json_response(raw)
                parsed = ReverseExpansionOutput.model_validate(payload)
            except (LLMError, ValueError, ValidationError) as exc:
                result.batches_failed += 1
                result.skip("batch_failed", str(exc))
                _log_run(
                    conn,
                    generation_type="reverse_expansion",
                    provider=provider,
                    input_json={"words": [w["word"] for w in batch]},
                    raw=raw,
                    parsed=None,
                    status="error",
                    error=str(exc)[:2000],
                    result=result,
                )
                continue

            accepted: list[dict[str, Any]] = []
            for word_block in parsed.words:
                try:
                    normalize_word(word_block.word)
                except NormalizationError as exc:
                    result.skip(f"bad_word: {exc}", word_block.model_dump())
                    continue
                for suggestion in word_block.memberships:
                    if suggestion.category_key not in known_keys:
                        result.skip("unknown_category_key", suggestion.model_dump())
                        continue
                    if bool(suggestion.sense_key) != bool(suggestion.sense_definition):
                        result.skip("incomplete_sense", suggestion.model_dump())
                        continue
                    record = {
                        "word": word_block.word.strip(),
                        "language": "en",
                        "part_of_speech": None,
                        "is_proper_noun": False,
                        "sense_key": normalize_sense_key(suggestion.sense_key)
                        if suggestion.sense_key
                        else None,
                        "sense_definition": suggestion.sense_definition,
                        "category_key": suggestion.category_key,
                        "relation_type": suggestion.relation_type
                        or relation_by_key.get(suggestion.category_key, "related_to"),
                        "reason": suggestion.reason.strip(),
                        "fit_score": suggestion.fit_score,
                        "obviousness_score": suggestion.obviousness_score,
                        "source": SOURCE_REVERSE_EXPANSION,
                        "review_status": "candidate",
                        "risk_flags": suggestion.risk_flags,
                    }
                    identity = _identity(record)
                    if identity in seen:
                        result.skip("duplicate", record)
                        continue
                    seen.add(identity)
                    accepted.append(record)

            result.records.extend(accepted)
            result.batches_ok += 1
            _log_run(
                conn,
                generation_type="reverse_expansion",
                provider=provider,
                input_json={"words": [w["word"] for w in batch]},
                raw=raw,
                parsed=accepted,
                status="ok",
                error=None,
                result=result,
            )

    return result


# ------------------------------------------------------------- C. adversarial review


def review_candidates(
    conn: sqlite3.Connection,
    provider: LLMProvider,
    *,
    statuses: list[str] | None = None,
    limit: int = 100,
    batch_size: int = 20,
    max_retries: int = 2,
    sleep: Any = None,
) -> GenerationResult:
    """Проход C: модель-критик оценивает кандидатов. review_status НЕ меняется."""
    from .repositories import memberships_by_status

    rows = memberships_by_status(conn, statuses, limit=limit)
    result = GenerationResult()
    if not rows:
        return result

    payload_rows = [
        {
            "membership_id": row["membership_id"],
            "word": row["word"],
            "sense_key": row["sense_key"],
            "sense_definition": row["sense_definition"],
            "category_key": row["category_key"],
            "category_label": row["category_label"],
            "category_rule": row["category_rule"],
            "relation_type": row["relation_type"],
            "reason": row["reason"],
            "fit_score": row["fit_score"],
            "obviousness_score": row["obviousness_score"],
            "source": row["source"],
            "current_status": row["review_status"],
        }
        for row in rows
    ]
    valid_ids = {item["membership_id"] for item in payload_rows}

    for start in range(0, len(payload_rows), batch_size):
        batch = payload_rows[start : start + batch_size]
        prompt = build_adversarial_review_prompt(memberships=batch)
        raw = ""
        try:
            raw = _call_model(provider, prompt, max_retries=max_retries, sleep=sleep)
            payload = parse_json_response(raw)
            parsed = AdversarialReviewOutput.model_validate(payload)
        except (LLMError, ValueError, ValidationError) as exc:
            result.batches_failed += 1
            result.skip("batch_failed", str(exc))
            _log_run(
                conn,
                generation_type="adversarial_review",
                provider=provider,
                input_json={"membership_ids": [item["membership_id"] for item in batch]},
                raw=raw,
                parsed=None,
                status="error",
                error=str(exc)[:2000],
                result=result,
            )
            continue

        accepted = []
        for verdict in parsed.verdicts:
            if verdict.membership_id not in valid_ids:
                result.skip("unknown_membership_id", verdict.model_dump())
                continue
            accepted.append(verdict.model_dump())

        result.records.extend(accepted)
        result.batches_ok += 1
        _log_run(
            conn,
            generation_type="adversarial_review",
            provider=provider,
            input_json={"membership_ids": [item["membership_id"] for item in batch]},
            raw=raw,
            parsed=accepted,
            status="ok",
            error=None,
            result=result,
        )

    return result


# ------------------------------------------------------------------------------ утилиты


def _log_run(
    conn: sqlite3.Connection,
    *,
    generation_type: str,
    provider: LLMProvider,
    input_json: Any,
    raw: str,
    parsed: Any,
    status: str,
    error: str | None,
    result: GenerationResult,
) -> None:
    """Пишет generation_run. Сырой ответ сохраняется в том числе при ошибке разбора."""
    with transaction(conn):
        run_id = record_generation_run(
            conn,
            generation_type=generation_type,
            model=provider.model,
            prompt_version=PROMPT_VERSION,
            input_json=input_json,
            raw_output_json=raw or None,
            parsed_output_json=parsed,
            status=status,
            error_message=error,
        )
    result.run_ids.append(run_id)


def records_to_jsonl_dicts(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Убирает пустые поля, чтобы JSONL оставался читаемым."""
    cleaned = []
    for record in records:
        cleaned.append({k: v for k, v in record.items() if v not in (None, [], "")})
    return cleaned


def dump_skipped(result: GenerationResult) -> str:
    return json.dumps(result.skipped, ensure_ascii=False, indent=2)


__all__ = [
    "GenerationResult",
    "ValidationIssue",
    "expand_category",
    "expand_words",
    "records_to_jsonl_dicts",
    "review_candidates",
]
