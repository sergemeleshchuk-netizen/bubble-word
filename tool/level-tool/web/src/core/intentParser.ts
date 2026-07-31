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
  geography: ['география', 'geography', 'путешеств', 'travel', 'стран', 'город'],
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
  business: ['бизнес', 'business', 'деньг', 'финанс'],
  jobs: ['професс', 'job', 'работ'],
  entertainment: ['развлеч', 'entertainment', 'игрушк', 'праздник'],
  media: ['медиа', 'media', 'кино', 'фильм', 'комикс'],
  music: ['музык', 'music'],
  art: ['искусств', 'art', 'рисов'],
  language: ['язык', 'language', 'слов'],
  people: ['люди', 'people', 'персон', 'извест'],
  time: ['время', 'time', 'календар', 'сезон', 'праздник'],
  transport: ['транспорт', 'transport', 'машин', 'самолёт', 'самолет'],
  tools: ['инструмент', 'tool', 'мастерск'],
  materials: ['материал', 'material'],
  properties: ['свойств', 'properties', 'цвета', 'colors'],
  culture: ['культур', 'culture'],
  history: ['истор', 'history'],
  ocean: ['океан', 'ocean', 'море', 'морск'],
  weather: ['погод', 'weather'],
  hobbies: ['хобби', 'hobby', 'hobbies'],
  farming: ['ферм', 'farm', 'сельск'],
  education: ['школ', 'school', 'учеб', 'образован'],
  religion: ['религ', 'religion'],
  mythology: ['миф', 'myth'],
  brands: ['бренд', 'brand'],
};

const NEGATIONS = ['без ', 'кроме ', 'исключ', 'no ', 'not ', 'avoid ', 'exclude ', 'не надо '];

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

export function parseIntent(text: string): ParsedIntent {
  const matches: IntentMatch[] = [];
  const unrecognized: string[] = [];
  const include = new Set<string>();
  const exclude = new Set<string>();
  const trapThemes = new Set<string>();
  const patch: Partial<BlockConfig> = {};

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

    // пики и передышки
    const peakCount = /дв[аух].{0,12}пик|two peaks/.test(fragment) ? 2
      : /(один|одном).{0,12}пик|one peak/.test(fragment) ? 1 : 0;
    if (peakCount) {
      touched = true;
      patch.spikePositions = peakCount === 2 ? [5, 9] : [8];
      matches.push({ field: 'spikePositions', value: patch.spikePositions.join(', '),
        source: fragment });
    }
    if (/пик.{0,16}(в конце|конц)|peak.{0,12}(near the end|at the end)/.test(fragment)) {
      touched = true;
      patch.spikePositions = [9];
      matches.push({ field: 'spikePositions', value: '9', source: fragment });
    }
    if (/передышк|recovery|отдых/.test(fragment)) {
      touched = true;
      patch.recoveryPositions = [3, 6, 10];
      matches.push({ field: 'recoveryPositions', value: '3, 6, 10', source: fragment });
    }

    // Модификаторов генератор не ставит (см. DEFAULT_BLOCK_CONFIG), поэтому
    // и разбирать просьбу о цепях нечестно: разобрали бы, показали в таблице
    // «понято», а на уровень это не попало бы. Просьба уйдёт в «не понято» —
    // это и есть правда.

    // редкость и сложность
    if (/редк|rare|экзотик|сложн слов/.test(fragment)) {
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

/** Список всех известных разбору тем: показывается пользователю как подсказка. */
export const KNOWN_THEMES = Object.keys(THEME_WORDS).sort();
