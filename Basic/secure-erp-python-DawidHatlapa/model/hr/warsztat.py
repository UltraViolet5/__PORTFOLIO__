import copy
from datetime import *
from view import terminal as view


#
# def is_leap_year(year):
#     x = year % 400 == 0
#     y = year % 4 == 0
#     z = year % 100 == 0
#
#     # a = x and z
#     # b = y and z
#
#     return x or y and not z
#
#
# def leap_year_or_normal_year(date_of_birth):
#     # date_of_birth data format [[yyyy][mm][dd]]
#     long_month = list(range(1, 32))
#     short_month = list(range(1, 31))
#     february = list(range(1, 29))
#     long_february = list(range(1, 30))
#     year = [long_month, february, long_month, short_month, long_month, short_month, long_month,
#             long_month, short_month, long_month, short_month, long_month]
#
#     leap_year = is_leap_year(date_of_birth[0])
#     if leap_year:
#         year[1] = long_february
#     else:
#         year[1] = february
#
#     return year
#
#
# def part_of_year(date_of_birth, year, current_data):
#     number_of_days_in_current_month = year[current_data[1] - 1]
#     current_day = year[current_data[1] - 1][(current_data[2]) - 1]
#     list_of_month = list(range(int(current_data[1]) - 1))
#
#     tmp_year = copy.deepcopy(year)
#
#     for month in list_of_month:
#         del tmp_year[month]
#
#     month_to_count = tmp_year[0]
#
#     return tmp_year
#
#
# def days_to_next_birthday(date_of_birth, year, current_data):
#     month_of_birth = int(date_of_birth[1]) - 1
#     current_month = current_data[1] - 1
#     day_of_birth = int(date_of_birth[2])
#     current_day = current_data[2]
#     current_year = current_data[0]
#     year_of_birth = int(date_of_birth[0])
#     number_of_days = 0
#     number_of_month = 0
#
#     year_part = part_of_year()
#
#     for month in year_part:
#         if number_of_month == month_of_birth:
#             break
#         number_of_month += 1
#         for day in month:
#             if number_of_days == date_of_birth[2]:
#                 break
#             number_of_days += 1
#
#     return number_of_days


########################################################################################################################
# controller
#
# def next_birthdays():
#     current_data = [2020, 10, 22]
#     employees = [["1", "adam", "1990-10-24"], ["2", "Zenek", "1990-03-12"], ["3", "Zenia", "1990-11-12"]]
#     names_next_birthdays = []
#
#     for employee in employees:
#         year = leap_year_or_normal_year(employee[2])
#         count_days_to_birthdays = days_to_next_birthday(employee[2], year, current_data)


# def count_time_to_next_birth_day(day_of_birth):
#     current_data = datetime.utcnow()
#     current_data = datetime(current_data.year, current_data.month, current_data.day)
#     born_date = day_of_birth
#     next_birthdays_date = datetime(current_data.year, born_date.month, born_date.day)
#     days_to_next = datetime(1, 1, 1)
#     if next_birthdays_date > current_data:
#         days_to_next = next_birthdays_date - current_data
#     elif next_birthdays_date < current_data:
#         next_birthdays_date = datetime(current_data.year + 1, born_date.month, born_date.year)
#         days_to_next = next_birthdays_date - current_data
#     days_to_next = days_to_next.days
#
#     return int(days_to_next)
#
#
# print(count_time_to_next_birth_day(datetime(2020, 12, 27)))
# def print_slownik(res):
#     data_typ = type(res)
#
#     if data_typ == dict:
#         list_of_pairs = []
#         sep = ";"
#
#         for element in res:
#             pair = []
#             dictonary_sep = ":"
#             pair.append(element)
#             pair.append(str(res[element]))
#             pair_with_sep = dictonary_sep.join(pair)
#             list_of_pairs.append(pair_with_sep)
#
#     convertion_dict_to_string =sep.join(list_of_pairs)
#     print(convertion_dict_to_string)
#
#
# dicton = {"ja": 1, 'dwa': 2, "story": 3}
# print_slownik(dicton)

# new_data = datetime.now().date()
# str_new_data = str(new_data)
#
# print(new_data)


def count_employees_with_clearance():
    # view.clear_console()
    # employees = hr.read()
    employees = [["1", "adam", "1990-10-24", "hr", "3"], ["2", "Zenek", "1990-03-12", "it", "3"],
                 ["3", "Zenia", "1990-11-12", "it", "4"]]
    sep = " "
    employees.sort(key=lambda employee: employee[4])
    list_of_employees_with_lowest_clearance = []
    employee_with_lowest_clearance = employees[0]
    for worker in employees:
        int_worker_clearance = int(worker[4])

        if int_worker_clearance <= int(employee_with_lowest_clearance[4])+1:
            worker_str = sep.join(worker)
            list_of_employees_with_lowest_clearance.append(worker_str)
    list_of_employees_with_lowest_clearance.sort(key=lambda clerk: clerk[4])
    separator = ':'
    employees_with_lowest_clearance_label = "employees with lowest clearance is :"
    view.print_general_results(list_of_employees_with_lowest_clearance, employees_with_lowest_clearance_label)
    view.wait_for_reaction()


count_employees_with_clearance()
