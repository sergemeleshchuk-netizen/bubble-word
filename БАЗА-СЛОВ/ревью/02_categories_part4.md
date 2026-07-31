# Категории, часть 4 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

### BOARD GAMES  `board_games`
- правило: Games played on a printed board with pieces
- тип связи: `is_a`, базовая сложность 0.25
- слов: 17
- ~mancala, +backgammon, +battleship, +candy land, +checkers, +chess, +chutes and ladders, +clue, +Life, +monopoly, +othello, +risk, +scrabble, +sorry, +trivial pursuit, +trouble, xparcheesi

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

### CIRCUS WORDS  `circus_words`
- правило: People, animals and objects you see at a traditional circus
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~sword swallower, +acrobat, +cannon, +clown, +cotton candy, +elephant, +juggler, +lion tamer, +net, +popcorn, +ring (ring_arena), +ringmaster, +sequin, +stilts, +tent, +tightrope, +trapeze, +unicycle

### COMEDY WORDS  `comedy_words`
- правило: Words used about comedy performances
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +gag, +heckler, +improv, +joke, +one liner, +parody, +pun, +punchline, +roast, +routine, +satire, +sketch, +slapstick, +standup, +timing

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
- слов: 25
- ~keyboard (keyboard_music), +accordion, +bagpipes, +banjo, +bassoon, +cello, +clarinet, +cymbal, +drum, +flute, +guitar, +harmonica, +harp, +mandolin, +oboe, +organ (organ_music), +piano, +saxophone, +tambourine, +trombone, +trumpet, +tuba, +ukulele, +violin, +xylophone

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

### TOYS  `toys`
- правило: Things children play with
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~kite (kite_toy), ~marble (marble_toy), ~rattle (rattle_toy), ~top (top_spin), +action figure, +ball (ball_sphere), +blocks, +bubble, +crayon, +doll, +frisbee, +jack in the box, +jump rope, +puzzle, +robot, +Slinky, +teddy bear, +train set, +tricycle, +yo-yo

### TELEVISION WORDS  `tv_words`
- правило: Words used about television programs
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +broadcast, +cable, +channel, +commercial, +episode, +finale, +network, +pilot, +ratings, +remote (remote_device), +rerun, +screen (screen_display), +sitcom, +spinoff, +streaming, +subtitle, !host (host_presenter), !season (season_time)

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


## Тема: history

### ANCIENT CIVILIZATIONS  `ancient_civilizations`
- правило: Civilizations of the ancient world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- ~Phoenicia, ~Sumer, +Assyria, +Aztec, +Babylon, +Carthage, +China, +Egypt, +Greece, +Inca, +Maya, +Persia, +Rome, +Sparta, +Troy

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
- слов: 16
- ~breastplate, ~chainmail, +armor, +banner, +crest, +dagger, +gauntlet, +helmet, +horse, +lance, +saddle, +shield, +spur, +squire, +sword, +visor

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
- слов: 25
- +aunt, +brother, +child, +cousin, +daughter, +father, +godmother, +grandchild, +grandfather, +grandmother, +husband, +in law, +mother, +nephew, +niece, +parent, +sibling, +sister, +son, +spouse, +stepfather, +stepmother, +twin, +uncle, +wife

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
- слов: 25
- +Abigail, +Amelia, +Ava, +Charlotte, +Chloe, +Elizabeth, +Ella, +Emily, +Emma, +Grace, +Hannah, +Isabella, +Jennifer, +Lily, +Linda, +Madison, +Mary, +Mia, +Natalie, +Olivia, +Rachel, +Sarah, +Sophia, +Susan, +Zoe

### GROUPS OF PEOPLE  `groups_of_people`
- правило: Words for gatherings of people
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +audience, +band (band_group), +cast (cast_people), +choir, +class, +committee, +congregation, +council, +crew, +crowd, +gang, +jury, +mob, +panel, +squad, +staff, +team, +tribe, +troop, !party (party_group)

### INVENTORS  `inventors`
- правило: Famous inventors
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~ford (ford_person), +bell, +diesel, +Edison, +Franklin, +Goodyear, +Gutenberg, +Marconi, +Morse, +Tesla, +Watt, +Whitney, +Wright, !Daguerre

### STAGES OF LIFE  `life_stages`
- правило: Words for the stages of a human life
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~preschooler, +adolescent, +adult, +baby, +child, +elder (elder_person), +grownup, +infant, +middle age, +newborn, +retiree, +senior, +teenager, +toddler, +youth

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


## Тема: technology

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
- слов: 11
- +April, +August, +December, +February, +January, +July, +June, +march (march_month), +November, +October, +September

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


## Тема: world_more

### MORE COUNTRIES  `countries_more`
- правило: Countries less often named in lists
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- +Albania, +Andorra, +Armenia, +Belarus, +Bhutan, +Cyprus, +Georgia, +Iceland, +Kazakhstan, +Latvia, +Lithuania, +Luxembourg, +Malta, +Moldova, +Monaco, +Mongolia, +Nepal, +Slovenia, +Ukraine, +Uzbekistan

### ISLAND NATIONS  `island_nations`
- правило: Countries made up of islands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Bahrain, +Cuba, +Cyprus, +Fiji, +Iceland, +Indonesia, +Jamaica, +Japan, +Madagascar, +Maldives, +Malta, +Mauritius, +Philippines, +Seychelles, +Sri Lanka

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

