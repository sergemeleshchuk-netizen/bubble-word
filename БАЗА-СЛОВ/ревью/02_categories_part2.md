# Категории, часть 2 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

### WILD CATTLE  `wild_cattle`
- правило: A large hoofed animal of the cattle family
- тип связи: `is_a`, базовая сложность 0.5
- слов: 6
- +angus, +bison, +buffalo, +ox, +yak, +zebu

### WORMS  `worms_and_crawlers`
- правило: Long soft bodied crawlers commonly called worms in English
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~earthworm, ~leech, ~nightcrawler, ~silkworm, ~tapeworm, !flatworm, !glowworm, !inchworm, !roundworm, xbloodworm


## Тема: body

### BODY MOVEMENTS  `body_movements`
- правило: Movements the human body makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- +bend, +blink, +breathe, +clap, +cough, +crouch, +jump, +kick, +lean, +nod, +shiver, +shrug, +sneeze, +stretch, +twist, +wave (wave_hand), +wink, +yawn, !point (point_gesture), !swallow (swallow_throat)

### BODY PARTS  `body_parts`
- правило: External parts of the human body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 27
- ~calf (calf_leg), +ankle, +arm, +back, +chest (chest_body), +chin, +ear, +elbow, +eye, +finger, +foot (foot_body), +forehead, +hand (hand_body), +head (head_body), +heel, +hip, +jaw, +knee, +leg, +neck, +shin, +shoulder (shoulder_body), +stomach, +thigh, +toe, +waist, +wrist

### BODY SOUNDS  `body_sounds`
- правило: Sounds the human body makes on its own
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~sniffle, ~wheeze, +burp, +cough, +cry, +gasp, +growl, +grunt, +gulp, +hiccup, +laugh, +sigh, +sneeze, +snore, +whistle, +yawn

### BODY SYSTEMS  `body_systems`
- правило: Systems that make up the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~circulatory, ~digestive, ~endocrine, ~immune, ~lymphatic, ~muscular, ~nervous, ~respiratory, ~skeletal, ~urinary

### BONES  `bones`
- правило: Bones of the human skeleton
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- ~breastbone, ~digits, ~tailbone, +ankle bone, +collarbone, +femur, +hip bone, +jawbone, +kneecap, +pelvis, +rib, +shin bone, +shoulder blade, +skull, +spine, +vertebra, +wrist bone

### BREATHING  `breathing`
- правило: An act or substance belonging to breathing
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 6
- +breathe, +exhale, +gasp, +inhale, +oxygen, +sigh

### DENTIST THINGS  `dentist_things`
- правило: Things found at a dentist office
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~crown (crown_dental), +bib, +brace, +cavity, +chair, +drill (drill_tool), +filling, +floss, +mirror, +plaque, +retainer, +rinse, +suction, +toothbrush, +X-ray, !mold (mold_form)

### EXERCISE WORDS  `exercise_words`
- правило: Movements done as physical exercise
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~burpee, ~press (press_push), ~pullup, ~pushup, +crunch (crunch_exercise), +curl, +dip, +jog, +jumping jack, +lunge, +plank, +row, +sprint, +squat, +stretch, ?situp

### FACE PARTS  `face_parts`
- правило: Parts of the human face
- тип связи: `part_of`, базовая сложность 0.12
- слов: 20
- +brow, +cheek, +chin, +dimple, +ear, +eye, +eyebrow, +eyelash, +eyelid, +forehead, +freckle, +iris, +jaw, +lash, +lip, +mouth (mouth_face), +nose, +nostril, +pupil, +temple (temple_head)

### DIGITS  `fingers_and_toes`
- правило: Names for individual fingers and toes
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~forefinger, +big toe, +digit, +index finger, +little toe, +middle finger, +pinky, +ring finger, +thumb, +toe

### HAIR WORDS  `hair_words`
- правило: Words for hairstyles and things done to hair
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~cornrow, ~dreadlock, ~pigtail, ~updo, ~wave (wave_hair), +bald, +bang, +bangs, +bob, +braid, +bun, +curl, +highlight, +layer, +mohawk, +part (part_hair), +perm, +ponytail, +trim (trim_cut), +wig

### HAND PARTS  `hand_parts`
- правило: Parts of the human hand
- тип связи: `part_of`, базовая сложность 0.3
- слов: 15
- +cuticle, +finger, +fingertip, +grip, +index finger, +joint, +knuckle, +middle finger, +nail (nail_body), +palm (palm_hand), +pinky, +ring finger, +tendon, +thumb, +wrist

### HOSPITAL THINGS  `hospital_things`
- правило: Things and places found in a hospital
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~monitor (monitor_medical), +ambulance, +bandage, +bed, +chart, +emergency room, +gown, +gurney, +IV, +oxygen mask, +scalpel, +scrubs, +stethoscope, +syringe, +waiting room, +ward, +wheelchair, +X-ray

### ILLNESSES  `illnesses`
- правило: Common illnesses an average person can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 19
- ~chickenpox, ~cold (cold_illness), +allergy, +arthritis, +asthma, +bronchitis, +diabetes, +diseases, +fever, +flu, +infection, +measles, +migraine, +mumps, +pneumonia, +rash, +sinusitis, +strep throat, +ulcer

### INTERNAL ORGANS  `internal_organs`
- правило: Organs inside the human body
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- +appendix, +artery, +bladder, +brain, +colon, +esophagus, +gallbladder, +gland, +heart (heart_organ), +intestine, +kidney, +liver, +lung, +marrow, +pancreas, +spleen, +stomach, +thyroid, +vein, +womb

### MEDICINE CABINET  `medicine_cabinet`
- правило: Things kept in a home medicine cabinet
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- ~antacid, ~lozenge, +alcohol, +aspirin, +bandage, +cotton swab, +cough syrup, +eye drops, +gauze, +ice pack, +ointment, +painkiller, +sunscreen, +thermometer, +tweezers, +vitamin

### MUSCLES  `muscles`
- правило: Muscles an average person can name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~abs, ~bicep, ~calf (calf_leg), ~core, ~forearm, ~hamstring, ~lat, ~quad, ~trap, !delt, !glute, !obliques, !pec, !tricep

### PARTS OF A BIRD  `parts_of_a_bird`
- правило: A body part belonging to a bird
- тип связи: `part_of`, базовая сложность 0.3
- слов: 6
- +beak, +crest, +feathers, +tail, +talons, +wings

### EYE PARTS  `parts_of_the_eye`
- правило: Parts of the human eye
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brow, ~cornea, ~eyelid, ~iris, ~lash, ~lens, ~optic nerve, ~pupil, ~retina, ~socket (socket_eye), ~tear duct, !white (white_color)

### THE SENSES  `senses_and_perception`
- правило: Ways the human body senses the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +balance, +hearing, +hunger, +itch, +pain, +pressure, +sight, +smell, +taste, +temperature, +thirst, +touch

### SYMPTOMS  `symptoms`
- правило: Signs that a person feels unwell
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +ache, +bruise, +chills, +congestion, +cough, +cramp, +dizziness, +fatigue, +fever, +headache, +itching, +nausea, +rash, +sneeze, +sore throat, +swelling

### BODY GROWTHS  `things_that_grow_on_you`
- правило: Things that grow naturally on the human body
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~beard, ~callus, ~eyebrow, ~eyelash, ~freckle, ~mole (mole_skin), ~mustache, ~tooth, ~wart, ~whisker, +hair, +skin, !nail (nail_body), !sideburn

### PAINFUL THINGS  `things_that_hurt`
- правило: Everyday things that cause physical pain
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~bee sting, ~blister, ~bruise, ~burn, ~cramp, ~cut, ~headache, ~paper cut, ~pinch, ~scrape, ~splinter, ~sprain, ~sunburn, ~thorn, !stubbed toe


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


## Тема: culture

### BIRTHDAY PARTY  `birthday_party`
- правило: Something you associate with a birthday party
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 6
- +balloon, +candles, +confetti, +gift, +streamers, +wish

### CLASSIC GAMES  `card_and_dice_games`
- правило: Classic games played for generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~charades, ~hopscotch, ~horseshoes, +badminton, +checkers, +chess, +croquet, +dominoes, +hide and seek, +jacks, +jump rope, +marbles, +tag (tag_game), !tiddlywinks

### EASTER  `easter`
- правило: Something you associate with Easter
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +basket, +bunny, +chick, +eggs, +hunt, +lamb, +spring (spring_season)

### FAIRY TALE  `fairy_tale`
- правило: A character or object out of a fairy tale
- тип связи: `found_in`, базовая сложность 0.5
- слов: 5
- ~beanstalk, +gingerbread, +gnome, +godmother, +troll

### WORLD FESTIVALS  `festivals`
- правило: Festivals celebrated around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~St Patricks Day, +Bastille Day, +Carnival, +Cinco de Mayo, +Day of the Dead, +Diwali, +Holi, +Lunar New Year, +Mardi Gras, +Oktoberfest, !Hogmanay, !Obon, !Songkran

### NATIONAL SYMBOLS  `flags_and_symbols`
- правило: Things used as symbols of a country
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~star (star_shape), +anthem, +bear, +crescent, +dragon, +eagle, +flag, +kangaroo, +lion, +maple leaf, +rose, +shamrock, +thistle, +tulip, !crown (crown_royal)

### GREEK LETTERS  `greek_letters`
- правило: Letters of the Greek alphabet
- тип связи: `is_a`, базовая сложность 0.35
- слов: 24
- ~omicron, ~upsilon, +alpha, +beta, +chi, +delta (delta_letter), +epsilon, +eta, +gamma, +iota, +kappa, +lambda, +mu, +nu, +Omega, +phi, +pi, +psi, +rho, +sigma, +tau, +theta, +xi, +zeta

### HAUNTED HOUSE  `haunted_house`
- правило: A word belonging to ghost stories and hauntings
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~seance, +banshee, +cobwebs, +ouija, +poltergeist

### KINDS OF HUMOR  `kinds_of_humor`
- правило: A form of humor or a way of being funny
- тип связи: `is_a`, базовая сложность 0.45
- слов: 7
- +irony, +joke, +parody, +prank, +pun, +sarcasm, +satire

### LATIN PHRASES  `latin_phrases`
- правило: Latin phrases used in everyday English
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~ad hoc, ~agenda, ~alibi, ~alma mater, ~alter ego, ~bona fide, ~et cetera, ~magnum opus, ~per capita, ~per se, ~quid pro quo, ~status quo, ~versus, ~vice versa, !carpe diem

### MANNERS WORDS  `manners`
- правило: Words used when teaching good manners
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +apologize, +chewing, +excuse me, +greeting, +listening, +may I, +patience, +please, +respect, +sharing, +sorry, +thank you, +turn taking, +waiting

### MUSEUM HALL  `museum_hall`
- правило: A display or person found in a museum hall
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- ~diorama, ~docent, +Antiquity, +archive, +display

### OPPOSITES  `opposites`
- правило: Words commonly taught as opposites
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~cold (cold_temperature), ~hot (hot_temperature), +big, +dark, +day, +down, +dry, +empty, +far, +fast, +full, +hard, +high, +in, +light (light_bright), +low, +near, +night, +open, +out, +shut, +slow, +small, +soft, +up, +wet

### PIRATE COVE  `pirate_cove`
- правило: A word from pirate tales beyond the obvious ones
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~buccaneer, ~spyglass, +marooned, +plunder

### PLAYGROUND GAMES  `playground_games`
- правило: Games children play at recess
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~hopscotch, ~kickball, +capture the flag, +dodgeball, +duck duck goose, +four square, +freeze tag, +hide and seek, +hot potato, +jump rope, +marbles, +red rover, +simon says, !tag (tag_game)

### NUMBER WORDS  `superstition_numbers`
- правило: Words for numbers and counting
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~quarter (quarter_fourth), ~score (score_twenty), +billion, +couple, +dozen, +eight, +eleven, +few, +five, +four, +half, +hundred, +million, +nine, +one, +pair, +seven, +single (single_one), +six, +ten, +thousand, +three, +twenty, +two, +zero

### TRADITIONAL CLOTHING  `traditional_clothing`
- правило: Traditional garments from world cultures
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +kilt, +kimono, +poncho, +sari, +sombrero, +toga, +turban, !dashiki, !dirndl, !hanbok, !kaftan, !kente, !lederhosen, !moccasin, !sarong

### UFO SIGHTING  `ufo_sighting`
- правило: A word belonging to stories of flying saucers
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +hovering, +martian, +roswell, +sighting

### RETRO GAMES  `video_game_classics`
- правило: Video games known across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Frogger, ~Minesweeper, +Asteroids, +centipede, +Donkey Kong, +Mario, +Pac Man, +Pinball, +Pong, +Solitaire, +Sonic, +Space Invaders, +Tetris, +Zelda, !Galaga

### MORE CURRENCIES  `world_currencies_more`
- правило: Currencies used in particular countries
- тип связи: `is_a`, базовая сложность 0.45
- слов: 18
- +baht, +dinar, +kroner, +lira, +peso, +rand, +real, +ruble, +rupee, +yen, +yuan, !dirham, !forint, !koruna, !ringgit, !riyal, !shekel, !zloty

### WORLD DANCES  `world_dances`
- правило: Traditional dances from around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bolero, +flamenco, +hula, +irish jig, +mambo, +polka, +salsa, +samba, +square dance, +tango, +waltz, !cancan, !merengue, !tarantella

### WORLD HATS  `world_hats`
- правило: Traditional headwear from world cultures
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~beret, ~bowler, ~conical hat, ~fez, ~panama, ~sombrero, ~tam, ~turban, ?tarboosh, !keffiyeh, xkufi, xushanka

### WORLD INSTRUMENTS  `world_instruments`
- правило: Musical instruments from cultures around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~koto, ~oud, ~sitar, +bagpipes, +steel drum, +ukulele, !balalaika, !bouzouki, !didgeridoo, !djembe, !erhu, !kalimba, !marimba, !shamisen, xpanpipe


## Тема: farming

### AT THE STABLES  `at_the_stables`
- правило: A piece of tack, animal or fixture found at stables
- тип связи: `found_in`, базовая сложность 0.5
- слов: 7
- ~stirrup, +bridle, +foal, +hooves, +horseshoe, +paddock, +reins

### BARN THINGS  `barn_things`
- правило: Things found inside a barn
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~gate (gate_barrier), ~sack (sack_bag), +bale, +bucket, +feed, +harness, +hay, +lantern, +loft, +milking stool, +pitchfork, +rope, +saddle, +shovel, +stall (stall_barn), +trough

### BEEKEEPER  `beekeeper`
- правило: A place, product or tool of keeping bees
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- ~apiary, +beeswax, +honeycomb, +smoker

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


## Тема: fashion

### BAGS AND CASES  `bags`
- правило: Kinds of bag people carry
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~trunk (trunk_case), +backpack, +briefcase, +clutch, +duffel, +fanny pack, +garment bag, +gym bag, +messenger bag, +pouch, +purse, +satchel, +suitcase, +tote, +wallet

### BEAUTY TOOLS  `beauty_tools`
- правило: Tools used for hair, nails and makeup
- тип связи: `used_in`, базовая сложность 0.35
- слов: 15
- ~file (file_tool), ~straightener, +applicator, +brush, +buffer, +clipper, +comb, +curler, +curling iron, +dryer, +mirror, +razor, +roller, +sponge (sponge_cleaning), +tweezers

### EYEWEAR  `eyewear`
- правило: Things worn over the eyes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~bifocals, +aviators, +blindfold, +contacts, +frames, +glasses, +goggles, +mask, +monocle, +reading glasses, +safety glasses, +shades, +sunglasses, +visor

### FACIAL CARE  `facial_care`
- правило: A product applied to the face to care for the skin
- тип связи: `used_for`, базовая сложность 0.4
- слов: 6
- +cleanser, +cream (cream_ointment), +moisturizer, +patches, +serum, +toner

### FASHION ACCESSORIES  `fashion_accessories`
- правило: Items added to complete a look
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~bowtie, ~hairband, ~tie (tie_clothing), +belt, +bracelet, +brooch, +cufflinks, +earring, +gloves, +hat, +necklace, +pocket square, +scarf, +sunglasses, +suspenders, +watch (watch_object)

### FASHION SHOW  `fashion_show`
- правило: Things found at a fashion show
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- +backstage, +camera, +collection, +designer, +fitting, +front row, +model, +outfit, +pose, +program, +rack, +runway, +seamstress, +spotlight

### FASHION STYLES  `fashion_styles`
- правило: Named styles of dressing
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +bohemian, +business casual, +casual, +classic, +formal, +gothic, +minimalist, +preppy, +punk, +retro, +sporty, +streetwear, +vintage, +western

### HAIRSTYLES  `hairstyles`
- правило: Ways of styling hair
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~chignon, ~cornrows, ~topknot, ~updo, +afro, +bangs, +beehive, +bob, +braid, +bun, +crew cut, +dreadlocks, +layers, +mohawk, +mullet, +perm, +pigtails, +pixie, +ponytail

### JEWELRY STONES  `jewelry_stones`
- правило: Stones set into jewelry
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +amethyst, +aquamarine, +diamond (diamond_gem), +emerald, +garnet, +jade, +moonstone, +onyx, +opal, +pearl, +peridot, +ruby, +sapphire, +topaz, +turquoise

### MAKEUP  `makeup`
- правило: Cosmetics applied to the face
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +blush, +bronzer, +brow pencil, +concealer, +eyeliner, +eyeshadow, +foundation (foundation_makeup), +gloss, +highlighter, +lipstick, +mascara, +powder, +primer, +setting spray

### NAIL SALON  `nail_salon`
- правило: A tool or product used in a nail salon
- тип связи: `used_in`, базовая сложность 0.55
- слов: 4
- ~topcoat, +cuticle, +lacquer, ?nailfile

### NAIL CARE  `nail_words`
- правило: Things used for manicures and nail care
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- +acrylic, +base coat, +buffer, +clipper, +cuticle, +file (file_tool), +gel, +glitter, +polish (polish_product), +pusher, +remover, +soak, +top coat, +wrap

### PATTERNS  `patterns`
- правило: Patterns printed on cloth
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~gingham, ~herringbone, ~houndstooth, +animal print, +argyle, +camouflage, +checkered, +chevron, +floral, +paisley, +plaid, +polka dot, +Stripe, +tartan, +tie dye

### FRAGRANCE WORDS  `perfume_words`
- правило: Words used to describe perfumes and scents
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~amber, ~citrus, ~Cologne, ~floral, ~fresh (fresh_scent), ~lavender (lavender_plant), ~mist, ~musk, ~sandalwood, ~spicy, ~vanilla, ~woody, +rose, +sweet, !note (note_scent)

### SELF CARE  `self_care`
- правило: A way people look after their appearance and body
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 6
- ~haircare, +manicure, +massage, +pedicure, +skincare, +spa

### GARMENT DETAILS  `sewing_patterns`
- правило: Details sewn into a garment design
- тип связи: `part_of`, базовая сложность 0.4
- слов: 15
- ~collar, ~cuff, ~dart (dart_sew), ~hem, ~lapel, ~lining, ~panel, ~pocket, ~ruffle, ~seam, ~trim (trim_edging), ~yoke, !applique, !gusset, !pleat

### SHOE STYLES  `shoe_styles`
- правило: Styles of shoe
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~loafer, ~moccasin, +boot (boot_shoe), +clog, +flat, +heel, +mule, +oxford, +platform, +pump, +sandal, +slipper, +sneaker, +stiletto, +wedge, xespadrille

### SPA DAY  `spa_day`
- правило: A treatment or fixture of a day at the spa
- тип связи: `found_in`, базовая сложность 0.55
- слов: 5
- ~loofah, +aromatherapy, +jacuzzi, +masseuse, +pampering

### WARDROBE CARE  `wardrobe_care`
- правило: Things used to store and care for clothes
- тип связи: `used_in`, базовая сложность 0.4
- слов: 13
- +brush, +cedar block, +closet, +drawer, +garment bag, +hanger, +hook (hook_fastener), +iron (iron_appliance), +lint roller, +shelf (shelf_furniture), +shoe tree, +steamer, !mothball


## Тема: history

### ANCIENT CIVILIZATIONS  `ancient_civilizations`
- правило: Civilizations of the ancient world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Phoenicia, ~Sumer, +Assyria, +Aztec, +Babylon, +Carthage, +China, +Egypt, +Greece, +Inca, +Maya, +Persia, +Rome, +Sparta, +Troy

### ANCIENT GREECE IDEAS  `ancient_greece_ideas`
- правило: An idea or institution that ancient Greece is remembered for
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 6
- +agora, +democracy, +mythology, +Olympics, +Oracle, +philosophy

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

### CASTLE KEEP  `castle_keep`
- правило: A word belonging to a castle and its defence
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- ~chainmail, ~portcullis, +battlements, +gatehouse, +rampart, +siege

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

### GOLD RUSH  `gold_rush`
- правило: A person or tool of the gold rush
- тип связи: `used_in`, базовая сложность 0.65
- слов: 4
- ~pickaxe, +panning, +prospector, +sluice

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
- слов: 18
- ~breastplate, ~chainmail, +armor, +banner, +bow (bow_weapon), +crest, +dagger, +gauntlet, +helmet, +horse, +lance, +saddle, +shield, +spear, +spur, +squire, +sword, +visor

### MEDIEVAL FAIR  `medieval_fair`
- правило: A performer or event at a medieval fair
- тип связи: `found_in`, базовая сложность 0.6
- слов: 6
- ~joust, +banquet, +bard, +falconer, +jester, +minstrel

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

### VIKINGS  `vikings`
- правило: A word belonging to the Vikings and their world
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~berserker, ~longboat, +fjord, +mead, +norse

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

### ON THE SKYLINE  `on_the_skyline`
- правило: A tall structure that stands out on a skyline
- тип связи: `is_a`, базовая сложность 0.65
- слов: 4
- +Minaret, +obelisk, +pagoda, +spire

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


## Тема: language

### RADIO ALPHABET  `alphabet_code`
- правило: Code words used to spell letters over a radio
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~alpha, ~Bravo, ~Charlie, ~delta (delta_letter), ~Echo, ~Golf, ~Hotel, ~India, ~Juliet, ~Kilo, ~Lima, ~Mike, ~November, ~Oscar, ~Papa, ~Quebec, ~Romeo, ~Sierra, ~tango, ~Victor, ~Whiskey, ~Yankee, ~Zulu, !foxtrot

### GREETING CARD  `greeting_card`
- правило: What is printed on, drawn on or sent with a greeting card
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- ~flowers, ~glitter, +envelope, +feelings, +greetings, +holidays, +stamp (stamp_postage)

### GREETINGS  `greetings_and_farewells`
- правило: Words and phrases used to greet or say goodbye
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- +aloha, +bye, +cheers (cheers_greeting), +evening, +farewell, +goodbye, +greetings, +hello, +hi, +howdy, +later, +morning, +salute, +so long, +welcome

### LANGUAGES  `languages`
- правило: Languages spoken around the world
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~polish (polish_language), +Arabic, +Chinese, +Dutch, +English, +French, +German, +greek, +Hebrew, +Hindi, +Italian, +Japanese, +Korean, +Latin, +Portuguese, +Russian, +spanish, +swahili, +Swedish, +Turkish, +Vietnamese

### PARTS OF SPEECH  `parts_of_speech`
- правило: Grammatical categories of English words
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~determiner, ~gerund, ~interjection, +adjective, +adverb, +article, +conjunction, +noun, +participle, +preposition, +pronoun, +verb

### POLITE WORDS  `polite_words`
- правило: Words used to be polite in English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +apologize, +appreciate, +excuse me, +kindly, +madam, +may, +pardon, +please, +sir, +sorry, +thanks, +welcome

### PUNCTUATION MARKS  `punctuation`
- правило: Marks used to punctuate written English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~dash (dash_mark), ~ellipsis, +apostrophe, +asterisk, +bracket, +colon, +comma, +exclamation point, +hyphen, +parenthesis, +period, +question mark, +quotation mark, +semicolon, +slash

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
- +compact, +dwarf, +little, +micro, +mini, +miniature, +minute (minute_tiny), +petite, +pint sized, +pocket, +slight, +small, +tiny, +wee

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
- ~barbecue, ~cheese, ~chili (chili_pepper), ~cranberry, ~fish, ~hot (hot_spicy), ~pizza, ~soy, ~steak, ~taco, ~tomato, ~white (white_color), +apple (apple_fruit), !duck (duck_meat), !tartar

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
- ~capital (capital_letter), +byline, +caption, +chapter, +column, +comma, +draft (draft_document), +font, +footnote, +heading, +index, +letter (letter_alphabet), +margin, +outline, +page, +paragraph, +period, +sentence (sentence_writing), +signature, +title, +word


## Тема: names

### BIBLICAL NAMES  `biblical_names`
- правило: First names that come from the Bible
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +Aaron, +Adam, +Daniel, +Elijah, +Esther, +Eve, +Isaiah, +John, +Luke, +mark, +Matthew, +Naomi, +Noah, +Rachel, +Rebecca, +Ruth, +Samuel, +Sarah, +Simon, +Timothy

### COMMON SURNAMES  `common_surnames`
- правило: Family names common in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Anderson, +Brown, +Clark, +Davis, +Garcia, +hall, +Harris, +Jackson, +Johnson, +Jones, +Lewis, +Martin, +Martinez, +miller, +Moore, +Robinson, +Smith, +Taylor, +Thomas, +Thompson, +walker, +white (white_surname), +Williams, +Wilson, +Young

### NAME PARTS  `initials_and_titles`
- правило: Parts that make up a person full name
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- +first name, +given name, +initial, +junior, +last name, +maiden name, +middle name, +nickname, +senior, +suffix, +surname, +title

### NATURE NAMES  `nature_names`
- правило: First names taken from nature words
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~sage (sage_name), +amber, +Aspen, +Autumn, +Daisy, +Fern, +Hazel, +Heather, +Ivy, +Jasmine, +Lily, +rain, +river, +rose, +sky, +summer, +Violet, +Willow

### NAME SHORTENINGS  `nicknames_for_names`
- правило: Short forms people use instead of a full first name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +Beth, +bob, +Cal, +Dan, +Fran, +Gus, +Hal, +Jim, +Lou, +Meg, +Nan, +Nate, +Pete, +rich, +Sue, +Ted, +tom, +Vic

### VINTAGE NAMES  `old_fashioned_names`
- правило: First names that sound old fashioned today
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- +Agnes, +Beatrice, +Cecil, +Clarence, +Dorothy, +Edna, +Ethel, +Eugene, +Florence, +Gertrude, +Harold, +Herbert, +Horace, +Mabel, +Mildred, +Norman, +Walter, +Wilbur

### PET NAMES  `pet_names`
- правило: Names people commonly give to pets
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~ginger (ginger_name), +Bailey, +Bella, +Buddy, +Charlie, +Coco, +Daisy, +Fluffy, +Lucy, +Max, +mittens, +Molly, +Oreo, +peanut, +Rex, +Rocky, +Shadow, +Sparky, +tiger, +Whiskers

### PLACE NAMES  `place_names_as_names`
- правило: First names that are also place names
- тип связи: `is_a`, базовая сложность 0.45
- слов: 16
- ~Aspen, ~Austin, ~Brooklyn, ~Cheyenne, ~Dakota, ~Devon, ~Georgia, ~Israel, ~Jordan, ~Kenya, ~Madison, ~Paris, ~Savannah, ~Sydney, ~Trenton, !phoenix (phoenix_city)

### ROYAL NAMES  `royal_names`
- правило: First names traditionally used by kings and queens
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +Alexander, +Anne, +Catherine, +Charles, +Edward, +Elizabeth, +George, +Henry, +James, +Louis, +Margaret, +Mary, +Philip, +Richard, +Victoria, +William

### SHORT NAMES  `short_names`
- правило: First names with only one syllable
- тип связи: `has_property`, базовая сложность 0.4
- слов: 20
- ~Ann, ~Blake, ~Bruce, ~Claire, ~dean, ~Grace, ~jack (jack_name), ~Jane, ~Joyce, ~Kate, ~Luke, +Faith, +George, +Hope, +James, +John, +mark, +Paul, +rose, +Scott


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
- +aurora, +balloon, +bird, +cloud, +comet, +eclipse, +fog, +haze, +helicopter, +kite (kite_toy), +lightning, +meteor, +moon, +plane (plane_aircraft), +rainbow, +satellite, +smoke, +star (star_space), +sun, +sunset

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
- ~begonia, ~petunia, ~zinnia, +aster, +azalea, +buttercup, +carnation, +daffodil, +dahlia, +Daisy, +geranium, +hyacinth, +iris, +Jasmine, +lavender (lavender_plant), +lilac, +Lily, +magnolia, +marigold, +orchid, +peony, +poppy, +rose, +sunflower, +tulip, +Violet, +wildflowers

### GARDEN PLANTS  `garden_plants`
- правило: Plants people grow in a home garden
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~hosta, ~lavender (lavender_plant), +basil, +bean, +carrot, +cucumber, +Fern, +Ivy, +lettuce, +marigold, +mint (mint_herb), +pepper, +pumpkin, +rose, +squash (squash_vegetable), +strawberry, +sunflower, +tomato, +tulip, +zucchini

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
- ~glowstick, ~streetlight, +bulb, +campfire, +candle, +fire, +firefly, +flashlight, +headlight, +lamp, +lantern, +laser, +lightning, +match, +moon, +neon, +screen (screen_display), +star (star_space), +sun, +torch

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


## Тема: places

### ANTIQUE SHOP  `antique_shop`
- правило: A word belonging to old objects sold as antiques
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~curio, +auction, +dusty, +heirloom

### AT THE HOTEL  `at_the_hotel`
- правило: A place or service a guest meets at a hotel
- тип связи: `found_in`, базовая сложность 0.4
- слов: 7
- +checkout, +housekeeper, +key (key_lock), +lobby, +reception, +suite, +vacancy

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

### FARMERS MARKET  `farmers_market`
- правило: Something you see at a farmers market
- тип связи: `found_in`, базовая сложность 0.5
- слов: 5
- +crate, +homegrown, +preserves, +stall (stall_market), +vendor

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
- слов: 26
- ~cabin (cabin_house), ~temple (temple_building), +apartment, +barn, +bungalow, +castle, +church, +cottage, +courthouse, +duplex, +factory, +garage, +hospital, +Hotel, +house, +library, +mall, +mansion, +museum, +school, +shed, +skyscraper, +stadium, +theater, +tower, +warehouse

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

### SUPERMARKET  `supermarket`
- правило: A fixture or worker found in a supermarket
- тип связи: `found_in`, базовая сложность 0.45
- слов: 5
- ~bagger, +aisle, +cart, +grocer, +trolley

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
- слов: 31
- +Barcelona, +Bogota, +Buenos Aires, +Cairo, +Casablanca, +Dubai, +Geneva, +Hamburg, +Istanbul, +Jakarta, +Johannesburg, +London, +Madrid, +Manchester, +Marseille, +Melbourne, +Milan, +Mumbai, +Munich, +Naples, +Osaka, +Paris, +Rio de Janeiro, +Rome, +Santiago, +Shanghai, +Sydney, +Tokyo, +Toronto, +Vancouver, +Venice

### FAMOUS MOUNTAINS  `world_mountains`
- правило: Famous individual mountains
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~Ararat, ~Matterhorn, +Alps, +Andes, +Denali, +Etna, +Everest, +Fuji, +Kilimanjaro, +Olympus, +Rainier, +Rockies, +Shasta, +Vesuvius, +Whitney, !Aconcagua, !Elbrus

### WORLD RIVERS  `world_rivers`
- правило: Major rivers outside the United States
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +Amazon, +Congo, +Danube, +Elbe, +Euphrates, +Ganges, +Loire, +Mekong, +Nile, +Po, +Rhine, +Seine, +Thames, +Tigris, +Volga, +Yangtze

### ZOO VISIT  `zoo_visit`
- правило: A person, place or activity at a zoo
- тип связи: `found_in`, базовая сложность 0.45
- слов: 4
- ~zookeeper, +enclosure, +feeding, +petting


## Тема: science

### HUMAN BIOLOGY  `body_science`
- правило: Scientific words about how the human body works
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~artery, ~blood, ~bone, ~cell (cell_body), ~dna, ~enzyme, ~gene, ~hormone, ~immunity, ~membrane, ~metabolism, ~muscle, ~nerve, ~organ (organ_body), ~oxygen, ~plasma, ~protein, ~tissue (tissue_body)

### CHEMISTRY LAB  `chemistry_lab`
- правило: A tool or method used in a chemistry lab
- тип связи: `used_in`, базовая сложность 0.65
- слов: 5
- ~bunsen, ~titration, +litmus, +reagent, +vial

### CHEMISTRY WORDS  `chemistry_words`
- правило: Words used in chemistry class
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~acid, ~atom, ~base, ~bond, ~catalyst, ~compound, ~element, ~formula, ~ion, ~isotope, ~mixture, ~molecule, ~reaction, ~salt, ~solution, ~valence

### DINOSAURS  `dinosaurs`
- правило: Dinosaur species an average person can name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~allosaurus, ~brachiosaurus, ~diplodocus, ~pterodactyl, ~spinosaurus, ~stegosaurus, ~velociraptor, +brontosaurus, +raptor, +triceratops, +tyrannosaurus, xankylosaurus

### ELECTRICITY WORDS  `electricity_words`
- правило: Words used to talk about electricity
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +amp, +battery, +charge, +circuit, +conductor, +current (current_electric), +fuse, +generator, +outlet, +plug, +resistor, +shock, +socket (socket_electric), +switch, +transformer, +voltage, +Watt, +wire

### CHEMICAL ELEMENTS  `elements`
- правило: Chemical elements an average person can name
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~mercury (mercury_metal), +argon, +calcium, +carbon (carbon_element), +chlorine, +copper, +gold, +helium, +hydrogen, +iron (iron_metal), +lead (lead_metal), +neon, +nitrogen, +oxygen, +potassium, +silver, +sodium, +sulfur, +uranium, +zinc

### ENERGY WORDS  `energy_words`
- правило: Words for kinds and sources of energy
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +battery, +biomass, +coal, +electric, +fuel, +gas, +geothermal, +hydro, +kinetic, +magnetic, +nuclear, +solar, +steam, +thermal, +wind

### DISSOLVING THINGS  `experiments`
- правило: Substances that dissolve in water
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~baking soda, ~candy, ~chalk (chalk_rock), ~coffee, ~gelatin, ~honey, ~ink, ~kool aid, ~powder, ~salt, ~soap, ~sugar, ~syrup, ~tablet

### INVENTIONS  `inventions`
- правило: Famous inventions that changed everyday life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +airplane, +battery, +camera, +compass, +computer, +elevator, +engine, +internet, +lightbulb, +microscope, +printing press, +radio, +refrigerator, +telephone, +telescope, +television, +vaccine, +wheel

### SCIENCE ACTIONS  `lab_actions`
- правило: Things a scientist does in an experiment
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- +analyze, +boil, +compare, +dilute, +dissolve, +filter, +freeze, +heat, +measure, +mix, +observe, +predict, +record, +sample, +test, +weigh

### LAB EQUIPMENT  `lab_equipment`
- правило: Equipment found in a school science laboratory
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~magnifier, ~pipette, +beaker, +burner, +centrifuge, +clamp, +dropper, +flask, +funnel, +goggles, +magnet, +microscope, +petri dish, +rack, +scale (scale_weigh), +slide, +stopper, +test tube, +thermometer, +tongs

### FORCES  `magnets_and_forces`
- правило: Physical forces studied in science class
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~buoyancy, ~drag, ~friction, ~gravity, ~inertia, ~lift, ~magnetism, ~pressure, ~pull, ~push, ~tension, ~thrust, ~torque

### MATH OPERATIONS  `math_operations`
- правило: Operations performed on numbers
- тип связи: `does_action`, базовая сложность 0.25
- слов: 15
- ~round (round_math), +add, +average, +calculate, +count, +cube, +divide, +double, +estimate, +factor, +halve, +multiply, +Square, +subtract, +sum

### MATH WORDS  `math_words`
- правило: Words used in school mathematics
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +angle, +area, +average, +decimal, +diameter, +equation, +exponent, +fraction, +integer, +percent, +perimeter, +prime, +product, +radius, +ratio, +remainder, +square root, +sum, +variable, +volume

### METALS  `metals`
- правило: Metals and metal alloys used in everyday objects
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~mercury (mercury_metal), +aluminum, +brass, +bronze, +chrome, +chromium, +cobalt, +copper, +gold, +iron (iron_metal), +lead (lead_metal), +magnesium, +nickel, +pewter, +platinum, +silver, +steel, +tin (tin_metal), +titanium, +tungsten, +zinc

### TINY THINGS  `microscope_things`
- правило: Things too small to see with the naked eye
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~atom, ~bacteria, ~cell (cell_body), ~dna, ~dust mite, ~electron, ~germ, ~microbe, ~mite, ~molecule, ~particle, ~pollen, ~spore, ~virus

### NATURAL HISTORY MUSEUM  `natural_history_museum`
- правило: What is displayed in a natural history museum case
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +bones, +diorama, +fossil, +gemstones, +insects, +minerals, +skeleton

### PLANETS  `planets`
- правило: Planets of our solar system
- тип связи: `is_a`, базовая сложность 0.2
- слов: 10
- +Earth, +Jupiter, +Mars, +mercury (mercury_planet), +Neptune, +Pluto, +Saturn, +Uranus, +Venus, xmoons

### GEOLOGY WORDS  `rock_cycle_words`
- правило: Words used to describe the earth and its rocks
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~core, ~crust, ~erosion, ~fault, ~fossil, ~glacier, ~lava, ~magma, ~mantle, ~mineral, ~plate (plate_tectonic), ~quarry, ~sediment, ~strata, ~tectonic, ~volcano

### SCIENCE FAIR  `science_fair`
- правило: What a school science fair project is about or made of
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 8
- ~metals, ~minerals, +beaker, +hypothesis, +inventions, +poster, +volcanoes, !shapes

### BRANCHES OF SCIENCE  `science_fields`
- правило: Fields of scientific study
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +anatomy, +archaeology, +astronomy, +biology, +botany, +chemistry, +ecology, +genetics, +geology, +medicine, +meteorology, +physics, +psychology, +robotics, +zoology

### SEISMOLOGY  `seismology`
- правило: A term used measuring earthquakes
- тип связи: `used_in`, базовая сложность 0.7
- слов: 4
- +aftershock, +epicenter, +magnitude, +tectonic

### SHAPES  `shapes`
- правило: Geometric shapes taught in school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 21
- ~diamond (diamond_shape), ~pyramid (pyramid_shape), +arch (arch_structure), +circle, +cone, +crescent, +cube, +cylinder, +heart (heart_shape), +hexagon, +octagon, +oval, +Pentagon, +prism, +rectangle, +rhombus, +sphere, +Square, +star (star_shape), +trapezoid, +triangle

### SPACE OBJECTS  `space_objects`
- правило: Objects found in outer space
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~quasar, ~ring (ring_circle), +asteroid, +asteroid belt, +black hole, +cluster, +comet, +constellation, +dwarf planet, +galaxy, +meteor, +meteorite, +moon (moon_space), +nebula, +planet, +pulsar, +satellite, +star (star_space), +sun, +supernova

### STATES OF MATTER  `states_of_matter`
- правило: Physical states matter can take
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~solid (solid_matter), +crystal, +foam, +gas, +ice, +liquid, +mist, +plasma, +powder, +slush, +steam, +vapor

### TEMPERATURE WORDS  `temperature_words`
- правило: Words describing how hot or cold something is
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +blazing, +boiling, +chilly, +cold (cold_temperature), +cool, +freezing, +frigid, +frosty, +hot (hot_temperature), +icy, +lukewarm, +mild, +scalding, +sweltering, +tepid, +warm

### THE MIND  `the_mind`
- правило: A faculty or activity of the thinking mind
- тип связи: `is_a`, базовая сложность 0.5
- слов: 7
- +emotion, +focus (focus_mind), +intuition, +logic, +memory, +reason, +thought

### ASTRONOMY WORDS  `things_in_the_sky_science`
- правило: Words used by astronomers
- тип связи: `found_in`, базовая сложность 0.35
- слов: 17
- +atmosphere, +comet, +constellation, +crater, +eclipse, +galaxy, +gravity, +light year, +meteor shower, +observatory, +orbit, +phase, +rotation, +satellite, +solar system, +telescope, +universe

### WEATHER SCIENCE  `weather_science`
- правило: Scientific words used to describe weather
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~updraft, +air mass, +barometer, +condensation, +dew point, +evaporation, +forecast, +front, +humidity, +jet stream, +precipitation, +pressure, +radar, !isobar

### WEIGHT UNITS  `weight_units`
- правило: A unit used to measure weight or mass
- тип связи: `is_a`, базовая сложность 0.35
- слов: 6
- +carat, +gram, +kilogram, +ounce, +pound (pound_weight), +ton


## Тема: world_food

### COFFEE DRINKS  `coffee_drinks`
- правило: Ways coffee is prepared and served
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~cortado, ~drip (drip_coffee), ~frappe, ~macchiato, +americano, +cappuccino, +cold brew, +espresso, +flat white, +french press, +iced coffee, +latte, +mocha, xaffogato

### CURED MEATS  `cured_meats`
- правило: Meats preserved by curing or smoking
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +bacon, +bologna, +chorizo, +corned beef, +ham, +jerky, +pastrami, +pepperoni, +prosciutto, +salami, +sausage, !mortadella, xbresaola, xcapicola

### PICKLED FOODS  `fermented_foods`
- правило: Foods preserved by pickling or fermenting
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~cheese, ~kimchi, ~kombucha, ~miso, ~olive, ~pickle, ~relish, ~salami, ~sauerkraut, ~sourdough, ~vinegar, ~yogurt, !kefir, !tempeh

### FRENCH DISHES  `french_dishes`
- правило: Dishes from French cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bouillabaisse, ~cassoulet, ~coq au vin, ~eclair, ~gratin, ~macaron, ~souffle, ~tartare, +baguette, +brioche, +crepe, +croissant, +escargot, +foie gras, +madeleine, +mousse, +quiche, +ratatouille

### GERMAN DISHES  `german_dishes`
- правило: Dishes from German cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~strudel, ~wurst, +bratwurst, +dumpling, +lager, +potato salad, +pretzel, +rye bread, +sauerkraut, +sausage, +schnitzel, !kuchen, !spaetzle, !stollen

### GREEK DISHES  `greek_dishes`
- правило: Dishes from Greek cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~baklava, ~halloumi, ~moussaka, ~ouzo, ~souvlaki, ~tzatziki, +calamari, +feta, +gyro, +hummus, +olive, +pita, !dolma, !spanakopita, xtaramasalata

### INDIAN DISHES  `indian_dishes`
- правило: Dishes from Indian cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~biryani, ~korma, ~lassi, ~paneer, ~raita, ~samosa, ~tandoori, ~vindaloo, +chutney, +curry, +dal, +masala, +naan, +roti, +tikka, ?papadum

### JAPANESE DISHES  `japanese_dishes`
- правило: Dishes from Japanese cuisine
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~edamame, ~gyoza, ~katsu, ~mochi, ~soba, ~tempura, ~udon, ~yakitori, +bento, +miso, +ramen, +sashimi, +sushi, +teriyaki, +tofu, +wasabi

### MIDDLE EASTERN  `middle_eastern_dishes`
- правило: Dishes from Middle Eastern cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~shawarma, ~tahini, +couscous, +falafel, +hummus, +kebab, +lentil soup, +pita, !dolma, !halva, !tabbouleh, xbaba ganoush, xfattoush, xlabneh

### SNACK NUTS  `nuts_world`
- правило: Nuts sold as snacks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~filbert, +almond, +brazil nut, +cashew, +chestnut, +hazelnut, +macadamia, +peanut, +pecan, +pine nut, +pistachio, +walnut

### SAUCES  `sauces`
- правило: Sauces used in cooking
- тип связи: `is_a`, базовая сложность 0.3
- слов: 22
- ~aioli, ~bechamel, ~chimichurri, +alfredo, +barbecue, +curry, +gravy, +hollandaise, +ketchup, +marinade, +marinara, +mayonnaise, +mustard, +pesto, +ranch, +relish, +roux, +salsa, +soy, +tartar, +teriyaki, +vinaigrette

### SOUPS AND STEWS  `soups`
- правило: Kinds of soup and stew
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~bisque, ~borscht, ~consomme, ~gazpacho, ~goulash, ~minestrone, +bouillon, +broth, +chicken noodle, +chili (chili_dish), +chowder, +gumbo, +lentil, +miso, +onion soup, +pho, +ramen, +split pea, +stew, +tomato

### SOUTHERN FOOD  `southern_dishes`
- правило: Dishes from the American South
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~jambalaya, +biscuit, +black eyed peas, +catfish, +cobbler, +collard greens, +cornbread, +fried chicken, +gravy, +grits, +gumbo, +hush puppy, +okra, +pecan pie, +pulled pork, +sweet tea

### SPANISH DISHES  `spanish_dishes`
- правило: Dishes from Spanish cuisine
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~churro, ~empanada, ~flan, ~gazpacho, ~jamon, ~manchego, +chorizo, +paella, +sangria, +tapas, +tortilla, ?croqueta, ?escalivada, xpatatas bravas

### STREET FOOD  `street_food`
- правило: Foods sold from street carts and stands
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~arepa, ~churro, +corn dog, +cotton candy, +crepe, +dumpling, +falafel, +gyro, +hot dog, +kebab, +popcorn, +pretzel, +roasted nuts, +taco, +waffle, !elote

### SUSHI BAR  `sushi_bar`
- правило: A dish or utensil served at a sushi bar
- тип связи: `found_in`, базовая сложность 0.55
- слов: 6
- ~chopstick, ~edamame, +bento, +maki, +sashimi, +teriyaki

### TEAS  `teas`
- правило: Kinds of tea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~ginger (ginger_spice), ~oolong, ~rooibos, ~white (white_food), +black, +chai, +chamomile, +darjeeling, +earl grey, +green (green_unripe), +herbal, +hibiscus, +Jasmine, +lemon, +matcha, +mint (mint_herb)

### WINE & BEER  `wines_and_drinks`
- правило: Kinds of wine and beer
- тип связи: `is_a`, базовая сложность 0.35
- слов: 17
- ~pilsner, ~Zinfandel, +ale, +Cabernet, +champagne, +Chardonnay, +cider, +ipa, +lager, +Merlot, +pinot, +porter, +prosecco, +Riesling, +rose, +sangria, +stout

### WORLD BREADS  `world_breads`
- правило: Breads from cuisines around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~challah, ~ciabatta, ~focaccia, ~matzo, ~pumpernickel, +baguette, +brioche, +naan, +pita, +roti, +rye, +sourdough, +tortilla, !arepa, !injera, !lavash

