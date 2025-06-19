# vision/capture.py

from PIL import ImageGrab
import datetime
import os

def capture_window(region=None, save=False):
    """
    Captures a screenshot of a specified region or full screen.
    region: (left, top, right, bottom)
    """
    screenshot = ImageGrab.grab(bbox=region)  # bbox is optional

    if save:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshot_{ts}.png"
        screenshot.save(path)
        print(f"Screenshot saved as {path}")

    return screenshot
