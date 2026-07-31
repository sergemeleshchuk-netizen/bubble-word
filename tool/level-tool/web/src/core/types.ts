/**
 * Типы ядра. Всё, что здесь описано, — чистые данные без поведения.
 *
 * Разделение, которое важно не потерять:
 *   level_spec      — детерминированный игровой контент, входит в хеш;
 *   build_metadata  — когда и чем собрано, в хеш НЕ входит (SPEC_AUDIT §8).
 */

// --------------------------------------------------------------------------- //
// снимок контентной базы
// --------------------------------------------------------------------------- //

/** Статус связи. Порядок важен: индекс лежит в снимке. */
export const STATUS = {
  approved: 0,
  alternative: 1,
  hard_only: 2,
  candidate: 3,
  rejected: 4,
} as const;

export type StatusCode = 0 | 1 | 2 | 3 | 4;

export interface SnapshotCategory {
  /** ключ, стабильный идентификатор */
  k: string;
  /** отображаемое имя — оно же слово-пузырь, если категория мета-ребёнок */
  l: string;
  /** правило «что тут лежит» человеческими словами */
  r: string;
  /** доминирующий тип связи */
  rel: string;
  /** тематическая сфера */
  th: string;
  /** базовая сложность 0..1, может отсутствовать */
  d: number | null;
}

export interface SnapshotWord {
  /** отображаемый текст */
  t: string;
  /** нормализованная форма — ключ идентичности */
  n: string;
  /** частотность zipf; null означает frequency_unknown (SPEC_AUDIT §13) */
  z: number | null;
  /** 1, если частотнику слово неизвестно */
  u: 0 | 1;
  /** 1, если строка — одиночная лемма нижнего регистра (lexicon_membership) */
  l: 0 | 1;
  /** 1, если имя собственное */
  p: 0 | 1;
  /** число токенов */
  tok: number;
}

/** Связь в снимке: массив вместо объекта, чтобы снимок не раздувался. */
export type SnapshotMembership = [
  wordIndex: number,
  categoryIndex: number,
  status: StatusCode,
  fit: number,
  obviousness: number,
  relation: string,
  senseIndex: number | null,
];

export interface Snapshot {
  schema_version: string;
  statuses: string[];
  constants: { zipf_max: number; top50k_zipf: number; quickwin_zipf: number };
  categories: SnapshotCategory[];
  words: SnapshotWord[];
  senses: { word: number | null; key: string; def: string }[];
  memberships: SnapshotMembership[];
  /** категории, чьё имя существует в базе как слово: материал для мета-связей */
  meta_capable: { category: number; word: number; hosts: number[] }[];
  content_snapshot_hash: string;
  stats?: Record<string, number>;
}

// --------------------------------------------------------------------------- //
// конфиг блока и план уровня
// --------------------------------------------------------------------------- //

export type Modifier = 'chains' | 'halves';

export interface BlockConfig {
  /** диапазон номеров уровней, например [201, 210] */
  levelRange: [number, number];
  /** коридор по числу категорий */
  categoryCorridor: [number, number];
  /** позиции в блоке (1-based), где стоит спайк сложности */
  spikePositions: number[];
  /** позиции передышки */
  recoveryPositions: number[];
  /** целевое число редких слов (zipf < 3) на уровень */
  rarityRange: [number, number];
  /** максимальная глубина мета-леса */
  maxMetaDepth: number;
  /** разрешённые модификаторы */
  allowedModifiers: Modifier[];
  /** тематические сферы: включить / исключить */
  includeThemes: string[];
  excludeThemes: string[];
  /** темы, на которых просят ловушки */
  trapThemes: string[];
  /** окно свежести: слово не повторяется столько уровней */
  wordFreshnessWindow: number;
  /** окно свежести для имён категорий */
  categoryFreshnessWindow: number;
  /** слов в категории, дефолт 4 */
  wordsPerCategory: number;
  /** seed генерации */
  seed: string;
  /**
   * Явный план по позициям блока. Если задан — сильнее коридора и ролей.
   * Профиль блока задаётся настройками, а не кодом: пользователь меняет любую
   * строку, и генератор обязан ей подчиниться либо объяснить отказ.
   */
  categoryPlan?: number[];
  metaPlan?: number[];
}

export type LevelRole = 'entry' | 'growth' | 'recovery' | 'peak' | 'spike' | 'exit';

export interface LevelPlan {
  levelId: number;
  /** позиция в блоке, 1-based */
  position: number;
  role: LevelRole;
  categoryCount: number;
  metaCount: number;
  metaDepthTarget: number;
  rareTarget: number;
  trapTarget: number;
  chainCount: number;
  /** целевой коридор оценок */
  targetDifficulty: [number, number];
  targetInterest: [number, number];
  /** K из формулы лимита ходов (TARGET_GAME_OBSERVATIONS §3) */
  moveLimitK: number;
}

// --------------------------------------------------------------------------- //
// уровень
// --------------------------------------------------------------------------- //

export interface LevelWord {
  text: string;
  /** 'word' — обычный пузырь; 'meta' — имя собранной категории */
  kind: 'word' | 'meta';
  /** ключ дочерней категории, если kind = meta */
  metaChild?: string;
  zipf: number | null;
  frequencyUnknown: boolean;
  relation?: string;
  fit?: number;
  obviousness?: number;
}

export interface LevelCategory {
  key: string;
  label: string;
  rule: string;
  theme: string;
  words: LevelWord[];
  /** глубина в мета-лесу: 0 — корень (никого не ждёт) */
  metaDepth: number;
  /** ключ родителя, если эта категория идёт словом в другую */
  parentKey: string | null;
  isQuickwin: boolean;
}

export interface Trap {
  word: string;
  /** категория, где слово действительно живёт */
  home: string;
  /** категория, куда правдоподобно тянет */
  decoy: string;
  homeObviousness: number;
  decoyFit: number;
  decoyObviousness: number;
}

export interface HalfSplit {
  word: string;
  home: string;
  fragments: [string, string];
  fragmentsAreWords: boolean;
}

export interface Chain {
  locksCategory: string;
  unlockedByCompleting: string;
}

export interface LevelSpec {
  levelId: number;
  schemaVersion: string;
  board: {
    categoriesCount: number;
    wordsPerCategory: number;
    /** производное поле: 4 × категорий − мета (SPEC_AUDIT §1) */
    startBubbles: number;
    /** одновременно на поле; остальное досыпается (TARGET_GAME_OBSERVATIONS §5) */
    boardCapacity: number;
    moveFloor: number;
    moveLimit: number;
    moveLimitK: number;
    moveLimitPolicy: 'conservative';
  };
  categories: LevelCategory[];
  traps: Trap[];
  halves: HalfSplit[];
  modifiers: { chains: Chain[]; frozenBubbles: []; hiddenBubbles: [] };
}

// --------------------------------------------------------------------------- //
// результаты проверок и оценок
// --------------------------------------------------------------------------- //

export type Severity = 'hard' | 'soft';

export interface ValidationIssue {
  code: string;
  severity: Severity;
  /** человекочитаемое объяснение: что именно нарушено */
  message: string;
  /** затронутые сущности */
  entities: string[];
  /** что можно сделать */
  suggestion?: string;
}

export interface ValidationResult {
  passed: boolean;
  checks: { code: string; passed: boolean; severity: Severity; detail: string }[];
  issues: ValidationIssue[];
}

export interface SolutionCount {
  /** 0 — уровень сломан, 1 — PASS, 2 — найдено минимум два (двусмысленность) */
  count: 0 | 1 | 2;
  /** узлов перебора: показывает, что счёт не был обрезан по лимиту */
  nodesVisited: number;
  exhausted: boolean;
  /** пример второй раскладки, если она есть */
  secondSolutionExample?: { category: string; words: string[] }[];
}

export interface DifficultyBreakdown {
  /** откалибровано на 199 референсных уровнях */
  base: Record<string, number>;
  /**
   * объявленные продуктовые веса: референс их НЕ идентифицирует.
   * Мета-связи, глубина и быстрые победы живут здесь, а не в base —
   * см. docs/SCORING.md §7. Граница между измеренным и решённым видна
   * в разбивке и в интерфейсе.
   */
  declared: Record<string, number>;
  /** двусмысленность: эмпирика решателя и смежность категорий */
  semantic: Record<string, number>;
  /** модификаторы и теснота лимита ходов */
  mechanical: Record<string, number>;
  baseTotal: number;
  declaredTotal: number;
  semanticTotal: number;
  mechanicalTotal: number;
  value: number;
  explanation: string[];
  scoringVersion: string;
}

export interface InterestBreakdown {
  clarity: number;
  variety: number;
  aha: number;
  freshness: number;
  value: number;
  explanation: string[];
  scoringVersion: string;
}

// --------------------------------------------------------------------------- //
// сборка блока
// --------------------------------------------------------------------------- //

export interface GeneratedLevel {
  plan: LevelPlan;
  spec: LevelSpec;
  validation: ValidationResult;
  solutions: SolutionCount;
  difficulty: DifficultyBreakdown;
  interest: InterestBreakdown;
  /** сколько попыток понадобилось и что отклонялось */
  attempts: GenerationAttempt[];
  levelSpecHash: string;
}

export interface GenerationAttempt {
  index: number;
  outcome: 'accepted' | 'rejected';
  stage: string;
  reason: string;
  relaxations: string[];
}

export interface GenerationFailure {
  levelId: number;
  /** почему не сошлось — человеческим языком */
  reason: string;
  /** что предлагается ослабить, в порядке предпочтения */
  suggestions: string[];
  attempts: GenerationAttempt[];
}

export interface BlockResult {
  config: BlockConfig;
  contentSnapshotHash: string;
  generatorVersion: string;
  levels: GeneratedLevel[];
  failures: GenerationFailure[];
  packHash: string;
}
