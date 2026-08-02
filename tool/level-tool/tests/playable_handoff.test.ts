/**
 * Передача пакета в играбельный прототип.
 *
 * Контракт здесь межпроектный: пакет пишет инструмент (TypeScript), а читают
 * `site/index.html` и `site/playable/index.html` — обычный HTML, который tsc
 * не проверяет. Поэтому форма пакета закреплена тестом: если она поедет,
 * прототип молча покажет пустой уровень, и понять причину будет нечем.
 *
 * Отдельно проверяется мета-пузырь. Прототип определяет его сам: слово, равное
 * имени другой категории уровня, становится мета-словом. Значит, слова обязаны
 * уезжать строками, а имя категории — совпадать с текстом мета-пузыря.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { HANDOFF_KEY, buildHandoffPack } from '../web/src/core/playableHandoff.ts';
import { TOOL_VERSION } from '../web/src/core/version.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
const pack = buildHandoffPack(block);

test('группа названа версией инструмента и хешем пакета', () => {
  assert.equal(pack.label, `v${TOOL_VERSION} · ${block.packHash.slice(0, 12)}`);
  assert.equal(pack.tool_version, TOOL_VERSION);
  assert.equal(pack.pack_hash, block.packHash);
});

test('в пакет уходят все собранные уровни', () => {
  assert.equal(pack.levels.length, block.levels.length);
  assert.deepEqual(pack.levels.map((l) => l.level_id),
    block.levels.map((l) => l.spec.levelId));
});

test('прототип получает имя категории и ровно четыре слова строками', () => {
  for (const level of pack.levels) {
    assert.ok(level.categories.length >= 5, `уровень ${level.level_id}: мало категорий`);
    for (const category of level.categories) {
      assert.equal(typeof category.name, 'string');
      assert.ok(category.name.length > 0, 'имя категории пустое');
      assert.equal(category.words.length, 4,
        `${category.id}: слов ${category.words.length}, прототип ждёт 4`);
      for (const word of category.words) {
        assert.equal(typeof word, 'string',
          'слово должно быть строкой: прототип зовёт w.toUpperCase()');
        assert.ok(word.length > 0);
      }
    }
  }
});

test('мета-пузырь совпадает с именем своей категории без учёта регистра', () => {
  /*
   * Иначе прототип не свяжет их и покажет мета-слово обычным пузырём.
   *
   * Именно без учёта регистра: в базе текст пузыря — словоформа `fish`, а имя
   * категории — `FISH`, и прототип приводит к верхнему регистру и то и другое
   * (`c.name.toUpperCase()`, `w.toUpperCase()`) прежде чем сравнивать.
   * Требовать здесь побайтового равенства значило бы описать не тот контракт,
   * который реально исполняется.
   */
  let checked = 0;
  for (const generated of block.levels) {
    const handoff = pack.levels.find((l) => l.level_id === generated.spec.levelId)!;
    for (const category of generated.spec.categories) {
      for (const word of category.words) {
        if (word.kind !== 'meta') continue;
        checked += 1;
        const child = handoff.categories.find((c) => c.id === word.metaChild);
        assert.ok(child, `нет категории ${word.metaChild} для мета-пузыря`);
        assert.equal(word.text.toUpperCase(), child!.name.toUpperCase(),
          'текст мета-пузыря обязан совпадать с именем дочерней категории');
      }
    }
  }
  assert.ok(checked > 0, 'в пресете нет мета-пузырей — проверка ничего не проверила');
});

test('лимит ходов доезжает до прототипа и не подменяется молча', () => {
  /*
   * Проверка родилась из живой поломки. Формат передачи нёс только вместимость
   * поля и число стартовых пузырей; прототип видел уровень без `move_limit` и
   * включал ∞. Вся сданная линейка игралась без давления ходов — то есть без
   * половины механики (GDD §2 п.9), — и заметили это только руками.
   *
   * Поэтому здесь закреплены три вещи: поле физически есть, оно равно тому, что
   * посчитал генератор, и инвариант схемы `move_limit >= 3*M` соблюдён. `null`
   * разрешён только там, где его поставил сам генератор (туториал): решение
   * «играть без лимита» принимает конфиг прототипа, а не отсутствие данных.
   */
  for (const generated of block.levels) {
    const handoff = pack.levels.find((l) => l.level_id === generated.spec.levelId)!;
    const board = handoff.board;
    assert.ok('move_limit' in board,
      `уровень ${handoff.level_id}: в доске нет move_limit — прототип включит ∞`);
    assert.equal(board.move_limit, generated.spec.board.moveLimit,
      `уровень ${handoff.level_id}: лимит разошёлся с посчитанным генератором`);
    assert.equal(board.move_limit_k, generated.spec.board.moveLimitK);
    if (board.move_limit === null) continue;
    const floor = handoff.categories.length * 3;
    assert.ok(board.move_limit >= floor,
      `уровень ${handoff.level_id}: лимит ${board.move_limit} ниже пола ${floor} — уровень непроходим`);
  }
});

test('без лимита уходит только туториал', () => {
  // Если безлимитных уровней вдруг стало много, значит лимит снова где-то
  // потерялся по дороге, а не был снят осознанно.
  const unlimited = pack.levels.filter((l) => l.board.move_limit === null);
  assert.ok(unlimited.length <= 1,
    `без лимита ${unlimited.length} уровней: ${unlimited.map((l) => l.level_id).join(', ')}`);
  for (const level of unlimited) {
    assert.equal(level.level_id, block.levels[0]!.spec.levelId,
      'без лимита может быть только первый уровень блока (туториал)');
  }
});

test('ключ хранилища совпадает у инструмента и у сайта', () => {
  // Единственная связь между бандлом и обычным HTML сайта — строка ключа.
  for (const file of ['../../site/index.html', '../../site/playable/index.html']) {
    const html = readFileSync(join(ROOT, file), 'utf8');
    assert.ok(html.includes(HANDOFF_KEY),
      `${file} не знает ключа ${HANDOFF_KEY}: пакет туда не доедет`);
  }
});

/**
 * Выложенные пакеты — такой же контракт, как и свежесобранный.
 *
 * Файлы в `site/playable/packs/` попадают в прототип без единой строки кода:
 * сайт склеивает их и кладёт в хранилище, прототип исполняет выкладку как есть.
 * Значит, сломать их может кто угодно и когда угодно, а увидит это только
 * человек, открывший уровень руками. Проверяем то, что прототип молча не
 * переживёт: манифест ссылается на существующие файлы, у каждого уровня есть
 * лимит ходов, и выкладка раздаёт ровно те слова, что заявлены в категориях.
 */
test('выложенные пакеты исправны: манифест, лимит ходов, полнота выкладки', () => {
  const dir = join(ROOT, '../../site/playable/packs');
  const index = JSON.parse(readFileSync(join(dir, 'index.json'), 'utf8')) as
    { packs: string[] };
  assert.ok(index.packs.length > 0, 'манифест пуст: в списке уровней сайта ничего не будет');

  for (const file of index.packs) {
    const pack = JSON.parse(readFileSync(join(dir, file), 'utf8')) as {
      label: string;
      levels: {
        level_id: number;
        categories: { id: string; name: string; words: string[] }[];
        board: { board_capacity: number; start_bubbles: number; move_limit: number | null };
        deal: { start: { word: string; category: string }[];
          queue: { word: string; category: string }[] };
      }[];
    };
    assert.ok(pack.levels.length > 0, `${file}: пакет без уровней`);

    for (const level of pack.levels) {
      const where = `${file} уровень ${level.level_id}`;
      const names = new Set(level.categories.map((c) => c.name.toUpperCase()));
      const ids = new Set(level.categories.map((c) => c.id));

      // мета-пузырь не спавнится: он появляется превращением собранной четвёрки
      const spawnable: string[] = [];
      for (const category of level.categories) {
        assert.equal(category.words.length, 4, `${where}: у ${category.name} не четыре слова`);
        for (const word of category.words) {
          const isMeta = names.has(word.toUpperCase())
            && word.toUpperCase() !== category.name.toUpperCase();
          if (!isMeta) spawnable.push(`${category.id}::${word}`);
        }
      }

      const dealt = [...level.deal.start, ...level.deal.queue]
        .map((b) => `${b.category}::${b.word}`);
      assert.deepEqual(dealt.slice().sort(), spawnable.slice().sort(),
        `${where}: выкладка не совпадает с составом категорий`);
      for (const bubble of [...level.deal.start, ...level.deal.queue]) {
        assert.ok(ids.has(bubble.category),
          `${where}: пузырь ${bubble.word} ссылается на несуществующую категорию`);
      }
      assert.ok(level.deal.start.length <= level.board.board_capacity,
        `${where}: на поле ${level.deal.start.length} пузырей при вместимости `
        + `${level.board.board_capacity}`);
      assert.equal(level.board.start_bubbles, spawnable.length,
        `${where}: заявлено ${level.board.start_bubbles} пузырей, раздаётся ${spawnable.length}`);
      // молчаливая пропажа лимита однажды сделала всю линейку безлимитной
      assert.ok(level.board.move_limit === null || level.board.move_limit > 0,
        `${where}: лимит ходов ${level.board.move_limit}`);
    }
  }
});

/**
 * Проходится ли выложенный уровень вообще.
 *
 * Проверка появилась после уровня 12: он собирался, валидировался и имел
 * единственное решение — и вставал в прототипе на 1/12 с 34 ходами в руках.
 * Ни валидатор, ни решатель этого не видят: оба смотрят на список категорий и
 * ни один не смотрит на ПОЛЕ — сколько пузырей помещается, что приходит на
 * смену собранным, хватает ли ходов. Симулятор смотрит именно туда.
 */
test('каждый выложенный уровень проходится ботом в пределах лимита', async () => {
  const { simulate } = await import('../scripts/simulate_play.ts');
  const dir = join(ROOT, '../../site/playable/packs');
  const index = JSON.parse(readFileSync(join(dir, 'index.json'), 'utf8')) as
    { packs: string[] };

  for (const file of index.packs) {
    const pack = JSON.parse(readFileSync(join(dir, file), 'utf8')) as
      { levels: Parameters<typeof simulate>[0][] };
    for (const level of pack.levels) {
      const r = simulate(level);
      assert.ok(r.won,
        `${file} уровень ${level.level_id}: ${r.categoriesDone}/${r.categoriesTotal} — `
        + `${r.reason} на ходу ${r.movesUsed} из ${r.moveLimit}, `
        + `в очереди осталось ${r.queueLeft}`);
    }
  }
});
