/**
 * Очередь линий: крупный уровень открывает категории волнами.
 *
 * Правило (владелец продукта, 04.08): на уровне больше 12 категорий четыре из
 * них не показываются со старта и выходят на поле по прогрессу. Причина
 * арифметическая — поле держит 24 пузыря, категория собирается из четырёх, и
 * тринадцать живых линий одновременно означают поле, на котором собрать нельзя
 * ничего: пачка досыпки в 4 шара расходится по четырём разным категориям.
 *
 * Проверяется весь путь целиком, потому что участников четверо и разъехаться
 * они могут молча:
 *   генератор  — гейты посчитаны и лежат в спеке, старт их не выкладывает;
 *   симулятор   — пузырь закрытой линии на поле не появляется раньше порога;
 *   приёмка     — уровень без очереди линий не проходит, вскрытый гейт видно;
 *   прототип    — `nextQueueIndex` в site/playable/index.html пропускает закрытые
 *                 линии; это обычный HTML, tsc его не проверяет.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { LevelCategory, LevelSpec, Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import {
  QUEUE_STAGING_FROM, STAGED_CATEGORIES, buildDeal, checkDeal, dealForSpec,
} from '../web/src/core/deal.ts';
import { BOARD_CAPACITY } from '../web/src/core/levelMath.ts';
import { createPlaySim } from '../web/src/core/playSim.ts';
import { simulatePlayability } from '../web/src/core/simulatePlayability.ts';
import { validateLevel } from '../web/src/core/validator.ts';
import { generateBlock, toGameJson } from '../web/src/core/generateBlock.ts';
import { buildHandoffPack } from '../web/src/core/playableHandoff.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import { buildSpec, levelCategory, word } from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const BOARD = { boardCapacity: BOARD_CAPACITY, wordsPerCategory: 4 };

/** Категории-заглушки: сколько нужно, все «чистые» и разные. */
function manyCategories(n: number): LevelCategory[] {
  return Array.from({ length: n }, (_, i) => levelCategory(`cat${i}`, `CAT ${i}`, [
    word(`w${i}a`, 4.5), word(`w${i}b`, 4.4), word(`w${i}c`, 4.3), word(`w${i}d`, 4.2),
  ]));
}

// --------------------------------------------------------------------------- //
// генератор
// --------------------------------------------------------------------------- //

test('уровень до 12 категорий гейтов не получает вовсе', () => {
  for (const n of [8, 12]) {
    const categories = manyCategories(n);
    const withHold = buildDeal(400, categories, BOARD, new Set(), 2, null, null,
      STAGED_CATEGORIES);
    const without = buildDeal(400, categories, BOARD, new Set(), 2, null, null, 0);
    assert.equal(withHold.gates, undefined, `${n} категорий: гейты не нужны`);
    // и выкладка обязана остаться байт в байт той же: просьба «отложи четыре»
    // на маленьком уровне ничего не меняет
    assert.deepEqual(withHold, without, `${n} категорий: выкладка изменилась`);
  }
});

test('на уровне больше 12 категорий четыре линии ждут прогресса', () => {
  for (const n of [QUEUE_STAGING_FROM, 15, 18]) {
    const categories = manyCategories(n);
    const deal = buildDeal(401, categories, BOARD, new Set(), 2, null, null,
      STAGED_CATEGORIES);
    const gates = deal.gates ?? [];
    assert.equal(gates.length, STAGED_CATEGORIES,
      `${n} категорий: за гейтом ${gates.length} линий, ожидалось ${STAGED_CATEGORIES}`);

    // пороги строго возрастают и лежат внутри уровня: линия, открывающаяся
    // после победы, — это не отложенная линия, а потерянная
    const thresholds = gates.map((g) => g.afterCollected);
    for (let i = 1; i < thresholds.length; i += 1) {
      assert.ok(thresholds[i] > thresholds[i - 1],
        `${n} категорий: пороги ${thresholds.join(',')} не возрастают`);
    }
    assert.ok(thresholds[0] >= 1 && thresholds[thresholds.length - 1] < n,
      `${n} категорий: пороги ${thresholds.join(',')} вне 1..${n - 1}`);

    // ни одного пузыря отложенной линии на старте
    const gated = new Set(gates.map((g) => g.category));
    const onStart = deal.start.filter((b) => gated.has(b.category));
    assert.deepEqual(onStart, [], `${n} категорий: на старте пузыри закрытых линий`);

    // и ни одного потерянного слова: очередь по-прежнему раздаёт всё
    const words = [...deal.start, ...deal.queue];
    assert.equal(words.length, n * 4,
      `${n} категорий: роздано ${words.length} слов из ${n * 4}`);
  }
});

test('очередь линий воспроизводится из одного спека', () => {
  const spec = stagedSpec(16);
  assert.ok((spec.deal.gates ?? []).length > 0, 'фикстура без гейтов');
  assert.deepEqual(dealForSpec(spec), spec.deal,
    'пересчёт выкладки из спека дал другие гейты или другой порядок');
  assert.deepEqual(checkDeal(spec, spec.deal), [], 'выкладка с гейтами не сходится');
});

test('пузырь закрытой линии на старте — претензия приёмки', () => {
  const spec = stagedSpec(16);
  const gated = spec.deal.gates![0].category;
  const broken: LevelSpec = {
    ...spec,
    deal: {
      ...spec.deal,
      start: [...spec.deal.start, { word: 'w0a', category: gated }],
    },
  };
  const problems = checkDeal(broken, broken.deal);
  assert.ok(problems.some((p) => p.includes('за гейтом')),
    `ожидалась претензия про гейт, получено: ${problems.join('; ')}`);
});

// --------------------------------------------------------------------------- //
// симулятор партии
// --------------------------------------------------------------------------- //

test('симулятор не выпускает закрытую линию на поле раньше порога', () => {
  const spec = stagedSpec(16);
  const gateOf = new Map(spec.deal.gates!.map((g) => [g.category, g.afterCollected]));
  const sim = createPlaySim(spec);

  let guard = 5000;
  while (!sim.won() && guard > 0) {
    guard -= 1;
    // ни один пузырь на поле не принадлежит линии, чей порог ещё не пройден
    for (const bubble of sim.field) {
      const need = gateOf.get(bubble.category);
      if (need === undefined) continue;
      assert.ok(sim.categoriesDone() >= need,
        `${bubble.category} на поле при ${sim.categoriesDone()} сборах, `
        + `порог ${need}`);
    }
    const pairs = sim.legalPairs();
    if (pairs.length === 0) { if (sim.rescue() !== null) continue; break; }
    const field = sim.field;
    const completing = pairs.find(([i, j]) => field[i].halfPair === 0
      && field[i].words.length + field[j].words.length === sim.fullOf(field[i].category));
    const pick = completing ?? pairs[0];
    sim.attempt(pick[0], pick[1]);
  }
  assert.ok(sim.won(), 'уровень с гейтами не доигрался: очередь линий заперла поле');
  assert.equal(sim.stats().gatesForced, 0,
    'досыпке пришлось вскрывать гейт: очередь и пороги разъехались');
});

test('крупные уровни пресета проходятся, не вскрывая гейтов', () => {
  const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
  const big = block.levels.filter((l) => l.spec.categories.length >= QUEUE_STAGING_FROM);
  assert.ok(big.length >= 5, `крупных уровней в пресете ${big.length}, ожидалось больше`);
  for (const level of big) {
    const gates = level.spec.deal.gates ?? [];
    assert.equal(gates.length, STAGED_CATEGORIES,
      `уровень ${level.spec.levelId}: линий за гейтом ${gates.length}`);
    const play = simulatePlayability(level.spec);
    assert.ok(play.winnable, `уровень ${level.spec.levelId}: ${play.failReason}`);
    assert.equal(play.gatesForced, 0,
      `уровень ${level.spec.levelId}: гейт вскрыт ${play.gatesForced} раз`);
  }
});

// --------------------------------------------------------------------------- //
// приёмка
// --------------------------------------------------------------------------- //

test('крупный уровень без очереди линий не проходит QUEUE_STAGED', () => {
  const spec = stagedSpec(16);
  const index = new ContentIndex(snapshot);
  const stripped: LevelSpec = {
    ...spec,
    deal: { start: spec.deal.start, queue: spec.deal.queue },
  };
  const issues = validateLevel(stripped, { index }).issues;
  const staged = issues.find((i) => i.code === 'QUEUE_STAGED');
  assert.ok(staged, 'проверка QUEUE_STAGED не сработала');
  assert.equal(staged!.severity, 'hard');

  // а уровень С очередью её проходит
  const ok = validateLevel(spec, { index }).issues
    .find((i) => i.code === 'QUEUE_STAGED');
  assert.equal(ok, undefined, 'уровень с очередью линий забракован');
});

// --------------------------------------------------------------------------- //
// экспорт: пакет прототипа и игровой JSON
// --------------------------------------------------------------------------- //

test('гейты уезжают и в пакет прототипа, и в игровой JSON', () => {
  const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
  const pack = buildHandoffPack(block);
  let checked = 0;
  for (const level of block.levels) {
    const gates = level.spec.deal.gates ?? [];
    const inPack = pack.levels.find((l) => l.level_id === level.spec.levelId)!.deal.gates;
    const inGame = (toGameJson(level.spec) as { deal: { gates?: unknown[] } }).deal.gates;
    if (gates.length === 0) {
      assert.equal(inPack, undefined, `уровень ${level.spec.levelId}: гейтов нет, а в пакете есть`);
      assert.equal(inGame, undefined, `уровень ${level.spec.levelId}: гейтов нет, а в JSON есть`);
      continue;
    }
    checked += 1;
    assert.deepEqual(inPack, gates.map((g) => ({
      category: g.category, after_collected: g.afterCollected,
    })), `уровень ${level.spec.levelId}: пакет отдаёт другие гейты`);
    assert.deepEqual(inGame, inPack, `уровень ${level.spec.levelId}: JSON и пакет разошлись`);
    // категория гейта обязана быть в списке категорий пакета: прототип ищет её
    // по id, и незнакомый ключ он молча пропустит
    const ids = new Set(pack.levels.find((l) => l.level_id === level.spec.levelId)!
      .categories.map((c) => c.id));
    for (const g of gates) {
      assert.ok(ids.has(g.category),
        `уровень ${level.spec.levelId}: гейт ссылается на ${g.category}, которого нет в пакете`);
    }
  }
  assert.ok(checked >= 5, `уровней с гейтами в пакете ${checked}`);
});

// --------------------------------------------------------------------------- //
// прототип: его собственный код
// --------------------------------------------------------------------------- //

/**
 * Правило исполняет прототип, а не инструмент, и tsc его HTML не читает.
 * Поэтому функция выбора шара из очереди берётся прямо из файла и выполняется
 * здесь: разъехаться с симулятором она может молча, и тогда наигровка руками
 * проверяет не тот уровень, который прошёл приёмку.
 */
function prototypeNextIndex(): (
  gates: Record<string, number> | null, queue: { v: string }[], done: number,
) => number {
  const html = readFileSync(join(ROOT, '../../site/playable/index.html'), 'utf8');
  const start = html.indexOf('function nextQueueIndex(');
  assert.ok(start >= 0, 'в прототипе нет функции nextQueueIndex');
  let depth = 0;
  let end = html.indexOf('{', start);
  for (let k = end; k < html.length; k += 1) {
    if (html[k] === '{') depth += 1;
    else if (html[k] === '}') { depth -= 1; if (depth === 0) { end = k; break; } }
  }
  const body = html.slice(start, end + 1);
  return new Function('gates', 'queue', 'done',
    `const GATES=gates; const console={warn(){}};\n${body}\nreturn nextQueueIndex();`) as
    ReturnType<typeof prototypeNextIndex>;
}

test('прототип пропускает закрытые линии и берёт первую открытую', () => {
  const next = prototypeNextIndex();
  const queue = [{ v: 'LATE' }, { v: 'ALSO LATE' }, { v: 'OPEN' }, { v: 'LATE' }];
  const gates = { LATE: 5, 'ALSO LATE': 3 };
  assert.equal(next(gates, queue, 0), 2, 'при нуле сборов открыта только OPEN');
  assert.equal(next(gates, queue, 3), 1, 'после 3 сборов открывается ALSO LATE');
  assert.equal(next(gates, queue, 5), 0, 'после 5 сборов очередь идёт по порядку');
  // без гейтов поведение прежнее: берётся голова очереди
  assert.equal(next(null, queue, 0), 0, 'уровень без гейтов обязан играться как раньше');
});

test('прототип вскрывает ближайший гейт, когда открытых линий не осталось', () => {
  const next = prototypeNextIndex();
  // в очереди только закрытые линии: поле важнее расписания, иначе досыпка
  // не придёт вовсе и игрок останется перед мёртвым полем
  const queue = [{ v: 'FAR' }, { v: 'NEAR' }];
  assert.equal(next({ FAR: 9, NEAR: 4 }, queue, 1), 1,
    'вскрывать надо линию, которой до открытия ближе всех');
});

/** Спек на N категорий с очередью линий: та же дорога, что у генератора. */
function stagedSpec(n: number): LevelSpec {
  const categories = manyCategories(n);
  const spec = buildSpec(402, categories);
  spec.board.dealMinStartWords = 2;
  spec.board.dealHoldCategories = STAGED_CATEGORIES;
  spec.deal = dealForSpec(spec);
  return spec;
}
