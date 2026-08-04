/**
 * Первая выкладка — обещание воспроизводимости.
 *
 * Смысл выкладки в том, что уровень, который проверили руками, и уровень,
 * который увидит игрок, — один и тот же. Значит проверять надо две вещи:
 * выкладка не теряет и не выдумывает слов (иначе категория несобираема прямо
 * в игре), и она не меняется от прогона к прогону (иначе всё предыдущее
 * бессмысленно).
 *
 * Отдельно проверяется, что оба прототипа получают ОДИН состав: встроенный
 * в инструмент — через `buildSetup`, играбельный HTML — через пакет.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { buildDeal, checkDeal, chunkKey, dealForSpec } from '../web/src/core/deal.ts';
import { BOARD_CAPACITY } from '../web/src/core/levelMath.ts';
import { buildSetup } from '../web/src/core/playableModifiers.ts';
import {
  buildSpec, levelCategory, metaWord, validLevel, word,
} from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });

// --------------------------------------------------------------------------- //
// полнота
// --------------------------------------------------------------------------- //

test('выкладка раздаёт каждое спавнящееся слово ровно один раз', () => {
  for (const level of block.levels) {
    assert.deepEqual(checkDeal(level.spec, level.spec.deal), [],
      `уровень ${level.spec.levelId}: выкладка не сходится`);
  }
});

test('мета-слово в выкладку не попадает: оно приходит превращением четвёрки', () => {
  let checked = 0;
  for (const level of block.levels) {
    const metaWords = level.spec.categories
      .flatMap((c) => c.words.filter((w) => w.kind === 'meta').map((w) => w.text));
    const dealt = new Set([...level.spec.deal.start, ...level.spec.deal.queue]
      .map((b) => b.word));
    for (const text of metaWords) {
      checked += 1;
      assert.ok(!dealt.has(text),
        `мета-слово ${text} лежит в выкладке уровня ${level.spec.levelId}`);
    }
  }
  assert.ok(checked > 0, 'в пресете нет мета-слов — проверка ничего не проверила');
});

test('на поле ровно столько пузырей, сколько вмещает поле', () => {
  for (const level of block.levels) {
    const total = level.spec.deal.start.length + level.spec.deal.queue.length;
    assert.equal(level.spec.deal.start.length, Math.min(BOARD_CAPACITY, total),
      `уровень ${level.spec.levelId}: поле заполнено не до вместимости`);
    assert.equal(total, level.spec.board.startBubbles,
      `уровень ${level.spec.levelId}: выкладка и start_bubbles разошлись`);
  }
});

test('на старте видна хотя бы одна категория целиком: уровню нужен вход', () => {
  for (const level of block.levels) {
    const onField = new Map<string, number>();
    for (const bubble of level.spec.deal.start) {
      onField.set(bubble.category, (onField.get(bubble.category) ?? 0) + 1);
    }
    const whole = level.spec.categories.filter((c) => {
      const spawnable = c.words.filter((w) => w.kind !== 'meta').length;
      return spawnable === level.spec.board.wordsPerCategory
        && onField.get(c.key) === spawnable;
    });
    assert.ok(whole.length >= 1,
      `уровень ${level.spec.levelId}: на старте нет ни одной полной категории`);
  }
});

// --------------------------------------------------------------------------- //
// воспроизводимость
// --------------------------------------------------------------------------- //

test('выкладка пересчитывается из спека и совпадает с сохранённой', () => {
  // Значит, её можно проверить у любого сданного пакета, не пересобирая блок.
  for (const level of block.levels) {
    assert.deepEqual(dealForSpec(level.spec), level.spec.deal,
      `уровень ${level.spec.levelId}: выкладка не воспроизводится из спека`);
  }
});

test('выкладка не зависит от потока случайности генератора', () => {
  // Свой seed из номера уровня и ключей категорий: лишняя выборка где-то выше
  // по коду не имеет права молча переложить поле на всех уровнях.
  const spec = validLevel();
  const first = buildDeal(spec.levelId, spec.categories, spec.board);
  const second = buildDeal(spec.levelId, spec.categories, spec.board);
  assert.deepEqual(first, second);
});

test('разные уровни получают разные выкладки', () => {
  const a = validLevel();
  const b = buildSpec(202, a.categories);
  assert.notDeepEqual(a.deal.start, b.deal.start,
    'выкладка одинакова на разных уровнях: seed не учитывает номер');
});

// --------------------------------------------------------------------------- //
// оба прототипа исполняют одну выкладку
// --------------------------------------------------------------------------- //

test('встроенный прототип берёт состав поля из выкладки уровня', () => {
  for (const level of block.levels.slice(0, 3)) {
    const setup = buildSetup(level.spec, 'none');
    const onField = setup.board.map((b) => b.words[0]).sort();
    const expected = level.spec.deal.start.map((b) => b.word).sort();
    assert.deepEqual(onField, expected,
      `уровень ${level.spec.levelId}: прототип инструмента разложил своё поле`);
    const inQueue = setup.queue.map((b) => b.words[0]).sort();
    assert.deepEqual(inQueue, level.spec.deal.queue.map((b) => b.word).sort(),
      `уровень ${level.spec.levelId}: очередь досыпки разошлась`);
  }
});

// --------------------------------------------------------------------------- //
// брак ловится
// --------------------------------------------------------------------------- //

test('потерянное слово выкладка не прощает', () => {
  const spec = validLevel();
  const broken = { start: spec.deal.start.slice(1), queue: spec.deal.queue };
  const problems = checkDeal(spec, broken);
  assert.ok(problems.length > 0, 'из выкладки убрали пузырь, а проверка молчит');
});

test('лишний пузырь выкладка не прощает', () => {
  const spec = validLevel();
  const broken = {
    start: spec.deal.start,
    queue: [...spec.deal.queue, { word: 'ghost', category: 'colors' }],
  };
  assert.ok(checkDeal(spec, broken).some((p) => p.includes('ghost')),
    'в выкладку добавили слово, которого в уровне нет, а проверка молчит');
});

test('уровень с мета-словом: в выкладке на пузырь меньше', () => {
  const spec = buildSpec(203, [
    ...validLevel().categories,
    // категория, чьё слово — имя другой категории уровня: мета-пузырь
    {
      key: 'nature', label: 'NATURE', rule: 'nature', theme: 'nature',
      words: [word('forest', 4.2), word('river', 4.4), word('mountain', 4.3),
        metaWord('colors', 'colors')],
      metaDepth: 0, parentKey: null, isQuickwin: false,
    },
  ]);
  const total = spec.deal.start.length + spec.deal.queue.length;
  assert.equal(total, spec.categories.length * 4 - 1,
    'мета-слово посчитали как обычный пузырь');
  assert.deepEqual(checkDeal(spec, spec.deal), []);
});

// --------------------------------------------------------------------------- //
// схема против мета и половинок
// --------------------------------------------------------------------------- //

/*
 * Требование владельца 03.08: «4 это 4, а половинки в разных досыпках и мета
 * не должны нарушать». До этого доля отдавалась очередной категории и молча
 * урезалась до её размера: мета-родитель (спавнится три слова, имя-мета на
 * старте не лежит) превращал четвёрку схемы в тройку, а распиленное слово
 * стоимостью в два пузыря съедало место соседней доли.
 */
const SCHEME_STRICT = [4, 4, 3, 3, 2];

function startByCategory(deal: ReturnType<typeof buildDeal>): Map<string, string[]> {
  const out = new Map<string, string[]>();
  for (const b of deal.start) {
    out.set(b.category, [...(out.get(b.category) ?? []), b.word]);
  }
  return out;
}

test('мета-категория не забирает четвёрку схемы: доля уходит тому, кто её держит', () => {
  // у категории meta_host спавнящихся слов три: четвёртое — имя дочерней категории
  const categories = [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)]),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('plum', 3.6)]),
    levelCategory('meta_host', 'GARDEN', [
      word('soil', 4.1), word('fence', 4.0), word('shed', 3.8), metaWord('COLORS', 'colors')]),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('saw', 4.4), word('drill', 4.0), word('wrench', 3.5)]),
    levelCategory('weather', 'WEATHER', [
      word('rain', 5.1), word('snow', 4.9), word('wind', 4.8), word('fog', 4.0)]),
  ];
  const deal = buildDeal(300, categories, { boardCapacity: BOARD_CAPACITY, wordsPerCategory: 4 },
    new Set<string>(), 2, SCHEME_STRICT);

  const shares = [...startByCategory(deal).values()].map((ws) => ws.length)
    .sort((a, b) => b - a);
  assert.deepEqual(shares, SCHEME_STRICT,
    `схема ${SCHEME_STRICT.join('-')} исполнена как ${shares.join('-')}`);
  // тройка досталась мета-родителю: четвёрку он держать не может
  const byCategory = startByCategory(deal);
  assert.equal(byCategory.get('meta_host')?.length, 3,
    'мета-родителю положена доля 3: спавнящихся слов у него три');
});

test('половинки уходят в досыпку и не съедают долю схемы', () => {
  const categories = [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)]),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('plum', 3.6)]),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('saw', 4.4), word('drill', 4.0), word('wrench', 3.5)]),
    levelCategory('weather', 'WEATHER', [
      word('rain', 5.1), word('snow', 4.9), word('wind', 4.8), word('fog', 4.0)]),
    levelCategory('birds', 'BIRDS', [
      word('crow', 4.3), word('owl', 4.2), word('swan', 3.9), word('finch', 3.4)]),
  ];
  // по распиленному слову в трёх категориях: каждое стоит на поле два пузыря
  const chunked = new Set([
    chunkKey('fruits', 'banana'), chunkKey('tools', 'wrench'), chunkKey('birds', 'finch')]);
  const deal = buildDeal(301, categories, { boardCapacity: BOARD_CAPACITY, wordsPerCategory: 4 },
    chunked, 2, SCHEME_STRICT);

  const byCategory = startByCategory(deal);
  const shares = [...byCategory.values()].map((ws) => ws.length).sort((a, b) => b - a);
  assert.deepEqual(shares, SCHEME_STRICT,
    `распилы не должны менять схему: вышло ${shares.join('-')}`);

  // распиленное слово попадает на старт только если доля забирает категорию целиком
  for (const [key, words] of byCategory) {
    const splits = words.filter((w) => chunked.has(chunkKey(key, w))).length;
    const spawnable = categories.find((c) => c.key === key)!.words
      .filter((w) => w.kind !== 'meta').length;
    const expected = words.length === spawnable ? 1 : 0;
    assert.ok(splits <= expected,
      `${key}: на старте ${splits} половинок при доле ${words.length} из ${spawnable}`);
  }
});
