"""Загрузка и сборка промптов. Шаблоны лежат в prompts/ и используют $-подстановки."""

from __future__ import annotations

import json
import os
from pathlib import Path
from string import Template
from typing import Any

PROMPT_VERSION = "v1"
ENV_PROMPTS_DIR = "WORD_CONTENT_PROMPTS_DIR"

SYSTEM_PROMPT = (
    "You are a careful lexical content editor for an American English word puzzle. "
    "You answer with raw JSON only: no markdown, no commentary, no code fences."
)


def prompts_dir() -> Path:
    """prompts/ рядом с корнем проекта; путь можно переопределить переменной окружения."""
    override = os.environ.get(ENV_PROMPTS_DIR)
    if override:
        return Path(override)
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "prompts"
        if candidate.is_dir() and (candidate / "expand_category.txt").exists():
            return candidate
    raise FileNotFoundError(
        "Каталог prompts/ не найден. Задайте переменную окружения "
        f"{ENV_PROMPTS_DIR} с путём к шаблонам."
    )


def load_prompt(name: str) -> Template:
    path = prompts_dir() / f"{name}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Шаблон промпта не найден: {path}")
    return Template(path.read_text(encoding="utf-8"))


def _json_block(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def build_expand_category_prompt(
    *,
    category: dict[str, Any],
    existing_words: list[str],
    available_category_keys: list[str],
    count: int,
) -> str:
    return load_prompt("expand_category").safe_substitute(
        category_key=category["category_key"],
        label=category["label"],
        rule=category["rule"],
        relation_type=category["relation_type"],
        theme=category["theme"],
        count=count,
        existing_words=", ".join(existing_words) if existing_words else "(none yet)",
        available_category_keys=_json_block(available_category_keys),
    )


def build_expand_words_prompt(
    *,
    words: list[dict[str, Any]],
    catalog: list[dict[str, Any]],
) -> str:
    return load_prompt("expand_words").safe_substitute(
        words_json=_json_block(words),
        catalog_json=_json_block(catalog),
    )


def build_adversarial_review_prompt(*, memberships: list[dict[str, Any]]) -> str:
    return load_prompt("adversarial_review").safe_substitute(
        memberships_json=_json_block(memberships)
    )
