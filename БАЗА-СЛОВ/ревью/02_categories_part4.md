# Категории, часть 4 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: animals

### AFRICAN ANIMALS  `african_animals`
- правило: Wild animals associated with the African savanna
- тип связи: `found_in`, базовая сложность 0.2
- слов: 21
- ~meerkat, ~warthog, +acacia, +antelope, +baboon, +buffalo, +cheetah, +crocodile, +elephant, +gazelle, +giraffe, +hippo, +hyena, +leopard, +lion, +mongoose, +ostrich, +rhino, +vulture, +wildebeest, +zebra

### AMPHIBIANS  `amphibians_and_bugs`
- правило: Animals that live both in water and on land as amphibians
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~bullfrog, ~frog, ~newt, ~salamander, ~toad, ~tree frog, ~wood frog, !axolotl, !hellbender, !spring peeper, xcaecilian, xmudpuppy

### BABY ANIMALS  `animal_babies`
- правило: English words for the young of an animal species
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~calf (calf_cow), ~cygnet, ~fry (fry_fish), +bunny, +chick, +colt, +cub, +duckling, +fawn, +foal, +gosling, +joey, +kid, +kitten, +lamb, +piglet, +pup, +puppy, +tadpole, !owlet

### ANIMAL PARTS  `animal_body_parts`
- правило: Body parts that animals have but people do not
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~horn (horn_animal), ~trunk (trunk_elephant), +antler, +beak, +claw, +fang, +fin, +flipper, +gill, +hoof, +hump, +mane, +muzzle, +paw, +snout, +tail, +talon, +tusk, +whisker, +wing

### ANIMAL COVERINGS  `animal_coverings`
- правило: Things that cover an animal body
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~coat (coat_fur), +down, +feather, +fleece, +fur, +hair, +hide, +plume, +quill, +scale (scale_skin), +shell, +skin, +spine, +wool, !plate (plate_armor)

### ANIMAL GROUPS  `animal_groups`
- правило: Collective nouns for groups of animals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~brood, ~colony, ~drove, ~flock, ~gaggle, ~herd, ~litter, ~pack, ~pod, ~pride, ~school, ~swarm, ~troop, !bevy, !covey

### ANIMAL HOMES  `animal_homes`
- правило: Words for the places animals live in
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~pen (pen_animal), +anthill, +barn, +burrow, +cave, +cocoon, +coop, +den, +hive, +hole, +hutch, +kennel, +lodge, +mound (mound_dirt), +nest, +roost, +shell, +stable, +warren, +web

### ANIMAL SOUNDS  `animal_sounds`
- правило: English words for the sound an animal makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 26
- ~bleat, ~croak, ~neigh, ~whinny, +bark (bark_sound), +bray, +buzz, +caw, +chirp, +cluck, +coo, +growl, +grunt, +hiss, +hoot, +howl, +meow, +moo, +oink, +purr, +quack, +roar, +snarl, +squeak, +tweet, +yelp

### ANIMAL MOVEMENTS  `animal_verbs`
- правило: Verbs for the way particular animals move
- тип связи: `does_action`, базовая сложность 0.4
- слов: 18
- ~burrow, ~crawl, ~dart (dart_move), ~flutter, ~gallop, ~glide, ~hop, ~leap, ~perch, ~pounce, ~prowl, ~scurry, ~slither, ~soar, ~swim, ~swoop, ~trot, ~waddle

### ANIMALS WITH SHELLS  `animals_with_shells`
- правило: Animals whose body is protected by a hard shell
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~armadillo, ~barnacle, ~beetle, ~clam, ~cockle, ~conch, ~crab, ~lobster, ~mussel, ~nautilus, ~oyster, ~scallop, ~snail, ~tortoise, ~turtle

### AQUARIUM  `aquarium_tank`
- правило: What lives in or belongs to a glass tank of water
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- ~crustaceans, ~gravel, ~shellfish, +coral, +filter, +fish, +turtles

### ARCTIC ANIMALS  `arctic_animals`
- правило: Animals that live in the Arctic north
- тип связи: `found_in`, базовая сложность 0.25
- слов: 17
- ~lemming, ~narwhal, ~ptarmigan, +arctic fox, +beluga, +caribou, +husky, +moose, +musk ox, +orca, +polar bear, +puffin, +reindeer, +seal (seal_animal), +snowy owl, +walrus, +wolverine

### BIRDS  `birds`
- правило: Bird species an average American can name
- тип связи: `is_a`, базовая сложность 0.12
- слов: 31
- +blue jay, +canary, +cardinal (cardinal_bird), +chicken, +crane (crane_bird), +crow, +duck (duck_bird), +eagle, +falcon, +flamingo, +goose, +hawk, +ostrich, +owl, +owls, +parrot, +peacock, +pelican, +penguin, +pigeon, +poultry, +raven, +robin, +seabirds, +seagull, +songbirds, +sparrow, +swan, +turkey (turkey_bird), +waterfowl, +woodpecker

### CAT THINGS  `cat_things`
- правило: Something you associate with keeping a cat
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 6
- +catnip, +litter, +meow, +purr, +scratch, +Whiskers

### DOG BREEDS  `dog_breeds`
- правило: Breeds of domestic dog recognized by an average American
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +beagle, +boxer, +bulldog, +chihuahua, +collie, +corgi, +dachshund, +dalmatian, +doberman, +greyhound, +husky, +labrador, +mastiff, +poodle, +pug, +retriever, +rottweiler, +shepherd, +spaniel, +terrier

### DOG THINGS  `dog_things`
- правило: Something you associate with keeping a dog
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- +bark (bark_sound), +bone, +collar, +fetch, +kennel, +leash, +paw

### EXTINCT ANIMALS  `extinct_animals`
- правило: Extinct animals and animal groups people recognize by name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~megalodon, ~pterodactyl, ~stegosaurus, ~trilobite, ~velociraptor, +bones, +brontosaurus, +dinosaur, +dodo, +mammoth, +mastodon, +raptor, +saber tooth, +triceratops, +tyrannosaurus

### FARM ANIMALS  `farm_animals`
- правило: Animals commonly kept on an ordinary farm
- тип связи: `is_a`, базовая сложность 0.1
- слов: 20
- ~calf (calf_cow), ~duck (duck_bird), ~turkey (turkey_bird), +bull, +cat, +chicken, +cow, +dog, +donkey, +goat, +goose, +hen, +horse, +lamb, +mule, +ox, +pig, +rabbit, +rooster, +sheep

### POULTRY  `farm_bird_words`
- правило: Birds raised for meat or eggs on a farm
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +chick, +chicken, +duck (duck_bird), +goose, +guinea fowl, +hen, +pheasant, +pigeon, +quail, +rooster, +turkey (turkey_bird), !capon

### FLYING ANIMALS  `flying_animals`
- правило: Animals that can fly under their own power
- тип связи: `has_property`, базовая сложность 0.2
- слов: 26
- +bat (bat_animal), +bee, +bluebird, +butterfly, +crow, +dragonfly, +duck (duck_bird), +eagle, +falcon, +goose, +hawk, +hornet, +hummingbird, +ladybug, +mosquito, +moth, +owl, +pelican, +pigeon, +robin, +seagull, +sparrow, +stork, +swan, +vulture, +wasp

### GIANT ANIMALS  `giant_animals`
- правило: An animal known for its very large size
- тип связи: `is_a`, базовая сложность 0.3
- слов: 7
- +elephant, +giraffe, +hippo, +moose, +rhino, +walrus, +whale

### HORSE WORDS  `horse_words`
- правило: Words for kinds of horses and horse gear
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~groom (groom_horse), ~stirrup, +bridle, +canter, +colt, +foal, +gallop, +halter, +harness, +hoof, +jockey, +mane, +mare, +pony, +reins, +saddle, +stable, +stallion, +thoroughbred, +trot

### BUGS  `insects`
- правило: Insects and other small bugs an average person recognizes
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~aphid, ~gnat, ~silkworm, +ant, +bee, +beetle, +butterfly, +caterpillar, +centipede, +cricket (cricket_insect), +dragonfly, +firefly, +flea, +fly (fly_insect), +grasshopper, +hornet, +ladybug, +locust, +mosquito, +moth, +roach, +spider, +termite, +tick (tick_bug), +wasp

### JUNGLE ANIMALS  `jungle_animals`
- правило: Animals that live in tropical jungles and rainforests
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~macaw, ~tapir, ~toucan, +anteater, +boa, +chimpanzee, +frog, +gorilla, +iguana, +jaguar, +lemur, +leopard, +monkey, +orangutan, +panther, +parrot, +python, +sloth, +snake, +tiger

### NOCTURNAL ANIMALS  `nocturnal_animals`
- правило: Animals that are active at night and rest during the day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 21
- ~armadillo, ~badger, ~bat (bat_animal), ~beaver, ~cougar, ~coyote, ~cricket (cricket_insect), ~firefly, ~fox, ~hamster, ~hedgehog, ~leopard, ~mole (mole_animal), ~moth, ~mouse (mouse_animal), ~opossum, ~owl, ~porcupine, ~raccoon, ~skunk, ~wolf

### OCEAN ANIMALS  `ocean_animals`
- правило: Animals that live in the ocean
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +barnacle, +clam, +coral, +crab, +dolphin, +eel, +jellyfish, +lobster, +manatee, +octopus, +orca, +oyster, +seahorse, +seal (seal_animal), +shark, +shrimp, +squid, +starfish, +stingray, +swordfish, +tuna, +turtle, +urchin, +walrus, +whale

### PESTS  `pests`
- правило: Animals treated as household or garden pests
- тип связи: `is_a`, базовая сложность 0.35
- слов: 22
- ~aphid, +ant, +flea, +gopher, +insects, +mole (mole_animal), +mosquito, +moth, +mouse (mouse_animal), +pigeon, +raccoon, +rat, +roach, +rodents, +slug, +snail, +termite, +tick (tick_bug), +wasp, +weevil, !bedbug, !silverfish

### PET STORE  `pet_store`
- правило: What a pet store sells or keeps in stock
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- ~rodents, +birds, +cage, +kibble, +leash, +pets, +reptiles

### PETS  `pets`
- правило: Animals commonly kept as household pets in the United States
- тип связи: `is_a`, базовая сложность 0.12
- слов: 22
- ~cockatiel, +bird, +canary, +cat, +chinchilla, +dog, +ferret, +fish, +gerbil, +goldfish, +guinea pig, +hamster, +hedgehog, +iguana, +lizard, +mouse (mouse_animal), +parakeet, +parrot, +pony, +rabbit, +snake, +turtle

### POND ANIMALS  `pond_animals`
- правило: Animals that live in or around a freshwater pond
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +beaver, +carp, +crayfish, +dragonfly, +duck (duck_bird), +fish, +frog, +goose, +heron, +mosquito, +newt, +otter, +salamander, +snail, +swan, +tadpole, +turtle, +water bug

### REPTILES  `reptiles`
- правило: Cold-blooded scaly animals classed as reptiles
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~skink, ~terrapin, +alligator, +anaconda, +boa, +chameleon, +cobra, +crocodile, +gecko, +iguana, +lizard, +lizards, +python, +rattlesnake, +snake, +snakes, +tortoise, +turtle, +turtles, +viper, !monitor (monitor_lizard)

### RODENTS  `rodents`
- правило: Small gnawing mammals classed as rodents
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~capybara, ~muskrat, +beaver, +chinchilla, +chipmunk, +gerbil, +gopher, +groundhog, +guinea pig, +hamster, +mouse (mouse_animal), +porcupine, +prairie dog, +rat, +squirrel, +vole

### STRIPED ANIMALS  `spotted_and_striped`
- правило: Animals whose coat has clear stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~badger, ~bee, ~chipmunk, ~hyena, ~raccoon, ~skunk, ~snake, ~tiger, ~wasp, ~zebra, !angelfish, !clownfish, !lemur, !okapi

### WILD CATS  `wild_cats`
- правило: Wild members of the cat family
- тип связи: `is_a`, базовая сложность 0.25
- слов: 13
- ~caracal, ~ocelot, ~serval, +bobcat, +cheetah, +cougar, +jaguar, +leopard, +lion, +lynx, +panther, +puma, +tiger

### ZOO ANIMALS  `zoo_animals`
- правило: Animals commonly seen at an American zoo
- тип связи: `found_in`, базовая сложность 0.15
- слов: 20
- +bear, +camel, +elephant, +flamingo, +giraffe, +gorilla, +hippo, +kangaroo, +koala, +lion, +monkey, +otter, +panda, +peacock, +penguin, +rhino, +seal (seal_animal), +sloth, +tiger, +zebra


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


## Тема: clothing

### ACCESSORIES  `accessories`
- правило: Small items worn or carried to complete an outfit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- ~bowtie, ~tie (tie_clothing), +backpack, +belt, +brooch, +clutch, +cufflinks, +eyewear, +gloves, +handbag, +hat, +hats, +headband, +jewelry, +purse, +scarf, +sunglasses, +suspenders, +umbrella, +wallet, +watch (watch_object)

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
- слов: 19
- ~crown (crown_royal), ~hood (hood_garment), +baseball cap, +beanie, +beret, +bonnet, +bowler, +cap, +cowboy hat, +fedora, +hard hat, +headband, +helmet, +panama, +sombrero, +sun hat, +top hat, +turban, +visor

### JEWELRY  `jewelry`
- правило: Decorative items worn on the body as jewelry
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- +anklet, +bangle, +bracelet, +brooch, +chain, +charm, +choker, +cufflink, +earring, +hoop, +locket, +necklace, +pendant, +ring (ring_jewelry), +stud, +tiara, +watch (watch_object), !pin (pin_fastener)

### JEWELRY BOX  `jewelry_box`
- правило: What is kept in a jewelry box or what it is made of
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~accessories, ~heirloom, +clasp, +gemstones, +jewelry, +metals, +velvet

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

### RAINY DAY GEAR  `rainy_day_gear`
- правило: Something you wear or meet on a rainy day
- тип связи: `used_in`, базовая сложность 0.3
- слов: 6
- +boots, +hood (hood_garment), +poncho, +puddle, +raincoat, +umbrella

### SEWING WORDS  `sewing_words`
- правило: Words used when sewing or altering clothes
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~baste, ~dart (dart_sew), +alter, +bobbin, +button (button_clothing), +cuff, +hem, +lining, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam, +stitch, +thimble, +thread, +tuck, +yarn, !pleat

### SHOE PARTS  `shoe_parts`
- правило: Parts of a shoe
- тип связи: `part_of`, базовая сложность 0.35
- слов: 16
- ~eyelet, ~insole, +aglet, +arch (arch_foot), +buckle, +cushion, +heel, +lace, +outsole, +shank, +sole (sole_shoe), +strap, +toe, +tongue, +tread, +upper

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

### WARDROBE  `wardrobe`
- правило: What hangs, sits or is stored in the place you keep clothes
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- ~mothball, +accessories, +closet, +footwear, +hanger, +hats, +sleepwear

### WINTER CABIN  `winter_cabin`
- правило: Something warm you wear or use in deep winter
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- ~earmuffs, ~snowshoe, ~thermals, ~toboggan

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

### PERSONALITY TRAITS  `personality_traits`
- правило: An adjective describing a person's character
- тип связи: `has_property`, базовая сложность 0.3
- слов: 7
- +brave, +curious, +honest, +kind, +loyal, +polite, +shy

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
- слов: 16
- +brisk, +creeping, +fast, +gradual, +hasty, +leisurely, +medium, +quick, +rapid, +slow, +sluggish, +speedy, +steady, +sudden, +swift, +turbo

### STRENGTH WORDS  `strength_words`
- правило: Words describing strength
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +brittle (brittle_property), +delicate, +durable, +feeble, +flimsy, +fragile, +frail, +mighty, +robust, +solid (solid_strong), +strong, +sturdy, +tough, +weak

### TASTE WORDS  `taste_words`
- правило: Words describing how food tastes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- +bitter, +bland, +buttery, +creamy, +crisp, +hearty, +mild, +nutty, +peppery, +rich, +salty, +savory, +smoky, +sour, +spicy, +sweet, +syrupy, +tangy, +tart, +umami, +zesty

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

### BEDTIME THINGS  `bedtime_things`
- правило: Something you associate with going to bed
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 7
- +bed, +blanket, +duvet, +mattress, +pillow, +sheets, +sleep

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
- слов: 27
- ~cabinet (cabinet_furniture), ~loveseat, +armchair, +bed, +bench (bench_seat), +bookshelf, +chair, +cot, +couch, +crib, +desk, +dresser, +futon, +headboard, +hutch, +nightstand, +ottoman, +rack, +recliner, +rocker, +shelves, +sideboard, +sofa, +stool, +table, +vanity, +wardrobe

### HOME APPLIANCES  `home_appliances`
- правило: A large electrical appliance kept in a home
- тип связи: `found_in`, базовая сложность 0.3
- слов: 6
- +dishwasher, +dryer, +fridge, +microwave, +toaster, +washer

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

### LAUNDRY DAY  `laundry_day`
- правило: Something used or done when washing clothes
- тип связи: `used_in`, базовая сложность 0.35
- слов: 7
- +bleach, +detergent, +hamper, +rinse, +softener, +spin, +stain

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

### TABLE SETTING  `table_setting`
- правило: An item laid on the table for one person at a meal
- тип связи: `found_in`, базовая сложность 0.2
- слов: 8
- +bowl, +cup, +fork, +glass, +knife, +napkin, +plate (plate_dish), +spoon

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
- ~blender, ~fan (fan_device), ~freezer, ~hairdryer, ~heater, ~iron (iron_appliance), ~kettle, ~lamp, ~lampshade, ~microwave, ~printer, ~toaster, +clock, +computer, +radio, +speaker, +television, +vacuum, !Charger (charger_device), !drill (drill_tool)

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


## Тема: jobs

### BEAUTY JOBS  `beauty_jobs`
- правило: Jobs held by people who work on hair, nails and appearance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~colorist, ~cosmetologist, ~esthetician, ~groomer, ~manicurist, +barber, +hairdresser, +makeup artist, +masseuse, +nail tech, +stylist, +tattoo artist

### BUILDING TRADES  `building_trades`
- правило: Skilled trades that build and repair buildings
- тип связи: `is_a`, базовая сложность 0.25
- слов: 19
- ~framer, ~glazier, ~plasterer, ~roofer, ~tiler, +architect, +bricklayer, +carpenter, +contractor, +electrician, +foreman, +installer, +laborer, +mason, +painter, +plumber, +surveyor, +welder, ?drywaller

### CIRCUS JOBS  `circus_and_fair_jobs`
- правило: Jobs held by performers and workers at a circus or fair
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~contortionist, ~stilt walker, +acrobat, +animal trainer, +barker, +clown, +fire eater, +juggler, +magician, +ringmaster, +tightrope walker, +trapeze artist

### COMMON PROFESSIONS  `common_professions`
- правило: A common job a person does for a living
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +chef, +doctor, +engineer, +farmer, +lawyer, +manager, +pilot, +teacher

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


## Тема: materials

### BUILDING MATERIALS  `building_materials`
- правило: Materials used to construct buildings
- тип связи: `made_of`, базовая сложность 0.25
- слов: 21
- +aluminum, +brick, +cement, +concrete, +drywall, +glass, +granite, +gravel, +insulation, +lumber, +marble (marble_stone), +plaster, +plywood, +shingle, +slate, +steel, +stone, +stucco, +tile, +vinyl, +wood

### EVERYDAY MATERIALS  `everyday_materials`
- правило: A material everyday objects are made of
- тип связи: `is_a`, базовая сложность 0.25
- слов: 7
- +glass, +leather, +metal, +paper, +plastic, +rubber, +wood

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
- слов: 15
- ~feldspar, ~hematite, +calcite, +gemstones, +graphite, +gypsum, +magnetite, +mica, +pyrite, +quartz, +sulfur, +talc, !azurite, !fluorite, !halite

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
- ~anchor, ~armor, ~bell (bell_object), ~faucet, ~hinge, ~kettle, ~key (key_lock), ~ladder, ~nail (nail_metal), ~pipe (pipe_tube), ~spoon, ~wrench, +can, +chain, +coin, +safe, +sword, +wire

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


## Тема: nature_more

### ARCTIC TREK  `arctic_trek`
- правило: Something met crossing the frozen Arctic
- тип связи: `found_in`, базовая сложность 0.65
- слов: 5
- ~auroras, ~floe, +huskies, +icebreaker, +permafrost

### BIOMES  `biomes`
- правило: Major natural regions of the earth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +chaparral, +desert, +grassland, +marsh, +mountain, +ocean, +prairie, +rainforest, +reef, +savanna, +steppe, +taiga, +tundra, +wetland

### CANYONS AND VALLEYS  `canyons_and_valleys`
- правило: Famous canyons and valleys
- тип связи: `is_a`, базовая сложность 0.45
- слов: 10
- +Antelope Canyon, +Bryce Canyon, +Copper Canyon, +Death Valley, +Grand Canyon, +Napa Valley, +Rift Valley, +Silicon Valley, +Yosemite Valley, +Zion

### CAVE THINGS  `cave_things`
- правило: Things found inside a cave
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bat (bat_animal), ~drip (drip_water), +cavern, +chamber, +column, +crystal, +darkness, +Echo, +fossil, +moss, +pool, +stalagmite, +tunnel, !stalactite

### CLOUD TYPES  `cloud_types`
- правило: A named type of cloud
- тип связи: `is_a`, базовая сложность 0.6
- слов: 4
- +cirrus, +cumulus, +nimbus, +stratus

### EROSION WORDS  `erosion_words`
- правило: Ways water shapes the land over time
- тип связи: `does_action`, базовая сложность 0.45
- слов: 13
- ~canyon, ~carve, ~delta (delta_river), ~deposit, ~erosion, ~flood, ~gully, ~meander, ~runoff, ~sediment, ~silt, ~undercut, ~weathering

### KINDS OF FOREST  `forest_types`
- правило: Kinds of forest and woodland
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~boreal, ~cloud forest, ~deciduous, ~grove, ~jungle, ~mangrove, ~pine forest, ~rainforest, ~taiga, ~thicket, ~woodland, +old growth

### NATIONAL PARKS  `national_parks_us`
- правило: American national parks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +Acadia, +Arches, +Badlands, +Denali, +Everglades, +glacier, +Grand Canyon, +Joshua Tree, +Olympic, +redwood, +sequoia, +Shenandoah, +Yellowstone, +Yosemite, +Zion

### NIGHT SKY  `night_sky_things`
- правило: Things visible in the night sky
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~plane (plane_aircraft), +aurora, +cloud, +comet, +constellation, +eclipse, +galaxy, +meteor, +Milky Way, +moon (moon_space), +planet, +satellite, +shooting star, +star (star_space)

### RAINFOREST  `rainforest`
- правило: A plant, animal or layer of the rainforest
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- ~macaw, ~treetop, +howler, +liana, +undergrowth

### ROCK FORMATIONS  `rock_formations`
- правило: Natural rock shapes and formations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~arch (arch_structure), +boulder, +butte, +cave, +cliff, +hoodoo, +mesa, +monolith, +outcrop, +pillar, +sinkhole, +spire, +terrace, !stack (stack_pile)

### FALL THINGS  `seasons_fall`
- правило: Things associated with autumn
- тип связи: `found_in`, базовая сложность 0.25
- слов: 14
- ~cornstalk, ~hayride, ~squash (squash_vegetable), +acorn, +apple cider, +bonfire, +chestnut, +foliage, +harvest, +leaf, +pumpkin, +rake, +scarecrow, +sweater

### SPRING THINGS  `seasons_spring`
- правило: Things associated with spring
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~kite (kite_toy), +bee, +blossom, +bud, +chick, +lamb, +mud, +nest, +pollen, +puddle, +rain, +rainbow, +robin, +sprout, +tulip, +umbrella

### SUMMER THINGS  `seasons_summer`
- правило: Things associated with summer
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- +barbecue, +beach, +camp, +fan (fan_device), +firefly, +hammock, +lemonade, +pool, +Popsicle, +sandals, +sprinkler, +sunburn, +sunscreen, +surfboard, +vacation, +watermelon

### WINTER THINGS  `seasons_winter`
- правило: Things associated with winter
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- +blanket, +blizzard, +boot (boot_shoe), +fireplace, +frost, +hot cocoa, +icicle, +mitten, +scarf, +shovel, +skate, +ski, +sled, +snow, +snowflake, +snowman

### MOON PHASES  `tide_and_moon`
- правило: Phases and states of the moon
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~quarter (quarter_fourth), +blue moon, +crescent, +eclipse, +full moon, +half moon, +harvest moon, +new moon, +waning, +waxing, !gibbous, !supermoon

### VOLCANO WATCH  `volcano_watch`
- правило: A term used describing a volcano
- тип связи: `associated_with`, базовая сложность 0.65
- слов: 5
- +caldera, +dormant, +molten, +pumice, +vent

### VOLCANOES  `volcanoes`
- правило: Famous volcanoes
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Kilauea, ~Krakatoa, ~Mauna Loa, ~Stromboli, +Etna, +Fuji, +Rainier, +St Helens, +Vesuvius, !Cotopaxi, !Pinatubo, !Popocatepetl

### WATERFALLS  `waterfalls`
- правило: Famous waterfalls
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~Havasu, ~Multnomah, ~Shoshone, +Angel Falls, +Niagara, +Sutherland, +Victoria, +Yosemite Falls, !Iguazu, xGullfoss

### WIND WORDS  `wind_words`
- правило: Words for kinds and strengths of wind
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~crosswind, ~downdraft, ~headwind, ~tailwind, +breeze, +chinook, +draft (draft_wind), +gale, +gust, +jet stream, +squall, +trade wind, +whirlwind, +zephyr

### LAKES  `world_lakes`
- правило: Well known lakes of the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Baikal, +Como, +Crater Lake, +Erie, +Geneva, +Great Salt Lake, +Huron, +Loch Ness, +Michigan, +Ontario, +Superior, +Tahoe, +Victoria, !Titicaca


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
- ~aphid, ~roly poly, +ant, +bee, +beetle, +caterpillar, +centipede, +cricket (cricket_insect), +earthworm, +earwig, +grub, +ladybug, +praying mantis, +slug, +snail, +spider

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

### EMOTIONS  `emotions`
- правило: A word naming or describing a feeling a person has
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 8
- +angry, +fear, +happy, +joy, +pride, +sad, +surprise, +worry

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
- слов: 26
- +aunt, +brother, +child, +cousin, +daughter, +father, +godmother, +grandchild, +grandfather, +grandma, +grandmother, +husband, +in law, +mother, +nephew, +niece, +parent, +sibling, +sister, +son, +spouse, +stepfather, +stepmother, +twin, +uncle, +wife

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
- слов: 26
- +Abigail, +Amelia, +Ava, +Charlotte, +Chloe, +Elizabeth, +Ella, +Emily, +Emma, +Grace, +Hannah, +Isabella, +Jennifer, +jessica, +Lily, +Linda, +Madison, +Mary, +Mia, +Natalie, +Olivia, +Rachel, +Sarah, +Sophia, +Susan, +Zoe

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
- ~ford (ford_person), +diesel, +Edison, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Tesla, +Watt, +Whitney, +Wright, !bell (bell_person), !Daguerre

### STAGES OF LIFE  `life_stages`
- правило: Words for the stages of a human life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 17
- ~preschooler, +adolescent, +adult, +baby, +child, +elder (elder_person), +grownup, +infant, +kid, +middle age, +newborn, +retiree, +senior, +teen, +teenager, +toddler, +youth

### MORNING ROUTINE  `morning_routine`
- правило: Something a person does first thing in the morning
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 6
- +alarm, +breakfast, +coffee, +shower, +stretch, +wake

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
- ~crocus, ~snowdrop, +azalea, +bluebell, +cherry blossom, +daffodil, +hyacinth, +iris (iris_flower), +lilac, +magnolia, +pansy, +primrose, +tulip, !forsythia

### SUMMER FLOWERS  `garden_flowers_summer`
- правило: Flowers that bloom in summer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~hydrangea, ~petunia, +black eyed susan, +cosmos, +dahlia, +Daisy, +geranium, +lavender (lavender_plant), +Lily, +marigold, +rose (rose_flower), +snapdragon, +sunflower, !zinnia

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
- ~azalea, ~hedge, ~holly, ~hydrangea, ~juniper, ~lilac, ~rhododendron, ~rose (rose_flower), !barberry, !boxwood, !forsythia, !privet, !spirea, !viburnum

### TROPICAL PLANTS  `tropical_plants`
- правило: Plants that grow in tropical climates
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~palm (palm_tree), +bamboo, +banana, +banyan, +cocoa, +coffee, +Fern, +hibiscus, +mangrove, +orchid, +papaya, +rubber tree, !bromeliad, !plumeria

### VINES AND CLIMBERS  `vines`
- правило: Plants that climb or trail along a surface
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bean, ~clematis, ~cucumber, ~grape, ~honeysuckle, ~hops, ~Ivy, ~morning glory, ~passion flower, ~pea, ~pumpkin, ~wisteria, !Jasmine (jasmine_flower), !kudzu

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


## Тема: technology

### CLOCKWORK  `clockwork`
- правило: A word belonging to the workings of a clock
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chime, +cogs, +pendulum, +winding

### COMPUTER ACTIONS  `computer_actions`
- правило: Actions done while using a computer
- тип связи: `does_action`, базовая сложность 0.25
- слов: 20
- +click, +close, +copy, +delete, +download, +drag, +install, +log in, +paste, +print, +refresh, +restart, +save, +scroll (scroll_screen), +search, +share, +type, +undo, +upload, +Zoom

### COMPUTER PARTS  `computer_parts`
- правило: Physical parts of a personal computer
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~touchpad, +battery, +cable, +Charger (charger_device), +fan (fan_device), +graphics card, +hard drive, +keyboard (keyboard_computer), +memory, +monitor (monitor_screen), +motherboard, +mouse (mouse_computer), +port, +power supply, +processor, +screen (screen_display), +speaker, +tower, +webcam, !case (case_box)

### EMAIL WORDS  `email_words`
- правило: Parts and actions of an email message
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~draft (draft_document), ~outbox, +archive, +attachment, +cc, +forward, +inbox, +recipient, +reply, +sender, +signature, +spam, +subject, +thread, +trash, +unread

### FILE WORDS  `file_types`
- правило: Words for computer files and documents
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +archive, +attachment, +backup, +document, +draft (draft_document), +file (file_computer), +folder, +image, +pdf, +presentation, +shortcut, +spreadsheet, +template, +trash, +video, +zip

### GADGETS  `gadgets`
- правило: Small electronic devices people own
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~remote (remote_device), +camera, +console, +doorbell, +drone, +e-reader, +earbuds, +fitness tracker, +headphones, +laptop, +phone, +printer, +projector, +scanner, +speaker, +tablet, +thermostat, +watch (watch_object)

### HOME ELECTRONICS  `home_electronics`
- правило: Electronic devices used in a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~humidifier, +air conditioner, +alarm, +blender, +doorbell, +dvd player, +game console, +microwave, +radio, +router, +smart speaker, +stereo, +television, +thermostat, +vacuum

### INTERNET WORDS  `internet_words`
- правило: Words used about the internet
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- +bandwidth, +bookmark, +browser, +cloud, +cookie, +domain, +download, +email, +firewall, +hotspot, +link (link_web), +network, +password, +router, +server, +spam, +streaming, +url, +website, +wifi

### MEASURING DEVICES  `measurement_devices`
- правило: Devices that measure and display a reading
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~altimeter, ~seismograph, ~sundial, ~voltmeter, +barometer, +compass, +gauge, +meter, +odometer, +scale (scale_weigh), +speedometer, +stopwatch, +tachometer, +thermometer

### OFFICE MACHINES  `office_machines`
- правило: Machines used in an office
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~laminator, +binder machine, +calculator, +computer, +copier, +fax, +label maker, +phone, +postage meter, +printer, +projector, +scanner, +shredder, +typewriter

### PHONE WORDS  `phone_words`
- правило: Things and features of a mobile phone
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- +alarm, +app, +battery, +camera, +Charger (charger_device), +contact, +headphones, +hotspot, +keypad, +notification, +ringtone, +screen (screen_display), +signal, +sim card, +speaker, +text, +voicemail, !case (case_box)

### PHOTOGRAPHY WORDS  `photography_words`
- правило: Words used when taking photographs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +album, +angle, +aperture, +crop, +darkroom, +exposure, +filter, +flash, +focus (focus_lens), +frame, +lens, +negative, +portrait, +selfie, +shutter, +snapshot, +tripod, +Zoom

### POWER WORDS  `power_and_batteries`
- правило: Words about supplying power to devices
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- +adapter, +battery, +cable, +Charger (charger_device), +cord, +extension, +fuse, +generator, +outlet, +plug, +power strip, +socket (socket_electric), +solar panel, +switch, +voltage, +Watt

### PROGRAMMING WORDS  `programming_words`
- правило: Words used when writing computer programs
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~algorithm, ~array, ~bug, ~class, ~code, ~compile, ~database, ~function, ~library, ~loop, ~module, ~output, ~query, ~script, ~string, ~syntax, ~variable, !debug

### ROBOT WORDS  `robot_words`
- правило: Words used when talking about robots
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~algorithm, ~android, ~arm, ~automation, ~chassis, ~circuit, ~drone, ~gear, ~joint, ~motor, ~robot, ~sensor, ~servo, +program, !remote (remote_device)

### THINGS WITH SCREENS  `screens`
- правило: Everyday devices that have a screen
- тип связи: `has_property`, базовая сложность 0.3
- слов: 16
- ~ATM, ~calculator, ~dashboard, ~kiosk, ~microwave, ~monitor (monitor_screen), ~treadmill, ~watch (watch_object), +camera, +console, +e-reader, +gps, +laptop, +phone, +tablet, +television

### SECURITY DEVICES  `security_tech`
- правило: Devices used to keep property secure
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~deadbolt, ~floodlight, ~siren (siren_device), +alarm, +badge, +buzzer, +camera, +fence, +keypad, +lock, +monitor (monitor_screen), +motion detector, +safe, +sensor

### SIGNALS AND CODES  `signals_and_codes`
- правило: Systems used to send coded messages
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~barcode, ~beacon, ~braille, ~cipher, ~flag signal, ~morse code, ~qr code, ~semaphore, ~sign language, ~smoke signal, ~telegraph

### SOCIAL MEDIA  `social_media_words`
- правило: Words used on social media
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +comment, +emoji, +feed, +filter, +follow, +hashtag, +like, +message, +post (post_online), +profile, +share, +thread, +trending, +viral, !block (block_ban), !reel (reel_video), !story (story_post), !tag (tag_mention)

### SOUND DEVICES  `sound_devices`
- правило: Devices that record or play sound
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~boombox, ~earbud, ~soundbar, +amplifier, +headphone, +megaphone, +microphone, +radio, +record player, +speaker, +stereo, +tape deck, +turntable, +walkman

### OLD TECHNOLOGY  `things_with_screens_history`
- правило: Technology that has mostly been replaced
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~cassette, ~dial up, ~fax, ~film camera, ~floppy disk, ~overhead projector, ~pager, ~phonograph, ~rotary phone, ~telegram, ~typewriter, ~vhs, ~walkman, !payphone

### TIMEPIECES  `timepieces`
- правило: A device that measures or shows the passing of time
- тип связи: `used_for`, базовая сложность 0.4
- слов: 6
- ~sundial, +clock, +hourglass, +metronome, +stopwatch, +watch (watch_object)

