# Проверка схемы прогона

Прогон: `run-001-meta-hubs`

- строк на входе: 265
- категорий принято: **27**
- связей принято: **230**
- из них мета-связей: **149**
- отклонено: **0**
- циклов в мета-графе прогона: 0

## Слой ручных исправлений

`raw.jsonl` не редактируется. Правки описаны в `human_fixes.json`:

- categories_dropped_by_human: 2
- categories_renamed_by_human: 1
- memberships_dropped_by_human: 6
- memberships_retargeted_by_human: 17

## Мета-связи, которые появятся в базе

| Ребёнок (категория) | Идёт словом в | Слово |
|---|---|---|
| `eyewear` | `accessories` | eyewear |
| `hats` | `accessories` | hats |
| `jewelry` | `accessories` | jewelry |
| `aircraft` | `airport_words` | aircraft |
| `airlines` | `airport_words` | airlines |
| `currencies` | `airport_words` | currencies |
| `languages` | `airport_words` | languages |
| `crustaceans` | `aquarium_tank` | crustaceans |
| `fish_species` | `aquarium_tank` | fish |
| `shellfish` | `aquarium_tank` | shellfish |
| `turtles_and_tortoises` | `aquarium_tank` | turtles |
| `colors` | `art_class_things` | colors |
| `crafts` | `art_class_things` | crafts |
| `patterns` | `art_class_things` | patterns |
| `shapes` | `art_class_things` | shapes |
| `eyewear` | `beach_day` | eyewear |
| `seabirds` | `beach_day` | seabirds |
| `shellfish` | `beach_day` | shellfish |
| `swimwear` | `beach_day` | swimwear |
| `owls` | `bird_watching` | owls |
| `seabirds` | `bird_watching` | seabirds |
| `songbirds` | `bird_watching` | songbirds |
| `waterfowl` | `bird_watching` | waterfowl |
| `farm_bird_words` | `birds` | poultry |
| `owls` | `birds` | owls |
| `seabirds` | `birds` | seabirds |
| `songbirds` | `birds` | songbirds |
| `waterfowl` | `birds` | waterfowl |
| `fingers_and_toes` | `bones` | digits |
| `constellations` | `bright_stars` | constellations |
| `teas` | `cocktails` | teas |
| `sauces` | `condiments` | sauces |
| `hats` | `costume_party` | hats |
| `makeup` | `costume_party` | makeup |
| `superheroes` | `costume_party` | superheroes |
| `work_uniforms` | `costume_party` | uniforms |
| `crimes` | `courtroom` | crimes |
| `punishments` | `courtroom` | penalties |
| `rights_and_freedoms` | `courtroom` | rights |
| `titles_of_address` | `courtroom` | titles |
| `cocktails` | `dinner_party` | cocktails |
| `desserts` | `dinner_party` | desserts |
| `dishes_and_glassware` | `dinner_party` | dishes |
| `sauces` | `dinner_party` | sauces |
| `silverware` | `dinner_party` | silverware |
| `desserts` | `dishes_and_glassware` | desserts |
| `salads` | `dishes_and_glassware` | salads |
| `bones` | `emergency_room` | bones |
| `illnesses` | `emergency_room` | illnesses |
| `injuries` | `emergency_room` | injuries |
| `symptoms` | `emergency_room` | symptoms |
| `farm_bird_words` | `farm_morning` | poultry |
| `livestock` | `farm_morning` | livestock |
| `pests` | `farm_morning` | pests |
| `weeds` | `farm_morning` | weeds |
| `wildflowers` | `flowers` | wildflowers |
| `berries` | `fruits` | berries |
| `flowers` | `garden_center` | flowers |
| `houseplants` | `garden_center` | houseplants |
| `trees` | `garden_center` | trees |
| `weeds` | `garden_center` | weeds |
| `islands` | `geography_class` | islands |
| `rivers` | `geography_class` | rivers |
| `seas_and_oceans` | `geography_class` | seas |
| `world_lakes` | `geography_class` | lakes |
| `feelings` | `greeting_card` | feelings |
| `flowers` | `greeting_card` | flowers |
| `greetings_and_farewells` | `greeting_card` | greetings |
| `holidays` | `greeting_card` | holidays |
| `fruits` | `grocery_aisles` | fruits |
| `meats` | `grocery_aisles` | meats |
| `seafood` | `grocery_aisles` | seafood |
| `vegetables` | `grocery_aisles` | vegetables |
| `awards` | `hall_of_fame` | awards |
| `explorers` | `hall_of_fame` | explorers |
| `famous_composers` | `hall_of_fame` | composers |
| `inventors` | `hall_of_fame` | inventors |
| `blades` | `hardware_store` | blades |
| `fasteners` | `hardware_store` | fasteners |
| `storage_containers` | `hardware_store` | containers |
| `things_that_burn` | `hardware_store` | fuels |
| `colors` | `home_decor` | colors |
| `fabrics` | `home_decor` | fabrics |
| `furniture` | `home_decor` | furniture |
| `lighting` | `home_decor` | lighting |
| `patterns` | `home_decor` | patterns |
| `diseases` | `illnesses` | diseases |
| `accessories` | `jewelry_box` | accessories |
| `gemstones` | `jewelry_box` | gemstones |
| `jewelry` | `jewelry_box` | jewelry |
| `metals` | `jewelry_box` | metals |
| `blades` | `kitchen_drawer` | blades |
| `fasteners` | `kitchen_drawer` | fasteners |
| `silverware` | `kitchen_drawer` | silverware |
| `storage_containers` | `kitchen_drawer` | containers |
| `islands` | `landforms` | islands |
| `volcanoes` | `landforms` | volcanoes |
| `biomes` | `map_legend` | biomes |
| `landforms` | `map_legend` | landforms |
| `volcanoes` | `map_legend` | volcanoes |
| `waterfalls` | `map_legend` | waterfalls |
| `gemstones` | `minerals` | gemstones |
| `bones` | `natural_history_museum` | bones |
| `gemstones` | `natural_history_museum` | gemstones |
| `insects` | `natural_history_museum` | insects |
| `minerals` | `natural_history_museum` | minerals |
| `insects` | `pests` | insects |
| `rodents` | `pests` | rodents |
| `birds` | `pet_store` | birds |
| `pets` | `pet_store` | pets |
| `reptiles` | `pet_store` | reptiles |
| `rodents` | `pet_store` | rodents |
| `condiments` | `picnic_basket` | condiments |
| `desserts` | `picnic_basket` | desserts |
| `fruits` | `picnic_basket` | fruits |
| `salads` | `picnic_basket` | salads |
| `moons` | `planets` | moons |
| `lizards` | `reptiles` | lizards |
| `snakes` | `reptiles` | snakes |
| `turtles_and_tortoises` | `reptiles` | turtles |
| `inventions` | `science_fair` | inventions |
| `metals` | `science_fair` | metals |
| `minerals` | `science_fair` | minerals |
| `shapes` | `science_fair` | shapes |
| `volcanoes` | `science_fair` | volcanoes |
| `shellfish` | `seafood` | shellfish |
| `crustaceans` | `shellfish` | crustaceans |
| `bright_stars` | `stargazing` | stars |
| `constellations` | `stargazing` | constellations |
| `moons` | `stargazing` | moons |
| `planets` | `stargazing` | planets |
| `gadgets` | `toy_chest` | gadgets |
| `puzzle_types` | `toy_chest` | puzzles |
| `sports_balls` | `toy_chest` | balls |
| `toys` | `toy_chest` | toys |
| `currencies` | `travel_abroad` | currencies |
| `islands` | `travel_abroad` | islands |
| `languages` | `travel_abroad` | languages |
| `nationalities` | `travel_abroad` | nationalities |
| `aircraft` | `vehicles` | aircraft |
| `heavy_trucks` | `vehicles` | trucks |
| `accessories` | `wardrobe` | accessories |
| `footwear` | `wardrobe` | footwear |
| `hats` | `wardrobe` | hats |
| `sleepwear` | `wardrobe` | sleepwear |
| `directions` | `weather_report` | directions |
| `months` | `weather_report` | months |
| `seasons` | `weather_report` | seasons |
| `storms` | `weather_report` | storms |
