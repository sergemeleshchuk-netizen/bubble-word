# Инструкция для Claude Code: внедрение единой системы D/F/R/C

## Контекст

В проекте уже выполняются отдельные работы по развитию базы слов, exact-level solver и системе quality scoring контента.

Эта инструкция добавляет единый слой оценки готовых уровней:

- `D` — Difficulty, сложность прохождения;
- `F` — Fun, интересность;
- `R` — Frustration Risk, риск фрустрации;
- `C` — Confidence, уверенность системы в оценке;
- `Fairness Gate` — `PASS / WARNING / FAIL`.

Исходная продуктовая модель находится в:

```text
UNIFIED_LEVEL_DIFFICULTY_FUN_SYSTEM.md
```

Эта модель должна быть реализована как рабочая система, а не только как документация.

Не переписывай текущую архитектуру без необходимости. Сначала изучи репозиторий, найди уже существующие сущности, scores, generator, solver и review-export, затем составь mapping новых требований на текущий код.

---

# 1. Куда применяется система

Система применяется к четырём слоям проекта.

## 1.1 Контентная база

Контентная база должна предоставлять исходные параметры, необходимые для оценки уровня:

### Word / display form

```text
familiarity_score
char_count
token_count
display_width_score
spelling_difficulty_score
ambiguity_score
novelty_score
accessibility_score
```

### Category variant / label

```text
label_familiarity_score
label_clarity_score
label_naturalness_score
label_specificity_score
label_quality_score
relation_type
base_difficulty
```

### Membership

```text
semantic_fit_score
membership_obviousness_score
sense_confidence
alternative_fit_score
trap_potential_score
```

### Quartet

```text
avg_word_familiarity
min_word_familiarity
semantic_cohesion_score
quartet_clarity_score
quartet_interest_score
quartet_ambiguity_score
quartet_quality_score
```

Не добавляй вручную утверждаемые `human_approved` статусы к словам, категориям или четвёркам.

На этом слое хранятся машинно проверяемые параметры и предупреждения.

---

## 1.2 Генератор уровня

Генератор использует параметры базы и целевой профиль, чтобы собрать level candidate.

Он должен уметь управлять:

```text
target_difficulty_range
target_fun_range
max_frustration
minimum_confidence

category_count
word_count
familiarity thresholds
word length thresholds
trap budget
near-category-pair budget
field fragmentation
zone isolation
completion opportunity
mechanic budget
mechanic freshness
payoff target
```

Генератор не должен максимизировать один общий score.

Он должен искать комбинацию, попадающую в целевой профиль `D/F/R`.

---

## 1.3 Solver и симулятор структуры поля

Exact solver отвечает за формальную корректность:

```text
solution_count == 1
```

Симулятор структуры поля отвечает за параметры, которые нельзя получить из одних слов:

```text
field_zone_count
zone_isolation_score
cross_zone_dependency_count
category_fragmentation_score
simultaneously_active_hypotheses
unresolved_partial_group_count
completion_opportunity_ratio
action_branching_complexity
dead_end_action_count
constraint_pressure
```

Blind AI не заменяет exact solver.

---

## 1.4 Review pack готового уровня

После технических проверок готовый уровень экспортируется человеку.

Review pack должен показывать:

```text
D
F
R
C
Fairness Gate

полный breakdown
слова и категории
ловушки
альтернативные связи
структуру поля
solver result
blind AI result
warnings
```

Человек принимает решение только по готовому уровню:

```text
accepted
needs_changes
rejected
```

---

# 2. Что не нужно делать

Не следует:

1. добавлять один непрозрачный `level_quality_score`;
2. заменять exact solver AI-оценкой;
3. применять D/F только к словам или отдельным четвёркам;
4. вручную подтверждать все элементы базы до генерации;
5. считать любую двусмысленность интересной;
6. считать любую новую механику сложной;
7. выдавать heuristic score за объективную истину;
8. менять принятые уровни при пересчёте новой версии формулы;
9. блокировать текущую работу большой миграцией без baseline и mapping.

---

# 3. Целевая архитектура

Используй текущие сущности проекта, если они уже существуют. Не создавай дубликаты.

Минимальная целевая структура:

```text
words / word_senses
category_concepts
category_variants
memberships
quartet_variants

level_instances
level_categories
level_items
level_layout
level_mechanics

level_solver_runs
level_structure_metrics
level_blind_evaluations
level_scores
level_reviews
level_review_reasons

mechanic_catalog
mechanic_usage_history
scoring_model_versions
generation_profiles
```

Если проект использует JSON/JSONL как source of truth, сохраняй этот принцип. SQLite остаётся пересобираемым snapshot.

---

# 4. Обязательные gates до расчёта оценки

Создай единый validation pipeline.

Уровень допускается к scoring только при выполнении:

```text
all categories contain exactly 4 required elements
no duplicate display token inside level
all required senses resolved
all words renderable
no blocked content
layout graph valid
mechanic state transitions valid
solver completed successfully
solution_count == 1
```

Результаты gate:

```text
PASS
WARNING
FAIL
```

## FAIL

- несколько решений;
- решений нет;
- solver timeout;
- invalid layout;
- broken mechanic sequence;
- blocked content;
- критически слабая необъяснимая связь.

## WARNING

- неизвестная familiarity;
- слабый label;
- слишком длинное слово;
- низкая confidence;
- новая непроверенная механика;
- повышенный frustration risk.

Только `PASS` и допустимые `WARNING` идут в review pack.

---

# 5. Внутренняя модель Difficulty

Рассчитывай шесть компонентов в диапазоне `0..100`:

```text
semantic_difficulty
ambiguity_pressure
structural_difficulty
content_load
constraint_pressure
mechanic_cognitive_load
```

Начальная формула:

```text
difficulty_internal =
    0.25 * semantic_difficulty
  + 0.25 * ambiguity_pressure
  + 0.25 * structural_difficulty
  + 0.10 * content_load
  + 0.10 * constraint_pressure
  + 0.05 * mechanic_cognitive_load
```

Итог:

```text
D_raw = 1 + 9 * difficulty_internal / 100
D = round_to_half(D_raw)
```

Все веса должны находиться в versioned config.

---

# 6. Semantic Difficulty

Рассчитать:

```text
word_unfamiliarity
word_readability_load
membership_non_obviousness
label_difficulty
```

Начальная формула:

```text
semantic_difficulty =
    0.30 * word_unfamiliarity
  + 0.15 * word_readability_load
  + 0.35 * membership_non_obviousness
  + 0.20 * label_difficulty
```

## Требования

Не использовать только среднее значение.

Обязательно учитывать:

```text
avg_word_familiarity
min_word_familiarity
p25_word_familiarity
unknown_familiarity_count

avg_membership_obviousness
min_membership_obviousness
weakest_membership_penalty
```

Одно ключевое неизвестное слово или одна слабая связь могут блокировать группу сильнее, чем показывает среднее.

---

# 7. Ambiguity Pressure

Ловушка считается валидной только если:

1. слово правдоподобно подходит другой категории уровня;
2. это подтверждается данными membership или независимой оценкой;
3. blind AI действительно рассматривает альтернативу;
4. exact solver всё равно доказывает единственное решение;
5. после раскрытия правильная связь выглядит честной.

Для слова в уровне вычислять:

```text
valid_target_count
plausible_target_count
alternative_fit_max
alternative_fit_gap
trap_strength
```

Для уровня:

```text
trap_word_count
weak_trap_count
medium_trap_count
strong_trap_count
cross_category_edge_count
ambiguity_density
hypothesis_competition
unplanned_ambiguity_count
```

Начальная формула:

```text
ambiguity_pressure =
    0.30 * normalized_trap_word_count
  + 0.30 * ambiguity_density
  + 0.20 * strong_trap_ratio
  + 0.20 * hypothesis_competition
```

Практический вклад ловушек в D:

```text
weak trap:    +0.50
medium trap:  +0.75
strong trap:  +1.00
maximum total trap contribution: +3.00
```

Не считай один и тот же конфликт одновременно ловушкой, near-pair и unplanned ambiguity без явного правила дедупликации.

---

# 8. Structural Difficulty

Этот компонент должен считаться из layout/state graph.

Начальная формула:

```text
structural_difficulty =
    0.25 * category_fragmentation
  + 0.20 * zone_isolation
  + 0.20 * working_memory_load
  + 0.20 * low_completion_opportunity
  + 0.15 * branching_complexity
```

## Обязательные метрики

```text
field_zone_count
zone_isolation_score
cross_zone_dependency_count
category_fragmentation_score

simultaneously_active_hypotheses
unresolved_partial_group_count
maximum_partial_group_count

completion_opportunity_ratio
time_or_steps_to_first_completion
states_without_productive_completion

action_branching_complexity
dead_end_action_count
```

## Completion opportunity

```text
completion_opportunity_ratio =
    reachable_states_with_at_least_one_completable_category
    / evaluated_reachable_states
```

Если полный перебор слишком дорогой, используй:

- deterministic sampling;
- фиксированный seed;
- ограниченное число representative paths;
- confidence penalty за приближение.

Не маскируй approximation под точный результат.

---

# 9. Content Load

Рассчитывать:

```text
category_count
total_word_count
visible_word_count
simultaneously_active_category_count
relation_type_variety
```

Начальная формула:

```text
content_load =
    0.55 * normalized_category_count
  + 0.30 * normalized_total_word_count
  + 0.15 * relation_type_variety
```

Используй saturating normalization, а не чистую линейную шкалу.

Рост с 5 до 8 категорий должен влиять сильнее, чем рост с 13 до 16.

---

# 10. Constraint Pressure

Если есть moves limit:

```text
K = available_moves / estimated_minimum_moves
```

Примерная шкала:

```text
K >= 1.60    spacious
1.40–1.59    comfortable
1.25–1.39    tense
1.10–1.24    spike
K < 1.10     high frustration risk
```

Если moves limit отсутствует, рассчитывать pressure по реальным ограничениям:

- доступные временные слоты;
- число допустимых ошибок;
- глубина скрытых элементов;
- блокировки;
- обязательный порядок;
- ограниченное число доступных действий.

---

# 11. Mechanic Cognitive Load

Для каждой механики хранить:

```text
mechanic_id
mechanic_family
rule_complexity
state_change_count
hidden_information_ratio
dependency_depth
player_familiarity
cognitive_load
```

Эффективная сложность:

```text
effective_mechanic_load =
    raw_mechanic_load * mechanic_unfamiliarity
```

Повтор уже изученной механики снижает её вклад в D.

Механика преимущественно влияет на F, но новая непрозрачная механика также повышает R.

---

# 12. Fun Model

Рассчитывать компоненты `0..100`:

```text
recognizability
semantic_aha
mechanic_novelty
anticipation_and_payoff
content_variety_and_theme
tempo
staleness_penalty
unfairness_penalty
```

Начальная формула:

```text
fun_internal =
    0.15 * recognizability
  + 0.25 * semantic_aha
  + 0.20 * mechanic_novelty
  + 0.20 * anticipation_and_payoff
  + 0.10 * content_variety_and_theme
  + 0.10 * tempo
  - staleness_penalty
  - unfairness_penalty
```

Затем:

```text
F_raw = 1 + 9 * clamp(fun_internal, 0, 100) / 100
F = round_to_half(F_raw)
```

---

# 13. Practical Fun V1

Для human-readable объяснения можно дополнительно показывать компактную систему:

```text
base F = 5.0
```

Модификаторы:

```text
concrete recognizable categories        +1.0
mixed but understandable content         +0.5
weak abstract category                  -0.5

honest trap that caused doubt           +0.5
maximum aha contribution                +2.0

varied life domains                     +0.5
coherent theme/story                    +0.5

fresh mechanic with payoff              +1.0
known mechanic in new combination       +0.5
repeated mechanic without evolution     -0.5

quick first success                     +0.5
long period without progress            -0.5
no aha and no event                     -0.5
```

Эта V1 является explainability layer. Источником расчёта остаются подробные метрики.

---

# 14. Mechanic Freshness and Payoff

Добавить каталог механик и историю использования.

Для каждой механики:

```text
first_introduction_level
last_used_level
usage_count_recent_10
usage_count_recent_30
consecutive_usage_count
mechanic_variant
combination_signature
novelty_score
payoff_score
visual_impact_score
```

Пример freshness multiplier:

```text
rare appearance                  1.00
recent repeat                    0.70
several consecutive repeats      0.40
routine repeat without evolution 0.10
```

Повтор механики не штрафуется сильно, если появился новый twist:

- другая комбинация;
- новая стратегическая роль;
- более глубокая цепь;
- новый payoff;
- взаимодействие с другой механикой.

---

# 15. Frustration Risk

Рассчитывать:

```text
unfair_ambiguity
weakest_membership_problem
unknown_word_pressure
low_progress_visibility
excessive_fragmentation
rule_opacity
mechanic_overload
```

Начальная формула:

```text
frustration_internal =
    0.25 * unfair_ambiguity
  + 0.20 * weakest_membership_problem
  + 0.15 * unknown_word_pressure
  + 0.15 * low_progress_visibility
  + 0.10 * excessive_fragmentation
  + 0.10 * rule_opacity
  + 0.05 * mechanic_overload
```

Итог:

```text
R_raw = 1 + 9 * frustration_internal / 100
R = round_to_half(R_raw)
```

## Hard gates

Если:

```text
solution_count != 1
```

или blind AI стабильно строит альтернативное логичное решение, уровень не может считаться качественным.

При Fairness `FAIL`:

```text
F <= 3.0
review_status = needs_changes or rejected
```

---

# 16. Confidence Score

Рассчитывать:

```text
data_completeness
metric_reliability
solver_certainty
blind_evaluation_consistency
model_calibration_quality
```

Начальная формула:

```text
C =
    weighted_geometric_or_conservative_mean(
        data_completeness,
        metric_reliability,
        solver_certainty,
        blind_evaluation_consistency,
        model_calibration_quality
    )
```

Не используй обычное среднее, если один критический компонент равен нулю.

Снижать C при:

- отсутствующей familiarity;
- неизвестном sense;
- AI-only naturalness;
- новой механике без симуляции;
- approximation в structural analysis;
- расхождении blind evaluators;
- выходе за калиброванный диапазон.

---

# 17. Blind AI Evaluation

Реализуй отдельный экспорт и runner.

Blind AI получает:

- слова;
- layout/state;
- правила уже объяснённых механик;
- без целевых категорий и правильного решения.

Он возвращает структурированный JSON:

```json
{
  "proposed_groups": [],
  "uncertain_words": [],
  "alternative_placements": [],
  "trap_candidates": [],
  "weak_links": [],
  "first_progress_point": null,
  "aha_moments": [],
  "confidence": 0.0,
  "fun_impression": "",
  "frustration_notes": []
}
```

Использовать минимум два независимых прогона или два seed/temperature режима, если инфраструктура позволяет.

Blind AI используется для семантической диагностики, а не математического proof.

---

# 18. Human Review Workflow

После всех автоматических этапов человек получает review pack.

Хранить:

```text
D_auto
F_auto
R_auto
C_auto

D_human
F_human
R_human

decision
reason_codes
comment
reviewed_at
reviewer_id_or_alias
```

Статусы:

```text
candidate
solver_valid
review_pending
accepted
needs_changes
rejected
```

Accepted level должен становиться regression fixture.

---

# 19. Review Pack

Для каждого уровня экспортировать:

## Summary

```text
D / F / R / C
Fairness Gate
target profile
solver state
review status
```

## Difficulty breakdown

```text
semantic
ambiguity
structure
content load
constraint pressure
mechanic load
```

## Fun breakdown

```text
recognizability
aha
novelty
payoff
variety/theme
tempo
```

## Risks

```text
unplanned ambiguity
weak memberships
unknown words
long words
poor labels
low progress visibility
mechanic repetition
rule opacity
```

## Content details

- words;
- senses;
- categories;
- exact quartets;
- traps;
- alternative fits;
- category near-pairs.

## Structure

- initial layout;
- zones;
- dependency graph;
- expected first progress;
- completion opportunity;
- mechanic timeline.

## Explanation

Сгенерировать короткий human-readable абзац:

```text
Почему уровень сложный.
Почему он интересный.
Где риск фрустрации.
```

---

# 20. Generation Profiles

Создать versioned YAML profiles.

Минимум:

```text
easy
core
hard
high_fun
hard_high_fun
recovery
mechanic_showcase
```

Пример:

```yaml
profile: hard_high_fun

difficulty:
  target: [6.5, 8.0]

fun:
  target: [7.0, 9.0]

frustration:
  max: 3.5

confidence:
  min: 75

content:
  category_count: [10, 14]
  min_word_familiarity: 0.40
  avg_word_familiarity_min: 0.62

ambiguity:
  strong_traps: [3, 6]
  unplanned_ambiguity_max: 1

structure:
  fragmentation: high
  zone_isolation: medium
  completion_opportunity_min: 0.35

mechanics:
  new_mechanics_max: 1
  payoff_required: true
  recent_repeat_penalty: true
```

---

# 21. CLI

Добавить или расширить команды:

```bash
level-content validate-level
level-content solve-level
level-content simulate-level
level-content score-level
level-content blind-evaluate
level-content export-review-pack
level-content review-level
level-content recalibrate-model
level-content compare-model-versions
```

Примеры:

```bash
level-content score-level \
  --level levels/candidates/127.json \
  --config config/scoring/difficulty_v1.yaml \
  --output reports/127_score.json

level-content export-review-pack \
  --level-id 127 \
  --output review/level_127/
```

Обязательные параметры:

```text
--seed
--dry-run
--config
--model-version
--output
```

---

# 22. Версионирование

Хранить:

```text
difficulty_model_version
fun_model_version
frustration_model_version
confidence_model_version
solver_version
structure_simulator_version
blind_evaluator_version
generation_profile_version
```

У принятого уровня сохранять snapshot рассчитанных параметров.

Новая версия формулы не должна автоматически менять историческую оценку принятого уровня.

---

# 23. Калибровка

Создать calibration dataset из:

- accepted levels;
- намеренно лёгких;
- средних;
- сложных;
- high-fun;
- low-fun;
- frustration examples;
- levels with/without mechanics.

Для каждого:

```text
target_D
target_F
target_R
human_explanation
```

При изменении модели:

1. прогнать все calibration fixtures;
2. сравнить old/new;
3. сформировать diff;
4. проверить допуск;
5. только затем активировать новую версию.

Начальный допуск:

```text
D ±1.0
F ±1.0
R ±1.0
```

---

# 24. Порядок внедрения

## Phase 0 — Baseline

1. Найти текущие модели данных и скрипты.
2. Зафиксировать текущие counts и тесты.
3. Найти дублирующиеся scores.
4. Составить mapping.
5. Не менять production data.

Выход:

```text
docs/evaluation_baseline.md
docs/evaluation_mapping.md
```

---

## Phase 1 — Gates and Score Schema

1. Добавить D/F/R/C и component scores.
2. Добавить Fairness Gate.
3. Добавить version fields.
4. Реализовать deterministic scoring API.
5. Добавить unit tests.

---

## Phase 2 — Structural Metrics

1. Подключить layout/state graph.
2. Реализовать zones и fragmentation.
3. Рассчитать completion opportunity.
4. Рассчитать branching и partial hypotheses.
5. Добавить confidence penalty при approximation.

---

## Phase 3 — Blind Evaluation

1. Сделать blind export.
2. Сделать structured response schema.
3. Добавить parsing/validation.
4. Подключить trap and ambiguity findings.
5. Не использовать blind result как proof.

---

## Phase 4 — Review Pack and Human Workflow

1. Экспортировать полный review pack.
2. Добавить accepted/needs_changes/rejected.
3. Добавить reason codes.
4. Превращать accepted levels в regression fixtures.

---

## Phase 5 — Generator Integration

1. Создать profiles.
2. Фильтровать candidates по D/F/R/C.
3. Добавить mechanic freshness/cooldown.
4. Генерировать batch кандидатов.
5. Выбирать Pareto-optimal levels, а не один максимальный score.

---

## Phase 6 — Calibration

1. Перенести существующие эталонные уровни.
2. Добавить human ratings.
3. Прогнать V1.
4. Сформировать before/after report.
5. Зафиксировать model version.

---

# 25. Тесты

## Unit

- familiarity and word length;
- weak membership penalty;
- valid trap;
- unplanned ambiguity;
- category near-pair;
- field fragmentation;
- zone isolation;
- completion opportunity;
- mechanic freshness;
- Fairness FAIL;
- confidence degradation.

## Solver regression

- unique level;
- alternative partition;
- no solution;
- timeout;
- dynamic mechanic state;
- cross-zone dependency.

## Scoring regression

Минимум:

- easy;
- medium;
- hard;
- high-fun easy;
- high-fun hard;
- high-frustration;
- mechanic overuse;
- unknown-word blocker.

## End-to-end

```text
content DB
→ candidate generation
→ solver
→ structural simulation
→ scoring
→ blind evaluation
→ review pack
→ human decision
→ regression fixture
```

---

# 26. Обязательные файлы

Предпочтительные пути; адаптируй к текущему репозиторию:

```text
docs/level_evaluation/README.md
docs/level_evaluation/MODEL.md
docs/level_evaluation/CALIBRATION.md

config/scoring/difficulty_v1.yaml
config/scoring/fun_v1.yaml
config/scoring/frustration_v1.yaml
config/scoring/confidence_v1.yaml
config/generation_profiles/*.yaml
config/mechanics/catalog.yaml

src/.../evaluation/
src/.../solver/
src/.../simulation/
src/.../review/

tests/evaluation/
tests/solver/
tests/simulation/
tests/e2e/

levels/calibration/
levels/accepted/
levels/candidates/
review/
```

Не создавай новую корневую структуру, если в проекте уже есть подходящая.

---

# 27. Definition of Done

Работа завершена, когда:

1. каждый валидный уровень получает `D/F/R/C`;
2. все component scores доступны;
3. Fairness Gate работает до human review;
4. exact solver доказывает уникальность;
5. blind AI не используется как proof;
6. structural difficulty считается по реальному layout;
7. генератор может выбирать уровни по целевому профилю;
8. mechanics имеют freshness/cooldown/payoff;
9. review pack объясняет оценки;
10. человек оценивает готовый уровень целиком;
11. accepted levels становятся regression fixtures;
12. все формулы версионированы;
13. одинаковый seed/config дают одинаковый результат;
14. модель проходит calibration fixtures;
15. текущий word-content pipeline не сломан;
16. существующая работа по основной инструкции сохранена.

---

# 28. Формат итогового отчёта

В конце предоставить:

1. baseline;
2. mapping старой и новой архитектуры;
3. список изменённых файлов;
4. миграции;
5. формулы и версии;
6. реализованные metrics;
7. CLI-команды;
8. результаты unit tests;
9. результаты solver regression;
10. результаты calibration;
11. три демонстрационных review pack:
    - easy;
    - hard;
    - hard high-fun;
12. известные ограничения;
13. что требует telemetry;
14. точные следующие шаги.

---

# 29. Команда на выполнение

Выполни эту работу как отдельный слой поверх текущих задач.

Сначала реализуй `Phase 0–2`, чтобы получить рабочие gates, score schema и structural metrics. Затем реализуй `Phase 3–4`. Интеграцию генератора и полную калибровку делай после того, как базовая оценка и review pack проходят тесты.

Не останавливайся только на документации. Результатом должны быть работающий код, тесты, конфиги и минимум три демонстрационных уровня.
