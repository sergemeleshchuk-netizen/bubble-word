#!/usr/bin/env python3
"""Ищет слова, у которых стоит развести значения, по данным SWOW.

Идея: если слово стоит в двух категориях, а сами эти категории живут в разных
ассоциативных областях (их профили почти не пересекаются), и при этом слово
уверенно подходит обеим — у слова, скорее всего, два разных значения.

Так находится bat (бейсбол против пещер), pitcher (бейсбол против посуды),
но не apple (FRUITS и RED THINGS — разные категории, значение одно, потому что
профили всё же пересекаются через сам фрукт).

Запуск:
    python scripts/swow_senses.py --limit 60
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

PIPE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPE / "src"))
sys.path.insert(0, str(PIPE / "scripts"))

import pickle  # noqa: E402

from swow_status import SWOW_AGG, build_vectors, canon, category_profiles, score  # noqa: E402

MIN_WORD_SCORE = 0.04  # слово должно уверенно подходить обеим категориям
MAX_CATEGORY_OVERLAP = 0.12  # профили категорий почти не пересекаются
CHECKED = PIPE / "data" / "seed" / "_not_homonyms.txt"


def load_checked() -> set[str]:
    """Слова, уже проверенные вручную и признанные однозначными."""
    if not CHECKED.exists():
        return set()
    return {
        line.split("#", 1)[0].strip().lower()
        for line in CHECKED.read_text(encoding="utf-8").splitlines()
        if line.split("#", 1)[0].strip()
    }


def profile_cosine(profiles: dict, a: str, b: str) -> float | None:
    pa, na = profiles.get(a, ({}, 0))
    pb, nb = profiles.get(b, ({}, 0))
    if not pa or not pb:
        return None
    import math

    norm_a = math.sqrt(sum(v * v for v in pa.values()))
    norm_b = math.sqrt(sum(v * v for v in pb.values()))
    if norm_a == 0 or norm_b == 0:
        return None
    small, big = (pa, pb) if len(pa) <= len(pb) else (pb, pa)
    dot = sum(v * big.get(k, 0.0) for k, v in small.items())
    return dot / (norm_a * norm_b)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=60)
    args = parser.parse_args()

    data = pickle.loads(SWOW_AGG.read_bytes())
    mem = [json.loads(line) for line in (PIPE / "data" / "membership_candidates.jsonl").open()]

    pool: dict[str, list[str]] = defaultdict(list)
    cats_of: dict[str, list[str]] = defaultdict(list)
    has_sense: set[str] = set()
    for m in mem:
        w = canon(m["word"])
        pool[m["category_key"]].append(w)
        cats_of[w].append(m["category_key"])
        if m.get("sense_key"):
            has_sense.add(w)

    words = {w for ws in pool.values() for w in ws}
    vectors = build_vectors(data["fwd"], data["bwd"], words)
    profiles = category_profiles(vectors, pool)

    checked = load_checked()
    found = []
    for word, keys in cats_of.items():
        if word in has_sense or word in checked or len(keys) < 2 or word not in vectors:
            continue
        scored = []
        for key in set(keys):
            s = score(vectors, profiles, word, key)
            if s is not None and s >= MIN_WORD_SCORE:
                scored.append((key, s))
        if len(scored) < 2:
            continue
        worst = None
        for (ka, sa), (kb, sb) in combinations(scored, 2):
            overlap = profile_cosine(profiles, ka, kb)
            if overlap is None:
                continue
            if worst is None or overlap < worst[0]:
                worst = (overlap, ka, kb, sa, sb)
        if worst and worst[0] <= MAX_CATEGORY_OVERLAP:
            found.append((worst[0], word, worst[1], worst[2], worst[3], worst[4]))

    found.sort(key=lambda r: r[0])
    print(f"кандидатов на разведение значений: {len(found)}\n")
    for overlap, word, ka, kb, sa, sb in found[: args.limit]:
        print(f"  {word:16} {ka:24} ({sa:.2f})  <->  {kb:24} ({sb:.2f})   пересечение {overlap:.3f}")


if __name__ == "__main__":
    main()
