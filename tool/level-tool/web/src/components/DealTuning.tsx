/**
 * Таблица декад: коридор категорий и схема выкладки старта.
 *
 * Формат — тот же, что у замера оригинала (DECADE_CALIBRATION.md §2, разбор
 * 02.08): «декада | категорий min-max | схема выкладки». Таблица наглядна и
 * редактируется руками: дизайнер правит конкретную декаду, а не глобальный
 * флаг, и видит, каким уровень встречает игрока.
 *
 * Живёт на первой вкладке: это настройка ИНСТРУМЕНТА на всю кривую, а не
 * одного блока. Правки переживают перезагрузку (localStorage в App) и
 * применяются к сборке блока по номеру его первого уровня. Пресет 201-210
 * (сдаваемый пакет) таблица не трогает — его выкладка и хеш закреплены.
 */
import { useState } from 'react';
import {
  DECADE_PROFILES, decadeTuningDefaults, formatScheme, liteSchemePreview, parseScheme,
} from '../core/decadeProfiles.ts';
import type { DecadeTuningRow } from '../core/decadeProfiles.ts';

function decadeLabelFor(from: number, rows: readonly DecadeTuningRow[]): string {
  const next = rows.find((r) => r.from === from + 10);
  return next ? `${from}-${from + 9}` : `${from}+`;
}

function meanFor(from: number): number {
  const profile = [...DECADE_PROFILES].reverse().find((p) => p.from <= from);
  return Math.round(profile?.categoryMean ?? 9);
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
      <h2>Декады: категории и схема выкладки</h2>
      <p className="hint">
        Формат замера оригинала: на каждую декаду — коридор по числу категорий
        и схема стартового поля. Схема читается как доли категорий на старте по
        убыванию: <span className="mono">4-3-3-3-2-2-2-2-1</span> — одна
        категория целиком (вход), три по тройке, четыре пары и одна одиночка.
        Пустая схема — автоматическая облегчённая раздача: вход целиком,
        остальным минимум пара, без одиночек; кому не хватило места — целиком
        в очереди досыпки. Явная схема применяется как написано — вместе с
        одиночками, если они в ней есть.
      </p>
      <div style={{ overflowX: 'auto' }}>
        <table>
          <thead>
            <tr>
              <th>декада</th>
              <th>категорий min</th>
              <th>max</th>
              <th style={{ minWidth: 260 }}>схема выкладки (пусто = авто)</th>
              <th>сейчас действует</th>
            </tr>
          </thead>
          <tbody>
            {sorted.map((row) => {
              const mean = meanFor(row.from);
              const auto = liteSchemePreview(mean);
              const base = defaults.find((d) => d.from === row.from);
              const edited = !base || JSON.stringify(base) !== JSON.stringify(row);
              const effective = row.scheme ?? auto;
              const queued = Math.max(0, mean - effective.length);
              return (
                <tr key={row.from} className={edited ? 'selected' : undefined}>
                  <td className="mono">{decadeLabelFor(row.from, sorted)}</td>
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
                      value={row.scheme}
                      placeholder={`авто: ${formatScheme(auto)}`}
                      onCommit={(scheme) => update(row.from, { scheme })}
                    />
                  </td>
                  <td className="small muted mono">
                    {formatScheme(effective)}
                    {queued > 0 ? ` · ~${queued} в очереди` : ''}
                    {row.scheme === null ? ' (авто)' : ''}
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
        «Сейчас действует» показано для среднего числа категорий декады —
        у конкретного уровня категорий может быть больше или меньше, схема
        подрезается по факту. Правка коридора подрезает и план категорий блока.
        Схема записывается в спек уровня и входит в хеш пакета. Пресет 201-210
        таблица не трогает.
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
