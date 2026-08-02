/**
 * Динамическая проверка проходимости: симуляция партии по правилам
 * играбельного прототипа (site/playable/index.html).
 *
 * Зачем. Слепой решатель отвечает «однозначен ли уровень семантически»,
 * счётчик решений — «одна ли у него раскладка». Ни тот, ни другой не видят
 * ДИНАМИКУ: выкладку, ритм досыпки и лимит ходов. Инцидент 02.08: уровень 12
 * «как в оригинале» формально проходим, но после первого сбора игрок упёрся
 * в поле из одних недоборов с единственным неочевидным мерджем — и честно
 * решил, что уровень сломан. Такое состояние ловится только проигрыванием.
 *
 * Правила симуляции 1в1 с прототипом:
 *   - мердж легален внутри одной категории и пока сумма слов не превышает 4;
 *     половинка склеивается только со своей парой; каждый мердж стоит 1 ход;
 *   - четвёрка схлопывается бесплатно; обычная категория улетает и приходит
 *     досыпка в 4 ПУЗЫРЯ, мета-категория превращается в слово родителя и
 *     приходит 3 (одно место поле уже получило);
 *   - лёд и «?» не мерджатся, пока не растают: каждый успешный мердж на поле
 *     снимает один слой со всех заблокированных;
 *   - цепь делит поле на две зоны, мердж поперёк запрещён; снимается сбором
 *     `need` категорий;
 *   - страховки прототипа, в его же порядке: нет легального мерджа → сначала
 *     падает цепь, потом тает лёд, потом досыпка «вне ритма» в 4 пузыря;
 *   - жёсткий тупик: мерджей нет, очередь пуста, уровень не собран.
 *
 * Бот играет жадно: завершающий мердж, иначе склейка половинок, иначе мердж
 * в категории с максимумом слов на поле. На число ходов до победы порядок
 * мерджей не влияет (каждый мердж уменьшает число кусков ровно на 1), поэтому
 * вердикт «хватит ли лимита» точный. А вот метрики ритма — досыпки вне ритма,
 * «тупики на глаз», серия ходов без сбора — считаются для этого разумного
 * игрока и служат меркой UX, а не абсолютной истиной.
 */
import type { LevelSpec } from './types.ts';

export interface PlayabilityResult {
  /** уровень доигрывается до конца и укладывается в лимит ходов */
  winnable: boolean;
  /** человекочитаемая причина провала; null, если уровень проходим */
  failReason: string | null;
  /** ходов потребовалось разумному игроку (равно минимуму: мерджи не тратятся зря) */
  movesNeeded: number;
  /** лимит уровня; null — туториал без лимита */
  moveLimit: number | null;
  /** запас: лимит − нужно; null при безлимите */
  spareMoves: number | null;
  /** досыпок «вне ритма» — поле вставало без единого мерджа при живой очереди */
  rescues: number;
  /** состояний «выглядит тупиком»: собрать нечего и легальных мерджей ≤ 1 */
  perceivedDead: number;
  /** самая длинная серия ходов без единого сбора категории */
  maxDrought: number;
  /** волн досыпки за партию (пачка после сбора, склейки или страховки) */
  refillWaves: number;
  /**
   * Волн, которые СРАЗУ открыли сбор: после пачки на поле появилась категория,
   * собираемая целиком. Это мера того, ведёт ли уровень игрока за руку: пачка
   * либо приносит развязку, либо только добавляет обрывков.
   */
  refillCompletions: number;
  /** цепь пришлось снять страховкой, а не сбором категорий */
  chainRescued: boolean;
  /** лёд/«?» пришлось снять страховкой, а не мерджами */
  blockersRescued: boolean;
}

interface SimBubble {
  category: string;
  /** сколько слов внутри (кластер); у половинки всегда 1 */
  words: number;
  /** id пары половинок; 0 — обычный пузырь */
  halfPair: number;
  /** какая это часть пары */
  halfSide: 0 | 1;
  /** слоёв льда или «?» осталось */
  blocked: number;
  /** зона относительно цепи; без цепи всегда 0 */
  zone: 0 | 1;
}

interface QueueItem {
  category: string;
  halfPair: number;
  halfSide: 0 | 1;
  word: string;
}

const BATCH = 4;

/** Ключ распиленного слова — регистронезависимо, как в deal.ts. */
function halfKey(category: string, word: string): string {
  return `${category}::${word.toLowerCase()}`;
}

export function simulatePlayability(spec: LevelSpec): PlayabilityResult {
  /*
   * Спек без выкладки симулировать нельзя, и врать «проходим» тут нельзя тоже:
   * такие спеки приезжают из пакетов до gen-1.1, и тихий зелёный вердикт на
   * них означал бы, что гейт приёмки пропускает непроверенное. Кто оценивает
   * уровень (`core/dealShape.ts`), сюда с таким спеком просто не приходит.
   */
  if (!spec.deal || !Array.isArray(spec.deal.start) || !Array.isArray(spec.deal.queue)) {
    return {
      winnable: false, failReason: 'выкладки нет: симулировать нечего',
      movesNeeded: 0, moveLimit: spec.board.moveLimit, spareMoves: null,
      rescues: 0, perceivedDead: 0, maxDrought: 0,
      refillWaves: 0, refillCompletions: 0,
      chainRescued: false, blockersRescued: false,
    };
  }
  const fullOf = new Map<string, number>();
  for (const c of spec.categories) fullOf.set(c.key, c.words.length);

  // мета-связь: сбор дочерней категории рождает слово родителя
  const parentOf = new Map<string, string>();
  for (const c of spec.categories) {
    if (c.parentKey) parentOf.set(c.key, c.parentKey);
  }

  // распилы: слово из выкладки превращается в два пузыря-половинки
  const halves = new Map<string, number>();
  spec.halves.forEach((h, i) => halves.set(halfKey(h.home, h.word), i + 1));

  const frozen = new Map<string, number>();
  for (const b of [...spec.modifiers.frozenBubbles, ...spec.modifiers.hiddenBubbles]) {
    frozen.set(halfKey(b.category, b.word), b.layers);
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
  const toBubble = (item: QueueItem): SimBubble => ({
    category: item.category,
    words: 1,
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
  let rescues = 0;
  let perceivedDead = 0;
  let drought = 0;
  let maxDrought = 0;
  let chainRescued = false;
  let blockersRescued = false;
  let refillWaves = 0;
  let refillCompletions = 0;

  /**
   * Категории, которые ПРЯМО СЕЙЧАС собираются целиком: все четыре слова на
   * поле, ничто из них не заблокировано. Множество, а не флаг: пачка досыпки
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
      sums.set(b.category, (sums.get(b.category) ?? 0) + b.words);
    }
    const out = new Set<string>();
    for (const [cat, n] of sums) {
      if (blockedCats.has(cat)) continue;
      if (n >= (fullOf.get(cat) ?? 4)) out.add(cat);
    }
    return out;
  };

  const spawn = (n: number): void => {
    if (n <= 0 || queue.length === 0) return;
    const before = completableSet();
    for (let i = 0; i < n && queue.length > 0; i += 1) {
      field.push(toBubble(queue.shift()!));
    }
    refillWaves += 1;
    const after = completableSet();
    for (const cat of after) {
      if (!before.has(cat)) { refillCompletions += 1; break; }
    }
  };

  const canPair = (a: SimBubble, b: SimBubble): boolean => {
    if (a.blocked > 0 || b.blocked > 0) return false;
    if (chainUp && a.zone !== b.zone) return false;
    if (a.halfPair || b.halfPair) {
      return a.halfPair === b.halfPair && a.halfSide !== b.halfSide;
    }
    return a.category === b.category
      && a.words + b.words <= (fullOf.get(a.category) ?? 4);
  };

  const legalPairs = (): [number, number][] => {
    const out: [number, number][] = [];
    for (let i = 0; i < field.length; i += 1) {
      for (let j = i + 1; j < field.length; j += 1) {
        if (canPair(field[i], field[j])) out.push([i, j]);
      }
    }
    return out;
  };

  const meltOne = (): void => {
    for (const b of field) if (b.blocked > 0) b.blocked -= 1;
  };

  /** Сбор категории: бесплатно; мета превращается в слово родителя. */
  const collect = (index: number): void => {
    const cat = field[index].category;
    field.splice(index, 1);
    done += 1;
    maxDrought = Math.max(maxDrought, drought);
    drought = 0;
    if (chainUp && done >= chainNeed) chainUp = false;
    const parent = parentOf.get(cat);
    if (parent) {
      field.push({
        category: parent, words: 1, halfPair: 0, halfSide: 0, blocked: 0,
        zone: chainUp ? ((zoneFlip += 1) % 2 === 0 ? 0 : 1) : 0,
      });
      spawn(BATCH - 1);
    } else {
      spawn(BATCH);
    }
  };

  const fail = (reason: string): PlayabilityResult => ({
    winnable: false, failReason: reason,
    movesNeeded: moves, moveLimit: spec.board.moveLimit,
    spareMoves: spec.board.moveLimit === null ? null : spec.board.moveLimit - moves,
    rescues, perceivedDead, maxDrought, chainRescued, blockersRescued,
    refillWaves, refillCompletions,
  });

  // страховочный предел: ходов у любого уровня меньше тысячи на порядки
  let guard = 20000;
  while (done < totalCats && guard > 0) {
    guard -= 1;
    const pairs = legalPairs();

    if (pairs.length === 0) {
      // страховки прототипа, в его порядке: цепь → лёд → досыпка вне ритма
      if (chainUp) { chainUp = false; chainRescued = true; continue; }
      const anyBlocked = field.some((b) => b.blocked > 0);
      if (anyBlocked) {
        for (const b of field) b.blocked = 0;
        blockersRescued = true;
        continue;
      }
      if (queue.length > 0) { rescues += 1; spawn(BATCH); continue; }
      return fail('жёсткий тупик: мерджей нет и очередь пуста');
    }

    // «выглядит тупиком»: собрать нечего, ходить почти некуда
    const completing = pairs.filter(([i, j]) => field[i].halfPair === 0
      && field[i].words + field[j].words === (fullOf.get(field[i].category) ?? 4));
    if (completing.length === 0 && pairs.length <= 1) perceivedDead += 1;

    let pick: [number, number];
    if (completing.length > 0) {
      pick = completing[0];
    } else {
      const halfMerge = pairs.find(([i]) => field[i].halfPair !== 0);
      if (halfMerge) {
        pick = halfMerge;
      } else {
        // категория, у которой на поле больше всего слов, ближе всех к сбору
        const onField = new Map<string, number>();
        for (const b of field) {
          if (b.halfPair === 0) {
            onField.set(b.category, (onField.get(b.category) ?? 0) + b.words);
          }
        }
        pick = pairs.reduce((best, p) =>
          ((onField.get(field[p[0]].category) ?? 0)
            > (onField.get(field[best[0]].category) ?? 0) ? p : best), pairs[0]);
      }
    }

    const [i, j] = pick;
    const a = field[i];
    const b = field[j];
    if (a.halfPair) {
      // склейка половинок: получился обычный пузырь-слово, счётчик слов
      // категории не вырос, а ход потрачен — как в прототипе
      a.halfPair = 0; a.halfSide = 0; a.words = 1;
      field.splice(j, 1);
    } else {
      a.words += b.words;
      field.splice(j, 1);
    }
    moves += 1;
    drought += 1;
    meltOne();

    const idx = field.indexOf(a);
    if (a.halfPair === 0 && a.words >= (fullOf.get(a.category) ?? 4)) {
      collect(idx);
    }
  }

  if (guard <= 0) return fail('симуляция не сошлась: защитный предел исчерпан');

  const limit = spec.board.moveLimit;
  if (limit !== null && moves > limit) {
    return {
      ...fail(`не хватает лимита ходов: нужно ${moves}, лимит ${limit}`),
      movesNeeded: moves,
    };
  }

  return {
    winnable: true, failReason: null,
    movesNeeded: moves, moveLimit: limit,
    spareMoves: limit === null ? null : limit - moves,
    rescues, perceivedDead, maxDrought, chainRescued, blockersRescued,
    refillWaves, refillCompletions,
  };
}
