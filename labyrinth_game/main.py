#!/usr/bin/env python3

from labyrinth_game.constants import COMMAND_ALIASES
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    show_map,
    solve_puzzle,
)


def process_command(game_state: dict, command: str) -> None:
    command = command.strip().lower()

    if command in COMMAND_ALIASES:
        command = COMMAND_ALIASES[command]

    parts = command.split()

    if not parts:
        return

    action = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    match action:
        case "look":
            describe_current_room(game_state)

        case "go":
            if argument:
                move_player(game_state, argument)
            else:
                print("Куда идти?")

        case "take":
            if argument:
                take_item(game_state, argument)
            else:
                print("Что взять?")

        case "use":
            if argument:
                use_item(game_state, argument)
            else:
                print("Что использовать?")

        case "inventory":
            show_inventory(game_state)

        case "help":
            show_help()

        case "map":
            show_map(game_state)

        case "solve":
            current_room = game_state["current_room"]
            if current_room == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case "quit" | "exit":
            print("Спасибо за игру!")
            game_state["game_over"] = True

        case _:
            print("Неизвестная команда.")


def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "visited_rooms": {"entrance"},
        "game_over": False,
        "steps_taken": 0,
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    print("Введите 'help', чтобы увидеть список доступных команд.")

    describe_current_room(game_state)

    while not game_state["game_over"]:
        command = get_input()
        process_command(game_state, command)


if __name__ == "__main__":
    main()
