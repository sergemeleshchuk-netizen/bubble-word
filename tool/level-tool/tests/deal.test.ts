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
import { buildDeal, checkDeal, dealForSpec } from '../web/src/core/deal.ts';
import { BOARD_CAPACITY } from '../web/src/core/levelMath.ts';
import { buildSetup } from '../web/src/core/playableModifiers.ts';
import { buildSpec, validLevel, word, metaWord } from './fixtures/synthetic.ts';

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
