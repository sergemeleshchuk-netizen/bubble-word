/**
 * Пересчёт оценок сданного блока под текущую модель — без пересборки уровней.
 *
 * Зачем отдельный скрипт. Когда модель сложности меняется, у сданных пакетов
 * есть только два честных пути: пересобрать их заново или пересчитать оценки
 * на месте. Пересборка не годится — снимок контента с тех пор менялся, и тот же
 * конфиг даёт уже другие уровни (это зафиксировано в `tests/decade.test.ts`).
 * Значит, уровни остаются ровно те, что сдали, а меняются только числа.
 *
 * Работает это потому, что `level-N.json` несёт полный `level_spec`, а
 * `computeDifficulty` — чистая функция от спека и конфига: `index` в ней не
 * используется, а `solutions` влияет только на нерешаемые и двусмысленные
 * уровни, которых в сданном пакете нет по построению (экспорт их не выпускает).
 *
 * Что НЕ пересчитывается: `pack_hash` и `level_spec_hash`. Они про уровень, а не
 * про его оценку; версия модели в них не входит и входить не должна — иначе
 * правка веса ломала бы регрессию по сданным пакетам.
 *
 * Использование:
 *   npx tsx scripts/rescore_block.ts ../../levels/packs/floor375-ten
 *   npx tsx scripts/rescore_block.ts ../../levels/packs/floor375-ten --write
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { computeDifficulty, difficultyTier } from '../web/src/core/scoringDifficulty.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import type { LevelSpec } from '../web/src/core/types.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const [dirArg, ...flags] = process.argv.slice(2);
if (!dirArg) {
  console.error('нужен путь к каталогу блока (там, где лежат level-N.json)');
  process.exit(2);
}
const write = flags.includes('--write');
const dir = resolve(process.cwd(), dirArg);

const files = readdirSync(dir)
  .filter((f) => /^level-\d+\.json$/.test(f))
  .sort((a, b) => Number(a.match(/\d+/)![0]) - Number(b.match(/\d+/)![0]));

if (!files.length) {
  console.error(`в ${dir} нет файлов level-N.json`);
  process.exit(2);
}

let changed = 0;
console.log(`${dir}\nмодель: ${scoring.scoring_version}\n`);
console.log('  ур.   было   стало   сдвиг   ярус');

for (const file of files) {
  const path = join(dir, file);
  const body = JSON.parse(readFileSync(path, 'utf8'));
  const spec = body.level_spec as LevelSpec;
  const before = body.scoring.difficulty as number;

  // solutions = 1: сданный уровень по построению имеет ровно одно решение,
  // иначе он не прошёл бы экспорт. Передаём явно, чтобы не менять ветку.
  const d = computeDifficulty(spec, null as never, scoring, { count: 1 } as never, {});

  const shift = Math.round((d.value - before) * 100) / 100;
  const tierBefore = body.scoring.difficulty_tier ?? difficultyTier(before);
  const tierAfter = difficultyTier(d.value);
  const tierNote = tierBefore === tierAfter ? tierAfter : `${tierBefore} → ${tierAfter}`;
  console.log(`  ${String(spec.levelId).padStart(4)}  ${before.toFixed(1).padStart(5)}`
    + `  ${d.value.toFixed(1).padStart(6)}  ${(shift >= 0 ? '+' : '') + shift.toFixed(2)}`.padEnd(9)
    + `  ${tierNote}`);
  if (shift !== 0) changed += 1;

  if (!write) continue;
  body.scoring.difficulty = d.value;
  body.scoring.difficulty_tier = tierAfter;
  body.scoring.difficulty_breakdown = {
    base_calibrated: d.base,
    declared_not_calibrated: d.declared,
    semantic: d.semantic,
    mechanical: d.mechanical,
    totals: {
      base: d.baseTotal, declared: d.declaredTotal,
      semantic: d.semanticTotal, mechanical: d.mechanicalTotal,
    },
  };
  body.scoring.difficulty_explanation = d.explanation;
  if (body.build_metadata) body.build_metadata.scoring_version = d.scoringVersion;
  writeFileSync(path, `${JSON.stringify(body, null, 2)}\n`, 'utf8');
}

console.log(`\nуровней ${files.length}, оценка сдвинулась у ${changed}`
  + (write ? ' — файлы перезаписаны' : ' — это сухой прогон, добавьте --write'));
