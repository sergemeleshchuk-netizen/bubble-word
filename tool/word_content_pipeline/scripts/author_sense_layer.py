#!/usr/bin/env python3
"""Разбор значений: вносит решения ревью в `data/seed/_sense_map.json`.

Скрипт — способ внести партию решений, а не источник правды. Источник правды —
сам `_sense_map.json`; после запуска скрипт больше не нужен, файл живёт своей
жизнью и правится руками. Так сделано потому, что 19 КБ JSON руками не
редактируются без ошибок, а решений здесь несколько сотен.

Две партии решений, они принципиально разные.

`MONOSEMOUS` — слова, у которых значение одно, просто контексты разные:
`turtle` в OCEAN ANIMALS и в GREEN THINGS — одна и та же черепаха. Такие слова
уезжают в `_not_homonyms.txt` (механизм в проекте уже есть) и получают
автоматически выведенное значение с оценками из знакомости слова.

`SENSES` — слова, которые действительно читаются по-разному. Здесь у каждого
значения объявлены вид, ранг доминантности, класс доступности и две оценки:
узнаваемость (узнает, если объяснить) и активация (вспомнит сам, увидев слово).
Для `Trouble` как настольной игры первое заметно выше второго, и это ровно та
разница, из-за которой четвёрка Life / risk / sorry / trouble неиграбельна.

Оценки экспертные (AI review, аудитория general_en_us_adult). Они не измерены
телеметрией и подлежат калибровке, когда телеметрия появится; поэтому у каждой
записи стоит `quality_source` и `quality_confidence`.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSE_MAP = ROOT / "data" / "seed" / "_sense_map.json"
NOT_HOMONYMS = ROOT / "data" / "seed" / "_not_homonyms.txt"

AUDIENCE = "general_en_us_adult"
REVIEW = "sense_review"


# --------------------------------------------------------------------------- 1
# Слова с одним значением. Разброс по темам у них есть, второго смысла нет.
MONOSEMOUS: tuple[str, ...] = (
    # предметы, которые везде остаются собой
    "cone", "bud", "canvas", "captain", "arch", "net", "salt", "uniform", "mask",
    "radar", "saw", "soda", "split", "director", "horse", "camera", "chair",
    "board", "cup", "reef", "rooster", "spin", "card", "clay", "cut", "gym",
    "heel", "radio", "referee", "spotlight", "sprint", "television", "arrow",
    "black", "buckle", "camel", "canal", "choir", "console", "counselor",
    "felt", "focus", "honey", "hoop", "kick", "knot", "marker", "needle",
    "nest", "orbit", "star", "witch", "aluminum", "ant", "bakery", "bird",
    "blade", "bolt", "bowl", "box", "calendar", "candle", "canteen", "carton",
    "caterpillar", "cement", "chalk", "chili", "chop", "cider", "closet",
    "comet", "compost", "confetti", "cooler", "crab", "cranberry", "crate",
    "cream", "cucumber", "desert", "dive", "doll", "doorbell", "dove", "egg",
    "envelope", "fish", "flour", "folder", "gloves", "granite", "grape",
    "gravel", "hammer", "harness", "hay", "hem", "hinge", "jade", "jar", "jet",
    "juice", "ketchup", "lavender", "lemon", "lemonade", "lettuce", "lime",
    "milk", "mint", "moon", "mustard", "nebula", "oyster", "party", "peach",
    "phone", "pilot", "pipe", "plaque", "poster", "primer", "puddle",
    "pyramid", "receipt", "rice", "roar", "robot", "roller", "safe", "sausage",
    "scarf", "shower", "shrimp", "shuffle", "sled", "spear", "spider",
    "sponge", "sprinkler", "squid", "stamp", "straw", "streamer", "sugar",
    "suitcase", "sunglasses", "sword", "tap", "tile", "tomato", "tractor",
    "vacuum", "wallet", "wand", "well", "whale", "wrench", "popcorn", "wool",
    "cotton", "silk", "velvet", "boulder", "coffee", "collar", "flashlight",
    "goggles", "meteor", "pollen", "tuna", "vine", "soil", "strap", "leaf",
    "doctor", "nurse", "chips", "bulb", "tank",
)


def sense(
    definition: str,
    *,
    pos: str = "noun",
    kind: str = "lexical",
    rank: int,
    access: str,
    recognition: float,
    activation: float,
    confidence: float,
    display: str | None = None,
    proper: bool = False,
) -> dict:
    entry = {
        "definition": definition,
        "part_of_speech": pos,
        "sense_kind": kind,
        "dominance_rank": rank,
        "accessibility_class": access,
        "recognition_score": recognition,
        "activation_score": activation,
        "audience_profile": AUDIENCE,
        "quality_source": REVIEW,
        "quality_confidence": confidence,
    }
    if display:
        entry["display"] = display
    if proper:
        entry["is_proper_noun"] = True
    return entry


# --------------------------------------------------------------------------- 2
# Многозначные слова: значения, ранги, доступность.
#
# Ранг 1 — то, чем слово читается без контекста. Он не обязан совпадать с тем
# значением, которое чаще используется в базе: `orange` в базе чаще цвет, но
# читается всё-таки фруктом.
SENSES: dict[str, dict[str, dict]] = {
    # ---- P0: разбор группы, из-за которой всё это затевалось ----------------
    "trouble": {
        "trouble_problem": sense(
            "A problem, difficulty, or distressing situation.",
            rank=1, access="primary",
            recognition=0.99, activation=0.97, confidence=0.95,
        ),
        "trouble_board_game": sense(
            "Trouble, an American board game with a dice popper.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.42, activation=0.04, confidence=0.90,
            display="Trouble", proper=True,
        ),
    },
    "risk": {
        "risk_danger": sense(
            "The chance that something bad will happen; exposure to danger.",
            rank=1, access="primary",
            recognition=0.99, activation=0.96, confidence=0.95,
        ),
        "risk_board_game": sense(
            "Risk, a board game of army conquest played on a world map.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.48, activation=0.06, confidence=0.88,
            display="Risk", proper=True,
        ),
    },
    "sorry": {
        "sorry_apology": sense(
            "The word said to apologise; feeling regret.",
            pos="interjection", rank=1, access="primary",
            recognition=0.99, activation=0.98, confidence=0.96,
        ),
        "sorry_board_game": sense(
            "Sorry!, a board game in which pieces send each other home.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.44, activation=0.05, confidence=0.88,
            display="Sorry", proper=True,
        ),
    },
    "life": {
        "life_existence": sense(
            "Being alive; the existence of a living thing.",
            rank=1, access="primary",
            recognition=0.99, activation=0.98, confidence=0.96,
        ),
        "life_game": sense(
            "The Game of Life, an American board game about careers and family.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.46, activation=0.05, confidence=0.88,
            display="Life", proper=True,
        ),
        "life_cereal": sense(
            "Life, an American breakfast cereal brand.",
            pos="proper_noun", kind="brand", rank=3, access="specialist",
            recognition=0.32, activation=0.02, confidence=0.85,
            display="Life", proper=True,
        ),
    },
    # Игры, у которых название и есть главное чтение слова: игрок видит
    # `monopoly` и думает про игру, а не про экономический термин.
    "monopoly": {
        "monopoly_game": sense(
            "Monopoly, the property-trading board game.",
            pos="proper_noun", kind="title", rank=1, access="primary",
            recognition=0.96, activation=0.88, confidence=0.92,
            display="Monopoly", proper=True,
        ),
        "monopoly_market": sense(
            "Exclusive control of a market by one seller.",
            rank=2, access="common_secondary",
            recognition=0.88, activation=0.35, confidence=0.85,
        ),
    },
    "scrabble": {
        "scrabble_game": sense(
            "Scrabble, the board game of building words on a grid.",
            pos="proper_noun", kind="title", rank=1, access="primary",
            recognition=0.95, activation=0.90, confidence=0.92,
            display="Scrabble", proper=True,
        ),
    },
    "chess": {
        "chess_game": sense(
            "Chess, the two-player strategy game played on a chequered board.",
            rank=1, access="primary",
            recognition=0.98, activation=0.96, confidence=0.95,
        ),
    },
    "checkers": {
        "checkers_game": sense(
            "Checkers, the board game played with round pieces on a chequered board.",
            rank=1, access="primary",
            recognition=0.96, activation=0.92, confidence=0.93,
        ),
    },
    "clue": {
        "clue_hint": sense(
            "A piece of evidence that helps solve a problem or mystery.",
            rank=1, access="primary",
            recognition=0.98, activation=0.95, confidence=0.94,
        ),
        "clue_board_game": sense(
            "Clue, the murder-mystery board game.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.55, activation=0.09, confidence=0.86,
            display="Clue", proper=True,
        ),
    },
    "battleship": {
        "battleship_ship": sense(
            "A large heavily armed warship.",
            rank=1, access="primary",
            recognition=0.94, activation=0.86, confidence=0.90,
        ),
        "battleship_game": sense(
            "Battleship, the guessing game of hidden ships on a grid.",
            pos="proper_noun", kind="title", rank=2, access="common_secondary",
            recognition=0.78, activation=0.30, confidence=0.82,
            display="Battleship", proper=True,
        ),
    },
    "cards": {
        "cards_game": sense(
            "Playing cards, or a game played with a deck of them.",
            rank=1, access="primary",
            recognition=0.97, activation=0.93, confidence=0.92,
        ),
    },
    "backgammon": {
        "backgammon_game": sense(
            "Backgammon, the board game of moving pieces round a board by dice.",
            rank=1, access="primary",
            recognition=0.88, activation=0.82, confidence=0.88,
        ),
    },
    "dominoes": {
        "dominoes_game": sense(
            "Dominoes, the game played with rectangular tiles marked with pips.",
            rank=1, access="primary",
            recognition=0.94, activation=0.90, confidence=0.90,
        ),
    },
    "marbles": {
        "marbles_game": sense(
            "Marbles, the children's game played with small glass balls.",
            rank=1, access="primary",
            recognition=0.90, activation=0.84, confidence=0.88,
        ),
    },
    "hopscotch": {
        "hopscotch_game": sense(
            "Hopscotch, the pavement game of hopping through chalked squares.",
            rank=1, access="primary",
            recognition=0.92, activation=0.90, confidence=0.90,
        ),
    },
    "tag": {
        "tag_label": sense(
            "A small label attached to an object.",
            rank=1, access="primary",
            recognition=0.97, activation=0.88, confidence=0.90,
        ),
        "tag_game": sense(
            "Tag, the chasing game children play.",
            rank=2, access="common_secondary",
            recognition=0.92, activation=0.52, confidence=0.85,
        ),
    },
    "jacks": {
        "jacks_game": sense(
            "Jacks, the game of picking up metal pieces between bounces of a ball.",
            rank=1, access="primary",
            recognition=0.72, activation=0.60, confidence=0.80,
        ),
    },
    "hearts": {
        "hearts_suit": sense(
            "Hearts, the red suit in a deck of playing cards.",
            rank=1, access="primary",
            recognition=0.96, activation=0.88, confidence=0.90,
        ),
        "hearts_game": sense(
            "Hearts, the trick-taking card game.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.50, activation=0.08, confidence=0.84,
            display="Hearts",
        ),
    },
    "spades": {
        "spades_suit": sense(
            "Spades, the black suit in a deck of playing cards.",
            rank=1, access="primary",
            recognition=0.96, activation=0.88, confidence=0.90,
        ),
        "spades_game": sense(
            "Spades, the partnership trick-taking card game.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.46, activation=0.07, confidence=0.84,
            display="Spades",
        ),
    },

    # ---- P0: честная вторичность, которую запрещать нельзя -----------------
    "orange": {
        "orange_fruit": sense(
            "A round citrus fruit with an orange peel.",
            rank=1, access="primary",
            recognition=0.99, activation=0.92, confidence=0.94,
        ),
        # Не главное значение слова — и при этом массово известное. Ровно та
        # честная ловушка, ради которой вторые значения вообще нужны в игре.
        "orange_color": sense(
            "The colour between red and yellow.",
            rank=2, access="common_secondary",
            recognition=0.99, activation=0.72, confidence=0.94,
        ),
    },

    # ---- структурный набор без сильного SWOW -------------------------------
    "north": {"north_direction": sense(
        "The direction towards the top of a map; one of the four cardinal points.",
        rank=1, access="primary", recognition=0.99, activation=0.95, confidence=0.95)},
    "south": {"south_direction": sense(
        "The direction opposite north; one of the four cardinal points.",
        rank=1, access="primary", recognition=0.99, activation=0.95, confidence=0.95)},
    "east": {"east_direction": sense(
        "The direction of the sunrise; one of the four cardinal points.",
        rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.95)},
    "west": {"west_direction": sense(
        "The direction of the sunset; one of the four cardinal points.",
        rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.95)},

    # ---- многозначные слова из очереди, по убыванию ценности ---------------
    "bark": {
        "bark_sound": sense(
            "The short loud sound a dog makes.",
            rank=1, access="primary", recognition=0.98, activation=0.85, confidence=0.92),
        "bark_tree": sense(
            "The tough outer covering of a tree trunk.",
            rank=2, access="common_secondary",
            recognition=0.97, activation=0.62, confidence=0.92),
    },
    "bass": {
        "bass_low": sense(
            "The lowest range of musical sound, or an instrument playing it.",
            rank=1, access="primary", recognition=0.96, activation=0.80, confidence=0.90),
        "bass_fish": sense(
            "A freshwater or sea fish caught by anglers.",
            rank=2, access="common_secondary",
            recognition=0.90, activation=0.48, confidence=0.88),
    },
    "turkey": {
        "turkey_bird": sense(
            "A large bird raised for meat and eaten at Thanksgiving.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.94),
        "turkey_country": sense(
            "Turkey, the country between Europe and Asia.",
            pos="proper_noun", kind="proper_name", rank=2, access="common_secondary",
            recognition=0.95, activation=0.42, confidence=0.90,
            display="Turkey", proper=True),
    },
    "silver": {
        "silver_metal": sense(
            "A shiny precious metal used for coins and jewellery.",
            rank=1, access="primary", recognition=0.99, activation=0.90, confidence=0.93),
        "silver_color": sense(
            "The pale grey colour of polished silver.",
            pos="adjective", rank=2, access="common_secondary",
            recognition=0.97, activation=0.60, confidence=0.90),
    },
    "compass": {
        "compass_navigation": sense(
            "An instrument with a magnetic needle that shows direction.",
            rank=1, access="primary", recognition=0.99, activation=0.93, confidence=0.93),
        "compass_drawing": sense(
            "A hinged instrument for drawing circles.",
            rank=2, access="common_secondary",
            recognition=0.88, activation=0.40, confidence=0.85),
    },
    "spring": {
        "spring_season": sense(
            "The season between winter and summer.",
            rank=1, access="primary", recognition=0.99, activation=0.90, confidence=0.93),
        "spring_coil": sense(
            "A coil of metal that returns to shape after being pressed.",
            rank=2, access="common_secondary",
            recognition=0.96, activation=0.55, confidence=0.90),
        "spring_water": sense(
            "A place where water flows naturally out of the ground.",
            rank=3, access="common_secondary",
            recognition=0.93, activation=0.38, confidence=0.88),
    },
    "iron": {
        "iron_metal": sense(
            "A hard grey metal, and the element Fe.",
            rank=1, access="primary", recognition=0.99, activation=0.90, confidence=0.93),
        "iron_appliance": sense(
            "A heated tool pressed on clothes to remove creases.",
            rank=2, access="common_secondary",
            recognition=0.97, activation=0.62, confidence=0.90),
        "iron_golf": sense(
            "A golf club with a flat angled metal head.",
            rank=3, access="specialist",
            recognition=0.52, activation=0.08, confidence=0.82),
    },
    "cast": {
        "cast_group": sense(
            "The group of actors performing in a film or play.",
            rank=1, access="primary", recognition=0.96, activation=0.78, confidence=0.88),
        "cast_plaster": sense(
            "A hard plaster covering that holds a broken bone still.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.55, confidence=0.88),
    },
    "scale": {
        "scale_weighing": sense(
            "A device for weighing things.",
            rank=1, access="primary", recognition=0.98, activation=0.82, confidence=0.90),
        "scale_animal": sense(
            "One of the small plates covering the skin of a fish or reptile.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.50, confidence=0.88),
        "scale_music": sense(
            "A series of musical notes in ascending order.",
            rank=3, access="common_secondary",
            recognition=0.88, activation=0.35, confidence=0.85),
        "scale_map": sense(
            "The ratio between distance on a map and distance on the ground.",
            rank=4, access="common_secondary",
            recognition=0.82, activation=0.25, confidence=0.82),
    },
    "heart": {
        "heart_organ": sense(
            "The organ that pumps blood around the body.",
            rank=1, access="primary", recognition=0.99, activation=0.95, confidence=0.95),
        "heart_shape": sense(
            "The rounded symbol used to mean love.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.65, confidence=0.90),
        "heart_suit": sense(
            "Hearts, the red suit in a deck of playing cards.",
            rank=3, access="common_secondary",
            recognition=0.90, activation=0.30, confidence=0.85),
    },
    "trunk": {
        "trunk_tree": sense(
            "The thick main stem of a tree.",
            rank=1, access="primary", recognition=0.98, activation=0.85, confidence=0.92),
        "trunk_car": sense(
            "The luggage compartment at the back of a car.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.55, confidence=0.90),
        "trunk_elephant": sense(
            "The long flexible nose of an elephant.",
            rank=3, access="common_secondary",
            recognition=0.97, activation=0.50, confidence=0.90),
        "trunk_chest": sense(
            "A large sturdy box used for storage or travel.",
            rank=4, access="common_secondary",
            recognition=0.88, activation=0.28, confidence=0.84),
    },
    "mouse": {
        "mouse_animal": sense(
            "A small rodent with a long thin tail.",
            rank=1, access="primary", recognition=0.99, activation=0.93, confidence=0.94),
        "mouse_computer": sense(
            "The hand-held device used to move a pointer on a screen.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.66, confidence=0.92),
    },
    "monitor": {
        "monitor_screen": sense(
            "A screen that displays output from a computer.",
            rank=1, access="primary", recognition=0.97, activation=0.85, confidence=0.90),
        "monitor_medical": sense(
            "A device that keeps watch on a patient's vital signs.",
            rank=2, access="common_secondary",
            recognition=0.90, activation=0.40, confidence=0.85),
        "monitor_lizard": sense(
            "A monitor lizard, a large tropical lizard.",
            rank=3, access="specialist",
            recognition=0.38, activation=0.04, confidence=0.82),
    },
    "keyboard": {
        "keyboard_computer": sense(
            "The set of keys used for typing on a computer.",
            rank=1, access="primary", recognition=0.99, activation=0.90, confidence=0.93),
        "keyboard_instrument": sense(
            "An electronic musical instrument with piano-style keys.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.48, confidence=0.88),
    },
    "cardinal": {
        "cardinal_bird": sense(
            "A bright red North American songbird.",
            rank=1, access="primary", recognition=0.90, activation=0.72, confidence=0.86),
        "cardinal_clergy": sense(
            "A senior Roman Catholic churchman who elects the Pope.",
            rank=2, access="common_secondary",
            recognition=0.85, activation=0.40, confidence=0.84),
    },
    "chest": {
        "chest_body": sense(
            "The front of the upper body, between neck and stomach.",
            rank=1, access="primary", recognition=0.99, activation=0.92, confidence=0.94),
        "chest_box": sense(
            "A large strong box with a lid, used for storage.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.52, confidence=0.90),
    },
    "beam": {
        "beam_structure": sense(
            "A long piece of timber or metal that supports a building.",
            rank=1, access="primary", recognition=0.95, activation=0.75, confidence=0.88),
        "beam_light": sense(
            "A ray or shaft of light.",
            rank=2, access="common_secondary",
            recognition=0.96, activation=0.62, confidence=0.88),
        "beam_smile": sense(
            "To smile broadly and happily.",
            pos="verb", rank=3, access="common_secondary",
            recognition=0.82, activation=0.25, confidence=0.82),
    },
    "bow": {
        "bow_bend": sense(
            "To bend the upper body forward as a greeting.",
            pos="verb", rank=1, access="primary",
            recognition=0.97, activation=0.72, confidence=0.88),
        "bow_weapon": sense(
            "A curved weapon that shoots arrows.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.68, confidence=0.90),
        "bow_music": sense(
            "The stick strung with hair used to play a violin.",
            rank=3, access="common_secondary",
            recognition=0.86, activation=0.32, confidence=0.84),
    },
    "hood": {
        "hood_garment": sense(
            "The part of a coat that covers the head.",
            rank=1, access="primary", recognition=0.98, activation=0.88, confidence=0.92),
        "hood_car": sense(
            "The hinged cover over a car engine.",
            rank=2, access="common_secondary",
            recognition=0.93, activation=0.42, confidence=0.86),
    },
    "coral": {
        "coral_animal": sense(
            "The hard structure built by tiny sea animals in warm oceans.",
            rank=1, access="primary", recognition=0.96, activation=0.85, confidence=0.92),
        "coral_color": sense(
            "A pinkish-orange colour named after the sea coral.",
            pos="adjective", rank=2, access="common_secondary",
            recognition=0.82, activation=0.30, confidence=0.82),
    },
    "trailer": {
        "trailer_vehicle": sense(
            "A wheeled container towed behind a vehicle.",
            rank=1, access="primary", recognition=0.96, activation=0.75, confidence=0.88),
        "trailer_film": sense(
            "A short advertisement for a film that is coming soon.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.58, confidence=0.88),
    },
    "triangle": {
        "triangle_shape": sense(
            "A flat shape with three straight sides.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "triangle_instrument": sense(
            "A percussion instrument made from a bent steel bar.",
            rank=2, access="common_secondary",
            recognition=0.86, activation=0.28, confidence=0.84),
    },
    "square": {
        "square_shape": sense(
            "A flat shape with four equal sides and four right angles.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "square_tool": sense(
            "An L-shaped tool used to check and mark right angles.",
            rank=2, access="specialist",
            recognition=0.55, activation=0.08, confidence=0.82),
        "square_math": sense(
            "The result of multiplying a number by itself.",
            rank=3, access="common_secondary",
            recognition=0.88, activation=0.30, confidence=0.85),
        "square_brand": sense(
            "Square, the American payment company.",
            pos="proper_noun", kind="brand", rank=4, access="specialist",
            recognition=0.40, activation=0.03, confidence=0.82,
            display="Square", proper=True),
    },
    "foot": {
        "foot_body": sense(
            "The part of the leg below the ankle that you stand on.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "foot_measure": sense(
            "A unit of length equal to twelve inches.",
            rank=2, access="common_secondary",
            recognition=0.96, activation=0.55, confidence=0.90),
    },
    "branch": {
        "branch_tree": sense(
            "An arm of a tree growing out from the trunk.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.94),
        "branch_office": sense(
            "A local office of a bank or company.",
            rank=2, access="common_secondary",
            recognition=0.92, activation=0.35, confidence=0.86),
    },
    "sole": {
        "sole_shoe": sense(
            "The bottom part of a shoe or foot.",
            rank=1, access="primary", recognition=0.94, activation=0.80, confidence=0.88),
        "sole_fish": sense(
            "A flat sea fish eaten as food.",
            rank=2, access="specialist",
            recognition=0.52, activation=0.10, confidence=0.82),
    },
    "slide": {
        "slide_playground": sense(
            "A smooth sloping structure children slide down.",
            rank=1, access="primary", recognition=0.97, activation=0.85, confidence=0.90),
        "slide_move": sense(
            "To move smoothly along a surface.",
            pos="verb", rank=2, access="common_secondary",
            recognition=0.97, activation=0.60, confidence=0.88),
        "slide_lab": sense(
            "The small glass plate a specimen sits on under a microscope.",
            rank=3, access="common_secondary",
            recognition=0.80, activation=0.22, confidence=0.82),
    },
    "dice": {
        "dice_game": sense(
            "Small cubes marked with dots, thrown in games.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.94),
        "dice_cut": sense(
            "To cut food into small cubes.",
            pos="verb", rank=2, access="common_secondary",
            recognition=0.88, activation=0.30, confidence=0.84),
    },
    "charcoal": {
        "charcoal_fuel": sense(
            "Black lumps of burnt wood used as fuel for grilling.",
            rank=1, access="primary", recognition=0.96, activation=0.85, confidence=0.90),
        "charcoal_drawing": sense(
            "A stick of charred wood used for drawing.",
            rank=2, access="common_secondary",
            recognition=0.88, activation=0.40, confidence=0.85),
        "charcoal_color": sense(
            "A very dark grey colour.",
            pos="adjective", rank=3, access="common_secondary",
            recognition=0.85, activation=0.28, confidence=0.83),
    },
    "foundation": {
        "foundation_building": sense(
            "The solid base a building is built on.",
            rank=1, access="primary", recognition=0.97, activation=0.82, confidence=0.90),
        "foundation_makeup": sense(
            "A cosmetic cream applied as a base layer on the face.",
            rank=2, access="common_secondary",
            recognition=0.88, activation=0.42, confidence=0.86),
    },
    "balance": {
        "balance_steady": sense(
            "The state of staying steady and not falling over.",
            rank=1, access="primary", recognition=0.98, activation=0.88, confidence=0.92),
        "balance_money": sense(
            "The amount of money in an account.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.48, confidence=0.88),
    },
    "white": {
        "white_color": sense(
            "The colour of snow and milk.",
            pos="adjective", rank=1, access="primary",
            recognition=0.99, activation=0.97, confidence=0.95),
        "white_surname": sense(
            "White, a common English family name.",
            pos="proper_noun", kind="proper_name", rank=2, access="common_secondary",
            recognition=0.86, activation=0.18, confidence=0.84,
            display="White", proper=True),
    },
    "apple": {
        "apple_fruit": sense(
            "The round edible fruit of an apple tree.",
            rank=1, access="primary", recognition=0.99, activation=0.97, confidence=0.95),
        "apple_company": sense(
            "Apple, the American technology company.",
            pos="proper_noun", kind="brand", rank=2, access="common_secondary",
            recognition=0.98, activation=0.55, confidence=0.92,
            display="Apple", proper=True),
    },
    "bob": {
        "bob_haircut": sense(
            "A short haircut of even length all round.",
            rank=1, access="primary", recognition=0.88, activation=0.55, confidence=0.84),
        "bob_name": sense(
            "Bob, a short form of the name Robert.",
            pos="proper_noun", kind="proper_name", rank=2, access="common_secondary",
            recognition=0.97, activation=0.70, confidence=0.90,
            display="Bob", proper=True),
    },
    "buzz": {
        "buzz_sound": sense(
            "The low humming sound made by a bee or an electric device.",
            rank=1, access="primary", recognition=0.98, activation=0.92, confidence=0.93),
        "buzz_character": sense(
            "Buzz Lightyear, a character from the Toy Story films.",
            pos="proper_noun", kind="title", rank=2, access="specialist",
            recognition=0.72, activation=0.12, confidence=0.82,
            display="Buzz", proper=True),
    },
    "mason": {
        "mason_trade": sense(
            "A worker who builds with stone or brick.",
            rank=1, access="primary", recognition=0.88, activation=0.62, confidence=0.85),
        "mason_name": sense(
            "Mason, an English family name and boy's given name.",
            pos="proper_noun", kind="proper_name", rank=2, access="common_secondary",
            recognition=0.86, activation=0.35, confidence=0.84,
            display="Mason", proper=True),
    },
    "carpenter": {
        "carpenter_trade": sense(
            "A worker who makes and repairs things from wood.",
            rank=1, access="primary", recognition=0.98, activation=0.92, confidence=0.93),
        "carpenter_name": sense(
            "Carpenter, an English family name taken from the trade.",
            pos="proper_noun", kind="proper_name", rank=2, access="common_secondary",
            recognition=0.82, activation=0.20, confidence=0.82,
            display="Carpenter", proper=True),
    },
    "amber": {
        "amber_resin": sense(
            "Hard yellow fossilised tree resin used in jewellery.",
            rank=1, access="primary", recognition=0.90, activation=0.68, confidence=0.86),
        "amber_color": sense(
            "A warm yellow-orange colour.",
            pos="adjective", rank=2, access="common_secondary",
            recognition=0.88, activation=0.42, confidence=0.85),
        "amber_name": sense(
            "Amber, a girl's given name taken from the gem.",
            pos="proper_noun", kind="proper_name", rank=3, access="common_secondary",
            recognition=0.85, activation=0.28, confidence=0.83,
            display="Amber", proper=True),
    },
    "bunker": {
        "bunker_shelter": sense(
            "A reinforced underground shelter.",
            rank=1, access="primary", recognition=0.94, activation=0.82, confidence=0.90),
        "bunker_golf": sense(
            "A sand-filled hollow on a golf course.",
            rank=2, access="specialist",
            recognition=0.55, activation=0.10, confidence=0.82),
    },
    "boom": {
        "boom_sound": sense(
            "A deep loud resonant sound.",
            rank=1, access="primary", recognition=0.97, activation=0.90, confidence=0.92),
        "boom_sailing": sense(
            "The horizontal pole at the foot of a sail.",
            rank=2, access="specialist",
            recognition=0.45, activation=0.06, confidence=0.82),
    },
    "button": {
        "button_clothing": sense(
            "A small disc that fastens clothing through a hole.",
            rank=1, access="primary", recognition=0.99, activation=0.92, confidence=0.94),
        "button_press": sense(
            "A part of a device that you press to make it work.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.62, confidence=0.90),
        "button_mushroom": sense(
            "A small young white mushroom.",
            rank=3, access="specialist",
            recognition=0.48, activation=0.06, confidence=0.80),
    },
    "paint": {
        "paint_substance": sense(
            "Coloured liquid spread on a surface to colour it.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "paint_horse": sense(
            "A Paint horse, an American breed with patches of colour.",
            rank=2, access="specialist",
            recognition=0.30, activation=0.03, confidence=0.80),
    },
    "gum": {
        "gum_chewing": sense(
            "A sweet chewy substance that is chewed but not swallowed.",
            rank=1, access="primary", recognition=0.99, activation=0.92, confidence=0.93),
        "gum_mouth": sense(
            "The firm pink flesh around the roots of the teeth.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.48, confidence=0.88),
    },
    "seal": {
        "seal_animal": sense(
            "A sea mammal with flippers that lives in cold water.",
            rank=1, access="primary", recognition=0.99, activation=0.90, confidence=0.93),
        "seal_close": sense(
            "A tight closure that keeps air or water out.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.45, confidence=0.87),
    },
    "crown": {
        "crown_royal": sense(
            "The ornamental headdress worn by a king or queen.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.94),
        "crown_tooth": sense(
            "An artificial cap fitted over a damaged tooth.",
            rank=2, access="common_secondary",
            recognition=0.86, activation=0.32, confidence=0.85),
        "crown_tree": sense(
            "The spreading top part of a tree.",
            rank=3, access="specialist",
            recognition=0.48, activation=0.07, confidence=0.80),
    },
    "conductor": {
        "conductor_music": sense(
            "The person who directs an orchestra.",
            rank=1, access="primary", recognition=0.96, activation=0.82, confidence=0.90),
        "conductor_train": sense(
            "The railway official who checks tickets on a train.",
            rank=2, access="common_secondary",
            recognition=0.90, activation=0.42, confidence=0.86),
        "conductor_physics": sense(
            "A material that lets electricity pass through it.",
            rank=3, access="common_secondary",
            recognition=0.85, activation=0.30, confidence=0.84),
    },
    "record": {
        "record_disc": sense(
            "A flat black vinyl disc that music is played from.",
            rank=1, access="primary", recognition=0.96, activation=0.78, confidence=0.89),
        "record_best": sense(
            "The best performance ever achieved in a sport.",
            rank=2, access="common_secondary",
            recognition=0.97, activation=0.60, confidence=0.89),
        "record_write": sense(
            "To write something down so it is kept.",
            pos="verb", rank=3, access="common_secondary",
            recognition=0.94, activation=0.40, confidence=0.86),
    },
    "swallow": {
        "swallow_throat": sense(
            "To make food or drink pass down the throat.",
            pos="verb", rank=1, access="primary",
            recognition=0.99, activation=0.93, confidence=0.94),
        "swallow_bird": sense(
            "A small fast bird with a forked tail.",
            rank=2, access="common_secondary",
            recognition=0.85, activation=0.28, confidence=0.84),
    },
    "level": {
        "level_flat": sense(
            "Being flat and even, at the same height throughout.",
            pos="adjective", rank=1, access="primary",
            recognition=0.98, activation=0.85, confidence=0.91),
        "level_tool": sense(
            "A tool with a bubble in liquid that shows whether a surface is flat.",
            rank=2, access="common_secondary",
            recognition=0.86, activation=0.35, confidence=0.85),
        "level_stage": sense(
            "One stage of a video game.",
            rank=3, access="common_secondary",
            recognition=0.92, activation=0.38, confidence=0.85),
    },
    "marble": {
        "marble_stone": sense(
            "A hard polished stone used for statues and floors.",
            rank=1, access="primary", recognition=0.97, activation=0.85, confidence=0.91),
        "marble_toy": sense(
            "A small glass ball children play with.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.50, confidence=0.88),
    },
    "jersey": {
        "jersey_shirt": sense(
            "A knitted shirt worn by a sports team.",
            rank=1, access="primary", recognition=0.94, activation=0.80, confidence=0.89),
        "jersey_cattle": sense(
            "A Jersey, a small fawn breed of dairy cow.",
            pos="proper_noun", kind="proper_name", rank=2, access="specialist",
            recognition=0.42, activation=0.05, confidence=0.80),
        "jersey_fabric": sense(
            "A soft stretchy knitted fabric.",
            rank=3, access="specialist",
            recognition=0.50, activation=0.08, confidence=0.80),
    },
    "screen": {
        "screen_display": sense(
            "The flat surface of a television, phone or computer that shows pictures.",
            rank=1, access="primary", recognition=0.99, activation=0.95, confidence=0.95),
        "screen_mesh": sense(
            "A frame covered with fine mesh that keeps insects out.",
            rank=2, access="common_secondary",
            recognition=0.85, activation=0.28, confidence=0.83),
    },
    "stage": {
        "stage_theatre": sense(
            "The raised platform in a theatre where performers appear.",
            rank=1, access="primary", recognition=0.99, activation=0.92, confidence=0.94),
        "stage_phase": sense(
            "One step in a process, such as a section of a rocket.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.42, confidence=0.87),
    },
    "wings": {
        "wings_bird": sense(
            "The pair of limbs a bird or insect uses to fly.",
            rank=1, access="primary", recognition=0.99, activation=0.95, confidence=0.95),
        "wings_theatre": sense(
            "The sides of a stage, out of sight of the audience.",
            rank=2, access="specialist",
            recognition=0.52, activation=0.08, confidence=0.81),
    },
    "key": {
        "key_lock": sense(
            "A shaped piece of metal that opens a lock.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "key_music": sense(
            "The set of notes a piece of music is based on.",
            rank=2, access="common_secondary",
            recognition=0.88, activation=0.32, confidence=0.85),
        "key_map": sense(
            "The panel on a map explaining what its symbols mean.",
            rank=3, access="common_secondary",
            recognition=0.82, activation=0.22, confidence=0.83),
    },
    "point": {
        "point_sharp": sense(
            "The sharp end of something.",
            rank=1, access="primary", recognition=0.97, activation=0.80, confidence=0.90),
        "point_gesture": sense(
            "To hold out a finger to show where something is.",
            pos="verb", rank=2, access="common_secondary",
            recognition=0.98, activation=0.68, confidence=0.90),
        "point_score": sense(
            "A unit of scoring in a game.",
            rank=3, access="common_secondary",
            recognition=0.98, activation=0.60, confidence=0.89),
    },
    "ring": {
        "ring_jewellery": sense(
            "A circular band worn on a finger.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.95),
        "ring_sound": sense(
            "The clear sound made by a bell or a telephone.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.62, confidence=0.90),
        "ring_arena": sense(
            "The roped square where boxers or circus acts perform.",
            rank=3, access="common_secondary",
            recognition=0.93, activation=0.40, confidence=0.86),
        "ring_circle": sense(
            "A circular band of material, such as the rings of Saturn.",
            rank=4, access="common_secondary",
            recognition=0.90, activation=0.32, confidence=0.85),
    },
    "case": {
        "case_container": sense(
            "A container made to hold and protect something.",
            rank=1, access="primary", recognition=0.98, activation=0.85, confidence=0.91),
        "case_investigation": sense(
            "A matter being investigated by police or decided in court.",
            rank=2, access="common_secondary",
            recognition=0.96, activation=0.55, confidence=0.89),
    },
    "green": {
        "green_color": sense(
            "The colour of grass and leaves.",
            pos="adjective", rank=1, access="primary",
            recognition=0.99, activation=0.97, confidence=0.95),
        "green_golf": sense(
            "The smooth area of short grass around a golf hole.",
            rank=2, access="common_secondary",
            recognition=0.80, activation=0.20, confidence=0.83),
    },
    "pass": {
        "pass_move": sense(
            "To go by something, or to hand something to someone.",
            pos="verb", rank=1, access="primary",
            recognition=0.99, activation=0.90, confidence=0.93),
        "pass_ticket": sense(
            "A card or ticket giving permission to enter.",
            rank=2, access="common_secondary",
            recognition=0.94, activation=0.45, confidence=0.87),
    },
    "cable": {
        "cable_wire": sense(
            "A thick wire or bundle of wires carrying power or signals.",
            rank=1, access="primary", recognition=0.98, activation=0.88, confidence=0.92),
        "cable_tv": sense(
            "Television delivered by wire rather than aerial.",
            rank=2, access="common_secondary",
            recognition=0.92, activation=0.40, confidence=0.86),
    },
    "pool": {
        "pool_swimming": sense(
            "A tank of water built for swimming in.",
            rank=1, access="primary", recognition=0.99, activation=0.94, confidence=0.94),
        "pool_water": sense(
            "A small area of still water.",
            rank=2, access="common_secondary",
            recognition=0.95, activation=0.48, confidence=0.88),
    },
    "bolt": {
        "bolt_fastener": sense(
            "A metal pin with a thread, fastened with a nut.",
            rank=1, access="primary", recognition=0.96, activation=0.82, confidence=0.90),
        "bolt_lock": sense(
            "A sliding metal bar that fastens a door.",
            rank=2, access="common_secondary",
            recognition=0.90, activation=0.40, confidence=0.86),
    },
    "star": {
        "star_sky": sense(
            "A distant sun seen as a point of light in the night sky.",
            rank=1, access="primary", recognition=0.99, activation=0.96, confidence=0.95),
        "star_shape": sense(
            "The pointed symbol drawn to represent a star.",
            rank=2, access="common_secondary",
            recognition=0.98, activation=0.60, confidence=0.90),
    },
}


# --------------------------------------------------------------------------- 3
# Привязка «слово + категория -> значение». Без неё объявленные значения лежат
# в базе мёртвым грузом: связь по-прежнему не знает, каким смыслом слово стоит.
ASSIGNMENTS: dict[str, dict[str, str]] = {
    "trouble": {"board_games": "trouble_board_game"},
    "risk": {"board_games": "risk_board_game"},
    "sorry": {"board_games": "sorry_board_game",
              "manners": "sorry_apology", "polite_words": "sorry_apology"},
    "life": {"board_games": "life_game", "cereal_brands": "life_cereal"},
    "monopoly": {"board_games": "monopoly_game"},
    "scrabble": {"board_games": "scrabble_game"},
    "chess": {"board_games": "chess_game", "board_and_card_games": "chess_game",
              "card_and_dice_games": "chess_game", "hobby_verbs": "chess_game",
              "ref_individual_sports": "chess_game", "pie_types": "chess_game"},
    "checkers": {"board_games": "checkers_game",
                 "board_and_card_games": "checkers_game",
                 "card_and_dice_games": "checkers_game"},
    "clue": {"board_games": "clue_board_game",
             "detective_words": "clue_hint", "detective_work": "clue_hint"},
    "battleship": {"board_games": "battleship_game"},
    "cards": {"board_games": "cards_game", "fortune_telling": "cards_game"},
    "backgammon": {"board_games": "backgammon_game",
                   "board_and_card_games": "backgammon_game"},
    "dominoes": {"card_and_dice_games": "dominoes_game",
                 "board_and_card_games": "dominoes_game"},
    "marbles": {"card_and_dice_games": "marbles_game",
                "playground_games": "marbles_game"},
    "hopscotch": {"card_and_dice_games": "hopscotch_game",
                  "playground_games": "hopscotch_game"},
    "jacks": {"card_and_dice_games": "jacks_game"},
    "tag": {"card_and_dice_games": "tag_game", "playground_games": "tag_game",
            "pet_supplies": "tag_label", "shopping_words": "tag_label",
            "social_media_words": "tag_label", "things_on_a_keychain": "tag_label"},
    "hearts": {"card_games": "hearts_game", "card_suits": "hearts_suit"},
    "spades": {"card_games": "spades_game", "card_suits": "spades_suit"},

    "orange": {"fruits": "orange_fruit", "citrus_fruits": "orange_fruit",
               "fruit_trees": "orange_fruit", "things_with_seeds": "orange_fruit",
               "round_things": "orange_fruit", "colors": "orange_color"},

    "north": {"directions": "north_direction", "map_words": "north_direction"},
    "south": {"directions": "south_direction", "map_words": "south_direction"},
    "east": {"directions": "east_direction", "map_words": "east_direction"},
    "west": {"directions": "west_direction", "map_words": "west_direction"},

    "bark": {"animal_sounds": "bark_sound", "dog_things": "bark_sound",
             "tree_parts": "bark_tree", "plant_parts": "bark_tree",
             "pine_and_cones": "bark_tree", "things_in_the_forest": "bark_tree"},
    "bass": {"fish_species": "bass_fish", "pond_fish": "bass_fish",
             "in_a_band": "bass_low", "singing_voices": "bass_low",
             "string_instruments": "bass_low", "types_of_guitars": "bass_low"},
    "turkey": {"asian_countries": "turkey_country", "birds": "turkey_bird",
               "farm_animals": "turkey_bird", "farm_bird_words": "turkey_bird",
               "livestock": "turkey_bird", "meats": "turkey_bird",
               "sandwich_fillings": "turkey_bird", "thanksgiving_foods": "turkey_bird",
               "bowling_words": "turkey_bird"},
    "silver": {"colors": "silver_color", "elements": "silver_metal",
               "elements_more": "silver_metal", "metals": "silver_metal",
               "precious_materials": "silver_metal", "shiny_things": "silver_metal"},
    "compass": {"camping_gear": "compass_navigation", "diving_gear": "compass_navigation",
                "exploration_words": "compass_navigation", "map_words": "compass_navigation",
                "military_things": "compass_navigation",
                "navigation_tools": "compass_navigation", "pirate_words": "compass_navigation",
                "inventions": "compass_navigation",
                "measurement_devices": "compass_drawing",
                "measuring_tools": "compass_drawing", "school_supplies": "compass_drawing"},
    "spring": {"seasons": "spring_season", "calendar_words": "spring_season",
               "easter": "spring_season", "things_that_stretch": "spring_coil",
               "ways_of_moving": "spring_coil", "bodies_of_water": "spring_water"},
    "iron": {"elements": "iron_metal", "metals": "iron_metal",
             "hard_things": "iron_metal", "nutrients": "iron_metal",
             "vitamins_and_minerals": "iron_metal",
             "laundry_care": "iron_appliance", "laundry_things": "iron_appliance",
             "hot_things": "iron_appliance", "tailor_words": "iron_appliance",
             "things_that_plug_in": "iron_appliance", "wardrobe_care": "iron_appliance",
             "golf_words": "iron_golf"},
    "cast": {"movie_words": "cast_group", "theater_words": "cast_group",
             "groups_of_people": "cast_group", "detective_procedures": "cast_group",
             "medical_procedures": "cast_plaster", "things_worn_on_hands": "cast_plaster"},
    "scale": {"bathroom_items": "scale_weighing", "baker_words": "scale_weighing",
              "butcher_words": "scale_weighing", "cooking_hobby": "scale_weighing",
              "lab_equipment": "scale_weighing", "measurement_devices": "scale_weighing",
              "measuring_tools": "scale_weighing", "world_markets": "scale_weighing",
              "animal_coverings": "scale_animal",
              "music_words": "scale_music",
              "map_legend": "scale_map", "map_words": "scale_map",
              "model_building": "scale_map", "startup_words": "scale_map"},
    "heart": {"internal_organs": "heart_organ", "shapes": "heart_shape",
              "card_words": "heart_suit"},
    "trunk": {"tree_parts": "trunk_tree", "car_parts": "trunk_car",
              "animal_body_parts": "trunk_elephant", "storage_containers": "trunk_chest",
              "bags": "trunk_chest"},
    "mouse": {"nocturnal_animals": "mouse_animal", "pests": "mouse_animal",
              "pets": "mouse_animal", "rodents": "mouse_animal",
              "quiet_things": "mouse_animal",
              "computer_parts": "mouse_computer", "video_gaming": "mouse_computer"},
    "monitor": {"computer_parts": "monitor_screen", "screens": "monitor_screen",
                "video_gaming": "monitor_screen", "security_tech": "monitor_screen",
                "baby_things": "monitor_medical", "first_aid_actions": "monitor_medical",
                "hospital_things": "monitor_medical", "medical_tools": "monitor_medical",
                "lizards": "monitor_lizard", "reptiles": "monitor_lizard"},
    "keyboard": {"computer_parts": "keyboard_computer",
                 "things_made_of_plastic": "keyboard_computer",
                 "things_with_buttons": "keyboard_computer",
                 "video_gaming": "keyboard_computer", "writing_tools": "keyboard_computer",
                 "in_a_band": "keyboard_instrument",
                 "musical_instruments": "keyboard_instrument"},
    "cardinal": {"birds": "cardinal_bird", "songbirds": "cardinal_bird",
                 "red_things": "cardinal_bird",
                 "religious_leaders": "cardinal_clergy"},
    "chest": {"body_parts": "chest_body",
              "bedroom_things": "chest_box", "boxes_and_cases": "chest_box",
              "pirate_words": "chest_box", "storage_containers": "chest_box"},
    "beam": {"carpentry_words": "beam_structure", "parts_of_a_house": "beam_structure",
             "gymnastics_events": "beam_structure",
             "facial_expressions": "beam_smile"},
    "bow": {"body_language": "bow_bend",
            "archery_words": "bow_weapon", "knights_and_armor": "bow_weapon",
            "weapons_of_the_past": "bow_weapon",
            "instruments_you_strum": "bow_music", "music_practice": "bow_music"},
    "hood": {"clothing_parts": "hood_garment", "hats": "hood_garment",
             "rainy_day_gear": "hood_garment", "winter_clothing": "hood_garment",
             "diving_gear": "hood_garment",
             "car_parts": "hood_car", "kitchen_appliances": "hood_car",
             "photography_hobby": "hood_car"},
    "coral": {"aquarium_tank": "coral_animal", "coral_reef": "coral_animal",
              "ocean_animals": "coral_animal", "ocean_floor": "coral_animal",
              "ocean_products": "coral_animal", "gemstones": "coral_animal",
              "color_words_advanced": "coral_color"},
    "trailer": {"things_with_wheels": "trailer_vehicle",
                "at_the_movies": "trailer_film", "movie_words": "trailer_film"},
    "triangle": {"shapes": "triangle_shape", "yoga_poses": "triangle_shape",
                 "music_class_things": "triangle_instrument",
                 "percussion": "triangle_instrument"},
    "square": {"shapes": "square_shape", "ref_polygons": "square_shape",
               "shape_adjectives": "square_shape",
               "carpentry_words": "square_tool", "hand_tools": "square_tool",
               "math_operations": "square_math",
               "payment_brands": "square_brand"},
    "foot": {"body_parts": "foot_body",
             "things_measured_in_inches": "foot_measure",
             "transportation_history": "foot_body"},
    "branch": {"tree_parts": "branch_tree", "things_in_the_forest": "branch_tree",
               "banking_words": "branch_office"},
    "sole": {"shoe_parts": "sole_shoe", "saltwater_fish": "sole_fish"},
    "slide": {"dance_moves": "slide_move", "carrying_actions": "slide_move",
              "ways_of_moving": "slide_move", "lab_equipment": "slide_lab"},
    "dice": {"board_game_pieces": "dice_game", "fortune_telling": "dice_game",
             "square_things": "dice_game", "things_that_have_a_face": "dice_game",
             "cooking_actions": "dice_cut"},
    "charcoal": {"barbecue": "charcoal_fuel", "things_that_burn": "charcoal_fuel",
                 "art_supplies": "charcoal_drawing", "art_tools": "charcoal_drawing",
                 "writing_tools": "charcoal_drawing",
                 "color_words_advanced": "charcoal_color"},
    "foundation": {"architecture_words": "foundation_building",
                   "parts_of_a_house": "foundation_building",
                   "makeup": "foundation_makeup"},
    "balance": {"senses_and_perception": "balance_steady", "wellness": "balance_steady",
                "accounting_words": "balance_money", "banking_words": "balance_money"},
    "white": {"colors": "white_color", "bread_types": "white_color",
              "parts_of_the_eye": "white_color", "potato_varieties": "white_color",
              "rice_types": "white_color", "sandwich_breads": "white_color",
              "teas": "white_color", "common_surnames": "white_surname"},
    "apple": {"fruits": "apple_fruit", "fruit_trees": "apple_fruit",
              "pie_ingredients": "apple_fruit", "pie_types": "apple_fruit",
              "red_things": "apple_fruit", "round_things": "apple_fruit",
              "things_with_seeds": "apple_fruit", "trees": "apple_fruit",
              "fairy_tale_things": "apple_fruit",
              "tech_companies": "apple_company"},
    "bob": {"hair_words": "bob_haircut", "hairstyles": "bob_haircut",
            "nicknames": "bob_name", "nicknames_for_names": "bob_name"},
    "buzz": {"animal_sounds": "buzz_sound", "bell_and_alarm": "buzz_sound",
             "machine_sounds": "buzz_sound", "nature_sounds": "buzz_sound",
             "onomatopoeia": "buzz_sound", "disney_characters": "buzz_character"},
    "mason": {"building_trades": "mason_trade", "old_professions": "mason_trade",
              "boys_names": "mason_name", "nature_surnames": "mason_name"},
    "carpenter": {"building_trades": "carpenter_trade", "jobs_with_tools": "carpenter_trade",
                  "nature_surnames": "carpenter_name"},
    "amber": {"ocean_products": "amber_resin", "precious_materials": "amber_resin",
              "perfume_words": "amber_resin",
              "color_words_advanced": "amber_color", "nature_names": "amber_name"},
    "bunker": {"military_things": "bunker_shelter", "underground_places": "bunker_shelter",
               "golf_words": "bunker_golf"},
    "boom": {"loud_noises": "boom_sound", "musical_sounds": "boom_sound",
             "onomatopoeia": "boom_sound",
             "sailing_terms": "boom_sailing", "sailing_words": "boom_sailing"},
    "button": {"clothing_parts": "button_clothing", "sewing_supplies": "button_clothing",
               "sewing_words": "button_clothing", "crafting_materials": "button_clothing",
               "collecting_hobbies": "button_clothing", "joining_actions": "button_clothing",
               "round_things": "button_clothing", "things_with_holes": "button_clothing",
               "mushroom_types": "button_mushroom"},
    "paint": {"art_class_things": "paint_substance", "art_supplies": "paint_substance",
              "building_actions": "paint_substance", "crafting_materials": "paint_substance",
              "liquids": "paint_substance", "model_building": "paint_substance",
              "painting_supplies": "paint_substance", "things_in_a_garage": "paint_substance",
              "horse_breeds": "paint_horse"},
    "gum": {"candy": "gum_chewing", "sticky_things": "gum_chewing",
            "things_in_a_glove_box": "gum_chewing", "things_in_a_purse": "gum_chewing",
            "things_that_stretch": "gum_chewing", "vending_machine_items": "gum_chewing",
            "adhesives": "gum_chewing", "dental_words": "gum_mouth"},
    "seal": {"arctic_animals": "seal_animal", "ocean_animals": "seal_animal",
             "sea_mammals": "seal_animal", "zoo_animals": "seal_animal",
             "things_made_of_rubber": "seal_close"},
    "crown": {"royalty": "crown_royal", "hats": "crown_royal",
              "flags_and_symbols": "crown_royal",
              "dental_words": "crown_tooth", "dentist_things": "crown_tooth",
              "tree_parts": "crown_tree"},
    "conductor": {"instruments_in_an_orchestra": "conductor_music",
                  "music_class_things": "conductor_music",
                  "train_words": "conductor_train", "transport_jobs": "conductor_train",
                  "electricity_words": "conductor_physics"},
    "record": {"collecting_hobbies": "record_disc", "things_that_spin": "record_disc",
               "sports_scoring": "record_best", "lab_actions": "record_write"},
    "swallow": {"body_movements": "swallow_throat", "eating_actions": "swallow_throat",
                "songbirds": "swallow_bird"},
    "level": {"building_actions": "level_flat", "masonry_words": "level_flat",
              "carpentry_words": "level_tool", "hand_tools": "level_tool",
              "measuring_tools": "level_tool", "sewing_and_repair": "level_tool",
              "things_in_a_toolbox": "level_tool",
              "video_game_words": "level_stage"},
    "marble": {"building_materials": "marble_stone", "hard_things": "marble_stone",
               "precious_materials": "marble_stone", "rocks_and_minerals": "marble_stone",
               "sculpture_materials": "marble_stone", "cake_types": "marble_stone",
               "collecting_hobbies": "marble_toy", "round_things": "marble_toy",
               "things_made_of_glass": "marble_toy", "toys": "marble_toy"},
    "jersey": {"cycling_words": "jersey_shirt", "fan_things": "jersey_shirt",
               "cattle_and_farm_breeds": "jersey_cattle",
               "fabric_types": "jersey_fabric"},
    "screen": {"at_the_movies": "screen_display", "computer_parts": "screen_display",
               "phone_words": "screen_display", "tv_words": "screen_display",
               "things_made_of_glass": "screen_display",
               "things_that_break": "screen_display", "light_sources": "screen_display",
               "printing_words": "screen_mesh", "transparent_things": "screen_mesh"},
    "stage": {"at_the_theater": "stage_theatre", "theater_words": "stage_theatre",
              "dance_class": "stage_theatre", "school_places": "stage_theatre",
              "rocket_parts": "stage_phase"},
    "wings": {"parts_of_a_bird": "wings_bird",
              "things_that_come_in_pairs": "wings_bird",
              "theater_stage_terms": "wings_theatre", "theater_words": "wings_theatre"},
    "key": {"at_the_hotel": "key_lock", "bedroom_things": "key_lock",
            "collecting_hobbies": "key_lock", "locksmith_words": "key_lock",
            "things_in_a_junk_drawer": "key_lock", "things_made_of_metal": "key_lock",
            "things_on_a_keychain": "key_lock", "under_lock": "key_lock",
            "music_words": "key_music", "map_words": "key_map"},
    "point": {"blades": "point_sharp",
              "body_language": "point_gesture", "body_movements": "point_gesture",
              "hand_actions": "point_gesture", "sports_scoring": "point_score"},
    "ring": {"jewelry": "ring_jewellery", "things_on_a_keychain": "ring_jewellery",
             "magic_objects": "ring_jewellery", "magic_tricks": "ring_jewellery",
             "bell_and_alarm": "ring_sound", "musical_sounds": "ring_sound",
             "onomatopoeia": "ring_sound",
             "boxing_words": "ring_arena", "circus_words": "ring_arena",
             "sports_venues": "ring_arena", "juggling_words": "ring_arena",
             "round_things": "ring_circle", "solar_system_words": "ring_circle",
             "space_objects": "ring_circle"},
    "case": {"boxes_and_cases": "case_container", "computer_parts": "case_container",
             "music_practice": "case_container", "phone_words": "case_container",
             "storage_containers": "case_container", "butcher_words": "case_container",
             "detective_words": "case_investigation"},
    "green": {"colors": "green_color", "olive_types": "green_color",
              "teas": "green_color", "tomato_varieties": "green_color",
              "golf_words": "green_golf"},
    "pass": {"sports_actions": "pass_move", "card_tricks": "pass_move",
             "grades_and_marks": "pass_move", "kitchen_brigade": "pass_move",
             "tickets_and_passes": "pass_ticket"},
    "cable": {"computer_parts": "cable_wire", "electrical_words": "cable_wire",
              "power_and_batteries": "cable_wire", "video_gaming": "cable_wire",
              "tv_words": "cable_tv"},
    "pool": {"at_the_pool": "pool_swimming", "hotel_words": "pool_swimming",
             "seasons_summer": "pool_swimming", "sports_venues": "pool_swimming",
             "things_that_hold_water": "pool_swimming",
             "bodies_of_water": "pool_water", "body_of_water_types": "pool_water",
             "cave_things": "pool_water"},
    "bolt": {"fasteners": "bolt_fastener", "building_actions": "bolt_fastener",
             "sewing_and_repair": "bolt_fastener", "things_that_stick_out": "bolt_fastener",
             "locksmith_words": "bolt_lock"},
    "star": {"cloud_and_sky": "star_sky", "light_sources": "star_sky",
             "navigation_tools": "star_sky", "night_sky_things": "star_sky",
             "space_objects": "star_sky", "shiny_things": "star_sky",
             "shapes": "star_shape", "christmas_things": "star_shape",
             "flags_and_symbols": "star_shape", "religious_symbols": "star_shape"},
}


def main() -> None:
    raw = json.loads(SENSE_MAP.read_text(encoding="utf-8"))
    raw.setdefault("audience_profile", AUDIENCE)
    senses = raw.setdefault("senses", {})
    assignments = raw.setdefault("assignments", {})

    for word, entries in SENSES.items():
        bucket = senses.setdefault(word, {})
        for key, spec in entries.items():
            bucket[key] = {**bucket.get(key, {}), **spec}
    for word, by_category in ASSIGNMENTS.items():
        assignments.setdefault(word, {}).update(by_category)

    SENSE_MAP.write_text(
        json.dumps(raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    existing = NOT_HOMONYMS.read_text(encoding="utf-8").rstrip("\n").split("\n")
    known = {line.split("#")[0].strip() for line in existing if line.split("#")[0].strip()}
    added = sorted(word for word in MONOSEMOUS if word not in known)
    if added:
        block = [
            "",
            "# Партия разбора слоя доступности значений. Слова проверены глазами:",
            "# разброс по темам есть, второго смысла нет.",
            *added,
        ]
        NOT_HOMONYMS.write_text("\n".join([*existing, *block]) + "\n", encoding="utf-8")

    print(f"значений объявлено: {sum(len(v) for v in SENSES.values())} у {len(SENSES)} слов")
    print(f"привязок: {sum(len(v) for v in ASSIGNMENTS.values())}")
    print(f"однозначных слов дописано в _not_homonyms.txt: {len(added)}")


if __name__ == "__main__":
    main()
