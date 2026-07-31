# База слов игры — текущее состояние

Снимок от 31.07.2026.

## Где что лежит

| файл | что это |
|---|---|
| `база-слов.sqlite` | **сама база**, файл SQLite (9.6 МБ). Открывается любым просмотрщиком SQLite, например DB Browser for SQLite |
| `ревью/` | материалы для проверки базы человеком или внешней моделью |

## Что внутри базы

- категорий: **1093** в 58 темах
- уникальных слов: **10007**
- связей слово-категория: **17556**
- значений у многозначных слов: **564** (у 222 слов)
- слов в двух и более категориях: **3466** (35%)

Шесть таблиц: `words` (слова), `word_senses` (значения слов), `categories`
(категории с правилами), `memberships` (связи слово-категория со статусом),
`import_runs` и `generation_runs` (журнал: что и откуда загружалось).

## Важно: это снимок, а не рабочая база

Рабочая база живёт здесь:

```
tool/word_content_pipeline/database/content.sqlite
```

Она **пересобирается из текстовых файлов** и в git не хранится — так сделано,
чтобы источником правды были читаемые файлы, а не бинарник. Источник правды:

```
tool/word_content_pipeline/data/seed/*.txt        категории и пулы слов
tool/word_content_pipeline/data/seed/_ambiguous.json   значения многозначных слов
tool/word_content_pipeline/data/review_decisions.csv   статусы всех связей
```

## Как обновить этот снимок

Из папки `tool/word_content_pipeline`:

```bash
.venv/bin/python scripts/build_seed.py                    # собрать JSONL из data/seed
.venv/bin/python scripts/swow_status.py                   # проставить статусы по SWOW
.venv/bin/word-content init-db            --db database/content.sqlite
.venv/bin/word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
.venv/bin/word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
.venv/bin/word-content import-review      --db database/content.sqlite --input data/review_decisions.csv
.venv/bin/python scripts/export_review_pack.py            # обновить эту папку
```

Последняя команда пересобирает и снимок базы, и папку `ревью/`.

## Как посмотреть базу без программиста

1. Поставить **DB Browser for SQLite** (бесплатный, sqlitebrowser.org)
2. Открыть `база-слов.sqlite`
3. Вкладка Browse Data, таблица `memberships` — все связи; `categories` — категории

Или из терминала, если нужно быстро глянуть одно слово:

```bash
cd tool/word_content_pipeline
PYTHONPATH=src .venv/bin/word-content word-info --db ../../БАЗА-СЛОВ/база-слов.sqlite --word monitor
```
