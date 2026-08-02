#!/usr/bin/env python3
"""Снимок связности четвёрок по SWOW: считается офлайн, в базу едет готовым.

Зачем снимок, а не чтение датасета генератором. SWOW-EN лежит локально
(`reference/swow/`, 144 МБ, лицензия research-only, в git не идёт). Если бы
генератор читал его сам, чистая сборка на машине без датасета давала бы другой
результат — то есть база перестала бы быть воспроизводимым артефактом. Поэтому
здесь research-команда, а её результат — файл в источниках правды.

Сила связи пары: sym(a,b) = s(a->b) + s(b->a), где s — доля взвешенных ответов
на стимул (R1 вес 1.0, R2/R3 вес 0.5). Формула та же, что в
`tool/scripts/swow_source.py` и в оценщике уровней; расходиться им нельзя.

Ключевое различие, ради которого снимок хранит два числа вместо одного флага:

    observed_pairs = 0   пару НЕЧЕМ было измерить: ни одно слово не встречалось
                         в датасете как стимул. Это пробел в чужих данных.
    positive_pairs = 0   пары измерялись, связи нет. Это уже свойство четвёрки.

Смешивать их нельзя. Отклонять четвёрку за первое значит наказывать её за то,
что кто-то не включил слово в опрос.

Запуск (из tool/word_content_pipeline):

    .venv/bin/python scripts/swow_quartet_metrics.py \
        --db database/content.sqlite \
        --output data/content/swow_quartet_metrics.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import pickle
import sqlite3
import sys
from itertools import combinations
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
AGG = REPO / "reference" / "swow" / "swow_agg.pkl"

# Версия формулы. Меняется вместе с формулой, и только вместе с ней: снимок,
# посчитанный старой версией, обязан быть отличим от нового.
METRIC_VERSION = "swow-quartet/1.0"
SOURCE_VERSION = "SWOW-EN.R100.20180827"

COLUMNS = [
    "quartet_key",
    "metric_version",
    "source_version",
    "source_hash",
    "observed_nodes",
    "observed_pairs",
    "positive_pairs",
    "strongest_edge",
    "median_edge",
    "disconnected",
]


def load_aggregate(path: Path) -> tuple[dict, dict, str]:
    if not path.exists():
        sys.exit(
            f"Нет агрегата SWOW ({path}). Он локальный и в git не идёт.\n"
            "Собрать: python3 tool/scripts/swow_source.py build"
        )
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()[:16]
    data = pickle.loads(payload)
    return data["fwd"], data.get("bwd", {}), digest


def metrics_for(words: list[str], fwd: dict, cues: set[str], known: set[str]) -> dict:
    """Метрики одной четвёрки. Слова уже нормализованы."""
    edges: list[float] = []
    observed = 0
    for first, second in combinations(words, 2):
        # Пара измерима, если хотя бы одно слово побывало стимулом: только тогда
        # у нас вообще были шансы увидеть связь.
        if first in cues or second in cues:
            observed += 1
            edges.append(
                fwd.get(first, {}).get(second, 0.0) + fwd.get(second, {}).get(first, 0.0)
            )
    positive = [value for value in edges if value > 0]
    return {
        "observed_nodes": sum(1 for word in words if word in known),
        "observed_pairs": observed,
        "positive_pairs": len(positive),
        "strongest_edge": round(max(edges), 6) if edges else 0.0,
        "median_edge": round(median(edges), 6) if edges else 0.0,
        # Флаг для отклонения конкретной четвёрки: измеряли и не нашли.
        "disconnected": int(observed > 0 and not positive),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="database/content.sqlite")
    parser.add_argument("--output", default="data/content/swow_quartet_metrics.csv")
    parser.add_argument("--swow", default=str(AGG))
    args = parser.parse_args()

    fwd, bwd, digest = load_aggregate(Path(args.swow))
    cues = set(fwd)
    known = cues | set(bwd)

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    grouped: dict[str, list[str]] = {}
    for row in conn.execute(
        """
        SELECT q.quartet_key AS quartet_key, w.normalized AS word
          FROM quartets q
          JOIN quartet_words qw ON qw.quartet_id = q.id
          JOIN words w          ON w.id = qw.word_id
         ORDER BY q.quartet_key, qw.slot
        """
    ):
        grouped.setdefault(row["quartet_key"], []).append(row["word"])

    rows = []
    for quartet_key, words in sorted(grouped.items()):
        if len(words) < 2:
            continue
        rows.append(
            {
                "quartet_key": quartet_key,
                "metric_version": METRIC_VERSION,
                "source_version": SOURCE_VERSION,
                "source_hash": digest,
                **metrics_for(words, fwd, cues, known),
            }
        )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    no_data = sum(1 for row in rows if row["observed_pairs"] == 0)
    dead = sum(1 for row in rows if row["positive_pairs"] == 0)
    print(f"четвёрок: {len(rows)}, снимок: {output}")
    print(f"нечем измерить: {no_data}")
    print(f"без единой связи: {dead} ({dead / max(len(rows), 1):.1%})")
    print(f"источник: {SOURCE_VERSION} {digest}, формула: {METRIC_VERSION}")


if __name__ == "__main__":
    main()
