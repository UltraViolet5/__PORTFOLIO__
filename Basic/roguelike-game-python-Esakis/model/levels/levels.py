""" Level module

Data structure:
    - Level created in http://asciiflow.com/
    - Walls: ╔ ═ ╗║╚ ╝
    - Door: ∕
    - Closed door: //
    - Life regeneration: ♥
    - Start player position: X
    - Coins: ◦ or ◌ or ○
"""

import os
from model import data_manager

DATA_DIRECTORY = "model/levels/"
HEADERS = ["id", "name", "level", "date"]


def create(table, file_name):
    path = DATA_DIRECTORY + file_name
    data_manager.write_table_to_file(path, table)


def read(file_name):
    """Read file "model/levels/{file_name}" and remove empty records."""
    path = DATA_DIRECTORY + file_name
    with open(path, 'r', encoding='utf-8') as file:
        level = file.readlines()
        level = [line.replace('\n', '') for line in level]

        return level


def update(table, file_name, separator=';', one_customer=True):
    path = DATA_DIRECTORY + file_name
    try:
        with open(path, 'a+') as file:
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file.write('\n')
            if one_customer:
                row = separator.join(table)
                file.write(row + "\n")
            else:
                for record in table:
                    row = separator.join(record)
                    file.write(row + "\n")
    except IOError:
        return []


def delete(file_name):
    path = DATA_DIRECTORY + file_name
    os.remove(path)
