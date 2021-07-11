import math
import util

from classes.enums import BoxFunctions


class MessageBox:

    def __init__(self, x, y, message, level_board, function=BoxFunctions.NoFunction):
        self.message = message
        self.margin = 1
        self.row_length = 20
        self.height = 2 * (self.margin + 1) + math.ceil(len(message) / self.row_length) + 2
        self.width = 2 * (self.margin + 1) + self.row_length
        self.table = self.make_table()
        self.add_message()
        self.x = util.clamp(0, x - int(self.width / 2), len(level_board[0]) - self.width)
        self.y = util.clamp(0, y - int(self.height / 2), len(level_board) - self.height)
        self.function = function

    def get_table(self):
        return self.table

    def add_message(self):
        """
        Add message to the table, that's mean: Add next letter from message to the table, with a margin.

        Returns:
            None
        """
        ending_message = 'Press enter...'
        index = 0
        index2 = 0
        for i, row in enumerate(self.table):
            for j, cell in enumerate(row):

                if j > self.margin and i > self.margin and index < len(self.message) \
                        and j < len(row) - self.margin - 1 and i < len(self.table) - self.margin - 1\
                        and index < len(self.message):
                    self.table[i][j] = self.message[index]
                    index += 1
                elif j > self.margin and i == self.height - 2 - self.margin and index2 < len(ending_message):
                    self.table[i][j] = ending_message[index2]
                    index2 += 1

    def make_table(self):
        """
        Create table for message with specific size.
        Returns:
            table: list with message in frame, ready to render
        """
        table = []
        for i in range(self.height):
            table.append([])
            for j in range(self.width):
                if i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1:
                    table[i].append('#')
                else:
                    table[i].append(' ')
        return table
