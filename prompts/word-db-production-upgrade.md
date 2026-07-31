# Кейс промптинга: база слов -> production content system (не запускался)

**Дата получения:** 31.07.2026, вечер (файл `CLAUDE_CODE_WORD_DATABASE_UPGRADE.md`)
**Автор задания:** ChatGPT Pro — следующий шаг после аудита базы
(см. `prompts/word-db-audit-gpt-pro.md`)
**Статус: ХРАНИТСЯ, В РАБОТУ НЕ ВЗЯТ.** Ничего по этому заданию не делалось.
Предназначено для отдельной сессии. Перед запуском — ручное ревью
(см. «Что решить до запуска» ниже).

---

## О чём задание в одном абзаце

Превратить `tool/word_content_pipeline` из «базы слов с пулами» в управляемую
content system: разделить *принцип группировки* (category concept),
*его игровую формулировку* (category variant) и *конкретную четвёрку слов*
(quartet variant); сделать уровень first-class сущностью; и главное — заменить
локальную проверку четвёрки на **solver полного уровня**, который принимает
уровень только при `solution_count == 1`. Плюс meta-цепи (label решённой
категории становится словом в родительской), кампания с cooldown,
модель сложности, risk/policy workflow и честное разделение
«предложено AI» / «проверено автоматикой» / «подтверждено человеком».

## Структура задания: 24 раздела, 1564 строки, 7 фаз

| § | О чём |
|---|---|
| 1 | Что нельзя потерять из текущего состояния; source of truth остаётся текстовым |
| 2 | Продуктовая модель: словаря уже достаточно (10-13k), рост — за счёт принципов группировки, а не количества слов |
| 3 | Целевая ёмкость: 3-4k принципов группировки, 8-9k готовых четвёрок, 500-1000 golden-четвёрок с ручным ревью |
| 4 | Восемь классов категорий: таксономии, подкатегории, свойства, назначение, association hubs, phrase/compound, polysemy, парные/структурные |
| 5 | Новая схема: concepts/variants/aliases, sense_mode вместо неоднозначного NULL, quartet variants, structured data, meta graph, level_instances, usage history, solver runs |
| 6 | **Главный P0: solver полного уровня** — exact cover, стоп после второго решения, meta-solver по состояниям, timeout != unique |
| 7 | Значения, display text, омонимы (bell, Charger, Jasmine, rose, siren, cricket, iris, Life, Spirit), написания брендов |
| 8 | Bridge words: считаемый bridge_score, кандидаты в meta-label |
| 9 | Пайплайн расширения: propose -> normalize -> dedupe -> validate -> sense resolve -> quartet build -> solver -> policy -> review |
| 10 | Human review и golden set: review pack на 500-1000 четвёрок, AI сам себе approval не ставит |
| 11 | Кампания и cooldown: слово 15-30 уровней, вариант категории 40-80, точная четвёрка 100+ |
| 12 | Модель сложности из 14 компонентов + шаблоны уровней (onboarding, chain_heavy, ambiguity_heavy, ...) |
| 13 | Risk/policy workflow: safe / needs_review / sensitive / trademark / outdated / regional / obscure / blocked |
| 14 | Список известных техдефектов на проверку (часть могла быть уже закрыта после аудита) |
| 15 | Текстовые source-of-truth файлы для новых сущностей (`data/content/*`) |
| 16 | CLI: migrate-schema, solve-level, validate-levels, schedule-campaign, ... + флаги --seed/--dry-run/--resume |
| 17 | Integrity checks, падающие с ненулевым кодом (по каждому слою) |
| 18 | Тесты: unit, solver (включая ambiguity-regression), migration, end-to-end одной командой |
| 19 | Порядок работы: Phase 0 baseline -> 1 correctness -> 2 schema -> 3 normalization -> 4 quartets -> 5 meta -> 6 campaign -> 7 export |
| 20 | Обязательные артефакты: 9 документов в `docs/` + review pack + sample-уровни + отчёты |
| 21 | Метрики before/after (список из ~20 показателей) |
| 22 | Definition of Done по пяти осям |
| 23 | Формат финального отчёта: 14 пунктов с конкретными counts и путями |
| 24 | Главный принцип: сначала доказуемая корректность и воспроизводимость, потом объём |

## Что здесь действительно новое для нас

- **Solver полного уровня.** Сейчас проверяется уникальность отдельной
  четвёрки. Неоднозначность же возникает на уровне целиком: два слова
  меняются местами между группами, и разбиений становится два. Это самый
  ценный пункт задания.
- **Concept / variant / quartet как три разные сущности.** Сейчас категория
  и её игровая формулировка — одно и то же, а четвёрка собирается из пула.
- **Meta-цепи** (label решённой категории становится словом родительской) —
  механики такого уровня у нас в генераторе нет вообще.
- **Кампания и cooldown как конфиг**, а не как правило свежести внутри скрипта.

## Что решить до запуска (ручные решения, не для агента)

1. **Объём.** 24 раздела и 7 фаз — это не одна сессия. Разумно резать:
   Phase 0-1 (baseline + solver полного уровня + починка значений) отдельной
   сессией со своим отчётом, остальное — после ревью результата.
2. **§14 может быть устаревшим.** Часть дефектов (пустой `generation_runs`,
   константный `fit_score`, misleading `solver_state=unique`) уже разбиралась
   в ответе на аудит. Phase 0 обязателен: сначала baseline, потом правки.
3. **Словарь статусов.** Задание вводит свой набор
   (`ai_proposed` / `auto_validated` / `human_approved` / ... + `eligibility_tier`),
   а после аудита у нас уже есть `semantic_status`, `gameplay_difficulty`,
   `readiness`. Нужно решить: маппинг в существующие оси или замена. Два
   параллельных словаря статусов — худший вариант.
4. **`data/content/*` против `data/seed/*`.** Задание предлагает новый layout
   текстовых источников. Решить: миграция или сосуществование.
5. **Meta-цепи — продуктовое решение.** Нужны ли они в нашей playable-версии
   и в сдаче задания вообще. Это не техника, это дизайн.
6. **Golden set 500-1000 четвёрок — это живые человеко-часы.** Агент может
   только подготовить очередь; approval ставит человек.
7. **Автономность против ревью.** В задании есть «не блокируй работу
   уточняющим вопросом, прими консервативное решение». С 24 разделами это
   даёт огромный неревьюируемый диф. Лучше оставить требование
   decision log, но ограничить объём фазами.

---

## Задание целиком (verbatim, как получено)

# Задание для Claude Code: превратить базу слов в production-ready content system

## Роль

Ты работаешь как senior data/content engineer, backend engineer и technical game designer словесной puzzle-игры.

Твоя задача — **не переписать базу с нуля**, а последовательно развить существующий проект `tool/word_content_pipeline` в воспроизводимую production-систему, которая:

1. хранит канонические слова, их значения и игровые связи;
2. хранит конкретные игровые группы ровно по четыре слова;
3. умеет собирать из этих групп полные уровни;
4. гарантирует единственность решения полного уровня;
5. поддерживает плоские уровни и уровни с последовательными meta-цепями;
6. управляет повторным использованием слов, категорий и групп по кампании;
7. отделяет автоматически предложенный контент от контента, подтверждённого человеком;
8. полностью пересобирается из читаемых source-of-truth файлов;
9. выдаёт понятный review pack для контентного и продуктового контроля.

Работай непосредственно в существующем репозитории. Не останавливайся после составления плана: после анализа реализуй изменения, мигрируй данные, запусти проверки, пересобери SQLite и подготовь итоговый отчёт.

Если встречаешь спорное продуктовое решение, не блокируй работу уточняющим вопросом. Прими наиболее консервативное решение, вынеси спорные элементы в manual-review очередь и зафиксируй допущение в decision log.

---

# 1. Текущее состояние, которое нужно сохранить и развить

На текущем снимке примерно:

- 10 007 уникальных слов;
- 1 093 категории;
- 17 556 связей слово-категория;
- 564 разведённых значения у 222 слов;
- 3 005 автоматически сформированных четвёрок;
- 516 конфликтов категорий.

В проекте уже есть полезные сущности и механизмы:

- `words`;
- `word_senses`;
- `categories` с `readiness`;
- `memberships` с раздельными semantic/gameplay полями;
- `category_conflicts`;
- `category_pair_groups`;
- `quartets` и `quartet_words`;
- `schema_meta`;
- `import_runs` и `generation_runs`;
- команды пересборки и `check-integrity`.

Эти улучшения нельзя потерять или заменить более простой моделью.

## Источник правды

SQLite остаётся **собираемым артефактом**, а не редактируемым вручную источником правды.

Рабочие данные должны продолжать жить в текстовых файлах внутри `tool/word_content_pipeline/data/`, включая существующие:

```text
data/seed/*.txt
data/seed/_ambiguous.json
data/seed/_sense_map.json
data/seed/_semantic_review.csv
data/seed/_risk_flags.csv
data/seed/_category_meta.json
data/review_decisions.csv
```

Новые типы данных также должны иметь читаемое, детерминированное текстовое представление. Не делай изменения только в `content.sqlite` или экспортном `база-слов.sqlite`.

## Обязательные правила совместимости

- Сохраняй существующие стабильные ID, если сущность семантически остаётся той же.
- Для переименований и дедупликации добавляй mapping/migration, а не молча создавай новые сущности.
- Старые CLI-команды должны либо продолжить работать, либо получить понятный backward-compatible переход.
- Любое новое поле должно иметь документированную семантику и допустимые значения.
- Все экспорты должны быть детерминированными: одинаковые источники дают byte-stable результат, кроме явно документированных timestamps.

---

# 2. Главная продуктовая модель

## 2.1. Словаря уже достаточно; масштаб строится не количеством слов

Не ставь целью бесконечное увеличение `words`.

Целевой диапазон словаря для текущей кампании:

```text
10 000–13 000 качественных уникальных слов и выражений
```

Основной рост должен происходить за счёт:

- новых принципов группировки;
- точных игровых четвёрок;
- разных значений одних и тех же слов;
- ассоциативных и property-based групп;
- compound/phrase групп;
- bridge words;
- meta-цепей;
- аккуратного повторного использования контента по кампании.

Не добавляй редкие слова только ради достижения числового target.

## 2.2. Три разные сущности, которые нельзя смешивать

Обязательно раздели:

1. **Category concept** — канонический смысл или принцип группировки.
2. **Category variant** — конкретная игровая формулировка/версия этого принципа.
3. **Quartet variant** — конкретные четыре слова, которые игрок должен объединить.

Пример логики:

```text
canonical concept: BIRDS

category variants:
- COMMON BIRDS
- BIRDS OF PREY
- NON-FLYING BIRDS
- WATERFOWL
- BLACK-AND-WHITE BIRDS

quartet variants for BIRDS OF PREY:
- eagle, hawk, falcon, owl
- eagle, vulture, kestrel, osprey
```

Не создавай отдельный canonical concept только потому, что у одной идеи есть другой label. Для синонимов и близких формулировок используй alias/variant слой.

## 2.3. Категория уровня — не случайные четыре слова из большого пула

Точная игровая четвёрка является first-class content entity.

Большой membership pool полезен для поиска кандидатов, но production-уровень должен ссылаться на заранее сохранённый `quartet_variant`, а не делать случайный `sample(4)` из категории.

Каждая четвёрка должна хранить:

- category concept;
- category variant;
- четыре word/sense token;
- стабильный slot order;
- intended relation для каждого слова;
- difficulty tier;
- происхождение;
- rationale/короткое объяснение общей связи;
- validation status;
- local uniqueness result;
- risk policy result;
- reviewer fields;
- timestamps и версии валидаторов.

---

# 3. Целевая контентная ёмкость

Построй архитектуру и pipeline под следующие ориентиры:

```text
unique words:                       10 000–13 000
playable grouping principles:       3 000–4 000
level-ready quartet variants:       8 000–9 000
words with 2+ useful categories:    40–45%
human-reviewed golden quartets:     500–1 000
meta-chain templates:               several hundred
supported meta depth:               0–3
```

Под `playable grouping principles` понимаются category variants после дедупликации aliases, а не искусственно раздутый список разных написаний одного и того же названия.

Не маркируй автоматически сгенерированные 8–9 тысяч групп как `human_approved`. Разделяй минимум:

```text
ai_proposed
auto_validated
human_approved
human_rejected
needs_revision
blocked
```

Claude/LLM-generated контент никогда не получает `human_approved` автоматически.

Если за один проход невозможно качественно заполнить весь target, реализуй инфраструктуру, мигрируй текущие данные и создай максимально сильный первый batch. В итоговом отчёте честно раздели:

- фактически созданный контент;
- auto-validated candidates;
- human-review queue;
- оставшийся capacity gap.

---

# 4. Расширение модели категорий

## 4.1. Поддерживаемые типы группировки

Сохрани существующие relation types и добавь явную поддержку минимум следующих типов:

```text
is_a
part_of
found_in
has_property
does_action
used_for
used_by
associated_with
describes
characteristic_of
related_to_entity
same_phrase_pattern
compound_with
polysemy_bridge
category_as_word
pair_relation
ordered_set
```

Названия могут быть адаптированы к текущему стилю схемы, но семантики должны быть разделены.

## 4.2. Классы игровых category variants

Pipeline должен уметь работать со следующими классами:

### A. Таксономические

```text
DOG BREEDS
GEMSTONES
MUSICAL INSTRUMENTS
```

### B. Более узкие подкатегории

```text
NON-FLYING BIRDS
TROPICAL FRUITS
STRING INSTRUMENTS
```

### C. Property-based

```text
ROUND THINGS
THINGS THAT MELT
BLACK-AND-WHITE THINGS
```

### D. Functional/usage

```text
THINGS USED BY A DOCTOR
THINGS USED FOR BAKING
NAVIGATION TOOLS
```

### E. Entity-centric association hubs

```text
DRAGON → fire, scales, wings, claws
LIBRARY → shelf, book, librarian, silence
```

Это не строгая `is_a` таксономия, поэтому такие категории должны иметь отдельный relation type и более строгую quartet-level проверку согласованности.

### F. Phrase/compound groups

```text
___ BOARD
SNOW ___
WORDS AFTER FIRE
```

Для них нельзя притворяться, что это обычное lexical sense слова.

### G. Polysemy/bridge groups

Группы и цепи, где слово переходит между знакомыми значениями, например условное `key` как:

- ключ от замка;
- клавиша;
- тональность;
- ключевой элемент выражения.

### H. Pair/structured groups

```text
OPPOSITES
CAUSE AND EFFECT
COUNTRY AND CAPITAL
ANIMAL AND SOUND
```

Для таких категорий хранится внутренняя структура, а не общий неструктурированный пул.

## 4.3. Требования к category variant

Каждый auto-eligible category variant должен иметь:

- ясный скрытый label;
- чёткое правило inclusion/exclusion;
- relation type;
- target audience tier;
- понятность для среднего взрослого американского casual-игрока;
- минимум одну качественную четвёрку;
- отсутствие неограниченной субъективности;
- UI-safe display label либо отдельный short label;
- semantic review status;
- readiness status.

Субъективные, культурно чувствительные, парные или сильно контекстные категории должны становиться `curated_only`/`manual_only`, а не попадать в случайную автогенерацию.

---

# 5. Новая схема данных

Сначала изучи текущую схему и предложи минимально разрушительную миграцию. Названия таблиц можно адаптировать, но должны существовать эквивалентные сущности.

## 5.1. Category concepts и variants

Добавь или выдели:

```text
category_concepts
category_variants
category_aliases
```

Рекомендуемые поля:

### `category_concepts`

```text
id
canonical_key
canonical_name
concept_definition
topic
status
created_at
updated_at
```

### `category_variants`

```text
id
concept_id
variant_key
display_name
short_display_name
rule_text
relation_type
variant_class
base_difficulty
readiness
eligibility_tier
manual_only
active
created_at
updated_at
```

### `category_aliases`

```text
id
concept_id or variant_id
alias_text
alias_type
locale
canonicalization_status
```

Не потеряй текущие category IDs: создай mapping из старых categories в concepts/variants.

## 5.2. Words и senses

Развивай текущие `words` и `word_senses`.

На уровне sense должны поддерживаться:

```text
canonical_lemma
display_text
normalized_display_text
part_of_speech
sense_definition
is_proper_noun
is_trademark
familiarity_override
locale
capitalization_policy
```

Это нужно, чтобы правильно показывать, например:

```text
apple / Apple
march / March
turkey / Turkey
polish / Polish
```

Один общий display text на уровне `words` недостаточен.

## 5.3. Явный sense mode

`NULL sense_id` не должен одновременно означать:

- значение не применимо;
- значение забыли указать;
- используется только surface form;
- используется category label;
- используется compound phrase.

Добавь явный режим, например:

```text
sense_mode = lexical
sense_mode = surface_form
sense_mode = compound
sense_mode = category_label
```

Для `lexical` sense обязателен, если слово имеет заведённые senses.

## 5.4. Memberships

Сохрани раздельные оси и убери двусмысленность статусов.

Минимально нужны:

```text
semantic_status
familiarity_score
obviousness_score
gameplay_difficulty
eligibility_tier
risk_status
risk_flags
review_origin
reviewer
reviewed_at
```

Рекомендуемые значения `eligibility_tier`:

```text
normal
challenge
manual_only
candidate
blocked
```

Не используй слово `approved` одновременно в смысле:

- «семантически верно»;
- «первое значение слова»;
- «можно использовать в обычном уровне»;
- «проверено человеком».

Сохрани старое поле только для backward compatibility и явно пометь deprecated либо пересчитай его из новых осей.

## 5.5. Quartet variants

Развивай текущие `quartets` / `quartet_words` либо мигрируй их в более точную модель.

Минимальные поля:

```text
quartet_id
category_variant_id
difficulty_tier
validation_status
origin
rationale
local_quartet_unique
semantic_coherence_score
familiarity_profile
ambiguity_pressure
risk_status
human_review_status
reviewer
reviewed_at
validator_version
created_at
updated_at
```

`quartet_words`:

```text
quartet_id
slot
word_id
sense_id
sense_mode
intended_relation
role_in_structure
```

Обязательные constraints:

- ровно 4 строки на quartet;
- slot ровно 1..4 и уникален;
- нет одинакового display token внутри quartet;
- sense принадлежит word;
- все четыре token действительно проходят правило category variant;
- для structured quartet сохраняется роль пары/порядка.

## 5.6. Structured category data

Для pair/ordered групп добавь сущность вроде:

```text
category_structures
category_structure_items
```

или расширь `category_pair_groups`.

Поддержи минимум:

- пары;
- две полные пары в quartet;
- ordered sequences;
- key-value relations;
- parent-child relation.

OPPOSITES не должен собираться случайными четырьмя словами из общего пула.

## 5.7. Meta graph

Добавь:

```text
meta_edges
meta_chain_templates
meta_chain_nodes
```

`meta_edge` описывает, что после решения дочерней группы её category label становится игровым token родительской группы.

Минимальные поля:

```text
child_category_variant_id
parent_category_variant_id
produced_token_word_id or produced_token_text
produced_sense_id
edge_type
eligibility_tier
validation_status
```

Требования:

- meta graph уровня должен быть DAG;
- циклы запрещены;
- depth по умолчанию 0–3;
- label дочерней категории должен канонически совпадать с produced token;
- переход должен быть семантически понятен;
- одна и та же category label не должна неожиданно производить разные tokens без явного variant mapping.

## 5.8. Уровни

Добавь first-class модель уровня:

```text
level_instances
level_groups
level_dependencies
level_tokens
```

Рекомендуемые поля `level_instances`:

```text
id
level_key
level_type              # flat / meta
content_tier
status                  # candidate / auto_validated / human_approved / rejected
category_count
initial_token_count
max_meta_depth
difficulty_score
solution_count
solver_version
solver_checked_at
generation_run_id
created_at
updated_at
```

`level_groups` связывает уровень с конкретными quartet variants.

`level_dependencies` хранит unlock/meta зависимости.

`level_tokens` при необходимости фиксирует initial tokens, generated labels и их происхождение.

## 5.9. Usage history

Добавь:

```text
content_usage_history
campaign_positions
```

Нужно отслеживать минимум:

- последнее использование word/sense;
- последнее использование category concept;
- последнее использование category variant;
- последнее использование exact quartet;
- cumulative use count;
- use count по chapter/tier;
- контекст последнего использования.

## 5.10. Solver runs и generation runs

Развивай журнал:

```text
level_solver_runs
quartet_validation_runs
generation_runs
```

Храни:

- input hash;
- source commit;
- validator/solver version;
- parameters;
- random seed;
- duration;
- candidate counts;
- rejection reasons;
- result metrics;
- alternative solution summary;
- created_at.

`generation_runs` больше не должен оставаться пустым после фактической генерации.

---

# 6. Главный P0: solver полного уровня

Текущая локальная проверка quartet не гарантирует единственность полного уровня.

Раздели два понятия:

```text
local_quartet_unique
level_solution_count
```

## 6.1. Flat-level solver

После выбора всех групп уровня:

1. Собери полный multiset initial word/sense tokens.
2. Для каждой потенциальной category variant найди все допустимые четвёрки внутри этого набора.
3. Учитывай memberships, senses, sense_mode, structured rules, eligibility tier и policy filters.
4. Найди все exact-cover разбиения полного token set на группы по четыре.
5. Прекрати поиск после нахождения второго решения.
6. Принимай production candidate только при:

```text
solution_count == 1
```

7. Сохраняй альтернативное разбиение для диагностики rejected candidate.

Category conflicts с большим пересечением полезны как prefilter, но не являются заменой solver: неоднозначность может возникнуть при обмене одним или несколькими словами между группами.

## 6.2. Meta-level solver

Поддержи state-space solver для meta-уровней.

Состояние должно включать:

- доступные tokens;
- уже решённые groups;
- созданные category-label tokens;
- открытые dependencies;
- оставшиеся groups.

Переход:

```text
игрок решает допустимую текущую quartet
→ tokens quartet удаляются/помечаются решёнными
→ при наличии meta edge создаётся category-label token
→ становятся доступными зависимые группы
```

Solver должен считать не только разные финальные partitions, но и разные валидные семантические решения. Если две разные последовательности отличаются только порядком решения независимых, уже однозначных веток, это не обязательно два разных puzzle solutions. Документируй эквивалентность состояний и канонизируй их.

Принимай meta level только если:

- весь graph разрешим;
- нет deadlock;
- нет альтернативного семантического partition;
- все required labels производятся;
- ни один produced token не остаётся бесхозным;
- max depth соответствует tier;
- graph acyclic.

## 6.3. Производительность

- Используй inverted index `token → eligible categories`.
- Пересекай category membership с token set, а не перебирай всю базу.
- Кэшируй admissible groups для конкретного token-set hash.
- Прекращай поиск после двух решений.
- Добавь configurable time/node limits, но timeout никогда не должен считаться доказательством уникальности.
- Состояние `unknown/timeout` блокирует production use.

## 6.4. Regression tests

Добавь regression fixtures для уже известных классов ambiguity, минимум:

```text
MELTING THINGS ↔ YELLOW THINGS
ROUND THINGS ↔ TOYS
BEAUTY TOOLS ↔ CLEANING SUPPLIES
MELTING THINGS ↔ PIE INGREDIENTS
ROUND THINGS ↔ MAGIC PROPS
```

Тест должен подтверждать, что intended partition существует, но `solution_count >= 2`, поэтому кандидат отклоняется.

Также добавь positive fixtures с доказанно единственным решением.

---

# 7. Senses, display text и омонимия

## 7.1. Закрой известные sense-дефекты

Проверь и исправь минимум:

- четыре обычные связи `moon` должны использовать космическое значение;
- wordplay/surface-form связи должны иметь явный `sense_mode`, а не неразличимый NULL;
- action-категории не должны ссылаться на noun sense, если правило требует verb/action.

Проверь как минимум:

```text
drill
nail
bill
button
```

## 7.2. Разведи высокоуверенные омонимы

Проведи отдельный проход минимум по:

```text
bell
Charger
Jasmine
rose
siren
cricket
iris
Life
Spirit
```

Для каждого:

- создай missing senses;
- перенеси memberships на корректные senses;
- задай display text/capitalization на уровне sense;
- проверь все existing quartets и level candidates;
- инвалидируй и пересобери всё, где intended sense изменился.

## 7.3. Canonical display и spelling

Добавь нормализацию брендов, proper nouns и punctuation.

Проверь существующие проблемные формы вроде:

```text
Kit Kat
Reese's
Häagen-Dazs
Ben & Jerry's
O'Hare
St. Patrick's Day
Pac-Man
Rubik's Cube
McDonald's
F-150
Rust-Oleum
Peet's
Arby's
Elmer's
```

Не меняй surface text без mapping и diff отчёта.

## 7.4. Phrase tokens

Поддержи multi-word expressions как полноценные tokens, но добавь:

- normalized form;
- display length;
- short display override;
- UI safety status;
- tokenization policy;
- apostrophe/hyphen normalization.

---

# 8. Bridge words и meta-chain потенциал

Добавь вычисляемый `bridge_score` для word sense/token.

Он должен учитывать минимум:

- количество знакомых и реально различных senses;
- количество разных relation types;
- количество playable category variants;
- способность быть category label;
- наличие знакомых compounds/phrases;
- familiarity;
- semantic clarity;
- risk/trademark penalties;
- историю использования.

Не награждай слово только за большое количество почти одинаковых категорий.

Отдельно формируй кандидатов:

```text
high_value_bridge_words
meta_label_candidates
polysemy_chain_candidates
compound_chain_candidates
```

Bridge words должны чаще использоваться для meta content, но generator обязан соблюдать cooldown и не превращать несколько hub-слов в навязчивый повтор.

---

# 9. Content expansion pipeline

## 9.1. Не расширяй базу одним сырым LLM-дампом

Создай staged pipeline:

```text
propose
→ normalize
→ deduplicate
→ semantic validate
→ sense resolve
→ quartet build
→ local validate
→ level-solver validate
→ policy validate
→ review queue
→ human approval
```

Каждый шаг должен быть воспроизводимым и оставлять machine-readable причины reject.

## 9.2. Источники расширения category variants

Для существующих сильных canonical concepts создавай кандидатов следующих типов:

- более узкая подкатегория;
- общая observable property;
- типичное действие;
- функциональное назначение;
- место/контекст использования;
- entity-centric association hub;
- phrase/compound pattern;
- bridge/polysemy pattern;
- structured pair/sequence.

Не создавай бессмысленные variants только для достижения target.

## 9.3. Дедупликация

Реализуй поиск:

- одинаковых quartet sets под разными labels;
- почти одинаковых category rules;
- aliases;
- singular/plural duplicates;
- spelling/punctuation duplicates;
- concepts, различающихся только слишком общим label;
- nested concepts, ошибочно заведённых как aliases.

Результат должен классифицировать:

```text
exact_duplicate
alias
near_duplicate
parent_child
legitimate_distinct
needs_review
```

Не объединяй parent-child категории автоматически.

## 9.4. Генерация quartet variants

Для каждого category variant:

1. собери eligible membership pool;
2. разреши intended senses;
3. сформируй candidate quartets;
4. исключи rejected/candidate/risky tokens согласно tier policy;
5. оцени cohesion, familiarity и ambiguity pressure;
6. избегай четырёх чрезмерно похожих или четырёх чрезмерно редких слов;
7. предпочитай 1–2 anchor words и 2–3 supporting words для normal tier;
8. проверь local uniqueness;
9. сохрани как `ai_proposed` или `auto_validated`, не `human_approved`;
10. добавь в review pack rationale и competing categories.

Не сохраняй все математически возможные combinations. Выбирай ограниченный набор качественно различных quartet variants.

## 9.5. Hard content

Редкие слова и сложные связи не удаляй автоматически.

Для challenge/hard tier:

- label должен быть особенно чётким;
- должна быть минимум одна узнаваемая anchor card;
- четыре слова должны быть одного уровня абстракции;
- нельзя собирать группу из четырёх obscure items без дополнительного product approval;
- solver uniqueness обязательна так же, как для normal tier.

---

# 10. Human review и golden set

Создай review workflow, который позволяет человеку подтверждать:

- category concept;
- category variant;
- membership;
- sense assignment;
- exact quartet;
- meta edge;
- full level.

Минимальные поля:

```text
review_status
reviewer
reviewed_at
review_note
review_source
supersedes_decision_id
```

## Golden set

Подготовь review pack для первых 500–1 000 strongest quartets.

Требования к golden candidates:

- normal familiarity;
- низкий cultural/legal risk;
- ясный label;
- strong semantic cohesion;
- минимум ambiguity;
- корректные senses;
- UI-safe text;
- разные темы и relation types;
- пригодность для ранней и средней кампании.

Не проставляй human approval сам. Сформируй удобный CSV/Markdown/HTML review pack с полями accept/reject/edit.

Curated/manual categories либо получают вручную подтверждённые quartets, либо остаются blocked для production generation.

---

# 11. Кампания и cooldown

Добавь конфигурируемые scheduling rules.

Стартовые рекомендуемые значения:

```text
same word/sense cooldown:        15–30 levels
same category variant cooldown:  40–80 levels
same exact quartet cooldown:     100+ levels
same display token in one level: forbidden
same category label in one level: forbidden
```

Также контролируй:

- повтор canonical concept;
- повтор bridge word;
- повтор relation pattern;
- повтор темы;
- количество hard/rare tokens на уровень;
- распределение meta depth;
- использование exact quartet variants.

Cooldown должен быть конфигом, а не magic numbers в коде.

Если кампании ещё нет, создай sample campaign generator и usage history на sample data, чтобы правила были протестированы.

---

# 12. Difficulty model

Не оценивай сложность только по редкости слова.

Создай объяснимый heuristic difficulty model, включающий минимум:

```text
category_count
total_initial_tokens
number_of_meta_groups
max_meta_depth
number_of_parallel_chains
number_of_bridge_words
average_word_familiarity
rare_word_count
phrase_length pressure
sense ambiguity
pairwise category overlap
alternative partition pressure
number_of plausible first moves
structured-category complexity
```

Для каждого level candidate сохраняй:

- итоговый score;
- component scores;
- textual explanation;
- model version.

Не утверждай прогноз win rate без telemetry. Difficulty score — design heuristic до калибровки на игровых данных.

## Campaign templates

Поддержи минимум типы уровней:

```text
onboarding
recovery
standard
chain_heavy
ambiguity_heavy
knowledge_heavy
large_special
```

Ранние уровни должны быть конкретными и легко читаемыми. Сложность увеличивается в первую очередь через structure, controlled overlap, hidden depth и meta dependencies, а не через ранний obscure vocabulary.

---

# 13. Risk и policy workflow

Существующих `risk_flags` недостаточно. Добавь workflow:

```text
risk_status
risk_type
review_source
replacement_text
reviewer
reviewed_at
next_review_at
policy_version
```

Минимальные policy classes:

```text
safe
needs_review
sensitive
trademark
outdated_term
regional
obscure
blocked
```

Auto-level generator должен иметь явную policy по tier.

По умолчанию не допускай в normal auto levels:

- `semantic_status = disputed`;
- `risk_status = needs_review/sensitive/blocked`;
- unresolved trademark naming;
- unresolved sense;
- missing familiarity без manual override;
- UI-unsafe long token без short display.

---

# 14. Известные технические дефекты, которые нужно закрыть

Проверь текущий репозиторий и исправь, если ещё актуально:

1. Manual conflict `BUGS ↔ GARDEN BUGS`: stored overlap должен совпадать с фактическим.
2. Экспорт quartet words должен идти строго `ORDER BY quartet_words.slot`.
3. `generation_runs` должен заполняться.
4. `schema_meta` должен содержать версии/хеши SWOW, wordfreq и всех source-of-truth файлов.
5. Добавь DB-level constraints, где возможно:
   - unique slot в structured groups;
   - sense принадлежит word;
   - quartet slot 1..4;
   - уникальность quartet word/sense token;
   - допустимые enum-like values;
   - отсутствие self-conflicts;
   - валидность meta edge.
6. Исправь misleading `solver_state=unique`: локальная уникальность не должна называться уникальностью уровня.
7. Категории без quartets не могут считаться полностью production-ready.
8. `fit_score`, если остаётся константой seed, не должен использоваться как реальная semantic metric.

---

# 15. Source-of-truth файлы для новых сущностей

Предложи и реализуй читаемую структуру примерно такого уровня:

```text
data/content/category_concepts.jsonl
data/content/category_variants.jsonl
data/content/category_aliases.csv
data/content/memberships.csv
data/content/word_senses.jsonl
data/content/sense_map.csv
data/content/category_structures.jsonl
data/content/quartets_candidates.csv
data/content/quartets_reviewed.csv
data/content/meta_edges.csv
data/content/meta_chain_templates.jsonl
data/content/levels_candidates.jsonl
data/content/levels_reviewed.jsonl
data/content/risk_reviews.csv
data/content/usage_policy.yaml
data/content/generation_config.yaml
```

Не обязан использовать именно эти имена, если текущая архитектура предлагает более чистый вариант. Но все новые DB-данные должны быть воспроизводимы из текстовых источников.

Для large generated candidate files разрешён JSONL/CSV. Для human decisions используй diff-friendly CSV/JSON/YAML с устойчивым ordering.

---

# 16. CLI и pipeline

Добавь или расширь CLI-команды примерно такого назначения:

```text
migrate-schema
normalize-content
derive-category-variants
resolve-senses
build-quartet-candidates
validate-quartets
build-meta-candidates
validate-meta-graph
generate-level-candidates
solve-level
validate-levels
schedule-campaign
export-review-pack
check-integrity
stamp-version
```

Точные названия адаптируй к текущему CLI.

Каждая generate-команда должна поддерживать:

```text
--seed
--limit
--config
--output
--dry-run
--resume
```

Где это осмысленно.

Все команды должны выдавать summary counts и machine-readable report.

---

# 17. Integrity checks

Расширь `check-integrity`, чтобы он падал с ненулевым кодом минимум при следующих условиях.

## Database integrity

- SQLite integrity не `ok`;
- foreign key violations;
- orphan records;
- invalid enums;
- duplicate stable IDs/keys;
- source hash mismatch.

## Words/senses

- lexical membership без required sense;
- sense принадлежит другому word;
- proper-noun display policy нарушена;
- unresolved display collision;
- missing familiarity у auto-eligible token без manual override.

## Categories

- auto-eligible category без ясного rule;
- category без quartet, но readiness объявлен production-ready;
- duplicate/alias conflict без resolution;
- structured category без полной структуры;
- manual-only category попала в automatic pool.

## Quartets

- не ровно четыре slots;
- duplicate token;
- invalid membership;
- unresolved sense;
- blocked risk;
- invalid structured roles;
- nondeterministic order;
- ложный human approval;
- validator timeout помечен как pass.

## Meta graph

- cycle;
- missing produced label;
- orphan produced token;
- depth > configured maximum;
- invalid parent/child mapping;
- unresolved sense/category label collision.

## Levels

- `solution_count != 1` для production candidate;
- solver timeout/unknown;
- alternative partition найден;
- deadlock;
- duplicate display token;
- duplicate category label;
- cooldown violation в scheduled campaign;
- risky/disputed content нарушает policy;
- intended groups не покрывают весь token set.

## Reproducibility

- clean rebuild отличается от committed/exported snapshot;
- exports недетерминированы;
- generation run не записан;
- content/schema version отсутствуют.

---

# 18. Тесты

Добавь unit, integration и regression tests.

Минимальный набор:

## Unit

- normalization и aliases;
- sense ownership;
- category rule eligibility;
- quartet structure;
- pair/ordered structures;
- bridge score;
- cooldown calculation;
- difficulty components.

## Solver

- unique flat level;
- ambiguous flat level;
- ambiguity через swap одного слова;
- timeout не считается unique;
- unique meta chain;
- meta deadlock;
- meta cycle reject;
- независимые ветки не создают ложное второе semantic solution;
- альтернативный meta partition reject.

## Migration

- старые IDs сохраняются;
- current 3 005 quartets мигрируются без потери состава;
- slot order стабилен;
- старые CLI/read exports либо совместимы, либо имеют documented adapter.

## End-to-end

Из чистого checkout:

```text
build sources
→ init DB
→ import
→ derive/migrate
→ build quartets
→ generate sample levels
→ solve
→ check-integrity
→ export review pack
```

Всё должно выполняться одной документированной командой или Make/task target.

---

# 19. Порядок реализации

Работай фазами и делай отдельные commits по логическим блокам.

## Phase 0 — Repository audit и baseline

1. Найди project root и изучи текущую schema/pipeline/tests.
2. Зафиксируй baseline metrics.
3. Запусти существующий test suite и `check-integrity`.
4. Создай `docs/content_system_upgrade_plan.md` с mapping текущих сущностей в целевые.
5. Не меняй данные до фиксации baseline.

## Phase 1 — Correctness blockers

1. Реализуй full-level exact-cover solver.
2. Переименуй локальную uniqueness semantics.
3. Добавь regression ambiguity tests.
4. Исправь sense mode, известные homonyms, POS и display issues.
5. Исправь technical/export defects.
6. Усиль constraints и integrity checks.

После Phase 1 ни один production-level candidate не должен проходить без доказанного `solution_count = 1`.

## Phase 2 — Schema evolution

1. Добавь concepts/variants/aliases.
2. Развивай quartet model.
3. Добавь structured category data.
4. Добавь first-class level model.
5. Добавь meta graph.
6. Добавь usage history и solver runs.
7. Напиши migrations и backfill.

## Phase 3 — Content normalization

1. Дедуплицируй labels/concepts.
2. Нормализуй spelling/display/casing.
3. Пересобери senses.
4. Перекалибруй eligibility status semantics.
5. Сформируй manual-review queues.
6. Не удаляй disputed content без decision log.

## Phase 4 — Quartet expansion

1. Расширь category variants.
2. Сгенерируй качественные quartet candidates.
3. Валидируй local semantics, risk и ambiguity.
4. Не создавай все комбинации из больших pools.
5. Сформируй первый review-ready batch.
6. Покажи gap до target 8–9k.

## Phase 5 — Meta content

1. Найди bridge words.
2. Создай meta edge candidates.
3. Построй chain templates depth 1–3.
4. Проверь DAG и dynamic solver.
5. Сформируй sample meta levels.

## Phase 6 — Campaign scheduling

1. Реализуй cooldown config.
2. Добавь difficulty model.
3. Сгенерируй sample campaign.
4. Проверь повторы, topic balance и difficulty curve.

## Phase 7 — Export и handoff

1. Пересобери SQLite с нуля.
2. Запусти полный test/integrity suite.
3. Сгенерируй review pack.
4. Обнови README.
5. Создай migration/decision/metrics report.
6. Подготовь reproducible source bundle или укажи точный commit.

---

# 20. Обязательные артефакты результата

В репозитории должны появиться или обновиться:

```text
docs/content_system_architecture.md
docs/content_system_upgrade_plan.md
docs/content_decisions.md
docs/content_status_semantics.md
docs/solver_design.md
docs/content_generation_guide.md
docs/review_workflow.md
docs/migration_report.md
docs/final_validation_report.md
```

Также подготовь:

- schema migrations;
- source-of-truth files новых сущностей;
- updated SQLite snapshot;
- review pack;
- before/after metrics JSON/Markdown;
- ambiguity regression fixtures;
- sample flat levels;
- sample meta levels;
- sample scheduled campaign;
- manual-review CSVs;
- command log или reproducible task target.

---

# 21. Метрики before/after

В финальном отчёте покажи минимум:

```text
words
word senses
category concepts
category variants
aliases
memberships by eligibility tier
memberships by semantic status
quartets by validation status
quartets by difficulty tier
quartets with human approval
categories without quartets
structured categories
meta edges
meta templates by depth
level candidates generated
unique levels
ambiguous levels rejected
solver timeouts
risk-policy rejects
words in 2+ playable variants
usage/cooldown violations
```

Отдельно покажи:

- сколько текущих 3 005 quartets сохранилось;
- сколько стало invalid после более строгого solver/sense review;
- сколько новых quartet candidates создано;
- сколько реально level-ready;
- сколько ещё требуют human review;
- gap до product targets.

---

# 22. Definition of Done

Работа считается выполненной только если одновременно соблюдены следующие условия.

## Architecture

- Words, senses, category concepts, category variants и exact quartets разделены.
- Flat и meta levels имеют first-class representation.
- Source of truth остаётся текстовым и diff-friendly.

## Correctness

- Локальная quartet uniqueness не выдаётся за uniqueness уровня.
- Каждый production level имеет `solution_count = 1`.
- Solver timeout/unknown блокирует уровень.
- Все regression ambiguity fixtures отклоняются.
- Meta graph acyclic и полностью разрешим.

## Content integrity

- Auto content не помечается human-approved.
- Curated/manual categories не попадают в случайную генерацию.
- Senses/display/POS валидны.
- Risk policy применяется до добавления в production pool.
- Exact quartet имеет ровно четыре уникальных token.

## Reproducibility

- База полностью пересобирается из чистого checkout.
- `check-integrity` проходит.
- Все тесты проходят.
- Exports детерминированы.
- Versions, hashes и generation runs заполнены.

## Product readiness

- Есть review-ready golden-set queue.
- Есть sample flat и meta levels.
- Есть sample campaign с cooldown.
- Есть честный before/after report и список ручных решений.
- Нет утверждений, что AI-generated content проверен человеком.

---

# 23. Формат твоего финального ответа

После реализации дай отчёт в следующем порядке:

1. **Executive summary** — что изменилось и готова ли система к production use.
2. **Commits** — hash и назначение каждого коммита.
3. **Schema changes** — новые/изменённые таблицы и migrations.
4. **Pipeline changes** — новые команды и полный rebuild flow.
5. **Solver** — алгоритм, производительность, regression results.
6. **Content migration** — что сохранено, изменено, отклонено.
7. **Content expansion** — сколько concepts/variants/quartets добавлено.
8. **Meta system** — edges, templates, sample levels.
9. **Campaign scheduling** — cooldown и difficulty results.
10. **Tests and integrity** — точные команды и результаты.
11. **Before/after metrics** — таблица.
12. **Manual decisions remaining** — конкретный список.
13. **Known limitations** — честно, без маскировки.
14. **Files to hand off** — точные пути.

Не ограничивайся общими заявлениями вроде «добавлен solver» или «улучшена база». Приводи фактические counts, test names, paths, commands и примеры rejected ambiguity.

---

# 24. Главный принцип работы

Цель — не получить большой SQLite-файл и не максимизировать число слов.

Цель — получить **управляемую content system**, в которой:

```text
слово и его значение корректны
→ принцип группировки ясен
→ конкретная четвёрка качественна
→ полный уровень имеет единственное решение
→ meta dependencies разрешимы
→ повторы контролируются по кампании
→ каждый статус отражает реальную степень проверки
→ любой результат воспроизводим из source-of-truth
```

Сначала обеспечь доказуемую корректность и воспроизводимость. Затем наращивай объём контента.
