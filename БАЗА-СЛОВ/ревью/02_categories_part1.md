# Категории, часть 1 из 4

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
- слов: 17
- ~breastbone, ~digits, ~tailbone, +ankle bone, +collarbone, +femur, +hip bone, +jawbone, +kneecap, +pelvis, +rib, +shin bone, +shoulder blade, +skull, +spine, +vertebra, +wrist bone

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
- слов: 18
- ~crown (crown_royal), ~hood (hood_garment), +baseball cap, +beanie, +beret, +bonnet, +bowler, +cap, +cowboy hat, +fedora, +hard hat, +headband, +helmet, +sombrero, +sun hat, +top hat, +turban, +visor

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

### WARDROBE  `wardrobe`
- правило: What hangs, sits or is stored in the place you keep clothes
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- ~mothball, +accessories, +closet, +footwear, +hanger, +hats, +sleepwear

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

### CLASSIC GAMES  `card_and_dice_games`
- правило: Classic games played for generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~charades, ~hopscotch, ~horseshoes, +badminton, +checkers, +chess, +croquet, +dominoes, +hide and seek, +jacks, +jump rope, +marbles, +tag (tag_game), !tiddlywinks

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

### OPPOSITES  `opposites`
- правило: Words commonly taught as opposites
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~cold (cold_temperature), ~hot (hot_temperature), +big, +dark, +day, +down, +dry, +empty, +far, +fast, +full, +hard, +high, +in, +light (light_bright), +low, +near, +night, +open, +out, +shut, +slow, +small, +soft, +up, +wet

### PLAYGROUND GAMES  `playground_games`
- правило: Games children play at recess
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~hopscotch, ~kickball, +capture the flag, +dodgeball, +duck duck goose, +four square, +freeze tag, +hide and seek, +hot potato, +jump rope, +marbles, +red rover, +simon says, !tag (tag_game)

### NUMBER WORDS  `superstition_numbers`
- правило: Words for numbers and counting
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~quarter (quarter_fourth), ~score (score_twenty), +billion, +couple, +dozen, +eight, +few, +five, +four, +half, +hundred, +million, +nine, +one, +pair, +seven, +single (single_one), +six, +ten, +thousand, +three, +twenty, +two, +zero

### TRADITIONAL CLOTHING  `traditional_clothing`
- правило: Traditional garments from world cultures
- тип связи: `is_a`, базовая сложность 0.4
- слов: 15
- +kilt, +kimono, +poncho, +sari, +sombrero, +toga, +turban, !dashiki, !dirndl, !hanbok, !kaftan, !kente, !lederhosen, !moccasin, !sarong

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
- слов: 12
- ~bifocals, +blindfold, +contacts, +glasses, +goggles, +mask, +monocle, +reading glasses, +safety glasses, +shades, +sunglasses, +visor

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
- слов: 18
- ~chignon, ~cornrows, ~topknot, ~updo, +afro, +bangs, +beehive, +bob, +braid, +bun, +crew cut, +dreadlocks, +layers, +mohawk, +perm, +pigtails, +pixie, +ponytail

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


## Тема: nature_more

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


## Тема: science

### HUMAN BIOLOGY  `body_science`
- правило: Scientific words about how the human body works
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~artery, ~blood, ~bone, ~cell (cell_body), ~dna, ~enzyme, ~gene, ~hormone, ~immunity, ~membrane, ~metabolism, ~muscle, ~nerve, ~organ (organ_body), ~oxygen, ~plasma, ~protein, ~tissue (tissue_body)

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
- слов: 20
- ~mercury (mercury_metal), +aluminum, +brass, +bronze, +chrome, +cobalt, +copper, +gold, +iron (iron_metal), +lead (lead_metal), +magnesium, +nickel, +pewter, +platinum, +silver, +steel, +tin (tin_metal), +titanium, +tungsten, +zinc

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

### SHAPES  `shapes`
- правило: Geometric shapes taught in school
- тип связи: `is_a`, базовая сложность 0.15
- слов: 20
- ~diamond (diamond_shape), ~pyramid (pyramid_shape), +arch (arch_structure), +circle, +cone, +crescent, +cube, +cylinder, +heart (heart_shape), +hexagon, +octagon, +oval, +Pentagon, +prism, +rectangle, +sphere, +Square, +star (star_shape), +trapezoid, +triangle

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

### ASTRONOMY WORDS  `things_in_the_sky_science`
- правило: Words used by astronomers
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +atmosphere, +comet, +constellation, +crater, +eclipse, +galaxy, +gravity, +light year, +meteor shower, +orbit, +phase, +rotation, +satellite, +solar system, +telescope, +universe

### WEATHER SCIENCE  `weather_science`
- правило: Scientific words used to describe weather
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~updraft, +air mass, +barometer, +condensation, +dew point, +evaporation, +forecast, +front, +humidity, +jet stream, +precipitation, +pressure, +radar, !isobar


## Тема: species

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
- слов: 18
- ~aioli, ~bechamel, ~chimichurri, +alfredo, +barbecue, +curry, +gravy, +hollandaise, +marinade, +marinara, +pesto, +ranch, +roux, +salsa, +soy, +tartar, +teriyaki, +vinaigrette

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

