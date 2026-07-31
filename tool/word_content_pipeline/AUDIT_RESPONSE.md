# Ответ на аудит базы слов (word_database_audit, снимок 31.07.2026)

Источник правды остаётся текстовым: `data/seed/*.txt`, `data/seed/_*.json`,
`data/review_decisions.csv`. SQLite пересобирается из них. Экспортированный
`БАЗА-СЛОВ/база-слов.sqlite` не редактируется руками — только пересобирается.

Легенда статусов реализации: `[x]` сделано, `[~]` сделано частично, `[m]` вынесено
в ручное решение (`ревью/06_manual_decisions.md`).

---

## 1. Карта «замечание аудита → файл проекта»

| # | Замечание | Где живёт причина | Что меняем |
|---|---|---|---|
| P0-1 | `approved` при `familiarity_score IS NULL` (26 слов, 20 approved) | `scripts/build_seed.py:_is_rare` (None → «не редкое»), `scripts/swow_status.py` (fallback), `importers.apply_membership` (нет гейта) | гейт «нет частотности → `candidate`» на всех трёх уровнях + integrity check |
| P0-2 | 96 связей у 18 многозначных слов с `sense_id = NULL` | `build_seed.build_memberships`: слова из файла темы не знают о значениях из `_ambiguous.json` | новый источник `data/seed/_sense_map.json` (значения + карта категория→значение) и жёсткая проверка инварианта в `build_seed.validate` |
| P0-3 | 736 переиспользуемых слов без значений | детектор `scripts/swow_senses.py` не даёт очереди в машинном виде | новый `scripts/sense_gaps.py` → `data/sense_review_queue.csv` + раздел в review pack |
| P0-4 | `04_flags.md` показывает 60 из 86 категорий | `export_review_pack.write_flags`: `LIMIT 60` и `total >= 8` в знаменателе | убрать LIMIT, считать по playable-знаменателю, добавить разделы |
| P0-5 | нет проверки, что категория соберёт четвёрку | нигде | `integrity.py:check_quartet_capability` + `categories.readiness` |
| P0-6 | 516 пар категорий с ≥4 общими словами | нигде | `scripts/derive_conflicts.py` → `data/category_conflicts.csv` → таблица `category_conflicts` |
| P0-7 | подтверждённые семантические ошибки | `data/seed/*.txt` | правки пулов, правил и названий (список в §3) |
| P0-8 | 34 категории не собирают normal-четвёрку | нигде | `readiness` + `categories.status='disabled'`, исключение из `list_categories` |
| P1-1 | смешаны семантика / знакомость / очевидность / сложность | `swow_status.py` (одна лестница), `memberships` (одна колонка статуса) | `memberships.semantic_status`, `memberships.gameplay_difficulty`, абсолютные пороги статуса |
| P1-2 | нет слоя проверенных четвёрок | нигде | `quartets`, `quartet_words`, `scripts/build_quartets.py`, `data/quartets.csv` |
| P1-3 | нет solver единственности | `tool/scripts/solver_*.py` работают по игровой базе, не по контентной | `src/word_content/solver.py` + CLI `solve-level` |
| P1-4 | нет запретов на сочетание категорий | нигде | `category_conflicts` + ручной слой `data/seed/_conflicts_manual.txt` |
| P1-5 | нет readiness у категорий | нигде | `categories.readiness` + CLI `derive-readiness` |
| P2 | нет версии схемы/контента | `schema.sql` (`user_version = 0`) | `PRAGMA user_version`, таблица `schema_meta` (git commit, хеши источников) |

---

## 2. Изменения по файлам

### 2.1 Схема и модели

**`src/word_content/schema.sql`**
- `PRAGMA user_version = 2`.
- `schema_meta(key, value)` — schema_version, content_version, git_commit, source hashes,
  wordfreq/SWOW версии, время сборки.
- `categories`: `+ readiness TEXT NOT NULL DEFAULT 'unknown'`
  (`ready | constrained | curated_only | hard_only | blocked | unknown`),
  `+ readiness_reason TEXT`.
- `memberships`: `+ semantic_status TEXT NOT NULL DEFAULT 'unreviewed'`
  (`unreviewed | correct | disputed | incorrect`),
  `+ gameplay_difficulty REAL NULL`.
- новые таблицы `category_conflicts`, `category_pair_groups`, `quartets`, `quartet_words`.

**`src/word_content/models.py`**
- `MembershipCandidateInput`: `+ semantic_status`, `+ gameplay_difficulty`.
- `RISK_FLAGS`: `+ outdated_term`, `+ trademark`, `+ needs_sense`.
- новые модели `CategoryConflictInput`, `QuartetInput`.

### 2.2 Гейт частотности (P0-1)

**`src/word_content/validators.py`** — `familiarity_gate(status, familiarity)`:
`None` → `candidate` + причина. Единая точка для импортов.

**`src/word_content/importers.py`** — вызов гейта в `apply_membership` и в
`import_review_csv` (решение из CSV тоже не может дать `approved` без частотности).

**`scripts/build_seed.py`** — `_is_rare` → `_needs_review`: `None` тоже уходит в `candidate`.

### 2.3 Значения многозначных слов (P0-2, P0-3)

**новый `data/seed/_sense_map.json`**
```json
{
  "senses":      { "ring": { "ring_sound": {"definition": "...", "part_of_speech": "noun"} } },
  "assignments": { "ring": { "bell_and_alarm": "ring_sound", "boxing_words": "ring_arena" } }
}
```
**`scripts/build_seed.py`** — применяет карту к связям из файлов тем; инвариант:
у слова с ≥2 значениями каждая связь обязана иметь `sense_key`, иначе сборка падает
со списком незакрытых связей.

**новый `scripts/sense_gaps.py`** — слова с ≥4 играбельными категориями в ≥3 темах
без значений, минус `_not_homonyms.txt` → `data/sense_review_queue.csv`.

### 2.4 Статусы по абсолютным порогам (P1-1)

**`scripts/swow_status.py`** — абсолютный пол вместо потолка «неочевидная категория»:
```
abs = 0.6*obviousness + 0.4*min(familiarity/0.7, 1)
abs >= 0.63 -> пол approved
abs >= 0.48 -> пол alternative
```
Пол не применяется, если: у слова больше одного значения (там судит `_ambiguous.json`),
`relation_type in (phrase_before, phrase_after)` (это игра слов, а не узнаваемость),
частотность неизвестна (гейт → `candidate`). SWOW остаётся вторичным сигналом:
может поднять выше пола, но не опустить ниже.

Проверка на примерах аудита: `xylophone`→MUSICAL INSTRUMENTS 0.75,
`key`→KEYCHAIN THINGS 0.82, `Sahara`→DESERTS 0.67, `agenda`→LATIN PHRASES 0.71,
`camera`→THINGS WITH SCREENS 0.88 — все выше порога approved.

Дополнительно пишется `gameplay_difficulty = 0.5*(1-abs) + 0.5*base_difficulty`.

### 2.5 Конфликты категорий и readiness (P0-5, P0-6, P0-8, P1-4, P1-5)

**новый `scripts/derive_conflicts.py`** → `data/category_conflicts.csv`
(пары с ≥4 общими играбельными словами, severity по величине пересечения)
плюс ручной слой `data/seed/_conflicts_manual.txt`.

**новый `src/word_content/readiness.py`** — вывод readiness из пулов:
`blocked` (<4 normal-слов) → `categories.status='disabled'`;
`hard_only` (нет normal-слов вообще); `curated_only` (ручной флаг: субъективное
или парное правило); `constrained` (<12 играбельных или перевес hard_only); `ready`.

**новый `data/seed/_category_meta.json`** — ручные оверрайды: `curated_only`,
`pair_structured` (OPPOSITES), заметки.

### 2.6 Четвёрки и solver (P1-2, P1-3)

**новый `src/word_content/solver.py`** — `unique_partition(level)`: перечисляет все
разбиения слов уровня на группы по 4, целиком лежащие в пуле какой-нибудь категории.
Уровень принимается, только если корректное разбиение ровно одно.

**новый `scripts/build_quartets.py`** — для каждой `ready`-категории собирает четвёрки
из normal-пула, прогоняет через solver (четвёрка отбрасывается, если её слова целиком
лежат в другой категории), пишет `data/quartets.csv` со `review_state=auto_validated`.

### 2.7 Проверки и выдача

**новый `src/word_content/integrity.py` + `scripts/integrity_checks.py`** — критерии
готовности из аудита, ненулевой код возврата при провале:
нет `approved/alternative` без частотности; нет `NULL sense_id` у многозначных;
нет включённых normal-категорий с пулом <4; нет `semantic_status='incorrect'`
среди играбельных; все четвёрки проходят solver; FK и `integrity_check`.

**`scripts/export_review_pack.py`** — исправленный `04_flags.md` (без `LIMIT`,
корректный знаменатель, новые разделы), новые файлы
`06_manual_decisions.md`, `07_readiness_and_conflicts.md`, `08_quartets.csv`.

**`src/word_content/cli.py`** — команды `check-integrity`, `derive-readiness`,
`import-conflicts`, `import-quartets`, `solve-level`.

---

## 3. Семантические правки (P0-7)

Приняты (высокая уверенность, есть источник или прямое противоречие правилу):

| категория | правка |
|---|---|
| BUTTERFLIES AND MOTHS | `gypsy moth` → `spongy moth` (официальное переименование USDA/ESA) |
| DAIRY BRANDS | убрать `Eskimo Pie` (переименован в Edy's Pie), ключ `candy_bar_flavors` → `ice_cream_brands` |
| WORLD DANCES | убрать `kabuki` (форма театра) |
| ARCTIC ANIMALS | название → `POLAR ANIMALS` (правило говорит о полярных регионах, в пуле пингвин) |
| CRUSTACEANS | правило → таксономическое, `crayfish`/`pill bug` перестают противоречить |
| SEAL FAMILY | правило включает моржа явно |
| WATERFOWL | убрать `heron`, `egret`, `ibis` (болотные, не плавающие) |
| WORMS | убрать `ringworm` (заболевание, не животное) |
| INSECTS | название → `BUGS` (в пуле паук, многоножка, клещ) |
| SLEEP ACTIONS | убрать `wake` |
| WAYS OF LOOKING | убрать `blink` |
| BOARD GAMES | убрать `jenga`, `dominoes`, `yahtzee` (без доски), правило уточнено |
| ANIMAL GROUPS | убрать `hive`, `nest` (сооружения, не собирательные существительные) |
| BANK BRANDS | убрать `Visa`, `Mastercard`, `Amex`, `Discover`, правило → только банки |
| BABY ANIMALS | убрать `calfling` (не английское слово) |
| AMPHIBIANS | убрать `tadpole` (стадия развития), `treefrog` → `tree frog` |
| EXTINCT ANIMALS | правило → «вымершие животные, которых узнают», а не «виды» |
| нормализация | `paper clip`/`paperclip`, `call sign`/`callsign`, `sun hat`/`sunhat`, `ear muffs`/`earmuffs`, `second hand`/`secondhand`, `bird bath`/`birdbath` — одна каноническая форма |

Вынесены в ручное решение (спорно, нужен носитель языка или продуктовое решение):

- WORMS: `silkworm`, `inchworm`, `glowworm` — не «настоящие» черви, но так их называют.
- NATIONAL SYMBOLS: нет страны в данных → `curated_only`, не для автогенерации.
- OPPOSITES: нужен слой пар → `curated_only` + `category_pair_groups`.
- SOFT CREATURES, CLASSIC GAMES: субъективные правила.
- DAIRY BRANDS: `Dreyers` и `Edys` — один продукт под региональными именами.
- 105 длинных названий: проверять в реальном UI.
- орфография брендов (`Kitkat`, `Reeses`, `McDonalds`, `OHare`) — нужен sense-level
  `display_text`, это P2.
- 736 слов из `sense_review_queue.csv`.

---

## 4. Что сделано

### P0

| # | Замечание | Статус | Как проверить |
|---|---|---|---|
| 1 | `approved` при `familiarity_score IS NULL` | `[x]` гейт в трёх местах: `build_seed._needs_review`, `swow_status`, `models.familiarity_gate` (вызывается из `apply_membership` и `set_review_status`) | `check-integrity` → «нет играбельных связей со словом без частотности»: 0 |
| 2 | 96 связей многозначных слов без `sense_id` | `[x]` 85 закрыты через `_sense_map.json` (15 новых значений), 11 — осознанное исключение для категорий игры слов | `check-integrity` → 0 нарушений + информационный пункт с 11 исключениями |
| 3 | Механизм поиска слов, которым нужны значения | `[x]` `src/word_content/sense_gaps.py` + команда `sense-gaps` → `data/sense_review_queue.csv` | `sense-gaps` находит 556 слов, из них 65 P0 |
| 4 | `04_flags.md` показывал 60 из 86 категорий | `[x]` `LIMIT` убран, знаменатель — играбельные связи, добавлены разделы про частотность, approved и риски; любая отсечка объявляется в тексте | раздел 5 показывает 21 из 21 |
| 5 | Нет проверки пригодности категории для четвёрки | `[x]` `readiness.py` + `integrity.check_normal_quartet_capability` | `check-integrity` → 0 |
| 6 | Нет проверки конфликтов и пересечений | `[x]` `conflicts.py` + команда `derive-conflicts` + таблица `category_conflicts` | 516 пар (514 derived + 3 manual), 86 из них P0 |
| 7 | Подтверждённые семантические ошибки | `[x]` 18 правок в `data/seed/*.txt` (список в §3) | `_semantic_review.csv`, раздел 1 в `06_manual_decisions.md` |
| 8 | Отключить категории без нормальной четвёрки | `[x]` `readiness` + `status='disabled'` для `blocked` | было 34 → осталось 5 (`hard_only`), `blocked` 0 |

### P1

| # | Замечание | Статус |
|---|---|---|
| 1 | Разделить семантику, знакомость, очевидность и игровую сложность | `[x]` `memberships.semantic_status`, `memberships.gameplay_difficulty`, абсолютные пороги статуса; таблица осей в README §3 |
| 2 | Слой проверенных четвёрок | `[x]` `quartets` + `quartet_words`, 3005 четвёрок в статусе `auto_validated` |
| 3 | Solver единственности решения | `[x]` `src/word_content/solver.py` + команда `solve-level`; категория в разбиении используется один раз |
| 4 | Конфликты и запреты на сочетание | `[x]` `category_conflicts` (derived + manual), `category_pair_groups` для OPPOSITES |
| 5 | Readiness категорий | `[x]` `categories.readiness` + `readiness_reason`, команда `derive-readiness` |

### P2 (частично)

- `[x]` `PRAGMA user_version = 2`, таблица `schema_meta`: версия схемы и контента,
  git-коммит, хеши всех трёх источников, версия wordfreq, время сборки.
- `[x]` Слой рисков заполнен: 5557 связей из 17 556 (было 0). Механические флаги
  (`multiword`, `proper_noun`, `obscure`, `trademark`, `culturally_specific`,
  `no_familiarity`) плюс ручные из `_risk_flags.csv`.
- `[m]` Sense-level `display_text` и concept/alias слой — не сделано, остаётся P2.
- `[m]` 105 длинных надписей — вынесены в `06_manual_decisions.md` §5, нужен реальный UI.
- `[ ]` `generation_runs` по-прежнему пуст: генератор уровней в него ещё не пишет.

## 5. Результаты после пересборки

| метрика | было (аудит) | стало |
|---|---|---|
| категорий | 1 092 | 1 093 |
| слов | 10 005 | 10 007 |
| связей | 17 550 | 17 556 |
| `approved` | 8 954 | 12 598 |
| `alternative` | 6 032 | 3 955 |
| `hard_only` | 2 503 | 917 |
| `rejected` | 61 | 60 |
| `candidate` | 0 | 26 (закрыты гейтом частотности) |
| `approved` при NULL-частотности | 20 | **0** |
| связей многозначных слов без значения | 96 | **0** (11 — объявленное исключение) |
| значений / слов со значениями | 549 / 222 | 564 / 222 |
| категорий без нормальной четвёрки | 34 | **5** (`readiness = hard_only`) |
| категорий без `approved` | 249 | 159 |
| категорий с меньше чем 4 `approved` | 276 | 221 |
| `hard_only` при очевидности ≥ 0.80 | 355 | 48 |
| категорий в `04_flags.md` (перевес hard_only) | 60 из 86 | 21 из 21 |
| связей с непустым `risk_flags` | 0 | 5 557 |
| проверенных четвёрок | 0 | 3 005 |
| запретов на сочетание категорий | 0 | 516 |
| `PRAGMA user_version` | 0 | 2 |
| тестов | 93 | 123 |

`hard_only` сократился втрое намеренно: аудит показал, что статус был перегружен —
он одновременно означал «неочевидно», «редкое слово» и «сложный уровень». Игровая
сложность вынесена в `gameplay_difficulty` (заполнена у 17 530 связей), а `hard_only`
теперь значит только «игрок сам не догадается».

Что **не** улучшилось радикально: 159 категорий по-прежнему без единого `approved`
(было 249). Это почти целиком категории игры слов (`___ BOARD`, `SNOW ___`) и категории
с флагом `C`: у них абсолютный пол не применяется по построению, потому что там играет
не узнаваемость слова, а загадка. Для нормальных уровней это не блокер — четвёрка
собирается из `alternative` (у всех 1 084 не-`curated_only` категорий нормальный пул
не меньше четырёх), но уровень получается сложнее, чем задумано. Полный список —
раздел 6 в `04_flags.md`.

## 6. Порядок команд для пересборки

```bash
cd tool/word_content_pipeline
.venv/bin/python scripts/build_seed.py
.venv/bin/python scripts/swow_status.py
rm -f database/content.sqlite*
.venv/bin/word-content init-db            --db database/content.sqlite
.venv/bin/word-content import-categories  --db database/content.sqlite --input data/categories.jsonl
.venv/bin/word-content import-memberships --db database/content.sqlite --input data/membership_candidates.jsonl
.venv/bin/word-content import-review      --db database/content.sqlite --input data/review_decisions.csv
.venv/bin/word-content derive-readiness   --db database/content.sqlite
.venv/bin/word-content derive-conflicts   --db database/content.sqlite --output data/category_conflicts.csv
.venv/bin/word-content build-quartets     --db database/content.sqlite --output data/quartets.csv
.venv/bin/word-content sense-gaps         --db database/content.sqlite --output data/sense_review_queue.csv
.venv/bin/word-content stamp-version      --db database/content.sqlite --content-version 2026.07.31
.venv/bin/word-content check-integrity    --db database/content.sqlite
.venv/bin/python scripts/export_review_pack.py --db database/content.sqlite
```
