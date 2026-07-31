"""Базовый интерфейс провайдера и повторные попытки с экспоненциальной задержкой."""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


class LLMError(RuntimeError):
    """Ошибка обращения к модели или разбора её ответа."""


@dataclass
class LLMResponse:
    """Сырой ответ модели плюс минимальные метаданные (без секретов)."""

    text: str
    model: str
    finish_reason: str | None = None


class LLMProvider(ABC):
    """Минимальный контракт: получить JSON-ответ на текстовый промпт."""

    name: str = "abstract"
    model: str = "unknown"

    @abstractmethod
    def complete_json(self, prompt: str, *, system: str | None = None) -> LLMResponse:
        """Возвращает сырой текст ответа (ожидается JSON без markdown)."""


def call_with_retries(
    func: Callable[[], T],
    *,
    max_retries: int = 3,
    base_delay: float = 1.0,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Повторяет вызов при LLMError: задержки base_delay, 2x, 4x ..."""
    attempt = 0
    while True:
        try:
            return func()
        except LLMError:
            attempt += 1
            if attempt > max_retries:
                raise
            sleep(base_delay * (2 ** (attempt - 1)))
