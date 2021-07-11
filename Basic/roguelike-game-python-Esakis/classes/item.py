from classes.enums import ItemTypes


class Item:
    pos_x = 0
    pos_y = 0

    def __init__(self, name='No name', type_=ItemTypes.NoType, icon='N', amount=1):
        self.name = name
        self.type = type_
        self.icon = icon
        self.amount = amount

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_attributes(self):
        return [str(self.icon), str(self.name), str(self.type), str(self.amount)]

    @staticmethod
    def get_headers():
        return ['Icon', 'Name', 'Type', 'Amount']
