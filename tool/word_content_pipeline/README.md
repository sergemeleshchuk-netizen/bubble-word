# word_content_pipeline — контентная база слов и категорий

Локальная база для игры-головоломки на словесных ассоциациях: одно английское слово
может принадлежать нескольким категориям и в разных значениях.

```
APPLE   -> FRUITS, PIE INGREDIENTS, THINGS WITH SEEDS, ___ SAUCE  (apple_fruit)
        -> TECH COMPANIES                                        (apple_company)
BANK    -> TOWN PLACES, MONEY WORDS                              (bank_finance)
        -> RIVER FEATURES                                        (bank_river)
MONITOR -> COMPUTER PARTS, SCREENS      (monitor_screen)
        -> HOSPITAL THINGS, FIRST AID   (monitor_medical)
        -> LIZARDS, REPTILES            (monitor_lizard)
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

Плюс слои, добавленные по итогам внешнего аудита базы (31.07.2026): готовность
категорий, запреты на сочетание категорий, проверенные четвёрки и solver
единственности решения.

Сюда **не входит**: генератор уровней целиком, веб-интерфейс, embeddings,
скачивание WordNet/Wikidata/ConceptNet.

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
        |    | review_status       |  candidate | approved | alternative |
        |    |                     |  hard_only | rejected
        |    | semantic_status     |  unreviewed | correct | disputed | incorrect
        |    | gameplay_difficulty |
        |    | review_comment      |
        |    | risk_flags          |
        |    +---------------------+
        |
categories                     import_runs            generation_runs
+------------------+           +----------------+     +--------------------+
| id               |           | import_type    |     | generation_type    |
| category_key UQ  |           | source_file    |     | model              |
| label            |           | records_*      |     | prompt_version     |
| rule             |           | errors_json    |     | input/raw/parsed   |
| relation_type    |           +----------------+     | status, error      |
| theme            |                                  +--------------------+
| base_difficulty  |
| status           |  active | disabled
| readiness        |  ready | constrained | curated_only | hard_only | blocked
| readiness_reason |
+------------------+
        ^
        |   category_conflicts        category_pair_groups
        |   +-------------------+     +------------------+
        +---| category_a_id     |     | category_id      |
        +---| category_b_id     |     | group_key        |
        |   | conflict_type     |     | word_id, slot    |
        |   | origin            |     +------------------+
        |   | overlap_count     |
        |   | overlap_words     |     schema_meta
        |   | severity, note    |     +------------------+
        |   +-------------------+     | key UQ           |
        |                             | value            |
        |   quartets                  +------------------+
        |   +------------------+
        +---| category_id      |      quartet_words
            | quartet_key UQ   |      +------------------+
            | tier             |<-----| quartet_id       |
            | review_state     |      | word_id          |
            | solver_state     |      | sense_id         |
            | difficulty, note |      | slot (1..4)      |
            +------------------+      +------------------+
```

`import_runs` и `generation_runs` — журнал: что, откуда, сколько записей и какие ошибки.
Нужны для воспроизводимости и разбора «откуда взялась эта связь».
`schema_meta` — версия схемы и контента, git-коммит и хеши источников: без них снимок
нельзя привязать к состоянию репозитория.

### Пять разных осей, которые нельзя путать

| ось | где живёт | что означает |
|---|---|---|
| семантическая корректность | `memberships.semantic_status` | слово удовлетворяет правилу категории |
| знакомость слова | `words.familiarity_score` | как часто слово встречается в письменном английском |
| очевидность значения | `memberships.obviousness_score` | быстро ли игрок увидит эту связь |
| игровая сложность | `memberships.gameplay_difficulty` | насколько связь усложняет уровень |
| игровая пригодность | `memberships.review_status` | куда связь можно поставить |

Раньше всё это сидело в `review_status`, поэтому `hard_only` означал одновременно
«неочевидно», «редкое слово» и «сложный уровень». Внешний аудит поймал это как
основную причину неверных статусов.

## 4. Установка

Требуется Python 3.12.

```bash
cd tool/word_content_pipeline
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"     # pydantic v2, typer, pytest, wordfreq
.venv/bin/pytest -q                   # 123 теста
```

`wordfreq` — необязательная зависимость (`pip install -e ".[freq]"`): она даёт
частотность слов. Без неё пайплайн работает, но `familiarity_score` остаётся пустым
и фильтр `--min-zipf` ничего не отсекает.

Дальше команды можно вызывать двумя способами:

```bash
.venv/bin/word-content <команда> ...                  # консольный скрипт
PYTHONPATH=src .venv/bin/python -m word_content.cli <команда> ...
```

## 5. Команды CLI

Сборка базы с нуля из seed-данных:

```bash
python scripts/build_seed.py                    # собрать JSONL из data/seed
python scripts/swow_status.py                   # проставить статусы связей

word-content init-db            --db database/content.sqlite
word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
word-content import-review      --db database/content.sqlite --input data/review_decisions.csv

word-content derive-readiness   --db database/content.sqlite
word-content derive-conflicts   --db database/content.sqlite --output data/category_conflicts.csv
word-content build-quartets     --db database/content.sqlite --output data/quartets.csv
word-content stamp-version      --db database/content.sqlite --content-version 2026.07.31
word-content check-integrity    --db database/content.sqlite   # ненулевой код = базу не отдавать
```

`import-review` применяет статусы ко всем 17 556 связям — без него база останется
в статусе `candidate` и генератор уровней не сможет отличить очевидную связь
от ловушки. Четыре команды после него достраивают слои, которых базе не хватало,
чтобы быть автономным источником уровней: готовность категорий, запреты на сочетание,
проверенные четвёрки и версию снимка.

| Команда | Что делает |
|---|---|
| `init-db` | Создаёт файл базы и таблицы. Повторный запуск безопасен, недостающие колонки добавляет. |
| `import-categories` | Upsert категорий по `category_key`, пишет `import_runs`. |
| `import-memberships` | Создаёт слова, значения и связи. Битая строка не останавливает импорт. |
| `export-review` | Выгружает связи в CSV для ручной проверки. |
| `import-review` | Возвращает решения reviewer в базу. |
| `derive-readiness` | Считает готовность категорий по пулам, отключает непригодные, пишет парные группы. |
| `derive-conflicts` | Считает пары категорий, которые нельзя ставить в один уровень. |
| `build-quartets` | Собирает четвёрки и проверяет каждую solver'ом единственности. |
| `solve-level` | Проверяет конкретный уровень: единственно ли разбиение. |
| `sense-gaps` | Очередь слов, которым нужны дополнительные значения. Базу не меняет. |
| `check-integrity` | Критерии приёмки в виде кода. Ненулевой код возврата, если база не готова. |
| `stamp-version` | Пишет версию схемы и контента, commit и хеши источников. |
| `word-info` | Все категории слова. |
| `category-info` | Все слова категории. |
| `stats` | Сводка и узкие места контента. |
| `coverage` | План работы: каким категориям сколько слов не хватает. |
| `generate-category-candidates` | AI-проход A: категория -> слова. |
| `generate-word-memberships` | AI-проход B: слово -> категории. |
| `review-membership-candidates` | AI-проход C: критик кандидатов (базу не меняет). |
| `derive-labels` | Заводит основную надпись каждому правилу группировки. |
| `plan-reference-backfill` | Считает патч: чего базе не хватает для уровней записи оригинала. |
| `import-reference-backfill` | Применяет патч из `data/reference/backfill`. |
| `import-reference-levels` | Кладёт уровни записи без потерь: группы, токены, формы, мета, провенанс. |
| `reference-coverage` | Покрытие записи по слоям; observed и inferred надписи считаются отдельно. |
| `reference-gate` | Reference Reproduction Gate. Ненулевой код = генерация нового контента запрещена. |
| `validate-meta` | Проходим ли уровень из стартового состояния: DAG, циклы, тупики. |
| `assess-levels` | Отрыв авторского разбиения от альтернатив, спроектированные и случайные ловушки. |
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

### Фильтры качества на импорте

```bash
# блок-лист включён по умолчанию (data/blocklist.txt, 131 запись)
word-content import-memberships --db database/content.sqlite \
    --input data/membership_candidates.jsonl --min-zipf 2.0

# Связи: total=1041 inserted=1039 rejected=2
#   Слово 'cufflink' слишком редкое: zipf 1.69 < 2.0
#   Слово 'pruner' слишком редкое: zipf 1.61 < 2.0
```

- `--blocklist PATH` — свой файл блок-листа, `--no-blocklist` — отключить (не рекомендуется).
  Совпадение по целому слову: `ass` блокирует `ass`, но не `grass`.
- `data/allowlist.txt` — исключения для безобидных многословных названий, внутри которых
  есть запрещённое слово (`sperm whale`, `maine coon`). Совпадение по всей фразе целиком.
- `--min-zipf N` — отклонять слова реже порога. Ориентиры: 5+ очень частое, 4 обычное,
  3 заметно реже, ниже 2.5 редкое. **По умолчанию выключено**: частотность ≠ узнаваемость
  (`jackhammer` знают все, а zipf у него 2.3). Частотность всё равно пишется
  в `words.familiarity_score`, а `stats` показывает список редких слов для глазами-проверки.

## 6. Review workflow

```
import-memberships  ->  export-review  ->  человек заполняет decision  ->  import-review  ->  stats
```

1. Кандидаты попадают в базу со статусом `candidate` (AI никогда не ставит `approved` сам).
2. `export-review` выгружает их в CSV с пустыми колонками `decision` и `review_comment`.
3. Reviewer заполняет `decision`: `approved`, `alternative`, `hard_only`, `rejected`
   или `candidate` (пустая ячейка = строка пропущена и не трогается).
   Образец заполнения — `data/review_example.csv`.
4. `import-review` возвращает решения; неизвестные связи и решения перечисляются в отчёте.
5. Повторный импорт того же AI-кандидата **не сбрасывает** ручное решение обратно в `candidate`.
   Сбросить можно только явным флагом `--overwrite-review-status`.

В CSV есть колонка `familiarity` (частотность слова, 0..1) — по ней сразу видно,
не тащит ли кандидат редкое слово.

**Решения хранятся отдельным слоем.** `data/review_decisions.csv` лежит в репозитории
и применяется после импорта связей — иначе пересборка базы из JSONL стёрла бы всю
ручную работу. Полная сборка базы это четыре шага:

```bash
word-content init-db            --db database/content.sqlite
word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
word-content import-review      --db database/content.sqlite --input data/review_decisions.csv
```

`membership_id` зависит от порядка вставки, поэтому после изменения JSONL старые id
могут указывать на другие связи. Импорт решений это учитывает: если id не сходится
со словом и категорией из той же строки, связь ищется по паре слово + категория.

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

# весь каталог за прогон, с чекпойнтом: прервали — запустили снова, пройденное пропустится
word-content generate-category-candidates --db database/content.sqlite \
    --all-categories --count 25 --checkpoint data/checkpoint.txt \
    --output data/generated_all.jsonl

# только категории, где меньше 15 слов
word-content generate-category-candidates --db database/content.sqlite \
    --only-thin 15 --count 25 --checkpoint data/checkpoint.txt \
    --output data/generated_thin.jsonl

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

## 10. Seed-контент и как его пополнять

Источник правды — каталог `data/seed/`: один текстовый файл на тему плюс несколько
служебных файлов. Python трогать не нужно.

```
data/seed/food.txt              43 категории
data/seed/language.txt          46 категорий
data/seed/animals.txt           30 категорий
...                             58 файлов тем
data/seed/_ambiguous.json       связи многозначных слов с разведёнными значениями
data/seed/_sense_map.json       какое значение у связи, пришедшей из файла темы
data/seed/_not_homonyms.txt     слова, вручную признанные однозначными
data/seed/_semantic_review.csv  семантические решения: correct / disputed / incorrect
data/seed/_risk_flags.csv       культурные, терминологические и правовые риски
data/seed/_category_meta.json   парные категории, curated_only, ручные запреты
```

### `_sense_map.json`: почему он нужен

Слово с разведёнными значениями обычно перечислено ещё и в обычном файле темы —
и такая связь оставалась без значения. База не могла ответить, в каком смысле
`ring` стоит в BOXING WORDS, а генератор собирал четвёрку из разных смыслов
одного слова. Аудит нашёл 96 таких связей у 18 слов.

```json
{
  "senses":      { "ring": { "ring_arena": {"definition": "The roped area used for boxing", "part_of_speech": "noun"} } },
  "assignments": { "ring": { "boxing_words": { "sense": "ring_arena", "review_status": "approved" } } }
}
```

Инвариант проверяется при сборке: у слова с двумя и более значениями каждая связь
обязана указывать значение, иначе `build_seed.py` падает со списком незакрытых связей.

Единственное исключение — категории игры слов (`phrase_before`, `phrase_after`):
там слово участвует **написанием**, а не смыслом. `starboard` не происходит от звезды,
`keystone` — не от ключа от замка. Приписать таким связям значение значило бы внести
в базу ложь, поэтому у них `sense_id` пустой осознанно, и `check-integrity`
показывает их отдельным информационным пунктом.

Формат: две строки на категорию — заголовок через `|` и список слов через запятую.

```
fruits | FRUITS | is_a | 0.1 | 0.95 | A | Common edible fruits familiar to an average American adult | $W is a common edible fruit
apple, banana, orange, grape, peach, cherry, lemon, strawberry, pear, watermelon
```

Поля заголовка: `key | LABEL | relation_type | difficulty | obviousness | flags | rule | reason_template`.
Флаги: `A` — связи можно ставить `approved`, `C` — только `candidate`, `P` — категория
из имён собственных. В шаблоне `$W` — слово с заглавной буквы, `$w` — как есть;
это избавляет от написания объяснения к каждому слову вручную. Для многозначных слов
объяснение пишется в `_ambiguous.json` вместе со значением.

Добавить контент = отредактировать файл темы (или создать новый) и пересобрать:

```bash
.venv/bin/python scripts/build_seed.py
# категорий: 1092 в 58 темах
# связей:    17550
# слов:      10005 (в двух и более категориях: 3456)
# approved:  12621
# редких слов (zipf < 2.5): 1232 -> mukluk, chiffonade, marionberry, ...
```

Сборка сама проверяет: дубли `category_key` между файлами, дубли связей,
ссылки на несуществующие категории и попадание слов в блок-лист. Нашла проблему —
не пишет файлы и возвращает ненулевой код. Редкое слово автоматически уходит
в `candidate`, даже если категория помечена флагом `A`.

### Что генерировать дальше

```bash
word-content coverage --db database/content.sqlite --target 25
# Категорий: 1092 | слов: 10005 | в 2+ категориях: 3455 (34%)
# До глубины 25 слов на категорию не хватает 9761 связей
# ... таблица по темам и список самых тонких категорий
```

Это и есть план работы: команда показывает, какие темы просели и каким категориям
сколько слов добрать.

58 тем: food, animals, home, nature, transport, sports, jobs, body, clothing, tools,
geography, science, language, entertainment, actions, properties, business, time,
education, people, technology, history, mythology, art, plants, ocean, places, media,
medicine, law, world_food, species, hobbies, farming, religion, sounds, brands, space,
materials, fashion, names, varieties, cities, culture, sports_world, nature_more,
trades, descriptive, landmarks, jargon, names_world, animals_more, food_more, skills,
world_more, lists, nature_species, misc.

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

## 11. Масштабирование до 10 000 слов

Ориентир: **~600 категорий × 25 слов ≈ 15 000 связей ≈ 10 000 уникальных слов** — цель достигнута.
Узкое место — не слова, а категории с точным правилом и плотность пересечений.

| | было | стало | цель |
|---|---|---|---|
| категорий | 92 | **1092** | ~600 |
| слов | 902 | **10 005** | ~10 000 |
| связей | 1039 | **17 550** | ~15 000 |
| слов в 2+ категориях | 12% | **34%** | 30–40% |

Порядок работы:

1. **Вширь** — новые файлы тем в `data/seed/`. Больше категорий важнее, чем более
   глубокие пулы: на 4 слова в уровне глубина 25 уже избыточна, а разнообразие категорий
   определяет, сколько уровней можно собрать без повторов.
2. **Вглубь** — добить тонкие категории по списку из `coverage`.
3. **Обратный проход** — прогнать слова по всему каталогу. Новых слов не даёт,
   зато поднимает долю пересечений, а это ловушки для сложных уровней.
4. **Чистка** — `stats` показывает редкие слова, `review-membership-candidates`
   даёт AI-критику, `export-review` выгружает спорное человеку.

## 12. Четыре статуса связи и откуда они взялись

Статус отвечает на вопрос «как игрок встретит эту связь в уровне». Между
«очевидно» и «никто не догадается» есть промежуток — именно он даёт ловушки.

| статус | связей | что значит | пример |
|---|---|---|---|
| `approved` | 12 598 | значение, которое игрок вспоминает первым; годится куда угодно | `monitor` -> COMPUTER PARTS |
| `alternative` | 3 955 | верное и узнаваемое, но не первое значение: **материал для ловушек** в обычном уровне | `monitor` -> HOSPITAL THINGS |
| `hard_only` | 917 | верно, но игрок сам не догадается: только сложные уровни | `monitor` -> LIZARDS (варан) |
| `rejected` | 60 | в игру не идёт: слово практически не встречается в английском | `caecilian`, `mudpuppy` |
| `candidate` | 26 | частотность посчитать не удалось: связь закрыта до ручной проверки | `calfling`, `WD40` |

### Статус считается в два шага: сначала абсолютно, потом относительно

**Шаг 1 — абсолютная заметность связи.** Считается независимо от других категорий слова:

```
заметность = 0.6 × очевидность правила категории + 0.4 × знакомость слова
заметность >= 0.80                          -> пол approved
очевидность >= 0.90 и знакомость >= 0.28    -> пол approved
заметность >= 0.60                          -> пол alternative
```

Очевидность отвечает за «понятно ли правило категории», знакомость — за «знает ли игрок
слово», и одно компенсирует другое. Категория, чьё правило само себя объясняет
(MUSICAL INSTRUMENTS, DESSERTS), даёт `approved` даже редкому слову: `xylophone`
редок в текстах (частотность 0.34), но игрок соберёт его с барабаном и пианино сразу.
Пул, выверенный вручную (флаг `A` в файле темы), тоже работает абсолютным полом.

**Шаг 2 — SWOW-EN** (Small World of Words): 12 282 стимула, свободные ассоциации живых
людей. Датасет лежит локально (`reference/swow/`, research/personal use), в репозиторий
идут только производные решения.

```bash
python scripts/swow_status.py          # весь слой решений одной командой
python scripts/swow_senses.py          # где стоит развести значения
```

Профиль слова — то, что люди отвечают на него и на что отвечают им. Слова одной
категории похожи профилями, даже если напрямую друг с другом не ассоциируются,
поэтому профиль слова сравнивается с профилем категории без этого слова.
SWOW может поднять связь выше абсолютного пола, но **не опустить ниже**.

Порядок именно такой по итогам внешнего аудита. Раньше SWOW сравнивал категории слова
только между собой, и объективно очевидная связь редкого слова уезжала в `hard_only`:
`xylophone` -> MUSICAL INSTRUMENTS, `key` -> KEYCHAIN THINGS, все пустыни, все латинские
выражения. 355 таких связей имели очевидность 0.80 и выше.

Из 17 556 связей 11 860 решены с участием SWOW, остальные — по абсолютной оценке
(слова вне датасета: многословные, имена собственные, редкие).

Два ограничения метода, которые пришлось обойти:

- **SWOW занижает вторичные значения известных слов.** На «apple» почти никто
  не отвечает «Microsoft», хотя компанию знают все.
- **SWOW не видит рассудочные связи.** Банк ассоциируется с деньгами, а не со
  школой и библиотекой, но что это здание в городе — сообразит любой.

Поэтому у многозначных слов абсолютный пол **не применяется вообще**: там судит ручная
разметка значений (`_ambiguous.json`, `_sense_map.json`). Частотность считается
по написанию слова, а `monitor` в значении «варан» частотным не является.
У категорий игры слов пол тоже не применяется: `___ BOARD` — это загадка,
а не очевидность.

**Нет частотности — нет игры.** Если `wordfreq` слова не знает, утверждать, что средний
игрок его узнает, нельзя: связь закрывается в `candidate`. Раньше 20 таких связей
проходили как `approved` (`calfling`, `WD40`, `Barqs`) — это было главное P0-замечание
аудита. Гейт стоит в трёх местах: сборка seed, слой решений, импорт в базу.

### Разведённые значения

Значения разведены у **223 слов** (549 значений). Кандидатов ищет
`scripts/swow_senses.py`: если категории слова живут в разных ассоциативных
областях, а слово уверенно подходит обеим — значений скорее всего два.

```
crown    -> ROYALTY (корона) / DENTAL WORDS (коронка) / TREE PARTS (крона)
delta    -> BODIES OF WATER (дельта) / GREEK LETTERS (буква) / AIRLINES (компания)
sentence -> WRITING WORDS (предложение) / PRISON WORDS (приговор)
mercury  -> METALS (ртуть) / PLANETS (планета) / ROMAN GODS (бог)
ball     -> TOYS (мяч) / ___ ROOM (бал)
cook     -> KITCHEN JOBS (повар) / EXPLORERS (капитан Кук)
```

**Очередь детектора пуста.** Каждый кандидат либо разведён, либо занесён
в `data/seed/_not_homonyms.txt` — это 140 слов, проверенных вручную и признанных
однозначными: `turtle` в OCEAN ANIMALS и GREEN THINGS — одна и та же черепаха,
`sun` в SPACE OBJECTS и YELLOW THINGS — одно и то же солнце. Детектор их
пропускает, поэтому его вывод — очередь работы, а не список для повторного разбора.

## 13. Готовность категорий, конфликты, четвёрки и solver

Три слоя, без которых база остаётся набором пулов, а не источником уровней.

### Готовность категории (`readiness`)

Категория в уровне — ровно четыре слова. Пул из двадцати связей ещё не значит, что
четвёрку можно собрать: пул может быть целиком `hard_only`, а правило — парным
или субъективным. Готовность выводится из данных, руками не пишется:

| readiness | что значит | категорий |
|---|---|---|
| `ready` | 4+ слов уровня, пул не перекошен | 816 |
| `constrained` | годится, но пул тонкий, перекошен в `hard_only` или мало `approved` | 268 |
| `curated_only` | правило парное или субъективное: только ручные четвёрки | 4 |
| `hard_only` | нормальных слов меньше четырёх: только сложные уровни | 5 |
| `blocked` | четвёрку не собрать даже с `hard_only`: `status = disabled` | 0 |

Аудит нашёл 34 категории, которые не собирали нормальную четвёрку. После пересчёта
статусов по абсолютным порогам осталось 5 — остальные оказались жертвами
переусердствовавшего `hard_only`.

Единственный ручной вход — `curated_only` в `_category_meta.json`. Туда попали
OPPOSITES (правило парное), NATIONAL SYMBOLS (страна в данных не хранится),
SOFT CREATURES и CLASSIC GAMES (субъективные правила).

### Конфликты категорий (`category_conflicts`)

**516 пар** категорий делят четыре и больше играбельных слов — `JEWELRY STONES`
и `GEMSTONES` делят пятнадцать. Значит четвёрка из одной целиком лежит в другой,
и у уровня появляется второй корректный ответ. Такие пары нельзя ставить в один уровень.

```bash
word-content derive-conflicts --db database/content.sqlite --output data/category_conflicts.csv
# Конфликтов: derived=514 manual=3 | По серьёзности: P0=86, P1=428
```

`derived` считается по пересечению пулов, `manual` — ручные запреты из
`_category_meta.json` для пар, где пересечение меньше порога, но категории
всё равно неотличимы для игрока.

### Парные категории (`category_pair_groups`)

`OPPOSITES` — это не пул из 26 слов, а 13 пар. Четвёрка для такой категории собирается
только как две полные пары: `hot / cold / big / small`, а не четыре случайных слова.

### Проверенные четвёрки (`quartets`) и solver

```bash
word-content build-quartets --db database/content.sqlite --output data/quartets.csv
# категорий рассмотрено: 1084 | категорий без четвёрок: 3 | четвёрок: 3005
```

Четвёрка попадает в базу, только если solver подтвердил: этих четырёх слов нет целиком
ни в одной другой категории. Статус `auto_validated` значит «solver прошёл, человек
не смотрел»; `human_approved` ставится только вручную.

Solver уровня перечисляет **все** разбиения слов на четвёрки-категории и принимает
уровень, только если разбиение одно. Категория в разбиении используется один раз.

```bash
# 8 камней из двух пересекающихся категорий: два ответа, уровень отклонён
word-content solve-level --db database/content.sqlite \
    --words "diamond,emerald,ruby,sapphire,amethyst,opal,topaz,garnet"
# Отклонён: найдено разбиений: 2 и более — у уровня несколько ответов

# инструменты плюс сезоны: ответ один
word-content solve-level --db database/content.sqlite \
    --words "guitar,piano,organ,drum,fall,spring,summer,winter"
# ОК: разбиение единственное
```

### Проверки готовности (`check-integrity`)

Критерии приёмки из внешнего аудита в виде кода. Ненулевой код возврата означает
«снимок отдавать нельзя»:

```bash
word-content check-integrity --db database/content.sqlite
```

| проверка | severity |
|---|---|
| файл базы цел, внешние ключи не нарушены | blocker |
| нет играбельных связей со словом без частотности | blocker |
| нет связей многозначных слов без указанного значения | blocker |
| у всех категорий посчитан `readiness` | blocker |
| нет включённых normal-категорий с пулом меньше четырёх слов уровня | blocker |
| семантически неверные связи не идут в игру | blocker |
| слой конфликтов заполнен | blocker |
| в каждой четвёрке ровно четыре слова | blocker |
| все действующие четвёрки прошли solver | blocker |
| нет играбельных связей с устаревшей терминологией | blocker |
| у снимка есть версия схемы и контента | warning |
| связи игры слов без значения (осознанное исключение) | info |
| очередь на ручную проверку (`candidate`) | warning |

### Очередь на разведение значений (`sense-gaps`)

```bash
word-content sense-gaps --db database/content.sqlite --output data/sense_review_queue.csv
# Слов, которым нужны значения: 556 | P0=65, P1=291, P2=200
```

Слово попадает в очередь, если живёт минимум в четырёх играбельных категориях
из трёх и более тем, значений у него нет, и вручную однозначным его не признали
(`_not_homonyms.txt`). Механизм не принимает решений — он выдаёт работу.

## 14. Ограничения текущей версии

- Дедупликация значений — только по точному совпадению определения, без семантики.
- Значения разведены у 222 слов-омонимов (564 значения). Ещё **556 слов** живут
  в четырёх и более категориях без значений — они в очереди `sense-gaps`.
- `fit_score` **не является измерением**: у 17 489 связей он равен 0.97, потому что это
  константа из seed. Реальная семантическая ось — `semantic_status`, и она пока
  `unreviewed` у 17 479 связей: ручное ревью носителем языка не проводилось.
- Частотность считается только при установленном `wordfreq`; она измеряет
  употребимость, а не узнаваемость, поэтому сама по себе не отсекает слова.
- Нет проверки, что слово реально существует в английском языке (нет словаря-оракула).
- `words.is_proper_noun` и регистр живут на уровне слова, хотя зависят от значения
  (`apple`/`Apple`, `turkey`/`Turkey`). Sense-level `display_text` не сделан — это P2.
- Четвёрки имеют статус `auto_validated`: solver прошёл, человек не смотрел.
- Миграции схемы минимальные: `init-db` добавляет недостающие колонки, но при
  серьёзном изменении `schema.sql` базу всё равно пересобирают из текстовых источников.
- Реальный LLM-провайдер не покрыт сетевыми тестами (только mock).
- Нет связи с игровой базой `tool/data/categories.json` — по договорённости
  этот пайплайн пока живёт отдельно.

## 15. Папка-выдача и пакет для ревью

```bash
python scripts/export_review_pack.py --db database/content.sqlite
```

Собирает `БАЗА-СЛОВ/` в корне проекта — это то, что отдают наружу:

```
БАЗА-СЛОВ/
├── README.md               что здесь лежит и как обновить (по-русски)
└── ревью/                   материалы для проверки человеком или внешней моделью
```

База в этой папке НЕ дублируется. Она одна: `database/content.sqlite`, лежит в
git и развивается по шагам как авторский набор. Раньше скрипт клал сюда её копию,
и в репозитории жили два файла с одинаковым содержимым — причём настоящая база
была в `.gitignore`, а история велась у копии. Экспорт делает `VACUUM` самой базы
(убирает мусор от импортов) и пишет только текстовые материалы.

Внутри `ревью/`:

| файл | что внутри |
|---|---|
| `00_INSTRUCTIONS.md` | что за игра, что значат статусы, о чём хочется услышать |
| `01_summary.md` | цифры и метод разметки |
| `02_categories.md` | все категории: правило и слова со статусами (375 КБ) |
| `02_categories_part1..4.md` | то же, разбито на 4 части по ~93 КБ для ревью в несколько проходов |
| `03_homonyms.md` | разведённые значения многозначных слов |
| `04_flags.md` | редкие слова, слова без частотности, отклонённые, тонкие категории, перевес hard_only, риски. **Все разделы полные**: где показана часть, под таблицей сказано сколько всего |
| `05_memberships.csv` | все связи в машинном виде (2.2 МБ), включая `semantic_status`, `gameplay_difficulty` и `risk_flags` |
| `06_manual_decisions.md` | **что осталось решить человеку** плюс решения, принятые по ходу |
| `07_readiness_and_conflicts.md` | готовность категорий, конфликты, парные категории, сводка по четвёркам |
| `08_quartets.csv` | 3005 проверенных четвёрок с правилом категории |

Слова помечены знаками статуса, чтобы ревью читалось без переключения между файлами:
`+` approved, `~` alternative, `!` hard_only, `x` rejected.

## 16. Воспроизведение референса: правило, надпись и авторский дом

Слой, добавленный после того, как выяснилось, что база не воспроизводит ни
одного уровня оригинала. Подробный разбор — `../docs/reference_reproduction/`.

Три сущности, которые до этого были одной:

```text
categories + rule_type      внутреннее правило: music_genres, musical_instruments
category_labels             надпись для игрока: MUSIC
group_rule_labels           какие надписи допустимы для правила
quartets + quartet_words    конкретная авторская четвёрка
```

Одна надпись обслуживает разные правила: MUSIC на уровне 3 референса — это
жанры, на уровне 6 — инструменты. Пока надпись была идентификатором принципа,
одно исключало другое, и генератор не мог собрать ни тот, ни другой уровень.

`rule_type` различает девять принципов группировки, в том числе те, которые не
сводятся к таксономии: `association_hub` (CAT -> meow, purr, whiskers),
`context_hub` (SLEEP -> bed, blanket, pillow, dream), `meta_collector`
(четвёрка целиком из результатов других категорий).

Уровень как сущность:

```text
level_tokens.token_kind     lexical_word | picture_token | chunked_word | category_output
level_tokens.observability  observed | unseen | generated
level_dependencies          какая собранная группа выпускает токен для другой
level_assignments           авторский дом токена в ЭТОМ уровне
level_decoys                правдоподобные чужие дома; planned = спроектированная ловушка
reference_sources           провенанс: файл записи, номер уровня, наблюдалось ли
```

Барьер: `generate-level-candidates` вызывает `reference-gate` и падает, если
уровни 1-10 не воспроизводятся без потерь. Снимается только явным
`--skip-reference-gate` — это флаг отладки, его результат контентом не является.

Правила и четвёрки, выведенные из записи, помечены `origin = reference_backfill`
и в генерацию нового контента не идут: они здесь как измерительный эталон, а не
как материал.

## 17. Следующие шаги

1. **Ручное ревью носителем языка.** `semantic_status` пока `unreviewed` у 17 479 связей.
   Начинать с `06_manual_decisions.md` и `04_flags.md`.
2. **Разведение значений по очереди `sense-gaps`** — 556 слов, 65 из них с приоритетом P0.
3. **Подтверждение четвёрок человеком**: 3005 штук в статусе `auto_validated`.
4. **Sense-level `display_text`** и слой canonical concept/alias: `Kitkat`, `Reeses`,
   `McDonalds`, `OHare` теряют апострофы и правильное написание (P2 аудита).
5. AI candidate generator в боевом режиме (реальная модель вместо mock, батчи по каталогу).
6. Мост к игровой базе: экспорт SQLite -> `tool/data/categories.json`.
7. Логирование каждого запуска генератора уровней в `generation_runs`: сейчас таблица пуста,
   поэтому происхождение сгенерированного уровня по снимку не восстановить.
