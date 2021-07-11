from colorama import Fore
from model.crm import crm
from view import terminal as view


BACK_WORD = 'back'


def list_customers():
    view.clear_console()
    customers = crm.read()
    view.print_table(customers, crm.HEADERS, title='All customers:')
    view.wait_for_reaction()
    view.clear_console()
    display_menu()


def accept_data(data, label):
    while not view.get_yes_or_no(view.color_sentence(Fore.GREEN, f"Is the value \"{data}\" correct? ")):
        data = view.get_input(label)
    return data


def get_customer_data():

    name_label = view.color_sentence(Fore.GREEN, "Provide customer name: ")
    name = view.get_input(name_label)
    if name.lower() == BACK_WORD:
        return
    name = accept_data(name, name_label)

    email_label = view.color_sentence(Fore.GREEN, "Provide customer email: ")
    email = view.get_input(email_label)
    if email.lower() == BACK_WORD:
        return
    email = accept_data(email, email_label)

    subscribe_label = view.color_sentence(Fore.GREEN, "Is the customer a subscriber? ")
    subscribed = view.get_yes_or_no(subscribe_label)
    subscribed = accept_data(subscribed, subscribe_label)
    subscribed = "1" if subscribed else '0'

    return [name, email, subscribed]


def add_customer():
    view.clear_console()
    view.print_message("Add customer:\n")

    customer = get_customer_data()
    if customer is None:
        return

    crm.update(customer)
    view.print_message("\nCustomer was added correctly!")


def get_updated_customer_data(customer, headers):
    index = 1

    while index < len(customer):
        ask_label = view.color_sentence(Fore.GREEN, f"Would you like to edit {headers[index]}? ")
        new_data_label = view.color_sentence(Fore.GREEN, f"Provide new {headers[index]}: ")
        decision = view.get_yes_or_no(ask_label)
        if decision:
            customer[index] = view.get_input(new_data_label)
            customer[index] = accept_data(customer[index], new_data_label)
        index += 1
    return customer


def update_customer():
    view.clear_console()
    view.print_message("Update customer: ")

    customers = crm.read()
    view.print_table(customers, crm.HEADERS, title='All customers:')

    update_label = view.color_sentence(Fore.GREEN, "Provide customer id to update: ")
    customer_index = view.get_input_number(update_label, max_value=len(customers)) - 1

    customer_to_update = customers.pop(int(customer_index))
    updated_customer = get_updated_customer_data(customer_to_update, crm.HEADERS)
    customers.insert(int(customer_index), updated_customer)

    crm.create(customers)

    view.print_message("Customer was updated correctly.")


def delete_customer():
    view.clear_console()
    view.print_message("Delete customer: ")

    customers = crm.read()
    view.print_table(customers, crm.HEADERS, title='All customers:')

    delete_label = view.color_sentence(Fore.GREEN, "Provide customer id to remove: ")
    customer_index = view.get_input_number(delete_label, max_value=len(customers))

    customers.pop(int(customer_index) - 1)
    crm.create(customers)

    view.print_message("Customer was removed correctly.")


def get_subscribed_emails():
    view.clear_console()
    view.print_message("Subscribed emails: ")

    customers = crm.read()
    subscribers = list(filter(lambda x: x[-1] == '1', customers))

    view.print_table(subscribers, crm.HEADERS)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError()


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options, add_logo=True)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input(view.color_sentence(Fore.GREEN, "\nSelect an operation: "))
            run_operation(int(operation))
            view.wait_for_reaction()
        except KeyError:
            view.print_error_message("There is no such option.")
            view.wait_for_reaction()
        except ValueError:
            view.print_error_message("Please enter a number!")
            view.wait_for_reaction()
