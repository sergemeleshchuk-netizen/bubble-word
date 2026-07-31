# Категории, часть 4 из 4

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
- слов: 30
- ~march (march_walk), ~shuffle (shuffle_walk), ~spring (spring_jump), ~trudge, +climb, +crawl, +crawling, +dart (dart_move), +dash (dash_run), +flying, +hop, +hopping, +jog, +jump, +leap, +limp, +race, +run, +scramble, +skip, +slide, +sprint, +stagger, +stroll, +swim, +swimming, +tiptoe, +wade, +walk, +wander

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


## Тема: animals

### ADVOCATE  `advocate`
- правило: What belongs to the group «Advocate» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +back, +Champion, +endorse, +support

### AFRICAN ANIMALS  `african_animals`
- правило: Wild animals associated with the African savanna
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~meerkat, ~warthog, +antelope, +baboon, +buffalo, +cheetah, +crocodile, +elephant, +gazelle, +giraffe, +hippo, +hyena, +leopard, +lion, +mongoose, +ostrich, +rhino, +vulture, +wildebeest, +zebra

### ALCATRAZ ISLAND  `alcatraz_island`
- правило: What belongs to the group «Alcatraz Island» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +guards, +inmates, +san francisco, +tourist attraction

### ALLOCATE  `allocate`
- правило: What belongs to the group «Allocate» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +allot, +appoint, +assign, !earmark

### AMPHIBIANS  `amphibians_and_bugs`
- правило: Animals that live both in water and on land as amphibians
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~bullfrog, ~frog, ~newt, ~salamander, ~toad, ~tree frog, ~wood frog, !axolotl, !hellbender, !spring peeper, xcaecilian, xmudpuppy

### ANIMAL AND BIRD HOMES  `animal_and_bird_homes`
- правило: What belongs to the group «Animal And Bird Homes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +burrow, +den, +hive, +nest

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

### ANIMAL CLASSIFICATION  `animal_classification`
- правило: What belongs to the group «Animal Classification» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +class, +kingdom, +order, +phylum

### ANIMAL COVERINGS  `animal_coverings`
- правило: Things that cover an animal body
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~coat (coat_fur), +down, +feather, +fleece, +fur, +hair, +hide, +plume, +quill, +scale (scale_skin), +shell, +skin, +spine, +wool, !plate (plate_armor)

### ANIMAL DEFENSE  `animal_defense`
- правило: What belongs to the group «Animal Defense» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +claw, +fang, +spine, +venom

### ANIMAL GROUP NAMES  `animal_group_names`
- правило: What belongs to the group «Animal Group Names» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +flock, +pack, +pod, +pride

### ANIMAL GROUPS  `animal_groups`
- правило: Collective nouns for groups of animals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 25
- ~brood, ~colony, ~dazzle, ~drove, ~flock, ~gaggle, ~herd, ~litter, ~pack, ~parliament, ~pod, ~pride, ~school, ~swarm, ~troop, ~wake, ?colony, ?herd, ?pack, ?pod, ?pride, ?school, ?swarm, !bevy, !covey

### ANIMAL HOMES  `animal_homes`
- правило: Words for the places animals live in
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~pen (pen_animal), +anthill, +barn, +burrow, +cave, +cocoon, +coop, +den, +hive, +hole, +hutch, +kennel, +lodge, +mound (mound_dirt), +nest, +roost, +shell, +stable, +warren, +web, ?burrow, ?hive, ?kennel, ?nest

### ANIMAL HOMOPHONES  `animal_homophones`
- правило: What belongs to the group «Animal Homophones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +bear, +deer, +hare, +moose

### ANIMAL KINGDOM  `animal_kingdom`
- правило: What belongs to the group «Animal Kingdom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +birds, +fish, +mammals, +reptiles

### ANIMAL SOUNDS  `animal_sounds`
- правило: English words for the sound an animal makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 34
- ~bleat, ~croak, ~neigh, ~whinny, +bark (bark_sound), +bray, +buzz, +caw, +chirp, +cluck, +coo, +growl, +grunt, +hiss, +hoot, +howl, +meow, +moo, +oink, +purr, +quack, +roar, +snarl, +squeak, +tweet, +yelp, ?chirp, ?growl, ?meow, ?moo, ?neigh, ?quack, ?roar, ?tweet

### ANIMAL TYPES  `animal_types`
- правило: What belongs to the group «Animal Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +birds, +fish, +mammals, +reptiles

### ANIMAL MOVEMENTS  `animal_verbs`
- правило: Verbs for the way particular animals move
- тип связи: `does_action`, базовая сложность 0.4
- слов: 18
- ~burrow, ~crawl, ~dart (dart_move), ~flutter, ~gallop, ~glide, ~hop, ~leap, ~perch, ~pounce, ~prowl, ~scurry, ~slither, ~soar, ~swim, ~swoop, ~trot, ~waddle

### ANIMALS  `animals`
- правило: What belongs to the group «Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 17
- +alpaca, +amphibians, +birds, +camel, +elephant, +fish, +giraffe, +hippo, +hyena, +lion, +mammals, +moose, +otter, +penguin, +reptiles, +sloth, +zebra

### ANIMALS THAT SHED SKIN  `animals_that_shed_skin`
- правило: What belongs to the group «Animals That Shed Skin» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +crab, +iguana, +salamander, +spider

### ANIMALS WITH HORNS  `animals_with_horns`
- правило: What belongs to the group «Animals With Horns» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +bighorn, +bull, +rhino, !ibex

### ANIMALS WITH POUCHES  `animals_with_pouches`
- правило: What belongs to the group «Animals With Pouches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +kangaroo, +koala, +possum, +wombat

### ANIMALS WITH SHELLS  `animals_with_shells`
- правило: Animals whose body is protected by a hard shell
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~armadillo, ~barnacle, ~beetle, ~clam, ~cockle, ~conch, ~crab, ~lobster, ~mussel, ~nautilus, ~oyster, ~scallop, ~snail, ~tortoise, ~turtle

### ANNOYING INSECTS  `annoying_insects`
- правило: What belongs to the group «Annoying Insects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +cockroach, +mosquito, +moth, !gnat

### APPETIZER  `appetizer`
- правило: What belongs to the group «Appetizer» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +nachos, +salad, +soup, +spring roll

### APPETIZERS  `appetizers`
- правило: What belongs to the group «Appetizers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +baguette, +fries, +nachos, +poppers, +wings, !antipasto, !bruschetta

### AQUARIUM FISH  `aquarium_fish`
- правило: What belongs to the group «Aquarium Fish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +betta, +gold fish, +tetra, !guppy

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

### BEACH VACATION  `beach_vacation`
- правило: What belongs to the group «Beach Vacation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +beach, +cocktail, +tanning, +water sports

### BIG CATS  `big_cats`
- правило: What belongs to the group «Big Cats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +cheetah, +leopard, +lion, +tiger

### BIG MAMMALS  `big_mammals`
- правило: What belongs to the group «Big Mammals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +elephant, +giraffe, +hippopotamus, +rhinoceros

### BIOLOGY CLASSIFICATIONS  `biology_classifications`
- правило: What belongs to the group «Biology Classifications» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +fungi, +genus, +phylum, +species

### BIRD FEATURES  `bird_features`
- правило: What belongs to the group «Bird Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +beak, +feather, +talon, +wing

### BIRD SOUND  `bird_sound`
- правило: What belongs to the group «Bird Sound» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +caw, +chirp, +hoot, +tweet

### BIRD SOUNDS  `bird_sounds`
- правило: What belongs to the group «Bird Sounds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +caw, +chirp, +hoot, +sing

### BIRD SPECIES  `bird_species`
- правило: What belongs to the group «Bird Species» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 8
- +albatross, +finch, +pelican, +robin, +starling, +toucan, +wren, !macaw

### BIRDS  `birds`
- правило: Bird species an average American can name
- тип связи: `is_a`, базовая сложность 0.12
- слов: 52
- +blue jay, +canary, +cardinal (cardinal_bird), +chicken, +crane (crane_bird), +crow, +duck (duck_bird), +eagle, +emu, +falcon, +finch, +flamingo, +goose, +hawk, +heron, +jay, +kiwi, +osprey, +ostrich, +owl, +owls, +parrot, +peacock, +pelican, +penguin, +pigeon, +plover, +poultry, +raven, +robin, +seabirds, +seagull, +songbirds, +sparrow, +swan, +turkey (turkey_bird), +waterfowl, +woodpecker, ?crow, ?eagle, ?falcon, ?flamingo, ?goose, ?hawk, ?ostrich, ?owl, ?parrot, ?penguin, ?pigeon, ?robin, ?sparrow, ?swan

### BIRDS LIFE  `birds_life`
- правило: What belongs to the group «Birds Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +birds, +egg, +nest, +trees

### BIRDSONG  `birdsong`
- правило: What belongs to the group «Birdsong» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +coo, !cheep, !chirrup, !warble

### BLACK AND WHITE ANIMALS  `black_and_white_animals`
- правило: What belongs to the group «Black And White Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +dalmatian, +panda, +penguin, +zebra

### BODY MODIFICATIONS  `body_modifications`
- правило: What belongs to the group «Body Modifications» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +can be pierced, +ear jewelry, +ear stretching, +facelift

### CARTOON CATS  `cartoon_cats`
- правило: What belongs to the group «Cartoon Cats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +felix, +Garfield, +Sylvester, +tom

### CARTOON DOGS  `cartoon_dogs`
- правило: What belongs to the group «Cartoon Dogs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +Goofy, +Pluto, +Scooby, +Snoopy

### CASTLE FORTIFICATIONS  `castle_fortifications`
- правило: What belongs to the group «Castle Fortifications» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +drawbridge, +moat, +tower, +wall

### CAT  `cat`
- правило: What belongs to the group «Cat» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 9
- +maine coon, +meow, +munchkin, +persian, +purr, +scratch, +siamese, +Whiskers, !sphynx

### CAT ESSENTIALS  `cat_essentials`
- правило: What belongs to the group «Cat Essentials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +boxes, +cat bed, +food bowl, +water bowl

### CAT FAMILY  `cat_family`
- правило: What belongs to the group «Cat Family» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +cat, +cheetah, +leopard, +tiger

### CAT RELATED  `cat_related`
- правило: What belongs to the group «Cat Related» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +litter box, +meow, +Whiskers, xmaneki neko

### CAT TYPES  `cat_types`
- правило: What belongs to the group «Cat Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bengal, +calico, +siamese, +tabby

### CATEGORIES  `categories`
- правило: What belongs to the group «Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +classifications, +genera, +inventions, +types

### CATERPILLAR  `caterpillar`
- правило: What belongs to the group «Caterpillar» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +cocoon, +crawl, +hungry, +leaf

### CATS  `cats`
- правило: What belongs to the group «Cats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +balinese, !abyssinian, !american shorthair, !birman

### CATTLE  `cattle`
- правило: What belongs to the group «Cattle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +angus, +ayrshire, +barn, +pasture

### CHINESE ZODIAC ANIMALS  `chinese_zodiac_animals`
- правило: What belongs to the group «Chinese Zodiac Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +dog, +dragon, +monkey, +tiger

### CHIRPING INSECTS  `chirping_insects`
- правило: What belongs to the group «Chirping Insects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +grasshopper, +locust, !cicada, !katydid

### CLASSIC DOG NAMES  `classic_dog_names`
- правило: What belongs to the group «Classic Dog Names» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +fido, +lucky, +rover, +spot

### CLASSIFICATION  `classification`
- правило: What belongs to the group «Classification» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.14
- слов: 7
- +category, +collection, +group, +ranking, +sorting, +species, +type

### CLIMATE CLASSIFICATION  `climate_classification`
- правило: What belongs to the group «Climate Classification» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +arid, +desert, +equatorial, +monsoon

### COLD BLOODED ANIMALS  `cold_blooded_animals`
- правило: What belongs to the group «Cold Blooded Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 5
- +crocodile, +fish, +lizard, +snake, +turtle

### COMMANDS FOR DOGS  `commands_for_dogs`
- правило: What belongs to the group «Commands For Dogs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +come, +down, +sit, +stay

### COMMUNICATION  `communication`
- правило: What belongs to the group «Communication» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 11
- +call, +email, +facetime, +fax, +phone, +radio, +sms, +snapchat, +telegraph, +text, +whatsapp

### COMMUNICATION CODES  `communication_codes`
- правило: What belongs to the group «Communication Codes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 5
- +binary, +braille, +cipher, +Morse, +semaphore

### COMMUNICATION SYSTEMS  `communication_systems`
- правило: What belongs to the group «Communication Systems» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 6
- +braille, +Morse, +morse code, +semaphore, +sign language, !hieroglyphs

### COMMUNICATION TECHNOLOGY  `communication_technology`
- правило: What belongs to the group «Communication Technology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +fiber, +radio, +satellite, +telephone

### COMMUNICATION TOOLS  `communication_tools`
- правило: What belongs to the group «Communication Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +beacon, +internet, +radio, +smartphone

### COMPETE  `compete`
- правило: What belongs to the group «Compete» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +award, +contest, +fight, +loser

### COMPETES  `competes`
- правило: What belongs to the group «Competes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +athletes, +car racer, +contestant, !duelist

### COMPETITIVE SPORTS  `competitive_sports`
- правило: What belongs to the group «Competitive Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +archery, +gymnastics, +swimming, +wrestling

### DAIRY ANIMALS  `dairy_animals`
- правило: What belongs to the group «Dairy Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +buffalo, +cow, +goat, +sheep

### DANGEROUS ANIMALS  `dangerous_animals`
- правило: What belongs to the group «Dangerous Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +cobra, +jaguar, +shark, +viper

### DELICATE  `delicate`
- правило: What belongs to the group «Delicate» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 7
- +ethereal, +exquisite, +fragile, +frail, +tender, +wispy, !gossamer

### DESERT ANIMAL  `desert_animal`
- правило: What belongs to the group «Desert Animal» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +camel, +scorpion, +snake, !meerkat

### DESERT ANIMALS  `desert_animals`
- правило: What belongs to the group «Desert Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 6
- +camel, +lizard, +scorpion, +snake, !fennec, !meerkat

### DOG  `dog`
- правило: What belongs to the group «Dog» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 13
- +beagle, +bone, +bulldog, +dalmatian, +fetch, +husky, +labrador, +leash, +mastiff, +pomeranian, +poodle, +pug, !malamute

### DOG BREEDS  `dog_breeds`
- правило: Breeds of domestic dog recognized by an average American
- тип связи: `is_a`, базовая сложность 0.25
- слов: 36
- ~vizsla, ~weimaraner, +beagle, +boxer, +bulldog, +chihuahua, +collie, +corgi, +dachshund, +dalmatian, +doberman, +greyhound, +husky, +labrador, +mastiff, +pointer, +poodle, +pug, +retriever, +rhodesian, +rottweiler, +shepherd, +spaniel, +terrier, ?beagle, ?bulldog, ?collie, ?corgi, ?dachshund, ?greyhound, ?husky, ?labrador, ?poodle, ?retriever, ?spaniel, ?terrier

### DOG BREEDS FROM ASIA  `dog_breeds_from_asia`
- правило: What belongs to the group «Dog Breeds From Asia» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chow chow, !akita, !shar pei, !shiba inu

### DOG COMMANDS  `dog_commands`
- правило: What belongs to the group «Dog Commands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +fetch, +heel, +sit, +stay

### DOG PARK  `dog_park`
- правило: What belongs to the group «Dog Park» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +frisbee, +leash, +training, +water bowl

### DOG SPORTS  `dog_sports`
- правило: What belongs to the group «Dog Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +agility, +herding, +obedience, !flyball

### DOG TRICKS  `dog_tricks`
- правило: What belongs to the group «Dog Tricks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.14
- слов: 4
- +fetch, +play dead, +roll over, +sit

### DOG TYPES  `dog_types`
- правило: What belongs to the group «Dog Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 7
- +beagle, +great dane, +husky, +labrador, +maltese, +poodle, +retriever

### DOGS  `dogs`
- правило: What belongs to the group «Dogs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 10
- +beagle, +bull, +bulldog, +dachshund, +dalmatian, +husky, +poodle, +pug, +shepherd, +terrier

### DRAFT ANIMALS  `draft_animals`
- правило: What belongs to the group «Draft Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +donkey, +horse, +mule, +ox

### DREAM CATCHER  `dream_catcher`
- правило: What belongs to the group «Dream Catcher» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +cord, +feather, +native american, +talisman

### ECONOMIC INDICATORS  `economic_indicators`
- правило: What belongs to the group «Economic Indicators» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +deficit, +gdp, +inflation, +surplus

### EDUCATION  `education`
- правило: What belongs to the group «Education» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 12
- +exam, +homework, +knowledge, +learning, +lesson, +math, +reading, +school, +science, +student, +teacher, +writing

### EDUCATION INSTITUTIONS  `education_institutions`
- правило: What belongs to the group «Education Institutions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +academy, +college, +institute, +university

### EDUCATION PATH  `education_path`
- правило: What belongs to the group «Education Path» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +college, +kindergarten, +school, +university

### EDUCATIONAL BUILDING  `educational_building`
- правило: What belongs to the group «Educational Building» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +academy, +institute, +school, +university

### EDUCATIONAL INSTITUTIONS  `educational_institutions`
- правило: What belongs to the group «Educational Institutions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +academy, +conservatory, +seminary, +university departments

### EMMY AWARD CATEGORIES  `emmy_award_categories`
- правило: What belongs to the group «Emmy Award Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +comedy, +documentary, +drama, +reality

### ENDANGERED ANIMALS  `endangered_animals`
- правило: What belongs to the group «Endangered Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !amur leopard, !kakapo, !vaquita, xsaola

### EUSOCIAL ANIMALS  `eusocial_animals`
- правило: What belongs to the group «Eusocial Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +ants, +bees, +mole rat, +termites

### EXTINCT ANIMALS  `extinct_animals`
- правило: Extinct animals and animal groups people recognize by name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~megalodon, ~pterodactyl, ~stegosaurus, ~trilobite, ~velociraptor, +brontosaurus, +dinosaur, +dodo, +kiwi, +mammoth, +mastodon, +raptor, +saber tooth, +triceratops, +tyrannosaurus, ?dinosaur, ?dodo, ?mammoth, ?saber tooth

### EXTINCT BIRDS  `extinct_birds`
- правило: What belongs to the group «Extinct Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +moa, +passenger pigeon, !auk, xhuia

### EXTINCT FLIGHTLESS BIRDS  `extinct_flightless_birds`
- правило: What belongs to the group «Extinct Flightless Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +dodo, +elephant bird, +moa, !great auk

### FAMOUS PETERS  `famous_peters`
- правило: What belongs to the group «Famous Peters» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +pan, +parker, +piper, +rabbit

### FARM ANIMALS  `farm_animals`
- правило: Animals commonly kept on an ordinary farm
- тип связи: `is_a`, базовая сложность 0.1
- слов: 27
- ~calf (calf_cow), ~duck (duck_bird), ~turkey (turkey_bird), +bull, +cat, +chicken, +cow, +dog, +donkey, +goat, +goose, +hen, +horse, +lamb, +mule, +ox, +pig, +rabbit, +rooster, +sheep, ?chicken, ?cow, ?goat, ?horse, ?pig, ?rooster, ?sheep

### POULTRY  `farm_bird_words`
- правило: Birds raised for meat or eggs on a farm
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +chick, +chicken, +duck (duck_bird), +goose, +guinea fowl, +hen, +pheasant, +pigeon, +quail, +rooster, +turkey (turkey_bird), !capon

### FARMYARD ANIMALS  `farmyard_animals`
- правило: What belongs to the group «Farmyard Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +donkey, +goat, +pig, +rooster

### FAST ANIMALS  `fast_animals`
- правило: What belongs to the group «Fast Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +cheetah, +falcon, +gazelle, !sailfish

### FEMALE ANIMALS  `female_animals`
- правило: What belongs to the group «Female Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +cow, +doe, +hen, +mare

### FICTIONAL CATS  `fictional_cats`
- правило: What belongs to the group «Fictional Cats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +cheshire, +Garfield, +Sylvester, +tom

### FISHING LOCATIONS  `fishing_locations`
- правило: What belongs to the group «Fishing Locations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +bay, +cove, +harbor, +lake

### FLIGHTLESS BIRDS  `flightless_birds`
- правило: What belongs to the group «Flightless Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +emu, +kiwi, +ostrich, +penguin

### FLUFFY ANIMALS  `fluffy_animals`
- правило: What belongs to the group «Fluffy Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +alpaca, +cat, +rabbit, +sheep

### FLYING ANIMALS  `flying_animals`
- правило: Animals that can fly under their own power
- тип связи: `has_property`, базовая сложность 0.2
- слов: 26
- +bat (bat_animal), +bee, +bluebird, +butterfly, +crow, +dragonfly, +duck (duck_bird), +eagle, +falcon, +goose, +hawk, +hornet, +hummingbird, +ladybug, +mosquito, +moth, +owl, +pelican, +pigeon, +robin, +seagull, +sparrow, +stork, +swan, +vulture, +wasp

### FLYING INSECTS  `flying_insects`
- правило: What belongs to the group «Flying Insects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 9
- +bee, +butterfly, +dragonfly, +firefly, +ladybug, +mosquito, +moth, !blowfly, !gnat

### FOREST ANIMALS  `forest_animals`
- правило: What belongs to the group «Forest Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 8
- +bear, +deer, +elk, +fox, +owl, +rabbit, +squirrel, +wolf

### FOUR LEGGED ANIMALS  `four_legged_animals`
- правило: What belongs to the group «Four Legged Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +armadillo, +cheetah, +elephant, +fox

### GARDEN INSECTS  `garden_insects`
- правило: What belongs to the group «Garden Insects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 7
- +bee, +cricket, +grasshopper, +ladybug, +moth, +worm, !aphid

### HARD WORKING ANIMALS  `hard_working_animals`
- правило: What belongs to the group «Hard Working Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +ant, +bee, +termite, !silkworm

### HATCHING ANIMALS  `hatching_animals`
- правило: What belongs to the group «Hatching Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +chicken, +dinosaur, +platypus, +snake

### HERALDIC ANIMALS  `heraldic_animals`
- правило: What belongs to the group «Heraldic Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +griffin, +unicorn, !cockatrice, !wyvern

### HOOVED ANIMALS  `hooved_animals`
- правило: What belongs to the group «Hooved Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +horse, +moose, +pig, +rhino

### HOPPING ANIMALS  `hopping_animals`
- правило: What belongs to the group «Hopping Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +hare, +kangaroo, +rabbit, +wallaby

### HORSE WORDS  `horse_words`
- правило: Words for kinds of horses and horse gear
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~groom (groom_horse), ~stirrup, +bridle, +canter, +colt, +foal, +gallop, +halter, +harness, +hoof, +jockey, +mane, +mare, +pony, +reins, +saddle, +stable, +stallion, +thoroughbred, +trot

### HOUSEHOLD PETS  `household_pets`
- правило: What belongs to the group «Household Pets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~budgie, +gerbil, +guinea pig, +tortoise

### HOUSING FOR ANIMALS  `housing_for_animals`
- правило: What belongs to the group «Housing For Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +aquarium, +barn, !birdcage, !terrarium

### BUGS  `insects`
- правило: Insects and other small bugs an average person recognizes
- тип связи: `is_a`, базовая сложность 0.15
- слов: 45
- ~aphid, ~cicada, ~gnat, ~silkworm, ~whitefly, ~woodlouse, +ant, +bee, +beetle, +butterfly, +caterpillar, +centipede, +cricket, +dragonfly, +firefly, +flea, +fly (fly_insect), +grasshopper, +hornet, +ladybug, +locust, +mantis, +mosquito, +moth, +roach, +scarab, +spider, +termite, +tick (tick_bug), +wasp, ?ant, ?aphid, ?bee, ?beetle, ?butterfly, ?cricket, ?dragonfly, ?firefly, ?ladybug, ?moth, ?roach, ?spider, ?termite, ?wasp, xwalkingstick

### JUMPING ANIMALS  `jumping_animals`
- правило: What belongs to the group «Jumping Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +cricket, +frog, +kangaroo, +rabbit

### JUNGLE ANIMAL  `jungle_animal`
- правило: What belongs to the group «Jungle Animal» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +jaguar, +monkey, +sloth, !toucan

### JUNGLE ANIMALS  `jungle_animals`
- правило: Animals that live in tropical jungles and rainforests
- тип связи: `found_in`, базовая сложность 0.2
- слов: 24
- ~macaw, ~tapir, ~toucan, +anteater, +boa, +chimpanzee, +frog, +gorilla, +iguana, +jaguar, +lemur, +leopard, +monkey, +orangutan, +panther, +parrot, +python, +sloth, +snake, +tiger, ?jaguar, ?monkey, ?parrot, ?tiger

### LADYBUG  `ladybug`
- правило: What belongs to the group «Ladybug» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +beetle, +garden, +red, +spotted

### LOCATION  `location`
- правило: What belongs to the group «Location» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 6
- +above, +area, +below, +beneath, +far, +near

### MALE ANIMALS  `male_animals`
- правило: What belongs to the group «Male Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 5
- +billy, +boar, +buck, +bull, +ram

### MAMMAL  `mammal`
- правило: What belongs to the group «Mammal» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 6
- +dolphin, +elephant, +lion, +monkey, +whale, +zebra

### MAMMALS  `mammals`
- правило: What belongs to the group «Mammals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 16
- +badger, +bear, +beaver, +bison, +dolphin, +elephant, +giraffe, +human, +jaguar, +lion, +otter, +rabbit, +rhino, +skunk, +walrus, +whale

### MARINE MAMMALS  `marine_mammals`
- правило: What belongs to the group «Marine Mammals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +dolphin, +manatee, +walrus, +whale, !dugong

### MIGRATING ANIMALS  `migrating_animals`
- правило: What belongs to the group «Migrating Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +bird, +butterfly, +caribou, +salmon

### MOUNTAIN ANIMALS  `mountain_animals`
- правило: What belongs to the group «Mountain Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 10
- +alpaca, +bighorn, +cougar, +eagle, +goat, +llama, +yak, !chamois, !ibex, !marmot

### MOVIE AWARD CATEGORIES  `movie_award_categories`
- правило: What belongs to the group «Movie Award Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +actor, +cinematography, +editing, +screenplay

### MOVIE CATEGORIES  `movie_categories`
- правило: What belongs to the group «Movie Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 5
- +animation, +documentary, +fantasy, +romance, +thriller

### NOBEL PRIZE CATEGORIES  `nobel_prize_categories`
- правило: What belongs to the group «Nobel Prize Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 5
- +chemistry, +literature, +medicine, +peace, +physics

### NOCTURNAL ANIMALS  `nocturnal_animals`
- правило: Animals that are active at night and rest during the day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 21
- ~armadillo, ~badger, ~bat (bat_animal), ~beaver, ~cougar, ~coyote, ~cricket, ~firefly, ~fox, ~hamster, ~hedgehog, ~leopard, ~mole (mole_animal), ~moth, ~mouse (mouse_animal), ~opossum, ~owl, ~porcupine, ~raccoon, ~skunk, ~wolf

### NON FLYING BIRDS  `non_flying_birds`
- правило: What belongs to the group «Non Flying Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +emu, +kiwi, +ostrich, +penguin

### OCEAN ANIMALS  `ocean_animals`
- правило: Animals that live in the ocean
- тип связи: `is_a`, базовая сложность 0.15
- слов: 30
- +barnacle, +clam, +coral, +crab, +dolphin, +eel, +jellyfish, +lobster, +manatee, +octopus, +orca, +oyster, +seahorse, +seal (seal_animal), +shark, +shrimp, +squid, +starfish, +stingray, +swordfish, +tuna, +turtle, +urchin, +walrus, +whale, ?crab, ?dolphin, ?octopus, ?shark, ?whale

### OCEAN MAMMALS  `ocean_mammals`
- правило: What belongs to the group «Ocean Mammals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +dolphins, +seals, +whales, !manatees

### OSCAR CATEGORIES  `oscar_categories`
- правило: What belongs to the group «Oscar Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 4
- +actor, +director, +picture, +screenplay

### PALINDROME ANIMALS  `palindrome_animals`
- правило: What belongs to the group «Palindrome Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +ara, +ewe, +pup, +tit

### PARTS OF ANIMALS  `parts_of_animals`
- правило: What belongs to the group «Parts Of Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +fur, +hoof, +paw, !forefoot

### PESTS  `pests`
- правило: Animals treated as household or garden pests
- тип связи: `is_a`, базовая сложность 0.35
- слов: 22
- ~aphid, +ant, +flea, +gopher, +insects, +mole (mole_animal), +mosquito, +moth, +mouse (mouse_animal), +pigeon, +raccoon, +rat, +roach, +rodents, +slug, +snail, +termite, +tick (tick_bug), +wasp, +weevil, !bedbug, !silverfish

### PET LIFE  `pet_life`
- правило: What belongs to the group «Pet Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +check up, +neutered, +tick med, +vaccines

### PET S FAVORITE  `pet_s_favorite`
- правило: What belongs to the group «Pet S Favorite» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +catnip, +scratching post, +squeaky toy, +treat

### PET SHOP  `pet_shop`
- правило: What belongs to the group «Pet Shop» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 5
- +aquarium, +cage, +carriers, +collar, +leash

### PET STORE  `pet_store`
- правило: What a pet store sells or keeps in stock
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- ~rodents, +birds, +cage, +kibble, +leash, +pets, +reptiles

### PETROLEUM  `petroleum`
- правило: What belongs to the group «Petroleum» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +diesel, +gasoline, +jet fuel, +kerosene

### PETS  `pets`
- правило: Animals commonly kept as household pets in the United States
- тип связи: `is_a`, базовая сложность 0.12
- слов: 32
- ~cockatiel, +axolotl, +bengal, +betta fish, +bird, +canary, +cat, +chinchilla, +dog, +ferret, +fish, +gerbil, +goldfish, +guinea pig, +hamster, +hedgehog, +iguana, +lizard, +mouse (mouse_animal), +parakeet, +parrot, +pony, +rabbit, +snake, +turtle, ?cat, ?dog, ?goldfish, ?guinea pig, ?hamster, ?parrot, ?rabbit

### PLACES TO SEE ANIMALS  `places_to_see_animals`
- правило: What belongs to the group «Places To See Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +farm, +safari, +wildlife, +zoo

### POND ANIMALS  `pond_animals`
- правило: Animals that live in or around a freshwater pond
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +beaver, +carp, +crayfish, +dragonfly, +duck (duck_bird), +fish, +frog, +goose, +heron, +mosquito, +newt, +otter, +salamander, +snail, +swan, +tadpole, +turtle, +water bug

### PREDATORY ANIMALS  `predatory_animals`
- правило: What belongs to the group «Predatory Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +panther, +polar bear, +shark, +wolf

### PUBLICATION  `publication`
- правило: What belongs to the group «Publication» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +copy, +edition, +issue, +print

### PUBLICATIONS  `publications`
- правило: What belongs to the group «Publications» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +article, +editorial, +essay, +review

### PUPPET  `puppet`
- правило: What belongs to the group «Puppet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +master, +show, +strings, +theater

### PUPPET THEATER  `puppet_theater`
- правило: What belongs to the group «Puppet Theater» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +curtain, +hand puppet, +stage, !marionette

### PUPPET THEATRE  `puppet_theatre`
- правило: What belongs to the group «Puppet Theatre» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +audience, +curtain, +Pinocchio, +puppeteer

### PUPPET TYPES  `puppet_types`
- правило: What belongs to the group «Puppet Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +marionette, +Shadow, +sock, !bunraku

### RABBIT BREEDS  `rabbit_breeds`
- правило: What belongs to the group «Rabbit Breeds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +angora, +Dutch, +lop, +Rex

### RARE BIRDS  `rare_birds`
- правило: What belongs to the group «Rare Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +albatross, !cassowary, !cormorant, !parakeet

### REPTILE  `reptile`
- правило: What belongs to the group «Reptile» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 7
- +crocodile, +gecko, +iguana, +lizard, +snake, +turtle, !whiptail

### REPTILES  `reptiles`
- правило: Cold-blooded scaly animals classed as reptiles
- тип связи: `is_a`, базовая сложность 0.25
- слов: 32
- ~caiman, ~skink, ~terrapin, +alligator, +anaconda, +boa, +chameleon, +cobra, +crocodile, +gecko, +iguana, +lizard, +lizards, +python, +rattlesnake, +snake, +snakes, +tortoise, +turtle, +turtles, +viper, ?crocodile, ?gecko, ?iguana, ?lizard, ?lizards, ?python, ?snake, ?tortoise, ?turtle, ?viper, !monitor (monitor_lizard)

### RIDEABLE ANIMALS  `rideable_animals`
- правило: What belongs to the group «Rideable Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +camels, +donkey, +elephant, +horse

### RIDING ANIMALS  `riding_animals`
- правило: What belongs to the group «Riding Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +camel, +donkey, +horse, +mule

### RIVER ANIMALS  `river_animals`
- правило: What belongs to the group «River Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +beaver, +crocodile, +hippopotamus, +otter

### RODENTS  `rodents`
- правило: Small gnawing mammals classed as rodents
- тип связи: `is_a`, базовая сложность 0.3
- слов: 31
- ~capybara, ~muskrat, +beaver, +bushy tail, +chinchilla, +chipmunk, +gerbil, +gopher, +groundhog, +guinea pig, +hamster, +mouse (mouse_animal), +porcupine, +prairie dog, +rat, +shrew, +squirrel, +vole, ?beaver, ?capybara, ?chinchilla, ?gerbil, ?gopher, ?guinea pig, ?hamster, ?muskrat, ?rat, ?squirrel, ?vole, !nutria, !rock cavy

### SAVAGE ANIMALS  `savage_animals`
- правило: What belongs to the group «Savage Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +bear, +crocodile, +mongoose, +wolverine

### SCAT  `scat`
- правило: What belongs to the group «Scat» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +beat, +scram, +shoo, !skedaddle, !vamoose

### SCATTER  `scatter`
- правило: What belongs to the group «Scatter» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +disperse, +spray, +spread, +strew

### SEA CREATURES  `sea_creatures`
- правило: What belongs to the group «Sea Creatures» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 15
- +clam, +coral, +crab, +dolphin, +jellyfish, +lobster, +mussel, +octopus, +oyster, +seahorse, +snapper, +squid, +starfish, +stingray, +whale

### SECRET COMMUNICATION  `secret_communication`
- правило: What belongs to the group «Secret Communication» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +cipher, +enigma, +invisible ink, +morse code

### SLOW ANIMALS  `slow_animals`
- правило: What belongs to the group «Slow Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +koala, +sloth, +snail, +turtle

### SONGBIRD  `songbird`
- правило: What belongs to the group «Songbird» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +finch, +lark, +thrush, +warbler

### STRIPED ANIMALS  `spotted_and_striped`
- правило: Animals whose coat has clear stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~badger, ~bee, ~chipmunk, ~hyena, ~raccoon, ~skunk, ~snake, ~tiger, ~wasp, ~zebra, !angelfish, !clownfish, !lemur, !okapi

### STAGE MAGIC CATEGORIES  `stage_magic_categories`
- правило: What belongs to the group «Stage Magic Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +restoration, +sleight, !mentalism, xescapology

### STARFISH  `starfish`
- правило: What belongs to the group «Starfish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +carnivore, +regeneration, +spines, +suction

### STINGING INSECTS  `stinging_insects`
- правило: What belongs to the group «Stinging Insects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +bees, +hornets, +wasps, !yellowjackets

### SWIFT ANIMALS  `swift_animals`
- правило: What belongs to the group «Swift Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +cheetah, +falcon, +horse, !sailfish

### TAROT CARD CATEGORIES  `tarot_card_categories`
- правило: What belongs to the group «Tarot Card Categories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +cups, +swords, +wands, !pentacles

### TRUMPET  `trumpet`
- правило: What belongs to the group «Trumpet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 6
- +bell, +brass, +fanfare, +mouthpiece, +slide, +valve

### TYPES OF ANIMALS  `types_of_animals`
- правило: What belongs to the group «Types Of Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +bird, +fish, +mammals, +reptiles

### TYPES OF BIRDS  `types_of_birds`
- правило: What belongs to the group «Types Of Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +finch, +robin, +wren, xcorvid

### UNDERGROUND ANIMALS  `underground_animals`
- правило: What belongs to the group «Underground Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gopher, +groundhog, +grub, +worm

### VENOMOUS ANIMALS  `venomous_animals`
- правило: What belongs to the group «Venomous Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +cobra, +hornet, +scorpion, +tarantula

### VIDEO GAME LOCATIONS  `video_game_locations`
- правило: What belongs to the group «Video Game Locations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +citadel, +forge, +outpost, +sanctuary

### WATER ANIMALS  `water_animals`
- правило: What belongs to the group «Water Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +beaver, +newt, +otter, +swan

### WATER BIRDS  `water_birds`
- правило: What belongs to the group «Water Birds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +albatross, +loon, +penguin, +seagull

### WATER PURIFICATION  `water_purification`
- правило: What belongs to the group «Water Purification» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +ceramic filter, +ion exchange, !distillate, !filtrate

### WILD ANIMALS  `wild_animals`
- правило: What belongs to the group «Wild Animals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +bear, +deer, +fox, +wolf

### WILD CATS  `wild_cats`
- правило: Wild members of the cat family
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~caracal, ~ocelot, ~serval, +bobcat, +cheetah, +cougar, +jaguar, +leopard, +lion, +lynx, +panther, +puma, +tiger, ?caracal, ?cheetah, ?cougar, ?jaguar, ?leopard, ?lion, ?lynx, ?tiger

### ZOO ANIMALS  `zoo_animals`
- правило: Animals commonly seen at an American zoo
- тип связи: `found_in`, базовая сложность 0.15
- слов: 31
- +bear, +camel, +cheetah, +elephant, +flamingo, +giraffe, +gorilla, +hippo, +kangaroo, +koala, +lemur, +lion, +monkey, +otter, +panda, +peacock, +penguin, +rhino, +seal (seal_animal), +sloth, +tapir, +tiger, +zebra, ?elephant, ?giraffe, ?gorilla, ?koala, ?monkey, ?penguin, ?tiger, ?zebra


## Тема: art

### ART STYLES  `art_styles`
- правило: Named styles of visual art
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~cubism, +abstract, +art deco, +baroque, +expressionism, +folk art, +gothic, +impressionism, +minimalism, +modernism, +pop art, +realism, +renaissance, +surrealism, ?abstract, ?baroque, ?cubism, ?impressionism, ?realism, ?surrealism

### ART TOOLS  `art_tools`
- правило: Tools an artist uses to make art
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~mold (mold_form), +airbrush, +brush, +canvas, +charcoal, +chisel, +easel, +kiln, +knife, +loom, +palette, +pen (pen_writing), +pencil, +roller, +sponge (sponge_cleaning), +stylus

### SHADES OF COLOR  `color_words_advanced`
- правило: Words for particular shades of color
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~lavender (lavender_color), ~mint (mint_color), ~sage (sage_color), +amber, +azure, +blush, +charcoal, +cobalt, +coral, +crimson, +ivory, +jade, +mauve, +mustard, +ochre, +olive, +plum, +rust, +scarlet, !cream (cream_color)

### CRAFTS  `crafts`
- правило: Handmade crafts people do as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 34
- ~basketry, ~beading, ~macrame, ~scrapbooking, +calligraphy, +candle, +candle making, +carpentry, +ceramics, +crochet, +embroidery, +glue stick, +knitting, +masonry, +origami, +paper, +popsicle stick, +pottery, +quilting, +scissors, +sculpture, +sewing, +soap making, +weaving, +woodworking, ?beading, ?knitting, ?macrame, ?origami, ?pottery, ?quilting, ?sewing, ?weaving, ?woodworking

### DECORATIONS  `decorative_things`
- правило: Things used to decorate a room or an event
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +balloon, +banner, +candle, +centerpiece, +curtain, +figurine, +garland, +lantern, +mobile, +mural, +ornament, +painting, +rug, +sculpture, +streamer, +tapestry, +vase, +wreath

### DRAWING WORDS  `drawing_words`
- правило: Words used when drawing a picture
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +blend, +contour, +curve, +doodle, +erase, +hatch, +highlight, +line (line_drawn), +outline, +perspective, +proportion, +shade, +silhouette, +sketch, +trace

### FAMOUS ARTWORKS  `famous_artworks`
- правило: Artworks most people can name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- +American Gothic, +David, +Girl with a Pearl Earring, +Last Supper, +Mona Lisa, +Starry Night, +Sunflowers, +The Scream, +The Thinker, +Venus de Milo, !Guernica

### JEWELRY SUPPLIES  `jewelry_making`
- правило: Things used to make jewelry
- тип связи: `used_in`, базовая сложность 0.4
- слов: 22
- ~bead, ~beads, ~chain, ~clasp, ~cord, ~flux, ~gem, ~hook (hook_fastener), ~pendant, ~pliers, ~ring blank, ~saw, ~setting, ~solder, ~thread, ~wire, ?clasp, ?pliers, ?solder, !crimps, !mandrel, !mold (mold_form)

### MUSEUM WORDS  `museum_words`
- правило: Things found in an art museum
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~docent, +admission, +audio tour, +collection, +curator, +exhibit, +frame, +gallery, +gift shop, +guide, +painting, +pedestal, +plaque, +portrait, +rope, +sculpture

### KINDS OF PAINT  `paint_types`
- правило: Kinds of paint used by artists and decorators
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~gouache, ~tempera, +acrylic, +chalk paint, +enamel, +finger paint, +latex, +primer, +spray, +varnish, +watercolor, ?acrylic, ?enamel, ?tempera, ?watercolor, !oil (oil_paint)

### PHOTO SUBJECTS  `photography_styles`
- правило: Kinds of pictures a photographer takes
- тип связи: `is_a`, базовая сложность 0.35
- слов: 17
- +action shot, +aerial, +candid, +close up, +group shot, +landscape, +macro, +panorama, +portrait, +selfie, +silhouette, +still life, +street, +wedding photo, ?aerial, ?macro, ?portrait

### POTTERY WORDS  `pottery_words`
- правило: Things used in making pottery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bowl, ~clay, ~fire, ~glaze, ~kiln, ~mold (mold_form), ~plaster, ~pot, ~sculpt, ~slip, ~tile, ~vase, ~wheel, !trim (trim_cut)

### SCULPTURE MATERIALS  `sculpture_materials`
- правило: Materials sculptors carve or cast
- тип связи: `made_of`, базовая сложность 0.35
- слов: 23
- ~soapstone, +alabaster, +bronze, +clay, +concrete, +glass, +granite, +ice, +limestone, +marble (marble_stone), +metal, +plaster, +sand, +sandstone, +stone, +terracotta, +wax (wax_substance), +wood, ?bronze, ?clay, ?granite, ?plaster, ?stone

### TEXTURES  `textures`
- правило: Words describing how a surface feels
- тип связи: `is_a`, базовая сложность 0.4
- слов: 26
- ~bumpy, ~chewy, ~coarse, ~crispy, ~crunchy, ~Fluffy, ~fuzzy, ~glossy, ~grainy, ~matte, ~polished, ~prickly, ~ridged, ~rough, ~silky, ~slick, ~smooth, ~soft, ~sticky, ~velvet, ~velvety, ?bumpy, ?rough, ?silky, ?smooth, ?sticky

### PERFORMING ARTS  `theater_arts`
- правило: Arts performed in front of an audience
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~puppetry, +ballet, +circus, +comedy, +concert, +dance, +improv, +magic, +mime, +musical, +opera, +play, +poetry reading, +recital


## Тема: business

### ADVERTISING WORDS  `advertising_words`
- правило: Words used in advertising and marketing
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +ad, +banner, +billboard, +brand (brand_company), +campaign, +commercial, +coupon, +endorsement, +flyer, +jingle, +logo, +mascot, +promo, +slogan, +sponsor, +tagline

### BANKING WORDS  `banking_words`
- правило: Words used at a bank
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~branch (branch_office), ~pin (pin_code), +account, +ATM, +balance, +check (check_payment), +deposit, +interest, +ledger, +loan, +mortgage, +overdraft, +safe deposit, +statement, +teller, +transfer, +vault, +withdrawal

### BUSINESS WORDS  `business_words`
- правило: Words used in running a business
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +asset, +budget, +client, +contract, +expense, +franchise, +inventory, +invoice, +loss, +market, +merger, +partner, +payroll, +profit, +quota, +revenue, +startup, +stock, +vendor, !brand (brand_company)

### CAR BRANDS  `car_brands`
- правило: Car manufacturers sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Audi, +BMW, +Buick, +Chevrolet, +Dodge, +Ferrari, +ford (ford_brand), +Honda, +Hyundai, +Jeep, +Kia, +Lexus, +Mazda, +Mercedes, +Nissan, +Subaru, +Tesla, +Toyota, +Volkswagen, +Volvo, ?Audi, ?BMW, ?Honda, ?Lexus, ?Toyota

### US MONEY  `coins_and_bills`
- правило: Coins and bills used in the United States
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- +bill (bill_money), +cent, +coin, +dime, +dollar, +fifty, +five, +half dollar, +hundred, +nickel, +penny, +quarter (quarter_coin), +ten, +twenty, !note (note_money)

### CURRENCIES  `currencies`
- правило: Names of national currencies
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~krona, ~shekel, +baht, +dinar, +dollar, +euro, +franc, +lira, +peso, +pound (pound_money), +real, +ruble, +rupee, +won, +yen

### FAMOUS BRANDS  `famous_brands`
- правило: Brand names most Americans recognize
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~Crayola, ~ford (ford_brand), +Adidas, +Chevrolet, +Coca Cola, +Colgate, +Disney, +Gillette, +Harley, +Hershey, +Kellogg, +Kodak, +Lego, +Levi, +McDonalds, +Nestle, +Nike, +Pepsi

### CONTRACT WORDS  `insurance_and_legal`
- правило: Words used in contracts and agreements
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~agreement, ~breach, ~claim, ~clause, ~deductible, ~liability, ~notice, ~policy, ~premium, ~renewal, ~signature, ~term (term_condition), ~waiver, ~witness

### JOB HUNTING  `job_hunting`
- правило: Words used when looking for a job
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +application, +benefits, +contract, +cover letter, +hire, +interview, +offer, +opening, +orientation, +portfolio, +position, +recruiter, +reference, +resume, +salary, +screening

### MAIL WORDS  `mail_words`
- правило: Things involved in sending mail
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- +address, +carrier, +courier, +envelope, +label, +letter (letter_mail), +mailbox, +package, +parcel, +post office, +postage, +postcard, +return address, +stamp (stamp_postage), +tracking, +zip code

### MONEY WORDS  `money_words`
- правило: Everyday English words for money, payments and personal finance
- тип связи: `is_a`, базовая сложность 0.25
- слов: 27
- +allowance, +bank (bank_finance), +bill (bill_money), +bonus, +budget, +capital (capital_money), +cash, +change, +check (check_payment), +coin, +credit, +debit, +debt, +deposit, +fee, +interest, +invoice, +loan, +receipt, +refund, +rent, +salary, +savings, +tax, +tip (tip_money), +wage, +wallet

### OFFICE WORDS  `office_words`
- правило: Things and routines found in an office workplace
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- +badge, +boss, +break room, +calendar, +conference call, +copier, +cubicle, +deadline, +desk, +inbox, +intern, +meeting, +memo, +overtime, +printer, +shift (shift_work), +spreadsheet, +water cooler

### RESTAURANT WORDS  `restaurant_words`
- правило: Things and roles found at a restaurant
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~bar (bar_pub), ~bill (bill_money), ~tip (tip_money), +appetizer, +booth, +buffet, +chef, +counter, +dessert, +entree, +host (host_person), +kitchen, +menu, +napkin, +order, +receipt, +reservation, +special, +table, +waiter

### SHOPPING WORDS  `shopping_words`
- правило: Words used while shopping in a store
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~tag (tag_label), +aisle, +bag, +barcode, +basket, +cart, +cashier, +checkout, +clearance, +coupon, +discount, +price, +receipt, +refund, +register, +sale, +shelf (shelf_furniture), !line (line_queue)

### STARTUP WORDS  `startup_words`
- правило: Words used when starting a new company
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~equity, ~founder, ~funding, ~incubator, ~investor, ~launch, ~pitch (pitch_present), ~prototype, ~runway, ~seed round, ~valuation, ~venture, !cofounder, !scale (scale_grow)

### KINDS OF STORES  `store_types`
- правило: Kinds of shops found in a town or mall
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- +bakery, +barbershop, +bookstore, +boutique, +butcher, +cafe, +deli, +florist, +gift shop, +grocery, +hardware store, +jeweler, +market, +newsstand, +pet shop, +pharmacy, +salon, +shoe store, +thrift store, +toy store

### TECH COMPANIES  `tech_companies`
- правило: Well-known technology companies or consumer technology brands
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- +Adobe, +Amazon, +apple (apple_company), +Cisco, +Dell, +Google, +IBM, +Intel, +Microsoft, +Netflix, +Nintendo, +Nvidia, +Oracle, +PayPal, +Qualcomm, +Samsung, +Sony, +Spotify, +Tesla, +Uber, +Zoom


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
- слов: 16
- +Big Apple, +Big Easy, +City of Angels, +Emerald City, +Mile High City, +Motor City, +Music City, +Queen City, +Sin City, +Steel City, +Windy City, ?Emerald City, ?Motor City, ?Sin City, ?Windy City, !Beantown

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


## Тема: farming

### BARN THINGS  `barn_things`
- правило: Things found inside a barn
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~gate (gate_barrier), ~sack (sack_bag), +bale, +bucket, +feed, +harness, +hay, +lantern, +loft, +milking stool, +pitchfork, +rope, +saddle, +shovel, +stall (stall_barn), +trough

### BEEKEEPING THINGS  `beekeeping`
- правило: Things used in beekeeping
- тип связи: `used_in`, базовая сложность 0.4
- слов: 21
- ~queen (queen_bee), +apiary, +comb, +drone, +extractor, +frame, +gloves, +hive, +honey, +nectar, +pollen, +smoker, +super, +swarm, +veil, +wax (wax_substance), +worker, ?drone, ?hive, ?honey, ?smoker

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


## Тема: geography

### AFRICA CAPITALS  `africa_capitals`
- правило: What belongs to the group «Africa Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +abuja, +Addis Ababa, +Cairo, +Nairobi

### AFRICAN COUNTRIES  `african_countries`
- правило: Countries located in Africa
- тип связи: `is_a`, базовая сложность 0.35
- слов: 28
- +Algeria, +Angola, +Botswana, +burkina faso, +burundi, +Chad, +Congo, +Egypt, +Ethiopia, +Ghana, +Kenya, +Libya, +Morocco, +Namibia, +Nigeria, +Rwanda, +Senegal, +Somalia, +Sudan, +Tanzania, +Tunisia, +Uganda, +Zambia, ?Angola, ?Botswana, ?Egypt, ?Ghana, ?Kenya

### AMERICAN STATES  `american_states`
- правило: What belongs to the group «American States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Alaska, +Arkansas, +Delaware, +Florida

### ANCIENT GREEK CITY STATES  `ancient_greek_city_states`
- правило: What belongs to the group «Ancient Greek City States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +Athens, +corinth, +Sparta, +thebes

### ANCIENT LANDMARKS  `ancient_landmarks`
- правило: What belongs to the group «Ancient Landmarks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Colosseum, +Parthenon, +pyramids, +Stonehenge

### ANCIENT STATES  `ancient_states`
- правило: What belongs to the group «Ancient States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +Babylon, +Carthage, +Egypt, +Rome

### ASIAN COUNTRIES  `asian_countries`
- правило: Countries located in Asia
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~turkey (turkey_country), +Bangladesh, +Cambodia, +China, +India, +Indonesia, +Iran, +Israel, +Japan, +Jordan, +Korea, +Laos, +Malaysia, +Mongolia, +Nepal, +Pakistan, +Philippines, +Singapore, +Thailand, +Vietnam, ?China, ?Japan, ?Korea, ?Vietnam

### CAPITAL  `capital`
- правило: What belongs to the group «Capital» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 8
- +abuja, +algiers, +Amsterdam, +Ankara, +Berlin, +Ottawa, +Paris, +Tokyo

### CAPITAL CITIES  `capital_cities`
- правило: What belongs to the group «Capital Cities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 8
- +Berlin, +Brasilia, +Canberra, +London, +Nairobi, +Ottawa, +Paris, +Tokyo

### CAPITALS  `capitals`
- правило: What belongs to the group «Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 11
- +Beijing, +Budapest, +Cairo, +Canberra, +Copenhagen, +London, +new delhi, +Paris, +Prague, +Pretoria, +Tokyo

### CARIBBEAN ISLANDS  `caribbean_islands`
- правило: What belongs to the group «Caribbean Islands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +Barbados, +Cuba, +Jamaica, +Trinidad

### CITY  `city`
- правило: What belongs to the group «City» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 13
- +Berlin, +Cairo, +Chicago, +Dallas, +Denver, +Florence, +Istanbul, +London, +new york, +newyork, +Paris, +Richmond, +Tokyo

### CITY BUILDINGS  `city_buildings`
- правило: What belongs to the group «City Buildings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 6
- +hospital, +library, +museum, +post office, +stadium, +town hall

### CITY ENTERTAINMENT  `city_entertainment`
- правило: What belongs to the group «City Entertainment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +circus, +opera, +stadium, +zoo

### CITY EVENTS  `city_events`
- правило: What belongs to the group «City Events» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +festival, +marathon, +parade, +rally

### CITY PLANNING  `city_planning`
- правило: What belongs to the group «City Planning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +parking, +transportation, +venues, +zoning

### CITY TRANSPORTATION  `city_transportation`
- правило: What belongs to the group «City Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +bus, +Subway, +taxi, +tram

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

### CROWDED LANDMARKS  `crowded_landmarks`
- правило: What belongs to the group «Crowded Landmarks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +piccadilly circus, +shibuya crossing, +Times Square, +trafalgar square

### CROWDED PLACES  `crowded_places`
- правило: What belongs to the group «Crowded Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +beach, +concert, +mall, +market

### CULTURAL PLACES  `cultural_places`
- правило: What belongs to the group «Cultural Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +gallery, +museum, +opera, +theater

### DESERTS  `deserts_and_wild_places`
- правило: Major deserts of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~Atacama, ~Sonoran, +Arabian, +Death Valley, +Gobi, +Great Basin, +Kalahari, +Mojave, +Painted Desert, +Sahara

### DIRECTIONS  `directions`
- правило: Words used to give directions
- тип связи: `is_a`, базовая сложность 0.2
- слов: 28
- +across, +around, +back, +backward, +behind, +beside, +down, +east, +far, +forward, +left, +near, +north, +over, +right, +south, +straight, +through, +under, +up, +west, ?back, ?down, ?east, ?forward, ?left, ?right, ?up

### ELECTRICITY  `electricity`
- правило: What belongs to the group «Electricity» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 9
- +ampere, +battery, +bulb, +ohm, +resistance, +voltage, +Watt, +wire, !ammeter

### EUROPEAN CAPITALS  `european_capitals`
- правило: What belongs to the group «European Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +Berlin, +Madrid, +Paris, +Rome

### EUROPEAN COUNTRIES  `european_countries`
- правило: Countries located in Europe
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- +Austria, +Belgium, +Bulgaria, +Croatia, +Denmark, +Estonia, +Finland, +France, +Germany, +Greece, +Hungary, +Iceland, +Ireland, +Italy, +Netherlands, +Norway, +Poland, +Portugal, +Romania, +Scotland, +Serbia, +Slovakia, +Spain, +Sweden, +Switzerland

### EUROPEAN MICROSTATES  `european_microstates`
- правило: What belongs to the group «European Microstates» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Andorra, +liechtenstein, +Monaco, +san marino

### FAMOUS LANDMARKS  `famous_landmarks`
- правило: World landmarks most people can recognize
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- +Acropolis, +Big Ben, +Colosseum, +Eiffel Tower, +Empire State, +Golden Gate, +Great Wall, +Leaning Tower, +Mount Rushmore, +pyramid (pyramid_monument), +sphinx, +Statue of Liberty, +Stonehenge, +Taj Mahal, +White House, ?Acropolis, ?Big Ben, ?Colosseum, ?Eiffel Tower, ?sphinx, ?Taj Mahal

### FANTASY MAP  `fantasy_map`
- правило: What belongs to the group «Fantasy Map» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +castle, +cave, +forest, +swamp

### FASHION CAPITALS  `fashion_capitals`
- правило: What belongs to the group «Fashion Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.14
- слов: 5
- +London, +Milan, +new york, +Paris, +Tokyo

### FIREPLACE  `fireplace`
- правило: What belongs to the group «Fireplace» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 10
- +ash, +brick, +chimney, +fire, +firewood, +flame, +log, +logs, +mantel, +matches

### FLAG  `flag`
- правило: What belongs to the group «Flag» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +banner, +cloth, +color, +Stripe

### GEOGRAPHY CLASS  `geography_class`
- правило: What you are asked to name or point at in a geography lesson
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- +atlas (atlas_book), +globe, +islands, +lakes, +latitude, +rivers, +seas

### GREEK ISLANDS  `greek_islands`
- правило: What belongs to the group «Greek Islands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +corfu, +Crete, +mykonos, +rhodes

### HAUNTED PLACES  `haunted_places`
- правило: What belongs to the group «Haunted Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 6
- +asylum, +catacomb, +crypt, +graveyard, +house, +mansion

### HOT PLACES  `hot_places`
- правило: Places that are typically hot
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~attic, ~campfire, ~desert, ~equator, ~furnace, ~greenhouse, ~jungle, ~kitchen, ~oven, ~sauna, ~tropics, ~volcano, +beach, +engine, +sun

### ISLAND  `island`
- правило: What belongs to the group «Island» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +Bali, +Ibiza, +Maui, +Sicily

### ISLAND COUNTRIES  `island_countries`
- правило: What belongs to the group «Island Countries» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +Iceland, +Japan, +Maldives, +New Zealand

### ISLAND GETAWAYS  `island_getaways`
- правило: What belongs to the group «Island Getaways» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +Bahamas, +Bali, +Fiji, +Maldives

### ISLAND STATES  `island_states`
- правило: What belongs to the group «Island States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +Cyprus, +Iceland, +Indonesia, +Jamaica

### ISLANDS  `islands`
- правило: Well known islands around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 28
- ~rottnest, +Bali, +Barbados, +Bermuda, +Crete, +Cuba, +Cyprus, +Fiji, +Greenland, +Hawaii, +Iceland, +Jamaica, +java, +Madagascar, +Maldives, +Malta, +Sardinia, +Sicily, +Tahiti, ?Bali, ?Crete, ?Cuba, ?Fiji, ?Hawaii, ?Iceland, ?Jamaica, ?Malta, ?Sicily

### LANDFORMS  `landforms`
- правило: Natural features of the land surface
- тип связи: `is_a`, базовая сложность 0.3
- слов: 43
- ~delta (delta_river), +basin, +butte, +canyon, +cave, +cliff, +crater, +desert, +dune, +foothill, +glacier, +gorge, +hill, +island, +islands, +isthmus, +marsh, +mesa, +mountain, +mountains, +ocean, +peninsula, +plain, +plateau, +prairie, +ridge, +rivers, +summit, +tundra, +valley, +valleys, +volcano, +volcanoes, ?butte, ?canyon, ?cliff, ?island, ?isthmus, ?mesa, ?mountain, ?peninsula, ?plateau, ?valley

### LANDMARK  `landmark`
- правило: What belongs to the group «Landmark» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +Eiffel Tower, +Great Wall, +Statue of Liberty, +Taj Mahal

### LANDMARK YEARS  `landmark_years`
- правило: What belongs to the group «Landmark Years» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +1776, +1945, +1969, !1492

### LANDMARKS  `landmarks`
- правило: What belongs to the group «Landmarks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 13
- +castle, +Colosseum, +Eiffel Tower, +Great Wall, +Parthenon, +pyramids, +statue, +Statue of Liberty, +Stonehenge, +tower, +towers, !Machu Picchu, !sagrada fam lia

### LATIN AMERICA  `latin_american_countries`
- правило: Countries of Central and South America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +Argentina, +Belize, +Bolivia, +Brazil, +Chile, +Colombia, +Costa Rica, +Cuba, +Ecuador, +Guatemala, +Honduras, +Mexico, +Nicaragua, +panama, +Paraguay, +Peru, +Uruguay, +Venezuela

### MAP  `map`
- правило: What belongs to the group «Map» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +area, +Australia, +borders, +chart

### MAP LEGEND  `map_legend`
- правило: What a map marks with a symbol or a colour
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- ~biomes, ~volcanoes, ~waterfalls, +contour, +landforms, +scale (scale_ratio), +symbol

### MAP PROJECTIONS  `map_projections`
- правило: What belongs to the group «Map Projections» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +cylindrical, +lambert conformal, +peters, +planar, !azimuthal, !conic, !mercator

### MAP TYPES  `map_types`
- правило: What belongs to the group «Map Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.14
- слов: 4
- +climate, +physical, +political, +topographic

### MAP WORDS  `map_words`
- правило: Words used to read and describe a map
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~key (key_legend), ~scale (scale_ratio), +atlas (atlas_book), +border, +compass, +contour, +coordinate, +east, +elevation, +globe, +grid, +latitude, +legend, +longitude, +meridian, +north, +route, +south, +symbol, +west

### MAPLE  `maple`
- правило: What belongs to the group «Maple» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 9
- +Autumn, +canada, +emblem, +leaf, +sap, +sugar, +syrup, +Vermont, +wood

### MARKED ON MAPS  `marked_on_maps`
- правило: What belongs to the group «Marked On Maps» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +border, +capital cities, +mining, +relief

### MARKETPLACE  `marketplace`
- правило: What belongs to the group «Marketplace» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +auction, +bazaar, +retail, +trade

### MOUNTAIN RANGES  `mountain_ranges`
- правило: Major mountain ranges of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~Appalachians, ~Carpathians, +Alps, +Andes, +Cascades, +Himalayas, +Ozarks, +Pyrenees, +Rockies, +Sierra Nevada, +Urals, ?Alps, ?Andes, ?Himalayas, ?Rockies, !atlas (atlas_mountains)

### PARK WORDS  `national_parks`
- правило: Things found in a national park or campground
- тип связи: `found_in`, базовая сложность 0.3
- слов: 26
- +Acadia, +bear box, +cabin (cabin_house), +campfire, +campsite, +canyon, +Everglades, +geyser, +glacier, +Grand Canyon, +lantern, +lodge, +map, +overlook, +path, +picnic table, +Ranger, +sequoia, +tent, +trail, +visitor center, +waterfall, +wildlife, +Yellowstone, +Yosemite, +Zion

### NEW YORK CITY  `new_york_city`
- правило: What belongs to the group «New York City» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Broadway, +bronx, +Brooklyn, +manhattan

### PARKING PLACES  `parking_places`
- правило: What belongs to the group «Parking Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +bus stop, +garage, +hangar, +helipad

### PLACES  `places`
- правило: What belongs to the group «Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +city, +Hamlet, +town, +village

### PLACES IN ITALY  `places_in_italy`
- правило: What belongs to the group «Places In Italy» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +basilica, +Pompeii, +san marco, +Tuscany

### PLACES TO SOCIALIZE  `places_to_socialize`
- правило: What belongs to the group «Places To Socialize» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +dance floor, +dating site, +forum, +study group

### PLACES TO VISIT  `places_to_visit`
- правило: What belongs to the group «Places To Visit» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 6
- +aquarium, +city hall, +library, +movie house, +museum, +zoo

### WAITING PLACES  `places_you_wait`
- правило: Places where people commonly stand in line
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~amusement park, ~buffet, ~checkout, ~DMV, ~grocery store, ~pharmacy, ~theater, ~ticket booth, +airport, +bus stop, +doctor office, +post office, +restaurant, !bank (bank_finance)

### PSYCHOLOGICAL STATES  `psychological_states`
- правило: What belongs to the group «Psychological States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +emotions, +feelings, +instincts, +moods

### QUANTUM STATES  `quantum_states`
- правило: What belongs to the group «Quantum States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +coherent, +entangled, +superposition, !superfluid

### QUIET PLACES  `quiet_places`
- правило: Places where people are expected to stay quiet
- тип связи: `has_property`, базовая сложность 0.35
- слов: 12
- ~cemetery, ~classroom, ~courtroom, ~exam room, ~funeral, ~monastery, ~theater, +church, +hospital, +library, +museum, +study hall

### REAL ESTATE  `real_estate`
- правило: What belongs to the group «Real Estate» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +manor, +plot, +ranch, +villa

### REPLACEMENT  `replacement`
- правило: What belongs to the group «Replacement» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 7
- +backup, +copy, +cover, +extra, +relief, +spare, +substitute

### RIVERS  `rivers`
- правило: Major rivers of the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- ~amur, +Amazon, +Colorado, +Congo, +Danube, +Euphrates, +Ganges, +Hudson, +Mississippi, +Missouri, +Nile, +Rhine, +Rio Grande, +Seine, +stream, +Thames, +Volga, +Yangtze, ?Amazon, ?Colorado, ?Nile

### SHOPPING PLACES  `shopping_places`
- правило: What belongs to the group «Shopping Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +boutique, +mall, +market, +shop

### SITTING PLACES  `sitting_places`
- правило: What belongs to the group «Sitting Places» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +bean bag, +chair, +stool, +swing

### SLAVIC CAPITALS  `slavic_capitals`
- правило: What belongs to the group «Slavic Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +bratislava, +Moscow, +Prague, +Warsaw

### SOUTH AMERICA CAPITALS  `south_america_capitals`
- правило: What belongs to the group «South America Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +Bogota, +Buenos Aires, +Lima, +Santiago

### STATE ABBREVIATIONS  `state_abbreviations`
- правило: What belongs to the group «State Abbreviations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +co, +ma, +ny, +pa

### STATES  `states`
- правило: What belongs to the group «States» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Arizona, +Nebraska, +Oregon, +Wyoming

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

### TREASURE MAP  `treasure_map`
- правило: What belongs to the group «Treasure Map» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 5
- +island, +legend, +route, +x, +x mark

### TYPES OF FLAGS  `types_of_flags`
- правило: What belongs to the group «Types Of Flags» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +banner, +jolly roger, +national flag, +race flag

### US CITIES  `us_cities`
- правило: Large cities in the United States
- тип связи: `is_a`, базовая сложность 0.25
- слов: 24
- +Atlanta, +Austin, +Baltimore, +Boston, +Charlotte, +Chicago, +Cleveland, +Dallas, +Denver, +Detroit, +Houston, +Memphis, +Miami, +Milwaukee, +Nashville, +Orlando, +Philadelphia, +phoenix (phoenix_city), +Portland, +Raleigh, +santa cruz, +Seattle, ?Miami, ?Nashville

### US STATE CAPITALS  `us_state_capitals`
- правило: What belongs to the group «Us State Capitals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +Austin, +Boston, +Denver, +Richmond

### US STATES  `us_states`
- правило: States of the United States of America
- тип связи: `is_a`, базовая сложность 0.2
- слов: 32
- +Alabama, +Alaska, +Arizona, +Arkansas, +California, +Colorado, +Delaware, +Florida, +Georgia, +Hawaii, +idaho (idaho_state), +Indiana, +Iowa, +Kansas, +Kentucky, +Maine, +Michigan, +Montana, +Nebraska, +Nevada, +Ohio, +Oregon, +Texas, +Utah, +Vermont, +Virginia, +Wyoming, ?Alabama, ?Alaska, ?Arizona, ?Nevada, ?Oregon

### WORKPLACE SOFT SKILLS  `workplace_soft_skills`
- правило: What belongs to the group «Workplace Soft Skills» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +creativity, +diligence, +empathy, +initiative

### WORLD CAPITALS  `world_capitals`
- правило: Capital cities of countries around the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +Amsterdam, +Athens, +Bangkok, +Beijing, +Berlin, +Budapest, +Cairo, +Dublin, +Havana, +Helsinki, +Lima, +Lisbon, +London, +Madrid, +Moscow, +Nairobi, +Oslo, +Ottawa, +Paris, +Prague, +Rome, +Seoul, +Tokyo, +Vienna, +Warsaw

### WORLD LANDMARKS  `world_landmarks`
- правило: What belongs to the group «World Landmarks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +Angkor Wat, +Big Ben, +Great Wall, +Stonehenge


## Тема: home

### APPLIANCES FOR THE HOME  `appliances_for_the_home`
- правило: What belongs to the group «Appliances For The Home» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +kettle, +oven, +stove, +toaster

### ARCHAEOLOGICAL TOOLS  `archaeological_tools`
- правило: What belongs to the group «Archaeological Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +plumb, +sieve, !theodolite, !trowel

### ASTRONOMY TOOLS  `astronomy_tools`
- правило: What belongs to the group «Astronomy Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +quadrant, +spectrometer, +telescope, !astrolabe, !photometer, !sextant, !spectroscope

### BABY THINGS  `baby_things`
- правило: Things used to care for a baby
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- ~highchair, ~monitor (monitor_medical), ~playpen, ~teether, +bib, +blanket, +bottle, +car seat, +cradle, +crib, +diaper, +formula, +onesie, +pacifier, +rattle (rattle_toy), +stroller, +swing, +wipes

### BAKING TOOLS  `baking_tools`
- правило: What belongs to the group «Baking Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 6
- +mixer, +rolling pin, +spatula, +timer, +whisk, !sifter

### BATHROOM  `bathroom`
- правило: What belongs to the group «Bathroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 8
- +basin, +mirror, +razor, +shampoo, +shower, +soap, +tile, +towel

### BATHROOM CABINET  `bathroom_cabinet`
- правило: What belongs to the group «Bathroom Cabinet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +floss, +lotion, +medicine, +toothpaste

### BATHROOM COUNTER  `bathroom_counter`
- правило: What belongs to the group «Bathroom Counter» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +lotion, +razor, +soap, +toothbrush

### BATHROOM ITEMS  `bathroom_items`
- правило: Objects normally found in a home bathroom
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- ~cabinet (cabinet_furniture), +bathtub, +brush, +comb, +curtain, +faucet, +floss, +hairdryer, +lotion, +mat, +mirror, +plunger, +razor, +robe, +shampoo, +shower, +sink (sink_basin), +soap, +sponge (sponge_cleaning), +tissue (tissue_paper), +toilet, +toothbrush, +toothpaste, +towel, !scale (scale_weigh)

### BEDROOM  `bedroom`
- правило: What belongs to the group «Bedroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 13
- +bed, +blanket, +book, +Charger, +clock, +closet, +dresser, +lamp, +mirror, +pillow, +sheets, +sleep, +wardrobe

### BEDROOM FURNITURE  `bedroom_furniture`
- правило: What belongs to the group «Bedroom Furniture» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +armchair, +nightstand, +vanity, +wardrobe

### BEDROOM THINGS  `bedroom_things`
- правило: Objects normally found in a bedroom
- тип связи: `found_in`, базовая сложность 0.2
- слов: 21
- +alarm clock, +bed, +blanket, +chest (chest_box), +closet, +comforter, +curtain, +dresser, +hamper, +hanger, +lamp, +mattress, +mirror, +nightstand, +pajamas, +pillow, +quilt, +rug, +sheet (sheet_bed), +slipper, !key (key_lock)

### BREAKROOM  `breakroom`
- правило: What belongs to the group «Breakroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +cooler, +small talk, +snacks, +table

### CALLIGRAPHY TOOLS  `calligraphy_tools`
- правило: What belongs to the group «Calligraphy Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 6
- +brush, +ink, +nib, +parchment, +reed, xinkstone

### CARPENTRY TOOLS  `carpentry_tools`
- правило: What belongs to the group «Carpentry Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 5
- +brace, +chisel, +hammer, +saw, +timber

### CHOPPING TOOLS  `chopping_tools`
- правило: What belongs to the group «Chopping Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +cleaver, +hatchet, +machete, !adze

### CLASSROOM ITEMS  `classroom_items`
- правило: What belongs to the group «Classroom Items» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +chalkboard, +crayons, +desk, +notebook

### CLEANING  `cleaning`
- правило: What belongs to the group «Cleaning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 6
- +bleach, +broom, +duster, +mop, +solvent, +vacuum

### CLEANING ITEMS  `cleaning_items`
- правило: What belongs to the group «Cleaning Items» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +broom, +brush, +duster, +mop

### CLEANING SUPPLIES  `cleaning_supplies`
- правило: Tools and products used to clean a house
- тип связи: `used_in`, базовая сложность 0.2
- слов: 20
- ~scrubber, ~squeegee, +bleach, +broom, +brush, +bucket, +cleanser, +detergent, +disinfectant, +duster, +dustpan, +gloves, +mop, +polish (polish_product), +rag, +soap, +sponge (sponge_cleaning), +trash bag, +vacuum, +wipes

### COFFEE TOOLS  `coffee_tools`
- правило: What belongs to the group «Coffee Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +filter, +grinder, +tamper, !frother

### COURTROOM DRAMA  `courtroom_drama`
- правило: What belongs to the group «Courtroom Drama» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +bailiff, +gavel, +jury, +verdict

### COZY ROOM  `cozy_room`
- правило: What belongs to the group «Cozy Room» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +chair, +fireplace, +rug, +sofa

### DENTAL TOOLS  `dental_tools`
- правило: What belongs to the group «Dental Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +dental drill, +dental mirror, +excavator, +forceps

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

### DIY TOOLS  `diy_tools`
- правило: What belongs to the group «Diy Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +glue gun, +glue stick, +safety goggles, +sandpaper

### DOCTORS TOOLS  `doctors_tools`
- правило: What belongs to the group «Doctors Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +reflex hammer, +stethoscope, +syringe, xotoscope

### DRAFTING TOOLS  `drafting_tools`
- правило: What belongs to the group «Drafting Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +blueprint, +compass, +stencil, +t square

### EVENING AT HOME  `evening_at_home`
- правило: What belongs to the group «Evening At Home» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +bathroom items, +book, +chess, +cinema

### HOME TEXTILES  `fabrics_at_home`
- правило: Cloth things used around the house
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- +apron (apron_garment), +blanket, +comforter, +curtain, +cushion cover, +doormat, +drape, +napkin, +pillowcase, +quilt, +rug, +sheet (sheet_bed), +tablecloth, +throw, +towel, !dishcloth, !placemat

### FARM TOOLS  `farm_tools`
- правило: What belongs to the group «Farm Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +bucket, +pitchfork, +rake, +shovel

### FUNHOUSE  `funhouse`
- правило: What belongs to the group «Funhouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 5
- +clown, +maze, +mirrors, +startle, +tunnel

### FURNITURE  `furniture`
- правило: Movable household furniture
- тип связи: `is_a`, базовая сложность 0.12
- слов: 54
- ~cabinet (cabinet_furniture), ~credenza, ~loveseat, +armchair, +armoire, +bed, +bedside table, +bench (bench_seat), +bookshelf, +buffet, +bureau, +chair, +chaise, +cot, +couch, +crib, +desk, +dining table, +drawer, +dresser, +fainting couch, +folding table, +footstool, +futon, +headboard, +hutch, +lamp, +nightstand, +ottoman, +plant stand, +rack, +recliner, +rocker, +settee, +shelves, +shoe cabinet, +sideboard, +sofa, +stool, +table, +vanity, +wardrobe, ?bed, ?chair, ?desk, ?dresser, ?futon, ?loveseat, ?nightstand, ?ottoman, ?sofa, ?stool, ?table, ?wardrobe

### FURNITURE FOR RELAXATION  `furniture_for_relaxation`
- правило: What belongs to the group «Furniture For Relaxation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +armchair, +hammock, +sofa, !lounger

### GEOMETRIC TOOLS  `geometric_tools`
- правило: What belongs to the group «Geometric Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 5
- ~protractor, +compass, +ruler, +set square, +triangle

### GREENHOUSE  `greenhouse`
- правило: What belongs to the group «Greenhouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +glass, +humidity, +plants, +temperature

### GROOMING TOOLS  `grooming_tools`
- правило: What belongs to the group «Grooming Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +brush, +comb, +razor, +trimmer

### HOME  `home`
- правило: What belongs to the group «Home» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +bathroom, +bedroom, +garage, +kitchen

### HOME BUYING  `home_buying`
- правило: What belongs to the group «Home Buying» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +down payment, +inspection, +mortgage, +realtor

### HOME DECOR  `home_decor`
- правило: What you choose when you decorate a room
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 12
- ~curtain, ~fabrics, ~lamp, ~rug, ~sofa, +colors, +curtains, +furniture, +lighting, +patterns, +vase, ?rug

### HOME DESIGN  `home_design`
- правило: What belongs to the group «Home Design» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +minimalist, +modern, +rustic, +vintage

### HOME ELECTRICALS  `home_electricals`
- правило: What belongs to the group «Home Electricals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +ceiling fan, +lamp, +smoke detector, +sockets

### HOME FEATURES  `home_features`
- правило: What belongs to the group «Home Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +attic, +basement, +garage, +garden

### HOME HEATING SYSTEM  `home_heating_system`
- правило: What belongs to the group «Home Heating System» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +boiler, +furnace, +radiator, +thermostat

### HOME LIBRARY  `home_library`
- правило: What belongs to the group «Home Library» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bookcase, +bookmark, +bookshelf, +reading chair

### HOUSE ROOMS  `home_rooms`
- правило: Rooms and spaces inside an ordinary house
- тип связи: `part_of`, базовая сложность 0.15
- слов: 20
- +attic, +basement, +bathroom, +bedroom, +cellar, +closet, +den, +dining room, +foyer, +garage, +hallway, +kitchen, +laundry room, +living room, +loft, +nursery, +pantry, +porch, +study, +sunroom

### HOME SECURITY  `home_security`
- правило: What belongs to the group «Home Security» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +alarm, +camera, +lock, +sensor

### HOME SOUNDS  `home_sounds`
- правило: What belongs to the group «Home Sounds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +door creak, +doorbell, +meowing, +snoring

### HOMELESS  `homeless`
- правило: What belongs to the group «Homeless» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +downtrodden, +peasant, +poor, +poverty

### HOTEL ROOMS  `hotel_rooms`
- правило: What belongs to the group «Hotel Rooms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +cabana, +deluxe, +penthouse, +suite

### HOUSE CHORES  `house_chores`
- правило: What belongs to the group «House Chores» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 6
- +cooking, +dishes, +dusting, +ironing, +laundry, +vacuuming

### HOUSE CLEANING  `house_cleaning`
- правило: What belongs to the group «House Cleaning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +broom, +duster, +mop, +vacuum

### HOUSEHOLD  `household`
- правило: What belongs to the group «Household» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +clock, +frame, +mirror, +vase

### HOUSEHOLD BUDGET  `household_budget`
- правило: What belongs to the group «Household Budget» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +expenses, +income, +rent, +savings

### HOUSEHOLD ROOMS  `household_rooms`
- правило: What belongs to the group «Household Rooms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +bathroom, +bedroom, +kitchen, +living

### HOUSEHOLD TASKS  `household_tasks`
- правило: What belongs to the group «Household Tasks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +chore, +cleaning, +cooking, +laundry

### HOUSEWORK TASKS  `housework_tasks`
- правило: What belongs to the group «Housework Tasks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +dusting, +mopping, +vacuuming, +washing

### IN THE HOUSE  `in_the_house`
- правило: What belongs to the group «In The House» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +coffee table, +dishwasher, +doormat, +laundry room

### IN YOUR HOUSE  `in_your_house`
- правило: What belongs to the group «In Your House» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +bathroom, +bedroom, +hallway, +kitchen

### KIDS BEDROOM  `kids_bedroom`
- правило: What belongs to the group «Kids Bedroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +crib, +poster, +rocking horse, +toy

### KITCHEN  `kitchen`
- правило: What belongs to the group «Kitchen» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 26
- ~peeler, +appliances, +baking essentials, +bowl, +butter, +chef, +cooker hood, +counter, +fridge, +grater, +griddle, +kettle, +knife, +ladle, +microwave, +oven, +recipe, +refrigerator, +skillet, +spatula, +stove, +table, +toaster, +tongs, +utensils, +whisk

### KITCHEN ACCESSORIES  `kitchen_accessories`
- правило: What belongs to the group «Kitchen Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +corkscrew, +grater, +tongs, +whisk

### KITCHEN APPLIANCES  `kitchen_appliances`
- правило: Electric machines used in a kitchen
- тип связи: `found_in`, базовая сложность 0.2
- слов: 28
- +air fryer, +blender, +can opener, +coffee machine, +coffee maker, +dishwasher, +food processor, +freezer, +fridge, +grill, +juicer, +kettle, +microwave, +mixer, +oven, +range (range_stove), +refrigerator, +slow cooker, +toaster, +waffle iron, +warmer, ?blender, ?dishwasher, ?juicer, ?kettle, ?microwave, ?toaster, !hood (hood_kitchen)

### KITCHEN DEVICES  `kitchen_devices`
- правило: What belongs to the group «Kitchen Devices» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +blender, +fridge, +grinder, +toaster

### KITCHEN DRAWER  `kitchen_drawer`
- правило: What you find when you open a kitchen drawer
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 7
- ~blades, ~containers, +corkscrew, +peeler, +silverware, +whisk, !fasteners

### KITCHEN EQUIPMENT  `kitchen_equipment`
- правило: What belongs to the group «Kitchen Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- ~colander, +blender, +food processor, +refrigerator

### KITCHEN KNIVES  `kitchen_knives`
- правило: What belongs to the group «Kitchen Knives» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +boning, +cleaver, +filet, +fillet, +paring

### KITCHEN TOOLS  `kitchen_tools`
- правило: Handheld tools and utensils used to prepare food in a kitchen
- тип связи: `used_in`, базовая сложность 0.15
- слов: 40
- ~colander, ~masher, +blender, +can opener, +corkscrew, +cutting board, +fork, +freezer, +grater, +juicer, +knife, +ladle, +measuring cup, +mixer, +napkin, +opener, +pan, +peeler, +plate (plate_dish), +pot, +rolling pin, +sieve, +skillet, +spatula, +spoon, +strainer, +thermometer, +timer, +tongs, +whisk, ?colander, ?fork, ?grater, ?knife, ?ladle, ?peeler, ?spatula, ?spoon, ?tongs, ?whisk

### KITCHEN UTENSILS  `kitchen_utensils`
- правило: What belongs to the group «Kitchen Utensils» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 9
- +fork, +knife, +ladle, +spatula, +spoon, +strainer, +tongs, +Turner, +whisk

### KITCHENWARE  `kitchenware`
- правило: What belongs to the group «Kitchenware» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 7
- +bowl, +cleaver, +glass, +grater, +spoon, +teapot, +thermos

### LAUNDRY THINGS  `laundry_things`
- правило: Things used to wash and dry clothes
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~clothespin, +basket, +bleach, +detergent, +dryer, +dryer sheet, +hamper, +hanger, +iron (iron_appliance), +ironing board, +lint trap, +softener, +stain remover, +starch, +washer, !line (line_cord)

### LEATHERWORKING TOOLS  `leatherworking_tools`
- правило: What belongs to the group «Leatherworking Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +swivel knife, !awl, !fid, xskiver

### LIGHTHOUSE  `lighthouse`
- правило: What belongs to the group «Lighthouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 15
- ~foghorn, +beacon, +coast, +fog, +fog horn, +keeper, +lantern, +lens, +navigation, +Rocky, +ships, +shore, +signal, +storm, +tower

### LIGHTING  `lighting`
- правило: Devices that light a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~floodlight, ~nightlight, ~sconce, +bulb, +candle, +ceiling fan, +chandelier, +dimmer, +fixture, +flashlight, +lamp, +lantern, +shade, +spotlight, +string lights, +torch, +track light, ?bulb, ?candle, ?lamp

### LIVING ROOM  `living_room_things`
- правило: Objects normally found in a living room
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~remote (remote_device), +armchair, +blanket, +bookshelf, +clock, +coffee table, +console, +curtain, +cushion, +fireplace, +lamp, +magazine, +ottoman, +painting, +rug, +sofa, +speaker, +television, +vase, !plant (plant_growth)

### MAGIC TOOLS  `magic_tools`
- правило: What belongs to the group «Magic Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +crystal, +enchanted mirror, +magic ball, +magic carpet

### MIXING TOOLS  `mixing_tools`
- правило: What belongs to the group «Mixing Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +blender, +ladle, +spatula, +whisk

### MODERN CLEANING DEVICES  `modern_cleaning_devices`
- правило: What belongs to the group «Modern Cleaning Devices» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +air purifier, +robot vacuum, +steam mop, +washing machine

### MOVING HOUSE  `moving_house`
- правило: What belongs to the group «Moving House» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +boxes, +label, +tape, +truck

### MUSHROOM  `mushroom`
- правило: What belongs to the group «Mushroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +oyster, +portobello, !chanterelle, !enoki, !porcini, !shiitake

### MUSHROOM VARIETIES  `mushroom_varieties`
- правило: What belongs to the group «Mushroom Varieties» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +morel, +truffle, !chanterelle, !porcini

### MUSHROOMS  `mushrooms`
- правило: What belongs to the group «Mushrooms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 10
- +morel, +oyster, +portobello, +truffle, !amanita, !chanterelle, !enoki, !porcini, !shiitake, xrussula

### NAIL CARE TOOLS  `nail_care_tools`
- правило: What belongs to the group «Nail Care Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +emery board, +nail buffer, +nail file, !cuticle pusher

### NAUTICAL TOOLS  `nautical_tools`
- правило: What belongs to the group «Nautical Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +compass, !astrolabe, !chronometer, !sextant

### NURSING TOOLS  `nursing_tools`
- правило: What belongs to the group «Nursing Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +catheter, +iv bag, +syringe, !pulse oximeter

### OPERA HOUSES  `opera_houses`
- правило: What belongs to the group «Opera Houses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +bolshoi, +covent garden, +la scala, +Met

### PAINTING TOOLS  `painting_tools`
- правило: What belongs to the group «Painting Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +brush, +canvas, +easel, +palette

### PALEONTOLOGY TOOLS  `paleontology_tools`
- правило: What belongs to the group «Paleontology Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +brush, +matrix, +plaster, !awl

### HOUSE PARTS  `parts_of_a_house`
- правило: Structural parts of a house
- тип связи: `part_of`, базовая сложность 0.2
- слов: 20
- ~beam (beam_wood), ~doorframe, +ceiling, +chimney, +column, +deck, +door, +floor, +foundation (foundation_building), +gutter, +porch, +railing, +roof, +shingle, +shutter, +siding, +stairs, +threshold, +wall, +window

### PET SUPPLIES  `pet_supplies`
- правило: Things bought to keep a pet at home
- тип связи: `used_in`, базовая сложность 0.3
- слов: 22
- ~tag (tag_label), +aquarium, +automatic feeder, +bed, +bowl, +brush, +cage, +carrier, +chew toy, +collar, +food, +harness, +kennel, +leash, +litter, +muzzle, +scratching post, +tank (tank_container), +toy, +treat, ?aquarium, ?bowl

### PHOTOGRAPHY TOOLS  `photography_tools`
- правило: What belongs to the group «Photography Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +diffuser, +flash, +tripod, !polarizer

### PLAYROOM  `playroom`
- правило: What belongs to the group «Playroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +blocks, +dolls, +mats, +toys

### POCKET TOOLS  `pocket_tools`
- правило: What belongs to the group «Pocket Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +bottle opener, +flashlight, +knife, +nail file

### POTTERY TOOLS  `pottery_tools`
- правило: What belongs to the group «Pottery Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 8
- +banding wheel, +clay, +glaze, +kiln, +needle tool, +wedge, +wheel, +wire tool

### ROOMS IN A HOUSE  `rooms_in_a_house`
- правило: What belongs to the group «Rooms In A House» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 6
- +basement, +bathroom, +bedroom, +children s room, +garage, +kitchen

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

### SURGERY TOOLS  `surgery_tools`
- правило: What belongs to the group «Surgery Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +clamp, +forceps, +scalpel, !retractor

### THINGS IN A BATHROOM  `things_in_a_bathroom`
- правило: What belongs to the group «Things In A Bathroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +mirror, +soap, +toothbrush, +towel

### THINGS IN A BEDROOM  `things_in_a_bedroom`
- правило: What belongs to the group «Things In A Bedroom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +bed, +nightstand, +pillow, +wardrobe

### GARAGE THINGS  `things_in_a_garage`
- правило: Things stored in an ordinary home garage
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~jack (jack_tool), ~oil (oil_motor), +bike, +broom, +car, +cooler, +extension cord, +gas can, +hose, +ladder, +lawnmower, +paint, +rake, +shelf (shelf_furniture), +shovel, +sled, +tire, +toolbox, +wheelbarrow, +workbench

### JUNK DRAWER  `things_in_a_junk_drawer`
- правило: Small odds and ends that pile up in a kitchen drawer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 22
- ~batteries, ~battery, ~chapstick, ~coin, ~flashlight, ~glue, ~magnet, ~matches, ~paper clip, ~pen (pen_writing), ~receipt, ~rubber band, ~scissors, ~screw, ~string, ~takeout menu, ~tape, ~twist tie, +key (key_lock), ?rubber band, ?scissors, ?tape

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

### TOOL  `tool`
- правило: What belongs to the group «Tool» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +hammer, +saw, +screwdriver, +wrench

### TOOL TYPES  `tool_types`
- правило: What belongs to the group «Tool Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +hammer, +pliers, +screwdriver, +wrench

### TOOLKIT  `toolkit`
- правило: What belongs to the group «Toolkit» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +chisel, +clamp, +level, +wrench

### TOOLS FOR MEASUREMENT  `tools_for_measurement`
- правило: What belongs to the group «Tools For Measurement» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +clock, +microscope, +ruler, +scales

### TOXIC MUSHROOMS  `toxic_mushrooms`
- правило: What belongs to the group «Toxic Mushrooms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +death cap, +destroying angel, +panther cap, !amanita

### TRASH THINGS  `trash_and_recycling`
- правило: Things related to household garbage and recycling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~wastebasket, +bag, +bin, +bottle, +can, +cardboard, +compost, +disposal, +dumpster, +junk, +landfill, +lid, +newspaper, +recycle, +scrap, +wrapper

### USED FOR CLEANING  `used_for_cleaning`
- правило: What belongs to the group «Used For Cleaning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +broom, +brush, +feather duster, +rag

### WEEDING TOOLS  `weeding_tools`
- правило: What belongs to the group «Weeding Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +fork, +hoe, +trowel, xkneeler

### WOODWORKING TOOLS  `woodworking_tools`
- правило: What belongs to the group «Woodworking Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +chisel, +lathe, +router, +saw

### WORKSHOP TOOLS  `workshop_tools`
- правило: What belongs to the group «Workshop Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +jigsaw, +lathe, +router, +vice


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
- слов: 23
- +anesthesia, +biopsy, +cast (cast_medical), +checkup, +dialysis, +endoscopy, +exam, +injection, +laser, +scan, +screening, +stitches, +surgery, +therapy, +transfusion, +transplant, +ultrasound, +vaccination, +X-ray, ?biopsy, ?surgery, ?therapy, ?ultrasound

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
- слов: 19
- ~aperture, ~depth of field, ~exposure, ~flash, ~focus (focus_lens), ~iso, ~macro, ~shutter speed, ~timer, ~tripod mount, ~white balance, ~Zoom, ?aperture, ?exposure, ?flash, ?iso, !bokeh, !metering, !viewfinder

### TYPOGRAPHY WORDS  `printing_and_type`
- правило: Words used to describe printed type
- тип связи: `found_in`, базовая сложность 0.5
- слов: 14
- ~bold (bold_type), ~caps, ~column, ~font, ~italic, ~justify, ~leading, ~margin, ~point size, ~serif, ~typeface, ~underline, !kerning, !lowercase

### SAILING TERMS  `sailing_terms`
- правило: Terms used when sailing a boat
- тип связи: `found_in`, базовая сложность 0.45
- слов: 20
- ~boom, ~draft (draft_boat), ~heel, ~knots, ~port, ~sheet (sheet_sail), ~starboard, ~stern, ?boom, ?jibe, !capsize, !cleat, !halyard, !jibe, !leeward, !luff, !mooring, !spinnaker, !tack (tack_sail), !windward

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

### BEVERAGE PROFESSIONALS  `beverage_professionals`
- правило: What belongs to the group «Beverage Professionals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +barista, +bartender, +Brewer, !brewmaster

### BUILDING TRADES  `building_trades`
- правило: Skilled trades that build and repair buildings
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~framer, ~glazier, ~plasterer, ~roofer, ~tiler, +bricklayer, +carpenter, +contractor, +electrician, +foreman, +installer, +laborer, +mason, +painter, +plumber, +surveyor, +welder, ?drywaller

### CAREER FIELDS  `career_fields`
- правило: What belongs to the group «Career Fields» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +education, +engineering, +finance, +medicine

### CIRCUS JOBS  `circus_and_fair_jobs`
- правило: Jobs held by performers and workers at a circus or fair
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~contortionist, ~stilt walker, +acrobat, +animal trainer, +barker, +clown, +fire eater, +juggler, +magician, +ringmaster, +tightrope walker, +trapeze artist

### CREATIVE CAREERS  `creative_careers`
- правило: What belongs to the group «Creative Careers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +architect, +curator, +designer, +sculptor

### CREATIVE JOBS  `creative_jobs`
- правило: Jobs held by people who make art or entertainment
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- +actor, +animator, +architect, +artist, +choreographer, +composer, +dancer, +designer, +director, +editor, +illustrator, +musician, +painter, +photographer, +poet, +producer, +sculptor, +singer, +writer, ?animator, ?artist, ?dancer

### DOCTOR  `doctor`
- правило: What belongs to the group «Doctor» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 14
- +clinic, +dentist, +diagnosis, +dietitian, +gloves, +hospital, +mask, +medicine, +patient, +prescription, +scalpel, +stethoscope, +surgeon, !allergist

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

### GOOD JOB  `good_job`
- правило: What belongs to the group «Good Job» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +amazing, +Bravo, +great, +well done

### GOVERNMENT JOBS  `government_jobs`
- правило: Jobs held by people who work for a government
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~secretary (secretary_minister), +ambassador, +auditor, +clerk, +commissioner, +councilman, +delegate, +diplomat, +governor, +inspector, +mayor, +official, +president, +senator, +treasurer

### HIGH SCHOOL COURSES  `high_school_courses`
- правило: What belongs to the group «High School Courses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +biology, +calculus, +chemistry, +economics

### BYGONE JOBS  `historic_jobs`
- правило: Jobs that were common in the past but are rare today
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~blacksmith, ~chimney sweep, ~cooper, ~miller, ~scribe, ~tanner, ~telegraph operator, ~weaver, !cobbler, !ferryman, !lamplighter, !milkman, !switchboard operator, !town crier, !wheelwright

### IN THE OFFICE  `in_the_office`
- правило: What belongs to the group «In The Office» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +badge, +calculator, +colleague, +desk

### JOB INTERVIEW  `job_interview`
- правило: What belongs to the group «Job Interview» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +application, +interview, +recruiter, +resume

### JOB OFFER  `job_offer`
- правило: What belongs to the group «Job Offer» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +candidate, +contract, +cv, +hiring

### JOB SEARCH  `job_search`
- правило: What belongs to the group «Job Search» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +cv, +interview, +reference, +resume

### JOBS  `jobs`
- правило: What belongs to the group «Jobs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 17
- +analyst, +architect, +artist, +chef, +dentist, +diplomat, +doctor, +engineer, +farmer, +firefighter, +lawyer, +manager, +nurse, +photographer, +surgeon, +teacher, +vet

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

### MEDIEVAL MILITARY  `medieval_military`
- правило: What belongs to the group «Medieval Military» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +Archer, +knight, +swordsman, !spearman

### MEDIEVAL PROFESSIONS  `medieval_professions`
- правило: What belongs to the group «Medieval Professions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +blacksmith, +fletcher, +jester, +scribe

### MILITARY FORMATIONS  `military_formations`
- правило: What belongs to the group «Military Formations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 7
- +battalion, +echelon, +flanking, +phalanx, +platoon, +squadron, !testudo

### MILITARY LEADERS  `military_leaders`
- правило: What belongs to the group «Military Leaders» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +caesar, +cort s, +genghis khan, +tokugawa

### MILITARY RANKS  `military_ranks`
- правило: Ranks held by members of the armed forces
- тип связи: `is_a`, базовая сложность 0.35
- слов: 19
- +admiral, +cadet, +captain, +colonel, +commander, +corporal, +ensign, +general, +lieutenant, +major (major_rank), +officer, +private, +seaman, +sergeant, ?admiral, ?colonel, ?corporal, ?private, ?sergeant

### MILITARY SECTIONS  `military_sections`
- правило: What belongs to the group «Military Sections» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +air force, +army, +marines, +navy

### MILITARY UNIFORM  `military_uniform`
- правило: What belongs to the group «Military Uniform» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +garrison cap, +overcoat, +tunic, !epaulets

### MILITARY UNITS  `military_units`
- правило: What belongs to the group «Military Units» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +battalion, +brigade, +platoon, +regiment

### NAVY OFFICER RANKS  `navy_officer_ranks`
- правило: What belongs to the group «Navy Officer Ranks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +captain, +commander, +ensign, +lieutenant

### NIGHT SHIFT  `night_shift_jobs`
- правило: Jobs commonly worked overnight
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~air traffic controller, ~baker, ~bartender, ~dispatcher, ~DJ, ~doctor, ~hotel clerk, ~janitor, ~night watchman, ~nurse, ~police officer, ~radio host, ~security guard, ~trucker

### OBSOLETE PROFESSIONS  `obsolete_professions`
- правило: What belongs to the group «Obsolete Professions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +alchemist, +blacksmith, +cobbler, +cooper

### OFFICE  `office`
- правило: What belongs to the group «Office» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 14
- +archive, +binder, +chair, +computer, +desk, +dossier, +laptop, +ledger, +memo, +papers, +printer, +scanner, +shredder, +stapler

### OFFICE EQUIPMENT  `office_equipment`
- правило: What belongs to the group «Office Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +copier, +scanner, +shredder, +typewriter

### OFFICE JOBS  `office_jobs`
- правило: Jobs held by people who work in an office
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- +accountant, +administrator, +analyst, +assistant, +auditor, +bookkeeper, +clerk, +consultant, +coordinator, +manager, +planner, +receptionist, +recruiter, +secretary (secretary_office), +supervisor, +treasurer

### OFFICE LIFE  `office_life`
- правило: What belongs to the group «Office Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +coffee, +deadline, +laptop, +meeting

### HELPING PROFESSIONS  `people_who_help`
- правило: Jobs whose main purpose is helping other people directly
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +aide, +caregiver, +chaplain, +coach, +counselor, +doctor, +firefighter, +interpreter, +mentor, +nurse, +social worker, +teacher, +therapist, +volunteer

### PHILOSOPHICAL SCHOOLS  `philosophical_schools`
- правило: What belongs to the group «Philosophical Schools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +existentialism, +nihilism, +pragmatism, +stoicism, +utilitarianism, !empiricism

### PHILOSOPHY SCHOOLS  `philosophy_schools`
- правило: What belongs to the group «Philosophy Schools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +existentialism, +nihilism, +stoicism, !empiricism

### POLICE ESSENTIALS  `police_essentials`
- правило: What belongs to the group «Police Essentials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +bulletproof vest, +handcuffs, +holster, +police badge

### POLICE STATION  `police_station`
- правило: What belongs to the group «Police Station» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +bail, +fingerprint, +identification, +mugshot

### PROFESSION  `profession`
- правило: What belongs to the group «Profession» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +accountant, +lawyer, +linguist, +professor

### REPAIR JOBS  `repair_jobs`
- правило: Jobs held by people who fix broken things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~upholsterer, +appliance repairman, +cobbler, +electrician, +handyman, +locksmith, +machinist, +mechanic, +plumber, +repairman, +tailor, +technician, +watchmaker, +welder

### SCHOOL  `school`
- правило: What belongs to the group «School» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 19
- +backpack, +book, +classroom, +curriculum, +desk, +folder, +globe, +homework, +learn, +locker, +pencil, +recess, +ruler, +school subjects, +semester, +student, +teacher, +teachers, !copybook

### SCHOOL ASSESSMENT  `school_assessment`
- правило: What belongs to the group «School Assessment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +essay, +exam, +quiz, +test

### SCHOOL CLASSES  `school_classes`
- правило: What belongs to the group «School Classes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +biology, +chemistry, +geometry, +literature

### SCHOOL FACILITIES  `school_facilities`
- правило: What belongs to the group «School Facilities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +auditorium, +classroom, +gymnasium, +library

### SCHOOL JOBS  `school_jobs`
- правило: Jobs held by adults who work at a school
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~secretary (secretary_office), +aide, +bus driver, +coach, +counselor, +crossing guard, +custodian, +dean, +janitor, +librarian, +lunch lady, +nurse, +principal, +professor, +registrar, +substitute, +teacher, +tutor

### SCHOOL LUNCH  `school_lunch`
- правило: What belongs to the group «School Lunch» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +nuggets, +pizza, +sandwich, +soup

### SCHOOL PERIODS  `school_periods`
- правило: What belongs to the group «School Periods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +class, +homeroom, +lunch, +recess

### SCHOOL RELATED  `school_related`
- правило: What belongs to the group «School Related» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +principal, +school bus, +timetable, +uniform

### SCHOOL TOPICS  `school_topics`
- правило: What belongs to the group «School Topics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +geography, +history, +math, +science

### SCHOOLWORK  `schoolwork`
- правило: What belongs to the group «Schoolwork» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +assignment, +exercise, +homework, +project

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

### STEM CAREERS  `stem_careers`
- правило: What belongs to the group «Stem Careers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +chemist, +engineer, +physicist, +scientist

### STEM JOBS  `stem_jobs`
- правило: What belongs to the group «Stem Jobs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +biologist, +chemist, +engineer, +physicist

### STORE JOBS  `store_jobs`
- правило: Jobs held by people who work in shops and stores
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~bagger, ~greeter, ~merchandiser, ~stocker, +barber, +buyer, +cashier, +clerk, +florist, +grocer, +jeweler, +manager, +pharmacist, +salesperson, +security guard, +tailor

### TEACHER  `teacher`
- правило: What belongs to the group «Teacher» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +educate, +explain, +guide, +instruct

### THINGS IN AN OFFICE  `things_in_an_office`
- правило: What belongs to the group «Things In An Office» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +computer, +desk, +paper, +phone

### TRADE WORKERS  `trade_workers`
- правило: What belongs to the group «Trade Workers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +mason, +plumber, +Smith, !glazier

### TRANSPORT JOBS  `transport_jobs`
- правило: Jobs held by people who drive, fly or pilot for a living
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~ferryman, +bus driver, +captain, +chauffeur, +conductor, +courier, +delivery driver, +dispatcher, +driver, +engineer, +flight attendant, +pilot, +taxi driver, +trucker


## Тема: materials

### BUILDING MATERIALS  `building_materials`
- правило: Materials used to construct buildings
- тип связи: `made_of`, базовая сложность 0.25
- слов: 28
- +Adobe, +aluminum, +brick, +cement, +concrete, +drywall, +glass, +granite, +insulation, +lumber, +marble (marble_stone), +plaster, +plywood, +shingle, +slate, +steel, +stone, +stucco, +thatch, +tile, +timber, +vinyl, +wood, ?brick, ?concrete, ?steel, ?tile, ?wood

### FABRIC TYPES  `fabric_types`
- правило: Kinds of cloth used to make things
- тип связи: `is_a`, базовая сложность 0.3
- слов: 31
- ~gingham, ~taffeta, +burlap, +canvas, +cashmere, +chiffon, +corduroy, +cotton, +denim, +felt, +flannel, +jersey, +lace, +linen, +muslin, +satin, +silk, +terry, +tweed, +velvet, +wool, ?chiffon, ?cotton, ?denim, ?flannel, ?linen, ?satin, ?silk, ?tweed, ?velvet, ?wool

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
- слов: 25
- ~feldspar, ~hematite, +calcite, +calcium, +gemstones, +graphite, +gypsum, +iodine, +magnesium, +magnetite, +mica, +phosphorus, +pyrite, +quartz, +sulfur, +talc, ?calcite, ?feldspar, ?gypsum, ?mica, ?pyrite, ?quartz, !azurite, !fluorite, !halite

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


## Тема: medicine

### BODY FLUIDS  `body_fluids`
- правило: Fluids produced by the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~bile, ~lymph, ~mucus, ~plasma, ~saliva, ~serum, ~sputum, ~sweat, ~tear, ~tears, ~urine, +blood, +milk, ?blood, ?lymph, ?plasma, ?saliva, ?serum, ?sweat, ?urine

### DENTAL WORDS  `dental_words`
- правило: Words used at a dental office
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~bridge (bridge_dental), ~crown (crown_dental), ~incisor, +braces, +canine, +cavity, +denture, +enamel, +extraction, +filling, +floss, +gum (gum_mouth), +molar, +plaque, +retainer, +root canal, +tartar, +whitening

### DISEASES  `diseases`
- правило: Diseases an average person can name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~chickenpox, +anemia, +arthritis, +asthma, +bronchitis, +cancer, +cholera, +diabetes, +flu, +hepatitis, +malaria, +measles, +mumps, +pneumonia, +polio, +rabies, +shingles, +tetanus, +tuberculosis, +typhoid

### EMERGENCY ROOM  `emergency_room`
- правило: What is treated, seen or used in a hospital emergency room
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~gurney, +bones, +illnesses, +injuries, +stretcher, +symptoms, +triage

### EMERGENCY WORDS  `emergency_words`
- правило: Words used during a medical emergency
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- +ambulance, +code, +CPR, +defibrillator, +dispatcher, +evacuation, +hotline, +oxygen, +paramedic, +rescue, +response, +siren, +stretcher, +trauma, +triage

### FIRST AID  `first_aid`
- правило: Things kept in a first aid kit
- тип связи: `used_in`, базовая сложность 0.25
- слов: 21
- +antiseptic, +aspirin, +bandage, +burn cream, +cotton ball, +eye wash, +gauze, +gloves, +ice pack, +ointment, +scissors, +sling, +splint, +tape, +thermometer, +tweezers, +wipe, ?antiseptic, ?bandage, ?gauze, ?splint

### HOSPITAL DEPARTMENTS  `hospital_departments`
- правило: Departments and units inside a hospital
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- +admissions, +cardiology, +dialysis, +emergency, +intensive care, +laboratory, +maternity, +morgue, +oncology, +pediatrics, +pharmacy, +physical therapy, +radiology, +recovery, +surgery

### HYGIENE THINGS  `hygiene`
- правило: Things used to keep the body clean
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- +brush, +comb, +cotton swab, +deodorant, +floss, +lotion, +mouthwash, +nail clipper, +razor, +rinse, +sanitizer, +shampoo, +shower, +soap, +tissue (tissue_paper), +toothbrush, +toothpaste, +towel, +washcloth, ?floss

### INJURIES  `injuries`
- правило: Kinds of physical injury
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~bite (bite_wound), +blister, +break, +bruise, +burn, +concussion, +cut, +dislocation, +fracture, +frostbite, +laceration, +puncture, +scrape, +splinter, +sprain, +strain, +sunburn, +whiplash, ?bruise, ?cut, ?fracture, ?sprain

### MEDICAL SPECIALTIES  `medical_specialties`
- правило: Branches of medical practice
- тип связи: `is_a`, базовая сложность 0.4
- слов: 23
- ~geriatrics, ~nephrology, ~orthopedics, +anesthesia, +cardiology, +dentist, +dermatology, +immunology, +midwife, +neurology, +obstetrics, +oncology, +ophthalmology, +pathology, +pediatrics, +psychiatry, +radiology, +surgeon, +surgery, +urology, ?oncology, ?radiology, !allergist

### MEDICAL TOOLS  `medical_tools`
- правило: Instruments a doctor or nurse uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 20
- ~monitor (monitor_medical), ~speculum, +catheter, +clamp, +defibrillator, +forceps, +gauze, +gurney, +IV, +needle (needle_medical), +scalpel, +sling, +splint, +stethoscope, +syringe, +thermometer, +tourniquet, +tweezers, +ventilator, xotoscope

### FORMS OF MEDICINE  `medicine_forms`
- правило: Forms in which medicine is taken
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~cream (cream_ointment), ~lozenge, ~suppository, +capsule, +drop, +gel, +inhaler, +injection, +ointment, +patch, +pill, +powder, +spray, +syrup, +tablet

### NUTRITION WORDS  `nutrition_words`
- правило: Words used to talk about diet and nutrition
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +calorie, +carbohydrate, +cholesterol, +diet, +fat, +fiber, +mineral, +nutrient, +organic, +portion, +protein, +serving, +sodium, +sugar, +vitamin, +whole grain

### BIRTH WORDS  `pregnancy_words`
- правило: Words used about pregnancy and childbirth
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- +cradle, +crib, +delivery, +due date, +formula, +incubator, +labor, +midwife, +newborn, +nursery, +obstetrician, +stroller, +trimester, +twins, +ultrasound

### SLEEP WORDS  `sleep_and_rest`
- правило: Words about sleep and its problems
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~jetlag, ~sleepwalk, +alarm, +apnea, +bedtime, +doze, +dream, +drowsy, +insomnia, +mattress, +nap, +nightmare, +pillow, +rest (rest_sleep), +snore

### THERAPY WORDS  `therapy_words`
- правило: Words used in physical and mental therapy
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~appointment, ~brace, ~counselor, ~crutch, ~exercise, ~massage, ~progress, ~recovery, ~rehab, ~session, ~stretch, ~walker, +goal, +treatment

### VISION WORDS  `vision_words`
- правило: Words used about eyesight and glasses
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~astigmatism, ~farsighted, ~nearsighted, +blind, +contacts, +cornea, +eye chart, +frame, +glasses, +lens, +optometrist, +prescription, +pupil, +squint, !bifocal

### VITAMINS AND MINERALS  `vitamins_and_minerals`
- правило: Nutrients the body needs in small amounts
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~riboflavin, ~thiamine, +biotin, +calcium, +folate, +iodine, +iron (iron_metal), +magnesium, +niacin, +potassium, +selenium, +sodium, +vitamin C, +vitamin D, +zinc


## Тема: nature_more

### BIOMES  `biomes`
- правило: Major natural regions of the earth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 21
- +chaparral, +desert, +dune, +forest, +grassland, +jungle, +marsh, +mountain, +ocean, +prairie, +rainforest, +reef, +savanna, +steppe, +taiga, +tundra, +wetland, ?desert, ?grassland, ?taiga, ?tundra

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
- ~plane (plane_aircraft), +aurora, +cloud, +comet, +constellation, +eclipse, +galaxy, +meteor, +Milky Way, +moon, +planet, +satellite, +shooting star, +star (star_space)

### ROCK FORMATIONS  `rock_formations`
- правило: Natural rock shapes and formations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- ~arch (arch_structure), +bluff, +boulder, +butte, +canyon, +cave, +cliff, +gorge, +hoodoo, +mesa, +monolith, +outcrop, +pillar, +ravine, +sinkhole, +spire, +terrace, !stack (stack_pile)

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
- слов: 15
- +blanket, +blizzard, +boot (boot_shoe), +fireplace, +frost, +hot cocoa, +icicle, +mitten, +scarf, +shovel, +skate, +ski, +sled, +snow, +snowman

### MOON PHASES  `tide_and_moon`
- правило: Phases and states of the moon
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~quarter (quarter_fourth), +blue moon, +crescent, +eclipse, +full moon, +half moon, +harvest moon, +new moon, +waning, +waxing, !gibbous, !supermoon

### VOLCANOES  `volcanoes`
- правило: Famous volcanoes
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Kilauea, ~Krakatoa, ~Mauna Loa, ~pyroclastic, ~Stromboli, +ash, +caldera, +cinder, +Etna, +Fuji, +Rainier, +St Helens, +Vesuvius, !Cotopaxi, !Pinatubo, !Popocatepetl

### WATERFALLS  `waterfalls`
- правило: Famous waterfalls
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Havasu, ~Multnomah, ~Shoshone, +angel, +Angel Falls, +Niagara, +Sutherland, +Victoria, +Yosemite Falls, ?Havasu, ?Iguazu, !Iguazu, xGullfoss, xkaieteur

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
- слов: 20
- +bakery, +bistro, +buffet, +cafe, +cafeteria, +deli, +diner, +drive through, +food truck, +grill, +pizzeria, +pub, +restaurant, +snack bar, +steakhouse, +tavern, ?cafe, ?diner, ?pub, ?restaurant

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
- слов: 25
- +almond, +apple (apple_fruit), +apricot, +avocado, +banana, +cherry, +coconut, +fig, +grape, +lemon, +lime, +mango, +olive, +orange (orange_fruit), +peach, +pear, +pecan, +plum, +walnut, ?apricot, ?cherry, ?mango, ?peach, ?pear, ?plum

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
- слов: 24
- ~chive, ~lavender (lavender_plant), ~lemongrass, ~marjoram, ~tarragon, +basil, +bay, +cilantro, +dill, +mint (mint_herb), +oregano, +parsley, +rosemary, +sage (sage_herb), +sorrel, +spices, +thyme, ?basil, ?cilantro, ?oregano, ?parsley, ?rosemary, ?tarragon, ?thyme

### HOUSEPLANTS  `houseplants`
- правило: Plants commonly kept indoors in pots
- тип связи: `is_a`, базовая сложность 0.3
- слов: 22
- ~begonia, ~palm (palm_tree), ~philodendron, +aloe, +bamboo, +cactus, +Fern, +geranium, +Ivy, +jade, +orchid, +peace lily, +rubber plant, +snake plant, +spider plant, +succulent, +Violet, ?cactus, ?Fern, ?orchid, ?pothos, !pothos

### LEAF WORDS  `leaf_shapes`
- правило: Words describing leaves and how they grow
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~blade, ~bud, ~canopy, ~deciduous, ~evergreen, ~foliage, ~lobe, ~needle (needle_pine), ~sprout, ~stalk, ~stem, ~vein, !broadleaf, !frond

### MUSHROOM TYPES  `mushroom_types`
- правило: Kinds of edible and wild mushrooms
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~morel, ~oyster, ~portobello, ~truffle, ?chanterelle, ?morel, ?oyster, ?portobello, ?shiitake, !button (button_mushroom), !chanterelle, !enoki, !porcini, !puffball, !shiitake, !toadstool, xcremini

### PLANT PARTS  `plant_parts`
- правило: Parts of a growing plant
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~bark (bark_tree), ~tendril, +bud, +flower, +fruit, +leaf, +node, +petal, +pollen, +root, +seed, +sprout, +stalk, +stem, +thorn, +vine, ?leaf, ?root, ?seed, ?stem

### POISONOUS PLANTS  `poisonous_plants`
- правило: Plants that are dangerous to touch or eat
- тип связи: `has_property`, базовая сложность 0.4
- слов: 17
- ~castor bean, ~hemlock, ~holly berry, ~Ivy, ~mistletoe, ~nightshade, ~poison ivy, ~poison oak, ~yew, ?foxglove, ?hemlock, ?nightshade, ?oleander, !foxglove, !monkshood, !oleander, !sumac

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


## Тема: science

### ARCHITECTURE ELEMENTS  `architecture_elements`
- правило: What belongs to the group «Architecture Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +Arches, +beams, +columns, +facades

### ASTROPHYSICS  `astrophysics`
- правило: What belongs to the group «Astrophysics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +dark matter, +event horizon, +neutron star, +red giant

### BAKING SCIENCE  `baking_science`
- правило: What belongs to the group «Baking Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +dough, +gluten, +rise, +yeast

### BIOCHEMICAL COMPOUNDS  `biochemical_compounds`
- правило: What belongs to the group «Biochemical Compounds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +antibody, +enzyme, +hormone, +neurotransmitter

### BIOCHEMISTRY  `biochemistry`
- правило: What belongs to the group «Biochemistry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +enzyme, +substrate, !cofactor, !glycolysis

### BIOLOGICAL FUNCTIONS  `biological_functions`
- правило: What belongs to the group «Biological Functions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +breathing, +circulation, +digestion, +reproduction

### BIOLOGICAL KINGDOMS  `biological_kingdoms`
- правило: What belongs to the group «Biological Kingdoms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 7
- +fruits, +fungi, +herbs, +vegetables, !animalia, !plantae, xprotista

### BIOLOGY BRANCHES  `biology_branches`
- правило: What belongs to the group «Biology Branches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +anatomy, +ecology, +genetics, +taxonomy

### BIOLOGY DOMAINS  `biology_domains`
- правило: What belongs to the group «Biology Domains» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bacteria, +fungi, !archaea, xeukarya

### BIOLOGY FIELDS  `biology_fields`
- правило: What belongs to the group «Biology Fields» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 8
- +botany, +ecology, +fungi, +histology, +taxonomy, +zoology, !cytology, !embryology

### BIOLOGY SUBJECTS  `biology_subjects`
- правило: What belongs to the group «Biology Subjects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +ecology, +genetics, +microbiology, !mycology

### BIOTECHNOLOGY  `biotechnology`
- правило: What belongs to the group «Biotechnology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +enzyme, +fermentation, +genome, +recombinant

### HUMAN BIOLOGY  `body_science`
- правило: Scientific words about how the human body works
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~artery, ~blood, ~bone, ~cell (cell_body), ~dna, ~enzyme, ~gene, ~hormone, ~immunity, ~membrane, ~metabolism, ~muscle, ~nerve, ~organ (organ_body), ~oxygen, ~plasma, ~protein, ~tissue (tissue_body)

### CHEMICAL BONDS  `chemical_bonds`
- правило: What belongs to the group «Chemical Bonds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +covalent, +hydrogen, +ionic, +metallic

### CHEMICAL COMPOUND PREFIXES  `chemical_compound_prefixes`
- правило: What belongs to the group «Chemical Compound Prefixes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +di, +mono, +tetra, +tri

### CHEMICAL ELEMENT  `chemical_element`
- правило: What belongs to the group «Chemical Element» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +chlorine, +hydrogen, +oxygen, +silicon

### CHEMICAL LAB GLASSWARE  `chemical_lab_glassware`
- правило: What belongs to the group «Chemical Lab Glassware» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +beaker, +flask, +funnel, !pipette

### CHEMICAL REACTIONS  `chemical_reactions`
- правило: What belongs to the group «Chemical Reactions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +combustion, +hydrolysis, +oxidation, +synthesis

### CHEMIST  `chemist`
- правило: What belongs to the group «Chemist» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 5
- +acetyl, +acid, +alcohol, +alkali, +compound

### CHEMISTRY  `chemistry`
- правило: What belongs to the group «Chemistry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 16
- +acid, +alloys, +atom, +base, +beaker, +compound, +element, +formula, +isotope, +molecule, +periodic, +polymer, +reaction, +solution, +solvent, +valence

### CHEMISTRY TERMS  `chemistry_terms`
- правило: What belongs to the group «Chemistry Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +catalyst, +ion, +molecule, +reaction

### CHEMISTRY TOPICS  `chemistry_topics`
- правило: What belongs to the group «Chemistry Topics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +acids, +metals, +polymers, +solutions

### CHEMISTRY WORDS  `chemistry_words`
- правило: Words used in chemistry class
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~acid, ~atom, ~base, ~bond, ~catalyst, ~compound, ~element, ~formula, ~ion, ~isotope, ~mixture, ~molecule, ~reaction, ~salt, ~solution, ~valence

### CLASSICAL ELEMENTS  `classical_elements`
- правило: What belongs to the group «Classical Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +air, +Earth, +fire, +water

### COMPUTER  `computer`
- правило: What belongs to the group «Computer» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 14
- ~heatsink, +cpu, +gpu, +hard drive, +hardware, +internet, +processor, +program, +programming, +programming language, +restart, +software, +terminal, +vga card

### COMPUTER COMMANDS  `computer_commands`
- правило: What belongs to the group «Computer Commands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 5
- +copy, +delete, +paste, +save, +undo

### COMPUTER FILE EXTENSIONS  `computer_file_extensions`
- правило: What belongs to the group «Computer File Extensions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +doc, +jpeg, +pdf, +zip

### COMPUTER KEYS  `computer_keys`
- правило: What belongs to the group «Computer Keys» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 7
- +alt, +control, +ctrl, +enter, +escape, +space, +tab

### COMPUTER LANGUAGES  `computer_languages`
- правило: What belongs to the group «Computer Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +java, +pascal, +python, +swift

### COMPUTER MEMORY  `computer_memory`
- правило: What belongs to the group «Computer Memory» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +buffer, +cache, +ram, +rom

### COMPUTER OPERATING SYSTEMS  `computer_operating_systems`
- правило: What belongs to the group «Computer Operating Systems» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +android, +linux, +macos, +windows

### COMPUTER PROGRAMMING  `computer_programming`
- правило: What belongs to the group «Computer Programming» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 8
- +debug, +fork, +function, +loop, +return, +switch, +variable, +while

### COMPUTER PROGRAMMING LANGUAGES  `computer_programming_languages`
- правило: What belongs to the group «Computer Programming Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +java, +python, +ruby, +swift

### COMPUTER PROGRAMMING TERMS  `computer_programming_terms`
- правило: What belongs to the group «Computer Programming Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +array, +function, +loop, +variable

### COMPUTER PROGRAMS  `computer_programs`
- правило: What belongs to the group «Computer Programs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +audacity, +firefox, +photoshop, +Spotify

### COMPUTER SCIENCE  `computer_science`
- правило: What belongs to the group «Computer Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +ai, +algorithm, +database, +software

### COMPUTER STORAGE  `computer_storage`
- правило: What belongs to the group «Computer Storage» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +buffer, +cache, +drive, +memory

### COMPUTER STORAGE DEVICES  `computer_storage_devices`
- правило: What belongs to the group «Computer Storage Devices» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +flash, +floppy disc, +hard, +thumb

### COMPUTER TERMS  `computer_terms`
- правило: What belongs to the group «Computer Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +browser, +cache, +server, +shell

### COMPUTER VIRUSES  `computer_viruses`
- правило: What belongs to the group «Computer Viruses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +malware, +spyware, +trojan, +worm

### COMPUTERS  `computers`
- правило: What belongs to the group «Computers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +laptop, +printer, +router, +server

### CULINARY TECHNIQUES  `culinary_techniques`
- правило: What belongs to the group «Culinary Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +emulsion, +poaching, +reduction, !braising

### DEEP SPACE OBJECTS  `deep_space_objects`
- правило: What belongs to the group «Deep Space Objects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +black hole, +nebula, +pulsar, !quasar

### DINOSAURS  `dinosaurs`
- правило: Dinosaur species an average person can name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~allosaurus, ~brachiosaurus, ~diplodocus, ~pterodactyl, ~spinosaurus, ~stegosaurus, ~triceratops, ~velociraptor, +brontosaurus, +raptor, +t rex, +tyrannosaurus, ?stegosaurus, ?triceratops, ?velociraptor, xankylosaurus

### DRAWING TECHNIQUES  `drawing_techniques`
- правило: What belongs to the group «Drawing Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +blending, +hatching, +shading, !stippling

### ELECTRICITY WORDS  `electricity_words`
- правило: Words used to talk about electricity
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +amp, +battery, +charge, +circuit, +conductor, +current (current_electric), +fuse, +generator, +outlet, +plug, +resistor, +shock, +socket (socket_electric), +switch, +transformer, +voltage, +Watt, +wire

### ELEMENT  `element`
- правило: What belongs to the group «Element» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 7
- +air, +Earth, +fire, +magnesium, +potassium, +silver, +water

### ELEMENTAL POWERS  `elemental_powers`
- правило: What belongs to the group «Elemental Powers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +air, +Earth, +fire, +water

### CHEMICAL ELEMENTS  `elements`
- правило: Chemical elements an average person can name
- тип связи: `is_a`, базовая сложность 0.35
- слов: 27
- ~mercury (mercury_metal), +air, +argon, +calcium, +carbon (carbon_element), +chlorine, +copper, +Earth, +fire, +gold, +helium, +hydrogen, +iron (iron_metal), +lead (lead_metal), +neon, +nitrogen, +oxygen, +potassium, +silver, +sodium, +sulfur, +uranium, +water, +zinc, ?gold, ?helium, ?oxygen

### ELEMENTS OF NATURE  `elements_of_nature`
- правило: What belongs to the group «Elements Of Nature» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 8
- +air, +Earth, +fire, +lightning, +rain, +thunder, +water, +wind

### EMERGING TECHNOLOGIES  `emerging_technologies`
- правило: What belongs to the group «Emerging Technologies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +biometric, +blockchain, +quantum, !nanotech

### ENERGY WORDS  `energy_words`
- правило: Words for kinds and sources of energy
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +battery, +biomass, +coal, +electric, +fuel, +gas, +geothermal, +hydro, +kinetic, +magnetic, +nuclear, +solar, +steam, +thermal, +wind

### EVEN NUMBERS  `even_numbers`
- правило: What belongs to the group «Even Numbers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +eight, +four, +six, +two

### EXACT SCIENCES  `exact_sciences`
- правило: What belongs to the group «Exact Sciences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +chemistry, +genetics, +mathematics, +physics

### DISSOLVING THINGS  `experiments`
- правило: Substances that dissolve in water
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~baking soda, ~candy, ~chalk (chalk_rock), ~coffee, ~gelatin, ~honey, ~ink, ~kool aid, ~powder, ~salt, ~soap, ~sugar, ~syrup, ~tablet

### FAMOUS PHYSICISTS  `famous_physicists`
- правило: What belongs to the group «Famous Physicists» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +Bohr, +Einstein, +Newton, +Tesla

### FANTASY COSTUME ELEMENTS  `fantasy_costume_elements`
- правило: What belongs to the group «Fantasy Costume Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +cloak, +mask, +tunic, !gauntlets

### FORENSIC SCIENCE  `forensic_science`
- правило: What belongs to the group «Forensic Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +criminology, +investigation, +pathology, +toxicology

### HOROSCOPE ELEMENTS  `horoscope_elements`
- правило: What belongs to the group «Horoscope Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +conjunction, +moon sign, +natal chart, +rising sign

### IMAGING TECHNIQUES  `imaging_techniques`
- правило: What belongs to the group «Imaging Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +crystallography, +microscopy, +radiography, +tomography

### INDUSTRIAL CHEMICALS  `industrial_chemicals`
- правило: What belongs to the group «Industrial Chemicals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +acetone, +benzene, +sodium chloride, +sulfuric acid

### INHERITED ELEMENTS  `inherited_elements`
- правило: What belongs to the group «Inherited Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +blood type, +dna, +facial features, +hair texture

### INVENTIONS  `inventions`
- правило: Famous inventions that changed everyday life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 26
- +airplane, +battery, +blueprint, +camera, +compass, +computer, +elevator, +engine, +internet, +lightbulb, +microscope, +model, +patent, +phonograph, +printing press, +prototype, +radio, +refrigerator, +telephone, +telescope, +television, +typewriter, +vaccine, +wheel, ?compass, ?telephone

### SCIENCE ACTIONS  `lab_actions`
- правило: Things a scientist does in an experiment
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- +analyze, +boil, +compare, +dilute, +dissolve, +filter, +freeze, +heat, +measure, +mix, +observe, +predict, +record, +sample, +test, +weigh

### LAB EQUIPMENT  `lab_equipment`
- правило: Equipment found in a school science laboratory
- тип связи: `found_in`, базовая сложность 0.35
- слов: 24
- ~magnifier, ~pipette, +beaker, +burner, +centrifuge, +clamp, +dropper, +flask, +funnel, +goggles, +magnet, +microscope, +petri dish, +rack, +scale (scale_weigh), +slide, +stopper, +test tube, +thermometer, +tongs, ?beaker, ?burner, ?centrifuge, ?pipette

### LABORATORY TECHNIQUES  `laboratory_techniques`
- правило: What belongs to the group «Laboratory Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +chromatography, +electrophoresis, +microscopy, +spectroscopy, !centrifugation, !titration

### LIBRARY SCIENCE  `library_science`
- правило: What belongs to the group «Library Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +archive, +bibliography, +dewey, +reserve

### FORCES  `magnets_and_forces`
- правило: Physical forces studied in science class
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~buoyancy, ~drag, ~friction, ~gravity, ~inertia, ~lift, ~magnetism, ~pressure, ~pull, ~push, ~tension, ~thrust, ~torque

### MARINE BIOLOGY  `marine_biology`
- правило: What belongs to the group «Marine Biology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +ecosystem, +habitat, +ocean layers, +taxonomy

### MATH  `math`
- правило: What belongs to the group «Math» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 8
- +abstract thinking, +addition, +division, +multiplication, +stats, +subtraction, +trigonometry, !radian

### MATH BRANCHES  `math_branches`
- правило: What belongs to the group «Math Branches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 7
- +algebra, +calculus, +geometry, +number theory, +probability, +statistics, +topology

### MATH CONCEPTS  `math_concepts`
- правило: What belongs to the group «Math Concepts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +algebra, +calculus, +geometry, +trigonometry

### MATH OPERATIONS  `math_operations`
- правило: Operations performed on numbers
- тип связи: `does_action`, базовая сложность 0.25
- слов: 15
- ~round (round_math), +add, +average, +calculate, +count, +cube, +divide, +double, +estimate, +factor, +halve, +multiply, +Square, +subtract, +sum

### MATH OPERATORS  `math_operators`
- правило: What belongs to the group «Math Operators» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +divide, +minus, +plus, +times

### MATH PUZZLES  `math_puzzles`
- правило: What belongs to the group «Math Puzzles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +fibonacci, +magic square, +riddle, +sudoku

### MATH SUBJECTS  `math_subjects`
- правило: What belongs to the group «Math Subjects» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 5
- +algebra, +calculus, +geometry, +statistics, +trigonometry

### MATH TERMS  `math_terms`
- правило: What belongs to the group «Math Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +calculus, +limit, +matrix, +vector

### MATH WORDS  `math_words`
- правило: Words used in school mathematics
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +angle, +area, +average, +decimal, +diameter, +equation, +exponent, +fraction, +integer, +percent, +perimeter, +prime, +product, +radius, +ratio, +remainder, +square root, +sum, +variable, +volume

### MATHEMATICAL CONSTANTS  `mathematical_constants`
- правило: What belongs to the group «Mathematical Constants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +euler, +phi, +pi, +tau

### MATHEMATICAL FIELDS  `mathematical_fields`
- правило: What belongs to the group «Mathematical Fields» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 6
- +analysis, +calculus, +number theory, +topology, +trigonometry, !combinatorics

### MATHEMATICAL SEQUENCES  `mathematical_sequences`
- правило: What belongs to the group «Mathematical Sequences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +arithmetic, +fibonacci, +geometric, +prime

### MATHEMATICIANS  `mathematicians`
- правило: What belongs to the group «Mathematicians» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +euler, +gauss, +riemann, !fermat

### MATHEMATICS  `mathematics`
- правило: What belongs to the group «Mathematics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 9
- +addition, +algebra, +arithmetic, +calculus, +geometry, +integer, +matrix, +tangent, +vector

### MATHEMATICS BRANCHES  `mathematics_branches`
- правило: What belongs to the group «Mathematics Branches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 5
- +calculus, +statistics, +topology, +trigonometry, !combinatorics

### MATHEMATICS FIELDS  `mathematics_fields`
- правило: What belongs to the group «Mathematics Fields» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +algebra, +calculus, +geometry, +Numbers

### MATHS  `maths`
- правило: What belongs to the group «Maths» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 11
- +addition, +algebra, +equations, +geometry, +modulus, +Newton, +Numbers, +percent, +probability, +theorem, !hypotenuse

### MEDIA TECHNOLOGY  `media_technology`
- правило: What belongs to the group «Media Technology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +audio, +broadcast, +storage devices, +visual

### METALS  `metals`
- правило: Metals and metal alloys used in everyday objects
- тип связи: `is_a`, базовая сложность 0.25
- слов: 32
- ~mercury (mercury_metal), +aluminum, +brass, +bronze, +chrome, +chromium, +cobalt, +copper, +gold, +iron (iron_metal), +lead (lead_metal), +magnesium, +nickel, +pewter, +platinum, +silver, +steel, +tin (tin_metal), +titanium, +tungsten, +zinc, ?aluminum, ?brass, ?bronze, ?copper, ?gold, ?nickel, ?platinum, ?silver, ?steel, ?titanium, ?zinc

### METALWORKING TECHNIQUES  `metalworking_techniques`
- правило: What belongs to the group «Metalworking Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +annealing, +forging, +quenching, +tempering

### METAPHYSICAL CONCEPTS  `metaphysical_concepts`
- правило: What belongs to the group «Metaphysical Concepts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +aura, +karma, +soul, +Spirit

### TINY THINGS  `microscope_things`
- правило: Things too small to see with the naked eye
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~atom, ~bacteria, ~cell (cell_body), ~dna, ~dust mite, ~electron, ~germ, ~microbe, ~mite, ~molecule, ~particle, ~pollen, ~spore, ~virus

### MICROSCOPY TECHNIQUES  `microscopy_techniques`
- правило: What belongs to the group «Microscopy Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +fluorescence, +phase, !confocal, xdarkfield

### NATURAL HISTORY MUSEUM  `natural_history_museum`
- правило: What is displayed in a natural history museum case
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +bones, +diorama, +fossil, +gemstones, +insects, +minerals, +skeleton

### NATURAL SCIENCES  `natural_sciences`
- правило: What belongs to the group «Natural Sciences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 7
- +botany, +chemistry, +ecology, +genetics, +geology, +physics, +zoology

### NUCLEAR PHYSICS  `nuclear_physics`
- правило: What belongs to the group «Nuclear Physics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +alpha, +atom, +beta decay, +fission

### NUMBER TYPES  `number_types`
- правило: What belongs to the group «Number Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +decimal, +fraction, +integer, +whole

### OLD TECH  `old_tech`
- правило: What belongs to the group «Old Tech» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 8
- +abacus, +cassette, +floppy, +floppy disk, +pager, +rotary phone, +telegram, +typewriter

### PERSUASIVE TECHNIQUES  `persuasive_techniques`
- правило: What belongs to the group «Persuasive Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bandwagon, +gaslighting, +rhetoric, !strawman

### PHOTOGRAPHY TECHNIQUES  `photography_techniques`
- правило: What belongs to the group «Photography Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +framing, +macro, +panning, !bokeh

### PHYSICAL ACTIONS  `physical_actions`
- правило: What belongs to the group «Physical Actions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +cuddle, +feel, +Pat, +shove

### PHYSICAL ACTIVITIES  `physical_activities`
- правило: What belongs to the group «Physical Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +climb, +jump, +rise, +run

### PHYSICAL HAZARDS  `physical_hazards`
- правило: What belongs to the group «Physical Hazards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +combustible, +flammable, +toxic, +volatile

### PHYSICAL THERAPY  `physical_therapy`
- правило: What belongs to the group «Physical Therapy» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +heat therapy, +massage, +stretching, +ultrasound

### PHYSICISTS  `physicists`
- правило: What belongs to the group «Physicists» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +Einstein, +Galileo, +Hawking, +Newton

### PHYSICS  `physics`
- правило: What belongs to the group «Physics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 29
- +astronomy, +dipole, +Einstein, +energy, +entropy, +force, +formula, +friction, +gravity, +inertia, +law, +magnet, +mass, +mechanics, +momentum, +motion, +particle, +photon, +photons, +quantum, +quarks, +speed, +thermodynamics, +torque, +velocity, +voltage, !bosons, !kinematics, !leptons

### PHYSICS BRANCHES  `physics_branches`
- правило: What belongs to the group «Physics Branches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 5
- +acoustics, +mechanics, +optics, +quantum, +thermodynamics

### PHYSICS CONCEPTS  `physics_concepts`
- правило: What belongs to the group «Physics Concepts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +energy, +force, +momentum, +velocity

### PHYSICS TERMS  `physics_terms`
- правило: What belongs to the group «Physics Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 10
- +atomic, +energy, +force, +gravity, +kinetic, +magnetic, +photon, +quantum, +thermal, +vortex

### PHYSICS UNITS  `physics_units`
- правило: What belongs to the group «Physics Units» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 6
- +ampere, +Newton, +pascal, +Tesla, +Watt, !joule

### PIGMENT CHEMISTRY  `pigment_chemistry`
- правило: What belongs to the group «Pigment Chemistry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +fugitive, !chromophore, !mordant, !tannin

### PLANETS  `planets`
- правило: Planets of our solar system
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- +Earth, +Jupiter, +Mars, +mercury (mercury_planet), +Neptune, +Pluto, +Saturn, +Uranus, +Venus, ?Earth, ?Jupiter, ?Mars, ?Neptune, ?Pluto, ?Saturn, ?Uranus, ?Venus, xmoons

### POP STARS  `pop_stars`
- правило: What belongs to the group «Pop Stars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +adele, +beyonce, +madonna, +rihanna

### POTTERY TECHNIQUES  `pottery_techniques`
- правило: What belongs to the group «Pottery Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +firing, +glazing, +throwing, !wedging

### PRIME NUMBERS  `prime_numbers`
- правило: What belongs to the group «Prime Numbers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 7
- +eleven, +five, +seven, +seventeen, +three, +twenty three, +two

### PRINTING TECHNIQUES  `printing_techniques`
- правило: What belongs to the group «Printing Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +digital, +etching, +inkjet, +laser, +lithograph, +woodcut, !gravure

### PRINTMAKING TECHNIQUES  `printmaking_techniques`
- правило: What belongs to the group «Printmaking Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +etching, +lithograph, +woodcut, !linocut

### QUANTUM PHYSICS  `quantum_physics`
- правило: What belongs to the group «Quantum Physics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +boson, +entanglement, +heisenberg, +photon, +quark, +spin, +superposition, !qubit

### RADIOACTIVE ELEMENTS  `radioactive_elements`
- правило: What belongs to the group «Radioactive Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +plutonium, +radium, +thorium, +uranium

### RARE ELEMENTS  `rare_elements`
- правило: What belongs to the group «Rare Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 9
- +cobalt, +iridium, +lithium, +nickel, +palladium, +uranium, !cerium, !osmium, !ruthenium

### RHETORIC TECHNIQUES  `rhetoric_techniques`
- правило: What belongs to the group «Rhetoric Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +ethos, +logos, +pathos, !anaphora

### GEOLOGY WORDS  `rock_cycle_words`
- правило: Words used to describe the earth and its rocks
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~core, ~crust, ~erosion, ~fault, ~fossil, ~glacier, ~lava, ~magma, ~mantle, ~mineral, ~plate (plate_tectonic), ~quarry, ~sediment, ~strata, ~tectonic, ~volcano

### ROOF TOP ELEMENTS  `roof_top_elements`
- правило: What belongs to the group «Roof Top Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +chimney, +gutter, +shingle, +vent

### SCIENCE  `science`
- правило: What belongs to the group «Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 12
- +analysis, +archaeology, +astronomy, +atom, +biology, +chemistry, +engineers, +gene, +inventors, +physics, +researchers, +scientists

### SCIENCE BRANCHES  `science_branches`
- правило: What belongs to the group «Science Branches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +biology, +chemistry, +physics, +psychology

### SCIENCE DISCIPLINES  `science_disciplines`
- правило: What belongs to the group «Science Disciplines» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +biology, +chemistry, +geology, +physics

### SCIENCE FAIR  `science_fair`
- правило: What a school science fair project is about or made of
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 12
- ~experiment, ~metals, ~minerals, ~trophy, ~volcano, +beaker, +hypothesis, +inventions, +poster, +volcanoes, !shapes, xposterboard

### SCIENCE FICTION  `science_fiction`
- правило: What belongs to the group «Science Fiction» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 13
- +Alien, +aliens, +cyberpunk, +cyborg, +galaxy, +laser, +laser gun, +robot, +space, +spaceship, +technology, +time loop, +utopia

### SCIENCE FICTION THEMES  `science_fiction_themes`
- правило: What belongs to the group «Science Fiction Themes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +cyborg, +dystopia, +time travel, +utopia

### BRANCHES OF SCIENCE  `science_fields`
- правило: Fields of scientific study
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +anatomy, +archaeology, +astronomy, +biology, +botany, +chemistry, +ecology, +genetics, +geology, +medicine, +meteorology, +physics, +psychology, +robotics, +zoology

### SCIENCE WORLD  `science_world`
- правило: What belongs to the group «Science World» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +chemistry, +lab, +microbe, +scientists

### SCIENTIFIC IMAGING TECHNIQUES  `scientific_imaging_techniques`
- правило: What belongs to the group «Scientific Imaging Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +crystallography, +microscopy, +radiography, +tomography

### SCIENTIFIC TECHNIQUES  `scientific_techniques`
- правило: What belongs to the group «Scientific Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +chromatography, +crystallography, +microscopy, +spectroscopy

### SHAPES  `shapes`
- правило: Geometric shapes taught in school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 36
- ~diamond (diamond_shape), ~pyramid (pyramid_shape), +arch (arch_structure), +circle, +cone, +crescent, +cube, +cylinder, +heart (heart_shape), +hexagon, +octagon, +oval, +Pentagon, +prism, +rectangle, +rhombus, +sphere, +Square, +star (star_shape), +torus, +trapezoid, +triangle, ?circle, ?cone, ?cube, ?cylinder, ?hexagon, ?oval, ?Pentagon, ?prism, ?rectangle, ?sphere, ?Square, ?trapezoid, ?triangle, xdecagon

### SOCIAL SCIENCES  `social_sciences`
- правило: What belongs to the group «Social Sciences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +anthropology, +economics, +psychology, +sociology

### SOIL SCIENCE  `soil_science`
- правило: What belongs to the group «Soil Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +leaching, +permeability, +topsoil, !humus

### SPACE EXPLORATION  `space_exploration`
- правило: What belongs to the group «Space Exploration» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 15
- +Apollo, +Artemis, +astronaut, +esa, +Hubble, +moon, +NASA, +rocket, +rover, +satellite, +shuttle, +spacex, +Sputnik, +Voyager, !Roscosmos

### SPACE MISSIONS  `space_missions`
- правило: What belongs to the group «Space Missions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 9
- +Apollo, +Artemis, +Cassini, +Gemini, +Hubble, +Luna, +Pioneer, +Soyuz, +Voyager

### SPACE OBJECTS  `space_objects`
- правило: Objects found in outer space
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~quasar, ~ring (ring_circle), +asteroid, +asteroid belt, +black hole, +cluster, +comet, +constellation, +dwarf planet, +galaxy, +meteor, +meteorite, +moon (moon_space), +nebula, +planet, +pulsar, +satellite, +star (star_space), +sun, +supernova

### SPACE PHYSICS  `space_physics`
- правило: What belongs to the group «Space Physics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +orbit, +radiation, +vacuum, !magnetosphere

### SPACE PIONEERS  `space_pioneers`
- правило: What belongs to the group «Space Pioneers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +aldrin, +Armstrong, +ride, !gagarin

### SPACE PROBES  `space_probes`
- правило: What belongs to the group «Space Probes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +Cassini, +Pioneer, +Sputnik, +Voyager

### STAGE ELEMENTS  `stage_elements`
- правило: What belongs to the group «Stage Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +backstage, +curtains, +props, +spotlight

### STAR CLUSTER  `star_cluster`
- правило: What belongs to the group «Star Cluster» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +globular, +nebula, +Orion, !pleiades

### STAR PATTERNS  `star_patterns`
- правило: What belongs to the group «Star Patterns» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Big Dipper, +Little Dipper, !orions belt, !scorpius

### STAR WARS  `star_wars`
- правило: What belongs to the group «Star Wars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 11
- +chewbacca, +clones, +darth vader, +death star, +empire, +force, +jedi, +leia, +lightsaber, +skywalker, +yoda

### STATES OF MATTER  `states_of_matter`
- правило: Physical states matter can take
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~solid (solid_matter), +crystal, +foam, +gas, +ice, +liquid, +mist, +plasma, +powder, +slush, +steam, +vapor

### TAPESTRY TECHNIQUES  `tapestry_techniques`
- правило: What belongs to the group «Tapestry Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +warp, !heddle, !selvedge, !weft

### TECH BILLIONAIRES  `tech_billionaires`
- правило: What belongs to the group «Tech Billionaires» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +bezos, +gates, +jobs, +musk

### TECHIE  `techie`
- правило: What belongs to the group «Techie» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +geek, +hacker, +nerd, +whiz

### TECHNICAL SKILLS  `technical_skills`
- правило: What belongs to the group «Technical Skills» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +coding, +drafting, +surveying, +welding

### TECHNOLOGY  `technology`
- правило: What belongs to the group «Technology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 7
- +3d printer, +computer, +drone, +robot, +satellite, +smartphone, +smartwatch

### TEMPERATURE WORDS  `temperature_words`
- правило: Words describing how hot or cold something is
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +blazing, +boiling, +chilly, +cold (cold_temperature), +cool, +freezing, +frigid, +frosty, +hot (hot_temperature), +icy, +lukewarm, +mild, +scalding, +sweltering, +tepid, +warm

### TEXTILE SCIENCE  `textile_science`
- правило: What belongs to the group «Textile Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +blend, +fabric types, +natural, +synthetic

### TEXTILE TECHNIQUES  `textile_techniques`
- правило: What belongs to the group «Textile Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +crochet, +embroidery, +knitting, +weaving

### THE AGE OF TECHNOLOGY  `the_age_of_technology`
- правило: What belongs to the group «The Age Of Technology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 4
- +blog, +code, +data science, +robots

### THEATER ELEMENTS  `theater_elements`
- правило: What belongs to the group «Theater Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +backdrop, +curtain, +stage, +wings

### ASTRONOMY WORDS  `things_in_the_sky_science`
- правило: Words used by astronomers
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +atmosphere, +comet, +constellation, +crater, +eclipse, +galaxy, +gravity, +light year, +meteor shower, +orbit, +phase, +rotation, +satellite, +solar system, +telescope, +universe

### THRILLER ELEMENTS  `thriller_elements`
- правило: What belongs to the group «Thriller Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +atmosphere, +plot twist, +suspense, +tension

### TRAFFIC ELEMENTS  `traffic_elements`
- правило: What belongs to the group «Traffic Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +crosswalk, +lane, +pedestrian, +vehicles

### TYPES OF NUMBERS  `types_of_numbers`
- правило: What belongs to the group «Types Of Numbers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +composite, +imaginary, +odd, +prime

### VISION SCIENCE  `vision_science`
- правило: What belongs to the group «Vision Science» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +cornea, +lens, +pupil, +retina

### VR TECH  `vr_tech`
- правило: What belongs to the group «Vr Tech» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +headset, +immersion, +latency, !haptics

### WATERCOLOR TECHNIQUES  `watercolor_techniques`
- правило: What belongs to the group «Watercolor Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +glaze, +lifting, +wash, +wet on wet

### WEATHER SCIENCE  `weather_science`
- правило: Scientific words used to describe weather
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~updraft, +air mass, +barometer, +condensation, +dew point, +evaporation, +forecast, +front, +humidity, +jet stream, +precipitation, +pressure, +radar, !isobar

### WEDDING ELEMENTS  `wedding_elements`
- правило: What belongs to the group «Wedding Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +bouquet, +chapel, +reception, +vows

### WORDS FOR STARE  `words_for_stare`
- правило: What belongs to the group «Words For Stare» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ogle, +squint, !gawk, !glower


## Тема: sounds

### ALARM SOUNDS  `bell_and_alarm`
- правило: Sounds made by alarms and signals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~alert, ~beep, ~bell, ~blare, ~buzz, ~chime, ~ding, ~gong, ~horn (horn_sound), ~siren, ~tone, ~whistle, +ring (ring_sound), !klaxon

### CITY SOUNDS  `city_sounds`
- правило: Sounds heard on a city street
- тип связи: `does_action`, базовая сложность 0.4
- слов: 18
- ~alarm, ~bell, ~brakes, ~chatter, ~footsteps, ~honk, ~hum, ~jackhammer, ~rumble, ~screech, ~shout, ~siren, ~whistle, +engine, +traffic, ?honk, ?rumble, ?screech

### KITCHEN SOUNDS  `kitchen_sounds`
- правило: Sounds heard in a kitchen
- тип связи: `does_action`, базовая сложность 0.45
- слов: 18
- ~boil, ~bubble, ~chop, ~clatter, ~clink, ~crunch (crunch_sound), ~ding, ~grind, ~hiss, ~pop (pop_sound), ~sizzle, ~slam, ~whisk, ?bubble, ?chop, ?clatter, ?sizzle, !whir

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
- слов: 16
- +Capella, +Castor, +constellations, +Polaris, +Sirius, +Vega, !Aldebaran, !Altair, !Antares, !Arcturus, !Betelgeuse, !Deneb, !Pollux, !Procyon, !Rigel, !Spica

### CONSTELLATIONS  `constellations`
- правило: Constellations in the night sky
- тип связи: `is_a`, базовая сложность 0.4
- слов: 30
- ~Cassiopeia, ~scorpius, +Andromeda, +Big Dipper, +Crux, +Cygnus, +dipper, +Draco, +Gemini, +Hercules, +Leo, +Little Dipper, +lynx, +Lyra, +Orion, +pegasus, +Perseus, +Polaris, +Taurus, +ursa, +Ursa Major, +Ursa Minor, ?Cassiopeia, ?Cygnus, ?Draco, ?Lyra, ?Orion, ?pegasus, ?Ursa Major, !Centaurus

### MOONS  `moons`
- правило: Named moons of the solar system
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- +Europa, +Ganymede, +Io, +Luna, +Miranda, +Rhea, +Titan, +triton, !Callisto, !Charon, !Deimos, !Enceladus, !Iapetus, !Phobos

### ROCKET PARTS  `rocket_parts`
- правило: Parts of a rocket
- тип связи: `part_of`, базовая сложность 0.4
- слов: 16
- +booster, +capsule, +engine, +fin, +fuel tank, +heat shield, +launch pad, +nose cone, +nozzle, +payload, +stage, +thruster, ?booster, ?engine, ?launch pad, ?nose cone

### SCI FI  `science_fiction_space`
- правило: Words used in space science fiction
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~Alien, ~android, ~colony, ~cyborg, ~galaxy, ~hyperdrive, ~laser, ~mothership, ~ray gun, ~starship, ~teleport, ~warp, ~wormhole, +force field

### SOLAR SYSTEM  `solar_system_words`
- правило: Words describing the solar system
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~kuiper belt, ~ring (ring_circle), +asteroid belt, +comet, +corona, +dwarf planet, +eclipse, +gravity, +meteor, +moon, +orbit, +planet, +solar wind, +sun

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
- слов: 18
- ~quasar, +aurora, +big bang, +black hole, +comet, +comet tail, +eclipse, +gravity well, +meteor, +meteor shower, +nebula, +orbit, +solar flare, +sunspot, +supernova, ?aurora, ?eclipse, ?supernova

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

