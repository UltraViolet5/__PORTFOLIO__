from classes import creature
from classes.enums import Genre, Role
from view import input_game as input_pc, sounds
from colorama import Fore
from view import ui


def get_payer_name():
    is_correct = False
    name = ""
    while not is_correct:
        get_payer_name_label = "Provide player name: "
        name = input_pc.get_input(get_payer_name_label)
        is_correct = input_pc.get_yes_or_no(f"Is the value \"{name}\" correct? ")

    return name


def set_player_name(player, name):
    player.name = name


def get_player_icon():
    is_correct = False
    icon_number = 1
    while not is_correct:
        set_player_icon_label = "Select the player icon 1:♀, 2:@, 3:X, 4:#\n" \
                                "Your pick: "
        icon_number = input_pc.input_number(set_player_icon_label, minimal=1, maximal=4)
        sounds.play_input_beep()
        is_correct = input_pc.get_yes_or_no(f"Is the value \"{icon_number}\" correct? ")

    return icon_number


def set_player_icon(player, icon_number):
    if icon_number == 1:
        player.icon = "♀"
    elif icon_number == 2:
        player.icon = "@"
    elif icon_number == 3:
        player.icon = "X"
    elif icon_number == 4:
        player.icon = "#"

    return player.icon


def get_payer_color():
    is_correct = False
    color_number = ""

    red = Fore.RED + "RED" + Fore.RESET
    green = Fore.GREEN + "GREEN" + Fore.RESET
    yellow = Fore.YELLOW + "YELLOW" + Fore.RESET
    blue = Fore.BLUE + "BLUE" + Fore.RESET
    magenta = Fore.MAGENTA + "VIOLET" + Fore.RESET
    cyan = Fore.CYAN + "CYAN" + Fore.RESET
    white = Fore.WHITE + "WHITE" + Fore.RESET

    while not is_correct:
        get_payer_color_label = f"Select the player color:  \n1:{red}, 2:{yellow}, 3:{blue}, 4:{magenta}, 5: {cyan}, 6:{white}" \
                                f"\nYour pick: "
        color_number = input_pc.input_number(get_payer_color_label, minimal=1, maximal=7)
        is_correct = input_pc.get_yes_or_no(f"Is the value \"{color_number}\" correct? ")

    return color_number


def set_player_color(player, color_number):
    if color_number == 1:
        player.color = Fore.RED
        player_color = "RED"
    elif color_number == 2:
        player.color = Fore.YELLOW
        player_color = "YELLOW"
    elif color_number == 3:
        player.color = Fore.BLUE
        player_color = "BLUE"
    elif color_number == 4:
        player.color = Fore.MAGENTA
        player_color = "MAGENTA"
    elif color_number == 5:
        player.color = Fore.CYAN
        player_color = "CYAN"
    elif color_number == 6:
        player.color = Fore.WHITE
        player_color = "WHITE"

    return player_color


def create_player_attribute_list(name="...", icon="...", color="..."):
    attribute_list = [["1", "Name", name], ["2", "icon", icon], ["3", "color", color]]

    return attribute_list


def convert_player_attribute_to_dictionary(player=creature.Creature()):
    player_dictionary = {"  NAME  ": player.name, "  iCON  ": player.icon,
                         "  LIFE  ": str(player.current_life) + "/" + str(player.life),
                         "  STRENGTH  ": player.strength, " DAMAGE ": player.damage, "  LEVEL  ": player.level,
                         "  POINTS  ": player.points}
    return player_dictionary


def create_player():
    list_header = ["number", "type", "value"]
    ui.clear_screen()

    player = creature.Creature(genre=Genre.Human, role=Role.Player)
    ui.print_table(create_player_attribute_list(), list_header, "PLAYER ATTRIBUTE")

    name = get_payer_name()
    set_player_name(player, name)
    ui.clear_screen()
    ui.print_table(create_player_attribute_list(name=name), list_header, "PLAYER ATTRIBUTE")

    icon_number = get_player_icon()
    icon = set_player_icon(player, icon_number)
    ui.clear_screen()
    ui.print_table(create_player_attribute_list(name=name, icon=icon), list_header, "PLAYER ATTRIBUTE")

    color_number = get_payer_color()
    color_text = set_player_color(player, color_number)
    ui.clear_screen()
    ui.print_table(create_player_attribute_list(name=name, icon=icon, color=color_text), list_header,
                   "PLAYER ATTRIBUTE")
    input_pc.wait_for_reaction()

    return player
