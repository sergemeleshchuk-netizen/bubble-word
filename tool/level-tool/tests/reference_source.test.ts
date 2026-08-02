/**
 * Второй источник контента: словарь оригинала (web/src/core/sources.ts).
 *
 * Что здесь защищается, кроме «оно собирается».
 *
 * Первое — что второй источник не притворяется первым. У выгрузки нет статусов
 * связи, значений слова и разметки имён собственных. Стоит одному из этих слоёв
 * «появиться» в снимке (например, кто-то проставит `alternative` на глазок,
 * чтобы включились ловушки), — и разница между источниками перестанет быть
 * разницей в данных. Проверяем прямо: слои отсутствуют.
 *
 * Второе — что появление второго источника не сдвинуло первый. Реестр обязан
 * держать нашу базу источником по умолчанию, а её снимок — лежать на прежнем
 * месте. Переключатель, который меняет умолчание, сделал бы сдаваемые пакеты
 * невоспроизводимыми у того, кто просто открыл инструмент.
 *
 * Третье — что шкалы двух источников сравнимы: сложность категории и
 * очевидность связи посчитаны разными способами (у выгрузки нет исходных
 * данных), но обязаны лежать в тех же границах. Иначе один и тот же гейт
 * означает на двух источниках разное, и сравнение прогонов бессмысленно.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { CONTENT_SOURCES, DEFAULT_SOURCE_ID, sourceById } from '../web/src/core/sources.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const reference = sourceById('reference');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, reference.snapshotFile), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

// --------------------------------------------------------------------------- //
// реестр источников
// --------------------------------------------------------------------------- //

test('умолчание — словарь игры, и снимок каждого источника на месте', () => {
  assert.equal(DEFAULT_SOURCE_ID, 'lexicon');
  for (const source of CONTENT_SOURCES) {
    assert.ok(existsSync(join(ROOT, source.snapshotFile)),
      `нет снимка источника ${source.id}: ${source.snapshotFile}`);
  }
});

test('чужой источник объявляет, чего у него нет', () => {
  assert.equal(reference.hasAiWorkflow, false,
    'журнал AI-прогонов — история нашей базы, у выгрузки его быть не может');
  assert.ok(reference.limits.length >= 4,
    'список ограничений не должен пустеть: он и есть честность источника');
});

test('снимки двух источников — разные снимки', () => {
  const production = JSON.parse(readFileSync(
    join(ROOT, sourceById('production').snapshotFile), 'utf8')) as Snapshot;
  assert.notEqual(production.content_snapshot_hash, snapshot.content_snapshot_hash);
});

// --------------------------------------------------------------------------- //
// слои, которых у выгрузки нет
// --------------------------------------------------------------------------- //

test('у выгрузки нет слоёв разметки, и она их не выдумывает', () => {
  assert.equal(snapshot.senses.length, 0, 'значений слова источник не знает');
  assert.equal(snapshot.conflicts?.length ?? 0, 0, 'запретов на пары источник не объявляет');
  assert.ok(snapshot.memberships.every((m) => m[2] === 0),
    'все связи approved: выгрузка — ключ ответов, оттенков в ней нет');
  assert.ok(snapshot.memberships.every((m) => m[6] === null),
    'связь не может ссылаться на значение слова, которого нет');
  assert.ok(snapshot.words.every((w) => w.p === 0),
    'регистр в выгрузке потерян — имена собственные размечать нечем');
});

test('шкалы сравнимы с нашей базой', () => {
  const constants = snapshot.constants;
  assert.equal(constants.top50k_zipf, 2.55);
  assert.equal(constants.quickwin_zipf, 3.0);

  for (const c of snapshot.categories) {
    if (c.d === null || c.d === undefined) continue;
    assert.ok(c.d >= 0.1 && c.d <= 0.7,
      `сложность категории ${c.k} вне шкалы нашей базы: ${c.d}`);
  }
  for (const m of snapshot.memberships) {
    assert.ok(m[4] >= 0.3 && m[4] <= 0.9,
      `очевидность связи вне объявленных границ: ${m[4]}`);
  }
});

test('вложенность оригинала доехала мета-парами', () => {
  const index = new ContentIndex(snapshot);
  assert.ok(snapshot.meta_capable.length > 500,
    `мета-пригодных категорий ${snapshot.meta_capable.length}: вложенность потерялась`);
  for (const mc of snapshot.meta_capable) {
    assert.ok(mc.hosts.length > 0, 'мета-пара без родителя бессмысленна');
    assert.ok(!mc.hosts.includes(mc.category), 'категория не может быть родителем сама себе');
    assert.equal(index.categoryOfLabelWord(mc.word), mc.category);
  }
});

// --------------------------------------------------------------------------- //
// генерация
// --------------------------------------------------------------------------- //

test('блок собирается из словаря оригинала тем же генератором', () => {
  const config = configForRange([11, 20], 'reference-source-test');
  const block = generateBlock({ snapshot, config, scoring });

  assert.ok(block.levels.length >= 9,
    `собрано ${block.levels.length} из 10: ${block.failures[0]?.reason ?? ''}`);
  for (const level of block.levels) {
    const hard = level.validation.issues.filter((i) => i.severity === 'hard');
    assert.equal(hard.length, 0,
      `уровень ${level.spec.levelId}: ${hard.map((i) => i.code).join(', ')}`);
    assert.equal(level.solutions.count, 1,
      `уровень ${level.spec.levelId} раскладывается не единственным способом`);
  }
  assert.equal(block.contentSnapshotHash, snapshot.content_snapshot_hash,
    'пакет обязан нести хеш того снимка, из которого собран');
});

test('генерация из второго источника так же воспроизводима', () => {
  const config = configForRange([31, 40], 'reference-determinism');
  const first = generateBlock({ snapshot, config, scoring });
  const second = generateBlock({ snapshot, config, scoring });
  assert.equal(first.packHash, second.packHash);
});
