from colorama import Fore
from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller

MENU_OFFSET = 1


def load_module(option):
    if option == 1:
        crm_controller.menu()
    elif option == 2:
        sales_controller.menu()
    elif option == 3:
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Exit program",
               "Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources"]
    view.print_menu("Main menu", options, add_logo=True, offset=MENU_OFFSET)


def menu():
    option = None
    while option != '0':
        display_menu()
        try:
            option = view.get_input(view.color_sentence(Fore.GREEN, view.add_sentence_offset("\nSelect module: ",
                                                                                                    MENU_OFFSET)))
            load_module(int(option))
        except KeyError:
            view.print_error_message(view.add_sentence_offset("There is no such option!", MENU_OFFSET))
            view.wait_for_reaction()
        except ValueError:
            view.print_error_message(view.add_sentence_offset("Please enter a number!", MENU_OFFSET))
            view.wait_for_reaction()
    view.print_message(view.add_sentence_offset("Good-bye!", MENU_OFFSET))
    view.wait_for_reaction()
