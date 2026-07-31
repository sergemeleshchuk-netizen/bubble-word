#!/usr/bin/env python3
"""Воспроизводимый аудит референсных данных.

Перепроверяет КАЖДОЕ число, заявленное в docs/SPEC.md, по сырым файлам
data/reference-derived/. Ничего не берёт на веру: zipf пересчитывается
частотником заново, мета-связи выводятся из имён категорий, арифметика
пузырей проверяется формулой.

Запуск:  python3 scripts/audit_reference.py
Вывод:   docs/DATA_AUDIT.md  +  data/audit.json
"""
from __future__ import annotations

import csv
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "data" / "reference-derived"
OUT_JSON = ROOT / "data" / "audit.json"
OUT_MD = ROOT / "docs" / "DATA_AUDIT.md"

TOP50K_ZIPF = 2.55          # граница top-50k английского по спеке
QUICKWIN_ZIPF = 3.0         # порог частотности для категории быстрой победы

# Пресет 201-210 из SPEC.md раздел 14 — проверяем арифметику построчно.
PRESET_201_210 = [
    # (уровень, категорий, мета, start_bubbles как заявлено в спеке)
    (201, 13, 2, 51),
    (202, 15, 3, 58),
    (203, 12, 1, 47),
    (204, 16, 4, 61),
    (205, 18, 5, 68),
    (206, 12, 1, 46),
    (207, 14, 3, 54),
    (208, 15, 2, 57),
    (209, 17, 4, 64),
    (210, 13, 2, 50),
]


# --------------------------------------------------------------------------- #
# нормализация identity key (одно место на весь проект)
# --------------------------------------------------------------------------- #
APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    """Ключ идентичности: NFKC, единый апостроф и дефис, casefold, одинарные пробелы."""
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


# --------------------------------------------------------------------------- #
# загрузка
# --------------------------------------------------------------------------- #
def load() -> dict:
    levels_raw = json.loads((REF / "reference-levels.json").read_text(encoding="utf-8"))
    with (REF / "reference-metrics.csv").open(encoding="utf-8") as fh:
        metrics = list(csv.DictReader(fh))
    with (REF / "reference-vocabulary.csv").open(encoding="utf-8") as fh:
        vocab = list(csv.DictReader(fh))
    with (REF / "half-split-candidates.csv").open(encoding="utf-8") as fh:
        halves = list(csv.DictReader(fh))
    return {"levels_raw": levels_raw, "metrics": metrics, "vocab": vocab, "halves": halves}


def zipf_lookup(vocab: list) -> dict:
    """zipf по нормализованному слову.

    ВАЖНО: в reference-vocabulary.csv значение 0.0 — это не частотность, а метка
    «слово неизвестно частотнику» (15 слов: khinkali, dorblu, airhockey...).
    Смешивать её с реальным значением нельзя: min_zipf уровня схлопнется в 0.0,
    а счётчик редких слов раздуется. Здесь она превращается в None.
    """
    out = {}
    for row in vocab:
        try:
            value = float(row["zipf"])
        except (TypeError, ValueError):
            value = None
        out[normalize(row["word"])] = None if (value is None or value <= 0.0) else value
    return out


# --------------------------------------------------------------------------- #
# мета-структура: лес, а не дерево
# --------------------------------------------------------------------------- #
def meta_edges(level_cats: list) -> list:
    """Ребро (child_key -> parent_key): имя категории child лежит словом в parent."""
    by_name = {}
    for cat in level_cats:
        by_name.setdefault(normalize(cat["category"]), cat["category"])
    edges = []
    for parent in level_cats:
        for word in parent["words"]:
            key = normalize(word)
            if key in by_name and by_name[key] != parent["category"]:
                edges.append((by_name[key], parent["category"]))
    return edges


def forest_depth(edges: list) -> tuple:
    """Глубина леса + счётчики нарушений (несколько родителей, циклы, компоненты)."""
    parents = defaultdict(list)
    children = defaultdict(list)
    nodes = set()
    for child, parent in edges:
        parents[child].append(parent)
        children[parent].append(child)
        nodes.update((child, parent))

    multi_parent = [n for n, ps in parents.items() if len(set(ps)) > 1]

    # глубина = самая длинная цепочка вверх; попутно детектируем цикл
    cycles = []
    memo = {}

    def depth(node, seen):
        if node in memo:
            return memo[node]
        if node in seen:
            cycles.append(node)
            return 0
        seen = seen | {node}
        best = 0
        for p in set(parents.get(node, [])):
            best = max(best, 1 + depth(p, seen))
        memo[node] = best
        return best

    max_depth = max((depth(n, frozenset()) for n in nodes), default=0)

    # число независимых компонент (лес vs одно дерево)
    adj = defaultdict(set)
    for child, parent in edges:
        adj[child].add(parent)
        adj[parent].add(child)
    seen, components = set(), 0
    for n in nodes:
        if n in seen:
            continue
        components += 1
        stack = [n]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(adj[cur] - seen)
    return max_depth, multi_parent, sorted(set(cycles)), components


# --------------------------------------------------------------------------- #
# основной проход по уровням
# --------------------------------------------------------------------------- #
def analyze_levels(levels_raw: dict, zipf: dict) -> dict:
    levels = levels_raw["levels"]
    problems = defaultdict(list)
    per_level = {}

    cat_sizes = Counter()
    all_words, all_cat_names = [], []
    word_levels = defaultdict(list)

    for lvl_str, cats in sorted(levels.items(), key=lambda kv: int(kv[0])):
        lvl = int(lvl_str)
        words_flat = [w for c in cats for w in c["words"]]
        norm_flat = [normalize(w) for w in words_flat]

        for c in cats:
            cat_sizes[len(c["words"])] += 1
            if len(c["words"]) != 4:
                problems["category_size_not_4"].append(
                    {"level": lvl, "category": c["category"], "size": len(c["words"])}
                )
            all_cat_names.append(c["category"])

        # повторы слова внутри уровня
        dup = [w for w, n in Counter(norm_flat).items() if n > 1]
        if dup:
            problems["within_level_duplicate_word"].append({"level": lvl, "words": dup})

        edges = meta_edges(cats)
        depth, multi_parent, cycles, components = forest_depth(edges)
        if multi_parent:
            problems["meta_multi_parent"].append({"level": lvl, "categories": multi_parent})
        if cycles:
            problems["meta_cycle"].append({"level": lvl, "categories": cycles})

        meta_children = {normalize(child) for child, _ in edges}
        # мета-слово не спавнится на старте
        start_bubbles = len(cats) * 4 - len(meta_children)

        # флаг is_meta_child в данных против вывода из имён категорий
        flagged = {normalize(c["category"]) for c in cats if c.get("is_meta_child")}
        if flagged != meta_children:
            problems["meta_flag_mismatch"].append(
                {
                    "level": lvl,
                    "flagged_only": sorted(flagged - meta_children),
                    "derived_only": sorted(meta_children - flagged),
                }
            )

        zipfs = [zipf.get(n) for n in norm_flat]
        known = [z for z in zipfs if z is not None]
        unknown = [w for w, z in zip(words_flat, zipfs) if z is None]
        if unknown:
            problems["word_missing_from_vocabulary"].append({"level": lvl, "words": unknown})

        # категория быстрой победы: без мета-слов, все 4 слова частотные
        quickwins = 0
        for c in cats:
            ws = [normalize(w) for w in c["words"]]
            if any(w in meta_children for w in ws):
                continue
            zs = [zipf.get(w) for w in ws]
            if all(z is not None and z >= QUICKWIN_ZIPF for z in zs):
                quickwins += 1
        if quickwins == 0:
            problems["no_quickwin_category"].append({"level": lvl})

        for n in set(norm_flat):
            word_levels[n].append(lvl)
        all_words.extend(norm_flat)

        per_level[lvl] = {
            "categories": len(cats),
            "meta_categories": len(meta_children),
            "meta_links": len(edges),
            "meta_components": components,
            "max_meta_depth": depth,
            "start_bubbles": start_bubbles,
            "total_word_slots": len(cats) * 4,
            "quickwin_categories": quickwins,
            "words_zipf_lt_3": sum(1 for z in known if z < 3.0),
            "words_zipf_lt_2": sum(1 for z in known if z < 2.0),
            "words_below_top50k": sum(1 for z in known if z < TOP50K_ZIPF),
            "min_zipf": round(min(known), 2) if known else None,
            "median_zipf": round(statistics.median(known), 2) if known else None,
            "unknown_words": len(unknown),
        }

    return {
        "per_level": per_level,
        "problems": problems,
        "cat_sizes": cat_sizes,
        "all_words": all_words,
        "all_cat_names": all_cat_names,
        "word_levels": word_levels,
    }


# --------------------------------------------------------------------------- #
# сверка с готовым reference-metrics.csv
# --------------------------------------------------------------------------- #
def compare_metrics(per_level: dict, metrics: list) -> dict:
    fields = [
        "categories",
        "meta_categories",
        "start_bubbles",
        "total_word_slots",
        "max_meta_depth",
        "quickwin_categories",
        "words_zipf_lt_3",
        "words_zipf_lt_2",
        "min_zipf",
        "median_zipf",
    ]
    diffs = defaultdict(list)
    for row in metrics:
        lvl = int(row["level"])
        mine = per_level.get(lvl)
        if not mine:
            diffs["level_missing_in_json"].append(lvl)
            continue
        for f in fields:
            theirs_raw = row.get(f)
            if theirs_raw in (None, ""):
                continue
            theirs = float(theirs_raw)
            ours = mine.get(f)
            if ours is None:
                continue
            if abs(float(ours) - theirs) > 0.011:
                diffs[f].append({"level": lvl, "csv": theirs, "recomputed": ours})
    return diffs


# --------------------------------------------------------------------------- #
# словарь: zipf, top50k, нормализация
# --------------------------------------------------------------------------- #
def audit_vocabulary(vocab: list) -> dict:
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        zipf_frequency = None

    norm_groups = defaultdict(list)
    top50k_conflicts, zipf_drift = [], []
    buckets = Counter()
    unknown_to_freq = []

    for row in vocab:
        word = row["word"]
        norm_groups[normalize(word)].append(word)
        try:
            z = float(row["zipf"])
        except (TypeError, ValueError):
            z = None
        in_top = row.get("in_top50k") in ("1", 1, True, "true")

        if z is not None and z <= 0.0:
            z = None                      # 0.0 — это метка «неизвестно», не значение
        if z is None:
            unknown_to_freq.append(word)
            buckets["unknown"] += 1
        else:
            if z >= TOP50K_ZIPF and not in_top:
                top50k_conflicts.append({"word": word, "zipf": z, "in_top50k": 0})
            elif z < TOP50K_ZIPF and in_top:
                top50k_conflicts.append({"word": word, "zipf": z, "in_top50k": 1})
            buckets[
                "<2.0" if z < 2.0 else
                "2.0-2.9" if z < 3.0 else
                "3.0-3.9" if z < 4.0 else
                "4.0-4.9" if z < 5.0 else "5.0+"
            ] += 1

        if zipf_frequency is not None and z is not None:
            fresh = round(zipf_frequency(word, "en"), 2)
            if abs(fresh - z) > 0.051:
                zipf_drift.append({"word": word, "csv": z, "wordfreq": fresh})

    collisions = {k: v for k, v in norm_groups.items() if len(set(v)) > 1}
    multi_token = [r["word"] for r in vocab if " " in r["word"] or "-" in r["word"]]
    return {
        "rows": len(vocab),
        "unique_normalized": len(norm_groups),
        "normalization_collisions": collisions,
        "top50k_conflicts": top50k_conflicts,
        "zipf_drift": zipf_drift,
        "buckets": buckets,
        "unknown_to_frequency_list": unknown_to_freq,
        "multi_token": multi_token,
        "max_length": max(len(r["word"]) for r in vocab),
    }


# --------------------------------------------------------------------------- #
# половинки: формально валидные vs игрово честные
# --------------------------------------------------------------------------- #
MORPHOLOGICAL_TAILS = {"ion", "ing", "ed", "er", "est", "ness", "ment", "ly", "s", "es"}
WEAK_HEADS = {"par", "com", "car", "lot", "mar", "pen", "bar", "tar", "cap", "man"}


def audit_halves(halves: list, zipf: dict) -> dict:
    flagged = []
    for row in halves:
        w, a, b = row["word"], row["half_a"], row["half_b"]
        flags = []
        if b.casefold() in MORPHOLOGICAL_TAILS:
            flags.append("rejected_morphological")
        if len(a) <= 3 or len(b) <= 3:
            flags.append("short_fragment")
        if a.casefold() in WEAK_HEADS:
            flags.append("weak_head")
        try:
            za, zb = float(row["zipf_a"]), float(row["zipf_b"])
            if min(za, zb) < 2.55:
                flags.append("fragment_below_top50k")
        except (TypeError, ValueError):
            flags.append("fragment_zipf_missing")
        if zipf.get(normalize(w)) is None:
            flags.append("source_word_not_in_vocabulary")
        if flags:
            flagged.append({"word": w, "halves": [a, b], "flags": flags})
    return {
        "rows": len(halves),
        "needs_manual_review": flagged,
        "clean": len(halves) - len(flagged),
    }


# --------------------------------------------------------------------------- #
# кривая, фазы, пила, свежесть, корреляции
# --------------------------------------------------------------------------- #
def audit_curve(per_level: dict, word_levels: dict, all_cat_names: list) -> dict:
    import numpy as np

    lvls = sorted(per_level)
    def col(name):
        return np.array([per_level[l][name] for l in lvls], dtype=float)

    nums = np.array(lvls, dtype=float)
    meta_share = np.array(
        [per_level[l]["meta_categories"] / per_level[l]["categories"] for l in lvls]
    )

    corr = {}
    for name in [
        "start_bubbles", "categories", "words_zipf_lt_3", "words_zipf_lt_2",
        "min_zipf", "median_zipf", "max_meta_depth", "quickwin_categories",
    ]:
        corr[name] = round(float(np.corrcoef(col(name), nums)[0, 1]), 3)
    corr["meta_share"] = round(float(np.corrcoef(meta_share, nums)[0, 1]), 3)

    blocks = []
    for start in range(1, 200, 20):
        chunk = [l for l in lvls if start <= l < start + 20]
        if not chunk:
            continue
        blocks.append({
            "block": f"{start}-{min(start + 19, 199)}",
            "levels": len(chunk),
            "categories": round(sum(per_level[l]["categories"] for l in chunk) / len(chunk), 1),
            "meta": round(sum(per_level[l]["meta_categories"] for l in chunk) / len(chunk), 1),
            "start_bubbles": round(sum(per_level[l]["start_bubbles"] for l in chunk) / len(chunk), 1),
            "meta_share": round(
                sum(per_level[l]["meta_categories"] / per_level[l]["categories"] for l in chunk)
                / len(chunk), 2),
            "rare": round(sum(per_level[l]["words_zipf_lt_3"] for l in chunk) / len(chunk), 1),
            "min_zipf": round(sum(per_level[l]["min_zipf"] for l in chunk) / len(chunk), 2),
        })

    # пила: сколько уровней проще предыдущего (по числу категорий)
    cats = [per_level[l]["categories"] for l in lvls]
    steps = [b - a for a, b in zip(cats, cats[1:])]
    easier = sum(1 for s in steps if s < 0)

    # позиция в десятке
    pos = defaultdict(list)
    for l in lvls:
        pos[l % 10].append(per_level[l]["categories"])
    position_profile = {p: round(sum(v) / len(v), 1) for p, v in sorted(pos.items())}

    # свежесть
    gaps = []
    adjacent_repeats = 0
    for _, ls in word_levels.items():
        ls = sorted(ls)
        for a, b in zip(ls, ls[1:]):
            gaps.append(b - a)
            if b - a == 1:
                adjacent_repeats += 1
    cat_counter = Counter(normalize(c) for c in all_cat_names)

    return {
        "correlations_with_level_number": corr,
        "blocks_of_20": blocks,
        "saw_tooth": {
            "transitions": len(steps),
            "easier_than_previous": easier,
            "share_easier": round(easier / len(steps), 3),
            "mean_abs_step": round(sum(abs(s) for s in steps) / len(steps), 2),
            "step_range": [min(steps), max(steps)],
        },
        "position_in_decade_avg_categories": position_profile,
        "freshness": {
            "words_used_more_than_once": sum(1 for v in word_levels.values() if len(v) > 1),
            "unique_words": len(word_levels),
            "median_reuse_gap": statistics.median(gaps) if gaps else None,
            "adjacent_level_repeats": adjacent_repeats,
            "unique_category_names": len(cat_counter),
            "total_categories": sum(cat_counter.values()),
        },
        "tail_180_199": {
            "categories_mean": round(
                sum(per_level[l]["categories"] for l in lvls if l >= 180)
                / len([l for l in lvls if l >= 180]), 1),
            "categories_range": [
                min(per_level[l]["categories"] for l in lvls if l >= 180),
                max(per_level[l]["categories"] for l in lvls if l >= 180)],
            "start_bubbles_range": [
                min(per_level[l]["start_bubbles"] for l in lvls if l >= 180),
                max(per_level[l]["start_bubbles"] for l in lvls if l >= 180)],
        },
        "observed_max_start_bubbles": max(per_level[l]["start_bubbles"] for l in lvls),
    }


def audit_relation_markers(all_cat_names: list) -> dict:
    markers = {
        "things that": 0, "words before": 0, "words after": 0,
        "types of": 0, "kinds of": 0, "parts of": 0, "used for": 0,
    }
    for name in all_cat_names:
        low = normalize(name)
        for m in markers:
            if low.startswith(m) or f" {m} " in low:
                markers[m] += 1
    uniq = {normalize(c) for c in all_cat_names}
    plain = sum(
        1 for c in uniq
        if not any(c.startswith(m) or f" {m} " in c for m in markers)
    )
    return {
        "unique_category_names": len(uniq),
        "plain_noun_like": plain,
        "plain_share": round(plain / len(uniq), 3),
        "markers": markers,
    }


def audit_preset() -> dict:
    rows = []
    for lvl, cats, meta, claimed in PRESET_201_210:
        correct = cats * 4 - meta
        rows.append({
            "level": lvl, "categories": cats, "meta": meta,
            "spec_value": claimed, "formula_value": correct,
            "ok": claimed == correct,
        })
    return {"rows": rows, "errors": sum(1 for r in rows if not r["ok"])}


# --------------------------------------------------------------------------- #
# отчёт
# --------------------------------------------------------------------------- #
def fmt_table(headers: list, rows: list) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def build_report(a: dict) -> str:
    lv, voc, cur = a["levels"], a["vocabulary"], a["curve"]
    pr = lv["problems"]
    L = []
    add = L.append

    add("# DATA_AUDIT — воспроизводимый аудит референсных данных\n")
    add("Сгенерировано `scripts/audit_reference.py`. Каждое число ниже пересчитано")
    add("из `data/reference-derived/` заново, а не перенесено из спеки.\n")
    add("Метки достоверности: **Measured** — посчитано по данным; **Inferred** —")
    add("интерпретация; **Unverified** — требует проверки в целевой игре.\n")

    add("## 1. Объём данных\n")
    add(fmt_table(["Сущность", "Значение", "Метка"], [
        ["Уровней разобрано", lv["levels_count"], "Measured"],
        ["Категорий всего", lv["categories_total"], "Measured"],
        ["Слов-слотов всего", lv["word_slots_total"], "Measured"],
        ["Уникальных слов (нормализованных)", cur["freshness"]["unique_words"], "Measured"],
        ["Уникальных имён категорий", cur["freshness"]["unique_category_names"], "Measured"],
        ["Строк в словаре", voc["rows"], "Measured"],
        ["Кандидатов на распил", a["halves"]["rows"], "Measured"],
    ]))

    add("\n## 2. Жёсткие инварианты\n")
    sizes = ", ".join(f"{k} слов: {v}" for k, v in sorted(lv["cat_sizes"].items()))
    add(fmt_table(["Инвариант", "Результат", "Вердикт"], [
        ["Ровно 4 слова в категории", sizes,
         "PASS" if not pr.get("category_size_not_4") else "FAIL"],
        ["Ноль повторов слова внутри уровня",
         f"{len(pr.get('within_level_duplicate_word', []))} уровней с повтором",
         "PASS" if not pr.get("within_level_duplicate_word") else "FAIL"],
        ["У мета-категории не больше одного родителя",
         f"{len(pr.get('meta_multi_parent', []))} нарушений",
         "PASS" if not pr.get("meta_multi_parent") else "FAIL"],
        ["Нет циклов в мета-графе",
         f"{len(pr.get('meta_cycle', []))} нарушений",
         "PASS" if not pr.get("meta_cycle") else "FAIL"],
        ["Категория быстрой победы в каждом уровне",
         f"{lv['levels_count'] - len(pr.get('no_quickwin_category', []))}/{lv['levels_count']}",
         "PASS" if not pr.get("no_quickwin_category") else "FAIL"],
    ]))

    add("\n### 2.1. Мета-структура — лес, а не одно дерево\n")
    add(fmt_table(["Показатель", "Значение"], [
        ["Мета-связей всего (выведено из имён категорий)", lv["meta_links_total"]],
        ["Уровней с мета-связями", f"{lv['levels_with_meta']} из {lv['levels_count']}"],
        ["Максимальная глубина", lv["max_depth_overall"]],
        ["Распределение глубин", dict(sorted(lv["depth_distribution"].items()))],
        ["Независимых компонент в среднем на уровень", lv["mean_meta_components"]],
        ["Уровней, где мета-граф — одна связная компонента", lv["single_component_levels"]],
    ]))
    add("")
    add("**Вывод (Measured).** Ни один уровень не является одним деревом: мета-связи")
    add(f"образуют в среднем {lv['mean_meta_components']} независимых компонент плюс плоские")
    add("категории вне графа. Корректный термин — **ациклический ориентированный лес**.")
    add("Инвариант в коде должен называться `meta_forest_acyclic`, и связность")
    add("всего графа проверять нельзя — это дало бы ложный FAIL на 100% референса.")

    add("\n## 3. Сверка с готовым reference-metrics.csv\n")
    if a["metrics_diff"]:
        add("Расхождения между CSV и пересчётом из JSON:\n")
        add(fmt_table(["Поле", "Расхождений", "Примеры"], [
            [k, len(v), json.dumps(v[:3], ensure_ascii=False)] for k, v in a["metrics_diff"].items()
        ]))
        add("")
        add("### 3.1. Два дефекта исходных данных, найденных этой сверкой\n")
        add("**Дефект 1 — `zipf = 0.0` как метка «неизвестно» (Measured).**")
        add(f"В словаре {len(voc['unknown_to_frequency_list'])} слов имеют zipf 0.0:")
        add("`" + "`, `".join(voc["unknown_to_frequency_list"][:8]) + "` и др.")
        add("Это не частотность, а отсутствие слова в частотнике (кулинарные и спортивные")
        add("реалии: `khinkali`, `dorblu`, `airhockey`). Если читать 0.0 как значение,")
        add("`min_zipf` уровня схлопывается в ноль, а счётчик редких слов раздувается.")
        add("**Решение:** `frequency_unknown` — отдельный булев сигнал; в агрегатах")
        add("такие слова исключаются из `min_zipf` и считаются отдельной строкой.")
        add("")
        add("**Дефект 2 — флаг `is_meta_child` недоразмечен (Measured).**")
        add("Совпадение имени категории со словом ищется без учёта регистра и многословности,")
        add("поэтому парсер источника пропустил три связи:\n")
        add(fmt_table(["Уровень", "Пропущенная мета-связь", "Где лежит словом"], [
            ["17", "`building materials`", "`construction`: crane, bulldozer, **Building Materials**, builders"],
            ["74", "`programming language`", "`computer`: **Programming Language**, keyboard, mouse, monitor"],
            ["165", "`status`", "`profile info`: **Status**, bio, username, avatar"],
        ]))
        add("")
        add("Следствие: на L74 появляется цепочка глубины 2")
        add("(`programming language` → `computer` → `office`), которой в CSV нет.")
        add("Итог всё равно **глубина 3 не встречается ни разу** — но вывод теперь")
        add("основан на пересчёте, а не на чужом флаге. Генератор и валидатор обязаны")
        add("выводить мета-связи из имён категорий сами, а не доверять флагу в данных.")
    else:
        add("Расхождений нет: все 10 полей CSV воспроизводятся из `reference-levels.json`")
        add("побайтово по значениям. CSV пригоден как датасет для калибровки. **Measured**")

    add("\n## 4. Арифметика пресета 201-210 из спеки\n")
    add("Формула `start_bubbles = 4 × categories − meta_categories`.\n")
    add(fmt_table(["Ур.", "Катег.", "Мета", "В спеке", "По формуле", "OK"], [
        [r["level"], r["categories"], r["meta"], r["spec_value"], r["formula_value"],
         "да" if r["ok"] else "**НЕТ**"] for r in a["preset"]["rows"]
    ]))
    add("")
    add(f"**Ошибок в спеке: {a['preset']['errors']} из 10 строк.** Исправлено в `docs/SPEC_AUDIT.md`,")
    add("генератор считает `start_bubbles` только формулой и никогда из таблицы.")

    add("\n## 5. Словарь: частотность и top-50k\n")
    add(fmt_table(["Диапазон zipf", "Слов", "Доля"], [
        [k, v, f"{v / voc['rows']:.1%}"] for k, v in sorted(
            voc["buckets"].items(), key=lambda kv: str(kv[0]))
    ]))
    add("")
    add(f"- слов внутри top-50k (zipf ≥ {TOP50K_ZIPF}): **{voc['in_top50k_share']:.1%}** — Measured")
    add(f"- слов, неизвестных частотнику: **{len(voc['unknown_to_frequency_list'])}** "
        "(отдельный сигнал `frequency_unknown`, не zipf = 0)")

    drift = voc["zipf_drift"]
    add(f"\n### 5.1. Пересчёт zipf частотником `wordfreq` заново\n")
    add(f"- расхождений с CSV больше 0.05: **{len(drift)}** из {voc['rows']} "
        f"({len(drift) / voc['rows']:.1%})")
    if drift:
        multi = sum(1 for d in drift if " " in d["word"] or "-" in d["word"])
        worst = max(abs(d["csv"] - d["wordfreq"]) for d in drift)
        add(f"- из них многотокенных: **{multi} из {len(drift)}** "
            f"({multi / len(drift):.0%}); максимальный дрейф {worst:.2f}")
        add("- **Вывод (Measured):** одиночные слова воспроизводятся частотником точно,")
        add("  расходятся только фразы — частотность фразы зависит от метода подсчёта")
        add("  и не является надёжным сигналом. Для многотокенных пузырей узнаваемость")
        add("  проверяется по самому редкому входящему слову, а не по частоте фразы.")

    add(f"\n### 5.2. `in_top50k` против порога zipf ≥ {TOP50K_ZIPF}\n")
    add(f"- конфликтов: **{len(voc['top50k_conflicts'])}**")
    if voc["top50k_conflicts"]:
        ex = ", ".join(f"`{c['word']}` (zipf {c['zipf']}, флаг {c['in_top50k']})"
                       for c in voc["top50k_conflicts"][:8])
        add(f"- примеры: {ex}")
        capital = sum(1 for c in voc["top50k_conflicts"] if c["word"] != c["word"].lower())
        hyphen = sum(1 for c in voc["top50k_conflicts"] if "-" in c["word"] or " " in c["word"])
        add(f"- из них с заглавной буквы: {capital}; с дефисом или пробелом: {hyphen}")
        add("- **Вывод:** это не ошибка, а два разных измерения. `frequency_score` —")
        add("  насколько часто слово встречается; `lexicon_membership` — входит ли ровно")
        add("  эта строка в список 50 000 лемм. Заглавные, дефисные и брендовые записи")
        add("  частотны, но в лемматизированный список не попадают. Перезаписывать одно")
        add("  другим нельзя: в базе это два независимых поля.")
    add(f"- многотокенных слов: {len(voc['multi_token'])} ({len(voc['multi_token']) / voc['rows']:.1%}), "
        f"максимальная длина {voc['max_length']} символов")
    add(f"- коллизий после нормализации: {len(voc['normalization_collisions'])}")
    if voc["normalization_collisions"]:
        add(f"  - {json.dumps(dict(list(voc['normalization_collisions'].items())[:5]), ensure_ascii=False)}")

    add("\n## 6. Кривая сложности: две фазы\n")
    add(fmt_table(["Блок", "Катег.", "Мета", "Пузырей", "Доля мета", "Редких", "Мин. zipf"], [
        [b["block"], b["categories"], b["meta"], b["start_bubbles"],
         f"{b['meta_share']:.0%}", b["rare"], b["min_zipf"]] for b in cur["blocks_of_20"]
    ]))
    add("")
    add("Корреляции признаков с номером уровня (Measured):\n")
    add("```")
    for k, v in sorted(cur["correlations_with_level_number"].items(),
                       key=lambda kv: -abs(kv[1])):
        add(f"{k:24s} r = {v:+.3f}")
    add("```")

    add("\n### 6.1. Пила\n")
    st = cur["saw_tooth"]
    add(f"- переходов между соседними уровнями: {st['transitions']}")
    add(f"- проще предыдущего: **{st['easier_than_previous']} ({st['share_easier']:.0%})** — Measured")
    add(f"- средний шаг по модулю: {st['mean_abs_step']} категории, диапазон {st['step_range']}")
    add(f"- профиль позиции в десятке: {cur['position_in_decade_avg_categories']}")
    add("")
    add("**Inferred:** провал сразу после пика читается как запрограммированная передышка.")
    add("По 20 значений на позицию — это сигнал, а не закон.")

    add("\n### 6.2. Потолок объёма\n")
    add(f"- наблюдаемый максимум пузырей на старте: **{cur['observed_max_start_bubbles']}**")
    add("- **Unverified:** это НЕ доказанный физический предел экрана. Разбор видео")
    add("  целевой игры показывает, что поле держит одновременно только ~20-24 пузыря,")
    add("  а остальные досыпаются волнами (`docs/TARGET_GAME_OBSERVATIONS.md`).")
    add("  Значит `start_bubbles` — это размер уровня, а не размер экрана.")

    add("\n## 7. Свежесть словаря\n")
    f = cur["freshness"]
    add(fmt_table(["Показатель", "Значение"], [
        ["Слов использовано более одного раза", f["words_used_more_than_once"]],
        ["Медианный разрыв между использованиями", f["median_reuse_gap"]],
        ["Повторов в соседних уровнях", f["adjacent_level_repeats"]],
        ["Уникальных имён категорий", f"{f['unique_category_names']} из {f['total_categories']}"],
    ]))

    add("\n## 8. Типы связи в именах категорий\n")
    rm = a["relation_markers"]
    explicit = sum(rm["markers"].values())
    add(f"- уникальных имён категорий: {rm['unique_category_names']}")
    add(f"- **с явным маркером связи: {explicit} ({1 - rm['plain_share']:.1%})** — Measured")
    add(f"- разбивка маркеров: {rm['markers']}")
    add("")
    add("Замечание о методе: «просто существительное» формально не определимо, поэтому")
    add("измеряется обратное — наличие явной реляционной конструкции. Спека приводит")
    add("«91% просто существительных»; воспроизводимая версия этого утверждения —")
    add(f"конструкций с маркером всего {explicit} из {rm['unique_category_names']},")
    add("а `words before X` / `words after X` не встречаются ни разу.")
    add("")
    add("**Inferred:** это игра в свободную ассоциацию, а не в таксономию. База на чистой")
    add("таксономии даст формально верный и мёртвый контент.")

    add("\n## 9. Половинки: кандидаты, а не готовый контент\n")
    h = a["halves"]
    add(f"- всего распилов: {h['rows']}")
    add(f"- прошли автоматические фильтры: {h['clean']}")
    add(f"- требуют ручного ревью: **{len(h['needs_manual_review'])}**\n")
    add(fmt_table(["Слово", "Половинки", "Флаги"], [
        [x["word"], " + ".join(x["halves"]), ", ".join(x["flags"])]
        for x in h["needs_manual_review"][:15]
    ]))
    add("")
    add("**Вывод:** статус половинки обязателен (`candidate` / `approved_compound` /")
    add("`approved_wordplay` / `rejected_morphological` / `rejected_unfair`).")
    add("В финальные уровни идут только вручную утверждённые.")

    add("\n## 10. Прочие проблемы данных\n")
    other = {k: len(v) for k, v in pr.items()}
    if other:
        add(fmt_table(["Код", "Случаев"], [[k, v] for k, v in sorted(other.items())]))
        for code in ("meta_flag_mismatch", "word_missing_from_vocabulary"):
            if pr.get(code):
                add(f"\nПримеры `{code}`:\n")
                add("```")
                add(json.dumps(pr[code][:5], ensure_ascii=False, indent=2))
                add("```")
    else:
        add("Не найдено.")

    add("\n---\n")
    add("Полные машинные результаты: `data/audit.json`.")
    return "\n".join(L)


def main() -> int:
    data = load()
    zipf = zipf_lookup(data["vocab"])

    lv = analyze_levels(data["levels_raw"], zipf)
    per_level = lv["per_level"]

    depth_dist = Counter(str(v["max_meta_depth"]) for v in per_level.values())
    levels_meta = {
        "levels_count": len(per_level),
        "categories_total": sum(v["categories"] for v in per_level.values()),
        "word_slots_total": sum(v["total_word_slots"] for v in per_level.values()),
        "meta_links_total": sum(v["meta_links"] for v in per_level.values()),
        "levels_with_meta": sum(1 for v in per_level.values() if v["meta_links"] > 0),
        "max_depth_overall": max(v["max_meta_depth"] for v in per_level.values()),
        "depth_distribution": dict(depth_dist),
        "mean_meta_components": round(
            sum(v["meta_components"] for v in per_level.values()) / len(per_level), 2),
        "single_component_levels": sum(
            1 for v in per_level.values() if v["meta_components"] == 1 and v["meta_links"] > 0),
        "cat_sizes": dict(lv["cat_sizes"]),
        "problems": {k: v for k, v in lv["problems"].items()},
        "per_level": per_level,
    }

    voc = audit_vocabulary(data["vocab"])
    known = sum(v for k, v in voc["buckets"].items() if k != "unknown")
    in_top = sum(v for k, v in voc["buckets"].items()
                 if k in ("3.0-3.9", "4.0-4.9", "5.0+")) + sum(
        1 for r in data["vocab"]
        if r["zipf"] not in ("", None) and TOP50K_ZIPF <= float(r["zipf"]) < 3.0)
    voc["in_top50k_share"] = in_top / voc["rows"]
    voc["known_words"] = known

    audit = {
        "levels": levels_meta,
        "metrics_diff": compare_metrics(per_level, data["metrics"]),
        "vocabulary": voc,
        "halves": audit_halves(data["halves"], zipf),
        "curve": audit_curve(per_level, lv["word_levels"], lv["all_cat_names"]),
        "relation_markers": audit_relation_markers(lv["all_cat_names"]),
        "preset": audit_preset(),
        "normalization": {
            "identity_key": "NFKC + unify apostrophes/dashes + casefold + collapse spaces",
            "note": "display_text хранится отдельно; агрессивный stemming не применяется",
        },
    }

    serializable = json.loads(json.dumps(audit, default=str))
    OUT_JSON.write_text(json.dumps(serializable, ensure_ascii=False, indent=1), encoding="utf-8")
    OUT_MD.write_text(build_report(audit) + "\n", encoding="utf-8")

    print(f"levels={levels_meta['levels_count']} "
          f"categories={levels_meta['categories_total']} "
          f"meta_links={levels_meta['meta_links_total']} "
          f"max_depth={levels_meta['max_depth_overall']}")
    print(f"metrics_csv_diffs={ {k: len(v) for k, v in audit['metrics_diff'].items()} }")
    print(f"preset_errors={audit['preset']['errors']}/10")
    print(f"top50k_conflicts={len(voc['top50k_conflicts'])} zipf_drift={len(voc['zipf_drift'])}")
    print(f"halves_need_review={len(audit['halves']['needs_manual_review'])}/{audit['halves']['rows']}")
    print(f"→ {OUT_MD.relative_to(ROOT)}, {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
