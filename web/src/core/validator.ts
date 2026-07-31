/**
 * Семантический валидатор. Детерминированный, без модели.
 *
 * Каждая проверка возвращает машинный код, человеческое объяснение, затронутые
 * сущности и предложение, что делать. Hard-инварианты не ослабляются никогда:
 * они и есть определение «уровень не сломан».
 */
import type {
  LevelSpec, ValidationIssue, ValidationResult, Severity, SolutionCount,
} from './types.ts';
import { STATUS } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import { moveFloor, moveLimit, startBubbles } from './levelMath.ts';

export interface ValidationContext {
  index: ContentIndex;
  solutions?: SolutionCount;
  /** окна свежести и история пакета */
  history?: {
    wordLastLevel: Map<string, number>;
    categoryLastLevel: Map<string, number>;
    wordWindow: number;
    categoryWindow: number;
  };
  /** хеши четвёрок референса: проверка, что уровень не копия чужого контента */
  referenceQuadrupleHashes?: Set<string>;
  /** максимальная разрешённая глубина мета */
  maxMetaDepth?: number;
  /** хеш-функция для novelty (передаётся, чтобы модуль не зависел от порядка импортов) */
  hashQuadruple?: (words: string[]) => string;
}

interface Check {
  code: string;
  severity: Severity;
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
      if (count === 1) {
        return { passed: true,
          detail: `ровно одна полная раскладка, перебор ${exhausted ? 'исчерпан' : 'обрезан'}`
            + ` (${nodesVisited} узлов)` };
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
    code: 'MOVE_LIMIT_SANE',
    severity: 'hard',
    run: (spec) => {
      const floor = moveFloor(spec.categories.length, spec.halves.length,
        spec.board.wordsPerCategory);
      const expected = moveLimit(floor, spec.board.moveLimitK);
      const ok = spec.board.moveLimit === expected && spec.board.moveLimit >= floor;
      return {
        passed: ok,
        detail: `лимит ${spec.board.moveLimit}, минимум мерджей ${floor}, `
          + `K = ${spec.board.moveLimitK} → ожидалось ${expected}`,
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
    severity: 'hard',
    run: (spec, ctx) => {
      if (!ctx.referenceQuadrupleHashes || !ctx.hashQuadruple) {
        return { passed: true, detail: 'хеши четвёрок референса не переданы: проверка пропущена' };
      }
      const copies: string[] = [];
      for (const category of spec.categories) {
        const hash = ctx.hashQuadruple(category.words.map((w) => w.text));
        if (ctx.referenceQuadrupleHashes.has(hash)) {
          copies.push(`${category.key}: четвёрка совпадает с референсной`);
        }
      }
      return {
        passed: copies.length === 0,
        detail: copies.length ? `точных копий четвёрок референса: ${copies.length}`
          : 'точных совпадений с четвёрками референса нет',
        entities: copies,
        suggestion: 'референс — источник кривой, а не контента',
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
];

export function validateLevel(spec: LevelSpec, ctx: ValidationContext): ValidationResult {
  const checks: ValidationResult['checks'] = [];
  const issues: ValidationIssue[] = [];

  for (const check of CHECKS) {
    const result = check.run(spec, ctx);
    checks.push({ code: check.code, passed: result.passed,
      severity: check.severity, detail: result.detail });
    if (!result.passed) {
      issues.push({
        code: check.code,
        severity: check.severity,
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
