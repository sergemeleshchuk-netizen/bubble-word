# Категории, часть 3 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

