# Baseline перед внедрением D/F/R/C

Phase 0 задания `prompts/level-difficulty-fun-pack/CLAUDE_CODE_APPLY_UNIFIED_LEVEL_EVALUATION.md`.
Продуктовая модель: `prompts/level-difficulty-fun-pack/UNIFIED_LEVEL_DIFFICULTY_FUN_SYSTEM.md`.

Снято 31.07.2026, коммит `3c2e85e`. Ни одна строка production-данных этой работой
не изменена: документ фиксирует состояние «до», чтобы после Phase 1-4 было с чем
сравнивать. Числа ниже — обязательный baseline для регрессии.

## Что вообще существует

Оценкой уровня в проекте занимаются **две независимые системы**. Это главный
факт baseline: у D уже есть две разные реализации, и они не согласованы между
собой.

```text
tool/level-tool/            TypeScript + React, задеплоен на bubble-level-tool.surge.sh
                            снимок базы → генерация блока → валидатор → счёт решений → D и I
                            источник правды: JSON-снимок content.snapshot.json

tool/word_content_pipeline/ Python, CLI `word-content`
                            SQLite-база контента → сборка кандидатов → exact solver → D → review pack
                            источник правды: JSONL + CSV, SQLite пересобирается
```

Третье место, где живёт модель оценки, — **документ**, а не код:
`levels/EVAL.md` (ручная модель D и F по факторам F1-F7, шкала 1-10 с шагом 0.5,
калибровка на четырёх эталонах). Скилл `level-evaluator` считает по ней руками.

Итого до начала работы **три разных D** и **две разных «интересности»**.

## Baseline: тесты

| Система | Команда | Тестов | Результат |
|---|---|---|---|
| `tool/level-tool` | `npm test` | 82 | 82 pass, 0 fail |
| `tool/word_content_pipeline` | `pytest -q` | 260 | 260 passed |

Прогон 31.07.2026. Оба набора зелёные — точка отсчёта чистая.

## Baseline: контентная база

`tool/word_content_pipeline/database/content.sqlite`, `schema_version = 5`,
`content_version = 2026.07.31`.

| Таблица | Записей |
|---|---|
| `words` | 10 441 |
| `word_senses` | 588 |
| `word_scores` | 10 798 |
| `categories` / `category_concepts` | 1 276 / 1 276 |
| `category_label_scores` | 1 276 |
| `memberships` | 18 775 |
| `quartets` | 3 197 |
| `level_instances` | 5 |
| `level_groups` / `level_tokens` | 25 / 100 |
| `level_solver_runs` | 5 |
| `level_decisions` | 0 |

Все пять уровней в статусе `review_pending`. **Принятых уровней ноль** —
значит, calibration dataset из accepted-уровней (Phase 6) пока собрать не из
чего, и это ограничение, а не недоработка.

## Baseline: версии формул

| Что | Версия | Где лежит |
|---|---|---|
| Генератор (level-tool) | `gen-1.0` | `web/src/core/generator.ts` |
| Сложность (level-tool) | `d-1.0-calibrated` | `web/src/data/scoring.config.json` |
| Интересность (level-tool) | `i-0.1-uncalibrated` | там же, секция `interest` |
| Сложность (pipeline) | `difficulty-heuristic/1.0` | `src/word_content/difficulty.py` |
| Рейтинги слов / названий / четвёрок | три независимых `scoring_version` | `data/content/scoring_config.yaml` |
| Снимок контента (level-tool) | `content_snapshot_hash` | `web/src/data/content.snapshot.json` |

Версии **солвера, симулятора структуры и blind-оценщика в level-tool не
существует вовсе** — счётчик решений `countSolutions()` не версионирован.
В pipeline версия солвера есть: `level_solver_runs.solver_version`.

## Найденные дублирующиеся оценки

Задание требует найти дубли до того, как заводить новые поля. Найдено четыре.

### 1. Сложность уровня считается трижды

| Реализация | Шкала | Компоненты | Калибровка |
|---|---|---|---|
| `scoringDifficulty.ts` | 1-10, шаг 0.5 | base (объём, редкость) + declared (мета) + semantic (ловушки, смежность) + mechanical (цепи, теснота K) | base откалиброван МНК на 199 референсных уровнях |
| `difficulty.py` | 1-10, шаг 0.5 | 10 компонентов: масштаб, редкость, знакомость, многозначность, пересечение пулов, альтернативные разбиения, первый ход, структурность, длина фразы, глубина мета | не калибрована |
| `levels/EVAL.md` | 1-10, шаг 0.5 | F1-F7: масштаб, ловушки, близость, редкость, лимит, память, внеплановая двусмысленность | калибрована на 4 эталонах, допуск ±1 |

Шкала у всех трёх одна и та же, компоненты пересекаются процентов на семьдесят,
а числа на одном и том же уровне совпадать не обязаны. Ни одна из трёх не
является «главной» по документации.

### 2. «Интересность» и «фан» — два имени одной оси

- `scoringInterest.ts` → `I` = Clarity + Variety + Aha + Freshness, каждый композит 0..2.5;
- `levels/EVAL.md` → `F` = база 5 + якоря (узнаваемость, ага-момент, разнообразие, темп, пресность).

Целевая модель называет эту ось `F` (Fun). Третьего имени заводить нельзя.

### 3. Ambiguity считается на трёх уровнях под тремя именами

- `word_scores.ambiguity_score` — многозначность слова;
- `quartets.ambiguity_pressure` — давление неоднозначности на четвёрке;
- `scoringDifficulty.ts` → `semantic.'подтверждённые ловушки'` + `'смежность категорий'` +
  `'незапланированная спорность'` — на уровне.

Целевая модель просит `ambiguity_pressure` как компонент D **уровня**. Имя уже
занято четвёркой. Разводится в mapping.

### 4. Ловушка и near-pair считают один и тот же конфликт

`levels/EVAL.md` уже содержит правило дедупликации (F3 не засчитывает связь
через одно слово-ловушку, F7 не считает заявленные ловушки). В коде
`scoringDifficulty.ts` такого правила **нет**: `adjacentPairs` считается по
совпадению `theme` у категорий и может пересчитать тот же конфликт, который уже
дал вклад в `confirmed traps`. Задание §7 прямо это запрещает.

## Что из требований целевой модели уже реализовано

| Требование целевой модели | Состояние |
|---|---|
| `solution_count == 1` как hard gate | **есть в обеих системах.** `GLOBAL_SOLUTION_COUNT` (hard) в валидаторе level-tool; `level_solver_runs` + `level_instances.solution_count` в pipeline |
| Технические gates до scoring | **частично.** 24 проверки в `validator.ts` (hard/soft), из них 8 покрывают список §4 задания |
| Статусы уровня `accepted / needs_changes / rejected` | **есть полностью**, плюс `candidate / solver_valid / review_pending` — см. `docs/status_semantics.md` |
| Reason codes на отклонении | **есть**, 9 кодов, три намеренно не пишут в базу |
| Review pack готового уровня | **есть**, `level_review.py` → JSON + Markdown; показывает D, компоненты, solver, группы, конкурирующие связи, cooldowns, ui/risk warnings |
| Blind AI evaluation | **есть частично.** `prompts/blind_solver.md`, `scripts/solver_input.ts`, 20 прогонов в `levels/solver/*.blind.json`. Не версионирован, схема ответа не валидируется |
| Параметры слова / названия / четвёрки из §1.1 | **есть почти полностью**, см. mapping |
| Generation profiles | **есть**, 3 профиля в `data/content/generation_profiles.yaml` |
| Mechanic cooldown | **есть частично**, `cooldown.py` + `cooldown_config.yaml` — про слова и категории, не про механики |
| Versioned config весов | **есть** для D/I (level-tool) и для рейтингов (pipeline) |
| Детерминизм «тот же seed → тот же результат» | **есть**, проверяется тестами `determinism.test.ts` |

## Чего нет вообще

Это и есть настоящий объём Phase 1-4.

1. **`R` (Frustration Risk)** — ни в одной из трёх моделей. Косвенно: `risk_warnings`
   в review pack и `memberships.risk_flags`.
2. **`C` (Confidence)** — нет. Неизвестная familiarity сейчас просто закрывает
   связь, а не снижает уверенность в оценке.
3. **`Fairness Gate` (PASS / WARNING / FAIL)** — нет как единой сущности.
   Есть `ValidationResult.passed` (bool) и severity `hard`/`soft` на проверках:
   двух значений вместо трёх.
4. **Structural metrics из §8** — нет ни одной. `field_zone_count`,
   `zone_isolation_score`, `category_fragmentation_score`,
   `completion_opportunity_ratio`, `action_branching_complexity`,
   `simultaneously_active_hypotheses` — ничего этого не считается.
   `boardCapacity` и `VISIBLE_SHARE` — единственное, что вообще знает про поле.
5. **Каталог механик** (`mechanic_catalog`, `mechanic_usage_history`,
   `novelty_score`, `payoff_score`, freshness multiplier) — нет.
   Модификаторы `chains` / `halves` заданы в типах, каталога и истории нет.
6. **Snapshot оценок на принятом уровне** — нет. `content_hash` фиксирует состав
   уровня, но не рассчитанные D/F/R/C, поэтому смена версии формулы сейчас
   поменяла бы историческую оценку.
7. **Calibration fixtures как код** — нет. Эталоны есть (`levels/etalon/e1-e3`,
   `levels/demo/journey-d7` с целевыми D), но прогоняются руками через скилл,
   а не тестом.
8. **Единый validation pipeline поверх обеих систем** — нет. Level-tool валидирует
   свои уровни, pipeline свои, общего входа в scoring не существует.

## Ограничения, которые надо держать в голове

- **Принятых уровней ноль, и приёмка базы отменена.** Решением продакта от
  31.07 приёмка делается на генераторе уровней, а не на пяти кандидатах базы:
  они остаются в `review_pending` навсегда. Значит, калибровочный набор берётся
  из четырёх эталонов (`levels/etalon/e1-e3`, `levels/demo/journey-d7`) и из
  приёмки собранных генератором уровней, а не из `level_decisions`.
- **Телеметрии нет и не будет в рамках задания.** Ни D, ни F, ни R не являются
  прогнозом win rate. Референсная калибровка D опирается на номер уровня как
  ordinal proxy — это записано в `scoring.config.json` как `caveat` и остаётся
  верным для новой модели.
- **Пакет 201-210 не воспроизводится из текущей базы:** `pack_hash` включает
  хеш снимка контента. Любая регрессия по этому пакету сравнивает артефакт,
  а не пересборку.
- **Blind-прогоны в `levels/solver/` сделаны по прежним уровням** и прежним
  промптом. Как fixture для `blind_evaluator_version` они не годятся без
  повторного прогона.
