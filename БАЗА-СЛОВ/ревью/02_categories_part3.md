# Категории, часть 3 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

### ARCTIC ANIMALS  `arctic_animals`
- правило: Animals that live in the Arctic north
- тип связи: `found_in`, базовая сложность 0.25
- слов: 17
- ~lemming, ~narwhal, ~ptarmigan, +arctic fox, +beluga, +caribou, +husky, +moose, +musk ox, +orca, +polar bear, +puffin, +reindeer, +seal (seal_animal), +snowy owl, +walrus, +wolverine

### BIRDS  `birds`
- правило: Bird species an average American can name
- тип связи: `is_a`, базовая сложность 0.12
- слов: 26
- +blue jay, +canary, +cardinal (cardinal_bird), +chicken, +crane (crane_bird), +crow, +duck (duck_bird), +eagle, +falcon, +flamingo, +goose, +hawk, +ostrich, +owl, +parrot, +peacock, +pelican, +penguin, +pigeon, +raven, +robin, +seagull, +sparrow, +swan, +turkey (turkey_bird), +woodpecker

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
- слов: 20
- ~aphid, +ant, +flea, +gopher, +mole (mole_animal), +mosquito, +moth, +mouse (mouse_animal), +pigeon, +raccoon, +rat, +roach, +slug, +snail, +termite, +tick (tick_bug), +wasp, +weevil, !bedbug, !silverfish

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
- слов: 18
- ~skink, ~terrapin, +alligator, +anaconda, +boa, +chameleon, +cobra, +crocodile, +gecko, +iguana, +lizard, +python, +rattlesnake, +snake, +tortoise, +turtle, +viper, !monitor (monitor_lizard)

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


## Тема: body

### BODY MOVEMENTS  `body_movements`
- правило: Movements the human body makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- +bend, +blink, +breathe, +clap, +cough, +crouch, +jump, +kick, +lean, +nod, +shiver, +shrug, +sneeze, +stretch, +twist, +wave (wave_hand), +wink, +yawn, !point (point_gesture), !swallow (swallow_throat)

### BODY PARTS  `body_parts`
- правило: External parts of the human body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 25
- ~calf (calf_leg), +ankle, +arm, +back, +chest (chest_body), +chin, +elbow, +finger, +foot (foot_body), +forehead, +hand (hand_body), +head (head_body), +heel, +hip, +jaw, +knee, +leg, +neck, +shin, +shoulder (shoulder_body), +stomach, +thigh, +toe, +waist, +wrist

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
- слов: 16
- ~breastbone, ~tailbone, +ankle bone, +collarbone, +femur, +hip bone, +jawbone, +kneecap, +pelvis, +rib, +shin bone, +shoulder blade, +skull, +spine, +vertebra, +wrist bone

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
- слов: 18
- ~chickenpox, ~cold (cold_illness), +allergy, +arthritis, +asthma, +bronchitis, +diabetes, +fever, +flu, +infection, +measles, +migraine, +mumps, +pneumonia, +rash, +sinusitis, +strep throat, +ulcer

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
- слов: 14
- +brisk, +creeping, +fast, +gradual, +hasty, +leisurely, +quick, +rapid, +slow, +sluggish, +speedy, +steady, +sudden, +swift

### STRENGTH WORDS  `strength_words`
- правило: Words describing strength
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +brittle (brittle_property), +delicate, +durable, +feeble, +flimsy, +fragile, +frail, +mighty, +robust, +solid (solid_strong), +strong, +sturdy, +tough, +weak

### TASTE WORDS  `taste_words`
- правило: Words describing how food tastes
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +bitter, +bland, +buttery, +creamy, +crisp, +hearty, +mild, +nutty, +peppery, +rich, +salty, +savory, +smoky, +sour, +spicy, +sweet, +syrupy, +tangy, +tart, +zesty

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


## Тема: food_more

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
- слов: 12
- ~baked ziti, ~carbonara, ~primavera, ~puttanesca, +alfredo, +bolognese, +lasagna, +mac and cheese, +marinara, +pesto pasta, +spaghetti and meatballs, xcacio e pepe

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
- слов: 25
- ~delta (delta_river), +basin, +butte, +canyon, +cave, +cliff, +crater, +dune, +foothill, +glacier, +gorge, +hill, +island, +isthmus, +marsh, +mesa, +mountain, +peninsula, +plain, +plateau, +prairie, +ridge, +summit, +tundra, +valley

### LATIN AMERICA  `latin_american_countries`
- правило: Countries of Central and South America
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +Argentina, +Belize, +Bolivia, +Brazil, +Chile, +Colombia, +Costa Rica, +Cuba, +Ecuador, +Guatemala, +Honduras, +Mexico, +Nicaragua, +panama, +Paraguay, +Peru, +Uruguay, +Venezuela

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
- слов: 20
- +backpack, +bug spray, +camp chair, +canteen, +compass, +cooler, +firewood, +first aid kit, +flashlight, +hatchet, +lantern, +map, +matches, +mess kit, +rope, +sleeping bag, +stove, +tarp, +tent, +thermos

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

### CLEANING SUPPLIES  `cleaning_supplies`
- правило: Tools and products used to clean a house
- тип связи: `used_in`, базовая сложность 0.2
- слов: 20
- ~scrubber, ~squeegee, +bleach, +broom, +brush, +bucket, +cleanser, +detergent, +disinfectant, +duster, +dustpan, +gloves, +mop, +polish (polish_product), +rag, +soap, +sponge (sponge_cleaning), +trash bag, +vacuum, +wipes

### DISHES  `dishes_and_glassware`
- правило: Things you eat and drink from at a table
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~carafe, ~ramekin, +bottle, +bowl, +cereal bowl, +cup, +dish, +glass, +goblet, +gravy boat, +jar, +mug, +pitcher (pitcher_jug), +plate (plate_dish), +platter, +saucer, +sugar bowl, +teapot, +tray, +tumbler

### HOME TEXTILES  `fabrics_at_home`
- правило: Cloth things used around the house
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- +apron (apron_garment), +blanket, +comforter, +curtain, +cushion cover, +doormat, +drape, +napkin, +pillowcase, +quilt, +rug, +sheet (sheet_bed), +tablecloth, +throw, +towel, !dishcloth, !placemat

### FURNITURE  `furniture`
- правило: Movable household furniture
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- ~cabinet (cabinet_furniture), ~loveseat, +armchair, +bed, +bench (bench_seat), +bookshelf, +chair, +cot, +couch, +crib, +desk, +dresser, +futon, +headboard, +hutch, +nightstand, +ottoman, +recliner, +rocker, +sideboard, +sofa, +stool, +table, +vanity, +wardrobe

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

### KITCHEN TOOLS  `kitchen_tools`
- правило: Handheld tools and utensils used to prepare food in a kitchen
- тип связи: `used_in`, базовая сложность 0.15
- слов: 26
- ~masher, ~peeler, +blender, +colander, +corkscrew, +cutting board, +fork, +grater, +knife, +ladle, +measuring cup, +mixer, +opener, +pan, +plate (plate_dish), +pot, +rolling pin, +sieve, +skillet, +spatula, +spoon, +strainer, +thermometer, +timer, +tongs, +whisk

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


## Тема: space

### ASTRONAUT GEAR  `astronaut_gear`
- правило: Equipment an astronaut uses
- тип связи: `used_in`, базовая сложность 0.35
- слов: 13
- ~spacesuit, +backpack, +boot (boot_shoe), +camera, +checklist, +communicator, +glove, +helmet, +jetpack, +oxygen tank, +tether, +tool belt, +visor

### STARS  `bright_stars`
- правило: Individual stars people can name
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Capella, +Castor, +Polaris, +Sirius, +Vega, !Aldebaran, !Altair, !Antares, !Arcturus, !Betelgeuse, !Deneb, !Pollux, !Procyon, !Rigel, !Spica

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

### TELESCOPE WORDS  `telescope_words`
- правило: Parts and words used with a telescope
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~aperture, ~dome, ~eyepiece, ~filter, ~finder, ~focus (focus_lens), ~lens, ~magnification, ~mirror, ~mount, ~observatory, ~reflector, ~refractor, ~tripod


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
- слов: 25
- ~stamp (stamp_tool), ~whiteout, +binder, +calculator, +calendar, +clip, +envelope, +eraser, +folder, +highlighter, +hole punch, +ink, +label, +marker, +notepad, +paper clip, +pen (pen_writing), +pencil, +planner, +rubber band, +ruler, +scissors, +stapler, +sticky note, +tape

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
- слов: 20
- ~foot (foot_measure), +acre, +cup, +fathom, +gallon, +gram, +inch, +kilometer, +liter, +meter, +mil, +mile, +ounce, +pint, +pound (pound_weight), +quart, +tablespoon, +teaspoon, +ton, +yard (yard_measure)

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

### BARBERSHOP WORDS  `barbershop_words`
- правило: Things found in a barbershop
- тип связи: `found_in`, базовая сложность 0.3
- слов: 14
- +apron (apron_garment), +brush, +cape, +chair, +clippers, +comb, +mirror, +pole, +powder, +razor, +scissors, +shaving cream, +towel, +trimmer

### BUTCHER SHOP  `butcher_words`
- правило: Things found in a butcher shop
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~block (block_cube), +apron (apron_garment), +brisket, +cleaver, +cut, +freezer, +grinder, +rack, +sausage, +saw, +twine, +wrap, !case (case_box), !scale (scale_weigh)

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
- слов: 14
- ~chalk (chalk_tailor), +bobbin, +hem, +iron (iron_appliance), +machine, +mannequin, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam ripper, +shears, +tape measure, +thimble, +thread

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

