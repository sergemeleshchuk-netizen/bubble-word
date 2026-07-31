# Категории, часть 1 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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


## Тема: language

### RADIO ALPHABET  `alphabet_code`
- правило: Code words used to spell letters over a radio
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~alpha, ~Bravo, ~Charlie, ~delta (delta_letter), ~Echo, ~Golf, ~Hotel, ~India, ~Juliet, ~Kilo, ~Lima, ~Mike, ~November, ~Oscar, ~Papa, ~Quebec, ~Romeo, ~Sierra, ~tango, ~Victor, ~Whiskey, ~Yankee, ~Zulu, !foxtrot

### GREETINGS  `greetings_and_farewells`
- правило: Words and phrases used to greet or say goodbye
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- +aloha, +bye, +cheers (cheers_greeting), +evening, +farewell, +goodbye, +greetings, +hello, +hi, +howdy, +later, +morning, +salute, +so long, +welcome

### LANGUAGES  `languages`
- правило: Languages spoken around the world
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~polish (polish_language), +Arabic, +Chinese, +Dutch, +English, +French, +German, +greek, +Hebrew, +Hindi, +Italian, +Japanese, +Korean, +Latin, +Portuguese, +Russian, +spanish, +Swedish, +Turkish, +Vietnamese

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

### FLOWER PARTS  `flower_parts`
- правило: Parts of a flowering plant
- тип связи: `part_of`, базовая сложность 0.35
- слов: 15
- ~pistil, ~sepal, +blossom, +bud, +bulb, +leaf, +nectar, +petal, +pollen, +root, +seed, +stalk, +stamen, +stem, +thorn

### FLOWERS  `flowers`
- правило: Kinds of flowers commonly sold or grown in gardens
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~begonia, ~petunia, ~zinnia, +azalea, +buttercup, +carnation, +daffodil, +dahlia, +Daisy, +geranium, +hyacinth, +iris, +Jasmine, +lavender (lavender_plant), +lilac, +Lily, +magnolia, +marigold, +orchid, +peony, +poppy, +rose, +sunflower, +tulip, +Violet

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
- слов: 20
- ~sandcastle, +boardwalk, +cooler, +crab, +driftwood, +dune, +gull, +jellyfish, +pebble, +sand, +seaweed, +shell, +starfish, +sunscreen, +surfboard, +tide, +towel, +umbrella, +wave (wave_water), !kite (kite_toy)

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

### UNDERGROUND THINGS  `underground_things`
- правило: Things found under the surface of the ground
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~ant nest, ~aquifer, ~bulb, ~burrow, ~cave, ~coal, ~fossil, ~mole (mole_animal), ~ore, ~pipe (pipe_tube), ~root, ~seed, ~sewer, ~Subway, ~treasure, ~tunnel, ~worm, +mine

### FORMS OF WATER  `water_states`
- правило: Forms water takes in nature
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~dew, ~drizzle, ~fog, ~frost, ~glacier, ~hail, ~humidity, ~icicle, ~mist, ~puddle, ~sleet, ~slush, ~vapor, +cloud, +ice, +rain, +snow, +steam

### WEATHER WORDS  `weather_words`
- правило: Words describing weather conditions or events in the sky
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +blizzard, +breeze, +cloud, +downpour, +drizzle, +flurry, +fog, +frost, +gale, +hail, +heat wave, +humidity, +hurricane, +lightning, +mist, +rain, +shower, +sleet, +snow, +storm, +sunshine, +thaw, +thunder, +tornado, +wind

### WILD PLANTS  `wild_plants`
- правило: Plants that grow wild in fields and woods
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~bracken, ~bramble, ~clover, ~dandelion, ~Fern, ~Ivy, ~lichen, ~moss, ~nettle, ~reed, ~thistle, ~vine, ~weed, !cattail, !goldenrod, !milkweed, !ragweed, !sedge


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

### PLANETS  `planets`
- правило: Planets of our solar system
- тип связи: `is_a`, базовая сложность 0.2
- слов: 9
- +Earth, +Jupiter, +Mars, +mercury (mercury_planet), +Neptune, +Pluto, +Saturn, +Uranus, +Venus

### GEOLOGY WORDS  `rock_cycle_words`
- правило: Words used to describe the earth and its rocks
- тип связи: `found_in`, базовая сложность 0.4
- слов: 16
- ~core, ~crust, ~erosion, ~fault, ~fossil, ~glacier, ~lava, ~magma, ~mantle, ~mineral, ~plate (plate_tectonic), ~quarry, ~sediment, ~strata, ~tectonic, ~volcano

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


## Тема: skills

### CARD TRICKS  `card_tricks`
- правило: Terms used in performing card tricks
- тип связи: `found_in`, базовая сложность 0.5
- слов: 12
- ~control, ~cut, ~double lift, ~false shuffle, ~flourish, ~force, ~pass, ~reveal, ~spread, !palm (palm_hand), !shuffle (shuffle_cards), !sleight

### COCKTAILS  `cocktails`
- правило: Named mixed drinks
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~daiquiri, ~negroni, ~pina colada, +bloody mary, +cosmopolitan, +mai tai, +manhattan, +margarita, +martini, +mimosa, +mojito, +moscow mule, +old fashioned, +sangria, +tom collins, +whiskey sour

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

### YOGA POSES  `yoga_poses`
- правило: Named poses used in yoga
- тип связи: `is_a`, базовая сложность 0.45
- слов: 14
- ~boat, ~child, ~cobra, ~crow, ~downward dog, ~half moon, ~lotus, ~mountain, ~pigeon, ~plank, ~tree, ~triangle, ~warrior, !bridge (bridge_move)


## Тема: species

### BEARS  `bears_and_big_animals`
- правило: Kinds of bear
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- ~spectacled bear, +black bear, +brown bear, +grizzly, +koala, +kodiak, +panda, +polar, +sloth bear, +sun bear

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


## Тема: transport

### AIRCRAFT  `aircraft`
- правило: Machines that fly through the air carrying people or cargo
- тип связи: `is_a`, базовая сложность 0.25
- слов: 15
- ~biplane, +airplane, +airship, +balloon, +blimp, +cargo plane, +drone, +glider, +helicopter, +jet, +rocket, +seaplane, +shuttle, +ultralight, +Zeppelin

### AIRPORT WORDS  `airport_words`
- правило: Words for things, places or roles you encounter at an airport
- тип связи: `found_in`, базовая сложность 0.25
- слов: 25
- ~gate (gate_airport), ~jetway, +aisle, +baggage, +boarding pass, +carousel, +checkpoint, +cockpit, +concourse, +control tower, +customs, +duty free, +hangar, +layover, +luggage, +passport, +pilot, +runway, +seatbelt, +security, +steward, +tarmac, +terminal, +ticket (ticket_admission), +tray table

### BOATS AND SHIPS  `boats`
- правило: Kinds of watercraft
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- ~rowboat, +barge, +canoe, +catamaran, +cruise ship, +dinghy, +ferry, +freighter, +gondola, +houseboat, +kayak, +motorboat, +raft, +sailboat, +schooner, +speedboat, +submarine, +trawler, +tugboat, +yacht

### CAR PARTS  `car_parts`
- правило: Physical parts of an ordinary passenger car
- тип связи: `part_of`, базовая сложность 0.2
- слов: 25
- ~gearshift, ~glovebox, +axle, +battery, +brake, +bumper, +clutch, +dashboard, +door, +engine, +exhaust, +fender, +headlight, +hood (hood_car), +horn (horn_sound), +ignition, +mirror, +muffler, +radiator, +seat, +tire, +trunk (trunk_car), +wheel, +windshield, +wiper

### CONSTRUCTION EQUIPMENT  `construction_equipment`
- правило: Large machines used on a building or road construction site
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~backhoe, ~compactor, ~paver, +bulldozer, +cement mixer, +crane (crane_machine), +digger, +drill rig, +dump truck, +excavator, +forklift, +grader, +hoist, +jackhammer, +loader, +roller, +scaffold, !trencher

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
- слов: 25
- ~plane (plane_aircraft), +ambulance, +bike, +boat, +bus, +canoe, +car, +ferry, +helicopter, +Jeep, +limousine, +minivan, +moped, +motorcycle, +scooter, +sled, +Subway, +taxi, +tractor, +train, +tram, +trolley, +truck, +van, +wagon


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

