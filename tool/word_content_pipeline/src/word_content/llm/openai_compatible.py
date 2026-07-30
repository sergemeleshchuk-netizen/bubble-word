"""Провайдер для любого OpenAI-compatible endpoint (/chat/completions).

Ключ читается только из переменной окружения LLM_API_KEY и никогда не пишется
в файлы, логи, SQLite и сообщения об ошибках.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

from .base import LLMError, LLMProvider, LLMResponse

ENV_API_KEY = "LLM_API_KEY"
ENV_BASE_URL = "LLM_BASE_URL"
ENV_MODEL = "LLM_MODEL"

DEFAULT_BASE_URL = "https://api.openai.com/v1"


class OpenAICompatibleProvider(LLMProvider):
    """Минимальный HTTP-клиент на стандартной библиотеке (без внешних SDK)."""

    name = "openai_compatible"

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        model: str,
        timeout: float = 120.0,
        temperature: float = 0.3,
    ) -> None:
        if not api_key:
            raise LLMError(f"Не задан API-ключ: переменная окружения {ENV_API_KEY}")
        self._api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.temperature = temperature

    def __repr__(self) -> str:  # ключ не должен попадать в repr/логи
        return f"OpenAICompatibleProvider(base_url={self.base_url!r}, model={self.model!r})"

    def complete_json(self, prompt: str, *, system: str | None = None) -> LLMResponse:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        body = json.dumps(
            {
                "model": self.model,
                "messages": messages,
                "temperature": self.temperature,
                "response_format": {"type": "json_object"},
            }
        ).encode("utf-8")

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._api_key}",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:  # тело ошибки может содержать детали, но не ключ
            detail = exc.read().decode("utf-8", errors="replace")[:500]
            raise LLMError(f"HTTP {exc.code} от LLM API: {detail}") from None
        except urllib.error.URLError as exc:
            raise LLMError(f"Сетевая ошибка при обращении к LLM API: {exc.reason}") from None
        except json.JSONDecodeError as exc:
            raise LLMError(f"Ответ LLM API не является JSON: {exc}") from None

        try:
            choice = payload["choices"][0]
            text = choice["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise LLMError(f"Неожиданная структура ответа LLM API: {exc}") from None

        return LLMResponse(
            text=text, model=payload.get("model", self.model), finish_reason=choice.get("finish_reason")
        )


def provider_from_env(model_override: str | None = None) -> OpenAICompatibleProvider:
    """Собирает провайдера из LLM_API_KEY / LLM_BASE_URL / LLM_MODEL."""
    api_key = os.environ.get(ENV_API_KEY, "")
    base_url = os.environ.get(ENV_BASE_URL, DEFAULT_BASE_URL)
    model = model_override or os.environ.get(ENV_MODEL, "")
    if not api_key:
        raise LLMError(
            f"Переменная окружения {ENV_API_KEY} не задана. "
            "Экспортируйте ключ в окружение (в файлы и базу он не пишется)."
        )
    if not model:
        raise LLMError(f"Не задана модель: переменная окружения {ENV_MODEL} или флаг --model")
    return OpenAICompatibleProvider(api_key=api_key, base_url=base_url, model=model)
