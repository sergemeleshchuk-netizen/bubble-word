/**
 * Профиль выкладки в сложности и память с механикой в интересе (ред. 03.08).
 *
 * Что здесь защищается:
 *   1. Знаки факторов. Готовая четвёрка и тройка на старте ОБЛЕГЧАЮТ уровень,
 *      одиночки и бесплодная досыпка УСЛОЖНЯЮТ. Перепутанный знак — самая
 *      дорогая ошибка в этой модели: она бы тихо инвертировала кривую.
 *   2. Профиль считается из выкладки, а не из числа категорий.
 *   3. Свежесть перестала быть константой: до ред. 03.08 все сто замеренных
 *      уровней получали ровно 2.05, и композит не несёл информации вовсе.
 *   4. Модификатор гасится повторением: сложность от повтора не падает,
 *      интерес падает — иначе обе шкалы двигались бы вместе.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { DealBubble, LevelSpec, Snapshot } from '../web/src/core/types.ts';
import { dealShape } from '../web/src/core/dealShape.ts';
import { computeDifficulty, type ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { computeInterest } from '../web/src/core/scoringInterest.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import { buildSpec, validLevel } from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const index = new ContentIndex(snapshot);

/** Тот же уровень, но выкладка переписана руками: поле собрано по категориям. */
function withStart(spec: LevelSpec, perCategory: number[]): LevelSpec {
  const start: DealBubble[] = [];
  const queue: DealBubble[] = [];
  spec.categories.forEach((c, i) => {
    const words = c.words.filter((w) => w.kind !== 'meta').map((w) => w.text);
    const onField = Math.min(perCategory[i] ?? 0, words.length);
    words.forEach((word, k) => {
      (k < onField ? start : queue).push({ word, category: c.key });
    });
  });
  return { ...spec, deal: { start, queue } };
}

test('профиль выкладки считает четвёрки, тройки, пары и одиночки', () => {
  const spec = buildSpec(910, validLevel().categories.slice(0, 4));
  const shaped = withStart(spec, [4, 3, 2, 1]);
  const shape = dealShape(shaped);
  assert.equal(shape.fullSets, 1);
  assert.equal(shape.triples, 1);
  assert.equal(shape.pairs, 1);
  assert.equal(shape.singles, 1);
  assert.equal(shape.startFieldSize, 10);
});

test('готовые четвёрки на старте облегчают, одиночки усложняют', () => {
  const categories = validLevel().categories.slice(0, 4);
  const generous = withStart(buildSpec(911, categories), [4, 4, 4, 4]);
  const scattered = withStart(buildSpec(911, categories), [1, 1, 1, 1]);

  const dGenerous = computeDifficulty(generous, index, scoring);
  const dScattered = computeDifficulty(scattered, index, scoring);

  assert.ok(dGenerous.value < dScattered.value,
    `поле из готовых четвёрок (${dGenerous.value}) обязано быть легче поля `
    + `из одиночек (${dScattered.value})`);
  // и это именно вклад раскладки, а не побочный эффект другого слагаемого
  assert.ok(dGenerous.declaredTotal < dScattered.declaredTotal);
  assert.equal(dGenerous.baseTotal, dScattered.baseTotal,
    'откалиброванная часть от раскладки зависеть не должна: слова те же');
});

test('тройка на старте легче пары, пара легче одиночки', () => {
  const categories = validLevel().categories.slice(0, 4);
  const values = [3, 2, 1].map((n) =>
    computeDifficulty(withStart(buildSpec(912, categories), [n, n, n, n]),
      index, scoring).declaredTotal);
  assert.ok(values[0] < values[1], `тройки ${values[0]} vs пары ${values[1]}`);
  assert.ok(values[1] < values[2], `пары ${values[1]} vs одиночки ${values[2]}`);
});

test('бесплодная досыпка усложняет: доля продуктивных волн входит в оценку', () => {
  const categories = validLevel().categories.slice(0, 4);
  const spec = withStart(buildSpec(913, categories), [4, 4, 1, 1]);
  const shape = dealShape(spec);
  assert.ok(shape.refillWaves > 0, 'у уровня с очередью обязаны быть волны досыпки');

  const weights = scoring.difficulty.declared;
  const withDry = computeDifficulty(spec, index, {
    ...scoring,
    difficulty: {
      ...scoring.difficulty,
      declared: { ...weights, deal_dry_refill: 2.0 },
    },
  });
  const withoutDry = computeDifficulty(spec, index, {
    ...scoring,
    difficulty: {
      ...scoring.difficulty,
      declared: { ...weights, deal_dry_refill: 0 },
    },
  });
  if (shape.refillCompletionShare < 1) {
    assert.ok(withDry.declaredTotal > withoutDry.declaredTotal,
      'при бесплодных волнах фактор обязан добавлять сложность');
  } else {
    assert.equal(withDry.declaredTotal, withoutDry.declaredTotal,
      'все волны продуктивны — фактор молчит');
  }
});

test('свежесть больше не константа: новизна и эхо-категории её двигают', () => {
  const spec = buildSpec(914, validLevel().categories);
  const fresh = computeInterest(spec, index, scoring, undefined, { newWordShare: 1 });
  const stale = computeInterest(spec, index, scoring, undefined, { newWordShare: 0.2 });
  const staleWithEcho = computeInterest(spec, index, scoring, undefined,
    { newWordShare: 0.2, echoCategories: 3 });

  assert.ok(fresh.freshness > stale.freshness,
    `новые слова (${fresh.freshness}) обязаны быть свежее повторов (${stale.freshness})`);
  assert.ok(staleWithEcho.freshness > stale.freshness,
    'эхо-категории компенсируют потерю новизны');
  assert.ok(staleWithEcho.freshness <= fresh.freshness,
    'но полностью новый уровень эхо не перебивает');
});

test('модификатор радует новизной: повторение гасит надбавку к интересу', () => {
  const spec = buildSpec(915, validLevel().categories);
  spec.modifiers = { ...spec.modifiers, chainLine: { need: 2 } };

  const first = computeInterest(spec, index, scoring, undefined,
    { newWordShare: 1, modifierSeenBefore: 0 });
  const fourth = computeInterest(spec, index, scoring, undefined,
    { newWordShare: 1, modifierSeenBefore: 3 });
  assert.ok(first.variety > fourth.variety,
    `первый уровень с механикой (${first.variety}) интереснее четвёртого (${fourth.variety})`);

  // а сложность от повторения механики не падает: механика та же
  const d = computeDifficulty(spec, index, scoring);
  assert.ok(d.mechanicalTotal > 0, 'цепь-линия обязана входить в механическую часть D');
});
