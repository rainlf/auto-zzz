import pyautogui
from PIL import Image
from cnocr import CnOcr

'''
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
检测模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnstd
识别模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnocr
'''

screen_region = (0, 0, 1940, 1100)


def test_img(path='test.png'):
    # img = Image.open(path).convert('RGB')
    img = Image.open(path)
    ocr = CnOcr()
    out = ocr.ocr(img)
    print(out)
    pass


def test_screenshot():
    screenshot = pyautogui.screenshot(region=screen_region)
    ocr = CnOcr(
        # det_model_name='ch_PP-OCRv3_det',
        # rec_model_name='densenet_lite_136-gru',
        # det_model_name='ch_PP-OCRv3_det',
        # rec_model_name='densenet_lite_136-gru',
    )
    out = ocr.ocr(screenshot)
    print(out)


def test_screenshot_with_save():
    screenshot = pyautogui.screenshot(region=screen_region)
    screenshot.save('test3.png')
    test_img('test3.png')


if __name__ == '__main__':
    # test_img()
    test_screenshot()
    # test_screenshot_with_save()
