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
import type { Deal, DealBubble, DealGate, LevelCategory, LevelSpec } from './types.ts';

export interface DealBoard {
  boardCapacity: number;
  wordsPerCategory: number;
}

/**
 * С какого размера уровня линии выстраиваются В ОЧЕРЕДЬ, а не выкладываются все
 * сразу.
 *
 * Арифметика поля: пузырей на поле 24, категория собирается из четырёх. Значит
 * больше двенадцати ЖИВЫХ линий одновременно — это поле, на котором в среднем
 * меньше двух слов на категорию, то есть собрать нельзя ничего, чем бы досыпка
 * ни помогала. Уровень на 16-18 категорий именно так и играется: старт кладёт
 * обрывки восьми линий, а остальные восемь ждут в очереди вперемешку, и пачка в
 * 4 пузыря почти всегда приносит слова тех линий, которых на поле по одному.
 *
 * Поэтому крупный уровень раскладывается ВОЛНАМИ: часть категорий не выходит на
 * поле вовсе, пока игрок не соберёт заданное число других (`planGates`). Пока
 * гейт закрыт, досыпка выбирает из очереди только открытые линии — то есть
 * тратит пачку на те категории, которые на поле уже начаты. Требование
 * владельца продукта 04.08: «в уровнях больше 12 категорий 4 категории не
 * показываются до некоторого прогресса — тогда досыпка сработает».
 */
export const QUEUE_STAGING_FROM = 13;

/** Сколько категорий крупный уровень откладывает за гейты по умолчанию. */
export const STAGED_CATEGORIES = 4;

/**
 * Сколько линий обязано остаться на раннем поле. Гейты не имеют права
 * превратить старт в три категории: игроку нужен выбор, а не коридор.
 */
const MIN_OPEN_LINES = 9;

/**
 * Отложенные категории и порог для каждой: очередь линий уровня.
 *
 * Кого откладываем. Сначала «чистые» линии — без мета-связей и не точку входа:
 * мета-родитель, ушедший за гейт, уносит с собой всю ветку (его слово рождается
 * сбором ребёнка), а точка входа обязана лежать на старте целиком. Мета и
 * quickwin берутся только если чистых линий не хватило: гейт всё равно полезнее
 * ровной раздачи всех линий сразу.
 *
 * Когда открываем. Пороги раскладываются по РАННЕЙ части уровня: i-я отложенная
 * линия открывается после `(i+1) * открытых / (отложенных + 2)` сборов. На
 * уровне 16 категорий это 2, 4, 6 и 8 сборов — последняя линия приходит около
 * половины прогресса, когда поле уже освободилось. Пороги строго возрастают:
 * две линии, открывающиеся одновременно, — это та же ровная раздача, только
 * позже.
 *
 * Делитель `+2`, а не `+1`, из-за хвоста уровня: порог, поставленный слишком
 * поздно, оставляет очередь без пузырей ОТКРЫТЫХ линий, и досыпке приходится
 * вскрывать гейт (`gatesForced` в core/playSim.ts). С делителем `+1` декада 51
 * не собиралась целиком: один уровень из десяти не проходил приёмку за 48
 * попыток именно по этой причине.
 *
 * Выбор детерминирован через `stableWeight`, а не `shuffle`: поток `rng` здесь
 * трогать нельзя — на нём стоит воспроизводимость выкладки уровней без гейтов.
 */
export function planGates(
  categories: readonly LevelCategory[], hold: number,
  rng: ReturnType<typeof createRng>,
): DealGate[] {
  if (hold <= 0 || categories.length < QUEUE_STAGING_FROM) return [];
  // потолок MIN_OPEN_LINES-1 держит пороги внутри уровня: при count+1 <= открытых
  // лестница «строго возрастая» гарантированно укладывается в раннюю часть
  const count = Math.min(hold, categories.length - MIN_OPEN_LINES, MIN_OPEN_LINES - 1);
  if (count <= 0) return [];

  const metaParents = new Set(categories
    .filter((c) => c.words.some((w) => w.kind === 'meta')).map((c) => c.key));
  const metaChildren = new Set(categories
    .filter((c) => c.parentKey !== null).map((c) => c.key));
  /** Чем меньше ранг, тем охотнее линию откладываем. */
  const rank = (c: LevelCategory): number =>
    (metaParents.has(c.key) ? 4 : 0)
    + (metaChildren.has(c.key) ? 2 : 0)
    + (c.isQuickwin ? 1 : 0);

  const held = [...categories]
    .sort((a, b) => (rank(a) - rank(b))
      || (rng.stableWeight(`gate::${a.key}`) - rng.stableWeight(`gate::${b.key}`))
      || (a.key < b.key ? -1 : 1))
    .slice(0, count);

  const open = categories.length - count;
  const gates: DealGate[] = [];
  let prev = 0;
  held.forEach((category, i) => {
    const want = Math.round(((i + 1) * open) / (count + 2));
    const after = Math.max(prev + 1, Math.min(open, want));
    prev = after;
    gates.push({ category: category.key, afterCollected: after });
  });
  return gates;
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
 * Сколько категорий старт выкладывает ЦЕЛИКОМ — готовыми четвёрками.
 *
 * Требование владельца продукта 04.08 после наигровки собранной десятки:
 * «добавь в конфиг, чтобы везде было минимум 3 четвёрки — всё ещё неиграбельно
 * для рядового не носителя языка».
 *
 * Почему это именно та ручка. Одна готовая четвёрка (прежнее правило: «вход»)
 * даёт неносителю один очевидный ход. Дальше поле — тройки и пары незнакомых
 * слов, и чтобы сделать второй ход, нужно УГАДАТЬ категорию, а не увидеть её.
 * Носитель языка на это не жалуется: у него связь «radish — овощ» бесплатная.
 * Три готовые четвёрки дают три хода, видимых глазами, и три сбора подряд —
 * а каждый сбор приносит пачку досыпки, то есть новые слова к тем обрывкам,
 * которые игрок пока не понял.
 *
 * Чем платим: шириной старта. 24 пузыря при трёх четвёрках открывают 7 линий
 * вместо 8 (было 4-3-3-3-3-3-3-2, стало 4-4-4-3-3-3-3), остальные категории
 * ждут в очереди целиком. Обмен сознательный.
 */
export const DEAL_MIN_FULL_SETS = 3;

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
  wordsPerCategory = 4, minStartWords = 2, minFullSets = 1,
): number[] {
  const floor = Math.max(2, minStartWords);
  const out: number[] = [];
  let left = fieldBubbles;

  /*
   * Готовые четвёрки: категории, которые видно целиком и можно собрать не
   * дожидаясь досыпки. Первая — «вход» (её получает quickwin), дальше столько,
   * сколько просит `minFullSets` и позволяет бюджет поля. Доля меньше полной
   * четвёркой не считается: если места не хватило, остаток раздают правила ниже
   * (тройки и одна пара). При minFullSets = 1 это ровно прежний «вход».
   */
  const wantFull = Math.max(1, Math.min(minFullSets, categories));
  while (categories > 0 && out.length < wantFull && left >= floor) {
    const share = Math.min(wordsPerCategory, left);
    if (out.length > 0 && share < wordsPerCategory) break;
    out.push(share);
    left -= share;
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
  holdCategories = 0,
  minFullSets = 1,
): Deal {
  const rng = createRng(`deal::${levelId}::${categories.map((c) => c.key).join(',')}`);
  /** Сколько мест на поле занимает слово: распиленное — два. */
  const cost = (categoryKey: string, word: string): number =>
    (chunked.has(chunkKey(categoryKey, word)) ? 2 : 1);

  /*
   * Очередь линий: отложенные категории на старт не идут вовсе и в досыпке ждут
   * своего порога. Считается до раздачи, потому что бюджет старта обязан делиться
   * между ОТКРЫТЫМИ линиями: иначе схема отдала бы четвёрку категории, которой на
   * поле ещё нет.
   */
  const gates = planGates(categories, holdCategories, rng);
  const gateOf = new Map(gates.map((g) => [g.category, g.afterCollected]));

  const pools = categories.map((category) => ({
    key: category.key,
    isQuickwin: category.isQuickwin,
    // порядок внутри категории тасуется: иначе на поле всегда оказывались бы
    // первые слова спека, а в очередь уходили последние — а спек упорядочен
    // по очевидности слова, и игрок получал бы самые явные слова бесплатно
    words: wholeWordsFirst(rng.shuffle(spawnableWords(category)), category.key, chunked),
  }));
  const open = pools.filter((p) => !gateOf.has(p.key));

  // бюджет поля считается в ПУЗЫРЯХ, а не в словах: распиленное слово стоит два.
  // За гейтом лежащие линии в бюджет старта не входят — их на поле нет
  const totalBubbles = open.reduce(
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
  const whole = open.filter((p) => p.words.length >= board.wordsPerCategory);
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
      ? autoScheme(fieldSize, open.length, board.wordsPerCategory, minStartWords,
        minFullSets)
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
   *
   * Отложенных линий в раздаче старта нет по построению: они не в `open`.
   */
  const rest = rng.shuffle(open.filter((p) => p !== opener));

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
    return assembleDeal(categories, pools, counts, cost, rng, gateOf);
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

  return assembleDeal(categories, pools, counts, cost, rng, gateOf);
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
  gateOf: Map<string, number>,
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
  const queue = paceQueue(categories, pools, counts, cost, rng, gateOf);
  const deal: Deal = { start: rng.shuffle(start), queue };
  // пустого списка не пишем: уровень без гейтов должен остаться прежним и в
  // хеше, и в экспорте — канонический сериализатор выбрасывает undefined
  if (gateOf.size > 0) {
    deal.gates = [...gateOf.entries()]
      .map(([category, afterCollected]) => ({ category, afterCollected }))
      .sort((a, b) => a.afterCollected - b.afterCollected);
  }
  return deal;
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
 *
 * Гейты (`gateOf`) очередь УЧИТЫВАЕТ: слово отложенной линии не попадает в
 * пачку, пока сборов меньше порога. Иначе порядок очереди и порядок спавна
 * расходились бы — клиент пропускал бы закрытые линии и брал следующее слово,
 * то есть играл бы не по тому ритму, который здесь посчитан.
 */
function paceQueue(
  categories: readonly LevelCategory[],
  pools: { key: string; words: string[] }[],
  counts: Map<string, number>,
  cost: (categoryKey: string, word: string) => number,
  rng: ReturnType<typeof createRng>,
  gateOf: Map<string, number>,
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

  /** Сборов позади: по нему открываются гейты отложенных линий. */
  let collected = 0;
  const gateOpen = (key: string): boolean => (gateOf.get(key) ?? 0) <= collected;

  let guard = categories.length * 8;
  while (guard > 0) {
    guard -= 1;
    const key = collectible();
    if (!key) break;
    // сбор: слова категории уходят с поля; мета-ребёнок дарит родителю слово
    collected += 1;
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
        if (!gateOpen(c.key)) continue;                        // линия ещё не открыта
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

    /*
     * Добивка: слова других начатых категорий, чтобы на поле было чем ходить;
     * нетронутые категории идут в хвосте — они открывают новую линию, когда
     * у начатых слова кончились.
     *
     * Исключение — линия, гейт которой открылся ИМЕННО ЭТИМ сбором: она идёт
     * первой. Иначе очередь ставила её в общий хвост «нетронутых», и на замере
     * уровня 209 (17 категорий) три отложенных линии из четырёх приезжали на
     * поле разом при 13 собранных — то есть порог 2, 4 и 7 сборов не работал, а
     * последняя треть уровня превращалась во второй уровень внутри первого.
     * Волна обязана совпадать с открытием: гейт для этого и нужен.
     */
    const shuffledKeys = rng.shuffle(pools.map((p) => p.key))
      .filter((k) => gateOpen(k));
    const justOpened = (k: string): boolean => gateOf.get(k) === collected;
    const fillers = [
      ...shuffledKeys.filter((k) => justOpened(k)),
      ...shuffledKeys.filter((k) => !justOpened(k) && (fieldCount.get(k) ?? 0) > 0),
      ...shuffledKeys.filter((k) => !justOpened(k) && (fieldCount.get(k) ?? 0) === 0),
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
  // идёт группами по категориям: каждая волна тогда хотя бы завершает одну.
  // Отложенные линии в хвосте стоят по порядку своих порогов: клиент всё равно
  // пропустит закрытую, но очередь обязана читаться так же, как играется
  const leftovers = [...pending.entries()].filter(([, w]) => w.length > 0)
    .sort((a, b) => ((gateOf.get(a[0]) ?? 0) - (gateOf.get(b[0]) ?? 0))
      || ((fieldCount.get(b[0]) ?? 0) - (fieldCount.get(a[0]) ?? 0)));
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
    spec.board.dealStartBubbles ?? null, spec.board.dealHoldCategories ?? 0,
    spec.board.dealMinFullSets ?? 1);
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

  /*
   * Очередь линий: отложенная категория обязана отсутствовать на старте, а её
   * порог — быть достижимым внутри уровня. Порог, равный числу категорий, линию
   * не откладывает, а хоронит: собрать её было бы нужно ПОСЛЕ победы.
   */
  const gates = deal.gates ?? [];
  const keys = new Set(spec.categories.map((c) => c.key));
  const gated = new Set(gates.map((g) => g.category));
  for (const gate of gates) {
    if (!keys.has(gate.category)) {
      problems.push(`гейт ${gate.category}: такой категории в уровне нет`);
    }
    if (!(gate.afterCollected >= 1 && gate.afterCollected < spec.categories.length)) {
      problems.push(`гейт ${gate.category}: порог ${gate.afterCollected} вне `
        + `1..${spec.categories.length - 1}`);
    }
  }
  if (gated.size !== gates.length) problems.push('гейты дублируют категорию');
  for (const bubble of deal.start) {
    if (gated.has(bubble.category)) {
      problems.push(`${bubble.category}::${bubble.word}: линия за гейтом, `
        + 'а пузырь лежит на старте');
    }
  }

  const startCost = bubbleCost(deal.start);
  const budget = spec.board.dealStartBubbles ?? null;
  const capacity = startCapacity(spec.board.boardCapacity, budget);
  if (startCost > capacity) {
    problems.push(`на поле ${startCost} пузырей при потолке старта ${capacity}`
      + (budget && budget[1] < spec.board.boardCapacity
        ? ` (вместимость ${spec.board.boardCapacity}, бюджет декады ${budget[1]})` : ''));
  }
  // бюджет старта делится только между ОТКРЫТЫМИ линиями: пузыри за гейтом на
  // поле попасть не могут, и требовать от старта их места нельзя
  const totalBubbles = bubbleCost([...deal.start, ...deal.queue]
    .filter((b) => !gated.has(b.category)));
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
  /*
   * Готовые четвёрки на старте: требование играбельности для не носителя языка
   * (`DEAL_MIN_FULL_SETS`). Проверяется только у автоматической раздачи и только
   * когда материала хватает: три четвёрки — это 12 пузырей и три категории с
   * четырьмя спавнящимися словами (мета-родитель четвёрку держать не может, его
   * имя на поле не лежит). Если уровень мельче или бюджет старта меньше — спрос
   * опускается до того, что физически возможно, иначе приёмка запрещала бы
   * туториальные уровни с неполным полем.
   */
  const wantFullSets = spec.board.dealMinFullSets ?? 1;
  if (!manualScheme && wantFullSets >= 2) {
    const full = spec.board.wordsPerCategory || 4;
    const roomy = spec.categories.filter((c) =>
      !gated.has(c.key) && spawnableWords(c).length >= full).length;
    const need = Math.min(wantFullSets, roomy, Math.floor(capacity / full));
    const onField = new Map<string, number>();
    for (const bubble of deal.start) {
      onField.set(bubble.category, (onField.get(bubble.category) ?? 0) + 1);
    }
    // четвёрка считается готовой, только если её МОЖНО собрать сейчас: у
    // мета-родителя на поле лежат три слова из четырёх, четвёртое родится сбором
    // ребёнка — такая категория ходом на старте не является
    const have = spec.categories.filter((c) => spawnableWords(c).length >= full
      && (onField.get(c.key) ?? 0) >= full).length;
    if (have < need) {
      problems.push(`на старте ${have} готовых четвёрок, нужно ${need}`);
    }
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
