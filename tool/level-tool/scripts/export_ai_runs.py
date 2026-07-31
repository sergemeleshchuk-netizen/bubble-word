#!/usr/bin/env python3
"""Сводка AI-прогонов для экрана «База» веб-инструмента.

Риск, который надо закрыть интерфейсом: детерминированная сборка выглядит как
«а где же тут AI». Лечится тем, что на экране видно — сколько связей в базе,
каким промптом и когда сгенерирован каждый блок контента, что критик отклонил
и почему. Эти данные собираются здесь автоматически из папок прогонов,
а не пишутся руками в последний день.

Запуск:  python3 scripts/export_ai_runs.py
Вывод:   web/src/data/ai_runs.json
"""
from __future__ import annotations

import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "data" / "runs"
# Источник ОДИН — канонический пайплайн tool/word_content_pipeline. Здесь стоял
# путь на локальную копию tool/level-tool/pipeline, и это тот же способ разъехаться
# с базой, который уже ловили в export_snapshot.py: копия не обновлялась с момента
# subtree-импорта, а экран «База» показывал бы цифры из неё.
PIPELINE = ROOT.parent / "word_content_pipeline"
DB = PIPELINE / "database" / "content.sqlite"
DB_FALLBACK = ROOT.parent.parent / "БАЗА-СЛОВ" / "база-слов.sqlite"
OUT = ROOT / "web" / "src" / "data" / "ai_runs.json"

PROMPT_LIBRARY = [
    {"id": "meta-hub-v1", "file": "prompts/meta_hub_ideation.md",
     "purpose": "создание категорий-хабов для мета-связей", "used": True},
    {"id": "intent-parser-v1", "file": "prompts/intent_parser.md",
     "purpose": "разбор свободного пожелания в конфиг", "used": True},
    {"id": "blind-solver-v1", "file": "prompts/blind_solver.md",
     "purpose": "слепой семантический аудит уровня, два режима", "used": True},
    {"id": "adversarial-v1", "file": "tool/word_content_pipeline/prompts/adversarial_review.txt",
     "purpose": "критик кандидатов: ищет причину отклонить", "used": True},
    {"id": "expand-category-v1", "file": "tool/word_content_pipeline/prompts/expand_category.txt",
     "purpose": "наполнение категории словами", "used": True},
    {"id": "expand-words-v1", "file": "tool/word_content_pipeline/prompts/expand_words.txt",
     "purpose": "обратный проход: в какие категории годится слово", "used": True},
]


def read_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def collect_run(run_dir: Path) -> dict:
    raw = read_jsonl(run_dir / "raw.jsonl")
    rejected = read_jsonl(run_dir / "rejected.jsonl")
    # что модель сделала неправильно: зафиксировано на первом проходе проверки,
    # до импорта и до правок. Иначе история ошибок исчезает из отчёта, как только
    # правки применены и прогон стал чистым.
    errors_path = run_dir / "model_errors.json"
    model_errors = (json.loads(errors_path.read_text(encoding="utf-8"))
                    if errors_path.exists() else {})
    review = read_jsonl(run_dir / "review.jsonl")
    fixes_path = run_dir / "human_fixes.json"
    fixes = json.loads(fixes_path.read_text(encoding="utf-8")) if fixes_path.exists() else {}

    decisions = Counter(v["decision"] for v in review)
    deciders = Counter(v["decided_by"] for v in review)

    overrides = [v for v in review if v["decided_by"] != "политика"]
    return {
        "run_id": run_dir.name,
        "purpose": "meta_hub_ideation",
        "prompt_id": "meta-hub-v1",
        "prompt_file": "prompts/meta_hub_ideation.md",
        "model": "Claude Opus 5 (сессия Claude Code)",
        "items_received": len(raw),
        "items_rejected_by_schema": len(rejected),
        "totals": model_errors.get("_totals", {}),
        "model_errors": model_errors.get("errors", []),
        "downgraded": model_errors.get("downgraded_not_rejected", []),
        "model_did_well": model_errors.get("what_the_model_did_well", []),
        "schema_rejections": [
            {"line": r.get("line"), "reason": r.get("reason", "")[:220],
             "what": (r.get("record") or {}).get("word")
                     or (r.get("record") or {}).get("label") or "?"}
            for r in rejected
        ],
        "human_fixes": {
            "renamed_categories": list((fixes.get("rename_categories") or {}).keys()),
            "dropped_categories": list((fixes.get("drop_categories") or {}).keys()),
            "retargeted": fixes.get("remap_membership_category") or {},
            "dropped_memberships": len(fixes.get("drop_memberships") or []),
            "reasons": {k: v for k, v in (fixes.get("rename_categories") or {}).items()},
        },
        "decisions": dict(decisions),
        "decided_by": dict(deciders),
        "overrides": [
            {"word": o["word"], "category": o["category_key"],
             "fit": o["fit_score"], "obviousness": o["obviousness_score"],
             "decision": o["decision"], "decided_by": o["decided_by"],
             "reason": o["reason"]}
            for o in overrides
        ],
    }


def db_stats() -> dict:
    db = DB if DB.exists() else DB_FALLBACK
    if not db.exists():
        return {}
    conn = sqlite3.connect(str(db))
    q = lambda sql: conn.execute(sql).fetchone()[0]  # noqa: E731
    stats = {
        "categories": q("select count(*) from categories"),
        "words": q("select count(*) from words"),
        "senses": q("select count(*) from word_senses"),
        "memberships": q("select count(*) from memberships"),
        "themes": q("select count(distinct theme) from categories"),
        "by_status": dict(conn.execute(
            "select review_status, count(*) from memberships group by 1").fetchall()),
        "by_source": dict(conn.execute(
            "select source, count(*) from memberships group by 1").fetchall()),
        "relation_types": dict(conn.execute(
            "select relation_type, count(*) from memberships group by 1 "
            "order by 2 desc limit 12").fetchall()),
        "zipf_buckets": {},
        "multi_category_words": q(
            "select count(*) from (select word_id from memberships "
            "where review_status in ('approved','alternative') "
            "group by word_id having count(distinct category_id) >= 2)"),
    }
    buckets = conn.execute(
        "select case when familiarity_score is null then 'неизвестно' "
        "when familiarity_score*7 < 2.0 then '< 2.0 очень редкие' "
        "when familiarity_score*7 < 3.0 then '2.0-2.9 редкие' "
        "when familiarity_score*7 < 4.0 then '3.0-3.9 нечастые' "
        "when familiarity_score*7 < 5.0 then '4.0-4.9 частые' "
        "else '5.0+ бытовые' end as bucket, count(*) "
        "from words group by 1 order by 1").fetchall()
    stats["zipf_buckets"] = dict(buckets)
    conn.close()
    return stats


def main() -> int:
    runs = [collect_run(d) for d in sorted(RUNS_DIR.iterdir())
            if d.is_dir() and (d / "raw.jsonl").exists()]

    payload = {
        "generated_by": "scripts/export_ai_runs.py",
        "prompt_library": PROMPT_LIBRARY,
        "runs": runs,
        "content_base": db_stats(),
        "where_ai_is_not_used": [
            "сборка уровня из проверенного контента — детерминированный алгоритм",
            "арифметика доски и лимита ходов",
            "проверка ацикличности мета-леса и графа цепей",
            "счёт глобальных решений уровня",
            "правила свежести и проверка novelty",
            "канонический хеш и экспорт",
        ],
        "where_ai_helped": [
            "массовое предложение категорий-хабов для мета-связей",
            "первичная классификация типов связи",
            "обратный проход: в какие категории годится слово",
            "adversarial-ревью кандидатов",
            "разбор пожелания заказчика в структурированный конфиг",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"прогонов: {len(runs)}")
    for run in runs:
        print(f"  {run['run_id']}: получено {run['items_received']}, "
              f"отклонено схемой {run['items_rejected_by_schema']}, "
              f"решений {sum(run['decisions'].values())}, "
              f"переопределений {len(run['overrides'])}")
    print(f"→ {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
