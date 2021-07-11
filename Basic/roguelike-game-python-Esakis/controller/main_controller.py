from copy import deepcopy

from colorama import Fore

import engine
from classes.creature import Creature
from classes.enums import Role
from controller import gameplay_controller, personalization_controller, settings_controller
from model.graphic import graphic
from view import ui, input_game, coursor
from model.scores import scores

book_menu = r"""
                            KEVIN ALONE IN DUNGEON
                    __________________   __________________
                .-/|                  \ /                  |\-.
                ||||     --==*==--     |                   ||||
                ||||                   |       ~~*~~       ||||
                ||||    MAIN MENU:     |                   ||||
                ||||                   |                   ||||
                ||||   (1) New Game    |                   ||||
                ||||   (2) Scores      |                   ||||
                ||||   (3) Settings    |                   ||||
                ||||   (4) Authors     |                   ||||
                ||||                   |                   ||||
                ||||   (0) Exit        |                   ||||
                ||||                   |      --==*==--    ||||
                ||||__________________ | __________________||||
                ||/===================\|/===================\||
                `--------------------~___~-------------------''
"""

story = 'Pewnego dnia coś tam coś tam. A potem znalazłem się w lochach pełnych skarbów. ' \
        + 'Niestety pilnują je straszne potwory.'


def display_menu():
    ui.display_simple_message(book_menu)


def fragment_sentence(sentence, part_len=15):
    parts = []
    words = sentence.split(' ')
    row_length = 0
    row = ''
    for i, word in enumerate(words):
        row_length += len(word) + 1
        if row_length > part_len:
            parts.append(row)
            row = ''
            row_length = 0
        row += word + ' '
        if i == len(words) - 1:
            parts.append(row)
    return parts


def display_story():
    story_book = 'story_book.txt'
    story_book = graphic.read(story_book)
    ui.display_board(story_book, 25)

    fragmenting_story = fragment_sentence(story)

    row_index = 4
    for row in fragmenting_story:
        ui.print_in_pos(row_index, 32, row)
        row_index += 1
    ui.print_in_pos(21, 1, '')


def play_new_game():
    # Load 1st level
    current_level = 'level_1_items.txt'
    level_board = engine.load_level(current_level)
    level_mask = engine.create_mask(level_board)

    # Custom your player, change condition to skip personalization
    if not True:
        player = Creature(role=Role.Player)
        engine.read_player_start_position(level_board, player)
    else:
        player = personalization_controller.create_player()
        engine.read_player_start_position(level_board, player)

    # Init enemies and boss
    enemies = engine.read_enemies(level_board)
    boss = engine.init_boss(level_board)

    # Store characters in list
    characters = [player]
    characters.extend(enemies)
    characters.extend(boss)

    # Display story
    ui.clear_console()
    display_story()
    input_game.wait_for_reaction()

    # Play the game
    coursor.KeyboardDisable.hide_and_block()
    gameplay_controller.play(level_board, level_mask, characters)
    coursor.KeyboardDisable.show_and_unblock()


def display_scores():

    headers = deepcopy(scores.HEADERS)
    headers.insert(0, 'lp.')
    list_of_list_scores = scores.read()
    list_of_list_scores.sort(key=lambda x: int(x[1]), reverse=True)
    counter = 1
    for i, score in enumerate(list_of_list_scores):
        list_of_list_scores[i].insert(0, str(counter))
        counter += 1
    ui.clear_console()
    ui.print_table(list_of_list_scores, headers, "SCORE BOARD")
    input_game.wait_for_reaction()


def run_settings():
    settings_controller.main()


def displays_authors():
    ui.display_authors()


def run_operation(option):
    if option == 1:
        play_new_game()
    elif option == 2:
        display_scores()
    elif option == 3:
        run_settings()
    elif option == 4:
        ui.display_authors()
    elif option == 0:
        exit()
    else:
        raise KeyError()


def main():
    offset = 25
    operation = None

    while operation != '0':
        ui.clear_console()
        display_menu()
        try:
            operation = input_game.get_input(
                ui.color_sentence(Fore.GREEN, ui.add_sentence_offset("Your pick: ", offset)))
            run_operation(int(operation))
        except KeyError:
            ui.display_error_message(ui.add_sentence_offset("There is no such option.", offset))
            input_game.wait_for_reaction()
        except ValueError:
            ui.display_error_message(ui.add_sentence_offset("Please enter a number!", offset))
            input_game.wait_for_reaction()
