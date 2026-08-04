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
import {
  HANDOFF_KEY, HANDOFF_LIST_KEY, HANDOFF_MAX_PACKS, HANDOFF_MESSAGE,
  buildHandoffPack, publishToPlayable, readHandoffPacks,
} from '../web/src/core/playableHandoff.ts';
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
   * половины механики (GDD §2 п.10), — и заметили это только руками.
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
  // Архив читает только страница отчёта: прототипу он не нужен, тот играет
  // рабочий слот. Требовать ключ архива от прототипа значило бы описать не тот
  // контракт, который исполняется.
  const report = readFileSync(join(ROOT, '../../site/index.html'), 'utf8');
  assert.ok(report.includes(HANDOFF_LIST_KEY),
    `site/index.html не знает ключа ${HANDOFF_LIST_KEY}: собранные пакеты не переживут перезагрузку`);
  // Тем же способом связан сигнал «пакет отдан»: инструмент шлёт его страница
  // отчёта слушает. Разъедутся строки — прототип молча перестанет обновляться
  // сам, и это заметят не раньше, чем руками свернут пункт и развернут обратно.
  assert.ok(report.includes(HANDOFF_MESSAGE),
    `site/index.html не слушает сообщение ${HANDOFF_MESSAGE}: `
    + 'прототип не обновится после «Добавить в Playable»');
});

/*
 * Досыпка прототипа — фиксированные числа.
 *
 * Со 02.08 по 03.08 прототип вместо пачки «добирал поле до нормы», и досыпка
 * платила по всем накопленным долгам разом: игрок собирал категорию и получал
 * 5, 8, 12 шаров вместо четырёх. Гейт здесь грубый — чтение HTML на подстроки, —
 * но именно он ловит возврат к добору: правила партии в TS (`playSim.ts`) и
 * правила прототипа обязаны совпадать, а сравнить их автоматически нечем.
 */
test('прототип досыпает фиксированными пачками, а не добирает поле до нормы', () => {
  const html = readFileSync(join(ROOT, '../../site/playable/index.html'), 'utf8');
  assert.ok(!/topUpField/.test(html),
    'в прототипе снова есть добор поля до нормы (topUpField)');
  for (const call of ['spawnBatch(4)', 'spawnBatch(3)', 'spawnBatch(1)']) {
    assert.ok(html.includes(call),
      `прототип не досыпает пачкой ${call}: `
      + 'сбор категории — 4, мета-превращение — 3, склейка половинок — 1');
  }
});

/*
 * Своего контента у прототипа нет.
 *
 * Зашитые двенадцать категорий (SEASONS, SPACE, FOOD…) убраны 03.08: любой сбой
 * загрузки молча подменял ими настоящий уровень, экран выглядел рабочим, и
 * проверяющий играл не в то, что проверял. Так уже терялась живая ошибка — пакет
 * без `board` роняло обращение к `L.board.move_limit`, ошибку гасил общий catch,
 * и вместо уровня показывалось демо.
 *
 * Проверка грубая, чтением исходника, но другой тут нет: контент был в HTML,
 * который tsc не видит, а падение молчаливое — тестом на поведение его не
 * поймать, потому что «поведение» как раз выглядело нормальным.
 */
test('в прототипе нет своего контента: уровень приходит только извне', () => {
  const html = readFileSync(join(ROOT, '../../site/playable/index.html'), 'utf8');
  assert.ok(!/DEFAULT_TARGETS/.test(html),
    'в прототипе снова появился зашитый контент (DEFAULT_TARGETS)');
  // выборочно по словам прежнего демо: имя константы могли и переименовать
  for (const word of ['HAMSTER', 'CAULDRON', 'SPRING']) {
    assert.ok(!html.includes(`'${word}'`),
      `в прототипе снова зашиты слова демо-контента (${word})`);
  }
  assert.ok(/function noLevel\(/.test(html),
    'нет noLevel: прототип без уровня должен говорить это вслух, а не показывать '
    + 'что-нибудь другое');
  // и на сайте не должно остаться пункта, который вёл на демо
  const report = readFileSync(join(ROOT, '../../site/index.html'), 'utf8');
  assert.ok(!/<option value="">\s*Демо/.test(report),
    'в списке уровней отчёта остался пункт «Демо»: он ведёт на пустой прототип');
});

/*
 * Половинки: у каждой ровно один законный партнёр.
 *
 * Живая поломка 03.08, уровень 12 из реф-источника: игрок доигрывал до конца и
 * оставался с шарами, которые не с чем слить. Причина — нумерация пар. Номера
 * выдавал `expandChunks`, считая от единицы в КАЖДОМ своём вызове, а вызывают его
 * дважды: на стартовое поле и на очередь. `dol|phin` со старта и `choco|late` из
 * очереди получали один номер пары, склейка проверяла только номер и сторону, и
 * `dol` склеивался с `late`: пузырь получал категорию первого и слово второго,
 * `dolphin` из уровня исчезал, `phin` и `choco` оставались сиротами. На 8 распилах
 * уровня 12 неоднозначный партнёр был у 12 половинок из 16.
 *
 * Ни один бот этого не видел и увидеть не мог: `core/playSim.ts` нумерует пары
 * индексом в `spec.halves`, то есть глобально, и у него коллизии не бывает
 * по построению. Поломка жила ровно в прототипе — значит и проверять её надо
 * на прототипе, читая его собственный код.
 *
 * Уровень для проверки — свой, прямо здесь. Раньше проверка брала половинки из
 * выложенных пакетов, и это было её слабым местом: единственный пакет с
 * распилами был один-единственный, а с очисткой выкладки 04.08 проверять стало
 * нечего вовсе. Своему уровню это безразлично — и он вдобавок бьёт точно в
 * поломку: распилы стоят И на старте, И в очереди, то есть ровно в тех двух
 * вызовах `expandChunks`, чьи номера когда-то столкнулись.
 */
const HALVES_FIXTURE = {
  level_id: 1,
  categories: [
    { id: 'ocean', name: 'OCEAN ANIMALS', words: ['dolphin', 'whale', 'shark', 'crab'] },
    { id: 'sweets', name: 'SWEETS', words: ['chocolate', 'candy', 'waffle', 'donut'] },
  ],
  board: { board_capacity: 24, start_bubbles: 8, move_limit: 20 },
  chunks: [
    { word: 'dolphin', category: 'ocean', pieces: ['dol', 'phin'] },
    { word: 'chocolate', category: 'sweets', pieces: ['choco', 'late'] },
  ],
  deal: {
    // распил на старте: `dol` + `phin`
    start: [
      { word: 'dolphin', category: 'ocean' },
      { word: 'whale', category: 'ocean' },
      { word: 'candy', category: 'sweets' },
    ],
    // распил в очереди: `choco` + `late` — второй вызов expandChunks
    queue: [
      { word: 'chocolate', category: 'sweets' },
      { word: 'shark', category: 'ocean' },
      { word: 'crab', category: 'ocean' },
      { word: 'waffle', category: 'sweets' },
      { word: 'donut', category: 'sweets' },
    ],
  },
};

test('половинки прототипа: у каждой ровно один законный партнёр', () => {
  const html = readFileSync(join(ROOT, '../../site/playable/index.html'), 'utf8');
  /** Вырезает объявление функции по имени — вместе с телом, по балансу скобок. */
  const grab = (name: string): string => {
    const start = html.indexOf(`function ${name}(`);
    assert.ok(start >= 0, `в прототипе нет функции ${name}`);
    let depth = 0;
    let end = html.indexOf('{', start);
    for (let k = end; k < html.length; k += 1) {
      if (html[k] === '{') depth += 1;
      else if (html[k] === '}') { depth -= 1; if (depth === 0) { end = k; break; } }
    }
    return html.slice(start, end + 1);
  };
  // функции чистые (DOM не трогают), поэтому их можно выполнить здесь
  const made = new Function(`${grab('applyChunks')}\n${grab('expandChunks')}\n`
    + `${grab('samePair')}\nreturn { applyChunks, expandChunks, samePair };`)() as {
    applyChunks: (l: unknown) => unknown;
    expandChunks: (l: unknown, m: unknown) => { list: { v: string; e: string;
      half: { pair: number; side: number; whole: string } | null }[] };
    samePair: (a: unknown, b: unknown) => boolean;
  };

  /* Свой уровень — всегда; выложенные с распилами — если они есть.
     Выкладка меняется от прогона к прогону, поэтому опираться на неё проверка
     не может, а пройтись по ней, когда она на месте, стоит: файлы попадают в
     прототип без единой строки кода, и сломать их может кто угодно. */
  const dir = join(ROOT, '../../site/playable/packs');
  const index = JSON.parse(readFileSync(join(dir, 'index.json'), 'utf8')) as
    { packs: string[] };
  type ChunkedLevel = { level_id: number; categories: { id: string; name: string }[];
    chunks?: unknown[];
    deal: { start: { word: string; category: string }[];
      queue: { word: string; category: string }[] } };
  const cases: { file: string; levels: ChunkedLevel[] }[] = [
    { file: 'фикстура теста', levels: [HALVES_FIXTURE as ChunkedLevel] },
  ];
  for (const file of index.packs) {
    const packJson = JSON.parse(readFileSync(join(dir, file), 'utf8')) as
      { levels: ChunkedLevel[] };
    cases.push({ file, levels: packJson.levels });
  }

  let checkedLevels = 0;
  for (const { file, levels } of cases) {
    for (const level of levels) {
      if (!level.chunks || level.chunks.length === 0) continue;
      checkedLevels += 1;
      const chunkMap = made.applyChunks(level);
      const nameOf = new Map(level.categories.map((c) => [c.id, c.name.toUpperCase()]));
      const up = (list: { word: string; category: string }[]) => list.map((b) => ({
        v: nameOf.get(b.category) ?? '', e: b.word.toUpperCase(),
      }));
      const halves = [
        ...made.expandChunks(up(level.deal.start), chunkMap).list,
        ...made.expandChunks(up(level.deal.queue), chunkMap).list,
      ].filter((b) => b.half).map((b) => ({ val: b.v, exs: [b.e], half: b.half }));

      for (const a of halves) {
        const mates = halves.filter((b) => b !== a && made.samePair(a, b));
        assert.equal(mates.length, 1,
          `${file} ур.${level.level_id}: у половинки ${a.exs[0]} <${a.half!.whole}> `
          + `[${a.val}] партнёров ${mates.length}, а должен быть ровно один`
          + (mates.length > 1 ? `: ${mates.map((m) => m.exs[0]).join(', ')}` : ''));
      }

      /*
       * Отдельно — сама нумерация. Она проверяется не потому, что без неё
       * склейка сломается (четыре признака `samePair` держат и при совпавших
       * номерах), а потому что это ВТОРОЙ рубеж: номер пары уникален на уровень,
       * и каждый встречается ровно дважды. Без этой проверки регресс нумерации
       * прошёл бы молча и ждал бы дня, когда кто-нибудь упростит `samePair`
       * обратно до одного номера.
       */
      const perId = new Map<number, string[]>();
      for (const a of halves) {
        const list = perId.get(a.half!.pair) ?? [];
        list.push(`${a.exs[0]} <${a.half!.whole}> [${a.val}]`);
        perId.set(a.half!.pair, list);
      }
      for (const [pair, list] of perId) {
        assert.equal(list.length, 2,
          `${file} ур.${level.level_id}: номер пары ${pair} носят ${list.length} `
          + `половинки вместо двух: ${list.join(' | ')}`);
      }
    }
  }
  assert.ok(checkedLevels > 0,
    'ни одного уровня с распилами — даже своего: фикстура потеряла chunks, '
    + 'и проверка ничего не проверила');

  /*
   * Вторая половина той же поломки, и она была главной. Досыпка звала
   * `makeBubble(it.v,it.e,x,y)` — без пятого аргумента, то есть без метки
   * половинки. Стартовое поле метку передавало, а очередь нет: кусочек `SAR`
   * приезжал ОБЫЧНЫМ пузырём и становился полноправным «словом» категории
   * HUMOR. Счётчик слов считал его наравне с целыми, склеить его было не с чем,
   * и уровень доигрывался до «остались шары, которые не с чем слить». На
   * уровне 12 так терялись все пять распилов, приходящих досыпкой.
   *
   * Проверка грубая — чтение исходника, — но другой здесь нет: оба бота
   * разворачивают распилы сами и этой ветки прототипа не исполняют вовсе.
   * Именно поэтому симулятор говорил PASS, пока живой уровень вставал.
   */
  // комментарии вырезаем: они тоже упоминают `it.half`, и проверка ловила бы
  // собственное объяснение вместо кода
  const spawnFn = grab('trySpawn')
    .replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/[^\n]*/g, '');
  const call = spawnFn.match(/makeBubble\(.*\);/);
  assert.ok(call, 'досыпка вообще не зовёт makeBubble — пузыри не появятся');
  assert.ok(call[0].includes('half'),
    'досыпка зовёт makeBubble без метки половинки: кусочек приедет обычным '
    + `пузырём и станет «словом» категории, а его пара останется сиротой — ${call[0]}`);
});

/**
 * Накопление пакетов.
 *
 * История простая: ключ был один, и в него писали двое — инструмент клал туда
 * собранный пакет, страница отчёта клала туда же склейку выложенных. Собранный
 * пакет исчезал на первой перезагрузке, а второй прогон генератора затирал
 * первый. Сравнить «до» и «после» правки было нечем, хотя у каждого пакета есть
 * собственный хеш и различать их было чем.
 */
function withFakeStorage<T>(body: () => T): T {
  const data = new Map<string, string>();
  const previous = (globalThis as { window?: unknown }).window;
  (globalThis as { window?: unknown }).window = {
    localStorage: {
      getItem: (k: string) => (data.has(k) ? data.get(k)! : null),
      setItem: (k: string, v: string) => { data.set(k, v); },
    },
  };
  try {
    return body();
  } finally {
    (globalThis as { window?: unknown }).window = previous;
  }
}

test('вторая сборка не затирает первую: пакеты копятся, свежий сверху', () => {
  withFakeStorage(() => {
    assert.deepEqual(readHandoffPacks(), [], 'архив должен стартовать пустым');

    publishToPlayable(block);
    assert.equal(readHandoffPacks().length, 1);

    // другой пакет = другой хеш; подделываем его, не пересобирая блок заново
    const other = { ...block, packHash: block.packHash.split('').reverse().join('') };
    publishToPlayable(other);

    const list = readHandoffPacks();
    assert.equal(list.length, 2, 'вторая сборка затёрла первую');
    assert.equal(list[0]!.pack_hash, other.packHash, 'свежий пакет обязан быть первым');
    assert.equal(list[1]!.pack_hash, block.packHash, 'первый пакет обязан уцелеть');
  });
});

test('пересборка того же конфига не плодит дублей, а поднимается наверх', () => {
  withFakeStorage(() => {
    const other = { ...block, packHash: block.packHash.split('').reverse().join('') };
    publishToPlayable(block);
    publishToPlayable(other);
    publishToPlayable(block);         // тот же конфиг, тот же хеш

    const list = readHandoffPacks();
    assert.equal(list.length, 2, 'одинаковый хеш обязан склеиться в одну запись');
    assert.equal(list[0]!.pack_hash, block.packHash);
  });
});

test('архив не растёт бесконечно: держим последние HANDOFF_MAX_PACKS', () => {
  withFakeStorage(() => {
    const hashes: string[] = [];
    for (let i = 0; i < HANDOFF_MAX_PACKS + 3; i += 1) {
      const hash = `${block.packHash}-${i}`;
      hashes.push(hash);
      publishToPlayable({ ...block, packHash: hash });
    }
    const list = readHandoffPacks();
    assert.equal(list.length, HANDOFF_MAX_PACKS);
    assert.deepEqual(list.map((p) => p.pack_hash), hashes.slice().reverse().slice(0, HANDOFF_MAX_PACKS),
      'вытесняться должен самый старый, а не самый новый');
  });
});

test('рабочий слот получает именно последнюю сборку', () => {
  // Прототип, открытый сразу после кнопки, обязан играть только что собранное.
  withFakeStorage(() => {
    const other = { ...block, packHash: block.packHash.split('').reverse().join('') };
    publishToPlayable(block);
    publishToPlayable(other);
    const slot = JSON.parse(window.localStorage.getItem(HANDOFF_KEY)!) as { pack_hash: string };
    assert.equal(slot.pack_hash, other.packHash);
  });
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
 *
 * Сколько пакетов в манифесте — не дело теста. Здесь стояла проверка «хотя бы
 * один», и она не ловила ничего: пустая выкладка — обычное состояние между
 * прогонами, а не поломка. Проверяем содержимое того, что выложено, и молчим
 * про количество.
 */
test('выложенные пакеты исправны: манифест, лимит ходов, полнота выкладки', () => {
  const dir = join(ROOT, '../../site/playable/packs');
  const index = JSON.parse(readFileSync(join(dir, 'index.json'), 'utf8')) as
    { packs: string[] };

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
 *
 * До финального прогона выкладка пуста, и проверять здесь нечего — проверка
 * зелёная просто потому, что не нашла работы. Это её нормальное состояние
 * между прогонами, а не признак того, что уровни в порядке: гейт по проходимости
 * стоит и в самом генераторе (`simulatePlayability`), выкладка проходит его до
 * того, как попадёт сюда.
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
