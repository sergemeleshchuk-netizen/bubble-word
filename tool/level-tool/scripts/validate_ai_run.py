#!/usr/bin/env python3
"""Проверка схемы сырого вывода AI-прохода перед импортом в базу.

Модель не имеет права писать в базу напрямую. Между её ответом и SQLite стоит
этот фильтр: он проверяет структуру, ссылочную целостность и — главное для
мета-связей — что слово, объявленное именем категории, действительно совпадает
с именем существующей категории после нормализации.

Битая строка не останавливает прогон: она уходит в rejected.jsonl с причиной.

Запуск:
    python3 scripts/validate_ai_run.py data/runs/run-001-meta-hubs

Вывод в той же папке:
    categories.jsonl    готово к import-categories
    memberships.jsonl   готово к import-memberships
    rejected.jsonl      что не прошло и почему
    schema_report.md    человекочитаемая сводка
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "pipeline" / "database" / "content.sqlite"

RELATION_TYPES = {
    "is_a", "part_of", "found_in", "used_for", "used_in", "has_property",
    "associated_with", "member_of_set", "wordplay", "does_action",
}
THEMES_ALLOWED = None  # заполняется из базы

APOSTROPHES = dict.fromkeys(map(ord, "‘’ʼ′"), "'")
DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(APOSTROPHES).translate(DASHES)
    return re.sub(r"\s+", " ", s.strip().casefold())


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


def load_db_state() -> dict:
    conn = connect_readonly(DB)
    conn.row_factory = sqlite3.Row
    cats = {r["category_key"]: dict(r) for r in conn.execute(
        "select category_key, label, theme from categories")}
    label_to_key = {}
    for key, c in cats.items():
        label_to_key.setdefault(normalize(c["label"]), key)
    themes = {r[0] for r in conn.execute("select distinct theme from categories")}
    approved_counts = dict(conn.execute(
        "select c.category_key, count(*) from categories c "
        "join memberships m on m.category_id = c.id and m.review_status='approved' "
        "group by c.category_key").fetchall())
    conn.close()
    return {"categories": cats, "label_to_key": label_to_key,
            "themes": themes, "approved": approved_counts}


def validate(run_dir: Path) -> int:
    raw_path = run_dir / "raw.jsonl"
    if not raw_path.exists():
        print(f"ОШИБКА: нет {raw_path}", file=sys.stderr)
        return 1

    db = load_db_state()
    new_categories, new_memberships, rejected = [], [], []
    declared_keys = set()
    problems = Counter()

    # слой ручных исправлений: raw.jsonl не редактируется никогда.
    # Флаг --no-fixes прогоняет проверку БЕЗ правок: так фиксируется, что именно
    # модель сделала неправильно. Без этого история ошибок исчезает из отчёта,
    # как только правки применены.
    apply_fixes = "--no-fixes" not in sys.argv
    # Повторный прогон после импорта: категории уже в базе, и это не ошибка.
    # Без флага проверка была бы неидемпотентной и на втором запуске падала бы
    # на собственном результате.
    allow_existing = "--allow-existing" in sys.argv
    fixes_path = run_dir / "human_fixes.json"
    fixes = (json.loads(fixes_path.read_text(encoding="utf-8"))
             if fixes_path.exists() and apply_fixes else {})
    renames = fixes.get("rename_categories", {})
    dropped_cats = set(fixes.get("drop_categories", {}))
    remap = fixes.get("remap_membership_category", {})
    dropped_memb = {(w.casefold(), c) for w, c in fixes.get("drop_memberships", [])}
    fix_stats = Counter()

    lines = raw_path.read_text(encoding="utf-8").splitlines()

    # проход 1: категории (чтобы связи могли на них ссылаться)
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as exc:
            rejected.append({"line": lineno, "reason": f"невалидный JSON: {exc}",
                             "raw": line[:200]})
            problems["json_parse_error"] += 1
            continue
        if rec.get("type") != "category":
            continue

        original_key = rec.get("category_key")
        if original_key in dropped_cats:
            fix_stats["categories_dropped_by_human"] += 1
            continue
        if original_key in renames:
            patch = renames[original_key]
            rec = dict(rec)
            rec["category_key"] = patch.get("category_key", original_key)
            if patch.get("label"):
                rec["label"] = patch["label"]
            fix_stats["categories_renamed_by_human"] += 1

        errs = []
        for field in ("category_key", "label", "rule", "relation_type", "theme"):
            if not rec.get(field):
                errs.append(f"нет поля {field}")
        key = rec.get("category_key", "")
        if key in db["categories"] and not allow_existing:
            errs.append(f"category_key '{key}' уже существует в базе")
        if key in declared_keys:
            errs.append(f"category_key '{key}' объявлен дважды в прогоне")
        if rec.get("relation_type") not in RELATION_TYPES:
            errs.append(f"неизвестный relation_type '{rec.get('relation_type')}'")
        if rec.get("theme") not in db["themes"]:
            errs.append(f"тема '{rec.get('theme')}' отсутствует в базе")
        label_norm = normalize(rec.get("label", ""))
        if label_norm in db["label_to_key"] and not (
                allow_existing and db["label_to_key"][label_norm] == key):
            errs.append(f"имя '{rec['label']}' уже занято категорией "
                        f"'{db['label_to_key'][label_norm]}'")

        if errs:
            rejected.append({"line": lineno, "reason": "; ".join(errs), "record": rec})
            problems["category_rejected"] += 1
            continue
        declared_keys.add(key)
        new_categories.append({k: v for k, v in rec.items() if k != "type"})

    # проход 2: связи
    known_keys = set(db["categories"]) | declared_keys
    all_labels = dict(db["label_to_key"])
    for c in new_categories:
        all_labels.setdefault(normalize(c["label"]), c["category_key"])

    meta_links = []
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue                      # уже отклонено в проходе 1
        if rec.get("type") != "membership":
            continue

        errs = []
        word = rec.get("word") or ""
        cat = remap.get(rec.get("category_key"), rec.get("category_key")) or ""
        if cat != rec.get("category_key"):
            fix_stats["memberships_retargeted_by_human"] += 1
        if (word.casefold(), cat) in dropped_memb:
            fix_stats["memberships_dropped_by_human"] += 1
            continue
        if not word:
            errs.append("нет поля word")
        if cat not in known_keys:
            errs.append(f"категория '{cat}' не существует и не объявлена в прогоне")
        if rec.get("relation_type") not in RELATION_TYPES:
            errs.append(f"неизвестный relation_type '{rec.get('relation_type')}'")
        if not rec.get("reason"):
            errs.append("нет объяснения связи")
        for field in ("fit_score", "obviousness_score"):
            value = rec.get(field)
            if not isinstance(value, (int, float)) or not 0.0 <= value <= 1.0:
                errs.append(f"{field} вне диапазона 0..1: {value!r}")

        # главная проверка прохода: мета-слово обязано быть именем категории
        claimed_meta = bool(rec.get("is_meta_label"))
        target_key = all_labels.get(normalize(word))
        if claimed_meta and target_key is None:
            errs.append(f"is_meta_label=true, но '{word}' не является именем "
                        f"ни одной категории — мета-связь не возникнет")
        if claimed_meta and target_key == cat:
            errs.append(f"категория '{cat}' была бы собственным родителем")
        if claimed_meta and target_key and db["approved"].get(target_key, 0) < 4:
            errs.append(f"категория '{target_key}' имеет "
                        f"{db['approved'].get(target_key, 0)} approved-слов, "
                        f"меньше четырёх — как мета-ребёнок не годится")

        if errs:
            rejected.append({"line": lineno, "reason": "; ".join(errs), "record": rec})
            problems["membership_rejected"] += 1
            continue

        out = {
            "word": word,
            "language": "en",
            "part_of_speech": "noun",
            "is_proper_noun": False,
            "category_key": cat,
            "relation_type": rec["relation_type"],
            "reason": rec["reason"],
            "fit_score": rec["fit_score"],
            "obviousness_score": rec["obviousness_score"],
            "source": "ai_meta_hubs_v1",
            "review_status": "candidate",      # AI никогда не ставит approved сам
        }
        new_memberships.append(out)
        if claimed_meta:
            meta_links.append({"child": target_key, "parent": cat, "word": word})

    # цикл в мета-графе внутри прогона
    parents = defaultdict(set)
    for link in meta_links:
        parents[link["child"]].add(link["parent"])
    cycles = []
    for start in parents:
        stack, seen = [(start, [start])], set()
        while stack:
            node, path = stack.pop()
            for p in parents.get(node, ()):
                if p in path:
                    cycles.append(path + [p])
                elif p not in seen:
                    seen.add(p)
                    stack.append((p, path + [p]))

    (run_dir / "categories.jsonl").write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in new_categories),
        encoding="utf-8")
    (run_dir / "memberships.jsonl").write_text(
        "".join(json.dumps(m, ensure_ascii=False) + "\n" for m in new_memberships),
        encoding="utf-8")
    (run_dir / "rejected.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rejected),
        encoding="utf-8")

    report = [
        "# Проверка схемы прогона\n",
        f"Прогон: `{run_dir.name}`\n",
        f"- строк на входе: {len([l for l in lines if l.strip()])}",
        f"- категорий принято: **{len(new_categories)}**",
        f"- связей принято: **{len(new_memberships)}**",
        f"- из них мета-связей: **{len(meta_links)}**",
        f"- отклонено: **{len(rejected)}**",
        f"- циклов в мета-графе прогона: {len(cycles)}",
        "",
    ]
    if fix_stats:
        report.append("## Слой ручных исправлений\n")
        report.append("`raw.jsonl` не редактируется. Правки описаны в `human_fixes.json`:\n")
        for k, v in sorted(fix_stats.items()):
            report.append(f"- {k}: {v}")
        report.append("")
    if rejected:
        report.append("## Отклонённые записи\n")
        for r in rejected:
            what = r.get("record", {}).get("word") or r.get("record", {}).get("label") or "?"
            report.append(f"- строка {r['line']}, `{what}`: {r['reason']}")
        report.append("")
    if meta_links:
        report.append("## Мета-связи, которые появятся в базе\n")
        report.append("| Ребёнок (категория) | Идёт словом в | Слово |")
        report.append("|---|---|---|")
        for link in sorted(meta_links, key=lambda x: (x["parent"], x["child"])):
            report.append(f"| `{link['child']}` | `{link['parent']}` | {link['word']} |")
    (run_dir / "schema_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"категорий принято: {len(new_categories)}")
    print(f"связей принято:    {len(new_memberships)} (мета: {len(meta_links)})")
    print(f"отклонено:         {len(rejected)}")
    if cycles:
        print(f"ЦИКЛЫ: {cycles}")
    for k, v in problems.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/runs/run-001-meta-hubs"
    sys.exit(validate(target if target.is_absolute() else ROOT / target))
