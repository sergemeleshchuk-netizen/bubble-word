/**
 * Профили декад: каким должен быть блок в зависимости от номера уровней.
 *
 * Причина существования файла. Раньше в генераторе был один пресет —
 * `DEFAULT_BLOCK_CONFIG` для блока 201-210. Когда в него подставили диапазон
 * 1-10, всё остальное осталось от поздней палитры: 13-18 категорий вместо 5-12,
 * 9-13 редких слов на уровень вместо ~2. На выходе получились уровни примерно
 * L150+, выданные под номерами 1-10 (разбор: docs/DECADE_CALIBRATION.md).
 *
 * Числа взяты замером всех 199 уровней оригинала, скрипт `scripts/decade_profile.py`.
 * Главное, что показал замер: размер уровня — НЕ основная ось сложности.
 * Категорий на уровень: плато ~9.5 на L1-120 и плато ~13.5 на L121+, между ними
 * ступенька. А растут внутри плато узнаваемость слов (медиана zipf 4.35 → 3.99),
 * мета-плотность (1.7 → 3.3) и повторы слов из прошлых уровней (2.9 → 18.4).
 *
 * Почему калибровка ограничена L1-199 и НЕ пересчитывается по выгрузке 1025
 * уровней (reference/bwj-org, замер 02.08). Ручной дизайн у оригинала виден
 * только в начале кривой: примерно с L300 статистика замерзает — среднее 12.4
 * категории, мин 10, макс 16, десятками декад без единого отклонения. Это
 * почерк их собственного генератора, а не гейм-дизайнера. Калиброваться по
 * хвосту значило бы копировать усреднённость машины; сложность позднего
 * оригинала растёт не размером, а повторами (доля уже виденных слов доходит
 * до ~80%, и 70-80% повторов лежат в НОВОЙ категории) и неочевидностью
 * четвёртого слова четвёрки (градиент 0.71/0.60/0.50/0.39 — см. generator.ts,
 * OBVIOUSNESS_SLOT_TARGETS).
 */
import type { BlockConfig, Modifier } from './types.ts';
import { BOARD_CAPACITY } from './levelMath.ts';
import { autoScheme } from './deal.ts';
import { createRng } from './rng.ts';

export interface DecadeProfile {
  /** первый уровень декады: 1, 11, 21, … */
  from: number;
  /** среднее число категорий на уровень */
  categoryMean: number;
  /** наблюдённый коридор мин-макс внутри декады */
  categoryCorridor: [number, number];
  /** слов zipf<3 на уровень (в референсе это счётчик, а не пол по частотности) */
  rareRange: [number, number];
  /** мета-пар (слово = имя другой категории уровня) на уровень */
  metaRange: [number, number];
  /** слов, уже встречавшихся раньше в ДРУГОЙ категории, на уровень */
  repeatRange: [number, number];
  /** целевая медиана и 25-й процентиль частотности слов уровня */
  zipfMedianTarget: number;
  zipfP25Target: number;
  /**
   * Куда в пуле категории целится декада: 0 — верх (самые расхожие слова
   * каждой категории), 1 — низ. Выводится из `zipfMedianTarget`, см.
   * `poolRankTargetFor`; поле оставлено для ручного переопределения там, где
   * вывод не попадёт.
   */
  poolRankTarget?: number;
  /** предел числа токенов в ответе: 1 = только однословные */
  maxTokens: number;
  /** предел длины слова в буквах */
  maxWordLen: number;
  /**
   * Средняя длина слова в буквах, замеренная на этой декаде оригинала.
   *
   * Это ЦЕЛЬ отбора, а не запрет: потолок `maxWordLen` почти ничего не режет
   * (13 букв при средней 6.2), а разница между нашим уровнем и записанным
   * видна именно здесь. Замер уровня 12: у нас средняя 6.7 буквы и 22% слов
   * длиннее восьми, у оригинала 5.5 и 6% — при том что медиана частотности
   * почти совпала. То есть «сложные слова», на которые жалуется глаз, —
   * это в первую очередь ДЛИННЫЕ слова, а не редкие.
   */
  wordLenMean: number;
  /**
   * Минимальный zipf для имени собственного. Референс имена использует с L1
   * (monday), но узнаваемые: mars 4.27, egypt 4.45, beethoven 3.41, picasso 3.46.
   * Ниже ~3.2 начинается викторина, а не ассоциация.
   */
  minProperNounZipf: number;
  /** модификаторы, разрешённые на этой декаде (chains в оригинале — с L20) */
  allowedModifiers: Modifier[];
}

/**
 * Минимальная доля уровня, видимая на поле.
 *
 * Не поле таблицы, а производное от коридора: поле вмещает 24 пузыря всегда,
 * значит худший случай декады — её самый большой уровень. Руками это число
 * задавать нельзя, я на этом ошибся дважды: поставил 0.55 для декады 1-10,
 * где референс на L7 даёт ровно 50%, и 0.42 для 121-130, где 15 категорий
 * дают ровно 40%.
 */
export function visibleShareMin(profile: DecadeProfile, wordsPerCategory = 4): number {
  return BOARD_CAPACITY / (profile.categoryCorridor[1] * wordsPerCategory);
}

/**
 * Куда в пуле категории целится декада.
 *
 * Ранняя декада берёт из верха пула каждой категории (`year`, `day` в единицах
 * времени; `sea`, `river` в водоёмах), поздняя опускается ниже. Раньше эту
 * работу делала `zipfMedianTarget`, но делала её НЕ ТЕМ КОНЦОМ: цель стояла на
 * ОТДЕЛЬНОМ СЛОВЕ, и самое расхожее слово категории проигрывало за то, что
 * слишком частотное. Теперь цель стоит на УРОВНЕ, а слово выбирается своим
 * местом в собственной категории; `zipfMedianTarget` осталась мерой приёмки.
 *
 * Числа в таблице подобраны, а не выведены: связь между глубиной по рангу и
 * медианой блока монотонна, но не линейна — она зависит от того, какие
 * категории попали в декаду и насколько широки их пулы. Линейная прикидка
 * промахнулась на шести декадах из двадцати. Подбор делает
 * `scripts/calibrate_pool_rank.ts` делением отрезка пополам; после него все
 * 20 декад сходятся с целью в пределах ±0.05, приёмка проходит везде.
 *
 * Формула ниже — запасной путь для профиля без калибровки: линейно между
 * 0.10 при медиане 4.35 и 0.62 при 3.70. Ей соответствует ровно одна ситуация
 * — новая декада, которую ещё не прогоняли.
 */
const POOL_RANK_AT_LOUD = 0.10;      // декада с целевой медианой ZIPF_LOUD
const POOL_RANK_AT_QUIET = 0.62;     // декада с целевой медианой ZIPF_QUIET
const ZIPF_LOUD = 4.35;
const ZIPF_QUIET = 3.70;

export function poolRankTargetFor(profile: DecadeProfile): number {
  if (profile.poolRankTarget !== undefined) return profile.poolRankTarget;
  const span = ZIPF_LOUD - ZIPF_QUIET;
  const position = (ZIPF_LOUD - profile.zipfMedianTarget) / span;
  const target = POOL_RANK_AT_LOUD + (POOL_RANK_AT_QUIET - POOL_RANK_AT_LOUD) * position;
  return Math.min(1, Math.max(0, Number(target.toFixed(3))));
}

/**
 * Целевая базовая сложность категории для декады.
 *
 * `base_difficulty` — поле базы (шкала 0.1-0.6, медиана 0.35): насколько трудна
 * сама группа, независимо от того, какие четыре слова из неё взяли. Генератор
 * это поле не читал, и уровень 1 собирался из UNIVERSITIES и LOCKSMITH WORDS
 * (d=0.4), хотя в базе лежат COLORS, FARM ANIMALS, FAMILY MEMBERS (d≤0.15).
 *
 * Числа здесь — не замер референса, а решение: у референсных категорий нашего
 * `d` не существует, сравнивать не с чем. Логика простая: первая декада берёт
 * нижнюю половину шкалы, к поздним потолок открывается до максимума. Отдельно
 * туториал: пять самых простых групп, как на L1 оригинала (коровы, цвета,
 * машины, компас, дни недели).
 */
const DIFFICULTY_CEILING_FIRST = 0.35;
const DIFFICULTY_CEILING_LAST = 0.6;
const TUTORIAL_DIFFICULTY_CEILING = 0.2;

/**
 * Пол частотности слова, одинаковый для всех декад. Смысл и замеры — в
 * `minWordZipf` (types.ts).
 *
 * Почему именно 3.75. Планку назвал владелец продукта, посмотрев два уровня в
 * прототипе: `quail` 3.13, `obituary` 3.41 и `congestion` 3.66 он назвал
 * неприемлемыми, а `cough` 3.95 и `rash` 3.67 претензий не вызвали. 3.75
 * проходит между `congestion` и `rash` — то есть это не круглое число, а
 * граница, снятая с конкретных примеров.
 */
const MIN_WORD_ZIPF = 3.75;

/**
 * Предельный регистр слова: 0 — в уровень идут только бытовые слова.
 *
 * Строже некуда, и это осознанно: игрок жаловался ровно на пассивный слой
 * (`quail`, `obituary`, `congestion`). Ёмкости хватает — бытовых слов 4924,
 * связей от них 10788, категорий с полной бытовой четвёркой 980 из 1265.
 * Если понадобится добрать сложность на поздних декадах, поднимать сюда до 1
 * (пускать пассивные), но не до 2: специальный слой это `tungsten` и `basilica`.
 */
const MAX_WORD_REGISTER = 0 as const;

/**
 * Регистр по декаде. Ранние — только бытовые, поздние допускают пассивные.
 *
 * Замер под жёстким нулём на всех двадцати декадах: собрано 196 уровней из 200,
 * потеряны по одному-двум на декадах 51, 61 и 91 — там коридор 7-14 категорий,
 * и бытового словаря на уровень из 14 групп уже не хватает по точному покрытию.
 *
 * Порог сдвига — 51-я декада, и это не круглое число, а граница жалобы: игрок
 * забраковал `quail` и `obituary` на уровнях 17 и 20, то есть в первых двух
 * декадах. Пятидесятый уровень — это далеко за пределами того, что он смотрел,
 * и там пассивный слой уже уместен как рычаг: игрок к этому времени сыграл
 * пятьсот категорий. Специальный слой (`tungsten`, `basilica`) не пускается
 * никогда — ни на одной декаде.
 */
function maxWordRegister(profile: DecadeProfile): 0 | 1 | 2 {
  return profile.from >= 51 ? 1 : MAX_WORD_REGISTER;
}

/**
 * Пол веса слова — тот же порог регистра, переведённый на шкалу веса.
 *
 * Веса слов есть только у словаря игры (рабочий источник, снимок 2.1); на двух
 * остальных гейт молчит, потому что поля `w` у слов нет. Переводить порог
 * приходится потому, что у слова из чужого словаря регистра не существует, а
 * решать что-то надо: см. `minWordWeight` в types.ts.
 *
 * Числа не выбраны, а вытекают из якорей веса (export_lexicon_snapshot.py):
 * бытовое слово весит 1.00, пассивное 0.55, специальное 0.20. Порог 0.70
 * пропускает ровно бытовые — это `maxWordRegister = 0`; порог 0.50 пропускает
 * бытовые и пассивные — это `maxWordRegister = 1`. Специальный слой не
 * проходит ни при одном пороге, как и было решено.
 *
 * Что порог делает с неразмеченной частью словаря (8786 слов выгрузки):
 * 0.70 пропускает 480 из них, 0.50 — 2773. То есть на ранних декадах чужой
 * словарь входит только самой расхожей своей частью, а на поздних открывается
 * шире — ровно так же, как открывается регистр.
 */
const WEIGHT_FLOOR_BY_REGISTER: Record<0 | 1 | 2, number> = {
  0: 0.70,
  1: 0.50,
  2: 0.0,
};

export function minWordWeight(profile: DecadeProfile): number {
  return WEIGHT_FLOOR_BY_REGISTER[maxWordRegister(profile)];
}

export function categoryDifficultyCeiling(profile: DecadeProfile): number {
  const decadeIndex = Math.floor((profile.from - 1) / 10);       // 0 … 19
  const span = DIFFICULTY_CEILING_LAST - DIFFICULTY_CEILING_FIRST;
  return Math.round((DIFFICULTY_CEILING_FIRST + (span * decadeIndex) / 19) * 100) / 100;
}

/**
 * Таблица §2 из docs/DECADE_CALIBRATION.md.
 *
 * Коридоры чуть шире наблюдённых мин-макс там, где выборка декады всего 10
 * уровней: наблюдение «мин 7» на одной декаде не запрещает 6 на соседней.
 */
export const DECADE_PROFILES: DecadeProfile[] = [
  { from: 1, categoryMean: 9.5, categoryCorridor: [5, 12], rareRange: [0, 2], metaRange: [0, 2],
    repeatRange: [0, 4], poolRankTarget: 0.233, zipfMedianTarget: 4.35, zipfP25Target: 3.80, maxTokens: 1,
    maxWordLen: 12, wordLenMean: 5.2, minProperNounZipf: 3.2, allowedModifiers: [] },
  { from: 11, categoryMean: 9.7, categoryCorridor: [7, 12], rareRange: [2, 5], metaRange: [2, 5],
    repeatRange: [3, 8], poolRankTarget: 0.398, zipfMedianTarget: 4.01, zipfP25Target: 3.50, maxTokens: 2,
    maxWordLen: 13, wordLenMean: 6.2, minProperNounZipf: 3.0, allowedModifiers: ['chains'] },
  { from: 21, categoryMean: 9.3, categoryCorridor: [7, 12], rareRange: [2, 5], metaRange: [1, 4],
    repeatRange: [5, 11], poolRankTarget: 0.383, zipfMedianTarget: 4.00, zipfP25Target: 3.51, maxTokens: 2,
    maxWordLen: 13, wordLenMean: 6.1, minProperNounZipf: 3.0, allowedModifiers: ['chains'] },
  { from: 31, categoryMean: 9.6, categoryCorridor: [6, 12], rareRange: [3, 7], metaRange: [3, 6],
    repeatRange: [6, 13], poolRankTarget: 0.602, zipfMedianTarget: 3.85, zipfP25Target: 3.40, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.3, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 41, categoryMean: 9.4, categoryCorridor: [6, 12], rareRange: [3, 7], metaRange: [2, 5],
    repeatRange: [6, 13], poolRankTarget: 0.383, zipfMedianTarget: 3.92, zipfP25Target: 3.41, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.2, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 51, categoryMean: 10.8, categoryCorridor: [7, 14], rareRange: [3, 6], metaRange: [3, 6],
    repeatRange: [10, 18], poolRankTarget: 0.172, zipfMedianTarget: 4.06, zipfP25Target: 3.55, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.0, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 61, categoryMean: 9.8, categoryCorridor: [8, 13], rareRange: [3, 6], metaRange: [3, 6],
    repeatRange: [11, 19], poolRankTarget: 0.210, zipfMedianTarget: 4.03, zipfP25Target: 3.51, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.3, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 71, categoryMean: 10.2, categoryCorridor: [6, 15], rareRange: [2, 5], metaRange: [2, 6],
    repeatRange: [14, 23], poolRankTarget: 0.188, zipfMedianTarget: 4.04, zipfP25Target: 3.49, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.3, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 81, categoryMean: 9.5, categoryCorridor: [7, 12], rareRange: [2, 6], metaRange: [2, 5],
    repeatRange: [14, 24], poolRankTarget: 0.258, zipfMedianTarget: 4.00, zipfP25Target: 3.47, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.0, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 91, categoryMean: 9.5, categoryCorridor: [7, 14], rareRange: [3, 7], metaRange: [3, 7],
    repeatRange: [13, 22], poolRankTarget: 0.332, zipfMedianTarget: 3.96, zipfP25Target: 3.35, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.5, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 101, categoryMean: 9.2, categoryCorridor: [6, 13], rareRange: [3, 6], metaRange: [2, 5],
    repeatRange: [14, 23], poolRankTarget: 0.125, zipfMedianTarget: 4.09, zipfP25Target: 3.45, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.3, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 111, categoryMean: 9.3, categoryCorridor: [5, 13], rareRange: [4, 8], metaRange: [2, 5],
    repeatRange: [14, 23], poolRankTarget: 0.313, zipfMedianTarget: 3.99, zipfP25Target: 3.44, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.5, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  // ступенька: с L121 размер уровня прыгает с ~9.3 до ~13.2 и больше не падает
  { from: 121, categoryMean: 13.2, categoryCorridor: [10, 16], rareRange: [7, 12], metaRange: [2, 5],
    repeatRange: [22, 32], poolRankTarget: 0.416, zipfMedianTarget: 3.70, zipfP25Target: 3.15, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.2, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  { from: 131, categoryMean: 14.3, categoryCorridor: [10, 17], rareRange: [5, 10], metaRange: [2, 5],
    repeatRange: [23, 33], poolRankTarget: 0.281, zipfMedianTarget: 3.92, zipfP25Target: 3.37, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.0, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  { from: 141, categoryMean: 13.4, categoryCorridor: [10, 17], rareRange: [6, 11], metaRange: [1, 4],
    repeatRange: [22, 32], poolRankTarget: 0.289, zipfMedianTarget: 3.83, zipfP25Target: 3.33, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.1, minProperNounZipf: 2.6, allowedModifiers: ['chains'] },
  { from: 151, categoryMean: 14.3, categoryCorridor: [11, 17], rareRange: [7, 13], metaRange: [1, 5],
    repeatRange: [21, 31], poolRankTarget: 0.279, zipfMedianTarget: 3.82, zipfP25Target: 3.23, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.2, minProperNounZipf: 2.6, allowedModifiers: ['chains'] },
  { from: 161, categoryMean: 14.0, categoryCorridor: [11, 17], rareRange: [8, 14], metaRange: [1, 4],
    repeatRange: [20, 30], poolRankTarget: 0.359, zipfMedianTarget: 3.73, zipfP25Target: 3.13, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.3, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 171, categoryMean: 14.5, categoryCorridor: [11, 18], rareRange: [7, 13], metaRange: [1, 4],
    repeatRange: [23, 33], poolRankTarget: 0.301, zipfMedianTarget: 3.83, zipfP25Target: 3.21, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.3, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 181, categoryMean: 13.1, categoryCorridor: [11, 16], rareRange: [7, 13], metaRange: [1, 4],
    repeatRange: [21, 31], poolRankTarget: 0.326, zipfMedianTarget: 3.80, zipfP25Target: 3.23, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.4, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 191, categoryMean: 13.1, categoryCorridor: [11, 17], rareRange: [7, 12], metaRange: [1, 4],
    repeatRange: [20, 30], poolRankTarget: 0.273, zipfMedianTarget: 3.87, zipfP25Target: 3.21, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.6, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
];

/**
 * Профиль для диапазона уровней. За пределами замеренных 199 уровней (наш блок
 * 201-210 как раз там) продолжаем последней декадой: экстраполировать тренд не
 * на чем, а последняя декада — ближайшее известное состояние игры.
 */
/**
 * С какого уровня оригинала мета-цепь глубины 3 встречается на самом деле.
 *
 * Долгое время в трёх местах кода стояло «глубже 2 в референсе не встречается
 * ни разу», и по этому потолку браковались блоки. Утверждение опиралось на
 * разбор первых 20 уровней с видео и на спеку. Замер выгрузки 1025 уровней
 * (`reference-curve.md`) говорит иначе: глубина 2 впервые на L34 и нормой с
 * L51, а глубина 3 — впервые на **L438**, нормой к L931, всего 23 уровня (2%).
 *
 * То есть запрет верен только в пределах первых четырёхсот уровней, а
 * применялся ко всем блокам подряд — включая 201-400, где мы теперь собираем.
 * Потолок привязан к номеру уровня: ниже границы глубина 3 действительно
 * не подтверждена ничем, выше — это замеренное поведение оригинала.
 */
export const META_DEPTH_3_FROM_LEVEL = 438;

/** Потолок глубины мета-цепи для конкретного номера уровня. */
export function maxMetaDepthFor(levelId: number): number {
  return levelId >= META_DEPTH_3_FROM_LEVEL ? 3 : 2;
}

export function profileForRange(levelRange: [number, number]): DecadeProfile {
  const first = levelRange[0];
  let profile = DECADE_PROFILES[0];
  for (const candidate of DECADE_PROFILES) {
    if (candidate.from <= first) profile = candidate;
  }
  return profile;
}

/** Человеческое имя декады для интерфейса: «уровни 1-10». */
export function decadeLabel(profile: DecadeProfile): string {
  const next = DECADE_PROFILES.find((p) => p.from === profile.from + 10);
  return next ? `${profile.from}-${profile.from + 9}` : `${profile.from}+`;
}

/**
 * Ритм внутри декады.
 *
 * Замер по 19 полным декадам: единственная устойчивая фигура — спайк на позиции 5
 * (×1.17 от средней декады) и передышка на позиции 6 (×0.81); вниз на позиции 6
 * идут 16 декад из 19. Остальные позиции колеблются в пределах ±5%.
 *
 * Но усреднённый шаблон брать нельзя: он даёт разброс 3 категории и одно падение,
 * а в референсе разброс внутри декады стабильно 5-7 и вниз идут 37% переходов.
 * Поэтому к фигуре добавляется детерминированный от seed дребезг, и из кандидатов
 * выбирается первый, проходящий инварианты ритма.
 */
export const SPIKE_POSITION = 5;
export const RECOVERY_POSITION = 6;
const POSITION_SHAPE = [0.93, 0.98, 0.97, 0.99, 1.17, 0.81, 1.00, 1.05, 1.04, 1.07];

export interface RhythmInvariants {
  minSpread: number;
  maxSpread: number;
  minDescents: number;
}

export const RHYTHM_INVARIANTS: RhythmInvariants = {
  minSpread: 5, maxSpread: 7, minDescents: 3,
};

/**
 * Требуемый разброс для КОНКРЕТНОГО коридора.
 *
 * Числа 5-7 сняты с референса, у которого коридоры широкие (11-17, 6-15). Но
 * коридор — решение дизайнера, и он вправе его сузить: решение владельца 03.08
 * опустило поздние промежутки до 8-12, чтобы на кривой везде были уровни
 * передышки. В коридоре шириной 4 разброс 5 недостижим физически, и жёсткая
 * планка ставила FAIL там, где план сделал всё, что коридор позволяет.
 *
 * Поэтому требование = «столько пилы, сколько коридор вообще допускает»:
 * min(5, ширина) снизу, min(7, ширина) сверху. У широких коридоров правило
 * прежнее, зубы не потеряны — блок-прямая по-прежнему не проходит.
 */
export function spreadBoundsFor(corridor: readonly [number, number]): [number, number] {
  const width = Math.max(0, corridor[1] - corridor[0]);
  return [
    Math.min(RHYTHM_INVARIANTS.minSpread, width),
    Math.min(RHYTHM_INVARIANTS.maxSpread, width),
  ];
}

function rhythmOk(
  counts: number[], corridor: [number, number], categoryMean: number,
): boolean {
  const spread = Math.max(...counts) - Math.min(...counts);
  const [minSpread, maxSpread] = spreadBoundsFor(corridor);
  if (spread < minSpread || spread > maxSpread) return false;
  const descents = counts.slice(1).filter((c, i) => c < counts[i]).length;
  if (descents < RHYTHM_INVARIANTS.minDescents) return false;
  if (counts.some((c) => c < corridor[0] || c > corridor[1])) return false;
  /**
   * Среднее плана обязано попадать в цель декады с тем же допуском ±1.0,
   * что и приёмка CATEGORY_MEAN. Раньше план это не проверял, и декада 51-60
   * (цель 10.8) стабильно планировалась на 11.9: клэмп к коридору и раздвижка
   * спайка тащат среднее вверх, а приёмка потом честно ставила FAIL — причём
   * одинаково на всех трёх источниках, потому что виноват был сам план.
   */
  const mean = counts.reduce((a, b) => a + b, 0) / counts.length;
  if (Math.abs(mean - categoryMean) > 1.0) return false;
  // передышка после спайка — единственная гарантированная фигура референса
  const spike = counts[SPIKE_POSITION - 1];
  const recovery = counts[RECOVERY_POSITION - 1];
  if (counts.length >= RECOVERY_POSITION && recovery >= spike) return false;
  // два соседних уровня не должны быть структурно одинаковы
  return !counts.slice(1).some((c, i) => c === counts[i]);
}

/**
 * План числа категорий на декаду.
 *
 * `total` обычно 10. Для первой декады позиция 1 — туториал: в референсе L1 это
 * 5 категорий, весь уровень на поле и без лимита ходов.
 *
 * `rhythmKey` — то, чем дребезг отличает одну декаду от другой. По умолчанию
 * номер профиля, и до 200-го уровня это то же самое, что номер декады. А дальше
 * профиль один на всю кривую (последний замеренный, 191), и блок 201-210
 * получал ровно тот же план, что блок 4991-5000: одинаковые не «похожие», а
 * побайтно те же десять чисел. Поэтому вызывающий передаёт сюда номер первого
 * уровня блока — разнообразие на поздней кривой начинается здесь.
 */
export function planCategoryCounts(
  profile: DecadeProfile, seed: string, total = 10, isFirstDecade = false,
  rhythmKey: number = profile.from,
): number[] {
  const corridor = profile.categoryCorridor;
  const clamp = (v: number): number => Math.min(corridor[1], Math.max(corridor[0], v));
  const base = POSITION_SHAPE.slice(0, total)
    .map((factor) => clamp(Math.round(profile.categoryMean * factor)));

  /**
   * Спайк и передышка задают разброс блока.
   *
   * Одной фигуры ×1.17/×0.81 мало: в узком коридоре (например 8-13 у декады
   * 61-70) она даёт разброс 4, а инвариант требует 5-7. В самом референсе спайк
   * и передышка почти всегда и есть крайние точки декады, поэтому раздвигаем
   * именно их — до нужного разброса, но не за пределы коридора.
   */
  let spike = base[SPIKE_POSITION - 1];
  let recovery = base[RECOVERY_POSITION - 1];
  const wantSpread = spreadBoundsFor(corridor)[0];
  while (spike - recovery < wantSpread
    && (spike < corridor[1] || recovery > corridor[0])) {
    if (spike < corridor[1]) spike += 1;
    if (spike - recovery >= wantSpread) break;
    if (recovery > corridor[0]) recovery -= 1;
  }
  base[SPIKE_POSITION - 1] = spike;
  base[RECOVERY_POSITION - 1] = recovery;

  const rng = createRng(`${seed}::rhythm::${rhythmKey}`);
  for (let attempt = 0; attempt < 500; attempt += 1) {
    const counts = base.map((value, i) => {
      // спайк и передышку дребезг не трогает: это несущая фигура ритма
      if (i + 1 === SPIKE_POSITION || i + 1 === RECOVERY_POSITION) return value;
      // остальные позиции держим между передышкой и спайком, иначе дребезг
      // легко выносит разброс за верхнюю границу 7
      return Math.min(spike, Math.max(recovery, clamp(value + rng.int(5) - 2)));
    });
    if (isFirstDecade) counts[0] = TUTORIAL_CATEGORY_COUNT;
    if (rhythmOk(counts, corridor, profile.categoryMean)) return counts;
  }
  // не сошлось за 500 попыток: возвращаем несущую фигуру с растянутыми краями,
  // чтобы разброс всё-таки набрался. Дальше блок отбракует checkBlockRhythm.
  const fallback = base.slice();
  fallback[SPIKE_POSITION - 1] = clamp(Math.round(profile.categoryMean * 1.25));
  fallback[RECOVERY_POSITION - 1] = clamp(Math.round(profile.categoryMean * 0.72));
  if (isFirstDecade) fallback[0] = TUTORIAL_CATEGORY_COUNT;
  return fallback;
}

/** L1 референса: 5 категорий, 20 пузырей = весь уровень, лимита ходов нет. */
export const TUTORIAL_CATEGORY_COUNT = 5;

/** Мета-план: середина коридора декады, ноль на туториале. */
export function planMetaCounts(
  profile: DecadeProfile, categoryCounts: number[], seed: string, isFirstDecade = false,
  rhythmKey: number = profile.from,
): number[] {
  const [lo, hi] = profile.metaRange;
  const rng = createRng(`${seed}::meta::${rhythmKey}`);
  return categoryCounts.map((categories, i) => {
    if (isFirstDecade && i === 0) return 0;   // мета-пары в оригинале с L3
    const span = hi - lo;
    const value = lo + (span > 0 ? rng.int(span + 1) : 0);
    return Math.min(value, categories - 1);
  });
}

/**
 * Конфиг блока, собранный из профиля декады.
 *
 * Всё, что пользователь потом поменяет руками в интерфейсе, сильнее этого:
 * профиль — разумный старт, а не запрет (принцип инструмента из DECISION_LOG).
 */
/** Какие игровые модификаторы доступны блоку, начинающемуся с уровня `from`. */
function modifiersForDecade(from: number): Modifier[] {
  const out: Modifier[] = [];
  if (from >= 11) out.push('halves');
  if (from >= 31) out.push('ice', 'hidden');
  if (from >= 51) out.push('chain_line');
  return out;
}

export function configForRange(
  levelRange: [number, number], seed: string, overrides: Partial<BlockConfig> = {},
): BlockConfig {
  const profile = profileForRange(levelRange);
  const total = levelRange[1] - levelRange[0] + 1;
  const isFirstDecade = levelRange[0] === 1;
  const categoryPlan = planCategoryCounts(profile, seed, total, isFirstDecade,
    levelRange[0]);
  const metaPlan = planMetaCounts(profile, categoryPlan, seed, isFirstDecade,
    levelRange[0]);

  return {
    levelRange,
    categoryCorridor: profile.categoryCorridor,
    spikePositions: [SPIKE_POSITION],
    recoveryPositions: [RECOVERY_POSITION],
    rarityRange: profile.rareRange,
    // глубина 3 в оригинале появляется с L438 — см. META_DEPTH_3_FROM_LEVEL
    maxMetaDepth: maxMetaDepthFor(levelRange[1]),
    // Игровые модификаторы включаются лесенкой по декадам (решение 02.08:
    // механики входят в генерацию, оценку и игровой JSON разом, а не по одной):
    //   с L11 половинки — в референсе распилы видны уже на уровне 12;
    //   с L31 лёд и «?» — блокираторы из GDD §7, референсом не калиброваны;
    //   с L51 цепь-линия — самый тяжёлый, только на пик блока.
    // Первая декада остаётся чистой: игрока учат базовой механике.
    // Цепи-замки (`chains` из profile.allowedModifiers) генератор по-прежнему
    // не ставит: прототип их не исполняет, а нечестный модификатор хуже никакого.
    allowedModifiers: modifiersForDecade(levelRange[0]),
    includeThemes: [],
    excludeThemes: [],
    trapThemes: [],
    // повтор слова в ДРУГОЙ категории — рычаг сложности, а не брак: окно запрета
    // сужаем до половины декады, а нужное число повторов задаёт repeatRange
    wordFreshnessWindow: 5,
    categoryFreshnessWindow: Math.max(10, 40 - Math.floor(profile.from / 10) * 2),
    wordsPerCategory: 4,
    seed,
    categoryPlan,
    metaPlan,
    decadeGates: {
      categoryDifficultyTarget: categoryDifficultyCeiling(profile),
      tutorialCategoryDifficultyMax: TUTORIAL_DIFFICULTY_CEILING,
      maxTokens: profile.maxTokens,
      maxWordLen: profile.maxWordLen,
      wordLenTarget: profile.wordLenMean,
      minProperNounZipf: profile.minProperNounZipf,
      // Пол частотности выключен: его заменил регистр слова. Держать оба
      // одновременно вредно — пол выбрасывает `omelet` 2.63 и `radish` 2.78
      // вместе с мусором, а регистр их оставляет. MIN_WORD_ZIPF сохранён рядом
      // как страховка для базы без разметки (см. типы DecadeGates).
      minWordZipf: 0,
      maxWordRegister: maxWordRegister(profile),
      minWordWeight: minWordWeight(profile),
      poolRankTarget: poolRankTargetFor(profile),
      zipfMedianTarget: profile.zipfMedianTarget,
      zipfP25Target: profile.zipfP25Target,
      visibleShareMin: visibleShareMin(profile, 4),
      repeatRange: profile.repeatRange,
      tutorialFirstLevel: isFirstDecade,
    },
    // облегчённая раздача — умолчание для калиброванных декад (решение 03.08);
    // пресет 201-210 поле не задаёт и сохраняет хеш сдаваемого пакета
    dealMinStartWords: dealMinStartWordsFor(levelRange[0]),
    // бюджет старта по замеру записанных уровней: первая декада встречает
    // игрока неполным полем, дальше 24. Здесь, а не только в интерфейсе, чтобы
    // офлайн-сборка блока давала то же, что кнопка в инструменте
    dealStartBubbles: dealStartBubblesFor(levelRange[0]),
    ...overrides,
  };
}

// --------------------------------------------------------------------------- //
// раздача стартового поля по промежуткам уровней
// --------------------------------------------------------------------------- //

/** Строка ручной настройки: с какого уровня действует какой минимум. */
export interface DealRangeSetting {
  /** первый уровень промежутка; действует до начала следующего промежутка */
  from: number;
  /** минимум слов категории на старте: 1 = историческая ровная раздача */
  minStartWords: number;
}

/**
 * Умолчание раздачи по промежуткам — облегчённая выкладка на всей кривой.
 *
 * Почему 2. Ровная раздача «всем понемногу» на уровнях от ~12 категорий
 * раскладывает часть категорий по одному слову. Пузырь-одиночка не сливается
 * ни с чем (пара ещё в очереди) — ход с ним невозможен, а внимание он съедает.
 * Замер по 400 уровням: на 13 категориях одиночек 4-7, на 16 — 10-13, до 62%
 * поля. Минимум «пара» превращает мёртвые пузыри в материал для хода; сложность
 * поздних уровней при этом живёт в повторах, редкости, мета и лимите ходов,
 * а не в неиграбельном поле.
 *
 * Таблица редактируется в инструменте (первая вкладка, блок «Раздача старта
 * по промежуткам уровней»); это умолчание — то, что действует из коробки
 * и в офлайн-скриптах.
 */
export const DEFAULT_DEAL_RANGES: DealRangeSetting[] = [
  { from: 1, minStartWords: 2 },
];

/** Минимум слов на старте для уровня: последняя строка таблицы, чей from <= level. */
export function dealMinStartWordsFor(
  level: number, ranges: readonly DealRangeSetting[] = DEFAULT_DEAL_RANGES,
): number {
  let value = 1;
  let best = -Infinity;
  for (const row of ranges) {
    if (row.from <= level && row.from > best) {
      best = row.from;
      value = row.minStartWords;
    }
  }
  return value;
}

// --------------------------------------------------------------------------- //
// таблица декад: коридор категорий и схема выкладки, редактируется на вкладке 1
// --------------------------------------------------------------------------- //

/**
 * Строка таблицы декад — формат замера оригинала (DECADE_CALIBRATION.md §2 и
 * таблица «декада | категорий min-max | схема выкладки» из разбора 02.08).
 * Таблица наглядна и редактируется руками: дизайнер видит, каким уровень
 * встречает игрока, и правит конкретную декаду, а не глобальный флаг.
 */
export interface DecadeTuningRow {
  /** первый уровень промежутка */
  from: number;
  /** последний уровень промежутка — определяет и подпись, и шаг сетки */
  to: number;
  /**
   * Шаров-слов на старте: [пол, потолок]. Потолок подрезает стартовое поле,
   * пол — требование приёмки выкладки. Смысл и замер — `dealStartBubbles`
   * в types.ts.
   */
  startBubbles: [number, number];
  /** коридор по числу категорий; уезжает в config.categoryCorridor */
  corridor: [number, number];
  /**
   * Вилка схем выкладки. Уровень с минимумом категорий коридора получает
   * schemeMin, с максимумом — schemeMax, между ними схема интерполируется
   * (resolveScheme). Заполнена одна из двух — она действует на весь промежуток.
   * Обе null = автоматическая облегчённая раздача (минимум пара, без одиночек).
   */
  schemeMin: number[] | null;
  schemeMax: number[] | null;
}

/**
 * Шаров-слов на старте по промежуткам — замер записанных уровней с
 * экстраполяцией (решение владельца 03.08).
 *
 * Что показывает запись 19 наигранных уровней (`obs.startBubbles` в
 * bwj-levels.json): L1-10 стартуют с 16-24 пузырей, L11-20 — с 18-24. Дальше
 * выгрузка старта не содержит вовсе, а поле к этому моменту уже доходит до
 * полной вместимости — значит экстраполяция одна: 24 и дальше 24 на всех
 * промежутках. Первая декада получает неполное поле не «на всякий случай», а
 * потому что так встречает игрока оригинал.
 *
 * Пол первой декады поднят с наблюдённых 16 до 16 как есть, потолок опущен до
 * 20: 24 пузыря в оригинале появляются на L7-L9, то есть в верхней половине
 * декады, и держать потолок 24 на весь промежуток значило бы отдать полное
 * поле уже второму уровню.
 */
const START_BUBBLES_BY_RANGE: { from: number; startBubbles: [number, number] }[] = [
  { from: 1, startBubbles: [16, 20] },
  { from: 11, startBubbles: [20, 24] },
  { from: 21, startBubbles: [24, 24] },
];

/**
 * Коридор категорий на поздней кривой — решение владельца 03.08, а не замер.
 *
 * Замер поздних уровней выгрузки даёт медиану ровно 12 категорий на всём
 * отрезке 201-1000 (мин 9, макс 16, десятками декад без отклонений). Профили
 * декад при этом сняты с L121-199, где медиана 14 и коридор 11-17, и раньше
 * этот коридор продолжался на ВСЮ остальную кривую: с L161 и до L5000 таблица
 * показывала одно и то же «11-17» и для минимума, и для максимума. Это неверно
 * дважды — потолок завышен против самого оригинала, а пол 11 не оставляет места
 * уровню передышки, хотя передышка обязана быть на любом участке кривой.
 *
 * Отсюда числа: до 500 пол опущен до 8 (передышек больше), до 1000 пол 9 при
 * том же потолке 12 оригинала, а после 1000 потолок открывается ВЫШЕ референса
 * (13, 14, 15) — это запас на уровни сложнее всего, что в оригинале есть.
 * Строки 1-160 не тронуты: там коридоры сняты с реальных уровней.
 */
const LATE_CORRIDORS: { from: number; corridor: [number, number] }[] = [
  { from: 161, corridor: [8, 12] },
  { from: 501, corridor: [9, 12] },
  { from: 1001, corridor: [9, 13] },
  { from: 2001, corridor: [8, 14] },
  { from: 3001, corridor: [9, 15] },
];

/** Строка таблицы по номеру уровня: последняя, чей `from <= level`. */
function rowAt<T extends { from: number }>(table: readonly T[], level: number): T {
  let found = table[0];
  for (const row of table) if (row.from <= level) found = row;
  return found;
}

/**
 * Сетка промежутков таблицы (решение владельца 03.08): первые сто уровней —
 * подекадно, дальше всё крупнее. Ручной дизайн у оригинала виден в начале
 * кривой, а с ~L300 статистика замерзает — править там каждую декаду не из
 * чего, и строк было бы не 27, а 500.
 *
 *   1-100    по 10   (10 строк, коридоры из замера соответствующих декад)
 *   101-200  по 20   (5 строк, коридор — объединение двух декад замера)
 *   201-1000 по 100  (8 строк, коридор поздней кривой)
 *   1001-5000 по 1000 (4 строки, потолок открывается выше референса)
 */
export function decadeTuningDefaults(): DecadeTuningRow[] {
  const rows: DecadeTuningRow[] = [];
  const corridorAt = (level: number): [number, number] => {
    let profile = DECADE_PROFILES[0];
    for (const p of DECADE_PROFILES) if (p.from <= level) profile = p;
    return [profile.categoryCorridor[0], profile.categoryCorridor[1]];
  };
  const push = (from: number, to: number) => {
    // с 161 коридор задан решением дизайнера, до 160 — объединением коридоров
    // всех декад замера внутри промежутка
    let corridor: [number, number];
    if (from >= LATE_CORRIDORS[0].from) {
      corridor = [...rowAt(LATE_CORRIDORS, from).corridor] as [number, number];
    } else {
      let lo = Infinity;
      let hi = -Infinity;
      for (let level = from; level <= Math.min(to, 200); level += 10) {
        const c = corridorAt(level);
        lo = Math.min(lo, c[0]);
        hi = Math.max(hi, c[1]);
      }
      corridor = Number.isFinite(lo) ? [lo, hi] : corridorAt(from);
    }
    const startBubbles = [...rowAt(START_BUBBLES_BY_RANGE, from).startBubbles] as [number, number];
    rows.push({ from, to, startBubbles, corridor, schemeMin: null, schemeMax: null });
  };
  for (let from = 1; from <= 91; from += 10) push(from, from + 9);
  for (let from = 101; from <= 181; from += 20) push(from, from + 19);
  for (let from = 201; from <= 901; from += 100) push(from, from + 99);
  for (let from = 1001; from <= 4001; from += 1000) push(from, from + 999);
  return rows;
}


/**
 * Бюджет старта для уровня — из таблицы декад (по умолчанию из её умолчаний).
 * Тот же способ поиска строки, что у `dealMinStartWordsFor`.
 */
export function dealStartBubblesFor(
  level: number, rows: readonly DecadeTuningRow[] = decadeTuningDefaults(),
): [number, number] {
  const row = decadeTuningRowFor(level, rows);
  return row ? [row.startBubbles[0], row.startBubbles[1]] : [1, BOARD_CAPACITY];
}

/** Строка таблицы для уровня: последняя, чей from <= level (как профиль декады). */
export function decadeTuningRowFor(
  level: number, rows: readonly DecadeTuningRow[],
): DecadeTuningRow | undefined {
  let found: DecadeTuningRow | undefined;
  for (const row of rows) {
    if (row.from <= level && (found === undefined || row.from > found.from)) found = row;
  }
  return found;
}

/**
 * Превью автоматической раздачи для M категорий: номинальная схема для колонки
 * таблицы (без распилов — они считаются уже на конкретном уровне).
 *
 * Правило одно и живёт в core/deal.ts (`autoScheme`): вход целиком, дальше
 * тройки, остаток — одна пара, одиночек нет. Здесь только вызов: две копии
 * правила разъехались бы, и таблица показывала бы дизайнеру не то, что уровень
 * получит на самом деле. Для M >= 8 при поле 24 даёт 4-3-3-3-3-3-3-2.
 */
export function liteSchemePreview(
  categories: number, wordsPerCategory = 4, capacity = BOARD_CAPACITY,
  minStartWords = 2,
): number[] {
  if (categories <= 0) return [];
  const field = Math.min(capacity, categories * wordsPerCategory);
  return autoScheme(field, categories, wordsPerCategory, minStartWords);
}

/** «4-3-3-3-2-2-2-2-1» → [4,3,3,3,2,2,2,2,1]; пусто → null (авто); мусор → undefined. */
export function parseScheme(raw: string): number[] | null | undefined {
  const trimmed = raw.trim();
  if (trimmed === '') return null;
  const parts = trimmed.split(/[-–—,\s]+/).filter(Boolean);
  if (parts.length === 0 || parts.length > 18) return undefined;
  const values: number[] = [];
  for (const p of parts) {
    if (!/^[1-4]$/.test(p)) return undefined;
    values.push(Number(p));
  }
  return values.sort((a, b) => b - a);
}

export function formatScheme(scheme: readonly number[]): string {
  return scheme.join('-');
}

/**
 * Целевое среднее категорий для коридора из таблицы.
 *
 * Пока коридор совпадал с замером декады, среднее брали оттуда же. Как только
 * дизайнер коридор поменял (а с решением 03.08 он поменян на всей кривой после
 * 160), замеренное среднее становится враньём: цель 13.1 внутри коридора 8-12
 * недостижима, и клэмп превращал весь план в ряд из одних потолков — десять
 * структурно одинаковых уровней. Середина коридора — это и есть то, что
 * дизайнер имеет в виду, написав «8-12»: уровни около десяти, передышка на
 * восьми, спайк на двенадцати.
 */
function meanForCorridor(corridor: readonly [number, number]): number {
  return (corridor[0] + corridor[1]) / 2;
}

/**
 * Применение строки таблицы к конфигу диапазона.
 *
 * Коридор: заменяет categoryCorridor и ПЕРЕСОБИРАЕТ план категорий и мета по
 * этому коридору. Раньше план только подрезался — и это работало, пока правка
 * была мелкой; коридор, целиком лежащий ниже замеренного среднего декады,
 * подрезкой превращался в прямую линию (все десять уровней по потолку).
 *
 * Сравнение идёт с коридором САМОГО конфига, а не со умолчанием таблицы: с
 * решением 03.08 умолчание таблицы для поздней кривой само отличается от
 * профиля декады, и сравнение с умолчанием молча выключало бы новые коридоры.
 *
 * Схема: уезжает в dealScheme как есть (null = авто, поле не ставится).
 * Бюджет старта: уезжает в dealStartBubbles всегда — потолок подрезает старт,
 * пол проверяется приёмкой выкладки.
 */
export function applyDecadeTuning(
  config: BlockConfig, rows: readonly DecadeTuningRow[],
): BlockConfig {
  const row = decadeTuningRowFor(config.levelRange[0], rows);
  if (!row) return config;
  const corridorDiffers = row.corridor[0] !== config.categoryCorridor[0]
    || row.corridor[1] !== config.categoryCorridor[1];
  const next: BlockConfig = { ...config };
  if (corridorDiffers) {
    next.categoryCorridor = [row.corridor[0], row.corridor[1]];
    const profile = profileForRange(config.levelRange);
    const effective: DecadeProfile = {
      ...profile,
      categoryCorridor: [row.corridor[0], row.corridor[1]],
      categoryMean: meanForCorridor(row.corridor),
    };
    const total = config.levelRange[1] - config.levelRange[0] + 1;
    const isFirstDecade = config.levelRange[0] === 1;
    next.categoryPlan = planCategoryCounts(effective, config.seed, total, isFirstDecade,
      config.levelRange[0]);
    next.metaPlan = planMetaCounts(effective, next.categoryPlan, config.seed, isFirstDecade,
      config.levelRange[0]);
  }
  next.dealStartBubbles = [row.startBubbles[0], row.startBubbles[1]];
  // Вилка схем: заполнена одна — действует на весь промежуток. Обе null =
  // авто; возможный след прежней вилки стирается, иначе однажды применённая
  // схема пережила бы свою отмену в таблице.
  const minSide = row.schemeMin ?? row.schemeMax;
  const maxSide = row.schemeMax ?? row.schemeMin;
  next.dealSchemeRange = minSide && minSide.length > 0 && maxSide
    ? { min: [...minSide], max: [...maxSide] }
    : undefined;
  next.dealScheme = undefined;
  return next;
}

// --------------------------------------------------------------------------- //
// приёмка блока по декаде
// --------------------------------------------------------------------------- //

/**
 * Допуск по медиане частотности для блока целиком.
 *
 * Значение искалось трижды, и обе первые попытки были неправильны — оставляю
 * историю, чтобы никто не повторил.
 *
 * 1. ±0.15 «на глаз». Калиброванный блок 1-10 давал 4.20 при цели 4.35 и падал
 *    на 0.153: проверка ловила не брак контента, а произвол собственного порога.
 * 2. «Половина расстояния до соседней декады». Красиво звучит и полностью
 *    ломается на плато: у декад 51-60, 61-70 и 71-80 цели 4.06, 4.03 и 4.04 —
 *    расстояние 0.01-0.03, то есть меньше шума замера. Требовать такой точности
 *    бессмысленно: эти декады по узнаваемости неразличимы в принципе.
 *
 * 3. Что есть на самом деле: у референса не 20 уровней узнаваемости, а три —
 *    туториальный (L1-10, медиана 4.35), основное плато (L11-120, 3.85-4.09,
 *    в среднем 4.00) и позднее плато (L121-199, 3.70-3.92, в среднем 3.81).
 *    Расстояние между тирами 0.35 и 0.19. Допуск 0.20 меньше этого расстояния
 *    (значит блок нельзя перепутать с чужим тиром) и больше разброса внутри
 *    тира (значит соседние декады не требуют невозможной точности).
 */
export const ZIPF_BLOCK_TOLERANCE = 0.20;

export function zipfBlockTolerance(_profile: DecadeProfile): number {
  return ZIPF_BLOCK_TOLERANCE;
}

/**
 * Соответствует ли собранный блок своей декаде.
 *
 * Отдельно от валидатора уровня, потому что часть требований проверяема только
 * на блоке целиком: медиана частотности — это медиана всей десятки (у самого
 * референса медианы отдельных уровней внутри L1-10 гуляют от 3.95 до 4.92),
 * а ритм — свойство последовательности.
 */
export interface DecadeFitInput {
  levelId: number;
  categoryCount: number;
  /** частотности всех слов уровня; null означает «частотнику слово неизвестно» */
  zipfs: (number | null)[];
  metaCount: number;
  metaDepth: number;
  chainCount: number;
  moveLimit: number | null;
  startBubbles: number;
  boardCapacity: number;
  wordsPerCategory: number;
}

export interface DecadeFitResult {
  passed: boolean;
  checks: { code: string; passed: boolean; detail: string }[];
}

function median(values: number[]): number {
  const s = [...values].sort((a, b) => a - b);
  return s.length ? s[Math.floor(s.length / 2)] : 0;
}

export function checkDecadeFit(
  levels: DecadeFitInput[], profile: DecadeProfile,
  blockTolerance = zipfBlockTolerance(profile),
  plannedCount = levels.length,
): DecadeFitResult {
  const checks: DecadeFitResult['checks'] = [];
  const add = (code: string, passed: boolean, detail: string): void => {
    checks.push({ code, passed, detail });
  };
  if (!levels.length) {
    return { passed: false, checks: [{ code: 'BLOCK_NOT_EMPTY', passed: false, detail: 'блок пуст' }] };
  }

  /**
   * Ритм — свойство ПОЛНОЙ последовательности. Если часть уровней не собралась,
   * судить по остатку нельзя: выпавший спайк превращает нормальный план в
   * «нет падений» и «разброс 3». Раньше приёмка так и врала, показывая FAIL
   * ритма там, где виноват был отказ генератора.
   */
  const complete = levels.length === plannedCount;
  add('BLOCK_COMPLETE', complete,
    `собрано ${levels.length} уровней из ${plannedCount}`
    + (complete ? '' : ' — проверки ритма пропущены, судить по остатку нельзя'));

  const counts = levels.map((l) => l.categoryCount);
  const mean = counts.reduce((a, b) => a + b, 0) / counts.length;
  if (complete) add('CATEGORY_MEAN', Math.abs(mean - profile.categoryMean) <= 1.0,
    `среднее категорий ${mean.toFixed(1)}, цель декады ${profile.categoryMean} (допуск ±1.0)`);

  const spread = Math.max(...counts) - Math.min(...counts);
  // требование по разбросу — «столько пилы, сколько допускает коридор»: в
  // коридоре шириной 4 разброс 5 недостижим физически (см. spreadBoundsFor)
  const [minSpread, maxSpread] = spreadBoundsFor(profile.categoryCorridor);
  if (complete) add('CATEGORY_SPREAD', spread >= minSpread && spread <= maxSpread,
    `разброс ${spread} категорий (${Math.min(...counts)}-${Math.max(...counts)}), `
    + `для коридора ${profile.categoryCorridor.join('-')} нужно ${minSpread}-${maxSpread} `
    + '(в референсе 5-7)');

  if (complete) add('CATEGORY_CORRIDOR',
    counts.every((c) => c >= profile.categoryCorridor[0] && c <= profile.categoryCorridor[1]),
    `коридор декады ${profile.categoryCorridor.join('-')}, факт `
    + `${Math.min(...counts)}-${Math.max(...counts)}`);

  const descents = counts.slice(1).filter((c, i) => c < counts[i]).length;
  if (complete) add('DESCENTS', descents >= 3,
    `переходов вниз ${descents} из ${counts.length - 1}, нужно минимум 3 (в референсе 37%)`);

  if (complete && counts.length >= RECOVERY_POSITION) {
    const spike = counts[SPIKE_POSITION - 1];
    const recovery = counts[RECOVERY_POSITION - 1];
    add('SPIKE_THEN_RECOVERY', recovery < spike,
      `позиция ${SPIKE_POSITION}: ${spike} категорий, позиция ${RECOVERY_POSITION}: ${recovery} `
      + '(в референсе 16 декад из 19 идут вниз именно здесь)');
  }

  // медиана по блоку: усредняем медианы уровней, а не сваливаем все слова в кучу,
  // иначе большой уровень перевешивал бы маленький
  const perLevelMedians = levels.map((l) => median(l.zipfs.filter((z): z is number => z !== null)));
  const blockMedian = perLevelMedians.reduce((a, b) => a + b, 0) / perLevelMedians.length;
  // эпсилон не косметика: разность double вида |4.20 - 4.35| даёт
  // 0.15000000000000036, и сравнение с ровным порогом падало без причины
  add('ZIPF_BLOCK_MEDIAN',
    Math.abs(blockMedian - profile.zipfMedianTarget) <= blockTolerance + 1e-9,
    `средняя медиана zipf по блоку ${blockMedian.toFixed(2)}, цель `
    + `${profile.zipfMedianTarget} (допуск ±${blockTolerance.toFixed(2)} — половина `
    + 'расстояния до соседней декады)');

  /**
   * Коридор редкости расширяем на RARE_RELAXATION.
   *
   * Генератору официально разрешено ослабление «точное число редких слов →
   * диапазон» (±3, см. RELAXATION_ORDER в generator.ts). Требовать в приёмке
   * строгий коридор — значит запрещать то, что сам генератор считает законным
   * компромиссом. Зубы проверка не теряет: у сломанного блока 1-10 было 9-13
   * редких слов на уровень при коридоре 0-2, то есть мимо даже с расширением.
   */
  const RARE_RELAXATION = 3;
  const lo = Math.max(0, profile.rareRange[0] - RARE_RELAXATION);
  const hi = profile.rareRange[1] + RARE_RELAXATION;
  const rareCounts = levels.map((l) =>
    l.zipfs.filter((z) => z === null || z < 3.0).length);
  const inRange = rareCounts.filter((n) => n >= lo && n <= hi).length;
  add('RARE_BUDGET', inRange >= Math.ceil(levels.length * 0.8),
    `редких слов в коридоре ${profile.rareRange.join('-')} (с допуском ${lo}-${hi}) `
    + `на ${inRange} уровнях из ${levels.length}; факт по уровням ${rareCounts.join(', ')}`);

  /**
   * Мета-пары: потолок жёсткий, пол — с допуском на один уровень.
   *
   * Сверху перебор запрещён строго: лишние мета-пары это скачок сложности, и
   * генератор их сам не просит. Снизу допуск нужен потому, что мета-пара
   * конкурирует с точным покрытием: на уровне 39 план требовал 3 пары, и на
   * 12 попытках из 21 набор с тремя парами не давал каждой категории четырёх
   * слов с единственным домом. Генератор отступил до 2 — это законный компромисс
   * (ослабление «меньше мета-связей»), запрещать его в приёмке значит запрещать
   * то, что мы сами разрешили. Ровно так же устроен допуск у RARE_BUDGET выше.
   *
   * Зубы проверка не теряет: провал ниже пола больше чем на 1 или больше чем на
   * одном уровне декады — это уже дефицит материала, и он обязан быть виден.
   */
  const META_FLOOR_SLACK = 1;
  const metaCounts = levels.map((l) => l.metaCount);
  const overCeiling = metaCounts.filter((n) => n > profile.metaRange[1]).length;
  const belowFloor = metaCounts.filter((n) => n < profile.metaRange[0]);
  const tooDeepBelow = belowFloor.filter((n) => profile.metaRange[0] - n > META_FLOOR_SLACK).length;
  add('META_RANGE',
    overCeiling === 0 && belowFloor.length <= 1 && tooDeepBelow === 0,
    `мета-пар по уровням ${metaCounts.join(', ')}; коридор декады `
    + `${profile.metaRange.join('-')}, ниже пола ${belowFloor.length} уровней `
    + `(допустим один и не глубже чем на ${META_FLOOR_SLACK})`);

  /*
   * Потолок глубины — у каждого уровня свой, по его номеру. Раньше здесь стояла
   * жёсткая двойка с формулировкой «в референсе глубже 2 не встречается»; замер
   * 1025 уровней это опроверг (глубина 3 с L438), и блоки за четырёхсотым
   * браковались ни за что. См. META_DEPTH_3_FROM_LEVEL.
   */
  const tooDeep = levels.filter((l) => l.metaDepth > maxMetaDepthFor(l.levelId));
  add('META_DEPTH', tooDeep.length === 0,
    `максимальная глубина мета-цепи ${Math.max(...levels.map((l) => l.metaDepth))}; `
    + `потолок до L${META_DEPTH_3_FROM_LEVEL} — 2, дальше 3 (в оригинале глубина 3 `
    + `впервые на L${META_DEPTH_3_FROM_LEVEL})`
    + (tooDeep.length ? `; нарушают ${tooDeep.map((l) => l.levelId).join(', ')}` : ''));

  const modifiersAllowed = profile.allowedModifiers.includes('chains');
  add('MODIFIERS_BY_DECADE', modifiersAllowed || levels.every((l) => l.chainCount === 0),
    modifiersAllowed
      ? 'цепи на этой декаде разрешены'
      : `цепи на декаде ${profile.from}+ запрещены (в оригинале с L20), найдено `
        + `${levels.reduce((n, l) => n + l.chainCount, 0)}`);

  const floor = visibleShareMin(profile);
  const shares = levels.map((l) => l.boardCapacity / (l.categoryCount * l.wordsPerCategory));
  add('VISIBLE_SHARE', shares.every((s) => s >= floor - 1e-9),
    `видимая доля уровня ${(Math.min(...shares) * 100).toFixed(0)}-`
    + `${(Math.max(...shares) * 100).toFixed(0)}%, минимум декады `
    + `${(floor * 100).toFixed(0)}% (24 пузыря на ${profile.categoryCorridor[1]} категорий)`);

  if (profile.from === 1) {
    const first = levels.find((l) => l.levelId === 1);
    add('TUTORIAL_FIRST_LEVEL',
      first !== undefined && first.moveLimit === null
        && first.categoryCount === TUTORIAL_CATEGORY_COUNT
        && first.startBubbles === first.categoryCount * first.wordsPerCategory,
      first
        ? `уровень 1: ${first.categoryCount} категорий, лимит `
          + `${first.moveLimit === null ? 'отсутствует' : first.moveLimit}, `
          + `пузырей ${first.startBubbles}`
        : 'уровня 1 в блоке нет');
  }

  return { passed: checks.every((c) => c.passed), checks };
}
