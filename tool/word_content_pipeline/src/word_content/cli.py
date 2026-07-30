"""CLI пайплайна. Все пути передаются флагами, абсолютных путей в коде нет."""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from typing import Annotated, Any

import typer

from . import candidate_generation as gen
from .db import init_db, open_existing
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
from .repositories import (
    collect_stats,
    get_category,
    memberships_for_category,
    memberships_for_word,
    words_with_status,
)
from .validators import ValidationIssue, parse_statuses

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
) -> None:
    """Импортирует связи слово->категория из JSONL. Плохие строки не останавливают импорт."""
    conn = _open(db)
    try:
        report = import_memberships(
            conn, input, overwrite_review_status=overwrite_review_status
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
    category: Annotated[str, typer.Option("--category", help="category_key")],
    output: OutputOption,
    count: Annotated[int, typer.Option("--count", help="Сколько слов запросить")] = 30,
    batch_size: Annotated[int, typer.Option("--batch-size")] = 15,
    max_retries: Annotated[int, typer.Option("--max-retries")] = 2,
    provider: ProviderOption = "mock",
    model: ModelOption = None,
    mock_file: MockFileOption = None,
    do_import: Annotated[
        bool, typer.Option("--import", help="Сразу импортировать кандидатов в базу")
    ] = False,
) -> None:
    """Проход A: категория -> кандидатные слова. Всё сохраняется со статусом candidate."""
    conn = _open(db)
    try:
        llm = _build_provider(provider, model, mock_file)
        result = gen.expand_category(
            conn,
            llm,
            category_key=category,
            count=count,
            batch_size=batch_size,
            max_retries=max_retries,
        )
    except (LLMError, ValidationIssue) as exc:
        conn.close()
        _fail(str(exc))
        return

    try:
        _report_generation(result, output)
        if result.hints:
            typer.echo(
                "Подсказки для reverse-прохода: "
                + ", ".join(f"{w}->{sorted(set(keys))}" for w, keys in list(result.hints.items())[:10])
            )
        if do_import:
            report = import_membership_records(
                conn,
                [(i, rec) for i, rec in enumerate(result.records, start=1)],
                source_file=str(output),
                import_type="ai_category_expansion",
            )
            _print_report("Импорт кандидатов", report)
    finally:
        conn.close()


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
) -> None:
    """Проход B: слово -> дополнительные категории из существующего каталога."""
    conn = _open(db)
    try:
        if all_approved_words:
            word_list = words_with_status(conn, ["approved", "hard_only"], limit=limit)
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


def main() -> Any:
    return app()


if __name__ == "__main__":
    sys.exit(main())
