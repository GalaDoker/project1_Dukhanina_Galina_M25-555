# labyrinth_game/constants.py

ROOMS = {
    "entrance": {
        "description": (
            "Вы стоите у входа в древний лабиринт. "
            "Воздух холодный, впереди темно."
        ),
        "exits": {"north": "hall"},
        "items": ["torch"],
        "puzzle": None,
    },
    "hall": {
        "description": "Большой зал с высоким потолком. Шаги гулко отдаются от стен.",
        "exits": {"south": "entrance", "east": "library"},
        "items": [],
        "puzzle": {
            "question": "Сколько будет дважды два?",
            "answers": ["4", "четыре"],
            "reward": "Бронзовый_ключ",
        },
    },
    "library": {
        "description": "Пыльная библиотека с древними книгами и свитками.",
        "exits": {"west": "hall", "north": "treasure_room"},
        "items": ["Древняя_книга"],
        "puzzle": None,
    },
    "trap_room": {
        "description": "Комната с подозрительным полом. Кажется, здесь ловушка.",
        "exits": {"south": "library"},
        "items": [],
        "puzzle": None,
    },
    "treasure_room": {
        "description": "Комната сокровищ! В центре стоит большой сундук.",
        "exits": {"south": "library"},
        "items": ["treasure_chest"],
        "puzzle": ("Подсказка: код состоит из 4 цифр, сумма которых равна 10", "1234"),
    },
}


COMMANDS = {
    "look": "Осмотреть текущую комнату",
    "go": "Перейти в другую комнату: go <direction>",
    "take": "Поднять предмет: take <items>, <reward>",
    "use": "Использовать предмет: use <items>, <reward>",
    "inventory": "Показать инвентарь",
    "solve": "Решить загадку в комнате",
    "map": "Показать изученные комнаты",
    "help": "Показать список команд",
    "quit": "Выйти из игры",
}


COMMAND_ALIASES = {
    "n": "go north",
    "s": "go south",
    "e": "go east",
    "w": "go west",
    "i": "inventory",
    "h": "help",
    "q": "quit",
    "l": "look",
}

# Константы для игровой механики
EVENT_PROBABILITY = 10  # Вероятность случайного события (1 из 10)
EVENT_TYPES_COUNT = 3  # Количество типов случайных событий
DAMAGE_RANGE = 10  # Диапазон урона от ловушки (0-9)
LETHAL_DAMAGE_THRESHOLD = 3  # Порог смертельного урона
