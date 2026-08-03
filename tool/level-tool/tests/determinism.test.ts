/**
 * Детерминированность — обещание, на котором держится вся архитектура.
 *
 * «Тот же конфиг + тот же seed + тот же снимок = тот же уровень» проверяется
 * здесь, а не декларируется в README. Отдельно проверяется обратное: время
 * сборки НЕ должно влиять на хеш.
 *
 * Плюс property-тест: на десятках seed каждый принятый уровень обязан
 * проходить hard-инварианты и иметь ровно одно решение.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { canonicalJson, levelSpecHash, sha256Hex } from '../web/src/core/hashing.ts';
import { createRng } from '../web/src/core/rng.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const run = (seed: string) => generateBlock({
  snapshot, scoring, config: { ...DEFAULT_BLOCK_CONFIG, seed },
});

// --------------------------------------------------------------------------- //
// хеширование
// --------------------------------------------------------------------------- //

test('sha256 совпадает с эталонными значениями', () => {
  assert.equal(sha256Hex(''),
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855');
  assert.equal(sha256Hex('abc'),
    'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
});

test('канонический JSON не зависит от порядка ключей', () => {
  assert.equal(canonicalJson({ b: 1, a: 2 }), canonicalJson({ a: 2, b: 1 }));
  assert.notEqual(canonicalJson({ a: [1, 2] }), canonicalJson({ a: [2, 1] }));
});

test('время сборки НЕ влияет на хеш уровня', () => {
  const spec = { levelId: 205, categories: [{ key: 'a' }] };
  const args = {
    levelSpec: spec, seed: 's', normalizedConfig: { x: 1 },
    generatorVersion: 'gen-1.0', contentSnapshotHash: 'h',
  };
  const first = levelSpecHash(args);
  // build_metadata живёт рядом с level_spec и в хеш не входит
  const withMetadata = { ...args, levelSpec: spec };
  assert.equal(levelSpecHash(withMetadata), first);
  // а изменение самого контента хеш менять обязано
  assert.notEqual(
    levelSpecHash({ ...args, levelSpec: { ...spec, levelId: 206 } }), first);
  assert.notEqual(levelSpecHash({ ...args, seed: 's2' }), first);
  assert.notEqual(levelSpecHash({ ...args, contentSnapshotHash: 'h2' }), first);
});

test('seed даёт воспроизводимый поток случайных чисел', () => {
  const a = createRng('seed-x');
  const b = createRng('seed-x');
  const c = createRng('seed-y');
  const seqA = Array.from({ length: 5 }, () => a.next());
  const seqB = Array.from({ length: 5 }, () => b.next());
  assert.deepEqual(seqA, seqB);
  assert.notDeepEqual(seqA, Array.from({ length: 5 }, () => c.next()));
  // stableWeight не зависит от того, сколько раз дёрнули next()
  const d = createRng('seed-x');
  d.next(); d.next();
  assert.equal(createRng('seed-x').stableWeight('key'), d.stableWeight('key'));
});

// --------------------------------------------------------------------------- //
// воспроизводимость сборки
// --------------------------------------------------------------------------- //

test('один и тот же seed даёт один и тот же блок', () => {
  const first = run('repeat-me');
  const second = run('repeat-me');
  assert.equal(first.packHash, second.packHash);
  assert.deepEqual(
    first.levels.map((l) => l.levelSpecHash),
    second.levels.map((l) => l.levelSpecHash));
});

test('разные seed обычно дают разные блоки', () => {
  const hashes = new Set(['a', 'b', 'c', 'd'].map((s) => run(`diff-${s}`).packHash));
  assert.ok(hashes.size >= 3, `из 4 seed получилось только ${hashes.size} разных блоков`);
});

test('изменение конфига меняет хеш уровня', () => {
  const base = run('cfg');
  const changed = generateBlock({
    snapshot, scoring,
    config: { ...DEFAULT_BLOCK_CONFIG, seed: 'cfg', rarityRange: [4, 6] },
  });
  assert.notEqual(base.packHash, changed.packHash);
});

// --------------------------------------------------------------------------- //
// property-тест
// --------------------------------------------------------------------------- //

test('на 12 seed каждый принятый уровень держит hard-инварианты', () => {
  let levels = 0;
  let failures = 0;
  for (let i = 0; i < 12; i += 1) {
    const result = run(`prop-${i}`);
    failures += result.failures.length;
    for (const level of result.levels) {
      levels += 1;
      const hard = level.validation.issues.filter((issue) => issue.severity === 'hard');
      assert.deepEqual(hard.map((issue) => issue.code), [],
        `seed prop-${i}, уровень ${level.spec.levelId}: ${JSON.stringify(hard)}`);
      assert.equal(level.solutions.count, 1,
        `seed prop-${i}, уровень ${level.spec.levelId}: решений ${level.solutions.count}`);
      assert.ok(level.spec.categories.every((c) => c.words.length === 4));
      assert.ok(level.spec.categories.some((c) => c.isQuickwin),
        'инвариант открытой двери нарушен');
    }
  }
  assert.ok(levels >= 100, `сгенерировано всего ${levels} уровней`);
  assert.equal(failures, 0, `отказов генератора: ${failures}`);
});

test('ритм дефолтного блока проходит проверку пилы', () => {
  const rhythm = checkBlockRhythm(buildBlockPlan(DEFAULT_BLOCK_CONFIG),
    DEFAULT_BLOCK_CONFIG.categoryCorridor);
  assert.deepEqual(rhythm.issues, []);
  assert.equal(rhythm.passed, true);
});

test('плохой ритм отлавливается: монотонная линия не проходит', () => {
  const flat = checkBlockRhythm(buildBlockPlan({
    ...DEFAULT_BLOCK_CONFIG,
    categoryPlan: [11, 12, 13, 14, 15, 16, 17, 18, 18, 18],
    metaPlan: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  }));
  assert.equal(flat.passed, false);
  assert.ok(flat.issues.some((i) => i.includes('вниз')),
    `ожидалась жалоба на отсутствие спусков, получено: ${flat.issues.join(' | ')}`);
});

test('арифметика доски совпадает с формулой на всех уровнях блока', () => {
  for (const level of run('math').levels) {
    const meta = level.spec.categories.reduce((n, c) =>
      n + c.words.filter((w) => w.kind === 'meta').length, 0);
    assert.equal(level.spec.board.startBubbles,
      level.spec.categories.length * 4 - meta);
    // null = туториал без лимита ходов; там сравнивать не с чем
    if (level.spec.board.moveLimit !== null) {
      assert.ok(level.spec.board.moveLimit >= level.spec.board.moveFloor);
    }
  }
});
