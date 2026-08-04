/**
 * Негативные фикстуры: каждая нарушает РОВНО ОДИН инвариант и обязана падать
 * именно на нём.
 *
 * Зачем так строго: если фикстура падает не на том коде, значит проверка ловит
 * что-то другое, а настоящий инвариант не покрыт. «Все тесты зелёные» при этом
 * ничего не значит.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import { ContentIndex } from '../web/src/core/snapshot.ts';
import { validateLevel } from '../web/src/core/validator.ts';
import { countSolutions } from '../web/src/core/solutionCounter.ts';
import { hashQuadruple } from '../web/src/core/generateBlock.ts';
import {
  SIMPLE_SNAPSHOT, buildSpec, levelCategory, makeSnapshot, metaWord, validLevel, word,
} from './fixtures/synthetic.ts';

const index = new ContentIndex(SIMPLE_SNAPSHOT);

function checkOf(spec: ReturnType<typeof validLevel>, extra: Record<string, unknown> = {}) {
  const solutions = countSolutions(index, spec);
  return validateLevel(spec, { index, solutions, hashQuadruple, ...extra });
}

function assertFailsWith(spec: ReturnType<typeof validLevel>, code: string) {
  const result = checkOf(spec);
  const failed = result.issues.map((i) => i.code);
  assert.ok(failed.includes(code),
    `ожидалось падение ${code}, а упали: ${failed.join(', ') || 'ничего'}`);
  const issue = result.issues.find((i) => i.code === code)!;
  assert.ok(issue.message.length > 10, `${code}: объяснение слишком короткое`);
}

// --------------------------------------------------------------------------- //
// позитивная фикстура
// --------------------------------------------------------------------------- //

test('корректный уровень проходит все hard-проверки', () => {
  const result = checkOf(validLevel());
  const hard = result.issues.filter((i) => i.severity === 'hard');
  assert.deepEqual(hard.map((i) => i.code), [],
    `неожиданные падения: ${JSON.stringify(hard, null, 1)}`);
  assert.equal(result.passed, true);
});

test('у корректного уровня ровно одно решение', () => {
  const solutions = countSolutions(index, validLevel());
  assert.equal(solutions.count, 1);
  assert.equal(solutions.exhausted, true);
});

test('каждая проверка выполнилась, а не была пропущена', () => {
  const result = checkOf(validLevel());
  assert.ok(result.checks.length >= 15, `проверок всего ${result.checks.length}`);
  for (const check of result.checks) {
    assert.ok(check.detail.length > 0, `${check.code} без объяснения`);
  }
});

// --------------------------------------------------------------------------- //
// негативные фикстуры
// --------------------------------------------------------------------------- //

test('три слова в категории → CATEGORY_SIZE', () => {
  const spec = validLevel();
  spec.categories[0].words = spec.categories[0].words.slice(0, 3);
  assertFailsWith(spec, 'CATEGORY_SIZE');
});

test('пять слов в категории → CATEGORY_SIZE', () => {
  const spec = validLevel();
  spec.categories[0].words.push(word('purple', 4.0));
  assertFailsWith(spec, 'CATEGORY_SIZE');
});

test('одно слово спавнится дважды → WORD_OCCURRENCE', () => {
  const spec = validLevel();
  spec.categories[1].words[0] = word('red', 5.0);
  assertFailsWith(spec, 'WORD_OCCURRENCE');
});

test('неверное число стартовых пузырей → START_BUBBLE_COUNT', () => {
  const spec = buildSpec(201, validLevel().categories, { overrideStartBubbles: 17 });
  assertFailsWith(spec, 'START_BUBBLE_COUNT');
});

test('лимит ходов ниже минимума мерджей → MOVE_LIMIT_SANE', () => {
  const spec = buildSpec(201, validLevel().categories, { overrideMoveLimit: 5 });
  assertFailsWith(spec, 'MOVE_LIMIT_SANE');
});

test('цикл в мета-лесу → META_FOREST_ACYCLIC', () => {
  const categories = validLevel().categories;
  // colors ждёт fruits, fruits ждёт colors — игрок заперт
  categories[0].words[3] = metaWord('FRUITS', 'fruits');
  categories[1].words[3] = metaWord('COLORS', 'colors');
  categories[0].metaDepth = 1;
  categories[1].metaDepth = 1;
  assertFailsWith(buildSpec(201, categories), 'META_FOREST_ACYCLIC');
});

test('у мета-категории два родителя → META_PARENT_COUNT', () => {
  const categories = validLevel().categories;
  categories[0].words[3] = metaWord('TOOLS', 'tools');
  categories[1].words[3] = metaWord('TOOLS', 'tools');
  assertFailsWith(buildSpec(201, categories), 'META_PARENT_COUNT');
});

test('цикл в графе цепей → CHAIN_ACYCLIC', () => {
  const spec = buildSpec(201, validLevel().categories, {
    chains: [
      { locksCategory: 'colors', unlockedByCompleting: 'fruits' },
      { locksCategory: 'fruits', unlockedByCompleting: 'colors' },
    ],
  });
  assertFailsWith(spec, 'CHAIN_ACYCLIC');
});

test('цепь заперла категорию быстрой победы → CHAIN_ACYCLIC', () => {
  const categories = validLevel().categories;
  const spec = buildSpec(201, categories, {
    chains: [{ locksCategory: categories[0].key, unlockedByCompleting: categories[1].key }],
  });
  assertFailsWith(spec, 'CHAIN_ACYCLIC');
});

test('нет ни одной категории быстрой победы → QUICK_WIN_PRESENT', () => {
  const snapshot = makeSnapshot([
    { key: 'rare_a', label: 'RARE A', words: [
      ['aglet', 1.8, 'approved'], ['numbat', 1.5, 'approved'],
      ['gharial', 1.4, 'approved'], ['tabouleh', 1.9, 'approved']] },
    { key: 'rare_b', label: 'RARE B', words: [
      ['decagon', 2.1, 'approved'], ['heptagon', 2.0, 'approved'],
      ['buckteeth', 1.7, 'approved'], ['soundhole', 1.6, 'approved']] },
  ]);
  const rareIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('rare_a', 'RARE A', [
      word('aglet', 1.8), word('numbat', 1.5), word('gharial', 1.4), word('tabouleh', 1.9)]),
    levelCategory('rare_b', 'RARE B', [
      word('decagon', 2.1), word('heptagon', 2.0), word('buckteeth', 1.7), word('soundhole', 1.6)]),
  ]);
  const result = validateLevel(spec, {
    index: rareIndex, solutions: countSolutions(rareIndex, spec), hashQuadruple });
  const codes = result.issues.map((i) => i.code);
  assert.ok(codes.includes('QUICK_WIN_PRESENT'), `упали: ${codes.join(', ')}`);
  assert.ok(codes.includes('RECOGNIZABILITY'),
    'уровень целиком из редких слов обязан падать и на узнаваемости');
});

test('слова-двойники в одной категории → NEAR_DUPLICATE_WORDS', () => {
  const snapshot = makeSnapshot([
    { key: 'sky', label: 'SKY', words: [
      ['star', 4.5, 'approved'], ['stars', 4.4, 'approved'],
      ['moon', 4.6, 'approved'], ['sun', 5.0, 'approved']] },
    { key: 'colors', label: 'COLORS', words: [
      ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
      ['green', 4.8, 'approved'], ['yellow', 4.5, 'approved']] },
  ]);
  const dupIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('sky', 'SKY', [
      word('star', 4.5), word('stars', 4.4), word('moon', 4.6), word('sun', 5.0)]),
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)]),
  ]);
  const result = validateLevel(spec, {
    index: dupIndex, solutions: countSolutions(dupIndex, spec), hashQuadruple });
  assert.ok(result.issues.some((i) => i.code === 'NEAR_DUPLICATE_WORDS'));
});

/**
 * Двойники в РАЗНЫХ категориях — тот случай, который прошёл приёмку 04.08:
 * `borders` в MAP и `border` в MAP WORDS. Формально уровень был безупречен (у
 * каждого слова один дом, решение единственное), играть в него было нельзя.
 */
test('слова-двойники в разных категориях → NEAR_DUPLICATE_WORDS', () => {
  const snapshot = makeSnapshot([
    { key: 'sky', label: 'SKY', words: [
      ['star', 4.5, 'approved'], ['moon', 4.6, 'approved'],
      ['sun', 5.0, 'approved'], ['cloud', 4.7, 'approved']] },
    { key: 'flags', label: 'FLAGS', words: [
      ['stars', 4.4, 'approved'], ['stripe', 4.2, 'approved'],
      ['pole', 4.3, 'approved'], ['banner', 4.1, 'approved']] },
  ]);
  const dupIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('sky', 'SKY', [
      word('star', 4.5), word('moon', 4.6), word('sun', 5.0), word('cloud', 4.7)]),
    levelCategory('flags', 'FLAGS', [
      word('stars', 4.4), word('stripe', 4.2), word('pole', 4.3), word('banner', 4.1)]),
  ]);
  const result = validateLevel(spec, {
    index: dupIndex, solutions: countSolutions(dupIndex, spec), hashQuadruple });
  const issue = result.issues.find((i) => i.code === 'NEAR_DUPLICATE_WORDS');
  assert.ok(issue, `не поймано, упали: ${result.issues.map((i) => i.code).join(', ')}`);
  assert.ok(issue.entities?.some((e) => e.includes('в разных категориях')),
    'разбор обязан называть обе категории — иначе непонятно, что править');
});

/**
 * Имена-близнецы: MAP и MAP WORDS. Проверка пересечения пулов (UNSEPARABLE_PAIR)
 * такую пару не видит — в базе у них НОЛЬ общих слов, потому что `border` никто
 * не разметил в MAP. Поэтому правило смотрит на имя, а не на разметку.
 */
test('вложенные имена категорий → CATEGORY_NAMES_DISTINCT', () => {
  const snapshot = makeSnapshot([
    { key: 'map', label: 'MAP', words: [
      ['chart', 4.5, 'approved'], ['area', 5.4, 'approved'],
      ['scale', 4.6, 'approved'], ['legend', 4.2, 'approved']] },
    { key: 'map_words', label: 'MAP WORDS', words: [
      ['globe', 4.3, 'approved'], ['route', 4.7, 'approved'],
      ['compass', 4.1, 'approved'], ['atlas', 4.0, 'approved']] },
  ]);
  const twinIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('map', 'MAP', [
      word('chart', 4.5), word('area', 5.4), word('scale', 4.6), word('legend', 4.2)]),
    levelCategory('map_words', 'MAP WORDS', [
      word('globe', 4.3), word('route', 4.7), word('compass', 4.1), word('atlas', 4.0)]),
  ]);
  const result = validateLevel(spec, {
    index: twinIndex, solutions: countSolutions(twinIndex, spec), hashQuadruple });
  assert.ok(result.issues.some((i) => i.code === 'CATEGORY_NAMES_DISTINCT'),
    `не поймано, упали: ${result.issues.map((i) => i.code).join(', ')}`);
});

test('фрагмент половинки совпадает со словом уровня → HALF_COLLISION', () => {
  const spec = validLevel();
  spec.halves = [{
    word: 'redwood', home: 'colors', fragments: ['red', 'wood'], fragmentsAreWords: true,
  }];
  assertFailsWith(spec, 'HALF_COLLISION');
});

test('копия четвёрки референса по умолчанию НЕ браковывается', () => {
  // referenceNovelty по умолчанию off: пока своя база не наполнена, очевидные
  // четвёрки совпадают с чужими сами собой, и это не повод отклонять уровень.
  const spec = validLevel();
  const copied = hashQuadruple(spec.categories[0].words.map((w) => w.text));
  const result = checkOf(spec, { referenceQuadrupleHashes: new Set([copied]) });
  assert.ok(!result.issues.some((i) => i.code === 'REFERENCE_NOVELTY'),
    `не должно быть замечания: ${result.issues.map((i) => i.code).join(', ')}`);
  assert.ok(result.passed, 'уровень должен проходить');
});

test('referenceNovelty=soft: копия отмечается, но уровень проходит', () => {
  const spec = validLevel();
  const copied = hashQuadruple(spec.categories[0].words.map((w) => w.text));
  const result = checkOf(spec, {
    referenceQuadrupleHashes: new Set([copied]), referenceNovelty: 'soft' });
  const issue = result.issues.find((i) => i.code === 'REFERENCE_NOVELTY');
  assert.ok(issue, `ждали замечание: ${result.issues.map((i) => i.code).join(', ')}`);
  assert.equal(issue?.severity, 'soft');
  assert.ok(result.passed, 'soft не должен браковать уровень');
});

test('referenceNovelty=hard: копия четвёрки референса браковывает уровень', () => {
  const spec = validLevel();
  const copied = hashQuadruple(spec.categories[0].words.map((w) => w.text));
  const result = checkOf(spec, {
    referenceQuadrupleHashes: new Set([copied]), referenceNovelty: 'hard' });
  const issue = result.issues.find((i) => i.code === 'REFERENCE_NOVELTY');
  assert.ok(issue, `ждали замечание: ${result.issues.map((i) => i.code).join(', ')}`);
  assert.equal(issue?.severity, 'hard');
  assert.ok(!result.passed, 'hard должен браковать уровень');
});

test('связь не в статусе approved → APPROVED_CONTENT_ONLY', () => {
  const snapshot = makeSnapshot([
    { key: 'colors', label: 'COLORS', words: [
      ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
      ['green', 4.8, 'approved'], ['teal', 3.4, 'hard_only']] },
    { key: 'fruits', label: 'FRUITS', words: [
      ['apple', 4.7, 'approved'], ['banana', 4.2, 'approved'],
      ['pear', 3.9, 'approved'], ['plum', 3.6, 'approved']] },
  ]);
  const hardIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('teal', 3.4)]),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('plum', 3.6)]),
  ]);
  const result = validateLevel(spec, {
    index: hardIndex, solutions: countSolutions(hardIndex, spec), hashQuadruple });
  assert.ok(result.issues.some((i) => i.code === 'APPROVED_CONTENT_ONLY'),
    `упали: ${result.issues.map((i) => i.code).join(', ')}`);
});

// --------------------------------------------------------------------------- //
// счётчик решений: главная семантическая проверка
// --------------------------------------------------------------------------- //

test('две полные раскладки обнаруживаются → GLOBAL_SOLUTION_COUNT', () => {
  // orange правдоподобно годится и в цвета, и во фрукты; при этом у каждой
  // категории есть запасное слово, поэтому существуют ДВЕ полные раскладки
  const snapshot = makeSnapshot([
    { key: 'colors', label: 'COLORS', words: [
      ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
      ['green', 4.8, 'approved'], ['orange', 4.6, 'approved'],
      ['lemon', 4.0, 'approved']] },
    { key: 'fruits', label: 'FRUITS', words: [
      ['apple', 4.7, 'approved'], ['banana', 4.2, 'approved'],
      ['pear', 3.9, 'approved'], ['orange', 4.6, 'approved'],
      ['lemon', 4.0, 'approved']] },
  ]);
  const ambIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('orange', 4.6)]),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('lemon', 4.0)]),
  ]);
  const solutions = countSolutions(ambIndex, spec);
  assert.equal(solutions.count, 2, 'должно найтись минимум две раскладки');
  const result = validateLevel(spec, { index: ambIndex, solutions, hashQuadruple });
  assert.ok(result.issues.some((i) => i.code === 'GLOBAL_SOLUTION_COUNT'));
  assert.equal(result.passed, false);
});

test('ловушка НЕ ломает уровень, если решение остаётся единственным', () => {
  // orange лежит в цветах и правдоподобен во фруктах, но у фруктов нет
  // свободного слота: подмена невозможна, решение одно
  const snapshot = makeSnapshot([
    { key: 'colors', label: 'COLORS', words: [
      ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
      ['green', 4.8, 'approved'], ['orange', 4.6, 'approved']] },
    { key: 'fruits', label: 'FRUITS', words: [
      ['apple', 4.7, 'approved'], ['banana', 4.2, 'approved'],
      ['pear', 3.9, 'approved'], ['plum', 3.6, 'approved']] },
  ], { alternatives: [['orange', 'fruits', 0.9, 0.4]] });
  const trapIndex = new ContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('orange', 4.6)]),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('plum', 3.6)]),
  ]);
  const solutions = countSolutions(trapIndex, spec);
  assert.equal(solutions.count, 1,
    'ловушка обязана сохранять единственность глобального решения');
});
