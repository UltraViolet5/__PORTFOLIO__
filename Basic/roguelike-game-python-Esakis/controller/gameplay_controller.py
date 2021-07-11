import datetime
from time import sleep

import actions as act
import engine
import util
from classes.enums import BoxFunctions, ItemTypes
from controller import enemy_controller, main_controller
from model.levels import icons
from model.scores import scores
from view import ui , input_game


tutorial_displayed = False


def render(messages, level_board, level_mask, characters):
    global tutorial_displayed
    for message in messages:
        if message is not None and not tutorial_displayed and message.function == BoxFunctions.Tutorial:
            engine.render(message, level_board, level_mask, characters)
            tutorial_displayed = True
            return
        elif message is not None and message.function != BoxFunctions.Tutorial:
            engine.render(message, level_board, level_mask, characters)
            return
    engine.render(None, level_board, level_mask, characters)


def actions(level_board, characters):
    player = engine.get_player(characters)

    item_message = act.get_item(level_board, player)
    door_message = act.open_door(level_board, player)
    npc_message = act.talk_to_npc(level_board, player)
    goblin_message = act.goblin_message(level_board, characters, player)
    trap_message = act.fell_into_trap(level_board, player)
    treasure_message = act.get_treasure(level_board, player)

    return [door_message, npc_message, goblin_message, trap_message, item_message, treasure_message]


def has_won(level_board):
    won = True
    for row in level_board:
        for cell in row:
            if cell == icons.treasure:
                won = False
                break
        if not won:
            break
    return won


def play(level_board, level_mask, characters):
    player = engine.get_player(characters)
    render([None], level_board, level_mask, characters)

    is_running = True
    while is_running:
        key = util.key_pressed()

        if key == 'q':
            is_running = False
        elif key == 'w':
            player.move_up(level_board, characters)
        elif key == 's':
            player.move_down(level_board, characters)
        elif key == 'a':
            player.move_left(level_board, characters)
        elif key == 'd':
            player.move_right(level_board, characters)
        elif key == "e":
            act.player_hit(characters)

        enemy_controller.AI(level_board, characters)

        # ACTIONS
        messages = actions(level_board, characters)

        # DISPLAY FINAL FRAME
        render(messages, level_board, level_mask, characters)

        # END GAME CONDITION
        if player.current_life == 0:
            is_running = False
            ui.clear_screen()
            ui.display_logo()
            print("                                 GAME OVER")
            input_game.wait_for_reaction()
        # WON CONDITION
        if has_won(level_board):
            is_running = False
            ui.clear_screen()
            ui.display_logo()
            print("                                 YOU WON!")
            player_gold = str(next(gold for gold in player.inventory if gold.type == ItemTypes.Money).amount)
            today = str(datetime.date.today())
            score_record = [player.name, player_gold, today]
            scores.update(score_record)
            sleep(2.0)
            ui.clear_screen()
            main_controller.display_scores()




