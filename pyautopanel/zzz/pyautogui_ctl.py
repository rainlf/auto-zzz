"""
@author rain
@date 8/10/2024 1:32 PM
"""

import os
import time

import pyautogui


class GuiCtl:
    def __init__(self):
        pass

    def find_position(self, images, confidence=0.8) -> (int, int):
        i = 0
        while i < 2:
            for image in images:
                find, x, y = self._find_position(image, confidence=confidence)
                if find:
                    return True, x, y
            i += 1
            time.sleep(0.5)
        return False, None, None

    @staticmethod
    def _find_position(image, confidence) -> (int, int):
        print("find image start: {}".format(os.path.basename(image)))
        try:
            x, y, width, height = pyautogui.locateOnScreen(image, confidence=confidence)
            x, y = pyautogui.center((x, y, width, height))
            print("find {}, position: {}.{}".format(os.path.basename(image), x, y))
            return True, x, y
        except Exception as e:
            return False, None, None
