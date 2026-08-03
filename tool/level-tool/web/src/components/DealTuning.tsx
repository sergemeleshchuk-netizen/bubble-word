/**
 * Таблица стартовой раскладки по декадам.
 *
 * Формат — решение владельца 03.08: на каждый промежуток уровней — стартовые
 * слова (min/max), коридор категорий (min/max) и ВИЛКА схем выкладки:
 *
 *   декада | стартовых слов | категорий | схема min | схема max
 *   1-10   | 16-20          | 5-12      | 4-3-3-3-2-1 | 4-4-3-3-3-2-1
 *
 * Уровень с минимумом категорий коридора получает схему min, с максимумом —
 * схему max, между ними схема интерполируется (resolveScheme в core/deal.ts).
 * «Стартовых слов» — производная колонка: суммы схем вилки; при пустых схемах
 * показываются суммы автоматической облегчённой раздачи.
 *
 * Сетка строк: до 100 подекадно, 101-200 по 20, 201-1000 по 100, дальше по
 * 1000 до 5000 — ручной дизайн у оригинала виден в начале кривой, с ~L300
 * статистика замерзает, и строк на каждую декаду там не из чего заполнять.
 *
 * Живёт на первой вкладке: это настройка ИНСТРУМЕНТА на всю кривую, а не
 * одного блока. Правки переживают перезагрузку (localStorage в App) и
 * применяются к сборке блока по номеру его первого уровня. Пресет 201-210
 * (сдаваемый пакет) таблица не трогает — его выкладка и хеш закреплены.
 */
import { useState } from 'react';
import {
  decadeTuningDefaults, formatScheme, liteSchemePreview, parseScheme,
} from '../core/decadeProfiles.ts';
import type { DecadeTuningRow } from '../core/decadeProfiles.ts';

function sum(scheme: readonly number[]): number {
  return scheme.reduce((a, b) => a + b, 0);
}

/** Вилка стартовых слов строки: суммы схем; пустая схема = авто для края коридора. */
function startWordsRange(row: DecadeTuningRow): [number, number] {
  const minScheme = row.schemeMin ?? row.schemeMax ?? liteSchemePreview(row.corridor[0]);
  const maxScheme = row.schemeMax ?? row.schemeMin ?? liteSchemePreview(row.corridor[1]);
  const a = sum(minScheme);
  const b = sum(maxScheme);
  return a <= b ? [a, b] : [b, a];
}

export function DecadeTable({ rows, onChange }: {
  rows: DecadeTuningRow[];
  onChange: (next: DecadeTuningRow[]) => void;
}) {
  const sorted = [...rows].sort((a, b) => a.from - b.from);
  const defaults = decadeTuningDefaults();
  const isDefault = JSON.stringify(sorted) === JSON.stringify(defaults);

  const update = (from: number, patch: Partial<DecadeTuningRow>) => {
    onChange(sorted.map((r) => (r.from === from ? { ...r, ...patch } : r)));
  };

  return (
    <div className="panel">
      <h2>Стартовая раскладка по декадам</h2>
      <p className="hint">
        Схема — доли категорий на старте по убыванию:{' '}
        <span className="mono">4-3-3-3-2-1</span> — одна категория целиком
        (вход), три по тройке, пара и одиночка. Уровень с минимумом категорий
        коридора получает схему min, с максимумом — схему max, между ними
        раскладка интерполируется. Пустые схемы — автоматическая облегчённая
        раздача: вход целиком, остальным минимум пара, без одиночек.
        «Стартовых слов» — суммы схем вилки, считается само.
      </p>
      <div style={{ overflowX: 'auto' }}>
        <table>
          <thead>
            <tr>
              <th>декада</th>
              <th>стартовых слов</th>
              <th>категорий min</th>
              <th>max</th>
              <th style={{ minWidth: 200 }}>схема min</th>
              <th style={{ minWidth: 200 }}>схема max</th>
            </tr>
          </thead>
          <tbody>
            {sorted.map((row) => {
              const base = defaults.find((d) => d.from === row.from);
              const edited = !base || JSON.stringify(base) !== JSON.stringify(row);
              const words = startWordsRange(row);
              const auto = row.schemeMin === null && row.schemeMax === null;
              return (
                <tr key={row.from} className={edited ? 'selected' : undefined}>
                  <td className="mono">{row.from}-{row.to}</td>
                  <td className="small mono">
                    {words[0] === words[1] ? words[0] : `${words[0]}-${words[1]}`}
                    {auto ? ' (авто)' : ''}
                  </td>
                  <td>
                    <input
                      type="text" inputMode="numeric" style={{ width: 52 }}
                      value={String(row.corridor[0])}
                      onChange={(e) => {
                        const n = Number(e.target.value);
                        if (Number.isInteger(n) && n >= 3 && n <= row.corridor[1]) {
                          update(row.from, { corridor: [n, row.corridor[1]] });
                        }
                      }}
                    />
                  </td>
                  <td>
                    <input
                      type="text" inputMode="numeric" style={{ width: 52 }}
                      value={String(row.corridor[1])}
                      onChange={(e) => {
                        const n = Number(e.target.value);
                        if (Number.isInteger(n) && n >= row.corridor[0] && n <= 18) {
                          update(row.from, { corridor: [row.corridor[0], n] });
                        }
                      }}
                    />
                  </td>
                  <td>
                    <SchemeField
                      value={row.schemeMin}
                      placeholder={`авто: ${formatScheme(liteSchemePreview(row.corridor[0]))}`}
                      onCommit={(schemeMin) => update(row.from, { schemeMin })}
                    />
                  </td>
                  <td>
                    <SchemeField
                      value={row.schemeMax}
                      placeholder={`авто: ${formatScheme(liteSchemePreview(row.corridor[1]))}`}
                      onCommit={(schemeMax) => update(row.from, { schemeMax })}
                    />
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <div className="row" style={{ marginTop: 10 }}>
        {!isDefault && (
          <button className="ghost" onClick={() => onChange(decadeTuningDefaults())}>
            вернуть умолчания
          </button>
        )}
      </div>
      <p className="small muted" style={{ marginTop: 8 }}>
        Заполнена одна схема из двух — она действует на весь промежуток.
        Правка коридора подрезает и план категорий блока. Разрешённая для
        уровня схема записывается в его спек и входит в хеш пакета.
        Пресет 201-210 таблица не трогает.
      </p>
    </div>
  );
}

/**
 * Поле схемы с черновиком: пока строка не разобралась в валидную схему,
 * в таблицу ничего не уезжает — то же поведение, что у полей Composer.
 */
function SchemeField({ value, placeholder, onCommit }: {
  value: number[] | null;
  placeholder: string;
  onCommit: (scheme: number[] | null) => void;
}) {
  const [draft, setDraft] = useState<string | null>(null);
  const canonical = value ? formatScheme(value) : '';
  const pending = draft !== null && parseScheme(draft) === undefined;

  return (
    <input
      type="text"
      style={{ width: '100%' }}
      className={pending ? 'pending' : undefined}
      value={draft ?? canonical}
      placeholder={placeholder}
      onChange={(e) => {
        setDraft(e.target.value);
        const parsed = parseScheme(e.target.value);
        if (parsed !== undefined) onCommit(parsed);
      }}
      onBlur={() => setDraft(null)}
    />
  );
}
