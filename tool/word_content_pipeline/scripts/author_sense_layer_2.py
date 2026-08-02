#!/usr/bin/env python3
"""Вторая партия разбора значений: резерв кандидатов для первой линейки.

Первая партия (`author_sense_layer.py`) закрыла приёмочные случаи и слова,
блокировавшие больше всего категорий. Этого хватило, чтобы база перестала
пропускать `Life / risk / sorry / trouble`, но не хватило, чтобы собрать из неё
двадцать уровней: генератор упирался в бюджет связности и останавливался на
одиннадцатом.

Очередь для этой партии собрана не на глаз, а запросом: связи, которые стоят в
четвёрках, годных по всем остальным порогам первой линейки И имеющих живую
попарную ассоциацию по SWOW. То есть разбирается ровно то, что превращается в
играбельный контент, а не словарь целиком.

Две половины, как и в первой партии.

`SCORES` — у слова значения уже разведены (это сделал `_ambiguous.json`), не
хватает только доступности. Определения здесь не повторяются: они в базе есть,
и перетирать их незачем.

`SENSES` и `MONOSEMOUS` — слова, у которых значений нет вовсе.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSE_MAP = ROOT / "data" / "seed" / "_sense_map.json"
NOT_HOMONYMS = ROOT / "data" / "seed" / "_not_homonyms.txt"

AUDIENCE = "general_en_us_adult"
REVIEW = "sense_review"


def spec(rank, access, rec, act, *, kind="lexical", conf=0.88, definition=None,
         pos=None, display=None, proper=False) -> dict:
    entry = {
        "sense_kind": kind,
        "dominance_rank": rank,
        "accessibility_class": access,
        "recognition_score": rec,
        "activation_score": act,
        "audience_profile": AUDIENCE,
        "quality_source": REVIEW,
        "quality_confidence": conf,
    }
    if definition:
        entry["definition"] = definition
    if pos:
        entry["part_of_speech"] = pos
    if display:
        entry["display"] = display
    if proper:
        entry["is_proper_noun"] = True
    return entry


# --------------------------------------------------------------------------- 1
# Значения разведены раньше, здесь только доступность.
# Формат: слово -> {ключ значения: (ранг, класс, узнаваемость, активация)}
P = "primary"
S = "common_secondary"
X = "specialist"
O = "obscure"  # noqa: E741 — читается как класс, а не как переменная

SCORES: dict[str, dict[str, tuple]] = {
    "bench":    {"bench_seat": (1, P, .97, .92), "bench_court": (2, X, .55, .09)},
    "bill":     {"bill_money": (1, P, .96, .78), "bill_charge": (2, S, .95, .60),
                 "bill_law": (3, S, .88, .32), "bill_name": (4, S, .90, .28)},
    "board":    {"board_plank": (1, P, .96, .80), "board_game": (2, S, .94, .55),
                 "board_committee": (3, S, .88, .30)},
    "cabinet":  {"cabinet_furniture": (1, P, .97, .88), "cabinet_government": (2, S, .86, .30)},
    "calf":     {"calf_cow": (1, P, .96, .80), "calf_leg": (2, S, .90, .45)},
    "calm":     {"calm_person": (1, P, .98, .90), "calm_sea": (2, S, .88, .35)},
    "carbon":   {"carbon_element": (1, P, .95, .85), "carbon_paper": (2, X, .48, .07)},
    "card":     {"card_playing": (1, P, .97, .82), "card_greeting": (2, S, .95, .55),
                 "card_plastic": (3, S, .94, .48), "card_board": (4, S, .80, .22)},
    "chalk":    {"chalk_stick": (1, P, .98, .90), "chalk_rock": (2, S, .78, .25),
                 "chalk_tailor": (3, X, .35, .04)},
    "cheers":   {"cheers_greeting": (1, P, .95, .88), "cheers_show": (2, X, .50, .08)},
    "coat":     {"coat_garment": (1, P, .99, .94), "coat_fur": (2, S, .90, .40)},
    # Учебниковый пример честной вторичности рядом с `orange`: простуду знают все.
    "cold":     {"cold_temperature": (1, P, .99, .92), "cold_illness": (2, S, .97, .68)},
    "current":  {"current_electric": (1, P, .93, .72), "current_water": (2, S, .90, .48)},
    "dash":     {"dash_run": (1, P, .92, .70), "dash_mark": (2, S, .88, .42),
                 "dash_car": (3, S, .82, .25)},
    "delta":    {"delta_letter": (1, P, .86, .62), "delta_river": (2, S, .84, .45),
                 "delta_airline": (3, X, .60, .10)},
    "diamond":  {"diamond_gem": (1, P, .99, .92), "diamond_shape": (2, S, .96, .62),
                 "diamond_card": (3, S, .92, .40), "diamond_field": (4, X, .55, .08)},
    "duck":     {"duck_bird": (1, P, .99, .95), "duck_meat": (2, S, .88, .35),
                 "duck_toy": (3, S, .82, .25)},
    "elder":    {"elder_person": (1, P, .94, .82), "elder_church": (2, S, .80, .28),
                 "elder_plant": (3, X, .35, .04)},
    "focus":    {"focus_mind": (1, P, .98, .90), "focus_lens": (2, S, .90, .45)},
    "fry":      {"fry_cook": (1, P, .98, .92), "fry_fish": (2, X, .40, .05)},
    "hand":     {"hand_body": (1, P, .99, .96), "hand_give": (2, S, .95, .55),
                 "hand_cards": (3, S, .86, .28), "hand_clock": (4, S, .84, .26),
                 "hand_worker": (5, X, .45, .06)},
    "head":     {"head_body": (1, P, .99, .96), "head_leader": (2, S, .95, .55),
                 "head_brand": (3, X, .32, .03)},
    "iris":     {"iris_flower": (1, P, .88, .62), "iris_eye": (2, S, .88, .48)},
    "letter":   {"letter_alphabet": (1, P, .98, .88), "letter_mail": (2, S, .97, .70)},
    "major":    {"major_study": (1, P, .92, .70), "major_rank": (2, S, .86, .40)},
    "march":    {"march_walk": (1, P, .95, .80), "march_month": (2, S, .96, .62)},
    "minute":   {"minute_time": (1, P, .99, .96), "minute_tiny": (2, S, .78, .18)},
    "moon":     {"moon_space": (1, P, .99, .96)},
    "mouth":    {"mouth_face": (1, P, .99, .96), "mouth_river": (2, S, .82, .22)},
    "oil":      {"oil_cooking": (1, P, .97, .82), "oil_crude": (2, S, .95, .60),
                 "oil_motor": (3, S, .93, .52), "oil_paint": (4, S, .86, .30)},
    "palm":     {"palm_hand": (1, P, .96, .82), "palm_tree": (2, S, .95, .62)},
    "party":    {"party_event": (1, P, .99, .95), "party_group": (2, S, .84, .26)},
    "pipe":     {"pipe_tube": (1, P, .96, .86), "pipe_symbol": (2, X, .40, .05)},
    "pound":    {"pound_weight": (1, P, .96, .82), "pound_money": (2, S, .92, .48),
                 "pound_cake": (3, S, .78, .20)},
    "press":    {"press_push": (1, P, .96, .84), "press_media": (2, S, .93, .52),
                 "press_machine": (3, S, .80, .22)},
    "pyramid":  {"pyramid_monument": (1, P, .98, .90), "pyramid_shape": (2, S, .94, .58)},
    "quarter":  {"quarter_fourth": (1, P, .96, .84), "quarter_coin": (2, S, .95, .62),
                 "quarter_lodging": (3, X, .48, .07)},
    "round":    {"round_shape": (1, P, .98, .90), "round_stage": (2, S, .88, .38),
                 "round_math": (3, S, .86, .32), "round_meat": (4, X, .38, .05)},
    "sail":     {"sail_cloth": (1, P, .96, .84), "sail_voyage": (2, S, .92, .52),
                 "sail_fish": (3, X, .42, .05)},
    "season":   {"season_time": (1, P, .99, .94), "season_flavor": (2, S, .90, .42)},
    "second":   {"second_time": (1, P, .99, .94), "second_order": (2, S, .96, .60)},
    "secretary": {"secretary_office": (1, P, .97, .90), "secretary_minister": (2, S, .82, .26)},
    "shoulder": {"shoulder_body": (1, P, .99, .95), "shoulder_road": (2, S, .80, .22),
                 "shoulder_meat": (3, X, .48, .07)},
    "sound":    {"sound_noise": (1, P, .99, .96), "sound_water": (2, X, .45, .06)},
    "sow":      {"sow_plant": (1, P, .88, .62), "sow_pig": (2, S, .78, .30)},
    "sponge":   {"sponge_cleaning": (1, P, .98, .92), "sponge_animal": (2, S, .86, .32),
                 "sponge_cake": (3, S, .78, .20)},
    "stamp":    {"stamp_postage": (1, P, .98, .90), "stamp_tool": (2, S, .84, .30)},
    "straw":    {"straw_tube": (1, P, .97, .86), "straw_hay": (2, S, .92, .50),
                 "straw_berry": (3, S, .80, .20)},
    "temple":   {"temple_building": (1, P, .96, .86), "temple_head": (2, S, .82, .26)},
    "ticket":   {"ticket_admission": (1, P, .99, .92), "ticket_fine": (2, S, .92, .50),
                 "ticket_order": (3, X, .45, .06)},
    "watch":    {"watch_object": (1, P, .98, .88), "watch_look": (2, S, .97, .68),
                 "watch_warning": (3, S, .78, .18)},
    "yard":     {"yard_ground": (1, P, .97, .88), "yard_measure": (2, S, .90, .42)},
}


# --------------------------------------------------------------------------- 2
# Значений нет вовсе; слово читается по-разному.
NEW_SENSES: dict[str, dict[str, dict]] = {
    "down": {
        "down_direction": spec(1, P, .99, .95, pos="adverb",
                               definition="Towards a lower place or position."),
        "down_feathers": spec(2, S, .88, .35,
                              definition="The soft fine feathers under a bird's outer feathers."),
    },
    "deck": {
        "deck_cards": spec(1, P, .95, .78,
                           definition="A pack of playing cards."),
        "deck_platform": spec(2, S, .94, .58,
                              definition="A flat wooden platform beside a house or on a ship."),
    },
    "column": {
        "column_pillar": spec(1, P, .95, .80,
                              definition="An upright pillar supporting a building."),
        "column_text": spec(2, S, .90, .45,
                            definition="A vertical block of text in a newspaper or table."),
    },
    "hall": {
        "hall_room": spec(1, P, .96, .86,
                          definition="A corridor or a large room for gatherings."),
        "hall_surname": spec(2, S, .84, .20, kind="proper_name", pos="proper_noun",
                             definition="Hall, an English family name.",
                             display="Hall", proper=True),
    },
    "metal": {
        "metal_material": spec(1, P, .99, .94,
                               definition="A hard shiny material such as iron or steel."),
        "metal_music": spec(2, S, .92, .45,
                            definition="Heavy metal, a loud guitar-driven music genre."),
    },
    "meter": {
        "meter_length": spec(1, P, .95, .80,
                             definition="A unit of length equal to about 39 inches."),
        "meter_device": spec(2, S, .90, .45,
                             definition="A device that measures and records a quantity."),
    },
    "panel": {
        "panel_board": spec(1, P, .92, .70,
                            definition="A flat rectangular piece forming part of a surface."),
        "panel_people": spec(2, S, .88, .40,
                             definition="A small group of people chosen to discuss or judge."),
    },
    "flat": {
        "flat_level": spec(1, P, .98, .92, pos="adjective",
                           definition="Having a smooth level surface."),
        "flat_shoe": spec(2, S, .82, .25,
                          definition="A shoe without a heel."),
    },
    "straight": {
        "straight_line": spec(1, P, .98, .92, pos="adjective",
                              definition="Going in one direction without bending."),
        "straight_cards": spec(2, S, .80, .20,
                               definition="A poker hand of five cards in sequence."),
    },
    "title": {
        "title_name": spec(1, P, .97, .88,
                           definition="The name of a book, film or piece of music."),
        "title_legal": spec(2, S, .84, .26,
                            definition="A legal document proving ownership."),
    },
    "judge": {
        "judge_person": spec(1, P, .98, .90,
                             definition="The official who decides cases in a court of law."),
        "judge_decide": spec(2, S, .94, .50, pos="verb",
                             definition="To form an opinion about something."),
    },
    "war": {
        "war_conflict": spec(1, P, .99, .96,
                             definition="Armed conflict between countries or groups."),
        "war_card_game": spec(2, X, .50, .06, kind="title", pos="proper_noun",
                              definition="War, the simple card game of high card wins.",
                              display="War"),
    },
    "tom": {
        "tom_name": spec(1, P, .96, .88, kind="proper_name", pos="proper_noun",
                         definition="Tom, a short form of the name Thomas.",
                         display="Tom", proper=True),
        "tom_cat": spec(2, S, .78, .22,
                        definition="A male cat."),
    },
    "dean": {
        "dean_college": spec(1, P, .90, .70,
                             definition="The head of a college faculty or school."),
        "dean_name": spec(2, S, .86, .30, kind="proper_name", pos="proper_noun",
                          definition="Dean, an English given name and surname.",
                          display="Dean", proper=True),
    },
    "rain": {
        "rain_weather": spec(1, P, .99, .97,
                             definition="Water falling from clouds in drops."),
        "rain_name": spec(2, X, .40, .04, kind="proper_name", pos="proper_noun",
                          definition="Rain, a given name taken from the weather.",
                          display="Rain", proper=True),
    },
    "summer": {
        "summer_season": spec(1, P, .99, .97,
                              definition="The warmest season of the year."),
        "summer_name": spec(2, S, .78, .16, kind="proper_name", pos="proper_noun",
                            definition="Summer, a girl's given name taken from the season.",
                            display="Summer", proper=True),
    },
    "willow": {
        "willow_tree": spec(1, P, .93, .82,
                            definition="A tree with long thin branches that hang down."),
        "willow_name": spec(2, S, .76, .16, kind="proper_name", pos="proper_noun",
                            definition="Willow, a girl's given name taken from the tree.",
                            display="Willow", proper=True),
    },
    "river": {
        "river_water": spec(1, P, .99, .96,
                            definition="A large natural stream of water flowing to the sea."),
        "river_name": spec(2, X, .42, .04, kind="proper_name", pos="proper_noun",
                           definition="River, a given name taken from the waterway.",
                           display="River", proper=True),
    },
    "english": {
        "english_language": spec(1, P, .99, .95, kind="proper_name", pos="proper_noun",
                                 definition="English, the language and the school subject.",
                                 display="English", proper=True),
    },
    "spanish": {
        "spanish_language": spec(1, P, .98, .92, kind="proper_name", pos="proper_noun",
                                 definition="Spanish, the language and the school subject.",
                                 display="Spanish", proper=True),
    },
    "alpha": {
        "alpha_letter": spec(1, P, .88, .70,
                             definition="Alpha, the first letter of the Greek alphabet."),
    },
    "omega": {
        "omega_letter": spec(1, P, .86, .66,
                             definition="Omega, the last letter of the Greek alphabet."),
        "omega_brand": spec(2, X, .38, .04, kind="brand", pos="proper_noun",
                            definition="Omega, the Swiss watch brand.",
                            display="Omega", proper=True),
    },
    "peanut": {
        "peanut_nut": spec(1, P, .99, .94,
                           definition="A small oval nut that grows underground."),
    },
    "glacier": {
        "glacier_ice": spec(1, P, .95, .88,
                            definition="A slow-moving mass of ice on land."),
    },
    "lighthouse": {
        "lighthouse_tower": spec(1, P, .97, .92,
                                 definition="A tower with a light that warns ships."),
    },
    "shell": {
        "shell_covering": spec(1, P, .98, .92,
                               definition="The hard outer covering of an egg, nut or sea animal."),
    },
    "python": {
        "python_snake": spec(1, P, .94, .84,
                             definition="A large snake that kills by constriction."),
    },
    "stars": {
        "stars_sky": spec(1, P, .99, .94,
                          definition="The points of light seen in the night sky."),
    },
    "belt": {
        "belt_band": spec(1, P, .98, .92,
                          definition="A band worn round the waist or driving a machine."),
    },
    "filter": {
        "filter_device": spec(1, P, .95, .86,
                              definition="A device that removes unwanted matter from a flow."),
    },
    "frame": {
        "frame_structure": spec(1, P, .96, .88,
                                definition="A rigid structure that surrounds or supports."),
    },
    "gear": {
        "gear_cog": spec(1, P, .94, .82,
                         definition="A toothed wheel that transmits motion in a machine."),
    },
    "sign": {
        "sign_board": spec(1, P, .97, .90,
                           definition="A board carrying words or a symbol for the public."),
    },
    "table": {
        "table_furniture": spec(1, P, .99, .95,
                                definition="A piece of furniture with a flat top on legs."),
    },
    "child": {
        "child_person": spec(1, P, .99, .96,
                             definition="A young human being."),
    },
    "license": {
        "license_document": spec(1, P, .97, .90,
                                 definition="An official document giving permission."),
    },
}


# Привязка «слово + категория -> значение» для многозначных слов этой партии.
# Однозначным она не нужна: единственное объявленное значение слоя раскладывается
# по всем связям слова само.
ASSIGNMENTS: dict[str, dict[str, str]] = {
    "down": {"animal_coverings": "down_feathers", "directions": "down_direction",
             "opposites": "down_direction", "football_words": "down_direction"},
    "deck": {"card_words": "deck_cards", "magic_words": "deck_cards",
             "parts_of_a_house": "deck_platform", "things_made_of_wood": "deck_platform",
             "skateboarding": "deck_platform", "sailing_words": "deck_platform"},
    "column": {"parts_of_a_house": "column_pillar", "architecture_words": "column_pillar",
               "cave_things": "column_pillar", "printing_and_type": "column_text",
               "writing_words": "column_text", "newspaper_parts": "column_text"},
    "hall": {"castle_things": "hall_room", "rooms_in_public_buildings": "hall_room",
             "common_surnames": "hall_surname"},
    "metal": {"sculpture_materials": "metal_material", "hard_things": "metal_material",
              "everyday_materials": "metal_material", "music_genres": "metal_music"},
    "meter": {"ref_length_units": "meter_length",
              "things_measured_in_inches": "meter_length",
              "measurement_devices": "meter_device", "measuring_tools": "meter_device",
              "parking_words": "meter_device"},
    "panel": {"sewing_patterns": "panel_board", "comic_words": "panel_board",
              "electrical_words": "panel_board", "groups_of_people": "panel_people"},
    "flat": {"shape_adjectives": "flat_level", "music_words": "flat_level",
             "theater_stage_terms": "flat_level",
             "footwear": "flat_shoe", "shoe_styles": "flat_shoe"},
    "straight": {"shape_adjectives": "straight_line", "directions": "straight_line",
                 "card_words": "straight_cards", "poker_hands": "straight_cards"},
    "title": {"reading_words": "title_name", "writing_words": "title_name",
              "initials_and_titles": "title_name", "sports_scoring": "title_name",
              "legal_documents": "title_legal"},
    "judge": {"law_jobs": "judge_person", "courtroom_things": "judge_person",
              "titles_of_address": "judge_person", "sports_officials": "judge_person",
              "thinking_actions": "judge_decide"},
    "war": {"movie_genres": "war_conflict", "card_games": "war_card_game"},
    "tom": {"nicknames": "tom_name", "nicknames_for_names": "tom_name",
            "cartoon_characters": "tom_name",
            "animal_names_male_female": "tom_cat"},
    "dean": {"college_words": "dean_college", "school_jobs": "dean_college",
             "famous_job_titles": "dean_college",
             "short_names": "dean_name", "titles_of_address": "dean_college"},
    "rain": {"weather_actions": "rain_weather", "weather_words": "rain_weather",
             "water_states": "rain_weather", "seasons_spring": "rain_weather",
             "spring_season": "rain_weather", "nature_names": "rain_name"},
    "summer": {"seasons": "summer_season", "nature_names": "summer_name"},
    "willow": {"trees": "willow_tree", "nature_names": "willow_name"},
    "river": {"bodies_of_water": "river_water", "nature_names": "river_name"},
    "omega": {"greek_letters": "omega_letter", "watch_and_luxury": "omega_brand"},
}


# Однозначные слова: разброс по темам есть, второго смысла нет.
MONOSEMOUS: tuple[str, ...] = (
    "actor", "anchor", "boss", "cactus", "canoe", "canyon", "chapel", "cherry",
    "chestnut", "church", "colony", "coop", "cough", "crescent", "crowd", "desk",
    "door", "dry", "eclipse", "flood", "foam", "gladiator", "growl", "hair",
    "hiss", "mountain", "newspaper", "oxygen", "painting", "pentagon",
    "pressure", "quill", "rabbit", "ridge", "rinse", "saddle", "satellite",
    "snack", "stable", "summit", "telescope", "theater", "valley", "volcano",
    "walnut", "whisper", "window",
)


def main() -> None:
    raw = json.loads(SENSE_MAP.read_text(encoding="utf-8"))
    senses = raw.setdefault("senses", {})

    scored = 0
    for word, entries in SCORES.items():
        bucket = senses.setdefault(word, {})
        for key, (rank, access, rec, act) in entries.items():
            bucket[key] = {**bucket.get(key, {}), **spec(rank, access, rec, act)}
            scored += 1
    added = 0
    for word, entries in NEW_SENSES.items():
        bucket = senses.setdefault(word, {})
        for key, entry in entries.items():
            bucket[key] = {**bucket.get(key, {}), **entry}
            added += 1

    assignments = raw.setdefault("assignments", {})
    linked = 0
    for word, by_category in ASSIGNMENTS.items():
        assignments.setdefault(word, {}).update(by_category)
        linked += len(by_category)

    SENSE_MAP.write_text(
        json.dumps(raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    existing = NOT_HOMONYMS.read_text(encoding="utf-8").rstrip("\n").split("\n")
    known = {line.split("#")[0].strip() for line in existing if line.split("#")[0].strip()}
    new = sorted(word for word in MONOSEMOUS if word not in known)
    if new:
        NOT_HOMONYMS.write_text(
            "\n".join([
                *existing,
                "",
                "# Вторая партия: слова из резерва кандидатов первой линейки.",
                *new,
            ]) + "\n",
            encoding="utf-8",
        )

    print(f"оценок доступности проставлено: {scored}")
    print(f"новых значений объявлено: {added} у {len(NEW_SENSES)} слов")
    print(f"привязок добавлено: {linked}")
    print(f"однозначных слов дописано: {len(new)}")


if __name__ == "__main__":
    main()
