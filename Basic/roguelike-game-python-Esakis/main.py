from time import sleep
from controller import main_controller
from util import window_config
from view import ui, coursor


def main():

    # LOGO
    ui.clear_console()
    ui.display_board(ui.castle_three.split('\n'))
    sleep(3.0)

    # MAIN MENU
    main_controller.main()


if __name__ == '__main__':
    window_config(font_size=22)
    main()
    coursor.KeyboardDisable.show_and_unblock()
