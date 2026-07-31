#!/usr/bin/env bash
#
# Полная пересборка контентной базы из текстовых источников.
#
# Зачем скрипт, а не список команд в README: база собирается из десятка
# источников в фиксированном порядке, и один пропущенный шаг даёт тихо неполную
# базу. Ровно так проект уже разошёлся — снимок для веб-инструмента месяц жил на
# копии базы, собранной до аудита, потому что пересборку делали руками в другом
# каталоге. Один скрипт = один источник правды.
#
# Запуск из каталога tool/word_content_pipeline:
#     bash scripts/rebuild_all.sh
#
# Ненулевой код возврата = база не готова, отдавать её нельзя.

set -euo pipefail

cd "$(dirname "$0")/.."

DB=database/content.sqlite
PY=.venv/bin/python
WC=.venv/bin/word-content
CONTENT_VERSION="${CONTENT_VERSION:-$(date -u +%Y.%m.%d)}"

if [[ ! -x "$PY" ]]; then
  echo "ОШИБКА: нет venv ($PY). Создайте: python3 -m venv .venv && .venv/bin/pip install -e ." >&2
  exit 1
fi

echo "== 1/15 seed -> JSONL =="
$PY scripts/build_seed.py

echo "== 2/15 статусы связей по SWOW =="
# Датасет SWOW лежит локально и в git не идёт. Без него статусы не пересчитать,
# но собранные ранее решения в data/review_decisions.csv остаются валидны.
if [[ -f ../../reference/swow/swow_agg.pkl ]]; then
  $PY scripts/swow_status.py
else
  echo "   SWOW не найден: беру готовые решения из data/review_decisions.csv"
fi

echo "== 3/15 пустая база =="
# Именно пустая: init-db повторный запуск переживает, но НЕ чистит. Если собирать
# поверх старой базы, правки источников дают не замену, а второй экземпляр связи:
# идентичность связи включает значение слова, поэтому «та же связь, но со смыслом»
# уезжает отдельной строкой, а решения ревью достаются старой. Проверено на себе.
if [[ -f "$DB" ]]; then
  mkdir -p database/backup
  mv "$DB" "database/backup/content.$(date -u +%Y%m%dT%H%M%SZ).sqlite"
fi
rm -f "$DB-wal" "$DB-shm"
$WC init-db --db "$DB"

echo "== 4/15 категории seed =="
$WC import-categories --db "$DB" --input data/categories.jsonl

echo "== 5/15 связи seed =="
$WC import-memberships --db "$DB" --input data/membership_candidates.jsonl

echo "== 6/15 прогоны AI: категории, связи, решения ревью =="
# Прогон = отдельный источник с сохранённым провенансом (кто предложил, кто
# решил). Мета-хабы дают материал для мета-пар: категория STARGAZING держит
# слово `planets`, а PLANETS — сама категория уровня. Без этого слоя механика
# мета-пузырей в генераторе не собирается вообще.
for run in data/runs/*/; do
  [[ -d "$run" ]] || continue
  name=$(basename "$run")
  echo "   прогон $name"
  [[ -f "$run/categories.jsonl" ]] && \
    $WC import-categories --db "$DB" --input "$run/categories.jsonl"
  [[ -f "$run/memberships.jsonl" ]] && \
    $WC import-memberships --db "$DB" --input "$run/memberships.jsonl"
done

echo "== 7/15 решения ревью =="
$WC import-review --db "$DB" --input data/review_decisions.csv
for run in data/runs/*/; do
  [[ -f "$run/review_decisions.csv" ]] || continue
  $WC import-review --db "$DB" --input "$run/review_decisions.csv"
done

echo "== 8/19 backfill по записи референса =="
# Порядок здесь не декоративный. Уровни оригинала — единственное место, где
# ответ известен заранее, и база обязана уметь их собрать ДО того, как получит
# право собирать что-то своё. Патч лежит в data/reference/backfill и является
# источником правды: правки только в SQLite запрещены.
$WC import-reference-backfill --db "$DB" --input data/reference/backfill

echo "== 9/19 readiness, типы правил и надписи =="
$WC derive-readiness --db "$DB"
# Тип принципа группировки: таксономия, части, ассоциативный хаб, структура.
# Миграция проставить его не может — на чистой сборке она идёт по пустой базе.
$WC derive-rule-types --db "$DB"
# Надпись — отдельная сущность от правила группировки. Шаг обязателен: без него
# у правил нет ни одной допустимой надписи, и показать игроку после сборки
# будет нечего.
$WC derive-labels --db "$DB"

echo "== 10/19 запреты на сочетание категорий =="
$WC derive-conflicts --db "$DB" --output data/category_conflicts.csv

echo "== 11/19 проверенные четвёрки =="
$WC build-quartets --db "$DB" --output data/quartets.csv

echo "== 12/19 перепроверка четвёрок =="
$WC validate-quartets --db "$DB"

echo "== 13/19 разбор дублей категорий =="
# Только отчёт: слияние принципов — отдельное решение, его применяет
# dedupe-concepts --apply после просмотра CSV.
$WC dedupe-concepts --db "$DB" --output data/content/category_duplicates.csv --show 0

echo "== 14/19 рейтинги качества =="
# Порядок обязателен: агрегаты четвёрки считаются из свежих оценок слов
# и названий. Профили генерации фильтруют именно по этим числам, поэтому
# шаг идёт до сборки уровней.
$WC score-all --db "$DB"

echo "== 15/19 уровни референса без потерь =="
# Импорт идемпотентен и ничего не создаёт: всё, что уровням нужно, уже пришло
# из патча на шаге 8. Если здесь что-то создаётся — патч неполон.
$WC import-reference-levels --db "$DB"

echo "== 16/19 Reference Reproduction Gate =="
# Непроходимый барьер. Пока уровни 1-10 не воспроизводятся без потерь,
# генерация нового контента запрещена — и следующий шаг упадёт сам.
$WC reference-gate --db "$DB" --max-level 10

echo "== 17/19 мета-граф и отрыв авторского разбиения =="
$WC validate-meta --db "$DB"
$WC assess-levels --db "$DB" --origin reference_video

echo "== 18/19 уровни-кандидаты и их проверка =="
# Пять уровней на фиксированном seed: это дымовой тест генератора на реальной
# базе, а не кампания. Уровни остаются кандидатами до приёмки человеком.
$WC generate-level-candidates --db "$DB" --limit 5 --categories 5 --seed 20260731 \
    --profile accessible_fun
$WC validate-levels --db "$DB"

echo "== 19/19 версия и приёмка =="
$WC stamp-version --db "$DB" --content-version "$CONTENT_VERSION"
$WC check-integrity --db "$DB"

echo
echo "База готова. Дальше по необходимости:"
echo "  $WC export-level-review-pack --db $DB              # уровни на приёмку"
echo "  $PY scripts/export_review_pack.py                  # снимок в БАЗА-СЛОВ/"
echo "  python3 ../level-tool/scripts/export_snapshot.py    # снимок для веб-инструмента"
