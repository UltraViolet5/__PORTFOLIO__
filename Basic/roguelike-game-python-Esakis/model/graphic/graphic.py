""" Graphic module

Read file txt with ascii graphic.
"""

import os
from model import data_manager

DATA_DIRECTORY = "model/graphic/"


def read(file_name):
    """Read file "model/graphic/{file_name}\""""
    path = DATA_DIRECTORY + file_name
    with open(path, 'r', encoding='utf-8') as file:
        level = file.readlines()
        level = [line.replace('\n', '') for line in level]

        return level


def delete(file_name):
    path = DATA_DIRECTORY + file_name
    os.remove(path)
