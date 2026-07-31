/**
 * Гейты, решение по которым принято на стороне контента.
 *
 * Инструмент не пересчитывает их сам: `derive-readiness` и `derive-conflicts`
 * посчитали готовность категорий и 517 запрещённых пар в базе, снимок их несёт,
 * генератор исполняет. Иначе одна и та же пара разрешена в базе и запрещена в
 * инструменте, и спорить будет нечем.
 *
 * Почему это отдельный файл тестов: до перехода на аудированную базу таких слоёв
 * в снимке не было вовсе, а неразделимые пары ловились живой эвристикой по
 * Жаккару — и только на калиброванных блоках.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import { loadContentIndex } from '../web/src/core/snapshot.ts';
import { emptyPackHistory, generateLevel } from '../web/src/core/generator.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { buildSpec, levelCategory, makeSnapshot, word } from './fixtures/synthetic.ts';
import { validateLevel } from '../web/src/core/validator.ts';
import { hashQuadruple } from '../web/src/core/generateBlock.ts';
import type { LevelPlan } from '../web/src/core/types.ts';

const CATEGORIES: Parameters<typeof makeSnapshot>[0] = [
  { key: 'colors', label: 'COLORS', theme: 'properties', words: [
    ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
    ['green', 4.8, 'approved'], ['yellow', 4.5, 'approved']] },
  { key: 'gemstones', label: 'GEMSTONES', theme: 'nature', words: [
    ['ruby', 4.0, 'approved'], ['opal', 3.6, 'approved'],
    ['topaz', 3.4, 'approved'], ['jade', 3.8, 'approved']] },
  { key: 'birthstones', label: 'BIRTHSTONES', theme: 'nature', words: [
    ['garnet', 3.2, 'approved'], ['pearl', 4.1, 'approved'],
    ['amethyst', 3.3, 'approved'], ['peridot', 2.9, 'approved']] },
  { key: 'tools', label: 'TOOLS', theme: 'tools', words: [
    ['hammer', 4.1, 'approved'], ['saw', 4.4, 'approved'],
    ['drill', 4.0, 'approved'], ['wrench', 3.5, 'approved']] },
  { key: 'weather', label: 'WEATHER', theme: 'nature', words: [
    ['rain', 5.1, 'approved'], ['snow', 4.9, 'approved'],
    ['wind', 4.8, 'approved'], ['fog', 4.0, 'approved']] },
  { key: 'opposites', label: 'OPPOSITES', theme: 'language', words: [
    ['hot', 4.9, 'approved'], ['cold', 4.9, 'approved'],
    ['up', 5.2, 'approved'], ['down', 5.2, 'approved']] },
];

function config(seed: string) {
  // окна свежести обнулены: тесты про гейты, а не про историю пакета
  return { ...DEFAULT_BLOCK_CONFIG, seed, categoryFreshnessWindow: 0, wordFreshnessWindow: 0 };
}

function plan(categoryCount: number): LevelPlan {
  return {
    levelId: 1, position: 1, role: 'entry', categoryCount,
    metaCount: 0, metaDepthTarget: 1, rareTarget: 0, trapTarget: 0,
    chainCount: 0, targetDifficulty: [1, 10], targetInterest: [1, 10], moveLimitK: 1.5,
  };
}

function generate(snapshot: ReturnType<typeof makeSnapshot>, categoryCount: number) {
  const index = loadContentIndex(snapshot);
  return generateLevel(index, plan(categoryCount), config('gates-test'), emptyPackHistory());
}

// --------------------------------------------------------------------------- //
// запреты пар
// --------------------------------------------------------------------------- //

test('запрещённая парой категория не попадает на один уровень с другой', () => {
  const snapshot = makeSnapshot(CATEGORIES, {
    conflicts: [['gemstones', 'birthstones', 'P0']],
  });
  // на уровне 5 категорий из 6 доступных: без гейта пара самоцветов почти
  // наверняка встретилась бы хотя бы в одной из выборок
  for (let i = 0; i < 12; i += 1) {
    const index = loadContentIndex(snapshot);
    const outcome = generateLevel(index, plan(5), config(`pair-${i}`),
      emptyPackHistory());
    const keys = new Set((outcome.spec?.categories ?? []).map((c) => c.key));
    assert.ok(!(keys.has('gemstones') && keys.has('birthstones')),
      `seed pair-${i}: обе категории запрещённой пары попали на уровень`);
  }
});

test('без запрета та же пара разрешена: гейт не запрещает категории вообще', () => {
  const snapshot = makeSnapshot(CATEGORIES);
  let together = 0;
  for (let i = 0; i < 12; i += 1) {
    const index = loadContentIndex(snapshot);
    const outcome = generateLevel(index, plan(5), config(`pair-${i}`),
      emptyPackHistory());
    const keys = new Set((outcome.spec?.categories ?? []).map((c) => c.key));
    if (keys.has('gemstones') && keys.has('birthstones')) together += 1;
  }
  assert.ok(together > 0,
    'пара ни разу не встретилась и без запрета — тест выше ничего не проверяет');
});

test('запрет читается независимо от порядка категорий в паре', () => {
  const index = loadContentIndex(makeSnapshot(CATEGORIES, {
    conflicts: [['birthstones', 'gemstones']],
  }));
  const a = index.categoryIndex('gemstones')!;
  const b = index.categoryIndex('birthstones')!;
  assert.ok(index.conflict(a, b), 'запрет не найден в прямом порядке');
  assert.ok(index.conflict(b, a), 'запрет не найден в обратном порядке');
  assert.equal(index.conflict(a, index.categoryIndex('tools')!), undefined);
});

// --------------------------------------------------------------------------- //
// готовность категорий
// --------------------------------------------------------------------------- //

test('категория curated_only в автосборку не идёт', () => {
  const snapshot = makeSnapshot(CATEGORIES, {
    readiness: { opposites: 'curated_only' },
  });
  for (let i = 0; i < 8; i += 1) {
    const index = loadContentIndex(snapshot);
    const outcome = generateLevel(index, plan(5), config(`ready-${i}`),
      emptyPackHistory());
    const keys = (outcome.spec?.categories ?? []).map((c) => c.key);
    assert.ok(!keys.includes('opposites'),
      `seed ready-${i}: парная категория OPPOSITES попала в автосборку`);
  }
});

test('hard_only и blocked тоже не идут, а constrained идёт', () => {
  const index = loadContentIndex(makeSnapshot(CATEGORIES, {
    readiness: {
      opposites: 'curated_only', gemstones: 'hard_only',
      birthstones: 'blocked', tools: 'constrained',
    },
  }));
  const usable = (key: string) => index.isAutoUsable(index.categoryIndex(key)!);
  assert.equal(usable('opposites'), false);
  assert.equal(usable('gemstones'), false);
  assert.equal(usable('birthstones'), false);
  assert.equal(usable('tools'), true);
  assert.equal(usable('colors'), true);
});

test('снимок без readiness генерируется как раньше: unknown пропускается', () => {
  const snapshot = makeSnapshot(CATEGORIES);
  for (const category of snapshot.categories) delete category.rd;
  const outcome = generate(snapshot, 5);
  assert.equal(outcome.spec?.categories.length, 5);
});

// --------------------------------------------------------------------------- //
// risk-флаги
// --------------------------------------------------------------------------- //

test('risk-флаги распаковываются из битовой маски', () => {
  const snapshot = makeSnapshot(CATEGORIES);
  // obscure (бит 0) + multiword (бит 3)
  const [w, c, status, fit, obviousness, relation, sense] = snapshot.memberships[0];
  snapshot.memberships[0] = [w, c, status, fit, obviousness, relation, sense, 0.5, 0b1001];
  const index = loadContentIndex(snapshot);
  const membership = index.memberships[0];
  assert.deepEqual(index.riskFlags(membership), ['obscure', 'multiword']);
  assert.equal(index.hasRiskFlag(membership, 'obscure'), true);
  assert.equal(index.hasRiskFlag(membership, 'proper_noun'), false);
  assert.equal(membership.gameplayDifficulty, 0.5);
});

test('в снимке 1.0 масок нет: флагов пусто, сложность null', () => {
  const index = loadContentIndex(makeSnapshot(CATEGORIES));
  const membership = index.memberships[0];
  assert.deepEqual(index.riskFlags(membership), []);
  assert.equal(membership.gameplayDifficulty, null);
});

// --------------------------------------------------------------------------- //
// валидатор: запрет базы — hard-инвариант и для уровней, собранных не генератором
// --------------------------------------------------------------------------- //

test('уровень с запрещённой базой парой не проходит валидацию', () => {
  const snapshot = makeSnapshot(CATEGORIES, {
    conflicts: [['gemstones', 'birthstones', 'P0']],
  });
  const index = loadContentIndex(snapshot);
  const spec = buildSpec(201, [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)],
      { theme: 'properties' }),
    levelCategory('gemstones', 'GEMSTONES', [
      word('ruby', 4.0), word('opal', 3.6), word('topaz', 3.4), word('jade', 3.8)],
      { theme: 'nature' }),
    levelCategory('birthstones', 'BIRTHSTONES', [
      word('garnet', 3.2), word('pearl', 4.1), word('amethyst', 3.3), word('peridot', 2.9)],
      { theme: 'nature' }),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('saw', 4.4), word('drill', 4.0), word('wrench', 3.5)],
      { theme: 'tools' }),
  ]);
  const result = validateLevel(spec, { index, hashQuadruple });
  const issue = result.issues.find((i) => i.code === 'CONFLICT_PAIR');
  assert.ok(issue, `CONFLICT_PAIR не сработал, упали: ${result.issues.map((i) => i.code).join(', ')}`);
  assert.equal(issue.severity, 'hard');
  assert.equal(result.passed, false);
  assert.match(issue.entities.join(' '), /gemstones/);
});

test('тот же уровень без запрета в базе проверку проходит', () => {
  const index = loadContentIndex(makeSnapshot(CATEGORIES));
  const spec = buildSpec(201, [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)],
      { theme: 'properties' }),
    levelCategory('gemstones', 'GEMSTONES', [
      word('ruby', 4.0), word('opal', 3.6), word('topaz', 3.4), word('jade', 3.8)],
      { theme: 'nature' }),
    levelCategory('birthstones', 'BIRTHSTONES', [
      word('garnet', 3.2), word('pearl', 4.1), word('amethyst', 3.3), word('peridot', 2.9)],
      { theme: 'nature' }),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('saw', 4.4), word('drill', 4.0), word('wrench', 3.5)],
      { theme: 'tools' }),
  ]);
  const result = validateLevel(spec, { index, hashQuadruple });
  assert.equal(result.issues.some((i) => i.code === 'CONFLICT_PAIR'), false);
});
