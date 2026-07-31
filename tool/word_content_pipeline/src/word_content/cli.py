"""CLI пайплайна. Все пути передаются флагами, абсолютных путей в коде нет."""

from __future__ import annotations

import csv
import hashlib
import json
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
    conflicts,
    dedupe,
    integrity,
    level_solver,
    migrations,
    quartet_builder,
    readiness,
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
                written, missing = replace_pair_groups(conn, category_key, groups)
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


@app.command("build-quartets")
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
) -> None:
    """Собирает четвёрки из пулов и проверяет каждую solver'ом единственности."""
    conn = _open(db)
    try:
        built, stats = quartet_builder.build(
            conn, max_per_category=per_category, only_category=category
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
