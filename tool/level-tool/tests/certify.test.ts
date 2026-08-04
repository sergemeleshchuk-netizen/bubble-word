/**
 * Сертификатор обязан уметь ОТКАЗЫВАТЬ.
 *
 * Проверка, которая на всех входах говорит PASS, — это не проверка, а украшение
 * отчёта. Поэтому тест не радуется зелёному сдаваемому пакету (это делает сам
 * прогон), а собирает заведомо сломанные уровни и требует по каждому провала
 * ровно той секции, которую сломали:
 *
 *   C1 — мета-ссылка в никуда, одинаковый текст в двух категориях, выкладка
 *        не покрывает уровень;
 *   C2 — уровень из слов, каждое из которых по базе годится в обе категории:
 *        раскладок больше одной, и это обязано быть видно;
 *   C3 — лимит ходов заведомо мал.
 *
 * Плюс отдельно — НЕЗАВИСИМОСТЬ: сертификатор не имеет права импортировать ядро
 * инструмента. Иначе он проверяет генератор его же кодом, а весь смысл был в том,
 * чтобы пройти вторым путём. Это проверяется чтением исходника: никакой тест на
 * поведение такого не заметит, пока копия правил случайно совпадает с оригиналом.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const SCRIPT = join(ROOT, 'scripts/certify_solvability.ts');

// --------------------------------------------------------------------------- //
// стенд: собрать пакет из одного уровня и прогнать через сертификатор
// --------------------------------------------------------------------------- //

interface Word { text: string; kind: string; meta_child?: string }
interface Category { key: string; label: string; words: Word[] }

/** Выкладка по умолчанию: все слова уровня, кроме мета-пузырей, по порядку. */
function dealFor(categories: Category[], capacity: number) {
  const all = categories.flatMap((c) =>
    c.words.filter((w) => w.kind !== 'meta').map((w) => ({ word: w.text, category: c.key })));
  return { start: all.slice(0, capacity), queue: all.slice(capacity) };
}

function runCertifier(
  categories: Category[],
  overrides: { moveLimit?: number; deal?: { start: unknown[]; queue: unknown[] };
    startBubbles?: number } = {},
): { code: number; cert: any; stdout: string } {
  const dir = mkdtempSync(join(tmpdir(), 'cert-'));
  const pack = join(dir, 'pack');
  mkdirSync(pack, { recursive: true });

  const capacity = 24;
  const metaCount = categories.flatMap((c) => c.words).filter((w) => w.kind === 'meta').length;
  const totalWords = categories.reduce((n, c) => n + c.words.length, 0);
  const contract = {
    level_id: 900,
    schema_version: '2.0',
    board: {
      categories_count: categories.length,
      words_per_category: categories[0].words.length,
      start_bubbles: overrides.startBubbles ?? totalWords - metaCount,
      board_capacity: capacity,
      move_limit: overrides.moveLimit ?? 200,
    },
    categories,
    modifiers: { chains: [] },
  };
  const pipeline = {
    level_spec: {
      levelId: 900,
      board: { moveLimit: overrides.moveLimit ?? 200 },
      halves: [],
      deal: overrides.deal ?? dealFor(categories, capacity),
    },
    build_metadata: {
      content_snapshot_hash: 'test', pack_hash: 'test', generator_version: 'test',
    },
    validation: { solution_count: 1 },
  };
  writeFileSync(join(pack, 'game-900.json'), JSON.stringify(contract), 'utf8');
  writeFileSync(join(pack, 'level-900.json'), JSON.stringify(pipeline), 'utf8');

  let code = 0;
  let stdout = '';
  try {
    stdout = execFileSync('node', [
      SCRIPT, '--pack', pack, '--out', join(dir, 'out'), '--report', join(dir, 'report.md'),
    ], { cwd: ROOT, encoding: 'utf8' });
  } catch (e: any) {
    code = e.status ?? 1;
    stdout = String(e.stdout ?? '');
  }
  const cert = JSON.parse(readFileSync(join(dir, 'out', 'level-900.cert.json'), 'utf8'));
  return { code, cert, stdout };
}

/** Слова, которых в базе нет: у них ровно один дом, и уровень заведомо однозначен. */
const invented = (key: string, label: string, texts: string[]): Category => ({
  key, label, words: texts.map((t) => ({ text: t, kind: 'word' })),
});

const cleanLevel = (): Category[] => [
  invented('zzz_alpha', 'ZZZ ALPHA', ['qqzz alpha one', 'qqzz alpha two', 'qqzz alpha three', 'qqzz alpha four']),
  invented('zzz_beta', 'ZZZ BETA', ['qqzz beta one', 'qqzz beta two', 'qqzz beta three', 'qqzz beta four']),
];

// --------------------------------------------------------------------------- //

test('исправный уровень сертифицируется', () => {
  const { code, cert } = runCertifier(cleanLevel());
  assert.equal(code, 0);
  assert.equal(cert.verdict, 'CERTIFIED');
  assert.equal(cert.c2_uniqueness.solutions, 1);
  assert.equal(cert.c3_playthrough.finished, true);
});

test('C1: мета-ссылка в никуда ломает ключ', () => {
  const cats = cleanLevel();
  cats[0].words[0] = { text: 'zzz gamma', kind: 'meta', meta_child: 'zzz_gamma' };
  const { code, cert } = runCertifier(cats);
  assert.equal(code, 1);
  assert.equal(cert.verdict, 'FAILED');
  const check = cert.c1_key.checks.find((c: any) => c.code === 'KEY_META_RESOLVES');
  assert.equal(check.passed, false);
});

test('C1: один и тот же текст в двух категориях ломает ключ', () => {
  const cats = cleanLevel();
  cats[1].words[0] = { text: 'qqzz alpha one', kind: 'word' };
  const { code, cert } = runCertifier(cats);
  assert.equal(code, 1);
  const check = cert.c1_key.checks.find((c: any) => c.code === 'KEY_NO_DUPLICATE_BUBBLE');
  assert.equal(check.passed, false);
});

test('C1: выкладка, потерявшая слово, ломает ключ', () => {
  const cats = cleanLevel();
  const deal = dealFor(cats, 24);
  deal.start = deal.start.slice(1);            // одно слово в партию не попадёт
  const { code, cert } = runCertifier(cats, { deal });
  assert.equal(code, 1);
  const check = cert.c1_key.checks.find((c: any) => c.code === 'KEY_DEAL_COVERS_LEVEL');
  assert.equal(check.passed, false);
});

test('C2: уровень с двумя раскладками не сертифицируется', () => {
  /*
   * Строим двусмысленность не выдумкой, а по базе: ищем пару категорий,
   * у которых есть минимум четыре общих слова. Тогда уровень из двух категорий
   * по два слова, набранный только из общих, раскладывается несколькими
   * способами — и сертификатор обязан это увидеть.
   */
  const snap = JSON.parse(readFileSync(
    join(ROOT, 'web/src/data/content.snapshot.json'), 'utf8'));
  const maxStatus = snap.statuses.indexOf('alternative');
  const byWord = new Map<number, number[]>();
  for (const row of snap.memberships) {
    if (row[2] > maxStatus) continue;
    byWord.set(row[0], [...(byWord.get(row[0]) ?? []), row[1]]);
  }
  const shared = new Map<string, number[]>();
  for (const [word, cats] of byWord) {
    for (let i = 0; i < cats.length; i += 1) {
      for (let j = i + 1; j < cats.length; j += 1) {
        const key = cats[i] < cats[j] ? `${cats[i]}|${cats[j]}` : `${cats[j]}|${cats[i]}`;
        shared.set(key, [...(shared.get(key) ?? []), word]);
      }
    }
  }
  const pair = [...shared.entries()].find(([, words]) => words.length >= 4);
  assert.ok(pair, 'в базе нет пары категорий с четырьмя общими словами — стенд собрать не из чего');
  const [pairKey, words] = pair!;
  const [a, b] = pairKey.split('|').map(Number);
  const texts = words.slice(0, 4).map((w: number) => snap.words[w].t);

  const cats: Category[] = [
    { key: snap.categories[a].k, label: snap.categories[a].l,
      words: texts.slice(0, 2).map((t) => ({ text: t, kind: 'word' })) },
    { key: snap.categories[b].k, label: snap.categories[b].l,
      words: texts.slice(2, 4).map((t) => ({ text: t, kind: 'word' })) },
  ];

  const { code, cert } = runCertifier(cats);
  assert.equal(code, 1);
  assert.equal(cert.verdict, 'FAILED');
  assert.ok(cert.c2_uniqueness.solutions > 1,
    `ожидали больше одной раскладки, получили ${cert.c2_uniqueness.solutions}`);
  assert.ok(cert.c2_uniqueness.secondSolution, 'вторая раскладка обязана быть показана');
});

test('C3: тесного лимита ходов достаточно для отказа', () => {
  const { code, cert } = runCertifier(cleanLevel(), { moveLimit: 2 });
  assert.equal(code, 1);
  assert.equal(cert.verdict, 'FAILED');
  assert.equal(cert.c3_playthrough.finished, false);
  assert.match(cert.c3_playthrough.failReason, /лимита не хватает/);
});

test('C3: партия переигрывается при настоящей ёмкости поля', () => {
  const { cert } = runCertifier(cleanLevel());
  assert.ok(cert.c3_playthrough.peakOnBoard <= cert.c3_playthrough.boardCapacity,
    'на поле не может лежать больше пузырей, чем в него влезает');
});

test('сертификатор независим: ядра инструмента в нём нет', () => {
  const source = readFileSync(SCRIPT, 'utf8');
  const imports = [...source.matchAll(/from\s+'([^']+)'/g)].map((m) => m[1]);
  const fromCore = imports.filter((i) => i.includes('web/src'));
  assert.deepEqual(fromCore, [],
    `сертификатор импортирует ядро инструмента: ${fromCore.join(', ')}`);
});

test('записи ручной игры выписаны на текущий пакет и попали в сертификаты', () => {
  /*
   * Дефект, который тест закрывает: пакет пересобирается, а запись «мы это
   * играли» остаётся от прошлого. Тогда сертификат уверенно показывает ручную
   * проверку, которой для ЭТИХ уровней не было. Поэтому запись действительна
   * только для своего pack_hash, а тест это требует явно.
   */
  const packDir = join(ROOT, 'data/final-pack');
  const pack = JSON.parse(readFileSync(join(packDir, 'pack.json'), 'utf8'));
  const manual = JSON.parse(readFileSync(
    resolve(ROOT, '../../levels/manual-play.json'), 'utf8'));
  const stale = (manual.records ?? []).filter((r: any) => r.pack_hash !== pack.pack_hash);
  assert.deepEqual(stale.map((r: any) => r.level_id), [],
    'записи ручной игры остались от другого пакета — их надо переиграть или удалить');

  const certDir = resolve(ROOT, '../../levels/certificates');
  for (const record of manual.records ?? []) {
    const cert = JSON.parse(readFileSync(
      join(certDir, `level-${record.level_id}.cert.json`), 'utf8'));
    assert.equal(cert.manual_play?.date, record.date,
      `сертификат уровня ${record.level_id} не подхватил запись ручной игры`);
  }
});

test('сдаваемый пакет сертифицирован целиком', () => {
  /*
   * Читаем то, что лежит в репозитории, а не пересчитываем: сертификаты —
   * такой же артефакт сдачи, как сами уровни, и разъехаться с пакетом они не
   * должны молча.
   */
  const dir = resolve(ROOT, '../../levels/certificates');
  const packDir = join(ROOT, 'data/final-pack');
  const pack = JSON.parse(readFileSync(join(packDir, 'pack.json'), 'utf8'));
  const ids = readdirSync(packDir)
    .map((f) => /^game-(\d+)\.json$/.exec(f))
    .filter((m): m is RegExpExecArray => m !== null)
    .map((m) => Number(m[1]));
  assert.ok(ids.length > 0, 'в сдаваемом пакете нет ни одного уровня');
  for (const id of ids) {
    const cert = JSON.parse(readFileSync(join(dir, `level-${id}.cert.json`), 'utf8'));
    assert.equal(cert.verdict, 'CERTIFIED', `уровень ${id} не сертифицирован`);
    assert.equal(cert.pack_hash, pack.pack_hash,
      `сертификат уровня ${id} выписан на другой пакет`);
  }
});
