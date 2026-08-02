/**
 * Одна и та же кривая декад, собранная из каждого источника контента.
 *
 *   node scripts/compare_source_decades.ts [--to 100] [--seed SEED]
 *
 * Зачем. Источников стало три, и у каждого свой словарь; вопрос, на который
 * отвечает этот прогон, ровно один: остаются ли уровни уровнями СВОЕЙ ДЕКАДЫ,
 * когда контент меняется целиком. Профиль декады (число категорий, ритм,
 * медиана частотности, длина слова, мета-пары, редкость) — наша параметризация,
 * и она не должна зависеть от того, откуда взяты слова. Если зависит — это
 * видно здесь строкой FAIL, а не спустя пакет.
 *
 * Что печатается на декаду и источник:
 *   собрано   уровней из плана (отказ генератора = дефицит контента);
 *   приёмка   checkDecadeFit целиком (те же проверки, что в отчёте блока);
 *   zipf      средняя медиана частотности блока против цели декады;
 *   букв      медиана и максимум длины слова против предела декады;
 *   мета/лов  мета-пар и ловушек на уровень;
 *   D / I     средние оценки блока.
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { checkDecadeFit, configForRange, profileForRange } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { CONTENT_SOURCES } from '../web/src/core/sources.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const lastLevel = Number(arg('to') ?? 100);
const seed = arg('seed') ?? 'decade-compare';
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const snapshots = new Map<string, Snapshot>();
for (const source of CONTENT_SOURCES) {
  snapshots.set(source.id, JSON.parse(
    readFileSync(join(ROOT, source.snapshotFile), 'utf8')) as Snapshot);
}

function median(values: number[]): number {
  const s = [...values].sort((a, b) => a - b);
  return s.length ? s[Math.floor(s.length / 2)] : 0;
}

console.log(`кривая 1-${lastLevel}, seed ${seed}\n`);
console.log('дек.  источник           собр  приёмка  zipf(цель)   букв мед/макс(пред)  '
  + 'мета  лов   D    I');

const totals = new Map<string, { built: number; planned: number; passed: number;
  decades: number; overLen: number; }>();

for (let from = 1; from <= lastLevel; from += 10) {
  const range: [number, number] = [from, Math.min(from + 9, lastLevel)];
  const profile = profileForRange(range);
  for (const source of CONTENT_SOURCES) {
    const snapshot = snapshots.get(source.id)!;
    const config = configForRange(range, seed);
    const result = generateBlock({ snapshot, config, scoring });
    const planned = result.levels.length + result.failures.length;

    const lengths = result.levels.flatMap((l) => l.spec.categories
      .flatMap((c) => c.words.map((w) => w.text.replace(/\s/g, '').length)));
    const zipfs = result.levels.map((l) => median(l.spec.categories
      .flatMap((c) => c.words.map((w) => w.zipf))
      .filter((z): z is number => z !== null)));
    const blockZipf = zipfs.length
      ? zipfs.reduce((a, b) => a + b, 0) / zipfs.length : 0;
    const meta = result.levels.map((l) => l.spec.categories
      .reduce((n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0));
    const traps = result.levels.map((l) => l.spec.traps.length);
    const d = result.levels.map((l) => l.difficulty.value);
    const i = result.levels.map((l) => l.interest.value);
    const mean = (xs: number[]): number =>
      (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : 0);

    const fit = checkDecadeFit(result.levels.map((l) => ({
      levelId: l.spec.levelId,
      categoryCount: l.spec.categories.length,
      zipfs: l.spec.categories.flatMap((c) => c.words.map((w) => w.zipf)),
      metaCount: l.spec.categories.reduce(
        (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0),
      metaDepth: Math.max(0, ...l.spec.categories.map((c) => c.metaDepth)),
      chainCount: l.spec.modifiers.chains.length,
      moveLimit: l.spec.board.moveLimit,
      startBubbles: l.spec.board.startBubbles,
      boardCapacity: l.spec.board.boardCapacity,
      wordsPerCategory: l.spec.board.wordsPerCategory,
    })), profile, undefined, planned);

    const failed = fit.checks.filter((c) => !c.passed).map((c) => c.code);
    const maxLen = lengths.length ? Math.max(...lengths) : 0;
    const stat = totals.get(source.id)
      ?? { built: 0, planned: 0, passed: 0, decades: 0, overLen: 0 };
    stat.built += result.levels.length;
    stat.planned += planned;
    stat.passed += fit.passed ? 1 : 0;
    stat.decades += 1;
    stat.overLen += maxLen > profile.maxWordLen ? 1 : 0;
    totals.set(source.id, stat);

    console.log(
      `${String(range[0]).padStart(3)}-  ${source.label.padEnd(18)} `
      + `${String(result.levels.length).padStart(2)}/${planned}  `
      + `${(fit.passed ? 'PASS' : failed.join(',')).padEnd(8)} `
      + `${blockZipf.toFixed(2)}(${profile.zipfMedianTarget.toFixed(2)})  `
      + `${String(median(lengths)).padStart(4)}/${String(maxLen).padStart(2)}`
      + `(${String(profile.maxWordLen).padStart(2)})  `
      + `${mean(meta).toFixed(1).padStart(4)} ${mean(traps).toFixed(1).padStart(4)} `
      + `${mean(d).toFixed(1).padStart(4)} ${mean(i).toFixed(1).padStart(4)}`);
  }
  console.log('');
}

console.log('итого по источникам:');
for (const source of CONTENT_SOURCES) {
  const t = totals.get(source.id)!;
  console.log(`  ${source.label.padEnd(18)} уровней ${t.built}/${t.planned}, `
    + `декад с полной приёмкой ${t.passed}/${t.decades}, `
    + `декад с превышением длины слова ${t.overLen}`);
}
