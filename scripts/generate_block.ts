/**
 * Офлайн-сборка блока уровней тем же ядром, что работает в браузере.
 *
 *   node scripts/generate_block.ts [--seed SEED] [--out DIR] [--quiet]
 *
 * Печатает отчёт по блоку и, если задан --out, пишет туда pipeline JSON и game JSON.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { BlockConfig, Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import { generateBlock, toGameJson, toPipelineJson } from '../web/src/core/generateBlock.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

let referenceQuadrupleHashes: Set<string> | undefined;
try {
  const raw = JSON.parse(readFileSync(
    join(ROOT, 'data/reference-derived/reference-quadruple-hashes.json'), 'utf8'));
  referenceQuadrupleHashes = new Set<string>(raw.hashes);
} catch {
  referenceQuadrupleHashes = undefined;
}

const config: BlockConfig = { ...DEFAULT_BLOCK_CONFIG, seed: arg('seed') ?? DEFAULT_BLOCK_CONFIG.seed };

const rhythm = checkBlockRhythm(buildBlockPlan(config));
const started = Date.now();
const result = generateBlock({ snapshot, config, scoring, referenceQuadrupleHashes });
const elapsed = Date.now() - started;

console.log(`снимок базы   ${snapshot.content_snapshot_hash.slice(0, 16)}…`);
console.log(`seed          ${config.seed}`);
console.log(`ритм блока    ${rhythm.passed ? 'PASS' : 'ЗАМЕЧАНИЯ'}`);
for (const issue of rhythm.issues) console.log(`  - ${issue}`);
console.log(`собрано       ${result.levels.length} из ${buildBlockPlan(config).length}`
  + `, отказов ${result.failures.length}, за ${elapsed} мс`);
console.log(`pack hash     ${result.packHash.slice(0, 16)}…`);
console.log('');

const head = ['ур.', 'роль', 'кат', 'пуз', 'мета', 'гл', 'редк', 'лов', 'цепи',
  'реш', 'вал', 'D', 'I', 'поп'];
console.log(head.map((h, i) => h.padEnd(i === 1 ? 9 : 5)).join(''));
for (const level of result.levels) {
  const s = level.spec;
  const metaLinks = s.categories.reduce((n, c) =>
    n + c.words.filter((w) => w.kind === 'meta').length, 0);
  const depth = Math.max(0, ...s.categories.map((c) => c.metaDepth));
  const rare = s.categories.flatMap((c) => c.words)
    .filter((w) => w.kind === 'word' && w.zipf !== null && w.zipf < 3).length;
  const hardIssues = level.validation.issues.filter((i) => i.severity === 'hard').length;
  const row = [
    String(s.levelId), level.plan.role, String(s.categories.length),
    String(s.board.startBubbles), String(metaLinks), String(depth), String(rare),
    String(s.traps.length), String(s.modifiers.chains.length),
    String(level.solutions.count),
    hardIssues === 0 ? 'PASS' : `FAIL${hardIssues}`,
    String(level.difficulty.value), String(level.interest.value),
    String(level.attempts.length),
  ];
  console.log(row.map((c, i) => c.padEnd(i === 1 ? 9 : 5)).join(''));
}

if (result.failures.length) {
  console.log('\nОтказы генератора:');
  for (const failure of result.failures) {
    console.log(`  уровень ${failure.levelId}: ${failure.reason}`);
    for (const s of failure.suggestions.slice(0, 3)) console.log(`    → ${s}`);
  }
}

const allIssues = new Map<string, number>();
for (const level of result.levels) {
  for (const issue of level.validation.issues) {
    allIssues.set(`${issue.severity}/${issue.code}`,
      (allIssues.get(`${issue.severity}/${issue.code}`) ?? 0) + 1);
  }
}
if (allIssues.size) {
  console.log('\nЗамечания валидатора по блоку:');
  for (const [code, n] of Array.from(allIssues).sort((a, b) => b[1] - a[1])) {
    console.log(`  ${code}: ${n}`);
  }
}

const out = arg('out');
if (out) {
  const dir = resolve(ROOT, out);
  mkdirSync(dir, { recursive: true });
  for (const level of result.levels) {
    writeFileSync(join(dir, `level-${level.spec.levelId}.json`),
      JSON.stringify(toPipelineJson(level, result), null, 2), 'utf8');
    writeFileSync(join(dir, `game-${level.spec.levelId}.json`),
      JSON.stringify(toGameJson(level.spec), null, 2), 'utf8');
  }
  writeFileSync(join(dir, 'block.json'), JSON.stringify({
    pack_hash: result.packHash,
    content_snapshot_hash: result.contentSnapshotHash,
    generator_version: result.generatorVersion,
    config: result.config,
    rhythm,
    levels: result.levels.map((l) => ({
      level_id: l.spec.levelId, role: l.plan.role,
      difficulty: l.difficulty.value, interest: l.interest.value,
      level_spec_hash: l.levelSpecHash,
      validation_passed: l.validation.passed,
      solution_count: l.solutions.count,
    })),
    failures: result.failures,
  }, null, 2), 'utf8');
  console.log(`\n→ ${out}`);
}
