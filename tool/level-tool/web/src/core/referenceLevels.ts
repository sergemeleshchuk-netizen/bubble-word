/**
 * Уровни оригинала как есть: без генерации, без гейтов, без подбора слов.
 *
 * Зачем отдельный путь. Всё остальное в инструменте — конвейер: профиль декады
 * задаёт правила, генератор подбирает слова, валидатор бракует, оценки говорят,
 * что вышло. Для уровня оригинала конвейер не нужен и вреден: состав уровня уже
 * задан источником, подбирать нечего, а браковать чужой уровень нашими гейтами
 * бессмысленно — он был сделан не по ним. Здесь уровень только СОБИРАЕТСЯ из
 * выгрузки и измеряется.
 *
 * Что берётся из выгрузки, а что считаем мы:
 *
 *   из выгрузки   категории, их порядок, слова, порядок слов, мета-пузыри,
 *                 вложенность, распилы (`chunks`)
 *   из записей    для L1-20: лимит ходов и число пузырей на старте
 *   считаем сами  лимит ходов для L21+, оценки D и I, число решений
 *
 * Почему выкладка здесь своя, а не `core/deal.ts`. Наша общая выкладка тасует
 * слова внутри категории — для собственных уровней это правильно (иначе игрок
 * получал бы самые очевидные слова бесплатно). Для уровня оригинала тасовать
 * нельзя: порядок выдачи и есть то, что мы восстановили покадрово по 19
 * записанным уровням (`reference-deal-order.md`). Перемешать его — значит
 * выбросить результат замера.
 */
import type {
  Deal, DealBubble, GeneratedLevel, HalfSplit, LevelCategory, LevelPlan,
  LevelSpec, LevelWord, ValidationResult,
} from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import { BOARD_CAPACITY, moveFloor, moveLimit, startBubbles } from './levelMath.ts';
import { canonicalJson, levelSpecHash, sha256Hex } from './hashing.ts';
import { countSolutions } from './solutionCounter.ts';
import { computeDifficulty, type ScoringConfig } from './scoringDifficulty.ts';
import { computeInterest } from './scoringInterest.ts';

// --------------------------------------------------------------------------- //
// данные выгрузки
// --------------------------------------------------------------------------- //

/** Категория уровня в компактном виде (`scripts/export_reference_levels.py`). */
export interface BwjCategory {
  /** имя категории */
  n: string;
  /** слова в порядке выдачи */
  w: string[];
  /** какие из слов — имена других категорий уровня */
  m?: string[];
  /** глубина вложенности; 0 не пишется */
  d?: number;
  /** имя родителя */
  p?: string;
  /** распилы: [слово, кусок1, кусок2] */
  c?: string[][];
}

export interface BwjLevel {
  id: number;
  cats: BwjCategory[];
  /** снятое с записей; есть только у уровней 1-20 */
  obs?: { moveLimit?: number; startBubbles?: number; wordsOnStart?: string[] };
}

export interface BwjLevels {
  schema_version: string;
  source: string;
  order_note: string;
  levels: BwjLevel[];
}

/**
 * K для уровней, у которых лимит ходов не наблюдался.
 *
 * Взято из записи уровня 12: 60 ходов при минимуме 44. Это единственное
 * измерение, которое у нас есть, и выдавать его за правило оригинала нельзя —
 * поэтому в интерфейсе такой лимит помечается как наш расчёт.
 */
export const FALLBACK_MOVE_LIMIT_K = 1.36;

/**
 * Версия схемы спека. Та же, что у собранных нами уровней: формат один, иначе
 * прототип и экспорт пришлось бы учить второму.
 */
export const REFERENCE_SCHEMA_VERSION = '2.2';

/**
 * Что подставляется на место конфига и версии генератора при хешировании.
 * Уровень оригинала не собирался ни конфигом, ни генератором, но хеш обязан
 * оставаться сравнимым: два одинаковых уровня из одной выгрузки должны давать
 * один хеш, а уровень из другой выгрузки — другой.
 */
export const REFERENCE_ORIGIN = 'bwj-org-1025';

// --------------------------------------------------------------------------- //
// сборка уровня
// --------------------------------------------------------------------------- //

/**
 * Распилы уровня, разложенные по КЛЮЧУ категории.
 *
 * Ключ, а не имя: имя из выгрузки («ocean animals») и метка категории в спеке
 * («OCEAN ANIMALS») пишутся по-разному, и выкладка, ищущая распилы по метке,
 * молча не находила ни одного — уровень 12 давал 31 пузырь на старте вместо
 * записанных 24. Один ключ на обе стороны эту рассинхронизацию исключает.
 */
function chunkedWordsOf(
  level: BwjLevel, keyOf: (categoryName: string) => string,
): Map<string, Set<string>> {
  const out = new Map<string, Set<string>>();
  for (const c of level.cats) {
    for (const [word] of c.c ?? []) {
      const key = keyOf(c.n);
      const set = out.get(key) ?? new Set<string>();
      set.add(word.toLowerCase());
      out.set(key, set);
    }
  }
  return out;
}

/**
 * Выкладка уровня оригинала: слова выдаются строго в порядке источника.
 *
 * Правило проверено на 19 записанных уровнях (`reference-deal-order.md` §4а):
 * стартовое поле — префикс этого порядка, из которого выброшены мета-пузыри,
 * а распиленное слово занимает ДВА места. Точность 87% слов; расходится только
 * там, где оригинал пропускает вложенную категорию, а закономерности в таких
 * пропусках найти не удалось.
 *
 * `startBudget` — сколько пузырей помещается на поле. Для L1-20 это снятое с
 * записи число, для остальных — вместимость поля.
 */
export function referenceDeal(
  categories: readonly LevelCategory[],
  chunked: Map<string, Set<string>>,
  startBudget: number,
): Deal {
  const cost = (categoryKey: string, word: string): number =>
    (chunked.get(categoryKey)?.has(word.toLowerCase()) ? 2 : 1);

  const start: DealBubble[] = [];
  const queue: DealBubble[] = [];
  let spent = 0;
  let full = false;
  for (const category of categories) {
    for (const word of category.words) {
      /*
       * Мета-пузырь не раздаётся вообще — ни на старт, ни в очередь.
       *
       * Он не приходит из колоды: он РОЖДАЕТСЯ, когда игрок собирает свою
       * категорию, и её имя становится пузырём в родителе. Прототип так и
       * считает и на лишний мета-пузырь в выкладке отвечает «выкладка не
       * сошлась — раскладываю сам», то есть молча выбрасывает восстановленный
       * порядок оригинала и раскладывает по-своему. Именно это и происходило
       * с уровнем 12: «лишний пузырь TIME PERIODS::MONTHS».
       */
      if (word.kind === 'meta') continue;
      const bubble = { word: word.text, category: category.key };
      const price = cost(category.key, word.text);
      if (!full && spent + price <= startBudget) {
        start.push(bubble);
        spent += price;
      } else {
        // как только бюджет кончился, дальше всё уходит в очередь по порядку:
        // «пропустить длинное слово и взять следующее» оригинал не делает
        full = true;
        queue.push(bubble);
      }
    }
  }
  return { start, queue };
}

export interface ReferenceSpecResult {
  spec: LevelSpec;
  /** лимит ходов снят с записи, а не посчитан нами */
  moveLimitObserved: boolean;
  /** размер старта снят с записи, а не взят вместимостью поля */
  startObserved: boolean;
  /** категории уровня, которых нет в снимке словаря (метаданные пришлось достроить) */
  unknownCategories: string[];
}

/**
 * Спек уровня оригинала. Словарь нужен только ради метаданных — частотности,
 * темы, правила категории; состав уровня целиком из выгрузки.
 */
export function buildReferenceSpec(
  index: ContentIndex, level: BwjLevel,
): ReferenceSpecResult {
  const byLabel = new Map<string, number>();
  index.categories.forEach((c, i) => byLabel.set(c.l, i));

  const unknown: string[] = [];
  const resolved = level.cats.map((entry) => {
    const catIndex = byLabel.get(entry.n.toUpperCase());
    if (catIndex === undefined) unknown.push(entry.n);
    return { entry, catIndex };
  });

  // имя категории -> её ключ: по нему мета-пузырь находит своего ребёнка
  const labelToKey = new Map<string, string>();
  for (const { entry, catIndex } of resolved) {
    labelToKey.set(entry.n, catIndex === undefined
      ? entry.n.toLowerCase().replace(/[^a-z0-9]+/g, '_')
      : index.categories[catIndex].k);
  }

  const categories: LevelCategory[] = resolved.map(({ entry, catIndex }) => {
    const meta = catIndex === undefined ? null : index.categories[catIndex];
    const metaWords = new Set(entry.m ?? []);
    const words: LevelWord[] = entry.w.map((text) => {
      const wi = index.wordIndex(text);
      const membership = (wi === undefined || catIndex === undefined) ? undefined
        : index.categoryMemberships(catIndex).find((m) => m.word === wi);
      const isMeta = metaWords.has(text);
      return {
        text,
        kind: isMeta ? 'meta' : 'word',
        metaChild: isMeta ? labelToKey.get(text) : undefined,
        zipf: wi === undefined ? null : index.zipf(wi),
        frequencyUnknown: wi === undefined ? true : index.isFrequencyUnknown(wi),
        relation: membership?.relation,
        fit: membership?.fit,
        obviousness: membership?.obviousness,
      };
    });
    const plain = words.filter((w) => w.kind === 'word');
    return {
      key: labelToKey.get(entry.n) ?? entry.n,
      label: meta?.l ?? entry.n.toUpperCase(),
      rule: meta?.r ?? `категория оригинала «${entry.n}»`,
      theme: meta?.th ?? 'reference',
      words,
      metaDepth: entry.d ?? 0,
      parentKey: entry.p ? labelToKey.get(entry.p) ?? null : null,
      isQuickwin: plain.length === words.length
        && plain.every((w) => w.zipf !== null && w.zipf >= index.quickwinThreshold),
    };
  });

  const metaCount = categories.reduce(
    (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0);
  const floor = moveFloor(categories.length);

  const observedLimit = level.obs?.moveLimit ?? null;
  const limit = observedLimit ?? moveLimit(floor, FALLBACK_MOVE_LIMIT_K);
  const board = {
    categoriesCount: categories.length,
    wordsPerCategory: 4,
    startBubbles: startBubbles(categories.length, metaCount),
    boardCapacity: BOARD_CAPACITY,
    moveFloor: floor,
    moveLimit: limit,
    // K печатается производным от лимита: для наблюдённого лимита это описание
    // факта, а не формула, по которой он получен
    moveLimitK: Math.round((limit / Math.max(1, floor)) * 100) / 100,
    moveLimitPolicy: 'conservative' as const,
  };

  /*
   * Распилы едут в спек полем `halves` — тем самым, которым инструмент
   * описывает механику половинок у собственных уровней. Без него распил знала
   * бы только выкладка (слово стоит два пузыря), а прототип рисовал бы слово
   * целым: поле визуально пустело бы, и уровень оригинала играл бы не так, как
   * записан. Одно поле на обе стороны эту рассинхронизацию исключает.
   */
  const halves: HalfSplit[] = [];
  for (const entry of level.cats) {
    for (const [word, a, b] of entry.c ?? []) {
      if (a === undefined || b === undefined) continue;
      halves.push({
        word,
        home: labelToKey.get(entry.n) ?? entry.n,
        fragments: [a, b],
        // кусок сам по себе слово («car» в «carpet») меняет чтение уровня,
        // поэтому проверяем по словарю, а не на глаз
        fragmentsAreWords: index.wordIndex(a) !== undefined
          && index.wordIndex(b) !== undefined,
      });
    }
  }

  const startBudget = level.obs?.startBubbles ?? BOARD_CAPACITY;
  const spec: LevelSpec = {
    levelId: level.id,
    schemaVersion: REFERENCE_SCHEMA_VERSION,
    board,
    categories,
    deal: referenceDeal(
      categories,
      chunkedWordsOf(level, (name) => labelToKey.get(name) ?? name),
      startBudget),
    traps: [],
    halves,
    modifiers: { chains: [], frozenBubbles: [], hiddenBubbles: [], chainLine: null },
  };

  return {
    spec,
    moveLimitObserved: observedLimit !== null,
    startObserved: level.obs?.startBubbles !== undefined,
    unknownCategories: unknown,
  };
}

// --------------------------------------------------------------------------- //
// пакет уровней
// --------------------------------------------------------------------------- //

/**
 * Заглушка приёмки. Валидатор — это НАШИ правила, и уровень оригинала им не
 * подчиняется: он сделан не по ним. Прогнать его и показать «12 нарушений»
 * значило бы обвинить чужой уровень в несоответствии нашему регламенту.
 * Поэтому проверка одна и честная: уровень взят как есть.
 */
function referenceValidation(unknown: string[]): ValidationResult {
  const checks: ValidationResult['checks'] = [{
    code: 'REFERENCE_AS_IS',
    passed: true,
    severity: 'soft' as const,
    detail: 'уровень взят из выгрузки оригинала как есть: наши гейты и '
      + 'валидатор к нему не применяются',
  }];
  if (unknown.length) {
    checks.push({
      code: 'REFERENCE_CATEGORY_UNKNOWN',
      passed: true,
      severity: 'soft' as const,
      detail: `нет в снимке словаря: ${unknown.join(', ')} — метаданные `
        + '(тема, правило) достроены, слова и состав не пострадали',
    });
  }
  return { passed: true, checks, issues: [] };
}

/** План, которого не было: уровень не планировался, а взят готовым. */
function referencePlan(spec: LevelSpec, position: number): LevelPlan {
  const metaCount = spec.categories.reduce(
    (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0);
  return {
    levelId: spec.levelId,
    position,
    role: 'growth',
    categoryCount: spec.categories.length,
    metaCount,
    metaDepthTarget: Math.max(0, ...spec.categories.map((c) => c.metaDepth)),
    rareTarget: 0,
    trapTarget: 0,
    chainCount: 0,
    modifier: 'none',
    targetDifficulty: [1, 10],
    targetInterest: [1, 10],
    moveLimitK: spec.board.moveLimitK,
  };
}

export interface ReferenceBlock {
  levels: GeneratedLevel[];
  /** по каждому уровню: что взято из записи, а что посчитано нами */
  provenance: Record<number, {
    moveLimitObserved: boolean;
    startObserved: boolean;
    unknownCategories: string[];
  }>;
  packHash: string;
  missing: number[];
}

/** Собирает выбранные уровни оригинала и измеряет их нашими моделями. */
export function buildReferenceBlock(
  index: ContentIndex, data: BwjLevels, ids: readonly number[],
  scoring: ScoringConfig,
): ReferenceBlock {
  const byId = new Map(data.levels.map((l) => [l.id, l]));
  const levels: GeneratedLevel[] = [];
  const provenance: ReferenceBlock['provenance'] = {};
  const missing: number[] = [];

  ids.forEach((id, i) => {
    const entry = byId.get(id);
    if (!entry) { missing.push(id); return; }
    const built = buildReferenceSpec(index, entry);
    const { spec } = built;
    const solutions = countSolutions(index, spec);
    levels.push({
      plan: referencePlan(spec, i + 1),
      spec,
      validation: referenceValidation(built.unknownCategories),
      solutions,
      difficulty: computeDifficulty(spec, index, scoring, solutions),
      interest: computeInterest(spec, index, scoring, solutions),
      attempts: [],
      levelSpecHash: levelSpecHash({
        levelSpec: spec,
        seed: REFERENCE_ORIGIN,
        normalizedConfig: { source: 'reference-as-is', levels: ids },
        generatorVersion: REFERENCE_ORIGIN,
        contentSnapshotHash: data.schema_version,
      }),
    });
    provenance[id] = {
      moveLimitObserved: built.moveLimitObserved,
      startObserved: built.startObserved,
      unknownCategories: built.unknownCategories,
    };
  });

  return {
    levels,
    provenance,
    packHash: sha256Hex(canonicalJson({
      levels: levels.map((l) => l.levelSpecHash),
      origin: REFERENCE_ORIGIN,
    })),
    missing,
  };
}

/**
 * Разбор строки выбора уровней: «1-10», «3, 7, 12», «1-5, 20».
 *
 * Отдельная функция, а не regexp по месту: тем же способом человек набирает
 * диапазон на экране настройки блока, и вести себя это должно одинаково.
 */
export function parseLevelSelection(input: string, max: number): {
  ids: number[]; error: string | null;
} {
  const ids: number[] = [];
  const seen = new Set<number>();
  for (const raw of input.split(/[,;]/)) {
    const part = raw.trim();
    if (!part) continue;
    const range = part.match(/^(\d+)\s*[-–—]\s*(\d+)$/);
    const single = part.match(/^(\d+)$/);
    if (range) {
      const from = Number(range[1]);
      const to = Number(range[2]);
      if (from < 1 || to > max || from > to) {
        return { ids: [], error: `диапазон «${part}» вне 1-${max}` };
      }
      for (let n = from; n <= to; n += 1) {
        if (!seen.has(n)) { seen.add(n); ids.push(n); }
      }
    } else if (single) {
      const n = Number(single[1]);
      if (n < 1 || n > max) {
        return { ids: [], error: `уровня ${n} нет: в выгрузке 1-${max}` };
      }
      if (!seen.has(n)) { seen.add(n); ids.push(n); }
    } else {
      return { ids: [], error: `не разобрал «${part}»: нужен номер или диапазон` };
    }
  }
  if (!ids.length) return { ids: [], error: 'не выбрано ни одного уровня' };
  return { ids, error: null };
}
