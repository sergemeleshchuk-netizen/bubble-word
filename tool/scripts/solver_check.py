#!/usr/bin/env python3
"""Сверяет решение слепого решателя с ответами уровня (шаг 4 approach.md).

Вход: <уровень.json> <решение.json>.
Формат решения (его возвращает независимый AI-решатель):
{
  "groups": [ { "category": "Fruits", "words": ["apple", ...], "confidence": 5 } ],
  "hesitations": [ { "word": "orange", "also_fits": "Colors", "why": "..." } ]
}

Правила вердикта (approach.md, столп "Честность"):
- любое расхождение со схемой уровня = FAIL (уровень бракуется);
- ловушка валидна, если решатель положил слово в home;
- hesitations - эмпирика для оценки сложности (шаг 5): ловушка "сработала",
  если слово положено верно, но решатель отметил сомнение.

Выход: отчёт в консоль + levels/solver/<имя>.report.md.
Код возврата: 0 PASS, 1 FAIL, 2 структурная ошибка решения (переспросить решателя).

Запуск: python3 tool/scripts/solver_check.py levels/etalon/e2.json levels/solver/e2.solution.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "levels" / "solver"


def structural_errors(level, solution):
    errors = []
    names = {c["name"] for c in level["categories"]}
    truth_words = {w.lower() for c in level["categories"] for w in c["words"]}

    groups = solution.get("groups")
    if not isinstance(groups, list) or not groups:
        return ["в решении нет списка groups"]

    seen_cats, seen_words = [], []
    for g in groups:
        cat, words = g.get("category"), [w.lower() for w in g.get("words", [])]
        if cat not in names:
            errors.append(f"категория '{cat}' не с этого уровня")
        seen_cats.append(cat)
        if len(words) != 4:
            errors.append(f"'{cat}': {len(words)} слов вместо 4")
        seen_words.extend(words)

    if len(seen_cats) != len(set(seen_cats)):
        errors.append("категория встречается в решении дважды")
    if set(seen_cats) != names:
        missing = names - set(seen_cats)
        if missing:
            errors.append("нет групп для категорий: " + ", ".join(sorted(missing)))
    if len(seen_words) != len(set(seen_words)):
        errors.append("слово встречается в решении дважды")
    extra = set(seen_words) - truth_words
    missing = truth_words - set(seen_words)
    if extra:
        errors.append("лишние слова: " + ", ".join(sorted(extra)))
    if missing:
        errors.append("пропущенные слова: " + ", ".join(sorted(missing)))
    return errors


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    level_path, solution_path = Path(argv[1]).resolve(), Path(argv[2]).resolve()
    level = json.loads(level_path.read_text(encoding="utf-8"))
    solution = json.loads(solution_path.read_text(encoding="utf-8"))

    errors = structural_errors(level, solution)
    if errors:
        print("СТРУКТУРНАЯ ОШИБКА решения (переспросить решателя):")
        for e in errors:
            print(" -", e)
        return 2

    truth = {}   # word -> category name
    id2name = {c["id"]: c["name"] for c in level["categories"]}
    for c in level["categories"]:
        for w in c["words"]:
            truth[w.lower()] = c["name"]

    guessed = {}  # word -> category name
    conf = {}     # category name -> confidence
    for g in solution["groups"]:
        conf[g["category"]] = g.get("confidence")
        for w in g["words"]:
            guessed[w.lower()] = g["category"]

    hesitations = {h["word"].lower(): h for h in solution.get("hesitations", [])}
    mismatches = [(w, truth[w], guessed[w]) for w in sorted(truth)
                  if guessed[w] != truth[w]]

    traps_report = []
    for t in level.get("traps", []):
        w = t["word"].lower()
        home, tempts = id2name.get(t["home"], t["home"]), id2name.get(t["tempts"], t["tempts"])
        ok = guessed.get(w) == home
        noticed = w in hesitations
        traps_report.append((w, home, tempts, ok, noticed))

    total = len(truth)
    correct = total - len(mismatches)
    verdict = "PASS" if not mismatches else "FAIL"

    lines = [
        f"# Solver report: {level_path.name}",
        "",
        f"- Уровень: `{level_path.relative_to(ROOT)}`, категорий {len(level['categories'])}, слов {total}",
        f"- Решение: `{solution_path.relative_to(ROOT)}`",
        f"- Точность: {correct}/{total}",
        f"- **Вердикт: {verdict}**" + ("" if verdict == "PASS" else " (расхождение = брак: чинить уровень генератором)"),
        "",
    ]
    if mismatches:
        lines.append("## Расхождения")
        for w, t_cat, g_cat in mismatches:
            lines.append(f"- `{w}`: дом **{t_cat}**, решатель положил в **{g_cat}**")
        lines.append("")
    if traps_report:
        lines.append("## Ловушки")
        for w, home, tempts, ok, noticed in traps_report:
            status = "валидна" if ok else "НЕ ВАЛИДНА (решатель ушёл в соблазн)"
            felt = "решатель отметил сомнение (ловушка сработала)" if noticed else "сомнения не отмечено"
            lines.append(f"- `{w}` ({home} vs {tempts}): {status}; {felt}")
        lines.append("")
    lines.append("## Эмпирика для оценки сложности (шаг 5)")
    for name in sorted(conf):
        lines.append(f"- {name}: уверенность {conf[name]}")
    if hesitations:
        lines.append("- Сомнения решателя:")
        for w in sorted(hesitations):
            h = hesitations[w]
            lines.append(f"  - `{w}` тянуло в {h.get('also_fits')}: {h.get('why', '')}")
    else:
        lines.append("- Сомнений решатель не отметил.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUT_DIR / (level_path.stem + ".report.md")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    print(f"\nОтчёт: {report_path.relative_to(ROOT)}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
