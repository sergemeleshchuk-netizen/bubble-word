# Уровни на приёмку

Оценивается уровень целиком: понятны ли категории, естественны ли именно
эти четыре слова, единственно ли решение, есть ли доступный первый ход.
Решения вносятся в `level_decisions.csv` и применяются командой
`apply-level-decisions`.

Уровней в пакете: 5

## L001 — solver_valid

Сложность 3.5 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +1.0). Разбиений: 1. Solver: unique за 0 мс.

Качество: знакомость средняя 0.6558, минимальная 0.557; доступность 0.7739; интересность четвёрок 0.7599; качество названий 0.8892.
Слов новизны: доля 0.65; длинных фраз 0; израсходовано неоднозначности 1.0; длины слов {'1-6': 15, '7-10': 4, '11-14': 1, '15+': 0}.

| # | категория | четыре слова | название | четвёрка | интерес | мин. знак. | макс. длина |
|---|---|---|---|---|---|---|---|
| 1 | INTERNAL ORGANS | heart (heart_organ), brain, stomach, liver | 0.8815 | 0.8695 | 0.7427 | 0.597 | 7 |
| 2 | COUNTRY LIFE | general store, well, creek, dirt road | 0.8955 | 0.8426 | 0.844 | 0.6 | 13 |
| 3 | LAB EQUIPMENT | scale (scale_weigh), slide, test tube, rack | 0.8836 | 0.8262 | 0.7837 | 0.557 | 9 |
| 4 | COMPUTER ACTIONS | print, log in, drag, delete | 0.8857 | 0.8697 | 0.7559 | 0.603 | 6 |
| 5 | MORNING ROUTINE | breakfast, coffee, shower, wake | 0.8995 | 0.8387 | 0.673 | 0.643 | 9 |

| слово | знакомость | доступность | новизна | неоднозначность | символов |
|---|---|---|---|---|---|
| heart | 0.759 | 0.855 | 0.137 | 0.4475 | 5 |
| brain | 0.706 | 0.8258 | 0.3651 | 0.0792 | 5 |
| stomach | 0.631 | 0.7596 | 0.8318 | 0.1083 | 7 |
| liver | 0.597 | 0.7659 | 0.972 | 0.1583 | 5 |
| general store | 0.699 | 0.5695 | 0.4054 | 0.0792 | 13 |
| well | 0.861 | 0.9236 | 0.0082 | 0.2667 | 4 |
| creek | 0.624 | 0.7807 | 0.8685 | 0.1583 | 5 |
| dirt road | 0.6 | 0.685 | 0.964 | 0.0792 | 9 |
| scale | 0.69 | 0.817 | 0.46 | 1.0 | 5 |
| slide | 0.614 | 0.7752 | 0.9146 | 0.2667 | 5 |
| test tube | 0.614 | 0.7027 | 0.9146 | 0.0792 | 9 |
| rack | 0.557 | 0.7564 | 0.9812 | 0.5042 | 4 |
| print | 0.649 | 0.7945 | 0.725 | 0.1875 | 5 |
| log in | 0.624 | 0.7682 | 0.8685 | 0.0792 | 6 |
| drag | 0.613 | 0.7872 | 0.9187 | 0.2375 | 4 |
| delete | 0.603 | 0.7567 | 0.955 | 0.0792 | 6 |
| breakfast | 0.659 | 0.745 | 0.6608 | 0.1583 | 9 |
| coffee | 0.694 | 0.8067 | 0.4354 | 0.6208 | 6 |
| shower | 0.643 | 0.7787 | 0.7622 | 0.3167 | 6 |
| wake | 0.68 | 0.824 | 0.5234 | 0.0792 | 4 |

Слова, которые подходят и другим категориям базы:
- scale (дом lab_equipment) — также cooking_hobby,bathroom_items,measurement_devices,measuring_tools,butcher_words,baker_words,world_markets
- print (дом computer_actions) — также words_after_foot,words_after_hand
- breakfast (дом morning_routine) — также meals_of_the_day
- well (дом country_life) — также irrigation,things_on_a_farm,body_of_water_types
- slide (дом lab_equipment) — также ways_of_moving,carrying_actions,dance_moves
- coffee (дом morning_routine) — также hot_drinks,ice_cream_flavors,pantry_staples,words_before_cake,liquids,vending_machine_items,tropical_plants,experiments,gas_station_things,everyday_drinks
- stomach (дом internal_organs) — также body_parts
- creek (дом country_life) — также bodies_of_water
- drag (дом computer_actions) — также carrying_actions,magnets_and_forces
- shower (дом morning_routine) — также bathroom_items,weather_words,juggling_words
- liver (дом internal_organs) — также meats
- rack (дом lab_equipment) — также fashion_show,bowling_words,boxes_and_cases,butcher_words,baker_words,furniture

Риски:
- computer_actions: риск-статус flagged
- country_life: риск-статус flagged
- lab_equipment: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого a1390d84935d.

## L002 — solver_valid

Сложность 3.5 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +1.0). Разбиений: 1. Solver: unique за 0 мс.

Качество: знакомость средняя 0.63, минимальная 0.534; доступность 0.714; интересность четвёрок 0.7304; качество названий 0.8466.
Слов новизны: доля 0.7; длинных фраз 0; израсходовано неоднозначности 0.79; длины слов {'1-6': 12, '7-10': 3, '11-14': 5, '15+': 0}.

| # | категория | четыре слова | название | четвёрка | интерес | мин. знак. | макс. длина |
|---|---|---|---|---|---|---|---|
| 1 | COOKING ACTIONS | steam, drain, slice, blend | 0.8765 | 0.8521 | 0.7777 | 0.564 | 5 |
| 2 | FAMOUS ZOOS | Lincoln Park, London Zoo, National Zoo, Toronto Zoo | 0.895 | 0.7928 | 0.7952 | 0.569 | 12 |
| 3 | SIGNALS AND CODES | sign language, smoke signal, telegraph, beacon | 0.857 | 0.8008 | 0.8144 | 0.534 | 13 |
| 4 | WORKSHOP THINGS | oil can, nail (nail_metal), hammer, drill (drill_tool) | 0.7887 | 0.81 | 0.7464 | 0.584 | 7 |
| 5 | PARKING WORDS | lot, sign, space, spot | 0.8158 | 0.8595 | 0.5184 | 0.699 | 5 |

| слово | знакомость | доступность | новизна | неоднозначность | символов |
|---|---|---|---|---|---|
| steam | 0.646 | 0.7928 | 0.7438 | 0.5042 | 5 |
| drain | 0.581 | 0.7571 | 0.9979 | 0.2667 | 5 |
| slice | 0.571 | 0.7515 | 0.9991 | 0.0792 | 5 |
| blend | 0.564 | 0.7477 | 0.9929 | 0.1583 | 5 |
| Lincoln Park | 0.607 | 0.5364 | 0.9416 | 0.0792 | 12 |
| London Zoo | 0.587 | 0.6004 | 0.9916 | 0.0792 | 10 |
| National Zoo | 0.589 | 0.5365 | 0.9886 | 0.0792 | 12 |
| Toronto Zoo | 0.569 | 0.563 | 0.9979 | 0.0792 | 11 |
| sign language | 0.684 | 0.5412 | 0.4978 | 0.0792 | 13 |
| smoke signal | 0.62 | 0.5335 | 0.8879 | 0.0792 | 12 |
| telegraph | 0.571 | 0.6965 | 0.9991 | 0.1583 | 9 |
| beacon | 0.534 | 0.7187 | 0.906 | 0.1583 | 6 |
| oil can | 0.726 | 0.8118 | 0.2621 | 0.0792 | 7 |
| nail | 0.601 | 0.7806 | 0.9611 | 0.79 | 4 |
| hammer | 0.594 | 0.7517 | 0.979 | 0.375 | 6 |
| drill | 0.584 | 0.7587 | 0.9953 | 0.7608 | 5 |
| lot | 0.801 | 0.8906 | 0.0498 | 0.0792 | 3 |
| sign | 0.726 | 0.8293 | 0.2621 | 0.425 | 4 |
| space | 0.747 | 0.8484 | 0.176 | 0.1583 | 5 |
| spot | 0.699 | 0.8345 | 0.4054 | 0.1875 | 4 |

Слова, которые подходят и другим категориям базы:
- steam (дом cooking_actions) — также laundry_care,cooking_methods,water_states,hot_things,states_of_matter,energy_words
- drain (дом cooking_actions) — также water_actions,body_of_water_types,plumbing_words
- nail (дом workshop_things) — также building_actions,fasteners,hard_things,sewing_and_repair,things_made_of_metal,things_that_are_sharp,things_that_cut,things_that_stick_out
- sign (дом parking_words) — также reading_material,words_before_board,cleaning_trade,road_things,world_markets
- telegraph (дом signals_and_codes) — также industrial_revolution
- hammer (дом workshop_things) — также building_actions,sewing_and_repair,things_in_a_toolbox,hand_tools,things_with_handles
- space (дом parking_words) — также words_after_air
- blend (дом cooking_actions) — также drawing_words
- beacon (дом signals_and_codes) — также navigation_tools
- drill (дом workshop_things) — также building_actions,dentist_things,hand_tools,power_tools,things_that_plug_in,things_that_spin
- spot (дом parking_words) — также words_before_light,words_after_sun

Риски:
- signals_and_codes: риск-статус flagged
- workshop_things: риск-статус flagged
- zoos_and_aquariums: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 80f753950568.

## L003 — solver_valid

Сложность 3.0 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +0.5). Разбиений: 1. Solver: unique за 0 мс.

Качество: знакомость средняя 0.6735, минимальная 0.607; доступность 0.7744; интересность четвёрок 0.7087; качество названий 0.8328.
Слов новизны: доля 0.5; длинных фраз 0; израсходовано неоднозначности 0.6208; длины слов {'1-6': 14, '7-10': 4, '11-14': 2, '15+': 0}.

| # | категория | четыре слова | название | четвёрка | интерес | мин. знак. | макс. длина |
|---|---|---|---|---|---|---|---|
| 1 | FULLNESS WORDS | full, empty, packed, loaded | 0.8092 | 0.8438 | 0.7419 | 0.607 | 6 |
| 2 | EUROPEAN COUNTRIES | Ireland, Spain, Sweden, Greece | 0.8588 | 0.867 | 0.7289 | 0.611 | 7 |
| 3 | ENERGY WORDS | gas, wind, electric, fuel | 0.8163 | 0.8455 | 0.6029 | 0.674 | 8 |
| 4 | BASEBALL WORDS | double play, home run, walk, strike (strike_baseball) | 0.8069 | 0.8117 | 0.6379 | 0.666 | 11 |
| 5 | HOME ELECTRONICS | radio, television, smart speaker, alarm | 0.8729 | 0.8102 | 0.8318 | 0.611 | 13 |

| слово | знакомость | доступность | новизна | неоднозначность | символов |
|---|---|---|---|---|---|
| full | 0.791 | 0.8851 | 0.0646 | 0.2375 | 4 |
| empty | 0.656 | 0.7883 | 0.6803 | 0.1583 | 5 |
| packed | 0.616 | 0.7638 | 0.906 | 0.0792 | 6 |
| loaded | 0.607 | 0.7589 | 0.9416 | 0.0792 | 6 |
| Ireland | 0.666 | 0.7788 | 0.6149 | 0.0792 | 7 |
| Spain | 0.656 | 0.7983 | 0.6803 | 0.1083 | 5 |
| Sweden | 0.629 | 0.771 | 0.8426 | 0.0792 | 6 |
| Greece | 0.611 | 0.7611 | 0.9267 | 0.1875 | 6 |
| gas | 0.716 | 0.8438 | 0.3112 | 0.3458 | 3 |
| wind | 0.691 | 0.83 | 0.4538 | 0.2375 | 4 |
| electric | 0.674 | 0.7607 | 0.5624 | 0.1583 | 8 |
| fuel | 0.674 | 0.8207 | 0.5624 | 0.0792 | 4 |
| double play | 0.701 | 0.6656 | 0.3937 | 0.0792 | 11 |
| home run | 0.76 | 0.7805 | 0.134 | 0.0792 | 8 |
| walk | 0.726 | 0.8493 | 0.2621 | 0.1583 | 4 |
| strike | 0.666 | 0.7813 | 0.6149 | 0.5967 | 6 |
| radio | 0.716 | 0.8313 | 0.3112 | 0.4042 | 5 |
| television | 0.684 | 0.7412 | 0.4978 | 0.325 | 10 |
| smart speaker | 0.619 | 0.5055 | 0.8925 | 0.0792 | 13 |
| alarm | 0.611 | 0.7736 | 0.9267 | 0.6208 | 5 |

Слова, которые подходят и другим категориям базы:
- full (дом fullness_words) — также opposites,words_before_time
- gas (дом energy_words) — также words_before_light,states_of_matter,welding_words,gas_station_things
- radio (дом home_electronics) — также things_with_buttons,things_that_plug_in,police_things,military_things,inventions,sound_devices
- empty (дом fullness_words) — также opposites
- Spain (дом european_countries) — также countries
- wind (дом energy_words) — также weather_words,fast_things
- television (дом home_electronics) — также living_room_things,things_on_a_wall,things_that_plug_in,inventions,screens
- electric (дом energy_words) — также types_of_guitars
- walk (дом baseball_words) — также ways_of_moving
- Greece (дом european_countries) — также ancient_civilizations,countries
- alarm (дом home_electronics) — также words_after_fire,sleep_and_rest,things_that_ring,loud_things,city_sounds,phone_words,security_tech,clock_words,morning_routine,under_lock

Риски:
- baseball_words: риск-статус flagged
- european_countries: риск-статус flagged
- home_electronics: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 0e47e612863e.

## L004 — solver_valid

Сложность 3.5 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +1.0). Разбиений: 1. Solver: unique за 0 мс.

Качество: знакомость средняя 0.6437, минимальная 0.51; доступность 0.7609; интересность четвёрок 0.6954; качество названий 0.8399.
Слов новизны: доля 0.55; длинных фраз 0; израсходовано неоднозначности 1.0; длины слов {'1-6': 13, '7-10': 6, '11-14': 1, '15+': 0}.

| # | категория | четыре слова | название | четвёрка | интерес | мин. знак. | макс. длина |
|---|---|---|---|---|---|---|---|
| 1 | JEWELRY SUPPLIES | hook (hook_fastener), ring blank, cord, gem | 0.8744 | 0.8142 | 0.8255 | 0.553 | 10 |
| 2 | CLOTHING BRANDS | New Balance, Champion, Nike, Adidas | 0.8759 | 0.8375 | 0.7832 | 0.51 | 11 |
| 3 | ADVERTISING WORDS | campaign, commercial, brand (brand_company), ad | 0.7792 | 0.8246 | 0.5899 | 0.68 | 10 |
| 4 | SKATEBOARDING WORDS | wheels, bearing, trucks, helmet | 0.7601 | 0.8004 | 0.7484 | 0.574 | 7 |
| 5 | DAYS & TIMES | Friday, morning, night, Sunday | 0.9098 | 0.8916 | 0.5298 | 0.703 | 7 |

| слово | знакомость | доступность | новизна | неоднозначность | символов |
|---|---|---|---|---|---|
| hook | 0.624 | 0.7932 | 0.8685 | 1.0 | 4 |
| ring blank | 0.58 | 0.6365 | 0.9985 | 0.0792 | 10 |
| cord | 0.569 | 0.763 | 0.9979 | 0.1583 | 4 |
| gem | 0.553 | 0.7542 | 0.972 | 0.0792 | 3 |
| New Balance | 0.679 | 0.6135 | 0.5299 | 0.0792 | 11 |
| Champion | 0.66 | 0.758 | 0.6543 | 0.0792 | 8 |
| Nike | 0.554 | 0.7547 | 0.9744 | 0.1583 | 4 |
| Adidas | 0.51 | 0.7055 | 0.7803 | 0.1583 | 6 |
| campaign | 0.714 | 0.7727 | 0.3216 | 0.1583 | 8 |
| commercial | 0.703 | 0.7116 | 0.3821 | 0.1583 | 10 |
| brand | 0.69 | 0.817 | 0.46 | 0.3275 | 5 |
| ad | 0.68 | 0.824 | 0.5234 | 0.0792 | 2 |
| wheels | 0.607 | 0.7589 | 0.9416 | 0.0792 | 6 |
| bearing | 0.603 | 0.7442 | 0.955 | 0.0792 | 7 |
| trucks | 0.6 | 0.745 | 0.964 | 0.1583 | 6 |
| helmet | 0.574 | 0.7407 | 0.9999 | 0.65 | 6 |
| Friday | 0.709 | 0.815 | 0.3484 | 0.0792 | 6 |
| morning | 0.761 | 0.8311 | 0.1311 | 0.1583 | 7 |
| night | 0.801 | 0.8681 | 0.0498 | 0.3458 | 5 |
| Sunday | 0.703 | 0.8116 | 0.3821 | 0.0792 | 6 |

Слова, которые подходят и другим категориям базы:
- hook (дом jewelry_making) — также fasteners,sewing_supplies,things_on_a_wall,things_that_cut,wardrobe_care
- campaign (дом advertising_words) — также government_branches
- commercial (дом advertising_words) — также tv_words
- morning (дом days_and_parts_of_day) — также greetings_and_farewells
- cord (дом jewelry_making) — также power_and_batteries
- Nike (дом clothing_brands) — также famous_brands
- brand (дом advertising_words) — также business_words
- trucks (дом skateboarding) — также vehicles
- night (дом days_and_parts_of_day) — также opposites,words_before_light,words_before_time,black_things
- Adidas (дом clothing_brands) — также famous_brands
- helmet (дом skateboarding) — также hats,knights_and_armor,military_things,things_made_of_plastic,astronaut_gear,baseball_equipment,football_words,hockey_words,sports_gear_worn,cycling_words,racing_words,safety_gear,welding_words

Риски:
- clothing_brands: риск-статус flagged
- jewelry_making: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 1e3f56b292dc.

## L005 — solver_valid

Сложность 3.0 (5 категорий, 20 слов; главный вклад: alternative_partition_pressure +1.5, sense_ambiguity +0.5). Разбиений: 1. Solver: unique за 0 мс.

Качество: знакомость средняя 0.6161, минимальная 0.526; доступность 0.758; интересность четвёрок 0.721; качество названий 0.8702.
Слов новизны: доля 0.8; длинных фраз 0; израсходовано неоднозначности 0.7142; длины слов {'1-6': 14, '7-10': 5, '11-14': 1, '15+': 0}.

| # | категория | четыре слова | название | четвёрка | интерес | мин. знак. | макс. длина |
|---|---|---|---|---|---|---|---|
| 1 | ASIAN DISHES | spring roll, egg roll, curry, sushi | 0.8794 | 0.8376 | 0.7974 | 0.526 | 11 |
| 2 | RADIO ALPHABET | Victor, delta (delta_letter), Sierra, Echo | 0.8998 | 0.8464 | 0.7819 | 0.577 | 6 |
| 3 | DETECTIVE WORDS | warrant, clue, lineup, motive | 0.7981 | 0.8268 | 0.7678 | 0.563 | 7 |
| 4 | TITLES | chief, lord, miss, sir | 0.8724 | 0.8995 | 0.482 | 0.723 | 5 |
| 5 | YOGA POSES | half moon, warrior, triangle, crow | 0.9015 | 0.8474 | 0.7761 | 0.543 | 9 |

| слово | знакомость | доступность | новизна | неоднозначность | символов |
|---|---|---|---|---|---|
| spring roll | 0.647 | 0.6359 | 0.7376 | 0.0792 | 11 |
| egg roll | 0.611 | 0.7286 | 0.9267 | 0.0792 | 8 |
| curry | 0.566 | 0.7488 | 0.9953 | 0.1875 | 5 |
| sushi | 0.526 | 0.7268 | 0.8685 | 0.2375 | 5 |
| Victor | 0.597 | 0.7534 | 0.972 | 0.0792 | 6 |
| delta | 0.589 | 0.7615 | 0.9886 | 0.7142 | 5 |
| Sierra | 0.58 | 0.744 | 0.9985 | 0.0792 | 6 |
| Echo | 0.577 | 0.7674 | 0.9998 | 0.2375 | 4 |
| warrant | 0.606 | 0.7458 | 0.9451 | 0.1375 | 7 |
| clue | 0.597 | 0.7784 | 0.972 | 0.1875 | 4 |
| lineup | 0.577 | 0.7424 | 0.9998 | 0.1583 | 6 |
| motive | 0.563 | 0.7346 | 0.9916 | 0.0792 | 6 |
| chief | 0.73 | 0.839 | 0.244 | 0.1583 | 5 |
| lord | 0.729 | 0.851 | 0.2484 | 0.0792 | 4 |
| miss | 0.746 | 0.8603 | 0.1796 | 0.0792 | 4 |
| sir | 0.723 | 0.8477 | 0.2763 | 0.1583 | 3 |
| half moon | 0.66 | 0.708 | 0.6543 | 0.1583 | 9 |
| warrior | 0.594 | 0.7392 | 0.979 | 0.0792 | 7 |
| triangle | 0.561 | 0.6986 | 0.9886 | 0.3167 | 8 |
| crow | 0.543 | 0.7487 | 0.9416 | 0.3458 | 4 |

Слова, которые подходят и другим категориям базы:
- warrant (дом detective_words) — также police_things,legal_documents
- chief (дом titles_of_address) — также famous_job_titles
- half moon (дом yoga_poses) — также tide_and_moon
- delta (дом alphabet_code) — также greek_letters
- clue (дом detective_words) — также board_games,detective_work
- curry (дом asian_dishes) — также indian_dishes,sauces
- lineup (дом detective_words) — также baseball_words
- triangle (дом yoga_poses) — также music_class_things,percussion,shapes
- sushi (дом asian_dishes) — также rice_types,japanese_dishes
- Echo (дом alphabet_code) — также mountain_things,cave_things
- sir (дом titles_of_address) — также polite_words
- crow (дом yoga_poses) — также birds,flying_animals,pest_control,black_things

Риски:
- alphabet_code: риск-статус flagged
- asian_dishes: риск-статус flagged
- yoga_poses: риск-статус flagged

Версия генератора level-generator/1.0, seed 20260731, хеш содержимого 14e34a88fd54.
