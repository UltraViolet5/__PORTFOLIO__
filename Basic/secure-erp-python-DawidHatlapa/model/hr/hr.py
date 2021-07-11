""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
import os
from model import data_manager, util
from datetime import *

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def create(table):
    data_manager.write_table_to_file(DATAFILE, table)


def read():
    """Read file "model/crm/crm.csv" and remove empty records."""
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


def birth_day_to_data_time(birth_day):
    day_of_birth = birth_day.split("-")
    day_of_birth_data_time = datetime(int(day_of_birth[0]), int(day_of_birth[1]), int(day_of_birth[2]))

    return day_of_birth_data_time


def get_birthday_date_and_name():
    employees = read()
    employee_list = []
    for employee in employees:
        name = employee[1]
        birth_day_in_data_time = birth_day_to_data_time(employee[2])
        data = [name, birth_day_in_data_time]
        employee_list.append(data)

    return employee_list


def count_time_to_next_birth_day(day_of_birth):
    current_data = datetime.utcnow()
    current_data = datetime(current_data.year, current_data.month, current_data.day)
    born_date = day_of_birth
    next_birthdays_date = datetime(current_data.year, born_date.month, born_date.day)
    days_to_next = datetime(1, 1, 1)
    if next_birthdays_date > current_data:
        days_to_next = next_birthdays_date - current_data
    elif next_birthdays_date < current_data:
        next_birthdays_date = datetime(current_data.year + 1, born_date.month, born_date.day)
        days_to_next = next_birthdays_date - current_data
    days_to_next = days_to_next.days

    return int(days_to_next)
