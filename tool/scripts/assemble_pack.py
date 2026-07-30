#!/usr/bin/env python3
"""Сборщик пакета уровней из базы по плану (механическая часть level-generator).

Вход: план пакета JSON:
{
  "pack": "volume1", "out_dir": "levels/packs/volume1",
  "levels": [
    { "level_id": 200, "difficulty_target": 5, "k": 1.5,
      "cats": ["fruits", "colors", ...],
      "traps": [{"word": "orange", "home": "fruits", "tempts": "colors"}],
      "must": {"seasons": ["winter"]} }
  ]
}

Умная часть (выбор категорий, ловушек, кривой) - за скиллом level-generator,
скрипт лишь честно раскладывает слова:
- слово ловушки кладётся в home и исключается из tempts;
- слово, живущее в базовом пуле ДРУГОЙ категории уровня, не берётся без
  объявленной ловушки (защита от незаявленной двусмысленности);
- слово, игравшее в прошлых уровнях пакета в другой категории, объявляется
  repeat (максимум 2 на уровень, дальше кандидат пропускается);
- лимит: move_limit = ceil(3*M*K); start_bubbles = min(24, 4M).

Запуск: python3 tool/scripts/assemble_pack.py levels/packs/volume1/plan.json
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tool" / "data" / "categories.json"
MAX_REPEATS = 2


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    plan_path = ROOT / sys.argv[1]
    plan = json.loads(plan_path.read_text())
    base = json.loads(BASE.read_text())
    cats = {c["id"]: c for c in base["categories"]}
    out_dir = ROOT / plan["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    history = {}  # слово -> (level_id, category_id) первое появление в пакете
    problems = []
    for spec in plan["levels"]:
        lid, ids = spec["level_id"], spec["cats"]
        m = len(ids)
        for cid in ids:
            if cid not in cats:
                problems.append(f"L{lid}: категории '{cid}' нет в базе")
        if problems:
            continue
        pools = {cid: [w["w"] for w in sorted(cats[cid]["words"],
                                              key=lambda w: -w["zipf"])] for cid in ids}
        trap_home = {}   # word -> home cat
        trap_block = {}  # word -> tempts cat (не класть туда)
        for t in spec.get("traps", []):
            trap_home[t["word"]] = t["home"]
            trap_block[t["word"]] = t["tempts"]

        used, words_by_cat, repeats = set(), {}, []
        for cid in ids:
            forced = [w for w, h in trap_home.items() if h == cid]
            forced += [w for w in spec.get("must", {}).get(cid, []) if w not in forced]
            chosen = []
            for w in forced:
                if w not in pools[cid]:
                    problems.append(f"L{lid}/{cid}: обязательного '{w}' нет в пуле базы")
                chosen.append(w)
                used.add(w)
            for w in pools[cid]:
                if len(chosen) >= 4:
                    break
                if w in used or w in chosen:
                    continue
                if w in trap_home and trap_home[w] != cid:
                    continue  # слово ловушки живёт только в home
                if trap_block.get(w) == cid:
                    continue
                # незаявленная двусмысленность: слово в базовом пуле другой категории уровня
                others = [o for o in ids if o != cid and w in pools[o]]
                if others:
                    continue
                # повтор из истории пакета
                if w in history and history[w][1] != cid:
                    if sum(1 for r in repeats) >= MAX_REPEATS:
                        continue
                    repeats.append({"word": w, "prev_level": history[w][0],
                                    "prev_category": history[w][1]})
                chosen.append(w)
                used.add(w)
            if len(chosen) != 4:
                problems.append(f"L{lid}/{cid}: набрал только {len(chosen)} слова из 4")
            # принудительные слова (ловушки, must) тоже честно объявляем повторами
            for w in chosen:
                if w in history and history[w][1] != cid and \
                        not any(r["word"] == w for r in repeats):
                    repeats.append({"word": w, "prev_level": history[w][0],
                                    "prev_category": history[w][1]})
            words_by_cat[cid] = chosen

        k = spec["k"]
        level = {
            "level_id": lid,
            "difficulty_target": spec["difficulty_target"],
            "categories": [{"id": cid, "name": cats[cid]["name"],
                            "words": words_by_cat.get(cid, [])} for cid in ids],
            "traps": spec.get("traps", []),
            "repeats": repeats,
            "board": {"start_bubbles": min(24, 4 * m),
                      "move_limit": math.ceil(3 * m * k), "move_limit_k": k},
            "extensions": {"chunks": [], "chains": None, "picture_words": []},
        }
        out = out_dir / f"l{lid}.json"
        out.write_text(json.dumps(level, ensure_ascii=False, indent=2) + "\n")
        # память игрока работает от ПОСЛЕДНЕГО появления слова
        for cid in ids:
            for w in words_by_cat.get(cid, []):
                history[w] = (lid, cid)
        print(f"L{lid}: {m} категорий, лимит {level['board']['move_limit']}, "
              f"ловушек {len(level['traps'])}, повторов {len(repeats)} -> {out.relative_to(ROOT)}")

    if problems:
        print("\nПРОБЛЕМЫ ПЛАНА:")
        for p in problems:
            print(" -", p)
        sys.exit(1)


if __name__ == "__main__":
    main()
