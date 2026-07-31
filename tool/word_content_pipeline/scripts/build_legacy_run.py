#!/usr/bin/env python3
"""Втягивает прежнюю (допайплайновую) базу слов в SQLite как обычный прогон.

Зачем. До пайплайна у проекта была курированная база на 306 категорий
(`tool/data/categories_legacy.json`, собрана 30.07 по категориям уровней 1-20
референса). Пайплайн её не знал, и она жила второй, непроверенной половиной
`tool/data/categories.json`: без готовности, без запретов на сочетание категорий,
без четвёрок, проверенных solver'ом. Уровень, собранный из таких категорий,
проходил мимо главной гарантии инструмента — единственности решения.

Этот скрипт превращает её в источник базы наравне с остальными: категории
получают правило, тип связи и тему, связи — объяснение и две оценки, после чего
readiness, запреты пар и четвёрки досчитываются штатно.

Что чем является:
    spec.jsonl        РУЧНАЯ разметка (в git): что слить, что создать, какое
                      значение у многозначных слов. Три типа записей — merge,
                      new, sense.
    этот скрипт       механическое расширение разметки на пулы слов + проверки
    categories.jsonl  выход: вход для `word-content import-categories`
    memberships.jsonl выход: вход для `word-content import-memberships`
    report.md         что пропущено и почему

Почему не через `validate_ai_run.py`. Тот скрипт проверяет вывод МОДЕЛИ и потому
жёстко ставит `source: ai_meta_hubs_v1` и `review_status: candidate` («AI никогда
не ставит approved сам»), а поля значения слова выбрасывает. Здесь источник —
ручная разметка, поэтому проверки того же класса сделаны ниже своими руками:
типы связей, темы, коллизии ключей и метк, диапазоны оценок, существование
значения слова в базе.

Запуск из каталога tool/word_content_pipeline:
    .venv/bin/python scripts/build_legacy_run.py
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

PIPE = Path(__file__).resolve().parent.parent
REPO = PIPE.parent.parent
RUN = PIPE / "data" / "runs" / "run-002-legacy-merge"
SPEC = RUN / "spec.jsonl"
LEGACY = REPO / "tool" / "data" / "categories_legacy.json"
DB = PIPE / "database" / "content.sqlite"

SOURCE = "legacy_merge_v1"

RELATION_TYPES = {
    "is_a", "part_of", "found_in", "used_for", "used_in", "has_property",
    "associated_with", "member_of_set", "wordplay", "does_action",
}

# Категории, чьи слова — имена собственные. Флаг влияет на risk-флаги и оценку,
# поэтому ставим его явно, а не угадываем по регистру: в прежней базе всё
# записано строчными, включая `spain` и `london`.
PROPER_NOUN_CATEGORIES = {
    "countries", "continents", "days_of_the_week",
    "world_cities", "world_mountains", "us_states", "planets", "bright_stars",
    "girls_names", "months", "greek_myths",
}

# Базовая очевидность по типу связи: насколько связь приходит игроку первой.
# Таксономия («это разновидность X») читается сразу, свободная ассоциация — нет.
OBVIOUSNESS_BASE = {
    "is_a": 0.80, "member_of_set": 0.80, "part_of": 0.75,
    "found_in": 0.70, "used_in": 0.70, "used_for": 0.70,
    "has_property": 0.70, "does_action": 0.70,
    "associated_with": 0.65, "wordplay": 0.55,
}
# Сила связи: строгие отношения курированного пула почти всегда верны,
# свободная ассоциация по определению мягче.
FIT_BY_RELATION = {"associated_with": 0.90, "wordplay": 0.90}
FIT_DEFAULT = 0.95


def policy(fit: float, obv: float) -> str:
    """Тот же порог, что применяется к прогонам AI (level-tool/scripts/review_ai_run.py).

    Разделение осмысленное: сила отвечает «связь настоящая?», очевидность —
    «игрок увидит её сразу?». Настоящая, но неочевидная связь — ловушка, не брак.
    """
    if fit < 0.7:
        return "rejected"
    if fit >= 0.85 and obv >= 0.5:
        return "approved"
    if obv < 0.32:
        return "hard_only"
    return "alternative"


def obviousness(relation: str, zipf: float | None, ambiguous: bool) -> float:
    """Очевидность = база по типу связи, поправленная на знакомость и многозначность.

    Многозначное слово штрафуется: игрок, увидев `bass`, не обязан подумать
    именно про музыку. Редкое слово штрафуется сильнее — его сначала надо узнать.
    """
    # Типы связей вне схемы прогона встречаются у категорий базы (`made_of`).
    # Считаем их такими же читаемыми, как `is_a`: «сделано из X» игрок видит сразу.
    value = OBVIOUSNESS_BASE.get(relation, 0.80)
    if ambiguous:
        value -= 0.15
    if zipf is None:
        value -= 0.25
    elif zipf >= 4.5:
        value += 0.05
    elif zipf < 2.5:
        value -= 0.25
    elif zipf < 3.0:
        value -= 0.15
    return round(min(0.95, max(0.20, value)), 2)


def gameplay_difficulty(obviousness_value: float, base_difficulty: float) -> float:
    """Игровая сложность связи — та же формула, что в scripts/swow_status.py.

    Половина от незаметности связи плюс половина от базовой сложности категории.
    Там на месте заметности стоит скор SWOW, здесь — наша оценка очевидности:
    это одна и та же величина, «насколько связь приходит игроку первой».
    Без этого поля четвёрка из таких слов не получает сложности, а генератор
    строит по ней кривую.
    """
    return round(min(max(0.5 * (1.0 - obviousness_value) + 0.5 * base_difficulty, 0.0), 1.0), 3)


def singular_forms(word: str) -> set[str]:
    """Формы, которые считаем тем же словом в одном пуле.

    В пул нельзя пускать `eye` и `eyes` одновременно: на поле это два пузыря
    одной категории, и уровень выглядит сломанным. Прежняя база писала часть
    слов во множественном числе, пайплайн — в единственном.
    """
    forms = {word}
    if word.endswith("ies") and len(word) > 4:
        forms.add(word[:-3] + "y")
    if word.endswith("es") and len(word) > 3:
        forms.add(word[:-2])
    if word.endswith("s") and not word.endswith("ss"):
        forms.add(word[:-1])
    forms.add(word + "s")
    forms.add(word + "es")
    return forms


def main() -> int:
    if not DB.exists():
        print(f"ОШИБКА: нет базы {DB}", file=sys.stderr)
        return 1

    # Ключи, которые создаёт САМ этот прогон, читаем из разметки заранее: база
    # может быть уже собрана с предыдущим запуском, и тогда её собственные
    # категории выглядели бы как «ключ занят». Скрипт обязан переживать
    # повторный запуск — разметку правят и пересобирают не один раз.
    own_keys = {json.loads(line)["key"]
                for line in SPEC.read_text(encoding="utf-8").splitlines()
                if line.strip() and json.loads(line)["type"] == "new"}

    conn = sqlite3.connect(str(DB))
    db_cats = {r[0]: {"label": r[1], "rule": r[2], "relation_type": r[3],
                      "base_difficulty": r[4]}
               for r in conn.execute("select category_key, label, rule, relation_type, "
                                     "base_difficulty from categories")
               if r[0] not in own_keys}
    db_labels = {}
    for key, cat in db_cats.items():
        db_labels.setdefault(re.sub(r"[^a-z0-9]+", "", cat["label"].lower()), key)
    db_themes = {r[0] for r in conn.execute("select distinct theme from categories")}
    # существующие пулы: нужны, чтобы не добавить в категорию слово, которое там
    # уже есть, и не поставить рядом единственное и множественное число
    pools: dict[str, set[str]] = {}
    # Пулы берём БЕЗ вклада самого этого прогона. Иначе второй запуск видит свои
    # же слова как «уже в категории», пропускает их, и выход зависит от того,
    # собрана ли база с предыдущей версией разметки. Прогон обязан давать один и
    # тот же результат из одной и той же разметки.
    for key, word in conn.execute(
            """select c.category_key, w.normalized from memberships m
                 join categories c on c.id = m.category_id
                 join words w on w.id = m.word_id
                where m.source <> ?""", (SOURCE,)):
        if key in own_keys:
            continue
        pools.setdefault(key, set()).add(word)
    senses_in_db: dict[str, set[str]] = {}
    for norm, sense_key in conn.execute(
            """select w.normalized, s.sense_key from words w
                 join word_senses s on s.word_id = w.id"""):
        senses_in_db.setdefault(norm, set()).add(sense_key)
    sense_defs = dict(conn.execute("select sense_key, definition from word_senses"))
    ambiguous = {w for w, ss in senses_in_db.items() if len(ss) > 1}
    conn.close()

    legacy = {c["id"]: c for c in json.loads(LEGACY.read_text(encoding="utf-8"))["categories"]}
    merge: dict[str, str] = {}
    new: dict[str, dict] = {}
    sense_pick: dict[tuple[str, str], str] = {}
    for line in SPEC.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec["type"] == "merge":
            merge[rec["legacy"]] = rec["into"]
        elif rec["type"] == "new":
            new[rec["legacy"]] = rec
        elif rec["type"] == "sense":
            sense_pick[(rec["legacy"], rec["word"].lower())] = rec["sense"]

    errors: list[str] = []
    skipped: list[str] = []
    stats = Counter()

    # ------------------------------------------------------------------ #
    # проверки разметки до того, как что-то писать
    # ------------------------------------------------------------------ #
    for cid in list(merge) + list(new):
        if cid not in legacy:
            errors.append(f"в разметке есть '{cid}', которого нет в прежней базе")
    missing = set(legacy) - set(merge) - set(new)
    if missing:
        errors.append(f"категории прежней базы не размечены: {sorted(missing)}")
    for cid, target in merge.items():
        if target not in db_cats:
            errors.append(f"слияние '{cid}' -> '{target}': такой категории в базе нет")
    seen_keys: set[str] = set()
    for cid, rec in new.items():
        key, label = rec["key"], rec["label"]
        if key in db_cats:
            errors.append(f"новая '{cid}': ключ '{key}' уже занят в базе")
        if key in seen_keys:
            errors.append(f"новая '{cid}': ключ '{key}' объявлен дважды")
        seen_keys.add(key)
        label_norm = re.sub(r"[^a-z0-9]+", "", label.lower())
        if label_norm in db_labels:
            errors.append(f"новая '{cid}': имя '{label}' занято категорией "
                          f"'{db_labels[label_norm]}'")
        if rec["relation_type"] not in RELATION_TYPES:
            errors.append(f"новая '{cid}': неизвестный relation_type "
                          f"'{rec['relation_type']}'")
        if rec["theme"] not in db_themes:
            errors.append(f"новая '{cid}': темы '{rec['theme']}' нет в базе")
        if "{W}" not in rec["reason"]:
            errors.append(f"новая '{cid}': в шаблоне объяснения нет места под слово")

    if errors:
        print("РАЗМЕТКА НЕ ПРОШЛА ПРОВЕРКУ:", file=sys.stderr)
        for e in errors[:40]:
            print(f"  {e}", file=sys.stderr)
        print(f"  всего проблем: {len(errors)}", file=sys.stderr)
        return 1

    # ------------------------------------------------------------------ #
    # категории
    # ------------------------------------------------------------------ #
    cat_records = []
    for cid, rec in sorted(new.items()):
        cat_records.append({
            "category_key": rec["key"],
            "label": rec["label"],
            "rule": rec["rule"],
            "relation_type": rec["relation_type"],
            "theme": rec["theme"],
            "base_difficulty": rec["base_difficulty"],
        })

    # ------------------------------------------------------------------ #
    # связи
    # ------------------------------------------------------------------ #
    memb_records = []
    # (категория, слово) -> уже добавили в этом прогоне
    emitted: set[tuple[str, str]] = set()
    for cid, cat in sorted(legacy.items()):
        if cid in new:
            target = new[cid]["key"]
            relation = new[cid]["relation_type"]
            reason_tpl = new[cid]["reason"]
            base_difficulty = new[cid]["base_difficulty"]
        else:
            target = merge[cid]
            relation = db_cats[target]["relation_type"]
            # у категории базы сложность может быть не задана — берём середину
            base_difficulty = db_cats[target]["base_difficulty"]
            if base_difficulty is None:
                base_difficulty = 0.5
            # У существующей категории объяснение строим из её собственного правила:
            # оно и есть причина, по которой слово туда попадает. Формулировка
            # ссылается на правило, а не пересказывает его: правила в базе написаны
            # по-разному (то единственным числом, то множественным), и подстановка
            # слова прямо в них давала бессвязные фразы вида «kid — words for the…».
            reason_tpl = "{W} fits the category rule: " + db_cats[target]["rule"]
        # Тип связи для НОВОЙ категории обязан быть из схемы прогона — он проверен
        # выше. Для слияния он берётся у существующей категории базы и потому
        # валиден по построению: в базе живут и типы вне схемы прогона (`made_of`
        # у материалов), и запрещать их значило бы пропустить законное слияние.
        if cid in new and relation not in RELATION_TYPES:
            skipped.append(f"{cid}: тип связи '{relation}' вне схемы прогона")
            stats["категорий пропущено по типу связи"] += 1
            continue

        pool = pools.setdefault(target, set())
        for entry in cat["words"]:
            word = entry["w"].strip()
            norm = word.lower()
            if (target, norm) in emitted:
                continue
            # слово уже в этой категории — импорт был бы пустой перезаписью
            if norm in pool:
                stats["связей пропущено: слово уже в категории"] += 1
                continue
            clash = singular_forms(norm) & pool
            if clash:
                skipped.append(f"{target}: '{word}' не добавлено — в пуле уже "
                               f"{', '.join(sorted(clash))} (то же слово в другом числе)")
                stats["связей пропущено: единственное/множественное"] += 1
                continue

            zipf = entry.get("zipf")
            is_ambiguous = norm in ambiguous
            obv = obviousness(relation, zipf, is_ambiguous)
            fit = FIT_BY_RELATION.get(relation, FIT_DEFAULT)
            status = policy(fit, obv)

            out = {
                "word": word,
                "language": "en",
                "part_of_speech": ("adjective" if relation == "has_property"
                                   else "verb" if relation == "does_action" else "noun"),
                "is_proper_noun": target in PROPER_NOUN_CATEGORIES,
                "category_key": target,
                "relation_type": relation,
                "reason": reason_tpl.replace("{W}", word),
                "fit_score": fit,
                "obviousness_score": obv,
                "gameplay_difficulty": gameplay_difficulty(obv, base_difficulty),
                "source": SOURCE,
                "review_status": status,
                "risk_flags": [],
            }

            # Значение слова. Для многозначных слов оно обязательно: приёмка
            # базы блокирует связь многозначного слова без указанного значения.
            picked = sense_pick.get((cid, norm))
            if picked:
                if picked not in senses_in_db.get(norm, set()):
                    errors.append(f"{cid}/{word}: значения '{picked}' у слова в базе нет")
                    continue
                out["sense_key"] = picked
                out["sense_definition"] = sense_defs[picked]
            elif is_ambiguous and relation != "wordplay":
                errors.append(f"{cid}/{word} -> {target}: слово многозначное "
                              f"({len(senses_in_db[norm])} значений), а значение не указано в spec.jsonl")
                continue

            memb_records.append(out)
            emitted.add((target, norm))
            pool.add(norm)
            stats[f"статус {status}"] += 1

    if errors:
        print("СБОРКА ОСТАНОВЛЕНА:", file=sys.stderr)
        for e in errors[:40]:
            print(f"  {e}", file=sys.stderr)
        print(f"  всего проблем: {len(errors)}", file=sys.stderr)
        return 1

    # Карта «прежний id -> нынешний ключ». Сданные пакеты (etalon, volume1,
    # volume2, демо) ссылаются на id прежней базы, и без карты они перестали бы
    # проверяться валидатором. Раньше ту же задачу решали иначе: в выгрузку для
    # скиллов подмешивали сами категории прежней базы, и в ней жили два слоя
    # качества — проверенный и никакой. Теперь слой один, а старые id разрешаются
    # через псевдоним.
    aliases = {cid: (new[cid]["key"] if cid in new else merge[cid])
               for cid in sorted(legacy)}
    ALIASES_OUT = REPO / "tool" / "data" / "category_aliases.json"
    ALIASES_OUT.write_text(json.dumps({
        "note": "прежний id категории -> ключ в SQLite; см. "
                "tool/word_content_pipeline/scripts/build_legacy_run.py",
        "aliases": aliases,
    }, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "categories.jsonl").write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cat_records),
        encoding="utf-8")
    (RUN / "memberships.jsonl").write_text(
        "".join(json.dumps(m, ensure_ascii=False) + "\n" for m in memb_records),
        encoding="utf-8")

    report = [
        "# Прогон run-002-legacy-merge\n",
        "Прежняя база на 306 категорий втянута в SQLite как обычный источник.",
        "Разметка — `spec.jsonl` (руками), расширение на пулы — "
        "`scripts/build_legacy_run.py`.\n",
        f"- категорий создано: **{len(cat_records)}**",
        f"- категорий пополнено словами: **{len(merge) - stats['категорий пропущено по типу связи']}**",
        f"- связей записано: **{len(memb_records)}**\n",
        "## Статусы связей\n",
        "Статус выведен политикой из силы связи и очевидности — тем же порогом,",
        "что применяется к прогонам AI. Семантическая ось (`semantic_status`)",
        "остаётся `unreviewed`: глазами эти связи никто не смотрел.\n",
    ]
    for key in ("статус approved", "статус alternative", "статус hard_only", "статус rejected"):
        if stats[key]:
            report.append(f"- {key.replace('статус ', '')}: {stats[key]}")
    report.append("\n## Что не пошло в базу\n")
    for key, value in sorted(stats.items()):
        if key.startswith("связей пропущено") or key.startswith("категорий пропущено"):
            report.append(f"- {key}: {value}")
    if skipped:
        report.append("\nПодробно:\n")
        report.extend(f"- {s}" for s in skipped)
    (RUN / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"категорий создано:  {len(cat_records)}")
    print(f"связей записано:    {len(memb_records)}")
    for key, value in sorted(stats.items()):
        print(f"  {key}: {value}")
    print(f"-> {RUN.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
