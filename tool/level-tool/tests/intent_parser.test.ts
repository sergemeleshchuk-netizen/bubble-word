/**
 * Разбор промпта для генерации набора уровней.
 *
 * Экран обещает человеку простую вещь: «инструмент показывает, как понял ваши
 * слова». Обещание держится ровно до тех пор, пока разбор понимает то, что
 * человек реально пишет, — а пишет он в первую очередь СКОЛЬКО уровней делать.
 * Раньше это число не читалось вовсе: промпт «сделай 10 уровней в линейке
 * 150-160» молча собирал пресет 201-210, и заметить подмену можно было только
 * по номерам в готовом пакете.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_INTENT_PROMPT, parseIntent } from '../web/src/core/intentParser.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/lexicon.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const CURRENT: [number, number] = [201, 210];

test('число уровней читается и задаёт длину блока', () => {
  const { patch } = parseIntent('сделай 6 уровней', CURRENT);
  assert.deepEqual(patch.levelRange, [201, 206],
    'без диапазона счёт отмеряется от начала применённого блока');
});

test('диапазон без счёта берётся как есть', () => {
  const { patch } = parseIntent('уровни 150-160', CURRENT);
  assert.deepEqual(patch.levelRange, [150, 160]);
});

/**
 * Спорный случай, ради которого всё и затевалось. «10 уровней в линейке 150-160»
 * — это 10 уровней или 11? Побеждает счёт: его человек называет прямо. Обе
 * фразы обязаны попасть в таблицу интерпретации, иначе расхождение не увидеть.
 */
test('счёт сильнее диапазона, и обе фразы видны в разборе', () => {
  const { patch, matches } = parseIntent('сделай 10 уровней в линейке 150-160', CURRENT);
  assert.deepEqual(patch.levelRange, [150, 159]);
  const rangeMatches = matches.filter((m) => m.field === 'levelRange');
  assert.equal(rangeMatches.length, 2,
    'в таблице должны быть обе фразы: и диапазон, и счёт');
});

test('бессмысленный счёт игнорируется, а не ломает блок', () => {
  assert.equal(parseIntent('сделай 400 уровней', CURRENT).patch.levelRange, undefined);
  assert.equal(parseIntent('сделай 1 уровень', CURRENT).patch.levelRange, undefined);
});

/**
 * «Два пика в середине и конце» союз «и» разрезает пополам, и место второго
 * пика терялось: разбор видел «два пика в середине» и обрубок «конце».
 */
test('места пиков читаются из фразы целиком', () => {
  const { patch, unrecognized } = parseIntent(
    'два пика в середине и конце', CURRENT);
  assert.deepEqual(patch.spikePositions, [5, 9]);
  assert.deepEqual(unrecognized, [], 'обрубок «конце» не жалоба, а часть фразы про пики');
});

test('позиции считаются от длины блока, а не константами', () => {
  const { patch } = parseIntent('сделай 6 уровней, пик в конце', CURRENT);
  assert.deepEqual(patch.levelRange, [201, 206]);
  assert.deepEqual(patch.spikePositions, [5], 'конец блока из шести — это пятая позиция');
});

test('«передышка после пиков» ставит её следом за каждым пиком', () => {
  const { patch } = parseIntent('два пика в середине и конце, передышка после пиков', CURRENT);
  assert.deepEqual(patch.spikePositions, [5, 9]);
  assert.deepEqual(patch.recoveryPositions, [6, 10]);
});

test('«меньше сложных слов» — это редкость, а не исключение темы', () => {
  const { patch } = parseIntent('меньше сложных слов', CURRENT);
  // 1-2 редких слова на уровень: решение владельца 04.08 (вечер), было 5-8
  assert.deepEqual(patch.rarityRange, [1, 2]);
  assert.equal(patch.excludeThemes, undefined,
    'слово «слов» не должно вычёркивать тему language');
});

/**
 * Пример в поле — обещание того, что инструмент понимает. Остаток в «не понято»
 * означал бы, что мы сами учим писать неработающие запросы.
 */
test('предзаполненный промпт разбирается без остатка', () => {
  const parsed = parseIntent(DEFAULT_INTENT_PROMPT, DEFAULT_BLOCK_CONFIG.levelRange);
  assert.deepEqual(parsed.unrecognized, []);
  assert.deepEqual(parsed.patch.levelRange, [121, 130], 'просили 10 уровней от 121');
  assert.deepEqual(parsed.patch.spikePositions, [5, 9]);
  assert.deepEqual(parsed.patch.recoveryPositions, [6, 10]);
  assert.ok((parsed.patch.includeThemes ?? []).length >= 3,
    `вайб-теги должны дать темы, получено: ${parsed.patch.includeThemes}`);
});

/**
 * И главное: по этому промпту блок обязан СОБИРАТЬСЯ. Разобрать текст в конфиг,
 * который потом ничего не генерирует, — худший вид работающей кнопки.
 *
 * Здесь же проверяется правило применения: диапазон из промпта пересобирает
 * профиль декады целиком. Без этого номера были бы из 150-х, а коридор
 * категорий и редкость — от пресета 201-210.
 */
test('по предзаполненному промпту блок собирается целиком', () => {
  const parsed = parseIntent(DEFAULT_INTENT_PROMPT, DEFAULT_BLOCK_CONFIG.levelRange);
  const config = {
    ...configForRange(parsed.patch.levelRange!, DEFAULT_BLOCK_CONFIG.seed),
    ...parsed.patch,
  };
  assert.ok(checkBlockRhythm(buildBlockPlan(config)).passed,
    'ритм блока должен быть пилой');

  const block = generateBlock({ snapshot, config, scoring });
  assert.equal(block.levels.length, 10);
  assert.deepEqual(block.failures, []);
  for (const level of block.levels) {
    assert.ok(level.validation.passed, `уровень ${level.spec.levelId} не прошёл инварианты`);
    assert.equal(level.solutions.count, 1,
      `уровень ${level.spec.levelId}: решений ${level.solutions.count}, должно быть одно`);
  }
  assert.deepEqual(block.levels.map((l) => l.spec.levelId),
    [121, 122, 123, 124, 125, 126, 127, 128, 129, 130]);
});
