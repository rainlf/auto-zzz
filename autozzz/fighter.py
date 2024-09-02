"""
@author rain
@date 8/10/2024 2:20 PM
"""
import time

import pydirectinput


def _press(key, duration=0.3) -> None:
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)


def number11():
    _press('y', 0.3)
    _press('y', 0.3)
    _press('y', 0.3)
    _press('e')


def tea_girl():
    for i in range(30):
        _press('y', 0.1)

def boom_sister():
    _press('y', 0.1)
    _press('y', 0.1)
    _press('y', 0.1)
    _press('e')
