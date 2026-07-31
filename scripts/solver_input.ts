/**
 * Готовит слепой вход для независимого решателя.
 *
 * Решатель обязан быть слепым: он получает только то, что видит игрок, и ничего
 * больше — никакого доступа к файлам уровня, базе и правильным ответам. Иначе
 * это не проверка, а самообман. Перемешивание детерминированное: один и тот же
 * уровень даёт один и тот же вход, поэтому прогоны сравнимы между собой.
 *
 *   node scripts/solver_input.ts --level 205 [--mode A|B] [--pack data/final-pack]
 */
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRng } from '../web/src/core/rng.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const arg = (name: string, fallback?: string) => {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : fallback;
};

const levelId = arg('level');
const mode = (arg('mode', 'B') ?? 'B').toUpperCase();
const packDir = arg('pack', 'data/final-pack')!;
if (!levelId) {
  console.error('нужен --level NNN');
  process.exit(1);
}

const payload = JSON.parse(readFileSync(
  join(ROOT, packDir, `level-${levelId}.json`), 'utf8'));
const spec = payload.level_spec;

const rng = createRng(`solver|${levelId}|${mode}`);
const words: string[] = rng.shuffle<string>(
  spec.categories.flatMap((c: any) => c.words.map((w: any) => String(w.text))));
const labels: string[] = rng.shuffle<string>(
  spec.categories.map((c: any) => String(c.label)));

console.log(`# Слепой вход, уровень ${spec.levelId}, режим ${mode}`);
console.log(`# Слов: ${words.length}, категорий: ${spec.categories.length}`);
console.log(`# Перемешивание: seed solver|${levelId}|${mode} — воспроизводимо`);
console.log('');
if (mode === 'A') {
  console.log('Категории:');
  for (const label of labels) console.log(`  ${label}`);
  console.log('');
}
console.log('Слова:');
console.log(words.map((w) => `  ${w}`).join('\n'));
console.log('');
console.log('# Ответ ожидается в формате из prompts/blind_solver.md');
