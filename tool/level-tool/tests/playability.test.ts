/**
 * Динамическая проходимость и модификаторы — обещания релиза 1.10.0.
 *
 * Проверяются три вещи, на которых держится «уровень доигрывается»:
 *   1. Симулятор подтверждает: каждый принятый уровень доигрывается в лимит,
 *      без жёстких тупиков, досыпок «вне ритма» и состояний-«тупиков»
 *      (инцидент 02.08, уровень 12 «как в оригинале»).
 *   2. Модификатор из плана доезжает до спека, до handoff-пакета и до оценки D.
 *   3. Ярус easy/medium/hard — детерминированная функция от D.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { buildHandoffPack } from '../web/src/core/playableHandoff.ts';
import { simulatePlayability } from '../web/src/core/simulatePlayability.ts';
import {
  difficultyTier, type ScoringConfig,
} from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

// декада 31-40: половинки на рост, блокиратор на спайк — все ветки модификаторов
const block = generateBlock({
  snapshot, scoring, config: configForRange([31, 40], 'playability-test'),
});
const preset = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });

test('каждый принятый уровень доигрывается: в лимит, без тупиков и досыпок вне ритма', () => {
  for (const level of [...block.levels, ...preset.levels]) {
    const play = simulatePlayability(level.spec);
    assert.equal(play.winnable, true,
      `уровень ${level.spec.levelId}: ${play.failReason}`);
    if (play.moveLimit !== null) {
      assert.ok(play.movesNeeded <= play.moveLimit,
        `уровень ${level.spec.levelId}: нужно ${play.movesNeeded} > лимит ${play.moveLimit}`);
    }
    if (!level.spec.modifiers.chainLine) {
      assert.equal(play.rescues, 0,
        `уровень ${level.spec.levelId}: ${play.rescues} досыпок вне ритма`);
      assert.equal(play.perceivedDead, 0,
        `уровень ${level.spec.levelId}: ${play.perceivedDead} состояний-«тупиков»`);
    }
  }
});

test('модификатор плана доезжает до спека и до оценки D', () => {
  const modded = block.levels.filter((l) => l.plan.modifier !== 'none');
  assert.ok(modded.length > 0, 'в декаде 31-40 обязан быть хотя бы один модификатор');
  for (const level of modded) {
    const m = level.spec.modifiers;
    const inSpec = level.spec.halves.length > 0 || m.frozenBubbles.length > 0
      || m.hiddenBubbles.length > 0 || m.chainLine !== null;
    assert.ok(inSpec, `уровень ${level.spec.levelId}: модификатор `
      + `${level.plan.modifier} не оставил следа в спеке`);
    // блокиратор и распилы обязаны попасть в оценку механики
    if (m.frozenBubbles.length + m.hiddenBubbles.length > 0
      || level.spec.halves.length > 0) {
      assert.ok(level.difficulty.mechanicalTotal > 0,
        `уровень ${level.spec.levelId}: механика не вошла в D`);
    }
  }
});

test('handoff несёт модификатор, распилы и ярус сложности в подписи', () => {
  const pack = buildHandoffPack(block);
  for (const level of block.levels) {
    const handoff = pack.levels.find((l) => l.level_id === level.spec.levelId)!;
    assert.equal(handoff.chunks?.length ?? 0, level.spec.halves.length);
    const m = level.spec.modifiers;
    if (m.frozenBubbles.length > 0) assert.equal(handoff.modifier?.type, 'ice');
    if (m.hiddenBubbles.length > 0) assert.equal(handoff.modifier?.type, 'hidden');
    if (m.chainLine) assert.equal(handoff.modifier?.type, 'chain');
    assert.match(handoff.title, /easy|medium|hard/,
      `подпись без яруса: ${handoff.title}`);
  }
});

test('ярус сложности — детерминированная функция от D', () => {
  assert.equal(difficultyTier(1), 'easy');
  assert.equal(difficultyTier(3.5), 'easy');
  assert.equal(difficultyTier(4), 'medium');
  assert.equal(difficultyTier(6.5), 'medium');
  assert.equal(difficultyTier(7), 'hard');
  assert.equal(difficultyTier(9.5), 'hard');
});
