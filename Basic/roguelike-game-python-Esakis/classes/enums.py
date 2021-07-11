from enum import Enum


class Genre(Enum):
    Human = 1
    Goblin = 2
    Dragon = 3
    Elf = 4
    Ghost = 5
    NoGenre = 0


class Role(Enum):
    NoRole = 0
    Player = 1
    Enemy = 2
    NPC = 3
    Boss = 4
    BossPart = 5


class ItemTypes(Enum):
    NoType = 0
    Weapons = 1
    Food = 2
    Key = 3
    Money = 4


class BoxFunctions(Enum):
    NoFunction = 0
    Tutorial = 1
    Message = 2