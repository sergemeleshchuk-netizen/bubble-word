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
import { computeDifficulty, type ScoringConfig, type SemanticEvidence } from './scoringDifficulty.ts';
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
    const validation = validateLevel(spec, {
      ...validationContext(), solutions, repeatCount: repeatCount(spec, history),
    });

    const evidence = options.solverEvidence?.get(plan.levelId) ?? {};
    const difficulty = computeDifficulty(spec, index, scoring, solutions, evidence);
    const interest = computeInterest(spec, index, scoring, solutions, {
      ...evidence,
      newWordShare: newWordShare(spec, history),
    });

    levels.push({
      plan,
      spec,
      validation,
      solutions,
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

/** Минимальный игровой JSON: контракт с клиентом игры, без следов пайплайна. */
export function toGameJson(spec: LevelSpec): unknown {
  return {
    level_id: spec.levelId,
    schema_version: spec.schemaVersion,
    board: {
      categories_count: spec.board.categoriesCount,
      words_per_category: spec.board.wordsPerCategory,
      start_bubbles: spec.board.startBubbles,
      board_capacity: spec.board.boardCapacity,
      move_limit: spec.board.moveLimit,
    },
    categories: spec.categories.map((c) => ({
      key: c.key,
      label: c.label,
      words: c.words.map((w) => (w.kind === 'meta'
        ? { text: w.text, kind: 'meta', meta_child: w.metaChild }
        : { text: w.text, kind: 'word' })),
    })),
    modifiers: {
      chains: spec.modifiers.chains.map((c) => ({
        locks: c.locksCategory, unlocked_by: c.unlockedByCompleting,
      })),
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
    },
    generation: { attempts: level.attempts },
  };
}
