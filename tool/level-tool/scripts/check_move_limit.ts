/**
 * Разбор лимита ходов: что даёт наша формула и во что уровень обходится живому.
 *
 *   node scripts/check_move_limit.ts
 *
 * Три числа на уровень, и все три в одной валюте — в ходах:
 *   пол        сколько ходов нужно ИДЕАЛЬНОМУ игроку (3*M + распилы);
 *   запас      лимит минус пол — весь бюджет ошибок живого игрока;
 *   промахи    сколько ходов живой игрок отдаст за незнание слов (слепой бот,
 *              медиана и p90 по прогонам).
 *
 * Если промахи p90 больше запаса — уровень не проходится не потому, что он
 * сложный, а потому что бюджета ошибок в нём нет.
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const ranges: [number, number][] = [[1, 10], [11, 20], [51, 60], [121, 130]];

console.log('декада  ур  роль      кат расп  пол  лимит  K     запас  '
  + 'промахи мед/p90  бюджет  winRate');
for (const range of ranges) {
  const block = generateBlock({ snapshot, scoring, config: configForRange(range, 'limit-audit') });
  for (const level of block.levels) {
    const spec = level.spec;
    const floor = spec.categories.length * 3 + spec.halves.length;
    const limit = spec.board.moveLimit;
    const blind = level.blindPlay;
    const slack = limit === null ? null : limit - floor;
    console.log(
      `${String(range[0]).padStart(4)}-${String(range[1]).padEnd(4)}`
      + `${String(spec.levelId).padStart(4)}  ${(level.plan.role ?? '').padEnd(9)}`
      + `${String(spec.categories.length).padStart(3)}${String(spec.halves.length).padStart(5)}`
      + `${String(floor).padStart(6)}${String(limit ?? '∞').padStart(6)}`
      + `${(spec.board.moveLimitK ?? 0).toFixed(2).padStart(7)}`
      + `${String(slack ?? '∞').padStart(6)}   `
      + `${String(blind?.missesMedian ?? '-').padStart(5)}/${String(blind?.missesP90 ?? '-').padEnd(5)}`
      + `${(blind?.errorBudgetUsed ?? 0).toFixed(2).padStart(7)}`
      + `${((blind?.winRate ?? 1) * 100).toFixed(0).padStart(8)}%`);
  }
}
