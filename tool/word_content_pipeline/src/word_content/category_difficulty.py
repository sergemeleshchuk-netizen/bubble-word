"""Сложность самой категории, выведенная из данных, а не написанная автором.

Зачем шаг существует. Поле `categories.base_difficulty` заполняет источник
контента (сид или прогон AI) одним числом «на глаз». Замер 02.08 показал, что
это число не связано с содержимым категории: его корреляция со знакомостью слов
пула −0.25, с долей имён собственных +0.03. То есть COMPOSERS и VOLCANOES
(пул целиком из имён собственных, знакомость 0.42) получили ту же оценку 0.4,
что и `___ MAN` из бытовых слов. Генератор фильтрует туториал по этому полю
(`categoryFitsGates`) и предпочитает простые категории по нему же
(`simpleBonus`) — то есть фильтрует по шуму. Отсюда THE MIND (0.5) в первом
уровне сдаваемого пакета при наличии COLORS и FRUITS.

Что мерим. Не «трудность темы» вообще, а один конкретный вопрос: **сможет ли
игрок назвать эту категорию, глядя на четвёрку её слов**. Он раскладывается на
три наблюдаемых величины:

1. `obviousness_score` связи — вспомнит ли игрок это значение слова первым.
   Главный вклад: ровно он отличает COLORS (0.95) от RICE TYPES (0.68), где
   слова `black / red / white / wild` частотные, но надпись по ним не читается.
2. `words.familiarity_score` — знакомо ли само слово. Второй по весу: он ловит
   редкие слова вроде `quail` и `obituary`, из-за которых уровень читается
   как справочник.
3. Тип правила (`rule_type`) — перечисление (`taxonomy_instances`) читается
   легче, чем ассоциативный хаб, где связь надо угадать.

Доля имён собственных СОЗНАТЕЛЬНО не штрафуется — см. блок про W_PROPER_NOUN
ниже. Узнаваемое название это качество контента, а не сложность.

Плюс надбавка за шаблон `___ MAN`: слова там бытовые, но механика
«подставь слово» для новичка отдельная трудность, и знакомость её не видит.

Чего шаг НЕ делает. Он не трогает `base_difficulty`: авторское число остаётся
на месте как вход источника, а результат пишется в `derived_difficulty`. Так
пересчёт обратим и сравним с авторской оценкой в любой момент.

Честная граница. `obviousness_score` у 93% связей тоже поставлен вручную
(`source = seed_manual`), то есть это не измерение игроков, а более удачная
экспертная оценка: на якорных категориях она ранжирует верно, а
`base_difficulty` — нет. Заменить её настоящими данными сможет только
телеметрия win rate; называть нынешнее число прогнозом было бы враньём.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass

MODEL_VERSION = "category-difficulty/1.0"

# Слова, которые игрок увидит в обычном уровне
NORMAL_STATUSES = ("approved", "alternative")

# Четвёрка — размер категории в уровне; сложность считаем по той четвёрке,
# которую генератор реально возьмёт, а не по всему пулу.
QUARTET_SIZE = 4

# Категории, добитые из записи референса, оценку не получают.
#
# Их 21, у каждой пул ровно четыре слова и авторской оценки нет вовсе — это
# слепок авторской группы, а не контентный пул. Пока `d` у них был NULL,
# `simpleBonus` в генераторе их не касался (он пропускает difficulty === null).
# Первый прогон 02.08 выдал им число, они поднялись в отборе — и уровень 102
# декады 101 перестал сходиться: категория ровно с четырьмя словами проваливает
# точное покрытие при первом же пересечении, о чём и предупреждает комментарий
# в `buildPool`. Оценка без пула — это оценка шума, поэтому их место здесь.
REFERENCE_ORIGIN = "reference_backfill"

# Вклады. Сумма весов больше 1: число всё равно обрезается по 1.0, а разносить
# их до ровной суммы значило бы подгонять веса под арифметику, а не под якоря.
W_OBVIOUSNESS = 0.60   # читается ли надпись по словам — главное
W_FAMILIARITY = 0.25   # знакомы ли сами слова
W_BLANK_LABEL = 0.12   # шаблон «___ MAN» — отдельная механика

# Штрафа за имена собственные здесь нет, и это решение стороны игры, а не
# упущение. Первая версия штрафовала долю имён собственных в пуле — на этом
# COMPOSERS, VOLCANOES и FAMOUS PAINTERS уехали с 0.35-0.4 на 0.45-0.55, а
# MONTHS (January и прочие формально имена собственные) выпали из туториала.
# Решение владельца продукта: узнаваемые названия — брендов, игр, месяцев — это
# КАЧЕСТВЕННЫЙ контент, «на слуху у игрока», а не признак трудной категории.
# Трудным слово делает редкость, а не заглавная буква: `quail` (zipf 3.13) и
# `obituary` (3.41) — обычные слова, и мешают они куда сильнее, чем `January`.
# Редкость ловится слагаемым W_FAMILIARITY и порогом частотности в генераторе.

# Насколько тип правила добавляет работы игроку сверх узнавания слов.
# Перечисление — ноль: увидел четыре птицы, назвал «птицы».
RULE_TYPE_COST = {
    "taxonomy_instances": 0.00,
    "components": 0.01,
    "functional_group": 0.03,
    "property_group": 0.05,
    "context_hub": 0.07,
    "association_hub": 0.10,
    "structured_set": 0.12,
    "sequence": 0.12,
    "meta_collector": 0.10,
    "unclassified": 0.07,
}
RULE_TYPE_DEFAULT = 0.07

# Отбор четвёрки внутри пула: генератор берёт слова, которые и очевидны, и
# знакомы. Пропорция та же, что у весов сложности.
PICK_OBVIOUSNESS = 0.6
PICK_FAMILIARITY = 0.4

# Значения по умолчанию, когда оценки нет вовсе. Берём середину наблюдённого
# разброса, чтобы отсутствие данных не читалось ни как «легко», ни как «трудно».
DEFAULT_OBVIOUSNESS = 0.5
DEFAULT_FAMILIARITY = 0.4

# Границы полос. Названия те же, что в отчётах по пакетам.
BANDS = (
    ("easy", 0.20),
    ("light", 0.30),
    ("medium", 0.45),
    ("hard", 1.01),
)


@dataclass(frozen=True)
class CategoryFacts:
    """Всё, из чего считается сложность категории."""

    category_id: int
    category_key: str
    label: str
    rule_type: str
    authored: float | None
    # (obviousness, familiarity) по каждой связи пула
    pool: tuple[tuple[float, float], ...]
    proper_noun_share: float

    @property
    def quartet(self) -> tuple[tuple[float, float], ...]:
        """Четвёрка, которую возьмёт генератор: самые очевидные знакомые слова."""
        ranked = sorted(
            self.pool,
            key=lambda pair: -(PICK_OBVIOUSNESS * pair[0] + PICK_FAMILIARITY * pair[1]),
        )
        return tuple(ranked[:QUARTET_SIZE])

    @property
    def quartet_obviousness(self) -> float:
        picked = self.quartet
        return sum(o for o, _ in picked) / len(picked) if picked else DEFAULT_OBVIOUSNESS

    @property
    def quartet_familiarity(self) -> float:
        picked = self.quartet
        return sum(f for _, f in picked) / len(picked) if picked else DEFAULT_FAMILIARITY


def band(value: float) -> str:
    for name, ceiling in BANDS:
        if value <= ceiling:
            return name
    return BANDS[-1][0]


def score(facts: CategoryFacts) -> tuple[float, str]:
    """Возвращает (сложность 0..1, объяснение человекочитаемым текстом)."""
    obviousness = facts.quartet_obviousness
    familiarity = facts.quartet_familiarity

    parts: list[tuple[str, float]] = [
        (f"надпись по словам (обвиус {obviousness:.2f})", W_OBVIOUSNESS * (1 - obviousness)),
        (f"знакомость слов ({familiarity:.2f})", W_FAMILIARITY * (1 - familiarity)),
    ]
    rule_cost = RULE_TYPE_COST.get(facts.rule_type, RULE_TYPE_DEFAULT)
    if rule_cost:
        parts.append((f"тип правила ({facts.rule_type})", rule_cost))
    if "___" in facts.label:
        parts.append(("шаблон «___» — отдельная механика", W_BLANK_LABEL))

    total = min(1.0, max(0.0, sum(value for _, value in parts)))
    top = sorted(parts, key=lambda p: -p[1])[:2]
    explanation = f"{band(total)}: " + ", ".join(f"{name} +{value:.2f}" for name, value in top)
    return round(total, 3), explanation


def category_facts(conn: sqlite3.Connection) -> list[CategoryFacts]:
    statuses = ", ".join(f"'{name}'" for name in NORMAL_STATUSES)
    rows = conn.execute(
        f"""
        SELECT c.id                AS category_id,
               c.category_key      AS category_key,
               c.label             AS label,
               c.rule_type         AS rule_type,
               c.base_difficulty   AS authored,
               COUNT(m.id)         AS pool_size,
               AVG(w.is_proper_noun) AS proper_noun_share,
               GROUP_CONCAT(
                   COALESCE(m.obviousness_score, {DEFAULT_OBVIOUSNESS}) || ':' ||
                   COALESCE(w.familiarity_score, {DEFAULT_FAMILIARITY}), '|'
               ) AS pool
          FROM categories c
          JOIN memberships m ON m.category_id = c.id
                            AND m.review_status IN ({statuses})
                            AND m.semantic_status <> 'incorrect'
          JOIN words w ON w.id = m.word_id
         WHERE c.status = 'active'
           AND c.origin <> '{REFERENCE_ORIGIN}'
         GROUP BY c.id
        HAVING pool_size >= {QUARTET_SIZE}
         ORDER BY c.category_key
        """
    )
    facts: list[CategoryFacts] = []
    for row in rows:
        pool = tuple(
            (float(chunk.split(":")[0]), float(chunk.split(":")[1]))
            for chunk in row["pool"].split("|")
        )
        facts.append(
            CategoryFacts(
                category_id=int(row["category_id"]),
                category_key=row["category_key"],
                label=row["label"],
                rule_type=row["rule_type"],
                authored=row["authored"],
                pool=pool,
                proper_noun_share=float(row["proper_noun_share"] or 0.0),
            )
        )
    return facts


def calibrate_to_authored(
    raw: list[tuple[int, float]], authored: list[float]
) -> dict[int, float]:
    """Кладёт выведенный порядок на авторскую шкалу, сохраняя её распределение.

    Зачем. От авторского числа нам нужно было исправить **порядок** категорий, а
    не диапазон. Первый прогон 02.08 менял и то и другое, и это уронило блок:
    потолки декад (0.35 → 0.60), делитель `simpleBonus` (0.25) и гейт туториала
    (0.20) в `decadeProfiles.ts` подобраны замерами под авторскую шкалу. На
    сырой шкале у декад с потолком 0.48+ бонус за простоту упирался в максимум
    почти у всех кандидатов, ничьи стал разрешать бонус за частотность слов — а
    самые частотные слова общие для десятков категорий. Уровень 102 (7 категорий
    при 4 мета-связях, самый тесный в декаде) перестал сходиться по точному
    покрытию: 48 попыток из 48.

    Поэтому результат — перестановка: каждая категория получает то значение из
    авторского набора, которое соответствует её месту в выведенном порядке.
    Гистограмма шкалы остаётся ровно той же, что была, меняется только адресат.
    Сырая величина сохраняется рядом (`derived_difficulty_raw`) — по ней видно,
    насколько порядок разошёлся с авторским.
    """
    if not authored:
        return {category_id: value for category_id, value in raw}
    target = sorted(authored)
    ordered = sorted(raw, key=lambda pair: pair[1])
    last = len(ordered) - 1
    result: dict[int, float] = {}
    for position, (category_id, _) in enumerate(ordered):
        # доля position/last, взятая по индексам целевого набора
        at = 0 if last == 0 else round(position * (len(target) - 1) / last)
        result[category_id] = target[at]
    return result


def ensure_columns(conn: sqlite3.Connection) -> list[str]:
    """Добавляет колонки результата, если их ещё нет.

    Шаг сознательно не идёт через `migrations.py`: на 02.08 база стоит на
    версии схемы 6, а в коде лежит неприменённый шаг 7 (`sense_accessibility`) —
    крупная перестройка слоя значений. Запустить `migrate` ради двух колонок
    значило бы протащить её заодно. Колонки аддитивные и идемпотентные, поэтому
    их место здесь, а перенос в общий механизм — вместе с решением по шагу 7.
    """
    existing = {row[1] for row in conn.execute("PRAGMA table_info(categories)")}
    added: list[str] = []
    for column, definition in (
        ("derived_difficulty", "REAL NULL"),
        ("derived_difficulty_raw", "REAL NULL"),
        ("derived_difficulty_reason", "TEXT NULL"),
        ("derived_difficulty_version", "TEXT NULL"),
    ):
        if column not in existing:
            conn.execute(f"ALTER TABLE categories ADD COLUMN {column} {definition}")
            added.append(column)
    return added


def derive(conn: sqlite3.Connection) -> dict[str, int]:
    """Пересчитывает сложность всем активным категориям. Возвращает сводку по полосам."""
    ensure_columns(conn)
    # Сначала снимаем прежний результат со всех: иначе категория, выпавшая из
    # выборки (ушла в reference_backfill, обмелел пул), сохранит устаревшее
    # число, и повторный прогон перестанет быть идемпотентным.
    conn.execute(
        "UPDATE categories SET derived_difficulty = NULL, derived_difficulty_raw = NULL, "
        "derived_difficulty_reason = NULL, derived_difficulty_version = NULL"
    )
    facts = category_facts(conn)
    scored = [(item.category_id, *score(item)) for item in facts]
    calibrated = calibrate_to_authored(
        [(category_id, value) for category_id, value, _ in scored],
        [item.authored for item in facts if item.authored is not None],
    )

    summary: dict[str, int] = {name: 0 for name, _ in BANDS}
    for category_id, raw, reason in scored:
        value = calibrated[category_id]
        conn.execute(
            """
            UPDATE categories
               SET derived_difficulty = ?, derived_difficulty_raw = ?,
                   derived_difficulty_reason = ?, derived_difficulty_version = ?
             WHERE id = ?
            """,
            (value, raw, reason, MODEL_VERSION, category_id),
        )
        summary[band(value)] += 1
    return summary
