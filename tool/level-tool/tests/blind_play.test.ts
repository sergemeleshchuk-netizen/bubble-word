/**
 * Слепой бот — обещания релиза 1.25.0.
 *
 * Проверяется то, на чём эта модель может сломаться молча:
 *   1. Движок партии (`core/playSim.ts`) общий у зрячего и слепого бота, и
 *      зрячий после выделения движка отвечает то же, что и до него. Если правила
 *      мерджа разъедутся, hard-гейт и диагностика начнут судить по разным законам.
 *   2. Прогон воспроизводим: тот же seed — те же числа. Без этого стохастическая
 *      модель не имеет права стоять рядом с детерминированными проверками.
 *   3. Слепой игрок платит ходами и НИКОГДА не платит меньше зрячего: минимум
 *      ходов — это пол, ниже которого партии не бывает.
 *   4. Партия всегда сходится: у бота есть память о неудачных попытках, и
 *      исключение обязано доводить его до конца. Зависший прогон (уровни 65 и 95
 *      в первой редакции — бесконечная попытка мерджа поперёк цепи) означает
 *      не «уровень трудный», а сломанную модель.
 *   5. Ясность слова монотонна по обеим осям — иначе «трудное» и «лёгкое»
 *      поменялись бы местами незаметно.
 *   6. Диагностика остаётся диагностикой: слепой прогон не влияет ни на D, ни на
 *      приёмку уровня.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { configForRange } from '../web/src/core/decadeProfiles.ts';
import { generateBlock } from '../web/src/core/generateBlock.ts';
import { simulatePlayability } from '../web/src/core/simulatePlayability.ts';
import { simulateBlindPlay } from '../web/src/core/simulateBlindPlay.ts';
import { createPlaySim, hasDeal } from '../web/src/core/playSim.ts';
import { DEFAULT_KNOWLEDGE, wordClarity } from '../web/src/core/playerKnowledge.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

// декада 31-40 несёт все ветки модификаторов (половинки, блокиратор, цепь),
// пресет — сдаваемый пакет: слепой бот обязан переживать и то и другое
const block = generateBlock({
  snapshot, scoring, config: configForRange([31, 40], 'blind-test'),
});
const preset = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
const all = [...block.levels, ...preset.levels];

test('движок партии общий: зрячий бот собирает уровень своими правилами', () => {
  for (const level of all) {
    const spec = level.spec;
    assert.equal(hasDeal(spec), true, `уровень ${spec.levelId}: выкладки нет`);
    // независимая проверка движка: пузырей на старте столько же, сколько
    // в выкладке плюс по одному на каждый распил (половинка = два пузыря)
    const sim = createPlaySim(spec);
    const splitsOnStart = spec.deal.start.filter((b) =>
      spec.halves.some((h) => h.home === b.category
        && h.word.toLowerCase() === b.word.toLowerCase())).length;
    assert.equal(sim.field.length, spec.deal.start.length + splitsOnStart,
      `уровень ${spec.levelId}: движок разложил поле не по выкладке`);
  }
});

test('слепой прогон воспроизводим: тот же seed — те же числа', () => {
  for (const level of all.slice(0, 6)) {
    const floor = simulatePlayability(level.spec).movesNeeded;
    const a = simulateBlindPlay(level.spec, floor, { seed: 'фикс', seeds: 8 });
    const b = simulateBlindPlay(level.spec, floor, { seed: 'фикс', seeds: 8 });
    assert.deepEqual(a, b, `уровень ${level.spec.levelId}: прогон не воспроизвёлся`);
  }
});

test('другой seed — другой игрок: числа не высечены в камне', () => {
  // модель стохастическая по замыслу (игроки знают разные слова). Если seed ни
  // на что не влияет, значит бросок «прочитал» где-то потерялся, и вся модель
  // выродилась в одну детерминированную траекторию
  const withSeed = (seed: string) => all
    .map((l) => simulateBlindPlay(l.spec, simulatePlayability(l.spec).movesNeeded,
      { seed, seeds: 4 }).movesMedian);
  assert.notDeepEqual(withSeed('игрок-А'), withSeed('игрок-Б'),
    'seed не меняет ни один прогон: выборка знакомых слов не работает');
});

test('слепой игрок не бывает дешевле зрячего и всегда доигрывает', () => {
  for (const level of all) {
    const play = simulatePlayability(level.spec);
    const blind = simulateBlindPlay(level.spec, play.movesNeeded,
      { seed: `blind-${level.spec.levelId}`, seeds: 12 });

    assert.equal(blind.hardStalls, 0,
      `уровень ${level.spec.levelId}: партия встала в ${blind.hardStalls} прогонах — `
      + 'память о неудачных попытках не доводит бота до конца');
    assert.ok(blind.movesMedian >= play.movesNeeded,
      `уровень ${level.spec.levelId}: слепой обошёлся ${blind.movesMedian} ходами `
      + `при минимуме ${play.movesNeeded} — минимум перестал быть полом`);
    assert.ok(blind.movesP90 >= blind.movesMedian,
      `уровень ${level.spec.levelId}: p90 ниже медианы`);
    assert.equal(blind.movesMedian - blind.missesMedian >= play.movesNeeded, true,
      `уровень ${level.spec.levelId}: лишние ходы не сходятся с промахами`);
  }
});

test('уровень из читаемых слов проходится без промахов', () => {
  // граничный случай модели: ясность 1 означает «игрок читает всё», и тогда
  // слепой бот обязан совпасть со зрячим. Если не совпадает — блуждает где-то
  // ещё, помимо незнания слов
  const clairvoyant = { ...DEFAULT_KNOWLEDGE, skill: 100 };
  for (const level of all) {
    const play = simulatePlayability(level.spec);
    const blind = simulateBlindPlay(level.spec, play.movesNeeded,
      { seed: 'ясно', seeds: 3, model: clairvoyant });
    assert.equal(blind.missesP90, 0,
      `уровень ${level.spec.levelId}: промахи при полной ясности слов`);
    assert.equal(blind.movesP90, play.movesNeeded,
      `уровень ${level.spec.levelId}: при полной ясности слепой бот разошёлся `
      + `со зрячим (${blind.movesP90} против ${play.movesNeeded})`);
  }
});

test('уровень из нечитаемых слов дороже, а не сломан', () => {
  // противоположный край: ясность 0, игрок не понимает ни одного слова и
  // раскладывает уровень чистым исключением. Дорого — но обязан доиграть
  const blindfold = { ...DEFAULT_KNOWLEDGE, skill: 0 };
  let paidSomewhere = 0;
  for (const level of all.slice(0, 6)) {
    const play = simulatePlayability(level.spec);
    const blind = simulateBlindPlay(level.spec, play.movesNeeded,
      { seed: 'вслепую', seeds: 3, model: blindfold });
    assert.equal(blind.hardStalls, 0,
      `уровень ${level.spec.levelId}: полностью слепая партия встала`);
    if (blind.missesMedian > 0) paidSomewhere += 1;
    /*
     * Промах требуется там, где уровень нельзя разложить одним исключением.
     * Если развилок нет (`deductionOnly`), нулевая цена — не поломка модели, а
     * свойство уровня: игрок доходит перебором размеров групп, не прочитав ни
     * одного слова, и приёмка сама помечает это soft-правилом DEDUCTION_ONLY.
     *
     * До 04.08 здесь стояло безусловное `missesMedian > 0`, и держалось оно на
     * везении: в декаде 31-40 просто не попадалось уровня без развилок. С
     * gen-1.9 состав четвёрок сменился, уровень 36 оказался чисто дедуктивным —
     * и тест упал на свойстве уровня, а не на ошибке слепого бота.
     */
    if (level.structural && !level.structural.deductionOnly) {
      assert.ok(blind.missesMedian > 0,
        `уровень ${level.spec.levelId}: на уровне есть развилки, но игрок без `
        + 'словаря прошёл его без единого промаха — значит догадка бота видит ответ');
    }
  }
  assert.ok(paidSomewhere > 0,
    'ни на одном уровне слепой игрок не заплатил промахом: '
    + 'модель незнания слов ничего не стоит');
});

test('ясность слова монотонна по частотности и по очевидности связи', () => {
  const clear = { zipf: 5.0, obviousness: 0.95 };
  const rare = { zipf: 2.0, obviousness: 0.95 };
  const quiet = { zipf: 5.0, obviousness: 0.35 };
  assert.ok(wordClarity(clear) > wordClarity(rare), 'редкость не снижает ясность');
  assert.ok(wordClarity(clear) > wordClarity(quiet), 'неочевидность не снижает ясность');
  /*
   * Главная асимметрия модели: ослепляет неочевидность связи, а редкость только
   * замедляет. Редкое, но бесспорное слово (`narwhal` в ARCTIC ANIMALS) обязано
   * остаться читаемым большинству, а расхожее, но неочевидное (`delta` в
   * AIRLINES) — нет. Первая редакция складывала оси и заваливала первый случай.
   */
  assert.ok(wordClarity(rare) > 0.5,
    `редкое бесспорное слово стало нечитаемым: ${wordClarity(rare).toFixed(2)}`);
  assert.ok(wordClarity(rare) > wordClarity(quiet),
    'редкость мешает сильнее неочевидности: оси поменялись ролями');
  for (const value of [wordClarity({ zipf: null, obviousness: undefined }),
    wordClarity({ zipf: 99, obviousness: 1 }), wordClarity({ zipf: -99, obviousness: 0 })]) {
    assert.ok(value >= 0 && value <= 1, `ясность вышла из 0..1: ${value}`);
  }
});

test('слепой прогон — диагностика: в D и в приёмку не входит', () => {
  const source = readFileSync(
    join(ROOT, 'web/src/core/scoringDifficulty.ts'), 'utf8');
  assert.ok(!source.includes('simulateBlindPlay') && !source.includes('blindPlay'),
    'модель сложности читает слепой прогон: неоткалиброванное число попало в D');

  // в блоке прогон есть у каждого принятого уровня, но уровни всё равно приняты
  for (const level of all) {
    assert.ok(level.blindPlay, `уровень ${level.spec.levelId}: слепого прогона нет`);
    assert.equal(level.blindPlay!.unavailable, null);
    assert.equal(level.validation.passed, true,
      `уровень ${level.spec.levelId}: не прошёл приёмку — слепой прогон не должен её менять`);
  }
});

test('догадка остаётся догадкой: порядок целей не подсматривает ответ', () => {
  /*
   * Страховка от главного способа незаметно обесценить эту модель. Догадка бота
   * опирается на размер уже собранной группы — эвристика правильная, живой игрок
   * тащит туда же, — но если она начнёт попадать почти всегда, цена незнания
   * слов схлопнется в ноль, а числа останутся правдоподобными. Замер по трём
   * декадам: 84% верных догадок в среднем, от 35% на трудных уровнях до 100%
   * на простых. Порог 0.95 ловит именно вырождение, а не разброс.
   */
  let sum = 0;
  let counted = 0;
  for (const level of all) {
    const b = level.blindPlay!;
    assert.ok(b.probeHitRate >= 0 && b.probeHitRate <= 1,
      `уровень ${level.spec.levelId}: доля верных догадок вне 0..1`);
    if (b.probesMedian > 0) { sum += b.probeHitRate; counted += 1; }
  }
  assert.ok(counted > 0, 'ни на одном уровне бот не гадал: модель незнания не работает');
  assert.ok(sum / counted < 0.95,
    `догадки верны в ${Math.round((sum / counted) * 100)}% случаев: порядок целей `
    + 'подсматривает ответ, и цена незнания слов занижена до нуля');
});

test('сила связи берётся из снимка, а не из сырого поля спека', () => {
  /*
   * Регрессия на реальную ошибку первой редакции. У словаря оригинала связи
   * происхождения `reference` (две трети словаря) несут в поле `obviousness`
   * заглушку 0.41 — нашей разметки за ними нет, настоящий сигнал в `weight`.
   * Модель читала спек напрямую, и ясность блока падала с 0.75 до 0.50 при
   * переключении источника: уровни объявлялись труднее просто потому, что
   * разметка другая. Генератор давно читает `weight ?? obviousness`
   * (`obviousnessIn`), и слепой бот обязан читать так же.
   */
  const lexicon = JSON.parse(readFileSync(
    join(ROOT, 'web/src/data/lexicon.snapshot.json'), 'utf8')) as Snapshot;
  const lexBlock = generateBlock({
    snapshot: lexicon, scoring, config: configForRange([41, 50], 'blind-lexicon'),
  });
  const index = new ContentIndex(lexicon);

  let better = 0;
  for (const level of lexBlock.levels) {
    const floor = simulatePlayability(level.spec).movesNeeded;
    const fromIndex = simulateBlindPlay(level.spec, floor,
      { seed: 'сигнал', seeds: 2, index });
    const fromSpec = simulateBlindPlay(level.spec, floor, { seed: 'сигнал', seeds: 2 });
    assert.equal(fromIndex.signalFromSpec, false);
    assert.equal(fromSpec.signalFromSpec, true);
    if (fromIndex.clarity > fromSpec.clarity + 0.05) better += 1;
  }
  assert.ok(better >= lexBlock.levels.length / 2,
    `сигнал из снимка поднял ясность только на ${better} уровнях из `
    + `${lexBlock.levels.length}: похоже, снимок опять не читается`);

  // на принятых уровнях блока прогон обязан быть посчитан ПО СНИМКУ
  for (const level of lexBlock.levels) {
    assert.equal(level.blindPlay?.signalFromSpec, false,
      `уровень ${level.spec.levelId}: блок посчитал слепой прогон без снимка`);
  }
});

test('спек без выкладки: слепой прогон честно отказывается', () => {
  const noDeal = { ...all[0].spec, deal: undefined } as never;
  const blind = simulateBlindPlay(noDeal, 0);
  assert.match(blind.unavailable ?? '', /выкладки нет/);
  assert.equal(blind.seeds, 0);
  assert.equal(blind.movesMedian, 0);
});
