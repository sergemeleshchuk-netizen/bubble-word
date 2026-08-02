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
 * Поэтому статических уровней у прототипа больше нет: в списке только то,
 * что отдал генератор, плюс встроенный демо-контент.
 *
 * Формат намеренно НЕ тот, что в игровом экспорте. Прототипу нужны имя
 * категории и четыре слова строками (`applyLevel` в `site/playable/index.html`),
 * мета-пузыри он определяет сам: слово, равное имени другой категории уровня,
 * становится мета-словом. Оценки и провенанс сюда не едут.
 *
 * А вот доска едет, и лимит ходов в ней — обязательно. Пока его тут не было,
 * прототип видел уровень без лимита и включал ∞: давление ходов — половина
 * механики (GDD §2 п.9), и наигровка руками проверяла не тот уровень, который
 * сдан. Считает лимит генератор, прототип его только исполняет.
 */
import type { BlockResult, GeneratedLevel } from './types.ts';
import { TOOL_VERSION } from './version.ts';

/**
 * Ключ хранилища. Читается сайтом (`site/index.html`) и прототипом
 * (`site/playable/index.html`) — при изменении править во всех трёх местах,
 * поэтому в имени есть версия формата.
 */
export const HANDOFF_KEY = 'bubble-level-tool.generated-pack.v1';

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

function levelTitle(level: GeneratedLevel): string {
  const categories = level.spec.categories.length;
  return `Уровень ${level.spec.levelId} · ${categories} кат · `
    + `D ${level.difficulty.value} · I ${level.interest.value}`;
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
      },
    })),
  };
}

/**
 * Кладёт пакет в хранилище. Возвращает false, если хранилище недоступно
 * (приватный режим, отключённые cookies) — молчать об этом нельзя, иначе
 * человек пойдёт в прототип и не найдёт там своих уровней.
 */
export function publishToPlayable(block: BlockResult): HandoffPack | null {
  const pack = buildHandoffPack(block);
  try {
    window.localStorage.setItem(HANDOFF_KEY, JSON.stringify(pack));
    return pack;
  } catch {
    return null;
  }
}
