# Категории, часть 3 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


## Тема: clothing

### ACCESSORIES  `accessories`
- правило: Small items worn or carried to complete an outfit
- тип связи: `is_a`, базовая сложность 0.3
- слов: 36
- ~bowtie, ~tie (tie_clothing), +backpack, +belt, +belts, +bracelet, +brooch, +clutch, +cufflinks, +eyewear, +glasses, +gloves, +handbag, +hat, +hats, +headband, +jewelry, +mittens, +necklace, +purse, +rings, +scarf, +scarves, +sunglasses, +suspenders, +umbrella, +wallet, +watch (watch_object), ?belt, ?brooch, ?hat, ?hats, ?purse, ?scarf, ?sunglasses, xhairbands

### ACTIVEWEAR  `activewear`
- правило: What belongs to the group «Activewear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +leggings, +shorts, +sports bra, +t shirt

### ADDRESS  `address`
- правило: What belongs to the group «Address» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +city, +state, +street, +zip

### BEACH ACCESSORIES  `beach_accessories`
- правило: What belongs to the group «Beach Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +beach bag, +sunglasses, +towel, +umbrella

### CHAT PLATFORM  `chat_platform`
- правило: What belongs to the group «Chat Platform» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +discord, +skype, +slack, +Zoom

### CHATBOT  `chatbot`
- правило: What belongs to the group «Chatbot» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +app, +Converse, +decoder, +intent

### CHATTING  `chatting`
- правило: What belongs to the group «Chatting» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +adieu, +bff, !afaik, !afk

### CLOTHING  `clothing`
- правило: What belongs to the group «Clothing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 19
- +belt, +blazer, +boots, +cardigan, +collar, +cuff, +dress, +gloves, +hat, +hem, +jacket, +pants, +poncho, +scarf, +seam, +shirt, +shorts, +tuxedo, +vest

### CLOTHING ITEMS  `clothing_items`
- правило: Garments worn on the body
- тип связи: `is_a`, базовая сложность 0.1
- слов: 29
- ~tie (tie_clothing), +blazer, +blouse, +boots, +cardigan, +coat (coat_garment), +dress, +glove, +gloves, +hat, +hoodie, +jacket, +jeans, +leggings, +overalls, +pants, +robe, +scarf, +shirt, +shorts, +skirt, +sock, +suit (suit_clothing), +sweater, +sweatshirt, +tank top, +vest, ?hat, ?jacket

### CLOTHING MATERIALS  `clothing_materials`
- правило: What belongs to the group «Clothing Materials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 10
- +cotton, +denim, +fabric, +fur, +lace, +leather, +silk, +synthetic, +velvet, +wool

### GARMENT PARTS  `clothing_parts`
- правило: Parts sewn into a piece of clothing
- тип связи: `part_of`, базовая сложность 0.3
- слов: 17
- ~hood (hood_garment), ~placket, +belt loop, +buckle, +button (button_clothing), +collar, +cuff, +hem, +lapel, +lining, +pocket, +seam, +sleeve, +strap, +waistband, +yoke, +zipper

### CLOTHING PURCHASE  `clothing_purchase`
- правило: What belongs to the group «Clothing Purchase» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +cashier, +clothing tag, +hanger, +try on

### CLOTHING SIZES  `clothing_sizes`
- правило: Words used for clothing sizes and fit
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +large, +loose, +medium, +narrow, +oversized, +petite, +plus, +regular, +slim, +small, +snug, +tall, +tight, +wide

### CLOTHING STORAGE  `clothing_storage`
- правило: What belongs to the group «Clothing Storage» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +dresser, +hanger, +shoe rack, +wardrobe

### CLOTHING STYLES  `clothing_styles`
- правило: What belongs to the group «Clothing Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +casual, +formal, +sporty, +vintage

### DECOR ACCESSORIES  `decor_accessories`
- правило: What belongs to the group «Decor Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +candles, +mirror, +photo frames, +rugs

### DESIGNER CLOTHES  `designer_clothes`
- правило: What belongs to the group «Designer Clothes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +fashion house, +haute couture, +seamstress, +tailored fit

### DRESS CODE  `dress_code`
- правило: What belongs to the group «Dress Code» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +business, +casual, +formal, +uniform

### DRESS CODES  `dress_codes`
- правило: What belongs to the group «Dress Codes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 5
- +black tie, +business, +casual, +cocktail, +formal

### DRESS HEMLINE STYLES  `dress_hemline_styles`
- правило: What belongs to the group «Dress Hemline Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.2
- слов: 4
- +handkerchief, +high low, +mini, +tea length

### DRESS UP  `dress_up`
- правило: What belongs to the group «Dress Up» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 7
- +apparel, +costume, +dinners, +doll up, +dress, +tiara, +wig

### DRESSINGS  `dressings`
- правило: What belongs to the group «Dressings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 5
- +balsamic, +caesar, +honey mustard, +ranch, +vinaigrette

### EAST ASIAN DRESSES  `east_asian_dresses`
- правило: What belongs to the group «East Asian Dresses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ao dai, +kimono, !hanbok, !qipao

### ETHNIC CLOTHING  `ethnic_clothing`
- правило: What belongs to the group «Ethnic Clothing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +kilt, +kimono, +poncho, +sari

### FABRIC  `fabric`
- правило: What belongs to the group «Fabric» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 18
- +burlap, +canvas, +chiffon, +cotton, +denim, +fleece, +lace, +linen, +pattern, +silk, +texture, +thread, +velvet, +weave, +wool, !damask, !organza, !taffeta

### FABRIC CARE  `fabric_care`
- правило: What belongs to the group «Fabric Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 5
- +bleach, +detergent, +fold, +steam, +wash

### FABRIC MATERIALS  `fabric_materials`
- правило: What belongs to the group «Fabric Materials» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +burlap, +denim, +flannel, +tweed

### FABRIC PATTERNS  `fabric_patterns`
- правило: What belongs to the group «Fabric Patterns» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 7
- +chevron, +plaid, +polka, +polka dot, +Stripe, +stripes, !houndstooth

### FABRIC TEXTURES  `fabric_textures`
- правило: What belongs to the group «Fabric Textures» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +corduroy, +satin, +suede, +velvet

### FABRIC WEAVE  `fabric_weave`
- правило: What belongs to the group «Fabric Weave» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +plain, +satin, +twill, !herringbone

### FABRIC WEAVES  `fabric_weaves`
- правило: What belongs to the group «Fabric Weaves» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chevron, +satin, +twill, !herringbone

### FABRICS  `fabrics`
- правило: Materials that clothes are made from
- тип связи: `is_a`, базовая сложность 0.3
- слов: 28
- +canvas, +cashmere, +chiffon, +corduroy, +cotton, +denim, +flannel, +fleece, +lace, +leather, +linen, +nylon, +polyester, +satin, +silk, +spandex, +suede, +tweed, +velvet, +wool, ?corduroy, ?cotton, ?denim, ?linen, ?satin, ?silk, ?velvet, ?wool

### FASHION  `fashion`
- правило: What belongs to the group «Fashion» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +accessories, +clothing, +footwear, +hairstyles

### FASHION DESIGNERS  `fashion_designers`
- правило: What belongs to the group «Fashion Designers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +Armani, +Chanel, +Dior, +Versace

### FASHION ITEMS  `fashion_items`
- правило: What belongs to the group «Fashion Items» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 5
- +gloves, +hat, +heels, +jacket, +scarf

### FASHIONABLE CITIES  `fashionable_cities`
- правило: What belongs to the group «Fashionable Cities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.16
- слов: 4
- +London, +Milan, +new york, +Tokyo

### FOOTWEAR  `footwear`
- правило: Things worn on the feet
- тип связи: `is_a`, базовая сложность 0.15
- слов: 30
- ~wader, +boot (boot_shoe), +boots, +brogue, +cleat, +clog, +flat, +flip-flop, +heel, +heels, +hiking boot, +loafer, +moccasin, +oxford, +pump, +sandal, +sandals, +slip on, +slipper, +sneaker, +sneakers, +sock, +stiletto, +wedge, ?galosh, ?loafer, ?moccasin, ?oxford, ?sandal, ?sneaker

### FORMAL WEAR  `formal_wear`
- правило: Clothing worn to a formal occasion
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~bowtie, ~cummerbund, +cocktail dress, +corsage, +cufflinks, +dress shoes, +evening dress, +gown, +sash, +suit (suit_clothing), +tails, +tuxedo, +veil, +waistcoat

### HAIRDRESSER  `hairdresser`
- правило: What belongs to the group «Hairdresser» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +comb, +scissors, +shampoo, xblowdryer

### HATRED  `hatred`
- правило: What belongs to the group «Hatred» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 5
- +abhor, +despise, +loath, +loathe, +resent

### HATS  `hats`
- правило: Things worn on the head
- тип связи: `is_a`, базовая сложность 0.25
- слов: 32
- ~crown (crown_royal), ~hood (hood_garment), +balaclava, +bandana, +baseball cap, +beanie, +beret, +bonnet, +bowler, +cap, +cowboy hat, +derby, +fedora, +hard hat, +headband, +helmet, +panama, +sombrero, +stetson, +sun hat, +top hat, +turban, +visor, ?baseball cap, ?beanie, ?beret, ?bowler, ?cap, ?fedora, ?helmet, ?sombrero, ?turban

### HEADWEAR  `headwear`
- правило: What belongs to the group «Headwear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +balaclava, +bandana, +beanie, +beret, +cap, +hat, +headband, +helmet

### JEWELRY  `jewelry`
- правило: Decorative items worn on the body as jewelry
- тип связи: `is_a`, базовая сложность 0.2
- слов: 29
- +anklet, +bangle, +bracelet, +brooch, +chain, +charm, +choker, +cufflink, +earring, +earrings, +gemstone, +hoop, +locket, +necklace, +pendant, +ring (ring_jewelry), +stud, +tiara, +watch (watch_object), ?bangle, ?bracelet, ?brooch, ?chain, ?charm, ?earring, ?locket, ?necklace, ?pendant, !pin (pin_fastener)

### JEWELRY BOX  `jewelry_box`
- правило: What is kept in a jewelry box or what it is made of
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~accessories, ~heirloom, +clasp, +gemstones, +jewelry, +metals, +velvet

### JEWELRY CHAIN STYLES  `jewelry_chain_styles`
- правило: What belongs to the group «Jewelry Chain Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +cable, +curb, +figaro, +rope

### JEWELRY COMPONENTS  `jewelry_components`
- правило: What belongs to the group «Jewelry Components» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +chain, +clasp, +pearl, +setting

### JEWELRY MAKING SUPPLIES  `jewelry_making_supplies`
- правило: What belongs to the group «Jewelry Making Supplies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +bezel, +findings, +prong, +wire

### JEWELRY SETTINGS  `jewelry_settings`
- правило: What belongs to the group «Jewelry Settings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bezel, +channel, +prong, !pav

### JEWELRY TYPES  `jewelry_types`
- правило: What belongs to the group «Jewelry Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +bracelet, +earring, +pearl, +pendant

### KIDS CLOTHING  `kids_clothing`
- правило: Clothing made especially for babies and children
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~footie pajamas, ~romper, +bib, +booties, +diaper, +jumper, +mittens, +onesie, +overalls, +smock, +sun hat, !snowsuit

### KNITWEAR  `knitwear`
- правило: What belongs to the group «Knitwear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +beanie, +cardigan, +coats, +pullover

### LAUNDRY CARE  `laundry_care`
- правило: Things done to clothes to keep them clean and neat
- тип связи: `does_action`, базовая сложность 0.35
- слов: 14
- ~press (press_push), +bleach, +dry, +dry clean, +fold, +hang, +iron (iron_appliance), +mend, +rinse, +soak, +sort, +starch, +steam, +wash

### LEGWEAR  `legwear`
- правило: What belongs to the group «Legwear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +hosiery, +jeans, +knee highs, !gaiters

### LUXURY FABRICS  `luxury_fabrics`
- правило: What belongs to the group «Luxury Fabrics» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +angora, +cashmere, +chiffon, +satin, +velvet, !mohair

### MALE ACCESSORIES  `male_accessories`
- правило: What belongs to the group «Male Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +briefcase, +pocket square, +suspenders, +tie clip

### MANHATTAN  `manhattan`
- правило: What belongs to the group «Manhattan» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.12
- слов: 4
- +central park, +skyscraper, +Times Square, +Wall Street

### MANHATTAN PROJECT  `manhattan_project`
- правило: What belongs to the group «Manhattan Project» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +fermi, +los alamos, +trinity test, +uranium

### MATERIALS FOR CLOTHING  `materials_for_clothing`
- правило: What belongs to the group «Materials For Clothing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +canvas, +leather, +rubber, +tweed

### NECKWEAR  `neckwear`
- правило: What belongs to the group «Neckwear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 5
- +ascot, +collar, +necklace, +pendant, +scarf

### PAIRED CLOTHING  `paired_clothing`
- правило: What belongs to the group «Paired Clothing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +gloves, +slippers, +socks, +stockings

### SALAD DRESSING  `salad_dressing`
- правило: What belongs to the group «Salad Dressing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +balsamic, +caesar, +ranch, +vinaigrette

### SEWING WORDS  `sewing_words`
- правило: Words used when sewing or altering clothes
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~baste, ~dart (dart_sew), +alter, +bobbin, +cuff, +hem, +lining, +needle (needle_sewing), +pattern, +pin (pin_fastener), +seam, +stitch, +thimble, +thread, +tuck, !pleat

### SHOE  `shoe`
- правило: What belongs to the group «Shoe» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +heel, +lace, +pair, !eyelet, !outsole, xaglet

### SHOE PARTS  `shoe_parts`
- правило: Parts of a shoe
- тип связи: `part_of`, базовая сложность 0.35
- слов: 20
- ~eyelet, ~insole, +arch (arch_foot), +buckle, +counter, +cushion, +heel, +lace, +shank, +sole (sole_shoe), +strap, +toe, +tongue, +tread, +upper, +welt, ?heel, ?lace, ?tongue, xaglet

### SHOES  `shoes`
- правило: What belongs to the group «Shoes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 11
- +boots, +canvas, +cowboy boots, +heel, +heels, +lace, +loafers, +low heeled, +sandals, +sneakers, xaglet

### SHOPPING FOR CLOTHES  `shopping_for_clothes`
- правило: What belongs to the group «Shopping For Clothes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +clothes rack, +fitting room, +hanger, +size chart

### SLEEPWEAR  `sleepwear`
- правило: Clothing worn to bed
- тип связи: `is_a`, базовая сложность 0.25
- слов: 10
- ~nightcap, ~nightshirt, +boxers, +lounge pants, +nightgown, +onesie, +pajamas, +robe, +sleep mask, +slippers

### SUMMER ACCESSORIES  `summer_accessories`
- правило: What belongs to the group «Summer Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +beach ball, +sandals, +sun hat, +sunglasses

### SUMMER SHOES  `summer_shoes`
- правило: What belongs to the group «Summer Shoes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +clogs, +pumps, +sandals, +slip ons

### SUNDRESS  `sundress`
- правило: What belongs to the group «Sundress» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +belted, +frilly, !backless, !hemline

### SWIMWEAR  `swimwear`
- правило: Clothing worn for swimming
- тип связи: `is_a`, базовая сложность 0.25
- слов: 11
- +bikini, +board shorts, +cover up, +flippers, +goggles, +one piece, +rash guard, +swim cap, +swimsuit, +trunks, +wetsuit

### THINGS THAT ARE HOT  `things_that_are_hot`
- правило: What belongs to the group «Things That Are Hot» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +furnace, +jalapeno, +sauna, +streak

### THINGS THAT BLOOM  `things_that_bloom`
- правило: What belongs to the group «Things That Bloom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +cactus, +cherry, +flower, +tulip

### THINGS THAT BUBBLE  `things_that_bubble`
- правило: What belongs to the group «Things That Bubble» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +cauldron, +champagne, +hot spring, +lava

### THINGS THAT CAN BE LOOSE  `things_that_can_be_loose`
- правило: What belongs to the group «Things That Can Be Loose» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +cannon, +change, +end, +thread

### THINGS THAT CAN BE PAINTED  `things_that_can_be_painted`
- правило: What belongs to the group «Things That Can Be Painted» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +canvas, +fence, +nails, +town

### THINGS THAT CAN BE RAISED  `things_that_can_be_raised`
- правило: What belongs to the group «Things That Can Be Raised» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +barn, +curtain, +salary, +stakes

### THINGS THAT CHAR  `things_that_char`
- правило: What belongs to the group «Things That Char» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +bone, +meat, +paper, +wood

### THINGS THAT ECHO  `things_that_echo`
- правило: What belongs to the group «Things That Echo» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +canyon, +cave, +stadium, +tunnel

### THINGS THAT FLY  `things_that_fly`
- правило: What belongs to the group «Things That Fly» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 6
- +bird, +butterfly, +firefly, +glider, +moth, +rocket

### THINGS THAT GLOW  `things_that_glow`
- правило: What belongs to the group «Things That Glow» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 6
- +bulb, +candle, +firefly, +fireworks, +jellyfish, +lamp

### THINGS THAT POP  `things_that_pop`
- правило: What belongs to the group «Things That Pop» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 8
- +balloon, +bubble, +bubblegum, +champagne, +corn, +firecracker, +pimple, +popcorn

### THINGS THAT RISE  `things_that_rise`
- правило: What belongs to the group «Things That Rise» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +balloon, +breads, +smoke, +sun

### THINGS THAT SET  `things_that_set`
- правило: What belongs to the group «Things That Set» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +bone, +cement, +jelly, +sun

### THINGS THAT SHINE  `things_that_shine`
- правило: What belongs to the group «Things That Shine» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +chrome, +glitter, +mica, +sequin

### THINGS THAT TICK  `things_that_tick`
- правило: What belongs to the group «Things That Tick» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 3
- +alarm clock, +kitchen timer, +metronome

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

### THINGS YOU WEAR  `things_you_wear`
- правило: What belongs to the group «Things You Wear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +boots, +gloves, +hat, +scarf

### TYPES OF FABRIC  `types_of_fabric`
- правило: What belongs to the group «Types Of Fabric» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +denim, +silk, +tweed, +velvet

### TYPES OF HATS  `types_of_hats`
- правило: What belongs to the group «Types Of Hats» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +beret, +bowler, +fedora, +stetson

### TYPES OF SHOES  `types_of_shoes`
- правило: What belongs to the group «Types Of Shoes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 8
- +boots, +clog, +heels, +pump, +sandals, +slide, +sneakers, +wedge

### UNDERWEAR  `underwear`
- правило: What belongs to the group «Underwear» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +boxers, +briefs, !brassiere, !undershirt

### VICTORIAN DRESS ELEMENTS  `victorian_dress_elements`
- правило: What belongs to the group «Victorian Dress Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +dress, +petticoat, !camisole, !crinoline

### VINTAGE DRESS  `vintage_dress`
- правило: What belongs to the group «Vintage Dress» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +corset, +hem, +puffs, !crinoline

### VINTAGE FASHION  `vintage_fashion`
- правило: What belongs to the group «Vintage Fashion» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +a line, +mod, +poodle skirt, +swing dress

### WARDROBE  `wardrobe`
- правило: What hangs, sits or is stored in the place you keep clothes
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 15
- ~closet, ~drawer, ~dresser, ~garment cover, ~hanger, ~mothball, ~pantry, ~skirt, +accessories, +footwear, +hats, +shoes, +sleepwear, ?hanger, !knobs

### WINTER ACCESSORIES  `winter_accessories`
- правило: What belongs to the group «Winter Accessories» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +beanie, +gloves, +scarf, !ear muffs

### WINTER CLOTHING  `winter_clothing`
- правило: Clothing worn specifically to stay warm in cold weather
- тип связи: `used_in`, базовая сложность 0.2
- слов: 25
- ~ear muffs, ~hood (hood_garment), ~thermals, +beanie, +boot (boot_shoe), +boots, +coat (coat_garment), +down jacket, +fleece, +glove, +gloves, +mitten, +mittens, +muffler, +parka, +scarf, +shawl, +ski mask, +snow pants, +sweater, +thermal, +wool socks, ?beanie, ?parka, ?scarf

### WOMENS FASHION  `womens_fashion`
- правило: What belongs to the group «Womens Fashion» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +clutch, +earrings, +headband, +stilettos

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
- слов: 30
- ~omicron, ~upsilon, +alpha, +beta, +chi, +delta (delta_letter), +epsilon, +eta, +gamma, +iota, +kappa, +lambda, +mu, +nu, +Omega, +phi, +pi, +psi, +rho, +sigma, +tau, +theta, +xi, +zeta, ?alpha, ?beta, ?chi, ?gamma, ?iota, ?sigma

### LATIN PHRASES  `latin_phrases`
- правило: Latin phrases used in everyday English
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- ~ad hoc, ~agenda, ~alibi, ~alma mater, ~alter ego, ~bona fide, ~et cetera, ~magnum opus, ~per capita, ~per se, ~quid pro quo, ~status quo, ~versus, ~vice versa, !carpe diem

### MANNERS WORDS  `manners`
- правило: Words used when teaching good manners
- тип связи: `is_a`, базовая сложность 0.35
- слов: 22
- +apologize, +bearing, +behavior, +chewing, +civility, +conduct, +excuse me, +greeting, +listening, +may I, +patience, +please, +respect, +sharing, +sorry, +thank you, +turn taking, +waiting, ?excuse me, ?please, ?sorry, ?thank you

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
- слов: 18
- ~carbon (carbon_paper), ~cardstock, +bond, +construction, +graph, +index card, +loose leaf, +newsprint, +notebook, +parchment, +printer, +sticky note, +tissue (tissue_paper), +tracing, +vellum, +wax (wax_substance), ?newsprint, ?parchment

### READING WORDS  `reading_words`
- правило: Words used when reading and studying text
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- +appendix, +bibliography, +chapter, +excerpt, +footnote, +glossary, +index, +page, +paragraph, +passage, +preface, +quote, +summary, +table of contents, +title

### SCHOOL EVENTS  `school_events`
- правило: Events that happen during a school year
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- +assembly, +book fair, +dance, +detention, +exam, +field trip, +graduation, +homecoming, +open house, +orientation, +pep rally, +picture day, +prom, +recess, +science fair, +spelling bee, +talent show, ?assembly, ?field trip, ?graduation

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
- слов: 40
- ~band (band_group), +algebra, +art, +art classes, +astronomy, +biology, +calculus, +chemistry, +civics, +computer science, +debate, +drama, +economics, +English, +geography, +geometry, +gym, +health, +history, +home economics, +literature, +math, +maths, +music, +photography, +physics, +science, +shop, +social studies, +spanish, +trigonometry, ?algebra, ?art, ?biology, ?chemistry, ?English, ?geometry, ?history, ?math, ?science

### SCHOOL SUPPLIES  `school_supplies`
- правило: Items a student brings to school in a backpack
- тип связи: `used_in`, базовая сложность 0.15
- слов: 31
- +backpack, +binder, +book, +calculator, +compass, +crayon, +eraser, +folder, +glue, +highlighter, +index card, +lunchbox, +marker, +notebook, +paper, +pen (pen_writing), +pencil, +pencil case, +planner, +protractor, +ruler, +scissors, +sharpener, +stapler, +tape, +textbook, ?eraser, ?marker, ?notebook, ?pencil, ?ruler

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


## Тема: food

### ARTISAN BREADS  `artisan_breads`
- правило: What belongs to the group «Artisan Breads» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +baguette, +brioche, +rye, +sourdough

### ASIAN DISHES  `asian_dishes`
- правило: Dishes from East and Southeast Asian cuisines eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bibimbap, ~satay, ~tempura, ~wonton, +chow mein, +curry, +dim sum, +dumpling, +egg roll, +fried rice, +kimchi, +lo mein, +miso soup, +pad thai, +pho, +ramen, +sashimi, +spring roll, +sushi, +teriyaki

### BAKE  `bake`
- правило: What belongs to the group «Bake» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 4
- +crust, +flour, +oven, +rise

### BAKEDGOODS  `bakedgoods`
- правило: What belongs to the group «Bakedgoods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +bread, +cakes, +cookies, +pastries

### BAKEHOUSE  `bakehouse`
- правило: What belongs to the group «Bakehouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +flour, +knead, +oven, +yeast

### BAKERY  `bakery`
- правило: What belongs to the group «Bakery» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 20
- +bagel, +baker, +bread, +cake, +chef, +cinnamon, +coffee, +croissant, +dough, +eggs, +flour, +milk, +mixer, +muffin, +oven, +pastry, +pretzel, +rolling pin, +sourdough, +yeast

### BAKERY CASE  `bakery_case`
- правило: What belongs to the group «Bakery Case» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +bagel, +croissant, +muffin, +pretzel

### BAKERY ITEMS  `bakery_items`
- правило: What belongs to the group «Bakery Items» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 6
- +bagel, +bread, +croissant, +muffin, +pretzel, +scone

### BAKESHOP  `bakeshop`
- правило: What belongs to the group «Bakeshop» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +baguette, +bread loaf, +brownie, +bun

### BAKEWARE  `bakeware`
- правило: What belongs to the group «Bakeware» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +baking tray, +bowls, +bread pan, !bundt pan

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
- слов: 18
- ~boysenberry, ~elderberry, +blackberry, +blueberry, +cherry, +cranberry, +currant, +gooseberry, +grape, +huckleberry, +mulberry, +raspberry, +strawberry, ?blueberry, ?cherry, ?cranberry, ?raspberry, ?strawberry

### BOTTLED DRINKS  `bottled_drinks`
- правило: What belongs to the group «Bottled Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- ~kefir, +juice, +soft drink, +water

### BREAD  `bread`
- правило: What belongs to the group «Bread» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 19
- +bagel, +baguette, +baker, +brioche, +crust, +dough, +flour, +knead, +loaf, +pita, +rise, +rye, +salt, +sourdough, +water, +yeast, !ciabatta, !focaccia, !pumpernickel

### BREAD INGREDIENTS  `bread_ingredients`
- правило: What belongs to the group «Bread Ingredients» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +baking powder, +buttermilk, +corn flour, +eggs

### BREAD RELATED  `bread_related`
- правило: What belongs to the group «Bread Related» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +baguette, +bakery, +crumbs, +gluten

### BREAD TYPES  `bread_types`
- правило: Kinds of bread and baked goods made from dough
- тип связи: `is_a`, базовая сложность 0.25
- слов: 34
- ~challah, ~ciabatta, ~flatbread, ~focaccia, ~pumpernickel, ~white (white_food), +bagel, +baguette, +banana bread, +biscuit, +brioche, +bun, +cornbread, +croissant, +muffin, +naan, +pita, +pretzel, +roll (roll_bread), +rye, +scone, +sourdough, +texas toast, +tortilla, +wheat, ?baguette, ?brioche, ?challah, ?ciabatta, ?cornbread, ?flatbread, ?pumpernickel, ?rye, ?sourdough

### BREAKFAST DISHES  `breakfast_dishes`
- правило: What belongs to the group «Breakfast Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +bagel, +omelet, +pancake, +waffle

### BREAKFAST DRINKS  `breakfast_drinks`
- правило: What belongs to the group «Breakfast Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +coffee, +juice, +milk, +tea

### BREAKFAST FOODS  `breakfast_foods`
- правило: Foods typically eaten at breakfast in the United States
- тип связи: `is_a`, базовая сложность 0.2
- слов: 38
- +bacon, +bagel, +biscuit, +cereal, +coffee cake, +croissant, +danish, +doughnut, +egg, +eggs, +french toast, +granola, +grits, +ham, +hash brown, +honey, +jam, +juice, +muffin, +oatmeal, +omelet, +pancake, +pancakes, +pop tart, +porridge, +sausage, +scone, +toast (toast_bread), +waffle, +yogurt, ?bacon, ?cereal, ?egg, ?muffin, ?oatmeal, ?omelet, ?pancake, ?yogurt

### BULB VEGETABLES  `bulb_vegetables`
- правило: What belongs to the group «Bulb Vegetables» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- ~shallot, +fennel, +garlic, +onion

### CAKE TYPES  `cake_types`
- правило: Kinds of cake baked and sold in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bundt, ~fruitcake, ~pound (pound_cake), ~sponge (sponge_cake), +angel food, +birthday, +carrot, +cheesecake, +chocolate, +coffee cake, +cupcake, +ice cream cake, +lava, +layer, +red velvet, +shortcake, +upside down, +vanilla, +wedding, !marble (marble_cake)

### CAN BE COOKED  `can_be_cooked`
- правило: What belongs to the group «Can Be Cooked» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +meat, +pasta, +rice, +vegetables

### CANDY  `candy`
- правило: Sweets sold in a candy aisle
- тип связи: `is_a`, базовая сложность 0.2
- слов: 37
- ~brittle (brittle_candy), ~gum (gum_candy), ~gumdrop, ~Reeses, ~Twix, +butterscotch, +candy cane, +caramel, +chocolate, +chocolate bar, +fudge, +gummy, +jelly bean, +Jolly Rancher, +kit kat, +licorice, +lollipop, +m ms, +marshmallow, +mint (mint_candy), +nougat, +praline, +rock candy, +Skittles, +Snickers, +sour patch kids, +Starburst, +swedish fish, +sweet, +taffy, +toffee, +truffle, +wrapper, ?chocolate, ?lollipop, ?nougat, ?taffy

### CANDY BAR  `candy_bar`
- правило: What belongs to the group «Candy Bar» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Kitkat, +Snickers, !Butterfinger, !Twix

### CANDY FILLINGS  `candy_fillings`
- правило: What belongs to the group «Candy Fillings» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +caramel, +praline, !ganache, !marzipan

### CANDY PIECES  `candy_pieces`
- правило: What belongs to the group «Candy Pieces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +dot, +kiss, +whopper, !goober

### CANDY PROFILES  `candy_profiles`
- правило: What belongs to the group «Candy Profiles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +chewy, +gummy, +sticky, +sugary

### CANNED FOOD  `canned_food`
- правило: What belongs to the group «Canned Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +beans, +soup, +sweet corn, +tuna

### CARNIVAL FOODS  `carnival_foods`
- правило: What belongs to the group «Carnival Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +corn dog, +funnel cake, +pretzel, !churro

### CHEESE  `cheese`
- правило: What belongs to the group «Cheese» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 18
- +aged, +American, +brie, +cheddar, +colby, +cottage, +dor blu, +feta, +gouda, +mozzarella, +ricotta, !asiago, !burrata, !edam, !gruyere, !manchego, !pecorino, xneufchatel

### CHEESE TYPES  `cheese_types`
- правило: Kinds of cheese sold in American grocery stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~camembert, ~gruyere, ~muenster, ~provolone, +American, +blue cheese, +brie, +cheddar, +colby, +cottage cheese, +cream cheese, +feta, +goat cheese, +gouda, +monterey jack, +mozzarella, +parmesan, +ricotta, +swiss, !havarti

### CHEESE VARIETIES  `cheese_varieties`
- правило: What belongs to the group «Cheese Varieties» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +brie, +cheddar, +feta, +gouda, !camembert, !manchego

### CHINESE FOOD  `chinese_food`
- правило: What belongs to the group «Chinese Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +fortune cookie, +noodles, +rice, +takeout

### CITRUS FRUITS  `citrus_fruits`
- правило: Fruits of the citrus family with a thick peel and juicy segments
- тип связи: `is_a`, базовая сложность 0.25
- слов: 21
- ~citron, ~kaffir lime, ~kumquat, ~pomelo, ~yuzu, +clementine, +grapefruit, +lemon, +lime, +mandarin, +orange (orange_fruit), +tangerine, ?citron, ?clementine, ?grapefruit, ?kumquat, ?lemon, ?lime, ?mandarin, ?pomelo, ?tangerine

### COLD DRINKS  `cold_drinks`
- правило: Drinks normally served cold
- тип связи: `is_a`, базовая сложность 0.2
- слов: 18
- ~horchata, ~kombucha, ~slushie, +coconut water, +cola, +ginger ale, +iced tea, +juice, +lemonade, +milk, +milkshake, +punch (punch_drink), +root beer, +seltzer, +smoothie, +soda, +sports drink, +water

### COLD FOODS  `cold_foods`
- правило: What belongs to the group «Cold Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gelato, +icecream, +Popsicle, +sorbet

### CONDIMENTS  `condiments`
- правило: Things squeezed or spooned onto food at the table
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~aioli, +barbecue sauce, +chutney, +honey, +horseradish, +hot sauce, +jam, +ketchup, +mayo, +mustard, +pesto, +ranch, +relish, +salsa, +sauces, +soy sauce, +sriracha, +syrup, +tartar sauce, +vinegar, +wasabi, ?ketchup, ?mayo, ?mustard, ?relish

### COOK  `cook`
- правило: What belongs to the group «Cook» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 11
- +boil, +chef, +chop, +garde manger, +pan, +pastry chef, +prep cook, +recipe, +sous chef, +stove, !saut

### COOKBOOK  `cookbook`
- правило: What belongs to the group «Cookbook» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +cooking, +cuisine, +index, +recipe

### COOKED STATE  `cooked_state`
- правило: What belongs to the group «Cooked State» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.11
- слов: 4
- +blue, +medium, +rare, +well done

### COOKIE ADD INS  `cookie_add_ins`
- правило: What belongs to the group «Cookie Add Ins» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 5
- +berry, +caramel, +chocolates, +nuts, +raisin

### COOKIE FLAVORS  `cookie_flavors`
- правило: What belongs to the group «Cookie Flavors» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +chocolate chip, +gingerbread, +oatmeal, !snickerdoodle

### COOKIE TEXTURES  `cookie_textures`
- правило: What belongs to the group «Cookie Textures» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- ~crumbly, +chewy, +crispy, +crunchy

### COOKIE VARIETIES  `cookie_varieties`
- правило: What belongs to the group «Cookie Varieties» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chocolate, +oatmeal, +shortbread, !snickerdoodle

### COOKING  `cooking`
- правило: What belongs to the group «Cooking» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 16
- +bake, +baking, +blanch, +boil, +boiling, +chef, +frying, +grill, +grilling, +pan, +puree, +recipe, +simmer, +stove, !confit, !saute

### COOKING APPLIANCES  `cooking_appliances`
- правило: What belongs to the group «Cooking Appliances» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +fryer, +grill, +oven, +steamer

### COOKING EQUIPMENT  `cooking_equipment`
- правило: What belongs to the group «Cooking Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +gas stove, +grill, +microwave, +oven

### COOKING FATS  `cooking_fats`
- правило: Fats and oils used to cook or dress food
- тип связи: `used_in`, базовая сложность 0.4
- слов: 19
- +avocado oil, +bacon grease, +butter, +canola, +coconut oil, +corn oil, +ghee, +lard, +margarine, +olive oil, +peanut oil, +sesame oil, +shortening, +sunflower oil, +vegetable oil, ?butter, ?ghee, ?lard, ?olive oil

### COOKING INGREDIENTS  `cooking_ingredients`
- правило: What belongs to the group «Cooking Ingredients» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 6
- +flour, +herbs, +spice, +spices, +sugar, +yeast

### COOKING OILS  `cooking_oils`
- правило: What belongs to the group «Cooking Oils» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 8
- +canola, +corn, +olive, +peanut, +sesame, +sunflower, !flaxseed, !grapeseed

### COOKING SHOWS  `cooking_shows`
- правило: What belongs to the group «Cooking Shows» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 5
- +chopped, +culinary terms, +iron chef, +masterchef, +top chef

### COOKING TECHNIQUES  `cooking_techniques`
- правило: What belongs to the group «Cooking Techniques» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 7
- +bake, +blanch, +boil, +grill, +poach, +roast, !saute

### COOKING TERMS  `cooking_terms`
- правило: What belongs to the group «Cooking Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +blanch, +reduce, +simmer, !deglaze

### COOKING TOOLS  `cooking_tools`
- правило: What belongs to the group «Cooking Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +pot, +saucepan, +spatula, +whisk

### COOKING UTENSILS  `cooking_utensils`
- правило: What belongs to the group «Cooking Utensils» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ladle, +spatula, +tongs, +whisk

### COOKING VERBS  `cooking_verbs`
- правило: What belongs to the group «Cooking Verbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +poach, +simmer, !braise, !saut, !saute

### COOKWARE  `cookware`
- правило: What belongs to the group «Cookware» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 9
- ~colander, +brazier, +cake pan, +cauldron, +crock, +potato, +saucepan, +skillet, +wok

### CRUNCHY FOODS  `crunchy_foods`
- правило: What belongs to the group «Crunchy Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +chips, +crackers, +cucumber, +radish

### DAIRY PRODUCTS  `dairy_products`
- правило: Foods made from milk or sold in the dairy section
- тип связи: `is_a`, базовая сложность 0.15
- слов: 26
- +butter, +buttermilk, +cheese, +condensed milk, +cottage cheese, +cream (cream_dairy), +cream cheese, +curd, +custard, +frozen yogurt, +gelato, +ghee, +half and half, +ice cream, +kefir, +milk, +sour cream, +whey, +whipped cream, +yogurt, ?butter, ?cheese, ?ice cream, ?kefir, ?milk, ?yogurt

### DEEP FRIED FOOD  `deep_fried_food`
- правило: What belongs to the group «Deep Fried Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +falafel, !katsu, !samosa, !schnitzel

### DELI FOODS  `deli_foods`
- правило: What belongs to the group «Deli Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +coleslaw, +pastrami, +pickle, +sandwich

### DELIVERED FOODS  `delivered_foods`
- правило: What belongs to the group «Delivered Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +pad thai, +pizza, +sandwich, +wings

### DESSERT  `dessert`
- правило: What belongs to the group «Dessert» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 18
- +brownie, +cake, +candy, +cheesecake, +cookie, +cupcake, +donut, +fruit, +fudge, +gelato, +ice cream, +pastry, +pie, +pudding, +sorbet, +tart, +trifle, !tiramisu

### DESSERT CREAMS  `dessert_creams`
- правило: What belongs to the group «Dessert Creams» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +gelato, +ice cream, +whipped, !froyo

### DESSERT INGREDIENTS  `dessert_ingredients`
- правило: What belongs to the group «Dessert Ingredients» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +butter, +flour, +sugar, +vanilla

### DESSERT TYPES  `dessert_types`
- правило: What belongs to the group «Dessert Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +cake, +pudding, +trifle, !galette

### DESSERTS  `desserts`
- правило: Sweet dishes served at the end of a meal
- тип связи: `is_a`, базовая сложность 0.15
- слов: 43
- +baklava, +berries, +brownie, +cake, +candy, +cheesecake, +cobbler, +cookie, +cupcake, +custard, +donut, +eclair, +flan, +fudge, +gelato, +ice, +ice cream, +macaron, +mousse, +parfait, +pastry, +pie, +Popsicle, +pudding, +sorbet, +souffle, +strudel, +sundae, +tart, +tiramisu, +trifle, ?brownie, ?cake, ?cookie, ?donut, ?eclair, ?ice cream, ?mousse, ?pie, ?pudding, ?souffle, ?tart, ?tiramisu

### DIPPING SAUCES  `dipping_sauces`
- правило: What belongs to the group «Dipping Sauces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ranch, +sriracha, !aioli, !tzatziki

### DISH  `dish`
- правило: What belongs to the group «Dish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 6
- +burger, +kebab, +pizza, +poutine, +salad, +sushi

### DOUGH DISHES  `dough_dishes`
- правило: What belongs to the group «Dough Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +bread, +dumplings, +noodles, +pizza

### DRIED FOODS  `dried_foods`
- правило: What belongs to the group «Dried Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +dates, +jerky, +nori, +raisins

### DRINK  `drink`
- правило: What belongs to the group «Drink» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chug, +gulp, +sip, !guzzle

### DRINK TYPES  `drink_types`
- правило: What belongs to the group «Drink Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +coffee, +juice, +tea, +wine

### DRINKWARE  `drinkware`
- правило: What belongs to the group «Drinkware» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +chalice, +cup, +glass, +goblet, +mug, +thermos, +tumbler, +yeti

### EGG COOKING STYLES  `egg_cooking_styles`
- правило: What belongs to the group «Egg Cooking Styles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +fried, +hard boiled, +poached, !coddled

### EGG DISHES  `egg_dishes`
- правило: Ways eggs are cooked and served
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~deviled, ~frittata, ~souffle, +benedict, +boiled, +custard, +egg salad, +fried, +omelet, +over easy, +poached, +quiche, +scrambled, +sunny side up

### ENERGY DRINKS  `energy_drinks`
- правило: What belongs to the group «Energy Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +celsius, +monster, +red bull, +vault

### EXOTIC FRUITS  `exotic_fruits`
- правило: What belongs to the group «Exotic Fruits» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +durian, !dragonfruit, !lychee, !rambutan

### EXPENSIVE FOODS  `expensive_foods`
- правило: What belongs to the group «Expensive Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +caviar, +saffron, +truffle, !wagyu

### DRIVE THRU  `fast_food_items`
- правило: Items ordered at an American fast food counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 24
- ~quesadilla, +biscuit, +burger, +burrito, +chicken sandwich, +chili (chili_dish), +corn dog, +french fries, +fries, +hot dog, +milkshake, +mozzarella stick, +nugget, +onion ring, +pizza, +shake, +slider, +soda, +sub, +sundae, +taco, +wrap, ?burger, ?soda

### FAST FOOD ORDER  `fast_food_order`
- правило: What belongs to the group «Fast Food Order» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +burger, +drink, +fries, +nuggets

### FAST FOOD RESTAURANT CHAINS  `fast_food_restaurant_chains`
- правило: What belongs to the group «Fast Food Restaurant Chains» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +Burger King, +Subway, !Popeyes, !Wendys

### FERMENTED FOOD  `fermented_food`
- правило: What belongs to the group «Fermented Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +sauerkraut, !kefir, !kombucha, !kvass

### FINGER FOODS  `finger_foods`
- правило: What belongs to the group «Finger Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +chicken wing, +dumpling, +spring roll, !bruschetta

### FIZZY DRINKS  `fizzy_drinks`
- правило: What belongs to the group «Fizzy Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 7
- +cider, +Coke, +ginger ale, +prosecco, +seltzer, +soda pop, +sparkling water

### FOOD  `food`
- правило: What belongs to the group «Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 20
- +berries, +berry, +bread, +burger, +butter, +chicken soup, +desserts, +egg, +fries, +grain, +milk, +omelet, +pizza, +rice, +salad, +snacks, +steak, +vegetables, +yogurt, !panna cotta

### FOOD CONTAINERS  `food_containers`
- правило: What belongs to the group «Food Containers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +bread bin, +butter dish, +cookie tin, +jam pot

### FOOD DELIVERY  `food_delivery`
- правило: What belongs to the group «Food Delivery» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +app, +courier, +driver, +packaging

### FOOD DISHES  `food_dishes`
- правило: What belongs to the group «Food Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 7
- +burger, +burrito, +nachos, +salad, +steak, +taco, !quesadilla

### FOOD ESTABLISHMENTS  `food_establishments`
- правило: What belongs to the group «Food Establishments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +cafe, +deli, +pub, +restaurant

### FOOD MARKET  `food_market`
- правило: What belongs to the group «Food Market» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +bakery, +fish, +meat, +vegetables

### FOOD ON A STICK  `food_on_a_stick`
- правило: What belongs to the group «Food On A Stick» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +corn dog, +lollipop, +sausage, +skewer

### FOOD PRESERVATION  `food_preservation`
- правило: What belongs to the group «Food Preservation» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 8
- +condensed milk, +curing, +jam, +pickled onions, +smoking, +zucchini relish, !brining, !pickling

### FOOD TASTE  `food_taste`
- правило: What belongs to the group «Food Taste» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +salty, +savory, +spicy, +sweet

### FOOD TYPES  `food_types`
- правило: What belongs to the group «Food Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 11
- +baked, +boiled, +dairy, +dessert, +fast food, +fried, +Frozen, +fruits, +grains, +seafood, +vegetables

### FOOD VENUES  `food_venues`
- правило: What belongs to the group «Food Venues» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +bakery, +food truck, +pizzeria, !gastropub

### FOOD WEB  `food_web`
- правило: What belongs to the group «Food Web» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +apex, +consumer, +producer, xdecomposer

### FOODS  `foods`
- правило: What belongs to the group «Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +bagel, +noodle, +pretzel, +wafer

### FOODS WITH SHELLS  `foods_with_shells`
- правило: What belongs to the group «Foods With Shells» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +clam, +lobster, +pistachio, +wrapper

### FORTUNE COOKIE  `fortune_cookie`
- правило: What belongs to the group «Fortune Cookie» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 4
- +prosperity, +success, +travel, +wisdom

### FRENCH CHEESES  `french_cheeses`
- правило: What belongs to the group «French Cheeses» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +brie, !camembert, !gruyere, !roquefort

### FROZEN DESSERTS  `frozen_desserts`
- правило: What belongs to the group «Frozen Desserts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +gelato, +sherbet, +sorbet, !granita

### FROZEN FOODS  `frozen_foods`
- правило: Foods normally bought from the freezer aisle
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~tater tot, +berries, +burrito, +chicken nugget, +corn dog, +dumpling, +fish stick, +french fries, +hash brown, +ice cream, +lasagna, +peas, +pizza, +Popsicle, +pot pie, +sorbet, +spinach, +waffle

### FRUIT  `fruit`
- правило: What belongs to the group «Fruit» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 19
- +apples, +apricot, +cranberries, +fig, +guava, +kiwi, +lemon, +lychee, +mango, +melon, +peach, +pear, +pineapple, +plum, +pomegranate, +quince, !dragonfruit, !mangosteen, !rambutan

### FRUIT COLORS  `fruit_colors`
- правило: What belongs to the group «Fruit Colors» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +amber, +crimson, +gold, +purple

### FRUIT DESSERTS  `fruit_desserts`
- правило: What belongs to the group «Fruit Desserts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +cobbler, +crumble, +turnover, !strudel

### FRUIT SPREADS  `fruit_spreads`
- правило: What belongs to the group «Fruit Spreads» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +jam, +jelly, +marmalade, !compote

### FRUITS  `fruits`
- правило: Common edible fruits familiar to an average American adult
- тип связи: `is_a`, базовая сложность 0.1
- слов: 44
- ~ackee, ~date (date_fruit), ~kumquat, +apple (apple_fruit), +apricot, +banana, +berries, +blackberry, +blueberry, +cantaloupe, +cherry, +cranberry, +fig, +grape, +grapefruit, +kiwi, +lemon, +lime, +lychee, +mango, +mulberry, +nectarine, +orange (orange_fruit), +papaya, +peach, +pear, +persimmon, +pineapple, +plum, +quince, +raspberry, +strawberry, +tamarind, +tangerine, +watermelon, ?apricot, ?banana, ?grape, ?mango, ?nectarine, ?papaya, ?peach, ?pear, ?plum

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

### HIGH PROTEIN FOODS  `high_protein_foods`
- правило: What belongs to the group «High Protein Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 3
- +eggs, +salmon, +whey protein

### HOT DRINKS  `hot_drinks`
- правило: Drinks normally served hot
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +americano, +broth, +cappuccino, +chai, +chamomile, +cider, +cocoa, +coffee, +espresso, +green tea, +herbal tea, +hot chocolate, +latte, +macchiato, +matcha, +mocha, +mulled wine, +tea, +toddy, ?chai, ?cider, ?cocoa, ?coffee, ?latte, ?tea

### HOT FOOD AND DRINKS  `hot_food_and_drinks`
- правило: What belongs to the group «Hot Food And Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +cooking techniques, +mulled wine, +soup, +tea

### HOT SAUCES  `hot_sauces`
- правило: What belongs to the group «Hot Sauces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pepper, +sriracha, +tabasco, !habanero

### ICE CREAM  `ice_cream_flavors`
- правило: Flavors of ice cream sold in American shops
- тип связи: `is_a`, базовая сложность 0.25
- слов: 26
- +banana, +birthday cake, +butter pecan, +caramel, +cherry, +chocolate, +coffee, +cookie, +cookie dough, +cookies and cream, +lemon, +mango, +mint (mint_candy), +moose tracks, +neapolitan, +peach, +pistachio, +rocky road, +sherbet, +strawberry, +vanilla, ?chocolate, ?neapolitan, ?rocky road, ?strawberry, ?vanilla

### ITALIAN DISHES  `italian_dishes`
- правило: Dishes from Italian cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~antipasto, ~bruschetta, ~calzone, ~cannoli, ~carbonara, ~focaccia, ~minestrone, ~parmigiana, ~tiramisu, +alfredo, +gelato, +gnocchi, +lasagna, +meatball, +panini, +pasta, +pesto, +pizza, +ravioli, +risotto, +sauce, +spaghetti, ?cannoli, ?gelato, ?risotto, ?tiramisu

### ITALIAN FOOD  `italian_food`
- правило: What belongs to the group «Italian Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +bolognese, +lasagna, +pasta, +pizza, +risotto, !biscotti, !bruschetta, !burrata

### JAPANESE FOODS  `japanese_foods`
- правило: What belongs to the group «Japanese Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +ramen, +sushi, +teriyaki, !yakitori

### JUICY FOODS  `juicy_foods`
- правило: What belongs to the group «Juicy Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +grapefruit, +pineapple, +strawberry, +watermelon

### KOREAN FOOD  `korean_food`
- правило: What belongs to the group «Korean Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +kimchi, !bibimbap, !bulgogi, xkalbi

### LA PIZZA  `la_pizza`
- правило: What belongs to the group «La Pizza» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +cheese, +crust, +sauce, +slice

### LEAFY GREENS  `leafy_greens`
- правило: Vegetables eaten for their leaves
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- ~arugula, ~bok choy, +cabbage, +chard, +collard, +endive, +kale, +lettuce, +parsley, +romaine, +spinach, +watercress

### LUNCH FOODS  `lunch_foods`
- правило: What belongs to the group «Lunch Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +bowl, +salad, +sandwich, +soup

### MAIN DISH  `main_dish`
- правило: What belongs to the group «Main Dish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +curry, +pasta, +pizza, +steak

### MEAT  `meat`
- правило: What belongs to the group «Meat» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 12
- +bacon, +beef, +chicken, +chorizo, +ham, +lamb, +pork, +poultry, +ribs, +sausage, +venison, +wings

### MEAT CUTS  `meat_cuts`
- правило: What belongs to the group «Meat Cuts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +fillet, +loin, +ribs, +shank

### MEAT DELICACIES  `meat_delicacies`
- правило: What belongs to the group «Meat Delicacies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +foie gras, +roast beef, !carpaccio, !jamon

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

### MISTAKEN FOR VEGETABLES  `mistaken_for_vegetables`
- правило: What belongs to the group «Mistaken For Vegetables» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +avocado, +cucumber, +tomato, +zucchini

### MIXED DRINKS  `mixed_drinks`
- правило: What belongs to the group «Mixed Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +bitters, +garnish, +shaker, +syrup

### MOVIE SNACKS  `movie_snacks`
- правило: What belongs to the group «Movie Snacks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +candy, +nachos, +popcorn, +soda

### MOVIE THEATER SNACKS  `movie_theater_snacks`
- правило: What belongs to the group «Movie Theater Snacks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +candy, +nachos, +popcorn, +soda

### NOODLE DISHES  `noodle_dishes`
- правило: What belongs to the group «Noodle Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pho, +ramen, !soba, !udon

### NUTS AND SEEDS  `nuts_and_seeds`
- правило: Edible nuts and seeds sold as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 14
- ~flaxseed, +almond, +cashew, +chestnut, +hazelnut, +macadamia, +peanut, +pecan, +pine nut, +pistachio, +pumpkin seed, +sesame, +sunflower seed, +walnut

### OLD FASHIONED CANDY  `old_fashioned_candy`
- правило: What belongs to the group «Old Fashioned Candy» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +fudge, +licorice, +taffy, +toffee

### PANTRY STAPLES  `pantry_staples`
- правило: Basic foods kept in a kitchen pantry for a long time
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- ~oil (oil_cooking), +baking soda, +beans, +broth, +canned soup, +cereal, +coffee, +flour, +honey, +ketchup, +oats, +pasta, +peanut butter, +rice, +salt, +spaghetti, +sugar, +tea, +tuna, +vinegar

### PARTS OF FRUIT  `parts_of_fruit`
- правило: What belongs to the group «Parts Of Fruit» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +core, +pulp, +seed, +skin

### PASTA SAUCE  `pasta_sauce`
- правило: What belongs to the group «Pasta Sauce» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +alfredo, +bolognese, +marinara, +pesto, !carbonara

### PASTA SAUCES  `pasta_sauces`
- правило: What belongs to the group «Pasta Sauces» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +alfredo, +bolognese, +marinara, +pesto, !carbonara, !puttanesca

### PASTA SHAPES  `pasta_shapes`
- правило: Shapes of pasta sold in American stores
- тип связи: `is_a`, базовая сложность 0.35
- слов: 30
- ~penne, +angel hair, +elbow, +gnocchi, +lasagna, +macaroni, +ravioli, +shell, +shells, +spaghetti, ?farfalle, ?linguine, ?orzo, ?penne, ?ravioli, ?rigatoni, ?ziti, !cannelloni, !farfalle, !fettuccine, !fettuccini, !fusilli, !linguine, !orzo, !rigatoni, !tortellini, !vermicelli, !ziti, xorecchiette, xrotini

### PICNIC BASKET  `picnic_basket`
- правило: What you pack or bring for a picnic
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 10
- ~blanket, ~chips, ~condiments, ~napkins, +cheese, +desserts, +fruits, +salads, ?thermos, !thermos

### PICNIC FOOD  `picnic_food`
- правило: What belongs to the group «Picnic Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +chips, +lemonade, +sandwich, +watermelon

### PIE INGREDIENTS  `pie_ingredients`
- правило: Ingredients commonly used in pie fillings or pie preparation
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- +apple (apple_fruit), +blueberry, +butter, +cherry, +chocolate, +cinnamon, +coconut, +cornstarch, +cream (cream_dairy), +crust, +custard, +egg, +flour, +lemon, +molasses, +nutmeg, +peach, +pecan, +pumpkin, +raisin, +rhubarb, +salt, +shortening, +sugar, +vanilla

### PIZZA  `pizza`
- правило: What belongs to the group «Pizza» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 18
- +cheese, +crust, +fast food, +hawaiian, +margherita, +marinara, +neapolitan, +pepperoni, +sauce, +sicilian, +slice, +supreme, +thick crust, +tomato base, +topping, +toppings, +veggie, !napoletana

### PIZZA TOPPINGS  `pizza_toppings`
- правило: Ingredients commonly put on top of a pizza
- тип связи: `used_in`, базовая сложность 0.2
- слов: 39
- ~arugula, +anchovies, +anchovy, +artichoke, +bacon, +basil, +broccoli, +cheese, +chicken, +egg, +garlic, +ham, +hot honey, +jalapeno, +meatball, +mushroom, +mushrooms, +olive, +olives, +onion, +onions, +pepper, +pepperoni, +pineapple, +ricotta, +salami, +sausage, +shrimp, +spinach, +tomato, ?anchovy, ?bacon, ?cheese, ?mushroom, ?olive, ?pepperoni, ?pineapple, ?sausage, ?spinach

### POCKET SNACKS  `pocket_snacks`
- правило: What belongs to the group «Pocket Snacks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +beef jerky, +granola bar, +nut mix, +trail mix

### POPULAR DESSERTS  `popular_desserts`
- правило: What belongs to the group «Popular Desserts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +cake, +cotton candy, +ice cream, +pie

### RAW DISH  `raw_dish`
- правило: What belongs to the group «Raw Dish» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +oyster, +poke, +sashimi, !ceviche

### REFRESHING DRINKS  `refreshing_drinks`
- правило: What belongs to the group «Refreshing Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 8
- +coconut water, +energy drink, +iced coffee, +juice, +lemonade, +soda, +tea, !frappe

### RESTAURANT DISHES  `restaurant_dishes`
- правило: What belongs to the group «Restaurant Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +foie gras, +greek salad, !borscht, !schnitzel

### ROOT VEGETABLES  `root_vegetables`
- правило: Vegetables eaten for the part that grows underground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- ~celeriac, +beet, +carrot, +garlic, +ginger (ginger_spice), +horseradish, +onion, +parsnip, +potato, +radish, +rutabaga, +sweet potato, +turnip, +yam, ?beet, ?carrot, ?parsnip, ?radish, ?rutabaga, ?turnip, !kohlrabi

### SALAD INGREDIENTS  `salad_ingredients`
- правило: Ingredients tossed into an ordinary green salad
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~arugula, ~crouton, +almond, +avocado, +bacon bits, +beet, +cabbage, +carrot, +celery, +cheese, +chickpea, +corn, +cranberry, +cucumber, +dressing, +egg, +lettuce, +mushroom, +olive, +onion, +pepper, +radish, +spinach, +tomato, +walnut

### SANDWICH FILLINGS  `sandwich_fillings`
- правило: Things commonly put inside a sandwich
- тип связи: `used_in`, базовая сложность 0.25
- слов: 30
- ~pastrami, ~turkey (turkey_meat), +avocado, +bacon, +cheese, +chicken, +coleslaw, +corned beef, +cucumber, +egg salad, +ham, +hummus, +jelly, +lettuce, +mayo, +meatball, +mustard, +onion, +peanut butter, +pickle, +roast beef, +salami, +sprouts, +tomato, +tuna, ?bacon, ?cheese, ?ham, ?lettuce, ?tomato

### SEAFOOD  `seafood`
- правило: Fish and shellfish eaten as food
- тип связи: `is_a`, базовая сложность 0.25
- слов: 36
- ~mahi mahi, +anchovy, +catfish, +caviar, +clam, +cod, +crab, +crawfish, +eel, +halibut, +herring, +lobster, +mussel, +octopus, +oyster, +salmon, +sardine, +scallop, +scampi, +shellfish, +shrimp, +snapper, +squid, +swordfish, +tilapia, +trout, +tuna, ?crab, ?eel, ?lobster, ?mussel, ?oyster, ?salmon, ?scallop, ?shellfish, ?shrimp

### SEAFOOD RESTAURANT  `seafood_restaurant`
- правило: What belongs to the group «Seafood Restaurant» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +crab, +lemon wedge, +oyster, !mignonette

### SIMPLE BREAD  `simple_bread`
- правило: What belongs to the group «Simple Bread» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +bakery, +flour, +water, +yeast

### SMOKED FOODS  `smoked_foods`
- правило: What belongs to the group «Smoked Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 5
- +brisket, +gouda, +mackerel, +pulled pork, +salmon

### SNACK FOODS  `snack_foods`
- правило: Packaged foods eaten between meals
- тип связи: `is_a`, базовая сложность 0.2
- слов: 27
- ~shawarma, +candy bar, +cheese stick, +chips, +cookie, +crackers, +fruit snack, +granola, +granola bar, +hummus, +jerky, +muffin, +nachos, +nuts, +pita chips, +popcorn, +Popsicle, +pretzel, +pretzels, +puffs, +raisin, +rice cake, +trail mix, +yogurt, ?chips, ?jerky, ?popcorn

### SNACKS  `snacks`
- правило: What belongs to the group «Snacks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 12
- +beef jerky, +chips, +cookie, +cookies, +crackers, +fruits, +muffins, +nuts, +popcorn, +pretzel, +pretzels, +trail mix

### SOFT DRINKS  `soft_drinks`
- правило: What belongs to the group «Soft Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +crush, +Sprite, +starry, !pibb

### SOUP  `soup`
- правило: What belongs to the group «Soup» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- +bowl, +broth, +chicken noodle, +chowder, +ladle, +miso, +steam

### SOUP INGREDIENTS  `soup_ingredients`
- правило: Ingredients commonly simmered into a pot of soup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 25
- ~cream (cream_dairy), +bacon, +barley, +bean, +broth, +cabbage, +carrot, +celery, +chicken, +corn, +dumpling, +garlic, +ham, +leek, +lentil, +mushroom, +noodle, +onion, +parsley, +pasta, +pepper, +potato, +rice, +salt, +tomato

### SOUP STOCKS  `soup_stocks`
- правило: What belongs to the group «Soup Stocks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bouillon, +chicken, +veal, !dashi

### SOUP VARIETIES  `soup_varieties`
- правило: What belongs to the group «Soup Varieties» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +chowder, !bisque, !gazpacho, !minestrone

### SPAIN DISHES  `spain_dishes`
- правило: What belongs to the group «Spain Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +paella, +tapas, !churros, !jamon

### SPICES AND HERBS  `spices_and_herbs`
- правило: Plant-based seasonings used to flavor food
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~chive, ~tarragon, +allspice, +basil, +bay leaf, +cardamom, +cilantro, +cinnamon, +clove, +coriander, +cumin, +dill, +fennel, +ginger (ginger_spice), +mint (mint_herb), +nutmeg, +oregano, +paprika, +parsley, +pepper, +rosemary, +saffron, +sage (sage_herb), +thyme, +turmeric

### SPICY FOOD  `spicy_food`
- правило: What belongs to the group «Spicy Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +black pepper, +black peppers, +cayenne, +jalapeno, xarrabbiata

### STREET FOODS  `street_foods`
- правило: What belongs to the group «Street Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +falafel, +hot dog, +kebab, +taco, !arepa, !banh mi, !churros

### SUMMER DRINKS  `summer_drinks`
- правило: What belongs to the group «Summer Drinks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +iced tea, +lemonade, +smoothie, !limeade

### THAI DISHES  `thai_dishes`
- правило: What belongs to the group «Thai Dishes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pad thai, +som tum, !khao soi, !tom kha gai

### THAI FOOD  `thai_food`
- правило: What belongs to the group «Thai Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +curry, +pad thai, +som tam, !larb

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

### TODDLER FOOD  `toddler_food`
- правило: What belongs to the group «Toddler Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +cottage cheese, +mashed banana, +rice cereal, +steamed carrot

### TROPICAL FRUITS  `tropical_fruits`
- правило: Fruits that grow in tropical climates and are sold in American stores
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~jackfruit, +banana, +coconut, +dragon fruit, +durian, +guava, +lychee, +mango, +papaya, +passion fruit, +pineapple, +plantain, ?guava, ?jackfruit, ?lychee, ?mango, ?papaya, ?pineapple, !starfruit

### TYPES OF BREAD  `types_of_bread`
- правило: What belongs to the group «Types Of Bread» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bagel, +croissant, +sourdough, !pumpernickel

### TYPES OF CHEESE  `types_of_cheese`
- правило: What belongs to the group «Types Of Cheese» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +American, +brie, +cheddar, +gouda

### TYPES OF PASTA SAUCE  `types_of_pasta_sauce`
- правило: What belongs to the group «Types Of Pasta Sauce» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +alfredo, +marinara, +pesto, !carbonara

### TYPES OF SAUCE  `types_of_sauce`
- правило: What belongs to the group «Types Of Sauce» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +alfredo, +bolognese, +marinara, +pesto

### TYPES OF SOUPS  `types_of_soups`
- правило: What belongs to the group «Types Of Soups» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +chicken, +chowder, +tomato, !gazpacho

### VEGAN FOOD  `vegan_food`
- правило: What belongs to the group «Vegan Food» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +berry, +chickpeas, +falafel, +hummus, +lentils, +tofu, !tempeh

### VEGETABLE INDUSTRY  `vegetable_industry`
- правило: What belongs to the group «Vegetable Industry» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +distribution, +farming, +harvest, +packaging

### VEGETABLES  `vegetables`
- правило: Common edible vegetables sold in an ordinary American grocery store
- тип связи: `is_a`, базовая сложность 0.12
- слов: 48
- ~kohlrabi, ~romanesco, +artichoke, +asparagus, +bean, +beet, +broccoli, +cabbage, +carrot, +cauliflower, +celery, +corn, +cucumber, +eggplant, +fennel, +kale, +leaves, +leek, +lettuce, +okra, +onion, +parsnip, +pea, +pepper, +peppers, +potato, +radish, +spinach, +squash (squash_vegetable), +tomato, +tuber, +turnip, +zucchini, ?broccoli, ?cabbage, ?carrot, ?cauliflower, ?celery, ?corn, ?eggplant, ?lettuce, ?onion, ?pea, ?potato, ?radish, ?spinach, ?turnip, ?zucchini

### VEGETARIAN FOODS  `vegetarian_foods`
- правило: What belongs to the group «Vegetarian Foods» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +lentil, +tofu, !seitan, !tempeh

### WORLD DESSERTS  `world_desserts`
- правило: What belongs to the group «World Desserts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +cheesecake, !macaron, !mochi, !tiramisu

### YELLOW FRUITS  `yellow_fruits`
- правило: What belongs to the group «Yellow Fruits» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +banana, +lemon, +mango, +pineapple


## Тема: history

### ANCIENT CIVILIZATIONS  `ancient_civilizations`
- правило: Civilizations of the ancient world
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~akkad, ~olmec, ~Phoenicia, ~Sumer, +ancient rome, +Assyria, +Aztec, +Babylon, +Carthage, +China, +Egypt, +Greece, +Inca, +Maya, +Persia, +prehistoric, +Rome, +samurai, +Sparta, +Troy, +Viking, ?Aztec, ?Babylon, ?Inca, ?Maya, ?Sumer

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
- слов: 18
- ~assembly line, ~canal, ~coal, ~cotton gin, ~factory, ~foundry, ~loom, ~machine, ~mill, ~railroad, ~railway, ~steam engine, ~telegraph, ~textile, ~worker, ?factory, ?steam engine, !smokestack

### KNIGHT THINGS  `knights_and_armor`
- правило: Things a medieval knight used or wore
- тип связи: `found_in`, базовая сложность 0.3
- слов: 16
- ~breastplate, ~chainmail, +armor, +banner, +crest, +dagger, +gauntlet, +helmet, +horse, +lance, +saddle, +shield, +spur, +squire, +sword, +visor

### HISTORIC TRADES  `old_professions`
- правило: Trades that were common in past centuries
- тип связи: `is_a`, базовая сложность 0.4
- слов: 19
- ~apothecary, ~blacksmith, ~chandler, ~cobbler, ~cooper, ~farmer, ~fletcher, ~mason, ~miller, ~potter, ~scribe, ~tanner, ~thatcher, ~weaver, ?blacksmith, ?cooper, ?weaver, !silversmith, !wheelwright

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
- слов: 14
- +civil, +Civil War, +Cold War, +Crusades, +guerrilla, +Hundred Years War, +Korean War, +naval, +Revolutionary War, +trench, +Trojan War, +Vietnam, +War of 1812, +World War

### OLD WEAPONS  `weapons_of_the_past`
- правило: Weapons used before modern firearms
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~halberd, +arrow, +axe, +bow (bow_weapon), +catapult, +club (club_stick), +crossbow, +dagger, +flail, +javelin, +mace, +musket, +sling, +spear, +sword, +trident

### WILD WEST  `wild_west`
- правило: Things associated with the American Old West
- тип связи: `found_in`, базовая сложность 0.25
- слов: 26
- +bandit, +boots, +cactus, +corral, +cowboy, +Cowboys, +gold rush, +horse, +horses, +lasso, +marshal, +outlaw, +prairie, +ranch, +revolver, +rodeo, +saloon, +sheriff, +spurs, +stagecoach, +tumbleweed, +wagon, ?cactus, ?cowboy, ?saloon, ?sheriff


## Тема: landmarks

### CLASSIC TV  `classic_tv_shows`
- правило: Television shows known across generations
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +Bonanza, +cheers (cheers_show), +Dallas, +Friends, +I Love Lucy, +Jeopardy, +mash, +Seinfeld, +Sesame Street, +Simpsons, +Star Trek, +Twilight Zone, +Wheel of Fortune, !Gunsmoke

### FAMOUS BRIDGES  `famous_bridges`
- правило: Famous bridges around the world
- тип связи: `is_a`, базовая сложность 0.4
- слов: 21
- ~Mackinac, ~Ponte Vecchio, +Bay Bridge, +bosphorus, +Brooklyn, +Charles Bridge, +Chesapeake, +Golden Gate, +lions gate, +London, +London Bridge, +Rialto, +Sydney Harbour, +tower, +Tower Bridge, ?Brooklyn, ?Golden Gate, ?Rialto, ?Sydney Harbour, ?Tower Bridge, !Millau

### FAMOUS MUSEUMS  `famous_museums`
- правило: Famous museums around the world
- тип связи: `is_a`, базовая сложность 0.45
- слов: 21
- +British Museum, +Field Museum, +gala dali castle, +Getty, +Guggenheim, +Hermitage, +Louvre, +Met, +MoMA, +Prado, +Smithsonian, +vatican museums, ?Guggenheim, ?Hermitage, ?Louvre, ?Met, ?MoMA, ?Prado, ?Uffizi, !Rijksmuseum, !Uffizi

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

### TEAM NAMES  `sports_teams`
- правило: Names of long standing American sports teams
- тип связи: `is_a`, базовая сложность 0.35
- слов: 22
- +Bears, +Braves, +Broncos, +Bulls, +Celtics, +Cowboys, +Cubs, +Dodgers, +Eagles, +Giants, +Knicks, +Lakers, +Packers, +Rangers, +Red Sox, +Steelers, +Tigers, +Yankees, ?Bears, ?Eagles, ?Lakers, ?Tigers

### THEME PARKS  `theme_parks`
- правило: Well known theme parks
- тип связи: `is_a`, базовая сложность 0.4
- слов: 19
- ~Knotts Berry Farm, +amusement park, +aquarium, +Busch Gardens, +Cedar Point, +Disney, +Disney World, +Disneyland, +Epcot, +Hershey Park, +Legoland, +Sea World, +seaworld, +Six Flags, +universal, +Universal Studios, +zoo, ?Busch Gardens, ?Sea World

### UNIVERSITIES  `universities`
- правило: Well known universities
- тип связи: `is_a`, базовая сложность 0.4
- слов: 23
- +Berkeley, +Brown, +Cambridge, +Columbia, +Cornell, +Dartmouth, +duke, +Georgetown, +Harvard, +howard, +MIT, +Notre Dame, +oxford, +Princeton, +rice, +Sorbonne, +Stanford, +Yale, ?duke, ?Harvard, ?MIT, ?Stanford, ?Yale

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

### ADVERBS  `adverbs`
- правило: What belongs to the group «Adverbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +carefully, +quickly, +silently, +slowly

### ADVERBS OF FREQUENCY  `adverbs_of_frequency`
- правило: What belongs to the group «Adverbs Of Frequency» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +often, +rarely, +sometimes, +usually

### RADIO ALPHABET  `alphabet_code`
- правило: Code words used to spell letters over a radio
- тип связи: `is_a`, базовая сложность 0.4
- слов: 24
- ~alpha, ~Bravo, ~Charlie, ~delta (delta_letter), ~Echo, ~Golf, ~Hotel, ~India, ~Juliet, ~Kilo, ~Lima, ~Mike, ~November, ~Oscar, ~Papa, ~Quebec, ~Romeo, ~Sierra, ~tango, ~Victor, ~Whiskey, ~Yankee, ~Zulu, !foxtrot

### ARABIC LANGUAGE  `arabic_language`
- правило: What belongs to the group «Arabic Language» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +Egyptian, +gulf, !levantine, !maghrebi

### ASIAN LANGUAGES  `asian_languages`
- правило: What belongs to the group «Asian Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +Hindi, +Japanese, +Korean, +mandarin

### CODED LANGUAGE  `coded_language`
- правило: What belongs to the group «Coded Language» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +gestures, +morse code, +pig pen, !anagrams

### COMMON PHRASES  `common_phrases`
- правило: What belongs to the group «Common Phrases» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.21
- слов: 4
- +be careful, +excuse me, +good morning, +goodbye

### CROSSWORD  `crossword`
- правило: What belongs to the group «Crossword» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 10
- +across, +answer, +cells, +clue, +clues, +down, +grid, +letters, +puzzle, +questions

### ENDING IN SILENT LETTERS  `ending_in_silent_letters`
- правило: What belongs to the group «Ending In Silent Letters» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +comb, +knee, +lamb, +psalm

### EXTINCT LANGUAGES  `extinct_languages`
- правило: What belongs to the group «Extinct Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +gothic, +Latin, +sumerian, !hittite

### FRENCH WORDS  `french_words`
- правило: What belongs to the group «French Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +bouquet, +deja vu, +guillotine, +rendezvous

### GRAMMAR  `grammar`
- правило: What belongs to the group «Grammar» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 12
- +adjective, +adverb, +alphabet, +article, +clause, +phrase, +predicate, +pronoun, +subject, +syntax, +verb, !gerund

### GRAMMAR TERMS  `grammar_terms`
- правило: What belongs to the group «Grammar Terms» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +adjective, +noun, +subject, +verb

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

### HYPHENATED WORDS  `hyphenated_words`
- правило: What belongs to the group «Hyphenated Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +check in, +eco friendly, +heart to heart, +mother in law

### JAPANESE WORDS  `japanese_words`
- правило: What belongs to the group «Japanese Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +bonsai, +futon, +karaoke, +tsunami

### LANGUAGE  `language`
- правило: What belongs to the group «Language» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +accent, +dialect, +grammar, +vocabulary

### LANGUAGE LEARNING APPS  `language_learning_apps`
- правило: What belongs to the group «Language Learning Apps» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +rosetta, !babbel, !duolingo, !memrise

### LANGUAGE STUDIES  `language_studies`
- правило: What belongs to the group «Language Studies» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +dialect, +lexicon, +syntax, !phoneme

### LANGUAGE UNITS  `language_units`
- правило: What belongs to the group «Language Units» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +lexicon, +syntax, !morpheme, !phoneme

### LANGUAGES  `languages`
- правило: Languages spoken around the world
- тип связи: `is_a`, базовая сложность 0.25
- слов: 24
- ~polish (polish_language), +Arabic, +Chinese, +Dutch, +English, +French, +German, +greek, +Hebrew, +Hindi, +Italian, +Japanese, +Korean, +Latin, +Portuguese, +Russian, +spanish, +Swedish, +Turkish, +Vietnamese, ?English, ?French, ?German, ?spanish

### LANGUAGES IN AFRICA  `languages_in_africa`
- правило: What belongs to the group «Languages In Africa» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +hausa, +swahili, +Zulu, !amharic

### LATIN WORDS  `latin_words`
- правило: What belongs to the group «Latin Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 8
- +alibi, +alma mater, +animus, +aqua, +caveat, +ergo, +quid, !pluribus

### LETTER  `letter`
- правило: What belongs to the group «Letter» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 7
- +address, +envelope, +message, +paper, +postcard, +sealing, !postmark

### LETTER A  `letter_a`
- правило: What belongs to the group «Letter A» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +aboard, +acreage, +adjusted, +affirmed

### MAGIC PHRASES  `magic_phrases`
- правило: What belongs to the group «Magic Phrases» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +voila, !abracadabra, !alakazam, !hocus pocus

### MAGIC SPELL  `magic_spell`
- правило: What belongs to the group «Magic Spell» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +charm, +curse, +enchant, +hex

### MAGIC SPELLS  `magic_spells`
- правило: What belongs to the group «Magic Spells» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 8
- +charm, +curse, +fireball, +hex, +jinx, +levitation, +missile, +teleport

### MEDIEVAL SWORDS  `medieval_swords`
- правило: What belongs to the group «Medieval Swords» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- !broadsword, !claymore, !falchion, !longsword

### MOTION VERBS  `motion_verbs`
- правило: What belongs to the group «Motion Verbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +dance, +jump, +run, +swim

### NONVERBAL CUES  `nonverbal_cues`
- правило: What belongs to the group «Nonverbal Cues» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +eye contact, +facial expressions, +gestures, +posture

### OLD LANGUAGES  `old_languages`
- правило: What belongs to the group «Old Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +aramaic, +greek, +Latin, +sanskrit

### PARTS OF SPEECH  `parts_of_speech`
- правило: Grammatical categories of English words
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- ~determiner, ~gerund, ~interjection, +adjective, +adverb, +article, +conjunction, +noun, +participle, +preposition, +pronoun, +verb, ?conjunction, ?interjection, ?preposition, ?pronoun

### POLITE WORDS  `polite_words`
- правило: Words used to be polite in English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 12
- +apologize, +appreciate, +excuse me, +kindly, +madam, +may, +pardon, +please, +sir, +sorry, +thanks, +welcome

### PROGRAMMING LANGUAGE  `programming_language`
- правило: What belongs to the group «Programming Language» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +java, +objective c, +php, +python, +ruby, +rust, +swift

### PROGRAMMING LANGUAGES  `programming_languages`
- правило: What belongs to the group «Programming Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 7
- +go, +java, +javascript, +python, +ruby, +rust, +swift

### PUNCTUATION MARKS  `punctuation`
- правило: Marks used to punctuate written English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~dash (dash_mark), ~ellipsis, +apostrophe, +asterisk, +bracket, +brackets, +colon, +comma, +exclamation, +exclamation point, +hyphen, +parenthesis, +period, +question, +question mark, +quotation mark, +semicolon, +slash, ?comma, ?hyphen, ?period, ?question mark, ?semicolon, xinterrobang

### QUESTION WORDS  `question_words`
- правило: Words that begin a question in English
- тип связи: `is_a`, базовая сложность 0.3
- слов: 10
- +how, +what, +when, +where, +whether, +which, +who, +whom, +whose, +why

### RHYME SCHEMES  `rhyme_schemes`
- правило: What belongs to the group «Rhyme Schemes» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +alternate rhyme, +ballad, +couplet, xtercet

### ROMANCE LANGUAGES  `romance_languages`
- правило: What belongs to the group «Romance Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +French, +Italian, +romanian, +spanish

### SANSKRIT LOANWORDS  `sanskrit_loanwords`
- правило: What belongs to the group «Sanskrit Loanwords» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 4
- +dharma, +karma, +mantra, +yoga

### SILENT B WORDS  `silent_b_words`
- правило: What belongs to the group «Silent B Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +crumb, +debt, +lamb, +thumb

### SILENT LETTER WORDS  `silent_letter_words`
- правило: What belongs to the group «Silent Letter Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +castle, +gnome, +knight, +psalm

### SOFTWARE VERBS  `software_verbs`
- правило: What belongs to the group «Software Verbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +configure, +sync, +uninstall, +upgrade

### SPANISH WORDS  `spanish_words`
- правило: What belongs to the group «Spanish Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +amigo, +fiesta, +loco, +plaza, +poco, +rojo, +tapas, !mijo

### SPELLING  `spelling`
- правило: What belongs to the group «Spelling» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +alphabet, +bee, +Champion, +contest

### SPLIT WORD PATTERNS  `split_word_patterns`
- правило: What belongs to the group «Split Word Patterns» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 4
- +grove, +knife, +piano, +storm

### SPLIT WORDS  `split_words`
- правило: What belongs to the group «Split Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 14
- +banana, +carpet, +fabric, +frame, +Frozen, +garden, +globe, +melon, +music, +quilt, +tablet, +water, +wrench, +zebra

### SWORD  `sword`
- правило: What belongs to the group «Sword» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 10
- +blade, +hilt, +katana, +rapier, +sabre, +sheath, +slashing, +tang, !broadsword, !parrying

### SWORDS  `swords`
- правило: What belongs to the group «Swords» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +katana, +rapier, !broadsword, !scimitar

### UNI WORDS  `uni_words`
- правило: What belongs to the group «Uni Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +uniform, +unison, +university, !unibrow

### VERBS OF MOVEMENT  `verbs_of_movement`
- правило: What belongs to the group «Verbs Of Movement» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 4
- +crawl, +jump, +run, +walk

### FAST WORDS  `word_fast`
- правило: English words that mean moving quickly
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- +breakneck, +brisk, +express, +fast, +fleet, +hasty, +hurried, +nimble, +prompt, +quick, +rapid, +snappy, +speedy, +swift

### WORD PUZZLES  `word_puzzles`
- правило: What belongs to the group «Word Puzzles» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +anagram, +crossword, +jumble, +scrabble

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

### WORDPLAY  `wordplay`
- правило: What belongs to the group «Wordplay» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +anagram, +palindrome, +pun, +rhyme

### WORDS  `words`
- правило: What belongs to the group «Words» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +adjective, +adverb, +noun, +verb

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

### WORDS AFTER GRAND  `words_after_grand`
- правило: What belongs to the group «Words After Grand» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +canyon, +jury, +piano, +slam

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

### WORDS BEFORE CYCLE  `words_before_cycle`
- правило: What belongs to the group «Words Before Cycle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +bi, +Life, +motor, +uni

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

### WORDS CONTAINING FALL  `words_containing_fall`
- правило: What belongs to the group «Words Containing Fall» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +downfall, +fallout, +infallible, +waterfall

### WORDS ENDING IN O  `words_ending_in_o`
- правило: What belongs to the group «Words Ending In O» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +piano, +soprano, +tornado, !palomino

### WORDS FOR BIG  `words_for_big`
- правило: What belongs to the group «Words For Big» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.19
- слов: 7
- +colossal, +enormous, +giant, +huge, +large, +massive, +monster

### WORDS FOR FIRST  `words_for_first`
- правило: What belongs to the group «Words For First» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.15
- слов: 4
- +chief, +foremost, +initial, +primary

### WORDS FOR PALE  `words_for_pale`
- правило: What belongs to the group «Words For Pale» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pallid, +wan, !ashen, !sallow

### WORDS FOR PERCEIVE  `words_for_perceive`
- правило: What belongs to the group «Words For Perceive» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 4
- +catch, +notice, +observe, +see

### WORDS FOR SAD  `words_for_sad`
- правило: What belongs to the group «Words For Sad» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +dejected, +forlorn, +sullen, +woeful

### WORDS FOR SMOOTH  `words_for_smooth`
- правило: What belongs to the group «Words For Smooth» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +glossy, +silky, +sleek, +velvety

### WORDS FOR THIN  `words_for_thin`
- правило: What belongs to the group «Words For Thin» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +gaunt, +lean, +scrawny, +slim

### WORDS FOR WALK  `words_for_walk`
- правило: What belongs to the group «Words For Walk» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +lumber, +saunter, +stride, !trudge

### WORDS WITH SPLIT SYLLABLES  `words_with_split_syllables`
- правило: What belongs to the group «Words With Split Syllables» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.28
- слов: 4
- +paper, +robot, +tiger, +zebra

### WORLD LANGUAGES  `world_languages`
- правило: What belongs to the group «World Languages» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 8
- +Arabic, +English, +French, +Hindi, +marathi, +Portuguese, +spanish, +Swedish

### WRITING WORDS  `writing_words`
- правило: Words for the parts and marks of written text
- тип связи: `found_in`, базовая сложность 0.3
- слов: 21
- ~capital (capital_letter), +byline, +caption, +chapter, +column, +comma, +draft (draft_document), +font, +footnote, +heading, +index, +letter (letter_alphabet), +margin, +outline, +page, +paragraph, +period, +sentence (sentence_writing), +signature, +title, +word


## Тема: law

### COURTROOM  `courtroom`
- правило: What is heard, handed down or worn in a courtroom
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- +crimes, +gavel, +jury, +penalties, +rights, +verdict, !titles

### COURTROOM THINGS  `courtroom_things`
- правило: Things and people found in a courtroom
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~bench (bench_court), ~sentence (sentence_punishment), ~stand (stand_witness), +bailiff, +defendant, +docket, +evidence, +exhibit, +gavel, +judge, +jury, +lawyer, +oath, +plaintiff, +testimony, +transcript, +verdict, +witness

### CRIMES  `crimes`
- правило: Acts that are against the law
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~jaywalking, +arson, +blackmail, +bribery, +burglary, +counterfeiting, +embezzlement, +forgery, +fraud, +kidnapping, +littering, +mugging, +perjury, +poaching, +robbery, +shoplifting, +smuggling, +speeding, +theft, +trespassing, +vandalism, ?arson, ?bribery, ?fraud, ?theft

### DETECTIVE WORDS  `detective_words`
- правило: Words used in a criminal investigation
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~case (case_legal), ~stakeout, +alibi, +autopsy, +clue, +evidence, +fingerprint, +footprint, +forensics, +interrogation, +lineup, +motive, +suspect, +warrant, +witness, !lead (lead_clue)

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
- слов: 20
- +affidavit, +certificate, +clause, +contract, +date line, +deed, +lease, +lease agreement, +license, +patent, +permit, +petition, +subpoena, +summons, +testament, +title, +waiver, +warrant, +will, ?contract

### MILITARY BRANCHES  `military_branches`
- правило: Branches of the armed forces
- тип связи: `is_a`, базовая сложность 0.3
- слов: 17
- +air force, +army, +artillery, +cavalry, +coast guard, +infantry, +marines, +militia, +national guard, +navy, +reserves, +space force, ?air force, ?army, ?coast guard, ?marines, ?navy

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
- слов: 16
- +badge, +baton, +cruiser, +dispatch, +flashlight, +handcuffs, +holster, +k9, +patrol, +radio, +siren, +ticket (ticket_fine), +uniform, +vest, +warrant, +whistle

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


## Тема: media

### AWARDS  `awards`
- правило: Famous prizes and awards
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +Booker, +Cannes, +Emmy, +Golden Globe, +Grammy, +Heisman, +Nobel, +Olympic medal, +Oscar, +Peabody, +Pulitzer, +Tony, ?Grammy, ?Nobel, ?Oscar, ?Pulitzer

### BOOK GENRES  `book_genres`
- правило: Categories used to classify books
- тип связи: `is_a`, базовая сложность 0.3
- слов: 25
- ~atlas (atlas_book), +biography, +comedy, +cookbook, +encyclopedia, +fantasy, +history, +horror, +humor, +memoir, +mystery, +poetry, +romance, +science fiction, +self help, +textbook, +thriller, +travel, +western, ?biography, ?horror, ?mystery, ?romance, ?science fiction, ?thriller

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
- слов: 24
- ~Tinkerbell, +Aladdin, +Anna, +Ariel, +Bambi, +beast, +Belle, +buzz, +Cinderella, +Dumbo, +Elsa, +genie, +Jasmine, +Moana, +Mulan, +Nemo, +Peter Pan, +Pinocchio, +Pocahontas, +Rapunzel, +scar, +Simba, +Snow White, +stitch

### FAIRY TALES  `fairy_tales`
- правило: Classic fairy tales children know
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- ~Hansel and Gretel, ~Jack and the Beanstalk, ~Rumpelstiltskin, ~Thumbelina, +Beauty and the Beast, +Cinderella, +fairy, +goblin, +Goldilocks, +Little Mermaid, +ogre, +Pinocchio, +Rapunzel, +Red Riding Hood, +Sleeping Beauty, +Snow White, +Three Little Pigs, +Ugly Duckling, +witch

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
- слов: 22
- +As You Like It, +Hamlet, +Julius Caesar, +King Lear, +Macbeth, +Merchant of Venice, +midsummer, +Midsummer Night, +Much Ado, +othello, +Richard III, +Romeo and Juliet, +Taming of the Shrew, +Tempest, +Twelfth Night, ?Hamlet, ?King Lear, ?Macbeth, ?Much Ado, ?othello, ?Tempest, ?Twelfth Night

### SUPERHEROES  `superheroes`
- правило: Comic book superheroes most people can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 28
- +Ant Man, +Aquaman, +Batman, +Black Widow, +blade, +Captain America, +Daredevil, +flash, +Green Lantern, +Hulk, +Iron Man, +robin, +spider man, +Spiderman, +storm, +Supergirl, +Superman, +Thor, +wolverine, +Wonder Woman, ?Batman, ?Black Widow, ?flash, ?Hulk, ?Spiderman, ?storm, ?Superman, ?Wonder Woman

### TV GENRES  `tv_genres`
- правило: Kinds of television program
- тип связи: `is_a`, базовая сложность 0.3
- слов: 19
- +cartoon, +cooking, +cooking show, +crime show, +documentary, +drama, +game show, +history, +mini series, +news, +reality, +sitcom, +soap opera, +sports, +talent show, +talk show, +variety show, ?cartoon, ?sitcom


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
- слов: 24
- ~Demeter, ~Hephaestus, ~Hestia, +Aphrodite, +Apollo, +Ares, +Artemis, +Athena, +Dionysus, +Hades, +Hera, +Hermes, +Persephone, +Poseidon, +Zeus, ?Aphrodite, ?Apollo, ?Ares, ?Artemis, ?Athena, ?Hera, ?Hermes, ?Poseidon, ?Zeus

### MYTHOLOGICAL HEROES  `greek_heroes`
- правило: Heroes of classical mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +Achilles, +Aeneas, +Ajax, +Atalanta, +Hector, +Hercules, +Jason, +Odysseus, +Orpheus, +Paris, +Perseus, +Theseus, ?Achilles, ?Hercules, ?Odysseus, ?Perseus

### LEGENDARY PLACES  `legendary_places`
- правило: Places known only from myth and legend
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +Asgard, +Atlantis, +Avalon, +Camelot, +Eden, +El Dorado, +Hades, +Olympus, +Shangri-La, +Troy, +Valhalla, +Xanadu

### MAGICAL BEINGS  `magic_creatures`
- правило: Magical beings from folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 20
- +banshee, +brownie, +dragon, +dwarf, +elf, +fairy, +genie, +gnome, +goblin, +imp, +leprechaun, +nymph, +pixie, +Sprite, +troll, +unicorn, +witch, +wizard, ?dwarf, ?fairy

### MAGIC OBJECTS  `magic_objects`
- правило: Objects with magical powers in stories
- тип связи: `is_a`, базовая сложность 0.3
- слов: 16
- ~spellbook, +amulet, +broomstick, +cauldron, +charm, +cloak, +crystal ball, +elixir, +lamp, +magic carpet, +mirror, +potion, +sword, +talisman, +wand, !ring (ring_jewelry)

### SCARY CREATURES  `monsters`
- правило: Frightening creatures from stories and folklore
- тип связи: `is_a`, базовая сложность 0.25
- слов: 27
- ~wyvern, +banshee, +bigfoot, +bogeyman, +demon, +Dracula, +ghost, +ghosts, +ghoul, +goblin, +gremlin, +hydra, +Loch Ness, +monster, +mummy, +ogre, +phantom, +poltergeist, +troll, +vampire, +werewolf, +witch, +zombie, ?ghost, ?vampire, ?werewolf, ?zombie

### MYTHICAL MONSTERS  `mythical_monsters`
- правило: Monsters from myth and legend
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~balrog, ~basilisk, ~manticore, +banshee, +cerberus, +chimera, +cyclops, +gorgon, +harpy, +hydra, +kraken, +leviathan, +medusa, +minotaur, +siren, +sphinx, ?basilisk, ?kraken

### NORSE GODS  `norse_gods`
- правило: Gods of Norse mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- ~Balder, ~Frigg, ~Heimdall, ~Vidar, +Freya, +Hel, +Loki, +Odin, +Thor, +Tyr, ?Balder, ?Freya, ?Frigg, ?Heimdall, ?Loki, ?Odin, ?Thor, ?Tyr, !Njord, xIdun

### ROMAN GODS  `roman_gods`
- правило: Gods and goddesses of Roman mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- +Apollo, +Bacchus, +Ceres, +Diana, +Juno, +Jupiter, +Mars, +mercury (mercury_god), +Minerva, +Neptune, +Pluto, +Saturn, +Venus, +Vulcan, ?Jupiter, ?Mars, ?Neptune, ?Venus

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
- слов: 20
- +Aquarius, +Aries, +cancer, +Capricorn, +Gemini, +Leo, +Libra, +Pisces, +Sagittarius, +Scorpio, +Taurus, +Virgo, ?Aquarius, ?cancer, ?Gemini, ?Leo, ?Pisces, ?Scorpio, ?Taurus, ?Virgo


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
- слов: 24
- ~ginger (ginger_name), +Bailey, +Bella, +Buddy, +Charlie, +Coco, +Daisy, +dear, +Fluffy, +honey, +Lucy, +Max, +mittens, +Molly, +Oreo, +peanut, +Rex, +Rocky, +Shadow, +Sparky, +sweetie, +tiger, +Whiskers, ?Buddy

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
- слов: 20
- +Alessandro, +Chiara, +Elena, +Enzo, +Francesca, +Giovanni, +Giulia, +Luca, +Marco, +Marta, +Matteo, +Paolo, +Rosa, +Sofia, +Stefano, +Valentina, ?Giovanni, ?Luca, ?Marco, ?Matteo

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
- слов: 19
- +anders, +Astrid, +Bjorn, +Elsa, +Erik, +gustav, +Ingrid, +Lars, +Magnus, +Nils, +Odin, +Sven, +Thor, !Freja, !Linnea, !olav, !Sigrid, !Solveig, !tord

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

### ALPINE PLANTS  `alpine_plants`
- правило: What belongs to the group «Alpine Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +anemone, !edelweiss, !gentian, !saxifrage

### DIRT THINGS  `animal_tracks_and_signs`
- правило: Marks and things you see in bare dirt
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~ant, ~dust, ~footprint, ~gravel, ~hole, ~mud, ~pebble, ~puddle, ~root, ~seed, ~stone, ~tire mark, ~track, ~twig, ~worm

### BIRTHSTONE MONTHS  `birthstone_months`
- правило: What belongs to the group «Birthstone Months» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.1
- слов: 4
- +April, +July, +October, +September

### BIRTHSTONES  `birthstones`
- правило: What belongs to the group «Birthstones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +emerald, +garnet, +pearl, +ruby

### BIRTHSTONES BY MONTH  `birthstones_by_month`
- правило: What belongs to the group «Birthstones By Month» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +aquamarine, +garnet, +pearl, +peridot

### BODIES OF WATER  `bodies_of_water`
- правило: Natural or man-made bodies of water on the surface of the earth
- тип связи: `is_a`, базовая сложность 0.2
- слов: 38
- ~spring (spring_water), +bay, +brook, +canal, +cove, +creek, +delta (delta_river), +estuary, +fjord, +gulf, +harbor, +inlet, +lagoon, +lake, +marsh, +ocean, +pond, +pool, +reservoir, +river, +sea, +strait, +stream, +swamp, +waterfall, ?bay, ?canal, ?estuary, ?inlet, ?lagoon, ?lake, ?ocean, ?pond, ?river, ?sea, ?strait, ?waterfall, !sound (sound_water)

### CARNIVOROUS PLANTS  `carnivorous_plants`
- правило: What belongs to the group «Carnivorous Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +pitcher plant, !sundew, !venus flytrap, xbladderwort

### CLIMBING PLANTS  `climbing_plants`
- правило: What belongs to the group «Climbing Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 6
- +grapes, +honeysuckle, +Ivy, +rose, +vine, !clematis

### SKY WORDS  `cloud_and_sky`
- правило: Things you can see in the sky
- тип связи: `found_in`, базовая сложность 0.3
- слов: 20
- +aurora, +balloon, +bird, +cloud, +comet, +eclipse, +fog, +haze, +helicopter, +kite (kite_toy), +lightning, +meteor, +moon, +plane (plane_aircraft), +rainbow, +satellite, +smoke, +star (star_space), +sun, +sunset

### DESERT PLANTS  `desert_plants`
- правило: What belongs to the group «Desert Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +aloe, +cactus, +sagebrush, +yucca

### DESERT THINGS  `desert_things`
- правило: Things found in a hot desert
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- +cactus, +camel, +canyon, +coyote, +drought, +dune, +heat, +lizard, +mirage, +oasis, +rattlesnake, +sagebrush, +sand, +scorpion, +snake, +tumbleweed, +vulture, !rock (rock_stone)

### DRIVER  `driver`
- правило: What belongs to the group «Driver» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +accelerate, +brake, +clutch, +steer

### EUROPEAN RIVERS  `european_rivers`
- правило: What belongs to the group «European Rivers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +Danube, +Rhine, +Seine, +Thames

### EXTREME WEATHER  `extreme_weather`
- правило: What belongs to the group «Extreme Weather» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +blizzard, +hail, +squall, !derecho

### FAMOUS RIVERS  `famous_rivers`
- правило: What belongs to the group «Famous Rivers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.49
- слов: 4
- +Amazon, +Congo, +Danube, +Ganges

### FLOWER  `flower`
- правило: What belongs to the group «Flower» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 12
- ~pistil, +azalea, +bud, +camellia, +nectar, +petal, +pollen, +rose, +sepal, +stamen, +stem, +tulip

### FLOWER MARKET  `flower_market`
- правило: What belongs to the group «Flower Market» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 4
- +bouquet, +florists, +flower food, +Sunflowers

### FLOWER PARTS  `flower_parts`
- правило: Parts of a flowering plant
- тип связи: `part_of`, базовая сложность 0.35
- слов: 21
- ~sepal, +blossom, +bud, +bulb, +leaf, +nectar, +petal, +pistil, +pollen, +root, +seed, +stalk, +stamen, +stem, +thorn, ?nectar, ?petal, ?pistil, ?pollen, ?sepal, ?stamen

### FLOWERS  `flowers`
- правило: Kinds of flowers commonly sold or grown in gardens
- тип связи: `is_a`, базовая сложность 0.15
- слов: 52
- ~asters, ~begonia, ~lotuses, ~nigella, ~petunia, ~phlox, ~zinnia, +aster, +azalea, +bluebell, +buttercup, +camellia, +carnation, +daffodil, +dahlia, +Daisy, +dandelion, +geranium, +hyacinth, +iris, +Jasmine, +lavender (lavender_plant), +lilac, +Lily, +magnolia, +marigold, +orchid, +pansy, +peony, +poppy, +rose, +sepals, +sunflower, +tulip, +Violet, +wildflowers, ?azalea, ?dahlia, ?Daisy, ?iris, ?Jasmine, ?lilac, ?Lily, ?orchid, ?peony, ?petunia, ?poppy, ?rose, ?sunflower, ?tulip, ?Violet, ?zinnia

### FLOWERS IN BLOOM  `flowers_in_bloom`
- правило: What belongs to the group «Flowers In Bloom» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 4
- +Daisy, +Lily, +rose, +tulip

### FOREST  `forest`
- правило: What belongs to the group «Forest» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 13
- +Aspen, +bird, +elk, +ferns, +grove, +jaguar, +moss, +mushroom, +squirrel, +tree, +trees, +vines, +wildlife

### FOREST FLOOR  `forest_floor`
- правило: What belongs to the group «Forest Floor» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +Fern, +lichen, +moss, !humus

### FOREST FUNGI  `forest_fungi`
- правило: What belongs to the group «Forest Fungi» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +morel, !porcini, !puffball, xmatsutake

### FOREST LAYERS  `forest_layers`
- правило: What belongs to the group «Forest Layers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +canopy, +ground, +herb, +shrub

### FOREST TREES  `forest_trees`
- правило: What belongs to the group «Forest Trees» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +beech, +cedar, +elm, +spruce

### FORESTS  `forests`
- правило: What belongs to the group «Forests» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 12
- +Amazon, +boreal, +borneo, +canopy, +mangrove, +rainforest, +redwood, +taiga, +temperate, +trees, +undergrowth, +wildlife

### GARDEN  `garden`
- правило: What belongs to the group «Garden» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 19
- +bloom, +compost, +fence, +flower, +flowers, +greenhouse, +hedge, +hose, +mulch, +rake, +roses, +seedling, +seeds, +shovel, +soil, +trellis, +watering, +weeds, +zen

### GARDEN CARE  `garden_care`
- правило: What belongs to the group «Garden Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +fertilize, +mulch, +prune, +pruning, +water, +watering can, +weeding, !mulching

### GARDEN ELEMENTS  `garden_elements`
- правило: What belongs to the group «Garden Elements» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +fence, +hedge, +hose, +turf

### GARDEN FEATURES  `garden_features`
- правило: What belongs to the group «Garden Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.57
- слов: 6
- +arbor, +fountain, +gazebo, +hedge, +trellis, !sundial

### GARDEN FERTILIZERS  `garden_fertilizers`
- правило: What belongs to the group «Garden Fertilizers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +compost, +manure, +mulch, +soil

### GARDEN FLOWERS  `garden_flowers`
- правило: What belongs to the group «Garden Flowers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 9
- +dahlia, +Daisy, +marigold, +pansy, +peony, +rose, +sunflower, +tulip, !zinnia

### GARDEN HERBS  `garden_herbs`
- правило: What belongs to the group «Garden Herbs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 5
- +basil, +cilantro, +parsley, +rosemary, +thyme

### GARDEN PESTS  `garden_pests`
- правило: What belongs to the group «Garden Pests» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 8
- +caterpillar, +slug, +snail, +weevil, !aphid, !mealybug, !whitefly, xthrip

### GARDEN PLANTS  `garden_plants`
- правило: Plants people grow in a home garden
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~hosta, ~lavender (lavender_plant), +basil, +bean, +carrot, +cucumber, +Fern, +Ivy, +lettuce, +marigold, +mint (mint_herb), +pepper, +pumpkin, +rose, +squash (squash_vegetable), +strawberry, +sunflower, +tomato, +tulip, +zucchini

### GARDEN SHRUBS  `garden_shrubs`
- правило: What belongs to the group «Garden Shrubs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +daphne, +holly, +juniper, !hydrangea

### GARDEN SPACE  `garden_space`
- правило: What belongs to the group «Garden Space» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.33
- слов: 4
- +greenhouse, +plants, +shrubs, +soil

### GARDENING TOOLS  `gardening_tools`
- правило: What belongs to the group «Gardening Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 6
- +hoe, +rake, +shovel, +trowel, +watering can, !pruner

### GEMSTONE  `gemstone`
- правило: What belongs to the group «Gemstone» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 6
- +emerald, +onyx, +opal, +pearl, +ruby, +sapphire

### GEMSTONE CUTS  `gemstone_cuts`
- правило: What belongs to the group «Gemstone Cuts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 11
- +baguette, +brilliant, +cushion, +emerald, +marquise, +oval, +pear, +princess, +radiant, +trillion, !asscher

### GEMSTONE TREATMENTS  `gemstone_treatments`
- правило: What belongs to the group «Gemstone Treatments» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +fracture, +heat, +irradiation, !oiling

### GEMSTONES  `gemstones`
- правило: Precious or semi-precious stones used in jewelry
- тип связи: `is_a`, базовая сложность 0.25
- слов: 30
- ~tanzanite, +agate, +amethyst, +aquamarine, +coral, +diamond (diamond_gem), +emerald, +garnet, +jade, +lapis, +moonstone, +obsidian, +onyx, +opal, +pearl, +peridot, +quartz, +ruby, +sapphire, +topaz, +turquoise, ?amethyst, ?emerald, ?garnet, ?jade, ?opal, ?ruby, ?sapphire, ?topaz, ?turquoise

### HARDWOOD TREES  `hardwood_trees`
- правило: What belongs to the group «Hardwood Trees» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +beech, +hickory, +maple, +walnut

### HERB GARDEN  `herb_garden`
- правило: What belongs to the group «Herb Garden» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 8
- +basil, +chives, +coriander, +dill, +parsley, +rosemary, +thyme, !tarragon

### HOUSEPLANT CARE  `houseplant_care`
- правило: What belongs to the group «Houseplant Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +drainage, +fertilizer, +grow light, !mulching

### IGNEOUS ROCKS  `igneous_rocks`
- правило: What belongs to the group «Igneous Rocks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +basalt, +granite, +obsidian, +pumice

### IN A GARDEN SHED  `in_a_garden_shed`
- правило: What belongs to the group «In A Garden Shed» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +hoe, +pot, +rake, +trowel

### IN THE RIVER  `in_the_river`
- правило: What belongs to the group «In The River» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 5
- +otter, +raft, +reeds, +salmon, xcrucian carp

### JUNGLE PLANTS  `jungle_plants`
- правило: What belongs to the group «Jungle Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +bamboo, +Fern, +orchid, +vine

### LIGHT SOURCES  `light_sources`
- правило: Things that give off light
- тип связи: `does_action`, базовая сложность 0.3
- слов: 31
- ~glowstick, ~streetlight, +bulb, +campfire, +candle, +fire, +firefly, +fireplace, +flashlight, +headlight, +lamp, +lantern, +laser, +lightning, +match, +moon, +neon, +prism, +screen (screen_display), +star (star_space), +sun, +torch, ?bulb, ?candle, ?fire, ?headlight, ?lamp, ?lantern, ?laser, ?sun, ?torch

### LONG RIVERS  `long_rivers`
- правило: What belongs to the group «Long Rivers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 4
- +Amazon, +Congo, +Mississippi, +Nile

### MEDICINAL PLANTS  `medicinal_plants`
- правило: What belongs to the group «Medicinal Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +valerian, +yarrow, !echinacea, !feverfew

### METAMORPHIC ROCKS  `metamorphic_rocks`
- правило: What belongs to the group «Metamorphic Rocks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +slate, !gneiss, !quartzite, !schist

### MILESTONES  `milestones`
- правило: What belongs to the group «Milestones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.13
- слов: 4
- +career, +graduate, +honor, +success

### MOUNTAIN  `mountain`
- правило: What belongs to the group «Mountain» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 14
- +Alps, +altitude, +Andes, +cliff, +climb, +eagle, +glacier, +Himalayas, +peak, +ridge, +Rockies, +snow, +summit, +trail

### MOUNTAIN ACTIVITY  `mountain_activity`
- правило: What belongs to the group «Mountain Activity» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +camping, +climbing, +hiking, +skiing

### MOUNTAIN CLIMBING  `mountain_climbing`
- правило: What belongs to the group «Mountain Climbing» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +altitude, +gear, +peak, +rope

### MOUNTAIN EQUIPMENT  `mountain_equipment`
- правило: What belongs to the group «Mountain Equipment» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +harness, !carabiner, !crampon, !piton

### MOUNTAIN FEATURES  `mountain_features`
- правило: What belongs to the group «Mountain Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +glacier, +ridge, +summit, !basecamp

### MOUNTAIN HAZARDS  `mountain_hazards`
- правило: What belongs to the group «Mountain Hazards» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +avalanche, +landslide, !crevasse, !rockfall

### MOUNTAIN HIKING  `mountain_hiking`
- правило: What belongs to the group «Mountain Hiking» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +altitude, +backpack, +summit, +trail

### MOUNTAIN LIFE  `mountain_life`
- правило: What belongs to the group «Mountain Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +bigfoot, +climate, +mountain animals, +terrain

### MOUNTAIN PEAKS  `mountain_peaks`
- правило: What belongs to the group «Mountain Peaks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 7
- +Denali, +Everest, +Fuji, +k2, +Kilimanjaro, !Aconcagua, !Matterhorn

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

### NASCAR DRIVERS  `nascar_drivers`
- правило: What belongs to the group «Nascar Drivers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +earnhardt, +Johnson, +pearson, +petty

### NATURAL DISASTERS  `natural_disasters`
- правило: Destructive natural events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 28
- ~mudslide, +avalanche, +blizzard, +cyclone, +drought, +earthquake, +eruption, +famine, +flood, +hurricane, +landslide, +quake, +sinkhole, +tornado, +tsunami, +volcano, +wildfire, ?avalanche, ?blizzard, ?cyclone, ?drought, ?earthquake, ?flood, ?hurricane, ?tornado, ?tsunami, ?volcano, ?wildfire

### OCEAN  `ocean`
- правило: What belongs to the group «Ocean» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 25
- +abyss, +Arctic, +Atlantic, +bay, +beach, +blue, +coral, +deep, +depths, +fish, +gulf, +Indian, +kelp, +Pacific, +pearl, +reef, +salt, +saltwater, +salty, +shark, +tide, +water, +waves, +whale, !narwhal

### OCEAN ACTIVITIES  `ocean_activities`
- правило: What belongs to the group «Ocean Activities» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 4
- +diving, +sailing, +snorkel, +surfing

### OCEAN CREATURES  `ocean_creatures`
- правило: What belongs to the group «Ocean Creatures» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +manta, +nautilus, +starfish, !blowfish

### OCEAN CURRENTS  `ocean_currents`
- правило: What belongs to the group «Ocean Currents» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +California, +gulf, +labrador, !kuroshio

### OCEAN DANGERS  `ocean_dangers`
- правило: What belongs to the group «Ocean Dangers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.43
- слов: 5
- +drown, +shark, +shipwreck, +tornado, +tsunami

### OCEAN LAYERS  `ocean_layers`
- правило: What belongs to the group «Ocean Layers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.59
- слов: 4
- +abyss, +benthic, +pelagic, +surface

### OCEAN LIFE  `ocean_life`
- правило: What belongs to the group «Ocean Life» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 16
- +coral, +crab, +crabs, +crustacean, +fish, +jellyfish, +kelp, +plankton, +reef, +seaweed, +shark, +starfish, +turtle, +whale, +whales, !mollusca

### OCEAN PHENOMENA  `ocean_phenomena`
- правило: What belongs to the group «Ocean Phenomena» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +tide, +tsunami, +vortex, +Whirlpool

### OCEANIA  `oceania`
- правило: What belongs to the group «Oceania» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +Australia, +Fiji, +Guam, +Papua New Guinea

### OCEANIC  `oceanic`
- правило: What belongs to the group «Oceanic» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +anemone, +barnacle, +coral, +crab

### OCEANS  `oceans`
- правило: What belongs to the group «Oceans» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +Arctic, +Atlantic, +Indian, +Pacific

### ON THE OCEAN FLOOR  `on_the_ocean_floor`
- правило: What belongs to the group «On The Ocean Floor» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +anchor, +mud, +pebbles, +starfish

### PARTS OF A FLOWER  `parts_of_a_flower`
- правило: What belongs to the group «Parts Of A Flower» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~pistil, +petal, +sepal, +stamen

### PLANT BASED MILKS  `plant_based_milks`
- правило: What belongs to the group «Plant Based Milks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +almond, +coconut, +oat, +soy

### PLANT CARE  `plant_care`
- правило: What belongs to the group «Plant Care» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 4
- +fertilize, +graft, +pot, +water

### PLANT FORM  `plant_form`
- правило: What belongs to the group «Plant Form» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +algae, +grass, +moss, +succulent

### PLANT LIFE CYCLE  `plant_life_cycle`
- правило: What belongs to the group «Plant Life Cycle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 8
- +baby plant, +berry, +blossom, +bud, +flowering, +germination, +growth, +seed

### PLANTS RELATED  `plants_related`
- правило: What belongs to the group «Plants Related» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +root, +sap, +seed, +stem

### POPULAR STREETS  `popular_streets`
- правило: What belongs to the group «Popular Streets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +Abbey Road, +champs lys es, +Fifth Avenue, +oxford street

### PRECIOUS STONES  `precious_stones`
- правило: What belongs to the group «Precious Stones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 10
- +emerald, +garnet, +jade, +moonstone, +onyx, +opal, +ruby, +sapphire, +topaz, +turquoise

### RAINFOREST LAYERS  `rainforest_layers`
- правило: What belongs to the group «Rainforest Layers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +canopy, +emergent, +floor, !understory

### RED GEMSTONES  `red_gemstones`
- правило: What belongs to the group «Red Gemstones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.42
- слов: 4
- +coral, +garnet, +jasper, +ruby

### RIVER  `river`
- правило: What belongs to the group «River» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 8
- +Amazon, +Danube, +fish, +fresh water, +Mississippi, +Nile, +rapids, +stream

### RIVER FEATURES  `river_features`
- правило: Parts and features of a river described in everyday English
- тип связи: `part_of`, базовая сложность 0.35
- слов: 20
- ~basin, ~bed, ~bend, ~channel, ~current (current_water), ~delta (delta_river), ~eddy, ~ford (ford_river), ~gorge, ~rapids, ~shore, ~source, ~tributary, ~waterfall, +bank (bank_river), +mouth (mouth_river), !floodplain, !headwater, !levee, !sandbar

### RIVERS OF EUROPE  `rivers_of_europe`
- правило: What belongs to the group «Rivers Of Europe» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.54
- слов: 4
- +Danube, +Rhine, +Seine, +Thames

### ROCK BANDS  `rock_bands`
- правило: What belongs to the group «Rock Bands» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +aerosmith, +green day, +pink floyd, +u2

### ROCK COLLECTION ITEMS  `rock_collection_items`
- правило: What belongs to the group «Rock Collection Items» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 4
- +fossils, +mineral, +quartz, !geode

### ROCK CONCERT  `rock_concert`
- правило: What belongs to the group «Rock Concert» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 4
- +amp, +drums, +guitar, +stage

### ROCK CYCLE  `rock_cycle`
- правило: What belongs to the group «Rock Cycle» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +erosion, +igneous, +metamorphic, +sedimentary

### ROCK GENRES  `rock_genres`
- правило: What belongs to the group «Rock Genres» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.24
- слов: 4
- +classic, +goth, +metal, +punk

### ROCK TYPES  `rock_types`
- правило: What belongs to the group «Rock Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 6
- +basalt, +flint, +granite, +minerals, +obsidian, +slate

### ROCKEFELLER FAMILY  `rockefeller_family`
- правило: What belongs to the group «Rockefeller Family» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.32
- слов: 4
- +dynasty, +elite family, +standard oil, xkykuit

### ROCKET  `rocket`
- правило: What belongs to the group «Rocket» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.36
- слов: 18
- +ariane, +astronaut, +blast, +booster, +countdown, +engine, +fuel, +fuel tank, +guidance system, +launch, +launchpad, +mission, +NASA, +orbit, +payload, +stabilizer fins, +thrust, +thruster

### ROCKET COMPONENTS  `rocket_components`
- правило: What belongs to the group «Rocket Components» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.53
- слов: 4
- +booster, +nozzle, +payload, +thruster

### ROCKS  `rocks`
- правило: What belongs to the group «Rocks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +basalt, +dolomite, +granite, +obsidian

### ROCKS AND MINERALS  `rocks_and_minerals`
- правило: Common rocks and minerals from the ground
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~chalk (chalk_rock), +basalt, +boulder, +clay, +coal, +flint, +granite, +gravel, +gypsum, +iron ore, +limestone, +marble (marble_stone), +obsidian, +pebble, +pumice, +quartz, +salt, +sandstone, +shale, +slate

### ROLLING STONES  `rolling_stones`
- правило: What belongs to the group «Rolling Stones» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.35
- слов: 4
- +Charlie, +keith, +mick, +ronnie

### BEACH THINGS  `sea_shore_things`
- правило: Things you find on an ocean beach
- тип связи: `found_in`, базовая сложность 0.2
- слов: 20
- ~sandcastle, +boardwalk, +cooler, +crab, +driftwood, +dune, +gull, +jellyfish, +pebble, +sand, +seaweed, +shell, +starfish, +sunscreen, +surfboard, +tide, +towel, +umbrella, +wave (wave_water), !kite (kite_toy)

### SEASON SIGNS  `season_signs`
- правило: What belongs to the group «Season Signs» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 4
- +blossom, +foliage, +harvest, +snowman

### SEASONAL HOLIDAYS  `seasonal_holidays`
- правило: What belongs to the group «Seasonal Holidays» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.22
- слов: 4
- +christmas tree, +Easter, +Halloween, +New Year

### SEASONING  `seasoning`
- правило: What belongs to the group «Seasoning» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 8
- +garlic, +oregano, +paprika, +salt, +salty, +sour, +spicy, +sweet

### SEASONING TYPES  `seasoning_types`
- правило: What belongs to the group «Seasoning Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 4
- +herbs, +salt, +spices, !umami

### SEASONAL WORDS  `seasons_and_nature`
- правило: Words describing the changing seasons outdoors
- тип связи: `found_in`, базовая сложность 0.3
- слов: 18
- ~molt, +bloom, +blossom, +bud, +equinox, +foliage, +frost, +harvest, +hibernate, +migrate, +ripen, +shed, +snowfall, +solstice, +sprout, +sunrise, +thaw, +wither

### SKY CONSTELLATIONS  `sky_constellations`
- правило: What belongs to the group «Sky Constellations» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +Orion, +Ursa Major, +Ursa Minor, !Cassiopeia

### SKY PREDATORS  `sky_predators`
- правило: What belongs to the group «Sky Predators» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +eagle, +falcon, +hawk, +vulture

### SKY SIGHTS  `sky_sights`
- правило: What belongs to the group «Sky Sights» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 5
- +halo, +mirage, +rainbow, +sunset, xsundog

### SKYDIVING  `skydiving`
- правило: What belongs to the group «Skydiving» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.47
- слов: 6
- +adrenaline, +altitude, +freefall, +jumpsuit, +landing, +parachute

### SKYSCAPERS  `skyscapers`
- правило: What belongs to the group «Skyscapers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +elevator, +lobby, +penthouse, +rooftop

### SKYSCRAPERS  `skyscrapers`
- правило: What belongs to the group «Skyscrapers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +elevator, +lobby, +penthouse, +rooftop

### SPACE ROCKS  `space_rocks`
- правило: What belongs to the group «Space Rocks» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 4
- +asteroid, +comet, +meteor, !bolide

### STONE AGE  `stone_age`
- правило: What belongs to the group «Stone Age» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 7
- +arrowhead, +cave art, +caveman, +flint, +hieroglyphics, +nomad, +spear

### STONEHENGE  `stonehenge`
- правило: What belongs to the group «Stonehenge» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.18
- слов: 4
- +circle, +druids, +england, +stone

### STORMS  `storms`
- правило: Kinds of violent weather events
- тип связи: `is_a`, базовая сложность 0.3
- слов: 26
- ~derecho, ~hailstorm, +blizzard, +cyclone, +downpour, +dust storm, +gale, +hurricane, +ice storm, +monsoon, +squall, +Tempest, +thunder, +thunderstorm, +tornado, +typhoon, +whirlwind, ?blizzard, ?cyclone, ?gale, ?hurricane, ?monsoon, ?squall, ?Tempest, ?tornado, ?typhoon

### STREET FEATURES  `street_features`
- правило: What belongs to the group «Street Features» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.56
- слов: 4
- +crosswalk, +curb, +sidewalk, !streetlamp

### STREET LAMP  `street_lamp`
- правило: What belongs to the group «Street Lamp» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.31
- слов: 4
- +alley, +avenue, +base, !amperage

### STREET NAMES  `street_names`
- правило: What belongs to the group «Street Names» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.29
- слов: 4
- +alley, +boulevard, +drive, +lane

### STREET PARTS  `street_parts`
- правило: What belongs to the group «Street Parts» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.48
- слов: 4
- +cul de sac, +curb, +gutter, +pavement

### STREET PERFORMERS  `street_performers`
- правило: What belongs to the group «Street Performers» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +fire eater, +poet, +puppeteer, !busker

### STREETS  `streets`
- правило: What belongs to the group «Streets» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +alley, +boulevard, +parkway, +road

### SUNFLOWER  `sunflower`
- правило: What belongs to the group «Sunflower» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.27
- слов: 4
- +petal, +seed, +stem, +yellow

### FOREST THINGS  `things_in_the_forest`
- правило: Things you find walking through a forest
- тип связи: `found_in`, базовая сложность 0.25
- слов: 20
- ~pinecone, +acorn, +bark (bark_tree), +branch (branch_tree), +campsite, +clearing, +deer, +Fern, +fox, +leaf, +log, +moss, +mushroom, +owl, +squirrel, +stream, +stump, +trail, +tree, +undergrowth

### THINGS IN THE SKY  `things_in_the_sky`
- правило: What belongs to the group «Things In The Sky» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.25
- слов: 4
- +comet, +moon, +rainbow, +sun

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

### THORNY PLANTS  `thorny_plants`
- правило: What belongs to the group «Thorny Plants» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +bramble, +cactus, +rose, !barberry

### TREE  `tree`
- правило: What belongs to the group «Tree» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.26
- слов: 8
- +branches, +fruit, +leaves, +log, +nest, +root, +roots, +sawdust

### TREE PARTS  `tree_parts`
- правило: Physical parts of a living tree
- тип связи: `part_of`, базовая сложность 0.25
- слов: 20
- ~needle (needle_pine), +acorn, +bark (bark_tree), +bough, +branch (branch_tree), +bud, +cone, +knot, +leaf, +limb, +pulp, +root, +sap, +seed, +shoot, +stump, +trunk (trunk_tree), +twig, !crown (crown_tree), !ring (ring_tree)

### TREE SPECIES  `tree_species`
- правило: What belongs to the group «Tree Species» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.4
- слов: 4
- +birch, +cedar, +maple, +pine

### TREE TYPES  `tree_types`
- правило: What belongs to the group «Tree Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.39
- слов: 5
- +birch, +maple, +oak, +pine, +Willow

### TREEHOUSE  `treehouse`
- правило: What belongs to the group «Treehouse» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.34
- слов: 5
- +hatch, +ladder, +planks, +rope, +window

### TREELESS  `treeless`
- правило: What belongs to the group «Treeless» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 4
- +bare, +clearing, +glade, !denuded

### TREES  `trees`
- правило: Kinds of trees an average American can name
- тип связи: `is_a`, базовая сложность 0.2
- слов: 35
- ~apple (apple_fruit), +ash, +Aspen, +beech, +birch, +cedar, +cherry, +chestnut, +cypress, +dogwood, +elm, +fir, +hickory, +juniper, +magnolia, +maple, +oak, +palm (palm_tree), +pine, +poplar, +redwood, +spruce, +sycamore, +walnut, +Willow, ?birch, ?cedar, ?cherry, ?elm, ?maple, ?oak, ?pine, ?poplar, ?redwood, ?Willow

### TYPES OF FORESTS  `types_of_forests`
- правило: What belongs to the group «Types Of Forests» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +boreal, +coniferous, +deciduous, +mangrove

### TYPES OF TREES  `types_of_trees`
- правило: What belongs to the group «Types Of Trees» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.52
- слов: 4
- +elm, +pine, +poplar, +Rowan

### TYPES OF WEATHER  `types_of_weather`
- правило: What belongs to the group «Types Of Weather» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.44
- слов: 8
- +cloudy, +foggy, +rainfall, +rainy, +snowstorm, +sunny, +sunshine, +thunderstorm

### UNDERGROUND THINGS  `underground_things`
- правило: Things found under the surface of the ground
- тип связи: `found_in`, базовая сложность 0.35
- слов: 18
- ~ant nest, ~aquifer, ~bulb, ~burrow, ~cave, ~coal, ~fossil, ~mole (mole_animal), ~ore, ~pipe (pipe_tube), ~root, ~seed, ~sewer, ~Subway, ~treasure, ~tunnel, ~worm, +mine

### WALL STREET  `wall_street`
- правило: What belongs to the group «Wall Street» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.23
- слов: 4
- +brokers, +economy, +finance, +stocks

### FORMS OF WATER  `water_states`
- правило: Forms water takes in nature
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~dew, ~drizzle, ~fog, ~frost, ~glacier, ~hail, ~humidity, ~icicle, ~mist, ~puddle, ~sleet, ~slush, ~vapor, +cloud, +ice, +rain, +snow, +steam

### WEATHER CONDITIONS  `weather_conditions`
- правило: What belongs to the group «Weather Conditions» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.46
- слов: 11
- +breezy, +cloudy, +drizzle, +fog, +frost, +hazy, +humid, +overcast, +rain, +wind, +windy

### WEATHER EVENTS  `weather_events`
- правило: What belongs to the group «Weather Events» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.37
- слов: 14
- +blizzard, +cyclone, +drizzle, +drought, +flood, +hail, +heat, +heatwave, +rainbow, +shower, +squall, +storm, +thunder, +tornado

### WEATHER FORECASTER  `weather_forecaster`
- правило: What belongs to the group «Weather Forecaster» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.17
- слов: 4
- +forecast, +future, +news, +precipitation

### WEATHER PHENOMENA  `weather_phenomena`
- правило: What belongs to the group «Weather Phenomena» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.38
- слов: 13
- +aurora, +ball lightning, +blizzard, +breeze, +cyclone, +fog, +hail, +hurricane, +lightning, +rainbow, +thunder, +tornado, +typhoon

### WEATHER REPORT  `weather_report`
- правило: What a weather report names or predicts
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~directions, ~seasons, +forecast, +humidity, +radar, +storms, xmonths

### WEATHER SEASONS  `weather_seasons`
- правило: What belongs to the group «Weather Seasons» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 4
- +dry, +monsoon, +temperate, +tropical

### WEATHER TOOLS  `weather_tools`
- правило: What belongs to the group «Weather Tools» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.58
- слов: 4
- +barometer, +radar, +vane, !anemometer

### WEATHER TYPES  `weather_types`
- правило: What belongs to the group «Weather Types» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.41
- слов: 11
- +Arctic, +clear, +cloudy, +desert, +foggy, +rainy, +snowy, +sunny, +temperate, +tropical, +windy

### WEATHER WORDS  `weather_words`
- правило: Words describing weather conditions or events in the sky
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- +blizzard, +breeze, +cloud, +downpour, +drizzle, +flurry, +fog, +frost, +gale, +hail, +heat wave, +humidity, +hurricane, +lightning, +mist, +rain, +shower, +sleet, +snow, +storm, +sunshine, +thaw, +thunder, +tornado, +wind

### WILD PLANTS  `wild_plants`
- правило: Plants that grow wild in fields and woods
- тип связи: `is_a`, базовая сложность 0.35
- слов: 23
- ~bracken, ~bramble, ~clover, ~dandelion, ~Fern, ~Ivy, ~lichen, ~moss, ~mushroom, ~nettle, ~reed, ~thistle, ~vine, ~weed, ?clover, ?dandelion, ?Fern, ?moss, !cattail, !goldenrod, !milkweed, !ragweed, !sedge

### WINTER WEATHER  `winter_weather`
- правило: What belongs to the group «Winter Weather» as used in the original game
- тип связи: `associated_with`, базовая сложность 0.51
- слов: 4
- +blizzard, +frost, +icicle, +snowfall


## Тема: ocean

### CORAL REEF  `coral_reef`
- правило: Things found on a coral reef
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~angelfish, ~clownfish, ~parrotfish, ~sponge (sponge_animal), +algae, +anemone, +coral, +eel, +grouper, +jellyfish, +reef shark, +seahorse, +starfish, +turtle, +urchin

### DEEP SEA  `deep_sea`
- правило: Things found in the deep ocean
- тип связи: `found_in`, базовая сложность 0.4
- слов: 19
- ~abyss, ~darkness, ~giant squid, ~hydrothermal vent, ~lantern fish, ~pressure, ~sediment, ~sperm whale, ~squid, ~submarine, ~trench, ~tube worm, ~vent, ~whale fall, ?abyss, ?anglerfish, ?viperfish, !anglerfish, !coelacanth

### DIVING GEAR  `diving_gear`
- правило: Equipment used for scuba diving and snorkeling
- тип связи: `used_in`, базовая сложность 0.35
- слов: 14
- ~hood (hood_garment), +buoy, +compass, +dive knife, +fins, +flashlight, +gauge, +gloves, +mask, +regulator, +snorkel, +tank (tank_container), +weight belt, +wetsuit

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
- слов: 23
- ~astrolabe, ~sextant, ~star (star_space), +beacon, +buoy, +chart, +city map, +compass, +gps, +Lighthouse, +log, +map, +radar, +sonar, +star chart, +telescope, ?astrolabe, ?chart, ?compass, ?gps, ?map, ?radar, ?sextant

### SEA HARVEST  `ocean_products`
- правило: Useful things people harvest from the sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~amber, ~coral, ~kelp, ~pearl, ~plankton, ~salt, ~sand, ~seaweed, ~shell, ~sponge (sponge_animal), +fish, !ambergris, !oil (oil_crude)

### SHORE FEATURES  `ocean_zones`
- правило: Features of the ocean and its shoreline
- тип связи: `is_a`, базовая сложность 0.35
- слов: 29
- ~abyssal, ~sandbar, ~undertow, +atoll, +bay, +benthic, +cliff, +cove, +current (current_water), +estuary, +gulf, +inlet, +lagoon, +littoral, +midnight, +pelagic, +reef, +shore, +sunlight, +surf, +tide, +trench, +trenches, +twilight, +wave (wave_water), !bathyal, !shelf (shelf_sea), xepipelagic, xhadal

### SEA MAMMALS  `sea_mammals`
- правило: Mammals that live in the sea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 18
- ~dugong, ~narwhal, +beluga, +blue whale, +dolphin, +humpback, +manatee, +orca, +otter, +porpoise, +sea lion, +seal (seal_animal), +walrus, +whale, ?dolphin, ?manatee, ?otter, ?walrus

### SEA LEGENDS  `sea_myths`
- правило: Creatures and stories from sea legend
- тип связи: `found_in`, базовая сложность 0.4
- слов: 15
- ~davy jones, ~flying dutchman, ~ghost ship, ~hippocampus, ~kraken, ~leviathan, ~mermaid, ~sea monster, ~sea serpent, ~siren, ~triton, ~Whirlpool, ?kraken, ?leviathan, !selkie

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

### FISHING FLEET  `whaling_and_fishing`
- правило: Things used in commercial fishing
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~buoy, ~crate, ~dredge, ~gaff, ~harpoon, ~hold, ~hook (hook_fishing), ~line (line_cord), ~net, ~pot, ~Seine, ~trap, ~trawler, ~winch


## Тема: properties

### BLACK THINGS  `black_things`
- правило: Everyday things that are typically black in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 18
- ~asphalt, ~bat (bat_animal), ~chalkboard, ~coal, ~crow, ~ink, ~licorice, ~oil (oil_motor), ~olive, ~panther, ~piano key, ~pupil, ~raven, ~Shadow, ~soot, ~tire, ~tuxedo, +night

### COLD THINGS  `cold_things`
- правило: Things that are cold by their physical nature
- тип связи: `has_property`, базовая сложность 0.3
- слов: 22
- ~blizzard, ~chill, ~freeze, ~freezer, ~frost, ~glacier, ~hail, ~ice cube, ~iceberg, ~icicle, ~permafrost, ~Popsicle, ~refrigerator, ~sleet, ~slush, ~snowball, ~sorbet, +ice, +ice cream, +snow, ?chill, ?frost

### COLORS  `colors`
- правило: Basic color names used in everyday English
- тип связи: `is_a`, базовая сложность 0.1
- слов: 45
- +beige, +black, +blue, +Brown, +chartreuse, +crimson, +cyan, +gold, +gray, +green (green_color), +indigo, +lilac, +lime, +magenta, +mahogany, +maroon, +navy, +ochre, +olive, +orange (orange_color), +periwinkle, +pink, +purple, +red, +salmon, +silver, +tan, +taupe, +teal, +turquoise, +vermilion, +vermillion, +Violet, +white (white_color), +yellow, ?beige, ?blue, ?crimson, ?indigo, ?magenta, ?navy, ?purple, ?red, ?Violet, ?yellow

### FAST THINGS  `fast_things`
- правило: Things known for moving very fast
- тип связи: `has_property`, базовая сложность 0.35
- слов: 14
- ~arrow, ~bullet, ~cheetah, ~comet, ~falcon, ~hare, ~jet, ~lightning, ~motorcycle, ~rocket, ~sprinter, ~torpedo, +race car, +wind

### GREEN THINGS  `green_things`
- правило: Everyday things that are typically green in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 24
- ~avocado, ~broccoli, ~cactus, ~clover, ~cucumber, ~emerald, ~Fern, ~frog, ~grass, ~jade, ~kale, ~kiwi, ~leaf, ~lettuce, ~lime, ~mint (mint_herb), ~moss, ~pea, ~pickle, ~shamrock, ~spinach, ~turtle, ?lime, ?moss

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
- слов: 22
- ~boiling water, ~campfire, ~candle, ~ember, ~furnace, ~geyser, ~iron (iron_appliance), ~lava, ~magma, ~oven, ~radiator, ~sauna, ~stove, ~torch, ~volcano, +coal, +engine, +fire, +steam, +sun, ?furnace, ?steam

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
- слов: 24
- ~apple (apple_fruit), ~barn, ~beet, ~brick, ~cardinal (cardinal_bird), ~cherry, ~chili (chili_pepper), ~fire truck, ~flame, ~ketchup, ~lipstick, ~lobster, ~radish, ~ruby, ~strawberry, ~tomato, ~valentine, +blood, +rose, +stop sign, ?blood, ?cherry, ?rose, ?tomato

### ROUND THINGS  `round_things`
- правило: Everyday objects whose normal shape is round or circular
- тип связи: `has_property`, базовая сложность 0.3
- слов: 32
- ~apple (apple_fruit), ~bagel, ~ball (ball_sphere), ~balloon, ~bubble, ~button (button_clothing), ~clock, ~coaster, ~coin, ~cookie, ~dial, ~donut, ~globe, ~hoop, ~lens, ~marble (marble_toy), ~moon (moon_space), ~orange (orange_fruit), ~pancake, ~pearl, ~pizza, ~plate (plate_dish), ~tire, ~wheel, ~wreath, +Earth, +ring (ring_circle), ?coin, ?donut, ?globe, ?hoop, ?wheel

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
- слов: 22
- ~blanket, ~cloud, ~cotton, ~cushion, ~dough, ~feather, ~foam, ~fur, ~kitten, ~marshmallow, ~moss, ~pillow, ~sand, ~silk, ~sponge (sponge_cleaning), ~teddy bear, ~velvet, ~wool, ?fur, ?pillow, ?silk, ?velvet

### SQUARE THINGS  `square_things`
- правило: Everyday things shaped like a square
- тип связи: `has_property`, базовая сложность 0.35
- слов: 13
- ~brick, ~checkerboard, ~envelope, ~keyboard key, ~napkin, ~picture frame, ~stamp (stamp_postage), ~sticky note, ~tile, ~waffle, +box, +window, !dice (dice_game)

### STICKY THINGS  `sticky_things`
- правило: Substances that stick to whatever they touch
- тип связи: `has_property`, базовая сложность 0.35
- слов: 25
- ~caramel, ~caulk, ~chewing gum, ~condensed milk, ~cotton candy, ~frosting, ~glue, ~gum (gum_glue), ~honey, ~jam, ~marshmallow, ~molasses, ~paste, ~resin, ~sap, ~slime, ~syrup, ~taffy, ~tape, ~tar, ~wax (wax_substance), ?glue, ?honey, ?tape, !pitch (pitch_tar)

### STRIPED THINGS  `striped_things`
- правило: Things that normally have stripes
- тип связи: `has_property`, базовая сложность 0.4
- слов: 19
- ~awning, ~barber pole, ~bee, ~candy cane, ~crosswalk, ~flag, ~peppermint, ~prison uniform, ~referee shirt, ~ribbon, ~road, ~skunk, ~tiger, ~zebra, ?bee, ?candy cane, ?flag, ?tiger, ?zebra

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
- слов: 20
- ~belt, ~button (button_clothing), ~cheese grater, ~colander, ~donut, ~flute, ~golf course, ~needle (needle_sewing), ~sieve, ~sock, ~sponge (sponge_cleaning), ~swiss, ~swiss cheese, ~waffle, ~whistle, +net, ?colander, ?donut, ?sieve, !straw (straw_tube)

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
- слов: 21
- ~goshawk, ~kestrel, +buzzard, +condor, +eagle, +falcon, +harrier, +hawk, +kite (kite_bird), +merlin, +osprey, +owl, +raven, +vulture, ?eagle, ?falcon, ?harrier, ?hawk, ?osprey, ?owl, ?vulture

### BUTTERFLIES AND MOTHS  `butterflies_and_moths`
- правило: Kinds of butterfly and moth
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +admiral, +buckeye, +cabbage white, +luna moth, +monarch, +painted lady, +skipper, +sphinx moth, +spongy moth, +viceroy, !fritillary, !swallowtail

### CAT BREEDS  `cat_breeds`
- правило: Breeds of domestic cat
- тип связи: `is_a`, базовая сложность 0.35
- слов: 19
- ~abyssinian, ~ragdoll, +bengal, +bombay, +burmese, +calico, +himalayan, +maine coon, +manx, +persian, +russian blue, +siamese, +tabby, ?maine coon, ?persian, ?ragdoll, ?siamese, !birman, !sphynx

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
- слов: 18
- ~andalusian, ~clydesdale, +Arabian, +Morgan, +Mustang, +paint, +pinto, +quarter horse, +shetland, +thoroughbred, ?Arabian, ?clydesdale, ?Mustang, ?thoroughbred, !appaloosa, !friesian, !palomino, !percheron

### LIZARDS  `lizards`
- правило: Kinds of lizard
- тип связи: `is_a`, базовая сложность 0.35
- слов: 17
- ~agama, ~skink, +bearded dragon, +chameleon, +gecko, +gila monster, +horned lizard, +iguana, +komodo dragon, +salamander, ?anole, ?chameleon, ?gecko, ?iguana, ?skink, !anole, !monitor (monitor_lizard)

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
- слов: 21
- ~oriole, +bluebird, +canary, +cardinal (cardinal_bird), +chickadee, +finch, +lark, +mockingbird, +robin, +sparrow, +starling, +swallow (swallow_bird), +thrush, +warbler, +wren, ?finch, ?robin, ?warbler, ?wren, !junco, !nuthatch

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
- слов: 18
- ~bearing, ~bearings, ~bowl, ~deck, ~grind, ~grip tape, ~helmet, ~nose, ~ollie, ~rail, ~ramp, ~trucks, ~wheels, ?deck, ?trucks, !halfpipe, !kickflip, xgriptape

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
- слов: 19
- +Indy 500, +Kentucky Derby, +Masters, +MLB, +MLS, +NBA, +NFL, +NHL, +Olympics, +Stanley Cup, +Super Bowl, +Tour de France, +Wimbledon, +World Cup, +World Series, +wwe, ?MLB, ?NFL, ?NHL

### SPORTS LEGENDS  `sports_legends`
- правило: Athletes remembered across generations
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- ~Navratilova, +Ali, +Chamberlain, +DiMaggio, +Gretzky, +Jordan, +Louis, +Montana, +Nicklaus, +Owens, +Pele, +Robinson, +Ruth, +Thorpe, !Comaneci

### SWIM STROKES  `swimming_strokes`
- правило: Strokes and events in competitive swimming
- тип связи: `is_a`, базовая сложность 0.35
- слов: 16
- +backstroke, +breaststroke, +butterfly, +distance, +dive, +doggy paddle, +freestyle, +medley, +relay, +sprint, +treading, ?backstroke, ?breaststroke, ?butterfly, ?freestyle, ?sidestroke

### TRACK EVENTS  `track_events`
- правило: Events contested in track and field
- тип связи: `is_a`, базовая сложность 0.35
- слов: 20
- +decathlon, +discus, +high jump, +hurdle, +hurdles, +javelin, +long jump, +marathon, +mile, +pole vault, +race walk, +relay, +shot put, +sprint, +steeplechase, +triple jump, ?hurdles, ?relay, ?sprint, ?steeplechase

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
- слов: 24
- ~chalk (chalk_stick), +bead, +brush, +canvas, +charcoal, +clay, +crayon, +easel, +glitter, +glue, +ink, +marker, +paint, +palette, +paper, +pastel, +pencil, +ribbon, +scissors, +sketch, +sketchbook, +stencil, +yarn, ?canvas

### BLADES  `blades`
- правило: Parts of tools that do the cutting
- тип связи: `is_a`, базовая сложность 0.35
- слов: 15
- +axe, +axe head, +blade, +chainsaw, +cutter, +edge, +knife edge, +point (point_tip), +razor, +saw blade, +scalpel, +scissor blade, +sword, +teeth, !tip (tip_point)

### TOOL STORAGE  `boxes_and_cases`
- правило: Things used to store and carry tools
- тип связи: `is_a`, базовая сложность 0.35
- слов: 14
- ~case (case_box), +bag, +belt, +bucket, +cabinet (cabinet_furniture), +caddy, +chest (chest_box), +drawer, +pouch, +rack, +shed, +toolbox, +tray, !pegboard

### CLEANING TOOLS  `cleaning_tools`
- правило: Tools used for cleaning and tidying
- тип связи: `used_in`, базовая сложность 0.25
- слов: 23
- ~scrubber, ~squeegee, +air freshener, +broom, +brush, +bucket, +duster, +dustpan, +lint roller, +mop, +plunger, +rag, +scraper, +sponge (sponge_cleaning), +steam cleaner, +toothbrush, +vacuum, ?broom, ?brush, ?duster, ?dustpan, ?mop, ?vacuum

### CUTTING TOOLS  `cutting_tools`
- правило: Tools used to cut material
- тип связи: `used_in`, базовая сложность 0.3
- слов: 21
- +blade, +box cutter, +chisel, +cleaver, +clipper, +guillotine, +hedge trimmer, +knife, +lawnmower, +machete, +razor, +saw, +scalpel, +scissors, +shears, +wire cutter, ?knife, ?razor, ?saw, ?scalpel, ?scissors

### FASTENERS  `fasteners`
- правило: Small parts used to hold things together
- тип связи: `is_a`, базовая сложность 0.3
- слов: 24
- ~paperclip, ~pin (pin_fastener), +anchor, +belt, +bolt, +bracket, +buckle, +clamp, +clip, +hinge, +hook (hook_fastener), +nail (nail_metal), +rivet, +rope, +screw, +snap, +staple, +tack (tack_pin), +velcro, +washer, +zip tie, +zipper, ?velcro, !nut (nut_metal)

### GARDEN TOOLS  `garden_tools`
- правило: Tools used for gardening and yard work
- тип связи: `used_in`, базовая сложность 0.25
- слов: 28
- ~cultivator, ~edger, ~pruner, ~seeder, ~weeder, +clippers, +gloves, +hoe, +hose, +lawnmower, +leaf blower, +pitchfork, +rake, +shears, +shovel, +spade (spade_tool), +sprinkler, +trowel, +twine, +watering can, +wheelbarrow, ?hoe, ?hose, ?rake, ?shears, ?shovel, ?trowel, xpruners

### HAND TOOLS  `hand_tools`
- правило: Tools held in the hand and used for building or repair work
- тип связи: `is_a`, базовая сложность 0.15
- слов: 25
- ~file (file_tool), ~plane (plane_tool), ~socket (socket_tool), +awl, +chisel, +clamp, +crowbar, +drill (drill_tool), +hammer, +knife, +level, +mallet, +pliers, +ratchet, +sander, +saw, +scraper, +screwdriver, +Square, +stapler, +tape measure, +vise, +wrench, ?screwgun, !punch (punch_tool)

### HARDWARE STORE  `hardware_store`
- правило: What a hardware store keeps in its bins and aisles
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~containers, ~fuels, +blades, +fasteners, +hose, +ladder, +sandpaper

### KITCHEN GADGETS  `kitchen_gadgets`
- правило: Small specialized gadgets used in a kitchen
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~baster, ~mandoline, ~peeler, ~sifter, +bread maker, +can opener, +coffee maker, +corkscrew, +egg slicer, +funnel, +garlic press, +griddle, +melon baller, +pizza cutter, +scoop, +strainer, +thermometer, +timer, !tenderizer, xzester

### MEASURING TOOLS  `measuring_tools`
- правило: Tools used to measure size, weight or amount
- тип связи: `used_in`, базовая сложность 0.3
- слов: 16
- +barometer, +caliper, +compass, +gauge, +level, +measuring cup, +meter, +odometer, +protractor, +ruler, +scale (scale_weigh), +speedometer, +stopwatch, +tape measure, +thermometer, +yardstick

### OFFICE SUPPLIES  `office_supplies`
- правило: Small items kept in an office desk and used for paperwork
- тип связи: `found_in`, базовая сложность 0.15
- слов: 37
- ~paperclips, ~stamp (stamp_tool), ~whiteout, +binder, +calculator, +calendar, +clip, +envelope, +eraser, +folder, +highlighter, +hole punch, +ink, +label, +marker, +notebook, +notepad, +paper, +paper clip, +paperclip, +pen (pen_writing), +pencil, +planner, +post it, +rubber band, +ruler, +scissors, +stapler, +sticky note, +tape, ?binder, ?eraser, ?highlighter, ?marker, ?pencil, ?ruler, ?stapler

### PAINTING SUPPLIES  `painting_supplies`
- правило: Things used to paint a wall or a picture
- тип связи: `used_in`, базовая сложность 0.3
- слов: 20
- +brush, +canvas, +drop cloth, +easel, +ladder, +paint, +palette, +primer, +roller, +smock, +sponge (sponge_cleaning), +spray can, +stencil, +tape, +thinner, +tray, ?brush, ?canvas, ?easel, ?palette

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


## Тема: world_more

### MORE COUNTRIES  `countries_more`
- правило: Countries less often named in lists
- тип связи: `is_a`, базовая сложность 0.4
- слов: 20
- +Albania, +Andorra, +Armenia, +Belarus, +Bhutan, +Cyprus, +Georgia, +Iceland, +Kazakhstan, +Latvia, +Lithuania, +Luxembourg, +Malta, +Moldova, +Monaco, +Mongolia, +Nepal, +Slovenia, +Ukraine, +Uzbekistan

### ISLAND NATIONS  `island_nations`
- правило: Countries made up of islands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 19
- +Bahrain, +Cuba, +Cyprus, +Fiji, +Iceland, +Indonesia, +Jamaica, +Japan, +Madagascar, +Maldives, +Malta, +Mauritius, +Philippines, +Seychelles, +Sri Lanka, ?Cuba, ?Iceland, ?Malta, ?Seychelles

### TROPICAL BIRDS  `tropical_birds`
- правило: Colorful birds of tropical regions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 22
- +bird of paradise, +canary, +cockatoo, +flamingo, +hummingbird, +kingfisher, +parakeet, +parrot, +toucan, ?cockatoo, ?macaw, ?parrot, ?quetzal, ?toucan, !cassowary, !hoopoe, !hornbill, !lorikeet, !macaw, !motmot, !quetzal, !sunbird

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

