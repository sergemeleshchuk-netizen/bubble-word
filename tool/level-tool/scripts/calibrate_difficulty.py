#!/usr/bin/env python3
"""Калибровка D_base на 199 референсных уровнях.

Что здесь важно понимать про метод, и это написано в отчёт как есть:

1. Эталона сложности нет. Есть номер уровня — СЛАБЫЙ ordinal proxy дизайнерского
   суждения авторов референса. Модель воспроизводит их прогрессию, а не реальный
   win rate игроков.

2. Веса ограничены по знаку. Без ограничений регрессия даёт отрицательный вес
   мета-плотности — но это эффект двухфазности кривой (после L120 объём растёт,
   а мета падает), а не свойство механики. Утверждать «мета делает уровень легче»
   на этих данных нельзя, поэтому знак фиксируется содержательно.

3. Публикуется блочный holdout: обучение 1-160, проверка 161-199. Результат
   выводится как есть, даже если он плохой — это и есть честная оценка переноса.

4. Признаки считаются ТАК ЖЕ, как в TypeScript (baseFeaturesOf): мета-слова
   не участвуют в счёте редкости, глубина берётся максимальная по лесу.

Запуск:  python3 scripts/calibrate_difficulty.py [--write]
         --write перезаписывает секцию base в web/src/data/scoring.config.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import lsq_linear

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_reference import forest_depth, load, meta_edges, normalize, zipf_lookup  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "web" / "src" / "data" / "scoring.config.json"
REPORT_PATH = ROOT / "docs" / "SCORING.md"

# те же признаки, что в web/src/core/scoringDifficulty.ts
# Откалиброванное ядро: только признаки, чей вклад данные РЕАЛЬНО идентифицируют.
#
# repeat_words (ред. 03.08, d-1.3) — слова, уже встречавшиеся в прошлых уровнях
# в ДРУГОЙ категории. Главный растущий рычаг оригинала после L121: размер уровня
# выходит на плато, а повторы продолжают расти (2.9 → 25 на уровень внутри
# L1-199, r с номером уровня 0.794 — сильнее объёма). Семантика подсчёта ровно
# как в generateBlock.repeatCount: слово знакомо И его последняя категория
# отличается от текущей.
FEATURES = [
    "start_bubbles",
    "rare_words",
    "very_rare_words",
    "repeat_words",
]

# Признаки, которые проверены и НЕ вошли в откалиброванную часть. Каждый разобран
# в отчёте с числами: это главный результат калибровки, а не пропуск.
#
#   meta_links          без ограничений вес отрицателен (эффект смены фаз кривой),
#                       с ограничением знака обнуляется — по референсу не
#                       идентифицируется вообще;
#   meta_depth          глубина 3 не встречается ни разу, глубина 2 — на 25 уровнях;
#   quickwin_categories корреляция с номером уровня ПОЛОЖИТЕЛЬНАЯ (+0.29), то есть
#                       данные не подтверждают, что быстрые победы облегчают уровень.
#
# Их веса объявлены как продуктовые и помечены `declared` — не выдаются за
# откалиброванные ни в JSON, ни в интерфейсе.
DIAGNOSTIC_FEATURES = ["meta_links", "meta_depth", "quickwin_categories"]

# Объявленные продуктовые веса. Основание — не референс, а дизайн-решение,
# и это написано прямо в отчёте.
DECLARED = {
    "meta_link": 0.22,
    "meta_link_max": 1.4,
    "meta_depth_beyond_1": 0.55,
    "quickwin_relief": -0.1,
    "quickwin_relief_max": -0.6,
    # раскладка старта (d-1.2): в выгрузке оригинала выкладки поля нет,
    # калибровать не на чем — вес объявлен, разбор в SCORING §7
    "lone_start_word": 0.05,
    "lone_start_word_max": 0.6,
}

# содержательные ограничения на знак: больше объёма / редкости / глубины
# не может делать уровень легче; больше быстрых побед не может делать тяжелее
SIGN = {
    "start_bubbles": +1,
    "rare_words": +1,
    "very_rare_words": +1,
    "repeat_words": +1,
    "meta_links": +1,
    "quickwin_categories": -1,
}

# референс занимает 1..8, чтобы новым механикам осталось место 8.5..10
D_FLOOR, D_CEILING = 1.0, 8.0


def level_features(cats: list, zipf: dict) -> dict:
    """Признаки одного уровня. Мета-слова исключены из счёта редкости."""
    edges = meta_edges(cats)
    depth, _, _, _ = forest_depth(edges)
    meta_children = {normalize(child) for child, _ in edges}

    rare = very_rare = 0
    quickwins = 0
    for cat in cats:
        norms = [normalize(w) for w in cat["words"]]
        for n in norms:
            if n in meta_children:
                continue                       # это мета-пузырь, а не обычное слово
            z = zipf.get(n)
            if z is not None and z < 3.0:
                rare += 1
            if z is not None and z < 2.0:
                very_rare += 1
        if any(n in meta_children for n in norms):
            continue
        zs = [zipf.get(n) for n in norms]
        if all(z is not None and z >= 3.0 for z in zs):
            quickwins += 1

    return {
        "start_bubbles": len(cats) * 4 - len(meta_children),
        "rare_words": rare,
        "very_rare_words": very_rare,
        "meta_links": len(edges),
        "meta_depth": depth,
        "quickwin_categories": quickwins,
        "categories": len(cats),
        "meta_share": len(meta_children) / len(cats),
    }


def build_dataset() -> tuple:
    data = load()
    zipf = zipf_lookup(data["vocab"])
    levels = data["levels_raw"]["levels"]
    rows, numbers = [], []
    # история слов для repeat_words: слово → нормализованное имя последней
    # категории. Обновляется ПОСЛЕ подсчёта уровня — уровень не может
    # «повторять» сам себя. Семантика — как в generateBlock.repeatCount.
    last_category: dict = {}
    for key in sorted(levels, key=int):
        cats = levels[key]
        repeats = 0
        for cat in cats:
            cat_key = normalize(cat["category"])
            for w in cat["words"]:
                word_key = normalize(w)
                if word_key in last_category and last_category[word_key] != cat_key:
                    repeats += 1
        row = level_features(cats, zipf)
        row["repeat_words"] = repeats
        rows.append(row)
        numbers.append(int(key))
        for cat in cats:
            cat_key = normalize(cat["category"])
            for w in cat["words"]:
                last_category[normalize(w)] = cat_key
    return rows, np.array(numbers, dtype=float)


def design_matrix(rows: list) -> np.ndarray:
    X = np.array([[row[f] for f in FEATURES] for row in rows], dtype=float)
    return np.hstack([np.ones((len(rows), 1)), X])


def target_scale(numbers: np.ndarray) -> np.ndarray:
    """Номер уровня → целевая D на шкале 1..8 (линейный ramp)."""
    lo, hi = numbers.min(), numbers.max()
    return D_FLOOR + (D_CEILING - D_FLOOR) * (numbers - lo) / (hi - lo)


def fit(X: np.ndarray, y: np.ndarray, constrained: bool) -> np.ndarray:
    if not constrained:
        return np.linalg.lstsq(X, y, rcond=None)[0]
    lower = np.full(X.shape[1], -np.inf)
    upper = np.full(X.shape[1], np.inf)
    for i, name in enumerate(FEATURES, start=1):
        if SIGN[name] > 0:
            lower[i] = 0.0
        else:
            upper[i] = 0.0
    return lsq_linear(X, y, bounds=(lower, upper)).x


def evaluate(name: str, y_true_levels: np.ndarray, predicted: np.ndarray) -> dict:
    pearson = float(np.corrcoef(predicted, y_true_levels)[0, 1])
    spearman = float(stats.spearmanr(predicted, y_true_levels).statistic)
    # MAE в единицах номера уровня: переводим предсказание обратно в номер
    lo, hi = y_true_levels.min(), y_true_levels.max()
    back = lo + (predicted - D_FLOOR) * (hi - lo) / (D_CEILING - D_FLOOR)
    mae_levels = float(np.mean(np.abs(back - y_true_levels)))
    return {"set": name, "pearson": round(pearson, 3), "spearman": round(spearman, 3),
            "mae_levels": round(mae_levels, 1)}


def main() -> int:
    rows, numbers = build_dataset()
    X = design_matrix(rows)
    y = target_scale(numbers)

    unconstrained = fit(X, y, constrained=False)
    constrained = fit(X, y, constrained=True)

    # numpy 2.0 на Accelerate BLAS выдаёт ложные предупреждения на matmul;
    # значения проверены на конечность отдельно
    with np.errstate(all="ignore"):
        pred_unc = X @ unconstrained
        pred_con = X @ constrained
    assert np.isfinite(pred_unc).all() and np.isfinite(pred_con).all()

    metrics = [
        evaluate("вся выборка, без ограничений", numbers, pred_unc),
        evaluate("вся выборка, с ограничениями", numbers, pred_con),
    ]

    # блочный holdout: обучение на голове, проверка на хвосте
    train = numbers <= 160
    test = numbers > 160
    w_train = fit(X[train], y[train], constrained=True)
    with np.errstate(all="ignore"):
        pred_test = X[test] @ w_train
    holdout = evaluate("holdout 161-199 (обучение 1-160)", numbers[test], pred_test)
    metrics.append(holdout)

    # различает ли модель две фазы
    phase1 = pred_con[numbers <= 120].mean()
    phase2 = pred_con[numbers > 120].mean()

    # чувствительность: насколько меняется D при изменении одного признака на 1
    sensitivity = {name: round(float(constrained[i]), 4)
                   for i, name in enumerate(FEATURES, start=1)}

    # сравнение знаков
    signs = []
    for i, name in enumerate(FEATURES, start=1):
        signs.append({
            "feature": name,
            "unconstrained": round(float(unconstrained[i]), 4),
            "constrained": round(float(constrained[i]), 4),
            "expected_sign": "+" if SIGN[name] > 0 else "−",
            "flipped": bool((unconstrained[i] < 0) != (SIGN[name] < 0)),
        })

    # диагностика невошедших признаков: считаем их вес в полной модели,
    # чтобы показать ЧИСЛАМИ, почему они не попали в откалиброванную часть
    full_names = FEATURES + DIAGNOSTIC_FEATURES
    X_full = np.hstack([np.ones((len(rows), 1)),
                        np.array([[row[f] for f in full_names] for row in rows], float)])
    w_full = np.linalg.lstsq(X_full, y, rcond=None)[0]
    lower = np.full(X_full.shape[1], -np.inf)
    upper = np.full(X_full.shape[1], np.inf)
    for i, name in enumerate(full_names, start=1):
        if name == "quickwin_categories":
            upper[i] = 0.0
        else:
            lower[i] = 0.0
    w_full_con = lsq_linear(X_full, y, bounds=(lower, upper)).x
    diagnostics = []
    for i, name in enumerate(full_names, start=1):
        if name not in DIAGNOSTIC_FEATURES:
            continue
        diagnostics.append({
            "feature": name,
            "unconstrained_weight": round(float(w_full[i]), 4),
            "constrained_weight": round(float(w_full_con[i]), 4),
            "correlation_with_level": round(float(np.corrcoef(
                np.array([r[name] for r in rows]), numbers)[0, 1]), 3),
        })

    # корреляция сырых признаков с номером уровня — для отчёта
    raw_corr = {}
    for i, name in enumerate(FEATURES):
        raw_corr[name] = round(float(np.corrcoef(X[:, i + 1], numbers)[0, 1]), 3)
    raw_corr["meta_share"] = round(float(np.corrcoef(
        np.array([r["meta_share"] for r in rows]), numbers)[0, 1]), 3)
    raw_corr["meta_depth (вне D_base)"] = round(float(np.corrcoef(
        np.array([r["meta_depth"] for r in rows]), numbers)[0, 1]), 3)

    weights = {"intercept": round(float(constrained[0]), 4)}
    for i, name in enumerate(FEATURES, start=1):
        weights[name] = round(float(constrained[i]), 4)

    # распределение D по референсу с итоговыми весами
    d_values = np.clip(pred_con, 1, 10)
    distribution = {
        "min": round(float(d_values.min()), 2),
        "max": round(float(d_values.max()), 2),
        "mean": round(float(d_values.mean()), 2),
        "p10": round(float(np.percentile(d_values, 10)), 2),
        "p90": round(float(np.percentile(d_values, 90)), 2),
    }

    result = {
        "weights": weights,
        "metrics": metrics,
        "phase_separation": {"phase1_mean_D": round(float(phase1), 2),
                            "phase2_mean_D": round(float(phase2), 2),
                            "gap": round(float(phase2 - phase1), 2)},
        "signs": signs,
        "sensitivity_per_unit": sensitivity,
        "raw_feature_correlation_with_level": raw_corr,
        "not_identified": diagnostics,
        "declared_weights": DECLARED,
        "reference_D_distribution": distribution,
        "levels": len(rows),
    }

    print(json.dumps(result, ensure_ascii=False, indent=1))

    if "--write" in sys.argv:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        config["difficulty"]["base"] = weights
        config["difficulty"]["declared"] = DECLARED
        config["difficulty"]["not_identified_by_reference"] = diagnostics
        config["scoring_version"] = "d-1.3-calibrated"
        config["calibrated"] = True
        config["calibration"] = {
            "dataset": "199 референсных уровней Bubble Word Jam",
            "target": f"номер уровня, линейно отображённый в {D_FLOOR}..{D_CEILING}",
            "method": "МНК с ограничениями на знак весов (scipy lsq_linear)",
            "metrics": metrics,
            "phase_separation": result["phase_separation"],
            "reference_D_distribution": distribution,
            "caveat": "Номер уровня — слабый ordinal proxy дизайнерской прогрессии, "
                      "а не измеренная сложность. Реальный эталон появится "
                      "из телеметрии игроков.",
        }
        CONFIG_PATH.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n",
                               encoding="utf-8")
        print(f"\n→ веса записаны в {CONFIG_PATH.relative_to(ROOT)}")

        write_report(result)
        print(f"→ отчёт {REPORT_PATH.relative_to(ROOT)}")
    return 0


def write_report(r: dict) -> None:
    L = []
    add = L.append
    add("# SCORING — как считаются сложность и интересность\n")
    add("Сгенерировано `scripts/calibrate_difficulty.py --write`.\n")

    add("## 1. Почему модель разделена на три части\n")
    add("Спека предполагала, что все факторы сложности калибруются на "
        "`reference-metrics.csv`. Это неверно: признаков для ловушек, смежности "
        "категорий, модификаторов и сомнений решателя в выгрузке ответов **нет** "
        "(SPEC_AUDIT §3). Поэтому:\n")
    add("```")
    add("D_base        структура уровня — калибруется на 199 референсных уровнях")
    add("D_semantic    двусмысленность — контролируемые пары уровней и решатель")
    add("D_mechanical  модификаторы и теснота лимита ходов — эмулятор")
    add("")
    add("D = clamp(D_base + D_semantic + D_mechanical, 1, 10)")
    add("```")
    add("")
    add("Ниже откалибрована **только первая часть**. Веса двух других объявлены "
        "как продуктовые heuristic и помечены так же в интерфейсе.\n")

    add("## 2. Целевая переменная и её честное название\n")
    add(f"Целевая переменная — номер уровня, линейно отображённый в диапазон "
        f"{D_FLOOR}..{D_CEILING}. Референсу оставлен потолок 8.0, чтобы новым "
        "механикам осталось место 8.5-10 (иначе продолжать кривую некуда).\n")
    add("Это **слабый ordinal proxy**: он отражает дизайнерское суждение авторов "
        "референса, а не измеренную сложность. Формулировка для отчёта:\n")
    add("> Модель D откалибрована на дизайнерской прогрессии референса как на слабом")
    add("> ordinal proxy. Она не претендует на предсказание реального win rate")
    add("> до появления телеметрии игроков.\n")

    add("## 3. Корреляция сырых признаков с номером уровня\n")
    add("| Признак | r |")
    add("|---|---|")
    for name, value in sorted(r["raw_feature_correlation_with_level"].items(),
                              key=lambda kv: -abs(kv[1])):
        add(f"| `{name}` | {value:+.3f} |")
    add("")

    add("## 4. Ограничения на знак весов — и зачем они\n")
    add("| Признак | Без ограничений | С ограничениями | Ожидаемый знак | Знак перевернулся |")
    add("|---|---|---|---|---|")
    for s in r["signs"]:
        add(f"| `{s['feature']}` | {s['unconstrained']:+.4f} | {s['constrained']:+.4f} "
            f"| {s['expected_sign']} | {'**да**' if s['flipped'] else 'нет'} |")
    add("")
    flipped = [s["feature"] for s in r["signs"] if s["flipped"]]
    if flipped:
        add(f"Без ограничений знак переворачивается у: {', '.join(f'`{f}`' for f in flipped)}. "
            "Это не свойство механики, а эффект двухфазности кривой: после L120 "
            "объём растёт, а мета-плотность падает, и регрессия по номеру уровня "
            "приписывает мета отрицательный вклад. Утверждать «мета делает уровень "
            "легче» на этих данных нельзя, поэтому знак зафиксирован содержательно.\n")
    else:
        add("Ни один знак не перевернулся: ограничения ничего не испортили.\n")

    add("## 5. Итоговые веса D_base\n")
    add("```")
    for name, value in r["weights"].items():
        add(f"{name:24s} {value:+.4f}")
    add("```")
    add("")
    add("Читается так: каждый дополнительный пузырь на старте прибавляет "
        f"{r['weights']['start_bubbles']:.4f} к D, каждое редкое слово "
        f"{r['weights']['rare_words']:.4f}, каждое очень редкое — дополнительно "
        f"{r['weights']['very_rare_words']:.4f}. Больше в откалиброванной части нет "
        "ничего, и это главный результат калибровки — см. §7.\n")

    add("## 6. Качество\n")
    add("| Выборка | Pearson | Spearman | MAE в номерах уровня |")
    add("|---|---|---|---|")
    for m in r["metrics"]:
        add(f"| {m['set']} | {m['pearson']:+.3f} | {m['spearman']:+.3f} | {m['mae_levels']} |")
    add("")
    ph = r["phase_separation"]
    add(f"**Различает ли модель две фазы:** средняя D для L1-120 = {ph['phase1_mean_D']}, "
        f"для L121-199 = {ph['phase2_mean_D']}, разрыв {ph['gap']:+.2f}. "
        "Если разрыв положительный, модель воспроизводит перелом кривой.\n")

    holdout = next((m for m in r["metrics"] if "holdout" in m["set"]), None)
    if holdout:
        add("### Блочный holdout — главная проверка честности\n")
        add(f"Обучение на уровнях 1-160, проверка на 161-199: Pearson "
            f"{holdout['pearson']:+.3f}, Spearman {holdout['spearman']:+.3f}, "
            f"MAE {holdout['mae_levels']} уровней.\n")
        if holdout["pearson"] < 0.3:
            add("Результат публикуется как есть: **перенос на хвост слабый**. Причина "
                "структурная — модель, обученная на голове кривой (там сложность растёт "
                "через мета-плотность), не описывает хвост (там она растёт через объём "
                "при падающей мета). Это ограничение метода, а не ошибка реализации, "
                "и оно ровно то, что скрывает внутривыборочная корреляция 0.7.\n")
        else:
            add("Перенос на хвост состоялся: модель описывает не только ту часть "
                "кривой, на которой обучалась.\n")

    add("## 7. Что референс НЕ идентифицирует — главный результат\n")
    add("Три признака проверены и в откалиброванную часть не вошли. Числа:\n")
    add("| Признак | Вес без ограничений | Вес с ограничением знака | r с номером уровня |")
    add("|---|---|---|---|")
    for d in r["not_identified"]:
        add(f"| `{d['feature']}` | {d['unconstrained_weight']:+.4f} | "
            f"{d['constrained_weight']:+.4f} | {d['correlation_with_level']:+.3f} |")
    add("")
    add("Разбор построчно:\n")
    add("**`meta_links` — вес не идентифицируется вообще.** Без ограничений он "
        "**отрицательный** (−0.28), то есть регрессия утверждает, что мета-связи "
        "делают уровень ЛЕГЧЕ. Это артефакт двухфазности: после L120 авторы "
        "референса роняют мета-плотность с 42% до 13% и одновременно раздувают объём, "
        "поэтому номер уровня приписывает мета отрицательный вклад. Под ограничением "
        "знака вес обнуляется. Вывод: **на этих данных вклад мета-связей в сложность "
        "измерить нельзя** — при том, что именно мета является главным механизмом "
        "сложности в референсе (639 связей на 183 уровнях). Это ограничение proxy, "
        "а не механики.\n")
    add("**`meta_depth` — данных нет.** Глубина 3 не встречается ни разу, глубина 2 — "
        "на 25 уровнях из 199, корреляция с номером уровня −0.055. Калибровать вес "
        "рычага, которого в данных нет, невозможно по определению.\n")
    add("**`quickwin_categories` — данные противоречат ожиданию.** Корреляция с номером "
        "уровня **положительная** (+0.29): чем дальше по игре, тем БОЛЬШЕ категорий "
        "быстрой победы. Причина понятна — в фазе 2 уровни крупнее, поэтому лёгких "
        "категорий в них больше в абсолюте. Гипотеза «больше быстрых побед → легче "
        "уровень» на этих данных не подтверждается.\n")
    add("### Как это учтено в модели\n")
    add("Эти три фактора не выброшены и не выданы за откалиброванные. Они собраны "
        "в отдельную корзину `declared` — объявленные продуктовые веса:\n")
    add("```")
    for name, value in r["declared_weights"].items():
        add(f"{name:24s} {value:+.2f}")
    add("```")
    add("")
    add("В разбивке оценки и в интерфейсе эта корзина подписана как «объявленные "
        "продуктовые факторы, не откалиброваны по референсу». Проверяющий видит "
        "границу между измеренным и решённым, а не одно число без происхождения.\n")

    dist = r["reference_D_distribution"]
    add("## 8. Распределение D_base по референсу\n")
    add(f"min {dist['min']}, p10 {dist['p10']}, среднее {dist['mean']}, "
        f"p90 {dist['p90']}, max {dist['max']}.\n")
    add("Головной запас (8.5-10) референсом не занят и остаётся новым механикам: "
        "глубине мета 3, ловушкам и модификаторам.\n")

    add("## 9. Что калибровкой НЕ закрыто\n")
    add("| Часть | Источник истины | Статус |")
    add("|---|---|---|")
    add("| `D_base` | 199 референсных уровней | откалибровано, метрики выше |")
    add("| `D_semantic` — ловушки | прогоны слепого решателя | heuristic, вес объявлен |")
    add("| `D_semantic` — смежность | пары категорий одной темы | heuristic |")
    add("| `D_semantic` — незапланированная спорность | только решатель | не измерено без прогона |")
    add("| `D_mechanical` — цепи | эмулятор и наблюдения | heuristic |")
    add("| `D_mechanical` — теснота ходов | наблюдения целевой игры (K 1.25-1.6) | heuristic |")
    add("")

    add("## 10. Модель интересности I\n")
    add("Четыре композита вместо десяти факторов: десять весов на 15 ручных оценок "
        "переобучились бы гарантированно (SPEC_AUDIT §5).\n")
    add("| Композит | 0..2.5 | Что входит |")
    add("|---|---|---|")
    add("| **Clarity** | + | доля узнаваемых слов, средняя очевидность связей, "
        "штраф за натужные категории и за незапланированную спорность |")
    add("| **Variety** | + | число типов связи, число тематических сфер, "
        "штраф за однотипность больше половины категорий |")
    add("| **Aha** | + | честные ловушки (связь настоящая, но тихая), мета-payoff, "
        "ноль при полном отсутствии и ловушек, и мета |")
    add("| **Freshness** | + | доля слов, новых для пакета, разнообразие тем |")
    add("")
    add("`I = Clarity + Variety + Aha + Freshness`, диапазон 0..10.\n")
    add("Жёсткое требование: интересность обязана уметь падать, когда сложность растёт. "
        "Поэтому у передышки и выхода целевая интересность в плане блока ВЫШЕ, чем у "
        "пика — лёгкий уровень имеет право быть самым приятным. Проверяется наличием "
        "обоих углов: D9/I3 и D3/I8 (`tests/fixtures`).\n")
    add("Что I не является: объективной мерой веселья. Это модель зафиксированного "
        "суждения автора на калибровочном наборе, проверяемая leave-one-out.\n")

    REPORT_PATH.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
