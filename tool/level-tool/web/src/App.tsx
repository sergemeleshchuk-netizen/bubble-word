import { useEffect, useMemo, useState } from 'react';
import type { BlockConfig, BlockResult, Snapshot } from './core/types.ts';
import { STARTING_BLOCK_CONFIG, buildBlockPlan } from './core/blockPlan.ts';
import {
  generateBlock, redealLevel, toGameJson, toPipelineJson, withLevel,
} from './core/generateBlock.ts';
import { ContentIndex } from './core/snapshot.ts';
import { DEFAULT_SOURCE_ID, sourceById, type SourceId } from './core/sources.ts';
import type { ScoringConfig } from './core/scoringDifficulty.ts';
import { TOOL_VERSION } from './core/version.ts';
import { Composer, RunView } from './components/Composer.tsx';
import { LevelInspector } from './components/LevelInspector.tsx';
import { ContentBase } from './components/ContentBase.tsx';
import { ExportView } from './components/ExportView.tsx';
import { PlayableStep } from './components/PlayableStep.tsx';
import { ReferencePicker } from './components/ReferencePicker.tsx';
import {
  REFERENCE_ORIGIN, buildReferenceBlock, type BwjLevels, type ReferenceBlock,
} from './core/referenceLevels.ts';
import { DecadeTable } from './components/DealTuning.tsx';
import {
  applyDecadeTuning, decadeTuningDefaults, type DecadeTuningRow,
} from './core/decadeProfiles.ts';
import { BOARD_CAPACITY } from './core/levelMath.ts';

import snapshotJson from './data/content.snapshot.json';
import scoringJson from './data/scoring.config.json';

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
  const module = await import('./data/reference.snapshot.json');
  return module.default as unknown as Snapshot;
}

/** Снимок, с которым инструмент рисует первый кадр, пока едет рабочий словарь. */
const BOOT_SOURCE_ID: SourceId = 'production';

/** Выгрузка уровней оригинала: 1 МБ, нужна только источнику «База-реф-BWJ». */
async function loadReferenceLevels(): Promise<BwjLevels> {
  const module = await import('./data/bwj-levels.json');
  return module.default as unknown as BwjLevels;
}

/**
 * Ручная настройка раздачи старта переживает перезагрузку страницы: это
 * настройка инструмента, а не одного блока. Ключ версионирован — смена формата
 * не должна ронять чтение старого значения.
 */
const DECADE_TUNING_KEY = 'level-tool.decade-tuning.v4';

function loadDecadeTuning(): DecadeTuningRow[] {
  const defaults = decadeTuningDefaults();
  const saneScheme = (s: unknown): boolean => s === null || (Array.isArray(s)
    && s.every((n) => Number.isInteger(n) && n >= 1 && n <= 4));
  try {
    const raw = localStorage.getItem(DECADE_TUNING_KEY);
    if (!raw) return defaults;
    const parsed = JSON.parse(raw) as DecadeTuningRow[];
    if (!Array.isArray(parsed) || parsed.length === 0) return defaults;
    const sane = parsed.every((r) => Number.isInteger(r.from) && r.from >= 1
      && Number.isInteger(r.to) && r.to >= r.from
      && Array.isArray(r.corridor) && r.corridor.length === 2
      && Number.isInteger(r.corridor[0]) && Number.isInteger(r.corridor[1])
      && r.corridor[0] >= 3 && r.corridor[1] <= 18 && r.corridor[0] <= r.corridor[1]
      && Array.isArray(r.startBubbles) && r.startBubbles.length === 2
      && Number.isInteger(r.startBubbles[0]) && Number.isInteger(r.startBubbles[1])
      && r.startBubbles[0] >= 4 && r.startBubbles[1] <= BOARD_CAPACITY
      && r.startBubbles[0] <= r.startBubbles[1]
      && saneScheme(r.schemeMin) && saneScheme(r.schemeMax));
    return sane ? parsed : defaults;
  } catch {
    return defaults;
  }
}

const TABS = [
  { id: 'base', label: 'База контента' },
  { id: 'compose', label: 'Настройка блока' },
  { id: 'run', label: 'Генерация' },
  { id: 'level', label: 'Уровень' },
  { id: 'play', label: 'Прототип' },
  { id: 'export', label: 'Экспорт' },
] as const;

/**
 * Закладки источника «База-реф-BWJ».
 *
 * «Настройки блока» и «Генерации» здесь нет, и это не упрощение интерфейса, а
 * следствие: на этом источнике собирать нечего — состав уровня задан выгрузкой.
 * Оставить те экраны значило бы предложить крутить ручки, которые ни на что не
 * влияют, и показать кнопку «Собрать блок» там, где блок не собирается.
 */
const REFERENCE_TABS = [
  { id: 'base', label: 'База контента' },
  { id: 'compose', label: 'Выбор уровней' },
  { id: 'level', label: 'Уровень' },
  { id: 'play', label: 'Прототип' },
  { id: 'export', label: 'Экспорт' },
] as const;

type TabId = typeof TABS[number]['id'];

export function App() {
  const [tab, setTab] = useState<TabId>('base');
  const [config, setConfig] = useState<BlockConfig>(STARTING_BLOCK_CONFIG);
  const [block, setBlock] = useState<BlockResult | null>(null);
  const [selectedLevel, setSelectedLevel] = useState<number | null>(null);
  const [elapsed, setElapsed] = useState<number>(0);
  const [decadeTuning, setDecadeTuning] = useState<DecadeTuningRow[]>(loadDecadeTuning);

  /**
   * Применение конфига декад: сохранить и НЕМЕДЛЕННО переписать конфиг блока.
   *
   * Раньше здесь было только сохранение, а таблица доезжала до конфига лишь в
   * момент следующей сборки. Практическое следствие: на шаге «Настройка блока»
   * стоял коридор, которого в конфиге декад уже нет, и понять, какое из двух
   * чисел действует, было нельзя.
   *
   * `presetLocked` здесь снимается сознательно. Закрепление сдаваемого пакета
   * защищает автоматический путь (`generate`), чтобы таблица не переписала хеш
   * пакета молча. Но человек, нажавший «Сохранить и применить», просит ровно
   * этого — и отказать ему значило бы показать кнопку, которая на пресете
   * ничего не делает.
   */
  const applyDecadeTuningConfig = (next: DecadeTuningRow[]) => {
    setDecadeTuning(next);
    try {
      localStorage.setItem(DECADE_TUNING_KEY, JSON.stringify(next));
    } catch { /* приватный режим: настройка живёт до перезагрузки */ }
    setConfig((prev) => applyDecadeTuning({ ...prev, presetLocked: undefined }, next));
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

  /**
   * Режим реф-базы. Выгрузка уровней грузится один раз при первом заходе на
   * источник и остаётся в памяти: переключение туда-обратно не должно каждый
   * раз тянуть мегабайт.
   */
  const isReference = source.id === 'reference';
  const [bwj, setBwj] = useState<BwjLevels | null>(null);
  const [refProvenance, setRefProvenance] =
    useState<ReferenceBlock['provenance']>({});

  useEffect(() => {
    if (!isReference || bwj !== null) return undefined;
    let cancelled = false;
    loadReferenceLevels()
      .then((loaded) => { if (!cancelled) setBwj(loaded); })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoadError(error instanceof Error ? error.message : String(error));
        }
      });
    return () => { cancelled = true; };
  }, [isReference, bwj]);

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
    if (tab !== 'base' && tab !== 'compose') setTab('base');
  };

  /**
   * Собирает блок по переданному конфигу и одновременно делает его применённым.
   *
   * Конфиг приходит параметром, а не берётся из состояния, потому что кнопка на
   * экране настройки отдаёт черновик формы: `setConfig` асинхронный, и генерация
   * по состоянию собрала бы блок по предыдущему конфигу — на один клик позади.
   */
  const generate = (raw: BlockConfig = config) => {
    // Таблица декад применяется В МОМЕНТ сборки: черновик конфига мог быть
    // собран до правки таблицы. Пресет инструмента она не переписывает — у
    // сдаваемого пакета своя форма кривой (`presetLocked` в core/types.ts).
    const next = raw.presetLocked ? raw : applyDecadeTuning(raw, decadeTuning);
    setConfig(next);
    const started = performance.now();
    const result = generateBlock({ snapshot, config: next, scoring });
    setElapsed(Math.round(performance.now() - started));
    setBlock(result);
    setSelectedLevel(result.levels[0]?.spec.levelId ?? null);
    setTab('run');
  };

  /**
   * Собрать выбранные уровни оригинала. Результат кладётся в то же состояние
   * `block`, что и наш собранный блок: дальше уровень идёт теми же экранами —
   * «Уровень», «Экспорт», «Добавить в Playable», — и дублировать их не нужно.
   */
  const buildReference = (ids: number[]) => {
    if (!bwj) return;
    const started = performance.now();
    const built = buildReferenceBlock(index, bwj, ids, scoring);
    setElapsed(Math.round(performance.now() - started));
    setRefProvenance(built.provenance);
    setBlock({
      // конфиг здесь — не настройка сборки, а расписка о происхождении: уровни
      // не собирались ни этим конфигом, ни вообще генератором
      config: { ...STARTING_BLOCK_CONFIG, levelRange: [ids[0], ids[ids.length - 1]],
        seed: REFERENCE_ORIGIN },
      contentSnapshotHash: snapshot.content_snapshot_hash,
      generatorVersion: REFERENCE_ORIGIN,
      levels: built.levels,
      failures: [],
      packHash: built.packHash,
    });
    setSelectedLevel(built.levels[0]?.spec.levelId ?? null);
  };

  const level = block?.levels.find((l) => l.spec.levelId === selectedLevel) ?? null;
  const busy = loadingSource !== null;

  /**
   * Переложить старт выбранного уровня по схеме с экрана «Уровень».
   *
   * Уровень пересчитывается целиком (`redealLevel`), а блок получает новый хеш
   * пакета (`withLevel`): выкладка входит в хеш спека, и оставить прежний
   * packHash значило бы подписать старым именем другой пакет.
   *
   * На реф-базе это не предлагается вовсе: там выкладка взята из записи
   * оригинала, и «поправить» её значило бы наиграть не тот уровень, что записан.
   */
  const redeal = (scheme: number[] | null) => {
    if (!block || !level || isReference) return;
    const next = redealLevel({ snapshot, scoring, block, level, scheme, index });
    setBlock(withLevel(block, next, scoring));
  };

  /**
   * Следующий шаг для кнопки в строке закладок. На последнем экране её нет:
   * кнопка «Дальше», ведущая в никуда, врёт про то, что работа не закончена.
   */
  const tabs: readonly { id: TabId; label: string }[] = isReference
    ? REFERENCE_TABS : TABS;
  // закладка «Генерация» на реф-базе исчезает: если человек стоял на ней,
  // возвращаем на выбор уровней, иначе экран остался бы пустым
  const activeTab: TabId = tabs.some((t) => t.id === tab) ? tab : 'compose';
  const nextTab = tabs[tabs.findIndex((t) => t.id === activeTab) + 1] ?? null;

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

      {loadError && (
        <div className="panel">
          <h2>Источник не загрузился</h2>
          <p className="small" style={{ color: 'var(--fail)' }}>{loadError}</p>
          <p className="hint">
            Инструмент остался на прежнем снимке — собранное этим не затронуто.
          </p>
        </div>
      )}

      {/*
        Закладки и переход к следующему шагу — одна строка. Кнопка стояла под
        содержимым экрана, и до неё приходилось прокручивать таблицу уровней
        целиком: «где я» и «куда дальше» логично держать в одном месте.
      */}
      <nav className="tabs">
        {tabs.map((t, i) => (
          <button
            key={t.id}
            className={activeTab === t.id ? 'active' : ''}
            onClick={() => setTab(t.id)}
          >
            <span className="num">{i + 1}</span>{t.label}
          </button>
        ))}
        {nextTab && (
          <button className="next" onClick={() => setTab(nextTab.id)}>
            Дальше · {nextTab.label} →
          </button>
        )}
      </nav>

      {activeTab === 'base' && (
        <>
          <ContentBase
            snapshot={snapshot}
            source={source}
            requested={requested}
            loading={loadingSource}
            busy={busy}
            onSwitch={switchSource}
          />
          <DecadeTable
            rows={decadeTuning}
            onApply={applyDecadeTuningConfig}
            appliedTo={config.levelRange}
          />
        </>
      )}

      {activeTab === 'compose' && (isReference
        ? (
          <ReferencePicker
            data={bwj}
            block={block}
            busy={busy}
            provenance={refProvenance}
            onBuild={buildReference}
            onSelect={(id) => { setSelectedLevel(id); setTab('level'); }}
          />
        )
        : (
          <Composer
            config={config}
            generated={block !== null}
            onGenerate={generate}
            tuneConfig={(c) => applyDecadeTuning(c, decadeTuning)}
          />
        ))}

      {activeTab === 'run' && (
        <RunView
          block={block}
          plans={plans}
          elapsed={elapsed}
          onGenerate={generate}
          onSelect={(id) => { setSelectedLevel(id); setTab('level'); }}
        />
      )}

      {activeTab === 'level' && (
        level
          ? (
            <LevelInspector
              level={level}
              index={index}
              onSelect={setSelectedLevel}
              levels={block!.levels}
              onRedeal={isReference ? undefined : redeal}
            />
          )
          : <Empty onGenerate={generate} isReference={isReference} onGoPick={() => setTab('compose')} />
      )}

      {activeTab === 'play' && (
        block
          // key по хешу пакета: новая сборка — новая партия, а не старый iframe
          ? <PlayableStep key={block.packHash} block={block} />
          : <Empty onGenerate={generate} isReference={isReference} onGoPick={() => setTab('compose')} />
      )}

      {activeTab === 'export' && (
        block
          ? <ExportView block={block} toGameJson={toGameJson} toPipelineJson={toPipelineJson} />
          : <Empty onGenerate={generate} isReference={isReference} onGoPick={() => setTab('compose')} />
      )}
    </div>
  );
}

function Empty({ onGenerate, isReference, onGoPick }: {
  onGenerate: () => void; isReference: boolean; onGoPick: () => void;
}) {
  // на реф-базе предлагать «собрать блок» нельзя: блок там не собирается,
  // а выбираются готовые уровни оригинала
  if (isReference) {
    return (
      <div className="panel">
        <h2>Уровни ещё не выбраны</h2>
        <p className="hint">
          На источнике «База-реф-BWJ» уровни не собираются, а берутся из
          выгрузки оригинала. Выберите номера — и уровень откроется здесь.
        </p>
        <button className="primary" onClick={onGoPick}>К выбору уровней</button>
      </div>
    );
  }
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
