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

/** Слова категории, которые реально спавнятся: мета-слово на поле не кладётся. */
function spawnableWords(category: LevelCategory): string[] {
  return category.words.filter((w) => w.kind !== 'meta').map((w) => w.text);
}

export function buildDeal(
  levelId: number, categories: readonly LevelCategory[], board: DealBoard,
): Deal {
  const rng = createRng(`deal::${levelId}::${categories.map((c) => c.key).join(',')}`);

  const pools = categories.map((category) => ({
    key: category.key,
    isQuickwin: category.isQuickwin,
    // порядок внутри категории тасуется: иначе на поле всегда оказывались бы
    // первые слова спека, а в очередь уходили последние — а спек упорядочен
    // по очевидности слова, и игрок получал бы самые явные слова бесплатно
    words: rng.shuffle(spawnableWords(category)),
  }));

  const total = pools.reduce((n, p) => n + p.words.length, 0);
  const fieldSize = Math.min(board.boardCapacity, total);

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
  let left = fieldSize;
  if (opener && left >= board.wordsPerCategory) {
    counts.set(opener.key, board.wordsPerCategory);
    left -= board.wordsPerCategory;
  }

  // остаток раздаётся по кругу почти поровну: так на поле видно понемногу от
  // многих категорий, и игрок ищет связь, а не собирает готовое
  const rest = rng.shuffle(pools.filter((p) => p !== opener));
  for (let i = 0; left > 0 && rest.length > 0; i += 1) {
    const pool = rest[i % rest.length];
    const cap = Math.min(board.wordsPerCategory, pool.words.length);
    if ((counts.get(pool.key) ?? 0) < cap) {
      counts.set(pool.key, (counts.get(pool.key) ?? 0) + 1);
      left -= 1;
    } else if (rest.every((p) => (counts.get(p.key) ?? 0) >= Math.min(
      board.wordsPerCategory, p.words.length))) {
      // все категории добраны до потолка, а место ещё есть: раздавать нечего
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
