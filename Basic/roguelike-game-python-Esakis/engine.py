from copy import deepcopy

from classes.boss import Boss
from classes.message_box import MessageBox
from model.levels import levels
from classes.creature import *

import util
from view import input_game
from view.ui import display_gameplay_frame


def create_board(level_board):
    """
    Creates a new game board based on input parameters.

    Args:
    level_board: List with designed level

    Returns:
    list: Game board
    """
    rows = len(level_board)
    cols = len(level_board[0])

    for row in level_board:
        if len(row) > cols:
            cols = len(row)

    board = []
    for i in range(rows):
        board.append(' ' * cols)
    return board


def create_mask(board):
    mask = create_board(board)
    for i, row in enumerate(mask):
        mask[i] = [0 for cell in row]
    return mask


def join_two_boards(board1, board2):
    result = deepcopy(board1)
    for i, row in enumerate(board2):
        for j, sign in enumerate(row):
            if sign != " ":
                result[i] = util.insert_mark(result[i], sign, j)
    return result


def read_player_start_position(level_board, character, mark='X'):
    """
    Find start position in current level and set character position. Next remove start position mark.

    Args:
    level_board: The level board
    player: Hero instance
    mark: Place to put player

    Returns:
    Nothing
    """
    player_found = False
    for i, row in enumerate(level_board):
        for j, col in enumerate(row):
            if level_board[i][j] == mark:
                character.set_position(j, i, level_board)
                clear_field(level_board, j, i)
                player_found = True
                break
        if player_found:
            break


def read_enemies(level_board, mark='E'):
    enemies = []
    for i, row in enumerate(level_board):
        for j, col in enumerate(row):
            if level_board[i][j] == mark:
                enemies.append(Creature(name='Goblin', icon='G', x=j, y=i, genre=Genre.Goblin, role=Role.Enemy, life=5))
                clear_field(level_board, j, i)
    return enemies


def refresh_characters_position(board, characters):
    """
    Add character icon with current position on the board
    Returns:
        None
    """
    for character in characters:
        row_with_character = list(board[character.pos_y])
        row_with_character[character.pos_x] = character.icon
        board[character.pos_y] = ''.join(row_with_character)


def clear_field(board, x, y):
    """Clear field in board."""
    board[y] = util.insert_mark(board[y], ' ', x)


def draw_mark_on_board(board, x, y, mark):
    """Clear field in board."""
    board[y] = util.insert_mark(board[y], mark, x)


def load_level(file_name):
    return levels.read(file_name)


def get_message_box(message, player, level_board):
    return MessageBox(player.pos_x, player.pos_y, message, level_board)


def add_message_to_board(message, level_board):
    index = 0
    for k, row in enumerate(level_board):
        if message.y <= k < message.height + message.y:
            level_board[k] = level_board[k][:message.x] + ''.join(message.get_table()[index]) \
                             + level_board[k][message.x + message.width:]
            index += 1
        elif k >= message.height + message.y:
            break


def mask_board(board_to_display, mask):
    masked_board = deepcopy(board_to_display)
    for i, row in enumerate(masked_board):
        masked_row = []
        for j, field in enumerate(row):
            if mask[i][j] == 0:
                masked_row.append('.')
            elif mask[i][j] == 1:
                masked_row.append(masked_board[i][j])
        masked_board[i] = ''.join(masked_row)
    return masked_board


def refresh_mask(level_mask, player, view_range=10):
    for i, row in enumerate(level_mask):
        for j, field in enumerate(row):
            distance_to_player = util.distance(j, i, player.pos_x, player.pos_y)
            if distance_to_player < view_range:
                level_mask[i][j] = 1


def render(message_to_display, level_board, level_mask, characters):
    """
    Calculate dungeon frame to display, and display it.
    Args:
        message_to_display:
        level_board:
        level_mask:
        characters:

    Returns:

    """
    player = get_player(characters)
    board_to_display = deepcopy(level_board)

    # TUTAJ ODSWIEŻAJ DYNAMICZNE OBIEKTY
    refresh_characters_position(board_to_display, characters)

    # ZAMASKUJ NIEODKRYTE CZĘŚCI MAPY
    refresh_mask(level_mask, player)
    masked_board = mask_board(board_to_display, level_mask)

    # WYŚWIETL WIADOMOŚć jeżeli jest przesłana do funkcji jako argument lub wyświetl bez wiadomości
    if message_to_display is not None:
        board_with_message = deepcopy(masked_board)
        add_message_to_board(message_to_display, board_with_message)

        display_gameplay_frame(board_with_message, characters)
    else:
        display_gameplay_frame(masked_board, characters)

    # po wciśnięciu enter usuń message box i odświez klatkę
    if message_to_display is not None:
        input_game.hidden_input()
        display_gameplay_frame(masked_board, characters)


def get_player(characters):
    return next(character for character in characters if character.role == Role.Player)


def get_enemies(characters):
    return list(filter(lambda x: x.role == Role.Enemy, characters))


def get_enemy(x, y, enemies):
    return next(enemy for enemy in enemies if enemy.pos_x == x and enemy.pos_y == y)


def get_boss(characters):
    for character in characters:
        if character.role == Role.Boss:
            return character


def get_boss_parts(characters):
    return list(filter(lambda x: x.role == Role.BossPart, characters))


def get_icon(x, y, level_board):
    return level_board[y][x]


def init_boss(level_board):
    # FIXME Odczytuje tylko bossa o rozmiarach 2x2, na sztywno
    for i, row in enumerate(level_board):
        for j, cell in enumerate(row):
            if level_board[i][j] == icons.boss_start_position:
                boss0 = Boss(name='Monster0', x=j, y=i, life=9)
                clear_field(level_board, j, i)
                boss1 = Boss(name='Monster1', x=j + 1, y=i, role=Role.BossPart)
                clear_field(level_board, j + 1, i)
                boss2 = Boss(name='Monster2', x=j, y=i + 1, role=Role.BossPart)
                clear_field(level_board, j, i + 1)
                boss3 = Boss(name='Monster3', x=j + 1, y=i + 1, role=Role.BossPart)
                clear_field(level_board, j + 1, i + 1)
                return [boss0, boss1, boss2, boss3]


