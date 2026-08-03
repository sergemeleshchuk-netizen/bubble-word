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

/**
 * Целые слова вперёд, распиленные — в хвост.
 *
 * Схема старта считается в СЛОВАХ: «4» означает четыре слова категории на поле.
 * Распиленное слово стоит два пузыря, поэтому, попав на старт, оно съедало место
 * соседней доли — и схема, написанная дизайнером, исполнялась не полностью.
 * Порядок внутри каждой группы остаётся тем, что дал `rng.shuffle`, поэтому
 * выкладка по-прежнему воспроизводится из спека, а у уровня без распилов не
 * меняется вовсе: там все слова стоят по одному пузырю, и партиция ничего
 * не перемешивает.
 *
 * Следствие продуктовое, и оно совпадает с записью оригинала: половинки
 * приходят ДОСЫПКОЙ, а не лежат на старте, пока стартовое поле не отдано
 * целым словам.
 */
function wholeWordsFirst(
  words: readonly string[], categoryKey: string, chunked: ChunkedWords,
): string[] {
  const whole = words.filter((w) => !chunked.has(chunkKey(categoryKey, w)));
  const split = words.filter((w) => chunked.has(chunkKey(categoryKey, w)));
  return [...whole, ...split];
}

/**
 * Целевая глубина категории на старте: сколько слов она получает, пока бюджет
 * поля не кончился. Тройка — потому что до сбора ей не хватает ОДНОГО слова:
 * такая категория и гипотезу подсказывает, и закрывается первой же пачкой
 * досыпки в 4 пузыря.
 */
const START_DEPTH = 3;

/**
 * Автоматическая схема старта: одиночек нет, двоек мало, троек и четвёрок много.
 *
 * Требование владельца продукта 03.08 после наигровки: уровень на 12 категорий
 * при ровной раздаче встречал игрока полем [4,2,2,2,2,2,2,2,2,2,1,1] — одна
 * собираемая категория, девять пар, из которых ни одна не собирается, и две
 * мёртвые одиночки. Собрать после первой четвёрки было нечего, и досыпку
 * приходилось раздувать до «добери поле до нормы», чтобы уровень вообще
 * доигрывался. Лечить надо было не досыпку, а старт.
 *
 * Поэтому бюджет поля тратится В ГЛУБИНУ, а не в ширину: вход получает полную
 * четвёрку, дальше категории берут по тройке, пока места хватает, и только
 * остаток (если он не меньше `minStartWords`) открывает ещё одну категорию
 * парой. Одиночка не появляется никогда: пузырь, которому не с чем сливаться,
 * забирает внимание и не даёт хода. Категории, не попавшие в схему, целиком
 * ждут в очереди — их линия открывается досыпкой.
 *
 * Арифметика поля на 24 пузыря: [4,3,3,3,3,3,3,2] при любом числе категорий от
 * восьми. Категорий на старте видно меньше, зато шесть из них — в одном слове
 * от сбора, и пачка в 4 пузыря закрывает сразу две.
 */
export function autoScheme(
  fieldBubbles: number, categories: number,
  wordsPerCategory = 4, minStartWords = 2,
): number[] {
  const floor = Math.max(2, minStartWords);
  const out: number[] = [];
  let left = fieldBubbles;

  // вход: категория, которую видно всю и можно собрать не дожидаясь досыпки
  if (categories > 0 && left >= floor) {
    const opener = Math.min(wordsPerCategory, left);
    out.push(opener);
    left -= opener;
  }
  // остальные — по тройке, пока бюджет позволяет
  while (out.length < categories && left >= START_DEPTH) {
    const n = Math.min(START_DEPTH, wordsPerCategory);
    out.push(n);
    left -= n;
  }
  // остаток открывает ещё одну категорию, но только если это не одиночка
  if (out.length < categories && left >= floor) {
    const n = Math.min(left, START_DEPTH, wordsPerCategory);
    out.push(n);
    left -= n;
  }
  // недобор (1-2 пузыря, категории кончились) доливается в уже открытые: место
  // на поле не должно простаивать, а лишний пузырь у тройки делает её четвёркой
  for (let i = 0; left > 0 && i < out.length * wordsPerCategory; i += 1) {
    const k = i % out.length;
    if (out[k] < wordsPerCategory) { out[k] += 1; left -= 1; }
  }

  return out.sort((a, b) => b - a);
}

/**
 * Потолок стартового поля: вместимость, подрезанная бюджетом таблицы декад.
 *
 * Вместимость поля физическая и всегда 24 — в оригинале столько пузырей видно
 * уже на L7. А вот СТАРТ в оригинале доходит до 24 постепенно: на записанных
 * уровнях первой декады он занимает 16-24 пузыря. Бюджет таблицы выражает
 * именно это, поэтому подрезает только старт, а не поле.
 */
export function startCapacity(
  boardCapacity: number, startBubbles?: readonly [number, number] | null,
): number {
  if (!startBubbles) return boardCapacity;
  return Math.max(1, Math.min(boardCapacity, startBubbles[1]));
}

export function buildDeal(
  levelId: number, categories: readonly LevelCategory[], board: DealBoard,
  chunked: ChunkedWords = new Set<string>(),
  minStartWords = 1,
  scheme: readonly number[] | null = null,
  startBudget: readonly [number, number] | null = null,
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
    words: wholeWordsFirst(rng.shuffle(spawnableWords(category)), category.key, chunked),
  }));

  // бюджет поля считается в ПУЗЫРЯХ, а не в словах: распиленное слово стоит два
  const totalBubbles = pools.reduce(
    (n, p) => n + p.words.reduce((k, w) => k + cost(p.key, w), 0), 0);
  const fieldSize = Math.min(
    startCapacity(board.boardCapacity, startBudget), totalBubbles);

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

  /*
   * Явная схема выкладки (scheme): точные доли старта по убыванию, например
   * [4, 3, 3, 3, 2, 2, 2, 2, 1] — как в таблице замера оригинала по декадам.
   * Самая крупная доля достаётся точке входа (quickwin), остальные — категориям
   * в перемешанном порядке; категории за пределами схемы целиком в очереди.
   * Схема — ручной инструмент дизайнера: поле имеет право НЕ добираться до
   * вместимости (в референсе старт тоже плавает, 19-24 пузыря — см.
   * reference-deal-order.md §5), поэтому checkDeal для спека со схемой
   * проверяет только вместимость и полноту слов, а не точное заполнение.
   */
  const explicit = scheme && scheme.length > 0
    ? [...scheme].sort((a, b) => b - a).map((n) =>
      Math.max(0, Math.min(board.wordsPerCategory, Math.floor(n))))
    : null;
  /*
   * Схема без ручной настройки: считается автоматически (autoScheme) — глубина
   * вместо ширины, без одиночек. Историческая ровная раздача остаётся ровно там,
   * где была: при minStartWords = 1, то есть у пакетов, собранных до 03.08. Их
   * хеши закреплены тестом, и трогать их нельзя.
   */
  const tpl = explicit
    ?? (minStartWords >= 2
      ? autoScheme(fieldSize, pools.length, board.wordsPerCategory, minStartWords)
      : null);
  /*
   * Пол доли: сколько слов должно достаться категории, чтобы её вообще
   * выкладывать. У автоматической схемы это `minStartWords` (одиночек нет по
   * правилу): категория, у которой спавнящихся слов меньше пола — например
   * мета-родитель с тремя детьми, — на старт не идёт, её слово приходит
   * досыпкой. Ручная схема остаётся ручной: дизайнер вправе поставить в неё
   * единицу, и она исполняется как написано.
   */
  const shareFloor = explicit ? 1 : Math.max(2, minStartWords);

  let left = fieldSize;
  const openerWant = tpl ? tpl[0] : board.wordsPerCategory;
  if (opener && openerWant > 0 && left >= bubblesFor(opener, openerWant)) {
    counts.set(opener.key, openerWant);
    left -= bubblesFor(opener, openerWant);
  }

  /*
   * Раздача по схеме — и ручной, и автоматической. Доли идут по порядку
   * перемешанных категорий; «доля меньше пола» или «не влезло в бюджет поля
   * целиком» означает, что категория уходит в очередь целиком. Частичных долей
   * нет: иначе схема без одиночек могла бы породить одиночку.
   *
   * Порядок категорий — тот же rng.shuffle, что и у исторической ровной
   * раздачи: выкладка по-прежнему пересчитывается из одного спека.
   *
   * При minStartWords = 1 схемы нет, и работает исторический путь «всем
   * понемногу» ниже — байт в байт, это закреплено тестом воспроизводимости
   * старых пакетов.
   */
  const rest = rng.shuffle(pools.filter((p) => p !== opener));

  if (tpl) {
    /*
     * Доли раздаются НЕ по порядку категорий, а по способности их закрыть.
     *
     * «4» в схеме означает четыре слова на поле. Раньше доля отдавалась
     * очередной категории и молча урезалась до её размера
     * (`min(доля, слов в пуле)`), поэтому мета-родитель — у него спавнится три
     * слова, имя-мета на старте не лежит — превращал четвёрку схемы в тройку.
     * Схема из инструмента дизайнера становилась пожеланием: человек писал
     * «4-4-3-3», а на поле ложилось «4-3-3-3» и объяснить это можно было только
     * задним числом.
     *
     * Теперь для каждой доли ищется категория, которая её реально держит, и из
     * подходящих берётся самая тесная (best-fit): категорию с четырьмя словами
     * не тратим на тройку, пока в схеме есть неотданная четвёрка. Порядок
     * перебора — тот же перемешанный, поэтому выкладка остаётся
     * детерминированной и воспроизводится из спека.
     *
     * Доля, которую отдать некому (нет категории такого размера) или которая не
     * влезает в остаток поля, пропускается — и это единственные два случая, в
     * которых схема исполняется не полностью. Оба видны в карточке уровня.
     */
    const shares = opener && counts.get(opener.key) ? tpl.slice(1) : tpl;
    const queue = [...rest];
    for (const share of shares) {
      if (left <= 0) break;
      if (share < shareFloor) continue;
      let bestIndex = -1;
      let bestSpare = Infinity;
      for (let i = 0; i < queue.length; i += 1) {
        const pool = queue[i];
        if (pool.words.length < share) continue;
        const price = bubblesFor(pool, share);
        if (price > left) continue;
        const spare = pool.words.length - share;
        if (spare < bestSpare) { bestSpare = spare; bestIndex = i; }
      }
      if (bestIndex < 0) continue;
      const pool = queue[bestIndex];
      counts.set(pool.key, share);
      left -= bubblesFor(pool, share);
      queue.splice(bestIndex, 1);
    }
    return assembleDeal(categories, pools, counts, cost, rng);
  }

  // остаток раздаётся по кругу почти поровну: так на поле видно понемногу от
  // многих категорий, и игрок ищет связь, а не собирает готовое
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

  return assembleDeal(categories, pools, counts, cost, rng);
}

/**
 * Общий хвост обеих раздач: состав поля из счётчиков, очередь по ритму,
 * перемешивание поля. Порядок обращений к rng здесь фиксирован — он входит
 * в воспроизводимость выкладки из спека.
 */
function assembleDeal(
  categories: readonly LevelCategory[],
  pools: { key: string; words: string[] }[],
  counts: Map<string, number>,
  cost: (categoryKey: string, word: string) => number,
  rng: ReturnType<typeof createRng>,
): Deal {
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
 * Как устроена досыпка в прототипе: пачка приходит после сбора категории — 4
 * пузыря, или 3, если категория осталась на поле мета-словом, — и ещё один
 * пузырь после склейки половинок. Числа фиксированные: сколько мест
 * освободилось, столько и приходит. Значит порядок очереди — это и есть ритм
 * уровня: если пачка не даёт собрать ничего нового, игрок смотрит на поле из
 * одних недоборов и считает уровень сломанным.
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

    /*
     * Цели пачки: категории, которые дешевле всего довести до сбора. Их в пачке
     * может быть ДВЕ — требование владельца продукта 03.08: «досыпка должна
     * всегда открывать следующий сбор, а если на поле лежали тройки — два
     * следующих». Тройке не хватает одного слова, значит пачка в 4 пузыря
     * закрывает сразу пару таких категорий, и игра не встаёт после каждого
     * сбора. Больше двух не берём: остаток пачки обязан достаться добивке,
     * иначе поле превращается в конвейер готовых четвёрок.
     */
    for (let t = 0; t < 2; t += 1) {
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
      if (!target) break;
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

/**
 * Схема для конкретного уровня из вилки min/max таблицы декад.
 *
 * Позиция уровня в вилке определяется его числом категорий внутри коридора:
 * минимум коридора → schemeMin, максимум → schemeMax, между ними целевое
 * число стартовых слов интерполируется линейно, и схема достраивается от
 * min к max слева направо. Функция чистая и детерминированная: собранная
 * схема записывается в спек, и выкладка воспроизводится из одного спека.
 */
export function resolveScheme(
  schemeMin: readonly number[], schemeMax: readonly number[],
  categories: number, corridor: [number, number],
): number[] {
  const lo = [...schemeMin].sort((a, b) => b - a);
  const hi = [...schemeMax].sort((a, b) => b - a);
  // вилка обязана быть согласованной: hi поэлементно не меньше lo
  const width = Math.max(lo.length, hi.length);
  const floor = Array.from({ length: width }, (_, i) => lo[i] ?? 0);
  const ceil = Array.from({ length: width }, (_, i) =>
    Math.max(floor[i], hi[i] ?? 0));

  const sumLo = floor.reduce((a, b) => a + b, 0);
  const sumHi = ceil.reduce((a, b) => a + b, 0);
  const t = corridor[1] <= corridor[0] ? 1
    : Math.max(0, Math.min(1, (categories - corridor[0]) / (corridor[1] - corridor[0])));
  let budget = Math.round(sumLo + (sumHi - sumLo) * t) - sumLo;

  const counts = [...floor];
  for (let i = 0; budget > 0 && i < width; i += 1) {
    const add = Math.min(budget, ceil[i] - counts[i]);
    counts[i] += add;
    budget -= add;
  }
  // категорий на старте не может быть больше, чем категорий на уровне
  return counts.filter((n) => n > 0).sort((a, b) => b - a).slice(0, categories);
}

/** Пересчёт выкладки из готового спека — для проверок и для старых пакетов. */
export function dealForSpec(spec: LevelSpec): Deal {
  // Всё, что влияет на выкладку, обязано лежать в самом спеке. Распилы — в
  // spec.halves (без них слово считается одним пузырём и поле собирается
  // иначе), режим раздачи — в board.dealMinStartWords (без него старые пакеты
  // пересчитываются историческим путём «всем понемногу»), бюджет старта — в
  // board.dealStartBubbles (без него старт упирается в вместимость поля).
  const chunked = new Set(spec.halves.map((h) => chunkKey(h.home, h.word)));
  return buildDeal(spec.levelId, spec.categories, spec.board, chunked,
    spec.board.dealMinStartWords ?? 1, spec.board.dealScheme ?? null,
    spec.board.dealStartBubbles ?? null);
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
  const budget = spec.board.dealStartBubbles ?? null;
  const capacity = startCapacity(spec.board.boardCapacity, budget);
  if (startCost > capacity) {
    problems.push(`на поле ${startCost} пузырей при потолке старта ${capacity}`
      + (budget && budget[1] < spec.board.boardCapacity
        ? ` (вместимость ${spec.board.boardCapacity}, бюджет декады ${budget[1]})` : ''));
  }
  const totalBubbles = bubbleCost([...deal.start, ...deal.queue]);
  const fieldSize = Math.min(capacity, totalBubbles);
  /*
   * Пол бюджета: столько пузырей старт обязан набрать, если материала хватает.
   * Проверяется только у автоматической раздачи — ручная схема сознательно
   * вправе не добирать поле (в референсе старт тоже плавает, 19-24), и требовать
   * от неё пола значило бы запрещать то, что дизайнер написал руками.
   */
  const manualScheme = !!(spec.board.dealScheme && spec.board.dealScheme.length > 0);
  if (budget && !manualScheme && totalBubbles >= budget[0] && startCost < budget[0]) {
    problems.push(`на старте ${startCost} пузырей, таблица декад требует минимум `
      + `${budget[0]} (пузырей в уровне ${totalBubbles})`);
  }
  // поле имеет право не добрать один пузырь: когда остаток бюджета — одно
  // место, а класть осталось только распиленные слова по два места каждое.
  // При явной схеме выкладки точное заполнение не требуется вовсе: схема —
  // ручной инструмент, и поле в референсе тоже плавает (19-24 пузыря)
  const exactFill = !(spec.board.dealScheme && spec.board.dealScheme.length > 0);
  if (exactFill && startCost !== fieldSize && startCost !== fieldSize - 1) {
    problems.push(`на поле ${startCost} пузырей, ожидалось ${fieldSize}`);
  }

  return problems;
}
