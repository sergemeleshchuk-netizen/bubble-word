/**
 * Детерминированная случайность.
 *
 * Генератору нужен произвольный, но воспроизводимый порядок перебора. Math.random
 * это ломает: один и тот же конфиг давал бы разные уровни, и брак нельзя было бы
 * воспроизвести. Поэтому seed → поток чисел, зависящий только от строки seed.
 */

/** Хеш строки в 32-битное семя (FNV-1a). */
function seedFromString(seed: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < seed.length; i += 1) {
    h ^= seed.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}

export interface Rng {
  /** следующее число в [0, 1) */
  next(): number;
  /** целое в [0, n) */
  int(n: number): number;
  /** перемешивание копии массива */
  shuffle<T>(items: readonly T[]): T[];
  /** случайный элемент */
  pick<T>(items: readonly T[]): T;
  /** стабильный вес элемента: не зависит от порядка вызовов */
  stableWeight(key: string): number;
}

/** mulberry32: короткий, быстрый, с достаточным качеством для перебора. */
export function createRng(seed: string): Rng {
  let state = seedFromString(seed);

  const next = (): number => {
    state = (state + 0x6d2b79f5) >>> 0;
    let t = state;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };

  const int = (n: number): number => Math.floor(next() * n);

  return {
    next,
    int,
    shuffle<T>(items: readonly T[]): T[] {
      const out = items.slice();
      for (let i = out.length - 1; i > 0; i -= 1) {
        const j = int(i + 1);
        [out[i], out[j]] = [out[j], out[i]];
      }
      return out;
    },
    pick<T>(items: readonly T[]): T {
      return items[int(items.length)];
    },
    stableWeight(key: string): number {
      // отдельный поток: используется как tie-breaker, поэтому не должен
      // зависеть от того, сколько раз до него дёрнули next()
      return seedFromString(`${seed}::${key}`) / 4294967296;
    },
  };
}
