# Категории: правило и слова

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
- ~aphid, ~gnat, ~silkworm, +ant, +bee, +beetle, +butterfly, +caterpillar, +centipede, +cricket, +dragonfly, +firefly, +flea, +fly (fly_insect), +grasshopper, +hornet, +ladybug, +locust, +mosquito, +moth, +roach, +spider, +termite, +tick (tick_bug), +wasp

### JUNGLE ANIMALS  `jungle_animals`
- правило: Animals that live in tropical jungles and rainforests
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~macaw, ~tapir, ~toucan, +anteater, +boa, +chimpanzee, +frog, +gorilla, +iguana, +jaguar, +lemur, +leopard, +monkey, +orangutan, +panther, +parrot, +python, +sloth, +snake, +tiger

### NOCTURNAL ANIMALS  `nocturnal_animals`
- правило: Animals that are active at night and rest during the day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 21
- ~armadillo, ~badger, ~bat (bat_animal), ~beaver, ~cougar, ~coyote, ~cricket, ~firefly, ~fox, ~hamster, ~hedgehog, ~leopard, ~mole (mole_animal), ~moth, ~mouse (mouse_animal), ~opossum, ~owl, ~porcupine, ~raccoon, ~skunk, ~wolf

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


## Тема: art

### ART STYLES  `art_styles`
- правило: Named styles of visual art
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~cubism, +abstract, +art deco, +baroque, +expressionism, +folk art, +gothic, +impressionism, +minimalism, +modernism, +pop art, +realism, +renaissance, +surrealism

### ART TOOLS  `art_tools`
- правило: Tools an artist uses to make art
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~mold (mold_form), +airbrush, +brush, +canvas, +charcoal, +chisel, +easel, +kiln, +knife, +loom, +palette, +pen (pen_writing), +pencil, +roller, +sponge (sponge_cleaning), +stylus

### CALLIGRAPHY  `calligraphy`
- правило: A term belonging to fine handwriting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~penmanship, +cursive, +flourish, +italic, +lettering

### SHADES OF COLOR  `color_words_advanced`
- правило: Words for particular shades of color
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~lavender (lavender_color), ~mint (mint_color), ~sage (sage_color), +amber, +azure, +blush, +charcoal, +cobalt, +coral, +crimson, +ivory, +jade, +mauve, +mustard, +ochre, +olive, +plum, +rust, +scarlet, !cream (cream_color)

### CRAFTS  `crafts`
- правило: Handmade crafts people do as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~beading, ~macrame, ~scrapbooking, +calligraphy, +candle making, +crochet, +embroidery, +knitting, +origami, +pottery, +quilting, +sewing, +soap making, +weaving, +woodworking

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
- слов: 14
- ~bead, ~chain, ~clasp, ~cord, ~gem, ~hook (hook_fastener), ~pendant, ~pliers, ~ring blank, ~setting, ~solder, ~thread, ~wire, !mold (mold_form)

### MUSEUM WORDS  `museum_words`
- правило: Things found in an art museum
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~docent, +admission, +audio tour, +collection, +curator, +exhibit, +frame, +gallery, +gift shop, +guide, +painting, +pedestal, +plaque, +portrait, +rope, +sculpture

### KINDS OF PAINT  `paint_types`
- правило: Kinds of paint used by artists and decorators
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~gouache, ~tempera, +acrylic, +chalk paint, +enamel, +finger paint, +latex, +primer, +spray, +varnish, +watercolor, !oil (oil_paint)

### PHOTO SUBJECTS  `photography_styles`
- правило: Kinds of pictures a photographer takes
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- +action shot, +aerial, +candid, +close up, +group shot, +landscape, +macro, +panorama, +portrait, +selfie, +silhouette, +still life, +wedding photo

### POTTERY STUDIO  `pottery_studio`
- правило: A material or ware made in a pottery studio
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- +ceramic, +earthenware, +terracotta, +urn, ?kilnfire

### POTTERY WORDS  `pottery_words`
- правило: Things used in making pottery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bowl, ~clay, ~fire, ~glaze, ~kiln, ~mold (mold_form), ~plaster, ~pot, ~sculpt, ~slip, ~tile, ~vase, ~wheel, !trim (trim_cut)

### SCULPTORS STUDIO  `sculptors_studio`
- правило: Something a sculptor makes or mounts work on
- тип связи: `used_in`, базовая сложность 0.65
- слов: 4
- +figurine, +mould, +pedestal, +plinth

### SCULPTURE MATERIALS  `sculpture_materials`
- правило: Materials sculptors carve or cast
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~soapstone, +bronze, +clay, +concrete, +glass, +granite, +ice, +marble (marble_stone), +metal, +plaster, +sand, +stone, +wax (wax_substance), +wood

### STREET ART  `street_art`
- правило: A form or technique of street art
- тип связи: `is_a`, базовая сложность 0.55
- слов: 4
- +graffiti, +mural, +stencil, +tagging

### TEXTURES  `textures`
- правило: Words describing how a surface feels
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~bumpy, ~coarse, ~fuzzy, ~glossy, ~grainy, ~matte, ~polished, ~prickly, ~ridged, ~rough, ~silky, ~slick, ~smooth, ~sticky, ~velvety

### PERFORMING ARTS  `theater_arts`
- правило: Arts performed in front of an audience
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~puppetry, +ballet, +circus, +comedy, +concert, +dance, +improv, +magic, +mime, +musical, +opera, +play, +poetry reading, +recital


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
- слов: 18
- +Audi, +BMW, +Buick, +Chevrolet, +Dodge, +ford (ford_brand), +Honda, +Hyundai, +Jeep, +Kia, +Lexus, +Mazda, +Mercedes, +Nissan, +Subaru, +Toyota, +Volkswagen, +Volvo

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
- слов: 34
- +account, +allowance, +bank (bank_finance), +bill (bill_money), +bonus, +budget, +capital (capital_money), +cash, +cent, +change, +check (check_payment), +coin, +credit, +debit, +debt, +deposit, +dime, +dollar, +euro, +fee, +interest, +invoice, +loan, +quarter (quarter_coin), +receipt, +refund, +rent, +salary, +savings, +tax, +teller, +tip (tip_money), +wage, +wallet

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

### TICKETS AND PASSES  `tickets_and_passes`
- правило: A word belonging to paying to enter or travel
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 6
- +entry, +fare, +pass, +receipt, +stub, +voucher

### TRADING FLOOR  `trading_floor`
- правило: A term used trading shares
- тип связи: `used_in`, базовая сложность 0.65
- слов: 5
- +broker, +bullish, +dividend, +portfolio, +ticker


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


## Тема: food

### ASIAN DISHES  `asian_dishes`
- правило: Dishes from East and Southeast Asian cuisines eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bibimbap, ~satay, ~tempura, ~wonton, +chow mein, +curry, +dim sum, +dumpling, +egg roll, +fried rice, +kimchi, +lo mein, +miso soup, +pad thai, +pho, +ramen, +sashimi, +spring roll, +sushi, +teriyaki

### BAKED GOODS  `baked_goods`
- правило: Something baked from dough or batter in an oven
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +bagel, +bread, +cake, +cookie, +croissant, +donut, +muffin, +pie

### BAKING INGREDIENTS  `baking_ingredients`
- правило: Ingredients commonly used to bake cakes, bread or cookies
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~oil (oil_cooking), +almond, +baking powder, +baking soda, +butter, +buttermilk, +chocolate, +cinnamon, +cocoa, +cream (cream_dairy), +egg, +flour, +frosting, +honey, +icing, +milk, +molasses, +oat, +raisin, +salt, +shortening, +sugar, +syrup, +vanilla, +yeast

### BARBECUE  `barbecue`
- правило: Something you cook with or over at a barbecue
- тип связи: `used_in`, базовая сложность 0.35
- слов: 6
- +burger, +charcoal, +grill, +ribs, +smoke, +tongs

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
- слов: 28
- +bacon, +bagel, +biscuit, +bread, +cereal, +coffee cake, +croissant, +danish, +doughnut, +egg, +french toast, +granola, +grits, +ham, +hash brown, +jam, +milk, +muffin, +oatmeal, +omelet, +pancake, +porridge, +rice, +sausage, +scone, +toast (toast_bread), +waffle, +yogurt

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
- слов: 21
- ~aioli, +barbecue sauce, +chutney, +honey, +horseradish, +hot sauce, +jam, +ketchup, +mayo, +mustard, +pesto, +ranch, +relish, +salsa, +sauces, +soy sauce, +sriracha, +syrup, +tartar sauce, +vinegar, +wasabi

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

### EVERYDAY DRINKS  `everyday_drinks`
- правило: A common non alcoholic drink
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +cocoa, +coffee, +juice, +lemonade, +milk, +smoothie, +soda, +tea

### DRIVE THRU  `fast_food_items`
- правило: Items ordered at an American fast food counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~quesadilla, +biscuit, +burger, +burrito, +chicken sandwich, +chili (chili_dish), +corn dog, +fries, +hot dog, +milkshake, +mozzarella stick, +nugget, +onion ring, +pizza, +slider, +soda, +sub, +sundae, +taco, +wrap

### FOOD GROUPS  `food_groups`
- правило: One of the food groups a balanced diet is divided into
- тип связи: `member_of_set`, базовая сложность 0.3
- слов: 6
- +dairy, +fruit, +grains, +meat, +protein, +vegetables

### FROZEN FOODS  `frozen_foods`
- правило: Foods normally bought from the freezer aisle
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~tater tot, +berries, +burrito, +chicken nugget, +corn dog, +dumpling, +fish stick, +french fries, +hash brown, +ice cream, +lasagna, +peas, +pizza, +Popsicle, +pot pie, +sorbet, +spinach, +waffle

### FRUITS  `fruits`
- правило: Common edible fruits familiar to an average American adult
- тип связи: `is_a`, базовая сложность 0.1
- слов: 27
- ~date (date_fruit), +apple (apple_fruit), +apricot, +banana, +berries, +blackberry, +blueberry, +cantaloupe, +cherry, +cranberry, +grape, +grapefruit, +kiwi, +lemon, +lime, +mango, +nectarine, +orange (orange_fruit), +papaya, +peach, +pear, +pineapple, +plum, +raspberry, +strawberry, +tangerine, +watermelon

### GRAINS AND BEANS  `grains_and_beans`
- правило: Grains, beans and other dried staples cooked as food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +barley, +black bean, +chickpea, +corn, +couscous, +kidney bean, +lentil, +millet, +oat, +pinto bean, +quinoa, +rice, +rye, +soybean, +wheat

### GROCERY AISLES  `grocery_aisles`
- правило: The sections a supermarket is divided into
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- +bakery, +dairy, +Frozen, +fruits, +meats, +seafood, +vegetables

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

### IN A SALAD  `in_a_salad`
- правило: An ingredient tossed into a green salad
- тип связи: `used_in`, базовая сложность 0.3
- слов: 6
- ~croutons, +cucumber, +dressing, +lettuce, +olives, +tomato

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

### LUNCH MENU  `lunch_menu`
- правило: A quick hot dish ordered for lunch
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +burger, +fries, +hotdog, +pizza, +salad, +sandwich, +steak, +taco

### MEALS OF THE DAY  `meals_of_the_day`
- правило: A meal or course eaten at a set time of day
- тип связи: `member_of_set`, базовая сложность 0.2
- слов: 7
- +breakfast, +brunch, +dessert, +dinner, +lunch, +snack, +supper

### MEATS  `meats`
- правило: Kinds of meat sold at an American butcher counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~pastrami, ~turkey (turkey_meat), +bacon, +beef, +bologna, +brisket, +chicken, +chop, +ground beef, +ham, +hot dog, +jerky, +lamb, +liver, +meatball, +pepperoni, +pork, +ribs, +roast, +salami, +sausage, +steak, +veal, +venison, !duck (duck_meat)

### MEXICAN DISHES  `mexican_dishes`
- правило: Dishes from Mexican cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- ~carnitas, ~churro, ~empanada, ~fajita, ~flan, ~horchata, ~pozole, ~quesadilla, ~tostada, +burrito, +enchilada, +guacamole, +nacho, +queso, +salsa, +taco, +tamale, +tortilla, !elote, !mole (mole_sauce), xchile relleno

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
- слов: 19
- ~penne, +angel hair, +gnocchi, +lasagna, +linguine, +macaroni, +noodle, +ravioli, +shells, +spaghetti, !cannelloni, !farfalle, !fettuccine, !orzo, !rigatoni, !tortellini, !vermicelli, !ziti, xrotini

### PASTRIES  `pastries`
- правило: A small sweet baked pastry sold in a bakery
- тип связи: `is_a`, базовая сложность 0.35
- слов: 8
- +biscuit, +croissant, +cupcake, +donut, +eclair, +muffin, +scone, +tart

### PICNIC  `picnic`
- правило: Something you pack or spread out for a picnic
- тип связи: `used_in`, базовая сложность 0.3
- слов: 7
- +basket, +blanket, +cooler, +hamper, +lemonade, +sandwich, +thermos

### PICNIC BASKET  `picnic_basket`
- правило: What you pack or bring for a picnic
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- ~condiments, ~napkins, +blanket, +desserts, +fruits, +salads, +thermos

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

### RESTAURANT COURSES  `restaurant_courses`
- правило: A course listed in order on a restaurant menu
- тип связи: `member_of_set`, базовая сложность 0.35
- слов: 6
- +appetizer, +dessert, +entree, +salad, +soup, +starter

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

### SALTY SNACKS  `salty_snacks`
- правило: A salty snack eaten from a packet or bowl
- тип связи: `is_a`, базовая сложность 0.3
- слов: 6
- +chips, +crackers, +nachos, +peanut, +popcorn, +pretzel

### SANDWICH FILLINGS  `sandwich_fillings`
- правило: Things commonly put inside a sandwich
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~pastrami, ~turkey (turkey_meat), +avocado, +bacon, +cheese, +chicken, +coleslaw, +corned beef, +cucumber, +egg salad, +ham, +hummus, +jelly, +lettuce, +mayo, +meatball, +mustard, +onion, +peanut butter, +pickle, +roast beef, +salami, +sprouts, +tomato, +tuna

### SEAFOOD  `seafood`
- правило: Fish and shellfish eaten as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 26
- ~mahi mahi, +anchovy, +catfish, +caviar, +clam, +cod, +crab, +crawfish, +eel, +halibut, +herring, +lobster, +mussel, +octopus, +oyster, +salmon, +sardine, +scallop, +shellfish, +shrimp, +snapper, +squid, +swordfish, +tilapia, +trout, +tuna

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

### SWEETS  `sweets`
- правило: A sweet treat eaten as a snack
- тип связи: `is_a`, базовая сложность 0.2
- слов: 7
- +brownie, +candy, +caramel, +cookie, +fudge, +lollipop, +toffee

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
- слов: 26
- +artichoke, +asparagus, +bean, +beet, +broccoli, +cabbage, +carrot, +cauliflower, +celery, +corn, +cucumber, +eggplant, +kale, +leek, +lettuce, +onion, +parsnip, +pea, +peppers, +potato, +radish, +spinach, +squash (squash_vegetable), +tomato, +turnip, +zucchini


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


## Тема: hobbies

### BIRDWATCHING THINGS  `birdwatching`
- правило: Things a birdwatcher uses
- тип связи: `used_in`, базовая сложность 0.4
- слов: 12
- +binoculars, +bird bath, +birdhouse, +blind, +camera, +checklist, +feeder, +field guide, +notebook, +scope, +seed, +whistle

### GAME PIECES  `board_game_pieces`
- правило: Pieces and parts used in board games
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~card (card_playing), +board (board_game), +chip, +cup, +dice (dice_game), +marker, +pawn, +rulebook, +spinner, +tile, +timer, +token, ?scorepad, xmeeple

### CAMPING GEAR  `camping_gear`
- правило: Gear packed for a camping trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 22
- +backpack, +bug spray, +camp chair, +campfire, +canteen, +compass, +cooler, +firewood, +first aid kit, +flashlight, +hatchet, +lantern, +map, +marshmallow, +matches, +mess kit, +rope, +sleeping bag, +stove, +tarp, +tent, +thermos

### CANDLE MAKING  `candle_making`
- правило: A word belonging to making candles
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +paraffin, +scented, +taper, +wick

### CARD SUITS  `card_suits`
- правило: One of the four suits in a deck of playing cards
- тип связи: `member_of_set`, базовая сложность 0.25
- слов: 4
- +clubs, +diamonds, +hearts, +spades

### CHESS WORDS  `chess_words`
- правило: Pieces and moves in a game of chess
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~board (board_game), ~check (check_chess), ~en passant, ~queen (queen_card), +bishop, +capture, +castle, +checkmate, +gambit, +king, +knight, +opening, +pawn, +promotion, +rook, +stalemate

### COLLECTIBLES  `collecting_hobbies`
- правило: Things people collect as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~button (button_clothing), ~card (card_playing), ~marble (marble_toy), ~matchbook, ~rock (rock_stone), +autograph, +badge, +bottle cap, +coin, +comic, +doll, +figurine, +magnet, +postcard, +record, +shell, +spoon, +stamp (stamp_postage), +thimble, !key (key_lock)

### HOME BAKING  `cooking_hobby`
- правило: Things a home baker uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~sheet (sheet_pan), ~sifter, +apron (apron_garment), +cooling rack, +cutter, +measuring cup, +mitt, +mixing bowl, +oven, +piping bag, +rolling pin, +spatula, +timer, +whisk, !mold (mold_form), !scale (scale_weigh)

### CRAFT MATERIALS  `crafting_materials`
- правило: Materials used in craft projects
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~button (button_clothing), +bead, +cardboard, +clay, +fabric, +felt, +foam, +glitter, +glue, +paint, +paper, +pipe cleaner, +popsicle stick, +ribbon, +sequin, +string, +wire, +yarn

### DANCE CLASS  `dance_class`
- правило: Things found in a dance class
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- +barre, +instructor, +leotard, +mat, +mirror, +music, +pointe shoe, +routine, +slippers, +spin, +stage, +stretch, +tights, +tutu

### FISHING TRIP  `fishing_hobby`
- правило: Things taken on a fishing trip
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~waders, +bait, +boat, +bucket, +cooler, +hat, +hook (hook_fishing), +license, +line (line_cord), +lure, +net, +reel (reel_fishing), +rod, +stringer, +sunscreen, +tackle box

### GARDEN HOBBY  `gardening_hobby`
- правило: Things a hobby gardener uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~pruner, +compost bin, +fertilizer, +gloves, +greenhouse, +hose, +planter, +pot, +seed packet, +soil, +stake, +trellis, +trowel, +twine, +watering can, +wheelbarrow

### GARDENING WORK  `gardening_work`
- правило: A task or tool belonging to working a garden
- тип связи: `used_in`, базовая сложность 0.35
- слов: 7
- ~trowel, +compost, +pruning, +seedlings, +soil, +watering, +weeding

### HIKING WORDS  `hiking_words`
- правило: Things involved in hiking a trail
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~switchback, +backpack, +blaze, +blister, +boots, +cairn, +campsite, +canteen, +elevation, +map, +poles, +ridge, +summit, +trail, +trailhead, +water bottle

### HOBBY ACTIVITIES  `hobby_verbs`
- правило: Activities people do as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~birdwatching, +baking, +camping, +chess, +collecting, +cycling, +dancing, +drawing, +fishing, +gardening, +hiking, +knitting, +painting, +photography, +reading, +running, +sewing, +singing, +woodworking, +writing

### KNITTING WORDS  `knitting_words`
- правило: Things used in knitting and crochet
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~ball (ball_sphere), ~bind off, ~cast on, ~gauge, ~loop, ~marker, ~needle (needle_sewing), ~pattern, ~purl, ~row, ~stitch, ~yarn, !hook (hook_crochet), !skein

### MAGIC PROPS  `magic_tricks`
- правило: Props used in performing magic tricks
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~ball (ball_sphere), ~coin, ~dove, ~handcuff, ~hat, ~mirror, ~ring (ring_circle), ~rope, ~scarf, ~thumb tip, ~wand, +box, +cup, !card (card_playing)

### MODEL KITS  `model_building`
- правило: Things used to build scale models
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~brush, ~clamp, ~decal, ~glue, ~instructions, ~kit, ~knife, ~paint, ~plastic, ~putty, ~sandpaper, ~tweezers, +base, !scale (scale_ratio)

### MUSIC PRACTICE  `music_practice`
- правило: Things used when practicing an instrument
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~bench (bench_seat), ~bow (bow_music), +amplifier, +capo, +metronome, +mute, +pick, +reed, +rosin, +sheet music, +stand (stand_holder), +strap, +tuner, !case (case_box)

### PHOTOGRAPHY GEAR  `photography_hobby`
- правило: Gear a hobby photographer uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~hood (hood_lens), ~lightbox, +backdrop, +bag, +battery, +camera, +filter, +flash, +lens, +memory card, +reflector, +strap, +tripod, !remote (remote_device)

### PUZZLES  `puzzle_types`
- правило: Kinds of puzzle people solve for fun
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~acrostic, ~brainteaser, ~cryptogram, ~rubiks cube, ~tangram, +anagram, +crossword, +jigsaw, +logic puzzle, +maze, +rebus, +riddle, +sudoku, +word search

### SCRAPBOOKING  `scrapbooking`
- правило: A material or keepsake used making a scrapbook
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- +cutouts, +keepsake, +laminate, +stickers

### GAMING SETUP  `video_gaming`
- правило: Things in a video gaming setup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~mouse (mouse_computer), ~mousepad, +cable, +cartridge, +chair, +console, +controller, +disc, +headset, +keyboard (keyboard_computer), +memory card, +microphone, +monitor (monitor_screen), +webcam


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
- ~atlas (atlas_book), +biography, +cookbook, +encyclopedia, +fantasy, +history, +horror, +humor, +memoir, +mystery, +poetry, +romance, +science fiction, +self help, +textbook, +thriller, +travel, +western

### CARTOON CHARACTERS  `cartoon_characters`
- правило: Classic cartoon characters
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~Tweety, +Betty Boop, +Bugs Bunny, +Daffy, +Donald, +Garfield, +Goofy, +Jerry, +Mickey, +Pluto, +Popeye, +Porky, +Scooby, +Snoopy, +Sylvester, +tom, +woody, +Yogi

### CLASSIC NOVELS  `classic_novels`
- правило: Classic novels widely read in school
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Call of the Wild, +Dracula, +Frankenstein, +Great Expectations, +Great Gatsby, +Gulliver, +Huckleberry Finn, +Jane Eyre, +Little Women, +Of Mice and Men, +Oliver Twist, +Robinson Crusoe, +Tom Sawyer, +Treasure Island, +Wuthering Heights

### COMIC BOOKS  `comic_words`
- правило: Words used about comic books
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~cape, ~graphic novel, ~hero, ~origin, ~panel, ~sidekick, ~speech bubble, ~strip, ~villain, +artist, +cover, +issue, +series, !inker

### DISNEY CHARACTERS  `disney_characters`
- правило: Characters from Disney animated films
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~Tinkerbell, +Aladdin, +Anna, +Ariel, +Bambi, +Belle, +buzz, +Cinderella, +Dumbo, +Elsa, +Jasmine, +Moana, +Mulan, +Nemo, +Peter Pan, +Pinocchio, +Pocahontas, +Rapunzel, +Simba, +Snow White

### FAIRY TALES  `fairy_tales`
- правило: Classic fairy tales children know
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Hansel and Gretel, ~Jack and the Beanstalk, ~Rumpelstiltskin, ~Thumbelina, +Beauty and the Beast, +Cinderella, +Goldilocks, +Little Mermaid, +Pinocchio, +Rapunzel, +Red Riding Hood, +Sleeping Beauty, +Snow White, +Three Little Pigs, +Ugly Duckling

### FAMOUS MOVIES  `famous_movies`
- правило: Films most Americans have heard of
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~titanic (titanic_movie), +Alien, +avatar, +Braveheart, +Casablanca, +Frozen, +Ghostbusters, +gladiator, +Godfather, +Grease, +Jaws, +Jurassic Park, +Psycho, +Rocky, +Shrek, +Star Wars, +Terminator, +Wizard of Oz

### MUSIC LEGENDS  `famous_musicians`
- правило: Musicians widely known across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Armstrong, +Bach, +Beatles, +Beethoven, +cash, +Chopin, +Dylan, +Ellington, +Elvis, +Gershwin, +Hendrix, +Mozart, +Presley, +Sinatra

### GAME SHOWS  `game_shows`
- правило: Things found on a television game show
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~board (board_game), ~round (round_stage), +audience, +buzzer, +category, +contestant, +host (host_presenter), +jackpot, +lifeline, +podium, +prize, +question, +spin, +trophy, +wheel

### HERO HQ  `hero_hq`
- правило: A word belonging to comic book superheroes
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +catchphrase, +nemesis, +sidekick, +vigilante

### KINDS OF BOOKS  `kinds_of_books`
- правило: A kind of book classed by how it is written
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +biography, +essay, +fable, +fiction, +memoir, +novel, +poetry

### MAGAZINE TYPES  `magazines`
- правило: Kinds of magazine sold at a newsstand
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +business, +comic, +cooking, +fashion, +gardening, +gossip, +hobby, +news, +parenting, +science, +sports, +tabloid, +teen, +trade, +travel

### FILM CREW  `movie_roles`
- правило: Jobs in the crew of a film production
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +actor, +cameraman, +casting director, +composer, +costume designer, +director, +editor, +extra, +gaffer, +makeup artist, +producer, +screenwriter, +set designer, +sound engineer, +stunt double

### NEWSPAPER PARTS  `newspaper_parts`
- правило: Sections and parts of a newspaper
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- +advice, +byline, +classifieds, +column, +comics, +crossword, +editorial, +front page, +headline, +horoscope, +letters, +obituary, +review, +sports, +weather

### NEWSROOM  `newsroom`
- правило: A person or item of a working newsroom
- тип связи: `found_in`, базовая сложность 0.55
- слов: 5
- +byline, +columnist, +newsflash, +reporter, +tabloid

### NURSERY RHYMES  `nursery_rhymes`
- правило: Nursery rhymes American children learn
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Humpty Dumpty, ~Itsy Bitsy Spider, +Baa Baa Black Sheep, +Jack and Jill, +Little Bo Peep, +London Bridge, +Mary Had a Little Lamb, +Old MacDonald, +Row Your Boat, +Three Blind Mice, +Twinkle Twinkle, !Hickory Dickory Dock

### RADIO STATION  `radio_station`
- правило: A term belonging to radio broadcasting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +airwaves, +broadcaster, +static, +transmitter

### RADIO WORDS  `radio_words`
- правило: Things and roles in radio broadcasting
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~station (station_place), +antenna, +broadcast, +call sign, +dial, +DJ, +frequency, +jingle, +playlist, +static, +studio, +transmitter, +tuner, !airwave, !host (host_presenter)

### RETRO MUSIC  `retro_music`
- правило: A way music was played or carried before streaming
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +mixtape, +stereo, +vinyl, +walkman

### SHAKESPEARE PLAYS  `shakespeare_plays`
- правило: Plays written by Shakespeare
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +As You Like It, +Hamlet, +Julius Caesar, +King Lear, +Macbeth, +Merchant of Venice, +Midsummer Night, +Much Ado, +othello, +Richard III, +Romeo and Juliet, +Taming of the Shrew, +Tempest, +Twelfth Night

### SPY MISSION  `spy_mission`
- правило: A trick or item used by a spy
- тип связи: `used_in`, базовая сложность 0.6
- слов: 5
- +alias, +decoy, +dossier, +infiltrate, +wiretap

### SUPERHEROES  `superheroes`
- правило: Comic book superheroes most people can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +Ant Man, +Aquaman, +Batman, +Black Widow, +Captain America, +Daredevil, +flash, +Green Lantern, +Hulk, +Iron Man, +robin, +Spiderman, +storm, +Supergirl, +Superman, +Thor, +wolverine, +Wonder Woman

### THE HEIST  `the_heist`
- правило: A word belonging to robbing a place in a film
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +getaway, +heist, +lookout, +loot

### TV GENRES  `tv_genres`
- правило: Kinds of television program
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +cartoon, +cooking show, +crime show, +documentary, +drama, +game show, +mini series, +news, +reality, +sitcom, +soap opera, +sports, +talent show, +talk show, +variety show


## Тема: medicine

### AT THE DENTIST  `at_the_dentist`
- правило: Something a dentist fits, treats or hands out
- тип связи: `found_in`, базовая сложность 0.45
- слов: 5
- +braces, +dentures, +floss, +fluoride, +toothache

### AT THE HOSPITAL  `at_the_hospital`
- правило: Someone or something found in a hospital
- тип связи: `found_in`, базовая сложность 0.3
- слов: 8
- +bandage, +clinic, +hospital, +medicine, +nurse, +patient, +stethoscope, +ward

### BODY FLUIDS  `body_fluids`
- правило: Fluids produced by the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~bile, ~lymph, ~mucus, ~plasma, ~saliva, ~serum, ~sputum, ~sweat, ~tear, ~urine, +blood, +milk

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

### FEELING SICK  `feeling_sick`
- правило: A symptom or minor illness a person complains of
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- +chills, +cold (cold_illness), +cough, +fever, +flu, +headache, +sneeze

### FIRST AID  `first_aid`
- правило: Things kept in a first aid kit
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- +antiseptic, +aspirin, +bandage, +burn cream, +cotton ball, +eye wash, +gauze, +gloves, +ice pack, +ointment, +scissors, +sling, +splint, +tape, +thermometer, +tourniquet, +tweezers, +wipe

### HOSPITAL DEPARTMENTS  `hospital_departments`
- правило: Departments and units inside a hospital
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- +admissions, +cardiology, +dialysis, +emergency, +intensive care, +laboratory, +maternity, +morgue, +oncology, +pediatrics, +pharmacy, +physical therapy, +radiology, +recovery, +surgery

### HYGIENE THINGS  `hygiene`
- правило: Things used to keep the body clean
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- +comb, +cotton swab, +deodorant, +floss, +lotion, +mouthwash, +nail clipper, +razor, +sanitizer, +shampoo, +soap, +tissue (tissue_paper), +toothbrush, +toothpaste, +towel, +washcloth

### INJURIES  `injuries`
- правило: Kinds of physical injury
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~bite (bite_wound), +blister, +break, +bruise, +burn, +concussion, +cut, +dislocation, +fracture, +frostbite, +laceration, +puncture, +scrape, +splinter, +sprain, +strain, +sunburn, +whiplash

### KINDS OF DOCTORS  `kinds_of_doctors`
- правило: A doctor named for the field they specialise in
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +allergist, +cardiologist, +dentist, +dietitian, +pediatrician, +surgeon

### MEDICAL SPECIALTIES  `medical_specialties`
- правило: Branches of medical practice
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~geriatrics, ~orthopedics, +anesthesia, +cardiology, +dermatology, +immunology, +neurology, +obstetrics, +oncology, +pathology, +pediatrics, +psychiatry, +radiology, +surgery, +urology

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

### MEDICINES  `medicines`
- правило: A form in which medicine is given to a patient
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +antibiotic, +injection, +insulin, +ointment, +pill, +syrup, +vaccine

### NUTRIENTS  `nutrients`
- правило: A nutrient the body needs from food
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +calcium, +fiber, +iron (iron_metal), +magnesium, +protein, +zinc

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
- слов: 18
- ~jetlag, ~sleepwalk, +alarm, +apnea, +bedtime, +doze, +dream, +drowsy, +insomnia, +lullaby, +mattress, +nap, +nightmare, +pillow, +rest (rest_sleep), +slumber, +snore, +yawn

### SUPPLEMENTS  `supplements`
- правило: A substance sold as a dietary or beauty supplement
- тип связи: `is_a`, базовая сложность 0.5
- слов: 6
- +biotin, +collagen, +keratin, +probiotic, +vitamin, +zinc

### THERAPY WORDS  `therapy_words`
- правило: Words used in physical and mental therapy
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~appointment, ~brace, ~counselor, ~crutch, ~exercise, ~massage, ~progress, ~recovery, ~rehab, ~session, ~stretch, ~walker, +goal, +treatment

### VET CLINIC  `vet_clinic`
- правило: A procedure or item used treating animals
- тип связи: `used_in`, базовая сложность 0.55
- слов: 4
- ~neutering, +checkup, +microchip, +muzzle

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

### WELLNESS  `wellness`
- правило: A practice people take up to feel healthier
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +balance, +detox, +diet, +hydration, +meditation, +yoga


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

### GREEK MYTHS  `greek_myths`
- правило: A creature or place from Greek mythology
- тип связи: `found_in`, базовая сложность 0.55
- слов: 5
- +centaur, +cyclops, +minotaur, +Olympus, +Titan

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

### POTIONS CLASS  `potions_class`
- правило: A word belonging to brewing magic potions
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +antidote, +bubbling, +concoction, +elixir, +tincture, +vial

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

### WIZARD TOWER  `wizard_tower`
- правило: A word belonging to wizards and spellcasting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~grimoire, +conjure, +enchanted, +incantation

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
- ~plane (plane_aircraft), +aurora, +cloud, +comet, +constellation, +eclipse, +galaxy, +meteor, +Milky Way, +moon, +planet, +satellite, +shooting star, +star (star_space)

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


## Тема: ocean

### AT THE HARBOR  `at_the_harbor`
- правило: A structure or vessel found in a harbour
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- +anchor, +dock, +ferry, +Lighthouse, +pier, +port

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
- слов: 15
- ~hood (hood_garment), +buoy, +compass, +dive knife, +fins, +flashlight, +flipper, +gauge, +gloves, +mask, +regulator, +snorkel, +tank (tank_container), +weight belt, +wetsuit

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

### OCEAN FLOOR  `ocean_floor`
- правило: Something resting or growing on the ocean floor
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- +anchor, +coral, +reef, +seaweed, +shipwreck, +sponge (sponge_animal)

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

### SET SAIL  `set_sail`
- правило: A part of a sailing boat above the deck
- тип связи: `part_of`, базовая сложность 0.6
- слов: 4
- +helm, +jib, +mast, +spinnaker

### SHARKS AND RAYS  `sharks_and_rays`
- правило: Kinds of shark and ray
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~thresher, +bull shark, +great white, +hammerhead, +mako, +manta ray, +nurse shark, +reef shark, +stingray, +tiger shark, +whale shark, !sawfish

### SHELLFISH  `shellfish`
- правило: Sea animals with a shell that people eat
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~whelk, +abalone, +barnacle, +clam, +cockle, +crab, +crawfish, +crustaceans, +lobster, +mussel, +oyster, +prawn, +scallop, +shrimp, +snail

### SEASHELLS  `shells`
- правило: Kinds of seashell found on a beach
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~abalone, ~auger, ~clam, ~cockle, ~conch, ~mussel, ~nautilus, ~olive shell, ~oyster, ~sand dollar, ~scallop, !cowrie, !whelk

### SUBMARINE DUTY  `submarine_duty`
- правило: A word belonging to serving aboard a submarine
- тип связи: `associated_with`, базовая сложность 0.65
- слов: 4
- +ballast, +nautical, +seabed, +submerge

### WHALE WATCH  `whale_watch`
- правило: A word belonging to whales and watching them
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~baleen, ~blowhole, ~narwhal, +breaching, +krill

### FISHING FLEET  `whaling_and_fishing`
- правило: Things used in commercial fishing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~buoy, ~crate, ~dredge, ~gaff, ~harpoon, ~hold, ~hook (hook_fishing), ~line (line_cord), ~net, ~pot, ~Seine, ~trap, ~trawler, ~winch


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
- ~ford (ford_person), +bell, +diesel, +Edison, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Tesla, +Watt, +Whitney, +Wright, !Daguerre

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


## Тема: properties

### BLACK THINGS  `black_things`
- правило: Everyday things that are typically black in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~asphalt, ~bat (bat_animal), ~chalkboard, ~coal, ~crow, ~ink, ~licorice, ~oil (oil_motor), ~olive, ~panther, ~piano key, ~pupil, ~raven, ~Shadow, ~soot, ~tire, ~tuxedo, +night

### COLD THINGS  `cold_things`
- правило: Things that are cold by their physical nature
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~chill, ~freezer, ~frost, ~glacier, ~hail, ~ice cube, ~iceberg, ~icicle, ~permafrost, ~Popsicle, ~refrigerator, ~sleet, ~slush, ~snowball, ~sorbet, +ice, +ice cream, +snow

### COLORS  `colors`
- правило: Basic color names used in everyday English
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- +beige, +black, +blue, +Brown, +crimson, +gold, +gray, +green (green_color), +indigo, +lime, +magenta, +maroon, +navy, +olive, +orange (orange_color), +pink, +purple, +red, +silver, +tan, +teal, +turquoise, +Violet, +white (white_color), +yellow

### FAST THINGS  `fast_things`
- правило: Things known for moving very fast
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~arrow, ~bullet, ~cheetah, ~comet, ~falcon, ~hare, ~jet, ~lightning, ~motorcycle, ~rocket, ~sprinter, ~torpedo, +race car, +wind

### GREEN THINGS  `green_things`
- правило: Everyday things that are typically green in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~avocado, ~broccoli, ~cactus, ~clover, ~cucumber, ~emerald, ~Fern, ~frog, ~grass, ~kiwi, ~leaf, ~lettuce, ~lime, ~mint (mint_herb), ~moss, ~pea, ~pickle, ~shamrock, ~spinach, ~turtle

### HARD THINGS  `hard_things`
- правило: Things that feel hard and solid to the touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~bone, ~brick, ~concrete, ~diamond (diamond_gem), ~granite, ~iron (iron_metal), ~marble (marble_stone), ~nail (nail_metal), ~nut (nut_food), ~rock (rock_stone), ~shell, ~tile, ~tooth, +glass, +ice, +metal, +steel, +wood

### HEAVY THINGS  `heavy_things`
- правило: Things that are hard to lift because of their weight
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~anchor, ~anvil, ~barbell, ~bathtub, ~boulder, ~cannon, ~elephant, ~piano, ~refrigerator, ~statue, ~tractor, ~truck, ~whale, +engine, +safe, !cinderblock

### HOT THINGS  `hot_things`
- правило: Things that are hot by their physical nature
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~boiling water, ~campfire, ~candle, ~ember, ~furnace, ~iron (iron_appliance), ~lava, ~magma, ~oven, ~radiator, ~sauna, ~stove, ~torch, +coal, +engine, +fire, +steam, +sun

### LIGHT THINGS  `light_things`
- правило: Things that weigh almost nothing
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~balloon, ~bubble, ~confetti, ~cotton, ~dust, ~feather, ~foam, ~leaf, ~petal, ~seed, ~snowflake, ~thread, ~tissue (tissue_paper), +hair, +paper, !straw (straw_hay)

### THIN THINGS  `long_thin_things`
- правило: Everyday things that are long and thin
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~arrow, ~cane, ~chopstick, ~needle (needle_sewing), ~noodle, ~pencil, ~pole, ~ribbon, ~rope, ~ruler, ~snake, ~spaghetti, ~wire, ~worm, +hair, !straw (straw_tube)

### LOUD THINGS  `loud_things`
- правило: Things that make a loud noise
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~alarm, ~bell, ~chainsaw, ~drum, ~explosion, ~firework, ~gunshot, ~horn (horn_sound), ~jackhammer, ~jet, ~motorcycle, ~siren, ~speaker, ~thunder, ~whistle, +crowd

### QUIET THINGS  `quiet_things`
- правило: Things that make almost no sound
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~breath, ~breeze, ~cat, ~cloud, ~feather, ~library, ~moth, ~Shadow, ~silk, ~sleep, ~snow, ~tiptoe, ~whisper, !mouse (mouse_animal)

### RED THINGS  `red_things`
- правило: Everyday things that are typically red in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~apple (apple_fruit), ~barn, ~beet, ~brick, ~cardinal (cardinal_bird), ~cherry, ~chili (chili_pepper), ~fire truck, ~flame, ~ketchup, ~lipstick, ~lobster, ~radish, ~ruby, ~strawberry, ~tomato, ~valentine, +blood, +rose, +stop sign

### ROUND THINGS  `round_things`
- правило: Everyday objects whose normal shape is round or circular
- тип связи: `has_property`, базовая сложность 0.3
- слов: 26
- ~apple (apple_fruit), ~bagel, ~ball (ball_sphere), ~balloon, ~bubble, ~button (button_clothing), ~clock, ~coaster, ~coin, ~cookie, ~dial, ~donut, ~globe, ~hoop, ~lens, ~marble (marble_toy), ~moon (moon_space), ~orange (orange_fruit), ~pancake, ~pearl, ~pizza, ~plate (plate_dish), ~tire, ~wheel, ~wreath, +ring (ring_circle)

### SHINY THINGS  `shiny_things`
- правило: Things that reflect light and look shiny
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~blade, ~bumper, ~chrome, ~coin, ~diamond (diamond_gem), ~foil, ~glitter, ~jewel, ~lacquer, ~mirror, ~polish (polish_verb), ~satin, ~sequin, ~star (star_space), +glass, +gold, +ice, +silver

### SLOW THINGS  `slow_things`
- правило: Things known for moving very slowly
- тип связи: `has_property`, базовая сложность 0.35
- слов: 12
- ~caterpillar, ~glacier, ~molasses, ~parade, ~sloth, ~slug, ~snail, ~tortoise, ~tractor, ~turtle, ~worm, +traffic

### SMELLY THINGS  `smelly_things`
- правило: Things with a very strong smell
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~ammonia, ~bleach, ~cheese, ~durian, ~fish, ~garlic, ~gasoline, ~incense, ~manure, ~onion, ~perfume, ~skunk, ~smoke, ~vinegar, !mothball

### SOFT THINGS  `soft_things`
- правило: Things that feel soft to the touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~blanket, ~cloud, ~cotton, ~cushion, ~dough, ~feather, ~foam, ~fur, ~kitten, ~marshmallow, ~moss, ~pillow, ~sand, ~silk, ~sponge (sponge_cleaning), ~teddy bear, ~velvet, ~wool

### SQUARE THINGS  `square_things`
- правило: Everyday things shaped like a square
- тип связи: `has_property`, базовая сложность 0.35
- слов: 13
- ~brick, ~checkerboard, ~envelope, ~keyboard key, ~napkin, ~picture frame, ~stamp (stamp_postage), ~sticky note, ~tile, ~waffle, +box, +window, !dice (dice_game)

### STICKY THINGS  `sticky_things`
- правило: Substances that stick to whatever they touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~caramel, ~frosting, ~glue, ~gum (gum_glue), ~honey, ~jam, ~marshmallow, ~molasses, ~paste, ~resin, ~sap, ~slime, ~syrup, ~taffy, ~tape, ~tar, ~wax (wax_substance), !pitch (pitch_tar)

### STRIPED THINGS  `striped_things`
- правило: Things that normally have stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 13
- ~awning, ~barber pole, ~bee, ~candy cane, ~crosswalk, ~flag, ~prison uniform, ~referee shirt, ~ribbon, ~road, ~skunk, ~tiger, ~zebra

### POINTED THINGS  `things_that_are_sharp`
- правило: Things that come to a sharp point
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~arrow, ~claw, ~cone, ~dart (dart_throw), ~fang, ~icicle, ~nail (nail_metal), ~needle (needle_sewing), ~pencil, ~pin (pin_fastener), ~spear, ~spike, ~sword, ~tack (tack_pin), ~thorn, !horn (horn_animal)

### FRAGILE THINGS  `things_that_break`
- правило: Things that break easily when dropped
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~bulb, ~chalk (chalk_stick), ~egg, ~lightbulb, ~mirror, ~ornament, ~porcelain, ~pottery, ~shell, ~vase, +China, +glass, +ice, !screen (screen_display)

### FLOATING THINGS  `things_that_float`
- правило: Things that float on water
- тип связи: `has_property`, базовая сложность 0.35
- слов: 17
- ~balloon, ~bubble, ~buoy, ~cork, ~driftwood, ~duck (duck_bird), ~feather, ~foam, ~leaf, ~life vest, ~lily pad, ~pool noodle, ~raft, +boat, +ice, +wood, !oil (oil_cooking)

### SHRINKING THINGS  `things_that_shrink`
- правило: Things that get smaller over time or with heat
- тип связи: `has_property`, базовая сложность 0.45
- слов: 13
- ~balloon, ~battery, ~candle, ~glacier, ~ice, ~pencil, ~puddle, ~savings, ~Shadow, ~snowman, ~soap, ~sponge (sponge_cleaning), ~sweater

### STRETCHY THINGS  `things_that_stretch`
- правило: Things that stretch when pulled
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~balloon, ~bungee cord, ~dough, ~elastic, ~gum (gum_candy), ~muscle, ~rubber band, ~skin, ~Slinky, ~sock, ~spandex, ~taffy, ~waistband, +spring (spring_coil)

### THINGS WITH HOLES  `things_with_holes`
- правило: Everyday things that have holes in them
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~belt, ~button (button_clothing), ~cheese grater, ~colander, ~donut, ~flute, ~golf course, ~needle (needle_sewing), ~sieve, ~sock, ~sponge (sponge_cleaning), ~swiss cheese, ~waffle, ~whistle, +net, !straw (straw_tube)

### CLEAR THINGS  `transparent_things`
- правило: Things you can see through
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~aquarium, ~bubble, ~cellophane, ~crystal, ~jellyfish, ~lens, ~plastic wrap, ~screen (screen_display), ~veil, +air, +glass, +ice, +water, +window

### WHITE THINGS  `white_things`
- правило: Everyday things that are typically white in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~bone, ~chalk (chalk_stick), ~cloud, ~cotton, ~dove, ~flour, ~ghost, ~ivory, ~marshmallow, ~pearl, ~rice, ~sail (sail_cloth), ~salt, ~sheet (sheet_bed), ~swan, ~tooth, +milk, +paper, +snow, +sugar

### YELLOW THINGS  `yellow_things`
- правило: Everyday things that are typically yellow in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~banana, ~bee, ~butter, ~canary, ~cheese, ~corn, ~daffodil, ~duckling, ~highlighter, ~honey, ~lemon, ~mustard, ~pineapple, ~raincoat, ~sunflower, ~taxi, ~yolk, +gold, +school bus, +sun


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


## Тема: sounds

### ALARM SOUNDS  `bell_and_alarm`
- правило: Sounds made by alarms and signals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~alert, ~beep, ~bell, ~blare, ~buzz, ~chime, ~ding, ~gong, ~horn (horn_sound), ~siren, ~tone, ~whistle, +ring (ring_sound), !klaxon

### CITY SOUNDS  `city_sounds`
- правило: Sounds heard on a city street
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~alarm, ~bell, ~brakes, ~chatter, ~footsteps, ~honk, ~jackhammer, ~rumble, ~screech, ~shout, ~siren, ~whistle, +engine, +traffic

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
- +asteroid, +comets, +galaxy, +meteor, +moon, +nebula, +stars

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


## Тема: sports_world

### ARCHERY WORDS  `archery_words`
- правило: Words used in archery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 17
- ~bowstring, ~nock, ~range (range_shooting), +aim, +Archer, +arm guard, +arrow, +bow (bow_weapon), +bullseye, +draw, +quiver, +release, +shaft, +sight, +string, +Target, !fletching

### AT THE DOJO  `at_the_dojo`
- правило: A martial art or practice found in a dojo
- тип связи: `found_in`, базовая сложность 0.6
- слов: 6
- ~headlock, ~kendo, ~tatami, +grappling, +sparring, +sumo

### BOWLING WORDS  `bowling_words`
- правило: Words used in bowling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~pin (pin_bowling), ~strike (strike_bowling), +alley, +approach, +foul line, +frame, +gutter, +lane, +rack, +score sheet, +spare, +split, !turkey (turkey_bowling)

### BOXING WORDS  `boxing_words`
- правило: Words used in a boxing match
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~hook (hook_boxing), ~round (round_stage), +bell, +belt, +bout, +clinch, +corner, +decision, +glove, +jab, +knockout, +referee, +ring (ring_arena), +southpaw, +uppercut, xcutman

### HORSE RIDING  `equestrian_words`
- правило: Words used in horse riding sports
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~groom (groom_horse), ~stirrup, +arena, +bridle, +canter, +dressage, +fence, +gallop, +jockey, +jumping, +reins, +saddle, +tack (tack_horse), +trot

### FAMOUS STADIUMS  `famous_stadiums`
- правило: Famous sports stadiums and arenas
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Augusta, +Camp Nou, +Churchill Downs, +Daytona, +Fenway, +Lambeau, +Madison Square Garden, +Old Trafford, +Rose Bowl, +Wembley, +Wrigley, +Yankee Stadium

### FAN THINGS  `fan_things`
- правило: Things sports fans bring or wear to a game
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~cowbell, ~horn (horn_sound), +banner, +cap, +cooler, +face paint, +foam finger, +jersey, +megaphone, +pennant, +poster, +scarf, +ticket (ticket_admission), +whistle

### GYMNASTICS EVENTS  `gymnastics_events`
- правило: Events and moves in gymnastics
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~beam (beam_gym), ~handstand, ~pommel horse, +bars, +cartwheel, +dismount, +flip, +floor, +rings, +routine, +somersault, +split, +tumbling, +vault

### MOTOR RACING  `racing_words`
- правило: Words used in motor racing
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~lap (lap_race), +caution, +checkered flag, +crew, +driver, +grid, +helmet, +pit stop, +pole position, +qualifying, +speedway, +spoiler, +tire, +track

### RODEO  `rodeo`
- правило: A person, animal or event of a rodeo
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- +bronco, +cowgirl, +lasso, +stampede, +Wrangler

### SKATEBOARDING WORDS  `skateboarding`
- правило: Words used in skateboarding
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bearing, ~bowl, ~deck, ~grind, ~grip tape, ~helmet, ~nose, ~ollie, ~rail, ~ramp, ~trucks, ~wheels, !halfpipe, !kickflip

### SKIING WORDS  `skiing_words`
- правило: Words used on a ski slope
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~apres ski, ~snowplow, +bindings, +black diamond, +boots, +goggles, +gondola, +lift, +lodge, +moguls, +poles, +powder, +slope, +trail map

### SPORTS INJURIES  `sports_injuries`
- правило: Injuries common in sports
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- +bruise, +concussion, +cramp, +dislocation, +fracture, +pulled muscle, +shin splints, +sprain, +strain, +tear, +tennis elbow, +torn acl, +whiplash

### SPORTS LEAGUES  `sports_leagues`
- правило: Professional sports leagues and competitions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Indy 500, +Kentucky Derby, +Masters, +MLB, +MLS, +NBA, +NFL, +NHL, +Olympics, +Stanley Cup, +Super Bowl, +Tour de France, +Wimbledon, +World Cup, +World Series

### SPORTS LEGENDS  `sports_legends`
- правило: Athletes remembered across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Navratilova, +Ali, +Chamberlain, +DiMaggio, +Gretzky, +Jordan, +Louis, +Montana, +Nicklaus, +Owens, +Pele, +Robinson, +Ruth, +Thorpe, !Comaneci

### SWIM STROKES  `swimming_strokes`
- правило: Strokes and events in competitive swimming
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +backstroke, +breaststroke, +butterfly, +distance, +dive, +doggy paddle, +freestyle, +medley, +relay, +sprint, +treading, ?sidestroke

### TRACK EVENTS  `track_events`
- правило: Events contested in track and field
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +decathlon, +discus, +high jump, +hurdles, +javelin, +long jump, +marathon, +pole vault, +race walk, +relay, +shot put, +sprint, +steeplechase, +triple jump

### TRAINING WORDS  `training_words`
- правило: Words used in athletic training
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~cooldown, +circuit, +coach, +conditioning, +drill (drill_practice), +endurance, +form, +interval, +recovery, +rep, +routine, +stretch, +warmup, !set (set_exercise)

### WRESTLING WORDS  `wrestling_words`
- правило: Words used in wrestling
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- +escape, +headgear, +hold, +mat, +period, +referee, +reversal, +singlet, +takedown, +throw, +weight class, !bridge (bridge_move), !pin (pin_wrestling)


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
- ~touchpad, +battery, +cable, +Charger, +fan (fan_device), +graphics card, +hard drive, +keyboard (keyboard_computer), +memory, +monitor (monitor_screen), +motherboard, +mouse (mouse_computer), +port, +power supply, +processor, +screen (screen_display), +speaker, +tower, +webcam, !case (case_box)

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
- +alarm, +app, +battery, +camera, +Charger, +contact, +headphones, +hotspot, +keypad, +notification, +ringtone, +screen (screen_display), +signal, +sim card, +speaker, +text, +voicemail, !case (case_box)

### PHOTOGRAPHY WORDS  `photography_words`
- правило: Words used when taking photographs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +album, +angle, +aperture, +crop, +darkroom, +exposure, +filter, +flash, +focus (focus_lens), +frame, +lens, +negative, +portrait, +selfie, +shutter, +snapshot, +tripod, +Zoom

### POWER WORDS  `power_and_batteries`
- правило: Words about supplying power to devices
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- +adapter, +battery, +cable, +Charger, +cord, +extension, +fuse, +generator, +outlet, +plug, +power strip, +socket (socket_electric), +solar panel, +switch, +voltage, +Watt

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
- ~deadbolt, ~floodlight, +alarm, +badge, +buzzer, +camera, +fence, +keypad, +lock, +monitor (monitor_screen), +motion detector, +safe, +sensor, +siren

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


## Тема: tools

### GLUES AND TAPES  `adhesives`
- правило: Sticky products used to join things
- тип связи: `used_in`, базовая сложность 0.35
- слов: 15
- ~caulk, +adhesive, +cement, +duct tape, +epoxy, +glue, +gum (gum_glue), +hot glue, +masking tape, +mortar, +paste, +putty, +sealant, +super glue, +tape

### ART SUPPLIES  `art_supplies`
- правило: Materials used to make art or crafts
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~chalk (chalk_stick), +bead, +brush, +canvas, +charcoal, +clay, +crayon, +glitter, +glue, +ink, +marker, +paint, +paper, +pastel, +pencil, +ribbon, +scissors, +sketchbook, +stencil, +yarn

### BLADES  `blades`
- правило: Parts of tools that do the cutting
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- +axe head, +blade, +cutter, +edge, +knife edge, +point (point_tip), +razor, +saw blade, +scissor blade, +teeth, !tip (tip_point)

### TOOL STORAGE  `boxes_and_cases`
- правило: Things used to store and carry tools
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~case (case_box), +bag, +belt, +bucket, +cabinet (cabinet_furniture), +caddy, +chest (chest_box), +drawer, +pouch, +rack, +shed, +toolbox, +tray, !pegboard

### CLEANING TOOLS  `cleaning_tools`
- правило: Tools used for cleaning and tidying
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~scrubber, ~squeegee, +air freshener, +broom, +brush, +bucket, +duster, +dustpan, +lint roller, +mop, +plunger, +rag, +sponge (sponge_cleaning), +steam cleaner, +toothbrush, +vacuum

### CUTTING TOOLS  `cutting_tools`
- правило: Tools used to cut material
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- +blade, +box cutter, +chisel, +cleaver, +clipper, +guillotine, +hedge trimmer, +knife, +lawnmower, +machete, +razor, +saw, +scalpel, +scissors, +shears, +wire cutter

### FASTENERS  `fasteners`
- правило: Small parts used to hold things together
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~pin (pin_fastener), +anchor, +bolt, +bracket, +buckle, +clamp, +clip, +hinge, +hook (hook_fastener), +nail (nail_metal), +rivet, +screw, +staple, +tack (tack_pin), +velcro, +washer, +zip tie, !nut (nut_metal)

### GARDEN SHED  `garden_shed`
- правило: A tool or material kept in a garden shed
- тип связи: `found_in`, базовая сложность 0.5
- слов: 4
- +mulch, +spade (spade_tool), +trellis, +wheelbarrow

### GARDEN TOOLS  `garden_tools`
- правило: Tools used for gardening and yard work
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~cultivator, ~edger, ~pruner, ~seeder, ~weeder, +clippers, +gloves, +hoe, +hose, +lawnmower, +leaf blower, +pitchfork, +rake, +shears, +shovel, +spade (spade_tool), +sprinkler, +trowel, +watering can, +wheelbarrow

### HAND TOOLS  `hand_tools`
- правило: Tools held in the hand and used for building or repair work
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~file (file_tool), ~plane (plane_tool), ~socket (socket_tool), +awl, +chisel, +clamp, +crowbar, +drill (drill_tool), +hammer, +knife, +level, +mallet, +pliers, +ratchet, +sander, +saw, +scraper, +screwdriver, +Square, +stapler, +tape measure, +vise, +wrench, ?screwgun, !punch (punch_tool)

### HANDYMAN  `handyman`
- правило: A tool or material a handyman carries
- тип связи: `used_in`, базовая сложность 0.5
- слов: 4
- ~caulk, ~stepladder, ~toolbelt, +crowbar

### HARDWARE STORE  `hardware_store`
- правило: What a hardware store keeps in its bins and aisles
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~containers, ~fuels, +blades, +fasteners, +hose, +ladder, +sandpaper

### KITCHEN GADGETS  `kitchen_gadgets`
- правило: Small specialized gadgets used in a kitchen
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~baster, ~peeler, ~sifter, +can opener, +corkscrew, +egg slicer, +funnel, +garlic press, +melon baller, +pizza cutter, +scoop, +strainer, +thermometer, +timer, !tenderizer, xzester

### MEASURING TOOLS  `measuring_tools`
- правило: Tools used to measure size, weight or amount
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- +barometer, +caliper, +compass, +gauge, +level, +measuring cup, +meter, +odometer, +protractor, +ruler, +scale (scale_weigh), +speedometer, +stopwatch, +tape measure, +thermometer, +yardstick

### OFFICE SUPPLIES  `office_supplies`
- правило: Small items kept in an office desk and used for paperwork
- тип связи: `found_in`, базовая сложность 0.15
- слов: 26
- ~stamp (stamp_tool), ~whiteout, +binder, +calculator, +calendar, +clip, +envelope, +eraser, +folder, +highlighter, +hole punch, +ink, +label, +marker, +notepad, +paper, +paper clip, +pen (pen_writing), +pencil, +planner, +rubber band, +ruler, +scissors, +stapler, +sticky note, +tape

### PAINTING SUPPLIES  `painting_supplies`
- правило: Things used to paint a wall or a picture
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- +brush, +canvas, +drop cloth, +easel, +ladder, +paint, +palette, +primer, +roller, +smock, +sponge (sponge_cleaning), +spray can, +stencil, +tape, +thinner, +tray

### POWER TOOLS  `power_tools`
- правило: Tools driven by electricity or a motor
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~planer, +air compressor, +blower, +buffer, +chainsaw, +drill (drill_tool), +grinder, +impact driver, +jackhammer, +jigsaw, +nail gun, +router, +sander, +saw, +table saw, +welder

### SAFETY GEAR  `safety_gear`
- правило: Equipment worn to stay safe while working
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~ear muffs, +apron (apron_garment), +boots, +earplugs, +face shield, +gloves, +goggles, +hard hat, +harness, +helmet, +knee pads, +mask, +respirator, +vest

### SEWING SUPPLIES  `sewing_supplies`
- правило: Items used for sewing and mending clothes
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~button (button_clothing), ~pincushion, +bobbin, +elastic, +hem, +hook (hook_fastener), +needle (needle_sewing), +patch, +pattern, +pin (pin_fastener), +scissors, +seam ripper, +snap, +tape measure, +thimble, +thread, +yarn, +zipper

### MEASURING UNITS  `things_measured_in_inches`
- правило: Units used to measure length, weight or volume
- тип связи: `is_a`, базовая сложность 0.35
- слов: 21
- ~foot (foot_measure), +acre, +centimeter, +cup, +fathom, +gallon, +gram, +inch, +kilometer, +liter, +meter, +mil, +mile, +ounce, +pint, +pound (pound_weight), +quart, +tablespoon, +teaspoon, +ton, +yard (yard_measure)

### SHARP THINGS  `things_that_cut`
- правило: Everyday things with a sharp edge or point
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~arrow, ~blade, ~dart (dart_throw), ~glass shard, ~knife, ~nail (nail_metal), ~needle (needle_sewing), ~pin (pin_fastener), ~razor, ~scissors, ~spear, ~splinter, ~sword, ~tack (tack_pin), ~thorn, +ice pick, +saw, !hook (hook_fastener)

### SPINNING THINGS  `things_that_spin`
- правило: Everyday things that spin or rotate
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~blender, ~carousel, ~ceiling fan, ~coin, ~dial, ~dryer, ~fan (fan_device), ~gear, ~globe, ~propeller, ~tire, ~top (top_spin), ~turbine, ~washing machine, ~wheel, ~windmill, +record, !drill (drill_tool)

### HAMMERED THINGS  `things_that_stick_out`
- правило: Things a hammer is normally used on
- тип связи: `does_action`, базовая сложность 0.4
- слов: 13
- ~bolt, ~chisel, ~dent, ~horseshoe, ~nail (nail_metal), ~Peg, ~rivet, ~spike, ~stake, ~tack (tack_pin), ~tent stake, ~wedge, !post (post_pole)

### THINGS WITH HANDLES  `things_with_handles`
- правило: Everyday objects gripped by a handle
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~axe, ~basket, ~briefcase, ~broom, ~bucket, ~drawer, ~hammer, ~kettle, ~knife, ~mug, ~pan, ~pitcher (pitcher_jug), ~purse, ~racket, ~shovel, ~suitcase, ~umbrella, +door

### TUBES  `tubes`
- правило: A hollow tube that something flows through
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +chute, +duct, +funnel, +hose, +nozzle, +pipe (pipe_tube), +straw (straw_tube)

### UNDER LOCK  `under_lock`
- правило: Something used to lock things away or guard them
- тип связи: `used_for`, базовая сложность 0.35
- слов: 7
- +alarm, +code, +key (key_lock), +lock, +padlock, +safe, +vault

### WORKSHOP THINGS  `workshop_things`
- правило: Things found in a home workshop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~pegboard, +apron (apron_garment), +bucket, +clamp, +drill (drill_tool), +extension cord, +goggles, +grinder, +hammer, +lumber, +nail (nail_metal), +oil can, +sandpaper, +sawdust, +shelf (shelf_furniture), +toolbox, +vise, +workbench


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
- ~habanero, ~pimento, +Anaheim, +banana, +bell, +cayenne, +Chipotle, +ghost, +jalapeno, +scotch bonnet, +serrano, !poblano, xshishito

### POTATO VARIETIES  `potato_varieties`
- правило: Varieties of potato sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~russet, ~white (white_food), +baby, +idaho (idaho_potato), +new potato, +purple, +red, +sweet potato, +yam, +yukon gold, !fingerling, !kennebec

### RICE TYPES  `rice_types`
- правило: Kinds of rice sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +black, +Brown, +Jasmine, +long grain, +red, +short grain, +sticky, +sushi, +white (white_food), +wild, !arborio, !basmati, !parboiled

### TOMATO VARIETIES  `tomato_varieties`
- правило: Varieties of tomato
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~campari, ~green (green_unripe), +cherry, +grape, +heirloom, +plum, +roma, +sun dried, +vine, +yellow, !beefsteak, !san marzano


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


## Тема: world_more

### MORE COUNTRIES  `countries_more`
- правило: Countries less often named in lists
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- +Albania, +Andorra, +Armenia, +Belarus, +Bhutan, +Cyprus, +Georgia, +Iceland, +Kazakhstan, +Latvia, +Lithuania, +Luxembourg, +Malta, +Moldova, +Monaco, +Mongolia, +Nepal, +Slovenia, +Ukraine, +Uzbekistan

### HIGHLANDS  `highlands`
- правило: A word belonging to the Scottish Highlands
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +bagpipes, +haggis, +kilt, +loch, +tartan

### ISLAND LUAU  `island_luau`
- правило: A word belonging to a Hawaiian island party
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- ~luau, +aloha, +hula, +lei, +tiki, +ukulele

### ISLAND NATIONS  `island_nations`
- правило: Countries made up of islands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Bahrain, +Cuba, +Cyprus, +Fiji, +Iceland, +Indonesia, +Jamaica, +Japan, +Madagascar, +Maldives, +Malta, +Mauritius, +Philippines, +Seychelles, +Sri Lanka

### TEA CEREMONY  `tea_ceremony`
- правило: A vessel, leaf or step of making tea properly
- тип связи: `used_in`, базовая сложность 0.55
- слов: 5
- ~infuser, ~teahouse, +darjeeling, +steep, +teapot

### TROPICAL BIRDS  `tropical_birds`
- правило: Colorful birds of tropical regions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +bird of paradise, +cockatoo, +flamingo, +hummingbird, +kingfisher, +parrot, +toucan, !hornbill, !lorikeet, !macaw, !motmot, !quetzal, !sunbird

### TROPICAL FLOWERS  `tropical_flowers`
- правило: Flowers that grow in tropical places
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +bird of paradise, +ginger flower, +hibiscus, +Jasmine, +lotus, +orchid, !anthurium, !bougainvillea, !frangipani, !heliconia, !plumeria, !protea

### WORLD BREAKFAST  `world_breakfasts`
- правило: Breakfast foods eaten in other countries
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~cheese plate, ~croissant, ~dim sum, ~fruit plate, ~full english, ~pastry, ~porridge, ~tamale, !arepa, !churro, !congee, !flatbread, !miso soup, !shakshuka

### WORLD REGIONS  `world_deserts_and_seas`
- правило: Named regions of the world
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Alps, +Amazon, +Andalusia, +Balkans, +Bavaria, +Caribbean, +Himalaya, +mediterranean, +Outback, +Patagonia, +Riviera, +Sahara, +Scandinavia, +Siberia, +Tuscany

### TRADITIONAL FOOTWEAR  `world_hats_and_dress`
- правило: Traditional shoes from world cultures
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- ~clog, ~sandal, ?babouche, ?jutti, !geta, !huarache, !moccasin, !sabot, xespadrille, xmukluk

### MARKET WORDS  `world_markets`
- правило: Things found at an open air market
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~stall (stall_market), +awning, +basket, +canopy, +cart, +cash, +crate, +crowd, +haggling, +produce, +sample, +sign, +spice, +vendor, !scale (scale_weigh)

### WORLD SOUPS  `world_soups`
- правило: Soups from cuisines around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +egg drop, +miso, +pho, +ramen, +tom yum, ?avgolemono, ?harira, !borscht, !caldo, !gazpacho, !goulash, !laksa, !minestrone, xmulligatawny

### WORLD SPORTS  `world_sports`
- правило: Sports popular outside the United States
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~kabaddi, +badminton, +bandy, +cricket, +curling, +futsal, +handball, +hurling, +netball, +rugby, +sumo, +table tennis, !pelota, xsepak takraw

### TRADITIONAL DRINKS  `world_teas_and_drinks`
- правило: Traditional drinks from world cultures
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~cider, ~mead, ~rum, ~sake, ~tequila, ~vodka, ~Whiskey, !aquavit, !horchata, !kvass, !lassi, !matcha, !ouzo, !sangria, !yerba mate

### WORLD TRANSPORT  `world_transport`
- правило: Ways people get around in other countries
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~funicular, ~tuk tuk, +bicycle, +cable car, +camel, +canoe, +double decker, +ferry, +gondola, +moped, +rickshaw, +sled, +tram, !jeepney

