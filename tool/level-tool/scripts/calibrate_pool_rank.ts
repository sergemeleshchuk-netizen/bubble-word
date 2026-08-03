/**
 * Калибровка цели по рангу для каждой декады.
 *
 *   node scripts/calibrate_pool_rank.ts [--seed SEED] [--source production]
 *
 * Зачем. `poolRankTarget` говорит генератору, из какой части пула категории
 * брать слова: 0 — верх (самые расхожие слова каждой категории), 1 — низ.
 * Приёмка же меряет декаду ДРУГИМ числом — медианой частотности блока
 * (`zipfMedianTarget`, замер оригинала). Связь между ними монотонна, но не
 * линейна: она зависит от того, какие категории попали в декаду и насколько
 * широки их пулы. Выводить её формулой значит подгонять на глаз — линейная
 * прикидка промахнулась на шести декадах из двадцати.
 *
 * Поэтому цель не выводится, а ПОДБИРАЕТСЯ: для каждой декады скрипт делит
 * отрезок пополам, пока медиана собранного блока не сойдётся с целью декады.
 * Числа печатаются готовой таблицей — их место в `DECADE_PROFILES`.
 *
 * Скрипт ничего не пишет сам: калибровка обязана быть видна в диффе.
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { BlockConfig, Snapshot } from '../web/src/core/types.ts';
import { buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { DECADE_PROFILES, configForRange, decadeLabel } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { CONTENT_SOURCES, DEFAULT_SOURCE_ID } from '../web/src/core/sources.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const sourceArg = arg('source') ?? DEFAULT_SOURCE_ID;
const source = CONTENT_SOURCES.find((s) => s.id === sourceArg);
if (!source) throw new Error(`неизвестный источник «${sourceArg}»`);
const snapshot = JSON.parse(
  readFileSync(join(ROOT, source.snapshotFile), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const seed = arg('seed') ?? 'final-03';

/** Медиана частотности слов блока — то же число, что меряет приёмка. */
function blockZipfMedian(config: BlockConfig): number | null {
  const result = generateBlock({ snapshot, config, scoring });
  const medians: number[] = [];
  for (const level of result.levels) {
    const zs = level.spec.categories
      .flatMap((c) => c.words)
      .map((w) => w.zipf)
      .filter((z): z is number => z !== null)
      .sort((a, b) => a - b);
    if (zs.length) medians.push(zs[Math.floor(zs.length * 0.5)]);
  }
  if (!medians.length) return null;
  return medians.reduce((a, b) => a + b, 0) / medians.length;
}

function withTarget(range: [number, number], target: number): BlockConfig {
  const config = configForRange(range, seed);
  if (!config.decadeGates) throw new Error('у декады нет гейтов');
  return { ...config, decadeGates: { ...config.decadeGates, poolRankTarget: target } };
}

/**
 * Деление отрезка пополам: чем глубже цель по рангу, тем тише блок, поэтому
 * функция монотонно убывает и половинное деление сходится. Двенадцати шагов
 * хватает: шаг по рангу становится меньше 0.001, а приёмка меряет с допуском
 * 0.20 — дальше уточнять нечего.
 */
function calibrate(range: [number, number], wanted: number): { target: number; got: number } {
  let lo = 0;
  let hi = 1;
  let best = { target: 0.3, got: Number.NaN };
  for (let step = 0; step < 12; step += 1) {
    const mid = (lo + hi) / 2;
    const got = blockZipfMedian(withTarget(range, mid));
    if (got === null) break;
    best = { target: mid, got };
    if (Math.abs(got - wanted) < 0.005) break;
    if (got > wanted) lo = mid; else hi = mid;   // глубже = тише
  }
  return best;
}

console.log(`источник ${source.label}, seed ${seed}`);
console.log('декада      цель zipf   ранг     получилось   промах');
const rows: string[] = [];
for (const profile of DECADE_PROFILES) {
  const range: [number, number] = [profile.from, profile.from + 9];
  const plan = buildBlockPlan(configForRange(range, seed));
  if (!plan.length) continue;
  const { target, got } = calibrate(range, profile.zipfMedianTarget);
  const miss = got - profile.zipfMedianTarget;
  console.log(`${decadeLabel(profile).padEnd(10)}  ${profile.zipfMedianTarget.toFixed(2)}      `
    + `${target.toFixed(3)}    ${got.toFixed(2)}         ${miss >= 0 ? '+' : ''}${miss.toFixed(2)}`);
  rows.push(`  { from: ${profile.from}, poolRankTarget: ${target.toFixed(3)} },`);
}
console.log('\nдля DECADE_PROFILES:');
console.log(rows.join('\n'));
