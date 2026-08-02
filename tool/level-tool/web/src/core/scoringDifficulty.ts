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
    /** объявленные продуктовые веса: референс их не идентифицирует */
    declared: Record<string, number>;
    semantic: Record<string, number>;
    mechanical: Record<string, number>;
    headroom: { reference_ceiling: number };
    not_identified_by_reference?: unknown[];
  };
  calibration?: unknown;
  interest: { scoring_version: string; weights: Record<string, number>; composite_max: number };
}

/** Признаки уровня, по которым считается D_base. Ровно те, что есть в референсе. */
export interface BaseFeatures {
  /**
   * Категорий на уровне (F1 «масштаб» в levels/EVAL.md). В формулу входит не
   * само M, а `startBubbles` ниже — но в разбор оно обязано попадать числом:
   * это первое, что спрашивают про сложность уровня.
   */
  categories: number;
  /**
   * Размер уровня в словах: `4*M − мета`. Мета-слово не спавнится, поэтому
   * вычитается. Имя историческое и обманчивое — это НЕ 24 пузыря стартового
   * поля, а весь уровень целиком, включая очередь досыпки.
   */
  startBubbles: number;
  rareWords: number;
  veryRareWords: number;
  metaLinks: number;
  metaDepth: number;
  quickwinCategories: number;
  /**
   * Категории, представленные на стартовом поле ровно одним словом.
   *
   * Такой пузырь не сливается ни с чем: его пара ещё в очереди. Он занимает
   * место на поле и, главное, внимание — игрок перебирает его в каждой
   * гипотезе, а ход с ним невозможен по построению. Замер по 400 уровням: до
   * 11 категорий одиночек нет вовсе, на 13 их 4-7, на 16 уже 10-13 — то есть
   * до 62% поля не участвует в ходе. Это отдельная от объёма нагрузка:
   * два уровня с одинаковым числом слов, но разной раскладкой играются
   * по-разному.
   */
  loneStartWords: number;
  /** Слов на стартовом поле — знаменатель для доли «мёртвых» пузырей. */
  startFieldSize: number;
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
  // Раскладка старта. У спека без выкладки одиночек считать не из чего —
  // тогда фактор равен нулю, а не выдумывается из числа категорий.
  const onField = new Map<string, number>();
  for (const bubble of spec.deal?.start ?? []) {
    onField.set(bubble.category, (onField.get(bubble.category) ?? 0) + 1);
  }
  const startFieldSize = spec.deal?.start.length ?? 0;
  let lone = 0;
  for (const count of onField.values()) if (count === 1) lone += 1;

  return {
    categories: spec.categories.length,
    startBubbles: spec.board.startBubbles,
    rareWords: rare,
    veryRareWords: veryRare,
    metaLinks,
    metaDepth: Math.max(0, ...spec.categories.map((c) => c.metaDepth)),
    quickwinCategories: spec.categories.filter((c) => c.isQuickwin).length,
    loneStartWords: lone,
    startFieldSize,
  };
}

/**
 * Откалиброванная часть. Здесь ТОЛЬКО те признаки, чей вклад данные референса
 * реально идентифицируют: объём и редкость. Мета-связи, глубина и быстрые
 * победы сюда не входят — их вес по референсу измерить нельзя
 * (docs/SCORING.md §7), поэтому они живут в `declared`.
 */
export function difficultyBase(features: BaseFeatures, config: ScoringConfig): number {
  const w = config.difficulty.base;
  return (w.intercept ?? 0)
    + (w.start_bubbles ?? 0) * features.startBubbles
    + (w.rare_words ?? 0) * features.rareWords
    + (w.very_rare_words ?? 0) * features.veryRareWords;
}

/**
 * Ярус сложности для продукта: чистая функция от D, а не третья шкала.
 *
 * Границы согласованы с ролями кривой блока (targetDifficulty в blockPlan.ts):
 * передышки и туториалы попадают в easy, вход/рост/выход в medium, спайки и
 * пики (7.5+) в hard. Порог между medium и hard проходит по 7.0 — ровно там,
 * где кривая референса ставит спайки. Единственный источник правды о ярусе:
 * менять границы здесь, а не в местах употребления.
 */
export type DifficultyTier = 'easy' | 'medium' | 'hard';

export function difficultyTier(value: number): DifficultyTier {
  if (value < 4) return 'easy';
  if (value < 7) return 'medium';
  return 'hard';
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

  // ---------------- base: откалибровано на 199 уровнях ----------------
  const base: Record<string, number> = {
    // масштаб = число категорий: слов на уровне ровно 4*M − мета, поэтому
    // именно M и есть то, что этот вес меряет (F1 в levels/EVAL.md)
    'масштаб (категорий × 4 слова)': (w.base.start_bubbles ?? 0) * features.startBubbles,
    'редкие слова (zipf < 3)': (w.base.rare_words ?? 0) * features.rareWords,
    'очень редкие (zipf < 2)': (w.base.very_rare_words ?? 0) * features.veryRareWords,
  };
  const baseTotal = (w.base.intercept ?? 0)
    + Object.values(base).reduce((a, b) => a + b, 0);

  explanation.push(`${features.categories} категорий — это ${features.startBubbles} слов `
    + 'на уровне; масштаб растёт линейно по числу категорий и остаётся '
    + 'главным слагаемым сложности');
  explanation.push(`${features.rareWords} редких слов, из них ${features.veryRareWords} очень редких`);

  // ---------------- declared: объявлено, НЕ откалибровано ----------------
  const d = w.declared ?? {};
  const metaScore = Math.min(d.meta_link_max ?? 1.4,
    (d.meta_link ?? 0) * features.metaLinks);
  const depthScore = (d.meta_depth_beyond_1 ?? 0) * Math.max(0, features.metaDepth - 1);
  const quickwinScore = Math.max(d.quickwin_relief_max ?? -0.6,
    (d.quickwin_relief ?? 0) * features.quickwinCategories);
  // Раскладка старта. Вес объявленный по той же причине, что и мета: выкладку
  // считаем МЫ (core/deal.ts), в выгрузке референса её нет вовсе, значит
  // калибровать не на чем — но и молчать о ней нельзя.
  const loneScore = Math.min(d.lone_start_word_max ?? 1.0,
    (d.lone_start_word ?? 0) * features.loneStartWords);
  const declared: Record<string, number> = {
    'мета-связи (объявлено)': metaScore,
    'глубина мета сверх 1 (объявлено)': depthScore,
    'быстрые победы (объявлено)': quickwinScore,
    'одиночки на старте (объявлено)': loneScore,
  };
  const declaredTotal = Object.values(declared).reduce((a, b) => a + b, 0);

  if (features.metaLinks > 0) {
    explanation.push(`${features.metaLinks} мета-связей, максимальная глубина `
      + `${features.metaDepth}`
      + (features.metaDepth >= 3
        ? ' — глубина 3 в оригинале появляется только с L438 (замер 1025 уровней)'
        : '')
      + '. Вес объявлен, а не откалиброван: по референсу вклад мета не '
      + 'идентифицируется (см. SCORING §7)');
  }
  explanation.push(`${features.quickwinCategories} категорий быстрой победы снижают `
    + 'оценку на объявленную величину: дверь остаётся открытой');
  if (features.startFieldSize > 0) {
    const share = Math.round((features.loneStartWords / features.startFieldSize) * 100);
    explanation.push(features.loneStartWords === 0
      ? `на старте нет категорий-одиночек: каждый из ${features.startFieldSize} пузырей `
        + 'поля имеет пару и участвует в ходе'
      : `${features.loneStartWords} категорий лежат на старте одним словом — `
        + `${share}% поля не сливается ни с чем и работает отвлечением, `
        + 'а не материалом для хода');
  }

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
  const iced = spec.modifiers.frozenBubbles.length;
  const hidden = spec.modifiers.hiddenBubbles.length;
  const chainLine = spec.modifiers.chainLine !== null && spec.modifiers.chainLine !== undefined;
  // без лимита ходов тесноты нет вовсе, а не «теснота по K = 0»
  const tightness = spec.board.moveLimitK === null ? 0
    : (MAX_MOVE_LIMIT_K - spec.board.moveLimitK) / (MAX_MOVE_LIMIT_K - MIN_MOVE_LIMIT_K);
  const mechanical: Record<string, number> = {
    'цепи': Math.min(w.mechanical.modifier_max, w.mechanical.chain * chains),
    'половинки': Math.min(w.mechanical.modifier_max, w.mechanical.half_pair * halves),
    // лёд, «?» и цепь-линия — объявленные веса: в референсе этих механик нет,
    // калибровать нечем, и это подписано в конфиге и в интерфейсе
    'лёд (объявлено)': Math.min(w.mechanical.modifier_max, (w.mechanical.ice ?? 0.45) * iced),
    '«?» (объявлено)': Math.min(w.mechanical.modifier_max, (w.mechanical.hidden ?? 0.5) * hidden),
    'цепь-линия (объявлено)': chainLine ? (w.mechanical.chain_line ?? 0.5) : 0,
    'теснота лимита ходов': w.mechanical.move_tightness * Math.max(0, Math.min(1, tightness)),
  };
  const mechanicalTotal = Math.min(
    w.mechanical.modifier_max + w.mechanical.move_tightness,
    Object.values(mechanical).reduce((a, b) => a + b, 0));

  if (chains > 0) explanation.push(`${chains} цепи: аналитически проверяемый модификатор`);
  if (halves > 0) explanation.push(`${halves} распилов: склейка половинки тратит ход, `
    + 'лимит это учитывает');
  if (iced > 0) explanation.push(`${iced} замороженных пузыря: тают от мерджей `
    + '(вес объявлен, референсом не калиброван)');
  if (hidden > 0) explanation.push(`${hidden} скрытых «?» (вес объявлен, `
    + 'референсом не калиброван)');
  if (chainLine) explanation.push('цепь-линия делит поле '
    + `(снимается сбором ${spec.modifiers.chainLine?.need} категорий; вес объявлен)`);
  explanation.push(spec.board.moveLimit === null
    ? `лимита ходов нет (туториал), минимум мерджей ${spec.board.moveFloor}`
    : `лимит ходов ${spec.board.moveLimit} при минимуме ${spec.board.moveFloor} `
      + `(K = ${spec.board.moveLimitK})`);

  // ---------------- итог ----------------
  let value = baseTotal + declaredTotal + semanticTotal + mechanicalTotal;
  if (solutions && solutions.count !== 1) {
    // сложность нерешаемого или двусмысленного уровня не имеет смысла
    explanation.unshift(solutions.count === 0
      ? 'уровень нерешаем: оценка не выставляется'
      : 'уровень двусмыслен: две полные раскладки, оценка не выставляется');
    return {
      base, declared, semantic, mechanical,
      baseTotal, declaredTotal, semanticTotal, mechanicalTotal,
      value: 0, explanation, scoringVersion: config.scoring_version,
    };
  }

  value = Math.max(1, Math.min(10, Math.round(value * 2) / 2));   // шаг 0.5

  return {
    base, declared, semantic, mechanical,
    baseTotal, declaredTotal, semanticTotal, mechanicalTotal,
    value, explanation, scoringVersion: config.scoring_version,
  };
}
