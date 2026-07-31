# Категории, часть 3 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: actions

### ANIMAL ACTIONS  `animal_actions`
- правило: Actions typical of animals rather than people
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~molt, +burrow, +forage, +graze, +hatch, +hibernate, +hunt, +migrate, +nest, +perch, +pounce, +prowl, +roost, +shed, +slither, +spawn

### BUILDING ACTIONS  `building_actions`
- правило: Actions done when building or repairing something
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~caulk, +assemble, +bolt, +drill (drill_tool), +glue, +hammer, +install, +level, +measure, +mount, +nail (nail_metal), +paint, +plaster, +sand, +saw, +screw, +tile, +weld

### CARRYING ACTIONS  `carrying_actions`
- правило: Ways of carrying or moving an object
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- +carry, +drag, +haul, +heave, +hoist, +lift, +load, +pull, +push, +shove, +slide, +toss, +tow, +transport, !roll (roll_turn)

### CLEANING ACTIONS  `cleaning_actions`
- правило: Actions done when cleaning something
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~declutter, +disinfect, +dry, +dust, +launder, +mop, +polish (polish_verb), +rinse, +scour, +scrub, +shine, +sweep, +tidy, +vacuum, +wash, +wipe

### COOKING ACTIONS  `cooking_actions`
- правило: Verbs describing something a cook does to food
- тип связи: `does_action`, базовая сложность 0.25
- слов: 26
- ~dice (dice_cut), ~saute, +bake, +blend, +boil, +broil, +chop, +drain, +fry (fry_cook), +garnish, +grill, +knead, +marinate, +mash, +mince, +peel, +roast, +sear, +simmer, +slice, +steam, +stir, +toss, +whipping, +whisk, !season (season_flavor)

### BREAKING ACTIONS  `destroying_actions`
- правило: Actions that damage or destroy something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~squash (squash_crush), +break, +burst, +crumble, +crush, +demolish, +dent, +flatten, +puncture, +rip, +shatter, +shred, +smash, +snap, +split, +tear

### DRIVING ACTIONS  `driving_actions`
- правило: Actions done while driving a car
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- +accelerate, +brake, +cruise, +honk, +idle, +merge, +park (park_verb), +reverse, +shift (shift_gear), +signal, +stall (stall_engine), +steer, +swerve, +tailgate, +yield

### EATING ACTIONS  `eating_actions`
- правило: Actions done while eating or drinking
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- ~swallow (swallow_throat), +bite (bite_eat), +chew, +devour, +drink, +feast, +gnaw, +gulp, +lick, +munch, +nibble, +sip, +slurp, +snack, +taste

### GARDEN ACTIONS  `garden_actions`
- правило: Actions done while gardening
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- ~plant (plant_verb), ~trim (trim_cut), +compost, +dig, +fertilize, +harvest, +mow, +mulch, +prune, +rake, +seed, +sow (sow_plant), +transplant, +water, +weed

### GIVING AND TAKING  `giving_and_taking`
- правило: Verbs about transferring something to or from someone
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~hand (hand_give), +borrow, +buy, +collect, +deliver, +donate, +give, +lend, +offer, +receive, +return, +sell, +share, +swap, +take, +trade

### HAND ACTIONS  `hand_actions`
- правило: Actions performed with the hands
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- ~point (point_gesture), +catch, +clap, +grab, +hold, +knock, +pinch, +pull, +push, +rub, +scratch, +shake, +slap, +squeeze, +tap (tap_touch), +throw, +twist, +wave (wave_hand), +wring, +write

### JOINING ACTIONS  `joining_actions`
- правило: Actions that join two things together
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~button (button_clothing), ~tie (tie_knot), +attach, +bind, +buckle, +clip, +fasten, +glue, +knot, +link (link_chain), +sew, +staple, +stitch, +tape, +weld, +zip

### MONEY ACTIONS  `money_actions`
- правило: Actions people do with money
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- +bill (bill_money), +borrow, +budget, +deposit, +donate, +earn, +gamble, +invest, +lend, +owe, +pay, +refund, +save, +spend, +tip (tip_money), +withdraw

### OPENING ACTIONS  `opening_actions`
- правило: Actions that open or uncover something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~unbutton, ~unroll, ~unscrew, +lift, +open, +peel, +pry, +reveal, +uncover, +unfold, +unlock, +unwrap, +unzip, !uncork

### SILENT ACTIONS  `quiet_actions`
- правило: Actions that make almost no noise
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~blink, ~breathe, ~glide, ~nod, ~read, ~sleep, ~smile, ~sneak, ~stare, ~think, ~tiptoe, ~whisper, ~wink, !wave (wave_hand)

### SCHOOL ACTIONS  `school_actions`
- правило: Actions done at school
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- ~spell (spell_letters), +calculate, +grade, +learn, +memorize, +quiz, +read, +recite, +research, +review, +study, +submit, +teach, +write, !present (present_show)

### SLEEP ACTIONS  `sleeping_actions`
- правило: Things a person does while sleeping or falling asleep
- тип связи: `does_action`, базовая сложность 0.35
- слов: 12
- ~sleepwalk, +doze, +dream, +drift off, +nap, +rest (rest_sleep), +slumber, +snore, +stretch, +toss, +turn, +yawn

### SPORTS ACTIONS  `sports_actions`
- правило: Actions done while playing sports
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~dunk (dunk_basketball), ~score (score_points), +catch, +dive, +dribble, +kick, +pass, +pitch (pitch_throw), +punt, +serve, +shoot, +spike, +sprint, +swing, +tackle, +throw, +volley, !block (block_stop)

### THINKING ACTIONS  `thinking_actions`
- правило: Verbs for mental activity
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~focus (focus_mind), +consider, +decide, +doubt, +forget, +guess, +imagine, +invent, +judge, +learn, +plan, +recall, +remember, +solve, +think, +wonder

### WATER ACTIONS  `water_actions`
- правило: Actions done in or with water
- тип связи: `does_action`, базовая сложность 0.35
- слов: 18
- +dive, +drain, +drip (drip_water), +dunk (dunk_dip), +float, +flood, +paddle, +pour, +rinse, +sink (sink_verb), +soak, +spill, +splash, +spray, +sprinkle, +swim, +wade, +wash

### WAYS OF LAUGHING  `ways_of_laughing`
- правило: Verbs for different kinds of laughing
- тип связи: `does_action`, базовая сложность 0.4
- слов: 11
- ~cackle, ~chortle, ~chuckle, ~giggle, ~guffaw, ~howl, ~laugh, ~roar, ~snicker, ~snort, !titter

### WAYS OF LOOKING  `ways_of_looking`
- правило: Verbs describing a way of looking at something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- +gaze, +glance, +glare, +inspect, +observe, +ogle, +peek, +peer, +scan, +spy, +squint, +stare, +survey, +watch (watch_look)

### WAYS OF MOVING  `ways_of_moving`
- правило: Verbs describing a way a person moves their body from place to place
- тип связи: `does_action`, базовая сложность 0.25
- слов: 26
- ~march (march_walk), ~shuffle (shuffle_walk), ~spring (spring_jump), ~trudge, +climb, +crawl, +dart (dart_move), +dash (dash_run), +hop, +jog, +jump, +leap, +limp, +race, +run, +scramble, +skip, +slide, +sprint, +stagger, +stroll, +swim, +tiptoe, +wade, +walk, +wander

### WAYS OF SPEAKING  `ways_of_speaking`
- правило: Verbs describing a way of saying something aloud
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~stammer, +announce, +chant, +chatter, +declare, +gossip, +growl, +hiss, +holler, +mumble, +murmur, +mutter, +recite, +scream, +shout, +sing, +whisper, +yell

### WEATHER ACTIONS  `weather_actions`
- правило: Verbs describing what weather does
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- +blow, +clear, +drizzle, +flood, +freeze, +gust, +hail, +melt, +pour, +rain, +shine, +sleet, +snow, +thaw, +thunder


## Тема: cities

### AFRICAN CITIES  `african_cities`
- правило: Well known cities in Africa
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Luanda, +Accra, +Addis Ababa, +Alexandria, +Cairo, +Cape Town, +Casablanca, +Dakar, +Durban, +Kampala, +Khartoum, +Lagos, +Marrakech, +Nairobi, +Pretoria, +Tunis

### TRANSPORT HUBS  `airports_and_ports`
- правило: Famous airports and transport hubs
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Charles de Gaulle, +Dubai International, +Gatwick, +Grand Central, +Heathrow, +JFK, +LAX, +Penn Station, +Union Station, !Narita, !Schiphol, xOHare

### EAST COAST  `american_east_cities`
- правило: Cities on the American East Coast
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +Albany, +Baltimore, +Boston, +buffalo, +Charleston, +Hartford, +Jacksonville, +Newark, +Norfolk, +Philadelphia, +Portland, +Providence, +Richmond, +Savannah, +Wilmington

### WEST COAST  `american_west_cities`
- правило: Cities on the American West Coast
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +Anaheim, +Berkeley, +Eugene, +Fresno, +Long Beach, +Oakland, +Portland, +Sacramento, +San Diego, +San Jose, +Santa Monica, +Seattle, +Spokane, +Tacoma

### ASIAN CITIES  `asian_cities`
- правило: Well known cities in Asia
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +Busan, +Chengdu, +Chennai, +Colombo, +Delhi, +Hanoi, +Hyderabad, +Jakarta, +Karachi, +Kathmandu, +Kolkata, +Kyoto, +Lahore, +Manila, +Mumbai, +Osaka, +Saigon, +Shanghai, +Taipei, +Xian

### MORE CAPITALS  `capital_cities_more`
- правило: Capital cities less commonly named
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +Ankara, +Bern, +Brasilia, +Brussels, +Bucharest, +Canberra, +Copenhagen, +Islamabad, +Nairobi, +Reykjavik, +Riga, +Riyadh, +Sofia, +Stockholm, +Tallinn, +Vilnius, +Wellington, +Zagreb

### CITY NICKNAMES  `city_nicknames`
- правило: Nicknames given to famous cities
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Big Apple, +Big Easy, +City of Angels, +Emerald City, +Mile High City, +Motor City, +Music City, +Queen City, +Sin City, +Steel City, +Windy City, !Beantown

### EUROPEAN CITIES  `european_cities`
- правило: Well known cities in Europe
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Antwerp, +Barcelona, +Bergen, +Bruges, +Cologne, +Edinburgh, +Florence, +Geneva, +Hamburg, +Krakow, +Liverpool, +Lyon, +Manchester, +Marseille, +Milan, +Munich, +Naples, +Porto, +Rotterdam, +Salzburg, +Seville, +Turin, +Valencia, +Venice, +Zurich

### MIDWEST CITIES  `midwest_cities`
- правило: Cities in the American Midwest
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +Chicago, +Cincinnati, +Cleveland, +Columbus, +Des Moines, +Detroit, +Duluth, +Indianapolis, +Kansas City, +Milwaukee, +Minneapolis, +Omaha, +St Louis, +Toledo, +Wichita

### RESORT DESTINATIONS  `resort_towns`
- правило: Places people travel to for vacation
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Aspen, +Bali, +Cabo, +Cancun, +Ibiza, +Key West, +Lake Tahoe, +Maldives, +Maui, +Monaco, +Myrtle Beach, +Napa, +Palm Springs, +Santorini, +Vail

### LATIN CITIES  `south_american_cities`
- правило: Well known cities in South America
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Asuncion, ~Cusco, +Bogota, +Brasilia, +Buenos Aires, +Caracas, +Cartagena, +La Paz, +Medellin, +Montevideo, +Quito, +Rio de Janeiro, +Santiago, +Sao Paulo

### SOUTHERN CITIES  `southern_cities`
- правило: Cities in the American South
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +Atlanta, +Austin, +Birmingham, +Charlotte, +Dallas, +Houston, +Little Rock, +Louisville, +Memphis, +Miami, +mobile, +Nashville, +New Orleans, +Raleigh, +Tampa


## Тема: education

### FIRST LESSONS  `alphabet_and_numbers`
- правило: The very first things children learn at school
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~season (season_time), ~sound (sound_noise), +addition, +alphabet, +color, +count, +day, +letter (letter_alphabet), +month, +name, +number, +rhyme, +shape, +sight word, +word

### ART CLASS  `art_class_things`
- правило: Things used in a school art class
- тип связи: `found_in`, базовая сложность 0.25
- слов: 22
- ~chalk (chalk_stick), +apron (apron_garment), +brush, +canvas, +clay, +colors, +construction paper, +crafts, +easel, +glitter, +glue, +kiln, +marker, +paint, +palette, +pastel, +patterns, +scissors, +shapes, +sketchbook, +smock, +stencil

### CLASSROOM THINGS  `classroom_things`
- правило: Things found in a school classroom
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- +alphabet, +bell, +bookshelf, +calendar, +chair, +chalk (chalk_stick), +chalkboard, +clock, +cubby, +desk, +easel, +flag, +globe, +hall pass, +locker, +map, +poster, +projector, +textbook, +whiteboard

### COLLEGE WORDS  `college_words`
- правило: Words used about university education
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~major (major_study), +alumni, +campus, +credit, +dean, +degree (degree_academic), +dorm, +fraternity, +freshman, +junior, +lecture, +minor, +professor, +scholarship, +semester, +seminar, +senior, +sophomore, +thesis, +tuition

### ACADEMIC DEGREES  `degrees_and_titles`
- правило: Degrees and academic qualifications
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +associate, +bachelor, +certificate, +credential, +diploma, +doctorate, +fellowship, +honors, +license, +master, +MBA, +PhD

### FIELD TRIPS  `field_trip_places`
- правило: Places classes visit on a field trip
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- +aquarium, +bakery, +capitol, +factory, +farm, +fire station, +gallery, +historical site, +museum, +orchard, +park (park_place), +planetarium, +science center, +theater, +zoo

### GRADING WORDS  `grades_and_marks`
- правило: Words used to grade and evaluate students
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +average, +credit, +essay, +exam, +fail, +final, +GPA, +grade, +homework, +honor roll, +midterm, +pass, +quiz, +report card, +rubric, +score (score_points), +test, +transcript

### GYM CLASS  `gym_class_things`
- правило: Things used in a school gym class
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- +ball (ball_sphere), +bleachers, +cone, +dodgeball, +hoop, +hurdle, +jump rope, +locker, +mat, +net, +parachute, +scoreboard, +sneakers, +stopwatch, +uniform, +whistle

### IN THE CLASSROOM  `in_the_classroom`
- правило: A person, task or fixture found in a classroom
- тип связи: `found_in`, базовая сложность 0.3
- слов: 6
- +blackboard, +exam, +homework, +lesson, +quiz, +student

### LEARNING ACTIONS  `learning_actions`
- правило: Things students do while learning
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- +discuss, +drill (drill_practice), +listen, +memorize, +note (note_written), +outline, +practice, +question, +quiz, +read, +rehearse, +research, +review, +solve, +summarize, +write

### LIBRARY WORDS  `library_words`
- правило: Things and rules found in a library
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~atlas (atlas_book), +aisle, +archive, +book, +catalog, +checkout, +due date, +encyclopedia, +fine, +librarian, +magazine, +periodical, +reference, +shelf (shelf_furniture), +silence, +stack (stack_shelves), +study room, !card (card_plastic)

### MUSIC CLASS  `music_class_things`
- правило: Things used in a school music class
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~maraca, ~stand (stand_holder), ~xylophone, +bell, +choir, +conductor, +drum, +metronome, +piano, +recorder, +riser, +sheet music, +tambourine, +triangle

### KINDS OF PAPER  `paper_types`
- правило: Kinds of paper used at school and home
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~carbon (carbon_paper), ~cardstock, +construction, +graph, +index card, +loose leaf, +newsprint, +notebook, +parchment, +printer, +sticky note, +tissue (tissue_paper), +tracing, +wax (wax_substance)

### READING WORDS  `reading_words`
- правило: Words used when reading and studying text
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +appendix, +bibliography, +chapter, +excerpt, +footnote, +glossary, +index, +page, +paragraph, +passage, +preface, +quote, +summary, +table of contents, +title

### SCHOOL EVENTS  `school_events`
- правило: Events that happen during a school year
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +assembly, +book fair, +detention, +exam, +field trip, +graduation, +homecoming, +open house, +orientation, +pep rally, +picture day, +prom, +recess, +science fair, +spelling bee, +talent show

### SCHOOL PEOPLE  `school_people`
- правило: People you meet at a school
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- +aide, +bus driver, +cafeteria worker, +classmate, +coach, +counselor, +crossing guard, +janitor, +librarian, +nurse, +principal, +student, +substitute, +teacher, +tutor, +volunteer

### SCHOOL PLACES  `school_places`
- правило: Rooms and places inside a school
- тип связи: `part_of`, базовая сложность 0.2
- слов: 18
- +art room, +auditorium, +bathroom, +cafeteria, +classroom, +computer lab, +courtyard, +field, +gym, +hallway, +lab, +library, +locker room, +nurse office, +office, +playground, +principal office, +stage

### SCHOOL SUBJECTS  `school_subjects`
- правило: Subjects taught in an American school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~band (band_group), +algebra, +art, +biology, +calculus, +chemistry, +civics, +computer science, +drama, +economics, +English, +geography, +geometry, +gym, +health, +history, +home economics, +literature, +math, +music, +physics, +science, +shop, +spanish, +trigonometry

### SCHOOL SUPPLIES  `school_supplies`
- правило: Items a student brings to school in a backpack
- тип связи: `used_in`, базовая сложность 0.15
- слов: 27
- +backpack, +binder, +book, +calculator, +compass, +crayon, +desk, +eraser, +folder, +glue, +highlighter, +index card, +lunchbox, +marker, +notebook, +paper, +pen (pen_writing), +pencil, +pencil case, +planner, +protractor, +ruler, +scissors, +sharpener, +stapler, +tape, +textbook

### TEST WORDS  `testing_words`
- правило: Words for kinds of test questions and formats
- тип связи: `found_in`, базовая сложность 0.35
- слов: 12
- +essay, +fill in the blank, +final, +matching, +multiple choice, +open book, +oral, +pop quiz, +practical, +short answer, +timed, +true false

### WRITING TOOLS  `writing_tools`
- правило: Tools used to write or draw
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~chalk (chalk_stick), ~keyboard (keyboard_computer), +brush, +charcoal, +crayon, +felt tip, +fountain pen, +highlighter, +marker, +pastel, +pen (pen_writing), +pencil, +quill, +stylus, +typewriter


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

### AT THE MOVIES  `at_the_movies`
- правило: Something you meet at a cinema
- тип связи: `found_in`, базовая сложность 0.35
- слов: 7
- +admission, +cinema, +matinee, +popcorn, +screen (screen_display), +trailer (trailer_movie), +usher

### AT THE THEATER  `at_the_theater`
- правило: A part of a theatre or the people in it
- тип связи: `found_in`, базовая сложность 0.35
- слов: 6
- +actor, +audience, +curtain, +props, +script, +stage

### AUDITIONS  `auditions`
- правило: A word belonging to trying out for a part
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +audition, +callback, +contestant, +spotlight

### BALLET CLASS  `ballet_class`
- правило: A move, garment or fixture of a ballet class
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- ~arabesque, ~pirouette, +barre, +leotard, +recital

### BOARD GAMES  `board_games`
- правило: Games played on a printed board with pieces
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~mancala, +backgammon, +battleship, +candy land, +checkers, +chess, +chutes and ladders, +clue, +dominoes, +Life, +monopoly, +othello, +risk, +scrabble, +sorry, +trivial pursuit, +trouble, xparcheesi

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

### CIRCUS RING  `circus_ring`
- правило: A circus act or prop beyond the obvious ones
- тип связи: `found_in`, базовая сложность 0.6
- слов: 4
- ~unicycle, +cannonball, +stilts, +strongman

### CIRCUS WORDS  `circus_words`
- правило: People, animals and objects you see at a traditional circus
- тип связи: `found_in`, базовая сложность 0.3
- слов: 19
- ~sword swallower, +acrobat, +cannon, +clown, +cotton candy, +elephant, +juggler, +lion tamer, +magician, +net, +popcorn, +ring (ring_arena), +ringmaster, +sequin, +stilts, +tent, +tightrope, +trapeze, +unicycle

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

### IN A BAND  `in_a_band`
- правило: A part played by a member of a music band
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- +bass (bass_music), +drummer, +frontman, +guitar, +keyboard (keyboard_music), +vocals

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
- слов: 26
- ~keyboard (keyboard_music), +accordion, +bagpipes, +banjo, +bassoon, +cello, +clarinet, +cymbal, +drum, +flute, +guitar, +harmonica, +harp, +horn (horn_sound), +mandolin, +oboe, +organ (organ_music), +piano, +saxophone, +tambourine, +trombone, +trumpet, +tuba, +ukulele, +violin, +xylophone

### ORCHESTRA WORDS  `orchestra_words`
- правило: A term belonging to an orchestra and its music
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 6
- ~woodwind, +concerto, +crescendo, +maestro, +overture, +symphony

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

### SINGING VOICES  `singing_voices`
- правило: A named singing range or singing group
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +alto, +bass (bass_music), +choir, +solo, +soprano, +tenor

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
- слов: 22
- ~kite (kite_toy), ~marble (marble_toy), ~rattle (rattle_toy), ~top (top_spin), +action figure, +ball (ball_sphere), +blocks, +bubble, +crayon, +doll, +frisbee, +jack in the box, +jump rope, +puzzle, +robot, +Slinky, +teddy, +teddy bear, +train set, +tricycle, +yo-yo, +yoyo

### TELEVISION WORDS  `tv_words`
- правило: Words used about television programs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +broadcast, +cable, +channel, +commercial, +episode, +finale, +network, +pilot, +ratings, +remote (remote_device), +rerun, +screen (screen_display), +sitcom, +spinoff, +streaming, +subtitle, !host (host_presenter), !season (season_time)

### TYPES OF GUITARS  `types_of_guitars`
- правило: A kind of guitar or a close relative of the guitar
- тип связи: `is_a`, базовая сложность 0.4
- слов: 6
- +acoustic, +banjo, +bass (bass_music), +classical, +electric, +ukulele

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


## Тема: geography

### AFRICAN COUNTRIES  `african_countries`
- правило: Countries located in Africa
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +Algeria, +Angola, +Botswana, +Chad, +Egypt, +Ethiopia, +Ghana, +Kenya, +Libya, +Morocco, +Namibia, +Nigeria, +Rwanda, +Senegal, +Somalia, +Sudan, +Tanzania, +Tunisia, +Uganda, +Zambia

### ASIAN COUNTRIES  `asian_countries`
- правило: Countries located in Asia
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~turkey (turkey_country), +Bangladesh, +Cambodia, +China, +India, +Indonesia, +Iran, +Israel, +Japan, +Jordan, +Korea, +Laos, +Malaysia, +Mongolia, +Nepal, +Pakistan, +Philippines, +Singapore, +Thailand, +Vietnam

### CITY WORDS  `city_words`
- правило: Words for the parts and features of a city
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- +alley, +avenue, +block (block_cube), +boulevard, +bridge (bridge_structure), +curb, +district, +downtown, +intersection, +neighborhood, +park (park_place), +plaza, +sidewalk, +skyline, +skyscraper, +street, +suburb, +Subway, +tower, +traffic

### CLIMATE WORDS  `climate_zones`
- правило: Words describing the climate of a region
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +alpine, +Arctic, +arid, +coastal, +continental, +desert, +humid, +mediterranean, +monsoon, +polar, +rainforest, +subtropical, +temperate, +tropical

### COLD PLACES  `cold_places`
- правило: Places that are typically cold
- тип связи: `has_property`, базовая сложность 0.3
- слов: 14
- ~Antarctica, ~Arctic, ~basement, ~cave, ~freezer, ~glacier, ~iceberg, ~igloo, ~north pole, ~refrigerator, ~ski slope, ~tundra, +mountain, !snowfield

### CONTINENTS AND OCEANS  `continents_and_oceans`
- правило: The continents and the world oceans
- тип связи: `is_a`, базовая сложность 0.2
- слов: 12
- +Africa, +Antarctica, +Arctic, +Asia, +Atlantic, +Australia, +Europe, +Indian, +North America, +Pacific, +South America, +Southern

### COUNTRIES  `countries`
- правило: A country of the world
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +Austria, +Brazil, +Egypt, +France, +Greece, +Italy, +Japan, +Spain

### DESERTS  `deserts_and_wild_places`
- правило: Major deserts of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~Atacama, ~Sonoran, +Arabian, +Death Valley, +Gobi, +Great Basin, +Kalahari, +Mojave, +Painted Desert, +Sahara

### DIRECTIONS  `directions`
- правило: Words used to give directions
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- +across, +around, +back, +behind, +beside, +down, +east, +far, +forward, +left, +near, +north, +over, +right, +south, +straight, +through, +under, +up, +west

### EUROPEAN COUNTRIES  `european_countries`
- правило: Countries located in Europe
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- +Austria, +Belgium, +Bulgaria, +Croatia, +Denmark, +Estonia, +Finland, +France, +Germany, +Greece, +Hungary, +Iceland, +Ireland, +Italy, +Netherlands, +Norway, +Poland, +Portugal, +Romania, +Scotland, +Serbia, +Slovakia, +Spain, +Sweden, +Switzerland

### FAMOUS LANDMARKS  `famous_landmarks`
- правило: World landmarks most people can recognize
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +Acropolis, +Big Ben, +Colosseum, +Eiffel Tower, +Empire State, +Golden Gate, +Great Wall, +Leaning Tower, +Mount Rushmore, +pyramid (pyramid_monument), +sphinx, +Statue of Liberty, +Stonehenge, +Taj Mahal, +White House

### GEOGRAPHY CLASS  `geography_class`
- правило: What you are asked to name or point at in a geography lesson
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- +atlas (atlas_book), +globe, +islands, +lakes, +latitude, +rivers, +seas

### HOT PLACES  `hot_places`
- правило: Places that are typically hot
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~attic, ~campfire, ~desert, ~equator, ~furnace, ~greenhouse, ~jungle, ~kitchen, ~oven, ~sauna, ~tropics, ~volcano, +beach, +engine, +sun

### ISLANDS  `islands`
- правило: Well known islands around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +Bali, +Barbados, +Bermuda, +Crete, +Cuba, +Fiji, +Greenland, +Hawaii, +Iceland, +Jamaica, +Madagascar, +Malta, +Sardinia, +Sicily, +Tahiti

### LANDFORMS  `landforms`
- правило: Natural features of the land surface
- тип связи: `is_a`, базовая сложность 0.3
- слов: 27
- ~delta (delta_river), +basin, +butte, +canyon, +cave, +cliff, +crater, +dune, +foothill, +glacier, +gorge, +hill, +island, +islands, +isthmus, +marsh, +mesa, +mountain, +peninsula, +plain, +plateau, +prairie, +ridge, +summit, +tundra, +valley, +volcanoes

### LATIN AMERICA  `latin_american_countries`
- правило: Countries of Central and South America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +Argentina, +Belize, +Bolivia, +Brazil, +Chile, +Colombia, +Costa Rica, +Cuba, +Ecuador, +Guatemala, +Honduras, +Mexico, +Nicaragua, +panama, +Paraguay, +Peru, +Uruguay, +Venezuela

### MAP LEGEND  `map_legend`
- правило: What a map marks with a symbol or a colour
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- ~biomes, ~volcanoes, ~waterfalls, +contour, +landforms, +scale (scale_ratio), +symbol

### MAP WORDS  `map_words`
- правило: Words used to read and describe a map
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~key (key_legend), ~scale (scale_ratio), +atlas (atlas_book), +border, +compass, +contour, +coordinate, +east, +elevation, +globe, +grid, +latitude, +legend, +longitude, +meridian, +north, +route, +south, +symbol, +west

### MOUNTAIN RANGES  `mountain_ranges`
- правило: Major mountain ranges of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Appalachians, ~Carpathians, +Alps, +Andes, +Cascades, +Himalayas, +Ozarks, +Pyrenees, +Rockies, +Sierra Nevada, +Urals, !atlas (atlas_mountains)

### PARK WORDS  `national_parks`
- правило: Things found in a national park or campground
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +bear box, +cabin (cabin_house), +campfire, +campsite, +canyon, +geyser, +lantern, +lodge, +map, +overlook, +path, +picnic table, +Ranger, +tent, +trail, +visitor center, +waterfall, +wildlife

### PARTS OF THE AMERICAS  `parts_of_the_americas`
- правило: A word that names a region when placed before America
- тип связи: `wordplay`, базовая сложность 0.45
- слов: 4
- +central, +Latin, +north, +south

### WAITING PLACES  `places_you_wait`
- правило: Places where people commonly stand in line
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~amusement park, ~buffet, ~checkout, ~DMV, ~grocery store, ~pharmacy, ~theater, ~ticket booth, +airport, +bus stop, +doctor office, +post office, +restaurant, !bank (bank_finance)

### QUIET PLACES  `quiet_places`
- правило: Places where people are expected to stay quiet
- тип связи: `has_property`, базовая сложность 0.35
- слов: 12
- ~cemetery, ~classroom, ~courtroom, ~exam room, ~funeral, ~monastery, ~theater, +church, +hospital, +library, +museum, +study hall

### RIVERS  `rivers`
- правило: Major rivers of the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +Amazon, +Colorado, +Congo, +Danube, +Euphrates, +Ganges, +Hudson, +Mississippi, +Missouri, +Nile, +Rhine, +Rio Grande, +Seine, +Thames, +Volga, +Yangtze

### FARM THINGS  `things_on_a_farm`
- правило: Things found on a working farm
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~pen (pen_animal), +bale, +barn, +coop, +crop, +fence, +field, +gate (gate_barrier), +harvest, +hay, +orchard, +pasture, +plow, +scarecrow, +silo, +stable, +tractor, +trough, +well, +windmill

### TOWN PLACES  `town_places`
- правило: Public buildings and places found in an ordinary American town
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- +bank (bank_finance), +cemetery, +church, +city hall, +clinic, +courthouse, +diner, +firehouse, +gym, +hospital, +jail, +library, +mall, +market, +museum, +park (park_place), +pharmacy, +playground, +plaza, +post office, +school, +stadium, +temple (temple_building), +theater, !station (station_place)

### TRAVEL ABROAD  `travel_abroad`
- правило: What changes about daily life when you cross a border
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 7
- +currencies, +languages, +nationalities, +phrasebook, +souvenir, +Visa, !islands

### US CITIES  `us_cities`
- правило: Large cities in the United States
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +Atlanta, +Austin, +Baltimore, +Boston, +Charlotte, +Chicago, +Cleveland, +Dallas, +Denver, +Detroit, +Houston, +Memphis, +Miami, +Milwaukee, +Nashville, +Orlando, +Philadelphia, +phoenix (phoenix_city), +Portland, +Seattle

### US STATES  `us_states`
- правило: States of the United States of America
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- +Alabama, +Alaska, +Arizona, +California, +Colorado, +Delaware, +Florida, +Georgia, +Hawaii, +idaho (idaho_state), +Indiana, +Iowa, +Kansas, +Maine, +Michigan, +Montana, +Nebraska, +Nevada, +Ohio, +Oregon, +Texas, +Utah, +Vermont, +Virginia, +Wyoming

### WORLD CAPITALS  `world_capitals`
- правило: Capital cities of countries around the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Amsterdam, +Athens, +Bangkok, +Beijing, +Berlin, +Budapest, +Cairo, +Dublin, +Havana, +Helsinki, +Lima, +Lisbon, +London, +Madrid, +Moscow, +Nairobi, +Oslo, +Ottawa, +Paris, +Prague, +Rome, +Seoul, +Tokyo, +Vienna, +Warsaw


## Тема: jargon

### ACCOUNTING WORDS  `accounting_words`
- правило: Words used in bookkeeping and accounting
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~asset, ~audit, ~balance, ~credit, ~debit, ~depreciation, ~expense, ~invoice, ~ledger, ~liability, ~payroll, ~receipt, ~revenue, ~statement

### ARCHITECTURE WORDS  `architecture_words`
- правило: Words used to describe buildings and their design
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~balcony (balcony_house), +arch (arch_structure), +atrium, +blueprint, +buttress, +column, +cornice, +dome, +facade, +foundation (foundation_building), +gable, +mezzanine, +portico, +spire, +terrace, +vault

### AVIATION WORDS  `aviation_words`
- правило: Words used by pilots and air crew
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~stall (stall_engine), +altitude, +autopilot, +call sign, +cockpit, +cruise, +flaps, +hangar, +landing gear, +radar, +rudder, +runway, +taxi, +throttle, +tower, +turbulence, +wingspan, +yaw

### BARISTA WORDS  `barista_words`
- правило: A term a barista uses making coffee
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- ~crema, ~frothing, +brewing, +decaf

### FORENSICS WORDS  `detective_procedures`
- правило: Words used in forensic investigation
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~autopsy, ~ballistics, ~cast (cast_mold), ~dna, ~dusting, ~evidence bag, ~fingerprint, ~lab, ~sample, ~swab, ~tape, ~toxicology, ~trace, !spatter

### FRENCH COOKING  `french_cooking_terms`
- правило: French words used in professional cooking
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~roux, !au gratin, !blanch, !bouquet garni, !braise, !consomme, !deglaze, !julienne, !mise en place, !puree, !saute, !souffle, xchiffonade, xflambe

### KITCHEN SLANG  `kitchen_brigade`
- правило: Terms used in a restaurant kitchen
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~comp, ~expo, ~fire, ~garnish, ~order up, ~pass, ~plating, ~prep, ~station (station_kitchen), ~walk in, !line (line_kitchen), !mise, !sous vide, !ticket (ticket_order)

### COURT TERMS  `legal_terms`
- правило: Terms used in legal proceedings
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~acquittal, ~appeal, ~arraignment, ~deposition, ~hearing, ~indictment, ~injunction, ~motion, ~objection, ~plea, ~recess, ~settlement, ~testimony, ~verdict

### MEDICAL PROCEDURES  `medical_procedures`
- правило: Procedures performed by doctors
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +anesthesia, +biopsy, +cast (cast_medical), +checkup, +dialysis, +injection, +scan, +screening, +stitches, +surgery, +therapy, +transfusion, +transplant, +ultrasound, +vaccination, +X-ray

### TEMPO TERMS  `music_tempo_terms`
- правило: Italian words used to mark tempo in music
- тип связи: `is_a`, базовая сложность 0.45
- слов: 16
- ~forte, ~grave, ~largo, ~piano, !accelerando, !adagio, !allegro, !andante, !crescendo, !legato, !lento, !moderato, !presto, !staccato, !vivace, xritardando

### SHIP CREW  `nautical_ranks`
- правило: Roles in the crew of a ship
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~captain, ~engineer, ~first mate, ~lookout, ~navigator, ~quartermaster, ~steward, !boatswain, !cook (cook_person), !deckhand, !helmsman, !purser

### CAMERA SETTINGS  `photography_terms`
- правило: Settings and controls on a camera
- тип связи: `found_in`, базовая сложность 0.45
- слов: 13
- ~aperture, ~depth of field, ~exposure, ~flash, ~focus (focus_lens), ~iso, ~shutter speed, ~timer, ~tripod mount, ~white balance, ~Zoom, !metering, !viewfinder

### TYPOGRAPHY WORDS  `printing_and_type`
- правило: Words used to describe printed type
- тип связи: `found_in`, базовая сложность 0.5
- слов: 14
- ~bold (bold_type), ~caps, ~column, ~font, ~italic, ~justify, ~leading, ~margin, ~point size, ~serif, ~typeface, ~underline, !kerning, !lowercase

### SAILING TERMS  `sailing_terms`
- правило: Terms used when sailing a boat
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~boom, ~draft (draft_boat), ~heel, ~sheet (sheet_sail), !capsize, !cleat, !halyard, !jibe, !leeward, !luff, !mooring, !spinnaker, !tack (tack_sail), !windward

### STAGE TERMS  `theater_stage_terms`
- правило: Terms used backstage in a theater
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- +blocking, +call time, +catwalk, +cue, +dimmer, +dress rehearsal, +flat, +gel, +green room, +prop table, +set piece, +wings, !apron (apron_stage), !strike (strike_theater)

### FORECAST TERMS  `weather_forecast_terms`
- правило: Terms used in a weather forecast
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- +advisory, +chance of rain, +dew point, +forecast, +front, +heat index, +high, +low, +precipitation, +pressure, +visibility, +warning, +wind chill, !watch (watch_warning)


## Тема: law

### COURTROOM  `courtroom`
- правило: What is heard, handed down or worn in a courtroom
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 11
- +crimes, +gavel, +jury, +objection, +penalties, +plaintiff, +rights, +subpoena, +testimony, +verdict, !titles

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

### DETECTIVE WORK  `detective_work`
- правило: Something a detective works with while solving a case
- тип связи: `used_in`, базовая сложность 0.45
- слов: 6
- +clue, +disguise, +evidence, +mystery, +suspect, +witness

### ELECTION DAY  `election_day`
- правило: A term belonging to a political election
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +candidate, +incumbent, +manifesto, +polls, +turnout

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
- слов: 17
- +badge, +baton, +cruiser, +dispatch, +flashlight, +handcuffs, +holster, +k9, +officer, +patrol, +radio, +siren, +ticket (ticket_fine), +uniform, +vest, +warrant, +whistle

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


## Тема: lists

### BIBLE BOOKS  `bible_books`
- правило: Books of the Bible
- тип связи: `is_a`, базовая сложность 0.45
- слов: 24
- +Acts, +Corinthians, +Daniel, +Deuteronomy, +Ecclesiastes, +Exodus, +Genesis, +Isaiah, +Jeremiah, +John, +Jonah, +Joshua, +Judges, +Kings, +Leviticus, +Luke, +mark, +Matthew, +Numbers, +Proverbs, +Psalms, +Revelation, +Romans, +Ruth

### WATER FEATURES  `body_of_water_types`
- правило: Kinds of water feature made by people
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +aqueduct, +bird bath, +canal, +cistern, +dam, +drain, +fountain, +moat, +pond, +pool, +reservoir, +sprinkler, +waterway, +well

### MORE BREEDS  `dog_breeds_more`
- правило: Dog breeds beyond the most common ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~akita, ~schnauzer, ~whippet, +bloodhound, +chow chow, +dalmatian, +newfoundland, +papillon, +pointer, +pomeranian, +setter, +shih tzu, !basenji, !bichon, !borzoi, !malamute, !saluki, !samoyed, !vizsla, !weimaraner

### MORE ELEMENTS  `elements_more`
- правило: Chemical elements beyond the most familiar ones
- тип связи: `is_a`, базовая сложность 0.45
- слов: 22
- +aluminum, +arsenic, +beryllium, +boron, +chromium, +cobalt, +fluorine, +iodine, +krypton, +lithium, +manganese, +nickel, +phosphorus, +platinum, +plutonium, +radium, +radon, +silicon, +silver, +titanium, +xenon, !bromine

### MORE FLOWERS  `flowers_more`
- правило: Flowers beyond the most common garden ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~gardenia, +anemone, +aster, +camellia, +chrysanthemum, +narcissus, +pansy, +snapdragon, +sweet pea, +wisteria, +yarrow, !amaryllis, !cornflower, !delphinium, !foxglove, !freesia, !gladiolus, !larkspur, !lupine, !ranunculus

### GEM CUTS  `gem_cuts`
- правило: Words used to describe cut and set gemstones
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~brilliant, ~carat, ~clarity, ~cut, ~emerald cut, ~facet, ~polish (polish_verb), ~princess cut, ~setting, ~Solitaire, !band (band_ring), !bezel, !cabochon, !prong

### MORE TREES  `trees_more`
- правило: Trees beyond the most common ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~ginkgo, +alder, +banyan, +cottonwood, +eucalyptus, +hawthorn, +hemlock, +larch, +linden, +locust, +mulberry, +olive, +persimmon, +sequoia, +sycamore, !baobab, !catalpa, !pawpaw, !sumac, !tamarack

### MORE STATES  `us_states_more`
- правило: States of the United States not in the shorter list
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Arkansas, +Connecticut, +Illinois, +Kansas, +Kentucky, +Louisiana, +Maryland, +Massachusetts, +Minnesota, +Mississippi, +Missouri, +Nevada, +New Hampshire, +New Mexico, +North Dakota, +Oklahoma, +Oregon, +Pennsylvania, +Rhode Island, +South Dakota, +Tennessee, +Utah, +Washington, +West Virginia, +Wisconsin

### ALPHABET AND SYMBOLS  `vitamins_letters`
- правило: Symbols and marks used in writing and math
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~ampersand, ~backslash, ~caret, ~tilde, +arrow, +asterisk, +at sign, +bullet, +dollar sign, +equals, +hashtag, +minus, +percent, +plus, !degree (degree_angle), !pipe (pipe_symbol)

### WEATHER INSTRUMENTS  `weather_instruments`
- правило: Instruments used to measure the weather
- тип связи: `used_in`, базовая сложность 0.45
- слов: 12
- +barometer, +radar, +rain gauge, +satellite, +thermometer, +weather balloon, +weather vane, !anemometer, !hygrometer, !seismograph, !sundial, !windsock


## Тема: nature_species

### BEETLES  `beetles`
- правило: Kinds of beetle
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~carpet beetle, ~click beetle, ~dung beetle, ~firefly, ~june bug, ~ladybug, ~scarab, ~stag beetle, ~water beetle, !boll weevil, !rhinoceros beetle, !weevil

### BUTTERFLY LIFE  `butterfly_life`
- правило: A stage or thing in the life of a butterfly
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 5
- ~milkweed, +caterpillar, +chrysalis, +cocoon, +monarch

### FROG POND  `frog_pond`
- правило: A word belonging to frogs and their pond
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- ~bullfrog, ~croak, +amphibious, +tadpole

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


## Тема: plants

### CACTUS AND SUCCULENTS  `cactus_and_succulents`
- правило: Desert plants that store water in thick leaves or stems
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~agave, ~aloe, ~barrel cactus, ~cactus, ~hens and chicks, ~jade, ~prickly pear, ~yucca, !cholla, !echeveria, !saguaro, !sedum

### FARM CROPS  `crops`
- правило: Plants grown on farms for food or material
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +alfalfa, +barley, +canola, +corn, +cotton, +flax, +hay, +millet, +oat, +peanut, +potato, +rice, +rye, +sorghum, +soybean, +sugarcane, +sunflower, +wheat

### EVERGREEN TREES  `evergreens`
- правило: Trees that keep their leaves or needles all year
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +cedar, +cypress, +fir, +hemlock, +holly, +juniper, +laurel, +magnolia, +pine, +redwood, +sequoia, +spruce, +yew, !arborvitae

### FRUIT TREES  `fruit_trees`
- правило: Trees grown for their edible fruit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +almond, +apple (apple_fruit), +apricot, +avocado, +banana, +cherry, +coconut, +fig, +lemon, +lime, +mango, +olive, +orange (orange_fruit), +peach, +pear, +pecan, +plum, +walnut

### GARDEN CENTER  `garden_center`
- правило: What a garden center sells or what you buy there
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- +flowers, +houseplants, +seedling, +soil, +trees, +trowel, !weeds

### SPRING FLOWERS  `garden_flowers_spring`
- правило: Flowers that bloom in spring
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~crocus, ~snowdrop, +azalea, +bluebell, +cherry blossom, +daffodil, +hyacinth, +iris, +lilac, +magnolia, +pansy, +primrose, +tulip, !forsythia

### SUMMER FLOWERS  `garden_flowers_summer`
- правило: Flowers that bloom in summer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~hydrangea, ~petunia, +black eyed susan, +cosmos, +dahlia, +Daisy, +geranium, +lavender (lavender_plant), +Lily, +marigold, +rose, +snapdragon, +sunflower, !zinnia

### GARDEN IN BLOOM  `garden_in_bloom`
- правило: A word belonging to a garden in bloom
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +bloom, +blossom, +bud, +flower, +garden, +petal, +pollen

### GARDENING WORDS  `gardening_words`
- правило: Words used when growing a garden
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +bed, +compost, +fertilizer, +greenhouse, +harvest, +hose, +mulch, +pot, +prune, +row, +seed, +shade, +soil, +sprout, +sunlight, +trellis, +water, +weed

### GRASSES  `grasses`
- правило: Kinds of grass and grain plants
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bamboo, ~barley, ~Bermuda, ~bluegrass, ~corn, ~oat, ~reed, ~rice, ~rye, ~sugarcane, ~wheat, !crabgrass, !fescue, !ryegrass

### COOKING HERBS  `herbs`
- правило: Leafy plants grown to flavor food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~chive, ~lavender (lavender_plant), ~lemongrass, ~marjoram, ~tarragon, +basil, +bay, +cilantro, +dill, +mint (mint_herb), +oregano, +parsley, +rosemary, +sage (sage_herb), +thyme

### HOUSEPLANTS  `houseplants`
- правило: Plants commonly kept indoors in pots
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~begonia, ~palm (palm_tree), ~philodendron, +aloe, +bamboo, +cactus, +Fern, +geranium, +Ivy, +jade, +orchid, +peace lily, +rubber plant, +snake plant, +spider plant, +succulent, +Violet, !pothos

### KINDS OF PLANTS  `kinds_of_plants`
- правило: A broad kind of plant that grows from the ground
- тип связи: `is_a`, базовая сложность 0.25
- слов: 7
- +Bush, +flower, +grass, +Ivy, +moss, +shrub, +tree

### LEAF WORDS  `leaf_shapes`
- правило: Words describing leaves and how they grow
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~blade, ~bud, ~canopy, ~deciduous, ~evergreen, ~foliage, ~lobe, ~needle (needle_pine), ~sprout, ~stalk, ~stem, ~vein, !broadleaf, !frond

### MUSHROOM TYPES  `mushroom_types`
- правило: Kinds of edible and wild mushrooms
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~morel, ~oyster, ~portobello, ~truffle, !button (button_mushroom), !chanterelle, !enoki, !porcini, !puffball, !shiitake, !toadstool, xcremini

### PLANT PARTS  `plant_parts`
- правило: Parts of a growing plant
- тип связи: `part_of`, базовая сложность 0.25
- слов: 16
- ~bark (bark_tree), ~tendril, +bud, +flower, +fruit, +leaf, +node, +petal, +pollen, +root, +seed, +sprout, +stalk, +stem, +thorn, +vine

### POISONOUS PLANTS  `poisonous_plants`
- правило: Plants that are dangerous to touch or eat
- тип связи: `has_property`, базовая сложность 0.4
- слов: 12
- ~castor bean, ~hemlock, ~holly berry, ~mistletoe, ~nightshade, ~poison ivy, ~poison oak, ~yew, !foxglove, !monkshood, !oleander, !sumac

### SEEDS AND BULBS  `seeds_and_bulbs`
- правило: Plant parts you put in the ground to grow a new plant
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~rhizome, ~sapling, +acorn, +bulb, +clove, +cutting, +kernel, +pit, +seed, +seedling, +spore, +sprout, +tuber, !corm

### SHRUBS AND BUSHES  `shrubs`
- правило: Woody plants smaller than a tree
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~azalea, ~hedge, ~holly, ~hydrangea, ~juniper, ~lilac, ~rhododendron, +rose, !barberry, !boxwood, !forsythia, !privet, !spirea, !viburnum

### TROPICAL PLANTS  `tropical_plants`
- правило: Plants that grow in tropical climates
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~palm (palm_tree), +bamboo, +banana, +banyan, +cocoa, +coffee, +Fern, +hibiscus, +mangrove, +orchid, +papaya, +rubber tree, !bromeliad, !plumeria

### VINES AND CLIMBERS  `vines`
- правило: Plants that climb or trail along a surface
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bean, ~clematis, ~cucumber, ~grape, ~honeysuckle, ~hops, ~Ivy, ~Jasmine, ~morning glory, ~passion flower, ~pea, ~pumpkin, ~wisteria, !kudzu

### WATER PLANTS  `water_plants`
- правило: Plants that grow in or on water
- тип связи: `found_in`, базовая сложность 0.35
- слов: 13
- +algae, +kelp, +lily pad, +lotus, +moss, +papyrus, +reed, +seaweed, +water lily, +watercress, !cattail, !duckweed, !eelgrass

### WEEDS  `weeds`
- правило: Unwanted plants that grow in lawns and gardens
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~ragweed, +clover, +dandelion, +Ivy, +moss, +nettle, +plantain, +poison ivy, +thistle, !bindweed, !chickweed, !crabgrass, !foxtail, !purslane


## Тема: skills

### CARD TRICKS  `card_tricks`
- правило: Terms used in performing card tricks
- тип связи: `found_in`, базовая сложность 0.5
- слов: 12
- ~control, ~cut, ~double lift, ~false shuffle, ~flourish, ~force, ~pass, ~reveal, ~spread, !palm (palm_hand), !shuffle (shuffle_cards), !sleight

### COCKTAILS  `cocktails`
- правило: Named mixed drinks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 17
- ~daiquiri, ~negroni, ~pina colada, +bloody mary, +cosmopolitan, +mai tai, +manhattan, +margarita, +martini, +mimosa, +mojito, +moscow mule, +old fashioned, +sangria, +tom collins, +whiskey sour, xteas

### DANCE MOVES  `dance_moves`
- правило: Named dance moves
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~moonwalk, ~shuffle (shuffle_dance), +dip, +floss, +hustle, +jump, +kick, +robot, +slide, +spin, +split, +tap (tap_dance), +turn, +twist, !wave (wave_dance)

### DRIVING SKILLS  `driving_skills`
- правило: Skills tested on a driving exam
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- +backing up, +hill start, +lane change, +merging, +mirror check, +parallel parking, +signaling, +stopping, +three point turn, +u turn, +yielding

### AID ACTIONS  `first_aid_actions`
- правило: Actions taken when giving first aid
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~immobilize, ~monitor (monitor_medical), +bandage, +call, +check pulse, +compress, +cool, +cover, +CPR, +disinfect, +elevate, +ice, +rinse, +splint

### JUGGLING WORDS  `juggling_words`
- правило: Words used in juggling
- тип связи: `found_in`, базовая сложность 0.5
- слов: 13
- ~ball (ball_sphere), ~cascade, ~catch, ~club (club_stick), ~drop, ~flash, ~pattern, ~scarf, ~shower, ~throw, ~toss, !diabolo, !ring (ring_circle)

### KITCHEN SKILLS  `kitchen_skills`
- правило: Practical skills used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~basting, ~filleting, ~garnishing, ~kneading, ~whisking, +chopping, +folding, +measuring, +plating, +seasoning, +sharpening, +tempering, +timing, !portioning

### KNOT TYING  `knot_tying`
- правило: A named knot or a way rope behaves
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~overhand, +hitch, +lasso, +slipknot, +tangle

### KNOTS  `knots`
- правило: Named knots tied in rope
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- ~clove hitch, ~figure eight, ~fisherman knot, ~granny knot, ~half hitch, ~sheet bend, ~slip knot, ~square knot, ~taut line, ~timber hitch, ~trucker hitch, !bowline, !overhand

### PIZZA STYLES  `pizza_styles`
- правило: Regional styles of pizza
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~flatbread, +California, +chicago deep dish, +Detroit, +neapolitan, +new york, +sicilian, +stuffed crust, +tavern, +thin crust, !calzone, !focaccia

### POKER HANDS  `poker_hands`
- правило: Hands that can be dealt in poker
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- +flush, +four of a kind, +full house, +high card, +pair, +royal flush, +straight, +straight flush, +three of a kind, +two pair

### SELF DEFENSE  `self_defense_moves`
- правило: Basic self defense moves
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~elbow, ~escape, ~grab release, ~kick, ~knee, ~palm strike, ~roll (roll_turn), ~stance, ~stomp, ~strike (strike_hit), ~throw, !block (block_stop)

### SURVIVAL SKILLS  `survival_skills`
- правило: Skills used to survive outdoors
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~orienteering, +fire starting, +first aid, +fishing, +foraging, +knot tying, +navigation, +shelter building, +signaling, +tracking, +trapping, +water purification

### SWIMMING SKILLS  `swimming_skills`
- правило: Skills learned in swimming lessons
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~stroke (stroke_swim), +backstroke, +bobbing, +breathing, +diving, +floating, +gliding, +jumping, +kicking, +rescue, +treading, +turning

### OFFICE SKILLS  `typing_and_office_skills`
- правило: Practical skills useful in an office job
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +answering phones, +budgeting, +data entry, +emailing, +filing, +note taking, +organizing, +presenting, +proofreading, +scheduling, +spreadsheets, +typing

### WEAVING  `weaving`
- правило: A tool, worker or product of weaving cloth
- тип связи: `used_in`, базовая сложность 0.6
- слов: 5
- +loom, +spindle, +tapestry, +warp, +weaver

### YOGA POSES  `yoga_poses`
- правило: Named poses used in yoga
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~boat, ~child, ~cobra, ~crow, ~downward dog, ~half moon, ~lotus, ~mountain, ~pigeon, ~plank, ~tree, ~triangle, ~warrior, !bridge (bridge_move)


## Тема: species

### ANIMAL CLASSES  `animal_classes`
- правило: One of the broad classes animals are sorted into
- тип связи: `member_of_set`, базовая сложность 0.35
- слов: 6
- +amphibian, +bird, +fish, +insect, +mammal, +reptile

### BEARS  `bears_and_big_animals`
- правило: Kinds of bear
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- ~spectacled bear, +black bear, +brown bear, +grizzly, +koala, +kodiak, +panda, +polar, +sloth bear, +sun bear

### BIRD WATCHING  `bird_watching`
- правило: What a birdwatcher looks for and looks through
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +binoculars, +feeder, +nest, +owls, +seabirds, +songbirds, +waterfowl

### BIRDS OF PREY  `birds_of_prey`
- правило: Birds that hunt other animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 13
- ~goshawk, ~kestrel, +buzzard, +condor, +eagle, +falcon, +harrier, +hawk, +kite (kite_bird), +merlin, +osprey, +owl, +vulture

### BUTTERFLIES AND MOTHS  `butterflies_and_moths`
- правило: Kinds of butterfly and moth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +admiral, +buckeye, +cabbage white, +luna moth, +monarch, +painted lady, +skipper, +sphinx moth, +spongy moth, +viceroy, !fritillary, !swallowtail

### CAT BREEDS  `cat_breeds`
- правило: Breeds of domestic cat
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~abyssinian, ~ragdoll, +bengal, +bombay, +burmese, +calico, +himalayan, +maine coon, +manx, +persian, +russian blue, +siamese, +tabby, !birman, !sphynx

### FARM BREEDS  `cattle_and_farm_breeds`
- правило: Breeds of cattle, sheep and pigs raised on farms
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- ~angus, ~berkshire, ~dorset, ~guernsey, ~hereford, ~jersey, ~suffolk, !brahman, !duroc, !holstein, !longhorn, !merino, !shorthorn

### DEER FAMILY  `deer_family`
- правило: Animals of the deer family
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +antelope, +buck, +caribou, +deer, +doe, +elk, +fawn, +gazelle, +impala, +moose, +reindeer, +roe deer, +stag, !muntjac

### PREHISTORIC ANIMALS  `extinct_and_prehistoric`
- правило: Animals that lived in prehistoric times
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~ammonite, ~megalodon, ~pterosaur, ~trilobite, +cave bear, +dire wolf, +dodo, +giant sloth, +mammoth, +mastodon, +saber tooth, ?glyptodon

### CHICKEN BREEDS  `farm_poultry_breeds`
- правило: Breeds of chicken raised on farms
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- ~plymouth rock, ~rhode island red, ~sussex, ?australorp, !bantam, !brahma, !leghorn, !orpington, !silkie, !wyandotte

### FROGS AND TOADS  `frogs_and_toads`
- правило: Kinds of frog and toad
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~bullfrog, ~cane toad, ~green frog, ~leopard frog, ~poison dart, ~toad, ~tree frog, ~wood frog, !pickerel frog, !spring peeper

### HORSE BREEDS  `horse_breeds`
- правило: Breeds of horse
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~andalusian, ~clydesdale, +Arabian, +Morgan, +Mustang, +paint, +pinto, +quarter horse, +shetland, +thoroughbred, !appaloosa, !friesian, !palomino, !percheron

### LIZARDS  `lizards`
- правило: Kinds of lizard
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- ~skink, +bearded dragon, +chameleon, +gecko, +gila monster, +horned lizard, +iguana, +komodo dragon, +salamander, !anole, !monitor (monitor_lizard)

### MONKEYS AND APES  `monkeys_and_apes`
- правило: Kinds of monkey and ape
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~bonobo, ~capuchin, ~macaque, ~mandrill, ~marmoset, ~tamarin, +baboon, +chimpanzee, +gibbon, +gorilla, +howler, +lemur, +orangutan, +spider monkey

### OWLS  `owls`
- правило: Kinds of owl
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- +barn owl, +barred owl, +burrowing owl, +elf owl, +great horned, +long eared, +screech owl, +snowy owl, +spotted owl, +tawny owl

### FRESHWATER FISH  `pond_fish`
- правило: Fish that live in lakes and rivers
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~bluegill, ~crappie, ~muskie, ~sunfish, +bass (bass_fish), +carp, +catfish, +gar, +koi, +minnow, +perch, +pike, +sturgeon, +trout, +walleye

### RODENT SPECIES  `rodent_species`
- правило: Particular kinds of rodent
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +chipmunk, +field mouse, +flying squirrel, +gray squirrel, +groundhog, +house mouse, +porcupine, +prairie dog, +vole, !capybara, !dormouse, !jerboa, !lemming

### SNAKES  `snakes`
- правило: Kinds of snake
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~copperhead, ~sidewinder, +adder, +anaconda, +boa, +cobra, +coral snake, +garter, +king snake, +mamba, +python, +rattlesnake, +viper, ?bullsnake

### SONGBIRDS  `songbirds`
- правило: Small singing birds found in yards and woods
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~oriole, +bluebird, +canary, +cardinal (cardinal_bird), +chickadee, +finch, +lark, +mockingbird, +robin, +sparrow, +starling, +swallow (swallow_bird), +thrush, +warbler, +wren, !junco, !nuthatch

### SPIDERS AND CRAWLERS  `spiders_and_crawlers`
- правило: Small many-legged creatures that are not insects
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~millipede, +Black Widow, +brown recluse, +centipede, +mite, +scorpion, +spider, +tarantula, +tick (tick_bug), +wolf spider, !daddy longlegs, xharvestman

### WHALE TYPES  `whale_types`
- правило: Kinds of whale
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~minke, ~narwhal, +beluga, +blue whale, +fin whale, +gray whale, +humpback, +orca, +pilot whale, +right whale, +sperm whale, !bowhead

### WILD DOGS  `wild_dogs`
- правило: Wild members of the dog family
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- ~fennec, ~maned wolf, +arctic fox, +coyote, +dingo, +fox, +gray wolf, +hyena, +jackal, +red fox, +wolf


## Тема: sports

### AT THE GYM  `at_the_gym`
- правило: A machine, weight or person found in a gym
- тип связи: `found_in`, базовая сложность 0.3
- слов: 7
- +barbell, +bench (bench_seat), +dumbbell, +squat, +trainer, +treadmill, +weights

### AT THE POOL  `at_the_pool`
- правило: Something you find at a swimming pool
- тип связи: `found_in`, базовая сложность 0.3
- слов: 7
- +cap, +dive, +flippers, +goggles, +lane, +pool, +swimsuit

### BASEBALL EQUIPMENT  `baseball_equipment`
- правило: Physical equipment used to play a game of baseball
- тип связи: `used_in`, базовая сложность 0.25
- слов: 15
- ~ball (ball_sphere), +base, +bat (bat_equipment), +batting glove, +cap, +chest protector, +cleats, +glove, +helmet, +mask, +mitt, +pine tar, +plate (plate_base), +rosin bag, +shin guard

### BASEBALL WORDS  `baseball_words`
- правило: Words used to describe plays, places or roles in a baseball game
- тип связи: `found_in`, базовая сложность 0.3
- слов: 28
- ~diamond (diamond_field), +batter, +bullpen, +bunt, +catcher, +curveball, +double play, +dugout, +error, +fastball, +foul, +grand slam, +home run, +infield, +inning, +lineup, +mound (mound_baseball), +outfield, +pitch (pitch_throw), +pitcher (pitcher_baseball), +shortstop, +slider, +steal, +strike (strike_baseball), +triple, +umpire, +walk, !single (single_baseball)

### BASKETBALL WORDS  `basketball_words`
- правило: Words used to describe plays and roles in basketball
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~court (court_sport), ~guard (guard_sport), +assist, +backboard, +buzzer, +center, +dribble, +dunk (dunk_basketball), +forward, +foul, +free throw, +hoop, +jump ball, +layup, +rebound, +three pointer, +timeout, +travel, !block (block_stop), !screen (screen_basketball)

### BILLIARDS  `billiards`
- правило: A term belonging to billiards and snooker
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- +chalked, +felt, +potting, +snooker

### GAMES OF SKILL  `board_and_card_games`
- правило: Competitive indoor games of skill
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~backgammon, ~bridge (bridge_card), ~cornhole, ~foosball, ~shuffleboard, +air hockey, +billiards, +bowling, +checkers, +chess, +darts, +dominoes, +poker, +table tennis

### BOXING GYM  `boxing_gym`
- правило: A term or piece of kit used in boxing training
- тип связи: `used_in`, базовая сложность 0.55
- слов: 5
- ~mouthguard, +clinch, +southpaw, +spar, +sparring

### OUTDOOR ACTIVITIES  `camping_and_outdoors`
- правило: Recreational activities done outdoors
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~birdwatching, ~geocaching, ~picnicking, +backpacking, +biking, +camping, +canoeing, +climbing, +fishing, +hiking, +hunting, +kayaking, +rafting, +running, +sailing, +skiing, +snorkeling, +surfing

### CLIMBING WALL  `climbing_wall`
- правило: A term or piece of kit used in climbing
- тип связи: `used_in`, базовая сложность 0.6
- слов: 5
- ~belay, ~carabiner, ~rappel, +ascent, +foothold

### CYCLING WORDS  `cycling_words`
- правило: Words used about riding and racing bicycles
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +brake, +cadence, +chain, +drafting, +gear, +handlebar, +helmet, +jersey, +pedal, +peloton, +saddle, +spoke, +sprint, +tire, +tour, +trail

### DARTS WORDS  `darts_words`
- правило: A term or piece of equipment used in darts
- тип связи: `used_in`, базовая сложность 0.45
- слов: 6
- +board (board_game), +bullseye, +flight, +score (score_points), +Target, +throw

### FISHING THINGS  `fishing_things`
- правило: Things used to catch fish
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~bobber, ~fly (fly_lure), ~waders, +bait, +boat, +cooler, +hook (hook_fishing), +line (line_cord), +lure, +net, +pole, +reel (reel_fishing), +rod, +sinker, +spear, +tackle box, +trap, +worm

### FOOTBALL WORDS  `football_words`
- правило: Words used to describe plays and roles in American football
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~sack (sack_football), +blitz, +down, +end zone, +field goal, +fumble, +helmet, +huddle, +interception, +kickoff, +lineman, +punt, +quarterback, +receiver, +referee, +safety, +snap, +tackle, +touchdown, +yard line

### GOLF WORDS  `golf_words`
- правило: Words used to describe play and equipment in golf
- тип связи: `found_in`, базовая сложность 0.3
- слов: 21
- ~bunker (bunker_golf), ~green (green_golf), ~iron (iron_golf), +birdie, +bogey, +caddie, +caddy, +club (club_stick), +course, +driver, +eagle, +fairway, +flag, +hole, +hole in one, +par, +putter, +rough, +sand trap, +tee, +wedge

### GYM EQUIPMENT  `gym_equipment`
- правило: Equipment used for exercise in a fitness gym
- тип связи: `used_in`, базовая сложность 0.25
- слов: 19
- ~kettlebell, +barbell, +dumbbell, +elliptical, +foam roller, +jump rope, +mat, +medicine ball, +pull up bar, +punching bag, +resistance band, +rope, +rowing machine, +stair climber, +stationary bike, +treadmill, +weights, !bench (bench_seat), !club (club_stick)

### HOCKEY WORDS  `hockey_words`
- правило: Words used to describe plays and gear in ice hockey
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~zamboni, +blue line, +crease, +faceoff, +goalie, +helmet, +icing, +net, +pad, +penalty box, +period, +power play, +puck, +rink, +skate, +stick (stick_hockey), !check (check_hockey), !slapshot

### MARATHON DAY  `marathon_day`
- правило: A word belonging to running a long distance race
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +finisher, +jog, +pacer, +stamina

### MARTIAL ARTS  `martial_arts`
- правило: Fighting sports and self defense disciplines
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~capoeira, ~kendo, +aikido, +boxing, +fencing, +judo, +jujitsu, +karate, +kickboxing, +kung fu, +muay thai, +sumo, +taekwondo, +wrestling

### OLYMPIC SPORTS  `olympic_sports`
- правило: Sports contested at the modern Olympic Games
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~bobsled, +archery, +badminton, +biathlon, +boxing, +canoeing, +curling, +diving, +fencing, +gymnastics, +hurdles, +javelin, +judo, +luge, +marathon, +rowing, +sailing, +shot put, +skating, +skiing, +swimming, +taekwondo, +triathlon, +weightlifting, +wrestling

### RACING SPORTS  `racing_sports`
- правило: Sports where competitors race to finish first
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +cross country, +cycling, +dog sled racing, +drag racing, +horse racing, +hurdles, +marathon, +motocross, +relay, +rowing, +sailing, +speed skating, +sprint, +swimming, +triathlon

### SKATE PARK  `skate_park`
- правило: A ramp or piece of kit found at a skate park
- тип связи: `found_in`, базовая сложность 0.6
- слов: 6
- ~griptape, ~halfpipe, ~longboard, ~skatepark, +kicker, +vert

### SOCCER WORDS  `soccer_words`
- правило: Words used to describe plays and roles in soccer
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~pitch (pitch_field), +assist, +corner kick, +defender, +dribble, +free kick, +goal, +goalkeeper, +header, +midfielder, +net, +offside, +penalty, +red card, +striker, +throw in, +whistle, +yellow card

### BALLS  `sports_balls`
- правило: Balls used in different sports
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- +baseball, +basketball, +beach ball, +bowling ball, +cricket ball, +football, +golf ball, +medicine ball, +ping pong ball, +rugby ball, +soccer ball, +softball, +tennis ball, +volleyball

### PROTECTIVE GEAR  `sports_gear_worn`
- правило: Gear athletes wear to protect the body
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~mouthguard, +brace, +chest protector, +cup, +elbow pad, +glove, +goggles, +harness, +helmet, +knee pad, +mask, +pad, +shin guard, +wrist guard

### SPORTS OFFICIALS  `sports_officials`
- правило: People who enforce the rules of a sport
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~timekeeper, +judge, +linesman, +marshal, +official, +referee, +scorer, +starter, +steward, +umpire

### SCORING WORDS  `sports_scoring`
- правило: Words used for scoring and results in sports
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~lead (lead_front), ~point (point_score), +championship, +comeback, +draw, +goal, +loss, +medal, +overtime, +playoff, +ranking, +record, +score (score_points), +shutout, +standing, +streak, +title, +trophy, +win, !tie (tie_score)

### SPORTS VENUES  `sports_venues`
- правило: Places built for playing or watching sports
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~diamond (diamond_field), ~pitch (pitch_field), ~ring (ring_arena), +alley, +arena, +ballpark, +course, +dojo, +dome, +field, +gym, +pool, +racetrack, +rink, +stadium, +track, +velodrome, !court (court_sport)

### TEAM SPORTS  `team_sports`
- правило: Sports played by two opposing teams
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- +baseball, +basketball, +cricket, +dodgeball, +field hockey, +football, +handball, +hockey, +kickball, +lacrosse, +netball, +polo, +rugby, +soccer, +softball, +ultimate frisbee, +volleyball, +water polo

### TENNIS WORDS  `tennis_words`
- правило: Words used to describe play and scoring in tennis
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~tiebreak, +Ace, +backhand, +baseline, +court (court_sport), +deuce, +fault, +forehand, +lob, +love, +match point, +net, +racket, +rally, +serve, +set (set_tennis), +umpire, +volley

### WATER SPORTS  `water_sports`
- правило: Sports played in or on the water
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~paddleboarding, ~wakeboarding, ~windsurfing, +canoeing, +diving, +kayaking, +rafting, +rowing, +sailing, +snorkeling, +surfing, +swimming, +synchronized swimming, +water polo, +water skiing

### WINTER FUN  `winter_fun`
- правило: Something you play with or wear for fun in the snow
- тип связи: `used_in`, базовая сложность 0.3
- слов: 6
- ~icicle, +mittens, +skates, +skis, +sled, +snowman

### WINTER SPORTS  `winter_sports`
- правило: Sports played on snow or ice
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~bobsled, ~snowshoeing, ~tobogganing, +biathlon, +curling, +figure skating, +hockey, +ice climbing, +luge, +skating, +skiing, +sled, +sledding, +snowboard, +snowboarding, +speed skating


## Тема: time

### BIRTHDAY THINGS  `birthday_things`
- правило: Things associated with a birthday celebration
- тип связи: `found_in`, базовая сложность 0.2
- слов: 16
- ~card (card_greeting), ~present (present_gift), +balloon, +cake, +candle, +confetti, +guest, +hat, +ice cream, +invitation, +party (party_event), +piñata, +song, +streamer, +surprise, +wish

### CALENDAR WORDS  `calendar_words`
- правило: Everyday English words for dates and periods of time on a calendar
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~quarter (quarter_fourth), ~term (term_period), +anniversary, +birthday, +century, +date (date_calendar), +day, +decade, +era, +fortnight, +holiday, +leap year, +millennium, +month, +season (season_time), +semester, +spring (spring_season), +week, +weekday, +weekend, +workweek, +year

### CHRISTMAS THINGS  `christmas_things`
- правило: Things associated with an American Christmas
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~star (star_shape), +candy cane, +carol, +chimney, +eggnog, +elf, +garland, +gift, +gingerbread, +lights, +mistletoe, +nutcracker, +ornament, +reindeer, +sleigh, +snowman, +stocking, +tinsel, +tree, +wreath

### CLOCK WORDS  `clock_words`
- правило: Words and parts having to do with clocks
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~sundial, +alarm, +chime, +cuckoo, +dial, +face, +hour hand, +hourglass, +minute hand, +pendulum, +second hand, +snooze, +stopwatch, +tick (tick_sound), +timer, !hand (hand_clock)

### DAYS & TIMES  `days_and_parts_of_day`
- правило: Names of weekdays and parts of the day
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- +afternoon, +dawn, +dusk, +evening, +Friday, +midnight, +Monday, +morning, +night, +noon, +Saturday, +Sunday, +sunrise, +sunset, +Thursday, +Tuesday, +twilight, +Wednesday

### HALLOWEEN THINGS  `halloween_things`
- правило: Things associated with Halloween
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~bat (bat_animal), +black cat, +broom, +candy, +cauldron, +cobweb, +costume, +ghost, +haunted house, +jack o lantern, +mask, +pumpkin, +skeleton, +spider, +tombstone, +treat, +trick, +vampire, +witch, +zombie

### HISTORICAL ERAS  `historical_eras`
- правило: Named periods of human history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Antiquity, +Bronze Age, +Colonial, +Dark Ages, +Great Depression, +Ice Age, +Industrial Revolution, +Iron Age, +Middle Ages, +renaissance, +Roaring Twenties, +Space Age, +Stone Age, +Victorian

### HOLIDAYS  `holidays`
- правило: Holidays widely celebrated in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~Juneteenth, ~Kwanzaa, +April Fools, +Christmas, +Columbus Day, +Easter, +Fathers Day, +Groundhog Day, +Halloween, +Hanukkah, +Independence Day, +Labor Day, +Memorial Day, +Mothers Day, +New Year, +Passover, +Presidents Day, +Thanksgiving, +Valentine's Day, +Veterans Day

### MONTHS  `months`
- правило: Months of the Gregorian calendar year
- тип связи: `is_a`, базовая сложность 0.1
- слов: 12
- +April, +August, +December, +February, +January, +July, +June, +march (march_month), +may, +November, +October, +September

### NEW YEAR  `new_year_things`
- правило: Things associated with New Year celebrations
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~noisemaker, ~sparkler, +ball drop, +calendar, +champagne, +confetti, +countdown, +fireworks, +kiss, +midnight, +party (party_event), +resolution, +streamer, !toast (toast_salute)

### TIME WORDS  `past_and_future`
- правило: Words that place something in time
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +after, +already, +always, +before, +early, +forever, +late, +later, +meanwhile, +never, +now, +once, +recently, +soon, +still, +today, +tomorrow, +yesterday

### SEASONS  `seasons`
- правило: The four seasons of the year
- тип связи: `is_a`, базовая сложность 0.15
- слов: 5
- +Autumn, +fall, +spring (spring_season), +summer, +winter

### QUICK WORDS  `speed_of_time`
- правило: Words meaning that something happens without delay
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~abruptly, ~at once, ~hastily, ~immediately, ~instantly, ~momentarily, ~promptly, ~quickly, ~right away, ~shortly, ~suddenly, ~swiftly

### SPRING SEASON  `spring_season`
- правило: Something you associate with the spring season
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 6
- +nest, +puddle, +rain, +sprout, +thaw, +warmth

### SUMMER SEASON  `summer_season`
- правило: Something you associate with the summer season
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 6
- +August, +beach, +heat, +July, +June, +sun

### UNITS OF TIME  `time_units`
- правило: Units used to measure time
- тип связи: `is_a`, базовая сложность 0.2
- слов: 16
- ~quarter (quarter_fourth), +century, +day, +decade, +era, +generation, +hour, +instant, +millennium, +minute (minute_time), +moment, +month, +second (second_time), +semester, +week, +year

### WEDDING THINGS  `wedding_things`
- правило: Things associated with a wedding
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- +aisle, +altar, +best man, +bouquet, +bride, +bridesmaid, +cake, +ceremony, +dress, +garter, +groom (groom_wedding), +honeymoon, +invitation, +reception, +rice, +ring (ring_jewelry), +tuxedo, +veil, +vows, !toast (toast_salute)


## Тема: transport

### AIRCRAFT  `aircraft`
- правило: Machines that fly through the air carrying people or cargo
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~biplane, +airplane, +airship, +balloon, +blimp, +cargo plane, +drone, +glider, +helicopter, +jet, +rocket, +seaplane, +shuttle, +ultralight, +Zeppelin

### AIRPORT WORDS  `airport_words`
- правило: Words for things, places or roles you encounter at an airport
- тип связи: `found_in`, базовая сложность 0.25
- слов: 30
- ~currencies, ~gate (gate_airport), ~jetway, ~languages, +aircraft, +airlines, +aisle, +baggage, +boarding, +boarding pass, +carousel, +checkpoint, +cockpit, +concourse, +control tower, +customs, +duty free, +hangar, +layover, +luggage, +passport, +pilot, +runway, +seatbelt, +security, +steward, +tarmac, +terminal, +ticket (ticket_admission), +tray table

### BOATS AND SHIPS  `boats`
- правило: Kinds of watercraft
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~rowboat, +barge, +boat, +canoe, +catamaran, +cruise ship, +dinghy, +ferry, +freighter, +gondola, +houseboat, +kayak, +motorboat, +raft, +sailboat, +schooner, +ship, +speedboat, +submarine, +trawler, +tugboat, +yacht

### CAR PARTS  `car_parts`
- правило: Physical parts of an ordinary passenger car
- тип связи: `part_of`, базовая сложность 0.2
- слов: 25
- ~gearshift, ~glovebox, +axle, +battery, +brake, +bumper, +clutch, +dashboard, +door, +engine, +exhaust, +fender, +headlight, +hood (hood_car), +horn (horn_sound), +ignition, +mirror, +muffler, +radiator, +seat, +tire, +trunk (trunk_car), +wheel, +windshield, +wiper

### CONSTRUCTION EQUIPMENT  `construction_equipment`
- правило: Large machines used on a building or road construction site
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~backhoe, ~compactor, ~paver, +bulldozer, +cement, +cement mixer, +crane (crane_machine), +digger, +drill rig, +dump truck, +excavator, +forklift, +grader, +hoist, +jackhammer, +loader, +roller, +scaffold, !trencher

### EMERGENCY VEHICLES  `emergency_vehicles`
- правило: Vehicles used by emergency services
- тип связи: `is_a`, базовая сложность 0.25
- слов: 12
- +ambulance, +cruiser, +fire truck, +hazmat truck, +helicopter, +ladder truck, +paramedic van, +patrol car, +police car, +rescue boat, +squad car, +tow truck

### GAS STATION  `gas_station_things`
- правило: Things found at an American gas station
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~squeegee, +air hose, +car wash, +coffee, +credit card reader, +diesel, +gas, +ice machine, +map, +nozzle, +oil (oil_motor), +pump, +receipt, +restroom, +snack, +windshield fluid

### TRUCKS  `heavy_trucks`
- правило: Kinds of truck used to move goods and materials
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +box truck, +cement mixer, +delivery truck, +dump truck, +flatbed, +garbage truck, +logging truck, +moving truck, +pickup, +refrigerated truck, +semi, +tanker, +tow truck, +van

### HOTEL WORDS  `hotel_words`
- правило: Things and roles found at a hotel
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~bellhop, ~minibar, +balcony (balcony_house), +buffet, +checkout, +concierge, +elevator, +front desk, +housekeeping, +key card, +lobby, +luggage cart, +pool, +reception, +room service, +suite, +vacancy, +valet

### ON THE ROAD  `on_the_road`
- правило: Something a driver meets on the road
- тип связи: `found_in`, базовая сложность 0.3
- слов: 7
- +brake, +crosswalk, +highway, +lane, +road, +signal, +traffic

### PARKING WORDS  `parking_words`
- правило: Words used about parking a car
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~stall (stall_parking), +curb, +driveway, +garage, +handicap, +lot, +meter, +permit, +ramp, +sign, +space, +spot, +ticket (ticket_fine), +tow, +valet, !boot (boot_clamp)

### BICYCLE PARTS  `parts_of_a_bike`
- правило: Physical parts of a bicycle
- тип связи: `part_of`, базовая сложность 0.3
- слов: 18
- ~kickstand, +basket, +bell, +brake, +chain, +crank, +fork, +frame, +gear, +handlebar, +pedal, +reflector, +rim, +saddle, +seat, +spoke, +tire, +wheel

### ROAD THINGS  `road_things`
- правило: Things you see on or beside a road
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~guardrail, ~shoulder (shoulder_road), ~streetlight, +bridge (bridge_structure), +cone, +crosswalk, +curb, +exit, +intersection, +lane, +median, +mile marker, +pothole, +ramp, +sidewalk, +sign, +speed bump, +toll booth, +traffic light, +tunnel

### SAILING WORDS  `sailing_words`
- правило: Words used aboard a sailing boat
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~anchor, ~boom, ~buoy, ~cabin (cabin_ship), ~deck, ~helm, ~hull, ~keel, ~knot, ~mast, ~oar, ~port, ~rope, ~rudder, ~sail (sail_cloth), ~starboard, ~stern, !bow (bow_ship)

### SPACE TRAVEL  `space_travel`
- правило: Things involved in traveling into space
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~spacesuit, ~station (station_place), +astronaut, +booster, +capsule, +countdown, +docking, +gravity, +lander, +launch, +mission, +module, +orbit, +rocket, +rover, +satellite, +shuttle, +telescope

### PEOPLE MOVERS  `things_that_carry_people`
- правило: Things built to carry a person from one place to another
- тип связи: `does_action`, базовая сложность 0.35
- слов: 18
- ~cable car, ~chairlift, ~elevator, ~escalator, ~ferry, ~gondola, ~moving walkway, ~plane (plane_aircraft), ~rickshaw, ~sled, ~stretcher, ~taxi, ~tram, ~wheelchair, +boat, +bus, +horse, +train

### THINGS WITH WHEELS  `things_with_wheels`
- правило: Everyday objects that have wheels as a normal part of their design
- тип связи: `has_property`, базовая сложность 0.25
- слов: 25
- ~cart, ~dolly, ~forklift, ~golf cart, ~gurney, ~lawnmower, ~roller skate, ~scooter, ~skateboard, ~stroller, ~suitcase, ~tractor, ~trailer (trailer_vehicle), ~tricycle, ~unicycle, ~wagon, ~wheelbarrow, ~wheelchair, +bike, +bus, +car, +train, +truck, +van, !rollerblade

### TRAFFIC SIGNS  `traffic_signs`
- правило: Signs that direct drivers on the road
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +crossing, +curve ahead, +dead end, +detour, +do not enter, +exit, +merge, +no parking, +one way, +railroad, +school zone, +slow, +speed limit, +stop, +yield

### TRAIN WORDS  `train_words`
- правило: Words for the parts, places and roles of railway travel
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~boxcar, +caboose, +conductor, +coupling, +crossing, +depot, +engine, +freight, +locomotive, +platform, +rail, +sleeper car, +station (station_place), +switch, +ticket (ticket_admission), +track, +tunnel, +whistle

### TRAVEL THINGS  `travel_documents`
- правило: Things a traveler packs or carries on a trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- +adapter, +backpack, +boarding pass, +camera, +Charger, +currency, +guidebook, +insurance, +itinerary, +map, +neck pillow, +passport, +suitcase, +sunglasses, +ticket (ticket_admission), +toiletries, +Visa, +wallet

### VEHICLES  `vehicles`
- правило: Machines built to carry people or goods from place to place
- тип связи: `is_a`, базовая сложность 0.1
- слов: 28
- ~plane (plane_aircraft), +aircraft, +ambulance, +bicycle, +bike, +boat, +bus, +canoe, +car, +ferry, +helicopter, +Jeep, +limousine, +minivan, +moped, +motorcycle, +scooter, +sled, +Subway, +taxi, +tractor, +train, +tram, +trolley, +truck, +trucks, +van, +wagon

