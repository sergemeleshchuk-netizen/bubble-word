# Bubble Level Forge

Level generation tool for **Bubble Associations: Word Game**
(word association puzzle: sort word bubbles into categories).

Test assignment deliverables:

- **Live tool:** https://serge-mel.surge.sh/tool/ — also embedded in section 05
  of the report site, no build step required
- **Report site:** https://serge-mel.surge.sh
- **10 generated levels with difficulty grades:** `levels/`
- **AI workflow write-up:** on the report site, section 03; full log in
  `tool/level-tool/docs/AI_WORKFLOW.md`

## Where the AI actually is

Worth stating plainly, because "AI level generator" would be the wrong summary:

**The tool does not call a model when it builds a level.** Opening the page and
pressing "build" runs a deterministic algorithm over a frozen snapshot of the
content base — no network, no API key, same input always produces the same pack
hash. That is a design decision, not a limitation: difficulty can only be
controlled and defects can only be reproduced if level assembly is deterministic.

**AI is used offline, on the content**, and that work is the bulk of the project:
proposing categories and word pools, splitting polysemous words into senses,
marking relation types and obviousness, and reviewing its own output as a critic.
Prompts, model mistakes and the decisions made about them are logged in
`tool/level-tool/docs/AI_WORKFLOW.md`.

So: **AI generates content; a deterministic algorithm assembles levels from it;
validators prove the result is correct.**

## Where the content comes from

The base has two layers, and they are marked apart in the data (`categories.origin`):

| layer | size | origin |
|---|---|---|
| `bwj_reference` | 5409 categories, ~27 700 links | a fan transcription of the target game's answers (bubblewordjam.org, 1025 levels), imported as a run with its provenance kept |
| `seed` | 1297 categories, ~21 500 links | written for this project: word pools, senses, rules, statuses, register |

Two things follow, and both are enforced rather than promised:

- **Ready-made quadruples from the game are never reused.** A quadruple is a
  level layout, not content; the `REFERENCE_NOVELTY` check rejects a level that
  reproduces one, and the shipped pack is built with that check set to `hard`
  (recorded in `data/final-pack/pack.json` as `reference_novelty`). Sources for
  the import are in `tool/word_content_pipeline/data/runs/run-002-bwj-org/`.
- **The reference layer does contribute categories, and the count is stated
  rather than glossed.** In the shipped pack of 10 levels, 55 of 145 categories
  have a key that also occurs in the game's transcription; the other 90 were
  written for this project. Per-level counts are in `levels/CERTIFICATION.md`,
  column C5. The words inside a borrowed category are re-selected by the
  generator, so no quadruple is a copy — but the category and its pool are the
  original's, and calling the whole pack original would be untrue.

A separate read-only source, `RefBWJ`, exposes the original game's levels as
recorded, for comparison and playtesting. It never feeds generation.

## What the tool does

1. **Assembles levels** from the content base with configurable difficulty:
   number of categories, word rarity, planned traps, meta-bubbles, start layout.
2. **Proves solvability**: every word has exactly one home (global solution
   counter), bubble counts match the board, and a simulated playthrough
   confirms the level finishes within the move limit without dead ends.
   A second simulation plays the level as a player who reads words rather than
   answers — it feeds the difficulty score, it does not gate the level.
3. **Grades difficulty and interest**: a score with a human-readable breakdown
   of contributing factors, calibrated on 199 recorded levels of the original.
4. **Exports JSON** — a game-facing format and a full pipeline artifact.
   Export is blocked while any level fails a hard check.

Solvability of the shipped pack is certified **by a second, independent program**
(`tool/level-tool/scripts/certify_solvability.ts`), which imports nothing from
the tool's core and reads only the shipped JSON. It re-proves uniqueness over a
wider plausibility graph, replays the deal with the real board capacity, and
writes a machine certificate per level. Report: `levels/CERTIFICATION.md`.

## Repository layout

- `site/` - report site sources (deployed to serge-mel.surge.sh)
- `tool/level-tool/` - the web tool (TypeScript, deterministic assembly)
- `tool/word_content_pipeline/` - the content base and its build
  (`scripts/rebuild_all.sh` rebuilds SQLite from the text sources in `data/`)
- `levels/` - generated level packs with their evaluations
- `reference/` - game reference materials: video, scrapes (not committed)

Project working files: `CLAUDE.md`, `rules.md`, `AGENTS.md`, `status.md`
(Claude Code project configuration, kept in the repo intentionally:
the AI workflow is part of the deliverable).

## Known state

`tool/level-tool/docs/AI_WORKFLOW.md` §8 lists what this submission does **not**
have — most importantly, that independent blind-solver runs by a separate AI
session were not performed. The base itself currently fails three
reference-reproduction tests and its integrity check; the causes and the repair
plan are in `status.md`.

`levels/CERTIFICATION.md` has its own "what this does not prove" section, and
`levels/manual-play.json` records how far a human actually played each level:
one of the ten was played by hand, the other nine were only opened and checked
against the pack's start layout.
