/**
 * Golden-фикстуры двух углов: сложность и интересность обязаны РАЗЪЕЗЖАТЬСЯ.
 *
 * Если обе шкалы всегда двигаются вместе, у нас не две шкалы, а одна с двумя
 * названиями, и вся идея разделения рушится. Поэтому существование обоих углов —
 * не пожелание, а тест:
 *
 *   D высокая / I низкая — тяжёлый и мучительный уровень;
 *   D низкая / I высокая — лёгкий и приятный.
 *
 * Плюс проверка, что нерешаемому и двусмысленному уровню оценка не выставляется.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { ContentIndex } from '../web/src/core/snapshot.ts';
import { computeDifficulty, type ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { computeInterest } from '../web/src/core/scoringInterest.ts';
import { countSolutions } from '../web/src/core/solutionCounter.ts';
import type { LevelCategory, LevelSpec, LevelWord, Trap } from '../web/src/core/types.ts';
import { buildSpec, levelCategory, makeSnapshot } from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

function w(text: string, zipf: number, obviousness: number, relation: string): LevelWord {
  return { text, kind: 'word', zipf, frequencyUnknown: false,
    relation, fit: 0.9, obviousness };
}

function metaW(text: string, child: string): LevelWord {
  return { text, kind: 'meta', metaChild: child, zipf: 4.0, frequencyUnknown: false };
}

// --------------------------------------------------------------------------- //
// угол 1: тяжёлый и мучительный
// --------------------------------------------------------------------------- //

/**
 * Как устроен этот уровень: 18 категорий, гора редких слов, все связи
 * однотипные и неочевидные, одна тема на весь уровень, ни ловушек, ни мета.
 * То есть нагрузка есть, а награды нет.
 */
function harshLevel(): { spec: LevelSpec; index: ContentIndex } {
  const categories: LevelCategory[] = [];
  const specs: Parameters<typeof makeSnapshot>[0] = [];

  for (let i = 0; i < 18; i += 1) {
    const words: LevelWord[] = [];
    const specWords: [string, number, 'approved', number][] = [];
    for (let j = 0; j < 4; j += 1) {
      // первые 4 категории частотные, чтобы уровень был решаем и имел вход;
      // остальные — намеренная экзотика
      const rare = i >= 4;
      const zipf = rare ? (j === 0 ? 1.6 : 2.2) : 3.4;
      const text = `w${i}_${j}`;
      words.push(w(text, zipf, rare ? 0.35 : 0.6, 'associated_with'));
      specWords.push([text, zipf, 'approved', rare ? 0.35 : 0.6]);
    }
    specs.push({ key: `cat${i}`, label: `CAT ${i}`, theme: 'monotone', words: specWords });
    categories.push(levelCategory(`cat${i}`, `CAT ${i}`, words,
      { theme: 'monotone', isQuickwin: i < 4 }));
  }
  return {
    spec: buildSpec(901, categories, { moveLimitK: 1.25 }),
    index: new ContentIndex(makeSnapshot(specs)),
  };
}

test('угол D-высокая / I-низкая существует', () => {
  const { spec, index } = harshLevel();
  const solutions = countSolutions(index, spec);
  const d = computeDifficulty(spec, index, scoring, solutions);
  const i = computeInterest(spec, index, scoring, solutions,
    { newWordShare: 0.2, unplannedHesitations: 3 });

  assert.equal(solutions.count, 1, 'фикстура обязана быть решаемой');
  assert.ok(d.value >= 8.5, `D = ${d.value}, ожидалось >= 8.5`);
  assert.ok(i.value <= 4.0, `I = ${i.value}, ожидалось <= 4.0`);
  assert.equal(i.aha, 0, 'без ловушек и мета ага-момента быть не может');
  assert.ok(i.variety <= 1.0, `Variety = ${i.variety}: одна тема и один тип связи`);
});

// --------------------------------------------------------------------------- //
// угол 2: лёгкий и приятный
// --------------------------------------------------------------------------- //

/**
 * Пять категорий, все слова частотные и очевидные, пять разных тем и пять разных
 * типов связи, одна честная ловушка и одна мета-связь: награда есть, нагрузки нет.
 */
function delightfulLevel(): { spec: LevelSpec; index: ContentIndex; traps: Trap[] } {
  const index = new ContentIndex(makeSnapshot([
    { key: 'colors', label: 'COLORS', theme: 'properties', words: [
      ['red', 5.0, 'approved', 0.95], ['blue', 4.9, 'approved', 0.95],
      ['green', 4.8, 'approved', 0.95], ['orange', 4.6, 'approved', 0.9]] },
    { key: 'fruits', label: 'FRUITS', theme: 'food', words: [
      ['apple', 4.7, 'approved', 0.95], ['banana', 4.2, 'approved', 0.95],
      ['pear', 3.9, 'approved', 0.9], ['plum', 3.6, 'approved', 0.9]] },
    { key: 'kitchen', label: 'KITCHEN', theme: 'home', words: [
      ['spoon', 4.4, 'approved', 0.92], ['fork', 4.5, 'approved', 0.92],
      ['plate', 4.6, 'approved', 0.92], ['kettle', 3.8, 'approved', 0.88]] },
    { key: 'weather', label: 'WEATHER', theme: 'nature', words: [
      ['rain', 5.1, 'approved', 0.95], ['snow', 4.9, 'approved', 0.95],
      ['wind', 4.8, 'approved', 0.93], ['fog', 4.0, 'approved', 0.9]] },
    { key: 'market', label: 'MARKET', theme: 'business', words: [
      ['stall', 3.9, 'approved', 0.85], ['basket', 4.3, 'approved', 0.9],
      ['price', 5.0, 'approved', 0.92], ['fruits', 4.4, 'approved', 0.8]] },
  ], { alternatives: [['orange', 'fruits', 0.9, 0.35]] }));

  const categories: LevelCategory[] = [
    levelCategory('colors', 'COLORS', [
      w('red', 5.0, 0.95, 'has_property'), w('blue', 4.9, 0.95, 'has_property'),
      w('green', 4.8, 0.95, 'has_property'), w('orange', 4.6, 0.9, 'has_property')],
      { theme: 'properties' }),
    levelCategory('fruits', 'FRUITS', [
      w('apple', 4.7, 0.95, 'is_a'), w('banana', 4.2, 0.95, 'is_a'),
      w('pear', 3.9, 0.9, 'is_a'), w('plum', 3.6, 0.9, 'is_a')],
      { theme: 'food' }),
    levelCategory('kitchen', 'KITCHEN', [
      w('spoon', 4.4, 0.92, 'found_in'), w('fork', 4.5, 0.92, 'found_in'),
      w('plate', 4.6, 0.92, 'found_in'), w('kettle', 3.8, 0.88, 'found_in')],
      { theme: 'home' }),
    levelCategory('weather', 'WEATHER', [
      w('rain', 5.1, 0.95, 'member_of_set'), w('snow', 4.9, 0.95, 'member_of_set'),
      w('wind', 4.8, 0.93, 'member_of_set'), w('fog', 4.0, 0.9, 'member_of_set')],
      { theme: 'nature' }),
    levelCategory('market', 'MARKET', [
      w('stall', 3.9, 0.85, 'part_of'), w('basket', 4.3, 0.9, 'part_of'),
      w('price', 5.0, 0.92, 'part_of'), metaW('fruits', 'fruits')],
      { theme: 'business' }),
  ];
  categories[1].metaDepth = 1;
  categories[1].parentKey = 'market';

  const traps: Trap[] = [{
    word: 'orange', home: 'colors', decoy: 'fruits',
    homeObviousness: 0.9, decoyFit: 0.9, decoyObviousness: 0.35,
  }];
  const spec = buildSpec(902, categories, { moveLimitK: 1.6 });
  spec.traps = traps;
  return { spec, index, traps };
}

test('угол D-низкая / I-высокая существует', () => {
  const { spec, index } = delightfulLevel();
  const solutions = countSolutions(index, spec);
  const d = computeDifficulty(spec, index, scoring, solutions);
  const i = computeInterest(spec, index, scoring, solutions, { newWordShare: 1 });

  assert.equal(solutions.count, 1, 'ловушка обязана сохранять единственность решения');
  assert.ok(d.value <= 4.5, `D = ${d.value}, ожидалось <= 4.5`);
  assert.ok(i.value >= 7.5, `I = ${i.value}, ожидалось >= 7.5`);
  assert.ok(i.aha > 0, 'честная ловушка и мета-связь обязаны давать ага-момент');
  assert.ok(i.variety >= 2.0, `Variety = ${i.variety}: пять типов связи и пять тем`);
});

test('шкалы действительно независимы: порядок по D и по I противоположен', () => {
  const harsh = harshLevel();
  const nice = delightfulLevel();
  const solHarsh = countSolutions(harsh.index, harsh.spec);
  const solNice = countSolutions(nice.index, nice.spec);

  const dHarsh = computeDifficulty(harsh.spec, harsh.index, scoring, solHarsh).value;
  const dNice = computeDifficulty(nice.spec, nice.index, scoring, solNice).value;
  const iHarsh = computeInterest(harsh.spec, harsh.index, scoring, solHarsh,
    { newWordShare: 0.2, unplannedHesitations: 3 }).value;
  const iNice = computeInterest(nice.spec, nice.index, scoring, solNice,
    { newWordShare: 1 }).value;

  assert.ok(dHarsh > dNice, `D: ${dHarsh} должно быть больше ${dNice}`);
  assert.ok(iHarsh < iNice, `I: ${iHarsh} должно быть МЕНЬШЕ ${iNice}`);
});

// --------------------------------------------------------------------------- //
// оценка не выставляется на бракованном уровне
// --------------------------------------------------------------------------- //

test('двусмысленному уровню оценка не выставляется', () => {
  const { spec, index } = delightfulLevel();
  const d = computeDifficulty(spec, index, scoring,
    { count: 2, nodesVisited: 10, exhausted: true });
  assert.equal(d.value, 0);
  assert.ok(d.explanation[0].includes('двусмыслен'));
});

test('нерешаемому уровню оценка не выставляется', () => {
  const { spec, index } = delightfulLevel();
  const d = computeDifficulty(spec, index, scoring,
    { count: 0, nodesVisited: 10, exhausted: true });
  assert.equal(d.value, 0);
  assert.ok(d.explanation[0].includes('нерешаем'));
});

test('разбивка D разделяет откалиброванное и объявленное', () => {
  const { spec, index } = delightfulLevel();
  const solutions = countSolutions(index, spec);
  const d = computeDifficulty(spec, index, scoring, solutions);
  assert.ok(Object.keys(d.base).length > 0, 'корзина base пуста');
  assert.ok(Object.keys(d.declared).length > 0, 'корзина declared пуста');
  for (const key of Object.keys(d.declared)) {
    assert.ok(key.includes('объявлено'),
      `фактор «${key}» в корзине declared должен быть явно помечен`);
  }
  const total = d.baseTotal + d.declaredTotal + d.semanticTotal + d.mechanicalTotal;
  assert.ok(Math.abs(total - d.value) <= 0.5,
    `сумма корзин ${total.toFixed(2)} расходится с D = ${d.value}`);
});
