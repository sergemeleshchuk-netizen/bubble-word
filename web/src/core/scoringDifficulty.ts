/**
 * Модель сложности D.
 *
 * Три части с РАЗНЫМИ источниками истины — это главное исправление спеки
 * (SPEC_AUDIT §3). Смешивать их нельзя: одна калибруется по данным, две другие нет.
 *
 *   D_base       структура уровня. Калибруется на 199 референсных уровнях.
 *   D_semantic   двусмысленность. Признаков F3/F5/F7 в выгрузке НЕТ — калибруется
 *                контролируемыми парами уровней и прогонами решателя.
 *   D_mechanical модификаторы и теснота лимита ходов. Калибруется эмулятором.
 *
 *   D = clamp(D_base + semantic + mechanical, 1, 10)
 *
 * Каждое слагаемое попадает в разбивку с объяснением: задание требует не только
 * число, но и из чего оно складывается.
 */
import type { DifficultyBreakdown, LevelSpec, SolutionCount } from './types.ts';
import { STATUS } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import { MAX_MOVE_LIMIT_K, MIN_MOVE_LIMIT_K } from './levelMath.ts';

export interface ScoringConfig {
  scoring_version: string;
  calibrated: boolean;
  difficulty: {
    base: Record<string, number>;
    semantic: Record<string, number>;
    mechanical: Record<string, number>;
    headroom: { reference_ceiling: number };
  };
  interest: { scoring_version: string; weights: Record<string, number>; composite_max: number };
}

/** Признаки уровня, по которым считается D_base. Ровно те, что есть в референсе. */
export interface BaseFeatures {
  startBubbles: number;
  rareWords: number;
  veryRareWords: number;
  metaLinks: number;
  metaDepth: number;
  quickwinCategories: number;
}

export function baseFeaturesOf(spec: LevelSpec): BaseFeatures {
  let rare = 0;
  let veryRare = 0;
  let metaLinks = 0;
  for (const category of spec.categories) {
    for (const word of category.words) {
      if (word.kind === 'meta') { metaLinks += 1; continue; }
      if (word.zipf !== null && word.zipf < 3.0) rare += 1;
      if (word.zipf !== null && word.zipf < 2.0) veryRare += 1;
    }
  }
  return {
    startBubbles: spec.board.startBubbles,
    rareWords: rare,
    veryRareWords: veryRare,
    metaLinks,
    metaDepth: Math.max(0, ...spec.categories.map((c) => c.metaDepth)),
    quickwinCategories: spec.categories.filter((c) => c.isQuickwin).length,
  };
}

export function difficultyBase(features: BaseFeatures, config: ScoringConfig): number {
  const w = config.difficulty.base;
  return (w.intercept ?? 0)
    + w.start_bubbles * features.startBubbles
    + w.rare_words * features.rareWords
    + w.very_rare_words * features.veryRareWords
    + w.meta_links * features.metaLinks
    + w.meta_depth * features.metaDepth
    + w.quickwin_categories * features.quickwinCategories;
}

export interface SemanticEvidence {
  /** сомнения решателя ВНЕ заявленных ловушек: только из прогона режима B */
  unplannedHesitations?: number;
  /** ловушки, на которых решатель реально споткнулся */
  confirmedTraps?: string[];
}

export function computeDifficulty(
  spec: LevelSpec,
  index: ContentIndex,
  config: ScoringConfig,
  solutions?: SolutionCount,
  evidence: SemanticEvidence = {},
): DifficultyBreakdown {
  const features = baseFeaturesOf(spec);
  const w = config.difficulty;
  const explanation: string[] = [];

  // ---------------- base ----------------
  const base: Record<string, number> = {
    'объём (пузырей на старте)': w.base.start_bubbles * features.startBubbles,
    'редкие слова (zipf < 3)': w.base.rare_words * features.rareWords,
    'очень редкие (zipf < 2)': w.base.very_rare_words * features.veryRareWords,
    'мета-связи': w.base.meta_links * features.metaLinks,
    'глубина мета': w.base.meta_depth * features.metaDepth,
    'категории быстрой победы': w.base.quickwin_categories * features.quickwinCategories,
  };
  const baseTotal = (w.base.intercept ?? 0)
    + Object.values(base).reduce((a, b) => a + b, 0);

  explanation.push(`${features.startBubbles} пузырей на старте `
    + `при ${spec.categories.length} категориях`);
  if (features.metaLinks > 0) {
    explanation.push(`${features.metaLinks} мета-связей, максимальная глубина ${features.metaDepth}`
      + (features.metaDepth >= 3 ? ' — глубины 3 в референсе нет ни разу' : ''));
  }
  explanation.push(`${features.rareWords} редких слов, из них ${features.veryRareWords} очень редких`);
  explanation.push(`${features.quickwinCategories} категорий быстрой победы снижают оценку: `
    + 'дверь остаётся открытой');

  // ---------------- semantic ----------------
  // ловушка засчитывается, если она настоящая и тихая: связь есть, но неочевидна
  const strongTraps = spec.traps.filter((t) => t.decoyFit >= 0.6 && t.decoyObviousness <= 0.55);
  const confirmed = evidence.confirmedTraps?.length ?? strongTraps.length;
  const trapScore = Math.min(w.semantic.trap_max, w.semantic.confirmed_trap * confirmed);

  // смежность: пара категорий одной темы на одном уровне
  const themeCounts = new Map<string, number>();
  for (const c of spec.categories) themeCounts.set(c.theme, (themeCounts.get(c.theme) ?? 0) + 1);
  const adjacentPairs = Array.from(themeCounts.values())
    .reduce((n, count) => n + (count * (count - 1)) / 2, 0);
  const adjacencyScore = Math.min(w.semantic.adjacent_max,
    w.semantic.adjacent_pair * adjacentPairs);

  const unplanned = evidence.unplannedHesitations ?? 0;
  const unplannedScore = Math.min(w.semantic.unplanned_max,
    w.semantic.unplanned_hesitation * unplanned);

  const semantic: Record<string, number> = {
    'подтверждённые ловушки': trapScore,
    'смежность категорий': adjacencyScore,
    'незапланированная спорность': unplannedScore,
  };
  const semanticTotal = Object.values(semantic).reduce((a, b) => a + b, 0);

  if (confirmed > 0) {
    explanation.push(`${confirmed} ловушек: слово с одним домом при наличии на поле `
      + 'второй правдоподобной категории');
  }
  if (adjacentPairs > 0) {
    explanation.push(`${adjacentPairs} пар категорий из одной тематической сферы`);
  }
  if (evidence.unplannedHesitations === undefined) {
    explanation.push('незапланированная спорность не измерена: нужен прогон слепого решателя');
  }

  // ---------------- mechanical ----------------
  const chains = spec.modifiers.chains.length;
  const halves = spec.halves.length;
  const tightness = (MAX_MOVE_LIMIT_K - spec.board.moveLimitK)
    / (MAX_MOVE_LIMIT_K - MIN_MOVE_LIMIT_K);
  const mechanical: Record<string, number> = {
    'цепи': Math.min(w.mechanical.modifier_max, w.mechanical.chain * chains),
    'половинки': Math.min(w.mechanical.modifier_max, w.mechanical.half_pair * halves),
    'теснота лимита ходов': w.mechanical.move_tightness * Math.max(0, Math.min(1, tightness)),
  };
  const mechanicalTotal = Math.min(
    w.mechanical.modifier_max + w.mechanical.move_tightness,
    Object.values(mechanical).reduce((a, b) => a + b, 0));

  if (chains > 0) explanation.push(`${chains} цепи: аналитически проверяемый модификатор`);
  explanation.push(`лимит ходов ${spec.board.moveLimit} при минимуме ${spec.board.moveFloor} `
    + `(K = ${spec.board.moveLimitK})`);

  // ---------------- итог ----------------
  let value = baseTotal + semanticTotal + mechanicalTotal;
  if (solutions && solutions.count !== 1) {
    // сложность нерешаемого или двусмысленного уровня не имеет смысла
    explanation.unshift(solutions.count === 0
      ? 'уровень нерешаем: оценка не выставляется'
      : 'уровень двусмыслен: две полные раскладки, оценка не выставляется');
    return {
      base, semantic, mechanical, baseTotal, semanticTotal, mechanicalTotal,
      value: 0, explanation, scoringVersion: config.scoring_version,
    };
  }

  value = Math.max(1, Math.min(10, Math.round(value * 2) / 2));   // шаг 0.5

  return {
    base, semantic, mechanical, baseTotal, semanticTotal, mechanicalTotal,
    value, explanation, scoringVersion: config.scoring_version,
  };
}
