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
  /**
   * Категории-эхо: ровно ОДНО слово знакомо из прошлых уровней, остальные новые.
   *
   * Решение владельца 03.08: это и есть приятная форма памяти. Знакомое слово
   * даёт зацепку («bass я уже где-то видел»), три новых — работу; при двух и
   * более знакомых категория превращается в перепечатку, а при нуле памяти не
   * задействовано вовсе. Считается по истории пакета (`generateBlock`), потому
   * что «знакомое» — свойство пакета, а не уровня.
   */
  echoCategories?: number;
  /** категорий, вернувшихся из прошлых уровней пакета (по имени) */
  returningCategories?: number;
  /**
   * Сколько РАНЬШЕ в пакете уже было уровней с этим же модификатором.
   *
   * Нужен, чтобы механика считалась интересной за новизну, а не за факт. Иначе
   * модификатор поднимал бы D (механика — это сложность) и I (механика — это
   * разнообразие) синхронно на каждом уровне, и две шкалы связывались бы
   * механически: замер 100 уровней показал рост корреляции 0.51 → 0.55 и падение
   * числа переходов, где линии идут в разные стороны, с 25 до 16. Первый лёд в
   * пакете — событие, пятый — рутина, и разводит линии именно это.
   */
  modifierSeenBefore?: number;
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

  /*
   * Игровой модификатор — тоже разнообразие, и именно здесь ему место
   * (решение владельца 03.08). Variety отвечает на вопрос «одинаково ли
   * играется уровень за уровнем», а половинки, лёд, «?» и цепь меняют не
   * содержание пазла, а сам способ взаимодействия: те же слова требуют другого
   * порядка действий. В Aha их класть нельзя — там семантическая пересборка
   * гипотезы, а механика к смыслу слов отношения не имеет.
   *
   * Вес объявленный и один на любую механику: калибровать нечем (в референсе
   * L1-200 этих модификаторов нет), а различать «лёд интереснее цепи» без
   * данных значило бы выдумывать. Один модификатор на уровень по построению
   * (blockPlan), поэтому бонус не складывается.
   *
   * Зато он ГАСНЕТ с повторением: делится на число прошлых уровней пакета с той
   * же механикой. Первый лёд — событие, пятый — фон; сложность от повторения не
   * падает, интерес падает, и именно это разводит две шкалы вместо того чтобы
   * двигать их вместе.
   */
  const declared = config.interest.declared ?? {};
  const modifier = spec.halves.length > 0
    || spec.modifiers.frozenBubbles.length > 0
    || spec.modifiers.hiddenBubbles.length > 0
    || spec.modifiers.chainLine !== null;
  const seenBefore = evidence.modifierSeenBefore ?? 0;
  const modifierBonus = modifier
    ? (declared.modifier_variety ?? 0.5) / (1 + seenBefore) : 0;
  variety += modifierBonus;
  variety = clamp(variety);

  explanation.push(`Variety ${variety.toFixed(2)}: ${relations.size} типов связи, `
    + `${themes.size} тематических сфер`
    + (dominantShare > 0.5 ? `, но ${(dominantShare * 100).toFixed(0)}% категорий однотипны` : '')
    + (modifier
      ? `; игровой модификатор ${seenBefore === 0 ? 'встречается впервые' : `повторяется (${seenBefore} раз до этого)`}`
        + ` — надбавка ${modifierBonus.toFixed(2)}`
      : ''));

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

  /*
   * ---------------- Freshness ----------------
   * Свежесть = новый материал ПЛЮС приятная память (решение владельца 03.08).
   *
   * До ред. 03.08 композит был мёртвым: формула
   * `0.7 * min(1, newShare/0.45) * 0.6 + 0.4 * min(1, темы*2)` содержала два
   * потолка, и оба упирались почти всегда — все сто замеренных уровней десяти
   * декад получали ровно 2.05. Вклад в оценку был, информации в нём не было
   * никакой, и это одна из причин, по которым линии D и I на графике шли рядом.
   *
   * Новизна — база, эхо — надбавка, и порядок именно такой. Эхо не может быть
   * долей потолка: на первых уровнях кампании знакомых слов не существует
   * физически, и уровень терял бы за это 40% свежести ни за что. Зато к концу
   * кампании новизна неизбежно падает (у оригинала с 88% на L1-20 до ~20% на
   * L400+) — и вот там эхо её компенсирует: слово вернулось, но в другой
   * четвёрке, и это уже не повтор, а узнавание.
   *
   *   новизна   доля слов, которых в пакете ещё не было;
   *   эхо       категории, где ровно ОДНО слово знакомо из прошлых уровней:
   *             зацепка есть, три остальных слова открываешь. Два и более
   *             знакомых — перепечатка, надбавки за них нет.
   */
  const newShare = evidence.newWordShare ?? 1;
  const echo = evidence.echoCategories ?? 0;
  const echoTarget = declared.echo_target ?? 3;
  const echoBonus = (declared.echo_bonus ?? 0.2) * Math.min(echo, echoTarget);
  const freshness = clamp(MAX * newShare + echoBonus);
  explanation.push(`Freshness ${freshness.toFixed(2)}: новых для пакета слов `
    + `${(newShare * 100).toFixed(0)}%`
    + (echo > 0
      ? `, ${echo} категорий с ровно одним знакомым словом (зацепка есть, `
        + 'перепечатки нет)'
      : ', категорий-эхо нет')
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
