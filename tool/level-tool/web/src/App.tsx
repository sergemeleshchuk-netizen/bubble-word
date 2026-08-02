import { useEffect, useMemo, useState } from 'react';
import type { BlockConfig, BlockResult, Snapshot } from './core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from './core/blockPlan.ts';
import { generateBlock, toGameJson, toPipelineJson } from './core/generateBlock.ts';
import { ContentIndex } from './core/snapshot.ts';
import {
  CONTENT_SOURCES, DEFAULT_SOURCE_ID, sourceById, type SourceId,
} from './core/sources.ts';
import type { ScoringConfig } from './core/scoringDifficulty.ts';
import { TOOL_VERSION } from './core/version.ts';
import { Composer, RunView } from './components/Composer.tsx';
import { LevelInspector } from './components/LevelInspector.tsx';
import { ContentBase } from './components/ContentBase.tsx';
import { ExportView } from './components/ExportView.tsx';

import snapshotJson from './data/content.snapshot.json';
import scoringJson from './data/scoring.config.json';
import aiRunsJson from './data/ai_runs.json';

const scoring = scoringJson as unknown as ScoringConfig;
const PRODUCTION_SNAPSHOT = snapshotJson as unknown as Snapshot;

/**
 * Наша база вшита в бандл — с неё инструмент открывается. Словарь оригинала
 * подтягивается отдельным чанком при первом выборе: он весит 4 МБ (565 КБ в
 * gzip), и платить за него должен тот, кто его попросил, а не каждый читатель
 * отчёта. Путь к файлу здесь литеральный сознательно: бандлер выделяет чанк
 * только по литералу, вычисленный путь он разрешить не сможет.
 */
async function loadSnapshot(id: SourceId): Promise<Snapshot> {
  if (id === 'production') return PRODUCTION_SNAPSHOT;
  const module = await import('./data/reference.snapshot.json');
  return module.default as unknown as Snapshot;
}

const TABS = [
  { id: 'base', label: 'База контента' },
  { id: 'compose', label: 'Настройка блока' },
  { id: 'run', label: 'Генерация' },
  { id: 'level', label: 'Уровень' },
  { id: 'export', label: 'Экспорт' },
] as const;

type TabId = typeof TABS[number]['id'];

export function App() {
  const [tab, setTab] = useState<TabId>('base');
  const [config, setConfig] = useState<BlockConfig>(DEFAULT_BLOCK_CONFIG);
  const [block, setBlock] = useState<BlockResult | null>(null);
  const [selectedLevel, setSelectedLevel] = useState<number | null>(null);
  const [elapsed, setElapsed] = useState<number>(0);

  /**
   * Источник контента. Запрошенный и действующий — разные состояния, и это
   * не педантизм: словарь оригинала весит 4 МБ и приезжает отдельным чанком.
   * Пока он в пути, на экранах обязан оставаться прежний снимок вместе со
   * своим описанием — иначе полсекунды инструмент показывает статистику одной
   * базы под именем другой.
   */
  const [requested, setRequested] = useState<SourceId>(DEFAULT_SOURCE_ID);
  const [active, setActive] = useState<{ id: SourceId; snapshot: Snapshot }>(
    { id: DEFAULT_SOURCE_ID, snapshot: PRODUCTION_SNAPSHOT });
  const [loadError, setLoadError] = useState<string | null>(null);
  const snapshot = active.snapshot;
  const source = sourceById(active.id);
  const loadingSource = requested === active.id ? null : requested;

  useEffect(() => {
    if (requested === active.id) return undefined;
    let cancelled = false;
    setLoadError(null);
    loadSnapshot(requested)
      .then((loaded) => {
        if (!cancelled) setActive({ id: requested, snapshot: loaded });
      })
      .catch((error: unknown) => {
        if (cancelled) return;
        setRequested(active.id);
        setLoadError(error instanceof Error ? error.message : String(error));
      });
    return () => { cancelled = true; };
  }, [requested, active.id]);

  const index = useMemo(() => new ContentIndex(snapshot), [snapshot]);
  // план применённого конфига нужен экрану генерации; экран настройки считает
  // свой собственный по черновику формы
  const plans = useMemo(() => buildBlockPlan(config), [config]);

  /**
   * Смена источника обнуляет собранный блок, и это не удобство, а требование.
   * Хеш снимка входит в хеш уровня: блок, собранный на одном словаре, на другом
   * не воспроизводится. Оставить его на экране значило бы показывать пакет
   * рядом с источником, из которого он не получается.
   */
  const switchSource = (next: SourceId) => {
    if (next === requested) return;
    setRequested(next);
    setBlock(null);
    setSelectedLevel(null);
    if (tab === 'level' || tab === 'export' || tab === 'run') setTab('base');
  };

  /**
   * Собирает блок по переданному конфигу и одновременно делает его применённым.
   *
   * Конфиг приходит параметром, а не берётся из состояния, потому что кнопка на
   * экране настройки отдаёт черновик формы: `setConfig` асинхронный, и генерация
   * по состоянию собрала бы блок по предыдущему конфигу — на один клик позади.
   */
  const generate = (next: BlockConfig = config) => {
    setConfig(next);
    const started = performance.now();
    const result = generateBlock({ snapshot, config: next, scoring });
    setElapsed(Math.round(performance.now() - started));
    setBlock(result);
    setSelectedLevel(result.levels[0]?.spec.levelId ?? null);
    setTab('run');
  };

  const level = block?.levels.find((l) => l.spec.levelId === selectedLevel) ?? null;
  const busy = loadingSource !== null;

  return (
    <div className="app">
      <header className="top">
        <div>
          <h1>Генератор уровней · word-association паззл</h1>
          <div className="sub">
            AI обогащает базу · детерминированный алгоритм собирает уровни ·
            валидатор доказывает корректность
          </div>
        </div>
        <div className="sub mono">
          v{TOOL_VERSION} ·
          снимок {snapshot.content_snapshot_hash.slice(0, 12)}… ·
          скоринг {scoring.scoring_version}
          {block && <> · пакет {block.packHash.slice(0, 12)}…</>}
        </div>
      </header>

      <div className="sources">
        <span className="lbl">источник контента</span>
        {CONTENT_SOURCES.map((s) => (
          <button
            key={s.id}
            className={`ghost ${requested === s.id ? 'on' : ''}`}
            disabled={busy}
            onClick={() => switchSource(s.id)}
          >
            {s.label}
            {loadingSource === s.id && ' · грузится…'}
          </button>
        ))}
        <span className="muted small">{source.origin}</span>
      </div>

      {loadError && (
        <div className="panel">
          <h2>Источник не загрузился</h2>
          <p className="small" style={{ color: 'var(--fail)' }}>{loadError}</p>
          <p className="hint">
            Инструмент остался на прежнем снимке — собранное этим не затронуто.
          </p>
        </div>
      )}

      <nav className="tabs">
        {TABS.map((t, i) => (
          <button
            key={t.id}
            className={tab === t.id ? 'active' : ''}
            onClick={() => setTab(t.id)}
          >
            <span className="num">{i + 1}</span>{t.label}
          </button>
        ))}
      </nav>

      {tab === 'base' && (
        <ContentBase
          snapshot={snapshot}
          index={index}
          runs={aiRunsJson as never}
          source={source}
        />
      )}

      {tab === 'compose' && (
        <Composer config={config} onGenerate={generate} />
      )}

      {tab === 'run' && (
        <RunView
          block={block}
          plans={plans}
          elapsed={elapsed}
          onGenerate={generate}
          onSelect={(id) => { setSelectedLevel(id); setTab('level'); }}
        />
      )}

      {tab === 'level' && (
        level
          ? (
            <LevelInspector
              level={level}
              block={block!}
              index={index}
              scoring={scoring}
              onSelect={setSelectedLevel}
              levels={block!.levels}
            />
          )
          : <Empty onGenerate={generate} />
      )}

      {tab === 'export' && (
        block
          ? <ExportView block={block} toGameJson={toGameJson} toPipelineJson={toPipelineJson} />
          : <Empty onGenerate={generate} />
      )}
    </div>
  );
}

function Empty({ onGenerate }: { onGenerate: () => void }) {
  return (
    <div className="panel">
      <h2>Блок ещё не собран</h2>
      <p className="hint">
        Генерация идёт целиком в браузере на замороженном снимке базы: без сервера,
        без API-ключа и без сети. Занимает десятки миллисекунд.
      </p>
      <button className="primary" onClick={onGenerate}>Собрать блок 201–210</button>
    </div>
  );
}
