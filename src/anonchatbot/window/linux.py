import Xlib


def detect_session_type():
    pass


def find_window():
    display = Xlib.display.Display()
    screen = display.screen()
    root = displa