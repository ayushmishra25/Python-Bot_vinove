import mss
import time
from datetime import datetime

class ScreenshotCapture:
    def _init_(self, capture_interval=60):
        self.capture_interval = capture_interval
        self.sct = mss.mss()

    def capture_screenshot(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        self.sct.shot(output=filename)
        return filename

    def start_capture(self):
        while True:
            filename = self.capture_screenshot()
            print(f"Screenshot saved: {filename}")
            time.sleep(self.capture_interval)