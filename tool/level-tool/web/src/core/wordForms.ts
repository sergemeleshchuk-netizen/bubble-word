/**
 * Формы слов и имён: что игрок прочитает как «одно и то же».
 *
 * Один модуль на генератор и приёмку сознательно. До 04.08 правило двойников
 * жило в двух копиях — в `generator.ts` и в правиле `NEAR_DUPLICATE_WORDS`, — и
 * копии успели разойтись: генератор знал про `city` → `cities`, приёмка нет.
 * То есть приёмка пропускала пару, которую генератор считал недопустимой.
 */

/**
 * Слова-двойники: `star` и `stars`, `bird` и `birds`, `city` и `cities`.
 * Формально это разные слова, но на поле рядом они читаются как ошибка данных.
 *
 * Проверять их нужно по всему уровню, а не внутри категории (04.08). Внутри
 * категории двойники были только некрасивы; в РАЗНЫХ категориях одного уровня
 * они делают уровень нечестным: владелец собрал поле, где `borders` жил в MAP,
 * а `border` — в MAP WORDS. У каждого слова один дом, решение единственное,
 * приёмка PASS — а играющий человек различить их не может и теряет ход на
 * угадывании.
 */
export function isNearDuplicate(a: string, b: string): boolean {
  if (a === b) return true;
  const [short, long] = a.length <= b.length ? [a, b] : [b, a];
  if (long === `${short}s` || long === `${short}es`) return true;
  if (short.endsWith('y') && long === `${short.slice(0, -1)}ies`) return true;
  return false;
}

/**
 * Все написания, которые `isNearDuplicate` считает тем же словом.
 *
 * Нужны, чтобы спрашивать «есть ли двойник на уровне» одним поиском по
 * множеству, а не перебором всех слов поля: проверка стоит внутри перебора
 * решателя, и на декадах с 12+ категориями пересборка списка на каждый вызов
 * стоила вчетверо больше времени, чем вся остальная сборка уровня.
 *
 * Набор обязан совпадать с `isNearDuplicate` пара-в-пару — это проверяется
 * тестом `wordForms`, иначе генератор и приёмка разошлись бы снова.
 */
export function nearDuplicateForms(n: string): string[] {
  const out = [n, `${n}s`, `${n}es`];
  if (n.endsWith('es')) out.push(n.slice(0, -2));
  if (n.endsWith('s')) out.push(n.slice(0, -1));
  if (n.endsWith('ies')) out.push(`${n.slice(0, -3)}y`);
  if (n.endsWith('y')) out.push(`${n.slice(0, -1)}ies`);
  return out;
}

/**
 * Слова подписи категории: «MAP WORDS» → ['map', 'words'].
 *
 * Сравниваются именно подписи, а не ключи базы: игрок читает подпись, и она с
 * ключом расходится — категория `national_parks` подписана «PARK WORDS».
 */
export function labelTokens(label: string): string[] {
  let cached = tokenCache.get(label);
  if (!cached) {
    cached = label.toLowerCase().replace(/[-/]/g, ' ').split(/\s+/).filter(Boolean);
    tokenCache.set(label, cached);
  }
  return cached;
}

/**
 * Разбор подписи кешируется: `namesTooClose` вызывается на каждой паре категорий
 * пула при отборе уровня, а подписей в базе всего 6685 — разбирать одну и ту же
 * строку заново десятки тысяч раз не за что платить. Кеш только читает свои же
 * входные строки, поэтому результат от него не зависит.
 */
const tokenCache = new Map<string, string[]>();

/**
 * Имя одной категории целиком входит в имя другой: MAP и MAP WORDS, CHESS и
 * CHESS TERMS, BIRDS и BIRDS OF PREY, COUNTRIES и ISLAND COUNTRIES. Такую пару
 * нельзя ставить на одно поле.
 *
 * Почему проверки пересечения пулов (`pairSeparable` по Жаккару) для этого не
 * хватает: у MAP и MAP WORDS в базе НОЛЬ общих слов — просто потому, что
 * `border` никто не разметил в MAP, а `borders` в MAP WORDS. Пересечение пулов
 * измеряет полноту разметки; смысл выдаёт имя. Игроку же очевидно, что слово,
 * годное для «карты», годится и для «слов про карту», — и он угадывает вместо
 * того, чтобы думать.
 *
 * Токены сверяются через `isNearDuplicate`, иначе BIRD и BIRDS OF PREY считались
 * бы разными именами из-за одной буквы.
 *
 * Общее слово в двух длинных именах парой не делает: MAP WORDS и PARK WORDS
 * остаются разрешёнными — совпадает только родовое «words», а полного вхождения
 * нет. Отсекается ровно вложенность: {map} ⊂ {map, words}.
 */
export function namesTooClose(a: string, b: string): boolean {
  const ta = labelTokens(a);
  const tb = labelTokens(b);
  if (ta.length === 0 || tb.length === 0) return false;
  const [small, big] = ta.length <= tb.length ? [ta, tb] : [tb, ta];
  return small.every((t) => big.some((o) => isNearDuplicate(t, o)));
}
