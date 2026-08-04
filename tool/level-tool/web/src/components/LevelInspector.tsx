/**
 * Экран 4 — карточка уровня.
 *
 * Разбивка оценки не должна быть таблицей из семи чисел: полоски влево-вправо
 * от нуля читаются сразу, а подписи «откалибровано» и «объявлено» показывают
 * границу между измеренным и решённым.
 */
import { useState } from 'react';
import type { BlockResult, GeneratedLevel, LevelSpec } from '../core/types.ts';
import type { ContentIndex } from '../core/snapshot.ts';
import type { ScoringConfig } from '../core/scoringDifficulty.ts';
import { formatScheme, parseScheme } from '../core/decadeProfiles.ts';
import { startCapacity } from '../core/deal.ts';

export function LevelInspector({
  level, block, index, scoring, onSelect, levels, onRedeal,
}: {
  level: GeneratedLevel;
  block: BlockResult;
  index: ContentIndex;
  scoring: ScoringConfig;
  onSelect: (id: number) => void;
  levels: GeneratedLevel[];
  /**
   * Переложить старт уровня по схеме (null — вернуть автоматическую). Не задан —
   * блок не наш: у уровней оригинала выкладка взята из записи, и «поправить» её
   * значило бы играть не тот уровень, который записан.
   */
  onRedeal?: (scheme: number[] | null) => void;
}) {
  const s = level.spec;
  const metaLinks = s.categories
    .flatMap((c) => c.words
      .filter((w) => w.kind === 'meta')
      .map((w) => ({ parent: c.key, child: w.metaChild!, word: w.text })));

  return (
    <>
      <div className="panel">
        <div className="spread">
          <div className="row">
            {levels.map((l) => (
              <button key={l.spec.levelId}
                className={`ghost ${l.spec.levelId === s.levelId ? 'on' : ''}`}
                onClick={() => onSelect(l.spec.levelId)}>{l.spec.levelId}</button>
            ))}
          </div>
        </div>
      </div>

      <div className="panel">
        <div className="spread">
          <div>
            <h2>Уровень {s.levelId} · {level.plan.role}</h2>
            <p className="hint">
              {s.categories.length} категорий · {s.board.startBubbles} пузырей всего,
              на старте видно {s.deal.start.length}
              {s.board.dealStartBubbles
                ? ` (бюджет декады ${s.board.dealStartBubbles.join('-')})` : ''} ·
              лимит {s.board.moveLimit} ходов при минимуме {s.board.moveFloor} ·
              вместимость поля {s.board.boardCapacity}, остальное досыпается
            </p>
          </div>
          <div className="row">
            <span className={`tag ${level.validation.passed ? 'ok' : 'fail'}`}>
              {level.validation.passed ? 'проверки пройдены' : 'есть нарушения'}
            </span>
            <span className={`tag ${level.solutions.count === 1 ? 'ok' : 'fail'}`}>
              решений: {level.solutions.count}
            </span>
            <span className="tag">D {level.difficulty.value}</span>
            <span className="tag">I {level.interest.value}</span>
          </div>
        </div>

        <StartScheme level={level} onRedeal={onRedeal} />
      </div>

      <div className="grid c2">
        <div className="panel">
          <h2>Категории и слова</h2>
          <p className="hint">
            <span className="tag meta">мета</span> — слово этого пузыря есть имя другой
            категории уровня: он не лежит на старте и приходит, только когда та
            категория собрана; «мета·картинка» — пузырь рисуется значком вместо слова
            (простое имя, примерно четверть мета-пузырей). Тег{' '}
            <span className="tag meta">глубина N → …</span> у самой категории — это её
            место в цепочке, а не число её связей.{' '}
            <span className="tag trap">редкое</span> — zipf ниже 3.
          </p>
          {s.categories.map((c) => (
            <div key={c.key} style={{ borderTop: '1px solid var(--line)', padding: '8px 0' }}>
              <div className="row">
                <strong>{c.label}</strong>
                <span className="tag">{c.theme}</span>
                {c.isQuickwin && <span className="tag ok">быстрая победа</span>}
                {c.metaDepth > 0 && (
                  <span className="tag meta">глубина {c.metaDepth} → {c.parentKey}</span>
                )}
              </div>
              <div className="small muted" style={{ margin: '2px 0 5px' }}>{c.rule}</div>
              <div className="row">
                {c.words.map((w) => {
                  const rare = w.zipf !== null && w.zipf < 3;
                  return (
                    <span key={w.text}
                      className={`tag ${w.kind === 'meta' ? 'meta' : rare ? 'trap' : ''}`}>
                      {w.icon && <span style={{ marginRight: 3 }}>{w.icon}</span>}
                      {w.text}
                      <span className="muted mono" style={{ fontSize: 10, marginLeft: 4 }}>
                        {w.kind === 'meta' ? (w.icon ? 'мета·картинка' : 'мета')
                          : w.zipf?.toFixed(1) ?? '?'}
                      </span>
                    </span>
                  );
                })}
              </div>
            </div>
          ))}
        </div>

        <div>
          <div className="panel">
            <h2>Мета-лес</h2>
            <p className="hint">
              Каждая стрелка — одна мета-пара: собранная категория превращается в
              пузырь со своим именем и уходит в ту, на которую указывает. Число
              стрелок — это «мета» в таблице блока, длина самой долгой ветки —
              «глуб». Именно лес, а не дерево: связность не требуется, в референсе
              мета-граф распадается в среднем на 2.12 независимых компонент.
            </p>
            {metaLinks.length === 0
              ? <p className="small muted">Плоский уровень: мета-связей нет.</p>
              : <MetaForest links={metaLinks} categories={s.categories} />}
          </div>

          <div className="panel">
            <h2>Сложность D = {level.difficulty.value}</h2>
            <p className="hint">
              Модель разделена по источнику истины. Первая корзина откалибрована
              на 199 уровнях референса; вторая — объявленные продуктовые веса,
              которые референс не идентифицирует.
            </p>
            <Bucket title="откалибровано на референсе" items={level.difficulty.base}
              total={level.difficulty.baseTotal} color="#4cc2ff" />
            <Bucket title="объявлено, не откалибровано" items={level.difficulty.declared}
              total={level.difficulty.declaredTotal} color="#bc8cff" />
            <Bucket title="семантика: двусмысленность" items={level.difficulty.semantic}
              total={level.difficulty.semanticTotal} color="#ff9e64" />
            <Bucket title="механика: лимит ходов" items={level.difficulty.mechanical}
              total={level.difficulty.mechanicalTotal} color="#d29922" />
            <ul className="small muted" style={{ paddingLeft: 18, marginTop: 10 }}>
              {level.difficulty.explanation.map((e, i) => <li key={i}>{e}</li>)}
            </ul>
          </div>

          <div className="panel">
            <h2>Интересность I = {level.interest.value}</h2>
            <p className="hint">
              Четыре композита по 0–2.5. Это не объективная мера веселья, а модель
              зафиксированного продуктового суждения.
            </p>
            <Bucket title="композиты" color="#3fb950" total={level.interest.value}
              items={{
                Clarity: level.interest.clarity,
                Variety: level.interest.variety,
                Aha: level.interest.aha,
                Freshness: level.interest.freshness,
              }} max={2.5} />
            <ul className="small muted" style={{ paddingLeft: 18, marginTop: 10 }}>
              {level.interest.explanation.map((e, i) => <li key={i}>{e}</li>)}
            </ul>
          </div>
        </div>
      </div>

      {s.traps.length > 0 && (
        <div className="panel">
          <h2>Ловушки</h2>
          <p className="hint">
            Ловушка — не повтор слова в двух категориях, а слово с ОДНИМ домом
            при наличии на поле второй правдоподобной категории. Связь настоящая
            (высокий fit), но тихая (низкая очевидность).
          </p>
          <table>
            <thead>
              <tr><th>слово</th><th>дом</th><th>приманка</th>
                <th className="num">fit приманки</th>
                <th className="num">очевидность приманки</th></tr>
            </thead>
            <tbody>
              {s.traps.map((t, i) => (
                <tr key={i}>
                  <td className="mono">{t.word}</td>
                  <td className="small">{t.home}</td>
                  <td className="small">{t.decoy}</td>
                  <td className="num">{t.decoyFit.toFixed(2)}</td>
                  <td className="num">{t.decoyObviousness.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {level.blindPlay && level.playability && (
        <BlindPlayPanel blind={level.blindPlay} minMoves={level.playability.movesNeeded} />
      )}

      <div className="panel">
        <h2>Проверки</h2>
        <table>
          <thead><tr><th>код</th><th>тип</th><th>итог</th><th>детали</th></tr></thead>
          <tbody>
            {level.validation.checks.map((c) => (
              <tr key={c.code}>
                <td className="mono small">{c.code}</td>
                <td className="small muted">{c.severity === 'hard' ? 'hard' : 'soft'}</td>
                <td>
                  <span className={`tag ${c.passed ? 'ok' : c.severity === 'hard' ? 'fail' : 'warn'}`}>
                    {c.passed ? 'PASS' : 'FAIL'}
                  </span>
                </td>
                <td className="small">{c.detail}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="small muted" style={{ marginTop: 10 }}>
          Единственность решения проверена перебором:
          {' '}{level.solutions.nodesVisited} узлов,
          {' '}{level.solutions.exhausted ? 'перебор исчерпан' : 'перебор обрезан по лимиту'}.
          {' '}Отсутствие тупиков в чистой сортировке слов доказывается графовым
          инвариантом мета-леса, а не прогонами бота: у каждого слова один дом,
          порядок сборки не важен.
        </p>
      </div>

      <div className="panel">
        <h2>Происхождение</h2>
        <table>
          <tbody>
            <tr><td className="muted small">хеш уровня</td>
              <td className="mono small">{level.levelSpecHash}</td></tr>
            <tr><td className="muted small">хеш пакета</td>
              <td className="mono small">{block.packHash}</td></tr>
            <tr><td className="muted small">снимок базы</td>
              <td className="mono small">{block.contentSnapshotHash}</td></tr>
            <tr><td className="muted small">версия генератора</td>
              <td className="mono small">{block.generatorVersion}</td></tr>
            <tr><td className="muted small">версия скоринга</td>
              <td className="mono small">{scoring.scoring_version}</td></tr>
            <tr><td className="muted small">seed</td>
              <td className="mono small">{block.config.seed}</td></tr>
            <tr><td className="muted small">попыток генерации</td>
              <td className="mono small">{level.attempts.length}</td></tr>
          </tbody>
        </table>
        <p className="small muted" style={{ marginTop: 8 }}>
          Время сборки в хеш не входит: иначе обещание «тот же вход → тот же уровень»
          нарушалось бы каждым запуском.
        </p>
      </div>
    </>
  );
}

/**
 * Слепой прогон: во что уровень обходится игроку, который читает слова, а не
 * ответы. Панель намеренно не показывает ни одной оценки — только ходы, промахи
 * и бюджет ошибок. Это диагностика: числа модели не откалиброваны, и подавать
 * их рядом с D как ещё одну оценку значило бы намекнуть, что им уже верят.
 */
function BlindPlayPanel({ blind, minMoves }: {
  blind: import('../core/simulateBlindPlay.ts').BlindPlayResult;
  minMoves: number;
}) {
  if (blind.unavailable) {
    return (
      <div className="panel">
        <h2>Слепой прогон</h2>
        <p className="small muted">{blind.unavailable}</p>
      </div>
    );
  }
  const used = blind.errorBudgetUsed;
  const budgetTag = used === null ? 'нет лимита'
    : used > 1 ? 'fail' : used > 0.7 ? 'warn' : 'ok';

  return (
    <div className="panel">
      <div className="spread">
        <div>
          <h2>Слепой прогон — цена незнания слов</h2>
          <p className="hint">
            Зрячий бот знает ответы и не промахивается: его запас ходов и есть
            бюджет ошибок живого игрока. Здесь этот бюджет ТРАТИТСЯ. Игрок читает
            слова — очевидность связи, приторможенная редкостью, — нечитаемое
            пробует наугад, неверная догадка стоит ход, как в прототипе.
            {' '}{blind.seeds} прогонов, у каждого своя выборка знакомых слов.
          </p>
        </div>
        <div className="row">
          <span className={`tag ${used === null ? '' : budgetTag}`}>
            бюджет ошибок {used === null ? '—' : `${Math.round(used * 100)}%`}
          </span>
          <span className={`tag ${blind.winRate >= 1 ? 'ok' : blind.winRate >= 0.75 ? 'warn' : 'fail'}`}>
            доходят {Math.round(blind.winRate * 100)}%
          </span>
        </div>
      </div>

      <table>
        <thead>
          <tr><th>что</th><th className="num">медиана</th><th className="num">p90</th>
            <th>чем это является</th></tr>
        </thead>
        <tbody>
          <tr>
            <td className="small">ходов на партию</td>
            <td className="num mono">{blind.movesMedian}</td>
            <td className="num mono">{blind.movesP90}</td>
            <td className="small muted">
              минимум {minMoves}
              {blind.moveLimit === null ? ', лимита нет' : `, лимит ${blind.moveLimit}`}
            </td>
          </tr>
          <tr>
            <td className="small">промахов</td>
            <td className="num mono">{blind.missesMedian}</td>
            <td className="num mono">{blind.missesP90}</td>
            <td className="small muted">ходов, отданных за неверную догадку</td>
          </tr>
          <tr>
            <td className="small">ходов вслепую</td>
            <td className="num mono">{blind.guessTurnsMedian}</td>
            <td className="num mono">—</td>
            <td className="small muted">
              поле не показало ни одного мерджа, который игрок понимает
            </td>
          </tr>
          <tr>
            <td className="small">догадок</td>
            <td className="num mono">{blind.probesMedian}</td>
            <td className="num mono">—</td>
            <td className="small muted">
              из них верных {Math.round(blind.probeHitRate * 100)}%: догадка
              опирается на размер уже собранной группы, поэтому попадает чаще
              случайной
            </td>
          </tr>
          <tr>
            <td className="small">досыпок-подсказок</td>
            <td className="num mono">{blind.hintRefillsMedian}</td>
            <td className="num mono">—</td>
            <td className="small muted">
              помощь прототипа после 5 промахов подряд
            </td>
          </tr>
        </tbody>
      </table>

      <div className="row" style={{ marginTop: 10 }}>
        <span className="tag">ясность слов {blind.clarity.toFixed(2)}</span>
        <span className="tag">
          старт читается на {Math.round(blind.startReadableShare * 100)}%
        </span>
        <span className={`tag ${blind.anchorlessCategories > 0 ? 'warn' : 'ok'}`}>
          категорий без опоры {blind.anchorlessCategories}
        </span>
        {blind.hardStalls > 0 && (
          <span className="tag fail">партия встала: {blind.hardStalls} из {blind.seeds}</span>
        )}
      </div>

      <ul className="small muted" style={{ paddingLeft: 18, marginTop: 10 }}>
        {blind.notes.map((n, i) => <li key={i}>{n}</li>)}
      </ul>
      <p className="small muted">
        В оценку D и в гейт приёмки эти числа НЕ входят: модель знания игрока
        ({blind.knowledgeVersion}) не откалибрована — живых наигровок с замером
        промахов у нас нет, а в референсе нет раскладки поля. Читать их надо как
        нижнюю границу: у бота идеальная память и он видит все досыпанные слова
        сразу, значит живому игроку уровень дешевле не обойдётся.
      </p>
    </div>
  );
}

function Bucket({ title, items, total, color, max }: {
  title: string; items: Record<string, number>; total: number; color: string; max?: number;
}) {
  const scale = max ?? Math.max(1.5, ...Object.values(items).map((v) => Math.abs(v)));
  return (
    <div style={{ marginBottom: 12 }}>
      <div className="spread" style={{ marginBottom: 5 }}>
        <span className="small muted">{title}</span>
        <span className="mono small">{total >= 0 ? '+' : ''}{total.toFixed(2)}</span>
      </div>
      <div className="bars">
        {Object.entries(items).map(([name, value]) => (
          <div className="bar-row" key={name}>
            <div className="bar-track">
              <div className="bar-mid" />
              <div className="bar-fill" style={{
                background: color,
                opacity: 0.75,
                width: `${Math.min(50, (Math.abs(value) / scale) * 50)}%`,
                left: value >= 0 ? '50%' : undefined,
                right: value < 0 ? '50%' : undefined,
              }} />
              <span className="bar-label">{name}</span>
            </div>
            <span className="mono small" style={{ textAlign: 'right' }}>
              {value >= 0 ? '+' : ''}{value.toFixed(2)}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

/** Мета-лес: ярусами сверху вниз, корни сверху. */
function MetaForest({ links, categories }: {
  links: { parent: string; child: string; word: string }[];
  categories: { key: string; label: string; metaDepth: number }[];
}) {
  const involved = new Set(links.flatMap((l) => [l.parent, l.child]));
  const byDepth = new Map<number, string[]>();
  for (const key of involved) {
    const depth = categories.find((c) => c.key === key)?.metaDepth ?? 0;
    byDepth.set(depth, [...(byDepth.get(depth) ?? []), key]);
  }
  const depths = Array.from(byDepth.keys()).sort((a, b) => b - a);
  const labelOf = (key: string) =>
    categories.find((c) => c.key === key)?.label ?? key;

  return (
    <div>
      {depths.map((depth) => (
        <div key={depth} style={{ marginBottom: 8 }}>
          <div className="muted small" style={{ marginBottom: 3 }}>
            {depth === 0 ? 'корни — никого не ждут' : `глубина ${depth}`}
          </div>
          <div className="row">
            {byDepth.get(depth)!.map((key) => (
              <span key={key} className={`tag ${depth > 0 ? 'meta' : ''}`}>{labelOf(key)}</span>
            ))}
          </div>
        </div>
      ))}
      <div style={{ borderTop: '1px solid var(--line)', paddingTop: 8, marginTop: 4 }}>
        {links.map((l, i) => (
          <div key={i} className="small" style={{ margin: '2px 0' }}>
            <span className="tag meta">{l.word}</span>
            <span className="muted"> — имя категории {labelOf(l.child)}, лежит словом в </span>
            <strong>{labelOf(l.parent)}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}

/**
 * Применённая схема старта и её правка на месте.
 *
 * Зачем показывать. Схема — самое сильное, что решает вопрос «а можно ли с этого
 * поля вообще начать»: при ровной раздаче уровень на 12 категорий встречает
 * игрока полем из пар, где не собирается ни одна. Раньше схему приходилось
 * искать в таблице декад на первом шаге и держать в голове; здесь она показана
 * ФАКТИЧЕСКАЯ — посчитанная из выкладки, а не из настройки, поэтому верна и для
 * автоматической раздачи, и для ручной.
 *
 * Зачем править здесь же. Проверка гипотезы «глубже старт — уровень идёт» стоила
 * пересборки всего блока, а после пересборки менялся весь контент, и понять,
 * что дало эффект, было нельзя. Правка схемы состав уровня не трогает: те же
 * категории и слова, другое стартовое поле. Пересчитываются при этом ВСЕ
 * проверки и оценки (см. redealLevel), поэтому ручная схема не отменяет приёмку.
 */
function StartScheme({ level, onRedeal }: {
  level: GeneratedLevel;
  onRedeal?: (scheme: number[] | null) => void;
}) {
  const s = level.spec;
  const applied = appliedScheme(s);
  const [draft, setDraft] = useState<string | null>(null);
  const raw = draft ?? formatScheme(applied);
  const parsed = parseScheme(raw);
  const bad = parsed === undefined;
  const manual = !!(s.board.dealScheme && s.board.dealScheme.length > 0);

  const capacity = startCapacity(s.board.boardCapacity, s.board.dealStartBubbles ?? null);
  const startBubbles = s.deal.start.length;
  const absent = s.categories.length - applied.length;
  const play = level.playability;
  /**
   * Запрошено не равно выложенному — и это законно, а не сбой.
   *
   * Доля меньше просимой по двум причинам: у категории с мета-словом спавнящихся
   * слов всего три (мета-пузырь на старте не лежит), и доля не берётся частично,
   * если целиком не влезла в бюджет поля. Молчать об этом нельзя: человек видит
   * в поле «4-4-3», а на старте лежит другое, и правка выглядит как не сработавшая.
   */
  const asked = manual ? [...s.board.dealScheme!].sort((a, b) => b - a) : null;
  const mismatch = asked && formatScheme(asked) !== formatScheme(applied);
  // очередь линий: категории, которых на старте нет по правилу, а не по остатку
  // бюджета поля (см. planGates в core/deal.ts)
  const gates = [...(s.deal.gates ?? [])].sort((a, b) => a.afterCollected - b.afterCollected);

  const apply = () => {
    if (bad || !onRedeal) return;
    onRedeal(parsed);
    setDraft(null);
  };

  return (
    <div style={{ borderTop: '1px solid var(--line)', marginTop: 12, paddingTop: 12 }}>
      <div className="row">
        <span className="lbl" style={{ color: 'var(--muted)', fontSize: 11,
          textTransform: 'uppercase', letterSpacing: '0.04em' }}>
          схема старта
        </span>
        {onRedeal
          ? (
            <>
              <input
                type="text"
                value={raw}
                className={bad ? 'pending' : undefined}
                style={{ width: 200, fontFamily: 'var(--mono)' }}
                onChange={(e) => setDraft(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter') apply(); }}
              />
              <button className="primary" disabled={bad} onClick={apply}>
                Переложить старт
              </button>
              <button className="ghost" onClick={() => { setDraft(null); onRedeal(null); }}>
                авто
              </button>
            </>
          )
          : <span className="tag mono">{formatScheme(applied)}</span>}
        <span className={`tag ${manual ? 'warn' : ''}`}>
          {manual ? 'задана вручную' : 'посчитана автоматически'}
        </span>
      </div>

      <p className="small muted" style={{ margin: '8px 0 0' }}>
        Доли старта по убыванию: сколько слов каждой категории видно в начале.
        {' '}<strong style={{ color: 'var(--text)' }}>4</strong> — категорию можно
        собрать сразу, <strong style={{ color: 'var(--text)' }}>3</strong> — не хватает
        одного слова (закроется первой пачкой досыпки),{' '}
        <strong style={{ color: 'var(--text)' }}>2</strong> — пара, которая ждёт двух
        слов. Всего цифр — сколько категорий вообще есть на старте; остальные
        приходят досыпкой. Значения 1–4, разделитель любой: «4-3-3-3» или «4 3 3 3».
      </p>

      <div className="row" style={{ marginTop: 8 }}>
        <span className="tag">на старте {startBubbles} пузырей из {capacity} возможных</span>
        <span className="tag">категорий на поле {applied.length}, в очереди {absent}</span>
        {play && (
          <span className={`tag ${play.winnable ? 'ok' : 'fail'}`}>
            {play.winnable
              ? `проходится за ${play.movesNeeded} ходов`
              : `не проходится: ${play.failReason}`}
          </span>
        )}
        {play && play.rescues > 0 && (
          <span className="tag warn">досыпок вне ритма {play.rescues}</span>
        )}
        {play && play.perceivedDead > 0 && (
          <span className="tag warn">
            состояний «выглядит тупиком» {play.perceivedDead}
          </span>
        )}
        {play && play.maxDrought > 0 && (
          <span className="tag">
            самая долгая пауза без сбора: {play.maxDrought} ходов
          </span>
        )}
        {play && play.gatesForced > 0 && (
          <span className="tag warn">
            гейт вскрыт досыпкой {play.gatesForced} раз
          </span>
        )}
      </div>

      {gates.length > 0 && (
        <p className="small muted" style={{ margin: '8px 0 0' }}>
          <strong style={{ color: 'var(--text)' }}>Очередь линий:</strong>{' '}
          {gates.length} {gates.length === 1 ? 'категория' : 'категории'} не
          показываются со старта и выходят на поле по прогрессу —{' '}
          {gates.map((g) => `${categoryLabel(s, g.category)} после `
            + `${g.afterCollected}`).join(', ')} сборов. На поле из 24 пузырей
          больше двенадцати живых линий одновременно означает, что собрать нельзя
          ничего: досыпка тратит пачку на четыре разные категории, не закрывая ни
          одной. Порог считает planGates в core/deal.ts.
        </p>
      )}

      {bad && (
        <p className="small" style={{ color: 'var(--warn)', margin: '8px 0 0' }}>
          Схема не разобрана: нужны числа 1–4 через дефис, запятую или пробел.
        </p>
      )}
      {mismatch && (
        <p className="small" style={{ color: 'var(--warn)', margin: '8px 0 0' }}>
          Запрошено {formatScheme(asked!)}, выложено {formatScheme(applied)}. Доля
          выходит меньше, когда категории нечем её закрыть (у категории с мета-словом
          на старте максимум 3 пузыря: имя-мета не спавнится) или когда доля целиком
          не влезла в бюджет поля — частичных долей выкладка не делает, иначе
          появлялись бы одиночки.
        </p>
      )}
      {onRedeal && (
        <p className="small muted" style={{ margin: '8px 0 0' }}>
          После правки уровень пересчитывается целиком: выкладка, проходимость,
          hard-инварианты, единственность решения, D и I, хеш уровня и пакета.
          Состав уровня не меняется — те же категории и слова, другое стартовое поле.
        </p>
      )}
    </div>
  );
}

/** Имя категории для подписи; ключ, если категории в уровне почему-то нет. */
function categoryLabel(spec: LevelSpec, key: string): string {
  return spec.categories.find((c) => c.key === key)?.label ?? key;
}

/**
 * Фактическая схема старта: сколько слов каждой категории лежит на поле.
 *
 * Считается из ВЫКЛАДКИ, а не из `board.dealScheme`: настройка бывает пустой
 * (автоматическая раздача), и тогда схему видно только по самому полю. Нули
 * отброшены — категория, которой на старте нет, в схеме не участвует, она целиком
 * в очереди досыпки.
 */
function appliedScheme(spec: LevelSpec): number[] {
  const counts = new Map<string, number>();
  for (const bubble of spec.deal.start) {
    counts.set(bubble.category, (counts.get(bubble.category) ?? 0) + 1);
  }
  return [...counts.values()].filter((n) => n > 0).sort((a, b) => b - a);
}
