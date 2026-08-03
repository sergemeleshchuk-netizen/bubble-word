/**
 * Движок партии: поле, очередь досыпки, правила мерджа, страховки.
 *
 * Зачем отдельный модуль. Правила «что с чем сливается» нужны ДВУМ разным
 * ботам: зрячему (`simulatePlayability.ts` — знает ответы, отвечает на вопрос
 * «хватит ли лимита идеальному игроку») и слепому (`simulateBlindPlay.ts` —
 * читает слова, а не ответы, и платит ходами за неверные догадки). Держать
 * правила в двух копиях нельзя: копии разъезжаются молча, и тогда hard-гейт и
 * диагностика начинают судить об уровне по разным законам.
 *
 * Границу провели так: движок знает ПРАВДУ (какой пузырь какой категории) и
 * механику, бот знает только то, что видит, и решает, что тащить. Всё, что
 * является фактом партии — волны досыпки, страховки, схлопывания, счётчик
 * ходов, — считает движок. Всё, что является МНЕНИЕМ игрока — «поле выглядит
 * тупиком», «я не вижу здесь связи», — считает бот.
 *
 * Правила 1в1 с прототипом (`site/playable/index.html`):
 *   - мердж легален внутри одной категории и пока сумма слов не превышает 4;
 *     половинка склеивается только со своей парой; каждый мердж стоит 1 ход;
 *   - ЛОГИЧЕСКИЙ промах (потащил на чужой пузырь) тоже стоит ход — на этой
 *     цене ошибки и держится давление лимита (GDD §2 п.3);
 *   - преграда (лёд, «?», цепь) хода НЕ ест: догадку о слове о неё даже не
 *     проверили;
 *   - четвёрка схлопывается бесплатно; обычная категория улетает и приходит
 *     досыпка в 4 пузыря, мета-категория превращается в слово родителя и
 *     приходит 3 (одно место поле уже получило);
 *   - лёд и «?» не мерджатся, пока не растают: каждый УСПЕШНЫЙ мердж на поле
 *     снимает один слой со всех заблокированных;
 *   - цепь делит поле на две зоны, мердж поперёк запрещён; снимается сбором
 *     `need` категорий;
 *   - страховки, в порядке прототипа: нет легального мерджа → сначала падает
 *     цепь, потом тает лёд, потом досыпка «вне ритма» в 4 пузыря.
 *
 * Известное упрощение, общее для обоих ботов: ёмкость поля не моделируется —
 * всё, что досыпано, считается видимым. У зрячего бота это ни на что не влияет
 * (порядок мерджей не меняет их числа), у слепого завышает выбор гипотез, то
 * есть даёт ему фору. Оценки слепого прогона поэтому оптимистичны, и это
 * записано в его отчёте.
 */
import type { LevelSpec } from './types.ts';

/** Пузырь на поле. `category` — правда движка, а не мнение игрока. */
export interface SimBubble {
  /** стабильный за партию номер: слепому боту нужен ключ для памяти */
  readonly id: number;
  category: string;
  /** слова внутри кластера; у половинки — одно слово, как и у целого пузыря */
  words: string[];
  /** id пары половинок; 0 — обычный пузырь */
  halfPair: number;
  /** какая это часть пары */
  halfSide: 0 | 1;
  /** слоёв льда или «?» осталось */
  blocked: number;
  /** зона относительно цепи; без цепи всегда 0 */
  zone: 0 | 1;
}

/** Почему мердж не состоялся. `wrong` — неверная догадка, остальное — преграда. */
export type MergeWhy = 'wrong' | 'blocked' | 'chain';

export interface AttemptResult {
  ok: boolean;
  why?: MergeWhy;
  /** потрачен ли ход: успешный мердж и логический промах — да, преграда — нет */
  moveSpent: boolean;
  /** категория, схлопнувшаяся этим ходом; null — не схлопнулось ничего */
  collected: string | null;
}

/** Какая страховка сработала, когда легальных мерджей не осталось. */
export type Rescue = 'chain' | 'blockers' | 'refill' | null;

const BATCH = 4;

/** Ключ распиленного слова — регистронезависимо, как в deal.ts. */
function halfKey(category: string, word: string): string {
  return `${category}::${word.toLowerCase()}`;
}

export interface PlaySim {
  /** живое поле: индексы валидны до следующего attempt/rescue */
  readonly field: readonly SimBubble[];
  /** слов в очереди досыпки */
  queueLength(): number;
  /** собрано категорий */
  categoriesDone(): number;
  categoriesTotal(): number;
  /** уровень собран целиком */
  won(): boolean;
  /** ходов потрачено (успешные мерджи + логические промахи) */
  moves(): number;
  /** сколько слов у категории по спеку */
  fullOf(category: string): number;
  /** законно ли слить: правда движка, боту напрямую недоступна */
  verdict(i: number, j: number): { ok: true } | { ok: false; why: MergeWhy };
  /** все законные пары; для зрячего бота это и есть список ходов */
  legalPairs(): [number, number][];
  /** попытка мерджа: считает ход, схлопывает, досыпает, тает лёд */
  attempt(i: number, j: number): AttemptResult;
  /** следующая страховка прототипа; null — страховок больше нет */
  rescue(): Rescue;
  /**
   * Досыпка-подсказка после серии промахов. Отдельный вход, а не `rescue()`:
   * это другое событие — поле не встало, игрок перебирает наугад, — и в
   * счётчик «досыпок вне ритма» оно попадать не должно.
   */
  hintRefill(): boolean;
  /** факты партии, накопленные движком */
  stats(): SimStats;
}

export interface SimStats {
  /** досыпок «вне ритма» — поле вставало без единого мерджа при живой очереди */
  rescues: number;
  /** волн досыпки за партию */
  refillWaves: number;
  /** волн, сразу открывших сбор новой категории целиком */
  refillCompletions: number;
  /** самая длинная серия ходов без единого сбора категории */
  maxDrought: number;
  /** цепь пришлось снять страховкой, а не сбором категорий */
  chainRescued: boolean;
  /** лёд/«?» пришлось снять страховкой, а не мерджами */
  blockersRescued: boolean;
}

/**
 * Спек без выкладки симулировать нечем: такие приезжают из пакетов до gen-1.1.
 * Вернуть «партия прошла» здесь было бы враньём, поэтому создание движка на
 * таком спеке — явная ошибка, а не тихий зелёный вердикт. Проверять обязан
 * вызывающий: у него есть чем ответить пользователю.
 */
export function hasDeal(spec: LevelSpec): boolean {
  return Boolean(spec.deal && Array.isArray(spec.deal.start)
    && Array.isArray(spec.deal.queue));
}

export function createPlaySim(spec: LevelSpec): PlaySim {
  const fullOfMap = new Map<string, number>();
  for (const c of spec.categories) fullOfMap.set(c.key, c.words.length);

  /*
   * Мета-связь: сбор дочерней категории рождает пузырь-слово родителя. Текст
   * слова здесь нужен наравне с ключом категории — слепой бот читает слова, и
   * мета-пузырь без текста был бы для него дырой в поле.
   */
  const metaWordOf = new Map<string, { parent: string; text: string }>();
  for (const c of spec.categories) {
    for (const w of c.words) {
      if (w.kind === 'meta' && w.metaChild) {
        metaWordOf.set(w.metaChild, { parent: c.key, text: w.text });
      }
    }
  }

  // распилы: слово из выкладки превращается в два пузыря-половинки
  const halves = new Map<string, number>();
  spec.halves.forEach((h, i) => halves.set(halfKey(h.home, h.word), i + 1));

  const frozen = new Map<string, number>();
  for (const b of [...spec.modifiers.frozenBubbles, ...spec.modifiers.hiddenBubbles]) {
    frozen.set(halfKey(b.category, b.word), b.layers);
  }

  interface QueueItem {
    category: string;
    halfPair: number;
    halfSide: 0 | 1;
    word: string;
  }

  const expand = (list: readonly { word: string; category: string }[]): QueueItem[] => {
    const out: QueueItem[] = [];
    for (const b of list) {
      const pair = halves.get(halfKey(b.category, b.word)) ?? 0;
      if (!pair) {
        out.push({ category: b.category, halfPair: 0, halfSide: 0, word: b.word });
      } else {
        out.push({ category: b.category, halfPair: pair, halfSide: 0, word: b.word });
        out.push({ category: b.category, halfPair: pair, halfSide: 1, word: b.word });
      }
    }
    return out;
  };

  const chain = spec.modifiers.chainLine;
  let chainUp = chain !== null && chain !== undefined;
  const chainNeed = chain?.need ?? 0;

  let zoneFlip = 0;
  let nextId = 0;
  const toBubble = (item: QueueItem): SimBubble => ({
    id: (nextId += 1),
    category: item.category,
    words: [item.word],
    halfPair: item.halfPair,
    halfSide: item.halfSide,
    blocked: item.halfPair === 0 ? (frozen.get(halfKey(item.category, item.word)) ?? 0) : 0,
    // зону цепи прототип назначает по координате; у симуляции координат нет,
    // поэтому зоны чередуются — худший для игрока случай «категория размазана
    // по обе стороны» при этом воспроизводится регулярно
    zone: chainUp ? ((zoneFlip += 1) % 2 === 0 ? 0 : 1) : 0,
  });

  const field: SimBubble[] = expand(spec.deal.start).map(toBubble);
  const queue: QueueItem[] = expand(spec.deal.queue);

  const totalCats = spec.categories.length;
  let done = 0;
  let moves = 0;
  let drought = 0;
  const stats: SimStats = {
    rescues: 0, refillWaves: 0, refillCompletions: 0, maxDrought: 0,
    chainRescued: false, blockersRescued: false,
  };

  const fullOf = (category: string): number => fullOfMap.get(category) ?? 4;

  /**
   * Категории, которые ПРЯМО СЕЙЧАС собираются целиком: все слова на поле,
   * ничто из них не заблокировано. Множество, а не флаг: пачка досыпки
   * считается продуктивной, если после неё появилась НОВАЯ такая категория —
   * иначе продуктивной выглядела бы любая пачка, пришедшая при уже открытом
   * сборе.
   */
  const completableSet = (): Set<string> => {
    const sums = new Map<string, number>();
    const blockedCats = new Set<string>();
    for (const b of field) {
      if (b.halfPair) continue;
      if (b.blocked > 0) blockedCats.add(b.category);
      sums.set(b.category, (sums.get(b.category) ?? 0) + b.words.length);
    }
    const out = new Set<string>();
    for (const [cat, n] of sums) {
      if (blockedCats.has(cat)) continue;
      if (n >= fullOf(cat)) out.add(cat);
    }
    return out;
  };

  const spawn = (n: number): void => {
    if (n <= 0 || queue.length === 0) return;
    const before = completableSet();
    for (let i = 0; i < n && queue.length > 0; i += 1) {
      field.push(toBubble(queue.shift()!));
    }
    stats.refillWaves += 1;
    const after = completableSet();
    for (const cat of after) {
      if (!before.has(cat)) { stats.refillCompletions += 1; break; }
    }
  };

  const verdict = (i: number, j: number): { ok: true } | { ok: false; why: MergeWhy } => {
    const a = field[i];
    const b = field[j];
    if (a.blocked > 0 || b.blocked > 0) return { ok: false, why: 'blocked' };
    if (chainUp && a.zone !== b.zone) return { ok: false, why: 'chain' };
    if (a.halfPair || b.halfPair) {
      return a.halfPair === b.halfPair && a.halfSide !== b.halfSide
        ? { ok: true } : { ok: false, why: 'wrong' };
    }
    if (a.category !== b.category) return { ok: false, why: 'wrong' };
    return a.words.length + b.words.length <= fullOf(a.category)
      ? { ok: true } : { ok: false, why: 'wrong' };
  };

  const legalPairs = (): [number, number][] => {
    const out: [number, number][] = [];
    for (let i = 0; i < field.length; i += 1) {
      for (let j = i + 1; j < field.length; j += 1) {
        if (verdict(i, j).ok) out.push([i, j]);
      }
    }
    return out;
  };

  /** Сбор категории: бесплатно; мета превращается в слово родителя. */
  const collect = (index: number): string => {
    const cat = field[index].category;
    field.splice(index, 1);
    done += 1;
    stats.maxDrought = Math.max(stats.maxDrought, drought);
    drought = 0;
    if (chainUp && done >= chainNeed) chainUp = false;
    const meta = metaWordOf.get(cat);
    if (meta) {
      field.push({
        id: (nextId += 1),
        category: meta.parent, words: [meta.text],
        halfPair: 0, halfSide: 0, blocked: 0,
        zone: chainUp ? ((zoneFlip += 1) % 2 === 0 ? 0 : 1) : 0,
      });
      spawn(BATCH - 1);
    } else {
      spawn(BATCH);
    }
    return cat;
  };

  return {
    field,
    queueLength: () => queue.length,
    categoriesDone: () => done,
    categoriesTotal: () => totalCats,
    won: () => done >= totalCats,
    moves: () => moves,
    fullOf,
    verdict,
    legalPairs,

    attempt(rawI: number, rawJ: number): AttemptResult {
      // порядок нормализуем: splice(j) не должен сдвигать i
      const i = Math.min(rawI, rawJ);
      const j = Math.max(rawI, rawJ);
      const v = verdict(i, j);
      if (!v.ok) {
        /*
         * Преграда хода не ест, неверная догадка ест. Это не деталь баланса, а
         * ровно то место, где слепой бот начинает отличаться от зрячего: у
         * зрячего этой ветки не бывает никогда.
         */
        if (v.why === 'wrong') { moves += 1; drought += 1; }
        return { ok: false, why: v.why, moveSpent: v.why === 'wrong', collected: null };
      }

      const a = field[i];
      const b = field[j];
      if (a.halfPair) {
        // склейка половинок: получился обычный пузырь-слово, счётчик слов
        // категории не вырос, а ход потрачен — как в прототипе
        a.halfPair = 0; a.halfSide = 0;
        field.splice(j, 1);
      } else {
        a.words = [...a.words, ...b.words];
        field.splice(j, 1);
      }
      moves += 1;
      drought += 1;
      for (const bubble of field) if (bubble.blocked > 0) bubble.blocked -= 1;

      let collected: string | null = null;
      if (a.halfPair === 0 && a.words.length >= fullOf(a.category)) {
        collected = collect(field.indexOf(a));
      }
      return { ok: true, moveSpent: true, collected };
    },

    rescue(): Rescue {
      // страховки прототипа, в его порядке: цепь → лёд → досыпка вне ритма
      if (chainUp) { chainUp = false; stats.chainRescued = true; return 'chain'; }
      if (field.some((b) => b.blocked > 0)) {
        for (const b of field) b.blocked = 0;
        stats.blockersRescued = true;
        return 'blockers';
      }
      if (queue.length > 0) { stats.rescues += 1; spawn(BATCH); return 'refill'; }
      return null;
    },

    hintRefill(): boolean {
      if (queue.length === 0) return false;
      spawn(BATCH);
      return true;
    },

    stats: () => ({ ...stats }),
  };
}

/**
 * Досыпка-подсказка прототипа: MISS_RESCUE неверных попыток ПОДРЯД — это уже не
 * ловушка, а перебор наугад, и поле пополняется помощью. Зрячий бот этой ветки
 * не достигает никогда (он не промахивается), слепой — регулярно.
 *
 * Число совпадает с `MISS_RESCUE_DEFAULT` в прототипе. Оно там подбирается
 * наигровкой, поэтому живёт константой и здесь, а не выводится из чего-либо.
 */
export const MISS_RESCUE = 5;
