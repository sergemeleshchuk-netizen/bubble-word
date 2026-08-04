/**
 * Модификаторы для играбельного прототипа.
 *
 * Зачем отдельный слой. Сдаваемый пакет уровней (levels/packs) собран без
 * модификаторов: в референсе первых 200 уровней ни льда, ни «?»-пузырей нет
 * (TARGET_GAME_OBSERVATIONS §3), а цепи и половинки объявлены, но в выгрузке
 * ответов их не видно. Поэтому модификаторы не входят в level_spec и не трогают
 * хеш уровня: они пересобирают РАСКЛАДКУ уровня в прототипе, чтобы механику из
 * ТЗ (GDD §7) можно было потрогать руками и увидеть, во что она превращает
 * ходы и сложность.
 *
 * Пересборка детерминированная: seed = ключ модификатора + номер уровня.
 * Один и тот же уровень с одним и тем же модификатором раскладывается одинаково.
 *
 * Слоты вместо координат на пузырь. Раньше позиция считалась от индекса слова,
 * поэтому 25-й пузырь уровня уезжал за нижнюю границу поля, а слова одной
 * категории вставали в один ряд (COLS = 4 при 4 словах в категории) — пазл
 * читался по рядам. Теперь поле — это набор слотов по числу board_capacity,
 * пузырь занимает слот, освободившийся слот отдаётся досыпке.
 */
import { createRng, type Rng } from './rng.ts';
import { moveFloor, moveLimit } from './levelMath.ts';
import type { LevelSpec } from './types.ts';

export type PlayableModifier = 'none' | 'halves' | 'ice' | 'hidden' | 'chain';

export const MODIFIERS: { id: PlayableModifier; label: string; hint: string }[] = [
  { id: 'none', label: 'без модификаторов',
    hint: 'уровень как в сдаваемом пакете: только слова и мета-категории' },
  { id: 'halves', label: 'половинки',
    hint: 'несколько слов распилены на два пузыря: сначала склей слово, потом веди в категорию' },
  { id: 'ice', label: 'лёд',
    hint: 'замороженный пузырь не тащится; каждый успешный мердж на поле снимает один слой льда' },
  { id: 'hidden', label: 'скрытые «?»',
    hint: 'слово закрыто, счётчик показывает, сколько мерджей до раскрытия' },
  { id: 'chain', label: 'цепь',
    hint: 'цепь делит поле: мерджи через неё запрещены, снимается сбором категорий' },
];

/** Пузырь на поле прототипа. */
export interface PlayableBubble {
  id: number;
  kind: 'word' | 'half' | 'meta';
  /** слова внутри пузыря; для половинки — один фрагмент */
  words: string[];
  /** для половинки: к какой паре относится и какая это часть */
  pair?: { id: number; whole: string; side: 0 | 1 };
  /** слоёв льда осталось; 0 — растаял */
  ice: number;
  /** мерджей до раскрытия; 0 — открыт */
  hidden: number;
  /** ключ категории, если пузырь — схлопнутая категория */
  completedCategory?: string;
  /** индекс слота на поле; −1 у пузыря, который ещё в очереди */
  slot: number;
}

export interface PlayableSlot { x: number; y: number }

export interface PlayableChain {
  /** линия цепи в процентах высоты поля */
  y: number;
  /** сколько категорий надо собрать, чтобы цепь лопнула */
  need: number;
}

export interface PlayableSetup {
  modifier: PlayableModifier;
  slots: PlayableSlot[];
  /** порядок, в котором досыпка занимает свободные слоты */
  refillOrder: number[];
  board: PlayableBubble[];
  queue: PlayableBubble[];
  chain: PlayableChain | null;
  /** минимум мерджей с учётом склеек половинок */
  floor: number;
  /** пересчитанный лимит ходов; null — туториальный уровень без лимита */
  moveLimit: number | null;
  /** что модификатор сделал с уровнем — печатается в интерфейсе */
  notes: string[];
  /** прикидка добавки к сложности */
  difficultyDelta: number;
}

/**
 * Веса добавки к сложности.
 *
 * chain и half_pair совпадают с секцией mechanical в data/scoring.config.json.
 * ice и hidden там отсутствуют: в референсе этих механик нет, калибровать нечем,
 * поэтому веса объявленные — в интерфейсе это подписано прямым текстом.
 */
const DELTA = { chain: 0.5, halfPair: 0.4, ice: 0.45, hidden: 0.5, max: 1.5 };

/** Запас ходов за модификатор, который сам мерджей не добавляет. */
export const BLOCKER_MOVE_BONUS = 1;

const COLS = 4;

/** Сетка слотов по числу мест на поле. Ряд — не категория: слоты тасуются. */
export function slotGrid(capacity: number): PlayableSlot[] {
  const rows = Math.max(1, Math.ceil(capacity / COLS));
  const top = 7;
  const bottom = 93;
  const step = rows > 1 ? (bottom - top) / (rows - 1) : 0;
  return Array.from({ length: capacity }, (_, i) => {
    const row = Math.floor(i / COLS);
    const col = i % COLS;
    return {
      x: 14 + col * 24 + ((i * 5) % 4),
      y: top + row * step + ((i * 3) % 3),
    };
  });
}

/** Ряды слотов по возрастанию y — из них выбирается линия цепи. */
function rowLines(slots: PlayableSlot[]): number[] {
  const rows = Math.max(1, Math.ceil(slots.length / COLS));
  const lines: number[] = [];
  for (let r = 1; r < rows; r += 1) {
    const above = slots[(r - 1) * COLS]?.y ?? 0;
    const below = slots[r * COLS]?.y ?? above;
    lines.push((above + below) / 2);
  }
  return lines;
}

interface Draft {
  text: string;
  category: string;
  kind: 'word' | 'meta';
}

/**
 * Слова уровня в порядке ВЫКЛАДКИ: сначала поле, потом очередь досыпки.
 *
 * Раньше здесь был порядок спека, и первые `board_capacity` слов давали шесть
 * категорий целиком — поле из готовых четвёрок, ничего общего с тем, что видел
 * игрок в HTML-прототипе. Теперь оба прототипа исполняют одну выкладку,
 * посчитанную генератором (`core/deal.ts`), и наигровка в инструменте
 * показывает ровно тот уровень, который уедет в игру.
 *
 * Мета-слово в выкладке не участвует: оно появляется превращением четвёрки.
 */
function drafts(spec: LevelSpec): Draft[] {
  return [...spec.deal.start, ...spec.deal.queue]
    .map((b) => ({ text: b.word, category: b.category, kind: 'word' as const }));
}

/**
 * Точка распила.
 *
 * Жёсткое правило спека: фрагмент половинки не имеет права быть валидным словом
 * (SPEC §4) — иначе игрок честно потащит половинку в категорию как слово.
 * Проверяется по трём спискам: слова уровня, уже выданные фрагменты и весь
 * лексикон контентной базы (10 тысяч слов), если он передан. Полного словаря
 * английского у инструмента нет, поэтому «shr|imp» такая проверка не поймает:
 * ограничение известное, в интерфейсе оно подписано.
 */
export function splitWord(word: string, taken: Set<string>): [string, string] | null {
  if (!/^[\p{L}]{6,}$/u.test(word)) return null;
  const mid = Math.floor(word.length / 2);
  for (const at of [mid, mid - 1, mid + 1]) {
    if (at < 2 || word.length - at < 2) continue;
    const a = word.slice(0, at);
    const b = word.slice(at);
    if (taken.has(a.toLowerCase()) || taken.has(b.toLowerCase())) continue;
    return [a, b];
  }
  return null;
}

/**
 * Сколько слов пилить. Половинки — акцент, а не фон: «немного слов, только для
 * части категорий, не больше одного распила в категории».
 */
export function halfBudget(categoryCount: number): number {
  return Math.max(1, Math.min(3, Math.round(categoryCount / 3)));
}

/** Кандидаты на блокировку: из разных категорий и обязательно на старте поля. */
function pickBlockers(
  list: Draft[], capacity: number, count: number, rng: Rng,
): number[] {
  const eligible: number[] = [];
  for (let i = 0; i < Math.min(list.length, capacity); i += 1) {
    if (list[i].kind === 'word') eligible.push(i);
  }
  const picked: number[] = [];
  const usedCategories = new Set<string>();
  for (const i of rng.shuffle(eligible)) {
    if (picked.length >= count) break;
    if (usedCategories.has(list[i].category)) continue;
    usedCategories.add(list[i].category);
    picked.push(i);
  }
  return picked.sort((a, b) => a - b);
}

export function buildSetup(
  spec: LevelSpec, modifier: PlayableModifier, lexicon?: ReadonlySet<string>,
): PlayableSetup {
  const rng = createRng(`playable::${modifier}::${spec.levelId}`);
  const capacity = spec.board.boardCapacity;
  const slots = slotGrid(capacity);
  const notes: string[] = [];
  let delta = 0;

  const list = drafts(spec);
  const bubbles: PlayableBubble[] = [];
  let id = 0;
  const blank = { ice: 0, hidden: 0, slot: -1 };

  // ------------------------------------------------------------------ половинки
  let halfPairs = 0;
  if (modifier === 'halves') {
    const taken = new Set(list.map((d) => d.text.toLowerCase()));
    for (const known of lexicon ?? []) taken.add(known);
    const budget = halfBudget(spec.categories.length);
    const usedCategories = new Set<string>();
    const splits = new Map<number, [string, string]>();
    // пилим только то, что видно на старте: половинка в конце очереди
    // не даёт «ага-момента», ради которого механика и вводится
    for (const i of rng.shuffle(
      list.map((_, k) => k).filter((k) => k < Math.min(list.length, capacity - budget)),
    )) {
      if (splits.size >= budget) break;
      if (usedCategories.has(list[i].category)) continue;
      const parts = splitWord(list[i].text, taken);
      if (!parts) continue;
      taken.add(parts[0].toLowerCase());
      taken.add(parts[1].toLowerCase());
      usedCategories.add(list[i].category);
      splits.set(i, parts);
    }
    halfPairs = splits.size;
    list.forEach((d, i) => {
      const parts = splits.get(i);
      if (!parts) {
        bubbles.push({ ...blank, id: (id += 1), kind: d.kind, words: [d.text] });
        return;
      }
      const pairId = id + 1;
      parts.forEach((fragment, side) => {
        bubbles.push({
          ...blank, id: (id += 1), kind: 'half', words: [fragment],
          pair: { id: pairId, whole: d.text, side: side as 0 | 1 },
        });
      });
    });
    if (halfPairs > 0) {
      notes.push(`распилено слов: ${halfPairs} (не больше одного в категории, `
        + `затронуто категорий: ${usedCategories.size} из ${spec.categories.length})`);
      notes.push(lexicon
        ? `фрагменты сверены с лексиконом базы (${lexicon.size} слов): `
          + 'ни один не является самостоятельным словом базы'
        : 'фрагменты сверены только со словами уровня: лексикон не передан');
      notes.push('склейка половинок тратит ход — лимит вырос на число распилов');
      delta = Math.min(DELTA.max, DELTA.halfPair * halfPairs);
    } else {
      notes.push('распилить нечего: на уровне нет слов от 6 букв, чьи половинки '
        + 'не совпадают со словами уровня и контентной базы');
    }
  } else {
    for (const d of list) {
      bubbles.push({ ...blank, id: (id += 1), kind: d.kind, words: [d.text] });
    }
  }

  // ------------------------------------------------------- лёд и скрытые слова
  if (modifier === 'ice' || modifier === 'hidden') {
    const count = Math.min(2, Math.max(1, Math.floor(spec.categories.length / 3)));
    const indices = pickBlockers(list, capacity, count, rng);
    indices.forEach((i, k) => {
      const layers = 2 + (k % 2);
      const target = bubbles[i];
      if (!target) return;
      if (modifier === 'ice') target.ice = layers;
      else target.hidden = layers;
    });
    const word = modifier === 'ice' ? 'заморожено' : 'закрыто';
    notes.push(`${word} пузырей: ${indices.length}, по одному на категорию, `
      + 'счётчик 2-3 мерджа');
    notes.push(modifier === 'ice'
      ? 'лёд тает от любого успешного мерджа на поле, ошибка слой не снимает'
      : 'счётчик «?» уменьшается от любого успешного мерджа на поле');
    delta = Math.min(DELTA.max,
      (modifier === 'ice' ? DELTA.ice : DELTA.hidden) * indices.length);
  }

  // --------------------------------------------------------------------- слоты
  const boardCount = Math.min(bubbles.length, capacity);
  const board = bubbles.slice(0, boardCount);
  const queue = bubbles.slice(boardCount);
  // СОСТАВ поля берётся из выкладки уровня как есть (там же и гарантия, что на
  // старте видна одна полная четвёрка), а вот КУДА встанет пузырь — пока
  // тасуется здесь: координаты в выкладку ещё не входят, это следующий шаг
  const shuffled = rng.shuffle(slots.map((_, i) => i));
  board.forEach((b, i) => { b.slot = shuffled[i]; });
  const refillOrder = rng.shuffle(slots.map((_, i) => i));

  // ---------------------------------------------------------------------- цепь
  let chain: PlayableChain | null = null;
  if (modifier === 'chain') {
    const lines = rowLines(slots);
    // Цепь должна отделять именно нижнюю часть поля, поэтому линия ставится там,
    // где под ней оказывается около трети слотов. Раньше линия выбиралась по
    // числу категорий, целиком лежащих по одну сторону, — и всегда уезжала к
    // самому краю: с 24 слотами и тасованной раскладкой у середины таких
    // категорий почти не бывает. Проходимость держится не выбором линии, а тем,
    // что досыпка подносит слова в обе зоны, плюс страховкой прототипа: если
    // легального мерджа не осталось, цепь снимается сама.
    const belowShare = (y: number) => slots.filter((s) => s.y > y).length / slots.length;
    const best = lines
      .map((y) => ({ y, share: belowShare(y) }))
      .sort((a, b) => Math.abs(a.share - 1 / 3) - Math.abs(b.share - 1 / 3))[0];
    if (best) {
      // сколько категорий собирается прямо сейчас, не пересекая цепь: это не
      // условие постановки, а честная цифра о том, насколько цепь стесняет старт
      const plain = spec.categories.filter((c) => c.words.every((w) => w.kind !== 'meta'));
      const intact = plain.filter((c) => {
        const sides = board
          .filter((b) => b.words.some((w) => c.words.some((cw) => cw.text === w)))
          .map((b) => slots[b.slot].y > best.y);
        return sides.length === spec.board.wordsPerCategory && new Set(sides).size === 1;
      }).length;
      const need = Math.min(2, Math.max(1, spec.categories.length - 1));
      chain = { y: best.y, need };
      notes.push(`цепь на ${Math.round(best.y)}% высоты поля: под ней `
        + `${Math.round(best.share * 100)}% слотов, мердж между зонами запрещён, `
        + 'пока цепь висит');
      notes.push(`счётчик цепи: ${need} собранные категории; на старте целиком `
        + `по одну сторону лежит категорий: ${intact}, остальные придётся `
        + 'добирать досыпкой');
      notes.push('если легального мерджа не осталось, прототип снимает цепь сам — '
        + 'иначе раскладка могла бы запереть игрока');
      delta = DELTA.chain;
    } else {
      notes.push('цепь не поставлена: поле в один ряд, делить нечего');
    }
  }

  // ---------------------------------------------------------------- лимит ходов
  const floor = moveFloor(spec.categories.length, halfPairs, spec.board.wordsPerCategory);
  let limit: number | null = null;
  if (spec.board.moveLimit !== null) {
    const k = spec.board.moveLimitK ?? 1.3;
    const blocker = modifier === 'ice' || modifier === 'hidden' || modifier === 'chain';
    limit = moveLimit(floor, k) + (blocker ? BLOCKER_MOVE_BONUS : 0);
    if (limit !== spec.board.moveLimit) {
      notes.push(`лимит ходов пересчитан: ${spec.board.moveLimit} → ${limit} `
        + `(минимум мерджей ${floor}, K = ${k}`
        + `${blocker ? `, +${BLOCKER_MOVE_BONUS} за блокирующий модификатор` : ''})`);
    }
  }

  if (modifier !== 'none' && delta > 0) {
    notes.push(`прикидка добавки к сложности: +${delta.toFixed(2)} `
      + '(цепь и половинки — по весам scoring.config, лёд и «?» — объявленные веса, '
      + 'замером не калиброваны)');
  }

  return {
    modifier, slots, refillOrder, board, queue, chain,
    floor, moveLimit: limit, notes, difficultyDelta: delta,
  };
}
