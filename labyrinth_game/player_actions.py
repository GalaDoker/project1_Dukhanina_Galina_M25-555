from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import (
    describe_current_room,
    random_event,
)


def get_input(prompt: str = "> ") -> str:
    """Получает ввод от пользователя с обработкой исключений."""
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def show_inventory(game_state: dict) -> None:
    """Отображает содержимое инвентаря игрока."""
    inventory = game_state["player_inventory"]

    if not inventory:
        print("Инвентарь пуст.")
        return

    print("У вас есть:")
    for item in inventory:
        print(f"- {item}")


def move_player(game_state: dict, direction: str) -> None:
    """Перемещает игрока в указанном направлении, обновляя его позицию."""
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return

    new_room = exits[direction]

    if new_room == "treasure_room":
        if "rusty_key" in game_state["player_inventory"]:
            print(
                "Вы используете найденный ключ,чтобы открыть путь в комнату сокровищ."
            )
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return

    game_state["current_room"] = new_room
    game_state["visited_rooms"].add(new_room)
    game_state["steps_taken"] += 1

    describe_current_room(game_state)

    random_event(game_state)


def take_item(game_state: dict, item_name: str) -> None:
    """Добавляет предмет из текущей комнаты в инвентарь игрока."""
    current_room = game_state["current_room"]
    room_items = ROOMS[current_room]["items"]

    if item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return

    if item_name not in room_items:
        print("Такого предмета здесь нет.")
        return

    room_items.remove(item_name)
    game_state["player_inventory"].append(item_name)

    print(f"Вы подняли: {item_name}")


def use_item(game_state: dict, item_name: str) -> None:
    """Использует предмет из инвентаря игрока."""
    inventory = game_state["player_inventory"]

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажигаете факел. Вокруг становится светлее.")

    elif item_name == "sword":
        print("Вы сжимаете меч. Вы чувствуете уверенность.")

    elif item_name == "bronze_box":
        if "rusty_key" not in inventory:
            inventory.append("rusty_key")
            print("Вы открыли шкатулку и находите rusty_key.")
        else:
            print("Шкатулка пуста.")

    else:
        print("Вы не знаете, как использовать этот предмет.")
