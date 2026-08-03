/**
 * Ручная схема старта на экране «Уровень».
 *
 * Правка выкладки — единственное место, где человек меняет СДАННЫЙ уровень
 * после генерации, поэтому проверяется главное обещание: пересчитывается всё,
 * что от выкладки зависит, и ничего, что от неё не зависит.
 *
 *   выкладка   — исполняет заданную схему и остаётся полной (каждое слово раз);
 *   состав     — категории и слова те же: это правка поля, а не пересборка;
 *   хеши       — хеш спека меняется (выкладка в нём), хеш пакета пересчитан;
 *   проверки   — валидация и проходимость посчитаны заново, а не унаследованы;
 *   «авто»     — возврат к автоматической раздаче даёт ровно исходный уровень.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import {
  generateBlock, levelHardGateFailure, redealLevel, withLevel,
} from '../web/src/core/generateBlock.ts';
import { checkDeal } from '../web/src/core/deal.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
const level = block.levels[0];

/** Фактическая схема: сколько слов каждой категории лежит на старте, по убыванию. */
function appliedScheme(spec: typeof level.spec): number[] {
  const counts = new Map<string, number>();
  for (const bubble of spec.deal.start) {
    counts.set(bubble.category, (counts.get(bubble.category) ?? 0) + 1);
  }
  return [...counts.values()].sort((a, b) => b - a);
}

const SCHEME = [4, 4, 3, 3, 2];

test('схема исполняется: старт становится глубже и уже', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  const applied = appliedScheme(redealt.spec);

  assert.deepEqual([...(redealt.spec.board.dealScheme ?? [])], SCHEME,
    'схема должна лежать в спеке: иначе выкладка не воспроизводится из пакета');
  assert.ok(applied.length <= SCHEME.length,
    `категорий на старте ${applied.length}, в схеме ${SCHEME.length}: `
    + 'лишних старт открывать не имеет права');
  /*
   * Поэлементно не больше запрошенного, но и не обязательно равно. Доля может
   * оказаться меньше по двум законным причинам: у категории с мета-словом
   * спавнящихся слов всего три (`want = min(доля, слов в пуле)`), и бюджет поля
   * может не вместить долю целиком. Требовать буквального совпадения значило бы
   * требовать от выкладки невозможного.
   */
  applied.forEach((n, i) => {
    assert.ok(n <= SCHEME[i], `доля ${i + 1}: выложено ${n}, в схеме ${SCHEME[i]}`);
  });
  // глубже: собираемых сразу категорий (четвёрок) стало не меньше, чем было
  const fullBefore = appliedScheme(level.spec).filter((n) => n === 4).length;
  const fullAfter = applied.filter((n) => n === 4).length;
  assert.ok(fullAfter >= fullBefore,
    `четвёрок на старте было ${fullBefore}, стало ${fullAfter}`);
});

test('выкладка остаётся полной: каждое слово ровно один раз', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  assert.deepEqual(checkDeal(redealt.spec, redealt.spec.deal), [],
    'потерянное слово делает категорию несобираемой, лишнее ломает досыпку');
});

test('состав уровня не меняется — это правка поля, а не пересборка', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  assert.deepEqual(
    redealt.spec.categories.map((c) => `${c.key}:${c.words.map((w) => w.text).join(',')}`),
    level.spec.categories.map((c) => `${c.key}:${c.words.map((w) => w.text).join(',')}`));
  assert.equal(redealt.spec.board.moveLimit, level.spec.board.moveLimit,
    'лимит ходов считается от числа категорий и склеек, выкладка на него не влияет');
});

test('хеш спека меняется, а хеш пакета пересчитывается', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  assert.notEqual(redealt.levelSpecHash, level.levelSpecHash,
    'выкладка входит в хеш спека: тот же хеш означал бы другой уровень под старым именем');

  const next = withLevel(block, redealt, scoring);
  assert.notEqual(next.packHash, block.packHash);
  assert.equal(next.levels.length, block.levels.length);
  assert.equal(next.levels[0].levelSpecHash, redealt.levelSpecHash);
  // остальные уровни блока правка не касается
  assert.deepEqual(next.levels.slice(1).map((l) => l.levelSpecHash),
    block.levels.slice(1).map((l) => l.levelSpecHash));
});

test('проверки и проходимость посчитаны заново, а не унаследованы', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  assert.ok(redealt.playability, 'без пересчёта проходимости правка была бы вслепую');
  assert.equal(redealt.solutions.count, level.solutions.count,
    'единственность решения от выкладки не зависит, но обязана быть перепроверена');
  assert.ok(redealt.validation.checks.length > 0);
  // след ручной правки виден в попытках: по уровню должно быть понятно, кто задал старт
  const last = redealt.attempts[redealt.attempts.length - 1];
  assert.equal(last.stage, 'выкладка');
  assert.match(last.reason, /вручную/);
});

test('«авто» возвращает ровно исходный уровень', () => {
  const manual = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  const back = redealLevel({ snapshot, scoring, block, level: manual, scheme: null });
  assert.equal(back.levelSpecHash, level.levelSpecHash,
    'возврат к автоматической раздаче обязан давать прежний уровень с прежним хешем');
  assert.deepEqual(appliedScheme(back.spec), appliedScheme(level.spec));
  assert.equal(back.spec.board.dealScheme, undefined);
});

/*
 * Ручная пересдача не имеет права обходить приёмку.
 *
 * Аудит 03.08: после правки выкладки к уровню не применялся тот же
 * динамический hard-гейт, что при генерации, — экспорт всё равно оставался
 * доступен. Гейт с тех пор один (`levelHardGateFailure`), и результат
 * пересдачи обязан быть таким, чтобы гейт мог его судить: с посчитанной
 * проходимостью, а не с унаследованной или пустой.
 */
test('к пересданному уровню применим тот же гейт, что к сгенерированному', () => {
  const redealt = redealLevel({ snapshot, scoring, block, level, scheme: SCHEME });
  // гейт обязан ВЫНЕСТИ СУЖДЕНИЕ, а не промолчать из-за недостающих данных
  const failure = levelHardGateFailure(redealt);
  if (failure) {
    assert.notEqual(failure.stage, 'проходимость',
      `гейт не смог оценить пересданный уровень: ${failure.reason}`);
  }
  // и исходный уровень блока гейт тоже судит — он пришёл из генерации и прошёл её
  assert.equal(levelHardGateFailure(level), null,
    'уровень, принятый генератором, обязан проходить общий гейт');
});
