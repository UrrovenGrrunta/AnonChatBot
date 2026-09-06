import mss

from PIL import Image

def capture_monitor(area:tuple[int, int, int, int], 
    monitor_id: int = 1    
) -> None:
    # Take screenshot in selected region
    with mss.MSS() as sct:
        monitor = sct.monitors[monitor_id]
        region = {
            "left":area[0],
            "top":area[1],
            "width":area[2],
            "height":area[3]
        }
        absolute_area = {
            "left": monitor["left"] + region["left"],
            "top": monitor["top"] + region["top"],
            "width": region["width"],
            "height": region["height"]
        }

        screenshot = sct.grab(absolute_area)

    # Covnert mss.screenshot.ScreenShot to PIL.Image for further processing
    screenshot_PIL = screenshot.to_pil()
    Image.Image.show(screenshot_PIL)

    return

capture_monitor((200,200,600, 67), 2)