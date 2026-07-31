# Категории: правило и слова

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


## Тема: animals

### AFRICAN ANIMALS  `african_animals`
- правило: Wild animals associated with the African savanna
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~baboon, ~lion, ~ostrich, ~vulture, +antelope, +buffalo, +cheetah, +crocodile, +elephant, +gazelle, +giraffe, +hippo, +hyena, +leopard, +mongoose, +rhino, +wildebeest, +zebra, !meerkat, !warthog

### AMPHIBIANS  `amphibians_and_bugs`
- правило: Animals that live both in water and on land as amphibians
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~bullfrog, ~frog, ~newt, ~salamander, ~tadpole, ~toad, !axolotl, xcaecilian, xmudpuppy, xtreefrog

### BABY ANIMALS  `animal_babies`
- правило: English words for the young of an animal species
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~bunny, ~calf (calf_cow), ~chick, ~colt, ~fawn, ~fry (fry_fish), ~gosling, ~kid, ~lamb, ~tadpole, +calfling, +cub, +duckling, +foal, +joey, +kitten, +piglet, +pup, +puppy, !owlet

### ANIMAL PARTS  `animal_body_parts`
- правило: Body parts that animals have but people do not
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~antler, ~flipper, ~hoof, ~horn (horn_animal), ~hump, ~mane, ~talon, ~trunk (trunk_elephant), +beak, +claw, +fang, +fin, +gill, +muzzle, +paw, +snout, +tail, +tusk, +whisker, +wing

### ANIMAL COVERINGS  `animal_coverings`
- правило: Things that cover an animal body
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~coat (coat_fur), ~down, ~feather, ~hair, ~hide, ~plate, ~quill, ~scale, ~shell, ~spine, +fleece, +fur, +plume, +skin, +wool

### ANIMAL GROUPS  `animal_groups`
- правило: Collective nouns for groups of animals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~colony, ~drove, ~flock, ~gaggle, ~herd, ~hive, ~nest, ~pack, ~swarm, ~troop, !brood, !litter, !pod, !pride, !school

### ANIMAL HOMES  `animal_homes`
- правило: Words for the places animals live in
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~anthill, ~barn, ~cave, ~cocoon, ~coop, ~hive, ~hutch, ~lodge, ~nest, ~pen (pen_animal), ~shell, ~stable, ~warren, ~web, +burrow, +den, +hole, +kennel, +mound (mound_dirt), +roost

### ANIMAL SOUNDS  `animal_sounds`
- правило: English words for the sound an animal makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 26
- ~bark (bark_sound), ~buzz, ~cluck, ~croak, ~hoot, ~moo, ~oink, ~snarl, ~squeak, ~yelp, +bray, +caw, +chirp, +coo, +growl, +grunt, +hiss, +howl, +meow, +purr, +quack, +roar, +tweet, !bleat, !neigh, !whinny

### ANIMAL MOVEMENTS  `animal_verbs`
- правило: Verbs for the way particular animals move
- тип связи: `does_action`, базовая сложность 0.4
- слов: 18
- ~burrow, ~crawl, ~dart (dart_move), ~flutter, ~gallop, ~glide, ~hop, ~leap, ~perch, ~pounce, ~slither, ~soar, ~swoop, ~trot, ~waddle, !prowl, !scurry, !swim

### ANIMALS WITH SHELLS  `animals_with_shells`
- правило: Animals whose body is protected by a hard shell
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~clam, ~cockle, ~conch, ~crab, ~lobster, ~mussel, ~oyster, ~scallop, ~snail, ~tortoise, ~turtle, !armadillo, !barnacle, !beetle, !nautilus

### ARCTIC ANIMALS  `arctic_animals`
- правило: Animals that live in the cold polar regions
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~husky, ~penguin, ~reindeer, ~seal (seal_animal), ~walrus, +arctic fox, +beluga, +caribou, +moose, +musk ox, +orca, +polar bear, +puffin, +snowy owl, +wolverine, !lemming, !narwhal, !ptarmigan

### BIRDS  `birds`
- правило: Bird species an average American can name
- тип связи: `is_a`, базовая сложность 0.12
- слов: 26
- ~chicken, +blue jay, +canary, +cardinal (cardinal_bird), +crane (crane_bird), +crow, +duck (duck_bird), +eagle, +falcon, +flamingo, +goose, +hawk, +ostrich, +owl, +parrot, +peacock, +pelican, +penguin, +pigeon, +raven, +robin, +seagull, +sparrow, +swan, +turkey (turkey_bird), +woodpecker

### DOG BREEDS  `dog_breeds`
- правило: Breeds of domestic dog recognized by an average American
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~retriever, +beagle, +boxer, +bulldog, +chihuahua, +collie, +corgi, +dachshund, +dalmatian, +doberman, +greyhound, +husky, +labrador, +mastiff, +poodle, +pug, +rottweiler, +shepherd, +spaniel, +terrier

### EXTINCT ANIMALS  `extinct_animals`
- правило: Animal species that no longer exist
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~brontosaurus, ~mammoth, ~triceratops, +dinosaur, +dodo, +mastodon, +raptor, +saber tooth, +tyrannosaurus, !megalodon, !pterodactyl, !stegosaurus, !trilobite, !velociraptor

### FARM ANIMALS  `farm_animals`
- правило: Animals commonly kept on an ordinary farm
- тип связи: `is_a`, базовая сложность 0.1
- слов: 20
- ~calf (calf_cow), ~cat, ~dog, ~duck (duck_bird), ~goose, ~hen, ~pig, ~rabbit, ~turkey (turkey_bird), +bull, +chicken, +cow, +donkey, +goat, +horse, +lamb, +mule, +ox, +rooster, +sheep

### POULTRY  `farm_bird_words`
- правило: Birds raised for meat or eggs on a farm
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +chick, +chicken, +duck (duck_bird), +goose, +guinea fowl, +hen, +pheasant, +pigeon, +quail, +rooster, +turkey (turkey_bird), !capon

### FLYING ANIMALS  `flying_animals`
- правило: Animals that can fly under their own power
- тип связи: `has_property`, базовая сложность 0.2
- слов: 26
- ~bat (bat_animal), ~bluebird, ~dragonfly, ~ladybug, ~mosquito, ~moth, +bee, +butterfly, +crow, +duck (duck_bird), +eagle, +falcon, +goose, +hawk, +hornet, +hummingbird, +owl, +pelican, +pigeon, +robin, +seagull, +sparrow, +stork, +swan, +vulture, +wasp

### HORSE WORDS  `horse_words`
- правило: Words for kinds of horses and horse gear
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~canter, ~groom (groom_horse), ~reins, +bridle, +colt, +foal, +gallop, +halter, +harness, +hoof, +jockey, +mane, +mare, +pony, +saddle, +stable, +stallion, +thoroughbred, +trot, !stirrup

### INSECTS  `insects`
- правило: Insects and other small bugs an average person recognizes
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~locust, ~spider, +ant, +bee, +beetle, +butterfly, +caterpillar, +centipede, +cricket, +dragonfly, +firefly, +flea, +fly (fly_insect), +grasshopper, +hornet, +ladybug, +mosquito, +moth, +roach, +termite, +tick (tick_bug), +wasp, !aphid, !gnat, !silkworm

### JUNGLE ANIMALS  `jungle_animals`
- правило: Animals that live in tropical jungles and rainforests
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~anteater, ~boa, ~frog, ~iguana, ~leopard, ~parrot, ~python, ~sloth, ~snake, ~tiger, ~toucan, +chimpanzee, +gorilla, +jaguar, +lemur, +monkey, +orangutan, +panther, !macaw, !tapir

### NOCTURNAL ANIMALS  `nocturnal_animals`
- правило: Animals that are active at night and rest during the day
- тип связи: `has_property`, базовая сложность 0.35
- слов: 21
- ~badger, ~bat (bat_animal), ~beaver, ~cougar, ~coyote, ~cricket, ~firefly, ~fox, ~hamster, ~hedgehog, ~leopard, ~mole (mole_animal), ~moth, ~mouse (mouse_animal), ~opossum, ~owl, ~porcupine, ~raccoon, ~skunk, ~wolf, !armadillo

### OCEAN ANIMALS  `ocean_animals`
- правило: Animals that live in the ocean
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~clam, ~manatee, ~seal (seal_animal), ~turtle, ~urchin, ~walrus, +barnacle, +coral, +crab, +dolphin, +eel, +jellyfish, +lobster, +octopus, +orca, +oyster, +seahorse, +shark, +shrimp, +squid, +starfish, +stingray, +swordfish, +tuna, +whale

### PESTS  `pests`
- правило: Animals treated as household or garden pests
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~moth, ~pigeon, ~raccoon, ~rat, ~snail, ~wasp, +ant, +flea, +gopher, +mole (mole_animal), +mosquito, +mouse (mouse_animal), +roach, +slug, +termite, +tick (tick_bug), +weevil, !aphid, !bedbug, !silverfish

### PETS  `pets`
- правило: Animals commonly kept as household pets in the United States
- тип связи: `is_a`, базовая сложность 0.12
- слов: 20
- ~gerbil, ~goldfish, ~hedgehog, ~iguana, ~lizard, ~parakeet, ~pony, ~snake, ~turtle, +canary, +cat, +chinchilla, +dog, +ferret, +guinea pig, +hamster, +mouse (mouse_animal), +parrot, +rabbit, !cockatiel

### POND ANIMALS  `pond_animals`
- правило: Animals that live in or around a freshwater pond
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~beaver, ~carp, ~crayfish, ~dragonfly, ~frog, ~goose, ~mosquito, ~salamander, ~snail, ~swan, ~tadpole, ~turtle, +duck (duck_bird), +fish, +heron, +newt, +otter, +water bug

### REPTILES  `reptiles`
- правило: Cold-blooded scaly animals classed as reptiles
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~tortoise, ~turtle, +alligator, +anaconda, +boa, +chameleon, +cobra, +crocodile, +gecko, +iguana, +lizard, +python, +rattlesnake, +snake, +viper, !monitor (monitor_lizard), !skink, !terrapin

### RODENTS  `rodents`
- правило: Small gnawing mammals classed as rodents
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~gerbil, +beaver, +chinchilla, +chipmunk, +gopher, +groundhog, +guinea pig, +hamster, +mouse (mouse_animal), +porcupine, +prairie dog, +rat, +squirrel, +vole, !capybara, !muskrat

### STRIPED ANIMALS  `spotted_and_striped`
- правило: Animals whose coat has clear stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~badger, ~bee, ~chipmunk, ~hyena, ~raccoon, ~skunk, ~tiger, ~wasp, ~zebra, !angelfish, !clownfish, !lemur, !okapi, !snake

### WILD CATS  `wild_cats`
- правило: Wild members of the cat family
- тип связи: `is_a`, базовая сложность 0.25
- слов: 13
- +bobcat, +cheetah, +cougar, +jaguar, +leopard, +lion, +lynx, +panther, +puma, +tiger, !caracal, !ocelot, !serval

### ZOO ANIMALS  `zoo_animals`
- правило: Animals commonly seen at an American zoo
- тип связи: `found_in`, базовая сложность 0.15
- слов: 20
- ~camel, ~flamingo, ~gorilla, ~kangaroo, ~koala, ~lion, ~monkey, ~panda, ~peacock, ~penguin, ~tiger, +bear, +elephant, +giraffe, +hippo, +otter, +rhino, +seal (seal_animal), +sloth, +zebra


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


## Тема: art

### ART STYLES  `art_styles`
- правило: Named styles of visual art
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~gothic, +abstract, +art deco, +baroque, +expressionism, +folk art, +impressionism, +minimalism, +modernism, +pop art, +realism, +renaissance, +surrealism, !cubism

### ART TOOLS  `art_tools`
- правило: Tools an artist uses to make art
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~brush, ~charcoal, ~chisel, ~kiln, ~knife, ~loom, ~mold (mold_form), ~palette, ~pen (pen_writing), ~pencil, ~roller, ~sponge (sponge_cleaning), +airbrush, +canvas, +easel, +stylus

### SHADES OF COLOR  `color_words_advanced`
- правило: Words for particular shades of color
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~azure, ~charcoal, ~coral, ~cream (cream_color), ~ivory, ~jade, ~lavender (lavender_color), ~mint (mint_color), ~mustard, ~olive, ~plum, ~sage (sage_color), +amber, +blush, +cobalt, +crimson, +mauve, +ochre, +rust, +scarlet

### CRAFTS  `crafts`
- правило: Handmade crafts people do as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~origami, ~pottery, ~woodworking, +calligraphy, +candle making, +crochet, +embroidery, +knitting, +quilting, +sewing, +soap making, +weaving, !beading, !macrame, !scrapbooking

### DECORATIONS  `decorative_things`
- правило: Things used to decorate a room or an event
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~balloon, ~banner, ~candle, ~curtain, ~figurine, ~garland, ~lantern, ~mobile, ~ornament, ~painting, ~rug, ~sculpture, ~tapestry, ~vase, ~wreath, +centerpiece, +mural, +streamer

### DRAWING WORDS  `drawing_words`
- правило: Words used when drawing a picture
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~blend, ~curve, ~hatch, ~highlight, ~perspective, ~proportion, ~shade, ~silhouette, +contour, +doodle, +erase, +line (line_drawn), +outline, +sketch, +trace

### FAMOUS ARTWORKS  `famous_artworks`
- правило: Artworks most people can name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~David, +American Gothic, +Girl with a Pearl Earring, +Last Supper, +Mona Lisa, +Starry Night, +Sunflowers, +The Scream, +The Thinker, +Venus de Milo, !Guernica

### JEWELRY SUPPLIES  `jewelry_making`
- правило: Things used to make jewelry
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~bead, ~chain, ~clasp, ~cord, ~hook (hook_fastener), ~pendant, ~pliers, ~solder, ~thread, ~wire, !gem, !mold (mold_form), !ring blank, !setting

### MUSEUM WORDS  `museum_words`
- правило: Things found in an art museum
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~admission, ~guide, ~plaque, ~rope, +audio tour, +collection, +curator, +exhibit, +frame, +gallery, +gift shop, +painting, +pedestal, +portrait, +sculpture, !docent

### KINDS OF PAINT  `paint_types`
- правило: Kinds of paint used by artists and decorators
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~enamel, ~latex, ~oil (oil_paint), ~spray, +acrylic, +chalk paint, +finger paint, +primer, +varnish, +watercolor, !gouache, !tempera

### PHOTO SUBJECTS  `photography_styles`
- правило: Kinds of pictures a photographer takes
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~macro, ~portrait, ~silhouette, +action shot, +aerial, +candid, +close up, +group shot, +landscape, +panorama, +selfie, +still life, +wedding photo

### POTTERY WORDS  `pottery_words`
- правило: Things used in making pottery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bowl, ~clay, ~fire, ~glaze, ~kiln, ~mold (mold_form), ~plaster, ~pot, ~sculpt, ~tile, ~vase, ~wheel, !slip, !trim (trim_cut)

### SCULPTURE MATERIALS  `sculpture_materials`
- правило: Materials sculptors carve or cast
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~bronze, ~clay, ~glass, ~ice, ~plaster, ~sand, ~wax (wax_substance), ~wood, +concrete, +granite, +marble (marble_stone), +metal, +stone, !soapstone

### TEXTURES  `textures`
- правило: Words describing how a surface feels
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~bumpy, ~coarse, ~fuzzy, ~glossy, ~grainy, ~polished, ~rough, ~silky, ~slick, ~smooth, !matte, !prickly, !ridged, !sticky, !velvety

### PERFORMING ARTS  `theater_arts`
- правило: Arts performed in front of an audience
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~ballet, ~magic, ~opera, ~recital, +circus, +comedy, +concert, +dance, +improv, +mime, +musical, +play, +poetry reading, !puppetry


## Тема: body

### BODY MOVEMENTS  `body_movements`
- правило: Movements the human body makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- ~breathe, ~clap, ~crouch, ~jump, ~kick, ~lean, ~nod, ~point (point_gesture), ~shrug, ~stretch, ~swallow (swallow_throat), ~twist, ~wave (wave_hand), ~yawn, +bend, +blink, +cough, +shiver, +sneeze, +wink

### BODY PARTS  `body_parts`
- правило: External parts of the human body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~back, ~calf (calf_leg), ~chest (chest_body), ~chin, ~finger, ~forehead, ~heel, ~stomach, ~waist, +ankle, +arm, +elbow, +foot (foot_body), +hand (hand_body), +head (head_body), +hip, +jaw, +knee, +leg, +neck, +shin, +shoulder (shoulder_body), +thigh, +toe, +wrist

### BODY SOUNDS  `body_sounds`
- правило: Sounds the human body makes on its own
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~burp, ~cough, ~cry, ~growl, ~grunt, ~gulp, ~laugh, ~snore, ~whistle, +gasp, +hiccup, +sigh, +sneeze, +yawn, !sniffle, !wheeze

### BODY SYSTEMS  `body_systems`
- правило: Systems that make up the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- ~digestive, ~immune, ~muscular, ~nervous, !circulatory, !endocrine, !lymphatic, !respiratory, !skeletal, !urinary

### BONES  `bones`
- правило: Bones of the human skeleton
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- +ankle bone, +collarbone, +femur, +hip bone, +jawbone, +kneecap, +pelvis, +rib, +shin bone, +shoulder blade, +skull, +spine, +vertebra, +wrist bone, !breastbone, !tailbone

### DENTIST THINGS  `dentist_things`
- правило: Things found at a dentist office
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~chair, ~crown (crown_dental), ~drill (drill_tool), ~mirror, ~mold (mold_form), ~rinse, ~X-ray, +bib, +brace, +cavity, +filling, +floss, +plaque, +retainer, +suction, +toothbrush

### EXERCISE WORDS  `exercise_words`
- правило: Movements done as physical exercise
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~curl, ~dip, ~plank, ~press (press_push), ~row, +crunch (crunch_exercise), +jog, +jumping jack, +lunge, +situp, +sprint, +squat, +stretch, !burpee, !pullup, !pushup

### FACE PARTS  `face_parts`
- правило: Parts of the human face
- тип связи: `part_of`, базовая сложность 0.12
- слов: 20
- ~freckle, ~temple (temple_head), +brow, +cheek, +chin, +dimple, +ear, +eye, +eyebrow, +eyelash, +eyelid, +forehead, +iris, +jaw, +lash, +lip, +mouth (mouth_face), +nose, +nostril, +pupil

### DIGITS  `fingers_and_toes`
- правило: Names for individual fingers and toes
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~index finger, ~toe, +big toe, +digit, +little toe, +middle finger, +pinky, +ring finger, +thumb, !forefinger

### HAIR WORDS  `hair_words`
- правило: Words for hairstyles and things done to hair
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~bang, ~bangs, ~bob, ~layer, ~mohawk, ~perm, ~wave (wave_hair), +bald, +braid, +bun, +curl, +highlight, +part (part_hair), +ponytail, +trim (trim_cut), +wig, !cornrow, !dreadlock, !pigtail, !updo

### HAND PARTS  `hand_parts`
- правило: Parts of the human hand
- тип связи: `part_of`, базовая сложность 0.3
- слов: 15
- ~index finger, ~joint, ~tendon, +cuticle, +finger, +fingertip, +grip, +knuckle, +middle finger, +nail (nail_body), +palm (palm_hand), +pinky, +ring finger, +thumb, +wrist

### HOSPITAL THINGS  `hospital_things`
- правило: Things and places found in a hospital
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~ambulance, ~bandage, ~bed, ~chart, ~gown, ~monitor (monitor_medical), ~scalpel, ~waiting room, ~wheelchair, ~X-ray, +emergency room, +gurney, +IV, +oxygen mask, +scrubs, +stethoscope, +syringe, +ward

### ILLNESSES  `illnesses`
- правило: Common illnesses an average person can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~bronchitis, ~cold (cold_illness), ~pneumonia, ~sinusitis, ~strep throat, +allergy, +arthritis, +asthma, +diabetes, +fever, +flu, +infection, +measles, +migraine, +mumps, +rash, +ulcer, !chickenpox

### INTERNAL ORGANS  `internal_organs`
- правило: Organs inside the human body
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~appendix, ~brain, ~colon, ~gland, ~marrow, ~pancreas, ~womb, +artery, +bladder, +esophagus, +gallbladder, +heart (heart_organ), +intestine, +kidney, +liver, +lung, +spleen, +stomach, +thyroid, +vein

### MEDICINE CABINET  `medicine_cabinet`
- правило: Things kept in a home medicine cabinet
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- ~alcohol, ~sunscreen, ~thermometer, ~tweezers, ~vitamin, +aspirin, +bandage, +cotton swab, +cough syrup, +eye drops, +gauze, +ice pack, +ointment, +painkiller, !antacid, !lozenge

### MUSCLES  `muscles`
- правило: Muscles an average person can name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~abs, ~bicep, ~calf (calf_leg), ~quad, !core, !delt, !forearm, !glute, !hamstring, !lat, !obliques, !pec, !trap, !tricep

### EYE PARTS  `parts_of_the_eye`
- правило: Parts of the human eye
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brow, ~cornea, ~eyelid, ~iris, ~lash, ~lens, ~pupil, ~retina, ~socket (socket_eye), !optic nerve, !tear duct, !white (white_color)

### THE SENSES  `senses_and_perception`
- правило: Ways the human body senses the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~balance, ~hearing, ~itch, ~pain, ~pressure, ~sight, ~smell, ~taste, ~temperature, ~thirst, +hunger, +touch

### SYMPTOMS  `symptoms`
- правило: Signs that a person feels unwell
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~chills, ~dizziness, ~fatigue, +ache, +bruise, +congestion, +cough, +cramp, +fever, +headache, +itching, +nausea, +rash, +sneeze, +sore throat, +swelling

### BODY GROWTHS  `things_that_grow_on_you`
- правило: Things that grow naturally on the human body
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~beard, ~eyebrow, ~eyelash, ~freckle, ~hair, ~mole (mole_skin), ~mustache, ~skin, ~tooth, ~wart, ~whisker, !callus, !nail (nail_body), !sideburn

### PAINFUL THINGS  `things_that_hurt`
- правило: Everyday things that cause physical pain
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~bruise, ~burn, ~cramp, ~cut, ~headache, ~pinch, ~scrape, ~splinter, ~sprain, ~sunburn, ~thorn, !bee sting, !blister, !paper cut, !stubbed toe


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


## Тема: business

### ADVERTISING WORDS  `advertising_words`
- правило: Words used in advertising and marketing
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~campaign, ~coupon, ~jingle, +ad, +banner, +billboard, +brand (brand_company), +commercial, +endorsement, +flyer, +logo, +mascot, +promo, +slogan, +sponsor, +tagline

### BANKING WORDS  `banking_words`
- правило: Words used at a bank
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~balance, ~branch (branch_office), ~pin (pin_code), +account, +ATM, +check (check_payment), +deposit, +interest, +ledger, +loan, +mortgage, +overdraft, +safe deposit, +statement, +teller, +transfer, +vault, +withdrawal

### BUSINESS WORDS  `business_words`
- правило: Words used in running a business
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~brand (brand_company), ~market, ~partner, +asset, +budget, +client, +contract, +expense, +franchise, +inventory, +invoice, +loss, +merger, +payroll, +profit, +quota, +revenue, +startup, +stock, +vendor

### CAR BRANDS  `car_brands`
- правило: Car manufacturers sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~Chevrolet, +Audi, +BMW, +Buick, +Dodge, +ford (ford_brand), +Honda, +Hyundai, +Jeep, +Kia, +Lexus, +Mazda, +Mercedes, +Nissan, +Subaru, +Toyota, +Volkswagen, +Volvo

### US MONEY  `coins_and_bills`
- правило: Coins and bills used in the United States
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~five, ~note (note_money), ~ten, +bill (bill_money), +cent, +coin, +dime, +dollar, +fifty, +half dollar, +hundred, +nickel, +penny, +quarter (quarter_coin), +twenty

### CURRENCIES  `currencies`
- правило: Names of national currencies
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +baht, +dinar, +dollar, +euro, +franc, +lira, +peso, +pound (pound_money), +real, +ruble, +rupee, +won, +yen, !krona, !shekel

### FAMOUS BRANDS  `famous_brands`
- правило: Brand names most Americans recognize
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~Adidas, ~Chevrolet, ~Disney, ~ford (ford_brand), ~Lego, ~Levi, ~Nike, ~Pepsi, +Coca Cola, +Colgate, +Gillette, +Harley, +Hershey, +Kellogg, +Kodak, +McDonalds, +Nestle, !Crayola

### CONTRACT WORDS  `insurance_and_legal`
- правило: Words used in contracts and agreements
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~agreement, ~breach, ~claim, ~clause, ~liability, ~notice, ~policy, ~premium, ~renewal, ~signature, ~term (term_condition), ~witness, !deductible, !waiver

### JOB HUNTING  `job_hunting`
- правило: Words used when looking for a job
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~offer, ~orientation, ~reference, ~salary, +application, +benefits, +contract, +cover letter, +hire, +interview, +opening, +portfolio, +position, +recruiter, +resume, +screening

### MAIL WORDS  `mail_words`
- правило: Things involved in sending mail
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~label, ~tracking, +address, +carrier, +courier, +envelope, +letter (letter_mail), +mailbox, +package, +parcel, +post office, +postage, +postcard, +return address, +stamp (stamp_postage), +zip code

### MONEY WORDS  `money_words`
- правило: Everyday English words for money, payments and personal finance
- тип связи: `is_a`, базовая сложность 0.25
- слов: 27
- ~refund, +allowance, +bank (bank_finance), +bill (bill_money), +bonus, +budget, +capital (capital_money), +cash, +change, +check (check_payment), +coin, +credit, +debit, +debt, +deposit, +fee, +interest, +invoice, +loan, +receipt, +rent, +salary, +savings, +tax, +tip (tip_money), +wage, +wallet

### OFFICE WORDS  `office_words`
- правило: Things and routines found in an office workplace
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~badge, ~boss, ~copier, ~inbox, ~printer, +break room, +calendar, +conference call, +cubicle, +deadline, +desk, +intern, +meeting, +memo, +overtime, +shift (shift_work), +spreadsheet, +water cooler

### RESTAURANT WORDS  `restaurant_words`
- правило: Things and roles found at a restaurant
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~bar (bar_pub), ~bill (bill_money), ~receipt, ~special, ~table, ~tip (tip_money), +appetizer, +booth, +buffet, +chef, +counter, +dessert, +entree, +host (host_person), +kitchen, +menu, +napkin, +order, +reservation, +waiter

### SHOPPING WORDS  `shopping_words`
- правило: Words used while shopping in a store
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~aisle, ~basket, ~cart, ~checkout, ~line (line_queue), ~refund, ~shelf (shelf_furniture), ~tag (tag_label), +bag, +barcode, +cashier, +clearance, +coupon, +discount, +price, +receipt, +register, +sale

### STARTUP WORDS  `startup_words`
- правило: Words used when starting a new company
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~launch, !cofounder, !equity, !founder, !funding, !incubator, !investor, !pitch, !prototype, !runway, !scale, !seed round, !valuation, !venture

### KINDS OF STORES  `store_types`
- правило: Kinds of shops found in a town or mall
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~bakery, ~butcher, ~newsstand, ~pharmacy, ~salon, +barbershop, +bookstore, +boutique, +cafe, +deli, +florist, +gift shop, +grocery, +hardware store, +jeweler, +market, +pet shop, +shoe store, +thrift store, +toy store

### TECH COMPANIES  `tech_companies`
- правило: Well-known technology companies or consumer technology brands
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~Adobe, ~Amazon, ~apple (apple_company), ~Dell, ~Google, ~Microsoft, ~Nintendo, ~Oracle, ~Tesla, ~Zoom, +Cisco, +IBM, +Intel, +Netflix, +Nvidia, +PayPal, +Qualcomm, +Samsung, +Sony, +Spotify, +Uber


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


## Тема: entertainment

### AMUSEMENT PARK  `amusement_park`
- правило: Rides and things found at an amusement park
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~arcade, ~popcorn, ~prize, ~ticket (ticket_admission), +bumper car, +carousel, +cotton candy, +drop tower, +ferris wheel, +log flume, +mascot, +midway, +ride, +roller coaster, +souvenir, !funhouse, !teacups, !turnstile

### ART FORMS  `art_forms`
- правило: Forms of visual and performing art
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~dance, ~origami, ~weaving, +calligraphy, +collage, +drawing, +film, +mosaic, +music, +painting, +photography, +poetry, +pottery, +printmaking, +sculpture, +theater

### BOARD GAMES  `board_games`
- правило: Games played on a board with pieces or cards on a table
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~backgammon, ~Life, ~othello, ~sorry, ~trouble, +battleship, +candy land, +checkers, +chess, +chutes and ladders, +clue, +dominoes, +monopoly, +risk, +scrabble, +trivial pursuit, !jenga, !mancala, !yahtzee, xparcheesi

### CARD GAMES  `card_games`
- правило: Games played with a deck of cards
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~bridge (bridge_card), ~rummy, ~war, +blackjack, +crazy eights, +go fish, +hearts, +old maid, +poker, +Solitaire, +spades, +uno, !canasta, !cribbage, !euchre, !pinochle

### CARD WORDS  `card_words`
- правило: Words for the cards, suits and parts of a standard deck of playing cards
- тип связи: `found_in`, базовая сложность 0.3
- слов: 22
- ~club (club_card), ~cut, ~diamond (diamond_card), ~flush, ~hand (hand_cards), ~heart (heart_card), ~jack (jack_card), ~king, ~pair, ~queen (queen_card), ~straight, ~suit (suit_card), +Ace, +deal, +deck, +discard, +face card, +joker, +shuffle (shuffle_cards), +spade (spade_card), +trump, +wild card

### CIRCUS WORDS  `circus_words`
- правило: People, animals and objects you see at a traditional circus
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~cannon, ~cotton candy, ~net, ~popcorn, ~ring, ~ringmaster, ~sequin, ~unicycle, +acrobat, +clown, +elephant, +juggler, +lion tamer, +stilts, +tent, +tightrope, +trapeze, !sword swallower

### COMEDY WORDS  `comedy_words`
- правило: Words used about comedy performances
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~roast, ~routine, ~satire, ~sketch, ~timing, +gag, +heckler, +improv, +joke, +one liner, +parody, +pun, +punchline, +slapstick, +standup

### DANCE STYLES  `dance_styles`
- правило: Styles of dance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~flamenco, +ballet, +ballroom, +cha cha, +disco, +folk, +foxtrot, +hip hop, +jazz, +line dance, +polka, +salsa, +samba, +swing, +tango, +tap (tap_dance), +waltz, !breakdance

### COMPOSERS  `famous_composers`
- правило: Famous classical composers
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~Chopin, +Bach, +Beethoven, +Brahms, +Debussy, +Handel, +Haydn, +Liszt, +Mozart, +Schubert, +Tchaikovsky, +Verdi, +Vivaldi, +Wagner

### MYTHICAL CREATURES  `fantasy_creatures`
- правило: Creatures from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~elf, ~fairy, ~giant, ~gnome, ~kraken, ~mermaid, ~sphinx, ~vampire, +centaur, +dragon, +goblin, +griffin, +minotaur, +ogre, +pegasus, +phoenix (phoenix_bird), +troll, +unicorn, +werewolf, +yeti

### ORCHESTRA SECTIONS  `instruments_in_an_orchestra`
- правило: Sections and roles in a symphony orchestra
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brass, ~conductor, ~ensemble, ~percussion, ~strings, ~woodwind, !cellist, !concertmaster, !first violin, !section, !soloist, xtimpanist

### THINGS WITH STRINGS  `instruments_you_strum`
- правило: Objects that have strings as an essential part
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~apron (apron_garment), ~balloon, ~banjo, ~bow (bow_music), ~cello, ~guitar, ~hammock, ~harp, ~kite (kite_toy), ~piano, ~puppet, ~violin, ~yo-yo, !marionette, !tennis racket

### MAGIC SHOW  `magic_words`
- правило: Things used in a stage magic performance
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~assistant, ~box, ~cape, ~chain, ~coin, ~deck, ~dove, ~handcuffs, ~mirror, ~rabbit, ~rope, ~scarf, ~smoke, ~top hat, +hat, +illusion, +trick, +wand

### MOVIE GENRES  `movie_genres`
- правило: Categories used to classify films
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~adventure, ~fantasy, ~musical, ~mystery, ~romance, ~satire, ~sci-fi, ~war, +action, +animation, +biopic, +comedy, +documentary, +drama, +horror, +noir, +thriller, +western

### FILM MAKING  `movie_words`
- правило: Words used in making and showing films
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~camera, ~cut, ~extra, ~screenplay, ~set (set_film), ~take, +actor, +box office, +cast (cast_people), +close up, +credits, +director, +editing, +matinee, +premiere, +scene, +script, +sequel, +stunt, +trailer (trailer_movie)

### MUSIC GENRES  `music_genres`
- правило: Styles used to classify music
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~rock (rock_music), +blues, +classical, +country, +disco, +folk, +funk, +gospel, +hip hop, +indie, +jazz, +metal, +opera, +pop (pop_music), +punk, +rap, +reggae, +soul, +swing, +techno

### MUSIC WORDS  `music_words`
- правило: Words used to describe how a piece of music is written or performed
- тип связи: `found_in`, базовая сложность 0.3
- слов: 25
- ~bar (bar_music), ~bridge (bridge_music), ~clef, ~flat, ~key (key_music), ~pitch (pitch_music), ~rest (rest_music), ~scale (scale_music), ~Sharp, ~staff, +beat, +chord, +chorus, +duet, +harmony, +measure, +melody, +note (note_music), +octave, +refrain, +rhythm, +riff, +solo, +tempo, +verse

### MUSICAL INSTRUMENTS  `musical_instruments`
- правило: Instruments played to produce music
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~keyboard (keyboard_music), ~ukulele, +accordion, +bagpipes, +banjo, +bassoon, +cello, +clarinet, +cymbal, +drum, +flute, +guitar, +harmonica, +harp, +mandolin, +oboe, +organ (organ_music), +piano, +saxophone, +tambourine, +trombone, +trumpet, +tuba, +violin, !xylophone

### PARTY THINGS  `party_things`
- правило: Things found at a birthday party
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~balloon, ~banner, ~cake, ~candle, ~candy, ~game, ~guest, ~music, ~napkin, ~piñata, ~plate, ~prize, ~punch (punch_drink), ~ribbon, +confetti, +favor, +invitation, +party hat, +present (present_gift), +streamer

### PERCUSSION INSTRUMENTS  `percussion`
- правило: Musical instruments played by striking or shaking
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~chime, ~triangle, +bongo, +cymbal, +drum, +gong, +snare, +tambourine, !castanets, !cowbell, !maraca, !marimba, !timpani, !xylophone

### READING MATTER  `reading_material`
- правило: Things people read
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~brochure, ~label, ~letter (letter_mail), ~map, ~menu, ~poem, ~script, ~sign, ~textbook, ~ticket (ticket_admission), +article, +blog, +book, +comic, +diary, +magazine, +manual, +newspaper, +novel, +recipe

### TALE CHARACTERS  `storybook_characters`
- правило: Characters that appear in classic fairy tales
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~dwarf, ~elf, ~frog, ~giant, ~king, ~knight, ~mermaid, ~Prince, ~queen (queen_royal), ~wolf, +dragon, +fairy, +genie, +goblin, +ogre, +princess, +troll, +unicorn, +witch, +wizard

### STRING INSTRUMENTS  `string_instruments`
- правило: Musical instruments played by plucking or bowing strings
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~lute, +banjo, +bass (bass_music), +cello, +fiddle, +guitar, +harp, +harpsichord, +mandolin, +ukulele, +viola, +violin, !sitar, !zither

### THEATER WORDS  `theater_words`
- правило: Words for the parts and people of a live theater production
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~aisle, ~wings, +act, +backstage, +balcony (balcony_theater), +box office, +cast (cast_people), +curtain, +encore, +intermission, +matinee, +monologue, +prop, +rehearsal, +script, +spotlight, +stage, +understudy, +usher, !playbill

### TOYS  `toys`
- правило: Things children play with
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~blocks, ~bubble, ~crayon, ~jump rope, ~kite (kite_toy), ~marble (marble_toy), ~puzzle, ~rattle (rattle_toy), ~robot, ~top (top_spin), ~tricycle, +action figure, +ball (ball_sphere), +doll, +frisbee, +jack in the box, +Slinky, +teddy bear, +train set, +yo-yo

### TELEVISION WORDS  `tv_words`
- правило: Words used about television programs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~finale, ~host (host_presenter), ~network, ~pilot, ~season (season_time), +broadcast, +cable, +channel, +commercial, +episode, +ratings, +remote (remote_device), +rerun, +screen (screen_display), +sitcom, +spinoff, +streaming, +subtitle

### GAMING WORDS  `video_game_words`
- правило: Words used when playing video games
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~boss, ~lag, ~save, +arcade, +avatar, +cheat code, +checkpoint, +console, +controller, +health bar, +joystick, +level, +loot, +multiplayer, +power up, +quest, +score (score_points), !respawn

### WIND INSTRUMENTS  `wind_instruments`
- правило: Musical instruments played by blowing air
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~whistle, +bagpipes, +bassoon, +clarinet, +flute, +french horn, +harmonica, +oboe, +piccolo, +recorder, +saxophone, +trombone, +trumpet, +tuba


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


## Тема: fashion

### BAGS AND CASES  `bags`
- правило: Kinds of bag people carry
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~fanny pack, ~trunk (trunk_case), +backpack, +briefcase, +clutch, +duffel, +garment bag, +gym bag, +messenger bag, +pouch, +purse, +satchel, +suitcase, +tote, +wallet

### BEAUTY TOOLS  `beauty_tools`
- правило: Tools used for hair, nails and makeup
- тип связи: `used_in`, базовая сложность 0.35
- слов: 15
- ~buffer, ~file (file_tool), ~mirror, ~razor, ~sponge (sponge_cleaning), +applicator, +brush, +clipper, +comb, +curler, +curling iron, +dryer, +roller, +tweezers, !straightener

### EYEWEAR  `eyewear`
- правило: Things worn over the eyes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~blindfold, ~mask, ~monocle, +contacts, +glasses, +goggles, +reading glasses, +safety glasses, +shades, +sunglasses, +visor, !bifocals

### FASHION ACCESSORIES  `fashion_accessories`
- правило: Items added to complete a look
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~brooch, ~hat, ~scarf, ~sunglasses, ~tie (tie_clothing), ~watch (watch_object), +belt, +bracelet, +cufflinks, +earring, +gloves, +necklace, +pocket square, +suspenders, !bowtie, !hairband

### FASHION SHOW  `fashion_show`
- правило: Things found at a fashion show
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~camera, ~collection, ~program, ~runway, +backstage, +designer, +fitting, +front row, +model, +outfit, +pose, +rack, +seamstress, +spotlight

### FASHION STYLES  `fashion_styles`
- правило: Named styles of dressing
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bohemian, ~preppy, ~punk, ~sporty, ~western, +business casual, +casual, +classic, +formal, +gothic, +minimalist, +retro, +streetwear, +vintage

### HAIRSTYLES  `hairstyles`
- правило: Ways of styling hair
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~bangs, ~bob, ~pixie, +afro, +beehive, +braid, +bun, +crew cut, +dreadlocks, +layers, +mohawk, +perm, +pigtails, +ponytail, !chignon, !cornrows, !topknot, !updo

### JEWELRY STONES  `jewelry_stones`
- правило: Stones set into jewelry
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~jade, ~pearl, +amethyst, +aquamarine, +diamond, +emerald, +garnet, +moonstone, +onyx, +opal, +peridot, +ruby, +sapphire, +topaz, +turquoise

### MAKEUP  `makeup`
- правило: Cosmetics applied to the face
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~gloss, ~highlighter, +blush, +bronzer, +brow pencil, +concealer, +eyeliner, +eyeshadow, +foundation (foundation_makeup), +lipstick, +mascara, +powder, +primer, +setting spray

### NAIL CARE  `nail_words`
- правило: Things used for manicures and nail care
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~glitter, ~remover, ~soak, ~wrap, +acrylic, +base coat, +buffer, +clipper, +cuticle, +file (file_tool), +gel, +polish (polish_product), +pusher, +top coat

### PATTERNS  `patterns`
- правило: Patterns printed on cloth
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~camouflage, ~floral, +animal print, +argyle, +checkered, +chevron, +paisley, +plaid, +polka dot, +stripe, +tartan, +tie dye, !gingham, !herringbone, !houndstooth

### FRAGRANCE WORDS  `perfume_words`
- правило: Words used to describe perfumes and scents
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~amber, ~citrus, ~Cologne, ~floral, ~fresh (fresh_scent), ~lavender (lavender_plant), ~musk, ~rose, ~spicy, ~sweet, ~vanilla, ~woody, !mist, !note (note_scent), !sandalwood

### GARMENT DETAILS  `sewing_patterns`
- правило: Details sewn into a garment design
- тип связи: `part_of`, базовая сложность 0.4
- слов: 15
- ~collar, ~cuff, ~dart (dart_sew), ~hem, ~lapel, ~lining, ~panel, ~pocket, ~ruffle, ~seam, ~trim (trim_edging), !applique, !gusset, !pleat, !yoke

### SHOE STYLES  `shoe_styles`
- правило: Styles of shoe
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~flat, ~mule, ~platform, ~pump, +boot (boot_shoe), +clog, +heel, +oxford, +sandal, +slipper, +sneaker, +stiletto, +wedge, !loafer, !moccasin, xespadrille

### WARDROBE CARE  `wardrobe_care`
- правило: Things used to store and care for clothes
- тип связи: `used_in`, базовая сложность 0.4
- слов: 13
- ~brush, ~hook (hook_fastener), ~iron (iron_appliance), ~shelf (shelf_furniture), +cedar block, +closet, +drawer, +garment bag, +hanger, +lint roller, +shoe tree, +steamer, !mothball


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


## Тема: food_more

### CEREAL TYPES  `breakfast_cereals_types`
- правило: Kinds of breakfast cereal by form
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~muesli, +bran, +clusters, +flakes, +granola, +loops, +oatmeal, +porridge, +puffs, +shredded wheat, +squares, !crisped rice

### CANDY TYPES  `candy_shapes`
- правило: Forms candy is sold in
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~ball (ball_sphere), ~bar (bar_block), ~brittle (brittle_candy), ~chew, ~cluster, ~drop, ~jelly, ~lollipop, ~mint (mint_candy), ~ribbon, ~stick (stick_candy), +chocolate square, +gummy, +hard candy

### CHEESE DISHES  `cheese_dishes`
- правило: Dishes built around cheese
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~cheesecake, +cheese board, +fondue, +grilled cheese, +lasagna, +mac and cheese, +nachos, +pizza, +queso, !gratin, !quesadilla, !raclette

### COOKIE TYPES  `cookie_types`
- правило: Kinds of cookie baked at home or sold in stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~molasses, ~oatmeal, ~peanut butter, +chocolate chip, +fortune cookie, +gingerbread, +sandwich cookie, +shortbread, +sugar, +wafer, !biscotti, !macaroon, !snickerdoodle, !thumbprint

### COOKING METHODS  `cooking_methods`
- правило: Methods used to cook food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~broil, ~roast, ~simmer, ~smoke, ~stir fry, +bake, +barbecue, +blanch, +boil, +deep fry, +fry (fry_cook), +grill, +poach, +sear, +slow cook, +steam, !braise, !saute

### CUTS OF MEAT  `cuts_of_meat`
- правило: Cuts of meat sold by a butcher
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~brisket, ~rib, ~round (round_meat), ~shoulder (shoulder_meat), +chuck, +flank, +loin, +rump, +shank, +short rib, +sirloin, +T-bone, +tenderloin, !porterhouse, !ribeye

### DESSERT TOPPINGS  `dessert_toppings`
- правило: Things put on top of desserts
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~cherry, ~coconut, ~marshmallow, ~nuts, +caramel, +chocolate sauce, +frosting, +fruit, +glaze, +hot fudge, +powdered sugar, +sprinkles, +syrup, +whipped cream

### DRINK MIXERS  `drink_mixers`
- правило: Things mixed into drinks
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~cola, ~cranberry, ~cream (cream_dairy), ~ice, ~mint (mint_herb), ~syrup, +bitters, +ginger ale, +juice, +lemonade, +lime, +soda water, +sour mix, +tonic

### BRUNCH DISHES  `egg_and_dairy_dishes`
- правило: Dishes served at brunch
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~omelet, ~quiche, ~scone, +bagel and lox, +casserole, +crepe, +eggs benedict, +french toast, +hash, +mimosa, +strata, +waffle, !frittata, !parfait

### PASTA DISHES  `pasta_dishes`
- правило: Named pasta dishes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~lasagna, +alfredo, +bolognese, +mac and cheese, +marinara, +pesto pasta, +spaghetti and meatballs, !baked ziti, !carbonara, !primavera, !puttanesca, xcacio e pepe

### PIE TYPES  `pie_types`
- правило: Kinds of pie
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~chess, +apple, +banana cream, +blueberry, +cherry, +chicken pot, +custard, +key lime, +lemon meringue, +mince, +peach, +pecan, +pumpkin, +rhubarb, +shepherds

### POTATO DISHES  `potato_dishes`
- правило: Ways potatoes are cooked and served
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +baked, +chips, +fried, +hash browns, +home fries, +mashed, +potato salad, +scalloped, +twice baked, +wedges, !au gratin, !croquette, !latke, !tater tots

### SALADS  `salads`
- правило: Named kinds of salad
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~garden, ~greek, +caesar, +chef salad, +cobb, +coleslaw, +egg salad, +fruit salad, +macaroni salad, +pasta salad, +potato salad, +spinach salad, +waldorf, !caprese

### SANDWICH BREADS  `sandwich_breads`
- правило: Breads used to make a sandwich
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~croissant, ~white (white_food), +bagel, +brioche bun, +english muffin, +pita, +roll (roll_bread), +rye, +sourdough, +texas toast, +wheat, !ciabatta, !focaccia, !hoagie roll

### SANDWICH TYPES  `sandwich_types`
- правило: Named kinds of sandwich
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~club, ~hero, ~wrap, +blt, +grilled cheese, +monte cristo, +panini, +patty melt, +po boy, +reuben, +sloppy joe, !hoagie, !philly cheesesteak, xmuffuletta

### GARNISHES  `toppings_and_garnish`
- правило: Things added on top of a finished dish
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~cheese, ~cherry, ~olive, ~paprika, ~parsley, ~sesame, ~sprinkles, ~whipped cream, +bacon bits, +chives, +lemon wedge, +mint leaf, +powdered sugar, !croutons, !scallion


## Тема: geography

### AFRICAN COUNTRIES  `african_countries`
- правило: Countries located in Africa
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~Egypt, ~Kenya, ~Morocco, +Algeria, +Angola, +Botswana, +Chad, +Ethiopia, +Ghana, +Libya, +Namibia, +Nigeria, +Rwanda, +Senegal, +Somalia, +Sudan, +Tanzania, +Tunisia, +Uganda, +Zambia

### ASIAN COUNTRIES  `asian_countries`
- правило: Countries located in Asia
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~Bangladesh, ~Iran, ~Pakistan, ~turkey (turkey_country), +Cambodia, +China, +India, +Indonesia, +Israel, +Japan, +Jordan, +Korea, +Laos, +Malaysia, +Mongolia, +Nepal, +Philippines, +Singapore, +Thailand, +Vietnam

### CITY WORDS  `city_words`
- правило: Words for the parts and features of a city
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~park (park_place), ~Subway, ~tower, +alley, +avenue, +block (block_cube), +boulevard, +bridge (bridge_structure), +curb, +district, +downtown, +intersection, +neighborhood, +plaza, +sidewalk, +skyline, +skyscraper, +street, +suburb, +traffic

### CLIMATE WORDS  `climate_zones`
- правило: Words describing the climate of a region
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Arctic, ~continental, ~humid, ~mediterranean, ~monsoon, ~polar, ~rainforest, ~temperate, +alpine, +arid, +coastal, +desert, +subtropical, +tropical

### COLD PLACES  `cold_places`
- правило: Places that are typically cold
- тип связи: `has_property`, базовая сложность 0.3
- слов: 14
- ~Antarctica, ~Arctic, ~basement, ~cave, ~freezer, ~glacier, ~iceberg, ~igloo, ~mountain, ~north pole, ~refrigerator, ~tundra, !ski slope, !snowfield

### CONTINENTS AND OCEANS  `continents_and_oceans`
- правило: The continents and the world oceans
- тип связи: `is_a`, базовая сложность 0.2
- слов: 12
- ~Arctic, ~Indian, ~Pacific, ~Southern, +Africa, +Antarctica, +Asia, +Atlantic, +Australia, +Europe, +North America, +South America

### DESERTS  `deserts_and_wild_places`
- правило: Major deserts of the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 10
- !Arabian, !Atacama, !Death Valley, !Gobi, !Great Basin, !Kalahari, !Mojave, !Painted Desert, !Sahara, !Sonoran

### DIRECTIONS  `directions`
- правило: Words used to give directions
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~far, ~near, ~right, ~straight, +across, +around, +back, +behind, +beside, +down, +east, +forward, +left, +north, +over, +south, +through, +under, +up, +west

### EUROPEAN COUNTRIES  `european_countries`
- правило: Countries located in Europe
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~Greece, ~Hungary, ~Netherlands, ~Portugal, +Austria, +Belgium, +Bulgaria, +Croatia, +Denmark, +Estonia, +Finland, +France, +Germany, +Iceland, +Ireland, +Italy, +Norway, +Poland, +Romania, +Scotland, +Serbia, +Slovakia, +Spain, +Sweden, +Switzerland

### FAMOUS LANDMARKS  `famous_landmarks`
- правило: World landmarks most people can recognize
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Colosseum, ~White House, +Acropolis, +Big Ben, +Eiffel Tower, +Empire State, +Golden Gate, +Great Wall, +Leaning Tower, +Mount Rushmore, +pyramid (pyramid_monument), +sphinx, +Statue of Liberty, +Stonehenge, +Taj Mahal

### HOT PLACES  `hot_places`
- правило: Places that are typically hot
- тип связи: `has_property`, базовая сложность 0.35
- слов: 15
- ~attic, ~beach, ~campfire, ~desert, ~engine, ~equator, ~furnace, ~jungle, ~kitchen, ~oven, ~sauna, ~sun, ~tropics, ~volcano, !greenhouse

### ISLANDS  `islands`
- правило: Well known islands around the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Iceland, ~Jamaica, +Bali, +Barbados, +Bermuda, +Crete, +Cuba, +Fiji, +Greenland, +Hawaii, +Madagascar, +Malta, +Sardinia, +Sicily, +Tahiti

### LANDFORMS  `landforms`
- правило: Natural features of the land surface
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~basin, ~cave, ~crater, ~delta (delta_river), ~dune, ~glacier, ~isthmus, ~marsh, ~plain, ~ridge, ~tundra, +butte, +canyon, +cliff, +foothill, +gorge, +hill, +island, +mesa, +mountain, +peninsula, +plateau, +prairie, +summit, +valley

### LATIN AMERICA  `latin_american_countries`
- правило: Countries of Central and South America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +Argentina, +Belize, +Bolivia, +Brazil, +Chile, +Colombia, +Costa Rica, +Cuba, +Ecuador, +Guatemala, +Honduras, +Mexico, +Nicaragua, +panama, +Paraguay, +Peru, +Uruguay, +Venezuela

### MAP WORDS  `map_words`
- правило: Words used to read and describe a map
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~border, ~elevation, ~key, ~latitude, ~legend, ~route, ~scale, ~symbol, +atlas (atlas_book), +compass, +contour, +coordinate, +east, +globe, +grid, +longitude, +meridian, +north, +south, +west

### MOUNTAIN RANGES  `mountain_ranges`
- правило: Major mountain ranges of the world
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~atlas (atlas_mountains), +Alps, +Andes, +Cascades, +Himalayas, +Ozarks, +Pyrenees, +Rockies, +Sierra Nevada, +Urals, !Appalachians, !Carpathians

### PARK WORDS  `national_parks`
- правило: Things found in a national park or campground
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~canyon, ~lantern, ~map, ~overlook, ~path, ~waterfall, +bear box, +cabin (cabin_house), +campfire, +campsite, +geyser, +lodge, +picnic table, +Ranger, +tent, +trail, +visitor center, +wildlife

### WAITING PLACES  `places_you_wait`
- правило: Places where people commonly stand in line
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~buffet, ~checkout, ~grocery store, ~restaurant, !airport, !amusement park, !bank, !bus stop, !DMV, !doctor office, !pharmacy, !post office, !theater, !ticket booth

### QUIET PLACES  `quiet_places`
- правило: Places where people are expected to stay quiet
- тип связи: `has_property`, базовая сложность 0.35
- слов: 12
- ~cemetery, ~church, ~classroom, ~funeral, ~hospital, ~library, ~monastery, !courtroom, !exam room, !museum, !study hall, !theater

### RIVERS  `rivers`
- правило: Major rivers of the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~Colorado, +Amazon, +Congo, +Danube, +Euphrates, +Ganges, +Hudson, +Mississippi, +Missouri, +Nile, +Rhine, +Rio Grande, +Seine, +Thames, +Volga, +Yangtze

### FARM THINGS  `things_on_a_farm`
- правило: Things found on a working farm
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~coop, ~fence, ~pen (pen_animal), ~stable, ~well, +bale, +barn, +crop, +field, +gate (gate_barrier), +harvest, +hay, +orchard, +pasture, +plow, +scarecrow, +silo, +tractor, +trough, +windmill

### TOWN PLACES  `town_places`
- правило: Public buildings and places found in an ordinary American town
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- ~bank (bank_finance), ~cemetery, ~church, ~diner, ~gym, ~jail, ~library, ~market, ~museum, ~park (park_place), ~playground, ~post office, ~school, ~stadium, ~station (station_place), ~temple (temple_building), ~theater, +city hall, +clinic, +courthouse, +firehouse, +hospital, +mall, +pharmacy, +plaza

### US CITIES  `us_cities`
- правило: Large cities in the United States
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~Houston, ~Miami, ~Philadelphia, +Atlanta, +Austin, +Baltimore, +Boston, +Charlotte, +Chicago, +Cleveland, +Dallas, +Denver, +Detroit, +Memphis, +Milwaukee, +Nashville, +Orlando, +phoenix (phoenix_city), +Portland, +Seattle

### US STATES  `us_states`
- правило: States of the United States of America
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- +Alabama, +Alaska, +Arizona, +California, +Colorado, +Delaware, +Florida, +Georgia, +Hawaii, +idaho (idaho_state), +Indiana, +Iowa, +Kansas, +Maine, +Michigan, +Montana, +Nebraska, +Nevada, +Ohio, +Oregon, +Texas, +Utah, +Vermont, +Virginia, +Wyoming

### WORLD CAPITALS  `world_capitals`
- правило: Capital cities of countries around the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~Berlin, ~Cairo, ~Lima, ~Madrid, ~Paris, ~Rome, +Amsterdam, +Athens, +Bangkok, +Beijing, +Budapest, +Dublin, +Havana, +Helsinki, +Lisbon, +London, +Moscow, +Nairobi, +Oslo, +Ottawa, +Prague, +Seoul, +Tokyo, +Vienna, +Warsaw


## Тема: history

### ANCIENT CIVILIZATIONS  `ancient_civilizations`
- правило: Civilizations of the ancient world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~China, ~Egypt, ~Greece, ~Rome, +Assyria, +Aztec, +Babylon, +Carthage, +Inca, +Maya, +Persia, +Sparta, +Troy, !Phoenicia, !Sumer

### WORLD WONDERS  `ancient_wonders`
- правило: Structures known as wonders of the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~Colosseum, ~Lighthouse, +Colossus, +Great Pyramid, +Great Wall, +Hanging Gardens, +Petra, +Stonehenge, +Taj Mahal, !Chichen Itza, !Machu Picchu

### ARCHAEOLOGY WORDS  `archaeology_words`
- правило: Things involved in digging up the past
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~artifact, ~bone, ~dig, ~fossil, ~ruin, ~site, ~skeleton, ~tomb, ~trowel, !carbon dating, !excavation, !layer, !pottery, !relic, !shard

### CASTLE THINGS  `castle_things`
- правило: Parts and features of a medieval castle
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~banner, ~chapel, ~courtyard, ~hall, ~moat, ~throne, ~turret, +armory, +chamber, +drawbridge, +dungeon, +gate (gate_barrier), +keep, +rampart, +tower, +wall, !battlement, !portcullis

### COLONIAL AMERICA  `colonial_america`
- правило: Things associated with colonial America
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~bonnet, ~pilgrim, ~settler, ~wagon, !blacksmith, !churn, !colony, !lantern, !musket, !plantation, !quill, !spinning wheel, !tavern, !town crier, !tricorn hat

### ANCIENT EGYPT  `egypt_things`
- правило: Things associated with ancient Egypt
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~scarab, ~scroll (scroll_paper), ~temple, +chariot, +mummy, +Nile, +obelisk, +papyrus, +pharaoh, +pyramid (pyramid_monument), +sarcophagus, +sphinx, +tomb, !canopic jar, !hieroglyph

### AGE OF EXPLORATION  `exploration_words`
- правило: Things associated with sea exploration in the age of sail
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~colony, ~compass, ~map, ~spice, ~telescope, +cargo, +charter, +crew, +expedition, +galleon, +harbor, +sail (sail_voyage), +trade route, +voyage, !sextant

### HISTORIC DOCUMENTS  `historic_documents`
- правило: Famous documents from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 8
- +Bill of Rights, +Constitution, +Declaration of Independence, +Emancipation Proclamation, +Gettysburg Address, +Magna Carta, +Rosetta Stone, +Treaty of Versailles

### FAMOUS SHIPS  `historic_ships`
- правило: Ships famous from history
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~beagle, ~Bounty, ~titanic (titanic_ship), +Ark, +Constitution, +Endeavour, +Mayflower, +Nina, +Santa Maria, +Victory, !Pinta

### INDUSTRIAL AGE  `industrial_revolution`
- правило: Things associated with the industrial revolution
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~assembly line, ~canal, ~coal, ~factory, ~machine, ~mill, ~railroad, ~worker, !cotton gin, !foundry, !loom, !smokestack, !steam engine, !telegraph

### KNIGHT THINGS  `knights_and_armor`
- правило: Things a medieval knight used or wore
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~banner, ~crest, ~helmet, ~horse, ~saddle, +armor, +dagger, +gauntlet, +lance, +shield, +spur, +squire, +sword, +visor, !breastplate, !chainmail

### HISTORIC TRADES  `old_professions`
- правило: Trades that were common in past centuries
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- !apothecary, !blacksmith, !chandler, !cobbler, !cooper, !fletcher, !mason, !miller, !potter, !scribe, !silversmith, !tanner, !thatcher, !weaver, !wheelwright

### PIRATE WORDS  `pirate_words`
- правило: Things and words associated with pirates
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~buccaneer, ~cannon, ~chest (chest_box), ~compass, ~eyepatch, ~flag, ~hook (hook_pirate), ~island, ~map, ~parrot, ~rum, ~sword, +anchor, +crew, +mast, +plank, +ship, +treasure, !doubloon, !spyglass

### ANCIENT ROME  `roman_things`
- правило: Things associated with ancient Rome
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~amphitheater, ~aqueduct, ~emperor, ~laurel, ~mosaic, ~senate, +arena, +centurion, +chariot, +Colosseum, +forum, +gladiator, +legion, +toga, +villa

### ROYAL WORDS  `royalty`
- правило: Titles and things belonging to royalty
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~court (court_royal), ~duchess, ~jewel, ~robe, +castle, +coronation, +crown (crown_royal), +duke, +empire, +heir, +king, +knight, +monarch, +palace, +Prince, +princess, +queen (queen_royal), +royal, +scepter, +throne

### BYGONE THINGS  `time_capsule_things`
- правило: Everyday objects that are no longer commonly used
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~corset, ~monocle, ~telegram, ~typewriter, !butter churn, !icebox, !inkwell, !oil lamp, !phonograph, !pocket watch, !quill, !spinning wheel, !wagon wheel, !washboard

### HISTORIC TRANSPORT  `transportation_history`
- правило: Ways people traveled before cars
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~camel, ~canoe, ~ferry, ~foot (foot_body), ~sled, ~trolley, +carriage, +chariot, +horse, +mule, +rickshaw, +sailing ship, +stagecoach, +steamboat, +wagon

### FAMOUS WARS  `wars`
- правило: Wars widely known from history
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- ~Vietnam, +Civil War, +Cold War, +Crusades, +Hundred Years War, +Korean War, +Revolutionary War, +Trojan War, +War of 1812, +World War

### OLD WEAPONS  `weapons_of_the_past`
- правило: Weapons used before modern firearms
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~arrow, +axe, +bow (bow_weapon), +catapult, +club, +crossbow, +dagger, +flail, +javelin, +mace, +musket, +sling, +spear, +sword, +trident, !halberd

### WILD WEST  `wild_west`
- правило: Things associated with the American Old West
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~cactus, ~corral, ~prairie, ~sheriff, ~wagon, +bandit, +boots, +cowboy, +gold rush, +horse, +lasso, +marshal, +outlaw, +ranch, +revolver, +rodeo, +saloon, +spurs, +stagecoach, +tumbleweed


## Тема: hobbies

### BIRDWATCHING THINGS  `birdwatching`
- правило: Things a birdwatcher uses
- тип связи: `used_in`, базовая сложность 0.4
- слов: 12
- ~birdhouse, ~blind, ~camera, ~notebook, ~seed, ~whistle, +binoculars, +bird bath, +checklist, +feeder, +field guide, +scope

### GAME PIECES  `board_game_pieces`
- правило: Pieces and parts used in board games
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~card (card_playing), ~chip, ~cup, ~marker, ~pawn, ~tile, ~timer, ~token, +board (board_game), +dice (dice_game), +rulebook, +scorepad, +spinner, xmeeple

### CAMPING GEAR  `camping_gear`
- правило: Gear packed for a camping trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~backpack, ~canteen, ~compass, ~cooler, ~flashlight, ~hatchet, ~lantern, ~map, ~matches, ~rope, ~stove, ~thermos, +bug spray, +camp chair, +firewood, +first aid kit, +mess kit, +sleeping bag, +tarp, +tent

### CHESS WORDS  `chess_words`
- правило: Pieces and moves in a game of chess
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~board (board_game), ~capture, ~castle, ~check (check_chess), ~king, ~opening, ~promotion, ~queen (queen_card), +bishop, +checkmate, +gambit, +knight, +pawn, +rook, +stalemate, !en passant

### COLLECTIBLES  `collecting_hobbies`
- правило: Things people collect as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~autograph, ~badge, ~button (button_clothing), ~card (card_playing), ~coin, ~comic, ~doll, ~figurine, ~key, ~magnet, ~marble (marble_toy), ~postcard, ~record, ~rock (rock_stone), ~shell, ~spoon, ~stamp (stamp_postage), ~thimble, +bottle cap, !matchbook

### HOME BAKING  `cooking_hobby`
- правило: Things a home baker uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~cutter, ~mitt, ~mold (mold_form), ~oven, ~scale, ~sheet (sheet_pan), ~timer, +apron (apron_garment), +cooling rack, +measuring cup, +mixing bowl, +piping bag, +rolling pin, +spatula, +whisk, !sifter

### CRAFT MATERIALS  `crafting_materials`
- правило: Materials used in craft projects
- тип связи: `made_of`, базовая сложность 0.3
- слов: 18
- ~bead, ~button (button_clothing), ~cardboard, ~clay, ~felt, ~foam, ~glitter, ~glue, ~paint, ~paper, ~ribbon, ~wire, ~yarn, +fabric, +pipe cleaner, +popsicle stick, +sequin, +string

### DANCE CLASS  `dance_class`
- правило: Things found in a dance class
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~instructor, ~mirror, ~music, ~routine, ~slippers, ~spin, ~stage, +barre, +leotard, +mat, +pointe shoe, +stretch, +tights, +tutu

### FISHING TRIP  `fishing_hobby`
- правило: Things taken on a fishing trip
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~boat, ~bucket, ~cooler, ~hat, ~license, ~sunscreen, +bait, +hook (hook_fishing), +line (line_cord), +lure, +net, +reel (reel_fishing), +rod, +stringer, +tackle box, !waders

### GARDEN HOBBY  `gardening_hobby`
- правило: Things a hobby gardener uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~gloves, ~greenhouse, ~hose, ~planter, ~pot, ~stake, ~trowel, ~twine, ~watering can, +compost bin, +fertilizer, +seed packet, +soil, +trellis, +wheelbarrow, !pruner

### HIKING WORDS  `hiking_words`
- правило: Things involved in hiking a trail
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~backpack, ~boots, ~canteen, ~map, ~poles, ~ridge, ~summit, ~trail, +blaze, +blister, +cairn, +campsite, +elevation, +trailhead, +water bottle, !switchback

### HOBBY ACTIVITIES  `hobby_verbs`
- правило: Activities people do as a hobby
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~baking, ~camping, ~chess, ~cycling, ~dancing, ~fishing, ~gardening, ~hiking, ~knitting, ~painting, ~photography, ~reading, ~sewing, ~singing, ~woodworking, +collecting, +drawing, +running, +writing, !birdwatching

### KNITTING WORDS  `knitting_words`
- правило: Things used in knitting and crochet
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~ball (ball_sphere), ~loop, ~needle (needle_sewing), ~pattern, ~purl, ~stitch, ~yarn, !bind off, !cast on, !gauge, !hook (hook_crochet), !marker, !row, !skein

### MAGIC PROPS  `magic_tricks`
- правило: Props used in performing magic tricks
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~ball (ball_sphere), ~cup, ~hat, ~ring, ~rope, ~scarf, !box, !card (card_playing), !coin, !dove, !handcuff, !mirror, !thumb tip, !wand

### MODEL KITS  `model_building`
- правило: Things used to build scale models
- тип связи: `used_in`, базовая сложность 0.4
- слов: 14
- ~brush, ~clamp, ~glue, ~kit, ~plastic, ~sandpaper, ~tweezers, !base, !decal, !instructions, !knife, !paint, !putty, !scale

### MUSIC PRACTICE  `music_practice`
- правило: Things used when practicing an instrument
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~amplifier, ~bench (bench_seat), ~bow (bow_music), ~case (case_box), ~metronome, ~mute, ~reed, ~strap, +capo, +pick, +rosin, +sheet music, +stand (stand_holder), +tuner

### PHOTOGRAPHY GEAR  `photography_hobby`
- правило: Gear a hobby photographer uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~bag, ~battery, ~camera, ~filter, ~hood (hood_lens), ~remote (remote_device), ~strap, +backdrop, +flash, +lens, +memory card, +reflector, +tripod, !lightbox

### PUZZLES  `puzzle_types`
- правило: Kinds of puzzle people solve for fun
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +anagram, +crossword, +jigsaw, +logic puzzle, +maze, +rebus, +riddle, +sudoku, +word search, !acrostic, !brainteaser, !cryptogram, !rubiks cube, !tangram

### GAMING SETUP  `video_gaming`
- правило: Things in a video gaming setup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~cable, ~cartridge, ~chair, ~controller, ~microphone, ~mouse (mouse_computer), +console, +disc, +headset, +keyboard (keyboard_computer), +memory card, +monitor (monitor_screen), +webcam, !mousepad


## Тема: home

### BABY THINGS  `baby_things`
- правило: Things used to care for a baby
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- ~blanket, ~monitor (monitor_medical), ~swing, ~wipes, +bib, +bottle, +car seat, +cradle, +crib, +diaper, +formula, +onesie, +pacifier, +rattle (rattle_toy), +stroller, !highchair, !playpen, !teether

### BATHROOM ITEMS  `bathroom_items`
- правило: Objects normally found in a home bathroom
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- ~cabinet (cabinet_furniture), ~curtain, ~floss, ~hairdryer, ~lotion, ~mat, ~mirror, ~plunger, ~razor, ~scale, ~tissue (tissue_paper), ~toothbrush, +bathtub, +brush, +comb, +faucet, +robe, +shampoo, +shower, +sink (sink_basin), +soap, +sponge (sponge_cleaning), +toilet, +toothpaste, +towel

### BEDROOM THINGS  `bedroom_things`
- правило: Objects normally found in a bedroom
- тип связи: `found_in`, базовая сложность 0.2
- слов: 21
- ~alarm clock, ~chest (chest_box), ~curtain, ~hamper, ~lamp, ~mirror, ~rug, ~slipper, +bed, +blanket, +closet, +comforter, +dresser, +hanger, +mattress, +nightstand, +pajamas, +pillow, +quilt, +sheet (sheet_bed), !key (key_lock)

### CLEANING SUPPLIES  `cleaning_supplies`
- правило: Tools and products used to clean a house
- тип связи: `used_in`, базовая сложность 0.2
- слов: 20
- ~brush, ~bucket, ~dustpan, ~gloves, ~polish (polish_product), ~wipes, +bleach, +broom, +cleanser, +detergent, +disinfectant, +duster, +mop, +rag, +soap, +sponge (sponge_cleaning), +trash bag, +vacuum, !scrubber, !squeegee

### DISHES  `dishes_and_glassware`
- правило: Things you eat and drink from at a table
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~pitcher (pitcher_jug), +bottle, +bowl, +cereal bowl, +cup, +dish, +glass, +goblet, +gravy boat, +jar, +mug, +plate, +platter, +saucer, +sugar bowl, +teapot, +tray, +tumbler, !carafe, !ramekin

### HOME TEXTILES  `fabrics_at_home`
- правило: Cloth things used around the house
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- ~apron (apron_garment), ~doormat, ~pillowcase, ~rug, ~throw, ~towel, +blanket, +comforter, +curtain, +cushion cover, +drape, +napkin, +quilt, +sheet (sheet_bed), +tablecloth, !dishcloth, !placemat

### FURNITURE  `furniture`
- правило: Movable household furniture
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- ~bed, ~bookshelf, ~cabinet (cabinet_furniture), ~crib, ~hutch, ~vanity, +armchair, +bench (bench_seat), +chair, +cot, +couch, +desk, +dresser, +futon, +headboard, +nightstand, +ottoman, +recliner, +rocker, +sideboard, +sofa, +stool, +table, +wardrobe, !loveseat

### HOUSE ROOMS  `home_rooms`
- правило: Rooms and spaces inside an ordinary house
- тип связи: `part_of`, базовая сложность 0.15
- слов: 20
- ~bathroom, ~cellar, ~closet, ~foyer, ~garage, ~nursery, ~porch, ~study, +attic, +basement, +bedroom, +den, +dining room, +hallway, +kitchen, +laundry room, +living room, +loft, +pantry, !sunroom

### KITCHEN APPLIANCES  `kitchen_appliances`
- правило: Electric machines used in a kitchen
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~freezer, ~grill, ~hood (hood_kitchen), ~kettle, +air fryer, +blender, +can opener, +coffee maker, +dishwasher, +food processor, +juicer, +microwave, +mixer, +oven, +range (range_stove), +refrigerator, +slow cooker, +toaster, +waffle iron, +warmer

### KITCHEN TOOLS  `kitchen_tools`
- правило: Handheld tools and utensils used to prepare food in a kitchen
- тип связи: `used_in`, базовая сложность 0.15
- слов: 26
- ~colander, ~knife, ~opener, ~peeler, ~thermometer, ~timer, +blender, +corkscrew, +cutting board, +fork, +grater, +ladle, +measuring cup, +mixer, +pan, +plate (plate_dish), +pot, +rolling pin, +sieve, +skillet, +spatula, +spoon, +strainer, +tongs, +whisk, !masher

### LAUNDRY THINGS  `laundry_things`
- правило: Things used to wash and dry clothes
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~bleach, ~iron (iron_appliance), ~line (line_cord), +basket, +detergent, +dryer, +dryer sheet, +hamper, +hanger, +ironing board, +lint trap, +softener, +stain remover, +starch, +washer, !clothespin

### LIGHTING  `lighting`
- правило: Devices that light a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~shade, +bulb, +candle, +ceiling fan, +chandelier, +dimmer, +fixture, +flashlight, +lamp, +lantern, +spotlight, +string lights, +track light, !floodlight, !nightlight, !sconce

### LIVING ROOM  `living_room_things`
- правило: Objects normally found in a living room
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~blanket, ~bookshelf, ~clock, ~console, ~curtain, ~fireplace, ~lamp, ~magazine, ~painting, ~plant (plant_growth), ~remote (remote_device), ~rug, ~speaker, ~television, ~vase, +armchair, +coffee table, +cushion, +ottoman, +sofa

### HOUSE PARTS  `parts_of_a_house`
- правило: Structural parts of a house
- тип связи: `part_of`, базовая сложность 0.2
- слов: 20
- ~beam (beam_wood), ~column, ~deck, ~gutter, ~shutter, ~window, +ceiling, +chimney, +door, +floor, +foundation (foundation_building), +porch, +railing, +roof, +shingle, +siding, +stairs, +threshold, +wall, !doorframe

### PET SUPPLIES  `pet_supplies`
- правило: Things bought to keep a pet at home
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~aquarium, ~bed, ~bowl, ~brush, ~cage, ~carrier, ~food, ~harness, ~litter, ~tag (tag_label), ~tank (tank_container), +collar, +kennel, +leash, +muzzle, +scratching post, +toy, +treat

### HOME REPAIR  `sewing_and_repair`
- правило: Small supplies used for fixing things around the house
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~bolt, ~bracket, ~glue, ~hammer, ~hinge, ~level, ~nail (nail_metal), ~patch, ~plunger, ~putty, ~sandpaper, ~tape, ~washer, ~wire, ~wrench, +screw, +sealant, !caulk

### SILVERWARE  `silverware`
- правило: Eating utensils laid out at a table setting
- тип связи: `is_a`, базовая сложность 0.2
- слов: 14
- ~knife, +butter knife, +carving knife, +chopsticks, +fork, +ladle, +salad fork, +serving spoon, +skewer, +soup spoon, +spoon, +teaspoon, +tongs, !spork

### CONTAINERS  `storage_containers`
- правило: Things made to store or carry other things
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~bin, ~bucket, ~drawer, ~envelope, ~folder, ~jar, ~pouch, ~tin (tin_can), ~trunk (trunk_case), +bag, +barrel, +basket, +box, +canister, +carton, +case (case_box), +chest (chest_box), +cooler, +crate, +sack (sack_bag)

### GARAGE THINGS  `things_in_a_garage`
- правило: Things stored in an ordinary home garage
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~bike, ~broom, ~car, ~cooler, ~hose, ~jack (jack_tool), ~ladder, ~oil (oil_motor), ~paint, ~shelf (shelf_furniture), ~shovel, ~sled, ~tire, ~toolbox, ~wheelbarrow, +extension cord, +gas can, +lawnmower, +rake, +workbench

### JUNK DRAWER  `things_in_a_junk_drawer`
- правило: Small odds and ends that pile up in a kitchen drawer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~coin, ~glue, ~magnet, ~paper clip, ~pen (pen_writing), ~receipt, ~scissors, ~screw, ~tape, !battery, !chapstick, !flashlight, !key, !matches, !rubber band, !string, !takeout menu, !twist tie

### WALL THINGS  `things_on_a_wall`
- правило: Things hung or mounted on an interior wall
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~antlers, ~clock, ~hook (hook_fastener), ~mirror, ~outlet, ~painting, ~plaque, ~shelf (shelf_furniture), ~switch, ~tapestry, ~television, ~trophy, ~whiteboard, +art, +calendar, +photo, +poster, +thermostat, +wallpaper, !sconce

### WATER HOLDERS  `things_that_hold_water`
- правило: Containers and objects built to hold water
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~aquarium, ~barrel, ~basin, ~bathtub, ~bottle, ~bucket, ~canteen, ~cup, ~glass, ~jug, ~kettle, ~pool, ~pot, ~sink (sink_basin), ~tank (tank_container), ~trough, ~vase, !watering can

### OPENING THINGS  `things_that_open`
- правило: Everyday objects that open and close
- тип связи: `has_property`, базовая сложность 0.35
- слов: 20
- ~box, ~cabinet (cabinet_furniture), ~curtain, ~door, ~drawer, ~envelope, ~fan (fan_hand), ~fridge, ~gate (gate_barrier), ~jar, ~lid, ~mailbox, ~suitcase, ~window, ~zipper, !book, !laptop, !shell, !umbrella, !wallet

### PLUGGED IN  `things_that_plug_in`
- правило: Household devices powered by plugging into an outlet
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~blender, ~computer, ~fan (fan_device), ~freezer, ~hairdryer, ~heater, ~iron (iron_appliance), ~kettle, ~lamp, ~lampshade, ~microwave, ~radio, ~speaker, ~television, ~toaster, !Charger, !clock, !drill (drill_tool), !printer, !vacuum

### THINGS WITH BUTTONS  `things_with_buttons`
- правило: Everyday objects operated by pressing buttons
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~blender, ~calculator, ~dishwasher, ~doorbell, ~keyboard (keyboard_computer), ~microwave, ~phone, ~printer, ~radio, ~remote (remote_device), ~watch (watch_object), !alarm clock, !camera, !cash register, !elevator, !game controller, !thermostat, !vending machine

### TRASH THINGS  `trash_and_recycling`
- правило: Things related to household garbage and recycling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~bottle, ~cardboard, ~newspaper, +bag, +bin, +can, +compost, +disposal, +dumpster, +junk, +landfill, +lid, +recycle, +scrap, +wrapper, !wastebasket


## Тема: jargon

### ACCOUNTING WORDS  `accounting_words`
- правило: Words used in bookkeeping and accounting
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~asset, ~credit, ~debit, ~expense, ~invoice, ~ledger, ~liability, ~receipt, ~revenue, ~statement, !audit, !balance, !depreciation, !payroll

### ARCHITECTURE WORDS  `architecture_words`
- правило: Words used to describe buildings and their design
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~balcony (balcony_house), ~column, ~vault, +arch (arch_structure), +atrium, +blueprint, +buttress, +cornice, +dome, +facade, +foundation (foundation_building), +gable, +mezzanine, +portico, +spire, +terrace

### AVIATION WORDS  `aviation_words`
- правило: Words used by pilots and air crew
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~cruise, ~runway, ~stall (stall_engine), ~taxi, ~tower, +altitude, +autopilot, +cockpit, +flaps, +hangar, +landing gear, +radar, +rudder, +throttle, +turbulence, +wingspan, +yaw, !callsign

### FORENSICS WORDS  `detective_procedures`
- правило: Words used in forensic investigation
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~cast (cast_mold), ~dna, ~lab, ~sample, !autopsy, !ballistics, !dusting, !evidence bag, !fingerprint, !spatter, !swab, !tape, !toxicology, !trace

### FRENCH COOKING  `french_cooking_terms`
- правило: French words used in professional cooking
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- !au gratin, !blanch, !bouquet garni, !braise, !consomme, !deglaze, !julienne, !mise en place, !puree, !roux, !saute, !souffle, xchiffonade, xflambe

### KITCHEN SLANG  `kitchen_brigade`
- правило: Terms used in a restaurant kitchen
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~station (station_kitchen), !comp, !expo, !fire, !garnish, !line (line_kitchen), !mise, !order up, !pass, !plating, !prep, !sous vide, !ticket (ticket_order), !walk in

### COURT TERMS  `legal_terms`
- правило: Terms used in legal proceedings
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~appeal, ~hearing, ~objection, ~plea, ~recess, ~settlement, ~testimony, ~verdict, !acquittal, !arraignment, !deposition, !indictment, !injunction, !motion

### MEDICAL PROCEDURES  `medical_procedures`
- правило: Procedures performed by doctors
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~anesthesia, ~cast (cast_medical), ~dialysis, ~scan, ~X-ray, +biopsy, +checkup, +injection, +screening, +stitches, +surgery, +therapy, +transfusion, +transplant, +ultrasound, +vaccination

### TEMPO TERMS  `music_tempo_terms`
- правило: Italian words used to mark tempo in music
- тип связи: `is_a`, базовая сложность 0.45
- слов: 16
- !accelerando, !adagio, !allegro, !andante, !crescendo, !forte, !grave, !largo, !legato, !lento, !moderato, !piano, !presto, !staccato, !vivace, xritardando

### SHIP CREW  `nautical_ranks`
- правило: Roles in the crew of a ship
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~captain, ~lookout, ~navigator, ~steward, !boatswain, !cook (cook_person), !deckhand, !engineer, !first mate, !helmsman, !purser, !quartermaster

### CAMERA SETTINGS  `photography_terms`
- правило: Settings and controls on a camera
- тип связи: `found_in`, базовая сложность 0.45
- слов: 13
- ~exposure, ~flash, ~focus (focus_lens), ~Zoom, !aperture, !depth of field, !iso, !metering, !shutter speed, !timer, !tripod mount, !viewfinder, !white balance

### TYPOGRAPHY WORDS  `printing_and_type`
- правило: Words used to describe printed type
- тип связи: `found_in`, базовая сложность 0.5
- слов: 14
- ~bold (bold_type), ~font, ~italic, ~serif, ~typeface, ~underline, !caps, !column, !justify, !kerning, !leading, !lowercase, !margin, !point size

### SAILING TERMS  `sailing_terms`
- правило: Terms used when sailing a boat
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~draft (draft_boat), ~sheet (sheet_sail), !boom, !capsize, !cleat, !halyard, !heel, !jibe, !leeward, !luff, !mooring, !spinnaker, !tack (tack_sail), !windward

### STAGE TERMS  `theater_stage_terms`
- правило: Terms used backstage in a theater
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~catwalk, ~cue, ~flat, ~gel, ~strike (strike_theater), ~wings, +blocking, +call time, +dimmer, +dress rehearsal, +green room, +prop table, +set piece, !apron (apron_stage)

### FORECAST TERMS  `weather_forecast_terms`
- правило: Terms used in a weather forecast
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~forecast, ~front, ~high, ~low, ~precipitation, ~pressure, ~warning, +advisory, +chance of rain, +dew point, +heat index, +visibility, +wind chill, !watch (watch_warning)


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


## Тема: lists

### BIBLE BOOKS  `bible_books`
- правило: Books of the Bible
- тип связи: `is_a`, базовая сложность 0.45
- слов: 24
- ~John, ~Kings, ~mark, ~Matthew, ~Numbers, +Acts, +Corinthians, +Daniel, +Deuteronomy, +Ecclesiastes, +Exodus, +Genesis, +Isaiah, +Jeremiah, +Jonah, +Joshua, +Judges, +Leviticus, +Luke, +Proverbs, +Psalms, +Revelation, +Romans, +Ruth

### WATER FEATURES  `body_of_water_types`
- правило: Kinds of water feature made by people
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~aqueduct, +canal, +cistern, +dam, +drain, +fountain, +moat, +pond, +pool, +reservoir, +sprinkler, +waterway, +well, !birdbath

### MORE BREEDS  `dog_breeds_more`
- правило: Dog breeds beyond the most common ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- +bloodhound, +chow chow, +dalmatian, +newfoundland, +papillon, +pointer, +pomeranian, +setter, +shih tzu, !akita, !basenji, !bichon, !borzoi, !malamute, !saluki, !samoyed, !schnauzer, !vizsla, !weimaraner, !whippet

### MORE ELEMENTS  `elements_more`
- правило: Chemical elements beyond the most familiar ones
- тип связи: `is_a`, базовая сложность 0.45
- слов: 22
- ~aluminum, ~arsenic, ~iodine, ~nickel, +beryllium, +boron, +chromium, +cobalt, +fluorine, +krypton, +lithium, +manganese, +phosphorus, +platinum, +plutonium, +radium, +radon, +silicon, +silver, +titanium, +xenon, !bromine

### MORE FLOWERS  `flowers_more`
- правило: Flowers beyond the most common garden ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- +anemone, +aster, +camellia, +chrysanthemum, +narcissus, +pansy, +snapdragon, +sweet pea, +wisteria, +yarrow, !amaryllis, !cornflower, !delphinium, !foxglove, !freesia, !gardenia, !gladiolus, !larkspur, !lupine, !ranunculus

### GEM CUTS  `gem_cuts`
- правило: Words used to describe cut and set gemstones
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~brilliant, ~facet, ~polish (polish_verb), !band (band_ring), !bezel, !cabochon, !carat, !clarity, !cut, !emerald cut, !princess cut, !prong, !setting, !Solitaire

### MORE TREES  `trees_more`
- правило: Trees beyond the most common ones
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~locust, ~sequoia, +alder, +banyan, +cottonwood, +eucalyptus, +hawthorn, +hemlock, +larch, +linden, +mulberry, +olive, +persimmon, +sycamore, !baobab, !catalpa, !ginkgo, !pawpaw, !sumac, !tamarack

### MORE STATES  `us_states_more`
- правило: States of the United States not in the shorter list
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~Massachusetts, ~Mississippi, ~New Hampshire, ~Oklahoma, ~Wisconsin, +Arkansas, +Connecticut, +Illinois, +Kansas, +Kentucky, +Louisiana, +Maryland, +Minnesota, +Missouri, +Nevada, +New Mexico, +North Dakota, +Oregon, +Pennsylvania, +Rhode Island, +South Dakota, +Tennessee, +Utah, +Washington, +West Virginia

### ALPHABET AND SYMBOLS  `vitamins_letters`
- правило: Symbols and marks used in writing and math
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~arrow, ~bullet, ~degree (degree_angle), ~minus, ~percent, ~pipe (pipe_symbol), +asterisk, +at sign, +dollar sign, +equals, +hashtag, +plus, !ampersand, !backslash, !caret, !tilde

### WEATHER INSTRUMENTS  `weather_instruments`
- правило: Instruments used to measure the weather
- тип связи: `used_in`, базовая сложность 0.45
- слов: 12
- ~barometer, ~radar, ~satellite, ~thermometer, +rain gauge, +weather balloon, +weather vane, !anemometer, !hygrometer, !seismograph, !sundial, !windsock


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


## Тема: medicine

### BODY FLUIDS  `body_fluids`
- правило: Fluids produced by the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~bile, ~mucus, ~plasma, ~serum, ~sputum, ~sweat, !blood, !lymph, !milk, !saliva, !tear, !urine

### DENTAL WORDS  `dental_words`
- правило: Words used at a dental office
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~bridge (bridge_dental), ~crown (crown_dental), ~tartar, +braces, +canine, +cavity, +denture, +enamel, +extraction, +filling, +floss, +gum (gum_mouth), +molar, +plaque, +retainer, +root canal, +whitening, !incisor

### DISEASES  `diseases`
- правило: Diseases an average person can name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~arthritis, ~pneumonia, +anemia, +asthma, +bronchitis, +cancer, +cholera, +diabetes, +flu, +hepatitis, +malaria, +measles, +mumps, +polio, +rabies, +shingles, +tetanus, +tuberculosis, +typhoid, !chickenpox

### EMERGENCY WORDS  `emergency_words`
- правило: Words used during a medical emergency
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~code, ~CPR, ~oxygen, ~rescue, ~response, +ambulance, +defibrillator, +dispatcher, +evacuation, +hotline, +paramedic, +siren, +stretcher, +trauma, +triage

### FIRST AID  `first_aid`
- правило: Things kept in a first aid kit
- тип связи: `used_in`, базовая сложность 0.25
- слов: 17
- ~aspirin, ~gloves, ~scissors, ~tape, ~thermometer, ~tweezers, ~wipe, +antiseptic, +bandage, +burn cream, +cotton ball, +eye wash, +gauze, +ice pack, +ointment, +sling, +splint

### HOSPITAL DEPARTMENTS  `hospital_departments`
- правило: Departments and units inside a hospital
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~dialysis, ~laboratory, ~physical therapy, ~surgery, +admissions, +cardiology, +emergency, +intensive care, +maternity, +morgue, +oncology, +pediatrics, +pharmacy, +radiology, +recovery

### HYGIENE THINGS  `hygiene`
- правило: Things used to keep the body clean
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~comb, ~floss, ~lotion, ~mouthwash, ~razor, ~sanitizer, ~tissue (tissue_paper), ~washcloth, +cotton swab, +deodorant, +nail clipper, +shampoo, +soap, +toothbrush, +toothpaste, +towel

### INJURIES  `injuries`
- правило: Kinds of physical injury
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~bite (bite_wound), ~break, ~frostbite, ~strain, +blister, +bruise, +burn, +concussion, +cut, +dislocation, +fracture, +laceration, +puncture, +scrape, +splinter, +sprain, +sunburn, +whiplash

### MEDICAL SPECIALTIES  `medical_specialties`
- правило: Branches of medical practice
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~anesthesia, +cardiology, +dermatology, +immunology, +neurology, +obstetrics, +oncology, +pathology, +pediatrics, +psychiatry, +radiology, +surgery, +urology, !geriatrics, !orthopedics

### MEDICAL TOOLS  `medical_tools`
- правило: Instruments a doctor or nurse uses
- тип связи: `used_in`, базовая сложность 0.3
- слов: 20
- ~clamp, ~forceps, ~gauze, ~monitor (monitor_medical), ~needle (needle_medical), ~scalpel, ~stethoscope, ~thermometer, ~tweezers, +catheter, +defibrillator, +gurney, +IV, +sling, +splint, +syringe, +tourniquet, +ventilator, !speculum, xotoscope

### FORMS OF MEDICINE  `medicine_forms`
- правило: Forms in which medicine is taken
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~cream (cream_ointment), ~drop, ~injection, ~patch, ~powder, ~spray, ~syrup, +capsule, +gel, +inhaler, +ointment, +pill, +tablet, !lozenge, !suppository

### NUTRITION WORDS  `nutrition_words`
- правило: Words used to talk about diet and nutrition
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~mineral, ~nutrient, ~sodium, ~sugar, +calorie, +carbohydrate, +cholesterol, +diet, +fat, +fiber, +organic, +portion, +protein, +serving, +vitamin, +whole grain

### BIRTH WORDS  `pregnancy_words`
- правило: Words used about pregnancy and childbirth
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~midwife, ~twins, +cradle, +crib, +delivery, +due date, +formula, +incubator, +labor, +newborn, +nursery, +obstetrician, +stroller, +trimester, +ultrasound

### SLEEP WORDS  `sleep_and_rest`
- правило: Words about sleep and its problems
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~alarm, +apnea, +bedtime, +doze, +dream, +drowsy, +insomnia, +mattress, +nap, +nightmare, +pillow, +rest (rest_sleep), +snore, !jetlag, !sleepwalk

### THERAPY WORDS  `therapy_words`
- правило: Words used in physical and mental therapy
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~appointment, ~brace, ~counselor, ~crutch, ~exercise, ~massage, ~progress, ~recovery, ~rehab, ~session, ~stretch, ~treatment, ~walker, !goal

### VISION WORDS  `vision_words`
- правило: Words used about eyesight and glasses
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~cornea, ~frame, ~prescription, ~pupil, +blind, +contacts, +eye chart, +glasses, +lens, +optometrist, +squint, !astigmatism, !bifocal, !farsighted, !nearsighted

### VITAMINS AND MINERALS  `vitamins_and_minerals`
- правило: Nutrients the body needs in small amounts
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~calcium, ~iron (iron_metal), ~magnesium, ~zinc, +biotin, +folate, +iodine, +niacin, +potassium, +selenium, +sodium, +vitamin C, +vitamin D, !riboflavin, !thiamine


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
- ~apple, ~beanstalk, ~cottage, ~harp, ~porridge, ~tower, +gingerbread house, +glass slipper, +golden egg, +magic mirror, +pumpkin coach, +red hood, +spinning wheel, !breadcrumb

### FORTUNE TELLING  `fortune_telling`
- правило: Things used to tell fortunes
- тип связи: `used_in`, базовая сложность 0.4
- слов: 13
- ~cards, ~crystal ball, ~dice (dice_game), ~horoscope, ~omen, ~Oracle, ~stars, ~tarot, !dream, !palm, !pendulum, !rune, !tea leaves

### GREEK GODS  `greek_gods`
- правило: Gods and goddesses of Greek mythology
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Apollo, ~Persephone, ~Poseidon, +Aphrodite, +Ares, +Artemis, +Athena, +Dionysus, +Hades, +Hera, +Hermes, +Zeus, !Demeter, !Hephaestus, !Hestia

### MYTHOLOGICAL HEROES  `greek_heroes`
- правило: Heroes of classical mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Paris, +Achilles, +Aeneas, +Ajax, +Atalanta, +Hector, +Hercules, +Jason, +Odysseus, +Orpheus, +Perseus, +Theseus

### LEGENDARY PLACES  `legendary_places`
- правило: Places known only from myth and legend
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~Hades, ~Olympus, +Asgard, +Atlantis, +Avalon, +Camelot, +Eden, +El Dorado, +Shangri-La, +Troy, +Valhalla, +Xanadu

### MAGICAL BEINGS  `magic_creatures`
- правило: Magical beings from folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~banshee, ~brownie, ~dwarf, ~genie, ~troll, +elf, +fairy, +gnome, +goblin, +imp, +leprechaun, +nymph, +pixie, +Sprite, +witch, +wizard

### MAGIC OBJECTS  `magic_objects`
- правило: Objects with magical powers in stories
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~broomstick, ~charm, ~lamp, ~mirror, ~ring, ~sword, +amulet, +cauldron, +cloak, +crystal ball, +elixir, +magic carpet, +potion, +talisman, +wand, !spellbook

### SCARY CREATURES  `monsters`
- правило: Frightening creatures from stories and folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~banshee, ~mummy, ~poltergeist, ~witch, +bogeyman, +demon, +ghost, +ghoul, +goblin, +gremlin, +monster, +phantom, +vampire, +werewolf, +zombie

### MYTHICAL MONSTERS  `mythical_monsters`
- правило: Monsters from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~banshee, ~kraken, ~minotaur, ~siren, ~sphinx, +cerberus, +chimera, +cyclops, +gorgon, +harpy, +hydra, +medusa, !basilisk, !manticore

### NORSE GODS  `norse_gods`
- правило: Gods of Norse mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Thor, +Freya, +Hel, +Loki, +Odin, +Tyr, !Balder, !Frigg, !Heimdall, !Njord, !Vidar, xIdun

### ROMAN GODS  `roman_gods`
- правило: Gods and goddesses of Roman mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Apollo, ~Diana, +Bacchus, +Ceres, +Juno, +Jupiter, +Mars, +mercury (mercury_god), +Minerva, +Neptune, +Pluto, +Saturn, +Venus, +Vulcan

### SUPERSTITION THINGS  `superstitions`
- правило: Objects tied to common superstitions
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~black cat, ~broken mirror, ~horseshoe, !cross, !four leaf clover, !knock on wood, !ladder, !mirror, !penny, !rabbit foot, !salt, !umbrella, !wishbone

### WIZARD WORDS  `wizards_and_spells`
- правило: Things belonging to a wizard in stories
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~book, ~cauldron, ~crystal, ~familiar, ~hat, ~robe, ~scroll (scroll_paper), ~staff, ~tower, +apprentice, +incantation, +potion, +spell (spell_magic), +wand

### ZODIAC SIGNS  `zodiac_signs`
- правило: Signs of the astrological zodiac
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~cancer, +Aquarius, +Aries, +Capricorn, +Gemini, +Leo, +Libra, +Pisces, +Sagittarius, +Scorpio, +Taurus, +Virgo


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


## Тема: names_world

### FRENCH NAMES  `french_names`
- правило: First names common in France
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Louis, +Amelie, +Antoine, +Camille, +Celine, +Chloe, +Claire, +Henri, +Jean, +Juliette, +Marie, +Michel, +Nicolas, +Philippe, +Pierre, +Sophie

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
- ~Archer, ~baker, ~carpenter, ~cooper, ~farmer, ~Hunter, ~mason, ~shepherd, ~Smith, +Brewer, +chandler, +Fisher, +miller, +potter, +Sawyer, +Taylor, +Turner, +weaver

### RUSSIAN NAMES  `russian_names`
- правило: First names common in Russia
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Alexei, +Anastasia, +Boris, +Dmitri, +Irina, +Ivan, +Katya, +Mikhail, +Natasha, +Nikolai, +Olga, +Sergei, +Svetlana, +Tatiana, +Vladimir

### SCANDINAVIAN NAMES  `scandinavian_names`
- правило: First names common in Scandinavia
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~Thor, +Astrid, +Bjorn, +Elsa, +Erik, +Ingrid, +Lars, +Magnus, +Nils, +Odin, +Sven, !Freja, !Linnea, !Sigrid, !Solveig

### SPANISH NAMES  `spanish_names`
- правило: First names common in Spanish speaking countries
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +Ana, +Antonio, +Carlos, +Carmen, +Diego, +Elena, +Isabel, +Javier, +Jose, +Lucia, +Luis, +Manuel, +Maria, +Miguel, +Pablo, +Pilar, +Ricardo, +Rosa, +Sofia, +Teresa

### UNISEX NAMES  `unisex_names`
- правило: First names given to both boys and girls
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- ~Charlie, ~Sam, +Alex, +Avery, +Bailey, +Casey, +Dakota, +Jamie, +Jordan, +Morgan, +Quinn, +Reese, +Riley, +Rowan, +Skyler, +Taylor


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


## Тема: nature_species

### BEETLES  `beetles`
- правило: Kinds of beetle
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~firefly, ~ladybug, ~scarab, !boll weevil, !carpet beetle, !click beetle, !dung beetle, !june bug, !rhinoceros beetle, !stag beetle, !water beetle, !weevil

### GARDEN BUGS  `garden_bugs`
- правило: Small creatures found in a garden
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~aphid, ~bee, ~earthworm, ~earwig, ~snail, ~spider, +ant, +beetle, +caterpillar, +centipede, +cricket, +grub, +ladybug, +praying mantis, +slug, !roly poly

### MOSS & LICHEN  `mosses_and_lichens`
- правило: Small plants that grow on rocks and bark
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- ~algae, ~fungus, ~moss, !lichen, !reindeer moss, !sphagnum, xcrustose, xfoliose, xhornwort, xliverwort

### CONIFER WORDS  `pine_and_cones`
- правило: Words about pine trees and their cones
- тип связи: `found_in`, базовая сложность 0.5
- слов: 14
- ~bark, ~cone, ~evergreen, ~fir, ~needle (needle_pine), ~resin, ~sap, ~seed, ~timber, !bough, !cluster, !pitch, !scent, !spruce

### SALTWATER FISH  `saltwater_fish`
- правило: Fish that live in salt water
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +bonito, +cod, +grouper, +mackerel, +sea bass, +snapper, +sole (sole_fish), +tuna, +wahoo, !amberjack, !bluefish, !hake, !mahi mahi, !pompano, !tarpon

### WILDFLOWERS  `wildflowers`
- правило: Flowers that grow wild in fields and roadsides
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +aster, +black eyed susan, +columbine, +indian paintbrush, +primrose, +wild rose, !bloodroot, !bluebonnet, !chicory, !coneflower, !goldenrod, !milkweed, !queen annes lace, !trillium


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


## Тема: people

### FAMOUS PAINTERS  `artists`
- правило: Famous painters from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +Da Vinci, +Dali, +Degas, +Matisse, +Michelangelo, +Monet, +Picasso, +Pollock, +Rembrandt, +Renoir, +Van Gogh, +Vermeer, +Warhol, !Cezanne

### FAMOUS AUTHORS  `authors`
- правило: Famous authors from literature
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Poe, ~Shakespeare, ~Tolkien, +Austen, +Bronte, +Dickens, +Fitzgerald, +Hemingway, +Kipling, +Melville, +Orwell, +Steinbeck, +Twain, +Verne, +Wilde

### BODY LANGUAGE  `body_language`
- правило: Gestures people make with the body to communicate
- тип связи: `does_action`, базовая сложность 0.4
- слов: 15
- ~bow (bow_bend), ~clap, ~handshake, ~point (point_gesture), ~salute, ~wave (wave_hand), !cross arms, !curtsy, !fist bump, !high five, !hug, !nod, !shake head, !shrug, !thumbs up

### BOYS NAMES  `boys_names`
- правило: Common first names given to boys in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~jack (jack_name), ~Jacob, ~mason, ~Matthew, ~Noah, +Andrew, +Benjamin, +Christopher, +Daniel, +David, +Ethan, +Henry, +James, +John, +Joseph, +Liam, +Lucas, +Michael, +Nathan, +Owen, +Robert, +Ryan, +Samuel, +Thomas, +William

### AUDIENCE WORDS  `crowd_words`
- правило: Words for people watching an event
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~audience, ~crowd, ~spectator, ~viewer, !attendee, !bystander, !fan (fan_person), !guest, !listener, !onlooker, !patron, !subscriber, !witness

### EXPLORERS  `explorers`
- правило: Famous explorers from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~cook (cook_explorer), +Balboa, +Cabot, +Clark, +Columbus, +Cortes, +Hudson, +Lewis, +Livingstone, +Magellan, +Marco Polo, +Shackleton, !Amundsen, !Vespucci

### FACIAL EXPRESSIONS  `facial_expressions`
- правило: Expressions people make with their face
- тип связи: `does_action`, базовая сложность 0.35
- слов: 15
- ~blush, ~glare, ~yawn, +beam (beam_smile), +blink, +frown, +gape, +grimace, +grin, +pout, +scowl, +smile, +smirk, +sneer, +wink

### FAMILY MEMBERS  `family_members`
- правило: Words for members of a family
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- ~child, ~grandchild, ~stepfather, +aunt, +brother, +cousin, +daughter, +father, +godmother, +grandfather, +grandmother, +husband, +in law, +mother, +nephew, +niece, +parent, +sibling, +sister, +son, +spouse, +stepmother, +twin, +uncle, +wife

### FAMOUS AMERICANS  `famous_americans`
- правило: Americans widely known from history
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~Disney, ~Edison, ~ford (ford_person), ~Kennedy, ~Lincoln, +Armstrong, +Carver, +Douglass, +Earhart, +Franklin, +Jefferson, +Keller, +Parks, +Roosevelt, +Tubman, +Twain, +Washington, +Wright

### FEELINGS  `feelings`
- правило: Words naming human emotions
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~bored, ~calm (calm_person), ~confused, ~curious, ~embarrassed, ~guilty, ~jealous, ~tired, +angry, +anxious, +content, +excited, +frustrated, +grateful, +happy, +hopeful, +joyful, +lonely, +nervous, +proud, +relieved, +sad, +scared, +surprised, +worried

### GIRLS NAMES  `girls_names`
- правило: Common first names given to girls in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~Elizabeth, ~Grace, ~Lily, ~Mary, +Abigail, +Amelia, +Ava, +Charlotte, +Chloe, +Ella, +Emily, +Emma, +Hannah, +Isabella, +Jennifer, +Linda, +Madison, +Mia, +Natalie, +Olivia, +Rachel, +Sarah, +Sophia, +Susan, +Zoe

### GROUPS OF PEOPLE  `groups_of_people`
- правило: Words for gatherings of people
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~cast (cast_people), ~choir, ~crew, ~jury, ~party (party_group), +audience, +band (band_group), +class, +committee, +congregation, +council, +crowd, +gang, +mob, +panel, +squad, +staff, +team, +tribe, +troop

### INVENTORS  `inventors`
- правило: Famous inventors
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~bell, ~diesel, ~ford (ford_person), ~Watt, +Edison, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Tesla, +Whitney, +Wright, !Daguerre

### STAGES OF LIFE  `life_stages`
- правило: Words for the stages of a human life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~grownup, ~retiree, +adolescent, +adult, +baby, +child, +elder (elder_person), +infant, +middle age, +newborn, +senior, +teenager, +toddler, +youth, !preschooler

### NATIONALITIES  `nationalities`
- правило: Words for people from a particular country
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~Australian, ~Canadian, ~polish (polish_language), +American, +Brazilian, +Chinese, +Dutch, +Egyptian, +French, +German, +greek, +Indian, +Irish, +Italian, +Japanese, +Korean, +Mexican, +Russian, +spanish, +Swedish

### NICKNAMES  `nicknames`
- правило: Short familiar forms of common first names
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~Ben, ~bill (bill_name), ~Jim, ~Pat, ~Peg, ~Sam, +Andy, +bob, +Chris, +Dave, +Joe, +Kate, +Liz, +Meg, +Mike, +Nick, +Rick, +Sue, +Ted, +tom

### WEDDING PEOPLE  `people_at_a_wedding`
- правило: People with a role at a wedding
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~bride, ~groom (groom_wedding), ~guest, ~photographer, +best man, +bridesmaid, +caterer, +DJ, +father of the bride, +flower girl, +maid of honor, +ring bearer, +usher, !officiant

### STORY CHARACTERS  `people_in_a_story`
- правило: Character roles found in stories
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~guardian, ~hero, ~mentor, ~orphan, ~outlaw, ~rival, ~stranger, ~witness, +detective, +narrator, +protagonist, +sidekick, +victim, +villain

### PERSONALITY WORDS  `personality_words`
- правило: Words describing a person character
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bold (bold_brave), ~careful, ~cheerful, ~curious, ~funny, ~loyal, ~serious, ~stubborn, +brave, +calm (calm_person), +clever, +generous, +gentle, +honest, +patient, +quiet, +sensible, +shy

### RELATIONSHIP WORDS  `relationships`
- правило: Words for how people are connected to each other
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- ~boss, ~client, ~host (host_person), +acquaintance, +Ally, +classmate, +colleague, +coworker, +friend, +guest, +mentor, +neighbor, +partner, +rival, +roommate, +stranger, +teammate

### FAMOUS SCIENTISTS  `scientists`
- правило: Famous scientists from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Darwin, +Archimedes, +Bohr, +Copernicus, +Curie, +Einstein, +Faraday, +Fleming, +Galileo, +Hawking, +Kepler, +Mendel, +Newton, +Pasteur

### TITLES  `titles_of_address`
- правило: Titles put before a person name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~captain, ~chief, ~coach, ~dean, ~doctor, ~judge, ~professor, ~reverend, ~senator, ~sergeant, +lady, +lord, +madam, +miss, +missus, +mister, +officer, +sir

### US PRESIDENTS  `us_presidents`
- правило: Presidents of the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~Grant, ~Kennedy, ~Wilson, +Adams, +Bush, +Carter, +Clinton, +Eisenhower, +Jackson, +Jefferson, +Johnson, +Lincoln, +Madison, +Monroe, +Nixon, +Obama, +Reagan, +Roosevelt, +Truman, +Washington


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


## Тема: plants

### CACTUS AND SUCCULENTS  `cactus_and_succulents`
- правило: Desert plants that store water in thick leaves or stems
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~aloe, ~cactus, !agave, !barrel cactus, !cholla, !echeveria, !hens and chicks, !jade, !prickly pear, !saguaro, !sedum, !yucca

### FARM CROPS  `crops`
- правило: Plants grown on farms for food or material
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~cotton, ~flax, ~hay, ~peanut, ~potato, ~sunflower, +alfalfa, +barley, +canola, +corn, +millet, +oat, +rice, +rye, +sorghum, +soybean, +sugarcane, +wheat

### EVERGREEN TREES  `evergreens`
- правило: Trees that keep their leaves or needles all year
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~laurel, ~sequoia, +cedar, +cypress, +fir, +hemlock, +holly, +juniper, +magnolia, +pine, +redwood, +spruce, +yew, !arborvitae

### FRUIT TREES  `fruit_trees`
- правило: Trees grown for their edible fruit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~almond, +apple, +apricot, +avocado, +banana, +cherry, +coconut, +fig, +lemon, +lime, +mango, +olive, +orange, +peach, +pear, +pecan, +plum, +walnut

### SPRING FLOWERS  `garden_flowers_spring`
- правило: Flowers that bloom in spring
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- +azalea, +bluebell, +cherry blossom, +daffodil, +hyacinth, +iris, +lilac, +magnolia, +pansy, +primrose, +tulip, !crocus, !forsythia, !snowdrop

### SUMMER FLOWERS  `garden_flowers_summer`
- правило: Flowers that bloom in summer
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~sunflower, +black eyed susan, +cosmos, +dahlia, +Daisy, +geranium, +lavender (lavender_plant), +Lily, +marigold, +rose, +snapdragon, !hydrangea, !petunia, !zinnia

### GARDENING WORDS  `gardening_words`
- правило: Words used when growing a garden
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bed, ~greenhouse, ~harvest, ~hose, ~prune, ~row, ~shade, ~sunlight, ~water, +compost, +fertilizer, +mulch, +pot, +seed, +soil, +sprout, +trellis, +weed

### GRASSES  `grasses`
- правило: Kinds of grass and grain plants
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bamboo, ~barley, ~corn, ~oat, ~reed, ~rice, ~rye, ~wheat, !Bermuda, !bluegrass, !crabgrass, !fescue, !ryegrass, !sugarcane

### COOKING HERBS  `herbs`
- правило: Leafy plants grown to flavor food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~bay, ~lavender (lavender_plant), +basil, +cilantro, +dill, +mint (mint_herb), +oregano, +parsley, +rosemary, +sage (sage_herb), +thyme, !chive, !lemongrass, !marjoram, !tarragon

### HOUSEPLANTS  `houseplants`
- правило: Plants commonly kept indoors in pots
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~jade, ~orchid, ~palm, ~succulent, ~Violet, +aloe, +bamboo, +cactus, +Fern, +geranium, +Ivy, +peace lily, +rubber plant, +snake plant, +spider plant, !begonia, !philodendron, !pothos

### LEAF WORDS  `leaf_shapes`
- правило: Words describing leaves and how they grow
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~bud, ~evergreen, ~foliage, ~needle (needle_pine), ~sprout, ~stalk, ~stem, !blade, !broadleaf, !canopy, !deciduous, !frond, !lobe, !vein

### MUSHROOM TYPES  `mushroom_types`
- правило: Kinds of edible and wild mushrooms
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- !button (button_mushroom), !chanterelle, !enoki, !morel, !oyster, !porcini, !portobello, !puffball, !shiitake, !toadstool, !truffle, xcremini

### PLANT PARTS  `plant_parts`
- правило: Parts of a growing plant
- тип связи: `part_of`, базовая сложность 0.25
- слов: 16
- ~bark, ~fruit, ~node, ~vine, +bud, +flower, +leaf, +petal, +pollen, +root, +seed, +sprout, +stalk, +stem, +thorn, !tendril

### POISONOUS PLANTS  `poisonous_plants`
- правило: Plants that are dangerous to touch or eat
- тип связи: `has_property`, базовая сложность 0.4
- слов: 12
- !castor bean, !foxglove, !hemlock, !holly berry, !mistletoe, !monkshood, !nightshade, !oleander, !poison ivy, !poison oak, !sumac, !yew

### SEEDS AND BULBS  `seeds_and_bulbs`
- правило: Plant parts you put in the ground to grow a new plant
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~acorn, ~bulb, ~clove, ~pit, ~seed, ~spore, +cutting, +kernel, +seedling, +sprout, +tuber, !corm, !rhizome, !sapling

### SHRUBS AND BUSHES  `shrubs`
- правило: Woody plants smaller than a tree
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~hedge, ~holly, ~juniper, ~lilac, ~rose, !azalea, !barberry, !boxwood, !forsythia, !hydrangea, !privet, !rhododendron, !spirea, !viburnum

### TROPICAL PLANTS  `tropical_plants`
- правило: Plants that grow in tropical climates
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~banana, ~cocoa, ~coffee, ~Fern, ~orchid, ~palm, ~papaya, +bamboo, +banyan, +hibiscus, +mangrove, +rubber tree, !bromeliad, !plumeria

### VINES AND CLIMBERS  `vines`
- правило: Plants that climb or trail along a surface
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bean, ~cucumber, ~grape, ~Ivy, ~pea, ~pumpkin, !clematis, !honeysuckle, !hops, !Jasmine, !kudzu, !morning glory, !passion flower, !wisteria

### WATER PLANTS  `water_plants`
- правило: Plants that grow in or on water
- тип связи: `found_in`, базовая сложность 0.35
- слов: 13
- ~papyrus, ~watercress, +algae, +kelp, +lily pad, +lotus, +moss, +reed, +seaweed, +water lily, !cattail, !duckweed, !eelgrass

### WEEDS  `weeds`
- правило: Unwanted plants that grow in lawns and gardens
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~poison ivy, +clover, +dandelion, +Ivy, +moss, +nettle, +plantain, +thistle, !bindweed, !chickweed, !crabgrass, !foxtail, !purslane, !ragweed


## Тема: properties

### BLACK THINGS  `black_things`
- правило: Everyday things that are typically black in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~asphalt, ~bat, ~chalkboard, ~coal, ~crow, ~ink, ~licorice, ~night, ~oil (oil_motor), ~olive, ~panther, ~pupil, ~raven, ~Shadow, ~soot, ~tire, ~tuxedo, !piano key

### COLD THINGS  `cold_things`
- правило: Things that are cold by their physical nature
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~chill, ~freezer, ~frost, ~glacier, ~hail, ~ice, ~ice cream, ~iceberg, ~icicle, ~Popsicle, ~refrigerator, ~sleet, ~slush, ~snow, ~snowball, !ice cube, !permafrost, !sorbet

### COLORS  `colors`
- правило: Basic color names used in everyday English
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~crimson, ~gold, ~lime, ~olive, ~orange (orange_color), ~silver, ~teal, +beige, +black, +blue, +Brown, +gray, +green (green_color), +indigo, +magenta, +maroon, +navy, +pink, +purple, +red, +tan, +turquoise, +Violet, +white (white_color), +yellow

### FAST THINGS  `fast_things`
- правило: Things known for moving very fast
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~bullet, ~cheetah, ~comet, ~hare, ~jet, ~lightning, ~motorcycle, ~race car, ~rocket, ~torpedo, !arrow, !falcon, !sprinter, !wind

### GREEN THINGS  `green_things`
- правило: Everyday things that are typically green in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~avocado, ~broccoli, ~cactus, ~clover, ~cucumber, ~emerald, ~Fern, ~frog, ~grass, ~kiwi, ~leaf, ~lettuce, ~lime, ~mint (mint_herb), ~moss, ~pea, ~pickle, ~shamrock, ~spinach, ~turtle

### HARD THINGS  `hard_things`
- правило: Things that feel hard and solid to the touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~bone, ~brick, ~concrete, ~diamond, ~glass, ~granite, ~ice, ~iron (iron_metal), ~marble (marble_stone), ~metal, ~nail (nail_metal), ~nut (nut_food), ~rock (rock_stone), ~shell, ~steel, ~tile, ~wood, !tooth

### HEAVY THINGS  `heavy_things`
- правило: Things that are hard to lift because of their weight
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~anchor, ~anvil, ~bathtub, ~boulder, ~cannon, ~elephant, ~engine, ~statue, ~truck, ~whale, !barbell, !cinderblock, !piano, !refrigerator, !safe, !tractor

### HOT THINGS  `hot_things`
- правило: Things that are hot by their physical nature
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~campfire, ~candle, ~coal, ~engine, ~fire, ~furnace, ~iron (iron_appliance), ~lava, ~magma, ~oven, ~radiator, ~sauna, ~steam, ~stove, ~sun, ~torch, !boiling water, !ember

### LIGHT THINGS  `light_things`
- правило: Things that weigh almost nothing
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~balloon, ~bubble, ~confetti, ~cotton, ~feather, ~foam, ~leaf, ~paper, ~petal, ~seed, ~tissue (tissue_paper), !dust, !hair, !snowflake, !straw (straw_hay), !thread

### THIN THINGS  `long_thin_things`
- правило: Everyday things that are long and thin
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~arrow, ~hair, ~needle (needle_sewing), ~noodle, ~pole, ~ribbon, ~rope, ~ruler, ~spaghetti, ~wire, ~worm, !cane, !chopstick, !pencil, !snake, !straw (straw_tube)

### LOUD THINGS  `loud_things`
- правило: Things that make a loud noise
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~alarm, ~bell, ~chainsaw, ~crowd, ~drum, ~explosion, ~firework, ~horn (horn_sound), ~jackhammer, ~motorcycle, ~siren, ~speaker, ~thunder, ~whistle, !gunshot, !jet

### QUIET THINGS  `quiet_things`
- правило: Things that make almost no sound
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~breath, ~breeze, ~cat, ~cloud, ~feather, ~library, ~moth, ~Shadow, ~silk, ~sleep, ~snow, ~tiptoe, ~whisper, !mouse (mouse_animal)

### RED THINGS  `red_things`
- правило: Everyday things that are typically red in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~apple (apple_fruit), ~barn, ~beet, ~blood, ~brick, ~cardinal (cardinal_bird), ~cherry, ~chili (chili_pepper), ~flame, ~ketchup, ~lipstick, ~lobster, ~radish, ~rose, ~ruby, ~strawberry, ~tomato, ~valentine, !fire truck, !stop sign

### ROUND THINGS  `round_things`
- правило: Everyday objects whose normal shape is round or circular
- тип связи: `has_property`, базовая сложность 0.3
- слов: 26
- ~apple (apple_fruit), ~bagel, ~ball (ball_sphere), ~balloon, ~bubble, ~button (button_clothing), ~coaster, ~coin, ~cookie, ~dial, ~donut, ~globe, ~hoop, ~marble (marble_toy), ~moon (moon_space), ~orange (orange_fruit), ~pancake, ~pearl, ~pizza, ~plate (plate_dish), ~ring, ~tire, ~wheel, ~wreath, !clock, !lens

### SHINY THINGS  `shiny_things`
- правило: Things that reflect light and look shiny
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~bumper, ~chrome, ~coin, ~diamond, ~foil, ~glass, ~glitter, ~gold, ~jewel, ~lacquer, ~mirror, ~polish (polish_verb), ~satin, ~sequin, ~silver, ~star, !blade, !ice

### SLOW THINGS  `slow_things`
- правило: Things known for moving very slowly
- тип связи: `has_property`, базовая сложность 0.35
- слов: 12
- ~caterpillar, ~molasses, ~sloth, ~slug, ~snail, ~tortoise, ~traffic, ~turtle, ~worm, !glacier, !parade, !tractor

### SMELLY THINGS  `smelly_things`
- правило: Things with a very strong smell
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~bleach, ~cheese, ~garlic, ~gasoline, ~incense, ~manure, ~onion, ~perfume, ~skunk, ~smoke, ~vinegar, !ammonia, !durian, !fish, !mothball

### SOFT THINGS  `soft_things`
- правило: Things that feel soft to the touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~blanket, ~cloud, ~cotton, ~cushion, ~dough, ~feather, ~foam, ~fur, ~kitten, ~marshmallow, ~moss, ~pillow, ~silk, ~sponge (sponge_cleaning), ~teddy bear, ~velvet, ~wool, !sand

### SQUARE THINGS  `square_things`
- правило: Everyday things shaped like a square
- тип связи: `has_property`, базовая сложность 0.35
- слов: 13
- ~box, ~brick, ~envelope, ~napkin, ~stamp (stamp_postage), ~tile, ~waffle, !checkerboard, !dice (dice_game), !keyboard key, !picture frame, !sticky note, !window

### STICKY THINGS  `sticky_things`
- правило: Substances that stick to whatever they touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~caramel, ~frosting, ~glue, ~gum (gum_glue), ~honey, ~jam, ~marshmallow, ~molasses, ~paste, ~resin, ~sap, ~slime, ~syrup, ~taffy, ~tape, ~tar, ~wax (wax_substance), !pitch (pitch_tar)

### STRIPED THINGS  `striped_things`
- правило: Things that normally have stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 13
- ~candy cane, ~crosswalk, ~flag, ~ribbon, ~road, ~skunk, ~tiger, ~zebra, !awning, !barber pole, !bee, !prison uniform, !referee shirt

### POINTED THINGS  `things_that_are_sharp`
- правило: Things that come to a sharp point
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~arrow, ~claw, ~cone, ~dart (dart_throw), ~fang, ~icicle, ~nail (nail_metal), ~needle (needle_sewing), ~pencil, ~pin (pin_fastener), ~spear, ~spike, ~sword, ~tack (tack_pin), ~thorn, !horn (horn_animal)

### FRAGILE THINGS  `things_that_break`
- правило: Things that break easily when dropped
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~chalk (chalk_stick), ~China, ~glass, ~ice, ~mirror, ~porcelain, ~pottery, ~vase, !bulb, !egg, !lightbulb, !ornament, !screen (screen_display), !shell

### FLOATING THINGS  `things_that_float`
- правило: Things that float on water
- тип связи: `has_property`, базовая сложность 0.35
- слов: 17
- ~balloon, ~boat, ~bubble, ~buoy, ~cork, ~duck (duck_bird), ~feather, ~foam, ~ice, ~leaf, ~raft, ~wood, !driftwood, !life vest, !lily pad, !oil (oil_cooking), !pool noodle

### SHRINKING THINGS  `things_that_shrink`
- правило: Things that get smaller over time or with heat
- тип связи: `has_property`, базовая сложность 0.45
- слов: 13
- ~candle, ~glacier, ~ice, ~puddle, ~Shadow, ~snowman, ~soap, ~sponge (sponge_cleaning), ~sweater, !balloon, !battery, !pencil, !savings

### STRETCHY THINGS  `things_that_stretch`
- правило: Things that stretch when pulled
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~elastic, ~gum (gum_candy), ~rubber band, ~spandex, ~taffy, ~waistband, !balloon, !bungee cord, !dough, !muscle, !skin, !Slinky, !sock, !spring

### THINGS WITH HOLES  `things_with_holes`
- правило: Everyday things that have holes in them
- тип связи: `has_property`, базовая сложность 0.35
- слов: 16
- ~button (button_clothing), ~colander, ~donut, ~needle (needle_sewing), ~sieve, ~sponge (sponge_cleaning), ~swiss cheese, !belt, !cheese grater, !flute, !golf course, !net, !sock, !straw (straw_tube), !waffle, !whistle

### CLEAR THINGS  `transparent_things`
- правило: Things you can see through
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~air, ~aquarium, ~bubble, ~crystal, ~glass, ~ice, ~jellyfish, ~lens, ~screen (screen_display), ~water, ~window, !cellophane, !plastic wrap, !veil

### WHITE THINGS  `white_things`
- правило: Everyday things that are typically white in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~bone, ~chalk (chalk_stick), ~cloud, ~cotton, ~dove, ~flour, ~ghost, ~ivory, ~marshmallow, ~milk, ~paper, ~pearl, ~rice, ~sail (sail_cloth), ~salt, ~sheet (sheet_bed), ~snow, ~sugar, ~swan, ~tooth

### YELLOW THINGS  `yellow_things`
- правило: Everyday things that are typically yellow in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~banana, ~bee, ~butter, ~canary, ~cheese, ~corn, ~daffodil, ~duckling, ~gold, ~lemon, ~mustard, ~pineapple, ~raincoat, ~school bus, ~sun, ~sunflower, ~taxi, ~yolk, !highlighter, !honey


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


## Тема: sounds

### ALARM SOUNDS  `bell_and_alarm`
- правило: Sounds made by alarms and signals
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~alert, ~beep, ~bell, ~buzz, ~chime, ~ding, ~gong, ~horn (horn_sound), ~ring, ~siren, ~tone, ~whistle, !blare, !klaxon

### CITY SOUNDS  `city_sounds`
- правило: Sounds heard on a city street
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~alarm, ~bell, ~chatter, ~engine, ~honk, ~jackhammer, ~rumble, ~screech, ~shout, ~siren, ~traffic, ~whistle, !brakes, !footsteps

### KITCHEN SOUNDS  `kitchen_sounds`
- правило: Sounds heard in a kitchen
- тип связи: `does_action`, базовая сложность 0.45
- слов: 14
- ~boil, ~bubble, ~crunch (crunch_sound), ~grind, ~hiss, ~pop (pop_sound), ~sizzle, !chop, !clatter, !clink, !ding, !slam, !whir, !whisk

### LOUD NOISES  `loud_noises`
- правило: Words for very loud noises
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~bang, ~blast, ~boom, ~clash, ~crash, ~explosion, ~roar, ~rumble, ~screech, ~slam, ~thunder, ~wail, !blare, !shatter

### MACHINE SOUNDS  `machine_sounds`
- правило: Sounds that machines make
- тип связи: `does_action`, базовая сложность 0.4
- слов: 16
- ~beep, ~buzz, ~click, ~hum, ~rattle (rattle_sound), ~roar, ~screech, ~whine, !chug, !clank, !ding, !grind, !purr, !rev, !sputter, !whir

### MUSIC SOUNDS  `musical_sounds`
- правило: Words for the sound a musical instrument makes
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~boom, ~chime, ~clang, ~hum, ~strum, ~toot, +jingle, +riff, +ring, +thump, +trill, +twang, !blare, !drumroll

### NATURE SOUNDS  `nature_sounds`
- правило: Sounds heard outdoors in nature
- тип связи: `does_action`, базовая сложность 0.4
- слов: 15
- ~buzz, ~chirp, ~crackle, ~crunch (crunch_sound), ~hoot, ~howl, ~hum, ~roar, ~thunder, ~whistle, !croak, !patter, !rustle, !splash, !whisper

### SOUND WORDS  `onomatopoeia`
- правило: Words that imitate the sound they name
- тип связи: `is_a`, базовая сложность 0.35
- слов: 25
- ~boom, ~clang, ~drip (drip_water), ~hiss, ~jingle, ~plop, ~ring, ~splash, ~tick (tick_sound), +bang, +beep, +buzz, +click, +crackle, +crash, +ping, +pop (pop_sound), +rumble, +sizzle, +snap, +squeak, +thud, +whack, +whoosh, +zap

### QUIET SOUNDS  `quiet_sounds`
- правило: Words for very soft sounds
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~breath, ~creak, ~hum, ~murmur, ~sigh, ~whisper, !drip (drip_water), !patter, !purr, !rustle, !shuffle (shuffle_walk), !tick (tick_sound), !tinkle

### SCARY SOUNDS  `scary_sounds`
- правило: Sounds that make people uneasy
- тип связи: `does_action`, базовая сложность 0.45
- слов: 14
- ~creak, ~groan, ~growl, ~howl, ~moan, ~rattle (rattle_sound), ~scream, ~shriek, ~thud, ~wail, !footstep, !scratch, !snap, !whisper

### VOICE SOUNDS  `voice_sounds`
- правило: Sounds a human voice makes without words
- тип связи: `does_action`, базовая сложность 0.35
- слов: 16
- ~cough, ~giggle, ~hum, ~laugh, ~scream, ~shout, ~snort, ~yawn, +cry, +gasp, +groan, +grunt, +moan, +sigh, +sob, +whistle

### WATER SOUNDS  `water_sounds`
- правило: Sounds that water makes
- тип связи: `does_action`, базовая сложность 0.4
- слов: 14
- ~drip (drip_water), ~hiss, ~lap (lap_water), ~splash, ~spray, ~whoosh, !babble, !gurgle, !patter, !plop, !ripple, !roar, !slosh, !trickle


## Тема: space

### ASTRONAUT GEAR  `astronaut_gear`
- правило: Equipment an astronaut uses
- тип связи: `used_in`, базовая сложность 0.35
- слов: 13
- ~backpack, ~boot (boot_shoe), ~camera, ~glove, ~helmet, +checklist, +communicator, +jetpack, +oxygen tank, +tether, +tool belt, +visor, !spacesuit

### STARS  `bright_stars`
- правило: Individual stars people can name
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Capella, +Castor, +Polaris, +Sirius, +Vega, !Aldebaran, !Altair, !Antares, !Arcturus, !Betelgeuse, !Deneb, !Pollux, !Procyon, !Rigel, !Spica

### CONSTELLATIONS  `constellations`
- правило: Constellations in the night sky
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +Andromeda, +Big Dipper, +Crux, +Cygnus, +Draco, +Hercules, +Little Dipper, +Lyra, +Orion, +pegasus, +Perseus, +Ursa Major, +Ursa Minor, !Cassiopeia, !Centaurus

### MOONS  `moons`
- правило: Named moons of the solar system
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~triton, +Europa, +Ganymede, +Io, +Luna, +Miranda, +Rhea, +Titan, !Callisto, !Charon, !Deimos, !Enceladus, !Iapetus, !Phobos

### ROCKET PARTS  `rocket_parts`
- правило: Parts of a rocket
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~capsule, ~engine, ~fin, ~stage, +booster, +fuel tank, +heat shield, +launch pad, +nose cone, +nozzle, +payload, +thruster

### SCI FI  `science_fiction_space`
- правило: Words used in space science fiction
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~Alien, ~android, ~colony, ~cyborg, ~galaxy, ~laser, ~ray gun, ~warp, !force field, !hyperdrive, !mothership, !starship, !teleport, !wormhole

### SOLAR SYSTEM  `solar_system_words`
- правило: Words describing the solar system
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~ring, +asteroid belt, +comet, +corona, +dwarf planet, +eclipse, +gravity, +meteor, +moon, +orbit, +planet, +solar wind, +sun, !kuiper belt

### SPACE PLACES  `space_agencies_and_places`
- правило: Places and organizations connected with space flight
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- +Cape Canaveral, +Houston, +ISS, +Jet Propulsion Lab, +Kennedy Space Center, +launch pad, +Mission Control, +NASA, +observatory, !Baikonur, !Roscosmos

### SPACE MEASUREMENTS  `space_measurements`
- правило: Units used to measure distance and time in space
- тип связи: `is_a`, базовая сложность 0.45
- слов: 11
- ~gravity, ~kilometer, ~light year, ~mile, ~orbit, ~revolution, ~rotation, !astronomical unit, !degree (degree_angle), !magnitude, !parsec

### SPACE PHENOMENA  `space_phenomena`
- правило: Events and phenomena seen in space
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~aurora, ~eclipse, ~supernova, +big bang, +black hole, +comet tail, +gravity well, +meteor shower, +nebula, +solar flare, +sunspot, !quasar

### SPACECRAFT  `spacecraft`
- правило: Famous spacecraft and space missions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Apollo, ~Curiosity, ~Discovery, ~Pioneer, ~Viking, +Atlantis, +Cassini, +Challenger, +Columbia, +Galileo, +Hubble, +Juno, +Soyuz, +Sputnik, +Voyager

### TELESCOPE WORDS  `telescope_words`
- правило: Parts and words used with a telescope
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~focus (focus_lens), ~lens, ~mirror, ~tripod, !aperture, !dome, !eyepiece, !filter, !finder, !magnification, !mount, !observatory, !reflector, !refractor


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


## Тема: sports

### BASEBALL EQUIPMENT  `baseball_equipment`
- правило: Physical equipment used to play a game of baseball
- тип связи: `used_in`, базовая сложность 0.25
- слов: 15
- ~ball (ball_sphere), ~cap, ~glove, ~helmet, ~mask, ~plate (plate_base), +base, +bat (bat_equipment), +batting glove, +chest protector, +cleats, +mitt, +pine tar, +rosin bag, +shin guard

### BASEBALL WORDS  `baseball_words`
- правило: Words used to describe plays, places or roles in a baseball game
- тип связи: `found_in`, базовая сложность 0.3
- слов: 27
- ~diamond (diamond_field), ~error, ~single (single_baseball), ~steal, ~walk, +bullpen, +bunt, +catcher, +curveball, +double play, +dugout, +fastball, +foul, +grand slam, +home run, +infield, +inning, +lineup, +mound (mound_baseball), +outfield, +pitch (pitch_throw), +pitcher (pitcher_baseball), +shortstop, +slider, +strike (strike_baseball), +triple, +umpire

### BASKETBALL WORDS  `basketball_words`
- правило: Words used to describe plays and roles in basketball
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~assist, ~block (block_stop), ~buzzer, ~center, ~court (court_sport), ~forward, ~foul, ~guard (guard_sport), ~travel, +backboard, +dribble, +dunk (dunk_basketball), +free throw, +hoop, +jump ball, +layup, +rebound, +three pointer, +timeout, !screen (screen_basketball)

### GAMES OF SKILL  `board_and_card_games`
- правило: Competitive indoor games of skill
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~backgammon, ~bridge (bridge_card), ~poker, +air hockey, +billiards, +bowling, +checkers, +chess, +darts, +dominoes, +table tennis, !cornhole, !foosball, !shuffleboard

### OUTDOOR ACTIVITIES  `camping_and_outdoors`
- правило: Recreational activities done outdoors
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~biking, ~camping, ~hunting, ~rafting, ~sailing, ~surfing, +backpacking, +canoeing, +climbing, +fishing, +hiking, +kayaking, +running, +skiing, +snorkeling, !birdwatching, !geocaching, !picnicking

### CYCLING WORDS  `cycling_words`
- правило: Words used about riding and racing bicycles
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~brake, ~chain, ~jersey, ~saddle, ~sprint, ~tire, ~trail, +cadence, +drafting, +gear, +handlebar, +helmet, +pedal, +peloton, +spoke, +tour

### FISHING THINGS  `fishing_things`
- правило: Things used to catch fish
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~boat, ~cooler, ~fly (fly_lure), ~spear, ~trap, +bait, +hook (hook_fishing), +line (line_cord), +lure, +net, +pole, +reel (reel_fishing), +rod, +sinker, +tackle box, +worm, !bobber, !waders

### FOOTBALL WORDS  `football_words`
- правило: Words used to describe plays and roles in American football
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~down, ~helmet, ~sack (sack_football), ~safety, ~snap, +blitz, +end zone, +field goal, +fumble, +huddle, +interception, +kickoff, +lineman, +punt, +quarterback, +receiver, +referee, +tackle, +touchdown, +yard line

### GOLF WORDS  `golf_words`
- правило: Words used to describe play and equipment in golf
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bogey, ~bunker (bunker_golf), ~eagle, ~flag, ~green (green_golf), ~iron (iron_golf), ~rough, ~wedge, +birdie, +caddy, +course, +driver, +fairway, +hole in one, +par, +putter, +sand trap, +tee

### GYM EQUIPMENT  `gym_equipment`
- правило: Equipment used for exercise in a fitness gym
- тип связи: `used_in`, базовая сложность 0.25
- слов: 19
- ~bench (bench_seat), ~jump rope, ~mat, ~rope, +barbell, +dumbbell, +elliptical, +foam roller, +medicine ball, +pull up bar, +punching bag, +resistance band, +rowing machine, +stair climber, +stationary bike, +treadmill, +weights, !club (club_stick), !kettlebell

### HOCKEY WORDS  `hockey_words`
- правило: Words used to describe plays and gear in ice hockey
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~check (check_hockey), ~crease, ~helmet, ~icing, ~net, ~period, ~skate, +blue line, +faceoff, +goalie, +pad, +penalty box, +power play, +puck, +rink, +stick (stick_hockey), !slapshot, !zamboni

### MARTIAL ARTS  `martial_arts`
- правило: Fighting sports and self defense disciplines
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~jujitsu, ~sumo, +aikido, +boxing, +fencing, +judo, +karate, +kickboxing, +kung fu, +muay thai, +taekwondo, +wrestling, !capoeira, !kendo

### OLYMPIC SPORTS  `olympic_sports`
- правило: Sports contested at the modern Olympic Games
- тип связи: `is_a`, базовая сложность 0.25
- слов: 25
- ~archery, ~badminton, ~diving, ~javelin, ~judo, ~marathon, ~shot put, ~skating, ~skiing, ~swimming, ~taekwondo, +biathlon, +boxing, +canoeing, +curling, +fencing, +gymnastics, +hurdles, +luge, +rowing, +sailing, +triathlon, +weightlifting, +wrestling, !bobsled

### RACING SPORTS  `racing_sports`
- правило: Sports where competitors race to finish first
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~cycling, ~swimming, +cross country, +dog sled racing, +drag racing, +horse racing, +hurdles, +marathon, +motocross, +relay, +rowing, +sailing, +speed skating, +sprint, +triathlon

### SOCCER WORDS  `soccer_words`
- правило: Words used to describe plays and roles in soccer
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~assist, ~defender, ~dribble, ~net, ~penalty, ~pitch, ~whistle, +corner kick, +free kick, +goal, +goalkeeper, +header, +midfielder, +offside, +red card, +striker, +throw in, +yellow card

### BALLS  `sports_balls`
- правило: Balls used in different sports
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- +baseball, +basketball, +beach ball, +bowling ball, +cricket ball, +football, +golf ball, +medicine ball, +ping pong ball, +rugby ball, +soccer ball, +softball, +tennis ball, +volleyball

### PROTECTIVE GEAR  `sports_gear_worn`
- правило: Gear athletes wear to protect the body
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~brace, ~cup, ~glove, ~goggles, ~harness, ~helmet, ~mask, ~pad, +chest protector, +elbow pad, +knee pad, +shin guard, +wrist guard, !mouthguard

### SPORTS OFFICIALS  `sports_officials`
- правило: People who enforce the rules of a sport
- тип связи: `is_a`, базовая сложность 0.35
- слов: 10
- ~judge, ~official, ~referee, ~starter, ~steward, ~umpire, +linesman, +marshal, +scorer, !timekeeper

### SCORING WORDS  `sports_scoring`
- правило: Words used for scoring and results in sports
- тип связи: `found_in`, базовая сложность 0.35
- слов: 20
- ~lead (lead_front), ~point (point_score), ~record, ~standing, ~tie (tie_score), ~title, +championship, +comeback, +draw, +goal, +loss, +medal, +overtime, +playoff, +ranking, +score (score_points), +shutout, +streak, +trophy, +win

### SPORTS VENUES  `sports_venues`
- правило: Places built for playing or watching sports
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~alley, ~course, ~court (court_sport), ~diamond, ~dome, ~gym, ~pitch, ~pool, ~racetrack, ~ring, ~rink, ~track, +arena, +ballpark, +dojo, +field, +stadium, +velodrome

### TEAM SPORTS  `team_sports`
- правило: Sports played by two opposing teams
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- ~dodgeball, +baseball, +basketball, +cricket, +field hockey, +football, +handball, +hockey, +lacrosse, +netball, +polo, +rugby, +soccer, +softball, +ultimate frisbee, +volleyball, +water polo, !kickball

### TENNIS WORDS  `tennis_words`
- правило: Words used to describe play and scoring in tennis
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~Ace, ~fault, ~love, ~net, ~rally, ~umpire, +backhand, +baseline, +court (court_sport), +deuce, +forehand, +lob, +match point, +racket, +serve, +set (set_tennis), +volley, !tiebreak

### WATER SPORTS  `water_sports`
- правило: Sports played in or on the water
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~rafting, +canoeing, +diving, +kayaking, +rowing, +sailing, +snorkeling, +surfing, +swimming, +synchronized swimming, +water polo, +water skiing, !paddleboarding, !wakeboarding, !windsurfing

### WINTER SPORTS  `winter_sports`
- правило: Sports played on snow or ice
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- +biathlon, +curling, +figure skating, +hockey, +ice climbing, +luge, +skating, +skiing, +sledding, +snowboarding, +speed skating, !bobsled, !snowshoeing, !tobogganing


## Тема: sports_world

### ARCHERY WORDS  `archery_words`
- правило: Words used in archery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~draw, ~range (range_shooting), ~release, ~sight, ~string, +arm guard, +arrow, +bow (bow_weapon), +bullseye, +quiver, +shaft, +Target, !fletching, !nock

### BOWLING WORDS  `bowling_words`
- правило: Words used in bowling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~alley, ~approach, ~ball (ball_sphere), ~frame, ~gutter, ~lane, ~pin (pin_bowling), ~rack, ~spare, ~split, ~strike (strike_bowling), ~turkey (turkey_bowling), +foul line, +score sheet

### BOXING WORDS  `boxing_words`
- правило: Words used in a boxing match
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~bell, ~belt, ~corner, ~glove, ~hook (hook_boxing), ~jab, ~referee, ~ring, ~round (round_stage), +bout, +clinch, +decision, +knockout, +southpaw, +uppercut, xcutman

### HORSE RIDING  `equestrian_words`
- правило: Words used in horse riding sports
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~arena, ~fence, ~groom (groom_horse), +bridle, +canter, +dressage, +gallop, +jockey, +jumping, +reins, +saddle, +tack (tack_horse), +trot, !stirrup

### FAMOUS STADIUMS  `famous_stadiums`
- правило: Famous sports stadiums and arenas
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- +Augusta, +Camp Nou, +Churchill Downs, +Daytona, +Fenway, +Lambeau, +Madison Square Garden, +Old Trafford, +Rose Bowl, +Wembley, +Wrigley, +Yankee Stadium

### FAN THINGS  `fan_things`
- правило: Things sports fans bring or wear to a game
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~cap, ~cooler, ~horn (horn_sound), ~jersey, ~megaphone, ~poster, ~scarf, ~ticket (ticket_admission), ~whistle, +banner, +face paint, +foam finger, +pennant, !cowbell

### GYMNASTICS EVENTS  `gymnastics_events`
- правило: Events and moves in gymnastics
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bars, ~beam (beam_gym), ~cartwheel, ~floor, ~rings, ~routine, ~somersault, ~split, ~vault, +dismount, +flip, +tumbling, !handstand, !pommel horse

### MOTOR RACING  `racing_words`
- правило: Words used in motor racing
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~caution, ~crew, ~grid, ~helmet, ~lap (lap_race), ~tire, ~track, +checkered flag, +driver, +pit stop, +pole position, +qualifying, +speedway, +spoiler

### SKATEBOARDING WORDS  `skateboarding`
- правило: Words used in skateboarding
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bearing, ~bowl, ~helmet, ~rail, ~ramp, ~trucks, ~wheels, !deck, !grind, !grip tape, !halfpipe, !kickflip, !nose, !ollie

### SKIING WORDS  `skiing_words`
- правило: Words used on a ski slope
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~boots, ~goggles, ~gondola, ~lift, ~lodge, ~powder, +bindings, +black diamond, +moguls, +poles, +slope, +trail map, !apres ski, !snowplow

### SPORTS INJURIES  `sports_injuries`
- правило: Injuries common in sports
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~tear, +bruise, +concussion, +cramp, +dislocation, +fracture, +pulled muscle, +shin splints, +sprain, +strain, +tennis elbow, +torn acl, +whiplash

### SPORTS LEAGUES  `sports_leagues`
- правило: Professional sports leagues and competitions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Olympics, ~Super Bowl, +Indy 500, +Kentucky Derby, +Masters, +MLB, +MLS, +NBA, +NFL, +NHL, +Stanley Cup, +Tour de France, +Wimbledon, +World Cup, +World Series

### SPORTS LEGENDS  `sports_legends`
- правило: Athletes remembered across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Louis, ~Robinson, +Ali, +Chamberlain, +DiMaggio, +Gretzky, +Jordan, +Montana, +Nicklaus, +Owens, +Pele, +Ruth, +Thorpe, !Comaneci, !Navratilova

### SWIM STROKES  `swimming_strokes`
- правило: Strokes and events in competitive swimming
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~butterfly, ~distance, ~dive, ~sprint, +backstroke, +breaststroke, +doggy paddle, +freestyle, +medley, +relay, +sidestroke, +treading

### TRACK EVENTS  `track_events`
- правило: Events contested in track and field
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~shot put, +decathlon, +discus, +high jump, +hurdles, +javelin, +long jump, +marathon, +pole vault, +race walk, +relay, +sprint, +steeplechase, +triple jump

### TRAINING WORDS  `training_words`
- правило: Words used in athletic training
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~circuit, ~coach, ~drill (drill_practice), ~endurance, ~form, ~interval, ~recovery, ~routine, ~set (set_exercise), ~stretch, +conditioning, +rep, +warmup, !cooldown

### WRESTLING WORDS  `wrestling_words`
- правило: Words used in wrestling
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~escape, ~hold, ~mat, ~period, ~pin (pin_wrestling), ~referee, ~throw, +headgear, +reversal, +singlet, +takedown, +weight class, !bridge (bridge_move)


## Тема: technology

### COMPUTER ACTIONS  `computer_actions`
- правило: Actions done while using a computer
- тип связи: `does_action`, базовая сложность 0.25
- слов: 20
- ~close, ~copy, ~drag, ~paste, ~save, ~search, ~share, ~Zoom, +click, +delete, +download, +install, +log in, +print, +refresh, +restart, +scroll (scroll_screen), +type, +undo, +upload

### COMPUTER PARTS  `computer_parts`
- правило: Physical parts of a personal computer
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~battery, ~cable, ~case (case_box), ~fan (fan_device), ~memory, ~port, ~speaker, ~tower, +Charger, +graphics card, +hard drive, +keyboard (keyboard_computer), +monitor (monitor_screen), +motherboard, +mouse (mouse_computer), +power supply, +processor, +screen (screen_display), +webcam, !touchpad

### EMAIL WORDS  `email_words`
- правило: Parts and actions of an email message
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~archive, ~draft (draft_document), ~forward, ~signature, ~subject, ~thread, ~trash, +attachment, +cc, +inbox, +recipient, +reply, +sender, +spam, +unread, !outbox

### FILE WORDS  `file_types`
- правило: Words for computer files and documents
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~archive, ~attachment, ~image, ~presentation, ~trash, ~video, ~zip, +backup, +document, +draft (draft_document), +file (file_computer), +folder, +pdf, +shortcut, +spreadsheet, +template

### GADGETS  `gadgets`
- правило: Small electronic devices people own
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~camera, ~console, ~doorbell, ~drone, ~e-reader, ~phone, ~printer, ~projector, ~remote (remote_device), ~speaker, ~watch (watch_object), +earbuds, +fitness tracker, +headphones, +laptop, +scanner, +tablet, +thermostat

### HOME ELECTRONICS  `home_electronics`
- правило: Electronic devices used in a home
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~alarm, ~blender, ~doorbell, ~microwave, ~stereo, ~vacuum, +air conditioner, +dvd player, +game console, +radio, +router, +smart speaker, +television, +thermostat, !humidifier

### INTERNET WORDS  `internet_words`
- правило: Words used about the internet
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~cloud, ~cookie, ~router, ~spam, +bandwidth, +bookmark, +browser, +domain, +download, +email, +firewall, +hotspot, +link (link_web), +network, +password, +server, +streaming, +url, +website, +wifi

### MEASURING DEVICES  `measurement_devices`
- правило: Devices that measure and display a reading
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~barometer, ~compass, ~meter, ~odometer, ~stopwatch, ~tachometer, ~thermometer, +gauge, +scale, +speedometer, !altimeter, !seismograph, !sundial, !voltmeter

### OFFICE MACHINES  `office_machines`
- правило: Machines used in an office
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~phone, ~projector, +binder machine, +calculator, +computer, +copier, +fax, +label maker, +postage meter, +printer, +scanner, +shredder, +typewriter, !laminator

### PHONE WORDS  `phone_words`
- правило: Things and features of a mobile phone
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~alarm, ~battery, ~case (case_box), ~screen (screen_display), ~signal, ~speaker, +app, +camera, +Charger, +contact, +headphones, +hotspot, +keypad, +notification, +ringtone, +sim card, +text, +voicemail

### PHOTOGRAPHY WORDS  `photography_words`
- правило: Words used when taking photographs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~angle, ~crop, ~filter, ~negative, +album, +aperture, +darkroom, +exposure, +flash, +focus (focus_lens), +frame, +lens, +portrait, +selfie, +shutter, +snapshot, +tripod, +Zoom

### POWER WORDS  `power_and_batteries`
- правило: Words about supplying power to devices
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~cable, +adapter, +battery, +Charger, +cord, +extension, +fuse, +generator, +outlet, +plug, +power strip, +socket (socket_electric), +solar panel, +switch, +voltage, +Watt

### PROGRAMMING WORDS  `programming_words`
- правило: Words used when writing computer programs
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~algorithm, ~array, ~code, ~compile, ~database, ~function, ~loop, ~output, ~script, ~string, ~variable, !bug, !class, !debug, !library, !module, !query, !syntax

### ROBOT WORDS  `robot_words`
- правило: Words used when talking about robots
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~algorithm, ~android, ~arm, ~automation, ~circuit, ~drone, ~gear, ~joint, ~motor, ~program, ~robot, !chassis, !remote (remote_device), !sensor, !servo

### THINGS WITH SCREENS  `screens`
- правило: Everyday devices that have a screen
- тип связи: `has_property`, базовая сложность 0.3
- слов: 16
- ~calculator, ~console, ~dashboard, ~gps, ~kiosk, ~laptop, ~monitor (monitor_screen), ~phone, ~tablet, ~television, ~watch (watch_object), !ATM, !camera, !e-reader, !microwave, !treadmill

### SECURITY DEVICES  `security_tech`
- правило: Devices used to keep property secure
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~alarm, ~badge, ~buzzer, ~camera, ~fence, ~lock, ~monitor (monitor_screen), ~sensor, ~siren, +keypad, +motion detector, +safe, !deadbolt, !floodlight

### SIGNALS AND CODES  `signals_and_codes`
- правило: Systems used to send coded messages
- тип связи: `is_a`, базовая сложность 0.4
- слов: 11
- ~morse code, ~telegraph, !barcode, !beacon, !braille, !cipher, !flag signal, !qr code, !semaphore, !sign language, !smoke signal

### SOCIAL MEDIA  `social_media_words`
- правило: Words used on social media
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~block (block_ban), ~comment, ~feed, ~filter, ~follow, ~like, ~profile, ~reel (reel_video), ~share, ~story (story_post), ~tag (tag_mention), ~thread, ~viral, +emoji, +hashtag, +message, +post (post_online), +trending

### SOUND DEVICES  `sound_devices`
- правило: Devices that record or play sound
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- +amplifier, +headphone, +megaphone, +microphone, +radio, +record player, +speaker, +stereo, +tape deck, +turntable, +walkman, !boombox, !earbud, !soundbar

### OLD TECHNOLOGY  `things_with_screens_history`
- правило: Technology that has mostly been replaced
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~cassette, ~fax, ~phonograph, ~telegram, ~typewriter, ~walkman, !dial up, !film camera, !floppy disk, !overhead projector, !pager, !payphone, !rotary phone, !vhs


## Тема: time

### BIRTHDAY THINGS  `birthday_things`
- правило: Things associated with a birthday celebration
- тип связи: `found_in`, базовая сложность 0.2
- слов: 16
- ~balloon, ~cake, ~candle, ~card (card_greeting), ~guest, ~hat, ~ice cream, ~present (present_gift), ~song, ~wish, +confetti, +invitation, +party (party_event), +piñata, +streamer, +surprise

### CALENDAR WORDS  `calendar_words`
- правило: Everyday English words for dates and periods of time on a calendar
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~birthday, ~quarter (quarter_fourth), ~semester, ~spring (spring_season), ~term (term_period), +anniversary, +century, +date (date_calendar), +day, +decade, +era, +fortnight, +holiday, +leap year, +millennium, +month, +season (season_time), +week, +weekday, +weekend, +workweek, +year

### CHRISTMAS THINGS  `christmas_things`
- правило: Things associated with an American Christmas
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~chimney, ~eggnog, ~garland, ~mistletoe, ~snowman, ~star, ~tinsel, ~tree, +candy cane, +carol, +elf, +gift, +gingerbread, +lights, +nutcracker, +ornament, +reindeer, +sleigh, +stocking, +wreath

### CLOCK WORDS  `clock_words`
- правило: Words and parts having to do with clocks
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~chime, ~dial, ~face, ~hand (hand_clock), ~snooze, ~stopwatch, +alarm, +cuckoo, +hour hand, +hourglass, +minute hand, +pendulum, +second hand, +tick (tick_sound), +timer, !sundial

### DAYS & TIMES  `days_and_parts_of_day`
- правило: Names of weekdays and parts of the day
- тип связи: `is_a`, базовая сложность 0.15
- слов: 18
- +afternoon, +dawn, +dusk, +evening, +Friday, +midnight, +Monday, +morning, +night, +noon, +Saturday, +Sunday, +sunrise, +sunset, +Thursday, +Tuesday, +twilight, +Wednesday

### HALLOWEEN THINGS  `halloween_things`
- правило: Things associated with Halloween
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~bat, ~broom, ~candy, ~cauldron, ~cobweb, ~haunted house, ~spider, ~tombstone, ~vampire, +black cat, +costume, +ghost, +jack o lantern, +mask, +pumpkin, +skeleton, +treat, +trick, +witch, +zombie

### HISTORICAL ERAS  `historical_eras`
- правило: Named periods of human history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~renaissance, +Antiquity, +Bronze Age, +Colonial, +Dark Ages, +Great Depression, +Ice Age, +Industrial Revolution, +Iron Age, +Middle Ages, +Roaring Twenties, +Space Age, +Stone Age, +Victorian

### HOLIDAYS  `holidays`
- правило: Holidays widely celebrated in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~Halloween, +April Fools, +Christmas, +Columbus Day, +Easter, +Fathers Day, +Groundhog Day, +Hanukkah, +Independence Day, +Labor Day, +Memorial Day, +Mothers Day, +New Year, +Passover, +Presidents Day, +Thanksgiving, +Valentine's Day, +Veterans Day, !Juneteenth, !Kwanzaa

### MONTHS  `months`
- правило: Months of the Gregorian calendar year
- тип связи: `is_a`, базовая сложность 0.1
- слов: 11
- +April, +August, +December, +February, +January, +July, +June, +march (march_month), +November, +October, +September

### NEW YEAR  `new_year_things`
- правило: Things associated with New Year celebrations
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~calendar, ~confetti, ~kiss, ~midnight, ~toast (toast_salute), +ball drop, +champagne, +countdown, +fireworks, +party (party_event), +resolution, +streamer, !noisemaker, !sparkler

### TIME WORDS  `past_and_future`
- правило: Words that place something in time
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~always, ~meanwhile, ~once, ~still, +after, +already, +before, +early, +forever, +late, +later, +never, +now, +recently, +soon, +today, +tomorrow, +yesterday

### SEASONS  `seasons`
- правило: The four seasons of the year
- тип связи: `is_a`, базовая сложность 0.15
- слов: 5
- +Autumn, +fall, +spring, +summer, +winter

### QUICK WORDS  `speed_of_time`
- правило: Words meaning that something happens without delay
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~abruptly, ~at once, ~immediately, ~instantly, ~quickly, ~right away, ~shortly, ~suddenly, ~swiftly, !hastily, !momentarily, !promptly

### UNITS OF TIME  `time_units`
- правило: Units used to measure time
- тип связи: `is_a`, базовая сложность 0.2
- слов: 16
- ~quarter (quarter_fourth), ~semester, +century, +day, +decade, +era, +generation, +hour, +instant, +millennium, +minute (minute_time), +moment, +month, +second (second_time), +week, +year

### WEDDING THINGS  `wedding_things`
- правило: Things associated with a wedding
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~cake, ~rice, ~toast (toast_salute), +aisle, +altar, +best man, +bouquet, +bride, +bridesmaid, +ceremony, +dress, +garter, +groom (groom_wedding), +honeymoon, +invitation, +reception, +ring, +tuxedo, +veil, +vows


## Тема: tools

### GLUES AND TAPES  `adhesives`
- правило: Sticky products used to join things
- тип связи: `used_in`, базовая сложность 0.35
- слов: 15
- ~cement, ~masking tape, ~putty, +adhesive, +duct tape, +epoxy, +glue, +gum (gum_glue), +hot glue, +mortar, +paste, +sealant, +super glue, +tape, !caulk

### ART SUPPLIES  `art_supplies`
- правило: Materials used to make art or crafts
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~bead, ~brush, ~canvas, ~chalk (chalk_stick), ~charcoal, ~clay, ~glitter, ~glue, ~pastel, ~ribbon, ~scissors, ~yarn, +crayon, +ink, +marker, +paint, +paper, +pencil, +sketchbook, +stencil

### BLADES  `blades`
- правило: Parts of tools that do the cutting
- тип связи: `is_a`, базовая сложность 0.35
- слов: 11
- ~teeth, ~tip (tip_point), +axe head, +blade, +cutter, +edge, +knife edge, +point (point_tip), +razor, +saw blade, +scissor blade

### TOOL STORAGE  `boxes_and_cases`
- правило: Things used to store and carry tools
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~belt, ~bucket, ~caddy, ~case (case_box), ~pouch, ~tray, +bag, +cabinet (cabinet_furniture), +chest (chest_box), +drawer, +rack, +shed, +toolbox, !pegboard

### CLEANING TOOLS  `cleaning_tools`
- правило: Tools used for cleaning and tidying
- тип связи: `used_in`, базовая сложность 0.25
- слов: 16
- ~brush, ~bucket, ~dustpan, ~plunger, ~toothbrush, +air freshener, +broom, +duster, +lint roller, +mop, +rag, +sponge (sponge_cleaning), +steam cleaner, +vacuum, !scrubber, !squeegee

### CUTTING TOOLS  `cutting_tools`
- правило: Tools used to cut material
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~chisel, ~cleaver, ~clipper, +blade, +box cutter, +guillotine, +hedge trimmer, +knife, +lawnmower, +machete, +razor, +saw, +scalpel, +scissors, +shears, +wire cutter

### FASTENERS  `fasteners`
- правило: Small parts used to hold things together
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~anchor, ~bolt, ~bracket, ~buckle, ~clamp, ~clip, ~hinge, ~hook (hook_fastener), ~nail (nail_metal), ~nut (nut_metal), ~pin (pin_fastener), ~washer, +rivet, +screw, +staple, +tack (tack_pin), +velcro, +zip tie

### GARDEN TOOLS  `garden_tools`
- правило: Tools used for gardening and yard work
- тип связи: `used_in`, базовая сложность 0.25
- слов: 20
- ~clippers, ~gloves, ~pitchfork, ~sprinkler, ~trowel, ~watering can, +hoe, +hose, +lawnmower, +leaf blower, +rake, +shears, +shovel, +spade (spade_tool), +wheelbarrow, !cultivator, !edger, !pruner, !seeder, !weeder

### HAND TOOLS  `hand_tools`
- правило: Tools held in the hand and used for building or repair work
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~file (file_tool), ~knife, ~level, ~plane (plane_tool), ~punch (punch_tool), ~socket (socket_tool), ~square, ~stapler, +chisel, +clamp, +crowbar, +drill (drill_tool), +hammer, +mallet, +pliers, +ratchet, +sander, +saw, +scraper, +screwdriver, +screwgun, +tape measure, +vise, +wrench, !awl

### KITCHEN GADGETS  `kitchen_gadgets`
- правило: Small specialized gadgets used in a kitchen
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~funnel, ~strainer, ~thermometer, ~timer, +can opener, +corkscrew, +egg slicer, +garlic press, +melon baller, +pizza cutter, +scoop, !baster, !peeler, !sifter, !tenderizer, xzester

### MEASURING TOOLS  `measuring_tools`
- правило: Tools used to measure size, weight or amount
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~barometer, ~compass, ~level, ~odometer, ~protractor, ~stopwatch, ~thermometer, +caliper, +gauge, +measuring cup, +meter, +ruler, +scale, +speedometer, +tape measure, +yardstick

### OFFICE SUPPLIES  `office_supplies`
- правило: Small items kept in an office desk and used for paperwork
- тип связи: `found_in`, базовая сложность 0.15
- слов: 25
- ~calculator, ~envelope, ~highlighter, ~label, ~paperclip, ~planner, ~rubber band, ~ruler, ~stamp (stamp_tool), ~sticky note, ~tape, +binder, +calendar, +clip, +eraser, +folder, +hole punch, +ink, +marker, +notepad, +pen (pen_writing), +pencil, +scissors, +stapler, !whiteout

### PAINTING SUPPLIES  `painting_supplies`
- правило: Things used to paint a wall or a picture
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- ~brush, ~ladder, ~roller, ~sponge (sponge_cleaning), ~tape, ~tray, +canvas, +drop cloth, +easel, +paint, +palette, +primer, +smock, +spray can, +stencil, +thinner

### POWER TOOLS  `power_tools`
- правило: Tools driven by electricity or a motor
- тип связи: `is_a`, базовая сложность 0.25
- слов: 16
- ~buffer, ~drill (drill_tool), ~grinder, ~jackhammer, ~jigsaw, ~router, +air compressor, +blower, +chainsaw, +impact driver, +nail gun, +sander, +saw, +table saw, +welder, !planer

### SAFETY GEAR  `safety_gear`
- правило: Equipment worn to stay safe while working
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~apron (apron_garment), ~boots, ~goggles, ~harness, ~helmet, ~mask, ~vest, +earplugs, +face shield, +gloves, +hard hat, +knee pads, +respirator, !ear muffs

### SEWING SUPPLIES  `sewing_supplies`
- правило: Items used for sewing and mending clothes
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~bobbin, ~button (button_clothing), ~elastic, ~hook (hook_fastener), ~scissors, ~snap, ~yarn, ~zipper, +hem, +needle (needle_sewing), +patch, +pattern, +pin (pin_fastener), +seam ripper, +tape measure, +thimble, +thread, !pincushion

### MEASURING UNITS  `things_measured_in_inches`
- правило: Units used to measure length, weight or volume
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~acre, ~cup, ~foot (foot_measure), +fathom, +gallon, +gram, +inch, +kilometer, +liter, +meter, +mil, +mile, +ounce, +pint, +pound (pound_weight), +quart, +tablespoon, +teaspoon, +ton, +yard (yard_measure)

### SHARP THINGS  `things_that_cut`
- правило: Everyday things with a sharp edge or point
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~arrow, ~blade, ~dart (dart_throw), ~knife, ~nail (nail_metal), ~needle (needle_sewing), ~pin (pin_fastener), ~razor, ~saw, ~scissors, ~spear, ~splinter, ~sword, ~tack (tack_pin), ~thorn, !glass shard, !hook (hook_fastener), !ice pick

### SPINNING THINGS  `things_that_spin`
- правило: Everyday things that spin or rotate
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~dryer, ~fan (fan_device), ~gear, ~globe, ~propeller, ~tire, ~top (top_spin), ~washing machine, ~wheel, ~windmill, !blender, !carousel, !ceiling fan, !coin, !dial, !drill (drill_tool), !record, !turbine

### HAMMERED THINGS  `things_that_stick_out`
- правило: Things a hammer is normally used on
- тип связи: `does_action`, базовая сложность 0.4
- слов: 13
- ~chisel, ~dent, ~horseshoe, ~nail (nail_metal), ~Peg, ~spike, ~stake, ~tack (tack_pin), ~wedge, !bolt, !post (post_pole), !rivet, !tent stake

### THINGS WITH HANDLES  `things_with_handles`
- правило: Everyday objects gripped by a handle
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~axe, ~basket, ~briefcase, ~bucket, ~door, ~drawer, ~hammer, ~kettle, ~knife, ~mug, ~pan, ~pitcher (pitcher_jug), ~purse, ~racket, ~shovel, ~suitcase, !broom, !umbrella

### WORKSHOP THINGS  `workshop_things`
- правило: Things found in a home workshop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~apron (apron_garment), ~bucket, ~drill (drill_tool), ~goggles, ~grinder, ~hammer, ~nail (nail_metal), ~shelf (shelf_furniture), +clamp, +extension cord, +lumber, +oil can, +sandpaper, +sawdust, +toolbox, +vise, +workbench, !pegboard


## Тема: trades

### AUTO REPAIR  `auto_repair`
- правило: Things a mechanic works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 17
- ~battery, ~belt, ~hose, ~lift, ~oil (oil_motor), ~tire iron, ~wrench, +alternator, +brake pad, +coolant, +diagnostic, +filter, +gasket, +jack (jack_tool), +radiator, +spark plug, +transmission

### BAKERY WORDS  `baker_words`
- правило: Things found in a bakery
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~icing, ~rack, ~scale, ~timer, ~tray, +apron (apron_garment), +cooling rack, +display case, +dough, +flour, +mixer, +oven, +pastry bag, +tongs, !proofer

### BARBERSHOP WORDS  `barbershop_words`
- правило: Things found in a barbershop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- ~apron (apron_garment), ~cape, ~chair, ~mirror, ~pole, ~powder, ~razor, ~scissors, ~towel, +brush, +clippers, +comb, +shaving cream, +trimmer

### BUTCHER SHOP  `butcher_words`
- правило: Things found in a butcher shop
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~apron (apron_garment), ~block (block_cube), ~brisket, ~case (case_box), ~cleaver, ~cut, ~freezer, ~rack, ~sausage, ~saw, ~scale, ~twine, ~wrap, +grinder

### CARPENTRY WORDS  `carpentry_words`
- правило: Things a carpenter works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~beam (beam_wood), ~chisel, ~groove, ~level, ~lumber, ~plane (plane_tool), ~plywood, ~square, ~stud, +molding, +nail gun, +rafter, +shim, +veneer, !dovetail, !joist, !miter, !sawhorse

### JANITORIAL WORDS  `cleaning_trade`
- правило: Things a janitor uses at work
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~bucket, ~buffer, ~cart, ~dustpan, ~gloves, ~keys, ~sign, ~uniform, ~wax (wax_polish), +broom, +disinfectant, +mop, +trash bag, +vacuum, !squeegee

### ELECTRICAL WORDS  `electrical_words`
- правило: Things an electrician works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~breaker, ~cable, ~ground, ~panel, ~terminal, +amp, +conduit, +fuse, +insulation, +junction box, +outlet, +socket (socket_electric), +switch, +transformer, +voltage, +wire

### FACTORY WORDS  `factory_words`
- правило: Things found in a factory
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~assembly line, ~crate, ~foreman, ~mold (mold_form), ~press (press_machine), ~robot, ~shift (shift_work), ~uniform, ~whistle, +conveyor, +machine, +quality control, +safety goggles, xtimeclock

### LANDSCAPING WORDS  `landscaping_words`
- правило: Things a landscaper works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~edger, ~gravel, ~planter, ~seed, ~shears, ~sprinkler, ~stake, ~trimmer, ~wheelbarrow, +blower, +fertilizer, +hedge, +mower, +mulch, +sod

### LOCKS & KEYS  `locksmith_words`
- правило: Things involved with locks and keys
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~chain, ~cylinder, ~tumbler, +bolt, +combination, +hinge, +key, +keyhole, +keypad, +latch, +lock, +master key, +padlock, +safe, !deadbolt

### MASONRY WORDS  `masonry_words`
- правило: Things a mason works with
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~block (block_cube), ~brick, ~cement, ~chisel, ~grout, ~mortar, ~stone, ~trowel, ~wheelbarrow, !hod, !joint, !level, !plumb line, !scaffold

### HOUSE PAINTING  `painting_trade`
- правило: Things a house painter uses
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~brush, ~ladder, ~putty, ~roller, ~sandpaper, ~scraper, ~tape, ~tray, +drop cloth, +extension pole, +primer, +sprayer, +stir stick, !caulk

### PLUMBING WORDS  `plumbing_words`
- правило: Things a plumber works with
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~elbow, ~fitting, ~snake, ~solder, ~spigot, ~trap, ~washer, ~wrench, +coupling, +drain, +faucet, +flange, +gasket, +pipe (pipe_tube), +plunger, +sewer, +sink (sink_basin), +valve

### PRINTING WORDS  `printing_words`
- правило: Things used in printing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~cartridge, ~font, ~ink, ~paper, ~press (press_machine), ~screen (screen_print), ~stencil, ~toner, ~type, !binding, !plate, !proof, !registration, !roller

### ROOFING WORDS  `roofing_words`
- правило: Things used in roofing a house
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~felt, ~gutter, ~ladder, ~shingle, ~tile, !drip edge, !flashing, !harness, !nail gun, !ridge, !tar, !underlayment, !valley, !vent

### TAILOR SHOP  `tailor_words`
- правило: Things a tailor uses
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bobbin, ~chalk (chalk_tailor), ~iron (iron_appliance), ~shears, +hem, +machine, +mannequin, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam ripper, +tape measure, +thimble, +thread

### WAREHOUSE WORDS  `warehouse_words`
- правило: Things found in a warehouse
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~aisle, ~box, ~crate, ~dock, ~forklift, ~label, ~pallet, ~ramp, ~scanner, ~shelf (shelf_furniture), +conveyor, +hand truck, +inventory, +tape gun

### WELDING WORDS  `welding_words`
- правило: Things used in welding metal
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~clamp, ~rod, ~spark, ~tack (tack_pin), ~torch, !apron (apron_garment), !arc, !bead, !filler, !flux, !gas, !helmet, !slag, !tip (tip_point)


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


## Тема: varieties

### APPLE VARIETIES  `apple_varieties`
- правило: Varieties of apple sold in stores
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~empire, ~Rome, +Cortland, +Envy, +Fuji, +Gala, +Golden Delicious, +Granny Smith, +Jonathan, +McIntosh, +Pink Lady, +Red Delicious, !Braeburn, !Honeycrisp

### BEAN TYPES  `bean_types`
- правило: Kinds of bean used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~black, ~navy, ~string, +black eyed pea, +butter bean, +great northern, +kidney, +Lima, +pinto, !adzuki, !cannellini, !fava, !garbanzo, !mung

### BERRY VARIETIES  `berry_varieties`
- правило: Varieties of berry sold fresh or frozen
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- +blackberry, +blueberry, +cranberry, +currant, +gooseberry, +raspberry, +strawberry, !boysenberry, !cloudberry, !elderberry, !loganberry, xmarionberry

### SPICE BLENDS  `chili_and_spice_blends`
- правило: Mixtures of spices sold as one seasoning
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +cajun, +chili powder, +curry powder, +five spice, +italian seasoning, +jerk, +old bay, +poultry seasoning, +pumpkin spice, +ranch mix, +taco seasoning, !garam masala, !herbes de provence, !za'atar

### GRAPE VARIETIES  `grape_varieties`
- правило: Varieties of grape used for wine and eating
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +Cabernet, +Chardonnay, +Concord, +Merlot, +Muscat, +Pinot Noir, +Riesling, +Sauvignon, +Thompson, !Malbec, !Sangiovese, !Syrah, !Zinfandel

### SYRUPS AND SWEETENERS  `honey_and_syrups`
- правило: Sweet syrups and sweeteners used in food
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~treacle, +agave, +brown sugar, +cane sugar, +caramel, +corn syrup, +date syrup, +honey, +maple syrup, +molasses, +powdered sugar, +sorghum, +stevia

### SALAD GREENS  `lettuce_and_greens`
- правило: Varieties of lettuce and salad green
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~butter, ~endive, ~iceberg, ~watercress, +green leaf, +red leaf, +romaine, +spinach, !arugula, !escarole, !radicchio, xfrisee, xmesclun

### MELONS & SQUASH  `melons_and_squash`
- правило: Varieties of melon and squash
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~acorn, ~honeydew, ~pumpkin, ~spaghetti, ~zucchini, +butternut, +cantaloupe, +crookneck, +hubbard, +watermelon, !delicata, !kabocha, xcasaba

### HERB VARIETIES  `mint_and_herbs_varieties`
- правило: Varieties of mint and other kitchen herbs
- тип связи: `is_a`, базовая сложность 0.45
- слов: 13
- ~basil, ~chervil, ~cilantro, ~dill, ~oregano, ~peppermint, ~spearmint, !curly parsley, !italian parsley, !lemon balm, !marjoram, !sorrel, !thai basil

### OLIVE TYPES  `olive_types`
- правило: Varieties of olive and olive oil
- тип связи: `is_a`, базовая сложность 0.45
- слов: 12
- ~black, ~extra virgin, ~light (light_mild), ~virgin, !green (green_unripe), !kalamata, !manzanilla, !nicoise, !pitted, !spanish, !stuffed, xcastelvetrano

### PEPPER VARIETIES  `pepper_varieties`
- правило: Varieties of pepper used in cooking
- тип связи: `is_a`, базовая сложность 0.35
- слов: 13
- ~banana, ~bell, ~ghost, +Anaheim, +cayenne, +Chipotle, +jalapeno, +scotch bonnet, +serrano, !habanero, !pimento, !poblano, xshishito

### POTATO VARIETIES  `potato_varieties`
- правило: Varieties of potato sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~baby, ~purple, ~red, ~sweet potato, ~white (white_food), +idaho (idaho_potato), +new potato, +yam, +yukon gold, !fingerling, !kennebec, !russet

### RICE TYPES  `rice_types`
- правило: Kinds of rice sold in stores
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~red, ~sticky, ~sushi, ~wild, +black, +Brown, +Jasmine, +long grain, +short grain, +white (white_food), !arborio, !basmati, !parboiled

### TOMATO VARIETIES  `tomato_varieties`
- правило: Varieties of tomato
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~green (green_unripe), ~heirloom, ~vine, ~yellow, +cherry, +grape, +plum, +roma, +sun dried, !beefsteak, !campari, !san marzano


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


## Тема: world_more

### MORE COUNTRIES  `countries_more`
- правило: Countries less often named in lists
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- ~Iceland, +Albania, +Andorra, +Armenia, +Belarus, +Bhutan, +Cyprus, +Georgia, +Kazakhstan, +Latvia, +Lithuania, +Luxembourg, +Malta, +Moldova, +Monaco, +Mongolia, +Nepal, +Slovenia, +Ukraine, +Uzbekistan

### ISLAND NATIONS  `island_nations`
- правило: Countries made up of islands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~Jamaica, +Bahrain, +Cuba, +Cyprus, +Fiji, +Iceland, +Indonesia, +Japan, +Madagascar, +Maldives, +Malta, +Mauritius, +Philippines, +Seychelles, +Sri Lanka

### TROPICAL BIRDS  `tropical_birds`
- правило: Colorful birds of tropical regions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~toucan, +bird of paradise, +cockatoo, +flamingo, +hummingbird, +kingfisher, +parrot, !hornbill, !lorikeet, !macaw, !motmot, !quetzal, !sunbird

### TROPICAL FLOWERS  `tropical_flowers`
- правило: Flowers that grow in tropical places
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +bird of paradise, +ginger flower, +hibiscus, +Jasmine, +lotus, +orchid, !anthurium, !bougainvillea, !frangipani, !heliconia, !plumeria, !protea

### WORLD BREAKFAST  `world_breakfasts`
- правило: Breakfast foods eaten in other countries
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~croissant, ~pastry, ~porridge, ~tamale, !arepa, !cheese plate, !churro, !congee, !dim sum, !flatbread, !fruit plate, !full english, !miso soup, !shakshuka

### WORLD REGIONS  `world_deserts_and_seas`
- правило: Named regions of the world
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~Alps, ~Amazon, ~Outback, ~Sahara, +Andalusia, +Balkans, +Bavaria, +Caribbean, +Himalaya, +mediterranean, +Patagonia, +Riviera, +Scandinavia, +Siberia, +Tuscany

### TRADITIONAL FOOTWEAR  `world_hats_and_dress`
- правило: Traditional shoes from world cultures
- тип связи: `is_a`, базовая сложность 0.5
- слов: 10
- ~clog, ~sandal, !babouche, !geta, !huarache, !jutti, !moccasin, !sabot, xespadrille, xmukluk

### MARKET WORDS  `world_markets`
- правило: Things found at an open air market
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~basket, ~cash, ~crate, ~crowd, ~produce, ~sample, ~scale, ~sign, ~spice, ~stall (stall_market), ~vendor, +awning, +canopy, +cart, +haggling

### WORLD SOUPS  `world_soups`
- правило: Soups from cuisines around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~ramen, +avgolemono, +egg drop, +harira, +miso, +pho, +tom yum, !borscht, !caldo, !gazpacho, !goulash, !laksa, !minestrone, xmulligatawny

### WORLD SPORTS  `world_sports`
- правило: Sports popular outside the United States
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~sumo, +badminton, +bandy, +cricket, +curling, +futsal, +handball, +hurling, +netball, +rugby, +table tennis, !kabaddi, !pelota, xsepak takraw

### TRADITIONAL DRINKS  `world_teas_and_drinks`
- правило: Traditional drinks from world cultures
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~cider, ~rum, ~sake, ~tequila, ~vodka, ~Whiskey, !aquavit, !horchata, !kvass, !lassi, !matcha, !mead, !ouzo, !sangria, !yerba mate

### WORLD TRANSPORT  `world_transport`
- правило: Ways people get around in other countries
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- ~bicycle, ~camel, ~gondola, ~moped, ~sled, ~tram, +cable car, +canoe, +double decker, +ferry, +rickshaw, !funicular, !jeepney, !tuk tuk

