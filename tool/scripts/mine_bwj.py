#!/usr/bin/env python3
"""Майнер выгрузки Bubble Word Jam: пачки кандидатов в базу слов.

Запуск из корня репозитория BB:
    python3 tool/scripts/mine_bwj.py [--limit 25] [--min-words 4]

Читает локальную выгрузку `reference/bwj-answers/bwj_levels.json` (в git не
попадает) и текущую базу `tool/data/categories.json`, выдаёт очередную пачку
кандидатов для курирования скиллом word-associations-generator:

- READY  - пул >= 6 однословных: бери, шлифуй, вливай;
- AUGMENT - пул 4-5 слов: ядро из источника + досыпка LLM до 6-8.

Состояния нет: влитые категории попадают в базу и отфильтровываются
при следующем запуске (по имени И по пересечению пулов >= 3 слов).
Мусор источника (бренды, солянки) отсеивается глазами при курировании.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DUMP = ROOT / "reference" / "bwj-answers" / "bwj_levels.json"
BASE = ROOT / "tool" / "data" / "categories.json"
BLOCKLIST = ROOT / "tool" / "data" / "blocklist.txt"


def single(w):
    return " " not in w and w.isascii() and w.isalpha() and len(w) <= 12


def kebab(name):
    return re.sub(r"\s+", "-", re.sub(r"[^a-z0-9 -]", "", name.lower()).strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=25, help="размер пачки")
    ap.add_argument("--min-words", type=int, default=4,
                    help="минимум однословных слов у кандидата")
    args = ap.parse_args()

    if not DUMP.exists():
        sys.exit(f"Нет выгрузки {DUMP} - она локальная (не в git); "
                 f"источник: puzzlegamemaster.com/bubble-word-jam-answers-all/")
    levels = json.loads(DUMP.read_text())
    base = json.loads(BASE.read_text())
    blocked = set()
    if BLOCKLIST.exists():
        blocked = {l.strip().lower() for l in BLOCKLIST.read_text().splitlines()
                   if l.strip() and not l.startswith("#")}

    base_ids = {c["id"] for c in base["categories"]}
    base_names = {c["name"].lower() for c in base["categories"]}
    base_pools = {c["id"]: {w["w"] for w in c["words"]} for c in base["categories"]}
    base_words = collections.defaultdict(list)
    for cid, pool in base_pools.items():
        for w in pool:
            base_words[w].append(cid)

    # агрегируем источник: имя категории -> объединённый пул по всем уровням
    agg = collections.defaultdict(set)
    for lv in levels:
        for c in lv["categories"]:
            agg[c["name"]].update(c["words"])

    candidates = []
    for name, words in sorted(agg.items()):
        cn = re.sub(r"[^a-z0-9 -]", "", name.lower()).strip()
        if not cn or len(cn.split()) > 3:
            continue
        ws = sorted(w for w in words if single(w) and w not in blocked)
        if len(ws) < args.min_words:
            continue
        if kebab(cn) in base_ids or cn in base_names:
            continue
        # дубль по пулу: 3+ общих слова с одной категорией базы (урок bank≈banking);
        # для короткого пула 4 слов хватает и 2 общих (headwear≈hats, beach items⊂beach)
        threshold = 2 if len(ws) == 4 else 3
        twin = None
        for cid, pool in base_pools.items():
            if len(pool & set(ws)) >= threshold:
                twin = cid
                break
        if twin:
            continue
        overlap = sorted(w for w in ws if w in base_words)
        candidates.append((cn, ws, overlap))

    # ценность: сперва больше пересечений с базой (ловушки), потом полнее пул
    candidates.sort(key=lambda x: (-len(x[2]), -len(x[1]), x[0]))

    total_ready = sum(1 for _, ws, _ in candidates if len(ws) >= 6)
    total_aug = len(candidates) - total_ready
    print(f"# Кандидаты из выгрузки BWJ: всего {len(candidates)} "
          f"(READY {total_ready} / AUGMENT {total_aug}); пачка {args.limit}\n")
    for cn, ws, ov in candidates[:args.limit]:
        tag = "READY  " if len(ws) >= 6 else "AUGMENT"
        ovs = f"  ловушки-кандидаты: {', '.join(ov)}" if ov else ""
        print(f"[{tag}] {cn} ({len(ws)}): {', '.join(ws)}{ovs}")


if __name__ == "__main__":
    main()
