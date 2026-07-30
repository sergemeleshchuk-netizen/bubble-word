#!/usr/bin/env python3
"""Структурные метрики уровня для оценки сложности и фана (levels/EVAL.md).

Считает детерминированную часть модели: масштаб, ловушки (с эмпирикой
решателя), zipf-редкость, K, повторы, кандидатов смежности по базе.
Семантические суждения (узнаваемость, сферы, смежность сверх базы)
остаются оценщику - скилл level-evaluator.

Требует прогона слепого решателя: levels/solver/<имя>.solution.json.

Запуск: python3 tool/scripts/eval_metrics.py levels/etalon/e2.json [...]
Выход: levels/eval/<имя>.metrics.json + сводка в консоль.
"""
import json
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tool" / "data" / "categories.json"
SOLVER_DIR = ROOT / "levels" / "solver"
OUT_DIR = ROOT / "levels" / "eval"

RARE_ZIPF = 3.0


def load_base():
    data = json.loads(BASE.read_text(encoding="utf-8"))
    cats = {c["id"]: c for c in data["categories"]}
    zipf = {}
    for c in data["categories"]:
        for w in c["words"]:
            zipf.setdefault(w["w"].lower(), w.get("zipf"))
    return cats, zipf


def metrics(level_path: Path, base_cats, zipf):
    level = json.loads(level_path.read_text(encoding="utf-8"))
    sol_path = SOLVER_DIR / (level_path.stem + ".solution.json")
    if not sol_path.exists():
        raise SystemExit(
            f"нет решения решателя: {sol_path} - сначала скилл level-solver")
    solution = json.loads(sol_path.read_text(encoding="utf-8"))

    id2name = {c["id"]: c["name"] for c in level["categories"]}
    truth = {w.lower(): c["name"] for c in level["categories"] for w in c["words"]}
    guessed = {w.lower(): g["category"] for g in solution["groups"]
               for w in g["words"]}
    hes = {h["word"].lower(): h for h in solution.get("hesitations", [])}
    conf = {g["category"]: g.get("confidence") for g in solution["groups"]}

    mismatches = sorted(w for w in truth if guessed.get(w) != truth[w])

    trap_words = set()
    traps = []
    for t in level.get("traps", []):
        w = t["word"].lower()
        trap_words.add(w)
        traps.append({
            "word": w,
            "home": id2name.get(t["home"], t["home"]),
            "tempts": id2name.get(t["tempts"], t["tempts"]),
            "valid": guessed.get(w) == id2name.get(t["home"], t["home"]),
            "noticed": w in hes,
        })

    unplanned = [
        {"word": w, "also_fits": hes[w].get("also_fits"), "why": hes[w].get("why")}
        for w in sorted(hes) if w not in trap_words
    ]

    rare, unknown = [], []
    for w in sorted(truth):
        z = zipf.get(w)
        if z is None:
            unknown.append(w)
        elif z < RARE_ZIPF:
            rare.append({"word": w, "zipf": z})

    level_ids = [c["id"] for c in level["categories"]]
    related_pairs = []
    for a, b in combinations(level_ids, 2):
        rel_a = base_cats.get(a, {}).get("related", [])
        rel_b = base_cats.get(b, {}).get("related", [])
        if b in rel_a or a in rel_b:
            related_pairs.append([id2name.get(a, a), id2name.get(b, b)])

    board = level.get("board", {})
    return {
        "level": str(level_path.relative_to(ROOT)),
        "solver_verdict": "PASS" if not mismatches else "FAIL",
        "mismatches": mismatches,
        "categories_m": len(level["categories"]),
        "words_total": len(truth),
        "traps": traps,
        "traps_valid": sum(1 for t in traps if t["valid"]),
        "aha_moments": sum(1 for t in traps if t["valid"] and t["noticed"]),
        "unplanned_hesitations": unplanned,
        "rare_words": rare,
        "words_not_in_base": unknown,
        "move_limit_k": board.get("move_limit_k"),
        "move_limit": board.get("move_limit"),
        "repeats": level.get("repeats", []),
        "confidence": conf,
        "confidence_min": min((c for c in conf.values() if c is not None),
                              default=None),
        "related_pairs_from_base": related_pairs,
    }


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    base_cats, zipf = load_base()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for arg in argv[1:]:
        path = Path(arg).resolve()
        m = metrics(path, base_cats, zipf)
        out = OUT_DIR / (path.stem + ".metrics.json")
        out.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(f"{path.stem}: M={m['categories_m']} traps_valid={m['traps_valid']} "
              f"aha={m['aha_moments']} unplanned={len(m['unplanned_hesitations'])} "
              f"rare={len(m['rare_words'])} K={m['move_limit_k']} "
              f"repeats={len(m['repeats'])} conf_min={m['confidence_min']} "
              f"related={m['related_pairs_from_base']} -> {out.relative_to(ROOT)}")
        if m["words_not_in_base"]:
            print(f"  ! слов нет в базе (zipf неизвестен): {', '.join(m['words_not_in_base'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
