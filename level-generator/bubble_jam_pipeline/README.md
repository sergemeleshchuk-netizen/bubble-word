# Bubble Jam Word Graph Pipeline

Production-oriented generator for semantic word groups.

## Sources

- Princeton WordNet / NLTK: noun hyponym groups (`is_a`).
- Wikidata Query Service: curated entity classes via SPARQL.
- ConceptNet API: associative relations such as RelatedTo, AtLocation, UsedFor and PartOf.
- `wordfreq`: Zipf frequency estimates. Its frequency snapshot is based on language data through approximately 2021.

## Important data caveat

`cefr_est` is a game-design heuristic derived from Zipf frequency. It is **not** an official CEFR annotation. Groups remain candidates until editorial review or playtest validation.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run WordNet first

```bash
python src/pipeline.py --wordnet-only
```

## Run all online sources

```bash
python src/pipeline.py
```

Outputs:

- `output/groups.csv`
- `output/words.csv`
- `output/conflicts.csv`
- `output/safe_groups.csv`
- `output/bubble_jam_database.xlsx`

## Recommended production gate

1. Keep `SAFE_CANDIDATE` only.
2. Exclude a word from two groups in the same level.
3. Human-review all groups with `risk_score >= 35`.
4. A/B-test perceived clarity and failure reason before shipping large batches.
5. Keep source IDs and URLs in the shipped content repository for auditability.
