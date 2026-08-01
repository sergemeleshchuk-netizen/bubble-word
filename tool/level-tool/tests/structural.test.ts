/**
 * Структурные метрики: вход в уровень, развилки, оспариваемые слоты.
 *
 * Эти числа не входят ни в D, ни в I — и последний тест файла это фиксирует.
 * Метрика, которая молча начала двигать оценку, обесценила бы калибровку:
 * сданные пакеты пересчитались бы сами собой, и сравнивать стало бы не с чем.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { ContentIndex } from '../web/src/core/snapshot.ts';
import { computeStructuralMetrics } from '../web/src/core/structuralMetrics.ts';
import { countSolutions } from '../web/src/core/solutionCounter.ts';
import { validateLevel } from '../web/src/core/validator.ts';
import { computeDifficulty, type ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { computeInterest } from '../web/src/core/scoringInterest.ts';
import type { LevelCategory, LevelSpec, LevelWord } from '../web/src/core/types.ts';
import { buildSpec, levelCategory, makeSnapshot } from './fixtures/synthetic.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

function w(text: string, zipf = 4.0, obviousness = 0.7): LevelWord {
  return { text, kind: 'word', zipf, frequencyUnknown: false,
    relation: 'is_a', fit: 0.9, obviousness };
}

/**
 * Три категории, каждое слово живёт ровно в одной. Развилок нет: такой уровень
 * раскладывается подряд, и никакой гипотезы пересобирать не надо.
 */
function plainLevel(): { spec: LevelSpec; index: ContentIndex } {
  const specs: Parameters<typeof makeSnapshot>[0] = [];
  const categories: LevelCategory[] = [];
  for (let c = 0; c < 3; c += 1) {
    const words: LevelWord[] = [];
    const specWords: [string, number, 'approved', number][] = [];
    for (let i = 0; i < 4; i += 1) {
      const text = `p${c}_${i}`;
      words.push(w(text));
      specWords.push([text, 4.0, 'approved', 0.7]);
    }
    specs.push({ key: `cat${c}`, label: `CAT ${c}`, theme: `theme${c}`, words: specWords });
    categories.push(levelCategory(`cat${c}`, `CAT ${c}`, words,
      { theme: `theme${c}`, isQuickwin: c === 0 }));
  }
  return { spec: buildSpec(801, categories), index: new ContentIndex(makeSnapshot(specs)) };
}

/**
 * Тот же уровень, но два слова из первой категории правдоподобно тянет во
 * вторую. Однодомных слов в первой категории остаётся два — закрыть её сразу
 * нельзя, и дедукция обязана упереться в выбор.
 */
function contestedLevel(): { spec: LevelSpec; index: ContentIndex } {
  const specs: Parameters<typeof makeSnapshot>[0] = [];
  const categories: LevelCategory[] = [];
  for (let c = 0; c < 3; c += 1) {
    const words: LevelWord[] = [];
    const specWords: [string, number, 'approved', number][] = [];
    for (let i = 0; i < 4; i += 1) {
      const text = `p${c}_${i}`;
      words.push(w(text));
      specWords.push([text, 4.0, 'approved', 0.7]);
    }
    specs.push({ key: `cat${c}`, label: `CAT ${c}`, theme: `theme${c}`, words: specWords });
    categories.push(levelCategory(`cat${c}`, `CAT ${c}`, words,
      { theme: `theme${c}`, isQuickwin: false }));
  }
  const index = new ContentIndex(makeSnapshot(specs, {
    alternatives: [['p0_0', 'cat1', 0.8, 0.4], ['p0_1', 'cat1', 0.8, 0.4]],
  }));
  return { spec: buildSpec(802, categories), index };
}

test('уровень без вторых домов помечается как чистая дедукция', () => {
  const { spec, index } = plainLevel();
  const m = computeStructuralMetrics(index, spec);

  assert.equal(m.multiHomeWords, 0, 'вторых домов в фикстуре нет');
  assert.equal(m.openingCategories, 3, 'все три категории собираются сразу');
  assert.equal(m.deductionOnly, true, 'развилок нет — это рутина, а не головоломка');
  assert.equal(m.forcedSteps, 12, 'дедукция обязана дойти до всех двенадцати слов');
});

test('второй правдоподобный дом создаёт развилку и убирает вход', () => {
  const { spec, index } = contestedLevel();
  const m = computeStructuralMetrics(index, spec);

  assert.equal(m.multiHomeWords, 2, 'ровно два слова тянет в соседнюю категорию');
  assert.ok(m.maxContestedSlots >= 2,
    `оспариваемых слотов ${m.maxContestedSlots}, ожидалось не меньше двух`);
  assert.equal(m.openingCategories, 2,
    'первую категорию сразу закрыть нельзя: в ней только два однодомных слова');
});

test('метрики попадают в валидатор: нет входа и нет развилок — два soft-замечания', () => {
  const { spec, index } = plainLevel();
  const solutions = countSolutions(index, spec);
  const structural = computeStructuralMetrics(index, spec);
  const result = validateLevel(spec, { index, solutions, structural });

  const codes = result.issues.map((i) => i.code);
  assert.ok(codes.includes('DEDUCTION_ONLY'),
    'уровень без развилок обязан получить замечание');
  assert.ok(result.issues.every((i) => i.severity === 'soft' || i.code !== 'DEDUCTION_ONLY'),
    'это замечание мягкое: оно не имеет права ронять сборку');
});

test('обрезанный перебор не считается доказательством единственности', () => {
  const { spec, index } = plainLevel();
  const truncated = validateLevel(spec, {
    index,
    solutions: { count: 1, nodesVisited: 200001, exhausted: false },
  });
  const check = truncated.checks.find((c) => c.code === 'GLOBAL_SOLUTION_COUNT');
  assert.ok(check && !check.passed,
    'единственность при обрезанном переборе — это «неизвестно», а не PASS');

  const honest = validateLevel(spec, {
    index,
    solutions: { count: 1, nodesVisited: 40, exhausted: true },
  });
  const ok = honest.checks.find((c) => c.code === 'GLOBAL_SOLUTION_COUNT');
  assert.ok(ok && ok.passed, 'исчерпанный перебор с одной раскладкой — по-прежнему PASS');
});

test('структурные метрики не двигают ни D, ни I', () => {
  const { spec, index } = contestedLevel();
  const solutions = countSolutions(index, spec);

  const dBefore = computeDifficulty(spec, index, scoring, solutions);
  const iBefore = computeInterest(spec, index, scoring, solutions);

  // считаем метрики и повторяем оценку: числа обязаны совпасть до сотых
  computeStructuralMetrics(index, spec);
  const dAfter = computeDifficulty(spec, index, scoring, solutions);
  const iAfter = computeInterest(spec, index, scoring, solutions);

  assert.equal(dAfter.value, dBefore.value);
  assert.equal(iAfter.value, iBefore.value);
  assert.deepEqual(dAfter.base, dBefore.base);
  assert.deepEqual(
    [iAfter.clarity, iAfter.variety, iAfter.aha, iAfter.freshness],
    [iBefore.clarity, iBefore.variety, iBefore.aha, iBefore.freshness],
  );
});
