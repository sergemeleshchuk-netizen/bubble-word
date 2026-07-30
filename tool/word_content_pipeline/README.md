# word_content_pipeline — контентная база слов и категорий

Локальная база для игры-головоломки на словесных ассоциациях: одно английское слово
может принадлежать нескольким категориям и в разных значениях.

```
APPLE -> FRUITS, PIE INGREDIENTS, THINGS WITH SEEDS, RED THINGS,
         WORDS BEFORE "SAUCE"   (значение apple_fruit)
      -> TECH COMPANIES         (значение apple_company)
BANK  -> PLACES IN A TOWN, MONEY WORDS (bank_finance)
      -> RIVER FEATURES                (bank_river)
BAT   -> FLYING ANIMALS, NOCTURNAL ANIMALS (bat_animal)
      -> BASEBALL EQUIPMENT, BASEBALL WORDS (bat_equipment)
```

Хранится не только пара «слово — категория», но и **значение** слова, **тип связи**,
**объяснение**, **сила связи** (fit), **очевидность** (obviousness), **статус ручной
проверки** и **источник** записи.

## 1. Задача этого этапа

Воспроизводимый пайплайн наполнения и проверки контента:

1. создать SQLite-базу;
2. импортировать каталог категорий из JSONL;
3. добавлять слова и связи слово-категория;
4. импортировать AI-кандидатов из JSONL;
5. нормализовать и валидировать данные;
6. выгружать кандидатов в CSV для ручной проверки;
7. импортировать решения reviewer обратно;
8. получать все одобренные категории слова;
9. получать все одобренные слова категории;
10. плюс два AI-прохода (категория -> слова, слово -> категории) и AI-критик.

Сюда **не входит**: генерация игровых уровней, Exact Cover, solver, веб-интерфейс,
embeddings, скачивание WordNet/Wikidata/ConceptNet.

## 2. Почему SQLite + JSONL

- **SQLite** — рабочая база: связи, уникальные индексы, транзакции, запросы за миллисекунды,
  один файл без сервера. Именно по ней будет работать будущий генератор уровней.
- **JSONL** — человекочитаемый обменный формат: одна связь = одна строка, удобно смотреть
  глазами, диффать в git и получать от LLM порциями. Файлы в `data/` — источник правды
  для seed-контента, база всегда пересобирается из них.
- **CSV** — формат ручного review: reviewer открывает файл в таблице, ставит decision, отдаёт обратно.

## 3. Схема данных

```
words                          word_senses
+----------------+             +-------------------+
| id             |<-----+      | id                |
| text           |      +------| word_id           |
| normalized     |             | sense_key         |
| language       |             | definition        |
| part_of_speech |             | part_of_speech    |
| familiarity    |             +-------------------+
| is_proper_noun |                      ^
| status         |                      |
+----------------+                      |
  UNIQUE(normalized, language)          |  UNIQUE(word_id, sense_key)
        ^                               |
        |          memberships          |
        |    +---------------------+    |
        +----| word_id             |----+
             | sense_id (NULL ok)  |
        +----| category_id         |
        |    | relation_type       |
        |    | reason              |
        |    | fit_score           |     UNIQUE(word_id, category_id,
        |    | obviousness_score   |            relation_type, COALESCE(sense_id,0))
        |    | source              |
        |    | review_status       |  candidate | approved | hard_only | rejected
        |    | review_comment      |
        |    | risk_flags          |
        |    +---------------------+
        |
categories                     import_runs            generation_runs
+-----------------+            +----------------+     +--------------------+
| id              |            | import_type    |     | generation_type    |
| category_key UQ |            | source_file    |     | model              |
| label           |            | records_*      |     | prompt_version     |
| rule            |            | errors_json    |     | input/raw/parsed   |
| relation_type   |            +----------------+     | status, error      |
| theme           |                                   +--------------------+
| base_difficulty |
| status          |
+-----------------+
```

`import_runs` и `generation_runs` — журнал: что, откуда, сколько записей и какие ошибки.
Нужны для воспроизводимости и разбора «откуда взялась эта связь».

## 4. Установка

Требуется Python 3.12.

```bash
cd tool/word_content_pipeline
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"     # pydantic v2, typer, pytest
.venv/bin/pytest -q                   # 66 тестов
```

Дальше команды можно вызывать двумя способами:

```bash
.venv/bin/word-content <команда> ...                  # консольный скрипт
PYTHONPATH=src .venv/bin/python -m word_content.cli <команда> ...
```

## 5. Команды CLI

Сборка базы с нуля из seed-данных:

```bash
word-content init-db --db database/content.sqlite
word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
```

| Команда | Что делает |
|---|---|
| `init-db` | Создаёт файл базы и таблицы. Повторный запуск безопасен. |
| `import-categories` | Upsert категорий по `category_key`, пишет `import_runs`. |
| `import-memberships` | Создаёт слова, значения и связи. Битая строка не останавливает импорт. |
| `export-review` | Выгружает связи в CSV для ручной проверки. |
| `import-review` | Возвращает решения reviewer в базу. |
| `word-info` | Все категории слова. |
| `category-info` | Все слова категории. |
| `stats` | Сводка и узкие места контента. |
| `generate-category-candidates` | AI-проход A: категория -> слова. |
| `generate-word-memberships` | AI-проход B: слово -> категории. |
| `review-membership-candidates` | AI-проход C: критик кандидатов (базу не меняет). |
| `show-runs` | Журнал импортов и генераций. |

Примеры:

```bash
# ручная проверка
word-content export-review --db database/content.sqlite \
    --output data/review_candidates.csv --status candidate
word-content import-review --db database/content.sqlite \
    --input data/review_candidates.csv

# запросы
word-content word-info     --db database/content.sqlite --word apple --statuses approved,hard_only
word-content category-info --db database/content.sqlite --category fruits --statuses approved
word-content stats         --db database/content.sqlite

# принудительно перезаписать статусы из файла (по умолчанию ручные решения защищены)
word-content import-memberships --db database/content.sqlite \
    --input data/membership_candidates.jsonl --overwrite-review-status
```

Важное поведение импорта: несколько невалидных строк — это **не** ошибка запуска.
Exit code 1 бывает только при системной ошибке (нет файла, нет базы).

## 6. Review workflow

```
import-memberships  ->  export-review  ->  человек заполняет decision  ->  import-review  ->  stats
```

1. Кандидаты попадают в базу со статусом `candidate` (AI никогда не ставит `approved` сам).
2. `export-review` выгружает их в CSV с пустыми колонками `decision` и `review_comment`.
3. Reviewer заполняет `decision`: `approved`, `hard_only`, `rejected` или `candidate`
   (пустая ячейка = строка пропущена и не трогается). Образец заполнения — `data/review_example.csv`.
4. `import-review` возвращает решения; неизвестные `membership_id` и решения перечисляются в отчёте.
5. Повторный импорт того же AI-кандидата **не сбрасывает** ручное решение обратно в `candidate`.
   Сбросить можно только явным флагом `--overwrite-review-status`.

## 7. fit_score и obviousness_score

Это **разные** вещи, и путать их нельзя.

- `fit_score` — насколько связь **корректна** по формальному правилу категории.
- `obviousness_score` — насколько быстро её **заметит средний игрок**.

```
APPLE -> FRUITS               fit 1.00   obv 1.00   очевидно и верно
APPLE -> WORDS BEFORE SAUCE   fit 0.98   obv 0.90   верно, чуть менее очевидно
BANK  -> RIVER FEATURES       fit 0.99   obv 0.70   абсолютно верно, но игрок думает о деньгах
PITCH -> STICKY THINGS        fit 0.90   obv 0.30   верно (смола), почти никто не вспомнит
```

Низкая очевидность — не ошибка, а материал для сложных уровней: такие связи получают
статус `hard_only`.

## 8. Примеры запросов для APPLE

```bash
$ word-content word-info --db database/content.sqlite --word Apple
word   sense          category            relation       fit   obv   status     reason
apple  apple_fruit    fruits              is_a           1.00  1.00  approved   An apple is a common edible fruit
apple  apple_fruit    pie_ingredients     used_in        0.99  0.95  approved   Apples are the classic pie filling
apple  apple_fruit    red_things          has_property   0.90  0.80  candidate  Apples are typically red
apple  apple_fruit    round_things        has_property   0.92  0.75  candidate  An apple is round in shape
apple  apple_company  tech_companies      is_a           1.00  0.99  approved   Apple is a well-known technology company
apple  apple_fruit    things_with_seeds   has_property   0.99  0.85  approved   An apple has a core full of seeds
apple  apple_fruit    words_before_sauce  phrase_before  0.98  0.90  approved   Apple forms the familiar expression apple sauce
```

`Apple` и `apple` — одна запись в `words`; компания и фрукт разведены через `word_senses`.

```bash
$ word-content word-info --db database/content.sqlite --word bat --statuses approved
bat  bat_equipment  baseball_equipment  used_in       1.00  0.95  approved
bat  bat_animal     flying_animals      has_property  1.00  0.90  approved
```

## 9. AI-assisted population workflow

Модель только **предлагает**. Всё, что она вернула, ложится в базу со статусом `candidate`.

```
1. import-categories                 каталог категорий с правилами
2. generate-category-candidates      проход A: категория -> слова
3. --import (или import-memberships) кандидаты в базу, статус candidate
4. generate-word-memberships         проход B: слово -> ещё категории из каталога
5. export-review                     CSV для человека
6. ручной review                     decision по каждой строке
7. import-review                     решения обратно в базу
8. stats                             покрытие: где меньше 8 approved-связей
```

Провайдер выбирается флагом `--provider`:

- `mock` — без сети. Без `--mock-file` отдаёт валидные пустые ответы (echo-режим),
  с `--mock-file` — заранее подготовленный JSON (см. `data/mock/`).
- `openai` — любой OpenAI-compatible endpoint. Настройки только через окружение:

```bash
export LLM_API_KEY=...        # ключ не пишется ни в файлы, ни в логи, ни в SQLite
export LLM_BASE_URL=https://api.openai.com/v1
export LLM_MODEL=gpt-4o-mini
```

Примеры:

```bash
word-content generate-category-candidates --db database/content.sqlite \
    --category things_with_seeds --count 30 --batch-size 15 \
    --provider mock --mock-file data/mock/expand_things_with_seeds.json \
    --output data/generated_things_with_seeds.jsonl --import

word-content generate-word-memberships --db database/content.sqlite \
    --words apple,bank,bat --provider mock \
    --mock-file data/mock/expand_words_apple_bank_bat.json \
    --output data/generated_reverse.jsonl --import

word-content generate-word-memberships --db database/content.sqlite \
    --all-approved-words --limit 100 --batch-size 8 --output data/generated_reverse.jsonl

word-content review-membership-candidates --db database/content.sqlite \
    --status candidate --limit 100 --output data/ai_review.jsonl
```

Что пайплайн делает с ответом модели:

- проверяет схему через Pydantic (score вне 0..1 — брак);
- нормализует слово, схлопывает одинаковые значения (`sense_key` с тем же определением);
- выбрасывает выдуманные `category_key` (их нет в каталоге — связи не будет);
- выбрасывает дубли по (нормализованное слово + категория + значение);
- при ошибке разбора сохраняет **сырой** ответ в `generation_runs` и продолжает со следующего batch;
- повторные попытки с экспоненциальной задержкой (`--max-retries`).

`review-membership-candidates` — модель в роли критика, а не адвоката. Она **не меняет**
`review_status`, результат — материал для человека (`recommended_decision`, исправленные
оценки, список претензий).

Промпты лежат в `prompts/` (`expand_category.txt`, `expand_words.txt`,
`adversarial_review.txt`), версия промпта пишется в `generation_runs.prompt_version`.

## 10. Seed-контент

`scripts/build_seed.py` собирает оба JSONL из компактного описания:

```bash
.venv/bin/python scripts/build_seed.py
# категорий: 92 в 19 темах
# связей:    1041
# слов:      904 (в двух и более категориях: 111)
```

Темы: food, animals, home, nature, transport, sports, jobs, body, clothing, tools,
geography, science, language, entertainment, actions, properties, business, time, education.

Категории описаны **правилом**, а не только ярлыком: `THINGS WITH SEEDS` — это
«Common objects or foods that naturally contain seeds», и слово проверяется по правилу.
Субъективных категорий (`NICE THINGS`) и категорий с меняющимися фактами
(`CURRENT POPULAR SINGERS`) в базе нет.

Многозначные слова с разведёнными значениями: apple, bank, bat, date, orange, spring,
pitch, bark, crane, capital, diamond, heart, spade, club, key, scale, mouth, palm, plate,
temple, star, moon, ring.

`approved` в seed стоит только у очевидных вручную выверенных пулов. Неочевидные
категории (`WORDS BEFORE BALL`, `ROUND THINGS`, `RIVER FEATURES`, `STICKY THINGS`…)
намеренно оставлены в `candidate` — это и есть очередь на ручной review.

## 11. Ограничения первой версии

- Дедупликация значений — только по точному совпадению определения, без семантики.
- Нет частотности слов: поле `familiarity_score` есть в схеме, но seed его не заполняет.
- Нет проверки, что слово реально существует в английском языке (нет словаря-оракула).
- `words.is_proper_noun` = «встречается как имя собственное»; настоящее разделение —
  через `word_senses`.
- Нет миграций схемы: при изменении `schema.sql` базу пересобирают из JSONL.
- Реальный LLM-провайдер не покрыт сетевыми тестами (только mock).
- Нет связи с игровой базой `tool/data/categories.json` — по договорённости
  этот пайплайн пока живёт отдельно.

## 12. Следующие шаги

1. AI candidate generator в боевом режиме (реальная модель вместо mock, батчи по каталогу).
2. Reverse expansion по всем approved-словам — набрать пересечения для «ловушек».
3. Генератор уровней поверх базы (выбор категорий, слов-ловушек, целевой сложности).
4. Валидатор Exact Cover: проверка, что уровень раскладывается однозначно.
5. Мост к игровой базе: экспорт SQLite -> `tool/data/categories.json`.
