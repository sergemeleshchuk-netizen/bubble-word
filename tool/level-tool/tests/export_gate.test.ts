/**
 * Гейт экспорта — тот же, что у генерации.
 *
 * Дефект, который тест закрывает (аудит 03.08): экран экспорта обещал «экспорт
 * разрешён только после hard-проверок», считал при этом только `validation.passed`
 * и число решений, а кнопки скачивания оставлял живыми в любом случае. Мимо
 * проверки проходила и динамическая проходимость — то есть уровень с вручную
 * переложенным стартом мог не доигрываться и всё равно уехать в файл.
 *
 * Проверяем два разных утверждения, и оба нужны:
 *   1) сам предикат отказывает по каждому hard-условию по отдельности;
 *   2) экран экспорта пользуется ИМЕННО им, а не своей копией условий.
 * Второе — чтением исходника: разъехаться два списка условий могут только
 * тогда, когда их два, и никакой тест на поведение UI этого не заметит,
 * пока копия ещё случайно совпадает с оригиналом.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { hardGateFailure } from '../web/src/core/generateBlock.ts';
import type { PlayabilityResult } from '../web/src/core/simulatePlayability.ts';
import type { SolutionCount, ValidationIssue } from '../web/src/core/types.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const unique: SolutionCount = { count: 1, nodesVisited: 10, exhausted: true };

const playable: PlayabilityResult = {
  winnable: true, failReason: null, movesNeeded: 12, moveLimit: 20,
  spareMoves: 8, rescues: 0, perceivedDead: 0,
} as PlayabilityResult;

const passing = { solutions: unique, hardIssues: [], playability: playable, chained: false };

test('уровень, прошедший всё, экспортируется', () => {
  assert.equal(hardGateFailure(passing), null);
});

test('две раскладки — экспорт запрещён, и в причине названы спорные категории', () => {
  const failure = hardGateFailure({
    ...passing,
    solutions: {
      count: 2, nodesVisited: 99, exhausted: false,
      secondSolutionExample: [
        { category: 'FRUITS', words: ['apple'] },
        { category: 'RED THINGS', words: ['apple'] },
      ],
    },
  });
  assert.ok(failure, 'двусмысленный уровень обязан блокировать экспорт');
  assert.equal(failure.stage, 'единственность решения');
  assert.match(failure.reason, /FRUITS и RED THINGS/);
});

test('ни одной раскладки — тоже отказ, но с другой причиной', () => {
  const failure = hardGateFailure({
    ...passing, solutions: { count: 0, nodesVisited: 5, exhausted: true },
  });
  assert.ok(failure);
  assert.match(failure.reason, /ни одной полной раскладки/);
});

test('hard-нарушение валидатора блокирует экспорт и попадает в причину', () => {
  const issue: ValidationIssue = {
    code: 'BUBBLE_COUNT', severity: 'hard',
    message: 'пузырей на поле больше вместимости', entities: ['201'],
  };
  const failure = hardGateFailure({ ...passing, hardIssues: [issue] });
  assert.ok(failure);
  assert.equal(failure.stage, 'валидация');
  assert.match(failure.reason, /BUBBLE_COUNT/);
});

test('непроходимый уровень блокирует экспорт: решается на бумаге — мало', () => {
  const failure = hardGateFailure({
    ...passing,
    playability: { ...playable, winnable: false, failReason: 'ходы кончились' },
  });
  assert.ok(failure);
  assert.equal(failure.stage, 'проходимость');
  assert.match(failure.reason, /ходы кончились/);
});

test('сломанный ритм блокирует экспорт, хотя уровень доигрывается', () => {
  const failure = hardGateFailure({
    ...passing, playability: { ...playable, rescues: 2, perceivedDead: 1 },
  });
  assert.ok(failure, 'досыпки вне ритма — такой же отказ, как непроходимость');
  assert.match(failure.reason, /досыпок вне ритма 2/);
});

test('цепь-линия освобождена от ритма: прототип снимает её сам', () => {
  assert.equal(hardGateFailure({
    ...passing, chained: true, playability: { ...playable, rescues: 2, perceivedDead: 1 },
  }), null);
});

test('не посчитанная проходимость — это отказ, а не «проверка пройдена»', () => {
  const failure = hardGateFailure({ ...passing, playability: undefined });
  assert.ok(failure, 'отсутствие результата симуляции не должно читаться как PASS');
  assert.equal(failure.stage, 'проходимость');
});

test('экран экспорта пользуется общим гейтом, а не своей копией условий', () => {
  const view = readFileSync(join(ROOT, 'web/src/components/ExportView.tsx'), 'utf8');
  assert.match(view, /levelHardGateFailure/,
    'ExportView обязан звать общий гейт: своя копия условий разъедется с генерацией');
  // и кнопки обязаны на него смотреть, а не просто рисовать плашку
  assert.match(view, /disabled=\{singleFailure !== null\}/,
    'кнопка «Скачать уровень» не блокируется отказом гейта');
  assert.match(view, /disabled=\{!exportAllowed\}/,
    'кнопка «Скачать весь пакет» не блокируется отказом гейта');
});
