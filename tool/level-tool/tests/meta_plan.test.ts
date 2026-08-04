/**
 * Мета-план декады: сколько мета-связей инструмент ПРОСИТ у генератора.
 *
 * Решение владельца 04.08: мета-пара — самый дорогой рычаг (пузырь-имя выглядит
 * обычным словом и принадлежит двум категориям), поэтому пять пар не нужны
 * нигде, четыре — только на спайке, а раз в две декады один уровень идёт совсем
 * без мета. Пока план брался случайным броском внутри замеренного коридора
 * декады, кривая жила на тройках-четвёрках, а у декад 31-40 и 91-100 доходило
 * до шести и семи.
 *
 * Тест держит именно форму плана, а не «красиво ли получилось»: форма — то, что
 * молча уползёт при следующей правке коридоров.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from '../web/src/core/blockPlan.ts';
import {
  EARLY_CURVE_UNTIL, META_MAX_EARLY, META_MAX_ORDINARY, META_MAX_SPIKE,
  META_ZERO_EVERY_DECADES,
  RECOVERY_POSITION, SPIKE_POSITION, checkDecadeFit, configForRange,
  metaCeilingFor, planMetaCounts, profileForRange,
} from '../web/src/core/decadeProfiles.ts';

/** Планы всех декад до 300-го уровня одним seed — на них и смотрим. */
const DECADES = Array.from({ length: 30 }, (_, i) => {
  const from = i * 10 + 1;
  const config = configForRange([from, from + 9], 'final-03');
  return { from, plan: config.metaPlan ?? [], categories: config.categoryPlan ?? [] };
});

// --------------------------------------------------------------------------- //
// потолок
// --------------------------------------------------------------------------- //

test('пятёрки нет нигде на кривой', () => {
  for (const { from, plan } of DECADES) {
    const over = plan.filter((n) => n > META_MAX_SPIKE);
    assert.equal(over.length, 0,
      `декада ${from}: план ${plan.join(',')} просит больше ${META_MAX_SPIKE} мета-пар`);
  }
});

test('четвёрка стоит только на спайке', () => {
  for (const { from, plan } of DECADES) {
    plan.forEach((count, i) => {
      if (i + 1 === SPIKE_POSITION) return;
      assert.ok(count <= META_MAX_ORDINARY,
        `декада ${from}, позиция ${i + 1}: ${count} мета-пар при потолке `
        + `${META_MAX_ORDINARY} на обычной позиции (план ${plan.join(',')})`);
    });
  }
});

test('потолок декады не выше её замера: у 1-10 спайк на двух парах, а не на четырёх', () => {
  // единственная декада, где референс мета почти не использует (metaRange 0-2)
  assert.equal(metaCeilingFor(profileForRange([1, 10]), SPIKE_POSITION), 2);
  // за ранней кривой работает проектный потолок: четвёрка спайку, тройка обычной
  const late = profileForRange([241, 250]);
  assert.equal(metaCeilingFor(late, SPIKE_POSITION, 241), META_MAX_SPIKE);
  assert.equal(metaCeilingFor(late, 1, 241), META_MAX_ORDINARY);
});

test('на первых двухстах уровнях потолок две мета-пары — и на спайке тоже', () => {
  for (const { from, plan } of DECADES) {
    if (from > EARLY_CURVE_UNTIL) continue;
    const over = plan.filter((n) => n > META_MAX_EARLY);
    assert.equal(over.length, 0,
      `декада ${from}: план ${plan.join(',')} просит больше ${META_MAX_EARLY} мета-пар, `
      + 'а ранняя кривая столько не выдерживает (замер слепым прогоном 04.08)');
  }
  // и это именно граница, а не «мета везде по две»: за 200-м спайк снова четвёрка
  const beyond = DECADES.filter((d) => d.from > EARLY_CURVE_UNTIL);
  assert.ok(beyond.some((d) => d.plan[SPIKE_POSITION - 1] > META_MAX_EARLY),
    'за ранней кривой спайк тоже подрезан — потолок перестал быть ранним');
});

// --------------------------------------------------------------------------- //
// низ: единицы и ноль
// --------------------------------------------------------------------------- //

test('в каждой декаде есть единицы — план не живёт на тройках', () => {
  for (const { from, plan } of DECADES) {
    assert.ok(plan.includes(1), `декада ${from}: в плане ${plan.join(',')} нет ни одной единицы`);
    const mean = plan.reduce((a, b) => a + b, 0) / plan.length;
    assert.ok(mean <= 2.2,
      `декада ${from}: среднее ${mean.toFixed(2)} мета-пар на уровень — это снова усложнение`);
  }
});

test('ноль на передышке — раз в две декады, и ровно один на декаду', () => {
  const withZero: number[] = [];
  for (const { from, plan } of DECADES) {
    const zeros = plan.filter((n) => n === 0).length;
    const tutorial = from === 1 ? 1 : 0;    // L1 без мета: в оригинале мета с L3
    if (plan[RECOVERY_POSITION - 1] === 0) {
      withZero.push(from);
      assert.equal(zeros, 1 + tutorial,
        `декада ${from}: нулей ${zeros}, а должен быть один (план ${plan.join(',')})`);
    } else {
      assert.equal(zeros, tutorial,
        `декада ${from}: ноль оказался не на передышке (план ${plan.join(',')})`);
    }
  }
  assert.equal(withZero.length, DECADES.length / META_ZERO_EVERY_DECADES,
    `уровень без мета встречается в декадах ${withZero.join(', ')} — это не раз в 20 уровней`);
  // и это именно каждая вторая декада, а не любые пятнадцать из тридцати
  assert.deepEqual(withZero, DECADES.filter((_, i) => i % META_ZERO_EVERY_DECADES === 0)
    .map((d) => d.from));
});

// --------------------------------------------------------------------------- //
// подрезки и воспроизводимость
// --------------------------------------------------------------------------- //

test('мета-пар не больше, чем имён категорий на уровне', () => {
  for (const { from, plan, categories } of DECADES) {
    plan.forEach((count, i) => {
      assert.ok(count <= categories[i] - 1,
        `декада ${from}, позиция ${i + 1}: ${count} мета-пар при ${categories[i]} категориях`);
    });
  }
});

test('тот же seed даёт тот же план, другой seed — другой порядок', () => {
  const profile = profileForRange([241, 250]);
  const categories = [14, 13, 12, 13, 16, 11, 15, 16, 13, 12];
  const again = planMetaCounts(profile, categories, 'final-03', false, 241);
  assert.deepEqual(again, planMetaCounts(profile, categories, 'final-03', false, 241));
  const other = planMetaCounts(profile, categories, 'other-seed', false, 241);
  // форма сохраняется, порядок обычных позиций — нет
  assert.equal(other[SPIKE_POSITION - 1], META_MAX_SPIKE);
  assert.deepEqual([...other].sort(), [...again].sort());
});

test('короткий блок без передышки: спайк съезжает на последнюю позицию', () => {
  const profile = profileForRange([241, 250]);
  const plan = planMetaCounts(profile, [12, 12, 12], 'final-03', false, 241);
  assert.equal(plan.length, 3);
  assert.equal(plan[2], META_MAX_SPIKE);
  assert.ok(plan.slice(0, 2).every((n) => n >= 1 && n <= META_MAX_ORDINARY));
});

// --------------------------------------------------------------------------- //
// путь без плана и пресет
// --------------------------------------------------------------------------- //

test('пустой план: вывод по роли держит тот же потолок', () => {
  const plan = buildBlockPlan({ ...DEFAULT_BLOCK_CONFIG, metaPlan: undefined });
  for (const level of plan) {
    const ceiling = level.role === 'peak' || level.role === 'spike'
      ? META_MAX_SPIKE : META_MAX_ORDINARY;
    assert.ok(level.metaCount <= ceiling,
      `уровень ${level.levelId} (${level.role}): ${level.metaCount} мета-пар при потолке ${ceiling}`);
  }
  assert.ok(plan.some((l) => l.metaCount === 0), 'ни одной передышки без мета');
  assert.ok(plan.some((l) => l.metaCount === 1), 'вывод по роли не даёт единиц');
});

test('пресет 201-210 приведён к тому же потолку: пятёрки на пике больше нет', () => {
  const plan = DEFAULT_BLOCK_CONFIG.metaPlan ?? [];
  assert.equal(plan.length, 10);
  assert.equal(Math.max(...plan), META_MAX_SPIKE);
  assert.equal(plan.filter((n) => n === META_MAX_SPIKE).length, 1);
  assert.equal(plan[SPIKE_POSITION - 1], META_MAX_SPIKE);
  assert.equal(plan[RECOVERY_POSITION - 1], 0);
  assert.ok(plan.includes(1));
});

// --------------------------------------------------------------------------- //
// приёмка декады
// --------------------------------------------------------------------------- //

/**
 * Вход приёмки, в котором интересны только мета-пары.
 *
 * Уровни берутся ЗА ранней кривой (241+): там работает проектный потолок 3/4, и
 * его видно отдельно от подрезки первых двухсот уровней.
 */
function fitInput(metaCounts: number[], firstLevel = 241) {
  return metaCounts.map((metaCount, i) => ({
    levelId: firstLevel + i,
    categoryCount: 13,
    zipfs: Array.from({ length: 52 }, () => 3.9),
    metaCount,
    metaDepth: metaCount > 0 ? 1 : 0,
    chainCount: 0,
    moveLimit: 50,
    startBubbles: 24,
    boardCapacity: 24,
    wordsPerCategory: 4,
  }));
}

const PROFILE_LATE = profileForRange([241, 250]);
const metaCheck = (counts: number[], firstLevel = 241) =>
  checkDecadeFit(fitInput(counts, firstLevel), PROFILE_LATE, undefined, counts.length)
    .checks.find((c) => c.code === 'META_RANGE')!;

test('приёмка пропускает план с нулями и единицами', () => {
  assert.equal(metaCheck([1, 2, 3, 2, 4, 0, 2, 3, 1, 1]).passed, true);
});

test('приёмка ловит четвёрку на обычной позиции', () => {
  const check = metaCheck([1, 2, 3, 4, 4, 0, 2, 3, 1, 1]);
  assert.equal(check.passed, false);
  assert.match(check.detail, /перебор на позициях 4/);
});

test('на ранней кривой приёмка ловит тройку — там потолок две пары', () => {
  const early = metaCheck([1, 2, 3, 2, 2, 0, 2, 1, 1, 1], 141);
  assert.equal(early.passed, false);
  assert.match(early.detail, /перебор на позициях 3/);
  // тот же план за ранней кривой законен
  assert.equal(metaCheck([1, 2, 3, 2, 2, 0, 2, 1, 1, 1]).passed, true);
});

test('приёмка ловит декаду, где мета не набралась вовсе', () => {
  const check = metaCheck([0, 0, 1, 0, 1, 0, 0, 0, 0, 0]);
  assert.equal(check.passed, false);
  assert.match(check.detail, /мета есть на 2 уровнях/);
});
