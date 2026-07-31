# Claude Code: upgrade базы слов и конвейера генерации уровней

## Назначение задания

Улучшить существующий `tool/word_content_pipeline`, чтобы он стал надёжным источником кандидатов для генератора уровней.

Система должна:

1. хранить слова, значения слов, принципы группировки и конкретные игровые четвёрки раздельно;
2. не выбирать случайные четыре слова из большого пула непосредственно в production-уровень;
3. собирать уровень из точных quartet variants;
4. проверять уникальность решения полного уровня через exact-cover solver;
5. сохранять причины автоматического принятия и отклонения;
6. передавать на ручную проверку уже собранный уровень, а не заставлять человека заранее подтверждать тысячи отдельных слов, связей и четвёрок;
7. полностью пересобираться из текстовых source-of-truth файлов.

Главный принцип:

```text
база данных = машинно проверенный пул кандидатов
генератор = сборка и автоматическая проверка уровня
ручная проверка = приёмка готового уровня целиком
```

---

# 1. Что нельзя сломать

Сохрани:

- текущие word IDs, category IDs и другие стабильные идентификаторы там, где это возможно;
- существующие seed-файлы и `review_decisions.csv` как источник исходных данных;
- SQLite как воспроизводимый snapshot, а не единственный источник правды;
- текущие значения `semantic_status`, `gameplay_difficulty`, `readiness` и другие уже внедрённые поля, если они имеют однозначную семантику;
- существующие CLI-команды либо документированный compatibility adapter;
- текущие 3 005 quartet records без потери состава при миграции, если они проходят новые constraints.

Перед изменениями:

1. найди project root;
2. изучи текущую schema, migrations, scripts, CLI и tests;
3. запусти baseline test suite и integrity checks;
4. сохрани baseline metrics;
5. составь mapping текущих полей и статусов в целевую модель;
6. не создавай параллельный второй словарь статусов без необходимости.

---

# 2. Что не входит в это задание

Не делай следующие вещи обязательным условием готовности базы:

- ручное подтверждение каждого слова;
- ручное подтверждение каждого membership;
- ручное подтверждение каждого category concept;
- ручное подтверждение каждой quartet variant;
- `human_approved` / `human_rejected` на словах, связях, категориях или четвёрках;
- golden set из 500–1 000 вручную проверенных четвёрок;
- огромные manual-review очереди для всей базы;
- заполнение 8–9 тысяч новых четвёрок любой ценой за один запуск;
- обязательная реализация meta-цепей и полной кампании, если они ещё не нужны текущей playable-версии.

LLM не должен выдавать свои кандидаты за подтверждённые человеком. Для этого достаточно хранить происхождение и результаты автоматических валидаторов, а не вводить human approval на каждом уровне данных.

---

# 3. Правильная точка ручной проверки

Ручная проверка происходит после генерации полного уровня.

Пайплайн:

```text
source content
→ machine validation
→ quartet candidate generation
→ level assembly
→ full-level solver
→ policy / UI / cooldown checks
→ level review package
→ человек принимает или отклоняет готовый уровень
→ принятый уровень фиксируется для кампании
```

Человек оценивает одновременно:

- понятность всех категорий;
- естественность конкретных четырёх слов;
- отсутствие спорной или натянутой связи;
- единственность решения;
- общее ощущение сложности;
- наличие доступного первого решения;
- качество meta-переходов, если они используются;
- длину и читаемость текста в UI;
- повторы относительно соседних уровней;
- культурные, юридические и продуктовые риски;
- соответствие уровню прогрессии.

Не требуется заранее просматривать каждую quartet variant отдельно.

## 3.1. Статус хранится на уровне

Для `level_instances` или экспортированного level artifact используй нейтральный workflow status:

```text
candidate
solver_valid
review_pending
accepted
rejected
needs_changes
```

Не называй его `human_approved`, если это создаёт ненужную семантическую нагрузку. Это статус жизненного цикла уровня.

Рекомендуемые поля:

```text
status
review_note
rejection_reason_codes
accepted_version
content_hash
updated_at
```

Поля `reviewer` и `reviewed_at` добавляй только если они реально нужны текущему рабочему процессу. Не делай их обязательными.

## 3.2. Feedback loop

Если уровень отклонён из-за конкретного элемента, система должна позволять зафиксировать причину на соответствующем объекте:

```text
bad_membership
bad_sense
weak_category_variant
weak_quartet
level_only_conflict
ui_text_problem
risk_problem
campaign_repeat
wrong_difficulty
```

Это не human approval всей сущности. Это точечный feedback, который предотвращает повторение одной и той же ошибки.

Для quartet можно хранить агрегированные сигналы:

```text
accepted_level_use_count
rejected_level_use_count
last_rejection_reason
is_disabled
```

Они могут вычисляться из истории уровней и не обязаны быть частью ручного source-of-truth.

## 3.3. Golden set

Не создавай отдельную цель `500–1000 human-approved quartets`.

Вместо этого:

- каждый принятый уровень может становиться regression fixture;
- набор принятых уровней постепенно образует `golden levels`;
- точные четвёрки внутри них считаются проверенными в данном level context, но не получают глобальный human-approved статус автоматически;
- начальный regression set может быть небольшим и расти вместе с фактической работой над кампанией.

---

# 4. Целевая модель контента

Раздели минимум следующие понятия.

## 4.1. Word

Каноническое написание или lexical entry.

## 4.2. Word sense

Конкретное значение слова.

На уровне sense должны поддерживаться:

```text
sense_key
definition
part_of_speech
display_text
normalized_text
is_proper_noun
familiarity_score
```

Регистр и display text должны зависеть от значения:

```text
apple / Apple
march / March
turkey / Turkey
polish / Polish
```

## 4.3. Category concept

Канонический семантический принцип группировки.

Пример:

```text
concept: birds_of_prey
```

## 4.4. Category variant

Игровая формулировка concept и конкретное правило допустимости.

Пример:

```text
BIRDS OF PREY
RAPTORS
PREDATORY BIRDS
```

Alias не должен автоматически становиться отдельным concept.

## 4.5. Membership

Потенциальная связь word/sense с category variant.

Используй существующие оси, не создавая дубли:

```text
semantic_status
eligibility_tier
gameplay_difficulty
confidence
risk_flags
validation_reasons
```

Целевая семантика:

```text
semantic_status: correct / disputed / incorrect / unreviewed
eligibility_tier: normal / hard / blocked
validation_state: valid / warning / invalid
origin: seed / imported / derived / ai_generated
```

Не добавляй `human_approved` к membership.

## 4.6. Quartet variant

Конкретные четыре word/sense token для конкретной category variant.

Обязательные поля:

```text
quartet_id
category_variant_id
slot 1..4
word_id
sense_id
sense_mode
intended_relation
difficulty_tier
origin
validation_state
cohesion_score
familiarity_score
ambiguity_pressure
risk_state
validator_version
created_at
updated_at
```

Обязательные constraints:

- ровно четыре token;
- уникальные slots 1..4;
- нет duplicate display token;
- sense принадлежит word;
- каждый token проходит правило variant;
- structured categories хранят роли пары или последовательности;
- deterministic export всегда идёт `ORDER BY slot`.

Статусы quartet:

```text
proposed
auto_validated
warning
invalid
disabled
```

Не используй `human_approved`.

## 4.7. Level instance

Уровень является first-class сущностью.

Минимум:

```text
level_instances
level_groups
level_tokens
level_dependencies        # только если используются meta/unlock связи
level_solver_runs
```

`level_groups` должен ссылаться на точные quartet variants.

Production-кандидат не должен делать случайный `sample(4)` из category pool во время игры.

---

# 5. Главный P0: solver полного уровня

Текущая локальная проверка четвёрки не гарантирует уникальность всего уровня.

Раздели:

```text
local_quartet_validation
level_solution_count
```

Не используй поле или формулировку `quartet is unique` как доказательство уникальности уровня.

## 5.1. Flat-level exact-cover solver

После выбора всех групп уровня:

1. собери полный multiset initial word/sense tokens;
2. найди все допустимые category/quartet interpretations внутри этого набора;
3. учитывай sense, sense_mode, relation type, structured rules, eligibility и policy filters;
4. найди exact-cover разбиения полного token set на группы по четыре;
5. останови поиск после второго решения;
6. принимай автоматический уровень только при:

```text
solution_count == 1
```

7. timeout, unknown или internal error никогда не считаются unique;
8. для rejected candidate сохраняй краткое alternative partition;
9. сохраняй solver version, input hash, parameters, duration и checked_at.

## 5.2. Обязательные regression cases

Добавь тесты минимум на:

- однозначный уровень;
- две полностью альтернативные группы;
- ambiguity через swap одного слова;
- ambiguity через swap нескольких слов;
- duplicate token;
- unresolved sense;
- timeout не считается успехом;
- blocked membership не участвует в решении;
- intended groups полностью покрывают token set.

## 5.3. Category conflicts

Предварительно вычисленные overlaps и `do_not_pair` полезны для ускорения генерации, но не заменяют exact-cover solver.

Неоднозначность может возникать даже при пересечении в одно слово.

---

# 6. Senses, POS и display normalization

Исправь оставшиеся случаи, где:

- слово многозначно, но membership не указывает intended sense;
- action category использует noun sense;
- proper noun и common noun имеют один display text;
- brand spelling неканоничен;
- `NULL sense_id` одновременно означает «пропущено» и «sense неприменим».

Введи явный `sense_mode`, минимум:

```text
lexical
surface_form
compound
phrase_pattern
```

`NULL sense_id` не должен скрывать пропущенное значение.

Проверь минимум известные high-value polysemy candidates:

```text
bell
rose
siren
cricket
iris
Life
Spirit
Charger
Jasmine
ring
moon
```

Проверь action-category sense assignments для слов вроде:

```text
drill
nail
bill
button
```

Не утверждай, что весь словарь семантически проверен человеком. Цель этого этапа — структурная корректность и машинно диагностируемые warnings.

---

# 7. Generation pipeline

Создай воспроизводимый staged pipeline:

```text
propose
→ normalize
→ deduplicate
→ resolve senses
→ validate memberships
→ build quartet candidates
→ validate quartet structure
→ assemble level candidate
→ full-level solver
→ policy / UI / cooldown validation
→ export level review package
```

Каждый reject должен иметь machine-readable reason code.

## 7.1. Не генерировать все комбинации

Для category pool из N слов не сохраняй все `C(N,4)` комбинации.

Выбирай ограниченный разнообразный набор quartet candidates по:

- semantic cohesion;
- familiarity;
- наличие 1–2 anchor words;
- разнообразие состава;
- controlled ambiguity;
- различие от уже существующих quartet;
- risk policy;
- пригодность к normal или hard tier.

## 7.2. Происхождение

Храни:

```text
origin
source_run_id
source_commit
input_hash
validator_version
random_seed
```

AI-generated означает только происхождение. Это не уровень качества и не approval status.

---

# 8. Concept / variant / alias deduplication

Реализуй поиск:

- exact duplicate labels;
- singular/plural duplicates;
- punctuation и spelling variants;
- aliases;
- почти одинаковых rules;
- identical quartet sets под разными labels;
- parent-child concepts, ошибочно сведённых в aliases.

Классификация:

```text
exact_duplicate
alias
near_duplicate
parent_child
legitimate_distinct
warning
```

Не объединяй `parent_child` автоматически.

---

# 9. Structured categories

Для категорий вроде противоположностей, пар и последовательностей нельзя выбирать случайные четыре слова из общего пула.

Поддержи:

```text
pairs
complete_two-pair quartet
ordered sequence
key-value relation
parent-child relation
```

Примеры правил:

- OPPOSITES = две полные пары;
- DAYS / MONTHS / SCALE = допустимая последовательность;
- COUNTRY–CAPITAL = две или четыре валидные пары согласно дизайну;
- BEFORE/AFTER PHRASES = явная роль каждого token.

Structured roles должны валидироваться и храниться в source-of-truth.

---

# 10. Level review package

После автоматической проверки экспортируй удобный пакет для оценки уровня.

Для каждого уровня покажи:

```text
level id
intended groups
category labels
four tokens per group
intended senses
relation types
difficulty score and components
solution_count
solver result
plausible competing memberships
word/category cooldowns
UI length warnings
risk warnings
generation seed and version
```

Также предоставь поля или команды:

```text
accept
reject
needs_changes
review_note
rejection_reason_codes
```

Решение применяется к level instance.

При необходимости отдельная причина может отключить конкретный quartet или membership, но это отдельное точечное действие.

---

# 11. Cooldown и usage history

Не делай полную кампанию обязательной частью первой итерации, но подготовь модель и конфиг.

Минимум отслеживай:

```text
last use of word/sense
last use of category concept
last use of category variant
last use of exact quartet
cumulative use count
```

Рекомендуемые стартовые defaults должны быть конфигом:

```text
same word/sense:        15–30 levels
same category variant:  40–80 levels
same exact quartet:     100+ levels
same display token in one level: forbidden
same category label in one level: forbidden
```

Для текущего задания достаточно:

- schema;
- config;
- validator;
- небольшого sample sequence для теста.

Не требуется генерировать финальную кампанию целиком.

---

# 12. Difficulty model

Сохрани объяснимую heuristic model.

Минимальные компоненты:

```text
category_count
total_tokens
average_word_familiarity
rare_word_count
sense_ambiguity
pairwise_category_overlap
alternative_partition_pressure
number_of_plausible_first_groups
structured_category_complexity
phrase_length_pressure
meta_depth                 # только если meta используется
```

Для каждого level candidate сохраняй:

```text
total_score
component_scores
model_version
short_explanation
```

Не называй это прогнозом win rate без telemetry.

---

# 13. Meta-цепи

Meta-цепи являются отдельной продуктовой возможностью, а не обязательным условием исправления базы.

Сначала проверь, поддерживает ли текущая playable-версия механику:

```text
решённая category label становится новым token
```

Если да:

- добавь `meta_edges`, `level_dependencies` и state-space solver;
- graph уровня должен быть DAG;
- cycles/deadlocks запрещены;
- timeout блокирует уровень;
- depth должен быть конфигом.

Если нет:

- не внедряй большой meta subsystem сейчас;
- оставь extension points и документированный schema proposal;
- не блокируй основной результат отсутствием meta implementation.

---

# 14. Source of truth

Не редактируй только SQLite snapshot.

Все изменения должны быть воспроизводимы из text-based files.

Сохрани текущие `data/seed/*` и добавляй новые сущности постепенно, без необязательной миграции всех файлов в другой каталог.

Допустимые новые файлы, если они нужны:

```text
data/content/category_concepts.jsonl
data/content/category_variants.jsonl
data/content/category_aliases.csv
data/content/quartet_variants.jsonl
data/content/structured_relations.jsonl
data/content/level_candidates.jsonl
data/content/level_decisions.csv
data/content/cooldown_config.yaml
```

`data/seed/*` и `data/content/*` могут сосуществовать:

- seed = исходные словари и membership pools;
- content = производные игровые сущности и решения генератора.

Все exports должны иметь стабильный ordering.

---

# 15. CLI

Добавь или адаптируй команды:

```text
baseline-report
migrate-content-schema
normalize-content
build-quartet-candidates
validate-quartets
generate-level-candidates
solve-level
validate-levels
export-level-review-pack
apply-level-decisions
check-integrity
rebuild-all
```

Поддержи там, где применимо:

```text
--db
--input
--output
--seed
--dry-run
--limit
--tier
--config
--explain
```

Все команды должны возвращать ненулевой exit code при блокирующей ошибке.

---

# 16. Integrity checks

`check-integrity` должен проверять минимум:

## Words / senses

- sense принадлежит word;
- required lexical sense не пропущен;
- display text валиден;
- normalization collision диагностирован.

## Categories / memberships

- variant ссылается на concept;
- alias не создаёт duplicate concept;
- blocked membership не попадает в normal generation;
- action relation не использует несовместимый POS без явного surface mode.

## Quartets

- ровно четыре slots;
- slots 1..4;
- нет duplicate token;
- membership и sense валидны;
- structured roles полны;
- export deterministic;
- disabled quartet не попадает в generation pool.

## Levels

- intended groups покрывают полный token set;
- `solution_count == 1` для solver-valid candidate;
- timeout/unknown не считается pass;
- duplicate display/category label запрещён;
- cooldown и policy violations диагностируются;
- accepted level имеет frozen content hash.

## Reproducibility

- clean rebuild совпадает со snapshot;
- generation run записан;
- versions и hashes заполнены;
- exports детерминированы.

---

# 17. Tests

Добавь unit, integration и regression tests.

Минимум:

## Unit

- normalization;
- sense ownership;
- alias resolution;
- quartet slots;
- structured pairs;
- cooldown calculation;
- difficulty components.

## Solver

- unique flat level;
- ambiguous flat level;
- one-word swap ambiguity;
- multi-word ambiguity;
- timeout != unique;
- blocked membership ignored;
- alternative partition saved.

## Migration

- stable IDs;
- текущие quartets не теряют состав;
- slot order стабилен;
- old exports совместимы либо адаптированы.

## End-to-end

Из чистого checkout:

```text
build seed sources
→ initialize DB
→ import/migrate
→ normalize
→ build quartet candidates
→ generate sample levels
→ solve
→ export review package
→ apply sample level decision
→ check-integrity
```

---

# 18. Порядок реализации

Работай отдельными логическими commits.

## Phase 0 — baseline

1. Repository audit.
2. Baseline metrics.
3. Existing tests/integrity.
4. Status mapping.
5. Migration plan.

## Phase 1 — correctness blockers

1. Full-level exact-cover solver.
2. Переименование misleading local uniqueness.
3. Regression ambiguity fixtures.
4. Sense/POS/display fixes.
5. Technical/export fixes.
6. Strong integrity checks.

Результат Phase 1:

```text
ни один solver-valid level candidate не проходит без solution_count == 1
```

## Phase 2 — minimal schema evolution

1. Concepts / variants / aliases.
2. Quartet variant model.
3. Structured category data.
4. First-class level model.
5. Solver/generation runs.
6. Migrations и backfill.

## Phase 3 — generator-to-review flow

1. Ограниченная генерация качественных quartet candidates.
2. Сборка sample level candidates.
3. Full automatic validation.
4. Export level review package.
5. Apply accept/reject/needs_changes decisions на уровне.
6. Feedback propagation для точечных дефектов.

## Phase 4 — optional extensions

Только после стабильного Phase 0–3:

- расширение каталога concepts/variants/quartets;
- campaign scheduler;
- cooldown tuning;
- meta chains;
- advanced difficulty curve;
- массовая генерация content batches.

Не начинай Phase 4, пока Phase 0–3 не имеют зелёных tests и воспроизводимого rebuild.

---

# 19. Обязательные артефакты

Не создавай девять документов ради количества.

Достаточно следующих актуальных файлов:

```text
docs/content_system_architecture.md
docs/solver_design.md
docs/status_semantics.md
docs/migration_and_validation_report.md
docs/level_review_flow.md
```

Также подготовь:

- migrations;
- updated source-of-truth files;
- updated SQLite snapshot;
- exact-cover regression fixtures;
- sample generated levels;
- level review package;
- before/after metrics;
- reproducible rebuild command;
- список известных ограничений.

---

# 20. Метрики before / after

Покажи минимум:

```text
words
word senses
category concepts
category variants
aliases
memberships by semantic status
memberships by eligibility tier
quartets proposed
quartets auto_validated
quartets warning/invalid/disabled
categories without usable quartets
level candidates generated
solver-valid levels
ambiguous levels rejected
solver timeouts
risk/policy rejects
accepted/rejected sample levels
rebuild hash
```

Не показывай метрики `human-approved quartets`, потому что такая стадия не является частью процесса.

Вместо неё покажи:

```text
quartets used in accepted levels
accepted level count
rejection reasons by type
repeated defect prevention count
```

---

# 21. Definition of Done

Работа считается завершённой для текущей итерации, если:

## Architecture

- word, sense, concept, variant, quartet и level разделены;
- source of truth остаётся текстовым;
- SQLite пересобирается;
- нет дублирующего набора статусов.

## Correctness

- local quartet validation не выдаётся за level uniqueness;
- exact-cover solver проверяет полный уровень;
- `solution_count == 1` обязателен для `solver_valid`;
- timeout/unknown блокируют уровень;
- ambiguity regression tests проходят.

## Content

- quartet состоит ровно из четырёх валидных token;
- senses/POS/display обрабатываются явно;
- origin и machine validation отделены от качества финального уровня;
- manual approval отсутствует на базовых сущностях.

## Workflow

- генератор создаёт sample levels;
- каждый sample level получает автоматический отчёт;
- review package позволяет принять или отклонить уровень целиком;
- решение уровня можно воспроизводимо применить;
- точечный дефект можно вернуть в базу как block/fix signal.

## Reproducibility

- clean rebuild проходит;
- tests и integrity checks зелёные;
- exports стабильны;
- versions, hashes и generation runs заполнены.

---

# 22. Формат финального отчёта Claude Code

После реализации дай:

1. Executive summary.
2. Commits и назначение каждого.
3. Baseline before/after.
4. Schema/migrations.
5. Status mapping и почему нет параллельного словаря.
6. Exact-cover solver design и результаты regression tests.
7. Sense/POS/display исправления.
8. Quartet migration/generation results.
9. Sample level generation results.
10. Level review flow.
11. Rebuild/test/integrity commands и outputs.
12. Known limitations.
13. Что оставлено в optional Phase 4.
14. Точные пути файлов для передачи.

Не ограничивайся словами «готово» или «улучшено». Приводи counts, paths, test names, rejected ambiguity examples и команды воспроизведения.

---

# Команда на запуск

Прочитай этот файл полностью и выполни Phase 0–3.

Сначала зафиксируй baseline и mapping существующих статусов. Затем реализуй full-level solver, минимальную целевую schema и generator-to-level-review flow.

Не внедряй human approval на словах, memberships, категориях и quartets. Ручная оценка проводится на готовом уровне. Не создавай golden set из вручную подтверждённых четвёрок.

Не редактируй SQLite вручную. Все изменения должны идти через source-of-truth, migrations и воспроизводимый pipeline.

Meta chains, массовое расширение до целевых объёмов и полную кампанию оставь в optional Phase 4, если они не требуются уже существующей playable-версией.
