import engine

from copy import deepcopy
from classes.creature import Creature
from classes.message_box import MessageBox
from classes.enums import BoxFunctions, Role
from controller import enemy_controller
from model.items.items import ItemsData
from model.levels import icons
from view import sounds


def get_treasure(level_board, player):
    if check_close_icon(level_board, player) is not None:
        message = 'Nice! I found a treasure! I\'ll be reach.'
        close_item, pos_x, pos_y = check_close_icon(level_board, player)

        if close_item == icons.treasure:
            treasure = deepcopy(ItemsData().coin)
            treasure.amount = icons.treasure_value
            player.add_item_to_inventory(treasure)
            engine.draw_mark_on_board(level_board, pos_x, pos_y, icons.treasure_empty)
            return engine.get_message_box(message, player, level_board)


def fell_into_trap(level_board, player):
    message = 'Oh, it\'s a trap! It hurt me...'

    if icons.trap == engine.get_icon(player.pos_x, player.pos_y, level_board):
        player.take_damage(3)
        return engine.get_message_box(message, player, level_board)


def goblin_message(level_board, characters, player):
    close_enemy, pos_x, pos_y = check_close_enemies(characters)
    message = "This is a bad goblin.Your fight with him has just begun." \
              "Press \"e\" to hit"

    if close_enemy:
        return MessageBox(player.pos_x, player.pos_y, message, level_board, function=BoxFunctions.Tutorial)


def open_door(level_board, player=Creature()):
    if check_close_icon(level_board, player) is not None:
        close_item, pos_x, pos_y = check_close_icon(level_board, player)
        player_items = [item.name for item in player.inventory]

        if close_item == icons.closed_door and ItemsData().items[ItemsData.key.icon].name in player_items:
            engine.draw_mark_on_board(level_board, pos_x, pos_y, icons.opened_door)
            item_to_remove_index = player.get_item_index_by_name(ItemsData().key.name)
            player.inventory.pop(item_to_remove_index)
            return None

        elif close_item == icons.closed_door and ItemsData().items[ItemsData.key.icon].name not in player_items:
            message = 'Closed! I need a key.'
            return engine.get_message_box(message, player, level_board)


def talk_to_npc(level_board, player=Creature()):
    if check_close_icon(level_board, player) is not None:
        close_item, pos_x, pos_y = check_close_icon(level_board, player)

        if close_item == icons.npc:
            message = "Hi, I've been a prisoner of this dungeon for many years..." \
                      " To get through this door you need to get the key."
            return engine.get_message_box(message, player, level_board)


def check_close_enemies(characters):
    player = engine.get_player(characters)
    enemies = engine.get_enemies(characters)

    for enemy in characters:
        if player.pos_x - 1 == enemy.pos_x and player.pos_y == enemy.pos_y:
            return True, enemy.pos_x, enemy.pos_y
        elif player.pos_x + 1 == enemy.pos_x and player.pos_y == enemy.pos_y:
            return True, enemy.pos_x, enemy.pos_y
        elif player.pos_x == enemy.pos_x and player.pos_y + 1 == enemy.pos_y:
            return True, enemy.pos_x, enemy.pos_y
        elif player.pos_x == enemy.pos_x and player.pos_y - 1 == enemy.pos_y:
            return True, enemy.pos_x, enemy.pos_y
    return False, -1, -1


def check_close_icon(level_board, player):
    """Check for close interactive item around player.
    Returns:
        icon of item -> str, position x -> int, and y -> int
    """
    if level_board[player.pos_y][player.pos_x - 1] in icons.interactive_elements:
        x = player.pos_x - 1
        y = player.pos_y
        icon = level_board[player.pos_y][player.pos_x - 1]
        return icon, x, y
    elif level_board[player.pos_y][player.pos_x + 1] in icons.interactive_elements:
        x = player.pos_x + 1
        y = player.pos_y
        icon = level_board[player.pos_y][player.pos_x + 1]
        return icon, x, y
    elif level_board[player.pos_y - 1][player.pos_x] in icons.interactive_elements:
        x = player.pos_x
        y = player.pos_y - 1
        icon = level_board[player.pos_y - 1][player.pos_x]
        return icon, x, y
    elif level_board[player.pos_y + 1][player.pos_x] in icons.interactive_elements:
        x = player.pos_x
        y = player.pos_y + 1
        icon = level_board[player.pos_y + 1][player.pos_x]
        return icon, x, y


def get_item(level_board, player):
    """Get item from the ground if there is the item in position of player."""
    available_items = ItemsData()
    item = engine.get_icon(player.pos_x, player.pos_y, level_board)

    if item in available_items.items.keys():
        player_items = [item.name for item in player.inventory]

        if available_items.items[item].name not in player_items:
            player.inventory.append(deepcopy(available_items.items[item]))
        else:
            item_index = player.get_item_index_by_name(available_items.items[item].name)
            player.inventory[item_index].amount += 1
        engine.clear_field(level_board, player.pos_x, player.pos_y)

        if item == ItemsData.sword.icon:
            player.damage += 5
            message = 'Nice! I found a sword. I\'ll be doing more damage. '
            return engine.get_message_box(message, player, level_board)

    elif item == icons.life:
        player.healing(icons.life_regeneration)
        engine.clear_field(level_board, player.pos_x, player.pos_y)


def player_hit(characters):
    enemies = engine.get_enemies(characters)
    boss = engine.get_boss(characters)
    boss_parts = engine.get_boss_parts(characters)
    player = engine.get_player(characters)
    is_enemy_next, pos_x, pos_y = check_close_enemies(characters)

    if is_enemy_next:
        enemy_next = engine.get_enemy(pos_x, pos_y, characters)
        if enemy_next.role == Role.Enemy:
            enemy_next.take_damage(player.damage)
        elif enemy_next.role == Role.Boss or enemy_next.role == Role.BossPart:
            boss.take_damage(player.damage)
        sounds.play_input_beep()

        if enemy_next.current_life <= 0 and enemy_next.role != Role.Boss:
            enemy_controller.remove_death_enemy(enemy_next, characters)
        if boss.current_life <= 0:
            enemy_controller.remove_death_boss(characters)
