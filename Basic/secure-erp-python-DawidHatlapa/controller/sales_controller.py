from model.sales import sales
from view import terminal as view
import datetime
from colorama import *


def list_transactions():
    view.clear_console()
    transactions = sales.read()
    view.print_table(transactions, sales.HEADERS)
    view.wait_for_reaction()


def add_transaction():
    view.clear_console()
    inputs = view.get_inputs(['Give Customer: ', 'Give Product: ', 'Give Price: '])
    inputs.append(str(datetime.date.today()))
    sales.update(inputs)
    view.wait_for_reaction()


def update_transaction():
    view.clear_console()
    transactions = sales.read()
    view.print_table(transactions, sales.HEADERS, "Transactions: ")

    is_correct_value = False
    while not is_correct_value:
        transaction_id = view.get_input('Provide a valid transactions id to update profile: ')
        try:
            transaction_id = int(transaction_id)
            if transaction_id > 0 and transaction_id <= len(transactions):
                is_correct_value = True
                transaction_id = int(transaction_id) - 1
            else:
                view.print_error_message("Incorrect value. Try again.")
        except:
            view.print_error_message("Incorrect value. Try again.")

    transaction_to_change = transactions.pop(transaction_id)
    want_change_next_value = True
    while want_change_next_value:
        index = view.get_input(
            'Specify which value you are attempting to change \n1 for Customer id, 2 for Product, 3 for Price, 4 for Date: ')
        choices = ['1', '2', '3', '4']
        while index not in choices:
            view.print_error_message("Incorrect value. Try again!")
            index = view.get_input(
                'Specify which value you are attempting to change \n1 for Customer id, 2 for Product, 3 for Price, 4 for Date: ')
        transaction_to_change[int(index)] = view.get_input("Provide new value: ")
        want_change_next_value = view.get_yes_or_no("Would you like to change another value? ")
    transactions.append(transaction_to_change)
    sales.create(transactions)


def delete_transaction():
    view.clear_console()
    transactions = sales.read()
    view.print_table(transactions, sales.HEADERS)
    index = view.get_input('Provide a valid transactions id to delete profile: ')
    choices = range(len(transactions))
    choices = map(lambda x: str(x + 1), choices)
    while index not in choices:
        view.print_error_message("Incorrect value. Try again!")
        index = view.get_input('Provide a valid transactions id to update profile: ')
    transactions.pop(int(index) - 1)
    sales.create(transactions)
    view.print_message(view.color_sentence(Fore.GREEN, "Transaction was deleted."))
    view.wait_for_reaction()


def get_biggest_revenue_transaction():
    view.clear_console()
    transactions = sales.read()
    revenue = {}
    for transaction in transactions:
        if transaction[2] in revenue.keys():
            revenue[transaction[2]] += float(transaction[3])
        else:
            revenue[transaction[2]] = float(transaction[3])

    the_biggest_transaction = list(revenue.keys())[0]
    for value in revenue:
        if revenue[value] >= revenue[the_biggest_transaction]:
            the_biggest_transaction = value

    view.print_message(
        'The biggest revenue transaction is: ' + the_biggest_transaction + ': ' + str(revenue[the_biggest_transaction]))
    view.wait_for_reaction()


def get_smallest_revenue_transaction():
    view.clear_console()
    transactions = sales.read()
    revenue = {}
    for transaction in transactions:
        if transaction[2] in revenue.keys():
            revenue[transaction[2]] += float(transaction[3])
        else:
            revenue[transaction[2]] = float(transaction[3])

    the_smallest_transaction = list(revenue.keys())[0]
    for value in revenue:
        if revenue[value] < revenue[the_smallest_transaction]:
            the_smallest_transaction = value

    view.print_message('The smallest revenue transaction is: ' + the_smallest_transaction + ': ' + str(
        revenue[the_smallest_transaction]))
    view.wait_for_reaction()


def get_biggest_revenue_product():
    view.clear_console()
    transactions = sales.read()
    revenues = {}
    for transaction in transactions:
        if transaction[2] in revenues.keys():
            revenues[transaction[2]] += float(transaction[3])
        else:
            revenues[transaction[2]] = float(transaction[3])

    the_biggest_product = list(revenues.keys())[0]
    for revenue in revenues:
        if revenues[revenue] > revenues[the_biggest_product]:
            the_biggest_product = revenue

    view.print_message('The biggest revenue product is: ' + the_biggest_product + ': '
                       + str(revenues[the_biggest_product]))
    view.wait_for_reaction()


def count_transactions_between():
    view.clear_console()
    transactions = sales.read()
    start_date = view.get_input("Provide start transaction date (e.g. 2018-02-03): ")
    end_date = view.get_input("Provide end transaction date (e.g. 2020-11-04): ")
    start_date = start_date.split("-")
    end_date = end_date.split("-")
    start_date = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    end_date = datetime.date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    counter = 0
    for index in range(len(transactions)):
        tran_date = transactions[index][4]
        tran_date = tran_date.split("-")
        tran_date = datetime.date(int(tran_date[0]), int(tran_date[1]), int(tran_date[2]))
        if tran_date <= end_date and tran_date >= start_date:
            counter += 1

    view.print_message('Count transactions between equals: ' + str(counter))
    view.wait_for_reaction()


def sum_transactions_between():
    view.clear_console()
    transactions = sales.read()
    min_data = view.get_input("Provide start transaction data (e.g. 2020-10-31): ")
    max_data = view.get_input("Provide end transaction data (e.g. 2020-10-31): ")
    min_data = min_data.split("-")
    max_data = max_data.split("-")
    min_data = datetime.date(int(min_data[0]), int(min_data[1]), int(min_data[2]))
    max_data = datetime.date(int(max_data[0]), int(max_data[1]), int(max_data[2]))
    sum_transaction = 0
    for transaction in transactions:
        current_transaction_data = transaction[4]
        current_transaction_data = current_transaction_data.split("-")
        current_transaction_data = datetime.date(int(current_transaction_data[0]), int(current_transaction_data[1]),
                                                 int(current_transaction_data[2]))
        if current_transaction_data <= max_data and current_transaction_data >= min_data:
            sum_transaction += float(transaction[3])
    view.print_message("Sum equals: " + str(sum_transaction))
    view.wait_for_reaction()


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_smallest_revenue_transaction()
    elif option == 7:
        get_biggest_revenue_product()
    elif option == 8:
        count_transactions_between()
    elif option == 9:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the transaction that made the smallest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
