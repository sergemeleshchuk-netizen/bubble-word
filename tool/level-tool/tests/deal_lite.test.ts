/**
 * Облегчённая раздача стартового поля (minStartWords >= 2, core/deal.ts).
 *
 * Обещания, которые здесь закреплены:
 *  1) при минимуме «пара» на старте нет категорий-одиночек — пузырей, которым
 *     не с чем сливаться;
 *  2) категории, не попавшие на поле, целиком ждут в очереди — слова не теряются;
 *  3) режим записывается в спек и выкладка пересчитывается из одного спека;
 *  4) историческая раздача (минимум 1 или поле не задано) не меняется ни на
 *     байт — хеши сданных пакетов вне опасности;
 *  5) конфиг декады получает облегчённое умолчание, пресет 201-210 — нет.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { LevelSpec, Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { buildDeal, checkDeal, dealForSpec } from '../web/src/core/deal.ts';
import { simulatePlayability } from '../web/src/core/simulatePlayability.ts';
import {
  DEFAULT_DEAL_RANGES, configForRange, dealMinStartWordsFor,
} from '../web/src/core/decadeProfiles.ts';
import { validLevel } from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/lexicon.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

/** Сколько слов каждой категории лежит на старте. */
function startCounts(spec: LevelSpec): Map<string, number> {
  const counts = new Map<string, number>();
  for (const b of spec.deal.start) {
    counts.set(b.category, (counts.get(b.category) ?? 0) + 1);
  }
  return counts;
}

// --------------------------------------------------------------------------- //
// свойства облегчённой раздачи на настоящем крупном блоке
// --------------------------------------------------------------------------- //

// Декада 121-130 — самая показательная: 11-16 категорий, при ровной раздаче
// одиночек 4-7 на уровень. Конфиг берётся штатным путём (configForRange),
// то есть проверяется и облегчённое умолчание.
const config = configForRange([121, 130], 'deal-lite-test');
const block = generateBlock({ snapshot, scoring, config });

test('конфиг декады получает облегчённое умолчание из таблицы промежутков', () => {
  assert.equal(config.dealMinStartWords, 2);
});

/*
 * Решение владельца 03.08: «починить причину». Пресет был последним местом с
 * исторической ровной раздачей — из-за неё уровень 201 встречал игрока полем
 * 4-2-2-2-2-2-2-2-2-1-1-1. Держали её ради байт-в-байт воспроизведения
 * data/final-pack, но тот пакет — артефакт прежнего снимка базы, и инструмент
 * перестал воспроизводить его ещё при переходе на аудированную базу.
 */
test('пресет 201-210 раздаёт старт в глубину, как вся остальная кривая', () => {
  assert.equal(DEFAULT_BLOCK_CONFIG.dealMinStartWords, 2);
});

test('облегчённая раздача: на старте нет категорий-одиночек', () => {
  assert.ok(block.levels.length >= 8, `декада собралась на ${block.levels.length}/10`);
  for (const level of block.levels) {
    for (const [key, n] of startCounts(level.spec)) {
      assert.ok(n >= 2,
        `уровень ${level.spec.levelId}: категория ${key} лежит на старте `
        + `${n} словом — одиночек в облегчённой раздаче быть не должно`);
    }
  }
});

/*
 * Требование владельца продукта 03.08, после наигровки уровня на 12 категорий:
 * «одиночек быть не должно, двоек меньше, троек и четвёрок сразу больше».
 * Двойка на старте — материал для хода, но пачка досыпки её не закрывает: ей
 * нужно ещё два слова. Тройке нужно одно, и пачка в 4 пузыря закрывает сразу
 * две таких категории. Поэтому бюджет поля тратится в глубину.
 */
test('старт уходит в глубину: троек и четвёрок больше, чем пар', () => {
  for (const level of block.levels) {
    const shares = [...startCounts(level.spec).values()];
    const deep = shares.filter((n) => n >= 3).length;
    const shallow = shares.filter((n) => n === 2).length;
    assert.ok(deep > shallow,
      `уровень ${level.spec.levelId}: троек и четвёрок ${deep}, пар ${shallow} `
      + `(${[...shares].sort((a, b) => b - a).join('-')})`);
  }
});

/*
 * Ритм досыпки: пачка обязана открывать сбор. Считаем это на зрячем боте — он
 * играет по правилам прототипа, включая фиксированные пачки 4/3/1. Доля
 * продуктивных волн ниже половины означала бы, что игрок чаще получает
 * обрывки, чем развязку, — то самое состояние «уровень сломан», из-за которого
 * досыпку когда-то раздули до добора поля до нормы.
 */
test('пачка досыпки открывает сбор чаще, чем не открывает', () => {
  for (const level of block.levels) {
    const play = simulatePlayability(level.spec);
    if (play.refillWaves === 0) continue;   // весь уровень уместился на поле
    const share = play.refillCompletions / play.refillWaves;
    assert.ok(share >= 0.5,
      `уровень ${level.spec.levelId}: продуктивных волн `
      + `${play.refillCompletions}/${play.refillWaves}`);
  }
});

test('категории вне поля целиком в очереди: выкладка сходится по словам', () => {
  for (const level of block.levels) {
    assert.deepEqual(checkDeal(level.spec, level.spec.deal), [],
      `уровень ${level.spec.levelId}: выкладка не сходится`);
  }
});

test('режим раздачи записан в спек и выкладка пересчитывается из спека', () => {
  for (const level of block.levels) {
    assert.equal(level.spec.board.dealMinStartWords, 2,
      `уровень ${level.spec.levelId}: режим раздачи не записан в спек`);
    assert.deepEqual(dealForSpec(level.spec), level.spec.deal,
      `уровень ${level.spec.levelId}: выкладка не воспроизводится из спека`);
  }
});

test('вход в уровень сохранился: одна категория лежит целиком и при облегчённой раздаче', () => {
  for (const level of block.levels) {
    const counts = startCounts(level.spec);
    const whole = level.spec.categories.filter((c) => {
      const spawnable = c.words.filter((w) => w.kind !== 'meta').length;
      return (counts.get(c.key) ?? 0) >= Math.min(
        spawnable, level.spec.board.wordsPerCategory);
    });
    assert.ok(whole.length >= 1,
      `уровень ${level.spec.levelId}: на старте нет полной категории`);
  }
});

// --------------------------------------------------------------------------- //
// историческая раздача не тронута
// --------------------------------------------------------------------------- //

test('минимум 1 равен исторической раздаче байт в байт', () => {
  const spec = validLevel();
  const legacy = buildDeal(spec.levelId, spec.categories, spec.board);
  const explicit = buildDeal(spec.levelId, spec.categories, spec.board,
    new Set<string>(), 1);
  assert.deepEqual(explicit, legacy);
});

test('явная «1» в конфиге не попадает в спек: хеш совпадает с историческим', () => {
  const explicit = generateBlock({ snapshot, scoring,
    config: { ...configForRange([121, 130], 'deal-lite-test'), dealMinStartWords: 1 } });
  for (const level of explicit.levels) {
    assert.equal(level.spec.board.dealMinStartWords, undefined);
  }
});

// --------------------------------------------------------------------------- //
// таблица промежутков
// --------------------------------------------------------------------------- //

test('умолчание таблицы — облегчённая раздача с первого уровня', () => {
  assert.deepEqual(DEFAULT_DEAL_RANGES, [{ from: 1, minStartWords: 2 }]);
});

test('промежутки выбираются по последней подходящей строке', () => {
  const ranges = [
    { from: 1, minStartWords: 2 },
    { from: 121, minStartWords: 1 },
    { from: 301, minStartWords: 3 },
  ];
  assert.equal(dealMinStartWordsFor(1, ranges), 2);
  assert.equal(dealMinStartWordsFor(120, ranges), 2);
  assert.equal(dealMinStartWordsFor(121, ranges), 1);
  assert.equal(dealMinStartWordsFor(300, ranges), 1);
  assert.equal(dealMinStartWordsFor(301, ranges), 3);
  // уровень раньше первой строки — историческая раздача
  assert.equal(dealMinStartWordsFor(5, [{ from: 100, minStartWords: 3 }]), 1);
});
