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
  for (const pool of pools) {
    const onField = counts.get(pool.key) ?? 0;
    pool.words.slice(0, onField).forEach((word) => {
      start.push({ word, category: pool.key });
    });
  }

  // поле тасуется: сгруппированные по категориям пузыри выдали бы структуру
  // уровня раньше, чем игрок её разгадает; очередь же строится ПО РИТМУ —
  // внутри пачки порядок и так перемешан выбором добивки
  const queue = paceQueue(categories, pools, counts, cost, rng);
  return { start: rng.shuffle(start), queue };
}

/**
 * Очередь досыпки по ритму референса: каждая пачка открывает следующий сбор.
 *
 * Как устроена досыпка в прототипе: новые пузыри приходят ТОЛЬКО после сбора
 * категории (4 пузыря; 3, если категория осталась на поле мета-словом). Значит
 * порядок очереди — это и есть ритм уровня: если пачка не даёт собрать ничего
 * нового, игрок смотрит на поле из одних недоборов и считает уровень сломанным.
 * Инцидент 02.08, уровень 12 «как в оригинале»: случайная очередь оставила
 * поле в таком состоянии на 15+ ходов, спасала только страховка «досыпка вне
 * ритма».
 *
 * Поэтому очередь строится симуляцией: пачка собирается так, чтобы в ней
 * ПЕРВЫМИ шли слова, закрывающие ближайшую к сбору категорию, а остаток
 * добивался словами других начатых категорий. Сложность уровня этим не
 * выравнивается: она живёт в числе категорий, ловушках, редкости, лимите и
 * модификаторах — ритм же обязан быть живым на любой сложности.
 *
 * Пачка меряется в ПУЗЫРЯХ (распиленное слово стоит два), как и спавн
 * прототипа. Точное попадание в границы пачек невозможно при распилах —
 * половинка может «переползти» в следующую волну; это допустимо, финальную
 * правду о ритме говорит симулятор проходимости.
 */
function paceQueue(
  categories: readonly LevelCategory[],
  pools: { key: string; words: string[] }[],
  counts: Map<string, number>,
  cost: (categoryKey: string, word: string) => number,
  rng: ReturnType<typeof createRng>,
): DealBubble[] {
  const needed = new Map(categories.map((c) => [c.key, c.words.length]));
  const parentOf = new Map(categories
    .filter((c) => c.parentKey !== null)
    .map((c) => [c.key, c.parentKey as string]));
  /** слов категории на поле: спавнившихся или пришедших мета-превращением */
  const fieldCount = new Map<string, number>();
  for (const [key, n] of counts) fieldCount.set(key, n);
  const pending = new Map<string, string[]>(pools.map((p) =>
    [p.key, p.words.slice(counts.get(p.key) ?? 0)]));

  const out: DealBubble[] = [];
  const push = (key: string, word: string): void => {
    out.push({ word, category: key });
    fieldCount.set(key, (fieldCount.get(key) ?? 0) + 1);
  };
  const pendingAlive = (): boolean =>
    [...pending.values()].some((w) => w.length > 0);
  const collectible = (): string | null => {
    for (const c of categories) {
      if ((fieldCount.get(c.key) ?? 0) >= (needed.get(c.key) ?? 4)) return c.key;
    }
    return null;
  };

  let guard = categories.length * 8;
  while (guard > 0) {
    guard -= 1;
    const key = collectible();
    if (!key) break;
    // сбор: слова категории уходят с поля; мета-ребёнок дарит родителю слово
    fieldCount.set(key, 0);
    const parent = parentOf.get(key);
    if (parent !== undefined) fieldCount.set(parent, (fieldCount.get(parent) ?? 0) + 1);
    if (!pendingAlive()) continue;   // хвост уровня добирается мерджами без досыпки

    let cap = parent !== undefined ? 3 : 4;

    // цель пачки: категория, которую дешевле всего довести до сбора
    let target: { key: string; words: string[]; costTotal: number } | null = null;
    for (const c of categories) {
      const rest = pending.get(c.key) ?? [];
      const missing = (needed.get(c.key) ?? 4) - (fieldCount.get(c.key) ?? 0);
      if (missing <= 0 || rest.length < missing) continue;   // не соберётся этой пачкой
      const words = rest.slice(0, missing);
      const costTotal = words.reduce((n, w) => n + cost(c.key, w), 0);
      if (costTotal > cap) continue;
      if (!target || costTotal < target.costTotal) target = { key: c.key, words, costTotal };
    }
    if (target) {
      const rest = pending.get(target.key) ?? [];
      pending.set(target.key, rest.slice(target.words.length));
      for (const w of target.words) push(target.key, w);
      cap -= target.costTotal;
    }

    // добивка: слова других начатых категорий, чтобы на поле было чем ходить;
    // нетронутые категории идут в хвосте — они открывают новую линию, когда
    // у начатых слова кончились
    const shuffledKeys = rng.shuffle(pools.map((p) => p.key));
    const fillers = [
      ...shuffledKeys.filter((k) => (fieldCount.get(k) ?? 0) > 0),
      ...shuffledKeys.filter((k) => (fieldCount.get(k) ?? 0) === 0),
    ];
    let progress = true;
    while (cap > 0 && progress) {
      progress = false;
      for (const fk of fillers) {
        if (cap <= 0) break;
        const rest = pending.get(fk) ?? [];
        if (rest.length === 0) continue;
        // добивка не имеет права ДОСРОЧНО закрыть категорию: сбор — работа цели
        const missing = (needed.get(fk) ?? 4) - (fieldCount.get(fk) ?? 0);
        if (missing <= 1) continue;
        const w = rest[0];
        const c = cost(fk, w);
        if (c > cap) continue;
        pending.set(fk, rest.slice(1));
        push(fk, w);
        cap -= c;
        progress = true;
      }
    }
  }

  // не разложилось по ритму (нет цели дешевле пачки, кончились сборы) — хвост
  // идёт группами по категориям: каждая волна тогда хотя бы завершает одну
  const leftovers = [...pending.entries()].filter(([, w]) => w.length > 0)
    .sort((a, b) => (fieldCount.get(b[0]) ?? 0) - (fieldCount.get(a[0]) ?? 0));
  for (const [key, words] of leftovers) {
    for (const w of words) push(key, w);
  }
  return out;
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

  // бюджет поля меряется в ПУЗЫРЯХ: распиленное слово (spec.halves) занимает два
  const chunked = new Set(spec.halves.map((h) => chunkKey(h.home, h.word)));
  const bubbleCost = (bubbles: readonly DealBubble[]): number =>
    bubbles.reduce((n, b) => n + (chunked.has(chunkKey(b.category, b.word)) ? 2 : 1), 0);

  const startCost = bubbleCost(deal.start);
  if (startCost > spec.board.boardCapacity) {
    problems.push(`на поле ${startCost} пузырей при вместимости `
      + `${spec.board.boardCapacity}`);
  }
  const totalBubbles = bubbleCost([...deal.start, ...deal.queue]);
  const fieldSize = Math.min(spec.board.boardCapacity, totalBubbles);
  // поле имеет право не добрать один пузырь: когда остаток бюджета — одно
  // место, а класть осталось только распиленные слова по два места каждое
  if (startCost !== fieldSize && startCost !== fieldSize - 1) {
    problems.push(`на поле ${startCost} пузырей, ожидалось ${fieldSize}`);
  }

  return problems;
}
