/**
 * Индекс снимка контентной базы.
 *
 * Снимок на диске компактный (индексы вместо строк), а генератору нужны быстрые
 * ответы на вопросы «какие слова годятся в эту категорию», «в какие категории
 * годится это слово», «какая категория может стать мета-ребёнком вот этой».
 * Здесь снимок один раз разворачивается в такие структуры.
 */
import type { Snapshot, SnapshotCategory, SnapshotWord, StatusCode } from './types.ts';
import { STATUS } from './types.ts';

export interface Membership {
  word: number;
  category: number;
  status: StatusCode;
  fit: number;
  obviousness: number;
  relation: string;
  sense: number | null;
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

  constructor(snapshot: Snapshot) {
    this.snapshot = snapshot;
    this.categories = snapshot.categories;
    this.words = snapshot.words;

    this.byCategory = Array.from({ length: this.categories.length }, () => []);
    this.byWord = Array.from({ length: this.words.length }, () => []);
    this.memberships = snapshot.memberships.map((row) => {
      const m: Membership = {
        word: row[0], category: row[1], status: row[2],
        fit: row[3], obviousness: row[4], relation: row[5], sense: row[6],
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
}

export function loadContentIndex(snapshot: Snapshot): ContentIndex {
  return new ContentIndex(snapshot);
}
