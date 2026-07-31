/**
 * Экран 5 — играбельный прототип.
 *
 * Это не клон целевой игры, а проверка того, что уровень действительно
 * собирается руками: имена категорий скрыты, игрок сам должен увидеть связь,
 * ошибочный мердж подсвечивается, ходы тратятся, собранная категория остаётся
 * на поле мета-пузырём и может войти в следующую.
 *
 * Досыпка воспроизведена: на поле одновременно не больше board_capacity пузырей,
 * остальные ждут очереди — так в целевой игре (наблюдение по видеозаписям).
 */
import { useEffect, useMemo, useState } from 'react';
import type { GeneratedLevel, LevelSpec } from '../core/types.ts';

interface Bubble {
  id: number;
  words: string[];
  /** категория, если пузырь уже собран целиком */
  completedCategory?: string;
  x: number;
  y: number;
  size: number;
}

const COLORS = ['#2f6f9f', '#2f8f6f', '#6f4f9f', '#c8781f'];

function bubblesOf(spec: LevelSpec): { board: Bubble[]; queue: Bubble[] } {
  const all: Bubble[] = [];
  let id = 0;
  for (const category of spec.categories) {
    for (const word of category.words) {
      // мета-слово не спавнится на старте: оно появится, когда соберут дочернюю
      if (word.kind === 'meta') continue;
      all.push({ id: id += 1, words: [word.text], x: 0, y: 0, size: 0 });
    }
  }
  // Детерминированная раскладка сеткой: одинаковый уровень выглядит одинаково.
  // Раньше здесь была формула вида (i * 37) % 74 — она давала ровно две колонки,
  // потому что множитель и модуль не взаимно просты, и пузыри слипались в столбики.
  const COLS = 4;
  const placed = all.map((b, i) => ({
    ...b,
    x: 15 + (i % COLS) * 23 + ((i * 5) % 4),
    y: 7 + Math.floor(i / COLS) * 15 + ((i * 3) % 4),
    size: 0,
  }));
  const capacity = spec.board.boardCapacity;
  return { board: placed.slice(0, capacity), queue: placed.slice(capacity) };
}

export function Playable({ level, levels, onSelect }: {
  level: GeneratedLevel;
  levels: GeneratedLevel[];
  onSelect: (id: number) => void;
}) {
  const spec = level.spec;
  const [state, setState] = useState(() => bubblesOf(spec));
  const [picked, setPicked] = useState<number | null>(null);
  const [bad, setBad] = useState<number | null>(null);
  const [moves, setMoves] = useState(spec.board.moveLimit);
  const [done, setDone] = useState<string[]>([]);
  const [showDev, setShowDev] = useState(false);

  useEffect(() => {
    setState(bubblesOf(spec));
    setPicked(null);
    setMoves(spec.board.moveLimit);
    setDone([]);
  }, [spec]);

  /** слово → ключ категории, где оно живёт (истина уровня, игроку не показывается) */
  const homeOf = useMemo(() => {
    const map = new Map<string, string>();
    for (const c of spec.categories) for (const w of c.words) map.set(w.text, c.key);
    return map;
  }, [spec]);

  const sizeFor = (words: string[]) => 44 + words.length * 7;

  const merge = (aId: number, bId: number) => {
    const a = state.board.find((b) => b.id === aId)!;
    const b = state.board.find((x) => x.id === bId)!;
    const merged = [...a.words, ...b.words];
    const homes = new Set(merged.map((w) => homeOf.get(w)));

    if (homes.size !== 1 || merged.length > spec.board.wordsPerCategory) {
      setBad(bId);
      setTimeout(() => setBad(null), 320);
      return;                                    // ошибочный мердж хода не тратит
    }

    const categoryKey = merged[0] ? homeOf.get(merged[0])! : '';
    const complete = merged.length === spec.board.wordsPerCategory;
    setMoves((m) => m - 1);

    setState((prev) => {
      let board = prev.board.filter((x) => x.id !== aId && x.id !== bId);
      const queue = [...prev.queue];

      if (complete) {
        const category = spec.categories.find((c) => c.key === categoryKey)!;
        setDone((d) => [...d, category.label]);
        // собранная категория остаётся на поле мета-пузырём, если она чей-то ребёнок
        const parent = spec.categories.find((c) =>
          c.words.some((w) => w.kind === 'meta' && w.metaChild === categoryKey));
        if (parent) {
          board.push({ id: 10000 + board.length, words: [category.label],
            completedCategory: categoryKey, x: a.x, y: a.y, size: 0 });
        }
      } else {
        board.push({ ...a, id: a.id, words: merged });
      }

      // досыпка: поле держит не больше capacity пузырей
      while (board.length < spec.board.boardCapacity && queue.length) {
        board.push(queue.shift()!);
      }
      return { board, queue };
    });
    setPicked(null);
  };

  const tap = (id: number) => {
    if (moves <= 0) return;
    if (picked === null) { setPicked(id); return; }
    if (picked === id) { setPicked(null); return; }
    merge(picked, id);
  };

  const total = spec.categories.length;
  const solved = done.length;

  return (
    <>
      <div className="panel">
        <div className="spread">
          <div>
            <h2>Играбельный прототип</h2>
            <p className="hint">
              Имена категорий скрыты — их надо угадать. Тапните два пузыря, чтобы
              объединить. Ошибка подсвечивается и хода не тратит. Собранная категория
              остаётся на поле, если она входит в другую.
            </p>
          </div>
          <div className="row">
            {levels.map((l) => (
              <button key={l.spec.levelId}
                className={`ghost ${l.spec.levelId === spec.levelId ? 'on' : ''}`}
                onClick={() => onSelect(l.spec.levelId)}>{l.spec.levelId}</button>
            ))}
            <button className="ghost" onClick={() => {
              setState(bubblesOf(spec)); setMoves(spec.board.moveLimit);
              setDone([]); setPicked(null);
            }}>Сброс</button>
            <button className={`ghost ${showDev ? 'on' : ''}`}
              onClick={() => setShowDev((v) => !v)}>Показать ответы</button>
          </div>
        </div>
      </div>

      <div className="panel">
        <div className="phone">
          <div className="hud">
            <span>MOVES {Math.max(0, moves)}</span>
            <span>{solved}/{total}</span>
            <span>в очереди {state.queue.length}</span>
          </div>
          <div style={{ position: 'absolute', inset: '44px 0 0 0' }}>
            {state.board.map((b) => {
              const size = sizeFor(b.words);
              const color = b.completedCategory
                ? COLORS[3]
                : COLORS[Math.min(b.words.length - 1, 2)];
              return (
                <div
                  key={b.id}
                  className={`bubble ${picked === b.id ? 'picked' : ''} ${bad === b.id ? 'bad' : ''}`}
                  style={{
                    left: `${b.x}%`, top: `${b.y}%`,
                    width: size, height: size, marginLeft: -size / 2, marginTop: -size / 2,
                    background: `radial-gradient(circle at 32% 28%, ${color}dd, ${color}88)`,
                    fontSize: b.words.length > 1 ? 8.5 : 10,
                    color: '#eaf4ff',
                    flexDirection: 'column',
                    zIndex: b.words.length,
                  }}
                  onClick={() => tap(b.id)}
                >
                  {b.words.map((w) => (
                    <div key={w} style={{ fontWeight: b.completedCategory ? 700 : 400 }}>
                      {w}
                    </div>
                  ))}
                </div>
              );
            })}
          </div>
          {solved === total && (
            <div style={{ position: 'absolute', inset: 0, display: 'flex',
              alignItems: 'center', justifyContent: 'center',
              background: 'rgba(4,20,30,0.86)', flexDirection: 'column', gap: 6 }}>
              <strong style={{ fontSize: 18 }}>Уровень собран</strong>
              <span className="muted small">
                осталось ходов: {moves} из {spec.board.moveLimit}
              </span>
            </div>
          )}
          {moves <= 0 && solved < total && (
            <div style={{ position: 'absolute', inset: 0, display: 'flex',
              alignItems: 'center', justifyContent: 'center',
              background: 'rgba(30,6,6,0.86)', flexDirection: 'column', gap: 6 }}>
              <strong style={{ fontSize: 18 }}>Ходы закончились</strong>
              <span className="muted small">собрано {solved} из {total}</span>
            </div>
          )}
        </div>

        <div className="row" style={{ justifyContent: 'center', marginTop: 12 }}>
          <span className="muted small">
            собрано: {done.join(' · ') || '—'}
          </span>
        </div>
      </div>

      {showDev && (
        <div className="panel">
          <h2>Ответы уровня</h2>
          <p className="hint">
            Оверлей для проверки. В настоящей игре игрок этого не видит.
          </p>
          {spec.categories.map((c) => (
            <div key={c.key} className="small" style={{ margin: '3px 0' }}>
              <strong>{c.label}</strong>
              <span className="muted"> — {c.words.map((w) =>
                w.kind === 'meta' ? `[${w.text}]` : w.text).join(', ')}</span>
            </div>
          ))}
          <p className="small muted" style={{ marginTop: 8 }}>
            В квадратных скобках — мета-пузыри: они появляются на поле только после
            того, как игрок соберёт соответствующую категорию.
          </p>
        </div>
      )}
    </>
  );
}
