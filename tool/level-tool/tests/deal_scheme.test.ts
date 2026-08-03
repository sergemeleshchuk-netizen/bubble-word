/**
 * Явная схема выкладки и таблица декад (core/deal.ts, core/decadeProfiles.ts).
 *
 * Закреплено:
 *  1) авто-превью повторяет медианную схему замера оригинала (M=9 →
 *     4-3-3-3-3-2-2-2-2 — таблица разбора 02.08);
 *  2) явная схема применяется как написано: доли по убыванию, категории за
 *     пределами схемы в очереди, одиночки допустимы, если заданы;
 *  3) схема записывается в спек, входит в конфиг-хеш и воспроизводится из
 *     одного спека;
 *  4) checkDeal при схеме не требует точного заполнения поля (в референсе
 *     старт тоже плавает, 19-24), но полноту слов проверяет по-прежнему;
 *  5) applyDecadeTuning: правка коридора подрезает план категорий, отмена
 *     схемы (null) стирает её из конфига;
 *  6) разбор строки схемы: формат «4-3-3-3-2-2-2-2-1».
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { LevelSpec, Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { checkDeal, dealForSpec, resolveScheme } from '../web/src/core/deal.ts';
import {
  applyDecadeTuning, configForRange, decadeTuningDefaults, decadeTuningRowFor,
  formatScheme, liteSchemePreview, parseScheme,
} from '../web/src/core/decadeProfiles.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/lexicon.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const SCHEME = [4, 3, 3, 3, 2, 2, 2, 2, 1];

function startCounts(spec: LevelSpec): number[] {
  const counts = new Map<string, number>();
  for (const b of spec.deal.start) {
    counts.set(b.category, (counts.get(b.category) ?? 0) + 1);
  }
  return [...counts.values()].sort((a, b) => b - a);
}

// --------------------------------------------------------------------------- //
// авто-превью
// --------------------------------------------------------------------------- //

test('авто-превью M=9 — медианная схема замера оригинала', () => {
  assert.deepEqual(liteSchemePreview(9), [4, 3, 3, 3, 3, 2, 2, 2, 2]);
});

test('авто-превью на больших M — без одиночек, лишние категории в очереди', () => {
  const scheme = liteSchemePreview(14);
  assert.ok(scheme.every((n) => n >= 2), `в авто-схеме есть одиночка: ${scheme}`);
  assert.equal(scheme.reduce((a, b) => a + b, 0), 24);
});

// --------------------------------------------------------------------------- //
// явная схема в генерации
// --------------------------------------------------------------------------- //

const config = {
  ...configForRange([121, 130], 'deal-scheme-test'),
  dealScheme: SCHEME,
};
const block = generateBlock({ snapshot, scoring, config });

test('схема записана в спек и входит в выкладку', () => {
  assert.ok(block.levels.length >= 8, `декада собралась на ${block.levels.length}/10`);
  for (const level of block.levels) {
    assert.deepEqual(level.spec.board.dealScheme, SCHEME,
      `уровень ${level.spec.levelId}: схема не записана в спек`);
  }
});

test('доли старта следуют схеме: не крупнее заявленных, одиночки допустимы', () => {
  for (const level of block.levels) {
    const counts = startCounts(level.spec);
    // каждая i-я доля не может превышать i-ю долю схемы: схема — потолок
    // формы (меньше бывает: у мета-родителя спавнится 3 слова, бюджет конечен)
    counts.forEach((n, i) => {
      assert.ok(i < SCHEME.length,
        `уровень ${level.spec.levelId}: на старте больше категорий, чем в схеме`);
      assert.ok(n <= SCHEME[i],
        `уровень ${level.spec.levelId}: доля ${i} равна ${n} при схеме ${SCHEME[i]}`);
    });
  }
});

test('одиночка из схемы реально появляется хотя бы на части уровней', () => {
  const withSingle = block.levels.filter((l) => startCounts(l.spec).includes(1));
  assert.ok(withSingle.length > 0,
    'схема с «1» не дала ни одной одиночки — схема не применяется');
});

test('выкладка по схеме сходится по словам и воспроизводится из спека', () => {
  for (const level of block.levels) {
    assert.deepEqual(checkDeal(level.spec, level.spec.deal), [],
      `уровень ${level.spec.levelId}: выкладка не сходится`);
    assert.deepEqual(dealForSpec(level.spec), level.spec.deal,
      `уровень ${level.spec.levelId}: выкладка не воспроизводится из спека`);
  }
});

test('схема меняет хеш пакета относительно авто-раздачи', () => {
  const auto = generateBlock({ snapshot, scoring,
    config: configForRange([121, 130], 'deal-scheme-test') });
  assert.notEqual(block.packHash, auto.packHash);
});

// --------------------------------------------------------------------------- //
// таблица декад
// --------------------------------------------------------------------------- //

test('правка коридора подрезает план категорий', () => {
  const base = configForRange([121, 130], 'deal-scheme-test');
  const rows = decadeTuningDefaults().map((r) =>
    (r.from === 121 ? { ...r, corridor: [10, 12] as [number, number] } : r));
  const tuned = applyDecadeTuning(base, rows);
  assert.deepEqual(tuned.categoryCorridor, [10, 12]);
  assert.ok(tuned.categoryPlan!.every((n) => n >= 10 && n <= 12),
    `план вышел за коридор: ${tuned.categoryPlan}`);
});

test('отмена схемы в таблице стирает её из конфига', () => {
  const base = { ...configForRange([121, 130], 'x'), dealScheme: SCHEME };
  const tuned = applyDecadeTuning(base, decadeTuningDefaults());
  assert.equal(tuned.dealScheme, undefined);
  assert.equal(tuned.dealSchemeRange, undefined);
});

test('нетронутая таблица не меняет конфиг декады', () => {
  const base = configForRange([61, 70], 'deal-scheme-test');
  const tuned = applyDecadeTuning(base, decadeTuningDefaults());
  assert.deepEqual(tuned.categoryCorridor, base.categoryCorridor);
  assert.deepEqual(tuned.categoryPlan, base.categoryPlan);
  assert.equal(tuned.dealScheme, undefined);
  assert.equal(tuned.dealSchemeRange, undefined);
});

test('сетка умолчаний: до 100 по 10, до 200 по 20, до 1000 по 100, до 5000 по 1000', () => {
  const rows = decadeTuningDefaults();
  assert.equal(rows.length, 27);
  assert.deepEqual(rows.slice(0, 2).map((r) => [r.from, r.to]), [[1, 10], [11, 20]]);
  assert.deepEqual(rows[10] && [rows[10].from, rows[10].to], [101, 120]);
  assert.deepEqual(rows[15] && [rows[15].from, rows[15].to], [201, 300]);
  assert.deepEqual(rows[26] && [rows[26].from, rows[26].to], [4001, 5000]);
  // строка находится и для уровня глубоко за пределами замера
  assert.equal(decadeTuningRowFor(4321, rows)?.from, 4001);
});

test('вилка схем из таблицы уезжает в конфиг и заполняется с одной стороны', () => {
  const rows = decadeTuningDefaults().map((r) =>
    (r.from === 121 ? { ...r, schemeMin: [4, 3, 3, 2], schemeMax: null } : r));
  const tuned = applyDecadeTuning(configForRange([121, 130], 'x'), rows);
  assert.deepEqual(tuned.dealSchemeRange, { min: [4, 3, 3, 2], max: [4, 3, 3, 2] });
});

// --------------------------------------------------------------------------- //
// вилка схем: resolveScheme
// --------------------------------------------------------------------------- //

const FORK_MIN = [4, 3, 3, 3, 2, 1];      // 16 слов
const FORK_MAX = [4, 4, 3, 3, 3, 2, 1];   // 20 слов

test('края вилки: минимум категорий — схема min, максимум — схема max', () => {
  assert.deepEqual(resolveScheme(FORK_MIN, FORK_MAX, 5, [5, 10]), FORK_MIN.slice(0, 5));
  assert.deepEqual(resolveScheme(FORK_MIN, FORK_MAX, 10, [5, 10]), FORK_MAX);
});

test('середина вилки: число стартовых слов интерполируется', () => {
  const mid = resolveScheme(FORK_MIN, FORK_MAX, 7, [5, 10]);
  const words = mid.reduce((a, b) => a + b, 0);
  assert.ok(words > 16 && words < 20, `стартовых слов ${words}, ждали между 16 и 20`);
  // каждая доля в пределах вилки
  mid.forEach((n, i) => {
    assert.ok(n <= FORK_MAX[i], `доля ${i} = ${n} выше максимума ${FORK_MAX[i]}`);
  });
});

test('вилка в генерации: разрешённая схема записана в спек и следует M уровня', () => {
  const config = {
    ...configForRange([121, 130], 'deal-fork-test'),
    dealSchemeRange: { min: FORK_MIN, max: FORK_MAX },
  };
  const forkBlock = generateBlock({ snapshot, scoring, config });
  assert.ok(forkBlock.levels.length >= 8, `собрано ${forkBlock.levels.length}/10`);
  for (const level of forkBlock.levels) {
    const m = level.spec.categories.length;
    const expected = resolveScheme(FORK_MIN, FORK_MAX, m, config.categoryCorridor);
    assert.deepEqual(level.spec.board.dealScheme, expected,
      `уровень ${level.spec.levelId} (M=${m}): схема в спеке не совпала с вилкой`);
    assert.deepEqual(dealForSpec(level.spec), level.spec.deal,
      `уровень ${level.spec.levelId}: выкладка не воспроизводится из спека`);
  }
});

// --------------------------------------------------------------------------- //
// разбор строки схемы
// --------------------------------------------------------------------------- //

test('строка схемы разбирается и нормализуется по убыванию', () => {
  assert.deepEqual(parseScheme('4-3-3-3-2-2-2-2-1'), SCHEME);
  assert.deepEqual(parseScheme('2 3 4'), [4, 3, 2]);
  assert.equal(parseScheme(''), null);
  assert.equal(parseScheme('4-5-3'), undefined);
  assert.equal(parseScheme('abc'), undefined);
  assert.equal(formatScheme(SCHEME), '4-3-3-3-2-2-2-2-1');
});
