/**
 * Версионность — обещание, которое легко нарушить молча.
 *
 * Здесь проверяется три вещи, каждая из которых уже ломалась бы незаметно:
 *   1. версию нельзя поднять, не описав, что изменилось;
 *   2. в наборе версий нет пустых значений — пустая строка врала бы,
 *      что модель существует;
 *   3. версия инструмента НЕ участвует в хеше уровня. Это структурная гарантия:
 *      если hashing.ts однажды импортирует version.ts, релиз вёрстки начнёт
 *      менять хеши сданных пакетов, и регрессия по ним обнулится.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { SOLVER_VERSION, TOOL_VERSION, versionSet } from '../web/src/core/version.ts';
import { GENERATOR_VERSION } from '../web/src/core/generator.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

test('версия инструмента — корректный semver', () => {
  assert.match(TOOL_VERSION, /^\d+\.\d+\.\d+$/,
    `TOOL_VERSION должен быть semver, получено «${TOOL_VERSION}»`);
});

test('package.json и version.ts не разъезжаются', () => {
  const pkg = JSON.parse(readFileSync(join(ROOT, 'package.json'), 'utf8')) as
    { version: string };
  assert.equal(pkg.version, TOOL_VERSION,
    'версия в package.json и TOOL_VERSION разошлись: '
    + 'источник правды — version.ts, package.json синхронизируется по нему');
});

test('у текущей версии есть строка в CHANGELOG', () => {
  const changelog = readFileSync(join(ROOT, 'CHANGELOG.md'), 'utf8');
  assert.ok(changelog.includes(`## ${TOOL_VERSION}`),
    `в CHANGELOG.md нет раздела «## ${TOOL_VERSION}»: `
    + 'версию подняли, а что изменилось — не написали');
});

test('набор версий полон и без пустых значений', () => {
  const versions = versionSet(scoring, snapshot.content_snapshot_hash);

  assert.deepEqual(Object.keys(versions).sort(), [
    'contentSnapshot', 'difficultyModel', 'funModel', 'generator', 'solver', 'tool',
  ]);
  for (const [key, value] of Object.entries(versions)) {
    assert.ok(typeof value === 'string' && value.length > 0,
      `версия ${key} пустая: набор версий обязан быть честным`);
  }

  assert.equal(versions.tool, TOOL_VERSION);
  assert.equal(versions.generator, GENERATOR_VERSION);
  assert.equal(versions.solver, SOLVER_VERSION);
  assert.equal(versions.difficultyModel, scoring.scoring_version);
  assert.equal(versions.funModel, scoring.interest.scoring_version);
});

test('версия инструмента не участвует в хешировании уровня', () => {
  const source = readFileSync(join(ROOT, 'web/src/core/hashing.ts'), 'utf8');

  assert.ok(!source.includes('version.ts'),
    'hashing.ts импортирует version.ts: релиз инструмента начнёт менять хеши');
  assert.ok(!source.includes('TOOL_VERSION'),
    'TOOL_VERSION попал в хеширование: «тот же вход → тот же уровень» больше не верно');

  // В хеш входит ровно пять вещей, и generator_version среди них — единственная версия.
  for (const key of ['level_spec', 'seed', 'config', 'generator_version',
    'content_snapshot_hash']) {
    assert.ok(source.includes(key), `в levelSpecHash пропало поле ${key}`);
  }
});
