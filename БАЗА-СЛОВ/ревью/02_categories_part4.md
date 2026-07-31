# Категории, часть 4 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: descriptive

### AGE WORDS  `age_words`
- правило: Words describing how old something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +aged, +ancient, +antique, +brand new, +contemporary, +fresh (fresh_new), +modern, +new, +old, +prehistoric, +secondhand, +vintage, +worn, !timeworn

### BRIGHTNESS WORDS  `brightness_words`
- правило: Words describing how much light something gives
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~blinding, ~bright, ~dazzling, ~dim, ~dull, ~faint, ~gloomy, ~glowing, ~luminous, ~murky, ~radiant, ~shady, ~shining, +dark

### CERTAINTY WORDS  `certainty_words`
- правило: Words describing how sure something is
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~definite, ~doubtful, ~guaranteed, ~obvious, ~probable, ~uncertain, ~unlikely, +certain, +likely, +maybe, +perhaps, +possible, +sure

### CLEANLINESS WORDS  `cleanliness_words`
- правило: Words describing how clean something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +clean, +dirty, +dusty, +filthy, +grimy, +immaculate, +messy, +muddy, +neat, +polished, +soiled, +spotless, +stained, +sterile, +tidy

### DIFFICULTY WORDS  `difficulty_words`
- правило: Words describing how hard a task is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +challenging, +complex, +demanding, +easy, +effortless, +grueling, +hard, +impossible, +manageable, +simple, +straightforward, +tedious, +tough, +tricky

### DISTANCE WORDS  `distance_words`
- правило: Words describing how far something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +adjacent, +alongside, +beyond, +close, +distant, +far, +faraway, +halfway, +near, +nearby, +next door, +opposite, +remote (remote_far), +within reach

### FREQUENCY WORDS  `frequency_words`
- правило: Words describing how often something happens
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +always, +annually, +constantly, +daily, +frequently, +hourly, +monthly, +never, +occasionally, +often, +rarely, +seldom, +sometimes, +weekly

### FULLNESS WORDS  `fullness_words`
- правило: Words describing how full something is
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bare, ~brimming, ~crowded, ~deserted, ~empty, ~hollow, ~jammed, ~loaded, ~overflowing, ~packed, ~sparse, ~stuffed, ~vacant, +full

### VOLUME WORDS  `noise_adjectives`
- правило: Words describing how loud something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +booming, +deafening, +faint, +hushed, +loud, +muffled, +noisy, +quiet, +roaring, +shrill, +silent, +soft, +still, +thunderous

### ORDER WORDS  `order_words`
- правило: Words describing position in a sequence
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +final, +first, +following, +former, +initial, +last, +latter, +middle, +next, +previous, +second (second_order), +subsequent, +third, +ultimate

### QUANTITY WORDS  `quantity_words`
- правило: Words describing how much of something there is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- +abundant, +batch, +bunch, +dozens, +few, +handful, +heap, +load, +many, +none, +pile, +pinch, +plenty, +scarce, +several, +some, +sprinkle, +ton

### SHAPE ADJECTIVES  `shape_adjectives`
- правило: Words describing the shape of an object
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- +bent, +crooked, +curved, +flat, +hollow, +jagged, +narrow, +oval, +pointed, +round (round_shape), +smooth, +Square, +straight, +tapered, +thick, +thin, +twisted, +wide

### SMELL WORDS  `smell_words`
- правило: Words describing how something smells
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~earthy, ~floral, ~fragrant, ~fresh (fresh_scent), ~minty, ~musty, ~pungent, ~rancid, ~smoky, ~sour, ~spicy, ~stale, +sweet, !briny, !woodsy

### SPEED WORDS  `speed_adjectives`
- правило: Words describing how fast something moves
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +brisk, +creeping, +fast, +gradual, +hasty, +leisurely, +quick, +rapid, +slow, +sluggish, +speedy, +steady, +sudden, +swift

### STRENGTH WORDS  `strength_words`
- правило: Words describing strength
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +brittle (brittle_property), +delicate, +durable, +feeble, +flimsy, +fragile, +frail, +mighty, +robust, +solid (solid_strong), +strong, +sturdy, +tough, +weak

### TASTE WORDS  `taste_words`
- правило: Words describing how food tastes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +bitter, +bland, +buttery, +creamy, +crisp, +hearty, +mild, +nutty, +peppery, +rich, +salty, +savory, +smoky, +sour, +spicy, +sweet, +syrupy, +tangy, +tart, +zesty

### TOUCH WORDS  `temperature_feel`
- правило: Words describing how something feels to touch
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~bumpy, ~cold (cold_temperature), ~damp, ~fuzzy, ~grainy, ~prickly, ~silky, ~slippery, ~spongy, ~sticky, +hard, +rough, +Sharp, +smooth, +soft, +warm

### PRICE WORDS  `value_words`
- правило: Words describing how much something costs
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +affordable, +bargain, +budget, +cheap, +costly, +discounted, +expensive, +free, +luxurious, +overpriced, +priceless, +pricey, +valuable, +worthless

### WEATHER ADJECTIVES  `weather_adjectives`
- правило: Words describing the weather outside
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +balmy, +breezy, +clear, +cloudy, +drizzly, +foggy, +freezing, +humid, +icy, +mild, +muggy, +overcast, +rainy, +snowy, +stormy, +sunny, +sweltering, +windy

### WETNESS WORDS  `wetness_words`
- правило: Words describing how wet something is
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +arid, +crisp, +damp, +dewy, +drenched, +dripping, +dry, +humid, +moist, +parched, +saturated, +soaked, +soggy, +wet


## Тема: entertainment

### AMUSEMENT PARK  `amusement_park`
- правило: Rides and things found at an amusement park
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~funhouse, ~teacups, ~turnstile, +arcade, +bumper car, +carousel, +cotton candy, +drop tower, +ferris wheel, +log flume, +mascot, +midway, +popcorn, +prize, +ride, +roller coaster, +souvenir, +ticket (ticket_admission)

### ART FORMS  `art_forms`
- правило: Forms of visual and performing art
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +calligraphy, +collage, +dance, +drawing, +film, +mosaic, +music, +origami, +painting, +photography, +poetry, +pottery, +printmaking, +sculpture, +theater, +weaving

### BOARD GAMES  `board_games`
- правило: Games played on a printed board with pieces
- тип связи: `is_a`, базовая сложность 0.25
- слов: 17
- ~mancala, +backgammon, +battleship, +candy land, +checkers, +chess, +chutes and ladders, +clue, +Life, +monopoly, +othello, +risk, +scrabble, +sorry, +trivial pursuit, +trouble, xparcheesi

### CARD GAMES  `card_games`
- правило: Games played with a deck of cards
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~bridge (bridge_card), ~canasta, ~cribbage, ~euchre, ~pinochle, +blackjack, +crazy eights, +go fish, +hearts, +old maid, +poker, +rummy, +Solitaire, +spades, +uno, +war

### CARD WORDS  `card_words`
- правило: Words for the cards, suits and parts of a standard deck of playing cards
- тип связи: `found_in`, базовая сложность 0.3
- слов: 22
- ~jack (jack_card), ~queen (queen_card), +Ace, +club (club_card), +cut, +deal, +deck, +diamond (diamond_card), +discard, +face card, +flush, +heart (heart_card), +joker, +king, +pair, +shuffle (shuffle_cards), +spade (spade_card), +straight, +suit (suit_card), +trump, +wild card, !hand (hand_cards)

### CIRCUS WORDS  `circus_words`
- правило: People, animals and objects you see at a traditional circus
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~sword swallower, +acrobat, +cannon, +clown, +cotton candy, +elephant, +juggler, +lion tamer, +net, +popcorn, +ring (ring_arena), +ringmaster, +sequin, +stilts, +tent, +tightrope, +trapeze, +unicycle

### COMEDY WORDS  `comedy_words`
- правило: Words used about comedy performances
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +gag, +heckler, +improv, +joke, +one liner, +parody, +pun, +punchline, +roast, +routine, +satire, +sketch, +slapstick, +standup, +timing

### COSTUME PARTY  `costume_party`
- правило: What you put on or need for a costume party
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~uniforms, +cape, +hats, +makeup, +mask, +superheroes, +wig

### DANCE STYLES  `dance_styles`
- правило: Styles of dance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~breakdance, +ballet, +ballroom, +cha cha, +disco, +flamenco, +folk, +foxtrot, +hip hop, +jazz, +line dance, +polka, +salsa, +samba, +swing, +tango, +tap (tap_dance), +waltz

### COMPOSERS  `famous_composers`
- правило: Famous classical composers
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Bach, +Beethoven, +Brahms, +Chopin, +Debussy, +Handel, +Haydn, +Liszt, +Mozart, +Schubert, +Tchaikovsky, +Verdi, +Vivaldi, +Wagner

### MYTHICAL CREATURES  `fantasy_creatures`
- правило: Creatures from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +centaur, +dragon, +elf, +fairy, +giant, +gnome, +goblin, +griffin, +kraken, +mermaid, +minotaur, +ogre, +pegasus, +phoenix (phoenix_bird), +sphinx, +troll, +unicorn, +vampire, +werewolf, +yeti

### ORCHESTRA SECTIONS  `instruments_in_an_orchestra`
- правило: Sections and roles in a symphony orchestra
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brass, ~cellist, ~conductor, ~ensemble, ~first violin, ~percussion, ~section, ~soloist, ~strings, ~woodwind, !concertmaster, xtimpanist

### THINGS WITH STRINGS  `instruments_you_strum`
- правило: Objects that have strings as an essential part
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~apron (apron_garment), ~balloon, ~banjo, ~bow (bow_music), ~cello, ~guitar, ~hammock, ~harp, ~kite (kite_toy), ~piano, ~puppet, ~tennis racket, ~violin, ~yo-yo, !marionette

### MAGIC SHOW  `magic_words`
- правило: Things used in a stage magic performance
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- +assistant, +box, +cape, +chain, +coin, +deck, +dove, +handcuffs, +hat, +illusion, +mirror, +rabbit, +rope, +scarf, +smoke, +top hat, +trick, +wand

### MOVIE GENRES  `movie_genres`
- правило: Categories used to classify films
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +action, +adventure, +animation, +biopic, +comedy, +documentary, +drama, +fantasy, +horror, +musical, +mystery, +noir, +romance, +satire, +sci-fi, +thriller, +war, +western

### FILM MAKING  `movie_words`
- правило: Words used in making and showing films
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +actor, +box office, +camera, +cast (cast_people), +close up, +credits, +cut, +director, +editing, +extra, +matinee, +premiere, +scene, +screenplay, +script, +sequel, +stunt, +take, +trailer (trailer_movie), !set (set_film)

### MUSIC GENRES  `music_genres`
- правило: Styles used to classify music
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~rock (rock_music), +blues, +classical, +country, +disco, +folk, +funk, +gospel, +hip hop, +indie, +jazz, +metal, +opera, +pop (pop_music), +punk, +rap, +reggae, +soul, +swing, +techno

### MUSIC WORDS  `music_words`
- правило: Words used to describe how a piece of music is written or performed
- тип связи: `found_in`, базовая сложность 0.3
- слов: 25
- ~bridge (bridge_music), +beat, +chord, +chorus, +clef, +duet, +flat, +harmony, +key (key_music), +measure, +melody, +note (note_music), +octave, +pitch (pitch_music), +refrain, +rhythm, +riff, +scale (scale_music), +Sharp, +solo, +staff, +tempo, +verse, !bar (bar_music), !rest (rest_music)

### MUSICAL INSTRUMENTS  `musical_instruments`
- правило: Instruments played to produce music
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~keyboard (keyboard_music), +accordion, +bagpipes, +banjo, +bassoon, +cello, +clarinet, +cymbal, +drum, +flute, +guitar, +harmonica, +harp, +mandolin, +oboe, +organ (organ_music), +piano, +saxophone, +tambourine, +trombone, +trumpet, +tuba, +ukulele, +violin, +xylophone

### PARTY THINGS  `party_things`
- правило: Things found at a birthday party
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~plate (plate_dish), +balloon, +banner, +cake, +candle, +candy, +confetti, +favor, +game, +guest, +invitation, +music, +napkin, +party hat, +piñata, +present (present_gift), +prize, +ribbon, +streamer, !punch (punch_drink)

### PERCUSSION INSTRUMENTS  `percussion`
- правило: Musical instruments played by striking or shaking
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~castanets, ~cowbell, ~maraca, ~marimba, ~timpani, ~xylophone, +bongo, +chime, +cymbal, +drum, +gong, +snare, +tambourine, +triangle

### READING MATTER  `reading_material`
- правило: Things people read
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +article, +blog, +book, +brochure, +comic, +diary, +label, +letter (letter_mail), +magazine, +manual, +map, +menu, +newspaper, +novel, +poem, +recipe, +script, +sign, +textbook, +ticket (ticket_admission)

### TALE CHARACTERS  `storybook_characters`
- правило: Characters that appear in classic fairy tales
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~queen (queen_royal), +dragon, +dwarf, +elf, +fairy, +frog, +genie, +giant, +goblin, +king, +knight, +mermaid, +ogre, +Prince, +princess, +troll, +unicorn, +witch, +wizard, +wolf

### STRING INSTRUMENTS  `string_instruments`
- правило: Musical instruments played by plucking or bowing strings
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~sitar, ~zither, +banjo, +bass (bass_music), +cello, +fiddle, +guitar, +harp, +harpsichord, +lute, +mandolin, +ukulele, +viola, +violin

### THEATER WORDS  `theater_words`
- правило: Words for the parts and people of a live theater production
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~playbill, +act, +aisle, +backstage, +balcony (balcony_theater), +box office, +cast (cast_people), +curtain, +encore, +intermission, +matinee, +monologue, +prop, +rehearsal, +script, +spotlight, +stage, +understudy, +usher, +wings

### TOY CHEST  `toy_chest`
- правило: What gets thrown into a child's toy chest
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +balls, +blocks, +doll, +marbles, +puzzles, +toys, !gadgets

### TOYS  `toys`
- правило: Things children play with
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~kite (kite_toy), ~marble (marble_toy), ~rattle (rattle_toy), ~top (top_spin), +action figure, +ball (ball_sphere), +blocks, +bubble, +crayon, +doll, +frisbee, +jack in the box, +jump rope, +puzzle, +robot, +Slinky, +teddy bear, +train set, +tricycle, +yo-yo

### TELEVISION WORDS  `tv_words`
- правило: Words used about television programs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +broadcast, +cable, +channel, +commercial, +episode, +finale, +network, +pilot, +ratings, +remote (remote_device), +rerun, +screen (screen_display), +sitcom, +spinoff, +streaming, +subtitle, !host (host_presenter), !season (season_time)

### GAMING WORDS  `video_game_words`
- правило: Words used when playing video games
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~respawn, +arcade, +avatar, +boss, +cheat code, +checkpoint, +console, +controller, +health bar, +joystick, +lag, +level, +loot, +multiplayer, +power up, +quest, +save, +score (score_points)

### WIND INSTRUMENTS  `wind_instruments`
- правило: Musical instruments played by blowing air
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +bagpipes, +bassoon, +clarinet, +flute, +french horn, +harmonica, +oboe, +piccolo, +recorder, +saxophone, +trombone, +trumpet, +tuba, +whistle


## Тема: farming

### BARN THINGS  `barn_things`
- правило: Things found inside a barn
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~gate (gate_barrier), ~sack (sack_bag), +bale, +bucket, +feed, +harness, +hay, +lantern, +loft, +milking stool, +pitchfork, +rope, +saddle, +shovel, +stall (stall_barn), +trough

### BEEKEEPING THINGS  `beekeeping`
- правило: Things used in beekeeping
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~queen (queen_bee), +comb, +drone, +extractor, +frame, +gloves, +hive, +honey, +pollen, +smoker, +super, +veil, +wax (wax_substance), +worker

### COUNTRY LIFE  `country_life`
- правило: Things associated with rural country living
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~hayride, +bonfire, +chores, +creek, +dirt road, +fence post, +general store, +mailbox, +pasture, +pickup truck, +pond, +porch, +rooster, +tractor, +well

### DAIRY FARM  `dairy_words`
- правило: Things involved in dairy farming
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- +barn, +calf (calf_cow), +cheese, +churn, +cream (cream_dairy), +curd, +herd, +milk, +milking machine, +pail, +separator, +udder, !butterfat, !pasteurize

### FARM BUILDINGS  `farm_buildings`
- правило: Buildings and structures on a farm
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~hayloft, ~pen (pen_animal), ~smokehouse, +barn, +coop, +corral, +dairy, +farmhouse, +fence, +granary, +greenhouse, +shed, +silo, +stable, +windmill

### FARM MACHINES  `farm_machines`
- правило: Machines used on a modern farm
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~baler, ~cultivator, ~seeder, ~thresher, +combine, +harrow, +harvester, +irrigation pump, +mower, +plow, +silo loader, +sprayer, +spreader, +tiller, +tractor

### FARM  `farm_morning`
- правило: What a farm has, keeps or fights
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- ~weeds, +barn, +livestock, +pests, +poultry, +silo, +tractor

### FARM PRODUCTS  `farm_products`
- правило: Things a farm produces to sell
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +beef, +cheese, +cider, +corn, +cotton, +eggs, +grain, +hay, +honey, +leather, +lumber, +maple syrup, +milk, +pork, +produce, +wool

### HARVEST WORDS  `harvest_words`
- правило: Words used at harvest time
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~gleaning, ~thresh, +bale, +bushel, +crop, +field, +granary, +reap, +scythe, +sheaf, +sickle, +silo, +stack (stack_pile), +wagon, +yield

### IRRIGATION THINGS  `irrigation`
- правило: Things used to water crops
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~aqueduct, ~canal, ~dam, ~ditch, ~drip line, ~furrow, ~hose, ~pipe (pipe_tube), ~pivot, ~pump, ~reservoir, ~sprinkler, ~valve, +well

### LIVESTOCK  `livestock`
- правило: Animals raised for food or farm work
- тип связи: `is_a`, базовая сложность 0.25
- слов: 17
- ~turkey (turkey_bird), +alpaca, +bison, +chicken, +cow, +donkey, +duck (duck_bird), +geese, +goat, +guinea fowl, +horse, +llama, +mule, +ox, +pig, +rabbit, +sheep

### ORCHARD WORDS  `orchard_words`
- правило: Things found in a fruit orchard
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- +basket, +bee, +blossom, +cider press, +crate, +grafting, +harvest, +ladder, +mulch, +netting, +picker, +row, +tree, !pruner

### CROP PESTS  `pest_control`
- правило: Creatures that damage crops
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~aphid, ~beetle, ~caterpillar, ~crow, ~deer, ~gopher, ~grasshopper, ~locust, ~mite, ~nematode, ~rabbit, ~slug, ~weevil, !cutworm

### RANCH WORDS  `ranch_words`
- правило: Things found on a cattle ranch
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~brand (brand_cattle), ~bunkhouse, +boot (boot_shoe), +cattle, +corral, +cowboy, +fence, +herd, +horse, +lasso, +roundup, +saddle, +spur, +stampede, +trough

### SOIL WORDS  `soil_words`
- правило: Words used to describe soil and its care
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~acidity, ~clay, ~compost, ~erosion, ~fertilizer, ~humus, ~loam, ~mulch, ~nutrient, ~plow, ~sand, ~silt, ~topsoil, !subsoil

### VINEYARD WORDS  `vineyard_words`
- правило: Things found in a vineyard
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~barrel, ~cellar, ~cluster, ~cork, ~crush, ~grape, ~harvest, ~pruning, ~terrace, ~trellis, ~vat, ~vine, !press (press_machine), !rootstock


## Тема: food_more

### CEREAL TYPES  `breakfast_cereals_types`
- правило: Kinds of breakfast cereal by form
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +bran, +clusters, +flakes, +granola, +loops, +muesli, +oatmeal, +porridge, +puffs, +shredded wheat, +squares, !crisped rice

### CANDY TYPES  `candy_shapes`
- правило: Forms candy is sold in
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~bar (bar_block), ~brittle (brittle_candy), ~stick (stick_candy), +chew, +chocolate square, +cluster, +drop, +gummy, +hard candy, +jelly, +lollipop, +mint (mint_candy), +ribbon, !ball (ball_sphere)

### CHEESE DISHES  `cheese_dishes`
- правило: Dishes built around cheese
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~gratin, ~quesadilla, +cheese board, +cheesecake, +fondue, +grilled cheese, +lasagna, +mac and cheese, +nachos, +pizza, +queso, !raclette

### COOKIE TYPES  `cookie_types`
- правило: Kinds of cookie baked at home or sold in stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~biscotti, ~macaroon, ~snickerdoodle, ~thumbprint, +chocolate chip, +fortune cookie, +gingerbread, +molasses, +oatmeal, +peanut butter, +sandwich cookie, +shortbread, +sugar, +wafer

### COOKING METHODS  `cooking_methods`
- правило: Methods used to cook food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~braise, ~saute, +bake, +barbecue, +blanch, +boil, +broil, +deep fry, +fry (fry_cook), +grill, +poach, +roast, +sear, +simmer, +slow cook, +smoke, +steam, +stir fry

### CUTS OF MEAT  `cuts_of_meat`
- правило: Cuts of meat sold by a butcher
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~ribeye, ~shoulder (shoulder_meat), +brisket, +chuck, +flank, +loin, +rib, +rump, +shank, +short rib, +sirloin, +T-bone, +tenderloin, !porterhouse, !round (round_meat)

### DESSERT TOPPINGS  `dessert_toppings`
- правило: Things put on top of desserts
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- +caramel, +cherry, +chocolate sauce, +coconut, +frosting, +fruit, +glaze, +hot fudge, +marshmallow, +nuts, +powdered sugar, +sprinkles, +syrup, +whipped cream

### DRINK MIXERS  `drink_mixers`
- правило: Things mixed into drinks
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~cream (cream_dairy), +bitters, +cola, +cranberry, +ginger ale, +ice, +juice, +lemonade, +lime, +mint (mint_herb), +soda water, +sour mix, +syrup, +tonic

### BRUNCH DISHES  `egg_and_dairy_dishes`
- правило: Dishes served at brunch
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~frittata, ~parfait, +bagel and lox, +casserole, +crepe, +eggs benedict, +french toast, +hash, +mimosa, +omelet, +quiche, +scone, +strata, +waffle

### PASTA DISHES  `pasta_dishes`
- правило: Named pasta dishes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~baked ziti, ~carbonara, ~primavera, ~puttanesca, +alfredo, +bolognese, +lasagna, +mac and cheese, +marinara, +pesto pasta, +spaghetti and meatballs, xcacio e pepe

### PIE TYPES  `pie_types`
- правило: Kinds of pie
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +apple (apple_fruit), +banana cream, +blueberry, +cherry, +chess, +chicken pot, +custard, +key lime, +lemon meringue, +mince, +peach, +pecan, +pumpkin, +rhubarb, +shepherds

### POTATO DISHES  `potato_dishes`
- правило: Ways potatoes are cooked and served
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~au gratin, ~croquette, ~tater tots, +baked, +chips, +fried, +hash browns, +home fries, +mashed, +potato salad, +scalloped, +twice baked, +wedges, !latke

### SALADS  `salads`
- правило: Named kinds of salad
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~caprese, +caesar, +chef salad, +cobb, +coleslaw, +egg salad, +fruit salad, +garden, +greek, +macaroni salad, +pasta salad, +potato salad, +spinach salad, +waldorf

### SANDWICH BREADS  `sandwich_breads`
- правило: Breads used to make a sandwich
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~ciabatta, ~focaccia, ~hoagie roll, ~white (white_food), +bagel, +brioche bun, +croissant, +english muffin, +pita, +roll (roll_bread), +rye, +sourdough, +texas toast, +wheat

### SANDWICH TYPES  `sandwich_types`
- правило: Named kinds of sandwich
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~hoagie, ~philly cheesesteak, +blt, +club (club_sandwich), +grilled cheese, +hero, +monte cristo, +panini, +patty melt, +po boy, +reuben, +sloppy joe, +wrap, xmuffuletta

### GARNISHES  `toppings_and_garnish`
- правило: Things added on top of a finished dish
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~croutons, ~scallion, +bacon bits, +cheese, +cherry, +chives, +lemon wedge, +mint leaf, +olive, +paprika, +parsley, +powdered sugar, +sesame, +sprinkles, +whipped cream


## Тема: history

### ANCIENT CIVILIZATIONS  `ancient_civilizations`
- правило: Civilizations of the ancient world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Phoenicia, ~Sumer, +Assyria, +Aztec, +Babylon, +Carthage, +China, +Egypt, +Greece, +Inca, +Maya, +Persia, +Rome, +Sparta, +Troy

### WORLD WONDERS  `ancient_wonders`
- правило: Structures known as wonders of the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- +Colosseum, +Colossus, +Great Pyramid, +Great Wall, +Hanging Gardens, +Lighthouse, +Petra, +Stonehenge, +Taj Mahal, !Chichen Itza, !Machu Picchu

### ARCHAEOLOGY WORDS  `archaeology_words`
- правило: Things involved in digging up the past
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~artifact, ~bone, ~carbon dating, ~dig, ~excavation, ~fossil, ~layer, ~pottery, ~relic, ~ruin, ~shard, ~site, ~skeleton, ~tomb, ~trowel

### CASTLE THINGS  `castle_things`
- правило: Parts and features of a medieval castle
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~battlement, ~portcullis, +armory, +banner, +chamber, +chapel, +courtyard, +drawbridge, +dungeon, +gate (gate_barrier), +hall, +keep, +moat, +rampart, +throne, +tower, +turret, +wall

### COLONIAL AMERICA  `colonial_america`
- правило: Things associated with colonial America
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~blacksmith, ~bonnet, ~churn, ~colony, ~lantern, ~musket, ~pilgrim, ~plantation, ~quill, ~settler, ~spinning wheel, ~tavern, ~wagon, !town crier, !tricorn hat

### ANCIENT EGYPT  `egypt_things`
- правило: Things associated with ancient Egypt
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~canopic jar, ~hieroglyph, ~scroll (scroll_paper), +chariot, +mummy, +Nile, +obelisk, +papyrus, +pharaoh, +pyramid (pyramid_monument), +sarcophagus, +scarab, +sphinx, +tomb, !temple (temple_building)

### AGE OF EXPLORATION  `exploration_words`
- правило: Things associated with sea exploration in the age of sail
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~sextant, +cargo, +charter, +colony, +compass, +crew, +expedition, +galleon, +harbor, +map, +sail (sail_voyage), +spice, +telescope, +trade route, +voyage

### HISTORIC DOCUMENTS  `historic_documents`
- правило: Famous documents from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 8
- +Bill of Rights, +Constitution, +Declaration of Independence, +Emancipation Proclamation, +Gettysburg Address, +Magna Carta, +Rosetta Stone, +Treaty of Versailles

### FAMOUS SHIPS  `historic_ships`
- правило: Ships famous from history
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~titanic (titanic_ship), +Ark, +beagle, +Bounty, +Constitution, +Endeavour, +Mayflower, +Nina, +Santa Maria, +Victory, !Pinta

### INDUSTRIAL AGE  `industrial_revolution`
- правило: Things associated with the industrial revolution
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~assembly line, ~canal, ~coal, ~cotton gin, ~factory, ~foundry, ~loom, ~machine, ~mill, ~railroad, ~steam engine, ~telegraph, ~worker, !smokestack

### KNIGHT THINGS  `knights_and_armor`
- правило: Things a medieval knight used or wore
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~breastplate, ~chainmail, +armor, +banner, +crest, +dagger, +gauntlet, +helmet, +horse, +lance, +saddle, +shield, +spur, +squire, +sword, +visor

### HISTORIC TRADES  `old_professions`
- правило: Trades that were common in past centuries
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~apothecary, ~blacksmith, ~chandler, ~cobbler, ~cooper, ~fletcher, ~mason, ~miller, ~potter, ~scribe, ~tanner, ~thatcher, ~weaver, !silversmith, !wheelwright

### PIRATE WORDS  `pirate_words`
- правило: Things and words associated with pirates
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~doubloon, ~hook (hook_pirate), ~spyglass, +anchor, +buccaneer, +cannon, +chest (chest_box), +compass, +crew, +eyepatch, +flag, +island, +map, +mast, +parrot, +plank, +rum, +ship, +sword, +treasure

### ANCIENT ROME  `roman_things`
- правило: Things associated with ancient Rome
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- +amphitheater, +aqueduct, +arena, +centurion, +chariot, +Colosseum, +emperor, +forum, +gladiator, +laurel, +legion, +mosaic, +senate, +toga, +villa

### ROYAL WORDS  `royalty`
- правило: Titles and things belonging to royalty
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~court (court_royal), +castle, +coronation, +crown (crown_royal), +duchess, +duke, +empire, +heir, +jewel, +king, +knight, +monarch, +palace, +Prince, +princess, +queen (queen_royal), +robe, +royal, +scepter, +throne

### BYGONE THINGS  `time_capsule_things`
- правило: Everyday objects that are no longer commonly used
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~butter churn, ~corset, ~monocle, ~oil lamp, ~phonograph, ~pocket watch, ~quill, ~spinning wheel, ~telegram, ~typewriter, ~wagon wheel, !icebox, !inkwell, !washboard

### HISTORIC TRANSPORT  `transportation_history`
- правило: Ways people traveled before cars
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~foot (foot_body), +camel, +canoe, +carriage, +chariot, +ferry, +horse, +mule, +rickshaw, +sailing ship, +sled, +stagecoach, +steamboat, +trolley, +wagon

### FAMOUS WARS  `wars`
- правило: Wars widely known from history
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- +Civil War, +Cold War, +Crusades, +Hundred Years War, +Korean War, +Revolutionary War, +Trojan War, +Vietnam, +War of 1812, +World War

### OLD WEAPONS  `weapons_of_the_past`
- правило: Weapons used before modern firearms
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~halberd, +arrow, +axe, +bow (bow_weapon), +catapult, +club (club_stick), +crossbow, +dagger, +flail, +javelin, +mace, +musket, +sling, +spear, +sword, +trident

### WILD WEST  `wild_west`
- правило: Things associated with the American Old West
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- +bandit, +boots, +cactus, +corral, +cowboy, +gold rush, +horse, +lasso, +marshal, +outlaw, +prairie, +ranch, +revolver, +rodeo, +saloon, +sheriff, +spurs, +stagecoach, +tumbleweed, +wagon


## Тема: home

### BABY THINGS  `baby_things`
- правило: Things used to care for a baby
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- ~highchair, ~monitor (monitor_medical), ~playpen, ~teether, +bib, +blanket, +bottle, +car seat, +cradle, +crib, +diaper, +formula, +onesie, +pacifier, +rattle (rattle_toy), +stroller, +swing, +wipes

### BATHROOM ITEMS  `bathroom_items`
- правило: Objects normally found in a home bathroom
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- ~cabinet (cabinet_furniture), +bathtub, +brush, +comb, +curtain, +faucet, +floss, +hairdryer, +lotion, +mat, +mirror, +plunger, +razor, +robe, +shampoo, +shower, +sink (sink_basin), +soap, +sponge (sponge_cleaning), +tissue (tissue_paper), +toilet, +toothbrush, +toothpaste, +towel, !scale (scale_weigh)

### BEDROOM THINGS  `bedroom_things`
- правило: Objects normally found in a bedroom
- тип связи: `found_in`, базовая сложность 0.2
- слов: 21
- +alarm clock, +bed, +blanket, +chest (chest_box), +closet, +comforter, +curtain, +dresser, +hamper, +hanger, +lamp, +mattress, +mirror, +nightstand, +pajamas, +pillow, +quilt, +rug, +sheet (sheet_bed), +slipper, !key (key_lock)

### CLEANING SUPPLIES  `cleaning_supplies`
- правило: Tools and products used to clean a house
- тип связи: `used_in`, базовая сложность 0.2
- слов: 20
- ~scrubber, ~squeegee, +bleach, +broom, +brush, +bucket, +cleanser, +detergent, +disinfectant, +duster, +dustpan, +gloves, +mop, +polish (polish_product), +rag, +soap, +sponge (sponge_cleaning), +trash bag, +vacuum, +wipes

### DINNER PARTY  `dinner_party`
- правило: What is set out, served or worried about at a dinner party
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 8
- ~sauces, ~seating, +centerpiece, +cocktails, +desserts, +dishes, +silverware, +toast (toast_salute)

### DISHES  `dishes_and_glassware`
- правило: Things you eat and drink from at a table
- тип связи: `is_a`, базовая сложность 0.2
- слов: 22
- ~carafe, ~desserts, ~ramekin, +bottle, +bowl, +cereal bowl, +cup, +dish, +glass, +goblet, +gravy boat, +jar, +mug, +pitcher (pitcher_jug), +plate (plate_dish), +platter, +salads, +saucer, +sugar bowl, +teapot, +tray, +tumbler

### HOME TEXTILES  `fabrics_at_home`
- правило: Cloth things used around the house
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- +apron (apron_garment), +blanket, +comforter, +curtain, +cushion cover, +doormat, +drape, +napkin, +pillowcase, +quilt, +rug, +sheet (sheet_bed), +tablecloth, +throw, +towel, !dishcloth, !placemat

### FURNITURE  `furniture`
- правило: Movable household furniture
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- ~cabinet (cabinet_furniture), ~loveseat, +armchair, +bed, +bench (bench_seat), +bookshelf, +chair, +cot, +couch, +crib, +desk, +dresser, +futon, +headboard, +hutch, +nightstand, +ottoman, +recliner, +rocker, +sideboard, +sofa, +stool, +table, +vanity, +wardrobe

### HOME DECOR  `home_decor`
- правило: What you choose when you decorate a room
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 8
- ~fabrics, +colors, +curtains, +furniture, +lighting, +patterns, +rug, +vase

### HOUSE ROOMS  `home_rooms`
- правило: Rooms and spaces inside an ordinary house
- тип связи: `part_of`, базовая сложность 0.15
- слов: 20
- +attic, +basement, +bathroom, +bedroom, +cellar, +closet, +den, +dining room, +foyer, +garage, +hallway, +kitchen, +laundry room, +living room, +loft, +nursery, +pantry, +porch, +study, +sunroom

### KITCHEN APPLIANCES  `kitchen_appliances`
- правило: Electric machines used in a kitchen
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- +air fryer, +blender, +can opener, +coffee maker, +dishwasher, +food processor, +freezer, +grill, +juicer, +kettle, +microwave, +mixer, +oven, +range (range_stove), +refrigerator, +slow cooker, +toaster, +waffle iron, +warmer, !hood (hood_kitchen)

### KITCHEN DRAWER  `kitchen_drawer`
- правило: What you find when you open a kitchen drawer
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- ~blades, ~containers, +corkscrew, +peeler, +silverware, +whisk, !fasteners

### KITCHEN TOOLS  `kitchen_tools`
- правило: Handheld tools and utensils used to prepare food in a kitchen
- тип связи: `used_in`, базовая сложность 0.15
- слов: 26
- ~masher, ~peeler, +blender, +colander, +corkscrew, +cutting board, +fork, +grater, +knife, +ladle, +measuring cup, +mixer, +opener, +pan, +plate (plate_dish), +pot, +rolling pin, +sieve, +skillet, +spatula, +spoon, +strainer, +thermometer, +timer, +tongs, +whisk

### LAUNDRY THINGS  `laundry_things`
- правило: Things used to wash and dry clothes
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~clothespin, +basket, +bleach, +detergent, +dryer, +dryer sheet, +hamper, +hanger, +iron (iron_appliance), +ironing board, +lint trap, +softener, +stain remover, +starch, +washer, !line (line_cord)

### LIGHTING  `lighting`
- правило: Devices that light a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~floodlight, ~nightlight, ~sconce, +bulb, +candle, +ceiling fan, +chandelier, +dimmer, +fixture, +flashlight, +lamp, +lantern, +shade, +spotlight, +string lights, +track light

### LIVING ROOM  `living_room_things`
- правило: Objects normally found in a living room
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~remote (remote_device), +armchair, +blanket, +bookshelf, +clock, +coffee table, +console, +curtain, +cushion, +fireplace, +lamp, +magazine, +ottoman, +painting, +rug, +sofa, +speaker, +television, +vase, !plant (plant_growth)

### HOUSE PARTS  `parts_of_a_house`
- правило: Structural parts of a house
- тип связи: `part_of`, базовая сложность 0.2
- слов: 20
- ~beam (beam_wood), ~doorframe, +ceiling, +chimney, +column, +deck, +door, +floor, +foundation (foundation_building), +gutter, +porch, +railing, +roof, +shingle, +shutter, +siding, +stairs, +threshold, +wall, +window

### PET SUPPLIES  `pet_supplies`
- правило: Things bought to keep a pet at home
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~tag (tag_label), +aquarium, +bed, +bowl, +brush, +cage, +carrier, +collar, +food, +harness, +kennel, +leash, +litter, +muzzle, +scratching post, +tank (tank_container), +toy, +treat

### HOME REPAIR  `sewing_and_repair`
- правило: Small supplies used for fixing things around the house
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~caulk, +bolt, +bracket, +glue, +hammer, +hinge, +level, +nail (nail_metal), +patch, +plunger, +putty, +sandpaper, +screw, +sealant, +tape, +washer, +wire, +wrench

### SILVERWARE  `silverware`
- правило: Eating utensils laid out at a table setting
- тип связи: `is_a`, базовая сложность 0.2
- слов: 14
- ~spork, +butter knife, +carving knife, +chopsticks, +fork, +knife, +ladle, +salad fork, +serving spoon, +skewer, +soup spoon, +spoon, +teaspoon, +tongs

### CONTAINERS  `storage_containers`
- правило: Things made to store or carry other things
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~tin (tin_can), ~trunk (trunk_case), +bag, +barrel, +basket, +bin, +box, +bucket, +canister, +carton, +case (case_box), +chest (chest_box), +cooler, +crate, +drawer, +envelope, +folder, +jar, +pouch, +sack (sack_bag)

### GARAGE THINGS  `things_in_a_garage`
- правило: Things stored in an ordinary home garage
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~jack (jack_tool), ~oil (oil_motor), +bike, +broom, +car, +cooler, +extension cord, +gas can, +hose, +ladder, +lawnmower, +paint, +rake, +shelf (shelf_furniture), +shovel, +sled, +tire, +toolbox, +wheelbarrow, +workbench

### JUNK DRAWER  `things_in_a_junk_drawer`
- правило: Small odds and ends that pile up in a kitchen drawer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~battery, ~chapstick, ~coin, ~flashlight, ~glue, ~magnet, ~matches, ~paper clip, ~pen (pen_writing), ~receipt, ~rubber band, ~scissors, ~screw, ~string, ~takeout menu, ~tape, ~twist tie, +key (key_lock)

### WALL THINGS  `things_on_a_wall`
- правило: Things hung or mounted on an interior wall
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~sconce, +antlers, +art, +calendar, +clock, +hook (hook_fastener), +mirror, +outlet, +painting, +photo, +plaque, +poster, +shelf (shelf_furniture), +switch, +tapestry, +television, +thermostat, +trophy, +wallpaper, +whiteboard

### WATER HOLDERS  `things_that_hold_water`
- правило: Containers and objects built to hold water
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~aquarium, ~barrel, ~basin, ~bathtub, ~bottle, ~bucket, ~canteen, ~jug, ~kettle, ~pot, ~sink (sink_basin), ~tank (tank_container), ~trough, ~vase, ~watering can, +cup, +glass, +pool

### OPENING THINGS  `things_that_open`
- правило: Everyday objects that open and close
- тип связи: `has_property`, базовая сложность 0.35
- слов: 20
- ~cabinet (cabinet_furniture), ~curtain, ~drawer, ~envelope, ~fan (fan_hand), ~fridge, ~gate (gate_barrier), ~jar, ~laptop, ~lid, ~mailbox, ~shell, ~suitcase, ~umbrella, ~wallet, ~zipper, +book, +box, +door, +window

### PLUGGED IN  `things_that_plug_in`
- правило: Household devices powered by plugging into an outlet
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~blender, ~Charger, ~fan (fan_device), ~freezer, ~hairdryer, ~heater, ~iron (iron_appliance), ~kettle, ~lamp, ~lampshade, ~microwave, ~printer, ~toaster, +clock, +computer, +radio, +speaker, +television, +vacuum, !drill (drill_tool)

### THINGS WITH BUTTONS  `things_with_buttons`
- правило: Everyday objects operated by pressing buttons
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~alarm clock, ~blender, ~calculator, ~cash register, ~dishwasher, ~doorbell, ~elevator, ~game controller, ~keyboard (keyboard_computer), ~microwave, ~printer, ~remote (remote_device), ~thermostat, ~vending machine, ~watch (watch_object), +camera, +phone, +radio

### TRASH THINGS  `trash_and_recycling`
- правило: Things related to household garbage and recycling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~wastebasket, +bag, +bin, +bottle, +can, +cardboard, +compost, +disposal, +dumpster, +junk, +landfill, +lid, +newspaper, +recycle, +scrap, +wrapper


## Тема: jobs

### BEAUTY JOBS  `beauty_jobs`
- правило: Jobs held by people who work on hair, nails and appearance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~colorist, ~cosmetologist, ~esthetician, ~groomer, ~manicurist, +barber, +hairdresser, +makeup artist, +masseuse, +nail tech, +stylist, +tattoo artist

### BUILDING TRADES  `building_trades`
- правило: Skilled trades that build and repair buildings
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~framer, ~glazier, ~plasterer, ~roofer, ~tiler, +bricklayer, +carpenter, +contractor, +electrician, +foreman, +installer, +laborer, +mason, +painter, +plumber, +surveyor, +welder, ?drywaller

### CIRCUS JOBS  `circus_and_fair_jobs`
- правило: Jobs held by performers and workers at a circus or fair
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~contortionist, ~stilt walker, +acrobat, +animal trainer, +barker, +clown, +fire eater, +juggler, +magician, +ringmaster, +tightrope walker, +trapeze artist

### CREATIVE JOBS  `creative_jobs`
- правило: Jobs held by people who make art or entertainment
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +actor, +animator, +artist, +choreographer, +composer, +dancer, +designer, +director, +editor, +illustrator, +musician, +painter, +photographer, +poet, +producer, +sculptor, +singer, +writer

### EMERGENCY JOBS  `emergency_jobs`
- правило: Jobs held by people who respond to emergencies
- тип связи: `is_a`, базовая сложность 0.2
- слов: 14
- +coast guard, +deputy, +dispatcher, +EMT, +firefighter, +first responder, +lifeguard, +medic, +paramedic, +police officer, +Ranger, +rescuer, +sheriff, +trooper

### LEADERSHIP TITLES  `famous_job_titles`
- правило: Titles held by people in charge of an organization
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +boss, +captain, +chairman, +chief, +coach, +commander, +dean, +director, +foreman, +head (head_leader), +manager, +mayor, +president, +principal, +supervisor, +warden

### FARM JOBS  `farm_jobs`
- правило: Jobs held by people who work on farms and with animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~milker, +beekeeper, +breeder, +dairy farmer, +farmer, +harvester, +herder, +picker, +rancher, +shepherd, +trainer, +vet, !groom (groom_horse), !hand (hand_worker)

### GOVERNMENT JOBS  `government_jobs`
- правило: Jobs held by people who work for a government
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~secretary (secretary_minister), +ambassador, +auditor, +clerk, +commissioner, +councilman, +delegate, +diplomat, +governor, +inspector, +mayor, +official, +president, +senator, +treasurer

### BYGONE JOBS  `historic_jobs`
- правило: Jobs that were common in the past but are rare today
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~blacksmith, ~chimney sweep, ~cooper, ~miller, ~scribe, ~tanner, ~telegraph operator, ~weaver, !cobbler, !ferryman, !lamplighter, !milkman, !switchboard operator, !town crier, !wheelwright

### UNIFORMED JOBS  `jobs_that_wear_uniforms`
- правило: Jobs where a uniform is normally worn to work
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~bus driver, ~chef, ~doorman, ~firefighter, ~flight attendant, ~mailman, ~nurse, ~paramedic, ~referee, ~sailor, ~soldier, ~usher, ~waiter, +pilot, +police officer, +security guard

### JOBS WITH ANIMALS  `jobs_with_animals`
- правило: Jobs held by people who work with animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~groomer, ~zookeeper, +beekeeper, +breeder, +dog walker, +falconer, +farmer, +handler, +jockey, +marine biologist, +rancher, +shepherd, +trainer, +vet, +Wrangler

### JOBS WITH TOOLS  `jobs_with_tools`
- правило: Jobs where hand tools are used every day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~barber, ~carpenter, ~chef, ~dentist, ~electrician, ~gardener, ~jeweler, ~locksmith, ~machinist, ~mechanic, ~plumber, ~sculptor, ~surgeon, ~tailor, ~welder

### KITCHEN JOBS  `kitchen_jobs`
- правило: Jobs held by people who work in a restaurant kitchen or food service
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~busser, ~sommelier, +baker, +barista, +bartender, +butcher, +caterer, +chef, +cook (cook_person), +dishwasher, +food runner, +host (host_person), +line cook, +pastry chef, +prep cook, +server, +sous chef, +waiter

### LAW JOBS  `law_jobs`
- правило: Jobs held by people who work in the legal system
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +attorney, +bailiff, +clerk, +court reporter, +defender, +investigator, +judge, +lawyer, +magistrate, +marshal, +mediator, +notary, +paralegal, +prosecutor

### MEDIA JOBS  `media_jobs`
- правило: Jobs held by people who produce news and broadcasts
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +anchor, +blogger, +broadcaster, +cameraman, +columnist, +correspondent, +critic, +editor, +journalist, +photographer, +producer, +publisher, +reporter, !host (host_presenter)

### MEDICAL JOBS  `medical_jobs`
- правило: Jobs held by people who treat patients or work in healthcare
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~podiatrist, +anesthesiologist, +cardiologist, +chiropractor, +dentist, +doctor, +hygienist, +midwife, +nurse, +nutritionist, +optometrist, +orderly, +paramedic, +pediatrician, +pharmacist, +psychiatrist, +radiologist, +surgeon, +therapist, +vet

### MILITARY RANKS  `military_ranks`
- правило: Ranks held by members of the armed forces
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +admiral, +cadet, +captain, +colonel, +commander, +corporal, +ensign, +general, +lieutenant, +major (major_rank), +officer, +private, +seaman, +sergeant

### NIGHT SHIFT  `night_shift_jobs`
- правило: Jobs commonly worked overnight
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~air traffic controller, ~baker, ~bartender, ~dispatcher, ~DJ, ~doctor, ~hotel clerk, ~janitor, ~night watchman, ~nurse, ~police officer, ~radio host, ~security guard, ~trucker

### OFFICE JOBS  `office_jobs`
- правило: Jobs held by people who work in an office
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- +accountant, +administrator, +analyst, +assistant, +auditor, +bookkeeper, +clerk, +consultant, +coordinator, +manager, +planner, +receptionist, +recruiter, +secretary (secretary_office), +supervisor, +treasurer

### HELPING PROFESSIONS  `people_who_help`
- правило: Jobs whose main purpose is helping other people directly
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +aide, +caregiver, +chaplain, +coach, +counselor, +doctor, +firefighter, +interpreter, +mentor, +nurse, +social worker, +teacher, +therapist, +volunteer

### REPAIR JOBS  `repair_jobs`
- правило: Jobs held by people who fix broken things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~upholsterer, +appliance repairman, +cobbler, +electrician, +handyman, +locksmith, +machinist, +mechanic, +plumber, +repairman, +tailor, +technician, +watchmaker, +welder

### SCHOOL JOBS  `school_jobs`
- правило: Jobs held by adults who work at a school
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~secretary (secretary_office), +aide, +bus driver, +coach, +counselor, +crossing guard, +custodian, +dean, +janitor, +librarian, +lunch lady, +nurse, +principal, +professor, +registrar, +substitute, +teacher, +tutor

### SCIENCE JOBS  `science_jobs`
- правило: Jobs held by people who do scientific work
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +archaeologist, +astronomer, +biologist, +botanist, +chemist, +ecologist, +engineer, +geologist, +lab technician, +meteorologist, +paleontologist, +physicist, +researcher, +statistician, +zoologist

### SEA JOBS  `sea_jobs`
- правило: Jobs held by people who work on the water
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~boatswain, ~whaler, +captain, +crewman, +diver, +fisherman, +lifeguard, +navigator, +oyster farmer, +pilot, +sailor, !deckhand, !harbormaster, !shipwright

### SPORTS JOBS  `sports_jobs`
- правило: Jobs held by people who work in professional sports
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~groundskeeper, +agent, +announcer, +athlete, +coach, +commentator, +manager, +mascot, +physio, +referee, +scout, +statistician, +trainer, +umpire

### STORE JOBS  `store_jobs`
- правило: Jobs held by people who work in shops and stores
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~bagger, ~greeter, ~merchandiser, ~stocker, +barber, +buyer, +cashier, +clerk, +florist, +grocer, +jeweler, +manager, +pharmacist, +salesperson, +security guard, +tailor

### TRANSPORT JOBS  `transport_jobs`
- правило: Jobs held by people who drive, fly or pilot for a living
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~ferryman, +bus driver, +captain, +chauffeur, +conductor, +courier, +delivery driver, +dispatcher, +driver, +engineer, +flight attendant, +pilot, +taxi driver, +trucker


## Тема: landmarks

### CLASSIC TV  `classic_tv_shows`
- правило: Television shows known across generations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Bonanza, +cheers (cheers_show), +Dallas, +Friends, +I Love Lucy, +Jeopardy, +mash, +Seinfeld, +Sesame Street, +Simpsons, +Star Trek, +Twilight Zone, +Wheel of Fortune, !Gunsmoke

### FAMOUS BRIDGES  `famous_bridges`
- правило: Famous bridges around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Mackinac, ~Ponte Vecchio, +Bay Bridge, +Brooklyn, +Charles Bridge, +Chesapeake, +Golden Gate, +London Bridge, +Rialto, +Sydney Harbour, +Tower Bridge, !Millau

### FAMOUS MUSEUMS  `famous_museums`
- правило: Famous museums around the world
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +British Museum, +Field Museum, +Getty, +Guggenheim, +Hermitage, +Louvre, +Met, +MoMA, +Prado, +Smithsonian, !Rijksmuseum, !Uffizi

### FAMOUS AIRCRAFT  `famous_ships_planes`
- правило: Famous aircraft from history
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- +Air Force One, +Blackbird, +Concorde, +Hindenburg, +Kitty Hawk, +Spirit of St Louis, +Spitfire, +Spruce Goose, +Zeppelin, !Enola Gay

### FAMOUS STREETS  `famous_streets`
- правило: Famous streets and avenues
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Abbey Road, +Beale Street, +Bourbon, +Bourbon Street, +Broadway, +Fifth Avenue, +Main Street, +Michigan Avenue, +Rodeo Drive, +Sunset Boulevard, +Wall Street, !Champs Elysees

### FAMOUS TOWERS  `famous_towers`
- правило: Famous towers around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Minaret, ~Petronas, +Belfry, +Bell Tower, +Big Ben, +Burj Khalifa, +CN Tower, +Eiffel, +Leaning Tower, +Space Needle, +Tokyo Tower, +Willis Tower

### FAMOUS TRAINS  `famous_trains`
- правило: Famous trains and railway lines
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- +Amtrak, +Bullet Train, +Flying Scotsman, +Metro, +Orient Express, +Rocky Mountaineer, +Trans Siberian, +Union Pacific, !Eurostar, !Ghan

### TEAM NAMES  `sports_teams`
- правило: Names of long standing American sports teams
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- +Bears, +Braves, +Broncos, +Bulls, +Celtics, +Cowboys, +Cubs, +Dodgers, +Eagles, +Giants, +Knicks, +Lakers, +Packers, +Rangers, +Red Sox, +Steelers, +Tigers, +Yankees

### THEME PARKS  `theme_parks`
- правило: Well known theme parks
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~Knotts Berry Farm, +Busch Gardens, +Cedar Point, +Disney World, +Disneyland, +Epcot, +Hershey Park, +Legoland, +Sea World, +Six Flags, +Universal Studios

### UNIVERSITIES  `universities`
- правило: Well known universities
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Berkeley, +Cambridge, +Columbia, +Cornell, +Dartmouth, +duke, +Georgetown, +Harvard, +MIT, +Notre Dame, +oxford, +Princeton, +Sorbonne, +Stanford, +Yale

### ANCIENT SITES  `world_heritage`
- правило: Famous ancient sites people visit
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Acropolis, +Angkor Wat, +Easter Island, +Ephesus, +Great Wall, +Petra, +Pompeii, +Stonehenge, +Valley of the Kings, !Chichen Itza, !Machu Picchu, !Tikal

### FAMOUS ZOOS  `zoos_and_aquariums`
- правило: Well known zoos and aquariums
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- +Berlin Zoo, +Bronx Zoo, +Georgia Aquarium, +Lincoln Park, +London Zoo, +Monterey Bay, +National Zoo, +San Diego Zoo, +Toronto Zoo, !Shedd


## Тема: law

### COURTROOM  `courtroom`
- правило: What is heard, handed down or worn in a courtroom
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- +crimes, +gavel, +jury, +penalties, +rights, +verdict, !titles

### COURTROOM THINGS  `courtroom_things`
- правило: Things and people found in a courtroom
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bench (bench_court), ~sentence (sentence_punishment), ~stand (stand_witness), +bailiff, +defendant, +docket, +evidence, +exhibit, +gavel, +judge, +jury, +lawyer, +oath, +plaintiff, +testimony, +transcript, +verdict, +witness

### CRIMES  `crimes`
- правило: Acts that are against the law
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +arson, +blackmail, +bribery, +burglary, +counterfeiting, +embezzlement, +forgery, +fraud, +kidnapping, +littering, +perjury, +poaching, +shoplifting, +smuggling, +speeding, +theft, +trespassing, +vandalism

### DETECTIVE WORDS  `detective_words`
- правило: Words used in a criminal investigation
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~case (case_legal), ~stakeout, +alibi, +autopsy, +clue, +evidence, +fingerprint, +footprint, +forensics, +interrogation, +lineup, +motive, +suspect, +warrant, +witness, !lead (lead_clue)

### EMERGENCY SERVICES  `emergency_services`
- правило: Public services that respond to emergencies
- тип связи: `is_a`, базовая сложность 0.25
- слов: 12
- +ambulance, +animal control, +coast guard, +dispatch, +fire department, +hazmat, +hospital, +poison control, +police, +Ranger, +rescue squad, +search and rescue

### GOVERNMENT WORDS  `government_branches`
- правило: Words for the parts and workings of government
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~bill (bill_law), ~cabinet (cabinet_government), ~term (term_period), +amendment, +ballot, +budget, +campaign, +committee, +congress, +election, +house, +law, +majority, +senate, +session, +treaty, +veto, +vote

### LEGAL DOCUMENTS  `legal_documents`
- правило: Documents used in legal matters
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +affidavit, +certificate, +contract, +deed, +lease, +license, +patent, +permit, +petition, +subpoena, +summons, +testament, +title, +waiver, +warrant, +will

### MILITARY BRANCHES  `military_branches`
- правило: Branches of the armed forces
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +air force, +army, +artillery, +cavalry, +coast guard, +infantry, +marines, +militia, +national guard, +navy, +reserves, +space force

### MILITARY EQUIPMENT  `military_things`
- правило: Equipment used by the armed forces
- тип связи: `used_in`, базовая сложность 0.3
- слов: 19
- +backpack, +binoculars, +boots, +bunker (bunker_shelter), +camouflage, +canteen, +compass, +dog tag, +helmet, +Jeep, +jet, +medal, +parachute, +radio, +ration, +rifle, +submarine, +tank (tank_military), +uniform

### MILITARY WORDS  `military_words`
- правило: Words used in military life
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~march (march_walk), ~reveille, +barracks, +base, +boot camp, +deploy, +drill (drill_practice), +formation, +leave, +mission, +patrol, +platoon, +rank, +roll call, +salute, +squad

### POLICE THINGS  `police_things`
- правило: Equipment and things used by police
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- +badge, +baton, +cruiser, +dispatch, +flashlight, +handcuffs, +holster, +k9, +patrol, +radio, +siren, +ticket (ticket_fine), +uniform, +vest, +warrant, +whistle

### PRISON WORDS  `prison_words`
- правило: Things and words associated with prison
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~cellmate, ~sentence (sentence_punishment), +bail, +bars, +bunk, +cell (cell_room), +guard (guard_prison), +inmate, +lockdown, +mess hall, +parole, +release, +uniform, +visitation, +warden, !yard (yard_ground)

### PENALTIES  `punishments`
- правило: Penalties handed down for breaking rules
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +ban, +community service, +curfew, +detention, +expulsion, +fine, +forfeit, +jail, +penalty, +probation, +restitution, +suspension, +ticket (ticket_fine), +warning

### RIGHTS  `rights_and_freedoms`
- правило: Legal rights and freedoms people have
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +appeal, +assembly, +bear arms, +counsel, +due process, +equality, +petition, +privacy, +protest, +religion, +speech, +trial, +vote, !press (press_media)

### SAFETY WORDS  `safety_signs`
- правило: Words seen on warning and safety signs
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +biohazard, +caution, +danger, +emergency, +exit, +flammable, +hazard, +high voltage, +keep out, +no entry, +poison, +restricted, +slippery, +stop, +warning, +yield

### SPY WORDS  `spy_words`
- правило: Things associated with spies and espionage
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~mole (mole_spy), +agent, +alias, +bug, +cipher, +code, +decoder, +disguise, +dossier, +informant, +microfilm, +mission, +safe house, +surveillance, +tail


## Тема: mythology

### FOLK HEROES  `american_legends`
- правило: Legendary figures from American folklore
- тип связи: `is_a`, базовая сложность 0.4
- слов: 9
- +Big Foot, +Davy Crockett, +John Henry, +Paul Bunyan, +Pecos Bill, +Rip Van Winkle, +Sasquatch, +Uncle Sam, !Johnny Appleseed

### TALE OBJECTS  `fairy_tale_things`
- правило: Objects that appear in classic fairy tales
- тип связи: `found_in`, базовая сложность 0.25
- слов: 14
- ~beanstalk, ~breadcrumb, +cottage, +gingerbread house, +glass slipper, +golden egg, +harp, +magic mirror, +porridge, +pumpkin coach, +red hood, +spinning wheel, +tower, !apple (apple_fruit)

### FORTUNE TELLING  `fortune_telling`
- правило: Things used to tell fortunes
- тип связи: `used_in`, базовая сложность 0.4
- слов: 13
- ~cards, ~crystal ball, ~dice (dice_game), ~horoscope, ~omen, ~Oracle, ~pendulum, ~rune, ~tarot, ~tea leaves, +dream, +stars, !palm (palm_hand)

### GREEK GODS  `greek_gods`
- правило: Gods and goddesses of Greek mythology
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Demeter, ~Hephaestus, ~Hestia, +Aphrodite, +Apollo, +Ares, +Artemis, +Athena, +Dionysus, +Hades, +Hera, +Hermes, +Persephone, +Poseidon, +Zeus

### MYTHOLOGICAL HEROES  `greek_heroes`
- правило: Heroes of classical mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +Achilles, +Aeneas, +Ajax, +Atalanta, +Hector, +Hercules, +Jason, +Odysseus, +Orpheus, +Paris, +Perseus, +Theseus

### LEGENDARY PLACES  `legendary_places`
- правило: Places known only from myth and legend
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Asgard, +Atlantis, +Avalon, +Camelot, +Eden, +El Dorado, +Hades, +Olympus, +Shangri-La, +Troy, +Valhalla, +Xanadu

### MAGICAL BEINGS  `magic_creatures`
- правило: Magical beings from folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- +banshee, +brownie, +dwarf, +elf, +fairy, +genie, +gnome, +goblin, +imp, +leprechaun, +nymph, +pixie, +Sprite, +troll, +witch, +wizard

### MAGIC OBJECTS  `magic_objects`
- правило: Objects with magical powers in stories
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~spellbook, +amulet, +broomstick, +cauldron, +charm, +cloak, +crystal ball, +elixir, +lamp, +magic carpet, +mirror, +potion, +sword, +talisman, +wand, !ring (ring_jewelry)

### SCARY CREATURES  `monsters`
- правило: Frightening creatures from stories and folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- +banshee, +bogeyman, +demon, +ghost, +ghoul, +goblin, +gremlin, +monster, +mummy, +phantom, +poltergeist, +vampire, +werewolf, +witch, +zombie

### MYTHICAL MONSTERS  `mythical_monsters`
- правило: Monsters from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~basilisk, ~manticore, +banshee, +cerberus, +chimera, +cyclops, +gorgon, +harpy, +hydra, +kraken, +medusa, +minotaur, +siren, +sphinx

### NORSE GODS  `norse_gods`
- правило: Gods of Norse mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Balder, ~Frigg, ~Heimdall, ~Vidar, +Freya, +Hel, +Loki, +Odin, +Thor, +Tyr, !Njord, xIdun

### ROMAN GODS  `roman_gods`
- правило: Gods and goddesses of Roman mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Apollo, +Bacchus, +Ceres, +Diana, +Juno, +Jupiter, +Mars, +mercury (mercury_god), +Minerva, +Neptune, +Pluto, +Saturn, +Venus, +Vulcan

### SUPERSTITION THINGS  `superstitions`
- правило: Objects tied to common superstitions
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~black cat, ~broken mirror, ~four leaf clover, ~horseshoe, ~knock on wood, ~ladder, ~mirror, ~penny, ~rabbit foot, ~salt, ~umbrella, ~wishbone, +cross

### WIZARD WORDS  `wizards_and_spells`
- правило: Things belonging to a wizard in stories
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~scroll (scroll_paper), +apprentice, +book, +cauldron, +crystal, +familiar, +hat, +incantation, +potion, +robe, +spell (spell_magic), +staff, +tower, +wand

### ZODIAC SIGNS  `zodiac_signs`
- правило: Signs of the astrological zodiac
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +Aquarius, +Aries, +cancer, +Capricorn, +Gemini, +Leo, +Libra, +Pisces, +Sagittarius, +Scorpio, +Taurus, +Virgo


## Тема: nature_species

### BEETLES  `beetles`
- правило: Kinds of beetle
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~carpet beetle, ~click beetle, ~dung beetle, ~firefly, ~june bug, ~ladybug, ~scarab, ~stag beetle, ~water beetle, !boll weevil, !rhinoceros beetle, !weevil

### GARDEN BUGS  `garden_bugs`
- правило: Small creatures found in a garden
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~aphid, ~roly poly, +ant, +bee, +beetle, +caterpillar, +centipede, +cricket, +earthworm, +earwig, +grub, +ladybug, +praying mantis, +slug, +snail, +spider

### MOSS & LICHEN  `mosses_and_lichens`
- правило: Small plants that grow on rocks and bark
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- ~algae, ~fungus, ~moss, !lichen, !reindeer moss, !sphagnum, xcrustose, xfoliose, xhornwort, xliverwort

### CONIFER WORDS  `pine_and_cones`
- правило: Words about pine trees and their cones
- тип связи: `found_in`, базовая сложность 0.5
- слов: 14
- ~bark (bark_tree), ~cluster, ~cone, ~evergreen, ~fir, ~needle (needle_pine), ~resin, ~sap, ~scent, ~seed, ~spruce, ~timber, !bough, !pitch (pitch_tar)

### SALTWATER FISH  `saltwater_fish`
- правило: Fish that live in salt water
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~hake, ~mahi mahi, ~pompano, ~tarpon, +bonito, +cod, +grouper, +mackerel, +sea bass, +snapper, +sole (sole_fish), +tuna, +wahoo, !amberjack, !bluefish

### WILDFLOWERS  `wildflowers`
- правило: Flowers that grow wild in fields and roadsides
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~chicory, ~milkweed, ~trillium, +aster, +black eyed susan, +columbine, +indian paintbrush, +primrose, +wild rose, !bloodroot, !bluebonnet, !coneflower, !goldenrod, !queen annes lace


## Тема: people

### FAMOUS PAINTERS  `artists`
- правило: Famous painters from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Cezanne, +Da Vinci, +Dali, +Degas, +Matisse, +Michelangelo, +Monet, +Picasso, +Pollock, +Rembrandt, +Renoir, +Van Gogh, +Vermeer, +Warhol

### FAMOUS AUTHORS  `authors`
- правило: Famous authors from literature
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +Austen, +Bronte, +Dickens, +Fitzgerald, +Hemingway, +Kipling, +Melville, +Orwell, +Poe, +Shakespeare, +Steinbeck, +Tolkien, +Twain, +Verne, +Wilde

### BODY LANGUAGE  `body_language`
- правило: Gestures people make with the body to communicate
- тип связи: `does_action`, базовая сложность 0.4
- слов: 15
- ~bow (bow_bend), ~clap, ~cross arms, ~fist bump, ~handshake, ~hug, ~nod, ~point (point_gesture), ~salute, ~shake head, ~shrug, ~thumbs up, ~wave (wave_hand), +high five, !curtsy

### BOYS NAMES  `boys_names`
- правило: Common first names given to boys in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~jack (jack_name), +Andrew, +Benjamin, +Christopher, +Daniel, +David, +Ethan, +Henry, +Jacob, +James, +John, +Joseph, +Liam, +Lucas, +mason, +Matthew, +Michael, +Nathan, +Noah, +Owen, +Robert, +Ryan, +Samuel, +Thomas, +William

### AUDIENCE WORDS  `crowd_words`
- правило: Words for people watching an event
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~attendee, ~audience, ~bystander, ~crowd, ~guest, ~listener, ~patron, ~spectator, ~subscriber, ~viewer, ~witness, !fan (fan_person), !onlooker

### EXPLORERS  `explorers`
- правило: Famous explorers from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Amundsen, ~Vespucci, +Balboa, +Cabot, +Clark, +Columbus, +Cortes, +Hudson, +Lewis, +Livingstone, +Magellan, +Marco Polo, +Shackleton, !cook (cook_explorer)

### FACIAL EXPRESSIONS  `facial_expressions`
- правило: Expressions people make with their face
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- +beam (beam_smile), +blink, +blush, +frown, +gape, +glare, +grimace, +grin, +pout, +scowl, +smile, +smirk, +sneer, +wink, +yawn

### FAMILY MEMBERS  `family_members`
- правило: Words for members of a family
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- +aunt, +brother, +child, +cousin, +daughter, +father, +godmother, +grandchild, +grandfather, +grandmother, +husband, +in law, +mother, +nephew, +niece, +parent, +sibling, +sister, +son, +spouse, +stepfather, +stepmother, +twin, +uncle, +wife

### FAMOUS AMERICANS  `famous_americans`
- правило: Americans widely known from history
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~ford (ford_person), +Armstrong, +Carver, +Disney, +Douglass, +Earhart, +Edison, +Franklin, +Jefferson, +Keller, +Kennedy, +Lincoln, +Parks, +Roosevelt, +Tubman, +Twain, +Washington, +Wright

### FEELINGS  `feelings`
- правило: Words naming human emotions
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~calm (calm_person), +angry, +anxious, +bored, +confused, +content, +curious, +embarrassed, +excited, +frustrated, +grateful, +guilty, +happy, +hopeful, +jealous, +joyful, +lonely, +nervous, +proud, +relieved, +sad, +scared, +surprised, +tired, +worried

### GIRLS NAMES  `girls_names`
- правило: Common first names given to girls in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- +Abigail, +Amelia, +Ava, +Charlotte, +Chloe, +Elizabeth, +Ella, +Emily, +Emma, +Grace, +Hannah, +Isabella, +Jennifer, +Lily, +Linda, +Madison, +Mary, +Mia, +Natalie, +Olivia, +Rachel, +Sarah, +Sophia, +Susan, +Zoe

### GROUPS OF PEOPLE  `groups_of_people`
- правило: Words for gatherings of people
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +audience, +band (band_group), +cast (cast_people), +choir, +class, +committee, +congregation, +council, +crew, +crowd, +gang, +jury, +mob, +panel, +squad, +staff, +team, +tribe, +troop, !party (party_group)

### HALL OF FAME  `hall_of_fame`
- правило: Who gets remembered and what marks the honour
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 7
- ~composers, ~legend, +awards, +bust, +explorers, +inventors, +plaque

### INVENTORS  `inventors`
- правило: Famous inventors
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~ford (ford_person), +bell, +diesel, +Edison, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Tesla, +Watt, +Whitney, +Wright, !Daguerre

### STAGES OF LIFE  `life_stages`
- правило: Words for the stages of a human life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~preschooler, +adolescent, +adult, +baby, +child, +elder (elder_person), +grownup, +infant, +middle age, +newborn, +retiree, +senior, +teenager, +toddler, +youth

### NATIONALITIES  `nationalities`
- правило: Words for people from a particular country
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~polish (polish_language), +American, +Australian, +Brazilian, +Canadian, +Chinese, +Dutch, +Egyptian, +French, +German, +greek, +Indian, +Irish, +Italian, +Japanese, +Korean, +Mexican, +Russian, +spanish, +Swedish

### NICKNAMES  `nicknames`
- правило: Short familiar forms of common first names
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~bill (bill_name), +Andy, +Ben, +bob, +Chris, +Dave, +Jim, +Joe, +Kate, +Liz, +Meg, +Mike, +Nick, +Pat, +Peg, +Rick, +Sam, +Sue, +Ted, +tom

### WEDDING PEOPLE  `people_at_a_wedding`
- правило: People with a role at a wedding
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~groom (groom_wedding), ~officiant, +best man, +bride, +bridesmaid, +caterer, +DJ, +father of the bride, +flower girl, +guest, +maid of honor, +photographer, +ring bearer, +usher

### STORY CHARACTERS  `people_in_a_story`
- правило: Character roles found in stories
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +detective, +guardian, +hero, +mentor, +narrator, +orphan, +outlaw, +protagonist, +rival, +sidekick, +stranger, +victim, +villain, +witness

### PERSONALITY WORDS  `personality_words`
- правило: Words describing a person character
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bold (bold_brave), +brave, +calm (calm_person), +careful, +cheerful, +clever, +curious, +funny, +generous, +gentle, +honest, +loyal, +patient, +quiet, +sensible, +serious, +shy, +stubborn

### RELATIONSHIP WORDS  `relationships`
- правило: Words for how people are connected to each other
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- ~host (host_person), +acquaintance, +Ally, +boss, +classmate, +client, +colleague, +coworker, +friend, +guest, +mentor, +neighbor, +partner, +rival, +roommate, +stranger, +teammate

### FAMOUS SCIENTISTS  `scientists`
- правило: Famous scientists from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Archimedes, +Bohr, +Copernicus, +Curie, +Darwin, +Einstein, +Faraday, +Fleming, +Galileo, +Hawking, +Kepler, +Mendel, +Newton, +Pasteur

### TITLES  `titles_of_address`
- правило: Titles put before a person name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +captain, +chief, +coach, +dean, +doctor, +judge, +lady, +lord, +madam, +miss, +missus, +mister, +officer, +professor, +reverend, +senator, +sergeant, +sir

### US PRESIDENTS  `us_presidents`
- правило: Presidents of the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +Adams, +Bush, +Carter, +Clinton, +Eisenhower, +Grant, +Jackson, +Jefferson, +Johnson, +Kennedy, +Lincoln, +Madison, +Monroe, +Nixon, +Obama, +Reagan, +Roosevelt, +Truman, +Washington, +Wilson


## Тема: places

### BEACH DAY  `beach_day`
- правило: What you bring to the beach or find while you are there
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- ~eyewear, ~shellfish, +seabirds, +sunscreen, +swimwear, +towel, +umbrella

### CANADIAN PLACES  `canadian_places`
- правило: Well known places in Canada
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Alberta, +Banff, +Calgary, +Halifax, +Manitoba, +Montreal, +Niagara, +Nova Scotia, +Ottawa, +Quebec, +Toronto, +Vancouver, +Winnipeg, +Yukon

### CARIBBEAN PLACES  `caribbean_places`
- правило: Islands and countries of the Caribbean
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Curacao, +Antigua, +Aruba, +Bahamas, +Barbados, +Bermuda, +Cuba, +Dominica, +Grenada, +Haiti, +Jamaica, +Martinique, +Saint Lucia, +Trinidad

### FAMOUS BUILDINGS  `famous_buildings`
- правило: Famous buildings around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Petronas Towers, ~Sagrada Familia, +Buckingham Palace, +Burj Khalifa, +Empire State, +Guggenheim, +Kremlin, +Louvre, +Notre Dame, +Parthenon, +Pentagon, +Sydney Opera House, +Taj Mahal, +Vatican

### US WATERS  `great_lakes_and_us_water`
- правило: Famous lakes and rivers in the United States
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Okeechobee, +Colorado, +Erie, +Hudson, +Huron, +Michigan, +Mississippi, +Missouri, +Ohio, +Ontario, +Potomac, +Powell, +Rio Grande, +Superior, +Tahoe

### HIGH PLACES  `high_places`
- правило: Places high above the ground
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~attic, ~balcony (balcony_house), ~bridge (bridge_structure), ~cliff, ~crane (crane_machine), ~hilltop, ~ladder, ~penthouse, ~skyscraper, ~steeple, ~summit, ~tower, ~treehouse, +mountain, +roof

### KINDS OF BUILDINGS  `kinds_of_buildings`
- правило: Kinds of building found in towns and cities
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~cabin (cabin_house), ~temple (temple_building), +apartment, +barn, +bungalow, +castle, +church, +cottage, +courthouse, +factory, +garage, +hospital, +Hotel, +house, +library, +mall, +mansion, +museum, +school, +shed, +skyscraper, +stadium, +theater, +tower, +warehouse

### MIDDLE EAST  `middle_east_places`
- правило: Countries and cities of the Middle East
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Baghdad, +Bahrain, +Damascus, +Iran, +Iraq, +Israel, +Jerusalem, +Jordan, +Kuwait, +Lebanon, +Oman, +Qatar, +Riyadh, +Syria, +Tehran, +Yemen

### OCEANIA PLACES  `oceania_places`
- правило: Countries and islands of Oceania
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Australia, +Fiji, +Guam, +Micronesia, +New Zealand, +Palau, +Papua New Guinea, +Samoa, +Solomon Islands, +Tahiti, +Tonga, +Vanuatu

### PLACES TO EAT  `places_to_eat`
- правило: Places where people go to eat a meal
- тип связи: `is_a`, базовая сложность 0.2
- слов: 16
- +bakery, +bistro, +buffet, +cafe, +cafeteria, +deli, +diner, +drive through, +food truck, +grill, +pizzeria, +pub, +restaurant, +snack bar, +steakhouse, +tavern

### PLACES WITH ANIMALS  `places_with_animals`
- правило: Places where animals are kept or seen
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~aviary, +aquarium, +barn, +coop, +farm, +hive, +kennel, +pasture, +pet store, +ranch, +reef, +safari, +sanctuary, +shelter, +stable, +zoo

### SLEEPING PLACES  `places_you_sleep`
- правило: Places where people sleep away from home
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~bunkhouse, ~cabin (cabin_house), ~camper, ~dorm, ~hostel, ~motel, ~sleeper car, ~yurt, +cottage, +guest room, +Hotel, +inn, +lodge, +tent

### PUBLIC ROOMS  `rooms_in_public_buildings`
- правило: Rooms found in public buildings
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- +auditorium, +ballroom, +cafeteria, +chapel, +corridor, +elevator, +foyer, +gallery, +hall, +lobby, +office, +restroom, +stairwell, +storeroom, +waiting room

### SEAS  `seas_and_oceans`
- правило: Named seas of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Adriatic, +Aegean, +Arabian Sea, +Baltic, +Bering Sea, +Black Sea, +Caribbean, +Caspian, +Coral Sea, +Dead Sea, +mediterranean, +North Sea, +Red Sea, +Yellow Sea

### STATE CAPITALS  `state_capitals`
- правило: Capital cities of American states
- тип связи: `is_a`, базовая сложность 0.35
- слов: 25
- ~phoenix (phoenix_city), +Albany, +Atlanta, +Augusta, +Austin, +Boise, +Boston, +Columbus, +Concord, +Denver, +Dover, +Helena, +Honolulu, +Juneau, +Lansing, +Lincoln, +Madison, +Nashville, +Olympia, +Raleigh, +Richmond, +Sacramento, +Salem, +Topeka, +Trenton

### KINDS OF ROADS  `streets_and_roads`
- правило: Kinds of road and pathway
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~byway, +alley, +avenue, +boulevard, +bypass, +causeway, +cul de sac, +driveway, +expressway, +freeway, +highway, +lane, +path, +road, +route, +street, +trail, +turnpike

### UNDERGROUND PLACES  `underground_places`
- правило: Places that are below ground level
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~basement, ~bunker (bunker_shelter), ~burrow, ~catacomb, ~cave, ~cellar, ~crypt, ~dungeon, ~parking garage, ~root cellar, ~sewer, ~Subway, ~tunnel, +mine

### US LANDMARKS  `us_landmarks`
- правило: Famous landmarks in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +Alcatraz, +Everglades, +Gateway Arch, +Golden Gate, +Grand Canyon, +Hollywood, +Liberty Bell, +Mount Rushmore, +Niagara Falls, +Space Needle, +Statue of Liberty, +Times Square, +White House, +Yellowstone, +Yosemite

### WORLD CITIES  `world_cities`
- правило: Large well known cities around the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Barcelona, +Bogota, +Buenos Aires, +Casablanca, +Dubai, +Geneva, +Hamburg, +Istanbul, +Jakarta, +Johannesburg, +Manchester, +Marseille, +Melbourne, +Milan, +Mumbai, +Munich, +Naples, +Osaka, +Rio de Janeiro, +Santiago, +Shanghai, +Sydney, +Toronto, +Vancouver, +Venice

### FAMOUS MOUNTAINS  `world_mountains`
- правило: Famous individual mountains
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Ararat, ~Matterhorn, +Denali, +Etna, +Everest, +Fuji, +Kilimanjaro, +Olympus, +Rainier, +Shasta, +Vesuvius, +Whitney, !Aconcagua, !Elbrus

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
- +Abraham, +Adam, +Daniel, +David, +Eve, +Isaac, +Jacob, +Job, +Jonah, +Joseph, +Mary, +Moses, +Noah, +Paul, +Peter, +Ruth, +Samson, +Solomon

### RELIGIOUS CEREMONIES  `ceremonies`
- правило: Ceremonies performed in religious life
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +baptism, +bar mitzvah, +blessing, +communion, +confirmation, +funeral, +mass, +ordination, +pilgrimage, +prayer, +procession, +sermon, +vigil, +wedding

### CHURCH THINGS  `church_things`
- правило: Things found inside a church
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~hymnal, +aisle, +altar, +bell, +candle, +chalice, +choir, +cross, +font, +icon, +incense, +offering plate, +organ (organ_music), +pew, +pulpit, +robe, +stained glass, +steeple

### AFTERLIFE WORDS  `heaven_and_afterlife`
- правило: Words about what religions say comes after death
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~ancestor, ~angel, ~eternity, ~heaven, ~immortality, ~judgment, ~nirvana, ~paradise, ~reincarnation, ~resurrection, ~salvation, +soul, +Spirit

### MONASTERY THINGS  `monastery_life`
- правило: Things found in a monastery
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~abbot, ~bell, ~chapel, ~cloister, ~courtyard, ~garden, ~library, ~manuscript, ~robe, ~silence, ~vow, !cell (cell_room), !refectory, !scriptorium

### PLACES OF WORSHIP  `places_of_worship`
- правило: Buildings where people gather to worship
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +abbey, +basilica, +cathedral, +chapel, +church, +convent, +monastery, +mosque, +pagoda, +sanctuary, +shrine, +synagogue, +tabernacle, +temple (temple_building)

### PRAYER WORDS  `prayer_words`
- правило: Words used in prayer and worship
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~benediction, +amen, +blessing, +chant, +Faith, +Grace, +hymn, +kneel, +meditation, +offering, +praise, +psalm, +rosary, +sermon, +vow

### SACRED TEXTS  `religious_books`
- правило: Sacred books of world religions
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~Avesta, ~Tripitaka, +Bible, +Exodus, +Genesis, +Gita, +gospel, +Psalms, +Quran, +Sutra, +Talmud, +Torah, +Vedas

### RELIGIOUS HOLIDAYS  `religious_holidays`
- правило: Holidays with religious origins
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Purim, ~Rosh Hashanah, ~Yom Kippur, +Advent, +Christmas, +Diwali, +Easter, +Eid, +Epiphany, +Good Friday, +Hanukkah, +Lent, +Palm Sunday, +Passover, +Pentecost, +Ramadan

### RELIGIOUS LEADERS  `religious_leaders`
- правило: Titles of religious leaders
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~cardinal (cardinal_church), +abbot, +bishop, +chaplain, +deacon, +elder (elder_church), +imam, +minister, +missionary, +monk, +nun, +pastor, +pope, +preacher, +priest, +rabbi

### RELIGIOUS SYMBOLS  `religious_symbols`
- правило: Symbols associated with religions
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~ankh, ~menorah, ~star (star_shape), +chalice, +crescent, +cross, +dove, +fish, +halo, +lotus, +om, +rosary, +trinity, +wheel, +yin yang

### WORLD RELIGIONS  `world_religions`
- правило: Major religions of the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~Bahá'í, ~Jainism, ~Sikhism, ~Zoroastrianism, +Buddhism, +Christianity, +Confucianism, +Hinduism, +Islam, +Judaism, +Shinto, +Taoism


## Тема: trades

### AUTO REPAIR  `auto_repair`
- правило: Things a mechanic works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 17
- ~oil (oil_motor), +alternator, +battery, +belt, +brake pad, +coolant, +diagnostic, +filter, +gasket, +hose, +jack (jack_tool), +lift, +radiator, +spark plug, +tire iron, +transmission, +wrench

### BAKERY WORDS  `baker_words`
- правило: Things found in a bakery
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- +apron (apron_garment), +cooling rack, +display case, +dough, +flour, +icing, +mixer, +oven, +pastry bag, +rack, +timer, +tongs, +tray, !proofer, !scale (scale_weigh)

### BARBERSHOP WORDS  `barbershop_words`
- правило: Things found in a barbershop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- +apron (apron_garment), +brush, +cape, +chair, +clippers, +comb, +mirror, +pole, +powder, +razor, +scissors, +shaving cream, +towel, +trimmer

### BUTCHER SHOP  `butcher_words`
- правило: Things found in a butcher shop
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~block (block_cube), +apron (apron_garment), +brisket, +cleaver, +cut, +freezer, +grinder, +rack, +sausage, +saw, +twine, +wrap, !case (case_box), !scale (scale_weigh)

### CARPENTRY WORDS  `carpentry_words`
- правило: Things a carpenter works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~beam (beam_wood), ~dovetail, ~joist, ~miter, ~plane (plane_tool), +chisel, +groove, +level, +lumber, +molding, +nail gun, +plywood, +rafter, +shim, +Square, +stud, +veneer, !sawhorse

### JANITORIAL WORDS  `cleaning_trade`
- правило: Things a janitor uses at work
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~squeegee, ~wax (wax_polish), +broom, +bucket, +buffer, +cart, +disinfectant, +dustpan, +gloves, +keys, +mop, +sign, +trash bag, +uniform, +vacuum

### ELECTRICAL WORDS  `electrical_words`
- правило: Things an electrician works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +amp, +breaker, +cable, +conduit, +fuse, +ground, +insulation, +junction box, +outlet, +panel, +socket (socket_electric), +switch, +terminal, +transformer, +voltage, +wire

### FACTORY WORDS  `factory_words`
- правило: Things found in a factory
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~shift (shift_work), +assembly line, +conveyor, +crate, +foreman, +machine, +quality control, +robot, +safety goggles, +uniform, +whistle, !mold (mold_form), !press (press_machine), xtimeclock

### LANDSCAPING WORDS  `landscaping_words`
- правило: Things a landscaper works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +blower, +edger, +fertilizer, +gravel, +hedge, +mower, +mulch, +planter, +seed, +shears, +sod, +sprinkler, +stake, +trimmer, +wheelbarrow

### LOCKS & KEYS  `locksmith_words`
- правило: Things involved with locks and keys
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- +bolt, +chain, +combination, +cylinder, +hinge, +key (key_lock), +keyhole, +keypad, +latch, +lock, +master key, +padlock, +safe, +tumbler, !deadbolt

### MASONRY WORDS  `masonry_words`
- правило: Things a mason works with
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~block (block_cube), ~brick, ~cement, ~chisel, ~grout, ~joint, ~level, ~mortar, ~scaffold, ~stone, ~trowel, ~wheelbarrow, !hod, !plumb line

### HOUSE PAINTING  `painting_trade`
- правило: Things a house painter uses
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~caulk, +brush, +drop cloth, +extension pole, +ladder, +primer, +putty, +roller, +sandpaper, +scraper, +sprayer, +stir stick, +tape, +tray

### PLUMBING WORDS  `plumbing_words`
- правило: Things a plumber works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~spigot, +coupling, +drain, +elbow, +faucet, +fitting, +flange, +gasket, +pipe (pipe_tube), +plunger, +sewer, +sink (sink_basin), +snake, +solder, +trap, +valve, +washer, +wrench

### PRINTING WORDS  `printing_words`
- правило: Things used in printing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~binding, ~cartridge, ~font, ~ink, ~paper, ~press (press_machine), ~proof, ~registration, ~roller, ~screen (screen_print), ~stencil, ~toner, ~type, !plate (plate_printing)

### ROOFING WORDS  `roofing_words`
- правило: Things used in roofing a house
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~drip edge, ~felt, ~flashing, ~gutter, ~harness, ~ladder, ~nail gun, ~ridge, ~shingle, ~tar, ~tile, ~valley, ~vent, !underlayment

### TAILOR SHOP  `tailor_words`
- правило: Things a tailor uses
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~chalk (chalk_tailor), +bobbin, +hem, +iron (iron_appliance), +machine, +mannequin, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam ripper, +shears, +tape measure, +thimble, +thread

### WAREHOUSE WORDS  `warehouse_words`
- правило: Things found in a warehouse
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- +aisle, +box, +conveyor, +crate, +dock, +forklift, +hand truck, +inventory, +label, +pallet, +ramp, +scanner, +shelf (shelf_furniture), +tape gun

### WELDING WORDS  `welding_words`
- правило: Things used in welding metal
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~arc, ~bead, ~clamp, ~filler, ~flux, ~gas, ~helmet, ~rod, ~slag, ~spark, ~tack (tack_pin), ~torch, !apron (apron_garment), !tip (tip_point)

