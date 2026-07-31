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
- ~dunk (dunk_basketball), ~score (score_points), +catch, +dive, +dribble, +kick, +pass, +pitch (pitch_throw_verb), +punt, +serve, +shoot, +spike, +sprint, +swing, +tackle, +throw, +volley, !block (block_stop)

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


## Тема: brands

### AIRLINES  `airlines`
- правило: Major passenger airlines
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~delta (delta_airline), +Air France, +Alaska, +American, +British Airways, +Emirates, +Frontier, +JetBlue, +KLM, +Lufthansa, +Qantas, +Southwest, +United, !Spirit (spirit_airline)

### APPLIANCE BRANDS  `appliance_brands`
- правило: Brands of home appliance
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~Amana, ~Electrolux, ~Frigidaire, ~KitchenAid, ~Maytag, +Bosch, +Dyson, +GE, +Hoover, +Kenmore, +LG, +Samsung, +Whirlpool

### BANK BRANDS  `bank_brands`
- правило: Major American retail banks
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Ally, +Capital One, +Chase, +Citibank, +Fifth Third, +PNC, +Regions Bank, +TD Bank, +US Bank, +Wells Fargo, ?Truist, !KeyBank

### ELECTRONICS BRANDS  `camera_and_electronics`
- правило: Brands of consumer electronics
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~JVC, ~Sanyo, +Bose, +Canon, +Fujifilm, +Kodak, +Nikon, +Panasonic, +Philips, +Pioneer, +Polaroid, +Sharp, +Sony, +Toshiba

### CANDY BRANDS  `candy_brands`
- правило: Candy brands sold in American stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Airheads, ~Butterfinger, ~Reeses, ~Twix, ~Twizzlers, ~Whoppers, +Almond Joy, +Hershey, +Jolly Rancher, +Kitkat, +Milky Way, +Nerds, +Skittles, +Snickers, +Starburst, +Tootsie Roll

### CAR MODELS  `car_models`
- правило: Well known car model names
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +Accord, +beetle, +Camaro, +Camry, +Charger (charger_car), +Civic, +Corvette, +Explorer, +impala, +Jeep Wrangler, +Mustang, +Prius, +Ranger, +Silverado, +Tahoe, xF150

### CEREAL BRANDS  `cereal_brands`
- правило: Breakfast cereal brands sold in America
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Chex, ~Froot Loops, ~Rice Krispies, ~Trix, ~Wheaties, +Cheerios, +Cocoa Puffs, +Corn Flakes, +Frosted Flakes, +Grape Nuts, +Lucky Charms, +Raisin Bran, +Special K, !Life (life_cereal)

### CLOTHING BRANDS  `clothing_brands`
- правило: Well known clothing and shoe brands
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +Adidas, +Champion, +Converse, +Fruit of the Loom, +Gap, +Hanes, +Lacoste, +Levi, +New Balance, +Nike, +puma, +Reebok, +Timberland, +Vans, +Wrangler

### COFFEE BRANDS  `coffee_brands`
- правило: Coffee brands and coffee shops
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +caribou, +Community, +Dunkin, +Keurig, +Maxwell House, +Starbucks, +Tim Hortons, ?Yuban, !Folgers, !Lavazza, !Nescafe, !Peets

### FAST FOOD  `fast_food_chains`
- правило: Fast food restaurant chains in America
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~Arbys, ~Popeyes, ~Wendys, ~Whataburger, +Burger King, +Chipotle, +Dairy Queen, +Dominos, +Five Guys, +KFC, +McDonalds, +Panera, +Pizza Hut, +Sonic, +Subway, +Taco Bell

### FROZEN TREATS  `frozen_treat_brands`
- правило: Brands and products sold in the American ice cream aisle
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~Drumstick, +Ben and Jerry, +Blue Bell, +Klondike, +Magnum, +Popsicle, ?Dreyers, ?Edys, !Breyers, !Haagen Dazs, xTalenti

### HOTEL CHAINS  `hotel_chains`
- правило: Major hotel chains
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Ramada, +Best Western, +Days Inn, +Four Seasons, +Hilton, +Holiday Inn, +Hyatt, +Marriott, +Motel 6, +Radisson, +Sheraton, +Westin

### HARDWARE BRANDS  `paint_and_home`
- правило: Brands sold at a hardware store
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Ace, +Gorilla Glue, +Scotch, +Sherwin Williams, +Weber, ?WD40, !Behr, !Duracell, !Elmers, !Energizer, !Rustoleum, !Valspar

### PAYMENT BRANDS  `payment_brands`
- правило: Card networks and payment apps used in America
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Venmo, +Amex, +Apple Pay, +Cash App, +Discover, +Google Pay, +Mastercard, +PayPal, +Square, +Stripe, +Visa, !Zelle

### RETAIL STORES  `retail_stores`
- правило: Large retail store chains in America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Kohls, ~Macys, +Aldi, +Best Buy, +Costco, +Dollar General, +Home Depot, +Kroger, +Lowes, +Nordstrom, +Publix, +Safeway, +Sears, +Staples, +Target, +Walmart

### SNACK BRANDS  `snack_brands`
- правило: Brands of packaged snacks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Fritos, ~Keebler, ~Nabisco, ~Tostitos, +Cheetos, +Chips Ahoy, +Doritos, +goldfish, +Lays, +Oreo, +Pringles, +Ritz, +Wheat Thins, xTriscuit

### SODA BRANDS  `soda_brands`
- правило: Soft drink brands sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~7up, ~Faygo, ~Schweppes, ~Sunkist, +Canada Dry, +Coke, +crush, +Dr Pepper, +Fanta, +Mountain Dew, +Pepsi, +Sprite, +Squirt, ?Barqs

### SPORTS BRANDS  `sports_brands`
- правило: Brands of sports equipment
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Schwinn, ~Titleist, +Bauer, +Callaway, +Easton, +Franklin, +Louisville Slugger, +Prince, +Rawlings, +Spalding, +Wilson, !head (head_brand)

### TOOL BRANDS  `tool_brands`
- правило: Brands of hand and power tools
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Black and Decker, +Bosch, +Craftsman, +husky, +Milwaukee, +Snap On, +Stanley, !DeWalt, !Hilti, !Makita, !Ryobi, !Skil

### TOY BRANDS  `toy_brands`
- правило: Well known toy brands
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Crayola, ~Little Tikes, ~Tonka, +Barbie, +Etch a Sketch, +Fisher Price, +Hasbro, +Hot Wheels, +Lego, +Lincoln Logs, +Mattel, +Nerf, +Play Doh, +Slinky

### LUXURY BRANDS  `watch_and_luxury`
- правило: Well known luxury brands
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Armani, +Burberry, +Cartier, +Chanel, +Dior, +Ferrari, +Gucci, +Hermes, +Lamborghini, +Omega, +Prada, +Rolex, +Tiffany, +Versace


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
- ~bell (bell_object), +alphabet, +bookshelf, +calendar, +chair, +chalk (chalk_stick), +chalkboard, +clock, +cubby, +desk, +easel, +flag, +globe, +hall pass, +locker, +map, +poster, +projector, +textbook, +whiteboard

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
- ~bell (bell_object), ~maraca, ~stand (stand_holder), ~xylophone, +choir, +conductor, +drum, +metronome, +piano, +recorder, +riser, +sheet music, +tambourine, +triangle

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
- ~Life (life_game), ~mancala, +backgammon, +battleship, +candy land, +checkers, +chess, +chutes and ladders, +clue, +dominoes, +monopoly, +othello, +risk, +scrabble, +sorry, +trivial pursuit, +trouble, xparcheesi

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


## Тема: food_more

### BAKE OFF  `bake_off`
- правило: A step or topping used in competitive baking
- тип связи: `used_in`, базовая сложность 0.55
- слов: 5
- +dough, +fondant, +icing, +piping, +proofing

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
- слов: 13
- ~baked ziti, ~carbonara, ~primavera, ~puttanesca, +alfredo, +bolognese, +lasagna, +mac and cheese, +marinara, +pesto, +pesto pasta, +spaghetti and meatballs, xcacio e pepe

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
- +badge, +baton, +cruiser, +dispatch, +flashlight, +handcuffs, +holster, +k9, +officer, +patrol, +radio, +siren (siren_device), +ticket (ticket_fine), +uniform, +vest, +warrant, +whistle

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


## Тема: names_world

### FRENCH NAMES  `french_names`
- правило: First names common in France
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Amelie, +Antoine, +Camille, +Celine, +Chloe, +Claire, +Henri, +Jean, +Juliette, +Louis, +Marie, +Michel, +Nicolas, +Philippe, +Pierre, +Sophie

### GERMAN NAMES  `german_names`
- правило: First names common in Germany
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Anna, +Dieter, +Erika, +Frieda, +Fritz, +Greta, +Hans, +Heidi, +Helga, +Ingrid, +Karl, +Klaus, +Otto, +Ursula, +Werner, +Wolfgang

### IRISH NAMES  `irish_names`
- правило: First names of Irish origin
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Aidan, +Brendan, +Bridget, +Ciara, +Colleen, +Declan, +Erin, +Fiona, +Kathleen, +Kelly, +Liam, +Maureen, +Patrick, +Ronan, +Sean, +Siobhan

### ITALIAN NAMES  `italian_names`
- правило: First names common in Italy
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Alessandro, +Chiara, +Elena, +Enzo, +Francesca, +Giovanni, +Giulia, +Luca, +Marco, +Marta, +Matteo, +Paolo, +Rosa, +Sofia, +Stefano, +Valentina

### JAPANESE NAMES  `japanese_names`
- правило: First names common in Japan
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Aiko, +Hana, +Hiroshi, +Kenji, +Mei, +Ren, +Rin, +Sakura, +Sora, +Takashi, +Yuki, +Yuna, !Daichi, !Haruto, !Kaito

### SURNAMES FROM TRADES  `nature_surnames`
- правило: Family names that come from old trades
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +Archer, +baker, +Brewer, +carpenter, +chandler, +cooper, +farmer, +Fisher, +Hunter, +mason, +miller, +potter, +Sawyer, +shepherd, +Smith, +Taylor, +Turner, +weaver

### RUSSIAN NAMES  `russian_names`
- правило: First names common in Russia
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Alexei, +Anastasia, +Boris, +Dmitri, +Irina, +Ivan, +Katya, +Mikhail, +Natasha, +Nikolai, +Olga, +Sergei, +Svetlana, +Tatiana, +Vladimir

### SCANDINAVIAN NAMES  `scandinavian_names`
- правило: First names common in Scandinavia
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Astrid, +Bjorn, +Elsa, +Erik, +Ingrid, +Lars, +Magnus, +Nils, +Odin, +Sven, +Thor, !Freja, !Linnea, !Sigrid, !Solveig

### SPANISH NAMES  `spanish_names`
- правило: First names common in Spanish speaking countries
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +Ana, +Antonio, +Carlos, +Carmen, +Diego, +Elena, +Isabel, +Javier, +Jose, +Lucia, +Luis, +Manuel, +Maria, +Miguel, +Pablo, +Pilar, +Ricardo, +Rosa, +Sofia, +Teresa

### UNISEX NAMES  `unisex_names`
- правило: First names given to both boys and girls
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Alex, +Avery, +Bailey, +Casey, +Charlie, +Dakota, +Jamie, +Jordan, +Morgan, +Quinn, +Reese, +Riley, +Rowan, +Sam, +Skyler, +Taylor


## Тема: nature

### DIRT THINGS  `animal_tracks_and_signs`
- правило: Marks and things you see in bare dirt
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~ant, ~dust, ~footprint, ~gravel, ~hole, ~mud, ~pebble, ~puddle, ~root, ~seed, ~stone, ~tire mark, ~track, ~twig, ~worm

### BODIES OF WATER  `bodies_of_water`
- правило: Natural or man-made bodies of water on the surface of the earth
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~spring (spring_water), +bay, +brook, +canal, +creek, +delta (delta_river), +estuary, +fjord, +gulf, +harbor, +inlet, +lagoon, +lake, +marsh, +ocean, +pond, +pool, +reservoir, +river, +sea, +strait, +stream, +swamp, +waterfall, !sound (sound_water)

### SKY WORDS  `cloud_and_sky`
- правило: Things you can see in the sky
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +aurora, +balloon, +bird, +cloud, +comet, +eclipse, +fog, +haze, +helicopter, +kite (kite_toy), +lightning, +meteor, +moon (moon_space), +plane (plane_aircraft), +rainbow, +satellite, +smoke, +star (star_space), +sun, +sunset

### DESERT THINGS  `desert_things`
- правило: Things found in a hot desert
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +cactus, +camel, +canyon, +coyote, +drought, +dune, +heat, +lizard, +mirage, +oasis, +rattlesnake, +sagebrush, +sand, +scorpion, +snake, +tumbleweed, +vulture, !rock (rock_stone)

### FIRE AND SMOKE  `fire_and_smoke`
- правило: Something given off by or belonging to a burning fire
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- +ash, +blaze, +ember, +flame, +smoke, +spark, +torch

### FLOWER PARTS  `flower_parts`
- правило: Parts of a flowering plant
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~pistil, ~sepal, +blossom, +bud, +bulb, +leaf, +nectar, +petal, +pollen, +root, +seed, +stalk, +stamen, +stem, +thorn

### FLOWERS  `flowers`
- правило: Kinds of flowers commonly sold or grown in gardens
- тип связи: `is_a`, базовая сложность 0.15
- слов: 27
- ~begonia, ~petunia, ~zinnia, +aster, +azalea, +buttercup, +carnation, +daffodil, +dahlia, +Daisy, +geranium, +hyacinth, +iris (iris_flower), +Jasmine (jasmine_flower), +lavender (lavender_plant), +lilac, +Lily, +magnolia, +marigold, +orchid, +peony, +poppy, +rose (rose_flower), +sunflower, +tulip, +Violet, +wildflowers

### GARDEN PLANTS  `garden_plants`
- правило: Plants people grow in a home garden
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~hosta, ~lavender (lavender_plant), ~rose (rose_flower), +basil, +bean, +carrot, +cucumber, +Fern, +Ivy, +lettuce, +marigold, +mint (mint_herb), +pepper, +pumpkin, +squash (squash_vegetable), +strawberry, +sunflower, +tomato, +tulip, +zucchini

### GEMSTONES  `gemstones`
- правило: Precious or semi-precious stones used in jewelry
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +agate, +amethyst, +aquamarine, +coral, +diamond (diamond_gem), +emerald, +garnet, +jade, +lapis, +moonstone, +obsidian, +onyx, +opal, +pearl, +peridot, +quartz, +ruby, +sapphire, +topaz, +turquoise

### IN THE JUNGLE  `in_the_jungle`
- правило: Something found in a tropical jungle
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- ~toucan, +canopy, +Fern, +jaguar, +mushroom, +vine

### LANDSCAPE  `landscape_features`
- правило: A natural feature seen in an open landscape
- тип связи: `found_in`, базовая сложность 0.3
- слов: 7
- +cliff, +cloud, +hill, +meadow, +sky, +soil, +valley

### LIGHT SOURCES  `light_sources`
- правило: Things that give off light
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- ~glowstick, ~moon (moon_space), ~streetlight, +bulb, +campfire, +candle, +fire, +firefly, +flashlight, +headlight, +lamp, +lantern, +laser, +lightning, +match, +neon, +screen (screen_display), +star (star_space), +sun, +torch

### MOUNTAIN THINGS  `mountain_things`
- правило: Things found on or around a mountain
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~cabin (cabin_house), ~timberline, +avalanche, +boulder, +cave, +cliff, +eagle, +Echo, +glacier, +goat, +peak, +pine, +ridge, +ski lift, +slope, +snow, +stream, +summit, +trail, +valley

### FUNGI  `mushrooms_and_fungi`
- правило: Mushrooms and other fungi
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~button mushroom, ~mildew, ~mold (mold_fungus), ~mushroom, ~toadstool, ~truffle, ~yeast, !chanterelle, !morel, !portobello, !puffball, !shiitake

### NATURAL DISASTERS  `natural_disasters`
- правило: Destructive natural events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~mudslide, +avalanche, +blizzard, +cyclone, +drought, +earthquake, +eruption, +famine, +flood, +hurricane, +landslide, +sinkhole, +tornado, +tsunami, +volcano, +wildfire

### NATURAL WONDERS  `natural_wonders`
- правило: A large natural landform or body of water
- тип связи: `is_a`, базовая сложность 0.3
- слов: 7
- +canyon, +desert, +glacier, +island, +mountains, +ocean, +volcano

### RIVER FEATURES  `river_features`
- правило: Parts and features of a river described in everyday English
- тип связи: `part_of`, базовая сложность 0.35
- слов: 20
- ~basin, ~bed, ~bend, ~channel, ~current (current_water), ~delta (delta_river), ~eddy, ~ford (ford_river), ~gorge, ~rapids, ~shore, ~source, ~tributary, ~waterfall, +bank (bank_river), +mouth (mouth_river), !floodplain, !headwater, !levee, !sandbar

### ROCKS AND MINERALS  `rocks_and_minerals`
- правило: Common rocks and minerals from the ground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~chalk (chalk_rock), +basalt, +boulder, +clay, +coal, +flint, +granite, +gravel, +gypsum, +iron ore, +limestone, +marble (marble_stone), +obsidian, +pebble, +pumice, +quartz, +salt, +sandstone, +shale, +slate

### BEACH THINGS  `sea_shore_things`
- правило: Things you find on an ocean beach
- тип связи: `found_in`, базовая сложность 0.2
- слов: 21
- ~sandcastle, ~seashell, +boardwalk, +cooler, +crab, +driftwood, +dune, +gull, +jellyfish, +pebble, +sand, +seaweed, +shell, +starfish, +sunscreen, +surfboard, +tide, +towel, +umbrella, +wave (wave_water), !kite (kite_toy)

### SEASONAL WORDS  `seasons_and_nature`
- правило: Words describing the changing seasons outdoors
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~molt, +bloom, +blossom, +bud, +equinox, +foliage, +frost, +harvest, +hibernate, +migrate, +ripen, +shed, +snowfall, +solstice, +sprout, +sunrise, +thaw, +wither

### STORMS  `storms`
- правило: Kinds of violent weather events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~hailstorm, +blizzard, +cyclone, +downpour, +dust storm, +gale, +hurricane, +ice storm, +monsoon, +squall, +Tempest, +thunderstorm, +tornado, +typhoon, +whirlwind

### FOREST THINGS  `things_in_the_forest`
- правило: Things you find walking through a forest
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~pinecone, +acorn, +bark (bark_tree), +branch (branch_tree), +campsite, +clearing, +deer, +Fern, +fox, +leaf, +log, +moss, +mushroom, +owl, +squirrel, +stream, +stump, +trail, +tree, +undergrowth

### GROWING THINGS  `things_that_grow`
- правило: Living things that grow larger over time
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~bud, ~crop, ~crystal, ~flower, ~grass, ~leaf, ~moss, ~mushroom, ~plant (plant_growth), ~root, ~sapling, ~seedling, ~vine, ~weed, +child, +hair, +tree, !nail (nail_body)

### THINGS WITH SEEDS  `things_with_seeds`
- правило: Common objects or foods that naturally contain seeds
- тип связи: `has_property`, базовая сложность 0.35
- слов: 25
- ~avocado, ~bean, ~cherry, ~corn, ~cucumber, ~fig, ~grape, ~kiwi, ~melon, ~orange (orange_fruit), ~peach, ~pear, ~pepper, ~plum, ~pomegranate, ~poppy, ~pumpkin, ~sesame, ~squash (squash_vegetable), ~strawberry, ~sunflower, ~tomato, ~watermelon, +apple (apple_fruit), !pinecone

### TREE PARTS  `tree_parts`
- правило: Physical parts of a living tree
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~needle (needle_pine), +acorn, +bark (bark_tree), +bough, +branch (branch_tree), +bud, +cone, +knot, +leaf, +limb, +pulp, +root, +sap, +seed, +shoot, +stump, +trunk (trunk_tree), +twig, !crown (crown_tree), !ring (ring_tree)

### TREES  `trees`
- правило: Kinds of trees an average American can name
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~apple (apple_fruit), +ash, +Aspen, +beech, +birch, +cedar, +cherry, +chestnut, +cypress, +dogwood, +elm, +fir, +hickory, +juniper, +magnolia, +maple, +oak, +palm (palm_tree), +pine, +poplar, +redwood, +spruce, +sycamore, +walnut, +Willow

### TYPES OF SOIL  `types_of_soil`
- правило: A type of soil or ground classed by what it is made of
- тип связи: `is_a`, базовая сложность 0.5
- слов: 6
- +chalk (chalk_rock), +clay, +loam, +peat, +sand, +silt

### UNDERGROUND THINGS  `underground_things`
- правило: Things found under the surface of the ground
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~ant nest, ~aquifer, ~bulb, ~burrow, ~cave, ~coal, ~fossil, ~mole (mole_animal), ~ore, ~pipe (pipe_tube), ~root, ~seed, ~sewer, ~Subway, ~treasure, ~tunnel, ~worm, +mine

### FORMS OF WATER  `water_states`
- правило: Forms water takes in nature
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~dew, ~drizzle, ~fog, ~frost, ~glacier, ~hail, ~humidity, ~icicle, ~mist, ~puddle, ~sleet, ~slush, ~vapor, +cloud, +ice, +liquid, +rain, +snow, +steam

### WEATHER REPORT  `weather_report`
- правило: What a weather report names or predicts
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~directions, ~seasons, +forecast, +humidity, +radar, +storms, xmonths

### WEATHER WORDS  `weather_words`
- правило: Words describing weather conditions or events in the sky
- тип связи: `is_a`, базовая сложность 0.15
- слов: 26
- +blizzard, +breeze, +cloud, +downpour, +drizzle, +flurry, +fog, +frost, +gale, +hail, +heat wave, +humidity, +hurricane, +lightning, +mist, +rain, +shower, +sleet, +snow, +storm, +sun, +sunshine, +thaw, +thunder, +tornado, +wind

### WILD PLANTS  `wild_plants`
- правило: Plants that grow wild in fields and woods
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bracken, ~bramble, ~clover, ~dandelion, ~Fern, ~Ivy, ~lichen, ~moss, ~nettle, ~reed, ~thistle, ~vine, ~weed, !cattail, !goldenrod, !milkweed, !ragweed, !sedge


## Тема: sounds

### ALARM SOUNDS  `bell_and_alarm`
- правило: Sounds made by alarms and signals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~alert, ~beep, ~bell (bell_object), ~blare, ~buzz, ~chime, ~ding, ~gong, ~horn (horn_sound), ~siren (siren_device), ~tone, ~whistle, +ring (ring_sound), !klaxon

### CITY SOUNDS  `city_sounds`
- правило: Sounds heard on a city street
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~alarm, ~bell (bell_object), ~brakes, ~chatter, ~footsteps, ~honk, ~jackhammer, ~rumble, ~screech, ~shout, ~siren (siren_device), ~whistle, +engine, +traffic

### KITCHEN SOUNDS  `kitchen_sounds`
- правило: Sounds heard in a kitchen
- тип связи: `does_action`, базовая сложность 0.45
- слов: 14
- ~boil, ~bubble, ~chop, ~clatter, ~clink, ~crunch (crunch_sound), ~ding, ~grind, ~hiss, ~pop (pop_sound), ~sizzle, ~slam, ~whisk, !whir

### LOUD NOISES  `loud_noises`
- правило: Words for very loud noises
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~blare, ~clash, ~explosion, ~roar, ~rumble, ~screech, ~shatter, ~slam, ~thunder, ~wail, +bang, +blast, +boom, +crash

### MACHINE SOUNDS  `machine_sounds`
- правило: Sounds that machines make
- тип связи: `does_action`, базовая сложность 0.4
- слов: 16
- ~beep, ~buzz, ~chug, ~clank, ~ding, ~grind, ~hum, ~purr, ~rattle (rattle_sound), ~rev, ~roar, ~screech, ~sputter, ~whine, +click, !whir

### MUSIC SOUNDS  `musical_sounds`
- правило: Words for the sound a musical instrument makes
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~blare, ~ring (ring_sound), +boom, +chime, +clang, +hum, +jingle, +riff, +strum, +thump, +toot, +trill, +twang, !drumroll

### NATURE SOUNDS  `nature_sounds`
- правило: Sounds heard outdoors in nature
- тип связи: `does_action`, базовая сложность 0.4
- слов: 15
- ~buzz, ~chirp, ~crackle, ~croak, ~crunch (crunch_sound), ~hoot, ~howl, ~hum, ~patter, ~roar, ~rustle, ~splash, ~thunder, ~whisper, ~whistle

### SOUND WORDS  `onomatopoeia`
- правило: Words that imitate the sound they name
- тип связи: `is_a`, базовая сложность 0.35
- слов: 25
- ~drip (drip_water), +bang, +beep, +boom, +buzz, +clang, +click, +crackle, +crash, +hiss, +jingle, +ping, +plop, +pop (pop_sound), +ring (ring_sound), +rumble, +sizzle, +snap, +splash, +squeak, +thud, +whack, +whoosh, +zap, !tick (tick_sound)

### QUIET SOUNDS  `quiet_sounds`
- правило: Words for very soft sounds
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~breath, ~creak, ~hum, ~murmur, ~patter, ~purr, ~rustle, ~sigh, ~tinkle, ~whisper, !drip (drip_water), !shuffle (shuffle_walk), !tick (tick_sound)

### SCARY SOUNDS  `scary_sounds`
- правило: Sounds that make people uneasy
- тип связи: `does_action`, базовая сложность 0.45
- слов: 14
- ~creak, ~groan, ~growl, ~howl, ~moan, ~rattle (rattle_sound), ~scratch, ~scream, ~shriek, ~snap, ~thud, ~wail, ~whisper, !footstep

### VOICE SOUNDS  `voice_sounds`
- правило: Sounds a human voice makes without words
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- +cough, +cry, +gasp, +giggle, +groan, +grunt, +hum, +laugh, +moan, +scream, +shout, +sigh, +snort, +sob, +whistle, +yawn

### WATER SOUNDS  `water_sounds`
- правило: Sounds that water makes
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~babble, ~drip (drip_water), ~hiss, ~lap (lap_water), ~patter, ~plop, ~ripple, ~roar, ~splash, ~spray, ~trickle, ~whoosh, !gurgle, !slosh


## Тема: space

### ASTRONAUT GEAR  `astronaut_gear`
- правило: Equipment an astronaut uses
- тип связи: `used_in`, базовая сложность 0.35
- слов: 13
- ~spacesuit, +backpack, +boot (boot_shoe), +camera, +checklist, +communicator, +glove, +helmet, +jetpack, +oxygen tank, +tether, +tool belt, +visor

### STARS  `bright_stars`
- правило: Individual stars people can name
- тип связи: `is_a`, базовая сложность 0.45
- слов: 17
- +Capella, +Castor, +constellations, +Polaris, +Sirius, +sun, +Vega, !Aldebaran, !Altair, !Antares, !Arcturus, !Betelgeuse, !Deneb, !Pollux, !Procyon, !Rigel, !Spica

### CONSTELLATIONS  `constellations`
- правило: Constellations in the night sky
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Cassiopeia, +Andromeda, +Big Dipper, +Crux, +Cygnus, +Draco, +Hercules, +Little Dipper, +Lyra, +Orion, +pegasus, +Perseus, +Ursa Major, +Ursa Minor, !Centaurus

### DEEP COSMOS  `deep_cosmos`
- правило: An object or measure of the far cosmos
- тип связи: `found_in`, базовая сложность 0.7
- слов: 5
- ~quasar, ~stargazer, +exoplanet, +lightyear, +pulsar

### DEEP SPACE  `deep_space`
- правило: An object seen in deep space beyond the earth
- тип связи: `found_in`, базовая сложность 0.35
- слов: 7
- +asteroid, +comets, +galaxy, +meteor, +moon (moon_space), +nebula, +stars

### MOONS  `moons`
- правило: Named moons of the solar system
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- +Europa, +Ganymede, +Io, +Luna, +Miranda, +Rhea, +Titan, +triton, !Callisto, !Charon, !Deimos, !Enceladus, !Iapetus, !Phobos

### ROCKET PARTS  `rocket_parts`
- правило: Parts of a rocket
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- +booster, +capsule, +engine, +fin, +fuel tank, +heat shield, +launch pad, +nose cone, +nozzle, +payload, +stage, +thruster

### SCI FI  `science_fiction_space`
- правило: Words used in space science fiction
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~Alien, ~android, ~colony, ~cyborg, ~galaxy, ~hyperdrive, ~laser, ~mothership, ~ray gun, ~starship, ~teleport, ~warp, ~wormhole, +force field

### SOLAR SYSTEM  `solar_system_words`
- правило: Words describing the solar system
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~kuiper belt, ~ring (ring_circle), +asteroid belt, +comet, +corona, +dwarf planet, +eclipse, +gravity, +meteor, +moon (moon_space), +orbit, +planet, +solar wind, +sun

### SPACE PLACES  `space_agencies_and_places`
- правило: Places and organizations connected with space flight
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- +Cape Canaveral, +Houston, +ISS, +Jet Propulsion Lab, +Kennedy Space Center, +launch pad, +Mission Control, +NASA, +observatory, !Baikonur, !Roscosmos

### SPACE MEASUREMENTS  `space_measurements`
- правило: Units used to measure distance and time in space
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- ~astronomical unit, ~gravity, ~kilometer, ~light year, ~magnitude, ~mile, ~orbit, ~revolution, ~rotation, !degree (degree_angle), !parsec

### SPACE PHENOMENA  `space_phenomena`
- правило: Events and phenomena seen in space
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~quasar, +aurora, +big bang, +black hole, +comet tail, +eclipse, +gravity well, +meteor shower, +nebula, +solar flare, +sunspot, +supernova

### SPACE STATION  `space_station`
- правило: A part of a space station or a task done aboard it
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- ~spacewalk, +airlock, +cosmonaut, +docking, +module

### SPACECRAFT  `spacecraft`
- правило: Famous spacecraft and space missions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Apollo, +Atlantis, +Cassini, +Challenger, +Columbia, +Curiosity, +Discovery, +Galileo, +Hubble, +Juno, +Pioneer, +Soyuz, +Sputnik, +Viking, +Voyager

### STARGAZING  `stargazing`
- правило: What you look at or name when you look up on a clear night
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- ~comet, ~eclipse, ~telescope, +constellations, +moons, +planets, +stars

### TELESCOPE WORDS  `telescope_words`
- правило: Parts and words used with a telescope
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~aperture, ~dome, ~eyepiece, ~filter, ~finder, ~focus (focus_lens), ~lens, ~magnification, ~mirror, ~mount, ~observatory, ~reflector, ~refractor, ~tripod


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

### BARBERSHOP  `barbershop`
- правило: A person or product found in a barbershop
- тип связи: `found_in`, базовая сложность 0.5
- слов: 4
- ~pomade, +aftershave, +barber, +clippers

### BARBERSHOP WORDS  `barbershop_words`
- правило: Things found in a barbershop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- +apron (apron_garment), +brush, +cape, +chair, +clippers, +comb, +mirror, +pole, +powder, +razor, +scissors, +shaving cream, +towel, +trimmer

### BLACKSMITH  `blacksmith`
- правило: A tool, place or step of working metal by hand
- тип связи: `used_in`, базовая сложность 0.6
- слов: 6
- +anvil, +bellows, +forge, +horseshoe, +quench, +smithy

### BUTCHER SHOP  `butcher_words`
- правило: Things found in a butcher shop
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~block (block_cube), ~cutlet, +apron (apron_garment), +brisket, +cleaver, +cut, +freezer, +grinder, +mince, +rack, +sausage, +saw, +sirloin, +tenderloin, +twine, +wrap, !case (case_box), !scale (scale_weigh)

### CARPENTER  `carpenter`
- правило: A material, tool or joint used working wood
- тип связи: `used_in`, базовая сложность 0.55
- слов: 5
- ~dovetail, +lathe, +plywood, +sander, +sawdust

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

### LUMBER CAMP  `lumber_camp`
- правило: A person, tool or product of felling trees
- тип связи: `found_in`, базовая сложность 0.55
- слов: 6
- +chainsaw, +flannel, +logger, +sawmill, +stump, +timber

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

### PLUMBER VISIT  `plumber_visit`
- правило: Something a plumber works with or on
- тип связи: `used_in`, базовая сложность 0.55
- слов: 4
- ~unclog, +pipeline, +plunger, +sewer

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
- слов: 17
- ~chalk (chalk_tailor), ~pinstripe, +bobbin, +cufflinks, +hem, +iron (iron_appliance), +machine, +mannequin, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam ripper, +seamstress, +shears, +tape measure, +thimble, +thread

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
- ~kickstand, +basket, +brake, +chain, +crank, +fork, +frame, +gear, +handlebar, +pedal, +reflector, +rim, +saddle, +seat, +spoke, +tire, +wheel, !bell (bell_object)

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
- +adapter, +backpack, +boarding pass, +camera, +Charger (charger_device), +currency, +guidebook, +insurance, +itinerary, +map, +neck pillow, +passport, +suitcase, +sunglasses, +ticket (ticket_admission), +toiletries, +Visa, +wallet

### VEHICLES  `vehicles`
- правило: Machines built to carry people or goods from place to place
- тип связи: `is_a`, базовая сложность 0.1
- слов: 28
- ~plane (plane_aircraft), +aircraft, +ambulance, +bicycle, +bike, +boat, +bus, +canoe, +car, +ferry, +helicopter, +Jeep, +limousine, +minivan, +moped, +motorcycle, +scooter, +sled, +Subway, +taxi, +tractor, +train, +tram, +trolley, +truck, +trucks, +van, +wagon


## Тема: varieties

### APPLE VARIETIES  `apple_varieties`
- правило: Varieties of apple sold in stores
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Cortland, +empire, +Envy, +Fuji, +Gala, +Golden Delicious, +Granny Smith, +Jonathan, +McIntosh, +Pink Lady, +Red Delicious, +Rome, !Braeburn, !Honeycrisp

### BEAN TYPES  `bean_types`
- правило: Kinds of bean used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~fava, ~garbanzo, ~mung, +black, +black eyed pea, +butter bean, +great northern, +kidney, +Lima, +navy, +pinto, +string, !adzuki, !cannellini

### BERRY VARIETIES  `berry_varieties`
- правило: Varieties of berry sold fresh or frozen
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~elderberry, +blackberry, +blueberry, +cranberry, +currant, +gooseberry, +raspberry, +strawberry, !boysenberry, !cloudberry, !loganberry, xmarionberry

### SPICE BLENDS  `chili_and_spice_blends`
- правило: Mixtures of spices sold as one seasoning
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +cajun, +chili powder, +curry powder, +five spice, +italian seasoning, +jerk, +old bay, +poultry seasoning, +pumpkin spice, +ranch mix, +taco seasoning, !garam masala, !herbes de provence, !za'atar

### GRAPE VARIETIES  `grape_varieties`
- правило: Varieties of grape used for wine and eating
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~Syrah, +Cabernet, +Chardonnay, +Concord, +Merlot, +Muscat, +Pinot Noir, +Riesling, +Sauvignon, +Thompson, !Malbec, !Sangiovese, !Zinfandel

### SYRUPS AND SWEETENERS  `honey_and_syrups`
- правило: Sweet syrups and sweeteners used in food
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +agave, +brown sugar, +cane sugar, +caramel, +corn syrup, +date syrup, +honey, +maple syrup, +molasses, +powdered sugar, +sorghum, +stevia, +treacle

### SALAD GREENS  `lettuce_and_greens`
- правило: Varieties of lettuce and salad green
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~arugula, +butter, +endive, +green leaf, +iceberg, +red leaf, +romaine, +spinach, +watercress, !escarole, !radicchio, xfrisee, xmesclun

### MELONS & SQUASH  `melons_and_squash`
- правило: Varieties of melon and squash
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- +acorn, +butternut, +cantaloupe, +honeydew, +hubbard, +pumpkin, +spaghetti, +watermelon, +zucchini, ?crookneck, !delicata, !kabocha, xcasaba

### HERB VARIETIES  `mint_and_herbs_varieties`
- правило: Varieties of mint and other kitchen herbs
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- ~basil, ~chervil, ~cilantro, ~curly parsley, ~dill, ~italian parsley, ~lemon balm, ~oregano, ~peppermint, ~spearmint, ~thai basil, !marjoram, !sorrel

### OLIVE TYPES  `olive_types`
- правило: Varieties of olive and olive oil
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~black, ~extra virgin, ~light (light_mild), ~pitted, ~spanish, ~stuffed, ~virgin, !green (green_unripe), !kalamata, !manzanilla, !nicoise, xcastelvetrano

### PEPPER VARIETIES  `pepper_varieties`
- правило: Varieties of pepper used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~habanero, ~pimento, +Anaheim, +banana, +cayenne, +Chipotle, +ghost, +jalapeno, +scotch bonnet, +serrano, !bell (bell_pepper), !poblano, xshishito

### POTATO VARIETIES  `potato_varieties`
- правило: Varieties of potato sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~russet, ~white (white_food), +baby, +idaho (idaho_potato), +new potato, +purple, +red, +sweet potato, +yam, +yukon gold, !fingerling, !kennebec

### RICE TYPES  `rice_types`
- правило: Kinds of rice sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +black, +Brown, +Jasmine (jasmine_rice), +long grain, +red, +short grain, +sticky, +sushi, +white (white_food), +wild, !arborio, !basmati, !parboiled

### TOMATO VARIETIES  `tomato_varieties`
- правило: Varieties of tomato
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~campari, ~green (green_unripe), +cherry, +grape, +heirloom, +plum, +roma, +sun dried, +vine, +yellow, !beefsteak, !san marzano

