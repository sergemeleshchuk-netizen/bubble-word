"""Mock-провайдер: детерминированные ответы для тестов и smoke-прогонов."""

from __future__ import annotations

import json
import re
from collections.abc import Callable, Sequence
from pathlib import Path

from .base import LLMError, LLMProvider, LLMResponse

_ID_RE = re.compile(r'"membership_id"\s*:\s*(\d+)')
_CATEGORY_KEY_RE = re.compile(r"category_key:\s*(\S+)")


def echo_handler(prompt: str) -> dict:
    """Ответ-заглушка, валидный по схеме: пустые предложения и нейтральные вердикты.

    Нужен, чтобы `--provider mock` без файла ответов проходил все три команды
    и ничего не выдумывал за модель.
    """
    ids = [int(x) for x in _ID_RE.findall(prompt)]
    if ids:
        return {
            "verdicts": [
                {
                    "membership_id": membership_id,
                    "recommended_decision": "manual_review",
                    "issues": ["mock provider: настоящая модель не вызывалась"],
                    "explanation": "Заглушка: решение должен принять человек или реальная модель.",
                }
                for membership_id in ids
            ]
        }
    match = _CATEGORY_KEY_RE.search(prompt)
    if match:
        return {"category_key": match.group(1), "candidates": []}
    return {"words": []}


class MockLLMProvider(LLMProvider):
    """Отдаёт заранее заданные ответы по очереди.

    responses: строки (сырой ответ модели) или объекты, которые будут сериализованы в JSON.
    handler:   функция (prompt) -> ответ; приоритетнее списка responses.
    Элемент-исключение в responses будет брошен — так тестируются retry и ошибки batch.
    """

    name = "mock"

    def __init__(
        self,
        responses: Sequence[object] | None = None,
        *,
        handler: Callable[[str], object] | None = None,
        model: str = "mock-model",
        repeat_last: bool = False,
    ) -> None:
        self.responses: list[object] = list(responses or [])
        self.handler = handler
        self.model = model
        self.repeat_last = repeat_last
        self.calls: list[str] = []
        self._index = 0

    @classmethod
    def from_file(cls, path: Path, *, model: str = "mock-file") -> MockLLMProvider:
        """Ответы из JSON-файла: либо один объект, либо список ответов по порядку."""
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        responses = payload if isinstance(payload, list) else [payload]
        return cls(responses, model=model, repeat_last=True)

    def complete_json(self, prompt: str, *, system: str | None = None) -> LLMResponse:
        self.calls.append(prompt)

        if self.handler is not None:
            result = self.handler(prompt)
        elif self._index < len(self.responses):
            result = self.responses[self._index]
            self._index += 1
        elif self.repeat_last and self.responses:
            result = self.responses[-1]
        else:
            raise LLMError("MockLLMProvider: заготовленные ответы закончились")

        if isinstance(result, BaseException):
            raise result
        text = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)
        return LLMResponse(text=text, model=self.model, finish_reason="stop")
