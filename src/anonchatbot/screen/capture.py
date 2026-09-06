import mss

from PIL import Image

def capture_monitor(area:tuple[int, int, int, int], 
    monitor_id: int = 1    
) -> Image.Image:
    with mss.MSS() as sct:
        monitor = sct.monitors[monitor_id]
        region = {"left":area[0],
                 "top":area[1],
                 "width":area[2],
                 "height":area[3]
        }

        print(region)
        print(monitor)

    return Image.Image()

capture_monitor((200,200,600, 67))