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
| spider | BUGS (`insects`) | approved | SWOW: оценка 0.117, доля от лучшей категории слова 0.93 |
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

## 3. Категории, которые не собирают нормальную четвёрку (1058)

Пул есть, но он целиком или почти целиком `hard_only`: обычный уровень из такой
категории не собрать. Нужно решение: добрать понятных слов или оставить категорию
только для сложных уровней.

| категория | почему |
|---|---|
| ALGAE (`algae`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ANCIENT GODS (`ancient_gods`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ANTARCTIC FEATURES (`antarctic_features`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| AUSTRALIAN IDENTITY (`australian_identity`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BACKEND (`backend`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BALLET TERMS (`ballet_terms`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BALTIC CITIES (`baltic_cities`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| BANTER (`banter`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BAT RELATED (`bat_related`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BIOLOGY DOMAINS (`biology_domains`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BOARD GAMES WITH PIECES (`board_games_with_pieces`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BONES IN THE ARM (`bones_in_the_arm`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BOOK COVERS (`book_covers`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BOOT (`boot`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BOTANICAL TERMINOLOGY (`botanical_terminology`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BURIED OBJECTS (`buried_objects`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| BUSYBODY (`busybody`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CALYPSO (`calypso`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CANYONS (`canyons`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CARIBBEAN MUSIC (`caribbean_music`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CARNIVOROUS PLANTS (`carnivorous_plants`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CAT RELATED (`cat_related`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CEPHALOPODS (`cephalopods`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CERAMIC FIRING METHODS (`ceramic_firing_methods`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CHARCUTERIE (`charcuterie`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CLASSICAL GREEK ORDERS (`classical_greek_orders`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| COMING UP WITH IDEAS (`coming_up_with_ideas`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CONDUCTORS DIRECTIONS (`conductors_directions`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CRICKET ANATOMY (`cricket_anatomy`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CRIMINALS (`criminals`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| CUNEIFORM (`cuneiform`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DAM (`dam`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DISPLAYS (`displays`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DIVING EQUIPMENT (`diving_equipment`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DOCTORS TOOLS (`doctors_tools`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DORMANT (`dormant`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DRAMATURGY (`dramaturgy`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DRUM KIT (`drum_kit`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DUNES (`dunes`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| DWARF PLANETS (`dwarf_planets`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| ENDANGERED ANIMALS (`endangered_animals`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ENGLISH SUFFIXES (`english_suffixes`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ENTERTAINMENT COMPLEXES (`entertainment_complexes`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| EPIGRAPHY (`epigraphy`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ERUPTS (`erupts`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| EUPHORIA (`euphoria`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| EXOTIC RODENTS (`exotic_rodents`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| EXPLOSIVE (`explosive`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| EXTINCT BIRDS (`extinct_birds`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| FINCHES (`finches`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| FLEA MARKET (`flea_market`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| FOOD WEB (`food_web`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| FOREST FUNGI (`forest_fungi`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| GREAT DEPRESSION (`great_depression`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| GUITAR PARTS (`guitar_parts`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HAIRBRUSH (`hairbrush`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HAIRDRESSER (`hairdresser`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HERBACEOUS PERENNIALS (`herbaceous_perennials`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HIGH PROTEIN FOODS (`high_protein_foods`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HINDU EPICS (`hindu_epics`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HISTORIOGRAPHY (`historiography`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HOLY BOOKS (`holy_books`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| HUMAN MUSCLES (`human_muscles`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| IAMBIC (`iambic`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| JACKPOT (`jackpot`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| JAPANESE TEA CEREMONY (`japanese_tea_ceremony`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| JUSTIFY (`justify`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| KNIFE TYPES (`knife_types`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| KOREAN FOOD (`korean_food`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| LAB GLASSWARE (`lab_glassware`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| LANCES (`lances`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| LEATHERWORKING TOOLS (`leatherworking_tools`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| LITERARY PERIODS (`literary_periods`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MARTIAL (`martial`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MAST (`mast`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MEDIEVAL ENTERTAINERS (`medieval_entertainers`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MEDITERRANEAN CUISINE (`mediterranean_cuisine`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MICROSCOPY TECHNIQUES (`microscopy_techniques`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MOOSE (`moose`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MOSS (`moss`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MULTIHEADED CREATURES (`multiheaded_creatures`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| MUSICAL ORNAMENTS (`musical_ornaments`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| NAKED (`naked`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| NEUROPEPTIDES (`neuropeptides`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| NONSENSE (`nonsense`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PACK (`pack`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PALAEOGRAPHY (`palaeography`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PALEOGRAPHY (`paleography`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PALEONTOLOGY (`paleontology`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PAPER ARTS (`paper_arts`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PAPER FOLDING ARTS (`paper_folding_arts`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PHENOMENOLOGY (`phenomenology`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PHYLA (`phyla`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| PROSODY (`prosody`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| RECORDING (`recording`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| RESERVED (`reserved`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| RHYME SCHEMES (`rhyme_schemes`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ROBES (`robes`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| ROCKEFELLER FAMILY (`rockefeller_family`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ROMAN GLADIATORS (`roman_gladiators`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SALUT (`salut`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SILK ROAD CITIES (`silk_road_cities`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SLAVIC MYTHOLOGY (`slavic_mythology`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| SNOOZE (`snooze`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SONNET FORMS (`sonnet_forms`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| STAGE MAGIC CATEGORIES (`stage_magic_categories`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| STRATIGRAPHIC TERMS (`stratigraphic_terms`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| STRUCTURAL WEAKNESSES (`structural_weaknesses`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SURFBOARDS (`surfboards`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| SYMBIOSIS TYPES (`symbiosis_types`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TACO TYPES (`taco_types`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TEXTUAL CRITICISM (`textual_criticism`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| THERMAL (`thermal`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| THEY UNLOCK THINGS (`they_unlock_things`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| THINGS THAT TICK (`things_that_tick`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| THINGS YOU SNAP (`things_you_snap`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TOXIC NATURE (`toxic_nature`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TYPES OF BIRDS (`types_of_birds`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TYPES OF PASTRY (`types_of_pastry`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TYPES OF PILLS (`types_of_pills`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| TYPES OF WHALE (`types_of_whale`) | четвёрку не собрать: играбельных слов 2 из нужных 4 |
| VEGAS (`vegas`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| VIOLIN BOWING (`violin_bowing`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| WEEDING TOOLS (`weeding_tools`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| WINE DEFECTS (`wine_defects`) | четвёрку не собрать: играбельных слов 3 из нужных 4 |
| ABBEYS (`abbeys`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ABSTRACT (`abstract`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ACORN (`acorn`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ACTIVE GAMES (`active_games`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ACTS (`acts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ADOBE FONT SIZES (`adobe_font_sizes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ADORNED (`adorned`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AFRICAN KINGDOMS (`african_kingdoms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AFRICAN TRIBES (`african_tribes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ALLOCATE (`allocate`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ALLURE (`allure`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ALPINE PLANTS (`alpine_plants`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ALPINISM (`alpinism`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ALTERNATIVE MUSIC (`alternative_music`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AMERICAN REVOLUTION (`american_revolution`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AMINO ACIDS (`amino_acids`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANALYTICS (`analytics`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT ALPHABET (`ancient_alphabet`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ANCIENT EGYPTIAN PHARAOHS (`ancient_egyptian_pharaohs`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ANCIENT GREEK MODES (`ancient_greek_modes`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ANCIENT GREEK THEATER (`ancient_greek_theater`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT INVENTIONS (`ancient_inventions`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT RUINS (`ancient_ruins`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT THINKERS (`ancient_thinkers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT WAR (`ancient_war`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT WEAPON (`ancient_weapon`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANCIENT WONDERS OF THE WORLD (`ancient_wonders_of_the_world`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANGLING (`angling`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ANIMALS WITH HORNS (`animals_with_horns`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ANNOYING INSECTS (`annoying_insects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AQUARIUM FISH (`aquarium_fish`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARABIAN MYTHOLOGY (`arabian_mythology`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ARABIAN NIGHTS (`arabian_nights`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARABIC LANGUAGE (`arabic_language`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ARCHAEOLOGICAL TOOLS (`archaeological_tools`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ARCHERY EQUIPMENT (`archery_equipment`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| ARCHERY TERMS (`archery_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| ARCHITECTURAL WONDERS (`architectural_wonders`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARCTIC EXPLORERS (`arctic_explorers`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ARIDITY (`aridity`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARMOR PIECES (`armor_pieces`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ART MOVEMENTS (`art_movements`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (4) |
| ART MUSEUMS (`art_museums`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ART SCHOOLS (`art_schools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARTIFICIAL MATERIALS (`artificial_materials`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ARTISAN CRAFTS (`artisan_crafts`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ARTS AND CRAFTS (`arts_and_crafts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ASTRONAUTS (`astronauts`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ASTRONOMY TOOLS (`astronomy_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (4) |
| AUDIO CABLES (`audio_cables`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AUDIO CODECS (`audio_codecs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AUDIO FORMAT (`audio_format`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AURORA (`aurora`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AUSTRALIAN SLANG (`australian_slang`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| AVIARIES (`aviaries`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| YOUNG ANIMALS (`baby_animal_words_more`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (5) |
| BACKYARD ACTIVITIES (`backyard_activities`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BAKEWARE (`bakeware`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BALLET MOVEMENTS (`ballet_movements`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| BALLET POSITIONS (`ballet_positions`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| BAROQUE MUSIC (`baroque_music`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BASKETS (`baskets`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BEANS (`beans`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BEAUTY CARE (`beauty_care`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BEEF CUT (`beef_cut`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BEETLE (`beetle`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BELIEFS (`beliefs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BELIEVER (`believer`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BELLY (`belly`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BEVERAGE PROFESSIONALS (`beverage_professionals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BIOCHEMISTRY (`biochemistry`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BIOLOGY SUBJECTS (`biology_subjects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BIPLANE (`biplane`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BIRDSONG (`birdsong`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| BLACKSMITH SKILLS (`blacksmith_skills`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BLADE GRINDS (`blade_grinds`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BLADE TYPES (`blade_types`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| BLAME (`blame`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BLARING (`blaring`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BOARD SPORTS (`board_sports`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BODYWEIGHT MOVES (`bodyweight_moves`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BOOTLEG (`bootleg`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BOTTLED WATER (`bottled_water`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BOUQUET (`bouquet`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BOWED INSTRUMENTS (`bowed_instruments`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BOWS (`bows`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BRAIDED (`braided`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BRAIN STRUCTURES (`brain_structures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BRAINIAC (`brainiac`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BRAMBLES (`brambles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BRAZILIAN CITIES (`brazilian_cities`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BRAZILIAN CULTURE (`brazilian_culture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (5) |
| BREWERY (`brewery`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| BREWERY EQUIPMENT (`brewery_equipment`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BROADWAY THEATERS (`broadway_theaters`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BROKEN (`broken`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BROWN (`brown`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BUBBLY (`bubbly`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BULL (`bull`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BULLFIGHT (`bullfight`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BUSINESS JARGON (`business_jargon`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BUTTERFLIES (`butterflies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| BYE BYE (`bye_bye`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CABINET HARDWARE (`cabinet_hardware`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CABLE SYSTEMS (`cable_systems`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CAFFEINE PREP (`caffeine_prep`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CAGE (`cage`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CAKE DECORATING (`cake_decorating`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CALLIGRAPHY STYLES (`calligraphy_styles`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CAMPING ACTIVITIES (`camping_activities`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CANDLE TYPES (`candle_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CANDY BAR (`candy_bar`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CANDY FILLINGS (`candy_fillings`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CANDY PIECES (`candy_pieces`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CANIDAE (`canidae`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CAR ENGINE COMPONENTS (`car_engine_components`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CAR GEAR (`car_gear`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CAR SAFETY (`car_safety`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CARBONATE MINERALS (`carbonate_minerals`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CARNIVAL FOODS (`carnival_foods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CARPENTRY JOINTS (`carpentry_joints`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| CARTOGRAPHER (`cartographer`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CARTOON STRIPS (`cartoon_strips`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CATS (`cats`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| CELESTIAL MECHANICS (`celestial_mechanics`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| CELESTIAL OBJECTS (`celestial_objects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CELL PARTS (`cell_parts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CELL TYPES (`cell_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CELLS (`cells`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| CERAMICS HISTORY (`ceramics_history`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHANGING (`changing`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHATTING (`chatting`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHEMICAL LAB GLASSWARE (`chemical_lab_glassware`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHERRY (`cherry`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHESS ENDGAME (`chess_endgame`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHESS GRANDMASTERS (`chess_grandmasters`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHESS PLAYERS (`chess_players`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHILDRENS TV (`childrens_tv`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHIRPING INSECTS (`chirping_insects`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHITIN (`chitin`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHIVALRIC CODE (`chivalric_code`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHOCOLATE BRANDS (`chocolate_brands`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHOPPING TOOLS (`chopping_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHRISTMAS CAROL (`christmas_carol`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHROMOSOME (`chromosome`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CHUCKLE (`chuckle`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CIPHER (`cipher`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CIRCUS PERFORMER (`circus_performer`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CLASSIC ARCADE (`classic_arcade`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CLASSIC ARCADE GAMES (`classic_arcade_games`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CLASSIC OPERAS (`classic_operas`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CLEAR (`clear`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CLIMBING EQUIPMENT (`climbing_equipment`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CLOUD COMPUTING TERMS (`cloud_computing_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| CLOUD FORMATIONS (`cloud_formations`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| CLOUDS (`clouds`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CLUMSY (`clumsy`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COASTAL FEATURES (`coastal_features`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COAT OF ARMS (`coat_of_arms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COAT STYLES (`coat_styles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COCKPIT INSTRUMENTS (`cockpit_instruments`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COCKTAIL FAMILIES (`cocktail_families`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COCKTAIL GARNISH (`cocktail_garnish`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CODED LANGUAGE (`coded_language`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CODICOLOGY (`codicology`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COFFEE BEAN (`coffee_bean`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| COFFEE MACHINE (`coffee_machine`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COFFEE RELATED (`coffee_related`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COFFEE SIZES (`coffee_sizes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COFFEE TOOLS (`coffee_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COGNITIVE LOAD (`cognitive_load`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COIN NAMES (`coin_names`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COLOR MODELS (`color_models`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COLUMBUS (`columbus`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COMIC ART (`comic_art`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COMIC SOUND EFFECTS (`comic_sound_effects`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COMIC STRIP CHARACTERS (`comic_strip_characters`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COMPETES (`competes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CONFUSE (`confuse`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CONSTELLATION NAMES (`constellation_names`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CONSTELLATION PATTERNS (`constellation_patterns`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| COOKIE FLAVORS (`cookie_flavors`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COOKIE VARIETIES (`cookie_varieties`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COOKING TERMS (`cooking_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COOKING VERBS (`cooking_verbs`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (3) |
| CORD (`cord`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CORSET (`corset`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CORVIDS (`corvids`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| COSMETICS INGREDIENTS (`cosmetics_ingredients`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| COSMIC OBJECTS (`cosmic_objects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CRAFTS HOBBIES (`crafts_hobbies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CREATIVE HOBBIES (`creative_hobbies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CRYSTAL TYPES (`crystal_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CRYSTALLINE MINERALS (`crystalline_minerals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CRYSTALLINE STRUCTURES (`crystalline_structures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CULINARY ACIDS (`culinary_acids`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CULINARY FERMENTATION (`culinary_fermentation`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CULINARY HERBS (`culinary_herbs`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CULINARY TECHNIQUES (`culinary_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CULINARY TERMS (`culinary_terms`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CURRENCY PAYMENT (`currency_payment`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| CURTAINS (`curtains`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CZECH CULTURE (`czech_culture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CZECH REPUBLIC (`czech_republic`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DAVID (`david`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DECLINE (`decline`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DEEP FRIED (`deep_fried`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (5) |
| DEEP FRIED FOOD (`deep_fried_food`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DEEP SEA FEATURES (`deep_sea_features`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DEEP SPACE OBJECTS (`deep_space_objects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DELICACY (`delicacy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DENDROCHRONOLOGY (`dendrochronology`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DENIM CUTS (`denim_cuts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DENTAL ANATOMY (`dental_anatomy`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DENTAL DISORDERS (`dental_disorders`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DESERT ANIMAL (`desert_animal`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DESERT LIFE (`desert_life`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DESSERT CREAMS (`dessert_creams`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DESSERT TYPES (`dessert_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DIAGRAMS (`diagrams`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DICE GAMES (`dice_games`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DIFFER (`differ`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DIGITAL FILE TYPES (`digital_file_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DIGITAL FILES (`digital_files`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DINOSAUR (`dinosaur`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DINOSAUR TYPES (`dinosaur_types`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DIPPING SAUCES (`dipping_sauces`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DIVINATION (`divination`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DIVINATION METHODS (`divination_methods`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DOG BREEDS FROM ASIA (`dog_breeds_from_asia`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| DOG SPORTS (`dog_sports`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DOLPHIN (`dolphin`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DONALD (`donald`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DRAWING TECHNIQUES (`drawing_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DRINK (`drink`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DRIVEWAY (`driveway`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DROPS (`drops`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DUCKS (`ducks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DUCTS (`ducts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DUMB (`dumb`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| DWARF (`dwarf`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| DYE (`dye`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EARLY PRINTING (`early_printing`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| EARTH SCIENCES (`earth_sciences`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| EARTH TONES (`earth_tones`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EAST ASIAN ARTS (`east_asian_arts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EAST ASIAN DRESSES (`east_asian_dresses`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| EASTERN SPORTS (`eastern_sports`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ECCLESIASTICAL TERMS (`ecclesiastical_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ECONOMIC THEORIES (`economic_theories`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EDIBLE BARS (`edible_bars`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EGG COOKING STYLES (`egg_cooking_styles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EGGS (`eggs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EGYPT SYMBOLS (`egypt_symbols`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| EGYPTIAN CULTURE (`egyptian_culture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EGYPTIAN PHARAOHS (`egyptian_pharaohs`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (3) |
| ELECTRONIC GADGETS (`electronic_gadgets`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ELEMENTARY PARTICLES (`elementary_particles`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ELUSIVE (`elusive`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EMERGING FIELDS (`emerging_fields`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EMERGING TECHNOLOGIES (`emerging_technologies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ENTOMOLOGY (`entomology`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ENVELOPE (`envelope`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ENZYME (`enzyme`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| ENZYME TYPES (`enzyme_types`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| ENZYMES (`enzymes`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| EPIC LITERATURE (`epic_literature`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EPONYMS (`eponyms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EQUESTRIAN (`equestrian`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ERAS (`eras`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ERROR (`error`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ETHICS (`ethics`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| EVANESCE (`evanesce`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXALT (`exalt`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXOCARP (`exocarp`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXOTIC FRUITS (`exotic_fruits`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| EXPENSIVE FOODS (`expensive_foods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXPLAIN (`explain`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXPLORATION (`exploration`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXTINCT CIVILIZATIONS (`extinct_civilizations`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| EXTINCT FLIGHTLESS BIRDS (`extinct_flightless_birds`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXTINCT LANGUAGES (`extinct_languages`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXTREME AIR SPORTS (`extreme_air_sports`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| EXTREME WEATHER (`extreme_weather`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FABRIC WEAVE (`fabric_weave`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FABRIC WEAVES (`fabric_weaves`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FACE OFF (`face_off`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAIL (`fail`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FALLOUT (`fallout`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAMOUS ARTISTS (`famous_artists`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAMOUS BAYS (`famous_bays`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FAMOUS DIAMONDS (`famous_diamonds`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FAMOUS ESCAPES (`famous_escapes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FAMOUS HOSTS (`famous_hosts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAMOUS OPERAS (`famous_operas`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FAMOUS PLAYWRIGHTS (`famous_playwrights`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAMOUS PYRAMIDS (`famous_pyramids`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FAMOUS STATUES (`famous_statues`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FANTASY COSTUME ELEMENTS (`fantasy_costume_elements`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| CHICKEN BREEDS (`farm_poultry_breeds`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (6) |
| FARMHAND (`farmhand`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FARMING (`farming`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FARMING MACHINERY (`farming_machinery`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAST ANIMALS (`fast_animals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FAST FOOD RESTAURANT CHAINS (`fast_food_restaurant_chains`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FEATHERS (`feathers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FELIDS (`felids`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FEMINIST (`feminist`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FENCING EQUIPMENT (`fencing_equipment`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FENCING TERMS (`fencing_terms`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FERMENTED FOOD (`fermented_food`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| FERN (`fern`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FEUDAL JAPAN (`feudal_japan`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FEUDAL SYSTEM (`feudal_system`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FEUDALISM (`feudalism`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| FICTIONAL FAMILIES (`fictional_families`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FICTIONAL PLANETS (`fictional_planets`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FIESTA (`fiesta`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FIGURE OF SPEECH (`figure_of_speech`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FILLINGS FOR PASTRIES (`fillings_for_pastries`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FILM NOIR (`film_noir`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| FINGER FOODS (`finger_foods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FIREARM PARTS (`firearm_parts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FLEXIBLE METALS (`flexible_metals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FLORISTS (`florists`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOLK DANCES (`folk_dances`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FOLK SONGS (`folk_songs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOOD VENUES (`food_venues`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOR OBSERVATION (`for_observation`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOR SHOPPING (`for_shopping`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FORENSIC (`forensic`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOREST FLOOR (`forest_floor`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FORMATS (`formats`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FORMULAS (`formulas`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FORTRESS (`fortress`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FOSSILS (`fossils`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOUND IN A SWAMP (`found_in_a_swamp`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOUND IN A WORKSHOP (`found_in_a_workshop`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FOUR (`four`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| FOUR HUMORS (`four_humors`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FRENCH CHEESES (`french_cheeses`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| FRENCH COOKING (`french_cooking_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (11) |
| FRENCH CULINARY TERMS (`french_culinary_terms`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| FRENCH CULTURE (`french_culture`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FRENCH REVOLUTION (`french_revolution`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FRICTION (`friction`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FRITTERS (`fritters`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| FROZEN DESSERTS (`frozen_desserts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FRUIT DESSERTS (`fruit_desserts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FRUIT SPREADS (`fruit_spreads`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| FRY CUTS (`fry_cuts`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| FURNITURE FOR RELAXATION (`furniture_for_relaxation`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GALAXY NAMES (`galaxy_names`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GAMBLING ACTIVITIES (`gambling_activities`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GARDEN SHRUBS (`garden_shrubs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GARLIC (`garlic`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| GARMENT POCKET STYLES (`garment_pocket_styles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GASTRONOMY (`gastronomy`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| GELLING (`gelling`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GEMINI (`gemini`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GEMSTONE TREATMENTS (`gemstone_treatments`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GENETIC TERMS (`genetic_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GEOLOGY BRANCHES (`geology_branches`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GERMINATION (`germination`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| GESTURES (`gestures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GHIBLI CHARACTERS (`ghibli_characters`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GLACIAL DEPOSITS (`glacial_deposits`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| GLACIOLOGY (`glaciology`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GLIDER (`glider`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GLOOMY (`gloomy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GLUTEN (`gluten`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GODS (`gods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GODS OF SUN (`gods_of_sun`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GOSSAMER (`gossamer`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GOURMET (`gourmet`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| GRAFFITI (`graffiti`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GRAMMATICAL CASES (`grammatical_cases`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GRANARY (`granary`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GRANITE (`granite`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GRAPHICS (`graphics`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GRASSLANDS (`grasslands`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GRASSY (`grassy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GREAT APES (`great_apes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GREED (`greed`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GREEK UNDERWORLD (`greek_underworld`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GREEKS (`greeks`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| GREENS (`greens`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GREET (`greet`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| GRIMY (`grimy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| GROUP THEORY (`group_theory`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HADRON (`hadron`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| HAIR PROBLEMS (`hair_problems`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HAIRDOS (`hairdos`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HALF HUMANS (`half_humans`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HANNUKAH (`hannukah`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| HARD TO FIND (`hard_to_find`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HARD WORKING ANIMALS (`hard_working_animals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HAS A TAIL (`has_a_tail`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HAS STRIPES (`has_stripes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HASH FUNCTIONS (`hash_functions`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HEDGE (`hedge`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HERALDIC ANIMALS (`heraldic_animals`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HERALDIC CHARGES (`heraldic_charges`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HERALDIC SYMBOLS (`heraldic_symbols`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HERALDIC TERMS (`heraldic_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HERB FLAVORS (`herb_flavors`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HIBACHI (`hibachi`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HIGHEST PEAKS (`highest_peaks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HIKING (`hiking`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HIP HOP (`hip_hop`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HISTORIC RULERS (`historic_rulers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HISTORICAL METHODOLOGIES (`historical_methodologies`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HOMO (`homo`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| HOODED (`hooded`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HORMONE (`hormone`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HORMONES (`hormones`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HORSE COATS (`horse_coats`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HOSPITAL SERVICES (`hospital_services`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HOT SAUCES (`hot_sauces`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HOUSEPLANT CARE (`houseplant_care`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HOUSING FOR ANIMALS (`housing_for_animals`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| HUMAN BLOOD COMPONENTS (`human_blood_components`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HUMAN POWERED (`human_powered`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HUMAN TEETH (`human_teeth`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HUNGARY (`hungary`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (3) |
| HUTS (`huts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| HYDRAULICS (`hydraulics`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ICE CREAM BRANDS (`ice_cream_brands`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ILLUSIVE (`illusive`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| IMAGE (`image`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| IMMUNOLOGY CELLS (`immunology_cells`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| IMPRESSIONISTS (`impressionists`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| INCENSE (`incense`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| INDIAN (`indian`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| INDIAN CUISINE (`indian_cuisine`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (3) |
| INEPT (`inept`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| INJECT (`inject`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| INSTRUMENTS OF MEASURE (`instruments_of_measure`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| INTERNET PROTOCOLS (`internet_protocols`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| INTERTWINE (`intertwine`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| INTRIGUE (`intrigue`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ITALIAN COMPOSERS (`italian_composers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ITALIAN CULINARY TERMS (`italian_culinary_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ITALIAN RESTAURANT MENU (`italian_restaurant_menu`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| IVY (`ivy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JAPANESE FOODS (`japanese_foods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JAPANESE POETRY FORMS (`japanese_poetry_forms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| JAPANESE RANKS (`japanese_ranks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JAPANESE WRITING (`japanese_writing`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| JASON (`jason`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JEEP CARS (`jeep_cars`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JET (`jet`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JEWELRY SETTINGS (`jewelry_settings`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JEWISH CULTURE (`jewish_culture`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| JOCKEY (`jockey`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JOGGLE (`joggle`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JUMPSUIT (`jumpsuit`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| JUNGLE ANIMAL (`jungle_animal`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| JURASSIC (`jurassic`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| KIND (`kind`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| KISS (`kiss`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| KNIGHTS TOURNAMENT (`knights_tournament`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| KNITTING STITCHES (`knitting_stitches`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| KNITTING TERMS (`knitting_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| KNOT TYPES (`knot_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| KOREA (`korea`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LABORATORY (`laboratory`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| LANDING (`landing`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LANDMARK YEARS (`landmark_years`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LANGUAGE LEARNING APPS (`language_learning_apps`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| LANGUAGE STUDIES (`language_studies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LANGUAGE UNITS (`language_units`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LANGUAGES IN AFRICA (`languages_in_africa`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LATIN (`latin`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LATIN AMERICAN DANCES (`latin_american_dances`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| LAUGHING (`laughing`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| LEATHER (`leather`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (4) |
| LEATHER TYPES (`leather_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LEATHER WORKING (`leather_working`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LEGWEAR (`legwear`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LEPORIDS (`leporids`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LIFESAVING (`lifesaving`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LIMBIC (`limbic`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LINENS (`linens`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| LINGERIE (`lingerie`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LINGUISTIC BRANCHES (`linguistic_branches`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LINGUISTIC FEATURES (`linguistic_features`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LINGUISTIC FIELDS (`linguistic_fields`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LINGUISTIC TERMS (`linguistic_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| LITERARY CRITICISM (`literary_criticism`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LITERARY FORMS (`literary_forms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LITTER (`litter`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LITTLE BITES (`little_bites`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LITURGICAL MUSIC (`liturgical_music`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| LIVE MUSIC VENUES (`live_music_venues`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LIZARD (`lizard`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| LOGIN OPTIONS (`login_options`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| LOOM PARTS (`loom_parts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LOST SPECIES (`lost_species`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| LUXURY TEXTURES (`luxury_textures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MACBETH (`macbeth`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MAGIC PHRASES (`magic_phrases`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| MAGIC SYSTEM TYPES (`magic_system_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MAGIC TERMS (`magic_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MAN POWERED TRANSPORT (`man_powered_transport`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MANDOLIN (`mandolin`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| MANICURE (`manicure`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MARITIME (`maritime`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MARTIAL DISCIPLINES (`martial_disciplines`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MATHEMATICIANS (`mathematicians`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEAT DELICACIES (`meat_delicacies`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MECHANICAL WATCH PARTS (`mechanical_watch_parts`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MEDICAL SPECIALIZATIONS (`medical_specializations`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEDICINAL PLANTS (`medicinal_plants`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MEDIEVAL ARMOR (`medieval_armor`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEDIEVAL CRAFTS (`medieval_crafts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEDIEVAL MILITARY (`medieval_military`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEDIEVAL PASTIME (`medieval_pastime`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MEDIEVAL SIEGE WEAPONS (`medieval_siege_weapons`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MEDIEVAL SWORDS (`medieval_swords`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| MEDIEVAL WRITING (`medieval_writing`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MELON (`melon`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MENDING (`mending`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| METAMORPHIC ROCKS (`metamorphic_rocks`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| MEXICAN (`mexican`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MICROBE (`microbe`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MICROSCOPE TYPES (`microscope_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MILITARY UNIFORM (`military_uniform`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MINERAL FORMATIONS (`mineral_formations`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MINERAL ORES (`mineral_ores`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MINOS (`minos`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| MIXTURE (`mixture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOBILE PHONE (`mobile_phone`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MODES OF TRANSPORT (`modes_of_transport`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MONEY STORAGE (`money_storage`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MONGOL EMPIRE (`mongol_empire`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MONKEY (`monkey`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (7) |
| MONOGRAM (`monogram`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOORING (`mooring`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MORPHOLOGY (`morphology`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOSAIC ART (`mosaic_art`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOSAICS (`mosaics`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOSS & LICHEN (`mosses_and_lichens`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| MOUNTAIN EQUIPMENT (`mountain_equipment`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| MOUNTAIN FEATURES (`mountain_features`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOUNTAIN HAZARDS (`mountain_hazards`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MOVING QUIETLY (`moving_quietly`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MOWGLI (`mowgli`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MULTI LEGGED (`multi_legged`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MULTI LEGGED CREATURES (`multi_legged_creatures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MURKY (`murky`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSCLE GROUPS (`muscle_groups`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSHROOM (`mushroom`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (4) |
| MUSHROOM VARIETIES (`mushroom_varieties`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MUSIC FESTIVALS (`music_festivals`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MUSIC PLAYERS (`music_players`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSIC TYPES (`music_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSICAL DIRECTIONS (`musical_directions`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSICAL ENSEMBLES (`musical_ensembles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSICAL GROUPS (`musical_groups`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MUSICAL SPEEDS (`musical_speeds`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| MUSICAL TEMPO MARKINGS (`musical_tempo_markings`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSICAL TEMPOS (`musical_tempos`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| MUSTY (`musty`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| MYCOLOGIST (`mycologist`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NAIL CARE TOOLS (`nail_care_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NAMES FOR MONEY (`names_for_money`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| NASCAR (`nascar`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NAUTICAL EQUIPMENT (`nautical_equipment`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NAUTICAL ROPE WORK (`nautical_rope_work`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| NAUTICAL ROPES (`nautical_ropes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NAUTICAL SAILS (`nautical_sails`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| NAUTICAL TOOLS (`nautical_tools`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| NAVIGATION INSTRUMENTS (`navigation_instruments`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| NEPTUNE (`neptune`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NEUTRINO (`neutrino`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| NEW ZEALAND (`new_zealand`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| NEXUS (`nexus`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NINJA (`ninja`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NOODLE DISHES (`noodle_dishes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| NOODLES (`noodles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (4) |
| NORWAY (`norway`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| NURSING TOOLS (`nursing_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OBELISK (`obelisk`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OBSERVATORY (`observatory`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OCEAN CREATURES (`ocean_creatures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OCEAN CURRENTS (`ocean_currents`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OCEAN MAMMALS (`ocean_mammals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ODYSSEUS (`odysseus`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OENOLOGY TERMS (`oenology_terms`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| OK GESTURE (`ok_gesture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OKAPI (`okapi`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OLD NORSE MYTHOLOGY (`old_norse_mythology`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| OLD TIME (`old_time`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OMIT (`omit`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ONLINE MEDIA (`online_media`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OPERA TERMS (`opera_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OPERAS (`operas`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| OPULENT (`opulent`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ORBITAL MECHANICS (`orbital_mechanics`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| ORCHESTRAL SECTIONS (`orchestral_sections`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ORGANIC CHEMISTRY (`organic_chemistry`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (4) |
| ORGANIZATIONAL SYSTEMS (`organizational_systems`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OTTOMAN (`ottoman`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OUTDOOR GAMES (`outdoor_games`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| OUTFIT (`outfit`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| OYSTER (`oyster`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PALEONTOLOGY EQUIPMENT (`paleontology_equipment`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PALEONTOLOGY TOOLS (`paleontology_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PALLID (`pallid`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PANORAMA (`panorama`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARROT SPECIES (`parrot_species`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PARTNER DANCES (`partner_dances`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARTS OF A CANOE (`parts_of_a_canoe`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARTS OF A CELL (`parts_of_a_cell`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PARTS OF A COMPASS (`parts_of_a_compass`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARTS OF A LETTER (`parts_of_a_letter`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARTS OF A TELESCOPE (`parts_of_a_telescope`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PARTS OF ANIMALS (`parts_of_animals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PARTY GAMES (`party_games`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PASTA TYPES (`pasta_types`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PASTRY DOUGH (`pastry_dough`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PASTRY TYPES (`pastry_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PEAK (`peak`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PENDANTS (`pendants`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PENGUINS (`penguins`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PEPPERS (`peppers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| PERFUME BRANDS (`perfume_brands`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PERFUME NOTES (`perfume_notes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PERSONAL CARE (`personal_care`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PERSONALITY DISORDERS (`personality_disorders`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PERSUASIVE TECHNIQUES (`persuasive_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHARMACOLOGY (`pharmacology`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHILATELY (`philately`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PHILOSOPHY SCHOOLS (`philosophy_schools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHILOSOPHY TERMS (`philosophy_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHONETIC (`phonetic`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PHONETICS SYMBOLS (`phonetics_symbols`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHONOLOGY (`phonology`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| PHOTOGRAPHY TECHNIQUES (`photography_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PHOTOGRAPHY TOOLS (`photography_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PIANO PARTS (`piano_parts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PIGMENT CHEMISTRY (`pigment_chemistry`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PILLS (`pills`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PISAGOR (`pisagor`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PLANE TYPES (`plane_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PLATING (`plating`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PLAY AROUND (`play_around`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PLUCKED INSTRUMENTS (`plucked_instruments`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PLUTO (`pluto`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POCKET STYLES (`pocket_styles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POEM (`poem`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POETIC FORMS (`poetic_forms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| POETIC STRESS (`poetic_stress`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POETRY FORMS (`poetry_forms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POETRY TYPES (`poetry_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| POKER TOURNAMENT STRUCTURE (`poker_tournament_structure`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POKER VARIANTS (`poker_variants`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POLISHED (`polished`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POLITICAL TACTICS (`political_tactics`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PORTRAY (`portray`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| POTTERY TECHNIQUES (`pottery_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PREHISTORIC PERIODS (`prehistoric_periods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PRESERVATION (`preservation`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PREY (`prey`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| PRINTING FORMS (`printing_forms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PRINTMAKING TECHNIQUES (`printmaking_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PROCESS (`process`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| PRODUCT STORAGE (`product_storage`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PROJECT METHODOLOGIES (`project_methodologies`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PROVINCES OF JAPAN (`provinces_of_japan`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PULSAR (`pulsar`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PUMPKIN VARIETIES (`pumpkin_varieties`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PUNKS (`punks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PUPPET THEATER (`puppet_theater`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PUPPET TYPES (`puppet_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| PUREE (`puree`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| PYTHON (`python`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| QUANTUM STATES (`quantum_states`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| QUARTZ (`quartz`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| QUILL (`quill`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RABBITS (`rabbits`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RACKET SPORTS (`racket_sports`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| RACQUET SPORTS (`racquet_sports`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RAINFOREST LAYERS (`rainforest_layers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RAKES (`rakes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RAPTOR (`raptor`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RARE BIRDS (`rare_birds`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| RARE FAUNA (`rare_fauna`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| RAW DISH (`raw_dish`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RAZOR BRANDS (`razor_brands`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| REED (`reed`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| REFRIGERATOR PARTS (`refrigerator_parts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RELICS (`relics`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RENAISSANCE COMPOSERS (`renaissance_composers`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| RENAISSANCE PAINTERS (`renaissance_painters`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RENAISSANCE WRITERS (`renaissance_writers`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RESTAURANT DISHES (`restaurant_dishes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RESTAURANT ROLES (`restaurant_roles`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RETRO GAMING CONSOLES (`retro_gaming_consoles`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RHETORIC TECHNIQUES (`rhetoric_techniques`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RHETORICAL DEVICES (`rhetorical_devices`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| RHETORICAL FIGURES (`rhetorical_figures`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| RHUBARB (`rhubarb`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RICE VARIETIES (`rice_varieties`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| RIDING A MOTORCYCLE (`riding_a_motorcycle`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ROAD ESSENTIALS (`road_essentials`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ROCK COLLECTION ITEMS (`rock_collection_items`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RODENT (`rodent`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ROMAN (`roman`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ROOF TYPES (`roof_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| ROOFTOP (`rooftop`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| ROSEMARY (`rosemary`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RUBBERY (`rubbery`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RUDIMENTARY STRUCTURES (`rudimentary_structures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RUSSIAN EMPIRE (`russian_empire`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| RUST (`rust`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SADDLE (`saddle`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SAILS (`sails`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SANDWICH NAMES (`sandwich_names`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SANSKRIT TERMS (`sanskrit_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| SAUSAGE TYPES (`sausage_types`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| SCALES (`scales`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SCAT (`scat`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| SCOTLAND (`scotland`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SCRIPT (`script`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| SEA FOAM (`sea_foam`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEAFOOD RESTAURANT (`seafood_restaurant`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEAHORSE (`seahorse`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEASONING TYPES (`seasoning_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEAWEED TYPES (`seaweed_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SEDAN (`sedan`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEED (`seed`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SEMIOTICS TERMS (`semiotics_terms`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SHADES OF GRAY (`shades_of_gray`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SHAKES (`shakes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SHAKESPEARE CHARACTERS (`shakespeare_characters`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SHIP SAILS (`ship_sails`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SHIPBUILDING (`shipbuilding`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SHOE (`shoe`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| SIEGE WEAPONS (`siege_weapons`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SIGHING (`sighing`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SIGNAL (`signal`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SIGNAL SYSTEMS (`signal_systems`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SILKY (`silky`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SINISTER (`sinister`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SINUOUS (`sinuous`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SITUATIONS IN CHESS (`situations_in_chess`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SKATEBOARD TRICKS (`skateboard_tricks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SKUNK (`skunk`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SKY CONSTELLATIONS (`sky_constellations`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SLAPSTICK (`slapstick`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SNOWFALL (`snowfall`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SOFT DRINKS (`soft_drinks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SOIL SCIENCE (`soil_science`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SOUP STOCKS (`soup_stocks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SOUP VARIETIES (`soup_varieties`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| SOUTH POLE (`south_pole`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPACE PHYSICS (`space_physics`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPACE PIONEERS (`space_pioneers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPACE ROCKS (`space_rocks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPAIN DISHES (`spain_dishes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SPANISH CUISINE (`spanish_cuisine`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (4) |
| SPEECH DISORDERS (`speech_disorders`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SPEECH FIGURES (`speech_figures`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPIKY (`spiky`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPINNING (`spinning`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPLICE (`splice`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPRINKLY (`sprinkly`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SPROUTS (`sprouts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SPY (`spy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SQUIRREL (`squirrel`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STAR CLUSTER (`star_cluster`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STAR PATTERNS (`star_patterns`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| STEAK CUTS (`steak_cuts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STEAKS (`steaks`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| STEAL (`steal`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STEAM BATH (`steam_bath`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| STEPPES (`steppes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| STINGING INSECTS (`stinging_insects`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STOCHASTIC PROCESSES (`stochastic_processes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| STREET FEATURES (`street_features`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STREET LAMP (`street_lamp`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STREET PERFORMERS (`street_performers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| STUNTS (`stunts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SUBDUERS (`subduers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SUDDEN (`sudden`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SUMMER DRINKS (`summer_drinks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SUNDRESS (`sundress`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SUPERHERO POWERS (`superhero_powers`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| SUPERMAN FOES (`superman_foes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SURGERY TOOLS (`surgery_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SURGICAL INSTRUMENTS (`surgical_instruments`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| SURVEYOR (`surveyor`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SWEDEN (`sweden`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| SWEEP (`sweep`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SWIFT ANIMALS (`swift_animals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| SWORDS (`swords`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TABOOS (`taboos`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TACTICS (`tactics`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TALKATIVE (`talkative`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TAPESTRY (`tapestry`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TAPESTRY TECHNIQUES (`tapestry_techniques`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TAROT CARD CATEGORIES (`tarot_card_categories`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TAROT CARD SUITS (`tarot_card_suits`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEA TIME (`tea_time`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TELESCOPE TYPES (`telescope_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TELLS TIME (`tells_time`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEMPLES (`temples`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEMPO (`tempo`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TEMPOS (`tempos`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEPHRA (`tephra`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TETHER (`tether`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEX MEX (`tex_mex`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TEXT FILE TYPES (`text_file_types`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TEXTILE DYES (`textile_dyes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TEXTILE PATTERNS (`textile_patterns`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THAI DISHES (`thai_dishes`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| THAI FOOD (`thai_food`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THE BOOT (`the_boot`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| THEATER DISTRICTS (`theater_districts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THEATER TERMS (`theater_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THEATRICAL TRADITIONS (`theatrical_traditions`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| THEY HAVE STRIPES (`they_have_stripes`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THICKENING AGENTS (`thickening_agents`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THIEVES (`thieves`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| THINGS WITH A FLAP (`things_with_a_flap`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THINGS YOU DIG (`things_you_dig`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THINKERS (`thinkers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THORNY PLANTS (`thorny_plants`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| THUMP (`thump`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| THUNDER GODS (`thunder_gods`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TIDAL FORCES (`tidal_forces`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TILE LAYOUT (`tile_layout`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TIME TRACKING DEVICES (`time_tracking_devices`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TOPOLOGY CONCEPTS (`topology_concepts`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TOXIC MUSHROOMS (`toxic_mushrooms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TOXICOLOGY TERMS (`toxicology_terms`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TRACTOR (`tractor`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TRADE WORKERS (`trade_workers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TRADITIONAL CRAFTS (`traditional_crafts`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| TREELESS (`treeless`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TRIANGLES (`triangles`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TRINKET (`trinket`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (3) |
| TRIP HOP (`trip_hop`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TUBA (`tuba`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TURKISH CULTURE (`turkish_culture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TUSCANY (`tuscany`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TV SHOW (`tv_show`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF BEER (`types_of_beer`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF BREAD (`types_of_bread`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF CHEFS (`types_of_chefs`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TYPES OF CLIMATE (`types_of_climate`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF CLOCKS (`types_of_clocks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF CORAL (`types_of_coral`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TYPES OF CURTAINS (`types_of_curtains`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF DOUGH (`types_of_dough`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TYPES OF ENCRYPTION (`types_of_encryption`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF FEEDING (`types_of_feeding`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF FIREWORKS (`types_of_fireworks`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF GRAVY (`types_of_gravy`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF HORSES (`types_of_horses`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF INK (`types_of_ink`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF KNOT (`types_of_knot`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF NATURAL DYE (`types_of_natural_dye`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF PASTA SAUCE (`types_of_pasta_sauce`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF PIGEONS (`types_of_pigeons`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF POKER (`types_of_poker`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF ROOFS (`types_of_roofs`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF ROPE (`types_of_rope`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF SOUPS (`types_of_soups`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF THERAPY (`types_of_therapy`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| TYPES OF WINDOWS (`types_of_windows`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPES OF YOGURT (`types_of_yogurt`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| TYPESETTING TERMS (`typesetting_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| UNDERWEAR (`underwear`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| UNI WORDS (`uni_words`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| UNITS OF VOLUME (`units_of_volume`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| UNSEEN FORCES (`unseen_forces`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| UPHOLSTERY (`upholstery`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| URL (`url`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| USED TO STOP (`used_to_stop`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| USES FILTER (`uses_filter`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VASE (`vase`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VEDIC PHILOSOPHY (`vedic_philosophy`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| VEDIC TEXTS (`vedic_texts`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| VEGETARIAN FOODS (`vegetarian_foods`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| VICTORIAN DRESS ELEMENTS (`victorian_dress_elements`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| VIDEO GAME BOSSES (`video_game_bosses`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| VIDEO GAME CONTROLLERS (`video_game_controllers`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| VIKING CULTURE (`viking_culture`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VINTAGE DRESS (`vintage_dress`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VINTAGE PHOTOGRAPHY (`vintage_photography`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VINTAGE SODA (`vintage_soda`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VISIBLE VIA MICROSCOPE (`visible_via_microscope`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VISIONS (`visions`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VISITOR TYPES (`visitor_types`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VODKA (`vodka`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| VOICE TYPES (`voice_types`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| VOLCANIC ACTIVITY (`volcanic_activity`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| VR TECH (`vr_tech`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WALLET (`wallet`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WARMTH (`warmth`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WASTE TIME (`waste_time`) | нормальную четвёрку не собрать: слов уровня 0, весь остальной пул hard_only (4) |
| WATER PURIFICATION (`water_purification`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WEATHER TOOLS (`weather_tools`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WEAVING EQUIPMENT (`weaving_equipment`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WEAVING PATTERNS (`weaving_patterns`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (2) |
| WEAVING TERMS (`weaving_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WEBPAGE SECTIONS (`webpage_sections`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WEDDING TRADITIONS (`wedding_traditions`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WELLNESS TREATMENTS (`wellness_treatments`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| WINE DESCRIPTORS (`wine_descriptors`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WINE GRAPE VARIETALS (`wine_grape_varietals`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WINE TASTING TERMS (`wine_tasting_terms`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WINE TERMS (`wine_terms`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WINE VARIETALS (`wine_varietals`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WINEMAKING (`winemaking`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WINEMAKING TERMS (`winemaking_terms`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| WING FLAVORS (`wing_flavors`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WINGED (`winged`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WINTER ACCESSORIES (`winter_accessories`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WIZARDS (`wizards`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WOODWORKING JOINTS (`woodworking_joints`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (5) |
| WORDS ENDING IN O (`words_ending_in_o`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WORDS FOR PALE (`words_for_pale`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WORDS FOR STARE (`words_for_stare`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (2) |
| WORDS FOR WALK (`words_for_walk`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| WORLD DESSERTS (`world_desserts`) | нормальную четвёрку не собрать: слов уровня 1, весь остальной пул hard_only (3) |
| TRADITIONAL FOOTWEAR (`world_hats_and_dress`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (4) |
| WORLD HEALTH DAY (`world_health_day`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |
| YOGURT (`yogurt`) | нормальную четвёрку не собрать: слов уровня 2, весь остальной пул hard_only (3) |
| ZANZIBAR (`zanzibar`) | нормальную четвёрку не собрать: слов уровня 3, весь остальной пул hard_only (1) |

## 4. Слова без частотности, закрытые в candidate (1462)

`wordfreq` не знает этих слов, поэтому утверждать, что средний игрок их узнает,
нельзя. Связи закрыты и в игру не идут. Решение по каждому: слово настоящее
и понятное — вернуть, нет — убрать из seed.

| слово | категория |
|---|---|
| abs | MUSCLES (`muscles`) |
| abstract | ART STYLES (`art_styles`) |
| abyss | DEEP SEA (`deep_sea`) |
| accordion | MUSICAL INSTRUMENTS (`musical_instruments`) |
| Achilles | MYTHOLOGICAL HEROES (`greek_heroes`) |
| Acropolis | FAMOUS LANDMARKS (`famous_landmarks`) |
| acrylic | KINDS OF PAINT (`paint_types`) |
| action | MOVIE GENRES (`movie_genres`) |
| admiral | MILITARY RANKS (`military_ranks`) |
| adult | STAGES OF LIFE (`life_stages`) |
| aerial | PHOTO SUBJECTS (`photography_styles`) |
| affogato | COFFEE DRINKS (`coffee_drinks`) |
| afro | HAIRSTYLES (`hairstyles`) |
| aikido | MARTIAL ARTS (`martial_arts`) |
| air force | MILITARY BRANCHES (`military_branches`) |
| Alabama | US STATES (`us_states`) |
| alarm | RINGING THINGS (`things_that_ring`) |
| Alaska | US STATES (`us_states`) |
| algebra | SCHOOL SUBJECTS (`school_subjects`) |
| alpha | GREEK LETTERS (`greek_letters`) |
| Alps | MOUNTAIN RANGES (`mountain_ranges`) |
| aluminum | METALS (`metals`) |
| Amazon | RIVERS (`rivers`) |
| americano | COFFEE DRINKS (`coffee_drinks`) |
| amethyst | GEMSTONES (`gemstones`) |
| anchovy | PIZZA TOPPINGS (`pizza_toppings`) |
| Andes | MOUNTAIN RANGES (`mountain_ranges`) |
| anemometer | WEATHER INSTRUMENTS (`weather_instruments`) |
| anglerfish | DEEP SEA (`deep_sea`) |
| Angola | AFRICAN COUNTRIES (`african_countries`) |
| animator | CREATIVE JOBS (`creative_jobs`) |
| ankle | BODY PARTS (`body_parts`) |
| anole | LIZARDS (`lizards`) |
| ant | BUGS (`insects`) |
| antiseptic | FIRST AID (`first_aid`) |
| aperture | CAMERA SETTINGS (`photography_terms`) |
| aphid | BUGS (`insects`) |
| Aphrodite | GREEK GODS (`greek_gods`) |
| Apollo | GREEK GODS (`greek_gods`) |
| apricot | FRUIT TREES (`fruit_trees`) |
| apricot | FRUITS (`fruits`) |
| April | MONTHS (`months`) |
| aquarium | PET SUPPLIES (`pet_supplies`) |
| Aquarius | ZODIAC SIGNS (`zodiac_signs`) |
| Arabian | HORSE BREEDS (`horse_breeds`) |
| Arbys | FAST FOOD (`fast_food_chains`) |
| archery | OLYMPIC SPORTS (`olympic_sports`) |
| Archimedes | FAMOUS SCIENTISTS (`scientists`) |
| Ares | GREEK GODS (`greek_gods`) |
| Arizona | US STATES (`us_states`) |
| arm | BODY PARTS (`body_parts`) |
| army | MILITARY BRANCHES (`military_branches`) |
| arson | CRIMES (`crimes`) |
| art | SCHOOL SUBJECTS (`school_subjects`) |
| Artemis | GREEK GODS (`greek_gods`) |
| article | READING MATTER (`reading_material`) |
| artist | CREATIVE JOBS (`creative_jobs`) |
| assembly | SCHOOL EVENTS (`school_events`) |
| astrolabe | NAVIGATION TOOLS (`navigation_tools`) |
| Athena | GREEK GODS (`greek_gods`) |
| Audi | CAR BRANDS (`car_brands`) |
| August | MONTHS (`months`) |
| aurora | SPACE PHENOMENA (`space_phenomena`) |
| australorp | CHICKEN BREEDS (`farm_poultry_breeds`) |
| Autumn | SEASONS (`seasons`) |
| avalanche | NATURAL DISASTERS (`natural_disasters`) |
| avgolemono | WORLD SOUPS (`world_soups`) |
| azalea | FLOWERS (`flowers`) |
| Aztec | ANCIENT CIVILIZATIONS (`ancient_civilizations`) |
| babouche | TRADITIONAL FOOTWEAR (`world_hats_and_dress`) |
| baby | STAGES OF LIFE (`life_stages`) |
| Babylon | ANCIENT CIVILIZATIONS (`ancient_civilizations`) |
| back | DIRECTIONS (`directions`) |
| backgammon | BOARD GAMES (`board_games`) |
| backpack | CAMPING GEAR (`camping_gear`) |
| backstroke | SWIM STROKES (`swimming_strokes`) |
| bacon | BREAKFAST FOODS (`breakfast_foods`) |
| bacon | PIZZA TOPPINGS (`pizza_toppings`) |
| bacon | SANDWICH FILLINGS (`sandwich_fillings`) |
| baguette | BREAD TYPES (`bread_types`) |
| bake | COOKING METHODS (`cooking_methods`) |
| Balder | NORSE GODS (`norse_gods`) |
| Bali | ISLANDS (`islands`) |
| ballet | DANCE STYLES (`dance_styles`) |
| banana | FRUITS (`fruits`) |
| bandage | FIRST AID (`first_aid`) |
| bangle | JEWELRY (`jewelry`) |
| banjo | MUSICAL INSTRUMENTS (`musical_instruments`) |
| banjo | STRING INSTRUMENTS (`string_instruments`) |
| barbell | GYM EQUIPMENT (`gym_equipment`) |
| barge | BOATS AND SHIPS (`boats`) |
| barometer | WEATHER INSTRUMENTS (`weather_instruments`) |
| baroque | ART STYLES (`art_styles`) |
| Barqs | SODA BRANDS (`soda_brands`) |
| baseball cap | HATS (`hats`) |
| basil | COOKING HERBS (`herbs`) |
| basilisk | MYTHICAL MONSTERS (`mythical_monsters`) |
| basketball | TEAM SPORTS (`team_sports`) |
| bassoon | MUSICAL INSTRUMENTS (`musical_instruments`) |
| bassoon | WIND INSTRUMENTS (`wind_instruments`) |
| Batman | SUPERHEROES (`superheroes`) |
| battleship | BOARD GAMES (`board_games`) |
| bay | BODIES OF WATER (`bodies_of_water`) |
| beading | CRAFTS (`crafts`) |
| beagle | DOG BREEDS (`dog_breeds`) |
| beaker | LAB EQUIPMENT (`lab_equipment`) |
| beanie | HATS (`hats`) |
| beanie | WINTER CLOTHING (`winter_clothing`) |
| Bears | TEAM NAMES (`sports_teams`) |
| beaver | RODENTS (`rodents`) |
| bed | FURNITURE (`furniture`) |
| bee | BUGS (`insects`) |
| bee | STRIPED THINGS (`striped_things`) |
| beet | ROOT VEGETABLES (`root_vegetables`) |
| beetle | BUGS (`insects`) |
| beige | COLORS (`colors`) |
| bell | INVENTORS (`inventors`) |
| belt | ACCESSORIES (`accessories`) |
| belt | FASHION ACCESSORIES (`fashion_accessories`) |
| beret | HATS (`hats`) |
| beta | GREEK LETTERS (`greek_letters`) |
| biathlon | WINTER SPORTS (`winter_sports`) |
| bicep | MUSCLES (`muscles`) |
| bifocals | EYEWEAR (`eyewear`) |
| Big Ben | FAMOUS LANDMARKS (`famous_landmarks`) |
| bike | THINGS WITH WHEELS (`things_with_wheels`) |
| binder | OFFICE SUPPLIES (`office_supplies`) |
| biography | BOOK GENRES (`book_genres`) |
| biology | SCHOOL SUBJECTS (`school_subjects`) |
| biopsy | MEDICAL PROCEDURES (`medical_procedures`) |
| birch | TREES (`trees`) |
| biscotti | COOKIE TYPES (`cookie_types`) |
| bishop | RELIGIOUS LEADERS (`religious_leaders`) |
| bisque | SOUPS AND STEWS (`soups`) |
| Black Widow | SUPERHEROES (`superheroes`) |
| blackberry | BERRY VARIETIES (`berry_varieties`) |
| blackjack | CARD GAMES (`card_games`) |
| blacksmith | HISTORIC TRADES (`old_professions`) |
| blender | KITCHEN APPLIANCES (`kitchen_appliances`) |
| blizzard | NATURAL DISASTERS (`natural_disasters`) |
| blizzard | STORMS (`storms`) |
| blocks | TOYS (`toys`) |
| blood | BODY FLUIDS (`body_fluids`) |
| blood | RED THINGS (`red_things`) |
| blue | COLORS (`colors`) |
| blueberry | BERRIES (`berries`) |
| blueberry | BERRY VARIETIES (`berry_varieties`) |
| blues | MUSIC GENRES (`music_genres`) |
| blush | MAKEUP (`makeup`) |
| BMW | CAR BRANDS (`car_brands`) |
| bob | HAIRSTYLES (`hairstyles`) |
| bobsled | OLYMPIC SPORTS (`olympic_sports`) |
| bobsled | WINTER SPORTS (`winter_sports`) |
| book | READING MATTER (`reading_material`) |
| boom | SAILING TERMS (`sailing_terms`) |
| booster | ROCKET PARTS (`rocket_parts`) |
| borscht | SOUPS AND STEWS (`soups`) |
| Botswana | AFRICAN COUNTRIES (`african_countries`) |
| bowl | PET SUPPLIES (`pet_supplies`) |
| bowler | HATS (`hats`) |
| bowline | KNOTS (`knots`) |
| boxing | MARTIAL ARTS (`martial_arts`) |
| boxing | OLYMPIC SPORTS (`olympic_sports`) |
| bracelet | JEWELRY (`jewelry`) |
| braid | HAIRSTYLES (`hairstyles`) |
| braise | COOKING METHODS (`cooking_methods`) |
| brake | CAR PARTS (`car_parts`) |
| brass | METALS (`metals`) |
| breaststroke | SWIM STROKES (`swimming_strokes`) |
| bribery | CRIMES (`crimes`) |
| brick | BUILDING MATERIALS (`building_materials`) |
| brioche | BREAD TYPES (`bread_types`) |
| broccoli | VEGETABLES (`vegetables`) |
| broil | COOKING METHODS (`cooking_methods`) |
| bronze | METALS (`metals`) |
| bronze | SCULPTURE MATERIALS (`sculpture_materials`) |
| brooch | ACCESSORIES (`accessories`) |
| brooch | FASHION ACCESSORIES (`fashion_accessories`) |
| brooch | JEWELRY (`jewelry`) |
| Brooklyn | FAMOUS BRIDGES (`famous_bridges`) |
| broom | CLEANING TOOLS (`cleaning_tools`) |
| brownie | DESSERTS (`desserts`) |
| bruise | INJURIES (`injuries`) |
| brush | CLEANING TOOLS (`cleaning_tools`) |
| brush | PAINTING SUPPLIES (`painting_supplies`) |
| bubble | KITCHEN SOUNDS (`kitchen_sounds`) |
| Buddy | PET NAMES (`pet_names`) |
| bulb | LIGHT SOURCES (`light_sources`) |
| bulb | LIGHTING (`lighting`) |
| bulldog | DOG BREEDS (`dog_breeds`) |
| bullsnake | SNAKES (`snakes`) |
| bumpy | TEXTURES (`textures`) |
| bun | HAIRSTYLES (`hairstyles`) |
| burger | DRIVE THRU (`fast_food_items`) |
| Burger King | FAST FOOD (`fast_food_chains`) |
| burner | LAB EQUIPMENT (`lab_equipment`) |
| burp | BODY SOUNDS (`body_sounds`) |
| burrow | ANIMAL HOMES (`animal_homes`) |
| bus | VEHICLES (`vehicles`) |
| Busch Gardens | THEME PARKS (`theme_parks`) |
| butte | LANDFORMS (`landforms`) |
| butter | COOKING FATS (`cooking_fats`) |
| butter | DAIRY PRODUCTS (`dairy_products`) |
| butterfly | BUGS (`insects`) |
| butterfly | SWIM STROKES (`swimming_strokes`) |
| cabbage | VEGETABLES (`vegetables`) |
| cactus | HOUSEPLANTS (`houseplants`) |
| cactus | WILD WEST (`wild_west`) |
| caesar | SALADS (`salads`) |
| cafe | PLACES TO EAT (`places_to_eat`) |
| cake | DESSERTS (`desserts`) |
| calcite | MINERALS (`minerals`) |
| camera | GADGETS (`gadgets`) |
| canal | BODIES OF WATER (`bodies_of_water`) |
| cancer | ZODIAC SIGNS (`zodiac_signs`) |
| candle | LIGHT SOURCES (`light_sources`) |
| candle | LIGHTING (`lighting`) |
| candy cane | STRIPED THINGS (`striped_things`) |
| cannoli | ITALIAN DISHES (`italian_dishes`) |
| canoe | BOATS AND SHIPS (`boats`) |
| canvas | ART SUPPLIES (`art_supplies`) |
| canvas | PAINTING SUPPLIES (`painting_supplies`) |
| canyon | LANDFORMS (`landforms`) |
| cap | HATS (`hats`) |
| cappuccino | COFFEE DRINKS (`coffee_drinks`) |
| capybara | RODENTS (`rodents`) |
| car | THINGS WITH WHEELS (`things_with_wheels`) |
| car | VEHICLES (`vehicles`) |
| caracal | WILD CATS (`wild_cats`) |
| carrot | ROOT VEGETABLES (`root_vegetables`) |
| carrot | VEGETABLES (`vegetables`) |
| cartoon | TV GENRES (`tv_genres`) |
| Cassiopeia | CONSTELLATIONS (`constellations`) |
| cat | PETS (`pets`) |
| cauliflower | VEGETABLES (`vegetables`) |
| cedar | TREES (`trees`) |
| celery | VEGETABLES (`vegetables`) |
| cello | MUSICAL INSTRUMENTS (`musical_instruments`) |
| cello | STRING INSTRUMENTS (`string_instruments`) |
| centaur | MYTHICAL CREATURES (`fantasy_creatures`) |
| centrifuge | LAB EQUIPMENT (`lab_equipment`) |
| cereal | BREAKFAST FOODS (`breakfast_foods`) |
| chai | HOT DRINKS (`hot_drinks`) |
| chain | JEWELRY (`jewelry`) |
| chair | FURNITURE (`furniture`) |
| challah | BREAD TYPES (`bread_types`) |
| chameleon | LIZARDS (`lizards`) |
| chanterelle | MUSHROOM TYPES (`mushroom_types`) |
| chapel | PLACES OF WORSHIP (`places_of_worship`) |
| chaplain | RELIGIOUS LEADERS (`religious_leaders`) |
| charm | JEWELRY (`jewelry`) |
| chart | NAVIGATION TOOLS (`navigation_tools`) |
| checkered | PATTERNS (`patterns`) |
| checkers | BOARD GAMES (`board_games`) |
| Cheerios | CEREAL BRANDS (`cereal_brands`) |
| cheese | DAIRY PRODUCTS (`dairy_products`) |
| cheese | PIZZA TOPPINGS (`pizza_toppings`) |
| cheese | SANDWICH FILLINGS (`sandwich_fillings`) |
| cheetah | WILD CATS (`wild_cats`) |
| chemistry | SCHOOL SUBJECTS (`school_subjects`) |
| cherry | BERRIES (`berries`) |
| cherry | FRUIT TREES (`fruit_trees`) |
| cherry | RED THINGS (`red_things`) |
| cherry | TREES (`trees`) |
| chess | BOARD GAMES (`board_games`) |
| chi | GREEK LETTERS (`greek_letters`) |
| chicken | FARM ANIMALS (`farm_animals`) |
| chicken noodle | SOUPS AND STEWS (`soups`) |
| chiffon | FABRIC TYPES (`fabric_types`) |
| child | STAGES OF LIFE (`life_stages`) |
| child | YOGA POSES (`yoga_poses`) |
| chill | COLD THINGS (`cold_things`) |
| chills | SYMPTOMS (`symptoms`) |
| chimichurri | SAUCES (`sauces`) |
| China | ASIAN COUNTRIES (`asian_countries`) |
| chinchilla | RODENTS (`rodents`) |
| chips | SNACK FOODS (`snack_foods`) |
| chirp | ANIMAL SOUNDS (`animal_sounds`) |
| chocolate | CANDY (`candy`) |
| chocolate | ICE CREAM (`ice_cream_flavors`) |
| chocolate chip | COOKIE TYPES (`cookie_types`) |
| chop | KITCHEN SOUNDS (`kitchen_sounds`) |
| chowder | SOUPS AND STEWS (`soups`) |
| Christmas | HOLIDAYS (`holidays`) |
| Christmas | RELIGIOUS HOLIDAYS (`religious_holidays`) |
| church | PLACES OF WORSHIP (`places_of_worship`) |
| ciabatta | BREAD TYPES (`bread_types`) |
| cider | HOT DRINKS (`hot_drinks`) |
| cilantro | COOKING HERBS (`herbs`) |
| circle | SHAPES (`shapes`) |
| circulatory | BODY SYSTEMS (`body_systems`) |
| citron | CITRUS FRUITS (`citrus_fruits`) |
| clarinet | WIND INSTRUMENTS (`wind_instruments`) |
| clasp | JEWELRY SUPPLIES (`jewelry_making`) |
| classical | MUSIC GENRES (`music_genres`) |
| clatter | KITCHEN SOUNDS (`kitchen_sounds`) |
| clay | SCULPTURE MATERIALS (`sculpture_materials`) |
| clementine | CITRUS FRUITS (`citrus_fruits`) |
| cliff | LANDFORMS (`landforms`) |
| Clinton | US PRESIDENTS (`us_presidents`) |
| clove hitch | KNOTS (`knots`) |
| clover | WILD PLANTS (`wild_plants`) |
| clue | BOARD GAMES (`board_games`) |
| clutch | CAR PARTS (`car_parts`) |
| clydesdale | HORSE BREEDS (`horse_breeds`) |
| coast guard | MILITARY BRANCHES (`military_branches`) |
| cobb | SALADS (`salads`) |
| cobra | YOGA POSES (`yoga_poses`) |
| cockatoo | TROPICAL BIRDS (`tropical_birds`) |
| cocoa | HOT DRINKS (`hot_drinks`) |
| coffee | HOT DRINKS (`hot_drinks`) |
| coin | ROUND THINGS (`round_things`) |
| colander | KITCHEN TOOLS (`kitchen_tools`) |
| colander | THINGS WITH HOLES (`things_with_holes`) |
| coleslaw | SALADS (`salads`) |
| collie | DOG BREEDS (`dog_breeds`) |
| colonel | MILITARY RANKS (`military_ranks`) |
| colony | ANIMAL GROUPS (`animal_groups`) |
| Colorado | RIVERS (`rivers`) |
| Colosseum | FAMOUS LANDMARKS (`famous_landmarks`) |
| comedy | MOVIE GENRES (`movie_genres`) |
| comma | PUNCTUATION MARKS (`punctuation`) |
| compass | CAMPING GEAR (`camping_gear`) |
| compass | INVENTIONS (`inventions`) |
| compass | NAVIGATION TOOLS (`navigation_tools`) |
| concrete | BUILDING MATERIALS (`building_materials`) |
| cone | SHAPES (`shapes`) |
| conjunction | PARTS OF SPEECH (`parts_of_speech`) |
| contacts | EYEWEAR (`eyewear`) |
| contract | LEGAL DOCUMENTS (`legal_documents`) |
| cookie | DESSERTS (`desserts`) |
| cooler | CAMPING GEAR (`camping_gear`) |
| cooper | HISTORIC TRADES (`old_professions`) |
| copper | METALS (`metals`) |
| copy | COMPUTER ACTIONS (`computer_actions`) |
| corduroy | FABRICS (`fabrics`) |
| corgi | DOG BREEDS (`dog_breeds`) |
| corn | VEGETABLES (`vegetables`) |
| cornbread | BREAD TYPES (`bread_types`) |
| corporal | MILITARY RANKS (`military_ranks`) |
| cortado | COFFEE DRINKS (`coffee_drinks`) |
| cosmopolitan | COCKTAILS (`cocktails`) |
| cotton | FABRIC TYPES (`fabric_types`) |
| cotton | FABRICS (`fabrics`) |
| cotton candy | AMUSEMENT PARK (`amusement_park`) |
| cotton candy | STREET FOOD (`street_food`) |
| cougar | WILD CATS (`wild_cats`) |
| cough | SYMPTOMS (`symptoms`) |
| country | MUSIC GENRES (`music_genres`) |
| cow | FARM ANIMALS (`farm_animals`) |
| cowboy | WILD WEST (`wild_west`) |
| crab | OCEAN ANIMALS (`ocean_animals`) |
| crab | SEAFOOD (`seafood`) |
| cranberry | BERRIES (`berries`) |
| crazy eights | CARD GAMES (`card_games`) |
| crepe | STREET FOOD (`street_food`) |
| Crete | ISLANDS (`islands`) |
| cricket | BUGS (`insects`) |
| crimson | COLORS (`colors`) |
| crocodile | REPTILES (`reptiles`) |
| crookneck | MELONS & SQUASH (`melons_and_squash`) |
| croqueta | SPANISH DISHES (`spanish_dishes`) |
| crossword | PUZZLES (`puzzle_types`) |
| crow | BIRDS (`birds`) |
| Cuba | ISLAND NATIONS (`island_nations`) |
| Cuba | ISLANDS (`islands`) |
| cube | SHAPES (`shapes`) |
| cubism | ART STYLES (`art_styles`) |
| cufflinks | FASHION ACCESSORIES (`fashion_accessories`) |
| Curie | FAMOUS SCIENTISTS (`scientists`) |
| curling | OLYMPIC SPORTS (`olympic_sports`) |
| curling | WINTER SPORTS (`winter_sports`) |
| cut | INJURIES (`injuries`) |
| cyclone | NATURAL DISASTERS (`natural_disasters`) |
| cyclone | STORMS (`storms`) |
| Cygnus | CONSTELLATIONS (`constellations`) |
| cylinder | SHAPES (`shapes`) |
| dachshund | DOG BREEDS (`dog_breeds`) |
| dahlia | FLOWERS (`flowers`) |
| Daisy | FLOWERS (`flowers`) |
| dance | ART FORMS (`art_forms`) |
| dancer | CREATIVE JOBS (`creative_jobs`) |
| dandelion | WILD PLANTS (`wild_plants`) |
| Darwin | FAMOUS SCIENTISTS (`scientists`) |
| deck | SKATEBOARDING WORDS (`skateboarding`) |
| delete | COMPUTER ACTIONS (`computer_actions`) |
| denim | FABRIC TYPES (`fabric_types`) |
| denim | FABRICS (`fabrics`) |
| desert | BIOMES (`biomes`) |
| desk | FURNITURE (`furniture`) |
| detour | TRAFFIC SIGNS (`traffic_signs`) |
| Detroit | PIZZA STYLES (`pizza_styles`) |
| digestive | BODY SYSTEMS (`body_systems`) |
| diner | PLACES TO EAT (`places_to_eat`) |
| dinosaur | EXTINCT ANIMALS (`extinct_animals`) |
| dip | DANCE MOVES (`dance_moves`) |
| disco | MUSIC GENRES (`music_genres`) |
| dishwasher | KITCHEN APPLIANCES (`kitchen_appliances`) |
| diving | OLYMPIC SPORTS (`olympic_sports`) |
| diving | WATER SPORTS (`water_sports`) |
| Diwali | RELIGIOUS HOLIDAYS (`religious_holidays`) |
| dodo | EXTINCT ANIMALS (`extinct_animals`) |
| dog | PETS (`pets`) |
| doll | TOYS (`toys`) |
| dolphin | OCEAN ANIMALS (`ocean_animals`) |
| dolphin | SEA MAMMALS (`sea_mammals`) |
| donut | DESSERTS (`desserts`) |
| donut | ROUND THINGS (`round_things`) |
| donut | THINGS WITH HOLES (`things_with_holes`) |
| doorbell | RINGING THINGS (`things_that_ring`) |
| dove | MAGIC PROPS (`magic_tricks`) |
| down | DIRECTIONS (`directions`) |
| downward dog | YOGA POSES (`yoga_poses`) |
| Draco | CONSTELLATIONS (`constellations`) |
| dragon | MYTHICAL CREATURES (`fantasy_creatures`) |
| dragonfly | BUGS (`insects`) |
| drawing | ART FORMS (`art_forms`) |
| dresser | FURNITURE (`furniture`) |
| Dreyers | FROZEN TREATS (`frozen_treat_brands`) |
| drone | BEEKEEPING THINGS (`beekeeping`) |
| drone | GADGETS (`gadgets`) |
| drought | NATURAL DISASTERS (`natural_disasters`) |
| drum | MUSICAL INSTRUMENTS (`musical_instruments`) |
| drywaller | BUILDING TRADES (`building_trades`) |
| duke | UNIVERSITIES (`universities`) |
| duster | CLEANING TOOLS (`cleaning_tools`) |
| dustpan | CLEANING TOOLS (`cleaning_tools`) |
| dwarf | MAGICAL BEINGS (`magic_creatures`) |
| eagle | BIRDS (`birds`) |
| eagle | BIRDS OF PREY (`birds_of_prey`) |
| Eagles | TEAM NAMES (`sports_teams`) |
| earring | JEWELRY (`jewelry`) |
| Earth | PLANETS (`planets`) |
| earthquake | NATURAL DISASTERS (`natural_disasters`) |
| easel | PAINTING SUPPLIES (`painting_supplies`) |
| east | DIRECTIONS (`directions`) |
| Easter | HOLIDAYS (`holidays`) |
| Easter | RELIGIOUS HOLIDAYS (`religious_holidays`) |
| eclair | DESSERTS (`desserts`) |
| eclipse | SPACE PHENOMENA (`space_phenomena`) |
| Edison | INVENTORS (`inventors`) |
| Edys | FROZEN TREATS (`frozen_treat_brands`) |
| eel | SEAFOOD (`seafood`) |
| egg | BREAKFAST FOODS (`breakfast_foods`) |
| eggplant | VEGETABLES (`vegetables`) |
| Egypt | AFRICAN COUNTRIES (`african_countries`) |
| Eiffel Tower | FAMOUS LANDMARKS (`famous_landmarks`) |
| Einstein | FAMOUS SCIENTISTS (`scientists`) |
| elbow | BODY PARTS (`body_parts`) |
| elephant | ZOO ANIMALS (`zoo_animals`) |
| elliptical | GYM EQUIPMENT (`gym_equipment`) |
| elm | TREES (`trees`) |
| emerald | GEMSTONES (`gemstones`) |
| Emerald City | CITY NICKNAMES (`city_nicknames`) |
| enamel | KINDS OF PAINT (`paint_types`) |
| endocrine | BODY SYSTEMS (`body_systems`) |
| engine | ROCKET PARTS (`rocket_parts`) |
| English | LANGUAGES (`languages`) |
| English | SCHOOL SUBJECTS (`school_subjects`) |
| eraser | OFFICE SUPPLIES (`office_supplies`) |
| eraser | SCHOOL SUPPLIES (`school_supplies`) |
| escalivada | SPANISH DISHES (`spanish_dishes`) |
| espresso | COFFEE DRINKS (`coffee_drinks`) |
| estuary | BODIES OF WATER (`bodies_of_water`) |
| excuse me | MANNERS WORDS (`manners`) |
| exposure | CAMERA SETTINGS (`photography_terms`) |
| eyeliner | MAKEUP (`makeup`) |
| factory | INDUSTRIAL AGE (`industrial_revolution`) |
| fairy | MAGICAL BEINGS (`magic_creatures`) |
| falcon | BIRDS (`birds`) |
| falcon | BIRDS OF PREY (`birds_of_prey`) |
| fall | SEASONS (`seasons`) |
| farfalle | PASTA SHAPES (`pasta_shapes`) |
| fatigue | SYMPTOMS (`symptoms`) |
| fedora | HATS (`hats`) |
| feldspar | MINERALS (`minerals`) |
| femur | BONES (`bones`) |
| fencing | OLYMPIC SPORTS (`olympic_sports`) |
| Fern | HOUSEPLANTS (`houseplants`) |
| Fern | WILD PLANTS (`wild_plants`) |
| fever | SYMPTOMS (`symptoms`) |
| field trip | SCHOOL EVENTS (`school_events`) |
| figure eight | KNOTS (`knots`) |
| Fiji | ISLANDS (`islands`) |
| finch | SONGBIRDS (`songbirds`) |
| finger | BODY PARTS (`body_parts`) |
| fire | LIGHT SOURCES (`light_sources`) |
| firefly | BUGS (`insects`) |
| flag | STRIPED THINGS (`striped_things`) |
| flamingo | BIRDS (`birds`) |
| flannel | FABRIC TYPES (`fabric_types`) |
| flash | CAMERA SETTINGS (`photography_terms`) |
| flash | SUPERHEROES (`superheroes`) |
| flashlight | CAMPING GEAR (`camping_gear`) |
| flat white | COFFEE DRINKS (`coffee_drinks`) |
| flatbread | BREAD TYPES (`bread_types`) |
| flood | NATURAL DISASTERS (`natural_disasters`) |
| floss | DANCE MOVES (`dance_moves`) |
| floss | HYGIENE THINGS (`hygiene`) |
| flush | POKER HANDS (`poker_hands`) |
| flute | MUSICAL INSTRUMENTS (`musical_instruments`) |
| flute | WIND INSTRUMENTS (`wind_instruments`) |
| folk | MUSIC GENRES (`music_genres`) |
| football | TEAM SPORTS (`team_sports`) |
| fork | KITCHEN TOOLS (`kitchen_tools`) |
| forward | DIRECTIONS (`directions`) |
| foxglove | POISONOUS PLANTS (`poisonous_plants`) |
| foxtrot | DANCE STYLES (`dance_styles`) |
| fracture | INJURIES (`injuries`) |
| fraud | CRIMES (`crimes`) |
| freestyle | SWIM STROKES (`swimming_strokes`) |
| French | LANGUAGES (`languages`) |
| Freya | NORSE GODS (`norse_gods`) |
| Frigg | NORSE GODS (`norse_gods`) |
| Frontier | AIRLINES (`airlines`) |
| frost | COLD THINGS (`cold_things`) |
| frown | FACIAL EXPRESSIONS (`facial_expressions`) |
| full house | POKER HANDS (`poker_hands`) |
| funk | MUSIC GENRES (`music_genres`) |
| fur | SOFT THINGS (`soft_things`) |
| furnace | HOT THINGS (`hot_things`) |
| futon | FURNITURE (`furniture`) |
| gale | STORMS (`storms`) |
| Galileo | FAMOUS SCIENTISTS (`scientists`) |
| galosh | FOOTWEAR (`footwear`) |
| gamma | GREEK LETTERS (`greek_letters`) |
| garden | SALADS (`salads`) |
| garnet | GEMSTONES (`gemstones`) |
| gauze | FIRST AID (`first_aid`) |
| gazpacho | SOUPS AND STEWS (`soups`) |
| gecko | LIZARDS (`lizards`) |
| gecko | REPTILES (`reptiles`) |
| gelato | ITALIAN DISHES (`italian_dishes`) |
| Gemini | ZODIAC SIGNS (`zodiac_signs`) |
| geometry | SCHOOL SUBJECTS (`school_subjects`) |
| gerbil | RODENTS (`rodents`) |
| German | LANGUAGES (`languages`) |
| Ghana | AFRICAN COUNTRIES (`african_countries`) |
| ghee | COOKING FATS (`cooking_fats`) |
| ghost | SCARY CREATURES (`monsters`) |
| gingerbread | COOKIE TYPES (`cookie_types`) |
| Giovanni | ITALIAN NAMES (`italian_names`) |
| giraffe | ZOO ANIMALS (`zoo_animals`) |
| glasses | EYEWEAR (`eyewear`) |
| globe | ROUND THINGS (`round_things`) |
| gloves | FASHION ACCESSORIES (`fashion_accessories`) |
| glue | STICKY THINGS (`sticky_things`) |
| glute | MUSCLES (`muscles`) |
| glyptodon | PREHISTORIC ANIMALS (`extinct_and_prehistoric`) |
| goat | FARM ANIMALS (`farm_animals`) |
| goggles | EYEWEAR (`eyewear`) |
| gold | CHEMICAL ELEMENTS (`elements`) |
| gold | METALS (`metals`) |
| Golden Gate | FAMOUS BRIDGES (`famous_bridges`) |
| goldfish | PETS (`pets`) |
| goose | BIRDS (`birds`) |
| gopher | RODENTS (`rodents`) |
| gorilla | ZOO ANIMALS (`zoo_animals`) |
| gospel | MUSIC GENRES (`music_genres`) |
| gps | NAVIGATION TOOLS (`navigation_tools`) |
| graduation | SCHOOL EVENTS (`school_events`) |
| Grammy | AWARDS (`awards`) |
| granite | SCULPTURE MATERIALS (`sculpture_materials`) |
| Grant | US PRESIDENTS (`us_presidents`) |
| grape | FRUITS (`fruits`) |
| grapefruit | CITRUS FRUITS (`citrus_fruits`) |
| grassland | BIOMES (`biomes`) |
| grater | KITCHEN TOOLS (`kitchen_tools`) |
| gravy | SAUCES (`sauces`) |
| greek | SALADS (`salads`) |
| greyhound | DOG BREEDS (`dog_breeds`) |
| grill | COOKING METHODS (`cooking_methods`) |
| grimace | FACIAL EXPRESSIONS (`facial_expressions`) |
| growl | ANIMAL SOUNDS (`animal_sounds`) |
| guava | TROPICAL FRUITS (`tropical_fruits`) |
| Guggenheim | FAMOUS MUSEUMS (`famous_museums`) |
| guinea pig | PETS (`pets`) |
| guinea pig | RODENTS (`rodents`) |
| guitar | MUSICAL INSTRUMENTS (`musical_instruments`) |
| guitar | STRING INSTRUMENTS (`string_instruments`) |
| gumbo | SOUPS AND STEWS (`soups`) |
| gymnastics | OLYMPIC SPORTS (`olympic_sports`) |
| gypsum | MINERALS (`minerals`) |
| Halloween | HOLIDAYS (`holidays`) |
| ham | SANDWICH FILLINGS (`sandwich_fillings`) |
| Hamlet | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| hamster | PETS (`pets`) |
| hamster | RODENTS (`rodents`) |
| hamstring | MUSCLES (`muscles`) |
| handball | TEAM SPORTS (`team_sports`) |
| hanger | WARDROBE (`wardrobe`) |
| harira | WORLD SOUPS (`world_soups`) |
| harp | MUSICAL INSTRUMENTS (`musical_instruments`) |
| harp | STRING INSTRUMENTS (`string_instruments`) |
| harrier | BIRDS OF PREY (`birds_of_prey`) |
| Harvard | UNIVERSITIES (`universities`) |
| hat | ACCESSORIES (`accessories`) |
| hat | CLOTHING ITEMS (`clothing_items`) |
| hats | ACCESSORIES (`accessories`) |
| Havasu | WATERFALLS (`waterfalls`) |
| Hawaii | ISLANDS (`islands`) |
| hawk | BIRDS (`birds`) |
| hawk | BIRDS OF PREY (`birds_of_prey`) |
| Hawking | FAMOUS SCIENTISTS (`scientists`) |
| headlight | LIGHT SOURCES (`light_sources`) |
| hearts | CARD GAMES (`card_games`) |
| heel | SHOE PARTS (`shoe_parts`) |
| Heimdall | NORSE GODS (`norse_gods`) |
| helium | CHEMICAL ELEMENTS (`elements`) |
| helmet | HATS (`hats`) |
| hemlock | POISONOUS PLANTS (`poisonous_plants`) |
| Hera | GREEK GODS (`greek_gods`) |
| Hercules | MYTHOLOGICAL HEROES (`greek_heroes`) |
| herd | ANIMAL GROUPS (`animal_groups`) |
| Hermes | GREEK GODS (`greek_gods`) |
| Hermitage | FAMOUS MUSEUMS (`famous_museums`) |
| hexagon | SHAPES (`shapes`) |
| hiccup | BODY SOUNDS (`body_sounds`) |
| highlighter | OFFICE SUPPLIES (`office_supplies`) |
| Himalayas | MOUNTAIN RANGES (`mountain_ranges`) |
| hip hop | DANCE STYLES (`dance_styles`) |
| history | SCHOOL SUBJECTS (`school_subjects`) |
| hive | ANIMAL HOMES (`animal_homes`) |
| hive | BEEKEEPING THINGS (`beekeeping`) |
| hockey | TEAM SPORTS (`team_sports`) |
| hoe | GARDEN TOOLS (`garden_tools`) |
| hollandaise | SAUCES (`sauces`) |
| Honda | CAR BRANDS (`car_brands`) |
| honey | BEEKEEPING THINGS (`beekeeping`) |
| honey | STICKY THINGS (`sticky_things`) |
| honk | CITY SOUNDS (`city_sounds`) |
| hoop | ROUND THINGS (`round_things`) |
| horror | BOOK GENRES (`book_genres`) |
| horror | MOVIE GENRES (`movie_genres`) |
| horse | FARM ANIMALS (`farm_animals`) |
| horse racing | RACING SPORTS (`racing_sports`) |
| hose | GARDEN TOOLS (`garden_tools`) |
| Hulk | SUPERHEROES (`superheroes`) |
| hurdles | TRACK EVENTS (`track_events`) |
| hurricane | NATURAL DISASTERS (`natural_disasters`) |
| hurricane | STORMS (`storms`) |
| husky | DOG BREEDS (`dog_breeds`) |
| hygrometer | WEATHER INSTRUMENTS (`weather_instruments`) |
| hyphen | PUNCTUATION MARKS (`punctuation`) |
| ice cream | DAIRY PRODUCTS (`dairy_products`) |
| ice cream | DESSERTS (`desserts`) |
| Iceland | ISLAND NATIONS (`island_nations`) |
| Iceland | ISLANDS (`islands`) |
| iguana | LIZARDS (`lizards`) |
| iguana | REPTILES (`reptiles`) |
| Iguazu | WATERFALLS (`waterfalls`) |
| imam | RELIGIOUS LEADERS (`religious_leaders`) |
| immune | BODY SYSTEMS (`body_systems`) |
| impressionism | ART STYLES (`art_styles`) |
| Inca | ANCIENT CIVILIZATIONS (`ancient_civilizations`) |
| indigo | COLORS (`colors`) |
| infant | STAGES OF LIFE (`life_stages`) |
| inlet | BODIES OF WATER (`bodies_of_water`) |
| interjection | PARTS OF SPEECH (`parts_of_speech`) |
| iota | GREEK LETTERS (`greek_letters`) |
| iris | FLOWERS (`flowers`) |
| island | LANDFORMS (`landforms`) |
| iso | CAMERA SETTINGS (`photography_terms`) |
| isthmus | LANDFORMS (`landforms`) |
| jacket | CLOTHING ITEMS (`clothing_items`) |
| jackfruit | TROPICAL FRUITS (`tropical_fruits`) |
| Jackson | US PRESIDENTS (`us_presidents`) |
| jade | GEMSTONES (`gemstones`) |
| jaguar | JUNGLE ANIMALS (`jungle_animals`) |
| jaguar | WILD CATS (`wild_cats`) |
| jaguarundi | SMALL CATS (`wild_cats_small`) |
| Jamaica | ISLANDS (`islands`) |
| Japan | ASIAN COUNTRIES (`asian_countries`) |
| Jasmine | FLOWERS (`flowers`) |
| jazz | MUSIC GENRES (`music_genres`) |
| Jeep | VEHICLES (`vehicles`) |
| jerky | SNACK FOODS (`snack_foods`) |
| jibe | SAILING TERMS (`sailing_terms`) |
| jigsaw | PUZZLES (`puzzle_types`) |
| judo | MARTIAL ARTS (`martial_arts`) |
| judo | OLYMPIC SPORTS (`olympic_sports`) |
| juicer | KITCHEN APPLIANCES (`kitchen_appliances`) |
| June | MONTHS (`months`) |
| Jupiter | PLANETS (`planets`) |
| Jupiter | ROMAN GODS (`roman_gods`) |
| jutti | TRADITIONAL FOOTWEAR (`world_hats_and_dress`) |
| kangaroo | MARSUPIALS (`marsupials`) |
| karate | MARTIAL ARTS (`martial_arts`) |
| kayaking | WATER SPORTS (`water_sports`) |
| kebab | STREET FOOD (`street_food`) |
| kefir | DAIRY PRODUCTS (`dairy_products`) |
| kefir | PICKLED FOODS (`fermented_foods`) |
| Kennedy | US PRESIDENTS (`us_presidents`) |
| kennel | ANIMAL HOMES (`animal_homes`) |
| Kenya | AFRICAN COUNTRIES (`african_countries`) |
| Kepler | FAMOUS SCIENTISTS (`scientists`) |
| ketchup | CONDIMENTS (`condiments`) |
| kettle | KITCHEN APPLIANCES (`kitchen_appliances`) |
| kettlebell | GYM EQUIPMENT (`gym_equipment`) |
| kimchi | PICKLED FOODS (`fermented_foods`) |
| King Lear | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| knife | CUTTING TOOLS (`cutting_tools`) |
| knife | KITCHEN TOOLS (`kitchen_tools`) |
| knitting | CRAFTS (`crafts`) |
| koala | MARSUPIALS (`marsupials`) |
| koala | ZOO ANIMALS (`zoo_animals`) |
| kombucha | PICKLED FOODS (`fermented_foods`) |
| Korea | ASIAN COUNTRIES (`asian_countries`) |
| kraken | MYTHICAL MONSTERS (`mythical_monsters`) |
| kraken | SEA LEGENDS (`sea_myths`) |
| kumquat | CITRUS FRUITS (`citrus_fruits`) |
| kung fu | MARTIAL ARTS (`martial_arts`) |
| labrador | DOG BREEDS (`dog_breeds`) |
| lace | SHOE PARTS (`shoe_parts`) |
| ladle | KITCHEN TOOLS (`kitchen_tools`) |
| ladybug | BUGS (`insects`) |
| lagoon | BODIES OF WATER (`bodies_of_water`) |
| lake | BODIES OF WATER (`bodies_of_water`) |
| Lakers | TEAM NAMES (`sports_teams`) |
| lamp | LIGHT SOURCES (`light_sources`) |
| lamp | LIGHTING (`lighting`) |
| lantern | CAMPING GEAR (`camping_gear`) |
| lantern | LIGHT SOURCES (`light_sources`) |
| laptop | GADGETS (`gadgets`) |
| lard | COOKING FATS (`cooking_fats`) |
| laser | LIGHT SOURCES (`light_sources`) |
| latte | COFFEE DRINKS (`coffee_drinks`) |
| latte | HOT DRINKS (`hot_drinks`) |
| launch pad | ROCKET PARTS (`rocket_parts`) |
| leaf | PLANT PARTS (`plant_parts`) |
| left | DIRECTIONS (`directions`) |
| leg | BODY PARTS (`body_parts`) |
| lemon | CITRUS FRUITS (`citrus_fruits`) |
| Leo | ZODIAC SIGNS (`zodiac_signs`) |
| leopard | WILD CATS (`wild_cats`) |
| lettuce | SANDWICH FILLINGS (`sandwich_fillings`) |
| lettuce | VEGETABLES (`vegetables`) |
| leviathan | SEA LEGENDS (`sea_myths`) |
| Lexus | CAR BRANDS (`car_brands`) |
| Life | BOARD GAMES (`board_games`) |
| lilac | FLOWERS (`flowers`) |
| Lily | FLOWERS (`flowers`) |
| lime | CITRUS FRUITS (`citrus_fruits`) |
| lime | GREEN THINGS (`green_things`) |
| Lincoln | US PRESIDENTS (`us_presidents`) |
| linen | FABRIC TYPES (`fabric_types`) |
| linen | FABRICS (`fabrics`) |
| linguine | PASTA SHAPES (`pasta_shapes`) |
| lion | WILD CATS (`wild_cats`) |
| lipstick | MAKEUP (`makeup`) |
| lizard | REPTILES (`reptiles`) |
| lizards | REPTILES (`reptiles`) |
| loafer | FOOTWEAR (`footwear`) |
| lobster | SEAFOOD (`seafood`) |
| locket | JEWELRY (`jewelry`) |
| Loki | NORSE GODS (`norse_gods`) |
| lollipop | CANDY (`candy`) |
| lotus | YOGA POSES (`yoga_poses`) |
| Louvre | FAMOUS MUSEUMS (`famous_museums`) |
| loveseat | FURNITURE (`furniture`) |
| Luca | ITALIAN NAMES (`italian_names`) |
| luge | WINTER SPORTS (`winter_sports`) |
| lychee | TROPICAL FRUITS (`tropical_fruits`) |
| lymph | BODY FLUIDS (`body_fluids`) |
| lynx | WILD CATS (`wild_cats`) |
| Lyra | CONSTELLATIONS (`constellations`) |
| macaroon | COOKIE TYPES (`cookie_types`) |
| macaw | TROPICAL BIRDS (`tropical_birds`) |
| Macbeth | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| macchiato | COFFEE DRINKS (`coffee_drinks`) |
| macrame | CRAFTS (`crafts`) |
| macro | PHOTO SUBJECTS (`photography_styles`) |
| magenta | COLORS (`colors`) |
| maine coon | CAT BREEDS (`cat_breeds`) |
| Malta | ISLAND NATIONS (`island_nations`) |
| Malta | ISLANDS (`islands`) |
| mammoth | EXTINCT ANIMALS (`extinct_animals`) |
| manatee | SEA MAMMALS (`sea_mammals`) |
| mancala | BOARD GAMES (`board_games`) |
| mandarin | CITRUS FRUITS (`citrus_fruits`) |
| mandolin | STRING INSTRUMENTS (`string_instruments`) |
| mango | FRUIT TREES (`fruit_trees`) |
| mango | FRUITS (`fruits`) |
| mango | TROPICAL FRUITS (`tropical_fruits`) |
| manhattan | COCKTAILS (`cocktails`) |
| map | CAMPING GEAR (`camping_gear`) |
| map | NAVIGATION TOOLS (`navigation_tools`) |
| maple | TREES (`trees`) |
| Marco | ITALIAN NAMES (`italian_names`) |
| margarita | COCKTAILS (`cocktails`) |
| marines | MILITARY BRANCHES (`military_branches`) |
| marker | GAME PIECES (`board_game_pieces`) |
| marker | OFFICE SUPPLIES (`office_supplies`) |
| marker | SCHOOL SUPPLIES (`school_supplies`) |
| Mars | PLANETS (`planets`) |
| Mars | ROMAN GODS (`roman_gods`) |
| martini | COCKTAILS (`cocktails`) |
| mascara | MAKEUP (`makeup`) |
| math | SCHOOL SUBJECTS (`school_subjects`) |
| Matteo | ITALIAN NAMES (`italian_names`) |
| Maya | ANCIENT CIVILIZATIONS (`ancient_civilizations`) |
| mayo | CONDIMENTS (`condiments`) |
| McDonalds | FAST FOOD (`fast_food_chains`) |
| meeple | GAME PIECES (`board_game_pieces`) |
| meow | ANIMAL SOUNDS (`animal_sounds`) |
| Merlot | GRAPE VARIETIES (`grape_varieties`) |
| mermaid | MYTHICAL CREATURES (`fantasy_creatures`) |
| mesa | LANDFORMS (`landforms`) |
| Met | FAMOUS MUSEUMS (`famous_museums`) |
| Miami | US CITIES (`us_cities`) |
| mica | MINERALS (`minerals`) |
| microwave | KITCHEN APPLIANCES (`kitchen_appliances`) |
| milk | DAIRY PRODUCTS (`dairy_products`) |
| minestrone | SOUPS AND STEWS (`soups`) |
| mirror | CAR PARTS (`car_parts`) |
| miso | PICKLED FOODS (`fermented_foods`) |
| miso | SOUPS AND STEWS (`soups`) |
| MIT | UNIVERSITIES (`universities`) |
| MLB | SPORTS LEAGUES (`sports_leagues`) |
| moccasin | FOOTWEAR (`footwear`) |
| mocha | COFFEE DRINKS (`coffee_drinks`) |
| mojito | COCKTAILS (`cocktails`) |
| MoMA | FAMOUS MUSEUMS (`famous_museums`) |
| monk | RELIGIOUS LEADERS (`religious_leaders`) |
| monkey | JUNGLE ANIMALS (`jungle_animals`) |
| monkey | ZOO ANIMALS (`zoo_animals`) |
| monopoly | BOARD GAMES (`board_games`) |
| monsoon | STORMS (`storms`) |
| moo | ANIMAL SOUNDS (`animal_sounds`) |
| moonwalk | DANCE MOVES (`dance_moves`) |
| mop | CLEANING TOOLS (`cleaning_tools`) |
| morel | MUSHROOM TYPES (`mushroom_types`) |
| mortadella | CURED MEATS (`cured_meats`) |
| mosaic | ART FORMS (`art_forms`) |
| mosque | PLACES OF WORSHIP (`places_of_worship`) |
| moss | GREEN THINGS (`green_things`) |
| moss | WILD PLANTS (`wild_plants`) |
| moth | BUGS (`insects`) |
| motocross | RACING SPORTS (`racing_sports`) |
| Motor City | CITY NICKNAMES (`city_nicknames`) |
| motorcycle | VEHICLES (`vehicles`) |
| mountain | LANDFORMS (`landforms`) |
| mountain | YOGA POSES (`yoga_poses`) |
| mousse | DESSERTS (`desserts`) |
| Much Ado | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| muffin | BREAKFAST FOODS (`breakfast_foods`) |
| muscular | BODY SYSTEMS (`body_systems`) |
| mushroom | PIZZA TOPPINGS (`pizza_toppings`) |
| music | ART FORMS (`art_forms`) |
| muskrat | RODENTS (`rodents`) |
| mussel | SEAFOOD (`seafood`) |
| Mustang | HORSE BREEDS (`horse_breeds`) |
| mustard | CONDIMENTS (`condiments`) |
| mystery | BOOK GENRES (`book_genres`) |
| Nashville | US CITIES (`us_cities`) |
| nausea | SYMPTOMS (`symptoms`) |
| navy | COLORS (`colors`) |
| navy | MILITARY BRANCHES (`military_branches`) |
| neapolitan | ICE CREAM (`ice_cream_flavors`) |
| neapolitan | PIZZA STYLES (`pizza_styles`) |
| necklace | JEWELRY (`jewelry`) |
| nectar | FLOWER PARTS (`flower_parts`) |
| nectarine | FRUITS (`fruits`) |
| negroni | COCKTAILS (`cocktails`) |
| neigh | ANIMAL SOUNDS (`animal_sounds`) |
| Neptune | PLANETS (`planets`) |
| Neptune | ROMAN GODS (`roman_gods`) |
| nervous | BODY SYSTEMS (`body_systems`) |
| nest | ANIMAL HOMES (`animal_homes`) |
| Nevada | US STATES (`us_states`) |
| new york | PIZZA STYLES (`pizza_styles`) |
| newsprint | KINDS OF PAPER (`paper_types`) |
| Newton | FAMOUS SCIENTISTS (`scientists`) |
| NFL | SPORTS LEAGUES (`sports_leagues`) |
| NHL | SPORTS LEAGUES (`sports_leagues`) |
| nickel | METALS (`metals`) |
| nightshade | POISONOUS PLANTS (`poisonous_plants`) |
| nightstand | FURNITURE (`furniture`) |
| Nile | RIVERS (`rivers`) |
| Nobel | AWARDS (`awards`) |
| nose cone | ROCKET PARTS (`rocket_parts`) |
| notebook | SCHOOL SUPPLIES (`school_supplies`) |
| nougat | CANDY (`candy`) |
| numbat | MARSUPIALS (`marsupials`) |
| oak | TREES (`trees`) |
| oatmeal | BREAKFAST FOODS (`breakfast_foods`) |
| oboe | MUSICAL INSTRUMENTS (`musical_instruments`) |
| oboe | WIND INSTRUMENTS (`wind_instruments`) |
| ocean | BODIES OF WATER (`bodies_of_water`) |
| October | MONTHS (`months`) |
| octopus | OCEAN ANIMALS (`ocean_animals`) |
| Odin | NORSE GODS (`norse_gods`) |
| Odysseus | MYTHOLOGICAL HEROES (`greek_heroes`) |
| old maid | CARD GAMES (`card_games`) |
| oleander | POISONOUS PLANTS (`poisonous_plants`) |
| olive | PIZZA TOPPINGS (`pizza_toppings`) |
| olive oil | COOKING FATS (`cooking_fats`) |
| omelet | BREAKFAST FOODS (`breakfast_foods`) |
| oncology | MEDICAL SPECIALTIES (`medical_specialties`) |
| one way | TRAFFIC SIGNS (`traffic_signs`) |
| onion | VEGETABLES (`vegetables`) |
| opal | GEMSTONES (`gemstones`) |
| orchid | FLOWERS (`flowers`) |
| orchid | HOUSEPLANTS (`houseplants`) |
| oregano | COOKING HERBS (`herbs`) |
| Oregon | US STATES (`us_states`) |
| origami | CRAFTS (`crafts`) |
| Orion | CONSTELLATIONS (`constellations`) |
| orzo | PASTA SHAPES (`pasta_shapes`) |
| Oscar | AWARDS (`awards`) |
| osprey | BIRDS OF PREY (`birds_of_prey`) |
| ostrich | BIRDS (`birds`) |
| othello | BOARD GAMES (`board_games`) |
| othello | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| otter | SEA MAMMALS (`sea_mammals`) |
| ottoman | FURNITURE (`furniture`) |
| oval | SHAPES (`shapes`) |
| owl | BIRDS (`birds`) |
| owl | BIRDS OF PREY (`birds_of_prey`) |
| ox | WORK ANIMALS (`pack_animals`) |
| oxford | FOOTWEAR (`footwear`) |
| oxygen | CHEMICAL ELEMENTS (`elements`) |
| oyster | MUSHROOM TYPES (`mushroom_types`) |
| oyster | SEAFOOD (`seafood`) |
| pack | ANIMAL GROUPS (`animal_groups`) |
| paddleboarding | WATER SPORTS (`water_sports`) |
| painting | ART FORMS (`art_forms`) |
| pair | POKER HANDS (`poker_hands`) |
| palette | PAINTING SUPPLIES (`painting_supplies`) |
| pancake | BREAKFAST FOODS (`breakfast_foods`) |
| papadum | INDIAN DISHES (`indian_dishes`) |
| papaya | FRUITS (`fruits`) |
| papaya | TROPICAL FRUITS (`tropical_fruits`) |
| parcheesi | BOARD GAMES (`board_games`) |
| parchment | KINDS OF PAPER (`paper_types`) |
| parka | WINTER CLOTHING (`winter_clothing`) |
| parrot | BIRDS (`birds`) |
| parrot | JUNGLE ANIMALS (`jungle_animals`) |
| parrot | PETS (`pets`) |
| parrot | TROPICAL BIRDS (`tropical_birds`) |
| parsley | COOKING HERBS (`herbs`) |
| parsnip | ROOT VEGETABLES (`root_vegetables`) |
| paste | COMPUTER ACTIONS (`computer_actions`) |
| pawn | GAME PIECES (`board_game_pieces`) |
| pea | VEGETABLES (`vegetables`) |
| peach | FRUIT TREES (`fruit_trees`) |
| peach | FRUITS (`fruits`) |
| pear | FRUIT TREES (`fruit_trees`) |
| pear | FRUITS (`fruits`) |
| peeler | KITCHEN TOOLS (`kitchen_tools`) |
| pegasus | CONSTELLATIONS (`constellations`) |
| pencil | OFFICE SUPPLIES (`office_supplies`) |
| pencil | SCHOOL SUPPLIES (`school_supplies`) |
| pendant | JEWELRY (`jewelry`) |
| penguin | BIRDS (`birds`) |
| penguin | ZOO ANIMALS (`zoo_animals`) |
| peninsula | LANDFORMS (`landforms`) |
| penne | PASTA SHAPES (`pasta_shapes`) |
| Pentagon | SHAPES (`shapes`) |
| peony | FLOWERS (`flowers`) |
| pepperoni | PIZZA TOPPINGS (`pizza_toppings`) |
| period | PUNCTUATION MARKS (`punctuation`) |
| Perseus | MYTHOLOGICAL HEROES (`greek_heroes`) |
| persian | CAT BREEDS (`cat_breeds`) |
| pesto | SAUCES (`sauces`) |
| petal | FLOWER PARTS (`flower_parts`) |
| petunia | FLOWERS (`flowers`) |
| pho | SOUPS AND STEWS (`soups`) |
| phone | RINGING THINGS (`things_that_ring`) |
| piano | MUSICAL INSTRUMENTS (`musical_instruments`) |
| Picasso | FAMOUS PAINTERS (`artists`) |
| pie | DESSERTS (`desserts`) |
| pig | FARM ANIMALS (`farm_animals`) |
| pigeon | BIRDS (`birds`) |
| pigeon | YOGA POSES (`yoga_poses`) |
| pillow | SOFT THINGS (`soft_things`) |
| pine | TREES (`trees`) |
| pineapple | PIZZA TOPPINGS (`pizza_toppings`) |
| pineapple | TROPICAL FRUITS (`tropical_fruits`) |
| pinochle | CARD GAMES (`card_games`) |
| Pinot Noir | GRAPE VARIETIES (`grape_varieties`) |
| pipette | LAB EQUIPMENT (`lab_equipment`) |
| Pisces | ZODIAC SIGNS (`zodiac_signs`) |
| pistil | FLOWER PARTS (`flower_parts`) |
| pixie | HAIRSTYLES (`hairstyles`) |
| plank | YOGA POSES (`yoga_poses`) |
| plasma | BODY FLUIDS (`body_fluids`) |
| plaster | SCULPTURE MATERIALS (`sculpture_materials`) |
| plateau | LANDFORMS (`landforms`) |
| platinum | METALS (`metals`) |
| please | MANNERS WORDS (`manners`) |
| pliers | JEWELRY SUPPLIES (`jewelry_making`) |
| plum | FRUIT TREES (`fruit_trees`) |
| plum | FRUITS (`fruits`) |
| Pluto | PLANETS (`planets`) |
| poach | COOKING METHODS (`cooking_methods`) |
| pod | ANIMAL GROUPS (`animal_groups`) |
| poker | CARD GAMES (`card_games`) |
| pollen | FLOWER PARTS (`flower_parts`) |
| pomelo | CITRUS FRUITS (`citrus_fruits`) |
| pond | BODIES OF WATER (`bodies_of_water`) |
| ponytail | HAIRSTYLES (`hairstyles`) |
| poodle | DOG BREEDS (`dog_breeds`) |
| popcorn | SNACK FOODS (`snack_foods`) |
| poplar | TREES (`trees`) |
| poppy | FLOWERS (`flowers`) |
| portobello | MUSHROOM TYPES (`mushroom_types`) |
| portrait | PHOTO SUBJECTS (`photography_styles`) |
| Poseidon | GREEK GODS (`greek_gods`) |
| potato | VEGETABLES (`vegetables`) |
| pothos | HOUSEPLANTS (`houseplants`) |
| pottery | ART FORMS (`art_forms`) |
| pottery | CRAFTS (`crafts`) |
| Prado | FAMOUS MUSEUMS (`famous_museums`) |
| preposition | PARTS OF SPEECH (`parts_of_speech`) |
| pride | ANIMAL GROUPS (`animal_groups`) |
| priest | RELIGIOUS LEADERS (`religious_leaders`) |
| prism | SHAPES (`shapes`) |
| private | MILITARY RANKS (`military_ranks`) |
| pronoun | PARTS OF SPEECH (`parts_of_speech`) |
| prosciutto | CURED MEATS (`cured_meats`) |
| pub | PLACES TO EAT (`places_to_eat`) |
| pudding | DESSERTS (`desserts`) |
| Pulitzer | AWARDS (`awards`) |
| pumpernickel | BREAD TYPES (`bread_types`) |
| purple | COLORS (`colors`) |
| purse | ACCESSORIES (`accessories`) |
| puzzle | TOYS (`toys`) |
| pyrite | MINERALS (`minerals`) |
| python | REPTILES (`reptiles`) |
| quack | ANIMAL SOUNDS (`animal_sounds`) |
| quartz | MINERALS (`minerals`) |
| question mark | PUNCTUATION MARKS (`punctuation`) |
| quetzal | TROPICAL BIRDS (`tropical_birds`) |
| quilting | CRAFTS (`crafts`) |
| quokka | MARSUPIALS (`marsupials`) |
| rabbi | RELIGIOUS LEADERS (`religious_leaders`) |
| rabbit | PETS (`pets`) |
| radar | NAVIGATION TOOLS (`navigation_tools`) |
| radiology | MEDICAL SPECIALTIES (`medical_specialties`) |
| radish | ROOT VEGETABLES (`root_vegetables`) |
| radish | VEGETABLES (`vegetables`) |
| ragdoll | CAT BREEDS (`cat_breeds`) |
| rake | GARDEN TOOLS (`garden_tools`) |
| ramen | SOUPS AND STEWS (`soups`) |
| ranch | SAUCES (`sauces`) |
| rap | MUSIC GENRES (`music_genres`) |
| raspberry | BERRIES (`berries`) |
| raspberry | BERRY VARIETIES (`berry_varieties`) |
| rat | RODENTS (`rodents`) |
| ravioli | PASTA SHAPES (`pasta_shapes`) |
| razor | CUTTING TOOLS (`cutting_tools`) |
| Reagan | US PRESIDENTS (`us_presidents`) |
| realism | ART STYLES (`art_styles`) |
| rebus | PUZZLES (`puzzle_types`) |
| rectangle | SHAPES (`shapes`) |
| red | COLORS (`colors`) |
| redwood | TREES (`trees`) |
| reggae | MUSIC GENRES (`music_genres`) |
| relay | TRACK EVENTS (`track_events`) |
| relish | CONDIMENTS (`condiments`) |
| Rembrandt | FAMOUS PAINTERS (`artists`) |
| renaissance | HISTORICAL ERAS (`historical_eras`) |
| restaurant | PLACES TO EAT (`places_to_eat`) |
| retriever | DOG BREEDS (`dog_breeds`) |
| Rialto | FAMOUS BRIDGES (`famous_bridges`) |
| rib | BONES (`bones`) |
| riddle | PUZZLES (`puzzle_types`) |
| rigatoni | PASTA SHAPES (`pasta_shapes`) |
| right | DIRECTIONS (`directions`) |
| risk | BOARD GAMES (`board_games`) |
| risotto | ITALIAN DISHES (`italian_dishes`) |
| river | BODIES OF WATER (`bodies_of_water`) |
| roach | BUGS (`insects`) |
| roar | ANIMAL SOUNDS (`animal_sounds`) |
| roast | COOKING METHODS (`cooking_methods`) |
| robin | BIRDS (`birds`) |
| robin | SONGBIRDS (`songbirds`) |
| robot | TOYS (`toys`) |
| Rockies | MOUNTAIN RANGES (`mountain_ranges`) |
| rocky road | ICE CREAM (`ice_cream_flavors`) |
| roller coaster | AMUSEMENT PARK (`amusement_park`) |
| romance | BOOK GENRES (`book_genres`) |
| romance | MOVIE GENRES (`movie_genres`) |
| Roosevelt | US PRESIDENTS (`us_presidents`) |
| rooster | FARM ANIMALS (`farm_animals`) |
| root | PLANT PARTS (`plant_parts`) |
| rose | FLOWERS (`flowers`) |
| rose | RED THINGS (`red_things`) |
| rosemary | COOKING HERBS (`herbs`) |
| rough | TEXTURES (`textures`) |
| roux | SAUCES (`sauces`) |
| rowing | OLYMPIC SPORTS (`olympic_sports`) |
| rowing | WATER SPORTS (`water_sports`) |
| rubber band | JUNK DRAWER (`things_in_a_junk_drawer`) |
| ruby | GEMSTONES (`gemstones`) |
| rug | HOME DECOR (`home_decor`) |
| rugby | TEAM SPORTS (`team_sports`) |
| ruler | OFFICE SUPPLIES (`office_supplies`) |
| ruler | SCHOOL SUPPLIES (`school_supplies`) |
| rumble | CITY SOUNDS (`city_sounds`) |
| rummy | CARD GAMES (`card_games`) |
| rutabaga | ROOT VEGETABLES (`root_vegetables`) |
| rye | BREAD TYPES (`bread_types`) |
| saber tooth | EXTINCT ANIMALS (`extinct_animals`) |
| sailing | WATER SPORTS (`water_sports`) |
| saliva | BODY FLUIDS (`body_fluids`) |
| salmon | SEAFOOD (`seafood`) |
| saloon | WILD WEST (`wild_west`) |
| salsa | DANCE STYLES (`dance_styles`) |
| samba | DANCE STYLES (`dance_styles`) |
| sandal | FOOTWEAR (`footwear`) |
| sapphire | GEMSTONES (`gemstones`) |
| satin | FABRIC TYPES (`fabric_types`) |
| satin | FABRICS (`fabrics`) |
| Saturn | PLANETS (`planets`) |
| sauerkraut | PICKLED FOODS (`fermented_foods`) |
| sausage | PIZZA TOPPINGS (`pizza_toppings`) |
| saute | COOKING METHODS (`cooking_methods`) |
| save | COMPUTER ACTIONS (`computer_actions`) |
| saw | CUTTING TOOLS (`cutting_tools`) |
| saxophone | MUSICAL INSTRUMENTS (`musical_instruments`) |
| saxophone | WIND INSTRUMENTS (`wind_instruments`) |
| scallop | SEAFOOD (`seafood`) |
| scalpel | CUTTING TOOLS (`cutting_tools`) |
| scarf | ACCESSORIES (`accessories`) |
| scarf | FASHION ACCESSORIES (`fashion_accessories`) |
| scarf | WINTER CLOTHING (`winter_clothing`) |
| school | ANIMAL GROUPS (`animal_groups`) |
| science | SCHOOL SUBJECTS (`school_subjects`) |
| science fiction | BOOK GENRES (`book_genres`) |
| scissors | CUTTING TOOLS (`cutting_tools`) |
| scissors | JUNK DRAWER (`things_in_a_junk_drawer`) |
| scooter | VEHICLES (`vehicles`) |
| scorepad | GAME PIECES (`board_game_pieces`) |
| Scorpio | ZODIAC SIGNS (`zodiac_signs`) |
| scrabble | BOARD GAMES (`board_games`) |
| screech | CITY SOUNDS (`city_sounds`) |
| screwgun | HAND TOOLS (`hand_tools`) |
| sculpture | ART FORMS (`art_forms`) |
| sea | BODIES OF WATER (`bodies_of_water`) |
| Sea World | THEME PARKS (`theme_parks`) |
| seed | PLANT PARTS (`plant_parts`) |
| semicolon | PUNCTUATION MARKS (`punctuation`) |
| sepal | FLOWER PARTS (`flower_parts`) |
| September | MONTHS (`months`) |
| sergeant | MILITARY RANKS (`military_ranks`) |
| serum | BODY FLUIDS (`body_fluids`) |
| sewing | CRAFTS (`crafts`) |
| sextant | NAVIGATION TOOLS (`navigation_tools`) |
| Seychelles | ISLAND NATIONS (`island_nations`) |
| shark | OCEAN ANIMALS (`ocean_animals`) |
| shears | GARDEN TOOLS (`garden_tools`) |
| sheep | FARM ANIMALS (`farm_animals`) |
| sheet bend | KNOTS (`knots`) |
| shellfish | SEAFOOD (`seafood`) |
| sheriff | WILD WEST (`wild_west`) |
| shiitake | MUSHROOM TYPES (`mushroom_types`) |
| shovel | GARDEN TOOLS (`garden_tools`) |
| shrimp | SEAFOOD (`seafood`) |
| siamese | CAT BREEDS (`cat_breeds`) |
| sicilian | PIZZA STYLES (`pizza_styles`) |
| Sicily | ISLANDS (`islands`) |
| sidestroke | SWIM STROKES (`swimming_strokes`) |
| sieve | THINGS WITH HOLES (`things_with_holes`) |
| sigma | GREEK LETTERS (`greek_letters`) |
| silk | FABRIC TYPES (`fabric_types`) |
| silk | FABRICS (`fabrics`) |
| silk | SOFT THINGS (`soft_things`) |
| silky | TEXTURES (`textures`) |
| silver | METALS (`metals`) |
| Sin City | CITY NICKNAMES (`city_nicknames`) |
| sitar | STRING INSTRUMENTS (`string_instruments`) |
| sitcom | TV GENRES (`tv_genres`) |
| situp | EXERCISE WORDS (`exercise_words`) |
| sizzle | KITCHEN SOUNDS (`kitchen_sounds`) |
| skateboard | THINGS WITH WHEELS (`things_with_wheels`) |
| skeletal | BODY SYSTEMS (`body_systems`) |
| skiing | OLYMPIC SPORTS (`olympic_sports`) |
| skiing | WINTER SPORTS (`winter_sports`) |
| skink | LIZARDS (`lizards`) |
| skull | BONES (`bones`) |
| sleeping bag | CAMPING GEAR (`camping_gear`) |
| slow | TRAFFIC SIGNS (`traffic_signs`) |
| smile | FACIAL EXPRESSIONS (`facial_expressions`) |
| smoker | BEEKEEPING THINGS (`beekeeping`) |
| smooth | TEXTURES (`textures`) |
| snake | REPTILES (`reptiles`) |
| sneaker | FOOTWEAR (`footwear`) |
| sneeze | BODY SOUNDS (`body_sounds`) |
| snickerdoodle | COOKIE TYPES (`cookie_types`) |
| snore | BODY SOUNDS (`body_sounds`) |
| snowboarding | WINTER SPORTS (`winter_sports`) |
| soccer | TEAM SPORTS (`team_sports`) |
| soda | DRIVE THRU (`fast_food_items`) |
| sofa | FURNITURE (`furniture`) |
| solder | JEWELRY SUPPLIES (`jewelry_making`) |
| Solitaire | CARD GAMES (`card_games`) |
| sombrero | HATS (`hats`) |
| Sonic | FAST FOOD (`fast_food_chains`) |
| sorry | BOARD GAMES (`board_games`) |
| sorry | MANNERS WORDS (`manners`) |
| souffle | DESSERTS (`desserts`) |
| soul | MUSIC GENRES (`music_genres`) |
| sourdough | BREAD TYPES (`bread_types`) |
| soy | SAUCES (`sauces`) |
| spaniel | DOG BREEDS (`dog_breeds`) |
| spanish | LANGUAGES (`languages`) |
| sparrow | BIRDS (`birds`) |
| spatula | KITCHEN TOOLS (`kitchen_tools`) |
| speed limit | TRAFFIC SIGNS (`traffic_signs`) |
| sphere | SHAPES (`shapes`) |
| sphinx | FAMOUS LANDMARKS (`famous_landmarks`) |
| spider | BUGS (`insects`) |
| Spiderman | SUPERHEROES (`superheroes`) |
| spin | DANCE MOVES (`dance_moves`) |
| spinach | PIZZA TOPPINGS (`pizza_toppings`) |
| spinach | VEGETABLES (`vegetables`) |
| spinner | GAME PIECES (`board_game_pieces`) |
| Spirit | AIRLINES (`airlines`) |
| splint | FIRST AID (`first_aid`) |
| spoon | KITCHEN TOOLS (`kitchen_tools`) |
| sprain | INJURIES (`injuries`) |
| sprint | TRACK EVENTS (`track_events`) |
| squall | STORMS (`storms`) |
| Square | SHAPES (`shapes`) |
| squirrel | RODENTS (`rodents`) |
| stamen | FLOWER PARTS (`flower_parts`) |
| Stanford | UNIVERSITIES (`universities`) |
| stapler | OFFICE SUPPLIES (`office_supplies`) |
| steam | COOKING METHODS (`cooking_methods`) |
| steam | HOT THINGS (`hot_things`) |
| steam engine | INDUSTRIAL AGE (`industrial_revolution`) |
| steel | BUILDING MATERIALS (`building_materials`) |
| steel | METALS (`metals`) |
| steeplechase | TRACK EVENTS (`track_events`) |
| stegosaurus | DINOSAURS (`dinosaurs`) |
| stem | PLANT PARTS (`plant_parts`) |
| sticky | TEXTURES (`textures`) |
| stone | SCULPTURE MATERIALS (`sculpture_materials`) |
| Stone Age | HISTORICAL ERAS (`historical_eras`) |
| stool | FURNITURE (`furniture`) |
| stop | TRAFFIC SIGNS (`traffic_signs`) |
| storm | SUPERHEROES (`superheroes`) |
| straight | POKER HANDS (`poker_hands`) |
| strait | BODIES OF WATER (`bodies_of_water`) |
| strawberry | BERRIES (`berries`) |
| strawberry | BERRY VARIETIES (`berry_varieties`) |
| strawberry | ICE CREAM (`ice_cream_flavors`) |
| Stripe | PATTERNS (`patterns`) |
| Subway | FAST FOOD (`fast_food_chains`) |
| Subway | VEHICLES (`vehicles`) |
| Sumer | ANCIENT CIVILIZATIONS (`ancient_civilizations`) |
| summer | SEASONS (`seasons`) |
| sun | LIGHT SOURCES (`light_sources`) |
| sunflower | FLOWERS (`flowers`) |
| sunglasses | ACCESSORIES (`accessories`) |
| sunglasses | EYEWEAR (`eyewear`) |
| sunglasses | FASHION ACCESSORIES (`fashion_accessories`) |
| Superman | SUPERHEROES (`superheroes`) |
| supernova | SPACE PHENOMENA (`space_phenomena`) |
| surfing | WATER SPORTS (`water_sports`) |
| surgery | MEDICAL PROCEDURES (`medical_procedures`) |
| surrealism | ART STYLES (`art_styles`) |
| swan | BIRDS (`birds`) |
| swarm | ANIMAL GROUPS (`animal_groups`) |
| sweat | BODY FLUIDS (`body_fluids`) |
| swelling | SYMPTOMS (`symptoms`) |
| swimming | OLYMPIC SPORTS (`olympic_sports`) |
| swimming | WATER SPORTS (`water_sports`) |
| swing | DANCE STYLES (`dance_styles`) |
| Sydney Harbour | FAMOUS BRIDGES (`famous_bridges`) |
| synagogue | PLACES OF WORSHIP (`places_of_worship`) |
| Syrah | GRAPE VARIETIES (`grape_varieties`) |
| table | FURNITURE (`furniture`) |
| tablet | GADGETS (`gadgets`) |
| taco | STREET FOOD (`street_food`) |
| taekwondo | MARTIAL ARTS (`martial_arts`) |
| taffy | CANDY (`candy`) |
| taiga | BIOMES (`biomes`) |
| Taj Mahal | FAMOUS LANDMARKS (`famous_landmarks`) |
| tambourine | PERCUSSION INSTRUMENTS (`percussion`) |
| tangerine | CITRUS FRUITS (`citrus_fruits`) |
| tango | DANCE STYLES (`dance_styles`) |
| tape | STICKY THINGS (`sticky_things`) |
| tape | JUNK DRAWER (`things_in_a_junk_drawer`) |
| tarboosh | WORLD HATS (`world_hats`) |
| tarp | CAMPING GEAR (`camping_gear`) |
| tarragon | COOKING HERBS (`herbs`) |
| tart | DESSERTS (`desserts`) |
| Taurus | ZODIAC SIGNS (`zodiac_signs`) |
| tea | HOT DRINKS (`hot_drinks`) |
| telephone | INVENTIONS (`inventions`) |
| tempera | KINDS OF PAINT (`paint_types`) |
| Tempest | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| Tempest | STORMS (`storms`) |
| tent | CAMPING GEAR (`camping_gear`) |
| teriyaki | SAUCES (`sauces`) |
| termite | BUGS (`insects`) |
| terrier | DOG BREEDS (`dog_breeds`) |
| Tesla | INVENTORS (`inventors`) |
| thank you | MANNERS WORDS (`manners`) |
| Thanksgiving | HOLIDAYS (`holidays`) |
| theft | CRIMES (`crimes`) |
| therapy | MEDICAL PROCEDURES (`medical_procedures`) |
| thermometer | WEATHER INSTRUMENTS (`weather_instruments`) |
| thermos | PICNIC BASKET (`picnic_basket`) |
| Thor | NORSE GODS (`norse_gods`) |
| thoroughbred | HORSE BREEDS (`horse_breeds`) |
| thriller | BOOK GENRES (`book_genres`) |
| thyme | COOKING HERBS (`herbs`) |
| tiger | JUNGLE ANIMALS (`jungle_animals`) |
| tiger | STRIPED THINGS (`striped_things`) |
| tiger | WILD CATS (`wild_cats`) |
| tiger | ZOO ANIMALS (`zoo_animals`) |
| Tigers | TEAM NAMES (`sports_teams`) |
| tile | BUILDING MATERIALS (`building_materials`) |
| tiramisu | DESSERTS (`desserts`) |
| tiramisu | ITALIAN DISHES (`italian_dishes`) |
| tire | CAR PARTS (`car_parts`) |
| titanium | METALS (`metals`) |
| toaster | KITCHEN APPLIANCES (`kitchen_appliances`) |
| toe | BODY PARTS (`body_parts`) |
| token | GAME PIECES (`board_game_pieces`) |
| tomato | RED THINGS (`red_things`) |
| tomato | SANDWICH FILLINGS (`sandwich_fillings`) |
| tomato | SOUPS AND STEWS (`soups`) |
| tongs | KITCHEN TOOLS (`kitchen_tools`) |
| tongue | SHOE PARTS (`shoe_parts`) |
| topaz | GEMSTONES (`gemstones`) |
| torch | LIGHT SOURCES (`light_sources`) |
| tornado | NATURAL DISASTERS (`natural_disasters`) |
| tornado | STORMS (`storms`) |
| tortoise | REPTILES (`reptiles`) |
| toucan | TROPICAL BIRDS (`tropical_birds`) |
| Tower Bridge | FAMOUS BRIDGES (`famous_bridges`) |
| Toyota | CAR BRANDS (`car_brands`) |
| tractor | VEHICLES (`vehicles`) |
| train set | TOYS (`toys`) |
| trapezoid | SHAPES (`shapes`) |
| treadmill | GYM EQUIPMENT (`gym_equipment`) |
| tree | YOGA POSES (`yoga_poses`) |
| triangle | PERCUSSION INSTRUMENTS (`percussion`) |
| triangle | SHAPES (`shapes`) |
| tricep | MUSCLES (`muscles`) |
| triceratops | DINOSAURS (`dinosaurs`) |
| trivial pursuit | BOARD GAMES (`board_games`) |
| Trix | CEREAL BRANDS (`cereal_brands`) |
| trouble | BOARD GAMES (`board_games`) |
| trowel | GARDEN TOOLS (`garden_tools`) |
| truck | VEHICLES (`vehicles`) |
| trucks | SKATEBOARDING WORDS (`skateboarding`) |
| Truist | BANK BRANDS (`bank_brands`) |
| trumpet | MUSICAL INSTRUMENTS (`musical_instruments`) |
| trumpet | WIND INSTRUMENTS (`wind_instruments`) |
| tsunami | NATURAL DISASTERS (`natural_disasters`) |
| tulip | FLOWERS (`flowers`) |
| tundra | BIOMES (`biomes`) |
| turban | HATS (`hats`) |
| turnip | ROOT VEGETABLES (`root_vegetables`) |
| turnip | VEGETABLES (`vegetables`) |
| turquoise | GEMSTONES (`gemstones`) |
| turtle | REPTILES (`reptiles`) |
| tweed | FABRIC TYPES (`fabric_types`) |
| tweet | ANIMAL SOUNDS (`animal_sounds`) |
| Twelfth Night | SHAKESPEARE PLAYS (`shakespeare_plays`) |
| twist | DANCE MOVES (`dance_moves`) |
| typhoon | STORMS (`storms`) |
| Tyr | NORSE GODS (`norse_gods`) |
| Uffizi | FAMOUS MUSEUMS (`famous_museums`) |
| ukulele | STRING INSTRUMENTS (`string_instruments`) |
| ultrasound | MEDICAL PROCEDURES (`medical_procedures`) |
| unicorn | MYTHICAL CREATURES (`fantasy_creatures`) |
| United | AIRLINES (`airlines`) |
| up | DIRECTIONS (`directions`) |
| Uranus | PLANETS (`planets`) |
| urine | BODY FLUIDS (`body_fluids`) |
| Ursa Major | CONSTELLATIONS (`constellations`) |
| vacuum | CLEANING TOOLS (`cleaning_tools`) |
| valley | LANDFORMS (`landforms`) |
| vampire | SCARY CREATURES (`monsters`) |
| van | VEHICLES (`vehicles`) |
| vanilla | ICE CREAM (`ice_cream_flavors`) |
| velcro | FASTENERS (`fasteners`) |
| velociraptor | DINOSAURS (`dinosaurs`) |
| velvet | FABRIC TYPES (`fabric_types`) |
| velvet | FABRICS (`fabrics`) |
| velvet | SOFT THINGS (`soft_things`) |
| Venus | PLANETS (`planets`) |
| Venus | ROMAN GODS (`roman_gods`) |
| Vermeer | FAMOUS PAINTERS (`artists`) |
| Victorian | HISTORICAL ERAS (`historical_eras`) |
| Vietnam | ASIAN COUNTRIES (`asian_countries`) |
| viola | STRING INSTRUMENTS (`string_instruments`) |
| Violet | COLORS (`colors`) |
| Violet | FLOWERS (`flowers`) |
| violin | STRING INSTRUMENTS (`string_instruments`) |
| viper | REPTILES (`reptiles`) |
| viperfish | DEEP SEA (`deep_sea`) |
| Virgo | ZODIAC SIGNS (`zodiac_signs`) |
| volcano | NATURAL DISASTERS (`natural_disasters`) |
| vole | RODENTS (`rodents`) |
| volleyball | TEAM SPORTS (`team_sports`) |
| vulture | BIRDS OF PREY (`birds_of_prey`) |
| wagon | VEHICLES (`vehicles`) |
| waldorf | SALADS (`salads`) |
| wallaby | MARSUPIALS (`marsupials`) |
| walrus | SEA MAMMALS (`sea_mammals`) |
| waltz | DANCE STYLES (`dance_styles`) |
| war | CARD GAMES (`card_games`) |
| warbler | SONGBIRDS (`songbirds`) |
| wardrobe | FURNITURE (`furniture`) |
| warrior | YOGA POSES (`yoga_poses`) |
| Washington | US PRESIDENTS (`us_presidents`) |
| wasp | BUGS (`insects`) |
| water polo | TEAM SPORTS (`team_sports`) |
| water polo | WATER SPORTS (`water_sports`) |
| watercolor | KINDS OF PAINT (`paint_types`) |
| waterfall | BODIES OF WATER (`bodies_of_water`) |
| WD40 | HARDWARE BRANDS (`paint_and_home`) |
| weaver | HISTORIC TRADES (`old_professions`) |
| weaving | CRAFTS (`crafts`) |
| weightlifting | OLYMPIC SPORTS (`olympic_sports`) |
| Wendys | FAST FOOD (`fast_food_chains`) |
| werewolf | SCARY CREATURES (`monsters`) |
| western | MOVIE GENRES (`movie_genres`) |
| whale | OCEAN ANIMALS (`ocean_animals`) |
| wheel | CAR PARTS (`car_parts`) |
| wheel | ROUND THINGS (`round_things`) |
| whisk | KITCHEN TOOLS (`kitchen_tools`) |
| wildfire | NATURAL DISASTERS (`natural_disasters`) |
| Willow | TREES (`trees`) |
| windsurfing | WATER SPORTS (`water_sports`) |
| Windy City | CITY NICKNAMES (`city_nicknames`) |
| wink | FACIAL EXPRESSIONS (`facial_expressions`) |
| winter | SEASONS (`seasons`) |
| wiper | CAR PARTS (`car_parts`) |
| wombat | MARSUPIALS (`marsupials`) |
| Wonder Woman | SUPERHEROES (`superheroes`) |
| wood | BUILDING MATERIALS (`building_materials`) |
| woodworking | CRAFTS (`crafts`) |
| wool | FABRIC TYPES (`fabric_types`) |
| wool | FABRICS (`fabrics`) |
| wren | SONGBIRDS (`songbirds`) |
| wrestling | OLYMPIC SPORTS (`olympic_sports`) |
| xylophone | PERCUSSION INSTRUMENTS (`percussion`) |
| yacht | BOATS AND SHIPS (`boats`) |
| Yale | UNIVERSITIES (`universities`) |
| yawn | BODY SOUNDS (`body_sounds`) |
| yellow | COLORS (`colors`) |
| yield | TRAFFIC SIGNS (`traffic_signs`) |
| yogurt | BREAKFAST FOODS (`breakfast_foods`) |
| yogurt | DAIRY PRODUCTS (`dairy_products`) |
| Yuban | COFFEE BRANDS (`coffee_brands`) |
| zebra | STRIPED THINGS (`striped_things`) |
| zebra | ZOO ANIMALS (`zoo_animals`) |
| Zeus | GREEK GODS (`greek_gods`) |
| zinc | METALS (`metals`) |
| zinnia | FLOWERS (`flowers`) |
| ziti | PASTA SHAPES (`pasta_shapes`) |
| zombie | SCARY CREATURES (`monsters`) |
| zucchini | VEGETABLES (`vegetables`) |

## 5. Длинные надписи (193)

Больше 15 символов. Влезет ли в пузырь на телефоне — вопрос к реальному интерфейсу,
а не к базе. Либо короткая форма для показа, либо слово убрать.

| слово | символов |
|---|---|
| Declaration of Independence | 27 |
| Emancipation Proclamation | 25 |
| Girl with a Pearl Earring | 25 |
| board games with pieces | 23 |
| spaghetti and meatballs | 23 |
| air traffic controller | 22 |
| Jack and the Beanstalk | 22 |
| Mary Had a Little Lamb | 22 |
| social media platforms | 22 |
| university departments | 22 |
| game night essentials | 21 |
| Industrial Revolution | 21 |
| Madison Square Garden | 21 |
| synchronized swimming | 21 |
| academic departments | 20 |
| Beauty and the Beast | 20 |
| cognitive behavioral | 20 |
| green bean casserole | 20 |
| Hickory Dickory Dock | 20 |
| Kennedy Space Center | 20 |
| programming language | 20 |
| return on investment | 20 |
| switchboard operator | 20 |
| Treaty of Versailles | 20 |
| appliance repairman | 19 |
| arthur ashe stadium | 19 |
| automotive industry | 19 |
| Baa Baa Black Sheep | 19 |
| cognitive functions | 19 |
| Dubai International | 19 |
| father of the bride | 19 |
| Taming of the Shrew | 19 |
| Valley of the Kings | 19 |
| american crocodile | 18 |
| american shorthair | 18 |
| back end developer | 18 |
| ceremonial objects | 18 |
| chutes and ladders | 18 |
| construction paper | 18 |
| cooking techniques | 18 |
| credit card reader | 18 |
| emotional numbness | 18 |
| facial expressions | 18 |
| Gettysburg Address | 18 |
| Great Expectations | 18 |
| herbes de provence | 18 |
| Jet Propulsion Lab | 18 |
| knowledge is power | 18 |
| Louisville Slugger | 18 |
| Merchant of Venice | 18 |
| orchestra sections | 18 |
| overhead projector | 18 |
| philly cheesesteak | 18 |
| production release | 18 |
| refrigerated truck | 18 |
| religious building | 18 |
| Spirit of St Louis | 18 |
| strategic thinking | 18 |
| Sydney Opera House | 18 |
| telegraph operator | 18 |
| the little mermaid | 18 |
| to be or not to be | 18 |
| tourist attraction | 18 |
| water purification | 18 |
| abstract thinking | 17 |
| apraxia of speech | 17 |
| astronomical unit | 17 |
| baking essentials | 17 |
| benjamin franklin | 17 |
| Buckingham Palace | 17 |
| Charles de Gaulle | 17 |
| chicago deep dish | 17 |
| combine harvester | 17 |
| community service | 17 |
| consumer insights | 17 |
| contextualization | 17 |
| cookies and cream | 17 |
| denzel washington | 17 |
| dramatis personae | 17 |
| education process | 17 |
| egyptian language | 17 |
| exclamation point | 17 |
| fill in the blank | 17 |
| forensic medicine | 17 |
| french revolution | 17 |
| Fruit of the Loom | 17 |
| gingerbread house | 17 |
| Hansel and Gretel | 17 |
| Hundred Years War | 17 |
| hydrothermal vent | 17 |
| indian paintbrush | 17 |
| italian seasoning | 17 |
| Itsy Bitsy Spider | 17 |
| Knotts Berry Farm | 17 |
| lambert conformal | 17 |
| leonardo dicaprio | 17 |
| millennium falcon | 17 |
| navigation system | 17 |
| physical activity | 17 |
| piccadilly circus | 17 |
| planetary science | 17 |
| poultry seasoning | 17 |
| release candidate | 17 |
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
| aurora australis | 16 |
| automatic feeder | 16 |
| beach volleyball | 16 |
| bird of paradise | 16 |
| Black and Decker | 16 |
| black eyed susan | 16 |
| botanical garden | 16 |
| brussels sprouts | 16 |
| bulletproof vest | 16 |
| business analyst | 16 |
| byzantine empire | 16 |
| cafeteria worker | 16 |
| Call of the Wild | 16 |
| capture the flag | 16 |
| carbon footprint | 16 |
| casting director | 16 |
| charging station | 16 |
| chicken sandwich | 16 |
| chocolate square | 16 |
| college features | 16 |
| computer science | 16 |
| consequentialism | 16 |
| costume designer | 16 |
| creation of adam | 16 |
| desktop research | 16 |
| destroying angel | 16 |
| enchanted forest | 16 |
| enchanted mirror | 16 |
| extraterrestrial | 16 |
| flight attendant | 16 |
| floyd mayweather | 16 |
| four leaf clover | 16 |
| gala dali castle | 16 |
| gasoline storage | 16 |
| Georgia Aquarium | 16 |
| Golden Delicious | 16 |

Показано 150 из 193.

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
