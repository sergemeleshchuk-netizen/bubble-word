/**
 * Первая выкладка: какие слова лежат на поле в момент старта и в каком порядке
 * приходит досыпка.
 *
 * Почему это часть уровня, а не дело клиента. Раньше выкладку каждый прототип
 * считал сам, и по-разному. Играбельный HTML тасовал слова через `Math.random`
 * при каждом заходе: один и тот же уровень у двух проверяющих выглядел
 * по-разному, и даже перезапуск давал новое поле. Встроенный в инструмент
 * прототип брал первые `board_capacity` слов в порядке спека — то есть шесть
 * категорий целиком, готовыми четвёрками. Наигровка руками в таких условиях
 * ничего не доказывает: неясно, уровень тяжёлый или выкладка не повезла, и
 * замечание «уровень 17 душный» невозможно ни воспроизвести, ни проверить.
 *
 * Поэтому выкладка считается один раз — здесь — и уезжает в спек, в игровой
 * JSON и в пакет для прототипа. Клиент её исполняет, а не изобретает.
 *
 * Что сюда НЕ входит: координаты пузырей на поле. Это следующий шаг; пока
 * клиент раскладывает выданный состав по своей сетке сам. Здесь — СОСТАВ (какие
 * слова видно на старте) и ПОРЯДОК (какие приходят следом).
 *
 * Детерминированность своя, а не унаследованная от генератора. Seed собирается
 * из номера уровня и ключей категорий, поэтому выкладку можно пересчитать из
 * одного только спека — в том числе для уровня, собранного другим прогоном.
 * Зависеть от потока `rng` генератора нельзя: тогда добавленная где-то выше
 * лишняя выборка молча меняла бы выкладку всех уровней.
 */
import { createRng } from './rng.ts';
import type { Deal, DealBubble, LevelCategory, LevelSpec } from './types.ts';

export interface DealBoard {
  boardCapacity: number;
  wordsPerCategory: number;
}

/**
 * Слова, распиленные на кусочки: такое слово занимает на поле ДВА пузыря.
 *
 * Появилось при воспроизведении записи уровня 12 оригинала: там восемь слов
 * приходят кусочками, а пузырей на старте по-прежнему 24. Если считать бюджет
 * поля в словах, восемь распилов дадут 32 пузыря вместо 24 — то есть не тот
 * уровень, который записан. Ключ — `категория::слово` в нижнем регистре:
 * одно и то же слово в двух категориях распилено не обязательно в обеих.
 *
 * Пустой набор (умолчание) ничего не меняет: выкладка уровней без кусочков
 * считается ровно так же, как считалась, и хеши остаются прежними.
 */
export type ChunkedWords = ReadonlySet<string>;

export function chunkKey(categoryKey: string, word: string): string {
  return `${categoryKey}::${word.toLowerCase()}`;
}

/** Слова категории, которые реально спавнятся: мета-слово на поле не кладётся. */
function spawnableWords(category: LevelCategory): string[] {
  return category.words.filter((w) => w.kind !== 'meta').map((w) => w.text);
}

export function buildDeal(
  levelId: number, categories: readonly LevelCategory[], board: DealBoard,
  chunked: ChunkedWords = new Set<string>(),
): Deal {
  const rng = createRng(`deal::${levelId}::${categories.map((c) => c.key).join(',')}`);
  /** Сколько мест на поле занимает слово: распиленное — два. */
  const cost = (categoryKey: string, word: string): number =>
    (chunked.has(chunkKey(categoryKey, word)) ? 2 : 1);

  const pools = categories.map((category) => ({
    key: category.key,
    isQuickwin: category.isQuickwin,
    // порядок внутри категории тасуется: иначе на поле всегда оказывались бы
    // первые слова спека, а в очередь уходили последние — а спек упорядочен
    // по очевидности слова, и игрок получал бы самые явные слова бесплатно
    words: rng.shuffle(spawnableWords(category)),
  }));

  // бюджет поля считается в ПУЗЫРЯХ, а не в словах: распиленное слово стоит два
  const totalBubbles = pools.reduce(
    (n, p) => n + p.words.reduce((k, w) => k + cost(p.key, w), 0), 0);
  const fieldSize = Math.min(board.boardCapacity, totalBubbles);

  /*
   * Одна категория выкладывается целиком.
   *
   * Правило из референса и из прототипа: на старте обязана быть хотя бы одна
   * категория, которую видно всю и можно собрать не дожидаясь досыпки. Без неё
   * первый ход упирается в перебор обрывков, и уровень начинается с паузы.
   *
   * Из подходящих берём quickwin — категорию из частотных слов без мета-связей.
   * Раньше прототип брал первую попавшуюся в порядке спека; предъявить игроку
   * самую простую четвёрку честнее: она объясняет правило игры, а не проверяет
   * его знание.
   */
  const whole = pools.filter((p) => p.words.length >= board.wordsPerCategory);
  const opener = whole.find((p) => p.isQuickwin) ?? whole[0] ?? null;

  const counts = new Map<string, number>(pools.map((p) => [p.key, 0]));
  /** Во сколько пузырей обойдутся первые `n` слов категории (порядок уже перемешан). */
  const bubblesFor = (pool: { key: string; words: string[] }, n: number): number =>
    pool.words.slice(0, n).reduce((k, w) => k + cost(pool.key, w), 0);

  let left = fieldSize;
  if (opener && left >= bubblesFor(opener, board.wordsPerCategory)) {
    counts.set(opener.key, board.wordsPerCategory);
    left -= bubblesFor(opener, board.wordsPerCategory);
  }

  // остаток раздаётся по кругу почти поровну: так на поле видно понемногу от
  // многих категорий, и игрок ищет связь, а не собирает готовое
  const rest = rng.shuffle(pools.filter((p) => p !== opener));
  for (let i = 0; left > 0 && rest.length > 0; i += 1) {
    const pool = rest[i % rest.length];
    const cap = Math.min(board.wordsPerCategory, pool.words.length);
    const have = counts.get(pool.key) ?? 0;
    // следующее слово этой категории может стоить два пузыря — тогда оно
    // берётся только если оба места свободны, иначе поле переполнится
    const next = have < cap ? cost(pool.key, pool.words[have]) : 0;
    if (have < cap && next <= left) {
      counts.set(pool.key, have + 1);
      left -= next;
    } else if (rest.every((p) => {
      const done = (counts.get(p.key) ?? 0) >= Math.min(
        board.wordsPerCategory, p.words.length);
      const tooBig = !done && cost(p.key, p.words[counts.get(p.key) ?? 0]) > left;
      return done || tooBig;
    })) {
      // добрать больше нечего: либо всё роздано, либо остаток поля меньше
      // самого дешёвого следующего пузыря
      break;
    }
  }

  const start: DealBubble[] = [];
  const queue: DealBubble[] = [];
  for (const pool of pools) {
    const onField = counts.get(pool.key) ?? 0;
    pool.words.forEach((word, i) => {
      (i < onField ? start : queue).push({ word, category: pool.key });
    });
  }

  // и поле, и очередь тасуются: сгруппированные по категориям пузыри выдали бы
  // структуру уровня раньше, чем игрок её разгадает
  return { start: rng.shuffle(start), queue: rng.shuffle(queue) };
}

/** Пересчёт выкладки из готового спека — для проверок и для старых пакетов. */
export function dealForSpec(spec: LevelSpec): Deal {
  return buildDeal(spec.levelId, spec.categories, spec.board);
}

/**
 * Проверка выкладки на полноту.
 *
 * Смысл строгий: выкладка обязана раздать каждое спавнящееся слово уровня ровно
 * один раз. Потерянное слово делает категорию несобираемой, лишнее — ломает
 * арифметику досыпки (сколько ушло, столько приходит). Мета-слова в выкладке не
 * участвуют вовсе: они появляются превращением собранной четвёрки.
 *
 * Возвращает список претензий; пустой список — выкладка исправна.
 */
export function checkDeal(spec: LevelSpec, deal: Deal | undefined | null): string[] {
  const problems: string[] = [];
  if (!deal || !Array.isArray(deal.start) || !Array.isArray(deal.queue)) {
    return ['выкладки нет'];
  }

  const expected = new Map<string, number>();
  for (const category of spec.categories) {
    for (const word of spawnableWords(category)) {
      const id = `${category.key}::${word}`;
      expected.set(id, (expected.get(id) ?? 0) + 1);
    }
  }

  const got = new Map<string, number>();
  for (const bubble of [...deal.start, ...deal.queue]) {
    const id = `${bubble.category}::${bubble.word}`;
    got.set(id, (got.get(id) ?? 0) + 1);
  }

  for (const [id, count] of expected) {
    const have = got.get(id) ?? 0;
    if (have !== count) problems.push(`${id}: в выкладке ${have}, в уровне ${count}`);
  }
  for (const id of got.keys()) {
    if (!expected.has(id)) problems.push(`${id}: в выкладке есть, в уровне нет`);
  }

  if (deal.start.length > spec.board.boardCapacity) {
    problems.push(`на поле ${deal.start.length} пузырей при вместимости `
      + `${spec.board.boardCapacity}`);
  }
  const totalSpawnable = [...expected.values()].reduce((n, c) => n + c, 0);
  const fieldSize = Math.min(spec.board.boardCapacity, totalSpawnable);
  if (deal.start.length !== fieldSize) {
    problems.push(`на поле ${deal.start.length} пузырей, ожидалось ${fieldSize}`);
  }

  return problems;
}
