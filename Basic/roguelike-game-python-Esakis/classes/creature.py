from colorama import *

from classes.enums import Genre, Role
from classes.item import Item
from model.items.items import ItemsData
from model.levels import icons


class Creature:

    def __init__(self, name='No name', life=10, strength=4, icon=u'♀',
                 color=Fore.WHITE, points=0, x=0, y=0, genre=Genre.NoGenre, role=Role.NoRole):
        self.name = name
        self.color = color
        self.icon = icon
        self.life = life
        self.current_life = self.life
        self.strength = strength
        self.level = 1
        self.inventory = []
        self.points = points
        self.pos_x = x
        self.pos_y = y
        self.genre = genre
        self.role = role
        self.damage = self.strength

    def set_position(self, x, y, level_board):
        if level_board[y][x] == ' ' or level_board[y][x] == 'X':
            self.pos_x = x
            self.pos_y = y
        else:
            raise ValueError("Field is not empty.")

    def move_up(self, level_board, characters):
        if level_board[self.pos_y - 1][self.pos_x] not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x, self.pos_y - 1, characters):
            self.pos_y -= 1

    def move_down(self, level_board, characters):
        if level_board[self.pos_y + 1][self.pos_x] not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x, self.pos_y + 1, characters):
            self.pos_y += 1

    def move_right(self, level_board, characters):
        if level_board[self.pos_y][self.pos_x + 1] not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x + 1, self.pos_y, characters):
            self.pos_x += 1

    def move_left(self, level_board, characters):
        if level_board[self.pos_y][self.pos_x - 1] not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x - 1, self.pos_y, characters):
            self.pos_x -= 1

    def get_item_index_by_name(self, name):
        for i, item in enumerate(self.inventory):
            if item.name == name:
                return i

    def is_other_character_position(self, x, y, characters):
        for enemy in characters:
            if enemy.pos_x == x and enemy.pos_y == y:
                return True
        return False

    def move_to_goal(self, x, y, level_board, characters) -> None:
        """
        Move to goal.
        Args:
            characters: player and enemies list
            level_board: playground
            x: position coordinate x
            y: position coordinate y

        Returns:
            None
        """
        if x > self.pos_x:
            self.move_right(level_board, characters)
        elif x < self.pos_x:
            self.move_left(level_board, characters)
        elif y > self.pos_y:
            self.move_down(level_board, characters)
        elif y < self.pos_y:
            self.move_up(level_board, characters)

    def take_damage(self, damage) -> None:
        """
        Take damage.

        Args:
            damage: value of damage -> int
        Returns:
            None
        """
        self.current_life -= damage
        if self.current_life < 0:
            self.current_life = 0

    def healing(self, value):
        self. current_life += value
        if self.current_life > self.life:
            self.current_life = self.life

    def add_item_to_inventory(self, item=Item()):
        inventory_items = [item.name for item in self.inventory]
        if item.name in inventory_items:
            item_index = self.get_item_index_by_name(ItemsData.items[item.icon].name)
            self.inventory[item_index].amount += item.amount
        else:
            self.inventory.append(item)
