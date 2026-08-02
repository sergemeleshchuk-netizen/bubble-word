/**
 * Детерминированный генератор уровня и блока.
 *
 * Главное свойство: один и тот же снимок базы + конфиг + seed дают один и тот же
 * `level_spec_hash`. Модель здесь не участвует — она обогатила базу заранее.
 * Если поставить её в горячий путь, кривой сложности нельзя управлять,
 * а брак нельзя воспроизвести.
 *
 * Порядок шагов (план §9.3):
 *   1. пул категорий-кандидатов по фильтрам
 *   2. пары для мета-связей
 *   3. выбор набора категорий
 *   4. назначение по 4 слова — задача точного покрытия, MRV + откат
 *   5. мета-лес
 *   6. ловушки
 *   7. модификаторы
 *   8. первая выкладка: состав поля на старте и очередь досыпки (core/deal.ts)
 *   9. счёт решений, валидация, оценки
 *  10. упорядоченное ослабление, если не сошлось
 */
import type {
  BlockConfig, BlockedBubble,
  DecadeGates, Chain, GenerationAttempt, GenerationFailure, HalfSplit, LevelCategory,
  LevelPlan, LevelSpec, LevelWord, Trap,
} from './types.ts';
import { STATUS } from './types.ts';
import { ContentIndex } from './snapshot.ts';
import { createRng, type Rng } from './rng.ts';
import { buildDeal, chunkKey } from './deal.ts';
import { BOARD_CAPACITY, moveFloor, moveLimit, startBubbles } from './levelMath.ts';
import { BLOCKER_MOVE_BONUS, halfBudget, splitWord } from './playableModifiers.ts';

/**
 * gen-1.0 — исходный алгоритм сборки.
 * gen-1.1 — в уровень вошла первая выкладка (`spec.deal`): состав поля на старте
 *           и очередь досыпки считает генератор, а не клиент. Хеши уровней
 *           меняются, и обязаны: уровень с другой выкладкой — другой уровень.
 * gen-1.2 — очередь досыпки строится по ритму (каждая пачка открывает следующий
 *           сбор, см. deal.ts) и в уровень вошёл игровой модификатор: половинки,
 *           лёд, «?» или цепь-линия — с параметрами в спеке и в игровом JSON.
 */
export const GENERATOR_VERSION = 'gen-1.2';

/** Что уже использовано в пакете — для правил свежести. */
export interface PackHistory {
  /** нормализованное слово → последний уровень, где оно встречалось */
  wordLastLevel: Map<string, number>;
  /** ключ категории → последний уровень */
  categoryLastLevel: Map<string, number>;
  /** четвёрки слов референса, чтобы не выдать копию: ключ = отсортированные слова */
  referenceQuadruples?: Set<string>;
  /**
   * Нормализованное слово → ключ категории, где оно лежало в прошлый раз.
   * Нужно, чтобы отличить повтор слова в ТОЙ ЖЕ категории (это брак) от повтора
   * в ДРУГОЙ категории (это рычаг сложности: 2.9 слова на уровень в L1-10
   * против 28 в L171-180 референса).
   */
  wordCategory?: Map<string, string>;
}

export function emptyPackHistory(): PackHistory {
  return { wordLastLevel: new Map(), categoryLastLevel: new Map(), wordCategory: new Map() };
}

export interface LevelGenerationOutcome {
  spec?: LevelSpec;
  traps: Trap[];
  attempts: GenerationAttempt[];
  failure?: GenerationFailure;
  relaxationsUsed: string[];
}

/** Ослабления в порядке предпочтения. Hard-инварианты сюда не входят никогда. */
const RELAXATION_ORDER = [
  'точное число редких слов → диапазон',
  'тематическая узость → соседние сферы',
  'меньше ловушек',
  'меньше мета-связей',
  'меньше глубины мета',
  'другой набор категорий',
] as const;

type Relaxation = typeof RELAXATION_ORDER[number];

interface Constraints {
  categoryCount: number;
  /**
   * Гейты формы слова из профиля декады. Фильтруют пул НА ВХОДЕ, а не отбраковывают
   * готовый уровень: когда гейты стояли только в валидаторе, генератор 24 попытки
   * подряд собирал уровень из многословных и длинных слов и каждый раз получал
   * отказ WORD_FORM_GATE, хотя годные слова в базе были.
   */
  gates: DecadeGates | null;
  /** окна свежести из конфига, а не захардкоженные числа */
  wordWindow: number;
  categoryWindow: number;
  metaCount: number;
  metaDepthTarget: number;
  rareTarget: number;
  rareTolerance: number;
  trapTarget: number;
  themesAllowed: Set<string> | null;
  themesExcluded: Set<string>;
  enforceFreshness: boolean;
}

// --------------------------------------------------------------------------- //
// вспомогательное
// --------------------------------------------------------------------------- //

/**
 * Слова-двойники внутри одной категории: `star` и `stars`, `bird` и `birds`.
 * Формально это разные слова, но на поле рядом они читаются как ошибка данных.
 */
function isNearDuplicate(a: string, b: string): boolean {
  if (a === b) return true;
  const [short, long] = a.length <= b.length ? [a, b] : [b, a];
  if (long === `${short}s` || long === `${short}es`) return true;
  if (short.endsWith('y') && long === `${short.slice(0, -1)}ies`) return true;
  return false;
}

function quadrupleKey(words: string[]): string {
  return words.map((w) => w.toLowerCase()).sort().join('|');
}

// --------------------------------------------------------------------------- //
// шаг 1: пул категорий
// --------------------------------------------------------------------------- //

interface PoolEntry {
  category: number;
  key: string;
  theme: string;
  approved: number[];
  /** сколько approved-слов частотные — потенциал quick-win */
  frequentCount: number;
  /** сколько approved-слов редкие — потенциал редкости */
  rareCount: number;
  canQuickwin: boolean;
  /** базовая сложность категории из базы; null, если поле не заполнено */
  difficulty: number | null;
  /**
   * Узнаваемость категории: медиана частотности четырёх самых частотных годных
   * слов, то есть «насколько понятной эта категория может быть, если брать из неё
   * лучшее». Нужна для отбора категорий под целевую медиану декады: в базе
   * 230 категорий способны дать медиану 4.35+, но без этого поля генератор
   * выбирал их не чаще любых других и блок 1-10 упирался в медиану 3.81.
   */
  recognizability: number;
}

/**
 * Порог, ниже которого слово считается редким — рычагом сложности.
 *
 * Абсолютное значение 3.0 было верным, пока пола частотности не существовало.
 * С полом (`minWordZipf` = 3.75) оно стало невыполнимым требованием: ни одно
 * допущенное слово не бывает ниже 3.0, а таблица декад требует у декады 11
 * от двух до пяти редких слов. Генератор честно сжигал 48 попыток и терял
 * уровень — «редких наберём» и «редких не пускаем» противоречили друг другу.
 *
 * Поэтому редкость становится ОТНОСИТЕЛЬНОЙ: редкое слово — самое редкое из
 * разрешённых, то есть попадающее в полосу шириной RARE_BAND над полом. Так и
 * пол соблюдён, и калибровка декад по референсу сохраняет смысл — уровень
 * по-прежнему опирается на менее частотный край словаря, просто край стал выше.
 *
 * Ширина полосы взята замером, а не на глаз. Первая попытка (0.35) дала полосу
 * 3.75-4.10, а это 33% всех разрешённых слов: уровень из 48 слов набирал 15.7
 * редких при цели 2-5, и генератор снова терял уровни — теперь на перевыполнении.
 * Доля слов в полосе над полом 3.75 (всего разрешённых 4410):
 *
 *   +0.05 -> 198 слов (4.5%),  на уровне 48 слов  2.2
 *   +0.10 -> 411 слов (9.3%),  на уровне          4.5   <- цель декад 2-5
 *   +0.20 -> 837 слов (19%),   на уровне          9.1
 *   +0.35 -> 1441 слово (33%), на уровне         15.7
 *
 * Отсюда 0.10: редкость снова редкость, а не низ разрешённого диапазона.
 */
const RARE_BAND = 0.10;
const RARE_ZIPF_ABSOLUTE = 3.0;

export function rareZipfCeiling(gates: DecadeGates | null): number {
  if (!gates || !gates.minWordZipf) return RARE_ZIPF_ABSOLUTE;
  return gates.minWordZipf + RARE_BAND;
}

/**
 * Пол частотности для МЕТА-слова — ниже общего, и это не поблажка.
 *
 * Мета-слово это имя категории, которую игрок собрал сам минуту назад: четвёрка
 * strawberry / blueberry / raspberry / cranberry превращается в пузырь `berries`,
 * и чтобы его прочитать, держать слово в активном словаре не нужно — значение
 * установлено ходом игры, а не словарём. Общий пол в этом месте вреден: он
 * срезал 41% мета-рёбер (151 из 258), и срезал такие слова, как `aquarium` 3.56,
 * `courtroom` 3.58, `berries` 3.57, `desserts` 3.31, `crafts` 3.73. Декада 11
 * из-за этого приходила к концу с нулём мета-пар на двух уровнях и падала
 * приёмкой META_RANGE.
 *
 * Пол 3.0 оставляет 229 рёбер из 258 (89%), а отсекает именно тёмное:
 * `biomes` 2.33, `scrapbooking` 2.41, `beekeeper` 2.54, `crustaceans` 2.78,
 * `houseplants` 2.15. То есть граница проходит там, где мета-слово перестаёт
 * читаться даже после сборки четвёрки.
 */
const META_WORD_ZIPF = 3.0;

/**
 * Вес очевидности связи при отборе слов в четвёрку.
 *
 * Зачем понадобилось. До этого отбор внутри категории решался частотностью
 * слова и ничем больше: поле `obviousness` в снимке было, но читали его только
 * описание ловушек и оценка интереса. Результат разбирали на живом уровне —
 * в SCHOOL SUBJECTS формула поставила chemistry / physics / economics / gym
 * (ранги 1, 2, 4, 5 по близости к медиане декады), а math, history, science,
 * English оказались внизу списка ЗА ТО, ЧТО СЛИШКОМ ЧАСТОТНЫЕ. Слово gym попало
 * на поле не потому, что база сочла «физкультуру» очевидным школьным предметом,
 * а потому, что его zipf 4.43 оказался в 0.08 от целевой медианы 4.35.
 *
 * Вес 0.9 — тот же, что у оси узнаваемости. Это заявление о равноправии двух
 * осей: при равной очевидности решает частотность, при равной частотности —
 * очевидность. Больший вес давать нельзя, пока база не заполнена: 74% категорий
 * залиты одним значением на весь пул (измерено по снимку b9c962), и на них
 * слагаемое всё равно вырождается в константу.
 */
const OBVIOUSNESS_WEIGHT = 0.9;

/**
 * Чем считать очевидность, если связи в индексе не нашлось.
 *
 * Медиана поля по approved-связям — 0.78 (по всем связям 0.75). Отбор смотрит
 * только на approved, поэтому берётся 0.78. Ставить 0 значило бы отправлять
 * такое слово в самый конец очереди, то есть наказывать за пробел в данных;
 * ставить 1 — наоборот, выдавать пробел за уверенность. Медиана не делает ни
 * того, ни другого. В оценке интереса (`scoringInterest.ts`) на этом же месте
 * стоит 0.7 — расхождение оставлено намеренно: это разные решения, свести их
 * в одну константу можно только замером, а замера пока нет.
 */
const OBVIOUSNESS_UNKNOWN = 0.78;

/**
 * Ширина шкалы узнаваемости при отборе слова — вниз и вверх от целевой медианы.
 *
 * Что было. Слово оценивалось по БЛИЗОСТИ к целевой медиане декады:
 * `0.9 * (1 - |z - target| / 1.5)`, штраф симметричный. Медиана — свойство
 * распределения уровня, а применялась как идеал к каждому отдельному слову.
 * Последствие: самые расхожие слова категории проигрывают ЗА ТО, ЧТО СЛИШКОМ
 * ЧАСТОТНЫЕ. В SCHOOL SUBJECTS декады 1-10 (цель 4.35) отбор выстроил
 * chemistry 4.35, physics 4.39, economics 4.42, gym 4.43 — и отправил вниз
 * списка math 4.45, science 5.12, English 5.19, history 5.39, music 5.52.
 * На поле поехал `gym`.
 *
 * Почему нельзя было просто убрать верхнюю сторону штрафа. Замер: чисто
 * монотонная шкала «чем узнаваемее, тем лучше» поднимает медиану блока до
 * 4.5-4.6 и выносит ZIPF_BLOCK_MEDIAN на всех 20 декадах. Это арифметика, а
 * не настройка: пол частотности 3.75 уже срезал нижний хвост распределения,
 * и держать референсную медиану приходится верхом. Референс держит её
 * РАЗБРОСОМ — часть слов 5.4, часть 3.3; запретив низ, мы вынудили генератор
 * срезать верх. По-настоящему это лечится либо порогом, либо переносом
 * контроля над распределением в квоты (как уже сделано для редких слов), но
 * и то и другое — решение не генератора.
 *
 * Что сделано. Штраф стал АСИММЕТРИЧНЫМ: вниз от медианы прежняя ширина 1.5,
 * вверх — 2.1. Число выбрано перебором по всем 20 декадам как наибольшее,
 * которое не добавляет ни одного отказа приёмки:
 *
 *   вверх 1.5 (как было): мимо медианы 5 декад, худший перебор допуска 168%
 *   вверх 1.8:            мимо 5, 169%
 *   вверх 2.1:            мимо 5, 173%   <- взято
 *   вверх 2.5:            мимо 6, 174%   (добавляется декада 171-180)
 *   вверх 3.0:            мимо 7, 184%   (добавляются 41-50 и 171-180)
 *
 * Цена — 5 пунктов допуска, выигрыш — состав четвёрки меняется у 484 категорий
 * из 1718 (28%): `rack` → `chair` в FURNITURE, `mint` → `chocolate` в CANDY,
 * `Stanley Cup` → `NBA` в SPORTS LEAGUES, `dawn` → `Tuesday` в DAYS AND PARTS
 * OF DAY. Плюс собирается больше уровней: пул перестал упираться в узкую
 * полосу вокруг медианы.
 *
 * Пять декад, что мимо медианы (31, 121, 151, 161, 181), были мимо и до
 * правки: их цели 3.70-3.85 лежат ниже того, что пул над полом 3.75 даёт
 * выжать. Это отдельный долг, здесь он не чинится и не усугубляется.
 */
/**
 * Вес предпочтения коротких слов и штраф за многословный пузырь.
 *
 * Зачем. Отбор слова знал две оси — частотность и очевидность — и ни одна
 * не видит длины. Замер уровня 12: медиана частотности в цель попала, а
 * средняя длина 6.7 буквы против 6.2 у оригинала и 22% слов длиннее восьми
 * против 12%. На поле это `silverware`, `ointment`, `neapolitan` рядом с
 * `egg salad` — «сложные слова», которые формально проходят все пороги.
 *
 * Многословный пузырь штрафуется отдельно и сильнее: у оригинала таких 3.1%
 * на декаде 11-20 и 0.3% на 1-10, у нас на уровне 12 их было 12%. Это не
 * слово, а подпись; четвёрка `egg salad / fruit salad / pasta salad /
 * chef salad` — вообще список ярлыков, а не задача.
 *
 * Веса подобраны так, чтобы не перебить ось узнаваемости (0.9): длина —
 * тай-брейкер при близкой частотности, а не новый главный фильтр.
 */
const LENGTH_WEIGHT = 0.45;
const MULTIWORD_PENALTY = 0.5;
/** За сколько букв сверх цели предпочтение обнуляется. */
const LENGTH_SPAN = 5;

const RECOGNITION_SPAN_BELOW = 1.5;
const RECOGNITION_SPAN_ABOVE = 2.1;

function recognitionScore(z: number, gates: DecadeGates): number {
  const target = gates.zipfMedianTarget;
  const penalty = z >= target
    ? (z - target) / RECOGNITION_SPAN_ABOVE
    : (target - z) / RECOGNITION_SPAN_BELOW;
  return Math.max(0, 1 - penalty);
}

function metaGates(gates: DecadeGates | null): DecadeGates | null {
  if (!gates || gates.minWordZipf <= META_WORD_ZIPF) return gates;
  return { ...gates, minWordZipf: META_WORD_ZIPF };
}

/**
 * Слово проходит форму декады: число токенов, длина, порог для имён собственных
 * и пол частотности. Без гейтов пропускает всё — так ведёт себя пресет 201-210.
 */
export function wordFitsGates(index: ContentIndex, word: number, gates: DecadeGates | null): boolean {
  if (!gates) return true;
  const w = index.words[word];
  if (w.tok > gates.maxTokens) return false;
  if (w.t.replace(/\s/g, '').length > gates.maxWordLen) return false;
  if (w.p === 1 && (w.z === null || w.z < gates.minProperNounZipf)) return false;
  /**
   * Пол частотности — см. `minWordZipf` в DecadeGates.
   *
   * Слово без посчитанной частотности (`z === null`, таких в базе 28) пол не
   * проходит: пропускать его значило бы вернуть ту же дырку, из-за которой
   * редкие слова оказывались на поле незамеченными. Пусть лучше 28 слов не
   * попадут в уровень, чем пол окажется необязательным.
   */
  if (gates.minWordZipf > 0 && (w.z === null || w.z < gates.minWordZipf)) return false;
  /**
   * Регистр слова — главный фильтр словаря, см. `maxWordRegister` в DecadeGates.
   * Неразмеченное слово (`e == null`) проходит: снимок, собранный до шага 010,
   * обязан остаться генерируемым.
   */
  if (w.e !== undefined && w.e !== null && w.e > gates.maxWordRegister) return false;
  /**
   * Вес слова — тот же фильтр для базы, где разметки регистра нет вовсе
   * (сводная база, см. `minWordWeight` в DecadeGates). Снимок без весов гейт
   * не замечает: `w` там undefined, и поведение остаётся прежним до знака.
   *
   * Два фильтра рядом не спорят, а страхуют друг друга: у размеченного слова
   * вес ВЫВЕДЕН из регистра, поэтому оба говорят одно и то же; у слова из
   * чужого словаря регистра нет, и решает только вес.
   */
  const weight = w.w;
  if (weight !== undefined && gates.minWordWeight > 0 && weight < gates.minWordWeight) {
    return false;
  }
  return true;
}

/**
 * Категория проходит по базовой сложности — жёстко только на туториале.
 *
 * Сложность самой группы живёт в базе (`base_difficulty`), и генератор её не
 * спрашивал вовсе: на уровень 1 приезжали UNIVERSITIES и LOCKSMITH WORDS при
 * наличии COLORS, WEATHER WORDS и SCHOOL SUPPLIES. На туториале это запрет,
 * на остальных уровнях — предпочтение при отборе (см. simpleBonus ниже):
 * жёсткий фильтр на всю декаду сужал пул так, что к концу декады кончались
 * мета-пары. Категории без `d` пропускаем: иначе снимок с незаполненным полем
 * перестал бы генерироваться.
 */
export function categoryFitsGates(
  index: ContentIndex, category: number, gates: DecadeGates | null, isTutorial: boolean,
): boolean {
  if (!gates || !isTutorial) return true;
  const difficulty = index.categories[category].d;
  if (difficulty === null) return true;
  return difficulty <= gates.tutorialCategoryDifficultyMax + 1e-9;
}

function buildPool(
  index: ContentIndex, plan: LevelPlan, c: Constraints, history: PackHistory,
  excluded?: Set<number>,
): PoolEntry[] {
  const pool: PoolEntry[] = [];
  for (let cat = 0; cat < index.categories.length; cat += 1) {
    const meta = index.categories[cat];
    if (excluded?.has(cat)) continue;
    // Готовность категории решает база (derive-readiness), а не генератор:
    // curated_only — парное правило вроде OPPOSITES, четвёрка собирается руками;
    // hard_only и blocked — нормальной четвёрки нет вообще.
    if (!index.isAutoUsable(cat)) continue;
    if (!categoryFitsGates(index, cat, c.gates, plan.role === 'tutorial')) continue;
    if (c.themesExcluded.has(meta.th)) continue;
    if (c.themesAllowed && !c.themesAllowed.has(meta.th)) continue;

    if (c.enforceFreshness) {
      const last = history.categoryLastLevel.get(meta.k);
      if (last !== undefined && plan.levelId - last <= c.categoryWindow) continue;
    }

    const approved = index.categoryMemberships(cat, STATUS.approved)
      .map((m) => m.word)
      .filter((w) => wordFitsGates(index, w, c.gates));
    /**
     * Минимум — четыре слова, то есть ровно четвёрка.
     *
     * Урок на будущее, если вернёмся к импорту чужого словаря. Назначение слов —
     * задача точного покрытия: каждое из четырёх слов обязано иметь ровно один
     * дом среди категорий уровня. Категория ровно с четырьмя играбельными
     * словами проваливает её при первом пересечении, и на импортированной базе
     * (медиана размера пула 4 слова) уровень на 17 категорий не собирался
     * 48 попыток из 48. Тогда я поставил порог 5-6 слов — и на родной базе
     * (медиана пула 14) это отсекло мета-детей с тонкими пулами: три декады
     * из двадцати перестали проходить META_RANGE. Мета-материала всего
     * 120 категорий, и запрет на дефицитном ресурсе дороже пользы.
     *
     * Правильное место для этого требования — не генератор, а база: пул
     * категории должен быть 6-8 слов, и это условие приёмки контента.
     */
    if (approved.length < 4) continue;

    const frequentCount = approved.filter((w) => index.isQuickwinWord(w)).length;
    const rareCeiling = rareZipfCeiling(c.gates);
    const rareCount = approved.filter((w) => {
      const z = index.zipf(w);
      return z !== null && z < rareCeiling;
    }).length;

    const top4 = approved
      .map((w) => index.zipf(w))
      .filter((z): z is number => z !== null)
      .sort((a, b) => b - a)
      .slice(0, 4);
    const recognizability = top4.length === 4 ? (top4[1] + top4[2]) / 2 : 0;

    pool.push({
      category: cat,
      key: meta.k,
      theme: meta.th,
      difficulty: meta.d,
      approved,
      frequentCount,
      rareCount,
      canQuickwin: frequentCount >= 4,
      recognizability,
    });
  }
  return pool;
}

// --------------------------------------------------------------------------- //
// шаг 2-3: мета-цепочки и выбор категорий
// --------------------------------------------------------------------------- //

export interface MetaEdge {
  child: number;
  parent: number;
  /** слово-имя ребёнка, которое ляжет в родителя */
  word: number;
}

/**
 * Строит мета-лес нужной глубины из доступных пар.
 *
 * Инварианты: у ребёнка максимум один родитель, циклов нет, связность НЕ требуется
 * (в референсе мета-граф — лес из в среднем 2.12 компонент, SPEC_AUDIT §2).
 */
/** Все возможные мета-рёбра внутри набора категорий. */
export function possibleMetaEdges(
  index: ContentIndex, categories: Iterable<number>, gates: DecadeGates | null = null,
): MetaEdge[] {
  const inSet = new Set(categories);
  const edges: MetaEdge[] = [];
  for (const cat of inSet) {
    const capable = index.metaCapable(cat);
    if (!capable) continue;
    // мета-слово — это ИМЯ категории, и на поле оно такой же пузырь, как остальные:
    // «school subjects» на уровне 1-10 нарушает форму декады ровно так же, как
    // обычное двусловное слово. Без этого фильтра гейты ловили мета-слова
    // уже в валидаторе, и уровень уходил в отказ на 24-й попытке
    if (!wordFitsGates(index, capable.word, metaGates(gates))) continue;
    for (const host of capable.hosts) {
      if (!inSet.has(host) || host === cat) continue;
      edges.push({ child: cat, parent: host, word: capable.word });
    }
  }
  return edges;
}

/**
 * Ищет цепочку заданной глубины по всей базе, без учёта истории пакета.
 *
 * Нужно потому, что глубокие цепочки — дефицитный ресурс: правила свежести
 * съедают их участников на ранних уровнях блока, и уровню, которому глубина
 * нужна по плану, её уже не хватает. Поэтому блок сначала резервирует цепочку,
 * а потом генерирует уровни.
 */
export function planDeepChain(
  index: ContentIndex, depth: number, seed: string, wordsPerCategory = 4,
  gates: DecadeGates | null = null,
): MetaEdge[] | null {
  if (depth < 2) return null;
  const usable: number[] = [];
  for (let cat = 0; cat < index.categories.length; cat += 1) {
    if (index.approvedCount(cat) >= wordsPerCategory) usable.push(cat);
  }
  const edges = possibleMetaEdges(index, usable, gates);
  const outgoing = new Map<number, MetaEdge[]>();
  const rng = createRng(`${seed}|deep-chain|${depth}`);
  for (const edge of rng.shuffle(edges)) {
    outgoing.set(edge.child, [...(outgoing.get(edge.child) ?? []), edge]);
  }
  const walk = (node: number, path: MetaEdge[], seen: Set<number>): MetaEdge[] | null => {
    if (path.length === depth) return path;
    for (const edge of outgoing.get(node) ?? []) {
      if (seen.has(edge.parent)) continue;
      seen.add(edge.parent);
      const found = walk(edge.parent, [...path, edge], seen);
      if (found) return found;
      seen.delete(edge.parent);
    }
    return null;
  };
  for (const start of rng.shuffle(Array.from(outgoing.keys()))) {
    const found = walk(start, [], new Set([start]));
    if (found) return found;
  }
  return null;
}

function buildMetaForest(
  index: ContentIndex, pool: PoolEntry[], c: Constraints, rng: Rng,
  forcedChain?: MetaEdge[],
  isWordFresh: (word: number) => boolean = () => true,
): { edges: MetaEdge[]; categories: Set<number> } {
  if (c.metaCount === 0) return { edges: [], categories: new Set() };

  const inPool = new Set(pool.map((p) => p.category));
  /**
   * Мета-слово тоже подчиняется свежести. Раньше не подчинялось, и получалось
   * так: слово `desserts` стоит на уровне 201 обычным пузырём, а на 202 приходит
   * мета-пузырём — формально это повтор слова внутри блока, который правила
   * свежести обязаны запрещать. Принудительные слова обходили проверку, потому
   * что ставились до перебора.
   */
  const allEdges: MetaEdge[] = possibleMetaEdges(index, inPool, c.gates)
    .filter((edge) => isWordFresh(edge.word));
  if (allEdges.length === 0 && !forcedChain?.length) {
    return { edges: [], categories: new Set() };
  }

  const shuffled = rng.shuffle(allEdges);
  const edges: MetaEdge[] = [];
  const parentOf = new Map<number, number>();
  const involved = new Set<number>();

  // рёбра, выходящие из категории: нужны, чтобы искать цепочки нужной глубины
  const outgoing = new Map<number, MetaEdge[]>();
  for (const edge of shuffled) {
    outgoing.set(edge.child, [...(outgoing.get(edge.child) ?? []), edge]);
  }

  const depthOf = (node: number, guard = 0): number => {
    if (guard > 8) return 99;
    const parent = parentOf.get(node);
    return parent === undefined ? 0 : 1 + depthOf(parent, guard + 1);
  };
  const chainDepth = (): number => {
    let deepest = 0;
    for (const node of parentOf.keys()) deepest = Math.max(deepest, depthOf(node));
    return deepest;
  };

  // сначала пытаемся набрать требуемую глубину: цепочка ребёнок → родитель → дед
  const wantDepth = Math.max(1, c.metaDepthTarget);
  const tryAdd = (edge: MetaEdge): boolean => {
    if (parentOf.has(edge.child)) return false;              // не больше одного родителя
    // цикл: родитель уже висит под ребёнком
    let cursor: number | undefined = edge.parent;
    for (let i = 0; cursor !== undefined && i < 10; i += 1) {
      if (cursor === edge.child) return false;
      cursor = parentOf.get(cursor);
    }
    parentOf.set(edge.child, edge.parent);
    if (chainDepth() > wantDepth) {                          // глубже, чем просили
      parentOf.delete(edge.child);
      return false;
    }
    edges.push(edge);
    involved.add(edge.child);
    involved.add(edge.parent);
    return true;
  };

  /**
   * Проход 1 — сначала строим САМУЮ ГЛУБОКУЮ цепочку, и только потом добираем
   * количество. Если делать наоборот, бюджет мета-связей расходуется на плоские
   * пары, и глубина 2-3 не появляется никогда: именно так выглядел первый
   * работающий прогон — 10 уровней из 10 с глубиной 1.
   *
   * Цепочка глубины d — это путь из d рёбер: c0 → c1 → … → cd.
   */
  const findChain = (length: number): MetaEdge[] | null => {
    if (length <= 1) return null;
    const walk = (node: number, path: MetaEdge[], seen: Set<number>): MetaEdge[] | null => {
      if (path.length === length) return path;
      for (const edge of outgoing.get(node) ?? []) {
        if (seen.has(edge.parent)) continue;
        seen.add(edge.parent);
        const found = walk(edge.parent, [...path, edge], seen);
        if (found) return found;
        seen.delete(edge.parent);
      }
      return null;
    };
    for (const start of rng.shuffle(Array.from(outgoing.keys()))) {
      const found = walk(start, [], new Set([start]));
      if (found) return found;
    }
    return null;
  };

  // зарезервированная цепочка идёт первой: под неё уровень и планировался
  if (forcedChain?.length) {
    for (const edge of forcedChain) tryAdd(edge);
  }

  if (chainDepth() < wantDepth && wantDepth >= 2 && c.metaCount >= wantDepth) {
    for (let target = wantDepth; target >= 2; target -= 1) {
      const chain = findChain(target);
      if (!chain) continue;
      for (const edge of chain) tryAdd(edge);
      if (chainDepth() >= target) break;
    }
  }

  // проход 2: добираем количество любыми доступными рёбрами
  for (const edge of shuffled) {
    if (edges.length >= c.metaCount) break;
    tryAdd(edge);
  }

  return { edges, categories: involved };
}

/** Выбор набора категорий: мета-каркас, quick-win, затем добор с учётом тем и редкости. */
function selectCategories(
  index: ContentIndex, pool: PoolEntry[], c: Constraints, rng: Rng,
  forcedChain?: MetaEdge[],
  isWordFresh: (word: number) => boolean = () => true,
): { selected: PoolEntry[]; edges: MetaEdge[] } | null {
  if (pool.length < c.categoryCount) return null;

  const byIndex = new Map(pool.map((p) => [p.category, p]));
  const { edges } = buildMetaForest(index, pool, c, rng,
    forcedChain?.filter((edge) => isWordFresh(edge.word)), isWordFresh);

  const selected: PoolEntry[] = [];
  const taken = new Set<number>();

  /**
   * Неразделимые пары отсекаются ЗДЕСЬ, при отборе категорий.
   *
   * Раньше это была только soft-проверка валидатора: пары вида
   * CONSTELLATIONS + ZODIAC SIGNS, DISEASES + ILLNESSES, TOYS + TOY CHEST
   * доезжали до готового уровня, счётчик решений находил две раскладки, и попытка
   * отклонялась — при том что какие именно четыре слова выбрать, уже не важно:
   * проблема в пулах, а не в выборке.
   *
   * Чего этот фильтр НЕ ловит: двусмысленность, собранную циклом обменов через
   * три и более категории. Там попарного пересечения пулов может не быть вовсе
   * (у `moons` и `stargazing` оно ровно ноль), и такие случаи остаются на
   * счётчике решений.
   *
   * Порог 0.30 по Жаккару: пересечение пулов approved-слов. Считаем по пулам,
   * а не по выбранным четвёркам, потому что проблема именно в пулах.
   *
   * Раньше фильтр работал только на калиброванных блоках: пресет 201-210 должен
   * был воспроизводить сдаваемый пакет байт-в-байт. Это условие отпало вместе со
   * сменой контентной базы — pack hash включает хеш снимка, и прежний пакет из
   * новой базы не воспроизводится ни при каких настройках. А нужда в фильтре
   * выросла: после импорта словаря оригинала слов, живущих в единственной
   * категории, стало меньше (пересечений 7696 против 3406), и точное покрытие
   * перестало сходиться на двух seed из двенадцати. Теперь фильтр работает всегда.
   */
  /**
   * Пул считаем по статусу alternative, а не approved.
   *
   * Двусмысленность создают именно alternative-связи: слово живёт в одной
   * категории как дом, но в соседней читается правдоподобно. Счётчик решений
   * смотрит ровно на этот статус, значит и фильтр пар обязан смотреть на него же,
   * иначе он мерит не то, что потом ломает уровень.
   */
  const plausibleSets = new Map<number, Set<number>>();
  const approvedSet = (entry: PoolEntry): Set<number> => {
    let set = plausibleSets.get(entry.category);
    if (!set) {
      set = new Set(index.categoryMemberships(entry.category, STATUS.alternative)
        .map((m) => m.word));
      plausibleSets.set(entry.category, set);
    }
    return set;
  };
  const UNSEPARABLE_JACCARD = 0.30;
  const separableFromSelected = (entry: PoolEntry): boolean => {
    /**
     * Запреты пар из базы действуют ВСЕГДА, в том числе без гейтов декады.
     *
     * Это не эвристика инструмента, а решение стороны контента: derive-conflicts
     * посчитал пересечение играбельных пулов и сохранил пару с причиной
     * (GEMSTONES + BIRTHSTONES — 15 общих слов, FABRICS + UPHOLSTERY — 13).
     * Живой Жаккар ниже остаётся: он ловит и то, чего в базе ещё нет, но
     * порог у него один на всех, а в базе есть ручные запреты и severity.
     */
    for (const other of selected) {
      if (index.conflict(entry.category, other.category)) return false;
    }
    const a = approvedSet(entry);
    for (const other of selected) {
      const b = approvedSet(other);
      let shared = 0;
      for (const w of a) if (b.has(w)) shared += 1;
      const union = a.size + b.size - shared;
      if (union > 0 && shared / union >= UNSEPARABLE_JACCARD) return false;
    }
    return true;
  };

  const add = (entry: PoolEntry | undefined): void => {
    if (!entry || taken.has(entry.category) || selected.length >= c.categoryCount) return;
    if (!separableFromSelected(entry)) return;
    taken.add(entry.category);
    selected.push(entry);
  };

  // мета-каркас идёт первым: без него нужной структуры не получить
  const usedEdges: MetaEdge[] = [];
  for (const edge of edges) {
    if (selected.length + 2 > c.categoryCount) break;
    add(byIndex.get(edge.child));
    add(byIndex.get(edge.parent));
    if (taken.has(edge.child) && taken.has(edge.parent)) usedEdges.push(edge);
  }

  // quick-win: инвариант открытой двери, нарушать нельзя
  const quickwinCandidates = rng.shuffle(
    pool.filter((p) => p.canQuickwin && !taken.has(p.category)));
  add(quickwinCandidates[0]);

  // добор: разнообразие тем и достаточный запас редких слов
  const themeUsage = new Map<string, number>();
  for (const entry of selected) {
    themeUsage.set(entry.theme, (themeUsage.get(entry.theme) ?? 0) + 1);
  }
  const rest = rng.shuffle(pool.filter((p) => !taken.has(p.category)));
  const scored = rest
    .map((entry) => {
      const themePenalty = (themeUsage.get(entry.theme) ?? 0) * 0.35;
      const rareBonus = c.rareTarget > 0 ? Math.min(entry.rareCount, 3) * 0.12 : 0;
      const depthBonus = Math.min(entry.approved.length - 4, 6) * 0.05;
      // категории под целевую медиану декады: чем ближе потолок узнаваемости
      // категории к цели сверху, тем она ценнее. Вес 0.9 сознательно крупный —
      // это главная ось сложности первых 120 уровней референса.
      // Вес 1.3 подобран перебором: 0.9 давало медиану блока 4.16 при цели 4.35,
      // 1.3 — 4.22 (в допуске), дальше рост упирается в содержимое базы
      const fitBonus = c.gates
        ? 1.3 * Math.max(0, 1 - Math.max(0, c.gates.zipfMedianTarget - entry.recognizability) / 1.2)
        : 0;
      /**
       * Простая категория ценнее сложной, и тем сильнее, чем раньше декада.
       * `base_difficulty` — оценка самой группы на стороне базы: COLORS 0.1,
       * UNIVERSITIES 0.4. Цель декады приезжает в гейтах; превышение не
       * запрещено, но дешевле. Вес 0.5 подобран замером: при 0.2 уровень 1
       * оставался на категориях d=0.4, при 1.0 блок 1-10 садился на одни и те же
       * простейшие темы и терял разнообразие (штраф за тему 0.35 переставал
       * работать).
       */
      const simpleBonus = c.gates && entry.difficulty !== null
        ? 0.5 * Math.max(0, Math.min(1, (c.gates.categoryDifficultyTarget - entry.difficulty) / 0.25))
        : 0;
      return {
        entry,
        score: rareBonus + depthBonus + fitBonus + simpleBonus - themePenalty
          + rng.stableWeight(entry.key) * 0.3,
      };
    })
    .sort((a, b) => b.score - a.score);

  for (const { entry } of scored) {
    if (selected.length >= c.categoryCount) break;
    add(entry);
    themeUsage.set(entry.theme, (themeUsage.get(entry.theme) ?? 0) + 1);
  }

  if (selected.length < c.categoryCount) return null;
  if (!selected.some((p) => p.canQuickwin)) return null;

  const selectedSet = new Set(selected.map((p) => p.category));
  return {
    selected,
    edges: usedEdges.filter((e) => selectedSet.has(e.child) && selectedSet.has(e.parent)),
  };
}

// --------------------------------------------------------------------------- //
// шаг 4: назначение слов — точное покрытие
// --------------------------------------------------------------------------- //

interface AssignmentResult {
  /** индекс категории → выбранные слова (индексы) */
  words: Map<number, number[]>;
  unrecognizableUsed: number;
  rareUsed: number;
}

function assignWords(
  index: ContentIndex,
  selected: PoolEntry[],
  edges: MetaEdge[],
  c: Constraints,
  history: PackHistory,
  plan: LevelPlan,
  rng: Rng,
  wordsPerCategory: number,
  isWordFresh: (word: number) => boolean,
): AssignmentResult | null {
  const selectedSet = new Set(selected.map((p) => p.category));
  // слова, которые являются именами выбранных категорий: их нельзя ставить
  // случайно, иначе возникнет незапланированная мета-связь
  const labelWords = new Map<number, number>();   // слово → категория, чьё это имя
  for (const cat of selectedSet) {
    const capable = index.metaCapable(cat);
    if (capable) labelWords.set(capable.word, cat);
  }
  const plannedMetaWord = new Map<number, MetaEdge>();  // слово → ребро
  for (const edge of edges) plannedMetaWord.set(edge.word, edge);

  const forced = new Map<number, number[]>();     // категория → обязательные слова
  for (const edge of edges) {
    const list = forced.get(edge.parent) ?? [];
    list.push(edge.word);
    forced.set(edge.parent, list);
  }

  // бюджет неузнаваемых слов: не более 10% пузырей уровня
  const totalSlots = selected.length * wordsPerCategory;
  const unrecognizableBudget = Math.floor(totalSlots * 0.1);

  // ровно одна категория объявляется quick-win и держит инвариант
  const quickwinCat = selected.find((p) => p.canQuickwin
    && !forced.has(p.category)
    && !edges.some((e) => e.child === p.category))?.category
    ?? selected.find((p) => p.canQuickwin)?.category;

  const used = new Set<number>();                 // занятые слова уровня
  const assignment = new Map<number, number[]>();
  let unrecognizableUsed = 0;
  let rareUsed = 0;

  /**
   * Очевидность связи «слово → эта категория», разложенная по словам.
   *
   * Считается лениво и один раз на категорию: `orderCandidates` вызывается на
   * каждом узле перебора, а связей у категории до 28 — линейный поиск в цикле
   * решателя обошёлся бы дороже самой сортировки.
   *
   * Где у снимка есть ВЕС СВЯЗИ (сводная база), берётся он, а не очевидность.
   * Это не замена оси, а её полная версия: вес связи — та же очевидность,
   * сведённая со статусом, точностью попадания и уликой оригинала в одно число
   * на той же шкале 0..1 (scripts/export_hybrid_snapshot.py). Смысл ровно тот
   * же — «какое из годных слов категории брать первым», — и вес отвечает на
   * него там, где очевидности не существует: у 33 384 связей, пришедших только
   * из выгрузки, размечать её было некому.
   *
   * У снимков без весов ничего не меняется: `weight` там null, и в кэш ложится
   * прежняя очевидность до знака.
   */
  const obviousnessCache = new Map<number, Map<number, number>>();
  const obviousnessIn = (cat: number): Map<number, number> => {
    let map = obviousnessCache.get(cat);
    if (!map) {
      map = new Map<number, number>();
      for (const m of index.categoryMemberships(cat, STATUS.approved)) {
        map.set(m.word, m.weight ?? m.obviousness);
      }
      obviousnessCache.set(cat, map);
    }
    return map;
  };

  const candidatesFor = (cat: number): number[] => {
    const chosen = assignment.get(cat) ?? [];
    const chosenNorms = chosen.map((w) => index.words[w].n);
    const isQuickwin = cat === quickwinCat;
    const catLabelNorm = index.categories[cat].l.toLowerCase();

    return index.categoryMemberships(cat, STATUS.approved)
      .map((m) => m.word)
      .filter((w) => {
        if (used.has(w)) return false;
        // тот же фильтр формы, что в buildPool: список кандидатов собирается
        // заново из индекса, поэтому без него сюда возвращались отсеянные слова
        if (!wordFitsGates(index, w, c.gates)) return false;
        const word = index.words[w];
        if (word.n === catLabelNorm) return false;               // слово = имя своей категории
        if (chosenNorms.some((n) => isNearDuplicate(n, word.n))) return false;

        // слово-имя другой выбранной категории допустимо только как плановая мета
        const labelOf = labelWords.get(w);
        if (labelOf !== undefined) {
          const edge = plannedMetaWord.get(w);
          if (!edge || edge.parent !== cat) return false;
        }

        if (isQuickwin && !index.isQuickwinWord(w)) return false;
        if (isQuickwin && plannedMetaWord.has(w)) return false;

        if (!index.isRecognizable(w) && unrecognizableUsed >= unrecognizableBudget) return false;

        if (c.enforceFreshness && !isWordFresh(w)) return false;
        return true;
      });
  };

  const orderCandidates = (cat: number, candidates: number[]): number[] => {
    const rareNeeded = c.rareTarget - rareUsed;
    const isQuickwin = cat === quickwinCat;
    const obviousness = obviousnessIn(cat);
    return candidates
      .map((w) => {
        const z = index.zipf(w);
        const isRare = z !== null && z < rareZipfCeiling(c.gates);
        let score = rng.stableWeight(`${cat}:${w}`) * 0.25;
        if (!isQuickwin && rareNeeded > 0 && isRare) score += 0.6;
        if (rareNeeded <= 0 && isRare) score -= 0.5;
        /**
         * Предпочтение по очевидности связи — см. OBVIOUSNESS_WEIGHT.
         *
         * Сравниваются только слова ОДНОЙ категории, поэтому постоянная часть
         * слагаемого на порядок не влияет: работает исключительно разброс
         * внутри пула. В категории, залитой одним значением, слагаемое —
         * константа, и порядок не меняется вовсе. Это правильное поведение:
         * там, где база ничего не различила, генератору нечего предпочитать.
         */
        score += OBVIOUSNESS_WEIGHT * (obviousness.get(w) ?? OBVIOUSNESS_UNKNOWN);
        /**
         * Предпочтение по узнаваемости — см. RECOGNITION_SPAN.
         *
         * Без гейтов декады это слабый тай-брейкер «при прочих равных —
         * понятнее» (вес 0.02): целевого распределения нет, шкалу не от чего
         * отсчитывать. С гейтами узнаваемость меряется от пола частотности.
         */
        if (z !== null) {
          if (c.gates) {
            score += 0.9 * recognitionScore(z, c.gates);
          } else {
            score += Math.min(z, 6) * 0.02;       // при прочих равных — понятнее
          }
        }
        /**
         * Короткое слово ценнее длинного — см. LENGTH_WEIGHT. Цель берётся из
         * профиля декады (замер оригинала), превышение стоит тем дороже, чем
         * дальше от цели; без гейтов ось выключена, как и остальные цели.
         */
        if (c.gates) {
          const letters = index.words[w].t.replace(/\s/g, '').length;
          const over = Math.max(0, letters - c.gates.wordLenTarget);
          score += LENGTH_WEIGHT * Math.max(0, 1 - over / LENGTH_SPAN);
          if (index.words[w].tok > 1) score -= MULTIWORD_PENALTY;
        }
        const last = history.wordLastLevel.get(index.words[w].n);
        if (last === undefined) score += 0.15;                   // новое для пакета слово
        return { w, score };
      })
      .sort((a, b) => b.score - a.score)
      .map((x) => x.w);
  };

  const cats = selected.map((p) => p.category);
  let nodes = 0;
  const NODE_LIMIT = 60000;

  const solve = (): boolean => {
    nodes += 1;
    if (nodes > NODE_LIMIT) return false;

    // MRV: категория с наименьшим числом доступных вариантов
    let target = -1;
    let best: number[] = [];
    for (const cat of cats) {
      const have = (assignment.get(cat) ?? []).length;
      if (have >= wordsPerCategory) continue;
      const options = candidatesFor(cat);
      const need = wordsPerCategory - have;
      if (options.length < need) return false;                   // forward checking
      if (target === -1 || options.length < best.length) {
        target = cat;
        best = options;
      }
    }
    if (target === -1) return true;                              // всё заполнено

    for (const word of orderCandidates(target, best)) {
      const list = assignment.get(target) ?? [];
      list.push(word);
      assignment.set(target, list);
      used.add(word);
      const wasUnrecognizable = !index.isRecognizable(word);
      const z = index.zipf(word);
      const wasRare = z !== null && z < rareZipfCeiling(c.gates);
      if (wasUnrecognizable) unrecognizableUsed += 1;
      if (wasRare) rareUsed += 1;

      if (solve()) return true;

      list.pop();
      if (list.length === 0) assignment.delete(target); else assignment.set(target, list);
      used.delete(word);
      if (wasUnrecognizable) unrecognizableUsed -= 1;
      if (wasRare) rareUsed -= 1;
    }
    return false;
  };

  // обязательные мета-слова ставим до перебора
  for (const [cat, words] of forced) {
    for (const word of words) {
      if (used.has(word)) return null;
      const list = assignment.get(cat) ?? [];
      if (list.length >= wordsPerCategory) return null;
      list.push(word);
      assignment.set(cat, list);
      used.add(word);
    }
  }

  if (!solve()) return null;
  return { words: assignment, unrecognizableUsed, rareUsed };
}

// --------------------------------------------------------------------------- //
// шаг 6: ловушки
// --------------------------------------------------------------------------- //

/**
 * Ловушка — не повтор слова в двух категориях, а слово с ОДНИМ домом при наличии
 * на поле второй правдоподобной категории. Именно так они работают в целевой игре:
 * ORANGE лежит в одной категории, но на поле есть и фрукты, и цвета
 * (TARGET_GAME_OBSERVATIONS §4, SPEC_AUDIT §16).
 *
 * Экспортируется ради уровней, которые собрал не этот генератор: чтобы оценить
 * готовый уровень оригинала по нашей модели, ловушки в нём надо найти ТЕМ ЖЕ
 * правилом, иначе сравнение оценок сравнивает правила, а не уровни.
 */
export function findTraps(
  index: ContentIndex, assignment: Map<number, number[]>, edges: MetaEdge[],
): Trap[] {
  const selected = new Set(assignment.keys());
  const homeOf = new Map<number, number>();
  for (const [cat, words] of assignment) for (const w of words) homeOf.set(w, cat);
  const metaWords = new Set(edges.map((e) => e.word));

  const traps: Trap[] = [];
  for (const [word, home] of homeOf) {
    if (metaWords.has(word)) continue;                  // мета-пузырь — не ловушка
    const homeMembership = index.categoryMemberships(home, STATUS.approved)
      .find((m) => m.word === word);
    for (const m of index.wordMemberships(word, STATUS.alternative)) {
      if (m.category === home || !selected.has(m.category)) continue;
      traps.push({
        word: index.words[word].t,
        home: index.categories[home].k,
        decoy: index.categories[m.category].k,
        homeObviousness: homeMembership?.obviousness ?? 0,
        decoyFit: m.fit,
        decoyObviousness: m.obviousness,
      });
    }
  }
  // сильнее та ловушка, где дом очевиднее, а приманка настоящая, но тихая
  return traps.sort((a, b) =>
    (b.decoyFit - b.decoyObviousness) - (a.decoyFit - a.decoyObviousness));
}

// --------------------------------------------------------------------------- //
// шаг 7: цепи
// --------------------------------------------------------------------------- //

/**
 * Цепи — единственный модификатор с аналитически доказуемым тупиком: если цепь
 * на A снимается сбором B, а цепь на B — сбором A, игрок заперт навсегда.
 * Поэтому граф зависимостей строится заведомо ациклическим, а валидатор это
 * перепроверяет независимо.
 */
function buildChains(
  categories: LevelCategory[], count: number, rng: Rng,
): Chain[] {
  if (count <= 0) return [];
  // запирать quick-win нельзя: игрок должен иметь точку входа
  const lockable = categories.filter((c) => !c.isQuickwin && c.metaDepth === 0);
  const unlockers = categories.filter((c) => c.isQuickwin || c.metaDepth === 0);
  if (lockable.length === 0 || unlockers.length === 0) return [];

  const chains: Chain[] = [];
  const locked = new Set<string>();
  for (const candidate of rng.shuffle(lockable)) {
    if (chains.length >= count) break;
    const unlocker = rng.shuffle(unlockers)
      .find((u) => u.key !== candidate.key && !locked.has(u.key));
    if (!unlocker) continue;
    chains.push({ locksCategory: candidate.key, unlockedByCompleting: unlocker.key });
    locked.add(candidate.key);
  }
  return chains;
}

// --------------------------------------------------------------------------- //
// сборка LevelSpec
// --------------------------------------------------------------------------- //

function buildLevelSpec(
  index: ContentIndex,
  plan: LevelPlan,
  selected: PoolEntry[],
  edges: MetaEdge[],
  assignment: Map<number, number[]>,
  wordsPerCategory: number,
  rng: Rng,
): { spec: LevelSpec; traps: Trap[] } {
  const parentOf = new Map<number, number>();
  for (const edge of edges) parentOf.set(edge.child, edge.parent);
  const metaWordToChild = new Map<number, number>();
  for (const edge of edges) metaWordToChild.set(edge.word, edge.child);

  const depthOf = (cat: number, guard = 0): number => {
    if (guard > 8) return 0;
    const parent = parentOf.get(cat);
    return parent === undefined ? 0 : 1 + depthOf(parent, guard + 1);
  };

  const quickwinKeys = new Set<string>();
  const categories: LevelCategory[] = selected.map((entry) => {
    const words = assignment.get(entry.category) ?? [];
    const meta = index.categories[entry.category];
    const levelWords: LevelWord[] = words.map((w) => {
      const child = metaWordToChild.get(w);
      const membership = index.categoryMemberships(entry.category, STATUS.approved)
        .find((m) => m.word === w);
      const word = index.words[w];
      if (child !== undefined) {
        return {
          text: word.t, kind: 'meta' as const,
          metaChild: index.categories[child].k,
          zipf: word.z, frequencyUnknown: word.u === 1,
        };
      }
      return {
        text: word.t, kind: 'word' as const,
        zipf: word.z, frequencyUnknown: word.u === 1,
        relation: membership?.relation,
        fit: membership?.fit,
        obviousness: membership?.obviousness,
      };
    });

    const hasMeta = levelWords.some((w) => w.kind === 'meta');
    const allFrequent = words.every((w) => index.isQuickwinWord(w));
    const isQuickwin = !hasMeta && allFrequent;
    if (isQuickwin) quickwinKeys.add(meta.k);

    return {
      key: meta.k,
      label: meta.l,
      rule: meta.r,
      theme: meta.th,
      words: levelWords,
      metaDepth: depthOf(entry.category),
      parentKey: parentOf.has(entry.category)
        ? index.categories[parentOf.get(entry.category)!].k : null,
      isQuickwin,
    };
  });

  const traps = findTraps(index, assignment, edges);
  const chains = buildChains(categories, plan.chainCount, rng);

  // ---------------- игровой модификатор: половинки считаются ДО выкладки ----
  // (распиленное слово занимает на поле два пузыря, и это меняет её бюджет),
  // лёд и «?» — ПОСЛЕ (блокируется то, что реально видно на старте)
  const halves: HalfSplit[] = [];
  if (plan.modifier === 'halves') {
    // фрагмент не имеет права быть валидным словом (SPEC §4): сверяем и со
    // словами уровня, и со всем лексиконом контентной базы
    const taken = new Set<string>(index.words.map((w) => w.n));
    for (const c of categories) {
      for (const w of c.words) taken.add(w.text.toLowerCase());
    }
    for (const c of rng.shuffle(categories)) {
      if (halves.length >= halfBudget(categories.length)) break;
      if (c.isQuickwin) continue;   // точку входа не пилим
      for (const w of rng.shuffle(c.words.filter((x) => x.kind === 'word'))) {
        const parts = splitWord(w.text, taken);
        if (!parts) continue;
        taken.add(parts[0].toLowerCase());
        taken.add(parts[1].toLowerCase());
        halves.push({ word: w.text, home: c.key, fragments: parts, fragmentsAreWords: false });
        break;                      // не больше одного распила в категории
      }
    }
  }
  const chunked = new Set(halves.map((h) => chunkKey(h.home, h.word)));

  const metaCount = edges.length;
  const bubbles = startBubbles(categories.length, metaCount, wordsPerCategory);
  // склейка половинки тратит ход: распилы входят в минимум мерджей и в лимит
  const floor = moveFloor(categories.length, halves.length, wordsPerCategory);

  // выкладка считается здесь, а не в прототипе: см. core/deal.ts
  const deal = buildDeal(plan.levelId, categories, {
    boardCapacity: BOARD_CAPACITY, wordsPerCategory,
  }, chunked);

  const frozenBubbles: BlockedBubble[] = [];
  const hiddenBubbles: BlockedBubble[] = [];
  if (plan.modifier === 'ice' || plan.modifier === 'hidden') {
    const list = plan.modifier === 'ice' ? frozenBubbles : hiddenBubbles;
    const usedCats = new Set<string>();
    const count = Math.min(2, Math.max(1, Math.floor(categories.length / 3)));
    for (const b of rng.shuffle(deal.start)) {
      if (list.length >= count) break;
      if (usedCats.has(b.category)) continue;
      // точка входа не блокируется: первый сбор обязан оставаться доступным
      if (quickwinKeys.has(b.category)) continue;
      if (chunked.has(chunkKey(b.category, b.word))) continue;
      usedCats.add(b.category);
      list.push({ word: b.word, category: b.category, layers: 2 + (list.length % 2) });
    }
  }
  const chainLine = plan.modifier === 'chain_line' && categories.length >= 2
    ? { need: Math.min(2, categories.length - 1) }
    : null;

  // блокирующий модификатор мерджей не добавляет, но стесняет выбор: +1 ход,
  // как в прототипе (BLOCKER_MOVE_BONUS)
  const blocker = frozenBubbles.length > 0 || hiddenBubbles.length > 0 || chainLine !== null;

  const spec: LevelSpec = {
    levelId: plan.levelId,
    schemaVersion: '2.2',
    board: {
      categoriesCount: categories.length,
      wordsPerCategory,
      startBubbles: bubbles,
      boardCapacity: BOARD_CAPACITY,
      moveFloor: floor,
      // K = null -> лимита нет: на L1 референса поле держит весь уровень
      moveLimit: plan.moveLimitK === null ? null
        : moveLimit(floor, plan.moveLimitK) + (blocker ? BLOCKER_MOVE_BONUS : 0),
      moveLimitK: plan.moveLimitK,
      moveLimitPolicy: 'conservative',
    },
    categories,
    deal,
    traps: traps.slice(0, Math.max(plan.trapTarget, traps.length > 0 ? 1 : 0)),
    halves,
    modifiers: { chains, frozenBubbles, hiddenBubbles, chainLine },
  };
  return { spec, traps };
}

// --------------------------------------------------------------------------- //
// генерация одного уровня с ослаблениями
// --------------------------------------------------------------------------- //

/**
 * Дополнительная проверка собранного уровня внутри цикла попыток.
 *
 * Сюда генератору передаются счёт решений и hard-валидация. Без этого
 * двусмысленный уровень доезжал бы до отчёта как готовый: именно так первый
 * прогон выдал уровень 202 с двумя полными раскладками. Отбраковывать надо
 * там, где ещё можно попробовать другой набор категорий.
 */
export type AcceptCheck = (spec: LevelSpec) => { ok: boolean; stage: string; reason: string };

export function generateLevel(
  index: ContentIndex,
  plan: LevelPlan,
  config: BlockConfig,
  history: PackHistory,
  options: {
    maxAttempts?: number;
    accept?: AcceptCheck;
    /** категории, зарезервированные под другие уровни блока */
    excludeCategories?: Set<number>;
    /** цепочка, зарезервированная под ЭТОТ уровень */
    forcedChain?: MetaEdge[];
  } = {},
): LevelGenerationOutcome {
  const attempts: GenerationAttempt[] = [];
  const relaxationsUsed: Relaxation[] = [];
  /**
   * Сорок восемь попыток, а не двадцать четыре.
   *
   * Сначала это было нужно только калиброванным блокам: гейты декады отсекают
   * часть пула, и при 24 попытках декада 51-60 собирала 9 уровней из 10. Без
   * гейтов лимит держали на 24, чтобы не менять поведение пресета 201-210.
   *
   * После импорта словаря оригинала лимит поднят для всех. Причина конкретная:
   * слов, живущих в единственной категории, стало меньше (пересечений 7696
   * против 3406), и точное покрытие на большом уровне сходится не с первой
   * выборки — уровень 209 на 17 категорий не собрался ни за одну из 24 попыток
   * при том, что остальные девять уровней блока сошлись за 1-4. Причин держать
   * прежний лимит больше нет: пакет 201-210 всё равно не воспроизводится
   * байт-в-байт из новой базы.
   */
  const maxAttempts = options.maxAttempts ?? 48;
  const wordsPerCategory = config.wordsPerCategory || 4;

  const baseConstraints = (): Constraints => ({
    categoryCount: plan.categoryCount,
    gates: config.decadeGates ?? null,
    wordWindow: config.wordFreshnessWindow,
    categoryWindow: config.categoryFreshnessWindow,
    metaCount: plan.metaCount,
    metaDepthTarget: plan.metaDepthTarget,
    rareTarget: plan.rareTarget,
    rareTolerance: 0,
    trapTarget: plan.trapTarget,
    themesAllowed: config.includeThemes.length ? new Set(config.includeThemes) : null,
    themesExcluded: new Set(config.excludeThemes),
    enforceFreshness: true,
  });

  const applyRelaxations = (c: Constraints, list: Relaxation[]): Constraints => {
    const out = { ...c, themesAllowed: c.themesAllowed, themesExcluded: c.themesExcluded };
    for (const r of list) {
      switch (r) {
        case 'точное число редких слов → диапазон':
          out.rareTolerance = 3; break;
        case 'тематическая узость → соседние сферы':
          out.themesAllowed = null; break;
        case 'меньше ловушек':
          out.trapTarget = Math.max(0, out.trapTarget - 1); break;
        case 'меньше мета-связей':
          out.metaCount = Math.max(0, out.metaCount - 1); break;
        case 'меньше глубины мета':
          out.metaDepthTarget = Math.max(1, out.metaDepthTarget - 1); break;
        case 'другой набор категорий':
          break;                                   // реализуется сменой seed попытки
      }
    }
    return out;
  };

  let lastReason = 'не начато';
  let lastStage = 'инициализация';

  for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
    // каждое следующее ослабление включается после нескольких неудач подряд
    const relaxLevel = Math.min(RELAXATION_ORDER.length, Math.floor(attempt / 4));
    const active = RELAXATION_ORDER.slice(0, relaxLevel) as Relaxation[];
    const constraints = applyRelaxations(baseConstraints(), active);
    const rng = createRng(`${config.seed}|L${plan.levelId}|a${attempt}`);

    /**
     * Свежесть слова: одно правило для обычных пузырей и для мета-слов.
     * Ключ истории — нормализованная форма, чтобы регистр и вид апострофа
     * не создавали дырку в проверке.
     */
    const isWordFresh = (word: number): boolean => {
      if (!constraints.enforceFreshness) return true;
      const last = history.wordLastLevel.get(index.words[word].n);
      return last === undefined || plan.levelId - last > constraints.wordWindow;
    };

    const pool = buildPool(index, plan, constraints, history, options.excludeCategories);
    if (pool.length < constraints.categoryCount) {
      lastStage = 'пул категорий';
      lastReason = `после фильтров осталось ${pool.length} совместимых категорий, `
        + `а нужно ${constraints.categoryCount}`;
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const picked = selectCategories(index, pool, constraints, rng,
      options.forcedChain, isWordFresh);
    if (!picked) {
      lastStage = 'выбор категорий';
      lastReason = 'не удалось собрать набор с мета-каркасом и категорией быстрой победы';
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    /**
     * Мета-связей должно быть столько, сколько просит план.
     *
     * Раньше этой проверки не было: сколько мета-пар удалось собрать, столько и
     * шло в уровень. Из 20 декад восемь не проходили собственную приёмку по
     * META_RANGE — и всегда из-за одного-двух уровней, провалившихся ПОД коридор
     * (декада 31-40: [5,3,4,2,4,3,5,4,1,5] при коридоре 3-6). Причина не в
     * дефиците материала: мета-пар в базе 178, а в том, что попытка с бедным
     * набором категорий принималась, хотя следующая дала бы нужное.
     *
     * Требование снимается в последней трети попыток: потерять уровень хуже, чем
     * потерять одну мета-пару. Считать эту границу нужно от лимита попыток, а не
     * от числа ослаблений — у некалиброванного пресета лимит 24, ослабления
     * заканчиваются на 24-й попытке, и требование не снималось никогда: пресет
     * 201-210 терял по уровню на трёх seed из двенадцати.
     */
    const metaRequired = attempt < Math.floor((maxAttempts * 2) / 3);
    if (metaRequired && picked.edges.length < constraints.metaCount) {
      lastStage = 'мета-связи';
      lastReason = `мета-пар ${picked.edges.length}, план требует ${constraints.metaCount}`;
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const assigned = assignWords(index, picked.selected, picked.edges, constraints,
      history, plan, rng, wordsPerCategory, isWordFresh);
    if (!assigned) {
      lastStage = 'назначение слов';
      lastReason = 'точное покрытие не сошлось: у части категорий не остаётся '
        + 'четырёх свободных слов, каждое из которых имеет ровно один дом';
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const rareGap = Math.abs(assigned.rareUsed - constraints.rareTarget);
    if (rareGap > 1 + constraints.rareTolerance) {
      lastStage = 'редкость';
      lastReason = `редких слов ${assigned.rareUsed}, цель ${constraints.rareTarget}`;
      attempts.push({ index: attempt, outcome: 'rejected', stage: lastStage,
        reason: lastReason, relaxations: active.slice() });
      continue;
    }

    const { spec, traps } = buildLevelSpec(index, plan, picked.selected, picked.edges,
      assigned.words, wordsPerCategory, rng);

    if (options.accept) {
      const verdict = options.accept(spec);
      if (!verdict.ok) {
        lastStage = verdict.stage;
        lastReason = verdict.reason;
        attempts.push({ index: attempt, outcome: 'rejected', stage: verdict.stage,
          reason: verdict.reason, relaxations: active.slice() });
        continue;
      }
    }

    attempts.push({ index: attempt, outcome: 'accepted', stage: 'готово',
      reason: `${spec.categories.length} категорий, ${picked.edges.length} мета-связей, `
        + `${assigned.rareUsed} редких слов, ${traps.length} ловушек`,
      relaxations: active.slice() });
    relaxationsUsed.push(...active);
    return { spec, traps, attempts, relaxationsUsed: Array.from(new Set(relaxationsUsed)) };
  }

  return {
    traps: [],
    attempts,
    relaxationsUsed: Array.from(new Set(relaxationsUsed)),
    failure: {
      levelId: plan.levelId,
      reason: `Не сошлось за ${maxAttempts} попыток. Последняя причина — `
        + `${lastStage}: ${lastReason}.`,
      suggestions: [
        'расширить тематические сферы или снять исключения',
        'снизить точное число редких слов до диапазона',
        'уменьшить число мета-связей',
        'уменьшить число категорий на уровне',
        'пополнить базу: категориям не хватает утверждённых слов',
      ],
      attempts,
    },
  };
}

/** Обновляет историю пакета после принятия уровня. */
export function recordLevelInHistory(history: PackHistory, spec: LevelSpec): void {
  for (const category of spec.categories) {
    history.categoryLastLevel.set(category.key, spec.levelId);
    for (const word of category.words) {
      // тот же ключ, что использует проверка свежести: иначе слово с необычным
      // апострофом или регистром проскочило бы мимо неё
      history.wordLastLevel.set(normalizeWordKey(word.text), spec.levelId);
      history.wordCategory?.set(normalizeWordKey(word.text), category.key);
    }
  }
}

/** Ключ идентичности слова: как в снимке базы (поле `n`). */
export function normalizeWordKey(text: string): string {
  return text.normalize('NFKC')
    .replace(/[\u2018\u2019\u02bc\u2032]/g, "'")
    .replace(/[\u2010-\u2015\u2212]/g, '-')
    .trim().toLowerCase()
    .replace(/\s+/g, ' ');
}

export { quadrupleKey };
