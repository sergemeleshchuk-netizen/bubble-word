"""Выгрузка готового пакета уровней наружу из базы.

База — источник правды, но читать её глазами нельзя, а пакет уровней должен
быть виден в репозитории и на сайте. Здесь ровно одно: собрать уровни с общим
префиксом ключа в один JSON, ничего не досочиняя.

Отличие от `level_review`: тот пакет — про приёмку человеком (бланк решений,
предупреждения, смена статуса на `review_pending`). Этот — про содержимое:
что игрок увидит на поле и как это соотносится с записью оригинала.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from . import composition as composition_mod

PACK_FORMAT = "bubble-level-pack/1.0"

# Манифест выкладок пайплайна. Имя не `index.json`: рядом лежит выкладка
# веб-инструмента со своим списком и другим форматом.
MANIFEST_NAME = "pipeline.json"


def build(conn: sqlite3.Connection, prefix: str) -> dict:
    """Собирает пакет уровней с ключами `<prefix>NNN`."""
    levels: list[dict] = []
    rows = list(
        conn.execute(
            """
            SELECT id, level_key, status, difficulty_score, difficulty_explanation,
                   solution_count, partition_margin, intended_partition_score,
                   best_alternative_score, planned_decoy_count, unplanned_decoy_count,
                   content_hash, generator_version, random_seed, tier
              FROM level_instances
             WHERE level_key LIKE ? || '%'
             ORDER BY level_key
            """,
            (prefix,),
        )
    )
    for number, row in enumerate(rows, start=1):
        level_id = int(row["id"])
        groups = _groups(conn, level_id)
        meta_links = _meta_links(conn, level_id)
        recorded = composition_mod.for_level(number)
        levels.append(
            {
                "level": number,
                "level_key": row["level_key"],
                "status": row["status"],
                "tier": row["tier"],
                "difficulty": {
                    "score": row["difficulty_score"],
                    "explanation": row["difficulty_explanation"],
                },
                "solver": {
                    "solution_count": row["solution_count"],
                    "intended_partition_score": row["intended_partition_score"],
                    "best_alternative_score": row["best_alternative_score"],
                    "partition_margin": row["partition_margin"],
                    "planned_decoys": row["planned_decoy_count"],
                    "unplanned_decoys": row["unplanned_decoy_count"],
                },
                # Состав рядом с записью оригинала: пакет заявлен как повтор её
                # кривой, и расхождение должно быть видно без пересчёта.
                "composition": {
                    "categories": {"pack": len(groups), "recorded": recorded.categories},
                    "meta_links": {"pack": len(meta_links), "recorded": recorded.meta_links},
                    "recorded_source": recorded.source,
                },
                "groups": groups,
                "meta_links": meta_links,
                "content_hash": row["content_hash"],
                "generator_version": row["generator_version"],
                "random_seed": row["random_seed"],
            }
        )

    return {
        "format": PACK_FORMAT,
        "prefix": prefix,
        "levels": levels,
        "totals": _totals(levels),
    }


def _groups(conn: sqlite3.Connection, level_id: int) -> list[dict]:
    groups: list[dict] = []
    for row in conn.execute(
        """
        SELECT g.id AS id, g.position AS position,
               COALESCE(l.display_text, c.label) AS label,
               c.category_key AS rule_key, c.rule AS rule, c.rule_type AS rule_type
          FROM level_groups g
          JOIN categories c ON c.id = g.category_id
          LEFT JOIN category_labels l ON l.id = g.display_label_id
         WHERE g.level_id = ? ORDER BY g.position
        """,
        (level_id,),
    ):
        words = [
            {
                "text": token["display_text"],
                "kind": token["token_kind"],
                **(
                    {"emitted_by": token["source_label"]}
                    if token["token_kind"] == "category_output"
                    else {}
                ),
            }
            for token in conn.execute(
                """
                SELECT t.display_text AS display_text, t.token_kind AS token_kind,
                       COALESCE(sl.display_text, sc.label) AS source_label
                  FROM level_tokens t
                  LEFT JOIN level_groups sg ON sg.id = t.source_group_id
                  LEFT JOIN categories sc   ON sc.id = sg.category_id
                  LEFT JOIN category_labels sl ON sl.id = sg.display_label_id
                 WHERE t.group_id = ? ORDER BY t.slot
                """,
                (int(row["id"]),),
            )
        ]
        groups.append(
            {
                "position": int(row["position"]),
                "label": row["label"],
                "rule_key": row["rule_key"],
                "rule": row["rule"],
                "rule_type": row["rule_type"],
                "words": words,
            }
        )
    return groups


def _meta_links(conn: sqlite3.Connection, level_id: int) -> list[dict]:
    return [
        {
            "token": row["token"],
            "source_group": row["source_label"],
            "target_group": row["target_label"],
            "depth": int(row["depth"]),
        }
        for row in conn.execute(
            """
            SELECT t.display_text AS token, d.depth AS depth,
                   COALESCE(sl.display_text, sc.label) AS source_label,
                   COALESCE(tl.display_text, tc.label) AS target_label
              FROM level_dependencies d
              JOIN level_tokens t  ON t.id = d.to_token_id
              JOIN level_groups sg ON sg.id = d.from_group_id
              JOIN categories sc   ON sc.id = sg.category_id
              LEFT JOIN category_labels sl ON sl.id = sg.display_label_id
              JOIN level_groups tg ON tg.id = t.group_id
              JOIN categories tc   ON tc.id = tg.category_id
              LEFT JOIN category_labels tl ON tl.id = tg.display_label_id
             WHERE d.level_id = ? ORDER BY t.display_text
            """,
            (level_id,),
        )
    ]


def _totals(levels: list[dict]) -> dict:
    words = [
        word["text"].strip().lower()
        for level in levels
        for group in level["groups"]
        for word in group["words"]
    ]
    return {
        "levels": len(levels),
        "groups": sum(len(level["groups"]) for level in levels),
        "bubbles": len(words),
        "distinct_words": len(set(words)),
        "meta_links": sum(len(level["meta_links"]) for level in levels),
        "levels_with_meta": sum(1 for level in levels if level["meta_links"]),
        "recorded_groups": sum(
            level["composition"]["categories"]["recorded"] for level in levels
        ),
        "recorded_meta_links": sum(
            level["composition"]["meta_links"]["recorded"] for level in levels
        ),
        "solver_valid": sum(1 for level in levels if level["status"] == "solver_valid"),
    }


# Медианный K записи: им считается лимит там, где запись его не сохранила
# (уровень 18 снят с середины). Наблюдённые значения — 1.25…1.67.
FALLBACK_K = 1.4
# Пузырей на старте, если запись не сохранила и это число.
FALLBACK_START_BUBBLES = 24


def to_playable(pack: dict) -> list[dict]:
    """Пакет в том виде, в котором его читает прототип `site/playable/`.

    Формат прототипа — `levels/SCHEMA.md`: имя категории и четыре слова
    строками. Мета-пузырь отдельным полем не передаётся: прототип узнаёт его
    сам, сравнивая слово с именами категорий уровня. Это и есть причина, по
    которой источник мета-связи показан под той надписью, которую выпускает.

    Поле берётся с записи оригинала того же номера: у нашего уровня столько же
    категорий, значит и минимум ходов тот же, и лимит сравним.
    """
    levels: list[dict] = []
    for level in pack["levels"]:
        recorded = composition_mod.for_level(level["level"])
        groups = level["groups"]
        moves = _move_limit(recorded, len(groups))
        levels.append(
            {
                "level_id": level["level"],
                "difficulty_target": level["difficulty"]["score"],
                "categories": [
                    {
                        "id": group["rule_key"],
                        "name": group["label"],
                        "words": [word["text"] for word in group["words"]],
                    }
                    for group in groups
                ],
                "traps": [],
                "repeats": [],
                "board": {
                    "start_bubbles": min(
                        recorded.start_bubbles or FALLBACK_START_BUBBLES, len(groups) * 4
                    ),
                    "move_limit": moves,
                    "move_limit_k": recorded.k_observed or (None if moves is None else FALLBACK_K),
                },
                "extensions": {"chunks": [], "chains": None, "picture_words": []},
                "source": {
                    "level_key": level["level_key"],
                    "pack": pack["prefix"],
                    "meta_links": level["meta_links"],
                    "recorded_move_limit": recorded.move_limit,
                },
            }
        )
    return levels


def _move_limit(recorded: composition_mod.Composition, categories: int) -> int | None:
    """Лимит ходов: с записи, а при её молчании — по формуле от категорий."""
    if recorded.number == 1 and recorded.move_limit is None:
        return None  # туториальный уровень записи идёт без лимита
    if recorded.move_limit is not None:
        return recorded.move_limit
    from math import ceil

    return ceil(3 * categories * (recorded.k_observed or FALLBACK_K))


def write_playable(directory: Path, pack: dict, *, prefix: str = "rmk") -> list[Path]:
    """Пишет по файлу на уровень: прототип грузит уровень по одному."""
    directory.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for level in to_playable(pack):
        path = directory / f"{prefix}{level['level_id']}.json"
        path.write_text(
            json.dumps(level, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        written.append(path)
    return written


def _unique_id(directory: Path, prefix: str, moment: datetime) -> str:
    """Идентификатор выкладки: `<префикс>-ММДД-ЧЧММ`, при совпадении с суффиксом.

    Минутной точности хватает для читаемого имени, но две выкладки одного
    пакета внутри минуты — обычное дело при отладке, и без суффикса вторая
    молча съела бы первую. Ровно то, от чего этот механизм и уводит.
    """
    base = f"{prefix}-{moment.strftime('%m%d-%H%M')}"
    if not (directory / f"{base}.json").exists():
        return base
    for attempt in range(2, 100):
        candidate = f"{base}-{attempt}"
        if not (directory / f"{candidate}.json").exists():
            return candidate
    raise RuntimeError(f"не удалось подобрать имя выкладки для {base}")


def write_playable_pack(
    directory: Path,
    pack: dict,
    *,
    prefix: str = "rmk",
    pack_id: str | None = None,
    now: datetime | None = None,
) -> tuple[Path, Path]:
    """Пишет пакет ОДНИМ файлом с уникальным именем плюс манифест каталога.

    Зачем это вместо `write_playable`. Тот кладёт по файлу на уровень с именем
    `<префикс><номер>.json` в общий каталог, и два пакета там неизбежно
    сталкиваются: `ten1.json` рядом с `top1.json` — это уже два разных первого
    уровня в одной папке, а повторный экспорт того же префикса молча затирает
    прошлую выкладку. Восстановить, чем играли неделю назад, нечем.

    Здесь у каждой выкладки свой идентификатор с датой и временем
    (`ten-0802-1731`), поэтому новая ничего не перезаписывает, а старая
    остаётся играбельной. Манифест перечисляет выложенное, и прототип берёт
    список оттуда, а не из зашитой в код строки.

    Манифест называется `pipeline.json`, а не `index.json`, намеренно: рядом
    в том же каталоге живёт выкладка веб-инструмента со своим списком и своим
    форматом. Один файл на две несовместимые схемы — это гонка, в которой
    выигрывает тот, кто записал последним.
    """
    moment = now or datetime.now(UTC)
    directory.mkdir(parents=True, exist_ok=True)
    identifier = pack_id or _unique_id(directory, prefix.lower(), moment)
    levels = to_playable(pack)
    payload = {
        "pack_id": identifier,
        "prefix": pack["prefix"],
        "label": f"{pack['prefix']} · {len(levels)} уровней",
        "created_at": moment.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "levels": levels,
    }
    path = directory / f"{identifier}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest_path = directory / MANIFEST_NAME
    entries: list[dict] = []
    if manifest_path.exists():
        try:
            entries = json.loads(manifest_path.read_text(encoding="utf-8")).get("packs", [])
        except json.JSONDecodeError:
            entries = []
    # Чужие/старые записи неизвестной формы просто пропускаем: манифест — не
    # то место, где стоит падать.
    entries = [
        entry for entry in entries
        if isinstance(entry, dict) and entry.get("pack_id") != identifier
    ]
    entries.append(
        {
            "pack_id": identifier,
            "prefix": payload["prefix"],
            "label": payload["label"],
            "created_at": payload["created_at"],
            "levels": len(levels),
            "file": path.name,
        }
    )
    # Новое сверху: играть обычно хотят в то, что только что собрали.
    entries.sort(key=lambda entry: str(entry.get("created_at", "")), reverse=True)
    manifest_path.write_text(
        json.dumps({"packs": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return path, manifest_path


def write(path: Path, pack: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return path
