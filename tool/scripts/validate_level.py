#!/usr/bin/env python3
"""Валидатор уровней (слой 1 из rules.md: программные проверки).

Запуск из корня репозитория BB:
    python3 tool/scripts/validate_level.py levels/etalon/e1.json [e2.json ...]

Несколько файлов = пакет уровней: repeats проверяются по истории пакета
в порядке следования файлов. Ошибки -> exit 1; предупреждения не блокируют.
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tool" / "data" / "categories.json"
BLOCKLIST = ROOT / "tool" / "data" / "blocklist.txt"


def load_base():
    """Пулы категорий, доступные и по нынешнему ключу, и по прежним именам.

    Сданные пакеты (etalon, volume1, volume2, демо) ссылаются на id
    допайплайновой базы: `ages`, `cities`, `gems`. В SQLite те же категории
    называются иначе (`life_stages`, `world_cities`, `gemstones`), поэтому
    выгрузка несёт прежние имена в `legacy_ids`, и валидатор их принимает.
    Без этого уровни сданных пакетов выглядели бы как ссылки на несуществующие
    категории.
    """
    data = json.loads(BASE.read_text())
    cats = {}
    for c in data["categories"]:
        pool = {w["w"] for w in c["words"]}
        cats[c["id"]] = pool
        for legacy_id in c.get("legacy_ids", ()):
            cats.setdefault(legacy_id, pool)
    return cats


def load_blocklist():
    words = set()
    if BLOCKLIST.exists():
        for line in BLOCKLIST.read_text().splitlines():
            line = line.strip().lower()
            if line and not line.startswith("#"):
                words.add(line)
    return words


def validate(level, base, blocked, history):
    """history: список уровней пакета, разобранных ДО текущего."""
    errors, warnings = [], []
    cats = level.get("categories", [])
    m = len(cats)
    ids = [c["id"] for c in cats]
    if len(set(ids)) != m:
        errors.append("дубли id категорий на уровне")

    word_home = {}  # слово -> id категории уровня
    for c in cats:
        words = c.get("words", [])
        if len(words) != 4:
            errors.append(f"{c['id']}: {len(words)} слов вместо 4")
        for w in words:
            if w != w.lower():
                errors.append(f"{c['id']}: '{w}' не в lowercase")
            if w in word_home:
                errors.append(f"'{w}' дважды на уровне ({word_home[w]} и {c['id']})")
            word_home[w] = c["id"]
            if w in blocked:
                errors.append(f"'{w}' в блок-листе")
            if c["id"] in base and w not in base[c["id"]]:
                warnings.append(f"'{w}' нет в пуле базы '{c['id']}' (слово вне базы)")
        if c["id"] not in base:
            warnings.append(f"категории '{c['id']}' нет в базе")

    # ловушки
    declared_traps = set()
    for t in level.get("traps", []):
        w, home, tempts = t["word"], t["home"], t["tempts"]
        declared_traps.add(w)
        if home not in ids or tempts not in ids:
            errors.append(f"ловушка '{w}': home/tempts не на уровне")
            continue
        if word_home.get(w) != home:
            errors.append(f"ловушка '{w}': слово не лежит в words home-категории '{home}'")
        tempts_words = next(c["words"] for c in cats if c["id"] == tempts)
        if w in tempts_words:
            errors.append(f"ловушка '{w}': слово одновременно в words '{tempts}'")
        if home in base and tempts in base and not (w in base[home] and w in base[tempts]):
            warnings.append(f"ловушка '{w}': базой не подтверждена (нет в обоих пулах {home}/{tempts})")

    # незаявленные пересечения: слово уровня живёт в базовых пулах ДВУХ категорий уровня
    for w, home in word_home.items():
        others = [cid for cid in ids if cid != home and cid in base and w in base[cid]]
        if others and w not in declared_traps:
            warnings.append(f"'{w}' ({home}) есть и в пуле {others} - незаявленная ловушка?")

    # доска
    board = level.get("board", {})
    limit, k, start = board.get("move_limit"), board.get("move_limit_k"), board.get("start_bubbles")
    if limit is not None:
        if limit < 3 * m:
            errors.append(f"move_limit {limit} < минимума {3*m} (3 мерджа на категорию)")
        if k and limit != math.ceil(3 * m * k):
            warnings.append(f"move_limit {limit} != ceil(3*{m}*{k}) = {math.ceil(3*m*k)}")
    total = 4 * m
    if start is not None:
        if start > total:
            errors.append(f"start_bubbles {start} > всего слов {total}")
        elif start > 24:
            warnings.append(f"start_bubbles {start} > 24 (референс: поле вмещает 20-24)")
        elif start < min(20, total):
            warnings.append(f"start_bubbles {start} < {min(20, total)} (референс: 20-24 или все слова)")

    # повторы по истории пакета
    hist_words = {}  # слово -> (level_id, category_id)
    for prev in history:
        for c in prev.get("categories", []):
            for w in c["words"]:
                hist_words[w] = (prev.get("level_id"), c["id"])
    declared_repeats = {r["word"] for r in level.get("repeats", [])}
    for r in level.get("repeats", []):
        w = r["word"]
        if w not in word_home:
            errors.append(f"repeat '{w}': слова нет на уровне")
        elif w not in hist_words:
            warnings.append(f"repeat '{w}': в предыдущих уровнях пакета не встречалось")
        elif hist_words[w] != (r.get("prev_level"), r.get("prev_category")):
            warnings.append(f"repeat '{w}': в истории {hist_words[w]}, заявлено "
                            f"({r.get('prev_level')}, {r.get('prev_category')})")
    for w, home in word_home.items():
        if w in hist_words and w not in declared_repeats and hist_words[w][1] != home:
            warnings.append(f"'{w}' уже был в уровне {hist_words[w][0]} ({hist_words[w][1]}) - "
                            f"незаявленный repeat")

    return errors, warnings


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print(__doc__)
        sys.exit(2)
    base, blocked = load_base(), load_blocklist()
    history, failed = [], False
    for p in paths:
        level = json.loads(p.read_text())
        errors, warnings = validate(level, base, blocked, history)
        status = "FAIL" if errors else "OK"
        m = len(level.get("categories", []))
        print(f"\n== {p.name}: {status}  (уровень {level.get('level_id')}, "
              f"{m} категорий, {4*m} слов, лимит {level.get('board', {}).get('move_limit')})")
        for e in errors:
            print(f"  ERROR: {e}")
        for w in warnings:
            print(f"  warn:  {w}")
        if errors:
            failed = True
        history.append(level)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
