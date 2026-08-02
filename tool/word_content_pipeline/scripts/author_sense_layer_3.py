#!/usr/bin/env python3
"""Третья партия: глагольные значения для категорий-действий.

Проверка приёмки `check_action_relation_pos` поймала пять связей, где категория
описывает действие (`does_action`), а разбор второй партии указал на предметное
значение: `iron -> LAUNDRY CARE` получил утюг вместо «гладить», `spring -> WAYS
OF MOVING` — пружину вместо «прыгнуть».

Ошибка ровно того сорта, ради которого весь слой и делался, только с другой
стороны: значение выбрано верное для слова и неверное для правила. Проверка
существовала до этой работы и сработала как задумано.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSE_MAP = ROOT / "data" / "seed" / "_sense_map.json"

AUDIENCE = "general_en_us_adult"


def verb(definition, rank, access, rec, act, conf=0.86) -> dict:
    return {
        "definition": definition,
        "part_of_speech": "verb",
        "sense_kind": "lexical",
        "dominance_rank": rank,
        "accessibility_class": access,
        "recognition_score": rec,
        "activation_score": act,
        "audience_profile": AUDIENCE,
        "quality_source": "sense_review",
        "quality_confidence": conf,
    }


def noun(definition, rank, access, rec, act, conf=0.86) -> dict:
    entry = verb(definition, rank, access, rec, act, conf)
    entry["part_of_speech"] = "noun"
    return entry


SENSES: dict[str, dict[str, dict]] = {
    "button": {
        "button_fasten": verb("To fasten a garment with buttons.", 4, "common_secondary",
                              0.92, 0.40),
    },
    "iron": {
        "iron_press": verb("To press clothes flat with a heated iron.", 4,
                           "common_secondary", 0.95, 0.48),
    },
    "monitor": {
        "monitor_watch": verb("To keep watch over something and check it regularly.", 4,
                              "common_secondary", 0.93, 0.45),
    },
    "spring": {
        "spring_jump": verb("To jump up suddenly.", 4, "common_secondary", 0.90, 0.35),
    },
    "drill": {
        # У слова три предметных значения и ни одного глагольного для «повторять
        # упражнение» — поэтому оно заводится здесь, а не переиспользуется.
        "drill_tool": noun("A power tool that bores holes.", 1, "primary", 0.98, 0.92),
        "drill_bore": verb("To bore a hole with a drill.", 2, "common_secondary",
                           0.95, 0.55),
        "drill_practice": noun("A repeated exercise done to learn something.", 3,
                               "common_secondary", 0.88, 0.35),
        "drill_rehearse": verb("To practise something by repeating it.", 4,
                               "common_secondary", 0.84, 0.28),
    },
}

ASSIGNMENTS: dict[str, dict[str, str]] = {
    "button": {"joining_actions": "button_fasten"},
    "iron": {"laundry_care": "iron_press"},
    "monitor": {"first_aid_actions": "monitor_watch"},
    "spring": {"ways_of_moving": "spring_jump"},
    "drill": {"learning_actions": "drill_rehearse", "building_actions": "drill_bore",
              "hand_tools": "drill_tool", "power_tools": "drill_tool",
              "things_in_a_toolbox": "drill_tool", "workshop_things": "drill_tool"},
}


def main() -> None:
    raw = json.loads(SENSE_MAP.read_text(encoding="utf-8"))
    senses = raw.setdefault("senses", {})
    assignments = raw.setdefault("assignments", {})
    for word, entries in SENSES.items():
        bucket = senses.setdefault(word, {})
        for key, entry in entries.items():
            bucket[key] = {**bucket.get(key, {}), **entry}
    for word, by_category in ASSIGNMENTS.items():
        assignments.setdefault(word, {}).update(by_category)
    SENSE_MAP.write_text(
        json.dumps(raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"значений: {sum(len(v) for v in SENSES.values())}, "
          f"привязок: {sum(len(v) for v in ASSIGNMENTS.values())}")


if __name__ == "__main__":
    main()
