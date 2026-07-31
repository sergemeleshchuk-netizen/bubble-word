# Категории, часть 2 из 4

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
- слов: 25
- ~dice (dice_cut), ~saute, +bake, +blend, +boil, +broil, +chop, +drain, +fry (fry_cook), +garnish, +grill, +knead, +marinate, +mash, +mince, +peel, +roast, +sear, +simmer, +slice, +steam, +stir, +toss, +whisk, !season (season_flavor)

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


## Тема: animals_more

### ANIMAL GENDERS  `animal_names_male_female`
- правило: Words for the male or female of an animal species
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +boar, +buck, +bull, +cow, +doe, +drake, +ewe, +gander, +hen, +jenny, +mare, +ram, +rooster, +sow (sow_pig), +stallion, +tom, +vixen, !jack (jack_animal)

### GRAZING ANIMALS  `antelope_and_grazers`
- правило: Animals that graze on grass in herds
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +antelope, +bison, +buffalo, +elk, +gazelle, +gnu, +impala, +oryx, +springbok, +wildebeest, +yak, +zebra, !eland, !kudu

### YOUNG ANIMALS  `baby_animal_words_more`
- правило: Less common words for young animals
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~kid, ~nymph, ~spat, !cygnet, !eaglet, !hatchling, !squab, !whelp, xelver, xleveret, xpoult, xshoat

### CRUSTACEANS  `crustaceans`
- правило: Animals classed as crustaceans: a hard shell and many jointed legs
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- +barnacle, +crab, +crayfish, +hermit crab, +king crab, +krill, +lobster, +pill bug, +prawn, +shrimp, !isopod

### EXOTIC PETS  `exotic_pets`
- правило: Unusual animals people keep as pets
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +chinchilla, +ferret, +gecko, +hedgehog, +hermit crab, +iguana, +parrot, +python, +sugar glider, +tarantula, +tortoise, !axolotl, xdegu

### SOFT CREATURES  `jellyfish_and_soft`
- правило: Soft bodied sea creatures without bones
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- ~jellyfish, ~man o war, ~octopus, ~sea cucumber, ~sea slug, ~sponge (sponge_animal), ~squid, !anemone, !coral polyp, !cuttlefish, !nudibranch

### MARSUPIALS  `marsupials`
- правило: Animals that carry young in a pouch
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- +bandicoot, +kangaroo, +koala, +opossum, +sugar glider, +tasmanian devil, +wallaby, +wombat, !quokka, xnumbat

### WORK ANIMALS  `pack_animals`
- правило: Animals used to carry loads or do work
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +alpaca, +camel, +dog, +donkey, +elephant, +horse, +husky, +llama, +mule, +ox, +reindeer, +water buffalo, +yak

### EXOTIC BIRDS  `parrots_and_exotic_birds`
- правило: Colorful birds kept as pets or seen in zoos
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~macaw, +budgie, +cockatoo, +parakeet, +parrot, +toucan, !cockatiel, !conure, !hornbill, !lorikeet, !lovebird, !myna, !quetzal

### SEAL FAMILY  `seals_and_walruses`
- правило: Kinds of seal, sea lion and walrus
- тип связи: `is_a`, базовая сложность 0.45
- слов: 9
- ~elephant seal, ~fur seal, ~harbor seal, ~harp seal, ~leopard seal, ~monk seal, ~ringed seal, ~sea lion, ~walrus

### TURTLES  `turtles_and_tortoises`
- правило: Kinds of turtle and tortoise
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~terrapin, +box turtle, +green turtle, +painted turtle, +sea turtle, +slider, +snapping turtle, +tortoise, !hawksbill, !leatherback

### WADING BIRDS  `wading_birds`
- правило: Birds with long legs that wade in shallow water
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~sandpiper, ~stilt, +crane (crane_bird), +egret, +flamingo, +heron, +ibis, +plover, +stork, !avocet, !bittern, !spoonbill

### WATERFOWL  `waterfowl`
- правило: Birds that swim on lakes and ponds
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~cormorant, ~eider, ~grebe, +coot, +duck (duck_bird), +goose, +loon, +mallard, +pelican, +swan, +teal, !canvasback, !merganser, !widgeon

### SMALL CATS  `wild_cats_small`
- правило: Smaller members of the wild cat family
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- ~bobcat, ~fishing cat, ~lynx, ~sand cat, ?jaguarundi, !caracal, !ocelot, !pallas cat, !serval, xmargay

### WORMS  `worms_and_crawlers`
- правило: Long soft bodied crawlers commonly called worms in English
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~earthworm, ~leech, ~nightcrawler, ~silkworm, ~tapeworm, !flatworm, !glowworm, !inchworm, !roundworm, xbloodworm


## Тема: brands

### AIRLINES  `airlines`
- правило: Major passenger airlines
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~delta (delta_airline), +Air France, +Alaska, +American, +British Airways, +Emirates, +Frontier, +JetBlue, +KLM, +Lufthansa, +Qantas, +Southwest, +Spirit, +United

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
- +Accord, +beetle, +Camaro, +Camry, +Charger, +Civic, +Corvette, +Explorer, +impala, +Jeep Wrangler, +Mustang, +Prius, +Ranger, +Silverado, +Tahoe, xF150

### CEREAL BRANDS  `cereal_brands`
- правило: Breakfast cereal brands sold in America
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Chex, ~Froot Loops, ~Rice Krispies, ~Trix, ~Wheaties, +Cheerios, +Cocoa Puffs, +Corn Flakes, +Frosted Flakes, +Grape Nuts, +Life, +Lucky Charms, +Raisin Bran, +Special K

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


## Тема: clothing

### ACCESSORIES  `accessories`
- правило: Small items worn or carried to complete an outfit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~bowtie, ~tie (tie_clothing), +backpack, +belt, +brooch, +clutch, +cufflinks, +gloves, +handbag, +hat, +headband, +purse, +scarf, +sunglasses, +suspenders, +umbrella, +wallet, +watch (watch_object)

### CLOTHING ITEMS  `clothing_items`
- правило: Garments worn on the body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~tie (tie_clothing), +blazer, +blouse, +cardigan, +coat (coat_garment), +dress, +glove, +hat, +hoodie, +jacket, +jeans, +leggings, +overalls, +pants, +robe, +scarf, +shirt, +shorts, +skirt, +sock, +suit (suit_clothing), +sweater, +sweatshirt, +tank top, +vest

### GARMENT PARTS  `clothing_parts`
- правило: Parts sewn into a piece of clothing
- тип связи: `part_of`, базовая сложность 0.3
- слов: 17
- ~hood (hood_garment), ~placket, +belt loop, +buckle, +button (button_clothing), +collar, +cuff, +hem, +lapel, +lining, +pocket, +seam, +sleeve, +strap, +waistband, +yoke, +zipper

### CLOTHING SIZES  `clothing_sizes`
- правило: Words used for clothing sizes and fit
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +large, +loose, +medium, +narrow, +oversized, +petite, +plus, +regular, +slim, +small, +snug, +tall, +tight, +wide

### FABRICS  `fabrics`
- правило: Materials that clothes are made from
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +canvas, +cashmere, +chiffon, +corduroy, +cotton, +denim, +flannel, +fleece, +lace, +leather, +linen, +nylon, +polyester, +satin, +silk, +spandex, +suede, +tweed, +velvet, +wool

### FOOTWEAR  `footwear`
- правило: Things worn on the feet
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- ~wader, +boot (boot_shoe), +cleat, +clog, +flat, +flip-flop, +heel, +hiking boot, +loafer, +moccasin, +oxford, +pump, +sandal, +slip on, +slipper, +sneaker, +sock, +stiletto, +wedge, ?galosh

### FORMAL WEAR  `formal_wear`
- правило: Clothing worn to a formal occasion
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~bowtie, ~cummerbund, +cocktail dress, +corsage, +cufflinks, +dress shoes, +evening dress, +gown, +sash, +suit (suit_clothing), +tails, +tuxedo, +veil, +waistcoat

### HATS  `hats`
- правило: Things worn on the head
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~crown (crown_royal), ~hood (hood_garment), +baseball cap, +beanie, +beret, +bonnet, +bowler, +cap, +cowboy hat, +fedora, +hard hat, +headband, +helmet, +sombrero, +sun hat, +top hat, +turban, +visor

### JEWELRY  `jewelry`
- правило: Decorative items worn on the body as jewelry
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- +anklet, +bangle, +bracelet, +brooch, +chain, +charm, +choker, +cufflink, +earring, +hoop, +locket, +necklace, +pendant, +ring (ring_jewelry), +stud, +tiara, +watch (watch_object), !pin (pin_fastener)

### KIDS CLOTHING  `kids_clothing`
- правило: Clothing made especially for babies and children
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~footie pajamas, ~romper, +bib, +booties, +diaper, +jumper, +mittens, +onesie, +overalls, +smock, +sun hat, !snowsuit

### LAUNDRY CARE  `laundry_care`
- правило: Things done to clothes to keep them clean and neat
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~press (press_push), +bleach, +dry, +dry clean, +fold, +hang, +iron (iron_appliance), +mend, +rinse, +soak, +sort, +starch, +steam, +wash

### SEWING WORDS  `sewing_words`
- правило: Words used when sewing or altering clothes
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~baste, ~dart (dart_sew), +alter, +bobbin, +cuff, +hem, +lining, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam, +stitch, +thimble, +thread, +tuck, !pleat

### SHOE PARTS  `shoe_parts`
- правило: Parts of a shoe
- тип связи: `part_of`, базовая сложность 0.35
- слов: 14
- ~eyelet, ~insole, +arch (arch_foot), +buckle, +cushion, +heel, +lace, +shank, +sole (sole_shoe), +strap, +toe, +tongue, +tread, +upper

### SLEEPWEAR  `sleepwear`
- правило: Clothing worn to bed
- тип связи: `is_a`, базовая сложность 0.25
- слов: 10
- ~nightcap, ~nightshirt, +boxers, +lounge pants, +nightgown, +onesie, +pajamas, +robe, +sleep mask, +slippers

### SWIMWEAR  `swimwear`
- правило: Clothing worn for swimming
- тип связи: `is_a`, базовая сложность 0.25
- слов: 11
- +bikini, +board shorts, +cover up, +flippers, +goggles, +one piece, +rash guard, +swim cap, +swimsuit, +trunks, +wetsuit

### THINGS WITH POCKETS  `things_with_pockets`
- правило: Clothes and bags that have pockets
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~apron (apron_garment), ~backpack, ~blazer, ~cargo pants, ~coat (coat_garment), ~hoodie, ~jacket, ~jeans, ~overalls, ~purse, ~robe, ~shirt, ~suitcase, ~vest

### HAND WEAR  `things_worn_on_hands`
- правило: Things worn on the hands
- тип связи: `has_property`, базовая сложность 0.3
- слов: 12
- ~bandage, ~boxing glove, ~bracelet, ~cast (cast_medical), ~gauntlet, ~glove, ~mitten, ~oven mitt, ~ring (ring_jewelry), ~splint, ~watch (watch_object), +nail polish

### BUTTONED THINGS  `things_you_button`
- правило: Clothes and objects fastened with buttons
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~blouse, ~cardigan, ~coat (coat_garment), ~cuff, ~glove, ~jacket, ~jeans, ~overalls, ~pajamas, ~pants, ~shirt, ~sweater, ~vest, !pillowcase

### TIED THINGS  `things_you_tie`
- правило: Things fastened by tying a knot or bow
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~bandana, ~belt, ~bowtie, ~drawstring, ~hair tie, ~knot, ~laces, ~ribbon, ~rope, ~sash, ~scarf, ~shoelace, ~tie (tie_knot), !apron (apron_garment)

### WINTER CLOTHING  `winter_clothing`
- правило: Clothing worn specifically to stay warm in cold weather
- тип связи: `used_in`, базовая сложность 0.2
- слов: 18
- ~ear muffs, ~hood (hood_garment), ~thermals, +beanie, +boot (boot_shoe), +coat (coat_garment), +down jacket, +fleece, +glove, +mitten, +muffler, +parka, +scarf, +shawl, +ski mask, +snow pants, +sweater, +wool socks

### UNIFORMS  `work_uniforms`
- правило: Outfits worn as a required uniform for work or school
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~cassock, ~coveralls, +apron (apron_garment), +badge, +blazer, +chef coat, +hard hat, +jumpsuit, +kilt, +lab coat, +scrubs, +smock, +tunic, +vest


## Тема: education

### FIRST LESSONS  `alphabet_and_numbers`
- правило: The very first things children learn at school
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~season (season_time), ~sound (sound_noise), +addition, +alphabet, +color, +count, +day, +letter (letter_alphabet), +month, +name, +number, +rhyme, +shape, +sight word, +word

### ART CLASS  `art_class_things`
- правило: Things used in a school art class
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~chalk (chalk_stick), +apron (apron_garment), +brush, +canvas, +clay, +construction paper, +easel, +glitter, +glue, +kiln, +marker, +paint, +palette, +pastel, +scissors, +sketchbook, +smock, +stencil

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
- слов: 25
- +backpack, +binder, +calculator, +compass, +crayon, +eraser, +folder, +glue, +highlighter, +index card, +lunchbox, +marker, +notebook, +paper, +pen (pen_writing), +pencil, +pencil case, +planner, +protractor, +ruler, +scissors, +sharpener, +stapler, +tape, +textbook

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


## Тема: food

### ASIAN DISHES  `asian_dishes`
- правило: Dishes from East and Southeast Asian cuisines eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bibimbap, ~satay, ~tempura, ~wonton, +chow mein, +curry, +dim sum, +dumpling, +egg roll, +fried rice, +kimchi, +lo mein, +miso soup, +pad thai, +pho, +ramen, +sashimi, +spring roll, +sushi, +teriyaki

### BAKING INGREDIENTS  `baking_ingredients`
- правило: Ingredients commonly used to bake cakes, bread or cookies
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~oil (oil_cooking), +almond, +baking powder, +baking soda, +butter, +buttermilk, +chocolate, +cinnamon, +cocoa, +cream (cream_dairy), +egg, +flour, +frosting, +honey, +icing, +milk, +molasses, +oat, +raisin, +salt, +shortening, +sugar, +syrup, +vanilla, +yeast

### BARBECUE FOODS  `bbq_foods`
- правило: Foods cooked or served at an American backyard barbecue
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +baked beans, +brisket, +bun, +burger, +chicken, +chips, +coleslaw, +corn, +cornbread, +hot dog, +kebab, +lemonade, +macaroni salad, +mustard, +pickle, +potato salad, +pulled pork, +ribs, +sausage, +watermelon

### BERRIES  `berries`
- правило: Small soft fruits called berries in everyday American English
- тип связи: `is_a`, базовая сложность 0.2
- слов: 13
- ~boysenberry, ~elderberry, +blackberry, +blueberry, +cherry, +cranberry, +currant, +gooseberry, +grape, +huckleberry, +mulberry, +raspberry, +strawberry

### BREAD TYPES  `bread_types`
- правило: Kinds of bread and baked goods made from dough
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~challah, ~ciabatta, ~flatbread, ~focaccia, ~pumpernickel, ~white (white_food), +bagel, +baguette, +banana bread, +biscuit, +brioche, +bun, +cornbread, +croissant, +muffin, +naan, +pita, +pretzel, +roll (roll_bread), +rye, +scone, +sourdough, +texas toast, +tortilla, +wheat

### BREAKFAST FOODS  `breakfast_foods`
- правило: Foods typically eaten at breakfast in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- +bacon, +bagel, +biscuit, +cereal, +coffee cake, +croissant, +danish, +doughnut, +egg, +french toast, +granola, +grits, +ham, +hash brown, +jam, +muffin, +oatmeal, +omelet, +pancake, +porridge, +sausage, +scone, +toast (toast_bread), +waffle, +yogurt

### CAKE TYPES  `cake_types`
- правило: Kinds of cake baked and sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bundt, ~fruitcake, ~pound (pound_cake), ~sponge (sponge_cake), +angel food, +birthday, +carrot, +cheesecake, +chocolate, +coffee cake, +cupcake, +ice cream cake, +lava, +layer, +red velvet, +shortcake, +upside down, +vanilla, +wedding, !marble (marble_cake)

### CANDY  `candy`
- правило: Sweets sold in a candy aisle
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~brittle (brittle_candy), ~gum (gum_candy), ~gumdrop, +butterscotch, +candy cane, +caramel, +chocolate, +chocolate bar, +fudge, +jelly bean, +licorice, +lollipop, +marshmallow, +mint (mint_candy), +nougat, +praline, +rock candy, +taffy, +toffee, +truffle

### CHEESE TYPES  `cheese_types`
- правило: Kinds of cheese sold in American grocery stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~camembert, ~gruyere, ~muenster, ~provolone, +American, +blue cheese, +brie, +cheddar, +colby, +cottage cheese, +cream cheese, +feta, +goat cheese, +gouda, +monterey jack, +mozzarella, +parmesan, +ricotta, +swiss, !havarti

### CITRUS FRUITS  `citrus_fruits`
- правило: Fruits of the citrus family with a thick peel and juicy segments
- тип связи: `is_a`, базовая сложность 0.25
- слов: 10
- ~citron, ~kumquat, ~pomelo, +clementine, +grapefruit, +lemon, +lime, +mandarin, +orange (orange_fruit), +tangerine

### COLD DRINKS  `cold_drinks`
- правило: Drinks normally served cold
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- ~horchata, ~kombucha, ~slushie, +coconut water, +cola, +ginger ale, +iced tea, +juice, +lemonade, +milk, +milkshake, +punch (punch_drink), +root beer, +seltzer, +smoothie, +soda, +sports drink, +water

### CONDIMENTS  `condiments`
- правило: Things squeezed or spooned onto food at the table
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~aioli, +barbecue sauce, +chutney, +honey, +horseradish, +hot sauce, +jam, +ketchup, +mayo, +mustard, +pesto, +ranch, +relish, +salsa, +soy sauce, +sriracha, +syrup, +tartar sauce, +vinegar, +wasabi

### COOKING FATS  `cooking_fats`
- правило: Fats and oils used to cook or dress food
- тип связи: `used_in`, базовая сложность 0.4
- слов: 15
- +avocado oil, +bacon grease, +butter, +canola, +coconut oil, +corn oil, +ghee, +lard, +margarine, +olive oil, +peanut oil, +sesame oil, +shortening, +sunflower oil, +vegetable oil

### DAIRY PRODUCTS  `dairy_products`
- правило: Foods made from milk or sold in the dairy section
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- +butter, +buttermilk, +cheese, +condensed milk, +cottage cheese, +cream (cream_dairy), +cream cheese, +curd, +custard, +frozen yogurt, +gelato, +ghee, +half and half, +ice cream, +kefir, +milk, +sour cream, +whey, +whipped cream, +yogurt

### DESSERTS  `desserts`
- правило: Sweet dishes served at the end of a meal
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +brownie, +cake, +cheesecake, +cobbler, +cookie, +cupcake, +custard, +donut, +eclair, +flan, +fudge, +gelato, +ice cream, +macaron, +mousse, +parfait, +pie, +Popsicle, +pudding, +souffle, +strudel, +sundae, +tart, +tiramisu, +trifle

### EGG DISHES  `egg_dishes`
- правило: Ways eggs are cooked and served
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~deviled, ~frittata, ~souffle, +benedict, +boiled, +custard, +egg salad, +fried, +omelet, +over easy, +poached, +quiche, +scrambled, +sunny side up

### DRIVE THRU  `fast_food_items`
- правило: Items ordered at an American fast food counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~quesadilla, +biscuit, +burger, +burrito, +chicken sandwich, +chili (chili_dish), +corn dog, +fries, +hot dog, +milkshake, +mozzarella stick, +nugget, +onion ring, +pizza, +slider, +soda, +sub, +sundae, +taco, +wrap

### FROZEN FOODS  `frozen_foods`
- правило: Foods normally bought from the freezer aisle
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~tater tot, +berries, +burrito, +chicken nugget, +corn dog, +dumpling, +fish stick, +french fries, +hash brown, +ice cream, +lasagna, +peas, +pizza, +Popsicle, +pot pie, +sorbet, +spinach, +waffle

### FRUITS  `fruits`
- правило: Common edible fruits familiar to an average American adult
- тип связи: `is_a`, базовая сложность 0.1
- слов: 26
- ~date (date_fruit), +apple (apple_fruit), +apricot, +banana, +blackberry, +blueberry, +cantaloupe, +cherry, +cranberry, +grape, +grapefruit, +kiwi, +lemon, +lime, +mango, +nectarine, +orange (orange_fruit), +papaya, +peach, +pear, +pineapple, +plum, +raspberry, +strawberry, +tangerine, +watermelon

### GRAINS AND BEANS  `grains_and_beans`
- правило: Grains, beans and other dried staples cooked as food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +barley, +black bean, +chickpea, +corn, +couscous, +kidney bean, +lentil, +millet, +oat, +pinto bean, +quinoa, +rice, +rye, +soybean, +wheat

### HOT DRINKS  `hot_drinks`
- правило: Drinks normally served hot
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- +americano, +broth, +cappuccino, +chai, +chamomile, +cider, +cocoa, +coffee, +espresso, +green tea, +herbal tea, +hot chocolate, +latte, +macchiato, +mocha, +mulled wine, +tea, +toddy

### ICE CREAM  `ice_cream_flavors`
- правило: Flavors of ice cream sold in American shops
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +banana, +birthday cake, +butter pecan, +caramel, +cherry, +chocolate, +coffee, +cookie dough, +cookies and cream, +lemon, +mango, +mint (mint_candy), +moose tracks, +neapolitan, +peach, +pistachio, +rocky road, +sherbet, +strawberry, +vanilla

### ITALIAN DISHES  `italian_dishes`
- правило: Dishes from Italian cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~antipasto, ~bruschetta, ~calzone, ~cannoli, ~carbonara, ~focaccia, ~minestrone, ~parmigiana, ~tiramisu, +alfredo, +gelato, +gnocchi, +lasagna, +meatball, +panini, +pesto, +pizza, +ravioli, +risotto, +spaghetti

### LEAFY GREENS  `leafy_greens`
- правило: Vegetables eaten for their leaves
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~arugula, ~bok choy, +cabbage, +chard, +collard, +endive, +kale, +lettuce, +parsley, +romaine, +spinach, +watercress

### MEATS  `meats`
- правило: Kinds of meat sold at an American butcher counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~pastrami, ~turkey (turkey_meat), +bacon, +beef, +bologna, +brisket, +chicken, +chop, +ground beef, +ham, +hot dog, +jerky, +lamb, +liver, +meatball, +pepperoni, +pork, +ribs, +roast, +salami, +sausage, +steak, +veal, +venison, !duck (duck_meat)

### MEXICAN DISHES  `mexican_dishes`
- правило: Dishes from Mexican cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~carnitas, ~churro, ~empanada, ~fajita, ~flan, ~horchata, ~pozole, ~quesadilla, ~tostada, +burrito, +enchilada, +guacamole, +nacho, +queso, +salsa, +taco, +tamale, !elote, !mole (mole_sauce), xchile relleno

### NUTS AND SEEDS  `nuts_and_seeds`
- правило: Edible nuts and seeds sold as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~flaxseed, +almond, +cashew, +chestnut, +hazelnut, +macadamia, +peanut, +pecan, +pine nut, +pistachio, +pumpkin seed, +sesame, +sunflower seed, +walnut

### PANTRY STAPLES  `pantry_staples`
- правило: Basic foods kept in a kitchen pantry for a long time
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~oil (oil_cooking), +baking soda, +beans, +broth, +canned soup, +cereal, +coffee, +flour, +honey, +ketchup, +oats, +pasta, +peanut butter, +rice, +salt, +spaghetti, +sugar, +tea, +tuna, +vinegar

### PASTA SHAPES  `pasta_shapes`
- правило: Shapes of pasta sold in American stores
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~penne, +angel hair, +gnocchi, +lasagna, +linguine, +macaroni, +ravioli, +shells, +spaghetti, !cannelloni, !farfalle, !fettuccine, !orzo, !rigatoni, !tortellini, !vermicelli, !ziti, xrotini

### PIE INGREDIENTS  `pie_ingredients`
- правило: Ingredients commonly used in pie fillings or pie preparation
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- +apple (apple_fruit), +blueberry, +butter, +cherry, +chocolate, +cinnamon, +coconut, +cornstarch, +cream (cream_dairy), +crust, +custard, +egg, +flour, +lemon, +molasses, +nutmeg, +peach, +pecan, +pumpkin, +raisin, +rhubarb, +salt, +shortening, +sugar, +vanilla

### PIZZA TOPPINGS  `pizza_toppings`
- правило: Ingredients commonly put on top of a pizza
- тип связи: `used_in`, базовая сложность 0.2
- слов: 25
- ~arugula, +anchovy, +artichoke, +bacon, +basil, +broccoli, +cheese, +chicken, +egg, +garlic, +ham, +jalapeno, +meatball, +mushroom, +olive, +onion, +pepper, +pepperoni, +pineapple, +ricotta, +salami, +sausage, +shrimp, +spinach, +tomato

### ROOT VEGETABLES  `root_vegetables`
- правило: Vegetables eaten for the part that grows underground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 13
- +beet, +carrot, +garlic, +ginger (ginger_spice), +horseradish, +onion, +parsnip, +potato, +radish, +rutabaga, +sweet potato, +turnip, +yam

### SALAD INGREDIENTS  `salad_ingredients`
- правило: Ingredients tossed into an ordinary green salad
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~arugula, ~crouton, +almond, +avocado, +bacon bits, +beet, +cabbage, +carrot, +celery, +cheese, +chickpea, +corn, +cranberry, +cucumber, +dressing, +egg, +lettuce, +mushroom, +olive, +onion, +pepper, +radish, +spinach, +tomato, +walnut

### SANDWICH FILLINGS  `sandwich_fillings`
- правило: Things commonly put inside a sandwich
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~pastrami, ~turkey (turkey_meat), +avocado, +bacon, +cheese, +chicken, +coleslaw, +corned beef, +cucumber, +egg salad, +ham, +hummus, +jelly, +lettuce, +mayo, +meatball, +mustard, +onion, +peanut butter, +pickle, +roast beef, +salami, +sprouts, +tomato, +tuna

### SEAFOOD  `seafood`
- правило: Fish and shellfish eaten as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~mahi mahi, +anchovy, +catfish, +caviar, +clam, +cod, +crab, +crawfish, +eel, +halibut, +herring, +lobster, +mussel, +octopus, +oyster, +salmon, +sardine, +scallop, +shrimp, +snapper, +squid, +swordfish, +tilapia, +trout, +tuna

### SNACK FOODS  `snack_foods`
- правило: Packaged foods eaten between meals
- тип связи: `is_a`, базовая сложность 0.2
- слов: 19
- +candy bar, +cheese stick, +chips, +cookie, +fruit snack, +granola bar, +hummus, +jerky, +muffin, +nuts, +pita chips, +popcorn, +Popsicle, +pretzel, +puffs, +raisin, +rice cake, +trail mix, +yogurt

### SOUP INGREDIENTS  `soup_ingredients`
- правило: Ingredients commonly simmered into a pot of soup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 25
- ~cream (cream_dairy), +bacon, +barley, +bean, +broth, +cabbage, +carrot, +celery, +chicken, +corn, +dumpling, +garlic, +ham, +leek, +lentil, +mushroom, +noodle, +onion, +parsley, +pasta, +pepper, +potato, +rice, +salt, +tomato

### SPICES AND HERBS  `spices_and_herbs`
- правило: Plant-based seasonings used to flavor food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~chive, ~tarragon, +allspice, +basil, +bay leaf, +cardamom, +cilantro, +cinnamon, +clove, +coriander, +cumin, +dill, +fennel, +ginger (ginger_spice), +mint (mint_herb), +nutmeg, +oregano, +paprika, +parsley, +pepper, +rosemary, +saffron, +sage (sage_herb), +thyme, +turmeric

### THANKSGIVING FOODS  `thanksgiving_foods`
- правило: Foods traditionally served at an American Thanksgiving dinner
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~squash (squash_vegetable), +apple cider, +biscuit, +brussels sprouts, +corn, +cornbread, +cranberry, +cranberry sauce, +gravy, +green bean casserole, +ham, +mashed potatoes, +pecan pie, +pie, +pumpkin pie, +rolls, +stuffing, +sweet potato, +turkey (turkey_meat), +yam

### MELTING THINGS  `things_that_melt`
- правило: Everyday things that melt when they get warm
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~butter, ~candle, ~caramel, ~cheese, ~chocolate, ~crayon, ~frosting, ~gelato, ~glacier, ~ice cream, ~icicle, ~lard, ~marshmallow, ~Popsicle, +ice, +snow, +sugar, !wax (wax_substance)

### SPREADS  `things_you_spread`
- правило: Foods that are spread with a knife onto bread or toast
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~apple butter, ~butter, ~cream cheese, ~frosting, ~guacamole, ~honey, ~hummus, ~jam, ~jelly, ~margarine, ~marmalade, ~mayo, ~mustard, ~nutella, ~peanut butter, ~ricotta

### TROPICAL FRUITS  `tropical_fruits`
- правило: Fruits that grow in tropical climates and are sold in American stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~jackfruit, +banana, +coconut, +dragon fruit, +guava, +lychee, +mango, +papaya, +passion fruit, +pineapple, +plantain, !starfruit

### VEGETABLES  `vegetables`
- правило: Common edible vegetables sold in an ordinary American grocery store
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- +artichoke, +asparagus, +bean, +beet, +broccoli, +cabbage, +carrot, +cauliflower, +celery, +corn, +cucumber, +eggplant, +kale, +leek, +lettuce, +onion, +parsnip, +pea, +potato, +radish, +spinach, +squash (squash_vegetable), +tomato, +turnip, +zucchini


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


## Тема: materials

### BUILDING MATERIALS  `building_materials`
- правило: Materials used to construct buildings
- тип связи: `made_of`, базовая сложность 0.25
- слов: 20
- +aluminum, +brick, +cement, +concrete, +drywall, +glass, +granite, +insulation, +lumber, +marble (marble_stone), +plaster, +plywood, +shingle, +slate, +steel, +stone, +stucco, +tile, +vinyl, +wood

### FABRIC TYPES  `fabric_types`
- правило: Kinds of cloth used to make things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~gingham, ~taffeta, +burlap, +canvas, +chiffon, +corduroy, +cotton, +denim, +felt, +flannel, +jersey, +lace, +linen, +muslin, +satin, +silk, +terry, +tweed, +velvet, +wool

### INSULATING MATERIALS  `insulating_materials`
- правило: Materials used to keep heat or sound in or out
- тип связи: `used_in`, базовая сложность 0.45
- слов: 13
- ~air, ~cellulose, ~cork, ~cotton, ~felt, ~fiberglass, ~foam, ~plastic, ~rubber, ~styrofoam, ~wool, !drywall, !straw (straw_hay)

### LIQUIDS  `liquids`
- правило: Common liquids found around a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~oil (oil_cooking), +alcohol, +bleach, +broth, +coffee, +gasoline, +glue, +ink, +juice, +lotion, +milk, +paint, +polish (polish_product), +shampoo, +soap, +soda, +syrup, +tea, +vinegar, +water

### MINERALS  `minerals`
- правило: Minerals found in the earth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~feldspar, ~hematite, +calcite, +graphite, +gypsum, +magnetite, +mica, +pyrite, +quartz, +sulfur, +talc, !azurite, !fluorite, !halite

### POWDERS  `powders`
- правило: Common substances that come as a powder
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~baking soda, ~cement, ~chalk (chalk_stick), ~cinnamon, ~cocoa, ~detergent, ~dust, ~flour, ~powdered milk, ~protein powder, ~salt, ~sand, ~spice, ~talcum, +sugar

### PRECIOUS MATERIALS  `precious_materials`
- правило: Rare and valuable materials
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~marble (marble_stone), +amber, +diamond (diamond_gem), +emerald, +gold, +ivory, +jade, +mahogany, +opal, +pearl, +platinum, +ruby, +sapphire, +silk, +silver

### RECYCLABLE MATERIALS  `recycled_materials`
- правило: Materials that can be recycled
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~aluminum, ~cardboard, ~carton, ~cloth, ~compost, ~electronics, ~rubber, ~tin (tin_can), +battery, +glass, +newspaper, +paper, +plastic, +steel

### GLASS THINGS  `things_made_of_glass`
- правило: Everyday things normally made of glass
- тип связи: `made_of`, базовая сложность 0.3
- слов: 15
- ~aquarium, ~bulb, ~greenhouse, ~jar, ~marble (marble_toy), ~ornament, ~prism, ~thermometer, ~tumbler, ~vase, +bottle, +lens, +mirror, +window, !screen (screen_display)

### LEATHER THINGS  `things_made_of_leather`
- правило: Everyday things normally made of leather
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~bookmark, ~boot (boot_shoe), ~briefcase, ~couch, ~glove, ~holster, ~purse, ~saddle, ~shoe, ~strap, ~wallet, +belt, +jacket

### METAL THINGS  `things_made_of_metal`
- правило: Everyday things normally made of metal
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~anchor, ~armor, ~faucet, ~hinge, ~kettle, ~key (key_lock), ~ladder, ~nail (nail_metal), ~pipe (pipe_tube), ~spoon, ~wrench, +bell, +can, +chain, +coin, +safe, +sword, +wire

### PAPER THINGS  `things_made_of_paper`
- правило: Everyday things normally made of paper
- тип связи: `made_of`, базовая сложность 0.3
- слов: 16
- ~card (card_greeting), ~carton, ~envelope, ~napkin, ~origami, ~receipt, ~ticket (ticket_admission), ~tissue (tissue_paper), ~wallpaper, +bag, +book, +calendar, +map, +newspaper, +poster, !kite (kite_toy)

### PLASTIC THINGS  `things_made_of_plastic`
- правило: Everyday things normally made of plastic
- тип связи: `made_of`, базовая сложность 0.35
- слов: 16
- ~bucket, ~comb, ~container, ~crate, ~hanger, ~helmet, ~pipe (pipe_tube), ~ruler, ~straw (straw_tube), +bag, +bottle, +chair, +cup, +toy, !card (card_plastic), !keyboard (keyboard_computer)

### RUBBER THINGS  `things_made_of_rubber`
- правило: Everyday things normally made of rubber
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~band (band_ring), ~boot (boot_shoe), ~bumper, ~duck (duck_toy), ~eraser, ~gasket, ~glove, ~hose, ~mat, ~seal (seal_rubber), ~stamp (stamp_tool), ~tire, ~tube

### WOODEN THINGS  `things_made_of_wood`
- правило: Everyday things normally made of wood
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~bat (bat_equipment), ~broom handle, ~cabinet (cabinet_furniture), ~canoe, ~crate, ~ladder, ~pencil, ~shelf (shelf_furniture), ~spoon, ~toothpick, +barrel, +chair, +deck, +door, +drum, +fence, +guitar, +table

### FUELS  `things_that_burn`
- правило: Materials burned to produce heat or power
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +alcohol, +charcoal, +coal, +diesel, +ethanol, +gasoline, +kerosene, +natural gas, +oil (oil_motor), +paper, +peat, +propane, +wax (wax_substance), +wood


## Тема: misc

### GLOVE BOX  `things_in_a_glove_box`
- правило: Things kept in a car glove compartment
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~Charger, ~flashlight, ~ice scraper, ~manual, ~napkins, ~registration, ~sunglasses, ~tire gauge, ~tissues, +insurance, +map, !gum (gum_candy), !pen (pen_writing)

### PURSE THINGS  `things_in_a_purse`
- правило: Things carried in a purse
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~hairbrush, +Charger, +hand sanitizer, +keys, +lipstick, +mirror, +pen (pen_writing), +phone, +planner, +receipt, +snack, +sunglasses, +tissue (tissue_paper), +wallet, !gum (gum_candy)

### TOOLBOX THINGS  `things_in_a_toolbox`
- правило: Things kept in a household toolbox
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- +allen key, +flashlight, +glue, +hammer, +level, +nails, +pliers, +sandpaper, +screwdriver, +screws, +tape, +tape measure, +utility knife, +wrench

### WALLET THINGS  `things_in_a_wallet`
- правило: Things people keep in a wallet
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~note (note_money), +badge, +business card, +card (card_plastic), +cash, +coupon, +gift card, +insurance card, +license, +membership card, +photo, +receipt, +stamp (stamp_postage), +ticket (ticket_admission)

### KEYCHAIN THINGS  `things_on_a_keychain`
- правило: Things hanging from a keychain
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~bottle opener, ~charm, ~flashlight, ~fob, ~lanyard, ~mini tool, ~souvenir, ~usb drive, ~whistle, +key (key_lock), +ring (ring_circle), !carabiner, !tag (tag_label)

### PAIRED THINGS  `things_that_come_in_pairs`
- правило: Things that normally come in twos
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~chopsticks, ~cufflinks, ~earrings, ~gloves, ~headphones, ~lungs, ~scissors, ~skis, ~socks, ~twins, +ears, +eyes, +hands, +shoes, +wings, !dice (dice_game)

### FACED THINGS  `things_that_have_a_face`
- правило: Objects described as having a face
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~building, ~cliff, ~clock, ~coin, ~doll, ~jack o lantern, ~mask, ~mountain, ~playing card, ~poster, ~puppet, ~snowman, ~watch (watch_object), !dice (dice_game)

### RINGING THINGS  `things_that_ring`
- правило: Things that ring or chime
- тип связи: `does_action`, базовая сложность 0.35
- слов: 12
- ~alarm, ~bicycle bell, ~buzzer, ~cash register, ~chime, ~church bell, ~clock, ~dinner bell, ~doorbell, ~timer, +bell, +phone

### TRASH ITEMS  `things_you_recycle`
- правило: Things commonly thrown out or recycled
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~carton, ~envelope, ~jar, ~packaging, ~peel, ~receipt, ~tissue (tissue_paper), ~wrapper, +bag, +bottle, +box, +can, +core, +newspaper

### VENDING MACHINE  `vending_machine_items`
- правило: Things sold from a vending machine
- тип связи: `found_in`, базовая сложность 0.35
- слов: 13
- ~gum (gum_candy), +candy bar, +chips, +coffee, +cookies, +granola bar, +juice, +mints, +popcorn, +pretzels, +sandwich, +soda, +water


## Тема: ocean

### CORAL REEF  `coral_reef`
- правило: Things found on a coral reef
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~angelfish, ~clownfish, ~parrotfish, ~sponge (sponge_animal), +algae, +anemone, +coral, +eel, +grouper, +jellyfish, +reef shark, +seahorse, +starfish, +turtle, +urchin

### DEEP SEA  `deep_sea`
- правило: Things found in the deep ocean
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~abyss, ~darkness, ~lantern fish, ~pressure, ~sediment, ~squid, ~submarine, ~trench, ~tube worm, ~vent, ~whale fall, ?viperfish, !anglerfish

### DIVING GEAR  `diving_gear`
- правило: Equipment used for scuba diving and snorkeling
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~hood (hood_garment), +buoy, +compass, +dive knife, +fins, +flashlight, +gauge, +gloves, +mask, +regulator, +snorkel, +tank (tank_container), +weight belt, +wetsuit

### FISH  `fish_species`
- правило: Kinds of fish an average person can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~guppy, +anchovy, +bass (bass_fish), +carp, +catfish, +cod, +flounder, +goldfish, +grouper, +halibut, +herring, +mackerel, +marlin, +minnow, +perch, +pike, +salmon, +sardine, +snapper, +sturgeon, +swordfish, +tilapia, +trout, +tuna, +walleye

### HARBOR THINGS  `harbor_things`
- правило: Things found in a harbor or marina
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- +anchor, +boat, +breakwater, +buoy, +dock, +jetty, +Lighthouse, +mooring, +net, +pier, +ramp, +rope, +tugboat, +warehouse, +wharf, !crane (crane_machine)

### NAVIGATION TOOLS  `navigation_tools`
- правило: Tools used to find the way at sea
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~astrolabe, ~sextant, ~star (star_space), +beacon, +buoy, +chart, +compass, +gps, +Lighthouse, +log, +map, +radar, +sonar, +telescope

### SEA HARVEST  `ocean_products`
- правило: Useful things people harvest from the sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~amber, ~coral, ~kelp, ~pearl, ~plankton, ~salt, ~sand, ~seaweed, ~shell, ~sponge (sponge_animal), +fish, !ambergris, !oil (oil_crude)

### SHORE FEATURES  `ocean_zones`
- правило: Features of the ocean and its shoreline
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~sandbar, ~undertow, +atoll, +bay, +cliff, +cove, +current (current_water), +estuary, +gulf, +inlet, +lagoon, +reef, +shore, +surf, +tide, +trench, +wave (wave_water), !shelf (shelf_sea)

### SEA MAMMALS  `sea_mammals`
- правило: Mammals that live in the sea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~dugong, ~narwhal, +beluga, +blue whale, +dolphin, +humpback, +manatee, +orca, +otter, +porpoise, +sea lion, +seal (seal_animal), +walrus, +whale

### SEA LEGENDS  `sea_myths`
- правило: Creatures and stories from sea legend
- тип связи: `found_in`, базовая сложность 0.4
- слов: 11
- ~davy jones, ~flying dutchman, ~ghost ship, ~kraken, ~leviathan, ~mermaid, ~sea monster, ~sea serpent, ~siren, ~triton, ~Whirlpool

### SEA CONDITIONS  `sea_weather`
- правило: Words describing conditions at sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~breaker, ~calm (calm_sea), ~chop, ~choppy, ~current (current_water), ~doldrums, ~fog, ~gale, ~rough, ~spray, ~squall, ~swell, ~tide, !whitecap

### SEABIRDS  `seabirds`
- правило: Birds that live along the coast or at sea
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~cormorant, ~gannet, ~petrel, ~sandpiper, ~skua, +albatross, +booby, +heron, +osprey, +pelican, +puffin, +seagull, +tern, xfrigatebird

### SHARKS AND RAYS  `sharks_and_rays`
- правило: Kinds of shark and ray
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~thresher, +bull shark, +great white, +hammerhead, +mako, +manta ray, +nurse shark, +reef shark, +stingray, +tiger shark, +whale shark, !sawfish

### SHELLFISH  `shellfish`
- правило: Sea animals with a shell that people eat
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~whelk, +abalone, +barnacle, +clam, +cockle, +crab, +crawfish, +lobster, +mussel, +oyster, +prawn, +scallop, +shrimp, +snail

### SEASHELLS  `shells`
- правило: Kinds of seashell found on a beach
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~abalone, ~auger, ~clam, ~cockle, ~conch, ~mussel, ~nautilus, ~olive shell, ~oyster, ~sand dollar, ~scallop, !cowrie, !whelk

### FISHING FLEET  `whaling_and_fishing`
- правило: Things used in commercial fishing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~buoy, ~crate, ~dredge, ~gaff, ~harpoon, ~hold, ~hook (hook_fishing), ~line (line_cord), ~net, ~pot, ~Seine, ~trap, ~trawler, ~winch


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

