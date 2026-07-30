# Solver report: journey-d7.json

- Уровень: `levels/demo/journey-d7.json`, категорий 10, слов 40
- Решение: `levels/solver/journey-d7.solution.json`
- Точность: 40/40
- **Вердикт: PASS**

## Ловушки
- `parrot` (Pirates vs Pets): валидна; решатель отметил сомнение (ловушка сработала)
- `turtle` (Sea Animals vs Pets): валидна; сомнения не отмечено

## Эмпирика для оценки сложности (шаг 5)
- At the Airport: уверенность 5
- At the Hotel: уверенность 5
- At the Pool: уверенность 4
- Boats and Ships: уверенность 5
- Bodies of Water: уверенность 5
- Compass Directions: уверенность 5
- Pets: уверенность 5
- Picnic: уверенность 5
- Pirates: уверенность 5
- Sea Animals: уверенность 5
- Сомнения решателя:
  - `dive` тянуло в Pirates: ныряние ассоциируется с морем, но прыжки в воду - классика бассейна
  - `parrot` тянуло в Pets: попугай - питомец, но Pets уже укомплектован (hamster/cat/rabbit/dog), а пиратам нужен попугай
  - `pool` тянуло в Bodies of Water: бассейн тоже водоём, но lake/river/pond/bay заполняют категорию полностью
