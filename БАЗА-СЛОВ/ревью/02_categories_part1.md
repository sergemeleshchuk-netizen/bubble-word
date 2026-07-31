# Категории, часть 1 из 4

Знаки статуса: `+` approved, `~` alternative (ловушка), `!` hard_only, `x` rejected.
В скобках после слова — значение, если у слова разведены значения.


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

### CALLIGRAPHY  `calligraphy`
- правило: A term belonging to fine handwriting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~penmanship, +cursive, +flourish, +italic, +lettering

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

### POTTERY STUDIO  `pottery_studio`
- правило: A material or ware made in a pottery studio
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- +ceramic, +earthenware, +terracotta, +urn, ?kilnfire

### POTTERY WORDS  `pottery_words`
- правило: Things used in making pottery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~bowl, ~clay, ~fire, ~glaze, ~kiln, ~mold (mold_form), ~plaster, ~pot, ~sculpt, ~slip, ~tile, ~vase, ~wheel, !trim (trim_cut)

### SCULPTORS STUDIO  `sculptors_studio`
- правило: Something a sculptor makes or mounts work on
- тип связи: `used_in`, базовая сложность 0.65
- слов: 4
- +figurine, +mould, +pedestal, +plinth

### SCULPTURE MATERIALS  `sculpture_materials`
- правило: Materials sculptors carve or cast
- тип связи: `made_of`, базовая сложность 0.35
- слов: 14
- ~soapstone, +bronze, +clay, +concrete, +glass, +granite, +ice, +marble (marble_stone), +metal, +plaster, +sand, +stone, +wax (wax_substance), +wood

### STREET ART  `street_art`
- правило: A form or technique of street art
- тип связи: `is_a`, базовая сложность 0.55
- слов: 4
- +graffiti, +mural, +stencil, +tagging

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
- слов: 34
- +account, +allowance, +bank (bank_finance), +bill (bill_money), +bonus, +budget, +capital (capital_money), +cash, +cent, +change, +check (check_payment), +coin, +credit, +debit, +debt, +deposit, +dime, +dollar, +euro, +fee, +interest, +invoice, +loan, +quarter (quarter_coin), +receipt, +refund, +rent, +salary, +savings, +tax, +teller, +tip (tip_money), +wage, +wallet

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

### TICKETS AND PASSES  `tickets_and_passes`
- правило: A word belonging to paying to enter or travel
- тип связи: `associated_with`, базовая сложность 0.45
- слов: 6
- +entry, +fare, +pass, +receipt, +stub, +voucher

### TRADING FLOOR  `trading_floor`
- правило: A term used trading shares
- тип связи: `used_in`, базовая сложность 0.65
- слов: 5
- +broker, +bullish, +dividend, +portfolio, +ticker


## Тема: food

### ASIAN DISHES  `asian_dishes`
- правило: Dishes from East and Southeast Asian cuisines eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 20
- ~bibimbap, ~satay, ~tempura, ~wonton, +chow mein, +curry, +dim sum, +dumpling, +egg roll, +fried rice, +kimchi, +lo mein, +miso soup, +pad thai, +pho, +ramen, +sashimi, +spring roll, +sushi, +teriyaki

### BAKED GOODS  `baked_goods`
- правило: Something baked from dough or batter in an oven
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +bagel, +bread, +cake, +cookie, +croissant, +donut, +muffin, +pie

### BAKING INGREDIENTS  `baking_ingredients`
- правило: Ingredients commonly used to bake cakes, bread or cookies
- тип связи: `used_in`, базовая сложность 0.25
- слов: 25
- ~oil (oil_cooking), +almond, +baking powder, +baking soda, +butter, +buttermilk, +chocolate, +cinnamon, +cocoa, +cream (cream_dairy), +egg, +flour, +frosting, +honey, +icing, +milk, +molasses, +oat, +raisin, +salt, +shortening, +sugar, +syrup, +vanilla, +yeast

### BARBECUE  `barbecue`
- правило: Something you cook with or over at a barbecue
- тип связи: `used_in`, базовая сложность 0.35
- слов: 6
- +burger, +charcoal, +grill, +ribs, +smoke, +tongs

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
- слов: 28
- +bacon, +bagel, +biscuit, +bread, +cereal, +coffee cake, +croissant, +danish, +doughnut, +egg, +french toast, +granola, +grits, +ham, +hash brown, +jam, +milk, +muffin, +oatmeal, +omelet, +pancake, +porridge, +rice, +sausage, +scone, +toast (toast_bread), +waffle, +yogurt

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

### EVERYDAY DRINKS  `everyday_drinks`
- правило: A common non alcoholic drink
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +cocoa, +coffee, +juice, +lemonade, +milk, +smoothie, +soda, +tea

### DRIVE THRU  `fast_food_items`
- правило: Items ordered at an American fast food counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 20
- ~quesadilla, +biscuit, +burger, +burrito, +chicken sandwich, +chili (chili_dish), +corn dog, +fries, +hot dog, +milkshake, +mozzarella stick, +nugget, +onion ring, +pizza, +slider, +soda, +sub, +sundae, +taco, +wrap

### FOOD GROUPS  `food_groups`
- правило: One of the food groups a balanced diet is divided into
- тип связи: `member_of_set`, базовая сложность 0.3
- слов: 6
- +dairy, +fruit, +grains, +meat, +protein, +vegetables

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

### IN A SALAD  `in_a_salad`
- правило: An ingredient tossed into a green salad
- тип связи: `used_in`, базовая сложность 0.3
- слов: 6
- ~croutons, +cucumber, +dressing, +lettuce, +olives, +tomato

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

### LUNCH MENU  `lunch_menu`
- правило: A quick hot dish ordered for lunch
- тип связи: `is_a`, базовая сложность 0.2
- слов: 8
- +burger, +fries, +hotdog, +pizza, +salad, +sandwich, +steak, +taco

### MEALS OF THE DAY  `meals_of_the_day`
- правило: A meal or course eaten at a set time of day
- тип связи: `member_of_set`, базовая сложность 0.2
- слов: 7
- +breakfast, +brunch, +dessert, +dinner, +lunch, +snack, +supper

### MEATS  `meats`
- правило: Kinds of meat sold at an American butcher counter
- тип связи: `is_a`, базовая сложность 0.2
- слов: 25
- ~pastrami, ~turkey (turkey_meat), +bacon, +beef, +bologna, +brisket, +chicken, +chop, +ground beef, +ham, +hot dog, +jerky, +lamb, +liver, +meatball, +pepperoni, +pork, +ribs, +roast, +salami, +sausage, +steak, +veal, +venison, !duck (duck_meat)

### MEXICAN DISHES  `mexican_dishes`
- правило: Dishes from Mexican cuisine widely eaten in the United States
- тип связи: `is_a`, базовая сложность 0.3
- слов: 21
- ~carnitas, ~churro, ~empanada, ~fajita, ~flan, ~horchata, ~pozole, ~quesadilla, ~tostada, +burrito, +enchilada, +guacamole, +nacho, +queso, +salsa, +taco, +tamale, +tortilla, !elote, !mole (mole_sauce), xchile relleno

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
- слов: 19
- ~penne, +angel hair, +gnocchi, +lasagna, +linguine, +macaroni, +noodle, +ravioli, +shells, +spaghetti, !cannelloni, !farfalle, !fettuccine, !orzo, !rigatoni, !tortellini, !vermicelli, !ziti, xrotini

### PASTRIES  `pastries`
- правило: A small sweet baked pastry sold in a bakery
- тип связи: `is_a`, базовая сложность 0.35
- слов: 8
- +biscuit, +croissant, +cupcake, +donut, +eclair, +muffin, +scone, +tart

### PICNIC  `picnic`
- правило: Something you pack or spread out for a picnic
- тип связи: `used_in`, базовая сложность 0.3
- слов: 7
- +basket, +blanket, +cooler, +hamper, +lemonade, +sandwich, +thermos

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

### RESTAURANT COURSES  `restaurant_courses`
- правило: A course listed in order on a restaurant menu
- тип связи: `member_of_set`, базовая сложность 0.35
- слов: 6
- +appetizer, +dessert, +entree, +salad, +soup, +starter

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

### SALTY SNACKS  `salty_snacks`
- правило: A salty snack eaten from a packet or bowl
- тип связи: `is_a`, базовая сложность 0.3
- слов: 6
- +chips, +crackers, +nachos, +peanut, +popcorn, +pretzel

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

### SWEETS  `sweets`
- правило: A sweet treat eaten as a snack
- тип связи: `is_a`, базовая сложность 0.2
- слов: 7
- +brownie, +candy, +caramel, +cookie, +fudge, +lollipop, +toffee

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
- слов: 26
- +artichoke, +asparagus, +bean, +beet, +broccoli, +cabbage, +carrot, +cauliflower, +celery, +corn, +cucumber, +eggplant, +kale, +leek, +lettuce, +onion, +parsnip, +pea, +peppers, +potato, +radish, +spinach, +squash (squash_vegetable), +tomato, +turnip, +zucchini


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
- слов: 22
- +backpack, +bug spray, +camp chair, +campfire, +canteen, +compass, +cooler, +firewood, +first aid kit, +flashlight, +hatchet, +lantern, +map, +marshmallow, +matches, +mess kit, +rope, +sleeping bag, +stove, +tarp, +tent, +thermos

### CANDLE MAKING  `candle_making`
- правило: A word belonging to making candles
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +paraffin, +scented, +taper, +wick

### CARD SUITS  `card_suits`
- правило: One of the four suits in a deck of playing cards
- тип связи: `member_of_set`, базовая сложность 0.25
- слов: 4
- +clubs, +diamonds, +hearts, +spades

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

### GARDENING WORK  `gardening_work`
- правило: A task or tool belonging to working a garden
- тип связи: `used_in`, базовая сложность 0.35
- слов: 7
- ~trowel, +compost, +pruning, +seedlings, +soil, +watering, +weeding

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

### SCRAPBOOKING  `scrapbooking`
- правило: A material or keepsake used making a scrapbook
- тип связи: `used_in`, базовая сложность 0.6
- слов: 4
- +cutouts, +keepsake, +laminate, +stickers

### GAMING SETUP  `video_gaming`
- правило: Things in a video gaming setup
- тип связи: `used_in`, базовая сложность 0.3
- слов: 14
- ~mouse (mouse_computer), ~mousepad, +cable, +cartridge, +chair, +console, +controller, +disc, +headset, +keyboard (keyboard_computer), +memory card, +microphone, +monitor (monitor_screen), +webcam


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
- ~Tinkerbell, +Aladdin, +Anna, +Ariel, +Bambi, +Belle, +buzz, +Cinderella, +Dumbo, +Elsa, +Jasmine (jasmine_disney), +Moana, +Mulan, +Nemo, +Peter Pan, +Pinocchio, +Pocahontas, +Rapunzel, +Simba, +Snow White

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

### HERO HQ  `hero_hq`
- правило: A word belonging to comic book superheroes
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +catchphrase, +nemesis, +sidekick, +vigilante

### KINDS OF BOOKS  `kinds_of_books`
- правило: A kind of book classed by how it is written
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +biography, +essay, +fable, +fiction, +memoir, +novel, +poetry

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

### NEWSROOM  `newsroom`
- правило: A person or item of a working newsroom
- тип связи: `found_in`, базовая сложность 0.55
- слов: 5
- +byline, +columnist, +newsflash, +reporter, +tabloid

### NURSERY RHYMES  `nursery_rhymes`
- правило: Nursery rhymes American children learn
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Humpty Dumpty, ~Itsy Bitsy Spider, +Baa Baa Black Sheep, +Jack and Jill, +Little Bo Peep, +London Bridge, +Mary Had a Little Lamb, +Old MacDonald, +Row Your Boat, +Three Blind Mice, +Twinkle Twinkle, !Hickory Dickory Dock

### RADIO STATION  `radio_station`
- правило: A term belonging to radio broadcasting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- +airwaves, +broadcaster, +static, +transmitter

### RADIO WORDS  `radio_words`
- правило: Things and roles in radio broadcasting
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~station (station_place), +antenna, +broadcast, +call sign, +dial, +DJ, +frequency, +jingle, +playlist, +static, +studio, +transmitter, +tuner, !airwave, !host (host_presenter)

### RETRO MUSIC  `retro_music`
- правило: A way music was played or carried before streaming
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +mixtape, +stereo, +vinyl, +walkman

### SHAKESPEARE PLAYS  `shakespeare_plays`
- правило: Plays written by Shakespeare
- тип связи: `is_a`, базовая сложность 0.4
- слов: 14
- +As You Like It, +Hamlet, +Julius Caesar, +King Lear, +Macbeth, +Merchant of Venice, +Midsummer Night, +Much Ado, +othello, +Richard III, +Romeo and Juliet, +Taming of the Shrew, +Tempest, +Twelfth Night

### SPY MISSION  `spy_mission`
- правило: A trick or item used by a spy
- тип связи: `used_in`, базовая сложность 0.6
- слов: 5
- +alias, +decoy, +dossier, +infiltrate, +wiretap

### SUPERHEROES  `superheroes`
- правило: Comic book superheroes most people can name
- тип связи: `is_a`, базовая сложность 0.25
- слов: 18
- +Ant Man, +Aquaman, +Batman, +Black Widow, +Captain America, +Daredevil, +flash, +Green Lantern, +Hulk, +Iron Man, +robin, +Spiderman, +storm, +Supergirl, +Superman, +Thor, +wolverine, +Wonder Woman

### THE HEIST  `the_heist`
- правило: A word belonging to robbing a place in a film
- тип связи: `associated_with`, базовая сложность 0.55
- слов: 4
- +getaway, +heist, +lookout, +loot

### TV GENRES  `tv_genres`
- правило: Kinds of television program
- тип связи: `is_a`, базовая сложность 0.3
- слов: 15
- +cartoon, +cooking show, +crime show, +documentary, +drama, +game show, +mini series, +news, +reality, +sitcom, +soap opera, +sports, +talent show, +talk show, +variety show


## Тема: medicine

### AT THE DENTIST  `at_the_dentist`
- правило: Something a dentist fits, treats or hands out
- тип связи: `found_in`, базовая сложность 0.45
- слов: 5
- +braces, +dentures, +floss, +fluoride, +toothache

### AT THE HOSPITAL  `at_the_hospital`
- правило: Someone or something found in a hospital
- тип связи: `found_in`, базовая сложность 0.3
- слов: 8
- +bandage, +clinic, +hospital, +medicine, +nurse, +patient, +stethoscope, +ward

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
- +ambulance, +code, +CPR, +defibrillator, +dispatcher, +evacuation, +hotline, +oxygen, +paramedic, +rescue, +response, +siren (siren_device), +stretcher, +trauma, +triage

### FEELING SICK  `feeling_sick`
- правило: A symptom or minor illness a person complains of
- тип связи: `associated_with`, базовая сложность 0.3
- слов: 7
- +chills, +cold (cold_illness), +cough, +fever, +flu, +headache, +sneeze

### FIRST AID  `first_aid`
- правило: Things kept in a first aid kit
- тип связи: `used_in`, базовая сложность 0.25
- слов: 18
- +antiseptic, +aspirin, +bandage, +burn cream, +cotton ball, +eye wash, +gauze, +gloves, +ice pack, +ointment, +scissors, +sling, +splint, +tape, +thermometer, +tourniquet, +tweezers, +wipe

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

### KINDS OF DOCTORS  `kinds_of_doctors`
- правило: A doctor named for the field they specialise in
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +allergist, +cardiologist, +dentist, +dietitian, +pediatrician, +surgeon

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

### MEDICINES  `medicines`
- правило: A form in which medicine is given to a patient
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +antibiotic, +injection, +insulin, +ointment, +pill, +syrup, +vaccine

### NUTRIENTS  `nutrients`
- правило: A nutrient the body needs from food
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +calcium, +fiber, +iron (iron_metal), +magnesium, +protein, +zinc

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
- слов: 18
- ~jetlag, ~sleepwalk, +alarm, +apnea, +bedtime, +doze, +dream, +drowsy, +insomnia, +lullaby, +mattress, +nap, +nightmare, +pillow, +rest (rest_sleep), +slumber, +snore, +yawn

### SUPPLEMENTS  `supplements`
- правило: A substance sold as a dietary or beauty supplement
- тип связи: `is_a`, базовая сложность 0.5
- слов: 6
- +biotin, +collagen, +keratin, +probiotic, +vitamin, +zinc

### THERAPY WORDS  `therapy_words`
- правило: Words used in physical and mental therapy
- тип связи: `found_in`, базовая сложность 0.4
- слов: 14
- ~appointment, ~brace, ~counselor, ~crutch, ~exercise, ~massage, ~progress, ~recovery, ~rehab, ~session, ~stretch, ~walker, +goal, +treatment

### VET CLINIC  `vet_clinic`
- правило: A procedure or item used treating animals
- тип связи: `used_in`, базовая сложность 0.55
- слов: 4
- ~neutering, +checkup, +microchip, +muzzle

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

### WELLNESS  `wellness`
- правило: A practice people take up to feel healthier
- тип связи: `is_a`, базовая сложность 0.45
- слов: 6
- +balance, +detox, +diet, +hydration, +meditation, +yoga


## Тема: misc

### GLOVE BOX  `things_in_a_glove_box`
- правило: Things kept in a car glove compartment
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~flashlight, ~ice scraper, ~manual, ~napkins, ~registration, ~sunglasses, ~tire gauge, ~tissues, +insurance, +map, !Charger (charger_device), !gum (gum_candy), !pen (pen_writing)

### PURSE THINGS  `things_in_a_purse`
- правило: Things carried in a purse
- тип связи: `found_in`, базовая сложность 0.3
- слов: 15
- ~hairbrush, +Charger (charger_device), +hand sanitizer, +keys, +lipstick, +mirror, +pen (pen_writing), +phone, +planner, +receipt, +snack, +sunglasses, +tissue (tissue_paper), +wallet, !gum (gum_candy)

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
- ~alarm, ~bell (bell_object), ~bicycle bell, ~buzzer, ~cash register, ~chime, ~church bell, ~clock, ~dinner bell, ~doorbell, ~timer, +phone

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

### GREEK MYTHS  `greek_myths`
- правило: A creature or place from Greek mythology
- тип связи: `found_in`, базовая сложность 0.55
- слов: 5
- +centaur, +cyclops, +minotaur, +Olympus, +Titan

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
- ~basilisk, ~manticore, +banshee, +cerberus, +chimera, +cyclops, +gorgon, +harpy, +hydra, +kraken, +medusa, +minotaur, +sphinx, !siren (siren_myth)

### NORSE GODS  `norse_gods`
- правило: Gods of Norse mythology
- тип связи: `is_a`, базовая сложность 0.35
- слов: 12
- ~Balder, ~Frigg, ~Heimdall, ~Vidar, +Freya, +Hel, +Loki, +Odin, +Thor, +Tyr, !Njord, xIdun

### POTIONS CLASS  `potions_class`
- правило: A word belonging to brewing magic potions
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- +antidote, +bubbling, +concoction, +elixir, +tincture, +vial

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

### WIZARD TOWER  `wizard_tower`
- правило: A word belonging to wizards and spellcasting
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 4
- ~grimoire, +conjure, +enchanted, +incantation

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


## Тема: ocean

### AT THE HARBOR  `at_the_harbor`
- правило: A structure or vessel found in a harbour
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- +anchor, +dock, +ferry, +Lighthouse, +pier, +port

### CORAL REEF  `coral_reef`
- правило: Things found on a coral reef
- тип связи: `found_in`, базовая сложность 0.35
- слов: 15
- ~angelfish, ~clownfish, ~parrotfish, ~sponge (sponge_animal), +algae, +anemone, +coral, +eel, +grouper, +jellyfish, +reef shark, +seahorse, +starfish, +turtle, +urchin

### DEEP SEA  `deep_sea`
- правило: Things found in the deep ocean
- тип связи: `found_in`, базовая сложность 0.4
- слов: 13
- ~abyss, ~darkness, ~lantern fish, ~pressure, ~sediment, ~squid, ~submarine, ~trench, ~tube worm, ~vent, ~whale fall, ?viperfish, !anglerfish

### DIVING GEAR  `diving_gear`
- правило: Equipment used for scuba diving and snorkeling
- тип связи: `used_in`, базовая сложность 0.35
- слов: 15
- ~hood (hood_garment), +buoy, +compass, +dive knife, +fins, +flashlight, +flipper, +gauge, +gloves, +mask, +regulator, +snorkel, +tank (tank_container), +weight belt, +wetsuit

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
- слов: 14
- ~astrolabe, ~sextant, ~star (star_space), +beacon, +buoy, +chart, +compass, +gps, +Lighthouse, +log, +map, +radar, +sonar, +telescope

### OCEAN FLOOR  `ocean_floor`
- правило: Something resting or growing on the ocean floor
- тип связи: `found_in`, базовая сложность 0.4
- слов: 6
- +anchor, +coral, +reef, +seaweed, +shipwreck, +sponge (sponge_animal)

### SEA HARVEST  `ocean_products`
- правило: Useful things people harvest from the sea
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~amber, ~coral, ~kelp, ~pearl, ~plankton, ~salt, ~sand, ~seaweed, ~shell, ~sponge (sponge_animal), +fish, !ambergris, !oil (oil_crude)

### SHORE FEATURES  `ocean_zones`
- правило: Features of the ocean and its shoreline
- тип связи: `is_a`, базовая сложность 0.35
- слов: 18
- ~sandbar, ~undertow, +atoll, +bay, +cliff, +cove, +current (current_water), +estuary, +gulf, +inlet, +lagoon, +reef, +shore, +surf, +tide, +trench, +wave (wave_water), !shelf (shelf_sea)

### SEA MAMMALS  `sea_mammals`
- правило: Mammals that live in the sea
- тип связи: `is_a`, базовая сложность 0.3
- слов: 14
- ~dugong, ~narwhal, +beluga, +blue whale, +dolphin, +humpback, +manatee, +orca, +otter, +porpoise, +sea lion, +seal (seal_animal), +walrus, +whale

### SEA LEGENDS  `sea_myths`
- правило: Creatures and stories from sea legend
- тип связи: `found_in`, базовая сложность 0.4
- слов: 11
- ~davy jones, ~flying dutchman, ~ghost ship, ~kraken, ~leviathan, ~mermaid, ~sea monster, ~sea serpent, ~siren (siren_myth), ~triton, ~Whirlpool

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

### SET SAIL  `set_sail`
- правило: A part of a sailing boat above the deck
- тип связи: `part_of`, базовая сложность 0.6
- слов: 4
- +helm, +jib, +mast, +spinnaker

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

### SUBMARINE DUTY  `submarine_duty`
- правило: A word belonging to serving aboard a submarine
- тип связи: `associated_with`, базовая сложность 0.65
- слов: 4
- +ballast, +nautical, +seabed, +submerge

### WHALE WATCH  `whale_watch`
- правило: A word belonging to whales and watching them
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- ~baleen, ~blowhole, ~narwhal, +breaching, +krill

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
- ~alarm, ~bell (bell_object), ~chainsaw, ~drum, ~explosion, ~firework, ~gunshot, ~horn (horn_sound), ~jackhammer, ~jet, ~motorcycle, ~siren (siren_device), ~speaker, ~thunder, ~whistle, +crowd

### QUIET THINGS  `quiet_things`
- правило: Things that make almost no sound
- тип связи: `has_property`, базовая сложность 0.4
- слов: 14
- ~breath, ~breeze, ~cat, ~cloud, ~feather, ~library, ~moth, ~Shadow, ~silk, ~sleep, ~snow, ~tiptoe, ~whisper, !mouse (mouse_animal)

### RED THINGS  `red_things`
- правило: Everyday things that are typically red in color
- тип связи: `has_property`, базовая сложность 0.3
- слов: 20
- ~apple (apple_fruit), ~barn, ~beet, ~brick, ~cardinal (cardinal_bird), ~cherry, ~chili (chili_pepper), ~fire truck, ~flame, ~ketchup, ~lipstick, ~lobster, ~radish, ~rose (rose_flower), ~ruby, ~strawberry, ~tomato, ~valentine, +blood, +stop sign

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
- ~bell (bell_object), ~hymnal, +aisle, +altar, +candle, +chalice, +choir, +cross, +font, +icon, +incense, +offering plate, +organ (organ_music), +pew, +pulpit, +robe, +stained glass, +steeple

### AFTERLIFE WORDS  `heaven_and_afterlife`
- правило: Words about what religions say comes after death
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- ~ancestor, ~angel, ~eternity, ~heaven, ~immortality, ~judgment, ~nirvana, ~paradise, ~reincarnation, ~resurrection, ~salvation, ~Spirit (spirit_soul), +soul

### MONASTERY THINGS  `monastery_life`
- правило: Things found in a monastery
- тип связи: `found_in`, базовая сложность 0.45
- слов: 14
- ~abbot, ~bell (bell_object), ~chapel, ~cloister, ~courtyard, ~garden, ~library, ~manuscript, ~robe, ~silence, ~vow, !cell (cell_room), !refectory, !scriptorium

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


## Тема: sports_world

### ARCHERY WORDS  `archery_words`
- правило: Words used in archery
- тип связи: `found_in`, базовая сложность 0.4
- слов: 17
- ~bowstring, ~nock, ~range (range_shooting), +aim, +Archer, +arm guard, +arrow, +bow (bow_weapon), +bullseye, +draw, +quiver, +release, +shaft, +sight, +string, +Target, !fletching

### AT THE DOJO  `at_the_dojo`
- правило: A martial art or practice found in a dojo
- тип связи: `found_in`, базовая сложность 0.6
- слов: 6
- ~headlock, ~kendo, ~tatami, +grappling, +sparring, +sumo

### BOWLING WORDS  `bowling_words`
- правило: Words used in bowling
- тип связи: `found_in`, базовая сложность 0.35
- слов: 14
- ~ball (ball_sphere), ~pin (pin_bowling), ~strike (strike_bowling), +alley, +approach, +foul line, +frame, +gutter, +lane, +rack, +score sheet, +spare, +split, !turkey (turkey_bowling)

### BOXING WORDS  `boxing_words`
- правило: Words used in a boxing match
- тип связи: `found_in`, базовая сложность 0.35
- слов: 16
- ~bell (bell_object), ~hook (hook_boxing), ~round (round_stage), +belt, +bout, +clinch, +corner, +decision, +glove, +jab, +knockout, +referee, +ring (ring_arena), +southpaw, +uppercut, xcutman

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

### RODEO  `rodeo`
- правило: A person, animal or event of a rodeo
- тип связи: `found_in`, базовая сложность 0.6
- слов: 5
- +bronco, +cowgirl, +lasso, +stampede, +Wrangler

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

### GARDEN SHED  `garden_shed`
- правило: A tool or material kept in a garden shed
- тип связи: `found_in`, базовая сложность 0.5
- слов: 4
- +mulch, +spade (spade_tool), +trellis, +wheelbarrow

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

### HANDYMAN  `handyman`
- правило: A tool or material a handyman carries
- тип связи: `used_in`, базовая сложность 0.5
- слов: 4
- ~caulk, ~stepladder, ~toolbelt, +crowbar

### HARDWARE STORE  `hardware_store`
- правило: What a hardware store keeps in its bins and aisles
- тип связи: `associated_with`, базовая сложность 0.5
- слов: 7
- ~containers, ~fuels, +blades, +fasteners, +hose, +ladder, +sandpaper

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
- слов: 26
- ~stamp (stamp_tool), ~whiteout, +binder, +calculator, +calendar, +clip, +envelope, +eraser, +folder, +highlighter, +hole punch, +ink, +label, +marker, +notepad, +paper, +paper clip, +pen (pen_writing), +pencil, +planner, +rubber band, +ruler, +scissors, +stapler, +sticky note, +tape

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
- слов: 21
- ~foot (foot_measure), +acre, +centimeter, +cup, +fathom, +gallon, +gram, +inch, +kilometer, +liter, +meter, +mil, +mile, +ounce, +pint, +pound (pound_weight), +quart, +tablespoon, +teaspoon, +ton, +yard (yard_measure)

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
- тип связи: `used_in`, базовая сложность 0.4
- слов: 13
- ~bolt, ~chisel, ~dent, ~horseshoe, ~nail (nail_metal), ~Peg, ~rivet, ~spike, ~stake, ~tack (tack_pin), ~tent stake, ~wedge, !post (post_pole)

### THINGS WITH HANDLES  `things_with_handles`
- правило: Everyday objects gripped by a handle
- тип связи: `has_property`, базовая сложность 0.35
- слов: 18
- ~axe, ~basket, ~briefcase, ~broom, ~bucket, ~drawer, ~hammer, ~kettle, ~knife, ~mug, ~pan, ~pitcher (pitcher_jug), ~purse, ~racket, ~shovel, ~suitcase, ~umbrella, +door

### TUBES  `tubes`
- правило: A hollow tube that something flows through
- тип связи: `is_a`, базовая сложность 0.4
- слов: 7
- +chute, +duct, +funnel, +hose, +nozzle, +pipe (pipe_tube), +straw (straw_tube)

### UNDER LOCK  `under_lock`
- правило: Something used to lock things away or guard them
- тип связи: `used_for`, базовая сложность 0.35
- слов: 7
- +alarm, +code, +key (key_lock), +lock, +padlock, +safe, +vault

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

### HIGHLANDS  `highlands`
- правило: A word belonging to the Scottish Highlands
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 5
- +bagpipes, +haggis, +kilt, +loch, +tartan

### ISLAND LUAU  `island_luau`
- правило: A word belonging to a Hawaiian island party
- тип связи: `associated_with`, базовая сложность 0.6
- слов: 6
- ~luau, +aloha, +hula, +lei, +tiki, +ukulele

### ISLAND NATIONS  `island_nations`
- правило: Countries made up of islands
- тип связи: `is_a`, базовая сложность 0.45
- слов: 15
- +Bahrain, +Cuba, +Cyprus, +Fiji, +Iceland, +Indonesia, +Jamaica, +Japan, +Madagascar, +Maldives, +Malta, +Mauritius, +Philippines, +Seychelles, +Sri Lanka

### TEA CEREMONY  `tea_ceremony`
- правило: A vessel, leaf or step of making tea properly
- тип связи: `used_in`, базовая сложность 0.55
- слов: 5
- ~infuser, ~teahouse, +darjeeling, +steep, +teapot

### TROPICAL BIRDS  `tropical_birds`
- правило: Colorful birds of tropical regions
- тип связи: `is_a`, базовая сложность 0.4
- слов: 13
- +bird of paradise, +cockatoo, +flamingo, +hummingbird, +kingfisher, +parrot, +toucan, !hornbill, !lorikeet, !macaw, !motmot, !quetzal, !sunbird

### TROPICAL FLOWERS  `tropical_flowers`
- правило: Flowers that grow in tropical places
- тип связи: `is_a`, базовая сложность 0.4
- слов: 12
- +bird of paradise, +ginger flower, +hibiscus, +Jasmine (jasmine_flower), +lotus, +orchid, !anthurium, !bougainvillea, !frangipani, !heliconia, !plumeria, !protea

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
- ~kabaddi, +badminton, +bandy, +cricket (cricket_sport), +curling, +futsal, +handball, +hurling, +netball, +rugby, +sumo, +table tennis, !pelota, xsepak takraw

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

