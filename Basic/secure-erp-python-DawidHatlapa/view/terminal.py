import os
import string
import winsound
from colorama import *


def clear_console():
    os.system("cls || clear")


def add_sentence_offset(sentence, offset):
    return ' ' * offset + sentence


def print_menu(title, list_options, add_logo=False, offset=0):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
        add_logo: if True print logo above the menu
        offset: offset of sentence in right direction
    """
    clear_console()
    if add_logo:
        print_logo()
    print()
    print(add_sentence_offset(title, offset))
    for index in range(len(list_options)):
        if index > 0:
            print(add_sentence_offset(f"({index}) {list_options[index]}", offset))
    print(add_sentence_offset(f"(0) {list_options[0]}", offset))


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print:
    - numbers       (like "@label: @value", floats with 2 digits after the decimal),
    - lists/tuples  (like "@label: \n  @item1; @item2"),
    - dictionaries  (like "@label \n  @key1: @value1; @key2: @value2")
    """
    data_type = type(result)

    if data_type == int:
        formatted_result = "{:.2f}".format(result)
        print(f"{label}: {formatted_result}")
    elif data_type == list or data_type == tuple:
        separator = ";"
        result_string = separator.join(result)
        print(label)
        print(result_string)
    elif data_type == dict:
        list_of_pairs = []
        sep = ";"
        for element in result:
            pair = []
            dictionary_sep = ":"
            pair.append(element)
            pair.append(str(result[element]))
            pair_with_sep = dictionary_sep.join(pair)
            list_of_pairs.append(pair_with_sep)

        conversion_dict_to_string = sep.join(list_of_pairs)
        print(label)
        print(conversion_dict_to_string)


def get_optimal_justify(table, table_headers):
    """Calculate optimal justify for every column in table.
    On first index is provided value of justify for first column."""
    offset = 2
    justify_offsets = []
    for header in table_headers:
        justify_offsets.append(len(header) + offset)

    for row in table:
        index = 0
        for value in row:
            if justify_offsets[index] < len(value):
                justify_offsets[index] = len(value) + offset
            index += 1

    return justify_offsets


def get_horizontal_separator(headers_to_print):
    """Create a horizontal separator based on the header."""
    horizontal_separator = ''
    for sign in headers_to_print:
        if sign != '|':
            horizontal_separator += '-'
        else:
            horizontal_separator += sign
    index = len(horizontal_separator) - 1
    is_last_sign = False
    while index >= 0:
        if horizontal_separator[index] == '|':
            is_last_sign = True
        if is_last_sign:
            horizontal_separator = horizontal_separator[:index + 1]
            break
        index -= 1
    return horizontal_separator


def get_headers_to_print(table_headers, justify_offsets):
    headers_to_print = '|'
    for index in range(len(table_headers)):
        headers_to_print += table_headers[index].center(justify_offsets[index]) + '|'.center(justify_offsets[index])
    return headers_to_print


def get_rows_to_print(table, justify_offsets):
    rows_to_print = []
    row_to_print = '|'
    row_id = 1
    for row in table:
        if row == ['']:
            continue
        counter = 0
        for value in row:
            if counter == 0:
                row_to_print += str(row_id).center(justify_offsets[counter]) + '|'.center(justify_offsets[counter])
            else:
                row_to_print += value.center(justify_offsets[counter]) + '|'.center(justify_offsets[counter])
            counter += 1
        rows_to_print.append(row_to_print)
        row_to_print = '|'
        row_id += 1
    return rows_to_print


def color_words(color, sentence):
    """Color sentence, only ascii letters.

    Args:
        color: colorama fore color, e.g. Fore.RED
        sentence: string
        """
    colored_sentence = ''
    for letter in sentence:
        if letter in string.ascii_letters:
            colored_sentence += color + letter + Fore.RESET
        else:
            colored_sentence += Fore.RESET + letter
    return colored_sentence


def color_sentence(color, sentence):
    """Color sentence and punctuation.
    Args:
        color: colorama fore color, e.g. Fore.RED
        sentence: string
        """
    return color + sentence + Fore.RESET


# /--------------------------------\ - edge
# |   id   |   product  |   type   | - headers to print
# |--------|------------|----------| - horizontal separator
# |   0    |  Bazooka   | portable | - row to print
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/ - edge


def print_table(table, table_headers, title=''):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
        table_headers: list of headers
        title: title to print above table
    """
    justify_offsets = get_optimal_justify(table, table_headers)
    headers_to_print = get_headers_to_print(table_headers, justify_offsets)
    horizontal_edge = "/" + "-" * (len(headers_to_print) - 8) + "\\"
    horizontal_separator = get_horizontal_separator(headers_to_print)
    rows_to_print = get_rows_to_print(table, justify_offsets)

    # Printing table
    print('\n' + title, end='\n\n')
    print(horizontal_edge)
    print(color_words(Fore.GREEN, headers_to_print))
    for row in rows_to_print:
        print(horizontal_separator)
        print(row)
    horizontal_edge = "\\" + "-" * (len(headers_to_print) - 8) + "/"
    print(horizontal_edge)


def play_input_beep():
    """Play Beep sound."""
    winsound.Beep(500, 200)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    result = input(label)
    play_input_beep()
    return result


def get_inputs(labels) -> []:
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    answers = []
    for label in labels:
        answer = input(label)
        play_input_beep()
        answers.append(answer)
    return answers


def get_yes_or_no(question):
    yes_or_no = input(question + '(press Y or N) ').lower()
    play_input_beep()
    while yes_or_no.lower() not in ['y', 'n']:
        yes_or_no = input(Fore.RED + 'Only Y/y or N/n is accepted ' + Fore.RESET).lower()
        play_input_beep()
    return yes_or_no == 'y'


def get_input_number(label, max_value=None) -> int:
    """Get number from user.

    Args:
        label: message in input func for user
        max_value: int - max value to provide by user, 0 is the lowest value
                    if you use max_value
    """
    customer_index = None
    is_correct_value = False
    while not is_correct_value:
        customer_index = get_input(label)
        try:
            int(customer_index)
            if max_value is not None:
                if int(customer_index) > max_value or int(customer_index) < 0:
                    raise IndexError
            is_correct_value = get_yes_or_no(f"Is correct value \"{customer_index}\"? ")
        except IndexError:
            print("That id not exist. Try again!")
        except ValueError:
            print("Is no a number. Try again!")
    return int(customer_index)


def wait_for_reaction():
    label = "\nPress enter to come back to menu..."
    label = color_sentence(Fore.GREEN, label)
    input(label)
    play_input_beep()


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(Fore.RED + "Error: " + str(message) + Fore.RESET)


def print_logo():
    print()
    print(
        r"                                                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(
        r"          =@@@@@@@@@@@@@@@@@@@@@@.   =@@@@@@@@@@@@@@@@`            @@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@[          [O@@@@@@@@@@@@@@@@@")
    print(
        r"            \@@@@           ,\@@       @@@@^      \@@@@\             @@@@      \@@@@\        @@@@@@@@@@@@@@@@[     ]]]]]]`    ,@@@@@@@@@@@@@@@")
    print(
        r"            =@@@@            .\@       =@@@^        \@@@@^           @@@@        @@@@@       @@@@@@@@@@@@@@/   ,@@@@@@@@@@@@\   =@@@@@@@@@@@@@")
    print(
        r"            =@@@@                      =@@@^         @@@@@.          @@@@         @@@@@      @@@@@@@@@@@@@^  ,@@@@@@@@@@@@@@@@^   @@@@@@@@@@@@")
    print(
        r"            =@@@@                      =@@@^         /@@@@.          @@@@         @@@@@      @@@@@@@@@@@[`   \@@@@@@@@@@@@@@@@@\  ,@@@@@@@@@@@")
    print(
        r"            =@@@@          =^          =@@@^        ,@@@@^           @@@@         @@@@@      @@@@@@@`            ,O@@@@@@@@@@@@@`  \@@@@@@@@@@")
    print(
        r"            =@@@@         /@^          =@@@^       /@@@@`            @@@@        @@@@@       @@@@@`   ]@@@@@@@\]    ,@@@@@@@@@@@^  =@@@@@@@@@@")
    print(
        r"            =@@@@@@@@@@@@@@@^          =@@@@@@@@@@@@/                @@@@@@@@@@@@@@@         @@@@`  =@@@@@@@@@@@@@\/@@@@@@@@@@@@`    ,[\@@@@@@")
    print(
        r"            =@@@@         \@^          =@@@^   \@@@@                 @@@@                    @@@^  =@@@@@@@@@@@@@@@@@@@@@@@@@@@/          \@@@")
    print(
        r"            =@@@@          =^          =@@@^     @@@@^               @@@@                    @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@/   @@@@@O`  ,@@")
    print(
        r"            =@@@@                      =@@@^      \@@@\              @@@@                    @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@`,@@@@@@@@^  =@")
    print(
        r"            =@@@@              /^      =@@@^        @@@@             @@@@                    @@@^  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^  =@")
    print(
        r"            =@@@@             /@       =@@@^         \@@@\           @@@@                    @@@@`  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /@")
    print(
        r"            =@@@@            /@@       /@@@@          =@@@@\         @@@@                    @@@@@\    [O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/`   /@@")
    print(
        r"          [/@@@@@@@@@@@@@@@@@@@@    [/@@@@@@@@]]]        @@@@@@@] @@@@@@@@@@@@@              @@@@@@@@`                                   /@@@@")
    print(
        r"                                                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(r"                                    ENTERPRISE RESOURCE PLANNING ")
    print(f"                                       Code Cool Incorporate©")
