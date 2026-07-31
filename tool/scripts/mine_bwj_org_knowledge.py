#!/usr/bin/env python3
"""Извлечение ЗНАНИЙ из выгрузки оригинала (1025 уровней), а не контента.

Разница принципиальная. Слова и четвёрки оригинала — чужой контент, в нашу базу
они не идут (эпизод импорта откачен, разбор в levels/packs/tool-test/DIFF-VS-REF.md).
А вот закономерности — как устроена таксономия категорий, какого размера пулы,
когда вводятся многословные ответы, как часто категория оказывается вложенной
в другую — это знание, и оно переносится законно.

Считает по `reference/bwj-org/levels.jsonl` (выгрузка, в git не хранится):

  1. таксономия: вложенность, мета-хабы, ветвление
  2. имена категорий: шаблоны, длина, типы правил
  3. пулы: размер, форма слов, повторы
  4. кривая по декадам: что растёт, что стоит на месте
  5. переиспользование: имена категорий и слова между уровнями
  6. разрезание тем: как оригинал делает из VEGETABLES -> ROOT VEGETABLES

Выход: markdown-отчёт в stdout (его и кладём в docs/), плюс --json для машин.

Запуск: python3 tool/scripts/mine_bwj_org_knowledge.py [--json путь]
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRAPE = ROOT / "reference" / "bwj-org" / "levels.jsonl"

# Шаблоны имён: по ним видно, какой ТИП правила у категории.
NAME_PATTERNS = [
    ("игра слов: ___ X / X ___", re.compile(r"^(words? (before|after)|___)\b|\b___\b")),
    ("типы/виды X", re.compile(r"^(types? of|kinds? of|sorts? of)\b")),
    ("части X", re.compile(r"^(parts? of|pieces? of)\b")),
    ("X things / things X", re.compile(r"\bthings\b")),
    ("свойство: X-ые", re.compile(r"^(hard|soft|round|cold|hot|sweet|sour|loud|quiet|"
                                  r"tall|small|big|long|short|fast|slow|shiny|sticky)\b")),
    ("место: in/at the X", re.compile(r"\b(in|at|on) the\b")),
    ("профессия/роль", re.compile(r"\b(jobs?|workers?|professions?|roles?|players?)\b")),
    ("бренды/имена", re.compile(r"\b(brands?|names?|makes?|companies)\b")),
]


def load() -> list[dict]:
    if not SCRAPE.exists():
        sys.exit(f"нет выгрузки {SCRAPE}\n"
                 "собрать: python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025")
    return sorted((json.loads(line) for line in SCRAPE.read_text(encoding="utf-8").splitlines()
                   if line.strip()), key=lambda x: x["level"])


def decade(level: int) -> int:
    return (level - 1) // 10 * 10 + 1


def analyse(levels: list[dict]) -> dict:
    out: dict = {}

    cat_first_level: dict[str, int] = {}
    cat_levels: dict[str, list[int]] = defaultdict(list)
    cat_pools: dict[str, list[tuple[str, ...]]] = defaultdict(list)
    word_categories: dict[str, set[str]] = defaultdict(set)
    word_levels: dict[str, list[int]] = defaultdict(list)

    depth_hist = Counter()
    children_per_parent = Counter()
    parent_own_words = Counter()
    meta_per_level = []
    levels_with_meta = 0
    pool_sizes = Counter()

    for lvl in levels:
        n = lvl["level"]
        metas = 0
        for cat in lvl["categories"]:
            name = cat["name"]
            cat_levels[name].append(n)
            cat_first_level.setdefault(name, n)
            cat_pools[name].append(tuple(sorted(cat["words"])))
            depth_hist[cat["depth"]] += 1
            pool_sizes[len(cat["words"])] += 1
            kids = cat.get("meta_words") or []
            if kids:
                children_per_parent[len(kids)] += 1
                parent_own_words[len(cat["words"]) - len(kids)] += 1
                metas += len(kids)
            for w in cat["words"]:
                word_categories[w].add(name)
                word_levels[w].append(n)
        meta_per_level.append(metas)
        if metas:
            levels_with_meta += 1

    out["levels"] = len(levels)
    out["category_occurrences"] = sum(len(l["categories"]) for l in levels)
    out["unique_categories"] = len(cat_levels)
    out["unique_words"] = len(word_categories)

    # 1. таксономия
    out["taxonomy"] = {
        "depth_hist": dict(sorted(depth_hist.items())),
        "children_per_parent": dict(sorted(children_per_parent.items())),
        "parent_own_words": dict(sorted(parent_own_words.items())),
        "levels_with_meta_share": round(levels_with_meta / len(levels), 3),
        "meta_per_level_mean": round(statistics.mean(meta_per_level), 2),
        "meta_per_level_max": max(meta_per_level),
    }

    # 2. имена категорий
    name_lengths = Counter(len(name.split()) for name in cat_levels)
    pattern_hits = Counter()
    for name in cat_levels:
        matched = False
        for label, rx in NAME_PATTERNS:
            if rx.search(name):
                pattern_hits[label] += 1
                matched = True
        if not matched:
            pattern_hits["простое имя группы"] += 1
    out["names"] = {
        "words_in_name": dict(sorted(name_lengths.items())),
        "patterns": dict(pattern_hits.most_common()),
    }

    # 3. пулы и переиспользование
    reused = {name: lv for name, lv in cat_levels.items() if len(lv) > 1}
    pool_variation = 0
    for name, pools in cat_pools.items():
        if len(set(pools)) > 1:
            pool_variation += 1
    out["pools"] = {
        "pool_sizes": dict(sorted(pool_sizes.items())),
        "categories_reused": len(reused),
        "categories_reused_share": round(len(reused) / len(cat_levels), 3),
        "reuse_times_mean": round(statistics.mean([len(v) for v in reused.values()]), 2)
        if reused else 0,
        "categories_with_varying_pool": pool_variation,
        "distinct_pools_of_top": sorted(
            ((name, len(set(pools))) for name, pools in cat_pools.items()),
            key=lambda kv: -kv[1])[:10],
    }

    # 4. слова-хабы
    hubs = sorted(((w, len(cats)) for w, cats in word_categories.items()),
                  key=lambda kv: -kv[1])
    out["word_hubs"] = {
        "words_in_2plus_categories": sum(1 for _, n in hubs if n >= 2),
        "share": round(sum(1 for _, n in hubs if n >= 2) / len(hubs), 3),
        "top": hubs[:15],
    }

    # 5. кривая по декадам: что растёт
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        sys.exit("нужен wordfreq")

    def zipf(word: str) -> float:
        parts = [p for p in re.split(r"[ \-']+", word) if p]
        values = [zipf_frequency(p, "en") for p in parts] or [0.0]
        return min(values) if len(parts) > 1 else values[0]

    by_decade: dict[int, dict] = {}
    seen_names: set[str] = set()
    seen_words: set[str] = set()
    for lvl in levels:
        d = decade(lvl["level"])
        bucket = by_decade.setdefault(d, {"cats": [], "zipfs": [], "multi": 0, "words": 0,
                                          "long": 0, "meta": [], "new_names": 0,
                                          "names": 0, "repeat_words": 0})
        bucket["cats"].append(len(lvl["categories"]))
        metas = 0
        for cat in lvl["categories"]:
            bucket["names"] += 1
            if cat["name"] not in seen_names:
                bucket["new_names"] += 1
                seen_names.add(cat["name"])
            metas += len(cat.get("meta_words") or [])
            for w in cat["words"]:
                bucket["words"] += 1
                z = zipf(w)
                if z > 0:
                    bucket["zipfs"].append(z)
                if " " in w or "-" in w:
                    bucket["multi"] += 1
                if len(w.replace(" ", "")) > 9:
                    bucket["long"] += 1
                if w in seen_words:
                    bucket["repeat_words"] += 1
                seen_words.add(w)
        bucket["meta"].append(metas)

    out["decades"] = {}
    for d in sorted(by_decade):
        b = by_decade[d]
        out["decades"][d] = {
            "cats_mean": round(statistics.mean(b["cats"]), 1),
            "zipf_median": round(statistics.median(b["zipfs"]), 2),
            "rare_share": round(sum(1 for z in b["zipfs"] if z < 3) / len(b["zipfs"]), 3),
            "multiword_share": round(b["multi"] / b["words"], 3),
            "long_share": round(b["long"] / b["words"], 3),
            "meta_mean": round(statistics.mean(b["meta"]), 1),
            "new_name_share": round(b["new_names"] / b["names"], 3),
            "repeat_word_share": round(b["repeat_words"] / b["words"], 3),
        }

    # 6. разрезание тем: имя-надмножество и имя-уточнение
    splits = []
    names = sorted(cat_levels)
    by_head: dict[str, list[str]] = defaultdict(list)
    for name in names:
        head = name.split()[-1]
        by_head[head].append(name)
    for head, group in by_head.items():
        if len(group) < 2:
            continue
        base = [g for g in group if g == head]
        if base and len(group) > 1:
            splits.append((head, sorted(g for g in group if g != head)[:6],
                           cat_first_level.get(head)))
    out["theme_splits"] = {
        "families": len(splits),
        "examples": sorted(splits, key=lambda s: -len(s[1]))[:12],
    }

    return out


def markdown(data: dict) -> str:
    t = data["taxonomy"]
    lines = [
        "# Что выгрузка оригинала говорит о структуре контента",
        "",
        "Замер по 1025 уровням (`reference/bwj-org/`, второй фанатский источник",
        "ответов, в git не хранится). Скрипт: `tool/scripts/mine_bwj_org_knowledge.py`.",
        "",
        "Здесь только ЗАКОНОМЕРНОСТИ. Слова и четвёрки оригинала — чужой контент,",
        "в базу не идут: эпизод импорта откачен, разбор в",
        "`levels/packs/tool-test/DIFF-VS-REF.md`.",
        "",
        f"Объём источника: {data['levels']} уровней, "
        f"{data['category_occurrences']} категорий-вхождений, "
        f"{data['unique_categories']} уникальных имён категорий, "
        f"{data['unique_words']} уникальных слов.",
        "",
        "## 1. Таксономия: категории вложены друг в друга",
        "",
        "Главное отличие от нашей базы. У нас плоский список категорий. У оригинала",
        "категория может быть РЕБЁНКОМ другой: её имя лежит пузырём в родителе, и",
        "собрав родителя, игрок получает подсказку к ребёнку.",
        "",
        "| глубина вложенности | категорий |",
        "|---|---:|",
    ]
    for depth, count in t["depth_hist"].items():
        lines.append(f"| {depth} | {count} |")
    lines += [
        "",
        "Сколько детей у родителя (то есть сколько из четырёх пузырей — имена категорий):",
        "",
        "| детей | родителей |",
        "|---|---:|",
    ]
    for kids, count in t["children_per_parent"].items():
        lines.append(f"| {kids} | {count} |")
    lines += [
        "",
        "Крайний случай — родитель без собственных слов: все четыре пузыря это имена",
        "вложенных категорий (`MEASUREMENTS` = TIME / LENGTH / WEIGHT / TEMPERATURE).",
        "",
        f"Уровней с хотя бы одной мета-парой: **{t['levels_with_meta_share'] * 100:.0f}%**, "
        f"в среднем {t['meta_per_level_mean']} на уровень, максимум {t['meta_per_level_max']}.",
        "",
        "## 2. Имена категорий",
        "",
        "| слов в имени | категорий |",
        "|---|---:|",
    ]
    for n, count in data["names"]["words_in_name"].items():
        lines.append(f"| {n} | {count} |")
    lines += ["", "Типы правил, видимые по имени:", "", "| шаблон | категорий |", "|---|---:|"]
    for label, count in data["names"]["patterns"].items():
        lines.append(f"| {label} | {count} |")

    p = data["pools"]
    lines += [
        "",
        "## 3. Пулы и переиспользование категорий",
        "",
        f"Категория переиспользуется на разных уровнях: **{p['categories_reused']}** имён "
        f"({p['categories_reused_share'] * 100:.0f}%), в среднем {p['reuse_times_mean']} раза.",
        f"При этом у **{p['categories_with_varying_pool']}** из них пул РАЗНЫЙ — то есть имя",
        "возвращается с другими четырьмя словами.",
        "",
        "Вывод для нашей базы: пул категории обязан быть глубже четвёрки. Оригиналу",
        "хватает четырёх, потому что он раскладку не пересобирает; нам нужен запас,",
        "чтобы одна категория давала разные четвёрки на разных уровнях.",
        "",
        "Категории с самым «текучим» пулом:",
        "",
    ]
    for name, count in p["distinct_pools_of_top"]:
        lines.append(f"- `{name}`: {count} разных четвёрок")

    h = data["word_hubs"]
    lines += [
        "",
        "## 4. Слова-хабы (материал ловушек)",
        "",
        f"Слов, живущих в 2+ категориях: **{h['words_in_2plus_categories']}** "
        f"({h['share'] * 100:.0f}% словаря).",
        "",
        "| слово | в скольких категориях |",
        "|---|---:|",
    ]
    for word, count in h["top"]:
        lines.append(f"| {word} | {count} |")

    lines += [
        "",
        "## 5. Кривая по декадам",
        "",
        "| декада | кат | zipf med | редк | мног | дл>9 | мета | новых имён | повторов слов |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for d, row in data["decades"].items():
        lines.append(
            f"| {d}-{d + 9} | {row['cats_mean']} | {row['zipf_median']} | "
            f"{row['rare_share'] * 100:.0f}% | {row['multiword_share'] * 100:.0f}% | "
            f"{row['long_share'] * 100:.0f}% | {row['meta_mean']} | "
            f"{row['new_name_share'] * 100:.0f}% | {row['repeat_word_share'] * 100:.0f}% |")

    s = data["theme_splits"]
    lines += [
        "",
        "## 6. Разрезание тем",
        "",
        f"Семейств «общая категория + её уточнения»: **{s['families']}**. Оригинал не",
        "выдумывает новую тему на каждый уровень — он режет уже сыгранную:",
        "",
    ]
    for head, kids, first in s["examples"]:
        first_txt = f" (дебют на L{first})" if first else ""
        lines.append(f"- `{head}`{first_txt} → {', '.join('`' + k + '`' for k in kids)}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", help="куда сложить сырые числа")
    args = parser.parse_args()

    data = analyse(load())
    if args.json:
        Path(args.json).write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                                   encoding="utf-8")
    print(markdown(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
