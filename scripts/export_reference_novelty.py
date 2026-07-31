#!/usr/bin/env python3
"""Хеши четвёрок референса для проверки novelty.

Референс — чужой контент. В репозиторий и в браузер уезжают только sha256 от
отсортированной четвёрки слов: этого достаточно, чтобы поймать точную копию,
и при этом сам контент не распространяется.

Проверка на БЛИЗКУЮ копию (3 из 4 слов, Jaccard) требует самих слов, поэтому
она выполняется офлайн в scripts/select_final_pack.ts на локальных данных
и её результат попадает в отчёт.

Запуск:  python3 scripts/export_reference_novelty.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "reference-derived" / "reference-levels.json"
OUT_HASHES = ROOT / "data" / "reference-derived" / "reference-quadruple-hashes.json"
OUT_WORDS = ROOT / "data" / "reference-derived" / "reference-quadruples.local.json"


def quad_hash(words: list) -> str:
    key = "|".join(sorted(w.lower().strip() for w in words))
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def main() -> int:
    if not SRC.exists():
        print(f"нет {SRC}: положите выгрузку референса локально", file=sys.stderr)
        return 1
    levels = json.loads(SRC.read_text(encoding="utf-8"))["levels"]
    hashes, quads = set(), []
    for key in sorted(levels, key=int):
        for cat in levels[key]:
            hashes.add(quad_hash(cat["words"]))
            quads.append({"level": int(key), "category": cat["category"],
                          "words": [w.lower() for w in cat["words"]]})
    OUT_HASHES.write_text(json.dumps(
        {"note": "sha256 от отсортированной четвёрки слов; сам контент не распространяется",
         "count": len(hashes), "hashes": sorted(hashes)}, ensure_ascii=False), encoding="utf-8")
    OUT_WORDS.write_text(json.dumps(quads, ensure_ascii=False), encoding="utf-8")
    print(f"четвёрок: {len(quads)}, уникальных хешей: {len(hashes)}")
    print(f"→ {OUT_HASHES.name} (в репозиторий), {OUT_WORDS.name} (только локально)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
