#!/usr/bin/env python3
"""Экспорт immutable снимка контентной базы для веб-инструмента.

Публичное демо не пишет в production-базу и не зависит от serverless-хранилища:

    word_content_pipeline/database/content.sqlite --(этот скрипт)--> content.snapshot.json
                                                                              |
                                                                      статика в браузере

Снимок компактный (индексы вместо повторяющихся строк) и содержит собственный
sha256: одинаковый снимок + конфиг + seed воспроизводят один и тот же уровень.

Источник — ОДИН, канонический пайплайн `tool/word_content_pipeline`. Здесь раньше
стоял путь на локальную копию `tool/level-tool/pipeline`, и это ровно тот способ
разойтись, которым проект уже разошёлся: копия осталась на состоянии до внешнего
аудита базы, её база опустела, а снимок продолжал жить с довоенными статусами
(approved 9136 против 12598) и без слоёв, которые аудит добавил.

Запуск:  python3 scripts/export_snapshot.py [--db путь]
Вывод:   web/src/data/content.snapshot.json
         data/production/content.snapshot.json  (копия для истории)
         data/production/content.snapshot.sha256
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT.parent / "word_content_pipeline" / "database" / "content.sqlite"
OUT_WEB = ROOT / "web" / "src" / "data" / "content.snapshot.json"
OUT_PROD = ROOT / "data" / "production" / "content.snapshot.json"

ZIPF_MAX = 7.0
TOP50K_ZIPF = 2.55
QUICKWIN_ZIPF = 3.0

# Код регистра слова в снимке. Порядок фиксирован: индекс попадает в снимок.
REGISTER_CODES = {"everyday": 0, "passive": 1, "specialist": 2}

# порядок статусов фиксирован: индекс попадает в снимок, менять нельзя без версии схемы
STATUSES = ["approved", "alternative", "hard_only", "candidate", "rejected"]
# порядок risk-флагов тоже фиксирован: в связи лежит битовая маска по этому списку
RISK_FLAGS = [
    "obscure", "regional", "proper_noun", "multiword", "culturally_specific",
    "weak_relation", "highly_ambiguous", "sensitive", "possible_duplicate",
    "outdated_term", "trademark", "no_familiarity", "needs_sense",
]
CONFLICT_TYPES = ["do_not_pair", "needs_disjoint_words"]
QUARTET_TIERS = ["normal", "hard"]
# 2.0: снимок несёт слои внешнего аудита базы — readiness категорий, запреты
# на сочетание категорий, risk-флаги и игровую сложность связей
SNAPSHOT_SCHEMA_VERSION = "snapshot-2.0"

APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


# --------------------------------------------------------------------------- #
# частотность
# --------------------------------------------------------------------------- #
def connect_readonly(path: Path) -> sqlite3.Connection:
    """Только чтение. База живёт в режиме WAL, и при существующих -wal/-shm
    файлах режим mode=ro открыть её не может — тогда открываем обычным
    соединением и просто ничего не пишем."""
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        conn.execute("select 1 from sqlite_master limit 1")
        return conn
    except sqlite3.OperationalError:
        return sqlite3.connect(str(path))


def zipf_resolver():
    """zipf слова или фразы.

    Для многотокенных пузырей частотность фразы метод-зависима (DATA_AUDIT §5.1:
    расходятся ровно все 137 многотокенных слов). Поэтому узнаваемость фразы
    определяется её самым редким словом — это воспроизводимо и консервативно.
    """
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        print("ОШИБКА: нужен wordfreq (pip install wordfreq)", file=sys.stderr)
        raise

    split_re = re.compile(r"[ \-']+")

    def resolve(text: str):
        norm = normalize(text)
        parts = [p for p in split_re.split(norm) if p]
        if not parts:
            return None, True
        values = [zipf_frequency(p, "en") for p in parts]
        if any(v <= 0 for v in values):
            # хотя бы один токен неизвестен частотнику: frequency_unknown,
            # а не zipf = 0 (SPEC_AUDIT §13)
            return None, True
        whole = zipf_frequency(norm, "en") if len(parts) > 1 else values[0]
        value = min(values) if len(parts) > 1 else whole
        return round(value, 2), False

    return resolve


def lexicon_member(text: str) -> bool:
    """lexicon_membership: ровно эта строка — одиночная лемма нижнего регистра.

    Независим от частотности (SPEC_AUDIT §11): 38 конфликтов в референсе — это
    заглавные, дефисные и брендовые записи, частотные, но не леммы.
    """
    return text == text.lower() and not re.search(r"[ \-'0-9]", text)


# --------------------------------------------------------------------------- #
# сборка снимка
# --------------------------------------------------------------------------- #
def build(conn: sqlite3.Connection) -> dict:
    conn.row_factory = sqlite3.Row
    resolve_zipf = zipf_resolver()

    # `derived_difficulty` появилась позже авторского `base_difficulty`; на базе,
    # где команда derive-category-difficulty ещё не прогонялась, колонки нет.
    have_derived = "derived_difficulty" in {
        row[1] for row in conn.execute("PRAGMA table_info(categories)")}
    derived_select = "derived_difficulty" if have_derived else "NULL as derived_difficulty"
    cats = [dict(r) for r in conn.execute(
        "select id, category_key, label, rule, relation_type, theme, base_difficulty, "
        f"{derived_select}, readiness from categories where status='active' "
        "order by category_key")]
    cat_index = {c["id"]: i for i, c in enumerate(cats)}

    # `everyday_class` появилась шагом 010; на базе, где разметку ещё не
    # прогоняли, колонки нет — тот же приём, что с derived_difficulty выше.
    have_register = "everyday_class" in {
        row[1] for row in conn.execute("PRAGMA table_info(words)")}
    register_select = ("everyday_class" if have_register
                       else "NULL as everyday_class")
    words = [dict(r) for r in conn.execute(
        "select id, text, normalized, part_of_speech, is_proper_noun, familiarity_score, "
        f"{register_select} from words where status='active' order by normalized, id")]
    word_index = {w["id"]: i for i, w in enumerate(words)}

    senses = {}
    for r in conn.execute("select id, word_id, sense_key, definition from word_senses"):
        senses[r["id"]] = {"word": word_index.get(r["word_id"]),
                           "key": r["sense_key"], "def": r["definition"]}
    sense_ids = sorted(senses)
    sense_index = {sid: i for i, sid in enumerate(sense_ids)}

    # слова
    out_words = []
    for w in words:
        z, unknown = resolve_zipf(w["text"])
        out_words.append({
            "t": w["text"],
            "n": w["normalized"],
            "z": z,
            "u": 1 if unknown else 0,                       # frequency_unknown
            "l": 1 if lexicon_member(w["text"]) else 0,     # lexicon_membership
            "p": 1 if w["is_proper_noun"] else 0,
            # Регистр слова: 0 everyday, 1 passive, 2 specialist, null — не размечено.
            # Почему не порог частотности: `congestion` 3.66 отвергнут владельцем
            # продукта, `carrot` 3.62 безупречен, `omelet` 2.63 тоже — никакой
            # порог по zipf эти группы не разделяет (см. миграцию 010).
            "e": REGISTER_CODES.get(w["everyday_class"]),
            "tok": len(re.split(r"[ \-']+", w["normalized"])),
        })

    # связи
    out_memberships = []
    skipped = 0
    skipped_incorrect = 0
    risk_bit = {flag: 1 << i for i, flag in enumerate(RISK_FLAGS)}
    # `graded_obviousness` появилась шагом 009; на базе, где команда
    # grade-obviousness ещё не прогонялась, колонки нет — тот же приём, что и
    # с `derived_difficulty` выше.
    have_graded = "graded_obviousness" in {
        row[1] for row in conn.execute("PRAGMA table_info(memberships)")}
    graded_select = ("graded_obviousness" if have_graded
                     else "NULL as graded_obviousness")
    for r in conn.execute(
        "select word_id, sense_id, category_id, relation_type, review_status, "
        f"fit_score, obviousness_score, {graded_select}, reason, semantic_status, "
        "gameplay_difficulty, risk_flags from memberships"
    ):
        wi, ci = word_index.get(r["word_id"]), cat_index.get(r["category_id"])
        if wi is None or ci is None or r["review_status"] == "rejected":
            skipped += 1
            continue
        # семантически неверная связь в игру не идёт независимо от review_status:
        # это отдельная ось, введённая аудитом, и здесь она обязана резать
        if r["semantic_status"] == "incorrect":
            skipped_incorrect += 1
            continue
        mask = 0
        if r["risk_flags"]:
            try:
                for flag in json.loads(r["risk_flags"]):
                    mask |= risk_bit.get(flag, 0)
            except json.JSONDecodeError:
                pass
        gd = r["gameplay_difficulty"]
        # Очевидность: отранжированное значение важнее исходного.
        #
        # `obviousness_score` сид заполнял по категории, а не по слову: в 74%
        # категорий на весь пул стоит одно число. Отбор слов в генераторе это
        # поле читает, и на плоской категории ему нечего предпочитать. Шаг
        # `grade-obviousness` расслаивает пул и пишет результат отдельной
        # колонкой; исходное значение остаётся на месте как вход источника.
        obv = r["graded_obviousness"]
        if obv is None:
            obv = r["obviousness_score"]
        out_memberships.append([
            wi, ci,
            STATUSES.index(r["review_status"]),
            round(r["fit_score"], 2),
            round(obv, 2),
            r["relation_type"],
            sense_index.get(r["sense_id"]) if r["sense_id"] is not None else None,
            round(gd, 2) if gd is not None else None,
            mask,
        ])

    # мета-потенциал: категория, чьё имя само является словом-пузырём
    by_norm_word = {w["n"]: i for i, w in enumerate(out_words)}
    words_with_home = set()
    for m in out_memberships:
        if m[2] == STATUSES.index("approved"):
            words_with_home.add(m[0])

    meta_capable = []
    for i, c in enumerate(cats):
        wi = by_norm_word.get(normalize(c["label"]))
        if wi is None:
            continue
        hosts = sorted({m[1] for m in out_memberships
                        if m[0] == wi and m[2] <= STATUSES.index("alternative")})
        meta_capable.append({"category": i, "word": wi, "hosts": hosts})

    # запреты на сочетание категорий: слой базы, а не эвристика генератора.
    # Живой фильтр по Жаккару остаётся (он ловит и то, чего в базе нет), но
    # решение «эти две вместе не ставим» принято на стороне контента и приезжает
    # сюда готовым — вместе с причиной и списком общих слов.
    out_conflicts = []
    for r in conn.execute(
        "select category_a_id, category_b_id, conflict_type, severity, overlap_count "
        "from category_conflicts order by category_a_id, category_b_id"
    ):
        ai, bi = cat_index.get(r["category_a_id"]), cat_index.get(r["category_b_id"])
        if ai is None or bi is None:
            continue
        out_conflicts.append([
            ai, bi,
            CONFLICT_TYPES.index(r["conflict_type"]) if r["conflict_type"] in CONFLICT_TYPES else 0,
            r["severity"],
            r["overlap_count"],
        ])

    # проверенные четвёрки: каждая прошла solver единственности на стороне базы
    quartet_rows = {}
    for r in conn.execute(
        "select q.id, q.category_id, q.tier, qw.word_id, qw.slot from quartets q "
        "join quartet_words qw on qw.quartet_id = q.id "
        "where q.validation_state NOT IN ('invalid', 'disabled') "
        "and q.local_check = 'local_unique' "
        "order by q.id, qw.slot"
    ):
        entry = quartet_rows.setdefault(r["id"], {"cat": cat_index.get(r["category_id"]),
                                                 "tier": r["tier"], "words": []})
        wi = word_index.get(r["word_id"])
        entry["words"].append(wi)
    out_quartets = [
        [q["cat"], q["words"], QUARTET_TIERS.index(q["tier"]) if q["tier"] in QUARTET_TIERS else 0]
        for q in quartet_rows.values()
        if q["cat"] is not None and len(q["words"]) == 4 and all(w is not None for w in q["words"])
    ]

    snapshot = {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "statuses": STATUSES,
        "risk_flags": RISK_FLAGS,
        "conflict_types": CONFLICT_TYPES,
        "quartet_tiers": QUARTET_TIERS,
        "constants": {
            "zipf_max": ZIPF_MAX,
            "top50k_zipf": TOP50K_ZIPF,
            "quickwin_zipf": QUICKWIN_ZIPF,
        },
        "categories": [{
            "k": c["category_key"],
            "l": c["label"],
            "r": c["rule"],
            "rel": c["relation_type"],
            "th": c["theme"],
            # `d` — то, чем генератор фильтрует туториал и предпочитает простые
            # категории. С 02.08 это выведенное из пула число, а не авторское:
            # замер показал, что авторское с содержимым категории не связано
            # (корреляция со знакомостью слов −0.25). Авторское остаётся рядом
            # как `d_authored`, чтобы расхождение было видно в снимке.
            "d": c["derived_difficulty"] if c["derived_difficulty"] is not None
                 else c["base_difficulty"],
            "d_authored": c["base_difficulty"],
            "rd": c["readiness"],
        } for c in cats],
        "words": out_words,
        "senses": [senses[sid] for sid in sense_ids],
        "memberships": out_memberships,
        "meta_capable": meta_capable,
        "conflicts": out_conflicts,
        "quartets": out_quartets,
    }

    stats = {
        "categories": len(cats),
        "categories_ready": sum(1 for c in cats if c["readiness"] == "ready"),
        "categories_constrained": sum(1 for c in cats if c["readiness"] == "constrained"),
        "words": len(out_words),
        "senses": len(sense_ids),
        "memberships": len(out_memberships),
        "conflicts": len(out_conflicts),
        "quartets": len(out_quartets),
        "memberships_with_risk": sum(1 for m in out_memberships if m[8]),
        "skipped_rejected": skipped,
        "skipped_semantically_incorrect": skipped_incorrect,
        "approved": sum(1 for m in out_memberships if m[2] == 0),
        "alternative": sum(1 for m in out_memberships if m[2] == 1),
        "hard_only": sum(1 for m in out_memberships if m[2] == 2),
        "frequency_unknown_words": sum(w["u"] for w in out_words),
        "words_below_top50k": sum(
            1 for w in out_words if w["z"] is not None and w["z"] < TOP50K_ZIPF),
        "multi_token_words": sum(1 for w in out_words if w["tok"] > 1),
        "meta_capable_categories": len(meta_capable),
        "meta_capable_with_host": sum(1 for m in meta_capable if m["hosts"]),
        "categories_with_4plus_approved": 0,
        "trap_capable_words": 0,
    }

    approved_per_cat = {}
    cat_per_word = {}
    for m in out_memberships:
        if m[2] == 0:
            approved_per_cat[m[1]] = approved_per_cat.get(m[1], 0) + 1
        if m[2] <= 1:
            cat_per_word.setdefault(m[0], set()).add(m[1])
    stats["categories_with_4plus_approved"] = sum(
        1 for v in approved_per_cat.values() if v >= 4)
    stats["trap_capable_words"] = sum(1 for v in cat_per_word.values() if len(v) >= 2)

    snapshot["stats"] = stats
    return snapshot


def canonical(obj) -> str:
    """Каноническая сериализация: одна форма записи → один хеш."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def resolve_db(explicit: str | None) -> Path | None:
    """Единственная база проекта.

    Запасной путь на копию в БАЗА-СЛОВ убран: база теперь лежит в git, поэтому на
    чистом клоне она есть. Пока её не было, скрипт молча брал копию — и снимок мог
    собраться из файла на другом состоянии, чем рабочая база.
    """
    if explicit:
        path = Path(explicit)
        return path if path.exists() else None
    return DB if DB.exists() else None


# Минимальная версия схемы, в которой есть слои readiness и конфликтов категорий.
# Проверяем «не ниже», а не «ровно»: жёсткое равенство ломало снимок на каждой
# миграции пайплайна, хотя нужные снимку таблицы никуда не девались.
MIN_SCHEMA_VERSION = 2


def check_audited(conn: sqlite3.Connection, path: Path) -> None:
    """База должна быть не старше версии 2: до неё слоёв readiness и конфликтов нет."""
    row = conn.execute(
        "select value from schema_meta where key='schema_version'").fetchone()
    version = int(row[0]) if row and str(row[0]).isdigit() else 0
    if version < MIN_SCHEMA_VERSION:
        raise SystemExit(
            f"ОШИБКА: база {path} не аудированной версии (schema_version="
            f"{row[0] if row else 'нет'}, нужна {MIN_SCHEMA_VERSION} и выше).\n"
            "Пересоберите базу: bash ../word_content_pipeline/scripts/rebuild_all.sh"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", help="путь к базе (по умолчанию канонический пайплайн)")
    args = parser.parse_args()

    db_path = resolve_db(args.db)
    if db_path is None:
        print(f"ОШИБКА: нет базы {args.db or DB}", file=sys.stderr)
        return 1

    conn = connect_readonly(db_path)
    check_audited(conn, db_path)
    print(f"источник: {db_path}")
    snapshot = build(conn)
    conn.close()

    payload = {k: v for k, v in snapshot.items() if k != "stats"}
    digest = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
    snapshot["content_snapshot_hash"] = digest

    body = canonical(snapshot)
    for path in (OUT_WEB, OUT_PROD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    (OUT_PROD.parent / "content.snapshot.sha256").write_text(
        f"{digest}  content.snapshot.json\n", encoding="utf-8")

    s = snapshot["stats"]
    print(f"snapshot {digest[:16]}…  {len(body) / 1024:.0f} KB")
    for k, v in s.items():
        print(f"  {k:32s} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
