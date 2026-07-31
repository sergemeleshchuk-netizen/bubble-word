#!/usr/bin/env python3
"""Конвертер пакета инструмента (schema 2.0) в формат playable (levels/SCHEMA.md).

Пакет инструмента отдаёт категории как {key,label,words:[{text,kind,meta_child}]},
playable ждёт {id,name,words:[строки]}. Мета-слово в схеме 2.0 помечено kind=meta,
в playable цепочка распознаётся сама: слово == имя другой категории уровня.

Отличия, которые фиксируем при конвертации:
- board.start_bubbles в пакете = число спавнящихся слов (50+), а в playable это
  ЁМКОСТЬ поля с досыпкой (референс 20-24) -> берём board.board_capacity;
- modifiers.chains прототип не реализует -> уносим в extensions.chains как данные.

На входе принимает и цельный пакет (`{levels: [...]}`), и папку с отдельными
`game-*.json` — так их отдаёт `tool/level-tool/scripts/generate_block.ts --out`.

Запуск: python3 tool/scripts/pack_to_playable.py <pack.json|dir> <outdir> [--prefix t]
"""
import json
import math
import sys
from pathlib import Path


def convert(level: dict, source: str) -> dict:
    cats = []
    for c in level["categories"]:
        cats.append({
            "id": c["key"].replace("_", "-"),
            "name": c["label"].title(),
            "words": [w["text"].lower() for w in c["words"]],
        })
    b = level["board"]
    m = len(cats)
    limit = b.get("move_limit")   # None = туториальный уровень без лимита ходов
    chains = (level.get("modifiers") or {}).get("chains") or []
    return {
        "level_id": level["level_id"],
        "difficulty_target": None,
        "source": source,
        "categories": cats,
        "traps": [],
        "repeats": [],
        "board": {
            "start_bubbles": b.get("board_capacity") or 24,
            "move_limit": limit,
            "move_limit_k": round(limit / (3 * m), 3) if limit else None,
        },
        "extensions": {"chunks": [], "chains": chains or None, "picture_words": []},
    }


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    src = Path(sys.argv[1])
    if src.is_dir():
        # папка от generate_block.ts --out: по файлу на уровень
        files = sorted(src.glob("game-*.json"), key=lambda f: int(f.stem.split("-")[1]))
        if not files:
            print(f"в {src} нет файлов game-*.json", file=sys.stderr)
            return 2
        pack = {"levels": [json.loads(f.read_text(encoding="utf-8")) for f in files]}
    else:
        pack = json.loads(src.read_text(encoding="utf-8"))
    source = src.name
    outdir = Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    prefix = "t"
    if "--prefix" in sys.argv:
        prefix = sys.argv[sys.argv.index("--prefix") + 1]

    for lv in pack["levels"]:
        out = convert(lv, source)
        # инварианты схемы: ровно 4 слова, слово на уровне уникально
        seen = set()
        for c in out["categories"]:
            assert len(c["words"]) == 4, (out["level_id"], c["id"], len(c["words"]))
            for w in c["words"]:
                assert w not in seen, (out["level_id"], "дубль слова", w)
                seen.add(w)
        m = len(out["categories"])
        limit = out["board"]["move_limit"]
        assert limit is None or limit >= 3 * m, (out["level_id"], "лимит ниже минимума")
        path = outdir / f"{prefix}{out['level_id']}.json"
        path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{path}  M={m} words={len(seen)} field={out['board']['start_bubbles']} "
              f"moves={'без лимита' if limit is None else limit} K={out['board']['move_limit_k']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
