import platform

from . import linux, macos, windows

def detect_platform() -> None:
    os_name = platform.system().lower()

    match os_name:
        case "linux":
            linux.find_window()
        case "darwin":
            macos.find_window()
        case "windows":
            windows.find_window()
        case _:
            raise RuntimeError("OS can not be detected")
