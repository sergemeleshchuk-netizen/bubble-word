/**
 * Уровень из ЗАПИСИ оригинала — в играбельный прототип, кусочек в кусочек.
 *
 *   node scripts/video_level_to_handoff.ts --level 12 [--out FILE]
 *
 * Источник — покадровый разбор четырёх записей геймплея,
 * `tool/word_content_pipeline/data/reference/video-levels-20.json`. Он знает то,
 * чего нет в текстовой выгрузке ответов: лимит ходов, число пузырей на старте,
 * модификаторы и — главное — какие слова приходят КУСОЧКАМИ и по какому месту
 * они распилены (`dol|phin`, `choco|late`, `au|gust`).
 *
 * Чем это отличается от `compare_level_sources.ts --level 12`. Тот берёт уровень
 * из текстовой выгрузки: категории и четвёрки верные, но кусочков там нет вовсе,
 * а лимит ходов приходится считать нашей формулой. Здесь и кусочки, и лимит —
 * из записи: 8 распилов, 60 ходов при минимуме 44 (K = 1.36).
 *
 * Что всё-таки считаем мы, а не запись. СОСТАВ старта: разбор фиксирует, что на
 * старте 24 пузыря, но не перечисляет, какие именно. Поэтому выкладка считается
 * общим правилом проекта (`core/deal.ts`) — тем же, что у всех наших уровней, —
 * с одной поправкой: распиленное слово занимает на поле ДВА места, иначе восемь
 * распилов дали бы 32 пузыря вместо записанных 24. Так уровень сходится с
 * записью по числу пузырей, по лимиту и по содержимому, а расходится только там,
 * где запись молчит. Врать про «покадровое совпадение старта» нельзя.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { LevelCategory } from '../web/src/core/types.ts';
import { buildDeal, chunkKey } from '../web/src/core/deal.ts';
import { BOARD_CAPACITY } from '../web/src/core/levelMath.ts';
import type { HandoffLevel, HandoffPack } from '../web/src/core/playableHandoff.ts';
import { TOOL_VERSION } from '../web/src/core/version.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DATASET = resolve(ROOT,
  '../word_content_pipeline/data/reference/video-levels-20.json');

interface VideoCategory { name: string; words: string[]; forms?: Record<string, string> }
interface VideoLevel {
  level: number;
  board: { move_limit: number; min_moves: number; K_observed: number;
    bubbles_on_start: number };
  modifiers: string[];
  chunked_words: { word: string; pieces: string[] }[];
  categories: VideoCategory[];
  traps?: string[];
  notes?: string;
}

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const levelId = Number(arg('level') ?? 12);
const outPath = arg('out')
  ?? resolve(ROOT, `../../site/playable/packs/level${levelId}-as-recorded.handoff.json`);

const dataset = JSON.parse(readFileSync(DATASET, 'utf8')) as { levels: VideoLevel[] };
const video = dataset.levels.find((l) => l.level === levelId);
if (!video) {
  throw new Error(`в разборе записей нет уровня ${levelId} `
    + `(есть ${dataset.levels.map((l) => l.level).join(', ')})`);
}

const key = (name: string) => name.trim().toLowerCase().replace(/[^a-z0-9]+/g, '_');
const byName = new Map(video.categories.map((c) => [c.name, key(c.name)]));

/**
 * Категории уровня. Мета-пузырь распознаётся так же, как везде в проекте:
 * слово, равное имени ДРУГОЙ категории этого уровня.
 */
const categories: LevelCategory[] = video.categories.map((c) => ({
  key: key(c.name),
  label: c.name.toUpperCase(),
  rule: `Из записи оригинала, уровень ${levelId}`,
  theme: 'reference',
  words: c.words.map((text) => {
    const child = text !== c.name ? byName.get(text) : undefined;
    return {
      text,
      kind: (child ? 'meta' : 'word') as 'meta' | 'word',
      metaChild: child,
      zipf: null,
      frequencyUnknown: false,
    };
  }),
  metaDepth: 0,
  parentKey: null,
  /**
   * Категория «открытой двери» — та, что выкладывается на старт целиком.
   * Берём четвёрку без единого распила: показывать игроку кучу обрывков в
   * качестве обучающей четвёрки бессмысленно.
   */
  isQuickwin: c.words.every((w) => !video.chunked_words.some((ch) => ch.word === w)),
}));

// распилы: ключ «категория::слово», как их понимает выкладка
const chunkedSet = new Set<string>();
const chunkList: NonNullable<HandoffLevel['chunks']> = [];
for (const chunk of video.chunked_words) {
  const home = video.categories.find((c) => c.words.includes(chunk.word));
  if (!home) {
    throw new Error(`распил «${chunk.word}» не нашёл своей категории на уровне ${levelId}`);
  }
  if (chunk.pieces.length !== 2) {
    throw new Error(`распил «${chunk.word}» не на две части: ${chunk.pieces.join('|')}`);
  }
  if (chunk.pieces.join('') !== chunk.word) {
    throw new Error(`куски «${chunk.pieces.join('|')}» не складываются в «${chunk.word}»`);
  }
  const categoryKey = key(home.name);
  chunkedSet.add(chunkKey(categoryKey, chunk.word));
  chunkList.push({
    word: chunk.word,
    category: categoryKey,
    pieces: [chunk.pieces[0], chunk.pieces[1]],
  });
}

const spawnable = categories.flatMap((c) => c.words.filter((w) => w.kind !== 'meta'));
const deal = buildDeal(levelId, categories,
  { boardCapacity: BOARD_CAPACITY, wordsPerCategory: 4 }, chunkedSet);

const bubblesOnStart = deal.start.reduce(
  (n, b) => n + (chunkedSet.has(chunkKey(b.category, b.word)) ? 2 : 1), 0);

const level: HandoffLevel = {
  level_id: levelId,
  title: `Уровень ${levelId} · как в записи · ${categories.length} кат `
    + `· ${chunkList.length} слов кусочками · ${video.board.move_limit} ходов`,
  categories: categories.map((c) => ({
    id: c.key, name: c.label, words: c.words.map((w) => w.text),
  })),
  board: {
    board_capacity: BOARD_CAPACITY,
    start_bubbles: spawnable.length,
    // лимит из записи, а не из формулы: запись — источник правды о том,
    // сколько ходов игроку реально дали
    move_limit: video.board.move_limit,
    move_limit_k: video.board.K_observed,
  },
  deal: {
    start: deal.start.map((b) => ({ word: b.word, category: b.category })),
    queue: deal.queue.map((b) => ({ word: b.word, category: b.category })),
  },
  chunks: chunkList,
};

const pack: HandoffPack = {
  label: `уровень ${levelId} оригинала, как в записи (с кусочками)`,
  tool_version: TOOL_VERSION,
  pack_hash: '',
  content_snapshot_hash: '',
  level_range: [levelId, levelId],
  levels: [level],
};

mkdirSync(dirname(outPath), { recursive: true });
writeFileSync(outPath, `${JSON.stringify(pack)}\n`, 'utf8');

// --------------------------------------------------------------------------- //
// сверка с записью: расхождение печатаем, а не прячем
// --------------------------------------------------------------------------- //
const metaCount = categories.reduce(
  (n, c) => n + c.words.filter((w) => w.kind === 'meta').length, 0);
const minMoves = categories.length * 3 + chunkList.length;

console.log(`уровень ${levelId} из записи`);
console.log(`  категорий        ${categories.length} (в записи ${video.categories.length})`);
console.log(`  слов             ${categories.length * 4}, мета ${metaCount}, `
  + `спавнится ${spawnable.length}`);
console.log(`  распилов         ${chunkList.length}: `
  + chunkList.map((c) => `${c.pieces[0]}|${c.pieces[1]}`).join(' '));
console.log(`  минимум ходов    ${minMoves} (в записи ${video.board.min_moves})`);
console.log(`  лимит ходов      ${video.board.move_limit} (K ${video.board.K_observed})`);
console.log(`  пузырей на старте ${bubblesOnStart} (в записи ${video.board.bubbles_on_start})`);
console.log(`  в очереди        ${deal.queue.reduce(
  (n, b) => n + (chunkedSet.has(chunkKey(b.category, b.word)) ? 2 : 1), 0)} пузырей`);
if (minMoves !== video.board.min_moves) {
  console.log(`  ! минимум ходов разошёлся с записью — проверьте разбор`);
}
if (bubblesOnStart !== video.board.bubbles_on_start) {
  console.log(`  ! пузырей на старте разошлось с записью`);
}
console.log(`\n${outPath}`);
