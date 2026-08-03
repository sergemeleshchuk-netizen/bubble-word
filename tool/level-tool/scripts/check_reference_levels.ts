/**
 * Диагностика уровней из источника «RefBWJ»: проигрываются ли они вообще.
 *
 *   node scripts/check_reference_levels.ts [1-40]
 *
 * Зачем отдельно от `simulate_play.ts`. Тот читает готовые handoff-пакеты из
 * `site/playable/packs/`, а уровни оригинала пакетом не выкладываются: их
 * собирают в инструменте на месте (`buildReferenceBlock`) и сразу отдают в
 * прототип. Поэтому жалобу «уровень из рефа встал, остался один шар» проверить
 * было нечем — здесь тот же зрячий бот, но по спекам реф-источника.
 *
 * Печатает по каждому уровню вердикт и, если уровень встал, РАЗБОР остатка:
 * какие пузыри остались на поле, каким категориям они принадлежат, сколько слов
 * этим категориям нужно и сколько их вообще есть в уровне. Именно эта тройка
 * чисел отвечает на вопрос «шар лишний или его пара потерялась».
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import {
  buildReferenceBlock, parseLevelSelection, type BwjLevels,
} from '../web/src/core/referenceLevels.ts';
import { simulatePlayability } from '../web/src/core/simulatePlayability.ts';
import { createPlaySim } from '../web/src/core/playSim.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;
const bwj = JSON.parse(readFileSync(
  join(ROOT, 'web/src/data/bwj-levels.json'), 'utf8')) as BwjLevels;

const arg = process.argv[2] ?? '1-40';
const maxId = bwj.levels.reduce((n, l) => Math.max(n, l.id), 0);
const picked = parseLevelSelection(arg, maxId);
const ids = picked.ids;
if (!ids.length) throw new Error(`не разобрал выбор уровней «${arg}»`);

const index = new ContentIndex(snapshot);
const block = buildReferenceBlock(index, bwj, ids, scoring);
console.log(`уровней собрано: ${block.levels.length}`
  + (block.missing.length ? `, нет в выгрузке: ${block.missing.join(', ')}` : ''));

let broken = 0;
for (const level of block.levels) {
  const spec = level.spec;
  const play = simulatePlayability(spec);
  const mark = play.winnable ? 'PASS' : 'FAIL';
  if (!play.winnable) broken += 1;
  console.log(`  ${mark}  ур.${String(spec.levelId).padStart(4)} `
    + `${spec.categories.length} кат · ходов ${play.movesNeeded}/${play.moveLimit ?? '∞'} `
    + `· страховка ${play.rescues} · ${play.failReason ?? 'win'}`);
  if (play.winnable) continue;

  /*
   * Разбор остатка. Партию проигрываем заново тем же жадным правилом (мозг
   * зрячего бота), потому что simulatePlayability возвращает вердикт, а не поле.
   */
  const sim = createPlaySim(spec);
  for (let guard = 0; guard < 20000 && !sim.won(); guard += 1) {
    const pairs = sim.legalPairs();
    if (pairs.length === 0) { if (sim.rescue() === null) break; continue; }
    const field = sim.field;
    const done = pairs.find(([i, j]) => field[i].halfPair === 0
      && field[i].words.length + field[j].words.length === sim.fullOf(field[i].category));
    const pick = done ?? pairs.find(([i]) => field[i].halfPair !== 0) ?? pairs[0];
    sim.attempt(pick[0], pick[1]);
  }
  const spawnable = new Map<string, number>();
  for (const c of spec.categories) {
    spawnable.set(c.key, c.words.filter((w) => w.kind !== 'meta').length);
  }
  console.log(`        осталось на поле ${sim.field.length}, в очереди ${sim.queueLength()}, `
    + `собрано ${sim.categoriesDone()}/${sim.categoriesTotal()}`);
  for (const b of sim.field) {
    const cat = spec.categories.find((c) => c.key === b.category);
    console.log(`        · ${b.words.join('+')} → ${b.category} `
      + `(нужно ${sim.fullOf(b.category)}, слов в уровне ${cat?.words.length ?? '?'}, `
      + `из них спавнится ${spawnable.get(b.category) ?? '?'}`
      + `${b.halfPair ? ', половинка' : ''}${b.blocked ? ', заблокирован' : ''})`);
  }
}
console.log(broken ? `\nне проигрываются: ${broken}` : '\nвсе выбранные уровни проигрываются');
