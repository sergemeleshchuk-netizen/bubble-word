# Категории, часть 2 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: actions

### ANIMAL ACTIONS  `animal_actions`
- правило: Actions typical of animals rather than people
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~burrow, ~graze, ~hunt, ~pounce, ~shed, ~slither, +forage, +hatch, +hibernate, +migrate, +nest, +perch, +prowl, +roost, +spawn, !molt

### BUILDING ACTIONS  `building_actions`
- правило: Actions done when building or repairing something
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~assemble, ~bolt, ~drill (drill_tool), ~glue, ~hammer, ~install, ~level, ~measure, ~mount, ~paint, ~sand, ~saw, ~tile, ~weld, +nail (nail_metal), +plaster, +screw, !caulk

### CARRYING ACTIONS  `carrying_actions`
- правило: Ways of carrying or moving an object
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- ~roll (roll_turn), ~slide, ~toss, +carry, +drag, +haul, +heave, +hoist, +lift, +load, +pull, +push, +shove, +tow, +transport

### CLEANING ACTIONS  `cleaning_actions`
- правило: Actions done when cleaning something
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~dry, ~shine, +disinfect, +dust, +launder, +mop, +polish (polish_verb), +rinse, +scour, +scrub, +sweep, +tidy, +vacuum, +wash, +wipe, !declutter

### COOKING ACTIONS  `cooking_actions`
- правило: Verbs describing something a cook does to food
- тип связи: `does_action`, базовая сложность 0.25
- слов: 25
- ~broil, ~dice (dice_cut), ~drain, ~knead, ~mash, ~peel, ~roast, ~season (season_flavor), ~simmer, ~toss, ~whisk, +bake, +blend, +boil, +chop, +fry (fry_cook), +garnish, +grill, +marinate, +mince, +sear, +slice, +steam, +stir, !saute

### BREAKING ACTIONS  `destroying_actions`
- правило: Actions that damage or destroy something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~puncture, ~squash (squash_crush), +break, +burst, +crumble, +crush, +demolish, +dent, +flatten, +rip, +shatter, +shred, +smash, +snap, +split, +tear

### DRIVING ACTIONS  `driving_actions`
- правило: Actions done while driving a car
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- ~cruise, ~merge, +accelerate, +brake, +honk, +idle, +park (park_verb), +reverse, +shift (shift_gear), +signal, +stall (stall_engine), +steer, +swerve, +tailgate, +yield

### EATING ACTIONS  `eating_actions`
- правило: Actions done while eating or drinking
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- ~swallow (swallow_throat), +bite (bite_eat), +chew, +devour, +drink, +feast, +gnaw, +gulp, +lick, +munch, +nibble, +sip, +slurp, +snack, +taste

### GARDEN ACTIONS  `garden_actions`
- правило: Actions done while gardening
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- ~dig, ~fertilize, ~harvest, ~plant (plant_verb), ~seed, ~transplant, ~trim (trim_cut), ~water, +compost, +mow, +mulch, +prune, +rake, +sow (sow_plant), +weed

### GIVING AND TAKING  `giving_and_taking`
- правило: Verbs about transferring something to or from someone
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~hand (hand_give), +borrow, +buy, +collect, +deliver, +donate, +give, +lend, +offer, +receive, +return, +sell, +share, +swap, +take, +trade

### HAND ACTIONS  `hand_actions`
- правило: Actions performed with the hands
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- ~catch, ~knock, ~pinch, ~point (point_gesture), ~pull, ~push, ~rub, ~scratch, ~shake, ~tap (tap_touch), ~throw, ~twist, ~wave (wave_hand), ~wring, ~write, +clap, +grab, +hold, +slap, +squeeze

### JOINING ACTIONS  `joining_actions`
- правило: Actions that join two things together
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~buckle, ~button (button_clothing), ~clip, ~glue, ~stitch, ~tape, ~tie (tie_knot), +attach, +bind, +fasten, +knot, +link (link_chain), +sew, +staple, +weld, +zip

### MONEY ACTIONS  `money_actions`
- правило: Actions people do with money
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~refund, +bill (bill_money), +borrow, +budget, +deposit, +donate, +earn, +gamble, +invest, +lend, +owe, +pay, +save, +spend, +tip (tip_money), +withdraw

### OPENING ACTIONS  `opening_actions`
- правило: Actions that open or uncover something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~lift, ~peel, +open, +pry, +reveal, +uncover, +unfold, +unlock, +unwrap, +unzip, !unbutton, !uncork, !unroll, !unscrew

### SILENT ACTIONS  `quiet_actions`
- правило: Actions that make almost no noise
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~blink, ~nod, ~sleep, ~sneak, ~stare, ~tiptoe, ~whisper, ~wink, !breathe, !glide, !read, !smile, !think, !wave (wave_hand)

### SCHOOL ACTIONS  `school_actions`
- правило: Actions done at school
- тип связи: `does_action`, базовая сложность 0.3
- слов: 15
- ~calculate, ~present (present_show), ~quiz, ~recite, ~spell (spell_letters), ~submit, +grade, +learn, +memorize, +read, +research, +review, +study, +teach, +write

### SLEEP ACTIONS  `sleeping_actions`
- правило: Things a person does while sleeping or falling asleep
- тип связи: `does_action`, базовая сложность 0.35
- слов: 13
- ~stretch, ~toss, ~turn, +doze, +dream, +drift off, +nap, +rest (rest_sleep), +slumber, +snore, +wake, +yawn, !sleepwalk

### SPORTS ACTIONS  `sports_actions`
- правило: Actions done while playing sports
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~block (block_stop), ~dive, ~dribble, ~dunk (dunk_basketball), ~score (score_points), ~serve, ~shoot, ~spike, ~sprint, ~swing, ~tackle, +catch, +kick, +pass, +pitch, +punt, +throw, +volley

### THINKING ACTIONS  `thinking_actions`
- правило: Verbs for mental activity
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~doubt, ~focus (focus_mind), ~invent, ~judge, ~learn, ~plan, ~solve, +consider, +decide, +forget, +guess, +imagine, +recall, +remember, +think, +wonder

### WATER ACTIONS  `water_actions`
- правило: Actions done in or with water
- тип связи: `does_action`, базовая сложность 0.35
- слов: 18
- ~wash, +dive, +drain, +drip (drip_water), +dunk (dunk_dip), +float, +flood, +paddle, +pour, +rinse, +sink (sink_verb), +soak, +spill, +splash, +spray, +sprinkle, +swim, +wade

### WAYS OF LAUGHING  `ways_of_laughing`
- правило: Verbs for different kinds of laughing
- тип связи: `does_action`, базовая сложность 0.4
- слов: 11
- ~chortle, ~chuckle, ~giggle, ~guffaw, ~laugh, ~snicker, ~snort, !cackle, !howl, !roar, !titter

### WAYS OF LOOKING  `ways_of_looking`
- правило: Verbs describing a way of looking at something
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- +blink, +gaze, +glance, +glare, +inspect, +observe, +ogle, +peek, +peer, +scan, +spy, +squint, +stare, +survey, +watch (watch_look)

### WAYS OF MOVING  `ways_of_moving`
- правило: Verbs describing a way a person moves their body from place to place
- тип связи: `does_action`, базовая сложность 0.25
- слов: 26
- ~climb, ~march (march_walk), ~shuffle (shuffle_walk), ~slide, ~spring (spring_jump), ~swim, ~tiptoe, +crawl, +dart (dart_move), +dash (dash_run), +hop, +jog, +jump, +leap, +limp, +race, +run, +scramble, +skip, +sprint, +stagger, +stroll, +wade, +walk, +wander, !trudge

### WAYS OF SPEAKING  `ways_of_speaking`
- правило: Verbs describing a way of saying something aloud
- тип связи: `does_action`, базовая сложность 0.3
- слов: 18
- ~growl, ~hiss, ~stammer, +announce, +chant, +chatter, +declare, +gossip, +holler, +mumble, +murmur, +mutter, +recite, +scream, +shout, +sing, +whisper, +yell

### WEATHER ACTIONS  `weather_actions`
- правило: Verbs describing what weather does
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- ~flood, ~gust, ~shine, ~snow, ~thunder, +blow, +clear, +drizzle, +freeze, +hail, +melt, +pour, +rain, +sleet, +thaw


## Тема: brands

### AIRLINES  `airlines`
- правило: Major passenger airlines
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Alaska, ~American, ~delta (delta_airline), ~Frontier, ~Southwest, ~Spirit, ~United, +Air France, +British Airways, +Emirates, +JetBlue, +KLM, +Lufthansa, +Qantas

### APPLIANCE BRANDS  `appliance_brands`
- правило: Brands of home appliance
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~Samsung, ~Whirlpool, +Bosch, +Dyson, +GE, +Hoover, +Kenmore, +LG, !Amana, !Electrolux, !Frigidaire, !KitchenAid, !Maytag

### BANK BRANDS  `bank_brands`
- правило: Major American banks and card brands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~Ally, ~Chase, ~Discover, ~Visa, +Amex, +Capital One, +Citibank, +Mastercard, +PNC, +TD Bank, +US Bank, +Wells Fargo

### ELECTRONICS BRANDS  `camera_and_electronics`
- правило: Brands of consumer electronics
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Canon, ~Pioneer, ~Polaroid, ~Sharp, ~Sony, +Bose, +Fujifilm, +Kodak, +Nikon, +Panasonic, +Philips, +Toshiba, !JVC, !Sanyo

### DAIRY BRANDS  `candy_bar_flavors`
- правило: Ice cream brands sold in America
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Drumstick, ~Popsicle, +Ben and Jerry, +Blue Bell, +Dreyers, +Edys, +Eskimo Pie, +Klondike, +Magnum, !Breyers, !Haagen Dazs, xTalenti

### CANDY BRANDS  `candy_brands`
- правило: Candy brands sold in American stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Milky Way, +Almond Joy, +Hershey, +Jolly Rancher, +Kitkat, +Nerds, +Skittles, +Snickers, +Starburst, +Tootsie Roll, !Airheads, !Butterfinger, !Reeses, !Twix, !Twizzlers, !Whoppers

### CAR MODELS  `car_models`
- правило: Well known car model names
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~Accord, ~beetle, ~Explorer, ~Ranger, +Camaro, +Camry, +Charger, +Civic, +Corvette, +impala, +Jeep Wrangler, +Mustang, +Prius, +Silverado, +Tahoe, xF150

### CEREAL BRANDS  `cereal_brands`
- правило: Breakfast cereal brands sold in America
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Life, +Cheerios, +Cocoa Puffs, +Corn Flakes, +Frosted Flakes, +Grape Nuts, +Lucky Charms, +Raisin Bran, +Special K, !Chex, !Froot Loops, !Rice Krispies, !Trix, !Wheaties

### CLOTHING BRANDS  `clothing_brands`
- правило: Well known clothing and shoe brands
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Gap, ~Levi, ~puma, +Adidas, +Champion, +Converse, +Fruit of the Loom, +Hanes, +Lacoste, +New Balance, +Nike, +Reebok, +Timberland, +Vans, +Wrangler

### COFFEE BRANDS  `coffee_brands`
- правило: Coffee brands and coffee shops
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~caribou, ~Starbucks, +Community, +Dunkin, +Keurig, +Maxwell House, +Tim Hortons, +Yuban, !Folgers, !Lavazza, !Nescafe, !Peets

### FAST FOOD  `fast_food_chains`
- правило: Fast food restaurant chains in America
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~Sonic, ~Subway, +Burger King, +Chipotle, +Dairy Queen, +Dominos, +Five Guys, +KFC, +McDonalds, +Panera, +Pizza Hut, +Taco Bell, !Arbys, !Popeyes, !Wendys, !Whataburger

### HOTEL CHAINS  `hotel_chains`
- правило: Major hotel chains
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Best Western, +Days Inn, +Four Seasons, +Hilton, +Holiday Inn, +Hyatt, +Marriott, +Motel 6, +Radisson, +Sheraton, +Westin, !Ramada

### HARDWARE BRANDS  `paint_and_home`
- правило: Brands sold at a hardware store
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~Ace, +Gorilla Glue, +Scotch, +Sherwin Williams, +WD40, +Weber, !Behr, !Duracell, !Elmers, !Energizer, !Rustoleum, !Valspar

### RETAIL STORES  `retail_stores`
- правило: Large retail store chains in America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Target, +Aldi, +Best Buy, +Costco, +Dollar General, +Home Depot, +Kroger, +Lowes, +Nordstrom, +Publix, +Safeway, +Sears, +Staples, +Walmart, !Kohls, !Macys

### SNACK BRANDS  `snack_brands`
- правило: Brands of packaged snacks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Cheetos, +Chips Ahoy, +Doritos, +goldfish, +Lays, +Oreo, +Pringles, +Ritz, +Wheat Thins, !Fritos, !Keebler, !Nabisco, !Tostitos, xTriscuit

### SODA BRANDS  `soda_brands`
- правило: Soft drink brands sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~crush, +Barqs, +Canada Dry, +Coke, +Dr Pepper, +Fanta, +Mountain Dew, +Pepsi, +Sprite, +Squirt, !7up, !Faygo, !Schweppes, !Sunkist

### SPORTS BRANDS  `sports_brands`
- правило: Brands of sports equipment
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~head (head_brand), ~Prince, ~Wilson, +Bauer, +Callaway, +Easton, +Franklin, +Louisville Slugger, +Rawlings, +Spalding, !Schwinn, !Titleist

### TOOL BRANDS  `tool_brands`
- правило: Brands of hand and power tools
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~Craftsman, ~husky, +Black and Decker, +Bosch, +Milwaukee, +Snap On, +Stanley, !DeWalt, !Hilti, !Makita, !Ryobi, !Skil

### TOY BRANDS  `toy_brands`
- правило: Well known toy brands
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Barbie, +Etch a Sketch, +Fisher Price, +Hasbro, +Hot Wheels, +Lego, +Lincoln Logs, +Mattel, +Nerf, +Play Doh, +Slinky, !Crayola, !Little Tikes, !Tonka

### LUXURY BRANDS  `watch_and_luxury`
- правило: Well known luxury brands
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Omega, +Armani, +Burberry, +Cartier, +Chanel, +Dior, +Ferrari, +Gucci, +Hermes, +Lamborghini, +Prada, +Rolex, +Tiffany, +Versace


## Тема: cities

### AFRICAN CITIES  `african_cities`
- правило: Well known cities in Africa
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Cairo, +Accra, +Addis Ababa, +Alexandria, +Cape Town, +Casablanca, +Dakar, +Durban, +Kampala, +Khartoum, +Lagos, +Marrakech, +Nairobi, +Pretoria, +Tunis, !Luanda

### TRANSPORT HUBS  `airports_and_ports`
- правило: Famous airports and transport hubs
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Charles de Gaulle, +Dubai International, +Gatwick, +Grand Central, +Heathrow, +JFK, +LAX, +Penn Station, +Union Station, !Narita, !Schiphol, xOHare

### EAST COAST  `american_east_cities`
- правило: Cities on the American East Coast
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Boston, ~buffalo, ~Philadelphia, ~Providence, ~Savannah, +Albany, +Baltimore, +Charleston, +Hartford, +Jacksonville, +Newark, +Norfolk, +Portland, +Richmond, +Wilmington

### WEST COAST  `american_west_cities`
- правило: Cities on the American West Coast
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~Seattle, +Anaheim, +Berkeley, +Eugene, +Fresno, +Long Beach, +Oakland, +Portland, +Sacramento, +San Diego, +San Jose, +Santa Monica, +Spokane, +Tacoma

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
- ~Cologne, ~Munich, +Antwerp, +Barcelona, +Bergen, +Bruges, +Edinburgh, +Florence, +Geneva, +Hamburg, +Krakow, +Liverpool, +Lyon, +Manchester, +Marseille, +Milan, +Naples, +Porto, +Rotterdam, +Salzburg, +Seville, +Turin, +Valencia, +Venice, +Zurich

### MIDWEST CITIES  `midwest_cities`
- правило: Cities in the American Midwest
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Chicago, ~Columbus, +Cincinnati, +Cleveland, +Des Moines, +Detroit, +Duluth, +Indianapolis, +Kansas City, +Milwaukee, +Minneapolis, +Omaha, +St Louis, +Toledo, +Wichita

### RESORT DESTINATIONS  `resort_towns`
- правило: Places people travel to for vacation
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Aspen, +Bali, +Cabo, +Cancun, +Ibiza, +Key West, +Lake Tahoe, +Maldives, +Maui, +Monaco, +Myrtle Beach, +Napa, +Palm Springs, +Santorini, +Vail

### LATIN CITIES  `south_american_cities`
- правило: Well known cities in South America
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Bogota, +Brasilia, +Buenos Aires, +Caracas, +Cartagena, +La Paz, +Medellin, +Montevideo, +Quito, +Rio de Janeiro, +Santiago, +Sao Paulo, !Asuncion, !Cusco

### SOUTHERN CITIES  `southern_cities`
- правило: Cities in the American South
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Houston, ~mobile, ~New Orleans, +Atlanta, +Austin, +Birmingham, +Charlotte, +Dallas, +Little Rock, +Louisville, +Memphis, +Miami, +Nashville, +Raleigh, +Tampa


## Тема: clothing

### ACCESSORIES  `accessories`
- правило: Small items worn or carried to complete an outfit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~backpack, ~brooch, ~clutch, ~hat, ~headband, ~purse, ~scarf, ~sunglasses, ~tie (tie_clothing), ~umbrella, ~wallet, ~watch (watch_object), +belt, +cufflinks, +gloves, +handbag, +suspenders, !bowtie

### CLOTHING ITEMS  `clothing_items`
- правило: Garments worn on the body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~glove, ~hat, ~sock, ~tie (tie_clothing), +blazer, +blouse, +cardigan, +coat (coat_garment), +dress, +hoodie, +jacket, +jeans, +leggings, +overalls, +pants, +robe, +scarf, +shirt, +shorts, +skirt, +suit (suit_clothing), +sweater, +sweatshirt, +tank top, +vest

### GARMENT PARTS  `clothing_parts`
- правило: Parts sewn into a piece of clothing
- тип связи: `part_of`, базовая сложность 0.3
- слов: 17
- ~hem, ~hood (hood_garment), ~seam, ~strap, ~waistband, ~yoke, +belt loop, +buckle, +button (button_clothing), +collar, +cuff, +lapel, +lining, +pocket, +sleeve, +zipper, !placket

### CLOTHING SIZES  `clothing_sizes`
- правило: Words used for clothing sizes and fit
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~plus, ~regular, +large, +loose, +medium, +narrow, +oversized, +petite, +slim, +small, +snug, +tall, +tight, +wide

### FABRICS  `fabrics`
- правило: Materials that clothes are made from
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~canvas, ~lace, ~spandex, +cashmere, +chiffon, +corduroy, +cotton, +denim, +flannel, +fleece, +leather, +linen, +nylon, +polyester, +satin, +silk, +suede, +tweed, +velvet, +wool

### FOOTWEAR  `footwear`
- правило: Things worn on the feet
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- ~flat, ~pump, +boot (boot_shoe), +clog, +flip-flop, +galosh, +heel, +hiking boot, +oxford, +sandal, +slip on, +slipper, +sneaker, +sock, +stiletto, +wedge, !cleat, !loafer, !moccasin, !wader

### FORMAL WEAR  `formal_wear`
- правило: Clothing worn to a formal occasion
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~corsage, ~tails, ~veil, ~waistcoat, +cocktail dress, +cufflinks, +dress shoes, +evening dress, +gown, +sash, +suit (suit_clothing), +tuxedo, !bowtie, !cummerbund

### HATS  `hats`
- правило: Things worn on the head
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~crown (crown_royal), ~hood (hood_garment), ~turban, +baseball cap, +beanie, +beret, +bonnet, +bowler, +cap, +cowboy hat, +fedora, +hard hat, +headband, +helmet, +sombrero, +sun hat, +top hat, +visor

### JEWELRY  `jewelry`
- правило: Decorative items worn on the body as jewelry
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- ~anklet, ~brooch, ~cufflink, ~hoop, ~locket, ~pin (pin_fastener), ~ring (ring_jewelry), ~stud, ~tiara, ~watch (watch_object), +bangle, +bracelet, +chain, +charm, +choker, +earring, +necklace, +pendant

### KIDS CLOTHING  `kids_clothing`
- правило: Clothing made especially for babies and children
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~diaper, ~jumper, ~mittens, ~overalls, +bib, +booties, +onesie, +smock, !footie pajamas, !romper, !snowsuit, !sunhat

### LAUNDRY CARE  `laundry_care`
- правило: Things done to clothes to keep them clean and neat
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~bleach, ~dry, ~hang, ~iron (iron_appliance), ~mend, ~press (press_push), ~soak, ~sort, ~steam, +dry clean, +fold, +rinse, +starch, +wash

### SEWING WORDS  `sewing_words`
- правило: Words used when sewing or altering clothes
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~alter, ~bobbin, ~cuff, ~dart (dart_sew), ~tuck, +hem, +lining, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam, +stitch, +thimble, +thread, !baste, !pleat

### SHOE PARTS  `shoe_parts`
- правило: Parts of a shoe
- тип связи: `part_of`, базовая сложность 0.35
- слов: 14
- ~cushion, ~strap, ~tongue, ~upper, +arch (arch_foot), +buckle, +heel, +lace, +shank, +sole (sole_shoe), +toe, +tread, !eyelet, !insole

### SLEEPWEAR  `sleepwear`
- правило: Clothing worn to bed
- тип связи: `is_a`, базовая сложность 0.25
- слов: 10
- ~boxers, +lounge pants, +nightgown, +onesie, +pajamas, +robe, +sleep mask, +slippers, !nightcap, !nightshirt

### SWIMWEAR  `swimwear`
- правило: Clothing worn for swimming
- тип связи: `is_a`, базовая сложность 0.25
- слов: 11
- +bikini, +board shorts, +cover up, +flippers, +goggles, +one piece, +rash guard, +swim cap, +swimsuit, +trunks, +wetsuit

### THINGS WITH POCKETS  `things_with_pockets`
- правило: Clothes and bags that have pockets
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~apron (apron_garment), ~backpack, ~blazer, ~coat (coat_garment), ~hoodie, ~jacket, ~jeans, ~overalls, ~purse, ~robe, ~shirt, ~suitcase, ~vest, !cargo pants

### HAND WEAR  `things_worn_on_hands`
- правило: Things worn on the hands
- тип связи: `has_property`, базовая сложность 0.3
- слов: 12
- ~bandage, ~bracelet, ~cast (cast_medical), ~glove, ~mitten, ~ring, ~splint, ~watch (watch_object), !boxing glove, !gauntlet, !nail polish, !oven mitt

### BUTTONED THINGS  `things_you_button`
- правило: Clothes and objects fastened with buttons
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~blouse, ~cardigan, ~coat (coat_garment), ~cuff, ~glove, ~jacket, ~jeans, ~overalls, ~pajamas, ~pants, ~shirt, ~sweater, ~vest, !pillowcase

### TIED THINGS  `things_you_tie`
- правило: Things fastened by tying a knot or bow
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~bandana, ~belt, ~knot, ~laces, ~ribbon, ~rope, ~sash, ~scarf, ~shoelace, ~tie (tie_knot), !apron (apron_garment), !bowtie, !drawstring, !hair tie

### WINTER CLOTHING  `winter_clothing`
- правило: Clothing worn specifically to stay warm in cold weather
- тип связи: `used_in`, базовая сложность 0.2
- слов: 18
- ~beanie, ~boot (boot_shoe), ~hood (hood_garment), ~mitten, ~muffler, +coat (coat_garment), +down jacket, +fleece, +glove, +parka, +scarf, +shawl, +ski mask, +snow pants, +sweater, +wool socks, !earmuffs, !thermals

### UNIFORMS  `work_uniforms`
- правило: Outfits worn as a required uniform for work or school
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~apron (apron_garment), ~badge, ~blazer, ~kilt, ~scrubs, ~vest, +chef coat, +hard hat, +jumpsuit, +lab coat, +smock, +tunic, !cassock, !coveralls


## Тема: education

### FIRST LESSONS  `alphabet_and_numbers`
- правило: The very first things children learn at school
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~addition, ~color, ~count, ~day, ~letter (letter_alphabet), ~month, ~name, ~number, ~season (season_time), ~shape, ~sound (sound_noise), ~word, +alphabet, +rhyme, +sight word

### ART CLASS  `art_class_things`
- правило: Things used in a school art class
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~apron (apron_garment), ~brush, ~chalk (chalk_stick), ~clay, ~glitter, ~glue, ~kiln, ~marker, ~pastel, ~scissors, +canvas, +construction paper, +easel, +paint, +palette, +sketchbook, +smock, +stencil

### CLASSROOM THINGS  `classroom_things`
- правило: Things found in a school classroom
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~alphabet, ~bell, ~bookshelf, ~calendar, ~chair, ~clock, ~desk, ~easel, ~flag, ~globe, ~map, ~poster, +chalk (chalk_stick), +chalkboard, +cubby, +hall pass, +locker, +projector, +textbook, +whiteboard

### COLLEGE WORDS  `college_words`
- правило: Words used about university education
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~credit, ~dean, ~major (major_study), ~minor, ~professor, ~sophomore, +alumni, +campus, +degree (degree_academic), +dorm, +fraternity, +freshman, +junior, +lecture, +scholarship, +semester, +seminar, +senior, +thesis, +tuition

### ACADEMIC DEGREES  `degrees_and_titles`
- правило: Degrees and academic qualifications
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~associate, ~fellowship, ~license, +bachelor, +certificate, +credential, +diploma, +doctorate, +honors, +master, +MBA, +PhD

### FIELD TRIPS  `field_trip_places`
- правило: Places classes visit on a field trip
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~aquarium, ~bakery, ~capitol, ~factory, ~farm, ~gallery, ~orchard, ~park (park_place), ~theater, ~zoo, +fire station, +historical site, +museum, +planetarium, +science center

### GRADING WORDS  `grades_and_marks`
- правило: Words used to grade and evaluate students
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~average, ~credit, ~report card, +essay, +exam, +fail, +final, +GPA, +grade, +homework, +honor roll, +midterm, +pass, +quiz, +rubric, +score (score_points), +test, +transcript

### GYM CLASS  `gym_class_things`
- правило: Things used in a school gym class
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- ~cone, ~dodgeball, ~hoop, ~jump rope, ~locker, ~mat, ~net, ~sneakers, ~stopwatch, ~uniform, ~whistle, +ball (ball_sphere), +bleachers, +hurdle, +parachute, +scoreboard

### LEARNING ACTIONS  `learning_actions`
- правило: Things students do while learning
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~discuss, ~drill (drill_practice), ~listen, ~memorize, ~outline, ~practice, ~question, ~quiz, ~solve, +note (note_written), +read, +rehearse, +research, +review, +summarize, +write

### LIBRARY WORDS  `library_words`
- правило: Things and rules found in a library
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~aisle, ~atlas (atlas_book), ~card (card_plastic), ~checkout, ~fine, +archive, +book, +catalog, +due date, +encyclopedia, +librarian, +magazine, +periodical, +reference, +shelf (shelf_furniture), +silence, +stack (stack_shelves), +study room

### MUSIC CLASS  `music_class_things`
- правило: Things used in a school music class
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~bell, ~choir, ~conductor, ~metronome, ~stand (stand_holder), ~triangle, +drum, +piano, +recorder, +riser, +sheet music, +tambourine, !maraca, !xylophone

### KINDS OF PAPER  `paper_types`
- правило: Kinds of paper used at school and home
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~carbon (carbon_paper), ~construction, ~sticky note, ~wax (wax_substance), +graph, +index card, +loose leaf, +newsprint, +notebook, +parchment, +printer, +tissue (tissue_paper), +tracing, !cardstock

### READING WORDS  `reading_words`
- правило: Words used when reading and studying text
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~excerpt, ~glossary, ~summary, +appendix, +bibliography, +chapter, +footnote, +index, +page, +paragraph, +passage, +preface, +quote, +table of contents, +title

### SCHOOL EVENTS  `school_events`
- правило: Events that happen during a school year
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~exam, ~orientation, ~prom, +assembly, +book fair, +detention, +field trip, +graduation, +homecoming, +open house, +pep rally, +picture day, +recess, +science fair, +spelling bee, +talent show

### SCHOOL PEOPLE  `school_people`
- правило: People you meet at a school
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~classmate, ~counselor, ~librarian, ~nurse, +aide, +bus driver, +cafeteria worker, +coach, +crossing guard, +janitor, +principal, +student, +substitute, +teacher, +tutor, +volunteer

### SCHOOL PLACES  `school_places`
- правило: Rooms and places inside a school
- тип связи: `part_of`, базовая сложность 0.2
- слов: 18
- ~bathroom, ~cafeteria, ~courtyard, ~field, ~gym, ~lab, ~library, ~stage, +art room, +auditorium, +classroom, +computer lab, +hallway, +locker room, +nurse office, +office, +playground, +principal office

### SCHOOL SUBJECTS  `school_subjects`
- правило: Subjects taught in an American school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~art, ~band (band_group), ~biology, ~chemistry, ~drama, ~English, ~geography, ~gym, ~health, ~history, ~literature, ~music, ~shop, ~spanish, +algebra, +calculus, +civics, +computer science, +economics, +geometry, +home economics, +math, +physics, +science, +trigonometry

### SCHOOL SUPPLIES  `school_supplies`
- правило: Items a student brings to school in a backpack
- тип связи: `used_in`, базовая сложность 0.15
- слов: 25
- ~compass, ~glue, ~highlighter, ~marker, ~planner, ~protractor, ~ruler, ~scissors, ~tape, +backpack, +binder, +calculator, +crayon, +eraser, +folder, +index card, +lunchbox, +notebook, +paper, +pen (pen_writing), +pencil, +pencil case, +sharpener, +stapler, +textbook

### TEST WORDS  `testing_words`
- правило: Words for kinds of test questions and formats
- тип связи: `found_in`, базовая сложность 0.35
- слов: 12
- ~essay, ~final, ~oral, ~practical, +fill in the blank, +matching, +multiple choice, +open book, +pop quiz, +short answer, +timed, +true false

### WRITING TOOLS  `writing_tools`
- правило: Tools used to write or draw
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~brush, ~chalk (chalk_stick), ~charcoal, ~crayon, ~highlighter, ~keyboard (keyboard_computer), ~pastel, ~pen (pen_writing), +felt tip, +fountain pen, +marker, +pencil, +quill, +stylus, +typewriter


## Тема: food

### ASIAN DISHES  `asian_dishes`
- правило: Dishes from East and Southeast Asian cuisines eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~curry, ~ramen, ~sashimi, +chow mein, +dim sum, +dumpling, +egg roll, +fried rice, +kimchi, +lo mein, +miso soup, +pad thai, +pho, +spring roll, +sushi, +teriyaki, !bibimbap, !satay, !tempura, !wonton

### BAKING INGREDIENTS  `baking_ingredients`
- правило: Ingredients commonly used to bake cakes, bread or cookies
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~almond, ~baking powder, ~buttermilk, ~cinnamon, ~egg, ~honey, ~milk, ~molasses, ~oat, ~oil (oil_cooking), ~salt, +baking soda, +butter, +chocolate, +cocoa, +cream (cream_dairy), +flour, +frosting, +icing, +raisin, +shortening, +sugar, +syrup, +vanilla, +yeast

### BARBECUE FOODS  `bbq_foods`
- правило: Foods cooked or served at an American backyard barbecue
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~bun, ~chicken, ~chips, ~coleslaw, ~lemonade, ~mustard, ~pickle, ~watermelon, +baked beans, +brisket, +burger, +corn, +cornbread, +hot dog, +kebab, +macaroni salad, +potato salad, +pulled pork, +ribs, +sausage

### BERRIES  `berries`
- правило: Small soft fruits called berries in everyday American English
- тип связи: `is_a`, базовая сложность 0.2
- слов: 13
- +blackberry, +blueberry, +cherry, +cranberry, +currant, +gooseberry, +grape, +huckleberry, +mulberry, +raspberry, +strawberry, !boysenberry, !elderberry

### BREAD TYPES  `bread_types`
- правило: Kinds of bread and baked goods made from dough
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~scone, ~white (white_food), +bagel, +baguette, +banana bread, +biscuit, +brioche, +bun, +cornbread, +croissant, +muffin, +naan, +pita, +pretzel, +roll (roll_bread), +rye, +sourdough, +texas toast, +tortilla, +wheat, !challah, !ciabatta, !flatbread, !focaccia, !pumpernickel

### BREAKFAST FOODS  `breakfast_foods`
- правило: Foods typically eaten at breakfast in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~ham, ~jam, ~scone, +bacon, +bagel, +biscuit, +cereal, +coffee cake, +croissant, +danish, +doughnut, +egg, +french toast, +granola, +grits, +hash brown, +muffin, +oatmeal, +omelet, +pancake, +porridge, +sausage, +toast (toast_bread), +waffle, +yogurt

### CAKE TYPES  `cake_types`
- правило: Kinds of cake baked and sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~carrot, ~lava, ~marble (marble_cake), ~pound (pound_cake), ~shortcake, ~sponge (sponge_cake), ~vanilla, +angel food, +birthday, +cheesecake, +chocolate, +coffee cake, +cupcake, +ice cream cake, +layer, +red velvet, +upside down, +wedding, !bundt, !fruitcake

### CANDY  `candy`
- правило: Sweets sold in a candy aisle
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~brittle (brittle_candy), ~candy cane, ~gum (gum_candy), ~nougat, ~praline, +butterscotch, +caramel, +chocolate, +chocolate bar, +fudge, +jelly bean, +licorice, +lollipop, +marshmallow, +mint (mint_candy), +rock candy, +taffy, +toffee, +truffle, !gumdrop

### CHEESE TYPES  `cheese_types`
- правило: Kinds of cheese sold in American grocery stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~American, ~cottage cheese, ~cream cheese, +blue cheese, +brie, +cheddar, +colby, +feta, +goat cheese, +gouda, +monterey jack, +mozzarella, +parmesan, +ricotta, +swiss, !camembert, !gruyere, !havarti, !muenster, !provolone

### CITRUS FRUITS  `citrus_fruits`
- правило: Fruits of the citrus family with a thick peel and juicy segments
- тип связи: `is_a`, базовая сложность 0.25
- слов: 10
- ~lime, +clementine, +grapefruit, +lemon, +mandarin, +orange, +tangerine, !citron, !kumquat, !pomelo

### COLD DRINKS  `cold_drinks`
- правило: Drinks normally served cold
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- ~milk, ~root beer, ~seltzer, +coconut water, +cola, +ginger ale, +iced tea, +juice, +lemonade, +milkshake, +punch (punch_drink), +smoothie, +soda, +sports drink, +water, !horchata, !kombucha, !slushie

### CONDIMENTS  `condiments`
- правило: Things squeezed or spooned onto food at the table
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~honey, ~jam, ~pesto, ~ranch, ~salsa, ~syrup, ~vinegar, ~wasabi, +barbecue sauce, +chutney, +horseradish, +hot sauce, +ketchup, +mayo, +mustard, +relish, +soy sauce, +sriracha, +tartar sauce, !aioli

### COOKING FATS  `cooking_fats`
- правило: Fats and oils used to cook or dress food
- тип связи: `used_in`, базовая сложность 0.4
- слов: 15
- +avocado oil, +bacon grease, +butter, +canola, +coconut oil, +corn oil, +ghee, +lard, +margarine, +olive oil, +peanut oil, +sesame oil, +shortening, +sunflower oil, +vegetable oil

### DAIRY PRODUCTS  `dairy_products`
- правило: Foods made from milk or sold in the dairy section
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- ~butter, ~buttermilk, ~cottage cheese, ~frozen yogurt, ~milk, +cheese, +condensed milk, +cream (cream_dairy), +cream cheese, +curd, +custard, +gelato, +ghee, +half and half, +ice cream, +sour cream, +whey, +whipped cream, +yogurt, !kefir

### DESSERTS  `desserts`
- правило: Sweet dishes served at the end of a meal
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~flan, ~Popsicle, +brownie, +cake, +cheesecake, +cobbler, +cookie, +cupcake, +custard, +donut, +fudge, +gelato, +ice cream, +mousse, +pie, +pudding, +sundae, +tart, +trifle, !eclair, !macaron, !parfait, !souffle, !strudel, !tiramisu

### EGG DISHES  `egg_dishes`
- правило: Ways eggs are cooked and served
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~custard, ~quiche, +benedict, +boiled, +egg salad, +fried, +omelet, +over easy, +poached, +scrambled, +sunny side up, !deviled, !frittata, !souffle

### DRIVE THRU  `fast_food_items`
- правило: Items ordered at an American fast food counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~biscuit, ~pizza, ~soda, +burger, +burrito, +chicken sandwich, +chili (chili_dish), +corn dog, +fries, +hot dog, +milkshake, +mozzarella stick, +nugget, +onion ring, +slider, +sub, +sundae, +taco, +wrap, !quesadilla

### FROZEN FOODS  `frozen_foods`
- правило: Foods normally bought from the freezer aisle
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~burrito, ~ice cream, ~lasagna, ~pizza, ~Popsicle, ~pot pie, ~sorbet, ~spinach, ~waffle, +berries, +chicken nugget, +corn dog, +dumpling, +fish stick, +french fries, +hash brown, +peas, !tater tot

### FRUITS  `fruits`
- правило: Common edible fruits familiar to an average American adult
- тип связи: `is_a`, базовая сложность 0.1
- слов: 26
- ~date (date_fruit), ~nectarine, +apple (apple_fruit), +apricot, +banana, +blackberry, +blueberry, +cantaloupe, +cherry, +cranberry, +grape, +grapefruit, +kiwi, +lemon, +lime, +mango, +orange (orange_fruit), +papaya, +peach, +pear, +pineapple, +plum, +raspberry, +strawberry, +tangerine, +watermelon

### GRAINS AND BEANS  `grains_and_beans`
- правило: Grains, beans and other dried staples cooked as food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~chickpea, ~lentil, +barley, +black bean, +corn, +couscous, +kidney bean, +millet, +oat, +pinto bean, +quinoa, +rice, +rye, +soybean, +wheat

### HOT DRINKS  `hot_drinks`
- правило: Drinks normally served hot
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- ~broth, ~cider, +americano, +cappuccino, +chai, +chamomile, +cocoa, +coffee, +espresso, +green tea, +herbal tea, +hot chocolate, +latte, +mocha, +mulled wine, +tea, +toddy, !macchiato

### ICE CREAM  `ice_cream_flavors`
- правило: Flavors of ice cream sold in American shops
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~caramel, ~chocolate, ~coffee, ~lemon, ~mint (mint_candy), ~pistachio, +banana, +birthday cake, +butter pecan, +cherry, +cookie dough, +cookies and cream, +mango, +moose tracks, +neapolitan, +peach, +rocky road, +sherbet, +strawberry, +vanilla

### ITALIAN DISHES  `italian_dishes`
- правило: Dishes from Italian cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +alfredo, +gelato, +gnocchi, +lasagna, +meatball, +panini, +pesto, +pizza, +ravioli, +risotto, +spaghetti, !antipasto, !bruschetta, !calzone, !cannoli, !carbonara, !focaccia, !minestrone, !parmigiana, !tiramisu

### LEAFY GREENS  `leafy_greens`
- правило: Vegetables eaten for their leaves
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~endive, ~watercress, +cabbage, +chard, +collard, +kale, +lettuce, +parsley, +romaine, +spinach, !arugula, !bok choy

### MEATS  `meats`
- правило: Kinds of meat sold at an American butcher counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~chicken, ~duck (duck_meat), ~ground beef, ~liver, ~meatball, ~pastrami, ~turkey (turkey_meat), +bacon, +beef, +bologna, +brisket, +chop, +ham, +hot dog, +jerky, +lamb, +pepperoni, +pork, +ribs, +roast, +salami, +sausage, +steak, +veal, +venison

### MEXICAN DISHES  `mexican_dishes`
- правило: Dishes from Mexican cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~enchilada, ~flan, ~tamale, +burrito, +guacamole, +nacho, +queso, +salsa, +taco, !carnitas, !churro, !elote, !empanada, !fajita, !horchata, !mole (mole_sauce), !pozole, !quesadilla, !tostada, xchile relleno

### NUTS AND SEEDS  `nuts_and_seeds`
- правило: Edible nuts and seeds sold as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~sesame, +almond, +cashew, +chestnut, +hazelnut, +macadamia, +peanut, +pecan, +pine nut, +pistachio, +pumpkin seed, +sunflower seed, +walnut, !flaxseed

### PANTRY STAPLES  `pantry_staples`
- правило: Basic foods kept in a kitchen pantry for a long time
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~baking soda, ~broth, ~cereal, ~coffee, ~honey, ~ketchup, ~oil (oil_cooking), ~peanut butter, ~spaghetti, ~sugar, ~tea, ~tuna, ~vinegar, +beans, +canned soup, +flour, +oats, +pasta, +rice, +salt

### PASTA SHAPES  `pasta_shapes`
- правило: Shapes of pasta sold in American stores
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~linguine, ~shells, +angel hair, +gnocchi, +lasagna, +macaroni, +ravioli, +spaghetti, !cannelloni, !farfalle, !fettuccine, !orzo, !penne, !rigatoni, !tortellini, !vermicelli, !ziti, xrotini

### PIE INGREDIENTS  `pie_ingredients`
- правило: Ingredients commonly used in pie fillings or pie preparation
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~butter, ~cinnamon, ~cornstarch, ~egg, ~flour, ~lemon, ~molasses, ~nutmeg, ~salt, ~vanilla, +apple (apple_fruit), +blueberry, +cherry, +chocolate, +coconut, +cream (cream_dairy), +crust, +custard, +peach, +pecan, +pumpkin, +raisin, +rhubarb, +shortening, +sugar

### PIZZA TOPPINGS  `pizza_toppings`
- правило: Ingredients commonly put on top of a pizza
- тип связи: `used_in`, базовая сложность 0.2
- слов: 25
- ~anchovy, ~basil, ~chicken, ~egg, ~ham, ~meatball, ~mushroom, ~pepper, ~pineapple, ~sausage, ~shrimp, ~tomato, +artichoke, +bacon, +broccoli, +cheese, +garlic, +jalapeno, +olive, +onion, +pepperoni, +ricotta, +salami, +spinach, !arugula

### ROOT VEGETABLES  `root_vegetables`
- правило: Vegetables eaten for the part that grows underground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 13
- ~garlic, ~parsnip, ~rutabaga, ~sweet potato, +beet, +carrot, +ginger (ginger_spice), +horseradish, +onion, +potato, +radish, +turnip, +yam

### SALAD INGREDIENTS  `salad_ingredients`
- правило: Ingredients tossed into an ordinary green salad
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~almond, ~cheese, ~corn, ~cranberry, ~egg, ~mushroom, ~pepper, ~walnut, +avocado, +bacon bits, +beet, +cabbage, +carrot, +celery, +chickpea, +cucumber, +dressing, +lettuce, +olive, +onion, +radish, +spinach, +tomato, !arugula, !crouton

### SANDWICH FILLINGS  `sandwich_fillings`
- правило: Things commonly put inside a sandwich
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~avocado, ~chicken, ~hummus, ~meatball, ~mustard, ~pickle, ~sprouts, ~tomato, ~tuna, ~turkey (turkey_meat), +bacon, +cheese, +coleslaw, +corned beef, +cucumber, +egg salad, +ham, +jelly, +lettuce, +mayo, +onion, +peanut butter, +roast beef, +salami, !pastrami

### SEAFOOD  `seafood`
- правило: Fish and shellfish eaten as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~clam, ~halibut, ~octopus, +anchovy, +catfish, +caviar, +cod, +crab, +crawfish, +eel, +herring, +lobster, +mussel, +oyster, +salmon, +sardine, +scallop, +shrimp, +snapper, +squid, +swordfish, +tilapia, +trout, +tuna, !mahi mahi

### SNACK FOODS  `snack_foods`
- правило: Packaged foods eaten between meals
- тип связи: `is_a`, базовая сложность 0.2
- слов: 19
- ~chips, ~cookie, ~granola bar, ~hummus, ~jerky, ~nuts, ~Popsicle, ~yogurt, +candy bar, +cheese stick, +fruit snack, +muffin, +pita chips, +popcorn, +pretzel, +puffs, +raisin, +rice cake, +trail mix

### SOUP INGREDIENTS  `soup_ingredients`
- правило: Ingredients commonly simmered into a pot of soup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 25
- ~bacon, ~barley, ~carrot, ~chicken, ~corn, ~cream (cream_dairy), ~ham, ~lentil, ~mushroom, ~parsley, ~pepper, ~rice, ~salt, ~tomato, +bean, +broth, +cabbage, +celery, +dumpling, +garlic, +leek, +noodle, +onion, +pasta, +potato

### SPICES AND HERBS  `spices_and_herbs`
- правило: Plant-based seasonings used to flavor food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~allspice, ~coriander, +basil, +bay leaf, +cardamom, +cilantro, +cinnamon, +clove, +cumin, +dill, +fennel, +ginger (ginger_spice), +mint (mint_herb), +nutmeg, +oregano, +paprika, +parsley, +pepper, +rosemary, +saffron, +sage (sage_herb), +thyme, +turmeric, !chive, !tarragon

### THANKSGIVING FOODS  `thanksgiving_foods`
- правило: Foods traditionally served at an American Thanksgiving dinner
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~corn, ~cranberry, ~ham, ~pie, ~pumpkin pie, ~squash (squash_vegetable), ~sweet potato, +apple cider, +biscuit, +brussels sprouts, +cornbread, +cranberry sauce, +gravy, +green bean casserole, +mashed potatoes, +pecan pie, +rolls, +stuffing, +turkey (turkey_meat), +yam

### MELTING THINGS  `things_that_melt`
- правило: Everyday things that melt when they get warm
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~butter, ~candle, ~caramel, ~cheese, ~chocolate, ~crayon, ~frosting, ~glacier, ~ice, ~ice cream, ~icicle, ~lard, ~marshmallow, ~Popsicle, ~snow, ~sugar, !gelato, !wax (wax_substance)

### SPREADS  `things_you_spread`
- правило: Foods that are spread with a knife onto bread or toast
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~butter, ~cream cheese, ~frosting, ~guacamole, ~honey, ~hummus, ~jam, ~jelly, ~margarine, ~marmalade, ~mayo, ~mustard, ~peanut butter, !apple butter, !nutella, !ricotta

### TROPICAL FRUITS  `tropical_fruits`
- правило: Fruits that grow in tropical climates and are sold in American stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~guava, ~lychee, +banana, +coconut, +dragon fruit, +mango, +papaya, +passion fruit, +pineapple, +plantain, !jackfruit, !starfruit

### VEGETABLES  `vegetables`
- правило: Common edible vegetables sold in an ordinary American grocery store
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- ~corn, ~kale, ~parsnip, ~tomato, +artichoke, +asparagus, +bean, +beet, +broccoli, +cabbage, +carrot, +cauliflower, +celery, +cucumber, +eggplant, +leek, +lettuce, +onion, +pea, +potato, +radish, +spinach, +squash (squash_vegetable), +turnip, +zucchini


## Тема: jobs

### BEAUTY JOBS  `beauty_jobs`
- правило: Jobs held by people who work on hair, nails and appearance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +barber, +hairdresser, +makeup artist, +masseuse, +nail tech, +stylist, +tattoo artist, !colorist, !cosmetologist, !esthetician, !groomer, !manicurist

### BUILDING TRADES  `building_trades`
- правило: Skilled trades that build and repair buildings
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~bricklayer, ~foreman, ~painter, ~plumber, +carpenter, +contractor, +drywaller, +electrician, +installer, +laborer, +mason, +surveyor, +welder, !framer, !glazier, !plasterer, !roofer, !tiler

### CIRCUS JOBS  `circus_and_fair_jobs`
- правило: Jobs held by performers and workers at a circus or fair
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~magician, ~ringmaster, +acrobat, +animal trainer, +barker, +clown, +fire eater, +juggler, +tightrope walker, +trapeze artist, !contortionist, !stilt walker

### CREATIVE JOBS  `creative_jobs`
- правило: Jobs held by people who make art or entertainment
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~designer, ~director, ~editor, +actor, +animator, +artist, +choreographer, +composer, +dancer, +illustrator, +musician, +painter, +photographer, +poet, +producer, +sculptor, +singer, +writer

### EMERGENCY JOBS  `emergency_jobs`
- правило: Jobs held by people who respond to emergencies
- тип связи: `is_a`, базовая сложность 0.2
- слов: 14
- ~Ranger, ~rescuer, +coast guard, +deputy, +dispatcher, +EMT, +firefighter, +first responder, +lifeguard, +medic, +paramedic, +police officer, +sheriff, +trooper

### LEADERSHIP TITLES  `famous_job_titles`
- правило: Titles held by people in charge of an organization
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~captain, ~coach, ~dean, ~foreman, ~principal, +boss, +chairman, +chief, +commander, +director, +head (head_leader), +manager, +mayor, +president, +supervisor, +warden

### FARM JOBS  `farm_jobs`
- правило: Jobs held by people who work on farms and with animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~beekeeper, ~groom (groom_horse), ~hand (hand_worker), ~harvester, ~picker, ~shepherd, ~trainer, ~vet, +breeder, +dairy farmer, +farmer, +herder, +rancher, !milker

### GOVERNMENT JOBS  `government_jobs`
- правило: Jobs held by people who work for a government
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~clerk, ~inspector, ~secretary (secretary_minister), +ambassador, +auditor, +commissioner, +councilman, +delegate, +diplomat, +governor, +mayor, +official, +president, +senator, +treasurer

### BYGONE JOBS  `historic_jobs`
- правило: Jobs that were common in the past but are rare today
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- !blacksmith, !chimney sweep, !cobbler, !cooper, !ferryman, !lamplighter, !milkman, !miller, !scribe, !switchboard operator, !tanner, !telegraph operator, !town crier, !weaver, !wheelwright

### UNIFORMED JOBS  `jobs_that_wear_uniforms`
- правило: Jobs where a uniform is normally worn to work
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~chef, ~firefighter, ~flight attendant, ~mailman, ~nurse, ~pilot, ~police officer, ~sailor, ~soldier, ~waiter, !bus driver, !doorman, !paramedic, !referee, !security guard, !usher

### JOBS WITH ANIMALS  `jobs_with_animals`
- правило: Jobs held by people who work with animals
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~beekeeper, ~farmer, ~jockey, ~vet, +breeder, +dog walker, +falconer, +handler, +marine biologist, +rancher, +shepherd, +trainer, +Wrangler, !groomer, !zookeeper

### JOBS WITH TOOLS  `jobs_with_tools`
- правило: Jobs where hand tools are used every day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~carpenter, ~dentist, ~electrician, ~mechanic, ~plumber, ~surgeon, !barber, !chef, !gardener, !jeweler, !locksmith, !machinist, !sculptor, !tailor, !welder

### KITCHEN JOBS  `kitchen_jobs`
- правило: Jobs held by people who work in a restaurant kitchen or food service
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~bartender, ~butcher, ~server, +baker, +barista, +caterer, +chef, +cook (cook_person), +dishwasher, +food runner, +host (host_person), +line cook, +pastry chef, +prep cook, +sous chef, +waiter, !busser, !sommelier

### LAW JOBS  `law_jobs`
- правило: Jobs held by people who work in the legal system
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~clerk, ~investigator, ~judge, ~mediator, +attorney, +bailiff, +court reporter, +defender, +lawyer, +magistrate, +marshal, +notary, +paralegal, +prosecutor

### MEDIA JOBS  `media_jobs`
- правило: Jobs held by people who produce news and broadcasts
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~anchor, ~host (host_presenter), ~photographer, ~producer, +blogger, +broadcaster, +cameraman, +columnist, +correspondent, +critic, +editor, +journalist, +publisher, +reporter

### MEDICAL JOBS  `medical_jobs`
- правило: Jobs held by people who treat patients or work in healthcare
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~midwife, ~optometrist, ~orderly, ~paramedic, +anesthesiologist, +cardiologist, +chiropractor, +dentist, +doctor, +hygienist, +nurse, +nutritionist, +pediatrician, +pharmacist, +psychiatrist, +radiologist, +surgeon, +therapist, +vet, !podiatrist

### MILITARY RANKS  `military_ranks`
- правило: Ranks held by members of the armed forces
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +admiral, +cadet, +captain, +colonel, +commander, +corporal, +ensign, +general, +lieutenant, +major (major_rank), +officer, +private, +seaman, +sergeant

### NIGHT SHIFT  `night_shift_jobs`
- правило: Jobs commonly worked overnight
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~doctor, ~janitor, ~nurse, !air traffic controller, !baker, !bartender, !dispatcher, !DJ, !hotel clerk, !night watchman, !police officer, !radio host, !security guard, !trucker

### OFFICE JOBS  `office_jobs`
- правило: Jobs held by people who work in an office
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~analyst, ~coordinator, ~planner, +accountant, +administrator, +assistant, +auditor, +bookkeeper, +clerk, +consultant, +manager, +receptionist, +recruiter, +secretary (secretary_office), +supervisor, +treasurer

### HELPING PROFESSIONS  `people_who_help`
- правило: Jobs whose main purpose is helping other people directly
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~firefighter, ~nurse, ~teacher, +aide, +caregiver, +chaplain, +coach, +counselor, +doctor, +interpreter, +mentor, +social worker, +therapist, +volunteer

### REPAIR JOBS  `repair_jobs`
- правило: Jobs held by people who fix broken things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~cobbler, ~tailor, +appliance repairman, +electrician, +handyman, +locksmith, +machinist, +mechanic, +plumber, +repairman, +technician, +watchmaker, +welder, !upholsterer

### SCHOOL JOBS  `school_jobs`
- правило: Jobs held by adults who work at a school
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~aide, ~counselor, ~dean, ~librarian, ~nurse, ~secretary (secretary_office), +bus driver, +coach, +crossing guard, +custodian, +janitor, +lunch lady, +principal, +professor, +registrar, +substitute, +teacher, +tutor

### SCIENCE JOBS  `science_jobs`
- правило: Jobs held by people who do scientific work
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +archaeologist, +astronomer, +biologist, +botanist, +chemist, +ecologist, +engineer, +geologist, +lab technician, +meteorologist, +paleontologist, +physicist, +researcher, +statistician, +zoologist

### SEA JOBS  `sea_jobs`
- правило: Jobs held by people who work on the water
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~pilot, +captain, +crewman, +diver, +fisherman, +lifeguard, +navigator, +oyster farmer, +sailor, !boatswain, !deckhand, !harbormaster, !shipwright, !whaler

### SPORTS JOBS  `sports_jobs`
- правило: Jobs held by people who work in professional sports
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~agent, ~manager, ~scout, ~umpire, +announcer, +athlete, +coach, +commentator, +mascot, +physio, +referee, +statistician, +trainer, !groundskeeper

### STORE JOBS  `store_jobs`
- правило: Jobs held by people who work in shops and stores
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~barber, ~manager, ~pharmacist, ~tailor, +buyer, +cashier, +clerk, +florist, +grocer, +jeweler, +salesperson, +security guard, !bagger, !greeter, !merchandiser, !stocker

### TRANSPORT JOBS  `transport_jobs`
- правило: Jobs held by people who drive, fly or pilot for a living
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~captain, ~conductor, ~courier, ~pilot, +bus driver, +chauffeur, +delivery driver, +dispatcher, +driver, +engineer, +flight attendant, +taxi driver, +trucker, !ferryman


## Тема: landmarks

### CLASSIC TV  `classic_tv_shows`
- правило: Television shows known across generations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Dallas, ~mash, ~Seinfeld, ~Simpsons, ~Star Trek, +Bonanza, +cheers (cheers_show), +Friends, +I Love Lucy, +Jeopardy, +Sesame Street, +Twilight Zone, +Wheel of Fortune, !Gunsmoke

### FAMOUS BRIDGES  `famous_bridges`
- правило: Famous bridges around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Bay Bridge, +Brooklyn, +Charles Bridge, +Chesapeake, +Golden Gate, +London Bridge, +Rialto, +Sydney Harbour, +Tower Bridge, !Mackinac, !Millau, !Ponte Vecchio

### FAMOUS MUSEUMS  `famous_museums`
- правило: Famous museums around the world
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +British Museum, +Field Museum, +Getty, +Guggenheim, +Hermitage, +Louvre, +Met, +MoMA, +Prado, +Smithsonian, !Rijksmuseum, !Uffizi

### FAMOUS AIRCRAFT  `famous_ships_planes`
- правило: Famous aircraft from history
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- ~Blackbird, +Air Force One, +Concorde, +Hindenburg, +Kitty Hawk, +Spirit of St Louis, +Spitfire, +Spruce Goose, +Zeppelin, !Enola Gay

### FAMOUS STREETS  `famous_streets`
- правило: Famous streets and avenues
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Abbey Road, +Beale Street, +Bourbon, +Bourbon Street, +Broadway, +Fifth Avenue, +Main Street, +Michigan Avenue, +Rodeo Drive, +Sunset Boulevard, +Wall Street, !Champs Elysees

### FAMOUS TOWERS  `famous_towers`
- правило: Famous towers around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Belfry, +Bell Tower, +Big Ben, +Burj Khalifa, +CN Tower, +Eiffel, +Leaning Tower, +Space Needle, +Tokyo Tower, +Willis Tower, !Minaret, !Petronas

### FAMOUS TRAINS  `famous_trains`
- правило: Famous trains and railway lines
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- +Amtrak, +Bullet Train, +Flying Scotsman, +Metro, +Orient Express, +Rocky Mountaineer, +Trans Siberian, +Union Pacific, !Eurostar, !Ghan

### TEAM NAMES  `sports_teams`
- правило: Names of long standing American sports teams
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~Cowboys, +Bears, +Braves, +Broncos, +Bulls, +Celtics, +Cubs, +Dodgers, +Eagles, +Giants, +Knicks, +Lakers, +Packers, +Rangers, +Red Sox, +Steelers, +Tigers, +Yankees

### THEME PARKS  `theme_parks`
- правило: Well known theme parks
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- +Busch Gardens, +Cedar Point, +Disney World, +Disneyland, +Epcot, +Hershey Park, +Legoland, +Sea World, +Six Flags, +Universal Studios, !Knotts Berry Farm

### UNIVERSITIES  `universities`
- правило: Well known universities
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Columbia, ~duke, +Berkeley, +Cambridge, +Cornell, +Dartmouth, +Georgetown, +Harvard, +MIT, +Notre Dame, +oxford, +Princeton, +Sorbonne, +Stanford, +Yale

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


## Тема: media

### AWARDS  `awards`
- правило: Famous prizes and awards
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +Booker, +Cannes, +Emmy, +Golden Globe, +Grammy, +Heisman, +Nobel, +Olympic medal, +Oscar, +Peabody, +Pulitzer, +Tony

### BOOK GENRES  `book_genres`
- правило: Categories used to classify books
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~atlas (atlas_book), ~cookbook, ~humor, ~memoir, ~romance, ~textbook, ~travel, +biography, +encyclopedia, +fantasy, +history, +horror, +mystery, +poetry, +science fiction, +self help, +thriller, +western

### CARTOON CHARACTERS  `cartoon_characters`
- правило: Classic cartoon characters
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~Donald, ~Pluto, ~Popeye, ~tom, ~woody, +Betty Boop, +Bugs Bunny, +Daffy, +Garfield, +Goofy, +Jerry, +Mickey, +Porky, +Scooby, +Snoopy, +Sylvester, +Yogi, !Tweety

### CLASSIC NOVELS  `classic_novels`
- правило: Classic novels widely read in school
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Call of the Wild, +Dracula, +Frankenstein, +Great Expectations, +Great Gatsby, +Gulliver, +Huckleberry Finn, +Jane Eyre, +Little Women, +Of Mice and Men, +Oliver Twist, +Robinson Crusoe, +Tom Sawyer, +Treasure Island, +Wuthering Heights

### COMIC BOOKS  `comic_words`
- правило: Words used about comic books
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~cape, ~cover, ~hero, ~series, ~villain, !artist, !graphic novel, !inker, !issue, !origin, !panel, !sidekick, !speech bubble, !strip

### DISNEY CHARACTERS  `disney_characters`
- правило: Characters from Disney animated films
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~buzz, +Aladdin, +Anna, +Ariel, +Bambi, +Belle, +Cinderella, +Dumbo, +Elsa, +Jasmine, +Moana, +Mulan, +Nemo, +Peter Pan, +Pinocchio, +Pocahontas, +Rapunzel, +Simba, +Snow White, !Tinkerbell

### FAIRY TALES  `fairy_tales`
- правило: Classic fairy tales children know
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Red Riding Hood, +Beauty and the Beast, +Cinderella, +Goldilocks, +Little Mermaid, +Pinocchio, +Rapunzel, +Sleeping Beauty, +Snow White, +Three Little Pigs, +Ugly Duckling, !Hansel and Gretel, !Jack and the Beanstalk, !Rumpelstiltskin, !Thumbelina

### FAMOUS MOVIES  `famous_movies`
- правило: Films most Americans have heard of
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~Alien, ~Ghostbusters, ~gladiator, ~Rocky, ~titanic (titanic_movie), +avatar, +Braveheart, +Casablanca, +Frozen, +Godfather, +Grease, +Jaws, +Jurassic Park, +Psycho, +Shrek, +Star Wars, +Terminator, +Wizard of Oz

### MUSIC LEGENDS  `famous_musicians`
- правило: Musicians widely known across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~cash, ~Chopin, +Armstrong, +Bach, +Beatles, +Beethoven, +Dylan, +Ellington, +Elvis, +Gershwin, +Hendrix, +Mozart, +Presley, +Sinatra

### GAME SHOWS  `game_shows`
- правило: Things found on a television game show
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~audience, ~board (board_game), ~buzzer, ~category, ~podium, ~question, ~round (round_stage), ~spin, ~wheel, +contestant, +host (host_presenter), +jackpot, +lifeline, +prize, +trophy

### MAGAZINE TYPES  `magazines`
- правило: Kinds of magazine sold at a newsstand
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~business, ~comic, ~cooking, ~fashion, ~gardening, ~gossip, ~hobby, ~news, ~parenting, ~science, ~sports, ~tabloid, ~teen, ~trade, ~travel

### FILM CREW  `movie_roles`
- правило: Jobs in the crew of a film production
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~composer, ~editor, ~extra, +actor, +cameraman, +casting director, +costume designer, +director, +gaffer, +makeup artist, +producer, +screenwriter, +set designer, +sound engineer, +stunt double

### NEWSPAPER PARTS  `newspaper_parts`
- правило: Sections and parts of a newspaper
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~byline, ~crossword, ~letters, ~review, ~sports, ~weather, +advice, +classifieds, +column, +comics, +editorial, +front page, +headline, +horoscope, +obituary

### NURSERY RHYMES  `nursery_rhymes`
- правило: Nursery rhymes American children learn
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +Baa Baa Black Sheep, +Jack and Jill, +Little Bo Peep, +London Bridge, +Mary Had a Little Lamb, +Old MacDonald, +Row Your Boat, +Three Blind Mice, +Twinkle Twinkle, !Hickory Dickory Dock, !Humpty Dumpty, !Itsy Bitsy Spider

### RADIO WORDS  `radio_words`
- правило: Things and roles in radio broadcasting
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~dial, ~host (host_presenter), ~jingle, ~static, ~station (station_place), ~studio, +antenna, +broadcast, +call sign, +DJ, +frequency, +playlist, +transmitter, +tuner, !airwave

### SHAKESPEARE PLAYS  `shakespeare_plays`
- правило: Plays written by Shakespeare
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +As You Like It, +Hamlet, +Julius Caesar, +King Lear, +Macbeth, +Merchant of Venice, +Midsummer Night, +Much Ado, +othello, +Richard III, +Romeo and Juliet, +Taming of the Shrew, +Tempest, +Twelfth Night

### SUPERHEROES  `superheroes`
- правило: Comic book superheroes most people can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~flash, ~Hulk, ~robin, ~storm, +Ant Man, +Aquaman, +Batman, +Black Widow, +Captain America, +Daredevil, +Green Lantern, +Iron Man, +Spiderman, +Supergirl, +Superman, +Thor, +wolverine, +Wonder Woman

### TV GENRES  `tv_genres`
- правило: Kinds of television program
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~news, ~sports, +cartoon, +cooking show, +crime show, +documentary, +drama, +game show, +mini series, +reality, +sitcom, +soap opera, +talent show, +talk show, +variety show


## Тема: names

### BIBLICAL NAMES  `biblical_names`
- правило: First names that come from the Bible
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~Adam, ~Eve, ~John, ~mark, ~Matthew, ~Noah, +Aaron, +Daniel, +Elijah, +Esther, +Isaiah, +Luke, +Naomi, +Rachel, +Rebecca, +Ruth, +Samuel, +Sarah, +Simon, +Timothy

### COMMON SURNAMES  `common_surnames`
- правило: Family names common in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~Brown, ~hall, ~Robinson, ~Thomas, ~Wilson, +Anderson, +Clark, +Davis, +Garcia, +Harris, +Jackson, +Johnson, +Jones, +Lewis, +Martin, +Martinez, +miller, +Moore, +Smith, +Taylor, +Thompson, +walker, +white (white_surname), +Williams, +Young

### NAME PARTS  `initials_and_titles`
- правило: Parts that make up a person full name
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~initial, ~junior, ~senior, ~title, +first name, +given name, +last name, +maiden name, +middle name, +nickname, +suffix, +surname

### NATURE NAMES  `nature_names`
- правило: First names taken from nature words
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~amber, ~Aspen, ~Autumn, ~Fern, ~Ivy, ~rain, ~river, ~sage (sage_name), ~sky, ~summer, ~Willow, +Daisy, +Hazel, +Heather, +Jasmine, +Lily, +rose, +Violet

### NAME SHORTENINGS  `nicknames_for_names`
- правило: Short forms people use instead of a full first name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- ~bob, ~Jim, ~rich, ~tom, +Beth, +Cal, +Dan, +Fran, +Gus, +Hal, +Lou, +Meg, +Nan, +Nate, +Pete, +Sue, +Ted, +Vic

### VINTAGE NAMES  `old_fashioned_names`
- правило: First names that sound old fashioned today
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +Agnes, +Beatrice, +Cecil, +Clarence, +Dorothy, +Edna, +Ethel, +Eugene, +Florence, +Gertrude, +Harold, +Herbert, +Horace, +Mabel, +Mildred, +Norman, +Walter, +Wilbur

### PET NAMES  `pet_names`
- правило: Names people commonly give to pets
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~Buddy, ~Charlie, ~Daisy, ~ginger (ginger_name), ~Lucy, ~Max, ~mittens, ~peanut, ~Rocky, ~Shadow, ~tiger, +Bailey, +Bella, +Coco, +Fluffy, +Molly, +Oreo, +Rex, +Sparky, +Whiskers

### PLACE NAMES  `place_names_as_names`
- правило: First names that are also place names
- тип связи: `is_a`, базовая сложность 0.45
- слов: 16
- ~Kenya, ~Savannah, !Aspen, !Austin, !Brooklyn, !Cheyenne, !Dakota, !Devon, !Georgia, !Israel, !Jordan, !Madison, !Paris, !phoenix (phoenix_city), !Sydney, !Trenton

### ROYAL NAMES  `royal_names`
- правило: First names traditionally used by kings and queens
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Alexander, ~Charles, ~Henry, ~Louis, ~Mary, +Anne, +Catherine, +Edward, +Elizabeth, +George, +James, +Margaret, +Philip, +Richard, +Victoria, +William

### SHORT NAMES  `short_names`
- правило: First names with only one syllable
- тип связи: `has_property`, базовая сложность 0.4
- слов: 20
- ~dean, ~Faith, ~George, ~Grace, ~Hope, ~jack (jack_name), ~James, ~Jane, ~John, ~Joyce, !Ann, !Blake, !Bruce, !Claire, !Kate, !Luke, !mark, !Paul, !rose, !Scott


## Тема: nature_more

### BIOMES  `biomes`
- правило: Major natural regions of the earth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~desert, ~mountain, ~ocean, ~rainforest, ~reef, ~steppe, ~taiga, ~tundra, +chaparral, +grassland, +marsh, +prairie, +savanna, +wetland

### CANYONS AND VALLEYS  `canyons_and_valleys`
- правило: Famous canyons and valleys
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- +Antelope Canyon, +Bryce Canyon, +Copper Canyon, +Death Valley, +Grand Canyon, +Napa Valley, +Rift Valley, +Silicon Valley, +Yosemite Valley, +Zion

### CAVE THINGS  `cave_things`
- правило: Things found inside a cave
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bat, ~chamber, ~column, ~crystal, ~drip (drip_water), ~fossil, ~moss, ~pool, ~stalagmite, ~tunnel, +cavern, +darkness, +Echo, !stalactite

### EROSION WORDS  `erosion_words`
- правило: Ways water shapes the land over time
- тип связи: `does_action`, базовая сложность 0.45
- слов: 13
- ~canyon, ~delta (delta_river), ~erosion, ~flood, ~gully, ~meander, !carve, !deposit, !runoff, !sediment, !silt, !undercut, !weathering

### KINDS OF FOREST  `forest_types`
- правило: Kinds of forest and woodland
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~grove, ~jungle, ~rainforest, ~thicket, !boreal, !cloud forest, !deciduous, !mangrove, !old growth, !pine forest, !taiga, !woodland

### NATIONAL PARKS  `national_parks_us`
- правило: American national parks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~glacier, ~Olympic, ~redwood, ~sequoia, ~Yellowstone, +Acadia, +Arches, +Badlands, +Denali, +Everglades, +Grand Canyon, +Joshua Tree, +Shenandoah, +Yosemite, +Zion

### NIGHT SKY  `night_sky_things`
- правило: Things visible in the night sky
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~aurora, ~cloud, ~eclipse, ~plane (plane_aircraft), +comet, +constellation, +galaxy, +meteor, +Milky Way, +moon, +planet, +satellite, +shooting star, +star

### ROCK FORMATIONS  `rock_formations`
- правило: Natural rock shapes and formations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~arch (arch_structure), ~boulder, ~cave, ~cliff, ~spire, ~stack (stack_pile), ~terrace, +butte, +hoodoo, +mesa, +monolith, +outcrop, +pillar, +sinkhole

### FALL THINGS  `seasons_fall`
- правило: Things associated with autumn
- тип связи: `found_in`, базовая сложность 0.25
- слов: 14
- ~harvest, ~pumpkin, ~scarecrow, ~squash (squash_vegetable), ~sweater, +acorn, +apple cider, +bonfire, +chestnut, +foliage, +leaf, +rake, !cornstalk, !hayride

### SPRING THINGS  `seasons_spring`
- правило: Things associated with spring
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~bee, ~chick, ~kite (kite_toy), ~lamb, ~mud, ~puddle, ~rain, ~rainbow, ~robin, ~sprout, +blossom, +bud, +nest, +pollen, +tulip, +umbrella

### SUMMER THINGS  `seasons_summer`
- правило: Things associated with summer
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- ~barbecue, ~firefly, ~lemonade, ~pool, ~Popsicle, ~sprinkler, ~surfboard, ~watermelon, +beach, +camp, +fan (fan_device), +hammock, +sandals, +sunburn, +sunscreen, +vacation

### WINTER THINGS  `seasons_winter`
- правило: Things associated with winter
- тип связи: `found_in`, базовая сложность 0.25
- слов: 15
- ~boot (boot_shoe), ~icicle, ~mitten, ~shovel, +blanket, +blizzard, +fireplace, +frost, +hot cocoa, +scarf, +skate, +ski, +sled, +snow, +snowman

### MOON PHASES  `tide_and_moon`
- правило: Phases and states of the moon
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~quarter (quarter_fourth), +blue moon, +crescent, +eclipse, +full moon, +half moon, +harvest moon, +new moon, +waning, +waxing, !gibbous, !supermoon

### VOLCANOES  `volcanoes`
- правило: Famous volcanoes
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Etna, +Fuji, +Rainier, +St Helens, +Vesuvius, !Cotopaxi, !Kilauea, !Krakatoa, !Mauna Loa, !Pinatubo, !Popocatepetl, !Stromboli

### WATERFALLS  `waterfalls`
- правило: Famous waterfalls
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~Victoria, +Angel Falls, +Niagara, +Sutherland, +Yosemite Falls, !Havasu, !Iguazu, !Multnomah, !Shoshone, xGullfoss

### WIND WORDS  `wind_words`
- правило: Words for kinds and strengths of wind
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~whirlwind, +breeze, +chinook, +draft (draft_wind), +gale, +gust, +jet stream, +squall, +trade wind, +zephyr, !crosswind, !downdraft, !headwind, !tailwind

### LAKES  `world_lakes`
- правило: Well known lakes of the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Erie, ~Michigan, ~Superior, ~Victoria, +Como, +Crater Lake, +Geneva, +Great Salt Lake, +Huron, +Loch Ness, +Ontario, +Tahoe, !Baikal, !Titicaca


## Тема: ocean

### CORAL REEF  `coral_reef`
- правило: Things found on a coral reef
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~algae, ~eel, ~sponge (sponge_animal), ~turtle, ~urchin, +anemone, +coral, +grouper, +jellyfish, +reef shark, +seahorse, +starfish, !angelfish, !clownfish, !parrotfish

### DEEP SEA  `deep_sea`
- правило: Things found in the deep ocean
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~pressure, ~submarine, ~trench, ~vent, !abyss, !anglerfish, !darkness, !lantern fish, !sediment, !squid, !tube worm, !viperfish, !whale fall

### DIVING GEAR  `diving_gear`
- правило: Equipment used for scuba diving and snorkeling
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~buoy, ~compass, ~fins, ~flashlight, ~gauge, ~gloves, ~hood (hood_garment), ~mask, ~tank (tank_container), +dive knife, +regulator, +snorkel, +weight belt, +wetsuit

### FISH  `fish_species`
- правило: Kinds of fish an average person can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~halibut, ~marlin, +anchovy, +bass (bass_fish), +carp, +catfish, +cod, +flounder, +goldfish, +grouper, +herring, +mackerel, +minnow, +perch, +pike, +salmon, +sardine, +snapper, +sturgeon, +swordfish, +tilapia, +trout, +tuna, +walleye, !guppy

### HARBOR THINGS  `harbor_things`
- правило: Things found in a harbor or marina
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~buoy, ~crane, ~net, ~ramp, ~rope, ~tugboat, ~warehouse, +anchor, +boat, +breakwater, +dock, +jetty, +Lighthouse, +mooring, +pier, +wharf

### NAVIGATION TOOLS  `navigation_tools`
- правило: Tools used to find the way at sea
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~buoy, ~compass, ~Lighthouse, ~log, ~radar, ~sonar, ~star, ~telescope, +beacon, +chart, +gps, +map, !astrolabe, !sextant

### SEA HARVEST  `ocean_products`
- правило: Useful things people harvest from the sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~amber, ~coral, ~fish, ~kelp, ~pearl, ~salt, ~sand, ~seaweed, ~shell, ~sponge (sponge_animal), !ambergris, !oil (oil_crude), !plankton

### SHORE FEATURES  `ocean_zones`
- правило: Features of the ocean and its shoreline
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~cliff, ~gulf, ~trench, +atoll, +bay, +cove, +current (current_water), +estuary, +inlet, +lagoon, +reef, +shore, +surf, +tide, +wave (wave_water), !sandbar, !shelf (shelf_sea), !undertow

### SEA MAMMALS  `sea_mammals`
- правило: Mammals that live in the sea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~manatee, ~sea lion, +beluga, +blue whale, +dolphin, +humpback, +orca, +otter, +porpoise, +seal (seal_animal), +walrus, +whale, !dugong, !narwhal

### SEA LEGENDS  `sea_myths`
- правило: Creatures and stories from sea legend
- тип связи: `found_in`, базовая сложность 0.4
- слов: 11
- ~mermaid, ~siren, ~Whirlpool, !davy jones, !flying dutchman, !ghost ship, !kraken, !leviathan, !sea monster, !sea serpent, !triton

### SEA CONDITIONS  `sea_weather`
- правило: Words describing conditions at sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~breaker, ~calm (calm_sea), ~current (current_water), ~fog, ~gale, ~spray, ~swell, ~tide, !chop, !choppy, !doldrums, !rough, !squall, !whitecap

### SEABIRDS  `seabirds`
- правило: Birds that live along the coast or at sea
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +albatross, +booby, +heron, +osprey, +pelican, +puffin, +seagull, +tern, !cormorant, !gannet, !petrel, !sandpiper, !skua, xfrigatebird

### SHARKS AND RAYS  `sharks_and_rays`
- правило: Kinds of shark and ray
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +bull shark, +great white, +hammerhead, +mako, +manta ray, +nurse shark, +reef shark, +stingray, +tiger shark, +whale shark, !sawfish, !thresher

### SHELLFISH  `shellfish`
- правило: Sea animals with a shell that people eat
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~cockle, ~snail, +abalone, +barnacle, +clam, +crab, +crawfish, +lobster, +mussel, +oyster, +prawn, +scallop, +shrimp, !whelk

### SEASHELLS  `shells`
- правило: Kinds of seashell found on a beach
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~clam, ~cockle, ~conch, ~mussel, ~oyster, ~scallop, !abalone, !auger, !cowrie, !nautilus, !olive shell, !sand dollar, !whelk

### FISHING FLEET  `whaling_and_fishing`
- правило: Things used in commercial fishing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~crate, ~harpoon, ~hook (hook_fishing), ~line (line_cord), ~net, ~trap, !buoy, !dredge, !gaff, !hold, !pot, !Seine, !trawler, !winch


## Тема: skills

### CARD TRICKS  `card_tricks`
- правило: Terms used in performing card tricks
- тип связи: `found_in`, базовая сложность 0.5
- слов: 12
- ~control, ~force, !cut, !double lift, !false shuffle, !flourish, !palm, !pass, !reveal, !shuffle (shuffle_cards), !sleight, !spread

### COCKTAILS  `cocktails`
- правило: Named mixed drinks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +bloody mary, +cosmopolitan, +mai tai, +manhattan, +margarita, +martini, +mimosa, +mojito, +moscow mule, +old fashioned, +sangria, +tom collins, +whiskey sour, !daiquiri, !negroni, !pina colada

### DANCE MOVES  `dance_moves`
- правило: Named dance moves
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~floss, ~jump, ~kick, ~robot, ~shuffle (shuffle_dance), ~slide, ~split, +dip, +hustle, +spin, +tap (tap_dance), +turn, +twist, !moonwalk, !wave (wave_dance)

### DRIVING SKILLS  `driving_skills`
- правило: Skills tested on a driving exam
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- +backing up, +hill start, +lane change, +merging, +mirror check, +parallel parking, +signaling, +stopping, +three point turn, +u turn, +yielding

### AID ACTIONS  `first_aid_actions`
- правило: Actions taken when giving first aid
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~bandage, ~call, ~cool, ~cover, ~CPR, ~elevate, ~ice, ~monitor (monitor_medical), ~rinse, ~splint, +check pulse, +compress, +disinfect, !immobilize

### JUGGLING WORDS  `juggling_words`
- правило: Words used in juggling
- тип связи: `found_in`, базовая сложность 0.5
- слов: 13
- ~ball (ball_sphere), ~cascade, ~catch, ~club, ~drop, ~scarf, ~shower, ~throw, ~toss, !diabolo, !flash, !pattern, !ring

### KITCHEN SKILLS  `kitchen_skills`
- правило: Practical skills used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~measuring, ~timing, +chopping, +folding, +plating, +seasoning, +sharpening, +tempering, !basting, !filleting, !garnishing, !kneading, !portioning, !whisking

### KNOTS  `knots`
- правило: Named knots tied in rope
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- !bowline, !clove hitch, !figure eight, !fisherman knot, !granny knot, !half hitch, !overhand, !sheet bend, !slip knot, !square knot, !taut line, !timber hitch, !trucker hitch

### PIZZA STYLES  `pizza_styles`
- правило: Regional styles of pizza
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~California, ~new york, ~tavern, +chicago deep dish, +Detroit, +neapolitan, +sicilian, +stuffed crust, +thin crust, !calzone, !flatbread, !focaccia

### POKER HANDS  `poker_hands`
- правило: Hands that can be dealt in poker
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~flush, ~pair, ~straight, +four of a kind, +full house, +high card, +royal flush, +straight flush, +three of a kind, +two pair

### SELF DEFENSE  `self_defense_moves`
- правило: Basic self defense moves
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~elbow, ~kick, ~knee, ~roll (roll_turn), ~stance, ~stomp, ~strike (strike_hit), ~throw, !block (block_stop), !escape, !grab release, !palm strike

### SURVIVAL SKILLS  `survival_skills`
- правило: Skills used to survive outdoors
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~fishing, +fire starting, +first aid, +foraging, +knot tying, +navigation, +shelter building, +signaling, +tracking, +trapping, +water purification, !orienteering

### SWIMMING SKILLS  `swimming_skills`
- правило: Skills learned in swimming lessons
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~jumping, ~rescue, ~stroke (stroke_swim), ~turning, +backstroke, +bobbing, +breathing, +diving, +floating, +gliding, +kicking, +treading

### OFFICE SKILLS  `typing_and_office_skills`
- правило: Practical skills useful in an office job
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~filing, ~typing, +answering phones, +budgeting, +data entry, +emailing, +note taking, +organizing, +presenting, +proofreading, +scheduling, +spreadsheets

### YOGA POSES  `yoga_poses`
- правило: Named poses used in yoga
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~boat, ~crow, ~pigeon, ~plank, ~tree, !bridge (bridge_move), !child, !cobra, !downward dog, !half moon, !lotus, !mountain, !triangle, !warrior


## Тема: world_food

### COFFEE DRINKS  `coffee_drinks`
- правило: Ways coffee is prepared and served
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~drip (drip_coffee), +americano, +cappuccino, +cold brew, +espresso, +flat white, +french press, +iced coffee, +latte, +mocha, !cortado, !frappe, !macchiato, xaffogato

### CURED MEATS  `cured_meats`
- правило: Meats preserved by curing or smoking
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~jerky, ~pastrami, +bacon, +bologna, +chorizo, +corned beef, +ham, +pepperoni, +prosciutto, +salami, +sausage, !mortadella, xbresaola, xcapicola

### PICKLED FOODS  `fermented_foods`
- правило: Foods preserved by pickling or fermenting
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~cheese, ~olive, ~pickle, ~relish, ~salami, ~sauerkraut, ~vinegar, ~yogurt, !kefir, !kimchi, !kombucha, !miso, !sourdough, !tempeh

### FRENCH DISHES  `french_dishes`
- правило: Dishes from French cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~crepe, ~escargot, ~mousse, ~quiche, +baguette, +brioche, +croissant, +foie gras, +madeleine, +ratatouille, !bouillabaisse, !cassoulet, !coq au vin, !eclair, !gratin, !macaron, !souffle, !tartare

### GERMAN DISHES  `german_dishes`
- правило: Dishes from German cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~bratwurst, ~lager, ~pretzel, ~sausage, ~schnitzel, +dumpling, +potato salad, +rye bread, +sauerkraut, !kuchen, !spaetzle, !stollen, !strudel, !wurst

### GREEK DISHES  `greek_dishes`
- правило: Dishes from Greek cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~calamari, ~hummus, ~olive, +feta, +gyro, +pita, !baklava, !dolma, !halloumi, !moussaka, !ouzo, !souvlaki, !spanakopita, !tzatziki, xtaramasalata

### INDIAN DISHES  `indian_dishes`
- правило: Dishes from Indian cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +chutney, +curry, +dal, +masala, +naan, +papadum, +roti, +tikka, !biryani, !korma, !lassi, !paneer, !raita, !samosa, !tandoori, !vindaloo

### JAPANESE DISHES  `japanese_dishes`
- правило: Dishes from Japanese cuisine
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~ramen, +bento, +miso, +sashimi, +sushi, +teriyaki, +tofu, +wasabi, !edamame, !gyoza, !katsu, !mochi, !soba, !tempura, !udon, !yakitori

### MIDDLE EASTERN  `middle_eastern_dishes`
- правило: Dishes from Middle Eastern cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +couscous, +falafel, +hummus, +kebab, +lentil soup, +pita, !dolma, !halva, !shawarma, !tabbouleh, !tahini, xbaba ganoush, xfattoush, xlabneh

### SNACK NUTS  `nuts_world`
- правило: Nuts sold as snacks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +almond, +brazil nut, +cashew, +chestnut, +hazelnut, +macadamia, +peanut, +pecan, +pine nut, +pistachio, +walnut, !filbert

### SAUCES  `sauces`
- правило: Sauces used in cooking
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~hollandaise, ~pesto, ~ranch, ~salsa, ~tartar, ~vinaigrette, +alfredo, +barbecue, +curry, +gravy, +marinade, +marinara, +roux, +soy, +teriyaki, !aioli, !bechamel, !chimichurri

### SOUPS AND STEWS  `soups`
- правило: Kinds of soup and stew
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~lentil, ~tomato, +bouillon, +broth, +chicken noodle, +chili (chili_dish), +chowder, +gumbo, +miso, +onion soup, +pho, +ramen, +split pea, +stew, !bisque, !borscht, !consomme, !gazpacho, !goulash, !minestrone

### SOUTHERN FOOD  `southern_dishes`
- правило: Dishes from the American South
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~biscuit, ~catfish, ~cobbler, ~cornbread, ~fried chicken, ~gravy, +black eyed peas, +collard greens, +grits, +gumbo, +hush puppy, +okra, +pecan pie, +pulled pork, +sweet tea, !jambalaya

### SPANISH DISHES  `spanish_dishes`
- правило: Dishes from Spanish cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~flan, ~tortilla, +chorizo, +croqueta, +escalivada, +paella, +sangria, +tapas, !churro, !empanada, !gazpacho, !jamon, !manchego, xpatatas bravas

### STREET FOOD  `street_food`
- правило: Foods sold from street carts and stands
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~cotton candy, ~falafel, ~hot dog, ~taco, +corn dog, +crepe, +dumpling, +gyro, +kebab, +popcorn, +pretzel, +roasted nuts, +waffle, !arepa, !churro, !elote

### TEAS  `teas`
- правило: Kinds of tea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~black, ~ginger (ginger_spice), ~lemon, ~white (white_food), +chai, +chamomile, +darjeeling, +earl grey, +green (green_unripe), +herbal, +hibiscus, +Jasmine, +matcha, +mint (mint_herb), !oolong, !rooibos

### WINE & BEER  `wines_and_drinks`
- правило: Kinds of wine and beer
- тип связи: `is_a`, базовая сложность 0.35
- слов: 17
- ~champagne, ~rose, +ale, +Cabernet, +Chardonnay, +cider, +ipa, +lager, +Merlot, +pinot, +porter, +prosecco, +Riesling, +sangria, +stout, !pilsner, !Zinfandel

### WORLD BREADS  `world_breads`
- правило: Breads from cuisines around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~tortilla, +baguette, +brioche, +naan, +pita, +roti, +rye, +sourdough, !arepa, !challah, !ciabatta, !focaccia, !injera, !lavash, !matzo, !pumpernickel

