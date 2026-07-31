# База слов игры — текущее состояние

Снимок от 31.07.2026.

## Где что лежит

| файл | что это |
|---|---|
| `ревью/` | материалы для проверки базы человеком или внешней моделью |

Сама база — один файл `tool/word_content_pipeline/database/content.sqlite`
(10.4 МБ), он лежит в git. Открывается любым просмотрщиком SQLite,
например DB Browser for SQLite. Копии базы в этой папке больше нет: два файла с
одинаковым содержимым только путали, какой из них актуален.

## Что внутри базы

- категорий: **1276** в 58 темах
- уникальных слов: **10441**
- связей слово-категория: **18775**
- значений у многозначных слов: **588** (у 231 слов)
- слов в двух и более категориях: **3758** (36%)

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
tool/word_content_pipeline/data/runs/*/                 прогоны: кандидаты + решения ревью
```

## Как обновить этот снимок

Из папки `tool/word_content_pipeline` — одна команда:

```bash
bash scripts/rebuild_all.sh
```

Она собирает JSONL из `data/seed`, пересчитывает статусы связей по SWOW, создаёт
базу С НУЛЯ (старая уезжает в `database/backup/`), импортирует seed и все прогоны
из `data/runs/`, применяет решения ревью, считает `readiness`, запреты на сочетание
категорий и проверенные четвёрки, ставит версию и прогоняет приёмку.

`check-integrity` в конце — критерии внешнего аудита в виде кода: ненулевой код
возврата означает, что базу отдавать нельзя.

Почему одной командой, а не списком из десяти. Именно на списке проект уже
разошёлся: пересборку делали руками, а веб-инструмент читал снимок из другой
копии пайплайна, оставшейся на состоянии до аудита. Плюс `init-db` старую базу
не чистит, поэтому сборка «поверх» давала не замену связей, а вторые экземпляры.

После пересборки обновить выгрузки:

```bash
.venv/bin/python scripts/export_review_pack.py        # эту папку (снимок + ревью/)
python3 ../scripts/export_base_json.py                # tool/data/categories.json для скиллов
python3 ../level-tool/scripts/export_snapshot.py      # снимок для веб-инструмента
```

## Как посмотреть базу без программиста

1. Поставить **DB Browser for SQLite** (бесплатный, sqlitebrowser.org)
2. Открыть `tool/word_content_pipeline/database/content.sqlite`
3. Вкладка Browse Data, таблица `memberships` — все связи; `categories` — категории

Или из терминала, если нужно быстро глянуть одно слово:

```bash
cd tool/word_content_pipeline
PYTHONPATH=src .venv/bin/word-content word-info --db database/content.sqlite --word monitor
```
