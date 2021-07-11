from classes.item import Item
from classes.enums import ItemTypes


class ItemsData:
    key = Item(name='Key', type_=ItemTypes.Key, icon='♪')
    coin = Item(name='Gold', type_=ItemTypes.Money, icon='○')
    sword = Item(name='Short sword', type_=ItemTypes.Weapons, icon='†')

    items = {}
    items['♪'] = key
    items['○'] = coin
    items['†'] = sword
