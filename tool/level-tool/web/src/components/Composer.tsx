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
import {
  DEFAULT_INTENT_PROMPT, parseIntent, type ParsedIntent,
} from '../core/intentParser.ts';
import { startBubbles } from '../core/levelMath.ts';
import {
  configForRange, decadeLabel, profileForRange, visibleShareMin,
} from '../core/decadeProfiles.ts';
import {
  parseCount, parseNumberList, parseOptionalList, parseRange,
} from '../core/fieldParse.ts';
import { buildBlockPlan, checkBlockRhythm } from '../core/blockPlan.ts';
import { canonicalJson } from '../core/hashing.ts';

/**
 * Поле ввода с черновиком.
 *
 * Раньше поля этого экрана были полностью управляемыми: показывалось значение,
 * пересобранное из конфига. Пока набранное не разбиралось, конфиг не менялся —
 * и React возвращал в поле прежний текст прямо во время набора. Практическое
 * следствие: коридор «7–9» нельзя было стереть, чтобы ввести «10–14». Стираешь
 * дефис — «7–9» тут же встаёт обратно, и в поле остаются куски прежнего
 * значения. У числовых полей было своё: `Number('')` даёт 0, поэтому очистить
 * поле не получалось вовсе — вместо пустого оставался ноль.
 *
 * Здесь набранное живёт в локальном черновике, пока поле в фокусе, и уходит
 * в конфиг только когда разобралось. На выходе из поля черновик отбрасывается
 * и снова показывается каноническое значение конфига: поле не может остаться
 * с текстом, которого в конфиге нет.
 */
function DraftField({ label, hint, value, commit, numeric }: {
  label: string;
  hint?: string;
  /** каноническое значение конфига — то, что видно, когда поле не редактируют */
  value: string;
  /** true — принято в конфиг; false — пока не разобралось */
  commit: (raw: string) => boolean;
  numeric?: boolean;
}) {
  const [draft, setDraft] = useState<string | null>(null);
  const [pending, setPending] = useState(false);

  return (
    <label className="field">
      <span className="lbl">{label}</span>
      <input
        type="text"
        inputMode={numeric ? 'numeric' : undefined}
        value={draft ?? value}
        className={pending ? 'pending' : undefined}
        onChange={(e) => {
          setDraft(e.target.value);
          setPending(!commit(e.target.value));
        }}
        onFocus={(e) => e.currentTarget.select()}
        onBlur={() => { setDraft(null); setPending(false); }}
      />
      <span className="small muted">
        {pending ? 'значение ещё не принято' : hint ?? ''}
      </span>
    </label>
  );
}

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

/**
 * Экран настройки работает с ЧЕРНОВИКОМ конфига, а не с применённым.
 *
 * Раньше каждое поле применялось сразу, и заполнение формы означало череду
 * промежуточных конфигов. Это плохо по двум причинам, и вторая серьёзнее первой.
 *
 * Первая: пока набираешь одно поле, требования к уровням уже пересчитаны по
 * половине формы, и график ритма скачет от незаконченного ввода.
 *
 * Вторая: смена диапазона уровней пересобирает ВЕСЬ профиль декады. Заполнив
 * коридор и редкость, а потом поправив диапазон, вы теряли только что введённое —
 * профиль перезаписывал его молча. Порядок заполнения формы влиял на результат.
 *
 * Поэтому: правки идут в черновик, применяются кнопкой, и до кнопки не влияют
 * ни на что. График под формой считается по черновику — это предпросмотр того,
 * что будет собрано, а не состояние генератора.
 */
export function Composer({ config, onGenerate }: {
  config: BlockConfig;
  onGenerate: (config: BlockConfig) => void;
}) {
  /**
   * Предзаполненный промпт — образец формы, а не украшение: по нему видно, из
   * чего вообще состоит запрос (сколько уровней, где, о чём, с каким ритмом).
   * Разбирается целиком, без остатка в «не понято», — иначе пример учил бы
   * писать то, что инструмент не понимает.
   */
  const [text, setText] = useState(DEFAULT_INTENT_PROMPT);
  const [parsed, setParsed] = useState<ParsedIntent | null>(null);
  /**
   * Черновик. Инициализируется применённым конфигом при каждом открытии
   * закладки: компонент размонтируется при уходе с неё, поэтому вернувшись,
   * человек видит то, что реально применено, а не забытый черновик.
   */
  const [draft, setDraft] = useState<BlockConfig>(config);

  const decade = profileForRange(draft.levelRange);
  const patch = (p: Partial<BlockConfig>) => setDraft((d) => ({ ...d, ...p }));

  // предпросмотр считается по черновику, а не по применённому конфигу
  const plans = buildBlockPlan(draft);
  const rhythm = checkBlockRhythm(plans);
  const dirty = canonicalJson(draft) !== canonicalJson(config);

  const interpret = () => setParsed(parseIntent(text, draft.levelRange));
  const applyParsed = () => {
    if (parsed) {
      setDraft((d) => {
        /**
         * Смена диапазона обязана пересобрать профиль декады целиком — ровно то
         * же правило, что у поля «диапазон уровней» ниже. Без этого промпт
         * «10 уровней в линейке 150-160» дал бы номера из полутора сотен, а
         * коридор категорий, редкость и план по позициям остались бы от
         * пресета 201-210: блок с чужим содержимым под правильными номерами.
         */
        const range = parsed.patch.levelRange;
        const base = range ? configForRange(range, d.seed) : d;
        return { ...base, ...parsed.patch };
      });
    }
    setParsed(null);
  };

  return (
    <>
      <div className="panel">
        <h2>Промпт для генерации набора уровней</h2>
        <p className="hint">
          Напишите словами, каким должен быть блок. Инструмент показывает, как понял
          ваши слова, и вы правите интерпретацию <strong>до</strong> генерации.
        </p>
        <textarea value={text} onChange={(e) => setText(e.target.value)} />
        <div className="row" style={{ marginTop: 8 }}>
          <button className="ghost" onClick={interpret}>Разобрать промпт</button>
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
            <span className="lbl">видно на поле</span>
            <strong>от {(visibleShareMin(decade) * 100).toFixed(0)}% уровня</strong>
            <span className="small muted">остальное досыпается по ходу</span>
          </div>
        </div>
        {draft.levelRange[0] === 1 && (
          <p className="small" style={{ color: 'var(--ok)', marginTop: 8 }}>
            Уровень 1 — туториал: 5 категорий, весь уровень на поле, лимита ходов нет,
            мета-пар ноль (как L1 оригинала).
          </p>
        )}
        {!draft.decadeGates && (
          <p className="small" style={{ color: 'var(--warn)', marginTop: 8 }}>
            Гейты декады выключены: это пресет блока 201–210, он воспроизводит
            сдаваемый пакет байт-в-байт. Поменяйте диапазон, чтобы включить калибровку.
          </p>
        )}
      </div>

      <div className="panel">
        <h2>Параметры</h2>
        <div className="grid c3">
          <DraftField
            label="диапазон уровней"
            hint="меняет весь профиль декады"
            value={draft.levelRange.join('–')}
            commit={(raw) => {
              const range = parseRange(raw, 1);
              if (!range) return false;
              /**
               * Смена диапазона пересобирает ВЕСЬ профиль из таблицы декад,
               * а не только два числа. Именно на этом мы получили блок 1-10
               * с контентом уровней ~150: диапазон поменяли, а коридор
               * категорий, редкость и модификаторы остались от пресета 201-210.
               */
              setDraft(configForRange(range, draft.seed));
              return true;
            }} />
          <DraftField
            label="коридор по категориям"
            value={draft.categoryCorridor.join('–')}
            commit={(raw) => {
              const range = parseRange(raw, 1);
              if (!range) return false;
              patch({ categoryCorridor: range });
              return true;
            }} />
          <DraftField
            label="редких слов на уровень"
            value={draft.rarityRange.join('–')}
            commit={(raw) => {
              const range = parseRange(raw, 0);
              if (!range) return false;
              patch({ rarityRange: range });
              return true;
            }} />
          <DraftField
            label="позиции спайков"
            hint="через запятую"
            value={draft.spikePositions.join(', ')}
            commit={(raw) => { patch({ spikePositions: parseNumberList(raw) }); return true; }} />
          <DraftField
            label="позиции передышек"
            hint="через запятую"
            value={draft.recoveryPositions.join(', ')}
            commit={(raw) => { patch({ recoveryPositions: parseNumberList(raw) }); return true; }} />
          <DraftField
            label="максимальная глубина мета"
            hint="0–4"
            numeric
            value={String(draft.maxMetaDepth)}
            commit={(raw) => {
              const value = parseCount(raw, 0, 4);
              if (value === null) return false;
              patch({ maxMetaDepth: value });
              return true;
            }} />
          <DraftField
            label="план по категориям (10 чисел)"
            hint="пусто — берётся коридор"
            value={(draft.categoryPlan ?? []).join(', ')}
            commit={(raw) => { patch({ categoryPlan: parseOptionalList(raw) }); return true; }} />
          <DraftField
            label="план по мета-связям"
            hint="пусто — берётся профиль декады"
            value={(draft.metaPlan ?? []).join(', ')}
            commit={(raw) => { patch({ metaPlan: parseOptionalList(raw) }); return true; }} />
          <DraftField
            label="seed генерации"
            value={draft.seed}
            commit={(raw) => {
              // пустой seed сделал бы генерацию невоспроизводимой
              if (!raw.trim()) return false;
              patch({ seed: raw });
              return true;
            }} />
          <DraftField
            label="окно свежести слов"
            hint="уровней"
            numeric
            value={String(draft.wordFreshnessWindow)}
            commit={(raw) => {
              const value = parseCount(raw, 0, 999);
              if (value === null) return false;
              patch({ wordFreshnessWindow: value });
              return true;
            }} />
          <DraftField
            label="окно свежести категорий"
            hint="уровней"
            numeric
            value={String(draft.categoryFreshnessWindow)}
            commit={(raw) => {
              const value = parseCount(raw, 0, 999);
              if (value === null) return false;
              patch({ categoryFreshnessWindow: value });
              return true;
            }} />
        </div>

        {/*
          Единственная точка, где заполненная форма превращается в требования
          к уровням. До нажатия ничего не применено — ни к генератору, ни к
          проверкам; выше только предпросмотр по черновику.
        */}
        <div className="row" style={{ marginTop: 14, alignItems: 'center' }}>
          <button className="primary" onClick={() => onGenerate(draft)}>
            Применить и собрать блок
          </button>
          {dirty && (
            <button className="ghost" onClick={() => setDraft(config)}>
              Вернуть применённое
            </button>
          )}
          <span className="muted small">
            {dirty
              ? 'форма изменена и пока не применена — требования к уровням возьмутся '
                + 'из неё в момент нажатия'
              : 'генерация целиком в браузере на снимке базы: без сервера и без ключа'}
          </span>
        </div>
      </div>
    </>
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
        {/* см. Empty в App.tsx: голый onGenerate получил бы событие клика
            на место конфига */}
        <button className="primary" onClick={() => onGenerate()}>Собрать блок</button>
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
          <button className="ghost" onClick={() => onGenerate()}>Собрать заново</button>
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
              <th className="num">лов</th>
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
