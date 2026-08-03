/**
 * Слепой бот: партия глазами игрока, который читает слова, а не ответы.
 *
 * Место в проверках. Зрячий бот (`simulatePlayability.ts`) отвечает «уложится ли
 * в лимит ИДЕАЛЬНЫЙ игрок» и остаётся hard-гейтом приёмки. Этот отвечает на
 * другой вопрос — «во что уровень обойдётся живому», — и отвечает в той же
 * валюте, в которой игра берёт плату: в ходах. Неверная догадка стоит ход
 * (прототип: `canMerge` → `moves--`), значит незнание слов измеримо, и мерить
 * его надо здесь, а не константой `K` на весь уровень.
 *
 * Как играет бот.
 *
 *   1. Читаемость. Перед партией каждое слово уровня получает бросок «прочитал
 *      или нет» с вероятностью `wordClarity` (`core/playerKnowledge.ts`). Бросок
 *      СТАБИЛЕН за прогон — берётся из `rng.stableWeight(слово)`, а не из потока.
 *      Иначе бот перебрасывал бы кубик каждый ход и в конце концов «прочитывал»
 *      бы любое слово, а память о неудачных попытках теряла бы смысл.
 *   2. Видимые ходы. Пара законна И оба её конца читаемы → игрок этот мердж
 *      ВИДИТ. Выбор среди видимых — тот же жадный порядок, что у зрячего бота:
 *      завершающий мердж, склейка половинок, крупнейшая категория.
 *   3. Кластер из двух и более слов читаем всегда: игрок своими руками убедился,
 *      что эти слова лежат вместе. Так в модель попадает эффект «три слова
 *      категории на поле подсказывают четвёртое» — не отдельным правилом с
 *      подобранным порогом, а следствием.
 *   4. Догадка. Видимых ходов нет → игрок тащит нечитаемое слово на самую
 *      правдоподобную цель. Промах: −1 ход, и цель попадает в память «с этими
 *      словами оно не лежит». Память и даёт исключение: перебрав всё кроме
 *      одного, игрок приходит к верному ответу — дорого, но приходит.
 *   5. MISS_RESCUE промахов подряд → досыпка-подсказка, как в прототипе.
 *
 * Порядок целей для догадки — единственное место, где бот подсматривает правду:
 * слово-ловушка тащится сначала к своей ПРИМАНКЕ, а не к дому, и слова одной
 * темы выглядят родственными. Подсматривание работает ПРОТИВ бота — оно ведёт
 * его к промаху, — поэтому оценка остаётся осторожной, а не приукрашенной.
 *
 * Что модель НЕ ловит, и это надо знать, читая её числа:
 *   - ёмкость поля не моделируется (упрощение движка): бот видит все досыпанные
 *     слова сразу, значит гипотез у него больше, чем у живого игрока;
 *   - память бота идеальная: он не пробует дважды то, что уже не сработало;
 *   - слово-ловушку, которая ВЫПАЛА читаемой, бот раскладывает верно и цены
 *     ловушки не платит.
 * Первые два делают оценку оптимистичной, третий — тоже. Поэтому её честное
 * прочтение: «дешевле этого уровень живому игроку не обойдётся».
 *
 * Числа модели не откалиброваны (см. шапку `playerKnowledge.ts`), поэтому
 * результат живёт метрикой в карточке уровня и НЕ входит ни в D, ни в гейт.
 */
import type { LevelSpec } from './types.ts';
import { createPlaySim, hasDeal, MISS_RESCUE, type PlaySim, type SimBubble } from './playSim.ts';
import {
  DEFAULT_KNOWLEDGE, KNOWLEDGE_MODEL_VERSION, levelClarity, wordProfiles,
  type KnowledgeModel, type WordProfile,
} from './playerKnowledge.ts';
import { createRng } from './rng.ts';
import type { ContentIndex } from './snapshot.ts';

export const BLIND_PLAY_VERSION = 'blind-play-0.1';

/** Итог одного прогона: одна выборка «какие слова этому игроку знакомы». */
export interface BlindRun {
  /** уровень доигран до конца (не путать с «уложился в лимит») */
  finished: boolean;
  /** партия встала наглухо: ни видимого хода, ни догадки, ни страховок */
  hardStall: boolean;
  /** ходов всего: успешные мерджи плюс промахи */
  moves: number;
  /** промахов — ходов, отданных за неверную догадку */
  misses: number;
  /** ходов, начатых при пустом поле видимых мерджей: игрок был вынужден гадать */
  guessTurns: number;
  /** догадок сделано — попыток мерджа, о котором игрок не знал, верен ли он */
  probes: number;
  /** досыпок-подсказок после серии промахов подряд */
  hintRefills: number;
  /** слов стартового поля, которые игрок прочитал */
  startReadable: number;
  /** слов на стартовом поле всего */
  startFieldSize: number;
  /** категорий, представленных на старте, но без ни одного читаемого слова */
  anchorlessCategories: number;
}

export interface BlindPlayResult {
  /** прогонов сделано: каждый — своя выборка знакомых слов */
  seeds: number;
  modelVersion: string;
  knowledgeVersion: string;
  /** null — уровень нельзя проиграть (нет выкладки); остальные поля тогда нулевые */
  unavailable: string | null;

  /** минимум ходов: столько нужно зрячему боту, ошибок в нём нет по построению */
  movesFloor: number;
  /** лимит уровня; null — туториал без лимита */
  moveLimit: number | null;

  /** ходов у слепого игрока: медиана и p90 по прогонам */
  movesMedian: number;
  movesP90: number;
  /** промахов: медиана и p90 */
  missesMedian: number;
  missesP90: number;

  /** доля прогонов, уложившихся в лимит ходов; 1 при безлимите */
  winRate: number;
  /**
   * Сколько бюджета ошибок съедает незнание слов: промахи p90, делённые на
   * запас зрячего бота (лимит − минимум). 1.0 — уровень выедает весь запас,
   * который ему дала константа K; больше 1.0 — не уложится. null при безлимите.
   */
  errorBudgetUsed: number | null;

  /** ходов, начатых без единого видимого мерджа: медиана */
  guessTurnsMedian: number;
  /** догадок за партию: медиана */
  probesMedian: number;
  /**
   * Доля верных догадок 0..1 — насколько модель «угадывания» на самом деле
   * угадывает. Число служит проверкой самой модели: если оно близко к единице,
   * значит порядок целей подсматривает ответ, и цена незнания занижена.
   */
  probeHitRate: number;
  /** досыпок-подсказок: медиана */
  hintRefillsMedian: number;
  /** прогонов, где партия встала наглухо */
  hardStalls: number;

  /** средняя ясность слов уровня 0..1 — до всяких бросков */
  clarity: number;
  /**
   * Сила связей взята из спека, а не из снимка: на словаре оригинала это
   * занижает ясность (см. `linkStrength` в playerKnowledge.ts). Признак нужен
   * в отчёте, иначе заниженные числа не отличить от трудного уровня.
   */
  signalFromSpec: boolean;
  /** доля стартового поля, которую игрок читает: медиана по прогонам */
  startReadableShare: number;
  /** категорий на старте без ни одной опоры: медиана по прогонам */
  anchorlessCategories: number;

  /** человекочитаемый разбор для карточки уровня */
  notes: string[];
}

const GUARD = 20000;
const DEFAULT_SEEDS = 12;

export interface BlindPlayOptions {
  /** прогонов; каждый — своя выборка знакомых слов */
  seeds?: number;
  /** базовый seed: прогоны идут как `${seed}#0`, `${seed}#1`, … */
  seed?: string;
  model?: KnowledgeModel;
  /**
   * Индекс снимка: без него сила связи берётся из спека, а там она сырая — на
   * словаре оригинала это занижает ясность (см. `linkStrength`). Передавать
   * стоит всегда, когда снимок под рукой.
   */
  index?: ContentIndex;
}

/** Медиана по возрастанию; для чётной длины — нижний из двух средних. */
function median(values: number[]): number {
  if (values.length === 0) return 0;
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.floor((sorted.length - 1) / 2)];
}

/** Перцентиль по ближайшему рангу: на выборке из 12 прогонов иначе врать. */
function percentile(values: number[], p: number): number {
  if (values.length === 0) return 0;
  const sorted = [...values].sort((a, b) => a - b);
  const rank = Math.min(sorted.length - 1, Math.ceil(p * sorted.length) - 1);
  return sorted[Math.max(0, rank)];
}

/** Ключ памяти «эти два слова вместе не лежат»: пара неупорядоченная. */
function pairKey(a: string, b: string): string {
  return a < b ? `${a} ${b}` : `${b} ${a}`;
}

/**
 * Один прогон. `readable` — выборка знакомых слов, уже сделанная снаружи:
 * бросок обязан быть стабилен за партию, поэтому он не внутри цикла.
 */
function playOnce(
  spec: LevelSpec,
  profiles: Map<string, WordProfile>,
  readable: Set<string>,
): BlindRun {
  const sim = createPlaySim(spec);

  const startFieldSize = sim.field.length;
  let startReadable = 0;
  const startCats = new Map<string, number>();
  for (const b of sim.field) {
    const word = b.words[0];
    if (readable.has(word)) startReadable += 1;
    startCats.set(b.category,
      (startCats.get(b.category) ?? 0) + (readable.has(word) ? 1 : 0));
  }
  let anchorlessCategories = 0;
  for (const anchors of startCats.values()) if (anchors === 0) anchorlessCategories += 1;

  /** Кластер читаем: игрок или знает слово, или своими руками собрал группу. */
  const clusterReadable = (b: SimBubble): boolean =>
    b.words.length > 1 || readable.has(b.words[0]);

  const ruledOut = new Set<string>();
  /** слово уже пробовали против всех слов этой группы и получили отказ */
  const isRuledOut = (a: SimBubble, b: SimBubble): boolean =>
    a.words.some((wa) => b.words.some((wb) => ruledOut.has(pairKey(wa, wb))));
  const remember = (a: SimBubble, b: SimBubble): void => {
    for (const wa of a.words) for (const wb of b.words) ruledOut.add(pairKey(wa, wb));
  };

  let misses = 0;
  let missStreak = 0;
  let guessTurns = 0;
  let probes = 0;
  let hintRefills = 0;
  let hardStall = false;

  let guard = GUARD;
  while (!sim.won() && guard > 0) {
    guard -= 1;
    const field = sim.field;
    const legal = sim.legalPairs();

    /*
     * Видимые ходы. Половинки видны всегда: игрок сопоставляет обрывки слова по
     * буквам, и словарный запас тут ни при чём (сторону склейки прототип не
     * подсказывает с c00b2d2, но обрывки остаются обрывками).
     */
    const seen = legal.filter(([i, j]) => field[i].halfPair !== 0
      || (clusterReadable(field[i]) && clusterReadable(field[j])));

    if (seen.length > 0) {
      const completing = seen.filter(([i, j]) => field[i].halfPair === 0
        && field[i].words.length + field[j].words.length === sim.fullOf(field[i].category));
      let pick: [number, number];
      if (completing.length > 0) {
        pick = completing[0];
      } else {
        const halfMerge = seen.find(([i]) => field[i].halfPair !== 0);
        if (halfMerge) {
          pick = halfMerge;
        } else {
          const onField = new Map<string, number>();
          for (const b of field) {
            if (b.halfPair === 0) {
              onField.set(b.category, (onField.get(b.category) ?? 0) + b.words.length);
            }
          }
          pick = seen.reduce((best, p) =>
            ((onField.get(field[p[0]].category) ?? 0)
              > (onField.get(field[best[0]].category) ?? 0) ? p : best), seen[0]);
        }
      }
      sim.attempt(pick[0], pick[1]);
      missStreak = 0;
      continue;
    }

    // видимых ходов нет: дальше только догадка
    guessTurns += 1;
    const probe = chooseProbe(sim, profiles, readable, isRuledOut);
    if (probe) {
      probes += 1;
      const [i, j] = probe;
      const a = field[i];
      const b = field[j];
      const outcome = sim.attempt(i, j);
      if (outcome.ok) {
        missStreak = 0;
      } else if (outcome.why === 'wrong') {
        remember(a, b);
        misses += 1;
        missStreak += 1;
        if (missStreak >= MISS_RESCUE) {
          missStreak = 0;
          if (sim.hintRefill()) hintRefills += 1;
        }
      }
      // преграда (лёд, «?», цепь) хода не стоит и в память не пишется:
      // растает — попробуем снова
      continue;
    }

    // ни видимого хода, ни догадки: остаются страховки движка
    if (sim.rescue() !== null) continue;
    hardStall = true;
    break;
  }

  return {
    finished: sim.won(),
    hardStall: hardStall || guard <= 0,
    moves: sim.moves(),
    misses,
    guessTurns,
    probes,
    hintRefills,
    startReadable,
    startFieldSize,
    anchorlessCategories,
  };
}

/**
 * Куда игрок потащит нечитаемое слово.
 *
 * Порядок предпочтений: сначала приманка заявленной ловушки (за ней слово и
 * тянет — в этом весь смысл ловушки), потом группа со словами той же темы (слова
 * одной сферы выглядят родственными, даже если категории разные), потом просто
 * самая большая группа: чем она больше, тем больше информации даст и успех, и
 * отказ. Внутри равных — по номеру пузыря, чтобы прогон был воспроизводим.
 */
function chooseProbe(
  sim: PlaySim,
  profiles: Map<string, WordProfile>,
  readable: Set<string>,
  isRuledOut: (a: SimBubble, b: SimBubble) => boolean,
): [number, number] | null {
  const field = sim.field;
  let best: { score: number; pair: [number, number] } | null = null;

  for (let i = 0; i < field.length; i += 1) {
    const a = field[i];
    // тащим то, чего не понимаем: заблокированное не тащится вовсе (прототип
    // не даёт даже взять такой пузырь), склеенную группу игрок уже понял
    if (a.blocked > 0 || a.halfPair !== 0) continue;
    if (a.words.length > 1 || readable.has(a.words[0])) continue;
    const profile = profiles.get(a.words[0]);

    for (let j = 0; j < field.length; j += 1) {
      if (i === j) continue;
      const b = field[j];
      if (b.blocked > 0 || b.halfPair !== 0) continue;
      if (isRuledOut(a, b)) continue;
      /*
       * Преграду игрок ВИДИТ — цепь нарисована на поле, лёд и «?» нарисованы на
       * пузыре, — и в неё не тычет. Здесь это не подсматривание ответа, а
       * единственный способ не зациклиться: попытка через преграду хода не
       * стоит и в память не пишется, поэтому бот выбирал бы её вечно
       * (уровни 65 и 95 упирались в защитный предел именно так).
       *
       * А вот «сумма слов не поместится» игроку НЕ видна: он не знает
       * категорий. Такая попытка законно кончится промахом, и цену её он
       * заплатит — поэтому отсеиваем только `chain`/`blocked`, но не `wrong`.
       */
      const barrier = sim.verdict(i, j);
      if (!barrier.ok && barrier.why !== 'wrong') continue;

      let score = b.words.length;
      if (profile) {
        if (profile.decoy && b.category === profile.decoy) score += 100;
        else if (b.words.some((w) => profiles.get(w)?.theme === profile.theme)) score += 10;
      }
      if (!best || score > best.score) best = { score, pair: [i, j] };
    }
  }
  return best?.pair ?? null;
}

/**
 * Слепой прогон уровня: N выборок «какие слова знакомы этому игроку».
 *
 * Стохастичность здесь не от лени, а от предмета: игроки знают разные слова.
 * Воспроизводимость держится на seed — прогон при том же seed даёт те же числа,
 * и в отчёт идут медиана (типичный игрок) и p90 (тот, кому слова не даются).
 */
export function simulateBlindPlay(
  spec: LevelSpec,
  movesFloor: number,
  options: BlindPlayOptions = {},
): BlindPlayResult {
  const model = options.model ?? DEFAULT_KNOWLEDGE;
  const seeds = Math.max(1, options.seeds ?? DEFAULT_SEEDS);
  const baseSeed = options.seed ?? `blind-${spec.levelId}`;
  const limit = spec.board.moveLimit;

  const empty = (reason: string): BlindPlayResult => ({
    seeds: 0,
    modelVersion: BLIND_PLAY_VERSION,
    knowledgeVersion: KNOWLEDGE_MODEL_VERSION,
    unavailable: reason,
    movesFloor, moveLimit: limit,
    movesMedian: 0, movesP90: 0, missesMedian: 0, missesP90: 0,
    winRate: 0, errorBudgetUsed: null,
    guessTurnsMedian: 0, probesMedian: 0, probeHitRate: 0,
    hintRefillsMedian: 0, hardStalls: 0,
    clarity: 0, signalFromSpec: false,
    startReadableShare: 0, anchorlessCategories: 0,
    notes: [reason],
  });

  if (!hasDeal(spec)) return empty('выкладки нет: слепой прогон невозможен');

  const profiles = wordProfiles(spec, model, options.index);
  const runs: BlindRun[] = [];
  for (let s = 0; s < seeds; s += 1) {
    const rng = createRng(`${baseSeed}#${s}`);
    const readable = new Set<string>();
    for (const profile of profiles.values()) {
      if (rng.stableWeight(profile.word) < profile.clarity) readable.add(profile.word);
    }
    runs.push(playOnce(spec, profiles, readable));
  }

  const moves = runs.map((r) => r.moves);
  const misses = runs.map((r) => r.misses);
  const movesMedian = median(moves);
  const movesP90 = percentile(moves, 0.9);
  const missesMedian = median(misses);
  const missesP90 = percentile(misses, 0.9);
  const hardStalls = runs.filter((r) => r.hardStall).length;
  const totalProbes = runs.reduce((n, r) => n + r.probes, 0);
  const totalMisses = runs.reduce((n, r) => n + r.misses, 0);
  const won = runs.filter((r) => r.finished && (limit === null || r.moves <= limit));
  const spare = limit === null ? null : Math.max(0, limit - movesFloor);
  const startShare = median(runs.map((r) => (r.startFieldSize === 0 ? 1
    : Math.round((r.startReadable / r.startFieldSize) * 100)))) / 100;

  const clarity = levelClarity(profiles);
  const notes: string[] = [];
  notes.push(`средняя ясность слов ${clarity.toFixed(2)}: с такой вероятностью игрок `
    + 'читает слово на его месте (очевидность связи, приторможенная редкостью)');
  if (options.index === undefined) {
    notes.push('сила связей взята из спека, а не из снимка базы: на словаре '
      + 'оригинала это занижает ясность — числа читать как нижнюю границу');
  }
  notes.push(`минимум ходов ${movesFloor}`
    + (limit === null ? ', лимита нет' : `, лимит ${limit} — запас ${spare}`)
    + `; слепой игрок тратит ${movesMedian} (медиана) и ${movesP90} (p90)`);
  if (spare !== null) {
    const used = spare === 0 ? null : missesP90 / spare;
    notes.push(used === null
      ? 'запаса ходов нет вовсе: любая неверная догадка проваливает уровень'
      : `промахи съедают ${Math.round(used * 100)}% бюджета ошибок `
        + `(${missesP90} промахов p90 из запаса ${spare})`);
  }
  notes.push(`ходов вслепую ${median(runs.map((r) => r.guessTurns))}: столько раз поле `
    + 'не показывало игроку ни одного мерджа, который он понимает');
  notes.push(totalProbes === 0
    ? 'догадок не понадобилось: видимых ходов хватило на всю партию'
    : `догадок ${median(runs.map((r) => r.probes))} за партию, верных `
      + `${Math.round(((totalProbes - totalMisses) / totalProbes) * 100)}%: `
      + 'догадка опирается на размер уже собранной группы, поэтому попадает '
      + 'чаще случайной — но каждый промах стоит ход');
  const anchorless = median(runs.map((r) => r.anchorlessCategories));
  notes.push(anchorless === 0
    ? 'у каждой категории на старте есть опора — хотя бы одно читаемое слово'
    : `${anchorless} категорий лежат на старте без опоры: ни одного слова, `
      + 'которое игрок понимает, — зацепиться не за что');
  if (hardStalls > 0) {
    notes.push(`в ${hardStalls} из ${seeds} прогонов партия встала наглухо: `
      + 'это сбой модели или уровня, а не мера сложности — разбирать руками');
  }

  return {
    seeds,
    modelVersion: BLIND_PLAY_VERSION,
    knowledgeVersion: KNOWLEDGE_MODEL_VERSION,
    unavailable: null,
    movesFloor,
    moveLimit: limit,
    movesMedian,
    movesP90,
    missesMedian,
    missesP90,
    winRate: runs.length === 0 ? 0 : won.length / runs.length,
    errorBudgetUsed: spare === null || spare === 0 ? null : missesP90 / spare,
    guessTurnsMedian: median(runs.map((r) => r.guessTurns)),
    probesMedian: median(runs.map((r) => r.probes)),
    probeHitRate: totalProbes === 0 ? 0 : (totalProbes - totalMisses) / totalProbes,
    hintRefillsMedian: median(runs.map((r) => r.hintRefills)),
    hardStalls,
    clarity,
    signalFromSpec: options.index === undefined,
    startReadableShare: startShare,
    anchorlessCategories: anchorless,
    notes,
  };
}
