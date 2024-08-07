import os
import time

import pyautogui

import pyautorain.tool.ctl as ctl

IMAGE_DIR = os.path.dirname(__file__)
IMG_IMAGEVERSION = os.path.join(IMAGE_DIR, 'img', 'imageversion.png')
IMG_IDEVINPUT = os.path.join(IMAGE_DIR, 'img', 'idevinput.png')
IMG_IDEVINPUT2 = os.path.join(IMAGE_DIR, 'img', 'idevinput2.png')
IMG_IDEV = os.path.join(IMAGE_DIR, 'img', 'idev.png')
IMG_IDEV2 = os.path.join(IMAGE_DIR, 'img', 'idev2.png')
IMG_UAT = os.path.join(IMAGE_DIR, 'img', 'uat.png')
IMG_UAT2 = os.path.join(IMAGE_DIR, 'img', 'uat2.png')
IMG_REASON = os.path.join(IMAGE_DIR, 'img', 'reason.png')
IMG_REASON2 = os.path.join(IMAGE_DIR, 'img', 'reason2.png')
IMG_OTHER = os.path.join(IMAGE_DIR, 'img', 'other.png')
IMG_OTHER2 = os.path.join(IMAGE_DIR, 'img', 'other2.png')
IMG_REASONINPUT = os.path.join(IMAGE_DIR, 'img', 'reasoninput.png')
IMG_REASONINPUT2 = os.path.join(IMAGE_DIR, 'img', 'reasoninput2.png')
IMG_PASS = os.path.join(IMAGE_DIR, 'img', 'pass.png')
IMG_PASS2 = os.path.join(IMAGE_DIR, 'img', 'pass2.png')
IMG_PRO = os.path.join(IMAGE_DIR, 'img', 'pro.png')
IMG_PRO2 = os.path.join(IMAGE_DIR, 'img', 'pro2.png')
IMG_PUBLISHPRO = os.path.join(IMAGE_DIR, 'img', 'publishpro.png')
IMG_PUBLISHPRO2 = os.path.join(IMAGE_DIR, 'img', 'publishpro2.png')
IMG_GROUPLIST = os.path.join(IMAGE_DIR, 'img', 'grouplist.png')


def main():
    # 关联 idev
    ctl.find_click(IMG_IDEVINPUT, IMG_IDEVINPUT2, confidence=0.7)
    pyautogui.write('3760646')
    ctl.find_click(IMG_IDEV, IMG_IDEV2)

    # 变更审批 UAT
    ctl.find_click(IMG_UAT, IMG_UAT2, confidence=0.9)
    ctl.find_click(IMG_REASON, IMG_REASON2)
    ctl.find_click(IMG_OTHER, IMG_OTHER2)
    ctl.find_click(IMG_REASONINPUT, IMG_REASONINPUT2)
    pyautogui.write('Temporary  release  Temporary  release ')
    time.sleep(1)
    ctl.find_click(IMG_PASS, IMG_PASS2, confidence=0.9)

    # 变更审批 PRO
    ctl.find_click(IMG_PRO, IMG_PRO2, confidence=0.9)
    ctl.find_click(IMG_REASON, IMG_REASON2)
    ctl.find_click(IMG_OTHER, IMG_OTHER2)
    ctl.find_click(IMG_REASONINPUT, IMG_REASONINPUT2)
    pyautogui.write('Temporary  release  Temporary  release ')
    time.sleep(1)
    ctl.find_click(IMG_PASS, IMG_PASS2, confidence=0.9)

    # 发布环境
    ctl.find_click(IMG_PUBLISHPRO, IMG_PUBLISHPRO2)
    ctl.find_click(IMG_GROUPLIST)
    pass


if __name__ == '__main__':
    main()
    pass
