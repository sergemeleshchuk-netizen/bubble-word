/**
 * Модель знания игрока: какие слова уровня игрок ЧИТАЕТ, а какие для него
 * просто буквы.
 *
 * Зачем это вообще. Оба наших проверяющих знают ответы. Счётчик решений
 * доказывает единственность раскладки, зрячий бот (`simulatePlayability.ts`)
 * читает `category` прямо из выкладки и поэтому не промахивается никогда.
 * Между ними провалилась ровно та часть игры, на которой держится её давление:
 * НЕВЕРНАЯ ДОГАДКА СТОИТ ХОД (прототип, `canMerge` → `moves--`). Уровень из
 * расхожих слов и уровень из редких получают у нас один и тот же бюджет ошибок
 * (`K` = 1.25…1.6 в `levelMath.ts`), хотя догадок во втором нужно заметно
 * больше. Эта модель — вход для слепого бота, который тот бюджет тратит.
 *
 * Что здесь важно про игру. Названий категорий игрок НЕ ВИДИТ: прототип
 * показывает только счётчик собранных наборов. Значит вопрос к слову не «знаю
 * ли я эту категорию», а «понимаю ли я, с чем это слово лежит вместе». Ровно на
 * это отвечает поле `obviousness` связи слово→категория, и ровно поэтому оно
 * здесь главная ось, а частотность — вторая.
 *
 * ЧЕСТНОЕ ПРЕДУПРЕЖДЕНИЕ О КАЛИБРОВКЕ. Числа ниже НЕ откалиброваны: живых
 * наигровок с замером промахов у нас нет, референс раскладку поля не содержит
 * вовсе. Поэтому результат слепого прогона живёт метрикой в отчёте и НЕ входит
 * ни в D, ни в hard-гейт приёмки — по той же причине, по которой веса мета-связей
 * подписаны «объявлено». Когда наигровки появятся, править надо ровно один
 * объект `DEFAULT_KNOWLEDGE`, и версию модели рядом с ним.
 */
import type { LevelSpec } from './types.ts';
import type { ContentIndex } from './snapshot.ts';
import { normalizeWordKey } from './generator.ts';

export const KNOWLEDGE_MODEL_VERSION = 'knowledge-0.2';

export interface KnowledgeModel {
  /**
   * zipf, ниже которого частотность слова не помогает вовсе. 2.0 — та же
   * граница, по которой D_base считает «очень редкие слова».
   */
  zipfUnknown: number;
  /** zipf, выше которого частотность больше не добавляет: слово и так на слуху */
  zipfKnown: number;
  /**
   * Множитель ясности у самого редкого слова — то есть НАСКОЛЬКО частотность
   * вообще вправе мешать.
   *
   * Не ноль, и это главное решение в формуле. Первая редакция складывала обе оси
   * с равным весом, и на ней очень редкое слово не могло стать читаемым, каким
   * бы бесспорным оно ни было: `narwhal` в ARCTIC ANIMALS получал 0.48, то есть
   * половина игроков будто бы не понимает, что нарвал — арктическое животное.
   * Это неверно по существу. В базе только играбельные слова, значит вопрос не
   * «знает ли игрок слово», а «как быстро он его читает»: редкость замедляет, но
   * не ослепляет. Ослепляет НЕОЧЕВИДНОСТЬ СВЯЗИ — расхожее `delta` в AIRLINES
   * игрок не увидит, — и она осталась главной осью, умножающей всё остальное.
   */
  zipfFloor: number;
  /**
   * Очевидность у связи без данных. То же число, что `OBVIOUSNESS_UNKNOWN` в
   * генераторе: 74% категорий базы залиты одним значением на весь пул, и
   * молчание там означает «неизвестно», а не «неочевидно».
   */
  obviousnessUnknown: number;
  /** zipf у слова, у которого частотность неизвестна */
  zipfFallback: number;
  /**
   * Навык игрока: множитель ясности. 1 — тот игрок, на которого посчитана
   * очевидность связей в базе; меньше — кому слова даются хуже.
   *
   * Это и есть первый кандидат на калибровку. Когда появятся наигровки с
   * замером промахов, подгонять надо ЭТО число: остальные три описывают
   * содержание уровня, а это — того, кто в него играет.
   */
  skill: number;
}

export const DEFAULT_KNOWLEDGE: KnowledgeModel = {
  zipfUnknown: 2.0,
  zipfKnown: 5.0,
  zipfFloor: 0.65,
  obviousnessUnknown: 0.78,
  zipfFallback: 3.0,
  skill: 1,
};

/**
 * Ясность слова 0..1 — насколько громко оно объявляет, с чем лежит.
 *
 * Не вероятность и не оценка сложности: это вход для броска «прочитал / не
 * прочитал» в слепом прогоне. Ясность 0.8 означает «четверо игроков из пяти
 * видят это слово на своём месте», а не «слово лёгкое на 0.8».
 *
 * Две оси перемножаются, а не складываются: это два разных препятствия, а не
 * два слагаемых одной трудности. Очевидность связи решает, увидит ли игрок
 * связь вообще; частотность — насколько быстро, и хуже чем в `zipfFloor` раз
 * помешать не может.
 */
export function wordClarity(
  word: { zipf: number | null; obviousness?: number },
  model: KnowledgeModel = DEFAULT_KNOWLEDGE,
): number {
  const obviousness = word.obviousness ?? model.obviousnessUnknown;
  const zipf = word.zipf ?? model.zipfFallback;
  const span = model.zipfKnown - model.zipfUnknown;
  const zipfFactor = span <= 0 ? 1
    : Math.max(0, Math.min(1, (zipf - model.zipfUnknown) / span));
  const pace = model.zipfFloor + (1 - model.zipfFloor) * zipfFactor;
  return Math.max(0, Math.min(1, obviousness * pace * model.skill));
}

/** Что слепой бот знает о каждом слове уровня до начала партии. */
export interface WordProfile {
  word: string;
  /** ключ категории, где слово действительно живёт */
  home: string;
  /** тема категории-дома: слова одной темы выглядят родственными */
  theme: string;
  clarity: number;
  /** категория-приманка, если слово заявлено ловушкой */
  decoy: string | null;
}

/**
 * Сила связи слово→категория так, как её читает ОТБОР СЛОВ в генераторе:
 * `weight ?? obviousness` (`obviousnessIn` в generator.ts).
 *
 * Зачем эта функция, а не поле `LevelWord.obviousness`. В спеке лежит СЫРАЯ
 * очевидность, и у словаря оригинала она заглушка: у связей происхождения
 * `reference` — а это две трети словаря — там медиана 0.41, потому что нашей
 * разметки за ними нет, а настоящий сигнал живёт в `weight` (медиана 0.795).
 * Первая редакция модели читала спек напрямую и объявляла две трети словаря
 * оригинала нечитаемыми: ясность блока падала с 0.75 до 0.50 при переключении
 * источника, хотя уровни там не стали труднее — просто разметка другая.
 *
 * Поле спека трогать нельзя: `LevelSpec` целиком входит в `levelSpecHash`, и
 * правка значения переписала бы хеши всех сданных пакетов. Поэтому сигнал
 * достаётся из индекса, а спек остаётся тем же.
 */
function linkStrength(
  index: ContentIndex, categoryKey: string, wordText: string,
): number | undefined {
  const category = index.categoryIndex(categoryKey);
  const word = index.wordIndex(normalizeWordKey(wordText));
  if (category === undefined || word === undefined) return undefined;
  const membership = index.categoryMemberships(category).find((m) => m.word === word);
  if (!membership) return undefined;
  return index.linkWeight(membership) ?? membership.obviousness;
}

/**
 * Профиль слов уровня. Ключ — текст слова: у валидного уровня у каждого слова
 * ровно один дом, это hard-инвариант валидатора, поэтому текста достаточно.
 *
 * Без `index` сигнал берётся из спека — так оцениваются сданные пакеты, у
 * которых снимка под рукой нет. На словаре оригинала это занижает ясность, и
 * прогон честно помечает себя `signalFromSpec`.
 */
export function wordProfiles(
  spec: LevelSpec,
  model: KnowledgeModel = DEFAULT_KNOWLEDGE,
  index?: ContentIndex,
): Map<string, WordProfile> {
  const decoyOf = new Map<string, string>();
  for (const trap of spec.traps) decoyOf.set(trap.word, trap.decoy);

  const out = new Map<string, WordProfile>();
  for (const category of spec.categories) {
    for (const word of category.words) {
      const obviousness = (index
        ? linkStrength(index, category.key, word.text) : undefined)
        ?? word.obviousness;
      out.set(word.text, {
        word: word.text,
        home: category.key,
        theme: category.theme,
        clarity: wordClarity({ zipf: word.zipf, obviousness }, model),
        decoy: decoyOf.get(word.text) ?? null,
      });
    }
  }
  return out;
}

/** Средняя ясность слов уровня — одна цифра «насколько уровень читается». */
export function levelClarity(profiles: Map<string, WordProfile>): number {
  if (profiles.size === 0) return 1;
  let sum = 0;
  for (const p of profiles.values()) sum += p.clarity;
  return sum / profiles.size;
}

/**
 * ОПОРА — слово, за которое игрок может зацепиться: он видит, с чем оно лежит.
 *
 * Порог 0.5 читается буквально: половина игроков раскладывает такое слово без
 * догадки. Ниже — слово работает как шифр, и четвёрка из таких слов собирается
 * только перебором, ход за ходом.
 *
 * Замер 04.08, 200 первых уровней слепым прогоном: категорий, у которых меньше
 * двух опор, набралось 206 на 200 уровней, и именно они предсказывают провал.
 * Уровни без таких категорий слепой игрок не доходит в 2% случаев, уровни с
 * тремя и больше — в 55%. Хрестоматийный пример — уровень 103 декады 101-110:
 * категория PIANO собралась из `kawai` (ясность 0.15), `steinway` (0.17),
 * `Chopin` (0.27) и `hammer` (0.60), то есть опора там ровно одна, и владелец
 * продукта не смог пройти уровень руками.
 *
 * Почему порог здесь, а не в генераторе: это утверждение о ЗНАНИИ ИГРОКА, а
 * генератор — его потребитель. Правило «сколько опор обязано быть в четвёрке»
 * живёт в генераторе (`ANCHORS_PER_CATEGORY`), потому что это уже дизайн.
 */
export const ANCHOR_CLARITY = 0.5;

/**
 * Опорное ли это слово для своей категории. `linkStrength` — сила связи
 * слово→категория (`weight ?? obviousness`, ровно то, что читает отбор слов
 * генератора); `undefined` означает «база не разметила», и тогда работает
 * умолчание модели.
 */
export function isAnchorWord(
  zipf: number | null, linkStrength: number | undefined,
  model: KnowledgeModel = DEFAULT_KNOWLEDGE,
): boolean {
  return wordClarity({ zipf, obviousness: linkStrength }, model) >= ANCHOR_CLARITY;
}
