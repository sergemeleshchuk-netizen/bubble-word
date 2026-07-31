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
- слов: 17
- +bandicoot, +kangaroo, +koala, +opossum, +sugar glider, +tasmanian devil, +wallaby, +wombat, ?kangaroo, ?koala, ?numbat, ?quokka, ?wallaby, ?wombat, !bilby, !quokka, xnumbat

### WORK ANIMALS  `pack_animals`
- правило: Animals used to carry loads or do work
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- +alpaca, +camel, +dog, +donkey, +donkeys, +elephant, +horse, +husky, +llama, +llamas, +mule, +mules, +ox, +reindeer, +water buffalo, +yak, ?ox

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

### BELOW THE SURFACE  `below_the_surface`
- правило: What belongs to the group «Below The Surface» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +abyss, +bottom, +cavern, +trench

### BODY EXTREMITIES  `body_extremities`
- правило: What belongs to the group «Body Extremities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +ear, +finger, +nose, +toe

### BODY MOVEMENTS  `body_movements`
- правило: Movements the human body makes
- тип связи: `does_action`, базовая сложность 0.3
- слов: 20
- +bend, +blink, +breathe, +clap, +cough, +crouch, +jump, +kick, +lean, +nod, +shiver, +shrug, +sneeze, +stretch, +twist, +wave (wave_hand), +wink, +yawn, !point (point_gesture), !swallow (swallow_throat)

### BODY PAIRS  `body_pairs`
- правило: What belongs to the group «Body Pairs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +ears, +eyes, +hands, +lips

### BODY PARTS  `body_parts`
- правило: External parts of the human body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 42
- ~calf (calf_leg), +ankle, +arm, +arms, +back, +bones, +chest (chest_body), +chin, +clavicle, +ear, +elbow, +eye, +finger, +fingers, +foot (foot_body), +forehead, +hand (hand_body), +head (head_body), +heel, +hip, +jaw, +kidney, +knee, +leg, +neck, +nose, +shin, +shoulder (shoulder_body), +spine, +stomach, +thigh, +toe, +tongue, +torso, +waist, +wrist, ?ankle, ?arm, ?elbow, ?finger, ?leg, ?toe

### BODY REACTIONS  `body_reactions`
- правило: What belongs to the group «Body Reactions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +cough, +hiccup, +sneeze, +yawn

### BODY SOUNDS  `body_sounds`
- правило: Sounds the human body makes on its own
- тип связи: `does_action`, базовая сложность 0.35
- слов: 21
- ~sniffle, ~wheeze, +burp, +cough, +cry, +gasp, +growl, +grunt, +gulp, +hiccup, +laugh, +sigh, +sneeze, +snore, +whistle, +yawn, ?burp, ?hiccup, ?sneeze, ?snore, ?yawn

### BODY SYSTEMS  `body_systems`
- правило: Systems that make up the human body
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~brain, ~circulatory, ~digestive, ~endocrine, ~immune, ~lung, ~lungs, ~lymphatic, ~muscular, ~nerves, ~nervous, ~organs, ~respiratory, ~skeletal, ~urinary, ~veins, ?circulatory, ?digestive, ?endocrine, ?immune, ?muscular, ?nervous, ?skeletal, !excretory

### BODYGUARD  `bodyguard`
- правило: What belongs to the group «Bodyguard» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +escort, +protect, +strong, +vigilance

### BODYWEIGHT MOVES  `bodyweight_moves`
- правило: What belongs to the group «Bodyweight Moves» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +lunge, +plank, +squat, !pushup

### BONES  `bones`
- правило: Bones of the human skeleton
- тип связи: `is_a`, базовая сложность 0.3
- слов: 31
- ~breastbone, ~coccyx, ~digits, ~phalanges, ~scapula, ~tailbone, ~ulna, +ankle bone, +clavicle, +collarbone, +cranium, +femur, +fibula, +hip bone, +jawbone, +kneecap, +patella, +pelvis, +radius, +rib, +shin bone, +shoulder blade, +skull, +spine, +tibia, +vertebra, +wrist bone, ?femur, ?rib, ?skull, xcarpals

### BONES IN THE ARM  `bones_in_the_arm`
- правило: What belongs to the group «Bones In The Arm» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +humerus, +radius, !ulna, xcarpals

### BUSINESS SHORTHAND  `business_shorthand`
- правило: What belongs to the group «Business Shorthand» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +asap, +fyi, +nda, +url

### BUSYBODY  `busybody`
- правило: What belongs to the group «Busybody» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +intruder, +nosey, !meddler, xgossiper

### CAR BODY STYLES  `car_body_styles`
- правило: What belongs to the group «Car Body Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +coupe, +hatchback, +sedan, +wagon

### DENTIST THINGS  `dentist_things`
- правило: Things found at a dentist office
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~crown (crown_dental), +bib, +brace, +cavity, +chair, +drill (drill_tool), +filling, +floss, +mirror, +plaque, +retainer, +rinse, +suction, +toothbrush, +X-ray, !mold (mold_form)

### DISEASE  `disease`
- правило: What belongs to the group «Disease» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 7
- +asthma, +cancer, +diabetes, +epilepsy, +flu, +malaria, +measles

### EXERCISE WORDS  `exercise_words`
- правило: Movements done as physical exercise
- тип связи: `does_action`, базовая сложность 0.3
- слов: 16
- ~burpee, ~press (press_push), ~pullup, ~pushup, +crunch (crunch_exercise), +curl, +dip, +jog, +jumping jack, +lunge, +plank, +row, +sprint, +squat, +stretch, ?situp

### FACE  `face`
- правило: What belongs to the group «Face» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 10
- +brow, +cheek, +cheeks, +chin, +ear, +eye, +eyelid, +eyes, +jaw, +nose

### FACE CONTROL  `face_control`
- правило: What belongs to the group «Face Control» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +bouncer, +entry, +id, +night club

### FACE EXPRESSIONS  `face_expressions`
- правило: What belongs to the group «Face Expressions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +frown, +scowl, +smile, +wink

### FACE HAIR  `face_hair`
- правило: What belongs to the group «Face Hair» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +beard, +mustache, +sideburns, +stubble

### FACE OFF  `face_off`
- правило: What belongs to the group «Face Off» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +scuffle, +showdown, +standoff, !fracas

### FACE PARTS  `face_parts`
- правило: Parts of the human face
- тип связи: `part_of`, базовая сложность 0.12
- слов: 20
- +brow, +cheek, +chin, +dimple, +ear, +eye, +eyebrow, +eyelash, +eyelid, +forehead, +freckle, +iris, +jaw, +lash, +lip, +mouth (mouth_face), +nose, +nostril, +pupil, +temple (temple_head)

### FARMHAND  `farmhand`
- правило: What belongs to the group «Farmhand» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +farmer, +hired, +rancher, !drover

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

### HAND GESTURES  `hand_gestures`
- правило: What belongs to the group «Hand Gestures» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 5
- +clap, +fist bump, +high five, +salute, +thumbs up

### HAND PARTS  `hand_parts`
- правило: Parts of the human hand
- тип связи: `part_of`, базовая сложность 0.3
- слов: 15
- +cuticle, +finger, +fingertip, +grip, +index finger, +joint, +knuckle, +middle finger, +nail (nail_body), +palm (palm_hand), +pinky, +ring finger, +tendon, +thumb, +wrist

### HAND SIGNS  `hand_signs`
- правило: What belongs to the group «Hand Signs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +high five, +peace sign, +thumbs down, +thumbs up

### HANDBAG MATERIALS  `handbag_materials`
- правило: What belongs to the group «Handbag Materials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +canvas, +crocodile, +leather, +nylon

### HANDICRAFTS  `handicrafts`
- правило: What belongs to the group «Handicrafts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +knitting, +origami, +pottery, +sewing

### HANDLES  `handles`
- правило: What belongs to the group «Handles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 8
- +car door, +cup handle, +flush pull, +grab, +grip, +knob, +lever, +pull

### HANDYWORK  `handywork`
- правило: What belongs to the group «Handywork» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +carpentry, +knitting, +sewing, +weaving

### HARMFUL TO HEALTH  `harmful_to_health`
- правило: What belongs to the group «Harmful To Health» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +alcohol, +fast food, +insomnia, +stress

### HAS A HANDLE  `has_a_handle`
- правило: What belongs to the group «Has A Handle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +briefcase, +broom, +cup, +umbrella

### HEALTH  `health`
- правило: What belongs to the group «Health» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +clinic, +doctor, +medicine, +patient

### HEALTH CARE  `health_care`
- правило: What belongs to the group «Health Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 8
- +antibiotic, +clinic, +disease, +doctor, +hospital, +insurance, +medicine, +nurse

### HEALTH METRICS  `health_metrics`
- правило: What belongs to the group «Health Metrics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 5
- +blood pressure, +bmi, +glucose, +heart rate, +temperature

### HEALTHCARE  `healthcare`
- правило: What belongs to the group «Healthcare» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 7
- +clinic, +disease, +hospital, +laboratory, +medicine, +pharmacy, +treatment

### HEALTHY EATING  `healthy_eating`
- правило: What belongs to the group «Healthy Eating» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 10
- +diet, +fiber, +fruit, +fruits, +grains, +nuts, +salad, +supplements, +vegetables, +water

### HEALTHY HABITS  `healthy_habits`
- правило: What belongs to the group «Healthy Habits» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +nutrition, +reading, +running, +sleep

### HEALTHY LIFE  `healthy_life`
- правило: What belongs to the group «Healthy Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 8
- +diet, +discipline, +exercise, +hydration, +meditation, +nutrition, +sleep, +workout

### HEALTHY LIFESTYLE  `healthy_lifestyle`
- правило: What belongs to the group «Healthy Lifestyle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 10
- +balanced diet, +daily walk, +diet, +enough sleep, +gym, +hydration, +meditation, +mindfulness, +nutrition, +physical activity

### HEALTHY SWEETENERS  `healthy_sweeteners`
- правило: What belongs to the group «Healthy Sweeteners» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +agave nectar, +coconut sugar, +honey, +maple syrup

### HOSPITAL THINGS  `hospital_things`
- правило: Things and places found in a hospital
- тип связи: `found_in`, базовая сложность 0.25
- слов: 18
- ~monitor (monitor_medical), +ambulance, +bandage, +bed, +chart, +emergency room, +gown, +gurney, +IV, +oxygen mask, +scalpel, +scrubs, +stethoscope, +syringe, +waiting room, +ward, +wheelchair, +X-ray

### HUMAN BODY  `human_body`
- правило: What belongs to the group «Human Body» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 13
- +back, +brain, +face, +knee, +kneecap, +lungs, +muscles, +nervous system, +ribcage, +skeleton, +spine, +tendon, +wrist

### HUMAN MUSCLES  `human_muscles`
- правило: What belongs to the group «Human Muscles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +biceps, !deltoid, !gluteus, xquadricep

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

### MEDICAL  `medical`
- правило: What belongs to the group «Medical» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +biopsy, +bp monitor, +catheter, +cold compress

### MEDICAL EQUIPMENT  `medical_equipment`
- правило: What belongs to the group «Medical Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +bandage, +forceps, +scalpel, +stethoscope, +syringe, +thermometer

### MEDICAL IMAGING  `medical_imaging`
- правило: What belongs to the group «Medical Imaging» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +ct scan, +mri, +ultrasound, +x ray

### MEDICAL IMAGING METHODS  `medical_imaging_methods`
- правило: What belongs to the group «Medical Imaging Methods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +ct, +mri, +pet, +x ray

### MEDICAL SCIENCES  `medical_sciences`
- правило: What belongs to the group «Medical Sciences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +immunology, +pathology, +pharmacology, +radiology

### MEDICAL SPECIALIZATIONS  `medical_specializations`
- правило: What belongs to the group «Medical Specializations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +cardiology, +ent, +forensic medicine, !geriatrics

### MEDICAL STAFF  `medical_staff`
- правило: What belongs to the group «Medical Staff» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 5
- +anesthesiologist, +doctor, +nurse, +paramedic, +surgeon

### MEDICINE CABINET  `medicine_cabinet`
- правило: Things kept in a home medicine cabinet
- тип связи: `found_in`, базовая сложность 0.25
- слов: 16
- ~antacid, ~lozenge, +alcohol, +aspirin, +bandage, +cotton swab, +cough syrup, +eye drops, +gauze, +ice pack, +ointment, +painkiller, +sunscreen, +thermometer, +tweezers, +vitamin

### MICROORGANISMS  `microorganisms`
- правило: What belongs to the group «Microorganisms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 6
- ~protozoa, +algae, +bacteria, +fungi, +virus, !archaea

### MIDDLE BODY  `middle_body`
- правило: What belongs to the group «Middle Body» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +hips, +navel, +stomach, +torso

### MUSCLE GROUPS  `muscle_groups`
- правило: What belongs to the group «Muscle Groups» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +biceps, +hamstrings, +triceps, !quadriceps

### MUSCLES  `muscles`
- правило: Muscles an average person can name
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~abs, ~bicep, ~calf (calf_leg), ~core, ~forearm, ~hamstring, ~lat, ~pectoral, ~quad, ~trap, ?abs, ?bicep, ?glute, ?hamstring, ?tricep, !delt, !deltoid, !glute, !lats, !obliques, !pec, !pecs, !quads, !tricep

### OFFHAND  `offhand`
- правило: What belongs to the group «Offhand» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +ad lib, +careless, +casually, +informal

### ORGANIC  `organic`
- правило: What belongs to the group «Organic» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +bio, +natural, +produce, +pure

### ORGANIC CHEMISTRY  `organic_chemistry`
- правило: What belongs to the group «Organic Chemistry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +amine, +ester, +ketone, !aldehyde, !alkane, !alkene, !alkyne

### ORGANIC MOLECULES  `organic_molecules`
- правило: What belongs to the group «Organic Molecules» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +carbohydrate, +enzyme, +lipid, +protein

### ORGANIZATIONAL SYSTEMS  `organizational_systems`
- правило: What belongs to the group «Organizational Systems» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +categories, +frameworks, +hierarchies, !taxonomies

### ORGANIZATIONS  `organizations`
- правило: What belongs to the group «Organizations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 5
- +clan, +eu, +guild, +house, +tribe

### ORGANIZE  `organize`
- правило: What belongs to the group «Organize» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +align, +arrange, +classify, +sort

### EYE PARTS  `parts_of_the_eye`
- правило: Parts of the human eye
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brow, ~cornea, ~eyelid, ~iris, ~lash, ~lens, ~optic nerve, ~pupil, ~retina, ~socket (socket_eye), ~tear duct, !white (white_color)

### PERSONAL ORGANIZATION  `personal_organization`
- правило: What belongs to the group «Personal Organization» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +ledger, +organize, +planner, +schedule

### PIPE ORGAN  `pipe_organ`
- правило: What belongs to the group «Pipe Organ» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +flue, +manual, +pedal, +rank

### PLAYGROUND SURFACES  `playground_surfaces`
- правило: What belongs to the group «Playground Surfaces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +bark mulch, +grass, +sand, +wood chips

### ROAD SURFACES  `road_surfaces`
- правило: What belongs to the group «Road Surfaces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +asphalt, +cobblestone, +gravel, +pitted

### SENSE ORGANS  `sense_organs`
- правило: What belongs to the group «Sense Organs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +ear, +eye, +nose, +skin

### THE SENSES  `senses_and_perception`
- правило: Ways the human body senses the world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +balance, +hearing, +hunger, +itch, +pain, +pressure, +sight, +smell, +taste, +temperature, +thirst, +touch

### SURFACE  `surface`
- правило: What belongs to the group «Surface» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +abrasive, +bumpy, +coating, +even

### SURFACE FINISH  `surface_finish`
- правило: What belongs to the group «Surface Finish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +gloss, +matte, +patina, +satin

### SYMPTOMS  `symptoms`
- правило: Signs that a person feels unwell
- тип связи: `is_a`, базовая сложность 0.3
- слов: 23
- +ache, +bruise, +chills, +congestion, +cough, +cramp, +dizziness, +fatigue, +fever, +headache, +itching, +nausea, +rash, +redness, +sneeze, +sore throat, +swelling, ?chills, ?cough, ?fatigue, ?fever, ?nausea, ?swelling

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

### THINGS YOU EAT WITH HANDS  `things_you_eat_with_hands`
- правило: What belongs to the group «Things You Eat With Hands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +burger, +pizza, +sandwich, +taco

### UNDERHANDED  `underhanded`
- правило: What belongs to the group «Underhanded» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +bluff, +cheat, +swindle, +trick

### WORLD HEALTH DAY  `world_health_day`
- правило: What belongs to the group «World Health Day» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +immune, +therapy, +vaccine, !sanitize


## Тема: brands

### AIRLINES  `airlines`
- правило: Major passenger airlines
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~delta (delta_airline), +Air France, +Alaska, +American, +British Airways, +Emirates, +Frontier, +JetBlue, +KLM, +Lufthansa, +Qantas, +Southwest, +Spirit, +United, +virgin, ?Frontier, ?Spirit, ?United

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
- слов: 18
- ~Chex, ~Froot Loops, ~kix, ~Rice Krispies, ~Trix, ~Wheaties, +Cheerios, +Cocoa Puffs, +Corn Flakes, +Frosted Flakes, +Grape Nuts, +Life, +Lucky Charms, +Raisin Bran, +Special K, +total, ?Cheerios, ?Trix

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
- слов: 24
- ~Arbys, ~Popeyes, ~Wendys, ~Whataburger, +Burger King, +checkers, +Chipotle, +Dairy Queen, +Dominos, +Five Guys, +KFC, +McDonalds, +Outback, +Panera, +Pizza Hut, +Sonic, +Subway, +Taco Bell, ?Arbys, ?Burger King, ?McDonalds, ?Sonic, ?Subway, ?Wendys

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


## Тема: entertainment

### ABANDONED  `abandoned`
- правило: What belongs to the group «Abandoned» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +derelict, +deserted, +forsaken, +neglected

### ACADEMIC DEPARTMENTS  `academic_departments`
- правило: What belongs to the group «Academic Departments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +anthropology, +geology, +philosophy, +sociology

### ACTORS  `actors`
- правило: What belongs to the group «Actors» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +denzel washington, +leonardo dicaprio, +meryl streep, +tom hanks

### AIRCRAFT PARTS  `aircraft_parts`
- правило: What belongs to the group «Aircraft Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +engines, +fuselage, +tail, +wings

### AIRSHOW  `airshow`
- правило: What belongs to the group «Airshow» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +jet, +pilot, +smoke, +stunt

### ALTERNATIVE MUSIC  `alternative_music`
- правило: What belongs to the group «Alternative Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +glam rock, +grunge, +indie, !britpop

### AMUSEMENT PARK  `amusement_park`
- правило: Rides and things found at an amusement park
- тип связи: `found_in`, базовая сложность 0.25
- слов: 22
- ~funhouse, ~teacups, ~turnstile, +arcade, +bumper car, +bumper cars, +carousel, +cotton candy, +drop tower, +ferris wheel, +log flume, +mascot, +midway, +popcorn, +prize, +ride, +roller coaster, +souvenir, +ticket (ticket_admission), +ticket booth, ?cotton candy, ?roller coaster

### ANIMATED FILMS  `animated_films`
- правило: What belongs to the group «Animated Films» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +Aladdin, +Bambi, +Cinderella, +Dumbo

### ANIMATED MOVIES  `animated_movies`
- правило: What belongs to the group «Animated Movies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 6
- +finding nemo, +Frozen, +Ice Age, +minions, +Shrek, +toy story

### ART  `art`
- правило: What belongs to the group «Art» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 13
- +brush, +canvas, +drawing, +easel, +literature, +music, +painting, +photography, +portrait, +pottery, +sculpture, +sketch, +watercolor

### ART CLASSES  `art_classes`
- правило: What belongs to the group «Art Classes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 9
- +ceramics, +drawing, +photography, +portrait, +pottery, +sculpture, +shading, +textures, +watercolor

### ART DECO ELEMENTS  `art_deco_elements`
- правило: What belongs to the group «Art Deco Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +chrome, +geometry, +gilded, +streamline

### ART FILMS  `art_films`
- правило: What belongs to the group «Art Films» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +abstract, +black and white, +slow cinema, +surrealism

### ART FORMS  `art_forms`
- правило: Forms of visual and performing art
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- +architecture, +calligraphy, +collage, +dance, +drawing, +fabric patterns, +film, +mosaic, +mural, +music, +origami, +painting, +photography, +poetry, +pottery, +printmaking, +sculpture, +theater, +weaving, ?dance, ?drawing, ?mosaic, ?music, ?painting, ?pottery, ?sculpture

### ART GALLERY  `art_gallery`
- правило: What belongs to the group «Art Gallery» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +artwork, +curator, +display, +exhibit

### ART HISTORY  `art_history`
- правило: What belongs to the group «Art History» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +baroque, +impressionism, +renaissance, +romanticism

### ART MEDIUMS  `art_mediums`
- правило: What belongs to the group «Art Mediums» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +charcoal, +clay, +pottery, +watercolor

### ART MOVEMENTS  `art_movements`
- правило: What belongs to the group «Art Movements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +impressionism, +naturalism, +surrealism, !cubism, !dadaism, !fauvism, !futurism

### ART MUSEUMS  `art_museums`
- правило: What belongs to the group «Art Museums» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Hermitage, +Louvre, +Prado, !Uffizi

### ART PERIODS  `art_periods`
- правило: What belongs to the group «Art Periods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +baroque, +modern, +renaissance, +romantic

### ART SCHOOLS  `art_schools`
- правило: What belongs to the group «Art Schools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +cooper union, +parsons, +pratt, !risd

### ART STUDIOS  `art_studios`
- правило: What belongs to the group «Art Studios» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 7
- +canvas, +darkroom, +life drawing, +paint, +pottery, +sculpt, +textile

### ARTICLE  `article`
- правило: What belongs to the group «Article» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +body, +column, +conclusion, +editor

### ARTIFICIAL INTELLIGENCE  `artificial_intelligence`
- правило: What belongs to the group «Artificial Intelligence» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 8
- +algorithm, +claude, +Gemini, +machine learning, +neural network, !chatbot, !copilot, !grok

### ARTIFICIAL MATERIALS  `artificial_materials`
- правило: What belongs to the group «Artificial Materials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +acetate, +acrylic, +nylon, !viscose

### ARTISAN CRAFTS  `artisan_crafts`
- правило: What belongs to the group «Artisan Crafts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pottery, +weaving, !blacksmithing, !woodcarving

### ARTIST  `artist`
- правило: What belongs to the group «Artist» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 10
- +actor, +brush, +canvas, +dancer, +easel, +gallery, +painter, +poet, +sculptor, +writer

### ARTIST TOOLS  `artist_tools`
- правило: What belongs to the group «Artist Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +brush, +canvas, +graphite, +stencil

### ARTS AND CRAFTS  `arts_and_crafts`
- правило: What belongs to the group «Arts And Crafts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +cross stitch, +modeling, +pottery, !macrame

### ARTS CRAFTS  `arts_crafts`
- правило: What belongs to the group «Arts Crafts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 5
- +glitter, +glue, +paint, +paper, +scissors

### ARTWORKS  `artworks`
- правило: What belongs to the group «Artworks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +art, +artists, +collage, +drawing

### AT A BIRTHDAY PARTY  `at_a_birthday_party`
- правило: What belongs to the group «At A Birthday Party» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +balloons, +cake, +candles, +streamers

### ATOMIC PARTICLES  `atomic_particles`
- правило: What belongs to the group «Atomic Particles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +electron, +neutron, +photon, +proton

### AWARD SHOWS  `award_shows`
- правило: What belongs to the group «Award Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +Emmy, +Grammy, +Oscar, +Tony

### BAND  `band`
- правило: What belongs to the group «Band» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 5
- +drummer, +drums, +guitar, +singer, +vocals

### BAND SECTIONS  `band_sections`
- правило: What belongs to the group «Band Sections» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 6
- +brass, +horns, +percussion, +rhythm, +strings, !woodwinds

### BANDS  `bands`
- правило: What belongs to the group «Bands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 5
- +abba, +Beatles, +kiss, +led zeppelin, +rush

### BAROQUE MUSIC  `baroque_music`
- правило: What belongs to the group «Baroque Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Bach, +Handel, +Vivaldi, !corelli

### BIG BAND SECTIONS  `big_band_sections`
- правило: What belongs to the group «Big Band Sections» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +brass, +reeds, +rhythm, +vocals

### BIKE PARTS  `bike_parts`
- правило: What belongs to the group «Bike Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +brake, +chain, +saddle, +spoke

### BOARD GAMES  `board_games`
- правило: Games played on a printed board with pieces
- тип связи: `is_a`, базовая сложность 0.25
- слов: 41
- ~boggle, ~candyland, ~catan, ~mancala, +backgammon, +battleship, +candy land, +card suits, +checkers, +chess, +chutes and ladders, +clue, +connect four, +dominion, +go, +Life, +monopoly, +othello, +pandemic, +risk, +scrabble, +sorry, +taboo, +trivial pursuit, +trouble, ?backgammon, ?battleship, ?checkers, ?chess, ?clue, ?Life, ?mancala, ?monopoly, ?othello, ?parcheesi, ?risk, ?scrabble, ?sorry, ?trivial pursuit, ?trouble, xparcheesi

### BOAT PARTS  `boat_parts`
- правило: What belongs to the group «Boat Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 5
- +hull, +keel, +mast, +rudder, +sails

### BOWED INSTRUMENTS  `bowed_instruments`
- правило: What belongs to the group «Bowed Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +viola, +violin, !erhu, !sarangi

### BRASS INSTRUMENTS  `brass_instruments`
- правило: What belongs to the group «Brass Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +bugle, +cornet, +french horn, +trombone, +trumpet, +tuba, !flugelhorn, !sousaphone

### BRIDGE PARTS  `bridge_parts`
- правило: What belongs to the group «Bridge Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +cable, +deck, +pier, +span

### BROADWAY MUSICALS  `broadway_musicals`
- правило: What belongs to the group «Broadway Musicals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 5
- +cats, +Chicago, +hamilton, +phantom, +wicked

### CABLE TV CHANNELS  `cable_tv_channels`
- правило: What belongs to the group «Cable Tv Channels» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +cnn, +espn, +hbo, +mtv

### CARD GAMES  `card_games`
- правило: Games played with a deck of cards
- тип связи: `is_a`, базовая сложность 0.3
- слов: 32
- ~bridge (bridge_card), ~canasta, ~cribbage, ~euchre, ~pinochle, ~whist, +ante, +blackjack, +crazy eights, +dealer, +deuce, +flush, +go fish, +hearts, +joker, +old maid, +poker, +rummy, +snap, +Solitaire, +spades, +uno, +war, ?blackjack, ?crazy eights, ?hearts, ?old maid, ?pinochle, ?poker, ?rummy, ?Solitaire, ?war

### CARD WORDS  `card_words`
- правило: Words for the cards, suits and parts of a standard deck of playing cards
- тип связи: `found_in`, базовая сложность 0.3
- слов: 22
- ~jack (jack_card), ~queen (queen_card), +Ace, +club (club_card), +cut, +deal, +deck, +diamond (diamond_card), +discard, +face card, +flush, +heart (heart_card), +joker, +king, +pair, +shuffle (shuffle_cards), +spade (spade_card), +straight, +suit (suit_card), +trump, +wild card, !hand (hand_cards)

### CARIBBEAN MUSIC  `caribbean_music`
- правило: What belongs to the group «Caribbean Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +calypso, +reggae, +soca, xsteelpan

### CARTEL  `cartel`
- правило: What belongs to the group «Cartel» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +capo, +don, +enforcer, +hitman

### CARTOGRAPHER  `cartographer`
- правило: What belongs to the group «Cartographer» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +longitude, +survey, +topographic, !mercator

### CARTOGRAPHY  `cartography`
- правило: What belongs to the group «Cartography» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 8
- +contour, +grid, +legend, +longitude, +meridian, +projection, +topology, xgraticule

### CARTOON STRIPS  `cartoon_strips`
- правило: What belongs to the group «Cartoon Strips» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +archie, +Garfield, +peanuts, !dilbert

### CELL PARTS  `cell_parts`
- правило: What belongs to the group «Cell Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +membrane, +mitochondria, +nucleus, !ribosome

### CHANDELIER PARTS  `chandelier_parts`
- правило: What belongs to the group «Chandelier Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +bulb, +chain, +crystal, +prism

### CHILDRENS TV  `childrens_tv`
- правило: What belongs to the group «Childrens Tv» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +paw patrol, +peppa pig, +Sesame Street, !bluey

### CIRCUS WORDS  `circus_words`
- правило: People, animals and objects you see at a traditional circus
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~sword swallower, +acrobat, +cannon, +clown, +cotton candy, +elephant, +juggler, +lion tamer, +net, +popcorn, +ring (ring_arena), +ringmaster, +sequin, +stilts, +tent, +tightrope, +trapeze, +unicycle

### CLASSICAL INSTRUMENTS  `classical_instruments`
- правило: What belongs to the group «Classical Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +cello, +harp, +oboe, +violin

### CLASSICAL MUSIC  `classical_music`
- правило: What belongs to the group «Classical Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 9
- +Bach, +chamber, +concerto, +hall, +maestro, +Mozart, +opera, +symphony, +violin

### CLASSICAL MUSIC FORMS  `classical_music_forms`
- правило: What belongs to the group «Classical Music Forms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +fugue, +prelude, +sonata, +waltz

### COCKPIT INSTRUMENTS  `cockpit_instruments`
- правило: What belongs to the group «Cockpit Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gyroscope, +radio, +throttle, !altimeter

### COMEDY WORDS  `comedy_words`
- правило: Words used about comedy performances
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +gag, +heckler, +improv, +joke, +one liner, +parody, +pun, +punchline, +roast, +routine, +satire, +sketch, +slapstick, +standup, +timing

### COMIC ART  `comic_art`
- правило: What belongs to the group «Comic Art» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +panel, +splash page, !inker, !letterer

### COMPASS PARTS  `compass_parts`
- правило: What belongs to the group «Compass Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +bezel, +housing, +meridian, +pivot

### COSTUME PARTY  `costume_party`
- правило: What you put on or need for a costume party
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~uniforms, +cape, +hats, +makeup, +mask, +superheroes, +wig

### CULINARY ARTS  `culinary_arts`
- правило: What belongs to the group «Culinary Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- +baking, +cooking, +cuisine, +gastronomy, +grilling, +restaurant, +steaming

### CYCLING PARTS  `cycling_parts`
- правило: What belongs to the group «Cycling Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +chain, +pedal, +saddle, +spokes

### DANCE  `dance`
- правило: What belongs to the group «Dance» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 8
- +ballet, +ballroom, +choreography, +flamenco, +partner, +salsa, +studio, !gavotte

### DANCE ROLES  `dance_roles`
- правило: What belongs to the group «Dance Roles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +corps, +principal, +soloist, +understudy

### DANCE STYLES  `dance_styles`
- правило: Styles of dance
- тип связи: `is_a`, базовая сложность 0.3
- слов: 27
- ~breakdance, +ballet, +ballroom, +cha cha, +disco, +flamenco, +folk, +foxtrot, +hip hop, +jazz, +line dance, +polka, +rumba, +salsa, +samba, +swing, +tango, +tap (tap_dance), +waltz, ?ballet, ?foxtrot, ?hip hop, ?salsa, ?samba, ?swing, ?tango, ?waltz

### DARTBOARD  `dartboard`
- правило: What belongs to the group «Dartboard» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +bullseye, +rings, +Target, +throw

### DEPARTMENTS  `departments`
- правило: What belongs to the group «Departments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +accounting, +c suite, +hr, +marketing

### DIAMOND QUALITY FACTORS  `diamond_quality_factors`
- правило: What belongs to the group «Diamond Quality Factors» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +carat, +clarity, +color, +cut

### DIGITAL ART  `digital_art`
- правило: What belongs to the group «Digital Art» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 5
- +gradient, +layer, +opacity, +palette, +vector

### DISNEY ANIMATED MOVIES  `disney_animated_movies`
- правило: What belongs to the group «Disney Animated Movies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +brave, +Frozen, +Moana, +tangled

### EARTH  `earth`
- правило: What belongs to the group «Earth» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 19
- +air, +atmosphere, +biosphere, +continent, +core, +crust, +desert, +forest, +jungle, +land, +landmass, +Life, +mantle, +mountain, +mountains, +ocean, +plowing, +tectonic plate, +water

### EARTH SCIENCES  `earth_sciences`
- правило: What belongs to the group «Earth Sciences» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +hydrology, +mineralogy, !seismology, !volcanology

### EARTH TONES  `earth_tones`
- правило: What belongs to the group «Earth Tones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ochre, +sienna, +taupe, !umber

### EARTHQUAKE  `earthquake`
- правило: What belongs to the group «Earthquake» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 5
- +fault, +magnitude, +seismic, +shake, +tremor

### EARTHQUAKE TERMS  `earthquake_terms`
- правило: What belongs to the group «Earthquake Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +aftershock, +fault, +richter, +tremor

### EAST ASIAN ARTS  `east_asian_arts`
- правило: What belongs to the group «East Asian Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +batik, +bonsai, +calligraphy, !ikebana

### ELEMENTARY PARTICLES  `elementary_particles`
- правило: What belongs to the group «Elementary Particles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +electron, +neutron, !gluon, !lepton

### FACTORY  `factory`
- правило: What belongs to the group «Factory» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +chimney, +conveyor, +machines, +workers

### FAMOUS ARTISTS  `famous_artists`
- правило: What belongs to the group «Famous Artists» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +banksy, +Monet, +Warhol, !klimt

### COMPOSERS  `famous_composers`
- правило: Famous classical composers
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Bach, +Beethoven, +Brahms, +Chopin, +Debussy, +Handel, +Haydn, +Liszt, +Mozart, +Schubert, +Tchaikovsky, +Verdi, +Vivaldi, +Wagner

### FAMOUS SINGERS  `famous_singers`
- правило: What belongs to the group «Famous Singers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 4
- +Jackson, +John, +Presley, +price

### MYTHICAL CREATURES  `fantasy_creatures`
- правило: Creatures from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- +centaur, +dragon, +elf, +fairy, +giant, +gnome, +goblin, +griffin, +kraken, +mermaid, +minotaur, +ogre, +pegasus, +phoenix (phoenix_bird), +sphinx, +troll, +unicorn, +vampire, +werewolf, +yeti, ?centaur, ?dragon, ?mermaid, ?unicorn

### FILM  `film`
- правило: What belongs to the group «Film» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 6
- +canister, +develop, +director, +negative, +premiere, +studio

### FILM CLASSICS  `film_classics`
- правило: What belongs to the group «Film Classics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 5
- +avatar, +Casablanca, +citizen kane, +gladiator, !old yeller

### FILM DIRECTORS  `film_directors`
- правило: What belongs to the group «Film Directors» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +kubrick, +scorsese, +spielberg, +tarantino

### FILM FESTIVAL  `film_festival`
- правило: What belongs to the group «Film Festival» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +celebrity, +paparazzi, +red carpet, +tuxedo

### FILM GENRES  `film_genres`
- правило: What belongs to the group «Film Genres» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 7
- +action, +comedy, +documentary, +drama, +horror, +romance, +thriller

### FILM MUSICALS  `film_musicals`
- правило: What belongs to the group «Film Musicals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +cabaret, +Grease, +hairspray, +la la land

### FILM NOIR  `film_noir`
- правило: What belongs to the group «Film Noir» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +shadowy, !femme fatale, !gumshoe, !trenchcoat

### FILM NOIR ELEMENTS  `film_noir_elements`
- правило: What belongs to the group «Film Noir Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 7
- +detective, +femme, +Shadow, +venetian, +voiceover, !femme fatale, !gumshoe

### FILMMAKING  `filmmaking`
- правило: What belongs to the group «Filmmaking» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 8
- +actor, +camera, +directing, +director, +editing, +lighting, +scene, +script

### FILMS  `films`
- правило: What belongs to the group «Films» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +action, +comedy, +documentary, +horror

### FINE ARTS  `fine_arts`
- правило: What belongs to the group «Fine Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 6
- +calligraphy, +ceramics, +drawing, +photography, +printmaking, +sculpture

### FINE PARTICLES  `fine_particles`
- правило: What belongs to the group «Fine Particles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +flour, +sand, +soot, +sugar

### FIRE SHOW  `fire_show`
- правило: What belongs to the group «Fire Show» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +artist, +fire, +night, +show

### FIREARM PARTS  `firearm_parts`
- правило: What belongs to the group «Firearm Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +barrel, +hammer, +trigger, !forend

### FOLK DANCES  `folk_dances`
- правило: What belongs to the group «Folk Dances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +flamenco, +polka, !haka, !tarantella

### FOLK SONGS  `folk_songs`
- правило: What belongs to the group «Folk Songs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +crow, +danny boy, +scarborough, !greensleeves

### FOUNTAIN PARTS  `fountain_parts`
- правило: What belongs to the group «Fountain Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +basin, +nozzle, +pump, +tier

### FRAT PARTY  `frat_party`
- правило: What belongs to the group «Frat Party» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 6
- +beer, +brothers, +house, +keg, +music, +Pong

### GUITAR PARTS  `guitar_parts`
- правило: What belongs to the group «Guitar Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +neck, +pegs, +tuner, xsoundhole

### GUN PARTS  `gun_parts`
- правило: What belongs to the group «Gun Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +barrel, +sight, +stock, +trigger

### GYM PARTS  `gym_parts`
- правило: What belongs to the group «Gym Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +cardio, +lockers, +sauna, +weight room

### HARBOR PARTS  `harbor_parts`
- правило: What belongs to the group «Harbor Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +breakwater, +jetty, +pier, +quay

### HEART  `heart`
- правило: What belongs to the group «Heart» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 24
- +aorta, +arteries, +artery, +atrium, +beat, +cardio, +chamber, +compassion, +courage, +dear, +four chambers, +hemoglobin, +Hope, +intimacy, +left ventricle, +love, +pulmonary vein, +pulse, +rhythmic beat, +romance, +valve, +vein, +ventricle, !ventricles

### HEART ACTIONS  `heart_actions`
- правило: What belongs to the group «Heart Actions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +attack, +murmur, +pump, +race

### HEARTS  `hearts`
- правило: What belongs to the group «Hearts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +aorta, +atrium, +valve, +ventricle

### ORCHESTRA SECTIONS  `instruments_in_an_orchestra`
- правило: Sections and roles in a symphony orchestra
- тип связи: `part_of`, базовая сложность 0.4
- слов: 12
- ~brass, ~cellist, ~conductor, ~ensemble, ~first violin, ~percussion, ~section, ~soloist, ~strings, ~woodwind, !concertmaster, xtimpanist

### INSTRUMENTS OF MEASURE  `instruments_of_measure`
- правило: What belongs to the group «Instruments Of Measure» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +barometer, +caliper, +thermometer, !chronometer

### THINGS WITH STRINGS  `instruments_you_strum`
- правило: Objects that have strings as an essential part
- тип связи: `has_property`, базовая сложность 0.4
- слов: 15
- ~apron (apron_garment), ~balloon, ~banjo, ~bow (bow_music), ~cello, ~guitar, ~hammock, ~harp, ~kite (kite_toy), ~piano, ~puppet, ~tennis racket, ~violin, ~yo-yo, !marionette

### JAPANESE ARTS  `japanese_arts`
- правило: What belongs to the group «Japanese Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +bonsai, +calligraphy, +haiku, +kabuki, +origami, +pottery, !ikebana, !sumi e

### JAZZ MUSICIANS  `jazz_musicians`
- правило: What belongs to the group «Jazz Musicians» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +coltrane, +miles, +monk, +parker

### KIMONO PARTS  `kimono_parts`
- правило: What belongs to the group «Kimono Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +collar, +hem, +obi, +sleeve

### LARGEST ON EARTH  `largest_on_earth`
- правило: What belongs to the group «Largest On Earth» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +Amazon, +caspian sea, +Everest, +pacific ocean

### LATIN AMERICAN DANCES  `latin_american_dances`
- правило: What belongs to the group «Latin American Dances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +salsa, !bachata, !cumbia, !merengue

### LATIN DANCES  `latin_dances`
- правило: What belongs to the group «Latin Dances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +rumba, +salsa, +samba, +tango

### LEG PARTS  `leg_parts`
- правило: What belongs to the group «Leg Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 5
- +ankle, +knee, +meniscus, +shin, +thigh

### LIGHTHOUSE PARTS  `lighthouse_parts`
- правило: What belongs to the group «Lighthouse Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 6
- +beacon, +keeper, +lamp, +lens, +spiral, +tower

### LITURGICAL MUSIC  `liturgical_music`
- правило: What belongs to the group «Liturgical Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !antiphon, !motet, !plainchant, !polyphony

### LIVE MUSIC VENUES  `live_music_venues`
- правило: What belongs to the group «Live Music Venues» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +amphitheater, +arena, +jazz club, !bandshell

### LIVE SHOWS  `live_shows`
- правило: What belongs to the group «Live Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 5
- +circus, +opera, +parade, +play, +theater

### LOOM PARTS  `loom_parts`
- правило: What belongs to the group «Loom Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +reed, +shuttle, +warp, !heddle

### MAGIC SHOW  `magic_words`
- правило: Things used in a stage magic performance
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- +assistant, +box, +cape, +chain, +coin, +deck, +dove, +handcuffs, +hat, +illusion, +mirror, +rabbit, +rope, +scarf, +smoke, +top hat, +trick, +wand

### MAKE UP ARTIST  `make_up_artist`
- правило: What belongs to the group «Make Up Artist» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 6
- +backstage, +brushes, +contour, +eyeliner, +lipstick, +mascara

### MARTIAL  `martial`
- правило: What belongs to the group «Martial» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +dojo, +obi, +sensei, xbokken

### MARTIAL DISCIPLINES  `martial_disciplines`
- правило: What belongs to the group «Martial Disciplines» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +sambo, +sumo, !capoeira, !kendo

### MARTINI  `martini`
- правило: What belongs to the group «Martini» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +gin, +olive, +shaken, +vermouth

### MARTINI GLASS  `martini_glass`
- правило: What belongs to the group «Martini Glass» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 6
- +cocktail, +ice, +juice, +lime, +olive, +vermouth

### MEAL PARTS  `meal_parts`
- правило: What belongs to the group «Meal Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +appetizers, +beverages, +dessert, +main course

### MEASURING INSTRUMENTS  `measuring_instruments`
- правило: What belongs to the group «Measuring Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- ~protractor, +caliper, +compass, +ruler

### MECHANICAL WATCH PARTS  `mechanical_watch_parts`
- правило: What belongs to the group «Mechanical Watch Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +balance, +jewel, !escapement, !mainspring

### MICHAEL JACKSON SONGS  `michael_jackson_songs`
- правило: What belongs to the group «Michael Jackson Songs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +beat it, +billie jean, +smooth criminal, +thriller

### MICROSCOPE PARTS  `microscope_parts`
- правило: What belongs to the group «Microscope Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +condenser, +objective, +ocular, +stage, !eyepiece

### MIXED MARTIAL ARTS  `mixed_martial_arts`
- правило: What belongs to the group «Mixed Martial Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +coach, +fighter, +octagon, +referee

### MOSAIC ART  `mosaic_art`
- правило: What belongs to the group «Mosaic Art» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +grout, +pattern, +tile, !tesserae

### MOTORCYCLE PARTS  `motorcycle_parts`
- правило: What belongs to the group «Motorcycle Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +carburetor, +clutch, +exhaust, +throttle

### MOVIE  `movie`
- правило: What belongs to the group «Movie» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 12
- +action, +actor, +comedy, +director, +feature, +film, +flick, +horror, +picture, +popcorn, +romance, +showing

### MOVIE CHARACTERS  `movie_characters`
- правило: What belongs to the group «Movie Characters» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +Ariel, +darth vader, +Dracula, +freddy krueger

### MOVIE FRANCHISES  `movie_franchises`
- правило: What belongs to the group «Movie Franchises» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +matrix, +Rocky, +saw, +Terminator

### MOVIE GENRE  `movie_genre`
- правило: What belongs to the group «Movie Genre» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +comedy, +drama, +horror, +western

### MOVIE GENRES  `movie_genres`
- правило: Categories used to classify films
- тип связи: `is_a`, базовая сложность 0.25
- слов: 24
- +action, +adventure, +animation, +biopic, +comedy, +documentary, +drama, +fantasy, +horror, +musical, +mystery, +noir, +romance, +satire, +sci-fi, +thriller, +vampire, +war, +western, ?action, ?comedy, ?horror, ?romance, ?western

### MOVIE RATINGS  `movie_ratings`
- правило: What belongs to the group «Movie Ratings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +g, +nc 17, +pg, +r

### MOVIE THEATER  `movie_theater`
- правило: What belongs to the group «Movie Theater» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +cinema, +has a screen, +popcorn, +projector

### MOVIE TYPES  `movie_types`
- правило: What belongs to the group «Movie Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +drama, +epic, +musical, +noir

### MOVIE VILLAINS  `movie_villains`
- правило: What belongs to the group «Movie Villains» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +bates, +corleone, +Montana, +Smith

### FILM MAKING  `movie_words`
- правило: Words used in making and showing films
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +actor, +box office, +camera, +cast (cast_people), +close up, +credits, +cut, +director, +editing, +extra, +matinee, +premiere, +scene, +screenplay, +script, +sequel, +stunt, +take, +trailer (trailer_movie), !set (set_film)

### MOVIES  `movies`
- правило: What belongs to the group «Movies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +actor, +scene, +script, +studio

### MUSIC  `music`
- правило: What belongs to the group «Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 27
- +beat, +chord, +chorus, +classical, +concert, +country, +dance, +disco, +drum, +flute, +guitar, +harmony, +jazz, +la, +lyrics, +melody, +mi, +notes, +octave, +outro, +piano, +rap, +rhythm, +si, +song, +tempo, +verse

### MUSIC BAND  `music_band`
- правило: What belongs to the group «Music Band» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +bassist, +drummer, +guitarist, +lead singer

### MUSIC COMPOSITION  `music_composition`
- правило: What belongs to the group «Music Composition» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +composer, +harmony, +melody, +notes

### MUSIC DEVICES  `music_devices`
- правило: What belongs to the group «Music Devices» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 8
- +eight track, +gramophone, +mp3 player, +radio, +tape deck, +turntable, +walkman, !boombox

### MUSIC FESTIVALS  `music_festivals`
- правило: What belongs to the group «Music Festivals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +coachella, +glastonbury, !bonnaroo, !lollapalooza

### MUSIC FORMATS  `music_formats`
- правило: What belongs to the group «Music Formats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +cassette tape, +cd, +mp3, +record

### MUSIC FORMS  `music_forms`
- правило: What belongs to the group «Music Forms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +concerto, +opera, +sonata, +symphony

### MUSIC GENRE  `music_genre`
- правило: What belongs to the group «Music Genre» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +classical, +country, +jazz, +ska

### MUSIC GENRES  `music_genres`
- правило: Styles used to classify music
- тип связи: `is_a`, базовая сложность 0.25
- слов: 33
- ~rock (rock_music), +blues, +classical, +country, +disco, +electronica, +folk, +funk, +gospel, +hip hop, +house, +indie, +jazz, +metal, +opera, +pop (pop_music), +punk, +rap, +reggae, +soul, +swing, +techno, ?blues, ?classical, ?country, ?disco, ?folk, ?funk, ?gospel, ?jazz, ?rap, ?reggae, ?soul

### MUSIC PERIODS  `music_periods`
- правило: What belongs to the group «Music Periods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +baroque, +classical, +renaissance, +romantic

### MUSIC PLAYERS  `music_players`
- правило: What belongs to the group «Music Players» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +earphones, +speaker, +turntable, !subwoofer

### MUSIC STYLES  `music_styles`
- правило: What belongs to the group «Music Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +folk, +funk, +jazz, +reggae

### MUSIC THEORY  `music_theory`
- правило: What belongs to the group «Music Theory» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 7
- +chord, +coda, +interval, +rhythm, +tempo, !arpeggio, !legato

### MUSIC TYPES  `music_types`
- правило: What belongs to the group «Music Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bebop, +scat, +ska, !acapella

### MUSIC WORDS  `music_words`
- правило: Words used to describe how a piece of music is written or performed
- тип связи: `found_in`, базовая сложность 0.3
- слов: 25
- ~bridge (bridge_music), +beat, +chord, +chorus, +clef, +duet, +flat, +harmony, +key (key_music), +measure, +melody, +note (note_music), +octave, +pitch (pitch_music), +refrain, +rhythm, +riff, +scale (scale_music), +Sharp, +solo, +staff, +tempo, +verse, !bar (bar_music), !rest (rest_music)

### MUSICAL  `musical`
- правило: What belongs to the group «Musical» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +company, +Grease, +hairspray, +rent

### MUSICAL ALLOYS  `musical_alloys`
- правило: What belongs to the group «Musical Alloys» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +brass, +bronze, +pewter, +sterling

### MUSICAL BANDS  `musical_bands`
- правило: What belongs to the group «Musical Bands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +aerosmith, +Beatles, +coldplay, +metallica

### MUSICAL COMPOSITIONS  `musical_compositions`
- правило: What belongs to the group «Musical Compositions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +concerto, +overture, +sonata, +symphony

### MUSICAL DIRECTIONS  `musical_directions`
- правило: What belongs to the group «Musical Directions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +adagio, +allegro, +presto, !lento

### MUSICAL ENSEMBLES  `musical_ensembles`
- правило: What belongs to the group «Musical Ensembles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +choir, +quartet, +violin, !septet

### MUSICAL FORMS  `musical_forms`
- правило: What belongs to the group «Musical Forms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +concerto, +fugue, +prelude, +sonata

### MUSICAL GENRES  `musical_genres`
- правило: What belongs to the group «Musical Genres» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +blues, +country, +opera, +reggae

### MUSICAL GROUPS  `musical_groups`
- правило: What belongs to the group «Musical Groups» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +linkin park, +nirvana, !acdc, !boyzone

### MUSICAL INSTRUMENTS  `musical_instruments`
- правило: Instruments played to produce music
- тип связи: `is_a`, базовая сложность 0.15
- слов: 41
- ~keyboard (keyboard_music), ~melodica, +accordion, +bagpipes, +banjo, +bassoon, +cello, +clarinet, +cymbal, +drum, +drums, +flute, +guitar, +harmonica, +harp, +mandolin, +maracas, +oboe, +organ (organ_music), +piano, +saxophone, +tambourine, +theremin, +trombone, +trumpet, +tuba, +ukulele, +violin, +xylophone, ?accordion, ?banjo, ?bassoon, ?cello, ?drum, ?flute, ?guitar, ?harp, ?oboe, ?piano, ?saxophone, ?trumpet

### MUSICAL NOTATION  `musical_notation`
- правило: What belongs to the group «Musical Notation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 8
- +clef, +flat, +natural, +octave, +Sharp, +slur, +staccato, +treble

### MUSICAL ORNAMENTS  `musical_ornaments`
- правило: What belongs to the group «Musical Ornaments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +trill, +turn, xappoggiatura, xmordent

### MUSICAL SPEEDS  `musical_speeds`
- правило: What belongs to the group «Musical Speeds» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +adagio, +allegro, !andante, !moderato

### MUSICAL STYLES  `musical_styles`
- правило: What belongs to the group «Musical Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 6
- +blues, +classical, +country, +folk, +jazz, +reggae

### MUSICAL TEMPO MARKINGS  `musical_tempo_markings`
- правило: What belongs to the group «Musical Tempo Markings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +adagio, +allegro, +presto, !andante

### MUSICAL TEMPOS  `musical_tempos`
- правило: What belongs to the group «Musical Tempos» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +adagio, +allegro, +presto, !andante

### MUSICAL TERMS  `musical_terms`
- правило: What belongs to the group «Musical Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 9
- +cadence, +harmony, +measure, +melody, +motif, +rhythm, +tempo, !arpeggio, !ostinato

### NAVIGATION INSTRUMENTS  `navigation_instruments`
- правило: What belongs to the group «Navigation Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gps, +gyroscope, !astrolabe, !sextant

### OPTICAL INSTRUMENTS  `optical_instruments`
- правило: What belongs to the group «Optical Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 5
- +binoculars, +microscope, +periscope, +telescope, !spectroscope

### ORCHESTRA INSTRUMENTS  `orchestra_instruments`
- правило: What belongs to the group «Orchestra Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 5
- +cello, +flute, +trumpet, +viola, +violin

### ORCHESTRAL INSTRUMENTS  `orchestral_instruments`
- правило: What belongs to the group «Orchestral Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +bassoon, +flute, +trumpet, +violin

### PAIRED DANCE  `paired_dance`
- правило: What belongs to the group «Paired Dance» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +cha cha, +foxtrot, +rumba, +tango

### PAPER ARTS  `paper_arts`
- правило: What belongs to the group «Paper Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +origami, !decoupage, !quilling, xkirigami

### PAPER FOLDING ARTS  `paper_folding_arts`
- правило: What belongs to the group «Paper Folding Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +origami, !decoupage, !quilling, xkirigami

### PARTICIPANTS IN COURT  `participants_in_court`
- правило: What belongs to the group «Participants In Court» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +criminals, +judge, +lawyer, +robber

### PARTICLE PHYSICS  `particle_physics`
- правило: What belongs to the group «Particle Physics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +boson, +hadron, +neutrino, +quark

### PARTICLES  `particles`
- правило: What belongs to the group «Particles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 10
- +boson, +electron, +hadron, +lepton, +molecule, +neutrino, +photon, +quark, !meson, !muon

### PARTNER DANCES  `partner_dances`
- правило: What belongs to the group «Partner Dances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +foxtrot, +tango, +viennese, !quickstep

### PARTNERSHIP  `partnership`
- правило: What belongs to the group «Partnership» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +affection, +closeness, +love, +trust

### PARTS OF A BOOK  `parts_of_a_book`
- правило: What belongs to the group «Parts Of A Book» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +cover, +jacket, +page, +spine

### PARTS OF A CANOE  `parts_of_a_canoe`
- правило: What belongs to the group «Parts Of A Canoe» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +keel, +stern, +thwart, !gunwale

### PARTS OF A CELL  `parts_of_a_cell`
- правило: What belongs to the group «Parts Of A Cell» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +cytoplasm, !lysosome, !ribosome, !vacuole

### PARTS OF A COMPASS  `parts_of_a_compass`
- правило: What belongs to the group «Parts Of A Compass» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +bezel, +dial, +rose, !magnetometer

### PARTS OF A GREENHOUSE  `parts_of_a_greenhouse`
- правило: What belongs to the group «Parts Of A Greenhouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +gutter, +pane, +ridge, +vent

### PARTS OF A HARBOR  `parts_of_a_harbor`
- правило: What belongs to the group «Parts Of A Harbor» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +berth, +breakwater, +buoy, +jetty

### PARTS OF A LETTER  `parts_of_a_letter`
- правило: What belongs to the group «Parts Of A Letter» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +body, +postscript, +signature, !salutation

### PARTS OF A MICROSCOPE  `parts_of_a_microscope`
- правило: What belongs to the group «Parts Of A Microscope» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- ~eyepiece, +mirror, +objective, +stage

### PARTS OF A MILL  `parts_of_a_mill`
- правило: What belongs to the group «Parts Of A Mill» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +flume, +hopper, +millstone, +sluice

### PARTS OF A NEURON  `parts_of_a_neuron`
- правило: What belongs to the group «Parts Of A Neuron» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +axon, +dendrite, +nucleus, +soma

### PARTS OF A ROSE  `parts_of_a_rose`
- правило: What belongs to the group «Parts Of A Rose» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +leaf, +petal, +stem, +thorn

### PARTS OF A SHIP  `parts_of_a_ship`
- правило: What belongs to the group «Parts Of A Ship» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 6
- +deck, +hold, +hull, +mast, +rigging, !porthole

### PARTS OF A STAIRCASE  `parts_of_a_staircase`
- правило: What belongs to the group «Parts Of A Staircase» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +banister, +landing, +railing, +step

### PARTS OF A TELESCOPE  `parts_of_a_telescope`
- правило: What belongs to the group «Parts Of A Telescope» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +aperture, +tube, !eyepiece, !focuser

### PARTS OF A VOLCANO  `parts_of_a_volcano`
- правило: What belongs to the group «Parts Of A Volcano» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 6
- +caldera, +conduit, +crater, +lava, +magma, +vent

### PARTS OF A WAVE  `parts_of_a_wave`
- правило: What belongs to the group «Parts Of A Wave» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +break, +crest, +swell, +trough

### PARTS OF A WELL  `parts_of_a_well`
- правило: What belongs to the group «Parts Of A Well» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +bucket, +pulley, +shaft, +winch

### PARTS OF CORN  `parts_of_corn`
- правило: What belongs to the group «Parts Of Corn» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +cob, +husk, +kernel, +silk

### PARTS OF LOCK  `parts_of_lock`
- правило: What belongs to the group «Parts Of Lock» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bolt, +keyhole, +shackle, +tumbler

### PARTS OF SANDWICH  `parts_of_sandwich`
- правило: What belongs to the group «Parts Of Sandwich» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +bread, +cold cut, +condiment, +lettuce

### PARTS OF SENTENCE  `parts_of_sentence`
- правило: What belongs to the group «Parts Of Sentence» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +adjective, +adverb, +noun, +verb

### PARTS OF THE DAY  `parts_of_the_day`
- правило: What belongs to the group «Parts Of The Day» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +dawn, +dusk, +night, +noon

### PARTY  `party`
- правило: What belongs to the group «Party» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +dancing, +Friends, +fun, +music

### PARTY ACTIVITIES  `party_activities`
- правило: What belongs to the group «Party Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +dancing, +karaoke, +limbo, +musical chairs

### PARTY ELEMENTS  `party_elements`
- правило: What belongs to the group «Party Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +confetti, +dances, +martini glass, +snacks

### PARTY HAT  `party_hat`
- правило: What belongs to the group «Party Hat» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +color, +cone, +glitter, +strap

### PARTY NIGHT  `party_night`
- правило: What belongs to the group «Party Night» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +dance, +Friends, +lights, +music

### PARTY PLANNING  `party_planning`
- правило: What belongs to the group «Party Planning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +decorations, +game night essentials, +invitations, +menu

### PARTY THINGS  `party_things`
- правило: Things found at a birthday party
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~plate (plate_dish), +balloon, +banner, +cake, +candle, +candy, +confetti, +favor, +game, +guest, +invitation, +music, +napkin, +party hat, +piñata, +present (present_gift), +prize, +ribbon, +streamer, !punch (punch_drink)

### PERCUSSION INSTRUMENTS  `percussion`
- правило: Musical instruments played by striking or shaking
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~castanets, ~cowbell, ~maraca, ~marimba, ~timpani, ~xylophone, +bongo, +chime, +cymbal, +drum, +drums, +gong, +snare, +tambourine, +triangle, ?tambourine, ?triangle, ?xylophone

### PERFORMANCE ARTS  `performance_arts`
- правило: What belongs to the group «Performance Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 7
- +ballet, +kabuki, +magic, +mime, +opera, +standup, !puppetry

### PIANO PARTS  `piano_parts`
- правило: What belongs to the group «Piano Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +hammer, +pedal, +scales, !soundboard

### PLUCKED INSTRUMENTS  `plucked_instruments`
- правило: What belongs to the group «Plucked Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +banjo, +mandolin, !koto, !sitar

### POOL PARTY  `pool_party`
- правило: What belongs to the group «Pool Party» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 8
- +bikini, +DJ, +float, +noodle, +pool, +splash, !floaties, !pina colada

### POP SINGERS  `pop_singers`
- правило: What belongs to the group «Pop Singers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +ariana grande, +bruno mars, +ed sheeran, +taylor swift

### PRINTER PARTS  `printer_parts`
- правило: What belongs to the group «Printer Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +cartridge, +feeder, +roller, +toner

### QUARTERBACK  `quarterback`
- правило: What belongs to the group «Quarterback» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +audible, +blitz, +pocket, +snap

### QUARTERS  `quarters`
- правило: What belongs to the group «Quarters» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +barracks, +chambers, +dorm, +lodgings

### QUARTZ  `quartz`
- правило: What belongs to the group «Quartz» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +amethyst, +rose, +smoky, !citrine

### READING MATTER  `reading_material`
- правило: Things people read
- тип связи: `is_a`, базовая сложность 0.25
- слов: 24
- +article, +blog, +book, +brochure, +comic, +diary, +journal, +label, +letter (letter_mail), +magazine, +manual, +map, +menu, +news, +newspaper, +novel, +poem, +recipe, +script, +sign, +textbook, +ticket (ticket_admission), ?article, ?book

### REFRIGERATOR PARTS  `refrigerator_parts`
- правило: What belongs to the group «Refrigerator Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +coil, +compressor, +freezer, !crisper

### RENAISSANCE ART  `renaissance_art`
- правило: What belongs to the group «Renaissance Art» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 7
- +apprentice, +fresco, +madonna, +patron, +perspective, +portrait, !altarpiece

### RENAISSANCE ARTISTS  `renaissance_artists`
- правило: What belongs to the group «Renaissance Artists» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 5
- +donatello, +leonardo, +Michelangelo, +raphael, !botticelli

### RENAISSANCE MUSIC  `renaissance_music`
- правило: What belongs to the group «Renaissance Music» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +choir, +harp, +lute, +sonnet, !madrigal

### RIHANNA SONGS  `rihanna_songs`
- правило: What belongs to the group «Rihanna Songs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +diamonds, +s o s, +umbrella, +work

### SCIENTIFIC INSTRUMENTS  `scientific_instruments`
- правило: What belongs to the group «Scientific Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 6
- +barometer, +microscope, +spectrometer, +telescope, !altimeter, !manometer

### SHIP PARTS  `ship_parts`
- правило: What belongs to the group «Ship Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 11
- +anchor, +boom, +hull, +keel, +mast, +rudder, +stern, !bollard, !bowsprit, !capstan, !forecastle

### SHOW THE DIRECTION  `show_the_direction`
- правило: What belongs to the group «Show The Direction» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +arrows, +compass, +gps, +map

### SHOW TYPES  `show_types`
- правило: What belongs to the group «Show Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +animation, +movie, +opera, +theater

### SILENT FILM STARS  `silent_film_stars`
- правило: What belongs to the group «Silent Film Stars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +chaplin, +fairbanks, +keaton, +pickford

### SIMPLE INSTRUMENTS  `simple_instruments`
- правило: What belongs to the group «Simple Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +guitar, +harmonica, +trumpet, +ukulele

### SINGER  `singer`
- правило: What belongs to the group «Singer» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 8
- +baritone, +chorus, +melody, +mezzo, +microphone, +soprano, +tenor, +vocalist

### SMART  `smart`
- правило: What belongs to the group «Smart» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +astute, +brilliant, +Sharp, +shrewd

### SMARTPHONE  `smartphone`
- правило: What belongs to the group «Smartphone» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 6
- +app, +apps, +battery, +camera, +Charger, +microphone

### SONG  `song`
- правило: What belongs to the group «Song» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +compose, +hum, +play, +tune

### SONG TYPES  `song_types`
- правило: What belongs to the group «Song Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +blues, +hymn, +jingle, +serenade

### SPICE GIRLS SONGS  `spice_girls_songs`
- правило: What belongs to the group «Spice Girls Songs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +goodbye, +holler, +mama, +wannabe

### STAGE SHOWS  `stage_shows`
- правило: What belongs to the group «Stage Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +concert, +magic, +theater, +variety

### START  `start`
- правило: What belongs to the group «Start» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +beginning, +dawn, +Genesis, +origin

### STARTING A FIRE  `starting_a_fire`
- правило: What belongs to the group «Starting A Fire» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +kindling, +matches, +spark, +tinder

### STARTS WITH F  `starts_with_f`
- правило: What belongs to the group «Starts With F» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +fable, +factory, +fashion, +feudalism

### TALE CHARACTERS  `storybook_characters`
- правило: Characters that appear in classic fairy tales
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~queen (queen_royal), +dragon, +dwarf, +elf, +fairy, +frog, +genie, +giant, +goblin, +king, +knight, +mermaid, +ogre, +Prince, +princess, +troll, +unicorn, +witch, +wizard, +wolf

### STRING INSTRUMENTS  `string_instruments`
- правило: Musical instruments played by plucking or bowing strings
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~sitar, ~zither, +banjo, +bass (bass_music), +cello, +fiddle, +guitar, +harp, +harpsichord, +lute, +mandolin, +ukulele, +viola, +violin, ?banjo, ?cello, ?guitar, ?harp, ?mandolin, ?sitar, ?ukulele, ?viola, ?violin, !erhu

### STRINGED INSTRUMENTS  `stringed_instruments`
- правило: What belongs to the group «Stringed Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 6
- +banjo, +cello, +lute, +mandolin, +ukulele, +violin

### STUDIO ARTS  `studio_arts`
- правило: What belongs to the group «Studio Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 8
- +ceramics, +mosaic, +photography, +pottery, +printmaking, +sculpture, +weaving, !metalwork

### SUBATOMIC PARTICLES  `subatomic_particles`
- правило: What belongs to the group «Subatomic Particles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +boson, +electron, +lepton, +neutrino, +neutron, +quark, !kaon

### SURGICAL INSTRUMENTS  `surgical_instruments`
- правило: What belongs to the group «Surgical Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +forceps, +probe, !hemostat, !retractor

### TALK SHOW HOSTS  `talk_show_hosts`
- правило: What belongs to the group «Talk Show Hosts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +colbert, +fallon, +kimmel, +oliver

### TARTLET  `tartlet`
- правило: What belongs to the group «Tartlet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +almond bits, +apple slice, +lemon wedge, +mint leaf

### TELESCOPE PARTS  `telescope_parts`
- правило: What belongs to the group «Telescope Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 5
- +finder, +mirror, +mount, +tripod, !eyepiece

### TELEVISION SHOWS  `television_shows`
- правило: What belongs to the group «Television Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +dark, +Friends, +Seinfeld, +survivor

### TEXTILE ARTS  `textile_arts`
- правило: What belongs to the group «Textile Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 6
- +batik, +embroidery, +fabric, +shuttle, +warp, +weaving

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
- слов: 32
- ~jenga, ~kite (kite_toy), ~marble (marble_toy), ~rattle (rattle_toy), ~top (top_spin), +action figure, +ball (ball_sphere), +blocks, +bubble, +car, +crayon, +doll, +famous robots, +frisbee, +jack in the box, +jump rope, +puzzle, +robot, +Slinky, +stuffed toy, +teddy, +teddy bear, +train set, +tricycle, +water gun, +yo yo, +yo-yo, ?blocks, ?doll, ?puzzle, ?robot, ?train set

### TRACTOR  `tractor`
- правило: What belongs to the group «Tractor» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +john deere, +massey ferguson, +new holland, !kubota

### TV SHOW  `tv_show`
- правило: What belongs to the group «Tv Show» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +actress, +daytime, +director, !blooper

### TV SHOW TYPES  `tv_show_types`
- правило: What belongs to the group «Tv Show Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +cartoon, +reality, +sitcom, +soap opera

### TV SHOWS  `tv_shows`
- правило: What belongs to the group «Tv Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 7
- +cooking, +Friends, +Jeopardy, +lost, +office, +Simpsons, +survivor

### TELEVISION WORDS  `tv_words`
- правило: Words used about television programs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +broadcast, +cable, +channel, +commercial, +episode, +finale, +network, +pilot, +ratings, +remote (remote_device), +rerun, +screen (screen_display), +sitcom, +spinoff, +streaming, +subtitle, !host (host_presenter), !season (season_time)

### TYPES OF ARTICLE  `types_of_article`
- правило: What belongs to the group «Types Of Article» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +editorial, +essay, +opinion, +review

### TYPES OF DANCE  `types_of_dance`
- правило: What belongs to the group «Types Of Dance» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 8
- +ballet, +ballroom, +break, +hip hop, +salsa, +Square, +tango, +waltz

### UNIVERSITY ACADEMIC DEPARTMENTS  `university_academic_departments`
- правило: What belongs to the group «University Academic Departments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +anthropology, +philosophy, +psychology, +sociology

### UNIVERSITY DEPARTMENTS  `university_departments`
- правило: What belongs to the group «University Departments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 7
- +anthropology, +chemistry, +economics, +fine arts, +linguistics, +philosophy, +psychology

### VAN GOGH ARTWORKS  `van_gogh_artworks`
- правило: What belongs to the group «Van Gogh Artworks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bedroom, +irises, +Starry Night, +Sunflowers

### GAMING WORDS  `video_game_words`
- правило: Words used when playing video games
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~respawn, +arcade, +avatar, +boss, +cheat code, +checkpoint, +console, +controller, +health bar, +joystick, +lag, +level, +loot, +multiplayer, +power up, +quest, +save, +score (score_points)

### VINTAGE MUSIC PLAYERS  `vintage_music_players`
- правило: What belongs to the group «Vintage Music Players» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gramophone, +jukebox, +record player, +turntable

### VISUAL ARTS  `visual_arts`
- правило: What belongs to the group «Visual Arts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 7
- +artists, +drawing, +gallery, +painting, +photography, +printmaking, +sculpture

### WHEEL PARTS  `wheel_parts`
- правило: What belongs to the group «Wheel Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +hub, +rim, +spoke, +tire

### WICKED SONGS  `wicked_songs`
- правило: What belongs to the group «Wicked Songs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +for good, +no good deed, +popular, +wonderful

### WIND INSTRUMENTS  `wind_instruments`
- правило: Musical instruments played by blowing air
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +bagpipes, +bassoon, +clarinet, +flute, +french horn, +harmonica, +oboe, +piccolo, +recorder, +saxophone, +trombone, +trumpet, +tuba, +whistle, ?bassoon, ?clarinet, ?flute, ?oboe, ?saxophone, ?trumpet

### WOMEN SINGERS  `women_singers`
- правило: What belongs to the group «Women Singers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +Houston, +keys, +perry, +swift

### WOODWIND INSTRUMENTS  `woodwind_instruments`
- правило: What belongs to the group «Woodwind Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 6
- +bassoon, +clarinet, +flute, +oboe, +piccolo, +saxophone

### WRITING INSTRUMENTS  `writing_instruments`
- правило: What belongs to the group «Writing Instruments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +fountain pen, +quill, +reed, +stylus


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
- слов: 20
- ~bifocals, ~biker goggle, +aviator, +blinders, +blindfold, +contacts, +glasses, +goggles, +mask, +monocle, +reading glasses, +safety glasses, +shades, +sunglasses, +visor, ?bifocals, ?contacts, ?glasses, ?goggles, ?sunglasses

### FASHION ACCESSORIES  `fashion_accessories`
- правило: Items added to complete a look
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~bowtie, ~hairband, ~tie (tie_clothing), +belt, +bracelet, +brooch, +cufflinks, +earring, +glasses, +gloves, +hat, +hats, +jewelry, +necklace, +pocket square, +scarf, +sunglasses, +suspenders, +watch (watch_object), ?belt, ?brooch, ?cufflinks, ?gloves, ?scarf, ?sunglasses

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
- слов: 30
- ~chignon, ~cornrows, ~cowlick, ~dreadlock, ~topknot, ~updo, +afro, +bangs, +beehive, +bob, +braid, +bun, +crew cut, +crop, +dreadlocks, +layers, +middle part, +mohawk, +mullet, +perm, +pigtails, +pixie, +ponytail, +shag, ?afro, ?bob, ?braid, ?bun, ?pixie, ?ponytail

### JEWELRY STONES  `jewelry_stones`
- правило: Stones set into jewelry
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +amethyst, +aquamarine, +diamond (diamond_gem), +emerald, +garnet, +jade, +moonstone, +onyx, +opal, +pearl, +peridot, +ruby, +sapphire, +topaz, +turquoise

### MAKEUP  `makeup`
- правило: Cosmetics applied to the face
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- +blush, +blusher, +bronzer, +brow pencil, +brush, +compact powder, +concealer, +eye shadow, +eyeliner, +eyeshadow, +foundation (foundation_makeup), +gloss, +highlighter, +lip oil, +lipstick, +mascara, +mirror, +powder, +primer, +setting spray, +toner, ?blush, ?eyeliner, ?lipstick, ?mascara

### NAIL CARE  `nail_words`
- правило: Things used for manicures and nail care
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- +acrylic, +base coat, +buffer, +clipper, +cuticle, +file (file_tool), +gel, +glitter, +polish (polish_product), +pusher, +remover, +soak, +top coat, +wrap

### PATTERNS  `patterns`
- правило: Patterns printed on cloth
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~gingham, ~herringbone, ~houndstooth, +animal print, +argyle, +camouflage, +checkered, +chevron, +floral, +paisley, +plaid, +polka dot, +spot, +Stripe, +tartan, +tie dye, +zigzag, ?checkered, ?Stripe

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
- слов: 22
- ~biscotti, ~macaroon, ~snickerdoodle, ~thumbprint, +butter, +chocolate chip, +fortune, +fortune cookie, +gingerbread, +molasses, +oatmeal, +peanut butter, +sandwich cookie, +shortbread, +sugar, +wafer, ?biscotti, ?chocolate chip, ?gingerbread, ?macaroon, ?snickerdoodle, xamaretti

### COOKING METHODS  `cooking_methods`
- правило: Methods used to cook food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~braise, ~saute, +bake, +barbecue, +blanch, +boil, +broil, +deep fry, +fry (fry_cook), +grill, +poach, +roast, +sear, +simmer, +slow cook, +smoke, +steam, +stir fry, ?bake, ?braise, ?broil, ?grill, ?poach, ?roast, ?saute, ?steam

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
- слов: 26
- ~caprese, ~nicoise, +beans, +caesar, +chef salad, +chopped, +cobb, +coleslaw, +egg salad, +fruit, +fruit salad, +garden, +greek, +macaroni salad, +pasta salad, +potato, +potato salad, +spinach salad, +waldorf, +watercress, ?caesar, ?cobb, ?coleslaw, ?garden, ?greek, ?waldorf

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


## Тема: hobbies

### BIRDWATCHING THINGS  `birdwatching`
- правило: Things a birdwatcher uses
- тип связи: `used_in`, базовая сложность 0.4
- слов: 12
- +binoculars, +bird bath, +birdhouse, +blind, +camera, +checklist, +feeder, +field guide, +notebook, +scope, +seed, +whistle

### GAME PIECES  `board_game_pieces`
- правило: Pieces and parts used in board games
- тип связи: `is_a`, базовая сложность 0.35
- слов: 21
- ~card (card_playing), +board (board_game), +chip, +counter, +cup, +dice (dice_game), +die, +marker, +pawn, +rulebook, +spinner, +tile, +timer, +token, ?marker, ?meeple, ?pawn, ?scorepad, ?spinner, ?token, xmeeple

### CAMPING GEAR  `camping_gear`
- правило: Gear packed for a camping trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 33
- ~firestarter, +backpack, +binoculars, +bug spray, +camp chair, +canteen, +compass, +cooler, +firewood, +first aid kit, +flashlight, +hammock, +hatchet, +lantern, +map, +matches, +mess kit, +rope, +sleeping, +sleeping bag, +stove, +tarp, +tent, +thermos, ?backpack, ?compass, ?cooler, ?flashlight, ?lantern, ?map, ?sleeping bag, ?tarp, ?tent

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
- слов: 26
- ~ball (ball_sphere), ~card trick, ~coin, ~dove, ~handcuff, ~hat, ~illusion, ~levitation, ~mirror, ~ring (ring_circle), ~rope, ~sawing, ~scarf, ~teleport, ~teleportation, ~thumb tip, ~transform, ~transformation, ~vanish, ~wand, +box, +cup, +mind reading, ?dove, !card (card_playing), xmindreading

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
- слов: 18
- ~acrostic, ~brainteaser, ~cryptogram, ~rubiks cube, ~tangram, +anagram, +crossword, +jigsaw, +logic puzzle, +maze, +rebus, +riddle, +sudoku, +word search, ?crossword, ?jigsaw, ?rebus, ?riddle

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
- слов: 18
- ~brilliant, ~carat, ~clarity, ~cut, ~emerald cut, ~facet, ~pear, ~polish (polish_verb), ~princess, ~princess cut, ~radiant, ~setting, ~Solitaire, ~trillion, !band (band_ring), !bezel, !cabochon, !prong

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
- слов: 16
- +barometer, +radar, +rain gauge, +satellite, +thermometer, +weather balloon, +weather vane, ?anemometer, ?barometer, ?hygrometer, ?thermometer, !anemometer, !hygrometer, !seismograph, !sundial, !windsock


## Тема: people

### FAMOUS PAINTERS  `artists`
- правило: Famous painters from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~Cezanne, +Da Vinci, +Dali, +Degas, +Matisse, +Michelangelo, +Monet, +Picasso, +Pollock, +Rembrandt, +Renoir, +rubens, +Van Gogh, +Vermeer, +Warhol, ?Picasso, ?Rembrandt, ?Vermeer

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

### EXPLORERS  `explorers`
- правило: Famous explorers from history
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~Amundsen, ~Vespucci, +Balboa, +Cabot, +Clark, +Columbus, +Cortes, +Hudson, +Lewis, +Livingstone, +Magellan, +Marco Polo, +Shackleton, !cook (cook_explorer)

### FACIAL EXPRESSIONS  `facial_expressions`
- правило: Expressions people make with their face
- тип связи: `does_action`, базовая сложность 0.35
- слов: 20
- +beam (beam_smile), +blink, +blush, +eye roll, +frown, +gape, +glare, +grimace, +grin, +pout, +scowl, +smile, +smirk, +sneer, +wink, +yawn, ?frown, ?grimace, ?smile, ?wink

### FAMILY MEMBERS  `family_members`
- правило: Words for members of a family
- тип связи: `is_a`, базовая сложность 0.12
- слов: 25
- +aunt, +brother, +child, +cousin, +daughter, +father, +godmother, +grandchild, +grandfather, +grandmother, +husband, +in law, +mother, +nephew, +niece, +parent, +sibling, +sister, +son, +spouse, +stepfather, +stepmother, +twin, +uncle, +wife

### FAMOUS AMERICANS  `famous_americans`
- правило: Americans widely known from history
- тип связи: `is_a`, базовая сложность 0.3
- слов: 22
- ~ford (ford_person), +abraham lincoln, +Armstrong, +benjamin franklin, +Carver, +Disney, +Douglass, +Earhart, +Edison, +frank sinatra, +Franklin, +Jefferson, +Keller, +Kennedy, +Lincoln, +Parks, +Roosevelt, +thomas edison, +Tubman, +Twain, +Washington, +Wright

### FEELINGS  `feelings`
- правило: Words naming human emotions
- тип связи: `is_a`, базовая сложность 0.25
- слов: 29
- ~calm (calm_person), +amaze, +angry, +anxious, +astonish, +bored, +confused, +content, +curious, +embarrassed, +excited, +frustrated, +grateful, +guilty, +happy, +hopeful, +jealous, +joyful, +lonely, +nervous, +proud, +relieved, +sad, +scared, +shock, +startle, +surprised, +tired, +worried

### GIRLS NAMES  `girls_names`
- правило: Common first names given to girls in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- +Abigail, +Amelia, +Ava, +Charlotte, +Chloe, +Elizabeth, +Ella, +Emily, +Emma, +Grace, +Hannah, +Isabella, +Jennifer, +Lily, +Linda, +Madison, +Mary, +Mia, +Natalie, +Olivia, +Rachel, +Sarah, +Sophia, +Susan, +Zoe

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
- слов: 19
- ~ford (ford_person), +bell, +diesel, +Edison, +Einstein, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Nobel, +Tesla, +Watt, +Whitney, +Wright, ?bell, ?Edison, ?Tesla, !Daguerre

### STAGES OF LIFE  `life_stages`
- правило: Words for the stages of a human life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~preschooler, +adolescent, +adult, +baby, +child, +elder (elder_person), +grownup, +infant, +kid, +middle age, +newborn, +old man, +retiree, +senior, +teen, +teenager, +toddler, +youth, ?adult, ?baby, ?child, ?infant

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
- слов: 24
- +albert einstein, +Archimedes, +Bohr, +Copernicus, +Curie, +Darwin, +Einstein, +Faraday, +Fleming, +Galileo, +Hawking, +Kepler, +Mendel, +Newton, +Pasteur, +Tesla, ?Archimedes, ?Curie, ?Darwin, ?Einstein, ?Galileo, ?Hawking, ?Kepler, ?Newton

### TITLES  `titles_of_address`
- правило: Titles put before a person name
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- +captain, +chief, +coach, +dean, +doctor, +judge, +lady, +lord, +madam, +miss, +missus, +mister, +officer, +professor, +reverend, +senator, +sergeant, +sir

### US PRESIDENTS  `us_presidents`
- правило: Presidents of the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 29
- +Adams, +Bush, +Carter, +Clinton, +coolidge, +Eisenhower, +Grant, +Jackson, +Jefferson, +Johnson, +Kennedy, +Lincoln, +Madison, +Monroe, +Nixon, +Obama, +Reagan, +Roosevelt, +Truman, +Washington, +Wilson, ?Clinton, ?Grant, ?Jackson, ?Kennedy, ?Lincoln, ?Reagan, ?Roosevelt, ?Washington


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
- слов: 18
- +abbey, +basilica, +cathedral, +chapel, +church, +convent, +monastery, +mosque, +pagoda, +sanctuary, +shrine, +synagogue, +tabernacle, +temple (temple_building), ?chapel, ?church, ?mosque, ?synagogue

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
- слов: 20
- ~Purim, ~Rosh Hashanah, ~Yom Kippur, +Advent, +Christmas, +Diwali, +Easter, +Eid, +Epiphany, +Good Friday, +Hanukkah, +Holi, +Lent, +Palm Sunday, +Passover, +Pentecost, +Ramadan, ?Christmas, ?Diwali, ?Easter

### RELIGIOUS LEADERS  `religious_leaders`
- правило: Titles of religious leaders
- тип связи: `is_a`, базовая сложность 0.3
- слов: 23
- ~cardinal (cardinal_church), +abbot, +bishop, +chaplain, +dalai lama, +deacon, +elder (elder_church), +imam, +minister, +missionary, +monk, +nun, +pastor, +pope, +preacher, +priest, +rabbi, ?bishop, ?chaplain, ?imam, ?monk, ?priest, ?rabbi

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


## Тема: skills

### CARD TRICKS  `card_tricks`
- правило: Terms used in performing card tricks
- тип связи: `found_in`, базовая сложность 0.5
- слов: 12
- ~control, ~cut, ~double lift, ~false shuffle, ~flourish, ~force, ~pass, ~reveal, ~spread, !palm (palm_hand), !shuffle (shuffle_cards), !sleight

### COCKTAILS  `cocktails`
- правило: Named mixed drinks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 27
- ~daiquiri, ~negroni, ~pina colada, ~spritz, +bloody mary, +cosmopolitan, +mai tai, +manhattan, +margarita, +martini, +mimosa, +mojito, +moscow mule, +mule, +old fashioned, +sangria, +sour, +stirred, +tom collins, +whiskey sour, ?cosmopolitan, ?manhattan, ?margarita, ?martini, ?mojito, ?negroni, xteas

### DANCE MOVES  `dance_moves`
- правило: Named dance moves
- тип связи: `is_a`, базовая сложность 0.4
- слов: 22
- ~moonwalk, ~shuffle (shuffle_dance), +dip, +floss, +hustle, +jump, +kick, +robot, +slide, +spin, +split, +sway, +tap (tap_dance), +turn, +twirl, +twist, ?dip, ?floss, ?moonwalk, ?spin, ?twist, !wave (wave_dance)

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

### KNOTS  `knots`
- правило: Named knots tied in rope
- тип связи: `is_a`, базовая сложность 0.45
- слов: 24
- ~clove, ~clove hitch, ~cobra, ~double davy, ~figure eight, ~fisherman knot, ~granny knot, ~half hitch, ~hitch, ~sheet bend, ~slip knot, ~splice, ~Square, ~square knot, ~taut line, ~timber hitch, ~trucker hitch, ?bowline, ?clove hitch, ?figure eight, ?sheet bend, !bight, !bowline, !overhand

### PIZZA STYLES  `pizza_styles`
- правило: Regional styles of pizza
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~flatbread, +California, +Chicago, +chicago deep dish, +Detroit, +neapolitan, +new york, +sicilian, +stuffed crust, +tavern, +thin crust, ?Detroit, ?neapolitan, ?new york, ?sicilian, !calzone, !focaccia

### POKER HANDS  `poker_hands`
- правило: Hands that can be dealt in poker
- тип связи: `is_a`, базовая сложность 0.4
- слов: 16
- +flush, +four of a kind, +full house, +high card, +pair, +royal, +royal flush, +straight, +straight flush, +three of a kind, +trips, +two pair, ?flush, ?full house, ?pair, ?straight

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

### YOGA POSES  `yoga_poses`
- правило: Named poses used in yoga
- тип связи: `is_a`, базовая сложность 0.45
- слов: 23
- ~boat, ~child, ~cobra, ~crow, ~downward dog, ~half moon, ~lotus, ~mountain, ~pigeon, ~plank, ~tree, ~triangle, ~warrior, ?child, ?cobra, ?downward dog, ?lotus, ?mountain, ?pigeon, ?plank, ?tree, ?warrior, !bridge (bridge_move)


## Тема: sports

### ACTION SPORTS  `action_sports`
- правило: What belongs to the group «Action Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +bmx, +skating, +snowboarding, +surfing

### ACTIVE GAMES  `active_games`
- правило: What belongs to the group «Active Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +capture the flag, +dodgeball, +frisbee, !cornhole

### AIR BALLOONS  `air_balloons`
- правило: What belongs to the group «Air Balloons» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +air, +basket, +helium, +rubber

### AIR TRANSPORT  `air_transport`
- правило: What belongs to the group «Air Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +airplane, +glider, +helicopter, +hot air balloon

### ARCADE GAMES  `arcade_games`
- правило: What belongs to the group «Arcade Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +air hockey, +arcade, +claw machine, +Donkey Kong

### ATHLETIC  `athletic`
- правило: What belongs to the group «Athletic» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +fit, +sneakers, +sports, +training

### ATHLETIC EQUIPMENT  `athletic_equipment`
- правило: What belongs to the group «Athletic Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +cleats, +goggles, +helmet, +shin guards

### BALLET  `ballet`
- правило: What belongs to the group «Ballet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 15
- +ballerina, +barre, +giselle, +graceful, +leap, +pirouette, +pointe, +reverence, +stage, +swan lake, +tutu, !arabesque, !pli, xbattement, xplie

### BALLET MOVEMENTS  `ballet_movements`
- правило: What belongs to the group «Ballet Movements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +grand jet, !arabesque, !pirouette, !pli

### BALLET POSITIONS  `ballet_positions`
- правило: What belongs to the group «Ballet Positions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +grand, !arabesque, !pli, !tendu, xplie

### BALLET PRODUCTIONS  `ballet_productions`
- правило: What belongs to the group «Ballet Productions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +giselle, +nutcracker, +Sleeping Beauty, +swan lake

### BALLET TERMS  `ballet_terms`
- правило: What belongs to the group «Ballet Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !arabesque, !pirouette, !tendu, xplie

### BALLOON  `balloon`
- правило: What belongs to the group «Balloon» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 5
- +air, +festival, +float, +helium, +rubber

### BALLOONS  `balloons`
- правило: What belongs to the group «Balloons» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 6
- +float, +helium, +inflate, +ribbon, +rubber, +string

### BALLROOM DANCES  `ballroom_dances`
- правило: What belongs to the group «Ballroom Dances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +foxtrot, +rumba, +tango, +viennese, +waltz, !quickstep

### BASEBALL EQUIPMENT  `baseball_equipment`
- правило: Physical equipment used to play a game of baseball
- тип связи: `used_in`, базовая сложность 0.25
- слов: 15
- ~ball (ball_sphere), +base, +bat (bat_equipment), +batting glove, +cap, +chest protector, +cleats, +glove, +helmet, +mask, +mitt, +pine tar, +plate (plate_base), +rosin bag, +shin guard

### BASEBALL PITCHES  `baseball_pitches`
- правило: What belongs to the group «Baseball Pitches» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +curve, +knuckle, +sinker, +slider

### BASEBALL TEAMS  `baseball_teams`
- правило: What belongs to the group «Baseball Teams» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +cardinals, +Giants, +Rangers, +Tigers

### BASEBALL WORDS  `baseball_words`
- правило: Words used to describe plays, places or roles in a baseball game
- тип связи: `found_in`, базовая сложность 0.3
- слов: 27
- ~diamond (diamond_field), +bullpen, +bunt, +catcher, +curveball, +double play, +dugout, +error, +fastball, +foul, +grand slam, +home run, +infield, +inning, +lineup, +mound (mound_baseball), +outfield, +pitch (pitch_throw), +pitcher (pitcher_baseball), +shortstop, +slider, +steal, +strike (strike_baseball), +triple, +umpire, +walk, !single (single_baseball)

### BASKETBALL PLAYERS  `basketball_players`
- правило: What belongs to the group «Basketball Players» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 8
- +bird, +curry, +durant, +irving, +James, +Jordan, +shaq, !oneal

### BASKETBALL TEAMS  `basketball_teams`
- правило: What belongs to the group «Basketball Teams» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 6
- +Bulls, +Celtics, +heat, +Lakers, +thunder, +warriors

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

### BOARD GAME ACTIONS  `board_game_actions`
- правило: What belongs to the group «Board Game Actions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 4
- +draw, +move, +pass, +skip

### BOARD GAME NIGHT  `board_game_night`
- правило: What belongs to the group «Board Game Night» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +chess, +clue, +monopoly, +scrabble

### BOARD GAME TYPES  `board_game_types`
- правило: What belongs to the group «Board Game Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +backgammon, +checkers, +chess, +go

### BOARD GAMES WITH PIECES  `board_games_with_pieces`
- правило: What belongs to the group «Board Games With Pieces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~backgammon, +checkers, +go, xparcheesi

### BOARD SPORTS  `board_sports`
- правило: What belongs to the group «Board Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +skateboarding, +snowboarding, !surfboards, !wakeboarding

### OUTDOOR ACTIVITIES  `camping_and_outdoors`
- правило: Recreational activities done outdoors
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- ~birdwatching, ~geocaching, ~picnicking, +backpacking, +biking, +camping, +canoeing, +climbing, +fishing, +hiking, +hunting, +kayaking, +rafting, +running, +sailing, +skiing, +snorkeling, +surfing

### CAR TRANSPORT  `car_transport`
- правило: What belongs to the group «Car Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +hitchhike, +lyft, +taxi, +Uber

### CARD GAME ACTIONS  `card_game_actions`
- правило: What belongs to the group «Card Game Actions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 10
- +ante, +bluff, +deal, +discard, +draw, +flip, +fold, +hit, +pass, +split

### CARD GAME KIT  `card_game_kit`
- правило: What belongs to the group «Card Game Kit» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +chips, +dealer, +deck, +felt

### CARD GAME TERMS  `card_game_terms`
- правило: What belongs to the group «Card Game Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 7
- +ante, +bluff, +call, +deal, +fold, +raise, +trick

### CASINO GAMES  `casino_games`
- правило: What belongs to the group «Casino Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- +blackjack, +cards, +craps, +poker, +roulette, +slots, !baccarat

### CHESS ENDGAME  `chess_endgame`
- правило: What belongs to the group «Chess Endgame» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +checkmate, +stalemate, !en passant, !zugzwang

### CLASSIC ARCADE GAMES  `classic_arcade_games`
- правило: What belongs to the group «Classic Arcade Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Asteroids, +pacman, !Frogger, !Galaga

### CLASSIC BOARD GAMES  `classic_board_games`
- правило: What belongs to the group «Classic Board Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 8
- +clue, +mastermind, +monopoly, +mouse trap, +operation, +risk, +scrabble, +sorry

### CLASSICAL BALLET  `classical_ballet`
- правило: What belongs to the group «Classical Ballet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +corps de ballet, +en pointe, +grand jet, +pas de deux

### CLASSICAL BALLETS  `classical_ballets`
- правило: What belongs to the group «Classical Ballets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +don quixote, +giselle, +nutcracker, +swan lake

### COMBAT SPORTS  `combat_sports`
- правило: What belongs to the group «Combat Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 7
- +boxing, +fencing, +judo, +karate, +martial arts, +taekwondo, +wrestling

### CONTACT SPORTS  `contact_sports`
- правило: What belongs to the group «Contact Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +boxing, +hockey, +rugby, +wrestling

### CUE GAME  `cue_game`
- правило: What belongs to the group «Cue Game» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +billiards, +eight ball, +pool cue, +snooker

### CYCLING WORDS  `cycling_words`
- правило: Words used about riding and racing bicycles
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- +brake, +cadence, +chain, +drafting, +gear, +handlebar, +helmet, +jersey, +pedal, +peloton, +saddle, +spoke, +sprint, +tire, +tour, +trail

### DICE GAMES  `dice_games`
- правило: What belongs to the group «Dice Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +craps, !bunco, !farkle, !yahtzee

### EASTERN SPORTS  `eastern_sports`
- правило: What belongs to the group «Eastern Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +ping pong, +sumo, +yoga, !wushu

### ENGINE TRANSPORTATION  `engine_transportation`
- правило: What belongs to the group «Engine Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +airplane, +car, +ship, +train

### EXTREME AIR SPORTS  `extreme_air_sports`
- правило: What belongs to the group «Extreme Air Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bungee jumping, +hang gliding, +wind resistance, !skydiver

### EXTREME SPORTS  `extreme_sports`
- правило: What belongs to the group «Extreme Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 9
- +base jumping, +bungee, +bungee jumping, +ice diving, +parkour, +rock climbing, +skydiving, +snowboarding, +surfing

### FAMOUS ATHLETES  `famous_athletes`
- правило: What belongs to the group «Famous Athletes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Ali, +hawk, +lebron, +woods

### FISHING THINGS  `fishing_things`
- правило: Things used to catch fish
- тип связи: `used_in`, базовая сложность 0.3
- слов: 18
- ~bobber, ~fly (fly_lure), ~waders, +bait, +boat, +cooler, +hook (hook_fishing), +line (line_cord), +lure, +net, +pole, +reel (reel_fishing), +rod, +sinker, +spear, +tackle box, +trap, +worm

### FITNESS  `fitness`
- правило: What belongs to the group «Fitness» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 7
- +aerobics, +cardio, +condition, +crossfit, +exercise, +form, +health

### FITNESS ACTIVITIES  `fitness_activities`
- правило: What belongs to the group «Fitness Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +aerobics, +pilates, +yoga, +zumba

### FITNESS CLASSES  `fitness_classes`
- правило: What belongs to the group «Fitness Classes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +pilates, +spinning, +yoga, +zumba

### FITNESS STYLES  `fitness_styles`
- правило: What belongs to the group «Fitness Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +barre, +pilates, +yoga, +zumba

### FOOTBALL  `football`
- правило: What belongs to the group «Football» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +field, +goal, +stadium, +team

### FOOTBALL TERMS  `football_terms`
- правило: What belongs to the group «Football Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +goal, +pass, +tackle, +touchdown

### FOOTBALL WORDS  `football_words`
- правило: Words used to describe plays and roles in American football
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~sack (sack_football), +blitz, +down, +end zone, +field goal, +fumble, +helmet, +huddle, +interception, +kickoff, +lineman, +punt, +quarterback, +receiver, +referee, +safety, +snap, +tackle, +touchdown, +yard line

### FOR WATER SPORTS  `for_water_sports`
- правило: What belongs to the group «For Water Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +kayak, +scuba diving, +surfboard, +water skiing

### GAME  `game`
- правило: What belongs to the group «Game» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +checkers, +chess, +domino, +scrabble

### GAME BASICS  `game_basics`
- правило: What belongs to the group «Game Basics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 5
- +avatar, +console, +controller, +graphics, +level

### GAME CONSOLES  `game_consoles`
- правило: What belongs to the group «Game Consoles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +dreamcast, +Genesis, +switch, +wii

### GAME DIFFICULTY  `game_difficulty`
- правило: What belongs to the group «Game Difficulty» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +easy, +expert, +hard, +medium

### GAME GENRES  `game_genres`
- правило: What belongs to the group «Game Genres» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 8
- +adventure, +arcade, +idle, +match three, +puzzle, +role play, +shooter, +simulation

### GAME NIGHT  `game_night`
- правило: What belongs to the group «Game Night» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +bingo, +darts, +dominoes, +uno

### GAME NIGHT ESSENTIALS  `game_night_essentials`
- правило: What belongs to the group «Game Night Essentials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +board games with pieces, +scoreboard, +snacks, +timer

### GAME TYPES  `game_types`
- правило: What belongs to the group «Game Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +arcade, +puzzle, +simulation, +strategy

### GAMES  `games`
- правило: What belongs to the group «Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 14
- +arcade, +cards, +checkers, +chess, +domino, +laser tag, +monopoly, +puzzle, +scrabble, +simulation, +Solitaire, +sport, +strategy, !charades

### GAMES OF CHANCE  `games_of_chance`
- правило: What belongs to the group «Games Of Chance» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 6
- +bingo, +blackjack, +craps, +lottery, +roulette, !baccarat

### GAMES WITH A BALL  `games_with_a_ball`
- правило: What belongs to the group «Games With A Ball» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +basketball, +soccer, +tennis, +volleyball

### GAMES WITH BOARDS  `games_with_boards`
- правило: What belongs to the group «Games With Boards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +checkers, +chess, +monopoly, +scrabble

### GOLF WORDS  `golf_words`
- правило: Words used to describe play and equipment in golf
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bunker (bunker_golf), ~green (green_golf), ~iron (iron_golf), +birdie, +bogey, +caddy, +course, +driver, +eagle, +fairway, +flag, +hole in one, +par, +putter, +rough, +sand trap, +tee, +wedge

### GYM EQUIPMENT  `gym_equipment`
- правило: Equipment used for exercise in a fitness gym
- тип связи: `used_in`, базовая сложность 0.25
- слов: 24
- ~dumbbells, ~kettlebell, +barbell, +dumbbell, +elliptical, +foam roller, +jump rope, +mat, +medicine ball, +pull up bar, +punching bag, +resistance band, +rope, +rowing machine, +stair climber, +stationary bike, +treadmill, +weights, ?barbell, ?elliptical, ?kettlebell, ?treadmill, !bench (bench_seat), !club (club_stick)

### HOCKEY WORDS  `hockey_words`
- правило: Words used to describe plays and gear in ice hockey
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~zamboni, +blue line, +crease, +faceoff, +goalie, +helmet, +icing, +net, +pad, +penalty box, +period, +power play, +puck, +rink, +skate, +stick (stick_hockey), !check (check_hockey), !slapshot

### HOT AIR BALLOON  `hot_air_balloon`
- правило: What belongs to the group «Hot Air Balloon» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +balloon, +basket, +flight, +gas

### INDIVIDUAL SPORTS  `individual_sports`
- правило: What belongs to the group «Individual Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +archery, +chess, +darts, +Golf

### LAND TRANSPORT  `land_transport`
- правило: What belongs to the group «Land Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +moped, +scooter, +Subway, +tram

### MAN POWERED TRANSPORT  `man_powered_transport`
- правило: What belongs to the group «Man Powered Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +bicycle, +scooter, +skateboard, !rowboat

### MARTIAL ARTS  `martial_arts`
- правило: Fighting sports and self defense disciplines
- тип связи: `is_a`, базовая сложность 0.3
- слов: 22
- ~capoeira, ~kendo, +aikido, +boxing, +dojo, +fencing, +judo, +jujitsu, +karate, +kickboxing, +kung fu, +muay thai, +sumo, +taekwondo, +wrestling, ?aikido, ?boxing, ?judo, ?karate, ?kung fu, ?taekwondo, xbokken

### MOBILE GAMES GENRE  `mobile_games_genre`
- правило: What belongs to the group «Mobile Games Genre» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +battle royale, +idle, +match three, +platformer

### MODES OF TRANSPORT  `modes_of_transport`
- правило: What belongs to the group «Modes Of Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gondola, +rickshaw, +tram, !dogsled

### MODES OF TRANSPORTATION  `modes_of_transportation`
- правило: What belongs to the group «Modes Of Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +airplane, +airship, +bicycle, +boat

### NBA TEAMS  `nba_teams`
- правило: What belongs to the group «Nba Teams» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +bull, +Bulls, +celtic, +Lakers, +spur, +warrior, +warriors

### NHL TEAMS  `nhl_teams`
- правило: What belongs to the group «Nhl Teams» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +capitals, +lightning, +penguins, +Rangers

### OLYMPIC CITIES  `olympic_cities`
- правило: What belongs to the group «Olympic Cities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +Beijing, +London, +rio, +Tokyo

### OLYMPIC EVENTS  `olympic_events`
- правило: What belongs to the group «Olympic Events» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 13
- +archery, +discus, +diving, +fencing, +gymnastics, +hammer, +javelin, +judo, +pole vault, +rowing, +swimming, +weightlifting, +wrestling

### OLYMPIC HOST CITIES  `olympic_host_cities`
- правило: What belongs to the group «Olympic Host Cities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 8
- +Barcelona, +London, +nagano, +rio, +sochi, +Tokyo, +Turin, !lillehammer

### OLYMPIC SPORTS  `olympic_sports`
- правило: Sports contested at the modern Olympic Games
- тип связи: `is_a`, базовая сложность 0.25
- слов: 47
- ~bobsled, ~breakdance, +archery, +badminton, +biathlon, +boxing, +canoeing, +cricket, +curling, +cycling, +diving, +fencing, +figure skating, +gymnastics, +hurdles, +javelin, +judo, +luge, +marathon, +polo, +rowing, +sailing, +shot put, +skateboard, +skating, +skiing, +surfing, +swimming, +taekwondo, +tennis, +track, +triathlon, +weightlifting, +wrestling, ?archery, ?bobsled, ?boxing, ?curling, ?diving, ?fencing, ?gymnastics, ?judo, ?rowing, ?skiing, ?swimming, ?weightlifting, ?wrestling

### OLYMPIC SWIMMING STROKES  `olympic_swimming_strokes`
- правило: What belongs to the group «Olympic Swimming Strokes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +backstroke, +breaststroke, +butterfly, +freestyle

### OLYMPICS  `olympics`
- правило: What belongs to the group «Olympics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +equestrian, +medal, +rings, +torch

### ONLINE GAME  `online_game`
- правило: What belongs to the group «Online Game» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +players, +quests, +skill trees, +virtual worlds

### OUTDOOR GAMES  `outdoor_games`
- правило: What belongs to the group «Outdoor Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +cricket, +croquet, !bocce, !horseshoes

### OUTDOOR SPORTS  `outdoor_sports`
- правило: What belongs to the group «Outdoor Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +cycling, +football, +running, +tennis

### PARTY GAMES  `party_games`
- правило: What belongs to the group «Party Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +taboo, +trivia, !charades, !pictionary

### PASSPORT  `passport`
- правило: What belongs to the group «Passport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 7
- +document, +expiry, +expiry date, +identity, +photo, +travel, +Visa

### PUB GAMES  `pub_games`
- правило: What belongs to the group «Pub Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 6
- +8 ball, +billiards, +bowling, +darts, +Pinball, !shuffleboard

### RACING SPORTS  `racing_sports`
- правило: Sports where competitors race to finish first
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- +cross country, +cycling, +dog sled racing, +drag racing, +f1, +horse racing, +hurdles, +karting, +marathon, +motocross, +nascar, +rally, +relay, +rowing, +sailing, +speed skating, +sprint, +swimming, +triathlon, ?horse racing, ?motocross

### RACKET SPORTS  `racket_sports`
- правило: What belongs to the group «Racket Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +badminton, +racquetball, +tennis, !padel, !pickleball

### RACQUET SPORTS  `racquet_sports`
- правило: What belongs to the group «Racquet Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +badminton, +racquetball, +tennis, !pickleball

### RECREATION GAMES  `recreation_games`
- правило: What belongs to the group «Recreation Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 5
- +8 ball, +air hockey, +bowling, +darts, +eight ball

### SOCCER TEAM  `soccer_team`
- правило: What belongs to the group «Soccer Team» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +coach, +hooligans, +players, +stadium

### SOCCER WORDS  `soccer_words`
- правило: Words used to describe plays and roles in soccer
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~pitch (pitch_field), +assist, +corner kick, +defender, +dribble, +free kick, +goal, +goalkeeper, +header, +midfielder, +net, +offside, +penalty, +red card, +striker, +throw in, +whistle, +yellow card

### SPORT EVENTS  `sport_events`
- правило: What belongs to the group «Sport Events» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +olympiad, +Super Bowl, +Wimbledon, +World Cup

### SPORTING VERBS  `sporting_verbs`
- правило: What belongs to the group «Sporting Verbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +dive, +dribble, +sprint, +tackle

### SPORTS  `sports`
- правило: What belongs to the group «Sports» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 22
- +archery, +baseball, +basketball, +bowling, +boxing, +climbing, +cricket, +fencing, +Golf, +hockey, +judo, +karate, +lacrosse, +luge, +motorsport, +polo, +rugby, +soccer, +surfing, +swimming, +tennis, +track

### SPORTS ARENAS  `sports_arenas`
- правило: What belongs to the group «Sports Arenas» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +coliseum, +dome, +rink, +stadium

### SPORTS AWARDS  `sports_awards`
- правило: What belongs to the group «Sports Awards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 5
- +championship, +gold medal, +mvp, +plaque, +trophy

### BALLS  `sports_balls`
- правило: Balls used in different sports
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- +baseball, +basketball, +beach ball, +bowling ball, +cricket ball, +football, +golf ball, +medicine ball, +ping pong ball, +rugby ball, +soccer ball, +softball, +tennis ball, +volleyball

### SPORTS EQUIPMENT  `sports_equipment`
- правило: What belongs to the group «Sports Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +glove, +net, +puck, +racket

### SPORTS GEAR  `sports_gear`
- правило: What belongs to the group «Sports Gear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 8
- +cleats, +dumbbell, +glove, +goggles, +helmet, +jump rope, +puck, +racket

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

### SPORTS TERMS  `sports_terms`
- правило: What belongs to the group «Sports Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +foul, +goal, +knockout, +out

### SPORTS VENUES  `sports_venues`
- правило: Places built for playing or watching sports
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~diamond (diamond_field), ~pitch (pitch_field), ~ring (ring_arena), +alley, +arena, +ballpark, +course, +dojo, +dome, +field, +gym, +pool, +racetrack, +rink, +stadium, +track, +velodrome, !court (court_sport)

### SPORTSWEAR  `sportswear`
- правило: What belongs to the group «Sportswear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +buff, +cap, +hoodie, +knee socks

### STEAM BATH  `steam_bath`
- правило: What belongs to the group «Steam Bath» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +hammam, +sauna, !banya, !onsen

### STRATEGIC BOARD GAMES  `strategic_board_games`
- правило: What belongs to the group «Strategic Board Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +checkers, +chess, +go, +othello

### STRATEGY GAMES  `strategy_games`
- правило: What belongs to the group «Strategy Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 10
- +backgammon, +checkers, +chess, +diplomacy, +go, +logic, +othello, +risk, +scrabble, !stratego

### SUMMER GAMES  `summer_games`
- правило: What belongs to the group «Summer Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +cricket, +field, +swimming, +volleyball

### SUMMER OLYMPIC GAMES  `summer_olympic_games`
- правило: What belongs to the group «Summer Olympic Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 6
- +athletics, +boxing, +fighting, +gymnastics, +team sports, +triathlon

### SUMMER OLYMPICS  `summer_olympics`
- правило: What belongs to the group «Summer Olympics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- +archery, +cycling, +equestrian, +gymnastics, +rowing, +swimming, +triathlon

### TEAM  `team`
- правило: What belongs to the group «Team» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +goals, +leader, +members, +tasks

### TEAM SPORTS  `team_sports`
- правило: Sports played by two opposing teams
- тип связи: `is_a`, базовая сложность 0.15
- слов: 26
- +baseball, +basketball, +cricket, +dodgeball, +field hockey, +football, +handball, +hockey, +kickball, +lacrosse, +netball, +polo, +rugby, +soccer, +softball, +ultimate frisbee, +volleyball, +water polo, ?basketball, ?football, ?handball, ?hockey, ?rugby, ?soccer, ?volleyball, ?water polo

### TENNIS WORDS  `tennis_words`
- правило: Words used to describe play and scoring in tennis
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~tiebreak, +Ace, +backhand, +baseline, +court (court_sport), +deuce, +fault, +forehand, +lob, +love, +match point, +net, +racket, +rally, +serve, +set (set_tennis), +umpire, +volley

### TRANSPORT  `transport`
- правило: What belongs to the group «Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 13
- +airplane, +driving, +flying, +gondola, +roads, +sailing, +ship, +traffic, +train, +transit, +truck, +vehicles, +walking

### TRANSPORTATION  `transportation`
- правило: What belongs to the group «Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 8
- +air, +bus, +ferry, +rail, +road, +taxi, +train, +water

### TRANSPORTED  `transported`
- правило: What belongs to the group «Transported» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +cargo, +freight, +goods, +haul

### TRANSPORTS GOODS  `transports_goods`
- правило: What belongs to the group «Transports Goods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +canister, +container, +crate, +suitcase

### TWO WHEELED TRANSPORT  `two_wheeled_transport`
- правило: What belongs to the group «Two Wheeled Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +bicycle, +dirt bike, +motorbike, +scooter

### VERTICAL TRANSPORTATION  `vertical_transportation`
- правило: What belongs to the group «Vertical Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 5
- +elevator, +escalator, +lift, +stairs, !funicular

### VIDEO GAME  `video_game`
- правило: What belongs to the group «Video Game» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +console, +controller, +lives, +pixel

### VIDEO GAME BOSSES  `video_game_bosses`
- правило: What belongs to the group «Video Game Bosses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bowser, !ganondorf, !robotnik, !sephiroth

### VIDEO GAME CONTROLLERS  `video_game_controllers`
- правило: What belongs to the group «Video Game Controllers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +dance pad, +joystick, +steering, !gamepad, !trackball

### VIDEO GAME GENRES  `video_game_genres`
- правило: What belongs to the group «Video Game Genres» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 10
- +action, +horror, +platformer, +puzzle, +racing, +shooter, +simulation, +strategy, !metroidvania, !roguelike

### VIDEO GAME PLATFORMS  `video_game_platforms`
- правило: What belongs to the group «Video Game Platforms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Nintendo, +playstation, +steam, +xbox

### VIDEO GAMES  `video_games`
- правило: What belongs to the group «Video Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +controller, +disc, +Nintendo, +Sony

### VOLLEYBALL  `volleyball`
- правило: What belongs to the group «Volleyball» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 5
- +dig, +net, +pass, +serve, +spike

### WATER SPORTS  `water_sports`
- правило: Sports played in or on the water
- тип связи: `is_a`, базовая сложность 0.25
- слов: 26
- ~kitesurfing, ~paddleboarding, ~wakeboarding, ~windsurfing, +canoeing, +diving, +kayaking, +rafting, +rowing, +sailing, +scuba, +snorkeling, +surfing, +swimming, +synchronized swimming, +water polo, +water skiing, ?diving, ?kayaking, ?paddleboarding, ?rowing, ?sailing, ?surfing, ?swimming, ?water polo, ?windsurfing

### WATER TRANSPORT  `water_transport`
- правило: What belongs to the group «Water Transport» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +barge, +boat, +raft, +ship

### WATER TRANSPORTATION  `water_transportation`
- правило: What belongs to the group «Water Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +boat, +ferry, +ship, +submarine

### WAYS OF TRANSPORTATION  `ways_of_transportation`
- правило: What belongs to the group «Ways Of Transportation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 5
- +air, +maritime, +railway, +road, +water

### WINTER OLYMPICS  `winter_olympics`
- правило: What belongs to the group «Winter Olympics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +biathlon, +bobsleigh, +figure skating, +luge, +skeleton, +slalom, +snowboard

### WINTER SPORTS  `winter_sports`
- правило: Sports played on snow or ice
- тип связи: `is_a`, базовая сложность 0.25
- слов: 22
- ~bobsled, ~snowshoeing, ~tobogganing, +alpine skiing, +biathlon, +curling, +figure skating, +hockey, +ice climbing, +luge, +skating, +skeleton, +skiing, +sledding, +snowboarding, +speed skating, ?biathlon, ?bobsled, ?curling, ?luge, ?skiing, ?snowboarding

### WORD GAMES  `word_games`
- правило: What belongs to the group «Word Games» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 7
- +anagram, +crossword, +hangman, +mad libs, +scrabble, +word search, !boggle


## Тема: technology

### COMPUTER ACTIONS  `computer_actions`
- правило: Actions done while using a computer
- тип связи: `does_action`, базовая сложность 0.25
- слов: 24
- +click, +close, +copy, +delete, +download, +drag, +install, +log in, +paste, +print, +refresh, +restart, +save, +scroll (scroll_screen), +search, +share, +type, +undo, +upload, +Zoom, ?copy, ?delete, ?paste, ?save

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
- слов: 20
- +archive, +attachment, +backup, +document, +draft (draft_document), +file (file_computer), +folder, +image, +json, +pdf, +presentation, +rar, +shortcut, +spreadsheet, +template, +trash, +video, +wav, +zip, xxlsx

### GADGETS  `gadgets`
- правило: Small electronic devices people own
- тип связи: `is_a`, базовая сложность 0.25
- слов: 26
- ~dashcam, ~remote (remote_device), +camera, +computer, +console, +doorbell, +drone, +e-reader, +earbuds, +fitness tracker, +headphones, +laptop, +phone, +printer, +projector, +scanner, +smartphone, +smartwatch, +speaker, +tablet, +thermostat, +watch (watch_object), ?camera, ?drone, ?laptop, ?tablet

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
- слов: 26
- +ancient, +ancient greece, +Antiquity, +baroque, +Bronze Age, +byzantine, +byzantine empire, +Colonial, +Dark Ages, +gilded, +Great Depression, +Ice Age, +industrial, +Industrial Revolution, +Iron Age, +medieval, +Middle Ages, +modern, +renaissance, +Roaring Twenties, +Space Age, +Stone Age, +Victorian, ?renaissance, ?Stone Age, ?Victorian

### HOLIDAYS  `holidays`
- правило: Holidays widely celebrated in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 24
- ~Juneteenth, ~Kwanzaa, +April Fools, +Christmas, +Columbus Day, +Easter, +Fathers Day, +Groundhog Day, +Halloween, +Hanukkah, +Independence Day, +Labor Day, +Memorial Day, +Mothers Day, +New Year, +Passover, +Presidents Day, +Thanksgiving, +Valentine's Day, +Veterans Day, ?Christmas, ?Easter, ?Halloween, ?Thanksgiving

### MONTHS  `months`
- правило: Months of the Gregorian calendar year
- тип связи: `is_a`, базовая сложность 0.1
- слов: 16
- +April, +August, +December, +February, +January, +July, +June, +march (march_month), +November, +October, +September, ?April, ?August, ?June, ?October, ?September

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
- слов: 9
- +Autumn, +fall, +spring (spring_season), +summer, +winter, ?Autumn, ?fall, ?summer, ?winter

### QUICK WORDS  `speed_of_time`
- правило: Words meaning that something happens without delay
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- ~abruptly, ~at once, ~hastily, ~immediately, ~instantly, ~momentarily, ~promptly, ~quickly, ~right away, ~shortly, ~suddenly, ~swiftly

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


## Тема: transport

### AIR TRAVEL  `air_travel`
- правило: What belongs to the group «Air Travel» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 6
- +attendant, +boarding, +captain, +crew, +passenger, +stewardess

### AIRCRAFT  `aircraft`
- правило: Machines that fly through the air carrying people or cargo
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~biplane, +airplane, +airship, +balloon, +blimp, +cargo plane, +drone, +glider, +helicopter, +jet, +rocket, +seaplane, +shuttle, +ultralight, +Zeppelin

### AIRPLANE  `airplane`
- правило: What belongs to the group «Airplane» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +cockpit, +engine, +tail, +wings

### AIRPORT WORDS  `airport_words`
- правило: Words for things, places or roles you encounter at an airport
- тип связи: `found_in`, базовая сложность 0.25
- слов: 29
- ~currencies, ~gate (gate_airport), ~jetway, ~languages, +aircraft, +airlines, +aisle, +baggage, +boarding pass, +carousel, +checkpoint, +cockpit, +concourse, +control tower, +customs, +duty free, +hangar, +layover, +luggage, +passport, +pilot, +runway, +seatbelt, +security, +steward, +tarmac, +terminal, +ticket (ticket_admission), +tray table

### BEAUTY CARE  `beauty_care`
- правило: What belongs to the group «Beauty Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +makeup, +nail care, +skincare, !haircare

### BIPLANE  `biplane`
- правило: What belongs to the group «Biplane» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +aircraft, +flying, +piloting, !aileron

### BOAT TYPES  `boat_types`
- правило: What belongs to the group «Boat Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +canoe, +catamaran, +dinghy, +kayak

### BOATS AND SHIPS  `boats`
- правило: Kinds of watercraft
- тип связи: `is_a`, базовая сложность 0.25
- слов: 24
- ~rowboat, +barge, +canoe, +catamaran, +cruise ship, +dinghy, +ferry, +freighter, +galley, +gondola, +houseboat, +kayak, +motorboat, +raft, +sailboat, +schooner, +speedboat, +submarine, +trawler, +tugboat, +yacht, ?barge, ?canoe, ?yacht

### BROADCAST  `broadcast`
- правило: What belongs to the group «Broadcast» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +radio, +satellite, +television, +transmitter

### BROADCASTING  `broadcasting`
- правило: What belongs to the group «Broadcasting» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +newscast, +radio, +studio, +telecast

### BROADWAY  `broadway`
- правило: What belongs to the group «Broadway» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +cats, +Chicago, +hamilton, +phantom

### BROADWAY THEATERS  `broadway_theaters`
- правило: What belongs to the group «Broadway Theaters» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +Gershwin, +majestic, +palace, !shubert

### BUYING A CAR  `buying_a_car`
- правило: What belongs to the group «Buying A Car» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +dealership, +haggle, +salesman, +test drive

### CAR  `car`
- правило: What belongs to the group «Car» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 20
- +airbag, +BMW, +coupe, +door, +engine, +headlights, +navigation system, +pickup, +roadster, +seat belt, +seatbelt, +sedan, +suv, +Tesla, +tire, +Toyota, +traffic jam, +transmission, +wheel, +wheels

### CAR BODIES  `car_bodies`
- правило: What belongs to the group «Car Bodies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +coupe, +hatchback, +sedan, +wagon

### CAR COMPONENTS  `car_components`
- правило: What belongs to the group «Car Components» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +brakes, +engine, +steering wheel, +transmission

### CAR DASHBOARD  `car_dashboard`
- правило: What belongs to the group «Car Dashboard» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +clock, +gauge, +odometer, +radio

### CAR DETAILS  `car_details`
- правило: What belongs to the group «Car Details» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +bumper, +dashboard, +fender, +headlight

### CAR ENGINE COMPONENTS  `car_engine_components`
- правило: What belongs to the group «Car Engine Components» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +cylinder block, +head gasket, +pistons, !camshaft

### CAR GEAR  `car_gear`
- правило: What belongs to the group «Car Gear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +brakes, +radiator, +seatbelt, !headrest

### CAR PARTS  `car_parts`
- правило: Physical parts of an ordinary passenger car
- тип связи: `part_of`, базовая сложность 0.2
- слов: 33
- ~gearshift, ~glovebox, +axle, +battery, +brake, +bumper, +clutch, +dashboard, +door, +engine, +exhaust, +fender, +gear, +headlight, +hood (hood_car), +horn (horn_sound), +ignition, +mirror, +muffler, +pedal, +radiator, +seat, +tire, +trunk (trunk_car), +wheel, +windshield, +wiper, ?brake, ?clutch, ?mirror, ?tire, ?wheel, ?wiper

### CAR RACING  `car_racing`
- правило: What belongs to the group «Car Racing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +drag, +drift, +formula 1, +nascar

### CAR SAFETY  `car_safety`
- правило: What belongs to the group «Car Safety» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +abs, +airbag, +seatbelt, !headrest

### CARBOHYDRATES  `carbohydrates`
- правило: What belongs to the group «Carbohydrates» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +bread, +pasta, +potato, +rice

### CARBONARA  `carbonara`
- правило: What belongs to the group «Carbonara» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +bacon, +egg, +parmesan, +pasta

### CARBONATE MINERALS  `carbonate_minerals`
- правило: What belongs to the group «Carbonate Minerals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +calcite, +dolomite, !aragonite, !siderite

### CARDINAL  `cardinal`
- правило: What belongs to the group «Cardinal» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 11
- +bird, +crimson, +direction, +east, +north, +number, +red, +robin, +south, +Vatican, +west

### CARDINALS  `cardinals`
- правило: What belongs to the group «Cardinals» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 8
- +borgia, +east, +north, +richelieu, +south, +west, +wolsey, !mazarin

### CARDS  `cards`
- правило: What belongs to the group «Cards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 9
- +Ace, +baseball, +debit, +hearts, +king, +magic, +rummy, +suits, +tarot

### CARETAKER  `caretaker`
- правило: What belongs to the group «Caretaker» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +babysitter, +guardian, +mother, +nurse

### CARNIVAL  `carnival`
- правило: What belongs to the group «Carnival» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 7
- +candy, +clown, +cotton, +ferris, +ferris wheel, +midway, +prize

### CARNIVAL RIDES  `carnival_rides`
- правило: What belongs to the group «Carnival Rides» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +bumper cars, +carousel, +ferris wheel, +tilt a whirl

### CARPENTERS WORKSHOP  `carpenters_workshop`
- правило: What belongs to the group «Carpenters Workshop» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +hammer, +measure, +sawdust, +workbench

### CARPENTRY  `carpentry`
- правило: What belongs to the group «Carpentry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 6
- +chisel, +clamp, +hammer, +mallet, +sander, +saw

### CARPENTRY JOINTS  `carpentry_joints`
- правило: What belongs to the group «Carpentry Joints» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !dovetail, !mortise, !rabbet, !tenon

### CHRISTMAS CAROL  `christmas_carol`
- правило: What belongs to the group «Christmas Carol» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +ghost, +marley, +scrooge, !cratchit

### CONSTRUCTION EQUIPMENT  `construction_equipment`
- правило: Large machines used on a building or road construction site
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~backhoe, ~compactor, ~paver, +bulldozer, +cement mixer, +crane (crane_machine), +digger, +drill rig, +dump truck, +excavator, +forklift, +grader, +hoist, +jackhammer, +loader, +roller, +scaffold, !trencher

### CREDIT CARD TYPES  `credit_card_types`
- правило: What belongs to the group «Credit Card Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +Discover, +Mastercard, +reward tier, +Visa

### CRUISE SHIP ZONES  `cruise_ship_zones`
- правило: What belongs to the group «Cruise Ship Zones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +atrium, +buffet, +lido deck, +promenade

### DWARF PLANETS  `dwarf_planets`
- правило: What belongs to the group «Dwarf Planets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Ceres, +eris, xhaumea, xmakemake

### ELECTRIC CAR  `electric_car`
- правило: What belongs to the group «Electric Car» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +battery, +car, +Charger, +charging station

### EMERGENCY VEHICLES  `emergency_vehicles`
- правило: Vehicles used by emergency services
- тип связи: `is_a`, базовая сложность 0.25
- слов: 12
- +ambulance, +cruiser, +fire truck, +hazmat truck, +helicopter, +ladder truck, +paramedic van, +patrol car, +police car, +rescue boat, +squad car, +tow truck

### EXOCARP  `exocarp`
- правило: What belongs to the group «Exocarp» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +avocados, +melons, +oranges, !papayas

### FAMILY RELATIONSHIPS  `family_relationships`
- правило: What belongs to the group «Family Relationships» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +brother, +father, +mother, +sister

### FICTIONAL PLANETS  `fictional_planets`
- правило: What belongs to the group «Fictional Planets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +krypton, +pandora, !arrakis, !tatooine

### GAS STATION  `gas_station_things`
- правило: Things found at an American gas station
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~squeegee, +air hose, +car wash, +coffee, +credit card reader, +diesel, +gas, +ice machine, +map, +nozzle, +oil (oil_motor), +pump, +receipt, +restroom, +snack, +windshield fluid

### HAVING A CAR  `having_a_car`
- правило: What belongs to the group «Having A Car» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +insurance, +license, +parking, +traffic

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

### HUMAN POWERED VEHICLES  `human_powered_vehicles`
- правило: What belongs to the group «Human Powered Vehicles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +bicycle, +roller skates, +skateboard, +tricycle

### INFANT CARE  `infant_care`
- правило: What belongs to the group «Infant Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +feeding, +nursing, +nurturing, +soothing

### JEEP CARS  `jeep_cars`
- правило: What belongs to the group «Jeep Cars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +cherokee, +renegade, +Wrangler, !wagoneer

### KINDS OF CARDS  `kinds_of_cards`
- правило: What belongs to the group «Kinds Of Cards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 4
- +business, +greeting, +membership, +playing

### KINSHIP  `kinship`
- правило: What belongs to the group «Kinship» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +affinity, +cousin, +father, +grandma

### LEADERSHIP QUALITIES  `leadership_qualities`
- правило: What belongs to the group «Leadership Qualities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +authority, +fairness, +initiative, +wisdom

### NASCAR  `nascar`
- правило: What belongs to the group «Nascar» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Daytona, +drafting, +talladega, !pitstop

### OUTER PLANETS  `outer_planets`
- правило: What belongs to the group «Outer Planets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +Jupiter, +Neptune, +Saturn, +Uranus

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

### PERSONAL CARE  `personal_care`
- правило: What belongs to the group «Personal Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +body wrap, +haircut, +manicure, !brow lamination

### PIRATE SHIP  `pirate_ship`
- правило: What belongs to the group «Pirate Ship» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +captain, +mast, +parrot, +plank

### PLANE  `plane`
- правило: What belongs to the group «Plane» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +drone, +glider, +helicopter, +jet

### PLANE TRAVEL HAZARDS  `plane_travel_hazards`
- правило: What belongs to the group «Plane Travel Hazards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +birds, +ice, +thunderstorm, +winds

### PLANE TYPES  `plane_types`
- правило: What belongs to the group «Plane Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +glider, +jet, !biplane, !floatplane

### PLANET  `planet`
- правило: What belongs to the group «Planet» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 14
- +atmosphere, +axis, +crater, +Earth, +Jupiter, +Mars, +Neptune, +planetary science, +Pluto, +Saturn, +stars, +terrain, +Venus, +water

### PLANETS WITH RINGS  `planets_with_rings`
- правило: What belongs to the group «Planets With Rings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +Jupiter, +Neptune, +Saturn, +Uranus

### REMOTE CONTROL VEHICLES  `remote_control_vehicles`
- правило: What belongs to the group «Remote Control Vehicles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +boat, +car, +drone, +helicopter

### ROAD ESSENTIALS  `road_essentials`
- правило: What belongs to the group «Road Essentials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +intersection, +parking lot, +tow truck, !guardrail

### ROAD HAZARDS  `road_hazards`
- правило: What belongs to the group «Road Hazards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +detour, +pothole, +roadblock, +speed bump

### ROAD SIGNS  `road_signs`
- правило: What belongs to the group «Road Signs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 13
- ~roadwork, +detour, +give way, +highway exits, +keep right, +merge, +no left turn, +one way, +parking, +speed limit, +stop, +two way traffic, +yield

### ROAD THINGS  `road_things`
- правило: Things you see on or beside a road
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~guardrail, ~shoulder (shoulder_road), ~streetlight, +bridge (bridge_structure), +cone, +crosswalk, +curb, +exit, +intersection, +lane, +median, +mile marker, +pothole, +ramp, +sidewalk, +sign, +speed bump, +toll booth, +traffic light, +tunnel

### ROAD TRAFFIC  `road_traffic`
- правило: What belongs to the group «Road Traffic» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +crossing, +intersection, +lane, +one way

### ROAD TYPES  `road_types`
- правило: What belongs to the group «Road Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +brick, +dirt, +gravel, +paved

### ROAD VEHICLES  `road_vehicles`
- правило: What belongs to the group «Road Vehicles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +bike, +bus, +car, +motorcycle

### ROADS  `roads`
- правило: What belongs to the group «Roads» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 6
- +alley, +avenue, +boulevard, +highway, +lane, +street

### ROADWAY FEATURES  `roadway_features`
- правило: What belongs to the group «Roadway Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 5
- +crosswalk, +median, +roundabout, +speed camera, !guardrail

### SAILING WORDS  `sailing_words`
- правило: Words used aboard a sailing boat
- тип связи: `found_in`, базовая сложность 0.4
- слов: 18
- ~anchor, ~boom, ~buoy, ~cabin (cabin_ship), ~deck, ~helm, ~hull, ~keel, ~knot, ~mast, ~oar, ~port, ~rope, ~rudder, ~sail (sail_cloth), ~starboard, ~stern, !bow (bow_ship)

### SCARY THINGS  `scary_things`
- правило: What belongs to the group «Scary Things» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +ghosts, +haunted house, +horror, +witch

### SELF CARE ACTIVITIES  `self_care_activities`
- правило: What belongs to the group «Self Care Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +bubble bath, +face mask, +journaling, +massage

### SHIP  `ship`
- правило: What belongs to the group «Ship» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 20
- +anchor, +anchored, +cabin boy, +captain, +clipper, +Corvette, +crew, +deck, +frigate, +galleon, +galley, +harbor, +junk, +navigation, +stern, +vessel, !brigantine, !longship, !trireme, xforepeak

### SHIP PARKING  `ship_parking`
- правило: What belongs to the group «Ship Parking» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +harbor, +pier, +port, +shipyard

### SHIP SAILS  `ship_sails`
- правило: What belongs to the group «Ship Sails» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +genoa, +jib, !mainsail, !spinnaker

### SHIP TYPES  `ship_types`
- правило: What belongs to the group «Ship Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +cruiser, +destroyer, +frigate, +galleon

### SHIPBUILDING  `shipbuilding`
- правило: What belongs to the group «Shipbuilding» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +dry dock, +keel, +rivet, !caulk

### SHIPBUILDING TERMS  `shipbuilding_terms`
- правило: What belongs to the group «Shipbuilding Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +hull, +keel, +mast, +rigging

### SHIPPING CONTAINERS  `shipping_containers`
- правило: What belongs to the group «Shipping Containers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +box, +envelope, +mailer, +tube

### SHIPS  `ships`
- правило: What belongs to the group «Ships» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 8
- +battleship, +cargo ship, +cruiser, +cutter, +ferry, +frigate, +sloop, +submarine

### SHIPWRECK CAUSES  `shipwreck_causes`
- правило: What belongs to the group «Shipwreck Causes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +breach, +iceberg, +shoal, +storm

### SHIPYARD  `shipyard`
- правило: What belongs to the group «Shipyard» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 8
- +berth, +boats, +bulkhead, +cranes, +dock, +gantry, +moor, !slipway

### SILK ROAD CITIES  `silk_road_cities`
- правило: What belongs to the group «Silk Road Cities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !bukhara, !kashgar, !samarkand, xturfan

### SKINCARE  `skincare`
- правило: What belongs to the group «Skincare» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 5
- +cleanser, +moisturizer, +serum, +sunscreen, +toner

### SPACE TRAVEL  `space_travel`
- правило: Things involved in traveling into space
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~spacesuit, ~station (station_place), +astronaut, +booster, +capsule, +countdown, +docking, +gravity, +lander, +launch, +mission, +module, +orbit, +rocket, +rover, +satellite, +shuttle, +telescope

### SPACESHIP  `spaceship`
- правило: What belongs to the group «Spaceship» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 7
- +asteroid, +astronaut, +comet, +eclipse, +orbit, +rocket, +shuttle

### TAROT CARD SUITS  `tarot_card_suits`
- правило: What belongs to the group «Tarot Card Suits» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +cups, +swords, +wands, !pentacles

### TAROT CARDS  `tarot_cards`
- правило: What belongs to the group «Tarot Cards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 7
- +death, +fool, +high priestess, +lovers, +tower, +world, !hierophant

### THINGS FOR CARS  `things_for_cars`
- правило: What belongs to the group «Things For Cars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +garage, +highway, +parking, +valet

### PEOPLE MOVERS  `things_that_carry_people`
- правило: Things built to carry a person from one place to another
- тип связи: `does_action`, базовая сложность 0.35
- слов: 18
- ~cable car, ~chairlift, ~elevator, ~escalator, ~ferry, ~gondola, ~moving walkway, ~plane (plane_aircraft), ~rickshaw, ~sled, ~stretcher, ~taxi, ~tram, ~wheelchair, +boat, +bus, +horse, +train

### THINGS WITH WHEELS  `things_with_wheels`
- правило: Everyday objects that have wheels as a normal part of their design
- тип связи: `has_property`, базовая сложность 0.25
- слов: 29
- ~cart, ~dolly, ~forklift, ~golf cart, ~gurney, ~lawnmower, ~roller skate, ~scooter, ~skateboard, ~stroller, ~suitcase, ~tractor, ~trailer (trailer_vehicle), ~tricycle, ~trolley, ~unicycle, ~wagon, ~wheelbarrow, ~wheelchair, +bike, +bus, +car, +train, +truck, +van, ?bike, ?car, ?skateboard, !rollerblade

### THINGS YOU CARRY  `things_you_carry`
- правило: What belongs to the group «Things You Carry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 8
- +baby, +bag, +basket, +briefcase, +groceries, +purse, +tray, +wallet

### TIME TRAVEL  `time_travel`
- правило: What belongs to the group «Time Travel» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +future, +paradox, +portal, +timeline

### TRAFFIC SIGNS  `traffic_signs`
- правило: Signs that direct drivers on the road
- тип связи: `is_a`, базовая сложность 0.3
- слов: 23
- +crossing, +crosswalk, +curve ahead, +dead end, +detour, +do not enter, +exit, +merge, +no entry, +no parking, +one way, +railroad, +school zone, +slow, +speed limit, +stop, +yield, ?detour, ?one way, ?slow, ?speed limit, ?stop, ?yield

### TRAIN  `train`
- правило: What belongs to the group «Train» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 13
- ~maglev, +bullet, +conductor, +depart, +diesel, +engine, +freight, +Metro, +railroad, +steam, +track, +tunnel, +wagon

### TRAIN CAR TYPES  `train_car_types`
- правило: What belongs to the group «Train Car Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +caboose, +dining, +freight, +sleeper

### TRAIN WORDS  `train_words`
- правило: Words for the parts, places and roles of railway travel
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~boxcar, +caboose, +conductor, +coupling, +crossing, +depot, +engine, +freight, +locomotive, +platform, +rail, +sleeper car, +station (station_place), +switch, +ticket (ticket_admission), +track, +tunnel, +whistle

### TRAVEL  `travel`
- правило: What belongs to the group «Travel» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 13
- +air, +cruise, +destination, +ground, +hostel, +journey, +path, +resort, +route, +safari, +space, +trip, +water

### TRAVEL ACTIVITIES  `travel_activities`
- правило: What belongs to the group «Travel Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +camping, +hiking, +traveling, +trekking

### TRAVEL THINGS  `travel_documents`
- правило: Things a traveler packs or carries on a trip
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- +adapter, +backpack, +boarding pass, +camera, +Charger, +currency, +guidebook, +insurance, +itinerary, +map, +neck pillow, +passport, +suitcase, +sunglasses, +ticket (ticket_admission), +toiletries, +Visa, +wallet

### TRAVEL GEAR  `travel_gear`
- правило: What belongs to the group «Travel Gear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +camera, +map, +passport, +suitcase

### TRAVEL HACKS  `travel_hacks`
- правило: What belongs to the group «Travel Hacks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +pack cubes, +portable charger, +roll clothes, +wear layers

### TRAVEL TERMINOLOGY  `travel_terminology`
- правило: What belongs to the group «Travel Terminology» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +journey, +transit, +trips, +voyage

### TRAVELER S SET  `traveler_s_set`
- правило: What belongs to the group «Traveler S Set» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +baggage, +currency, +money, +passport

### TRAVELING ABROAD  `traveling_abroad`
- правило: What belongs to the group «Traveling Abroad» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +language, +passport, +souvenir, +suitcase

### TYPES OF AIRPLANES  `types_of_airplanes`
- правило: What belongs to the group «Types Of Airplanes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +cargo, +fighter, +glider, +seaplane

### TYPES OF BOATS  `types_of_boats`
- правило: What belongs to the group «Types Of Boats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 8
- +barge, +dingy, +kayak, +row, +schooner, +ship, +vessel, +yacht

### VEHICLE  `vehicle`
- правило: What belongs to the group «Vehicle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 11
- +coupe, +driver, +minivan, +seat, +sedan, +suv, +truck, +van, +wagon, +wheels, +windows

### VEHICLES  `vehicles`
- правило: Machines built to carry people or goods from place to place
- тип связи: `is_a`, базовая сложность 0.1
- слов: 43
- ~plane (plane_aircraft), +aircraft, +ambulance, +bicycle, +bike, +boat, +bus, +canoe, +car, +convertible, +ferry, +hatchback, +helicopter, +Jeep, +limousine, +minivan, +moped, +motorbike, +motorcycle, +scooter, +sedan, +sled, +Subway, +suv, +taxi, +tractor, +train, +tram, +trolley, +truck, +trucks, +van, +wagon, ?bus, ?car, ?Jeep, ?motorcycle, ?scooter, ?Subway, ?tractor, ?truck, ?van, ?wagon

### VINTAGE CAR MODELS  `vintage_car_models`
- правило: What belongs to the group «Vintage Car Models» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 8
- +Camaro, +Corvette, +impala, +nash, +thunderbird, +tucker, !edsel, !studebaker

### VINTAGE CARS  `vintage_cars`
- правило: What belongs to the group «Vintage Cars» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +delorean, +impala, +Mustang, +vw beetle

### WAYS TO TRAVEL  `ways_to_travel`
- правило: What belongs to the group «Ways To Travel» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +bicycle, +car, +motorcycle, +scooter


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
- слов: 16
- ~elderberry, +blackberry, +blueberry, +cranberry, +currant, +gooseberry, +raspberry, +strawberry, ?blackberry, ?blueberry, ?raspberry, ?strawberry, !boysenberry, !cloudberry, !loganberry, xmarionberry

### SPICE BLENDS  `chili_and_spice_blends`
- правило: Mixtures of spices sold as one seasoning
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +cajun, +chili powder, +curry powder, +five spice, +italian seasoning, +jerk, +old bay, +poultry seasoning, +pumpkin spice, +ranch mix, +taco seasoning, !garam masala, !herbes de provence, !za'atar

### GRAPE VARIETIES  `grape_varieties`
- правило: Varieties of grape used for wine and eating
- тип связи: `is_a`, базовая сложность 0.4
- слов: 17
- ~Syrah, +Cabernet, +Chardonnay, +Concord, +Merlot, +Muscat, +Pinot Noir, +Riesling, +Sauvignon, +sauvignon blanc, +Thompson, ?Merlot, ?Pinot Noir, ?Syrah, !Malbec, !Sangiovese, !Zinfandel

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
- слов: 23
- ~cortado, ~drip (drip_coffee), ~frappe, ~macchiato, +americano, +cappuccino, +cold brew, +espresso, +flat white, +french press, +iced coffee, +latte, +mocha, ?affogato, ?americano, ?cappuccino, ?cortado, ?espresso, ?flat white, ?latte, ?macchiato, ?mocha, xaffogato

### CURED MEATS  `cured_meats`
- правило: Meats preserved by curing or smoking
- тип связи: `is_a`, базовая сложность 0.4
- слов: 18
- ~coppa, ~pancetta, +bacon, +bologna, +chorizo, +corned beef, +ham, +jerky, +pastrami, +pepperoni, +prosciutto, +salami, +sausage, ?mortadella, ?prosciutto, !mortadella, xbresaola, xcapicola

### PICKLED FOODS  `fermented_foods`
- правило: Foods preserved by pickling or fermenting
- тип связи: `is_a`, базовая сложность 0.4
- слов: 21
- ~bread, ~cheese, ~kimchi, ~kombucha, ~miso, ~olive, ~pickle, ~relish, ~salami, ~sauerkraut, ~sourdough, ~vinegar, ~wine, ~yogurt, ?kefir, ?kimchi, ?kombucha, ?miso, ?sauerkraut, !kefir, !tempeh

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
- слов: 36
- ~aioli, ~bechamel, ~chimichurri, ~garlic aioli, ~remoulade, ~szechuan, +alfredo, +barbecue, +curry, +glaze, +gravy, +hollandaise, +honey mustard, +ketchup, +marinade, +marinara, +mayonnaise, +mustard, +pesto, +ranch, +relish, +roux, +salsa, +soy, +tartar, +teriyaki, +thousand island, +vinaigrette, ?chimichurri, ?gravy, ?hollandaise, ?pesto, ?ranch, ?roux, ?soy, ?teriyaki

### SOUPS AND STEWS  `soups`
- правило: Kinds of soup and stew
- тип связи: `is_a`, базовая сложность 0.25
- слов: 33
- ~bisque, ~borscht, ~consomme, ~gazpacho, ~goulash, ~minestrone, +bouillon, +broth, +chicken noodle, +chili (chili_dish), +chowder, +gumbo, +lentil, +miso, +onion soup, +pea, +pho, +ramen, +shark fin, +split pea, +stew, +tomato, ?bisque, ?borscht, ?chicken noodle, ?chowder, ?gazpacho, ?gumbo, ?minestrone, ?miso, ?pho, ?ramen, ?tomato

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
- слов: 23
- ~arepa, ~churro, ~churros, +burger, +corn dog, +cotton candy, +crepe, +dumpling, +falafel, +fries, +gyro, +hot dog, +kebab, +popcorn, +pretzel, +roasted nuts, +taco, +waffle, ?cotton candy, ?crepe, ?kebab, ?taco, !elote

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

