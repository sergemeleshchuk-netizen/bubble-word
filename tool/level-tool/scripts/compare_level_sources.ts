/**
 * Один и тот же номер уровня из трёх источников — в один пакет для прототипа.
 *
 *   node scripts/compare_level_sources.ts --level 12 [--seed SEED] [--out FILE]
 *
 * Что кладётся в пакет, по порядку:
 *   1. наша база        — уровень, собранный генератором из `content.snapshot.json`;
 *   2. словарь оригинала — тот же генератор, тот же профиль декады, но контент
 *                          из `reference.snapshot.json`;
 *   3. как в оригинале   — уровень ровно такой, каким он вышел в целевой игре:
 *                          категории и четвёрки взяты из выгрузки без изменений.
 *
 * Зачем третий. Первые два отвечают на вопрос «что генератор делает из разного
 * контента». Третий — на другой, и он важнее: «а как выглядит настоящий уровень
 * с этим номером». Без него сравнивать не с чем, и любое «наш уровень 12
 * похож на оригинальный» остаётся словами.
 *
 * Честная граница третьего уровня. Из выгрузки известны только категории и их
 * четвёрки. Выкладки и лимита ходов оригинал не оставил, поэтому и то и другое
 * посчитано НАШИМИ правилами (`core/deal.ts`, `core/levelMath.ts`) — теми же,
 * что у первых двух. Это сознательно: если бы выкладку третьего уровня считали
 * иначе, разница в наигровке была бы разницей выкладок, а не уровней. Всё, что
 * взято у оригинала без изменений, — состав категорий и слова.
 *
 * Оценки D и I третьему уровню выставляет наша модель на индексе словаря
 * оригинала — включая ловушки, найденные тем же `findTraps`. Это не оценка
 * оригинала «по правде», а ответ на вопрос «что бы наша модель сказала про
 * этот уровень»; расхождение с первыми двумя ровно так и надо читать.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type {
  BlockResult, GeneratedLevel, LevelCategory, LevelSpec, Snapshot, Trap,
} from '../web/src/core/types.ts';
import { CONTENT_SOURCES, type SourceId } from '../web/src/core/sources.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';
import { buildBlockPlan } from '../web/src/core/blockPlan.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import { findTraps, type MetaEdge } from '../web/src/core/generator.ts';
import { buildDeal } from '../web/src/core/deal.ts';
import { BOARD_CAPACITY, moveFloor, moveLimit, startBubbles } from '../web/src/core/levelMath.ts';
import { countSolutions } from '../web/src/core/solutionCounter.ts';
import { computeDifficulty, type ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { computeInterest } from '../web/src/core/scoringInterest.ts';
import { TOOL_VERSION } from '../web/src/core/version.ts';
import type { HandoffLevel, HandoffPack } from '../web/src/core/playableHandoff.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DUMP = resolve(ROOT, '../../reference/bwj-org/levels.jsonl');
const LEVEL_SCHEMA_VERSION = '2.1';

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const levelId = Number(arg('level') ?? 12);
if (!Number.isInteger(levelId) || levelId < 1) {
  throw new Error(`--level ждёт номер уровня, получено «${arg('level')}»`);
}
const seed = arg('seed') ?? `compare-${levelId}`;
const outPath = arg('out')
  ?? resolve(ROOT, `../../site/playable/packs/level${levelId}-three-sources.handoff.json`);

const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

function loadSnapshot(id: SourceId): Snapshot {
  const source = CONTENT_SOURCES.find((s) => s.id === id)!;
  return JSON.parse(readFileSync(join(ROOT, source.snapshotFile), 'utf8')) as Snapshot;
}

/** Декада, в которую попадает номер: профиль берётся по ней, а не по одному уровню. */
const decade: [number, number] = [
  Math.floor((levelId - 1) / 10) * 10 + 1,
  Math.floor((levelId - 1) / 10) * 10 + 10,
];

// --------------------------------------------------------------------------- //
// уровни, собранные генератором
// --------------------------------------------------------------------------- //

interface Built {
  id: string;
  label: string;
  level: GeneratedLevel;
  block: BlockResult;
  snapshot: Snapshot;
}

function generateFrom(id: SourceId, label: string): Built {
  const snapshot = loadSnapshot(id);
  const config = configForRange(decade, seed);
  const block = generateBlock({ snapshot, config, scoring });
  const level = block.levels.find((l) => l.spec.levelId === levelId);
  if (!level) {
    const failure = block.failures.find((f) => f.levelId === levelId);
    throw new Error(`источник ${id}: уровень ${levelId} не собрался — `
      + `${failure?.reason ?? 'причина не записана'}`);
  }
  return { id, label, level, block, snapshot };
}

// --------------------------------------------------------------------------- //
// уровень ровно такой, каким он вышел в оригинале
// --------------------------------------------------------------------------- //

interface DumpCategory {
  name: string;
  words: string[];
  parent: string | null;
  depth: number;
}

function readDumpLevel(): DumpCategory[] {
  let raw: string;
  try {
    raw = readFileSync(DUMP, 'utf8');
  } catch {
    throw new Error(`нет выгрузки ${DUMP}\n`
      + 'Она не хранится в git (правило /reference/ в .gitignore).\n'
      + 'Собрать заново: python3 tool/scripts/scrape_bwj_org.py --from 1 --to 1025');
  }
  for (const line of raw.split('\n')) {
    if (!line.trim()) continue;
    const entry = JSON.parse(line) as { level: number; categories: DumpCategory[] };
    if (entry.level === levelId) return entry.categories;
  }
  throw new Error(`в выгрузке нет уровня ${levelId}`);
}

/**
 * Уровень оригинала в наш `LevelSpec`.
 *
 * Категории и слова берутся из выгрузки как есть. Всё остальное — ключи, тема,
 * частотности, quick-win, выкладка, лимит ходов — считается по нашим правилам,
 * потому что у выгрузки этого нет вовсе. Индексом служит снимок словаря
 * оригинала: он собран из той же выгрузки, значит все слова уровня в нём есть.
 */
function buildOriginalSpec(index: ContentIndex, moveLimitK: number): {
  spec: LevelSpec; traps: Trap[];
} {
  const dump = readDumpLevel();
  const byLabel = new Map<string, number>();
  index.categories.forEach((c, i) => byLabel.set(c.l, i));

  const resolved = dump.map((entry) => {
    const label = entry.name.toUpperCase();
    const catIndex = byLabel.get(label);
    if (catIndex === undefined) {
      throw new Error(`категория «${entry.name}» уровня ${levelId} не найдена в снимке `
        + 'словаря оригинала — снимок собран из другой выгрузки?');
    }
    return { entry, catIndex, meta: index.categories[catIndex] };
  });

  const labelToKey = new Map(resolved.map((r) => [r.entry.name, r.meta.k]));

  const categories: LevelCategory[] = resolved.map(({ entry, catIndex, meta }) => {
    const words = entry.words.map((text) => {
      const wi = index.wordIndex(text);
      // слово-имя ДРУГОЙ категории этого же уровня — мета-пузырь: ровно так его
      // читает и прототип, и так же строит его генератор
      const childKey = text !== entry.name ? labelToKey.get(text) : undefined;
      const membership = wi === undefined ? undefined
        : index.categoryMemberships(catIndex).find((m) => m.word === wi);
      return {
        text,
        kind: (childKey ? 'meta' : 'word') as 'meta' | 'word',
        metaChild: childKey,
        zipf: wi === undefined ? null : index.zipf(wi),
        frequencyUnknown: wi === undefined ? true : index.isFrequencyUnknown(wi),
        relation: membership?.relation,
        fit: membership?.fit,
        obviousness: membership?.obviousness,
      };
    });
    const plain = words.filter((w) => w.kind === 'word');
    return {
      key: meta.k,
      label: meta.l,
      rule: meta.r,
      theme: meta.th,
      words,
      metaDepth: entry.depth,
      parentKey: entry.parent ? labelToKey.get(entry.parent) ?? null : null,
      // тем же правилом, что в генераторе: четыре частотных слова без мета-связей
      isQuickwin: plain.length === words.length
        && plain.every((w) => w.zipf !== null && w.zipf >= index.quickwinThreshold),
    };
  });

  const metaCount = categories.reduce(
    (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0);
  const floor = moveFloor(categories.length);
  const board = {
    categoriesCount: categories.length,
    wordsPerCategory: 4,
    startBubbles: startBubbles(categories.length, metaCount),
    boardCapacity: BOARD_CAPACITY,
    moveFloor: floor,
    moveLimit: moveLimit(floor, moveLimitK),
    moveLimitK,
    moveLimitPolicy: 'conservative' as const,
  };

  const spec: LevelSpec = {
    levelId,
    schemaVersion: LEVEL_SCHEMA_VERSION,
    board,
    categories,
    deal: buildDeal(levelId, categories, board),
    traps: [],
    halves: [],
    modifiers: { chains: [], frozenBubbles: [], hiddenBubbles: [] },
  };

  // ловушки ищем тем же правилом, что генератор: иначе оценка D третьего уровня
  // сравнивалась бы с первыми двумя по разной мерке
  const assignment = new Map<number, number[]>();
  for (const { entry, catIndex } of resolved) {
    const indices = entry.words
      .map((w) => index.wordIndex(w))
      .filter((w): w is number => w !== undefined);
    assignment.set(catIndex, indices);
  }
  // из рёбер `findTraps` читает только слова: мета-пузырь ловушкой не считается,
  // потому что игрок получает его уже собранным
  const keyToIndex = new Map(resolved.map((r) => [r.meta.k, r.catIndex]));
  const edges: MetaEdge[] = categories.flatMap((c) => c.words
    .filter((w) => w.kind === 'meta')
    .map((w) => ({
      child: keyToIndex.get(w.metaChild ?? '') ?? -1,
      parent: keyToIndex.get(c.key) ?? -1,
      word: index.wordIndex(w.text) ?? -1,
    })));
  spec.traps = findTraps(index, assignment, edges);
  return { spec, traps: spec.traps };
}

// --------------------------------------------------------------------------- //
// сборка пакета
// --------------------------------------------------------------------------- //

function handoffLevel(spec: LevelSpec, title: string): HandoffLevel {
  return {
    level_id: spec.levelId,
    title,
    categories: spec.categories.map((c) => ({
      id: c.key, name: c.label, words: c.words.map((w) => w.text),
    })),
    board: {
      board_capacity: spec.board.boardCapacity,
      start_bubbles: spec.board.startBubbles,
      move_limit: spec.board.moveLimit,
      move_limit_k: spec.board.moveLimitK,
    },
    deal: {
      start: spec.deal.start.map((b) => ({ word: b.word, category: b.category })),
      queue: spec.deal.queue.map((b) => ({ word: b.word, category: b.category })),
    },
  };
}

const ours = generateFrom('production', 'наша база');
const theirs = generateFrom('reference', 'словарь оригинала');

// K берётся из плана декады — того же, по которому собраны первые два уровня.
// Свой лимит оригинал в выгрузке не оставил, а выдумывать второе число значило бы
// сделать третий уровень несравнимым по давлению ходов.
const plan = buildBlockPlan(configForRange(decade, seed))
  .find((p) => p.levelId === levelId);
const originalK = plan?.moveLimitK ?? ours.level.spec.board.moveLimitK ?? 1.35;

const referenceIndex = new ContentIndex(theirs.snapshot);
const { spec: originalSpec } = buildOriginalSpec(referenceIndex, originalK);
const originalSolutions = countSolutions(referenceIndex, originalSpec);
const originalDifficulty = computeDifficulty(
  originalSpec, referenceIndex, scoring, originalSolutions);
const originalInterest = computeInterest(
  originalSpec, referenceIndex, scoring, originalSolutions);

function title(source: string, spec: LevelSpec, d: number, i: number): string {
  return `Уровень ${spec.levelId} · ${source} · ${spec.categories.length} кат `
    + `· D ${d} · I ${i}`;
}

const levels: HandoffLevel[] = [
  handoffLevel(ours.level.spec,
    title('наша база', ours.level.spec,
      ours.level.difficulty.value, ours.level.interest.value)),
  handoffLevel(theirs.level.spec,
    title('словарь оригинала', theirs.level.spec,
      theirs.level.difficulty.value, theirs.level.interest.value)),
  handoffLevel(originalSpec,
    title('как в оригинале', originalSpec,
      originalDifficulty.value, originalInterest.value)),
];

const pack: HandoffPack = {
  label: `уровень ${levelId} из трёх источников`,
  tool_version: TOOL_VERSION,
  pack_hash: '',
  content_snapshot_hash: '',
  level_range: [levelId, levelId],
  levels,
};

mkdirSync(dirname(outPath), { recursive: true });
writeFileSync(outPath, `${JSON.stringify(pack)}\n`, 'utf8');

// --------------------------------------------------------------------------- //
// отчёт
// --------------------------------------------------------------------------- //

const rows = [
  {
    source: 'наша база',
    spec: ours.level.spec,
    d: ours.level.difficulty.value,
    i: ours.level.interest.value,
    solutions: ours.level.solutions.count,
    hard: ours.level.validation.issues.filter((x) => x.severity === 'hard').length,
    snapshot: ours.block.contentSnapshotHash,
  },
  {
    source: 'словарь оригинала',
    spec: theirs.level.spec,
    d: theirs.level.difficulty.value,
    i: theirs.level.interest.value,
    solutions: theirs.level.solutions.count,
    hard: theirs.level.validation.issues.filter((x) => x.severity === 'hard').length,
    snapshot: theirs.block.contentSnapshotHash,
  },
  {
    source: 'как в оригинале',
    spec: originalSpec,
    d: originalDifficulty.value,
    i: originalInterest.value,
    solutions: originalSolutions.count,
    hard: -1,
    snapshot: theirs.block.contentSnapshotHash,
  },
];

console.log(`уровень ${levelId}, профиль декады ${decade[0]}-${decade[1]}, seed ${seed}`);
console.log('источник           кат  пуз  мета  лов  реш   лимит   D     I');
for (const r of rows) {
  const meta = r.spec.categories.reduce(
    (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0);
  console.log(
    `${r.source.padEnd(18)} ${String(r.spec.categories.length).padStart(3)} `
    + `${String(r.spec.board.startBubbles).padStart(4)} ${String(meta).padStart(5)} `
    + `${String(r.spec.traps.length).padStart(4)} ${String(r.solutions).padStart(4)} `
    + `${String(r.spec.board.moveLimit).padStart(7)} `
    + `${String(r.d).padStart(5)} ${String(r.i).padStart(5)}`);
}
for (const r of rows) {
  console.log(`${r.source}: ${r.spec.categories.map((c) => c.label).join(', ')}`);
}
console.log(`\n${outPath}`);
console.log('добавьте имя файла первым в site/playable/packs/index.json');
