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

/**
 * Готовность категории к автоматической сборке уровня. Считается на стороне
 * базы (`derive-readiness`), не здесь: это свойство контента, а не генератора.
 *   ready        — 4+ слов уровня approved/alternative, пул не перекошен
 *   constrained  — годится, но пул тонкий или перекошен в hard_only
 *   curated_only — только вручную собранные четвёрки (парное правило)
 *   hard_only    — нормальных слов нет, только сложные уровни
 *   blocked      — четвёрку не собрать даже со hard_only
 */
export type Readiness =
  | 'ready' | 'constrained' | 'curated_only' | 'hard_only' | 'blocked' | 'unknown';

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
  /** готовность категории; в снимках 1.0 поля нет */
  rd?: Readiness;
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
  /** игровая сложность связи 0..1; отдельная ось от статуса (снимок 2.0) */
  gameplayDifficulty?: number | null,
  /** битовая маска risk-флагов по порядку Snapshot.risk_flags (снимок 2.0) */
  riskMask?: number,
];

/**
 * Запрет на сочетание двух категорий в одном уровне.
 *
 * Решение принято на стороне контента: `derive-conflicts` считает пересечение
 * играбельных пулов и сохраняет пару с причиной. Генератор его исполняет, а не
 * пересчитывает — иначе одна и та же пара разрешена в базе и запрещена в
 * инструменте (или наоборот), и спорить будет нечем.
 */
export type SnapshotConflict = [
  categoryA: number,
  categoryB: number,
  /** индекс в Snapshot.conflict_types: do_not_pair | needs_disjoint_words */
  type: number,
  /** P0/P1/…, как решено в базе */
  severity: string | null,
  /** сколько играбельных слов у пулов общие */
  overlap: number,
];

/** Проверенная четвёрка: прошла solver единственности на стороне базы. */
export type SnapshotQuartet = [
  category: number,
  words: number[],
  /** индекс в Snapshot.quartet_tiers: normal | hard */
  tier: number,
];

export interface Snapshot {
  schema_version: string;
  statuses: string[];
  /** порядок risk-флагов: индекс = бит в маске связи (снимок 2.0) */
  risk_flags?: string[];
  conflict_types?: string[];
  quartet_tiers?: string[];
  constants: { zipf_max: number; top50k_zipf: number; quickwin_zipf: number };
  categories: SnapshotCategory[];
  words: SnapshotWord[];
  senses: { word: number | null; key: string; def: string }[];
  memberships: SnapshotMembership[];
  /** категории, чьё имя существует в базе как слово: материал для мета-связей */
  meta_capable: { category: number; word: number; hosts: number[] }[];
  /** пары категорий, которые нельзя ставить в один уровень (снимок 2.0) */
  conflicts?: SnapshotConflict[];
  /** четвёрки, проверенные solver'ом базы (снимок 2.0) */
  quartets?: SnapshotQuartet[];
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
  /**
   * Гейты декады: чем уровень 1-10 отличается от уровня 191-200 не размером,
   * а содержимым. Собираются из `DECADE_PROFILES` (см. decadeProfiles.ts).
   *
   * Поле необязательное сознательно: пресет блока 201-210 его не задаёт, поэтому
   * нормализованный конфиг для него не меняется и хеш сдаваемого пакета остаётся
   * прежним. Как только гейты заданы — они входят в хеш, потому что влияют
   * на контент.
   */
  decadeGates?: DecadeGates;
}

export interface DecadeGates {
  /**
   * Потолок базовой сложности категории (поле `base_difficulty` базы, 0.1-0.6).
   *
   * База знает, что COLORS и FARM ANIMALS проще, чем UNIVERSITIES и LOCKSMITH
   * WORDS, — а генератор это поле не читал вовсе. Отсюда и жалоба на пакет
   * T1-T10: «простые якорные категории не взяты», уровень 1 собирался из
   * категорий d=0.4 при том, что в базе есть d=0.1.
   *
   * Числа не из референса: у референсных категорий нашего d нет. Это шкала базы —
   * ранние декады тяготеют к её нижней половине, поздние ко всей.
   *
   * Это ЦЕЛЬ, а не запрет: категории выше цели остаются доступны, просто ценятся
   * ниже при отборе. Жёстким фильтром на всю декаду быть нельзя — пробовал:
   * пул сужался настолько, что мета-пары кончались к концу декады (шесть декад
   * из двадцати уходили в хвост 0-0-2 при коридоре 3-6).
   */
  categoryDifficultyTarget: number;
  /**
   * Потолок для уровня-туториала — вот он жёсткий. На L1 оригинала лежат коровы,
   * цвета, машины, компас и дни недели; там нет места «сложной, но красивой»
   * категории, и пул из одной декады этот запрет выдерживает.
   */
  tutorialCategoryDifficultyMax: number;
  /** предел числа токенов в ответе: 1 = только однословные */
  maxTokens: number;
  /** предел длины слова в буквах */
  maxWordLen: number;
  /** минимальный zipf для имени собственного */
  minProperNounZipf: number;
  /**
   * Пол частотности: ниже него слово в уровень не берётся вообще.
   *
   * До 02.08 такого запрета не было ни одного. Редкость слов существовала только
   * как ЦЕЛЬ (`rareTarget`, порог `zipf < 3.0`) — то есть как рычаг сложности,
   * которым можно добрать D. Пола не было, и это давало вот что: в сданном
   * пакете TOP ни одного слова ниже 3.0 нет, отчёт честно печатает «редких слов
   * 0», а на поле при этом лежат `quail` 3.13, `obituary` 3.41, `congestion`
   * 3.66, `veal` 3.08, `epoxy` 3.10, `tungsten` 3.12, `basilica` 3.08. Порог
   * стоял ровно там, где под него ничего не попадает, и метрика отчитывалась об
   * успехе. Владелец продукта посмотрел два уровня в прототипе и назвал эти
   * слова первыми.
   *
   * Замер базы под пол 3.75: связей выше порога 8923, категорий, способных дать
   * четвёрку целиком, — 931 из 1265, четвёрок без повтора слова 1773. Пакету из
   * 20 уровней нужно 192 четвёрки, десятке — 96, так что пол проходит с запасом;
   * упирается он только в цель 1000 уровней (нужно ~12800 связей).
   *
   * Пол постоянный для всех декад. Соблазн опускать его к поздним уровням есть —
   * в записи оригинала редкость слов даёт +0.68 к D, — но жалобы пришли как раз
   * на уровни 17 и 20, то есть поздние. Сложность растёт числом категорий,
   * мета-цепями, ловушками и лимитом ходов, а не незнакомыми словами.
   */
  minWordZipf: number;
  /** целевая медиана частотности слов уровня */
  zipfMedianTarget: number;
  /** целевой 25-й процентиль частотности */
  zipfP25Target: number;
  /** минимальная доля уровня, видимая на поле одновременно */
  visibleShareMin: number;
  /** коридор повторов слова из прошлых уровней в ДРУГОЙ категории */
  repeatRange: [number, number];
  /** первый уровень блока — туториал (только для блока, начинающегося с 1) */
  tutorialFirstLevel: boolean;
}

/**
 * Допуски по частотности.
 *
 * Важное различие, на котором легко ошибиться. Цель из таблицы декад (медиана
 * 4.35 для L1-10) — это медиана ВСЕЙ декады, а не каждого уровня. Замер по
 * референсу: внутри L1-10 медианы отдельных уровней идут 4.92, 4.42, 4.53, 4.66,
 * 4.04, 4.07, 4.65, 3.97, 3.95, 4.42 — разброс почти целый zipf, sd 0.32.
 * Поэтому на уровень допуск широкий (≈2σ), а строгий держится на блоке целиком.
 */
export const ZIPF_BLOCK_TOLERANCE = 0.15;
export const ZIPF_LEVEL_TOLERANCE = 0.65;

export type LevelRole = 'tutorial' | 'entry' | 'growth' | 'recovery' | 'peak' | 'spike' | 'exit';

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
  /** K из формулы лимита ходов (TARGET_GAME_OBSERVATIONS §3); null = без лимита */
  moveLimitK: number | null;
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

/** Один пузырь выкладки: текст и категория, которой слово принадлежит. */
export interface DealBubble {
  word: string;
  /** ключ категории (`LevelCategory.key`) */
  category: string;
}

/**
 * Первая выкладка уровня: что лежит на поле на старте и в каком порядке
 * приходит досыпка. Правила и обоснование — в `core/deal.ts`.
 */
export interface Deal {
  /** пузыри на поле в момент старта */
  start: DealBubble[];
  /** очередь досыпки строго в этом порядке */
  queue: DealBubble[];
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
    /** null = без лимита ходов (туториальный первый уровень, как L1 референса) */
    moveLimit: number | null;
    moveLimitK: number | null;
    moveLimitPolicy: 'conservative';
  };
  categories: LevelCategory[];
  /**
   * Первая выкладка. Часть уровня, а не дело клиента: см. `core/deal.ts`.
   * Входит в хеш уровня — уровень с другой выкладкой это другой уровень.
   */
  deal: Deal;
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
  /** структура задачи: вход, развилки, оспариваемые слоты (не входит в D и I) */
  structural?: import('./structuralMetrics.ts').StructuralMetrics;
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
