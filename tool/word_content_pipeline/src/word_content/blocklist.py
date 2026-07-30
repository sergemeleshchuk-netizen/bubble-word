"""Блок-лист: слова, которые не должны попадать в игровой контент ни при каких условиях."""

from __future__ import annotations

import re
from pathlib import Path

from .normalization import normalize_word

_SPLIT_RE = re.compile(r"[ \-]+")


def default_path() -> Path | None:
    """Штатный блок-лист проекта: data/blocklist.txt рядом с корнем пакета."""
    return _data_file("blocklist.txt")


def default_allowlist_path() -> Path | None:
    """Список исключений: безобидные названия, внутри которых есть запрещённое слово."""
    return _data_file("allowlist.txt")


def _data_file(name: str) -> Path | None:
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "data" / name
        if candidate.exists():
            return candidate
    return None


def _read_entries(path: Path) -> set[str]:
    entries: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        entry = line.split("#", 1)[0].strip().lower()
        if entry:
            entries.add(entry)
    return entries


class Blocklist:
    """Проверка по точному совпадению слова или любого слова внутри фразы.

    allowed — фразы-исключения целиком: «sperm whale» и «maine coon» проходят,
    хотя внутри них есть слово из блок-листа.
    """

    def __init__(self, words: set[str] | None = None, allowed: set[str] | None = None) -> None:
        self.words = words or set()
        self.allowed = allowed or set()

    @classmethod
    def load(cls, path: Path | str | None, allowlist: Path | str | None = None) -> Blocklist:
        """Читает текстовый файл: одно слово в строке, # — комментарий."""
        if path is None:
            return cls()
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Блок-лист не найден: {file_path}")

        allow_path = Path(allowlist) if allowlist else default_allowlist_path()
        allowed = _read_entries(allow_path) if allow_path and allow_path.exists() else set()
        return cls(_read_entries(file_path), allowed)

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
        if normalized in self.allowed:
            return None
        if normalized in self.words:
            return normalized
        for token in _SPLIT_RE.split(normalized):
            if token in self.words:
                return token
        return None
