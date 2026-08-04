/**
 * Шаг 6 — экспорт.
 *
 * Два разных JSON, и это не педантизм. Полный — артефакт пайплайна: provenance,
 * оценки, следы проверок. Игровой — контракт с клиентом игры. Смешивать их значит
 * тащить в билд килобайты отладочных данных на каждый уровень.
 *
 * Передача пакета в прототип жила здесь и уехала на шаг «Прототип»: сыграть в
 * собранное — проверка, а не выгрузка, и делается она до того, как файлы ушли
 * в билд, а не рядом с ними.
 */
import { useState } from 'react';
import type { BlockResult, GeneratedLevel, LevelSpec } from '../core/types.ts';
import { levelHardGateFailure } from '../core/generateBlock.ts';

export function ExportView({ block, toGameJson, toPipelineJson }: {
  block: BlockResult;
  toGameJson: (spec: LevelSpec, difficultyValue?: number) => unknown;
  toPipelineJson: (level: GeneratedLevel, block: BlockResult) => unknown;
}) {
  const [mode, setMode] = useState<'game' | 'pipeline'>('game');
  const [levelId, setLevelId] = useState(block.levels[0]?.spec.levelId ?? 0);
  const level = block.levels.find((l) => l.spec.levelId === levelId) ?? block.levels[0];

  const single = mode === 'game'
    ? toGameJson(level.spec, level.difficulty.value)
    : toPipelineJson(level, block);

  const wholePack = {
    pack_hash: block.packHash,
    content_snapshot_hash: block.contentSnapshotHash,
    generator_version: block.generatorVersion,
    config: block.config,
    levels: mode === 'game'
      ? block.levels.map((l) => toGameJson(l.spec, l.difficulty.value))
      : block.levels.map((l) => toPipelineJson(l, block)),
  };

  const download = (name: string, data: unknown) => {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = name;
    a.click();
    URL.revokeObjectURL(url);
  };

  const copy = () => navigator.clipboard?.writeText(JSON.stringify(single, null, 2));

  /*
   * Гейт экспорта — тот же самый, что у генерации: `levelHardGateFailure`.
   * Своей копии условий здесь нет намеренно. Раньше экран считал только
   * `validation.passed` и число решений, да и то лишь показывал плашкой —
   * кнопки скачивания оставались живыми, и обещание «экспорт разрешён только
   * после проверок» было неправдой. Плюс мимо проверки проходила динамическая
   * проходимость: уровень с вручную переложенным стартом мог не доигрываться
   * и всё равно уехать в файл.
   */
  const blocked = block.levels
    .map((l) => ({ levelId: l.spec.levelId, failure: levelHardGateFailure(l) }))
    .filter((r): r is { levelId: number; failure: { stage: string; reason: string } } =>
      r.failure !== null);
  const exportAllowed = blocked.length === 0;
  const singleFailure = levelHardGateFailure(level);

  /*
   * Плашки показывают ровно то, по чему судит гейт, и берут это из его же
   * отказов. Считать их отдельно — тот же капкан, из которого этот экран
   * вытаскивали: `playability.winnable` был бы «проходимость: везде» даже на
   * уровне со сломанным ритмом, то есть плашка спорила бы с блокировкой,
   * стоящей строкой ниже.
   */
  const failedStages = new Set(blocked.map((b) => b.failure.stage));
  const stageTags = [
    { stage: 'валидация', ok: 'hard-инварианты: все пройдены', fail: 'hard-инварианты: есть нарушения' },
    { stage: 'единственность решения', ok: 'единственность решения: везде', fail: 'единственность решения: нарушена' },
    { stage: 'проходимость', ok: 'проходимость: везде', fail: 'проходимость: нарушена' },
  ];

  return (
    <>
      <div className="panel">
        <h2>Экспорт</h2>
        <p className="hint">
          Экспорт разрешён только когда все уровни прошли hard-инварианты,
          имеют ровно одно глобальное решение и доигрываются в симуляции.
          После ручной правки уровня проверки считаются заново, и уровень,
          который их не прошёл, скачать нельзя.
        </p>
        <div className="row">
          {stageTags.map((t) => {
            const ok = !failedStages.has(t.stage);
            return (
              <span key={t.stage} className={`tag ${ok ? 'ok' : 'fail'}`}>
                {ok ? t.ok : t.fail}
              </span>
            );
          })}
          <span className="tag mono">пакет {block.packHash.slice(0, 12)}…</span>
        </div>
        {!exportAllowed && (
          <div className="hint" style={{ marginTop: 10 }}>
            <strong>Экспорт заблокирован.</strong> Не прошли проверку:
            <ul style={{ margin: '6px 0 0', paddingLeft: 18 }}>
              {blocked.map((b) => (
                <li key={b.levelId}>
                  уровень {b.levelId} — {b.failure.stage}: {b.failure.reason}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <div className="panel">
        <div className="spread">
          <div className="row">
            <button className={`ghost ${mode === 'game' ? 'on' : ''}`}
              onClick={() => setMode('game')}>Игровой JSON</button>
            <button className={`ghost ${mode === 'pipeline' ? 'on' : ''}`}
              onClick={() => setMode('pipeline')}>Полный JSON пайплайна</button>
          </div>
          <div className="row">
            {block.levels.map((l) => (
              <button key={l.spec.levelId}
                className={`ghost ${l.spec.levelId === levelId ? 'on' : ''}`}
                onClick={() => setLevelId(l.spec.levelId)}>{l.spec.levelId}</button>
            ))}
          </div>
        </div>

        <p className="hint" style={{ marginTop: 10 }}>
          {mode === 'game'
            ? 'Только то, что нужно клиенту игры: категории, слова, мета-связи, '
              + 'лимит ходов. Без оценок и следов валидации.'
            : 'Артефакт пайплайна: происхождение, разбивка оценок, результаты всех '
              + 'проверок, история попыток генерации.'}
        </p>

        <div className="row" style={{ marginBottom: 10 }}>
          {/* Отдельный уровень блокируется своим отказом, пакет — любым в пакете:
              файл пакета содержит все десять, и один непроходимый портит его весь. */}
          <button className="primary" disabled={singleFailure !== null}
            title={singleFailure
              ? `${singleFailure.stage}: ${singleFailure.reason}` : undefined}
            onClick={() => download(
              `${mode}-level-${levelId}.json`, single)}>
            Скачать уровень {levelId}
          </button>
          <button className="ghost" disabled={!exportAllowed}
            title={exportAllowed ? undefined
              : `не прошли проверку уровни: ${blocked.map((b) => b.levelId).join(', ')}`}
            onClick={() => download(
              `${mode}-pack-${block.config.levelRange.join('-')}.json`, wholePack)}>
            Скачать весь пакет
          </button>
          <button className="ghost" disabled={singleFailure !== null}
            onClick={copy}>Скопировать в буфер</button>
        </div>
        {singleFailure && (
          <p className="hint" style={{ marginTop: 0 }}>
            Уровень {levelId} скачать нельзя — {singleFailure.stage}:
            {' '}{singleFailure.reason}
          </p>
        )}

        <pre className="code">{JSON.stringify(single, null, 2)}</pre>
      </div>

      <div className="panel">
        <h2>Сводка пакета</h2>
        <table>
          <thead>
            <tr><th>ур.</th><th>роль</th><th className="num">D</th><th className="num">I</th>
              <th className="num">реш.</th><th>проверки</th><th>хеш уровня</th></tr>
          </thead>
          <tbody>
            {block.levels.map((l) => (
              <tr key={l.spec.levelId}>
                <td className="mono">{l.spec.levelId}</td>
                <td className="small">{l.plan.role}</td>
                <td className="num">{l.difficulty.value}</td>
                <td className="num">{l.interest.value}</td>
                <td className="num">{l.solutions.count}</td>
                <td>
                  <span className={`tag ${l.validation.passed ? 'ok' : 'fail'}`}>
                    {l.validation.passed ? 'PASS' : 'FAIL'}
                  </span>
                </td>
                <td className="mono small muted">{l.levelSpecHash.slice(0, 16)}…</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
