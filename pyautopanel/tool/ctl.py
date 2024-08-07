import os
import time

import pyautogui
import pydirectinput


def click(num=1) -> None:
    pyautogui.click(clicks=num, interval=0.5)


def press_key(key, duration=0.3) -> None:
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)


def _find_position(image, confidence) -> (int, int):
    print("find image start: {}".format(os.path.basename(image)))
    try:
        x, y, width, height = pyautogui.locateOnScreen(image, confidence=confidence)
        x, y = pyautogui.center((x, y, width, height))
        print("find {}, position: {}.{}".format(os.path.basename(image), x, y))
        return x, y
    except Exception as e:
        return None, None


def _find_once(*imgs, confidence=0.8) -> (int, int):
    for img in imgs:
        x, y = _find_position(img, confidence=confidence)
        if x and y:
            return x, y
    return None, None


def _find(*imgs, confidence=0.8, second=5) -> (int, int):
    i = 0
    while i < second * 10:
        for img in imgs:
            x, y = _find_once(img, confidence=confidence)
            if x and y:
                return x, y
            else:
                time.sleep(0.1)
        i = i + 1
    raise Exception("can't find image: {}".format(imgs))


def find_position(*imgs, confidence=0.8) -> (int, int):
    return _find(*imgs, confidence=confidence)


def is_find_once(*imgs, confidence=0.8) -> bool:
    x, y = _find_once(*imgs, confidence=confidence)
    return x and y


def is_find(*imgs, confidence=0.8) -> bool:
    x, y = _find(*imgs, confidence=confidence)
    return x and y


def find_click(*image, confidence=0.8) -> None:
    x, y = _find(*image, confidence=confidence)
    pyautogui.click(x, y)
    time.sleep(0.5)


def find_click_safe(*image, confidence=0.8) -> None:
    try:
        x, y = _find(*image, confidence=confidence, second=1)
        pyautogui.click(x, y)
        time.sleep(0.5)
    except Exception as e:
        print("can't find image: {}, skip".format(image))


def find_move_to(*image, confidence=0.8) -> None:
    x, y = _find(*image, confidence=confidence)
    pyautogui.moveTo(x, y, duration=1)
