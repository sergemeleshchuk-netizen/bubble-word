# Готовность категорий, конфликты и четвёрки

Три слоя, которых в базе не было и которые требовал аудит.

## 1. Готовность категорий

Выводится из пулов командой `derive-readiness`, руками не пишется.

| readiness | что значит | категорий |
|---|---|---|
| `ready` | 4+ слов уровня, пул не перекошен — годится для автогенерации | 816 |
| `constrained` | годится, но пул тонкий, перекошен в hard_only или мало approved | 268 |
| `hard_only` | нормальных слов меньше четырёх: только сложные уровни | 5 |
| `curated_only` | правило парное или субъективное: только ручные четвёрки | 4 |

## 2. Конфликты категорий (516)

Пары, которые нельзя ставить в один уровень: их пулы пересекаются так, что
четвёрка из одной целиком лежит в другой, и у уровня появляется второй
корректный ответ. `derived` — посчитано по пересечению пулов, `manual` — решение
человека из `_category_meta.json`.

| A | B | общих слов | серьёзность | источник |
|---|---|---|---|---|
| JEWELRY STONES (`jewelry_stones`) | GEMSTONES (`gemstones`) | 15 | P0 | derived |
| BIRDS (`birds`) | FLYING ANIMALS (`flying_animals`) | 13 | P0 | derived |
| FABRICS (`fabrics`) | FABRIC TYPES (`fabric_types`) | 13 | P0 | derived |
| FOOTWEAR (`footwear`) | SHOE STYLES (`shoe_styles`) | 13 | P0 | derived |
| SCHOOL SUPPLIES (`school_supplies`) | OFFICE SUPPLIES (`office_supplies`) | 13 | P0 | derived |
| ART CLASS (`art_class_things`) | ART SUPPLIES (`art_supplies`) | 12 | P0 | derived |
| FARM ANIMALS (`farm_animals`) | LIVESTOCK (`livestock`) | 12 | P0 | derived |
| LANGUAGES (`languages`) | NATIONALITIES (`nationalities`) | 12 | P0 | derived |
| PIE INGREDIENTS (`pie_ingredients`) | BAKING INGREDIENTS (`baking_ingredients`) | 12 | P0 | derived |
| SCHOOL PEOPLE (`school_people`) | SCHOOL JOBS (`school_jobs`) | 12 | P0 | derived |
| SEAFOOD (`seafood`) | FISH (`fish_species`) | 12 | P0 | derived |
| ACCESSORIES (`accessories`) | FASHION ACCESSORIES (`fashion_accessories`) | 11 | P0 | derived |
| BREAD TYPES (`bread_types`) | SANDWICH BREADS (`sandwich_breads`) | 11 | P0 | derived |
| BREAD TYPES (`bread_types`) | WORLD BREADS (`world_breads`) | 11 | P0 | derived |
| CLEANING SUPPLIES (`cleaning_supplies`) | CLEANING TOOLS (`cleaning_tools`) | 11 | P0 | derived |
| CLOTHING ITEMS (`clothing_items`) | BUTTONED THINGS (`things_you_button`) | 11 | P0 | derived |
| FISHING TRIP (`fishing_hobby`) | FISHING THINGS (`fishing_things`) | 11 | P0 | derived |
| FRUITS (`fruits`) | FRUIT TREES (`fruit_trees`) | 11 | P0 | derived |
| RIVERS (`rivers`) | WORLD RIVERS (`world_rivers`) | 11 | P0 | derived |
| SPICES AND HERBS (`spices_and_herbs`) | COOKING HERBS (`herbs`) | 11 | P0 | derived |
| VEGETABLES (`vegetables`) | SALAD INGREDIENTS (`salad_ingredients`) | 11 | P0 | derived |
| BATHROOM ITEMS (`bathroom_items`) | HYGIENE THINGS (`hygiene`) | 10 | P0 | derived |
| CALENDAR WORDS (`calendar_words`) | UNITS OF TIME (`time_units`) | 10 | P0 | derived |
| COOKING ACTIONS (`cooking_actions`) | COOKING METHODS (`cooking_methods`) | 10 | P0 | derived |
| FLOWERS (`flowers`) | SUMMER FLOWERS (`garden_flowers_summer`) | 10 | P0 | derived |
| FRUITS (`fruits`) | THINGS WITH SEEDS (`things_with_seeds`) | 10 | P0 | derived |
| MUSICAL INSTRUMENTS (`musical_instruments`) | WIND INSTRUMENTS (`wind_instruments`) | 10 | P0 | derived |
| NUTS AND SEEDS (`nuts_and_seeds`) | SNACK NUTS (`nuts_world`) | 10 | P0 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SEAFOOD (`seafood`) | 10 | P0 | derived |
| TOWN PLACES (`town_places`) | KINDS OF BUILDINGS (`kinds_of_buildings`) | 10 | P0 | derived |
| WEATHER WORDS (`weather_words`) | FORMS OF WATER (`water_states`) | 10 | P0 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SHELLFISH (`shellfish`) | 9 | P0 | derived |
| BERRIES (`berries`) | BERRY VARIETIES (`berry_varieties`) | 9 | P0 | derived |
| CLEANING SUPPLIES (`cleaning_supplies`) | JANITORIAL WORDS (`cleaning_trade`) | 9 | P0 | derived |
| CLOTHING ITEMS (`clothing_items`) | THINGS WITH POCKETS (`things_with_pockets`) | 9 | P0 | derived |
| SKY WORDS (`cloud_and_sky`) | NIGHT SKY (`night_sky_things`) | 9 | P0 | derived |
| CURRENCIES (`currencies`) | MORE CURRENCIES (`world_currencies_more`) | 9 | P0 | derived |
| ELECTRICITY WORDS (`electricity_words`) | POWER WORDS (`power_and_batteries`) | 9 | P0 | derived |
| EUROPEAN CITIES (`european_cities`) | WORLD CITIES (`world_cities`) | 9 | P0 | derived |
| FISH (`fish_species`) | FRESHWATER FISH (`pond_fish`) | 9 | P0 | derived |
| FLOWER PARTS (`flower_parts`) | PLANT PARTS (`plant_parts`) | 9 | P0 | derived |
| HORSE WORDS (`horse_words`) | HORSE RIDING (`equestrian_words`) | 9 | P0 | derived |
| ILLNESSES (`illnesses`) | DISEASES (`diseases`) | 9 | P0 | derived |
| BUGS (`insects`) | PESTS (`pests`) | 9 | P0 | derived |
| MEASURING DEVICES (`measurement_devices`) | MEASURING TOOLS (`measuring_tools`) | 9 | P0 | derived |
| PARTY THINGS (`party_things`) | BIRTHDAY THINGS (`birthday_things`) | 9 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SALAD INGREDIENTS (`salad_ingredients`) | 9 | P0 | derived |
| SEWING SUPPLIES (`sewing_supplies`) | TAILOR SHOP (`tailor_words`) | 9 | P0 | derived |
| TALE CHARACTERS (`storybook_characters`) | MYTHICAL CREATURES (`fantasy_creatures`) | 9 | P0 | derived |
| POINTED THINGS (`things_that_are_sharp`) | SHARP THINGS (`things_that_cut`) | 9 | P0 | derived |
| VEGETABLES (`vegetables`) | SOUP INGREDIENTS (`soup_ingredients`) | 9 | P0 | derived |
| VEHICLES (`vehicles`) | THINGS WITH WHEELS (`things_with_wheels`) | 9 | P0 | derived |
| BODY SOUNDS (`body_sounds`) | VOICE SOUNDS (`voice_sounds`) | 8 | P0 | derived |
| BUILDING MATERIALS (`building_materials`) | HARD THINGS (`hard_things`) | 8 | P0 | derived |
| GARMENT PARTS (`clothing_parts`) | GARMENT DETAILS (`sewing_patterns`) | 8 | P0 | derived |
| CRAFT MATERIALS (`crafting_materials`) | ART SUPPLIES (`art_supplies`) | 8 | P0 | derived |
| CYCLING WORDS (`cycling_words`) | BICYCLE PARTS (`parts_of_a_bike`) | 8 | P0 | derived |
| ELECTRICITY WORDS (`electricity_words`) | ELECTRICAL WORDS (`electrical_words`) | 8 | P0 | derived |
| GRAINS AND BEANS (`grains_and_beans`) | FARM CROPS (`crops`) | 8 | P0 | derived |
| HAIR WORDS (`hair_words`) | HAIRSTYLES (`hairstyles`) | 8 | P0 | derived |
| BUGS (`insects`) | FLYING ANIMALS (`flying_animals`) | 8 | P0 | derived |
| MAGIC SHOW (`magic_words`) | MAGIC PROPS (`magic_tricks`) | 8 | P0 | derived |
| MEATS (`meats`) | CURED MEATS (`cured_meats`) | 8 | P0 | derived |
| NIGHT SKY (`night_sky_things`) | SPACE OBJECTS (`space_objects`) | 8 | P0 | derived |
| HISTORIC TRADES (`old_professions`) | BYGONE JOBS (`historic_jobs`) | 8 | P0 | derived |
| PIE INGREDIENTS (`pie_ingredients`) | PIE TYPES (`pie_types`) | 8 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SANDWICH FILLINGS (`sandwich_fillings`) | 8 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SOUP INGREDIENTS (`soup_ingredients`) | 8 | P0 | derived |
| SALAD INGREDIENTS (`salad_ingredients`) | SOUP INGREDIENTS (`soup_ingredients`) | 8 | P0 | derived |
| SEAFOOD (`seafood`) | SHELLFISH (`shellfish`) | 8 | P0 | derived |
| SOUTHERN CITIES (`southern_cities`) | US CITIES (`us_cities`) | 8 | P0 | derived |
| SPACE OBJECTS (`space_objects`) | SOLAR SYSTEM (`solar_system_words`) | 8 | P0 | derived |
| TALE CHARACTERS (`storybook_characters`) | MAGICAL BEINGS (`magic_creatures`) | 8 | P0 | derived |
| TEXTURES (`textures`) | TOUCH WORDS (`temperature_feel`) | 8 | P0 | derived |
| PAINFUL THINGS (`things_that_hurt`) | INJURIES (`injuries`) | 8 | P0 | derived |
| THINGS WITH SEEDS (`things_with_seeds`) | FRUIT TREES (`fruit_trees`) | 8 | P0 | derived |
| THINGS WITH SEEDS (`things_with_seeds`) | GARDEN PLANTS (`garden_plants`) | 8 | P0 | derived |
| TREES (`trees`) | EVERGREEN TREES (`evergreens`) | 8 | P0 | derived |
| VEHICLES (`vehicles`) | PEOPLE MOVERS (`things_that_carry_people`) | 8 | P0 | derived |
| FORMS OF WATER (`water_states`) | COLD THINGS (`cold_things`) | 8 | P0 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SEASHELLS (`shells`) | 7 | P1 | derived |
| ART CLASS (`art_class_things`) | PAINTING SUPPLIES (`painting_supplies`) | 7 | P1 | derived |
| BIBLE BOOKS (`bible_books`) | BIBLICAL NAMES (`biblical_names`) | 7 | P1 | derived |
| BUILDING ACTIONS (`building_actions`) | HOME REPAIR (`sewing_and_repair`) | 7 | P1 | derived |
| FARM CROPS (`crops`) | GRASSES (`grasses`) | 7 | P1 | derived |
| EXTINCT ANIMALS (`extinct_animals`) | DINOSAURS (`dinosaurs`) | 7 | P0 | derived |
| FARM BUILDINGS (`farm_buildings`) | FARM THINGS (`things_on_a_farm`) | 7 | P1 | derived |
| FARM JOBS (`farm_jobs`) | JOBS WITH ANIMALS (`jobs_with_animals`) | 7 | P1 | derived |
| FLOWERS (`flowers`) | SPRING FLOWERS (`garden_flowers_spring`) | 7 | P1 | derived |
| FRUITS (`fruits`) | BERRIES (`berries`) | 7 | P1 | derived |
| GADGETS (`gadgets`) | THINGS WITH SCREENS (`screens`) | 7 | P1 | derived |
| GARDEN ACTIONS (`garden_actions`) | GARDENING WORDS (`gardening_words`) | 7 | P1 | derived |
| INJURIES (`injuries`) | SPORTS INJURIES (`sports_injuries`) | 7 | P1 | derived |
| JEWELRY STONES (`jewelry_stones`) | PRECIOUS MATERIALS (`precious_materials`) | 7 | P1 | derived |
| MEDICINE CABINET (`medicine_cabinet`) | FIRST AID (`first_aid`) | 7 | P1 | derived |
| METALS (`metals`) | CHEMICAL ELEMENTS (`elements`) | 7 | P1 | derived |
| FUNGI (`mushrooms_and_fungi`) | MUSHROOM TYPES (`mushroom_types`) | 7 | P0 | derived |
| MUSICAL INSTRUMENTS (`musical_instruments`) | STRING INSTRUMENTS (`string_instruments`) | 7 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | CORAL REEF (`coral_reef`) | 7 | P1 | derived |
| PAINTING SUPPLIES (`painting_supplies`) | HOUSE PAINTING (`painting_trade`) | 7 | P1 | derived |
| EXOTIC BIRDS (`parrots_and_exotic_birds`) | TROPICAL BIRDS (`tropical_birds`) | 7 | P1 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | MEATS (`meats`) | 7 | P1 | derived |
| PRECIOUS MATERIALS (`precious_materials`) | GEMSTONES (`gemstones`) | 7 | P1 | derived |
| REPAIR JOBS (`repair_jobs`) | JOBS WITH TOOLS (`jobs_with_tools`) | 7 | P1 | derived |
| ROMAN GODS (`roman_gods`) | PLANETS (`planets`) | 7 | P0 | derived |
| SANDWICH FILLINGS (`sandwich_fillings`) | MEATS (`meats`) | 7 | P1 | derived |
| SCULPTURE MATERIALS (`sculpture_materials`) | BUILDING MATERIALS (`building_materials`) | 7 | P1 | derived |
| SCULPTURE MATERIALS (`sculpture_materials`) | HARD THINGS (`hard_things`) | 7 | P1 | derived |
| SEWING WORDS (`sewing_words`) | SEWING SUPPLIES (`sewing_supplies`) | 7 | P1 | derived |
| SEWING WORDS (`sewing_words`) | TAILOR SHOP (`tailor_words`) | 7 | P1 | derived |
| SHELLFISH (`shellfish`) | SEASHELLS (`shells`) | 7 | P1 | derived |
| SOUPS AND STEWS (`soups`) | WORLD SOUPS (`world_soups`) | 7 | P0 | derived |
| SPEED WORDS (`speed_adjectives`) | FAST WORDS (`word_fast`) | 7 | P1 | derived |
| THINGS WITH BUTTONS (`things_with_buttons`) | GADGETS (`gadgets`) | 7 | P1 | derived |
| VEGETABLES (`vegetables`) | GARDEN PLANTS (`garden_plants`) | 7 | P1 | derived |
| VEGETABLES (`vegetables`) | ROOT VEGETABLES (`root_vegetables`) | 7 | P1 | derived |
| WEATHER ACTIONS (`weather_actions`) | WEATHER WORDS (`weather_words`) | 7 | P1 | derived |
| WILD PLANTS (`wild_plants`) | WEEDS (`weeds`) | 7 | P1 | derived |
| WRITING TOOLS (`writing_tools`) | ART SUPPLIES (`art_supplies`) | 7 | P1 | derived |
| AFRICAN ANIMALS (`african_animals`) | ZOO ANIMALS (`zoo_animals`) | 6 | P1 | derived |
| ANIMAL SOUNDS (`animal_sounds`) | NATURE SOUNDS (`nature_sounds`) | 6 | P1 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SEAFOOD (`seafood`) | 6 | P1 | derived |
| ART TOOLS (`art_tools`) | PAINTING SUPPLIES (`painting_supplies`) | 6 | P1 | derived |
| BAKING INGREDIENTS (`baking_ingredients`) | PANTRY STAPLES (`pantry_staples`) | 6 | P1 | derived |
| BAKING INGREDIENTS (`baking_ingredients`) | POWDERS (`powders`) | 6 | P1 | derived |
| BEDROOM THINGS (`bedroom_things`) | HOME TEXTILES (`fabrics_at_home`) | 6 | P1 | derived |
| CLEANING TOOLS (`cleaning_tools`) | JANITORIAL WORDS (`cleaning_trade`) | 6 | P1 | derived |
| SKY WORDS (`cloud_and_sky`) | SPACE OBJECTS (`space_objects`) | 6 | P1 | derived |
| DENTIST THINGS (`dentist_things`) | DENTAL WORDS (`dental_words`) | 6 | P1 | derived |
| MORE ELEMENTS (`elements_more`) | METALS (`metals`) | 6 | P1 | derived |
| EXTINCT ANIMALS (`extinct_animals`) | PREHISTORIC ANIMALS (`extinct_and_prehistoric`) | 6 | P1 | derived |
| FARM ANIMALS (`farm_animals`) | POULTRY (`farm_bird_words`) | 6 | P1 | derived |
| FRUITS (`fruits`) | ICE CREAM (`ice_cream_flavors`) | 6 | P1 | derived |
| GARDEN HOBBY (`gardening_hobby`) | GARDEN TOOLS (`garden_tools`) | 6 | P1 | derived |
| GARDEN HOBBY (`gardening_hobby`) | GARDENING WORDS (`gardening_words`) | 6 | P1 | derived |
| GRAINS AND BEANS (`grains_and_beans`) | GRASSES (`grasses`) | 6 | P1 | derived |
| HOSPITAL THINGS (`hospital_things`) | MEDICAL TOOLS (`medical_tools`) | 6 | P1 | derived |
| HOT DRINKS (`hot_drinks`) | COFFEE DRINKS (`coffee_drinks`) | 6 | P1 | derived |
| HOT PLACES (`hot_places`) | HOT THINGS (`hot_things`) | 6 | P1 | derived |
| IRRIGATION THINGS (`irrigation`) | WATER FEATURES (`body_of_water_types`) | 6 | P1 | derived |
| ISLANDS (`islands`) | ISLAND NATIONS (`island_nations`) | 6 | P1 | derived |
| LANDFORMS (`landforms`) | MOUNTAIN THINGS (`mountain_things`) | 6 | P1 | derived |
| MOVIE GENRES (`movie_genres`) | BOOK GENRES (`book_genres`) | 6 | P1 | derived |
| MUSICAL INSTRUMENTS (`musical_instruments`) | THINGS WITH STRINGS (`instruments_you_strum`) | 6 | P1 | derived |
| NAME SHORTENINGS (`nicknames_for_names`) | NICKNAMES (`nicknames`) | 6 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | ANIMALS WITH SHELLS (`animals_with_shells`) | 6 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SEA MAMMALS (`sea_mammals`) | 6 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SHELLFISH (`shellfish`) | 6 | P1 | derived |
| HISTORIC TRADES (`old_professions`) | SURNAMES FROM TRADES (`nature_surnames`) | 6 | P1 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | RACING SPORTS (`racing_sports`) | 6 | P1 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | WINTER SPORTS (`winter_sports`) | 6 | P1 | derived |
| WORK ANIMALS (`pack_animals`) | LIVESTOCK (`livestock`) | 6 | P1 | derived |
| KINDS OF PAPER (`paper_types`) | ___ PAPER (`words_before_paper`) | 6 | P1 | derived |
| PIE INGREDIENTS (`pie_ingredients`) | FRUIT TREES (`fruit_trees`) | 6 | P1 | derived |
| POWER WORDS (`power_and_batteries`) | ELECTRICAL WORDS (`electrical_words`) | 6 | P1 | derived |
| READING WORDS (`reading_words`) | WRITING WORDS (`writing_words`) | 6 | P1 | derived |
| REPTILES (`reptiles`) | SNAKES (`snakes`) | 6 | P1 | derived |
| RODENTS (`rodents`) | RODENT SPECIES (`rodent_species`) | 6 | P1 | derived |
| SANDWICH FILLINGS (`sandwich_fillings`) | SALAD INGREDIENTS (`salad_ingredients`) | 6 | P1 | derived |
| SCHOOL ACTIONS (`school_actions`) | LEARNING ACTIONS (`learning_actions`) | 6 | P1 | derived |
| SCHOOL PEOPLE (`school_people`) | HELPING PROFESSIONS (`people_who_help`) | 6 | P1 | derived |
| SCHOOL SUPPLIES (`school_supplies`) | ART SUPPLIES (`art_supplies`) | 6 | P1 | derived |
| HOME REPAIR (`sewing_and_repair`) | FASTENERS (`fasteners`) | 6 | P1 | derived |
| HOME REPAIR (`sewing_and_repair`) | TOOLBOX THINGS (`things_in_a_toolbox`) | 6 | P1 | derived |
| SEWING WORDS (`sewing_words`) | GARMENT DETAILS (`sewing_patterns`) | 6 | P1 | derived |
| SLEEP ACTIONS (`sleeping_actions`) | SLEEP WORDS (`sleep_and_rest`) | 6 | P1 | derived |
| CONTAINERS (`storage_containers`) | TOOL STORAGE (`boxes_and_cases`) | 6 | P1 | derived |
| TOOLBOX THINGS (`things_in_a_toolbox`) | HAND TOOLS (`hand_tools`) | 6 | P1 | derived |
| PAPER THINGS (`things_made_of_paper`) | TRASH ITEMS (`things_you_recycle`) | 6 | P1 | derived |
| PEOPLE MOVERS (`things_that_carry_people`) | WORLD TRANSPORT (`world_transport`) | 6 | P1 | derived |
| MELTING THINGS (`things_that_melt`) | COLD THINGS (`cold_things`) | 6 | P1 | derived |
| BUTTONED THINGS (`things_you_button`) | THINGS WITH POCKETS (`things_with_pockets`) | 6 | P1 | derived |
| TOWN PLACES (`town_places`) | QUIET PLACES (`quiet_places`) | 6 | P1 | derived |
| TREE PARTS (`tree_parts`) | CONIFER WORDS (`pine_and_cones`) | 6 | P1 | derived |
| UNDERGROUND THINGS (`underground_things`) | UNDERGROUND PLACES (`underground_places`) | 6 | P1 | derived |
| US CITIES (`us_cities`) | STATE CAPITALS (`state_capitals`) | 6 | P1 | derived |
| WATER SPORTS (`water_sports`) | OUTDOOR ACTIVITIES (`camping_and_outdoors`) | 6 | P1 | derived |
| WORLD DANCES (`world_dances`) | DANCE STYLES (`dance_styles`) | 6 | P1 | derived |
| LAKES (`world_lakes`) | US WATERS (`great_lakes_and_us_water`) | 6 | P1 | derived |
| AFRICAN ANIMALS (`african_animals`) | GRAZING ANIMALS (`antelope_and_grazers`) | 5 | P1 | derived |
| AMPHIBIANS (`amphibians_and_bugs`) | FROGS AND TOADS (`frogs_and_toads`) | 5 | P1 | derived |
| WORLD WONDERS (`ancient_wonders`) | ANCIENT SITES (`world_heritage`) | 5 | P1 | derived |
| ANIMAL ACTIONS (`animal_actions`) | ANIMAL MOVEMENTS (`animal_verbs`) | 5 | P1 | derived |
| ANIMAL HOMES (`animal_homes`) | PLACES WITH ANIMALS (`places_with_animals`) | 5 | P1 | derived |
| ARCTIC ANIMALS (`arctic_animals`) | SEA MAMMALS (`sea_mammals`) | 5 | P1 | derived |
| ART TOOLS (`art_tools`) | ART CLASS (`art_class_things`) | 5 | P1 | derived |
| ART TOOLS (`art_tools`) | WRITING TOOLS (`writing_tools`) | 5 | P1 | derived |
| ASIAN DISHES (`asian_dishes`) | JAPANESE DISHES (`japanese_dishes`) | 5 | P1 | derived |
| BAKING INGREDIENTS (`baking_ingredients`) | DISSOLVING THINGS (`experiments`) | 5 | P1 | derived |
| BASEBALL EQUIPMENT (`baseball_equipment`) | PROTECTIVE GEAR (`sports_gear_worn`) | 5 | P1 | derived |
| BATHROOM ITEMS (`bathroom_items`) | BARBERSHOP WORDS (`barbershop_words`) | 5 | P1 | derived |
| BEAUTY TOOLS (`beauty_tools`) | BATHROOM ITEMS (`bathroom_items`) | 5 | P1 | derived |
| BIBLICAL NAMES (`biblical_names`) | BIBLE FIGURES (`bible_figures`) | 5 | P1 | derived |
| BIBLICAL NAMES (`biblical_names`) | BOYS NAMES (`boys_names`) | 5 | P1 | derived |
| BIRDS (`birds`) | POULTRY (`farm_bird_words`) | 5 | P1 | derived |
| BODIES OF WATER (`bodies_of_water`) | SHORE FEATURES (`ocean_zones`) | 5 | P1 | derived |
| BODY MOVEMENTS (`body_movements`) | BODY LANGUAGE (`body_language`) | 5 | P1 | derived |
| BOYS NAMES (`boys_names`) | BIBLE FIGURES (`bible_figures`) | 5 | P1 | derived |
| BREAKFAST FOODS (`breakfast_foods`) | BREAD TYPES (`bread_types`) | 5 | P1 | derived |
| BUSINESS WORDS (`business_words`) | ACCOUNTING WORDS (`accounting_words`) | 5 | P1 | derived |

Показано 200 из 516. Полный список — в базе, таблица `category_conflicts`.

Самое крупное пересечение:

- **JEWELRY STONES** и **GEMSTONES**: 15 общих слов
  — amethyst | aquamarine | diamond | emerald | garnet | jade | moonstone | onyx | opal | pearl | peridot | ruby | sapphire | topaz | turquoise

## 3. Парные категории (13 пар)

OPPOSITES — это не пул из 26 слов, а 13 пар. Четвёрка для такой категории
собирается только как две полные пары, иначе четыре случайных слова не образуют
понятного правила.

- OPPOSITES (`opposites`): hot / cold
- OPPOSITES (`opposites`): light / dark
- OPPOSITES (`opposites`): near / far
- OPPOSITES (`opposites`): high / low
- OPPOSITES (`opposites`): full / empty
- OPPOSITES (`opposites`): big / small
- OPPOSITES (`opposites`): up / down
- OPPOSITES (`opposites`): in / out
- OPPOSITES (`opposites`): fast / slow
- OPPOSITES (`opposites`): hard / soft
- OPPOSITES (`opposites`): day / night
- OPPOSITES (`opposites`): open / shut
- OPPOSITES (`opposites`): wet / dry

## 4. Проверенные четвёрки

База хранит пулы, игре нужны решения. Четвёрка попадает сюда, только если
solver подтвердил: этих четырёх слов нет целиком ни в одной другой категории.

| review_state | solver_state | четвёрок |
|---|---|---|
| auto_validated | unique | 3005 |

`auto_validated` значит «solver прошёл, человек не смотрел». Статус
`human_approved` ставится только вручную — это и есть следующий шаг ревью.
Сами четвёрки — в `08_quartets.csv`.
