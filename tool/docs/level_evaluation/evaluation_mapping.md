# Mapping: требования D/F/R/C на существующий код

Phase 0 задания `prompts/level-difficulty-fun-pack/CLAUDE_CODE_APPLY_UNIFIED_LEVEL_EVALUATION.md`.
Состояние «до» зафиксировано в `evaluation_baseline.md`.

Правило, по которому принимались все решения ниже, — то же, что уже применялось
в `word_content_pipeline/docs/scoring_mapping.md`:

> **Если величина уже считается, она переиспользуется под своим именем.**
> Новое поле заводится только там, где такой величины не было, и только если
> оно отвечает на вопрос, на который не отвечает ни одно существующее.

И второе правило, из `word_content_pipeline/docs/status_semantics.md`:

> **Второй словарь статусов не заводится.** Целевые статусы задания уже
> существуют — проецируем, а не дублируем.

## 0. Где что будет реализовано

Целевая модель — один слой, но проект состоит из двух систем (см. baseline).
Разделение ответственности, без переписывания ни одной из них:

```text
tool/level-tool/           ГЛАВНОЕ МЕСТО РЕАЛИЗАЦИИ D/F/R/C
                           здесь уже живёт D и I, здесь генератор, валидатор
                           и счётчик решений, здесь UI для человека,
                           это задеплоенный инструмент

tool/word_content_pipeline/ остаётся источником ПАРАМЕТРОВ §1.1
                           (familiarity, ambiguity, label quality, quartet scores)
                           и владельцем review-workflow в базе;
                           его difficulty.py становится импортёром оценки,
                           а не второй моделью

levels/EVAL.md             становится explainability layer (§13 задания):
                           human-readable объяснение, не источник расчёта
```

Причина: задание §29 требует работающий код и UI для человека, а не второй
пайплайн. Дублировать D/F/R/C в обеих системах — гарантированно получить два
несовпадающих числа на одном уровне, что уже случилось с D (baseline, дубль №1).

## 1. Три модели D сводятся в одну

Это единственное дублирование, которое **обязано** исчезнуть, иначе новый слой
станет четвёртым D.

| Реализация | Что с ней делаем |
|---|---|
| `level-tool/web/src/core/scoringDifficulty.ts` | **становится единственной моделью D.** Её три секции (base / declared / semantic / mechanical) переразмечаются в шесть компонентов §5 задания — переразметка, а не переписывание, см. таблицу ниже |
| `pipeline/src/word_content/difficulty.py` | **не удаляется и не развивается.** Остаётся as-is для сборки кандидатов внутри базы (быстрая эвристика отбора). Помечается в docstring как pre-scoring эвристика, чьё число не является D уровня |
| `levels/EVAL.md` (F1-F7) | остаётся как §13 Practical V1 — объяснение для человека. Таблица факторов уже совпадает с компонентами по смыслу |

Калиброванные веса `d-1.0-calibrated` **сохраняются**: 199 референсных уровней —
единственная реальная калибровка в проекте, терять её нельзя. Новая модель
надстраивается так, чтобы при пустых новых компонентах давала прежнее число
(регрессия на четырёх эталонах — обязательное условие Phase 1).

## 2. Difficulty: шесть компонентов §5 на существующий код

Целевая формула требует шесть компонентов в шкале `0..100`. Текущий код считает
слагаемые прямо в шкале 1-10. Мапится так:

| Компонент §5 | Вес | Что уже есть | Что добавляется |
|---|---|---|---|
| `semantic_difficulty` | 0.25 | `base.'редкие слова'`, `base.'очень редкие'`; `words.familiarity_score`; `memberships.obviousness_score` | агрегаты `min`/`p25`/`unknown_count` и `weakest_membership_penalty` — §6 прямо запрещает считать только среднее |
| `ambiguity_pressure` | 0.25 | `semantic.'подтверждённые ловушки'`, `semantic.'смежность категорий'`, `semantic.'незапланированная спорность'`; `Trap.decoyFit` / `decoyObviousness` | `trap_strength` (weak/medium/strong), `alternative_fit_gap`, **правило дедупликации** ловушка↔near-pair↔unplanned (сейчас отсутствует, baseline дубль №4) |
| `structural_difficulty` | 0.25 | почти ничего: `board.boardCapacity`, проверка `VISIBLE_SHARE`, `level_dependencies` в базе | весь §8: зоны, фрагментация, completion opportunity, branching, partial hypotheses. **Самый большой объём Phase 2** |
| `content_load` | 0.10 | `base.start_bubbles` (объём), `categories.length` | saturating normalization вместо линейной; `relation_type_variety` (данные есть в `memberships.relation_type`) |
| `constraint_pressure` | 0.10 | **есть целиком:** `mechanical.'теснота лимита ходов'`, `board.moveLimitK`, `MIN/MAX_MOVE_LIMIT_K` | шкала K из §10 (`>=1.60 spacious` … `<1.10 high frustration`) — сейчас линейная интерполяция без порогов |
| `mechanic_cognitive_load` | 0.05 | `mechanical.'цепи'`, `mechanical.'половинки'`; типы `Chain`, `HalfSplit`, `Modifier` | `mechanic_catalog` + `mechanic_usage_history`, `effective_mechanic_load = raw × unfamiliarity` |

**Куда девается секция `declared`.** Мета-связи, глубина мета и quickwin-relief
не имеют аналога в шести компонентах §5. Решение: `meta_link` и `meta_depth`
уходят в `structural_difficulty` (мета-лес — это и есть зависимость и
фрагментация поля), `quickwin_relief` уходит в `completion_opportunity`
(быстрая победа = ранняя возможность завершить категорию). Пометка «объявлено,
не откалибровано» **сохраняется**: это честная граница, и §2.7 задания требует
не выдавать эвристику за истину.

## 3. Fun: `I` переименовывается в `F`, композиты остаются

Целевая модель просит восемь компонентов. Четыре композита `scoringInterest.ts`
покрывают их так:

| Компонент §12 | Что уже есть |
|---|---|
| `recognizability` | `clarity` (доля слов выше `topFrequencyThreshold` + средняя `obviousness`) |
| `semantic_aha` | `aha` (честные ловушки: `decoyFit >= 0.6 && decoyObviousness <= 0.55`) |
| `mechanic_novelty` | нет — новое, зависит от `mechanic_catalog` |
| `anticipation_and_payoff` | частично `aha` (мета-payoff: `metaLinks`, `metaDepth >= 2`) |
| `content_variety_and_theme` | `variety` (типы связи + тематические сферы + штраф за однотипность) |
| `tempo` | нет как компонента; в `EVAL.md` есть якорь «стартовая категория». Данные есть: `LevelCategory.isQuickwin` |
| `staleness_penalty` | `freshness` — сейчас положительный композит, станет штрафом |
| `unfairness_penalty` | нет — новое, приходит из `R` и Fairness Gate |

**Имя.** Ось называется `F` (Fun), как в целевой модели и в `levels/EVAL.md`.
`InterestBreakdown` и `i-0.1-uncalibrated` переименовываются — третьего имени
для одной оси не заводим. Это переименование, а не новое поле.

**Hard gate §15** уже частично есть: при `solutions.count >= 2` код ставит
`clarity = 0`. Требование задания жёстче — `F <= 3.0` и
`review_status = needs_changes | rejected`. Дожимается в Phase 1.

## 4. `R` и `C` — целиком новые, дублей нет

Ни одного существующего поля с этим смыслом в проекте нет. Заводятся с нуля.

**`R` (Frustration Risk).** Семь компонентов §15 опираются на уже существующие
данные — новых источников не требуется, требуется новая агрегация:

| Компонент | Источник данных |
|---|---|
| `unfair_ambiguity` | `SolutionCount.count`, `secondSolutionExample`, blind-прогон |
| `weakest_membership_problem` | `memberships.obviousness_score` (минимум по уровню) |
| `unknown_word_pressure` | `words.familiarity_score IS NULL`, `SnapshotWord.u = 1` |
| `low_progress_visibility` | `isQuickwin`, completion opportunity (Phase 2) |
| `excessive_fragmentation` | `category_fragmentation_score` (Phase 2) |
| `rule_opacity` | `categories.rule`, `label_clarity_score` |
| `mechanic_overload` | `mechanic_catalog` (Phase 5) |

Косвенные предшественники, которые **переиспользуются, а не дублируются**:
`memberships.risk_flags`, `quartets.risk_state`, `risk_warnings` review pack.
Они становятся входом в `R`, а не второй шкалой риска.

**`C` (Confidence).** Пять компонентов §16. Ключевое требование — не среднее
арифметическое, а консервативная агрегация: один нулевой критический компонент
обнуляет уверенность. Источники:

| Компонент | Источник |
|---|---|
| `data_completeness` | `words_without_familiarity`, `SnapshotWord.u`, отсутствие `sense_id` у многозначного слова |
| `metric_reliability` | `calibrated: true/false` в конфиге; `d-1.0-calibrated` vs `i-0.1-uncalibrated` |
| `solver_certainty` | `SolutionCount.exhausted` — **уже есть и ровно про это**: перебор исчерпан или обрезан по лимиту |
| `blind_evaluation_consistency` | расхождение двух blind-прогонов (§17) |
| `model_calibration_quality` | выход признаков за калиброванный диапазон (`reference_D_distribution` в конфиге) |

`SolutionCount.exhausted` — хороший пример того, зачем нужен этот mapping:
поле уже год лежит в коде и означает именно `solver_certainty`. Заводить рядом
новое было бы ошибкой.

## 5. Fairness Gate: третье значение к существующим двум

Сейчас: `ValidationResult.passed: boolean` + `Severity = 'hard' | 'soft'` на
каждой проверке. Целевая модель: `PASS / WARNING / FAIL`.

**Дубля не заводим.** Три значения выводятся из уже существующей разметки:

```text
FAIL     есть непройденная проверка severity 'hard'
WARNING  все hard пройдены, есть непройденная 'soft'
PASS     непройденных проверок нет
```

То есть `Fairness Gate` — производная от `ValidationResult`, а не второй
результат валидации. `passed` остаётся как есть (`FAIL` ⇔ `!passed`).

Список gates §4 задания против существующих проверок:

| Требование §4 | Существующая проверка | Состояние |
|---|---|---|
| `all categories contain exactly 4 required elements` | `CATEGORY_SIZE` (hard) | есть |
| `no duplicate display token inside level` | `WORD_OCCURRENCE` (hard) | есть |
| `all required senses resolved` | `memberships.sense_mode` + `validation_state` в базе | есть в pipeline, нет проверки в level-tool |
| `all words renderable` | `MAX_DISPLAY_LENGTH` / `MAX_LABEL_LENGTH` в review pack | есть как warning, не как gate |
| `no blocked content` | `APPROVED_CONTENT_ONLY` (hard) | есть |
| `layout graph valid` | `META_FOREST_ACYCLIC`, `META_PARENT_COUNT`, `START_BUBBLE_COUNT` (hard) | есть |
| `mechanic state transitions valid` | `CHAIN_ACYCLIC`, `HALF_COLLISION` (hard) | есть |
| `solver completed successfully` + `solution_count == 1` | `GLOBAL_SOLUTION_COUNT` (hard) | есть |
| `критически слабая необъяснимая связь` → FAIL | `ASSIGNED_HOME` (hard), `UNSEPARABLE_PAIR` (soft) | частично |
| `неизвестная familiarity` → WARNING | `RECOGNIZABILITY` (hard, порог 90%) | есть, но hard, а не warning |
| `слабый label` → WARNING | `label_quality_score` в базе | есть значение, нет проверки |
| `слишком длинное слово` → WARNING | `WORD_FORM_GATE` (hard, если заданы `decadeGates`) | есть |
| `низкая confidence` → WARNING | — | новое, зависит от `C` |
| `новая непроверенная механика` → WARNING | — | новое, Phase 5 |
| `повышенный frustration risk` → WARNING | — | новое, зависит от `R` |

Восемь из девяти обязательных gates §4 **уже существуют** как hard-проверки.
Добавляется четыре WARNING-проверки и единая точка входа перед scoring.

## 6. Статусы уровня: дублей не заводим

Задание §18 требует шесть статусов. Все шесть **уже есть** в
`level_instances.status` (`docs/status_semantics.md` §8):

| §18 задания | В базе | Решение |
|---|---|---|
| `candidate` | `candidate` | совпадает |
| `solver_valid` | `solver_valid` | совпадает |
| `review_pending` | `review_pending` | совпадает |
| `accepted` | `accepted` | совпадает |
| `needs_changes` | `needs_changes` | совпадает |
| `rejected` | `rejected` | совпадает |

Один в один. **Новых статусов не добавляется, существующие не переименовываются.**

Reason codes §18 — тоже есть: девять кодов в `level_review.REASON_TARGETS`,
из них `wrong_difficulty` покрывает расхождение `D_auto` и `D_human`.
Добавляется недостающее: `unfair_ambiguity` и `frustration` как отдельные коды,
поскольку `level_only_conflict` их не различает.

Поля `D_human / F_human / R_human` §18 — новые. Сейчас есть только `review_note`
(текст) и `accepted_version`. Числовой человеческой оценки нет.

**`human_approved` на словах, связях, категориях и четвёрках не появляется.**
Запрет §1.1 задания совпадает с уже принятым решением проекта
(`status_semantics.md`) — ничего менять не нужно.

## 7. Параметры §1.1: что база уже даёт

Проверено по фактическим колонкам `content.sqlite` (schema_version 5).

### Word / display form

| §1.1 | В базе | Состояние |
|---|---|---|
| `familiarity_score` | `words.familiarity_score` | есть |
| `char_count` | `word_scores.char_count` | есть |
| `token_count` | `word_scores.token_count` | есть |
| `display_width_score` | `word_scores.display_width_score` | есть |
| `spelling_difficulty_score` | `word_scores.spelling_difficulty_score` | есть |
| `ambiguity_score` | `word_scores.ambiguity_score` | есть |
| `novelty_score` | `word_scores.novelty_score` | есть |
| `accessibility_score` | `word_scores.accessibility_score` | есть |

**Восемь из восьми.** Ничего добавлять не нужно.

### Category variant / label

| §1.1 | В базе | Состояние |
|---|---|---|
| `label_familiarity_score` | `category_label_scores.label_familiarity_score` | есть |
| `label_clarity_score` | `…label_clarity_score` | есть |
| `label_naturalness_score` | `…label_naturalness_score` | есть |
| `label_specificity_score` | `…label_specificity_score` | есть |
| `label_quality_score` | `…label_quality_score` | есть |
| `relation_type` | `categories.relation_type` | есть |
| `base_difficulty` | `categories.base_difficulty` → снимок `SnapshotCategory.d` | есть |

**Семь из семи.**

### Membership

| §1.1 | В базе | Состояние |
|---|---|---|
| `semantic_fit_score` | `memberships.fit_score` | есть, имя оставляем |
| `membership_obviousness_score` | `memberships.obviousness_score` | есть, имя оставляем |
| `sense_confidence` | — | **новое.** Косвенно: `sense_mode` + `validation_state`, но числа уверенности нет |
| `alternative_fit_score` | — | **новое.** Считается из `fit_score` связи с другой категорией уровня; отдельной колонки не нужно, это агрегат уровня |
| `trap_potential_score` | `gameplay_difficulty` + `review_status = 'alternative'` | частично: материал ловушек размечен, числа силы нет |

### Quartet

| §1.1 | В базе | Состояние |
|---|---|---|
| `avg_word_familiarity` | `quartets.familiarity_score` | есть, имя оставлено |
| `min_word_familiarity` | `quartets.min_word_familiarity` | есть |
| `semantic_cohesion_score` | `quartets.cohesion_score` | есть, имя оставлено |
| `quartet_clarity_score` | `quartets.quartet_clarity_score` | есть |
| `quartet_interest_score` | `quartets.quartet_interest_score` | есть |
| `quartet_ambiguity_score` | `quartets.ambiguity_pressure` | есть, имя оставлено |
| `quartet_quality_score` | `quartets.quartet_quality_score` | есть |

**Семь из семи.**

Вывод: **из 27 параметров §1.1 в базе уже есть 24.** Работа Phase 1-4 — не
наполнение базы, а расчёт уровневых агрегатов поверх неё. Это ровно то, ради
чего задание требует mapping до кода.

## 8. Целевые сущности §3 на существующие

| §3 задания | Что есть | Решение |
|---|---|---|
| `words` / `word_senses` | `words`, `word_senses` | совпадает |
| `category_concepts` | `category_concepts` | совпадает |
| `category_variants` | `categories` (+ `category_aliases`) | переиспользуем: варианта как отдельной сущности в проекте нет, `categories` играет обе роли |
| `memberships` | `memberships` | совпадает |
| `quartet_variants` | `quartets` (+ `quartet_words`) | переиспользуем |
| `level_instances` | `level_instances` | совпадает |
| `level_categories` | `level_groups` | переиспользуем, **не переименовываем** |
| `level_items` | `level_tokens` | переиспользуем |
| `level_layout` | `level_dependencies` (частично) | расширяется в Phase 2: зон и графа поля нет |
| `level_mechanics` | — | **новое**, Phase 5 |
| `level_solver_runs` | `level_solver_runs` | совпадает |
| `level_structure_metrics` | — | **новое**, Phase 2 |
| `level_blind_evaluations` | файлы `levels/solver/*.blind.json` | формализуется, Phase 3 |
| `level_scores` | `level_instances.difficulty_*` (3 колонки) | **расширяется**: сейчас только D. Выносится в отдельную сущность, чтобы хранить D/F/R/C + компоненты + версии + snapshot |
| `level_reviews` | `level_decisions` | переиспользуем |
| `level_review_reasons` | `level_decision_reasons` | переиспользуем |
| `mechanic_catalog` | — | **новое**, Phase 5 |
| `mechanic_usage_history` | `cooldown.py` (слова и категории) | расширяется на механики, Phase 5 |
| `scoring_model_versions` | `scoring.config.json`, `scoring_config.yaml`, `schema_meta` | переиспользуем + реестр версий инструмента (§10 ниже) |
| `generation_profiles` | `data/content/generation_profiles.yaml` (3 профиля) | переиспользуем, добавляются профили §20 |

**Ни одна таблица не переименовывается.** Новых сущностей ровно четыре:
`level_mechanics`, `level_structure_metrics`, `mechanic_catalog`, и
формализованный `level_blind_evaluations`.

Принцип «JSON/JSONL как source of truth, SQLite — пересобираемый snapshot»
(§3 задания) в проекте уже действует и сохраняется.

## 9. CLI: имена команд

Задание §21 предлагает префикс `level-content`. В проекте CLI называется
`word-content` (`pyproject.toml → project.scripts`). **Второй CLI не заводим**,
имена команд проецируются:

| §21 задания | В проекте | Состояние |
|---|---|---|
| `validate-level` | `validate-levels` | есть |
| `solve-level` | `solve-level` | есть |
| `simulate-level` | — | новая, Phase 2 |
| `score-level` | — | новая, Phase 1 (сейчас D считается внутри `generate-level-candidates`) |
| `blind-evaluate` | `scripts/solver_input.ts` + промпт | формализуется, Phase 3 |
| `export-review-pack` | `export-level-review-pack` | есть |
| `review-level` | `apply-level-decisions` | есть |
| `recalibrate-model` | `scripts/calibrate_difficulty.py` | есть, обобщается |
| `compare-model-versions` | — | новая, Phase 6 |

Обязательные параметры §21 (`--seed`, `--dry-run`, `--config`, `--model-version`,
`--output`) частично есть: `--seed` и `--output` используются, `--dry-run` есть
у части команд. Приводится к общему виду в Phase 1.

## 10. Версионирование инструмента

Задание §22 требует восемь независимых версий. Сопоставление с фактическим
состоянием (baseline) и решение:

| §22 задания | Сейчас | Решение |
|---|---|---|
| `difficulty_model_version` | `d-1.0-calibrated` | есть |
| `fun_model_version` | `i-0.1-uncalibrated` | есть, переименовывается в `f-…` вместе с осью |
| `frustration_model_version` | — | новая, Phase 1 |
| `confidence_model_version` | — | новая, Phase 1 |
| `solver_version` | **в level-tool нет**, в pipeline `level_solver_runs.solver_version` | добавляется константа в level-tool |
| `structure_simulator_version` | — | новая, Phase 2 |
| `blind_evaluator_version` | — | новая, Phase 3 |
| `generation_profile_version` | `generation_profiles.yaml` | есть, версия файла не выделена |

Плюс то, чего задание не просит, но чего требовал пользователь отдельно:
**версия самого инструмента**. Заведена как `TOOL_VERSION` в
`web/src/core/version.ts` с журналом в `tool/level-tool/CHANGELOG.md`.

Правила, зафиксированные в Phase 0 (реализация — `version.ts`):

1. `TOOL_VERSION` — единственный номер релиза инструмента, semver.
2. Версии моделей независимы от `TOOL_VERSION` и меняются отдельно: правка веса
   в `scoring.config.json` поднимает `difficulty_model_version`, но не версию
   инструмента, и наоборот.
3. **`TOOL_VERSION` не входит в `levelSpecHash`.** В хеш входят только
   `generator_version`, `seed`, нормализованный конфиг и хеш снимка
   (`hashing.ts`). Иначе релиз инструмента ломал бы обещание
   «тот же вход → тот же уровень» и обнулял бы регрессию по пакетам.
4. `GENERATOR_VERSION` меняется только при изменении алгоритма сборки —
   это единственная версия, которая обязана менять хеш.
5. У принятого уровня версии сохраняются снимком (§22): пересчёт по новой
   формуле не имеет права переписать историческую оценку. Реализация — Phase 4.

## 11. Что этой работой сознательно НЕ делается

Прямо из §2 задания, плюс решения этого mapping:

1. **Единый непрозрачный `level_quality_score` не заводится.** D, F, R, C
   остаются четырьмя разными числами. Существующий `quartet_quality_score` —
   про четвёрку, а не про уровень, и на роль общего рейтинга не повышается.
2. **Exact solver не заменяется AI.** `countSolutions()` и `solve-level`
   остаются доказательством; blind AI — диагностика.
3. **`difficulty.py` не удаляется и не становится второй моделью D.**
4. **Существующие имена колонок не меняются** (`cohesion_score`,
   `familiarity_score`, `ambiguity_pressure`, `fit_score`,
   `obviousness_score`, `level_groups`, `level_tokens`).
5. **Второго словаря статусов и второго CLI не появляется.**
6. **`human_approved` не появляется ни на одном элементе базы.**
7. **Production-данные Phase 0 не изменены**: ни одной записи в
   `content.sqlite`, ни одного файла в `levels/`.
8. **Текущая основная задача не остановлена.** Приёмка пяти кандидатов идёт
   своим порядком; новый слой к ней не привязан и её артефакты не переписывает.

## 12. Порядок работ и предусловия

| Phase | Содержание | Предусловие |
|---|---|---|
| 0 | этот документ + baseline + реестр версий | — (**выполнено**) |
| 1 | gates → `PASS/WARNING/FAIL`, D/F/R/C + компоненты, version fields, unit tests | — |
| 2 | structural metrics §8, confidence penalty за approximation | Phase 1 |
| 3 | blind export + схема ответа + валидация | Phase 1 |
| 4 | review pack §19, `D_human/F_human/R_human`, accepted → regression fixture | Phase 1-3 |
| 5 | интеграция генератора, профили §20, mechanic freshness | **только после того, как тесты базовой модели проходят** |
| 6 | калибровка, before/after report | приёмка уровней генератора |

Ограничение по Phase 6: приёмка базы отменена решением продакта (31.07),
принятых уровней ноль и не появится оттуда. Calibration dataset собирается из
четырёх существующих эталонов (`levels/etalon/e1-e3`, `levels/demo/journey-d7`)
с их целевыми D — человеческие F и R для них ещё не выставлены — и далее из
приёмки уровней, собранных генератором.
