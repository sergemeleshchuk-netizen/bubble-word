# Дополнительная инструкция для Claude Code: система рейтингов контента

## Контекст

Основная инструкция по развитию `tool/word_content_pipeline` уже выполняется.  
Эта задача является отдельным дополнением и не должна ломать, переписывать или останавливать текущую работу.

Цель дополнения — добавить в базу и генератор явную параметризацию качества слов, названий категорий и игровых четвёрок, чтобы генератор мог управляемо собирать более понятные, короткие, знакомые и при этом интересные уровни.

Ручная проверка по-прежнему выполняется на уровне готового уровня целиком.  
Не добавляй обязательный human approval для слов, категорий или четвёрок.

---

## 1. Главный принцип

Не хранить только один непрозрачный общий рейтинг.

Нужно хранить отдельные измеримые параметры, а итоговые scores рассчитывать по версионируемым формулам.

Обязательное разделение:

- знакомость;
- читаемость;
- длина;
- визуальная пригодность;
- семантическая ясность;
- неоднозначность;
- интересность;
- сложность;
- пригодность для конкретного профиля генерации.

---

## 2. Параметры слова

Для каждого игрового слова или display form должны быть доступны:

```text
familiarity_score
char_count
token_count
display_width_score
spelling_difficulty_score
ambiguity_score
novelty_score
accessibility_score
word_quality_score
scoring_version
```

### 2.1 familiarity_score

Использовать существующий показатель частотности на базе `wordfreq`.

Требования:

- значение должно существовать для максимально возможной доли слов;
- отсутствие значения хранить как `NULL` / `unknown`, а не как ноль;
- неизвестная знакомость не должна автоматически проходить в обычные уровни;
- генератор должен уметь задавать минимальный и средний порог знакомости.

### 2.2 char_count

Количество отображаемых символов после нормализации display text.

Считать автоматически для 100% слов.

Не учитывать скрытые технические идентификаторы, sense suffix и служебную разметку.

### 2.3 token_count

Количество слов в отображаемой фразе.

Примеры:

```text
apple -> 1
polar bear -> 2
hot air balloon -> 3
```

### 2.4 display_width_score

Оценка того, насколько хорошо слово помещается на игровой карточке или bubble.

Не ограничиваться только числом символов: учитывать широкие буквы, пробелы, дефисы и реальную display form.

На первом этапе допустима детерминированная приближённая формула.

Значение нормализовать в диапазон 0..1:

```text
1.0 = очень удобно помещается
0.0 = практически непригодно без уменьшения текста
```

### 2.5 spelling_difficulty_score

Оценка сложности чтения и написания слова для средней взрослой американской casual-аудитории.

Можно учитывать:

- длину;
- редкие буквенные сочетания;
- количество слогов, если доступно;
- нестандартное написание;
- диакритику;
- аббревиатуры;
- сложные имена собственные.

Не выдавать heuristic score за human truth. Сохранять версию формулы.

### 2.6 ambiguity_score

Оценка того, насколько слово многозначно в рамках базы.

Учитывать:

- количество senses;
- количество сильно различающихся category concepts;
- количество игровых memberships;
- количество известных bridge-use cases.

Высокая неоднозначность не всегда плоха: она может быть полезна как ловушка. Поэтому это отдельный параметр, а не прямой штраф качества.

### 2.7 novelty_score

Оценка того, насколько слово даёт ощущение новизны или интереса, не становясь слишком редким.

Не приравнивать novelty к rarity.

Пример:

- очень частое и банальное слово может иметь низкую novelty;
- умеренно знакомое, яркое и конкретное слово может иметь высокую novelty;
- крайне редкое специальное слово не должно автоматически получать высокий novelty.

### 2.8 accessibility_score

Итоговая лёгкость восприятия слова.

Начальная формула может быть такой:

```text
accessibility_score =
    0.55 * familiarity_score
  + 0.20 * display_width_score
  + 0.15 * brevity_score
  + 0.10 * spelling_simplicity_score
```

Формула должна быть:

- вынесена в конфиг;
- версионирована;
- покрыта тестами;
- пересчитываема без ручной правки базы.

### 2.9 word_quality_score

Это общий рейтинг пригодности слова для генератора, но он не должен заменять отдельные параметры.

Примерная логика:

```text
word_quality_score =
    accessibility
  + semantic usefulness
  + controlled novelty
  - policy penalty
  - severe display penalty
```

Не использовать `word_quality_score` как единственный критерий отбора.

---

## 3. Параметры названия категории

Для каждого `category_variant` или игрового label добавить:

```text
label_familiarity_score
label_char_count
label_token_count
label_display_width_score
label_naturalness_score
label_clarity_score
label_specificity_score
label_novelty_score
label_quality_score
scoring_version
```

### 3.1 label_naturalness_score

Оценка того, насколько естественно категория звучит для носителя американского английского.

Не пытаться получить надёжную human-level оценку только формулой.

Разрешены:

- автоматический heuristic score;
- AI-proposed score;
- warning при сомнительной формулировке.

Но не ставить `human_approved`.

### 3.2 label_clarity_score

Насколько название помогает однозначно понять принцип группы после её решения.

Высокий score:

```text
BIRDS OF PREY
KITCHEN TOOLS
THINGS THAT MELT
```

Низкий score:

```text
MISCELLANEOUS ITEMS
RELATED THINGS
SPECIAL WORDS
```

### 3.3 label_specificity_score

Категория не должна быть ни чрезмерно широкой, ни искусственно узкой.

Примеры:

```text
ANIMALS
```

понятно, но слишком широко.

```text
AFRICAN SAVANNA PREDATORS
```

более конкретно, если слова действительно соответствуют.

Specificity нужно хранить отдельно от clarity.

### 3.4 label_quality_score

Агрегированный показатель названия категории.

Пример:

```text
label_quality_score =
    naturalness
  + clarity
  + specificity
  + display fitness
  + familiarity
```

Формулу вынести в версионируемый конфиг.

---

## 4. Параметры конкретной четвёрки

Для каждого `quartet_variant` вычислять:

```text
avg_word_familiarity
min_word_familiarity
avg_word_accessibility
min_word_accessibility
avg_word_length
max_word_length
semantic_cohesion_score
quartet_clarity_score
quartet_novelty_score
quartet_interest_score
quartet_ambiguity_score
label_quality_score
quartet_quality_score
difficulty_score
scoring_version
```

### 4.1 semantic_cohesion_score

Насколько все четыре слова одинаково хорошо соответствуют категории.

Одна слабая связь должна снижать score сильнее, чем четыре средние связи.

Поэтому использовать не только среднее, но и минимум / weakest-link penalty.

### 4.2 quartet_interest_score

Интересность четвёрки должна быть отдельной от понятности.

Учитывать:

- наличие умеренной новизны;
- разнообразие слов;
- яркость образов;
- качество aha-момента;
- отсутствие четырёх полностью банальных элементов;
- отсутствие четырёх слишком редких элементов.

Примерная логика:

```text
quartet_interest =
    controlled_novelty
  + semantic_elegance
  + word_diversity
  + label_quality
  - obscurity_penalty
  - repetition_penalty
```

### 4.3 quartet_quality_score

Общий технический рейтинг пригодности четвёрки для генерации.

Он не заменяет full-level solver.

Высокий quartet score не означает, что сочетание безопасно использовать с любыми другими группами.

---

## 5. Профили генерации

Генератор должен уметь работать с конфигами качества.

Пример профиля лёгкого уровня:

```yaml
profile: easy_accessible

word_familiarity_min: 0.65
word_familiarity_avg_min: 0.75
word_accessibility_min: 0.70

max_word_chars: 12
max_word_tokens: 2
max_label_chars: 20
max_label_tokens: 4

label_quality_min: 0.75
quartet_quality_min: 0.75
quartet_interest_target: 0.35

allowed_ambiguity: low
allowed_hard_words_per_level: 0
```

Пример более интересного уровня:

```yaml
profile: accessible_fun

word_familiarity_min: 0.50
word_familiarity_avg_min: 0.68
word_accessibility_min: 0.60

max_word_chars: 16
max_word_tokens: 3

label_quality_min: 0.72
quartet_quality_min: 0.70
quartet_interest_target: 0.60

allowed_ambiguity: medium
novel_words_target_ratio: 0.20
```

Пример сложного уровня:

```yaml
profile: hard_knowledge

word_familiarity_min: 0.30
word_familiarity_avg_min: 0.50

label_quality_min: 0.75
quartet_quality_min: 0.65

allowed_ambiguity: high
allowed_hard_words_per_level: 8
novel_words_target_ratio: 0.35
```

Фактические пороги не считать финальными. Они должны быть конфигурируемыми и калиброваться на реальных уровнях.

---

## 6. Баланс понятности и интересности

Генератор не должен просто выбирать четыре слова с максимальной частотностью.

Иначе уровни станут понятными, но скучными.

Для обычного уровня использовать управляемую смесь:

```text
70-85% — знакомые и короткие слова
15-30% — менее банальные, но всё ещё понятные слова
0% — непонятные слова без контекстного основания
```

Поддержать параметры:

```text
familiar_anchor_ratio
novel_word_ratio
rare_word_budget
long_phrase_budget
ambiguity_budget
```

Пример требования генератору:

```text
Собрать уровень, где большинство слов очень знакомы аудитории,
но в каждой второй или третьей категории есть один более интересный
и менее банальный элемент, не нарушающий понятность группы.
```

---

## 7. Где хранить данные

Предпочтительно:

- сырые вычислимые параметры хранить в основной модели или воспроизводимом derived-слое;
- формулы и веса хранить в versioned config;
- агрегированные scores можно кэшировать;
- любой кэш должен быть полностью пересчитываемым.

Не дублировать вручную:

```text
char_count
token_count
display_width_score
```

если они могут быть надёжно пересчитаны из canonical display form.

Но они должны быть доступны генератору через БД, materialized view или отдельный экспорт.

---

## 8. Версионирование

Добавить:

```text
word_scoring_version
label_scoring_version
quartet_scoring_version
```

При изменении формулы должно быть возможно:

1. пересчитать scores;
2. сравнить старые и новые значения;
3. понять, какие уровни изменили оценку;
4. не менять автоматически уже принятые уровни.

---

## 9. CLI

Добавить или расширить команды:

```bash
word-content score-words
word-content score-labels
word-content score-quartets
word-content score-all
word-content explain-word-score --word apple
word-content explain-label-score --category birds_of_prey
word-content explain-quartet-score --quartet-id <id>
```

Обязательные параметры:

```text
--db
--config
--scoring-version
--dry-run
--output
```

Команда `explain-*` должна показывать вклад каждого компонента, а не только итоговое число.

---

## 10. Проверки целостности

Добавить проверки:

- `char_count` рассчитан для всех display forms;
- `token_count` рассчитан для всех display forms;
- все scores находятся в диапазоне 0..1;
- отсутствующие familiarity не замаскированы нулём;
- score version заполнена;
- агрегированные quartet scores соответствуют текущим word и label scores;
- invalid / blocked элементы не получают высокий eligibility автоматически;
- генератор действительно применяет выбранный профиль;
- одинаковый seed даёт одинаковый результат.

---

## 11. Тесты

Нужны unit-тесты для:

- короткого знакомого слова;
- длинного знакомого слова;
- короткого редкого слова;
- длинного редкого слова;
- фразы из нескольких слов;
- имени собственного;
- слова с несколькими senses;
- категории с хорошим коротким label;
- категории с широким label;
- категории с неестественной формулировкой;
- четвёрки из четырёх банальных слов;
- четвёрки с одним интересным элементом;
- четвёрки с одним слишком редким элементом;
- профилей easy / fun / hard.

Добавить regression fixtures минимум для 20-30 известных слов и 10-20 category labels.

---

## 12. Экспорт для проверки уровня

В review pack готового уровня показывать для каждого слова:

```text
display text
familiarity
char count
accessibility
novelty
ambiguity
```

Для каждой категории:

```text
label
label quality
quartet quality
quartet interest
minimum word familiarity
maximum word length
warnings
```

Для всего уровня:

```text
average familiarity
minimum familiarity
average accessibility
word length distribution
novel word ratio
long phrase count
ambiguity budget used
average label quality
average quartet interest
difficulty score
solver result
```

Это должно помогать человеку быстро понять, почему уровень получился лёгким, скучным, перегруженным или интересным.

---

## 13. Ограничение human review

Не добавлять human approval к:

- словам;
- senses;
- memberships;
- category concepts;
- category variants;
- quartets;
- scores.

Ручная проверка выполняется для собранного уровня целиком.

Результаты проверки уровня могут:

- отключить плохую четвёрку;
- изменить eligibility;
- добавить warning;
- исправить category label;
- изменить веса scoring model;
- добавить pairing restriction.

Но отсутствие ручной проверки отдельного слова не должно блокировать всю базу.

---

## 14. Порядок реализации

1. Изучить текущую схему и уже существующие scores.
2. Не создавать дублирующие поля, если аналог уже существует.
3. Зафиксировать mapping существующих параметров.
4. Добавить вычислимые word metrics.
5. Добавить category label metrics.
6. Добавить quartet aggregates.
7. Добавить versioned scoring config.
8. Подключить profiles к генератору.
9. Добавить explainability CLI.
10. Добавить integrity checks и тесты.
11. Пересчитать базу.
12. Сформировать before/after отчёт.

---

## 15. Definition of Done

Задача выполнена, когда:

- для каждого слова доступны длина и token count;
- familiarity корректно существует или явно unknown;
- генератор может фильтровать по familiarity и длине;
- для category labels есть отдельная оценка качества;
- для четвёрок есть accessibility, interest и quality scores;
- понятность и интересность не смешаны в одну ось;
- все формулы версионированы;
- scores объяснимы через CLI;
- генератор поддерживает минимум три профиля;
- review pack уровня показывает ключевые quality metrics;
- одинаковый seed и config дают одинаковый результат;
- текущая основная работа по базе не сломана;
- human review остаётся только на уровне готового уровня.
