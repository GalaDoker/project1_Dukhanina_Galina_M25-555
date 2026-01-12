from labyrinth_game.constants import ROOMS
from labyrinth_game.constants import COMMANDS, COMMAND_ALIASES
import math

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
    puzzle = room.get("puzzle")

    if puzzle is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle

    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()

    correct_answer = correct_answer.lower()
    acceptable_answers = {correct_answer}

    if correct_answer == "10":
        acceptable_answers.add("десять")

    if user_answer in acceptable_answers:
        print("Верно! Вы решили загадку.")

        room["puzzle"] = None

        if current_room == "hall":
            if "rusty_key" not in game_state["player_inventory"]:
                print("В награду вы получаете старый ключ.")
                game_state["player_inventory"].append("rusty_key")

        elif current_room == "library":
            print("Вы находите древний свиток.")
            game_state["player_inventory"].append("ancient_scroll")

    else:
        print("Неверно. Попробуйте снова.")

        if current_room == "trap_room":
            trigger_trap(game_state)


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

def pseudo_random(seed: int, modulo: int) -> int:
    if modulo <= 0:
        return 0

    x = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = x - math.floor(x)
    return int(fractional_part * modulo)

def random_event(game_state: dict) -> None:
    chance = pseudo_random(game_state["steps_taken"], 10)
    if chance != 0:
        return

    event_type = pseudo_random(game_state["steps_taken"], 3)
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if event_type == 0:
        print("Вы заметили на полу монетку.")
        room["items"].append("coin")

    elif event_type == 1:
        print("Вы слышите странный шорох поблизости...")
        if "sword" in game_state["player_inventory"]:
            print("Вы сжимаете меч, и существо отступает.")

    elif event_type == 2:
        if current_room == "trap_room" and "torch" not in game_state["player_inventory"]:
            print("Вы не заметили опасность в темноте!")
            trigger_trap(game_state)

def trigger_trap(game_state: dict) -> None:
    print("Ловушка активирована! Пол начал дрожать...")

    inventory = game_state["player_inventory"]

    if inventory:
        index = pseudo_random(game_state["steps_taken"], len(inventory))
        lost_item = inventory.pop(index)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        damage = pseudo_random(game_state["steps_taken"], 10)
        if damage < 3:
            print("Вы получили смертельный урон. Игра окончена.")
            game_state["game_over"] = True
        else:
            print("Вам удалось уцелеть.")
