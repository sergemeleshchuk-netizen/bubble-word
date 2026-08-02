/**
 * Профиль выкладки: КАК уровень лежит на поле, а не из чего он состоит.
 *
 * Два уровня одинакового размера играются по-разному, и разница — в раскладке.
 * Решение владельца продукта 03.08: сложность обязана видеть форму выкладки
 * целиком, а не только одиночек.
 *
 *   четвёрка на старте  категория видна вся — ход очевиден, это точка входа;
 *   тройка на старте    не хватает одного слова, гипотеза уже читается;
 *   пара                материал для хода есть, но категория ещё не угадана;
 *   одиночка            пузырь не сливается ни с чем: пара ещё в очереди.
 *                       Ход с ним невозможен по построению, а внимание он
 *                       забирает наравне с остальными — и чем таких больше,
 *                       тем ближе поле к состоянию «ходить некуда».
 *
 * Плюс динамика: досыпка либо приносит развязку (пачка открывает сбор), либо
 * только добавляет обрывков. Это меряет симулятор партии, а не арифметика
 * выкладки, поэтому цифры берутся оттуда.
 *
 * Модуль чистый: на вход спек, на выход числа. Поэтому его зовёт и оценка
 * сложности, и пересчёт сданных блоков (`scripts/rescore_block.ts`).
 */
import type { LevelSpec } from './types.ts';
import { simulatePlayability } from './simulatePlayability.ts';

export interface DealShape {
  /** категорий, лежащих на старте целиком (все 4 слова видны) */
  fullSets: number;
  /** категорий, у которых на старте 3 слова из 4 */
  triples: number;
  /** категорий с 2 словами на старте */
  pairs: number;
  /** категорий с ровно 1 словом на старте */
  singles: number;
  /** категорий, которых на старте нет вовсе: они целиком в очереди досыпки */
  absent: number;
  /** пузырей на стартовом поле — знаменатель для долей */
  startFieldSize: number;
  /** волн досыпки за партию */
  refillWaves: number;
  /** волн, сразу открывших сбор новой категории */
  refillCompletions: number;
  /**
   * Доля продуктивных волн, 0..1. У уровня без досыпки (весь уровень на поле,
   * как туториал L1) волн нет — доля считается единицей: досыпка не подводила,
   * потому что и не требовалась. Ноль здесь означал бы «уровень ведёт себя
   * плохо», а это не так.
   */
  refillCompletionShare: number;
}

/** Сколько слов каждой категории лежит на стартовом поле. */
function startCounts(spec: LevelSpec): Map<string, number> {
  const counts = new Map<string, number>();
  for (const c of spec.categories) counts.set(c.key, 0);
  for (const bubble of spec.deal?.start ?? []) {
    counts.set(bubble.category, (counts.get(bubble.category) ?? 0) + 1);
  }
  return counts;
}

export function dealShape(spec: LevelSpec): DealShape {
  const counts = startCounts(spec);
  const full = spec.board.wordsPerCategory || 4;

  let fullSets = 0;
  let triples = 0;
  let pairs = 0;
  let singles = 0;
  let absent = 0;
  for (const c of spec.categories) {
    // мета-слово не спавнится, поэтому «вся категория на поле» для мета-родителя
    // означает на одно слово меньше: считаем от числа спавнящихся слов
    const spawnable = c.words.filter((w) => w.kind !== 'meta').length;
    const n = counts.get(c.key) ?? 0;
    if (n === 0) { absent += 1; continue; }
    if (n >= Math.min(full, spawnable)) { fullSets += 1; continue; }
    if (n === 3) { triples += 1; continue; }
    if (n === 2) { pairs += 1; continue; }
    singles += 1;
  }

  const play = simulatePlayability(spec);
  const share = play.refillWaves === 0 ? 1
    : play.refillCompletions / play.refillWaves;

  return {
    fullSets, triples, pairs, singles, absent,
    startFieldSize: spec.deal?.start.length ?? 0,
    refillWaves: play.refillWaves,
    refillCompletions: play.refillCompletions,
    refillCompletionShare: share,
  };
}
