import Xlib.display
import os

from Xlib import X


def detect_session_type():
    sesstion_type = os.getenv("XDG_SESSION_TYPE")
    backend = None
    match sesstion_type:
        case "x11":
            backend = X11Backend()
            backend.find_window()
        case "wayland":
            backend = WaylandBackend()
            backend.find_window()
        case _:
            raise RuntimeError("Can not identify session type.")


class X11Backend:
    def find_window(self):
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


class WaylandBackend:
    def find_window(self):
        print("Hello from Wayland!")

detect_session_type()