#!/usr/bin/env python3
"""Третий источник контента: сводная база — наша разметка плюс словарь оригинала.

    content.snapshot.json  ┐
    reference.snapshot.json├─(этот скрипт)─> hybrid.snapshot.json
    reference/…/levels.jsonl ┘                        |
                                              статика в браузере

Зачем третий источник
--------------------------------------------------------------------------
Первые два отвечают на разные вопросы и оба — половинчато.

  наша база          1317 категорий, каждая выращена под правила генератора:
                     статусы связей, значения слов, регистр слова, запреты пар.
                     Разметка есть, широты нет.
  словарь оригинала  6714 категорий, отыгранных в живой игре 1025 уровней.
                     Широта есть, разметки нет вовсе: все связи приезжают
                     approved, регистр слова потерян, значений нет.

Сводная база — это широта оригинала, пропущенная через нашу разметку. Категорий
столько же, сколько у оригинала, плюс наши; но слово попадает в уровень не
потому, что оригинал когда-то его засчитал, а потому, что у него есть ВЕС.

Что такое вес и почему он здесь главный
--------------------------------------------------------------------------
У нашей базы главный фильтр словаря — регистр слова (`everyday` / `passive` /
`specialist`, шаг 010 пайплайна): им отсекается `quail` и `obituary`, на которые
жаловался владелец продукта. У оригинала регистра нет — и это не мелочь: 8786
слов выгрузки нашей разметки не имеют вовсе, то есть на источнике «словарь
оригинала» главный фильтр не работает ни для одного из них.

Вес слова (`w` в снимке, 0..1) — это тот же фильтр, но умеющий работать без
разметки:

  * слово размечено нашей базой — вес читается прямо с регистра:
        everyday 1.00, passive 0.55, specialist 0.20;
  * слово размечено только оригиналом — вес ОЦЕНИВАЕТСЯ по тому, как оригинал
    сам с этим словом обращался (сколько уровней оно отработало) и по
    частотности. Формула и её проверка — в `estimate_word_weight` ниже.

Что здесь измерено, а что придумано
--------------------------------------------------------------------------
Измерено на 6369 словах, которые есть и у нас, и у оригинала (то есть там, где
оценку можно сверить с настоящей разметкой):

  порог веса   слов выше   доля everyday   доля specialist
      0.50        4111          0.72            0.07
      0.60        3002          0.78            0.05
      0.70        1988          0.83            0.04
      0.80        1127          0.88            0.02
  без порога      6369          0.58            0.14

То есть оценка работает: она поднимает долю бытовых слов с 58% до 88%, и
делает это монотонно. Но она СЛАБЕЕ разметки — поэтому размеченному слову
верим на слово, а неразмеченному ставим планку выше (см. `minWordWeight`
в decadeProfiles.ts: на декадах 1-50 порог 0.70 при том, что размеченное
бытовое слово имеет вес 1.00).

Придумано (и честно помечено): ничего из того, что можно было измерить.
Две гипотезы проверены и ОТВЕРГНУТЫ замером — обе про вес СВЯЗИ, не слова:

  1. «доля выходов слова в четвёрках категории (core_share) предсказывает
     качество связи». Нет. На 1948 связях, известных обоим источникам:
     наш approved имеет средний core_share 0.32, alternative 0.37,
     hard_only 0.43 — то есть в обратную сторону. Причина понятна: core_share
     меряет, насколько слово штатное ДЛЯ КАТЕГОРИИ, а не насколько оно первое,
     что придёт игроку в голову.
  2. «слово, которое у другой категории ядро, для этой — alternative».
     Тоже нет: у связей с rel-share 0.8-1.0 доля нашего approved 0.78, а у
     связей с rel-share ниже 0.4 — 0.91.

Вывод, который из этого следует и исполнен буквально: слоя «верно, но не первая
мысль» в выгрузке нет и вывести его не из чего. Связи, которых наша база не
знает, приезжают `approved` — ровно как на источнике «словарь оригинала», —
а всю работу по отсеву делает вес СЛОВА. core_share при этом сохранён, но
только как порядок ВНУТРИ категории (какие слова у неё штатные), и никогда как
право связи попасть в уровень.

Что источник знает и чего не знает
--------------------------------------------------------------------------
Знает: всё, что знает наша база, — для слов и категорий, которые в ней есть
(6369 слов из 15155 у выгрузки), плюс всю широту оригинала сверху.
Не знает: значений слова и регистра для 8786 слов, которые есть только у
оригинала; статусов связи для связей, которых нет у нас. Это объявлено в
`limits` источника (web/src/core/sources.ts) и проверяется тестом.

Решение владельца от 31.07 «чужой словарь в нашей базе не храним» исполнено
так же, как для второго источника: сводная база — ОТДЕЛЬНЫЙ файл. Ни
content.snapshot.json, ни его хеш этот скрипт не трогает.

Запуск:  python3 scripts/export_hybrid_snapshot.py [--max-level N]
Вывод:   web/src/data/hybrid.snapshot.json
         data/hybrid-derived/hybrid.snapshot.sha256
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROD_SNAPSHOT = ROOT / "web" / "src" / "data" / "content.snapshot.json"
REF_SNAPSHOT = ROOT / "web" / "src" / "data" / "reference.snapshot.json"
DUMP = ROOT.parent.parent / "reference" / "bwj-org" / "levels.jsonl"
OUT_WEB = ROOT / "web" / "src" / "data" / "hybrid.snapshot.json"
OUT_HASH = ROOT / "data" / "hybrid-derived" / "hybrid.snapshot.sha256"

SNAPSHOT_SCHEMA_VERSION = "snapshot-2.1"

APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


# --------------------------------------------------------------------------- #
# вес слова
# --------------------------------------------------------------------------- #
# Якоря по регистру. Не «оценка качества слова вообще», а ровно та шкала, на
# которой стоят пороги декад: бытовое слово обязано проходить самый строгий
# порог (0.70), пассивное — только смягчённый (0.50), специальное — никакой.
# Поэтому 1.00 / 0.55 / 0.20, а не 1 / 0.5 / 0: круглые числа попали бы ровно
# на порог, и поведение зависело бы от ошибки округления.
WEIGHT_BY_REGISTER = {0: 1.00, 1: 0.55, 2: 0.20}

# Оценка веса для слова без нашей разметки. Три величины перебором по сетке
# (веса 0-3 у каждой, штраф за многословность 0/0.1/0.2) проверены против
# настоящего регистра на 6369 общих словах; лучший вариант — вот этот:
#
#   выходов слова в уровнях оригинала   вес 3   <- главный признак
#   частотность zipf                    вес 2
#   уровень дебюта у оригинала          вес 0   <- не добавил ничего
#   штраф за многословность             0.0     <- его берёт на себя maxTokens
#
# Уровень дебюта отпал не потому, что он не значим сам по себе (слова, впервые
# вышедшие на L1-50, бытовые в 76% случаев, а вышедшие после L700 — в 40%), а
# потому, что он повторяет число выходов: слово, отработавшее много уровней,
# почти всегда дебютировало рано. Оставить обе величины значило бы посчитать
# один и тот же признак дважды.
#
# RMSE оценки против регистра 0.35 на шкале 0..1 — то есть это именно оценка,
# а не измерение, и порог для неё поднят (см. шапку файла).
USES_SATURATION = 10          # выходов, после которых улика перестаёт расти
USES_WEIGHT = 3.0
ZIPF_WEIGHT = 2.0
ZIPF_FLOOR = 2.5              # ниже — оценка нулевая
ZIPF_CEILING = 5.0            # выше — оценка единичная


def estimate_word_weight(uses: int, zipf: float | None) -> float:
    """Вес слова, о котором известно только то, как с ним обращался оригинал."""
    uses_score = clamp(((1 + uses) ** 0.5) / ((1 + USES_SATURATION) ** 0.5))
    zipf_score = clamp(((zipf if zipf is not None else ZIPF_FLOOR) - ZIPF_FLOOR)
                       / (ZIPF_CEILING - ZIPF_FLOOR))
    total = USES_WEIGHT + ZIPF_WEIGHT
    return round((USES_WEIGHT * uses_score + ZIPF_WEIGHT * zipf_score) / total, 3)


# --------------------------------------------------------------------------- #
# вес связи
# --------------------------------------------------------------------------- #
# Вес связи отвечает на другой вопрос: не «годится ли слово в уровень вообще»,
# а «насколько оно ответ ИМЕННО этой категории». Он не фильтрует (замер показал,
# что улика оригинала на это не годится — см. шапку файла), он упорядочивает:
# внутри категории генератор берёт сначала слова с большим весом.
#
# Наша сторона: статус решает, разметка уточняет. Числа не новые — это те же
# оси, что уже читает генератор (`obviousness` с весом 0.9 в orderCandidates),
# сведённые в одно число, чтобы связь из выгрузки можно было поставить с нашей
# в один ряд.
STATUS_FACTOR = {0: 1.00, 1: 0.75, 2: 0.50, 3: 0.30, 4: 0.0}
OBVIOUSNESS_PART = 0.6
FIT_PART = 0.4

# Сторона выгрузки: core_share, усаженный к середине при малом числе наблюдений.
# Усадка обязательна: 4254 категории из 6714 выходили в уровнях ровно один раз,
# и без неё все их слова получили бы core_share 1.0 — «идеальное ядро» из
# единственного наблюдения. Сила усадки 2 наблюдения, цель усадки 0.55 (середина
# полосы). Полоса 0.55-0.90: связь из выгрузки не может оказаться выше нашей
# approved-связи (те дают 0.93-0.97), потому что за ней нет разметки.
REF_SHRINK_STRENGTH = 2.0
REF_SHRINK_PRIOR = 0.55
REF_BAND_LOW = 0.55
REF_BAND_SPAN = 0.35


def ours_link_weight(status: int, fit: float, obviousness: float) -> float:
    return round(STATUS_FACTOR.get(status, 0.0)
                 * (OBVIOUSNESS_PART * obviousness + FIT_PART * fit), 3)


def ref_link_weight(hits: int, appearances: int) -> float:
    share = ((hits + REF_SHRINK_STRENGTH * REF_SHRINK_PRIOR)
             / (appearances + REF_SHRINK_STRENGTH))
    return round(REF_BAND_LOW + REF_BAND_SPAN * clamp(share), 3)


def agree(a: float, b: float) -> float:
    """Обе стороны знают связь: уверенность складывается, а не усредняется.

    Это единственное место, где источники друг друга усиливают: слово, которое
    и наша база засчитала категории, и оригинал ставил в неё на живых уровнях,
    надёжнее любого из двух свидетельств по отдельности. Таких связей 1948.
    """
    return round(1 - (1 - a) * (1 - b), 3)


# --------------------------------------------------------------------------- #
# происхождение
# --------------------------------------------------------------------------- #
# Индекс попадает в снимок, порядок менять нельзя.
ORIGINS = ["ours", "reference", "both"]
O_OURS, O_REF, O_BOTH = 0, 1, 2


# --------------------------------------------------------------------------- #
# сборка
# --------------------------------------------------------------------------- #
def load_dump(path: Path, max_level: int | None) -> list[dict]:
    if not path.exists():
        raise SystemExit(
            f"ОШИБКА: нет выгрузки {path}\n"
            "Она не хранится в git (правило /reference/ в .gitignore).\n"
            "Собрать заново: python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025"
        )
    levels = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
              if line.strip()]
    if max_level is not None:
        levels = [l for l in levels if l["level"] <= max_level]
    return sorted(levels, key=lambda x: x["level"])


def build(prod: dict, ref: dict, levels: list[dict]) -> dict:
    # ------------------------------------------------------------------ #
    # 1. улики оригинала
    # ------------------------------------------------------------------ #
    appearances: Counter[str] = Counter()          # категория → выходов в уровнях
    hits: dict[str, Counter[str]] = defaultdict(Counter)
    first_level: dict[str, int] = {}
    uses: Counter[str] = Counter()                 # слово → в скольких уровнях вышло
    parents: dict[str, set[str]] = defaultdict(set)

    for level in levels:
        for entry in level["categories"]:
            name = normalize(entry["name"])
            appearances[name] += 1
            first_level.setdefault(name, level["level"])
            for raw in entry["words"]:
                word = normalize(raw)
                hits[name][word] += 1
                uses[word] += 1
            if entry.get("parent"):
                parents[name].add(normalize(entry["parent"]))

    # ------------------------------------------------------------------ #
    # 2. словарь
    # ------------------------------------------------------------------ #
    # Слово из обоих источников — одна запись. Идентичность по нормализованной
    # форме `n`: оба снимка нормализуют одной и той же функцией, поэтому
    # склейка точная, а не по похожести.
    words: dict[str, dict] = {}
    for w in prod["words"]:
        words[w["n"]] = dict(w, o=O_OURS)
    for w in ref["words"]:
        have = words.get(w["n"])
        if have is None:
            # слово знает только оригинал: регистра и значений у него нет,
            # имя собственное не размечено — всё это объявлено в limits источника
            words[w["n"]] = dict(w, o=O_REF)
        else:
            # наша запись сильнее: у неё есть регистр, разметка имени
            # собственного и человеческий регистр букв в `t`
            have["o"] = O_BOTH

    word_list = sorted(words.values(), key=lambda w: w["n"])
    word_index = {w["n"]: i for i, w in enumerate(word_list)}

    out_words = []
    weight_estimated = 0
    for w in word_list:
        register = w.get("e")
        if register is not None:
            weight = WEIGHT_BY_REGISTER[register]
            estimated = 0
        else:
            weight = estimate_word_weight(uses.get(w["n"], 0), w.get("z"))
            estimated = 1
            weight_estimated += 1
        entry = {
            "t": w["t"], "n": w["n"], "z": w["z"], "u": w["u"], "l": w["l"],
            "p": w["p"], "tok": w["tok"],
            "w": weight,
            # 1 — вес оценён по уликам, а не прочитан с разметки. Поле нужно не
            # для красоты: без него нельзя отличить «слово бытовое» от «слово
            # похоже на бытовое», а это ровно та разница, из-за которой порог
            # для оценки стоит выше.
            "we": estimated,
            "o": w["o"],
        }
        if register is not None:
            entry["e"] = register
        out_words.append(entry)

    # ------------------------------------------------------------------ #
    # 3. категории
    # ------------------------------------------------------------------ #
    # Склейка по ИМЕНИ: наша FARM ANIMALS и `farm animals` оригинала — одна
    # категория с общим пулом, а не две с одинаковой надписью. Иначе генератор
    # мог бы поставить обе в один уровень, и точное покрытие развалилось бы на
    # первом же общем слове.
    prod_by_label: dict[str, int] = {}
    for i, c in enumerate(prod["categories"]):
        prod_by_label.setdefault(normalize(c["l"]), i)

    ref_by_label: dict[str, int] = {}
    for i, c in enumerate(ref["categories"]):
        ref_by_label.setdefault(normalize(c["l"]), i)

    used_keys: set[str] = set()

    def unique_key(key: str) -> str:
        if key not in used_keys:
            used_keys.add(key)
            return key
        suffix = 2
        while f"{key}_{suffix}" in used_keys:
            suffix += 1
        used_keys.add(f"{key}_{suffix}")
        return f"{key}_{suffix}"

    cats: list[dict] = []
    cat_index_by_label: dict[str, int] = {}

    for i, c in enumerate(prod["categories"]):
        label = normalize(c["l"])
        if label in cat_index_by_label:
            continue
        entry = dict(c)
        entry["k"] = unique_key(c["k"])
        entry["o"] = O_OURS
        if label in appearances:
            entry["o"] = O_BOTH
            entry["ref_levels"] = appearances[label]
            entry["ref_first_level"] = first_level[label]
        cat_index_by_label[label] = len(cats)
        cats.append(entry)

    for i, c in enumerate(ref["categories"]):
        label = normalize(c["l"])
        if label in cat_index_by_label:
            continue
        entry = dict(c)
        entry["k"] = unique_key(c["k"])
        entry["o"] = O_REF
        cat_index_by_label[label] = len(cats)
        cats.append(entry)

    prod_cat_to_index = {i: cat_index_by_label[normalize(c["l"])]
                         for i, c in enumerate(prod["categories"])}
    ref_cat_to_index = {i: cat_index_by_label[normalize(c["l"])]
                        for i, c in enumerate(ref["categories"])}

    # ------------------------------------------------------------------ #
    # 4. связи
    # ------------------------------------------------------------------ #
    prod_word_n = [w["n"] for w in prod["words"]]
    ref_word_n = [w["n"] for w in ref["words"]]

    merged: dict[tuple[int, int], list] = {}

    for m in prod["memberships"]:
        wi = word_index[prod_word_n[m[0]]]
        ci = prod_cat_to_index[m[1]]
        weight = ours_link_weight(m[2], m[3], m[4])
        merged[(wi, ci)] = [wi, ci, m[2], m[3], m[4], m[5], m[6],
                            m[7] if len(m) > 7 else None,
                            m[8] if len(m) > 8 else 0,
                            weight, O_OURS]

    # значения слова индексируются заново вместе со словарём
    sense_shift: dict[int, int] = {}
    senses = []
    for i, s in enumerate(prod["senses"]):
        sense_shift[i] = len(senses)
        senses.append({
            "word": word_index[prod_word_n[s["word"]]] if s["word"] is not None else None,
            "key": s["key"], "def": s["def"],
        })
    for row in merged.values():
        if row[6] is not None:
            row[6] = sense_shift[row[6]]

    ref_only = 0
    confirmed = 0
    for m in ref["memberships"]:
        norm = ref_word_n[m[0]]
        wi = word_index[norm]
        ci = ref_cat_to_index[m[1]]
        label = normalize(ref["categories"][m[1]]["l"])
        weight = ref_link_weight(hits[label][norm], appearances.get(label, 1))
        row = merged.get((wi, ci))
        if row is None:
            # связь знает только оригинал. Статус approved — потому что выгрузка
            # это ключ ответов, а вывести из неё оттенок нечем (замер в шапке).
            merged[(wi, ci)] = [wi, ci, 0, m[3], m[4], m[5], None, None, 0,
                                weight, O_REF]
            ref_only += 1
        else:
            # связь знают оба: статус остаётся НАШ (он размечен, а не выведен),
            # а вес растёт — два независимых свидетельства сильнее одного
            row[9] = agree(row[9], weight)
            row[10] = O_BOTH
            confirmed += 1

    out_memberships = [merged[k] for k in sorted(merged)]

    # ------------------------------------------------------------------ #
    # 5. мета-потенциал
    # ------------------------------------------------------------------ #
    # Считается заново по сводной базе, а не склеивается из двух списков:
    # категория, чьё имя есть в словаре, могла получить хозяина из ДРУГОГО
    # источника — именно ради таких пар источники и сводятся.
    memberships_by_word: dict[int, set[int]] = defaultdict(set)
    for row in out_memberships:
        memberships_by_word[row[0]].add(row[1])

    label_to_index = cat_index_by_label
    meta_capable = []
    for label, ci in sorted(label_to_index.items(), key=lambda kv: kv[1]):
        wi = word_index.get(label)
        if wi is None:
            continue
        hosts = set(memberships_by_word.get(wi, set()))
        # наблюдённая вложенность оригинала — факт, а не догадка
        hosts |= {label_to_index[p] for p in parents.get(label, set())
                  if p in label_to_index}
        hosts.discard(ci)
        if not hosts:
            continue
        meta_capable.append({"category": ci, "word": wi, "hosts": sorted(hosts)})

    # ------------------------------------------------------------------ #
    # 6. слои, которые есть только у нас
    # ------------------------------------------------------------------ #
    # Запреты пар и проверенные четвёрки переиндексируются как есть. Выдумывать
    # запреты для категорий оригинала не из чего: у генератора на этот случай
    # есть живой фильтр пересечения пулов.
    conflicts = [[prod_cat_to_index[c[0]], prod_cat_to_index[c[1]], c[2], c[3], c[4]]
                 for c in (prod.get("conflicts") or [])]
    quartets = [[prod_cat_to_index[q[0]],
                 [word_index[prod_word_n[w]] for w in q[1]], q[2]]
                for q in (prod.get("quartets") or [])]

    snapshot = {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "statuses": prod["statuses"],
        "risk_flags": prod.get("risk_flags", []),
        "conflict_types": prod.get("conflict_types", []),
        "quartet_tiers": prod.get("quartet_tiers", []),
        "origins": ORIGINS,
        "constants": prod["constants"],
        "categories": cats,
        "words": out_words,
        "senses": senses,
        "memberships": out_memberships,
        "meta_capable": meta_capable,
        "conflicts": conflicts,
        "quartets": quartets,
    }

    # ------------------------------------------------------------------ #
    # 7. статистика: прежде всего ёмкость под порогами веса
    # ------------------------------------------------------------------ #
    weight_of = [w["w"] for w in out_words]
    by_category: dict[int, list[int]] = defaultdict(list)
    for row in out_memberships:
        if row[2] == 0:                       # approved, как их видит генератор
            by_category[row[1]].append(row[0])

    def categories_with_quartet(floor: float) -> int:
        return sum(1 for ws in by_category.values()
                   if sum(1 for w in ws if weight_of[w] >= floor) >= 4)

    zs = [w["z"] for w in out_words if w["z"] is not None]
    snapshot["stats"] = {
        "categories": len(cats),
        "categories_ours": sum(1 for c in cats if c["o"] == O_OURS),
        "categories_reference": sum(1 for c in cats if c["o"] == O_REF),
        "categories_both": sum(1 for c in cats if c["o"] == O_BOTH),
        "words": len(out_words),
        "words_ours": sum(1 for w in out_words if w["o"] == O_OURS),
        "words_reference": sum(1 for w in out_words if w["o"] == O_REF),
        "words_both": sum(1 for w in out_words if w["o"] == O_BOTH),
        "words_weight_estimated": weight_estimated,
        "words_weight_above_070": sum(1 for w in weight_of if w >= 0.70),
        "words_weight_above_050": sum(1 for w in weight_of if w >= 0.50),
        "senses": len(senses),
        "memberships": len(out_memberships),
        "memberships_ours": sum(1 for m in out_memberships if m[10] == O_OURS),
        "memberships_reference": ref_only,
        "memberships_both": confirmed,
        "approved": sum(1 for m in out_memberships if m[2] == 0),
        "alternative": sum(1 for m in out_memberships if m[2] == 1),
        "hard_only": sum(1 for m in out_memberships if m[2] == 2),
        "conflicts": len(conflicts),
        "quartets": len(quartets),
        "meta_capable_categories": len(meta_capable),
        "meta_capable_with_host": len(meta_capable),
        "categories_with_4plus_approved": sum(1 for ws in by_category.values()
                                              if len(ws) >= 4),
        "categories_quartet_weight_070": categories_with_quartet(0.70),
        "categories_quartet_weight_050": categories_with_quartet(0.50),
        "frequency_unknown_words": sum(w["u"] for w in out_words),
        "words_below_top50k": sum(1 for z in zs
                                  if z < prod["constants"]["top50k_zipf"]),
        "multi_token_words": sum(1 for w in out_words if w["tok"] > 1),
        "trap_capable_words": sum(1 for ws in memberships_by_word.values()
                                  if len(ws) >= 2),
        "zipf_median_x100": round(statistics.median(zs) * 100) if zs else 0,
        "reference_levels": len(levels),
    }
    return snapshot


def canonical(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=None,
                        help="учитывать только уровни оригинала до этого номера "
                             "(по умолчанию вся выгрузка: чем больше уровней, "
                             "тем надёжнее улика для веса слова)")
    args = parser.parse_args()

    prod = json.loads(PROD_SNAPSHOT.read_text(encoding="utf-8"))
    ref = json.loads(REF_SNAPSHOT.read_text(encoding="utf-8"))
    levels = load_dump(DUMP, args.max_level)
    print(f"наша база: {len(prod['categories'])} категорий, {len(prod['words'])} слов")
    print(f"словарь оригинала: {len(ref['categories'])} категорий, "
          f"{len(ref['words'])} слов")
    print(f"выгрузка: {len(levels)} уровней")

    snapshot = build(prod, ref, levels)
    snapshot["content_snapshot_hash"] = hashlib.sha256(
        canonical({k: v for k, v in snapshot.items() if k != "stats"}).encode("utf-8")
    ).hexdigest()

    OUT_WEB.parent.mkdir(parents=True, exist_ok=True)
    OUT_HASH.parent.mkdir(parents=True, exist_ok=True)
    OUT_WEB.write_text(canonical(snapshot) + "\n", encoding="utf-8")
    OUT_HASH.write_text(snapshot["content_snapshot_hash"] + "\n", encoding="utf-8")

    s = snapshot["stats"]
    print(f"\nснимок: {OUT_WEB.relative_to(ROOT)}  "
          f"{OUT_WEB.stat().st_size / 1_048_576:.2f} МБ")
    print(f"хеш: {snapshot['content_snapshot_hash'][:16]}…")
    print(f"  категорий {s['categories']}: наших {s['categories_ours']}, "
          f"оригинала {s['categories_reference']}, общих {s['categories_both']}")
    print(f"  слов {s['words']}: наших {s['words_ours']}, "
          f"оригинала {s['words_reference']}, общих {s['words_both']}")
    print(f"  вес слова оценён (нет нашей разметки): {s['words_weight_estimated']}")
    print(f"  слов с весом >= 0.70: {s['words_weight_above_070']}, "
          f">= 0.50: {s['words_weight_above_050']}")
    print(f"  связей {s['memberships']}: наших {s['memberships_ours']}, "
          f"оригинала {s['memberships_reference']}, "
          f"подтверждённых обоими {s['memberships_both']}")
    print(f"  категорий с четвёркой под порогом 0.70: "
          f"{s['categories_quartet_weight_070']}, под 0.50: "
          f"{s['categories_quartet_weight_050']}, без порога: "
          f"{s['categories_with_4plus_approved']}")
    print(f"  мета-пар: {s['meta_capable_categories']}, "
          f"значений слова: {s['senses']}, запретов пар: {s['conflicts']}")
    print(f"  медиана zipf: {s['zipf_median_x100'] / 100:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
