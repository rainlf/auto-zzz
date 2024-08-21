"""
@author rain
@date 8/20/2024 11:05 PM
"""
import threading
import time

import keyboard
import numpy as np
import pyautogui

running = False

color_position = (1695, 610)
click_position = (1430, 600)
default_color = (107, 134, 114)
rating1 = (88, 255, 163)
rating2 = (255, 85, 50)
rating3 = (29,255,255)

rating_colors = [rating1, rating2, rating3]


def listen_start():
    global running
    keyboard.wait('+')
    running = True


def listen_stop():
    global running
    keyboard.wait('-')
    running = False


def is_change_color(color):
    diff_default = np.array(color) - np.array(default_color)
    if np.linalg.norm(diff_default) < 10:
        return False

    for rating_color in rating_colors:
        diff_target = np.array(color) - np.array(rating_color)
        if np.linalg.norm(diff_target) < 10:
            return True

    return False


def game():
    while running:
        color = pyautogui.pixel(color_position[0], color_position[1])
        if is_change_color(color):
            print(color)
            pyautogui.click()
        time.sleep(0.01)


def main():
    start_thread = threading.Thread(target=listen_start)
    stop_thread = threading.Thread(target=listen_stop)

    start_thread.start()
    stop_thread.start()

    start_thread.join()
    print('start')
    game()

    stop_thread.join()
    print('done')


if __name__ == '__main__':
    main()
