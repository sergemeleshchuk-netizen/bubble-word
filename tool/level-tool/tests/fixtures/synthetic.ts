/**
 * Синтетический снимок базы и конструктор уровней для тестов.
 *
 * Негативные фикстуры обязаны действительно падать. Проверять это на настоящем
 * снимке неудобно: нужно уметь собрать уровень, нарушающий ровно один инвариант,
 * не задев остальные. Поэтому здесь маленькая управляемая база.
 */
import type {
  LevelSpec, LevelCategory, LevelWord, Readiness, Snapshot, SnapshotMembership,
} from '../../web/src/core/types.ts';
import { STATUS } from '../../web/src/core/types.ts';
import { buildDeal } from '../../web/src/core/deal.ts';
import { BOARD_CAPACITY } from '../../web/src/core/levelMath.ts';

interface CatSpec {
  key: string;
  label: string;
  theme?: string;
  /** [слово, zipf, статус, очевидность] */
  words: [string, number, keyof typeof STATUS, number?][];
}

/** Собирает снимок из компактного описания категорий. */
export function makeSnapshot(specs: CatSpec[], extra: {
  /** дополнительные связи: слово годится ещё и в эту категорию */
  alternatives?: [string, string, number, number][];
  metaCapable?: [string, string][];
  /** запреты пар из базы: [ключ, ключ, severity] */
  conflicts?: [string, string, string?][];
  /** готовность категорий: ключ → readiness (по умолчанию ready) */
  readiness?: Record<string, Readiness>;
} = {}): Snapshot {
  const wordList: { t: string; z: number }[] = [];
  const wordIndex = new Map<string, number>();
  const addWord = (text: string, zipf: number): number => {
    const key = text.toLowerCase();
    if (wordIndex.has(key)) return wordIndex.get(key)!;
    wordIndex.set(key, wordList.length);
    wordList.push({ t: text, z: zipf });
    return wordList.length - 1;
  };

  const memberships: SnapshotMembership[] = [];
  specs.forEach((spec, ci) => {
    for (const [text, zipf, status, obviousness] of spec.words) {
      const wi = addWord(text, zipf);
      memberships.push([wi, ci, STATUS[status], 0.95, obviousness ?? 0.8,
        'associated_with', null]);
    }
  });

  const catIndex = new Map(specs.map((s, i) => [s.key, i]));

  for (const [word, categoryKey, fit, obviousness] of extra.alternatives ?? []) {
    const wi = wordIndex.get(word.toLowerCase());
    const ci = catIndex.get(categoryKey);
    if (wi === undefined || ci === undefined) {
      throw new Error(`фикстура: нет слова ${word} или категории ${categoryKey}`);
    }
    memberships.push([wi, ci, STATUS.alternative, fit, obviousness,
      'associated_with', null]);
  }

  // мета-пригодность: имя категории существует как слово и годится в родителя
  const metaCapable: Snapshot['meta_capable'] = [];
  for (const [childKey, parentKey] of extra.metaCapable ?? []) {
    const child = catIndex.get(childKey);
    const parent = catIndex.get(parentKey);
    if (child === undefined || parent === undefined) {
      throw new Error(`фикстура: нет категории ${childKey} или ${parentKey}`);
    }
    const labelWord = specs[child].label.toLowerCase();
    const wi = wordIndex.get(labelWord) ?? addWord(specs[child].label, 4.0);
    metaCapable.push({ category: child, word: wi, hosts: [parent] });
  }

  const conflicts: Snapshot['conflicts'] = [];
  for (const [aKey, bKey, severity] of extra.conflicts ?? []) {
    const a = catIndex.get(aKey);
    const b = catIndex.get(bKey);
    if (a === undefined || b === undefined) {
      throw new Error(`фикстура: нет категории ${aKey} или ${bKey}`);
    }
    conflicts.push([Math.min(a, b), Math.max(a, b), 0, severity ?? 'P0', 4]);
  }

  return {
    schema_version: 'snapshot-test',
    statuses: ['approved', 'alternative', 'hard_only', 'candidate', 'rejected'],
    risk_flags: ['obscure', 'regional', 'proper_noun', 'multiword'],
    conflict_types: ['do_not_pair', 'needs_disjoint_words'],
    quartet_tiers: ['normal', 'hard'],
    constants: { zipf_max: 7, top50k_zipf: 2.55, quickwin_zipf: 3.0 },
    categories: specs.map((s) => ({
      k: s.key, l: s.label, r: `правило для ${s.label}`,
      rel: 'associated_with', th: s.theme ?? 'test', d: 0.4,
      rd: extra.readiness?.[s.key] ?? 'ready',
    })),
    conflicts,
    words: wordList.map((w) => ({
      t: w.t, n: w.t.toLowerCase(), z: w.z, u: 0,
      l: /^[a-z]+$/.test(w.t) ? 1 : 0, p: 0, tok: 1,
    })),
    senses: [],
    memberships,
    meta_capable: metaCapable,
    content_snapshot_hash: 'test-snapshot-hash',
  };
}

/** Простая корректная база: четыре плоские категории с частотными словами. */
export const SIMPLE_SNAPSHOT = makeSnapshot([
  { key: 'colors', label: 'COLORS', theme: 'properties', words: [
    ['red', 5.0, 'approved'], ['blue', 4.9, 'approved'],
    ['green', 4.8, 'approved'], ['yellow', 4.5, 'approved']] },
  { key: 'fruits', label: 'FRUITS', theme: 'food', words: [
    ['apple', 4.7, 'approved'], ['banana', 4.2, 'approved'],
    ['pear', 3.9, 'approved'], ['plum', 3.6, 'approved']] },
  { key: 'tools', label: 'TOOLS', theme: 'tools', words: [
    ['hammer', 4.1, 'approved'], ['saw', 4.4, 'approved'],
    ['drill', 4.0, 'approved'], ['wrench', 3.5, 'approved']] },
  { key: 'weather', label: 'WEATHER', theme: 'nature', words: [
    ['rain', 5.1, 'approved'], ['snow', 4.9, 'approved'],
    ['wind', 4.8, 'approved'], ['fog', 4.0, 'approved']] },
]);

function word(text: string, zipf: number, obviousness = 0.8): LevelWord {
  return { text, kind: 'word', zipf, frequencyUnknown: false,
    relation: 'associated_with', fit: 0.95, obviousness };
}

function metaWord(text: string, child: string, zipf = 4.0): LevelWord {
  return { text, kind: 'meta', metaChild: child, zipf, frequencyUnknown: false };
}

/** Категория уровня из компактного описания. */
export function levelCategory(
  key: string, label: string, words: LevelWord[],
  opts: { theme?: string; metaDepth?: number; parentKey?: string | null;
    isQuickwin?: boolean } = {},
): LevelCategory {
  const hasMeta = words.some((w) => w.kind === 'meta');
  const allFrequent = words.every((w) => w.zipf !== null && w.zipf >= 3.0);
  return {
    key, label, rule: `правило для ${label}`, theme: opts.theme ?? 'test',
    words,
    metaDepth: opts.metaDepth ?? 0,
    parentKey: opts.parentKey ?? null,
    isQuickwin: opts.isQuickwin ?? (!hasMeta && allFrequent),
  };
}

/** Корректный уровень на SIMPLE_SNAPSHOT: все инварианты выполнены. */
export function validLevel(): LevelSpec {
  const categories = [
    levelCategory('colors', 'COLORS', [
      word('red', 5.0), word('blue', 4.9), word('green', 4.8), word('yellow', 4.5)],
      { theme: 'properties' }),
    levelCategory('fruits', 'FRUITS', [
      word('apple', 4.7), word('banana', 4.2), word('pear', 3.9), word('plum', 3.6)],
      { theme: 'food' }),
    levelCategory('tools', 'TOOLS', [
      word('hammer', 4.1), word('saw', 4.4), word('drill', 4.0), word('wrench', 3.5)],
      { theme: 'tools' }),
    levelCategory('weather', 'WEATHER', [
      word('rain', 5.1), word('snow', 4.9), word('wind', 4.8), word('fog', 4.0)],
      { theme: 'nature' }),
  ];
  return buildSpec(201, categories);
}

/** Собирает LevelSpec с правильной арифметикой доски. */
export function buildSpec(
  levelId: number, categories: LevelCategory[],
  opts: { chains?: { locksCategory: string; unlockedByCompleting: string }[];
    halves?: LevelSpec['halves']; moveLimitK?: number;
    overrideStartBubbles?: number; overrideMoveLimit?: number } = {},
): LevelSpec {
  const metaCount = categories.reduce((n, c) =>
    n + c.words.filter((w) => w.kind === 'meta').length, 0);
  const k = opts.moveLimitK ?? 1.4;
  const floor = categories.length * 3 + (opts.halves?.length ?? 0);
  const board = {
    categoriesCount: categories.length,
    wordsPerCategory: 4,
    startBubbles: opts.overrideStartBubbles ?? categories.length * 4 - metaCount,
    boardCapacity: BOARD_CAPACITY,
    moveFloor: floor,
    moveLimit: opts.overrideMoveLimit ?? Math.ceil(floor * k),
    moveLimitK: k,
    moveLimitPolicy: 'conservative' as const,
  };
  return {
    levelId,
    schemaVersion: '2.1',
    board,
    categories,
    deal: buildDeal(levelId, categories, board),
    traps: [],
    halves: opts.halves ?? [],
    modifiers: { chains: opts.chains ?? [], frozenBubbles: [], hiddenBubbles: [] },
  };
}

export { word, metaWord };
