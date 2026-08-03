#!/usr/bin/env python3
"""Уровни оригинала как есть — в файл, который читает браузер.

    reference/bwj-org/levels.jsonl  ┐
    …/reference/video-boards-20.json├─(этот скрипт)─> web/src/data/bwj-levels.json

Зачем отдельный файл, если словарь оригинала уже есть снимком. Снимок — это
СЛОВАРЬ: категории, слова, связи. По нему можно собрать уровень генератором, но
нельзя воспроизвести уровень ОРИГИНАЛА: в снимке нет ни состава уровня N, ни
порядка слов, ни распилов. Всё это живёт в выгрузке, и здесь она переводится в
компактный вид для бандла.

Что кладём и почему именно это:

  cats[].n     имя категории (в снимке словаря по нему находится всё остальное)
  cats[].w     слова В ПОРЯДКЕ ВЫДАЧИ — это порядок сайта, и он подтверждён
               покадрово по 19 записанным уровням (reference-deal-order.md §4а)
  cats[].m     какие из слов — мета-пузыри (имена других категорий уровня)
  cats[].d/p   глубина и родитель: мета-цепь размечена самим источником
  cats[].c     распилы: слово, приходящее на поле ДВУМЯ пузырями, и место распила

Плюс наблюдённые величины для уровней 1-20, которых в выгрузке нет вообще:
лимит ходов и число пузырей на старте, снятые с записей. Для остальных уровней
их нет, и врать про них нельзя — потребитель обязан считать сам и сказать, что
это его оценка, а не факт оригинала.

Запуск:  python3 scripts/export_reference_levels.py
Вывод:   web/src/data/bwj-levels.json
         data/reference-derived/bwj-levels.sha256
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DUMP = ROOT.parent.parent / "reference" / "bwj-org" / "levels.jsonl"
BOARDS = (ROOT.parent / "word_content_pipeline" / "data" / "reference"
          / "video-boards-20.json")
OUT = ROOT / "web" / "src" / "data" / "bwj-levels.json"
OUT_HASH = ROOT / "data" / "reference-derived" / "bwj-levels.sha256"

SCHEMA_VERSION = "bwj-levels-1.0"


def observed() -> dict[int, dict]:
    """Снятое с записей: лимит ходов и пузыри на старте. Только L1-20."""
    if not BOARDS.exists():
        return {}
    data = json.loads(BOARDS.read_text(encoding="utf-8"))
    out = {}
    for lvl in data.get("levels", []):
        entry = {}
        if lvl.get("move_limit_observed"):
            entry["moveLimit"] = lvl["move_limit_observed"]
        if lvl.get("bubbles_on_start"):
            entry["startBubbles"] = lvl["bubbles_on_start"]
        if lvl.get("words_on_start"):
            entry["wordsOnStart"] = lvl["words_on_start"]
        if entry:
            out[lvl["level"]] = entry
    return out


def main() -> int:
    if not DUMP.exists():
        raise SystemExit(f"нет выгрузки: {DUMP}")
    seen = observed()

    levels = []
    for line in DUMP.open(encoding="utf-8"):
        if not line.strip():
            continue
        d = json.loads(line)
        cats = []
        for c in d["categories"]:
            item = {"n": c["name"], "w": c["words"]}
            if c["meta_words"]:
                item["m"] = c["meta_words"]
            if c["depth"]:
                item["d"] = c["depth"]
            if c["parent"]:
                item["p"] = c["parent"]
            if c.get("chunked_words"):
                item["c"] = [[k["word"], *k["pieces"]] for k in c["chunked_words"]]
            cats.append(item)
        entry = {"id": d["level"], "cats": cats}
        if d["level"] in seen:
            entry["obs"] = seen[d["level"]]
        levels.append(entry)

    levels.sort(key=lambda x: x["id"])
    payload = {
        "schema_version": SCHEMA_VERSION,
        "source": "bubblewordjam.org, выгрузка 1025 уровней",
        "order_note": ("порядок слов внутри категории и порядок категорий — "
                       "порядок выдачи оригинала, подтверждён покадрово на 19 "
                       "записанных уровнях (reference-deal-order.md)"),
        "levels": levels,
    }
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    OUT.write_text(body + "\n", encoding="utf-8")
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    OUT_HASH.parent.mkdir(parents=True, exist_ok=True)
    OUT_HASH.write_text(digest + "\n", encoding="utf-8")

    chunked = sum(1 for l in levels if any("c" in c for c in l["cats"]))
    print(f"уровней: {len(levels)}")
    print(f"  с распиленными словами: {chunked}")
    print(f"  с наблюдённым стартом (записи): {sum(1 for l in levels if 'obs' in l)}")
    print(f"  размер: {len(body) / 1_000_000:.2f} МБ")
    print(f"→ {OUT.relative_to(ROOT)}  sha256 {digest[:16]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
