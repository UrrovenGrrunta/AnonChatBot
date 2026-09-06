import Xlib.display

from Xlib import X
def detect_session_type():
    pass


def find_window():
    display = Xlib.display.Display()
    screen = display.screen()
    root = screen.root
    atom = display.intern_atom("_NET_CLIENT_LIST")
    full_geometry = root.get_full_property(
        atom, 
        X.AnyPropertyType
    )
    print(full_geometry)
"""    for window in windows:
        title = window.get_wm_name()
        if title is None:
            continue
        if type(title) == bytes:
            title = title.decode()
        title_lower = title.lower()
        if "telegram" in title_lower or "ayugramdesktop" in title_lower:
            print(window.get_geometry())"""
find_window()