""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import os
from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def create(table):
    data_manager.write_table_to_file(DATAFILE, table)


def read():
    """Read file "model/sales/sales.csv" and remove empty records."""
    data = data_manager.read_table_from_file(DATAFILE)
    data_without_empty_lines = []
    for index in range(len(data)):
        if (len(data[index]) == 1 and data[index][0] == '') or data[index] == []:
            continue
        data_without_empty_lines.append(data[index])
    return data_without_empty_lines


def update(table, separator=';', one_customer=True):
    try:
        with open(DATAFILE, 'a+') as file:
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file.write('\n')
            if one_customer:
                row = util.generate_id() + separator
                row += separator.join(table)
                file.write(row + "\n")
            else:
                for record in table:
                    row = separator.join(record)
                    file.write(row + "\n")
    except IOError:
        return []


def delete():
    os.remove(DATAFILE)
