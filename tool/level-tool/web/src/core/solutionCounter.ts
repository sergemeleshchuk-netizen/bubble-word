/**
 * Сколько у уровня глобальных решений.
 *
 * Это сильнее проверки «каждое слово записано в одной категории». База на атрибутах
 * делает слова многодомными по замыслу: слово может правдоподобно годиться и в свою
 * категорию, и в соседнюю. Вопрос не «есть ли у слова один дом по нашей разметке»,
 * а «существует ли ВТОРАЯ полная раскладка всех слов уровня по всем категориям,
 * при которой каждое слово стоит там, где оно правдоподобно».
 *
 *   0 решений  → уровень сломан;
 *   1 решение  → PASS;
 *   2+         → семантически двусмыслен, игрок может быть прав по-своему.
 *
 * Считаем максимум до двух: найти второе решение достаточно, чтобы забраковать.
 */
import type { LevelSpec, SolutionCount } from './types.ts';
import { STATUS } from './types.ts';
import type { ContentIndex } from './snapshot.ts';

const NODE_LIMIT = 200000;

export function countSolutions(index: ContentIndex, spec: LevelSpec): SolutionCount {
  const catKeys = spec.categories.map((c) => c.key);
  const catIndices = catKeys.map((k) => index.categoryIndex(k));
  const slotOf = new Map<string, number>();
  catKeys.forEach((k, i) => slotOf.set(k, i));

  // мета-связь структурна: имя ребёнка лежит в родителе по построению уровня,
  // и другого дома у этого пузыря быть не может
  const forcedSlot = new Map<number, number>();

  interface Item { word: number; text: string; plausible: number[] }
  const items: Item[] = [];

  spec.categories.forEach((category, slot) => {
    for (const word of category.words) {
      const wi = index.wordIndex(word.text.toLowerCase());
      if (wi === undefined) {
        items.push({ word: -1, text: word.text, plausible: [slot] });
        continue;
      }
      if (word.kind === 'meta') {
        forcedSlot.set(wi, slot);
        items.push({ word: wi, text: word.text, plausible: [slot] });
        continue;
      }
      const plausible: number[] = [];
      for (const m of index.wordMemberships(wi, STATUS.alternative)) {
        const target = catIndices.indexOf(m.category);
        if (target >= 0) plausible.push(target);
      }
      if (!plausible.includes(slot)) plausible.push(slot);
      items.push({ word: wi, text: word.text, plausible: Array.from(new Set(plausible)) });
    }
  });

  // самые ограниченные слова первыми: дерево перебора схлопывается на однодомных
  items.sort((a, b) => a.plausible.length - b.plausible.length
    || (a.text < b.text ? -1 : 1));

  const capacity = spec.categories.map(() => spec.board.wordsPerCategory);
  const assignment: number[] = new Array(items.length).fill(-1);
  let found = 0;
  let nodes = 0;
  let exhausted = true;
  let secondExample: SolutionCount['secondSolutionExample'];
  const firstSignature: string[] = [];

  const feasible = (from: number): boolean => {
    // сколько ещё нераспределённых слов могут попасть в каждую категорию
    const reach = capacity.map(() => 0);
    for (let i = from; i < items.length; i += 1) {
      for (const slot of items[i].plausible) reach[slot] += 1;
    }
    return capacity.every((need, slot) => need <= reach[slot]);
  };

  const snapshotAssignment = (): { category: string; words: string[] }[] => {
    const buckets: string[][] = spec.categories.map(() => []);
    items.forEach((item, i) => buckets[assignment[i]].push(item.text));
    return spec.categories.map((c, i) => ({ category: c.key, words: buckets[i].sort() }));
  };

  const dfs = (i: number): boolean => {
    nodes += 1;
    if (nodes > NODE_LIMIT) { exhausted = false; return true; }
    if (i === items.length) {
      found += 1;
      if (found === 1) {
        firstSignature.push(...snapshotAssignment().map((s) => `${s.category}:${s.words.join(',')}`));
      } else {
        secondExample = snapshotAssignment();
      }
      return found >= 2;
    }
    if (!feasible(i)) return false;

    for (const slot of items[i].plausible) {
      if (capacity[slot] === 0) continue;
      capacity[slot] -= 1;
      assignment[i] = slot;
      if (dfs(i + 1)) return true;
      capacity[slot] += 1;
      assignment[i] = -1;
    }
    return false;
  };

  dfs(0);

  return {
    count: Math.min(found, 2) as 0 | 1 | 2,
    nodesVisited: nodes,
    exhausted,
    secondSolutionExample: secondExample,
  };
}
