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
 * Веса слов есть только у сводной базы (третий источник, снимок 2.1); на двух
 * остальных гейт молчит, потому что поля `w` у слов нет. Переводить порог
 * приходится потому, что у слова из чужого словаря регистра не существует, а
 * решать что-то надо: см. `minWordWeight` в types.ts.
 *
 * Числа не выбраны, а вытекают из якорей веса (export_hybrid_snapshot.py):
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
    repeatRange: [0, 4], zipfMedianTarget: 4.35, zipfP25Target: 3.80, maxTokens: 1,
    maxWordLen: 12, wordLenMean: 5.2, minProperNounZipf: 3.2, allowedModifiers: [] },
  { from: 11, categoryMean: 9.7, categoryCorridor: [7, 12], rareRange: [2, 5], metaRange: [2, 5],
    repeatRange: [3, 8], zipfMedianTarget: 4.01, zipfP25Target: 3.50, maxTokens: 2,
    maxWordLen: 13, wordLenMean: 6.2, minProperNounZipf: 3.0, allowedModifiers: ['chains'] },
  { from: 21, categoryMean: 9.3, categoryCorridor: [7, 12], rareRange: [2, 5], metaRange: [1, 4],
    repeatRange: [5, 11], zipfMedianTarget: 4.00, zipfP25Target: 3.51, maxTokens: 2,
    maxWordLen: 13, wordLenMean: 6.1, minProperNounZipf: 3.0, allowedModifiers: ['chains'] },
  { from: 31, categoryMean: 9.6, categoryCorridor: [6, 12], rareRange: [3, 7], metaRange: [3, 6],
    repeatRange: [6, 13], zipfMedianTarget: 3.85, zipfP25Target: 3.40, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.3, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 41, categoryMean: 9.4, categoryCorridor: [6, 12], rareRange: [3, 7], metaRange: [2, 5],
    repeatRange: [6, 13], zipfMedianTarget: 3.92, zipfP25Target: 3.41, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.2, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 51, categoryMean: 10.8, categoryCorridor: [7, 14], rareRange: [3, 6], metaRange: [3, 6],
    repeatRange: [10, 18], zipfMedianTarget: 4.06, zipfP25Target: 3.55, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.0, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 61, categoryMean: 9.8, categoryCorridor: [8, 13], rareRange: [3, 6], metaRange: [3, 6],
    repeatRange: [11, 19], zipfMedianTarget: 4.03, zipfP25Target: 3.51, maxTokens: 2,
    maxWordLen: 14, wordLenMean: 6.3, minProperNounZipf: 2.9, allowedModifiers: ['chains'] },
  { from: 71, categoryMean: 10.2, categoryCorridor: [6, 15], rareRange: [2, 5], metaRange: [2, 6],
    repeatRange: [14, 23], zipfMedianTarget: 4.04, zipfP25Target: 3.49, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.3, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 81, categoryMean: 9.5, categoryCorridor: [7, 12], rareRange: [2, 6], metaRange: [2, 5],
    repeatRange: [14, 24], zipfMedianTarget: 4.00, zipfP25Target: 3.47, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.0, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 91, categoryMean: 9.5, categoryCorridor: [7, 14], rareRange: [3, 7], metaRange: [3, 7],
    repeatRange: [13, 22], zipfMedianTarget: 3.96, zipfP25Target: 3.35, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.5, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 101, categoryMean: 9.2, categoryCorridor: [6, 13], rareRange: [3, 6], metaRange: [2, 5],
    repeatRange: [14, 23], zipfMedianTarget: 4.09, zipfP25Target: 3.45, maxTokens: 2,
    maxWordLen: 15, wordLenMean: 6.3, minProperNounZipf: 2.8, allowedModifiers: ['chains'] },
  { from: 111, categoryMean: 9.3, categoryCorridor: [5, 13], rareRange: [4, 8], metaRange: [2, 5],
    repeatRange: [14, 23], zipfMedianTarget: 3.99, zipfP25Target: 3.44, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.5, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  // ступенька: с L121 размер уровня прыгает с ~9.3 до ~13.2 и больше не падает
  { from: 121, categoryMean: 13.2, categoryCorridor: [10, 16], rareRange: [7, 12], metaRange: [2, 5],
    repeatRange: [22, 32], zipfMedianTarget: 3.70, zipfP25Target: 3.15, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.2, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  { from: 131, categoryMean: 14.3, categoryCorridor: [10, 17], rareRange: [5, 10], metaRange: [2, 5],
    repeatRange: [23, 33], zipfMedianTarget: 3.92, zipfP25Target: 3.37, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.0, minProperNounZipf: 2.7, allowedModifiers: ['chains'] },
  { from: 141, categoryMean: 13.4, categoryCorridor: [10, 17], rareRange: [6, 11], metaRange: [1, 4],
    repeatRange: [22, 32], zipfMedianTarget: 3.83, zipfP25Target: 3.33, maxTokens: 2,
    maxWordLen: 16, wordLenMean: 6.1, minProperNounZipf: 2.6, allowedModifiers: ['chains'] },
  { from: 151, categoryMean: 14.3, categoryCorridor: [11, 17], rareRange: [7, 13], metaRange: [1, 5],
    repeatRange: [21, 31], zipfMedianTarget: 3.82, zipfP25Target: 3.23, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.2, minProperNounZipf: 2.6, allowedModifiers: ['chains'] },
  { from: 161, categoryMean: 14.0, categoryCorridor: [11, 17], rareRange: [8, 14], metaRange: [1, 4],
    repeatRange: [20, 30], zipfMedianTarget: 3.73, zipfP25Target: 3.13, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.3, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 171, categoryMean: 14.5, categoryCorridor: [11, 18], rareRange: [7, 13], metaRange: [1, 4],
    repeatRange: [23, 33], zipfMedianTarget: 3.83, zipfP25Target: 3.21, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.3, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 181, categoryMean: 13.1, categoryCorridor: [11, 16], rareRange: [7, 13], metaRange: [1, 4],
    repeatRange: [21, 31], zipfMedianTarget: 3.80, zipfP25Target: 3.23, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.4, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
  { from: 191, categoryMean: 13.1, categoryCorridor: [11, 17], rareRange: [7, 12], metaRange: [1, 4],
    repeatRange: [20, 30], zipfMedianTarget: 3.87, zipfP25Target: 3.21, maxTokens: 2,
    maxWordLen: 17, wordLenMean: 6.6, minProperNounZipf: 2.5, allowedModifiers: ['chains'] },
];

/**
 * Профиль для диапазона уровней. За пределами замеренных 199 уровней (наш блок
 * 201-210 как раз там) продолжаем последней декадой: экстраполировать тренд не
 * на чем, а последняя декада — ближайшее известное состояние игры.
 */
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

function rhythmOk(
  counts: number[], corridor: [number, number], categoryMean: number,
): boolean {
  const spread = Math.max(...counts) - Math.min(...counts);
  if (spread < RHYTHM_INVARIANTS.minSpread || spread > RHYTHM_INVARIANTS.maxSpread) return false;
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
 */
export function planCategoryCounts(
  profile: DecadeProfile, seed: string, total = 10, isFirstDecade = false,
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
  while (spike - recovery < RHYTHM_INVARIANTS.minSpread
    && (spike < corridor[1] || recovery > corridor[0])) {
    if (spike < corridor[1]) spike += 1;
    if (spike - recovery >= RHYTHM_INVARIANTS.minSpread) break;
    if (recovery > corridor[0]) recovery -= 1;
  }
  base[SPIKE_POSITION - 1] = spike;
  base[RECOVERY_POSITION - 1] = recovery;

  const rng = createRng(`${seed}::rhythm::${profile.from}`);
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
): number[] {
  const [lo, hi] = profile.metaRange;
  const rng = createRng(`${seed}::meta::${profile.from}`);
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
  const categoryPlan = planCategoryCounts(profile, seed, total, isFirstDecade);
  const metaPlan = planMetaCounts(profile, categoryPlan, seed, isFirstDecade);

  return {
    levelRange,
    categoryCorridor: profile.categoryCorridor,
    spikePositions: [SPIKE_POSITION],
    recoveryPositions: [RECOVERY_POSITION],
    rarityRange: profile.rareRange,
    maxMetaDepth: 2,          // глубже 2 в референсе не встречается ни разу
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
      zipfMedianTarget: profile.zipfMedianTarget,
      zipfP25Target: profile.zipfP25Target,
      visibleShareMin: visibleShareMin(profile, 4),
      repeatRange: profile.repeatRange,
      tutorialFirstLevel: isFirstDecade,
    },
    ...overrides,
  };
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
  if (complete) add('CATEGORY_SPREAD', spread >= 5 && spread <= 7,
    `разброс ${spread} категорий (${Math.min(...counts)}-${Math.max(...counts)}), в референсе 5-7`);

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

  add('META_DEPTH', levels.every((l) => l.metaDepth <= 2),
    `максимальная глубина мета-цепи ${Math.max(...levels.map((l) => l.metaDepth))}, `
    + 'в референсе глубже 2 не встречается');

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
