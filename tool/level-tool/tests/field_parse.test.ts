/**
 * Разбор полей настройки блока.
 *
 * Тесты написаны по конкретной жалобе: значение в поле нельзя было заменить —
 * оставались куски прежнего. Причина была не в разборе, а в том, что конфиг не
 * принимал недонабранное и React возвращал прежний текст. Разбор вынесен сюда,
 * и главное, что здесь проверяется, — различие «пока не разобралось» (null,
 * поле в середине набора) и «разобралось» (значение).
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import {
  parseCount, parseNumberList, parseOptionalList, parseRange,
} from '../web/src/core/fieldParse.ts';

test('диапазон разбирается при любом разделителе', () => {
  assert.deepEqual(parseRange('10–14'), [10, 14]);   // длинное тире
  assert.deepEqual(parseRange('10-14'), [10, 14]);   // дефис
  assert.deepEqual(parseRange('10 14'), [10, 14]);
  assert.deepEqual(parseRange('10, 14'), [10, 14]);
});

test('половина набранного диапазона не уходит в конфиг', () => {
  // Ровно этот путь человек проходит, заменяя «7–9» на «10–14».
  assert.equal(parseRange(''), null);
  assert.equal(parseRange('1'), null);
  assert.equal(parseRange('10'), null);
  assert.equal(parseRange('10–'), null);
});

test('перевёрнутый диапазон отклоняется', () => {
  // «10–1» — неизбежный промежуточный набор на пути к «10–14». Уйди он
  // в конфиг, профиль декады пересобрался бы от мусора.
  assert.equal(parseRange('10–1'), null);
  assert.equal(parseRange('14–10'), null);
  assert.deepEqual(parseRange('10–10'), [10, 10]);   // одно значение — законно
});

test('диапазон уважает нижнюю границу', () => {
  assert.equal(parseRange('0–9', 1), null);
  assert.deepEqual(parseRange('0–9', 0), [0, 9]);
});

test('пустое числовое поле — это null, а не ноль', () => {
  // Прежний код звал Number(''), получал 0 и подставлял ноль в конфиг:
  // поле нельзя было очистить, вместо пустого оставался «0».
  assert.equal(parseCount('', 0, 4), null);
  assert.equal(parseCount('   ', 0, 4), null);
  assert.equal(parseCount('0', 0, 4), 0);
});

test('число вне границ и не-число отклоняются', () => {
  assert.equal(parseCount('5', 0, 4), null);
  assert.equal(parseCount('-1', 0, 4), null);
  assert.equal(parseCount('2.5', 0, 4), null);
  assert.equal(parseCount('abc', 0, 4), null);
  assert.equal(parseCount('3', 0, 4), 3);
});

test('список чисел терпит незаконченный набор', () => {
  assert.deepEqual(parseNumberList(''), []);
  assert.deepEqual(parseNumberList('3, '), [3]);
  assert.deepEqual(parseNumberList('3, 7'), [3, 7]);
  assert.deepEqual(parseNumberList('3,7,10'), [3, 7, 10]);
});

test('пустой необязательный список — undefined, а не пустой массив', () => {
  // Плана нет и план нулевой длины — разные вещи: без плана генератор берёт
  // коридор, а план из нуля уровней сломал бы разметку блока.
  assert.equal(parseOptionalList(''), undefined);
  assert.equal(parseOptionalList('  '), undefined);
  assert.deepEqual(parseOptionalList('5, 5, 6'), [5, 5, 6]);
});
