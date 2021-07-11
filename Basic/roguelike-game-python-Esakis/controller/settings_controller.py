from colorama import Fore

import util
from view import ui, input_game


def display_menu():
    menu_params = ['Exit',
                   'Small',
                   'Medium',
                   'Big']
    label = "SETTINGS:\n" \
            "Set font size:"
    ui.print_menu(label, menu_params)


def run_operation(operation):
    if operation == 1:
        util.window_config(font_size=18)
    elif operation == 2:
        util.window_config(font_size=22)
    elif operation == 3:
        util.window_config(font_size=26)
    elif operation == 0:
        pass
    else:
        raise KeyError()


def main():
    operation = None

    while operation != '0':
        display_menu()
        try:
            operation = input_game.get_input(ui.color_sentence(Fore.GREEN, "Your pick: "))
            run_operation(int(operation))
        except KeyError:
            ui.display_error_message("There is no such option.")
            input_game.wait_for_reaction()
        except ValueError:
            ui.display_error_message("Please enter a number!", )
            input_game.wait_for_reaction()
