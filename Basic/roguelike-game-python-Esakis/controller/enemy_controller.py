# Behavior of the enemies
from copy import deepcopy

import engine
import util
from classes.enums import Role

from view import sounds


def AI(level_board, characters):
    player = engine.get_player(characters)
    enemies = engine.get_enemies(characters)
    view_range = 8

    # Standard enemy behavior
    for enemy in enemies:
        distance_to_player = util.distance(enemy.pos_x, enemy.pos_y, player.pos_x, player.pos_y)
        if distance_to_player == 1:
            player.take_damage(enemy.damage)
            sounds.attack_beep()
        if distance_to_player < view_range:
            enemy.move_to_goal(player.pos_x, player.pos_y, level_board, characters)
            sounds.play_step_beep()

    # Boss behavior
    if len([boss for boss in characters if boss.role == Role.Boss]) == 1:
        boss_parts = engine.get_boss_parts(characters)
        boss = engine.get_boss(characters)
        boss_distance_to_player = util.distance(boss.pos_x, boss.pos_y, player.pos_x, player.pos_y)
        if 1 < boss_distance_to_player < view_range:
            boss.move_to_goal(player.pos_x, player.pos_y, level_board, characters, boss_parts)
        if boss_distance_to_player == 1:
            player.take_damage(boss.damage)
            sounds.attack_beep()
        for boss_part in boss_parts:
            distance_to_player = util.distance(boss_part.pos_x, boss_part.pos_y, player.pos_x, player.pos_y)
            if distance_to_player == 1:
                player.take_damage(boss.damage)
                sounds.attack_beep()


def remove_death_enemy(enemy, characters):
    enemy_index = characters.index(enemy)
    characters.pop(enemy_index)
    sounds.dead_beep()


def remove_death_boss(characters):
    # Fixme usuwam wszystkich bosów a nie jednego konkretnego
    characters.pop(-1)
    characters.pop(-1)
    characters.pop(-1)
    characters.pop(-1)
    sounds.dead_beep()
