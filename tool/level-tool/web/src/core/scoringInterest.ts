/**
 * Модель интересности I.
 *
 * У сложности есть эталон: решатель либо ошибся, либо нет. У интересности эталона
 * не существует — и это её главная слабость. Решение: эталоном становится
 * зафиксированное суждение продакта на калибровочном наборе. Тогда I — не мнение,
 * а МОДЕЛЬ мнения, которую можно проверить и опровергнуть.
 *
 * Четыре композита вместо десяти факторов (SPEC_AUDIT §5): десять весов на
 * 15 ручных оценок — гарантированное переобучение. Каждый композит 0..2.5.
 *
 *   I = Clarity + Variety + Aha + Freshness
 *
 * Жёсткое требование: интересность обязана уметь ПАДАТЬ, когда сложность растёт.
 * Если обе шкалы всегда двигаются вместе — это одна шкала с двумя названиями.
 */
import type { InterestBreakdown, LevelSpec, SolutionCount } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import type { ScoringConfig } from './scoringDifficulty.ts';

export interface InterestEvidence {
  /** доля слов, новых для пакета: считается по истории, 0..1 */
  newWordShare?: number;
  /** сомнения решателя вне замысла — прямой штраф к Clarity */
  unplannedHesitations?: number;
  /** ловушки, на которых решатель споткнулся, но пришёл к верному ответу */
  confirmedTraps?: number;
}

const MAX = 2.5;

function clamp(value: number): number {
  return Math.max(0, Math.min(MAX, value));
}

export function computeInterest(
  spec: LevelSpec,
  index: ContentIndex,
  config: ScoringConfig,
  solutions?: SolutionCount,
  evidence: InterestEvidence = {},
): InterestBreakdown {
  const explanation: string[] = [];
  const weights = config.interest.weights;

  const plainWords = spec.categories.flatMap((c) =>
    c.words.filter((w) => w.kind === 'word'));

  // ---------------- Clarity ----------------
  // слова узнаваемы, связи объяснимы, нет нечестной многозначности
  const recognizable = plainWords.filter((w) =>
    w.zipf !== null && w.zipf >= index.topFrequencyThreshold).length;
  const recognizableShare = plainWords.length ? recognizable / plainWords.length : 1;

  const obviousnessValues = plainWords.map((w) => w.obviousness ?? 0.7);
  const meanObviousness = obviousnessValues.length
    ? obviousnessValues.reduce((a, b) => a + b, 0) / obviousnessValues.length : 0.7;

  // категория, где два и более очень редких слова, — натужная
  const strainedCategories = spec.categories.filter((c) =>
    c.words.filter((w) => w.zipf !== null && w.zipf < 2.5).length >= 2).length;

  let clarity = MAX * (0.55 * recognizableShare + 0.45 * meanObviousness);
  clarity -= strainedCategories * 0.35;
  clarity -= (evidence.unplannedHesitations ?? 0) * 0.4;
  if (solutions && solutions.count >= 2) clarity = 0;      // нечестная двусмысленность
  clarity = clamp(clarity);

  explanation.push(`Clarity ${clarity.toFixed(2)}: узнаваемых слов `
    + `${(recognizableShare * 100).toFixed(0)}%, средняя очевидность связи `
    + `${meanObviousness.toFixed(2)}`
    + (strainedCategories ? `, натужных категорий ${strainedCategories}` : ''));

  // ---------------- Variety ----------------
  // разные типы связи и разные сферы жизни; десять однотипных таксономий — скучно
  const relations = new Set(plainWords.map((w) => w.relation).filter(Boolean));
  const themes = new Set(spec.categories.map((c) => c.theme));
  const relationVariety = Math.min(1, relations.size / 5);
  const themeVariety = Math.min(1, themes.size / Math.max(4, spec.categories.length * 0.6));

  // однотипность: больше половины категорий одного типа связи
  const relationCounts = new Map<string, number>();
  for (const c of spec.categories) {
    const dominant = c.words.find((w) => w.relation)?.relation ?? c.key;
    relationCounts.set(dominant, (relationCounts.get(dominant) ?? 0) + 1);
  }
  const dominantShare = Math.max(...relationCounts.values()) / spec.categories.length;
  let variety = MAX * (0.5 * relationVariety + 0.5 * themeVariety);
  if (dominantShare > 0.5) variety -= (dominantShare - 0.5) * 2 * 0.8;
  variety = clamp(variety);

  explanation.push(`Variety ${variety.toFixed(2)}: ${relations.size} типов связи, `
    + `${themes.size} тематических сфер`
    + (dominantShare > 0.5 ? `, но ${(dominantShare * 100).toFixed(0)}% категорий однотипны` : ''));

  // ---------------- Aha ----------------
  // момент пересборки гипотезы: честная ловушка и мета-payoff
  const fairTraps = spec.traps.filter((t) =>
    t.decoyFit >= 0.6 && t.decoyObviousness <= 0.55).length;
  const confirmed = evidence.confirmedTraps ?? fairTraps;
  const metaDepth = Math.max(0, ...spec.categories.map((c) => c.metaDepth));
  const metaLinks = spec.categories.reduce((n, c) =>
    n + c.words.filter((w) => w.kind === 'meta').length, 0);

  let aha = 0;
  aha += Math.min(1.2, confirmed * 0.6);
  aha += Math.min(0.8, metaLinks * 0.2);
  aha += metaDepth >= 2 ? 0.5 : 0;
  // пресность: сложный уровень без ни одного ага-момента
  if (confirmed === 0 && metaLinks === 0) {
    aha = 0;
    explanation.push('Aha 0.00: ни ловушек, ни мета-связей — уровень пресный');
  }
  aha = clamp(aha);
  if (confirmed > 0 || metaLinks > 0) {
    explanation.push(`Aha ${aha.toFixed(2)}: ${confirmed} честных ловушек, `
      + `${metaLinks} мета-связей, глубина ${metaDepth}`);
  }

  // ---------------- Freshness ----------------
  const newShare = evidence.newWordShare ?? 1;
  const uniqueCategoryThemes = themes.size / Math.max(1, spec.categories.length);
  let freshness = MAX * (0.7 * Math.min(1, newShare / 0.45) * 0.6
    + 0.4 * Math.min(1, uniqueCategoryThemes * 2));
  freshness = clamp(freshness);
  explanation.push(`Freshness ${freshness.toFixed(2)}: новых для пакета слов `
    + `${(newShare * 100).toFixed(0)}%`
    + (evidence.newWordShare === undefined ? ' (история пакета не передана, взято 100%)' : ''));

  const value = Math.round(
    (weights.clarity * clarity + weights.variety * variety
      + weights.aha * aha + weights.freshness * freshness) * 2) / 2;

  return {
    clarity: Math.round(clarity * 100) / 100,
    variety: Math.round(variety * 100) / 100,
    aha: Math.round(aha * 100) / 100,
    freshness: Math.round(freshness * 100) / 100,
    value: Math.max(0, Math.min(10, value)),
    explanation,
    scoringVersion: config.interest.scoring_version,
  };
}
