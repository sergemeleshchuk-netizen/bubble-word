/**
 * Поштучные переключатели уровня: мета и модификатор.
 *
 * До чекбоксов на графике ритма увидеть, что на уровне включены половинки,
 * можно было только в собранном уровне — то есть после генерации. Выключить их
 * на ОДНОМ уровне было нельзя вовсе: `allowedModifiers` действует на весь блок.
 *
 * Здесь проверяется контракт, на который опираются чекбоксы: явный план по
 * позициям сильнее лесенки по декадам, а его отсутствие ничего не меняет.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import type { BlockConfig } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { canonicalJson } from '../web/src/core/hashing.ts';

/** Блок 51+: лесенка декад ставит там и половинки, и блокираторы, и цепь. */
const WITH_MODIFIERS: BlockConfig = {
  ...DEFAULT_BLOCK_CONFIG,
  levelRange: [51, 60],
  allowedModifiers: ['halves', 'ice', 'hidden', 'chain_line'],
};

test('без явного плана модификаторы расставляет лесенка декад', () => {
  const plans = buildBlockPlan(WITH_MODIFIERS);
  assert.ok(plans.some((p) => p.modifier !== 'none'),
    'на блоке 51+ хотя бы один модификатор обязан появиться сам');
});

test('явный модификатор сильнее лесенки', () => {
  const plans = buildBlockPlan(WITH_MODIFIERS);
  const modifierPlan = plans.map(() => null) as (BlockConfig['modifierPlan'] & object);
  modifierPlan[0] = 'chain_line';
  const patched = buildBlockPlan({ ...WITH_MODIFIERS, modifierPlan });
  assert.equal(patched[0].modifier, 'chain_line');
  // остальные позиции остались на усмотрение плана
  assert.deepEqual(patched.slice(1).map((p) => p.modifier), plans.slice(1).map((p) => p.modifier));
});

test('«none» в плане выключает модификатор на одном уровне', () => {
  const plans = buildBlockPlan(WITH_MODIFIERS);
  const index = plans.findIndex((p) => p.modifier !== 'none');
  assert.ok(index >= 0, 'нужен уровень, где модификатор поставлен автоматически');

  const modifierPlan = plans.map(() => null) as (BlockConfig['modifierPlan'] & object);
  modifierPlan[index] = 'none';
  const patched = buildBlockPlan({ ...WITH_MODIFIERS, modifierPlan });
  assert.equal(patched[index].modifier, 'none',
    'снятый чекбокс обязан выключить модификатор, а не вернуть значение лесенки');
});

test('ноль в metaPlan выключает мета на уровне', () => {
  const metaPlan = buildBlockPlan(WITH_MODIFIERS).map((p) => p.metaCount);
  metaPlan[2] = 0;
  const patched = buildBlockPlan({ ...WITH_MODIFIERS, metaPlan });
  assert.equal(patched[2].metaCount, 0);
  assert.equal(patched[2].metaDepthTarget, 0, 'без мета-связей глубина обязана быть нулём');
});

/**
 * Поле необязательное, и это часть контракта: пока чекбоксов не касались,
 * нормализованный конфиг обязан остаться прежним, иначе хеш сдаваемого пакета
 * поехал бы от одного лишь появления новой возможности в инструменте.
 */
test('без правок чекбоксами конфиг не меняется', () => {
  assert.equal(DEFAULT_BLOCK_CONFIG.modifierPlan, undefined);
  assert.ok(!canonicalJson(DEFAULT_BLOCK_CONFIG).includes('modifierPlan'));
});
