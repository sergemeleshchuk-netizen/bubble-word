/**
 * Прогон модификаторов прототипа по настоящему блоку уровней.
 *
 *   node scripts/check_playable_modifiers.ts
 *
 * Тесты гоняют модификаторы на синтетическом уровне. Здесь важно другое: что
 * настоящий контент даёт им материал — есть что пилить на половинки, цепь
 * находит собираемую по одну сторону категорию, лимит ходов не уезжает.
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { MODIFIERS, buildSetup } from '../web/src/core/playableModifiers.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const block = generateBlock({ snapshot, config: DEFAULT_BLOCK_CONFIG, scoring });
// тот же лексикон, что передаёт App: фрагменты половинок сверяются с базой
const lexicon = new Set(snapshot.words.map((w) => w.n.toLowerCase()));
let problems = 0;

for (const level of block.levels) {
  const spec = level.spec;
  const cells: string[] = [];
  for (const { id } of MODIFIERS) {
    if (id === 'none') continue;
    const setup = buildSetup(spec, id, lexicon);
    const all = [...setup.board, ...setup.queue];
    if (id === 'halves') {
      const pairs = new Set(all.filter((b) => b.kind === 'half').map((b) => b.pair!.id));
      if (pairs.size === 0) { problems += 1; cells.push('половинки: НЕЧЕГО ПИЛИТЬ'); continue; }
      const shown = [...pairs].map((p) => {
        const parts = all.filter((b) => b.pair?.id === p)
          .sort((a, b) => a.pair!.side - b.pair!.side).map((b) => b.words[0]);
        return parts.join('|');
      });
      cells.push(`половинки ${pairs.size} (${shown.join(', ')})`);
    } else if (id === 'chain') {
      if (!setup.chain) { problems += 1; cells.push('цепь: НЕ ПОСТАВЛЕНА'); continue; }
      cells.push(`цепь y=${setup.chain.y.toFixed(0)}% need=${setup.chain.need}`);
    } else {
      const field = id === 'ice' ? 'ice' : 'hidden';
      const marked = setup.board.filter((b) => b[field] > 0);
      if (marked.length === 0) { problems += 1; cells.push(`${id}: НЕ ПОСТАВЛЕН`); continue; }
      cells.push(`${id} ${marked.length} (${marked
        .map((b) => `${b.words[0]}:${b[field]}`).join(', ')})`);
    }
    const limit = setup.moveLimit;
    if (limit !== null && (limit < setup.floor || limit > setup.floor * 2)) {
      problems += 1;
      cells.push(`${id}: лимит ${limit} при минимуме ${setup.floor} — ПОДОЗРИТЕЛЬНО`);
    }
  }
  console.log(`L${spec.levelId} (${spec.categories.length} кат., `
    + `лимит ${spec.board.moveLimit ?? '∞'})\n  ${cells.join('\n  ')}`);
}

console.log(problems === 0
  ? '\nвсе модификаторы находят материал на всех уровнях блока'
  : `\nпроблем: ${problems}`);
process.exit(problems === 0 ? 0 : 1);
