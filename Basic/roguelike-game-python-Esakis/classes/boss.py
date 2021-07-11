from classes.creature import Creature
from classes.enums import Role
from model.levels import icons


class Boss(Creature):

    def __init__(self, x=0, y=0, size=2, name="NO name", life=20, icon='B', damage=6, role=Role.Boss):
        super().__init__(name=name, life=life, icon=icon, x=x, y=y)
        self.size = size
        self.body_parts = self.init_body(size)
        self.damage = damage
        self.role = role

    def init_body(self, size):
        body = []
        for i in range(size):
            body.append([])
            for j in range(size):
                body[i].append(self.icon)
        return body

    def set_position(self, x, y, level_board):
        if level_board[y][x] == ' ' or level_board[y][x] == 'B' \
                and level_board[y][x + 1] == ' ' or level_board[y][x + 1] == 'B'\
                and level_board[y + 1][x + 1] == ' ' or level_board[y + 1][x + 1] == 'B'\
                and level_board[y + 1][x] == ' ' or level_board[y + 1][x] == 'B':
            self.pos_x = x
            self.pos_y = y
        else:
            raise ValueError("Field is not empty.")

    # FIXME FUNC PORUSZANIA ZADZIALAJĄ TYLKO DLA BOSA 2x2
    def move_up(self, level_board, characters):
        if self.get_top_icon(self.pos_x, self.pos_y, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x, self.pos_y - 1, characters)\
                and self.get_top_icon(self.pos_x + 1, self.pos_y, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x + 1, self.pos_y - 1, characters):
            self.pos_y -= 1

    def move_down(self, level_board, characters):
        if self.get_lower_icon(self.pos_x, self.pos_y + 1, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x, self.pos_y + 2, characters)\
                and self.get_lower_icon(self.pos_x + 1, self.pos_y + 1, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x + 1, self.pos_y + 2, characters):
            self.pos_y += 1

    def move_right(self, level_board, characters):
        if self.get_right_icon(self.pos_x + 1, self.pos_y, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x + 2, self.pos_y, characters)\
                and self.get_right_icon(self.pos_x + 1, self.pos_y + 1, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x + 2, self.pos_y + 1, characters):
            self.pos_x += 1

    def move_left(self, level_board, characters):
        if self.get_left_icon(self.pos_x, self.pos_y, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x - 1, self.pos_y, characters)\
                and self.get_left_icon(self.pos_x, self.pos_y + 1, level_board) not in icons.collision_elements\
                and not self.is_other_character_position(self.pos_x - 1, self.pos_y + 1, characters):
            self.pos_x -= 1

    def move_to_goal(self, x, y, level_board, characters, body_parts) -> None:
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
            for part in body_parts:
                part.pos_x += 1
        elif x < self.pos_x:
            self.move_left(level_board, characters)
            for part in body_parts:
                part.pos_x -= 1
        elif y > self.pos_y:
            self.move_down(level_board, characters)
            for part in body_parts:
                part.pos_y += 1
        elif y < self.pos_y:
            self.move_up(level_board, characters)
            for part in body_parts:
                part.pos_y -= 1

    def get_top_icon(self, x, y, level_board):
        return level_board[y - 1][x]

    def get_lower_icon(self, x, y, level_board):
        return level_board[y + 1][x]

    def get_left_icon(self, x, y, level_board):
        return level_board[y][x - 1]

    def get_right_icon(self, x, y, level_board):
        return level_board[y][x + 1]
