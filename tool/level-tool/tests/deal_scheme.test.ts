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
 *  5) applyDecadeTuning: правка коридора ПЕРЕСОБИРАЕТ план категорий, отмена
 *     схемы (null) стирает её из конфига;
 *  6) разбор строки схемы: формат «4-3-3-3-2-2-2-2-1»;
 *  7) шары-слова на старте: умолчания сняты с записанных уровней (L1-10 —
 *     16-20, L11-20 — 20-24, дальше 24), потолок реально подрезает старт, пол
 *     проверяется приёмкой выкладки;
 *  8) поздние коридоры (решение 03.08): потолок 12 до 1000, дальше 13-14-15,
 *     пол опущен до 8-9 ради уровней передышки, и ни одна декада за 200-м
 *     не повторяет план соседней.
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
  applyDecadeTuning, configForRange, dealStartBubblesFor, decadeTuningDefaults,
  decadeTuningRowFor, formatScheme, liteSchemePreview, parseScheme, spreadBoundsFor,
} from '../web/src/core/decadeProfiles.ts';
import { buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import { BOARD_CAPACITY } from '../web/src/core/levelMath.ts';

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

/*
 * Требование владельца продукта 03.08: на старте нет одиночек, двоек мало,
 * троек и четвёрок много. Схема 4-3-3-3-3-3-3-2 — прямое следствие: вход
 * четвёркой, дальше тройки (им до сбора не хватает одного слова), остаток —
 * одна пара. Прежнее умолчание 4-3-3-3-3-2-2-2-2 держало на поле четыре пары,
 * ни одна из которых не собиралась пачкой досыпки.
 */
test('авто-превью M=9 — глубина вместо ширины: четвёрка, тройки, одна пара', () => {
  assert.deepEqual(liteSchemePreview(9), [4, 3, 3, 3, 3, 3, 3, 2]);
});

test('авто-превью на больших M — без одиночек, лишние категории в очереди', () => {
  const scheme = liteSchemePreview(14);
  assert.ok(scheme.every((n) => n >= 2), `в авто-схеме есть одиночка: ${scheme}`);
  assert.equal(scheme.reduce((a, b) => a + b, 0), 24);
  const deep = scheme.filter((n) => n >= 3).length;
  const shallow = scheme.filter((n) => n === 2).length;
  assert.ok(deep > shallow, `троек и четвёрок ${deep}, пар ${shallow}: ${scheme}`);
});

test('авто-превью на малых M — все категории видны целиком', () => {
  assert.deepEqual(liteSchemePreview(5), [4, 4, 4, 4, 4]);
  assert.deepEqual(liteSchemePreview(7), [4, 4, 4, 3, 3, 3, 3]);
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

/*
 * Требование владельца 03.08: «4 это 4, а половинки в разных досыпках и мета
 * не должны нарушать». Схема — инструмент дизайнера, а не пожелание: доля
 * отдаётся категории, которая её реально держит (best-fit в buildDeal), поэтому
 * мета-родитель с тремя спавнящимися словами больше не превращает четвёрку
 * схемы в тройку. Проверяем буквально: выложенные доли совпадают с началом
 * схемы, а не «не крупнее» её.
 */
test('доли старта исполняются буквально: 4 в схеме — четыре слова на поле', () => {
  for (const level of block.levels) {
    const counts = startCounts(level.spec);
    assert.ok(counts.length <= SCHEME.length,
      `уровень ${level.spec.levelId}: на старте больше категорий, чем в схеме`);
    assert.deepEqual(counts, SCHEME.slice(0, counts.length),
      `уровень ${level.spec.levelId}: выложено ${counts.join('-')} `
      + `при схеме ${SCHEME.join('-')}`);
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

test('правка коридора пересобирает план категорий, а не подрезает его в линию', () => {
  const base = configForRange([121, 130], 'deal-scheme-test');
  const rows = decadeTuningDefaults().map((r) =>
    (r.from === 121 ? { ...r, corridor: [10, 12] as [number, number] } : r));
  const tuned = applyDecadeTuning(base, rows);
  assert.deepEqual(tuned.categoryCorridor, [10, 12]);
  const plan = tuned.categoryPlan!;
  assert.ok(plan.every((n) => n >= 10 && n <= 12), `план вышел за коридор: ${plan}`);
  /*
   * Главное в этой проверке — не коридор, а то, что план остался планом.
   * Замеренное среднее декады 121-130 равно 13.2, то есть выше нового потолка;
   * прежняя подрезка давала десять двенадцаток — прямую линию из структурно
   * одинаковых уровней. Пересборка обязана дать и пилу, и передышку.
   */
  assert.equal(new Set(plan).size > 1, true, `план стал прямой линией: ${plan}`);
  assert.ok(plan.slice(1).every((n, i) => n !== plan[i]),
    `в плане есть структурно одинаковые соседи: ${plan}`);
  assert.ok(checkBlockRhythm(buildBlockPlan(tuned), tuned.categoryCorridor).passed,
    'пересобранный план не прошёл проверку ритма');
});

test('разброс требуется по ширине коридора: в узком пила физически меньше', () => {
  assert.deepEqual(spreadBoundsFor([11, 18]), [5, 7]);   // широкий — правило референса
  assert.deepEqual(spreadBoundsFor([8, 12]), [4, 4]);    // ширина 4: разброс 5 недостижим
  assert.deepEqual(spreadBoundsFor([9, 12]), [3, 3]);
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

// --------------------------------------------------------------------------- //
// шары-слова на старте
// --------------------------------------------------------------------------- //

/*
 * Числа — замер `obs.startBubbles` записанных уровней: L1-10 стартуют с 16-24
 * пузырей, L11-20 с 18-24, дальше выгрузка старта не содержит и поле уже полное.
 * Потолок первой декады опущен до 20: полные 24 в оригинале появляются на L7-L9,
 * то есть в верхней половине декады.
 */
test('умолчание шаров на старте: 16-20, потом 20-24, дальше всегда 24', () => {
  assert.deepEqual(dealStartBubblesFor(1), [16, 20]);
  assert.deepEqual(dealStartBubblesFor(7), [16, 20]);
  assert.deepEqual(dealStartBubblesFor(11), [20, 24]);
  assert.deepEqual(dealStartBubblesFor(21), [24, 24]);
  assert.deepEqual(dealStartBubblesFor(500), [24, 24]);
  assert.deepEqual(dealStartBubblesFor(4321), [24, 24]);
  for (const row of decadeTuningDefaults()) {
    assert.ok(row.startBubbles[0] <= row.startBubbles[1]
      && row.startBubbles[1] <= BOARD_CAPACITY,
      `строка ${row.from}: бюджет ${row.startBubbles} вне шкалы`);
  }
});

test('бюджет старта подрезает поле первой декады и держится пола', () => {
  const cfg = configForRange([1, 10], 'start-budget-test');
  assert.deepEqual(cfg.dealStartBubbles, [16, 20]);
  const early = generateBlock({ snapshot, scoring, config: cfg });
  assert.ok(early.levels.length >= 8, `декада собралась на ${early.levels.length}/10`);
  for (const level of early.levels) {
    const start = level.spec.deal.start.length;
    assert.ok(start >= 16 && start <= 20,
      `уровень ${level.spec.levelId}: на старте ${start} пузырей, бюджет 16-20`);
    // вместимость поля физическая и не двигается: подрезан старт, а не поле
    assert.equal(level.spec.board.boardCapacity, BOARD_CAPACITY);
    assert.deepEqual(level.spec.board.dealStartBubbles, [16, 20]);
    assert.deepEqual(checkDeal(level.spec, level.spec.deal), [],
      `уровень ${level.spec.levelId}: выкладка не сходится`);
    assert.deepEqual(dealForSpec(level.spec), level.spec.deal,
      `уровень ${level.spec.levelId}: выкладка не воспроизводится из спека`);
  }
});

test('первый уровень остаётся туториалом: весь уровень видно на старте', () => {
  const early = generateBlock({ snapshot, scoring,
    config: configForRange([1, 10], 'start-budget-test') });
  const first = early.levels.find((l) => l.spec.levelId === 1);
  assert.ok(first, 'уровня 1 в блоке нет');
  assert.equal(first!.spec.deal.queue.length, 0,
    'на туториале очередь досыпки обязана быть пустой');
  assert.equal(first!.spec.deal.start.length,
    first!.spec.categories.length * first!.spec.board.wordsPerCategory);
});

test('бюджет «до 24» ничего не подрезает и в спек не пишется', () => {
  const cfg = configForRange([21, 30], 'start-budget-test');
  assert.deepEqual(cfg.dealStartBubbles, [24, 24]);
  const block = generateBlock({ snapshot, scoring, config: cfg });
  for (const level of block.levels) {
    assert.equal(level.spec.board.dealStartBubbles, undefined,
      `уровень ${level.spec.levelId}: в спек уехал бюджет, который ничего не меняет`);
  }
});

// --------------------------------------------------------------------------- //
// коридоры поздней кривой
// --------------------------------------------------------------------------- //

/*
 * Решение владельца 03.08. До него таблица показывала на всём отрезке от 161 до
 * 5000 одно и то же «11-17» — потолок выше самого оригинала (медиана выгрузки на
 * 201-1000 равна ровно 12) и пол 11, не оставляющий места уровню передышки.
 */
test('поздние коридоры: потолок оригинала до 1000, выше него — только после', () => {
  const rows = decadeTuningDefaults();
  const at = (level: number) => decadeTuningRowFor(level, rows)!.corridor;
  assert.deepEqual(at(161), [8, 12]);
  assert.deepEqual(at(450), [8, 12]);
  assert.deepEqual(at(501), [9, 12]);
  assert.deepEqual(at(1000), [9, 12]);
  assert.deepEqual(at(1001), [9, 13]);
  assert.deepEqual(at(2001), [8, 14]);
  assert.deepEqual(at(3001), [9, 15]);
  assert.deepEqual(at(4321), [9, 15]);
  // до 1000 потолок не выше замеренного оригинала, пол оставляет передышку
  for (const row of rows) {
    if (row.from < 161) continue;
    if (row.to <= 1000) assert.ok(row.corridor[1] <= 12, `строка ${row.from}: потолок выше 12`);
    assert.ok(row.corridor[0] <= 9, `строка ${row.from}: пол ${row.corridor[0]} без передышки`);
  }
  // строки 1-160 остались замером: их трогать было нечем, они сняты с уровней
  assert.deepEqual(at(1), [5, 12]);
  assert.deepEqual(at(11), [7, 12]);
  assert.deepEqual(at(121), [10, 17]);
});

test('каждая строка таблицы даёт живой ритм с передышкой', () => {
  const rows = decadeTuningDefaults();
  for (const row of rows) {
    const cfg = applyDecadeTuning(
      configForRange([row.from, row.from + 9], 'rows-rhythm'), rows);
    const plans = buildBlockPlan(cfg);
    const rhythm = checkBlockRhythm(plans, cfg.categoryCorridor);
    assert.ok(rhythm.passed,
      `строка ${row.from}-${row.to} (коридор ${cfg.categoryCorridor.join('-')}): `
      + rhythm.issues.join('; '));
    const counts = plans.map((p) => p.categoryCount);
    assert.ok(counts[5] < counts[4],
      `строка ${row.from}: нет передышки после спайка (${counts.join(',')})`);
  }
});

/*
 * Ритм сеялся номером ПРОФИЛЯ декады, а профиль за 191-м один на всю кривую —
 * поэтому блоки 201-210 и 4991-5000 получали побайтно один и тот же план.
 * Разнообразие поздней кривой начинается здесь, а не в коридоре.
 */
test('декады за 200-м не повторяют план друг друга', () => {
  const rows = decadeTuningDefaults();
  const plans = [201, 211, 301, 501, 1001, 2001, 4991].map((from) => {
    const cfg = applyDecadeTuning(configForRange([from, from + 9], 'late-variety'), rows);
    return cfg.categoryPlan!.join(',');
  });
  assert.equal(new Set(plans).size, plans.length,
    `совпали планы разных декад: ${plans.join(' | ')}`);
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
