"""Абстракция над LLM-провайдером: реальный OpenAI-compatible API и mock для тестов."""

from .base import LLMError, LLMProvider, LLMResponse, call_with_retries
from .mock import MockLLMProvider
from .openai_compatible import OpenAICompatibleProvider, provider_from_env

__all__ = [
    "LLMError",
    "LLMProvider",
    "LLMResponse",
    "MockLLMProvider",
    "OpenAICompatibleProvider",
    "call_with_retries",
    "provider_from_env",
]
