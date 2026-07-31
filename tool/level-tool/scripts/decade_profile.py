#!/usr/bin/env python3
"""Профиль референса по декадам уровней — источник цифр для docs/DECADE_CALIBRATION.md.

Считает по выгрузке ответов оригинала (199 уровней) всё, на что калибруется
генератор: размер уровня, распределение частотности, форму слов, мета-плотность,
повторы слов между уровнями, переиспользование имён категорий и ритм внутри декады.

Запуск (нужен wordfreq; в проекте BB есть venv пайплайна):
  level-generator/bubble_jam_pipeline/.venv/bin/python \
      tool/level-tool/scripts/decade_profile.py [путь-к-bwj_levels.json]

Референс — чужой контент, в репозиторий не коммитится (см. .gitignore),
поэтому путь по умолчанию указывает на локальную копию в проекте BB.
"""
from __future__ import annotations

import json
import statistics as st
import sys
from collections import Counter, defaultdict
from pathlib import Path

from wordfreq import zipf_frequency

DEFAULT_REF = Path(__file__).resolve().parents[3] / "reference/bwj-answers/bwj_levels.json"

_zipf: dict[str, float] = {}


def z(word: str) -> float:
    if word not in _zipf:
        _zipf[word] = zipf_frequency(word.lower(), "en")
    return _zipf[word]


def share(items: list, pred) -> float:
    return sum(1 for x in items if pred(x)) / len(items) * 100


def decades(levels: list[dict], size: int = 10):
    for start in range(0, len(levels), size):
        chunk = levels[start:start + size]
        if chunk:
            yield start + 1, start + len(chunk), chunk


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_REF
    if not path.exists():
        print(f"нет файла референса: {path}", file=sys.stderr)
        return 2
    levels = json.loads(path.read_text(encoding="utf-8"))

    # слово -> [(уровень, имя категории)] для повторов
    history: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for lv in levels:
        for cat in lv["categories"]:
            for w in cat["words"]:
                history[w].append((lv["level"], cat["name"]))

    print("=== профиль по декадам (таблица §2 в DECADE_CALIBRATION.md) ===")
    head = (f"{'декада':>9} | {'кат':>4} {'мин-макс':>8} {'слов':>4} | {'zmed':>4} {'p25':>4} {'p5':>4} "
            f"{'редк':>5} | {'мног':>5} {'дл>9':>5} | {'мета':>4} {'повт':>5} {'реюз':>5}")
    print(head)
    # реюз считаем ПО УРОВНЯМ: доля имён категорий уровня, встречавшихся на любом
    # предыдущем уровне. Считать пересечением множеств декад нельзя — тогда реюз
    # внутри самой декады теряется и первая декада всегда даёт 0.
    seen_names: set[str] = set()
    reuse_by_level: dict[int, float] = {}
    for lv in levels:
        names = {c["name"] for c in lv["categories"]}
        reuse_by_level[lv["level"]] = len(names & seen_names) / len(names) * 100
        seen_names |= names

    for lo, hi, chunk in decades(levels):
        cats = [len(lv["categories"]) for lv in chunk]
        words = [w for lv in chunk for c in lv["categories"] for w in c["words"]]
        zs = sorted(z(w) for w in words)
        metas, repeats = [], []
        for lv in chunk:
            names = {c["name"].lower() for c in lv["categories"]}
            metas.append(sum(1 for c in lv["categories"] for w in c["words"] if w.lower() in names))
            repeats.append(sum(
                1 for c in lv["categories"] for w in c["words"]
                if any(l < lv["level"] and n != c["name"] for l, n in history[w])
            ))
        reuse = st.mean(reuse_by_level[lv["level"]] for lv in chunk)
        print(f"{lo:>4}-{hi:<4} | {st.mean(cats):>4.1f} {min(cats):>3}-{max(cats):<4} "
              f"{st.mean(cats) * 4:>4.0f} | {st.median(zs):>4.2f} {zs[len(zs) // 4]:>4.2f} "
              f"{zs[int(len(zs) * 0.05)]:>4.2f} {share(words, lambda w: z(w) < 3.0):>4.0f}% | "
              f"{share(words, lambda w: ' ' in w):>4.0f}% {share(words, lambda w: len(w) > 9):>4.0f}% | "
              f"{st.mean(metas):>4.1f} {st.mean(repeats):>5.1f} {reuse:>4.0f}%")

    # ритм: категории позиции, нормированные на среднее своей декады
    print("\n=== ритм внутри декады (таблица §3) ===")
    cats_all = [len(lv["categories"]) for lv in levels]
    norm: list[list[float]] = [[] for _ in range(10)]
    for lo, hi, chunk in decades(levels):
        if len(chunk) < 10:
            continue
        mean = st.mean(len(lv["categories"]) for lv in chunk)
        for i, lv in enumerate(chunk):
            norm[i].append(len(lv["categories"]) / mean)
    print(f"{'поз':>4} {'отн.':>6} {'декад вниз':>11}")
    for i in range(10):
        down = sum(1 for d in range(0, 190, 10) if i > 0 and cats_all[d + i] < cats_all[d + i - 1])
        print(f"{i + 1:>4} {st.mean(norm[i]):>6.3f} {down:>8}/19")
    down_all = sum(1 for i in range(1, len(cats_all)) if cats_all[i] < cats_all[i - 1])
    print(f"переходов вниз всего: {down_all}/{len(cats_all) - 1} = {down_all / (len(cats_all) - 1) * 100:.0f}%")

    # когда впервые появляется каждая форма слова
    print("\n=== первое появление форм (раздел §2) ===")
    first: dict[str, tuple[int, str]] = {}
    for lv in levels:
        for c in lv["categories"]:
            for w in c["words"]:
                if " " in w:
                    first.setdefault("многословное", (lv["level"], w))
                if z(w) < 3.0:
                    first.setdefault("zipf<3.0", (lv["level"], w))
                if z(w) < 2.0:
                    first.setdefault("zipf<2.0", (lv["level"], w))
    for key, (lvl, w) in first.items():
        print(f"  {key:14s} ур.{lvl:>3}  «{w}»")

    # темы декад — ориентир для наполнения базы слов
    print("\n=== частые слова в именах категорий (ориентир для базы) ===")
    stop = {"of", "the", "and", "a", "in", "on", "at", "to", "things", "words", "types",
            "kinds", "more", "parts", "you"}
    for lo, hi, chunk in decades(levels):
        toks = Counter()
        for lv in chunk:
            for c in lv["categories"]:
                for t in c["name"].lower().split():
                    if t not in stop and len(t) > 2:
                        toks[t] += 1
        print(f"  {lo:>3}-{hi:<3}: " + ", ".join(f"{t}×{n}" for t, n in toks.most_common(9)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
