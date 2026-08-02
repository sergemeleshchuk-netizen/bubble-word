#!/usr/bin/env python3
"""Приёмник батча разметки регистра слов.

Разметку регистра (`words.everyday_class`, шаг миграции 010) нельзя вывести
формулой — замер на 233 размеченных вручную словах показал, что тема даёт лишь
частичный сигнал (в `animals` 53 пассивных против 10 бытовых, в `food` наоборот
159 против 23), а частотность не даёт никакого: в полосе zipf 3.5-3.75 лежат
68 бытовых и 32 пассивных. Поэтому решение принимает модель, а скрипт лишь
принимает готовый батч в компактном виде: построчный JSONL на 10 000 слов стоит
впятеро дороже по объёму, чем списки через пробел.

Вход: текстовый файл, три секции. Слова через пробел или перевод строки,
многословные записи — через подчёркивание (`hot_sauce` -> `hot sauce`).

    # everyday
    carrot mop bagel omelet
    # passive
    quail obituary congestion
    # specialist
    tungsten epoxy basilica

Слово ищется по нормализованной форме и должно уже быть в базе: регистр — это
суждение о том, что в базе есть, а не способ добавлять слова.

Запуск:  python3 scripts/register_batch.py --db database/content.sqlite --input батч.txt
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

CLASSES = ("everyday", "passive", "specialist")
SECTION = re.compile(r"^#\s*(everyday|passive|specialist)\s*$", re.I)


def parse(text: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {name: [] for name in CLASSES}
    current: str | None = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = SECTION.match(line)
        if match:
            current = match.group(1).lower()
            continue
        if current is None:
            raise SystemExit(f"ОШИБКА: слова до первой секции: {line[:60]}")
        out[current].extend(w.replace("_", " ") for w in line.split())
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--source", default="assistant")
    parser.add_argument("--rest", choices=CLASSES,
                        help="класс для ОСТАЛЬНЫХ неразмеченных слов перечисленных тем")
    parser.add_argument("--themes",
                        help="темы через запятую: из них берётся остаток для --rest")
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
    from word_content.db import utc_now
    from word_content.normalization import normalize_word

    batch = parse(Path(args.input).read_text(encoding="utf-8"))
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    # --rest: явное решение «весь остаток этих тем относится к такому-то классу».
    # Нужен потому, что в бытовых темах меньшинство перечислить дешевле, чем
    # большинство: в food/home из 681 слова бытовыми оказались 580. Решение всё
    # равно моё и записано в вызове, а не выведено формулой.
    if args.rest:
        if not args.themes:
            raise SystemExit("ОШИБКА: --rest требует --themes (или --themes '*')")
        # '*' — весь остаток базы. Нужен для слов, у которых темы нет вовсе:
        # это те, у кого не осталось ни одной играбельной связи (только rejected
        # или hard_only), и по теме их не выбрать.
        if args.themes.strip() == "*":
            rest = [
                row["normalized"]
                for row in conn.execute(
                    "SELECT normalized FROM words "
                    "WHERE everyday_class IS NULL AND status = 'active'"
                )
            ]
        else:
            themes = [t.strip() for t in args.themes.split(",") if t.strip()]
            placeholders = ", ".join("?" for _ in themes)
            rest = [
                row["normalized"]
                for row in conn.execute(
                    f"""SELECT w.normalized FROM words w
                         WHERE w.everyday_class IS NULL AND w.status = 'active'
                           AND (SELECT c.theme FROM memberships m
                                  JOIN categories c ON c.id = m.category_id
                                 WHERE m.word_id = w.id
                                   AND m.review_status IN ('approved', 'alternative')
                                 ORDER BY m.id LIMIT 1) IN ({placeholders})""",
                    themes,
                )
            ]
        listed = {normalize_word(w) for name in CLASSES for w in batch[name]}
        added = [w for w in rest if w not in listed]
        batch[args.rest].extend(added)
        print(f"остаток ({args.themes}) -> {args.rest}: {len(added)} слов")

    applied = 0
    unknown: list[str] = []
    repeat: list[str] = []
    seen: set[str] = set()
    with conn:
        for name in CLASSES:
            for word in batch[name]:
                norm = normalize_word(word)
                if norm in seen:
                    repeat.append(word)
                    continue
                seen.add(norm)
                row = conn.execute(
                    "SELECT id FROM words WHERE normalized = ?", (norm,)
                ).fetchone()
                if row is None:
                    unknown.append(word)
                    continue
                conn.execute(
                    "UPDATE words SET everyday_class = ?, everyday_source = ?, updated_at = ? "
                    "WHERE id = ?",
                    (name, args.source, utc_now(), int(row["id"])),
                )
                applied += 1

    counts = dict(
        conn.execute(
            "SELECT everyday_class, COUNT(*) FROM words WHERE everyday_class IS NOT NULL GROUP BY 1"
        ).fetchall()
    )
    total = int(conn.execute("SELECT COUNT(*) FROM words").fetchone()[0])
    left = int(
        conn.execute(
            "SELECT COUNT(*) FROM words WHERE everyday_class IS NULL AND status = 'active'"
        ).fetchone()[0]
    )
    conn.close()

    done = sum(counts.values())
    print(f"батч: проставлено {applied}")
    for name in CLASSES:
        print(f"  {name:11} {counts.get(name, 0)}")
    print(f"всего размечено {done} из {total} ({100 * done / total:.1f}%), осталось активных {left}")
    if repeat:
        print(f"  повтор внутри батча ({len(repeat)}): {', '.join(repeat[:10])}", file=sys.stderr)
    if unknown:
        print(f"  нет в базе ({len(unknown)}): {', '.join(unknown[:15])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
