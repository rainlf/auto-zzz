import logging
import os
import time

import pyautogui
import pyautopanel.trip.captain_publish.approve as approve
import pyautopanel.trip.tool.ctl as ctl


IMAGE_DIR = os.path.dirname(__file__)

IMG_ENVB = os.path.join(IMAGE_DIR, 'img', 'envb.png')
IMG_NEW = os.path.join(IMAGE_DIR, 'img', 'new.png')
IMG_NEXT = os.path.join(IMAGE_DIR, 'img', 'next.png')


def main():
    try:
        approve.main()
        pyautogui.write('dev_b')
        time.sleep(2)
        ctl.find_click(IMG_ENVB)
        ctl.find_click(IMG_NEXT)
        ctl.find_click(IMG_NEW)
    except Exception as e:
        logging.warning(e)


if __name__ == '__main__':
    main()
    pass
