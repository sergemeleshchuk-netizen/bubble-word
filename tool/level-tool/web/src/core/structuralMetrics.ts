/**
 * Структура задачи глазами игрока — то, чего в оценке D не хватало.
 *
 * Откуда взялись именно эти метрики. Разбор публичных данных по головоломкам
 * (см. docs/SCORING.md §11) даёт три вещи, которые мы не считали:
 *
 *   1. Трудность создаёт НЕ редкая лексика, а число одновременно живых гипотез.
 *      Частотность слова стоит игроку десятки миллисекунд узнавания; лишний
 *      правдоподобный кандидат на место в четвёрке роняет решаемость в разы.
 *   2. Лучший переносимый предиктор сложности в литературе по головоломкам —
 *      ветвление на первых ходах: сколько групп игрок может закрыть сразу.
 *      Уровень с одной очевидной группой на старте кардинально труднее уровня
 *      с четырьмя, при одинаковых словах.
 *   3. Уровень, который раскладывается чистой дедукцией без единого выбора, —
 *      это работа, а не головоломка: инсайту там взяться неоткуда.
 *
 * Метрики намеренно НЕ входят в число D и в число I. Они считаются, попадают
 * в отчёт и в валидатор, и служат материалом для следующей калибровки: сначала
 * измеряем, потом решаем веса. Смешивать измеренное и объявленное в одном
 * числе — ровно то, чего эта модель избегает с самого начала.
 */
import type { LevelSpec } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import { plausibleHomes } from './solutionCounter.ts';

export interface StructuralMetrics {
  /** слов, у которых на этом уровне два и более правдоподобных дома */
  multiHomeWords: number;
  /** самая оспариваемая категория: сколько кандидатов сверх её четвёрки */
  maxContestedSlots: number;
  /** категорий, которые можно закрыть сразу: все четыре слова однодомны */
  openingCategories: number;
  /** уровень раскладывается чистой дедукцией, без единого выбора наугад */
  deductionOnly: boolean;
  /** сколько слов дедукция расставляет до первой развилки */
  forcedSteps: number;
  /** объяснение словами: числа без интерпретации никому не помогают */
  explanation: string[];
}

export function computeStructuralMetrics(
  index: ContentIndex,
  spec: LevelSpec,
): StructuralMetrics {
  const items = plausibleHomes(index, spec);
  const slots = spec.categories.length;
  const perCategory = spec.board.wordsPerCategory;

  const multiHomeWords = items.filter((i) => i.plausible.length >= 2).length;

  // сколько слов правдоподобно тянет в каждую категорию
  const candidates = new Array<number>(slots).fill(0);
  for (const item of items) {
    for (const slot of item.plausible) candidates[slot] += 1;
  }
  const maxContestedSlots = Math.max(0,
    ...candidates.map((n) => n - perCategory));

  // категория «на открытие»: все её слова однодомны, собирается без гипотез
  const homeSingle = new Array<number>(slots).fill(0);
  for (const item of items) {
    if (item.plausible.length === 1) homeSingle[item.home] += 1;
  }
  const openingCategories = homeSingle.filter((n) => n >= perCategory).length;

  const { deductionOnly, forcedSteps } = deductionPass(items, slots, perCategory);

  const explanation: string[] = [
    `${multiHomeWords} слов с двумя и более правдоподобными домами`,
    openingCategories > 0
      ? `${openingCategories} категорий можно закрыть сразу, без гипотез`
      : 'ни одной категории нельзя закрыть сразу: первый ход — гипотеза',
    deductionOnly
      ? 'уровень раскладывается чистой дедукцией: развилок нет, инсайту взяться неоткуда'
      : `дедукция доходит до ${forcedSteps} из ${items.length} слов, дальше нужен выбор`,
  ];
  if (maxContestedSlots > 0) {
    explanation.push(`самая оспариваемая категория: ${maxContestedSlots} кандидатов `
      + `сверх своей четвёрки`);
  }

  return {
    multiHomeWords,
    maxContestedSlots,
    openingCategories,
    deductionOnly,
    forcedSteps,
    explanation,
  };
}

/**
 * Прогон чистой дедукции — тот способ рассуждения, который доступен игроку
 * без перебора наугад. Два правила, обе стороны одного и того же вывода:
 *
 *   у слова остался один возможный дом            → слово ставится туда;
 *   у категории ровно столько кандидатов, сколько мест → все они её.
 *
 * Если так расставляются все слова, уровень решается без единой развилки.
 * Перебор с возвратом здесь намеренно не используется: он умеет то, чего не
 * умеет человек, и как мера человеческой трудности бесполезен.
 */
function deductionPass(
  items: ReturnType<typeof plausibleHomes>,
  slots: number,
  perCategory: number,
): { deductionOnly: boolean; forcedSteps: number } {
  const options = items.map((i) => new Set(i.plausible));
  const assigned = new Array<number>(items.length).fill(-1);
  const free = new Array<number>(slots).fill(perCategory);
  let placed = 0;

  const place = (i: number, slot: number): void => {
    assigned[i] = slot;
    free[slot] -= 1;
    placed += 1;
    if (free[slot] === 0) {
      // категория заполнена — она больше не вариант ни для кого
      options.forEach((set, j) => { if (assigned[j] === -1) set.delete(slot); });
    }
  };

  let progress = true;
  while (progress && placed < items.length) {
    progress = false;

    // правило 1: у слова остался единственный дом
    for (let i = 0; i < items.length; i += 1) {
      if (assigned[i] !== -1 || options[i].size !== 1) continue;
      const slot = options[i].values().next().value as number;
      if (free[slot] <= 0) return { deductionOnly: false, forcedSteps: placed };
      place(i, slot);
      progress = true;
    }

    // правило 2: у категории ровно столько кандидатов, сколько осталось мест
    for (let slot = 0; slot < slots; slot += 1) {
      if (free[slot] <= 0) continue;
      const pool: number[] = [];
      for (let i = 0; i < items.length; i += 1) {
        if (assigned[i] === -1 && options[i].has(slot)) pool.push(i);
      }
      if (pool.length === free[slot]) {
        for (const i of pool) place(i, slot);
        progress = true;
      }
    }
  }

  return { deductionOnly: placed === items.length, forcedSteps: placed };
}
