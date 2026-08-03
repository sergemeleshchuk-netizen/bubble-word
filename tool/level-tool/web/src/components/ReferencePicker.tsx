/**
 * Экран выбора уровней оригинала.
 *
 * Заменяет собой «Настройку блока» и «Генерацию», когда выбран источник
 * «База-реф-BWJ». Причина замены, а не дополнения: на этом источнике собирать
 * нечего. Профиль декады, коридор категорий, ритм, ловушки, ослабления —
 * всё это инструменты ПОДБОРА слов, а состав уровня оригинала уже задан.
 * Оставить те экраны включёнными значило бы предложить человеку крутить ручки,
 * которые ни на что не влияют.
 *
 * Что здесь есть: выбор номеров, сборка выбранных уровней из выгрузки и оценка
 * их нашими моделями D и I. Дальше уровень идёт теми же экранами, что и наш
 * собственный, — «Уровень», «Экспорт», «Добавить в Playable».
 */
import { useState } from 'react';
import type { BlockResult, GeneratedLevel } from '../core/types.ts';
import { parseLevelSelection, type BwjLevels } from '../core/referenceLevels.ts';

export function ReferencePicker({ data, block, busy, onBuild, onSelect, provenance }: {
  data: BwjLevels | null;
  block: BlockResult | null;
  busy: boolean;
  onBuild: (ids: number[]) => void;
  onSelect: (levelId: number) => void;
  provenance: Record<number, {
    moveLimitObserved: boolean; startObserved: boolean; unknownCategories: string[];
  }>;
}) {
  const max = data?.levels.length ?? 0;
  const [text, setText] = useState('1-10');
  const [error, setError] = useState<string | null>(null);

  const build = () => {
    const { ids, error: parseError } = parseLevelSelection(text, max);
    setError(parseError);
    if (!parseError) onBuild(ids);
  };

  return (
    <>
      <div className="panel">
        <h2>Уровни оригинала</h2>
        <p className="hint">
          Конвейер генерации на этом источнике выключен: состав уровня задан
          выгрузкой, подбирать нечего. Инструмент собирает выбранные уровни как
          есть и измеряет их нашими моделями — чтобы их можно было выгрузить
          и наиграть в прототипе.
        </p>

        {data === null
          ? <p className="hint">Выгрузка уровней ещё грузится…</p>
          : (
            <>
              <div className="row" style={{ alignItems: 'flex-end', gap: 12 }}>
                <label style={{ flex: 1 }}>
                  <span className="lbl">какие уровни</span>
                  <input
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    onKeyDown={(e) => { if (e.key === 'Enter') build(); }}
                    placeholder="1-10, или 3, 7, 12"
                  />
                </label>
                <button className="primary" disabled={busy} onClick={build}>
                  Собрать выбранные
                </button>
              </div>
              <p className="small muted">
                В выгрузке уровни 1–{max}. Можно диапазоном «1-10», списком
                «3, 7, 12» или вперемешку «1-5, 20».
              </p>
              {error && (
                <p className="small" style={{ color: 'var(--fail)' }}>{error}</p>
              )}
            </>
          )}
      </div>

      <div className="panel">
        <h2>Что здесь из оригинала, а что наше</h2>
        <table className="grid-table">
          <tbody>
            <Row what="Категории, их порядок и слова" who="оригинал"
              note="выгрузка 1025 уровней bubblewordjam.org" />
            <Row what="Порядок выдачи слов" who="оригинал"
              note="подтверждён покадрово на 19 записанных уровнях, 87% слов старта" />
            <Row what="Распиленные слова (два пузыря)" who="оригинал"
              note="поле chunks выгрузки: 755 уровней из 1025" />
            <Row what="Мета-пузыри" who="оригинал"
              note="на старте не лежат — уходят в досыпку, как в записях" />
            <Row what="Лимит ходов, уровни 1-20" who="запись"
              note="снят покадрово" />
            <Row what="Лимит ходов, уровни 21+" who="наш расчёт"
              note="K = 1.36 от минимума мерджей — единственное измерение, какое есть" />
            <Row what="Число пузырей на старте, 21+" who="наш расчёт"
              note="вместимость поля 24; у оригинала оно плавает 16-27" />
            <Row what="Оценки D и I, число решений" who="наши модели"
              note="это измерение чужого уровня, а не его свойство" />
          </tbody>
        </table>
      </div>

      {block && block.levels.length > 0 && (
        <div className="panel">
          <h2>Собрано уровней: {block.levels.length}</h2>
          <table className="grid-table">
            <thead>
              <tr>
                <th>уровень</th><th>категорий</th><th>пузырей на старте</th>
                <th>лимит ходов</th><th>D</th><th>I</th><th>решений</th><th></th>
              </tr>
            </thead>
            <tbody>
              {block.levels.map((l) => (
                <LevelRow
                  key={l.spec.levelId}
                  level={l}
                  prov={provenance[l.spec.levelId]}
                  onSelect={onSelect}
                />
              ))}
            </tbody>
          </table>
          <p className="small muted">
            Хеш пакета {block.packHash.slice(0, 16)}… — считается от состава
            уровней и источника, поэтому один и тот же выбор всегда даёт один хеш.
          </p>
        </div>
      )}
    </>
  );
}

function Row({ what, who, note }: { what: string; who: string; note: string }) {
  return (
    <tr>
      <td>{what}</td>
      <td><strong>{who}</strong></td>
      <td className="small muted">{note}</td>
    </tr>
  );
}

function LevelRow({ level, prov, onSelect }: {
  level: GeneratedLevel;
  prov?: { moveLimitObserved: boolean; startObserved: boolean; unknownCategories: string[] };
  onSelect: (id: number) => void;
}) {
  const spec = level.spec;
  const mark = (observed: boolean | undefined) => (observed
    ? <span className="small" style={{ color: 'var(--ok)' }}> · с записи</span>
    : <span className="small muted"> · наш расчёт</span>);
  return (
    <tr>
      <td><strong>{spec.levelId}</strong></td>
      <td>{spec.categories.length}</td>
      <td>{spec.deal.start.length}{mark(prov?.startObserved)}</td>
      <td>{spec.board.moveLimit ?? '—'}{mark(prov?.moveLimitObserved)}</td>
      <td>{level.difficulty.value}</td>
      <td>{level.interest.value}</td>
      <td>
        {level.solutions.count === 1 ? 'одно'
          : level.solutions.count === 0 ? 'нет' : 'больше одного'}
      </td>
      <td>
        <button className="ghost" onClick={() => onSelect(spec.levelId)}>
          Открыть
        </button>
      </td>
    </tr>
  );
}
