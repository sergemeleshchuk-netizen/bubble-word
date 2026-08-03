/**
 * Шаг 5 — играбельный прототип.
 *
 * Прототип живёт одной страницей сайта (`site/playable/index.html`) и встроен
 * сюда рамкой телефона. Копии прототипа здесь нет и быть не должно: он один,
 * это только окно в него. Раньше между «собрал» и «сыграл» стоял переход в
 * другой пункт отчёта — собранное проверяли реже, чем стоило.
 *
 * Почему нужна кнопка, а не автозапуск: прототип читает уровень из рабочего
 * слота localStorage по индексу (`?gen=N`), и слот общий — в нём может лежать
 * пакет с прошлой сборки или склейка сданных пакетов от страницы отчёта.
 * Нажатие кладёт туда ИМЕННО этот пакет, и только после этого индекс уровня
 * означает то, что написано на кнопке. Заодно пакет попадает в архив — тот же
 * путь, что и раньше, поэтому уровни видны и в пункте «Build Playable».
 */
import { useState } from 'react';
import type { BlockResult } from '../core/types.ts';
import { HANDOFF_MAX_PACKS, publishToPlayable, type HandoffPack } from '../core/playableHandoff.ts';

/**
 * Путь к прототипу — относительный, потому что инструмент и прототип на сайте
 * лежат соседними каталогами (`/tool/` и `/playable/`). В dev-сервере
 * инструмент открыт из корня, и тот же путь отдаёт прослойка из vite.config.ts:
 * файл один и тот же, копии нет.
 */
const PLAYABLE_URL = '../playable/index.html';

export function PlayableStep({ block }: { block: BlockResult }) {
  /** null — пакет ещё не отдавали; 'failed' — хранилище недоступно */
  const [handed, setHanded] = useState<HandoffPack | 'failed' | null>(null);
  const [gen, setGen] = useState(0);
  /** счётчик перезапусков: смена ключа iframe заставляет партию начаться заново */
  const [restart, setRestart] = useState(0);

  const pack = handed === 'failed' ? null : handed;
  const level = pack?.levels[gen];

  const publish = () => {
    setHanded(publishToPlayable(block) ?? 'failed');
    setGen(0);
    setRestart((n) => n + 1);
  };

  const play = (index: number) => {
    setGen(index);
    setRestart((n) => n + 1);
  };

  /*
   * Одна панель на весь шаг, и это не косметика: вертикали здесь мало —
   * инструмент сам открыт в рамке отчёта, — а телефон должен влезать в неё
   * целиком. Каждая отдельная панель забирала бы у него по 30-40 пикселей.
   */
  return (
    <div className="panel">
      <div className="spread">
        <div>
          <h2>Сыграть в собранное</h2>
          <p className="hint" style={{ marginBottom: 10 }}>
            Пакет играется здесь же. Архив последних {HANDOFF_MAX_PACKS} сборок
            виден и в пункте «Build Playable» — «до» и «после» правки сравнимы.
          </p>
        </div>
        <div className="row">
          <button className="primary" onClick={publish}>
            {pack ? 'Обновить пакет в Playable' : 'Добавить в Playable'}
          </button>
        </div>
      </div>

      {handed === 'failed' && (
        <p className="small" style={{ color: 'var(--warn)', margin: 0 }}>
          Браузер не дал сохранить пакет (приватный режим или запрет хранилища).
          Прототип его не увидит — воспользуйтесь скачиванием JSON на шаге «Экспорт».
        </p>
      )}

      {pack
        ? (
          <>
            <div className="row" style={{ marginBottom: 12 }}>
              <span className="muted small">уровень:</span>
              {pack.levels.map((l, i) => (
                <button
                  key={l.level_id}
                  className={`ghost ${i === gen ? 'on' : ''}`}
                  onClick={() => play(i)}
                >
                  {l.level_id}
                </button>
              ))}
              <button className="ghost" onClick={() => setRestart((n) => n + 1)}>
                ↻ заново
              </button>
              {level && <span className="muted small">{level.title}</span>}
              <a className="small" href={`${PLAYABLE_URL}?gen=${gen}`}
                target="_blank" rel="noopener">
                отдельной вкладкой ↗
              </a>
            </div>
            <div className="play-phone">
              {/* key меняется на выборе уровня и на «заново»: iframe обязан
                  перемонтироваться, иначе прототип продолжит прошлую партию */}
              <iframe
                key={`${gen}-${restart}`}
                src={`${PLAYABLE_URL}?gen=${gen}`}
                title="Играбельный прототип"
              />
            </div>
          </>
        )
        : (
          <p className="small muted" style={{ margin: 0 }}>
            Прототип запустится, когда пакет уедет в хранилище. Лимит ходов,
            стартовая выкладка и модификаторы берутся из пакета — прототип их
            исполняет, своей случайности у него нет.
          </p>
        )}
    </div>
  );
}
