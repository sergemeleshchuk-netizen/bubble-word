#!/usr/bin/env python3
"""Пакет из пайплайна -> формат передачи в играбельный прототип.

Зачем нужен. Кнопка «Добавить в Playable» в инструменте кладёт в `localStorage`
результат TS-генератора (`buildHandoffPack` в
`tool/level-tool/web/src/core/playableHandoff.ts`). Но пакеты вида
`levels/packs/*/pack.json` собирает Python-пайплайн, и `BlockResult` для этой
кнопки у них не существует вовсе — сыграть в сданную двадцатку было нельзя.

Скрипт печатает JSON ровно того формата, который читают сайт
(`mountHandoff` в `site/index.html`) и прототип (`?gen=N` в
`site/playable/index.html`). Формат — источник правды в `playableHandoff.ts`,
здесь только перевод; при изменении контракта править там.

Прототипу нужны имя категории и четыре слова строками (мета-пузыри он находит
сам, сравнивая слово с именами других категорий уровня — `applyLevel`), плюс
ПЕРВАЯ ВЫКЛАДКА: что лежит на поле на старте и в каком порядке приходит досыпка,
плюс ЛИМИТ ХОДОВ. Оценки и провенанс сюда по-прежнему не переносятся.

Про лимит отдельно. У блоков TS-генератора он посчитан и берётся как есть.
У пакетов Python-пайплайна блока `board` нет вовсе — они собраны до того, как
доска стала частью пакета. Раньше такой уровень уезжал в прототип без лимита,
и прототип играл его с ∞: давление ходов исчезало, а это половина механики
(GDD §2 п.9). Поэтому недостающий лимит здесь ДОСЧИТЫВАЕТСЯ по той же формуле,
а не оставляется пустым — см. `derive_move_limit`.

Выкладка здесь считается заново, потому что у пакетов пайплайна её нет: они
собраны до того, как выкладка стала частью уровня. Правило — то же, что в
`tool/level-tool/web/src/core/deal.ts`, и оно там же объяснено. Совпадения
байт-в-байт с TS-генератором не требуется и не проверяется: важно, что выкладка
одна и та же при каждом запуске скрипта, то есть уровень в прототипе не меняется
между заходами. Одно отличие честно есть: у пайплайна нет признака quickwin,
поэтому полную четвёрку на старте получает первая подходящая категория, а не
самая простая.

Использование:
    python3 scripts/pack_to_handoff.py ../../levels/packs/first-lineup-20/pack.json
    # затем вставить вывод в консоль браузера на origin сайта:
    #   localStorage.setItem('bubble-level-tool.generated-pack.v1', <вывод>)
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path

# Ключ хранилища. Дублируется в playableHandoff.ts, site/index.html и
# site/playable/index.html — при смене править во всех четырёх местах.
HANDOFF_KEY = "bubble-level-tool.generated-pack.v1"

# Вместимость поля: столько пузырей видно одновременно. Значение одно на проект —
# BOARD_CAPACITY в core/levelMath.ts и в site/playable/index.html.
BOARD_CAPACITY = 24
WORDS_PER_CATEGORY = 4

# Границы K из core/levelMath.ts: 1.6 — просторный ранний уровень, 1.25 — hard,
# где у игрока реально кончаются ходы. Ниже 1.25 не опускаемся.
MIN_MOVE_LIMIT_K = 1.25
MAX_MOVE_LIMIT_K = 1.6


def level_title(level: dict) -> str:
    """Подпись в выпадающем списке. У пакетов пайплайна нет оценки I, только D."""
    groups = level.get("groups") or []
    score = (level.get("difficulty") or {}).get("score")
    parts = [f"Уровень {level.get('level')}", f"{len(groups)} кат"]
    if score is not None:
        parts.append(f"D {score}")
    if level.get("interest") is not None:
        parts.append(f"I {level['interest']}")
    return " · ".join(parts)


def derive_move_limit(level: dict, category_count: int) -> tuple[int | None, float | None]:
    """Лимит ходов уровня для прототипа: взять готовый или досчитать по формуле.

    Формула одна на проект (GDD §2 п.9, `moveLimit` в core/levelMath.ts):
    `move_limit = ceil((3*M + chunks) * K)`. Половинок у наших пакетов нет,
    поэтому chunks = 0 и пол равен `3*M` — трём мерджам на категорию.

    Если у уровня есть блок `board`, он источник правды целиком, включая
    `move_limit: null` у туториала: там лимита нет по замыслу референса, и
    подменять этот осознанный null придуманным числом нельзя.

    Если блока `board` нет (пакеты Python-пайплайна), K выводим из оценки
    сложности: правило говорит «1.6 на ранних, 1.25 на Hard», а сложность —
    единственное, что у такого уровня про тесноту прохода известно. D 1 -> 1.6,
    D 10 -> 1.25, между ними линейно. Это оценка, а не замер, но пустой лимит
    здесь означал бы ∞ в прототипе, что заведомо неверно.
    """
    board = level.get("board")
    if isinstance(board, dict):
        limit = board.get("move_limit", board.get("moveLimit"))
        k = board.get("move_limit_k", board.get("moveLimitK"))
        return limit, k

    floor = category_count * (WORDS_PER_CATEGORY - 1)
    score = (level.get("difficulty") or {}).get("score")
    if score is None:
        k = (MIN_MOVE_LIMIT_K + MAX_MOVE_LIMIT_K) / 2
    else:
        span = (MAX_MOVE_LIMIT_K - MIN_MOVE_LIMIT_K) / 9
        k = MAX_MOVE_LIMIT_K - (max(1.0, min(10.0, float(score))) - 1) * span
    k = round(min(MAX_MOVE_LIMIT_K, max(MIN_MOVE_LIMIT_K, k)), 2)
    return math.ceil(floor * k), k


def from_block_dir(path: Path) -> dict:
    """Выход TS-генератора (`npm run block -- --out DIR`) в тот же промежуточный вид.

    Второй производитель пакетов помимо Python-пайплайна: `scripts/generate_block.ts`
    пишет в каталог `level-N.json` (полная спецификация с оценками) и `game-N.json`
    (то, что отдают в игру). Читаем `level-N.json` — там есть D и I, а подпись в
    списке без оценок бесполезна.
    """
    files = sorted(
        path.glob("level-*.json"),
        key=lambda p: int("".join(c for c in p.stem if c.isdigit()) or 0),
    )
    if not files:
        raise SystemExit(f"ОШИБКА: в {path} нет файлов level-*.json")
    levels = []
    for file in files:
        body = json.loads(file.read_text(encoding="utf-8"))
        spec = body["level_spec"]
        scoring = body.get("scoring") or {}
        levels.append(
            {
                "level": spec["levelId"],
                "difficulty": {"score": scoring.get("difficulty")},
                "interest": scoring.get("interest"),
                "groups": [
                    {
                        "rule_key": c.get("key"),
                        "label": c.get("label"),
                        "words": [{"text": w["text"]} for w in c.get("words", [])],
                    }
                    for c in spec.get("categories", [])
                ],
                # выкладка TS-генератора берётся как есть: пересчитывать её здесь
                # значило бы выдать игроку не тот уровень, который проверен и оценён
                "deal": spec.get("deal"),
                # доска посчитана генератором — вместе с лимитом ходов и его K
                "board": spec.get("board"),
            }
        )
    meta = json.loads((path / "block.json").read_text(encoding="utf-8")) \
        if (path / "block.json").exists() else {}
    return {
        "prefix": path.name,
        "generator_version": meta.get("generator_version"),
        "pack_hash": meta.get("pack_hash", ""),
        "content_snapshot_hash": meta.get("content_snapshot_hash", ""),
        "levels": levels,
    }


def build_deal(level_id: int, categories: list[dict]) -> dict:
    """Первая выкладка: состав поля на старте и очередь досыпки.

    Правило и его обоснование — в `core/deal.ts`, здесь перевод. Коротко:
    мета-слово на поле не кладётся (оно приходит превращением собранной
    четвёрки), одна категория выкладывается целиком, остальное раздаётся по
    кругу почти поровну, и поле с очередью тасуются.
    """
    names = {(c.get("name") or "").upper() for c in categories}
    seed = f"deal::{level_id}::" + ",".join(str(c.get("id")) for c in categories)
    rng = random.Random(seed)

    pools = []
    for category in categories:
        own = (category.get("name") or "").upper()
        # мета-слово: текст пузыря совпадает с именем ДРУГОЙ категории уровня —
        # ровно так его распознаёт и прототип (applyLevel)
        words = [w for w in (category.get("words") or [])
                 if not (w.upper() in names and w.upper() != own)]
        rng.shuffle(words)
        pools.append({"id": category.get("id"), "words": words})

    total = sum(len(p["words"]) for p in pools)
    left = min(BOARD_CAPACITY, total)

    counts = {p["id"]: 0 for p in pools}
    whole = [p for p in pools if len(p["words"]) >= WORDS_PER_CATEGORY]
    opener = whole[0] if whole else None
    if opener is not None and left >= WORDS_PER_CATEGORY:
        counts[opener["id"]] = WORDS_PER_CATEGORY
        left -= WORDS_PER_CATEGORY

    rest = [p for p in pools if p is not opener]
    rng.shuffle(rest)
    i = 0
    while left > 0 and rest:
        pool = rest[i % len(rest)]
        cap = min(WORDS_PER_CATEGORY, len(pool["words"]))
        if counts[pool["id"]] < cap:
            counts[pool["id"]] += 1
            left -= 1
        elif all(counts[p["id"]] >= min(WORDS_PER_CATEGORY, len(p["words"])) for p in rest):
            break   # раздавать больше нечего, а место на поле ещё есть
        i += 1

    start, queue = [], []
    for pool in pools:
        on_field = counts[pool["id"]]
        for k, word in enumerate(pool["words"]):
            (start if k < on_field else queue).append(
                {"word": word, "category": pool["id"]})
    rng.shuffle(start)
    rng.shuffle(queue)
    return {"start": start, "queue": queue}


def build_level(level: dict) -> dict:
    categories = [
        {
            "id": g.get("rule_key") or g.get("label"),
            "name": g.get("label"),
            "words": [w["text"] for w in (g.get("words") or [])],
        }
        for g in (level.get("groups") or [])
    ]
    # готовая выкладка из спека TS-генератора важнее пересчитанной: уровень
    # проверяли и оценивали именно с ней
    deal = level.get("deal") or build_deal(level.get("level") or 0, categories)
    spawnable = len(deal["start"]) + len(deal["queue"])
    move_limit, move_limit_k = derive_move_limit(level, len(categories))
    return {
        "level_id": level.get("level"),
        "title": level_title(level),
        "categories": categories,
        "board": {
            "board_capacity": BOARD_CAPACITY,
            "start_bubbles": spawnable,
            "move_limit": move_limit,
            "move_limit_k": move_limit_k,
        },
        "deal": deal,
    }


def build(pack: dict, label: str | None) -> dict:
    levels = pack.get("levels") or []
    if not levels:
        raise SystemExit("ОШИБКА: в пакете нет уровней")

    numbers = [lv.get("level") for lv in levels if isinstance(lv.get("level"), int)]
    prefix = pack.get("prefix") or "pack"
    return {
        "label": label or f"{prefix} · {len(levels)} уровней",
        # версии инструмента у пакета пайплайна нет: он собран не им
        "tool_version": pack.get("generator_version") or "pipeline",
        "pack_hash": pack.get("pack_hash") or "",
        "content_snapshot_hash": pack.get("content_snapshot_hash") or "",
        "level_range": [min(numbers), max(numbers)] if numbers else [1, len(levels)],
        "levels": [build_level(lv) for lv in levels],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", help="путь к pack.json из levels/packs/*/")
    parser.add_argument("--label", help="имя группы в списке уровней сайта")
    parser.add_argument("--out", help="куда записать (по умолчанию stdout)")
    parser.add_argument("--setitem", action="store_true",
                        help="обернуть в готовую строку localStorage.setItem(...)")
    args = parser.parse_args()

    source = Path(args.pack)
    # Два производителя пакетов: Python-пайплайн отдаёт pack.json, TS-генератор —
    # каталог с level-N.json. Различаем по тому, что передали.
    pack = from_block_dir(source) if source.is_dir() else json.loads(
        source.read_text(encoding="utf-8"))
    handoff = build(pack, args.label)
    body = json.dumps(handoff, ensure_ascii=False, separators=(",", ":"))

    if args.setitem:
        body = f"localStorage.setItem({HANDOFF_KEY!r}, {body!r})"
    if args.out:
        Path(args.out).write_text(body + "\n", encoding="utf-8")
        counts = [len(lv["categories"]) for lv in handoff["levels"]]
        field = [len(lv["deal"]["start"]) for lv in handoff["levels"]]
        limits = [lv["board"]["move_limit"] for lv in handoff["levels"]]
        set_limits = [x for x in limits if x is not None]
        # лимиты печатаем всегда: именно их молчаливая пропажа однажды
        # превратила все сданные уровни в безлимитные
        limit_note = (f"лимит ходов {min(set_limits)}-{max(set_limits)}"
                      if set_limits else "лимита ходов НЕТ НИ У ОДНОГО уровня")
        if set_limits and len(set_limits) < len(limits):
            limit_note += f" (без лимита: {len(limits) - len(set_limits)})"
        print(f"{args.out}: {len(handoff['levels'])} уровней, "
              f"категорий {min(counts)}-{max(counts)}, "
              f"на поле {min(field)}-{max(field)} пузырей, "
              f"{limit_note}, "
              f"метка «{handoff['label']}»",
              file=sys.stderr)
    else:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
