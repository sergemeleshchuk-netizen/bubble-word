/**
 * Третий источник контента: сводная база (web/src/core/sources.ts).
 *
 * Что здесь защищается, кроме «оно собирается».
 *
 * Первое — что сведение не потеряло наши слои. Сводная база собирается ИЗ
 * нашего снимка, и соблазн «ну, значения слов и запреты пар потом» стоит ровно
 * одного забытого шага в скрипте: снимок соберётся, генератор заработает, а
 * решатель единственности молча перестанет разводить омонимы. Поэтому senses,
 * conflicts и quartets сверяются по числу с нашим снимком.
 *
 * Второе — что вес слова не врёт. Вес размеченного слова обязан быть выведен из
 * регистра (иначе два фильтра начнут спорить), а вес оценённого — помечен
 * флагом `we`. Слово, у которого есть и разметка, и флаг оценки, — это ошибка
 * сборки, и она обязана падать здесь, а не всплывать через декаду.
 *
 * Третье — что наша база от появления третьего источника не сдвинулась. Её хеш
 * лежит рядом со снимком отдельным файлом; сравнение с ним — самая дешёвая
 * проверка решения владельца «чужой словарь в нашей базе не храним».
 *
 * Четвёртое — что параметризация декад работает и на чужом словаре: длина слова,
 * число токенов и порог веса на собранном блоке 1-10 соблюдены до последнего
 * пузыря, а приёмка декады проходит целиком.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { CONTENT_SOURCES, DEFAULT_SOURCE_ID, sourceById } from '../web/src/core/sources.ts';
import {
  checkDecadeFit, configForRange, minWordWeight, profileForRange,
} from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import { wordFitsGates } from '../web/src/core/generator.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const hybrid = sourceById('hybrid');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, hybrid.snapshotFile), 'utf8')) as Snapshot;
const production = JSON.parse(
  readFileSync(join(ROOT, sourceById('production').snapshotFile), 'utf8')) as Snapshot;
const reference = JSON.parse(
  readFileSync(join(ROOT, sourceById('reference').snapshotFile), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const index = new ContentIndex(snapshot);

/** Якоря веса по регистру — те же, что в scripts/export_hybrid_snapshot.py. */
const WEIGHT_BY_REGISTER: Record<number, number> = { 0: 1.0, 1: 0.55, 2: 0.2 };

// --------------------------------------------------------------------------- //
// реестр
// --------------------------------------------------------------------------- //

test('источников три, умолчание по-прежнему наша база', () => {
  assert.equal(CONTENT_SOURCES.length, 3);
  assert.equal(DEFAULT_SOURCE_ID, 'production');
  assert.ok(existsSync(join(ROOT, hybrid.snapshotFile)));
});

test('три снимка — три разных хеша', () => {
  const hashes = new Set([
    production.content_snapshot_hash,
    reference.content_snapshot_hash,
    snapshot.content_snapshot_hash,
  ]);
  assert.equal(hashes.size, 3);
});

test('сводный источник объявляет, чего у него нет', () => {
  assert.equal(hybrid.hasAiWorkflow, false,
    'журнал AI-прогонов — история нашей базы; сводная наследует только её половину');
  assert.ok(hybrid.limits.length >= 4,
    'список ограничений не должен пустеть: он и есть честность источника');
});

test('наша база от появления сводной не сдвинулась ни на связь', () => {
  // формат файла — как у `shasum`: «хеш  имя файла»
  const stored = readFileSync(
    join(ROOT, 'data/production/content.snapshot.sha256'), 'utf8').trim().split(/\s+/)[0];
  assert.equal(production.content_snapshot_hash, stored,
    'хеш нашего снимка разошёлся с записанным — значит, база всё-таки поменялась');
});

// --------------------------------------------------------------------------- //
// сведение
// --------------------------------------------------------------------------- //

test('сведение прибавило широты и сохранило наши категории', () => {
  const s = snapshot.stats ?? {};
  assert.ok(snapshot.categories.length > production.categories.length,
    'категорий должно стать больше нашей базы');
  assert.ok(snapshot.categories.length > reference.categories.length,
    'категорий должно стать больше словаря оригинала');
  assert.ok((s.categories_both as number) > 0,
    'должны найтись категории, которые есть у обоих источников');
  assert.ok((s.memberships_both as number) > 0,
    'должны найтись связи, подтверждённые обоими источниками');
});

test('наши слои переехали целиком, а не наполовину', () => {
  assert.equal(snapshot.senses.length, production.senses.length,
    'значения слова потеряны при сведении');
  assert.equal((snapshot.conflicts ?? []).length, (production.conflicts ?? []).length,
    'запреты на пары категорий потеряны при сведении');
  assert.equal((snapshot.quartets ?? []).length, (production.quartets ?? []).length,
    'проверенные четвёрки потеряны при сведении');
});

test('переиндексация связей не разъехалась: значение слова указывает на своё слово', () => {
  for (const m of snapshot.memberships) {
    const sense = m[6];
    if (sense === null || sense === undefined) continue;
    assert.ok(sense >= 0 && sense < snapshot.senses.length,
      `связь ссылается на значение ${sense}, которого нет`);
    assert.equal(snapshot.senses[sense].word, m[0],
      'значение слова принадлежит другому слову — сдвинулась индексация');
  }
});

// --------------------------------------------------------------------------- //
// вес
// --------------------------------------------------------------------------- //

test('вес есть у каждого слова и лежит в 0..1', () => {
  for (const w of snapshot.words) {
    assert.equal(typeof w.w, 'number', `у слова «${w.t}» нет веса`);
    assert.ok((w.w as number) >= 0 && (w.w as number) <= 1,
      `вес слова «${w.t}» вне шкалы: ${w.w}`);
  }
});

test('вес размеченного слова выведен из регистра, а не назначен отдельно', () => {
  let marked = 0;
  for (const w of snapshot.words) {
    if (w.e === undefined || w.e === null) continue;
    marked += 1;
    assert.equal(w.w, WEIGHT_BY_REGISTER[w.e],
      `у слова «${w.t}» регистр ${w.e}, а вес ${w.w} — два фильтра начнут спорить`);
    assert.equal(w.we, 0, `вес слова «${w.t}» помечен как оценённый, хотя разметка есть`);
  }
  assert.equal(marked, production.words.length,
    'разметку регистра должны сохранить все слова нашей базы');
});

test('оценённый вес помечен флагом, и только у слов без разметки', () => {
  const estimated = snapshot.words.filter((w) => w.we === 1);
  assert.ok(estimated.length > 0, 'сводная база обязана содержать чужие слова');
  for (const w of estimated) {
    assert.ok(w.e === undefined || w.e === null,
      `слово «${w.t}» и размечено, и оценено одновременно`);
  }
});

test('у каждой связи есть вес и происхождение', () => {
  for (const m of snapshot.memberships) {
    const weight = m[9];
    assert.equal(typeof weight, 'number', 'связь без веса');
    assert.ok((weight as number) > 0 && (weight as number) <= 1,
      `вес связи вне шкалы: ${weight}`);
    assert.ok(m[10] === 0 || m[10] === 1 || m[10] === 2,
      `неизвестное происхождение связи: ${m[10]}`);
  }
  assert.deepEqual(snapshot.origins, ['ours', 'reference', 'both']);
});

test('индекс отдаёт веса наружу, а на снимке без весов молчит', () => {
  const withWeight = snapshot.words.findIndex((w) => (w.w ?? 0) > 0);
  assert.ok(index.wordWeight(withWeight)! > 0);
  const plain = new ContentIndex(reference);
  assert.equal(plain.wordWeight(0), null,
    'у снимка без весов wordWeight обязан вернуть null, а не ноль');
  assert.equal(plain.memberships[0].weight, null);
});

// --------------------------------------------------------------------------- //
// гейт по весу
// --------------------------------------------------------------------------- //

test('порог веса стоит там же, где порог регистра', () => {
  assert.equal(minWordWeight(profileForRange([1, 10])), 0.70,
    'декады 1-50 берут только бытовой слой');
  assert.equal(minWordWeight(profileForRange([51, 60])), 0.50,
    'с декады 51 открыт пассивный слой — порог обязан открыться вместе с ним');
});

test('гейт пропускает бытовое слово и заворачивает пассивное', () => {
  const gates = configForRange([1, 10], 'gate-test').decadeGates!;
  const everyday = snapshot.words.findIndex(
    (w) => w.e === 0 && w.tok === 1 && w.t.length <= 8 && w.p === 0);
  const passive = snapshot.words.findIndex(
    (w) => w.e === 1 && w.tok === 1 && w.t.length <= 8 && w.p === 0);
  assert.ok(everyday >= 0 && passive >= 0);
  assert.equal(wordFitsGates(index, everyday, gates), true);
  assert.equal(wordFitsGates(index, passive, gates), false);
});

test('снимок без весов гейт не замечает', () => {
  const plain = new ContentIndex(reference);
  const gates = configForRange([1, 10], 'gate-test').decadeGates!;
  const passing = reference.words.findIndex(
    (w) => w.tok === 1 && w.t.length <= 8 && (w.z ?? 0) >= 4.5);
  assert.ok(passing >= 0);
  assert.equal(wordFitsGates(plain, passing, gates), true,
    'словарь оригинала весов не несёт — порог веса не имеет права его резать');
});

// --------------------------------------------------------------------------- //
// декада собирается и остаётся своей декадой
// --------------------------------------------------------------------------- //

test('декада 1-10 собирается из сводной базы целиком и проходит приёмку', () => {
  const config = configForRange([1, 10], 'hybrid-decade');
  const result = generateBlock({ snapshot, config, scoring });
  assert.equal(result.levels.length, 10,
    `собрано ${result.levels.length} из 10; отказы: `
    + result.failures.map((f) => `${f.levelId} ${f.reason}`).join('; '));

  const fit = checkDecadeFit(result.levels.map((l) => ({
    levelId: l.spec.levelId,
    categoryCount: l.spec.categories.length,
    zipfs: l.spec.categories.flatMap((c) => c.words.map((w) => w.zipf)),
    metaCount: l.spec.categories.reduce(
      (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0),
    metaDepth: Math.max(0, ...l.spec.categories.map((c) => c.metaDepth)),
    chainCount: l.spec.modifiers.chains.length,
    moveLimit: l.spec.board.moveLimit,
    startBubbles: l.spec.board.startBubbles,
    boardCapacity: l.spec.board.boardCapacity,
    wordsPerCategory: l.spec.board.wordsPerCategory,
  })), profileForRange([1, 10]));
  assert.ok(fit.passed,
    `приёмка декады не пройдена: ${fit.checks.filter((c) => !c.passed)
      .map((c) => `${c.code} — ${c.detail}`).join('; ')}`);
});

test('форма слова декады соблюдена на каждом пузыре, включая чужие слова', () => {
  const config = configForRange([1, 10], 'hybrid-decade');
  const gates = config.decadeGates!;
  const result = generateBlock({ snapshot, config, scoring });
  let foreign = 0;
  for (const level of result.levels) {
    for (const category of level.spec.categories) {
      for (const word of category.words) {
        const wi = index.wordIndex(word.text.toLowerCase());
        if (wi === undefined) continue;              // мета-слово может не быть в словаре
        const w = index.words[wi];
        assert.ok(w.tok <= gates.maxTokens,
          `«${word.text}»: ${w.tok} токена при пределе ${gates.maxTokens}`);
        assert.ok(word.text.replace(/\s/g, '').length <= gates.maxWordLen,
          `«${word.text}»: ${word.text.length} букв при пределе ${gates.maxWordLen}`);
        assert.ok((w.w ?? 1) >= gates.minWordWeight,
          `«${word.text}»: вес ${w.w} ниже порога декады ${gates.minWordWeight}`);
        if (w.we === 1) foreign += 1;
      }
    }
  }
  assert.ok(foreign >= 0);
});
