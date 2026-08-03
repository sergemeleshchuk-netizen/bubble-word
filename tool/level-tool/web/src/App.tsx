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
import { DealTuning } from './components/DealTuning.tsx';
import {
  DEFAULT_DEAL_RANGES, dealMinStartWordsFor, type DealRangeSetting,
} from './core/decadeProfiles.ts';

import snapshotJson from './data/content.snapshot.json';
import scoringJson from './data/scoring.config.json';
import aiRunsJson from './data/ai_runs.json';

const scoring = scoringJson as unknown as ScoringConfig;
const PRODUCTION_SNAPSHOT = snapshotJson as unknown as Snapshot;

/**
 * Что вшито в бандл, а что приезжает чанком.
 *
 * Рабочий источник — словарь игры, но весит он 7,5 МБ, и вшивать его в бандл
 * нельзя: инструмент встроен в отчёт, и такой вес платил бы каждый читатель.
 * Поэтому в бандле лежит авторская разметка (3 МБ) — на ней инструмент
 * открывается за один кадр, — а словарь игры и словарь оригинала подтягиваются
 * отдельными чанками. Словарь игры запрашивается сразу при старте, остальные —
 * по выбору в переключателе.
 *
 * Пути к файлам здесь литеральные сознательно: бандлер выделяет чанк только по
 * литералу, вычисленный путь он разрешить не сможет.
 */
async function loadSnapshot(id: SourceId): Promise<Snapshot> {
  if (id === 'production') return PRODUCTION_SNAPSHOT;
  if (id === 'lexicon') {
    const module = await import('./data/lexicon.snapshot.json');
    return module.default as unknown as Snapshot;
  }
  const module = await import('./data/reference.snapshot.json');
  return module.default as unknown as Snapshot;
}

/** Снимок, с которым инструмент рисует первый кадр, пока едет рабочий словарь. */
const BOOT_SOURCE_ID: SourceId = 'production';

/**
 * Ручная настройка раздачи старта переживает перезагрузку страницы: это
 * настройка инструмента, а не одного блока. Ключ версионирован — смена формата
 * не должна ронять чтение старого значения.
 */
const DEAL_RANGES_KEY = 'level-tool.deal-ranges.v1';

function loadDealRanges(): DealRangeSetting[] {
  try {
    const raw = localStorage.getItem(DEAL_RANGES_KEY);
    if (!raw) return DEFAULT_DEAL_RANGES;
    const parsed = JSON.parse(raw) as DealRangeSetting[];
    if (!Array.isArray(parsed) || parsed.length === 0) return DEFAULT_DEAL_RANGES;
    if (!parsed.every((r) => Number.isInteger(r.from) && r.from >= 1
      && Number.isInteger(r.minStartWords)
      && r.minStartWords >= 1 && r.minStartWords <= 4)) return DEFAULT_DEAL_RANGES;
    return parsed;
  } catch {
    return DEFAULT_DEAL_RANGES;
  }
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
  const [dealRanges, setDealRanges] = useState<DealRangeSetting[]>(loadDealRanges);

  const changeDealRanges = (next: DealRangeSetting[]) => {
    setDealRanges(next);
    try {
      localStorage.setItem(DEAL_RANGES_KEY, JSON.stringify(next));
    } catch { /* приватный режим: настройка живёт до перезагрузки */ }
  };

  /**
   * Источник контента. Запрошенный и действующий — разные состояния, и это
   * не педантизм: рабочий словарь весит 7,5 МБ и приезжает отдельным чанком.
   * Пока он в пути, на экранах обязан оставаться прежний снимок вместе со
   * своим описанием — иначе полсекунды инструмент показывает статистику одной
   * базы под именем другой.
   *
   * Поэтому на первом кадре действующий источник — вшитая авторская разметка,
   * а запрошенный — уже рабочий словарь: тот же эффект ниже, который возит
   * снимки по переключателю, доставляет его при старте.
   */
  const [requested, setRequested] = useState<SourceId>(DEFAULT_SOURCE_ID);
  const [active, setActive] = useState<{ id: SourceId; snapshot: Snapshot }>(
    { id: BOOT_SOURCE_ID, snapshot: PRODUCTION_SNAPSHOT });
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
  const generate = (raw: BlockConfig = config) => {
    // Раздача старта берётся из таблицы промежутков В МОМЕНТ сборки: черновик
    // конфига мог быть собран до правки таблицы. Пресет 201-210 поле не задаёт
    // (undefined) — его не трогаем, хеш сдаваемого пакета закреплён.
    const next = raw.dealMinStartWords === undefined ? raw
      : { ...raw, dealMinStartWords: dealMinStartWordsFor(raw.levelRange[0], dealRanges) };
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

  /**
   * Следующий шаг для кнопки под содержимым. На последнем экране её нет:
   * кнопка «Дальше», ведущая в никуда, врёт про то, что работа не закончена.
   */
  const nextTab = TABS[TABS.findIndex((t) => t.id === tab) + 1] ?? null;

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
        <>
          <ContentBase
            snapshot={snapshot}
            index={index}
            runs={aiRunsJson as never}
            source={source}
          />
          <DealTuning ranges={dealRanges} onChange={changeDealRanges} />
        </>
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

      {nextTab && (
        <div className="step-next">
          <button className="next" onClick={() => setTab(nextTab.id)}>
            Дальше · {nextTab.label} →
          </button>
        </div>
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
      {/* onClick={onGenerate} НЕЛЬЗЯ: React передаёт первым аргументом событие
          клика, оно встаёт на место необязательного конфига, и generateBlock
          получает MouseEvent вместо блока. Типы это пропускают: () => void
          присваивается обработчику события беспрепятственно. */}
      <button className="primary" onClick={() => onGenerate()}>Собрать блок 201–210</button>
    </div>
  );
}
