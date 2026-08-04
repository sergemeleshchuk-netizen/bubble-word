/**
 * Решаемость живым игроком: четыре ручки, включённые 04.08.
 *
 * Повод — уровень 103, который владелец продукта не смог пройти руками, хотя
 * приёмка объявила его решаемым. Приёмку до этого проходил ЗРЯЧИЙ бот: он читает
 * `category` прямо из выкладки и не ошибается никогда, поэтому его «PASS»
 * означал только «раскладка физически существует». Слепой прогон 200 первых
 * уровней показал цену этого: 35 уровней из 200 модельный игрок не доходил чаще,
 * чем в 20% попыток, а предсказывали провал ровно два признака — число мета-пар
 * и слова, за которые нельзя зацепиться.
 *
 * Ручки, которые тест держит:
 *   1. ПРАВИЛО ОПОРЫ — в каждой категории минимум два слова с ясностью от
 *      `ANCHOR_CLARITY` (generator.ts, `ANCHORS_PER_CATEGORY`);
 *   2. ПОТОЛОК МЕТА-ПАР на первых двухстах уровнях — `META_MAX_EARLY`
 *      (проверяется в meta_plan.test.ts, здесь — что генератор его не
 *      перебирает: план он обязан исполнять, а не превышать);
 *   3. СЛЕПОЙ ГЕЙТ — уровень, который модельный игрок проигрывает, приёмку не
 *      проходит (`BLIND_WIN_MIN` в generateBlock.ts);
 *   4. БЮДЖЕТ ОШИБОК на ранней кривой — `EARLY_MOVE_LIMIT_BONUS` в blockPlan.ts.
 *
 * Почему тест смотрит на СОБРАННЫЙ блок, а не на функции по отдельности: все
 * четыре ручки договариваются между собой через генератор, и сломать их можно,
 * не тронув ни одной из них — например, вернув перебор мета-пар мимо плана.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { LevelSpec, Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { configForRange, EARLY_CURVE_UNTIL } from '../web/src/core/decadeProfiles.ts';
import { BLIND_WIN_MIN, generateBlock } from '../web/src/core/generateBlock.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import { ANCHOR_CLARITY, wordProfiles } from '../web/src/core/playerKnowledge.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const index = new ContentIndex(snapshot);

/** Декада с тем самым уровнем 103 — на ней всё и разбиралось. */
const block = generateBlock({
  snapshot, scoring, config: configForRange([101, 110], 'final-03'),
});

/** Сколько слов категории игрок опознаёт на их месте. */
function anchorsOf(spec: LevelSpec, categoryKey: string): string[] {
  const profiles = wordProfiles(spec, undefined, index);
  const category = spec.categories.find((c) => c.key === categoryKey)!;
  return category.words
    .filter((w) => (profiles.get(w.text)?.clarity ?? 0) >= ANCHOR_CLARITY)
    .map((w) => w.text);
}

// --------------------------------------------------------------------------- //
// 1. правило опоры
// --------------------------------------------------------------------------- //

test('в каждой категории блока есть минимум две опоры', () => {
  assert.equal(block.levels.length, 10, 'декада собралась не целиком');
  for (const level of block.levels) {
    for (const category of level.spec.categories) {
      const anchors = anchorsOf(level.spec, category.key);
      assert.ok(anchors.length >= 2,
        `уровень ${level.spec.levelId}, категория ${category.key}: опор `
        + `${anchors.length} (${anchors.join(', ') || 'ни одной'}) — четвёрка `
        + `${category.words.map((w) => w.text).join('/')} собирается только перебором`);
    }
  }
});

test('опора считается тем же правилом, которым её мерит слепой прогон', () => {
  // ясность зависит от силы связи слово→категория, а не от слова самого по себе:
  // одно и то же слово может быть опорой в одной категории и шифром в другой.
  // Тест сторожит именно это: правило одно, а не две копии формулы.
  const level = block.levels[0];
  const profiles = wordProfiles(level.spec, undefined, index);
  const words = level.spec.categories.flatMap((c) => c.words.map((w) => w.text));
  for (const word of words) {
    assert.ok(profiles.has(word), `слова ${word} нет в профилях слепого прогона`);
  }
  assert.ok(level.blindPlay!.clarity > 0, 'слепой прогон не посчитал ясность блока');
});

// --------------------------------------------------------------------------- //
// 2. план мета-пар исполняется, а не превышается
// --------------------------------------------------------------------------- //

test('мета-пар на уровне не больше, чем просил план', () => {
  const plans = buildBlockPlan(block.config);
  for (const level of block.levels) {
    const plan = plans.find((p) => p.levelId === level.spec.levelId)!;
    const actual = level.spec.categories.reduce((n, c) =>
      n + c.words.filter((w) => w.kind === 'meta').length, 0);
    assert.ok(actual <= plan.metaCount,
      `уровень ${level.spec.levelId}: мета-пар ${actual}, план просил ${plan.metaCount} — `
      + 'бюджет мета-пар обязан быть потолком, а не пожеланием');
  }
});

// --------------------------------------------------------------------------- //
// 3. слепой гейт
// --------------------------------------------------------------------------- //

test('принятый уровень доходит у модельного игрока — или принят на снятом гейте', () => {
  for (const level of block.levels) {
    const blind = level.blindPlay!;
    if (blind.moveLimit === null) continue;                  // туториал без лимита
    // гейт снимается в последней трети попыток: 48 попыток, граница 32
    const lateAccept = level.attempts.length > Math.floor((48 * 2) / 3);
    assert.ok(blind.winRate >= BLIND_WIN_MIN || lateAccept,
      `уровень ${level.spec.levelId}: доходят ${Math.round(blind.winRate * 100)}% `
      + `при пороге ${Math.round(BLIND_WIN_MIN * 100)}%, а попыток всего `
      + `${level.attempts.length} — значит гейт его пропустил, а не уступил`);
  }
});

test('декада 101-110 больше не содержит уровня, который не пройти', () => {
  // именно этот случай и разбирался: на прежнем генераторе уровень 103 доходил
  // в 17-42% прогонов, а промахи съедали 200% бюджета ошибок
  const level = block.levels.find((l) => l.spec.levelId === 103)!;
  const blind = level.blindPlay!;
  assert.ok(blind.winRate >= BLIND_WIN_MIN,
    `уровень 103: доходят ${Math.round(blind.winRate * 100)}%`);
  assert.ok((blind.errorBudgetUsed ?? 0) <= 1,
    `уровень 103: промахи съедают ${Math.round((blind.errorBudgetUsed ?? 0) * 100)}% `
    + 'бюджета ошибок');
});

// --------------------------------------------------------------------------- //
// 4. бюджет ошибок ранней кривой
// --------------------------------------------------------------------------- //

test('на ранней кривой лимит ходов шире, чем на той же роли позже', () => {
  const early = buildBlockPlan(configForRange([101, 110], 'final-03'));
  const late = buildBlockPlan(configForRange([301, 310], 'final-03'));
  const roleK = (plans: typeof early, role: string): number | undefined =>
    plans.find((p) => p.role === role)?.moveLimitK ?? undefined;
  // передышка и так на потолке MAX_MOVE_LIMIT_K, прибавлять ей некуда
  const roles = ['growth', 'entry', 'peak', 'exit'];
  for (const role of roles) {
    const before = roleK(early, role);
    const after = roleK(late, role);
    assert.ok(before !== undefined && after !== undefined,
      `роль ${role} не встречается в декаде — сравнивать нечего`);
    assert.ok(before > after,
      `роль ${role}: K на ранней кривой ${before}, дальше ${after} — прибавки нет`);
  }
  assert.equal(roleK(early, 'recovery'), roleK(late, 'recovery'),
    'передышка стоит на потолке K и прибавку получить не может');
});

test('прибавка кончается ровно на границе ранней кривой', () => {
  const inside = buildBlockPlan(configForRange([191, 200], 'final-03'));
  const outside = buildBlockPlan(configForRange([201, 210], 'final-03'));
  const growthK = (plans: typeof inside): number =>
    plans.find((p) => p.role === 'growth')!.moveLimitK!;
  assert.equal(inside[inside.length - 1].levelId, EARLY_CURVE_UNTIL);
  assert.ok(growthK(inside) > growthK(outside),
    'граница ранней кривой перестала действовать');
});

test('пресет 201-210 прибавку не получает: он за ранней кривой', () => {
  const plans = buildBlockPlan(DEFAULT_BLOCK_CONFIG);
  assert.equal(plans.find((p) => p.role === 'growth')!.moveLimitK, 1.35);
});
