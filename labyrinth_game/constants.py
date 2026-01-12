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
        "exits": {"south": "entrance"},
        "items": [],
        "puzzle": (
            "На стене высечена надпись: «Сколько будет дважды два?»",
            "4",
        ),
    },
}
