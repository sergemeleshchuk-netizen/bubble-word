#!/usr/bin/env python3
"""SWOW-источник: живые ассоциации людей для базы слов и ловушек.

Датасет: Small World of Words SWOW-EN (2018), сырые ответы участников
cue -> R1,R2,R3. Лицензия: research/personal use, без редистрибуции -
файл живёт ЛОКАЛЬНО в reference/swow/ (папка в .gitignore).

Запуск из корня репозитория BB:
    python3 tool/scripts/swow_source.py build          # агрегат (один раз, ~1 мин)
    python3 tool/scripts/swow_source.py word orange    # топ-ассоциации слова
    python3 tool/scripts/swow_source.py traps          # замер ловушек базы (shared_words)
    python3 tool/scripts/swow_source.py mine [--top 30]  # новые кандидаты в ловушки

Сила связи слово-слово: sym(a,b) = s(a->b) + s(b->a), где s = доля взвешенных
ответов (R1 вес 1.0, R2/R3 вес 0.5) среди всех ответов на стимул.
Сила связи слово-КАТЕГОРИЯ = средняя sym к словам пула (имена категорий в игре
скрыты до сборки, игрок ассоциирует с видимыми словами, не с именем).
"""
import argparse
import collections
import csv
import json
import pickle
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "reference" / "swow" / "SWOW-EN.R100.20180827.csv"
AGG = ROOT / "reference" / "swow" / "swow_agg.pkl"
BASE = ROOT / "tool" / "data" / "categories.json"

W2, MIN_COUNT = 0.5, 2.0  # вес R2/R3; шумовой порог взвешенного счёта


def build():
    if not RAW.exists():
        sys.exit(f"Нет датасета {RAW} (локальный, не в git). Источник: smallworldofwords.org")
    counts = collections.defaultdict(collections.Counter)
    with open(RAW, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            cue = row["cue"].strip().lower()
            if not cue:
                continue
            for col, w in (("R1", 1.0), ("R2", W2), ("R3", W2)):
                r = (row[col] or "").strip().lower()
                if r and r not in ("na", "no more responses", "unknown word"):
                    counts[cue][r] += w
    strengths, backward = {}, collections.defaultdict(dict)
    for cue, ctr in counts.items():
        total = sum(ctr.values())
        kept = {r: round(c / total, 5) for r, c in ctr.items() if c >= MIN_COUNT}
        if kept:
            strengths[cue] = kept
            for r, s in kept.items():
                backward[r][cue] = s
    AGG.write_bytes(pickle.dumps({"fwd": strengths, "bwd": dict(backward)}))
    print(f"стимулов: {len(strengths)}, связей: {sum(len(v) for v in strengths.values())}, "
          f"агрегат: {AGG} ({AGG.stat().st_size//1_000_000} MB)")


def load():
    if not AGG.exists():
        sys.exit("Сначала: python3 tool/scripts/swow_source.py build")
    return pickle.loads(AGG.read_bytes())


def sym(agg, a, b):
    return agg["fwd"].get(a, {}).get(b, 0.0) + agg["fwd"].get(b, {}).get(a, 0.0)


def cat_strength(agg, word, pool):
    others = [w for w in pool if w != word]
    return sum(sym(agg, word, w) for w in others) / max(1, len(others))


def cmd_word(agg, word):
    fwd = sorted(agg["fwd"].get(word, {}).items(), key=lambda x: -x[1])[:15]
    bwd = sorted(agg["bwd"].get(word, {}).items(), key=lambda x: -x[1])[:15]
    print(f"{word} -> ответы людей: {[(w, round(s,3)) for w, s in fwd]}")
    print(f"{word} <- стимулы, ведущие к нему: {[(w, round(s,3)) for w, s in bwd]}")


def cmd_traps(agg):
    base = json.loads(BASE.read_text())
    pools = {c["id"]: [w["w"] for w in c["words"]] for c in base["categories"]}
    rows = []
    for c in base["categories"]:
        for w, others in c.get("shared_words", {}).items():
            for other in others:
                if other not in pools:
                    continue
                home = cat_strength(agg, w, pools[c["id"]])
                away = cat_strength(agg, w, pools[other])
                rows.append((w, c["id"], other, home, away))
    rows.sort(key=lambda r: -min(r[3], r[4]))
    print(f"{'слово':14} {'дом':18} {'соблазн':18} {'к дому':>7} {'к соблазну':>10}  вердикт")
    seen = set()
    for w, home_id, away_id, h, a in rows:
        key = tuple(sorted([w, home_id, away_id]))
        if key in seen:
            continue
        seen.add(key)
        if min(h, a) >= 0.010:
            verdict = "СИЛЬНАЯ ловушка (обе стороны тянут)"
        elif max(h, a) >= 0.010 and min(h, a) > 0:
            verdict = "рабочая (одна сторона заметно сильнее)"
        elif max(h, a) > 0:
            verdict = "слабая по SWOW"
        else:
            verdict = "SWOW не видит связи (ловушка логическая)"
        print(f"{w:14} {home_id:18} {away_id:18} {h:7.3f} {a:10.3f}  {verdict}")


def cmd_mine(agg, top):
    base = json.loads(BASE.read_text())
    pools = {c["id"]: [w["w"] for w in c["words"]] for c in base["categories"]}
    declared = set()
    for c in base["categories"]:
        for w, others in c.get("shared_words", {}).items():
            for o in others:
                declared.add((w, o))
                declared.add((w, c["id"]))
    cands = []
    ids = list(pools)
    for cid in ids:
        for w in pools[cid]:
            for other in ids:
                if other == cid or (w, other) in declared or w in pools[other]:
                    continue
                s = cat_strength(agg, w, pools[other])
                if s >= 0.012:
                    cands.append((w, cid, other, s))
    cands.sort(key=lambda r: -r[3])
    print(f"Новые кандидаты в ловушки (слово живёт в 'доме', SWOW тянет к чужому пулу), топ {top}:")
    for w, home, other, s in cands[:top]:
        print(f"  {w:14} дом {home:18} тянет к {other:20} sym={s:.3f}  "
              f"(пул: {', '.join(pools[other])})")
    print(f"всего кандидатов с sym>=0.012: {len(cands)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "word", "traps", "mine"])
    ap.add_argument("arg", nargs="?")
    ap.add_argument("--top", type=int, default=30)
    a = ap.parse_args()
    if a.cmd == "build":
        build()
        return
    agg = load()
    if a.cmd == "word":
        cmd_word(agg, (a.arg or "").lower())
    elif a.cmd == "traps":
        cmd_traps(agg)
    elif a.cmd == "mine":
        cmd_mine(agg, a.top)


if __name__ == "__main__":
    main()
