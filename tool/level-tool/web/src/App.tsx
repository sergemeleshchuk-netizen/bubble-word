import { useMemo, useState } from 'react';
import type { BlockConfig, BlockResult } from './core/types.ts';
import { DEFAULT_BLOCK_CONFIG, buildBlockPlan } from './core/blockPlan.ts';
import { generateBlock, toGameJson, toPipelineJson } from './core/generateBlock.ts';
import { ContentIndex } from './core/snapshot.ts';
import type { ScoringConfig } from './core/scoringDifficulty.ts';
import { TOOL_VERSION } from './core/version.ts';
import { Composer, RunView } from './components/Composer.tsx';
import { LevelInspector } from './components/LevelInspector.tsx';
import { ContentBase } from './components/ContentBase.tsx';
import { ExportView } from './components/ExportView.tsx';

import snapshotJson from './data/content.snapshot.json';
import scoringJson from './data/scoring.config.json';
import aiRunsJson from './data/ai_runs.json';

const snapshot = snapshotJson as unknown as import('./core/types.ts').Snapshot;
const scoring = scoringJson as unknown as ScoringConfig;

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

  const index = useMemo(() => new ContentIndex(snapshot), []);
  // план применённого конфига нужен экрану генерации; экран настройки считает
  // свой собственный по черновику формы
  const plans = useMemo(() => buildBlockPlan(config), [config]);

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

      {tab === 'base' && <ContentBase snapshot={snapshot} index={index} runs={aiRunsJson as never} />}

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
