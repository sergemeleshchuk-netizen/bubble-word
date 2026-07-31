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


## Тема: animals

### AFRICAN ANIMALS  `african_animals`
- правило: Wild animals associated with the African savanna
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~meerkat, ~warthog, +antelope, +baboon, +buffalo, +cheetah, +crocodile, +elephant, +gazelle, +giraffe, +hippo, +hyena, +leopard, +lion, +mongoose, +ostrich, +rhino, +vulture, +wildebeest, +zebra

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

### DOG BREEDS  `dog_breeds`
- правило: Breeds of domestic dog recognized by an average American
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +beagle, +boxer, +bulldog, +chihuahua, +collie, +corgi, +dachshund, +dalmatian, +doberman, +greyhound, +husky, +labrador, +mastiff, +poodle, +pug, +retriever, +rottweiler, +shepherd, +spaniel, +terrier

### EXTINCT ANIMALS  `extinct_animals`
- правило: Extinct animals and animal groups people recognize by name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~megalodon, ~pterodactyl, ~stegosaurus, ~trilobite, ~velociraptor, +brontosaurus, +dinosaur, +dodo, +mammoth, +mastodon, +raptor, +saber tooth, +triceratops, +tyrannosaurus

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
- слов: 20
- ~cockatiel, +canary, +cat, +chinchilla, +dog, +ferret, +gerbil, +goldfish, +guinea pig, +hamster, +hedgehog, +iguana, +lizard, +mouse (mouse_animal), +parakeet, +parrot, +pony, +rabbit, +snake, +turtle

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

### POTTERY WORDS  `pottery_words`
- правило: Things used in making pottery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bowl, ~clay, ~fire, ~glaze, ~kiln, ~mold (mold_form), ~plaster, ~pot, ~sculpt, ~slip, ~tile, ~vase, ~wheel, !trim (trim_cut)

### SCULPTURE MATERIALS  `sculpture_materials`
- правило: Materials sculptors carve or cast
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~soapstone, +bronze, +clay, +concrete, +glass, +granite, +ice, +marble (marble_stone), +metal, +plaster, +sand, +stone, +wax (wax_substance), +wood

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

### NURSERY RHYMES  `nursery_rhymes`
- правило: Nursery rhymes American children learn
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Humpty Dumpty, ~Itsy Bitsy Spider, +Baa Baa Black Sheep, +Jack and Jill, +Little Bo Peep, +London Bridge, +Mary Had a Little Lamb, +Old MacDonald, +Row Your Boat, +Three Blind Mice, +Twinkle Twinkle, !Hickory Dickory Dock

### RADIO WORDS  `radio_words`
- правило: Things and roles in radio broadcasting
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~station (station_place), +antenna, +broadcast, +call sign, +dial, +DJ, +frequency, +jingle, +playlist, +static, +studio, +transmitter, +tuner, !airwave, !host (host_presenter)

### SHAKESPEARE PLAYS  `shakespeare_plays`
- правило: Plays written by Shakespeare
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +As You Like It, +Hamlet, +Julius Caesar, +King Lear, +Macbeth, +Merchant of Venice, +Midsummer Night, +Much Ado, +othello, +Richard III, +Romeo and Juliet, +Taming of the Shrew, +Tempest, +Twelfth Night

### SUPERHEROES  `superheroes`
- правило: Comic book superheroes most people can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +Ant Man, +Aquaman, +Batman, +Black Widow, +Captain America, +Daredevil, +flash, +Green Lantern, +Hulk, +Iron Man, +robin, +Spiderman, +storm, +Supergirl, +Superman, +Thor, +wolverine, +Wonder Woman

### TV GENRES  `tv_genres`
- правило: Kinds of television program
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +cartoon, +cooking show, +crime show, +documentary, +drama, +game show, +mini series, +news, +reality, +sitcom, +soap opera, +sports, +talent show, +talk show, +variety show


## Тема: medicine

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

### FIRST AID  `first_aid`
- правило: Things kept in a first aid kit
- тип связи: `used_in`, базовая сложность 0.25
- слов: 17
- +antiseptic, +aspirin, +bandage, +burn cream, +cotton ball, +eye wash, +gauze, +gloves, +ice pack, +ointment, +scissors, +sling, +splint, +tape, +thermometer, +tweezers, +wipe

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
- слов: 16
- +Capella, +Castor, +constellations, +Polaris, +Sirius, +Vega, !Aldebaran, !Altair, !Antares, !Arcturus, !Betelgeuse, !Deneb, !Pollux, !Procyon, !Rigel, !Spica

### CONSTELLATIONS  `constellations`
- правило: Constellations in the night sky
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- ~Cassiopeia, +Andromeda, +Big Dipper, +Crux, +Cygnus, +Draco, +Hercules, +Little Dipper, +Lyra, +Orion, +pegasus, +Perseus, +Ursa Major, +Ursa Minor, !Centaurus

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


## Тема: sports

### BASEBALL EQUIPMENT  `baseball_equipment`
- правило: Physical equipment used to play a game of baseball
- тип связи: `used_in`, базовая сложность 0.25
- слов: 15
- ~ball (ball_sphere), +base, +bat (bat_equipment), +batting glove, +cap, +chest protector, +cleats, +glove, +helmet, +mask, +mitt, +pine tar, +plate (plate_base), +rosin bag, +shin guard

### BASEBALL WORDS  `baseball_words`
- правило: Words used to describe plays, places or roles in a baseball game
- тип связи: `found_in`, базовая сложность 0.3
- слов: 27
- ~diamond (diamond_field), +bullpen, +bunt, +catcher, +curveball, +double play, +dugout, +error, +fastball, +foul, +grand slam, +home run, +infield, +inning, +lineup, +mound (mound_baseball), +outfield, +pitch (pitch_throw), +pitcher (pitcher_baseball), +shortstop, +slider, +steal, +strike (strike_baseball), +triple, +umpire, +walk, !single (single_baseball)

### BASKETBALL WORDS  `basketball_words`
- правило: Words used to describe plays and roles in basketball
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~court (court_sport), ~guard (guard_sport), +assist, +backboard, +buzzer, +center, +dribble, +dunk (dunk_basketball), +forward, +foul, +free throw, +hoop, +jump ball, +layup, +rebound, +three pointer, +timeout, +travel, !block (block_stop), !screen (screen_basketball)

### GAMES OF SKILL  `board_and_card_games`
- правило: Competitive indoor games of skill
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~backgammon, ~bridge (bridge_card), ~cornhole, ~foosball, ~shuffleboard, +air hockey, +billiards, +bowling, +checkers, +chess, +darts, +dominoes, +poker, +table tennis

### OUTDOOR ACTIVITIES  `camping_and_outdoors`
- правило: Recreational activities done outdoors
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~birdwatching, ~geocaching, ~picnicking, +backpacking, +biking, +camping, +canoeing, +climbing, +fishing, +hiking, +hunting, +kayaking, +rafting, +running, +sailing, +skiing, +snorkeling, +surfing

### CYCLING WORDS  `cycling_words`
- правило: Words used about riding and racing bicycles
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +brake, +cadence, +chain, +drafting, +gear, +handlebar, +helmet, +jersey, +pedal, +peloton, +saddle, +spoke, +sprint, +tire, +tour, +trail

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
- слов: 18
- ~bunker (bunker_golf), ~green (green_golf), ~iron (iron_golf), +birdie, +bogey, +caddy, +course, +driver, +eagle, +fairway, +flag, +hole in one, +par, +putter, +rough, +sand trap, +tee, +wedge

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

### WINTER SPORTS  `winter_sports`
- правило: Sports played on snow or ice
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~bobsled, ~snowshoeing, ~tobogganing, +biathlon, +curling, +figure skating, +hockey, +ice climbing, +luge, +skating, +skiing, +sledding, +snowboarding, +speed skating


## Тема: sports_world

### ARCHERY WORDS  `archery_words`
- правило: Words used in archery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~nock, ~range (range_shooting), +arm guard, +arrow, +bow (bow_weapon), +bullseye, +draw, +quiver, +release, +shaft, +sight, +string, +Target, !fletching

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

