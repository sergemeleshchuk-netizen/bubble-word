# Рейтинги качества: что уже есть и что добавлено

Документ выполняет шаг 3 задания `prompts/word-db-quality-scoring.md`: до
единой строки кода зафиксировать, какие параметры в базе уже живут, под какими
именами, и что из требований действительно новое.

Правило, по которому принимались решения: **если показатель уже считается,
он переиспользуется под своим именем.** Заводить рядом колонку с тем же
смыслом и другим названием — верный способ получить базу, где одна четвёрка
имеет два разных рейтинга связности и никто не знает, какой главнее.

## Слово

| Требование задания | Что в базе | Решение |
|---|---|---|
| `familiarity_score` | `words.familiarity_score` (zipf / 7, wordfreq) | переиспользуем; `NULL` означает «неизвестно» и уже закрывает связь для игры |
| `char_count` | не было | считается по display form, кэш в `word_scores` |
| `token_count` | не было | то же |
| `display_width_score` | не было | новый, формула в конфиге |
| `spelling_difficulty_score` | не было | новый |
| `ambiguity_score` | косвенно: число `word_senses` и число связей | новый агрегат поверх существующих данных |
| `novelty_score` | не было | новый |
| `accessibility_score` | не было | новый, взвешенная сумма |
| `word_quality_score` | не было | новый, взвешенная сумма |
| `scoring_version` | `quartets.validator_version` — про другое | новый `word_scores.scoring_version` |

Единица оценки — не слово, а **display form**: `rose` (цветок) и `Rose` (имя) —
одна строка в `words`, но разные надписи на экране и разная знакомость.
Поэтому `word_scores` ключуется парой `(word_id, sense_id)`, где `sense_id`
может быть пустым.

## Название категории

| Требование | Что в базе | Решение |
|---|---|---|
| `label_familiarity_score` | не было | новый |
| `label_char_count`, `label_token_count` | не было | считаются по `categories.label` |
| `label_display_width_score` | не было | новый |
| `label_naturalness_score` | не было | новый, эвристика + предупреждения |
| `label_clarity_score` | не было | новый |
| `label_specificity_score` | не было | новый |
| `label_novelty_score` | не было | новый |
| `label_quality_score` | не было | новый агрегат |

Все они складываются в отдельную таблицу `category_label_scores`, а не в
колонки `categories`: это производные значения, пересчитываемые из label
и пулов, и держать их рядом с источником правды означало бы предлагать
править их руками.

## Четвёрка

Здесь больше всего пересечений — и именно здесь легче всего наплодить дубли.

| Требование | Что в базе | Решение |
|---|---|---|
| `semantic_cohesion_score` | **`quartets.cohesion_score`** | то же самое; колонка не переименовывается, формула уточняется (штраф за слабое звено) |
| `avg_word_familiarity` | **`quartets.familiarity_score`** | то же самое, имя оставлено |
| `quartet_ambiguity_score` | **`quartets.ambiguity_pressure`** | то же самое, имя оставлено |
| `difficulty_score` | **`quartets.difficulty`** | то же самое |
| `label_quality_score` на четвёрке | считается для категории | не дублируем: берётся из `category_label_scores` через `category_id` |
| `min_word_familiarity` | не было | новая колонка |
| `avg_word_accessibility`, `min_word_accessibility` | не было | новые |
| `avg_word_length`, `max_word_length` | не было | новые |
| `quartet_clarity_score` | не было | новая |
| `quartet_novelty_score` | не было | новая |
| `quartet_interest_score` | не было | новая |
| `quartet_quality_score` | не было | новая |
| `scoring_version` | `validator_version` — про валидаторы | новая `scoring_version` |

Три существующих поля (`cohesion_score`, `familiarity_score`,
`ambiguity_pressure`) до этой работы считались прямо в `quartet_builder`.
Теперь их считает `scoring.py`, а сборщик его вызывает: иначе одна и та же
величина имела бы два вычисления, которые разъедутся при первой же правке.

## Что не делается

- **Ручного подтверждения нет ни на одном уровне рейтингов.** Score — это
  результат формулы, а не мнение. Ручная оценка остаётся на собранном уровне.
- **`word_quality_score` не становится единственным фильтром.** Профили
  генерации фильтруют по отдельным параметрам; общий рейтинг только сортирует.
- **`char_count` и `token_count` не пишутся руками.** Это кэш, полностью
  пересчитываемый из canonical display form командой `score-words`.
- **Второй словарь статусов не заводится.** Пригодность связи по-прежнему
  `review_status`, машинная валидность — `validation_state`, рейтинги живут
  отдельной осью и ни на что не влияют, пока их не спросит профиль генерации.

## Версионирование

Три независимые версии формул, каждая в конфиге и в кэше:

```text
word_scoring_version     -> word_scores.scoring_version
label_scoring_version    -> category_label_scores.scoring_version
quartet_scoring_version  -> quartets.scoring_version
```

Смена версии в `data/content/scoring_config.yaml` делает старый кэш
устаревшим, что видно проверкой целостности. Пересчёт — `score-all`.
Уже принятые уровни не меняются: их состав зафиксирован `content_hash`,
а рейтинги на принятый уровень не влияют.
