#!/usr/bin/env python3
"""Четвёртая партия: всё, что режет ТОЛЬКО слой значений.

Очередь снята запросом: четвёрки, у которых после отбора остались одни
семантические причины отказа. Это ровно тот контент, который вернётся в пул,
как только значения будут разобраны, — 117 четвёрок в 58 категориях,
75 блокирующих слов.

Зачем это нужно отдельной партией. Пул первой линейки после включения слоя
сжался с 1101 четвёрки до 972, и вместе с ним просела мета-механика: 20
связей против 22 у прежней сборки. Мета-пара — совпадение редкое, и она
чувствительна к размеру пула сильнее любой другой метрики.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSE_MAP = ROOT / "data" / "seed" / "_sense_map.json"
NOT_HOMONYMS = ROOT / "data" / "seed" / "_not_homonyms.txt"

AUDIENCE = "general_en_us_adult"
P, S, X = "primary", "common_secondary", "specialist"


def sc(rank, access, rec, act, *, kind="lexical", conf=0.87, definition=None,
       pos=None, display=None, proper=False) -> dict:
    entry = {
        "sense_kind": kind, "dominance_rank": rank, "accessibility_class": access,
        "recognition_score": rec, "activation_score": act,
        "audience_profile": AUDIENCE, "quality_source": "sense_review",
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


# Значения уже разведены — не хватает доступности.
SCORES: dict[str, dict[str, tuple]] = {
    "pen":      {"pen_writing": (1, P, .99, .95), "pen_animal": (2, S, .86, .30)},
    "wave":     {"wave_hand": (1, P, .98, .88), "wave_water": (2, S, .97, .70),
                 "wave_hair": (3, S, .80, .20), "wave_dance": (4, X, .55, .08)},
    "band":     {"band_group": (1, P, .97, .88), "band_ring": (2, S, .90, .40)},
    "arch":     {"arch_structure": (1, P, .95, .84), "arch_foot": (2, S, .82, .28)},
    "mound":    {"mound_dirt": (1, P, .92, .78), "mound_baseball": (2, S, .78, .22)},
    "horn":     {"horn_animal": (1, P, .96, .84), "horn_sound": (2, S, .94, .55)},
    "shuffle":  {"shuffle_cards": (1, P, .95, .78), "shuffle_walk": (2, S, .90, .45),
                 "shuffle_dance": (3, X, .52, .08)},
    "tap":      {"tap_touch": (1, P, .96, .86), "tap_dance": (2, S, .88, .38)},
    "mint":     {"mint_herb": (1, P, .95, .80), "mint_candy": (2, S, .94, .58),
                 "mint_color": (3, S, .80, .20)},
    "mercury":  {"mercury_planet": (1, P, .95, .80), "mercury_metal": (2, S, .90, .45),
                 "mercury_god": (3, S, .78, .18)},
    "lead":     {"lead_front": (1, P, .97, .86), "lead_metal": (2, S, .92, .48),
                 "lead_clue": (3, S, .80, .20)},
    "cream":    {"cream_dairy": (1, P, .99, .93), "cream_ointment": (2, S, .90, .40),
                 "cream_color": (3, S, .84, .26)},
    "phoenix":  {"phoenix_bird": (1, P, .90, .70),
                 "phoenix_city": (2, S, .88, .38)},
    "chili":    {"chili_dish": (1, P, .96, .84), "chili_pepper": (2, S, .94, .55)},
    "park":     {"park_place": (1, P, .99, .94), "park_verb": (2, S, .95, .55)},
    "host":     {"host_person": (1, P, .95, .82), "host_presenter": (2, S, .90, .45)},
    "rose":     {"rose_flower": (1, P, .99, .94), "rose_name": (2, S, .88, .32),
                 "rose_wine": (3, S, .78, .18)},
    "lavender": {"lavender_plant": (1, P, .92, .78), "lavender_color": (2, S, .86, .35)},
    "atlas":    {"atlas_book": (1, P, .92, .80), "atlas_mountains": (2, X, .40, .05)},
    "pop":      {"pop_sound": (1, P, .96, .82), "pop_music": (2, S, .95, .60)},
    "rock":     {"rock_stone": (1, P, .99, .93), "rock_music": (2, S, .97, .66)},
    "tank":     {"tank_container": (1, P, .94, .78), "tank_military": (2, S, .95, .58)},
    "lap":      {"lap_race": (1, P, .90, .70), "lap_water": (2, X, .48, .07)},
    "post":     {"post_mail": (1, P, .94, .76), "post_online": (2, S, .96, .62),
                 "post_pole": (3, S, .84, .26)},
    "station":  {"station_place": (1, P, .98, .90), "station_kitchen": (2, X, .42, .05)},
    "cricket":  {"cricket_insect": (1, P, .94, .78), "cricket_sport": (2, S, .90, .48)},
    "wax":      {"wax_substance": (1, P, .96, .86), "wax_polish": (2, S, .86, .32)},
    "needle":   {"needle_sewing": (1, P, .98, .90), "needle_medical": (2, S, .94, .55),
                 "needle_pine": (3, S, .82, .24)},
    "club":     {"club_stick": (1, P, .92, .72), "club_card": (2, S, .90, .42),
                 "club_sandwich": (3, S, .80, .20)},
}

# Значений нет; слово читается по-разному.
NEW: dict[str, dict[str, dict]] = {
    "oracle": {
        "oracle_seer": sc(1, P, .88, .70,
                          definition="A priest or priestess who foretold the future."),
        "oracle_company": sc(2, X, .55, .08, kind="brand", pos="proper_noun",
                             definition="Oracle, the American software company.",
                             display="Oracle", proper=True),
    },
    "brown": {
        "brown_color": sc(1, P, .99, .96, pos="adjective",
                          definition="The colour of wood or chocolate."),
        "brown_surname": sc(2, S, .86, .20, kind="proper_name", pos="proper_noun",
                            definition="Brown, a common English family name.",
                            display="Brown", proper=True),
    },
    "floss": {
        "floss_dental": sc(1, P, .96, .88,
                           definition="Thin thread used to clean between the teeth."),
        "floss_dance": sc(2, X, .58, .08,
                          definition="The Floss, a dance of swinging the arms past the hips."),
    },
    "cancer": {
        "cancer_disease": sc(1, P, .99, .95,
                             definition="A disease of uncontrolled cell growth."),
        "cancer_sign": sc(2, S, .86, .28, kind="proper_name", pos="proper_noun",
                          definition="Cancer, the crab sign of the zodiac.",
                          display="Cancer", proper=True),
    },
    "frozen": {
        "frozen_state": sc(1, P, .99, .94, pos="adjective",
                           definition="Turned to ice, or kept very cold."),
        "frozen_film": sc(2, S, .90, .35, kind="title", pos="proper_noun",
                          definition="Frozen, the Disney animated film.",
                          display="Frozen", proper=True),
    },
    "vault": {
        "vault_strongroom": sc(1, P, .94, .80,
                               definition="A secure room where valuables are kept."),
        "vault_jump": sc(2, S, .84, .30, pos="verb",
                         definition="To leap over something using the hands or a pole."),
        "vault_ceiling": sc(3, X, .48, .06,
                            definition="An arched ceiling of stone or brick."),
    },
    "swing": {
        "swing_move": sc(1, P, .98, .90, pos="verb",
                         definition="To move back and forth from a fixed point."),
        "swing_music": sc(2, S, .84, .28,
                          definition="Swing, a style of big-band jazz."),
    },
    "robin": {
        "robin_bird": sc(1, P, .96, .88,
                         definition="A small bird with a red breast."),
        "robin_hero": sc(2, S, .88, .30, kind="title", pos="proper_noun",
                         definition="Robin, Batman's sidekick.",
                         display="Robin", proper=True),
    },
    "diesel": {
        "diesel_fuel": sc(1, P, .97, .90,
                          definition="A heavy fuel oil burned in diesel engines."),
        "diesel_inventor": sc(2, X, .40, .04, kind="proper_name", pos="proper_noun",
                              definition="Rudolf Diesel, the German engineer.",
                              display="Diesel", proper=True),
    },
    "aspen": {
        "aspen_tree": sc(1, P, .84, .68,
                         definition="A poplar tree with leaves that tremble in the wind."),
        "aspen_town": sc(2, S, .80, .26, kind="proper_name", pos="proper_noun",
                         definition="Aspen, the Colorado ski resort town.",
                         display="Aspen", proper=True),
    },
    "ranger": {
        "ranger_warden": sc(1, P, .93, .80,
                            definition="An official who looks after a park or forest."),
        "ranger_truck": sc(2, X, .38, .04, kind="brand", pos="proper_noun",
                           definition="Ranger, a Ford pickup truck model.",
                           display="Ranger", proper=True),
    },
    "olympics": {
        "olympics_games": sc(1, P, .99, .95, kind="proper_name", pos="proper_noun",
                             definition="The Olympic Games.",
                             display="Olympics", proper=True),
    },
    "jeep": {
        "jeep_vehicle": sc(1, P, .97, .90, kind="brand", pos="proper_noun",
                           definition="Jeep, the American off-road vehicle brand.",
                           display="Jeep", proper=True),
    },
    "lift": {
        "lift_raise": sc(1, P, .98, .92, pos="verb",
                         definition="To raise something to a higher position."),
    },
    "track": {
        "track_path": sc(1, P, .97, .88,
                         definition="A prepared path or course for running or trains."),
    },
    "field": {
        "field_ground": sc(1, P, .98, .92,
                           definition="An open area of ground, often used for sport or crops."),
    },
    "cape": {
        "cape_cloak": sc(1, P, .94, .84,
                         definition="A sleeveless cloak fastened at the neck."),
    },
    "smoke": {
        "smoke_gas": sc(1, P, .99, .94,
                        definition="The grey cloud given off by something burning."),
    },
    "thread": {
        "thread_string": sc(1, P, .97, .90,
                            definition="A thin strand of cotton used for sewing."),
    },
    "label": {
        "label_tag": sc(1, P, .97, .90,
                        definition="A small piece of paper or fabric giving information."),
    },
    "basket": {
        "basket_container": sc(1, P, .99, .93,
                               definition="A container woven from cane or wire."),
    },
    "coin": {
        "coin_money": sc(1, P, .99, .95,
                         definition="A flat piece of metal used as money."),
    },
    "hat": {
        "hat_headwear": sc(1, P, .99, .96,
                           definition="A covering worn on the head."),
    },
}

# Однозначные слова: разброс есть, второго смысла нет.
MONOSEMOUS: tuple[str, ...] = (
    "brake", "rack", "audience", "elevator", "chick", "lamb", "lodge", "pottery",
    "routine", "gauge", "runway", "buzzer", "vase", "bleach", "gospel", "planner",
    "witness", "textbook", "gravity", "alley", "mule", "troll", "elf", "sponge",
)

ASSIGNMENTS: dict[str, dict[str, str]] = {
    "oracle": {"fortune_telling": "oracle_seer", "ancient_greece_ideas": "oracle_seer",
               "tech_companies": "oracle_company"},
    "brown": {"colors": "brown_color", "rice_types": "brown_color",
              "common_surnames": "brown_surname"},
    "floss": {"dentist_things": "floss_dental", "bathroom_items": "floss_dental",
              "dental_words": "floss_dental", "hygiene": "floss_dental",
              "at_the_dentist": "floss_dental", "dance_moves": "floss_dance"},
    "cancer": {"diseases": "cancer_disease", "zodiac_signs": "cancer_sign"},
    "frozen": {"grocery_aisles": "frozen_state", "famous_movies": "frozen_film"},
    "vault": {"banking_words": "vault_strongroom", "under_lock": "vault_strongroom",
              "gymnastics_events": "vault_jump", "architecture_words": "vault_ceiling"},
    "swing": {"sports_actions": "swing_move", "dance_styles": "swing_music",
              "music_genres": "swing_music", "baby_things": "swing_move"},
    "robin": {"birds": "robin_bird", "flying_animals": "robin_bird",
              "seasons_spring": "robin_bird", "songbirds": "robin_bird",
              "superheroes": "robin_hero"},
    "diesel": {"things_that_burn": "diesel_fuel", "gas_station_things": "diesel_fuel",
               "inventors": "diesel_inventor"},
    "aspen": {"trees": "aspen_tree", "nature_names": "aspen_town",
              "resort_towns": "aspen_town", "place_names_as_names": "aspen_town"},
    "ranger": {"national_parks": "ranger_warden", "emergency_jobs": "ranger_warden",
               "emergency_services": "ranger_warden", "car_models": "ranger_truck"},
    # Значения слова `wave` и подобных уже разведены в базе; здесь только те
    # связи, которые разбор не покрывал.
    "wave": {"body_movements": "wave_hand", "ocean_zones": "wave_water"},
    "pen": {"animal_homes": "pen_animal", "farm_buildings": "pen_animal",
            "things_on_a_farm": "pen_animal"},
    "band": {"groups_of_people": "band_group", "school_subjects": "band_group",
             "gem_cuts": "band_ring", "things_made_of_rubber": "band_ring"},
    "arch": {"shapes": "arch_structure", "architecture_words": "arch_structure",
             "rock_formations": "arch_structure", "shoe_parts": "arch_foot"},
    "mound": {"animal_homes": "mound_dirt", "baseball_words": "mound_baseball"},
    "horn": {"animal_body_parts": "horn_animal", "things_that_are_sharp": "horn_animal",
             "bell_and_alarm": "horn_sound", "car_parts": "horn_sound",
             "loud_things": "horn_sound", "musical_instruments": "horn_sound",
             "fan_things": "horn_sound"},
    "shuffle": {"card_tricks": "shuffle_cards", "card_words": "shuffle_cards",
                "ways_of_moving": "shuffle_walk", "quiet_sounds": "shuffle_walk",
                "dance_moves": "shuffle_dance"},
    "tap": {"hand_actions": "tap_touch", "dance_moves": "tap_dance",
            "dance_styles": "tap_dance"},
    "mint": {"garden_plants": "mint_herb", "herbs": "mint_herb",
             "spices_and_herbs": "mint_herb", "green_things": "mint_herb",
             "teas": "mint_herb", "drink_mixers": "mint_herb",
             "candy": "mint_candy", "candy_shapes": "mint_candy",
             "ice_cream_flavors": "mint_candy",
             "color_words_advanced": "mint_color"},
    "mercury": {"planets": "mercury_planet", "elements": "mercury_metal",
                "metals": "mercury_metal", "roman_gods": "mercury_god"},
    "lead": {"sports_scoring": "lead_front", "elements": "lead_metal",
             "metals": "lead_metal", "detective_words": "lead_clue"},
    "cream": {"dairy_products": "cream_dairy", "dairy_words": "cream_dairy",
              "baking_ingredients": "cream_dairy", "drink_mixers": "cream_dairy",
              "pie_ingredients": "cream_dairy", "soup_ingredients": "cream_dairy",
              "medicine_forms": "cream_ointment", "facial_care": "cream_ointment",
              "color_words_advanced": "cream_color"},
    "phoenix": {"fantasy_creatures": "phoenix_bird",
                "place_names_as_names": "phoenix_city", "state_capitals": "phoenix_city",
                "us_cities": "phoenix_city"},
    "chili": {"soups": "chili_dish", "fast_food_items": "chili_dish",
              "red_things": "chili_pepper"},
    "park": {"city_words": "park_place", "field_trip_places": "park_place",
             "town_places": "park_place", "driving_actions": "park_verb"},
    "host": {"restaurant_words": "host_person", "relationships": "host_person",
             "kitchen_jobs": "host_person", "game_shows": "host_presenter",
             "media_jobs": "host_presenter", "radio_words": "host_presenter",
             "tv_words": "host_presenter"},
    "rose": {"flowers": "rose_flower", "garden_plants": "rose_flower",
             "garden_flowers_summer": "rose_flower", "shrubs": "rose_flower",
             "red_things": "rose_flower", "perfume_words": "rose_flower",
             "flags_and_symbols": "rose_flower",
             "nature_names": "rose_name", "short_names": "rose_name",
             "wines_and_drinks": "rose_wine"},
    "lavender": {"flowers": "lavender_plant", "garden_flowers_summer": "lavender_plant",
                 "garden_plants": "lavender_plant", "herbs": "lavender_plant",
                 "perfume_words": "lavender_plant",
                 "color_words_advanced": "lavender_color"},
    "atlas": {"book_genres": "atlas_book", "library_words": "atlas_book",
              "map_words": "atlas_book", "geography_class": "atlas_book",
              "mountain_ranges": "atlas_mountains"},
    "pop": {"kitchen_sounds": "pop_sound", "onomatopoeia": "pop_sound",
            "music_genres": "pop_music"},
    "rock": {"collecting_hobbies": "rock_stone", "desert_things": "rock_stone",
             "hard_things": "rock_stone", "music_genres": "rock_music"},
    "tank": {"diving_gear": "tank_container", "pet_supplies": "tank_container",
             "things_that_hold_water": "tank_container",
             "military_things": "tank_military"},
    "lap": {"racing_words": "lap_race", "water_sounds": "lap_water"},
    "post": {"social_media_words": "post_online",
             "things_that_stick_out": "post_pole"},
    "station": {"radio_words": "station_place", "space_travel": "station_place",
                "town_places": "station_place", "train_words": "station_place",
                "kitchen_brigade": "station_kitchen"},
    "cricket": {"insects": "cricket_insect", "nocturnal_animals": "cricket_insect",
                "garden_bugs": "cricket_insect",
                "team_sports": "cricket_sport", "world_sports": "cricket_sport"},
    "wax": {"beekeeping": "wax_substance", "sculpture_materials": "wax_substance",
            "sticky_things": "wax_substance", "things_that_burn": "wax_substance",
            "things_that_melt": "wax_substance", "paper_types": "wax_substance",
            "cleaning_supplies": "wax_polish"},
    "needle": {"knitting_words": "needle_sewing", "sewing_supplies": "needle_sewing",
               "sewing_words": "needle_sewing", "tailor_words": "needle_sewing",
               "long_thin_things": "needle_sewing",
               "things_that_are_sharp": "needle_sewing",
               "medical_tools": "needle_medical",
               "pine_and_cones": "needle_pine", "leaf_shapes": "needle_pine",
               "tree_parts": "needle_pine"},
    "club": {"gym_equipment": "club_stick", "weapons_of_the_past": "club_stick",
             "golf_words": "club_stick", "juggling_words": "club_stick",
             "card_words": "club_card", "sandwich_types": "club_sandwich"},
}


def main() -> None:
    raw = json.loads(SENSE_MAP.read_text(encoding="utf-8"))
    senses = raw.setdefault("senses", {})
    assignments = raw.setdefault("assignments", {})

    for word, entries in SCORES.items():
        bucket = senses.setdefault(word, {})
        for key, (rank, access, rec, act) in entries.items():
            bucket[key] = {**bucket.get(key, {}), **sc(rank, access, rec, act)}
    for word, entries in NEW.items():
        bucket = senses.setdefault(word, {})
        for key, entry in entries.items():
            bucket[key] = {**bucket.get(key, {}), **entry}
    for word, by_category in ASSIGNMENTS.items():
        assignments.setdefault(word, {}).update(by_category)

    SENSE_MAP.write_text(
        json.dumps(raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    existing = NOT_HOMONYMS.read_text(encoding="utf-8").rstrip("\n").split("\n")
    known = {line.split("#")[0].strip() for line in existing if line.split("#")[0].strip()}
    new = sorted(word for word in MONOSEMOUS if word not in known)
    if new:
        NOT_HOMONYMS.write_text(
            "\n".join([*existing, "",
                       "# Четвёртая партия: слова, блокировавшие четвёрки, "
                       "которые режет только слой значений.",
                       *new]) + "\n",
            encoding="utf-8",
        )
    print(f"оценок: {sum(len(v) for v in SCORES.values())}, "
          f"новых значений: {sum(len(v) for v in NEW.values())}, "
          f"привязок: {sum(len(v) for v in ASSIGNMENTS.values())}, "
          f"однозначных: {len(new)}")


if __name__ == "__main__":
    main()
