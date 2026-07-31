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
import shutil
import sqlite3
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

PIPE = Path(__file__).resolve().parents[1]
REPO = PIPE.parents[1]

# Папка-выдача в корне проекта: сюда кладётся снимок базы и материалы для ревью
HANDOFF = REPO / "БАЗА-СЛОВ"
OUT = HANDOFF / "ревью"
DB_SNAPSHOT = HANDOFF / "база-слов.sqlite"

MARK = {"approved": "+", "alternative": "~", "hard_only": "!", "rejected": "x", "candidate": "?"}


def fetch(conn: sqlite3.Connection):
    conn.row_factory = sqlite3.Row
    cats = {r["category_key"]: dict(r) for r in conn.execute("SELECT * FROM categories ORDER BY theme, category_key")}
    rows = list(
        conn.execute(
            """
            SELECT c.category_key ck, w.text word, w.normalized norm, w.familiarity_score fam,
                   s.sense_key sense, s.definition sense_def, m.review_status st,
                   m.semantic_status semantic, m.gameplay_difficulty gdiff,
                   m.risk_flags flags,
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


def write_instructions(counts: dict, readiness_counts: dict, extra: dict) -> None:
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
- {extra['quartets']} проверенных четвёрок, {extra['conflicts']} запретов на сочетание категорий

Одно слово может принадлежать нескольким категориям — это и создаёт ловушки.

## Что изменилось после внешнего аудита (31.07.2026)

- **Нет частотности — нет игры.** Слово, частотность которого посчитать не удалось,
  больше не может получить `approved`: связь закрывается в `candidate`.
- **Многозначное слово всегда со значением.** Все связи слов с разведёнными значениями
  указывают конкретное значение. Исключение — категории игры слов (`___ BOARD`):
  там участвует написание, а не смысл.
- **Статусы пересчитаны по абсолютным порогам,** а не только сравнением категорий слова
  между собой. Из-за относительного сравнения `xylophone` в MUSICAL INSTRUMENTS
  и все пустыни в DESERTS раньше уезжали в `hard_only`.
- **Разделены четыре разные вещи:** семантическая корректность (`semantic_status`),
  знакомость слова (`familiarity_score`), очевидность значения (`obviousness_score`)
  и игровая сложность (`gameplay_difficulty`).
- **Появились слои, которых не было:** готовность категории (`readiness`), запреты
  на сочетание категорий (`category_conflicts`), парная структура (`category_pair_groups`)
  и проверенные четвёрки (`quartets`) с solver'ом единственности решения.
- **Заполнен слой рисков** (`risk_flags`): раньше он был пустым у всех связей.

Готовность категорий: """
        + ", ".join(f"{k} — {v}" for k, v in readiness_counts.items())
        + """.

## Что означают статусы связи

| знак | статус | смысл |
|---|---|---|
| `+` | approved | значение, которое игрок вспоминает первым; годится для любого уровня |
| `~` | alternative | верно и узнаваемо, но не первое значение: **ловушка** для обычного уровня |
| `!` | hard_only | верно, но игрок сам не догадается: только сложные уровни |
| `x` | rejected | в игру не идёт |

Пример: `monitor` -> COMPUTER PARTS это `+`, -> HOSPITAL THINGS это `~`,
-> LIZARDS (варан) это `!`.

Статус — это игровая пригодность, а не правильность. Семантическая корректность
живёт отдельно в `semantic_status`, игровая сложность — в `gameplay_difficulty`.

Статусы проставлены автоматически: сначала абсолютная заметность связи (очевидность
правила категории плюс знакомость слова), затем данные SWOW-EN (свободные ассоциации
живых людей, 12 282 стимула) как вторичный сигнал. Подробности метода — в 01_summary.md.

## О чём хочется услышать во втором круге

Первый аудит закрыт: структурные дыры (частотность, значения многозначных слов,
неполный экспорт, отсутствие слоя четвёрок и конфликтов) исправлены, `check-integrity`
проходит все блокирующие проверки. Поэтому теперь интересно другое.

Приоритет 1 — то, что машина проверить не может:

1. **Семантика связей.** `semantic_status` равен `unreviewed` у 17 479 связей из
   17 556: правило категории против слова никто не сверял глазами. Где слово
   не удовлетворяет правилу своей категории? Начинать удобно с `02_categories.md`.
2. **Правильность статусов после пересчёта.** Статусы пересчитаны по абсолютным
   порогам, и `hard_only` сократился с 2 503 до 917. Где теперь `+` стоит
   у связи, которую средний американец не увидит? Где пропущена ловушка `~`?
3. **Проверенные четвёрки.** 3 005 четвёрок в `08_quartets.csv` прошли solver
   единственности, но человек их не смотрел. Какие четвёрки читаются
   неоднозначно, скучно или требуют специальных знаний?
4. **Спорные решения.** `06_manual_decisions.md` — 74 связи помечены `disputed`
   плюс список решений, которые я принял сам. С чем не согласны?

Приоритет 2 — качество остального:

5. **Слова, незнакомые среднему американцу** — `04_flags.md`, разделы 1 и 2.
6. **Пропущенные значения слов.** 556 слов живут в четырёх и более категориях
   без разведённых значений (`03_homonyms.md` показывает, что уже разведено).
7. **Категории, непригодные для игры.** Слишком узкие, субъективные или требующие
   специальных знаний. Готовность по каждой — в `07_readiness_and_conflicts.md`.
8. **Культурные и этические риски.** `04_flags.md`, раздел 7.

Что проверять **не** нужно, это уже закрыто автоматикой и проверяется на каждой
сборке: связи без частотности, связи многозначных слов без значения, категории
без нормальной четвёрки, четвёрки с неединственным решением, полнота экспорта.

## Файлы

- `01_summary.md` — метод и цифры
- `02_categories.md` — все категории: правило и слова со статусами
- `03_homonyms.md` — разведённые значения многозначных слов
- `04_flags.md` — то, в чём меньше всего уверенности (все разделы полные)
- `05_memberships.csv` — все связи в машинном виде
- `06_manual_decisions.md` — **что осталось решить человеку**: спорная семантика,
  слова без частотности, длинные надписи, и принятые по ходу решения
- `07_readiness_and_conflicts.md` — готовность категорий, запреты на сочетание,
  парные категории, сводка по четвёркам
- `08_quartets.csv` — проверенные четвёрки с правилом категории
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
        "## Четыре разные оси, которые нельзя путать",
        "",
        "| ось | где живёт | что означает |",
        "|---|---|---|",
        "| семантическая корректность | `memberships.semantic_status` | слово удовлетворяет правилу категории |",
        "| знакомость слова | `words.familiarity_score` | как часто слово встречается в письменном английском |",
        "| очевидность значения | `memberships.obviousness_score` | быстро ли игрок увидит эту связь |",
        "| игровая сложность | `memberships.gameplay_difficulty` | насколько связь усложняет уровень |",
        "| игровая пригодность | `memberships.review_status` | куда связь можно поставить |",
        "",
        "До аудита всё это сидело в одном `review_status`, поэтому `hard_only` значил",
        "одновременно «неочевидно», «редкое слово» и «сложный уровень».",
        "",
        "## Как проставлены статусы",
        "",
        "**Шаг 1 — абсолютная заметность.** Считается независимо от других категорий",
        "слова: `0.6 × очевидность правила категории + 0.4 × знакомость слова`.",
        "Очевидность отвечает за «понятно ли правило», знакомость — за «знает ли игрок",
        "слово», и одно компенсирует другое. Категория, чьё правило само себя объясняет",
        "(MUSICAL INSTRUMENTS, DESSERTS), даёт `approved` даже редкому слову: `xylophone`",
        "редок в текстах, но игрок соберёт его с барабаном и пианино без раздумий.",
        "",
        "**Шаг 2 — SWOW-EN** (Small World of Words): 12 282 стимула, свободные ассоциации",
        "живых людей. Профиль слова это то, что люди отвечают на него и на что отвечают ему.",
        "Профиль слова сравнивается с профилем категории без этого слова. SWOW может",
        "поднять связь выше абсолютного пола, но не опустить ниже.",
        "",
        "Порядок именно такой по замечанию аудита: раньше SWOW сравнивал категории слова",
        "только между собой, и объективно очевидная связь редкого слова уезжала",
        "в `hard_only` — все пустыни, все латинские выражения, `xylophone`.",
        "",
        "Два ограничения SWOW, которые обходятся ручной разметкой:",
        "",
        "1. SWOW занижает вторичные значения известных слов: на «apple» почти никто",
        "   не отвечает «Microsoft», хотя компанию знают все.",
        "2. SWOW не видит рассудочные связи: банк ассоциируется с деньгами, а не",
        "   со школой и библиотекой, но что это здание в городе — сообразит любой.",
        "",
        "Поэтому у многозначных слов абсолютный пол не применяется вообще: там судит",
        "ручная разметка значений (`_ambiguous.json`, `_sense_map.json`). Частотность",
        "считается по написанию слова, а `monitor` в значении «варан» частотным не является.",
        "",
        "Частотность слов считается по wordfreq (шкала zipf, 0..1 после нормировки).",
        "Слова ниже 0.20 отклонены как практически не встречающиеся в английском.",
        "**Слово, частотность которого посчитать не удалось, не может стать играбельным** —",
        "связь закрывается в `candidate`. Это исправление по аудиту: раньше такие связи",
        "проходили как `approved`.",
        "",
        "## О чём `fit_score` не говорит",
        "",
        "У почти всех связей `fit_score` равен 0.97, потому что это константа из seed-файла,",
        "а не измерение. Аудит справедливо это отметил. Реальная семантическая ось —",
        "`semantic_status`; `fit_score` остаётся заявленным значением до полного ручного ревью.",
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


RARE_FAMILIARITY_UI = 0.30
THIN_PLAYABLE = 12
# Порог для «показаны не все»: если строк больше, ставим явную отсечку и говорим об этом.
# Аудит поймал ровно эту ошибку: раздел 4 молча обрезался на LIMIT 60 из 86 категорий.
MAX_TABLE_ROWS = 400


def _table(lines: list[str], header: list[str], rows: list[list[str]], total: int) -> None:
    """Пишет таблицу и, если строк больше показанного, честно об этом сообщает."""
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "---|" * len(header))
    for row in rows[:MAX_TABLE_ROWS]:
        lines.append("| " + " | ".join(row) + " |")
    if total > MAX_TABLE_ROWS:
        lines.append("")
        lines.append(
            f"Показано {MAX_TABLE_ROWS} строк из {total}. Полный список — "
            "в `05_memberships.csv` и `07_readiness_and_conflicts.md`."
        )


def write_flags(conn: sqlite3.Connection, rows: list) -> None:
    """Разделы, в которых меньше всего уверенности.

    Ни один раздел не обрезается молча: если строк больше, чем показано,
    об этом сказано прямо под таблицей.
    """
    conn.row_factory = sqlite3.Row
    rare = list(
        conn.execute(
            "SELECT text, familiarity_score f FROM words WHERE familiarity_score IS NOT NULL "
            "AND familiarity_score < ? ORDER BY familiarity_score, normalized",
            (RARE_FAMILIARITY_UI,),
        )
    )
    no_familiarity = list(
        conn.execute(
            """
            SELECT w.text word, c.category_key ck, c.label label, m.review_status st
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE w.familiarity_score IS NULL
             ORDER BY w.normalized
            """
        )
    )
    rejected = sorted({r["word"] for r in rows if r["st"] == "rejected"})
    thin = list(
        conn.execute(
            """
            SELECT c.label, c.category_key ck, c.readiness,
                   COUNT(m.id) FILTER (WHERE m.review_status IN ('approved','alternative','hard_only')) n
              FROM categories c LEFT JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id HAVING n < ? ORDER BY n, c.category_key
            """,
            (THIN_PLAYABLE,),
        )
    )
    # Знаменатель — играбельные связи, а не все: rejected не имеет отношения к тому,
    # годится ли категория для лёгкого уровня. Порога по размеру пула больше нет:
    # маленькая категория с перекосом в hard_only так же непригодна, как большая.
    hard_heavy = list(
        conn.execute(
            """
            SELECT c.label, c.category_key ck, c.readiness,
                   COUNT(m.id) FILTER (WHERE m.review_status IN ('approved','alternative','hard_only')) playable,
                   COUNT(m.id) FILTER (WHERE m.review_status = 'hard_only') hard
              FROM categories c JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id
            HAVING playable > 0 AND hard * 2 > playable
             ORDER BY hard * 1.0 / playable DESC, c.category_key
            """
        )
    )
    no_approved = list(
        conn.execute(
            """
            SELECT c.label, c.category_key ck, c.readiness,
                   COUNT(m.id) FILTER (WHERE m.review_status = 'approved') n
              FROM categories c LEFT JOIN memberships m ON m.category_id = c.id
             GROUP BY c.id HAVING n < 4 ORDER BY n, c.category_key
            """
        )
    )
    risky = list(
        conn.execute(
            """
            SELECT w.text word, c.category_key ck, m.risk_flags flags, m.review_status st
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.risk_flags LIKE '%sensitive%'
                OR m.risk_flags LIKE '%outdated_term%'
                OR m.risk_flags LIKE '%possible_duplicate%'
             ORDER BY w.normalized
            """
        )
    )

    lines = [
        "# В чём меньше всего уверенности",
        "",
        "Все разделы полные. Где показана часть строк, под таблицей сказано, сколько всего.",
        "",
        f"## 1. Редкие слова ({len(rare)})",
        "",
        f"Частотность ниже {RARE_FAMILIARITY_UI} по шкале wordfreq. Формально связи верны,",
        "но слово может быть незнакомо среднему американцу. Частотность измеряет",
        "употребимость в текстах, а не узнаваемость: `xylophone` знают все, а частотность",
        "у него 0.34. Нужен взгляд: что оставить, что убрать.",
        "",
    ]
    _table(lines, ["слово", "частотность"], [[r["text"], f"{r['f']:.3f}"] for r in rare], len(rare))

    lines += [
        "",
        f"## 2. Слова без частотности ({len(no_familiarity)})",
        "",
        "Частотность посчитать не удалось: `wordfreq` не знает слова. Такие связи",
        "автоматически закрыты в `candidate` и в игру не идут — это исправление по аудиту,",
        "раньше они проходили как `approved`. Нужно решение: слово настоящее и понятное",
        "среднему игроку — или его надо убрать.",
        "",
    ]
    _table(
        lines,
        ["слово", "категория", "статус"],
        [[r["word"], f"{r['label']} (`{r['ck']}`)", r["st"]] for r in no_familiarity],
        len(no_familiarity),
    )

    lines += [
        "",
        f"## 3. Отклонённые слова ({len(rejected)})",
        "",
        "Отклонены автоматически: частотность ниже 0.20, то есть слово практически",
        "не встречается в письменном английском. Проверить, не выброшено ли лишнее.",
        "",
        ", ".join(rejected) if rejected else "(нет)",
        "",
        f"## 4. Тонкие категории ({len(thin)})",
        "",
        f"Меньше {THIN_PLAYABLE} играбельных слов. Часть конечна по природе (сезонов правда",
        "четыре), часть просто недобрана. Колонка readiness показывает, что с этим сделал",
        "пайплайн.",
        "",
    ]
    _table(
        lines,
        ["категория", "играбельных слов", "readiness"],
        [[f"{r['label']} (`{r['ck']}`)", str(r["n"]), r["readiness"]] for r in thin],
        len(thin),
    )

    lines += [
        "",
        f"## 5. Категории с перевесом hard_only ({len(hard_heavy)})",
        "",
        "Больше половины **играбельных** связей в hard_only: лёгкий уровень из такой",
        "категории не собрать. Знаменатель — играбельные связи, `rejected` не считается.",
        "Раздел полный: раньше он молча обрезался на 60 строках.",
        "",
    ]
    _table(
        lines,
        ["категория", "hard_only / играбельных", "readiness"],
        [
            [f"{r['label']} (`{r['ck']}`)", f"{r['hard']} / {r['playable']}", r["readiness"]]
            for r in hard_heavy
        ],
        len(hard_heavy),
    )

    lines += [
        "",
        f"## 6. Категории с меньше чем четырьмя approved ({len(no_approved)})",
        "",
        "Четвёрку из одних только очевидных связей не собрать — придётся брать ловушки",
        "`alternative`. Не ошибка сама по себе, но уровень будет сложнее задуманного.",
        "",
    ]
    _table(
        lines,
        ["категория", "approved", "readiness"],
        [[f"{r['label']} (`{r['ck']}`)", str(r["n"]), r["readiness"]] for r in no_approved],
        len(no_approved),
    )

    lines += [
        "",
        f"## 7. Культурные и терминологические риски ({len(risky)})",
        "",
        "Связи с флагами `sensitive`, `outdated_term`, `possible_duplicate`. Слой рисков",
        "заполняется в `data/seed/_risk_flags.csv` плюс механически (`multiword`,",
        "`proper_noun`, `obscure`, `trademark`, `culturally_specific`) — раньше поле",
        "`risk_flags` было пустым у всех связей.",
        "",
    ]
    _table(
        lines,
        ["слово", "категория", "флаги", "статус"],
        [[r["word"], f"`{r['ck']}`", r["flags"] or "", r["st"]] for r in risky],
        len(risky),
    )

    (OUT / "04_flags.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(rows: list) -> None:
    with (OUT / "05_memberships.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["word", "normalized", "familiarity", "sense_key", "sense_definition",
             "category_key", "relation_type", "status", "semantic_status",
             "gameplay_difficulty", "fit", "obviousness", "risk_flags", "reason"]
        )
        for r in rows:
            writer.writerow(
                [r["word"], r["norm"], r["fam"] if r["fam"] is not None else "",
                 r["sense"] or "", r["sense_def"] or "", r["ck"], r["rel"], r["st"],
                 r["semantic"], r["gdiff"] if r["gdiff"] is not None else "",
                 r["fit"], r["obv"], r["flags"] or "", r["reason"]]
            )


def write_manual_decisions(conn: sqlite3.Connection) -> None:
    """Что осталось решить человеку. Аудит просил не принимать спорное автоматически."""
    conn.row_factory = sqlite3.Row
    disputed = list(
        conn.execute(
            """
            SELECT w.text word, c.label label, c.category_key ck, m.review_status st,
                   m.review_comment note
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.semantic_status = 'disputed'
             ORDER BY c.category_key, w.normalized
            """
        )
    )
    curated = list(
        conn.execute(
            "SELECT label, category_key ck, readiness_reason r FROM categories "
            "WHERE readiness = 'curated_only' ORDER BY category_key"
        )
    )
    hard_only = list(
        conn.execute(
            "SELECT label, category_key ck, readiness_reason r FROM categories "
            "WHERE readiness IN ('hard_only', 'blocked') ORDER BY readiness, category_key"
        )
    )
    candidates = list(
        conn.execute(
            """
            SELECT w.text word, c.label label, c.category_key ck
              FROM memberships m
              JOIN words w      ON w.id = m.word_id
              JOIN categories c ON c.id = m.category_id
             WHERE m.review_status = 'candidate'
             ORDER BY w.normalized
            """
        )
    )
    long_labels = list(
        conn.execute(
            """
            SELECT DISTINCT w.text word, length(w.text) n
              FROM memberships m JOIN words w ON w.id = m.word_id
             WHERE length(w.text) > 15 AND m.review_status <> 'rejected'
             ORDER BY n DESC, w.normalized
            """
        )
    )

    lines = [
        "# Что осталось решить человеку",
        "",
        "Список собран из аудита базы (31.07.2026). Подтверждённые ошибки уже исправлены",
        "в текстовых источниках; здесь то, где автоматическое решение было бы вредным:",
        "нужен носитель языка, продуктовое решение или проверка в реальном интерфейсе.",
        "",
        f"## 1. Спорная семантика ({len(disputed)} связей)",
        "",
        "Связь помечена `semantic_status = disputed`: замечание есть, но однозначно",
        "неверной её назвать нельзя. Такие связи остаются в игре — решение за человеком.",
        "",
        "| слово | категория | статус | почему спорно |",
        "|---|---|---|---|",
    ]
    for r in disputed:
        lines.append(
            f"| {r['word']} | {r['label']} (`{r['ck']}`) | {r['st']} | "
            f"{(r['note'] or '').replace('|', '/')} |"
        )

    lines += [
        "",
        f"## 2. Категории только для ручной сборки ({len(curated)})",
        "",
        "Правило парное или субъективное, поэтому случайная четвёрка из пула может",
        "не иметь одного общего смысла. Такие категории исключены из автоматической",
        "генерации: уровни для них собираются вручную (таблица `quartets`).",
        "",
        "| категория | почему |",
        "|---|---|",
    ]
    for r in curated:
        lines.append(f"| {r['label']} (`{r['ck']}`) | {r['r']} |")

    lines += [
        "",
        f"## 3. Категории, которые не собирают нормальную четвёрку ({len(hard_only)})",
        "",
        "Пул есть, но он целиком или почти целиком `hard_only`: обычный уровень из такой",
        "категории не собрать. Нужно решение: добрать понятных слов или оставить категорию",
        "только для сложных уровней.",
        "",
        "| категория | почему |",
        "|---|---|",
    ]
    for r in hard_only:
        lines.append(f"| {r['label']} (`{r['ck']}`) | {r['r']} |")

    lines += [
        "",
        f"## 4. Слова без частотности, закрытые в candidate ({len(candidates)})",
        "",
        "`wordfreq` не знает этих слов, поэтому утверждать, что средний игрок их узнает,",
        "нельзя. Связи закрыты и в игру не идут. Решение по каждому: слово настоящее",
        "и понятное — вернуть, нет — убрать из seed.",
        "",
        "| слово | категория |",
        "|---|---|",
    ]
    for r in candidates:
        lines.append(f"| {r['word']} | {r['label']} (`{r['ck']}`) |")

    lines += [
        "",
        f"## 5. Длинные надписи ({len(long_labels)})",
        "",
        "Больше 15 символов. Влезет ли в пузырь на телефоне — вопрос к реальному интерфейсу,",
        "а не к базе. Либо короткая форма для показа, либо слово убрать.",
        "",
        "| слово | символов |",
        "|---|---|",
    ]
    for r in long_labels[:150]:
        lines.append(f"| {r['word']} | {r['n']} |")
    if len(long_labels) > 150:
        lines.append("")
        lines.append(f"Показано 150 из {len(long_labels)}.")

    lines += [
        "",
        "## 6. Решения, принятые по ходу — если не согласны, скажите",
        "",
        "- **Категории игры слов без значения.** У `phrase_before`/`phrase_after` связей",
        "  многозначных слов `sense_id` оставлен пустым осознанно: `starboard` не",
        "  происходит от звезды, `keystone` — не от ключа от замка. Приписать им значение",
        "  значит внести в базу ложь. Таких связей 11, они помечены в integrity checks.",
        "- **`fit_score` не является измерением.** У 17 489 связей он равен 0.97, потому",
        "  что это константа из seed, а не оценка. Семантическая корректность вынесена",
        "  в отдельную колонку `semantic_status`; `fit_score` остаётся заявленным",
        "  значением до полного ручного ревью.",
        "- **`hard_only` стало заметно меньше** (2 503 → примерно 900). Аудит показал, что",
        "  статус был перегружен: он одновременно означал «неочевидно» и «сложно».",
        "  Игровая сложность вынесена в `gameplay_difficulty`, а `hard_only` теперь",
        "  значит только «игрок сам не догадается».",
        "- **Пингвин убран из ARCTIC ANIMALS**, а не переименована категория: пул",
        "  из полярного медведя, нарвала и оленя честнее, чем размытие правила.",
        "- **INSECTS переименована в BUGS**, потому что паук и клещ не насекомые,",
        "  а из пула их убирать жалко: игрок группирует их вместе без сомнений.",
    ]
    (OUT / "06_manual_decisions.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readiness_and_conflicts(conn: sqlite3.Connection) -> None:
    """Готовность категорий и запреты на сочетание — новый слой по аудиту."""
    conn.row_factory = sqlite3.Row
    by_readiness = list(
        conn.execute(
            "SELECT readiness, COUNT(*) n FROM categories GROUP BY readiness ORDER BY n DESC"
        )
    )
    conflicts = list(
        conn.execute(
            """
            SELECT ca.label la, ca.category_key ka, cb.label lb, cb.category_key kb,
                   x.overlap_count n, x.severity sev, x.origin origin, x.overlap_words words
              FROM category_conflicts x
              JOIN categories ca ON ca.id = x.category_a_id
              JOIN categories cb ON cb.id = x.category_b_id
             ORDER BY x.overlap_count DESC, ca.category_key
            """
        )
    )
    pairs = list(
        conn.execute(
            """
            SELECT c.label label, c.category_key ck, g.group_key gk, w.text word
              FROM category_pair_groups g
              JOIN categories c ON c.id = g.category_id
              JOIN words w      ON w.id = g.word_id
             ORDER BY c.category_key, g.group_key, g.slot
            """
        )
    )
    quartets = list(
        conn.execute(
            """
            SELECT q.review_state st, q.solver_state ss, COUNT(*) n
              FROM quartets q GROUP BY q.review_state, q.solver_state
            """
        )
    )

    lines = [
        "# Готовность категорий, конфликты и четвёрки",
        "",
        "Три слоя, которых в базе не было и которые требовал аудит.",
        "",
        "## 1. Готовность категорий",
        "",
        "Выводится из пулов командой `derive-readiness`, руками не пишется.",
        "",
        "| readiness | что значит | категорий |",
        "|---|---|---|",
    ]
    meaning = {
        "ready": "4+ слов уровня, пул не перекошен — годится для автогенерации",
        "constrained": "годится, но пул тонкий, перекошен в hard_only или мало approved",
        "curated_only": "правило парное или субъективное: только ручные четвёрки",
        "hard_only": "нормальных слов меньше четырёх: только сложные уровни",
        "blocked": "четвёрку не собрать даже с hard_only: категория отключена",
        "unknown": "не посчитано",
    }
    for r in by_readiness:
        lines.append(f"| `{r['readiness']}` | {meaning.get(r['readiness'], '')} | {r['n']} |")

    lines += [
        "",
        f"## 2. Конфликты категорий ({len(conflicts)})",
        "",
        "Пары, которые нельзя ставить в один уровень: их пулы пересекаются так, что",
        "четвёрка из одной целиком лежит в другой, и у уровня появляется второй",
        "корректный ответ. `derived` — посчитано по пересечению пулов, `manual` — решение",
        "человека из `_category_meta.json`.",
        "",
        "| A | B | общих слов | серьёзность | источник |",
        "|---|---|---|---|---|",
    ]
    for r in conflicts[:200]:
        lines.append(
            f"| {r['la']} (`{r['ka']}`) | {r['lb']} (`{r['kb']}`) | {r['n']} | "
            f"{r['sev'] or ''} | {r['origin']} |"
        )
    if len(conflicts) > 200:
        lines.append("")
        lines.append(f"Показано 200 из {len(conflicts)}. Полный список — в базе, таблица `category_conflicts`.")

    if conflicts:
        lines += [
            "",
            "Самое крупное пересечение:",
            "",
            f"- **{conflicts[0]['la']}** и **{conflicts[0]['lb']}**: {conflicts[0]['n']} общих слов",
            f"  — {conflicts[0]['words']}",
        ]

    grouped: dict[str, list[str]] = defaultdict(list)
    labels: dict[str, str] = {}
    for r in pairs:
        grouped[r["gk"]].append(r["word"])
        labels[r["gk"]] = f"{r['label']} (`{r['ck']}`)"
    lines += [
        "",
        f"## 3. Парные категории ({len(grouped)} пар)",
        "",
        "OPPOSITES — это не пул из 26 слов, а 13 пар. Четвёрка для такой категории",
        "собирается только как две полные пары, иначе четыре случайных слова не образуют",
        "понятного правила.",
        "",
    ]
    for gk in sorted(grouped):
        lines.append(f"- {labels[gk]}: {' / '.join(grouped[gk])}")

    lines += [
        "",
        "## 4. Проверенные четвёрки",
        "",
        "База хранит пулы, игре нужны решения. Четвёрка попадает сюда, только если",
        "solver подтвердил: этих четырёх слов нет целиком ни в одной другой категории.",
        "",
        "| review_state | solver_state | четвёрок |",
        "|---|---|---|",
    ]
    for r in quartets:
        lines.append(f"| {r['st']} | {r['ss']} | {r['n']} |")
    lines += [
        "",
        "`auto_validated` значит «solver прошёл, человек не смотрел». Статус",
        "`human_approved` ставится только вручную — это и есть следующий шаг ревью.",
        "Сами четвёрки — в `08_quartets.csv`.",
    ]
    (OUT / "07_readiness_and_conflicts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_quartets_csv(conn: sqlite3.Connection) -> None:
    conn.row_factory = sqlite3.Row
    rows = list(
        conn.execute(
            """
            SELECT q.quartet_key, c.category_key, c.label, c.rule, q.tier,
                   q.review_state, q.solver_state, q.difficulty,
                   GROUP_CONCAT(w.text, ' | ') words
              FROM quartets q
              JOIN categories c    ON c.id = q.category_id
              JOIN quartet_words qw ON qw.quartet_id = q.id
              JOIN words w         ON w.id = qw.word_id
             GROUP BY q.id
             ORDER BY c.theme, c.category_key, q.quartet_key
            """
        )
    )
    with (OUT / "08_quartets.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["quartet_key", "category_key", "label", "rule", "tier",
             "review_state", "solver_state", "difficulty", "words"]
        )
        for r in rows:
            writer.writerow(
                [r["quartet_key"], r["category_key"], r["label"], r["rule"], r["tier"],
                 r["review_state"], r["solver_state"],
                 r["difficulty"] if r["difficulty"] is not None else "", r["words"]]
            )


def write_handoff_readme(counts: dict, db_size_mb: float, source_db: Path) -> None:
    """README на русском: чтобы через месяц было понятно, что здесь лежит."""
    stamp = datetime.now(UTC).strftime("%d.%m.%Y")
    (HANDOFF / "README.md").write_text(
        f"""# База слов игры — текущее состояние

Снимок от {stamp}.

## Где что лежит

| файл | что это |
|---|---|
| `база-слов.sqlite` | **сама база**, файл SQLite ({db_size_mb:.1f} МБ). Открывается любым просмотрщиком SQLite, например DB Browser for SQLite |
| `ревью/` | материалы для проверки базы человеком или внешней моделью |

## Что внутри базы

- категорий: **{counts['categories']}** в {counts['themes']} темах
- уникальных слов: **{counts['words']}**
- связей слово-категория: **{counts['memberships']}**
- значений у многозначных слов: **{counts['senses']}** (у {counts['sense_words']} слов)
- слов в двух и более категориях: **{counts['multi']}** ({counts['multi_pct']}%)

Таблицы:

| таблица | что внутри |
|---|---|
| `words` | слова с частотностью |
| `word_senses` | значения многозначных слов |
| `categories` | категории с правилом и готовностью (`readiness`) |
| `memberships` | связи слово-категория: статус, семантика, игровая сложность, риски |
| `category_conflicts` | пары категорий, которые нельзя ставить в один уровень |
| `category_pair_groups` | структура парных категорий (OPPOSITES — это пары, а не пул) |
| `quartets`, `quartet_words` | проверенные игровые четвёрки |
| `schema_meta` | версия схемы и контента, commit, хеши источников |
| `import_runs`, `generation_runs` | журнал: что и откуда загружалось |

## Важно: это снимок, а не рабочая база

Рабочая база живёт здесь:

```
tool/word_content_pipeline/database/content.sqlite
```

Она **пересобирается из текстовых файлов** и в git не хранится — так сделано,
чтобы источником правды были читаемые файлы, а не бинарник. Источник правды:

```
tool/word_content_pipeline/data/seed/*.txt              категории и пулы слов
tool/word_content_pipeline/data/seed/_ambiguous.json    значения многозначных слов
tool/word_content_pipeline/data/seed/_sense_map.json    какое значение у какой связи
tool/word_content_pipeline/data/seed/_semantic_review.csv  семантические решения
tool/word_content_pipeline/data/seed/_risk_flags.csv    культурные и правовые риски
tool/word_content_pipeline/data/seed/_category_meta.json   парные категории, запреты
tool/word_content_pipeline/data/review_decisions.csv    статусы всех связей
```

## Как обновить этот снимок

Из папки `tool/word_content_pipeline`:

```bash
.venv/bin/python scripts/build_seed.py                    # собрать JSONL из data/seed
.venv/bin/python scripts/swow_status.py                   # проставить статусы связей
.venv/bin/word-content init-db            --db database/content.sqlite
.venv/bin/word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
.venv/bin/word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
.venv/bin/word-content import-review      --db database/content.sqlite --input data/review_decisions.csv
.venv/bin/word-content derive-readiness   --db database/content.sqlite
.venv/bin/word-content derive-conflicts   --db database/content.sqlite --output data/category_conflicts.csv
.venv/bin/word-content build-quartets     --db database/content.sqlite --output data/quartets.csv
.venv/bin/word-content stamp-version      --db database/content.sqlite --content-version ГГГГ.ММ.ДД
.venv/bin/word-content check-integrity    --db database/content.sqlite   # обязательно: ненулевой код = не отдавать
.venv/bin/python scripts/export_review_pack.py            # обновить эту папку
```

Последняя команда пересобирает и снимок базы, и папку `ревью/`.
`check-integrity` — это критерии приёмки из внешнего аудита в виде кода: если он
падает, снимок отдавать нельзя.

## Как посмотреть базу без программиста

1. Поставить **DB Browser for SQLite** (бесплатный, sqlitebrowser.org)
2. Открыть `база-слов.sqlite`
3. Вкладка Browse Data, таблица `memberships` — все связи; `categories` — категории

Или из терминала, если нужно быстро глянуть одно слово:

```bash
cd tool/word_content_pipeline
PYTHONPATH=src .venv/bin/word-content word-info --db ../../БАЗА-СЛОВ/база-слов.sqlite --word monitor
```
""",
        encoding="utf-8",
    )


def snapshot_db(source: Path) -> float:
    """Копирует базу, предварительно сжав её (VACUUM убирает мусор от импортов)."""
    conn = sqlite3.connect(source)
    try:
        conn.execute("VACUUM")
    finally:
        conn.close()
    shutil.copy2(source, DB_SNAPSHOT)
    for suffix in ("-wal", "-shm"):
        stale = DB_SNAPSHOT.with_name(DB_SNAPSHOT.name + suffix)
        if stale.exists():
            stale.unlink()
    return DB_SNAPSHOT.stat().st_size / 1024 / 1024


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(PIPE / "database" / "content.sqlite"))
    args = parser.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
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

    readiness_counts = {
        row[0]: row[1]
        for row in conn.execute(
            "SELECT readiness, COUNT(*) FROM categories GROUP BY readiness ORDER BY COUNT(*) DESC"
        )
    }
    extra = {
        "quartets": conn.execute("SELECT COUNT(*) FROM quartets").fetchone()[0],
        "conflicts": conn.execute("SELECT COUNT(*) FROM category_conflicts").fetchone()[0],
    }

    write_instructions(counts, readiness_counts, extra)
    write_summary(counts, by_status, {k: tuple(v) for k, v in by_theme.items()})
    write_categories(cats, rows)
    write_homonyms(rows)
    write_flags(conn, rows)
    write_csv(rows)
    write_manual_decisions(conn)
    write_readiness_and_conflicts(conn)
    write_quartets_csv(conn)
    conn.close()

    db_size = snapshot_db(Path(args.db))
    write_handoff_readme(counts, db_size, Path(args.db))

    print(f"папка-выдача: {HANDOFF}")
    print(f"  README.md")
    print(f"  база-слов.sqlite         {db_size:.1f} МБ")
    print(f"  ревью/")
    for path in sorted(OUT.iterdir()):
        print(f"    {path.name:26} {path.stat().st_size // 1024:>5} КБ")


if __name__ == "__main__":
    main()
