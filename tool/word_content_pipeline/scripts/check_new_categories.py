#!/usr/bin/env python3
"""Предпроверка предложенных категорий ДО импорта.

Зачем. Первый батч новых категорий 02.08 дал 13 дублей из 24: я сверил занятость
ключей и не сверил занятость понятий. В базе 1296 категорий, и совпадение по
ключу редкость, а совпадение по смыслу — норма: `dirty_words` наткнулся на
`cleanliness_words` (12 общих слов из 12), `how_often` на `frequency_words` (12),
`us_holidays` на `holidays` (12), `places_to_sit` на `furniture` (12). Каждый
такой дубль не добавляет ёмкости, зато добавляет запрет пары `do_not_pair` и
усложняет точное покрытие — то есть делает базу хуже, а не лучше.

Что проверяет, по каждой предложенной категории:
  * ключ уже занят;
  * слова, которых в базе нет;
  * слова не класса `everyday` (шаг 010) — они не пройдут фильтр генератора;
  * СУЩЕСТВУЮЩИЕ категории с большим пересечением по словам — главная проверка.

Порог пересечения — шесть слов, см. OVERLAP_WARN ниже. Это предупреждение, а не
запрет: пересечение бывает законным (BIRDS и FLYING ANIMALS делят 13 слов, и обе
категории нужны — база держит их парой `do_not_pair`). Решает человек.

Чего скрипт НЕ ловит. Он ничего не знает про слой записи референса. Слово,
положенное в родительскую категорию ради мета-ребра, может сломать разрешение
надписи из записи: `marsupials` в ZOO ANIMALS увёл на себя надпись «safari
animals» (ZOO ANIMALS делит с AFRICAN ANIMALS шесть слов), и тесты 8b/12b упали,
хотя пересечение самого набора было ниже порога. Поэтому после каждого батча
обязателен прогон `pytest tests/test_reference_reproduction.py`.

Вход — тот же JSONL, что у `import-categories`, плюс поле `words` со списком.
Запуск:  python3 scripts/check_new_categories.py --db ... --input предложение.jsonl
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

# Выше этого числа общих слов считаем, что понятие в базе уже есть.
#
# Начинал с 8 и один дубль пропустил: `days_of_the_week` делит с
# `days_and_parts_of_day` семь слов, порог не сработал, а категория сломала
# воспроизведение референса — в записи есть группа «days of the week», и её
# надпись стала разрешаться двумя категориями сразу (тесты 8b и 12b).
# Отсюда 6: лучше лишнее предупреждение, чем сломанный слой записи.
OVERLAP_WARN = 6


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--overlap", type=int, default=OVERLAP_WARN)
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
    from word_content.normalization import normalize_word

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    taken = {row[0] for row in conn.execute("SELECT category_key FROM categories")}
    # Надписи занятых категорий. Ключ и надпись — разные вещи, и проверять надо
    # обе: моя `frozen_treats` прошла по свободному ключу, но её надпись
    # «FROZEN TREATS» уже носила `frozen_treat_brands`. Одинаковая надпись у двух
    # категорий — дефект вдвойне: игрок видит одну подпись у разных групп, а
    # мета-механика ищет родителя как раз по надписи и становится неоднозначной.
    labels = {
        row[0].strip().upper()
        for row in conn.execute("SELECT label FROM categories WHERE status='active'")
    }
    register = {
        row["normalized"]: row["everyday_class"]
        for row in conn.execute("SELECT normalized, everyday_class FROM words WHERE status='active'")
    }
    # пулы существующих категорий: только играбельные связи
    pools: dict[str, set[str]] = {}
    for row in conn.execute(
        """SELECT c.category_key AS k, w.normalized AS w FROM memberships m
             JOIN categories c ON c.id = m.category_id
             JOIN words w ON w.id = m.word_id
            WHERE m.review_status IN ('approved', 'alternative')"""
    ):
        pools.setdefault(row["k"], set()).add(row["w"])
    conn.close()

    verdicts = {"ok": 0, "дубль": 0, "занят ключ": 0}
    for line in Path(args.input).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        item = json.loads(line)
        key = item["category_key"]
        words = {normalize_word(w) for w in item.get("words", [])}
        problems: list[str] = []

        if key in taken:
            problems.append("ключ уже занят")
            verdicts["занят ключ"] += 1
        if item.get("label", "").strip().upper() in labels:
            problems.append(f"надпись уже занята: {item.get('label')}")
            verdicts["занят ключ"] += 1

        missing = sorted(w for w in words if w not in register)
        if missing:
            problems.append(f"нет в базе: {', '.join(missing)}")
        not_everyday = sorted(
            f"{w} ({register[w]})" for w in words
            if w in register and register[w] != "everyday"
        )
        if not_everyday:
            problems.append(f"не everyday: {', '.join(not_everyday)}")

        overlaps = sorted(
            ((len(words & pool), other) for other, pool in pools.items() if len(words & pool) >= args.overlap),
            reverse=True,
        )
        if overlaps:
            problems.append(
                "похоже на существующие: "
                + ", ".join(f"{other} ({n} общих)" for n, other in overlaps[:3])
            )
            verdicts["дубль"] += 1

        if problems:
            print(f"✗ {key}")
            for text in problems:
                print(f"    {text}")
        else:
            verdicts["ok"] += 1
            print(f"✓ {key}  ({len(words)} слов)")

    print(
        f"\nитог: годных {verdicts['ok']}, "
        f"дублей {verdicts['дубль']}, занятых ключей {verdicts['занят ключ']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
