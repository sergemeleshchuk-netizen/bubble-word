# Категории, часть 1 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: animals_more

### ANIMAL GENDERS  `animal_names_male_female`
- правило: Words for the male or female of an animal species
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- ~buck, ~bull, ~doe, ~gander, ~hen, ~jack (jack_animal), ~rooster, ~tom, ~vixen, +boar, +cow, +drake, +ewe, +jenny, +mare, +ram, +sow (sow_pig), +stallion

### GRAZING ANIMALS  `antelope_and_grazers`
- правило: Animals that graze on grass in herds
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~zebra, +antelope, +bison, +buffalo, +elk, +gazelle, +gnu, +impala, +oryx, +springbok, +wildebeest, +yak, !eland, !kudu

### YOUNG ANIMALS  `baby_animal_words_more`
- правило: Less common words for young animals
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- !cygnet, !eaglet, !hatchling, !kid, !nymph, !spat, !squab, !whelp, xelver, xleveret, xpoult, xshoat

### CRUSTACEANS  `crustaceans`
- правило: Sea creatures with a hard shell and many legs
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- +barnacle, +crab, +crayfish, +hermit crab, +king crab, +krill, +lobster, +pill bug, +prawn, +shrimp, !isopod

### EXOTIC PETS  `exotic_pets`
- правило: Unusual animals people keep as pets
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~ferret, ~hedgehog, ~parrot, ~python, ~tarantula, ~tortoise, +chinchilla, +gecko, +hermit crab, +iguana, +sugar glider, !axolotl, xdegu

### SOFT CREATURES  `jellyfish_and_soft`
- правило: Soft bodied sea creatures without bones
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- ~jellyfish, ~octopus, ~sponge (sponge_animal), ~squid, !anemone, !coral polyp, !cuttlefish, !man o war, !nudibranch, !sea cucumber, !sea slug

### MARSUPIALS  `marsupials`
- правило: Animals that carry young in a pouch
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~opossum, +bandicoot, +kangaroo, +koala, +sugar glider, +tasmanian devil, +wallaby, +wombat, !quokka, xnumbat

### WORK ANIMALS  `pack_animals`
- правило: Animals used to carry loads or do work
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~alpaca, ~camel, ~dog, ~elephant, ~husky, ~reindeer, +donkey, +horse, +llama, +mule, +ox, +water buffalo, +yak

### EXOTIC BIRDS  `parrots_and_exotic_birds`
- правило: Colorful birds kept as pets or seen in zoos
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~budgie, ~parakeet, ~toucan, +cockatoo, +parrot, !cockatiel, !conure, !hornbill, !lorikeet, !lovebird, !macaw, !myna, !quetzal

### SEAL FAMILY  `seals_and_walruses`
- правило: Kinds of seal and sea lion
- тип связи: `is_a`, базовая сложность 0.45
- слов: 9
- ~sea lion, ~walrus, !elephant seal, !fur seal, !harbor seal, !harp seal, !leopard seal, !monk seal, !ringed seal

### TURTLES  `turtles_and_tortoises`
- правило: Kinds of turtle and tortoise
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- +box turtle, +green turtle, +painted turtle, +sea turtle, +slider, +snapping turtle, +tortoise, !hawksbill, !leatherback, !terrapin

### WADING BIRDS  `wading_birds`
- правило: Birds with long legs that wade in shallow water
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~egret, +crane, +flamingo, +heron, +ibis, +plover, +stork, !avocet, !bittern, !sandpiper, !spoonbill, !stilt

### WATERFOWL  `waterfowl`
- правило: Birds that swim on lakes and ponds
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~teal, +coot, +duck (duck_bird), +goose, +heron, +ibis, +loon, +mallard, +pelican, +swan, !cormorant, !egret, !grebe, !merganser

### SMALL CATS  `wild_cats_small`
- правило: Smaller members of the wild cat family
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- !bobcat, !caracal, !fishing cat, !jaguarundi, !lynx, !ocelot, !pallas cat, !sand cat, !serval, xmargay

### WORMS  `worms_and_crawlers`
- правило: Kinds of worm
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~earthworm, ~leech, ~tapeworm, !flatworm, !glowworm, !inchworm, !nightcrawler, !ringworm, !roundworm, !silkworm, xbloodworm


## Тема: culture

### CLASSIC GAMES  `card_and_dice_games`
- правило: Classic games played for generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~badminton, ~jump rope, +checkers, +chess, +croquet, +dominoes, +hide and seek, +jacks, +marbles, +tag (tag_game), !charades, !hopscotch, !horseshoes, !tiddlywinks

### WORLD FESTIVALS  `festivals`
- правило: Festivals celebrated around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +Bastille Day, +Carnival, +Cinco de Mayo, +Day of the Dead, +Diwali, +Holi, +Lunar New Year, +Mardi Gras, +Oktoberfest, !Hogmanay, !Obon, !Songkran, !St Patricks Day

### NATIONAL SYMBOLS  `flags_and_symbols`
- правило: Things used as symbols of a country
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~anthem, ~bear, ~crescent, ~crown (crown_royal), ~dragon, ~eagle, ~kangaroo, ~lion, ~maple leaf, ~rose, ~shamrock, ~star, ~tulip, +flag, +thistle

### GREEK LETTERS  `greek_letters`
- правило: Letters of the Greek alphabet
- тип связи: `is_a`, базовая сложность 0.35
- слов: 24
- ~pi, +alpha, +beta, +chi, +delta (delta_letter), +epsilon, +eta, +gamma, +iota, +kappa, +lambda, +mu, +nu, +Omega, +phi, +psi, +rho, +sigma, +tau, +theta, +xi, +zeta, !omicron, !upsilon

### LATIN PHRASES  `latin_phrases`
- правило: Latin phrases used in everyday English
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- !ad hoc, !agenda, !alibi, !alma mater, !alter ego, !bona fide, !carpe diem, !et cetera, !magnum opus, !per capita, !per se, !quid pro quo, !status quo, !versus, !vice versa

### MANNERS WORDS  `manners`
- правило: Words used when teaching good manners
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~chewing, ~greeting, ~listening, ~patience, ~please, ~respect, ~sharing, ~sorry, ~waiting, +apologize, +excuse me, +may I, +thank you, +turn taking

### OPPOSITES  `opposites`
- правило: Words commonly taught as opposites
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~big, ~cold (cold_temperature), ~day, ~dry, ~far, ~fast, ~full, ~hard, ~hot (hot_temperature), ~in, ~near, ~night, ~slow, ~small, ~soft, ~wet, +dark, +down, +high, +light (light_bright), +low, +open, +out, +shut, +up

### PLAYGROUND GAMES  `playground_games`
- правило: Games children play at recess
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~dodgeball, ~jump rope, ~tag (tag_game), +capture the flag, +duck duck goose, +four square, +freeze tag, +hide and seek, +hot potato, +marbles, +red rover, +simon says, !hopscotch, !kickball

### NUMBER WORDS  `superstition_numbers`
- правило: Words for numbers and counting
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~dozen, ~few, ~half, ~quarter (quarter_fourth), ~score (score_twenty), +billion, +couple, +eight, +five, +four, +hundred, +million, +nine, +one, +pair, +seven, +single (single_one), +six, +ten, +thousand, +three, +twenty, +two, +zero

### TRADITIONAL CLOTHING  `traditional_clothing`
- правило: Traditional garments from world cultures
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~kilt, ~kimono, ~sombrero, ~toga, ~turban, +poncho, +sari, !dashiki, !dirndl, !hanbok, !kaftan, !kente, !lederhosen, !moccasin, !sarong

### RETRO GAMES  `video_game_classics`
- правило: Video games known across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~centipede, ~Sonic, +Asteroids, +Donkey Kong, +Mario, +Pac Man, +Pinball, +Pong, +Solitaire, +Space Invaders, +Tetris, +Zelda, !Frogger, !Galaga, !Minesweeper

### MORE CURRENCIES  `world_currencies_more`
- правило: Currencies used in particular countries
- тип связи: `is_a`, базовая сложность 0.45
- слов: 18
- ~yen, +baht, +dinar, +kroner, +lira, +peso, +rand, +real, +ruble, +rupee, +yuan, !dirham, !forint, !koruna, !ringgit, !riyal, !shekel, !zloty

### WORLD DANCES  `world_dances`
- правило: Traditional dances from around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~flamenco, +hula, +irish jig, +kabuki, +mambo, +polka, +salsa, +samba, +square dance, +tango, +waltz, !bolero, !cancan, !merengue, !tarantella

### WORLD HATS  `world_hats`
- правило: Traditional headwear from world cultures
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~beret, ~panama, ~sombrero, !bowler, !conical hat, !fez, !keffiyeh, !tam, !tarboosh, !turban, xkufi, xushanka

### WORLD INSTRUMENTS  `world_instruments`
- правило: Musical instruments from cultures around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~bagpipes, ~ukulele, +steel drum, !balalaika, !bouzouki, !didgeridoo, !djembe, !erhu, !kalimba, !koto, !marimba, !oud, !shamisen, !sitar, xpanpipe


## Тема: descriptive

### AGE WORDS  `age_words`
- правило: Words describing how old something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~brand new, +aged, +ancient, +antique, +contemporary, +fresh (fresh_new), +modern, +new, +old, +prehistoric, +secondhand, +vintage, +worn, !timeworn

### BRIGHTNESS WORDS  `brightness_words`
- правило: Words describing how much light something gives
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bright, ~dark, ~dim, ~dull, ~faint, ~gloomy, ~glowing, ~murky, ~radiant, ~shady, ~shining, !blinding, !dazzling, !luminous

### CERTAINTY WORDS  `certainty_words`
- правило: Words describing how sure something is
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~certain, ~definite, ~doubtful, ~likely, ~maybe, ~obvious, ~perhaps, ~possible, ~probable, ~sure, ~uncertain, ~unlikely, !guaranteed

### CLEANLINESS WORDS  `cleanliness_words`
- правило: Words describing how clean something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~polished, +clean, +dirty, +dusty, +filthy, +grimy, +immaculate, +messy, +muddy, +neat, +soiled, +spotless, +stained, +sterile, +tidy

### DIFFICULTY WORDS  `difficulty_words`
- правило: Words describing how hard a task is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~manageable, +challenging, +complex, +demanding, +easy, +effortless, +grueling, +hard, +impossible, +simple, +straightforward, +tedious, +tough, +tricky

### DISTANCE WORDS  `distance_words`
- правило: Words describing how far something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~next door, ~opposite, +adjacent, +alongside, +beyond, +close, +distant, +far, +faraway, +halfway, +near, +nearby, +remote (remote_far), +within reach

### FREQUENCY WORDS  `frequency_words`
- правило: Words describing how often something happens
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +always, +annually, +constantly, +daily, +frequently, +hourly, +monthly, +never, +occasionally, +often, +rarely, +seldom, +sometimes, +weekly

### FULLNESS WORDS  `fullness_words`
- правило: Words describing how full something is
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bare, ~brimming, ~crowded, ~deserted, ~empty, ~full, ~hollow, ~packed, ~sparse, ~stuffed, ~vacant, !jammed, !loaded, !overflowing

### VOLUME WORDS  `noise_adjectives`
- правило: Words describing how loud something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~faint, ~soft, +booming, +deafening, +hushed, +loud, +muffled, +noisy, +quiet, +roaring, +shrill, +silent, +still, +thunderous

### ORDER WORDS  `order_words`
- правило: Words describing position in a sequence
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~middle, +final, +first, +following, +former, +initial, +last, +latter, +next, +previous, +second (second_order), +subsequent, +third, +ultimate

### QUANTITY WORDS  `quantity_words`
- правило: Words describing how much of something there is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~load, ~none, ~pile, ~pinch, ~sprinkle, +abundant, +batch, +bunch, +dozens, +few, +handful, +heap, +many, +plenty, +scarce, +several, +some, +ton

### SHAPE ADJECTIVES  `shape_adjectives`
- правило: Words describing the shape of an object
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~hollow, ~oval, ~smooth, ~square, +bent, +crooked, +curved, +flat, +jagged, +narrow, +pointed, +round (round_shape), +straight, +tapered, +thick, +thin, +twisted, +wide

### SMELL WORDS  `smell_words`
- правило: Words describing how something smells
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~earthy, ~floral, ~fragrant, ~fresh (fresh_scent), ~minty, ~musty, ~pungent, ~rancid, ~sour, ~stale, ~sweet, !briny, !smoky, !spicy, !woodsy

### SPEED WORDS  `speed_adjectives`
- правило: Words describing how fast something moves
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~creeping, ~sluggish, +brisk, +fast, +gradual, +hasty, +leisurely, +quick, +rapid, +slow, +speedy, +steady, +sudden, +swift

### STRENGTH WORDS  `strength_words`
- правило: Words describing strength
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +brittle (brittle_property), +delicate, +durable, +feeble, +flimsy, +fragile, +frail, +mighty, +robust, +solid (solid_strong), +strong, +sturdy, +tough, +weak

### TASTE WORDS  `taste_words`
- правило: Words describing how food tastes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bland, ~hearty, ~mild, ~peppery, ~rich, ~smoky, ~syrupy, ~zesty, +bitter, +buttery, +creamy, +crisp, +nutty, +salty, +savory, +sour, +spicy, +sweet, +tangy, +tart

### TOUCH WORDS  `temperature_feel`
- правило: Words describing how something feels to touch
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~bumpy, ~cold (cold_temperature), ~damp, ~fuzzy, ~grainy, ~hard, ~rough, ~Sharp, ~silky, ~slippery, ~smooth, ~soft, ~spongy, ~sticky, ~warm, !prickly

### PRICE WORDS  `value_words`
- правило: Words describing how much something costs
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~overpriced, +affordable, +bargain, +budget, +cheap, +costly, +discounted, +expensive, +free, +luxurious, +priceless, +pricey, +valuable, +worthless

### WEATHER ADJECTIVES  `weather_adjectives`
- правило: Words describing the weather outside
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~drizzly, ~snowy, +balmy, +breezy, +clear, +cloudy, +foggy, +freezing, +humid, +icy, +mild, +muggy, +overcast, +rainy, +stormy, +sunny, +sweltering, +windy

### WETNESS WORDS  `wetness_words`
- правило: Words describing how wet something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~crisp, ~dewy, +arid, +damp, +drenched, +dripping, +dry, +humid, +moist, +parched, +saturated, +soaked, +soggy, +wet


## Тема: farming

### BARN THINGS  `barn_things`
- правило: Things found inside a barn
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~bucket, ~gate (gate_barrier), ~lantern, ~rope, ~sack (sack_bag), ~shovel, +bale, +feed, +harness, +hay, +loft, +milking stool, +pitchfork, +saddle, +stall (stall_barn), +trough

### BEEKEEPING THINGS  `beekeeping`
- правило: Things used in beekeeping
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~comb, ~frame, ~gloves, ~queen (queen_bee), ~smoker, ~super, ~veil, +drone, +extractor, +hive, +honey, +pollen, +wax (wax_substance), +worker

### COUNTRY LIFE  `country_life`
- правило: Things associated with rural country living
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~bonfire, ~chores, ~creek, ~mailbox, ~pasture, ~pond, ~porch, ~rooster, ~tractor, ~well, +dirt road, +fence post, +general store, +pickup truck, !hayride

### DAIRY FARM  `dairy_words`
- правило: Things involved in dairy farming
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~barn, ~cheese, ~churn, ~pail, ~udder, +calf (calf_cow), +cream (cream_dairy), +curd, +herd, +milk, +milking machine, +separator, !butterfat, !pasteurize

### FARM BUILDINGS  `farm_buildings`
- правило: Buildings and structures on a farm
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~coop, ~greenhouse, ~pen (pen_animal), ~shed, ~silo, ~stable, +barn, +corral, +dairy, +farmhouse, +fence, +granary, +windmill, !hayloft, !smokehouse

### FARM MACHINES  `farm_machines`
- правило: Machines used on a modern farm
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~combine, ~harvester, ~mower, ~plow, ~tractor, +harrow, +irrigation pump, +silo loader, +sprayer, +spreader, +tiller, !baler, !cultivator, !seeder, !thresher

### FARM PRODUCTS  `farm_products`
- правило: Things a farm produces to sell
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~beef, ~cheese, ~cider, ~corn, ~cotton, ~eggs, ~hay, ~honey, ~lumber, ~maple syrup, ~milk, ~pork, ~produce, ~wool, +grain, +leather

### HARVEST WORDS  `harvest_words`
- правило: Words used at harvest time
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~wagon, ~yield, +bale, +bushel, +crop, +field, +granary, +reap, +scythe, +sheaf, +sickle, +silo, +stack (stack_pile), !gleaning, !thresh

### IRRIGATION THINGS  `irrigation`
- правило: Things used to water crops
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~canal, ~dam, ~ditch, ~hose, ~pipe (pipe_tube), ~pump, ~sprinkler, ~valve, ~well, !aqueduct, !drip line, !furrow, !pivot, !reservoir

### LIVESTOCK  `livestock`
- правило: Animals raised for food or farm work
- тип связи: `is_a`, базовая сложность 0.25
- слов: 17
- ~alpaca, ~bison, ~chicken, ~pig, ~rabbit, ~turkey (turkey_bird), +cow, +donkey, +duck (duck_bird), +geese, +goat, +guinea fowl, +horse, +llama, +mule, +ox, +sheep

### ORCHARD WORDS  `orchard_words`
- правило: Things found in a fruit orchard
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~basket, ~bee, ~blossom, ~crate, ~harvest, ~ladder, ~row, ~tree, +cider press, +grafting, +mulch, +netting, +picker, !pruner

### CROP PESTS  `pest_control`
- правило: Creatures that damage crops
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~aphid, ~beetle, ~caterpillar, ~deer, ~gopher, ~grasshopper, ~mite, ~slug, !crow, !cutworm, !locust, !nematode, !rabbit, !weevil

### RANCH WORDS  `ranch_words`
- правило: Things found on a cattle ranch
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~boot (boot_shoe), ~brand (brand_cattle), ~corral, ~fence, ~lasso, ~trough, +cattle, +cowboy, +herd, +horse, +roundup, +saddle, +spur, +stampede, !bunkhouse

### SOIL WORDS  `soil_words`
- правило: Words used to describe soil and its care
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~clay, ~compost, ~erosion, ~fertilizer, ~plow, ~sand, !acidity, !humus, !loam, !mulch, !nutrient, !silt, !subsoil, !topsoil

### VINEYARD WORDS  `vineyard_words`
- правило: Things found in a vineyard
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~barrel, ~cellar, ~cork, ~grape, ~vine, !cluster, !crush, !harvest, !press (press_machine), !pruning, !rootstock, !terrace, !trellis, !vat


## Тема: language

### RADIO ALPHABET  `alphabet_code`
- правило: Code words used to spell letters over a radio
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~alpha, ~delta (delta_letter), ~Juliet, ~Romeo, !Bravo, !Charlie, !Echo, !foxtrot, !Golf, !Hotel, !India, !Kilo, !Lima, !Mike, !November, !Oscar, !Papa, !Quebec, !Sierra, !tango, !Victor, !Whiskey, !Yankee, !Zulu

### GREETINGS  `greetings_and_farewells`
- правило: Words and phrases used to greet or say goodbye
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~evening, ~later, ~morning, ~salute, +aloha, +bye, +cheers (cheers_greeting), +farewell, +goodbye, +greetings, +hello, +hi, +howdy, +so long, +welcome

### LANGUAGES  `languages`
- правило: Languages spoken around the world
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~polish (polish_language), +Arabic, +Chinese, +Dutch, +English, +French, +German, +greek, +Hebrew, +Hindi, +Italian, +Japanese, +Korean, +Latin, +Portuguese, +Russian, +spanish, +Swedish, +Turkish, +Vietnamese

### PARTS OF SPEECH  `parts_of_speech`
- правило: Grammatical categories of English words
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~article, +adjective, +adverb, +conjunction, +noun, +participle, +preposition, +pronoun, +verb, !determiner, !gerund, !interjection

### POLITE WORDS  `polite_words`
- правило: Words used to be polite in English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~madam, ~sir, ~welcome, +apologize, +appreciate, +excuse me, +kindly, +may, +pardon, +please, +sorry, +thanks

### PUNCTUATION MARKS  `punctuation`
- правило: Marks used to punctuate written English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~dash (dash_mark), ~semicolon, +apostrophe, +asterisk, +bracket, +colon, +comma, +exclamation point, +hyphen, +parenthesis, +period, +question mark, +quotation mark, +slash, !ellipsis

### QUESTION WORDS  `question_words`
- правило: Words that begin a question in English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- +how, +what, +when, +where, +whether, +which, +who, +whom, +whose, +why

### FAST WORDS  `word_fast`
- правило: English words that mean moving quickly
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +breakneck, +brisk, +express, +fast, +fleet, +hasty, +hurried, +nimble, +prompt, +quick, +rapid, +snappy, +speedy, +swift

### BIG WORDS  `word_size`
- правило: English words that mean large in size
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +big, +bulky, +colossal, +enormous, +giant, +gigantic, +grand, +hefty, +huge, +immense, +jumbo, +mammoth, +massive, +towering, +vast

### SMALL WORDS  `word_small`
- правило: English words that mean small in size
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~pocket, +compact, +dwarf, +little, +micro, +mini, +miniature, +minute (minute_tiny), +petite, +pint sized, +slight, +small, +tiny, +wee

### AIR ___  `words_after_air`
- правило: Words that form a familiar English compound when placed after the word air
- тип связи: `phrase_after`, базовая сложность 0.4
- слов: 18
- ~brush, ~conditioner, ~craft, ~plane (plane_aircraft), ~space, !bag, !borne, !fare, !field, !force, !line (line_drawn), !mail, !port, !show, !strip, !tight, !time, !way

### BACK ___  `words_after_back`
- правило: Words that form a familiar English compound when placed after the word back
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 18
- ~bend, ~board (board_plank), ~door, ~drop, ~fire, ~ground, ~hand (hand_body), ~log, ~pack, ~splash, ~stage, ~track, ~up, ~yard (yard_ground), !bone, !lash, !seat, !ward

### WORDS AFTER BOOK  `words_after_book`
- правило: Words that form a familiar English compound when placed after the word book
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 14
- ~bag, ~binding, ~case (case_box), ~keeper, ~mark, ~report, ~review, ~seller, ~shelf (shelf_furniture), ~store, ~worm, !club, !end, !let

### FIRE ___  `words_after_fire`
- правило: Words that form a familiar English compound when placed after the word fire
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 19
- ~alarm, ~ant, ~break, ~drill (drill_practice), ~escape, ~fly (fly_insect), ~house, ~man, ~pit, ~place, ~side, ~truck, ~wood, !arm, !ball (ball_sphere), !hydrant, !proof, !storm, !works

### FOOT ___  `words_after_foot`
- правило: Words that form a familiar English compound when placed after the word foot
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 15
- ~ball (ball_sphere), ~bridge (bridge_structure), ~hill, ~locker, ~loose, ~note (note_written), ~path, ~print, ~step, ~wear, ~work, !age, !lights, !rest (rest_sleep), !stool

### HAND ___  `words_after_hand`
- правило: Words that form a familiar English compound when placed after the word hand
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 17
- ~bag, ~book, ~cuff, ~held, ~made, ~print, ~shake, ~stand (stand_pose), ~writing, !ball (ball_sphere), !ful, !gun, !kerchief, !out, !picked, !rail, !saw

### HEAD ___  `words_after_head`
- правило: Words that form a familiar English compound when placed after the word head
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 16
- ~ache, ~band (band_ring), ~count, ~gear, ~stone, !board (board_plank), !dress, !first, !light (light_bright), !line (line_drawn), !master, !phone, !quarters, !rest (rest_sleep), !strong, !way

### HORSE ___  `words_after_horse`
- правило: Words that form a familiar English compound when placed after the word horse
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 14
- ~cart, ~drawn, ~man, ~race, ~radish, ~trailer (trailer_vehicle), ~whip, !back, !fly (fly_insect), !hair, !play, !power, !sense, !shoe

### RAIN ___  `words_after_rain`
- правило: Words that form a familiar English compound when placed after the word rain
- тип связи: `phrase_after`, базовая сложность 0.4
- слов: 14
- ~barrel, ~cloud, ~coat (coat_garment), ~drop, ~fall, ~gutter, ~maker, ~storm, ~water, !boot (boot_shoe), !bow (bow_arc), !check (check_rain), !dance, !forest

### SNOW ___  `words_after_snow`
- правило: Words that form a familiar English compound when placed after the word snow
- тип связи: `phrase_after`, базовая сложность 0.4
- слов: 18
- ~ball (ball_sphere), ~blind, ~board (board_plank), ~cone, ~drift, ~flake, ~man, ~plow, ~storm, ~tire, !angel, !bank, !cap, !day, !fall, !mobile, !shoe, !suit (suit_clothing)

### SUN ___  `words_after_sun`
- правило: Words that form a familiar English compound when placed after the word sun
- тип связи: `phrase_after`, базовая сложность 0.4
- слов: 20
- ~bathe, ~beam (beam_light), ~burn, ~day, ~dial, ~dress, ~flower, ~glasses, ~light (light_bright), ~rise, ~roof, ~room, ~screen (screen_shield), ~set (set_sun), ~shine, ~spot, ~tan, !block (block_shield), !fish, !stroke (stroke_sun)

### WATER ___  `words_after_water`
- правило: Words that form a familiar English compound when placed after the word water
- тип связи: `phrase_after`, базовая сложность 0.45
- слов: 18
- ~color, ~fall, ~melon, ~mill, ~park (park_place), ~shed, ~spout, ~way, ~works, !bed, !cress, !front, !gun, !line (line_drawn), !logged, !mark, !proof, !tower

### ___ BAG  `words_before_bag`
- правило: Words that form a familiar English compound when placed before the word bag
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 18
- ~body, ~garbage, ~grab, ~hand (hand_body), ~sleeping, ~tea, ~trash, !air, !book, !doggy, !duffel, !gift, !gym, !ice, !mail, !punching, !saddle, !sand

### ___ BALL  `words_before_ball`
- правило: Words that form a familiar English compound when placed before the word ball
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 20
- ~base, ~basket, ~cannon, ~eye, ~foot (foot_body), ~hair, ~high, ~odd, ~pin (pin_fastener), ~soft, ~spit, !fire, !gum (gum_candy), !hard, !low, !meat, !mother, !screw, !snow, !volley

### ___ BERRY  `words_before_berry`
- правило: Words that form a familiar berry name when placed before the word berry
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 14
- ~bar (bar_berry), ~black, ~blue, ~goose, ~straw (straw_berry), !boysen, !choke, !cran, !dew, !elder (elder_plant), !huckle, !logan, !mul, !rasp

### ___ BIRD  `words_before_bird`
- правило: Words that form a familiar English compound when placed before the word bird
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 14
- ~black, ~blue, ~early, ~ground, ~humming, ~sea, ~snow, ~song, !cat, !jail, !lady, !love, !mocking, !thunder

### ___ BOARD  `words_before_board`
- правило: Words that form a familiar English compound when placed before the word board
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 20
- ~bill (bill_money), ~black, ~card (card_board), ~chalk (chalk_stick), ~clip, ~dash (dash_car), ~head (head_body), ~score (score_points), ~sea, ~skate, ~snow, ~spring, ~star, ~surf, ~switch, ~white (white_color), !cup, !key, !side, !sign

### ___ BOOK  `words_before_book`
- правило: Words that form a familiar English compound when placed before the word book
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 20
- ~check (check_payment), ~comic, ~cook (cook_prepare), ~face, ~guide, ~hand (hand_body), ~hymn, ~log, ~match, ~note (note_written), ~phone, ~play, ~pocket, ~scrap, ~sketch, ~story (story_tale), ~text, ~work, !pass, !year

### ___ BOX  `words_before_box`
- правило: Words that form a familiar English compound when placed before the word box
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 18
- ~ballot, ~boom, ~chatter, ~gear, ~glove, ~ice, ~jack (jack_box), ~litter, ~lunch, ~mail, ~shoe, ~tool, !black, !breaker, !cash, !juke, !match, !sand

### ___ CAKE  `words_before_cake`
- правило: Words that form a familiar English compound when placed before the word cake
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 18
- ~carrot, ~cheese, ~coffee, ~corn, ~crab, ~cup, ~fruit, ~hot (hot_temperature), ~oat, ~pan, ~pound (pound_cake), ~rice, ~sheet (sheet_pan), ~sponge (sponge_cake), ~tea, ~wedding, !birth, !short

### ___ FISH  `words_before_fish`
- правило: Words that form a familiar English compound when placed before the word fish
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 18
- ~blow, ~cat, ~dog, ~gold, ~lion, ~sail (sail_fish), ~shell, ~silver, ~star, ~sun, !angel, !clown, !cray, !cuttle, !jelly, !king, !sword, !sword tail

### ___ GROUND  `words_before_ground`
- правило: Words that form a familiar English compound when placed before the word ground
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 14
- ~back, ~burial, ~common, ~fair, ~fore, ~play, !battle, !breeding, !camp, !high, !home, !proving, !stamping, !under

### ___ HOUSE  `words_before_house`
- правило: Words that form a familiar English compound when placed before the word house
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 20
- ~bird, ~club, ~court (court_law), ~dog, ~doll, ~farm, ~green (green_color), ~guest, ~hen, ~out, ~ranch, ~safe, ~steak, ~town, ~tree, !boat, !light (light_bright), !road, !school, !ware

### ___ LIGHT  `words_before_light`
- правило: Words that form a familiar English compound when placed before the word light
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 20
- ~back, ~candle, ~day, ~fire, ~flash, ~gas, ~high, ~moon (moon_space), ~night, ~search, ~side, ~sky, ~spot, ~star (star_shape), ~stop, ~sun, ~tail, !head (head_body), !lime, !twi

### ___ LINE  `words_before_line`
- правило: Words that form a familiar English compound when placed before the word line
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 20
- ~air, ~clothes, ~coast, ~dead, ~front, ~guide, ~hair, ~head (head_body), ~hot (hot_temperature), ~Life, ~out, ~pipe (pipe_tube), ~shore, ~side, ~sky, ~time, ~waist, !base, !punch (punch_hit), !tree

### ___ MAN  `words_before_man`
- правило: Words that form a familiar English compound when placed before the word man
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 20
- ~business, ~fire, ~gentle, ~ice, ~mail, ~milk, ~police, ~sales, ~snow, ~spider, ~sports, ~super, ~weather, ~work, !chair, !crafts, !door, !garbage, !hu, !states

### ___ MASTER  `words_before_master`
- правило: Words that form a familiar English compound when placed before the word master
- тип связи: `phrase_before`, базовая сложность 0.5
- слов: 14
- ~band (band_ring), ~choir, ~pay, ~quarter (quarter_lodging), ~school, ~task, !grand, !harbor, !head (head_body), !post (post_mail), !ring, !spy, !station (station_place), !web

### ___ PAPER  `words_before_paper`
- правило: Words that form a familiar English compound when placed before the word paper
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 16
- ~construction, ~graph, ~news, ~note (note_written), ~parchment, ~term (term_period), ~tissue (tissue_paper), ~toilet, ~wall, ~wrapping, !crepe, !filter, !flypaper, !sand, !tracing, !wax (wax_substance)

### ___ PROOF  `words_before_proof`
- правило: Words that form a familiar English compound when placed before the word proof
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 14
- ~fire, ~leak, ~oven, ~rust, ~water, ~weather, ~wrinkle, !bullet, !child, !fool, !mistake, !shock, !sound (sound_noise), !tamper

### ___ ROOM  `words_before_room`
- правило: Words that form a familiar English phrase when placed before the word room
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 18
- ~ball (ball_dance), ~bath, ~bed, ~board (board_committee), ~class, ~court (court_law), ~dark, ~dining, ~elbow, ~guest, ~living, ~mush, ~rest (rest_sleep), ~sun, ~wait, !lock, !show, !store

### ___ SAUCE  `words_before_sauce`
- правило: Words that form a familiar English expression when placed before the word sauce
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 15
- ~apple (apple_fruit), ~barbecue, ~cheese, ~chili (chili_pepper), ~cranberry, ~fish, ~hot (hot_spicy), ~pizza, ~soy, ~steak, ~taco, ~tomato, ~white (white_color), !duck (duck_meat), !tartar

### ___ SIDE  `words_before_side`
- правило: Words that form a familiar English compound when placed before the word side
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 18
- ~bed, ~broad, ~curb, ~dark, ~down, ~hill, ~in, ~out, ~river, ~road, ~sea, ~top (top_upper), ~up, ~way, !be, !country, !fire, !ring

### ___ STONE  `words_before_stone`
- правило: Words that form a familiar English compound when placed before the word stone
- тип связи: `phrase_before`, базовая сложность 0.5
- слов: 16
- ~birth, ~brim, ~corner, ~curb, ~grave, ~rolling, ~tomb, !flag, !gall, !hail, !key, !lime, !mile, !moon, !sand, !stepping

### ___ TIME  `words_before_time`
- правило: Words that form a familiar English phrase when placed before the word time
- тип связи: `phrase_before`, базовая сложность 0.4
- слов: 20
- ~bed, ~day, ~full, ~half, ~Life, ~lunch, ~meal, ~night, ~part (part_portion), ~play, ~prime, ~show, ~some, ~spring, ~story (story_tale), ~summer, ~tea, !big, !over, !war

### ___ WORK  `words_before_work`
- правило: Words that form a familiar English compound when placed before the word work
- тип связи: `phrase_before`, базовая сложность 0.45
- слов: 18
- ~art, ~brick, ~clock, ~fire, ~frame, ~ground, ~home, ~house, ~metal, ~paper, ~patch, ~team, ~wood, !foot (foot_body), !guess, !hand (hand_body), !net, !road

### WRITING WORDS  `writing_words`
- правило: Words for the parts and marks of written text
- тип связи: `found_in`, базовая сложность 0.3
- слов: 21
- ~byline, ~capital (capital_letter), ~column, ~comma, ~footnote, ~letter (letter_alphabet), ~period, +caption, +chapter, +draft (draft_document), +font, +heading, +index, +margin, +outline, +page, +paragraph, +sentence (sentence_writing), +signature, +title, +word


## Тема: law

### COURTROOM THINGS  `courtroom_things`
- правило: Things and people found in a courtroom
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bench (bench_court), ~exhibit, ~sentence (sentence_punishment), ~stand (stand_witness), +bailiff, +defendant, +docket, +evidence, +gavel, +judge, +jury, +lawyer, +oath, +plaintiff, +testimony, +transcript, +verdict, +witness

### CRIMES  `crimes`
- правило: Acts that are against the law
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~smuggling, ~speeding, +arson, +blackmail, +bribery, +burglary, +counterfeiting, +embezzlement, +forgery, +fraud, +kidnapping, +littering, +perjury, +poaching, +shoplifting, +theft, +trespassing, +vandalism

### DETECTIVE WORDS  `detective_words`
- правило: Words used in a criminal investigation
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~case (case_legal), ~clue, ~footprint, ~forensics, ~lead (lead_clue), +alibi, +autopsy, +evidence, +fingerprint, +interrogation, +lineup, +motive, +suspect, +warrant, +witness, !stakeout

### EMERGENCY SERVICES  `emergency_services`
- правило: Public services that respond to emergencies
- тип связи: `is_a`, базовая сложность 0.25
- слов: 12
- ~ambulance, ~police, ~Ranger, +animal control, +coast guard, +dispatch, +fire department, +hazmat, +hospital, +poison control, +rescue squad, +search and rescue

### GOVERNMENT WORDS  `government_branches`
- правило: Words for the parts and workings of government
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~bill (bill_law), ~budget, ~cabinet (cabinet_government), ~committee, ~house, ~term (term_period), ~treaty, +amendment, +ballot, +campaign, +congress, +election, +law, +majority, +senate, +session, +veto, +vote

### LEGAL DOCUMENTS  `legal_documents`
- правило: Documents used in legal matters
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~certificate, ~patent, ~testament, ~title, ~warrant, ~will, +affidavit, +contract, +deed, +lease, +license, +permit, +petition, +subpoena, +summons, +waiver

### MILITARY BRANCHES  `military_branches`
- правило: Branches of the armed forces
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~cavalry, +air force, +army, +artillery, +coast guard, +infantry, +marines, +militia, +national guard, +navy, +reserves, +space force

### MILITARY EQUIPMENT  `military_things`
- правило: Equipment used by the armed forces
- тип связи: `used_in`, базовая сложность 0.3
- слов: 19
- ~backpack, ~binoculars, ~boots, ~canteen, ~compass, ~helmet, ~Jeep, ~jet, ~medal, ~radio, ~rifle, ~submarine, ~uniform, +bunker (bunker_shelter), +camouflage, +dog tag, +parachute, +ration, +tank (tank_military)

### MILITARY WORDS  `military_words`
- правило: Words used in military life
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~drill (drill_practice), ~leave, ~march (march_walk), ~mission, ~patrol, +barracks, +base, +boot camp, +deploy, +formation, +platoon, +rank, +roll call, +salute, +squad, !reveille

### POLICE THINGS  `police_things`
- правило: Equipment and things used by police
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~flashlight, ~holster, ~radio, ~ticket (ticket_fine), ~vest, ~whistle, +badge, +baton, +cruiser, +dispatch, +handcuffs, +k9, +patrol, +siren, +uniform, +warrant

### PRISON WORDS  `prison_words`
- правило: Things and words associated with prison
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~bunk, ~parole, ~sentence (sentence_punishment), ~uniform, ~yard (yard_ground), +bail, +bars, +cell (cell_room), +guard (guard_prison), +inmate, +lockdown, +mess hall, +release, +visitation, +warden, !cellmate

### PENALTIES  `punishments`
- правило: Penalties handed down for breaking rules
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~ban, ~curfew, ~detention, ~fine, ~forfeit, ~suspension, ~ticket (ticket_fine), ~warning, +community service, +expulsion, +jail, +penalty, +probation, +restitution

### RIGHTS  `rights_and_freedoms`
- правило: Legal rights and freedoms people have
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~appeal, ~assembly, ~equality, ~press (press_media), ~protest, ~religion, ~speech, ~vote, +bear arms, +counsel, +due process, +petition, +privacy, +trial

### SAFETY WORDS  `safety_signs`
- правило: Words seen on warning and safety signs
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~emergency, ~poison, ~slippery, +biohazard, +caution, +danger, +exit, +flammable, +hazard, +high voltage, +keep out, +no entry, +restricted, +stop, +warning, +yield

### SPY WORDS  `spy_words`
- правило: Things associated with spies and espionage
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~bug, ~informant, ~mission, ~mole (mole_spy), ~tail, +agent, +alias, +cipher, +code, +decoder, +disguise, +dossier, +microfilm, +safe house, +surveillance


## Тема: materials

### BUILDING MATERIALS  `building_materials`
- правило: Materials used to construct buildings
- тип связи: `made_of`, базовая сложность 0.25
- слов: 20
- ~aluminum, ~drywall, ~glass, ~lumber, ~plywood, ~shingle, ~steel, ~vinyl, +brick, +cement, +concrete, +granite, +insulation, +marble (marble_stone), +plaster, +slate, +stone, +stucco, +tile, +wood

### FABRIC TYPES  `fabric_types`
- правило: Kinds of cloth used to make things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~canvas, ~jersey, ~lace, ~terry, ~wool, +burlap, +chiffon, +corduroy, +cotton, +denim, +felt, +flannel, +linen, +muslin, +satin, +silk, +tweed, +velvet, !gingham, !taffeta

### INSULATING MATERIALS  `insulating_materials`
- правило: Materials used to keep heat or sound in or out
- тип связи: `used_in`, базовая сложность 0.45
- слов: 13
- ~cork, ~cotton, ~felt, ~foam, ~plastic, ~rubber, ~styrofoam, ~wool, !air, !cellulose, !drywall, !fiberglass, !straw (straw_hay)

### LIQUIDS  `liquids`
- правило: Common liquids found around a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~bleach, ~broth, ~coffee, ~gasoline, ~glue, ~ink, ~juice, ~milk, ~oil (oil_cooking), ~paint, ~polish (polish_product), ~shampoo, ~soap, ~soda, ~syrup, ~tea, ~vinegar, +alcohol, +lotion, +water

### MINERALS  `minerals`
- правило: Minerals found in the earth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~graphite, ~gypsum, ~quartz, ~sulfur, +calcite, +magnetite, +mica, +pyrite, +talc, !azurite, !feldspar, !fluorite, !halite, !hematite

### POWDERS  `powders`
- правило: Common substances that come as a powder
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~baking soda, ~chalk (chalk_stick), ~cinnamon, ~cocoa, ~detergent, ~dust, ~flour, ~salt, ~sand, ~spice, ~sugar, ~talcum, !cement, !powdered milk, !protein powder

### PRECIOUS MATERIALS  `precious_materials`
- правило: Rare and valuable materials
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~emerald, ~ivory, ~jade, ~marble (marble_stone), ~silk, +amber, +diamond, +gold, +mahogany, +opal, +pearl, +platinum, +ruby, +sapphire, +silver

### RECYCLABLE MATERIALS  `recycled_materials`
- правило: Materials that can be recycled
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~aluminum, ~cardboard, ~carton, ~glass, ~newspaper, ~paper, ~plastic, ~steel, ~tin (tin_can), !battery, !cloth, !compost, !electronics, !rubber

### GLASS THINGS  `things_made_of_glass`
- правило: Everyday things normally made of glass
- тип связи: `made_of`, базовая сложность 0.3
- слов: 15
- ~aquarium, ~bottle, ~bulb, ~jar, ~lens, ~marble (marble_toy), ~mirror, ~prism, ~thermometer, ~tumbler, ~vase, ~window, !greenhouse, !ornament, !screen (screen_display)

### LEATHER THINGS  `things_made_of_leather`
- правило: Everyday things normally made of leather
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~belt, ~boot (boot_shoe), ~briefcase, ~glove, ~holster, ~jacket, ~purse, ~saddle, ~shoe, ~strap, ~wallet, !bookmark, !couch

### METAL THINGS  `things_made_of_metal`
- правило: Everyday things normally made of metal
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~armor, ~bell, ~chain, ~coin, ~faucet, ~hinge, ~kettle, ~key, ~ladder, ~nail (nail_metal), ~pipe (pipe_tube), ~safe, ~spoon, ~sword, ~wire, ~wrench, !anchor, !can

### PAPER THINGS  `things_made_of_paper`
- правило: Everyday things normally made of paper
- тип связи: `made_of`, базовая сложность 0.3
- слов: 16
- ~bag, ~book, ~calendar, ~card (card_greeting), ~envelope, ~map, ~napkin, ~newspaper, ~origami, ~poster, ~receipt, ~ticket (ticket_admission), ~tissue (tissue_paper), ~wallpaper, !carton, !kite (kite_toy)

### PLASTIC THINGS  `things_made_of_plastic`
- правило: Everyday things normally made of plastic
- тип связи: `made_of`, базовая сложность 0.35
- слов: 16
- ~bag, ~bottle, ~bucket, ~container, ~crate, ~cup, ~helmet, ~pipe (pipe_tube), ~ruler, ~straw (straw_tube), ~toy, !card (card_plastic), !chair, !comb, !hanger, !keyboard (keyboard_computer)

### RUBBER THINGS  `things_made_of_rubber`
- правило: Everyday things normally made of rubber
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~band (band_ring), ~boot (boot_shoe), ~bumper, ~duck (duck_toy), ~eraser, ~hose, ~seal (seal_rubber), ~stamp (stamp_tool), ~tire, ~tube, !gasket, !glove, !mat

### WOODEN THINGS  `things_made_of_wood`
- правило: Everyday things normally made of wood
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~barrel, ~bat, ~cabinet (cabinet_furniture), ~chair, ~crate, ~deck, ~drum, ~fence, ~guitar, ~shelf (shelf_furniture), ~spoon, ~table, ~toothpick, !broom handle, !canoe, !door, !ladder, !pencil

### FUELS  `things_that_burn`
- правило: Materials burned to produce heat or power
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~alcohol, ~paper, ~wax (wax_substance), ~wood, +charcoal, +coal, +diesel, +ethanol, +gasoline, +kerosene, +natural gas, +oil (oil_motor), +peat, +propane


## Тема: misc

### GLOVE BOX  `things_in_a_glove_box`
- правило: Things kept in a car glove compartment
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~flashlight, ~insurance, ~sunglasses, !Charger, !gum (gum_candy), !ice scraper, !manual, !map, !napkins, !pen (pen_writing), !registration, !tire gauge, !tissues

### PURSE THINGS  `things_in_a_purse`
- правило: Things carried in a purse
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~gum (gum_candy), ~keys, ~lipstick, ~mirror, ~pen (pen_writing), ~phone, ~planner, ~snack, ~sunglasses, ~tissue (tissue_paper), ~wallet, +Charger, +hand sanitizer, +receipt, !hairbrush

### TOOLBOX THINGS  `things_in_a_toolbox`
- правило: Things kept in a household toolbox
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~flashlight, ~glue, ~level, ~sandpaper, ~tape, +allen key, +hammer, +nails, +pliers, +screwdriver, +screws, +tape measure, +utility knife, +wrench

### WALLET THINGS  `things_in_a_wallet`
- правило: Things people keep in a wallet
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~badge, ~cash, ~coupon, ~license, ~note (note_money), ~photo, ~stamp (stamp_postage), ~ticket (ticket_admission), +business card, +card (card_plastic), +gift card, +insurance card, +membership card, +receipt

### KEYCHAIN THINGS  `things_on_a_keychain`
- правило: Things hanging from a keychain
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~ring, !bottle opener, !carabiner, !charm, !flashlight, !fob, !key, !lanyard, !mini tool, !souvenir, !tag (tag_label), !usb drive, !whistle

### PAIRED THINGS  `things_that_come_in_pairs`
- правило: Things that normally come in twos
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~earrings, ~ears, ~eyes, ~gloves, ~hands, ~headphones, ~shoes, ~skis, ~socks, !chopsticks, !cufflinks, !dice (dice_game), !lungs, !scissors, !twins, !wings

### FACED THINGS  `things_that_have_a_face`
- правило: Objects described as having a face
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~building, ~cliff, ~clock, ~doll, ~jack o lantern, ~mask, ~mountain, ~poster, ~watch (watch_object), !coin, !dice (dice_game), !playing card, !puppet, !snowman

### RINGING THINGS  `things_that_ring`
- правило: Things that ring or chime
- тип связи: `does_action`, базовая сложность 0.35
- слов: 12
- ~alarm, ~bell, ~buzzer, ~chime, ~clock, ~doorbell, ~phone, ~timer, !bicycle bell, !cash register, !church bell, !dinner bell

### TRASH ITEMS  `things_you_recycle`
- правило: Things commonly thrown out or recycled
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~bag, ~bottle, ~box, ~can, ~carton, ~core, ~envelope, ~jar, ~newspaper, ~packaging, ~peel, ~receipt, ~tissue (tissue_paper), !wrapper

### VENDING MACHINE  `vending_machine_items`
- правило: Things sold from a vending machine
- тип связи: `found_in`, базовая сложность 0.35
- слов: 13
- ~chips, ~coffee, ~granola bar, ~gum (gum_candy), ~juice, ~soda, ~water, +candy bar, +cookies, +mints, +popcorn, +pretzels, +sandwich


## Тема: nature

### DIRT THINGS  `animal_tracks_and_signs`
- правило: Marks and things you see in bare dirt
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~ant, ~dust, ~footprint, ~gravel, ~hole, ~mud, ~pebble, ~puddle, ~root, ~seed, ~stone, ~track, ~twig, ~worm, !tire mark

### BODIES OF WATER  `bodies_of_water`
- правило: Natural or man-made bodies of water on the surface of the earth
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~gulf, ~sound (sound_water), ~spring (spring_water), +bay, +brook, +canal, +creek, +delta (delta_river), +estuary, +fjord, +harbor, +inlet, +lagoon, +lake, +marsh, +ocean, +pond, +pool, +reservoir, +river, +sea, +strait, +stream, +swamp, +waterfall

### SKY WORDS  `cloud_and_sky`
- правило: Things you can see in the sky
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~aurora, ~balloon, ~fog, ~lightning, ~smoke, ~sunset, +bird, +cloud, +comet, +eclipse, +haze, +helicopter, +kite (kite_toy), +meteor, +moon, +plane (plane_aircraft), +rainbow, +satellite, +star, +sun

### DESERT THINGS  `desert_things`
- правило: Things found in a hot desert
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~canyon, ~coyote, ~heat, ~lizard, ~rock (rock_stone), ~sand, ~snake, ~vulture, +cactus, +camel, +drought, +dune, +mirage, +oasis, +rattlesnake, +sagebrush, +scorpion, +tumbleweed

### FLOWER PARTS  `flower_parts`
- правило: Parts of a flowering plant
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~bulb, ~leaf, ~pistil, ~root, ~sepal, ~stamen, +blossom, +bud, +nectar, +petal, +pollen, +seed, +stalk, +stem, +thorn

### FLOWERS  `flowers`
- правило: Kinds of flowers commonly sold or grown in gardens
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +azalea, +buttercup, +carnation, +daffodil, +dahlia, +Daisy, +geranium, +hyacinth, +iris, +Jasmine, +lavender (lavender_plant), +lilac, +Lily, +magnolia, +marigold, +orchid, +peony, +poppy, +rose, +sunflower, +tulip, +Violet, !begonia, !petunia, !zinnia

### GARDEN PLANTS  `garden_plants`
- правило: Plants people grow in a home garden
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~basil, ~carrot, ~lavender (lavender_plant), ~pepper, ~pumpkin, ~rose, ~strawberry, ~sunflower, ~tomato, ~tulip, +bean, +cucumber, +Fern, +Ivy, +lettuce, +marigold, +mint (mint_herb), +squash (squash_vegetable), +zucchini, !hosta

### GEMSTONES  `gemstones`
- правило: Precious or semi-precious stones used in jewelry
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~coral, ~jade, ~quartz, +agate, +amethyst, +aquamarine, +diamond (diamond_gem), +emerald, +garnet, +lapis, +moonstone, +obsidian, +onyx, +opal, +pearl, +peridot, +ruby, +sapphire, +topaz, +turquoise

### LIGHT SOURCES  `light_sources`
- правило: Things that give off light
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- ~fire, ~lightning, ~moon, ~screen (screen_display), +bulb, +campfire, +candle, +firefly, +flashlight, +headlight, +lamp, +lantern, +laser, +match, +neon, +star, +sun, +torch, !glowstick, !streetlight

### MOUNTAIN THINGS  `mountain_things`
- правило: Things found on or around a mountain
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~boulder, ~cabin (cabin_house), ~cave, ~eagle, ~Echo, ~glacier, ~goat, ~pine, ~ridge, ~snow, ~stream, ~trail, +avalanche, +cliff, +peak, +ski lift, +slope, +summit, +valley, !timberline

### FUNGI  `mushrooms_and_fungi`
- правило: Mushrooms and other fungi
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~mildew, ~mold (mold_fungus), ~mushroom, ~toadstool, ~yeast, !button mushroom, !chanterelle, !morel, !portobello, !puffball, !shiitake, !truffle

### NATURAL DISASTERS  `natural_disasters`
- правило: Destructive natural events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~drought, ~eruption, ~famine, ~flood, ~volcano, +avalanche, +blizzard, +cyclone, +earthquake, +hurricane, +landslide, +sinkhole, +tornado, +tsunami, +wildfire, !mudslide

### RIVER FEATURES  `river_features`
- правило: Parts and features of a river described in everyday English
- тип связи: `part_of`, базовая сложность 0.35
- слов: 20
- ~bank (bank_river), ~basin, ~bend, ~channel, ~current (current_water), ~delta (delta_river), ~ford (ford_river), ~gorge, ~mouth (mouth_river), ~shore, ~source, ~waterfall, !bed, !eddy, !floodplain, !headwater, !levee, !rapids, !sandbar, !tributary

### ROCKS AND MINERALS  `rocks_and_minerals`
- правило: Common rocks and minerals from the ground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~chalk (chalk_rock), ~clay, ~coal, ~quartz, ~salt, ~sandstone, +basalt, +boulder, +flint, +granite, +gravel, +gypsum, +iron ore, +limestone, +marble (marble_stone), +obsidian, +pebble, +pumice, +shale, +slate

### BEACH THINGS  `sea_shore_things`
- правило: Things you find on an ocean beach
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~cooler, ~kite (kite_toy), ~pebble, ~towel, ~umbrella, +boardwalk, +crab, +driftwood, +dune, +gull, +jellyfish, +sand, +seaweed, +shell, +starfish, +sunscreen, +surfboard, +tide, +wave (wave_water), !sandcastle

### SEASONAL WORDS  `seasons_and_nature`
- правило: Words describing the changing seasons outdoors
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~equinox, ~foliage, ~frost, ~harvest, ~migrate, ~ripen, ~shed, ~sprout, ~sunrise, ~thaw, +bloom, +blossom, +bud, +hibernate, +snowfall, +solstice, +wither, !molt

### STORMS  `storms`
- правило: Kinds of violent weather events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~thunderstorm, +blizzard, +cyclone, +downpour, +dust storm, +gale, +hurricane, +ice storm, +monsoon, +squall, +Tempest, +tornado, +typhoon, +whirlwind, !hailstorm

### FOREST THINGS  `things_in_the_forest`
- правило: Things you find walking through a forest
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~campsite, ~deer, ~Fern, ~fox, ~mushroom, ~owl, ~stream, ~trail, ~undergrowth, +acorn, +bark, +branch (branch_tree), +clearing, +leaf, +log, +moss, +squirrel, +stump, +tree, !pinecone

### GROWING THINGS  `things_that_grow`
- правило: Living things that grow larger over time
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~bud, ~crop, ~flower, ~grass, ~leaf, ~moss, ~mushroom, ~plant (plant_growth), ~root, ~tree, ~vine, ~weed, !child, !crystal, !hair, !nail (nail_body), !sapling, !seedling

### THINGS WITH SEEDS  `things_with_seeds`
- правило: Common objects or foods that naturally contain seeds
- тип связи: `has_property`, базовая сложность 0.35
- слов: 25
- ~apple (apple_fruit), ~avocado, ~bean, ~cherry, ~corn, ~cucumber, ~fig, ~grape, ~kiwi, ~melon, ~orange (orange_fruit), ~peach, ~pear, ~pepper, ~plum, ~pomegranate, ~poppy, ~pumpkin, ~sesame, ~squash (squash_vegetable), ~strawberry, ~sunflower, ~tomato, ~watermelon, !pinecone

### TREE PARTS  `tree_parts`
- правило: Physical parts of a living tree
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~bud, ~cone, ~crown (crown_tree), ~knot, ~needle (needle_pine), ~ring (ring_tree), ~shoot, +acorn, +bark (bark_tree), +bough, +branch (branch_tree), +leaf, +limb, +pulp, +root, +sap, +seed, +stump, +trunk (trunk_tree), +twig

### TREES  `trees`
- правило: Kinds of trees an average American can name
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~apple, +ash, +Aspen, +beech, +birch, +cedar, +cherry, +chestnut, +cypress, +dogwood, +elm, +fir, +hickory, +juniper, +magnolia, +maple, +oak, +palm (palm_tree), +pine, +poplar, +redwood, +spruce, +sycamore, +walnut, +Willow

### UNDERGROUND THINGS  `underground_things`
- правило: Things found under the surface of the ground
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~bulb, ~burrow, ~cave, ~coal, ~fossil, ~mine, ~mole (mole_animal), ~ore, ~pipe (pipe_tube), ~root, ~seed, ~sewer, ~Subway, ~treasure, ~tunnel, ~worm, !ant nest, !aquifer

### FORMS OF WATER  `water_states`
- правило: Forms water takes in nature
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~cloud, ~dew, ~drizzle, ~fog, ~frost, ~glacier, ~hail, ~humidity, ~ice, ~icicle, ~mist, ~puddle, ~rain, ~sleet, ~slush, ~snow, ~steam, ~vapor

### WEATHER WORDS  `weather_words`
- правило: Words describing weather conditions or events in the sky
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~shower, ~snow, ~sunshine, ~thaw, +blizzard, +breeze, +cloud, +downpour, +drizzle, +flurry, +fog, +frost, +gale, +hail, +heat wave, +humidity, +hurricane, +lightning, +mist, +rain, +sleet, +storm, +thunder, +tornado, +wind

### WILD PLANTS  `wild_plants`
- правило: Plants that grow wild in fields and woods
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bramble, ~clover, ~dandelion, ~Fern, ~Ivy, ~moss, ~reed, ~vine, ~weed, !bracken, !cattail, !goldenrod, !lichen, !milkweed, !nettle, !ragweed, !sedge, !thistle


## Тема: places

### CANADIAN PLACES  `canadian_places`
- правило: Well known places in Canada
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Alberta, +Banff, +Calgary, +Halifax, +Manitoba, +Montreal, +Niagara, +Nova Scotia, +Ottawa, +Quebec, +Toronto, +Vancouver, +Winnipeg, +Yukon

### CARIBBEAN PLACES  `caribbean_places`
- правило: Islands and countries of the Caribbean
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Cuba, +Antigua, +Aruba, +Bahamas, +Barbados, +Bermuda, +Dominica, +Grenada, +Haiti, +Jamaica, +Martinique, +Saint Lucia, +Trinidad, !Curacao

### FAMOUS BUILDINGS  `famous_buildings`
- правило: Famous buildings around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Pentagon, +Buckingham Palace, +Burj Khalifa, +Empire State, +Guggenheim, +Kremlin, +Louvre, +Notre Dame, +Parthenon, +Sydney Opera House, +Taj Mahal, +Vatican, !Petronas Towers, !Sagrada Familia

### US WATERS  `great_lakes_and_us_water`
- правило: Famous lakes and rivers in the United States
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Colorado, ~Erie, ~Michigan, ~Mississippi, ~Ohio, ~Superior, +Hudson, +Huron, +Missouri, +Ontario, +Potomac, +Powell, +Rio Grande, +Tahoe, !Okeechobee

### HIGH PLACES  `high_places`
- правило: Places high above the ground
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~attic, ~balcony (balcony_house), ~bridge (bridge_structure), ~cliff, ~crane, ~ladder, ~mountain, ~roof, ~skyscraper, ~steeple, ~summit, ~tower, !hilltop, !penthouse, !treehouse

### KINDS OF BUILDINGS  `kinds_of_buildings`
- правило: Kinds of building found in towns and cities
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~barn, ~cabin (cabin_house), ~castle, ~church, ~factory, ~garage, ~hospital, ~Hotel, ~library, ~mall, ~museum, ~school, ~stadium, ~temple, ~theater, +apartment, +bungalow, +cottage, +courthouse, +house, +mansion, +shed, +skyscraper, +tower, +warehouse

### MIDDLE EAST  `middle_east_places`
- правило: Countries and cities of the Middle East
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Jerusalem, +Baghdad, +Bahrain, +Damascus, +Iran, +Iraq, +Israel, +Jordan, +Kuwait, +Lebanon, +Oman, +Qatar, +Riyadh, +Syria, +Tehran, +Yemen

### OCEANIA PLACES  `oceania_places`
- правило: Countries and islands of Oceania
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Australia, +Fiji, +Guam, +Micronesia, +New Zealand, +Palau, +Papua New Guinea, +Samoa, +Solomon Islands, +Tahiti, +Tonga, +Vanuatu

### PLACES TO EAT  `places_to_eat`
- правило: Places where people go to eat a meal
- тип связи: `is_a`, базовая сложность 0.2
- слов: 16
- ~bakery, ~bistro, ~drive through, ~grill, +buffet, +cafe, +cafeteria, +deli, +diner, +food truck, +pizzeria, +pub, +restaurant, +snack bar, +steakhouse, +tavern

### PLACES WITH ANIMALS  `places_with_animals`
- правило: Places where animals are kept or seen
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~aquarium, ~coop, ~hive, ~pasture, ~reef, ~sanctuary, ~stable, +barn, +farm, +kennel, +pet store, +ranch, +safari, +shelter, +zoo, !aviary

### SLEEPING PLACES  `places_you_sleep`
- правило: Places where people sleep away from home
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~cabin (cabin_house), ~camper, ~cottage, ~dorm, ~hostel, ~Hotel, ~inn, ~lodge, ~motel, ~tent, !bunkhouse, !guest room, !sleeper car, !yurt

### PUBLIC ROOMS  `rooms_in_public_buildings`
- правило: Rooms found in public buildings
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~ballroom, ~cafeteria, ~chapel, ~elevator, ~gallery, ~lobby, ~office, ~restroom, ~stairwell, +auditorium, +corridor, +foyer, +hall, +storeroom, +waiting room

### SEAS  `seas_and_oceans`
- правило: Named seas of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Adriatic, +Aegean, +Arabian Sea, +Baltic, +Bering Sea, +Black Sea, +Caribbean, +Caspian, +Coral Sea, +Dead Sea, +mediterranean, +North Sea, +Red Sea, +Yellow Sea

### STATE CAPITALS  `state_capitals`
- правило: Capital cities of American states
- тип связи: `is_a`, базовая сложность 0.35
- слов: 25
- ~Austin, ~Boston, ~Columbus, ~Lincoln, ~phoenix (phoenix_city), +Albany, +Atlanta, +Augusta, +Boise, +Concord, +Denver, +Dover, +Helena, +Honolulu, +Juneau, +Lansing, +Madison, +Nashville, +Olympia, +Raleigh, +Richmond, +Sacramento, +Salem, +Topeka, +Trenton

### KINDS OF ROADS  `streets_and_roads`
- правило: Kinds of road and pathway
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +alley, +avenue, +boulevard, +bypass, +causeway, +cul de sac, +driveway, +expressway, +freeway, +highway, +lane, +path, +road, +route, +street, +trail, +turnpike, !byway

### UNDERGROUND PLACES  `underground_places`
- правило: Places that are below ground level
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~basement, ~bunker (bunker_shelter), ~burrow, ~catacomb, ~cave, ~cellar, ~crypt, ~dungeon, ~sewer, ~Subway, ~tunnel, !mine, !parking garage, !root cellar

### US LANDMARKS  `us_landmarks`
- правило: Famous landmarks in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Hollywood, ~White House, ~Yellowstone, +Alcatraz, +Everglades, +Gateway Arch, +Golden Gate, +Grand Canyon, +Liberty Bell, +Mount Rushmore, +Niagara Falls, +Space Needle, +Statue of Liberty, +Times Square, +Yosemite

### WORLD CITIES  `world_cities`
- правило: Large well known cities around the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~Munich, +Barcelona, +Bogota, +Buenos Aires, +Casablanca, +Dubai, +Geneva, +Hamburg, +Istanbul, +Jakarta, +Johannesburg, +Manchester, +Marseille, +Melbourne, +Milan, +Mumbai, +Naples, +Osaka, +Rio de Janeiro, +Santiago, +Shanghai, +Sydney, +Toronto, +Vancouver, +Venice

### FAMOUS MOUNTAINS  `world_mountains`
- правило: Famous individual mountains
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Denali, +Etna, +Everest, +Fuji, +Kilimanjaro, +Olympus, +Rainier, +Shasta, +Vesuvius, +Whitney, !Aconcagua, !Ararat, !Elbrus, !Matterhorn

### WORLD RIVERS  `world_rivers`
- правило: Major rivers outside the United States
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +Amazon, +Congo, +Danube, +Elbe, +Euphrates, +Ganges, +Loire, +Mekong, +Nile, +Po, +Rhine, +Seine, +Thames, +Tigris, +Volga, +Yangtze


## Тема: religion

### BIBLE FIGURES  `bible_figures`
- правило: People from Bible stories
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~Eve, ~Noah, +Abraham, +Adam, +Daniel, +David, +Isaac, +Jacob, +Job, +Jonah, +Joseph, +Mary, +Moses, +Paul, +Peter, +Ruth, +Samson, +Solomon

### RELIGIOUS CEREMONIES  `ceremonies`
- правило: Ceremonies performed in religious life
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~funeral, ~procession, ~wedding, +baptism, +bar mitzvah, +blessing, +communion, +confirmation, +mass, +ordination, +pilgrimage, +prayer, +sermon, +vigil

### CHURCH THINGS  `church_things`
- правило: Things found inside a church
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bell, ~candle, ~font, ~icon, ~incense, ~pulpit, ~robe, +aisle, +altar, +chalice, +choir, +cross, +offering plate, +organ (organ_music), +pew, +stained glass, +steeple, !hymnal

### AFTERLIFE WORDS  `heaven_and_afterlife`
- правило: Words about what religions say comes after death
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~angel, ~eternity, ~heaven, ~judgment, ~nirvana, ~paradise, ~reincarnation, ~resurrection, ~salvation, ~soul, ~Spirit, !ancestor, !immortality

### MONASTERY THINGS  `monastery_life`
- правило: Things found in a monastery
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~abbot, ~bell, ~chapel, ~cloister, ~library, ~manuscript, ~robe, ~silence, ~vow, !cell (cell_room), !courtyard, !garden, !refectory, !scriptorium

### PLACES OF WORSHIP  `places_of_worship`
- правило: Buildings where people gather to worship
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~tabernacle, +abbey, +basilica, +cathedral, +chapel, +church, +convent, +monastery, +mosque, +pagoda, +sanctuary, +shrine, +synagogue, +temple

### PRAYER WORDS  `prayer_words`
- правило: Words used in prayer and worship
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~meditation, ~rosary, ~vow, +amen, +blessing, +chant, +Faith, +Grace, +hymn, +kneel, +offering, +praise, +psalm, +sermon, !benediction

### SACRED TEXTS  `religious_books`
- правило: Sacred books of world religions
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- +Bible, +Exodus, +Genesis, +Gita, +gospel, +Psalms, +Quran, +Sutra, +Talmud, +Torah, +Vedas, !Avesta, !Tripitaka

### RELIGIOUS HOLIDAYS  `religious_holidays`
- правило: Holidays with religious origins
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Epiphany, +Advent, +Christmas, +Diwali, +Easter, +Eid, +Good Friday, +Hanukkah, +Lent, +Palm Sunday, +Passover, +Pentecost, +Ramadan, !Purim, !Rosh Hashanah, !Yom Kippur

### RELIGIOUS LEADERS  `religious_leaders`
- правило: Titles of religious leaders
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~abbot, ~cardinal (cardinal_church), +bishop, +chaplain, +deacon, +elder (elder_church), +imam, +minister, +missionary, +monk, +nun, +pastor, +pope, +preacher, +priest, +rabbi

### RELIGIOUS SYMBOLS  `religious_symbols`
- правило: Symbols associated with religions
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~crescent, ~cross, ~dove, ~fish, ~halo, ~rosary, ~star, ~trinity, ~wheel, +chalice, +lotus, +om, +yin yang, !ankh, !menorah

### WORLD RELIGIONS  `world_religions`
- правило: Major religions of the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~Taoism, +Buddhism, +Christianity, +Confucianism, +Hinduism, +Islam, +Judaism, +Shinto, !Bahá'í, !Jainism, !Sikhism, !Zoroastrianism


## Тема: science

### HUMAN BIOLOGY  `body_science`
- правило: Scientific words about how the human body works
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~artery, ~blood, ~bone, ~cell (cell_body), ~dna, ~enzyme, ~gene, ~hormone, ~membrane, ~muscle, ~nerve, ~organ (organ_body), ~plasma, ~protein, ~tissue (tissue_body), !immunity, !metabolism, !oxygen

### CHEMISTRY WORDS  `chemistry_words`
- правило: Words used in chemistry class
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~acid, ~atom, ~bond, ~catalyst, ~compound, ~element, ~formula, ~ion, ~mixture, ~molecule, ~reaction, ~solution, !base, !isotope, !salt, !valence

### DINOSAURS  `dinosaurs`
- правило: Dinosaur species an average person can name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~brontosaurus, ~triceratops, +raptor, +tyrannosaurus, !allosaurus, !brachiosaurus, !diplodocus, !pterodactyl, !spinosaurus, !stegosaurus, !velociraptor, xankylosaurus

### ELECTRICITY WORDS  `electricity_words`
- правило: Words used to talk about electricity
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~conductor, ~resistor, +amp, +battery, +charge, +circuit, +current (current_electric), +fuse, +generator, +outlet, +plug, +shock, +socket (socket_electric), +switch, +transformer, +voltage, +Watt, +wire

### CHEMICAL ELEMENTS  `elements`
- правило: Chemical elements an average person can name
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~calcium, ~copper, ~gold, ~iron (iron_metal), ~mercury (mercury_metal), ~neon, ~silver, ~sodium, ~zinc, +argon, +carbon (carbon_element), +chlorine, +helium, +hydrogen, +lead (lead_metal), +nitrogen, +oxygen, +potassium, +sulfur, +uranium

### ENERGY WORDS  `energy_words`
- правило: Words for kinds and sources of energy
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~coal, ~steam, ~wind, +battery, +biomass, +electric, +fuel, +gas, +geothermal, +hydro, +kinetic, +magnetic, +nuclear, +solar, +thermal

### DISSOLVING THINGS  `experiments`
- правило: Substances that dissolve in water
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~baking soda, ~candy, ~chalk (chalk_rock), ~coffee, ~gelatin, ~honey, ~ink, ~powder, ~salt, ~sugar, ~syrup, !kool aid, !soap, !tablet

### INVENTIONS  `inventions`
- правило: Famous inventions that changed everyday life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~airplane, ~battery, ~compass, ~elevator, ~engine, ~microscope, ~radio, ~refrigerator, ~telephone, ~telescope, ~vaccine, ~wheel, +camera, +computer, +internet, +lightbulb, +printing press, +television

### SCIENCE ACTIONS  `lab_actions`
- правило: Things a scientist does in an experiment
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~compare, ~freeze, ~mix, ~observe, ~predict, ~sample, ~test, ~weigh, +analyze, +boil, +dilute, +dissolve, +filter, +heat, +measure, +record

### LAB EQUIPMENT  `lab_equipment`
- правило: Equipment found in a school science laboratory
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~clamp, ~funnel, ~goggles, ~rack, ~scale (scale_weigh), ~slide, ~thermometer, ~tongs, +beaker, +burner, +centrifuge, +dropper, +flask, +magnet, +microscope, +petri dish, +stopper, +test tube, !magnifier, !pipette

### FORCES  `magnets_and_forces`
- правило: Physical forces studied in science class
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~drag, ~friction, ~gravity, ~inertia, ~lift, ~pressure, ~pull, ~push, ~tension, ~thrust, ~torque, !buoyancy, !magnetism

### MATH OPERATIONS  `math_operations`
- правило: Operations performed on numbers
- тип связи: `does_action`, базовая сложность 0.25
- слов: 15
- ~average, ~cube, ~double, ~round (round_math), ~square, +add, +calculate, +count, +divide, +estimate, +factor, +halve, +multiply, +subtract, +sum

### MATH WORDS  `math_words`
- правило: Words used in school mathematics
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~average, ~product, ~volume, +angle, +area, +decimal, +diameter, +equation, +exponent, +fraction, +integer, +percent, +perimeter, +prime, +radius, +ratio, +remainder, +square root, +sum, +variable

### METALS  `metals`
- правило: Metals and metal alloys used in everyday objects
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~magnesium, ~mercury (mercury_metal), ~pewter, ~zinc, +aluminum, +brass, +bronze, +chrome, +cobalt, +copper, +gold, +iron (iron_metal), +lead (lead_metal), +nickel, +platinum, +silver, +steel, +tin (tin_metal), +titanium, +tungsten

### TINY THINGS  `microscope_things`
- правило: Things too small to see with the naked eye
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~atom, ~bacteria, ~cell (cell_body), ~dna, ~electron, ~germ, ~microbe, ~mite, ~molecule, ~particle, ~virus, !dust mite, !pollen, !spore

### PLANETS  `planets`
- правило: Planets of our solar system
- тип связи: `is_a`, базовая сложность 0.2
- слов: 9
- +Earth, +Jupiter, +Mars, +mercury (mercury_planet), +Neptune, +Pluto, +Saturn, +Uranus, +Venus

### GEOLOGY WORDS  `rock_cycle_words`
- правило: Words used to describe the earth and its rocks
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~core, ~crust, ~erosion, ~fault, ~fossil, ~lava, ~magma, ~mineral, ~quarry, ~tectonic, ~volcano, !glacier, !mantle, !plate, !sediment, !strata

### BRANCHES OF SCIENCE  `science_fields`
- правило: Fields of scientific study
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~medicine, +anatomy, +archaeology, +astronomy, +biology, +botany, +chemistry, +ecology, +genetics, +geology, +meteorology, +physics, +psychology, +robotics, +zoology

### SHAPES  `shapes`
- правило: Geometric shapes taught in school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- ~crescent, ~diamond (diamond_shape), ~heart, ~prism, ~pyramid (pyramid_shape), ~star (star_shape), +arch (arch_structure), +circle, +cone, +cube, +cylinder, +hexagon, +octagon, +oval, +Pentagon, +rectangle, +sphere, +square, +triangle, !trapezoid

### SPACE OBJECTS  `space_objects`
- правило: Objects found in outer space
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~ring, ~supernova, +asteroid, +asteroid belt, +black hole, +cluster, +comet, +constellation, +dwarf planet, +galaxy, +meteor, +meteorite, +moon (moon_space), +nebula, +planet, +pulsar, +satellite, +star (star_space), +sun, !quasar

### STATES OF MATTER  `states_of_matter`
- правило: Physical states matter can take
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~crystal, ~foam, ~gas, ~ice, ~mist, ~plasma, ~powder, ~slush, ~solid (solid_matter), +liquid, +steam, +vapor

### TEMPERATURE WORDS  `temperature_words`
- правило: Words describing how hot or cold something is
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +blazing, +boiling, +chilly, +cold (cold_temperature), +cool, +freezing, +frigid, +frosty, +hot (hot_temperature), +icy, +lukewarm, +mild, +scalding, +sweltering, +tepid, +warm

### ASTRONOMY WORDS  `things_in_the_sky_science`
- правило: Words used by astronomers
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~rotation, +atmosphere, +comet, +constellation, +crater, +eclipse, +galaxy, +gravity, +light year, +meteor shower, +orbit, +phase, +satellite, +solar system, +telescope, +universe

### WEATHER SCIENCE  `weather_science`
- правило: Scientific words used to describe weather
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~barometer, ~front, ~pressure, ~radar, +air mass, +condensation, +dew point, +evaporation, +forecast, +humidity, +jet stream, +precipitation, !isobar, !updraft


## Тема: species

### BEARS  `bears_and_big_animals`
- правило: Kinds of bear
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- +black bear, +brown bear, +grizzly, +koala, +kodiak, +panda, +polar, +sloth bear, +sun bear, !spectacled bear

### BIRDS OF PREY  `birds_of_prey`
- правило: Birds that hunt other animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 13
- +buzzard, +condor, +eagle, +falcon, +harrier, +hawk, +kite (kite_bird), +merlin, +osprey, +owl, +vulture, !goshawk, !kestrel

### BUTTERFLIES AND MOTHS  `butterflies_and_moths`
- правило: Kinds of butterfly and moth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~admiral, ~monarch, +buckeye, +cabbage white, +gypsy moth, +luna moth, +painted lady, +skipper, +sphinx moth, +viceroy, !fritillary, !swallowtail

### CAT BREEDS  `cat_breeds`
- правило: Breeds of domestic cat
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +bengal, +bombay, +burmese, +calico, +himalayan, +maine coon, +manx, +persian, +russian blue, +siamese, +tabby, !abyssinian, !birman, !ragdoll, !sphynx

### FARM BREEDS  `cattle_and_farm_breeds`
- правило: Breeds of cattle, sheep and pigs raised on farms
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- !angus, !berkshire, !brahman, !dorset, !duroc, !guernsey, !hereford, !holstein, !jersey, !longhorn, !merino, !shorthorn, !suffolk

### DEER FAMILY  `deer_family`
- правило: Animals of the deer family
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~reindeer, +antelope, +buck, +caribou, +deer, +doe, +elk, +fawn, +gazelle, +impala, +moose, +roe deer, +stag, !muntjac

### PREHISTORIC ANIMALS  `extinct_and_prehistoric`
- правило: Animals that lived in prehistoric times
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~dodo, ~mammoth, +cave bear, +dire wolf, +giant sloth, +glyptodon, +mastodon, +saber tooth, !ammonite, !megalodon, !pterosaur, !trilobite

### CHICKEN BREEDS  `farm_poultry_breeds`
- правило: Breeds of chicken raised on farms
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- !australorp, !bantam, !brahma, !leghorn, !orpington, !plymouth rock, !rhode island red, !silkie, !sussex, !wyandotte

### FROGS AND TOADS  `frogs_and_toads`
- правило: Kinds of frog and toad
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~bullfrog, ~toad, !cane toad, !green frog, !leopard frog, !pickerel frog, !poison dart, !spring peeper, !tree frog, !wood frog

### HORSE BREEDS  `horse_breeds`
- правило: Breeds of horse
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Mustang, ~paint, ~shetland, +Arabian, +Morgan, +pinto, +quarter horse, +thoroughbred, !andalusian, !appaloosa, !clydesdale, !friesian, !palomino, !percheron

### LIZARDS  `lizards`
- правило: Kinds of lizard
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- +bearded dragon, +chameleon, +gecko, +gila monster, +horned lizard, +iguana, +komodo dragon, +salamander, !anole, !monitor (monitor_lizard), !skink

### MONKEYS AND APES  `monkeys_and_apes`
- правило: Kinds of monkey and ape
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +baboon, +chimpanzee, +gibbon, +gorilla, +howler, +lemur, +orangutan, +spider monkey, !bonobo, !capuchin, !macaque, !mandrill, !marmoset, !tamarin

### OWLS  `owls`
- правило: Kinds of owl
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- +barn owl, +barred owl, +burrowing owl, +elf owl, +great horned, +long eared, +screech owl, +snowy owl, +spotted owl, +tawny owl

### FRESHWATER FISH  `pond_fish`
- правило: Fish that live in lakes and rivers
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +bass (bass_fish), +carp, +catfish, +gar, +koi, +minnow, +perch, +pike, +sturgeon, +trout, +walleye, !bluegill, !crappie, !muskie, !sunfish

### RODENT SPECIES  `rodent_species`
- правило: Particular kinds of rodent
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +chipmunk, +field mouse, +flying squirrel, +gray squirrel, +groundhog, +house mouse, +porcupine, +prairie dog, +vole, !capybara, !dormouse, !jerboa, !lemming

### SNAKES  `snakes`
- правило: Kinds of snake
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~adder, +anaconda, +boa, +bullsnake, +cobra, +coral snake, +garter, +king snake, +mamba, +python, +rattlesnake, +viper, !copperhead, !sidewinder

### SONGBIRDS  `songbirds`
- правило: Small singing birds found in yards and woods
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~chickadee, +bluebird, +canary, +cardinal (cardinal_bird), +finch, +lark, +mockingbird, +robin, +sparrow, +starling, +swallow (swallow_bird), +thrush, +warbler, +wren, !junco, !nuthatch, !oriole

### SPIDERS AND CRAWLERS  `spiders_and_crawlers`
- правило: Small many-legged creatures that are not insects
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +Black Widow, +brown recluse, +centipede, +mite, +scorpion, +spider, +tarantula, +tick (tick_bug), +wolf spider, !daddy longlegs, !millipede, xharvestman

### WHALE TYPES  `whale_types`
- правило: Kinds of whale
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +beluga, +blue whale, +fin whale, +gray whale, +humpback, +orca, +pilot whale, +right whale, +sperm whale, !bowhead, !minke, !narwhal

### WILD DOGS  `wild_dogs`
- правило: Wild members of the dog family
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- ~jackal, +arctic fox, +coyote, +dingo, +fox, +gray wolf, +hyena, +red fox, +wolf, !fennec, !maned wolf


## Тема: transport

### AIRCRAFT  `aircraft`
- правило: Machines that fly through the air carrying people or cargo
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~drone, ~rocket, ~shuttle, +airplane, +airship, +balloon, +blimp, +cargo plane, +glider, +helicopter, +jet, +seaplane, +ultralight, +Zeppelin, !biplane

### AIRPORT WORDS  `airport_words`
- правило: Words for things, places or roles you encounter at an airport
- тип связи: `found_in`, базовая сложность 0.25
- слов: 25
- ~aisle, ~gate (gate_airport), ~passport, ~ticket (ticket_admission), +baggage, +boarding pass, +carousel, +checkpoint, +cockpit, +concourse, +control tower, +customs, +duty free, +hangar, +layover, +luggage, +pilot, +runway, +seatbelt, +security, +steward, +tarmac, +terminal, +tray table, !jetway

### BOATS AND SHIPS  `boats`
- правило: Kinds of watercraft
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~gondola, ~tugboat, +barge, +canoe, +catamaran, +cruise ship, +dinghy, +ferry, +freighter, +houseboat, +kayak, +motorboat, +raft, +sailboat, +schooner, +speedboat, +submarine, +trawler, +yacht, !rowboat

### CAR PARTS  `car_parts`
- правило: Physical parts of an ordinary passenger car
- тип связи: `part_of`, базовая сложность 0.2
- слов: 25
- ~door, ~fender, ~mirror, ~muffler, +axle, +battery, +brake, +bumper, +clutch, +dashboard, +engine, +exhaust, +headlight, +hood (hood_car), +horn (horn_sound), +ignition, +radiator, +seat, +tire, +trunk (trunk_car), +wheel, +windshield, +wiper, !gearshift, !glovebox

### CONSTRUCTION EQUIPMENT  `construction_equipment`
- правило: Large machines used on a building or road construction site
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~crane (crane_machine), ~forklift, ~jackhammer, ~roller, +bulldozer, +cement mixer, +digger, +drill rig, +dump truck, +excavator, +grader, +hoist, +loader, +scaffold, !backhoe, !compactor, !paver, !trencher

### EMERGENCY VEHICLES  `emergency_vehicles`
- правило: Vehicles used by emergency services
- тип связи: `is_a`, базовая сложность 0.25
- слов: 12
- ~ambulance, ~helicopter, +cruiser, +fire truck, +hazmat truck, +ladder truck, +paramedic van, +patrol car, +police car, +rescue boat, +squad car, +tow truck

### GAS STATION  `gas_station_things`
- правило: Things found at an American gas station
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~coffee, ~map, ~pump, ~receipt, ~restroom, ~snack, +air hose, +car wash, +credit card reader, +diesel, +gas, +ice machine, +nozzle, +oil (oil_motor), +windshield fluid, !squeegee

### TRUCKS  `heavy_trucks`
- правило: Kinds of truck used to move goods and materials
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +box truck, +cement mixer, +delivery truck, +dump truck, +flatbed, +garbage truck, +logging truck, +moving truck, +pickup, +refrigerated truck, +semi, +tanker, +tow truck, +van

### HOTEL WORDS  `hotel_words`
- правило: Things and roles found at a hotel
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~buffet, ~checkout, ~elevator, ~pool, ~reception, +balcony (balcony_house), +concierge, +front desk, +housekeeping, +key card, +lobby, +luggage cart, +room service, +suite, +vacancy, +valet, !bellhop, !minibar

### PARKING WORDS  `parking_words`
- правило: Words used about parking a car
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~curb, ~meter, ~space, ~spot, ~stall (stall_parking), ~ticket (ticket_fine), ~tow, +driveway, +garage, +handicap, +lot, +permit, +ramp, +sign, +valet, !boot (boot_clamp)

### BICYCLE PARTS  `parts_of_a_bike`
- правило: Physical parts of a bicycle
- тип связи: `part_of`, базовая сложность 0.3
- слов: 18
- ~basket, ~bell, ~brake, ~chain, ~fork, ~frame, ~saddle, ~seat, +crank, +gear, +handlebar, +pedal, +reflector, +rim, +spoke, +tire, +wheel, !kickstand

### ROAD THINGS  `road_things`
- правило: Things you see on or beside a road
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~cone, ~exit, ~ramp, ~shoulder (shoulder_road), ~tunnel, +bridge (bridge_structure), +crosswalk, +curb, +intersection, +lane, +median, +mile marker, +pothole, +sidewalk, +sign, +speed bump, +toll booth, +traffic light, !guardrail, !streetlight

### SAILING WORDS  `sailing_words`
- правило: Words used aboard a sailing boat
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~anchor, ~cabin (cabin_ship), ~deck, ~hull, ~knot, ~mast, ~oar, ~port, ~rope, ~sail (sail_cloth), ~starboard, ~stern, !boom, !bow (bow_ship), !buoy, !helm, !keel, !rudder

### SPACE TRAVEL  `space_travel`
- правило: Things involved in traveling into space
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~module, ~station (station_place), ~telescope, +astronaut, +booster, +capsule, +countdown, +docking, +gravity, +lander, +launch, +mission, +orbit, +rocket, +rover, +satellite, +shuttle, !spacesuit

### PEOPLE MOVERS  `things_that_carry_people`
- правило: Things built to carry a person from one place to another
- тип связи: `does_action`, базовая сложность 0.35
- слов: 18
- ~boat, ~bus, ~elevator, ~escalator, ~ferry, ~plane (plane_aircraft), ~taxi, ~train, ~tram, !cable car, !chairlift, !gondola, !horse, !moving walkway, !rickshaw, !sled, !stretcher, !wheelchair

### THINGS WITH WHEELS  `things_with_wheels`
- правило: Everyday objects that have wheels as a normal part of their design
- тип связи: `has_property`, базовая сложность 0.25
- слов: 25
- ~bike, ~bus, ~car, ~cart, ~dolly, ~roller skate, ~scooter, ~skateboard, ~stroller, ~suitcase, ~tractor, ~trailer (trailer_vehicle), ~train, ~tricycle, ~truck, ~unicycle, ~van, ~wagon, ~wheelbarrow, ~wheelchair, !forklift, !golf cart, !gurney, !lawnmower, !rollerblade

### TRAFFIC SIGNS  `traffic_signs`
- правило: Signs that direct drivers on the road
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~exit, ~merge, ~railroad, ~slow, ~yield, +crossing, +curve ahead, +dead end, +detour, +do not enter, +no parking, +one way, +school zone, +speed limit, +stop

### TRAIN WORDS  `train_words`
- правило: Words for the parts, places and roles of railway travel
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~depot, ~engine, ~switch, +caboose, +conductor, +coupling, +crossing, +freight, +locomotive, +platform, +rail, +sleeper car, +station (station_place), +ticket (ticket_admission), +track, +tunnel, +whistle, !boxcar

### TRAVEL THINGS  `travel_documents`
- правило: Things a traveler packs or carries on a trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- ~camera, ~map, ~sunglasses, ~ticket (ticket_admission), +adapter, +backpack, +boarding pass, +Charger, +currency, +guidebook, +insurance, +itinerary, +neck pillow, +passport, +suitcase, +toiletries, +Visa, +wallet

### VEHICLES  `vehicles`
- правило: Machines built to carry people or goods from place to place
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~ambulance, ~boat, ~canoe, ~ferry, ~helicopter, ~minivan, ~plane (plane_aircraft), ~sled, ~tractor, +bike, +bus, +car, +Jeep, +limousine, +moped, +motorcycle, +scooter, +Subway, +taxi, +train, +tram, +trolley, +truck, +van, +wagon

