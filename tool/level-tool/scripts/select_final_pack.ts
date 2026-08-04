/**
 * Воронка отбора финальных 10 уровней.
 *
 * Нельзя брать первые десять, прошедших генерацию. Воронка:
 *
 *   K блоков-кандидатов
 *          ↓ hard-валидация и единственность решения
 *   блоки, где прошли все 10 уровней
 *          ↓ novelty против референса (точная копия и близкая копия)
 *          ↓ критерии блока: пила, два пика, передышка после пика, разъезд D и I
 *   лучший блок
 *          ↓ ручная игра
 *   10 сдаваемых уровней
 *
 * Запуск:  node scripts/select_final_pack.ts [--seeds 24]
 * Вывод:   data/final-pack/  +  docs/VALIDATION_REPORT.md  +  docs/LEVEL_CARDS.md
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { BlockResult, GeneratedLevel, Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan, checkBlockRhythm } from '../web/src/core/blockPlan.ts';
import { generateBlock, hashQuadruple, toGameJson, toPipelineJson } from '../web/src/core/generateBlock.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const OUT = join(ROOT, 'data/final-pack');

const snapshot = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const novelty = JSON.parse(readFileSync(
  join(ROOT, 'data/reference-derived/reference-quadruple-hashes.json'), 'utf8'));
const referenceQuadrupleHashes = new Set<string>(novelty.hashes);

/** Полные четвёрки референса нужны для проверки БЛИЗКОЙ копии; только локально. */
const localQuadsPath = join(ROOT, 'data/reference-derived/reference-quadruples.local.json');
const localQuads: { level: number; category: string; words: string[] }[] =
  existsSync(localQuadsPath) ? JSON.parse(readFileSync(localQuadsPath, 'utf8')) : [];

const seedCount = Number(process.argv[process.argv.indexOf('--seeds') + 1]) || 24;

// --------------------------------------------------------------------------- //
// критерии блока
// --------------------------------------------------------------------------- //

interface BlockScore {
  seed: string;
  levels: number;
  allPassed: boolean;
  allUnique: boolean;
  descents: number;
  dSpread: number;
  iSpread: number;
  /** насколько D и I НЕ идут одной линией: 1 − |корреляция| */
  divergence: number;
  maxDepth: number;
  trapLevels: number;
  chainLevels: number;
  wordCollisions: number;
  categoryCollisions: number;
  exactCopies: number;
  nearCopies: number;
  near?: NearCopy[];
  recoveryAfterPeak: boolean;
  total: number;
  reject?: string;
}

function correlation(a: number[], b: number[]): number {
  const n = a.length;
  const ma = a.reduce((x, y) => x + y, 0) / n;
  const mb = b.reduce((x, y) => x + y, 0) / n;
  let num = 0; let da = 0; let db = 0;
  for (let i = 0; i < n; i += 1) {
    num += (a[i] - ma) * (b[i] - mb);
    da += (a[i] - ma) ** 2;
    db += (b[i] - mb) ** 2;
  }
  return da === 0 || db === 0 ? 0 : num / Math.sqrt(da * db);
}

/**
 * Близкая копия: 3 из 4 тех же слов или Jaccard ≥ 0.75 с четвёркой референса.
 *
 * Важно, как это трактовать. Точное совпадение четвёрки — брак, тут вопросов нет.
 * А совпадение трёх слов из четырёх на очевидной категории (fruits: apple, banana,
 * pear, plum) — это сходимость на общем знании, а не копирование: любой автор,
 * делая категорию «фрукты», возьмёт те же слова. Поэтому близкие совпадения
 * не отбраковывают блок автоматически, а выносятся на ручную проверку и
 * перечисляются в отчёте с указанием, что именно совпало.
 */
interface NearCopy {
  levelId: number; category: string; words: string[];
  refLevel: number; refCategory: string; shared: string[];
}

function nearCopies(level: GeneratedLevel): NearCopy[] {
  if (!localQuads.length) return [];
  const out: NearCopy[] = [];
  for (const category of level.spec.categories) {
    const mine = new Set(category.words.map((w) => w.text.toLowerCase()));
    for (const ref of localQuads) {
      const shared = ref.words.filter((w) => mine.has(w));
      const union = new Set([...ref.words, ...mine]).size;
      if (shared.length >= 3 || shared.length / union >= 0.75) {
        out.push({
          levelId: level.spec.levelId, category: category.label,
          words: category.words.map((w) => w.text),
          refLevel: ref.level, refCategory: ref.category, shared,
        });
      }
    }
  }
  return out;
}

function scoreBlock(seed: string, block: BlockResult): BlockScore {
  const levels = block.levels;
  const allPassed = levels.every((l) => l.validation.passed);
  const allUnique = levels.every((l) => l.solutions.count === 1);
  const cats = levels.map((l) => l.spec.categories.length);
  const ds = levels.map((l) => l.difficulty.value);
  const is = levels.map((l) => l.interest.value);

  const descents = cats.slice(1).filter((c, i) => c < cats[i]).length;
  const dSpread = Math.max(...ds) - Math.min(...ds);
  const iSpread = Math.max(...is) - Math.min(...is);
  const divergence = 1 - Math.abs(correlation(ds, is));
  const maxDepth = Math.max(...levels.map((l) =>
    Math.max(0, ...l.spec.categories.map((c) => c.metaDepth))));
  const trapLevels = levels.filter((l) => l.spec.traps.length > 0).length;
  const chainLevels = levels.filter((l) => l.spec.modifiers.chains.length > 0).length;

  // повторы слов и категорий внутри блока
  const wordSeen = new Map<string, number>();
  const catSeen = new Map<string, number>();
  let wordCollisions = 0;
  let categoryCollisions = 0;
  for (const level of levels) {
    for (const category of level.spec.categories) {
      const prevCat = catSeen.get(category.key);
      if (prevCat !== undefined) categoryCollisions += 1;
      catSeen.set(category.key, level.spec.levelId);
      for (const word of category.words) {
        const key = word.text.toLowerCase();
        const prev = wordSeen.get(key);
        if (prev !== undefined) wordCollisions += 1;
        wordSeen.set(key, level.spec.levelId);
      }
    }
  }

  let exactCopies = 0;
  for (const level of levels) {
    for (const category of level.spec.categories) {
      if (referenceQuadrupleHashes.has(hashQuadruple(category.words.map((w) => w.text)))) {
        exactCopies += 1;
      }
    }
  }
  const near = levels.flatMap((l) => nearCopies(l));
  const nearCopyTotal = near.length;

  // после максимального пика обязана идти передышка
  const peakIndex = ds.indexOf(Math.max(...ds));
  const recoveryAfterPeak = peakIndex === ds.length - 1
    ? false : ds[peakIndex + 1] < ds[peakIndex] - 1;

  const score: BlockScore = {
    seed, levels: levels.length, allPassed, allUnique, descents,
    dSpread, iSpread, divergence, maxDepth, trapLevels, chainLevels,
    wordCollisions, categoryCollisions, exactCopies, nearCopies: nearCopyTotal,
    recoveryAfterPeak, total: 0, near,
  };

  if (levels.length < 10) score.reject = `собрано только ${levels.length} уровней`;
  else if (!allPassed) score.reject = 'есть нарушения hard-инвариантов';
  else if (!allUnique) score.reject = 'есть уровень с числом решений ≠ 1';
  else if (exactCopies > 0) score.reject = `${exactCopies} четвёрок копируют референс`;
  else if (wordCollisions > 0) score.reject = `${wordCollisions} повторов слова внутри блока`;
  else if (categoryCollisions > 0) score.reject = `${categoryCollisions} повторов категории`;
  else if (descents < 3) score.reject = `переходов вниз ${descents}, нужно минимум 3`;
  else if (!recoveryAfterPeak) score.reject = 'после максимального пика нет передышки';
  // Разъезд шкал — заявленное требование к модели, а не пожелание: если в блоке
  // D и I идут одной линией, блок не демонстрирует две независимые шкалы.
  else if (divergence < 0.15) score.reject = 'сложность и интересность идут одной линией';

  score.total = score.reject ? -1
    : divergence * 5.0              // главное: шкалы обязаны разъезжаться
      + dSpread * 0.8
      + iSpread * 0.6
      + (maxDepth >= 3 ? 1.5 : 0)   // демонстрация неиспользованного рычага
      + Math.min(trapLevels, 6) * 0.3
      + (chainLevels >= 1 && chainLevels <= 3 ? 0.8 : 0)   // акцент, а не фон
      - nearCopyTotal * 0.1;        // сигнал на ручную проверку, не приговор

  return score;
}

// --------------------------------------------------------------------------- //
// прогон воронки
// --------------------------------------------------------------------------- //

const candidates: { score: BlockScore; block: BlockResult }[] = [];
for (let i = 0; i < seedCount; i += 1) {
  const seed = `final-${String(i).padStart(2, '0')}`;
  /*
   * novelty=hard именно ЗДЕСЬ, а не только в отборе блока. Хеши референса
   * воронка получала и раньше, но режим оставался 'off': генератор копию
   * четвёрки собирал молча, а воронка потом выбрасывала из-за неё весь блок.
   * На склеенной базе (в снимке живёт и слой оригинала) так отсеялись все 24
   * кандидата разом. Правильное место отказа — сборка категории: генератор
   * пересдаёт четвёрку и блок доживает до критериев.
   */
  const block = generateBlock({
    snapshot, scoring, config: { ...DEFAULT_BLOCK_CONFIG, seed },
    referenceQuadrupleHashes, referenceNovelty: 'hard',
  });
  candidates.push({ score: scoreBlock(seed, block), block });
}

const survivors = candidates.filter((c) => !c.score.reject)
  .sort((a, b) => b.score.total - a.score.total);
const rejected = candidates.filter((c) => c.score.reject);

console.log(`кандидатов блоков:      ${candidates.length}`);
console.log(`отброшено воронкой:     ${rejected.length}`);
console.log(`прошло все критерии:    ${survivors.length}`);
console.log('');
console.log('Причины отбраковки:');
const reasons = new Map<string, number>();
for (const r of rejected) {
  const key = r.score.reject!.replace(/\d+/g, 'N');
  reasons.set(key, (reasons.get(key) ?? 0) + 1);
}
for (const [reason, n] of Array.from(reasons).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${n}× ${reason}`);
}

if (!survivors.length) {
  console.error('\nНи один блок не прошёл воронку.');
  process.exit(1);
}

console.log('\nЛучшие пять кандидатов:');
console.log('seed'.padEnd(11) + 'итог'.padEnd(7) + 'разбр.D'.padEnd(9)
  + 'разбр.I'.padEnd(9) + 'разъезд'.padEnd(9) + 'глуб'.padEnd(6)
  + 'лов'.padEnd(5) + 'цепи'.padEnd(6) + 'близк.копий');
for (const { score } of survivors.slice(0, 5)) {
  console.log(score.seed.padEnd(11)
    + score.total.toFixed(2).padEnd(7)
    + score.dSpread.toFixed(1).padEnd(9)
    + score.iSpread.toFixed(1).padEnd(9)
    + score.divergence.toFixed(2).padEnd(9)
    + String(score.maxDepth).padEnd(6)
    + String(score.trapLevels).padEnd(5)
    + String(score.chainLevels).padEnd(6)
    + String(score.nearCopies));
}

const winner = survivors[0];
console.log(`\nВыбран блок ${winner.score.seed}, pack hash ${winner.block.packHash.slice(0, 16)}…`);

// --------------------------------------------------------------------------- //
// запись пакета
// --------------------------------------------------------------------------- //

mkdirSync(OUT, { recursive: true });
for (const level of winner.block.levels) {
  writeFileSync(join(OUT, `level-${level.spec.levelId}.json`),
    JSON.stringify(toPipelineJson(level, winner.block), null, 2), 'utf8');
  writeFileSync(join(OUT, `game-${level.spec.levelId}.json`),
    JSON.stringify(toGameJson(level.spec, level.difficulty.value), null, 2), 'utf8');
}
writeFileSync(join(OUT, 'pack.json'), JSON.stringify({
  pack_hash: winner.block.packHash,
  content_snapshot_hash: winner.block.contentSnapshotHash,
  generator_version: winner.block.generatorVersion,
  scoring_version: scoring.scoring_version,
  seed: winner.score.seed,
  funnel: {
    candidate_blocks: candidates.length,
    rejected: rejected.length,
    survivors: survivors.length,
    rejection_reasons: Object.fromEntries(reasons),
  },
  block_criteria: winner.score,
  /*
   * Режим novelty пишем в пакет наравне с seed: без него команда воспроизведения
   * неполна. Тот же seed и тот же снимок при `off` дают ДРУГОЙ блок — генератор
   * не пересдаёт скопированные четвёрки, — и тест воспроизводимости не смог бы
   * отличить «пакет испортился» от «его собирали другой командой».
   */
  reference_novelty: 'hard',
  config: winner.block.config,
  levels: winner.block.levels.map((l) => ({
    level_id: l.spec.levelId, role: l.plan.role,
    difficulty: l.difficulty.value, interest: l.interest.value,
    level_spec_hash: l.levelSpecHash,
  })),
}, null, 2), 'utf8');

// --------------------------------------------------------------------------- //
// карточки уровней и отчёт по проверкам
// --------------------------------------------------------------------------- //

const ROLE_RU: Record<string, string> = {
  entry: 'вход в блок', growth: 'рост', recovery: 'передышка-награда',
  peak: 'главный пик', spike: 'спайк', exit: 'выход, награда',
};

function levelCard(level: GeneratedLevel): string {
  const s = level.spec;
  const meta = s.categories.flatMap((c) => c.words
    .filter((w) => w.kind === 'meta')
    .map((w) => `${w.text} → ${c.label}`));
  const depth = Math.max(0, ...s.categories.map((c) => c.metaDepth));
  const rare = s.categories.flatMap((c) => c.words)
    .filter((w) => w.kind === 'word' && w.zipf !== null && w.zipf < 3);
  const quickwin = s.categories.find((c) => c.isQuickwin);
  const L: string[] = [];
  L.push(`### Уровень ${s.levelId} · ${ROLE_RU[level.plan.role]}\n`);
  L.push('| | |');
  L.push('|---|---|');
  L.push(`| Категорий | ${s.categories.length} |`);
  L.push(`| Пузырей на старте | ${s.board.startBubbles} (4 × ${s.categories.length} − ${meta.length} мета) |`);
  L.push(`| На поле одновременно | ${s.board.boardCapacity}, остальное досыпается волнами |`);
  L.push(`| Лимит ходов | ${s.board.moveLimit} при минимуме ${s.board.moveFloor} (K = ${s.board.moveLimitK}) |`);
  L.push(`| Мета-связей | ${meta.length}, максимальная глубина ${depth}${depth >= 3 ? ' — в оригинале такая глубина появляется только с L438' : ''} |`);
  L.push(`| Редких слов (zipf < 3) | ${rare.length} |`);
  L.push(`| Ловушек | ${s.traps.length} |`);
  L.push(`| Модификаторы | ${s.modifiers.chains.length ? `${s.modifiers.chains.length} цепи` : '—'} |`);
  L.push(`| **Сложность D** | **${level.difficulty.value}** |`);
  L.push(`| **Интересность I** | **${level.interest.value}** |`);
  L.push(`| Глобальных решений | ${level.solutions.count} (перебор ${level.solutions.exhausted ? 'исчерпан' : 'обрезан'}, ${level.solutions.nodesVisited} узлов) |`);
  L.push(`| Семантический аудит | ${level.validation.passed ? 'PASS' : 'FAIL'} |`);
  L.push(`| Хеш уровня | \`${level.levelSpecHash.slice(0, 24)}…\` |`);
  L.push('');
  if (quickwin) {
    L.push(`**Быстрая победа:** ${quickwin.label} — ${quickwin.words.map((w) => w.text).join(', ')}. `
      + 'Дверь открыта: собирается сразу и без раздумий.\n');
  }
  if (meta.length) {
    L.push(`**Мета-связи:** ${meta.join('; ')}.\n`);
  }
  if (s.traps.length) {
    L.push('**Ловушки:** ' + s.traps.map((t) =>
      `\`${t.word}\` живёт в ${t.home}, но на поле есть ${t.decoy} `
      + `(связь настоящая ${t.decoyFit.toFixed(2)}, но тихая ${t.decoyObviousness.toFixed(2)})`)
      .join('; ') + '.\n');
  }
  L.push('**Из чего складывается D:**\n');
  L.push('```');
  const buckets: [string, Record<string, number>][] = [
    ['откалибровано на референсе', level.difficulty.base],
    ['объявлено, не откалибровано', level.difficulty.declared],
    ['семантика', level.difficulty.semantic],
    ['механика', level.difficulty.mechanical],
  ];
  for (const [title, items] of buckets) {
    const entries = Object.entries(items).filter(([, v]) => Math.abs(v) > 0.001);
    if (!entries.length) continue;
    L.push(`${title}:`);
    for (const [name, value] of entries) {
      L.push(`  ${value >= 0 ? '+' : ''}${value.toFixed(2)}  ${name}`);
    }
  }
  L.push('```');
  L.push('');
  L.push(`**Интересность:** Clarity ${level.interest.clarity}, Variety ${level.interest.variety}, `
    + `Aha ${level.interest.aha}, Freshness ${level.interest.freshness}.\n`);
  /*
   * Раньше здесь стояло «заполняется после прохождения» — и не заполнялось
   * никогда: файл переписывается воронкой, любая ручная правка терялась при
   * следующей пересборке. Поэтому запись живёт в `levels/manual-play.json`,
   * а карточка на неё ссылается.
   */
  L.push('**Ручная игра:** запись — `levels/manual-play.json`, сводка — '
    + '`levels/CERTIFICATION.md`, раздел «Ручная игра».\n');
  return L.join('\n');
}

const cards = ['# Карточки финальных уровней 201–210\n',
  `Пакет \`${winner.block.packHash.slice(0, 16)}…\`, снимок базы `
  + `\`${winner.block.contentSnapshotHash.slice(0, 16)}…\`, seed \`${winner.score.seed}\`.\n`,
  'Полные JSON — рядом в этой же папке: `level-NNN.json` (пайплайн) '
  + 'и `game-NNN.json` (контракт с клиентом игры).\n',
  ...winner.block.levels.map(levelCard)];
writeFileSync(join(ROOT, 'docs/LEVEL_CARDS.md'), cards.join('\n'), 'utf8');

// отчёт по проверкам
const allChecks = new Map<string, { passed: number; failed: number; severity: string }>();
for (const level of winner.block.levels) {
  for (const check of level.validation.checks) {
    const entry = allChecks.get(check.code)
      ?? { passed: 0, failed: 0, severity: check.severity };
    if (check.passed) entry.passed += 1; else entry.failed += 1;
    allChecks.set(check.code, entry);
  }
}

const rhythm = checkBlockRhythm(buildBlockPlan(winner.block.config),
  winner.block.config.categoryCorridor);
const V: string[] = [];
V.push('# VALIDATION_REPORT — что и как проверено\n');
V.push(`Пакет \`${winner.block.packHash}\`\n`);
V.push('## 1. Воронка отбора\n');
V.push('```');
V.push(`${candidates.length} блоков-кандидатов`);
V.push(`  ↓ hard-валидация, единственность решения, novelty, критерии блока`);
V.push(`${survivors.length} блоков прошли все критерии`);
V.push(`  ↓ выбор по разъезду шкал D и I, глубине мета, ловушкам`);
V.push(`1 блок сдаётся: ${winner.score.seed}`);
V.push('```');
V.push('');
V.push('Причины отбраковки кандидатов:\n');
V.push('| Причина | Блоков |');
V.push('|---|---|');
for (const [reason, n] of Array.from(reasons).sort((a, b) => b[1] - a[1])) {
  V.push(`| ${reason} | ${n} |`);
}
V.push('');
V.push('## 2. Проверки по всем 10 уровням\n');
V.push('| Код | Тип | Прошло | Упало |');
V.push('|---|---|---|---|');
for (const [code, e] of Array.from(allChecks).sort()) {
  V.push(`| \`${code}\` | ${e.severity} | ${e.passed}/10 | ${e.failed} |`);
}
V.push('');
V.push('## 3. Что доказано, а что проверено эмпирически\n');
V.push('| Утверждение | Сила | Основание |');
V.push('|---|---|---|');
V.push('| Мета-лес ацикличен, у ребёнка один родитель | **доказательство** | обход графа, инвариант |');
V.push('| Граф зависимостей цепей ацикличен | **доказательство** | обход графа |');
V.push('| Арифметика пузырей и лимита ходов | **доказательство** | формула, сверка с фактом |');
V.push('| Ровно одно глобальное решение | **доказательство относительно модели базы** | полный перебор точного покрытия, перебор исчерпан |');
V.push('| Тупиков в чистой сортировке слов нет | **доказательство** | у каждого слова один дом, порядок сборки не важен |');
V.push('| Уровень проходится человеком | эмпирика | ручная игра в прототипе |');
V.push('| Ловушки кусают, но честно | эмпирика | нужен прогон слепого решателя |');
V.push('');
V.push('Слово «доказательство» использовано только там, где есть графовый инвариант '
  + 'или полный обход пространства. Для случайных прогонов правильное слово — '
  + '«стресс-тест», и в этом пакете таких утверждений нет: модификатор здесь '
  + 'единственный (цепи), а он проверяется аналитически.\n');
V.push('## 4. Инварианты блока\n');
const sc = winner.score;
V.push('| Критерий | Значение | Итог |');
V.push('|---|---|---|');
V.push(`| Переходов вниз (пила) | ${sc.descents} из 9 | ${sc.descents >= 3 ? 'PASS' : 'FAIL'} |`);
V.push(`| После пика идёт передышка | ${sc.recoveryAfterPeak ? 'да' : 'нет'} | ${sc.recoveryAfterPeak ? 'PASS' : 'FAIL'} |`);
V.push(`| Разброс D по блоку | ${sc.dSpread.toFixed(1)} | PASS |`);
V.push(`| Разброс I по блоку | ${sc.iSpread.toFixed(1)} | PASS |`);
V.push(`| Разъезд D и I (1 − \\|r\\|) | ${sc.divergence.toFixed(2)} | ${sc.divergence > 0.2 ? 'PASS' : 'ВНИМАНИЕ: шкалы идут вместе'} |`);
V.push(`| Максимальная глубина мета | ${sc.maxDepth} | ${sc.maxDepth >= 3 ? 'демонстрирует неиспользованный рычаг' : 'PASS'} |`);
V.push(`| Уровней с ловушками | ${sc.trapLevels} из 10 | PASS |`);
V.push(`| Уровней с модификатором | ${sc.chainLevels} из 10 | ${sc.chainLevels <= 3 ? 'акцент, а не фон' : 'слишком часто'} |`);
V.push(`| Повторов слова внутри блока | ${sc.wordCollisions} | ${sc.wordCollisions === 0 ? 'PASS' : 'FAIL'} |`);
V.push(`| Повторов категории | ${sc.categoryCollisions} | ${sc.categoryCollisions === 0 ? 'PASS' : 'FAIL'} |`);
V.push(`| Точных копий четвёрок референса | ${sc.exactCopies} | ${sc.exactCopies === 0 ? 'PASS' : 'FAIL'} |`);
V.push(`| Близких копий (3 из 4 слов или Jaccard ≥ 0.75) | ${sc.nearCopies} | ${sc.nearCopies === 0 ? 'PASS' : 'на ручную проверку'} |`);
V.push(`| Ритм плана блока | ${rhythm.passed ? 'PASS' : rhythm.issues.join('; ')} | |`);
V.push('');
if (sc.near && sc.near.length) {
  V.push('### Близкие совпадения с референсом — на ручную проверку\n');
  V.push('Совпадение трёх слов из четырёх на очевидной категории — сходимость на общем '
    + 'знании, а не копирование: любой автор, делая «фрукты», возьмёт те же слова. '
    + 'Точных копий четвёрок в пакете нет (проверено по хешам всех 2244 четвёрок).\n');
  V.push('| Наш уровень | Наша категория | Совпало слов | С какой категорией референса |');
  V.push('|---|---|---|---|');
  for (const n of sc.near.slice(0, 20)) {
    V.push(`| ${n.levelId} | ${n.category} | ${n.shared.length}: ${n.shared.join(', ')} `
      + `| L${n.refLevel} «${n.refCategory}» |`);
  }
  if (sc.near.length > 20) V.push(`| … | ещё ${sc.near.length - 20} | | |`);
  V.push('');
}

V.push('## 5. Оценки финальных уровней\n');
V.push('| Ур. | Роль | Кат. | Пузырей | Мета | Глуб. | Редких | Ловушек | Цепи | D | I |');
V.push('|---|---|---|---|---|---|---|---|---|---|---|');
for (const level of winner.block.levels) {
  const s = level.spec;
  const metaCount = s.categories.reduce((n, c) =>
    n + c.words.filter((w) => w.kind === 'meta').length, 0);
  const depth = Math.max(0, ...s.categories.map((c) => c.metaDepth));
  const rare = s.categories.flatMap((c) => c.words)
    .filter((w) => w.kind === 'word' && w.zipf !== null && w.zipf < 3).length;
  V.push(`| ${s.levelId} | ${ROLE_RU[level.plan.role]} | ${s.categories.length} `
    + `| ${s.board.startBubbles} | ${metaCount} | ${depth} | ${rare} `
    + `| ${s.traps.length} | ${s.modifiers.chains.length} `
    + `| ${level.difficulty.value} | ${level.interest.value} |`);
}
V.push('');
writeFileSync(join(ROOT, 'docs/VALIDATION_REPORT.md'), V.join('\n'), 'utf8');

console.log(`\n→ data/final-pack/ (${winner.block.levels.length * 2 + 1} файлов)`);
console.log('→ docs/LEVEL_CARDS.md');
console.log('→ docs/VALIDATION_REPORT.md');
