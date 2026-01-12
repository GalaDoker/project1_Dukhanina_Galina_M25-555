from labyrinth_game.constants import ROOMS
from labyrinth_game.constants import COMMANDS, COMMAND_ALIASES

def show_map(game_state: dict) -> None:
    print("Изученные комнаты:")
    for room in game_state["visited_rooms"]:
        exits = ", ".join(ROOMS[room]["exits"].keys())
        print(f"- {room} (выходы: {exits})")

def describe_current_room(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    print(f"\n== {room_name.upper()} ==")
    print(room["description"])

    if room["items"]:
        print("Заметные предметы:")
        for item in room["items"]:
            print(f"- {item}")

    exits = ", ".join(room["exits"].keys())
    print(f"Выходы: {exits}")

    if room["puzzle"] is not None:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state: dict) -> None:
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    puzzle = room["puzzle"]
    if puzzle is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(question)

    answer = input("Ваш ответ: ").strip().lower()

    if answer == correct_answer.lower():
        print("Верно! Загадка решена.")
        room["puzzle"] = None

        if "treasure_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("treasure_key")
            print("Вы получаете: treasure_key")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state: dict) -> None:
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if "treasure_chest" not in room["items"]:
        print("Здесь нет сундука.")
        return

    inventory = game_state["player_inventory"]

    if "treasure_key" in inventory:
        print("Вы применяете ключ, и замок щелкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    choice = input(
        "Сундук заперт. Хотите попробовать ввести код? (да/нет): "
    ).strip().lower()

    if choice != "да":
        print("Вы отступаете от сундука.")
        return

    if room["puzzle"] is None:
        print("Подсказок больше нет. Код неизвестен.")
        return

    _, correct_code = room["puzzle"]
    code = input("Введите код: ").strip()

    if code == correct_code:
        print("Код верный! Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("Вы нашли сокровище! Победа!")
        game_state["game_over"] = True
    else:
        print("Код неверный.")


def show_help() -> None:
    print("Доступные команды:")

    aliases_by_command: dict[str, list[str]] = {}

    for alias, full_command in COMMAND_ALIASES.items():
        base_command = full_command.split()[0]
        aliases_by_command.setdefault(base_command, []).append(alias)

    for command, description in COMMANDS.items():
        aliases = aliases_by_command.get(command, [])
        if aliases:
            alias_text = f" ({'/'.join(sorted(aliases))})"
        else:
            alias_text = ""

        print(f"- {command}{alias_text}: {description}")
