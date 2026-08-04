/**
 * Семантический валидатор. Детерминированный, без модели.
 *
 * Каждая проверка возвращает машинный код, человеческое объяснение, затронутые
 * сущности и предложение, что делать. Hard-инварианты не ослабляются никогда:
 * они и есть определение «уровень не сломан».
 */
import type {
  DecadeGates, LevelSpec, ValidationIssue, ValidationResult, Severity, SolutionCount,
} from './types.ts';
import { STATUS, ZIPF_LEVEL_TOLERANCE } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import type { StructuralMetrics } from './structuralMetrics.ts';
import { checkDeal } from './deal.ts';
import { metaIconFor } from './metaIcons.ts';
import { BOARD_CAPACITY, moveFloor, moveLimit, startBubbles } from './levelMath.ts';

export interface ValidationContext {
  index: ContentIndex;
  solutions?: SolutionCount;
  /** структура задачи: вход в уровень, развилки, оспариваемые слоты */
  structural?: StructuralMetrics;
  /** окна свежести и история пакета */
  history?: {
    wordLastLevel: Map<string, number>;
    categoryLastLevel: Map<string, number>;
    wordWindow: number;
    categoryWindow: number;
  };
  /** хеши четвёрок референса: проверка, что уровень не копия чужого контента */
  referenceQuadrupleHashes?: Set<string>;
  /**
   * Режим проверки на копирование референса.
   *
   *   off  — не проверяем (ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ)
   *   soft — сообщаем, но уровень не браковываем
   *   hard — уровень с четвёркой референса не проходит
   *
   * Раньше проверка была жёстко hard и включалась сама, стоило файлу с хешами
   * оказаться на диске. Пока своя база не наполнена, это мешает: почти любая
   * очевидная четвёрка вроде «красный, синий, зелёный, жёлтый» совпадает с чужой
   * не потому, что её списали, а потому что она одна такая. Вернём в hard, когда
   * база будет полной, — либо когда рядом появится отдельная база референсов и
   * сравнивать будет с чем осмысленно.
   */
  referenceNovelty?: 'off' | 'soft' | 'hard';
  /** максимальная разрешённая глубина мета */
  maxMetaDepth?: number;
  /** хеш-функция для novelty (передаётся, чтобы модуль не зависел от порядка импортов) */
  hashQuadruple?: (words: string[]) => string;
  /**
   * Гейты декады. Если не заданы, соответствующие проверки считаются пройденными:
   * так блок 201-210 остаётся ровно таким, каким сдавался, а калиброванные по
   * декадам блоки получают дополнительные ограничения (docs/DECADE_CALIBRATION.md).
   */
  decadeGates?: DecadeGates;
  /** сколько слов уровня уже встречались раньше в ДРУГОЙ категории; целевой коридор */
  repeatRange?: [number, number];
  repeatCount?: number;
  /** целевое число редких слов (zipf<3) на уровень */
  rareRange?: [number, number];
}

/** Медиана и 25-й процентиль набора чисел. */
function percentile(sorted: number[], p: number): number {
  if (!sorted.length) return 0;
  const i = Math.min(sorted.length - 1, Math.floor(sorted.length * p));
  return sorted[i];
}

interface Check {
  code: string;
  severity: Severity;
  /**
   * Строгость, зависящая от контекста. Нужна там, где проверку можно ослабить
   * параметром: объявленная severity остаётся максимальной, а фактическая
   * считается на прогоне. Hard-инварианты своей severityOf не имеют — их
   * ослабить нельзя по определению.
   */
  severityOf?: (ctx: ValidationContext) => Severity;
  run: (spec: LevelSpec, ctx: ValidationContext) => { passed: boolean; detail: string;
    entities?: string[]; suggestion?: string };
}

function allWords(spec: LevelSpec): { text: string; category: string; kind: string }[] {
  return spec.categories.flatMap((c) =>
    c.words.map((w) => ({ text: w.text, category: c.key, kind: w.kind })));
}

const CHECKS: Check[] = [
  {
    code: 'SCHEMA_VALID',
    severity: 'hard',
    run: (spec) => {
      const problems: string[] = [];
      if (!spec.levelId) problems.push('нет levelId');
      if (!spec.categories.length) problems.push('нет категорий');
      for (const c of spec.categories) {
        if (!c.key || !c.label) problems.push(`категория без ключа или имени: ${c.key || '?'}`);
        if (c.words.some((w) => !w.text)) problems.push(`пустое слово в ${c.key}`);
      }
      return { passed: problems.length === 0,
        detail: problems.length ? problems.join('; ') : 'структура соответствует схеме',
        entities: problems };
    },
  },
  {
    code: 'CATEGORY_SIZE',
    severity: 'hard',
    run: (spec) => {
      const bad = spec.categories.filter((c) => c.words.length !== spec.board.wordsPerCategory);
      return {
        passed: bad.length === 0,
        detail: bad.length
          ? `категорий с неверным числом слов: ${bad.length}`
          : `во всех ${spec.categories.length} категориях ровно ${spec.board.wordsPerCategory} слова`,
        entities: bad.map((c) => `${c.key} (${c.words.length})`),
        suggestion: 'генератор обязан добирать ровно 4 слова; проверить назначение',
      };
    },
  },
  {
    code: 'WORD_OCCURRENCE',
    severity: 'hard',
    run: (spec) => {
      const seen = new Map<string, string[]>();
      for (const w of allWords(spec)) {
        const key = w.text.toLowerCase();
        seen.set(key, [...(seen.get(key) ?? []), w.category]);
      }
      const dup = Array.from(seen.entries()).filter(([, cats]) => cats.length > 1);
      return {
        passed: dup.length === 0,
        detail: dup.length ? `слов, спавнящихся дважды: ${dup.length}` : 'повторов слова нет',
        entities: dup.map(([w, cats]) => `${w}: ${cats.join(', ')}`),
        suggestion: 'слово может занимать только один слот на уровне',
      };
    },
  },
  {
    code: 'ASSIGNED_HOME',
    severity: 'hard',
    run: (spec, ctx) => {
      const bad: string[] = [];
      for (const category of spec.categories) {
        const cat = ctx.index.categoryIndex(category.key);
        if (cat === undefined) { bad.push(`${category.key}: нет в снимке базы`); continue; }
        for (const word of category.words) {
          if (word.kind === 'meta') continue;                  // дом мета-пузыря структурный
          const wi = ctx.index.wordIndex(word.text.toLowerCase());
          if (wi === undefined) { bad.push(`${word.text}: нет в снимке базы`); continue; }
          const has = ctx.index.categoryMemberships(cat, STATUS.approved)
            .some((m) => m.word === wi);
          if (!has) bad.push(`${word.text} не имеет approved-связи с ${category.key}`);
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `слов без утверждённого дома: ${bad.length}`
          : 'у каждого слова есть утверждённая связь со своей категорией',
        entities: bad,
      };
    },
  },
  {
    code: 'APPROVED_CONTENT_ONLY',
    severity: 'hard',
    run: (spec, ctx) => {
      const bad: string[] = [];
      for (const category of spec.categories) {
        const cat = ctx.index.categoryIndex(category.key);
        if (cat === undefined) continue;
        for (const word of category.words) {
          if (word.kind === 'meta') continue;
          const wi = ctx.index.wordIndex(word.text.toLowerCase());
          if (wi === undefined) continue;
          const m = ctx.index.categoryMemberships(cat, STATUS.hard_only)
            .find((x) => x.word === wi);
          if (m && m.status !== STATUS.approved) {
            bad.push(`${word.text} → ${category.key}: статус ${ctx.index.snapshot.statuses[m.status]}`);
          }
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `связей не в статусе approved: ${bad.length}`
          : 'весь контент уровня утверждён',
        entities: bad,
        suggestion: 'кандидаты и hard_only не имеют права быть домом слова',
      };
    },
  },
  {
    code: 'GLOBAL_SOLUTION_COUNT',
    severity: 'hard',
    run: (spec, ctx) => {
      if (!ctx.solutions) {
        return { passed: false, detail: 'счёт решений не выполнен' };
      }
      const { count, exhausted, nodesVisited, secondSolutionExample } = ctx.solutions;
      if (count === 1 && !exhausted) {
        // обрезанный перебор — это «не знаем», а не «единственно». Вторая
        // раскладка могла лежать за лимитом узлов, и тогда PASS был бы ложью
        return {
          passed: false,
          detail: `перебор обрезан по лимиту узлов (${nodesVisited}): единственность `
            + 'решения не доказана',
          suggestion: 'упростить уровень или поднять лимит узлов и пересчитать; '
            + 'состояние «неизвестно» в production не пропускаем',
        };
      }
      if (count === 1) {
        return { passed: true,
          detail: `ровно одна полная раскладка, перебор исчерпан (${nodesVisited} узлов)` };
      }
      if (count === 0) {
        return { passed: false, detail: 'ни одной полной раскладки: уровень нерешаем',
          suggestion: 'ошибка генератора, не контента' };
      }
      const example = secondSolutionExample
        ?.filter((s, i) => s.words.join(',') !== undefined && i < 3)
        .map((s) => `${s.category}: ${s.words.join(', ')}`) ?? [];
      return {
        passed: false,
        detail: 'найдено минимум две полные раскладки: уровень семантически двусмыслен',
        entities: example,
        suggestion: 'убрать одну из конкурирующих категорий или заменить спорное слово',
      };
    },
  },
  {
    // вход в уровень. Игрок бросает не там, где трудно, а там, где нет
    // никакого прогресса: доля уходов концентрируется в состоянии
    // «ноль собранных групп» (docs/SCORING.md §11)
    code: 'OPENING_CATEGORY',
    severity: 'soft',
    run: (spec, ctx) => {
      if (!ctx.structural) {
        return { passed: true, detail: 'структурные метрики не переданы: проверка пропущена' };
      }
      const { openingCategories } = ctx.structural;
      if (openingCategories > 0) {
        return { passed: true,
          detail: `${openingCategories} категорий можно закрыть сразу: вход в уровень есть` };
      }
      return {
        passed: false,
        detail: 'ни одной категории нельзя закрыть сразу: каждый первый ход — гипотеза',
        suggestion: 'дать уровню одну категорию из однодомных слов — это вход, '
          + 'а не поблажка по сложности',
      };
    },
  },
  {
    // уровень, который раскладывается без единой развилки, — работа, а не
    // головоломка: пересобирать гипотезу негде, значит и «ага» взяться неоткуда
    code: 'DEDUCTION_ONLY',
    severity: 'soft',
    run: (spec, ctx) => {
      if (!ctx.structural) {
        return { passed: true, detail: 'структурные метрики не переданы: проверка пропущена' };
      }
      if (!ctx.structural.deductionOnly) {
        return { passed: true,
          detail: `дедукция доходит до ${ctx.structural.forcedSteps} слов, дальше выбор` };
      }
      return {
        passed: false,
        detail: 'уровень раскладывается чистой дедукцией: развилок нет',
        suggestion: 'добавить слово со вторым правдоподобным домом — иначе уровень '
          + 'проходится как рутина',
      };
    },
  },
  {
    code: 'META_PARENT_COUNT',
    severity: 'hard',
    run: (spec) => {
      const parents = new Map<string, string[]>();
      for (const c of spec.categories) {
        for (const w of c.words) {
          if (w.kind === 'meta' && w.metaChild) {
            parents.set(w.metaChild, [...(parents.get(w.metaChild) ?? []), c.key]);
          }
        }
      }
      const bad = Array.from(parents.entries()).filter(([, ps]) => ps.length > 1);
      return {
        passed: bad.length === 0,
        detail: bad.length ? `категорий с двумя родителями: ${bad.length}`
          : 'у каждой мета-категории не больше одного родителя',
        entities: bad.map(([c, ps]) => `${c} ← ${ps.join(', ')}`),
      };
    },
  },
  {
    code: 'META_FOREST_ACYCLIC',
    severity: 'hard',
    run: (spec) => {
      // ЛЕС, а не дерево: связность не требуется и не проверяется (SPEC_AUDIT §2)
      const parentOf = new Map<string, string>();
      for (const c of spec.categories) {
        for (const w of c.words) {
          if (w.kind === 'meta' && w.metaChild) parentOf.set(w.metaChild, c.key);
        }
      }
      const cycles: string[] = [];
      for (const start of parentOf.keys()) {
        const path = [start];
        let cursor = parentOf.get(start);
        while (cursor !== undefined) {
          if (path.includes(cursor)) { cycles.push([...path, cursor].join(' → ')); break; }
          path.push(cursor);
          cursor = parentOf.get(cursor);
          if (path.length > 12) break;
        }
      }
      return {
        passed: cycles.length === 0,
        detail: cycles.length ? `циклов в мета-лесу: ${cycles.length}`
          : `мета-лес ацикличен, связей ${parentOf.size}`,
        entities: cycles,
      };
    },
  },
  {
    /*
     * Картинка на пузыре (core/metaIcons.ts) — hard-инвариант формы, а не вкуса.
     * Проверяется три вещи, и каждая ломает уровень по-своему:
     *   картинка у обычного слова — игрок не сможет её прочитать: у обычного
     *     слова нет категории, чьё имя значок называет;
     *   значок не из словаря — «простое имя» решает словарь, иначе на поле
     *     появится ребус;
     *   два одинаковых значка — два разных пузыря выглядят одним.
     * Количество (четверть мета-пузырей) здесь НЕ проверяется: словарь покрывает
     * не все имена, и уровень, где простых имён не нашлось, законен.
     */
    code: 'META_ICONS_VALID',
    severity: 'hard',
    run: (spec) => {
      const wrongKind: string[] = [];
      const unknown: string[] = [];
      const seen = new Map<string, string>();
      const duplicate: string[] = [];
      for (const c of spec.categories) {
        for (const w of c.words) {
          if (!w.icon) continue;
          if (w.kind !== 'meta') { wrongKind.push(`${c.key}: ${w.text}`); continue; }
          if (metaIconFor(w.text) !== w.icon) { unknown.push(`${w.text} ${w.icon}`); continue; }
          const owner = seen.get(w.icon);
          if (owner !== undefined) duplicate.push(`${w.icon}: ${owner} и ${w.text}`);
          else seen.set(w.icon, w.text);
        }
      }
      const bad = [...wrongKind, ...unknown, ...duplicate];
      return {
        passed: bad.length === 0,
        detail: bad.length === 0
          ? `картинок на мета-пузырях: ${seen.size}`
          : `картинки не по правилу: ${bad.length}`,
        entities: bad,
        suggestion: bad.length === 0 ? undefined
          : 'картинку несёт только мета-пузырь с именем из словаря metaIcons.ts, '
            + 'и одна картинка на уровень',
      };
    },
  },
  {
    code: 'META_DEPTH_WITHIN_CONFIG',
    severity: 'soft',
    run: (spec, ctx) => {
      const cap = ctx.maxMetaDepth ?? 3;
      const deepest = Math.max(0, ...spec.categories.map((c) => c.metaDepth));
      return {
        passed: deepest <= cap,
        detail: `максимальная глубина мета ${deepest}, разрешено ${cap}`,
        entities: spec.categories.filter((c) => c.metaDepth > cap).map((c) => c.key),
      };
    },
  },
  {
    code: 'CHAIN_ACYCLIC',
    severity: 'hard',
    run: (spec) => {
      const unlocks = new Map<string, string>();
      for (const chain of spec.modifiers.chains) {
        unlocks.set(chain.locksCategory, chain.unlockedByCompleting);
      }
      const cycles: string[] = [];
      for (const start of unlocks.keys()) {
        const path = [start];
        let cursor = unlocks.get(start);
        while (cursor !== undefined) {
          if (path.includes(cursor)) { cycles.push([...path, cursor].join(' → ')); break; }
          path.push(cursor);
          cursor = unlocks.get(cursor);
          if (path.length > 12) break;
        }
      }
      const lockedQuickwins = spec.modifiers.chains.filter((chain) =>
        spec.categories.find((c) => c.key === chain.locksCategory)?.isQuickwin);
      const passed = cycles.length === 0 && lockedQuickwins.length === 0;
      return {
        passed,
        detail: cycles.length
          ? `цикл зависимостей цепей: игрок заперт навсегда`
          : lockedQuickwins.length
            ? 'цепь заперла категорию быстрой победы: у игрока нет точки входа'
            : `цепей ${spec.modifiers.chains.length}, граф зависимостей ацикличен`,
        entities: [...cycles, ...lockedQuickwins.map((c) => c.locksCategory)],
      };
    },
  },
  {
    code: 'START_BUBBLE_COUNT',
    severity: 'hard',
    run: (spec) => {
      const metaCount = spec.categories.reduce((n, c) =>
        n + c.words.filter((w) => w.kind === 'meta').length, 0);
      const expected = startBubbles(spec.categories.length, metaCount, spec.board.wordsPerCategory);
      return {
        passed: expected === spec.board.startBubbles,
        detail: `заявлено ${spec.board.startBubbles}, по формуле `
          + `4 × ${spec.categories.length} − ${metaCount} = ${expected}`,
        suggestion: 'число пузырей — производное поле, задавать его руками нельзя',
      };
    },
  },
  {
    /*
     * Выкладка обязана раздать каждое спавнящееся слово ровно один раз.
     * Потерянное слово делает категорию несобираемой уже в игре, а не в отчёте:
     * игрок будет искать четвёртый пузырь, которого в уровне нет. Проверка hard
     * именно поэтому — брак не виден ни глазами, ни решателем, который читает
     * категории, а не выкладку.
     */
    code: 'DEAL_COMPLETE',
    severity: 'hard',
    run: (spec) => {
      const problems = checkDeal(spec, spec.deal);
      return {
        passed: problems.length === 0,
        detail: problems.length === 0
          ? `на поле ${spec.deal.start.length} из ${spec.board.startBubbles}, `
            + `в очереди ${spec.deal.queue.length}`
          : problems.slice(0, 5).join('; '),
        suggestion: 'выкладку считает core/deal.ts из спека, руками её не правят',
        entities: problems.slice(0, 5),
      };
    },
  },
  {
    code: 'MOVE_LIMIT_SANE',
    severity: 'hard',
    run: (spec) => {
      const floor = moveFloor(spec.categories.length, spec.halves.length,
        spec.board.wordsPerCategory);
      // туториал без лимита: K и лимит обязаны быть null ОБА, иначе это
      // рассинхрон плана и уровня, а не осознанный режим
      if (spec.board.moveLimitK === null || spec.board.moveLimit === null) {
        const consistent = spec.board.moveLimitK === null && spec.board.moveLimit === null;
        return {
          passed: consistent,
          detail: consistent
            ? `лимита ходов нет (туториал), минимум мерджей ${floor}`
            : `рассинхрон: moveLimit ${spec.board.moveLimit}, K ${spec.board.moveLimitK}`,
          suggestion: 'режим «без лимита» задаётся одновременно в K и в лимите',
        };
      }
      // блокирующий модификатор (лёд, «?», цепь-линия) мерджей не добавляет,
      // но стесняет выбор: генератор даёт за него ход форы, формула это знает
      const blocker = spec.modifiers.frozenBubbles.length > 0
        || spec.modifiers.hiddenBubbles.length > 0
        || spec.modifiers.chainLine !== null;
      const expected = moveLimit(floor, spec.board.moveLimitK) + (blocker ? 1 : 0);
      const ok = spec.board.moveLimit === expected && spec.board.moveLimit >= floor;
      return {
        passed: ok,
        detail: `лимит ${spec.board.moveLimit}, минимум мерджей ${floor}, `
          + `K = ${spec.board.moveLimitK} → ожидалось ${expected}`
          + (blocker ? ' (включая +1 за блокирующий модификатор)' : ''),
        suggestion: 'лимит ниже минимума делает уровень непроходимым',
      };
    },
  },
  {
    code: 'QUICK_WIN_PRESENT',
    severity: 'hard',
    run: (spec, ctx) => {
      const quickwins = spec.categories.filter((c) => c.isQuickwin);
      // перепроверяем независимо от флага: без мета-слов и все слова частотные
      const verified = spec.categories.filter((c) => {
        if (c.words.some((w) => w.kind === 'meta')) return false;
        return c.words.every((w) => w.zipf !== null
          && w.zipf >= ctx.index.quickwinThreshold);
      });
      return {
        passed: verified.length >= 1,
        detail: verified.length
          ? `категорий быстрой победы ${verified.length}: ${verified.map((c) => c.key).join(', ')}`
          : 'нет ни одной категории без мета-слов со всеми частотными словами',
        entities: quickwins.map((c) => c.key),
        suggestion: 'инвариант открытой двери: игроку нужна точка входа без раздумий',
      };
    },
  },
  {
    code: 'RECOGNIZABILITY',
    severity: 'hard',
    run: (spec, ctx) => {
      const words = allWords(spec);
      const threshold = ctx.index.topFrequencyThreshold;
      const unknown: string[] = [];
      for (const category of spec.categories) {
        for (const w of category.words) {
          if (w.kind === 'meta') continue;
          if (w.zipf === null || w.zipf < threshold) unknown.push(w.text);
        }
      }
      const share = 1 - unknown.length / Math.max(1, words.length);
      return {
        passed: share >= 0.9,
        detail: `внутри top-50k ${(share * 100).toFixed(1)}% пузырей `
          + `(порог zipf ${threshold}, вне порога ${unknown.length})`,
        entities: unknown,
        suggestion: 'экзотика дозируется: не более 10% пузырей уровня',
      };
    },
  },
  {
    code: 'NEAR_DUPLICATE_WORDS',
    severity: 'hard',
    run: (spec) => {
      const bad: string[] = [];
      for (const category of spec.categories) {
        const norms = category.words.map((w) => w.text.toLowerCase());
        for (let i = 0; i < norms.length; i += 1) {
          for (let j = i + 1; j < norms.length; j += 1) {
            const [a, b] = [norms[i], norms[j]];
            const [short, long] = a.length <= b.length ? [a, b] : [b, a];
            if (long === `${short}s` || long === `${short}es`) {
              bad.push(`${category.key}: ${a} и ${b}`);
            }
          }
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `пар слов-двойников в одной категории: ${bad.length}`
          : 'слов-двойников внутри категорий нет',
        entities: bad,
        suggestion: 'star и stars рядом читаются как ошибка данных',
      };
    },
  },
  {
    code: 'HALF_COLLISION',
    severity: 'hard',
    run: (spec) => {
      const levelWords = new Set(allWords(spec).map((w) => w.text.toLowerCase()));
      const bad: string[] = [];
      for (const half of spec.halves) {
        for (const fragment of half.fragments) {
          if (levelWords.has(fragment.toLowerCase())) {
            bad.push(`${half.word}: фрагмент «${fragment}» — валидное слово этого уровня`);
          }
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `коллизий половинок: ${bad.length}`
          : spec.halves.length ? `половинок ${spec.halves.length}, коллизий нет`
            : 'половинок нет',
        entities: bad,
        suggestion: 'иначе уровень становится по-настоящему двусмысленным',
      };
    },
  },
  {
    code: 'FRESHNESS',
    severity: 'soft',
    run: (spec, ctx) => {
      if (!ctx.history) return { passed: true, detail: 'история пакета не передана' };
      const { wordLastLevel, categoryLastLevel, wordWindow, categoryWindow } = ctx.history;
      const stale: string[] = [];
      for (const category of spec.categories) {
        const last = categoryLastLevel.get(category.key);
        if (last !== undefined && spec.levelId - last <= categoryWindow) {
          stale.push(`категория ${category.key} была на уровне ${last}`);
        }
        for (const word of category.words) {
          const lastWord = wordLastLevel.get(word.text.toLowerCase());
          if (lastWord !== undefined && spec.levelId - lastWord <= wordWindow) {
            stale.push(`слово ${word.text} было на уровне ${lastWord}`);
          }
        }
      }
      return {
        passed: stale.length === 0,
        detail: stale.length ? `нарушений свежести: ${stale.length}`
          : `свежесть соблюдена (окна: слова ${wordWindow}, категории ${categoryWindow})`,
        entities: stale.slice(0, 10),
      };
    },
  },
  {
    code: 'REFERENCE_NOVELTY',
    severity: 'soft',
    severityOf: (ctx) => (ctx.referenceNovelty === 'hard' ? 'hard' : 'soft'),
    run: (spec, ctx) => {
      // По умолчанию выключено: см. ValidationContext.referenceNovelty.
      const mode = ctx.referenceNovelty ?? 'off';
      if (mode === 'off') {
        return { passed: true, detail: 'проверка на копирование чужих четвёрок выключена (referenceNovelty=off)' };
      }
      if (!ctx.referenceQuadrupleHashes || !ctx.hashQuadruple) {
        return { passed: true, detail: 'хеши чужих четвёрок не переданы: проверка пропущена' };
      }
      const copies: string[] = [];
      for (const category of spec.categories) {
        const hash = ctx.hashQuadruple(category.words.map((w) => w.text));
        if (ctx.referenceQuadrupleHashes.has(hash)) {
          copies.push(`${category.key}: четвёрка совпадает с чужой`);
        }
      }
      return {
        passed: copies.length === 0,
        detail: copies.length ? `точных копий чужих четвёрок: ${copies.length}`
          : 'точных совпадений с чужими четвёрками нет',
        entities: copies,
        suggestion: 'чужие уровни — источник кривой, а не контента',
      };
    },
  },
  {
    /**
     * Запрет пары, объявленный базой. В отличие от UNSEPARABLE_PAIR ниже это не
     * оценка, а решение: `derive-conflicts` посчитал пересечение играбельных
     * пулов и записал пару с причиной и severity. Поэтому severity здесь hard.
     *
     * Генератор такие пары не выдаёт (гейт в selectCategories), но валидатор
     * смотрит и на уровни, собранные не им: руками, импортом, старой выгрузкой.
     */
    code: 'CONFLICT_PAIR',
    severity: 'hard',
    run: (spec, ctx) => {
      const cats = spec.categories
        .map((c) => ({ key: c.key, index: ctx.index.categoryIndex(c.key) }))
        .filter((c): c is { key: string; index: number } => c.index !== undefined);
      const bad: string[] = [];
      for (let i = 0; i < cats.length; i += 1) {
        for (let j = i + 1; j < cats.length; j += 1) {
          const conflict = ctx.index.conflict(cats[i].index, cats[j].index);
          if (!conflict) continue;
          bad.push(`${cats[i].key} и ${cats[j].key}: запрет ${conflict.severity ?? '—'}, `
            + `общих играбельных слов ${conflict.overlap}`);
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `запрещённых базой пар категорий: ${bad.length}`
          : 'запрещённых базой пар на уровне нет',
        entities: bad,
        suggestion: 'запрет снимается в базе (data/seed/_category_meta.json), а не в уровне',
      };
    },
  },
  {
    code: 'UNSEPARABLE_PAIR',
    severity: 'soft',
    run: (spec, ctx) => {
      const cats = spec.categories
        .map((c) => ({ key: c.key, index: ctx.index.categoryIndex(c.key) }))
        .filter((c): c is { key: string; index: number } => c.index !== undefined);
      const bad: string[] = [];
      for (let i = 0; i < cats.length; i += 1) {
        for (let j = i + 1; j < cats.length; j += 1) {
          const a = new Set(ctx.index.categoryMemberships(cats[i].index, STATUS.approved)
            .map((m) => m.word));
          const b = ctx.index.categoryMemberships(cats[j].index, STATUS.approved)
            .map((m) => m.word);
          const shared = b.filter((w) => a.has(w)).length;
          const union = a.size + b.length - shared;
          const jaccard = union > 0 ? shared / union : 0;
          if (jaccard >= 0.35) {
            bad.push(`${cats[i].key} и ${cats[j].key}: пересечение кандидатов `
              + `${(jaccard * 100).toFixed(0)}%`);
          }
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `неразделимых пар категорий: ${bad.length}`
          : 'сильно пересекающихся пар категорий нет',
        entities: bad,
        suggestion: 'такие категории на один уровень не ставят: слова будут двоиться',
      };
    },
  },
  /**
   * Дальше — гейты декады. Все они пропускают уровень, если `ctx.decadeGates`
   * не задан: пресет блока 201-210 их не получает и остаётся байт-в-байт тем же.
   */
  {
    code: 'WORD_FORM_GATE',
    severity: 'hard',
    run: (spec, ctx) => {
      const gates = ctx.decadeGates;
      if (!gates) return { passed: true, detail: 'гейты декады не заданы' };
      const bad: string[] = [];
      for (const category of spec.categories) {
        for (const w of category.words) {
          const tokens = w.text.trim().split(/\s+/).length;
          if (tokens > gates.maxTokens) {
            bad.push(`«${w.text}»: ${tokens} слова, предел ${gates.maxTokens}`);
          }
          if (w.text.replace(/\s/g, '').length > gates.maxWordLen) {
            bad.push(`«${w.text}»: ${w.text.length} букв, предел ${gates.maxWordLen}`);
          }
          // имя собственное определяем по снимку, а не по регистру строки
          const wi = ctx.index.wordIndex(w.text.toLowerCase());
          const isProper = wi !== undefined && ctx.index.words[wi].p === 1;
          if (isProper && (w.zipf === null || w.zipf < gates.minProperNounZipf)) {
            bad.push(`«${w.text}»: имя собственное с zipf ${w.zipf ?? '?'}, `
              + `порог ${gates.minProperNounZipf}`);
          }
        }
      }
      return {
        passed: bad.length === 0,
        detail: bad.length ? `слов вне формы декады: ${bad.length}`
          : `форма слов в норме декады (до ${gates.maxTokens} токенов, `
            + `${gates.maxWordLen} букв, имена собственные от zipf ${gates.minProperNounZipf})`,
        entities: bad,
        suggestion: 'ранние декады однословные и без редких имён собственных: '
          + 'mars 4.27 и egypt 4.45 узнаваемы, steinbeck 2.67 — уже викторина',
      };
    },
  },
  {
    code: 'ZIPF_DISTRIBUTION',
    // soft, потому что цель декады — медиана всей десятки, а не каждого уровня:
    // у самого референса медианы уровней внутри L1-10 гуляют на целый zipf.
    // Строгую проверку среднего по блоку делает checkDecadeFit().
    severity: 'soft',
    run: (spec, ctx) => {
      const gates = ctx.decadeGates;
      if (!gates) return { passed: true, detail: 'гейты декады не заданы' };
      const zs = spec.categories
        .flatMap((c) => c.words)
        .map((w) => w.zipf)
        .filter((z): z is number => z !== null)
        .sort((a, b) => a - b);
      if (!zs.length) return { passed: false, detail: 'ни у одного слова нет частотности' };
      const median = percentile(zs, 0.5);
      const p25 = percentile(zs, 0.25);
      const dMedian = Math.abs(median - gates.zipfMedianTarget);
      const dP25 = Math.abs(p25 - gates.zipfP25Target);
      const ok = dMedian <= ZIPF_LEVEL_TOLERANCE && dP25 <= ZIPF_LEVEL_TOLERANCE;
      return {
        passed: ok,
        detail: `медиана zipf ${median.toFixed(2)} (цель декады ${gates.zipfMedianTarget}), `
          + `p25 ${p25.toFixed(2)} (цель ${gates.zipfP25Target}), допуск на уровень `
          + `±${ZIPF_LEVEL_TOLERANCE}`,
        suggestion: 'узнаваемость — главная ось сложности первых 120 уровней: '
          + 'медиана 4.35 на L1-10 против 3.70 на L121-130',
      };
    },
  },
  {
    code: 'RARE_WORD_BUDGET',
    severity: 'soft',
    run: (spec, ctx) => {
      if (!ctx.rareRange) return { passed: true, detail: 'коридор редкости не задан' };
      const [lo, hi] = ctx.rareRange;
      const rare = spec.categories.flatMap((c) => c.words)
        .filter((w) => w.zipf === null || w.zipf < 3.0);
      return {
        passed: rare.length >= lo && rare.length <= hi,
        detail: `редких слов (zipf<3) ${rare.length}, коридор декады ${lo}-${hi}`,
        entities: rare.map((w) => w.text),
        suggestion: 'экзотика по замеру есть с L4 (aglet, zipf 1.32), но ровно 1-2 '
          + 'слова на уровень — это счётчик, а не пол по частотности',
      };
    },
  },
  {
    code: 'VISIBLE_SHARE',
    severity: 'hard',
    run: (spec, ctx) => {
      const gates = ctx.decadeGates;
      if (!gates) return { passed: true, detail: 'гейты декады не заданы' };
      const total = spec.categories.length * spec.board.wordsPerCategory;
      const capacity = spec.board.boardCapacity || BOARD_CAPACITY;
      const share = capacity / total;
      return {
        passed: share >= gates.visibleShareMin,
        detail: `на поле видно ${(share * 100).toFixed(1)}% уровня `
          + `(${capacity} из ${total}), минимум декады ${(gates.visibleShareMin * 100).toFixed(1)}%`,
        suggestion: 'чем меньше видно, тем меньше пар в поле зрения: это скрытый '
          + 'источник сложности. На L1 видно 100% — потому там и нет лимита ходов',
      };
    },
  },
  {
    code: 'REPEAT_BUDGET',
    severity: 'soft',
    run: (spec, ctx) => {
      const range = ctx.repeatRange ?? ctx.decadeGates?.repeatRange;
      if (!range || ctx.repeatCount === undefined) {
        return { passed: true, detail: 'коридор повторов не задан' };
      }
      const [lo, hi] = range;
      return {
        passed: ctx.repeatCount >= lo && ctx.repeatCount <= hi,
        detail: `слов из прошлых уровней в другой категории: ${ctx.repeatCount}, `
          + `коридор декады ${lo}-${hi}`,
        suggestion: 'повтор слова в ДРУГОЙ категории — самая сильная растущая ось '
          + 'по замеру (2.9 слова на уровень в L1-10 против 28 в L171-180)',
      };
    },
  },
];

export function validateLevel(spec: LevelSpec, ctx: ValidationContext): ValidationResult {
  const checks: ValidationResult['checks'] = [];
  const issues: ValidationIssue[] = [];

  for (const check of CHECKS) {
    const result = check.run(spec, ctx);
    const severity = check.severityOf ? check.severityOf(ctx) : check.severity;
    checks.push({ code: check.code, passed: result.passed,
      severity, detail: result.detail });
    if (!result.passed) {
      issues.push({
        code: check.code,
        severity,
        message: result.detail,
        entities: result.entities ?? [],
        suggestion: result.suggestion,
      });
    }
  }

  return {
    passed: issues.every((i) => i.severity !== 'hard'),
    checks,
    issues,
  };
}

export const CHECK_CODES = CHECKS.map((c) => ({ code: c.code, severity: c.severity }));
