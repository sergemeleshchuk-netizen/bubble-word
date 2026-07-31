#!/usr/bin/env python3
"""Экспорт контентной базы (SQLite) в JSON, который читают скиллы и скрипты.

Зачем этот файл существует. Скиллы `level-generator`, `word-associations-generator`
и скрипты `assemble_pack.py`, `validate_level.py`, `eval_metrics.py` читают
`tool/data/categories.json`. Настоящая база живёт в SQLite и одна — этот скрипт
её выгружает в формат, к которому привыкли потребители.

Формат выхода — ровно тот же, что был у `build_base.py`, чтобы ни один потребитель
не пришлось переписывать:

    {"categories": [{"id", "name", "related", "words": [{"w","zipf","len"}],
                     "shared_words": {слово: [другие категории]}}]}

Что добавлено сверх прежнего формата (старые потребители лишние поля игнорируют):

    readiness   готовность категории из базы: ready | constrained | …
    conflicts   категории, которые НЕЛЬЗЯ ставить на один уровень с этой
    alt         слова со статусом alternative — материал для ловушек, не для дома
    source      всегда db: второго слоя в выгрузке больше нет
    legacy_ids  прежние id этой категории, если они были
    aliases     в корне: карта «прежний id -> нынешний ключ»

Про прежние id. Сданные пакеты (etalon, volume1, volume2, демо) ссылаются на id
допайплайновой базы. Раньше ради них в выгрузку подмешивали сами те категории, и
в файле жили два слоя качества — проверенный и никакой. Теперь их содержимое
втянуто в SQLite (прогон run-002-legacy-merge), а старые имена разрешаются через
`aliases` и `legacy_ids`.

Запуск:  python3 tool/scripts/export_base_json.py [--db путь] [--out путь]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "tool" / "word_content_pipeline" / "database" / "content.sqlite"
OUT = ROOT / "tool" / "data" / "categories.json"
ALIASES = ROOT / "tool" / "data" / "category_aliases.json"

# Статусы, из которых собирается «дом» слова. alternative идёт отдельным полем:
# это ловушка, а не дом, и складывать их в один пул нельзя — на этом ловится
# половина двусмысленностей.
HOME_STATUSES = ("approved",)
TRAP_STATUSES = ("alternative",)


def resolve_db(explicit: str | None) -> Path | None:
    if explicit:
        path = Path(explicit)
        return path if path.exists() else None
    # База одна и лежит в git; запасной путь на копию в БАЗА-СЛОВ убран.
    return DB if DB.exists() else None


def connect(path: Path) -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        conn.execute("select 1 from sqlite_master limit 1")
    except sqlite3.OperationalError:
        conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    return conn


def zipf_resolver():
    """zipf слова или фразы — та же формула, что в снимке веб-инструмента.

    Осторожно: `familiarity_score` в базе — НЕ zipf, а нормированная 0..1
    величина. Один раз я подставил её в поле `zipf`, и все 8459 слов стали
    «редкими» (eval_metrics на эталоне e2 выдал rare=24 из 32). Частотность
    считаем частотником, а `familiarity` отдаём отдельным полем.
    """
    from wordfreq import zipf_frequency

    def resolve(word: str) -> float:
        parts = [p for p in re.split(r"[ \-']+", word) if p]
        if not parts:
            return 0.0
        values = [zipf_frequency(p, "en") for p in parts]
        return round(min(values) if len(parts) > 1 else values[0], 2)

    return resolve


def build(conn: sqlite3.Connection) -> list[dict]:
    version = conn.execute(
        "select value from schema_meta where key='schema_version'").fetchone()
    if version is None or version["value"] != "2":
        raise SystemExit("ОШИБКА: база не аудированной версии (нужна schema_version 2)")

    zipf_of = zipf_resolver()
    cats = {
        int(r["id"]): {
            "id": r["category_key"],
            "name": r["label"].title(),
            "readiness": r["readiness"],
            "words": [],
            "alt": [],
            "related": [],
            "conflicts": [],
            "shared_words": {},
            "source": "db",
        }
        for r in conn.execute(
            "select id, category_key, label, readiness from categories "
            "where status='active' order by category_key")
    }

    # пулы: дом и ловушки отдельно
    home_of = defaultdict(set)       # слово -> категории, где это дом
    plausible_in = defaultdict(set)  # слово -> категории, где слово правдоподобно
    for r in conn.execute(
        "select w.normalized as word, w.familiarity_score as familiarity, m.category_id, "
        "       m.review_status "
        "  from memberships m "
        "  join words w on w.id = m.word_id "
        " where m.review_status in ('approved','alternative') "
        "   and m.semantic_status <> 'incorrect' "
        "   and w.status = 'active' "
        " order by w.normalized"
    ):
        cat = cats.get(int(r["category_id"]))
        if cat is None:
            continue
        entry = {
            "w": r["word"],
            "zipf": zipf_of(r["word"]),
            "len": len(r["word"]),
            # нормированная оценка знакомости из базы: отдельная ось от частотности
            "familiarity": round(r["familiarity"], 2) if r["familiarity"] is not None else None,
        }
        if r["review_status"] in HOME_STATUSES:
            cat["words"].append(entry)
            home_of[r["word"]].add(cat["id"])
        else:
            cat["alt"].append(entry)
        plausible_in[r["word"]].add(cat["id"])

    # пересечения: слово, у которого дом здесь, но правдоподобно и в другой категории
    for cat in cats.values():
        for entry in cat["words"]:
            others = sorted(plausible_in[entry["w"]] - {cat["id"]})
            if others:
                cat["shared_words"][entry["w"]] = others

    # запреты пар из базы
    keys = {cid: cat["id"] for cid, cat in cats.items()}
    for r in conn.execute(
        "select category_a_id as a, category_b_id as b from category_conflicts"
    ):
        a, b = keys.get(int(r["a"])), keys.get(int(r["b"]))
        if a is None or b is None:
            continue
        cats_by_key = {cat["id"]: cat for cat in cats.values()}
        cats_by_key[a]["conflicts"].append(b)
        cats_by_key[b]["conflicts"].append(a)

    # смежные категории: делят хотя бы одно играбельное слово и НЕ запрещены.
    # Прежний `related` был курированным списком «соседних тем»; здесь то же
    # самое считается по данным, а запрещённые пары из него исключены — они
    # не «смежные», они вообще не ставятся вместе.
    shared_pairs: dict[tuple[str, str], int] = defaultdict(int)
    for word, category_keys in plausible_in.items():
        keys_list = sorted(category_keys)
        for i, a in enumerate(keys_list):
            for b in keys_list[i + 1:]:
                shared_pairs[(a, b)] += 1
    by_key = {cat["id"]: cat for cat in cats.values()}
    for (a, b), count in shared_pairs.items():
        if b in by_key[a]["conflicts"]:
            continue
        by_key[a]["related"].append(b)
        by_key[b]["related"].append(a)

    for cat in by_key.values():
        cat["related"] = sorted(set(cat["related"]))
        cat["conflicts"] = sorted(set(cat["conflicts"]))
        cat["words"].sort(key=lambda w: -w["zipf"])
        cat["alt"].sort(key=lambda w: -w["zipf"])

    return sorted(by_key.values(), key=lambda c: c["id"])


def merge_legacy(categories: list[dict]) -> tuple[list[dict], int]:
    """Привязывает прежние id категорий к нынешним ключам базы.

    Раньше эта функция ДОБАВЛЯЛА в выгрузку категории прежней базы, которых не
    было в SQLite. Из-за этого в файле жили два слоя качества: 1275 категорий,
    прошедших пайплайн, и 242 — без готовности, без запретов на сочетание, без
    четвёрок, проверенных solver'ом. Отличить их можно было только по полю
    `source`, а генератор по нему не смотрел.

    Теперь содержимое прежней базы втянуто в SQLite (прогон run-002-legacy-merge),
    и здесь остаётся только разрешение старых имён: сданные пакеты ссылаются на
    прежние id, поэтому каждая категория несёт список своих прежних имён в
    `legacy_ids`, а в корне выгрузки лежит общая карта `aliases`.

    Возвращает (категории, сколько прежних id не удалось разрешить). Ненулевое
    второе значение — повод разбираться: значит часть прежней базы потеряна.
    """
    if not ALIASES.exists():
        return categories, 0
    aliases = json.loads(ALIASES.read_text(encoding="utf-8"))["aliases"]
    by_key = {c["id"]: c for c in categories}
    unresolved = 0
    for legacy_id, key in sorted(aliases.items()):
        target = by_key.get(key)
        if target is None:
            unresolved += 1
            continue
        if legacy_id != key:
            target.setdefault("legacy_ids", []).append(legacy_id)
    return categories, unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", help="путь к базе SQLite")
    parser.add_argument("--out", help="куда писать JSON")
    args = parser.parse_args()

    db_path = resolve_db(args.db)
    if db_path is None:
        print(f"ОШИБКА: нет базы {args.db or DB}", file=sys.stderr)
        return 1
    out_path = Path(args.out) if args.out else OUT

    conn = connect(db_path)
    categories = build(conn)
    from_db = len(categories)
    conn.close()

    categories, unresolved = merge_legacy(categories)
    aliases = (json.loads(ALIASES.read_text(encoding="utf-8"))["aliases"]
               if ALIASES.exists() else {})

    payload = {
        "version": 3,
        "language": "en",
        "built_from": f"{db_path.name} (export_base_json.py)",
        # прежний id категории -> нынешний ключ: сданные пакеты ссылаются на старые имена
        "aliases": aliases,
        "categories": categories,
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    words = {w["w"] for c in categories for w in c["words"]}
    traps = sum(1 for c in categories for _ in c.get("shared_words", {}))
    print(f"источник: {db_path}")
    print(f"категорий: {len(categories)} (все из базы)")
    print(f"прежних id разрешено псевдонимами: {len(aliases) - unresolved} из {len(aliases)}")
    if unresolved:
        # Обычная причина — категория в базе есть, но отключена: пул не собирает
        # четвёрку, и в выгрузку идут только активные. Это не потеря данных.
        print(f"ИНФО: прежних id без активной категории: {unresolved} "
              f"(категория в базе есть, но отключена — пул не собирает четвёрку)")
    print(f"уникальных слов-домов: {len(words)}")
    print(f"связей слово-в-двух-категориях: {traps}")
    print(f"запретов пар: {sum(len(c.get('conflicts', [])) for c in categories) // 2}")
    print(f"→ {out_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
