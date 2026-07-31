# Кейс промптинга: создание базы слов с нуля (этап 1, до аудита)

**Когда:** до внешнего аудита — это промпт, которым база и pipeline были
созданы. Разбор аудита той же базы: `prompts/word-db-audit-gpt-pro.md`.
**Кому адресован:** кодовому агенту (у нас — Claude Code).
**Что получилось:** `tool/word_content_pipeline/` — SQLite-база
«слово — значение — категория», CLI из 8 команд, seed-файлы, тесты.
Структура и формат данных до сих пор те, что заданы в промпте
(`data/categories.jsonl`, `data/membership_candidates.jsonl`,
`src/word_content/{db,models,normalization,repositories,validators,
importers,exporters,cli}.py`), хотя pipeline с тех пор сильно оброс.

---

## Почему кейс хороший

Это пример «спецификация вместо пожелания». Промпт длинный, но каждый
блок закрывает конкретный класс ошибок, которые агент делает, если ему
дать волю:

1. **Роль + один этап.** «senior Python engineer и data/content pipeline
   developer», «нужно создать **первый рабочий этап**». Не «сделай
   инструмент для генерации уровней».
2. **Явный список «НЕ нужно»** (не генерировать уровни, не делать
   Exact Cover, не подключать embeddings, не качать WordNet/Wikidata,
   не звать внешние API). Это самая полезная часть: агент по своей
   инициативе тянет в проект всё, что «пригодится», и этап 1 растягивается
   в неделю.
3. **Схема БД выписана до полей и ограничений**, включая неочевидное:
   уникальный индекс по `word_id + category_id + relation_type +
   COALESCE(sense_id, 0)` и подсказка «если обычным UNIQUE не выйдет —
   сделай expression index». Так агент не изобретает свою модель данных.
4. **Нормализация задана примерами**, а не описанием:
   `" Apple " → "apple"`, `"X–RAY" → "x-ray"`. Примеры проверяемы, описание — нет.
5. **Продуктовые правила отделены от технических.** «Не путай
   корректность и очевидность» (`fit_score` ≠ `obviousness_score`),
   «низкая очевидность не значит ошибка — это материал для сложного
   уровня», «AI-скор нельзя считать истиной, всё AI по умолчанию
   `candidate`». Без этого получилась бы одна шкала «хорошо/плохо».
6. **Анти-примеры с причиной.** `APPLE → HEALTHY THINGS` — плохо, потому
   что категория субъективная и слишком широкая. Требования к 60
   категориям тоже сформулированы через запреты (никаких `NICE THINGS`,
   никаких меняющихся фактов вроде `CURRENT POPULAR SINGERS`, никаких
   узколокальных знаний).
7. **Заданы объёмы seed-данных** (≥60 категорий, ≥150 связей, минимум
   12 тем) и конкретные многозначные слова для проверки модели значений
   (apple, bank, bat, date, orange, spring, pitch, bark, crane, capital).
   Плюс оговорка «не раздувай искусственно — только естественные связи».
8. **Тесты перечислены по случаям**, а не «напиши тесты». Включая
   идемпотентность и защиту ручного `approved` от перезаписи повторным
   импортом (и флаг `--overwrite-review-status` как осознанный обход).
9. **Поведение при ошибках прописано:** одна битая строка не валит весь
   импорт, ошибки складываются в `import_runs.errors_json`, ненулевой
   exit code — только на системной ошибке.
10. **Финальный протокол:** создай все файлы → запусти pytest → smoke-тест
    всех CLI-команд на seed-данных → исправь → перечисли файлы, команды,
    результаты тестов и ограничения. И прямая инструкция
    **«не останавливайся после плана и не проси подтверждения»** —
    иначе агент отдаёт план и ждёт.

## Чего этот промпт не предусмотрел (видно только по аудиту)

Полезно держать рядом с разбором аудита — хорошо составленная
спецификация всё равно оставила дыры в *качестве данных*:

- **Пул ≠ игровая четвёрка.** Промпт требует «минимум 8–12 хороших членов»
  на категорию, но нигде не требует проверенных четвёрок и запрета
  пересекающихся категорий в одном уровне. Аудит нашёл 516 пар категорий
  с ≥4 общими словами.
- **`NULL` не описан как отдельное состояние.** `familiarity_score REAL NULL`
  разрешён, но правила «нет частотности → нельзя `approved`» нет —
  и 20 связей проехали в `approved`.
- **Разделение метрик задано наполовину.** `fit_score` и
  `obviousness_score` разведены (это сильная часть промпта), а вот
  знакомость слова и игровая сложность остались слиты со статусом ревью.
- **Инвариант значений не сделан обязательным.** Есть правило «если
  передан `sense_key`, нужен `sense_definition`», но нет правила
  «если у слова больше одного значения, каждая связь обязана ссылаться
  на `sense_id`» — отсюда 96 связей с `sense_id = NULL`.
- **Отчёты для человека никто не сверял с базой.** `04_flags.md` занижал
  число проблемных категорий (60 вместо 86) — класс ошибок, который
  тестами из промпта не ловится вообще.

Вывод для будущих промптов: список «НЕ нужно» экономит время, но каждый
отложенный пункт стоит завести как явное ограничение данных, иначе он
всплывёт как проблема качества, а не как незакрытая задача.

## Промпт целиком (verbatim)

```text
Ты — senior Python engineer и data/content pipeline developer.

Нужно создать первый рабочий этап инструмента для генерации уровней word association puzzle: локальную базу данных, в которой одно английское слово может принадлежать нескольким категориям и использовать разные значения.

Контекст игры

В одном уровне есть 40 слов, распределённых по категориям. Одно слово может относиться к нескольким категориям.

Примеры:

APPLE:
- FRUITS
- PIE INGREDIENTS
- THINGS WITH SEEDS
- RED THINGS
- TECH COMPANIES
- WORDS BEFORE "SAUCE"

BANK:
- FINANCIAL INSTITUTIONS
- RIVER FEATURES

BAT:
- FLYING MAMMALS
- BASEBALL EQUIPMENT

Важно хранить не только слово и категорию, но и:
- конкретное значение слова;
- тип связи;
- объяснение связи;
- силу связи;
- очевидность связи для среднего американского игрока;
- статус ручной проверки;
- источник записи.

Цель текущего этапа

Создать воспроизводимый pipeline:

1. Создать SQLite-базу.
2. Импортировать каталог категорий из JSONL.
3. Добавлять слова и связи word-category.
4. Импортировать AI-сгенерированные candidate-связи из JSONL.
5. Нормализовать и валидировать данные.
6. Экспортировать кандидатов в CSV для ручной проверки.
7. Импортировать решения reviewer обратно в SQLite.
8. Уметь получать все одобренные категории для конкретного слова.
9. Уметь получать все одобренные слова для конкретной категории.
10. Хранить JSONL как человекочитаемый промежуточный формат, а SQLite использовать как основную рабочую базу.

На этом этапе НЕ нужно:
- генерировать игровые уровни;
- проверять Exact Cover;
- реализовывать gameplay solver;
- делать полноценный веб-интерфейс;
- подключать embeddings;
- скачивать WordNet, Wikidata или ConceptNet;
- автоматически обращаться к внешним API.

Технологии

Используй:
- Python 3.12;
- стандартный sqlite3;
- Pydantic v2 для проверки входных данных;
- Typer для CLI;
- pytest для тестов;
- pathlib;
- csv/json из стандартной библиотеки.

Не используй ORM. SQL должен быть явным и понятным.

Структура проекта

Создай примерно такую структуру:

word_content_pipeline/
  README.md
  pyproject.toml
  .gitignore

  data/
    categories.jsonl
    membership_candidates.jsonl
    review_example.csv

  database/
    .gitkeep

  src/
    word_content/
      __init__.py
      db.py
      schema.sql
      models.py
      normalization.py
      repositories.py
      validators.py
      importers.py
      exporters.py
      cli.py

  tests/
    test_normalization.py
    test_categories_import.py
    test_memberships_import.py
    test_review_flow.py
    test_queries.py

SQLite-схема

Используй следующую логическую модель.

Таблица words:

- id INTEGER PRIMARY KEY
- text TEXT NOT NULL
- normalized TEXT NOT NULL
- language TEXT NOT NULL DEFAULT 'en'
- part_of_speech TEXT NULL
- familiarity_score REAL NULL
- is_proper_noun INTEGER NOT NULL DEFAULT 0
- status TEXT NOT NULL DEFAULT 'active'
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

Ограничение:
- UNIQUE(normalized, language)

Таблица word_senses:

- id INTEGER PRIMARY KEY
- word_id INTEGER NOT NULL
- sense_key TEXT NOT NULL
- definition TEXT NOT NULL
- part_of_speech TEXT NULL
- created_at TEXT NOT NULL

Ограничения:
- FOREIGN KEY word_id → words.id
- UNIQUE(word_id, sense_key)

Таблица categories:

- id INTEGER PRIMARY KEY
- category_key TEXT NOT NULL UNIQUE
- label TEXT NOT NULL
- rule TEXT NOT NULL
- relation_type TEXT NOT NULL
- theme TEXT NOT NULL
- base_difficulty REAL NULL
- status TEXT NOT NULL DEFAULT 'active'
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

Таблица memberships:

- id INTEGER PRIMARY KEY
- word_id INTEGER NOT NULL
- sense_id INTEGER NULL
- category_id INTEGER NOT NULL
- relation_type TEXT NOT NULL
- reason TEXT NOT NULL
- fit_score REAL NOT NULL
- obviousness_score REAL NOT NULL
- source TEXT NOT NULL
- review_status TEXT NOT NULL DEFAULT 'candidate'
- review_comment TEXT NULL
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

Ограничения:
- fit_score от 0 до 1
- obviousness_score от 0 до 1
- review_status только:
  - candidate
  - approved
  - hard_only
  - rejected
- FOREIGN KEY word_id → words.id
- FOREIGN KEY sense_id → word_senses.id
- FOREIGN KEY category_id → categories.id
- одна и та же связь не должна дублироваться

Для защиты от дублей создай уникальный индекс по:
- word_id
- category_id
- relation_type
- COALESCE(sense_id, 0)

Если SQLite не позволяет сделать это обычным UNIQUE constraint, используй expression index.

Дополнительная таблица import_runs:

- id INTEGER PRIMARY KEY
- import_type TEXT NOT NULL
- source_file TEXT NOT NULL
- records_total INTEGER NOT NULL
- records_inserted INTEGER NOT NULL
- records_updated INTEGER NOT NULL
- records_rejected INTEGER NOT NULL
- errors_json TEXT NULL
- created_at TEXT NOT NULL

Это нужно для воспроизводимости и аудита импорта.

Нормализация слов

Реализуй функцию normalize_word.

Правила:
- Unicode NFKC;
- trim;
- lowercase;
- несколько пробелов превращать в один;
- типографские апострофы приводить к обычному апострофу;
- типографские дефисы приводить к обычному дефису;
- не удалять апострофы и дефисы полностью;
- отклонять пустые строки;
- ограничить длину, например 50 символами.

Примеры:

" Apple " → "apple"
"ICE   CREAM" → "ice cream"
"Mother’s" → "mother's"
"X–RAY" → "x-ray"

Pydantic-модели

Создай модели как минимум для:

CategoryInput

Поля:
- category_key
- label
- rule
- relation_type
- theme
- base_difficulty optional
- status optional

MembershipCandidateInput

Поля:
- word
- language default "en"
- part_of_speech optional
- is_proper_noun default false
- sense_key optional
- sense_definition optional
- category_key
- relation_type
- reason
- fit_score
- obviousness_score
- source default "ai"
- review_status default "candidate"

ReviewDecisionInput

Поля:
- membership_id
- decision
- review_comment optional

Валидация category_key:
- только lowercase;
- латинские буквы, цифры и underscore;
- не начинается с цифры;
- пробелы запрещены.

Валидация membership:
- category_key должен существовать в базе;
- reason не может быть пустым;
- fit_score и obviousness_score от 0 до 1;
- если передан sense_key, обязательно должен быть передан sense_definition;
- если передан sense_definition, обязательно должен быть передан sense_key.

Формат categories.jsonl

Одна JSON-запись на строку.

Пример:

{"category_key":"fruits","label":"FRUITS","rule":"Common edible fruits familiar to an average American adult","relation_type":"is_a","theme":"food","base_difficulty":0.1}
{"category_key":"pie_ingredients","label":"PIE INGREDIENTS","rule":"Ingredients commonly used in pie fillings or pie preparation","relation_type":"used_in","theme":"food","base_difficulty":0.25}
{"category_key":"tech_companies","label":"TECH COMPANIES","rule":"Well-known technology companies or consumer technology brands","relation_type":"is_a","theme":"business","base_difficulty":0.25}
{"category_key":"things_with_seeds","label":"THINGS WITH SEEDS","rule":"Common objects or foods that naturally contain seeds","relation_type":"has_property","theme":"nature","base_difficulty":0.35}
{"category_key":"words_before_sauce","label":"WORDS BEFORE SAUCE","rule":"Words that form a familiar English expression when placed before the word sauce","relation_type":"phrase_before","theme":"language","base_difficulty":0.45}

Создай seed-файл минимум из 60 категорий.

Требования к 60 категориям:
- категории должны быть понятны американской casual-аудитории;
- категории не должны быть слишком широкими;
- у каждой потенциально должно быть минимум 8–12 хороших членов;
- используй разные типы связей;
- распределение минимум по 12 темам;
- не используй категории, основанные на субъективных оценках вроде NICE THINGS или GOOD PEOPLE;
- не создавай категории с временно меняющимися фактами вроде CURRENT POPULAR SINGERS;
- избегай категорий, которые требуют узких локальных знаний.

Примерные темы:
- food
- animals
- home
- nature
- transport
- sports
- jobs
- body
- clothing
- tools
- geography
- science
- language
- entertainment
- actions
- properties

Формат membership_candidates.jsonl

Пример:

{"word":"apple","language":"en","part_of_speech":"noun","is_proper_noun":false,"sense_key":"apple_fruit","sense_definition":"The round edible fruit of an apple tree","category_key":"fruits","relation_type":"is_a","reason":"An apple is a common edible fruit","fit_score":1.0,"obviousness_score":1.0,"source":"seed_manual"}
{"word":"apple","language":"en","part_of_speech":"noun","is_proper_noun":false,"sense_key":"apple_fruit","sense_definition":"The round edible fruit of an apple tree","category_key":"pie_ingredients","relation_type":"used_in","reason":"Apples are commonly used as pie filling","fit_score":0.99,"obviousness_score":0.95,"source":"seed_manual"}
{"word":"Apple","language":"en","part_of_speech":"proper_noun","is_proper_noun":true,"sense_key":"apple_company","sense_definition":"The American technology company Apple Inc.","category_key":"tech_companies","relation_type":"is_a","reason":"Apple is a well-known technology company","fit_score":1.0,"obviousness_score":0.99,"source":"seed_manual"}
{"word":"apple","language":"en","part_of_speech":"noun","is_proper_noun":false,"sense_key":"apple_fruit","sense_definition":"The round edible fruit of an apple tree","category_key":"words_before_sauce","relation_type":"phrase_before","reason":"Apple forms the common expression apple sauce","fit_score":0.98,"obviousness_score":0.9,"source":"seed_manual"}

Создай seed-файл минимум со 150 membership-связями.

В seed должны присутствовать примеры многокатегорийных слов:
- apple
- bank
- bat
- date
- orange
- spring
- pitch
- bark
- crane
- capital

Не пытайся искусственно дать каждому слову много категорий. Добавляй только естественные и защищаемые связи.

CLI-команды

Реализуй CLI через Typer.

Команды:

1. init-db

Пример:

python -m word_content.cli init-db --db database/content.sqlite

Создаёт базу и таблицы. Повторный запуск безопасен.

2. import-categories

Пример:

python -m word_content.cli import-categories \
  --db database/content.sqlite \
  --input data/categories.jsonl

Поведение:
- валидирует каждую строку;
- создаёт новые категории;
- обновляет существующие по category_key;
- записывает import_run;
- в конце показывает:
  - total
  - inserted
  - updated
  - rejected.

3. import-memberships

Пример:

python -m word_content.cli import-memberships \
  --db database/content.sqlite \
  --input data/membership_candidates.jsonl

Поведение:
- нормализует слово;
- создаёт word, если его ещё нет;
- создаёт word_sense, если переданы данные значения;
- находит category по category_key;
- создаёт или обновляет membership;
- не создаёт дубликаты;
- ошибки одной строки не должны останавливать весь импорт;
- сохраняет список ошибок в import_runs.errors_json;
- команда завершается ненулевым exit code только при системной ошибке, а не при нескольких невалидных строках.

4. export-review

Пример:

python -m word_content.cli export-review \
  --db database/content.sqlite \
  --output data/review_candidates.csv \
  --status candidate

CSV должен содержать:

- membership_id
- word
- normalized
- sense_key
- sense_definition
- category_key
- category_label
- category_rule
- relation_type
- reason
- fit_score
- obviousness_score
- source
- current_status
- decision
- review_comment

Поля decision и review_comment должны быть пустыми для ручного заполнения.

5. import-review

Пример:

python -m word_content.cli import-review \
  --db database/content.sqlite \
  --input data/review_candidates.csv

Поведение:
- читает membership_id;
- принимает decision:
  - approved
  - hard_only
  - rejected
  - candidate
- обновляет review_status и review_comment;
- некорректные строки перечисляет в результате.

6. word-info

Пример:

python -m word_content.cli word-info \
  --db database/content.sqlite \
  --word apple \
  --statuses approved,hard_only

Выводит таблицу:
- word;
- sense;
- category;
- relation_type;
- fit_score;
- obviousness_score;
- review_status;
- reason.

7. category-info

Пример:

python -m word_content.cli category-info \
  --db database/content.sqlite \
  --category fruits \
  --statuses approved,hard_only

Выводит все слова категории.

8. stats

Пример:

python -m word_content.cli stats --db database/content.sqlite

Выводит:
- число уникальных слов;
- число значений слов;
- число категорий;
- число memberships;
- количество memberships по review_status;
- среднее число категорий на слово;
- число слов с одной категорией;
- число слов с 2, 3, 4, 5+ категориями;
- категории с количеством approved-связей меньше 8;
- топ-20 слов по числу approved-категорий;
- топ-20 категорий по числу approved-слов.

Правила upsert

Categories:
- идентификатор — category_key;
- при повторном импорте обновлять label, rule, relation_type, theme, base_difficulty и status.

Words:
- идентификатор — normalized + language;
- сохранять исходный text;
- не создавать отдельные words для Apple и apple;
- различия значения должны храниться через word_senses.

Senses:
- идентификатор — word_id + sense_key.

Memberships:
- идентификатор — word + category + relation_type + sense;
- повторный импорт должен обновлять reason, scores и source;
- вручную выставленный approved/hard_only/rejected не должен автоматически сбрасываться обратно в candidate при повторном импорте;
- добавь CLI-флаг --overwrite-review-status для принудительного обновления статуса.

Важные продуктовые правила

1. Не путай корректность и очевидность.

Например:
- APPLE → FRUITS:
  - fit_score = 1.0
  - obviousness_score = 1.0

- APPLE → WORDS BEFORE SAUCE:
  - fit_score может быть 0.98
  - obviousness_score может быть 0.85

Низкая obviousness не означает, что связь неправильная. Она может быть полезна для сложного уровня.

2. Не добавляй слабые метафорические связи.

Плохой пример:
APPLE → HEALTHY THINGS

Причина:
категория субъективная и слишком широкая.

3. Категория должна описываться правилом, а не только label.

4. Разные значения одной строки должны быть разделены через word_senses.

5. Нельзя доверять AI-generated score как абсолютной истине. Все записи AI должны по умолчанию иметь candidate.

6. Для seed_manual допустимо установить approved только у очевидных и вручную подготовленных примеров. Все остальные оставь candidate.

Тесты

Напиши тесты минимум для следующих случаев:

1. Нормализация:
- Apple и apple дают один normalized;
- несколько пробелов;
- типографский апостроф;
- типографский дефис;
- пустая строка отклоняется.

2. Импорт категорий:
- новая категория создаётся;
- повторный импорт обновляет категорию;
- неправильный category_key отклоняется;
- обработка невалидной JSON-строки.

3. Импорт memberships:
- слово создаётся автоматически;
- существующее слово переиспользуется;
- создаётся sense;
- одна строка слова может иметь несколько senses;
- слово может принадлежать нескольким категориям;
- повторный импорт не создаёт дубликат;
- отсутствующая category_key отклоняется;
- score вне диапазона отклоняется;
- sense_key без definition отклоняется.

4. Review flow:
- export-review создаёт ожидаемые колонки;
- import-review обновляет status;
- неизвестный membership_id отклоняется;
- неизвестный decision отклоняется;
- повторный импорт AI-кандидата не сбрасывает approved.

5. Запросы:
- word-info для apple возвращает несколько категорий;
- category-info возвращает только нужные статусы;
- stats правильно считает количество категорий на слово.

6. Идемпотентность:
- два одинаковых запуска импорта дают одинаковое количество сущностей.

README

README должен содержать:

1. Описание задачи.
2. Почему используется SQLite + JSONL.
3. Диаграмму сущностей в текстовом виде.
4. Инструкцию установки.
5. Все CLI-команды с примерами.
6. Описание review workflow:
   - импортировать candidates;
   - экспортировать CSV;
   - заполнить decision;
   - импортировать CSV обратно.
7. Объяснение fit_score и obviousness_score.
8. Примеры запросов для APPLE.
9. Ограничения первой версии.
10. Следующие шаги:
    - AI candidate generator;
    - reverse expansion word → categories;
    - генератор уровней;
    - Exact Cover validator.

Качество реализации

- Код должен быть полностью рабочим, а не псевдокодом.
- Все пути должны приниматься через CLI.
- Не хардкодь абсолютные пути.
- Используй транзакции.
- Включи PRAGMA foreign_keys = ON.
- Добавь понятные сообщения об ошибках.
- Добавь type hints.
- Избегай чрезмерной архитектуры.
- Не создавай веб-интерфейс.
- Не оставляй TODO вместо обязательной функциональности.
- Не ограничивайся описанием или планом: создай все файлы проекта.
- После реализации запусти pytest.
- Затем проведи smoke test всех основных CLI-команд на seed-данных.
- Исправь найденные ошибки.
- В финальном ответе перечисли:
  - созданные файлы;
  - команды запуска;
  - результаты тестов;
  - известные ограничения.

Последовательность работы

1. Сначала кратко сформулируй технический план.
2. Затем сразу создавай проект.
3. Реализуй SQLite schema и database layer.
4. Реализуй модели и нормализацию.
5. Реализуй import/export.
6. Реализуй CLI.
7. Создай seed categories и memberships.
8. Напиши тесты.
9. Запусти тесты и smoke test.
10. Исправь ошибки до рабочего состояния.

Не останавливайся после плана и не проси подтверждения, если можешь принять разумное техническое решение самостоятельно.
```
