from model.hr import hr
from view import terminal as view
from datetime import *


def list_employees():
    view.clear_console()
    employee = hr.read()
    view.print_table(employee, hr.HEADERS, title="All employees")
    view.wait_for_reaction()
    view.clear_console()
    display_menu()


def accept_data(data, label):
    while not view.get_yes_or_no(f"Is the value \"{data}\" correct? "):
        data = view.get_input(label)
    return data


def get_employee_data():
    data_label = hr.HEADERS

    # id_label = f"Please provide {data_label[0]} of new employee:  "
    # id = view.get_input(id_label)
    # id = accept_data(id, id_label)
    # unikalny id

    name_label = f"Please provide {data_label[1]} of new employee:  "
    name = view.get_input(name_label)
    name = accept_data(name, name_label)

    date_of_birth_label = f"Please provide {data_label[2]} of new employee i n format yyyy-mm-dd:  "
    date_of_birth = view.get_input(date_of_birth_label)
    date_of_birth = accept_data(date_of_birth, date_of_birth_label)

    department_label = f"Please provide {data_label[3]} of new employee:  "
    department = view.get_input(department_label)
    department = accept_data(department, department_label)

    clearance_label = f"Please provide {data_label[4]} of new employee:  "
    clearance = view.get_input(clearance_label)
    clearance = accept_data(clearance, clearance_label)

    return [name, date_of_birth, department, clearance]


def add_employee():
    view.clear_console()
    view.print_message("Add new employee:\n")

    new_employee = get_employee_data()

    hr.update(new_employee)

    view.print_message("\nnew employee was added correctly!")
    view.wait_for_reaction()


def get_updated_employee_data(employee, headers):
    index = 1

    while index < len(employee):
        ask_label = f"Would you like to edit {headers[index]}? "
        new_data_label = f"Provide new {headers[index]}: "
        decision = view.get_yes_or_no(ask_label)
        if decision:
            employee[index] = view.get_input(new_data_label)
            employee[index] = accept_data(employee[index], new_data_label)
        index += 1
    return employee


def update_employee():
    view.clear_console()
    view.print_message("update employee:\n")

    employees = hr.read()
    view.print_table(employees, hr.HEADERS, title="All Employees")

    update_label = "Provide employees id to update: "
    employee_index = view.get_input_number(update_label, max_value=len(employees)) - 1

    employee_to_update = employees.pop(int(employee_index))
    updated_employee = get_updated_employee_data(employee_to_update, hr.HEADERS)
    employees.insert(int(employee_index), updated_employee)

    hr.create(employees)

    view.print_message("Customer was updated correctly.")
    view.wait_for_reaction()


def delete_employee():
    view.clear_console()
    view.print_message("Delete employee: ")

    employees = hr.read()
    view.print_table(employees, hr.HEADERS, title="All Employees")

    delete_label = "Provide employee id to remove: "
    employee_index = view.get_input_number(delete_label, max_value=len(employees))

    employees.pop(int(employee_index)-1)

    hr.create(employees)

    view.print_message("Employee was removed correctly.")
    view.wait_for_reaction()


def get_oldest_and_youngest():
    view.clear_console()
    employees = hr.read()
    employees.sort(key=lambda employee: employee[2])
    oldest_employee = employees[0][1]
    youngest_employee = employees[len(employees) - 1][1]
    oldest_and_youngest = oldest_employee, youngest_employee
    oldest_and_youngest_label = "Oldest and youngest employees is : "
    view.print_general_results(oldest_and_youngest, oldest_and_youngest_label)
    view.wait_for_reaction()

    return oldest_employee, youngest_employee


def get_average_age():
    view.clear_console()
    current_year = int(datetime.now().year)
    all_together = 0
    number_of_employee = 0
    employees = hr.read()
    for employee in employees:
        date_list = employee[2].split("-")
        year = int(date_list[0])
        all_together += year
        number_of_employee += 1

    average = current_year - all_together // number_of_employee

    average_label = "the average age of the employees is"
    view.print_general_results(average, average_label)
    view.wait_for_reaction()

    return average


def next_birthdays():
    view.clear_console()
    employee_list = hr.get_birthday_date_and_name()
    next_birthdays_list = []
    for employee in employee_list:
        days_to_next_birthday = hr.count_time_to_next_birth_day(employee[1])
        if days_to_next_birthday < 14:
            next_birthdays_list.append(employee[0])
            next_birthdays_list.append(str(employee[1].date()))

    next_birthdays_label = "Next birthday has: "
    view.print_general_results(next_birthdays_list, next_birthdays_label)
    view.wait_for_reaction()

    return next_birthdays_list


def count_employees_with_clearance():
    view.clear_console()
    employees = hr.read()
    sep = " "
    employees.sort(key=lambda employee: employee[4])
    list_of_employees_with_lowest_clearance = []
    for worker in employees:
        int_worker_clearance = int(worker[4])

        if int_worker_clearance > 0:
            worker_str = sep.join(worker)
            list_of_employees_with_lowest_clearance.append(worker_str)
    list_of_employees_with_lowest_clearance.sort(key=lambda emplo: emplo[4])
    employees_with_lowest_clearance_label = "number of employees with clearances is :"
    view.print_general_results(len(list_of_employees_with_lowest_clearance), employees_with_lowest_clearance_label)
    view.wait_for_reaction()


def count_employees_per_department():
    view.clear_console()
    employees = hr.read()
    sep = " "
    employees.sort(key=lambda emplo: emplo[3])
    dict_of_emplo_in_departament = {}
    for employee in employees:
        name_of_departament = employee[3]
        if name_of_departament not in dict_of_emplo_in_departament:
            dict_of_emplo_in_departament[name_of_departament] = 1
        elif name_of_departament in dict_of_emplo_in_departament:
            dict_of_emplo_in_departament[name_of_departament] += 1
    dict_of_emplo_in_departament_label = "Employee numbers by department"
    view.print_general_results(dict_of_emplo_in_departament, dict_of_emplo_in_departament_label)
    view.wait_for_reaction()


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
