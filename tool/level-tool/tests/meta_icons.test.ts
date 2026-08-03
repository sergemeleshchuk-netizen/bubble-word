/**
 * Картинка вместо слова на мета-пузыре (core/metaIcons.ts).
 *
 * Проверяется не «красиво ли получилось», а три вещи, которые ломаются молча:
 *
 *   1. правило количества — четверть мета-пузырей, округление к ближайшему;
 *   2. инвариант «картинка — слой отображения»: слово пузыря остаётся словом и
 *      по-прежнему совпадает с именем дочерней категории. Стоит подменить текст
 *      значком — прототип перестанет находить мета-связь, а решатель и оценки
 *      начнут считать другой уровень;
 *   3. картинки доезжают до обоих потребителей: игрового JSON (помеченными, а
 *      не подменёнными) и прототипа (отдельным списком, потому что слова уезжают
 *      туда строками).
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import type { Snapshot } from '../web/src/core/types.ts';
import type { ScoringConfig } from '../web/src/core/scoringDifficulty.ts';
import { DEFAULT_BLOCK_CONFIG } from '../web/src/core/blockPlan.ts';
import { generateBlock, toGameJson } from '../web/src/core/generateBlock.ts';
import { buildHandoffPack } from '../web/src/core/playableHandoff.ts';
import {
  META_ICONS, META_ICON_SHARE, metaIconFor, metaIconTarget, pickMetaIcons,
} from '../web/src/core/metaIcons.ts';
import { validateLevel } from '../web/src/core/validator.ts';
import { ContentIndex } from '../web/src/core/snapshot.ts';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const snapshot = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8')) as Snapshot;
const scoring = JSON.parse(
  readFileSync(join(ROOT, 'web/src/data/scoring.config.json'), 'utf8')) as ScoringConfig;

const block = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });

/** Мета-пузыри уровня в порядке уровня. */
function metaWords(level: typeof block.levels[number]) {
  return level.spec.categories.flatMap((c) => c.words.filter((w) => w.kind === 'meta'));
}

// --------------------------------------------------------------------------- //
// правило количества
// --------------------------------------------------------------------------- //

test('правило — четверть мета-пузырей, округление к ближайшему', () => {
  assert.equal(META_ICON_SHARE, 0.25);
  assert.equal(metaIconTarget(0), 0);
  assert.equal(metaIconTarget(1), 0);
  assert.equal(metaIconTarget(2), 1);   // вниз округлять нельзя: иначе на 1-3
  assert.equal(metaIconTarget(3), 1);   // мета-парах картинок не было бы вовсе
  assert.equal(metaIconTarget(4), 1);   // пример из постановки задачи
  assert.equal(metaIconTarget(6), 2);
  assert.equal(metaIconTarget(8), 2);
});

test('картинок на уровне не больше цели, и меньше — только из-за словаря', () => {
  for (const level of block.levels) {
    const metas = metaWords(level);
    const withIcon = metas.filter((w) => w.icon);
    const target = metaIconTarget(metas.length);
    assert.ok(withIcon.length <= target,
      `уровень ${level.spec.levelId}: картинок ${withIcon.length} при цели ${target}`);
    if (withIcon.length === target) continue;
    // недобор законен ровно тогда, когда простых имён в уровне не хватило
    const eligible = metas.filter((w) => metaIconFor(w.text) !== null);
    assert.ok(eligible.length <= withIcon.length,
      `уровень ${level.spec.levelId}: простые имена были (${eligible.map((w) => w.text)}), `
      + `а картинок ${withIcon.length} из ${target}`);
  }
});

test('на пресете 201-210 картинки реально появляются', () => {
  const total = block.levels.reduce(
    (n, l) => n + metaWords(l).filter((w) => w.icon).length, 0);
  assert.ok(total >= 4,
    `картинок на пакете ${total} — правило не работает или словарь не покрывает базу`);
});

test('на рабочем словаре игры словарь картинок покрывает заметную часть имён', () => {
  /*
   * Замер, а не вкус. Рабочий источник инструмента — словарь игры, и мета-имена
   * там другие: не множественное число категорий (`fruits`), а конкретные
   * существительные (`water`, `clock`, `door`). Первая версия словаря была
   * собрана только по аудированной базе — на блоке из словаря игры картинка
   * выпадала на одном уровне из десяти, и правило «четверть мета-пузырей» на
   * практике не работало.
   *
   * Порог низкий сознательно: словарь и не должен покрывать всё. Он ловит
   * обратное — что покрытие не сползло к нулю после чистки словаря.
   */
  const lexicon = JSON.parse(readFileSync(
    join(ROOT, 'web/src/data/lexicon.snapshot.json'), 'utf8')) as Snapshot;
  const names = lexicon.meta_capable.map((m) => lexicon.words[m.word].t);
  const covered = names.filter((n) => metaIconFor(n) !== null);
  const share = covered.length / names.length;
  assert.ok(share >= 0.05,
    `покрыто ${covered.length} из ${names.length} мета-имён (${(share * 100).toFixed(1)}%)`);
});

test('выбор детерминированный: пересборка того же конфига даёт те же картинки', () => {
  const again = generateBlock({ snapshot, scoring, config: DEFAULT_BLOCK_CONFIG });
  assert.deepEqual(
    again.levels.map((l) => metaWords(l).map((w) => `${w.text}:${w.icon ?? '-'}`)),
    block.levels.map((l) => metaWords(l).map((w) => `${w.text}:${w.icon ?? '-'}`)));
});

test('вес не зависит от порядка вызовов: pickMetaIcons чистая функция', () => {
  const words = ['fish', 'candy', 'minerals', 'planets'];
  const weight = (key: string) => key.length / 100;
  assert.deepEqual([...pickMetaIcons(words, weight)], [...pickMetaIcons(words, weight)]);
});

// --------------------------------------------------------------------------- //
// словарь
// --------------------------------------------------------------------------- //

test('в словаре только осмысленные записи: непустая эмодзи, ключ в нижнем регистре', () => {
  for (const [name, icon] of Object.entries(META_ICONS)) {
    assert.equal(name, name.toLowerCase(), `ключ «${name}» не в нижнем регистре`);
    assert.ok(icon.length > 0 && icon.length <= 6, `значок «${icon}» у «${name}» подозрителен`);
    assert.ok(!/[a-zA-Zа-яА-Я0-9]/.test(icon), `значок «${icon}» содержит текст`);
  }
});

test('имя ищется без учёта регистра: в базе есть «Easter» при ключе «easter»', () => {
  assert.equal(metaIconFor('Easter'), META_ICONS.easter);
  assert.equal(metaIconFor('ICE CREAM'), META_ICONS['ice cream']);
  assert.equal(metaIconFor('minerals'), null);
});

test('одна эмодзи на уровень: дубликат в словаре не даёт двух одинаковых значков', () => {
  // словарь может содержать похожие пары (fish / aquarium), но ОДНА эмодзи
  // дважды на поле — это два пузыря, которые игрок прочитает как один
  const collide = Object.entries(META_ICONS)
    .filter(([, icon]) => icon === META_ICONS.fish).map(([name]) => name);
  assert.deepEqual(collide, ['fish'], 'эмодзи рыбы занята больше чем одним именем');

  const chosen = pickMetaIcons(['fish', 'fish'], () => 0.5);
  assert.equal(chosen.size, 1);
});

// --------------------------------------------------------------------------- //
// инвариант: картинка не подменяет слово
// --------------------------------------------------------------------------- //

test('картинка стоит только на мета-пузыре и не трогает его слово', () => {
  for (const level of block.levels) {
    for (const category of level.spec.categories) {
      for (const word of category.words) {
        if (!word.icon) continue;
        assert.equal(word.kind, 'meta',
          `${category.key}: картинка у обычного слова ${word.text}`);
        assert.ok(word.text.length > 0, 'текст мета-пузыря подменён картинкой');
        assert.equal(metaIconFor(word.text), word.icon,
          `${word.text}: значок не из словаря`);
        const child = level.spec.categories.find((c) => c.key === word.metaChild);
        assert.ok(child, `нет дочерней категории ${word.metaChild}`);
        assert.equal(word.text.toUpperCase(), child!.label.toUpperCase(),
          'мета-пузырь с картинкой обязан по-прежнему совпадать с именем категории');
      }
    }
  }
});

test('пузырь с картинкой не попадает в выкладку — мета-слова не спавнятся', () => {
  for (const level of block.levels) {
    const icons = new Set(metaWords(level).filter((w) => w.icon).map((w) => w.text));
    for (const bubble of [...level.spec.deal.start, ...level.spec.deal.queue]) {
      assert.ok(!icons.has(bubble.word),
        `уровень ${level.spec.levelId}: мета-слово ${bubble.word} оказалось в выкладке`);
    }
  }
});

test('валидатор бракует картинку у обычного слова', () => {
  const index = new ContentIndex(snapshot);
  const level = block.levels[0];
  const broken = structuredClone(level.spec);
  const plain = broken.categories.flatMap((c) => c.words).find((w) => w.kind === 'word')!;
  plain.icon = '🐟';
  const result = validateLevel(broken, { index });
  const issue = result.issues.find((i) => i.code === 'META_ICONS_VALID');
  assert.ok(issue, 'проверка META_ICONS_VALID не сработала');
  assert.equal(issue!.severity, 'hard');
});

test('валидатор бракует значок не из словаря', () => {
  const index = new ContentIndex(snapshot);
  const level = block.levels.find((l) => metaWords(l).some((w) => w.icon))!;
  const broken = structuredClone(level.spec);
  const meta = broken.categories.flatMap((c) => c.words).find((w) => w.icon)!;
  meta.icon = '🧿';
  const result = validateLevel(broken, { index });
  assert.ok(result.issues.some((i) => i.code === 'META_ICONS_VALID'));
});

// --------------------------------------------------------------------------- //
// потребители: игровой JSON и прототип
// --------------------------------------------------------------------------- //

test('в игровом JSON пузырь помечен, а не подменён', () => {
  const level = block.levels.find((l) => metaWords(l).some((w) => w.icon))!;
  const json = toGameJson(level.spec) as {
    categories: { words: { text: string; kind: string; display?: string; icon?: string }[] }[];
  };
  const withIcon = json.categories.flatMap((c) => c.words).filter((w) => w.icon);
  assert.ok(withIcon.length > 0, 'картинки не доехали до игрового JSON');
  for (const word of withIcon) {
    assert.equal(word.kind, 'meta');
    assert.equal(word.display, 'icon');
    assert.ok(word.text.length > 0, 'текст обязан остаться: по нему клиент ищет категорию');
  }
  // у пузырей без картинки поля нет вовсе — уровень без них читается как прежде
  const plain = json.categories.flatMap((c) => c.words).filter((w) => !w.icon);
  assert.ok(plain.every((w) => w.display === undefined));
});

test('прототип получает картинки отдельным списком, слова остаются строками', () => {
  const pack = buildHandoffPack(block);
  let checked = 0;
  for (const generated of block.levels) {
    const handoff = pack.levels.find((l) => l.level_id === generated.spec.levelId)!;
    const expected = metaWords(generated).filter((w) => w.icon);
    if (expected.length === 0) {
      assert.equal(handoff.icons, undefined,
        `уровень ${handoff.level_id}: пустой список картинок вместо отсутствия поля`);
      continue;
    }
    assert.ok(handoff.icons, `уровень ${handoff.level_id}: картинки не доехали до прототипа`);
    assert.deepEqual(handoff.icons!.map((i) => `${i.word} ${i.icon}`),
      expected.map((w) => `${w.text} ${w.icon}`));
    for (const entry of handoff.icons!) {
      // слово из списка обязано лежать среди слов уровня СТРОКОЙ: прототип
      // сравнивает его с именами категорий, чтобы найти мета-связь
      const owner = handoff.categories.find((c) =>
        c.words.some((w) => w.toUpperCase() === entry.word.toUpperCase()));
      assert.ok(owner, `слово ${entry.word} с картинкой не найдено среди слов уровня`);
      checked += 1;
    }
  }
  assert.ok(checked > 0, 'в пакете нет картинок — проверка ничего не проверила');
});

test('прототип читает поле icons и рисует значок вместо слова', () => {
  /*
   * Контракт межпроектный: пишет его TypeScript, читает обычный HTML прототипа,
   * который tsc не проверяет. Если поле переименуют с одной стороны, прототип
   * молча покажет слово — и понять, почему картинок нет, будет нечем.
   */
  const html = readFileSync(resolve(ROOT, '../../site/playable/index.html'), 'utf8');
  assert.match(html, /L\.icons/, 'прототип не читает поле icons пакета');
  assert.match(html, /METAICON\[/, 'прототип не подставляет значок при отрисовке');
});
