import numpy as np
import pyautogui
from PIL import Image
from cnocr import CnOcr

'''
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
'''

screen_region = (0, 0, 1920, 1080)


def main():
    screenshot = pyautogui.screenshot(region=screen_region)
    ocr = CnOcr()
    out = ocr.ocr(screenshot)
    print(out)


def test():
    img = Image.open('../../tests/test.png').convert('RGB')
    ocr = CnOcr()
    out = ocr.ocr(img)
    print(out)
    pass


if __name__ == '__main__':
    main()
