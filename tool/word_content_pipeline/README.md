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
        |    | review_status       |  candidate | approved | alternative |
        |    |                     |  hard_only | rejected
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
.venv/bin/pip install -e ".[dev]"     # pydantic v2, typer, pytest, wordfreq
.venv/bin/pytest -q                   # 93 теста
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
word-content init-db            --db database/content.sqlite
word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
word-content import-review      --db database/content.sqlite --input data/review_decisions.csv
```

Последний шаг применяет статусы ко всем 17 550 связям — без него база останется
в статусе `candidate` и генератор уровней не сможет отличить очевидную связь
от ловушки. Слой решений порождается командой `python scripts/swow_status.py`.

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
| `coverage` | План работы: каким категориям сколько слов не хватает. |
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

Источник правды — каталог `data/seed/`: один текстовый файл на тему плюс
`_ambiguous.json` для многозначных слов. Python трогать не нужно.

```
data/seed/food.txt           43 категории
data/seed/language.txt       46 категорий
data/seed/animals.txt        30 категорий
...                          58 файлов тем
data/seed/_ambiguous.json    62 связи с разведёнными значениями
```

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
| `approved` | 8 954 | значение, которое игрок вспоминает первым; годится куда угодно | `monitor` -> COMPUTER PARTS |
| `alternative` | 6 032 | верное и узнаваемое, но не первое значение: **материал для ловушек** в обычном уровне | `monitor` -> HOSPITAL THINGS |
| `hard_only` | 2 503 | верно, но игрок сам не догадается: только сложные уровни | `monitor` -> LIZARDS (варан) |
| `rejected` | 61 | в игру не идёт: слово практически не встречается в английском | `caecilian`, `mudpuppy` |

### Статусы проставлены по человеческим ассоциациям, а не «на глаз»

Источник — **SWOW-EN** (Small World of Words): 12 282 стимула, свободные ассоциации
живых людей. Датасет лежит локально (`reference/swow/`, research/personal use),
в репозиторий идут только производные решения.

```bash
python scripts/swow_status.py          # весь слой решений одной командой
python scripts/swow_senses.py          # где стоит развести значения
```

Профиль слова — то, что люди отвечают на него и на что отвечают им. Слова одной
категории похожи профилями, даже если напрямую друг с другом не ассоциируются,
поэтому профиль слова сравнивается с профилем категории без этого слова.
У слова сравниваются его же категории между собой: лучшая идёт в `approved`,
заметно слабее — в `alternative`, почти без связи — в `hard_only`.

Из 17 550 связей 11 864 решены по SWOW, остальные — по правилам категории
и частотности (слова вне датасета: многословные, имена собственные, редкие).

Два ограничения метода, которые пришлось обойти:

- **SWOW занижает вторичные значения известных слов.** На «apple» почти никто
  не отвечает «Microsoft», хотя компанию знают все. Поэтому порог `alternative`
  низкий, а ручная разметка значений омонимов сильнее данных.
- **SWOW не видит рассудочные связи.** Банк ассоциируется с деньгами, а не со
  школой и библиотекой, но что это здание в городе — сообразит любой. Поэтому
  в прозрачных категориях действует пол: ниже `alternative` связь не опускается.

Разница между `alternative` и `hard_only` — не в правильности, а в узнаваемости.
Монитор в больнице американец опознает сразу, как только увидит категорию;
монитор-варан — нет. Первое работает ловушкой на обычном уровне, второе годится
только там, где игрок готов к подвоху.

Очередь ручной проверки разобрана полностью: `candidate` в базе не осталось.

Как принимались решения (правило проверяемое, а не «на глаз»):

1. Слова из курируемого списка «редкое в текстах, но знает каждый» (colander,
   jackhammer, unicycle) — `approved`, если сама категория очевидная.
2. Частотность ниже 0.20 и не в списке — `rejected`: слова вроде `caecilian`,
   `mudpuppy`, `taramasalata` средний игрок не узнает никогда.
3. Всё остальное — `hard_only`. Сюда попали неочевидные категории целиком
   (`RED THINGS`, `___ SAUCE`, `THINGS WITH SEEDS`): связи верные, но для лёгких
   уровней не годятся.

### Разведённые значения

Значения разведены у **161 слова** (401 значение). Кандидатов ищет
`scripts/swow_senses.py`: если категории слова живут в разных ассоциативных
областях, а слово уверенно подходит обеим — значений скорее всего два.

```
crown    -> ROYALTY (корона) / DENTAL WORDS (коронка) / TREE PARTS (крона)
delta    -> BODIES OF WATER (дельта) / GREEK LETTERS (буква) / AIRLINES (компания)
sentence -> WRITING WORDS (предложение) / PRISON WORDS (приговор)
duck     -> WATERFOWL (птица) / MEATS (мясо) / RUBBER THINGS (игрушка)
```

Результат: **1031 категория из 1092 имеет 12 и более пригодных слов**
(`approved` + `hard_only`). Тонкими остались три, и они конечны по природе:
`SEASONS` (5), `MOSS & LICHEN` (6), `AMPHIBIANS` (7).

## 13. Ограничения текущей версии

- Дедупликация значений — только по точному совпадению определения, без семантики.
- Значения разведены у 161 слова-омонима (401 значение). У остальных слов значение
  не указано: для однозначных это нормально, но неразведённая многозначность
  в базе наверняка ещё есть.
- Частотность считается только при установленном `wordfreq`; она измеряет
  употребимость, а не узнаваемость, поэтому по умолчанию не отсекает слова.
- Нет проверки, что слово реально существует в английском языке (нет словаря-оракула).
- `words.is_proper_noun` = «встречается как имя собственное»; настоящее разделение —
  через `word_senses`.
- Нет миграций схемы: при изменении `schema.sql` базу пересобирают из JSONL.
- Реальный LLM-провайдер не покрыт сетевыми тестами (только mock).
- Нет связи с игровой базой `tool/data/categories.json` — по договорённости
  этот пайплайн пока живёт отдельно.

## 14. Следующие шаги

1. AI candidate generator в боевом режиме (реальная модель вместо mock, батчи по каталогу).
2. Reverse expansion по всем approved-словам — набрать пересечения для «ловушек».
3. Генератор уровней поверх базы (выбор категорий, слов-ловушек, целевой сложности).
4. Валидатор Exact Cover: проверка, что уровень раскладывается однозначно.
5. Мост к игровой базе: экспорт SQLite -> `tool/data/categories.json`.
