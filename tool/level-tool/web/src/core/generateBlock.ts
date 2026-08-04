/**
 * Сборка блока: план → уровень → проверки → оценки → хеш.
 *
 * Одна функция, которую вызывают и веб-инструмент, и офлайн-скрипты. Никакого
 * ввода-вывода внутри: на вход снимок и конфиг, на выход результат. Поэтому она
 * одинаково работает в браузере и в node, и её результат проверяем тестами.
 */
import type {
  BlockConfig, BlockResult, GeneratedLevel, GenerationFailure, LevelSpec, Snapshot,
  SolutionCount, ValidationIssue,
} from './types.ts';
import type { PlayabilityResult } from './simulatePlayability.ts';
import { ContentIndex } from './snapshot.ts';
import { buildBlockPlan } from './blockPlan.ts';
import {
  GENERATOR_VERSION, emptyPackHistory, generateLevel, normalizeWordKey, planDeepChain,
  recordLevelInHistory, type PackHistory,
} from './generator.ts';
import { validateLevel, type ValidationContext } from './validator.ts';
import { dealForSpec } from './deal.ts';
import { countSolutions } from './solutionCounter.ts';
import { computeStructuralMetrics } from './structuralMetrics.ts';
import { simulatePlayability } from './simulatePlayability.ts';
import { simulateBlindPlay } from './simulateBlindPlay.ts';
import {
  computeDifficulty, difficultyTier, type ScoringConfig, type SemanticEvidence,
} from './scoringDifficulty.ts';
import { computeInterest, type InterestEvidence } from './scoringInterest.ts';
import { canonicalJson, levelSpecHash, sha256Hex } from './hashing.ts';
import { BOARD_CAPACITY } from './levelMath.ts';

/**
 * Hard-условия приёмки уровня — ОДИН список на весь инструмент.
 *
 * Раньше их было два: генерация проверяла единственность решения, hard-инварианты
 * и динамическую проходимость, а экран экспорта — только первые два, да и то
 * лишь рисовал плашку, не мешая скачать. Получалось, что инструмент обещал
 * «экспорт разрешён только после проверок» и тут же отдавал файл. Уровень после
 * ручной пересдачи выкладки не проходил и проверку проходимости — то есть
 * человек мог выложить старт, который сам же генератор забраковал бы.
 *
 * Поэтому условия живут здесь и вызываются из обоих мест. Возвращается причина
 * отказа (её показывают человеку) или `null`, если уровень принят.
 */
export interface HardGateInput {
  solutions: SolutionCount;
  hardIssues: ValidationIssue[];
  /** результат симуляции; `undefined`, если до неё не дошли */
  playability?: PlayabilityResult;
  /** цепь-линия снимается прототипом сама — ритм ей мерить нечем */
  chained: boolean;
}

export function hardGateFailure(
  input: HardGateInput,
): { stage: string; reason: string } | null {
  const { solutions, hardIssues, playability, chained } = input;
  if (solutions.count === 0) {
    return { stage: 'единственность решения',
      reason: 'ни одной полной раскладки — ошибка сборки' };
  }
  if (solutions.count >= 2) {
    const clash = solutions.secondSolutionExample?.slice(0, 2)
      .map((s) => s.category).join(' и ') ?? 'две категории';
    return { stage: 'единственность решения',
      reason: `найдено две полные раскладки: слова двоятся между ${clash}` };
  }
  if (hardIssues.length) {
    return { stage: 'валидация',
      reason: hardIssues.map((i) => `${i.code}: ${i.message}`).join('; ') };
  }
  /*
   * Динамическая проходимость — такой же hard-гейт, как единственность решения.
   * Инцидент 02.08 (уровень 12 «как в оригинале»): семантически безупречный
   * уровень со случайной очередью досыпки оставил игрока перед полем из одних
   * недоборов. Уровень обязан не только решаться на бумаге, но и доигрываться
   * в ритме: без жёстких тупиков, в лимит ходов, без досыпок «вне ритма» и
   * состояний «выглядит тупиком».
   */
  if (!playability) {
    return { stage: 'проходимость', reason: 'симуляция партии не прогонялась' };
  }
  if (!playability.winnable) {
    return { stage: 'проходимость',
      reason: playability.failReason ?? 'симуляция партии не дошла до победы' };
  }
  /*
   * Очередь линий обязана выдержать партию. Гейт, вскрытый досыпкой, означает
   * ровно одно: в очереди не осталось пузырей открытых линий, и правило «линия
   * ждёт прогресса» пришлось нарушить, чтобы поле не встало. Уровень от этого не
   * ломается (страховка сработала), но обещание «крупный уровень раскладывается
   * волнами» перестаёт выполняться — а это и есть то, ради чего гейты введены.
   */
  if (playability.gatesForced > 0) {
    return { stage: 'проходимость',
      reason: `очередь линий не сошлась: досыпка вскрывала закрытый гейт `
        + `${playability.gatesForced} раз` };
  }
  if (!chained && (playability.rescues > 0 || playability.perceivedDead > 0)) {
    return { stage: 'проходимость',
      reason: `ритм сломан: досыпок вне ритма ${playability.rescues}, `
        + `состояний-«тупиков» ${playability.perceivedDead}` };
  }
  return null;
}

/** Тот же гейт, но по уже посчитанному уровню: для экспорта и сводки пакета. */
export function levelHardGateFailure(
  level: GeneratedLevel,
): { stage: string; reason: string } | null {
  return hardGateFailure({
    solutions: level.solutions,
    hardIssues: level.validation.issues.filter((i) => i.severity === 'hard'),
    playability: level.playability,
    chained: level.spec.modifiers.chainLine !== null,
  });
}

export interface BlockGenerationOptions {
  snapshot: Snapshot;
  config: BlockConfig;
  scoring: ScoringConfig;
  /** хеши четвёрок референса для проверки novelty */
  referenceQuadrupleHashes?: Set<string>;
  /** режим проверки на копирование референса; по умолчанию off (см. validator.ts) */
  referenceNovelty?: 'off' | 'soft' | 'hard';
  /** эмпирика прогонов слепого решателя, по номеру уровня */
  solverEvidence?: Map<number, SemanticEvidence & InterestEvidence>;
  history?: PackHistory;
  maxAttempts?: number;
}

/** Хеш четвёрки слов: порядок не важен, регистр не важен. */
export function hashQuadruple(words: string[]): string {
  return sha256Hex(words.map((w) => w.toLowerCase().trim()).sort().join('|'));
}

/** Нормализованный конфиг: в хеш уровня входит только то, что влияет на контент. */
function normalizeConfig(config: BlockConfig): unknown {
  return {
    categoryCorridor: config.categoryCorridor,
    rarityRange: config.rarityRange,
    maxMetaDepth: config.maxMetaDepth,
    allowedModifiers: [...config.allowedModifiers].sort(),
    includeThemes: [...config.includeThemes].sort(),
    excludeThemes: [...config.excludeThemes].sort(),
    wordFreshnessWindow: config.wordFreshnessWindow,
    categoryFreshnessWindow: config.categoryFreshnessWindow,
    wordsPerCategory: config.wordsPerCategory,
    categoryPlan: config.categoryPlan ?? null,
    metaPlan: config.metaPlan ?? null,
    // undefined канонический сериализатор выбрасывает, поэтому у пресета 201-210
    // хеш остаётся прежним, а у калиброванного по декаде блока гейты в хеш входят:
    // они влияют на контент, значит обязаны влиять на хеш
    decadeGates: config.decadeGates,
    // облегчённая раздача меняет стартовое поле — входит в хеш; «1» = историческая
    dealMinStartWords: config.dealMinStartWords !== undefined
      && config.dealMinStartWords >= 2 ? config.dealMinStartWords : undefined,
    // явная схема выкладки тоже контент: входит в хеш, пустая = не задана
    dealScheme: config.dealScheme && config.dealScheme.length > 0
      ? config.dealScheme : undefined,
    // вилка схем из таблицы декад — контент по той же причине
    dealSchemeRange: config.dealSchemeRange
      && config.dealSchemeRange.min.length > 0
      ? config.dealSchemeRange : undefined,
    // бюджет старта входит в хеш только когда реально подрезает поле: у
    // промежутков «до 24» выкладка та же, что была до таблицы, и хеш прежний
    dealStartBubbles: config.dealStartBubbles
      && config.dealStartBubbles[1] < BOARD_CAPACITY
      ? config.dealStartBubbles : undefined,
    // очередь линий меняет и старт, и порядок досыпки — то есть контент: входит
    // в хеш. Ноль приравнен к отсутствию поля: это уровень без гейтов
    dealHoldCategories: config.dealHoldCategories && config.dealHoldCategories > 0
      ? config.dealHoldCategories : undefined,
  };
}

/** Слов уровня, которые уже встречались раньше в ДРУГОЙ категории. */
function repeatCount(spec: LevelSpec, history: PackHistory): number {
  let n = 0;
  for (const category of spec.categories) {
    for (const w of category.words) {
      const key = normalizeWordKey(w.text);
      if (!history.wordLastLevel.has(key)) continue;
      if (history.wordCategory?.get(key) !== category.key) n += 1;
    }
  }
  return n;
}

/**
 * Категории-эхо: ровно ОДНО слово знакомо из прошлых уровней пакета.
 *
 * Считается здесь, а не в модели интереса, по той же причине, что и повторы:
 * «знакомое слово» — свойство пакета и его истории, а спек одного уровня о
 * прошлом ничего не знает. Мета-слова не считаются: они не спавнятся и игрок
 * их как слово не встречает.
 */
function echoCategories(spec: LevelSpec, history: PackHistory): number {
  let echo = 0;
  for (const category of spec.categories) {
    const known = category.words.filter((w) => w.kind === 'word'
      && history.wordLastLevel.has(normalizeWordKey(w.text))).length;
    if (known === 1) echo += 1;
  }
  return echo;
}

/** Категорий, которые в пакете уже были (вернулись после окна свежести). */
function returningCategories(spec: LevelSpec, history: PackHistory): number {
  return spec.categories.filter((c) => history.categoryLastLevel.has(c.key)).length;
}

/** Доля слов уровня, новых для пакета. */
function newWordShare(spec: LevelSpec, history: PackHistory): number {
  const words = spec.categories.flatMap((c) => c.words);
  if (!words.length) return 1;
  const fresh = words.filter((w) => !history.wordLastLevel.has(w.text.toLowerCase())).length;
  return fresh / words.length;
}

export function generateBlock(options: BlockGenerationOptions): BlockResult {
  const { snapshot, config, scoring } = options;
  const index = new ContentIndex(snapshot);
  const plans = buildBlockPlan(config);
  const history = options.history ?? emptyPackHistory();

  const levels: GeneratedLevel[] = [];
  const failures: GenerationFailure[] = [];
  /**
   * Сколько уровней пакета уже вышли с тем же модификатором. Живёт здесь, а не
   * в `PackHistory`: это счётчик ОДНОГО прогона, нужный только модели интереса,
   * а история пакета описывает контент (слова и категории) и участвует в
   * правилах свежести. Смешивать не стоит.
   */
  const modifierSeen = new Map<string, number>();

  /**
   * Резервирование глубокой цепочки.
   *
   * Цепочки глубины 3 в базе есть, но их мало, и правила свежести съедают их
   * участников на первых уровнях блока: уровень, которому глубина нужна по плану,
   * приходит к пустому пулу. Поэтому блок сначала находит цепочку и запрещает
   * её категории всем остальным уровням.
   */
  const deepestPlan = plans.reduce((best, p) =>
    (p.metaDepthTarget > best.metaDepthTarget ? p : best), plans[0]);
  const reservedChain = deepestPlan.metaDepthTarget >= 2
    ? planDeepChain(index, deepestPlan.metaDepthTarget, config.seed, config.wordsPerCategory,
      config.decadeGates ?? null)
    : null;
  const reservedCategories = new Set<number>();
  if (reservedChain) {
    for (const edge of reservedChain) {
      reservedCategories.add(edge.child);
      reservedCategories.add(edge.parent);
    }
  }

  for (const plan of plans) {
    const isDeepLevel = plan.levelId === deepestPlan.levelId;
    /**
     * Уровень принимается только если у него ровно одно глобальное решение
     * и нет нарушений hard-инвариантов. Проверка стоит ВНУТРИ цикла попыток:
     * иначе двусмысленный уровень доезжал бы до отчёта как готовый, хотя
     * достаточно было взять другой набор категорий.
     */
    const validationContext = () => ({
      index,
      history: {
        wordLastLevel: history.wordLastLevel,
        categoryLastLevel: history.categoryLastLevel,
        wordWindow: config.wordFreshnessWindow,
        categoryWindow: config.categoryFreshnessWindow,
      },
      referenceQuadrupleHashes: options.referenceQuadrupleHashes,
      referenceNovelty: options.referenceNovelty,
      hashQuadruple,
      maxMetaDepth: config.maxMetaDepth,
      decadeGates: config.decadeGates,
      rareRange: config.decadeGates ? config.rarityRange : undefined,
    });

    const outcome = generateLevel(index, plan, config, history, {
      maxAttempts: options.maxAttempts,
      excludeCategories: isDeepLevel ? undefined : reservedCategories,
      forcedChain: isDeepLevel && reservedChain ? reservedChain : undefined,
      accept: (spec) => {
        const solutions = countSolutions(index, spec);
        const validation = solutions.count === 1
          ? validateLevel(spec, {
            ...validationContext(), solutions, repeatCount: repeatCount(spec, history),
          })
          : undefined;
        const failure = hardGateFailure({
          solutions,
          hardIssues: validation
            ? validation.issues.filter((i) => i.severity === 'hard')
            : [],
          // Симуляцию гоняем только когда уровень дошёл до неё: она дороже
          // остальных проверок, а на двусмысленном уровне бессмысленна.
          playability: solutions.count === 1 && validation
              && !validation.issues.some((i) => i.severity === 'hard')
            ? simulatePlayability(spec)
            : undefined,
          chained: spec.modifiers.chainLine !== null,
        });
        if (failure) return { ok: false, ...failure };
        return { ok: true, stage: 'проверки', reason: 'все hard-инварианты пройдены' };
      },
    });

    if (!outcome.spec) {
      if (outcome.failure) failures.push(outcome.failure);
      continue;
    }
    const spec = outcome.spec;

    const level = evaluateSpec({
      spec,
      plan,
      index,
      config,
      scoring,
      history,
      snapshotHash: snapshot.content_snapshot_hash,
      attempts: outcome.attempts,
      evidence: options.solverEvidence?.get(plan.levelId) ?? {},
      modifierSeenBefore: plan.modifier === 'none' ? 0
        : (modifierSeen.get(plan.modifier) ?? 0),
      validationExtras: validationContext(),
    });
    if (plan.modifier !== 'none') {
      modifierSeen.set(plan.modifier, (modifierSeen.get(plan.modifier) ?? 0) + 1);
    }
    levels.push(level);

    // историю пополняем только принятыми уровнями: иначе отклонённая попытка
    // «съедала» бы слова и следующий уровень не сходился
    if (level.validation.passed) recordLevelInHistory(history, spec);
  }

  const packHash = packHashOf(levels, snapshot.content_snapshot_hash, scoring);

  return {
    config,
    contentSnapshotHash: snapshot.content_snapshot_hash,
    generatorVersion: GENERATOR_VERSION,
    levels,
    failures,
    packHash,
  };
}

/** Хеш пакета: список хешей уровней плюс версии, от которых он зависит. */
function packHashOf(
  levels: readonly GeneratedLevel[], snapshotHash: string, scoring: ScoringConfig,
): string {
  return sha256Hex(canonicalJson({
    levels: levels.map((l) => l.levelSpecHash),
    snapshot: snapshotHash,
    generator: GENERATOR_VERSION,
    scoring: scoring.scoring_version,
  }));
}

/**
 * Оценка готового спека: решения → структура → проходимость → проверки → D и I
 * → слепой прогон → хеш.
 *
 * Вынесено из цикла сборки не ради красоты. Тем же путём обязан пройти уровень,
 * которому ВРУЧНУЮ поменяли схему выкладки (`redealLevel` ниже): выкладка входит
 * и в оценку сложности (фактор «раскладка старта»), и в проходимость, и в хеш
 * спека. Считать её отдельно значило бы оставить в карточке оценки, посчитанные
 * для другой выкладки, — то есть врать о том уровне, который сдаётся.
 */
function evaluateSpec(args: {
  spec: LevelSpec;
  plan: import('./types.ts').LevelPlan;
  index: ContentIndex;
  config: BlockConfig;
  scoring: ScoringConfig;
  /** история пакета НА МОМЕНТ этого уровня: свежесть слов и категорий */
  history: PackHistory;
  snapshotHash: string;
  attempts: GeneratedLevel['attempts'];
  evidence: SemanticEvidence & InterestEvidence;
  modifierSeenBefore: number;
  /** контекст валидатора: индекс, окна свежести, гейты декады, novelty */
  validationExtras: ValidationContext;
}): GeneratedLevel {
  const { spec, plan, index, config, scoring, history } = args;

  // порядок важен: сначала считаем решения, потом валидируем (валидатор
  // использует результат), и только потом выставляем оценки
  const solutions = countSolutions(index, spec);
  const structural = computeStructuralMetrics(index, spec);
  const playability = simulatePlayability(spec);
  const validation = validateLevel(spec, {
    ...args.validationExtras, solutions, structural,
    repeatCount: repeatCount(spec, history),
  });

  const difficulty = computeDifficulty(spec, index, scoring, solutions, args.evidence);
  const interest = computeInterest(spec, index, scoring, solutions, {
    ...args.evidence,
    newWordShare: newWordShare(spec, history),
    echoCategories: echoCategories(spec, history),
    returningCategories: returningCategories(spec, history),
    modifierSeenBefore: args.modifierSeenBefore,
  });

  /*
   * Слепой прогон — ДИАГНОСТИКА, а не гейт.
   *
   * Он считается только для принятого уровня и ни на что в приёмке не влияет:
   * модель знания игрока не откалибрована (см. шапку `playerKnowledge.ts`),
   * и браковать уровни по неоткалиброванному числу значило бы выдать догадку
   * за измерение. Здесь он затем, чтобы цена незнания слов была ВИДНА в
   * карточке уровня и накапливалась по пакетам — до того, как ей доверят
   * решать судьбу уровня. Seed привязан к блоку и уровню: тот же блок даёт те
   * же числа, разные уровни — разных игроков.
   */
  const blindPlay = simulateBlindPlay(spec, playability.movesNeeded,
    { seed: `${config.seed}#blind-${plan.levelId}`, index });

  return {
    plan,
    spec,
    validation,
    solutions,
    structural,
    playability,
    blindPlay,
    difficulty,
    interest,
    attempts: args.attempts,
    levelSpecHash: levelSpecHash({
      levelSpec: spec,
      seed: config.seed,
      normalizedConfig: normalizeConfig(config),
      generatorVersion: GENERATOR_VERSION,
      contentSnapshotHash: args.snapshotHash,
    }),
  };
}

export interface RedealOptions {
  snapshot: Snapshot;
  scoring: ScoringConfig;
  /** блок, в котором живёт уровень: из него берутся конфиг и история пакета */
  block: BlockResult;
  level: GeneratedLevel;
  /**
   * Новая схема старта, доли по убыванию: `[4,3,3,3,2]`. Пустой массив или null
   * возвращают уровень на автоматическую раздачу (`autoScheme`).
   */
  scheme: readonly number[] | null;
  /** готовый индекс снимка, чтобы не строить его заново на каждое нажатие */
  index?: ContentIndex;
}

/**
 * Переложить старт уровня по заданной схеме и пересчитать его целиком.
 *
 * Зачем это в инструменте. Схема выкладки — самый быстрый рычаг проходимости:
 * при ровной раздаче уровень на 12 категорий встречает игрока полем из пар, где
 * не собирается ни одна, и «продвинуться со старта» нечем. Дизайнеру нужно
 * увидеть применённую схему и поправить её на месте, а не пересобирать блок и
 * гадать, что изменилось.
 *
 * Честность: пересчитывается ВСЁ, что зависит от выкладки — единственность
 * решения, hard-инварианты, проходимость, слепой прогон, D и I, хеш спека и хеш
 * пакета. Ручная схема не отменяет приёмку, она проходит её заново.
 *
 * Чего функция НЕ делает: не меняет состав уровня. Категории и слова остаются
 * те же — иначе это была бы пересборка блока, а не правка выкладки.
 */
export function redealLevel(options: RedealOptions): GeneratedLevel {
  const { block, level, scoring } = options;
  const index = options.index ?? new ContentIndex(options.snapshot);
  const config = block.config;
  const scheme = options.scheme && options.scheme.length > 0
    ? [...options.scheme].sort((a, b) => b - a) : undefined;

  const spec: LevelSpec = {
    ...level.spec,
    board: { ...level.spec.board, dealScheme: scheme },
  };
  spec.deal = dealForSpec(spec);

  /*
   * История пакета восстанавливается из уровней, стоящих в блоке ДО этого.
   * Свежесть слов и категорий, повторы и доля новых слов считаются от неё, и
   * взять её «как есть» из блока нельзя: она живёт только внутри сборки.
   */
  const history = emptyPackHistory();
  let modifierSeenBefore = 0;
  for (const earlier of block.levels) {
    if (earlier.spec.levelId === spec.levelId) break;
    if (earlier.plan.modifier !== 'none' && earlier.plan.modifier === level.plan.modifier) {
      modifierSeenBefore += 1;
    }
    if (earlier.validation.passed) recordLevelInHistory(history, earlier.spec);
  }

  return evaluateSpec({
    spec,
    plan: level.plan,
    index,
    config,
    scoring,
    history,
    snapshotHash: block.contentSnapshotHash,
    // след ручной правки остаётся в самом уровне: по попыткам видно, что
    // выкладку задал человек, а не генератор
    attempts: [...level.attempts, {
      index: level.attempts.length + 1,
      outcome: 'accepted' as const,
      stage: 'выкладка',
      reason: scheme
        ? `схема старта задана вручную: ${scheme.join('-')}`
        : 'схема старта возвращена к автоматической',
      relaxations: [],
    }],
    evidence: {},
    modifierSeenBefore,
    validationExtras: {
      index,
      history: {
        wordLastLevel: history.wordLastLevel,
        categoryLastLevel: history.categoryLastLevel,
        wordWindow: config.wordFreshnessWindow,
        categoryWindow: config.categoryFreshnessWindow,
      },
      hashQuadruple,
      maxMetaDepth: config.maxMetaDepth,
      decadeGates: config.decadeGates,
      rareRange: config.decadeGates ? config.rarityRange : undefined,
    },
  });
}

/**
 * Заменить уровень в блоке и пересчитать хеш пакета.
 *
 * Хеш пакета собран из хешей уровней, а правка выкладки меняет хеш спека.
 * Оставить прежний packHash значило бы подписать старым хешем другой пакет — и
 * прототип с экспортом показывали бы имя группы, которой уже нет.
 */
export function withLevel(
  block: BlockResult, level: GeneratedLevel, scoring: ScoringConfig,
): BlockResult {
  const levels = block.levels.map((l) =>
    (l.spec.levelId === level.spec.levelId ? level : l));
  return { ...block, levels, packHash: packHashOf(levels, block.contentSnapshotHash, scoring) };
}

/**
 * Минимальный игровой JSON: контракт с клиентом игры, без следов пайплайна.
 *
 * Ярус сложности (`difficulty_tier`) — продуктовая пометка easy/medium/hard,
 * а не след пайплайна: игра показывает её игроку и строит по ней меню.
 * Считается из D (см. difficultyTier) и передаётся вторым аргументом, потому
 * что в самом спеке оценок нет — спек хешируется без них.
 */
export function toGameJson(spec: LevelSpec, difficultyValue?: number): unknown {
  return {
    level_id: spec.levelId,
    schema_version: spec.schemaVersion,
    difficulty_tier: difficultyValue === undefined ? undefined
      : difficultyTier(difficultyValue),
    board: {
      categories_count: spec.board.categoriesCount,
      words_per_category: spec.board.wordsPerCategory,
      start_bubbles: spec.board.startBubbles,
      board_capacity: spec.board.boardCapacity,
      move_limit: spec.board.moveLimit,
    },
    /*
     * Первая выкладка едет в игру вместе с уровнем.
     *
     * Без неё клиент раскладывал бы поле сам и со своей случайностью — значит,
     * уровень, который мы проверили руками и оценили по D, у игрока оказался бы
     * другим. Порядок массивов значащий: `start` — что лежит на поле, `queue` —
     * очередь досыпки строго слева направо.
     *
     * `gates` — очередь линий крупного уровня: категория ждёт, пока игрок не
     * собрал `after_collected` других, и досыпка пропускает её пузыри, беря из
     * очереди следующий подходящий (core/deal.ts). Поля нет — гейтов нет.
     */
    deal: {
      start: spec.deal.start.map((b) => ({ word: b.word, category: b.category })),
      queue: spec.deal.queue.map((b) => ({ word: b.word, category: b.category })),
      gates: (spec.deal.gates ?? []).length === 0 ? undefined
        : spec.deal.gates!.map((g) => ({
          category: g.category, after_collected: g.afterCollected,
        })),
    },
    categories: spec.categories.map((c) => ({
      key: c.key,
      label: c.label,
      /*
       * Мета-пузырь с картинкой помечен, а не подменён: `text` остаётся словом
       * (по нему клиент связывает пузырь с дочерней категорией), `display`
       * говорит «рисуй значок», `icon` — сам значок. Эмодзи здесь — реализация
       * прототипа; клиент вправе подставить свой спрайт по тому же `text`.
       */
      words: c.words.map((w) => (w.kind === 'meta'
        ? {
          text: w.text, kind: 'meta', meta_child: w.metaChild,
          display: w.icon ? 'icon' : undefined,
          icon: w.icon,
        }
        : { text: w.text, kind: 'word' })),
    })),
    /*
     * Модификаторы уровня: игра их ИСПОЛНЯЕТ, как и выкладку. Половинки едут
     * с точками распила (склейка тратит ход, лимит это уже учитывает), лёд и
     * «?» — с конкретными словами и счётчиками, цепь-линия — со счётчиком
     * категорий. Пустые поля не пишутся: уровень без механик читается как
     * прежде.
     */
    modifiers: {
      chains: spec.modifiers.chains.map((c) => ({
        locks: c.locksCategory, unlocked_by: c.unlockedByCompleting,
      })),
      halves: spec.halves.length === 0 ? undefined
        : spec.halves.map((h) => ({
          word: h.word, category: h.home, pieces: h.fragments,
        })),
      frozen: spec.modifiers.frozenBubbles.length === 0 ? undefined
        : spec.modifiers.frozenBubbles.map((b) => ({
          word: b.word, category: b.category, layers: b.layers,
        })),
      hidden: spec.modifiers.hiddenBubbles.length === 0 ? undefined
        : spec.modifiers.hiddenBubbles.map((b) => ({
          word: b.word, category: b.category, layers: b.layers,
        })),
      chain_line: spec.modifiers.chainLine
        ? { need: spec.modifiers.chainLine.need } : undefined,
    },
  };
}

/** Полный JSON пайплайна: provenance, оценки, проверки — для инструмента и отчёта. */
export function toPipelineJson(level: GeneratedLevel, block: BlockResult): unknown {
  return {
    level_spec: level.spec,
    build_metadata: {
      generated_at: new Date().toISOString(),   // НЕ входит в хеш (SPEC_AUDIT §8)
      generator_version: block.generatorVersion,
      scoring_version: level.difficulty.scoringVersion,
      content_snapshot_hash: block.contentSnapshotHash,
      level_spec_hash: level.levelSpecHash,
      pack_hash: block.packHash,
      seed: block.config.seed,
    },
    plan: level.plan,
    scoring: {
      difficulty: level.difficulty.value,
      difficulty_tier: difficultyTier(level.difficulty.value),
      difficulty_breakdown: {
        // порядок корзин важен: сначала то, что откалибровано по данным,
        // потом то, что объявлено продуктовым решением
        base_calibrated: level.difficulty.base,
        declared_not_calibrated: level.difficulty.declared,
        semantic: level.difficulty.semantic,
        mechanical: level.difficulty.mechanical,
        totals: {
          base: level.difficulty.baseTotal,
          declared: level.difficulty.declaredTotal,
          semantic: level.difficulty.semanticTotal,
          mechanical: level.difficulty.mechanicalTotal,
        },
      },
      difficulty_explanation: level.difficulty.explanation,
      interest: level.interest.value,
      interest_breakdown: {
        clarity: level.interest.clarity,
        variety: level.interest.variety,
        aha: level.interest.aha,
        freshness: level.interest.freshness,
      },
      interest_explanation: level.interest.explanation,
    },
    validation: {
      passed: level.validation.passed,
      checks: level.validation.checks,
      issues: level.validation.issues,
      solution_count: level.solutions.count,
      solution_search_exhausted: level.solutions.exhausted,
      solution_nodes_visited: level.solutions.nodesVisited,
      playability: level.playability ? {
        winnable: level.playability.winnable,
        moves_needed: level.playability.movesNeeded,
        move_limit: level.playability.moveLimit,
        spare_moves: level.playability.spareMoves,
        offbeat_refills: level.playability.rescues,
        perceived_dead_states: level.playability.perceivedDead,
        max_moves_without_collect: level.playability.maxDrought,
      } : undefined,
      structure: level.structural ? {
        multi_home_words: level.structural.multiHomeWords,
        max_contested_slots: level.structural.maxContestedSlots,
        opening_categories: level.structural.openingCategories,
        deduction_only: level.structural.deductionOnly,
        forced_steps: level.structural.forcedSteps,
        explanation: level.structural.explanation,
      } : undefined,
    },
    generation: { attempts: level.attempts },
  };
}
