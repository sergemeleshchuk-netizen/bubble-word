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

echo "== 1/20 seed -> JSONL =="
$PY scripts/build_seed.py

echo "== 2/20 статусы связей по SWOW =="
# Датасет SWOW лежит локально и в git не идёт. Без него статусы не пересчитать,
# но собранные ранее решения в data/review_decisions.csv остаются валидны.
if [[ -f ../../reference/swow/swow_agg.pkl ]]; then
  $PY scripts/swow_status.py
else
  echo "   SWOW не найден: беру готовые решения из data/review_decisions.csv"
fi

echo "== 3/20 пустая база =="
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

echo "== 4/20 категории seed =="
$WC import-categories --db "$DB" --input data/categories.jsonl

echo "== 5/20 связи seed =="
$WC import-memberships --db "$DB" --input data/membership_candidates.jsonl

echo "== 6/20 прогоны AI: категории, связи, решения ревью =="
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

echo "== 7/20 решения ревью =="
$WC import-review --db "$DB" --input data/review_decisions.csv
for run in data/runs/*/; do
  [[ -f "$run/review_decisions.csv" ]] || continue
  $WC import-review --db "$DB" --input "$run/review_decisions.csv"
done

echo "== 8/20 backfill по записи референса =="
# Порядок здесь не декоративный. Уровни оригинала — единственное место, где
# ответ известен заранее, и база обязана уметь их собрать ДО того, как получит
# право собирать что-то своё. Патч лежит в data/reference/backfill и является
# источником правды: правки только в SQLite запрещены.
$WC import-reference-backfill --db "$DB" --input data/reference/backfill

echo "== 8.5/20 слой доступности значений =="
# Порядок обязателен: слой читает уже загруженные связи и признак «категория из
# названий», а четвёрки на шаге 11 забирают готовые значения себе в слоты.
# Запусти его позже — и четвёрки соберутся с пустыми значениями, то есть база
# снова не сможет сказать, каким смыслом слово стоит в группе.
$WC apply-sense-layer --db "$DB"

echo "== 9/20 readiness, типы правил и надписи =="
$WC derive-readiness --db "$DB"
# Тип принципа группировки: таксономия, части, ассоциативный хаб, структура.
# Миграция проставить его не может — на чистой сборке она идёт по пустой базе.
$WC derive-rule-types --db "$DB"
# Надпись — отдельная сущность от правила группировки. Шаг обязателен: без него
# у правил нет ни одной допустимой надписи, и показать игроку после сборки
# будет нечего.
$WC derive-labels --db "$DB"

echo "== 10/20 запреты на сочетание категорий =="
$WC derive-conflicts --db "$DB" --output data/category_conflicts.csv

echo "== 11/20 проверенные четвёрки (самый долгий шаг, ~6 минут) =="
# Потолки перебора живут в quartet_builder и подобраны замером, а не на глаз:
# пул 40 (то есть без отсечки), пересечение четвёрок по одному слову, до 20
# четвёрок на правило. Прежние 12/0/3 стоили 2035 выброшенных слов и упирали
# кампанию в 323 уровня; сейчас база даёт 2238.
$WC build-quartets --db "$DB" --output data/quartets.csv

echo "== 11.5/20 связность четвёрок по SWOW =="
# Снимок, а не датасет: SWOW-EN лежит локально, 144 МБ, лицензия research-only.
# Пересобрать снимок можно только там, где датасет есть:
#     .venv/bin/python scripts/swow_quartet_metrics.py
# Обычная сборка импортирует готовый файл и потому воспроизводима где угодно.
$WC import-swow-metrics --db "$DB" --input data/content/swow_quartet_metrics.csv

echo "== 12/20 перепроверка четвёрок =="
$WC validate-quartets --db "$DB"

echo "== 13/20 разбор дублей категорий =="
# Только отчёт: слияние принципов — отдельное решение, его применяет
# dedupe-concepts --apply после просмотра CSV.
$WC dedupe-concepts --db "$DB" --output data/content/category_duplicates.csv --show 0

echo "== 14/20 рейтинги качества =="
# Порядок обязателен: агрегаты четвёрки считаются из свежих оценок слов
# и названий. Профили генерации фильтруют именно по этим числам, поэтому
# шаг идёт до сборки уровней.
$WC score-all --db "$DB"

echo "== 15/20 уровни референса без потерь =="
# Импорт идемпотентен и ничего не создаёт: всё, что уровням нужно, уже пришло
# из патча на шаге 8. Если здесь что-то создаётся — патч неполон.
$WC import-reference-levels --db "$DB"

echo "== 16/20 Reference Reproduction Gate =="
# Непроходимый барьер. Пока уровни 1-10 не воспроизводятся без потерь,
# генерация нового контента запрещена — и следующий шаг упадёт сам.
$WC reference-gate --db "$DB" --max-level 10

echo "== 17/20 мета-граф и отрыв авторского разбиения =="
$WC validate-meta --db "$DB"
$WC assess-levels --db "$DB" --origin reference_video

echo "== 18/20 уровни-кандидаты и их проверка =="
# Пять уровней на фиксированном seed: это дымовой тест генератора на реальной
# базе, а не кампания. Уровни остаются кандидатами до приёмки человеком.
$WC generate-level-candidates --db "$DB" --limit 5 --categories 5 --seed 20260731 \
    --profile accessible_fun
$WC validate-levels --db "$DB"

echo "== 18.5/20 ремейк двадцатки оригинала (RMK) =="
# Пакет RMK001..RMK020 — не украшение, а сданный артефакт: он лежит в
# levels/packs/reference-remake-20/ и на него ссылается отчёт. Пока сборка его
# не делала, пакет в репозитории и база в репозитории жили порознь, а тест
# межпроектного контракта с прототипом (test_18d) молча уходил в skip —
# «пакета RMK в базе нет». Зерно фиксировано, состав берётся с записи
# (--categories 0), то есть шаг воспроизводим.
$WC generate-level-candidates --db "$DB" --limit 20 --categories 0 --seed 101 \
    --key-prefix RMK
$WC export-level-pack --db "$DB" --prefix RMK \
    --output ../../levels/packs/reference-remake-20/pack.json
# Тот же пакет в формате прототипа: без этого шага пакет в levels/ и пакет,
# в который можно сыграть на сайте, расходятся молча. Имя файла уже стоит в
# site/playable/packs/index.json, поэтому здесь только перезапись содержимого.
python3 ../level-tool/scripts/pack_to_handoff.py \
    ../../levels/packs/reference-remake-20/pack.json \
    --label "Ремейк двадцатки оригинала" \
    > ../../site/playable/packs/remake20.handoff.json

echo "== 19/20 версия и приёмка =="
$WC stamp-version --db "$DB" --content-version "$CONTENT_VERSION"
$WC check-integrity --db "$DB"

echo
echo "База готова. Дальше по необходимости:"
echo "  $WC export-level-review-pack --db $DB              # уровни на приёмку"
echo "  $PY scripts/export_review_pack.py                  # снимок в БАЗА-СЛОВ/"
echo "  python3 ../level-tool/scripts/export_snapshot.py    # снимок для веб-инструмента"
