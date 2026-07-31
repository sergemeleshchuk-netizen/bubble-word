/**
 * Модификаторы прототипа: инварианты раскладки.
 *
 * Модификатор меняет только раскладку в playable, но ошибиться здесь так же
 * легко, как в генераторе: половинка, совпавшая со словом уровня, ломает
 * механику; два пузыря в одном слоте накладываются друг на друга; цепь, у которой
 * на старте нет ни одного мерджа внутри зоны, делает первый ход невозможным.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

import { buildSetup, slotGrid, MODIFIERS } from '../web/src/core/playableModifiers.ts';
import type { PlayableModifier } from '../web/src/core/playableModifiers.ts';
import { buildSpec, levelCategory, validLevel, word } from './fixtures/synthetic.ts';

/** Уровень пошире: с 4 категориями модификаторам почти негде развернуться. */
function wideLevel() {
  const categories = [
    levelCategory('colors', 'COLORS', [
      word('crimson', 4.0), word('magenta', 3.6), word('indigo', 3.7), word('scarlet', 3.5)],
      { theme: 'properties' }),
    levelCategory('fruits', 'FRUITS', [
      word('apricot', 3.9), word('banana', 4.2), word('cherry', 4.0), word('avocado', 3.8)],
      { theme: 'food' }),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('chisel', 3.4), word('pliers', 3.6), word('wrench', 3.5)],
      { theme: 'tools' }),
    levelCategory('weather', 'WEATHER', [
      word('thunder', 4.3), word('drizzle', 3.3), word('blizzard', 3.4), word('tornado', 3.9)],
      { theme: 'nature' }),
    levelCategory('planets', 'PLANETS', [
      word('mercury', 3.8), word('jupiter', 3.9), word('saturn', 3.9), word('neptune', 3.5)],
      { theme: 'space' }),
    levelCategory('animals', 'ANIMALS', [
      word('leopard', 3.7), word('giraffe', 3.6), word('dolphin', 3.9), word('penguin', 3.8)],
      { theme: 'nature' }),
  ];
  return buildSpec(207, categories);
}

const ALL: PlayableModifier[] = MODIFIERS.map((m) => m.id);

// --------------------------------------------------------------------------- //
// общие инварианты
// --------------------------------------------------------------------------- //

test('раскладка детерминирована: тот же уровень и модификатор — та же расстановка', () => {
  for (const modifier of ALL) {
    const a = buildSetup(wideLevel(), modifier);
    const b = buildSetup(wideLevel(), modifier);
    assert.deepEqual(
      a.board.map((x) => [x.words, x.slot, x.ice, x.hidden]),
      b.board.map((x) => [x.words, x.slot, x.ice, x.hidden]),
      `${modifier}: раскладка не воспроизводится`);
    assert.deepEqual(a.chain, b.chain, `${modifier}: цепь не воспроизводится`);
  }
});

test('слоты не пересекаются и лежат внутри поля', () => {
  for (const modifier of ALL) {
    const setup = buildSetup(wideLevel(), modifier);
    const slots = setup.board.map((b) => b.slot);
    assert.equal(new Set(slots).size, slots.length, `${modifier}: два пузыря в одном слоте`);
    for (const s of setup.slots) {
      assert.ok(s.x >= 5 && s.x <= 95, `слот вне поля по x: ${s.x}`);
      assert.ok(s.y >= 5 && s.y <= 95, `слот вне поля по y: ${s.y}`);
    }
  }
});

test('на поле не больше board_capacity пузырей, остальные в очереди', () => {
  const spec = wideLevel();
  for (const modifier of ALL) {
    const setup = buildSetup(spec, modifier);
    assert.ok(setup.board.length <= spec.board.boardCapacity,
      `${modifier}: на поле ${setup.board.length} при capacity ${spec.board.boardCapacity}`);
    // распил добавляет ровно один пузырь на распиленное слово, остальное — как в спеке
    const all = [...setup.board, ...setup.queue];
    const pairs = new Set(all.filter((b) => b.kind === 'half').map((b) => b.pair!.id)).size;
    assert.equal(all.length, spec.board.startBubbles + pairs,
      `${modifier}: пузырей ${all.length}, слов уровня ${spec.board.startBubbles}, `
      + `распилов ${pairs}`);
  }
});

test('каждая позиция досыпки — существующий слот', () => {
  const setup = buildSetup(wideLevel(), 'none');
  assert.equal(new Set(setup.refillOrder).size, setup.slots.length);
  for (const s of setup.refillOrder) {
    assert.ok(s >= 0 && s < setup.slots.length, `слот досыпки вне сетки: ${s}`);
  }
});

test('слоты покрывают всю высоту поля: 25-й пузырь не уезжает за границу', () => {
  const slots = slotGrid(24);
  assert.equal(slots.length, 24);
  assert.ok(Math.max(...slots.map((s) => s.y)) <= 95);
});

// --------------------------------------------------------------------------- //
// половинки
// --------------------------------------------------------------------------- //

test('половинки: не больше одного распила в категории и не больше трёх на уровень', () => {
  const spec = wideLevel();
  const setup = buildSetup(spec, 'halves');
  const halves = [...setup.board, ...setup.queue].filter((b) => b.kind === 'half');
  const pairs = new Set(halves.map((b) => b.pair!.id));
  assert.ok(pairs.size >= 1, 'ни одного распила: механику нечего показать');
  assert.ok(pairs.size <= 3, `распилов ${pairs.size}, это уже фон, а не акцент`);
  assert.equal(halves.length, pairs.size * 2, 'у распила должно быть ровно две половинки');

  const home = new Map<string, string>();
  for (const c of spec.categories) for (const w of c.words) home.set(w.text, c.key);
  const perCategory = new Map<string, number>();
  for (const b of halves) {
    if (b.pair!.side !== 0) continue;
    const key = home.get(b.pair!.whole)!;
    perCategory.set(key, (perCategory.get(key) ?? 0) + 1);
  }
  for (const [key, n] of perCategory) {
    assert.ok(n <= 1, `в категории ${key} распилено ${n} слов`);
  }
  assert.ok(perCategory.size < spec.categories.length,
    'распилены все категории: должна быть затронута только часть');
});

test('половинки: фрагмент не совпадает ни со словом уровня, ни с другим фрагментом', () => {
  const spec = wideLevel();
  const setup = buildSetup(spec, 'halves');
  const levelWords = new Set<string>();
  for (const c of spec.categories) for (const w of c.words) levelWords.add(w.text.toLowerCase());
  const fragments: string[] = [];
  for (const b of [...setup.board, ...setup.queue]) {
    if (b.kind !== 'half') continue;
    const fragment = b.words[0].toLowerCase();
    assert.ok(!levelWords.has(fragment), `фрагмент ${fragment} — слово уровня`);
    assert.ok(fragment.length >= 2, `фрагмент ${fragment} слишком короткий`);
    fragments.push(fragment);
  }
  assert.equal(new Set(fragments).size, fragments.length, 'два одинаковых фрагмента');
});

test('половинки: склейки учтены в лимите ходов', () => {
  const spec = wideLevel();
  const setup = buildSetup(spec, 'halves');
  const pairs = new Set([...setup.board, ...setup.queue]
    .filter((b) => b.kind === 'half').map((b) => b.pair!.id)).size;
  assert.equal(setup.floor, spec.categories.length * 3 + pairs);
  assert.ok(setup.moveLimit! > spec.board.moveLimit!,
    'лимит должен вырасти: склейка половинок тратит ход');
});

// --------------------------------------------------------------------------- //
// лёд и скрытые слова
// --------------------------------------------------------------------------- //

for (const modifier of ['ice', 'hidden'] as const) {
  const field = modifier === 'ice' ? 'ice' : 'hidden';
  test(`${modifier}: блокируется несколько пузырей, по одному на категорию, со счётчиком`, () => {
    const spec = wideLevel();
    const setup = buildSetup(spec, modifier);
    const marked = setup.board.filter((b) => b[field] > 0);
    assert.ok(marked.length >= 1 && marked.length <= 2,
      `заблокировано ${marked.length} пузырей`);
    assert.equal(setup.queue.filter((b) => b[field] > 0).length, 0,
      'блокировка в очереди: игрок её не увидит');
    const home = new Map<string, string>();
    for (const c of spec.categories) for (const w of c.words) home.set(w.text, c.key);
    const categories = marked.map((b) => home.get(b.words[0])!);
    assert.equal(new Set(categories).size, categories.length,
      'две блокировки в одной категории');
    for (const b of marked) {
      assert.ok(b[field] >= 2 && b[field] <= 3, `счётчик ${b[field]} вне 2-3`);
    }
    assert.ok(setup.moveLimit! > spec.board.moveLimit!, 'блокировка должна дать запас ходов');
  });
}

// --------------------------------------------------------------------------- //
// цепь
// --------------------------------------------------------------------------- //

test('цепь: отделяет примерно треть поля и снимается сбором категорий', () => {
  const spec = wideLevel();
  const setup = buildSetup(spec, 'chain');
  assert.ok(setup.chain, 'цепь не поставлена');
  const { y, need } = setup.chain!;
  assert.ok(need >= 1 && need <= 2, `счётчик цепи ${need}`);

  const below = setup.slots.filter((s) => s.y > y).length / setup.slots.length;
  assert.ok(below > 0.2 && below < 0.45,
    `под цепью ${(below * 100).toFixed(0)}% слотов — это не «нижняя часть поля»`);

  // старт не должен быть мёртвым: хотя бы один мердж возможен, не пересекая цепь.
  // Собираемость всего уровня цепь не гарантирует — за это отвечает страховка
  // прототипа (снимает цепь, когда легальных мерджей не осталось), поэтому
  // проверяется именно первый ход.
  const home = new Map<string, string>();
  for (const c of spec.categories) for (const w of c.words) home.set(w.text, c.key);
  const pairs = setup.board.flatMap((a, i) => setup.board.slice(i + 1)
    .filter((b) => home.get(a.words[0]) === home.get(b.words[0])
      && (setup.slots[a.slot].y > y) === (setup.slots[b.slot].y > y)));
  assert.ok(pairs.length > 0, 'на старте нет ни одного мерджа в пределах одной зоны');
});

test('без модификатора уровень остаётся тем же, что в спеке', () => {
  const spec = validLevel();
  const setup = buildSetup(spec, 'none');
  assert.equal(setup.chain, null);
  assert.equal(setup.moveLimit, spec.board.moveLimit);
  assert.equal(setup.difficultyDelta, 0);
  assert.equal(setup.board.length + setup.queue.length, spec.board.startBubbles);
  assert.equal(setup.board.filter((b) => b.ice || b.hidden || b.kind === 'half').length, 0);
});
