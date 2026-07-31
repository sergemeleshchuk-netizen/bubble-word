/**
 * Экран 6 — экспорт.
 *
 * Два разных JSON, и это не педантизм. Полный — артефакт пайплайна: provenance,
 * оценки, следы проверок. Игровой — контракт с клиентом игры. Смешивать их значит
 * тащить в билд килобайты отладочных данных на каждый уровень.
 */
import { useState } from 'react';
import type { BlockResult, GeneratedLevel, LevelSpec } from '../core/types.ts';
import { publishToPlayable, type HandoffPack } from '../core/playableHandoff.ts';

export function ExportView({ block, toGameJson, toPipelineJson }: {
  block: BlockResult;
  toGameJson: (spec: LevelSpec) => unknown;
  toPipelineJson: (level: GeneratedLevel, block: BlockResult) => unknown;
}) {
  const [mode, setMode] = useState<'game' | 'pipeline'>('game');
  const [levelId, setLevelId] = useState(block.levels[0]?.spec.levelId ?? 0);
  const level = block.levels.find((l) => l.spec.levelId === levelId) ?? block.levels[0];
  /** null — ещё не отдавали; 'failed' — хранилище недоступно */
  const [handed, setHanded] = useState<HandoffPack | 'failed' | null>(null);

  const single = mode === 'game'
    ? toGameJson(level.spec)
    : toPipelineJson(level, block);

  const wholePack = {
    pack_hash: block.packHash,
    content_snapshot_hash: block.contentSnapshotHash,
    generator_version: block.generatorVersion,
    config: block.config,
    levels: mode === 'game'
      ? block.levels.map((l) => toGameJson(l.spec))
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

  const allPassed = block.levels.every((l) => l.validation.passed);
  const allUnique = block.levels.every((l) => l.solutions.count === 1);

  return (
    <>
      <div className="panel">
        <h2>Экспорт</h2>
        <p className="hint">
          Экспорт разрешён только когда все уровни прошли hard-инварианты
          и имеют ровно одно глобальное решение. После ручной правки уровня
          проверки становятся недействительными, и экспорт снова блокируется.
        </p>
        <div className="row">
          <span className={`tag ${allPassed ? 'ok' : 'fail'}`}>
            hard-инварианты: {allPassed ? 'все пройдены' : 'есть нарушения'}
          </span>
          <span className={`tag ${allUnique ? 'ok' : 'fail'}`}>
            единственность решения: {allUnique ? 'везде' : 'нарушена'}
          </span>
          <span className="tag mono">пакет {block.packHash.slice(0, 12)}…</span>
        </div>
      </div>

      {/*
        Отдать пакет в прототип. Кнопка стоит до экспорта JSON намеренно:
        сыграть в собранное — самая быстрая проверка, что уровень живой,
        и делать её удобнее до того, как файлы уехали в билд.
      */}
      <div className="panel">
        <h2>Сыграть в собранное</h2>
        <p className="hint">
          Пакет уезжает в играбельный прототип — он отдельным пунктом рядом
          («Build Playable»). Уровни появятся там в списке отдельной группой,
          названной версией инструмента и хешем пакета.
        </p>
        <div className="row">
          <button className="primary"
            onClick={() => setHanded(publishToPlayable(block) ?? 'failed')}>
            Добавить в Playable
          </button>
          {handed && handed !== 'failed' && (
            <span className="tag mono">{handed.label}</span>
          )}
        </div>

        {handed === 'failed' && (
          <p className="small" style={{ color: 'var(--warn)', marginTop: 10 }}>
            Браузер не дал сохранить пакет (приватный режим или запрет хранилища).
            Прототип его не увидит — воспользуйтесь скачиванием JSON ниже.
          </p>
        )}
        {handed && handed !== 'failed' && (
          <p className="small" style={{ color: 'var(--ok)', marginTop: 10 }}>
            Готово: {handed.levels.length} уровней добавлено как группа
            «{handed.label}». Можете сыграть в эти уровни в Playable —
            откройте пункт «Build Playable» и выберите эту группу в списке уровней.
          </p>
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
          <button className="primary"
            onClick={() => download(
              `${mode}-level-${levelId}.json`, single)}>
            Скачать уровень {levelId}
          </button>
          <button className="ghost"
            onClick={() => download(
              `${mode}-pack-${block.config.levelRange.join('-')}.json`, wholePack)}>
            Скачать весь пакет
          </button>
          <button className="ghost" onClick={copy}>Скопировать в буфер</button>
        </div>

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
