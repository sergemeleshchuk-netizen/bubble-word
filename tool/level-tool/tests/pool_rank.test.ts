/**
 * Ось ранга: какое место в пуле СВОЕЙ категории занимает слово.
 *
 * До этого отбор мерил слово расстоянием его частотности до медианы декады, то
 * есть ЦЕЛЫМ ПАКЕТОМ, и потому наказывал самое расхожее слово категории за то,
 * что оно слишком частотное: в UNITS OF TIME на первый уровень уезжал `instant`
 * (zipf 4.34, в 0.01 от цели 4.35), а `year` 5.96 и `day` 5.95 стояли в конце
 * очереди. Ранг мерит слово внутри его категории, и `year` получает верх пула
 * независимо от того, на какую декаду собирается уровень.
 *
 * Здесь проверяется ровно это обещание и три способа его потерять: снимок без
 * ранжирования, пресет без цели и уровень, которому цель дали слишком глубокую.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import { loadContentIndex } from '../web/src/core/snapshot.ts';
import { emptyPackHistory, generateLevel } from '../web/src/core/generator.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { configForRange, poolRankTargetFor, profileForRange } from '../web/src/core/decadeProfiles.ts';
import { makeSnapshot } from './fixtures/synthetic.ts';
import type { BlockConfig, LevelPlan } from '../web/src/core/types.ts';

/**
 * Категории с широким пулом: по восемь слов, частотность убывает. Именно на
 * широком пуле и живёт вся задача — у пула ровно в четыре слова выбора нет.
 */
const WIDE = [
  { key: 'time_units', label: 'UNITS OF TIME', theme: 'time', words: [
    ['year', 5.96], ['day', 5.95], ['second', 5.63], ['week', 5.56],
    ['month', 5.25], ['hour', 5.18], ['century', 5.02], ['instant', 4.34],
  ] },
  { key: 'water', label: 'BODIES OF WATER', theme: 'nature', words: [
    ['sea', 5.4], ['river', 5.3], ['lake', 5.1], ['bay', 4.7],
    ['pool', 4.6], ['canal', 4.0], ['gulf', 3.9], ['lagoon', 3.2],
  ] },
  { key: 'colors', label: 'COLORS', theme: 'properties', words: [
    ['red', 5.5], ['blue', 5.4], ['green', 5.3], ['white', 5.2],
    ['yellow', 4.8], ['purple', 4.4], ['gray', 4.3], ['beige', 3.4],
  ] },
  { key: 'tools', label: 'TOOLS', theme: 'tools', words: [
    ['saw', 4.9], ['hammer', 4.4], ['drill', 4.3], ['nail', 4.2],
    ['wrench', 3.8], ['pliers', 3.4], ['chisel', 3.0], ['awl', 2.6],
  ] },
  { key: 'birds', label: 'BIRDS', theme: 'animals', words: [
    ['bird', 5.4], ['duck', 4.8], ['owl', 4.4], ['crow', 4.2],
    ['robin', 3.9], ['finch', 3.2], ['heron', 3.0], ['grebe', 2.4],
  ] },
] as const;

function snapshotOf(poolRanks: boolean) {
  return makeSnapshot(
    WIDE.map((c) => ({
      key: c.key,
      label: c.label,
      theme: c.theme,
      words: c.words.map(([t, z]) => [t as string, z as number, 'approved' as const, 0.8]),
    })),
    { poolRanks });
}

function planWith(target: number | null): LevelPlan {
  return {
    levelId: 1, position: 1, role: 'entry', categoryCount: 4,
    metaCount: 0, metaDepthTarget: 0, rareTarget: 0, trapTarget: 0,
    chainCount: 0, modifier: 'none', targetDifficulty: [1, 10], targetInterest: [1, 10],
    moveLimitK: 1.5, poolRankTarget: target,
  };
}

function configWith(seed: string): BlockConfig {
  return { ...DEFAULT_BLOCK_CONFIG, seed, levelRange: [1, 1] };
}

function wordsOf(target: number | null, seed: string, poolRanks = true): Map<string, string[]> {
  const index = loadContentIndex(snapshotOf(poolRanks));
  const outcome = generateLevel(index, planWith(target), configWith(seed), emptyPackHistory());
  const out = new Map<string, string[]>();
  for (const c of outcome.spec?.categories ?? []) out.set(c.key, c.words.map((w) => w.text));
  return out;
}

/** Средняя частотность выданных слов: чем выше, тем расхожее взял отбор. */
function meanZipf(words: Map<string, string[]>): number {
  const zipf = new Map<string, number>();
  for (const c of WIDE) for (const [t, z] of c.words) zipf.set(t as string, z as number);
  const all = [...words.values()].flat().map((t) => zipf.get(t) ?? 0);
  return all.reduce((a, b) => a + b, 0) / Math.max(1, all.length);
}

test('цель на верх пула даёт самые расхожие слова категории', () => {
  const words = wordsOf(0, 'rank-top');
  const time = words.get('time_units');
  if (time) {
    assert.ok(!time.includes('instant'),
      `на верху пула instant делать нечего: ${time.join(', ')}`);
  }
  const water = words.get('water');
  if (water) {
    assert.ok(!water.includes('lagoon'), `${water.join(', ')}`);
  }
});

test('чем глубже цель, тем тише слова', () => {
  // одинаковый seed: меняется только цель, значит меняется только отбор слов
  const top = meanZipf(wordsOf(0, 'rank-depth'));
  const middle = meanZipf(wordsOf(0.5, 'rank-depth'));
  const bottom = meanZipf(wordsOf(1, 'rank-depth'));
  assert.ok(top > middle, `верх ${top.toFixed(2)} обязан быть громче середины ${middle.toFixed(2)}`);
  assert.ok(middle > bottom,
    `середина ${middle.toFixed(2)} обязана быть громче низа ${bottom.toFixed(2)}`);
});

test('снимок без ранжирования собирается по-прежнему', () => {
  // Ось ранга читается только там, где база принесла ранг. Если снимок его не
  // несёт, отбор обязан вернуться к прежней оси, а не остаться без сигнала.
  const words = wordsOf(0, 'rank-none', false);
  assert.ok(words.size > 0, 'уровень собрался');
  for (const list of words.values()) assert.equal(list.length, 4);
});

test('цель по рангу выключена у пресета без гейтов декады', () => {
  // 201-210 собирается без профиля декады: цели по рангу взять неоткуда, и
  // подставлять её самим нельзя — пакет обязан воспроизводиться как прежде.
  const plans = buildBlockPlan(DEFAULT_BLOCK_CONFIG);
  assert.ok(plans.length > 0);
  for (const p of plans) assert.equal(p.poolRankTarget ?? null, null);
});

test('роль уровня двигает цель: передышка берёт выше пика', () => {
  const config = configForRange([121, 130], 'rank-role');
  const plans = buildBlockPlan(config);
  const recovery = plans.find((p) => p.role === 'recovery');
  const peak = plans.find((p) => p.role === 'peak');
  assert.ok(recovery && peak, 'в декаде есть и передышка, и пик');
  assert.ok((recovery.poolRankTarget ?? 0) < (peak.poolRankTarget ?? 0),
    `передышка ${recovery.poolRankTarget} обязана быть выше пика ${peak.poolRankTarget}`);
});

test('у каждой декады цель по рангу задана и лежит в 0..1', () => {
  for (let from = 1; from <= 191; from += 10) {
    const profile = profileForRange([from, from + 9]);
    const target = poolRankTargetFor(profile);
    assert.ok(target >= 0 && target <= 1, `декада ${from}: цель ${target} вне 0..1`);
    assert.equal(typeof profile.poolRankTarget, 'number',
      `декада ${from}: цель не откалибрована, работает запасная формула`);
  }
});

test('спек уровня остаётся четвёрками по четыре слова', () => {
  const index = loadContentIndex(snapshotOf(true));
  const outcome = generateLevel(index, planWith(0.3), configWith('rank-shape'), emptyPackHistory());
  const spec = outcome.spec;
  assert.ok(spec, `уровень не собрался: ${outcome.reason ?? ''}`);
  assert.equal(spec.categories.length, 4);
  for (const c of spec.categories) {
    assert.equal(c.words.length, 4);
    assert.equal(new Set(c.words.map((w) => w.text)).size, 4);
  }
});
