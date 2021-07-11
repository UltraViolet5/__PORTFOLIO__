import getpass

from colorama import Fore
from view import sounds, ui, coursor


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    result = input(label)
    sounds.play_input_beep()
    return result


def input_number(message='', minimal=None, maximal=None):
    number = ""
    while number not in list(range(minimal, maximal + 1)):
        str_number = input(message)
        try:
            number = int(str_number)
        except ValueError:
            print(f"Provide a number from the range {minimal} - {maximal}")
            continue

    return number


def get_yes_or_no(question=''):
    yes_or_no = ''
    while yes_or_no.lower() not in ['y', 'n', 'yes', 'no']:
        print(question)
        yes_or_no = input(Fore.RED + 'Only Y/y or N/n is accepted: ' + Fore.RESET).lower()
        sounds.play_input_beep()
    return yes_or_no == 'y'


def wait_for_reaction():
    label = "\nPress enter to come back to continue..."
    label = ui.color_sentence(Fore.GREEN, label)
    coursor.KeyboardDisable.hide_and_block()
    hidden_input(label)
    sounds.play_input_beep()
    coursor.KeyboardDisable.show_and_unblock()


def hidden_input(msg=''):
    getpass.getpass(msg)
