/**
 * Индекс снимка контентной базы.
 *
 * Снимок на диске компактный (индексы вместо строк), а генератору нужны быстрые
 * ответы на вопросы «какие слова годятся в эту категорию», «в какие категории
 * годится это слово», «какая категория может стать мета-ребёнком вот этой».
 * Здесь снимок один раз разворачивается в такие структуры.
 */
import type {
  Readiness, Snapshot, SnapshotCategory, SnapshotWord, StatusCode,
} from './types.ts';
import { STATUS } from './types.ts';

export interface Membership {
  word: number;
  category: number;
  status: StatusCode;
  fit: number;
  obviousness: number;
  relation: string;
  sense: number | null;
  /** игровая сложность связи; null в снимках 1.0 */
  gameplayDifficulty: number | null;
  /** маска risk-флагов; 0 в снимках 1.0 */
  riskMask: number;
}

/** Запрет пары категорий, как он приехал из базы. */
export interface CategoryConflict {
  a: number;
  b: number;
  type: string;
  severity: string | null;
  overlap: number;
}

export interface MetaCapable {
  /** категория, которая может стать мета-ребёнком */
  category: number;
  /** её имя как слово */
  word: number;
  /** категории, в которых это слово является правдоподобным членом */
  hosts: number[];
}

export class ContentIndex {
  readonly snapshot: Snapshot;
  readonly categories: SnapshotCategory[];
  readonly words: SnapshotWord[];
  readonly memberships: Membership[];

  private readonly byCategory: Membership[][];
  private readonly byWord: Membership[][];
  private readonly categoryKeyToIndex = new Map<string, number>();
  private readonly wordNormToIndex = new Map<string, number>();
  private readonly metaByCategory = new Map<number, MetaCapable>();
  private readonly labelWordToCategory = new Map<number, number>();
  /** запреты пар: ключ «меньший|больший индекс» */
  private readonly conflictByPair = new Map<string, CategoryConflict>();
  private readonly conflictsByCategory = new Map<number, CategoryConflict[]>();
  private readonly riskFlagNames: string[];

  constructor(snapshot: Snapshot) {
    this.snapshot = snapshot;
    this.categories = snapshot.categories;
    this.words = snapshot.words;
    this.riskFlagNames = snapshot.risk_flags ?? [];

    this.byCategory = Array.from({ length: this.categories.length }, () => []);
    this.byWord = Array.from({ length: this.words.length }, () => []);
    this.memberships = snapshot.memberships.map((row) => {
      const m: Membership = {
        word: row[0], category: row[1], status: row[2],
        fit: row[3], obviousness: row[4], relation: row[5], sense: row[6],
        gameplayDifficulty: row[7] ?? null, riskMask: row[8] ?? 0,
      };
      this.byCategory[m.category].push(m);
      this.byWord[m.word].push(m);
      return m;
    });

    this.categories.forEach((c, i) => this.categoryKeyToIndex.set(c.k, i));
    this.words.forEach((w, i) => this.wordNormToIndex.set(w.n, i));
    for (const mc of snapshot.meta_capable) {
      this.metaByCategory.set(mc.category, mc);
      this.labelWordToCategory.set(mc.word, mc.category);
    }

    const types = snapshot.conflict_types ?? ['do_not_pair'];
    for (const row of snapshot.conflicts ?? []) {
      const conflict: CategoryConflict = {
        a: row[0], b: row[1], type: types[row[2]] ?? 'do_not_pair',
        severity: row[3], overlap: row[4],
      };
      this.conflictByPair.set(pairKey(conflict.a, conflict.b), conflict);
      for (const side of [conflict.a, conflict.b]) {
        this.conflictsByCategory.set(side, [
          ...(this.conflictsByCategory.get(side) ?? []), conflict,
        ]);
      }
    }
  }

  get topFrequencyThreshold(): number {
    return this.snapshot.constants.top50k_zipf;
  }

  get quickwinThreshold(): number {
    return this.snapshot.constants.quickwin_zipf;
  }

  categoryIndex(key: string): number | undefined {
    return this.categoryKeyToIndex.get(key);
  }

  wordIndex(normalized: string): number | undefined {
    return this.wordNormToIndex.get(normalized);
  }

  /** Связи категории. `maxStatus` = 0 только approved, 1 включая alternative. */
  categoryMemberships(category: number, maxStatus: StatusCode = STATUS.approved): Membership[] {
    return this.byCategory[category].filter((m) => m.status <= maxStatus);
  }

  /** Связи слова — то есть все категории, куда оно правдоподобно годится. */
  wordMemberships(word: number, maxStatus: StatusCode = STATUS.alternative): Membership[] {
    return this.byWord[word].filter((m) => m.status <= maxStatus);
  }

  /** Может ли эта категория выступить мета-ребёнком, и у кого. */
  metaCapable(category: number): MetaCapable | undefined {
    return this.metaByCategory.get(category);
  }

  /** Если это слово — имя категории, вернуть её индекс. */
  categoryOfLabelWord(word: number): number | undefined {
    return this.labelWordToCategory.get(word);
  }

  zipf(word: number): number | null {
    return this.words[word].z;
  }

  isFrequencyUnknown(word: number): boolean {
    return this.words[word].u === 1;
  }

  /** Слово узнаваемо: частотность известна и не ниже границы top-50k. */
  isRecognizable(word: number): boolean {
    const z = this.words[word].z;
    return z !== null && z >= this.topFrequencyThreshold;
  }

  /** Слово годится в quick-win: частотное и с известной частотностью. */
  isQuickwinWord(word: number): boolean {
    const z = this.words[word].z;
    return z !== null && z >= this.quickwinThreshold;
  }

  /** Сколько approved-слов есть у категории — годится ли она вообще для уровня. */
  approvedCount(category: number): number {
    return this.byCategory[category].reduce(
      (n, m) => (m.status === STATUS.approved ? n + 1 : n), 0);
  }

  /** Готовность категории по базе. `unknown` для снимков 1.0, где поля нет. */
  readiness(category: number): Readiness {
    return this.categories[category].rd ?? 'unknown';
  }

  /**
   * Годится ли категория для автоматической сборки уровня.
   *
   * `curated_only` и `hard_only` в автосборку не идут: у первой правило парное
   * (OPPOSITES — это пары, а не пул, четвёрка собирается руками), у второй
   * нормальных слов нет вообще. `unknown` пропускаем, иначе снимок 1.0
   * перестал бы генерироваться целиком.
   */
  isAutoUsable(category: number): boolean {
    const readiness = this.readiness(category);
    return readiness === 'ready' || readiness === 'constrained' || readiness === 'unknown';
  }

  /** Запрет на пару категорий, если он объявлен в базе. */
  conflict(a: number, b: number): CategoryConflict | undefined {
    return this.conflictByPair.get(pairKey(a, b));
  }

  /** Все запреты, в которых участвует категория. */
  conflictsFor(category: number): CategoryConflict[] {
    return this.conflictsByCategory.get(category) ?? [];
  }

  get conflictCount(): number {
    return this.conflictByPair.size;
  }

  /** Имена risk-флагов связи: снимок хранит их битовой маской. */
  riskFlags(membership: Membership): string[] {
    if (!membership.riskMask) return [];
    return this.riskFlagNames.filter((_, bit) => (membership.riskMask & (1 << bit)) !== 0);
  }

  hasRiskFlag(membership: Membership, flag: string): boolean {
    const bit = this.riskFlagNames.indexOf(flag);
    return bit >= 0 && (membership.riskMask & (1 << bit)) !== 0;
  }
}

function pairKey(a: number, b: number): string {
  return a < b ? `${a}|${b}` : `${b}|${a}`;
}

export function loadContentIndex(snapshot: Snapshot): ContentIndex {
  return new ContentIndex(snapshot);
}
