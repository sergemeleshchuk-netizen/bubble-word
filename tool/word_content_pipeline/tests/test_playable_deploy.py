"""Выкладка пакета в прототип: уникальное имя и манифест каталога.

Прежний способ — `write_playable`, по файлу на уровень с именем
`<префикс><номер>.json` — складывал разные пакеты в один каталог, где
`ten1.json` и `top1.json` это два разных первого уровня, а повторный экспорт
того же префикса молча затирал прошлую выкладку.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from word_content import level_pack

MOMENT = datetime(2026, 8, 2, 15, 20, 26, tzinfo=UTC)


def _pack(prefix: str, levels: int = 2) -> dict:
    return {
        "format": level_pack.PACK_FORMAT,
        "prefix": prefix,
        "levels": [
            {
                "level": number,
                "level_key": f"{prefix}{number:03d}",
                "status": "solver_valid",
                "difficulty": {"score": 3.0, "explanation": ""},
                "meta_links": [],
                "groups": [
                    {
                        "position": 1,
                        "label": "COLORS",
                        "rule_key": "colors",
                        "rule": "Basic colours",
                        "rule_type": "property_group",
                        "words": [
                            {"text": word, "kind": "lexical_word"}
                            for word in ("red", "blue", "green", "orange")
                        ],
                    }
                ],
            }
            for number in range(1, levels + 1)
        ],
    }


def test_pack_id_carries_short_date_and_time(tmp_path: Path):
    path, _ = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    assert path.name == "ten-0802-1520.json"


def test_second_deploy_in_the_same_minute_does_not_overwrite(tmp_path: Path):
    """Две выкладки внутри минуты — обычная отладка, и вторая не должна съедать первую."""
    first, _ = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    second, manifest = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    assert first.exists() and second.exists()
    assert first.name != second.name
    ids = [entry["pack_id"] for entry in json.loads(manifest.read_text())["packs"]]
    assert set(ids) == {"ten-0802-1520", "ten-0802-1520-2"}


def test_two_packs_do_not_collide_in_one_directory(tmp_path: Path):
    """Разные пакеты в одном каталоге: прежний способ давал два `1.json`."""
    ten, _ = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    top, manifest = level_pack.write_playable_pack(
        tmp_path, _pack("TOP", levels=3), prefix="top", now=MOMENT
    )
    assert ten.name != top.name
    entries = json.loads(manifest.read_text())["packs"]
    assert {entry["prefix"] for entry in entries} == {"TEN", "TOP"}
    assert {entry["levels"] for entry in entries} == {2, 3}


def test_manifest_survives_a_foreign_format(tmp_path: Path):
    """Рядом живёт выкладка веб-инструмента со своим списком строк.

    Свой манифест у пайплайна отдельным именем, но если в него всё же попадёт
    чужая запись, падать нельзя: манифест — не то место, где стоит ронять
    сборку.
    """
    manifest_path = tmp_path / level_pack.MANIFEST_NAME
    manifest_path.write_text(
        json.dumps({"packs": ["someone-elses.handoff.json"]}), encoding="utf-8"
    )
    _, manifest = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    entries = json.loads(manifest.read_text())["packs"]
    assert [entry["pack_id"] for entry in entries] == ["ten-0802-1520"]


def test_pack_file_is_self_describing(tmp_path: Path):
    """Прототип читает файл целиком: ему нужны id, подпись и уровни."""
    path, _ = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", now=MOMENT
    )
    payload = json.loads(path.read_text())
    assert payload["pack_id"] == "ten-0802-1520"
    assert payload["prefix"] == "TEN"
    assert payload["created_at"] == "2026-08-02T15:20:26Z"
    assert len(payload["levels"]) == 2
    first = payload["levels"][0]
    assert first["categories"][0]["name"] == "COLORS"
    assert first["categories"][0]["words"] == ["red", "blue", "green", "orange"]


def test_explicit_pack_id_wins(tmp_path: Path):
    """Имя можно задать руками: выкладка обязана быть воспроизводимой."""
    path, _ = level_pack.write_playable_pack(
        tmp_path, _pack("TEN"), prefix="ten", pack_id="demo", now=MOMENT
    )
    assert path.name == "demo.json"
