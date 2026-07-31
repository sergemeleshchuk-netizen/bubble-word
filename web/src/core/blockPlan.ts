/**
 * План блока из 10 уровней.
 *
 * Блок — не десять монотонно растущих уровней, а композиция с ритмом. В референсе
 * 74 перехода из 198 идут ВНИЗ (37%), а разброс внутри любого окна из десяти
 * уровней стабильно 5-7 категорий. Провал сразу после пика читается как
 * запрограммированная передышка — тяжёлый уровень, затем лёгкий как награда.
 *
 * Профиль задаётся настройками. Дефолтный пресет воспроизводит найденный ритм.
 */
import type { BlockConfig, LevelPlan, LevelRole } from './types.ts';
import { MAX_MOVE_LIMIT_K, MIN_MOVE_LIMIT_K } from './levelMath.ts';

/**
 * Дефолтный пресет для 201-210.
 *
 * Числа категорий и мета взяты из спеки (они построены по ритму референса),
 * но стартовые пузыри здесь НЕ задаются: спека содержала в них 7 ошибок из 10.
 * Пузыри считает `startBubbles()` из числа категорий и мета.
 */
export const DEFAULT_BLOCK_CONFIG: BlockConfig = {
  levelRange: [201, 210],
  categoryCorridor: [11, 18],
  spikePositions: [5, 9],
  recoveryPositions: [3, 6, 10],
  rarityRange: [9, 13],
  maxMetaDepth: 3,
  allowedModifiers: ['chains'],
  includeThemes: [],
  excludeThemes: [],
  trapThemes: [],
  wordFreshnessWindow: 30,
  categoryFreshnessWindow: 40,
  wordsPerCategory: 4,
  seed: 'bb-201-210-v1',
  categoryPlan: [13, 15, 12, 16, 18, 12, 14, 15, 17, 13],
  metaPlan: [2, 3, 1, 4, 5, 1, 3, 2, 4, 2],
};

function roleFor(position: number, total: number, config: BlockConfig): LevelRole {
  if (position === 1) return 'entry';
  if (position === total) return 'exit';
  if (config.spikePositions.includes(position)) {
    // самый нагруженный спайк называем пиком, остальные — спайками
    const peak = config.spikePositions.reduce((best, p) => {
      const plan = config.categoryPlan;
      if (!plan) return Math.max(best, p);
      return plan[p - 1] > plan[best - 1] ? p : best;
    }, config.spikePositions[0]);
    return position === peak ? 'peak' : 'spike';
  }
  if (config.recoveryPositions.includes(position)) return 'recovery';
  return 'growth';
}

/** Число категорий для позиции, если явного плана нет. */
function derivedCategoryCount(
  role: LevelRole, position: number, total: number, config: BlockConfig,
): number {
  const [lo, hi] = config.categoryCorridor;
  const mid = Math.round((lo + hi) / 2);
  switch (role) {
    case 'peak': return hi;
    case 'spike': return hi - 1;
    case 'recovery': return lo;
    case 'entry': return mid;
    case 'exit': return mid;
    default: {
      // плавный подъём между передышками
      const ramp = position / total;
      return Math.min(hi - 1, Math.round(lo + (hi - lo) * ramp));
    }
  }
}

/** Мета-связей для позиции, если явного плана нет. */
function derivedMetaCount(role: LevelRole, categoryCount: number, config: BlockConfig): number {
  if (config.maxMetaDepth <= 0) return 0;
  const dense = Math.round(categoryCount * 0.28);
  switch (role) {
    case 'recovery': return Math.min(1, dense);
    case 'peak': return dense;
    case 'spike': return Math.max(1, dense - 1);
    case 'entry': return Math.max(1, Math.round(dense * 0.6));
    case 'exit': return Math.max(1, Math.round(dense * 0.6));
    default: return Math.max(1, Math.round(dense * 0.8));
  }
}

/** Глубина мета-леса: 3 — рычаг, которого в референсе нет ни разу. */
function metaDepthTarget(role: LevelRole, metaCount: number, config: BlockConfig): number {
  if (metaCount === 0) return 0;
  const cap = config.maxMetaDepth;
  if (role === 'peak') return Math.min(cap, 2);
  // ровно один уровень блока получает максимальную глубину — демонстрация рычага,
  // а не ставка на непроверенную в целевой игре механику (DECISION_LOG §9)
  if (role === 'spike') return Math.min(cap, 3);
  if (role === 'recovery') return 1;
  return Math.min(cap, metaCount >= 3 ? 2 : 1);
}

function targetDifficulty(role: LevelRole): [number, number] {
  switch (role) {
    case 'entry': return [5.5, 6.5];
    case 'growth': return [6.0, 7.5];
    case 'recovery': return [4.0, 5.5];
    case 'peak': return [8.0, 9.0];
    case 'spike': return [7.5, 8.5];
    case 'exit': return [5.0, 6.5];
  }
}

/**
 * Целевая интересность.
 *
 * Ключевое требование: интересность обязана уметь падать, когда сложность растёт,
 * иначе это одна шкала с двумя названиями. Поэтому у передышки и выхода целевая
 * интересность ВЫШЕ, чем у пика: лёгкий уровень имеет право быть самым приятным.
 */
function targetInterest(role: LevelRole): [number, number] {
  switch (role) {
    case 'entry': return [6.5, 8.0];
    case 'growth': return [6.0, 8.0];
    case 'recovery': return [7.0, 9.0];
    case 'peak': return [6.5, 8.0];
    case 'spike': return [6.0, 7.5];
    case 'exit': return [7.5, 9.0];
  }
}

/** K лимита ходов: чем тяжелее роль, тем теснее проход. */
function moveLimitK(role: LevelRole): number {
  switch (role) {
    case 'recovery': return MAX_MOVE_LIMIT_K;
    case 'entry': return 1.45;
    case 'exit': return 1.5;
    case 'growth': return 1.35;
    case 'peak': return MIN_MOVE_LIMIT_K;
    case 'spike': return 1.3;
  }
}

export function buildBlockPlan(config: BlockConfig): LevelPlan[] {
  const [from, to] = config.levelRange;
  const total = to - from + 1;
  const [rareLo, rareHi] = config.rarityRange;

  const plans: LevelPlan[] = [];
  for (let position = 1; position <= total; position += 1) {
    const role = roleFor(position, total, config);
    const categoryCount = config.categoryPlan?.[position - 1]
      ?? derivedCategoryCount(role, position, total, config);
    const metaCount = config.metaPlan?.[position - 1]
      ?? derivedMetaCount(role, categoryCount, config);

    // редкость — единственный признак референса, который рос до самого конца
    // и не разворачивался; растим её вместе с ролью, а не с номером уровня
    const load = role === 'peak' ? 1 : role === 'spike' ? 0.9
      : role === 'recovery' ? 0.15 : role === 'growth' ? 0.6 : 0.3;
    const rareTarget = Math.round(rareLo + (rareHi - rareLo) * load);

    const trapTarget = role === 'recovery' ? 0
      : role === 'peak' ? 2 : role === 'spike' ? 2 : 1;

    // Модификатор — акцент, а не фон: цепи ставятся только на пики. Когда они
    // стояли на каждом уровне роста, верх шкалы сложности схлопывался (четыре
    // уровня подряд упирались в 9.5-10) и терялась разрешающая способность.
    const chainCount = config.allowedModifiers.includes('chains')
      ? (role === 'peak' ? 2 : role === 'spike' ? 1 : 0)
      : 0;

    plans.push({
      levelId: from + position - 1,
      position,
      role,
      categoryCount,
      metaCount: Math.min(metaCount, categoryCount - 1),
      metaDepthTarget: metaDepthTarget(role, metaCount, config),
      rareTarget,
      trapTarget,
      chainCount,
      targetDifficulty: targetDifficulty(role),
      targetInterest: targetInterest(role),
      moveLimitK: moveLimitK(role),
    });
  }
  return plans;
}

/**
 * Инварианты блока: пила, а не линия.
 * Проверяются на плане, до генерации: если план плохой, генерировать бессмысленно.
 */
export function checkBlockRhythm(plans: LevelPlan[]): { passed: boolean; issues: string[] } {
  const issues: string[] = [];
  const counts = plans.map((p) => p.categoryCount);

  const descents = counts.slice(1).filter((c, i) => c < counts[i]).length;
  if (descents < 3) {
    issues.push(`переходов вниз ${descents}, нужно минимум 3: блок читается как прямая линия, `
      + 'а в референсе 37% уровней проще предыдущего');
  }

  const spread = Math.max(...counts) - Math.min(...counts);
  if (spread < 4) {
    issues.push(`разброс внутри блока ${spread} категорий, в референсе стабильно 5-7`);
  }

  const peaks = plans.filter((p) => p.role === 'peak' || p.role === 'spike');
  if (peaks.length < 2) issues.push('меньше двух выраженных пиков');

  for (const peak of peaks) {
    const next = plans.find((p) => p.position === peak.position + 1);
    if (next && next.categoryCount >= peak.categoryCount) {
      issues.push(`после пика на позиции ${peak.position} нет передышки: `
        + `уровень ${next.levelId} не проще`);
    }
  }

  for (let i = 1; i < plans.length; i += 1) {
    const a = plans[i - 1];
    const b = plans[i];
    if (a.categoryCount === b.categoryCount && a.metaCount === b.metaCount) {
      issues.push(`уровни ${a.levelId} и ${b.levelId} структурно одинаковы`);
    }
  }

  return { passed: issues.length === 0, issues };
}
