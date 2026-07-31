# Уровни на приёмку

Оценивается уровень целиком: понятны ли категории, естественны ли именно
эти четыре слова, единственно ли решение, есть ли доступный первый ход.
Решения вносятся в `level_decisions.csv` и применяются командой
`apply-level-decisions`.

Уровней в пакете: 5

## L001 — solver_valid

Сложность 3.5 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +1.0). Разбиений: 1. Solver: unique за 0 мс.

| # | категория | правило | четыре слова |
|---|---|---|---|
| 1 | ANIMAL HOMES | Words for the places animals live in | nest, den, barn, mound (mound_dirt) |
| 2 | GARNISHES | Things added on top of a finished dish | cheese, cherry, olive, bacon bits |
| 3 | WORLD CAPITALS | Capital cities of countries around the world | Dublin, Amsterdam, Ottawa, Vienna |
| 4 | LAW JOBS | Jobs held by people who work in the legal system | investigator, magistrate, mediator, notary |
| 5 | MASONRY WORDS | Things a mason works with | level, block (block_cube), stone, joint |

Слова, которые подходят и другим категориям базы:
- nest (дом animal_homes) — также animal_actions,seasons_spring,bird_watching,spring_season
- cheese (дом toppings_and_garnish) — также dairy_words,farm_products,pizza_toppings,sandwich_fillings,salad_ingredients,dairy_products,things_that_melt,words_before_sauce,words_before_cake,yellow_things,smelly_things,fermented_foods
- level (дом masonry_words) — также building_actions,video_game_words,sewing_and_repair,things_in_a_toolbox,hand_tools,measuring_tools,carpentry_words
- den (дом animal_homes) — также home_rooms
- cherry (дом toppings_and_garnish) — также fruits,berries,pie_ingredients,ice_cream_flavors,pie_types,dessert_toppings,trees,things_with_seeds,fruit_trees,red_things,tomato_varieties
- block (дом masonry_words) — также butcher_words,city_words
- barn (дом animal_homes) — также dairy_words,farm_buildings,things_on_a_farm,kinds_of_buildings,places_with_animals,red_things,farm_morning
- olive (дом toppings_and_garnish) — также color_words_advanced,pizza_toppings,salad_ingredients,trees_more,fruit_trees,black_things,colors,greek_dishes,fermented_foods
- Ottawa (дом world_capitals) — также canadian_places
- stone (дом masonry_words) — также sculpture_materials,words_after_head,building_materials,animal_tracks_and_signs
- bacon bits (дом toppings_and_garnish) — также salad_ingredients
- joint (дом masonry_words) — также hand_parts,robot_words

Риски:
- toppings_and_garnish: риск-статус flagged
- world_capitals: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого aaead3eda333.

## L002 — solver_valid

Сложность 3.0 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +0.5). Разбиений: 1. Solver: unique за 0 мс.

| # | категория | правило | четыре слова |
|---|---|---|---|
| 1 | TEXTURES | Words describing how a surface feels | slick, fuzzy, matte, silky |
| 2 | GOVERNMENT JOBS | Jobs held by people who work for a government | inspector, clerk, treasurer, delegate |
| 3 | VOLCANOES | Famous volcanoes | Vesuvius, Mauna Loa, Kilauea, Stromboli |
| 4 | FACIAL EXPRESSIONS | Expressions people make with their face | smile, beam (beam_smile), blink, grin |
| 5 | QUIET THINGS | Things that make almost no sound | sleep, library, cat, snow |

Слова, которые подходят и другим категориям базы:
- Vesuvius (дом volcanoes) — также world_mountains
- smile (дом facial_expressions) — также quiet_actions
- sleep (дом quiet_things) — также quiet_actions,bedtime_things
- fuzzy (дом textures) — также temperature_feel
- clerk (дом government_jobs) — также office_jobs,law_jobs,store_jobs
- library (дом quiet_things) — также school_places,town_places,quiet_places,kinds_of_buildings,monastery_life,programming_words
- treasurer (дом government_jobs) — также office_jobs
- blink (дом facial_expressions) — также quiet_actions,body_movements
- cat (дом quiet_things) — также farm_animals,pets,words_before_fish,words_before_bird
- silky (дом textures) — также temperature_feel
- snow (дом quiet_things) — также weather_actions,things_that_melt,words_before_ball,words_before_man,words_before_board,words_before_bird,weather_words,water_states,mountain_things,seasons_winter,white_things,cold_things

Риски:
- volcanoes: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 77101d8cd8f7.

## L003 — solver_valid

Сложность 3.0 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +0.5). Разбиений: 1. Solver: unique за 0 мс.

| # | категория | правило | четыре слова |
|---|---|---|---|
| 1 | CLEANING SUPPLIES | Tools and products used to clean a house | polish (polish_product), trash bag, brush, soap |
| 2 | TEMPO TERMS | Italian words used to mark tempo in music | grave, piano, forte, largo |
| 3 | US WATERS | Famous lakes and rivers in the United States | Ohio, Michigan, Colorado, Superior |
| 4 | RELIGIOUS CEREMONIES | Ceremonies performed in religious life | confirmation, blessing, communion, sermon |
| 5 | TEA CEREMONY | A vessel, leaf or step of making tea properly | steep, darjeeling, teapot, teahouse |

Слова, которые подходят и другим категориям базы:
- polish (дом cleaning_supplies) — также liquids,nail_words
- grave (дом music_tempo_terms) — также words_before_stone
- Ohio (дом great_lakes_and_us_water) — также us_states
- trash bag (дом cleaning_supplies) — также cleaning_trade
- piano (дом music_tempo_terms) — также music_class_things,musical_instruments,instruments_you_strum,heavy_things
- Michigan (дом great_lakes_and_us_water) — также us_states,world_lakes
- blessing (дом ceremonies) — также prayer_words
- darjeeling (дом tea_ceremony) — также teas
- brush (дом cleaning_supplies) — также art_tools,writing_tools,art_class_things,beauty_tools,wardrobe_care,model_building,bathroom_items,pet_supplies,words_after_air,painting_supplies,art_supplies,cleaning_tools,painting_trade,barbershop_words
- Colorado (дом great_lakes_and_us_water) — также us_states,rivers
- teapot (дом tea_ceremony) — также dishes_and_glassware
- soap (дом cleaning_supplies) — также bathroom_items,liquids,hygiene,things_that_shrink,experiments
- Superior (дом great_lakes_and_us_water) — также world_lakes
- sermon (дом ceremonies) — также prayer_words

Риски:
- ceremonies: риск-статус flagged
- cleaning_supplies: риск-статус flagged
- great_lakes_and_us_water: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 82a6e346bf2d.

## L004 — solver_valid

Сложность 2.5 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5). Разбиений: 1. Solver: unique за 0 мс.

| # | категория | правило | четыре слова |
|---|---|---|---|
| 1 | CLOTHING SIZES | Words used for clothing sizes and fit | large, plus, regular, small |
| 2 | COLD DRINKS | Drinks normally served cold | cola, ginger ale, iced tea, lemonade |
| 3 | KNIGHT THINGS | Things a medieval knight used or wore | horse, sword, shield, banner |
| 4 | RODENT SPECIES | Particular kinds of rodent | house mouse, field mouse, prairie dog, groundhog |
| 5 | GREEK DISHES | Dishes from Greek cuisine | halloumi, souvlaki, tzatziki, moussaka |

Слова, которые подходят и другим категориям базы:
- cola (дом cold_drinks) — также drink_mixers
- horse (дом knights_and_armor) — также farm_animals,pack_animals,livestock,ranch_words,wild_west,transportation_history,things_that_carry_people
- plus (дом clothing_sizes) — также vitamins_letters
- ginger ale (дом cold_drinks) — также drink_mixers
- sword (дом knights_and_armor) — также weapons_of_the_past,pirate_words,words_before_fish,things_made_of_metal,magic_objects,things_that_are_sharp,things_that_cut
- prairie dog (дом rodent_species) — также rodents
- small (дом clothing_sizes) — также opposites,word_small
- lemonade (дом cold_drinks) — также bbq_foods,drink_mixers,seasons_summer,everyday_drinks,picnic
- banner (дом knights_and_armor) — также decorative_things,advertising_words,party_things,castle_things,fan_things
- groundhog (дом rodent_species) — также rodents

Риски:
- cold_drinks: риск-статус flagged
- greek_dishes: риск-статус flagged
- rodent_species: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого dcc4f8e27684.

## L005 — solver_valid

Сложность 4.0 (5 категорий, 20 слов; главный вклад: sense_ambiguity +1.5, alternative_partition_pressure +1.5). Разбиений: 1. Solver: unique за 0 мс.

| # | категория | правило | четыре слова |
|---|---|---|---|
| 1 | RESTAURANT WORDS | Things and roles found at a restaurant | tip (tip_money), menu, chef, booth |
| 2 | BOOK GENRES | Categories used to classify books | science fiction, romance, humor, thriller |
| 3 | ZODIAC SIGNS | Signs of the astrological zodiac | Scorpio, Aries, Aquarius, Virgo |
| 4 | CITY SOUNDS | Sounds heard on a city street | siren (siren_device), rumble, chatter, honk |
| 5 | UNDER LOCK | Something used to lock things away or guard them | code, lock, safe, key (key_lock) |

Слова, которые подходят и другим категориям базы:
- tip (дом restaurant_words) — также money_actions,money_words
- siren (дом city_sounds) — также police_things,emergency_words,loud_things,bell_and_alarm,security_tech
- code (дом under_lock) — также spy_words,emergency_words,programming_words
- menu (дом restaurant_words) — также reading_material
- romance (дом book_genres) — также movie_genres
- rumble (дом city_sounds) — также onomatopoeia,loud_noises
- lock (дом under_lock) — также words_before_room,security_tech,locksmith_words
- chef (дом restaurant_words) — также kitchen_jobs,jobs_that_wear_uniforms,jobs_with_tools,common_professions
- chatter (дом city_sounds) — также ways_of_speaking,words_before_box
- safe (дом under_lock) — также words_before_house,things_made_of_metal,heavy_things,security_tech,locksmith_words
- thriller (дом book_genres) — также movie_genres
- honk (дом city_sounds) — также driving_actions
- key (дом under_lock) — также bedroom_things,collecting_hobbies,things_in_a_junk_drawer,words_before_board,words_before_stone,things_made_of_metal,things_on_a_keychain,locksmith_words,at_the_hotel

Предупреждения по тексту:
- длинный пузырь: science fiction (15 символов)

Риски:
- book_genres: риск-статус flagged
- zodiac_signs: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого ebf965b5570b.
