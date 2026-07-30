#!/usr/bin/env python3
"""Готовит "слепой" вид уровня для решателя (шаг 4 approach.md).

Вход: файлы уровней по схеме levels/SCHEMA.md.
Выход: levels/solver/<имя>.blind.json - только названия категорий (по алфавиту)
и плоский перемешанный список слов. Никаких ответов, ловушек и id.
Перемешивание детерминированное (seed из содержимого), прогон воспроизводим.

Запуск: python3 tool/scripts/solver_blind.py levels/etalon/e2.json [...]
"""
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "levels" / "solver"


def build_blind(level_path: Path) -> Path:
    level = json.loads(level_path.read_text(encoding="utf-8"))
    names = sorted(c["name"] for c in level["categories"])
    words = [w.lower() for c in level["categories"] for w in c["words"]]
    seed = int(hashlib.md5(",".join(sorted(words)).encode()).hexdigest(), 16)
    random.Random(seed).shuffle(words)

    blind = {
        "source": str(level_path.relative_to(ROOT)),
        "level_id": level.get("level_id"),
        "categories": names,
        "words": words,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / (level_path.stem + ".blind.json")
    out.write_text(json.dumps(blind, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    for arg in argv[1:]:
        path = Path(arg).resolve()
        out = build_blind(path)
        print(f"{path.name}: blind -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
