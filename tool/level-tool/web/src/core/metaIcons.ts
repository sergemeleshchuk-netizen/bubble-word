/**
 * Картинка вместо слова на мета-пузыре.
 *
 * Мета-пузырь — это собранная категория, которая сама идёт словом в другую
 * категорию: игрок собрал четвёрку рыб, четвёрка превратилась в один пузырь
 * `fish`, и его надо доложить в AQUARIUM. Текстом это работает, но выглядит
 * ровно как обычное слово — мета-связь на поле ничем не отмечена.
 *
 * Расширение: если у мета-категории ПРОСТОЕ имя, пузырь несёт не слово, а
 * картинку. Для прототипа картинка — эмодзи: она бесплатна, встроена в любую
 * ОС, не требует ни атласа, ни загрузки, и её видно на сайте-отчёте без
 * единого килобайта ассетов. В игровой JSON пузырь уезжает помеченным
 * (`display: 'icon'`), так что клиент вправе подставить свой спрайт.
 *
 * ГЛАВНЫЙ ИНВАРИАНТ: картинка — слой ОТОБРАЖЕНИЯ, а не личность пузыря.
 * Слово остаётся тем же (`LevelWord.text`), выкладка, решатель, оценки, ловушки
 * и хеш четвёрок работают со словом. Иначе пришлось бы переучивать всё ядро,
 * а мета-пузырь с картинкой перестал бы совпадать с именем дочерней категории —
 * именно по этому совпадению прототип и находит мета-связь.
 *
 * Что значит «простое имя» — решает словарь ниже, а не длина строки. Условие
 * одно и оно строгое: эмодзи должна читаться обратно. Игрок видит 🐟 в
 * компании слов TANK, CORAL, GRAVEL и обязан понять «это рыбы» без подписи.
 * Поэтому `seasons`, `patterns`, `emotions`, `metals` в словарь не попали:
 * однозначной картинки у них нет. А `ice cream` попало, хотя это два слова:
 * 🍦 не спутать ни с чем.
 */

/**
 * Доля мета-категорий уровня, которые получают картинку.
 *
 * Пока правило нарочно простое — одна константа вместо системы: четыре
 * мета-категории на уровне → одна с картинкой. Тонкая настройка (по декадам,
 * по глубине мета-леса, по тому, насколько узнаваема конкретная эмодзи) —
 * следующий шаг, и её лучше делать на замерах, а не на догадках.
 */
export const META_ICON_SHARE = 0.25;

/**
 * Сколько мета-пузырей уровня получают картинку.
 *
 * Округление к ближайшему, а не вниз: вниз давало бы ноль на всех уровнях с
 * 1-3 мета-парами, то есть на большей части первых десяти декад — механику
 * было бы попросту не видно. Так две мета-пары дают одну картинку, шесть —
 * две, восемь — две.
 */
export function metaIconTarget(metaCount: number): number {
  return Math.round(metaCount * META_ICON_SHARE);
}

/**
 * Словарь «имя мета-категории → эмодзи». Ключ — текст пузыря в нижнем регистре.
 *
 * Собран не из головы, а по мета-пригодным именам двух баз: рабочего словаря
 * игры (2379 имён, поле `meta_capable` снимка — там в основном конкретные
 * существительные в единственном числе: `water`, `ring`, `clock`, `door`) и
 * аудированной базы (197 имён, там множественное число категорий: `fruits`,
 * `planets`, `desserts`). Отбор ручной и по одному правилу: значок должен
 * читаться обратно. Имена без однозначной картинки (`emotions`, `patterns`,
 * `metals`, `focus`, `draft`) в словарь не попали, и это не пробел.
 *
 * Формы одного понятия делят один значок нарочно (`trees` и `tree` → 🌳): для
 * игрока это одна и та же картинка, а два имени одного понятия на одном уровне
 * встретиться не могут. Похожие, но РАЗНЫЕ понятия разведены: jewelry 💍 и
 * gemstones 💎, seafood 🍤 и crustaceans 🦀, fish 🐟 и aquarium 🐠, alarm ⏰ и
 * clock 🕰️. Дубликат значка внутри одного уровня запрещён (см. `pickMetaIcons`).
 */
export const META_ICONS: Record<string, string> = {
  // животные
  fish: '🐟',
  aquarium: '🐠',
  birds: '🐦', bird: '🐦',
  owls: '🦉',
  waterfowl: '🦆',
  poultry: '🐔', chicken: '🐔',
  bears: '🐻',
  snakes: '🐍', snake: '🐍',
  turtles: '🐢',
  lizards: '🦎',
  amphibians: '🐸',
  dinosaurs: '🦕', dinosaur: '🦕',
  rodents: '🐭',
  marsupials: '🦘',
  beetles: '🪲', beetle: '🪲',
  bugs: '🐛',
  worms: '🪱',
  pets: '🐾',
  livestock: '🐄',
  seashells: '🐚', shell: '🐚',
  crustaceans: '🦀', crab: '🦀',
  cat: '🐱',
  dog: '🐶',
  horse: '🐴',
  tiger: '🐯',
  lion: '🦁',
  elephant: '🐘',
  zebra: '🦓',
  whale: '🐳',
  rabbit: '🐇',
  butterfly: '🦋',
  bee: '🐝',
  spider: '🕷️',
  parrot: '🦜',
  eagle: '🦅',
  oyster: '🦪',
  dragon: '🐉',

  // растения и природа
  flowers: '🌸', flower: '🌸',
  bouquet: '💐',
  rose: '🌹',
  trees: '🌳', tree: '🌳',
  fungi: '🍄',
  houseplants: '🪴',
  moss: '🌿', basil: '🌿',
  nest: '🪺',
  volcanoes: '🌋', volcano: '🌋',
  islands: '🏝️',
  deserts: '🏜️', desert: '🏜️',
  seas: '🌊', ocean: '🌊',
  coral: '🪸',
  storms: '⛈️', storm: '⛈️',
  hurricane: '🌀',
  tornado: '🌪️',
  lightning: '⚡',
  blizzard: '🌨️',
  frost: '❄️',
  cloud: '☁️',
  wind: '💨',
  rainbow: '🌈',
  water: '💧',
  fire: '🔥',
  ice: '🧊',
  sun: '☀️',
  galaxy: '🌌',
  planets: '🪐',
  stars: '⭐',
  moons: '🌙', moon: '🌙',
  comet: '☄️',
  satellite: '🛰️',
  mountain: '⛰️',
  cave: '🕳️',
  forest: '🌲',
  jungle: '🌴',
  river: '🏞️',
  beach: '🏖️',
  garden: '🌷',
  fountain: '⛲',
  mushroom: '🍄',

  // еда
  fruits: '🍎', apple: '🍎',
  vegetables: '🥕',
  berries: '🍓',
  cherry: '🍒',
  grape: '🍇',
  lemon: '🍋',
  onion: '🧅',
  garlic: '🧄',
  lettuce: '🥬',
  pepper: '🌶️',
  candy: '🍬',
  sweets: '🍭',
  chocolate: '🍫',
  honey: '🍯',
  'ice cream': '🍦',
  desserts: '🍰', cake: '🍰',
  pastries: '🥐', croissant: '🥐',
  baguette: '🥖',
  bagel: '🥯',
  bread: '🍞',
  cheese: '🧀',
  butter: '🧈',
  egg: '🥚',
  milk: '🥛',
  meats: '🍖',
  seafood: '🍤',
  salads: '🥗', salad: '🥗',
  soup: '🍲',
  pasta: '🍝',
  pizza: '🍕',
  burger: '🍔',
  sandwich: '🥪',
  popcorn: '🍿',
  salt: '🧂',
  teas: '🍵', tea: '🍵',
  coffee: '☕',
  juice: '🧃',
  cocktails: '🍸',
  wine: '🍷',
  beer: '🍺',
  whiskey: '🥃',
  soda: '🥤',
  sushi: '🍣',
  donut: '🍩',
  pie: '🥧',
  watermelon: '🍉',
  pear: '🍐',

  // вещи
  hats: '🎩', hat: '🎩',
  crown: '👑',
  footwear: '👟',
  eyewear: '👓', glasses: '👓',
  swimwear: '🩱',
  jewelry: '💍', ring: '💍',
  gemstones: '💎', diamond: '💎',
  makeup: '💄',
  toys: '🧸',
  balls: '⚽',
  balloon: '🎈',
  kite: '🪁',
  puzzles: '🧩',
  chess: '♟️',
  awards: '🏆',
  furniture: '🛋️', 'living room': '🛋️',
  bed: '🛏️',
  silverware: '🍴', fork: '🍴',
  dishes: '🍽️', plate: '🍽️',
  bowl: '🥣',
  blades: '🔪', knife: '🔪',
  sword: '🗡️',
  hammer: '🔨',
  saw: '🪚',
  needle: '🪡',
  thread: '🧵',
  wool: '🧶',
  ladder: '🪜',
  anchor: '⚓',
  medicines: '💊',
  'first aid': '🩹',
  lighting: '💡', light: '💡',
  lantern: '🏮',
  candle: '🕯️',
  mirror: '🪞',
  umbrella: '☂️',
  timepieces: '⌚', watch: '⌚',
  clock: '🕰️',
  alarm: '⏰',
  timer: '⏲️',
  calendar: '📅', months: '📅',
  fuels: '⛽',
  currencies: '💰', coin: '🪙',
  camera: '📷',
  phone: '📱',
  radio: '📻',
  computer: '💻',
  battery: '🔋',
  telescope: '🔭',
  microscope: '🔬',
  chemistry: '🧪',
  magnet: '🧲',
  lock: '🔒',
  axe: '🪓',
  flag: '🚩',
  coat: '🧥',
  boot: '🥾',
  wallet: '👛',
  book: '📚',
  paper: '📄',
  envelope: '✉️',
  pencil: '✏️',
  pen: '🖊️',
  brush: '🖌️',
  painting: '🖼️',
  ticket: '🎫',
  map: '🗺️',
  backpack: '🎒',
  tent: '⛺',
  heart: '❤️',
  bones: '🦴',
  hand: '✋',

  // места и постройки
  house: '🏠',
  castle: '🏰',
  tower: '🗼',
  bridge: '🌉',
  road: '🛣️',
  bank: '🏦',
  hotel: '🏨',
  hospital: '🏥',
  church: '⛪',
  museum: '🏛️',
  stadium: '🏟️',
  station: '🚉',
  school: '🎒',
  farm: '🚜',
  picnic: '🧺',
  barbershop: '💈',
  countries: '🌍',
  door: '🚪',

  // транспорт
  vehicles: '🚗', car: '🚗',
  trucks: '🚚', truck: '🚚',
  aircraft: '✈️', plane: '✈️',
  spacecraft: '🚀', rocket: '🚀',
  ship: '🚢',
  train: '🚆',
  taxi: '🚕',
  bicycle: '🚲', bike: '🚲',
  canoe: '🛶',
  ambulance: '🚑',

  // прочее
  directions: '🧭', compass: '🧭',
  colors: '🎨',
  green: '🟢',
  music: '🎵',
  guitar: '🎸',
  piano: '🎹',
  violin: '🎻',
  saxophone: '🎷',
  drum: '🥁',
  trumpet: '🎺',
  microphone: '🎤',
  theater: '🎭',
  movies: '🎬', films: '🎬', cinema: '🎬',
  circus: '🎪',
  dance: '💃',
  basketball: '🏀',
  tennis: '🎾',
  baseball: '⚾',
  bowling: '🎳',
  boxing: '🥊',
  golf: '⛳',
  skiing: '⛷️',
  surfing: '🏄',
  fishing: '🎣',
  ghost: '👻',
  vampire: '🧛',
  zombie: '🧟',
  wizard: '🧙',
  fairy: '🧚',
  unicorn: '🦄',
  alien: '👽',
  robot: '🤖',
  ninja: '🥷',
  pirate: '🏴‍☠️',
  sculpture: '🗿',
  christmas: '🎄',
  casino: '🎰',
  tooth: '🦷',
  eye: '👁️',
  nose: '👃',
  brain: '🧠',
  blood: '🩸',
  king: '🤴',
  queen: '👸',
  superheroes: '🦸',
  greetings: '👋',
  'new year': '🎉',
  easter: '🐰',
};

/** Эмодзи для текста мета-пузыря или null, если имя не из простых. */
export function metaIconFor(text: string): string | null {
  return META_ICONS[text.trim().toLowerCase()] ?? null;
}

/**
 * Кому из мета-пузырей уровня дать картинку.
 *
 * На входе — тексты мета-пузырей в порядке уровня, на выходе — карта
 * «текст → эмодзи» ровно на `metaIconTarget` записей (или меньше, если простых
 * имён в уровне не хватило — придумывать картинку там, где её не прочитают,
 * хуже, чем оставить слово).
 *
 * Выбор детерминированный и НЕ трогает поток случайных чисел генератора: вес
 * берётся из `rng.stableWeight`, который зависит только от seed и ключа. Иначе
 * появление картинок сдвинуло бы всю последующую случайность — распилы,
 * блокираторы, цепи, — и уровень изменился бы целиком, а не одним пузырём.
 */
export function pickMetaIcons(
  metaWords: readonly string[],
  weight: (key: string) => number,
  /**
   * Минимум картинок на уровне. Ноль — правило доли работает как всегда.
   * Единица приходит от плана: уровень, которому человек поставил галочку
   * «категория-картинка», обязан её получить, даже если мета-пара на нём одна
   * (доля дала бы ноль, см. `metaIconTarget`).
   */
  minCount = 0,
): Map<string, string> {
  const target = Math.max(minCount, metaIconTarget(metaWords.length));
  const chosen = new Map<string, string>();
  if (target <= 0) return chosen;

  const eligible = metaWords
    .map((text) => ({ text, icon: metaIconFor(text) }))
    .filter((c): c is { text: string; icon: string } => c.icon !== null)
    .sort((a, b) => weight(a.text) - weight(b.text));

  const usedIcons = new Set<string>();
  for (const candidate of eligible) {
    if (chosen.size >= target) break;
    // одна эмодзи на уровень: два одинаковых значка на поле игрок прочитает
    // как один и тот же пузырь
    if (usedIcons.has(candidate.icon)) continue;
    usedIcons.add(candidate.icon);
    chosen.set(candidate.text, candidate.icon);
  }
  return chosen;
}
