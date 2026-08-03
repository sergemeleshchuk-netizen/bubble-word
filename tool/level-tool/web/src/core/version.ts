/**
 * Версии инструмента и его моделей — один реестр вместо россыпи констант.
 *
 * До этого модуля версии лежали в трёх разных местах: `GENERATOR_VERSION` в
 * generator.ts, `scoring_version` в конфиге скоринга, хеш снимка в самом снимке.
 * У счётчика решений версии не было вовсе. Спросить «а на какой версии собран
 * этот пакет» было негде.
 *
 * Разделение, которое здесь важно не потерять (docs/level_evaluation/evaluation_mapping.md §10):
 *
 *   TOOL_VERSION      релиз инструмента: UI, экспорт, что угодно. НЕ входит в хеш.
 *   GENERATOR_VERSION алгоритм сборки уровня. ВХОДИТ в хеш — и обязан входить.
 *   версии моделей    формулы D и I. Живут в конфиге, меняются отдельно от релиза.
 *   SOLVER_VERSION    алгоритм доказательства единственности решения.
 *
 * Почему TOOL_VERSION не в хеше: обещание «тот же конфиг + тот же seed + тот же
 * снимок = тот же уровень» должно переживать релизы инструмента. Иначе каждая
 * правка вёрстки обнуляла бы регрессию по сданным пакетам. Проверяется тестом
 * в tests/version.test.ts.
 */
import { GENERATOR_VERSION } from './generator.ts';
import type { ScoringConfig } from './scoringDifficulty.ts';

/**
 * Релиз инструмента, semver. Поднимается вместе со строкой в CHANGELOG.md —
 * тест не даст поднять версию, не описав, что изменилось.
 *
 *   major — сломана совместимость экспорта или конфига блока;
 *   minor — новая возможность;
 *   patch — исправление без новых возможностей.
 */
export const TOOL_VERSION = '1.28.0';

/**
 * Версия счётчика решений. Отдельная от генератора: доказательство
 * единственности можно улучшить, не меняя сборку уровня, и наоборот.
 *
 * 1.0 — полный перебор exact-cover с лимитом узлов и флагом `exhausted`.
 * 1.1 — обрезанный по лимиту перебор больше не считается доказательством:
 *       одна найденная раскладка при `exhausted = false` — это «неизвестно».
 */
export const SOLVER_VERSION = 'solver-1.1';

/**
 * Полный набор версий одного прогона. Кладётся в экспорт и показывается в UI,
 * чтобы любое сданное число можно было привязать к тому, чем оно посчитано.
 *
 * Поля `frustration` / `confidence` / `structureSimulator` / `blindEvaluator`
 * появятся в Phase 1-3 (см. mapping §10). Пока их нет — в наборе их нет тоже:
 * пустая строка на месте версии врала бы, что модель существует.
 */
export interface VersionSet {
  tool: string;
  generator: string;
  solver: string;
  difficultyModel: string;
  interestModel: string;
  contentSnapshot: string;
}

export function versionSet(
  scoring: ScoringConfig,
  contentSnapshotHash: string,
): VersionSet {
  return {
    tool: TOOL_VERSION,
    generator: GENERATOR_VERSION,
    solver: SOLVER_VERSION,
    difficultyModel: scoring.scoring_version,
    interestModel: scoring.interest.scoring_version,
    contentSnapshot: contentSnapshotHash,
  };
}
