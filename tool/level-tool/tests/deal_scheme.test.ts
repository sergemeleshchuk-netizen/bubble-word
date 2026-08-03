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
import { checkDeal, dealForSpec } from '../web/src/core/deal.ts';
import {
  applyDecadeTuning, configForRange, decadeTuningDefaults, formatScheme,
  liteSchemePreview, parseScheme,
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
});

test('нетронутая таблица не меняет конфиг декады', () => {
  const base = configForRange([61, 70], 'deal-scheme-test');
  const tuned = applyDecadeTuning(base, decadeTuningDefaults());
  assert.deepEqual(tuned.categoryCorridor, base.categoryCorridor);
  assert.deepEqual(tuned.categoryPlan, base.categoryPlan);
  assert.equal(tuned.dealScheme, undefined);
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
