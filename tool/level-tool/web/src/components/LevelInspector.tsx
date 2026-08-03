/**
 * Экран 4 — карточка уровня.
 *
 * Разбивка оценки не должна быть таблицей из семи чисел: полоски влево-вправо
 * от нуля читаются сразу, а подписи «откалибровано» и «объявлено» показывают
 * границу между измеренным и решённым.
 */
import type { BlockResult, GeneratedLevel } from '../core/types.ts';
import type { ContentIndex } from '../core/snapshot.ts';
import type { ScoringConfig } from '../core/scoringDifficulty.ts';

export function LevelInspector({ level, block, index, scoring, onSelect, levels }: {
  level: GeneratedLevel;
  block: BlockResult;
  index: ContentIndex;
  scoring: ScoringConfig;
  onSelect: (id: number) => void;
  levels: GeneratedLevel[];
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
      </div>

      <div className="grid c2">
        <div className="panel">
          <h2>Категории и слова</h2>
          <p className="hint">
            <span className="tag meta">мета</span> — имя собранной категории, на старте
            не спавнится; «мета·картинка» — пузырь рисуется значком вместо слова
            (простое имя, примерно четверть мета-пузырей).{' '}
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
              Именно лес, а не дерево: связность не требуется. В референсе мета-граф
              распадается в среднем на 2.12 независимых компонент.
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
