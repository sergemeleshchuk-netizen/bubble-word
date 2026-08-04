/**
 * Выбор категории-картинки по позициям блока (`iconPlan`).
 *
 * Картинка на мета-пузыре существовала с 03.08, но управлять ею было нечем:
 * доля 25% от числа мета-пузырей плюс попадание имени в словарь значков давали
 * картинку на четырёх уровнях блока из десяти, и повлиять на это владелец не мог.
 * Решение 04.08: галочка «🖼» на графике ритма — «картинка на этом уровне нужна»
 * или «картинок нет».
 *
 * Что тест держит:
 *   1. требование выполняется на всех уровнях, где оно физически выполнимо
 *      (уровень без мета-пар нести картинку не может);
 *   2. запрет — абсолютный, даже когда имена подходят;
 *   3. отсутствие плана не меняет НИЧЕГО: хеш пакета остаётся прежним, то есть
 *      уже собранные пакеты не разъезжаются;
 *   4. картинка по требованию доезжает до прототипа, а не только до спека.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { BlockConfig, Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { buildHandoffPack } from '../web/src/core/playableHandoff.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const build = (iconPlan?: (0 | 1 | null)[]) => generateBlock({
  snapshot, scoring, config: { ...DEFAULT_BLOCK_CONFIG, iconPlan } as BlockConfig,
});

const TEN = <T,>(v: T): T[] => Array.from({ length: 10 }, () => v);

const required = build(TEN<0 | 1 | null>(1));
const forbidden = build(TEN<0 | 1 | null>(0));

/** Мета-пузыри уровня и те из них, что несут значок. */
function icons(level: typeof required.levels[number]) {
  const metas = level.spec.categories.flatMap((c) => c.words.filter((w) => w.kind === 'meta'));
  return { metas, withIcon: metas.filter((w) => w.icon) };
}

// --------------------------------------------------------------------------- //
// план
// --------------------------------------------------------------------------- //

test('план переводит галочку в режим уровня', () => {
  const plans = buildBlockPlan({ ...DEFAULT_BLOCK_CONFIG, iconPlan: [1, 0, null, ...TEN(null)] });
  assert.equal(plans[0].iconMode, 'require');
  assert.equal(plans[1].iconMode, 'forbid');
  assert.equal(plans[2].iconMode, 'auto');
});

test('на уровне без мета-пар требование превращается в auto, а не в отказ', () => {
  // позиция 6 пресета — передышка без мета (мета-план 1,2,1,3,4,0,2,3,3,1)
  const plans = buildBlockPlan({ ...DEFAULT_BLOCK_CONFIG, iconPlan: TEN<0 | 1 | null>(1) });
  assert.equal(plans[5].metaCount, 0);
  assert.equal(plans[5].iconMode, 'auto');
});

// --------------------------------------------------------------------------- //
// требование
// --------------------------------------------------------------------------- //

test('требование выполнено на каждом уровне, где есть мета-пары', () => {
  assert.equal(required.levels.length, 10, 'блок с требованием картинки собрался не целиком');
  for (const level of required.levels) {
    const { metas, withIcon } = icons(level);
    if (metas.length === 0) {
      assert.equal(withIcon.length, 0,
        `уровень ${level.spec.levelId}: картинка без мета-пар невозможна`);
      continue;
    }
    assert.ok(withIcon.length >= 1,
      `уровень ${level.spec.levelId}: мета-пар ${metas.length}, а картинки нет`);
  }
});

test('требование поднимает покрытие блока: было 4 уровня из 10, стало 9', () => {
  const withIcon = required.levels.filter((l) => icons(l).withIcon.length > 0).length;
  const noMeta = required.levels.filter((l) => icons(l).metas.length === 0).length;
  assert.equal(withIcon + noMeta, required.levels.length,
    `картинка есть на ${withIcon} уровнях, без мета-пар ${noMeta} — остальные необъяснимы`);
  assert.ok(withIcon >= 8, `картинок всего на ${withIcon} уровнях`);
});

test('одна картинка на уровень, а не значки на всех мета-пузырях', () => {
  for (const level of required.levels) {
    const { metas, withIcon } = icons(level);
    assert.ok(withIcon.length <= Math.max(1, Math.round(metas.length * 0.25)),
      `уровень ${level.spec.levelId}: значков ${withIcon.length} при ${metas.length} мета-парах`);
  }
});

test('картинка по требованию доезжает до прототипа', () => {
  const pack = buildHandoffPack(required);
  let checked = 0;
  for (const level of required.levels) {
    const { withIcon } = icons(level);
    if (withIcon.length === 0) continue;
    const handoff = pack.levels.find((l) => l.level_id === level.spec.levelId)!;
    assert.deepEqual(handoff.icons?.map((i) => `${i.word} ${i.icon}`),
      withIcon.map((w) => `${w.text} ${w.icon}`));
    checked += 1;
  }
  assert.ok(checked >= 8, `картинки доехали только с ${checked} уровней`);
});

// --------------------------------------------------------------------------- //
// запрет
// --------------------------------------------------------------------------- //

test('запрет абсолютный: ни одного значка на блоке', () => {
  assert.equal(forbidden.levels.length, 10, 'блок с запретом картинок собрался не целиком');
  for (const level of forbidden.levels) {
    assert.equal(icons(level).withIcon.length, 0,
      `уровень ${level.spec.levelId}: значок при запрете`);
  }
  const pack = buildHandoffPack(forbidden);
  assert.ok(pack.levels.every((l) => l.icons === undefined),
    'в пакете прототипа остался список картинок');
});

test('запрет не отменяет мета-связи: пузыри остались, значков нет', () => {
  const metaTotal = forbidden.levels.reduce((n, l) => n + icons(l).metas.length, 0);
  assert.ok(metaTotal >= 15, `мета-пар в блоке всего ${metaTotal} — запрет унёс и связи`);
});

// --------------------------------------------------------------------------- //
// совместимость
// --------------------------------------------------------------------------- //

test('плана нет — не изменилось ничего: тот же хеш пакета', () => {
  const auto = build(undefined);
  const nulls = build(TEN<0 | 1 | null>(null));
  assert.equal(nulls.packHash, auto.packHash,
    'план из одних null попал в хеш — старые пакеты разъедутся');
  assert.deepEqual(nulls.levels.map((l) => l.levelSpecHash),
    auto.levels.map((l) => l.levelSpecHash));
});
