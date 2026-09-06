import mss # type: ignore

from PIL import Image

from anonchatbot.local.types import AreaTuple

def capture_monitor(
    area: AreaTuple,
    monitor_id: int = 1,
) -> Image.Image:
    with mss.MSS() as sct:
        monitor = sct.monitors[monitor_id]

        if area.width <= 0 or area.height <= 0:
            raise ValueError("Width/Height must be greater than 0")

        if area.left < 0 or area.top < 0:
            raise ValueError("Left/Top margins must be non-negative")

        if (
            area.left + area.width > monitor["width"]
            or area.top + area.height > monitor["height"]
        ):
            raise ValueError("Selected area exceeds monitor bounds")

        absolute_area = {
            "left": monitor["left"] + area.left,
            "top": monitor["top"] + area.top,
            "width": area.width,
            "height": area.height,
        }

        screenshot = sct.grab(absolute_area)

    # Convert mss.screenshot.ScreenShot to PIL.Image for further processing
    screenshot_image = Image.frombytes(
        mode="RGB",
        size=screenshot.size,
        data=screenshot.rgb,
    )

    return screenshot_image


area = AreaTuple(
    left=200,
    top=200,
    width=600,
    height=67,
)

capture_monitor(area, 2)