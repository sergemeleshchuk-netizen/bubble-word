#!/usr/bin/env python3
"""Проход критика + решения человека по кандидатам AI-прохода.

Три слоя, и они не смешиваются:

1. ПОЛИТИКА — механическое правило по двум числам связи. Воспроизводимо,
   применяется ко всем кандидатам одинаково.
2. КРИТИК — модель в роли скептика: ищет причину отклонить, а не одобрить.
   Её вердикт НЕ меняет статус автоматически.
3. ЧЕЛОВЕК — явные переопределения с письменной причиной. Сильнее всего.

Результат — CSV в формате `word-content import-review`, то есть решения попадают
в базу тем же путём, что и любое ручное ревью.

Запуск:  python3 scripts/review_ai_run.py ../word_content_pipeline/data/runs/run-001-meta-hubs
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Каталоги AI-прогонов — источники базы, лежат рядом с ней в каноническом пайплайне,
# а не второй копией в level-tool.
DEFAULT_RUN = ROOT.parent / "word_content_pipeline" / "data" / "runs" / "run-001-meta-hubs"

# --------------------------------------------------------------------------- #
# слой 1: политика по двум числам
# --------------------------------------------------------------------------- #
def policy(fit: float, obv: float) -> tuple:
    """Статус по силе связи и очевидности.

    Смысл разделения: сила отвечает «связь настоящая?», очевидность —
    «игрок увидит её сразу?». Настоящая, но неочевидная связь — это ловушка
    (`alternative`), а не брак. Слабая связь — брак независимо от очевидности.
    """
    if fit < 0.7:
        return "rejected", "связь слишком слабая: игрок не узнает её даже после раскрытия"
    if fit >= 0.85 and obv >= 0.5:
        return "approved", "связь сильная и читаемая: годится как дом слова"
    if obv < 0.32:
        return "hard_only", "связь настоящая, но игрок сам не догадается: только сложные уровни"
    return "alternative", "связь верная, но не первая мысль: материал для ловушки"


# --------------------------------------------------------------------------- #
# слои 2 и 3: вердикты критика и переопределения человека
# --------------------------------------------------------------------------- #
# Формат: (слово, ключ категории) -> (статус, кто решил, причина)
OVERRIDES = {
    ("teas", "cocktails"): (
        "rejected", "критик+человек",
        "Модель обосновала связь названием «Long Island iced tea». Это каламбур, "
        "а не ассоциация: игрок, увидев пузырь TEAS среди коктейлей, будет прав, "
        "решив, что это ошибка. Худший кандидат прогона."),
    ("moons", "planets"): (
        "rejected", "критик+человек",
        "Луна не является планетой. Связь «moons принадлежат planets» верна для "
        "физики, но категория PLANETS означает «планеты», и мета-пузырь MOONS "
        "внутри неё учил бы игрока неверному. Формально высокий fit 0.72 — "
        "пример того, как модель защищает кандидата вместо проверки."),
    ("months", "weather_report"): (
        "rejected", "критик+человек",
        "Обоснование «в прогнозе называют среднемесячные значения» технически "
        "верно, но игрок никогда не сгруппирует MONTHS с forecast и radar. "
        "Очевидность 0.26 — сама модель это признала и всё равно предложила."),
    ("comet", "stargazing"): (
        "alternative", "критик",
        "Слово уже живёт в категории NIGHT SKY. Как дом слова создало бы пару "
        "неразделимых категорий, как ловушка между STARGAZING и NIGHT SKY — "
        "работает честно."),
    ("digits", "bones"): (
        "alternative", "человек",
        "Пальцы действительно кости, но DIGITS среди skull и spine читается "
        "как «цифры». Двусмысленность настоящая, поэтому только ловушка."),
    ("fasteners", "kitchen_drawer"): (
        "hard_only", "критик",
        "«Зажимы и стяжки оказываются в кухонном ящике» — это про конкретную "
        "чужую кухню, а не про общее знание."),
    ("gadgets", "toy_chest"): (
        "hard_only", "критик",
        "Гаджет — не игрушка. Связь есть только через «оказалось в ящике»."),
    ("islands", "travel_abroad"): (
        "hard_only", "критик",
        "Островные страны — частный случай поездки за границу, а не признак её."),
    ("titles", "courtroom"): (
        "hard_only", "критик",
        "Обращения в суде существуют, но TITLES — слишком общее слово, "
        "чтобы игрок связал его именно с судом."),
    ("shapes", "science_fair"): (
        "hard_only", "критик",
        "Геометрия на научной выставке встречается, но связь общая до пустоты."),
    ("weeds", "garden_center"): (
        "hard_only", "критик",
        "Садовый центр продаёт средства ОТ сорняков. Игрок скорее решит, "
        "что это ошибка."),
    ("humidity", "weather_report"): (
        "approved", "человек",
        "Политика дала alternative по очевидности 0.78 против порога силы 0.92 — "
        "но это буквально строка прогноза погоды. Явное повышение."),
}

# Кандидаты, которые критик проверил и подтвердил без изменений, — выборка
# для отчёта: критик не только отклоняет.
CRITIC_CONFIRMED = [
    ("crustaceans", "shellfish", "Ракообразные — моллюски и раки одной витрины; "
     "цепочка crustaceans → shellfish → seafood даёт честную глубину 2."),
    ("songbirds", "birds", "Бесспорная таксономия, высокая узнаваемость."),
    ("gavel", "courtroom", "Канонический предмет: молоток судьи узнают все."),
    ("binoculars", "bird_watching", "Инструмент наблюдателя, очевидность 0.88 оправдана."),
]


def main(run_dir: Path) -> int:
    memb_path = run_dir / "memberships.jsonl"
    if not memb_path.exists():
        print(f"ОШИБКА: нет {memb_path}. Сначала validate_ai_run.py", file=sys.stderr)
        return 1

    rows, verdicts, stats = [], [], Counter()
    by_source = Counter()

    for line in memb_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        key = (rec["word"].casefold(), rec["category_key"])
        status, reason = policy(rec["fit_score"], rec["obviousness_score"])
        decided_by = "политика"

        if key in OVERRIDES:
            status, decided_by, reason = OVERRIDES[key]

        stats[status] += 1
        by_source[decided_by] += 1
        rows.append({
            # normalized + category_key — по ним import-review находит связь
            # независимо от порядка вставки (membership_id нестабилен)
            "word": rec["word"],
            "normalized": rec["word"].strip().lower(),
            "category_key": rec["category_key"],
            "decision": status,
            "review_comment": f"[{decided_by}] {reason}",
        })
        verdicts.append({
            "word": rec["word"],
            "category_key": rec["category_key"],
            "fit_score": rec["fit_score"],
            "obviousness_score": rec["obviousness_score"],
            "decision": status,
            "decided_by": decided_by,
            "reason": reason,
        })

    out_csv = run_dir / "review_decisions.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "word", "normalized", "category_key", "decision", "review_comment"])
        writer.writeheader()
        writer.writerows(rows)

    (run_dir / "review.jsonl").write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in verdicts),
        encoding="utf-8")

    report = ["# Ревью кандидатов прогона\n", f"Прогон: `{run_dir.name}`\n",
              "## Итог по статусам\n"]
    for status in ("approved", "alternative", "hard_only", "rejected"):
        report.append(f"- `{status}`: **{stats[status]}**")
    report.append("\n## Кто решил\n")
    for who, n in by_source.most_common():
        report.append(f"- {who}: {n}")

    report.append("\n## Отклонено и понижено вручную\n")
    report.append("| Слово | Категория | fit | obv | Решение | Кто | Почему |")
    report.append("|---|---|---|---|---|---|---|")
    for v in verdicts:
        if v["decided_by"] == "политика":
            continue
        report.append(f"| {v['word']} | `{v['category_key']}` | {v['fit_score']} | "
                      f"{v['obviousness_score']} | `{v['decision']}` | {v['decided_by']} | "
                      f"{v['reason']} |")

    report.append("\n## Критик подтвердил без изменений (выборка)\n")
    for word, cat, why in CRITIC_CONFIRMED:
        report.append(f"- `{word}` → `{cat}`: {why}")

    (run_dir / "review_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"решений: {len(rows)}")
    for status in ("approved", "alternative", "hard_only", "rejected"):
        print(f"  {status:12s} {stats[status]}")
    print(f"  переопределений вручную: {sum(1 for v in verdicts if v['decided_by'] != 'политика')}")
    # Каталог прогона лежит в пайплайне, то есть ВНЕ level-tool: relative_to(ROOT)
    # на таком пути падает с ValueError. Печатаем путь от корня проекта.
    try:
        shown = out_csv.relative_to(ROOT.parent.parent)
    except ValueError:
        shown = out_csv
    print(f"→ {shown}")
    return 0


if __name__ == "__main__":
    positional = [a for a in sys.argv[1:] if not a.startswith("--")]
    target = Path(positional[0]) if positional else DEFAULT_RUN
    sys.exit(main(target if target.is_absolute() else ROOT / target))
