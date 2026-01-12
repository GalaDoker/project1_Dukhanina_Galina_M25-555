# labyrinth_game/constants.py

ROOMS = {
    "entrance": {
        "description": "Вы стоите у входа в древний лабиринт. Воздух холодный, впереди темно.",
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
            "reward": "bronze_key",
        },
    },

    "library": {
        "description": "Пыльная библиотека с древними книгами и свитками.",
        "exits": {"west": "hall", "north": "trap_room"},
        "items": ["ancient_book"],
        "puzzle": None,
    },

    "trap_room": {
        "description": "Комната с подозрительным полом. Кажется, здесь ловушка.",
        "exits": {"south": "library"},
        "items": [],
        "puzzle": None,
    },
}


COMMANDS = {
    "look": "Осмотреть текущую комнату",
    "go": "Перейти в другую комнату: go <direction>",
    "take": "Поднять предмет: take <item>",
    "use": "Использовать предмет: use <item>",
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

