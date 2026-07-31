# Что осталось решить человеку

Список собран из аудита базы (31.07.2026). Подтверждённые ошибки уже исправлены
в текстовых источниках; здесь то, где автоматическое решение было бы вредным:
нужен носитель языка, продуктовое решение или проверка в реальном интерфейсе.

## 1. Спорная семантика (74 связей)

Связь помечена `semantic_status = disputed`: замечание есть, но однозначно
неверной её назвать нельзя. Такие связи остаются в игре — решение за человеком.

| слово | категория | статус | почему спорно |
|---|---|---|---|
| badminton | CLASSIC GAMES (`card_and_dice_games`) | approved | SWOW: оценка 0.112, доля от лучшей категории слова 0.53; абсолютная заметность 0.72 поднимает до approved |
| charades | CLASSIC GAMES (`card_and_dice_games`) | alternative | нет данных SWOW: абсолютная заметность 0.64 (очевидность 0.75, знакомость 0.34) |
| checkers | CLASSIC GAMES (`card_and_dice_games`) | approved | SWOW: оценка 0.285, доля от лучшей категории слова 0.62 |
| chess | CLASSIC GAMES (`card_and_dice_games`) | approved | SWOW: оценка 0.224, доля от лучшей категории слова 0.60 |
| croquet | CLASSIC GAMES (`card_and_dice_games`) | approved | нет данных SWOW: сохранена ручная разметка |
| dominoes | CLASSIC GAMES (`card_and_dice_games`) | approved | нет данных SWOW: сохранена ручная разметка |
| hide and seek | CLASSIC GAMES (`card_and_dice_games`) | approved | нет данных SWOW: сохранена ручная разметка |
| hopscotch | CLASSIC GAMES (`card_and_dice_games`) | alternative | нет данных SWOW: абсолютная заметность 0.64 (очевидность 0.75, знакомость 0.34) |
| horseshoes | CLASSIC GAMES (`card_and_dice_games`) | alternative | нет данных SWOW: абсолютная заметность 0.65 (очевидность 0.75, знакомость 0.36) |
| jacks | CLASSIC GAMES (`card_and_dice_games`) | approved | нет данных SWOW: сохранена ручная разметка |
| jump rope | CLASSIC GAMES (`card_and_dice_games`) | approved | SWOW: оценка 0.000, доля от лучшей категории слова 0.00; абсолютная заметность 0.77 поднимает до approved |
| marbles | CLASSIC GAMES (`card_and_dice_games`) | approved | нет данных SWOW: сохранена ручная разметка |
| tag | CLASSIC GAMES (`card_and_dice_games`) | approved | SWOW: оценка 0.211, доля от лучшей категории слова 1.00 |
| tiddlywinks | CLASSIC GAMES (`card_and_dice_games`) | hard_only | нет данных SWOW: абсолютная заметность 0.58 (очевидность 0.75, знакомость 0.23) |
| anthem | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.045, доля от лучшей категории слова 1.00; абсолютная заметность 0.74 поднимает до approved |
| bear | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.024, доля от лучшей категории слова 0.24; абсолютная заметность 0.80 поднимает до approved |
| crescent | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.029, доля от лучшей категории слова 0.07; абсолютная заметность 0.71 поднимает до approved |
| crown | NATIONAL SYMBOLS (`flags_and_symbols`) | hard_only | SWOW: оценка 0.032, доля от лучшей категории слова 0.05 |
| dragon | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.030, доля от лучшей категории слова 0.19; абсолютная заметность 0.78 поднимает до approved |
| eagle | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.021, доля от лучшей категории слова 0.03; абсолютная заметность 0.76 поднимает до approved |
| flag | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.087, доля от лучшей категории слова 0.65 |
| kangaroo | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.007, доля от лучшей категории слова 0.01; абсолютная заметность 0.71 поднимает до approved |
| lion | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.045, доля от лучшей категории слова 0.19; абсолютная заметность 0.77 поднимает до approved |
| maple leaf | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.017, доля от лучшей категории слова 1.00; абсолютная заметность 0.72 поднимает до approved |
| rose | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.183, доля от лучшей категории слова 0.32; абсолютная заметность 0.81 поднимает до approved |
| shamrock | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.012, доля от лучшей категории слова 0.02; абсолютная заметность 0.65 поднимает до approved |
| star | NATIONAL SYMBOLS (`flags_and_symbols`) | alternative | SWOW: оценка 0.025, доля от лучшей категории слова 0.08 |
| thistle | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | нет данных SWOW: сохранена ручная разметка |
| tulip | NATIONAL SYMBOLS (`flags_and_symbols`) | approved | SWOW: оценка 0.162, доля от лучшей категории слова 0.19; абсолютная заметность 0.68 поднимает до approved |
| Dreyers | FROZEN TREATS (`frozen_treat_brands`) | candidate | частотность не посчитана: связь закрыта до ручной проверки |
| Edys | FROZEN TREATS (`frozen_treat_brands`) | candidate | частотность не посчитана: связь закрыта до ручной проверки |
| centipede | BUGS (`insects`) | approved | SWOW: оценка 0.565, доля от лучшей категории слова 0.99 |
| spider | BUGS (`insects`) | approved | SWOW: оценка 0.142, доля от лучшей категории слова 0.45; абсолютная заметность 0.87 поднимает до approved |
| tick | BUGS (`insects`) | approved | SWOW: оценка 0.335, доля от лучшей категории слова 1.00 |
| anemone | SOFT CREATURES (`jellyfish_and_soft`) | hard_only | нет данных SWOW: абсолютная заметность 0.60 (очевидность 0.65, знакомость 0.37) |
| coral polyp | SOFT CREATURES (`jellyfish_and_soft`) | hard_only | нет данных SWOW: абсолютная заметность 0.58 (очевидность 0.65, знакомость 0.34) |
| cuttlefish | SOFT CREATURES (`jellyfish_and_soft`) | hard_only | нет данных SWOW: абсолютная заметность 0.60 (очевидность 0.65, знакомость 0.36) |
| jellyfish | SOFT CREATURES (`jellyfish_and_soft`) | alternative | SWOW: оценка 0.186, доля от лучшей категории слова 0.38 |
| man o war | SOFT CREATURES (`jellyfish_and_soft`) | alternative | нет данных SWOW: абсолютная заметность 0.79 (очевидность 0.65, знакомость 0.70) |
| nudibranch | SOFT CREATURES (`jellyfish_and_soft`) | hard_only | нет данных SWOW: абсолютная заметность 0.53 (очевидность 0.65, знакомость 0.24) |
| octopus | SOFT CREATURES (`jellyfish_and_soft`) | alternative | SWOW: оценка 0.275, доля от лучшей категории слова 1.00; категория неочевидная |
| sea cucumber | SOFT CREATURES (`jellyfish_and_soft`) | alternative | нет данных SWOW: абсолютная заметность 0.67 (очевидность 0.65, знакомость 0.49) |
| sea slug | SOFT CREATURES (`jellyfish_and_soft`) | alternative | нет данных SWOW: абсолютная заметность 0.66 (очевидность 0.65, знакомость 0.47) |
| sponge | SOFT CREATURES (`jellyfish_and_soft`) | alternative | SWOW: оценка 0.112, доля от лучшей категории слова 0.36 |
| squid | SOFT CREATURES (`jellyfish_and_soft`) | alternative | SWOW: оценка 0.265, доля от лучшей категории слова 1.00; категория неочевидная |
| big | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.050, доля от лучшей категории слова 0.08; абсолютная заметность 0.89 поднимает до approved |
| cold | OPPOSITES (`opposites`) | alternative | SWOW: оценка 0.044, доля от лучшей категории слова 0.19 |
| dark | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.128, доля от лучшей категории слова 0.59 |
| day | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.109, доля от лучшей категории слова 0.51; абсолютная заметность 0.89 поднимает до approved |
| down | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.118, доля от лучшей категории слова 0.96 |
| dry | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.028, доля от лучшей категории слова 0.08; абсолютная заметность 0.88 поднимает до approved |
| empty | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.023, доля от лучшей категории слова 0.12; абсолютная заметность 0.87 поднимает до approved |
| far | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.046, доля от лучшей категории слова 0.18; абсолютная заметность 0.89 поднимает до approved |
| fast | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.019, доля от лучшей категории слова 0.05; абсолютная заметность 0.89 поднимает до approved |
| full | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.030, доля от лучшей категории слова 0.09; абсолютная заметность 0.89 поднимает до approved |
| hard | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.012, доля от лучшей категории слова 0.03; абсолютная заметность 0.89 поднимает до approved |
| high | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.083, доля от лучшей категории слова 1.00 |
| hot | OPPOSITES (`opposites`) | alternative | SWOW: оценка 0.050, доля от лучшей категории слова 0.15 |
| in | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.041, доля от лучшей категории слова 0.63; абсолютная заметность 0.89 поднимает до approved |
| light | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.072, доля от лучшей категории слова 0.57 |
| low | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.115, доля от лучшей категории слова 1.00 |
| near | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.145, доля от лучшей категории слова 0.25; абсолютная заметность 0.89 поднимает до approved |
| night | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.073, доля от лучшей категории слова 0.21; абсолютная заметность 0.89 поднимает до approved |
| open | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.231, доля от лучшей категории слова 1.00 |
| out | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.054, доля от лучшей категории слова 1.00 |
| shut | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.286, доля от лучшей категории слова 1.00 |
| slow | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.042, доля от лучшей категории слова 0.09; абсолютная заметность 0.89 поднимает до approved |
| small | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.048, доля от лучшей категории слова 0.16; абсолютная заметность 0.89 поднимает до approved |
| soft | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.023, доля от лучшей категории слова 0.12; абсолютная заметность 0.87 поднимает до approved |
| up | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.162, доля от лучшей категории слова 1.00 |
| wet | OPPOSITES (`opposites`) | approved | SWOW: оценка 0.048, доля от лучшей категории слова 0.14; абсолютная заметность 0.86 поднимает до approved |
| glowworm | WORMS (`worms_and_crawlers`) | hard_only | нет данных SWOW: абсолютная заметность 0.55 (очевидность 0.70, знакомость 0.23) |
| inchworm | WORMS (`worms_and_crawlers`) | hard_only | нет данных SWOW: абсолютная заметность 0.55 (очевидность 0.70, знакомость 0.22) |
| silkworm | WORMS (`worms_and_crawlers`) | alternative | нет данных SWOW: абсолютная заметность 0.62 (очевидность 0.70, знакомость 0.34) |

## 2. Категории только для ручной сборки (4)

Правило парное или субъективное, поэтому случайная четвёрка из пула может
не иметь одного общего смысла. Такие категории исключены из автоматической
генерации: уровни для них собираются вручную (таблица `quartets`).

| категория | почему |
|---|---|
| CLASSIC GAMES (`card_and_dice_games`) | Правило субъективное («классическая игра»), сильное пересечение с BOARD GAMES и PLAYGROUND GAMES. |
| NATIONAL SYMBOLS (`flags_and_symbols`) | Страна в данных не хранится, поэтому случайная четвёрка не имеет одного общего правила (замечание аудита). |
| SOFT CREATURES (`jellyfish_and_soft`) | Правило субъективное: под «soft bodied sea creature» подходит слишком много морских беспозвоночных. |
| OPPOSITES (`opposites`) | Правило парное: четвёрка обязана быть двумя полными парами противоположностей. |

## 3. Категории, которые не собирают нормальную четвёрку (6)

Пул есть, но он целиком или почти целиком `hard_only`: обычный уровень из такой
категории не собрать. Нужно решение: добрать понятных слов или оставить категорию
только для сложных уровней.

| категория | почему |
|---|---|
| NAIL SALON (`nail_salon`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| YOUNG ANIMALS (`baby_animal_words_more`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (5) |
| CHICKEN BREEDS (`farm_poultry_breeds`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (6) |
| FRENCH COOKING (`french_cooking_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (11) |
| MOSS & LICHEN (`mosses_and_lichens`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| TRADITIONAL FOOTWEAR (`world_hats_and_dress`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (4) |

## 4. Слова без частотности, закрытые в candidate (28)

`wordfreq` не знает этих слов, поэтому утверждать, что средний игрок их узнает,
нельзя. Связи закрыты и в игру не идут. Решение по каждому: слово настоящее
и понятное — вернуть, нет — убрать из seed.

| слово | категория |
|---|---|
| australorp | CHICKEN BREEDS (`farm_poultry_breeds`) |
| avgolemono | WORLD SOUPS (`world_soups`) |
| babouche | TRADITIONAL FOOTWEAR (`world_hats_and_dress`) |
| Barqs | SODA BRANDS (`soda_brands`) |
| bullsnake | SNAKES (`snakes`) |
| crookneck | MELONS & SQUASH (`melons_and_squash`) |
| croqueta | SPANISH DISHES (`spanish_dishes`) |
| Dreyers | FROZEN TREATS (`frozen_treat_brands`) |
| drywaller | BUILDING TRADES (`building_trades`) |
| Edys | FROZEN TREATS (`frozen_treat_brands`) |
| escalivada | SPANISH DISHES (`spanish_dishes`) |
| galosh | FOOTWEAR (`footwear`) |
| glyptodon | PREHISTORIC ANIMALS (`extinct_and_prehistoric`) |
| harira | WORLD SOUPS (`world_soups`) |
| jaguarundi | SMALL CATS (`wild_cats_small`) |
| jutti | TRADITIONAL FOOTWEAR (`world_hats_and_dress`) |
| kilnfire | POTTERY STUDIO (`pottery_studio`) |
| nailfile | NAIL SALON (`nail_salon`) |
| papadum | INDIAN DISHES (`indian_dishes`) |
| scorepad | GAME PIECES (`board_game_pieces`) |
| screwgun | HAND TOOLS (`hand_tools`) |
| sidestroke | SWIM STROKES (`swimming_strokes`) |
| situp | EXERCISE WORDS (`exercise_words`) |
| tarboosh | WORLD HATS (`world_hats`) |
| Truist | BANK BRANDS (`bank_brands`) |
| viperfish | DEEP SEA (`deep_sea`) |
| WD40 | HARDWARE BRANDS (`paint_and_home`) |
| Yuban | COFFEE BRANDS (`coffee_brands`) |

## 5. Длинные надписи (105)

Больше 15 символов. Влезет ли в пузырь на телефоне — вопрос к реальному интерфейсу,
а не к базе. Либо короткая форма для показа, либо слово убрать.

| слово | символов |
|---|---|
| Declaration of Independence | 27 |
| Emancipation Proclamation | 25 |
| Girl with a Pearl Earring | 25 |
| spaghetti and meatballs | 23 |
| air traffic controller | 22 |
| Jack and the Beanstalk | 22 |
| Mary Had a Little Lamb | 22 |
| Industrial Revolution | 21 |
| Madison Square Garden | 21 |
| synchronized swimming | 21 |
| Beauty and the Beast | 20 |
| green bean casserole | 20 |
| Hickory Dickory Dock | 20 |
| Kennedy Space Center | 20 |
| switchboard operator | 20 |
| Treaty of Versailles | 20 |
| appliance repairman | 19 |
| Baa Baa Black Sheep | 19 |
| Dubai International | 19 |
| father of the bride | 19 |
| Taming of the Shrew | 19 |
| Valley of the Kings | 19 |
| chutes and ladders | 18 |
| construction paper | 18 |
| credit card reader | 18 |
| Gettysburg Address | 18 |
| Great Expectations | 18 |
| herbes de provence | 18 |
| Jet Propulsion Lab | 18 |
| Louisville Slugger | 18 |
| Merchant of Venice | 18 |
| overhead projector | 18 |
| philly cheesesteak | 18 |
| refrigerated truck | 18 |
| Spirit of St Louis | 18 |
| Sydney Opera House | 18 |
| telegraph operator | 18 |
| water purification | 18 |
| astronomical unit | 17 |
| Buckingham Palace | 17 |
| Charles de Gaulle | 17 |
| chicago deep dish | 17 |
| community service | 17 |
| cookies and cream | 17 |
| exclamation point | 17 |
| fill in the blank | 17 |
| Fruit of the Loom | 17 |
| gingerbread house | 17 |
| Hansel and Gretel | 17 |
| Hundred Years War | 17 |
| indian paintbrush | 17 |
| italian seasoning | 17 |
| Itsy Bitsy Spider | 17 |
| Knotts Berry Farm | 17 |
| poultry seasoning | 17 |
| Revolutionary War | 17 |
| rhinoceros beetle | 17 |
| Rocky Mountaineer | 17 |
| search and rescue | 17 |
| Statue of Liberty | 17 |
| table of contents | 17 |
| Three Little Pigs | 17 |
| Universal Studios | 17 |
| Wuthering Heights | 17 |
| anesthesiologist | 16 |
| answering phones | 16 |
| bird of paradise | 16 |
| Black and Decker | 16 |
| black eyed susan | 16 |
| brussels sprouts | 16 |
| cafeteria worker | 16 |
| Call of the Wild | 16 |
| capture the flag | 16 |
| casting director | 16 |
| chicken sandwich | 16 |
| chocolate square | 16 |
| computer science | 16 |
| costume designer | 16 |
| flight attendant | 16 |
| four leaf clover | 16 |
| Georgia Aquarium | 16 |
| Golden Delicious | 16 |
| Great Depression | 16 |
| Huckleberry Finn | 16 |
| Independence Day | 16 |
| Johnny Appleseed | 16 |
| marine biologist | 16 |
| mozzarella stick | 16 |
| Papua New Guinea | 16 |
| parallel parking | 16 |
| physical therapy | 16 |
| principal office | 16 |
| queen annes lace | 16 |
| rhode island red | 16 |
| Roaring Twenties | 16 |
| Romeo and Juliet | 16 |
| shelter building | 16 |
| Sherwin Williams | 16 |
| Sunset Boulevard | 16 |
| Three Blind Mice | 16 |
| three point turn | 16 |
| tightrope walker | 16 |
| ultimate frisbee | 16 |
| Wheel of Fortune | 16 |
| windshield fluid | 16 |

## 6. Решения, принятые по ходу — если не согласны, скажите

- **Категории игры слов без значения.** У `phrase_before`/`phrase_after` связей
  многозначных слов `sense_id` оставлен пустым осознанно: `starboard` не
  происходит от звезды, `keystone` — не от ключа от замка. Приписать им значение
  значит внести в базу ложь. Таких связей 11, они помечены в integrity checks.
- **`fit_score` не является измерением.** У 17 489 связей он равен 0.97, потому
  что это константа из seed, а не оценка. Семантическая корректность вынесена
  в отдельную колонку `semantic_status`; `fit_score` остаётся заявленным
  значением до полного ручного ревью.
- **`hard_only` стало заметно меньше** (2 503 → примерно 900). Аудит показал, что
  статус был перегружен: он одновременно означал «неочевидно» и «сложно».
  Игровая сложность вынесена в `gameplay_difficulty`, а `hard_only` теперь
  значит только «игрок сам не догадается».
- **Пингвин убран из ARCTIC ANIMALS**, а не переименована категория: пул
  из полярного медведя, нарвала и оленя честнее, чем размытие правила.
- **INSECTS переименована в BUGS**, потому что паук и клещ не насекомые,
  а из пула их убирать жалко: игрок группирует их вместе без сомнений.
