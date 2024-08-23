"""
@author rain
@date 8/23/2024 6:29 AM
"""
import os
import threading

import cv2
import keyboard
import numpy as np
import pyautogui

running = True

FILE_DIR = os.path.dirname(__file__)
virus = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus.png'), cv2.IMREAD_GRAYSCALE)
virus2 = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus2.png'), cv2.IMREAD_GRAYSCALE)
virus3 = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus3.png'), cv2.IMREAD_GRAYSCALE)
virus4 = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus4.png'), cv2.IMREAD_GRAYSCALE)
virus_star = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus_star.png'), cv2.IMREAD_GRAYSCALE)
virus_star2 = cv2.imread(os.path.join(FILE_DIR, 'image', 'virus_star2.png'), cv2.IMREAD_GRAYSCALE)


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


def mark_frames(frame, targets):
    for target in targets:
        mark_frame(frame, target)


def mark_frame(frame, target):
    # 计算模板的宽度和高度
    target_width, target_height = target.shape[::-1]
    # 转换为灰度图以进行模板匹配
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用模板匹配
    res = cv2.matchTemplate(gray_frame, target, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    # 在找到的匹配位置画框
    pre_x = 0
    for pt in zip(*loc[::-1]):
        # 画红色矩形框标记
        # cv2.rectangle(frame, pt, (pt[0] + target_width, pt[1] + target_height), (0, 0, 255), 1)
        # 点击目标
        x, y = pt[0] + target_width // 2, pt[1] + target_height // 2
        if abs(x - pre_x) > 10:
            print(f'click: {x}, {y}')
            pyautogui.click(x, y)
            pre_x = x


def game(top_left_x, top_left_y, width, height):
    # # 创建一个窗口并设置为可调整大小
    # cv2.namedWindow('Screen Capture', cv2.WINDOW_NORMAL)
    # # 设置窗口的初始大小
    # cv2.resizeWindow('Screen Capture', 1070, 600)

    while running:
        # 使用 pyautogui 截取屏幕的指定区域
        screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))
        # 将 PIL 图像转换为 OpenCV 格式
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # 标记模板
        mark_frames(frame, [virus3])

        # 在窗口中显示图像
        # cv2.imshow('Screen Capture', frame)
        # 检查用户是否按下了 'q' 键以退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 清理资源
    cv2.destroyAllWindows()


def main():
    stop_thread = threading.Thread(target=listen_stop)
    stop_thread.start()

    print('start')
    game(0, 0, 1920, 1080)

    stop_thread.join()
    print('done')


if __name__ == '__main__':
    main()
