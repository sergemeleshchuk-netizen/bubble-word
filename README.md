# Bubble Level Forge

AI-powered level generation tool for **Bubble Associations: Word Game**
(word association puzzle: sort word bubbles into categories).

Test assignment deliverables:

- **Live tool:** (link will appear here)
- **Report site:** https://serge-mel.surge.sh
- **10 generated levels with difficulty grades:** `levels/`
- **AI workflow write-up:** on the report site

## What the tool does

1. **Generates levels**: AI-powered category + word sets with configurable difficulty.
2. **Validates solvability**: every word has exactly one home, bubble counts match,
   no dead ends. Includes a "blind solver" pass: an independent AI solves the level
   without seeing the answers; any mismatch rejects the level.
3. **Grades difficulty**: a score with a human-readable breakdown of contributing factors.
4. **Exports JSON** ready to be loaded into the game.

## Repository layout

- `site/` - report site sources (deployed to serge-mel.surge.sh)
- `tool/` - the web tool itself
- `levels/` - generated levels (JSON)
- `reference/` - game reference materials (not committed)

Project working files: `CLAUDE.md`, `rules.md`, `AGENTS.md`, `status.md`
(Claude Code project configuration, kept in the repo intentionally:
the AI workflow is part of the deliverable).
