#!/usr/bin/env python3
"""Динамическая проверка проходимости уровня: симуляция партии по правилам
играбельного прототипа (site/playable/index.html).

Слепой решатель (solver_blind) отвечает на вопрос «однозначен ли уровень
семантически». Этот скрипт отвечает на другой вопрос: «доиграется ли уровень
с выкладкой генератора» - хватит ли лимита ходов, не встанет ли поле без
легального мерджа и как часто игрок попадает в состояние, ВЫГЛЯДЯЩЕЕ тупиком
(собрать нечего, ходить почти некуда, досыпки не видно).

Правила симуляции 1в1 с прототипом:
- мердж легален: одна категория и суммарно не больше 4 слов; половинки
  склеиваются только со своей парой; каждый мердж стоит 1 ход;
- четвёрка собирается бесплатно; обычная категория улетает и приходит
  досыпка 4, мета-категория превращается в слово родителя и приходит 3;
- модификатор пакета (`modifier`): лёд/«?» не мерджатся, пока не растают
  (каждый мердж снимает слой со всех), цепь делит поле на зоны до сбора
  chain_need категорий (зоны чередуются: координат у симуляции нет);
- страховки прототипа, в его порядке: цепь падает, лёд тает, потом
  досыпка 4 «вне ритма»;
- жёсткий тупик: легального мерджа нет и очередь пуста - уровень непроходим.

TS-двойник в ядре инструмента: web/src/core/simulatePlayability.ts (гейт
приёмки при сборке блока). Этот скрипт - внешняя приёмка готовых паков.

Бот играет жадно: сперва мердж, завершающий четвёрку, иначе мердж в категории,
у которой на поле больше всего слов. Число ходов до победы от порядка мерджей
не зависит (каждый мердж уменьшает число кусков на 1), поэтому вердикт
«хватит ли лимита» точный, а не эвристический.

Запуск:
  python3 sim_playability.py <pack.handoff.json ...>
  python3 sim_playability.py --all   # все паки из site/playable/packs/index.json
"""
import json, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PACKS_DIR = os.path.join(ROOT, 'site', 'playable', 'packs')


def load_levels(path):
    d = json.load(open(path))
    levels = d.get('levels') or []
    return d.get('label', os.path.basename(path)), levels


def build_level(lv):
    """Категории, мета-связи (цепочки), выкладка и распилы - как в applyLevel."""
    cats = [{'v': c['name'].upper(),
             'id': c['id'],
             'ex': [w.upper() for w in c['words']],
             'meta': None} for c in lv['categories']]
    by_name = {c['v']: i for i, c in enumerate(cats)}
    for p in cats:
        for w in p['ex']:
            ci = by_name.get(w)
            if ci is not None and cats[ci] is not p:
                cats[ci]['meta'] = {'parent': p['v'], 'word': w}
    metaw = {c['meta']['word'] for c in cats if c['meta']}
    full = {c['v']: len(c['ex']) for c in cats}
    by_id = {c['id']: c['v'] for c in cats}

    deal = lv.get('deal')
    if not deal:
        return None
    chunks = {}
    for ch in (lv.get('chunks') or []):
        chunks[(by_id[ch['category']], ch['word'].upper())] = [p.upper() for p in ch['pieces']]

    def expand(src):
        out, pid = [], [0]
        def conv(b):
            v, e = by_id[b['category']], b['word'].upper()
            parts = chunks.get((v, e))
            if not parts:
                return [{'v': v, 'e': e, 'half': None}]
            pid[0] += 1
            return [{'v': v, 'e': parts[0], 'half': (pid[0], 0)},
                    {'v': v, 'e': parts[1], 'half': (pid[0], 1)}]
        for b in src:
            out.extend(conv(b))
        return out

    mod = lv.get('modifier') or None
    blocked = {}
    chain_need = 0
    if mod:
        if mod.get('type') == 'chain':
            chain_need = max(1, int(mod.get('chain_need') or 2))
        else:
            src = mod.get('frozen') if mod.get('type') == 'ice' else mod.get('hidden')
            for b in (src or []):
                blocked[(by_id.get(b['category']), b['word'].upper())] = \
                    max(1, int(b.get('layers') or 2))

    return {'cats': cats, 'metaw': metaw, 'full': full,
            'start': expand(deal['start']), 'queue': expand(deal['queue']),
            'blocked': blocked, 'chain_need': chain_need,
            'moves': (lv.get('board') or {}).get('move_limit')}


def legal_merges(field, full, chain_up):
    """Все легальные пары: (i, j). Кластер = {'v','exs','half','blk','zone'}."""
    res = []
    for i in range(len(field)):
        for j in range(i + 1, len(field)):
            a, b = field[i], field[j]
            if a['blk'] > 0 or b['blk'] > 0:
                continue
            if chain_up and a['zone'] != b['zone']:
                continue
            if a['half'] or b['half']:
                if a['half'] and b['half'] and a['half'][0] == b['half'][0] \
                   and a['half'][1] != b['half'][1]:
                    res.append((i, j))
                continue
            if a['v'] == b['v'] and len(a['exs']) + len(b['exs']) <= full[a['v']]:
                res.append((i, j))
    return res


def simulate(L):
    cats_by_name = {c['v']: c for c in L['cats']}
    full = L['full']
    blocked, chain_need = L.get('blocked', {}), L.get('chain_need', 0)
    chain_up = chain_need > 0
    zone_flip = [0]

    def to_bubble(it):
        zone_flip[0] += 1
        return {'v': it['v'], 'exs': [it['e']], 'half': it['half'],
                'blk': 0 if it['half'] else blocked.get((it['v'], it['e']), 0),
                'zone': zone_flip[0] % 2 if chain_up else 0}

    field = [to_bubble(it) for it in L['start']]
    queue = list(L['queue'])
    total_cats = len(L['cats'])
    done, moves_spent, rescues = 0, 0, 0
    cur_drought, perceived_dead = 0, 0
    max_drought = 0

    def spawn(n):
        for _ in range(min(n, len(queue))):
            field.append(to_bubble(queue.pop(0)))

    guard = 10000
    while done < total_cats and guard > 0:
        guard -= 1
        lm = legal_merges(field, full, chain_up)
        if not lm:
            # страховки прототипа, в его порядке: цепь -> лёд -> досыпка
            if chain_up:
                chain_up = False
                continue
            if any(b['blk'] > 0 for b in field):
                for b in field:
                    b['blk'] = 0
                continue
            if queue:
                rescues += 1
                spawn(4)
                continue
            return {'ok': False, 'why': 'ЖЁСТКИЙ ТУПИК: мерджей нет и очередь пуста',
                    'done': done, 'moves': moves_spent, 'rescues': rescues,
                    'max_drought': max_drought, 'perceived_dead': perceived_dead}
        # состояние «выглядит тупиком»: собрать нечего и ходить почти некуда
        completing = [(i, j) for i, j in lm
                      if not field[i]['half'] and
                      len(field[i]['exs']) + len(field[j]['exs']) == full[field[i]['v']]]
        if not completing and len(lm) <= 1:
            perceived_dead += 1
        # жадный выбор: завершающий мердж, иначе категория с максимумом слов на поле
        if completing:
            i, j = completing[0]
        else:
            def weight(p):
                a, b = field[p[0]], field[p[1]]
                if a['half']:
                    return 100  # половинки склеиваем сразу: без целого слова категория не соберётся
                on_field = sum(len(c['exs']) for c in field if not c['half'] and c['v'] == a['v'])
                return on_field
            i, j = max(lm, key=weight)
        a, b = field[i], field[j]
        if a['half'] and b['half']:
            # склейка половинок: получается обычный пузырь-слово, счётчик слов
            # категории от неё не растёт, но ход тратится (как в прототипе)
            merged = {'v': a['v'], 'exs': ['WHOLE#%d' % a['half'][0]], 'half': None,
                      'blk': 0, 'zone': a['zone']}
        else:
            merged = {'v': a['v'], 'exs': a['exs'] + b['exs'], 'half': None,
                      'blk': 0, 'zone': a['zone']}
        field = [c for k, c in enumerate(field) if k not in (i, j)]
        field.append(merged)
        moves_spent += 1
        cur_drought += 1
        # успешный мердж снимает слой льда/«?» со всего поля
        for c in field:
            if c['blk'] > 0:
                c['blk'] -= 1
        # сборка четвёрки
        if not merged['half'] and len(merged['exs']) >= full[merged['v']]:
            field.remove(merged)
            done += 1
            max_drought = max(max_drought, cur_drought)
            cur_drought = 0
            if chain_up and done >= chain_need:
                chain_up = False   # цепь снята сбором категорий
            cd = cats_by_name[merged['v']]
            if cd['meta']:
                field.append({'v': cd['meta']['parent'], 'exs': [cd['meta']['word']],
                              'half': None, 'blk': 0, 'zone': 0})
                spawn(3)
            else:
                spawn(4)
        else:
            # страховка прототипа: после мерджа поле могло остаться без пар
            if not legal_merges(field, full, chain_up) and queue and done < total_cats:
                rescues += 1
                spawn(4)
    return {'ok': True, 'done': done, 'moves': moves_spent, 'rescues': rescues,
            'max_drought': max_drought, 'perceived_dead': perceived_dead}


def run_pack(path):
    label, levels = load_levels(path)
    print(f'== {os.path.basename(path)} ({label})')
    for lv in levels:
        L = build_level(lv)
        title = lv.get('title', f"level {lv.get('level_id')}")
        if L is None:
            print(f'  - {title}: нет выкладки (deal) - симулировать нечего, пропуск')
            continue
        r = simulate(L)
        limit = L['moves']
        if not r['ok']:
            print(f'  ✗ {title}: {r["why"]} (собрано {r["done"]}, потрачено {r["moves"]})')
            continue
        spare = (limit - r['moves']) if limit is not None else None
        verdict = 'ПРОХОДИМ' if (spare is None or spare >= 0) else 'НЕ ХВАТАЕТ ХОДОВ'
        print(f'  {"✓" if verdict=="ПРОХОДИМ" else "✗"} {title}')
        print(f'      ходов надо {r["moves"]} / лимит {limit} (запас {spare}); '
              f'досыпок вне ритма {r["rescues"]}; '
              f'состояний-«тупиков» на глаз {r["perceived_dead"]}; '
              f'макс. серия ходов без сбора {r["max_drought"]}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or args[0] == '--all':
        idx = json.load(open(os.path.join(PACKS_DIR, 'index.json')))
        files = [os.path.join(PACKS_DIR, p) for p in idx['packs']]
    else:
        files = args
    for f in files:
        run_pack(f)
