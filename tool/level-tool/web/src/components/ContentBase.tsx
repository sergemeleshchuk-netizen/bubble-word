/**
 * Шаг 1 — база контента.
 *
 * Экрану нужны ровно три вещи: выбрать словарь, одной строкой показать, что в
 * нём лежит, и пустить дальше — к конфигу раскладки, который стоит ниже.
 *
 * Чего здесь больше нет (решение владельца 03.08): журнал AI-прогонов, разбор
 * ошибок модели, сравнение словарей и списки ограничений источника. Всё это —
 * материал отчёта, а не рабочего инструмента: на первом шаге оно занимало три
 * экрана прокрутки до первой настройки, которую человек пришёл покрутить.
 * Данные никуда не пропали (`data/ai_runs.json`, `core/sources.ts`) — просто не
 * рисуются здесь.
 */
import type { Snapshot } from '../core/types.ts';
import { CONTENT_SOURCES, type ContentSource, type SourceId } from '../core/sources.ts';

/**
 * Плашки состава. Показываем только то, что в снимке действительно есть:
 * у словаря оригинала нет ни значений слова, ни статусов связи, и плашка
 * «0 значений» врала бы, что там пустой слой, а не отсутствующий.
 */
function facts(snapshot: Snapshot): string[] {
  const s = snapshot.stats ?? {};
  const n = (key: string): number | null => {
    const v = s[key];
    return typeof v === 'number' && v > 0 ? v : null;
  };
  const fmt = (v: number): string => v.toLocaleString('ru-RU');

  const out: string[] = [];
  const add = (key: string, label: string) => {
    const v = n(key);
    if (v !== null) out.push(`${fmt(v)} ${label}`);
  };

  add('reference_levels', 'уровней выгрузки');
  add('categories', 'категорий');
  add('words', 'слов');
  add('memberships', 'связей слово ↔ категория');
  add('quartets', 'готовых четвёрок');
  add('senses', 'разведённых значений');
  add('trap_capable_words', 'слов в 2+ категориях');
  add('meta_capable_categories', 'мета-пригодных категорий');
  return out;
}

export function ContentBase({ snapshot, source, requested, loading, busy, onSwitch }: {
  snapshot: Snapshot;
  source: ContentSource;
  /** запрошенный источник: подсвечен сразу, снимок к нему может быть ещё в пути */
  requested: SourceId;
  loading: SourceId | null;
  busy: boolean;
  onSwitch: (id: SourceId) => void;
}) {
  return (
    <div className="panel">
      <h2>База контента</h2>
      <p className="hint">
        Словарь, из которого собираются уровни. Хеш снимка входит в хеш уровня —
        по пакету всегда видно, откуда он.
      </p>

      <div className="sources">
        <span className="lbl">источник</span>
        {CONTENT_SOURCES.map((s) => (
          <button
            key={s.id}
            className={`ghost ${requested === s.id ? 'on' : ''}`}
            disabled={busy}
            onClick={() => onSwitch(s.id)}
          >
            {s.label}
            {loading === s.id && ' · грузится…'}
          </button>
        ))}
        <span className="muted small">{source.origin}</span>
      </div>

      <div className="row" style={{ marginTop: 12 }}>
        {facts(snapshot).map((f) => <span className="tag" key={f}>{f}</span>)}
      </div>
    </div>
  );
}
