import engine
from classes.boss import Boss
from classes.creature import Creature
from classes.enums import Role, ItemTypes
from classes.message_box import MessageBox

current_level = 'level_1_items.txt'
level_board = engine.load_level(current_level)
messaage = MessageBox(0, 0, 'Drzwi są zamknięte! Muszę znależć klucz.', level_board)
box = messaage.get_table()
characters = [Creature(role=Role.Enemy), Boss(role=Role.BossPart), Creature(role=Role.Player), Boss(), Boss(role=Role.BossPart)]

print(engine.get_boss_parts(characters))


