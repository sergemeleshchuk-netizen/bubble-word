/**
 * Таблица стартовой раскладки по декадам.
 *
 * Формат — решение владельца 03.08: на каждый промежуток уровней — шары-слова
 * на старте (min/max), коридор категорий (min/max) и ВИЛКА схем выкладки:
 *
 *   декада | шаров на старте | категорий | схема min | схема max
 *   1-10   | 16-20           | 5-12      | 4-3-3-3-2-1 | 4-4-3-3-3-2-1
 *
 * Уровень с минимумом категорий коридора получает схему min, с максимумом —
 * схему max, между ними схема интерполируется (resolveScheme в core/deal.ts).
 *
 * «Шаров на старте» была расчётной колонкой (суммы схем вилки) и всегда
 * упиралась в вместимость поля — то есть врала: в оригинале старт доходит до 24
 * постепенно, на записанных уровнях первой декады он занимает 16-24 пузыря.
 * Теперь это настройка: max подрезает стартовое поле, min проверяется приёмкой
 * выкладки. Сумма схемы видна в самой схеме, дублировать её колонкой не нужно.
 *
 * Сетка строк: до 100 подекадно, 101-200 по 20, 201-1000 по 100, дальше по
 * 1000 до 5000 — ручной дизайн у оригинала виден в начале кривой, с ~L300
 * статистика замерзает, и строк на каждую декаду там не из чего заполнять.
 *
 * Живёт на первой вкладке: это настройка ИНСТРУМЕНТА на всю кривую, а не
 * одного блока. Правки переживают перезагрузку (localStorage в App) и
 * применяются к сборке блока по номеру его первого уровня.
 *
 * Таблица — ЧЕРНОВИК до кнопки «Сохранить и применить» (решение владельца
 * 04.08). Раньше каждое нажатие клавиши уезжало в localStorage и молча
 * становилось действующей настройкой, но на конфиг блока не влияло до
 * следующей сборки — то есть настройка была применена и не применена
 * одновременно, и по экранам это было никак не видно. Теперь применение
 * одно, явное, и оно же переписывает конфиг текущего блока: включая пресет
 * 201-210 — человек, нажавший «применить», сильнее закрепления пресета
 * (`presetLocked`), которое защищает только автоматический путь.
 */
import { useEffect, useState } from 'react';
import {
  decadeTuningDefaults, formatScheme, liteSchemePreview, parseScheme,
} from '../core/decadeProfiles.ts';
import type { DecadeTuningRow } from '../core/decadeProfiles.ts';
import { BOARD_CAPACITY } from '../core/levelMath.ts';

function sum(scheme: readonly number[]): number {
  return scheme.reduce((a, b) => a + b, 0);
}

/** Сколько пузырей реально даст схема строки на краях коридора. */
function schemeSums(row: DecadeTuningRow): [number, number] {
  const cap = row.startBubbles[1];
  const minScheme = row.schemeMin ?? row.schemeMax
    ?? liteSchemePreview(row.corridor[0], 4, cap);
  const maxScheme = row.schemeMax ?? row.schemeMin
    ?? liteSchemePreview(row.corridor[1], 4, cap);
  const a = sum(minScheme);
  const b = sum(maxScheme);
  return a <= b ? [a, b] : [b, a];
}

export function DecadeTable({ rows, onApply, appliedTo }: {
  /** действующий конфиг: то, по чему собирается блок */
  rows: DecadeTuningRow[];
  onApply: (next: DecadeTuningRow[]) => void;
  /**
   * Диапазон уровней текущего конфига блока — только для подписи под кнопкой.
   * Человеку нужно видеть, какая именно строка таблицы уедет в его блок:
   * применяется та, в которую попадает первый уровень диапазона.
   */
  appliedTo?: [number, number];
}) {
  const applied = [...rows].sort((a, b) => a.from - b.from);
  const defaults = decadeTuningDefaults();
  /**
   * Черновик таблицы. Правки живут здесь и не влияют ни на что до кнопки.
   */
  const [draft, setDraft] = useState<DecadeTuningRow[]>(applied);
  const appliedKey = JSON.stringify(applied);
  // внешняя смена действующего конфига (загрузка из localStorage, «умолчания»
  // из другого места) обязана попасть в черновик: иначе таблица показывала бы
  // числа, которых в конфиге больше нет
  useEffect(() => { setDraft(applied); }, [appliedKey]);

  const sorted = draft;
  const dirty = JSON.stringify(sorted) !== appliedKey;
  const isDefault = JSON.stringify(sorted) === JSON.stringify(defaults);
  const appliedRow = appliedTo
    ? sorted.find((r) => r.from <= appliedTo[0]
      && !sorted.some((o) => o.from <= appliedTo[0] && o.from > r.from))
    : undefined;

  const update = (from: number, patch: Partial<DecadeTuningRow>) => {
    setDraft(sorted.map((r) => (r.from === from ? { ...r, ...patch } : r)));
  };

  return (
    <div className="panel">
      <h2>Стартовая раскладка по декадам</h2>
      <p className="hint">
        «Шаров на старте» — бюджет стартового поля на промежуток: max подрезает
        поле (в оригинале первая декада встречает игрока 16-20 пузырями, полные
        24 приходят к L11-20 и дальше остаются), min — сколько пузырей старт
        обязан набрать, если материала хватает. Схема — доли категорий на старте
        по убыванию: <span className="mono">4-3-3-3-2-1</span> — одна категория
        целиком (вход), три по тройке, пара и одиночка. Уровень с минимумом
        категорий коридора получает схему min, с максимумом — схему max, между
        ними раскладка интерполируется. Пустые схемы — автоматическая
        облегчённая раздача: вход целиком, остальным минимум пара, без одиночек.
      </p>
      <div style={{ overflowX: 'auto' }}>
        <table>
          <thead>
            <tr>
              <th>декада</th>
              <th>шаров min</th>
              <th>max</th>
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
              const live = applied.find((a) => a.from === row.from);
              const pending = !live || JSON.stringify(live) !== JSON.stringify(row);
              const sums = schemeSums(row);
              const cap = row.startBubbles[1];
              return (
                <tr key={row.from} className={edited ? 'selected' : undefined}>
                  <td className="mono">
                    {row.from}-{row.to}
                    {pending && <div className="note">не применено</div>}
                    {!pending && appliedRow?.from === row.from
                      && <div className="note">в текущем блоке</div>}
                  </td>
                  <td>
                    <NumField
                      value={row.startBubbles[0]} min={4} max={row.startBubbles[1]}
                      onCommit={(n) => update(row.from,
                        { startBubbles: [n, row.startBubbles[1]] })}
                    />
                  </td>
                  <td>
                    <NumField
                      value={cap} min={row.startBubbles[0]} max={BOARD_CAPACITY}
                      onCommit={(n) => update(row.from,
                        { startBubbles: [row.startBubbles[0], n] })}
                    />
                  </td>
                  <td>
                    <NumField
                      value={row.corridor[0]} min={3} max={row.corridor[1]}
                      onCommit={(n) => update(row.from, { corridor: [n, row.corridor[1]] })}
                    />
                  </td>
                  <td>
                    <NumField
                      value={row.corridor[1]} min={row.corridor[0]} max={18}
                      onCommit={(n) => update(row.from, { corridor: [row.corridor[0], n] })}
                    />
                  </td>
                  <td>
                    <SchemeField
                      value={row.schemeMin}
                      placeholder={`авто: ${formatScheme(
                        liteSchemePreview(row.corridor[0], 4, cap))} = ${sums[0]}`}
                      onCommit={(schemeMin) => update(row.from, { schemeMin })}
                    />
                  </td>
                  <td>
                    <SchemeField
                      value={row.schemeMax}
                      placeholder={`авто: ${formatScheme(
                        liteSchemePreview(row.corridor[1], 4, cap))} = ${sums[1]}`}
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
        <button
          className="primary"
          disabled={!dirty}
          onClick={() => onApply(sorted)}
        >
          Сохранить и применить
        </button>
        {dirty && (
          <button className="ghost" onClick={() => setDraft(applied)}>
            отменить правки
          </button>
        )}
        {!isDefault && (
          <button className="ghost" onClick={() => setDraft(decadeTuningDefaults())}>
            вернуть умолчания
          </button>
        )}
      </div>
      <p className="hint">
        {dirty
          ? 'Правки в черновике: на сборку блока они не влияют, пока не применены.'
          : 'Конфиг применён и сохранён — блок собирается по нему.'}
        {appliedRow && (
          <>
            {' '}Текущему блоку (уровни {appliedTo?.[0]}-{appliedTo?.[1]}) достаётся
            строка <span className="mono">{appliedRow.from}-{appliedRow.to}</span>:
            категорий <span className="mono">
              {appliedRow.corridor[0]}-{appliedRow.corridor[1]}
            </span>. Своего поля у коридора на шаге «Настройка блока» нет — он
            предустановка кривой и правится здесь.
          </>
        )}
      </p>
      {/*
        Абзац с оговорками под таблицей убран (решение владельца 04.08): пять
        правил подряд про хеш пакета, целевое среднее коридора и неприкосновенность
        пресета читателю таблицы не нужны — он пришёл поправить числа. Сами правила
        никуда не делись, они в шапке этого файла и в `core/decadeProfiles.ts`,
        где им и место.
      */}
    </div>
  );
}

/**
 * Числовая ячейка с черновиком.
 *
 * Без черновика ячейки таблицы были нередактируемы, и это не мелочь: поле
 * полностью управляемое, а проверка отвергала промежуточный ввод. Чтобы
 * поставить в потолок коридора 13 вместо 12, нужно было набрать «1» — а «1»
 * меньше пола 8, значение не принималось, и в поле возвращалось прежнее «12».
 * Ни одну двузначную границу изменить было нельзя вовсе.
 *
 * Поведение теперь то же, что у полей Composer: пока набранное не проходит
 * границы, оно живёт в черновике и подсвечивается, в таблицу не уезжает, а на
 * выходе из поля черновик отбрасывается.
 */
function NumField({ value, min, max, onCommit }: {
  value: number;
  min: number;
  max: number;
  onCommit: (n: number) => void;
}) {
  const [draft, setDraft] = useState<string | null>(null);
  const [pending, setPending] = useState(false);

  return (
    <input
      type="text" inputMode="numeric" style={{ width: 52 }}
      className={pending ? 'pending' : undefined}
      value={draft ?? String(value)}
      onChange={(e) => {
        const raw = e.target.value;
        setDraft(raw);
        const n = Number(raw.trim());
        const ok = raw.trim() !== '' && Number.isInteger(n) && n >= min && n <= max;
        setPending(!ok);
        if (ok) onCommit(n);
      }}
      onFocus={(e) => e.currentTarget.select()}
      onBlur={() => { setDraft(null); setPending(false); }}
    />
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
