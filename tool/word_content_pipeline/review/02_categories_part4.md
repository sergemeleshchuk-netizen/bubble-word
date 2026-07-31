# Категории, часть 4 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

