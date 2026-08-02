/**
 * Проходится ли уровень вообще — симулятор партии без браузера.
 *
 *   node scripts/simulate_play.ts [файл.handoff.json ...]
 *   node scripts/simulate_play.ts --all      # все пакеты из манифеста сайта
 *
 * Зачем понадобилось. Уровень 12 оригинала — тот самый, который в записи
 * проходится с запасом 15 ходов, — у нас встал на 1/12 с 34 ходами в руках.
 * Ни одна проверка проекта этого не видела: валидатор доказывает, что уровень
 * СОБИРАЕТСЯ (у каждого слова ровно один дом), решатель — что раскладка
 * единственна. Обе смотрят на список категорий и ни одна не смотрит на ПОЛЕ:
 * сколько пузырей помещается, что приходит на смену собранным, хватает ли
 * ходов. А сломалось ровно поле.
 *
 * Что моделируется (правила из GDD §2 и reference-analysis.md):
 *   * на поле не больше `board_capacity` пузырей;
 *   * мердж двух пузырей одной категории даёт один пузырь, тратит ход;
 *   * четвёртое слово схлопывает категорию: обычная уходит с поля, а
 *     мета-ребёнок ПРЕВРАЩАЕТСЯ в пузырь-слово родителя и место занимать
 *     продолжает;
 *   * досыпка идёт ПО МЕРЕ ОСВОБОЖДЕНИЯ МЕСТА, а не по собранным категориям
 *     (наблюдение записи: «новые пузыри падают волнами по мере освобождения
 *     места»). Именно это правило прототип и нарушал.
 *
 * Чего НЕ моделируется: физика, промахи драга, бустеры и бонус-пузыри «+5
 * ходов». Поэтому вердикт читается так: «не прошёл» — уровень сломан наверняка;
 * «прошёл с запасом N» — верхняя оценка, живой игрок потратит больше.
 *
 * Бот жадный и намеренно неумный: сначала то, что достраивает категорию до
 * четырёх, потом самая крупная пара. Умный бот доказывал бы, что уровень
 * проходим гением, а нужно обратное — что он проходим без гения.
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const PACKS = resolve(ROOT, '../../site/playable/packs');

interface HandoffLevelJson {
  level_id: number;
  title?: string;
  categories: { id: string; name: string; words: string[] }[];
  board: { board_capacity: number; move_limit: number | null };
  deal: { start: { word: string; category: string }[];
    queue: { word: string; category: string }[] };
  chunks?: { word: string; category: string; pieces: [string, string] }[];
}

export interface PlayResult {
  won: boolean;
  categoriesDone: number;
  categoriesTotal: number;
  movesUsed: number;
  moveLimit: number | null;
  /** почему остановились: 'win' | 'нет ходов' | 'нет легального мерджа' */
  reason: string;
  /** минимум пузырей, до которого проседало поле */
  fieldMin: number;
  /** сколько слов осталось в очереди на момент остановки */
  queueLeft: number;
}

/** Один пузырь на поле: категория и сколько слов в нём уже слиплось. */
interface Cluster { cat: string; size: number; }

export function simulate(level: HandoffLevelJson): PlayResult {
  const capacity = level.board.board_capacity || 24;
  const limit = level.board.move_limit;
  const total = level.categories.length;

  // мета-ребёнок: его имя лежит словом в другой категории уровня
  const nameToId = new Map(level.categories.map((c) => [c.name.toUpperCase(), c.id]));
  const parentOf = new Map<string, { parent: string }>();
  for (const c of level.categories) {
    for (const w of c.words) {
      const childId = nameToId.get(w.toUpperCase());
      if (childId !== undefined && childId !== c.id) parentOf.set(childId, { parent: c.id });
    }
  }
  // сколько слов нужно категории: мета-слово тоже слово, четвёрка есть четвёрка
  const need = new Map(level.categories.map((c) => [c.id, c.words.length]));

  // распиленное слово приходит двумя пузырями и стоит лишний ход на склейку
  const chunked = new Set((level.chunks ?? []).map((c) => `${c.category}::${c.word.toLowerCase()}`));
  const expand = (b: { word: string; category: string }): Cluster[] =>
    (chunked.has(`${b.category}::${b.word.toLowerCase()}`)
      // половинка моделируется как «пузырь ценой в один лишний ход»: на поле их
      // два, склейка тратит ход и даёт одно слово
      ? [{ cat: `half:${b.category}::${b.word}`, size: 1 },
        { cat: `half:${b.category}::${b.word}`, size: 1 }]
      : [{ cat: b.category, size: 1 }]);

  const queue: Cluster[] = level.deal.queue.flatMap(expand);
  let field: Cluster[] = level.deal.start.flatMap(expand);

  const topUp = () => {
    while (field.length < capacity && queue.length) field.push(queue.shift()!);
  };
  topUp();

  let moves = 0;
  let done = 0;
  let fieldMin = field.length;
  const halfNeed = 2;

  for (let guard = 0; guard < 5000; guard += 1) {
    fieldMin = Math.min(fieldMin, field.length);
    if (done >= total) {
      return { won: true, categoriesDone: done, categoriesTotal: total, movesUsed: moves,
        moveLimit: limit, reason: 'win', fieldMin, queueLeft: queue.length };
    }
    if (limit !== null && moves >= limit) {
      return { won: false, categoriesDone: done, categoriesTotal: total, movesUsed: moves,
        moveLimit: limit, reason: 'кончились ходы', fieldMin, queueLeft: queue.length };
    }

    // все легальные пары
    let best: [number, number] | null = null;
    let bestScore = -1;
    for (let i = 0; i < field.length; i += 1) {
      for (let j = i + 1; j < field.length; j += 1) {
        const a = field[i];
        const b = field[j];
        if (a.cat !== b.cat) continue;
        const cap = a.cat.startsWith('half:') ? halfNeed : (need.get(a.cat) ?? 4);
        const sum = a.size + b.size;
        if (sum > cap) continue;
        // жадность: достроить категорию важнее, крупная пара важнее мелкой
        const score = (sum === cap ? 100 : 0) + sum;
        if (score > bestScore) { bestScore = score; best = [i, j]; }
      }
    }
    if (!best) {
      return { won: false, categoriesDone: done, categoriesTotal: total, movesUsed: moves,
        moveLimit: limit, reason: 'нет легального мерджа', fieldMin, queueLeft: queue.length };
    }

    const [i, j] = best;
    const a = field[i];
    const b = field[j];
    const cap = a.cat.startsWith('half:') ? halfNeed : (need.get(a.cat) ?? 4);
    const merged: Cluster = { cat: a.cat, size: a.size + b.size };
    field = field.filter((_, k) => k !== i && k !== j);
    moves += 1;

    if (a.cat.startsWith('half:')) {
      // склеили половинки — получился обычный пузырь-слово своей категории
      const categoryKey = a.cat.slice('half:'.length).split('::')[0];
      field.push({ cat: categoryKey, size: 1 });
    } else if (merged.size >= cap) {
      done += 1;
      const parent = parentOf.get(a.cat);
      // мета-ребёнок не уходит с поля: он становится словом родителя
      if (parent) field.push({ cat: parent.parent, size: 1 });
    } else {
      field.push(merged);
    }
    topUp();
  }
  return { won: false, categoriesDone: done, categoriesTotal: total, movesUsed: moves,
    moveLimit: limit, reason: 'симуляция зациклилась', fieldMin, queueLeft: queue.length };
}

// --------------------------------------------------------------------------- //
// запуск
// --------------------------------------------------------------------------- //
function main(): void {
  const args = process.argv.slice(2);
  let files: string[];
  if (args.includes('--all') || args.length === 0) {
    const index = JSON.parse(readFileSync(join(PACKS, 'index.json'), 'utf8')) as
      { packs: string[] };
    files = index.packs.map((f) => join(PACKS, f));
  } else {
    files = args.map((f) => resolve(f));
  }

  let broken = 0;
  for (const file of files) {
    const pack = JSON.parse(readFileSync(file, 'utf8')) as
      { label: string; levels: HandoffLevelJson[] };
    console.log(`\n${pack.label}  (${file.split('/').pop()})`);
    for (const level of pack.levels) {
      const r = simulate(level);
      const spare = r.moveLimit === null ? '∞' : `${r.moveLimit - r.movesUsed}`;
      const mark = r.won ? 'PASS' : 'FAIL';
      if (!r.won) broken += 1;
      console.log(`  ${mark}  ур.${String(level.level_id).padStart(3)} `
        + `${(level.title ?? '').slice(0, 44).padEnd(44)} `
        + `${r.categoriesDone}/${r.categoriesTotal} кат · `
        + `ходов ${r.movesUsed}/${r.moveLimit ?? '∞'} (запас ${spare}) · `
        + `поле проседало до ${r.fieldMin} · ${r.reason}`);
    }
  }
  console.log(broken ? `\nнепроходимых уровней: ${broken}` : '\nвсе уровни проходятся');
}

if (process.argv[1] && process.argv[1].endsWith('simulate_play.ts')) main();
