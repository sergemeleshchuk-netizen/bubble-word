/**
 * Формы слов и имён: `web/src/core/wordForms.ts`.
 *
 * Модуль появился 04.08 потому, что правило двойников жило в двух копиях —
 * в генераторе и в правиле приёмки, — и копии разошлись: генератор знал про
 * `city` → `cities`, приёмка нет. Тесты здесь закрепляют оба соглашения, от
 * которых зависят и генератор, и приёмка.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import {
  isNearDuplicate, labelTokens, namesTooClose, nearDuplicateForms,
} from '../web/src/core/wordForms.ts';

test('двойники: множественное число, -es и -y → -ies', () => {
  for (const [a, b] of [
    ['star', 'stars'], ['bird', 'birds'], ['box', 'boxes'], ['city', 'cities'],
    ['border', 'borders'],
  ] as const) {
    assert.ok(isNearDuplicate(a, b), `${a} и ${b} обязаны считаться двойниками`);
    assert.ok(isNearDuplicate(b, a), 'правило симметрично');
  }
  for (const [a, b] of [
    ['star', 'moon'], ['border', 'boarder'], ['map', 'trap'], ['area', 'ares'],
  ] as const) {
    assert.ok(!isNearDuplicate(a, b), `${a} и ${b} — разные слова`);
  }
});

/**
 * Быстрая проверка двойников в генераторе спрашивает не «переберём все слова
 * уровня», а «есть ли на уровне одно из написаний кандидата». Оба пути обязаны
 * давать один ответ, иначе перебор начнёт пропускать пары, которые приёмка потом
 * забракует, — и уровень уйдёт в отказ на последнем шаге.
 */
test('nearDuplicateForms совпадает с isNearDuplicate пара-в-пару', () => {
  const words = ['star', 'stars', 'city', 'cities', 'box', 'boxes', 'border',
    'borders', 'map', 'maps', 'area', 'sun', 'bus', 'buses', 'lily', 'lilies'];
  for (const a of words) {
    const forms = new Set(nearDuplicateForms(a));
    for (const b of words) {
      assert.equal(forms.has(b), isNearDuplicate(a, b),
        `${a} / ${b}: быстрый путь и правило расходятся`);
    }
  }
});

test('подпись разбирается на слова, ключ базы не используется', () => {
  assert.deepEqual(labelTokens('MAP WORDS'), ['map', 'words']);
  assert.deepEqual(labelTokens('BIRDS OF PREY'), ['birds', 'of', 'prey']);
  assert.deepEqual(labelTokens('ROCK-POP'), ['rock', 'pop']);
});

test('имена-близнецы: вложенность запрещена, общее слово — нет', () => {
  for (const [a, b] of [
    ['MAP', 'MAP WORDS'], ['CHESS', 'CHESS TERMS'], ['BIRDS', 'BIRDS OF PREY'],
    ['COUNTRIES', 'ISLAND COUNTRIES'], ['BIRD', 'BIRDS OF PREY'],
  ] as const) {
    assert.ok(namesTooClose(a, b), `«${a}» и «${b}» на одно поле ставить нельзя`);
    assert.ok(namesTooClose(b, a), 'правило симметрично');
  }
  // родовое слово в обоих именах парой не делает: игрок различает их по первому
  for (const [a, b] of [
    ['MAP WORDS', 'PARK WORDS'], ['DESERTS', 'MAP'], ['SKY', 'COLORS'],
    ['ISLAND COUNTRIES', 'COASTAL CITIES'],
  ] as const) {
    assert.ok(!namesTooClose(a, b), `«${a}» и «${b}» рядом стоять можно`);
  }
});
