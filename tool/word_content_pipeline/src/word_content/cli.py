"""CLI пайплайна. Все пути передаются флагами, абсолютных путей в коде нет."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Annotated, Any

import typer
from pydantic import ValidationError

from . import baseline
from . import candidate_generation as gen
from . import (
    composition,
    conflicts,
    cooldown,
    dedupe,
    integrity,
    level_audit,
    level_eval,
    level_generator,
    level_pack,
    level_review,
    level_solver,
    meta_pairs,
    meta_validation,
    migrations,
    normalization,
    profiles,
    quartet_builder,
    readiness,
    reference_coverage,
    reference_fixtures,
    reference_import,
    scoring,
    sense_gaps,
    solver,
    structured,
)
from .blocklist import Blocklist
from .blocklist import default_path as default_blocklist_path
from .db import init_db, open_existing, utc_now
from .exporters import export_review_csv, write_jsonl
from .importers import (
    ImportReport,
    import_categories,
    import_membership_records,
    import_memberships,
    import_review_csv,
)
from .llm.base import LLMError, LLMProvider
from .llm.mock import MockLLMProvider, echo_handler
from .llm.openai_compatible import provider_from_env
from .models import CategoryConflictInput, QuartetInput
from .repositories import (
    RepositoryError,
    clear_category_conflicts,
    clear_quartets,
    collect_stats,
    coverage_report,
    ensure_primary_labels,
    ensure_rule_types,
    get_category,
    list_categories,
    memberships_for_category,
    memberships_for_word,
    replace_pair_groups,
    set_schema_meta,
    upsert_category_conflict,
    upsert_quartet,
    words_with_status,
)
from .validators import ContentFilter, ValidationIssue, parse_statuses

app = typer.Typer(
    add_completion=False,
    help="Контентная база слов и категорий: SQLite как рабочая база, JSONL как обменный формат.",
)

DbOption = Annotated[Path, typer.Option("--db", help="Путь к файлу SQLite")]
InputOption = Annotated[Path, typer.Option("--input", help="Путь к входному файлу")]
OutputOption = Annotated[Path, typer.Option("--output", help="Путь к выходному файлу")]
StatusesOption = Annotated[
    str | None,
    typer.Option("--statuses", help="Фильтр статусов через запятую: approved,hard_only"),
]
BlocklistOption = Annotated[
    Path | None,
    typer.Option("--blocklist", help="Файл блок-листа (по умолчанию data/blocklist.txt проекта)"),
]
NoBlocklistOption = Annotated[
    bool, typer.Option("--no-blocklist", help="Отключить блок-лист (не рекомендуется)")
]
MinZipfOption = Annotated[
    float | None,
    typer.Option(
        "--min-zipf",
        help="Отклонять слова с частотностью ниже порога (ориентир 2.5; по умолчанию только предупреждение)",
    ),
]


def _content_filter(
    blocklist: Path | None, no_blocklist: bool, min_zipf: float | None
) -> ContentFilter:
    """Собирает фильтры контента. Блок-лист включён по умолчанию."""
    if no_blocklist:
        return ContentFilter(blocklist=None, min_zipf=min_zipf)
    path = blocklist or default_blocklist_path()
    try:
        loaded = Blocklist.load(path)
    except FileNotFoundError as exc:
        _fail(str(exc))
        raise
    if path is not None:
        typer.echo(f"Блок-лист: {path} ({len(loaded)} записей)")
    return ContentFilter(blocklist=loaded, min_zipf=min_zipf)


def _fail(message: str) -> None:
    typer.secho(f"Ошибка: {message}", fg=typer.colors.RED, err=True)
    raise typer.Exit(code=1)


def _open(db: Path) -> sqlite3.Connection:
    try:
        return open_existing(db)
    except (FileNotFoundError, RuntimeError) as exc:
        _fail(str(exc))
        raise  # недостижимо, нужно для типизации


def _print_report(title: str, report: ImportReport, show_errors: int = 10) -> None:
    typer.echo(
        f"{title}: total={report.total} inserted={report.inserted} "
        f"updated={report.updated} rejected={report.rejected}"
    )
    for error in report.errors[:show_errors]:
        typer.secho(
            f"  строка {error['line']}: {error['error']}", fg=typer.colors.YELLOW, err=True
        )
    if len(report.errors) > show_errors:
        typer.secho(
            f"  ... ещё {len(report.errors) - show_errors} ошибок (полный список в import_runs)",
            fg=typer.colors.YELLOW,
            err=True,
        )


def _print_table(headers: list[str], rows: list[list[str]]) -> None:
    if not rows:
        typer.echo("(пусто)")
        return
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    line = "  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    typer.echo(line)
    typer.echo("-" * len(line))
    for row in rows:
        typer.echo("  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))


def _truncate(text: str | None, limit: int) -> str:
    value = text or ""
    return value if len(value) <= limit else value[: limit - 1] + "…"


# ----------------------------------------------------------------------- база и импорт


@app.command("init-db")
def cmd_init_db(db: DbOption) -> None:
    """Создаёт базу и все таблицы. Повторный запуск безопасен."""
    path = init_db(db)
    typer.echo(f"База готова: {path}")


@app.command("import-categories")
def cmd_import_categories(db: DbOption, input: InputOption) -> None:
    """Импортирует каталог категорий из JSONL (upsert по category_key)."""
    conn = _open(db)
    try:
        report = import_categories(conn, input)
    except FileNotFoundError as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()
    _print_report("Категории", report)


@app.command("import-memberships")
def cmd_import_memberships(
    db: DbOption,
    input: InputOption,
    overwrite_review_status: Annotated[
        bool,
        typer.Option(
            "--overwrite-review-status",
            help="Принудительно перезаписать review_status из файла (по умолчанию ручные решения сохраняются)",
        ),
    ] = False,
    blocklist: BlocklistOption = None,
    no_blocklist: NoBlocklistOption = False,
    min_zipf: MinZipfOption = None,
) -> None:
    """Импортирует связи слово->категория из JSONL. Плохие строки не останавливают импорт."""
    conn = _open(db)
    try:
        report = import_memberships(
            conn,
            input,
            overwrite_review_status=overwrite_review_status,
            content_filter=_content_filter(blocklist, no_blocklist, min_zipf),
        )
    except FileNotFoundError as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()
    _print_report("Связи", report)


@app.command("export-review")
def cmd_export_review(
    db: DbOption,
    output: OutputOption,
    status: Annotated[
        str, typer.Option("--status", help="Какие статусы выгружать, через запятую")
    ] = "candidate",
) -> None:
    """Выгружает связи в CSV для ручной проверки (колонки decision/review_comment пустые)."""
    conn = _open(db)
    try:
        statuses = parse_statuses(status)
        count = export_review_csv(conn, output, statuses)
    except ValidationIssue as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()
    typer.echo(f"Выгружено строк: {count} -> {output}")


@app.command("import-review")
def cmd_import_review(db: DbOption, input: InputOption) -> None:
    """Импортирует решения reviewer из CSV обратно в базу."""
    conn = _open(db)
    try:
        report = import_review_csv(conn, input)
    except FileNotFoundError as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()
    _print_report("Review", report)


# ------------------------------------------------------------------------------ запросы


@app.command("word-info")
def cmd_word_info(
    db: DbOption,
    word: Annotated[str, typer.Option("--word", help="Слово в любом регистре")],
    statuses: StatusesOption = None,
) -> None:
    """Показывает все категории слова с учётом фильтра статусов."""
    conn = _open(db)
    try:
        status_list = parse_statuses(statuses)
        rows = memberships_for_word(conn, word, status_list)
    except ValidationIssue as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()

    _print_table(
        ["word", "sense", "category", "relation", "fit", "obv", "status", "reason"],
        [
            [
                row["word"],
                _truncate(row["sense_key"], 22),
                row["category_key"],
                row["relation_type"],
                f"{row['fit_score']:.2f}",
                f"{row['obviousness_score']:.2f}",
                row["review_status"],
                _truncate(row["reason"], 50),
            ]
            for row in rows
        ],
    )
    typer.echo(f"Всего связей: {len(rows)}")


@app.command("category-info")
def cmd_category_info(
    db: DbOption,
    category: Annotated[str, typer.Option("--category", help="category_key")],
    statuses: StatusesOption = None,
) -> None:
    """Показывает все слова категории с учётом фильтра статусов."""
    conn = _open(db)
    try:
        status_list = parse_statuses(statuses)
        if get_category(conn, category) is None:
            _fail(f"Категория {category!r} не найдена")
        rows = memberships_for_category(conn, category, status_list)
    except ValidationIssue as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()

    _print_table(
        ["word", "sense", "relation", "fit", "obv", "status", "reason"],
        [
            [
                row["word"],
                _truncate(row["sense_key"], 22),
                row["relation_type"],
                f"{row['fit_score']:.2f}",
                f"{row['obviousness_score']:.2f}",
                row["review_status"],
                _truncate(row["reason"], 50),
            ]
            for row in rows
        ],
    )
    typer.echo(f"Всего слов: {len(rows)}")


@app.command("stats")
def cmd_stats(db: DbOption) -> None:
    """Сводка по базе: объём, статусы, распределение категорий на слово, узкие места."""
    conn = _open(db)
    try:
        data = collect_stats(conn)
    finally:
        conn.close()

    typer.echo(f"Слов:        {data['words']}")
    typer.echo(f"Значений:    {data['senses']}")
    typer.echo(f"Категорий:   {data['categories']}")
    typer.echo(f"Связей:      {data['memberships']}")
    typer.echo("По статусам: " + (", ".join(f"{k}={v}" for k, v in sorted(data["by_status"].items())) or "-"))
    typer.echo(f"Среднее число категорий на слово: {data['avg_categories_per_word']}")
    buckets = data["words_by_category_count"]
    typer.echo(
        "Слов с N категориями: "
        + ", ".join(f"{k}: {buckets[k]}" for k in ("1", "2", "3", "4", "5+"))
    )

    typer.echo(f"\nКатегории с числом approved-связей < 8 ({len(data['thin_categories'])}):")
    for key, count in data["thin_categories"][:40]:
        typer.echo(f"  {key}: {count}")
    if len(data["thin_categories"]) > 40:
        typer.echo(f"  ... ещё {len(data['thin_categories']) - 40}")

    typer.echo("\nТоп-20 слов по числу approved-категорий:")
    for text, count in data["top_words"]:
        typer.echo(f"  {text}: {count}")

    typer.echo("\nТоп-20 категорий по числу approved-слов:")
    for key, count in data["top_categories"]:
        typer.echo(f"  {key}: {count}")

    typer.echo(
        f"\nРедких слов (частотность ниже порога): {data['rare_words_total']}"
        f" | без оценки частотности: {data['words_without_familiarity']}"
    )
    for text, score in data["rare_words"][:15]:
        typer.echo(f"  {text}: {score}")


@app.command("coverage")
def cmd_coverage(
    db: DbOption,
    target: Annotated[
        int, typer.Option("--target", help="Целевая глубина пула: сколько слов нужно категории")
    ] = 25,
    statuses: StatusesOption = None,
    show: Annotated[int, typer.Option("--show", help="Сколько самых тонких категорий показать")] = 30,
) -> None:
    """План работы: каким категориям сколько слов не хватает до целевой глубины."""
    conn = _open(db)
    try:
        status_list = parse_statuses(statuses)
        data = coverage_report(conn, target_depth=target, statuses=status_list)
    except ValidationIssue as exc:
        _fail(str(exc))
        return
    finally:
        conn.close()

    typer.echo(
        f"Категорий: {data['categories']} | слов: {data['words']} | "
        f"в 2+ категориях: {data['multi_category_words']} ({data['multi_category_share'] * 100:.0f}%)"
    )
    typer.echo(
        f"До глубины {data['target_depth']} слов на категорию не хватает "
        f"{data['memberships_needed']} связей"
    )

    typer.echo("\nПо темам:")
    _print_table(
        ["theme", "категорий", "есть", "добрать"],
        [
            [theme, str(v["categories"]), str(v["have"]), str(v["need"])]
            for theme, v in sorted(data["by_theme"].items(), key=lambda kv: -kv[1]["need"])
        ],
    )

    thin = [item for item in data["per_category"] if item["need"] > 0][:show]
    typer.echo(f"\nСамые тонкие категории (показано {len(thin)}):")
    _print_table(
        ["category_key", "тема", "есть", "добрать"],
        [[i["category_key"], i["theme"], str(i["have"]), str(i["need"])] for i in thin],
    )


# --------------------------------------------------------------------------- AI-проходы


def _build_provider(provider: str, model: str | None, mock_file: Path | None) -> LLMProvider:
    if provider == "mock":
        if mock_file is not None:
            return MockLLMProvider.from_file(mock_file)
        return MockLLMProvider(handler=echo_handler, model=model or "mock-echo")
    if provider in ("openai", "openai_compatible"):
        return provider_from_env(model)
    raise LLMError(f"Неизвестный провайдер {provider!r}. Доступны: mock, openai")


ProviderOption = Annotated[
    str, typer.Option("--provider", help="mock или openai (OpenAI-compatible API)")
]
MockFileOption = Annotated[
    Path | None,
    typer.Option("--mock-file", help="JSON-файл с заготовленными ответами для mock-провайдера"),
]
ModelOption = Annotated[
    str | None, typer.Option("--model", help="Имя модели (иначе берётся из LLM_MODEL)")
]


def _report_generation(result: gen.GenerationResult, output: Path) -> None:
    written = write_jsonl(output, gen.records_to_jsonl_dicts(result.records))
    typer.echo(
        f"Записей получено: {written} | batches ok={result.batches_ok} "
        f"failed={result.batches_failed} | отброшено: {len(result.skipped)}"
    )
    reasons: dict[str, int] = {}
    for item in result.skipped:
        key = str(item["reason"]).split(":")[0]
        reasons[key] = reasons.get(key, 0) + 1
    if reasons:
        typer.echo("Причины отбраковки: " + ", ".join(f"{k}={v}" for k, v in sorted(reasons.items())))
    typer.echo(f"Файл: {output}")


@app.command("generate-category-candidates")
def cmd_generate_category_candidates(
    db: DbOption,
    output: OutputOption,
    category: Annotated[
        str | None, typer.Option("--category", help="category_key одной категории")
    ] = None,
    all_categories: Annotated[
        bool, typer.Option("--all-categories", help="Прогнать весь каталог категорий")
    ] = False,
    only_thin: Annotated[
        int | None,
        typer.Option("--only-thin", help="Только категории, где слов меньше указанного числа"),
    ] = None,
    checkpoint: Annotated[
        Path | None,
        typer.Option("--checkpoint", help="Файл прогресса: пройденные категории пропускаются"),
    ] = None,
    count: Annotated[int, typer.Option("--count", help="Сколько слов запросить")] = 30,
    batch_size: Annotated[int, typer.Option("--batch-size")] = 15,
    max_retries: Annotated[int, typer.Option("--max-retries")] = 2,
    provider: ProviderOption = "mock",
    model: ModelOption = None,
    mock_file: MockFileOption = None,
    do_import: Annotated[
        bool, typer.Option("--import", help="Сразу импортировать кандидатов в базу")
    ] = False,
    blocklist: BlocklistOption = None,
    no_blocklist: NoBlocklistOption = False,
    min_zipf: MinZipfOption = None,
) -> None:
    """Проход A: категория -> кандидатные слова. Всё сохраняется со статусом candidate."""
    conn = _open(db)
    try:
        targets = _generation_targets(conn, category, all_categories, only_thin, checkpoint)
        if not targets:
            typer.echo("Нечего генерировать: все категории уже пройдены или отфильтрованы.")
            return

        llm = _build_provider(provider, model, mock_file)
        filters = _content_filter(blocklist, no_blocklist, min_zipf)
        all_records: list[dict[str, Any]] = []
        hints: dict[str, list[str]] = {}
        merged = gen.GenerationResult()

        for index, key in enumerate(targets, start=1):
            if len(targets) > 1:
                typer.echo(f"[{index}/{len(targets)}] {key}")
            try:
                result = gen.expand_category(
                    conn,
                    llm,
                    category_key=key,
                    count=count,
                    batch_size=batch_size,
                    max_retries=max_retries,
                )
            except LLMError as exc:  # провайдер лёг — не теряем уже собранное
                typer.secho(f"  провайдер недоступен: {exc}", fg=typer.colors.RED, err=True)
                break
            all_records.extend(result.records)
            merged.skipped.extend(result.skipped)
            merged.batches_ok += result.batches_ok
            merged.batches_failed += result.batches_failed
            for word, keys in result.hints.items():
                hints.setdefault(word, []).extend(keys)
            if checkpoint is not None:
                _append_checkpoint(checkpoint, key)

        merged.records = all_records
        merged.hints = hints
        _report_generation(merged, output)
        if hints:
            preview = ", ".join(f"{w}->{sorted(set(k))}" for w, k in list(hints.items())[:10])
            typer.echo(f"Подсказки для reverse-прохода: {preview}")
        if do_import:
            report = import_membership_records(
                conn,
                [(i, rec) for i, rec in enumerate(all_records, start=1)],
                source_file=str(output),
                import_type="ai_category_expansion",
                content_filter=filters,
            )
            _print_report("Импорт кандидатов", report)
    except (LLMError, ValidationIssue) as exc:
        _fail(str(exc))
    finally:
        conn.close()


def _generation_targets(
    conn: sqlite3.Connection,
    category: str | None,
    all_categories: bool,
    only_thin: int | None,
    checkpoint: Path | None,
) -> list[str]:
    """Список категорий для прогона с учётом --only-thin и чекпойнта."""
    if category and all_categories:
        raise ValidationIssue("Укажите либо --category, либо --all-categories, но не оба")
    if category:
        keys = [category]
    elif all_categories or only_thin is not None:
        keys = [row["category_key"] for row in list_categories(conn)]
    else:
        raise ValidationIssue("Укажите --category, --all-categories или --only-thin")

    if only_thin is not None:
        sizes = {
            row["category_key"]: int(row["n"])
            for row in conn.execute(
                """
                SELECT c.category_key AS category_key, COUNT(m.id) AS n
                  FROM categories c LEFT JOIN memberships m ON m.category_id = c.id
                 GROUP BY c.id
                """
            )
        }
        keys = [key for key in keys if sizes.get(key, 0) < only_thin]

    done = _read_checkpoint(checkpoint)
    return [key for key in keys if key not in done]


def _read_checkpoint(path: Path | None) -> set[str]:
    if path is None or not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def _append_checkpoint(path: Path, key: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(key + "\n")


@app.command("generate-word-memberships")
def cmd_generate_word_memberships(
    db: DbOption,
    output: OutputOption,
    words: Annotated[
        str | None, typer.Option("--words", help="Слова через запятую: apple,bank,bat")
    ] = None,
    all_approved_words: Annotated[
        bool,
        typer.Option("--all-approved-words", help="Взять все слова с approved-связями"),
    ] = False,
    limit: Annotated[int | None, typer.Option("--limit", help="Ограничить число слов")] = None,
    batch_size: Annotated[int, typer.Option("--batch-size")] = 8,
    max_retries: Annotated[int, typer.Option("--max-retries")] = 2,
    provider: ProviderOption = "mock",
    model: ModelOption = None,
    mock_file: MockFileOption = None,
    do_import: Annotated[
        bool, typer.Option("--import", help="Сразу импортировать кандидатов в базу")
    ] = False,
    blocklist: BlocklistOption = None,
    no_blocklist: NoBlocklistOption = False,
    min_zipf: MinZipfOption = None,
) -> None:
    """Проход B: слово -> дополнительные категории из существующего каталога."""
    conn = _open(db)
    try:
        if all_approved_words:
            word_list = words_with_status(
                conn, ["approved", "alternative", "hard_only"], limit=limit
            )
        elif words:
            word_list = [w.strip() for w in words.split(",") if w.strip()]
            if limit:
                word_list = word_list[:limit]
        else:
            conn.close()
            _fail("Укажите --words или --all-approved-words")
            return

        if not word_list:
            conn.close()
            _fail("Список слов пуст")
            return

        llm = _build_provider(provider, model, mock_file)
        result = gen.expand_words(
            conn,
            llm,
            words=word_list,
            batch_size=batch_size,
            max_retries=max_retries,
        )
    except (LLMError, ValidationIssue) as exc:
        conn.close()
        _fail(str(exc))
        return

    try:
        typer.echo(f"Слов на входе: {len(word_list)}")
        _report_generation(result, output)
        if do_import:
            report = import_membership_records(
                conn,
                [(i, rec) for i, rec in enumerate(result.records, start=1)],
                source_file=str(output),
                import_type="ai_reverse_expansion",
                content_filter=_content_filter(blocklist, no_blocklist, min_zipf),
            )
            _print_report("Импорт кандидатов", report)
    finally:
        conn.close()


@app.command("review-membership-candidates")
def cmd_review_membership_candidates(
    db: DbOption,
    output: OutputOption,
    status: Annotated[str, typer.Option("--status", help="Какие статусы отдать критику")] = "candidate",
    limit: Annotated[int, typer.Option("--limit")] = 100,
    batch_size: Annotated[int, typer.Option("--batch-size")] = 20,
    max_retries: Annotated[int, typer.Option("--max-retries")] = 2,
    provider: ProviderOption = "mock",
    model: ModelOption = None,
    mock_file: MockFileOption = None,
) -> None:
    """Проход C: модель-критик. Ничего в базе не меняет, результат — подсказка человеку."""
    conn = _open(db)
    try:
        statuses = parse_statuses(status)
        llm = _build_provider(provider, model, mock_file)
        result = gen.review_candidates(
            conn,
            llm,
            statuses=statuses,
            limit=limit,
            batch_size=batch_size,
            max_retries=max_retries,
        )
        written = write_jsonl(output, result.records)
        typer.echo(
            f"Вердиктов: {written} | batches ok={result.batches_ok} failed={result.batches_failed}"
        )
        typer.echo("review_status в базе не изменён — это только материал для человека.")
        typer.echo(f"Файл: {output}")
    except (LLMError, ValidationIssue) as exc:
        _fail(str(exc))
    finally:
        conn.close()


# ----------------------------------------------- готовность, конфликты, четвёрки


def _category_meta(path: Path | None) -> dict[str, Any]:
    """Читает ручные оверрайды категорий. Файла нет — работаем без них."""
    target = path or (Path(__file__).resolve().parents[2] / "data" / "seed" / "_category_meta.json")
    if not target.exists():
        return {}
    return json.loads(target.read_text(encoding="utf-8"))


MetaOption = Annotated[
    Path | None,
    typer.Option("--meta", help="Файл ручных оверрайдов (по умолчанию data/seed/_category_meta.json)"),
]


@app.command("derive-readiness")
def cmd_derive_readiness(db: DbOption, meta: MetaOption = None) -> None:
    """Пересчитывает readiness категорий по пулам и отключает те, что не собирают четвёрку."""
    conn = _open(db)
    try:
        loaded = _category_meta(meta)
        curated = dict(loaded.get("curated_only") or {})
        pair_groups = dict(loaded.get("pair_groups") or {})
        with conn:
            summary = readiness.derive(conn, curated)
            pairs_written = 0
            pairs_missing: list[str] = []
            for category_key, groups in pair_groups.items():
                try:
                    written, missing = replace_pair_groups(conn, category_key, groups)
                except RepositoryError as exc:
                    # Файл мета-данных пишется руками и живёт дольше отдельных
                    # категорий. Отсутствующая категория — повод предупредить,
                    # а не уронить пересборку всей базы.
                    pairs_missing.append(str(exc))
                    continue
                pairs_written += written
                pairs_missing.extend(missing)
        blocked = list(
            conn.execute(
                "SELECT category_key, label, readiness_reason FROM categories "
                "WHERE readiness = 'blocked' ORDER BY category_key"
            )
        )
        hard = list(
            conn.execute(
                "SELECT category_key, label, readiness_reason FROM categories "
                "WHERE readiness = 'hard_only' ORDER BY category_key"
            )
        )
    finally:
        conn.close()

    typer.echo("Готовность категорий:")
    for key in ("ready", "constrained", "curated_only", "hard_only", "blocked"):
        typer.echo(f"  {key:14} {summary.get(key, 0)}")
    if pair_groups:
        typer.echo(f"Парных групп записано: {pairs_written}")
    for item in pairs_missing:
        typer.secho(f"  слово пары не найдено: {item}", fg=typer.colors.YELLOW, err=True)
    if blocked:
        typer.echo(f"\nОтключено (status=disabled), четвёрку не собрать — {len(blocked)}:")
        for row in blocked:
            typer.echo(f"  {row['label']} ({row['category_key']}): {row['readiness_reason']}")
    if hard:
        typer.echo(f"\nТолько для сложных уровней — {len(hard)}:")
        for row in hard[:30]:
            typer.echo(f"  {row['label']} ({row['category_key']}): {row['readiness_reason']}")
        if len(hard) > 30:
            typer.echo(f"  ... ещё {len(hard) - 30}")


@app.command("derive-conflicts")
def cmd_derive_conflicts(
    db: DbOption,
    output: Annotated[
        Path | None, typer.Option("--output", help="Куда выгрузить CSV конфликтов")
    ] = None,
    meta: MetaOption = None,
    min_overlap: Annotated[
        int, typer.Option("--min-overlap", help="Минимальное пересечение пулов")
    ] = conflicts.MIN_OVERLAP,
) -> None:
    """Считает пары категорий, которые нельзя ставить в один уровень."""
    conn = _open(db)
    try:
        overlaps = conflicts.find_overlaps(conn, min_overlap)
        rows = conflicts.to_rows(overlaps)
        manual = _category_meta(meta).get("do_not_pair") or []
        for pair in manual:
            rows.append(
                {
                    "category_a": pair[0],
                    "category_b": pair[1],
                    "conflict_type": "do_not_pair",
                    "origin": "manual",
                    "overlap_count": 0,
                    "overlap_words": "",
                    "severity": "P1",
                    "note": "ручное правило из _category_meta.json",
                }
            )

        inserted = updated = skipped = 0
        with conn:
            clear_category_conflicts(conn)
            for row in rows:
                try:
                    item = CategoryConflictInput.model_validate(row)
                    result = upsert_category_conflict(conn, item)
                except (ValidationError, RepositoryError) as exc:
                    skipped += 1
                    typer.secho(f"  пропущено: {exc}", fg=typer.colors.YELLOW, err=True)
                    continue
                if result == "inserted":
                    inserted += 1
                else:
                    updated += 1
    finally:
        conn.close()

    typer.echo(
        f"Конфликтов: derived={len(overlaps)} manual={len(manual)} | "
        f"записано {inserted}, обновлено {updated}, пропущено {skipped}"
    )
    by_severity: dict[str, int] = {}
    for item in overlaps:
        by_severity[item.severity] = by_severity.get(item.severity, 0) + 1
    typer.echo("По серьёзности: " + ", ".join(f"{k}={v}" for k, v in sorted(by_severity.items())))
    typer.echo("\nСамые опасные пересечения:")
    _print_table(
        ["категория A", "категория B", "общих слов"],
        [[i.category_a, i.category_b, str(i.count)] for i in overlaps[:15]],
    )
    if output:
        written = _write_csv(output, rows)
        typer.echo(f"\nCSV: {output} ({written} строк)")


@app.command("build-quartet-candidates")
@app.command("build-quartets")  # прежнее имя: команда осталась совместимой
def cmd_build_quartets(
    db: DbOption,
    output: Annotated[
        Path | None, typer.Option("--output", help="Куда выгрузить CSV четвёрок")
    ] = None,
    per_category: Annotated[
        int, typer.Option("--per-category", help="Сколько четвёрок собирать на категорию")
    ] = quartet_builder.MAX_PER_CATEGORY,
    category: Annotated[
        str | None, typer.Option("--category", help="Только одна категория")
    ] = None,
    pool_cap: Annotated[
        int,
        typer.Option("--pool-cap",
                     help="Сколько слов пула рассматривать. Больше — больше "
                          "четвёрок и дольше перебор"),
    ] = quartet_builder.CANDIDATE_POOL,
    max_shared: Annotated[
        int,
        typer.Option("--max-shared",
                     help="Сколько слов могут делить две четвёрки одного правила"),
    ] = quartet_builder.MAX_SHARED_WORDS,
) -> None:
    """Собирает четвёрки из пулов и проверяет каждую solver'ом единственности."""
    conn = _open(db)
    try:
        built, stats = quartet_builder.build(
            conn, max_per_category=per_category, only_category=category,
            candidate_pool=pool_cap, max_shared_words=max_shared,
        )
        rows = quartet_builder.to_rows(built)
        inserted = updated = skipped = 0
        with conn:
            clear_quartets(conn)
            for row in rows:
                try:
                    item = QuartetInput.model_validate(row)
                    result = upsert_quartet(conn, item)
                except (ValidationError, RepositoryError) as exc:
                    skipped += 1
                    typer.secho(f"  пропущено: {exc}", fg=typer.colors.YELLOW, err=True)
                    continue
                if result == "inserted":
                    inserted += 1
                else:
                    updated += 1
    finally:
        conn.close()

    for key, value in stats.items():
        typer.echo(f"{key}: {value}")
    typer.echo(f"записано в базу: {inserted}, обновлено: {updated}, пропущено: {skipped}")
    typer.echo("Статус четвёрок: auto_validated — solver прошёл, человек не смотрел.")
    if output:
        written = _write_csv(output, rows)
        typer.echo(f"CSV: {output} ({written} строк)")


@app.command("solve-level")
def cmd_solve_level(
    db: DbOption,
    words: Annotated[
        str,
        typer.Option(
            "--words",
            help="Слова уровня через запятую. Значение через решётку: bank#bank_river",
        ),
    ],
    timeout_ms: Annotated[
        int, typer.Option("--timeout-ms", help="Бюджет времени solver'а")
    ] = level_solver.DEFAULT_TIMEOUT_MS,
    explain: Annotated[
        bool, typer.Option("--explain", help="Показать параметры запуска и хеш входа")
    ] = False,
) -> None:
    """Exact-cover проверка полного уровня. Принимает только при solution_count == 1."""
    conn = _open(db)
    try:
        tokens = level_solver.parse_tokens(words)
        index = level_solver.load_memberships(conn)
        structures = structured.load(conn)
        result = level_solver.solve_level(tokens, index, structures, timeout_ms=timeout_ms)
    finally:
        conn.close()

    typer.echo(
        f"Слов: {len(tokens)} | исход: {result.outcome} | "
        f"разбиений: {result.solution_count} | {result.duration_ms} мс"
    )
    for number, solution in enumerate(result.solutions, start=1):
        typer.echo(f"\nРазбиение {number}:")
        for category_key, group in sorted(solution):
            typer.echo(f"  {category_key}: {', '.join(group)}")
    if explain:
        typer.echo(f"\nsolver: {result.solver_version}")
        typer.echo(f"input_hash: {result.input_hash}")
        typer.echo(f"параметры: {json.dumps(result.parameters, ensure_ascii=False)}")
        typer.echo(f"узлов перебора: {result.nodes_visited}")

    if result.unique:
        typer.secho(f"\nОК: {result.reason}", fg=typer.colors.GREEN)
    else:
        typer.secho(f"\nОтклонён: {result.reason}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


ScoringConfigOption = Annotated[
    Path | None, typer.Option("--config", help="Конфиг формул (по умолчанию data/content/)")
]
ScoringVersionOption = Annotated[
    str | None,
    typer.Option("--scoring-version", help="Записать эту версию формул вместо конфиговой"),
]
DryRunOption = Annotated[bool, typer.Option("--dry-run", help="Не сохранять в базу")]


def _scoring_config(config: Path | None, version: str | None, keys: tuple[str, ...]) -> dict:
    try:
        values = scoring.load_config(config)
    except scoring.flat_config.ConfigError as exc:
        _fail(str(exc))
        raise
    if version:
        try:
            for key in keys:
                values[key] = float(version)
        except ValueError:
            _fail(f"--scoring-version должен быть числом, получено {version!r}")
    return values


def _run_scoring(
    db: Path,
    config: Path | None,
    version: str | None,
    dry_run: bool,
    output: Path | None,
    steps: tuple[str, ...],
) -> None:
    """Общий запуск любого набора шагов пересчёта: один код на четыре команды."""
    keys = {
        "words": ("word_scoring_version",),
        "labels": ("label_scoring_version",),
        "quartets": ("quartet_scoring_version",),
    }
    values = _scoring_config(config, version, tuple(k for s in steps for k in keys[s]))
    conn = _open(db)
    summary: dict[str, Any] = {}
    try:
        # Порядок обязателен: агрегаты четвёрки считаются из свежих оценок
        # слов и названий, иначе получится смесь двух версий формул.
        with conn:
            if "words" in steps:
                _count, stats = scoring.score_words(conn, values)
                summary["слова"] = stats
            if "labels" in steps:
                _count, stats = scoring.score_labels(conn, values)
                summary["названия"] = stats
            if "quartets" in steps:
                _count, stats = scoring.score_quartets(conn, values)
                summary["четвёрки"] = stats
            if dry_run:
                conn.rollback()
    finally:
        conn.close()

    for section, stats in summary.items():
        typer.echo(f"{section}:")
        for key, value in stats.items():
            typer.echo(f"    {key}: {value}")
    if dry_run:
        typer.secho("--dry-run: в базу ничего не записано", fg=typer.colors.YELLOW)
    if output:
        baseline.write_json(output, summary)
        typer.echo(f"JSON: {output}")


@app.command("score-words")
def cmd_score_words(
    db: DbOption,
    config: ScoringConfigOption = None,
    scoring_version: ScoringVersionOption = None,
    dry_run: DryRunOption = False,
    output: Annotated[Path | None, typer.Option("--output", help="Сводка в JSON")] = None,
) -> None:
    """Пересчитывает метрики слов: длина, вместимость, знакомость, новизна, доступность."""
    _run_scoring(db, config, scoring_version, dry_run, output, ("words",))


@app.command("derive-rule-types")
def cmd_derive_rule_types(db: DbOption) -> None:
    """Проставляет тип принципа группировки: таксономия, части, хаб, структура.

    Тип выводится из уже принятого relation_type, а не угадывается. Шаг нужен
    в каждой сборке: миграция отрабатывает на пустой базе, категории приезжают
    позже.
    """
    conn = _open(db)
    try:
        with conn:
            applied = ensure_rule_types(conn)
    finally:
        conn.close()
    _print_table(
        ["тип правила", "правил"],
        [[name, str(count)] for name, count in sorted(applied.items())],
    )


@app.command("derive-labels")
def cmd_derive_labels(db: DbOption) -> None:
    """Заводит основную надпись каждому правилу группировки.

    Надпись — отдельная сущность от правила: одна надпись обслуживает разные
    принципы (MUSIC — и жанры, и инструменты). Но правило без единой допустимой
    надписи показать игроку нечем, поэтому связка с собственным именем правила
    создаётся всегда.
    """
    conn = _open(db)
    try:
        with conn:
            labels, links = ensure_primary_labels(conn)
    finally:
        conn.close()
    typer.echo(f"Надписей заведено: {labels}, связок правило-надпись: {links}")


@app.command("score-labels")
def cmd_score_labels(
    db: DbOption,
    config: ScoringConfigOption = None,
    scoring_version: ScoringVersionOption = None,
    dry_run: DryRunOption = False,
    output: Annotated[Path | None, typer.Option("--output", help="Сводка в JSON")] = None,
) -> None:
    """Пересчитывает качество названий категорий."""
    _run_scoring(db, config, scoring_version, dry_run, output, ("labels",))


@app.command("score-quartets")
def cmd_score_quartets(
    db: DbOption,
    config: ScoringConfigOption = None,
    scoring_version: ScoringVersionOption = None,
    dry_run: DryRunOption = False,
    output: Annotated[Path | None, typer.Option("--output", help="Сводка в JSON")] = None,
) -> None:
    """Пересчитывает агрегаты четвёрок из текущих оценок слов и названий."""
    _run_scoring(db, config, scoring_version, dry_run, output, ("quartets",))


@app.command("score-all")
def cmd_score_all(
    db: DbOption,
    config: ScoringConfigOption = None,
    scoring_version: ScoringVersionOption = None,
    dry_run: DryRunOption = False,
    output: Annotated[Path | None, typer.Option("--output", help="Сводка в JSON")] = None,
) -> None:
    """Полный пересчёт рейтингов: слова, названия, четвёрки — в этом порядке."""
    _run_scoring(db, config, scoring_version, dry_run, output, ("words", "labels", "quartets"))


def _explain_table(title: str, total: float, parts: dict[str, float]) -> None:
    typer.echo(f"{title}: {round(total, 4)}")
    _print_table(
        ["компонент", "вклад"],
        [[name, f"{value:+.4f}"] for name, value in parts.items()],
    )


@app.command("explain-word-score")
def cmd_explain_word_score(
    db: DbOption,
    word: Annotated[str, typer.Option("--word", help="Слово в любом написании")],
    config: ScoringConfigOption = None,
) -> None:
    """Разбирает оценку слова по компонентам, а не показывает одно число."""
    values = _scoring_config(config, None, ())
    conn = _open(db)
    try:
        rows = list(
            conn.execute(
                """
                SELECT ws.*, w.normalized AS normalized, w.familiarity_score AS familiarity,
                       s.sense_key AS sense_key, s.definition AS definition
                  FROM word_scores ws
                  JOIN words w ON w.id = ws.word_id
                  LEFT JOIN word_senses s ON s.id = ws.sense_id
                 WHERE w.normalized = ?
                 ORDER BY ws.sense_id
                """,
                (normalization.normalize_word(word),),
            )
        )
    finally:
        conn.close()

    if not rows:
        _fail(f"Оценок для {word!r} нет. Сначала выполните: score-words --db …")
    for row in rows:
        header = row["display_text"] + (f" ({row['sense_key']})" if row["sense_key"] else "")
        typer.secho(f"\n{header}", fg=typer.colors.CYAN)
        if row["definition"]:
            typer.echo(f"  значение: {row['definition']}")
        typer.echo(
            f"  символов {row['char_count']}, слов {row['token_count']}, "
            f"версия формул {row['scoring_version']}"
        )
        familiarity = row["familiarity"]
        typer.echo(
            "  знакомость: "
            + ("неизвестна" if familiarity is None else f"{familiarity:.4f}")
        )
        access = scoring.accessibility(
            familiarity=familiarity,
            display_width_score=row["display_width_score"],
            char_count=row["char_count"],
            spelling_difficulty_score=row["spelling_difficulty_score"],
            config=values,
        )
        _explain_table("  доступность", access.score, access.parts)
        typer.echo(
            f"  новизна {row['novelty_score']}, неоднозначность {row['ambiguity_score']}, "
            f"сложность написания {row['spelling_difficulty_score']}, "
            f"вместимость {row['display_width_score']}"
        )
        typer.echo(f"  общий рейтинг слова: {row['word_quality_score']}")


@app.command("explain-label-score")
def cmd_explain_label_score(
    db: DbOption,
    category: Annotated[str, typer.Option("--category", help="category_key")],
    config: ScoringConfigOption = None,
) -> None:
    """Разбирает оценку названия категории по компонентам."""
    values = _scoring_config(config, None, ())
    conn = _open(db)
    try:
        row = conn.execute(
            """
            SELECT ls.*, c.label AS label, c.category_key AS category_key,
                   (SELECT COUNT(*) FROM memberships m
                     WHERE m.category_id = c.id
                       AND m.review_status IN ('approved','alternative','hard_only')) AS pool
              FROM category_label_scores ls
              JOIN categories c ON c.id = ls.category_id
             WHERE c.category_key = ?
            """,
            (category,),
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        _fail(f"Оценок для категории {category!r} нет. Сначала выполните: score-labels --db …")
    typer.secho(f"\n{row['label']} ({row['category_key']})", fg=typer.colors.CYAN)
    typer.echo(
        f"  символов {row['label_char_count']}, слов {row['label_token_count']}, "
        f"пул {row['pool']}, версия формул {row['scoring_version']}"
    )
    for title, explained in (
        ("  естественность", scoring.label_naturalness(row["label"])),
        ("  ясность", scoring.label_clarity(row["label"])),
        ("  объясняет четвёрку задним числом",
         scoring.label_retrospective_fit(row["label"], int(row["pool"]))),
        ("  приятность раскрытия", scoring.label_reveal_satisfaction(row["label"])),
        ("  конкретность (диагностика, в качество не входит)",
         scoring.label_specificity(row["label"], int(row["pool"]))),
    ):
        _explain_table(title, explained.score, explained.parts)
    typer.echo(
        f"  охват надписи: {scoring.label_scope(row['label'], int(row['pool']))} "
        "(характеристика, не штраф)"
    )
    quality = scoring.label_quality(
        naturalness=row["label_naturalness_score"],
        clarity=row["label_clarity_score"],
        retrospective_fit=scoring.label_retrospective_fit(
            row["label"], int(row["pool"])).score,
        reveal_satisfaction=scoring.label_reveal_satisfaction(row["label"]).score,
        display_width_score=row["label_display_width_score"],
        familiarity=row["label_familiarity_score"],
        config=values,
    )
    _explain_table("  итог качества названия", quality.score, quality.parts)


@app.command("explain-quartet-score")
def cmd_explain_quartet_score(
    db: DbOption,
    quartet: Annotated[
        str, typer.Option("--quartet-id", help="quartet_key или числовой id")
    ],
    config: ScoringConfigOption = None,
) -> None:
    """Разбирает оценку четвёрки: связность, ясность, интересность, качество."""
    values = _scoring_config(config, None, ())
    conn = _open(db)
    try:
        row = conn.execute(
            "SELECT q.*, c.category_key AS category_key, c.label AS label "
            "FROM quartets q JOIN categories c ON c.id = q.category_id "
            "WHERE q.quartet_key = ? OR CAST(q.id AS TEXT) = ?",
            (quartet, quartet),
        ).fetchone()
        if row is None:
            _fail(f"Четвёрка {quartet!r} не найдена")
        members = list(
            conn.execute(
                """
                SELECT COALESCE(s.display_text, w.text) AS display,
                       w.familiarity_score AS familiarity, m.fit_score AS fit,
                       ws.accessibility_score AS accessibility, ws.novelty_score AS novelty,
                       ws.ambiguity_score AS ambiguity, ws.char_count AS char_count
                  FROM quartet_words qw
                  JOIN words w ON w.id = qw.word_id
                  LEFT JOIN word_senses s ON s.id = qw.sense_id
                  LEFT JOIN word_scores ws ON ws.word_id = qw.word_id
                       AND COALESCE(ws.sense_id, 0) = COALESCE(qw.sense_id, 0)
                  LEFT JOIN memberships m ON m.word_id = qw.word_id
                       AND m.category_id = ?
                       AND COALESCE(m.sense_id, 0) = COALESCE(qw.sense_id, 0)
                 WHERE qw.quartet_id = ? ORDER BY qw.slot
                """,
                (row["category_id"], row["id"]),
            )
        )
    finally:
        conn.close()

    typer.secho(f"\n{row['quartet_key']} — {row['label']}", fg=typer.colors.CYAN)
    _print_table(
        ["слово", "знакомость", "доступность", "новизна", "неоднозн.", "связь", "симв."],
        [
            [
                str(m["display"]),
                "—" if m["familiarity"] is None else f"{m['familiarity']:.2f}",
                "—" if m["accessibility"] is None else f"{m['accessibility']:.2f}",
                "—" if m["novelty"] is None else f"{m['novelty']:.2f}",
                "—" if m["ambiguity"] is None else f"{m['ambiguity']:.2f}",
                "—" if m["fit"] is None else f"{m['fit']:.2f}",
                str(m["char_count"] or len(str(m["display"]))),
            ]
            for m in members
        ],
    )
    fits = [m["fit"] for m in members if m["fit"] is not None]
    access = [m["accessibility"] for m in members if m["accessibility"] is not None]
    cohesion = scoring.cohesion(fits, values)
    _explain_table("связность (штраф за слабое звено)", cohesion.score, cohesion.parts)
    interest = scoring.quartet_interest(
        novelty_scores=[m["novelty"] or 0.0 for m in members],
        accessibility_scores=access,
        cohesion_score=cohesion.score,
        label_quality_score=row["label_quality_score"] or 0.0,
        rare_count=sum(
            1
            for m in members
            if m["familiarity"] is not None
            and m["familiarity"] < values["word_rare_familiarity"]
        ),
        config=values,
    )
    _explain_table("интересность", interest.score, interest.parts)
    quality = scoring.quartet_quality(
        cohesion_score=cohesion.score,
        avg_accessibility=sum(access) / len(access) if access else 0.0,
        clarity_score=row["quartet_clarity_score"] or 0.0,
        label_quality_score=row["label_quality_score"] or 0.0,
        config=values,
    )
    _explain_table("итог качества четвёрки", quality.score, quality.parts)
    typer.echo(
        f"\nверсия формул {row['scoring_version']}, "
        f"ясность {row['quartet_clarity_score']}, сложность {row['difficulty']}"
    )
    typer.secho(
        "Высокий рейтинг не значит, что четвёрку безопасно ставить рядом с любой "
        "другой: это проверяет только solver полного уровня.",
        fg=typer.colors.YELLOW,
    )


@app.command("validate-quartets")
def cmd_validate_quartets(
    db: DbOption,
    show: Annotated[int, typer.Option("--show", help="Сколько примеров показать")] = 10,
) -> None:
    """Перепроверяет четвёрки: состав, значения, структура, локальная однозначность."""
    conn = _open(db)
    try:
        structures = structured.load(conn)
        pools = solver.category_pools(conn)
        rows = list(
            conn.execute(
                """
                SELECT q.id AS id, q.quartet_key AS quartet_key, q.validation_state AS state,
                       q.origin AS origin, c.category_key AS category_key,
                       GROUP_CONCAT(w.normalized) AS words, COUNT(qw.id) AS n
                  FROM quartets q
                  JOIN categories c     ON c.id = q.category_id
                  LEFT JOIN quartet_words qw ON qw.quartet_id = q.id
                  LEFT JOIN words w     ON w.id = qw.word_id
                 GROUP BY q.id ORDER BY q.quartet_key
                """
            )
        )
        problems: list[tuple[str, str]] = []
        # Четвёрки записи референса не выводятся из пулов, а приходят из
        # fixture. Их пересечение с чужим пулом — свойство оригинала, а не наш
        # брак: в игре у токена есть авторский дом. Считаем отдельно.
        fixture_overlaps: list[tuple[str, str]] = []
        checked = 0
        for row in rows:
            if row["state"] in ("disabled", "invalid"):
                continue
            checked += 1
            words = (row["words"] or "").split(",") if row["words"] else []
            if int(row["n"]) != 4:
                problems.append((row["quartet_key"], f"слов {row['n']}, нужно 4"))
                continue
            if len(set(words)) != 4:
                problems.append((row["quartet_key"], "в четвёрке повторяется слово"))
                continue
            allowed, reason = structures.allows(row["category_key"], frozenset(words))
            if not allowed:
                problems.append((row["quartet_key"], f"структура категории: {reason}"))
                continue
            result = solver.quartet_locally_unique(
                conn, row["category_key"], words, pools=pools
            )
            if not result.unique:
                target = (
                    fixture_overlaps
                    if row["origin"] == "reference_backfill"
                    else problems
                )
                target.append((row["quartet_key"], result.reason))
    finally:
        conn.close()

    typer.echo(f"Проверено четвёрок: {checked} | с проблемами: {len(problems)}")
    _print_table(
        ["четвёрка", "проблема"],
        [[key, _truncate(reason, 70)] for key, reason in problems[:show]],
    )
    if fixture_overlaps:
        typer.echo(
            f"\nЧетвёрки записи референса с пересечением пулов: {len(fixture_overlaps)}. "
            "Это не брак: у токена есть авторский дом, однозначность меряется "
            "отрывом разбиения (assess-levels)."
        )
        for key, reason in fixture_overlaps[:show]:
            typer.echo(f"        - {key}: {_truncate(reason, 70)}")
    if problems:
        raise typer.Exit(code=1)
    typer.secho("Все действующие четвёрки валидны.", fg=typer.colors.GREEN)


@app.command("generate-level-candidates")
def cmd_generate_level_candidates(
    db: DbOption,
    count: Annotated[int, typer.Option("--limit", help="Сколько уровней собрать")] = 5,
    categories: Annotated[
        int,
        typer.Option("--categories",
                     help="Категорий в уровне. 0 — по записи оригинала: "
                          "5 на первом уровне, 12 на седьмом, 7 на пятнадцатом"),
    ] = level_generator.DEFAULT_CATEGORY_COUNT,
    seed: Annotated[int, typer.Option("--seed", help="Зерно случайности")] = 20260731,
    tier: Annotated[str, typer.Option("--tier", help="normal или hard")] = "normal",
    target: Annotated[
        float | None, typer.Option("--target-difficulty", help="Целевая сложность 1-10")
    ] = None,
    profile: Annotated[
        str | None,
        typer.Option("--profile",
                     help="Профиль качества: easy_accessible / accessible_fun / "
                          "hard_knowledge, либо auto — по номеру уровня, как в записи"),
    ] = None,
    profiles_config: Annotated[
        Path | None, typer.Option("--profiles-config", help="Файл профилей генерации")
    ] = None,
    config: Annotated[
        Path | None, typer.Option("--config", help="Конфиг cooldown")
    ] = None,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Только показать, в базу не писать")
    ] = False,
    explain: Annotated[
        bool, typer.Option("--explain", help="Разложить сложность по компонентам")
    ] = False,
    meta: Annotated[
        bool,
        typer.Option("--meta/--no-meta",
                     help="Собирать мета-связи: собранная группа оставляет пузырь "
                          "для другой группы уровня"),
    ] = True,
    meta_links: Annotated[
        int | None,
        typer.Option("--meta-links",
                     help="Сколько мета-связей просить на уровень. "
                          "По умолчанию — профиль композиции по номеру уровня"),
    ] = None,
    key_prefix: Annotated[
        str,
        typer.Option("--key-prefix",
                     help="Префикс ключей уровней. Отдельный пакет под своим "
                          "префиксом не затирается дымовым прогоном сборки"),
    ] = "L",
    skip_reference_gate: Annotated[
        bool,
        typer.Option("--skip-reference-gate",
                     help="Собрать уровни, не проверяя воспроизводимость референса. "
                          "Только для отладки: результат нельзя считать контентом"),
    ] = False,
) -> None:
    """Собирает уровни из готовых четвёрок и проверяет каждый solver'ом целиком.

    Перед сборкой обязательно проходит Reference Reproduction Gate: пока система
    не может повторить то, что мы точно видели, её способность создавать «лучше»
    не подтверждена.
    """
    conn = _open(db)
    if not skip_reference_gate:
        try:
            reference_coverage.require_gate(conn)
        except (reference_coverage.ReferenceGateError,
                reference_fixtures.FixtureError) as exc:
            conn.close()
            _fail(str(exc))
            raise
        typer.secho("Reference gate пройден.", fg=typer.colors.GREEN)
    try:
        try:
            cooldown_config = cooldown.load_config(config)
        except cooldown.ConfigError as exc:
            _fail(str(exc))
            return
        chosen_profile = None
        auto_profile = profile == "auto"
        if profile and not auto_profile:
            try:
                chosen_profile = profiles.get(profile, profiles_config)
            except profiles.flat_config.ConfigError as exc:
                _fail(str(exc))
                return
        levels, stats = level_generator.generate(
            conn,
            count=count,
            category_count=categories or None,
            seed=seed,
            tier=tier,
            target_difficulty=target,
            config=cooldown_config,
            profile=chosen_profile,
            rare_familiarity=scoring.load_config(None)["word_rare_familiarity"],
            use_meta=meta,
            meta_target=meta_links,
            key_prefix=key_prefix,
            auto_profile=auto_profile,
            profiles_config=profiles_config,
        )
        saved = 0
        if not dry_run and levels:
            with conn:
                run_id = level_generator.record_run(
                    conn,
                    run_kind="generate-level-candidates",
                    parameters={
                        "count": count,
                        "categories": categories,
                        "tier": tier,
                        "target_difficulty": target,
                        "profile": profile,
                        "meta": meta,
                        "meta_links": meta_links,
                    },
                    records_out=len(levels),
                    random_seed=seed,
                    source_commit=_git_commit(),
                )
                saved = level_generator.save(conn, levels, run_id=run_id)
    finally:
        conn.close()

    for key, value in stats.items():
        typer.echo(f"{key}: {value}")
    _print_table(
        ["уровень", "статус", "разбиений", "сложность", "мета", "категории"],
        [
            [
                level.level_key,
                level.status,
                str(level.solver.solution_count),
                str(level.difficulty.total_score),
                str(len(level.meta_links)),
                _truncate(", ".join(g.category_key for g in level.groups), 40),
            ]
            for level in levels
        ],
    )
    for level in levels:
        for link in level.meta_links:
            typer.echo(
                f"  {level.level_key} мета: «{link.source_label}» выпускает "
                f"«{link.token_display}» для «{link.consumer_key}»"
            )
        if explain:
            typer.echo(f"\n{level.level_key}: {level.difficulty.short_explanation}")
            for name, value in level.difficulty.component_scores.items():
                if value:
                    typer.echo(f"    {name}: +{value}")
        for reason in level.reject_reasons:
            typer.secho(f"  {level.level_key} отклонён — {reason}", fg=typer.colors.YELLOW)
        for violation in level.cooldown_violations:
            typer.secho(f"  {level.level_key} cooldown — {violation}", fg=typer.colors.YELLOW)

    if dry_run:
        typer.echo("\n--dry-run: в базу ничего не записано")
    else:
        typer.echo(f"\nЗаписано уровней: {saved}")


@app.command("validate-levels")
def cmd_validate_levels(
    db: DbOption,
    show: Annotated[int, typer.Option("--show", help="Сколько примеров показать")] = 10,
) -> None:
    """Проверяет сохранённые уровни: покрытие, единственность, повторы, политика."""
    conn = _open(db)
    try:
        results = integrity.run_level_checks(conn)
    finally:
        conn.close()

    failed = [r for r in results if r.failed]
    for result in results:
        mark = "OK  " if result.ok else ("СТОП" if result.severity == "blocker" else "ВНИМ")
        color = (
            typer.colors.GREEN
            if result.ok
            else (typer.colors.RED if result.severity == "blocker" else typer.colors.YELLOW)
        )
        typer.secho(f"{mark}  {result.question}: {result.count}", fg=color)
        for example in result.examples[:show]:
            typer.echo(f"        - {example}")
    if failed:
        typer.secho(f"\nУровни не готовы: провалено {len(failed)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
    typer.secho("\nВсе проверки уровней пройдены.", fg=typer.colors.GREEN)


@app.command("export-level-review-pack")
def cmd_export_level_review_pack(
    db: DbOption,
    output: Annotated[
        Path, typer.Option("--output", help="Каталог пакета")
    ] = Path("data/content/level_review"),
    limit: Annotated[int | None, typer.Option("--limit", help="Сколько уровней выгрузить")] = None,
    statuses: Annotated[
        str, typer.Option("--statuses", help="Статусы уровней через запятую")
    ] = "solver_valid,candidate",
) -> None:
    """Выгружает уровни на приёмку: отчёт, JSON и бланк решений."""
    conn = _open(db)
    try:
        wanted = tuple(s.strip() for s in statuses.split(",") if s.strip())
        packages = level_review.build(conn, statuses=wanted, limit=limit)
        if not packages:
            typer.secho("Уровней в этих статусах нет.", fg=typer.colors.YELLOW)
            return
        markdown = level_review.write_markdown(output / "LEVELS.md", packages)
        data = level_review.write_json(output / "levels.json", packages)
        decisions = level_review.write_decisions_template(
            output / "level_decisions.csv", packages
        )
        # Пометка «ушёл человеку» ставится в базе: иначе непонятно, что уже отдано.
        with conn:
            conn.execute(
                "UPDATE level_instances SET status = 'review_pending', updated_at = ? "
                "WHERE status = 'solver_valid'",
                (utc_now(),),
            )
    finally:
        conn.close()

    typer.echo(f"Уровней в пакете: {len(packages)}")
    typer.echo(f"  отчёт:   {markdown}")
    typer.echo(f"  данные:  {data}")
    typer.echo(f"  решения: {decisions}")
    typer.echo("Заполните колонку decision (accept / reject / needs_changes) и примените:")
    typer.echo(f"  word-content apply-level-decisions --db {db} --input {decisions}")


@app.command("apply-level-decisions")
def cmd_apply_level_decisions(
    db: DbOption,
    input: InputOption,
) -> None:
    """Применяет решения по уровням и точечно возвращает причины в базу."""
    conn = _open(db)
    try:
        if not input.exists():
            _fail(f"Файл решений не найден: {input}")
        with conn:
            report = level_review.apply_decisions(conn, input)
    finally:
        conn.close()

    typer.echo(f"Применено решений: {report.applied}, пропущено пустых: {report.skipped}")
    for note in report.feedback:
        typer.echo(f"  {note}")
    for error in report.errors:
        typer.secho(f"  {error}", fg=typer.colors.YELLOW, err=True)
    if report.errors:
        raise typer.Exit(code=1)


@app.command("dedupe-concepts")
def cmd_dedupe_concepts(
    db: DbOption,
    output: Annotated[
        Path | None, typer.Option("--output", help="Куда выгрузить разбор пар в CSV")
    ] = None,
    apply: Annotated[
        bool,
        typer.Option("--apply", help="Свести exact_duplicate и alias к одному принципу"),
    ] = False,
    show: Annotated[int, typer.Option("--show", help="Сколько пар показать")] = 15,
) -> None:
    """Ищет категории, которые на самом деле один принцип под разными вывесками."""
    conn = _open(db)
    try:
        pairs = dedupe.find(conn)
        by_verdict: dict[str, int] = {}
        for pair in pairs:
            by_verdict[pair.verdict] = by_verdict.get(pair.verdict, 0) + 1
        merged, notes = (0, [])
        if apply:
            with conn:
                merged, notes = dedupe.merge_into_concepts(conn, pairs)
        rows = dedupe.to_rows(pairs)
    finally:
        conn.close()

    typer.echo(f"Пар найдено: {len(pairs)}")
    for verdict, count in sorted(by_verdict.items()):
        typer.echo(f"  {verdict}: {count}")
    _print_table(
        ["вердикт", "категория A", "категория B", "общих", "причина"],
        [
            [p.verdict, p.category_a, p.category_b, str(p.shared_words), _truncate(p.reason, 50)]
            for p in pairs[:show]
        ],
    )
    if apply:
        typer.echo(f"\nСведено к одному принципу: {merged}")
        for note in notes[:show]:
            typer.echo(f"  {note}")
        typer.echo("parent_child не сливается: родитель и ребёнок — разные категории.")
    if output:
        written = _write_csv(output, rows)
        typer.echo(f"\nCSV: {output} ({written} строк)")


@app.command("migrate-content-schema")
def cmd_migrate_content_schema(
    db: DbOption,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Показать шаги, ничего не применяя")
    ] = False,
) -> None:
    """Докатывает недостающие шаги схемы. Повторный запуск ничего не делает."""
    conn = _open(db)
    try:
        version = migrations.current_version(conn)
        applied = migrations.migrate(conn, dry_run=dry_run)
        after = migrations.current_version(conn)
    finally:
        conn.close()

    if not applied:
        typer.secho(f"Схема актуальна: версия {version}", fg=typer.colors.GREEN)
        return
    for migration, changes in applied:
        typer.echo(f"{migration.version:03d} {migration.name}: {migration.description}")
        for change in changes:
            typer.echo(f"    {change}")
    typer.echo(f"\nВерсия схемы: {version} -> {after}")


@app.command("sense-gaps")
def cmd_sense_gaps(
    db: DbOption,
    output: Annotated[
        Path | None, typer.Option("--output", help="Куда выгрузить очередь на разведение значений")
    ] = None,
    show: Annotated[int, typer.Option("--show", help="Сколько строк показать")] = 20,
) -> None:
    """Ищет слова, которым нужны дополнительные значения. Ничего не меняет в базе."""
    conn = _open(db)
    try:
        not_homonyms = sense_gaps.load_not_homonyms(
            Path(__file__).resolve().parents[2] / "data" / "seed" / "_not_homonyms.txt"
        )
        gaps = sense_gaps.find(conn, not_homonyms=not_homonyms)
    finally:
        conn.close()

    by_priority: dict[str, int] = {}
    for gap in gaps:
        by_priority[gap.priority] = by_priority.get(gap.priority, 0) + 1
    typer.echo(f"Слов, которым нужны значения: {len(gaps)}")
    typer.echo("По приоритету: " + ", ".join(f"{k}={v}" for k, v in sorted(by_priority.items())))
    _print_table(
        ["приоритет", "слово", "категорий", "тем", "темы"],
        [
            [g.priority, g.word, str(g.category_count), str(g.theme_count),
             _truncate(", ".join(g.themes), 46)]
            for g in gaps[:show]
        ],
    )
    if output:
        written = _write_csv(output, sense_gaps.to_rows(gaps))
        typer.echo(f"\nОчередь: {output} ({written} строк)")


@app.command("baseline-report")
def cmd_baseline_report(
    db: DbOption,
    output: Annotated[
        Path | None, typer.Option("--output", help="Куда сохранить снимок метрик в JSON")
    ] = None,
    compare: Annotated[
        Path | None, typer.Option("--compare", help="JSON предыдущего снимка: показать diff")
    ] = None,
) -> None:
    """Снимок метрик базы. С --compare печатает изменения относительно прошлого снимка."""
    conn = _open(db)
    try:
        report = baseline.collect(conn)
    finally:
        conn.close()

    typer.echo(baseline.render_text(report))
    if output:
        path = baseline.write_json(output, report)
        typer.echo(f"\nJSON: {path}")
    if compare:
        if not compare.exists():
            _fail(f"Файл для сравнения не найден: {compare}")
        previous = json.loads(compare.read_text(encoding="utf-8"))
        changes = baseline.diff(previous, report)
        typer.echo(f"\nИзменений относительно {compare}: {len(changes)}")
        _print_table(
            ["метрика", "было", "стало"],
            [[key, str(old), str(new)] for key, old, new in changes],
        )


@app.command("check-integrity")
def cmd_check_integrity(
    db: DbOption,
    show: Annotated[int, typer.Option("--show", help="Сколько примеров показывать")] = 5,
) -> None:
    """Критерии приёмки из аудита. Ненулевой код возврата, если база не готова."""
    conn = _open(db)
    try:
        results = integrity.run_all(conn)
    finally:
        conn.close()

    failed = [r for r in results if r.failed]
    for result in results:
        if result.severity == "blocker":
            mark = "OK  " if result.ok else "СТОП"
            color = typer.colors.GREEN if result.ok else typer.colors.RED
        elif result.severity == "warning":
            mark = "OK  " if result.ok else "ВНИМ"
            color = typer.colors.GREEN if result.ok else typer.colors.YELLOW
        else:
            mark, color = "ИНФО", typer.colors.BLUE
        typer.secho(f"{mark}  {result.question}: {result.count}", fg=color)
        if result.note and not result.ok:
            typer.echo(f"        {result.note}")
        for example in result.examples[:show]:
            typer.echo(f"        - {example}")
        if len(result.examples) > show:
            typer.echo(f"        ... ещё {len(result.examples) - show}")

    if failed:
        typer.secho(
            f"\nБаза не готова: провалено проверок {len(failed)}", fg=typer.colors.RED, err=True
        )
        raise typer.Exit(code=1)
    typer.secho("\nВсе блокирующие проверки пройдены.", fg=typer.colors.GREEN)


@app.command("stamp-version")
def cmd_stamp_version(
    db: DbOption,
    content_version: Annotated[
        str, typer.Option("--content-version", help="Версия контента, например 2026.07.31")
    ],
) -> None:
    """Записывает версию схемы и контента, commit и хеши источников в schema_meta."""
    conn = _open(db)
    try:
        data = Path(__file__).resolve().parents[2] / "data"
        meta: dict[str, str] = {
            "schema_version": str(conn.execute("PRAGMA user_version").fetchone()[0]),
            "content_version": content_version,
            "git_commit": _git_commit(),
            "built_at": utc_now(),
            "wordfreq_version": _package_version("wordfreq"),
        }
        for name in ("categories.jsonl", "membership_candidates.jsonl", "review_decisions.csv"):
            path = data / name
            if path.exists():
                meta[f"sha256_{name}"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with conn:
            set_schema_meta(conn, meta)
    finally:
        conn.close()

    for key, value in meta.items():
        typer.echo(f"{key}: {value}")


def _git_commit() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=Path(__file__).resolve().parents[4],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def _package_version(name: str) -> str:
    try:
        from importlib.metadata import version

        return version(name)
    except Exception:
        return "not installed"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return 0
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


@app.command("rebuild-all")
def cmd_rebuild_all(
    content_version: Annotated[
        str | None,
        typer.Option("--content-version", help="Версия контента; по умолчанию текущая дата UTC"),
    ] = None,
) -> None:
    """Полная пересборка базы из текстовых источников.

    Команда сознательно не повторяет шаги, а запускает `scripts/rebuild_all.sh`.
    Порядок сборки описан там один раз: две копии одного порядка неизбежно
    разъезжаются, и тогда «пересобрал через CLI» и «пересобрал скриптом» дают
    разные базы.
    """
    root = Path(__file__).resolve().parents[2]
    script = root / "scripts" / "rebuild_all.sh"
    if not script.exists():
        _fail(f"Скрипт пересборки не найден: {script}")
    env = dict(os.environ)
    if content_version:
        env["CONTENT_VERSION"] = content_version
    result = subprocess.run(["bash", str(script)], cwd=root, env=env, check=False)
    if result.returncode != 0:
        raise typer.Exit(code=result.returncode)


@app.command("show-runs")
def cmd_show_runs(
    db: DbOption,
    limit: Annotated[int, typer.Option("--limit")] = 10,
) -> None:
    """Последние запуски импорта и генерации (аудит воспроизводимости)."""
    conn = _open(db)
    try:
        imports = list(
            conn.execute(
                "SELECT * FROM import_runs ORDER BY id DESC LIMIT ?", (limit,)
            )
        )
        generations = list(
            conn.execute(
                "SELECT id, generation_type, model, prompt_version, status, created_at "
                "FROM generation_runs ORDER BY id DESC LIMIT ?",
                (limit,),
            )
        )
    finally:
        conn.close()

    typer.echo("import_runs:")
    _print_table(
        ["id", "type", "file", "total", "ins", "upd", "rej", "created"],
        [
            [
                str(row["id"]),
                row["import_type"],
                _truncate(row["source_file"], 40),
                str(row["records_total"]),
                str(row["records_inserted"]),
                str(row["records_updated"]),
                str(row["records_rejected"]),
                row["created_at"],
            ]
            for row in imports
        ],
    )
    typer.echo("\ngeneration_runs:")
    _print_table(
        ["id", "type", "model", "prompt", "status", "created"],
        [
            [
                str(row["id"]),
                row["generation_type"],
                row["model"],
                row["prompt_version"],
                row["status"],
                row["created_at"],
            ]
            for row in generations
        ],
    )


# -------------------------------------------------------------- воспроизведение референса


ReferenceInputOption = Annotated[
    Path | None,
    typer.Option("--input", help="Запись уровней референса (по умолчанию "
                                 "reference/video-levels-20.json в корне репозитория)"),
]
MaxLevelOption = Annotated[
    int | None, typer.Option("--max-level", help="Считать только уровни до этого номера")
]
OverridesOption = Annotated[
    Path | None,
    typer.Option("--overrides",
                 help="CSV курируемых решений по группам записи "
                      "(level,group_index,decision,rule_key,rule_type,note)"),
]


def _default_overrides_path() -> Path:
    return reference_import.default_overrides_path()


def _default_sense_choices_path() -> Path:
    return reference_import.default_sense_choices_path()


def _load_reference(input: Path | None, overrides: Path | None):
    try:
        fixtures = reference_fixtures.load(input)
    except reference_fixtures.FixtureError as exc:
        _fail(str(exc))
        raise
    table = reference_import.load_overrides(
        overrides if overrides is not None else _default_overrides_path()
    )
    return fixtures, table


@app.command("plan-reference-backfill")
def cmd_plan_reference_backfill(
    db: DbOption,
    input: ReferenceInputOption = None,
    out: Annotated[Path, typer.Option("--out", help="Каталог патча")] = Path(
        "data/reference/backfill"
    ),
    max_level: MaxLevelOption = None,
    overrides_file: OverridesOption = None,
    sense_choices: Annotated[
        Path | None,
        typer.Option("--sense-choices",
                     help="CSV выбранных значений многозначных слов "
                          "(category_key,word,sense_key,note)"),
    ] = None,
) -> None:
    """Считает, чего базе не хватает для уровней записи, и пишет патч в data/.

    Патч — источник правды: база обязана пересобираться из него. Планировщик
    намеренно не видит элементов, созданных прошлым backfill'ом, поэтому
    результат одинаков на пустой и на заполненной базе.
    """
    conn = _open(db)
    fixtures, overrides = _load_reference(input, overrides_file)
    try:
        plan = reference_import.plan_backfill(
            conn, fixtures, max_level=max_level, overrides=overrides,
            sense_choices=reference_import.load_sense_choices(
                sense_choices if sense_choices is not None
                else _default_sense_choices_path()
            ),
        )
    finally:
        conn.close()
    written = reference_import.write_plan(plan, out)
    typer.echo(f"Патч записан в {out}")
    _print_table(
        ["файл", "записей"], [[name, str(count)] for name, count in sorted(written.items())]
    )
    typer.echo("")
    _print_table(
        ["чего не хватало", "штук"],
        [[name, str(count)] for name, count in sorted(plan.counts().items())],
    )


@app.command("import-reference-backfill")
def cmd_import_reference_backfill(
    db: DbOption,
    input: Annotated[Path, typer.Option("--input", help="Каталог патча")] = Path(
        "data/reference/backfill"
    ),
) -> None:
    """Применяет патч из data/. Вставляет только недостающее, решения seed не трогает."""
    conn = _open(db)
    try:
        plan = reference_import.read_plan(input)
        with conn:
            stats = reference_import.apply_backfill(conn, plan)
    except reference_import.ReferenceImportError as exc:
        conn.close()
        _fail(str(exc))
        raise
    finally:
        if conn:
            conn.close()
    _print_table(
        ["что добавлено", "штук"], [[name, str(count)] for name, count in sorted(stats.items())]
    )


@app.command("import-reference-levels")
def cmd_import_reference_levels(
    db: DbOption,
    input: ReferenceInputOption = None,
    max_level: MaxLevelOption = None,
    overrides_file: OverridesOption = None,
) -> None:
    """Кладёт уровни записи в базу без потерь. Идемпотентно."""
    conn = _open(db)
    fixtures, overrides = _load_reference(input, overrides_file)
    try:
        with conn:
            report = reference_import.import_levels(
                conn, fixtures, max_level=max_level, overrides=overrides
            )
    finally:
        conn.close()
    _print_table(
        ["что импортировано", "штук"],
        [
            ["уровней", str(report.levels)],
            ["групп", str(report.groups)],
            ["токенов", str(report.tokens)],
            ["мета-зависимостей", str(report.meta_edges)],
            ["авторских назначений", str(report.assignments)],
            ["правдоподобных чужих домов", str(report.decoys)],
            ["записей провенанса", str(report.provenance_rows)],
        ],
    )
    for gap in report.partial_gaps:
        typer.secho(f"  предел записи: {gap}", fg=typer.colors.BLUE)
    for problem in report.unresolved[:20]:
        typer.secho(f"  не разрешилось: {problem}", fg=typer.colors.YELLOW, err=True)
    if report.unresolved:
        typer.secho(
            f"Всего не разрешилось: {len(report.unresolved)}", fg=typer.colors.RED, err=True
        )
        raise typer.Exit(code=1)


@app.command("reference-coverage")
def cmd_reference_coverage(
    db: DbOption,
    input: ReferenceInputOption = None,
    max_level: MaxLevelOption = None,
    output: Annotated[Path | None, typer.Option("--output", help="Куда положить JSON")] = None,
    baseline: Annotated[
        Path | None, typer.Option("--baseline", help="Куда положить восемь чисел baseline")
    ] = None,
    show_misses: Annotated[int, typer.Option("--show-misses")] = 10,
    overrides_file: OverridesOption = None,
) -> None:
    """Покрытие записи по слоям. observed и inferred считаются отдельно."""
    conn = _open(db)
    fixtures, overrides = _load_reference(input, overrides_file)
    try:
        report = reference_coverage.measure(
            conn, fixtures, max_level=max_level, overrides=overrides
        )
    finally:
        conn.close()

    _print_table(
        ["проверка", "готово", "всего", "доля"],
        [
            [metric.name, str(metric.done), str(metric.total), f"{metric.ratio:.0%}"]
            for metric in report.metrics.values()
        ],
    )
    typer.echo("")
    _print_table(
        ["уровень", "запись", "групп", "воспроизводится", "расхождений"],
        [
            [
                str(level.level), level.completeness,
                f"{level.groups_recorded}/{level.groups_expected}",
                "да" if level.reconstructable else "нет", str(len(level.diff)),
            ]
            for level in report.levels
        ],
    )
    if show_misses:
        for metric in report.metrics.values():
            for miss in metric.misses[:show_misses]:
                typer.secho(f"  {miss}", fg=typer.colors.YELLOW)
    if output is not None:
        reference_coverage.write_report(report, output)
        typer.echo(f"\nОтчёт: {output}")
    if baseline is not None:
        baseline.parent.mkdir(parents=True, exist_ok=True)
        baseline.write_text(
            json.dumps(reference_coverage.baseline_snapshot(report), ensure_ascii=False,
                       indent=2) + "\n",
            encoding="utf-8",
        )
        typer.echo(f"Baseline: {baseline}")


@app.command("reference-gate")
def cmd_reference_gate(
    db: DbOption,
    input: ReferenceInputOption = None,
    max_level: Annotated[int, typer.Option("--max-level")] = reference_coverage.GATE_MAX_LEVEL,
    overrides_file: OverridesOption = None,
) -> None:
    """Reference Reproduction Gate. Ненулевой код = генерация нового контента запрещена."""
    conn = _open(db)
    fixtures, overrides = _load_reference(input, overrides_file)
    try:
        result = reference_coverage.gate(
            conn, fixtures, max_level=max_level, overrides=overrides
        )
    finally:
        conn.close()
    _print_table(
        ["проверка", "итог", "значение"],
        [[title, "OK" if ok else "ПРОВАЛ", detail] for title, ok, detail in result.checks],
    )
    if not result.passed:
        typer.secho(
            "\nGate не пройден. Пока система не может повторить то, что мы точно "
            "видели, её способность создавать «лучше» не подтверждена.",
            fg=typer.colors.RED,
            err=True,
        )
        raise typer.Exit(code=1)
    typer.secho("\nGate пройден: уровни референса воспроизводятся.", fg=typer.colors.GREEN)


@app.command("assess-levels")
def cmd_assess_levels(
    db: DbOption,
    origin: Annotated[
        str | None,
        typer.Option("--origin", help="Фильтр по происхождению: generated / reference_video"),
    ] = None,
    level_key: Annotated[
        str | None, typer.Option("--level-key", help="Один уровень по ключу")
    ] = None,
    margin: Annotated[
        float,
        typer.Option("--margin", help="Минимальный отрыв авторского разбиения"),
    ] = level_solver.DEFAULT_MARGIN_THRESHOLD,
    timeout_ms: Annotated[int, typer.Option("--timeout-ms")] = 5000,
    show: Annotated[int, typer.Option("--show")] = 10,
) -> None:
    """Мета-граф и отрыв авторского разбиения по каждому сохранённому уровню.

    Заменяет бинарное «одно решение или брак»: уровень с пересечениями
    проходит, если авторский ответ заметно естественнее альтернатив.
    """
    conn = _open(db)
    try:
        with conn:
            audits = level_audit.audit_all(
                conn,
                origins=(origin,) if origin else None,
                level_keys=(level_key,) if level_key else None,
                margin_threshold=margin,
                timeout_ms=timeout_ms,
            )
    finally:
        conn.close()
    _print_table(
        ["уровень", "мета", "авторское", "альтернатива", "отрыв", "ловушки", "итог"],
        [
            [
                audit.level_key,
                "ok" if audit.meta.ok else "ПРОБЛЕМА",
                f"{audit.assessment.intended_partition_score:.3f}",
                f"{audit.assessment.best_alternative_score:.3f}",
                f"{audit.assessment.partition_margin:+.3f}",
                f"{audit.assessment.planned_decoy_count}/"
                f"{audit.assessment.unplanned_decoy_count}",
                "OK" if audit.ok else "брак",
            ]
            for audit in audits
        ],
    )
    for audit in audits:
        for problem in audit.problems[:show]:
            typer.secho(f"  {audit.level_key}: {problem}", fg=typer.colors.YELLOW)


@app.command("validate-meta")
def cmd_validate_meta(
    db: DbOption,
    level_key: Annotated[
        str | None, typer.Option("--level-key", help="Один уровень по ключу")
    ] = None,
) -> None:
    """Проходим ли уровень из стартового состояния: DAG, циклы, тупики."""
    conn = _open(db)
    try:
        sql = "SELECT id, level_key FROM level_instances"
        params: tuple[object, ...] = ()
        if level_key:
            sql += " WHERE level_key = ?"
            params = (level_key,)
        rows = list(conn.execute(sql + " ORDER BY level_key", params))
        results = [
            (row["level_key"], meta_validation.validate_level_in_db(conn, int(row["id"])))
            for row in rows
        ]
    finally:
        conn.close()
    _print_table(
        ["уровень", "DAG", "глубина", "порядок сборки", "проблем"],
        [
            [
                key,
                "да" if result.is_dag else "НЕТ",
                str(result.max_depth),
                str(len(result.order)),
                str(len(result.problems)),
            ]
            for key, result in results
        ],
    )
    broken = [(key, result) for key, result in results if not result.ok]
    for key, result in broken:
        for problem in result.problems:
            typer.secho(f"  {key}: {problem}", fg=typer.colors.RED, err=True)
    if broken:
        raise typer.Exit(code=1)
    typer.secho("\nМета-граф всех уровней проходим.", fg=typer.colors.GREEN)


@app.command("export-level-pack")
def cmd_export_level_pack(
    db: DbOption,
    output: Annotated[Path, typer.Option("--output", help="Файл пакета")],
    prefix: Annotated[
        str, typer.Option("--prefix", help="Префикс ключей уровней пакета")
    ] = "L",
    playable_dir: Annotated[
        Path | None,
        typer.Option("--playable-dir",
                     help="Ещё и по файлу на уровень в формате играбельного "
                          "прототипа (site/playable/levels)"),
    ] = None,
) -> None:
    """Выгружает уровни пакета в JSON: группы, надписи, мета-связи, состав.

    Рядом с каждым уровнем кладётся состав записи оригинала того же номера —
    расхождение обязано быть видно без пересчёта.
    """
    conn = _open(db)
    try:
        pack = level_pack.build(conn, prefix)
    finally:
        conn.close()
    if not pack["levels"]:
        _fail(f"уровней с префиксом {prefix!r} в базе нет")
        return
    written = level_pack.write(output, pack)
    totals = pack["totals"]
    typer.echo(f"Пакет: {written}")
    for key, value in totals.items():
        typer.echo(f"  {key}: {value}")
    if playable_dir is not None:
        files = level_pack.write_playable(playable_dir, pack, prefix=prefix.lower())
        typer.echo(f"Для прототипа: {len(files)} файлов в {playable_dir}")


@app.command("meta-pairs")
def cmd_meta_pairs(
    db: DbOption,
    limit: Annotated[int, typer.Option("--limit", help="Сколько пар показать")] = 20,
    tier: Annotated[str, typer.Option("--tier", help="normal или hard")] = "normal",
) -> None:
    """Сколько мета-связей вообще собирается из имеющихся надписей.

    Мета-пара — совпадение слова готовой четвёрки с надписью другого правила:
    на уровне это значит «собранная группа B оставит пузырь для группы A».
    """
    conn = _open(db)
    try:
        index = meta_pairs.load(conn, tier=tier)
    finally:
        conn.close()
    for key, value in index.stats.items():
        typer.echo(f"{key}: {value}")
    if not len(index):
        typer.secho("\nМета-пар нет: генератор соберёт плоские уровни.",
                    fg=typer.colors.YELLOW)
        return
    _print_table(
        ["надпись-источник", "токен", "правило-потребитель", "пересечение пулов"],
        [
            [
                pair.source_label,
                pair.token_display,
                pair.consumer_key,
                f"{pair.pool_overlap:.0%}",
            ]
            for pair in sorted(
                {
                    (pair.consumer_id, pair.source_id): pair for pair in index.pairs
                }.values(),
                key=lambda item: (item.source_label, item.consumer_key),
            )[:limit]
        ],
    )


@app.command("composition-profile")
def cmd_composition_profile(
    upto: Annotated[int, typer.Option("--upto", help="До какого уровня показать")] = 25,
) -> None:
    """Опорный состав уровня по номеру: категории, мета-связи, ловушки.

    Числа сняты с записи оригинала. За двадцатым уровнем запись кончается,
    и профиль честно помечает продолжение кривой как `extrapolated`.
    """
    _print_table(
        ["уровень", "категорий", "мета-связей", "ловушек", "источник"],
        [
            [
                str(item.number),
                str(item.categories),
                str(item.meta_links),
                str(item.traps),
                item.source,
            ]
            for item in (composition.for_level(number) for number in range(1, upto + 1))
        ],
    )


@app.command("eval-levels")
def cmd_eval_levels(
    db: DbOption,
    prefix: Annotated[
        str, typer.Option("--prefix", help="Префикс ключей пакета: REF, RMK, ...")
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", help="Куда положить разбор по факторам (JSON)"),
    ] = None,
    swow: Annotated[
        Path | None,
        typer.Option("--swow", help="Файл ассоциаций SWOW; по умолчанию ищется сам"),
    ] = None,
    show: Annotated[
        int, typer.Option("--show", help="Сколько притяжений печатать на уровень")
    ] = 0,
) -> None:
    """Сложность D и фан F по каждому уровню пакета — по модели `levels/EVAL.md`.

    Считается детерминированно, без слепого решателя: сорок прогонов LLM на два
    пакета дали бы несравнимые числа ровно там, где нужно сравнение. Подстановки
    описаны в модуле и в `EVAL.md`.
    """
    conn = _open(db)
    try:
        results = level_eval.evaluate_pack(conn, prefix, swow=swow)
    finally:
        conn.close()
    if not results:
        _fail(f"уровней с префиксом {prefix!r} в базе нет")
        return
    _print_table(
        ["уровень", "D", "F", "категорий", "ловушек", "ага", "спорных",
         "мета", "натужных", "нечитаемых", "знакомость"],
        [
            [
                item.level_key,
                f"{item.difficulty:.1f}",
                f"{item.fun:.1f}",
                str(item.facts["категорий"]),
                str(item.facts["честных ловушек"]),
                str(item.facts["ага-моментов"]),
                str(item.facts["спорных"]),
                str(item.facts["мета-связей"]),
                str(len(item.facts["натужных надписей"])),  # type: ignore[arg-type]
                str(len(item.facts["нечитаемых токенов"])),  # type: ignore[arg-type]
                str(item.facts["знакомость средняя"]),
            ]
            for item in results
        ],
    )
    typer.echo("")
    for key, value in level_eval.summarise(results).items():
        typer.echo(f"{key}: {value}")
    if show:
        for item in results:
            for pull in item.temptations[:show]:
                mark = "ага" if pull.aha else "   "
                arrow = "ПЕРЕТЯГИВАЕТ" if pull.outpulls_home else "честная"
                typer.echo(
                    f"  {item.level_key} {mark} «{pull.token}» {pull.home} -> "
                    f"{pull.rival}: дом {pull.home_pull:.3f}, чужой "
                    f"{pull.rival_pull:.3f} — {arrow}"
                )
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(
                {
                    "prefix": prefix,
                    "summary": level_eval.summarise(results),
                    "levels": [item.as_dict() for item in results],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        typer.echo(f"\nРазбор: {output}")


def main() -> Any:
    return app()


if __name__ == "__main__":
    sys.exit(main())
