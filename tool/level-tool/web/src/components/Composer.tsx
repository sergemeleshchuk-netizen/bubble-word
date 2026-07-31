/**
 * Экраны 2 и 3 — Настройка блока и Генерация.
 *
 * Главное требование к этому экрану: ритм блока должен быть виден ГЛАЗОМ.
 * Блок из 10 уровней — композиция, а не десять растущих строк: рост, пик,
 * передышка, второй пик, приятный выход. Таблица из чисел этого не показывает,
 * поэтому здесь график.
 */
import { useState } from 'react';
import type { BlockConfig, BlockResult, GeneratedLevel, LevelPlan } from '../core/types.ts';
import { parseIntent, type ParsedIntent } from '../core/intentParser.ts';
import { startBubbles } from '../core/levelMath.ts';
import {
  configForRange, decadeLabel, profileForRange, visibleShareMin,
} from '../core/decadeProfiles.ts';

const ROLE_LABEL: Record<string, string> = {
  entry: 'вход', growth: 'рост', recovery: 'передышка',
  peak: 'пик', spike: 'спайк', exit: 'выход',
};

// --------------------------------------------------------------------------- //
// график ритма
// --------------------------------------------------------------------------- //

export function RhythmChart({ plans, levels }: {
  plans: LevelPlan[]; levels?: GeneratedLevel[];
}) {
  const W = 900;
  const H = 260;
  const padL = 34;
  const padR = 14;
  const padT = 14;
  const padB = 46;
  const innerW = W - padL - padR;
  const innerH = H - padT - padB;
  const step = innerW / plans.length;

  const maxBubbles = Math.max(...plans.map((p) =>
    startBubbles(p.categoryCount, p.metaCount)), 40);
  const yScore = (v: number) => padT + innerH - (v / 10) * innerH;
  const xCenter = (i: number) => padL + step * (i + 0.5);

  const byId = new Map((levels ?? []).map((l) => [l.spec.levelId, l]));
  const dPoints = plans.map((p, i) => {
    const level = byId.get(p.levelId);
    return level ? `${xCenter(i)},${yScore(level.difficulty.value)}` : null;
  }).filter(Boolean).join(' ');
  const iPoints = plans.map((p, i) => {
    const level = byId.get(p.levelId);
    return level ? `${xCenter(i)},${yScore(level.interest.value)}` : null;
  }).filter(Boolean).join(' ');

  return (
    <div style={{ overflowX: 'auto' }}>
      <svg viewBox={`0 0 ${W} ${H}`} style={{ width: '100%', minWidth: 620 }}>
        {[0, 2, 4, 6, 8, 10].map((v) => (
          <g key={v}>
            <line x1={padL} x2={W - padR} y1={yScore(v)} y2={yScore(v)}
              stroke="#2a3441" strokeWidth={1} />
            <text x={padL - 6} y={yScore(v) + 4} fill="#8b98a6" fontSize={10}
              textAnchor="end">{v}</text>
          </g>
        ))}

        {plans.map((plan, i) => {
          const bubbles = startBubbles(plan.categoryCount, plan.metaCount);
          const barH = (bubbles / maxBubbles) * innerH * 0.94;
          const level = byId.get(plan.levelId);
          const isPeak = plan.role === 'peak' || plan.role === 'spike';
          const isRest = plan.role === 'recovery';
          return (
            <g key={plan.levelId}>
              {/* коридор целевой сложности */}
              <rect
                x={xCenter(i) - step * 0.34}
                y={yScore(plan.targetDifficulty[1])}
                width={step * 0.68}
                height={Math.max(2, yScore(plan.targetDifficulty[0])
                  - yScore(plan.targetDifficulty[1]))}
                fill="#4cc2ff" opacity={0.09}
              />
              {/* объём */}
              <rect
                x={xCenter(i) - step * 0.22}
                y={padT + innerH - barH}
                width={step * 0.44}
                height={barH}
                fill={isPeak ? '#3a2a1c' : isRest ? '#16281c' : '#1c2430'}
                stroke={isPeak ? '#ff9e64' : isRest ? '#3fb950' : '#2a3441'}
                strokeWidth={1}
                rx={2}
              />
              <text x={xCenter(i)} y={padT + innerH - barH - 4} fill="#8b98a6"
                fontSize={9} textAnchor="middle">{bubbles}</text>

              <text x={xCenter(i)} y={H - 28} fill="#e6edf3" fontSize={10}
                textAnchor="middle" className="mono">{plan.levelId}</text>
              <text x={xCenter(i)} y={H - 16} fill={isPeak ? '#ff9e64'
                : isRest ? '#3fb950' : '#8b98a6'} fontSize={9} textAnchor="middle">
                {ROLE_LABEL[plan.role]}
              </text>
              <text x={xCenter(i)} y={H - 5} fill="#8b98a6" fontSize={8.5}
                textAnchor="middle">
                {plan.categoryCount} кат · {plan.metaCount} мета
              </text>

              {level && (
                <>
                  <circle cx={xCenter(i)} cy={yScore(level.difficulty.value)} r={3.6}
                    fill="#f85149" />
                  <circle cx={xCenter(i)} cy={yScore(level.interest.value)} r={3.6}
                    fill="#3fb950" />
                </>
              )}
            </g>
          );
        })}

        {dPoints && <polyline points={dPoints} fill="none" stroke="#f85149" strokeWidth={2} />}
        {iPoints && <polyline points={iPoints} fill="none" stroke="#3fb950" strokeWidth={2} />}
      </svg>
      <div className="row small muted" style={{ marginTop: 4 }}>
        <span><span style={{ color: '#f85149' }}>●</span> сложность D</span>
        <span><span style={{ color: '#3fb950' }}>●</span> интересность I</span>
        <span><span style={{ color: '#8b98a6' }}>▮</span> пузырей на старте</span>
        <span><span style={{ color: '#4cc2ff' }}>▮</span> целевой коридор D</span>
      </div>
    </div>
  );
}

// --------------------------------------------------------------------------- //
// экран 2: настройка
// --------------------------------------------------------------------------- //

export function Composer({ config, onChange, plans, rhythm, onGenerate, knownThemes }: {
  config: BlockConfig;
  onChange: (c: BlockConfig) => void;
  plans: LevelPlan[];
  rhythm: { passed: boolean; issues: string[] };
  onGenerate: () => void;
  knownThemes: string[];
}) {
  const [text, setText] = useState(
    'Еда и путешествия, без спорта, два пика, передышка после каждого пика, '
    + 'несколько честных ловушек на цветах, побольше редких слов.');
  const [parsed, setParsed] = useState<ParsedIntent | null>(null);
  const decade = profileForRange(config.levelRange);

  const patch = (p: Partial<BlockConfig>) => onChange({ ...config, ...p });
  const nums = (v: string) => v.split(/[^0-9]+/).filter(Boolean).map(Number);

  const interpret = () => setParsed(parseIntent(text));
  const applyParsed = () => {
    if (parsed) onChange({ ...config, ...parsed.patch });
    setParsed(null);
  };

  return (
    <>
      <div className="panel">
        <h2>Свободное пожелание</h2>
        <p className="hint">
          Напишите словами, каким должен быть блок. Инструмент показывает, как понял
          ваши слова, и вы правите интерпретацию <strong>до</strong> генерации —
          иначе непонятно, что именно пошло в фильтр.
        </p>
        <textarea value={text} onChange={(e) => setText(e.target.value)} />
        <div className="row" style={{ marginTop: 8 }}>
          <button className="ghost" onClick={interpret}>Разобрать пожелание</button>
          {parsed && (
            <button className="primary" onClick={applyParsed}>
              Применить интерпретацию
            </button>
          )}
        </div>

        {parsed && (
          <div style={{ marginTop: 12 }}>
            <table>
              <thead>
                <tr><th>поле конфига</th><th>значение</th><th>из какой фразы</th></tr>
              </thead>
              <tbody>
                {parsed.matches.map((m, i) => (
                  <tr key={i}>
                    <td className="mono small">{m.field}</td>
                    <td className="mono small">{m.value}</td>
                    <td className="small muted">«{m.source}»</td>
                  </tr>
                ))}
              </tbody>
            </table>
            {parsed.unrecognized.length > 0 && (
              <p className="small" style={{ color: 'var(--warn)', marginTop: 8 }}>
                Не понято и проигнорировано: {parsed.unrecognized.map((u) => `«${u}»`).join(', ')}.
                Это честнее, чем молча угадать.
              </p>
            )}
            <pre className="code" style={{ marginTop: 8 }}>
              {JSON.stringify(parsed.patch, null, 2)}
            </pre>
          </div>
        )}
      </div>

      <div className="panel">
        <h2>Ритм блока до генерации</h2>
        <p className="hint">
          Профиль задаётся настройками, а не кодом. Пресет воспроизводит найденный
          в референсе ритм: пик на позициях 5 и 9, провал сразу после пика,
          4 перехода вниз из 9.
        </p>
        <RhythmChart plans={plans} />
        {rhythm.passed
          ? <p className="small" style={{ color: 'var(--ok)' }}>
              Проверка ритма пройдена: это пила, а не прямая линия.
            </p>
          : (
            <div style={{ marginTop: 8 }}>
              {rhythm.issues.map((issue) => (
                <p key={issue} className="small" style={{ color: 'var(--warn)', margin: '3px 0' }}>
                  {issue}
                </p>
              ))}
            </div>
          )}
      </div>

      <div className="panel">
        <h2>Профиль декады</h2>
        <p className="hint">
          Профиль подставляется по номеру уровней из замера всех 199 уровней
          оригинала (docs/DECADE_CALIBRATION.md). Любое поле ниже можно
          переопределить руками — профиль это старт, а не запрет.
        </p>
        <div className="grid c3">
          <div className="field">
            <span className="lbl">декада</span>
            <strong>{decadeLabel(decade)}</strong>
          </div>
          <div className="field">
            <span className="lbl">категорий в среднем</span>
            <strong>{decade.categoryMean}</strong>
            <span className="small muted">коридор {decade.categoryCorridor.join('–')}</span>
          </div>
          <div className="field">
            <span className="lbl">целевая узнаваемость</span>
            <strong>медиана zipf {decade.zipfMedianTarget}</strong>
            <span className="small muted">p25 {decade.zipfP25Target}</span>
          </div>
          <div className="field">
            <span className="lbl">форма слова</span>
            <strong>{decade.maxTokens === 1 ? 'только однословные' : `до ${decade.maxTokens} слов`}</strong>
            <span className="small muted">
              до {decade.maxWordLen} букв, имена собственные от zipf {decade.minProperNounZipf}
            </span>
          </div>
          <div className="field">
            <span className="lbl">мета-пар на уровень</span>
            <strong>{decade.metaRange.join('–')}</strong>
            <span className="small muted">повторов слов {decade.repeatRange.join('–')}</span>
          </div>
          <div className="field">
            <span className="lbl">модификаторы</span>
            <strong>{decade.allowedModifiers.length ? 'цепи разрешены' : 'запрещены'}</strong>
            <span className="small muted">
              видно на поле от {(visibleShareMin(decade) * 100).toFixed(0)}% уровня
            </span>
          </div>
        </div>
        {config.levelRange[0] === 1 && (
          <p className="small" style={{ color: 'var(--ok)', marginTop: 8 }}>
            Уровень 1 — туториал: 5 категорий, весь уровень на поле, лимита ходов нет,
            мета-пар и модификаторов ноль (как L1 оригинала).
          </p>
        )}
        {!config.decadeGates && (
          <p className="small" style={{ color: 'var(--warn)', marginTop: 8 }}>
            Гейты декады выключены: это пресет блока 201–210, он воспроизводит
            сдаваемый пакет байт-в-байт. Поменяйте диапазон, чтобы включить калибровку.
          </p>
        )}
      </div>

      <div className="panel">
        <h2>Параметры</h2>
        <div className="grid c3">
          <label className="field">
            <span className="lbl">диапазон уровней</span>
            <input type="text" value={config.levelRange.join('–')}
              onChange={(e) => {
                const v = nums(e.target.value);
                /**
                 * Смена диапазона пересобирает ВЕСЬ профиль из таблицы декад,
                 * а не только два числа. Именно на этом мы получили блок 1-10
                 * с контентом уровней ~150: диапазон поменяли, а коридор
                 * категорий, редкость и модификаторы остались от пресета 201-210.
                 */
                if (v.length === 2) onChange(configForRange([v[0], v[1]], config.seed));
              }} />
          </label>
          <label className="field">
            <span className="lbl">коридор по категориям</span>
            <input type="text" value={config.categoryCorridor.join('–')}
              onChange={(e) => {
                const v = nums(e.target.value);
                if (v.length === 2) patch({ categoryCorridor: [v[0], v[1]] });
              }} />
          </label>
          <label className="field">
            <span className="lbl">редких слов на уровень</span>
            <input type="text" value={config.rarityRange.join('–')}
              onChange={(e) => {
                const v = nums(e.target.value);
                if (v.length === 2) patch({ rarityRange: [v[0], v[1]] });
              }} />
          </label>
          <label className="field">
            <span className="lbl">позиции спайков</span>
            <input type="text" value={config.spikePositions.join(', ')}
              onChange={(e) => patch({ spikePositions: nums(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">позиции передышек</span>
            <input type="text" value={config.recoveryPositions.join(', ')}
              onChange={(e) => patch({ recoveryPositions: nums(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">максимальная глубина мета</span>
            <input type="number" min={0} max={4} value={config.maxMetaDepth}
              onChange={(e) => patch({ maxMetaDepth: Number(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">план по категориям (10 чисел)</span>
            <input type="text" value={(config.categoryPlan ?? []).join(', ')}
              onChange={(e) => patch({ categoryPlan: nums(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">план по мета-связям</span>
            <input type="text" value={(config.metaPlan ?? []).join(', ')}
              onChange={(e) => patch({ metaPlan: nums(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">seed генерации</span>
            <input type="text" value={config.seed}
              onChange={(e) => patch({ seed: e.target.value })} />
          </label>
          <label className="field">
            <span className="lbl">окно свежести слов</span>
            <input type="number" value={config.wordFreshnessWindow}
              onChange={(e) => patch({ wordFreshnessWindow: Number(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">окно свежести категорий</span>
            <input type="number" value={config.categoryFreshnessWindow}
              onChange={(e) => patch({ categoryFreshnessWindow: Number(e.target.value) })} />
          </label>
          <label className="field">
            <span className="lbl">модификаторы</span>
            <select value={config.allowedModifiers.join(',')}
              onChange={(e) => patch({
                allowedModifiers: e.target.value ? e.target.value.split(',') as never : [],
              })}>
              <option value="chains">цепи</option>
              <option value="">без модификаторов</option>
            </select>
          </label>
        </div>

        <div className="grid c2" style={{ marginTop: 4 }}>
          <ThemePicker label="включить только эти сферы" themes={knownThemes}
            selected={config.includeThemes}
            onChange={(v) => patch({ includeThemes: v })} />
          <ThemePicker label="исключить сферы" themes={knownThemes}
            selected={config.excludeThemes}
            onChange={(v) => patch({ excludeThemes: v })} />
        </div>

        <div className="row" style={{ marginTop: 14 }}>
          <button className="primary" onClick={onGenerate}>Собрать блок</button>
          <span className="muted small">
            генерация целиком в браузере на снимке базы: без сервера и без ключа
          </span>
        </div>
      </div>
    </>
  );
}

function ThemePicker({ label, themes, selected, onChange }: {
  label: string; themes: string[]; selected: string[]; onChange: (v: string[]) => void;
}) {
  const toggle = (theme: string) => onChange(
    selected.includes(theme) ? selected.filter((t) => t !== theme) : [...selected, theme]);
  return (
    <div>
      <span className="lbl muted small">{label}</span>
      <div className="row" style={{ marginTop: 6, maxHeight: 116, overflowY: 'auto' }}>
        {themes.map((theme) => (
          <button key={theme} className={`ghost ${selected.includes(theme) ? 'on' : ''}`}
            style={{ padding: '3px 8px', fontSize: 11 }}
            onClick={() => toggle(theme)}>{theme}</button>
        ))}
      </div>
    </div>
  );
}

// --------------------------------------------------------------------------- //
// экран 3: генерация
// --------------------------------------------------------------------------- //

export function RunView({ block, plans, elapsed, onGenerate, onSelect }: {
  block: BlockResult | null;
  plans: LevelPlan[];
  elapsed: number;
  onGenerate: () => void;
  onSelect: (levelId: number) => void;
}) {
  if (!block) {
    return (
      <div className="panel">
        <h2>Блок ещё не собран</h2>
        <button className="primary" onClick={onGenerate}>Собрать блок</button>
      </div>
    );
  }

  const rejected = block.levels.flatMap((l) =>
    l.attempts.filter((a) => a.outcome === 'rejected')
      .map((a) => ({ level: l.spec.levelId, ...a })));

  return (
    <>
      <div className="panel">
        <div className="spread">
          <div>
            <h2>Результат сборки</h2>
            <p className="hint">
              Оценки выставляются только уровням, прошедшим hard-инварианты
              и имеющим ровно одно глобальное решение.
            </p>
          </div>
          <button className="ghost" onClick={onGenerate}>Собрать заново</button>
        </div>
        <div className="grid c4">
          <div className="stat"><div className="v">{block.levels.length}/{plans.length}</div>
            <div className="k">уровней собрано</div></div>
          <div className="stat"><div className="v">{block.failures.length}</div>
            <div className="k">отказов генератора</div></div>
          <div className="stat"><div className="v">{elapsed} мс</div>
            <div className="k">время сборки в браузере</div></div>
          <div className="stat">
            <div className="v mono" style={{ fontSize: 13 }}>
              {block.packHash.slice(0, 10)}…
            </div>
            <div className="k">хеш пакета</div>
            <div className="note">тот же вход → тот же хеш</div>
          </div>
        </div>
      </div>

      <div className="panel">
        <h2>Ритм собранного блока</h2>
        <p className="hint">
          Красная линия — сложность, зелёная — интересность. Они обязаны
          расходиться: у передышки интересность выше, чем у пика.
        </p>
        <RhythmChart plans={plans} levels={block.levels} />
      </div>

      <div className="panel">
        <h2>Уровни</h2>
        <table>
          <thead>
            <tr>
              <th>ур.</th><th>роль</th><th className="num">кат</th>
              <th className="num">пуз</th><th className="num">мета</th>
              <th className="num">глуб</th><th className="num">редк</th>
              <th className="num">лов</th><th className="num">цепи</th>
              <th className="num">реш</th><th>проверки</th>
              <th className="num">D</th><th className="num">I</th>
              <th className="num">поп</th>
            </tr>
          </thead>
          <tbody>
            {block.levels.map((level) => {
              const s = level.spec;
              const meta = s.categories.reduce((n, c) =>
                n + c.words.filter((w) => w.kind === 'meta').length, 0);
              const depth = Math.max(0, ...s.categories.map((c) => c.metaDepth));
              const rare = s.categories.flatMap((c) => c.words)
                .filter((w) => w.kind === 'word' && w.zipf !== null && w.zipf < 3).length;
              const hard = level.validation.issues.filter((i) => i.severity === 'hard').length;
              const soft = level.validation.issues.filter((i) => i.severity === 'soft').length;
              return (
                <tr key={s.levelId} className="clickable" onClick={() => onSelect(s.levelId)}>
                  <td className="mono">{s.levelId}</td>
                  <td><span className="tag role">{ROLE_LABEL[level.plan.role]}</span></td>
                  <td className="num">{s.categories.length}</td>
                  <td className="num">{s.board.startBubbles}</td>
                  <td className="num">{meta}</td>
                  <td className="num">{depth >= 3 ? <strong>{depth}</strong> : depth}</td>
                  <td className="num">{rare}</td>
                  <td className="num">{s.traps.length}</td>
                  <td className="num">{s.modifiers.chains.length}</td>
                  <td className="num">{level.solutions.count}</td>
                  <td>
                    {hard === 0
                      ? <span className="tag ok">PASS</span>
                      : <span className="tag fail">{hard} hard</span>}
                    {soft > 0 && <> <span className="tag warn">{soft} soft</span></>}
                  </td>
                  <td className="num">{level.difficulty.value}</td>
                  <td className="num">{level.interest.value}</td>
                  <td className="num muted">{level.attempts.length}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {rejected.length > 0 && (
        <div className="panel">
          <h2>Отклонённые попытки — {rejected.length}</h2>
          <p className="hint">
            Самое убедительное место инструмента: видно, что именно генератор
            забраковал и почему, а не просто «крутится спиннер».
          </p>
          <table>
            <thead>
              <tr><th>ур.</th><th className="num">попытка</th><th>этап</th>
                <th>причина</th><th>ослабления</th></tr>
            </thead>
            <tbody>
              {rejected.map((r, i) => (
                <tr key={i}>
                  <td className="mono">{r.level}</td>
                  <td className="num">{r.index + 1}</td>
                  <td className="small">{r.stage}</td>
                  <td className="small">{r.reason}</td>
                  <td className="small muted">{r.relaxations.join('; ') || '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {block.failures.length > 0 && (
        <div className="panel">
          <h2>Генератор не сошёлся</h2>
          <p className="hint">
            Хороший генератор не обязан всегда выдавать результат — он обязан
            объяснить, чего не хватило, и предложить осознанные ослабления.
            Hard-инварианты не ослабляются никогда.
          </p>
          {block.failures.map((f) => (
            <div key={f.levelId} style={{ marginBottom: 12 }}>
              <strong className="mono">уровень {f.levelId}</strong>
              <div className="small">{f.reason}</div>
              <ul className="small muted" style={{ paddingLeft: 18, marginTop: 4 }}>
                {f.suggestions.map((s) => <li key={s}>{s}</li>)}
              </ul>
            </div>
          ))}
        </div>
      )}
    </>
  );
}
