/**
 * Передача собранного пакета в играбельный прототип.
 *
 * Прототип живёт отдельным пунктом сайта (`/playable/`), инструмент — соседним
 * (`/tool/`). Это один origin, поэтому передавать пакет можно через
 * `localStorage`: без сервера, без файлов и без ручного копирования JSON.
 *
 * Почему не «скачать и подложить файл»: скачанный файл пришлось бы класть
 * рядом с прототипом, прописывать в списке и деплоить сайт. Между «собрал
 * уровень» и «сыграл в него» оказывался деплой — на этом проверка идей и
 * умирает. Здесь путь короткий: собрал → отдал в прототип → сыграл.
 * Поэтому статических уровней у прототипа больше нет: в списке только то, что
 * отдал генератор, и выложенные пакеты. Своего контента у прототипа тоже нет —
 * зашитое демо убрано 03.08: любой сбой загрузки молча подменял им настоящий
 * уровень, и проверяющий играл не в то, что проверял. Прототип без уровня
 * честно говорит «играть нечего» (`noLevel` в site/playable/index.html).
 *
 * Формат намеренно НЕ тот, что в игровом экспорте. Прототипу нужны имя
 * категории и четыре слова строками (`applyLevel` в `site/playable/index.html`),
 * мета-пузыри он определяет сам: слово, равное имени другой категории уровня,
 * становится мета-словом. Оценки и провенанс сюда не едут.
 *
 * А вот доска едет, и лимит ходов в ней — обязательно. Пока его тут не было,
 * прототип видел уровень без лимита и включал ∞: давление ходов — половина
 * механики (GDD §2 п.10), и наигровка руками проверяла не тот уровень, который
 * сдан. Считает лимит генератор, прототип его только исполняет.
 */
import type { BlockResult, GeneratedLevel } from './types.ts';
import { difficultyTier } from './scoringDifficulty.ts';
import { TOOL_VERSION } from './version.ts';

/**
 * Ключей два, и путать их нельзя — на этой путанице пакеты и терялись.
 *
 * `HANDOFF_KEY` — «что прототип играет прямо сейчас»: ОДИН массив уровней,
 * прототип адресует его как `?gen=N`, где N — индекс в массиве. Слот рабочий:
 * его законно перезаписывает и инструмент (собрал — сыграл сразу), и страница
 * отчёта (склеивает выложенные пакеты с собранными, чтобы список уровней был
 * один). Ничего долговечного в нём хранить нельзя.
 *
 * `HANDOFF_LIST_KEY` — архив собранных пакетов, и вот он растёт. Раньше архива
 * не было вовсе: инструмент писал пакет в рабочий слот, страница отчёта клала
 * туда же свою склейку — и собранный пакет исчезал на первой же перезагрузке,
 * даже если больше ничего не собирали. Второй прогон генератора затирал первый
 * по той же причине. Сравнить «до» и «после» правки было нечем.
 *
 * Оба читаются обычным HTML сайта, который tsc не проверяет, поэтому строки
 * продублированы в `site/index.html` и `site/playable/index.html`; при смене
 * править везде. Версия формата — в имени ключа.
 */
export const HANDOFF_KEY = 'bubble-level-tool.generated-pack.v1';
export const HANDOFF_LIST_KEY = 'bubble-level-tool.generated-packs.v1';

/**
 * Сигнал странице отчёта: пакет только что уехал в хранилище.
 *
 * Инструмент и прототип — два соседних iframe одной страницы, и список уровней
 * прототипа собирается при раскрытии его пункта. Если оба пункта уже открыты,
 * список к моменту сборки давно построен: человек жал «Добавить в Playable»,
 * шёл в прототип и своих уровней там не видел, пока не свернёт и не развернёт
 * пункт обратно. Сообщение закрывает эту дыру — страница пересобирает список и
 * перезагружает прототип сама.
 *
 * Через `postMessage`, а не через событие `storage`: то не приходит вкладке,
 * которая сама писала в хранилище, а тут это одна и та же вкладка.
 *
 * Строка продублирована в `site/index.html` (обычный HTML, tsc его не видит);
 * при смене править в обоих местах — это закреплено тестом `playable_handoff`.
 */
export const HANDOFF_MESSAGE = 'bubble-level-tool:handoff';

/**
 * Сколько собранных пакетов держим. Пакет весит 25-55 КБ, лимит браузера на
 * origin — около 5 МБ, так что упереться в него архивом трудно; ограничение
 * тут не ради места, а чтобы список групп в прототипе оставался читаемым.
 * Вытесняется всегда самый старый.
 */
export const HANDOFF_MAX_PACKS = 5;

export interface HandoffLevel {
  level_id: number;
  /** подпись в выпадающем списке прототипа */
  title: string;
  categories: { id: string; name: string; words: string[] }[];
  /**
   * Вместимость поля: сколько пузырей видно одновременно. Прототип раньше брал
   * своё число 19, инструмент считал по 24 (замер целевой игры) — и поле в
   * проверке было разреженнее, чем в уровне, который мы сдаём.
   */
  board: {
    board_capacity: number;
    start_bubbles: number;
    /**
     * Лимит ходов уровня, `ceil((3*M + chunks) * K)`. `null` — только туториал:
     * в референсе L1 без лимита, игрока там учат одному драгу. Прототип не имеет
     * права додумывать это `null` в бесконечность сам — безлимит он включает
     * только своим конфигом (`UNLIMITED` в `site/playable/index.html`).
     */
    move_limit: number | null;
    /** K из формулы — чтобы в прототипе было видно, насколько тесен проход. */
    move_limit_k: number | null;
  };
  /**
   * Первая выкладка: состав поля и очередь досыпки, посчитанные генератором.
   * Прототип обязан исполнить её как есть — своей случайности у него больше нет,
   * иначе наигровка руками проверяет не тот уровень, который сдан.
   * `category` — это `id` категории из списка выше.
   */
  deal: {
    start: { word: string; category: string }[];
    queue: { word: string; category: string }[];
    /**
     * Очередь линий: категории, которые не выходят на поле, пока игрок не собрал
     * `after_collected` других (core/deal.ts, `planGates`). Прототип обязан их
     * ИСПОЛНЯТЬ: досыпка берёт из очереди первый пузырь ОТКРЫТОЙ линии, а
     * закрытую пропускает. Без этого пакет с гейтами играется не так, как его
     * проверял симулятор: линия выходила бы на поле сразу, и крупный уровень
     * снова встречал бы игрока обрывками всех категорий разом.
     *
     * Поля нет = гейтов у уровня нет (так собраны все пакеты до 04.08).
     */
    gates?: { category: string; after_collected: number }[];
  };
  /**
   * Слова, приходящие кусочками: пузырь не один, а два, и склейка тратит ход.
   *
   * Поле необязательное и по умолчанию пустое. Появилось, чтобы воспроизвести
   * запись уровня 12 оригинала: там распилено ровно восемь слов и ровно в тех
   * местах, что видно на видео (`dol|phin`, `choco|late`, `au|gust`). Прототип
   * умел пилить сам по `?mod=halves`, но выбирал слова и точку распила своей
   * эвристикой — то есть показывал похожий уровень, а не записанный.
   *
   * Правило то же, что у выкладки: если распил задан пакетом, прототип его
   * ИСПОЛНЯЕТ и своей эвристики не применяет. Лимит ходов в таком пакете уже
   * учитывает склейки (`3*M + chunks`), добавлять ничего не нужно.
   */
  chunks?: { word: string; category: string; pieces: [string, string] }[];
  /**
   * Мета-пузыри, которые рисуются картинкой вместо слова (см. core/metaIcons.ts).
   *
   * Отдельным списком, а не полем внутри `categories`, ровно по одной причине:
   * слова уезжают в прототип строками (`words: string[]`), и прототип зовёт
   * `w.toUpperCase()`. Превратить слово в объект значило бы сломать формат
   * целиком ради четверти мета-пузырей. Здесь же прототип читает список и
   * подставляет значок при отрисовке; слово остаётся словом — по нему он и
   * находит мета-связь, сравнивая с именами категорий уровня.
   */
  icons?: { word: string; icon: string }[];
  /**
   * Игровой модификатор уровня, если генератор его назначил. Половинки сюда
   * не входят — они едут полем `chunks` выше. Прототип модификатор ИСПОЛНЯЕТ:
   * замораживает/закрывает ровно указанные слова и ставит цепь с указанным
   * счётчиком, а свою эвристику `?mod=` при этом не применяет. Лимит ходов
   * пакета бонус за блокиратор уже содержит — прототип ничего не добавляет.
   */
  modifier?: {
    type: 'ice' | 'hidden' | 'chain';
    frozen?: { word: string; category: string; layers: number }[];
    hidden?: { word: string; category: string; layers: number }[];
    chain_need?: number;
  };
}

export interface HandoffPack {
  /** имя группы в списке: версия инструмента и хеш пакета */
  label: string;
  tool_version: string;
  pack_hash: string;
  content_snapshot_hash: string;
  level_range: [number, number];
  levels: HandoffLevel[];
}

const MODIFIER_TAG: Record<string, string> = {
  halves: 'половинки', ice: 'лёд', hidden: '«?»', chain_line: 'цепь',
};

function specModifier(level: GeneratedLevel): string | null {
  if (level.spec.halves.length > 0) return 'halves';
  if (level.spec.modifiers.frozenBubbles.length > 0) return 'ice';
  if (level.spec.modifiers.hiddenBubbles.length > 0) return 'hidden';
  if (level.spec.modifiers.chainLine) return 'chain_line';
  return null;
}

function levelTitle(level: GeneratedLevel): string {
  const categories = level.spec.categories.length;
  const mod = specModifier(level);
  return `Уровень ${level.spec.levelId} · ${categories} кат · `
    + `D ${level.difficulty.value} ${difficultyTier(level.difficulty.value)} · `
    + `I ${level.interest.value}`
    + (mod ? ` · ${MODIFIER_TAG[mod]}` : '');
}

/** Собирает пакет в том виде, в котором его понимает прототип. */
export function buildHandoffPack(block: BlockResult): HandoffPack {
  return {
    label: `v${TOOL_VERSION} · ${block.packHash.slice(0, 12)}`,
    tool_version: TOOL_VERSION,
    pack_hash: block.packHash,
    content_snapshot_hash: block.contentSnapshotHash,
    level_range: block.config.levelRange,
    levels: block.levels.map((level) => ({
      level_id: level.spec.levelId,
      title: levelTitle(level),
      categories: level.spec.categories.map((category) => ({
        id: category.key,
        name: category.label,
        // строками: мета-пузырь несёт имя дочерней категории, и прототип
        // распознаёт его сам, сравнивая слово с именами категорий уровня
        words: category.words.map((word) => word.text),
      })),
      board: {
        board_capacity: level.spec.board.boardCapacity,
        start_bubbles: level.spec.board.startBubbles,
        move_limit: level.spec.board.moveLimit,
        move_limit_k: level.spec.board.moveLimitK,
      },
      deal: {
        start: level.spec.deal.start.map((b) => ({ word: b.word, category: b.category })),
        queue: level.spec.deal.queue.map((b) => ({ word: b.word, category: b.category })),
        // пустого списка не пишем: уровень без гейтов уезжает в прототип таким же,
        // каким уезжал до них
        gates: (level.spec.deal.gates ?? []).length === 0 ? undefined
          : level.spec.deal.gates!.map((g) => ({
            category: g.category, after_collected: g.afterCollected,
          })),
      },
      chunks: level.spec.halves.length === 0 ? undefined
        : level.spec.halves.map((h) => ({
          word: h.word, category: h.home, pieces: h.fragments,
        })),
      icons: handoffIcons(level),
      modifier: handoffModifier(level),
    })),
  };
}

/** Картинки мета-пузырей уровня; пустого списка не пишем — уровень без них прежний. */
function handoffIcons(level: GeneratedLevel): HandoffLevel['icons'] {
  const icons = level.spec.categories.flatMap((c) => c.words
    .filter((w) => w.kind === 'meta' && w.icon)
    .map((w) => ({ word: w.text, icon: w.icon! })));
  return icons.length === 0 ? undefined : icons;
}

/** Модификатор уровня в формате прототипа; половинки едут полем chunks. */
function handoffModifier(level: GeneratedLevel): HandoffLevel['modifier'] {
  const m = level.spec.modifiers;
  if (m.frozenBubbles.length > 0) {
    return { type: 'ice', frozen: m.frozenBubbles.map((b) => ({ ...b })) };
  }
  if (m.hiddenBubbles.length > 0) {
    return { type: 'hidden', hidden: m.hiddenBubbles.map((b) => ({ ...b })) };
  }
  if (m.chainLine) return { type: 'chain', chain_need: m.chainLine.need };
  return undefined;
}

/**
 * Архив собранных пакетов, свежий первым. Битое содержимое — не повод падать:
 * лучше показать пустой архив, чем сломать страницу целиком.
 */
export function readHandoffPacks(): HandoffPack[] {
  try {
    const raw = window.localStorage.getItem(HANDOFF_LIST_KEY);
    const list = raw ? JSON.parse(raw) : null;
    return Array.isArray(list) ? list.filter((p) => p && Array.isArray(p.levels)) : [];
  } catch {
    return [];
  }
}

/**
 * Добавляет пакет в архив, вытесняя самый старый, пока не влезет.
 *
 * Квота браузера — единственная причина, по которой запись может не пройти, и
 * реагировать на неё «ничего не сохранилось» неправильно: свежий пакет нужнее
 * старых. Поэтому при отказе жертвуем хвостом архива и пробуем снова, а
 * сдаёмся только когда не влезает даже он один.
 */
function writeHandoffPacks(list: HandoffPack[]): boolean {
  const packs = list.slice(0, HANDOFF_MAX_PACKS);
  while (packs.length > 0) {
    try {
      window.localStorage.setItem(HANDOFF_LIST_KEY, JSON.stringify(packs));
      return true;
    } catch {
      packs.pop();
    }
  }
  return false;
}

/**
 * Кладёт пакет в хранилище. Возвращает null, если хранилище недоступно
 * (приватный режим, отключённые cookies) — молчать об этом нельзя, иначе
 * человек пойдёт в прототип и не найдёт там своих уровней.
 *
 * Пишется в оба ключа, и это не дублирование, а разные роли: в рабочий слот —
 * чтобы прототип, открытый прямо сейчас, играл именно этот пакет; в архив —
 * чтобы он пережил и следующую сборку, и склейку от страницы отчёта.
 *
 * Пересборка того же конфига даёт тот же `pack_hash`: такой пакет не плодит
 * второй записи, а поднимается наверх архива как свежий.
 */
export function publishToPlayable(block: BlockResult): HandoffPack | null {
  const pack = buildHandoffPack(block);
  try {
    const kept = readHandoffPacks().filter((p) => p.pack_hash !== pack.pack_hash);
    writeHandoffPacks([pack, ...kept]);
    window.localStorage.setItem(HANDOFF_KEY, JSON.stringify(pack));
    notifyHost(pack);
    return pack;
  } catch {
    return null;
  }
}

/**
 * Говорит странице-хосту, что пакет в хранилище и прототип пора обновить.
 *
 * Молча ничего не делает, когда инструмент открыт сам по себе (`/tool/` без
 * обёртки) или когда хост на другом origin: обновлять там нечего, и падать
 * из-за этого публикация пакета не должна — она уже состоялась.
 */
function notifyHost(pack: HandoffPack): void {
  try {
    if (window.parent === window) return;
    window.parent.postMessage({
      type: HANDOFF_MESSAGE,
      pack_hash: pack.pack_hash,
      label: pack.label,
      levels: pack.levels.length,
    }, window.location.origin);
  } catch {
    /* хост недоступен — пакет от этого не пострадал */
  }
}
