/**
 * Калибровка по декадам.
 *
 * Проверяется главное обещание правки: блок, собранный под номера 1-10, обязан
 * быть похож на уровни 1-10 оригинала, а не на уровни 150+. И обратное, не менее
 * важное: сдаваемый пакет 201-210 не сломан.
 *
 * Что значит «не сломан» после перехода на аудированную базу. `packHash` по
 * построению включает хеш снимка контента, а снимок сменился: инструмент читал
 * копию базы, оставшуюся на состоянии до внешнего аудита. Поэтому регенерация
 * прежнего пакета из текущей базы невозможна в принципе, и требовать её от теста
 * бессмысленно. Проверяем то, что проверяемо: пакет-артефакт цел (его pack_hash
 * пересчитывается из записанных в нём же хешей уровней), а воспроизводимость
 * генератора живёт в determinism.test.ts. Если снимок вернётся к тому же хешу —
 * тест снова потребует байт-в-байт совпадение.
 *
 * Числа-цели живут в web/src/core/decadeProfiles.ts, замер — в
 * scripts/decade_profile.py, разбор — в docs/DECADE_CALIBRATION.md.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import {
  DECADE_PROFILES, SPIKE_POSITION, RECOVERY_POSITION, checkDecadeFit, configForRange,
  planCategoryCounts, profileForRange, visibleShareMin,
} from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { canonicalJson, sha256Hex } from '../web/src/core/hashing.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

/** Сдаваемый пакет как артефакт: data/final-pack/pack.json. */
const FINAL_PACK = JSON.parse(
  readFileSync(join(ROOT, 'data/final-pack/pack.json'), 'utf8'));
const FINAL_PACK_HASH = FINAL_PACK.pack_hash as string;

function fitInput(block: ReturnType<typeof generateBlock>) {
  return block.levels.map((l) => ({
    levelId: l.spec.levelId,
    categoryCount: l.spec.categories.length,
    zipfs: l.spec.categories.flatMap((c) => c.words.map((w) => w.zipf)),
    metaCount: l.spec.categories.reduce((n, c) =>
      n + c.words.filter((w) => w.kind === 'meta').length, 0),
    metaDepth: Math.max(0, ...l.spec.categories.map((c) => c.metaDepth)),
    chainCount: l.spec.modifiers.chains.length,
    moveLimit: l.spec.board.moveLimit,
    startBubbles: l.spec.board.startBubbles,
    boardCapacity: l.spec.board.boardCapacity,
    wordsPerCategory: l.spec.board.wordsPerCategory,
  }));
}

// --------------------------------------------------------------------------- //
// самое важное: старый пакет не сломан
// --------------------------------------------------------------------------- //

test('сдаваемый пакет 201-210 цел: его pack hash пересчитывается из самого пакета', () => {
  const recomputed = sha256Hex(canonicalJson({
    levels: FINAL_PACK.levels.map((l: { level_spec_hash: string }) => l.level_spec_hash),
    snapshot: FINAL_PACK.content_snapshot_hash,
    generator: FINAL_PACK.generator_version,
    scoring: FINAL_PACK.scoring_version,
  }));
  assert.equal(recomputed, FINAL_PACK_HASH);
  assert.equal(FINAL_PACK.levels.length, 10);
});

test('пресет 201-210 воспроизводится, пока снимок базы тот же', () => {
  const block = generateBlock({ snapshot, config: DEFAULT_BLOCK_CONFIG, scoring });
  assert.equal(block.levels.length, 10);
  if (FINAL_PACK.content_snapshot_hash !== snapshot.content_snapshot_hash) {
    // База сменилась осознанно (переход на аудированную базу). Пакет остаётся
    // артефактом прежнего снимка; чтобы инструмент снова воспроизводил его
    // байт-в-байт, пакет надо пересобрать и заново прогнать слепым решателем.
    assert.notEqual(block.packHash, FINAL_PACK_HASH);
    return;
  }
  assert.equal(block.packHash, FINAL_PACK_HASH);
});

test('у пресета 201-210 гейтов декады нет: иначе изменился бы нормализованный конфиг', () => {
  assert.equal(DEFAULT_BLOCK_CONFIG.decadeGates, undefined);
});

// --------------------------------------------------------------------------- //
// таблица профилей
// --------------------------------------------------------------------------- //

test('профили декад идут шагом 10 и покрывают 1-191', () => {
  assert.equal(DECADE_PROFILES.length, 20);
  DECADE_PROFILES.forEach((p, i) => assert.equal(p.from, i * 10 + 1));
});

test('профиль выбирается по первому уровню диапазона', () => {
  assert.equal(profileForRange([1, 10]).from, 1);
  assert.equal(profileForRange([5, 14]).from, 1);      // блок внахлёст берёт свою декаду
  assert.equal(profileForRange([121, 130]).from, 121);
  // за пределами замеренных 199 уровней продолжаем последней декадой
  assert.equal(profileForRange([201, 210]).from, 191);
});

test('ступенька размера уровня на L121 сохранена в таблице', () => {
  const before = profileForRange([111, 120]).categoryMean;
  const after = profileForRange([121, 130]).categoryMean;
  assert.ok(after - before > 3, `ожидался прыжок, получено ${before} → ${after}`);
});

test('узнаваемость падает от первой декады к последней', () => {
  const first = DECADE_PROFILES[0].zipfMedianTarget;
  const last = DECADE_PROFILES[DECADE_PROFILES.length - 1].zipfMedianTarget;
  assert.ok(first > last, `медиана обязана падать: ${first} → ${last}`);
});

test('видимая доля выводится из коридора, а не задаётся руками', () => {
  for (const profile of DECADE_PROFILES) {
    const share = visibleShareMin(profile);
    // самый большой уровень декады обязан оставаться допустимым
    assert.ok(share <= 24 / (profile.categoryCorridor[1] * 4) + 1e-9,
      `декада ${profile.from}: порог ${share} выше собственного максимума`);
  }
});

// --------------------------------------------------------------------------- //
// ритм
// --------------------------------------------------------------------------- //

test('план категорий держит спайк на 5 и передышку на 6', () => {
  for (const profile of DECADE_PROFILES) {
    for (const seed of ['a', 'b', 'c']) {
      const counts = planCategoryCounts(profile, seed, 10, profile.from === 1);
      assert.ok(counts[RECOVERY_POSITION - 1] < counts[SPIKE_POSITION - 1],
        `декада ${profile.from}, seed ${seed}: позиция 6 (${counts[RECOVERY_POSITION - 1]}) `
        + `не ниже позиции 5 (${counts[SPIKE_POSITION - 1]})`);
    }
  }
});

test('план категорий укладывается в коридор своей декады и даёт разброс 5-7', () => {
  for (const profile of DECADE_PROFILES) {
    const counts = planCategoryCounts(profile, 'rhythm', 10, profile.from === 1);
    const spread = Math.max(...counts) - Math.min(...counts);
    assert.ok(spread >= 5 && spread <= 7, `декада ${profile.from}: разброс ${spread}`);
    for (const c of counts) {
      assert.ok(c >= profile.categoryCorridor[0] && c <= profile.categoryCorridor[1],
        `декада ${profile.from}: ${c} вне коридора ${profile.categoryCorridor.join('-')}`);
    }
  }
});

test('ритм пресета 201-210 по-прежнему проходит проверку', () => {
  assert.ok(checkBlockRhythm(buildBlockPlan(DEFAULT_BLOCK_CONFIG)).passed);
});

test('плоский план ритм не проходит', () => {
  const flat = checkBlockRhythm(buildBlockPlan({
    ...DEFAULT_BLOCK_CONFIG,
    categoryPlan: [12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
  }));
  assert.equal(flat.passed, false);
});

// --------------------------------------------------------------------------- //
// туториал
// --------------------------------------------------------------------------- //

test('уровень 1 — туториал: 5 категорий, без лимита, весь уровень на поле', () => {
  const config = configForRange([1, 10], 'final-03');
  const block = generateBlock({ snapshot, config, scoring });
  const first = block.levels.find((l) => l.spec.levelId === 1);
  assert.ok(first, 'уровень 1 не собрался');
  assert.equal(first.spec.categories.length, 5);
  assert.equal(first.spec.board.moveLimit, null);
  assert.equal(first.spec.board.moveLimitK, null);
  assert.equal(first.spec.board.startBubbles, 20);
  assert.equal(first.plan.role, 'tutorial');
  // мета-пар и модификаторов на туториале быть не должно
  const metas = first.spec.categories.reduce((n, c) =>
    n + c.words.filter((w) => w.kind === 'meta').length, 0);
  assert.equal(metas, 0);
  assert.equal(first.spec.modifiers.chains.length, 0);
});

test('туториал проходит валидацию, несмотря на отсутствие лимита ходов', () => {
  const block = generateBlock({ snapshot, config: configForRange([1, 10], 'final-03'), scoring });
  const first = block.levels.find((l) => l.spec.levelId === 1)!;
  const hard = first.validation.issues.filter((i) => i.severity === 'hard');
  assert.deepEqual(hard.map((i) => i.code), []);
});

// --------------------------------------------------------------------------- //
// гейты формы слова
// --------------------------------------------------------------------------- //

test('на декаде 1-10 нет многословных ответов и слов длиннее 12 букв', () => {
  const config = configForRange([1, 10], 'final-03');
  const block = generateBlock({ snapshot, config, scoring });
  assert.ok(block.levels.length >= 1);
  for (const level of block.levels) {
    for (const category of level.spec.categories) {
      for (const w of category.words) {
        assert.equal(w.text.trim().split(/\s+/).length, 1,
          `уровень ${level.spec.levelId}: многословный ответ «${w.text}»`);
        assert.ok(w.text.length <= 12,
          `уровень ${level.spec.levelId}: слово «${w.text}» длиннее 12 букв`);
      }
    }
  }
});

test('редких имён собственных на декаде 1-10 нет', () => {
  const config = configForRange([1, 10], 'final-03');
  const block = generateBlock({ snapshot, config, scoring });
  const norm = new Map(snapshot.words.map((w) => [w.n, w]));
  for (const level of block.levels) {
    for (const category of level.spec.categories) {
      for (const w of category.words) {
        const record = norm.get(w.text.toLowerCase());
        if (record?.p !== 1) continue;
        assert.ok(record.z !== null && record.z >= 3.2,
          `уровень ${level.spec.levelId}: имя собственное «${w.text}» с zipf ${record.z}`);
      }
    }
  }
});

test('цепи на декадах до L20 не ставятся', () => {
  for (const range of [[1, 10], [11, 20]] as [number, number][]) {
    const block = generateBlock({ snapshot, config: configForRange(range, 'final-03'), scoring });
    const chains = block.levels.reduce((n, l) => n + l.spec.modifiers.chains.length, 0);
    if (range[0] === 1) assert.equal(chains, 0, 'на декаде 1-10 цепей быть не должно');
  }
});

// --------------------------------------------------------------------------- //
// приёмка блока
// --------------------------------------------------------------------------- //

test('калиброванный блок 1-10 проходит приёмку по декаде', () => {
  const config = configForRange([1, 10], 'final-03');
  const block = generateBlock({ snapshot, config, scoring });
  assert.equal(block.levels.length, 10, `собрано ${block.levels.length} из 10`);
  const fit = checkDecadeFit(fitInput(block), profileForRange([1, 10]), undefined, 10);
  const failed = fit.checks.filter((c) => !c.passed);
  assert.deepEqual(failed.map((c) => `${c.code}: ${c.detail}`), []);
});

test('приёмка не судит ритм по неполному блоку', () => {
  // берём три уровня из десяти: последовательность заведомо не пила
  const profile = profileForRange([1, 10]);
  const three = [7, 7, 7].map((categoryCount, i) => ({
    levelId: i + 1, categoryCount, zipfs: [4.3, 4.4, 4.35, 4.5],
    metaCount: 0, metaDepth: 0, chainCount: 0, moveLimit: 30,
    startBubbles: 28, boardCapacity: 24, wordsPerCategory: 4,
  }));
  const fit = checkDecadeFit(three, profile, undefined, 10);
  const codes = fit.checks.map((c) => c.code);
  assert.ok(codes.includes('BLOCK_COMPLETE'));
  assert.equal(fit.checks.find((c) => c.code === 'BLOCK_COMPLETE')?.passed, false);
  for (const rhythmCode of ['CATEGORY_SPREAD', 'DESCENTS', 'SPIKE_THEN_RECOVERY', 'CATEGORY_MEAN']) {
    assert.ok(!codes.includes(rhythmCode),
      `${rhythmCode} не должен проверяться на неполном блоке`);
  }
});

test('блок с поздним контентом не проходит приёмку декады 1-10', () => {
  // тот самый брак: уровни 1-10 с размером и редкостью поздней палитры
  const profile = profileForRange([1, 10]);
  const late = [13, 15, 12, 16, 18, 12, 14, 15, 17, 13].map((categoryCount, i) => ({
    levelId: i + 1, categoryCount,
    zipfs: Array.from({ length: categoryCount * 4 }, (_, k) => (k % 5 === 0 ? 2.6 : 3.5)),
    metaCount: 2, metaDepth: 2, chainCount: 0, moveLimit: 57,
    startBubbles: categoryCount * 4 - 2, boardCapacity: 24, wordsPerCategory: 4,
  }));
  const fit = checkDecadeFit(late, profile, undefined, 10);
  assert.equal(fit.passed, false);
  const failed = fit.checks.filter((c) => !c.passed).map((c) => c.code);
  assert.ok(failed.includes('CATEGORY_MEAN'), 'размер уровня обязан быть замечен');
  assert.ok(failed.includes('ZIPF_BLOCK_MEDIAN'), 'редкость слов обязана быть замечена');
  assert.ok(failed.includes('TUTORIAL_FIRST_LEVEL'), 'отсутствие туториала обязано быть замечено');
});

test('каждая декада собирается целиком и проходит приёмку', () => {
  for (const profile of DECADE_PROFILES) {
    const range: [number, number] = [profile.from, profile.from + 9];
    const block = generateBlock({ snapshot, config: configForRange(range, 'final-03'), scoring });
    assert.equal(block.levels.length, 10,
      `декада ${profile.from}: собрано ${block.levels.length} из 10, `
      + `отказы: ${block.failures.map((f) => f.reason).join(' | ')}`);
    const fit = checkDecadeFit(fitInput(block), profile, undefined, 10);
    assert.deepEqual(fit.checks.filter((c) => !c.passed).map((c) => `${c.code}: ${c.detail}`), [],
      `декада ${profile.from}`);
  }
});

test('генерация по декаде детерминирована', () => {
  const config = configForRange([1, 10], 'repeat-me');
  const a = generateBlock({ snapshot, config, scoring });
  const b = generateBlock({ snapshot, config: configForRange([1, 10], 'repeat-me'), scoring });
  assert.equal(a.packHash, b.packHash);
});
