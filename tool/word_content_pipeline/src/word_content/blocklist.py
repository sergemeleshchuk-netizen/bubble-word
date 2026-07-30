"""Блок-лист: слова, которые не должны попадать в игровой контент ни при каких условиях."""

from __future__ import annotations

import re
from pathlib import Path

from .normalization import normalize_word

_SPLIT_RE = re.compile(r"[ \-]+")


def default_path() -> Path | None:
    """Штатный блок-лист проекта: data/blocklist.txt рядом с корнем пакета."""
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "data" / "blocklist.txt"
        if candidate.exists():
            return candidate
    return None


class Blocklist:
    """Проверка по точному совпадению слова или любого слова внутри фразы."""

    def __init__(self, words: set[str] | None = None) -> None:
        self.words = words or set()

    @classmethod
    def load(cls, path: Path | str | None) -> Blocklist:
        """Читает текстовый файл: одно слово в строке, # — комментарий."""
        if path is None:
            return cls()
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Блок-лист не найден: {file_path}")
        words: set[str] = set()
        for line in file_path.read_text(encoding="utf-8").splitlines():
            entry = line.split("#", 1)[0].strip().lower()
            if entry:
                words.add(entry)
        return cls(words)

    def __len__(self) -> int:
        return len(self.words)

    def __bool__(self) -> bool:
        return bool(self.words)

    def check(self, word: str) -> str | None:
        """Возвращает сработавшую запись блок-листа или None."""
        if not self.words:
            return None
        try:
            normalized = normalize_word(word)
        except Exception:
            return None
        if normalized in self.words:
            return normalized
        for token in _SPLIT_RE.split(normalized):
            if token in self.words:
                return token
        return None
