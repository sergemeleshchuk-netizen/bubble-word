/**
 * Экран 5 — играбельный прототип.
 *
 * Это не клон целевой игры, а проверка того, что уровень действительно
 * собирается руками: имена категорий скрыты, игрок сам должен увидеть связь,
 * ошибочный мердж подсвечивается, ходы тратятся, собранная категория остаётся
 * на поле мета-пузырём и может войти в следующую.
 *
 * Драг вместо тапа. В целевой игре пузырь тащат, и по дороге подсвечиваются те
 * пузыри, над которыми он проходит: игрок видит траекторию и понимает, на каком
 * шаре будет остановка. Пока пузырь в руке, структура поля не меняется — место
 * не заполняется досыпкой, ничего не пересобирается. Реконфигурация происходит
 * только в момент финального решения, то есть после успешного мерджа. Неверный
 * мердж подсвечивает цель красным, пузырь возвращается на своё место, ход
 * не тратится.
 *
 * Модификаторы (половинки, лёд, «?», цепь) — отдельный слой поверх спека:
 * см. core/playableModifiers.ts, там объяснено, почему они не входят в level_spec.
 *
 * Досыпка воспроизведена: на поле одновременно не больше board_capacity пузырей,
 * остальные ждут очереди — так в целевой игре (наблюдение по видеозаписям).
 */
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import type { PointerEvent as ReactPointerEvent } from 'react';
import type { GeneratedLevel, LevelSpec } from '../core/types.ts';
import {
  MODIFIERS, buildSetup,
  type PlayableBubble, type PlayableModifier, type PlayableSetup,
} from '../core/playableModifiers.ts';

const COLORS = ['#2f6f9f', '#2f8f6f', '#6f4f9f', '#c8781f'];
const HALF_COLOR = '#3aa0d8';
const ICE_COLOR = '#7fb6cc';
const HIDDEN_COLOR = '#5c5f8f';

/** Причина отказа: цвет подсветки цели зависит от того, ошибка это или блокировка. */
type Reject = { id: number; reason: 'wrong' | 'ice' | 'hidden' | 'chain' } | null;

interface Board {
  board: PlayableBubble[];
  queue: PlayableBubble[];
}

const sizeOf = (b: PlayableBubble): number =>
  b.kind === 'half' ? 40 : 44 + b.words.length * 7;

function initial(setup: PlayableSetup): Board {
  // копия: состояние партии мутирует счётчики льда и «?»
  return {
    board: setup.board.map((b) => ({ ...b })),
    queue: setup.queue.map((b) => ({ ...b })),
  };
}

export function Playable({ level, levels, lexicon, onSelect }: {
  level: GeneratedLevel;
  levels: GeneratedLevel[];
  /** слова контентной базы: по ним проверяются фрагменты половинок */
  lexicon?: ReadonlySet<string>;
  onSelect: (id: number) => void;
}) {
  const spec: LevelSpec = level.spec;
  const [modifier, setModifier] = useState<PlayableModifier>('none');
  const setup = useMemo(() => buildSetup(spec, modifier, lexicon), [spec, modifier, lexicon]);

  const [state, setState] = useState<Board>(() => initial(setup));
  const [picked, setPicked] = useState<number | null>(null);
  const [reject, setReject] = useState<Reject>(null);
  const unlimited = setup.moveLimit === null;          // туториальный уровень
  const [moves, setMoves] = useState(setup.moveLimit ?? Infinity);
  const [done, setDone] = useState<string[]>([]);
  const [glued, setGlued] = useState(0);               // склеек половинок сделано
  const [rescue, setRescue] = useState<string | null>(null);
  const [chainHit, setChainHit] = useState(false);      // цепь мигает, когда в неё уперлись
  const [showDev, setShowDev] = useState(false);

  const boardRef = useRef<HTMLDivElement>(null);
  const grabRef = useRef<{ cx: number; cy: number; ox: number; oy: number } | null>(null);
  const [drag, setDrag] = useState<
    { id: number; dx: number; dy: number; over: number | null; trail: number[] } | null
  >(null);
  const [snap, setSnap] = useState<{ id: number; dx: number; dy: number } | null>(null);

  const reset = useCallback(() => {
    setState(initial(setup));
    setPicked(null);
    setReject(null);
    setMoves(setup.moveLimit ?? Infinity);
    setDone([]);
    setGlued(0);
    setRescue(null);
    setChainHit(false);
    setDrag(null);
    setSnap(null);
  }, [setup]);

  useEffect(reset, [reset]);

  /** слово → ключ категории, где оно живёт (истина уровня, игроку не показывается) */
  const homeOf = useMemo(() => {
    const map = new Map<string, string>();
    for (const c of spec.categories) for (const w of c.words) map.set(w.text, c.key);
    return map;
  }, [spec]);

  const chain = setup.chain;
  const chainDown = !chain || done.length >= chain.need || rescue !== null;
  const zoneOf = useCallback(
    (b: PlayableBubble) => (chain && setup.slots[b.slot].y > chain.y ? 1 : 0),
    [chain, setup.slots],
  );

  const blocked = (b: PlayableBubble) => b.ice > 0 || b.hidden > 0;

  /** Существует ли хоть один легальный мердж — страховка от запертой раскладки. */
  const hasLegalMove = useCallback((board: PlayableBubble[], withChain: boolean) => {
    const free = board.filter((b) => !blocked(b));
    for (let i = 0; i < free.length; i += 1) {
      for (let j = i + 1; j < free.length; j += 1) {
        const a = free[i];
        const b = free[j];
        if (withChain && zoneOf(a) !== zoneOf(b)) continue;
        if (a.kind === 'half' || b.kind === 'half') {
          if (a.kind === 'half' && b.kind === 'half'
            && a.pair!.id === b.pair!.id && a.pair!.side !== b.pair!.side) return true;
          continue;
        }
        const words = [...a.words, ...b.words];
        if (words.length > spec.board.wordsPerCategory) continue;
        if (new Set(words.map((w) => homeOf.get(w))).size === 1) return true;
      }
    }
    return false;
  }, [homeOf, spec.board.wordsPerCategory, zoneOf]);

  // Страховка. Лёд тает только от успешных мерджей, а цепь снимается только
  // сбором категорий: если легальных мерджей не осталось, игрок заперт навсегда.
  // Прототип в этом случае снимает препятствие и говорит об этом вслух — молча
  // показывать неразрешимое поле было бы хуже, чем признать ограничение раскладки.
  useEffect(() => {
    if (rescue || moves <= 0 || done.length === spec.categories.length) return;
    if (hasLegalMove(state.board, !chainDown)) return;
    if (chain && !chainDown) {
      setRescue('цепь снята автоматически: легального мерджа под ней не осталось');
      return;
    }
    if (state.board.some(blocked)) {
      setState((prev) => ({
        ...prev,
        board: prev.board.map((b) => ({ ...b, ice: 0, hidden: 0 })),
      }));
      setRescue('лёд растоплен и «?» раскрыты автоматически: '
        + 'других легальных мерджей на поле не осталось');
    }
  }, [state.board, chain, chainDown, done.length, hasLegalMove, moves, rescue,
    spec.categories.length]);

  /** Успешное действие: снимает слой льда и «?» со всего поля и тратит ход. */
  const applySuccess = (
    change: (board: PlayableBubble[], queue: PlayableBubble[]) => Board,
  ) => {
    if (!unlimited) setMoves((m) => m - 1);
    setState((prev) => {
      const next = change(prev.board.map((b) => ({ ...b })), prev.queue.slice());
      const board = next.board.map((b) => ({
        ...b,
        ice: Math.max(0, b.ice - 1),
        hidden: Math.max(0, b.hidden - 1),
      }));
      const queue = next.queue;
      const taken = new Set(board.map((b) => b.slot));
      // досыпка: поле держит не больше capacity пузырей, освободившийся слот
      // отдаётся следующему из очереди
      while (board.length < setup.slots.length && queue.length) {
        const slot = setup.refillOrder.find((s) => !taken.has(s));
        if (slot === undefined) break;
        taken.add(slot);
        board.push({ ...queue.shift()!, slot });
      }
      return { board, queue };
    });
    setPicked(null);
  };

  const fail = (id: number, reason: Exclude<Reject, null>['reason']) => {
    setReject({ id, reason });
    setTimeout(() => setReject(null), 420);
    setPicked(null);
  };

  /** Возвращает true, если действие состоялось (поле пересобирается). */
  const attempt = (aId: number, bId: number): boolean => {
    if (moves <= 0) return false;
    const a = state.board.find((x) => x.id === aId);
    const b = state.board.find((x) => x.id === bId);
    if (!a || !b || a.id === b.id) return false;

    if (b.ice > 0) { fail(bId, 'ice'); return false; }
    if (b.hidden > 0) { fail(bId, 'hidden'); return false; }
    if (!chainDown && zoneOf(a) !== zoneOf(b)) {
      // мигает и цель, и сама цепь: игрок должен понять, что помешала именно она,
      // а не то, что слова не связаны
      setChainHit(true);
      setTimeout(() => setChainHit(false), 420);
      fail(bId, 'chain');
      return false;
    }

    // половинки: сначала слово, потом категория
    if (a.kind === 'half' || b.kind === 'half') {
      const pairOk = a.kind === 'half' && b.kind === 'half'
        && a.pair!.id === b.pair!.id && a.pair!.side !== b.pair!.side;
      if (!pairOk) { fail(bId, 'wrong'); return false; }
      const whole = a.pair!.whole;
      setGlued((g) => g + 1);
      applySuccess((board, queue) => ({
        board: board
          .filter((x) => x.id !== bId)
          .map((x) => (x.id === aId
            ? { ...x, kind: 'word' as const, words: [whole], pair: undefined }
            : x)),
        queue,
      }));
      return true;
    }

    const merged = [...a.words, ...b.words];
    const homes = new Set(merged.map((w) => homeOf.get(w)));
    if (homes.size !== 1 || merged.length > spec.board.wordsPerCategory) {
      fail(bId, 'wrong');
      return false;
    }

    const categoryKey = homeOf.get(merged[0])!;
    const complete = merged.length === spec.board.wordsPerCategory;
    if (complete) {
      const category = spec.categories.find((c) => c.key === categoryKey)!;
      setDone((d) => [...d, category.label]);
    }
    applySuccess((board, queue) => {
      let next = board.filter((x) => x.id !== aId && x.id !== bId);
      if (complete) {
        const category = spec.categories.find((c) => c.key === categoryKey)!;
        // собранная категория остаётся на поле мета-пузырём, если она чей-то ребёнок
        const parent = spec.categories.find((c) =>
          c.words.some((w) => w.kind === 'meta' && w.metaChild === categoryKey));
        if (parent) {
          next.push({
            id: 10000 + next.length, kind: 'meta', words: [category.label],
            completedCategory: categoryKey, ice: 0, hidden: 0, slot: a.slot,
          });
        }
      } else {
        next = next.concat([{ ...a, words: merged }]);
      }
      return { board: next, queue };
    });
    return true;
  };

  // ------------------------------------------------------------------ драг
  const centerOf = (b: PlayableBubble, rect: DOMRect) => ({
    x: (setup.slots[b.slot].x / 100) * rect.width,
    y: (setup.slots[b.slot].y / 100) * rect.height,
  });

  const onPointerDown = (e: ReactPointerEvent, b: PlayableBubble) => {
    if (moves <= 0 || done.length === spec.categories.length) return;
    if (blocked(b)) { fail(b.id, b.ice > 0 ? 'ice' : 'hidden'); return; }
    const rect = boardRef.current?.getBoundingClientRect();
    if (!rect) return;
    const c = centerOf(b, rect);
    grabRef.current = { cx: e.clientX, cy: e.clientY, ox: c.x, oy: c.y };
    // захват указателя: без него драг рвётся, когда курсор уходит с пузыря.
    // В try, потому что при синтетических событиях (автотесты) захватывать нечего
    try { e.currentTarget.setPointerCapture?.(e.pointerId); } catch { /* нечего захватывать */ }
    setDrag({ id: b.id, dx: 0, dy: 0, over: null, trail: [] });
    setSnap(null);
  };

  const onPointerMove = (e: ReactPointerEvent) => {
    const grab = grabRef.current;
    const rect = boardRef.current?.getBoundingClientRect();
    if (!grab || !rect || !drag) return;
    const dx = e.clientX - grab.cx;
    const dy = e.clientY - grab.cy;
    const px = grab.ox + dx;
    const py = grab.oy + dy;
    let over: number | null = null;
    let best = Infinity;
    for (const b of state.board) {
      if (b.id === drag.id) continue;
      const c = centerOf(b, rect);
      const d = Math.hypot(c.x - px, c.y - py);
      if (d < sizeOf(b) / 2 + 10 && d < best) { best = d; over = b.id; }
    }
    setDrag((prev) => {
      if (!prev) return prev;
      const trail = over !== null && !prev.trail.includes(over)
        ? [...prev.trail, over].slice(-6)
        : prev.trail;
      return { ...prev, dx, dy, over, trail };
    });
  };

  const onPointerUp = () => {
    const d = drag;
    grabRef.current = null;
    setDrag(null);
    if (!d) return;
    const tap = Math.abs(d.dx) < 6 && Math.abs(d.dy) < 6;
    if (tap) {
      // тап-тап оставлен как альтернатива драгу: удобнее мышью на длинных полях
      if (picked === null) setPicked(d.id);
      else if (picked === d.id) setPicked(null);
      else attempt(picked, d.id);
      return;
    }
    const merged = d.over !== null && attempt(d.id, d.over);
    if (!merged) {
      // пузырь возвращается на своё место: поле за время драга не менялось
      setSnap({ id: d.id, dx: d.dx, dy: d.dy });
      requestAnimationFrame(() => requestAnimationFrame(() =>
        setSnap((s) => (s && s.id === d.id ? { ...s, dx: 0, dy: 0 } : s))));
      setTimeout(() => setSnap((s) => (s && s.id === d.id ? null : s)), 400);
    }
  };

  const total = spec.categories.length;
  const solved = done.length;
  const won = solved === total;
  const lost = moves <= 0 && !won;
  const iceLeft = state.board.filter((b) => b.ice > 0).length;
  const hiddenLeft = state.board.filter((b) => b.hidden > 0).length;
  const halvesLeft = state.board.filter((b) => b.kind === 'half').length
    + state.queue.filter((b) => b.kind === 'half').length;
  const modifierMeta = MODIFIERS.find((m) => m.id === modifier)!;

  return (
    <>
      <div className="panel">
        <div className="spread">
          <div>
            <h2>Играбельный прототип</h2>
            <p className="hint">
              Имена категорий скрыты — их надо угадать. Тащите пузырь: по дороге
              подсвечиваются те, над которыми он проходит, обведённый — точка
              остановки. Неверный мердж подсвечивает цель красным, пузырь
              возвращается на место, ход не тратится. Поле пересобирается только
              после удачного мерджа.
            </p>
          </div>
          <div className="row">
            {levels.map((l) => (
              <button key={l.spec.levelId}
                className={`ghost ${l.spec.levelId === spec.levelId ? 'on' : ''}`}
                onClick={() => onSelect(l.spec.levelId)}>{l.spec.levelId}</button>
            ))}
            <button className="ghost" onClick={reset}>Сброс</button>
            <button className={`ghost ${showDev ? 'on' : ''}`}
              onClick={() => setShowDev((v) => !v)}>Показать ответы</button>
          </div>
        </div>

        <div className="row" style={{ marginTop: 12, alignItems: 'baseline' }}>
          <span className="small muted">модификатор:</span>
          {MODIFIERS.map((m) => (
            <button key={m.id} className={`ghost ${modifier === m.id ? 'on' : ''}`}
              onClick={() => setModifier(m.id)}>{m.label}</button>
          ))}
        </div>
        <p className="hint" style={{ marginBottom: 0 }}>{modifierMeta.hint}</p>
        {setup.notes.length > 0 && (
          <ul className="small muted" style={{ margin: '6px 0 0', paddingLeft: 18 }}>
            {setup.notes.map((n) => <li key={n}>{n}</li>)}
          </ul>
        )}
      </div>

      <div className="panel">
        <div className="phone">
          <div className="hud">
            <span>MOVES {unlimited ? '∞' : Math.max(0, moves)}</span>
            <span>{solved}/{total}</span>
            <span>в очереди {state.queue.length}</span>
          </div>
          <div className="board" ref={boardRef}>
            {chain && (
              <div className={`chain ${chainDown ? 'off' : ''} ${chainHit ? 'hit' : ''}`}
                style={{ top: `${chain.y}%` }}>
                <span className="chain-badge">
                  {chainDown ? 'цепь снята' : `${Math.min(solved, chain.need)}/${chain.need}`}
                </span>
              </div>
            )}

            {/* Метка покинутого места: показывает, что слот держится за пузырём и
                досыпка его не занимает, пока шар в руке. Линии-траектории здесь
                нет сознательно — путь читается по подсветке пройденных пузырей. */}
            {drag && (() => {
              const from = setup.slots[state.board.find((b) => b.id === drag.id)?.slot ?? 0];
              return (
                <div className="slot-ghost" style={{ left: `${from.x}%`, top: `${from.y}%` }} />
              );
            })()}

            {state.board.map((b) => {
              const slot = setup.slots[b.slot];
              const size = sizeOf(b);
              const dragged = drag?.id === b.id;
              const snapping = snap?.id === b.id;
              const offset = dragged ? drag! : snapping ? snap! : null;
              const color = b.hidden > 0 ? HIDDEN_COLOR
                : b.ice > 0 ? ICE_COLOR
                : b.kind === 'half' ? HALF_COLOR
                : b.completedCategory ? COLORS[3]
                : COLORS[Math.min(b.words.length - 1, 2)];
              const classes = ['bubble'];
              if (picked === b.id) classes.push('picked');
              if (dragged) classes.push('dragging');
              if (snapping) classes.push('snapping');
              if (drag?.over === b.id) classes.push('over');
              else if (drag?.trail.includes(b.id)) classes.push('trail');
              if (reject?.id === b.id) classes.push(reject.reason === 'wrong' ? 'bad' : 'blocked');
              if (b.ice > 0) classes.push('iced');
              if (b.hidden > 0) classes.push('veiled');
              if (b.kind === 'half') classes.push('half');
              return (
                <div
                  key={b.id}
                  className={classes.join(' ')}
                  style={{
                    left: `${slot.x}%`, top: `${slot.y}%`,
                    width: size, height: size,
                    marginLeft: -size / 2, marginTop: -size / 2,
                    background: `radial-gradient(circle at 32% 28%, ${color}dd, ${color}88)`,
                    fontSize: b.words.length > 1 ? 8.5 : 10,
                    color: '#eaf4ff',
                    flexDirection: 'column',
                    transform: offset
                      ? `translate(${offset.dx}px, ${offset.dy}px)${dragged ? ' scale(1.08)' : ''}`
                      : undefined,
                    zIndex: dragged ? 50 : snapping ? 40 : b.words.length,
                  }}
                  onPointerDown={(e) => onPointerDown(e, b)}
                  onPointerMove={onPointerMove}
                  onPointerUp={onPointerUp}
                  onPointerCancel={onPointerUp}
                >
                  {b.hidden > 0 ? (
                    <>
                      <div style={{ fontSize: 18, fontWeight: 700 }}>?</div>
                      <div className="counter">{b.hidden}</div>
                    </>
                  ) : (
                    <>
                      {b.words.map((w) => (
                        <div key={w} style={{ fontWeight: b.completedCategory ? 700 : 400 }}>
                          {b.kind === 'half' ? (b.pair!.side === 0 ? `${w}·` : `·${w}`) : w}
                        </div>
                      ))}
                      {b.ice > 0 && <div className="counter">❄ {b.ice}</div>}
                    </>
                  )}
                </div>
              );
            })}
          </div>

          {won && (
            <div className="verdict ok">
              <strong style={{ fontSize: 18 }}>Уровень собран</strong>
              <span className="muted small">
                {unlimited
                  ? 'лимита ходов нет: туториальный уровень'
                  : `осталось ходов: ${moves} из ${setup.moveLimit}`}
              </span>
            </div>
          )}
          {lost && (
            <div className="verdict fail">
              <strong style={{ fontSize: 18 }}>Ходы закончились</strong>
              <span className="muted small">собрано {solved} из {total}</span>
            </div>
          )}
        </div>

        <div className="row" style={{ justifyContent: 'center', marginTop: 12, flexWrap: 'wrap' }}>
          <span className="muted small">собрано: {done.join(' · ') || '—'}</span>
          {modifier === 'halves' && (
            <span className="muted small">· половинок на поле {halvesLeft}, склеек {glued}</span>
          )}
          {modifier === 'ice' && <span className="muted small">· под льдом {iceLeft}</span>}
          {modifier === 'hidden' && <span className="muted small">· закрыто {hiddenLeft}</span>}
          {chain && (
            <span className="muted small">
              · цепь {chainDown ? 'снята' : `держится (${solved}/${chain.need})`}
            </span>
          )}
        </div>
        {rescue && <p className="hint" style={{ textAlign: 'center' }}>{rescue}</p>}
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
          {modifier === 'halves' && (
            <p className="small muted">
              Половинки:{' '}
              {[...setup.board, ...setup.queue]
                .filter((b) => b.kind === 'half' && b.pair!.side === 0)
                .map((b) => b.pair!.whole).join(', ') || '—'}
            </p>
          )}
        </div>
      )}
    </>
  );
}
