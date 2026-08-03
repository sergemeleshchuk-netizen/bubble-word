/**
 * Сборка блока: план → уровень → проверки → оценки → хеш.
 *
 * Одна функция, которую вызывают и веб-инструмент, и офлайн-скрипты. Никакого
 * ввода-вывода внутри: на вход снимок и конфиг, на выход результат. Поэтому она
 * одинаково работает в браузере и в node, и её результат проверяем тестами.
 */
import type {
  BlockConfig, BlockResult, GeneratedLevel, GenerationFailure, LevelSpec, Snapshot,
} from './types.ts';
import { ContentIndex } from './snapshot.ts';
import { buildBlockPlan } from './blockPlan.ts';
import {
  GENERATOR_VERSION, emptyPackHistory, generateLevel, normalizeWordKey, planDeepChain,
  recordLevelInHistory, type PackHistory,
} from './generator.ts';
import { validateLevel } from './validator.ts';
import { countSolutions } from './solutionCounter.ts';
import { computeStructuralMetrics } from './structuralMetrics.ts';
import { simulatePlayability } from './simulatePlayability.ts';
import {
  computeDifficulty, difficultyTier, type ScoringConfig, type SemanticEvidence,
} from './scoringDifficulty.ts';
import { computeInterest, type InterestEvidence } from './scoringInterest.ts';
import { canonicalJson, levelSpecHash, sha256Hex } from './hashing.ts';

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
        if (solutions.count === 0) {
          return { ok: false, stage: 'единственность решения',
            reason: 'ни одной полной раскладки — ошибка сборки' };
        }
        if (solutions.count >= 2) {
          const clash = solutions.secondSolutionExample?.slice(0, 2)
            .map((s) => s.category).join(' и ') ?? 'две категории';
          return { ok: false, stage: 'единственность решения',
            reason: `найдено две полные раскладки: слова двоятся между ${clash}` };
        }
        const validation = validateLevel(spec, {
          ...validationContext(), solutions, repeatCount: repeatCount(spec, history),
        });
        const hard = validation.issues.filter((i) => i.severity === 'hard');
        if (hard.length) {
          return { ok: false, stage: 'валидация',
            reason: hard.map((i) => `${i.code}: ${i.message}`).join('; ') };
        }
        /*
         * Динамическая проходимость — такой же hard-гейт, как единственность
         * решения. Инцидент 02.08 (уровень 12 «как в оригинале»): семантически
         * безупречный уровень со случайной очередью досыпки оставил игрока
         * перед полем из одних недоборов. Уровень обязан не только решаться
         * на бумаге, но и доигрываться в ритме: без жёстких тупиков, в лимит
         * ходов, без досыпок «вне ритма» и состояний «выглядит тупиком».
         * Цепь-линия — исключение по построению: прототип снимает её сам,
         * когда мерджей не осталось, и это штатная механика, а не сбой.
         */
        const play = simulatePlayability(spec);
        if (!play.winnable) {
          return { ok: false, stage: 'проходимость',
            reason: play.failReason ?? 'симуляция партии не дошла до победы' };
        }
        const chained = spec.modifiers.chainLine !== null;
        if (!chained && (play.rescues > 0 || play.perceivedDead > 0)) {
          return { ok: false, stage: 'проходимость',
            reason: `ритм сломан: досыпок вне ритма ${play.rescues}, `
              + `состояний-«тупиков» ${play.perceivedDead}` };
        }
        return { ok: true, stage: 'проверки', reason: 'все hard-инварианты пройдены' };
      },
    });

    if (!outcome.spec) {
      if (outcome.failure) failures.push(outcome.failure);
      continue;
    }
    const spec = outcome.spec;

    // порядок важен: сначала считаем решения, потом валидируем (валидатор
    // использует результат), и только потом выставляем оценки
    const solutions = countSolutions(index, spec);
    const structural = computeStructuralMetrics(index, spec);
    const playability = simulatePlayability(spec);
    const validation = validateLevel(spec, {
      ...validationContext(), solutions, structural, repeatCount: repeatCount(spec, history),
    });

    const evidence = options.solverEvidence?.get(plan.levelId) ?? {};
    const difficulty = computeDifficulty(spec, index, scoring, solutions, evidence);
    const interest = computeInterest(spec, index, scoring, solutions, {
      ...evidence,
      newWordShare: newWordShare(spec, history),
      echoCategories: echoCategories(spec, history),
      returningCategories: returningCategories(spec, history),
      modifierSeenBefore: plan.modifier === 'none' ? 0
        : (modifierSeen.get(plan.modifier) ?? 0),
    });
    if (plan.modifier !== 'none') {
      modifierSeen.set(plan.modifier, (modifierSeen.get(plan.modifier) ?? 0) + 1);
    }

    levels.push({
      plan,
      spec,
      validation,
      solutions,
      structural,
      playability,
      difficulty,
      interest,
      attempts: outcome.attempts,
      levelSpecHash: levelSpecHash({
        levelSpec: spec,
        seed: config.seed,
        normalizedConfig: normalizeConfig(config),
        generatorVersion: GENERATOR_VERSION,
        contentSnapshotHash: snapshot.content_snapshot_hash,
      }),
    });

    // историю пополняем только принятыми уровнями: иначе отклонённая попытка
    // «съедала» бы слова и следующий уровень не сходился
    if (validation.passed) recordLevelInHistory(history, spec);
  }

  const packHash = sha256Hex(canonicalJson({
    levels: levels.map((l) => l.levelSpecHash),
    snapshot: snapshot.content_snapshot_hash,
    generator: GENERATOR_VERSION,
    scoring: scoring.scoring_version,
  }));

  return {
    config,
    contentSnapshotHash: snapshot.content_snapshot_hash,
    generatorVersion: GENERATOR_VERSION,
    levels,
    failures,
    packHash,
  };
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
     */
    deal: {
      start: spec.deal.start.map((b) => ({ word: b.word, category: b.category })),
      queue: spec.deal.queue.map((b) => ({ word: b.word, category: b.category })),
    },
    categories: spec.categories.map((c) => ({
      key: c.key,
      label: c.label,
      words: c.words.map((w) => (w.kind === 'meta'
        ? { text: w.text, kind: 'meta', meta_child: w.metaChild }
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
