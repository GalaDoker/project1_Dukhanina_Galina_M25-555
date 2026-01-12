def show_inventory(game_state: dict) -> None:
    inventory = game_state["player_inventory"]

    if not inventory:
        print("Ваш инвентарь пуст.")
        return

    print("В вашем инвентаре:")
    for item in inventory:
        print(f"- {item}")


def get_input(prompt: str = "> ") -> str:
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room


def move_player(game_state: dict, direction: str) -> None:
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return

    game_state["current_room"] = exits[direction]
    game_state["steps_taken"] += 1

    describe_current_room(game_state)

def take_item(game_state: dict, item_name: str) -> None:
    current_room = game_state["current_room"]
    room_items = ROOMS[current_room]["items"]

    if item_name not in room_items:
        print("Такого предмета здесь нет.")
        return

    room_items.remove(item_name)
    game_state["player_inventory"].append(item_name)

    print(f"Вы подняли: {item_name}")


def use_item(game_state: dict, item_name: str) -> None:
    inventory = game_state["player_inventory"]

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажигаете факел. Вокруг становится светлее.")
    elif item_name == "sword":
        print("Вы сжимаете меч. Чувствуете уверенность.")
    elif item_name == "bronze_box":
        if "rusty_key" not in inventory:
            inventory.append("rusty_key")
            print("Вы открыли шкатулку и нашли rusty_key!")
        else:
            print("Шкатулка пуста.")
    else:
        print("Вы не знаете, как использовать этот предмет.")
