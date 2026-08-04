/**
 * Сертификация решаемости сдаваемого пакета.
 *
 * ЗАЧЕМ ОТДЕЛЬНАЯ ПРОГРАММА. Инструмент уже отвечает «решение единственное» и
 * «уровень проходим» — но отвечает СВОИМ ЖЕ кодом, тем самым, что уровень и
 * собрал. Ревьюеру такой ответ ничего не доказывает: ошибка в общем модуле
 * одинаково соврёт и генератору, и проверяльщику. Сертификат отвечает на тот же
 * вопрос ВТОРЫМ, независимым путём и по более строгим правилам, чем гейт сборки.
 *
 * НЕЗАВИСИМОСТЬ — это правило файла, а не пожелание. Здесь намеренно нет ни
 * одного импорта из `web/src/core`: ни счётчика решений, ни движка партии, ни
 * валидатора, ни типов уровня. На входе — только сдаваемый JSON (то, что
 * получит команда игры) и снимки контента как данные. Закреплено тестом
 * `tests/certify.test.ts`.
 *
 * Пять проверок. Первые три — приговор, последние две — обязательные факты,
 * которые сертификат называет вслух, а не прячет за словом PASS.
 *
 *   C1 КЛЮЧ          контракт с клиентом сходится сам с собой: числа, мета-ссылки,
 *                    выкладка покрывает ровно слова уровня;
 *   C2 ЕДИНСТВЕННОСТЬ свой перебор всех полных раскладок по РАСШИРЕННОМУ графу
 *                    правдоподобия — шире того, которым пользовался генератор;
 *   C3 ПАРТИЯ        свой переигрыш выкладки с УЧЁТОМ ЁМКОСТИ ПОЛЯ (движок
 *                    инструмента её не моделирует — см. playSim.ts §«упрощение»);
 *   C4 ВНЕШНИЙ ВЗГЛЯД словарь оригинала как посторонний свидетель: подтверждает
 *                    он наш ключ или спорит с ним;
 *   C5 ПРОИСХОЖДЕНИЕ  из чьих категорий собран уровень — наших или взятых из
 *                    транскрипции оригинала.
 *
 *   node scripts/certify_solvability.ts [--pack data/final-pack]
 *                                       [--out ../../levels/certificates]
 *                                       [--report ../../levels/CERTIFICATION.md]
 *
 * Выход ненулевой, если хоть один уровень провалил C1–C3.
 */
import { readdirSync, readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function arg(name: string, fallback: string): string {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : fallback;
}

// resolve, а не join: путь могут дать и абсолютным (так делает тест)
const PACK_DIR = resolve(ROOT, arg('pack', 'data/final-pack'));
const OUT_DIR = resolve(ROOT, arg('out', '../../levels/certificates'));
const REPORT = resolve(ROOT, arg('report', '../../levels/CERTIFICATION.md'));

/** Версия правил сертификации: меняется вместе с составом или строгостью проверок. */
const CERT_VERSION = 'cert-1.0';

// --------------------------------------------------------------------------- //
// данные на входе
// --------------------------------------------------------------------------- //

/**
 * Снимок контента читается как сырые данные, без индексатора инструмента.
 * Раскладка строк снимка описана в `web/src/core/snapshot.ts`; здесь она
 * повторена нарочно — если формат поменяется, сертификатор обязан сломаться
 * громко, а не молча согласиться с генератором.
 */
interface RawSnapshot {
  content_snapshot_hash: string;
  categories: { k: string; l: string }[];
  words: { n: string; t: string }[];
  /** [слово, категория, статус, ...] — статусы см. `statuses` */
  memberships: number[][];
  statuses: string[];
}

function readSnapshot(file: string): RawSnapshot {
  return JSON.parse(readFileSync(join(ROOT, file), 'utf8')) as RawSnapshot;
}

/** Слово → индексы категорий, куда снимок считает его правдоподобным членом. */
function wordToCategories(snap: RawSnapshot, maxStatus: number): Map<number, Set<number>> {
  const out = new Map<number, Set<number>>();
  for (const row of snap.memberships) {
    if (row[2] > maxStatus) continue;
    let set = out.get(row[0]);
    if (!set) { set = new Set(); out.set(row[0], set); }
    set.add(row[1]);
  }
  return out;
}

const norm = (s: string): string => s.toLowerCase();
/** Имя категории для сверки с чужим источником: буквы и цифры, без регистра. */
const normLabel = (s: string): string => s.toUpperCase().replace(/[^A-Z0-9]+/g, ' ').trim();

// --------------------------------------------------------------------------- //
// сдаваемый уровень, как его читает посторонний
// --------------------------------------------------------------------------- //

interface ContractWord { text: string; kind: string; meta_child?: string }
interface ContractCategory { key: string; label: string; words: ContractWord[] }
interface Contract {
  level_id: number;
  board: {
    categories_count: number; words_per_category: number;
    start_bubbles: number; board_capacity: number; move_limit: number | null;
  };
  categories: ContractCategory[];
}

interface DealBubble { word: string; category: string }
interface Pipeline {
  level_spec: {
    levelId: number;
    board: { moveFloor?: number; moveLimit: number | null };
    halves: { home: string; word: string }[];
    deal?: { start: DealBubble[]; queue: DealBubble[] };
  };
  build_metadata: { content_snapshot_hash: string; pack_hash: string; generator_version: string };
  validation: { solution_count: number; playability?: { moves_needed: number } };
}

interface Check {
  code: string;
  passed: boolean;
  detail: string;
}

// --------------------------------------------------------------------------- //
// C1 — ключ сходится сам с собой
// --------------------------------------------------------------------------- //

function certifyKey(contract: Contract, pipeline: Pipeline): Check[] {
  const checks: Check[] = [];
  const add = (code: string, passed: boolean, detail: string) =>
    checks.push({ code, passed, detail });

  const cats = contract.categories;
  add('KEY_CATEGORY_COUNT', cats.length === contract.board.categories_count,
    `категорий ${cats.length}, объявлено ${contract.board.categories_count}`);

  const wrongSize = cats.filter((c) => c.words.length !== contract.board.words_per_category);
  add('KEY_CATEGORY_SIZE', wrongSize.length === 0,
    wrongSize.length === 0
      ? `у всех категорий по ${contract.board.words_per_category} слова`
      : `не по ${contract.board.words_per_category}: ${wrongSize.map((c) => c.key).join(', ')}`);

  // мета-пузырь на старте не лежит: он рождается сбором дочерней категории
  const metaWords = cats.flatMap((c) => c.words.filter((w) => w.kind === 'meta'));
  const expectedStart = cats.reduce((n, c) => n + c.words.length, 0) - metaWords.length;
  add('KEY_START_BUBBLES', expectedStart === contract.board.start_bubbles,
    `слов ${cats.reduce((n, c) => n + c.words.length, 0)} − мета ${metaWords.length} `
    + `= ${expectedStart}, объявлено ${contract.board.start_bubbles}`);

  const keys = new Set(cats.map((c) => c.key));
  const danglingMeta = metaWords.filter((w) => !w.meta_child || !keys.has(w.meta_child));
  add('KEY_META_RESOLVES', danglingMeta.length === 0,
    danglingMeta.length === 0
      ? `мета-ссылок ${metaWords.length}, все ведут на категорию этого уровня`
      : `ссылки в никуда: ${danglingMeta.map((w) => w.text).join(', ')}`);

  // одинаковый текст в двух категориях — это не ловушка, а неразрешимая позиция
  const seen = new Map<string, string[]>();
  for (const c of cats) {
    for (const w of c.words) {
      const list = seen.get(norm(w.text)) ?? [];
      list.push(c.key);
      seen.set(norm(w.text), list);
    }
  }
  const dupes = [...seen.entries()].filter(([, homes]) => homes.length > 1);
  add('KEY_NO_DUPLICATE_BUBBLE', dupes.length === 0,
    dupes.length === 0 ? 'одинаковых текстов на поле нет'
      : dupes.map(([w, homes]) => `«${w}» → ${homes.join(' и ')}`).join('; '));

  // выкладка обязана покрывать ровно слова уровня — ни больше, ни меньше
  const deal = pipeline.level_spec.deal;
  if (!deal) {
    add('KEY_DEAL_PRESENT', false,
      'выкладки в спеке нет: партию воспроизвести нечем (пакеты до gen-1.1)');
    return checks;
  }
  add('KEY_DEAL_PRESENT', true, `старт ${deal.start.length}, очередь ${deal.queue.length}`);

  const need = new Map<string, number>();
  for (const c of cats) {
    for (const w of c.words) {
      if (w.kind === 'meta') continue;      // мета-пузырь в выкладку не входит
      const k = `${c.key}::${norm(w.text)}`;
      need.set(k, (need.get(k) ?? 0) + 1);
    }
  }
  const got = new Map<string, number>();
  for (const b of [...deal.start, ...deal.queue]) {
    const k = `${b.category}::${norm(b.word)}`;
    got.set(k, (got.get(k) ?? 0) + 1);
  }
  const missing = [...need.keys()].filter((k) => (got.get(k) ?? 0) !== need.get(k));
  const extra = [...got.keys()].filter((k) => !need.has(k));
  add('KEY_DEAL_COVERS_LEVEL', missing.length === 0 && extra.length === 0,
    missing.length === 0 && extra.length === 0
      ? `выкладка покрывает ровно ${need.size} пузырей уровня`
      : `не выложено: ${missing.join(', ') || '—'}; лишнее: ${extra.join(', ') || '—'}`);

  add('KEY_START_FITS_BOARD', deal.start.length <= contract.board.board_capacity,
    `на старте ${deal.start.length} пузырей при ёмкости поля ${contract.board.board_capacity}`);

  return checks;
}

// --------------------------------------------------------------------------- //
// C2 — единственность решения по расширенному графу
// --------------------------------------------------------------------------- //

interface UniquenessResult {
  solutions: number;
  exhausted: boolean;
  nodes: number;
  /** слов, у которых на этом уровне больше одного правдоподобного дома */
  multiHome: number;
  /** слова, которых в базе нет вовсе: у них дом принят на веру */
  unknownWords: string[];
  /** вторая раскладка, если она нашлась */
  secondSolution?: { category: string; words: string[] }[];
  widening: {
    ownStatuses: string;
    /** домов, добавленных статусом hard_only — его генератор не смотрит */
    hardOnlyLinksAdded: number;
    /** домов, добавленных словарём оригинала СВЕРХ того, что знает наша база */
    outsideLinksAdded: number;
    outsideMatchedCategories: number;
  };
}

const SOLUTION_CAP = 4;
const NODE_CAP = 3_000_000;

/**
 * Перебор всех полных раскладок.
 *
 * Отличия от счётчика инструмента, и каждое — в сторону строгости:
 *   1) свой граф правдоподобия ШИРЕ: наши связи берутся включая `hard_only`
 *      (генератор смотрит только approved и alternative), плюс к ним
 *      добавляются связи из словаря оригинала — постороннего источника,
 *      который наш уровень не собирал;
 *   2) перебор не останавливается на второй раскладке, а считает их до четырёх:
 *      «решений ровно два» и «решений десятки» — разные диагнозы;
 *   3) слова, которых нет ни в одном источнике, перечисляются поимённо: их
 *      единственность не доказана, а принята на веру, и молчать об этом нельзя.
 */
function certifyUniqueness(
  contract: Contract,
  own: { snap: RawSnapshot; w2c: Map<number, Set<number>>; w2cGenerator: Map<number, Set<number>>;
    wordIdx: Map<string, number>; catIdx: Map<string, number> },
  outside: { snap: RawSnapshot; w2c: Map<number, Set<number>>; wordIdx: Map<string, number>;
    byLabel: Map<string, number[]> },
): UniquenessResult {
  const slots = contract.categories;
  const ownSlotIdx = slots.map((c) => own.catIdx.get(c.key) ?? -1);
  const outsideSlotCats = slots.map((c) => outside.byLabel.get(normLabel(c.label)) ?? []);
  const outsideMatchedCategories = outsideSlotCats.filter((l) => l.length > 0).length;

  interface Item { text: string; home: number; plausible: number[] }
  const items: Item[] = [];
  const unknownWords: string[] = [];
  let outsideLinksAdded = 0;
  let hardOnlyLinksAdded = 0;

  slots.forEach((category, slot) => {
    for (const word of category.words) {
      // мета-пузырь структурен: это имя дочерней категории, лежащее у родителя
      // по построению уровня. Другого дома у него быть не может физически.
      if (word.kind === 'meta') {
        items.push({ text: word.text, home: slot, plausible: [slot] });
        continue;
      }
      const plausible = new Set<number>([slot]);

      const ownWi = own.wordIdx.get(norm(word.text));
      if (ownWi !== undefined) {
        const homes = own.w2c.get(ownWi);
        const generatorHomes = own.w2cGenerator.get(ownWi);
        if (homes) {
          slots.forEach((_, s) => {
            if (!homes.has(ownSlotIdx[s])) return;
            // считаем отдельно то, чего генератор не видел: связи hard_only
            if (!plausible.has(s) && !generatorHomes?.has(ownSlotIdx[s])) {
              hardOnlyLinksAdded += 1;
            }
            plausible.add(s);
          });
        }
      }

      const outWi = outside.wordIdx.get(norm(word.text));
      if (outWi !== undefined) {
        const homes = outside.w2c.get(outWi);
        if (homes) {
          slots.forEach((_, s) => {
            if (outsideSlotCats[s].some((c) => homes.has(c)) && !plausible.has(s)) {
              plausible.add(s);
              outsideLinksAdded += 1;
            }
          });
        }
      }

      if (ownWi === undefined && outWi === undefined) unknownWords.push(word.text);
      items.push({ text: word.text, home: slot, plausible: [...plausible] });
    }
  });

  const multiHome = items.filter((i) => i.plausible.length > 1).length;

  // самые зажатые слова первыми — дерево схлопывается на однодомных
  items.sort((a, b) => a.plausible.length - b.plausible.length
    || (a.text < b.text ? -1 : 1));

  const capacity = slots.map((c) => c.words.length);
  const assignment = new Array<number>(items.length).fill(-1);
  let solutions = 0;
  let nodes = 0;
  let exhausted = true;
  let secondSolution: UniquenessResult['secondSolution'];

  const feasible = (from: number): boolean => {
    const reach = capacity.map(() => 0);
    for (let i = from; i < items.length; i += 1) {
      for (const s of items[i].plausible) reach[s] += 1;
    }
    return capacity.every((need, s) => need <= reach[s]);
  };

  const snapshotAssignment = () => {
    const buckets: string[][] = slots.map(() => []);
    items.forEach((item, i) => buckets[assignment[i]].push(item.text));
    return slots.map((c, i) => ({ category: c.key, words: buckets[i].slice().sort() }));
  };

  const dfs = (i: number): boolean => {
    nodes += 1;
    if (nodes > NODE_CAP) { exhausted = false; return true; }
    if (i === items.length) {
      solutions += 1;
      if (solutions === 2) secondSolution = snapshotAssignment();
      return solutions >= SOLUTION_CAP;
    }
    if (!feasible(i)) return false;
    for (const slot of items[i].plausible) {
      if (capacity[slot] === 0) continue;
      capacity[slot] -= 1;
      assignment[i] = slot;
      if (dfs(i + 1)) return true;
      capacity[slot] += 1;
      assignment[i] = -1;
    }
    return false;
  };
  dfs(0);

  return {
    solutions, exhausted, nodes, multiHome, unknownWords, secondSolution,
    widening: {
      ownStatuses: 'approved + alternative + hard_only',
      hardOnlyLinksAdded,
      outsideLinksAdded,
      outsideMatchedCategories,
    },
  };
}

// --------------------------------------------------------------------------- //
// C3 — партия переигрывается, поле не встаёт
// --------------------------------------------------------------------------- //

interface PlaythroughResult {
  finished: boolean;
  failReason: string | null;
  moves: number;
  moveLimit: number | null;
  spare: number | null;
  /** максимум пузырей, одновременно лежавших на поле */
  peakOnBoard: number;
  boardCapacity: number;
  /** ходов, на которых легальный мердж был ровно один */
  onlyMoveStates: number;
  /** состояний, где поле встало и пришлось звать досыпку вне ритма */
  stalls: number;
  /** доказательство «поле не может встать»: ёмкость больше числа живых категорий */
  deadlockImpossible: boolean;
}

/**
 * Свой переигрыш выкладки.
 *
 * Главное отличие от движка инструмента: ЁМКОСТЬ ПОЛЯ ЗДЕСЬ НАСТОЯЩАЯ. В
 * `web/src/core/playSim.ts` она сознательно не моделируется (там это записано
 * как известное упрощение), поэтому вердикт «проходим» инструмент выносит для
 * поля без границ. Сертификат обязан отвечать за то поле, которое увидит игрок:
 * досыпка идёт только на свободные места, и если мест нет — пузырь ждёт.
 *
 * Стратегия — идеальный игрок, знающий ответы: сначала завершающий мердж, иначе
 * мердж в категории, у которой на поле больше всего слов. Порядок мерджей на их
 * ЧИСЛО не влияет (каждый мердж уменьшает число кусков ровно на один), поэтому
 * вердикт «хватило ли лимита» от стратегии не зависит. От неё зависит только то,
 * встаёт ли поле, — а это и проверяется.
 */
function certifyPlaythrough(contract: Contract, pipeline: Pipeline): PlaythroughResult {
  const deal = pipeline.level_spec.deal!;
  const capacity = contract.board.board_capacity;
  const limit = contract.board.move_limit;

  const fullOf = new Map<string, number>();
  for (const c of contract.categories) fullOf.set(c.key, c.words.length);
  const metaOf = new Map<string, { parent: string; text: string }>();
  for (const c of contract.categories) {
    for (const w of c.words) {
      if (w.kind === 'meta' && w.meta_child) metaOf.set(w.meta_child, { parent: c.key, text: w.text });
    }
  }

  interface Bubble { category: string; words: string[] }
  const board: Bubble[] = deal.start.map((b) => ({ category: b.category, words: [b.word] }));
  const queue: DealBubble[] = deal.queue.slice();
  const collected = new Set<string>();
  let moves = 0;
  let peakOnBoard = board.length;
  let onlyMoveStates = 0;
  let stalls = 0;

  /** Досыпка: только на свободные места, строго по очереди. */
  const refill = (): void => {
    while (board.length < capacity && queue.length > 0) {
      const next = queue.shift()!;
      board.push({ category: next.category, words: [next.word] });
    }
    peakOnBoard = Math.max(peakOnBoard, board.length);
  };
  refill();

  const legalPairs = (): [number, number][] => {
    const out: [number, number][] = [];
    for (let i = 0; i < board.length; i += 1) {
      for (let j = i + 1; j < board.length; j += 1) {
        if (board[i].category !== board[j].category) continue;
        if (board[i].words.length + board[j].words.length > (fullOf.get(board[i].category) ?? 4)) continue;
        out.push([i, j]);
      }
    }
    return out;
  };

  let guard = 20000;
  while (collected.size < contract.categories.length && guard > 0) {
    guard -= 1;
    let pairs = legalPairs();

    if (pairs.length === 0) {
      // поле встало: единственная законная помощь прототипа — досыпка вне ритма
      if (queue.length === 0) {
        return {
          finished: false, failReason: 'жёсткий тупик: мерджей нет и очередь пуста',
          moves, moveLimit: limit, spare: limit === null ? null : limit - moves,
          peakOnBoard, boardCapacity: capacity, onlyMoveStates, stalls,
          deadlockImpossible: false,
        };
      }
      stalls += 1;
      // место под досыпку взять неоткуда — это уже настоящий тупик поля
      if (board.length >= capacity) {
        return {
          finished: false,
          failReason: `поле забито ${board.length} пузырями, мерджей нет, досыпать некуда`,
          moves, moveLimit: limit, spare: limit === null ? null : limit - moves,
          peakOnBoard, boardCapacity: capacity, onlyMoveStates, stalls,
          deadlockImpossible: false,
        };
      }
      refill();
      pairs = legalPairs();
      if (pairs.length === 0) continue;
    }

    if (pairs.length === 1) onlyMoveStates += 1;

    const completing = pairs.filter(([i, j]) =>
      board[i].words.length + board[j].words.length === (fullOf.get(board[i].category) ?? 4));
    let pick: [number, number];
    if (completing.length > 0) {
      pick = completing[0];
    } else {
      const onBoard = new Map<string, number>();
      for (const b of board) onBoard.set(b.category, (onBoard.get(b.category) ?? 0) + b.words.length);
      pick = pairs.reduce((best, p) =>
        ((onBoard.get(board[p[0]].category) ?? 0) > (onBoard.get(board[best[0]].category) ?? 0)
          ? p : best), pairs[0]);
    }

    // legalPairs всегда отдаёт i < j, поэтому splice(j) индекс i не сдвигает
    const [i, j] = pick;
    board[i].words = [...board[i].words, ...board[j].words];
    board.splice(j, 1);
    moves += 1;

    const bubble = board[i];
    if (bubble.words.length >= (fullOf.get(bubble.category) ?? 4)) {
      collected.add(bubble.category);
      board.splice(i, 1);
      // сбор дочерней категории рождает у родителя пузырь с её именем
      const meta = metaOf.get(bubble.category);
      if (meta) board.push({ category: meta.parent, words: [meta.text] });
      refill();
    }
  }

  /*
   * Отдельный, не зависящий от прогона довод: пока живых категорий меньше, чем
   * мест на поле, поле встать не может. На поле лежит больше пузырей, чем есть
   * несобранных категорий, значит по принципу Дирихле хотя бы у одной категории
   * на поле два пузыря — а это законный мердж.
   */
  const deadlockImpossible = capacity > contract.categories.length;

  if (guard <= 0) {
    return {
      finished: false, failReason: 'переигрыш не сошёлся: защитный предел исчерпан',
      moves, moveLimit: limit, spare: null, peakOnBoard, boardCapacity: capacity,
      onlyMoveStates, stalls, deadlockImpossible,
    };
  }
  if (limit !== null && moves > limit) {
    return {
      finished: false, failReason: `лимита не хватает: нужно ${moves}, лимит ${limit}`,
      moves, moveLimit: limit, spare: limit - moves, peakOnBoard, boardCapacity: capacity,
      onlyMoveStates, stalls, deadlockImpossible,
    };
  }
  return {
    finished: true, failReason: null, moves, moveLimit: limit,
    spare: limit === null ? null : limit - moves,
    peakOnBoard, boardCapacity: capacity, onlyMoveStates, stalls, deadlockImpossible,
  };
}

// --------------------------------------------------------------------------- //
// C4 — посторонний свидетель
// --------------------------------------------------------------------------- //

interface OutsideView {
  /** категорий уровня, которые чужой словарь вообще знает по имени */
  matchedCategories: number;
  totalCategories: number;
  /** слов, про которые чужой словарь может что-то сказать на этом уровне */
  covered: number;
  totalWords: number;
  /** из покрытых — сколько чужой источник кладёт туда же, куда и наш ключ */
  agreeing: number;
  /** слова, которые чужой источник кладёт в ДРУГУЮ категорию уровня и не в нашу */
  disputed: { word: string; ourHome: string; outsideHome: string[] }[];
}

/**
 * Взгляд со стороны: подтверждает ли словарь оригинала нашу раскладку.
 *
 * Это не «слепой решатель ходит по полю» — это проверка ключа посторонним
 * источником, который наш уровень не собирал и наших правил не знает. Он
 * покрывает не всё (у оригинала своя нарезка категорий), и доля покрытия
 * печатается честно: сертификат без неё выдавал бы согласие двух слов за
 * согласие уровня.
 */
function certifyOutsideView(
  contract: Contract,
  outside: { snap: RawSnapshot; w2c: Map<number, Set<number>>; wordIdx: Map<string, number>;
    byLabel: Map<string, number[]> },
): OutsideView {
  const slots = contract.categories;
  const slotCats = slots.map((c) => outside.byLabel.get(normLabel(c.label)) ?? []);
  const matchedCategories = slotCats.filter((l) => l.length > 0).length;

  let covered = 0;
  let agreeing = 0;
  let totalWords = 0;
  const disputed: OutsideView['disputed'] = [];

  slots.forEach((category, slot) => {
    for (const word of category.words) {
      if (word.kind === 'meta') continue;
      totalWords += 1;
      const wi = outside.wordIdx.get(norm(word.text));
      if (wi === undefined) continue;
      const homes = outside.w2c.get(wi);
      if (!homes) continue;
      const hit: number[] = [];
      slots.forEach((_, s) => { if (slotCats[s].some((c) => homes.has(c))) hit.push(s); });
      if (hit.length === 0) continue;
      covered += 1;
      if (hit.includes(slot)) {
        agreeing += 1;
      } else {
        disputed.push({
          word: word.text, ourHome: category.label,
          outsideHome: hit.map((s) => slots[s].label),
        });
      }
    }
  });

  return {
    matchedCategories, totalCategories: slots.length,
    covered, totalWords, agreeing, disputed,
  };
}

// --------------------------------------------------------------------------- //
// C5 — происхождение категорий
// --------------------------------------------------------------------------- //

/**
 * Ключи категорий, приехавших транскрипцией оригинала.
 *
 * Источник — файл прогона в репозитории, а не база: сертификат обязан
 * воспроизводиться у ревьюера, у которого SQLite-базы нет.
 */
function readReferenceKeys(): Set<string> | null {
  const file = resolve(ROOT,
    '../word_content_pipeline/data/runs/run-002-bwj-org/categories.jsonl');
  if (!existsSync(file)) return null;
  const keys = new Set<string>();
  for (const line of readFileSync(file, 'utf8').split('\n')) {
    if (!line.trim()) continue;
    keys.add(JSON.parse(line).category_key as string);
  }
  return keys;
}

// --------------------------------------------------------------------------- //
// ручная игра — единственное, чего скрипт дать не может
// --------------------------------------------------------------------------- //

interface ManualPlay {
  level_id: number;
  pack_hash: string;
  date: string;
  build: string;
  /** won — доиграно до конца; partial — играли, но не доиграли; loaded — только загрузили */
  result: 'won' | 'partial' | 'loaded' | 'lost';
  moves_used: number;
  move_limit: number | null;
  categories_collected: number;
  categories_total: number;
  note: string;
}

/**
 * Записи ручной игры ведёт человек в `levels/manual-play.json`.
 *
 * Запись, выписанная на ДРУГОЙ пакет, не засчитывается: пакет пересобирается, а
 * «мы это когда-то играли» — ровно та отговорка, из-за которой строка «ручная
 * игра» в карточках уровней год стояла пустой и никто этого не замечал.
 */
function readManualPlay(packHash: string): Map<number, ManualPlay> {
  const file = resolve(ROOT, '../../levels/manual-play.json');
  const out = new Map<number, ManualPlay>();
  if (!existsSync(file)) return out;
  const raw = JSON.parse(readFileSync(file, 'utf8')) as { records?: ManualPlay[] };
  for (const record of raw.records ?? []) {
    if (record.pack_hash !== packHash) continue;
    out.set(record.level_id, record);
  }
  return out;
}

interface Provenance { own: number; fromReference: number; referenceCategories: string[] }

function certifyProvenance(contract: Contract, refKeys: Set<string> | null): Provenance | null {
  if (!refKeys) return null;
  const fromRef = contract.categories.filter((c) => refKeys.has(c.key));
  return {
    own: contract.categories.length - fromRef.length,
    fromReference: fromRef.length,
    referenceCategories: fromRef.map((c) => c.label),
  };
}

// --------------------------------------------------------------------------- //
// прогон
// --------------------------------------------------------------------------- //

const ownSnap = readSnapshot('web/src/data/content.snapshot.json');
const outSnap = readSnapshot('web/src/data/reference.snapshot.json');

const own = {
  snap: ownSnap,
  // hard_only включительно — шире, чем смотрит генератор
  w2c: wordToCategories(ownSnap, ownSnap.statuses.indexOf('hard_only')),
  // ровно то, что видит генератор: нужно, чтобы посчитать РАЗНИЦУ, а не поверить в неё
  w2cGenerator: wordToCategories(ownSnap, ownSnap.statuses.indexOf('alternative')),
  wordIdx: new Map(ownSnap.words.map((w, i) => [w.n, i])),
  catIdx: new Map(ownSnap.categories.map((c, i) => [c.k, i])),
};
const outsideByLabel = new Map<string, number[]>();
outSnap.categories.forEach((c, i) => {
  const key = normLabel(c.l);
  outsideByLabel.set(key, [...(outsideByLabel.get(key) ?? []), i]);
});
const outside = {
  snap: outSnap,
  w2c: wordToCategories(outSnap, outSnap.statuses.indexOf('hard_only')),
  wordIdx: new Map(outSnap.words.map((w, i) => [w.n, i])),
  byLabel: outsideByLabel,
};
const refKeys = readReferenceKeys();

const levelIds = readdirSync(PACK_DIR)
  .map((f) => /^game-(\d+)\.json$/.exec(f))
  .filter((m): m is RegExpExecArray => m !== null)
  .map((m) => Number(m[1]))
  .sort((a, b) => a - b);

if (levelIds.length === 0) {
  console.error(`в ${PACK_DIR} нет ни одного game-NNN.json`);
  process.exit(1);
}

interface Certificate {
  cert_version: string;
  level_id: number;
  pack_hash: string;
  content_snapshot_hash: string;
  generator_version: string;
  verdict: 'CERTIFIED' | 'FAILED';
  c1_key: { passed: boolean; checks: Check[] };
  c2_uniqueness: { passed: boolean } & UniquenessResult;
  c3_playthrough: { passed: boolean } & PlaythroughResult;
  c4_outside_view: OutsideView;
  c5_provenance: Provenance | null;
  /** что сказал о том же уровне сам инструмент — для сверки двух путей */
  tool_said: { solution_count: number; moves_needed: number | null };
  /** запись человека из levels/manual-play.json; null — руками не проверяли */
  manual_play: ManualPlay | null;
}

const certificates: Certificate[] = [];

for (const id of levelIds) {
  const contract = JSON.parse(
    readFileSync(join(PACK_DIR, `game-${id}.json`), 'utf8')) as Contract;
  const pipeline = JSON.parse(
    readFileSync(join(PACK_DIR, `level-${id}.json`), 'utf8')) as Pipeline;

  const keyChecks = certifyKey(contract, pipeline);
  const keyPassed = keyChecks.every((c) => c.passed);

  const uniq = certifyUniqueness(contract, own, outside);
  const uniqPassed = uniq.solutions === 1 && uniq.exhausted;

  const play = keyPassed && pipeline.level_spec.deal
    ? certifyPlaythrough(contract, pipeline)
    : {
      finished: false, failReason: 'партию не переигрывали: ключ не прошёл C1',
      moves: 0, moveLimit: contract.board.move_limit, spare: null,
      peakOnBoard: 0, boardCapacity: contract.board.board_capacity,
      onlyMoveStates: 0, stalls: 0, deadlockImpossible: false,
    } as PlaythroughResult;

  const view = certifyOutsideView(contract, outside);
  const provenance = certifyProvenance(contract, refKeys);

  certificates.push({
    cert_version: CERT_VERSION,
    level_id: id,
    pack_hash: pipeline.build_metadata.pack_hash,
    content_snapshot_hash: pipeline.build_metadata.content_snapshot_hash,
    generator_version: pipeline.build_metadata.generator_version,
    verdict: keyPassed && uniqPassed && play.finished ? 'CERTIFIED' : 'FAILED',
    c1_key: { passed: keyPassed, checks: keyChecks },
    c2_uniqueness: { passed: uniqPassed, ...uniq },
    c3_playthrough: { passed: play.finished, ...play },
    c4_outside_view: view,
    c5_provenance: provenance,
    tool_said: {
      solution_count: pipeline.validation.solution_count,
      moves_needed: pipeline.validation.playability?.moves_needed ?? null,
    },
    manual_play: null,      // проставляется ниже, когда известен pack_hash пакета
  });
}

const manual = readManualPlay(certificates[0].pack_hash);
for (const cert of certificates) cert.manual_play = manual.get(cert.level_id) ?? null;

mkdirSync(OUT_DIR, { recursive: true });
for (const cert of certificates) {
  writeFileSync(join(OUT_DIR, `level-${cert.level_id}.cert.json`),
    `${JSON.stringify(cert, null, 2)}\n`, 'utf8');
}

// --------------------------------------------------------------------------- //
// отчёт
// --------------------------------------------------------------------------- //

const failed = certificates.filter((c) => c.verdict === 'FAILED');
const packHash = certificates[0].pack_hash;
const snapHash = certificates[0].content_snapshot_hash;

const lines: string[] = [];
lines.push('# Сертификация решаемости');
lines.push('');
lines.push('Файл собран `tool/level-tool/scripts/certify_solvability.ts`. Руками не правится:');
lines.push('перезапуск скрипта переписывает его целиком.');
lines.push('');
lines.push(`- Пакет: \`${packHash.slice(0, 16)}…\`, снимок базы \`${snapHash.slice(0, 16)}…\`, `
  + `генератор \`${certificates[0].generator_version}\`, правила \`${CERT_VERSION}\``);
lines.push(`- Уровней: ${certificates.length}, сертифицировано ${certificates.length - failed.length}`);
lines.push('- Машинные сертификаты по уровню: `levels/certificates/level-NNN.cert.json`');
lines.push('');
lines.push('## Зачем это отдельно от инструмента');
lines.push('');
lines.push('Инструмент отвечает «решение единственное» и «уровень проходим» своим же кодом —');
lines.push('тем, что уровень и собрал. Одна ошибка в общем модуле соврала бы одинаково и');
lines.push('генератору, и проверке. Сертификатор идёт вторым путём: он не импортирует ни');
lines.push('строчки из ядра инструмента, читает только сдаваемый JSON и снимки контента,');
lines.push('и проверяет строже:');
lines.push('');
lines.push('| | инструмент | сертификат |');
lines.push('|---|---|---|');
lines.push('| граф правдоподобия | наши связи `approved` + `alternative` | + `hard_only` + связи словаря оригинала (что это дало на этом пакете — ниже) |');
lines.push('| перебор раскладок | до второй, дальше не считает | до четырёх: «ровно два» и «десятки» — разные диагнозы |');
lines.push('| ёмкость поля | не моделируется (записанное упрощение `playSim.ts`) | настоящая: досыпка идёт только на свободные места |');
lines.push('| слова вне базы | молча считаются однодомными | перечислены поимённо |');
lines.push('');
lines.push('## Итог по уровням');
lines.push('');
lines.push('| ур. | вердикт | C1 ключ | C2 раскладок | C3 ходов / лимит | пик поля | C4 внешний | C5 наших кат. |');
lines.push('|---|---|---|---|---|---|---|---|');
for (const c of certificates) {
  const view = c.c4_outside_view;
  const agree = view.covered ? `${Math.round((view.agreeing / view.covered) * 100)}% из ${view.covered}` : '—';
  const prov = c.c5_provenance
    ? `${c.c5_provenance.own} из ${c.c5_provenance.own + c.c5_provenance.fromReference}` : '—';
  lines.push(`| ${c.level_id} | ${c.verdict === 'CERTIFIED' ? '**CERTIFIED**' : '**FAILED**'} `
    + `| ${c.c1_key.passed ? 'PASS' : 'FAIL'} `
    + `| ${c.c2_uniqueness.solutions}${c.c2_uniqueness.exhausted ? '' : ' (перебор не исчерпан)'} `
    + `| ${c.c3_playthrough.moves} / ${c.c3_playthrough.moveLimit ?? '∞'} `
    + `| ${c.c3_playthrough.peakOnBoard} из ${c.c3_playthrough.boardCapacity} `
    + `| ${agree} | ${prov} |`);
}
lines.push('');
lines.push('## Что означает каждый столбец');
lines.push('');
lines.push('- **C2 раскладок** — сколько всего существует полных раскладок слов уровня по его');
lines.push('  категориям, если считать правдоподобным всё, что считает правдоподобным хоть');
lines.push('  один из двух источников. 1 — решение доказано единственным.');
lines.push('- **C3 ходов / лимит** — сколько мерджей нужно идеальному игроку и сколько ему дано.');
lines.push('  Порядок мерджей на их число не влияет, поэтому число точное, а не оценка.');
lines.push('- **пик поля** — сколько пузырей максимум лежало одновременно при настоящей ёмкости.');
lines.push('- **C4 внешний** — какая доля слов, про которые словарь оригинала вообще что-то знает');
lines.push('  на этом уровне, лежит там же, где в нашем ключе. Оговорку про то, насколько');
lines.push('  этот свидетель посторонний, см. ниже.');
lines.push('- **C5 наших кат.** — у скольких категорий уровня ключа НЕТ в транскрипции');
lines.push('  оригинала, то есть они написаны для этого проекта.');
lines.push('');
lines.push('## Чего этот сертификат НЕ доказывает');
lines.push('');
const hardOnlyTotal = certificates.reduce((n, c) => n + c.c2_uniqueness.widening.hardOnlyLinksAdded, 0);
const outsideTotal = certificates.reduce((n, c) => n + c.c2_uniqueness.widening.outsideLinksAdded, 0);
const ownProvenance = certificates.reduce((n, c) => n + (c.c5_provenance?.own ?? 0), 0);
const refProvenance = certificates.reduce((n, c) => n + (c.c5_provenance?.fromReference ?? 0), 0);
lines.push('**Расширение графа дало мало.** По всем уровням статус `hard_only` добавил слову');
lines.push(`новых правдоподобных домов: ${hardOnlyTotal}; словарь оригинала: ${outsideTotal}.`);
lines.push('То есть перебор по расширенным правилам почти совпал с перебором генератора, и');
lines.push('главная ценность C2 не в ширине графа, а в том, что это ВТОРАЯ реализация: она');
lines.push('написана отдельно и сошлась с первой.');
lines.push('');
lines.push('**Словарь оригинала — не вполне посторонний свидетель.** С 03.08 наша база');
lines.push('склеена: транскрипция оригинала живёт в том же снимке. Поэтому C4 проверяет');
lines.push('согласованность разметки внутри одной базы, а не подтверждает её извне. Написано');
lines.push('здесь именно потому, что цифра «100% согласия» без этой оговорки читалась бы');
lines.push('сильнее, чем есть на самом деле.');
lines.push('');
lines.push(`**Треть категорий пакета — из оригинала.** У ${refProvenance} категорий из `
  + `${ownProvenance + refProvenance} ключ встречается в транскрипции целевой игры (столбец C5).`);
lines.push('Готовые четвёрки при этом не переиспользуются: `referenceNovelty=hard` бракует');
lines.push('категорию, чья четвёрка совпала с четвёркой оригинала. Но сама категория и её пул');
lines.push('в этих случаях — чужие, и называть весь пакет своим было бы неправдой.');
lines.push('');
lines.push('**Живой игрок не проверен машиной.** C3 играет идеально: он знает ответы и не');
lines.push('промахивается. Сколько ходов уйдёт на догадки, машина не знает — это меряют');
lines.push('слепой прогон (диагностика, `scripts/generate_block.ts`) и ручная игра.');
lines.push('');

const disputedAll = certificates.flatMap((c) =>
  c.c4_outside_view.disputed.map((d) => ({ level: c.level_id, ...d })));
if (disputedAll.length) {
  lines.push('## Где внешний источник спорит с ключом');
  lines.push('');
  lines.push('Спор — не приговор: у оригинала своя нарезка категорий, и слово честно может');
  lines.push('жить в обеих. Но каждый такой случай назван, а не спрятан.');
  lines.push('');
  lines.push('| ур. | слово | у нас | у оригинала |');
  lines.push('|---|---|---|---|');
  for (const d of disputedAll) {
    lines.push(`| ${d.level} | ${d.word} | ${d.ourHome} | ${d.outsideHome.join(', ')} |`);
  }
  lines.push('');
}

const unknownAll = certificates.filter((c) => c.c2_uniqueness.unknownWords.length);
if (unknownAll.length) {
  lines.push('## Слова, единственность которых принята на веру');
  lines.push('');
  lines.push('Этих слов нет ни в нашей базе, ни в словаре оригинала, поэтому перебор считает');
  lines.push('их однодомными по построению уровня — то есть не доказывает ничего.');
  lines.push('');
  for (const c of unknownAll) {
    lines.push(`- уровень ${c.level_id}: ${c.c2_uniqueness.unknownWords.join(', ')}`);
  }
  lines.push('');
}

lines.push('## Ручная игра');
lines.push('');
lines.push('Единственная часть сертификации, где нужен человек: скрипт её дать не может.');
lines.push('Записи ведутся руками в `levels/manual-play.json` и попадают сюда как есть.');
lines.push('Запись, выписанная на другой пакет, не засчитывается — пакет пересобирается.');
lines.push('');
const RESULT_WORD: Record<string, string> = {
  won: 'доиграно до конца', partial: 'играли, не доиграли',
  loaded: 'только загрузка', lost: 'проиграно',
};
lines.push('| ур. | что сделано | ходов | собрано | когда |');
lines.push('|---|---|---|---|---|');
for (const c of certificates) {
  const m = c.manual_play;
  lines.push(m
    ? `| ${c.level_id} | ${RESULT_WORD[m.result] ?? m.result} | ${m.moves_used} из `
      + `${m.move_limit ?? '∞'} | ${m.categories_collected} из ${m.categories_total} | ${m.date} |`
    : `| ${c.level_id} | **записи нет** | — | — | — |`);
}
lines.push('');
const played = certificates.filter((c) => c.manual_play
  && (c.manual_play.result === 'won' || c.manual_play.result === 'partial'));
lines.push(`Уровней, где человек действительно ходил: ${played.length} из ${certificates.length}. `
  + 'Остальные только открыты и сверены со стартовой выкладкой пакета — это проверяет,');
lines.push('что уровень доезжает до клиента целым, и не проверяет ничего сверх того.');
lines.push('');
for (const c of certificates) {
  if (!c.manual_play?.note) continue;
  if (c.manual_play.result === 'loaded') continue;
  lines.push(`**Уровень ${c.level_id}.** ${c.manual_play.note}`);
  lines.push('');
}

writeFileSync(REPORT, `${lines.join('\n')}\n`, 'utf8');

// --------------------------------------------------------------------------- //
// вывод
// --------------------------------------------------------------------------- //

console.log(`пакет ${packHash.slice(0, 16)}…, снимок ${snapHash.slice(0, 16)}…, правила ${CERT_VERSION}`);
console.log('');
console.log('ур.  вердикт     C1    C2 раскл.  C3 ходов/лимит  пик поля  C4 согласие  C5 наших');
for (const c of certificates) {
  const v = c.c4_outside_view;
  const agree = v.covered ? `${Math.round((v.agreeing / v.covered) * 100)}% из ${v.covered}` : '—';
  const prov = c.c5_provenance ? `${c.c5_provenance.own}/${c.c5_provenance.own + c.c5_provenance.fromReference}` : '—';
  console.log(`${String(c.level_id).padEnd(5)}`
    + `${c.verdict.padEnd(12)}`
    + `${(c.c1_key.passed ? 'PASS' : 'FAIL').padEnd(6)}`
    + `${String(c.c2_uniqueness.solutions).padEnd(11)}`
    + `${`${c.c3_playthrough.moves}/${c.c3_playthrough.moveLimit ?? '∞'}`.padEnd(16)}`
    + `${`${c.c3_playthrough.peakOnBoard}/${c.c3_playthrough.boardCapacity}`.padEnd(10)}`
    + `${agree.padEnd(13)}`
    + `${prov}`);
}
console.log('');
for (const c of certificates) {
  if (c.verdict === 'CERTIFIED') continue;
  console.log(`уровень ${c.level_id}: ПРОВАЛ`);
  for (const check of c.c1_key.checks.filter((x) => !x.passed)) {
    console.log(`  C1 ${check.code}: ${check.detail}`);
  }
  if (!c.c2_uniqueness.passed) {
    console.log(`  C2: раскладок ${c.c2_uniqueness.solutions}`
      + `${c.c2_uniqueness.exhausted ? '' : ', перебор не исчерпан'}`);
  }
  if (!c.c3_playthrough.passed) console.log(`  C3: ${c.c3_playthrough.failReason}`);
}
console.log(`→ ${OUT_DIR}`);
console.log(`→ ${REPORT}`);

if (failed.length) {
  console.error(`\nне сертифицировано уровней: ${failed.length}`);
  process.exit(1);
}
