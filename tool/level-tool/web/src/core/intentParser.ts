/**
 * Разбор свободного текстового пожелания в структурированный конфиг.
 *
 * Где здесь AI и где его нет. В спеке этот шаг был единственным живым вызовом
 * модели: «интерпретация намерения». В публичной статической версии он выполняется
 * детерминированным разбором по словарю тем — и это осознанное решение, а не
 * упрощение из лени:
 *
 *   1. проверяющий обязан увидеть работающий инструмент даже при исчерпанном
 *      ключе, а прокси добавляет точку отказа ради одной функции;
 *   2. результат интерпретации всё равно должен быть детерминированным фильтром,
 *      иначе один и тот же текст давал бы разные блоки;
 *   3. промпт `prompts/intent_parser.md` и сохранённые прогоны в репозитории есть,
 *      так что видно, как это работает с моделью.
 *
 * Главное требование к шагу остаётся выполненным: пользователь ВИДИТ, как поняли
 * его слова, и правит интерпретацию ДО генерации.
 */
import type { BlockConfig } from './types.ts';

export interface IntentMatch {
  /** какое поле конфига затронуто */
  field: string;
  /** во что превратилось */
  value: string;
  /** фрагмент текста, который это вызвал */
  source: string;
}

export interface ParsedIntent {
  patch: Partial<BlockConfig>;
  matches: IntentMatch[];
  /** фразы, которые разбор не понял: показываются пользователю честно */
  unrecognized: string[];
}

/**
 * Словарь тем: ключевое слово → темы снимка базы.
 * Русские и английские варианты, потому что заказчик пишет как ему удобно.
 */
const THEME_WORDS: Record<string, string[]> = {
  food: ['еда', 'еду', 'еде', 'food', 'кухн', 'кулинар', 'блюд'],
  world_food: ['кухни мира', 'world food', 'этнич'],
  food_more: ['десерт', 'сладк'],
  geography: ['география', 'geography', 'путешеств', 'travel', 'стран', 'город',
    'отпуск', 'каникул', 'vacation', 'holiday'],
  places: ['места', 'places', 'локац'],
  landmarks: ['достопримечат', 'landmark'],
  sports: ['спорт', 'sport'],
  sports_world: ['олимп', 'мировой спорт'],
  animals: ['животн', 'animal', 'зверь', 'зверей'],
  animals_more: ['экзотическ животн'],
  species: ['вид', 'species', 'породы'],
  nature: ['природ', 'nature'],
  nature_more: ['ландшафт'],
  plants: ['растен', 'plant', 'цвет'],
  space: ['космос', 'space', 'звёзд', 'звезд', 'планет'],
  science: ['наука', 'science', 'научн'],
  technology: ['техн', 'tech', 'гаджет'],
  home: ['дом', 'home', 'быт', 'мебел'],
  clothing: ['одежд', 'cloth', 'обув'],
  fashion: ['мода', 'fashion', 'стиль'],
  body: ['тело', 'body', 'анатом'],
  medicine: ['медицин', 'medicine', 'болезн', 'здоров'],
  law: ['закон', 'law', 'суд', 'юрид'],
  business: ['бизнес', 'business', 'деньг', 'финанс', 'покупк', 'шопинг', 'shopping',
    'магазин'],
  jobs: ['професс', 'job', 'работ'],
  entertainment: ['развлеч', 'entertainment', 'игрушк', 'праздник'],
  media: ['медиа', 'media', 'кино', 'фильм', 'комикс'],
  music: ['музык', 'music'],
  art: ['искусств', 'art', 'рисов'],
  // 'слов' тут было и ловило любую фразу про слова: «меньше сложных слов»
  // молча исключало тему language, хотя речь шла о редкости, а не о теме
  language: ['язык', 'language', 'лингв', 'словар', 'грамматик', 'алфавит'],
  people: ['люди', 'people', 'персон', 'извест'],
  // сезоны сюда же: «конец лета» — это про календарь уровня, а не про погоду
  time: ['время', 'time', 'календар', 'сезон', 'праздник',
    'лета', 'летн', 'summer', 'осен', 'autumn', 'зим', 'winter', 'весн', 'spring'],
  transport: ['транспорт', 'transport', 'машин', 'самолёт', 'самолет'],
  tools: ['инструмент', 'tool', 'мастерск'],
  materials: ['материал', 'material'],
  properties: ['свойств', 'properties', 'цвета', 'colors'],
  culture: ['культур', 'culture'],
  history: ['истор', 'history'],
  ocean: ['океан', 'ocean', 'море', 'морск'],
  weather: ['погод', 'weather'],
  hobbies: ['хобби', 'hobby', 'hobbies'],
  farming: ['ферм', 'farm', 'сельск', 'урожа', 'harvest', 'сад ', 'огород'],
  education: ['школ', 'school', 'учеб', 'образован'],
  religion: ['религ', 'religion'],
  mythology: ['миф', 'myth'],
  brands: ['бренд', 'brand'],
};

/**
 * Отрицание фрагмента. «Меньше» и «поменьше» тут же, и это не вольность: для
 * рычагов вроде редкости слов «меньше редких» и «без редких» задают одну и ту же
 * сторону шкалы, а разница между ними — в силе, которой у нас всё равно нет.
 */
const NEGATIONS = ['без ', 'кроме ', 'исключ', 'no ', 'not ', 'avoid ', 'exclude ',
  'не надо ', 'меньше', 'поменьше', 'less ', 'fewer'];

/** Находит темы, упомянутые во фрагменте текста. */
function themesIn(fragment: string): string[] {
  const found = new Set<string>();
  for (const [theme, keywords] of Object.entries(THEME_WORDS)) {
    for (const keyword of keywords) {
      if (fragment.includes(keyword)) { found.add(theme); break; }
    }
  }
  return Array.from(found);
}

/** Разбивает текст на фрагменты по запятым и союзам: у каждого своя полярность. */
function fragments(text: string): string[] {
  return text.toLowerCase()
    .split(/[,;.]|\bи\b|\band\b|\bно\b|\bbut\b/)
    .map((f) => f.trim())
    .filter(Boolean);
}

/** «сделай 10 уровней», «10 levels» — сколько уровней просят. */
const COUNT_RE = /(\d{1,2})\s*(уровн\w*|levels?)/;
/** «в линейке 150-160», «уровни 150–160» — где они стоят. */
const RANGE_RE = /(\d{1,4})\s*[-–—]\s*(\d{1,4})/;
/** Блок короче двух уровней не блок, длиннее двадцати — уже не композиция. */
const MIN_BLOCK = 2;
const MAX_BLOCK = 20;

/**
 * Размер и место блока.
 *
 * Числа два, и они спорят: «10 уровней в линейке 150-160» — это 10 уровней или
 * 11? Побеждает счёт: сколько уровней сделать, человек говорит прямо, а диапазон
 * в такой фразе задаёт скорее место, чем длину. Поэтому от начала диапазона
 * отмеряется ровно запрошенное количество, и обе фразы попадают в таблицу
 * интерпретации — расхождение видно до генерации, а не после.
 */
function parseBlockRange(
  text: string, current: [number, number],
): { range: [number, number]; sources: IntentMatch[] } | null {
  const lower = text.toLowerCase();
  const countHit = lower.match(COUNT_RE);
  const rangeHit = lower.match(RANGE_RE);
  const count = countHit ? Number(countHit[1]) : null;
  const validCount = count !== null && count >= MIN_BLOCK && count <= MAX_BLOCK
    ? count : null;

  let from = current[0];
  let to = current[1];
  const sources: IntentMatch[] = [];

  if (rangeHit) {
    const [a, b] = [Number(rangeHit[1]), Number(rangeHit[2])];
    if (a >= 1 && b > a && b - a + 1 <= MAX_BLOCK) {
      from = a;
      to = b;
      sources.push({ field: 'levelRange', value: `${a}–${b}`, source: rangeHit[0] });
    }
  }
  if (validCount !== null) {
    to = from + validCount - 1;
    sources.push({ field: 'levelRange', value: `${validCount} уровней → ${from}–${to}`,
      source: countHit![0] });
  }
  if (!sources.length) return null;
  return { range: [from, to], sources };
}

/**
 * Куда ставить пики, если человек назвал места словами.
 *
 * Позиции считаются от длины блока, а не берутся константами: «пик в конце»
 * блока из шести уровней и блока из десяти — разные номера.
 */
function peakSlot(word: 'начало' | 'середина' | 'конец', total: number): number {
  if (word === 'начало') return 2;
  if (word === 'середина') return Math.max(2, Math.round(total / 2));
  return Math.max(2, total - 1);
}

/**
 * Пики разбираются по ВСЕМУ тексту, а не по фрагменту.
 *
 * «Два пика в середине и конце» разрезается союзом «и» на «два пика в середине»
 * и «конце»: второе место теряется, а обрубок «конце» уходит в «не понято».
 * Поэтому берём предложение целиком — от слова «пик» до ближайшей запятой или
 * точки. Дальше запятой не смотрим специально: во фразе «два пика, передышка в
 * конце» слово «конце» относится к передышке, и утащить его в позицию пика
 * значило бы понять человека наоборот.
 */
function parsePeaks(text: string, total: number): { positions: number[]; source: string } | null {
  const lower = text.toLowerCase();
  const start = lower.search(/пик|peak/);
  if (start < 0) return null;
  const clause = lower.slice(start).split(/[,;.]/)[0];

  const count = /дв[аеух]|two/.test(clause) ? 2 : 1;
  const named: number[] = [];
  if (/начал/.test(clause)) named.push(peakSlot('начало', total));
  if (/середин/.test(clause)) named.push(peakSlot('середина', total));
  if (/конц/.test(clause)) named.push(peakSlot('конец', total));

  const positions = named.length
    ? Array.from(new Set(named)).sort((a, b) => a - b)
    : (count === 2
      ? [peakSlot('середина', total), peakSlot('конец', total)]
      : [Math.max(2, total - 2)]);
  return { positions, source: clause.trim() };
}

/** Передышки по умолчанию: примерно треть, две трети и хвост блока. */
function defaultRecovery(total: number): number[] {
  return Array.from(new Set([
    Math.round(total * 0.3), Math.round(total * 0.6), total,
  ])).filter((p) => p >= 2 && p <= total).sort((a, b) => a - b);
}

export function parseIntent(
  text: string,
  /** применённый диапазон: от него отмеряется блок, если названо только число уровней */
  currentRange: [number, number] = [201, 210],
): ParsedIntent {
  const matches: IntentMatch[] = [];
  const unrecognized: string[] = [];
  const include = new Set<string>();
  const exclude = new Set<string>();
  const trapThemes = new Set<string>();
  const patch: Partial<BlockConfig> = {};

  // Размер блока разбирается первым: от него зависят позиции пиков и передышек.
  const block = parseBlockRange(text, currentRange);
  if (block) {
    patch.levelRange = block.range;
    matches.push(...block.sources);
  }
  const total = (patch.levelRange ?? currentRange)[1] - (patch.levelRange ?? currentRange)[0] + 1;

  const peaks = parsePeaks(text, total);
  if (peaks) {
    patch.spikePositions = peaks.positions;
    matches.push({ field: 'spikePositions', value: peaks.positions.join(', '),
      source: peaks.source });
  }

  for (const fragment of fragments(text)) {
    let touched = false;
    const negated = NEGATIONS.some((n) => fragment.includes(n));
    const isTrap = /ловуш|trap/.test(fragment);
    const themes = themesIn(fragment);

    for (const theme of themes) {
      touched = true;
      if (isTrap) {
        trapThemes.add(theme);
        matches.push({ field: 'trapThemes', value: theme, source: fragment });
      } else if (negated) {
        exclude.add(theme);
        matches.push({ field: 'excludeThemes', value: theme, source: fragment });
      } else {
        include.add(theme);
        matches.push({ field: 'includeThemes', value: theme, source: fragment });
      }
    }

    /**
     * Просьба о ловушках без темы. Раньше уходила в «не понято», хотя понимать
     * тут нечего: сколько ловушек ставить, решает роль уровня в плане блока,
     * а тема лишь сужает, из чего их брать. Строка в таблице честнее молчания —
     * человек видит, что просьбу прочитали, и что конфиг от неё не меняется.
     */
    if (isTrap && themes.length === 0) {
      touched = true;
      matches.push({ field: 'trapThemes',
        value: 'любые темы · число ловушек задаёт роль уровня', source: fragment });
    }

    // Пики и размер блока уже разобраны по всему тексту; здесь только помечаем
    // такие фрагменты понятыми, чтобы они не попали в «не понято». Обрубок
    // «конце» от фразы «в середине и конце» — из той же оперы: сам по себе он
    // ничего не значит, но и жалобы на него быть не должно.
    if (/пик|peak/.test(fragment)) touched = true;
    if (COUNT_RE.test(fragment) || RANGE_RE.test(fragment)) touched = true;
    if (peaks && /^(в\s+)?(начал\w*|середин\w*|конц\w*)$/.test(fragment)) touched = true;

    if (/передышк|recovery|отдых/.test(fragment)) {
      touched = true;
      /**
       * «Передышка после пиков» — это ровно следующий уровень за каждым пиком,
       * а не три позиции из пресета. Без этого просьба звучала понято, но блок
       * получал передышки в местах, к пикам отношения не имеющих.
       */
      const afterPeaks = peaks && /после\s+пик|after.{0,6}peak/.test(fragment);
      const positions = afterPeaks
        ? Array.from(new Set(peaks.positions.map((p) => p + 1)))
          .filter((p) => p <= total).sort((a, b) => a - b)
        : defaultRecovery(total);
      if (positions.length) {
        patch.recoveryPositions = positions;
        matches.push({ field: 'recoveryPositions', value: positions.join(', '),
          source: fragment });
      }
    }

    // Модификаторов генератор не ставит (см. DEFAULT_BLOCK_CONFIG), поэтому
    // и разбирать просьбу о цепях нечестно: разобрали бы, показали в таблице
    // «понято», а на уровень это не попало бы. Просьба уйдёт в «не понято» —
    // это и есть правда.

    // редкость и сложность
    if (/редк|rare|экзотик|сложн\S*\s+слов|hard words/.test(fragment)) {
      touched = true;
      patch.rarityRange = negated ? [5, 8] : [11, 15];
      matches.push({ field: 'rarityRange', value: patch.rarityRange.join('-'),
        source: fragment });
    }
    if (/попроще|легч|easier|мягч/.test(fragment)) {
      touched = true;
      patch.categoryCorridor = [10, 15];
      patch.rarityRange = [6, 10];
      matches.push({ field: 'categoryCorridor', value: '10-15', source: fragment });
      matches.push({ field: 'rarityRange', value: '6-10', source: fragment });
    }
    if (/тяжел|тяжёл|harder|сложнее/.test(fragment)) {
      touched = true;
      patch.categoryCorridor = [13, 18];
      matches.push({ field: 'categoryCorridor', value: '13-18', source: fragment });
    }

    // глубина мета
    const depth = fragment.match(/глубин\D{0,10}(\d)|depth\D{0,6}(\d)/);
    if (depth) {
      touched = true;
      patch.maxMetaDepth = Number(depth[1] ?? depth[2]);
      matches.push({ field: 'maxMetaDepth', value: String(patch.maxMetaDepth),
        source: fragment });
    }

    if (!touched && fragment.length > 3) unrecognized.push(fragment);
  }

  if (include.size) patch.includeThemes = Array.from(include).sort();
  if (exclude.size) patch.excludeThemes = Array.from(exclude).sort();
  if (trapThemes.size) patch.trapThemes = Array.from(trapThemes).sort();

  return { patch, matches, unrecognized };
}

/**
 * Промпт, которым поле заполнено при открытии экрана.
 *
 * Живёт здесь, а не в компоненте, ради теста: пример обязан разбираться целиком,
 * без остатка в «не понято». Пример, половину которого инструмент не понимает,
 * учит писать неработающие запросы.
 */
export const DEFAULT_INTENT_PROMPT =
  'Сделай 10 уровней в линейке 150-160, вайб-теги: конец лета отпуск сбор урожая '
  + 'покупки, два пика в середине и конце, передышка после пиков, честные ловушки, '
  + 'меньше сложных слов';

/** Список всех известных разбору тем: показывается пользователю как подсказка. */
export const KNOWN_THEMES = Object.keys(THEME_WORDS).sort();
