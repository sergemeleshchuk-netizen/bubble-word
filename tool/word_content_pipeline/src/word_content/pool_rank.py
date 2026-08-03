"""Ранжирование широкого пула категории по популярности слов.

Зачем это понадобилось. Наша база и данные оригинала устроены по-разному:
у оригинала категория И ЕСТЬ четвёрка (медиана пула 4.0, ровно четыре слова
в 74% категорий), у нас медиана пула 13.0 и шире четырёх — 86% категорий.
То есть у оригинала выбирать не из чего, а у нас каждый уровень выбирает
4 слова из 13, и до этого выбор делала формула отбора в генераторе.

Чем плох был выбор формулой. Она оценивала слово БЛИЗОСТЬЮ его частотности
к целевой медиане декады, поэтому самые расхожие слова категории проигрывали
за то, что слишком частотные. Замеренные последствия: в UNITS OF TIME на
первый уровень уезжало `instant` (zipf 4.34, в 0.01 от цели 4.35), а `year`
5.96 и `day` 5.95 оказывались в конце очереди; в COMPASS собиралось
`rose / heading / housing / dial` вместо `north / south / west / rose`.
Та же формула на словаре оригинала даёт тот же брак — дело не в базе.

Что делает этот модуль. Один раз, на стороне базы, раскладывает пул каждой
категории от самого популярного слова к самому редкому и раздаёт готовым
четвёркам тир easy / medium / hard по их месту в этом порядке. Дальше
генератору не надо ничего выводить формулой: он берёт четвёрку нужного тира.

Почему ранг ОТНОСИТЕЛЬНЫЙ, внутри категории, а не абсолютный по частотности.
Абсолютные пороги дают перекос: усреднение четырёх рангов стягивает всё к
середине, и на замере 11 938 четвёрок абсолютные полосы разложились как
70% medium против 20% easy и 10% hard. Категория при этом остаётся без
выбора: у «тихой» категории нет ни одной четвёрки в easy, у «громкой» — ни
одной в hard. Относительный ранг гарантирует, что у КАЖДОГО широкого пула
есть и лёгкая четвёрка, и трудная — а насколько трудна сама категория,
говорит отдельная ось `categories.base_difficulty`. Абсолютное число тоже
сохраняется (`pool_rank_avg`), чтобы вторая ось считалась из него, а не
восстанавливалась заново.

Почему популярность берётся из `words.familiarity_score`, а не из wordfreq.
Это одно и то же: корреляция замерена на 10 475 словах и равна 0.998.
Но familiarity_score лежит в базе, а zipf считается только при выгрузке
снимка, — значит ранг остаётся свойством базы и не зависит от внешней
библиотеки. Имена собственные при этом не проваливаются: их средняя
частотность (3.56) совпадает со средней у нарицательных.

Категории с пулом ровно в 4 слова не ранжируются: там одна возможная
четвёрка, выбирать не из чего, и тир у неё `unranked`.
"""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from statistics import mean

# Границы тиров по МЕСТУ четвёрки в порядке своей категории: 0.0 — самая
# популярная четвёрка пула, 1.0 — самая редкая.
#
# easy и medium намеренно перекрываются на 0.25-0.40 (решение 03.08): граница
# между «лёгкой» и «средней» четвёркой не резкая, и жёсткий срез заставлял бы
# генератор брать соседнюю четвёрку через пропасть, когда нужная занята
# запретом на повтор. Полоса перекрытия — 15% позиций, на замере в неё попадает
# 11% четвёрок. hard не перекрывается ни с чем: трудная четвёрка обязана быть
# трудной, иначе тир перестаёт что-либо обещать.
EASY_MAX = 0.40
MEDIUM_MIN = 0.25
MEDIUM_MAX = 0.75

TIERS = ("easy", "medium", "hard")
UNRANKED = "unranked"

# Пул, из которого нечего выбирать: четвёрка ровно одна.
MIN_WIDE_POOL = 5


@dataclass(frozen=True)
class RankSummary:
    categories_ranked: int
    categories_skipped: int
    words_ranked: int
    quartets_ranked: int
    quartets_unranked: int
    by_tier: dict[str, int]
    overlap: int


def _word_ranks(conn: sqlite3.Connection) -> tuple[dict[tuple[int, int], float],
                                                   dict[int, int],
                                                   list[tuple[int, int, int, float]]]:
    """Место каждого approved-слова в пуле своей категории.

    Возвращает (ранг по паре категория-слово, размер пула, строки для записи).
    Ранг нормирован: 0.0 — самое популярное слово пула, 1.0 — самое редкое.

    Пул — только approved-связи: именно их читает отбор слов в генераторе.
    `alternative` и `hard_only` в пул не входят, они материал для ловушек и
    для отдельных сложных уровней.
    """
    pools: dict[int, list[tuple[float, int, str, int]]] = defaultdict(list)
    for row in conn.execute(
        "SELECT m.id, m.category_id, m.word_id, w.text, w.familiarity_score "
        "FROM memberships m JOIN words w ON w.id = m.word_id "
        "WHERE m.review_status = 'approved'"
    ):
        # familiarity_score пуст у 28 слов из 10 503. Ставим -1, то есть в самый
        # хвост: неизвестная популярность — не повод считать слово расхожим.
        score = row["familiarity_score"] if row["familiarity_score"] is not None else -1.0
        pools[row["category_id"]].append((score, row["id"], row["text"], row["word_id"]))

    ranks: dict[tuple[int, int], float] = {}
    sizes: dict[int, int] = {}
    rows: list[tuple[int, int, int, float]] = []
    for category_id, words in pools.items():
        sizes[category_id] = len(words)
        if len(words) < MIN_WIDE_POOL:
            continue
        # Порядок детерминирован до последнего слова: популярность, затем более
        # короткое слово, затем алфавит. Без этого пересчёт тасовал бы равные.
        words.sort(key=lambda item: (-item[0], len(item[2]), item[2]))
        last = len(words) - 1
        for position, (_, membership_id, _, word_id) in enumerate(words):
            pct = position / last if last else 0.0
            ranks[(category_id, word_id)] = pct
            rows.append((membership_id, position + 1, len(words), pct))
    return ranks, sizes, rows


def _tiers_for(position: float) -> tuple[str, list[str]]:
    """Тир по месту четвёрки в своей категории: первичный и полный набор.

    Первичный тир всегда входит в набор — иначе выгрузка и глаз читали бы
    разное.
    """
    members = []
    if position <= EASY_MAX:
        members.append("easy")
    if MEDIUM_MIN < position <= MEDIUM_MAX:
        members.append("medium")
    if position > MEDIUM_MAX:
        members.append("hard")
    if position <= EASY_MAX:
        primary = "easy"
    elif position <= MEDIUM_MAX:
        primary = "medium"
    else:
        primary = "hard"
    return primary, members


def rank(conn: sqlite3.Connection) -> RankSummary:
    """Пересчитывает ранги слов и тиры четвёрок. Идемпотентна."""
    ranks, sizes, word_rows = _word_ranks(conn)

    conn.execute("UPDATE memberships SET pool_rank = NULL, pool_size = NULL, "
                 "pool_rank_pct = NULL")
    conn.executemany(
        "UPDATE memberships SET pool_rank = ?, pool_size = ?, pool_rank_pct = ? WHERE id = ?",
        [(rank_no, size, pct, membership_id)
         for membership_id, rank_no, size, pct in word_rows],
    )

    quartets: dict[int, list[int]] = defaultdict(list)
    category_of: dict[int, int] = {}
    for row in conn.execute(
        "SELECT q.id, q.category_id, qw.word_id FROM quartets q "
        "JOIN quartet_words qw ON qw.quartet_id = q.id"
    ):
        quartets[row["id"]].append(row["word_id"])
        category_of[row["id"]] = row["category_id"]

    # Средний ранг четвёрки — абсолютная величина: где её слова лежат в пуле.
    by_category: dict[int, list[tuple[float, int]]] = defaultdict(list)
    unranked: list[int] = []
    for quartet_id, words in quartets.items():
        category_id = category_of[quartet_id]
        if sizes.get(category_id, 0) < MIN_WIDE_POOL:
            unranked.append(quartet_id)
            continue
        # Слово вне approved-пула (alternative или hard_only) — 7% на замере.
        # Считаем его самым редким: в пуле, из которого выбирает генератор,
        # его нет вовсе, и делать вид, что оно среднее, было бы поблажкой.
        by_category[category_id].append(
            (mean(ranks.get((category_id, word), 1.0) for word in words), quartet_id))

    updates: list[tuple[str, str, float, float, int]] = []
    by_tier = {tier: 0 for tier in TIERS}
    overlap = 0
    for _, entries in by_category.items():
        entries.sort()
        last = len(entries) - 1
        for index, (rank_avg, quartet_id) in enumerate(entries):
            position = index / last if last else 0.0
            primary, members = _tiers_for(position)
            by_tier[primary] += 1
            if len(members) > 1:
                overlap += 1
            updates.append((primary, ",".join(members), position, rank_avg, quartet_id))

    conn.executemany(
        "UPDATE quartets SET difficulty_tier = ?, pool_tiers = ?, "
        "pool_position = ?, pool_rank_avg = ? WHERE id = ?",
        updates,
    )
    conn.executemany(
        "UPDATE quartets SET difficulty_tier = ?, pool_tiers = NULL, "
        "pool_position = NULL, pool_rank_avg = NULL WHERE id = ?",
        [(UNRANKED, quartet_id) for quartet_id in unranked],
    )

    return RankSummary(
        categories_ranked=len(by_category),
        categories_skipped=sum(1 for size in sizes.values() if size < MIN_WIDE_POOL),
        words_ranked=len(word_rows),
        quartets_ranked=len(updates),
        quartets_unranked=len(unranked),
        by_tier=by_tier,
        overlap=overlap,
    )
