/**
 * Ручная настройка сложности промежутков уровней: раздача стартового поля.
 *
 * Живёт на первой вкладке рядом с базой: это настройка ИНСТРУМЕНТА, а не
 * одного блока — действует на любую декаду, которую соберёт генератор, и
 * переживает перезагрузку страницы (localStorage). Настройка блока (вкладка 2)
 * отвечает за один диапазон; здесь — правило для всей кривой.
 *
 * Что настраивается: минимум слов категории на стартовом поле (core/deal.ts).
 * Умолчание — облегчённая раздача (минимум пара) на всей кривой: пузырь-одиночка
 * не сливается ни с чем и работает отвлечением, а не материалом для хода.
 * Пресет 201-210 (сдаваемый пакет) таблицей не трогается — его хеш закреплён.
 */
import type { DealRangeSetting } from '../core/decadeProfiles.ts';
import { DEFAULT_DEAL_RANGES } from '../core/decadeProfiles.ts';

const MODES: { value: number; label: string; hint: string }[] = [
  { value: 1,
    label: '1 — ровная (историческая)',
    hint: 'всем категориям понемногу; на 13+ категориях появляются одиночки' },
  { value: 2,
    label: '2 — облегчённая: без одиночек',
    hint: 'у категории на старте минимум пара; кому не хватило места — целиком в очереди' },
  { value: 3,
    label: '3 — плотная: минимум тройка',
    hint: 'категорий на старте меньше, каждая почти собрана — поле читается сразу' },
];

export function DealTuning({ ranges, onChange }: {
  ranges: DealRangeSetting[];
  onChange: (next: DealRangeSetting[]) => void;
}) {
  const sorted = [...ranges].sort((a, b) => a.from - b.from);
  const isDefault = JSON.stringify(sorted) === JSON.stringify(DEFAULT_DEAL_RANGES);

  const update = (i: number, patch: Partial<DealRangeSetting>) => {
    const next = sorted.map((row, k) => (k === i ? { ...row, ...patch } : row));
    onChange(next);
  };
  const addRow = () => {
    const last = sorted[sorted.length - 1];
    onChange([...sorted, {
      from: (last?.from ?? 0) + 120,
      minStartWords: last?.minStartWords === 1 ? 2 : 1,
    }]);
  };
  const removeRow = (i: number) => {
    onChange(sorted.filter((_, k) => k !== i));
  };

  return (
    <div className="panel">
      <h2>Раздача старта по промежуткам уровней</h2>
      <p className="hint">
        Поле держит 24 пузыря при любом числе категорий, поэтому раздача решает,
        каким уровень встречает игрока. Ровная раздача «всем понемногу» на 13+
        категориях кладёт часть категорий одним словом: такой пузырь не сливается
        ни с чем (пара ещё в очереди) — по замеру 400 уровней до 62% поля работало
        отвлечением. Облегчённая раздача даёт каждой видимой категории минимум
        пару, а кому не хватило места — оставляет целиком в очереди досыпки.
      </p>
      {sorted.map((row, i) => (
        <div className="row" style={{ alignItems: 'center', marginTop: 6 }} key={i}>
          <label className="field" style={{ maxWidth: 140 }}>
            <span className="lbl">с уровня</span>
            <input
              type="text"
              inputMode="numeric"
              value={String(row.from)}
              disabled={i === 0}
              onChange={(e) => {
                const n = Number(e.target.value);
                if (Number.isInteger(n) && n >= 2) update(i, { from: n });
              }}
            />
          </label>
          <label className="field" style={{ flex: 1 }}>
            <span className="lbl">минимум слов категории на старте</span>
            <select
              value={row.minStartWords}
              onChange={(e) => update(i, { minStartWords: Number(e.target.value) })}
            >
              {MODES.map((m) => (
                <option key={m.value} value={m.value}>{m.label}</option>
              ))}
            </select>
            <span className="small muted">
              {MODES.find((m) => m.value === row.minStartWords)?.hint ?? ''}
            </span>
          </label>
          {i > 0 && (
            <button className="ghost" onClick={() => removeRow(i)}>убрать</button>
          )}
        </div>
      ))}
      <div className="row" style={{ marginTop: 10 }}>
        <button className="ghost" onClick={addRow}>+ промежуток</button>
        {!isDefault && (
          <button className="ghost" onClick={() => onChange(DEFAULT_DEAL_RANGES)}>
            вернуть умолчание
          </button>
        )}
      </div>
      <p className="small muted" style={{ marginTop: 8 }}>
        Применяется при сборке блока по номеру его первого уровня. Пресет 201-210
        (сдаваемый пакет) настройка не трогает: его выкладка и хеш закреплены.
        Режим раздачи записывается в спек уровня и входит в хеш пакета.
      </p>
    </div>
  );
}
