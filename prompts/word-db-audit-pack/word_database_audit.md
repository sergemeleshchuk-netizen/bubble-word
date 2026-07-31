# Word Database Audit

Audit source: `база-слов.sqlite`  
Audit time (UTC): 2026-07-31T09:58:17+00:00

## Executive verdict

**The SQLite snapshot is technically healthy, but it is not yet safe as an unattended production source for generating hidden-category four-word levels.**

The file passes SQLite integrity checks and has no foreign-key violations. The exported CSV and Markdown review files are structurally consistent with the database. The main risks are semantic and game-specific: incomplete sense assignment, status contradictions, categories that cannot form a normal quartet, large category overlaps, no explicit quartet/conflict layer, and no populated cultural-risk metadata.

This is a structural and targeted semantic audit. It does not claim that every one of the 17,550 links has received exhaustive native-speaker review.

## What is good

- `PRAGMA integrity_check`: **ok**.
- Foreign-key violations: **0**.
- Inventory matches the supplied summary: **10,005 words, 1,092 categories, 17,550 memberships, 549 senses for 222 words**.
- Membership status counts match the review summary: approved 8,954, alternative 6,032, hard_only 2,503, rejected 61.
- The machine CSV matches the SQLite snapshot field-for-field in the checked identity and scoring fields.
- All categories currently have at least four non-rejected words, so every category can technically produce one quartet if hard_only content is allowed.

## P0 blockers

### 1. The database stores pools, not validated four-word solutions

The game requires exactly four words per hidden category. A raw word-category graph does not guarantee a unique answer. There are **516 category pairs sharing at least four playable words**, involving **526 categories**. This allows a generated set to have two or more defensible category answers.

Required additions:

- reviewed `quartets` and `quartet_words` tables;
- `category_conflicts` / do-not-pair rules;
- pair/group structure metadata for categories such as OPPOSITES;
- a solver that rejects any level with more than one valid partition.

Top overlap examples:

- **JEWELRY STONES** vs **GEMSTONES**: 15 shared words (amethyst | aquamarine | diamond | emerald | garnet | jade | moonstone | onyx | opal | pearl | peridot | ruby | sapphire | topaz | turquoise).
- **BIRDS** vs **FLYING ANIMALS**: 13 shared words (crow | duck | eagle | falcon | goose | hawk | owl | pelican | pigeon | robin | seagull | sparrow | swan).
- **FABRICS** vs **FABRIC TYPES**: 13 shared words (canvas | chiffon | corduroy | cotton | denim | flannel | lace | linen | satin | silk | tweed | velvet | wool).
- **FOOTWEAR** vs **SHOE STYLES**: 13 shared words (boot | clog | flat | heel | loafer | moccasin | oxford | pump | sandal | slipper | sneaker | stiletto | wedge).
- **SCHOOL SUPPLIES** vs **OFFICE SUPPLIES**: 13 shared words (binder | calculator | eraser | folder | highlighter | marker | pen | pencil | planner | ruler | scissors | stapler | tape).
- **ART CLASS** vs **ART SUPPLIES**: 12 shared words (brush | canvas | chalk | clay | glitter | glue | marker | paint | pastel | scissors | sketchbook | stencil).
- **FARM ANIMALS** vs **LIVESTOCK**: 12 shared words (chicken | cow | donkey | duck | goat | horse | mule | ox | pig | rabbit | sheep | turkey).
- **LANGUAGES** vs **NATIONALITIES**: 12 shared words (Chinese | Dutch | French | German | greek | Italian | Japanese | Korean | polish | Russian | spanish | Swedish).
- **PIE INGREDIENTS** vs **BAKING INGREDIENTS**: 12 shared words (butter | chocolate | cinnamon | cream | egg | flour | molasses | raisin | salt | shortening | sugar | vanilla).
- **SCHOOL PEOPLE** vs **SCHOOL JOBS**: 12 shared words (aide | bus driver | coach | counselor | crossing guard | janitor | librarian | nurse | principal | substitute | teacher | tutor).
- **SEAFOOD** vs **FISH**: 12 shared words (anchovy | catfish | cod | halibut | herring | salmon | sardine | snapper | swordfish | tilapia | trout | tuna).
- **ACCESSORIES** vs **FASHION ACCESSORIES**: 11 shared words (belt | bowtie | brooch | cufflinks | gloves | hat | scarf | sunglasses | suspenders | tie | watch).
- **BREAD TYPES** vs **SANDWICH BREADS**: 11 shared words (bagel | ciabatta | croissant | focaccia | pita | roll | rye | sourdough | texas toast | wheat | white).
- **BREAD TYPES** vs **WORLD BREADS**: 11 shared words (baguette | brioche | challah | ciabatta | focaccia | naan | pita | pumpernickel | rye | sourdough | tortilla).
- **CLEANING SUPPLIES** vs **CLEANING TOOLS**: 11 shared words (broom | brush | bucket | duster | dustpan | mop | rag | scrubber | sponge | squeegee | vacuum).
- **CLOTHING ITEMS** vs **BUTTONED THINGS**: 11 shared words (blouse | cardigan | coat | glove | jacket | jeans | overalls | pants | shirt | sweater | vest).
- **FISHING TRIP** vs **FISHING THINGS**: 11 shared words (bait | boat | cooler | hook | line | lure | net | reel | rod | tackle box | waders).
- **FRUITS** vs **FRUIT TREES**: 11 shared words (apple | apricot | banana | cherry | lemon | lime | mango | orange | peach | pear | plum).
- **RIVERS** vs **WORLD RIVERS**: 11 shared words (Amazon | Congo | Danube | Euphrates | Ganges | Nile | Rhine | Seine | Thames | Volga | Yangtze).
- **SPICES AND HERBS** vs **COOKING HERBS**: 11 shared words (basil | chive | cilantro | dill | mint | oregano | parsley | rosemary | sage | tarragon | thyme).

### 2. Incomplete sense assignment

There are **96 memberships across 18 words** that already have multiple senses but still use `sense_id = NULL`. For example, `ring` has jewelry/tree senses, while other links use it as a sound, boxing ring, circus ring, planet ring, and more without a matching sense.

Additionally, **736 high-reuse words** have at least four playable categories across multiple themes but no senses at all. Examples include `bell`, `Charger`, `Jasmine`, `rose`, `siren`, `cricket`, `iris`, `Life`, and `Spirit`.

Required invariant: **if a word has more than one sense, every membership must reference exactly one sense**.

### 3. Missing familiarity is treated as valid data

**26 words have `familiarity_score = NULL`; 20 of their memberships are approved.** Examples include `calfling`, `glyptodon`, `escalivada`, `avgolemono`, `Dreyers`, and `Edys`.

Missing familiarity must fail closed: `candidate` / `review_required`, never `approved`.

### 4. Cultural-risk field is unused

The review brief calls for cultural and ethical risk checks, but **0 memberships have populated `risk_flags`**. At least two clear terminology problems are present: `gypsy moth` should be `spongy moth`, and `Eskimo Pie` is an obsolete brand name replaced by `Edy's Pie`.

## P1 content and scoring problems

### Category pools

- **34 categories** have fewer than four approved+alternative words and cannot make a normal-level quartet.
- **13 categories** have zero approved+alternative words; all usable links are hard_only.
- **276 categories** have fewer than four approved words.
- **249 categories** have no approved words.
- **86 categories** have more than half of all links marked hard_only.
- `04_flags.md` lists only **60** of them and omits **26** qualifying categories, so that review export is incomplete.
- **61 categories** have fewer than twelve non-rejected words, creating high repetition risk.

Categories blocked for normal-level generation:

YOUNG ANIMALS (baby_animal_words_more), BEETLES (beetles), CACTUS AND SUCCULENTS (cactus_and_succulents), CARD TRICKS (card_tricks), FARM BREEDS (cattle_and_farm_breeds), DESERTS (deserts_and_wild_places), CHICKEN BREEDS (farm_poultry_breeds), FRENCH COOKING (french_cooking_terms), FROGS AND TOADS (frogs_and_toads), GEM CUTS (gem_cuts), BYGONE JOBS (historic_jobs), KITCHEN SLANG (kitchen_brigade), KNOTS (knots), LATIN PHRASES (latin_phrases), MOSS & LICHEN (mosses_and_lichens), MUSHROOM TYPES (mushroom_types), TEMPO TERMS (music_tempo_terms), NIGHT SHIFT (night_shift_jobs), HISTORIC TRADES (old_professions), PLACE NAMES (place_names_as_names), POISONOUS PLANTS (poisonous_plants), SAILING TERMS (sailing_terms), SEA LEGENDS (sea_myths), SEAL FAMILY (seals_and_walruses), SIGNALS AND CODES (signals_and_codes), STARTUP WORDS (startup_words), SUPERSTITION THINGS (superstitions), GLOVE BOX (things_in_a_glove_box), KEYCHAIN THINGS (things_on_a_keychain), SMALL CATS (wild_cats_small), WORLD HATS (world_hats), TRADITIONAL FOOTWEAR (world_hats_and_dress), WORLD INSTRUMENTS (world_instruments), WORMS (worms_and_crawlers)

Categories with zero normal words:

YOUNG ANIMALS (baby_animal_words_more), FARM BREEDS (cattle_and_farm_breeds), DESERTS (deserts_and_wild_places), CHICKEN BREEDS (farm_poultry_breeds), FRENCH COOKING (french_cooking_terms), BYGONE JOBS (historic_jobs), KNOTS (knots), LATIN PHRASES (latin_phrases), MUSHROOM TYPES (mushroom_types), TEMPO TERMS (music_tempo_terms), HISTORIC TRADES (old_professions), POISONOUS PLANTS (poisonous_plants), SMALL CATS (wild_cats_small)

### Status contradictions

- **355 hard_only links have `obviousness_score >= 0.80`**.
- **457 hard_only links use words with familiarity >= 0.60**.
- Examples: `xylophone -> MUSICAL INSTRUMENTS`, `key -> KEYCHAIN THINGS`, `camera/e-reader/ATM -> THINGS WITH SCREENS`, common Latin expressions, and famous deserts.
- `fit_score` has almost no discrimination: **17,489 of 17,550 links are exactly 0.97**, with only **10 distinct values**.

The likely root cause is relative ranking of a word's categories against each other. The best category of a rare one-category word can become approved, while an objectively obvious secondary use can become hard_only. Use absolute thresholds first, then relative ranking as a secondary signal.

### Word count reporting

The headline **10,005 words** includes **60 words that are rejected in every category**. The actual non-rejected playable vocabulary is **9,945 words**. The normal-tier vocabulary is **8,345 words**; **1,600 words** are hard-only everywhere.

The supplied multi-category count of 3,456 includes rejected links. Using playable links only, the count is 3,455.

## High-confidence semantic examples

See `semantic_issues.csv` and the workbook sheet `08 Semantic Issues` for the full targeted list. Representative problems:

- WORLD DANCES includes `kabuki`.
- ARCTIC ANIMALS includes `penguin` while the label is Arctic.
- CRUSTACEANS uses a sea-only rule but includes crayfish and pill bug.
- WATERFOWL mixes waterfowl with heron, ibis and egret.
- WORMS includes ringworm and several insect larvae/common names.
- INSECTS includes spider, centipede and tick under a hidden INSECTS label.
- SLEEP ACTIONS includes `wake`.
- BOARD GAMES includes games that do not use a board.
- NATIONAL SYMBOLS lacks country IDs, so arbitrary quartets do not share one precise relation.
- Some action memberships point to noun senses, such as `drill_tool` in BUILDING ACTIONS.

## Schema and display risks

- Proper-noun/casing data is stored at word level, but casing often depends on sense (`apple/Apple`, `turkey/Turkey`, `march/March`, `polish/Polish`). **422 proper-noun-flagged multi-category words have no senses**, and **90 proper nouns are stored entirely lowercase**.
- **8 spelling collision groups** need canonical concept/alias review, including `call sign/callsign`, `paper clip/paperclip`, `tree frog/treefrog`, and `bird bath/birdbath`.
- **105 labels exceed 15 characters** and need real bubble/card UI testing.
- `PRAGMA user_version` is 0; there is no explicit schema/content version in the snapshot.
- All membership provenance is coarse (`seed_manual`) even though status decisions use SWOW/wordfreq logic.
- `generation_runs` contains 0 rows, so generated content cannot yet be reproduced/audited from this snapshot.

## Recommended production model

1. Keep the current normalized word-category graph as the **candidate knowledge layer**.
2. Move ambiguity-sensitive fields to the sense level: `display_text`, `is_proper_noun`, `part_of_speech`, `familiarity_score`.
3. Add canonical concepts and aliases for spelling/trademark variants.
4. Separate independent scores:
   - semantic correctness;
   - sense salience;
   - lexical familiarity;
   - category cohesion;
   - gameplay difficulty;
   - cultural/terminology risk.
5. Add reviewed quartet and conflict tables.
6. Gate exports with automated validations:
   - no approved link with NULL familiarity;
   - no NULL sense_id for multi-sense words;
   - no active normal category with fewer than four normal words;
   - no duplicate alias concepts in one level;
   - no level with multiple valid partitions;
   - no stale/sensitive term without review metadata;
   - no action relation pointing to an incompatible noun sense.
7. Version every snapshot with schema version, content version, Git commit, source hashes, SWOW version, wordfreq version, and review timestamp.

## Suggested acceptance criteria before level generation

- 0 integrity and foreign-key errors.
- 0 approved/alternative links with missing familiarity.
- 0 ambiguous memberships without a sense_id.
- 0 enabled normal categories with fewer than four normal words.
- 100% of generated levels pass the uniqueness solver.
- 100% of production quartets have human/native-speaker review state.
- 100% of terminology-risk flags resolved or explicitly accepted.
- Canonical display text fits the target UI at supported font sizes.

## Files in this audit pack

- `word_database_audit.xlsx`: filterable workbook with all findings.
- `category_pool_audit.csv`: every category and its usable pool.
- `missing_sense_assignments.csv`: exact NULL-sense memberships for already ambiguous words.
- `sense_candidates.csv`: high-reuse words that likely need sense decomposition.
- `null_familiarity.csv`: every membership using a word with missing familiarity.
- `status_conflicts.csv`: hard_only links contradicted by obviousness/familiarity signals.
- `normalization_collisions.csv`: spelling/canonicalization collisions.
- `category_overlap_conflicts.csv`: all category pairs sharing at least four playable words.
- `semantic_issues.csv`: targeted high-confidence semantic/gameplay findings.
- `proper_noun_sense_risks.csv`: word-level proper-noun/casing risks.
- `long_labels.csv`: UI-length candidates.
- `rejected_only_words.csv`: stored words that are not playable anywhere.
- `flags_export_gaps.csv`: categories omitted from the majority-hard section of `04_flags.md`.
