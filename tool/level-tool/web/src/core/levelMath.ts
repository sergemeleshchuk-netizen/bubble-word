/**
 * Арифметика уровня — одно место на весь проект.
 *
 * В спеке пресет 201-210 содержал 7 ошибок в числе стартовых пузырей из 10 строк
 * (SPEC_AUDIT §1). Причина в том, что это число вводилось руками рядом с формулой.
 * Здесь оно вычисляется, и нигде больше не задаётся.
 */

/** Одновременно на поле в целевой игре (наблюдение, TARGET_GAME_OBSERVATIONS §2). */
export const BOARD_CAPACITY = 24;

/**
 * Пузырей на старте. Мета-слово не спавнится: оно появляется только после
 * схлопывания дочерней категории, поэтому вычитается.
 */
export function startBubbles(
  categoryCount: number, metaCount: number, wordsPerCategory = 4,
): number {
  return categoryCount * wordsPerCategory - metaCount;
}

/**
 * Минимум ходов: чтобы собрать категорию из 4 слов, нужно 3 мерджа.
 * Плюс по мерджу на склейку каждой половинки.
 */
export function moveFloor(
  categoryCount: number, halfSplits = 0, wordsPerCategory = 4,
): number {
  return categoryCount * (wordsPerCategory - 1) + halfSplits;
}

/**
 * Лимит ходов = минимум × K.
 *
 * K наблюдался в целевой игре на 18 уровнях: ~1.6 на просторных, ~1.3 на обычных,
 * ~1.25 на hard, где у игрока реально кончились ходы. Ниже 1.25 не опускаемся:
 * ошибочный мердж ТРАТИТ ход (GDD §2 п.3, прототип исполняет с 02.08), поэтому
 * запас сверх минимума — это и есть бюджет ошибок игрока; при K = 1.1 честный
 * игрок с одной-двумя опечатками проваливал бы спайк. Симулятор проходимости
 * играет без ошибок: его «запас ходов» и означает, сколько промахов уровень
 * прощает живому игроку.
 */
export const MIN_MOVE_LIMIT_K = 1.25;
export const MAX_MOVE_LIMIT_K = 1.6;

export function moveLimit(floor: number, k: number): number {
  const safeK = Math.min(MAX_MOVE_LIMIT_K, Math.max(MIN_MOVE_LIMIT_K, k));
  return Math.ceil(floor * safeK);
}

/** Сколько волн досыпки понадобится: пузырей больше, чем помещается на поле. */
export function refillWaves(bubbles: number, capacity = BOARD_CAPACITY): number {
  return Math.max(0, Math.ceil(bubbles / capacity) - 1);
}
