#!/usr/bin/env python3
"""Экспорт immutable снимка контентной базы для веб-инструмента.

Публичное демо не пишет в production-базу и не зависит от serverless-хранилища:

    pipeline/database/content.sqlite  --(этот скрипт)-->  content.snapshot.json
                                                                  |
                                                          статика в браузере

Снимок компактный (индексы вместо повторяющихся строк) и содержит собственный
sha256: одинаковый снимок + конфиг + seed воспроизводят один и тот же уровень.

Запуск:  python3 scripts/export_snapshot.py
Вывод:   web/src/data/content.snapshot.json
         data/production/content.snapshot.json  (копия для истории)
         data/production/content.snapshot.sha256
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "pipeline" / "database" / "content.sqlite"
OUT_WEB = ROOT / "web" / "src" / "data" / "content.snapshot.json"
OUT_PROD = ROOT / "data" / "production" / "content.snapshot.json"

ZIPF_MAX = 7.0
TOP50K_ZIPF = 2.55
QUICKWIN_ZIPF = 3.0

# порядок статусов фиксирован: индекс попадает в снимок, менять нельзя без версии схемы
STATUSES = ["approved", "alternative", "hard_only", "candidate", "rejected"]
SNAPSHOT_SCHEMA_VERSION = "snapshot-1.0"

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

    cats = [dict(r) for r in conn.execute(
        "select id, category_key, label, rule, relation_type, theme, base_difficulty "
        "from categories where status='active' order by category_key")]
    cat_index = {c["id"]: i for i, c in enumerate(cats)}

    words = [dict(r) for r in conn.execute(
        "select id, text, normalized, part_of_speech, is_proper_noun, familiarity_score "
        "from words where status='active' order by normalized, id")]
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
            "tok": len(re.split(r"[ \-']+", w["normalized"])),
        })

    # связи
    out_memberships = []
    skipped = 0
    for r in conn.execute(
        "select word_id, sense_id, category_id, relation_type, review_status, "
        "fit_score, obviousness_score, reason from memberships"
    ):
        wi, ci = word_index.get(r["word_id"]), cat_index.get(r["category_id"])
        if wi is None or ci is None or r["review_status"] == "rejected":
            skipped += 1
            continue
        out_memberships.append([
            wi, ci,
            STATUSES.index(r["review_status"]),
            round(r["fit_score"], 2),
            round(r["obviousness_score"], 2),
            r["relation_type"],
            sense_index.get(r["sense_id"]) if r["sense_id"] is not None else None,
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

    snapshot = {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "statuses": STATUSES,
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
            "d": c["base_difficulty"],
        } for c in cats],
        "words": out_words,
        "senses": [senses[sid] for sid in sense_ids],
        "memberships": out_memberships,
        "meta_capable": meta_capable,
    }

    stats = {
        "categories": len(cats),
        "words": len(out_words),
        "senses": len(sense_ids),
        "memberships": len(out_memberships),
        "skipped_rejected": skipped,
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


def main() -> int:
    if not DB.exists():
        print(f"ОШИБКА: нет базы {DB}", file=sys.stderr)
        return 1

    conn = connect_readonly(DB)
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
