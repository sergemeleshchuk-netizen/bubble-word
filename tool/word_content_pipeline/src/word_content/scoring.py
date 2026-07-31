"""Рейтинги качества слов, названий категорий и четвёрок.

Главный принцип: **не один непрозрачный рейтинг, а измеримые параметры плюс
версионируемая формула поверх них.** Если хранить только общий балл, невозможно
ответить на вопрос «уровень скучный или перегруженный» — оба случая дают
средний балл, и оба выглядят одинаково.

Поэтому разведены оси, которые постоянно путают:

  * знакомость — знает ли игрок слово;
  * читаемость и длина — влезает ли слово в пузырь;
  * ясность — понятно ли, почему эти четыре слова вместе;
  * неоднозначность — тянет ли слово в соседнюю категорию (это не всегда плохо:
    ровно из этого делаются ловушки);
  * интересность — есть ли «ага»-момент;
  * сложность.

Понятность и интересность намеренно **не** складываются в одну ось. Уровень из
четырёх самых частотных слов максимально понятен и совершенно скучен.

Ни один score не является мнением человека. Это результат формулы, версия
которой сохраняется вместе со значением.
"""

from __future__ import annotations

import math
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from . import flat_config
from .db import utc_now

DEFAULTS: dict[str, float] = {
    "word_scoring_version": 1,
    "label_scoring_version": 2,
    "quartet_scoring_version": 1,
    "word_display_comfort_chars": 8,
    "word_display_limit_chars": 16,
    "word_display_space_cost": 0.6,
    "word_display_token_cost": 1.5,
    "word_rare_familiarity": 0.43,
    "word_common_familiarity": 0.72,
    "novelty_spread_factor": 0.45,
    "accessibility_familiarity_weight": 0.55,
    "accessibility_display_weight": 0.20,
    "accessibility_brevity_weight": 0.15,
    "accessibility_spelling_weight": 0.10,
    "word_quality_accessibility_weight": 0.55,
    "word_quality_semantic_weight": 0.20,
    "word_quality_novelty_weight": 0.25,
    "word_quality_risk_penalty": 0.25,
    "word_quality_display_penalty": 0.30,
    "label_display_comfort_chars": 14,
    "label_display_limit_chars": 28,
    "label_quality_naturalness_weight": 0.20,
    "label_quality_clarity_weight": 0.30,
    "label_quality_naturalness_floor": 0.35,
    "label_quality_retrospective_weight": 0.20,
    "label_quality_reveal_weight": 0.10,
    "label_quality_display_weight": 0.10,
    "label_quality_familiarity_weight": 0.10,
    "cohesion_weakest_link_weight": 0.45,
    "quartet_interest_novelty_weight": 0.40,
    "quartet_interest_diversity_weight": 0.20,
    "quartet_interest_elegance_weight": 0.20,
    "quartet_interest_label_weight": 0.20,
    "quartet_interest_obscurity_penalty": 0.35,
    "quartet_quality_cohesion_weight": 0.30,
    "quartet_quality_accessibility_weight": 0.30,
    "quartet_quality_clarity_weight": 0.20,
    "quartet_quality_label_weight": 0.20,
}


def default_path() -> Path | None:
    return flat_config.find_upwards("data/content/scoring_config.yaml")


def load_config(path: Path | str | None = None) -> dict[str, float]:
    return flat_config.load(Path(path) if path else default_path(), DEFAULTS)


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass
class Explained:
    """Итог и вклад каждого компонента — чтобы балл можно было объяснить."""

    score: float
    parts: dict[str, float] = field(default_factory=dict)

    def rounded(self) -> float:
        return round(self.score, 4)


# =========================================================================== слово

# Широкие буквы занимают заметно больше места, узкие — заметно меньше.
# Приближение достаточное, чтобы отличить `illinois` от `wombat`.
WIDE_LETTERS = set("mwMW@%")
NARROW_LETTERS = set("iljItf.,;:'!|")
# Буквосочетания, на которых спотыкается чтение вслух.
HARD_CLUSTERS = ("ough", "eigh", "sch", "phth", "gn", "kn", "ps", "rh", "xh", "cz", "zh")
VOWELS = set("aeiouy")
_TOKEN_RE = re.compile(r"[\s\-/]+")


def display_metrics(display: str, config: dict[str, float]) -> dict[str, float]:
    """Длина, число слов и оценка вместимости надписи в пузырь.

    Считается по canonical display form, без служебных суффиксов значения:
    игрок видит `rose`, а не `rose#rose_flower`.
    """
    text = display.strip()
    char_count = len(text)
    token_count = len([part for part in _TOKEN_RE.split(text) if part])

    # Ширина в условных единицах: широкая буква считается за 1.4, узкая за 0.6,
    # пробел и дефис — за настраиваемую долю, потому что читаются легче буквы.
    width = 0.0
    for char in text:
        if char in WIDE_LETTERS:
            width += 1.4
        elif char in NARROW_LETTERS:
            width += 0.6
        elif char.isspace() or char == "-":
            width += config["word_display_space_cost"]
        elif char.isupper():
            width += 1.2
        else:
            width += 1.0

    # Каждое лишнее слово в надписи — отдельный штраф, а не просто лишние буквы.
    # `hot air balloon` и `refrigerator` близки по длине, но на пузыре ведут себя
    # по-разному: фраза требует переноса и читается как несколько подписей.
    width += config["word_display_token_cost"] * max(0, token_count - 1)

    comfort = config["word_display_comfort_chars"]
    limit = config["word_display_limit_chars"]
    if width <= comfort:
        display_width_score = 1.0
    elif width >= limit:
        display_width_score = 0.0
    else:
        display_width_score = (limit - width) / (limit - comfort)

    return {
        "char_count": float(char_count),
        "token_count": float(token_count),
        "display_units": round(width, 2),
        "display_width_score": round(clamp(display_width_score), 4),
    }


def spelling_difficulty(display: str, is_proper_noun: bool) -> float:
    """Насколько слово трудно прочитать и написать. 0 — легко, 1 — тяжело."""
    text = display.strip().lower()
    if not text:
        return 1.0
    score = 0.0

    letters = [c for c in text if c.isalpha()]
    if len(letters) > 10:
        score += 0.2
    if len(letters) > 14:
        score += 0.15

    score += 0.20 * sum(1 for cluster in HARD_CLUSTERS if cluster in text)

    # Диакритика: после NFKC она остаётся отдельным знаком или составным символом.
    if any(ord(char) > 127 for char in text):
        score += 0.25

    # Скопление согласных подряд — верный признак трудного чтения.
    run = 0
    longest = 0
    for char in text:
        if char.isalpha() and char not in VOWELS:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    if longest >= 4:
        score += 0.2
    elif longest == 3:
        score += 0.1

    # Аббревиатуры: три и более заглавных подряд в исходном написании.
    if re.search(r"[A-Z]{3,}", display):
        score += 0.2
    if is_proper_noun and len(letters) > 8:
        score += 0.1

    return round(clamp(score), 4)


def novelty(familiarity: float | None, config: dict[str, float]) -> float:
    """Ощущение свежести слова. Новизна — не то же самое, что редкость.

    Банальное слово даёт низкую новизну. Крайне редкое — тоже: игрок его просто
    не знает, и никакого «ага» не происходит. Пик приходится на слова, которые
    игрок знает, но встречает нечасто.
    """
    if familiarity is None:
        return 0.0
    rare = config["word_rare_familiarity"]
    common = config["word_common_familiarity"]
    peak = (rare + common) / 2
    spread = max(common - rare, 0.05) * config["novelty_spread_factor"]
    return round(clamp(math.exp(-(((familiarity - peak) / spread) ** 2))), 4)


def ambiguity(sense_count: int, membership_count: int, theme_count: int) -> float:
    """Насколько слово тянет в разные стороны внутри базы.

    Это не штраф: управляемая неоднозначность — материал для ловушек.
    Параметр отдельный именно поэтому.
    """
    senses = min(sense_count, 5) / 5
    memberships = min(membership_count, 12) / 12
    themes = min(theme_count, 6) / 6
    return round(clamp(0.35 * senses + 0.35 * memberships + 0.30 * themes), 4)


def accessibility(
    *,
    familiarity: float | None,
    display_width_score: float,
    char_count: float,
    spelling_difficulty_score: float,
    config: dict[str, float],
) -> Explained:
    """Итоговая лёгкость восприятия. Неизвестная знакомость считается нулевой."""
    brevity = clamp(1.0 - (char_count - 4) / 12)
    parts = {
        "familiarity": round(
            config["accessibility_familiarity_weight"] * (familiarity or 0.0), 4
        ),
        "display_width": round(
            config["accessibility_display_weight"] * display_width_score, 4
        ),
        "brevity": round(config["accessibility_brevity_weight"] * brevity, 4),
        "spelling_simplicity": round(
            config["accessibility_spelling_weight"] * (1.0 - spelling_difficulty_score), 4
        ),
    }
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def word_quality(
    *,
    accessibility_score: float,
    semantic_usefulness: float,
    novelty_score: float,
    risk_flagged: bool,
    display_width_score: float,
    config: dict[str, float],
) -> Explained:
    """Пригодность слова генератору. Один из критериев, а не единственный."""
    parts = {
        "accessibility": round(
            config["word_quality_accessibility_weight"] * accessibility_score, 4
        ),
        "semantic_usefulness": round(
            config["word_quality_semantic_weight"] * semantic_usefulness, 4
        ),
        "controlled_novelty": round(
            config["word_quality_novelty_weight"] * novelty_score, 4
        ),
    }
    if risk_flagged:
        parts["risk_penalty"] = -round(config["word_quality_risk_penalty"], 4)
    if display_width_score < 0.2:
        parts["display_penalty"] = -round(config["word_quality_display_penalty"], 4)
    return Explained(score=clamp(sum(parts.values())), parts=parts)


# ================================================================ название категории

# Слова, из-за которых название ничего не объясняет игроку.
VAGUE_WORDS = frozenset(
    {
        "misc", "miscellaneous", "other", "others", "related", "special", "various",
        "assorted", "general", "stuff", "items", "things", "words", "terms",
    }
)
# Широкие названия. ВАЖНО: это описательный список, а не список плохих слов.
#
# Прежняя формула штрафовала широкую надпись как «принцип не сужен», и это было
# настроено прямо против референса. Оригинал массово использует короткие широкие
# ярлыки: FOOD, SCHOOL, DOCTOR, BIRD, TREE, CAT — и они работают, потому что
# надпись здесь не подсказка, а финальный reveal. Игрок видит четыре слова и
# только потом короткое слово, объясняющее, что это было.
#
# Поэтому охват стал характеристикой (`label_scope`), а не штрафом. Список
# используется только для того, чтобы эту характеристику назвать.
BROAD_WORDS = frozenset(
    {
        "animals", "food", "objects", "people", "places", "colors", "colours",
        "nature", "school", "doctor", "bird", "tree", "cat", "dog", "music",
        "sports", "jobs", "weather", "house", "body", "space", "water", "time",
    }
)


def label_metrics(label: str, config: dict[str, float]) -> dict[str, float]:
    text = label.strip()
    tokens = [part for part in _TOKEN_RE.split(text) if part]
    comfort = config["label_display_comfort_chars"]
    limit = config["label_display_limit_chars"]
    length = len(text)
    if length <= comfort:
        width_score = 1.0
    elif length >= limit:
        width_score = 0.0
    else:
        width_score = (limit - length) / (limit - comfort)
    return {
        "label_char_count": float(length),
        "label_token_count": float(len(tokens)),
        "label_display_width_score": round(clamp(width_score), 4),
    }


def label_clarity(label: str) -> Explained:
    """Помогает ли название понять принцип группы после её решения."""
    lowered = label.strip().lower()
    words = [w for w in _TOKEN_RE.split(lowered) if w]
    parts = {"base": 1.0}
    vague = [w for w in words if w in VAGUE_WORDS]
    # `THINGS THAT MELT` — конкретно, `RELATED THINGS` — нет: решает не слово
    # `things`, а наличие уточнения после него.
    meaningful = [w for w in words if w not in VAGUE_WORDS]
    if vague and not meaningful:
        parts["vague_only"] = -0.7
    elif vague and len(meaningful) < 2:
        parts["vague_head"] = -0.25
    if not words:
        parts["empty"] = -1.0
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def label_scope(label: str, pool_size: int) -> str:
    """Охват надписи: broad | medium | narrow. Характеристика, а не оценка.

    Отдельная функция именно для того, чтобы охват нельзя было случайно
    превратить в штраф: она возвращает строку, а не число, и в формулу
    качества не входит.
    """
    words = [w for w in _TOKEN_RE.split(label.strip().lower()) if w]
    if not words:
        return "unknown"
    if len(words) == 1 and (words[0] in BROAD_WORDS or pool_size >= 60):
        return "broad"
    if len(words) >= 3 or pool_size and pool_size < 8:
        return "narrow"
    return "medium"


def label_retrospective_fit(label: str, pool_size: int) -> Explained:
    """Читается ли короткая надпись как естественное объяснение четвёрки.

    Главный вопрос, заменивший «насколько название специфично»: игрок уже
    увидел четыре слова — воспринимается ли надпись как «ах, вот что это
    было». Широта здесь не мешает: FOOD над `bread, rice, egg, milk`
    объясняет всё. Мешает пустота (`RELATED THINGS`), техномусор и длина.
    """
    text = label.strip()
    lowered = text.lower()
    words = [w for w in _TOKEN_RE.split(lowered) if w]
    parts = {"base": 1.0}
    if not words:
        return Explained(score=0.0, parts={"empty": 0.0})
    meaningful = [w for w in words if w not in VAGUE_WORDS]
    if not meaningful:
        # Надпись не объясняет ничего: после решения игрок знает не больше.
        parts["explains_nothing"] = -0.75
    elif len(meaningful) < len(words):
        parts["vague_filler"] = -0.25
    if re.search(r"[_/]|\d{2,}", text):
        parts["technical_marks"] = -0.6
    if len(words) >= 5:
        # Объяснение длиной в предложение перестаёт быть reveal'ом.
        parts["reads_as_sentence"] = -0.35
    elif len(words) == 4:
        parts["long_label"] = -0.15
    if pool_size and pool_size < 5:
        # Пул меньше четвёрки: правило подогнано под конкретные слова.
        parts["pool_below_quartet"] = -0.2
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def label_reveal_satisfaction(label: str) -> Explained:
    """Насколько приятно надпись читается в момент раскрытия.

    Короткое конкретное слово приятнее длинного описания — для этой игры это
    достоинство, а не упрощение. Формула поощряет краткость и наказывает
    оборванные служебные хвосты.
    """
    text = label.strip()
    lowered = text.lower()
    words = [w for w in _TOKEN_RE.split(lowered) if w]
    if not words:
        return Explained(score=0.0, parts={"empty": 0.0})
    parts = {"base": 0.7}
    if len(words) <= 2:
        parts["short_and_punchy"] = 0.3
    elif len(words) == 3:
        parts["still_readable"] = 0.1
    else:
        parts["too_wordy"] = -0.2
    if lowered.endswith((" of", " the", " and", " a", " in", " with")):
        parts["dangling_word"] = -0.4
    if all(word in VAGUE_WORDS for word in words):
        parts["nothing_revealed"] = -0.5
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def label_specificity(label: str, pool_size: int) -> Explained:
    """Насколько название сужает принцип. Диагностика, в качество НЕ входит.

    Оставлено ради непрерывности отчётов и разбора спорных названий. В формулу
    `label_quality` эта ось больше не попадает: монотонный бонус за узость
    работал против референса, где короткий широкий ярлык — норма.
    """
    words = [w for w in _TOKEN_RE.split(label.strip().lower()) if w]
    parts = {"base": 0.5}
    if len(words) >= 2:
        parts["qualified"] = 0.25
    if len(words) >= 4:
        parts["overqualified"] = -0.2
    if any(word in BROAD_WORDS for word in words) and len(words) == 1:
        parts["too_broad"] = -0.3
    # Огромный пул — признак того, что принцип шире, чем звучит название.
    if pool_size >= 60:
        parts["huge_pool"] = -0.2
    elif pool_size >= 30:
        parts["large_pool"] = -0.1
    elif pool_size and pool_size < 6:
        parts["thin_pool"] = -0.15
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def label_naturalness(label: str) -> Explained:
    """Звучит ли название так, как сказал бы носитель. Эвристика, не истина.

    Формула не может судить о естественности надёжно, поэтому она только
    отмечает подозрительное: служебные хвосты, лишние знаки, слишком много слов.
    """
    text = label.strip()
    lowered = text.lower()
    parts = {"base": 1.0}
    if re.search(r"[_/]|\d{2,}", text):
        parts["technical_marks"] = -1.0
    if lowered.endswith((" of", " the", " and", " a", " in")):
        parts["dangling_word"] = -0.4
    if len([w for w in _TOKEN_RE.split(lowered) if w]) > 4:
        parts["too_many_words"] = -0.2
    if text != text.upper() and text != text.title() and text != text.capitalize():
        parts["odd_casing"] = -0.1
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def label_quality(
    *,
    naturalness: float,
    clarity: float,
    retrospective_fit: float,
    reveal_satisfaction: float,
    display_width_score: float,
    familiarity: float,
    config: dict[str, float],
) -> Explained:
    """Качество надписи. Оси специфичности здесь намеренно нет.

    Раньше здесь стоял `specificity`, и более узкая надпись автоматически
    получала больше. Для этой игры это неверно: надпись показывается ПОСЛЕ
    решения, и короткое широкое слово часто и есть лучший reveal. Ось заменена
    на «объясняет ли надпись четвёрку задним числом» и «приятно ли читается».
    Охват (`label_scope`) остался, но как характеристика, а не как слагаемое.
    """
    parts = {
        "naturalness": round(config["label_quality_naturalness_weight"] * naturalness, 4),
        "clarity": round(config["label_quality_clarity_weight"] * clarity, 4),
        "retrospective_fit": round(
            config["label_quality_retrospective_weight"] * retrospective_fit, 4
        ),
        "reveal": round(config["label_quality_reveal_weight"] * reveal_satisfaction, 4),
        "display": round(config["label_quality_display_weight"] * display_width_score, 4),
        "familiarity": round(config["label_quality_familiarity_weight"] * familiarity, 4),
    }
    total = sum(parts.values())

    # Потолок при сломанной формулировке. Взвешенная сумма усредняет: короткое
    # понятное название с техническим мусором вроде `kitchen_tools_v2` набирало
    # 0.84 за счёт остальных осей. Но это не название с изъяном — это вообще
    # не название, и высокого качества у него быть не может.
    cap = naturalness + config["label_quality_naturalness_floor"]
    if total > cap:
        parts["broken_label_cap"] = round(cap - total, 4)
        total = cap
    return Explained(score=clamp(total), parts=parts)


# ========================================================================= четвёрка


def cohesion(fit_scores: list[float], config: dict[str, float]) -> Explained:
    """Связность четвёрки со штрафом за слабое звено.

    Одна натянутая связь портит четвёрку сильнее, чем четыре средние: игрок
    спотыкается именно на ней. Поэтому минимум весит почти половину.
    """
    if not fit_scores:
        return Explained(score=0.0, parts={"empty": 0.0})
    weight = config["cohesion_weakest_link_weight"]
    average = sum(fit_scores) / len(fit_scores)
    weakest = min(fit_scores)
    parts = {
        "average": round((1 - weight) * average, 4),
        "weakest_link": round(weight * weakest, 4),
    }
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def foreign_pressure(
    pools: dict[str, set[str]], category_key: str, words: tuple[str, ...] | list[str]
) -> float:
    """Доля слов четвёрки, которые встречаются ещё хотя бы в одной категории.

    Это и есть управляемая неоднозначность на уровне четвёрки: слово тянет
    игрока в сторону, но дом у него здесь один. Ноль — четвёрка без соблазна,
    единица — каждое слово спорно.

    Хранится в `quartets.ambiguity_pressure`. Не путать с `ambiguity_score`
    отдельного слова: то про слово вообще, это — про конкретную четвёрку.
    """
    if not words:
        return 0.0
    hits = sum(
        1
        for word in words
        if any(other != category_key and word in pool for other, pool in pools.items())
    )
    return round(hits / len(words), 4)


def quartet_interest(
    *,
    novelty_scores: list[float],
    accessibility_scores: list[float],
    cohesion_score: float,
    label_quality_score: float,
    rare_count: int,
    config: dict[str, float],
) -> Explained:
    """Интересность четвёрки — ось, отдельная от понятности.

    Четыре банальных слова понятны и скучны. Четыре редких — «интересны» и
    непроходимы. Пик там, где есть один-два менее очевидных элемента при
    сохранении понятности группы.
    """
    if not novelty_scores:
        return Explained(score=0.0, parts={"empty": 0.0})
    peak_novelty = max(novelty_scores)
    average_novelty = sum(novelty_scores) / len(novelty_scores)
    controlled = 0.65 * peak_novelty + 0.35 * average_novelty
    spread = max(accessibility_scores) - min(accessibility_scores) if accessibility_scores else 0.0

    parts = {
        "controlled_novelty": round(config["quartet_interest_novelty_weight"] * controlled, 4),
        "word_diversity": round(
            config["quartet_interest_diversity_weight"] * clamp(spread * 2), 4
        ),
        "semantic_elegance": round(
            config["quartet_interest_elegance_weight"] * cohesion_score, 4
        ),
        "label_quality": round(
            config["quartet_interest_label_weight"] * label_quality_score, 4
        ),
    }
    if rare_count >= 2:
        parts["obscurity_penalty"] = -round(
            config["quartet_interest_obscurity_penalty"] * min(rare_count, 4) / 4, 4
        )
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def quartet_clarity(
    *, min_accessibility: float, max_ambiguity: float, label_clarity_score: float
) -> Explained:
    """Насколько быстро игрок поймёт, что эти четыре слова — одна группа."""
    parts = {
        "weakest_word": round(0.45 * min_accessibility, 4),
        "label_clarity": round(0.35 * label_clarity_score, 4),
        "low_ambiguity": round(0.20 * (1.0 - max_ambiguity), 4),
    }
    return Explained(score=clamp(sum(parts.values())), parts=parts)


def quartet_quality(
    *,
    cohesion_score: float,
    avg_accessibility: float,
    clarity_score: float,
    label_quality_score: float,
    config: dict[str, float],
) -> Explained:
    """Технический рейтинг пригодности четвёрки. Solver уровня он не заменяет.

    Высокий балл не означает, что четвёрку безопасно ставить рядом с любой
    другой: неоднозначность рождается на стыке групп, и это проверяет только
    exact-cover solver полного уровня.
    """
    parts = {
        "cohesion": round(config["quartet_quality_cohesion_weight"] * cohesion_score, 4),
        "accessibility": round(
            config["quartet_quality_accessibility_weight"] * avg_accessibility, 4
        ),
        "clarity": round(config["quartet_quality_clarity_weight"] * clarity_score, 4),
        "label_quality": round(config["quartet_quality_label_weight"] * label_quality_score, 4),
    }
    return Explained(score=clamp(sum(parts.values())), parts=parts)


# ======================================================================= пересчёт базы


def score_words(conn: sqlite3.Connection, config: dict[str, float]) -> tuple[int, dict[str, int]]:
    """Пересчитывает метрики всех игровых display form. Полностью идемпотентно."""
    version = str(int(config["word_scoring_version"]))
    rows = list(
        conn.execute(
            """
            SELECT w.id AS word_id, s.id AS sense_id,
                   COALESCE(s.display_text, w.text) AS display,
                   w.familiarity_score AS familiarity,
                   COALESCE(s.is_proper_noun, w.is_proper_noun) AS is_proper_noun,
                   (SELECT COUNT(*) FROM word_senses x WHERE x.word_id = w.id) AS sense_count,
                   (SELECT COUNT(*) FROM memberships m
                     WHERE m.word_id = w.id
                       AND m.review_status IN ('approved','alternative','hard_only')) AS memberships,
                   (SELECT COUNT(DISTINCT c.theme) FROM memberships m
                      JOIN categories c ON c.id = m.category_id
                     WHERE m.word_id = w.id
                       AND m.review_status IN ('approved','alternative','hard_only')) AS themes,
                   (SELECT MAX(m.fit_score) FROM memberships m
                     WHERE m.word_id = w.id
                       AND m.review_status IN ('approved','alternative','hard_only')) AS best_fit,
                   (SELECT COUNT(*) FROM memberships m
                     WHERE m.word_id = w.id AND m.risk_flags IS NOT NULL
                       AND m.risk_flags <> '[]') AS risky
              FROM words w
              LEFT JOIN word_senses s ON s.word_id = w.id
             ORDER BY w.id, s.id
            """
        )
    )
    now = utc_now()
    stats = {"строк": 0, "без частотности": 0}
    conn.execute("DELETE FROM word_scores")
    for row in rows:
        metrics = display_metrics(row["display"], config)
        spelling = spelling_difficulty(row["display"], bool(row["is_proper_noun"]))
        novelty_score = novelty(row["familiarity"], config)
        ambiguity_score = ambiguity(
            int(row["sense_count"]), int(row["memberships"]), int(row["themes"])
        )
        access = accessibility(
            familiarity=row["familiarity"],
            display_width_score=metrics["display_width_score"],
            char_count=metrics["char_count"],
            spelling_difficulty_score=spelling,
            config=config,
        )
        quality = word_quality(
            accessibility_score=access.score,
            semantic_usefulness=row["best_fit"] or 0.0,
            novelty_score=novelty_score,
            risk_flagged=bool(row["risky"]),
            display_width_score=metrics["display_width_score"],
            config=config,
        )
        if row["familiarity"] is None:
            stats["без частотности"] += 1
        conn.execute(
            """
            INSERT INTO word_scores
                (word_id, sense_id, display_text, char_count, token_count,
                 display_width_score, spelling_difficulty_score, ambiguity_score,
                 novelty_score, accessibility_score, word_quality_score,
                 scoring_version, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(row["word_id"]),
                row["sense_id"],
                row["display"],
                int(metrics["char_count"]),
                int(metrics["token_count"]),
                metrics["display_width_score"],
                spelling,
                ambiguity_score,
                novelty_score,
                access.rounded(),
                quality.rounded(),
                version,
                now,
            ),
        )
        stats["строк"] += 1
    return stats["строк"], stats


def score_labels(conn: sqlite3.Connection, config: dict[str, float]) -> tuple[int, dict[str, int]]:
    """Пересчитывает качество названий категорий."""
    version = str(int(config["label_scoring_version"]))
    rows = list(
        conn.execute(
            """
            SELECT c.id AS category_id, c.label AS label,
                   (SELECT COUNT(*) FROM memberships m
                     WHERE m.category_id = c.id
                       AND m.review_status IN ('approved','alternative','hard_only')) AS pool,
                   (SELECT AVG(w.familiarity_score) FROM memberships m
                      JOIN words w ON w.id = m.word_id
                     WHERE m.category_id = c.id
                       AND m.review_status IN ('approved','alternative')) AS pool_familiarity
              FROM categories c ORDER BY c.id
            """
        )
    )
    now = utc_now()
    stats = {"строк": 0, "со слабым названием": 0}
    conn.execute("DELETE FROM category_label_scores")
    for row in rows:
        metrics = label_metrics(row["label"], config)
        naturalness = label_naturalness(row["label"])
        clarity = label_clarity(row["label"])
        specificity = label_specificity(row["label"], int(row["pool"]))
        retrospective = label_retrospective_fit(row["label"], int(row["pool"]))
        reveal = label_reveal_satisfaction(row["label"])
        scope = label_scope(row["label"], int(row["pool"]))
        familiarity = row["pool_familiarity"] or 0.0
        novelty_score = novelty(familiarity, config)
        quality = label_quality(
            naturalness=naturalness.score,
            clarity=clarity.score,
            retrospective_fit=retrospective.score,
            reveal_satisfaction=reveal.score,
            display_width_score=metrics["label_display_width_score"],
            familiarity=familiarity,
            config=config,
        )
        if quality.score < 0.6:
            stats["со слабым названием"] += 1
        conn.execute(
            """
            INSERT INTO category_label_scores
                (category_id, label_char_count, label_token_count,
                 label_display_width_score, label_familiarity_score,
                 label_naturalness_score, label_clarity_score, label_specificity_score,
                 label_novelty_score, label_quality_score,
                 label_retrospective_fit, label_reveal_satisfaction,
                 label_display_fitness, label_scope,
                 scoring_version, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(row["category_id"]),
                int(metrics["label_char_count"]),
                int(metrics["label_token_count"]),
                metrics["label_display_width_score"],
                round(familiarity, 4),
                naturalness.rounded(),
                clarity.rounded(),
                specificity.rounded(),
                novelty_score,
                quality.rounded(),
                retrospective.rounded(),
                reveal.rounded(),
                metrics["label_display_width_score"],
                scope,
                version,
                now,
            ),
        )
        stats["строк"] += 1
    return stats["строк"], stats


def score_quartets(
    conn: sqlite3.Connection, config: dict[str, float]
) -> tuple[int, dict[str, int]]:
    """Пересчитывает агрегаты четвёрок из актуальных word и label scores."""
    version = str(int(config["quartet_scoring_version"]))
    rare = config["word_rare_familiarity"]
    now = utc_now()
    stats = {"четвёрок": 0, "без словарных оценок": 0}

    label_scores = {
        int(row["category_id"]): row
        for row in conn.execute("SELECT * FROM category_label_scores")
    }
    # Надпись у правила своя: quartet variant обязан знать, что покажут игроку.
    primary_labels = {
        int(row["category_id"]): int(row["label_id"])
        for row in conn.execute(
            "SELECT category_id, label_id FROM group_rule_labels WHERE is_primary = 1"
        )
    }
    # Сколько чужих правил принимают слова этой четвёрки: материал для ловушек
    # и вход в оценку отрыва разбиения.
    alternatives: dict[int, int] = {}
    for row in conn.execute(
        """
        SELECT qw.quartet_id AS quartet_id, COUNT(*) AS n
          FROM quartet_words qw
          JOIN quartets q  ON q.id = qw.quartet_id
          JOIN memberships m ON m.word_id = qw.word_id
                            AND m.category_id <> q.category_id
                            AND m.review_status IN ('approved', 'alternative', 'hard_only')
                            AND m.semantic_status <> 'incorrect'
         GROUP BY qw.quartet_id
        """
    ):
        alternatives[int(row["quartet_id"])] = int(row["n"])
    words: dict[int, list[sqlite3.Row]] = {}
    for row in conn.execute(
        """
        SELECT qw.quartet_id AS quartet_id, w.familiarity_score AS familiarity,
               ws.accessibility_score AS accessibility, ws.novelty_score AS novelty,
               ws.ambiguity_score AS ambiguity, ws.char_count AS char_count,
               m.fit_score AS fit
          FROM quartet_words qw
          JOIN quartets q ON q.id = qw.quartet_id
          JOIN words w ON w.id = qw.word_id
          LEFT JOIN word_scores ws
                 ON ws.word_id = qw.word_id
                AND COALESCE(ws.sense_id, 0) = COALESCE(qw.sense_id, 0)
          LEFT JOIN memberships m
                 ON m.word_id = qw.word_id AND m.category_id = q.category_id
                AND COALESCE(m.sense_id, 0) = COALESCE(qw.sense_id, 0)
        """
    ):
        words.setdefault(int(row["quartet_id"]), []).append(row)

    for quartet in conn.execute("SELECT id, category_id FROM quartets ORDER BY id"):
        members = words.get(int(quartet["id"]), [])
        if not members:
            stats["без словарных оценок"] += 1
            continue
        familiarity = [m["familiarity"] for m in members if m["familiarity"] is not None]
        access = [m["accessibility"] for m in members if m["accessibility"] is not None]
        novelties = [m["novelty"] or 0.0 for m in members]
        ambiguities = [m["ambiguity"] or 0.0 for m in members]
        lengths = [m["char_count"] or 0 for m in members]
        fits = [m["fit"] for m in members if m["fit"] is not None]

        label_row = label_scores.get(int(quartet["category_id"]))
        label_quality_score = float(label_row["label_quality_score"]) if label_row else 0.0
        label_clarity_score = float(label_row["label_clarity_score"]) if label_row else 0.0

        cohesion_result = cohesion(fits, config)
        clarity_result = quartet_clarity(
            min_accessibility=min(access) if access else 0.0,
            max_ambiguity=max(ambiguities) if ambiguities else 0.0,
            label_clarity_score=label_clarity_score,
        )
        interest_result = quartet_interest(
            novelty_scores=novelties,
            accessibility_scores=access,
            cohesion_score=cohesion_result.score,
            label_quality_score=label_quality_score,
            rare_count=sum(1 for value in familiarity if value < rare),
            config=config,
        )
        quality_result = quartet_quality(
            cohesion_score=cohesion_result.score,
            avg_accessibility=sum(access) / len(access) if access else 0.0,
            clarity_score=clarity_result.score,
            label_quality_score=label_quality_score,
            config=config,
        )

        conn.execute(
            """
            UPDATE quartets
               SET cohesion_score = ?, familiarity_score = ?,
                   min_word_familiarity = ?, avg_word_accessibility = ?,
                   min_word_accessibility = ?, avg_word_length = ?, max_word_length = ?,
                   quartet_clarity_score = ?, quartet_novelty_score = ?,
                   quartet_interest_score = ?, quartet_quality_score = ?,
                   label_quality_score = ?,
                   weakest_link_score = ?, label_retrospective_fit = ?,
                   alternative_membership_count = ?,
                   display_label_id = COALESCE(display_label_id, ?),
                   scoring_version = ?, updated_at = ?
             WHERE id = ?
            """,
            (
                cohesion_result.rounded(),
                round(sum(familiarity) / len(familiarity), 4) if familiarity else None,
                round(min(familiarity), 4) if familiarity else None,
                round(sum(access) / len(access), 4) if access else None,
                round(min(access), 4) if access else None,
                round(sum(lengths) / len(lengths), 2) if lengths else None,
                max(lengths) if lengths else None,
                clarity_result.rounded(),
                round(max(novelties), 4) if novelties else None,
                interest_result.rounded(),
                quality_result.rounded(),
                label_quality_score,
                # Слабое звено: одна натянутая связь портит четвёрку сильнее,
                # чем четыре средние, поэтому число хранится отдельно от средней.
                round(min(fits), 4) if fits else None,
                float(label_row["label_retrospective_fit"]) if label_row else None,
                alternatives.get(int(quartet["id"]), 0),
                primary_labels.get(int(quartet["category_id"])),
                version,
                now,
                int(quartet["id"]),
            ),
        )
        stats["четвёрок"] += 1

    stats["слотов дозаполнено"] = _fill_quartet_slots(conn)
    return stats["четвёрок"], stats


def _fill_quartet_slots(conn: sqlite3.Connection) -> int:
    """Слот четвёрки — не просто слово: у него своя связь с правилом.

    Тип связи, её сила, очевидность и выбранное значение хранятся у слота, а не
    только агрегатом у четвёрки. Без этого нельзя ответить на вопрос «какое
    звено самое слабое и почему», а именно он решает, интересная четвёрка или
    натянутая.
    """
    return int(
        conn.execute(
            """
            UPDATE quartet_words AS qw
               SET relation_type = COALESCE(qw.relation_type, (
                       SELECT m.relation_type FROM memberships m
                        JOIN quartets q ON q.id = qw.quartet_id
                        WHERE m.word_id = qw.word_id AND m.category_id = q.category_id
                          AND m.review_status <> 'rejected'
                        ORDER BY m.id LIMIT 1)),
                   relation_strength = COALESCE(qw.relation_strength, (
                       SELECT m.fit_score FROM memberships m
                        JOIN quartets q ON q.id = qw.quartet_id
                        WHERE m.word_id = qw.word_id AND m.category_id = q.category_id
                          AND m.review_status <> 'rejected'
                        ORDER BY m.id LIMIT 1)),
                   obviousness = COALESCE(qw.obviousness, (
                       SELECT m.obviousness_score FROM memberships m
                        JOIN quartets q ON q.id = qw.quartet_id
                        WHERE m.word_id = qw.word_id AND m.category_id = q.category_id
                          AND m.review_status <> 'rejected'
                        ORDER BY m.id LIMIT 1)),
                   intended_sense_key = COALESCE(qw.intended_sense_key, (
                       SELECT s.sense_key FROM word_senses s WHERE s.id = qw.sense_id))
             WHERE qw.relation_type IS NULL
                OR qw.relation_strength IS NULL
                OR qw.obviousness IS NULL
            """
        ).rowcount
        or 0
    )
