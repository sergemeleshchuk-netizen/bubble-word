/**
 * Уровни оригинала как есть (web/src/core/referenceLevels.ts).
 *
 * Проверяется главное обещание этого пути: уровень НЕ собирается, а
 * воспроизводится. Значит состав обязан совпасть с выгрузкой слово в слово,
 * порядок выдачи — с порядком источника, а стартовое поле — с тем, что снято
 * с записей оригинала (tool/word_content_pipeline/data/reference/
 * video-boards-20.json).
 */
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

import { ContentIndex } from '../web/src/core/snapshot.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import type { Snapshot } from '../web/src/core/types.ts';
import { sourceById } from '../web/src/core/sources.ts';
import {
  buildReferenceBlock, buildReferenceSpec, parseLevelSelection,
  type BwjLevels,
} from '../web/src/core/referenceLevels.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const data = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/bwj-levels.json'), 'utf8')) as BwjLevels;
const snapshot = JSON.parse(readFileSync(
  join(ROOT, sourceById('reference').snapshotFile), 'utf8')) as Snapshot;
const scoring = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const index = new ContentIndex(snapshot);
const byId = new Map(data.levels.map((l) => [l.id, l]));

const observed = JSON.parse(readFileSync(
  join(ROOT, '../word_content_pipeline/data/reference/video-boards-20.json'),
  'utf8')) as { levels: { level: number; words_on_start: string[];
    bubbles_on_start: number; move_limit_observed: number | null }[] };

// --------------------------------------------------------------------------- //
// данные
// --------------------------------------------------------------------------- //

test('в выгрузке 1025 уровней и распилы на месте', () => {
  assert.equal(data.levels.length, 1025);
  const withChunks = data.levels.filter((l) => l.cats.some((c) => c.c?.length));
  assert.ok(withChunks.length > 700,
    `уровней с распилами ${withChunks.length}, ожидалось больше 700`);
  const l12 = byId.get(12)!;
  const chunks = l12.cats.flatMap((c) => c.c ?? []);
  assert.equal(chunks.length, 9, 'на уровне 12 оригинала девять распиленных слов');
  assert.deepEqual(chunks.find((c) => c[0] === 'august'), ['august', 'Au', 'gust']);
});

test('наблюдённые величины приехали только для записанных уровней', () => {
  const withObs = data.levels.filter((l) => l.obs);
  assert.ok(withObs.length >= 19 && withObs.length <= 20,
    `с наблюдением ${withObs.length}: записей у нас на 19-20 уровней`);
  assert.ok(withObs.every((l) => l.id <= 20),
    'наблюдение не может быть у уровня, которого нет на записях');
});

// --------------------------------------------------------------------------- //
// сборка уровня
// --------------------------------------------------------------------------- //

test('состав уровня совпадает с выгрузкой слово в слово', () => {
  for (const id of [1, 12, 200, 700, 1025]) {
    const entry = byId.get(id)!;
    const { spec } = buildReferenceSpec(index, entry);
    assert.equal(spec.categories.length, entry.cats.length, `L${id}: число категорий`);
    entry.cats.forEach((cat, i) => {
      assert.deepEqual(
        spec.categories[i].words.map((w) => w.text), cat.w,
        `L${id}: слова категории «${cat.n}» и их порядок`);
    });
  }
});

test('мета-пузырь на старте не лежит', () => {
  for (const id of [3, 7, 12, 500]) {
    const { spec } = buildReferenceSpec(index, byId.get(id)!);
    const metaTexts = new Set(spec.categories
      .flatMap((c) => c.words.filter((w) => w.kind === 'meta').map((w) => w.text)));
    for (const bubble of spec.deal.start) {
      assert.ok(!metaTexts.has(bubble.word),
        `L${id}: мета-пузырь «${bubble.word}» оказался на старте`);
    }
  }
});

test('распиленное слово занимает на поле два места', () => {
  const { spec } = buildReferenceSpec(index, byId.get(12)!);
  const chunked = new Set(byId.get(12)!.cats.flatMap((c) => (c.c ?? []).map((k) => k[0])));
  const bubbles = spec.deal.start.reduce(
    (n, b) => n + (chunked.has(b.word) ? 2 : 1), 0);
  assert.equal(bubbles, 24,
    'на записи уровня 12 старт — ровно 24 пузыря, распилы считаются за два');
});

test('распилы уезжают в спек полем halves, иначе прототип нарисует слово целым', () => {
  const { spec } = buildReferenceSpec(index, byId.get(12)!);
  assert.equal(spec.halves.length, 9, 'на уровне 12 девять распиленных слов');
  const august = spec.halves.find((h) => h.word === 'august');
  assert.deepEqual(august?.fragments, ['Au', 'gust']);
  // у уровня без распилов поле обязано остаться пустым, иначе прототип
  // включит механику половинок там, где её нет
  const plain = buildReferenceSpec(index, byId.get(1)!);
  assert.equal(plain.spec.halves.length, 0);
});

test('выкладка покрывает уровень без мета-пузырей и ничего лишнего', () => {
  for (const id of [1, 12, 333, 1025]) {
    const { spec } = buildReferenceSpec(index, byId.get(id)!);
    const dealt = [...spec.deal.start, ...spec.deal.queue].map((b) => b.word).sort();
    // мета-пузырь не раздаётся: он рождается при сборке своей категории.
    // Прототип на лишний мета-пузырь в выкладке отвечает «не сошлась» и
    // раскладывает поле сам — то есть выбрасывает порядок оригинала
    const all = spec.categories
      .flatMap((c) => c.words.filter((w) => w.kind !== 'meta').map((w) => w.text))
      .sort();
    assert.deepEqual(dealt, all, `L${id}: выкладка обязана покрыть весь уровень`);
  }
});

test('мета-пузырь не раздаётся вообще — ни на старт, ни в очередь', () => {
  for (const id of [3, 7, 12, 500]) {
    const { spec } = buildReferenceSpec(index, byId.get(id)!);
    const metaTexts = new Set(spec.categories
      .flatMap((c) => c.words.filter((w) => w.kind === 'meta').map((w) => w.text)));
    for (const bubble of [...spec.deal.start, ...spec.deal.queue]) {
      assert.ok(!metaTexts.has(bubble.word),
        `L${id}: мета-пузырь «${bubble.word}» попал в выкладку`);
    }
  }
});

// --------------------------------------------------------------------------- //
// сверка с записями оригинала
// --------------------------------------------------------------------------- //

test('стартовое поле сходится с записями на 85% слов и больше', () => {
  let hit = 0;
  let total = 0;
  for (const rec of observed.levels) {
    const entry = byId.get(rec.level);
    if (!entry) continue;
    const { spec } = buildReferenceSpec(index, entry);
    const start = new Set(spec.deal.start.map((b) => b.word));
    for (const word of rec.words_on_start) {
      total += 1;
      if (start.has(word)) hit += 1;
    }
  }
  assert.ok(total > 300, `слов для сверки ${total}, ожидалось больше 300`);
  const share = hit / total;
  assert.ok(share >= 0.85,
    `совпало ${hit}/${total} (${Math.round(share * 100)}%), порог 85% — `
    + 'замер в reference-deal-order.md §4а даёт 87%');
});

test('лимит ходов записанных уровней берётся с записи, а не считается', () => {
  for (const rec of observed.levels) {
    if (!rec.move_limit_observed) continue;
    const built = buildReferenceSpec(index, byId.get(rec.level)!);
    assert.equal(built.spec.board.moveLimit, rec.move_limit_observed,
      `L${rec.level}: лимит ходов обязан совпасть с записью`);
    assert.equal(built.moveLimitObserved, true);
  }
  // а у уровня за пределами записей честно помечено, что лимит наш
  const far = buildReferenceSpec(index, byId.get(600)!);
  assert.equal(far.moveLimitObserved, false);
  assert.ok((far.spec.board.moveLimit ?? 0) > far.spec.board.moveFloor);
});

// --------------------------------------------------------------------------- //
// пакет и выбор
// --------------------------------------------------------------------------- //

test('пакет собирается, оценивается и воспроизводится по хешу', () => {
  const ids = [1, 2, 3];
  const first = buildReferenceBlock(index, data, ids, scoring);
  const again = buildReferenceBlock(index, data, ids, scoring);
  assert.equal(first.levels.length, 3);
  assert.equal(first.missing.length, 0);
  assert.equal(first.packHash, again.packHash,
    'тот же выбор обязан давать тот же хеш пакета');
  for (const level of first.levels) {
    assert.ok(level.difficulty.value >= 1 && level.difficulty.value <= 10);
    assert.ok(level.interest.value >= 0);
    assert.equal(level.validation.passed, true,
      'уровень оригинала не бракуется нашими правилами: он сделан не по ним');
    assert.equal(level.attempts.length, 0, 'попыток подбора здесь нет по построению');
  }
});

test('несуществующий уровень попадает в missing, а не роняет сборку', () => {
  const built = buildReferenceBlock(index, data, [1, 9999], scoring);
  assert.deepEqual(built.missing, [9999]);
  assert.equal(built.levels.length, 1);
});

test('разбор выбора уровней', () => {
  assert.deepEqual(parseLevelSelection('1-3', 1025).ids, [1, 2, 3]);
  assert.deepEqual(parseLevelSelection('3, 7, 12', 1025).ids, [3, 7, 12]);
  assert.deepEqual(parseLevelSelection('1-3, 3, 10', 1025).ids, [1, 2, 3, 10],
    'повтор не должен задваивать уровень');
  assert.ok(parseLevelSelection('0-5', 1025).error, 'нулевого уровня нет');
  assert.ok(parseLevelSelection('1-2000', 1025).error, 'за пределами выгрузки');
  assert.ok(parseLevelSelection('десять', 1025).error);
  assert.ok(parseLevelSelection('', 1025).error);
});

test('источник реф-базы называется «База-реф-BWJ»', () => {
  assert.equal(sourceById('reference').label, 'База-реф-BWJ');
});
