#!/usr/bin/env python3
"""Устаревший замер покрытия референса. Пользуйтесь CLI пайплайна.

Этот скрипт отвечал на три вопроса: есть ли слово, есть ли концепт, есть ли
связь. Двух вещей он не умел, и обе оказались решающими.

1. **Сопоставлял категории по имени.** Для 71 группы из 95 на уровнях 1-10 имя
   не прочитано с пузыря, а придумано нами по четвёрке. Сравнение по такому
   имени измеряет совпадение базы с нашими же догадками, а не с оригиналом.
2. **Не видел уровня целиком.** Формы токенов, мета-зависимости и сам факт
   «уровень собирается» в замер не входили, а именно они и не работали.

Замена: `word-content reference-coverage`. Она считает observed и inferred
надписи разными проверками, знает про формы и мета-ссылки и отвечает на главный
вопрос — воспроизводится ли уровень целиком с нулевым diff.

    cd tool/word_content_pipeline
    .venv/bin/word-content reference-coverage --db database/content.sqlite \
        --max-level 10 --output ../docs/reference_reproduction/coverage_1_10.json

Барьер, который блокирует генерацию нового контента:

    .venv/bin/word-content reference-gate --db database/content.sqlite --max-level 10
"""

from __future__ import annotations

import sys


def main() -> int:
    sys.stderr.write((__doc__ or "") + "\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
