/**
 * Разбор того, что человек набрал в поле настройки блока.
 *
 * Вынесено из компонента ради одного свойства: «набрано наполовину» и
 * «набрано неверно» — разные вещи, и различать их обязано что-то проверяемое
 * тестом, а не выражение внутри JSX.
 *
 * Правило у всех функций одно: `null` означает «пока не разобралось, в конфиг
 * не отдаём». Это НЕ ошибка ввода — так выглядит любое поле в середине набора.
 */

/** Числа из строки в порядке появления. Разделитель любой нечисловой. */
export function parseNumberList(raw: string): number[] {
  return raw.split(/[^0-9]+/).filter(Boolean).map(Number);
}

/**
 * Диапазон «от–до». Требует ровно два числа и осмысленный порядок.
 *
 * Порядок проверяется не из педантизма: набирая «10–14» поверх «7–9», человек
 * неизбежно проходит через «10–1». Без проверки это ушло бы в конфиг как
 * диапазон уровней 10..1, и профиль декады пересобрался бы от мусора.
 */
export function parseRange(raw: string, min = 0): [number, number] | null {
  const values = parseNumberList(raw);
  if (values.length !== 2) return null;
  const [from, to] = values;
  if (from < min || to < from) return null;
  return [from, to];
}

/** Одно целое число в границах. Пустое поле — `null`, а не ноль. */
export function parseCount(raw: string, min: number, max: number): number | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;
  if (!/^\d+$/.test(trimmed)) return null;
  const value = Number(trimmed);
  if (value < min || value > max) return null;
  return value;
}

/**
 * Необязательный список: пустое поле означает «плана нет» (`undefined`),
 * а не «план из нуля уровней». Разница существенная — генератор без плана
 * берёт коридор, а план нулевой длины сломал бы разметку блока.
 */
export function parseOptionalList(raw: string): number[] | undefined {
  const values = parseNumberList(raw);
  return values.length ? values : undefined;
}
