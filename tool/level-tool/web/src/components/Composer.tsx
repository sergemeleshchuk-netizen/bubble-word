/**
 * Экраны 2 и 3 — Настройка блока и Генерация.
 *
 * Главное требование к этому экрану: ритм блока должен быть виден ГЛАЗОМ.
 * Блок из 10 уровней — композиция, а не десять растущих строк: рост, пик,
 * передышка, второй пик, приятный выход. Таблица из чисел этого не показывает,
 * поэтому здесь график.
 */
import { useRef, useState } from 'react';
import type {
  BlockConfig, BlockResult, GeneratedLevel, LevelModifier, LevelPlan,
} from '../core/types.ts';
import {
  DEFAULT_INTENT_PROMPT, parseIntent, type ParsedIntent,
} from '../core/intentParser.ts';
import { startBubbles } from '../core/levelMath.ts';
import { configForRange } from '../core/decadeProfiles.ts';
import { metaIconTarget } from '../core/metaIcons.ts';
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
function DraftField({ label, hint, tip, value, commit, numeric }: {
  label: string;
  hint?: string;
  /** что поле определяет: всплывает по наведению на значок рядом с названием */
  tip?: string;
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
      <span className="lbl">
        {label}
        {tip && <InfoTip text={tip} />}
      </span>
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

/**
 * Значок «что это за настройка» с подсказкой по наведению.
 *
 * Подсказка сделана на CSS, а не атрибутом `title`: системная всплывает через
 * секунду с лишним и обрезает текст в одну строку, а объяснение настройки в одну
 * строку не влезает. `tabIndex` и `aria-label` — чтобы подсказка открывалась и с
 * клавиатуры, а не только мышью.
 */
function InfoTip({ text }: { text: string }) {
  return (
    <span className="info" data-tip={text} tabIndex={0} role="note" aria-label={text}>i</span>
  );
}

const ROLE_LABEL: Record<string, string> = {
  entry: 'вход', growth: 'рост', recovery: 'передышка',
  peak: 'пик', spike: 'спайк', exit: 'выход',
};

// --------------------------------------------------------------------------- //
// график ритма
// --------------------------------------------------------------------------- //

/**
 * Что можно включить на уровне поштучно.
 *
 * Мета стоит в одном ряду с модификаторами, хотя модификатором не является:
 * для человека, который смотрит на график, это такой же переключатель «есть или
 * нет», и прятать его в другое место значит прятать половину ответа на вопрос
 * «почему тут так тяжело». Остальные четыре взаимоисключающие — на уровне живёт
 * один модификатор (GDD §7), поэтому включение одного гасит другой.
 */
const LEVEL_TOGGLES: {
  key: 'meta' | 'icon' | LevelModifier;
  mark: string;
  /** короткая подпись для легенды под графиком */
  title: string;
  /** подробное объяснение по наведению на сам чекбокс */
  tip?: string;
}[] = [
  { key: 'meta', mark: 'M', title: 'мета-связи' },
  {
    key: 'icon',
    mark: '\u{1F5BC}',
    title: 'категория-картинка: мета-пузырь рисуется значком',
    tip: 'Категория-картинка. Включено — уровень ОБЯЗАН получить мета-пузырь со '
      + 'значком вместо слова: генератор выбирает мета-пары среди имён, у которых '
      + 'значок в словаре есть (core/metaIcons.ts, 313 имён). Выключено — картинок '
      + 'на уровне нет вовсе. Пока галочку не трогали, работает прежнее правило: '
      + 'четверть мета-пузырей уровня, что нашлось в словаре. На уровне без '
      + 'мета-связей картинки быть не может — там галочка недоступна.',
  },
  { key: 'halves', mark: '½', title: 'половинки: слово из двух пузырей' },
  { key: 'ice', mark: '❄', title: 'лёд: снимается счётчиком мерджей' },
  { key: 'hidden', mark: '?', title: 'скрытые: слово открывается мерджами' },
  { key: 'chain_line', mark: '⛓', title: 'цепь: делит поле до сбора категорий' },
];

/**
 * Ждём ли картинку на уровне по одному плану, без собранного блока.
 *
 * `require` — обязана быть; `forbid` — нет; `auto` — по правилу доли, то есть от
 * двух мета-пар и выше. Галочка на графике и обработчик клика обязаны отвечать
 * одинаково, иначе первый же клик «переворачивал» бы не то, что видно.
 */
export function iconExpected(plan: LevelPlan): boolean {
  if (plan.iconMode === 'require') return true;
  if (plan.iconMode === 'forbid') return false;
  return metaIconTarget(plan.metaCount) >= 1;
}

export interface RhythmEditing {
  /** перетащили колонку: композиция позиции едет за ней */
  onReorder: (from: number, to: number) => void;
  onToggleMeta: (index: number) => void;
  onToggleIcon: (index: number) => void;
  onToggleModifier: (index: number, modifier: LevelModifier) => void;
}

/**
 * Полоса колонок под графиком: по колонке на уровень.
 *
 * Сделана обычным HTML, а не частью SVG, сознательно. Внутри графика это были бы
 * рукописные хит-зоны и рукописный чекбокс, а здесь работают настоящий
 * `draggable` и настоящий `input[type=checkbox]` — с клавиатурой, фокусом и
 * поведением, которого от них ждут.
 */
function RhythmColumns({ plans, editing, offsets, iconOn }: {
  plans: LevelPlan[];
  editing: RhythmEditing;
  offsets: { left: string; right: string };
  /** есть ли картинка на СОБРАННОМ уровне позиции: галочка показывает факт, а не желание */
  iconOn: (index: number) => boolean;
}) {
  /**
   * Откуда тащат, живёт в ref, а не только в состоянии.
   *
   * Состояние нужно для подсветки, но читать его в обработчике `drop` нельзя:
   * между `dragstart` и `drop` React может не успеть перерисоваться, и замыкание
   * обработчика увидит прежнее значение — перетаскивание молча не сработает.
   * Ref одинаково верен в обоих случаях.
   */
  const source = useRef<number | null>(null);
  const [dragged, setDragged] = useState<number | null>(null);
  const [over, setOver] = useState<number | null>(null);

  return (
    <div
      className="rhythm-cols"
      style={{
        gridTemplateColumns: `repeat(${plans.length}, minmax(0, 1fr))`,
        marginLeft: offsets.left,
        marginRight: offsets.right,
      }}
    >
      {plans.map((plan, i) => (
        <div
          key={plan.levelId}
          className={`rhythm-col${over === i && dragged !== i ? ' over' : ''}`
            + `${dragged === i ? ' dragged' : ''}`}
          draggable
          onDragStart={() => { source.current = i; setDragged(i); }}
          onDragEnd={() => { source.current = null; setDragged(null); setOver(null); }}
          onDragOver={(e) => { e.preventDefault(); setOver(i); }}
          onDrop={(e) => {
            e.preventDefault();
            const from = source.current;
            if (from !== null && from !== i) editing.onReorder(from, i);
            source.current = null;
            setDragged(null);
            setOver(null);
          }}
          title="перетащите, чтобы поменять порядок уровней в блоке"
        >
          <div className="rc-head mono">{plan.levelId}</div>
          {LEVEL_TOGGLES.map((toggle) => {
            const on = toggle.key === 'meta' ? plan.metaCount > 0
              : toggle.key === 'icon' ? iconOn(i)
              : plan.modifier === toggle.key;
            return (
              <label key={toggle.key} className="rc-toggle" title={toggle.tip ?? toggle.title}>
                <input
                  type="checkbox"
                  checked={on}
                  // картинка на уровне без мета-пар невозможна физически
                  disabled={toggle.key === 'icon' && plan.metaCount === 0}
                  onChange={() => (toggle.key === 'meta'
                    ? editing.onToggleMeta(i)
                    : toggle.key === 'icon'
                      ? editing.onToggleIcon(i)
                      : editing.onToggleModifier(i, toggle.key as LevelModifier))}
                />
                <span>{toggle.mark}</span>
              </label>
            );
          })}
        </div>
      ))}
    </div>
  );
}

export function RhythmChart({ plans, levels, editing }: {
  plans: LevelPlan[];
  levels?: GeneratedLevel[];
  /** передан — колонки можно перетаскивать и переключать; иначе график только показывает */
  editing?: RhythmEditing;
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
      {editing && (
        <RhythmColumns
          plans={plans}
          editing={editing}
          iconOn={(i) => {
            const level = byId.get(plans[i].levelId);
            // есть собранный уровень — показываем факт, иначе ожидание плана
            return level
              ? level.spec.categories.some((c) => c.words.some((w) => w.icon))
              : iconExpected(plans[i]);
          }}
          offsets={{
            left: `${(padL / W) * 100}%`,
            right: `${(padR / W) * 100}%`,
          }}
        />
      )}
      <div className="row small muted" style={{ marginTop: 4 }}>
        <span><span style={{ color: '#f85149' }}>●</span> сложность D</span>
        <span><span style={{ color: '#3fb950' }}>●</span> интересность I</span>
        <span><span style={{ color: '#8b98a6' }}>▮</span> пузырей на старте</span>
        <span><span style={{ color: '#4cc2ff' }}>▮</span> целевой коридор D</span>
      </div>
    </div>
  );
}

/** Расшифровка чекбоксов под графиком: без неё колонка значков — ребус. */
export function RhythmLegend() {
  return (
    <div className="small muted" style={{ marginTop: 8, lineHeight: 1.6 }}>
      <div>
        {LEVEL_TOGGLES.map((t) => (
          <span key={t.key} style={{ marginRight: 14, whiteSpace: 'nowrap' }}>
            <strong style={{ color: 'var(--text)' }}>{t.mark}</strong> {t.title}
          </span>
        ))}
      </div>
      <div style={{ marginTop: 4 }}>
        Отмечено то, что уже применено на уровне. Колонку можно перетащить —
        состав, роль и модификатор переедут на другой номер уровня вместе с ней.
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
/**
 * Конфиг из промпта: то, что понято из текста, поверх профиля декады.
 *
 * Порядок именно такой. Сначала диапазон уровней из промпта поднимает ПРОФИЛЬ
 * этих номеров (таблица декад: коридор категорий, редкость, раскладка старта),
 * и только потом сверху ложится разобранное. Иначе «10 уровней в линейке 150-160»
 * дало бы правильные номера с содержимым чужой декады.
 *
 * Используется в двух местах: кнопкой «Применить интерпретацию» и для начального
 * заполнения формы — форма обязана показывать то же, что написано в промпте выше.
 */
function configFromIntent(
  base: BlockConfig, patch: Partial<BlockConfig>, tuned: (c: BlockConfig) => BlockConfig,
): BlockConfig {
  const range = patch.levelRange;
  const profile = range ? tuned(configForRange(range, base.seed)) : base;
  return { ...profile, ...patch };
}

export function Composer({ config, onGenerate, tuneConfig, generated }: {
  config: BlockConfig;
  onGenerate: (config: BlockConfig) => void;
  /**
   * Собран ли блок. Нужен ровно для одного: решить, чем заполнить форму при
   * открытии закладки — промптом (ещё ничего не собирали) или применённым
   * конфигом (собрали, и человек вернулся его править).
   */
  generated?: boolean;
  /**
   * Таблица декад с первой вкладки (коридор категорий, схема выкладки):
   * применяется к конфигу, собранному из диапазона, чтобы форма показывала
   * то, что реально будет собрано. Пресета 201-210 не касается.
   */
  tuneConfig?: (config: BlockConfig) => BlockConfig;
}) {
  const tuned = tuneConfig ?? ((c: BlockConfig) => c);
  /**
   * Предзаполненный промпт — образец формы, а не украшение: по нему видно, из
   * чего вообще состоит запрос (сколько уровней, где, о чём, с каким ритмом).
   * Разбирается целиком, без остатка в «не понято», — иначе пример учил бы
   * писать то, что инструмент не понимает.
   */
  const [text, setText] = useState(DEFAULT_INTENT_PROMPT);
  const [parsed, setParsed] = useState<ParsedIntent | null>(null);
  /**
   * Черновик формы.
   *
   * Пока ничего не собрано, форма заполняется ИЗ ПРОМПТА, который стоит в поле
   * выше: раньше она показывала пресет 201-210 рядом с промптом про линейку
   * 150-160 — два разных задания на одном экране, и человек не мог понять, что
   * из этого соберётся. Теперь дефолты честные: диапазон, спайки, передышки,
   * редкость и темы — из текста промпта, остальное — из профиля этих номеров
   * (таблица декад).
   *
   * Как только блок собран, форма при возврате на закладку показывает
   * ПРИМЕНЁННОЕ, а не промпт: компонент размонтируется при уходе, и подставлять
   * снова текст промпта значило бы терять то, с чем человек только что работал.
   */
  const [draft, setDraft] = useState<BlockConfig>(() => (
    generated ? config : configFromIntent(config, parseIntent(text, config.levelRange).patch, tuned)
  ));

  const patch = (p: Partial<BlockConfig>) => setDraft((d) => ({ ...d, ...p }));

  // предпросмотр считается по черновику, а не по применённому конфигу
  const plans = buildBlockPlan(draft);
  const rhythm = checkBlockRhythm(plans, draft.categoryCorridor);
  const dirty = canonicalJson(draft) !== canonicalJson(config);

  /**
   * Коридор, который даёт конфиг декад с первого шага для диапазона черновика.
   *
   * Своего поля у коридора на этом экране нет: он предустановка кривой, а не
   * параметр блока. Сравнение нужно, чтобы поймать единственный случай, когда
   * блок и конфиг разъехались, — конфиг применили после сборки блока.
   */
  const configCorridor = tuned(draft).categoryCorridor;
  const corridorOffConfig = configCorridor[0] !== draft.categoryCorridor[0]
    || configCorridor[1] !== draft.categoryCorridor[1];

  /**
   * Правки прямо на графике.
   *
   * Все три пишут в черновик ЯВНЫЕ планы по позициям. Иначе правка жила бы до
   * первого пересчёта: коридор и лесенка модификаторов вывели бы своё значение
   * заново и молча стёрли выбор человека.
   */
  const editing: RhythmEditing = {
    onReorder: (from, to) => setDraft((d) => {
      const order = plans.map((_, i) => i);
      order.splice(to, 0, order.splice(from, 1)[0]);
      const spikes = new Set(d.spikePositions);
      const rests = new Set(d.recoveryPositions);
      const movedPositions = (was: Set<number>) => order
        .map((src, dst) => (was.has(src + 1) ? dst + 1 : 0))
        .filter((p) => p > 0)
        .sort((a, b) => a - b);
      return {
        ...d,
        categoryPlan: order.map((i) => plans[i].categoryCount),
        metaPlan: order.map((i) => plans[i].metaCount),
        modifierPlan: order.map((i) => plans[i].modifier),
        // роли живут в позициях, а не в уровнях: чтобы пик уехал вместе
        // с колонкой, позиции пиков и передышек надо переставить тоже
        spikePositions: movedPositions(spikes),
        recoveryPositions: movedPositions(rests),
      };
    }),
    onToggleMeta: (index) => setDraft((d) => {
      const metaPlan = plans.map((p) => p.metaCount);
      // включаем обратно не в единицу, а в то, что план посчитал бы сам
      const derived = buildBlockPlan({ ...d, metaPlan: undefined })[index]?.metaCount ?? 1;
      metaPlan[index] = metaPlan[index] > 0 ? 0 : Math.max(1, derived);
      return { ...d, metaPlan };
    }),
    onToggleIcon: (index) => setDraft((d) => {
      /*
       * Пишем ЯВНЫЙ план: иначе выбор жил бы до первого пересчёта — правило доли
       * вывело бы своё и молча стёрло галочку. Остальные позиции фиксируем в том
       * виде, в котором человек их сейчас видит на графике, чтобы одна галочка
       * не переставила картинки на всём блоке.
       */
      const iconPlan: (0 | 1 | null)[] = plans.map((plan) => (iconExpected(plan) ? 1 : 0));
      iconPlan[index] = iconPlan[index] === 1 ? 0 : 1;
      return { ...d, iconPlan };
    }),
    onToggleModifier: (index, modifier) => setDraft((d) => {
      const modifierPlan: (typeof plans[number]['modifier'])[] = plans.map((p) => p.modifier);
      modifierPlan[index] = modifierPlan[index] === modifier ? 'none' : modifier;
      return { ...d, modifierPlan };
    }),
  };

  const interpret = () => setParsed(parseIntent(text, draft.levelRange));
  const applyParsed = () => {
    // правило «смена диапазона пересобирает профиль декады целиком» живёт в
    // configFromIntent — то же, что при первом заполнении формы
    if (parsed) setDraft((d) => configFromIntent(d, parsed.patch, tuned));
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
        <RhythmChart plans={plans} editing={editing} />
        {!rhythm.passed && (
          <div style={{ marginTop: 8 }}>
            {rhythm.issues.map((issue) => (
              <p key={issue} className="small" style={{ color: 'var(--warn)', margin: '3px 0' }}>
                {issue}
              </p>
            ))}
          </div>
        )}
        <RhythmLegend />
      </div>

      <div className="panel">
        <h2>Параметры</h2>
        <div className="grid c3">
          <DraftField
            label="диапазон уровней"
            tip="Номера уровней блока, например 201–210. Меняет весь профиль сразу: коридор категорий, редкость и стартовую раскладку инструмент берёт из таблицы декад для этих номеров — уровень 5 и уровень 500 строятся по-разному."
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
              setDraft(tuned(configForRange(range, draft.seed)));
              return true;
            }} />
          {/*
            Поля «коридор по категориям» здесь нет (решение владельца 04.08).
            Коридор — предустановка кривой, и живёт он в конфиге декад на первом
            шаге: строка того промежутка, в который попадает первый уровень
            блока. Дублировать его здесь значило показывать одно и то же число в
            двух местах и разрешать им разъехаться — что и произошло: пресет
            201-210 нёс 11-18, конфиг декад для тех же номеров 8-12, а форма при
            открытии показывала 10-17 по промпту-образцу.

            Значение человека по-прежнему сильнее предустановки, но берётся оно
            там, где человек его и задаёт: правкой строки конфига декад или
            прямо на графике ритма (явный план по категориям ниже).
          */}
          <DraftField
            label="редких слов на уровень"
            tip="Сколько слов уровня разрешено брать из редких (zipf ниже 3.0 — уровень слова AGLET). Больше редких — выше сложность, но и выше риск, что игрок слово просто не знает."
            value={draft.rarityRange.join('–')}
            commit={(raw) => {
              const range = parseRange(raw, 0);
              if (!range) return false;
              patch({ rarityRange: range });
              return true;
            }} />
          <DraftField
            label="позиции спайков"
            tip="Позиции в блоке (1–10), где сложность идёт вверх. Самая нагруженная из них становится «пиком», остальные — «спайками»: категорий берётся максимум коридора или на одну меньше."
            hint="через запятую"
            value={draft.spikePositions.join(', ')}
            commit={(raw) => { patch({ spikePositions: parseNumberList(raw) }); return true; }} />
          <DraftField
            label="позиции передышек"
            tip="Позиции, где сложность падает: лёгкий уровень как награда после пика. Категорий берётся минимум коридора. В референсе 37% переходов идут вниз — без передышек блок читается как ровная стена."
            hint="через запятую"
            value={draft.recoveryPositions.join(', ')}
            commit={(raw) => { patch({ recoveryPositions: parseNumberList(raw) }); return true; }} />
          <DraftField
            label="глубина мета: длина цепочки"
            tip="ДЛИНА вложенности, не количество. 1 — собранная категория превращается в пузырь и уходит в другую: собрали WATER, слово WATER легло в KITCHEN, на этом всё. 2 — та вторая категория сама лежит в третьей: WATER → KITCHEN → HOUSE, и HOUSE не закрыть, пока не собраны обе. Цепочку длины 2 физически можно построить только из двух мета-пар, поэтому глубина ограничена и полем «мета-пар на уровень». В оригинале глубина 3 встречается только с уровня 438, поэтому для ранних блоков потолок 2."
            hint="0–4, длина цепочки"
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
            tip="Явное число категорий на каждую позицию блока, через запятую. Пусто — число выводится из коридора и роли уровня. Заполняется само, когда вы тащите колонку на графике ритма."
            hint="пусто — берётся коридор"
            value={(draft.categoryPlan ?? []).join(', ')}
            commit={(raw) => { patch({ categoryPlan: parseOptionalList(raw) }); return true; }} />
          <DraftField
            label="мета-пар на уровень (10 чисел)"
            tip="КОЛИЧЕСТВО мета-пар на каждой позиции блока, через запятую. Мета-пара — это одна связь «категория внутри категории»: собранная четвёрка не исчезает, а превращается в один пузырь со своим именем и уходит в другую категорию уровня (собрали WATER — слово WATER стало пузырём внутри KITCHEN). На поле такой пузырь ничем не отмечен, поэтому это самый дорогой для игрока рычаг: три пары — три независимые связи, а не тройная вложенность (за длину отвечает поле глубины). Пусто — план строится сам: 1-2-3 ровными долями, 4 только на спайке (позиция 5), раз в две декады один уровень идёт совсем без мета. Ноль в позиции — уровень из одних плоских категорий."
            hint="пусто — 1-2 на уровень, 4 на спайке"
            value={(draft.metaPlan ?? []).join(', ')}
            commit={(raw) => { patch({ metaPlan: parseOptionalList(raw) }); return true; }} />
          <DraftField
            label="seed генерации"
            tip="Строка, из которой растёт вся случайность сборки. Тот же seed плюс тот же конфиг и тот же снимок базы дают ровно тот же блок и тот же хеш пакета — на этом держится воспроизводимость."
            value={draft.seed}
            commit={(raw) => {
              // пустой seed сделал бы генерацию невоспроизводимой
              if (!raw.trim()) return false;
              patch({ seed: raw });
              return true;
            }} />
          <DraftField
            label="окно свежести слов"
            tip="Сколько предыдущих уровней помнить, чтобы не выдать то же слово снова. Повтор слова в НОВОЙ категории — ловушка на памяти игрока, поэтому окно управляет не только разнообразием, но и сложностью."
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
            tip="Сколько предыдущих уровней помнить, чтобы не брать ту же категорию. Шире окно — разнообразнее блок, но у генератора меньше выбора: на узкой базе он начнёт отказываться собирать уровень."
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
          Коридор категорий блока — из конфига декад, поля для него здесь нет.
          Строка показывает действующее значение и его источник, а кнопка нужна
          для одного случая: конфиг декад применили ПОСЛЕ того, как этот блок
          был собран (или блок собран закреплённым пресетом), и числа разошлись.
        */}
        <div className="row small muted" style={{ marginTop: 12, alignItems: 'center' }}>
          <span>
            коридор по категориям <span className="mono">
              {draft.categoryCorridor.join('–')}
            </span> — предустановка кривой из конфига декад (шаг «База контента»)
          </span>
          {corridorOffConfig && (
            <>
              <span style={{ color: 'var(--warn)' }}>
                конфиг декад для уровней {draft.levelRange.join('–')} даёт
                {' '}<span className="mono">{configCorridor.join('–')}</span>
              </span>
              <button className="ghost" onClick={() => setDraft(tuned(draft))}>
                взять из конфига декад
              </button>
            </>
          )}
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

/**
 * Этап, на котором генератор споткнулся → настройка, которую надо трогать.
 *
 * Здесь и была ценность прежнего лога попыток: он показывал этап и причину.
 * Но показывал их ВСЕГДА и построчно — двести строк технических записей о
 * блоке, который в итоге собрался целиком и прошёл все проверки. Читать это
 * незачем: попытка, после которой уровень всё равно принят, — рабочий ход
 * генератора, а не проблема.
 */
const STAGE_SETTING: Record<string, string> = {
  'пул категорий': 'темы (включённые и исключённые), окно свежести категорий, коридор по категориям в конфиге декад на шаге «База контента»',
  'выбор категорий': 'число категорий на уровне и «мета-пар на уровень»',
  'мета-связи': '«мета-пар на уровень» и «глубина мета»',
  картинка: 'галочка 🖼 на графике ритма: у имён мета-категорий этого уровня нет значка в словаре — снимите галочку или дайте уровню другие мета-пары',
  'назначение слов': 'окно свежести слов и наполнение базы: категориям не хватает утверждённых слов',
  редкость: 'редких слов на уровень',
};

interface SettingConflict {
  setting: string;
  attempts: number;
  reason: string;
  levels: number[];
}

/**
 * Что мешало собрать ПРОБЛЕМНЫЕ уровни.
 *
 * Проблемный — это либо уровень, который не собрался вовсе, либо собранный, но
 * не прошедший hard-инварианты, либо с числом решений не равным одному. Если
 * таких нет, функция возвращает пустой список и на экране не появляется ничего:
 * блок собрался, объяснять нечего.
 */
function settingConflicts(block: BlockResult): SettingConflict[] {
  const broken = block.levels.filter((l) => !l.validation.passed || l.solutions.count !== 1);
  const sources = [
    ...block.failures.map((f) => ({ levelId: f.levelId, attempts: f.attempts })),
    ...broken.map((l) => ({ levelId: l.spec.levelId, attempts: l.attempts })),
  ];
  if (!sources.length) return [];

  const byStage = new Map<string, SettingConflict>();
  for (const source of sources) {
    for (const attempt of source.attempts) {
      if (attempt.outcome !== 'rejected') continue;
      const setting = STAGE_SETTING[attempt.stage] ?? attempt.stage;
      const entry = byStage.get(setting)
        ?? { setting, attempts: 0, reason: attempt.reason, levels: [] };
      entry.attempts += 1;
      // держим последнюю причину: она ближе всего к тому, на чём всё встало
      entry.reason = attempt.reason;
      if (!entry.levels.includes(source.levelId)) entry.levels.push(source.levelId);
      byStage.set(setting, entry);
    }
  }
  return Array.from(byStage.values()).sort((a, b) => b.attempts - a.attempts);
}

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

  const conflicts = settingConflicts(block);

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
              <th className="num">пуз</th>
              <th className="num" title="мета-пар на уровне: сколько связей «категория внутри категории». Пузырь с именем другой категории на поле ничем не отмечен">мета</th>
              <th className="num" title="длина самой долгой цепочки вложенности: 1 — категория лежит в другой, 2 — та в третьей. Это НЕ количество пар">глуб</th>
              <th className="num">редк</th>
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

      {conflicts.length > 0 && (
        <div className="panel">
          <h2>Настройки, в которые упёрлась сборка</h2>
          <p className="hint">
            Показывается только когда есть проблемные уровни. Слева — настройка,
            об которую генератор споткнулся, справа — что именно не сошлось.
            Список собран из забракованных попыток этих уровней, а не всего блока.
          </p>
          <table>
            <thead>
              <tr><th>настройка</th><th className="num">попыток</th>
                <th>что не сошлось</th><th>уровни</th></tr>
            </thead>
            <tbody>
              {conflicts.map((c) => (
                <tr key={c.setting}>
                  <td>{c.setting}</td>
                  <td className="num muted">{c.attempts}</td>
                  <td className="small">{c.reason}</td>
                  <td className="mono small muted">{c.levels.join(', ')}</td>
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
