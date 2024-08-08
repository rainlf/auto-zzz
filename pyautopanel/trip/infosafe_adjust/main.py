import os
import time
import webbrowser

import pyautogui

IMAGE_DIR = os.path.dirname(__file__)
IMG_HANDLE = os.path.join(IMAGE_DIR, 'image', 'handle.png')
IMG_INPUTWINDOW = os.path.join(IMAGE_DIR, 'image', 'inputwindow.png')
IMG_SELECTBUTTON = os.path.join(IMAGE_DIR, 'image', 'selectbutton.png')
IMG_SELECTLIST = os.path.join(IMAGE_DIR, 'image', 'selectlist.png')
IMG_SELECTLIST2 = os.path.join(IMAGE_DIR, 'image', 'selectlist2.png')
IMG_SUBMITBUTTON = os.path.join(IMAGE_DIR, 'image', 'submitbutton.png')

INFOSAFE_SITE = 'http://jumpserver.audit.infosec.ctripcorp.com/#/mysession'


def find_click(img):
    finds_click([img])


def finds_click(imgs: []):
    i = 0
    while i < 10:
        for img in imgs:
            try:
                x, y, width, height = pyautogui.locateOnScreen(img)
                x, y = pyautogui.center((x, y, width, height))
                pyautogui.click(x, y)
                return
            except Exception as e:
                print('looking for {}'.format(os.path.basename(img)))
                time.sleep(0.1)
                i += 1
    if i >= 10:
        raise Exception('Cannot find img')


def main():
    # open infosafe site
    webbrowser.open(INFOSAFE_SITE)
    time.sleep(2)

    # open adjust window
    find_click(IMG_HANDLE)
    time.sleep(1)

    # adjust
    while True:
        find_click(IMG_SELECTBUTTON)
        time.sleep(1)
        finds_click([IMG_SELECTLIST, IMG_SELECTLIST2])
        time.sleep(0.5)
        find_click(IMG_INPUTWINDOW)
        pyautogui.write('OPS')
        pyautogui.press('space')
        find_click(IMG_SUBMITBUTTON)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
