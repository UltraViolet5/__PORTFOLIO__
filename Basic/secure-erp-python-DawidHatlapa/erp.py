import os
from controller import main_controller


if __name__ == '__main__':
    os.system("mode con cols=150 lines=35")
    main_controller.menu()
