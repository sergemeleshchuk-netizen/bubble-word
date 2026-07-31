# Готовность категорий, конфликты и четвёрки

Три слоя, которых в базе не было и которые требовал аудит.

## 1. Готовность категорий

Выводится из пулов командой `derive-readiness`, руками не пишется.

| readiness | что значит | категорий |
|---|---|---|
| `constrained` | годится, но пул тонкий, перекошен в hard_only или мало approved | 4364 |
| `ready` | 4+ слов уровня, пул не перекошен — годится для автогенерации | 993 |
| `hard_only` | нормальных слов меньше четырёх: только сложные уровни | 933 |
| `blocked` | четвёрку не собрать даже с hard_only: категория отключена | 125 |
| `curated_only` | правило парное или субъективное: только ручные четвёрки | 4 |

## 2. Конфликты категорий (2076)

Пары, которые нельзя ставить в один уровень: их пулы пересекаются так, что
четвёрка из одной целиком лежит в другой, и у уровня появляется второй
корректный ответ. `derived` — посчитано по пересечению пулов, `manual` — решение
человека из `_category_meta.json`.

| A | B | общих слов | серьёзность | источник |
|---|---|---|---|---|
| DESSERTS (`desserts`) | DESSERT (`dessert`) | 17 | P0 | derived |
| ACCESSORIES (`accessories`) | FASHION ACCESSORIES (`fashion_accessories`) | 16 | P0 | derived |
| JEWELRY STONES (`jewelry_stones`) | GEMSTONES (`gemstones`) | 15 | P0 | derived |
| SCHOOL SUPPLIES (`school_supplies`) | OFFICE SUPPLIES (`office_supplies`) | 15 | P0 | derived |
| ART CLASS (`art_class_things`) | ART SUPPLIES (`art_supplies`) | 14 | P0 | derived |
| FABRICS (`fabrics`) | FABRIC TYPES (`fabric_types`) | 14 | P0 | derived |
| BIRDS (`birds`) | FLYING ANIMALS (`flying_animals`) | 13 | P0 | derived |
| FOOTWEAR (`footwear`) | SHOE STYLES (`shoe_styles`) | 13 | P0 | derived |
| FRUITS (`fruits`) | FRUIT TREES (`fruit_trees`) | 13 | P0 | derived |
| HOBBY ACTIVITIES (`hobby_verbs`) | HOBBIES (`hobbies`) | 13 | P0 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SEA CREATURES (`sea_creatures`) | 13 | P0 | derived |
| BATHROOM ITEMS (`bathroom_items`) | HYGIENE THINGS (`hygiene`) | 12 | P0 | derived |
| BREAKFAST FOODS (`breakfast_foods`) | BREAKFAST (`breakfast`) | 12 | P0 | derived |
| CLOTHING ITEMS (`clothing_items`) | CLOTHING (`clothing`) | 12 | P0 | derived |
| FARM ANIMALS (`farm_animals`) | LIVESTOCK (`livestock`) | 12 | P0 | derived |
| LANGUAGES (`languages`) | NATIONALITIES (`nationalities`) | 12 | P0 | derived |
| PIE INGREDIENTS (`pie_ingredients`) | BAKING INGREDIENTS (`baking_ingredients`) | 12 | P0 | derived |
| SCHOOL PEOPLE (`school_people`) | SCHOOL JOBS (`school_jobs`) | 12 | P0 | derived |
| SEAFOOD (`seafood`) | FISH (`fish_species`) | 12 | P0 | derived |
| VEGETABLES (`vegetables`) | SALAD INGREDIENTS (`salad_ingredients`) | 12 | P0 | derived |
| BREAD TYPES (`bread_types`) | SANDWICH BREADS (`sandwich_breads`) | 11 | P0 | derived |
| BREAD TYPES (`bread_types`) | WORLD BREADS (`world_breads`) | 11 | P0 | derived |
| CHEMISTRY WORDS (`chemistry_words`) | CHEMISTRY (`chemistry`) | 11 | P0 | derived |
| CLEANING SUPPLIES (`cleaning_supplies`) | CLEANING TOOLS (`cleaning_tools`) | 11 | P0 | derived |
| CLOTHING ITEMS (`clothing_items`) | BUTTONED THINGS (`things_you_button`) | 11 | P0 | derived |
| FABRIC TYPES (`fabric_types`) | FABRIC (`fabric`) | 11 | P0 | derived |
| FISHING TRIP (`fishing_hobby`) | FISHING THINGS (`fishing_things`) | 11 | P0 | derived |
| FRUITS (`fruits`) | FRUIT (`fruit`) | 11 | P0 | derived |
| FRUITS (`fruits`) | THINGS WITH SEEDS (`things_with_seeds`) | 11 | P0 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | SPORTS (`sports`) | 11 | P0 | derived |
| RIVERS (`rivers`) | WORLD RIVERS (`world_rivers`) | 11 | P0 | derived |
| SPICES AND HERBS (`spices_and_herbs`) | COOKING HERBS (`herbs`) | 11 | P0 | derived |
| CALENDAR WORDS (`calendar_words`) | UNITS OF TIME (`time_units`) | 10 | P0 | derived |
| COOKING ACTIONS (`cooking_actions`) | COOKING METHODS (`cooking_methods`) | 10 | P0 | derived |
| FABRICS (`fabrics`) | FABRIC (`fabric`) | 10 | P0 | derived |
| FLOWERS (`flowers`) | SUMMER FLOWERS (`garden_flowers_summer`) | 10 | P0 | derived |
| GEMSTONES (`gemstones`) | PRECIOUS STONES (`precious_stones`) | 10 | P0 | derived |
| JEWELRY STONES (`jewelry_stones`) | PRECIOUS STONES (`precious_stones`) | 10 | P0 | derived |
| MUSICAL INSTRUMENTS (`musical_instruments`) | WIND INSTRUMENTS (`wind_instruments`) | 10 | P0 | derived |
| NUTS AND SEEDS (`nuts_and_seeds`) | SNACK NUTS (`nuts_world`) | 10 | P0 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SEAFOOD (`seafood`) | 10 | P0 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | OLYMPIC EVENTS (`olympic_events`) | 10 | P0 | derived |
| TALE CHARACTERS (`storybook_characters`) | MAGICAL BEINGS (`magic_creatures`) | 10 | P0 | derived |
| TOWN PLACES (`town_places`) | KINDS OF BUILDINGS (`kinds_of_buildings`) | 10 | P0 | derived |
| US STATES (`us_states`) | USA (`usa`) | 10 | P0 | derived |
| VEGETABLES (`vegetables`) | SOUP INGREDIENTS (`soup_ingredients`) | 10 | P0 | derived |
| VEHICLES (`vehicles`) | THINGS WITH WHEELS (`things_with_wheels`) | 10 | P0 | derived |
| WEATHER WORDS (`weather_words`) | FORMS OF WATER (`water_states`) | 10 | P0 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SHELLFISH (`shellfish`) | 9 | P0 | derived |
| BAKING (`baking`) | BREAD (`bread`) | 9 | P0 | derived |
| BERRIES (`berries`) | BERRY VARIETIES (`berry_varieties`) | 9 | P0 | derived |
| BREAD TYPES (`bread_types`) | BREAD (`bread`) | 9 | P0 | derived |
| CHEESE TYPES (`cheese_types`) | CHEESE (`cheese`) | 9 | P0 | derived |
| CLEANING SUPPLIES (`cleaning_supplies`) | JANITORIAL WORDS (`cleaning_trade`) | 9 | P0 | derived |
| CLOTHING ITEMS (`clothing_items`) | THINGS WITH POCKETS (`things_with_pockets`) | 9 | P0 | derived |
| SKY WORDS (`cloud_and_sky`) | NIGHT SKY (`night_sky_things`) | 9 | P0 | derived |
| CONSTELLATIONS (`constellations`) | CONSTELLATION (`constellation`) | 9 | P0 | derived |
| CURRENCIES (`currencies`) | MORE CURRENCIES (`world_currencies_more`) | 9 | P0 | derived |
| DOG BREEDS (`dog_breeds`) | DOGS (`dogs`) | 9 | P0 | derived |
| ELECTRICITY WORDS (`electricity_words`) | POWER WORDS (`power_and_batteries`) | 9 | P0 | derived |
| EUROPEAN CITIES (`european_cities`) | WORLD CITIES (`world_cities`) | 9 | P0 | derived |
| FISH (`fish_species`) | FRESHWATER FISH (`pond_fish`) | 9 | P0 | derived |
| FLOWER PARTS (`flower_parts`) | PLANT PARTS (`plant_parts`) | 9 | P0 | derived |
| FLOWERS (`flowers`) | GARDEN FLOWERS (`garden_flowers`) | 9 | P0 | derived |
| FLOWERS (`flowers`) | SPRING FLOWERS (`garden_flowers_spring`) | 9 | P0 | derived |
| HAIR WORDS (`hair_words`) | HAIRSTYLES (`hairstyles`) | 9 | P0 | derived |
| HORSE WORDS (`horse_words`) | HORSE RIDING (`equestrian_words`) | 9 | P0 | derived |
| ILLNESSES (`illnesses`) | DISEASES (`diseases`) | 9 | P0 | derived |
| BUGS (`insects`) | PESTS (`pests`) | 9 | P0 | derived |
| LAB EQUIPMENT (`lab_equipment`) | LABORATORY EQUIPMENT (`laboratory_equipment`) | 9 | P0 | derived |
| MAGIC SHOW (`magic_words`) | MAGIC PROPS (`magic_tricks`) | 9 | P0 | derived |
| MEASURING DEVICES (`measurement_devices`) | MEASURING TOOLS (`measuring_tools`) | 9 | P0 | derived |
| MEATS (`meats`) | MEAT (`meat`) | 9 | P0 | derived |
| MONKEYS AND APES (`monkeys_and_apes`) | PRIMATES (`primates`) | 9 | P0 | derived |
| MUSIC WORDS (`music_words`) | MUSIC (`music`) | 9 | P0 | derived |
| PARTY THINGS (`party_things`) | BIRTHDAY THINGS (`birthday_things`) | 9 | P0 | derived |
| PASTA SHAPES (`pasta_shapes`) | TYPES OF PASTA (`types_of_pasta`) | 9 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SALAD INGREDIENTS (`salad_ingredients`) | 9 | P0 | derived |
| SEWING SUPPLIES (`sewing_supplies`) | TAILOR SHOP (`tailor_words`) | 9 | P0 | derived |
| SOUTHERN CITIES (`southern_cities`) | US CITIES (`us_cities`) | 9 | P0 | derived |
| TALE CHARACTERS (`storybook_characters`) | MYTHICAL CREATURES (`fantasy_creatures`) | 9 | P0 | derived |
| TEXTURES (`textures`) | TOUCH WORDS (`temperature_feel`) | 9 | P0 | derived |
| POINTED THINGS (`things_that_are_sharp`) | SHARP THINGS (`things_that_cut`) | 9 | P0 | derived |
| THINGS WITH SEEDS (`things_with_seeds`) | FRUIT TREES (`fruit_trees`) | 9 | P0 | derived |
| WEATHER WORDS (`weather_words`) | STORM (`storm`) | 9 | P0 | derived |
| ZOO ANIMALS (`zoo_animals`) | ANIMALS (`animals`) | 9 | P0 | derived |
| BODY SOUNDS (`body_sounds`) | VOICE SOUNDS (`voice_sounds`) | 8 | P0 | derived |
| BONES (`bones`) | ANATOMY (`anatomy`) | 8 | P0 | derived |
| BUILDING MATERIALS (`building_materials`) | HARD THINGS (`hard_things`) | 8 | P0 | derived |
| GARMENT PARTS (`clothing_parts`) | GARMENT DETAILS (`sewing_patterns`) | 8 | P0 | derived |
| COMEDY WORDS (`comedy_words`) | COMEDY (`comedy`) | 8 | P0 | derived |
| CRAFT MATERIALS (`crafting_materials`) | ART SUPPLIES (`art_supplies`) | 8 | P0 | derived |
| CYCLING WORDS (`cycling_words`) | BICYCLE PARTS (`parts_of_a_bike`) | 8 | P0 | derived |
| DESERT THINGS (`desert_things`) | DESERT (`desert`) | 8 | P0 | derived |
| DOG BREEDS (`dog_breeds`) | DOG (`dog`) | 8 | P0 | derived |
| ELECTRICITY WORDS (`electricity_words`) | ELECTRICAL WORDS (`electrical_words`) | 8 | P0 | derived |
| EUROPEAN COUNTRIES (`european_countries`) | COUNTRIES IN EUROPE (`countries_in_europe`) | 8 | P0 | derived |
| FACE PARTS (`face_parts`) | FACE (`face`) | 8 | P0 | derived |
| FLOWER PARTS (`flower_parts`) | FLOWER (`flower`) | 8 | P0 | derived |
| FRUITS (`fruits`) | BERRIES (`berries`) | 8 | P0 | derived |
| GEOLOGICAL ERAS (`geological_eras`) | PALEONTOLOGY ERAS (`paleontology_eras`) | 8 | P0 | derived |
| GRAINS AND BEANS (`grains_and_beans`) | FARM CROPS (`crops`) | 8 | P0 | derived |
| BUGS (`insects`) | FLYING ANIMALS (`flying_animals`) | 8 | P0 | derived |
| BUGS (`insects`) | FLYING INSECTS (`flying_insects`) | 8 | P0 | derived |
| ISLANDS (`islands`) | ISLAND NATIONS (`island_nations`) | 8 | P0 | derived |
| KITCHEN TOOLS (`kitchen_tools`) | KITCHEN (`kitchen`) | 8 | P0 | derived |
| KITCHEN TOOLS (`kitchen_tools`) | KITCHEN UTENSILS (`kitchen_utensils`) | 8 | P0 | derived |
| LANDFORMS (`landforms`) | NATURE (`nature`) | 8 | P0 | derived |
| MEATS (`meats`) | CURED MEATS (`cured_meats`) | 8 | P0 | derived |
| MOUNTAIN THINGS (`mountain_things`) | MOUNTAIN (`mountain`) | 8 | P0 | derived |
| MUSHROOM TYPES (`mushroom_types`) | MUSHROOMS (`mushrooms`) | 8 | P0 | derived |
| MYTHICAL MONSTERS (`mythical_monsters`) | MYTHOLOGY (`mythology`) | 8 | P0 | derived |
| PARK WORDS (`national_parks`) | NATIONAL PARKS (`national_parks_us`) | 8 | P0 | derived |
| NIGHT SKY (`night_sky_things`) | SPACE OBJECTS (`space_objects`) | 8 | P0 | derived |
| HISTORIC TRADES (`old_professions`) | BYGONE JOBS (`historic_jobs`) | 8 | P0 | derived |
| EXOTIC BIRDS (`parrots_and_exotic_birds`) | TROPICAL BIRDS (`tropical_birds`) | 8 | P0 | derived |
| PIE INGREDIENTS (`pie_ingredients`) | PIE TYPES (`pie_types`) | 8 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SANDWICH FILLINGS (`sandwich_fillings`) | 8 | P0 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | SOUP INGREDIENTS (`soup_ingredients`) | 8 | P0 | derived |
| SALAD INGREDIENTS (`salad_ingredients`) | SOUP INGREDIENTS (`soup_ingredients`) | 8 | P0 | derived |
| SCHOOL SUBJECTS (`school_subjects`) | LESSONS (`lessons`) | 8 | P0 | derived |
| SEAFOOD (`seafood`) | SEA CREATURES (`sea_creatures`) | 8 | P0 | derived |
| SEAFOOD (`seafood`) | SHELLFISH (`shellfish`) | 8 | P0 | derived |
| SHAPES (`shapes`) | GEOMETRIC SHAPES (`geometric_shapes`) | 8 | P0 | derived |
| SNACK FOODS (`snack_foods`) | SNACKS (`snacks`) | 8 | P0 | derived |
| SPACE OBJECTS (`space_objects`) | SOLAR SYSTEM (`solar_system_words`) | 8 | P0 | derived |
| SPICES AND HERBS (`spices_and_herbs`) | SPICE (`spice`) | 8 | P0 | derived |
| STORMS (`storms`) | STORM (`storm`) | 8 | P0 | derived |
| TEAM SPORTS (`team_sports`) | SPORTS (`sports`) | 8 | P0 | derived |
| TELESCOPE WORDS (`telescope_words`) | TELESCOPE (`telescope`) | 8 | P0 | derived |
| PAINFUL THINGS (`things_that_hurt`) | INJURIES (`injuries`) | 8 | P0 | derived |
| THINGS WITH SEEDS (`things_with_seeds`) | GARDEN PLANTS (`garden_plants`) | 8 | P0 | derived |
| TREES (`trees`) | EVERGREEN TREES (`evergreens`) | 8 | P0 | derived |
| VEGETABLES (`vegetables`) | GARDEN PLANTS (`garden_plants`) | 8 | P0 | derived |
| VEGETABLES (`vegetables`) | ROOT VEGETABLES (`root_vegetables`) | 8 | P0 | derived |
| VEHICLES (`vehicles`) | PEOPLE MOVERS (`things_that_carry_people`) | 8 | P0 | derived |
| FORMS OF WATER (`water_states`) | COLD THINGS (`cold_things`) | 8 | P0 | derived |
| WEATHER WORDS (`weather_words`) | WEATHER PHENOMENA (`weather_phenomena`) | 8 | P0 | derived |
| WORLD BREADS (`world_breads`) | BREAD (`bread`) | 8 | P0 | derived |
| AFRICAN ANIMALS (`african_animals`) | ZOO ANIMALS (`zoo_animals`) | 7 | P1 | derived |
| AFRICAN COUNTRIES (`african_countries`) | COUNTRIES IN AFRICA (`countries_in_africa`) | 7 | P0 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SHELL (`shell`) | 7 | P0 | derived |
| ANIMALS WITH SHELLS (`animals_with_shells`) | SEASHELLS (`shells`) | 7 | P1 | derived |
| ARCHITECTURE WORDS (`architecture_words`) | ARCHITECTURE (`architecture`) | 7 | P1 | derived |
| ART CLASS (`art_class_things`) | PAINTING SUPPLIES (`painting_supplies`) | 7 | P1 | derived |
| FAMOUS AUTHORS (`authors`) | WRITERS (`writers`) | 7 | P0 | derived |
| BABY THINGS (`baby_things`) | BABY (`baby`) | 7 | P1 | derived |
| BAKERY (`bakery`) | BAKING (`baking`) | 7 | P1 | derived |
| BEDROOM THINGS (`bedroom_things`) | BEDROOM (`bedroom`) | 7 | P1 | derived |
| BIBLE BOOKS (`bible_books`) | BIBLICAL NAMES (`biblical_names`) | 7 | P1 | derived |
| BOARD GAMES (`board_games`) | STRATEGY GAMES (`strategy_games`) | 7 | P0 | derived |
| BUILDING ACTIONS (`building_actions`) | HOME REPAIR (`sewing_and_repair`) | 7 | P1 | derived |
| BUILDING MATERIALS (`building_materials`) | CONSTRUCTION MATERIALS (`construction_materials`) | 7 | P0 | derived |
| CHRISTMAS THINGS (`christmas_things`) | CHRISTMAS (`christmas`) | 7 | P1 | derived |
| COLD DRINKS (`cold_drinks`) | BEVERAGES (`beverages`) | 7 | P1 | derived |
| CONDIMENTS (`condiments`) | SAUCES (`sauces`) | 7 | P1 | derived |
| COOKING METHODS (`cooking_methods`) | COOKING TECHNIQUES (`cooking_techniques`) | 7 | P0 | derived |
| FARM CROPS (`crops`) | GRASSES (`grasses`) | 7 | P1 | derived |
| MORE ELEMENTS (`elements_more`) | METALS (`metals`) | 7 | P1 | derived |
| EXTINCT ANIMALS (`extinct_animals`) | DINOSAURS (`dinosaurs`) | 7 | P1 | derived |
| FABRIC (`fabric`) | TEXTILES (`textiles`) | 7 | P1 | derived |
| FABRIC TYPES (`fabric_types`) | TEXTILES (`textiles`) | 7 | P1 | derived |
| FABRICS (`fabrics`) | CLOTHING MATERIALS (`clothing_materials`) | 7 | P0 | derived |
| FABRICS (`fabrics`) | TEXTILES (`textiles`) | 7 | P1 | derived |
| MYTHICAL CREATURES (`fantasy_creatures`) | MAGICAL BEINGS (`magic_creatures`) | 7 | P1 | derived |
| FARM BUILDINGS (`farm_buildings`) | FARM THINGS (`things_on_a_farm`) | 7 | P1 | derived |
| FARM JOBS (`farm_jobs`) | JOBS WITH ANIMALS (`jobs_with_animals`) | 7 | P1 | derived |
| FOOTWEAR (`footwear`) | TYPES OF SHOES (`types_of_shoes`) | 7 | P0 | derived |
| FRUIT TREES (`fruit_trees`) | FRUIT (`fruit`) | 7 | P1 | derived |
| GADGETS (`gadgets`) | THINGS WITH SCREENS (`screens`) | 7 | P1 | derived |
| GARDEN ACTIONS (`garden_actions`) | GARDENING WORDS (`gardening_words`) | 7 | P1 | derived |
| GARDEN HOBBY (`gardening_hobby`) | GARDEN TOOLS (`garden_tools`) | 7 | P1 | derived |
| GRAPE VARIETIES (`grape_varieties`) | WINE (`wine`) | 7 | P0 | derived |
| HATS (`hats`) | HEADWEAR (`headwear`) | 7 | P0 | derived |
| HOT PLACES (`hot_places`) | HOT THINGS (`hot_things`) | 7 | P1 | derived |
| INJURIES (`injuries`) | SPORTS INJURIES (`sports_injuries`) | 7 | P1 | derived |
| JEWELRY STONES (`jewelry_stones`) | PRECIOUS MATERIALS (`precious_materials`) | 7 | P1 | derived |
| KITCHEN APPLIANCES (`kitchen_appliances`) | APPLIANCES (`appliances`) | 7 | P0 | derived |
| LANDFORMS (`landforms`) | BIOMES (`biomes`) | 7 | P1 | derived |
| LANGUAGES (`languages`) | WORLD LANGUAGES (`world_languages`) | 7 | P0 | derived |
| LIBRARY WORDS (`library_words`) | LIBRARY (`library`) | 7 | P1 | derived |
| MEDICINE CABINET (`medicine_cabinet`) | FIRST AID (`first_aid`) | 7 | P1 | derived |
| METALS (`metals`) | CHEMICAL ELEMENTS (`elements`) | 7 | P1 | derived |
| MOVIE GENRES (`movie_genres`) | BOOK GENRES (`book_genres`) | 7 | P1 | derived |
| MOVIE GENRES (`movie_genres`) | FILM GENRES (`film_genres`) | 7 | P0 | derived |
| FUNGI (`mushrooms_and_fungi`) | MUSHROOM TYPES (`mushroom_types`) | 7 | P0 | derived |
| MUSICAL INSTRUMENTS (`musical_instruments`) | STRING INSTRUMENTS (`string_instruments`) | 7 | P1 | derived |
| NATURAL DISASTERS (`natural_disasters`) | DISASTERS (`disasters`) | 7 | P0 | derived |
| OCEAN ANIMALS (`ocean_animals`) | CORAL REEF (`coral_reef`) | 7 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | OCEAN LIFE (`ocean_life`) | 7 | P1 | derived |
| OCEAN ANIMALS (`ocean_animals`) | SEA LIFE (`sea_life`) | 7 | P0 | derived |
| HISTORIC TRADES (`old_professions`) | SURNAMES FROM TRADES (`nature_surnames`) | 7 | P1 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | RACING SPORTS (`racing_sports`) | 7 | P1 | derived |
| OLYMPIC SPORTS (`olympic_sports`) | WINTER SPORTS (`winter_sports`) | 7 | P1 | derived |
| PAINTING SUPPLIES (`painting_supplies`) | HOUSE PAINTING (`painting_trade`) | 7 | P1 | derived |
| PHOTOGRAPHY WORDS (`photography_words`) | PHOTOGRAPHY (`photography`) | 7 | P1 | derived |
| PIZZA TOPPINGS (`pizza_toppings`) | MEATS (`meats`) | 7 | P1 | derived |
| PLANETS (`planets`) | PLANET (`planet`) | 7 | P0 | derived |
| POTTERY WORDS (`pottery_words`) | POTTERY (`pottery`) | 7 | P1 | derived |
| PRECIOUS MATERIALS (`precious_materials`) | GEMSTONES (`gemstones`) | 7 | P1 | derived |

Показано 200 из 2076. Полный список — в базе, таблица `category_conflicts`.

Самое крупное пересечение:

- **DESSERTS** и **DESSERT**: 17 общих слов
  — brownie | cake | candy | cheesecake | cookie | cupcake | donut | fudge | gelato | ice cream | pastry | pie | pudding | sorbet | tart | tiramisu | trifle

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
| auto_validated | unique | 7304 |

`auto_validated` значит «solver прошёл, человек не смотрел». Статус
`human_approved` ставится только вручную — это и есть следующий шаг ревью.
Сами четвёрки — в `08_quartets.csv`.
