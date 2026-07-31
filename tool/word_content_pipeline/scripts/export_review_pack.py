#!/usr/bin/env python3
"""Собирает пакет файлов для внешнего ревью базы (например, в ChatGPT).

Задача пакета — дать ревьюеру всё, что нужно для суждения, и ничего лишнего:
правило категории, слова с их статусами, разведённые значения и отдельно то,
в чём я сам меньше всего уверен.

Запуск:
    python scripts/export_review_pack.py --db database/content.sqlite
Результат: review/ рядом с корнем проекта.
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import defaultdict
from pathlib import Path

PIPE = Path(__file__).resolve().parents[1]
OUT = PIPE / "review"

MARK = {"approved": "+", "alternative": "~", "hard_only": "!", "rejected": "x", "candidate": "?"}


def fetch(conn: sqlite3.Connection):
    conn.row_factory = sqlite3.Row
    cats = {r["category_key"]: dict(r) for r in conn.execute("SELECT * FROM categories ORDER BY theme, category_key")}
    rows = list(
        conn.execute(
            """
            SELECT c.category_key ck, w.text word, w.normalized norm, w.familiarity_score fam,
                   s.sense_key sense, s.definition sense_def, m.review_status st,
                   m.obviousness_score obv, m.fit_score fit, m.relation_type rel, m.reason
              FROM memberships m
              JOIN words w ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
              LEFT JOIN word_senses s ON s.id = m.sense_id
             ORDER BY c.theme, c.category_key, m.review_status, w.normalized
            """
        )
    )
    return cats, rows


def write_instructions(counts: dict) -> None:
    (OUT / "00_INSTRUCTIONS.md").write_text(
        f"""# Ревью базы слов для игры-головоломки на словесных ассоциациях

## Что за игра

Игрок видит поле пузырей со словами. Названия категорий скрыты. Нужно сгруппировать
слова по категориям, догадавшись о принципе. Категория в уровне — ровно 4 слова.
Аудитория: средний взрослый американец, casual-игрок, без специальных знаний.

## Что в базе

- {counts['categories']} категорий в {counts['themes']} темах
- {counts['words']} уникальных слов
- {counts['memberships']} связей слово-категория
- {counts['senses']} значений у {counts['sense_words']} многозначных слов

Одно слово может принадлежать нескольким категориям — это и создаёт ловушки.

## Что означают статусы связи

| знак | статус | смысл |
|---|---|---|
| `+` | approved | значение, которое игрок вспоминает первым; годится для любого уровня |
| `~` | alternative | верно и узнаваемо, но не первое значение: **ловушка** для обычного уровня |
| `!` | hard_only | верно, но игрок сам не догадается: только сложные уровни |
| `x` | rejected | в игру не идёт |

Пример: `monitor` -> COMPUTER PARTS это `+`, -> HOSPITAL THINGS это `~`,
-> LIZARDS (варан) это `!`.

Статусы проставлены автоматически по данным SWOW-EN (свободные ассоциации живых
людей, 12 282 стимула): профиль слова сравнивается с профилем категории.
Подробности метода — в 01_summary.md.

## О чём хочется услышать

1. **Ошибки в правилах категорий.** Правило должно однозначно определять, входит
   слово в категорию или нет. Где правило шире или уже своего названия?
2. **Слова, не удовлетворяющие правилу своей категории.** Формально неверные связи.
3. **Неправильные статусы.** Где `+` стоит у связи, которую средний американец
   не увидит? Где `!` стоит у очевидного? Где пропущена ловушка `~`?
4. **Слова, незнакомые среднему американцу.** Отдельно они собраны в 04_flags.md.
5. **Пропущенные значения слов.** Многозначные слова, у которых значения не
   разведены (файл 03_homonyms.md показывает, что уже разведено).
6. **Категории, непригодные для игры.** Слишком узкие, субъективные, требующие
   специальных знаний, или такие, где 4 слова не собрать без повторов.
7. **Культурные и этические риски.** Слова и категории, способные задеть.

## Файлы

- `01_summary.md` — метод и цифры
- `02_categories.md` — все категории: правило и слова со статусами
- `03_homonyms.md` — разведённые значения многозначных слов
- `04_flags.md` — то, в чём меньше всего уверенности
- `05_memberships.csv` — все связи в машинном виде
""",
        encoding="utf-8",
    )


def write_summary(counts: dict, by_status: dict, by_theme: dict) -> None:
    lines = [
        "# База слов: цифры и метод",
        "",
        "## Объём",
        "",
        f"- категорий: **{counts['categories']}** в {counts['themes']} темах",
        f"- уникальных слов: **{counts['words']}**",
        f"- связей слово-категория: **{counts['memberships']}**",
        f"- значений: **{counts['senses']}** у {counts['sense_words']} слов",
        f"- слов в двух и более категориях: **{counts['multi']}** ({counts['multi_pct']}%)",
        "",
        "## Статусы связей",
        "",
        "| статус | связей |",
        "|---|---|",
    ]
    for st in ("approved", "alternative", "hard_only", "rejected", "candidate"):
        if by_status.get(st):
            lines.append(f"| `{st}` | {by_status[st]} |")
    lines += [
        "",
        "## Как проставлены статусы",
        "",
        "Источник — SWOW-EN (Small World of Words): 12 282 стимула, свободные",
        "ассоциации живых людей. Профиль слова это то, что люди отвечают на него",
        "и на что отвечают им. Слова одной категории похожи профилями, даже если",
        "напрямую друг с другом не ассоциируются, поэтому профиль слова сравнивается",
        "с профилем категории без этого слова.",
        "",
        "У слова сравниваются его же категории между собой: лучшая идёт в `approved`,",
        "заметно слабее — в `alternative`, почти без связи — в `hard_only`.",
        "",
        "Два известных ограничения метода, которые обошли вручную:",
        "",
        "1. SWOW занижает вторичные значения известных слов: на «apple» почти никто",
        "   не отвечает «Microsoft», хотя компанию знают все. Поэтому порог",
        "   `alternative` низкий, а ручная разметка омонимов сильнее данных.",
        "2. SWOW не видит рассудочные связи: банк ассоциируется с деньгами, а не",
        "   со школой и библиотекой, но что это здание в городе — сообразит любой.",
        "   Поэтому в прозрачных категориях связь не опускается ниже `alternative`.",
        "",
        "Частотность слов считается по wordfreq (шкала zipf, 0..1 после нормировки).",
        "Слова ниже 0.20 отклонены как практически не встречающиеся в английском.",
        "",
        "## Категорий по темам",
        "",
        "| тема | категорий | связей |",
        "|---|---|---|",
    ]
    for theme, (n_cat, n_mem) in sorted(by_theme.items(), key=lambda kv: -kv[1][0]):
        lines.append(f"| {theme} | {n_cat} | {n_mem} |")
    (OUT / "01_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


HEADER = (
    "Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.\n"
    "В скобках после слова — значение, если у слова разведены значения.\n"
)


def write_categories(cats: dict, rows: list, parts: int = 4) -> None:
    """Пишет полный файл и разбитые по темам части: 373 КБ целиком съедают контекст."""
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["ck"]].append(r)

    blocks: dict[str, list[str]] = defaultdict(list)
    for key, cat in cats.items():
        words = []
        for r in by_cat.get(key, []):
            mark = MARK.get(r["st"], "?")
            sense = f" ({r['sense']})" if r["sense"] else ""
            words.append(f"{mark}{r['word']}{sense}")
        blocks[cat["theme"]] += [
            f"### {cat['label']}  `{key}`",
            f"- правило: {cat['rule']}",
            f"- тип связи: `{cat['relation_type']}`, базовая сложность {cat['base_difficulty']}",
            f"- слов: {len(words)}",
            "- " + ", ".join(words),
            "",
        ]

    def render(themes: list[str], title: str) -> str:
        out = [f"# {title}", "", HEADER]
        for theme in themes:
            out += ["", f"## Тема: {theme}", ""] + blocks[theme]
        return "\n".join(out) + "\n"

    themes = sorted(blocks, key=lambda t: -sum(len(b) for b in blocks[t]))
    (OUT / "02_categories.md").write_text(
        render(sorted(blocks), "Категории: правило и слова"), encoding="utf-8"
    )

    # раскладываем темы по частям примерно равного размера
    sizes = {t: sum(len(x) for x in blocks[t]) for t in themes}
    buckets: list[list[str]] = [[] for _ in range(parts)]
    loads = [0] * parts
    for theme in themes:
        i = loads.index(min(loads))
        buckets[i].append(theme)
        loads[i] += sizes[theme]
    for i, bucket in enumerate(buckets, start=1):
        (OUT / f"02_categories_part{i}.md").write_text(
            render(sorted(bucket), f"Категории, часть {i} из {parts}"), encoding="utf-8"
        )


def write_homonyms(rows: list) -> None:
    by_word = defaultdict(list)
    for r in rows:
        if r["sense"]:
            by_word[r["norm"]].append(r)

    lines = [
        "# Разведённые значения многозначных слов",
        "",
        f"Слов: **{len(by_word)}**. Одно написание — разные значения, каждое со своими",
        "категориями. Это главный источник ловушек в игре.",
        "",
        "Знаки статуса: `+` approved, `~` alternative, `!` hard_only, `x` rejected.",
        "",
    ]
    for word in sorted(by_word):
        entries = by_word[word]
        senses = defaultdict(list)
        defs = {}
        for r in entries:
            senses[r["sense"]].append(f"{MARK.get(r['st'], '?')}{r['ck']}")
            defs[r["sense"]] = r["sense_def"]
        lines.append(f"## {word.upper()}")
        for sense, cats in sorted(senses.items()):
            lines.append(f"- **{sense}** — {defs[sense]}")
            lines.append(f"  - {', '.join(sorted(cats))}")
        lines.append("")
    (OUT / "03_homonyms.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_flags(conn: sqlite3.Connection, rows: list) -> None:
    conn.row_factory = sqlite3.Row
    rare = list(
        conn.execute(
            "SELECT text, familiarity_score f FROM words WHERE familiarity_score < 0.30 "
            "ORDER BY familiarity_score LIMIT 400"
        )
    )
    rejected = sorted({r["word"] for r in rows if r["st"] == "rejected"})
    thin = list(
        conn.execute(
            """
            SELECT c.label, c.category_key ck,
                   COUNT(m.id) FILTER (WHERE m.review_status IN ('approved','alternative','hard_only')) n
              FROM categories c LEFT JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id HAVING n < 12 ORDER BY n
            """
        )
    )
    hard_heavy = list(
        conn.execute(
            """
            SELECT c.label, c.category_key ck, COUNT(m.id) total,
                   COUNT(m.id) FILTER (WHERE m.review_status = 'hard_only') hard
              FROM categories c JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id HAVING hard * 2 > total AND total >= 8
             ORDER BY hard * 1.0 / total DESC LIMIT 60
            """
        )
    )

    lines = [
        "# В чём меньше всего уверенности",
        "",
        "## 1. Редкие слова",
        "",
        "Частотность ниже 0.30 по шкале wordfreq. Формально связи верны, но слово",
        "может быть незнакомо среднему американцу. Нужен взгляд: что оставить,",
        "что убрать.",
        "",
        f"Всего таких слов: {len(rare)} (показаны самые редкие).",
        "",
        "| слово | частотность |",
        "|---|---|",
    ]
    for r in rare[:200]:
        lines.append(f"| {r['text']} | {r['f']:.3f} |")

    lines += [
        "",
        f"## 2. Отклонённые слова ({len(rejected)})",
        "",
        "Отклонены автоматически: частотность ниже 0.20, то есть слово практически",
        "не встречается в письменном английском. Проверить, не выброшено ли лишнее.",
        "",
        ", ".join(rejected),
        "",
        f"## 3. Тонкие категории ({len(thin)})",
        "",
        "Меньше 12 пригодных слов. Часть конечна по природе (сезонов правда четыре),",
        "часть просто недобрана.",
        "",
        "| категория | пригодных слов |",
        "|---|---|",
    ]
    for r in thin:
        lines.append(f"| {r['label']} (`{r['ck']}`) | {r['n']} |")

    lines += [
        "",
        f"## 4. Категории, где больше половины связей hard_only ({len(hard_heavy)})",
        "",
        "Такая категория почти не годится для лёгких уровней. Либо правило слишком",
        "хитрое, либо слова подобраны неудачно.",
        "",
        "| категория | hard_only / всего |",
        "|---|---|",
    ]
    for r in hard_heavy:
        lines.append(f"| {r['label']} (`{r['ck']}`) | {r['hard']} / {r['total']} |")

    (OUT / "04_flags.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(rows: list) -> None:
    with (OUT / "05_memberships.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["word", "normalized", "familiarity", "sense_key", "sense_definition",
             "category_key", "relation_type", "status", "fit", "obviousness", "reason"]
        )
        for r in rows:
            writer.writerow(
                [r["word"], r["norm"], r["fam"] if r["fam"] is not None else "",
                 r["sense"] or "", r["sense_def"] or "", r["ck"], r["rel"], r["st"],
                 r["fit"], r["obv"], r["reason"]]
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(PIPE / "database" / "content.sqlite"))
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    conn = sqlite3.connect(args.db)
    cats, rows = fetch(conn)

    by_status: dict[str, int] = defaultdict(int)
    for r in rows:
        by_status[r["st"]] += 1
    by_theme: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for key, cat in cats.items():
        by_theme[cat["theme"]][0] += 1
    for r in rows:
        by_theme[cats[r["ck"]]["theme"]][1] += 1

    words = {r["norm"] for r in rows}
    per_word: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        per_word[r["norm"]].add(r["ck"])
    multi = sum(1 for v in per_word.values() if len(v) > 1)
    sense_words = {r["norm"] for r in rows if r["sense"]}

    counts = {
        "categories": len(cats),
        "themes": len(by_theme),
        "words": len(words),
        "memberships": len(rows),
        "senses": conn.execute("SELECT COUNT(*) FROM word_senses").fetchone()[0],
        "sense_words": len(sense_words),
        "multi": multi,
        "multi_pct": round(multi * 100 / len(words)),
    }

    write_instructions(counts)
    write_summary(counts, by_status, {k: tuple(v) for k, v in by_theme.items()})
    write_categories(cats, rows)
    write_homonyms(rows)
    write_flags(conn, rows)
    write_csv(rows)
    conn.close()

    print(f"пакет собран: {OUT}")
    for path in sorted(OUT.iterdir()):
        print(f"  {path.name:24} {path.stat().st_size // 1024:>5} КБ")


if __name__ == "__main__":
    main()
