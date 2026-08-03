#!/usr/bin/env bash
#
# Деплой сайта из КОММИТА, а не из рабочей папки.
#
# Зачем: `npx surge ./site` выкладывает каталог, как он лежит на диске. Над
# проектом работают несколько сессий в ОДНОМ рабочем каталоге — ветка git его не
# изолирует, — поэтому обычный деплой уносил на продакшен чужие незакоммиченные
# правки и временные файлы (03.08: правки прототипа из второй сессии и
# `site/playable/_refcheck.json`).
#
# Здесь коммит выкладывается через временный git worktree: в нём лежит ровно то,
# что закоммичено, без чужих правок и без неотслеживаемых файлов. Заодно это
# проверяет уже принятое правило «сайт обязан деплоиться из репозитория без
# предварительной сборки»: если собранный `site/tool/` забыли закоммитить,
# на продакшен уедет прежний бандл, и это будет видно сразу.
#
# Запуск:  bash scripts/deploy_commit.sh [ref] [domain]
#          npm run deploy:commit -- <ref>
#   ref     что выкладываем, по умолчанию HEAD (обычно main с влитой веткой)
#   domain  куда, по умолчанию serge-mel.surge.sh
#   DRY=1   не публиковать, только показать, что уехало бы
#
# Важно: выкладывается ТОЛЬКО этот ref. Если в main есть чужие коммиты, которых
# нет в вашей ветке, деплой ветки откатит их на сайте — сначала влейте main.
set -euo pipefail

REF="${1:-HEAD}"
DOMAIN="${2:-serge-mel.surge.sh}"

ROOT="$(git rev-parse --show-toplevel)"
SHA="$(git rev-parse --short "$REF")"
TMP="$(mktemp -d)/site-$SHA"

cleanup() { git -C "$ROOT" worktree remove --force "$TMP" >/dev/null 2>&1 || true; }
trap cleanup EXIT

git -C "$ROOT" worktree add --detach "$TMP" "$REF" >/dev/null
echo "деплой из коммита $SHA ($(git -C "$ROOT" log -1 --format=%s "$REF"))"

# Ветки без влитого main тихо откатывают сайт — предупреждаем до публикации.
BEHIND="$(git -C "$ROOT" rev-list --count "$REF..origin/main" 2>/dev/null || echo 0)"
if [ "$BEHIND" != "0" ]; then
  echo "ВНИМАНИЕ: в origin/main $BEHIND коммит(ов), которых нет в $REF — они уедут с сайта"
fi

if [ "${DRY:-}" = "1" ]; then
  echo "DRY=1, публикация пропущена. Содержимое site/ этого коммита:"
  find "$TMP/site" -maxdepth 2 -mindepth 1 | sed "s|$TMP/||" | sort
  exit 0
fi

npx --yes surge "$TMP/site" "$DOMAIN"
