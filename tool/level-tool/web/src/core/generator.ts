/**
 * Детерминированный генератор уровня и блока.
 *
 * Главное свойство: один и тот же снимок базы + конфиг + seed дают один и тот же
 * `level_spec_hash`. Модель здесь не участвует — она обогатила базу заранее.
 * Если поставить её в горячий путь, кривой сложности нельзя управлять,
 * а брак нельзя воспроизвести.
 *
 * Порядок шагов (план §9.3):
 *   1. пул категорий-кандидатов по фильтрам
 *   2. пары для мета-связей
 *   3. выбор набора категорий
 *   4. назначение по 4 слова — задача точного покрытия, MRV + откат
 *   5. мета-лес
 *   6. ловушки
 *   7. модификаторы
 *   8. счёт решений, валидация, оценки
 *   9. упорядоченное ослабление, если не сошлось
 */
import type {
  BlockConfig,
  DecadeGates, Chain, GenerationAttempt, GenerationFailure, LevelCategory,
  LevelPlan, LevelSpec, LevelWord, Trap,
} from './types.ts';
import { STATUS } from './types.ts';
import { ContentIndex } from './snapshot.ts';
import { createRng, type Rng } from './rng.ts';
import { BOARD_CAPACITY, moveFloor, moveLimit, startBubbles } from './levelMath.ts';

export const GENERATOR_VERSION = 'gen-1.0';

/** Что уже использовано в пакете — для правил свежести. */
export interface PackHistory {
  /** нормализованное слово → последний уровень, где оно встречалось */
  wordLastLevel: Map<string, number>;
  /** ключ категории → последний уровень */
  categoryLastLevel: Map<string, number>;
  /** четвёрки слов референса, чтобы не выдать копию: ключ = отсортированные слова */
  referenceQuadruples?: Set<string>;
  /**
   * Нормализованное слово → ключ категории, где оно лежало в прошлый раз.
   * Нужно, чтобы отличить повтор слова в ТОЙ ЖЕ категории (это брак) от повтора
   * в ДРУГОЙ категории (это рычаг сложности: 2.9 слова на уровень в L1-10
   * против 28 в L171-180 референса).
   */
  wordCategory?: Map<string, string>;
}

export function emptyPackHistory(): PackHistory {
  return { wordLastLevel: new Map(), categoryLastLevel: new Map(), wordCategory: new Map() };
}

export interface LevelGenerationOutcome {
  spec?: LevelSpec;
  traps: Trap[];
  attempts: GenerationAttempt[];
  failure?: GenerationFailure;
  relaxationsUsed: string[];
}

/** Ослабления в порядке предпочтения. Hard-инварианты сюда не входят никогда. */
const RELAXATION_ORDER = [
  'точное число редких слов → диапазон',
  'тематическая узость → соседние сферы',
  'меньше ловушек',
  'меньше мета-связей',
  'меньше глубины мета',
  'другой набор категорий',
] as const;

type Relaxation = typeof RELAXATION_ORDER[number];

interface Constraints {
  categoryCount: number;
  /**
   * Гейты формы слова из профиля декады. Фильтруют пул НА ВХОДЕ, а не отбраковывают
   * готовый уровень: когда гейты стояли только в валидаторе, генератор 24 попытки
   * подряд собирал уровень из многословных и длинных слов и каждый раз получал
   * отказ WORD_FORM_GATE, хотя годные слова в базе были.
   */
  gates: DecadeGates | null;
  /** окна свежести из конфига, а не захардкоженные числа */
  wordWindow: number;
  categoryWindow: number;
  metaCount: number;
  metaDepthTarget: number;
  rareTarget: number;
  rareTolerance: number;
  trapTarget: number;
  themesAllowed: Set<string> | null;
  themesExcluded: Set<string>;
  enforceFreshness: boolean;
}

// --------------------------------------------------------------------------- //
// вспомогательное
// --------------------------------------------------------------------------- //

/**
 * Слова-двойники внутри одной категории: `star` и `stars`, `bird` и `birds`.
 * Формально это разные слова, но на поле рядом они читаются как ошибка данных.
 */
function isNearDuplicate(a: string, b: string): boolean {
  if (a === b) return true;
  const [short, long] = a.length <= b.length ? [a, b] : [b, a];
  if (long === `${short}s` || long === `${short}es`) return true;
  if (short.endsWith('y') && long === `${short.slice(0, -1)}ies`) return true;
  return false;
}

function quadrupleKey(words: string[]): string {
  return words.map((w) => w.toLowerCase()).sort().join('|');
}

// --------------------------------------------------------------------------- //
// шаг 1: пул категорий
// --------------------------------------------------------------------------- //

interface PoolEntry {
  category: number;
  key: string;
  theme: string;
  approved: number[];
  /** сколько approved-слов частотные — потенциал quick-win */
  frequentCount: number;
  /** сколько approved-слов редкие — потенциал редкости */
  rareCount: number;
  canQuickwin: boolean;
  /**
   * Узнаваемость категории: медиана частотности четырёх самых частотных годных
   * слов, то есть «насколько понятной эта категория может быть, если брать из неё
   * лучшее». Нужна для отбора категорий под целевую медиану декады: в базе
   * 230 категорий способны дать медиану 4.35+, но без этого поля генератор
   * выбирал их не чаще любых других и блок 1-10 упирался в медиану 3.81.
   */
  recognizability: number;
}

/**
 * Слово проходит форму декады: число токенов, длина, порог для имён собственных.
 * Без гейтов пропускает всё — так ведёт себя пресет блока 201-210.
 */
export function wordFitsGates(index: ContentIndex, word: number, gates: DecadeGates | null): boolean {
  if (!gates) return true;
  const w = index.words[word];
  if (w.tok > gates.maxTokens) return false;
  if (w.t.replace(/\s/g, '').length > gates.maxWordLen) return false;
  if (w.p === 1 && (w.z === null || w.z < gates.minProperNounZipf)) return false;
  return true;
}

function buildPool(
  index: ContentIndex, plan: LevelPlan, c: Constraints, history: PackHistory,
  excluded?: Set<number>,
): PoolEntry[] {
  const pool: PoolEntry[] = [];
  for (let cat = 0; cat < index.categories.length; cat += 1) {
    const meta = index.categories[cat];
    if (excluded?.has(cat)) continue;
    if (c.themesExcluded.has(meta.th)) continue;
    if (c.themesAllowed && !c.themesAllowed.has(meta.th)) continue;

    if (c.enforceFreshness) {
      const last = history.categoryLastLevel.get(meta.k);
      if (last !== undefined && plan.levelId - last <= c.categoryWindow) continue;
    }

    const approved = index.categoryMemberships(cat, STATUS.approved)
      .map((m) => m.word)
      .filter((w) => wordFitsGates(index, w, c.gates));
    if (approved.length < 4) continue;

    const frequentCount = approved.filter((w) => index.isQuickwinWord(w)).length;
    const rareCount = approved.filter((w) => {
      const z = index.zipf(w);
      return z !== null && z < 3.0;
    }).length;

    const top4 = approved
      .map((w) => index.zipf(w))
      .filter((z): z is number => z !== null)
      .sort((a, b) => b - a)
      .slice(0, 4);
    const recognizability = top4.length === 4 ? (top4[1] + top4[2]) / 2 : 0;

    pool.push({
      category: cat,
      key: meta.k,
      theme: meta.th,
      approved,
      frequentCount,
      rareCount,
      canQuickwin: frequentCount >= 4,
      recognizability,
    });
  }
  return pool;
}

// --------------------------------------------------------------------------- //
// шаг 2-3: мета-цепочки и выбор категорий
// --------------------------------------------------------------------------- //

interface MetaEdge {
  child: number;
  parent: number;
  /** слово-имя ребёнка, которое ляжет в родителя */
  word: number;
}

/**
 * Строит мета-лес нужной глубины из доступных пар.
 *
 * Инварианты: у ребёнка максимум один родитель, циклов нет, связность НЕ требуется
 * (в референсе мета-граф — лес из в среднем 2.12 компонент, SPEC_AUDIT §2).
 */
/** Все возможные мета-рёбра внутри набора категорий. */
export function possibleMetaEdges(
  index: ContentIndex, categories: Iterable<number>, gates: DecadeGates | null = null,
): MetaEdge[] {
  const inSet = new Set(categories);
  const edges: MetaEdge[] = [];
  for (const cat of inSet) {
    const capable = index.metaCapable(cat);
    if (!capable) continue;
    // мета-слово — это ИМЯ категории, и на поле оно такой же пузырь, как остальные:
    // «school subjects» на уровне 1-10 нарушает форму декады ровно так же, как
    // обычное двусловное слово. Без этого фильтра гейты ловили мета-слова
    // уже в валидаторе, и уровень уходил в отказ на 24-й попытке
    if (!wordFitsGates(index, capable.word, gates)) continue;
    for (const host of capable.hosts) {
      if (!inSet.has(host) || host === cat) continue;
      edges.push({ child: cat, parent: host, word: capable.word });
    }
  }
  return edges;
}

/**
 * Ищет цепочку заданной глубины по всей базе, без учёта истории пакета.
 *
 * Нужно потому, что глубокие цепочки — дефицитный ресурс: правила свежести
 * съедают их участников на ранних уровнях блока, и уровню, которому глубина
 * нужна по плану, её уже не хватает. Поэтому блок сначала резервирует цепочку,
 * а потом генерирует уровни.
 */
export function planDeepChain(
  index: ContentIndex, depth: number, seed: string, wordsPerCategory = 4,
  gates: DecadeGates | null = null,
): MetaEdge[] | null {
  if (depth < 2) return null;
  const usable: number[] = [];
  for (let cat = 0; cat < index.categories.length; cat += 1) {
    if (index.approvedCount(cat) >= wordsPerCategory) usable.push(cat);
  }
  const edges = possibleMetaEdges(index, usable, gates);
  const outgoing = new Map<number, MetaEdge[]>();
  const rng = createRng(`${seed}|deep-chain|${depth}`);
  for (const edge of rng.shuffle(edges)) {
    outgoing.set(edge.child, [...(outgoing.get(edge.child) ?? []), edge]);
  }
  const walk = (node: number, path: MetaEdge[], seen: Set<number>): MetaEdge[] | null => {
    if (path.length === depth) return path;
    for (const edge of outgoing.get(node) ?? []) {
      if (seen.has(edge.parent)) continue;
      seen.add(edge.parent);
      const found = walk(edge.parent, [...path, edge], seen);
      if (found) return found;
      seen.delete(edge.parent);
    }
    return null;
  };
  for (const start of rng.shuffle(Array.from(outgoing.keys()))) {
    const found = walk(start, [], new Set([start]));
    if (found) return found;
  }
  return null;
}

function buildMetaForest(
  index: ContentIndex, pool: PoolEntry[], c: Constraints, rng: Rng,
  forcedChain?: MetaEdge[],
  isWordFresh: (word: number) => boolean = () => true,
): { edges: MetaEdge[]; categories: Set<number> } {
  if (c.metaCount === 0) return { edges: [], categories: new Set() };

  const inPool = new Set(pool.map((p) => p.category));
  /**
   * Мета-слово тоже подчиняется свежести. Раньше не подчинялось, и получалось
   * так: слово `desserts` стоит на уровне 201 обычным пузырём, а на 202 приходит
   * мета-пузырём — формально это повтор слова внутри блока, который правила
   * свежести обязаны запрещать. Принудительные слова обходили проверку, потому
   * что ставились до перебора.
   */
  const allEdges: MetaEdge[] = possibleMetaEdges(index, inPool, c.gates)
    .filter((edge) => isWordFresh(edge.word));
  if (allEdges.length === 0 && !forcedChain?.length) {
    return { edges: [], categories: new Set() };
  }

  const shuffled = rng.shuffle(allEdges);
  const edges: MetaEdge[] = [];
  const parentOf = new Map<number, number>();
  const involved = new Set<number>();

  // рёбра, выходящие из категории: нужны, чтобы искать цепочки нужной глубины
  const outgoing = new Map<number, MetaEdge[]>();
  for (const edge of shuffled) {
    outgoing.set(edge.child, [...(outgoing.get(edge.child) ?? []), edge]);
  }

  const depthOf = (node: number, guard = 0): number => {
    if (guard > 8) return 99;
    const parent = parentOf.get(node);
    return parent === undefined ? 0 : 1 + depthOf(parent, guard + 1);
  };
  const chainDepth = (): number => {
    let deepest = 0;
    for (const node of parentOf.keys()) deepest = Math.max(deepest, depthOf(node));
    return deepest;
  };

  // сначала пытаемся набрать требуемую глубину: цепочка ребёнок → родитель → дед
  const wantDepth = Math.max(1, c.metaDepthTarget);
  const tryAdd = (edge: MetaEdge): boolean => {
    if (parentOf.has(edge.child)) return false;              // не больше одного родителя
    // цикл: родитель уже висит под ребёнком
    let cursor: number | undefined = edge.parent;
    for (let i = 0; cursor !== undefined && i < 10; i += 1) {
      if (cursor === edge.child) return false;
      cursor = parentOf.get(cursor);
    }
    parentOf.set(edge.child, edge.parent);
    if (chainDepth() > wantDepth) {                          // глубже, чем просили
      parentOf.delete(edge.child);
      return false;
    }
    edges.push(edge);
    involved.add(edge.child);
    involved.add(edge.parent);
    return true;
  };

  /**
   * Проход 1 — сначала строим САМУЮ ГЛУБОКУЮ цепочку, и только потом добираем
   * количество. Если делать наоборот, бюджет мета-связей расходуется на плоские
   * пары, и глубина 2-3 не появляется никогда: именно так выглядел первый
   * работающий прогон — 10 уровней из 10 с глубиной 1.
   *
   * Цепочка глубины d — это путь из d рёбер: c0 → c1 → … → cd.
   */
  const findChain = (length: number): MetaEdge[] | null => {
    if (length <= 1) return null;
    const walk = (node: number, path: MetaEdge[], seen: Set<number>): MetaEdge[] | null => {
      if (path.length === length) return path;
      for (const edge of outgoing.get(node) ?? []) {
        if (seen.has(edge.parent)) continue;
        seen.add(edge.parent);
        const found = walk(edge.parent, [...path, edge], seen);
        if (found) return found;
        seen.delete(edge.parent);
      }
      return null;
    };
    for (const start of rng.shuffle(Array.from(outgoing.keys()))) {
      const found = walk(start, [], new Set([start]));
      if (found) return found;
    }
    return null;
  };

  // зарезервированная цепочка идёт первой: под неё уровень и планировался
  if (forcedChain?.length) {
    for (const edge of forcedChain) tryAdd(edge);
  }

  if (chainDepth() < wantDepth && wantDepth >= 2 && c.metaCount >= wantDepth) {
    for (let target = wantDepth; target >= 2; target -= 1) {
      const chain = findChain(target);
      if (!chain) continue;
      for (const edge of chain) tryAdd(edge);
      if (chainDepth() >= target) break;
    }
  }

  // проход 2: добираем количество любыми доступными рёбрами
  for (const edge of shuffled) {
    if (edges.length >= c.metaCount) break;
    tryAdd(edge);
  }

  return { edges, categories: involved };
}

/** Выбор набора категорий: мета-каркас, quick-win, затем добор с учётом тем и редкости. */
function selectCategories(
  index: ContentIndex, pool: PoolEntry[], c: Constraints, rng: Rng,
  forcedChain?: MetaEdge[],
  isWordFresh: (word: number) => boolean = () => true,
): { selected: PoolEntry[]; edges: MetaEdge[] } | null {
  if (pool.length < c.categoryCount) return null;

  const byIndex = new Map(pool.map((p) => [p.category, p]));
  const { edges } = buildMetaForest(index, pool, c, rng,
    forcedChain?.filter((edge) => isWordFresh(edge.word)), isWordFresh);

  const selected: PoolEntry[] = [];
  const taken = new Set<number>();

  /**
   * Неразделимые пары отсекаются ЗДЕСЬ, при отборе категорий.
   *
   * Раньше это была только soft-проверка валидатора: пары вида
   * CONSTELLATIONS + ZODIAC SIGNS, DISEASES + ILLNESSES, TOYS + TOY CHEST
   * доезжали до готового уровня, счётчик решений находил две раскладки, и попытка
   * отклонялась — при том что какие именно четыре слова выбрать, уже не важно:
   * проблема в пулах, а не в выборке.
   *
   * Чего этот фильтр НЕ ловит: двусмысленность, собранную циклом обменов через
   * три и более категории. Там попарного пересечения пулов может не быть вовсе
   * (у `moons` и `stargazing` оно ровно ноль), и такие случаи остаются на
   * счётчике решений.
   *
   * Порог 0.30 по Жаккару: пересечение пулов approved-слов. Считаем по пулам,
   * а не по выбранным четвёркам, потому что проблема именно в пулах.
   *
   * Работает только на калиброванных блоках (там, где заданы гейты декады).
   * Пресет 201-210 обязан воспроизводить сдаваемый пакет байт-в-байт, а этот
   * фильтр меняет выбор категорий и, значит, pack hash. Тот пакет уже прошёл
   * слепого решателя целиком — переcобирать его под новое правило нельзя.
   */
  /**
   * Пул считаем по статусу alternative, а не approved.
   *
   * Двусмысленность создают именно alternative-связи: слово живёт в одной
   * категории как дом, но в соседней читается правдоподобно. Счётчик решений
   * смотрит ровно на этот статус, значит и фильтр пар обязан смотреть на него же,
   * иначе он мерит не то, что потом ломает уровень.
   */
  const plausibleSets = new Map<number, Set<number>>();
  const approvedSet = (entry: PoolEntry): Set<number> => {
    let set = plausibleSets.get(entry.category);
    if (!set) {
      set = new Set(index.categoryMemberships(entry.category, STATUS.alternative)
        .map((m) => m.word));
      plausibleSets.set(entry.category, set);
    }
    return set;
  };
  const UNSEPARABLE_JACCARD = 0.30;
  const separableFromSelected = (entry: PoolEntry): boolean => {
    if (!c.gates) return true;
    const a = approvedSet(entry);
    for (const other of selected) {
      const b = approvedSet(other);
      let shared = 0;
      for (const w of a) if (b.has(w)) shared += 1;
      const union = a.size + b.size - shared;
      if (union > 0 && shared / union >= UNSEPARABLE_JACCARD) return false;
    }
    return true;
  };

  const add = (entry: PoolEntry | undefined): void => {
    if (!entry || taken.has(entry.category) || selected.length >= c.categoryCount) return;
    if (!separableFromSelected(entry)) return;
    taken.add(entry.category);
    selected.push(entry);
  };

  // мета-каркас идёт первым: без него нужной структуры не получить
  const usedEdges: MetaEdge[] = [];
  for (const edge of edges) {
    if (selected.length + 2 > c.categoryCount) break;
    add(byIndex.get(edge.child));
    add(byIndex.get(edge.parent));
    if (taken.has(edge.child) && taken.has(edge.parent)) usedEdges.push(edge);
  }

  // quick-win: инвариант открытой двери, нарушать нельзя
  const quickwinCandidates = rng.shuffle(
    pool.filter((p) => p.canQuickwin && !taken.has(p.category)));
  add(quickwinCandidates[0]);

  // добор: разнообразие тем и достаточный запас редких слов
  const themeUsage = new Map<string, number>();
  for (const entry of selected) {
    themeUsage.set(entry.theme, (themeUsage.get(entry.theme) ?? 0) + 1);
  }
  const rest = rng.shuffle(pool.filter((p) => !taken.has(p.category)));
  const scored = rest
    .map((entry) => {
      const themePenalty = (themeUsage.get(entry.theme) ?? 0) * 0.35;
      const rareBonus = c.rareTarget > 0 ? Math.min(entry.rareCount, 3) * 0.12 : 0;
      const depthBonus = Math.min(entry.approved.length - 4, 6) * 0.05;
      // категории под целевую медиану декады: чем ближе потолок узнаваемости
      // категории к цели сверху, тем она ценнее. Вес 0.9 сознательно крупный —
      // это главная ось сложности первых 120 уровней референса.
      // Вес 1.3 подобран перебором: 0.9 давало медиану блока 4.16 при цели 4.35,
      // 1.3 — 4.22 (в допуске), дальше рост упирается в содержимое базы
      const fitBonus = c.gates
        ? 1.3 * Math.max(0, 1 - Math.max(0, c.gates.zipfMedianTarget - entry.recognizability) / 1.2)
        : 0;
      return {
        entry,
        score: rareBonus + depthBonus + fitBonus - themePenalty
          + rng.stableWeight(entry.key) * 0.3,
      };
    })
    .sort((a, b) => b.score - a.score);

  for (const { entry } of scored) {
    if (selected.length >= c.categoryCount) break;
    add(entry);
    themeUsage.set(entry.theme, (themeUsage.get(entry.theme) ?? 0) + 1);
  }

  if (selected.length < c.categoryCount) return null;
  if (!selected.some((p) => p.canQuickwin)) return null;

  const selectedSet = new Set(selected.map((p) => p.category));
  return {
    selected,
    edges: usedEdges.filter((e) => selectedSet.has(e.child) && selectedSet.has(e.parent)),
  };
}

// --------------------------------------------------------------------------- //
// шаг 4: назначение слов — точное покрытие
// --------------------------------------------------------------------------- //

interface AssignmentResult {
  /** индекс категории → выбранные слова (индексы) */
  words: Map<number, number[]>;
  unrecognizableUsed: number;
  rareUsed: number;
}

function assignWords(
  index: ContentIndex,
  selected: PoolEntry[],
  edges: MetaEdge[],
  c: Constraints,
  history: PackHistory,
  plan: LevelPlan,
  rng: Rng,
  wordsPerCategory: number,
  isWordFresh: (word: number) => boolean,
): AssignmentResult | null {
  const selectedSet = new Set(selected.map((p) => p.category));
  // слова, которые являются именами выбранных категорий: их нельзя ставить
  // случайно, иначе возникнет незапланированная мета-связь
  const labelWords = new Map<number, number>();   // слово → категория, чьё это имя
  for (const cat of selectedSet) {
    const capable = index.metaCapable(cat);
    if (capable) labelWords.set(capable.word, cat);
  }
  const plannedMetaWord = new Map<number, MetaEdge>();  // слово → ребро
  for (const edge of edges) plannedMetaWord.set(edge.word, edge);

  const forced = new Map<number, number[]>();     // категория → обязательные слова
  for (const edge of edges) {
    const list = forced.get(edge.parent) ?? [];
    list.push(edge.word);
    forced.set(edge.parent, list);
  }

  // бюджет неузнаваемых слов: не более 10% пузырей уровня
  const totalSlots = selected.length * wordsPerCategory;
  const unrecognizableBudget = Math.floor(totalSlots * 0.1);

  // ровно одна категория объявляется quick-win и держит инвариант
  const quickwinCat = selected.find((p) => p.canQuickwin
    && !forced.has(p.category)
    && !edges.some((e) => e.child === p.category))?.category
    ?? selected.find((p) => p.canQuickwin)?.category;

  const used = new Set<number>();                 // занятые слова уровня
  const assignment = new Map<number, number[]>();
  let unrecognizableUsed = 0;
  let rareUsed = 0;

  const candidatesFor = (cat: number): number[] => {
    const chosen = assignment.get(cat) ?? [];
    const chosenNorms = chosen.map((w) => index.words[w].n);
    const isQuickwin = cat === quickwinCat;
    const catLabelNorm = index.categories[cat].l.toLowerCase();

    return index.categoryMemberships(cat, STATUS.approved)
      .map((m) => m.word)
      .filter((w) => {
        if (used.has(w)) return false;
        // тот же фильтр формы, что в buildPool: список кандидатов собирается
        // заново из индекса, поэтому без него сюда возвращались отсеянные слова
        if (!wordFitsGates(index, w, c.gates)) return false;
        const word = index.words[w];
        if (word.n === catLabelNorm) return false;               // слово = имя своей категории
        if (chosenNorms.some((n) => isNearDuplicate(n, word.n))) return false;

        // слово-имя другой выбранной категории допустимо только как плановая мета
        const labelOf = labelWords.get(w);
        if (labelOf !== undefined) {
          const edge = plannedMetaWord.get(w);
          if (!edge || edge.parent !== cat) return false;
        }

        if (isQuickwin && !index.isQuickwinWord(w)) return false;
        if (isQuickwin && plannedMetaWord.has(w)) return false;

        if (!index.isRecognizable(w) && unrecognizableUsed >= unrecognizableBudget) return false;

        if (c.enforceFreshness && !isWordFresh(w)) return false;
        return true;
      });
  };

  const orderCandidates = (cat: number, candidates: number[]): number[] => {
    const rareNeeded = c.rareTarget - rareUsed;
    const isQuickwin = cat === quickwinCat;
    return candidates
      .map((w) => {
        const z = index.zipf(w);
        const isRare = z !== null && z < 3.0;
        let score = rng.stableWeight(`${cat}:${w}`) * 0.25;
        if (!isQuickwin && rareNeeded > 0 && isRare) score += 0.6;
        if (rareNeeded <= 0 && isRare) score -= 0.5;
        /**
         * Предпочтение по узнаваемости.
         *
         * Без гейтов декады это слабый тай-брейкер «при прочих равных — понятнее»
         * (вес 0.02). С гейтами узнаваемость становится главной осью: у декады
         * есть целевая медиана zipf, и слово тем ценнее, чем ближе оно к ней
         * сверху. Вес 0.9 подобран так, чтобы обгонять бонус за новизну (0.15),
         * но не перебивать добор редких слов (0.6): 1-2 редких слова на уровень —
         * тоже требование декады, а не случайность.
         */
        if (z !== null) {
          if (c.gates) {
            const target = c.gates.zipfMedianTarget;
            score += 0.9 * Math.max(0, 1 - Math.abs(z - target) / 1.5);
          } else {
            score += Math.min(z, 6) * 0.02;       // при прочих равных — понятнее
          }
        }
        const last = history.wordLastLevel.get(index.words[w].n);
        if (last === undefined) score += 0.15;                   // новое для пакета слово
        return { w, score };
      })
      .sort((a, b) => b.score - a.score)
      .map((x) => x.w);
  };

  const cats = selected.map((p) => p.category);
  let nodes = 0;
  const NODE_LIMIT = 60000;

  const solve = (): boolean => {
    nodes += 1;
    if (nodes > NODE_LIMIT) return false;

    // MRV: категория с наименьшим числом доступных вариантов
    let target = -1;
    let best: number[] = [];
    for (const cat of cats) {
      const have = (assignment.get(cat) ?? []).length;
      if (have >= wordsPerCategory) continue;
      const options = candidatesFor(cat);
      const need = wordsPerCategory - have;
      if (options.length < need) return false;                   // forward checking
      if (target === -1 || options.length < best.length) {
        target = cat;
        best = options;
      }
    }
    if (target === -1) return true;                              // всё заполнено

    for (const word of orderCandidates(target, best)) {
      const list = assignment.get(target) ?? [];
      list.push(word);
      assignment.set(target, list);
      used.add(word);
      const wasUnrecognizable = !index.isRecognizable(word);
      const z = index.zipf(word);
      const wasRare = z !== null && z < 3.0;
      if (wasUnrecognizable) unrecognizableUsed += 1;
      if (wasRare) rareUsed += 1;

      if (solve()) return true;

      list.pop();
      if (list.length === 0) assignment.delete(target); else assignment.set(target, list);
      used.delete(word);
      if (wasUnrecognizable) unrecognizableUsed -= 1;
      if (wasRare) rareUsed -= 1;
    }
    return false;
  };

  // обязательные мета-слова ставим до перебора
  for (const [cat, words] of forced) {
    for (const word of words) {
      if (used.has(word)) return null;
      const list = assignment.get(cat) ?? [];
      if (list.length >= wordsPerCategory) return null;
      list.push(word);
      assignment.set(cat, list);
      used.add(word);
    }
  }

  if (!solve()) return null;
  return { words: assignment, unrecognizableUsed, rareUsed };
}

// --------------------------------------------------------------------------- //
// шаг 6: ловушки
// --------------------------------------------------------------------------- //

/**
 * Ловушка — не повтор слова в двух категориях, а слово с ОДНИМ домом при наличии
 * на поле второй правдоподобной категории. Именно так они работают в целевой игре:
 * ORANGE лежит в одной категории, но на поле есть и фрукты, и цвета
 * (TARGET_GAME_OBSERVATIONS §4, SPEC_AUDIT §16).
 */
function findTraps(
  index: ContentIndex, assignment: Map<number, number[]>, edges: MetaEdge[],
): Trap[] {
  const selected = new Set(assignment.keys());
  const homeOf = new Map<number, number>();
  for (const [cat, words] of assignment) for (const w of words) homeOf.set(w, cat);
  const metaWords = new Set(edges.map((e) => e.word));

  const traps: Trap[] = [];
  for (const [word, home] of homeOf) {
    if (metaWords.has(word)) continue;                  // мета-пузырь — не ловушка
    const homeMembership = index.categoryMemberships(home, STATUS.approved)
      .find((m) => m.word === word);
    for (const m of index.wordMemberships(word, STATUS.alternative)) {
      if (m.category === home || !selected.has(m.category)) continue;
      traps.push({
        word: index.words[word].t,
        home: index.categories[home].k,
        decoy: index.categories[m.category].k,
        homeObviousness: homeMembership?.obviousness ?? 0,
        decoyFit: m.fit,
        decoyObviousness: m.obviousness,
      });
    }
  }
  // сильнее та ловушка, где дом очевиднее, а приманка настоящая, но тихая
  return traps.sort((a, b) =>
    (b.decoyFit - b.decoyObviousness) - (a.decoyFit - a.decoyObviousness));
}

// --------------------------------------------------------------------------- //
// шаг 7: цепи
// --------------------------------------------------------------------------- //

/**
 * Цепи — единственный модификатор с аналитически доказуемым тупиком: если цепь
 * на A снимается сбором B, а цепь на B — сбором A, игрок заперт навсегда.
 * Поэтому граф зависимостей строится заведомо ациклическим, а валидатор это
 * перепроверяет независимо.
 */
function buildChains(
  categories: LevelCategory[], count: number, rng: Rng,
): Chain[] {
  if (count <= 0) return [];
  // запирать quick-win нельзя: игрок должен иметь точку входа
  const lockable = categories.filter((c) => !c.isQuickwin && c.metaDepth === 0);
  const unlockers = categories.filter((c) => c.isQuickwin || c.metaDepth === 0);
  if (lockable.length === 0 || unlockers.length === 0) return [];

  const chains: Chain[] = [];
  const locked = new Set<string>();
  for (const candidate of rng.shuffle(lockable)) {
    if (chains.length >= count) break;
    const unlocker = rng.shuffle(unlockers)
      .find((u) => u.key !== candidate.key && !locked.has(u.key));
    if (!unlocker) continue;
    chains.push({ locksCategory: candidate.key, unlockedByCompleting: unlocker.key });
    locked.add(candidate.key);
  }
  return chains;
}

// --------------------------------------------------------------------------- //
// сборка LevelSpec
// --------------------------------------------------------------------------- //

function buildLevelSpec(
  index: ContentIndex,
  plan: LevelPlan,
  selected: PoolEntry[],
  edges: MetaEdge[],
  assignment: Map<number, number[]>,
  wordsPerCategory: number,
  rng: Rng,
): { spec: LevelSpec; traps: Trap[] } {
  const parentOf = new Map<number, number>();
  for (const edge of edges) parentOf.set(edge.child, edge.parent);
  const metaWordToChild = new Map<number, number>();
  for (const edge of edges) metaWordToChild.set(edge.word, edge.child);

  const depthOf = (cat: number, guard = 0): number => {
    if (guard > 8) return 0;
    const parent = parentOf.get(cat);
    return parent === undefined ? 0 : 1 + depthOf(parent, guard + 1);
  };

  const quickwinKeys = new Set<string>();
  const categories: LevelCategory[] = selected.map((entry) => {
    const words = assignment.get(entry.category) ?? [];
    const meta = index.categories[entry.category];
    const levelWords: LevelWord[] = words.map((w) => {
      const child = metaWordToChild.get(w);
      const membership = index.categoryMemberships(entry.category, STATUS.approved)
        .find((m) => m.word === w);
      const word = index.words[w];
      if (child !== undefined) {
        return {
          text: word.t, kind: 'meta' as const,
          metaChild: index.categories[child].k,
          zipf: word.z, frequencyUnknown: word.u === 1,
        };
      }
      return {
        text: word.t, kind: 'word' as const,
        zipf: word.z, frequencyUnknown: word.u === 1,
        relation: membership?.relation,
        fit: membership?.fit,
        obviousness: membership?.obviousness,
      };
    });

    const hasMeta = levelWords.some((w) => w.kind === 'meta');
    const allFrequent = words.every((w) => index.isQuickwinWord(w));
    const isQuickwin = !hasMeta && allFrequent;
    if (isQuickwin) quickwinKeys.add(meta.k);

    return {
      key: meta.k,
      label: meta.l,
      rule: meta.r,
      theme: meta.th,
      words: levelWords,
      metaDepth: depthOf(entry.category),
      parentKey: parentOf.has(entry.category)
        ? index.categories[parentOf.get(entry.category)!].k : null,
      isQuickwin,
    };
  });

  const traps = findTraps(index, assignment, edges);
  const chains = buildChains(categories, plan.chainCount, rng);

  const metaCount = edges.length;
  const bubbles = startBubbles(categories.length, metaCount, wordsPerCategory);
  const floor = moveFloor(categories.length, 0, wordsPerCategory);

  const spec: LevelSpec = {
    levelId: plan.levelId,
    schemaVersion: '2.0',
    board: {
      categoriesCount: categories.length,
      wordsPerCategory,
      startBubbles: bubbles,
      boardCapacity: BOARD_CAPACITY,
      moveFloor: floor,
      // K = null -> лимита нет: на L1 референса поле держит весь уровень
      moveLimit: plan.moveLimitK === null ? null : moveLimit(floor, plan.moveLimitK),
      moveLimitK: plan.moveLimitK,
      moveLimitPolicy: 'conservative',
    },
    categories,
    traps: traps.slice(0, Math.max(plan.trapTarget, traps.length > 0 ? 1 : 0)),
    halves: [],
    modifiers: { chains, frozenBubbles: [], hiddenBubbles: [] },
  };
  return { spec, traps };
}

// --------------------------------------------------------------------------- //
// генерация одного уровня с ослаблениями
// --------------------------------------------------------------------------- //

/**
 * Дополнительная проверка собранного уровня внутри цикла попыток.
 *
 * Сюда генератору передаются счёт решений и hard-валидация. Без этого
 * двусмысленный уровень доезжал бы до отчёта как готовый: именно так первый
 * прогон выдал уровень 202 с двумя полными раскладками. Отбраковывать надо
 * там, где ещё можно попробовать другой набор категорий.
 */
export type AcceptCheck = (spec: LevelSpec) => { ok: boolean; stage: string; reason: string };

export function generateLevel(
  index: ContentIndex,
  plan: LevelPlan,
  config: BlockConfig,
  history: PackHistory,
  options: {
    maxAttempts?: number;
    accept?: AcceptCheck;
    /** категории, зарезервированные под другие уровни блока */
    excludeCategories?: Set<number>;
    /** цепочка, зарезервированная под ЭТОТ уровень */
    forcedChain?: MetaEdge[];
  } = {},
): LevelGenerationOutcome {
  const attempts: GenerationAttempt[] = [];
  const relaxationsUsed: Relaxation[] = [];
  /**
   * Калиброванному блоку нужно больше попыток: гейты декады отсекают часть пула,
   * и подходящий набор категорий находится не так быстро. Замер по всем 20
   * декадам: при 24 попытках декада 51-60 собирала 9 уровней из 10, при 48 —
   * все двадцать декад дают 10 из 10. Без гейтов лимит остаётся прежним, иначе
   * изменилось бы поведение пресета 201-210.
   */
  const maxAttempts = options.maxAttempts ?? (config.decadeGates ? 48 : 24);
  const wordsPerCategory = config.wordsPerCategory || 4;

  const baseConstraints = (): Constraints => ({
    categoryCount: plan.categoryCount,
    gates: config.decadeGates ?? null,
    wordWindow: config.wordFreshnessWindow,
    categoryWindow: config.categoryFreshnessWindow,
    metaCount: plan.metaCount,
    metaDepthTarget: plan.metaDepthTarget,
    rareTarget: plan.rareTarget,
    rareTolerance: 0,
    trapTarget: plan.trapTarget,
    themesAllowed: config.includeThemes.length ? new Set(config.includeThemes) : null,
    themesExcluded: new Set(config.excludeThemes),
    enforceFreshness: true,
  });

  const applyRelaxations = (c: Constraints, list: Relaxation[]): Constraints => {
    const out = { ...c, themesAllowed: c.themesAllowed, themesExcluded: c.themesExcluded };
    for (const r of list) {
      switch (r) {
        case 'точное число редких слов → диапазон':
          out.rareTolerance = 3; break;
        case 'тематическая узость → соседние сферы':
          out.themesAllowed = null; break;
        case 'меньше ловушек':
          out.trapTarget = Math.max(0, out.trapTarget - 1); break;
        case 'меньше мета-связей':
          out.metaCount = Math.max(0, out.metaCount - 1); break;
        case 'меньше глубины мета':
          out.metaDepthTarget = Math.max(1, out.metaDepthTarget - 1); break;
        case 'другой набор категорий':
          break;                                   // реализуется сменой seed попытки
      }
    }
    return out;
  };

  let lastReason = 'не начато';
  let lastStage = 'инициализация';

  for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
    // каждое следующее ослабление включается после нескольких неудач подряд
    const relaxLevel = Math.min(RELAXATION_ORDER.length, Math.floor(attempt / 4));
    const active = RELAXATION_ORDER.slice(0, relaxLevel) as Relaxation[];
    const constraints = applyRelaxations(baseConstraints(), active);
    const rng = createRng(`${config.seed}|L${plan.levelId}|a${attempt}`);

    /**
     * Свежесть слова: одно правило для обычных пузырей и для мета-слов.
     * Ключ истории — нормализованная форма, чтобы регистр и вид апострофа
     * не создавали дырку в проверке.
     */
    const isWordFresh = (word: number): boolean => {
      if (!constraints.enforceFreshness) return true;
      const last = history.wordLastLevel.get(index.words[word].n);
      return last === undefined || plan.levelId - last > constraints.wordWindow;
    };

    const pool = buildPool(index, plan, constraints, history, options.excludeCategories);
    if (pool.length < constraints.categoryCount) {
      lastStage = 'пул категорий';
      lastReason = `после фильтров осталось ${pool.length} совместимых категорий, `
        + `а нужно ${constraints.categoryCount}`;
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const picked = selectCategories(index, pool, constraints, rng,
      options.forcedChain, isWordFresh);
    if (!picked) {
      lastStage = 'выбор категорий';
      lastReason = 'не удалось собрать набор с мета-каркасом и категорией быстрой победы';
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const assigned = assignWords(index, picked.selected, picked.edges, constraints,
      history, plan, rng, wordsPerCategory, isWordFresh);
    if (!assigned) {
      lastStage = 'назначение слов';
      lastReason = 'точное покрытие не сошлось: у части категорий не остаётся '
        + 'четырёх свободных слов, каждое из которых имеет ровно один дом';
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const rareGap = Math.abs(assigned.rareUsed - constraints.rareTarget);
    if (rareGap > 1 + constraints.rareTolerance) {
      lastStage = 'редкость';
      lastReason = `редких слов ${assigned.rareUsed}, цель ${constraints.rareTarget}`;
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const { spec, traps } = buildLevelSpec(index, plan, picked.selected, picked.edges,
      assigned.words, wordsPerCategory, rng);

    if (options.accept) {
      const verdict = options.accept(spec);
      if (!verdict.ok) {
        lastStage = verdict.stage;
        lastReason = verdict.reason;
        attempts.push({ index: attempt, outcome: 'rejected', stage: verdict.stage,
          reason: verdict.reason, relaxations: active.slice() });
        continue;
      }
    }

    attempts.push({ index: attempt, outcome: 'accepted', stage: 'готово',
      reason: `${spec.categories.length} категорий, ${picked.edges.length} мета-связей, `
        + `${assigned.rareUsed} редких слов, ${traps.length} ловушек`,
      relaxations: active.slice() });
    relaxationsUsed.push(...active);
    return { spec, traps, attempts, relaxationsUsed: Array.from(new Set(relaxationsUsed)) };
  }

  return {
    traps: [],
    attempts,
    relaxationsUsed: Array.from(new Set(relaxationsUsed)),
    failure: {
      levelId: plan.levelId,
      reason: `Не сошлось за ${maxAttempts} попыток. Последняя причина — `
        + `${lastStage}: ${lastReason}.`,
      suggestions: [
        'расширить тематические сферы или снять исключения',
        'снизить точное число редких слов до диапазона',
        'уменьшить число мета-связей',
        'уменьшить число категорий на уровне',
        'пополнить базу: категориям не хватает утверждённых слов',
      ],
      attempts,
    },
  };
}

/** Обновляет историю пакета после принятия уровня. */
export function recordLevelInHistory(history: PackHistory, spec: LevelSpec): void {
  for (const category of spec.categories) {
    history.categoryLastLevel.set(category.key, spec.levelId);
    for (const word of category.words) {
      // тот же ключ, что использует проверка свежести: иначе слово с необычным
      // апострофом или регистром проскочило бы мимо неё
      history.wordLastLevel.set(normalizeWordKey(word.text), spec.levelId);
      history.wordCategory?.set(normalizeWordKey(word.text), category.key);
    }
  }
}

/** Ключ идентичности слова: как в снимке базы (поле `n`). */
export function normalizeWordKey(text: string): string {
  return text.normalize('NFKC')
    .replace(/[\u2018\u2019\u02bc\u2032]/g, "'")
    .replace(/[\u2010-\u2015\u2212]/g, '-')
    .trim().toLowerCase()
    .replace(/\s+/g, ' ');
}

export { quadrupleKey };
