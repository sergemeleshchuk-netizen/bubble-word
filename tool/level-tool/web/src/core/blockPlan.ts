/**
 * План блока из 10 уровней.
 *
 * Блок — не десять монотонно растущих уровней, а композиция с ритмом. В референсе
 * 74 перехода из 198 идут ВНИЗ (37%), а разброс внутри любого окна из десяти
 * уровней стабильно 5-7 категорий. Провал сразу после пика читается как
 * запрограммированная передышка — тяжёлый уровень, затем лёгкий как награда.
 *
 * Профиль задаётся настройками. Дефолтный пресет воспроизводит найденный ритм.
 */
import type { BlockConfig, LevelModifier, LevelPlan, LevelRole } from './types.ts';
import { MAX_MOVE_LIMIT_K, MIN_MOVE_LIMIT_K } from './levelMath.ts';
import { STAGED_CATEGORIES } from './deal.ts';
import {
  EARLY_CURVE_UNTIL, META_MAX_EARLY, META_MAX_ORDINARY, META_MAX_SPIKE, configForRange,
} from './decadeProfiles.ts';

/**
 * Дефолтный пресет для 201-210.
 *
 * Числа категорий и мета взяты из спеки (они построены по ритму референса),
 * но стартовые пузыри здесь НЕ задаются: спека содержала в них 7 ошибок из 10.
 * Пузыри считает `startBubbles()` из числа категорий и мета.
 */
export const DEFAULT_BLOCK_CONFIG: BlockConfig = {
  levelRange: [201, 210],
  categoryCorridor: [11, 18],
  spikePositions: [5, 9],
  recoveryPositions: [3, 6, 10],
  rarityRange: [9, 13],
  /**
   * Глубина мета-цепи. Было 3 — легаси-значение, оставшееся с времён до
   * калибровки по декадам. Замер 199 уровней оригинала показал, что в ЭТОМ
   * диапазоне глубже двух мета-цепь не встречается (по выгрузке 1025 уровней
   * глубина 3 начинается с L438 — `META_DEPTH_3_FROM_LEVEL`), и калиброванный
   * путь (`configForRange`) с тех пор ставит потолок по номеру уровня, то есть
   * для наших диапазонов 2. Пресет 201-210 остался на трёх, и это
   * расхождение стоило дорого: уровень 209 (17 категорий, 4 мета-связи, 13
   * редких слов, 2 ловушки) требовал цепи глубины 3, поэтому был на границе
   * выполнимости и падал по точному покрытию при каждом пополнении базы — с
   * 02.08 трижды. Поднятие бюджета попыток с 48 до 200 не помогало: набор
   * категорий под такую цепь просто не покрывается. Приведено к замеру.
   */
  maxMetaDepth: 2,
  /**
   * Пусто сознательно: генератор работает как словесный/семантический.
   *
   * Единственный реализованный модификатор — цепь, и одна цепь не делает
   * «систему модификаторов»: она добавляет к сложности механику, которую
   * нечем сбалансировать против остальных, и запутывает оценку D. Поле и
   * механика цепи в типах и в прототипе остались — включать их обратно
   * нужно вместе с остальным набором, а не по одной.
   */
  allowedModifiers: [],
  includeThemes: [],
  excludeThemes: [],
  trapThemes: [],
  wordFreshnessWindow: 30,
  categoryFreshnessWindow: 40,
  wordsPerCategory: 4,
  // Seed сдаваемого пакета: инструмент по умолчанию собирает тот же блок, что
  // лежит в data/final-pack. Это и есть демонстрация детерминированности —
  // проверяющий нажимает «Собрать блок» и получает тот же результат.
  seed: 'final-03',
  /**
   * Старт раздаётся В ГЛУБИНУ, как во всей остальной кривой (решение владельца
   * 03.08 — «починить причину, а не симптом»).
   *
   * Пресет был единственным местом, где оставалась ИСТОРИЧЕСКАЯ ровная раздача
   * «всем понемногу»: поле уровня 201 выглядело как 4-2-2-2-2-2-2-2-2-1-1-1 —
   * одна собираемая четвёрка, восемь пар, из которых пачка досыпки не закрывает
   * ни одной, и три мёртвые одиночки. Именно это и означала жалоба «много разных
   * слов из разных категорий, сложно продвинуться со стартового состояния».
   *
   * Держали это ради воспроизводимости `data/final-pack`, но пакет там — артефакт
   * ПРЕЖНЕГО снимка базы (2afaed22, gen-1.0, скоринг d-1.0): с переходом на
   * аудированную базу инструмент перестал воспроизводить его байт в байт и без
   * этой правки. Значит цена правки — ноль, а выигрыш — уровни, в которые можно
   * играть с первого хода.
   */
  dealMinStartWords: 2,
  /**
   * Крупные уровни пресета (13-18 категорий) раскладывают линии в очередь:
   * четыре категории ждут прогресса и выходят на поле волнами (`planGates` в
   * core/deal.ts). Пресет — единственный блок кривой, где больше 12 категорий
   * встречается на шести уровнях из десяти, и именно на нём жалоба «со старта
   * некуда двигаться» была громче всего.
   */
  dealHoldCategories: STAGED_CATEGORIES,
  /**
   * Таблица стартовой раскладки пресет не переписывает: у сдаваемого пакета своя
   * форма кривой (13-18 категорий против 8-12 в таблице для этих номеров).
   */
  presetLocked: true,
  categoryPlan: [13, 15, 12, 16, 18, 12, 14, 15, 17, 13],
  /**
   * Мета-план приведён к проектному потолку (решение владельца 04.08, см.
   * `META_MAX_SPIKE` в decadeProfiles.ts): пятёрка на пике убрана, четвёрка
   * осталась только на нём, передышка на позиции 6 идёт совсем без мета.
   * Раньше здесь стояло [2, 3, 1, 4, 5, 1, 3, 2, 4, 2] — из спеки, а спека
   * брала числа из замера референса, где мета-пар щедро.
   */
  metaPlan: [1, 2, 1, 3, 4, 0, 2, 3, 3, 1],
};

/**
 * С чем инструмент ОТКРЫВАЕТСЯ (решение владельца 04.08, вечер: «сделай
 * дефолтно выбранными значениями в генераторе»).
 *
 * Это ровно тот блок, который владелец собрал руками, когда искал, чем ещё
 * облегчить уровни: линейка 121-130, два пика (5 и 9) с передышкой сразу после
 * каждого, редких слов 1-2, глубина мета 1 (цепочек нет), узкие окна свежести,
 * план категорий до 12 и мета-план до двух пар. Держать эти числа в коде, а не
 * в чьей-то памяти, — единственный способ открывать инструмент на состоянии,
 * которое проверено игрой.
 *
 * Пресет 201-210 (`DEFAULT_BLOCK_CONFIG`) остаётся отдельно: по нему живут
 * скрипты и регрессия сданного пакета, и подменять его настройками одного
 * вечера нельзя.
 *
 * Гейты декады берём у 121-130 (`configForRange`): длина слова, число токенов,
 * пол для имён собственных — это свойства номеров уровней, а не вкуса.
 * `presetLocked` стоит по той же причине, что у пресета: конфиг собран руками,
 * и таблица декад не вправе переписать его молча — она вступает в дело, когда
 * человек меняет диапазон.
 */
export const STARTING_BLOCK_CONFIG: BlockConfig = {
  ...configForRange([121, 130], 'final-04'),
  categoryCorridor: [8, 12],
  spikePositions: [5, 9],
  recoveryPositions: [6, 10],
  rarityRange: [1, 2],
  maxMetaDepth: 1,
  wordFreshnessWindow: 1,
  categoryFreshnessWindow: 5,
  categoryPlan: [10, 8, 9, 10, 12, 8, 10, 11, 12, 10],
  metaPlan: [0, 1, 2, 2, 2, 0, 1, 2, 1, 0],
  presetLocked: true,
};

function roleFor(position: number, total: number, config: BlockConfig): LevelRole {
  if (position === 1) return 'entry';
  if (position === total) return 'exit';
  if (config.spikePositions.includes(position)) {
    // самый нагруженный спайк называем пиком, остальные — спайками
    const peak = config.spikePositions.reduce((best, p) => {
      const plan = config.categoryPlan;
      if (!plan) return Math.max(best, p);
      return plan[p - 1] > plan[best - 1] ? p : best;
    }, config.spikePositions[0]);
    return position === peak ? 'peak' : 'spike';
  }
  if (config.recoveryPositions.includes(position)) return 'recovery';
  return 'growth';
}

/** Число категорий для позиции, если явного плана нет. */
function derivedCategoryCount(
  role: LevelRole, position: number, total: number, config: BlockConfig,
): number {
  const [lo, hi] = config.categoryCorridor;
  const mid = Math.round((lo + hi) / 2);
  switch (role) {
    case 'peak': return hi;
    case 'spike': return hi - 1;
    case 'recovery': return lo;
    case 'entry': return mid;
    case 'exit': return mid;
    default: {
      // плавный подъём между передышками
      const ramp = position / total;
      return Math.min(hi - 1, Math.round(lo + (hi - lo) * ramp));
    }
  }
}

/**
 * Мета-связей для позиции, если явного плана нет.
 *
 * Держится того же потолка, что и план декады (`META_MAX_SPIKE`): было 28% от
 * числа категорий — на уровне из 16 категорий это четыре мета-пары на КАЖДОЙ
 * обычной позиции. Теперь доля 15% (две пары на типичном уровне), четвёрка
 * только на пике, передышка без мета вовсе.
 *
 * На ранней кривой (до `EARLY_CURVE_UNTIL`) потолок тот же, что у плана декады,
 * — `META_MAX_EARLY`. Иначе блок, собранный без явного мета-плана, обходил бы
 * измеренное правило и выдавал на первой сотне по три-четыре пары.
 */
function derivedMetaCount(
  role: LevelRole, categoryCount: number, config: BlockConfig, levelId: number,
): number {
  if (config.maxMetaDepth <= 0) return 0;
  const early = levelId <= EARLY_CURVE_UNTIL;
  const ordinaryCap = early ? META_MAX_EARLY : META_MAX_ORDINARY;
  const spikeCap = early ? META_MAX_EARLY : META_MAX_SPIKE;
  const dense = Math.min(ordinaryCap, Math.round(categoryCount * 0.15));
  switch (role) {
    case 'recovery': return 0;
    case 'peak': return Math.min(spikeCap, dense + 2);
    case 'spike': return Math.min(ordinaryCap, dense + 1);
    case 'entry': return Math.min(dense, 1);
    case 'exit': return dense;
    default: return dense;
  }
}

/** Глубина мета-леса: 3 — рычаг, который в оригинале включается только с L438. */
function metaDepthTarget(role: LevelRole, metaCount: number, config: BlockConfig): number {
  if (metaCount === 0) return 0;
  const cap = config.maxMetaDepth;
  if (role === 'peak') return Math.min(cap, 2);
  // ровно один уровень блока получает максимальную глубину — демонстрация рычага,
  // а не ставка на непроверенную в целевой игре механику (DECISION_LOG §9)
  if (role === 'spike') return Math.min(cap, 3);
  if (role === 'recovery') return 1;
  return Math.min(cap, metaCount >= 3 ? 2 : 1);
}

function targetDifficulty(role: LevelRole): [number, number] {
  switch (role) {
    case 'tutorial': return [1.0, 2.0];
    case 'entry': return [5.5, 6.5];
    case 'growth': return [6.0, 7.5];
    case 'recovery': return [4.0, 5.5];
    case 'peak': return [8.0, 9.0];
    case 'spike': return [7.5, 8.5];
    case 'exit': return [5.0, 6.5];
  }
}

/**
 * Целевая интересность.
 *
 * Ключевое требование: интересность обязана уметь падать, когда сложность растёт,
 * иначе это одна шкала с двумя названиями. Поэтому у передышки и выхода целевая
 * интересность ВЫШЕ, чем у пика: лёгкий уровень имеет право быть самым приятным.
 */
function targetInterest(role: LevelRole): [number, number] {
  switch (role) {
    case 'tutorial': return [6.5, 8.5];
    case 'entry': return [6.5, 8.0];
    case 'growth': return [6.0, 8.0];
    case 'recovery': return [7.0, 9.0];
    case 'peak': return [6.5, 8.0];
    case 'spike': return [6.0, 7.5];
    case 'exit': return [7.5, 9.0];
  }
}

/**
 * Игровой модификатор уровня — один на партию (GDD §7), и это акцент, а не фон.
 *
 * Раскладка по ролям, из тех же соображений, что и цепи выше: механика должна
 * подчёркивать ритм блока, а не размазываться по нему. Половинки — механика
 * «роста» (в референсе распилы видны уже на L12 и не делают уровень пиковым),
 * лёд и «?» — блокираторы для спайков, цепь-линия — самый тяжёлый, на пик.
 * Передышка, вход, выход и туториал остаются чистыми словесными уровнями:
 * игрок отдыхает от механик, а оценка D сохраняет разрешающую способность.
 * Лёд и «?» чередуются по номеру ДЕКАДЫ: спайк стоит на фиксированной позиции
 * блока, и чётность позиции дала бы один и тот же блокиратор всем декадам.
 */
function modifierFor(
  role: LevelRole, levelId: number, position: number,
  allowed: BlockConfig['allowedModifiers'],
): LevelModifier {
  // Цепь на пик ставится только если её кто-то положил в `allowedModifiers`
  // руками: лесенка декад с 04.08 цепь не выдаёт (механика нестабильна).
  if (role === 'peak' && allowed.includes('chain_line')) return 'chain_line';
  if (role === 'spike' || role === 'peak') {
    const blockers = (['ice', 'hidden'] as const).filter((m) => allowed.includes(m));
    if (blockers.length > 0) {
      return blockers[Math.floor((levelId - 1) / 10) % blockers.length];
    }
  }
  if (role === 'growth' && allowed.includes('halves') && position % 2 === 0) {
    return 'halves';
  }
  return 'none';
}

/**
 * Прибавка к бюджету ошибок на ранней кривой (решение владельца 04.08).
 *
 * Запас сверх минимума ходов — это и есть бюджет ошибок: неверный мердж тратит
 * ход. Слепой прогон 200 первых уровней показал, что на уровне роста типичный
 * игрок делает 5-15 промахов при запасе в 10 ходов, то есть проигрывает не
 * потому, что не понял уровень, а потому, что понял его со второй попытки.
 * +0.15 к K даёт растущему уровню на 9 категорий примерно четыре лишних хода.
 *
 * Это ручка ПРОЩЕНИЯ, а не понятности: путаницу в словах она не убирает (это
 * делают правило опоры и потолок мета-пар), она перестаёт наказывать за неё
 * проигрышем. Потолок `MAX_MOVE_LIMIT_K` остаётся: 1.6 наблюдался в оригинале
 * на самых просторных уровнях, выше — уже не наблюдение, а выдумка.
 */
const EARLY_MOVE_LIMIT_BONUS = 0.15;

/** K лимита ходов: чем тяжелее роль, тем теснее проход. */
function moveLimitK(role: LevelRole, levelId: number): number | null {
  const early = levelId <= EARLY_CURVE_UNTIL ? EARLY_MOVE_LIMIT_BONUS : 0;
  const withBonus = (k: number): number => Math.min(MAX_MOVE_LIMIT_K, k + early);
  switch (role) {
    case 'tutorial': return null;
    case 'recovery': return MAX_MOVE_LIMIT_K;
    case 'entry': return withBonus(1.45);
    case 'exit': return withBonus(1.5);
    case 'growth': return withBonus(1.35);
    case 'peak': return withBonus(MIN_MOVE_LIMIT_K);
    case 'spike': return withBonus(1.3);
  }
}

/**
 * Насколько роль уровня двигает цель по рангу внутри декады.
 *
 * Ранг работает той же ручкой, что и редкость: у декады есть цель, а роль
 * уровня двигает её вокруг. Передышка берёт из верха пула (слова расхожие,
 * уровень читается с ходу), пик — из низа. Ход тот же и по той же причине,
 * что у `rareTarget` выше: сложность растёт с ролью, а не с номером уровня.
 *
 * Величина 0.12 подобрана так, чтобы размах между передышкой и пиком (0.24)
 * был меньше полосы разброса по категориям (POOL_RANK_SPREAD 0.36): роль
 * смещает акцент, но не переворачивает уровень целиком.
 */
function poolRankShift(role: LevelRole): number {
  switch (role) {
    case 'tutorial': return -0.12;
    case 'recovery': return -0.12;
    case 'entry': return -0.06;
    case 'exit': return -0.03;
    case 'growth': return 0.03;
    case 'spike': return 0.09;
    case 'peak': return 0.12;
  }
}

/**
 * Режим картинки для позиции блока.
 *
 * Картинка живёт НА мета-пузыре, поэтому уровень без мета-пар нести её не может
 * физически: требование на таком уровне не отказ генератора, а бессмыслица в
 * плане, и оно превращается в `auto`. Запрет наоборот действует всегда — он
 * ничего не требует от материала.
 */
function iconModeFor(
  choice: 0 | 1 | null, metaCount: number, isTutorial: boolean,
): 'auto' | 'require' | 'forbid' {
  if (choice === 0) return 'forbid';
  if (isTutorial || metaCount === 0) return 'auto';
  return choice === 1 ? 'require' : 'auto';
}

export function buildBlockPlan(config: BlockConfig): LevelPlan[] {
  const [from, to] = config.levelRange;
  const total = to - from + 1;
  const [rareLo, rareHi] = config.rarityRange;
  // туториал: первый уровень игры вообще. 5 категорий, весь уровень на поле,
  // лимита ходов нет, мета и модификаторы запрещены (референс L1)
  const tutorial = config.decadeGates?.tutorialFirstLevel === true && from === 1;

  const plans: LevelPlan[] = [];
  for (let position = 1; position <= total; position += 1) {
    const levelId = from + position - 1;
    const role = roleFor(position, total, config);
    const isTutorial = tutorial && position === 1;
    const categoryCount = config.categoryPlan?.[position - 1]
      ?? derivedCategoryCount(role, position, total, config);
    const metaCount = isTutorial ? 0 : (config.metaPlan?.[position - 1]
      ?? derivedMetaCount(role, categoryCount, config, levelId));

    // редкость — единственный признак референса, который рос до самого конца
    // и не разворачивался; растим её вместе с ролью, а не с номером уровня
    const load = role === 'peak' ? 1 : role === 'spike' ? 0.9
      : role === 'recovery' ? 0.15 : role === 'growth' ? 0.6 : 0.3;
    const rareTarget = Math.round(rareLo + (rareHi - rareLo) * load);

    const trapTarget = isTutorial ? 0
      : role === 'recovery' ? 0
      : role === 'peak' ? 2 : role === 'spike' ? 2 : 1;

    // Модификатор — акцент, а не фон: цепи ставятся только на пики. Когда они
    // стояли на каждом уровне роста, верх шкалы сложности схлопывался (четыре
    // уровня подряд упирались в 9.5-10) и терялась разрешающая способность.
    const chainCount = config.allowedModifiers.includes('chains') && !isTutorial
      ? (role === 'peak' ? 2 : role === 'spike' ? 1 : 0)
      : 0;

    // Явный выбор человека сильнее лесенки по декадам: `null` в плане означает
    // «решай сам», значение — «поставь ровно это». Туториал исключений не знает.
    const modifier = isTutorial ? 'none'
      : (config.modifierPlan?.[position - 1]
        ?? modifierFor(role, levelId, position, config.allowedModifiers));

    plans.push({
      levelId,
      position,
      role: isTutorial ? 'tutorial' : role,
      categoryCount,
      metaCount: Math.min(metaCount, categoryCount - 1),
      metaDepthTarget: isTutorial ? 0 : metaDepthTarget(role, metaCount, config),
      rareTarget: isTutorial ? 0 : rareTarget,
      trapTarget,
      chainCount,
      modifier,
      targetDifficulty: isTutorial ? [1.0, 2.0] : targetDifficulty(role),
      targetInterest: isTutorial ? [6.5, 8.5] : targetInterest(role),
      // лимита ходов на туториале нет: в референсе L1 без лимита, поле держит
      // весь уровень целиком, игрока учат только драгу
      moveLimitK: isTutorial ? null : moveLimitK(role, levelId),
      poolRankTarget: config.decadeGates?.poolRankTarget === undefined
        || config.decadeGates.poolRankTarget === null
        ? null
        : Math.min(1, Math.max(0, config.decadeGates.poolRankTarget
          + poolRankShift(isTutorial ? 'tutorial' : role))),
      // Категория-картинка. Явный выбор человека сильнее доли: 1 — уровень
      // обязан её получить, 0 — картинок нет. Без плана режим `auto`, то есть
      // ровно прежнее поведение. Уровень без мета-пар картинку нести не может
      // по построению, поэтому требование на нём молча становится `auto`.
      iconMode: iconModeFor(config.iconPlan?.[position - 1] ?? null, metaCount, isTutorial),
    });
  }
  return plans;
}

/**
 * Инварианты блока: пила, а не линия.
 * Проверяются на плане, до генерации: если план плохой, генерировать бессмысленно.
 */
export function checkBlockRhythm(
  plans: LevelPlan[],
): { passed: boolean; issues: string[] } {
  const issues: string[] = [];
  const counts = plans.map((p) => p.categoryCount);

  const descents = counts.slice(1).filter((c, i) => c < counts[i]).length;
  if (descents < 3) {
    issues.push(`переходов вниз ${descents}, нужно минимум 3: блок читается как прямая линия, `
      + 'а по замеру 37% уровней проще предыдущего');
  }

  /**
   * Разброса макс-мин здесь больше нет (решение владельца 04.08, вечер:
   * «это требование не нужно», оранжевая строка про разбросы путала и мешала).
   *
   * Требование стояло по замеру референса (5-7 категорий внутри декады), но
   * работало против человека: разброс — следствие коридора, а не выбор
   * дизайнера, и планировщик уже раздвигает спайк с передышкой на всю ширину
   * коридора (`spreadBoundsFor` в decadeProfiles.ts, там оно и осталось). Форму
   * кривой проверяют переходы вниз и передышка после спайка — ниже.
   */
  const peaks = plans.filter((p) => p.role === 'peak' || p.role === 'spike');
  if (peaks.length < 1) issues.push('нет ни одного выраженного пика');

  /**
   * Передышка гарантируется только после позиции 5 — это единственная фигура,
   * устойчивая в референсе (16 декад из 19 идут вниз именно на позиции 6).
   * Требовать провал после КАЖДОГО пика было ошибкой: позиция 10 в референсе,
   * наоборот, самая нагруженная после спайка (1.07 от средней декады).
   */
  const mainSpike = plans.find((p) => p.position === 5);
  const afterSpike = plans.find((p) => p.position === 6);
  if (mainSpike && afterSpike && afterSpike.categoryCount >= mainSpike.categoryCount) {
    issues.push('после спайка на позиции 5 нет передышки: '
      + `уровень ${afterSpike.levelId} не проще уровня ${mainSpike.levelId}`);
  }

  for (let i = 1; i < plans.length; i += 1) {
    const a = plans[i - 1];
    const b = plans[i];
    if (a.categoryCount === b.categoryCount && a.metaCount === b.metaCount) {
      issues.push(`уровни ${a.levelId} и ${b.levelId} структурно одинаковы`);
    }
  }

  return { passed: issues.length === 0, issues };
}
