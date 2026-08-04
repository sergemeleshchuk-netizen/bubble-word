/**
 * Зрячий бот: проверка проходимости уровня по правилам прототипа.
 *
 * Зачем. Слепой AI-решатель отвечает «однозначен ли уровень семантически»,
 * счётчик решений — «одна ли у него раскладка». Ни тот, ни другой не видят
 * ДИНАМИКУ: выкладку, ритм досыпки и лимит ходов. Инцидент 02.08: уровень 12
 * «как в оригинале» формально проходим, но после первого сбора игрок упёрся
 * в поле из одних недоборов с единственным неочевидным мерджем — и честно
 * решил, что уровень сломан. Такое состояние ловится только проигрыванием.
 *
 * Правила партии живут в `core/playSim.ts` — там же, откуда их берёт слепой
 * бот (`core/simulateBlindPlay.ts`). Здесь только МОЗГ: что тащить.
 *
 * Бот играет жадно и знает ответы: завершающий мердж, иначе склейка половинок,
 * иначе мердж в категории с максимумом слов на поле. Неверных догадок у него не
 * бывает по построению. На число ходов до победы порядок мерджей не влияет
 * (каждый мердж уменьшает число кусков ровно на 1), поэтому вердикт «хватит ли
 * лимита ИДЕАЛЬНОМУ игроку» точный. А вот метрики ритма — досыпки вне ритма,
 * «тупики на глаз», серия ходов без сбора — считаются для этого разумного
 * игрока и служат меркой UX, а не абсолютной истиной.
 *
 * Чего этот бот не меряет принципиально: цену незнания слов. Его «запас ходов»
 * (`spareMoves`) и есть весь бюджет ошибок живого игрока — сколько промахов
 * уровень прощает. Тратит этот бюджет слепой бот, и меряет его он же.
 */
import type { LevelSpec } from './types.ts';
import { createPlaySim, hasDeal } from './playSim.ts';

export interface PlayabilityResult {
  /** уровень доигрывается до конца и укладывается в лимит ходов */
  winnable: boolean;
  /** человекочитаемая причина провала; null, если уровень проходим */
  failReason: string | null;
  /** ходов потребовалось разумному игроку (равно минимуму: мерджи не тратятся зря) */
  movesNeeded: number;
  /** лимит уровня; null — туториал без лимита */
  moveLimit: number | null;
  /** запас: лимит − нужно; null при безлимите */
  spareMoves: number | null;
  /** досыпок «вне ритма» — поле вставало без единого мерджа при живой очереди */
  rescues: number;
  /** раз досыпка вскрыла закрытый гейт: открытых линий в очереди не осталось */
  gatesForced: number;
  /** состояний «выглядит тупиком»: собрать нечего и легальных мерджей ≤ 1 */
  perceivedDead: number;
  /** самая длинная серия ходов без единого сбора категории */
  maxDrought: number;
  /** волн досыпки за партию (пачка после сбора, склейки или страховки) */
  refillWaves: number;
  /**
   * Волн, которые СРАЗУ открыли сбор: после пачки на поле появилась категория,
   * собираемая целиком. Это мера того, ведёт ли уровень игрока за руку: пачка
   * либо приносит развязку, либо только добавляет обрывков.
   */
  refillCompletions: number;
  /** цепь пришлось снять страховкой, а не сбором категорий */
  chainRescued: boolean;
  /** лёд/«?» пришлось снять страховкой, а не мерджами */
  blockersRescued: boolean;
}

export function simulatePlayability(spec: LevelSpec): PlayabilityResult {
  /*
   * Спек без выкладки симулировать нельзя, и врать «проходим» тут нельзя тоже:
   * такие спеки приезжают из пакетов до gen-1.1, и тихий зелёный вердикт на
   * них означал бы, что гейт приёмки пропускает непроверенное. Кто оценивает
   * уровень (`core/dealShape.ts`), сюда с таким спеком просто не приходит.
   */
  if (!hasDeal(spec)) {
    return {
      winnable: false, failReason: 'выкладки нет: симулировать нечего',
      movesNeeded: 0, moveLimit: spec.board.moveLimit, spareMoves: null,
      rescues: 0, gatesForced: 0, perceivedDead: 0, maxDrought: 0,
      refillWaves: 0, refillCompletions: 0,
      chainRescued: false, blockersRescued: false,
    };
  }

  const sim = createPlaySim(spec);
  let perceivedDead = 0;

  const result = (winnable: boolean, failReason: string | null): PlayabilityResult => {
    const s = sim.stats();
    const limit = spec.board.moveLimit;
    return {
      winnable,
      failReason,
      movesNeeded: sim.moves(),
      moveLimit: limit,
      spareMoves: limit === null ? null : limit - sim.moves(),
      rescues: s.rescues,
      gatesForced: s.gatesForced,
      perceivedDead,
      maxDrought: s.maxDrought,
      refillWaves: s.refillWaves,
      refillCompletions: s.refillCompletions,
      chainRescued: s.chainRescued,
      blockersRescued: s.blockersRescued,
    };
  };

  // страховочный предел: ходов у любого уровня меньше тысячи на порядки
  let guard = 20000;
  while (!sim.won() && guard > 0) {
    guard -= 1;
    const pairs = sim.legalPairs();

    if (pairs.length === 0) {
      if (sim.rescue() !== null) continue;
      return result(false, 'жёсткий тупик: мерджей нет и очередь пуста');
    }

    const field = sim.field;
    // «выглядит тупиком»: собрать нечего, ходить почти некуда
    const completing = pairs.filter(([i, j]) => field[i].halfPair === 0
      && field[i].words.length + field[j].words.length === sim.fullOf(field[i].category));
    if (completing.length === 0 && pairs.length <= 1) perceivedDead += 1;

    let pick: [number, number];
    if (completing.length > 0) {
      pick = completing[0];
    } else {
      const halfMerge = pairs.find(([i]) => field[i].halfPair !== 0);
      if (halfMerge) {
        pick = halfMerge;
      } else {
        // категория, у которой на поле больше всего слов, ближе всех к сбору
        const onField = new Map<string, number>();
        for (const b of field) {
          if (b.halfPair === 0) {
            onField.set(b.category, (onField.get(b.category) ?? 0) + b.words.length);
          }
        }
        pick = pairs.reduce((best, p) =>
          ((onField.get(field[p[0]].category) ?? 0)
            > (onField.get(field[best[0]].category) ?? 0) ? p : best), pairs[0]);
      }
    }

    sim.attempt(pick[0], pick[1]);
  }

  if (guard <= 0) return result(false, 'симуляция не сошлась: защитный предел исчерпан');

  const limit = spec.board.moveLimit;
  if (limit !== null && sim.moves() > limit) {
    return result(false, `не хватает лимита ходов: нужно ${sim.moves()}, лимит ${limit}`);
  }
  return result(true, null);
}
