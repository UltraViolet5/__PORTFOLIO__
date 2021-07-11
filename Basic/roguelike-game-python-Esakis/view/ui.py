import os
import string
import engine
import util

from classes.item import Item
from colorama import Fore
from console import sc
from controller import personalization_controller as personalization
from model.items.items import ItemsData
from model.levels import icons
from view import input_game


def clear_console():
    os.system("cls || clear")


def print_in_pos(y, x, message):
    with sc.location(x, y):
        print(message)


def display_board(board, offset=0):
    """
    Displays complete game board on the screen

    Returns:
    Nothing
    """
    util.clear_screen()
    for line in board:
        print(' ' * offset + u'{}'.format(line))


caste_one = r"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@`=@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@/...,@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@/.....,@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@/.......,@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@/....  ...,@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@^.\@@@@`              /@@@@`.@@@@@@@@@@
@@@@@@@@@`...=@@@@@^          @@@@@@....\@@@@@@@@
@@@@@@@[. . . ,@@@@^   .**    @@@@/.     ,\@@@@@@
@@@@@@@\`     ./@@@^   ***.   @@@@`.     ,@@@@@@@
@@@@@@@@^ .*. =@@@@^   ....   @@@@@  **  @@@@@@@@
@@@@@@@[^     ,[@@@^          @@@/[      [[@@@@@@
@@@@@@@         @@@^          @@@^        ,@@@@@@
@@@@@@@^   .   =@@@^          @@@@        @@@@@@@
@@@@@@@^  ***.                      .**.  @@@@@@@
@@@@@@@^  ***.                      .**.  @@@@@@@
@@@@@@@^         *.   ......   **         @@@@@@@
@@@@@@@^            .........             @@@@@@@
@@@@@@@^            ..........            @@@@@@@
@@@@@@^.            ..........            .@@@@@@
@@@`....            .........             ....\@@
@`...              ...........              ....\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

castle_two = r"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@[[[[[@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@]]]]]@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@^=@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@^  =@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@^    =@@@@@@@@@@@@@@@@@@@@@
@@@@@@@/@@@@@@@@@@@[[`      ,\[@@@@@@@@@@@@@@@@@@
@@@@@@@^....=@@@@@@............@@@@@@@@@@@.....@@
@@@@@@@^@@@@@@@@@@@@..........@@@@@@@@@@@/\@@@@@@
@@@@@@^  @@@@@@@@@@@. . **^...@@@@@@@@@@/  \@@@@@
@@@@@^    @@@@@@@@@@. .   `...@@@@@@@@@/    \@@@@
@@@@^      @@@@@@@@@. ........@@@@@@@@O      \@@@
@^            @@@@@@. . **`...@@@@@@            @
@@@         =@@@@@@@. . **^...@@@@@@@^         @@
@@@   ,**   =@@@@@@@. ........@@@@@@@^   **`   @@
@@@   =**                                **^   @@
@@@             ..              ,,`            @@
@@@    .`      =**      , ,     ^*.      ,*    @@
@@@   =**            =*^o**=             **^   @@
@@@                  =*^o**=                   @@
@@@                  =*`\**=                   @@
@@.............................................=@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

castle_three = r"""                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            /`\
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
                        KEVIN ALONE IN DUNGEON
                               BETHESDA™"""


def display_logo(offset_x=0, offset_y=0):
    print('\n' * offset_y, end='')
    print(castle_three)

    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`......\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`........\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`..........=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.............=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...............=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.................=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...................=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/[.,..    ...   ...     .=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@^                              =@@@@@@@@@^.=@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@^....=@@@@@@@@@^     ...................    /@@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@`......,@@@@@@@@@@@].                   ..]@@@@@@@@@@/.......\@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@..........@@@@@@@@@@@^                    O@@@@@@@@@@^.........=@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@/.....  .....\@@@@@@@@@^        .**.        O@@@@@@@@@`....   ....,@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@   .          .. [@@@@@@@^      .******.      O@@@@@@/` .           .  ,@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@\   ...........  =@@@@@@@^      .******.      O@@@@@@@   ...........  ,@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@     ..     =@@@@@@@@@^      .******.      O@@@@@@@@@`    ...    =@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@    .***    =@@@@@@@@@^      ..****..      O@@@@@@@@@^   .***    =@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@    .**.    =@@@@@@@@@^                    O@@@@@@@@@^   .***    =@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@            =@@@@@@@@@^                    O@@@@@@@@@^           =@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@                  =@@@@@@^                    O@@@@@@^                 .@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@                  =@@@@@@^                    O@@@@@@^                 .@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@`................,@@@@@@@^                    O@@@@@@\................./@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^               @@@@@@@@^                    O@@@@@@@^               O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^     ....      /\@@[@@[`                    [\@/\@@[^     ....      O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^    .*****.                                              .*****.    O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^    .*****.                                              ******.    O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^    .*****.                                              ******.    O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^   ..*****..       ..                          ..       ..*****..   O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                  ***.      ....... .. .      .***                  O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                  ***.     ....*.........     .***                  O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                         ......*.......*...                         O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                        .......*.......*....                        O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                        .......*.......*....                        O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@^                         ......*.......*..                          O@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@`.                       ........*.......*.....                       .\@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@/...                       ........*.......*.....                       ..,@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@/`..[^...                       ........*.......*.....                       .../`..[@@@@@@@")
    print(' ' * offset_x + r"@@@@@@^........                        ........*.......*.....                        ........@@@@@@")
    print(' ' * offset_x + r"@@@/[[\......                           .......*.......*...                           ......,[[[O@@")
    print(' ' * offset_x + r"@@^.......                             ........*.......*.....                             .......\@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(' ' * offset_x + r"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def display_authors():
    clear_screen()
    table = [["HEAD developer", "Jarosław Kaszczak"], ["developer", "Krzysztof Fieber"], ["developer", "Lukasz Sroka"]]
    header = ["ROLE", "NAME"]
    print_table(table, header, "AUTHORS")
    input_game.wait_for_reaction()


def display_statistics(hero):
    print(hero.life)
    pass


def display_communicate(x, y, message):
    pass


def display_inventory(inventory):
    inventory_table = []
    headers = Item.get_headers()
    for i, item in enumerate(inventory):
        inventory_table.append(item.get_attributes())
    print_table(inventory_table, headers, title='INVENTORY:')


def display_hall_of_fame():
    pass


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def display_simple_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def display_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(Fore.RED + "Error: " + str(message) + Fore.RESET)


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
    clear_screen()
    if add_logo:
        display_logo()
    print()
    print(add_sentence_offset(title, offset))
    for index in range(len(list_options)):
        if index > 0:
            print(add_sentence_offset(f"({index}) {list_options[index]}", offset))
    print(add_sentence_offset(f"(0) {list_options[0]}", offset))


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


def print_table(table, table_headers, title=''):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
        table_headers: list of headers
        title: title to print above table
    """
    justify_offsets = _get_optimal_justify(table, table_headers)
    headers_to_print = _get_headers_to_print(table_headers, justify_offsets)
    horizontal_edge = "/" + "-" * (len(headers_to_print) - 8) + "\\"
    horizontal_separator = _get_horizontal_separator(headers_to_print)
    rows_to_print = _get_rows_to_print(table, justify_offsets)

    # Printing table
    print('\n' + title, end='\n\n')
    print(horizontal_edge)
    print(color_words(Fore.GREEN, headers_to_print))
    for row in rows_to_print:
        print(horizontal_separator)
        print(row)
    horizontal_edge = "\\" + "-" * (len(headers_to_print) - 8) + "/"
    print(horizontal_edge)


def _get_optimal_justify(table, table_headers):
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


def _get_horizontal_separator(headers_to_print):
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


def _get_rows_to_print(table, justify_offsets):
    rows_to_print = []
    row_to_print = '|'
    row_id = 1

    for row in table:
        if row == ['']:
            continue
        counter = 0

        for value in row:
            row_to_print += value.center(justify_offsets[counter]) + '|'.center(justify_offsets[counter])
            counter += 1
        rows_to_print.append(row_to_print)
        row_to_print = '|'
        row_id += 1
    return rows_to_print


def _get_headers_to_print(table_headers, justify_offsets):
    headers_to_print = '|'
    for index in range(len(table_headers)):
        headers_to_print += table_headers[index].center(justify_offsets[index]) + '|'.center(justify_offsets[index])
    return headers_to_print


def color_sentence(color, sentence):
    """Color sentence and punctuation.
    Args:
        color: colorama fore color, e.g. Fore.RED
        sentence: string
        """
    return color + sentence + Fore.RESET


def display_attributes(player):
    player_attribute = personalization.convert_player_attribute_to_dictionary(player=player)
    print_general_results(player_attribute, "PLAYER ATTRIBUTE")


def display_gameplay_frame(board, characters):
    player = engine.get_player(characters)

    board = color_frame(board, characters)
    display_board(board)
    display_attributes(player)
    display_inventory(player.inventory)


def color_frame(level_board, characters):
    player = engine.get_player(characters)
    coin_color = Fore.YELLOW
    key_color = Fore.YELLOW
    fog_color = Fore.BLUE
    trap_color = Fore.BLUE
    treasure_color = Fore.YELLOW
    player_color = player.color
    heart_color = Fore.RED
    NPC_color = Fore.GREEN
    colored_level = []

    for i, row in enumerate(level_board):
        colored_row = []

        for j, cell in enumerate(row):
            if cell == ItemsData().coin.icon:
                colored_row.append(color_sentence(coin_color, cell))
            elif cell == ItemsData().key.icon:
                colored_row.append(color_sentence(key_color, cell))
            elif cell == icons.fog:
                colored_row.append(color_sentence(fog_color, cell))
            elif cell == icons.trap:
                colored_row.append(color_sentence(trap_color, cell))
            elif cell == icons.treasure:
                colored_row.append(color_sentence(treasure_color, cell))
            elif cell == player.icon:
                colored_row.append(color_sentence(player_color, cell))
            elif cell == icons.npc:
                colored_row.append(color_sentence(NPC_color, cell))
            elif cell == icons.life:
                colored_row.append(color_sentence(heart_color, cell))
            else:
                colored_row.append(cell)
        colored_level.append(''.join(colored_row))
    return colored_level
