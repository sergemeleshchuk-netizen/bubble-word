#!/usr/bin/env python3
"""Собирает data/categories.jsonl и data/membership_candidates.jsonl из компактного описания.

Источник правды для seed-контента — этот файл: категории с правилами, пулы слов
и отдельный список многозначных слов, у которых значения разведены через sense_key.

Запуск:  python scripts/build_seed.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from word_content.normalization import normalize_word  # noqa: E402

SOURCE = "seed_manual"

# --------------------------------------------------------------------------------------
# Категории.
# t   — theme, rel — relation_type, d — base_difficulty,
# obv — обычная очевидность связи в этой категории,
# ok  — можно ли ставить approved (только для очевидных, вручную выверенных пулов),
# tpl — шаблон объяснения связи ($W — слово с заглавной, $w — как есть).
# --------------------------------------------------------------------------------------
CATEGORIES: list[dict] = [
    # ---------------------------------------------------------------- food
    dict(key="fruits", label="FRUITS", t="food", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Common edible fruits familiar to an average American adult",
         tpl="$W is a common edible fruit",
         words=["apple", "banana", "orange", "grape", "peach", "cherry", "lemon",
                "strawberry", "pear", "watermelon", "pineapple", "plum"]),
    dict(key="vegetables", label="VEGETABLES", t="food", rel="is_a", d=0.12, obv=0.95, ok=True,
         rule="Common edible vegetables sold in an ordinary American grocery store",
         tpl="$W is a common edible vegetable",
         words=["carrot", "potato", "onion", "tomato", "lettuce", "broccoli", "corn",
                "cucumber", "spinach", "celery", "pea", "cabbage"]),
    dict(key="pie_ingredients", label="PIE INGREDIENTS", t="food", rel="used_in", d=0.25, obv=0.80, ok=True,
         rule="Ingredients commonly used in pie fillings or pie preparation",
         tpl="$W is commonly used when making a pie",
         words=["apple", "butter", "sugar", "flour", "cinnamon", "egg", "pumpkin",
                "cherry", "lemon", "pecan", "crust", "salt"]),
    dict(key="breakfast_foods", label="BREAKFAST FOODS", t="food", rel="is_a", d=0.20, obv=0.90, ok=True,
         rule="Foods typically eaten at breakfast in the United States",
         tpl="$W is a typical American breakfast food",
         words=["pancake", "waffle", "bacon", "egg", "cereal", "toast", "oatmeal",
                "bagel", "sausage", "muffin", "omelet", "yogurt"]),
    dict(key="pizza_toppings", label="PIZZA TOPPINGS", t="food", rel="used_in", d=0.20, obv=0.85, ok=True,
         rule="Ingredients commonly put on top of a pizza",
         tpl="$W is a common pizza topping",
         words=["cheese", "pepperoni", "mushroom", "onion", "olive", "sausage",
                "bacon", "pineapple", "spinach", "garlic", "basil", "ham"]),
    dict(key="dairy_products", label="DAIRY PRODUCTS", t="food", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Foods made from milk or sold in the dairy section",
         tpl="$W is a dairy product made from milk",
         words=["milk", "cheese", "butter", "yogurt", "cream", "ice cream",
                "sour cream", "buttermilk", "cream cheese", "whipped cream"]),
    dict(key="baking_ingredients", label="BAKING INGREDIENTS", t="food", rel="used_in", d=0.25, obv=0.85, ok=True,
         rule="Ingredients commonly used to bake cakes, bread or cookies",
         tpl="$W is a standard baking ingredient",
         words=["flour", "sugar", "butter", "egg", "yeast", "vanilla", "salt",
                "milk", "chocolate", "honey", "cocoa", "baking soda"]),
    dict(key="hot_drinks", label="HOT DRINKS", t="food", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Drinks normally served hot",
         tpl="$W is normally served as a hot drink",
         words=["coffee", "tea", "cocoa", "cider", "espresso", "latte",
                "cappuccino", "chai", "hot chocolate", "broth"]),
    dict(key="desserts", label="DESSERTS", t="food", rel="is_a", d=0.15, obv=0.92, ok=True,
         rule="Sweet dishes served at the end of a meal",
         tpl="$W is a sweet dish served as dessert",
         words=["cake", "pie", "cookie", "brownie", "pudding", "ice cream",
                "donut", "cupcake", "cheesecake", "sundae"]),
    dict(key="spices_and_herbs", label="SPICES AND HERBS", t="food", rel="is_a", d=0.30, obv=0.75, ok=True,
         rule="Plant-based seasonings used to flavor food",
         tpl="$W is a seasoning used to flavor food",
         words=["pepper", "cinnamon", "basil", "oregano", "thyme", "ginger",
                "mint", "parsley", "nutmeg", "sage", "rosemary", "paprika"]),
    # ---------------------------------------------------------------- animals
    dict(key="farm_animals", label="FARM ANIMALS", t="animals", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Animals commonly kept on an ordinary farm",
         tpl="$W is an animal commonly kept on a farm",
         words=["cow", "pig", "horse", "sheep", "goat", "chicken", "duck",
                "rooster", "donkey", "turkey"]),
    dict(key="birds", label="BIRDS", t="animals", rel="is_a", d=0.12, obv=0.92, ok=True,
         rule="Bird species an average American can name",
         tpl="$W is a bird",
         words=["robin", "eagle", "owl", "crow", "sparrow", "hawk", "penguin",
                "pigeon", "swan", "goose", "parrot"]),
    dict(key="ocean_animals", label="OCEAN ANIMALS", t="animals", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Animals that live in the ocean",
         tpl="$W lives in the ocean",
         words=["whale", "shark", "dolphin", "octopus", "crab", "jellyfish",
                "seal", "lobster", "starfish", "tuna", "squid"]),
    dict(key="insects", label="INSECTS", t="animals", rel="is_a", d=0.15, obv=0.88, ok=True,
         rule="Insects and other small bugs an average person recognizes",
         tpl="$W is a common insect",
         words=["ant", "bee", "fly", "beetle", "moth", "butterfly", "wasp",
                "cricket", "grasshopper", "ladybug", "mosquito", "dragonfly"]),
    dict(key="pets", label="PETS", t="animals", rel="is_a", d=0.12, obv=0.90, ok=True,
         rule="Animals commonly kept as household pets in the United States",
         tpl="$W is commonly kept as a household pet",
         words=["dog", "cat", "hamster", "goldfish", "rabbit", "gerbil",
                "ferret", "canary", "guinea pig", "parrot"]),
    dict(key="flying_animals", label="FLYING ANIMALS", t="animals", rel="has_property", d=0.20, obv=0.85, ok=True,
         rule="Animals that can fly under their own power",
         tpl="$W can fly under its own power",
         words=["eagle", "owl", "bee", "butterfly", "moth", "sparrow", "hawk",
                "dragonfly", "goose", "hummingbird", "wasp"]),
    dict(key="animal_babies", label="BABY ANIMALS", t="animals", rel="is_a", d=0.25, obv=0.75, ok=True,
         rule="English words for the young of an animal species",
         tpl="$W is the English word for a young animal",
         words=["puppy", "kitten", "calf", "foal", "lamb", "piglet", "chick",
                "cub", "duckling", "fawn", "joey"]),
    dict(key="animal_sounds", label="ANIMAL SOUNDS", t="animals", rel="does_action", d=0.30, obv=0.80, ok=True,
         rule="English words for the sound an animal makes",
         tpl="$W is the English word for a sound an animal makes",
         words=["meow", "moo", "oink", "quack", "roar", "hiss", "chirp",
                "neigh", "howl", "growl", "buzz"]),
    dict(key="nocturnal_animals", label="NOCTURNAL ANIMALS", t="animals", rel="has_property", d=0.35, obv=0.65, ok=False,
         rule="Animals that are active at night and rest during the day",
         tpl="$W is active at night and rests during the day",
         words=["owl", "raccoon", "opossum", "moth", "coyote", "badger",
                "hedgehog", "firefly", "mouse", "skunk"]),
    # ---------------------------------------------------------------- home
    dict(key="kitchen_tools", label="KITCHEN TOOLS", t="home", rel="used_in", d=0.15, obv=0.88, ok=True,
         rule="Handheld tools and utensils used to prepare food in a kitchen",
         tpl="$W is a tool used to prepare food in a kitchen",
         words=["spatula", "whisk", "ladle", "grater", "peeler", "colander",
                "knife", "spoon", "fork", "pan", "pot", "blender"]),
    dict(key="bathroom_items", label="BATHROOM ITEMS", t="home", rel="found_in", d=0.15, obv=0.90, ok=True,
         rule="Objects normally found in a home bathroom",
         tpl="$W is normally found in a bathroom",
         words=["towel", "soap", "shampoo", "toothbrush", "razor", "comb",
                "toothpaste", "sink", "bathtub", "shower", "tissue"]),
    dict(key="furniture", label="FURNITURE", t="home", rel="is_a", d=0.12, obv=0.92, ok=True,
         rule="Movable household furniture",
         tpl="$W is a piece of household furniture",
         words=["chair", "table", "sofa", "bed", "desk", "dresser",
                "bookshelf", "stool", "bench", "cabinet", "nightstand", "couch"]),
    dict(key="cleaning_supplies", label="CLEANING SUPPLIES", t="home", rel="used_in", d=0.20, obv=0.88, ok=True,
         rule="Tools and products used to clean a house",
         tpl="$W is used for cleaning a house",
         words=["broom", "mop", "sponge", "bucket", "vacuum", "detergent",
                "bleach", "duster", "brush", "soap"]),
    dict(key="bedroom_things", label="THINGS IN A BEDROOM", t="home", rel="found_in", d=0.20, obv=0.88, ok=True,
         rule="Objects normally found in a bedroom",
         tpl="$W is normally found in a bedroom",
         words=["bed", "pillow", "blanket", "dresser", "closet", "lamp",
                "nightstand", "sheet", "mattress", "hanger", "alarm clock"]),
    # ---------------------------------------------------------------- nature
    dict(key="trees", label="TREES", t="nature", rel="is_a", d=0.20, obv=0.85, ok=True,
         rule="Kinds of trees an average American can name",
         tpl="$W is a kind of tree",
         words=["oak", "maple", "pine", "birch", "willow", "elm", "cedar",
                "spruce", "redwood", "aspen", "walnut"]),
    dict(key="tree_parts", label="PARTS OF A TREE", t="nature", rel="part_of", d=0.25, obv=0.85, ok=True,
         rule="Physical parts of a living tree",
         tpl="$W is a physical part of a tree",
         words=["root", "trunk", "branch", "leaf", "twig", "sap", "bud",
                "knot", "ring", "seed"]),
    dict(key="flowers", label="FLOWERS", t="nature", rel="is_a", d=0.15, obv=0.88, ok=True,
         rule="Kinds of flowers commonly sold or grown in gardens",
         tpl="$W is a kind of flower",
         words=["rose", "tulip", "daisy", "lily", "sunflower", "orchid",
                "violet", "carnation", "daffodil", "iris", "poppy", "marigold"]),
    dict(key="weather_words", label="WEATHER WORDS", t="nature", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Words describing weather conditions or events in the sky",
         tpl="$W is a word for a weather condition",
         words=["rain", "snow", "wind", "fog", "hail", "thunder", "lightning",
                "storm", "cloud", "sleet", "drizzle", "frost"]),
    dict(key="things_with_seeds", label="THINGS WITH SEEDS", t="nature", rel="has_property", d=0.35, obv=0.70, ok=False,
         rule="Common objects or foods that naturally contain seeds",
         tpl="$W naturally contains seeds",
         words=["watermelon", "sunflower", "pumpkin", "tomato", "grape",
                "pepper", "cucumber", "pear", "pomegranate", "squash"]),
    dict(key="bodies_of_water", label="BODIES OF WATER", t="nature", rel="is_a", d=0.20, obv=0.88, ok=True,
         rule="Natural or man-made bodies of water on the surface of the earth",
         tpl="$W is a body of water",
         words=["lake", "river", "ocean", "pond", "sea", "stream", "bay",
                "creek", "lagoon", "gulf", "canal", "harbor"]),
    dict(key="river_features", label="RIVER FEATURES", t="nature", rel="part_of", d=0.35, obv=0.60, ok=False,
         rule="Parts and features of a river described in everyday English",
         tpl="$W is a feature or part of a river",
         words=["current", "delta", "rapids", "bend", "channel", "source",
                "tributary", "shore", "ford", "basin"]),
    dict(key="gemstones", label="GEMSTONES", t="nature", rel="is_a", d=0.25, obv=0.82, ok=True,
         rule="Precious or semi-precious stones used in jewelry",
         tpl="$W is a stone used in jewelry",
         words=["ruby", "emerald", "sapphire", "opal", "pearl", "amethyst",
                "topaz", "jade", "garnet", "turquoise", "quartz"]),
    # ---------------------------------------------------------------- transport
    dict(key="vehicles", label="VEHICLES", t="transport", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Machines built to carry people or goods from place to place",
         tpl="$W is a vehicle that carries people or goods",
         words=["car", "truck", "bus", "train", "bike", "motorcycle", "van",
                "boat", "plane", "scooter", "tractor", "taxi"]),
    dict(key="things_with_wheels", label="THINGS WITH WHEELS", t="transport", rel="has_property", d=0.25, obv=0.75, ok=False,
         rule="Everyday objects that have wheels as a normal part of their design",
         tpl="$W normally has wheels",
         words=["car", "bike", "bus", "wagon", "cart", "skateboard",
                "stroller", "wheelchair", "suitcase", "tractor", "scooter"]),
    dict(key="car_parts", label="PARTS OF A CAR", t="transport", rel="part_of", d=0.20, obv=0.88, ok=True,
         rule="Physical parts of an ordinary passenger car",
         tpl="$W is a part of an ordinary car",
         words=["engine", "tire", "brake", "hood", "trunk", "bumper",
                "windshield", "wheel", "horn", "seat", "door", "muffler"]),
    dict(key="airport_words", label="AIRPORT WORDS", t="transport", rel="found_in", d=0.25, obv=0.85, ok=True,
         rule="Words for things, places or roles you encounter at an airport",
         tpl="$W is something you encounter at an airport",
         words=["gate", "runway", "terminal", "luggage", "ticket", "passport",
                "pilot", "security", "baggage", "tarmac"]),
    dict(key="construction_equipment", label="CONSTRUCTION EQUIPMENT", t="transport", rel="is_a", d=0.30, obv=0.75, ok=True,
         rule="Large machines used on a building or road construction site",
         tpl="$W is a machine used on a construction site",
         words=["bulldozer", "excavator", "forklift", "backhoe", "dump truck",
                "cement mixer", "jackhammer", "roller", "scaffold", "digger"]),
    # ---------------------------------------------------------------- sports
    dict(key="baseball_equipment", label="BASEBALL EQUIPMENT", t="sports", rel="used_in", d=0.25, obv=0.85, ok=True,
         rule="Physical equipment used to play a game of baseball",
         tpl="$W is equipment used to play baseball",
         words=["glove", "helmet", "base", "mitt", "cleats", "cap", "mask", "plate"]),
    dict(key="baseball_words", label="BASEBALL WORDS", t="sports", rel="found_in", d=0.30, obv=0.75, ok=True,
         rule="Words used to describe plays, places or roles in a baseball game",
         tpl="$W is a word used in a baseball game",
         words=["strike", "inning", "home run", "bunt", "dugout", "umpire",
                "mound", "outfield", "steal", "slider"]),
    dict(key="team_sports", label="TEAM SPORTS", t="sports", rel="is_a", d=0.15, obv=0.92, ok=True,
         rule="Sports played by two opposing teams",
         tpl="$W is played by two opposing teams",
         words=["soccer", "baseball", "basketball", "hockey", "football",
                "volleyball", "rugby", "cricket", "lacrosse", "handball"]),
    dict(key="olympic_sports", label="OLYMPIC SPORTS", t="sports", rel="is_a", d=0.25, obv=0.80, ok=True,
         rule="Sports contested at the modern Olympic Games",
         tpl="$W is contested at the Olympic Games",
         words=["swimming", "gymnastics", "fencing", "archery", "judo",
                "rowing", "boxing", "skiing", "diving", "wrestling", "curling"]),
    dict(key="gym_equipment", label="GYM EQUIPMENT", t="sports", rel="used_in", d=0.25, obv=0.80, ok=True,
         rule="Equipment used for exercise in a fitness gym",
         tpl="$W is equipment used for exercise in a gym",
         words=["treadmill", "dumbbell", "barbell", "mat", "rope", "kettlebell",
                "elliptical", "weights", "jump rope", "punching bag"]),
    # ---------------------------------------------------------------- jobs
    dict(key="medical_jobs", label="MEDICAL JOBS", t="jobs", rel="is_a", d=0.20, obv=0.88, ok=True,
         rule="Jobs held by people who treat patients or work in healthcare",
         tpl="$W is a job in healthcare",
         words=["doctor", "nurse", "surgeon", "dentist", "pharmacist",
                "paramedic", "midwife", "therapist", "vet", "radiologist"]),
    dict(key="kitchen_jobs", label="KITCHEN JOBS", t="jobs", rel="is_a", d=0.30, obv=0.80, ok=True,
         rule="Jobs held by people who work in a restaurant kitchen or food service",
         tpl="$W is a job in a restaurant kitchen or food service",
         words=["chef", "cook", "baker", "butcher", "dishwasher", "waiter",
                "host", "barista", "sous chef", "line cook"]),
    dict(key="school_jobs", label="SCHOOL JOBS", t="jobs", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Jobs held by adults who work at a school",
         tpl="$W is a job held by an adult working at a school",
         words=["teacher", "principal", "janitor", "coach", "librarian",
                "counselor", "tutor", "bus driver", "secretary", "aide"]),
    # ---------------------------------------------------------------- body
    dict(key="body_parts", label="BODY PARTS", t="body", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="External parts of the human body",
         tpl="$W is an external part of the human body",
         words=["arm", "leg", "hand", "foot", "head", "knee", "elbow",
                "shoulder", "neck", "back", "chest", "ankle"]),
    dict(key="face_parts", label="PARTS OF THE FACE", t="body", rel="part_of", d=0.12, obv=0.92, ok=True,
         rule="Parts of the human face",
         tpl="$W is a part of the human face",
         words=["eye", "nose", "mouth", "ear", "cheek", "chin", "lip",
                "forehead", "eyebrow", "eyelash", "jaw"]),
    dict(key="internal_organs", label="INTERNAL ORGANS", t="body", rel="part_of", d=0.25, obv=0.85, ok=True,
         rule="Organs inside the human body",
         tpl="$W is an organ inside the human body",
         words=["lung", "liver", "kidney", "stomach", "brain", "spleen",
                "pancreas", "intestine", "bladder", "gallbladder"]),
    dict(key="hand_parts", label="PARTS OF THE HAND", t="body", rel="part_of", d=0.30, obv=0.80, ok=True,
         rule="Parts of the human hand",
         tpl="$W is a part of the human hand",
         words=["thumb", "finger", "knuckle", "nail", "wrist", "pinky",
                "cuticle", "index finger", "ring finger", "fingertip"]),
    # ---------------------------------------------------------------- clothing
    dict(key="clothing_items", label="CLOTHING ITEMS", t="clothing", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Garments worn on the body",
         tpl="$W is a garment worn on the body",
         words=["shirt", "pants", "dress", "skirt", "jacket", "coat",
                "sweater", "hat", "sock", "scarf", "glove", "tie"]),
    dict(key="footwear", label="FOOTWEAR", t="clothing", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Things worn on the feet",
         tpl="$W is worn on the feet",
         words=["boot", "sneaker", "sandal", "slipper", "heel", "loafer",
                "flip-flop", "cleat", "moccasin", "clog"]),
    dict(key="winter_clothing", label="WINTER CLOTHING", t="clothing", rel="used_in", d=0.20, obv=0.85, ok=True,
         rule="Clothing worn specifically to stay warm in cold weather",
         tpl="$W is worn to stay warm in cold weather",
         words=["coat", "scarf", "mitten", "boot", "sweater", "glove",
                "parka", "earmuffs", "thermals", "beanie"]),
    dict(key="jewelry", label="JEWELRY", t="clothing", rel="is_a", d=0.20, obv=0.88, ok=True,
         rule="Decorative items worn on the body as jewelry",
         tpl="$W is a piece of jewelry worn on the body",
         words=["necklace", "bracelet", "earring", "brooch", "pendant",
                "chain", "anklet", "locket", "watch", "cufflink"]),
    # ---------------------------------------------------------------- tools
    dict(key="hand_tools", label="HAND TOOLS", t="tools", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Tools held in the hand and used for building or repair work",
         tpl="$W is a hand tool used for building or repair",
         words=["hammer", "screwdriver", "wrench", "pliers", "saw", "drill",
                "chisel", "level", "tape measure", "clamp", "file", "mallet"]),
    dict(key="garden_tools", label="GARDEN TOOLS", t="tools", rel="used_in", d=0.25, obv=0.85, ok=True,
         rule="Tools used for gardening and yard work",
         tpl="$W is a tool used for gardening",
         words=["rake", "shovel", "hoe", "trowel", "pruner", "wheelbarrow",
                "hose", "watering can", "shears", "sprinkler"]),
    dict(key="office_supplies", label="OFFICE SUPPLIES", t="tools", rel="found_in", d=0.15, obv=0.88, ok=True,
         rule="Small items kept in an office desk and used for paperwork",
         tpl="$W is an office supply used for paperwork",
         words=["stapler", "pen", "pencil", "folder", "clip", "tape",
                "eraser", "highlighter", "envelope", "notepad", "scissors"]),
    dict(key="sewing_supplies", label="SEWING SUPPLIES", t="tools", rel="used_in", d=0.30, obv=0.80, ok=True,
         rule="Items used for sewing and mending clothes",
         tpl="$W is used for sewing or mending clothes",
         words=["needle", "thread", "thimble", "pin", "button", "zipper",
                "patch", "yarn", "bobbin", "hem"]),
    # ---------------------------------------------------------------- geography
    dict(key="us_states", label="US STATES", t="geography", rel="is_a", d=0.20, obv=0.90, ok=True,
         rule="States of the United States of America",
         tpl="$W is a state of the United States", proper=True,
         words=["Texas", "Florida", "Alaska", "Ohio", "Maine", "Nevada",
                "Kansas", "Oregon", "Utah", "Virginia", "Montana"]),
    dict(key="world_capitals", label="WORLD CAPITALS", t="geography", rel="is_a", d=0.30, obv=0.80, ok=True,
         rule="Capital cities of countries around the world",
         tpl="$W is the capital city of a country", proper=True,
         words=["Paris", "London", "Tokyo", "Rome", "Madrid", "Berlin",
                "Ottawa", "Cairo", "Moscow", "Lima", "Oslo", "Athens"]),
    dict(key="european_countries", label="EUROPEAN COUNTRIES", t="geography", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Countries located in Europe",
         tpl="$W is a country in Europe", proper=True,
         words=["France", "Spain", "Italy", "Germany", "Poland", "Greece",
                "Portugal", "Sweden", "Norway", "Ireland", "Austria", "Hungary"]),
    dict(key="landforms", label="LANDFORMS", t="geography", rel="is_a", d=0.30, obv=0.80, ok=True,
         rule="Natural features of the land surface",
         tpl="$W is a natural feature of the land surface",
         words=["mountain", "valley", "canyon", "plateau", "hill", "cliff",
                "dune", "plain", "cave", "island", "peninsula", "glacier"]),
    dict(key="town_places", label="PLACES IN A TOWN", t="geography", rel="found_in", d=0.15, obv=0.90, ok=True,
         rule="Public buildings and places found in an ordinary American town",
         tpl="$W is a public place found in an ordinary town",
         words=["school", "library", "hospital", "park", "museum", "station",
                "market", "church", "temple", "post office", "courthouse"]),
    # ---------------------------------------------------------------- science
    dict(key="space_objects", label="SPACE OBJECTS", t="science", rel="is_a", d=0.20, obv=0.88, ok=True,
         rule="Objects found in outer space",
         tpl="$W is an object found in outer space",
         words=["planet", "comet", "asteroid", "galaxy", "meteor", "sun",
                "nebula", "satellite", "black hole", "constellation"]),
    dict(key="metals", label="METALS", t="science", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Metals and metal alloys used in everyday objects",
         tpl="$W is a metal used in everyday objects",
         words=["iron", "gold", "silver", "copper", "aluminum", "steel",
                "tin", "lead", "nickel", "zinc", "brass", "bronze"]),
    dict(key="lab_equipment", label="LAB EQUIPMENT", t="science", rel="found_in", d=0.35, obv=0.70, ok=True,
         rule="Equipment found in a school science laboratory",
         tpl="$W is equipment found in a science lab",
         words=["beaker", "microscope", "test tube", "flask", "pipette",
                "burner", "goggles", "tongs", "funnel", "dropper"]),
    dict(key="shapes", label="SHAPES", t="science", rel="is_a", d=0.15, obv=0.92, ok=True,
         rule="Geometric shapes taught in school",
         tpl="$W is a geometric shape",
         words=["circle", "square", "triangle", "rectangle", "oval", "cube",
                "cone", "sphere", "pyramid", "hexagon", "octagon"]),
    # ---------------------------------------------------------------- language
    dict(key="words_before_sauce", label="WORDS BEFORE SAUCE", t="language", rel="phrase_before", d=0.45, obv=0.65, ok=False,
         rule="Words that form a familiar English expression when placed before the word sauce",
         tpl="$w forms the familiar expression \"$w sauce\"",
         words=["barbecue", "soy", "hot", "tomato", "cranberry", "tartar",
                "cheese", "white", "chili", "steak"]),
    dict(key="words_before_ball", label="WORDS BEFORE BALL", t="language", rel="phrase_before", d=0.40, obv=0.65, ok=False,
         rule="Words that form a familiar English compound when placed before the word ball",
         tpl="$w forms the familiar compound \"${w}ball\"",
         words=["base", "foot", "basket", "snow", "eye", "meat", "odd",
                "soft", "volley", "fire"]),
    dict(key="words_after_fire", label="WORDS AFTER FIRE", t="language", rel="phrase_after", d=0.45, obv=0.60, ok=False,
         rule="Words that form a familiar English compound when placed after the word fire",
         tpl="$w forms the familiar compound \"fire $w\"",
         words=["place", "fly", "works", "wood", "arm", "truck", "alarm",
                "drill", "escape", "cracker"]),
    dict(key="words_before_box", label="WORDS BEFORE BOX", t="language", rel="phrase_before", d=0.40, obv=0.65, ok=False,
         rule="Words that form a familiar English compound when placed before the word box",
         tpl="$w forms the familiar compound \"$w box\"",
         words=["mail", "sand", "tool", "ice", "lunch", "jack", "match",
                "shoe", "chatter", "boom"]),
    dict(key="words_before_light", label="WORDS BEFORE LIGHT", t="language", rel="phrase_before", d=0.40, obv=0.65, ok=False,
         rule="Words that form a familiar English compound when placed before the word light",
         tpl="$w forms the familiar compound \"${w}light\"",
         words=["day", "moon", "star", "flash", "high", "night", "sun",
                "spot", "head", "candle"]),
    dict(key="writing_words", label="WRITING WORDS", t="language", rel="found_in", d=0.30, obv=0.80, ok=True,
         rule="Words for the parts and marks of written text",
         tpl="$W is a part or mark of written text",
         words=["letter", "period", "comma", "sentence", "paragraph", "page",
                "word", "margin", "font", "heading"]),
    # ---------------------------------------------------------------- entertainment
    dict(key="musical_instruments", label="MUSICAL INSTRUMENTS", t="entertainment", rel="is_a", d=0.15, obv=0.92, ok=True,
         rule="Instruments played to produce music",
         tpl="$W is a musical instrument",
         words=["piano", "guitar", "drum", "violin", "flute", "trumpet",
                "cello", "harp", "banjo", "clarinet", "saxophone", "tuba"]),
    dict(key="music_words", label="MUSIC WORDS", t="entertainment", rel="found_in", d=0.30, obv=0.75, ok=True,
         rule="Words used to describe how a piece of music is written or performed",
         tpl="$W is a word used to describe written or performed music",
         words=["note", "chord", "scale", "tempo", "rhythm", "beat",
                "melody", "harmony", "verse", "chorus"]),
    dict(key="board_games", label="BOARD GAMES", t="entertainment", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Games played on a board with pieces or cards on a table",
         tpl="$W is a board game played on a table",
         words=["chess", "checkers", "monopoly", "scrabble", "clue", "risk",
                "backgammon", "battleship", "jenga", "dominoes"]),
    dict(key="card_words", label="PLAYING CARD WORDS", t="entertainment", rel="found_in", d=0.30, obv=0.80, ok=True,
         rule="Words for the cards, suits and parts of a standard deck of playing cards",
         tpl="$W is a word for something in a standard deck of playing cards",
         words=["ace", "king", "queen", "jack", "joker", "deck", "suit", "trump"]),
    dict(key="movie_genres", label="MOVIE GENRES", t="entertainment", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Categories used to classify films",
         tpl="$W is a genre used to classify films",
         words=["comedy", "horror", "drama", "western", "thriller", "romance",
                "musical", "documentary", "fantasy", "action"]),
    dict(key="circus_words", label="CIRCUS WORDS", t="entertainment", rel="found_in", d=0.30, obv=0.80, ok=True,
         rule="People, animals and objects you see at a traditional circus",
         tpl="$W is something you see at a traditional circus",
         words=["clown", "tent", "trapeze", "juggler", "acrobat", "ringmaster",
                "elephant", "unicycle", "tightrope", "stilts"]),
    # ---------------------------------------------------------------- actions
    dict(key="cooking_actions", label="COOKING ACTIONS", t="actions", rel="does_action", d=0.25, obv=0.85, ok=True,
         rule="Verbs describing something a cook does to food",
         tpl="To $w is something a cook does to food",
         words=["bake", "boil", "fry", "grill", "chop", "stir", "roast",
                "simmer", "peel", "slice", "knead", "whisk"]),
    dict(key="ways_of_moving", label="WAYS OF MOVING", t="actions", rel="does_action", d=0.25, obv=0.85, ok=True,
         rule="Verbs describing a way a person moves their body from place to place",
         tpl="To $w is a way a person moves from place to place",
         words=["walk", "run", "jump", "crawl", "skip", "swim", "climb",
                "slide", "march", "hop", "sprint", "stroll"]),
    # ---------------------------------------------------------------- properties
    dict(key="round_things", label="ROUND THINGS", t="properties", rel="has_property", d=0.30, obv=0.70, ok=False,
         rule="Everyday objects whose normal shape is round or circular",
         tpl="$W is normally round in shape",
         words=["ball", "coin", "plate", "wheel", "pizza", "button",
                "clock", "donut", "tire", "marble"]),
    dict(key="red_things", label="RED THINGS", t="properties", rel="has_property", d=0.30, obv=0.70, ok=False,
         rule="Everyday things that are typically red in color",
         tpl="$W is typically red in color",
         words=["blood", "brick", "cherry", "ruby", "stop sign", "lobster",
                "strawberry", "cardinal", "fire truck", "tomato"]),
    dict(key="sticky_things", label="STICKY THINGS", t="properties", rel="has_property", d=0.35, obv=0.70, ok=False,
         rule="Substances that stick to whatever they touch",
         tpl="$W sticks to whatever it touches",
         words=["honey", "glue", "tape", "syrup", "gum", "tar", "jam",
                "sap", "caramel", "molasses"]),
    dict(key="cold_things", label="COLD THINGS", t="properties", rel="has_property", d=0.30, obv=0.75, ok=False,
         rule="Things that are cold by their physical nature",
         tpl="$W is cold by its physical nature",
         words=["ice", "snow", "freezer", "popsicle", "iceberg", "frost",
                "sleet", "glacier", "refrigerator", "icicle"]),
    dict(key="colors", label="COLORS", t="properties", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Basic color names used in everyday English",
         tpl="$W is a basic color name",
         words=["red", "blue", "green", "yellow", "purple", "pink",
                "brown", "black", "white", "gray", "teal"]),
    # ---------------------------------------------------------------- business
    dict(key="tech_companies", label="TECH COMPANIES", t="business", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Well-known technology companies or consumer technology brands",
         tpl="$W is a well-known technology company", proper=True,
         words=["Google", "Microsoft", "Amazon", "Intel", "Oracle", "Netflix",
                "Adobe", "Dell", "Nvidia", "IBM", "Samsung"]),
    dict(key="money_words", label="MONEY WORDS", t="business", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Everyday English words for money, payments and personal finance",
         tpl="$W is an everyday word for money or payment",
         words=["cash", "coin", "bill", "check", "credit", "debit", "loan",
                "salary", "budget", "change", "wallet", "interest"]),
    # ---------------------------------------------------------------- time
    dict(key="months", label="MONTHS", t="time", rel="is_a", d=0.10, obv=0.95, ok=True,
         rule="Months of the Gregorian calendar year",
         tpl="$W is a month of the calendar year", proper=True,
         words=["January", "February", "March", "April", "June", "July",
                "August", "September", "October", "November", "December"]),
    dict(key="calendar_words", label="CALENDAR WORDS", t="time", rel="is_a", d=0.25, obv=0.85, ok=True,
         rule="Everyday English words for dates and periods of time on a calendar",
         tpl="$W is an everyday word for a date or period of time",
         words=["month", "year", "week", "day", "weekend", "season",
                "decade", "century", "holiday", "leap year"]),
    dict(key="holidays", label="HOLIDAYS", t="time", rel="is_a", d=0.20, obv=0.88, ok=True,
         rule="Holidays widely celebrated in the United States",
         tpl="$W is a holiday widely celebrated in the United States", proper=True,
         words=["Christmas", "Halloween", "Thanksgiving", "Easter", "Hanukkah",
                "Passover", "Independence Day", "New Year", "Labor Day",
                "Valentine's Day"]),
    # ---------------------------------------------------------------- education
    dict(key="school_supplies", label="SCHOOL SUPPLIES", t="education", rel="used_in", d=0.15, obv=0.90, ok=True,
         rule="Items a student brings to school in a backpack",
         tpl="$W is an item a student brings to school",
         words=["backpack", "notebook", "pencil", "eraser", "ruler", "crayon",
                "glue", "folder", "marker", "calculator", "binder"]),
    dict(key="school_subjects", label="SCHOOL SUBJECTS", t="education", rel="is_a", d=0.15, obv=0.90, ok=True,
         rule="Subjects taught in an American school",
         tpl="$W is a subject taught in school",
         words=["math", "history", "science", "art", "music", "geography",
                "biology", "chemistry", "English", "gym", "algebra", "physics"]),
]

# --------------------------------------------------------------------------------------
# Многозначные слова: значения разведены через sense_key.
# Каждая запись: (word, category_key, relation, reason, fit, obv, status, sense_key,
#                 sense_definition, part_of_speech, is_proper_noun)
# --------------------------------------------------------------------------------------
A_FRUIT = ("apple_fruit", "The round edible fruit of an apple tree", "noun", False)
BANK_FIN = ("bank_finance", "A business that keeps and lends money", "noun", False)
BANK_RIVER = ("bank_river", "The sloping land along the side of a river", "noun", False)
BAT_ANIMAL = ("bat_animal", "A small flying mammal active at night", "noun", False)
BAT_SPORT = ("bat_equipment", "A wooden or metal club used to hit a baseball", "noun", False)
DATE_FRUIT = ("date_fruit", "The sweet brown fruit of a date palm", "noun", False)
DATE_DAY = ("date_calendar", "A particular day of the month or year", "noun", False)
ORANGE_FRUIT = ("orange_fruit", "A round citrus fruit with an orange peel", "noun", False)
ORANGE_COLOR = ("orange_color", "The color between red and yellow", "noun", False)
SPRING_SEASON = ("spring_season", "The season between winter and summer", "noun", False)
SPRING_WATER = ("spring_water", "A place where water flows naturally out of the ground", "noun", False)
SPRING_JUMP = ("spring_jump", "To jump suddenly upward or forward", "verb", False)
PITCH_BALL = ("pitch_throw", "A throw of the ball by the pitcher in baseball", "noun", False)
PITCH_MUSIC = ("pitch_music", "How high or low a musical sound is", "noun", False)
PITCH_TAR = ("pitch_tar", "A thick sticky black substance made from tar", "noun", False)
BARK_SOUND = ("bark_sound", "The short loud sound a dog makes", "noun", False)
BARK_TREE = ("bark_tree", "The tough outer covering of a tree trunk", "noun", False)
CRANE_BIRD = ("crane_bird", "A tall long-legged wading bird", "noun", False)
CRANE_MACHINE = ("crane_machine", "A tall machine that lifts heavy loads on a building site", "noun", False)
CAPITAL_MONEY = ("capital_money", "Money invested in a business", "noun", False)
CAPITAL_LETTER = ("capital_letter", "An upper-case letter of the alphabet", "noun", False)
DIAMOND_GEM = ("diamond_gem", "A clear precious stone used in jewelry", "noun", False)
DIAMOND_SHAPE = ("diamond_shape", "A four-sided shape standing on one of its corners", "noun", False)
DIAMOND_CARD = ("diamond_card", "One of the four suits in a deck of playing cards", "noun", False)
DIAMOND_FIELD = ("diamond_field", "The infield of a baseball field", "noun", False)
HEART_ORGAN = ("heart_organ", "The organ that pumps blood through the body", "noun", False)
HEART_CARD = ("heart_card", "One of the four suits in a deck of playing cards", "noun", False)
SPADE_TOOL = ("spade_tool", "A digging tool with a flat blade", "noun", False)
SPADE_CARD = ("spade_card", "One of the four suits in a deck of playing cards", "noun", False)
CLUB_CARD = ("club_card", "One of the four suits in a deck of playing cards", "noun", False)
CLUB_STICK = ("club_stick", "A heavy stick used as a weapon or for hitting a ball", "noun", False)
KEY_LOCK = ("key_lock", "A small metal object that opens a lock", "noun", False)
KEY_MUSIC = ("key_music", "The set of notes a piece of music is based on", "noun", False)
SCALE_MUSIC = ("scale_music", "A series of musical notes in rising or falling order", "noun", False)
SCALE_WEIGH = ("scale_weigh", "A device used to weigh things", "noun", False)
SCALE_FISH = ("scale_fish", "One of the small hard plates covering a fish", "noun", False)
MOUTH_FACE = ("mouth_face", "The opening in the face used for eating and speaking", "noun", False)
MOUTH_RIVER = ("mouth_river", "The place where a river flows into the sea", "noun", False)
PALM_HAND = ("palm_hand", "The inner surface of the hand", "noun", False)
PALM_TREE = ("palm_tree", "A tall tropical tree with large leaves at the top", "noun", False)
PLATE_DISH = ("plate_dish", "A flat round dish food is served on", "noun", False)
PLATE_BASE = ("plate_base", "The flat marker a baseball batter stands beside", "noun", False)
TEMPLE_HEAD = ("temple_head", "The flat area on each side of the forehead", "noun", False)
TEMPLE_BUILDING = ("temple_building", "A building used for religious worship", "noun", False)
STAR_SPACE = ("star_space", "A burning ball of gas seen as a point of light in the night sky", "noun", False)
STAR_SHAPE = ("star_shape", "A shape with five or more points around a center", "noun", False)
MOON_SPACE = ("moon_space", "The natural satellite that orbits the earth", "noun", False)
RING_JEWEL = ("ring_jewelry", "A band worn on a finger", "noun", False)
RING_TREE = ("ring_tree", "One of the circles in a tree trunk that mark a year of growth", "noun", False)
APPLE_COMPANY = ("apple_company", "The American technology company Apple Inc.", "proper_noun", True)

AMBIGUOUS: list[tuple] = [
    # apple
    ("apple", "fruits", "is_a", "An apple is a common edible fruit", 1.0, 1.0, "approved", A_FRUIT),
    ("apple", "pie_ingredients", "used_in", "Apples are the classic pie filling", 0.99, 0.95, "approved", A_FRUIT),
    ("apple", "things_with_seeds", "has_property", "An apple has a core full of seeds", 0.99, 0.85, "approved", A_FRUIT),
    ("apple", "red_things", "has_property", "Apples are typically red", 0.9, 0.8, "candidate", A_FRUIT),
    ("apple", "round_things", "has_property", "An apple is round in shape", 0.92, 0.75, "candidate", A_FRUIT),
    ("apple", "words_before_sauce", "phrase_before", "Apple forms the familiar expression apple sauce", 0.98, 0.9, "approved", A_FRUIT),
    ("Apple", "tech_companies", "is_a", "Apple is a well-known technology company", 1.0, 0.99, "approved", APPLE_COMPANY),
    # bank
    ("bank", "town_places", "found_in", "A bank is a public place found in almost every town", 0.97, 0.9, "approved", BANK_FIN),
    ("bank", "money_words", "is_a", "A bank is where people keep and borrow money", 0.9, 0.85, "candidate", BANK_FIN),
    ("bank", "river_features", "part_of", "The bank is the sloping land along the side of a river", 0.99, 0.7, "approved", BANK_RIVER),
    # bat
    ("bat", "flying_animals", "has_property", "A bat is the only mammal that truly flies", 1.0, 0.9, "approved", BAT_ANIMAL),
    ("bat", "nocturnal_animals", "has_property", "Bats hunt at night and sleep during the day", 0.98, 0.85, "candidate", BAT_ANIMAL),
    ("bat", "baseball_equipment", "used_in", "A bat is the club a batter uses to hit the ball", 1.0, 0.95, "approved", BAT_SPORT),
    # date
    ("date", "fruits", "is_a", "A date is the sweet fruit of the date palm", 0.95, 0.6, "candidate", DATE_FRUIT),
    ("date", "calendar_words", "is_a", "A date is a particular day on the calendar", 0.99, 0.9, "approved", DATE_DAY),
    # orange
    ("orange", "fruits", "is_a", "An orange is a common citrus fruit", 1.0, 1.0, "approved", ORANGE_FRUIT),
    ("orange", "colors", "is_a", "Orange is a basic color name", 1.0, 1.0, "approved", ORANGE_COLOR),
    ("orange", "things_with_seeds", "has_property", "Oranges contain seeds inside the segments", 0.9, 0.7, "candidate", ORANGE_FRUIT),
    ("orange", "round_things", "has_property", "An orange is round in shape", 0.95, 0.8, "candidate", ORANGE_FRUIT),
    # spring
    ("spring", "calendar_words", "is_a", "Spring is the season between winter and summer", 0.95, 0.85, "approved", SPRING_SEASON),
    ("spring", "bodies_of_water", "is_a", "A spring is water flowing naturally out of the ground", 0.85, 0.55, "candidate", SPRING_WATER),
    ("spring", "ways_of_moving", "does_action", "To spring is to jump suddenly upward", 0.9, 0.5, "candidate", SPRING_JUMP),
    # pitch
    ("pitch", "baseball_words", "found_in", "A pitch is the throw a pitcher makes to the batter", 0.99, 0.9, "approved", PITCH_BALL),
    ("pitch", "music_words", "found_in", "Pitch is how high or low a musical note sounds", 0.99, 0.8, "approved", PITCH_MUSIC),
    ("pitch", "sticky_things", "has_property", "Pitch is the thick sticky tar used to seal boats", 0.9, 0.3, "candidate", PITCH_TAR),
    # bark
    ("bark", "animal_sounds", "does_action", "Bark is the sound a dog makes", 1.0, 0.95, "approved", BARK_SOUND),
    ("bark", "tree_parts", "part_of", "Bark is the outer covering of a tree trunk", 1.0, 0.9, "approved", BARK_TREE),
    # crane
    ("crane", "birds", "is_a", "A crane is a tall long-legged wading bird", 0.98, 0.75, "approved", CRANE_BIRD),
    ("crane", "construction_equipment", "is_a", "A crane lifts heavy loads on a building site", 1.0, 0.9, "approved", CRANE_MACHINE),
    # capital
    ("capital", "money_words", "is_a", "Capital is the money invested in a business", 0.9, 0.55, "candidate", CAPITAL_MONEY),
    ("capital", "writing_words", "found_in", "A capital is an upper-case letter", 0.95, 0.75, "candidate", CAPITAL_LETTER),
    # diamond
    ("diamond", "gemstones", "is_a", "A diamond is the classic precious stone in jewelry", 1.0, 0.95, "approved", DIAMOND_GEM),
    ("diamond", "shapes", "is_a", "A diamond is a four-sided shape standing on a corner", 0.9, 0.8, "candidate", DIAMOND_SHAPE),
    ("diamond", "card_words", "found_in", "Diamonds are one of the four suits in a deck of cards", 0.99, 0.9, "approved", DIAMOND_CARD),
    ("diamond", "baseball_words", "found_in", "The diamond is the infield of a baseball field", 0.95, 0.7, "candidate", DIAMOND_FIELD),
    # heart
    ("heart", "internal_organs", "part_of", "The heart is the organ that pumps blood", 1.0, 0.98, "approved", HEART_ORGAN),
    ("heart", "card_words", "found_in", "Hearts are one of the four suits in a deck of cards", 0.99, 0.9, "approved", HEART_CARD),
    # spade
    ("spade", "garden_tools", "used_in", "A spade is a digging tool with a flat blade", 0.98, 0.85, "approved", SPADE_TOOL),
    ("spade", "card_words", "found_in", "Spades are one of the four suits in a deck of cards", 0.99, 0.9, "approved", SPADE_CARD),
    # club
    ("club", "card_words", "found_in", "Clubs are one of the four suits in a deck of cards", 0.99, 0.9, "approved", CLUB_CARD),
    ("club", "gym_equipment", "used_in", "An Indian club is a weighted stick swung for exercise", 0.7, 0.25, "candidate", CLUB_STICK),
    # key
    ("key", "music_words", "found_in", "The key is the set of notes a piece of music is based on", 0.95, 0.7, "approved", KEY_MUSIC),
    ("key", "bedroom_things", "found_in", "House keys are usually left on the nightstand", 0.6, 0.3, "candidate", KEY_LOCK),
    # scale
    ("scale", "music_words", "found_in", "A scale is a series of notes in rising order", 0.98, 0.8, "approved", SCALE_MUSIC),
    ("scale", "lab_equipment", "found_in", "A scale is used in the lab to weigh samples", 0.95, 0.75, "approved", SCALE_WEIGH),
    # mouth
    ("mouth", "face_parts", "part_of", "The mouth is part of the face", 1.0, 0.98, "approved", MOUTH_FACE),
    ("mouth", "river_features", "part_of", "The mouth of a river is where it meets the sea", 0.99, 0.6, "approved", MOUTH_RIVER),
    # palm
    ("palm", "hand_parts", "part_of", "The palm is the inner surface of the hand", 1.0, 0.95, "approved", PALM_HAND),
    ("palm", "trees", "is_a", "A palm is a tall tropical tree", 0.98, 0.85, "approved", PALM_TREE),
    # plate
    ("plate", "kitchen_tools", "used_in", "A plate is the flat dish food is served on", 0.9, 0.9, "approved", PLATE_DISH),
    ("plate", "round_things", "has_property", "A plate is round in shape", 0.95, 0.85, "candidate", PLATE_DISH),
    ("plate", "baseball_equipment", "used_in", "Home plate marks where the batter stands", 0.95, 0.75, "approved", PLATE_BASE),
    # temple
    ("temple", "face_parts", "part_of", "The temple is the flat area beside the forehead", 0.98, 0.7, "approved", TEMPLE_HEAD),
    ("temple", "town_places", "found_in", "A temple is a building used for religious worship", 0.95, 0.85, "approved", TEMPLE_BUILDING),
    # star
    ("star", "space_objects", "is_a", "A star is a burning ball of gas in the night sky", 1.0, 0.98, "approved", STAR_SPACE),
    ("star", "shapes", "is_a", "A star is a pointed shape drawn around a center", 0.95, 0.9, "approved", STAR_SHAPE),
    ("star", "words_before_light", "phrase_before", "Star forms the familiar compound starlight", 0.95, 0.7, "candidate", STAR_SHAPE),
    # moon
    ("moon", "space_objects", "is_a", "The moon is the natural satellite of the earth", 1.0, 0.98, "approved", MOON_SPACE),
    ("moon", "round_things", "has_property", "The full moon looks like a round disc", 0.9, 0.75, "candidate", MOON_SPACE),
    ("moon", "words_before_light", "phrase_before", "Moon forms the familiar compound moonlight", 0.98, 0.85, "candidate", MOON_SPACE),
    # ring
    ("ring", "jewelry", "is_a", "A ring is a band worn on a finger", 1.0, 0.98, "approved", RING_JEWEL),
    ("ring", "tree_parts", "part_of", "Tree rings mark each year of growth in a trunk", 0.95, 0.6, "candidate", RING_TREE),
]


def capitalize(word: str) -> str:
    return word[0].upper() + word[1:] if word else word


def render(template: str, word: str) -> str:
    return template.replace("$W", capitalize(word)).replace("${w}", word).replace("$w", word)


def build_categories() -> list[dict]:
    return [
        {
            "category_key": spec["key"],
            "label": spec["label"],
            "rule": spec["rule"],
            "relation_type": spec["rel"],
            "theme": spec["t"],
            "base_difficulty": spec["d"],
        }
        for spec in CATEGORIES
    ]


def build_memberships() -> list[dict]:
    records: list[dict] = []
    explicit_pairs = {(normalize_word(row[0]), row[1]) for row in AMBIGUOUS}

    for word, category_key, relation, reason, fit, obv, status, sense in AMBIGUOUS:
        sense_key, definition, pos, proper = sense
        records.append(
            {
                "word": word,
                "language": "en",
                "part_of_speech": pos,
                "is_proper_noun": proper,
                "sense_key": sense_key,
                "sense_definition": definition,
                "category_key": category_key,
                "relation_type": relation,
                "reason": reason,
                "fit_score": fit,
                "obviousness_score": obv,
                "source": SOURCE,
                "review_status": status,
            }
        )

    for spec in CATEGORIES:
        for word in spec["words"]:
            if (normalize_word(word), spec["key"]) in explicit_pairs:
                continue  # у многозначного слова эта связь описана вручную со значением
            record = {
                "word": word,
                "language": "en",
                "part_of_speech": "proper_noun" if spec.get("proper") else "noun",
                "is_proper_noun": bool(spec.get("proper")),
                "category_key": spec["key"],
                "relation_type": spec["rel"],
                "reason": render(spec["tpl"], word),
                "fit_score": 0.97,
                "obviousness_score": spec["obv"],
                "source": SOURCE,
                # approved только для очевидных вручную выверенных пулов
                "review_status": "approved" if spec["ok"] else "candidate",
            }
            records.append(record)
    return records


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    categories = build_categories()
    memberships = build_memberships()

    keys = {c["category_key"] for c in categories}
    assert len(keys) == len(categories), "дубликаты category_key"
    bad = [m for m in memberships if m["category_key"] not in keys]
    assert not bad, f"связи с несуществующей категорией: {bad[:3]}"

    identity = {
        (normalize_word(m["word"]), m["category_key"], m.get("sense_key") or "")
        for m in memberships
    }
    assert len(identity) == len(memberships), "дубликаты связей в seed"

    write_jsonl(ROOT / "data" / "categories.jsonl", categories)
    write_jsonl(ROOT / "data" / "membership_candidates.jsonl", memberships)

    themes = {c["theme"] for c in categories}
    words = {normalize_word(m["word"]) for m in memberships}
    multi: dict[str, set[str]] = {}
    for m in memberships:
        multi.setdefault(normalize_word(m["word"]), set()).add(m["category_key"])
    multi_words = sum(1 for v in multi.values() if len(v) > 1)

    print(f"категорий: {len(categories)} в {len(themes)} темах")
    print(f"связей:    {len(memberships)}")
    print(f"слов:      {len(words)} (в двух и более категориях: {multi_words})")
    print(f"approved:  {sum(1 for m in memberships if m['review_status'] == 'approved')}")


if __name__ == "__main__":
    main()
