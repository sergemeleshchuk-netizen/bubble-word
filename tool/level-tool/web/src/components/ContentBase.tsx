/**
 * Экран 1 — База контента.
 *
 * Задача экрана продуктовая, а не информационная: показать, что AI действительно
 * создавал и ревьюил контент, а не упомянут в README. Поэтому здесь видно не только
 * размер базы, но и что модель сделала неправильно, кто это поймал и как исправили.
 */
import { useState } from 'react';
import type { Snapshot } from '../core/types.ts';
import type { ContentIndex } from '../core/snapshot.ts';
import type { ContentSource } from '../core/sources.ts';

interface AiRuns {
  prompt_library: { id: string; file: string; purpose: string }[];
  runs: {
    run_id: string; prompt_id: string; prompt_file: string; model: string;
    items_received: number;
    totals?: Record<string, number>;
    decisions: Record<string, number>;
    decided_by: Record<string, number>;
    model_errors: { type: string; severity: string; what: string; detail: string;
      caught_by?: string; fix?: string; lesson?: string; scores?: Record<string, number> }[];
    downgraded: { what: string; to: string; why: string }[];
    model_did_well: string[];
    human_fixes: { renamed_categories: string[]; dropped_categories: string[];
      retargeted: Record<string, string>; dropped_memberships: number };
  }[];
  content_base: Record<string, number | Record<string, number>>;
  where_ai_helped: string[];
  where_ai_is_not_used: string[];
}

export function ContentBase({ snapshot, index, runs, source }: {
  snapshot: Snapshot; index: ContentIndex; runs: AiRuns; source: ContentSource;
}) {
  const [tab, setTab] = useState<'stats' | 'ai' | 'errors'>('stats');
  const s = snapshot.stats ?? {};
  const base = runs.content_base as Record<string, number>;

  /**
   * Журнал AI-прогонов и разбор ошибок модели — это история НАШЕЙ базы
   * (`ai_runs.json`). У чужого словаря её нет и быть не может, поэтому на нём
   * показываем один экран из трёх. Показывать все три, подставив чужие цифры
   * в наши таблицы, было бы прямым враньём о происхождении контента.
   */
  if (!source.hasAiWorkflow) {
    return <ForeignSource snapshot={snapshot} index={index} source={source} />;
  }
  const byStatus = (runs.content_base.by_status ?? {}) as Record<string, number>;
  const zipf = (runs.content_base.zipf_buckets ?? {}) as Record<string, number>;
  const run = runs.runs[0];

  return (
    <>
      <div className="panel">
        <div className="spread">
          <div>
            <h2>База контента</h2>
            <p className="hint">
              Категория — не список слов, а запрос по признакам. Одно слово живёт
              сразу в нескольких категориях, поэтому при сборке уровня приходится
              доказывать, что у каждого слова ровно один дом.
            </p>
          </div>
          <div className="row">
            <button className={`ghost ${tab === 'stats' ? 'on' : ''}`}
              onClick={() => setTab('stats')}>Состав</button>
            <button className={`ghost ${tab === 'ai' ? 'on' : ''}`}
              onClick={() => setTab('ai')}>AI-воркфлоу</button>
            <button className={`ghost ${tab === 'errors' ? 'on' : ''}`}
              onClick={() => setTab('errors')}>Ошибки модели</button>
          </div>
        </div>

        {tab === 'stats' && (
          <>
            <div className="grid c4">
              <Stat v={base.categories} k="категорий" />
              <Stat v={base.words} k="слов" />
              <Stat v={base.memberships} k="связей слово ↔ категория" />
              <Stat v={base.senses} k="разведённых значений"
                note="bank как учреждение и как берег" />
              <Stat v={base.themes} k="тематических сфер" />
              <Stat v={base.multi_category_words} k="слов в 2+ категориях"
                note="готовый справочник ловушек" />
              <Stat v={s.meta_capable_with_host as number} k="мета-пригодных категорий"
                note="имя категории само является пузырём" />
              <Stat v={s.frequency_unknown_words as number} k="слов неизвестны частотнику"
                note="отдельный сигнал, не zipf = 0" />
            </div>

            <div className="grid c2" style={{ marginTop: 16 }}>
              <div>
                <h3 style={{ fontSize: 13, margin: '0 0 8px' }}>Статусы связей</h3>
                <table>
                  <tbody>
                    <tr><td><span className="tag ok">approved</span></td>
                      <td className="muted small">игрок вспоминает первым, годится как дом</td>
                      <td className="num">{byStatus.approved}</td></tr>
                    <tr><td><span className="tag trap">alternative</span></td>
                      <td className="muted small">верно, но не первая мысль — материал ловушек</td>
                      <td className="num">{byStatus.alternative}</td></tr>
                    <tr><td><span className="tag warn">hard_only</span></td>
                      <td className="muted small">верно, но сам не догадается</td>
                      <td className="num">{byStatus.hard_only}</td></tr>
                    <tr><td><span className="tag fail">rejected</span></td>
                      <td className="muted small">в игру не идёт</td>
                      <td className="num">{byStatus.rejected ?? 0}</td></tr>
                  </tbody>
                </table>
                <p className="muted small" style={{ marginTop: 8 }}>
                  Статусы проставлены по человеческим ассоциациям SWOW (12 282 стимула,
                  ответы живых людей), а не оценкой модели «на глаз».
                </p>
              </div>
              <div>
                <h3 style={{ fontSize: 13, margin: '0 0 8px' }}>Частотность слов</h3>
                <table>
                  <tbody>
                    {Object.entries(zipf).map(([bucket, n]) => (
                      <tr key={bucket}>
                        <td>{bucket}</td>
                        <td className="num">{n}</td>
                        <td className="num muted">
                          {((n / base.words) * 100).toFixed(1)}%
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <p className="muted small" style={{ marginTop: 8 }}>
                  Граница top-50k английского — zipf 2.55. Правило генератора:
                  не менее 90% пузырей уровня внутри неё.
                </p>
              </div>
            </div>

          </>
        )}

        {tab === 'ai' && (
          <>
            <div className="grid c4">
              <Stat v={run.items_received} k="записей от модели в прогоне" />
              <Stat v={run.decisions.approved} k="утверждено" />
              <Stat v={run.decisions.alternative + run.decisions.hard_only}
                k="понижено до ловушек и сложных" />
              <Stat v={run.decisions.rejected} k="отклонено" />
            </div>

            <h3 style={{ fontSize: 13, margin: '16px 0 8px' }}>Кто принимал решение</h3>
            <div className="row">
              {Object.entries(run.decided_by).map(([who, n]) => (
                <span className="tag" key={who}>{who} · {n}</span>
              ))}
            </div>
            <p className="muted small" style={{ marginTop: 6 }}>
              Модель никогда не ставит статус сама. Между её ответом и базой стоят три
              слоя: механическая политика по двум числам связи, критик-скептик
              и решение человека с письменной причиной.
            </p>

            <h3 style={{ fontSize: 13, margin: '16px 0 8px' }}>Библиотека промптов</h3>
            <table>
              <thead><tr><th>id</th><th>файл</th><th>зачем</th></tr></thead>
              <tbody>
                {runs.prompt_library.map((p) => (
                  <tr key={p.id}>
                    <td className="mono">{p.id}</td>
                    <td className="mono muted small">{p.file}</td>
                    <td className="small">{p.purpose}</td>
                  </tr>
                ))}
              </tbody>
            </table>

            <div className="grid c2" style={{ marginTop: 16 }}>
              <div>
                <h3 style={{ fontSize: 13, margin: '0 0 8px' }}>Где AI дал ускорение</h3>
                <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
                  {runs.where_ai_helped.map((x) => <li key={x}>{x}</li>)}
                </ul>
              </div>
              <div>
                <h3 style={{ fontSize: 13, margin: '0 0 8px' }}>
                  Где AI сознательно НЕ используется
                </h3>
                <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
                  {runs.where_ai_is_not_used.map((x) => <li key={x}>{x}</li>)}
                </ul>
              </div>
            </div>
          </>
        )}

        {tab === 'errors' && (
          <>
            <p className="hint">
              Это важнее списка успехов: видно, что процесс контролировался, а не
              делегировался. Ошибки зафиксированы на первом проходе проверки схемы,
              до импорта в базу.
            </p>
            {run.model_errors.map((e) => (
              <div key={e.what} style={{ borderTop: '1px solid var(--line)', paddingTop: 10,
                marginTop: 10 }}>
                <div className="row">
                  <span className={`tag ${e.severity === 'blocking' ? 'fail' : 'warn'}`}>
                    {e.severity === 'blocking' ? 'заблокировано схемой' : 'отклонено критиком'}
                  </span>
                  <strong className="mono">{e.what}</strong>
                  <span className="tag">{e.type}</span>
                  {e.scores && (
                    <span className="muted small mono">
                      fit {e.scores.fit} · очевидность {e.scores.obviousness}
                    </span>
                  )}
                </div>
                <div className="small" style={{ marginTop: 5 }}>{e.detail}</div>
                {e.caught_by && (
                  <div className="small muted" style={{ marginTop: 3 }}>
                    поймал: {e.caught_by}
                  </div>
                )}
                {e.fix && (
                  <div className="small muted" style={{ marginTop: 3 }}>
                    исправление: {e.fix}
                  </div>
                )}
                {e.lesson && (
                  <div className="small" style={{ marginTop: 3, color: 'var(--accent)' }}>
                    вывод: {e.lesson}
                  </div>
                )}
              </div>
            ))}

            <h3 style={{ fontSize: 13, margin: '18px 0 6px' }}>
              Понижено, но не отклонено — {run.downgraded.length}
            </h3>
            <table>
              <thead><tr><th>связь</th><th>статус</th><th>почему</th></tr></thead>
              <tbody>
                {run.downgraded.map((d) => (
                  <tr key={d.what}>
                    <td className="mono small">{d.what}</td>
                    <td><span className="tag">{d.to}</span></td>
                    <td className="small muted">{d.why}</td>
                  </tr>
                ))}
              </tbody>
            </table>

            <h3 style={{ fontSize: 13, margin: '18px 0 6px' }}>Что модель сделала хорошо</h3>
            <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
              {run.model_did_well.map((x) => <li key={x}>{x}</li>)}
            </ul>

            <h3 style={{ fontSize: 13, margin: '18px 0 6px' }}>Ручные правки прогона</h3>
            <p className="small muted">
              Сырой вывод модели не редактируется никогда: правки лежат отдельным
              слоем в <span className="mono">human_fixes.json</span>, каждая с причиной.
              Переименовано категорий: {run.human_fixes.renamed_categories.length},
              отброшено: {run.human_fixes.dropped_categories.length},
              переадресовано ссылок: {Object.keys(run.human_fixes.retargeted).length},
              снято дубликатов: {run.human_fixes.dropped_memberships}.
            </p>
          </>
        )}
      </div>
    </>
  );
}

/**
 * Экран для источника, который мы не выращивали, а прочитали.
 *
 * Показывает три вещи, и третья важнее первых двух: размер словаря, чем он
 * отличается от нашего в цифрах и чего у него нет. Последний список — не
 * дисклеймер для приличия: генератор на этом источнике работает иначе (ловушки
 * рождаются из пересечений, а не из размеченного слоя), и не сказать об этом
 * значит выдать разницу в данных за разницу в качестве сборки.
 */
function ForeignSource({ snapshot, index, source }: {
  snapshot: Snapshot; index: ContentIndex; source: ContentSource;
}) {
  const s = snapshot.stats ?? {};
  const num = (key: string): number | undefined =>
    (typeof s[key] === 'number' ? s[key] : undefined);

  // самые ходовые категории источника: сколько раз выходили и когда впервые
  const busiest = [...snapshot.categories]
    .map((c, i) => ({ c, i }))
    .filter((x) => (x.c.ref_levels ?? 0) > 1)
    .sort((a, b) => (b.c.ref_levels ?? 0) - (a.c.ref_levels ?? 0))
    .slice(0, 12);

  const zipfMedian = num('zipf_median_x100');
  const poolMedian = num('pool_size_median_x100');
  const mapped = num('categories_theme_mapped');
  const categories = num('categories') ?? snapshot.categories.length;

  return (
    <>
      <div className="panel">
        <h2>{source.label}</h2>
        <p className="hint">{source.summary}</p>

        <div className="grid c4">
          <Stat v={num('reference_levels')} k="уровней в выгрузке"
            note="полный отыгранный сезон игры" />
          <Stat v={categories} k="категорий"
            note={`${num('reference_category_occurrences')} вхождений в уровни`} />
          <Stat v={num('words')} k="слов" />
          <Stat v={num('memberships')} k="связей слово ↔ категория" />
          <Stat v={num('reference_meta_children')} k="вложенных категорий"
            note="имя ребёнка лежит пузырём в родителе" />
          <Stat v={num('trap_capable_words')} k="слов в 2+ категориях"
            note="единственный источник ловушек здесь" />
          <Stat v={num('words_above_generator_floor')} k="слов выше пола частотности"
            note="ниже 3.75 генератор слово не возьмёт" />
          <Stat v={num('frequency_unknown_words')} k="слов неизвестны частотнику" />
        </div>
      </div>

      <div className="panel">
        <h2>Чем этот словарь отличается от нашего</h2>
        <p className="hint">
          Цифры сравнимы: частотность считается тем же способом, шкала сложности
          категории та же. Разница в цифрах — разница в контенте, а не в методе.
        </p>
        <table>
          <thead>
            <tr><th>величина</th><th className="num">здесь</th><th>что это значит</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>медиана частотности слова</td>
              <td className="num">{zipfMedian !== undefined ? (zipfMedian / 100).toFixed(2) : '—'}</td>
              <td className="small muted">
                у нашей базы 3.58 — словарь оригинала заметно реже, и пол 3.75
                срезает здесь больше половины слов
              </td>
            </tr>
            <tr>
              <td>медиана размера пула категории</td>
              <td className="num">{poolMedian !== undefined ? (poolMedian / 100).toFixed(1) : '—'}</td>
              <td className="small muted">
                у нашей базы 14. Пул ровно из четырёх слов даёт четвёрку
                единственным способом — точному покрытию негде отступить
              </td>
            </tr>
            <tr>
              <td>категорий со сферой из нашего словаря</td>
              <td className="num">{mapped !== undefined ? `${mapped} из ${categories}` : '—'}</td>
              <td className="small muted">
                остальным сферой служит голова собственного имени: фильтр тем
                на них не сработает, разнообразие уровня — сработает
              </td>
            </tr>
            <tr>
              <td>мета-пригодных категорий</td>
              <td className="num">{num('meta_capable_categories') ?? '—'}</td>
              <td className="small muted">
                вложенность размечена самим источником, а не выведена — это
                самый богатый слой этого словаря
              </td>
            </tr>
            <tr>
              <td>запретов на пары категорий</td>
              <td className="num">{index.conflictCount}</td>
              <td className="small muted">
                источник их не объявляет; неразделимые пары ловит живой фильтр
                по пересечению пулов в генераторе
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="panel">
        <h2>Чего у источника нет</h2>
        <p className="hint">
          Список обязателен. Источник с меньшим числом слоёв разметки даёт другие
          уровни, и разницу нужно относить на данные, а не на генератор.
        </p>
        <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
          {source.limits.map((limit) => <li key={limit} style={{ marginBottom: 5 }}>{limit}</li>)}
        </ul>
        <p className="small" style={{ marginTop: 12, color: 'var(--accent)' }}>
          Наша база при этом не меняется ни на одну связь: словарь оригинала лежит
          отдельным снимком и только читается. Решение владельца от 31.07 —
          чужой словарь в нашу базу не вливать — остаётся в силе.
        </p>
      </div>

      {busiest.length > 0 && (
        <div className="panel">
          <h2>Самые ходовые категории оригинала</h2>
          <p className="hint">
            Сколько раз категория выходила за 1025 уровней и на каком появилась
            впервые. Пул у переиспользованных категорий шире четырёх слов — именно
            они и дают генератору свободу выбора.
          </p>
          <table>
            <thead>
              <tr>
                <th>категория</th><th>сфера</th>
                <th className="num">выходов</th><th className="num">впервые</th>
                <th className="num">слов в пуле</th><th className="num">d</th>
              </tr>
            </thead>
            <tbody>
              {busiest.map(({ c, i }) => (
                <tr key={c.k}>
                  <td className="mono small">{c.l}</td>
                  <td className="small muted">{c.th}</td>
                  <td className="num">{c.ref_levels}</td>
                  <td className="num muted">{c.ref_first_level}</td>
                  <td className="num">{index.approvedCount(i)}</td>
                  <td className="num muted">{c.d ?? '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  );
}

function Stat({ v, k, note }: { v: number | undefined; k: string; note?: string }) {
  return (
    <div className="stat">
      <div className="v">{v ?? '—'}</div>
      <div className="k">{k}</div>
      {note && <div className="note">{note}</div>}
    </div>
  );
}
