import os, sys

if os.name == 'nt':
    import msvcrt
    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


class KeyboardDisable:
    on = False

    @staticmethod
    def unblock():
        KeyboardDisable.on = True

    @staticmethod
    def block():
        KeyboardDisable.on = False

    @staticmethod
    def __call__():
        while KeyboardDisable.on:
            msvcrt.getwch()

    @staticmethod
    def __init__():
        import os, sys

    @staticmethod
    def hide():
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    @staticmethod
    def show():
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

    @staticmethod
    def hide_and_block():
        KeyboardDisable.hide()
        KeyboardDisable.block()

    @staticmethod
    def show_and_unblock():
        KeyboardDisable.show()
        KeyboardDisable.unblock()
