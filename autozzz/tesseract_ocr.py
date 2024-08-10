import pyautogui
import pytesseract
from PIL import ImageEnhance, ImageFilter

'''
tesseract
下载地址：https://digi.bib.uni-mannheim.de/tesseract/
官方网站：https://github.com/tesseract-ocr/tesseract
官方文档：https://github.com/tesseract-ocr/tessdoc
语言包地址：https://github.com/tesseract-ocr/tessdata
简体中文：chi_sim.traineddata
繁体中文：chi_sim_vert.traineddata
存放位置：C:\\Program Files\\Tesseract-OCR\\tessdata
'''

# 设置Tesseract的安装路径（如果它不在默认的系统路径中）
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
screen_region = (0, 0, 1920, 1080)


def main():
    # 截取屏幕截图
    screenshot = pyautogui.screenshot(region=screen_region)

    # 将图像对象转换为灰度图像，以帮助提高文本识别的准确性
    screenshot = screenshot.convert('L')
    enhancer = ImageEnhance.Contrast(screenshot)
    screenshot = enhancer.enhance(2)  # 提高对比度
    screenshot = screenshot.filter(ImageFilter.MedianFilter())  # 应用中值滤波去噪
    screenshot = screenshot.point(lambda x: 0 if x < 140 else 255)  # 二值化

    # 使用pytesseract进行文字识别
    text = pytesseract.image_to_string(screenshot, lang='chi_sim')

    # 打印识别的文本
    print(text)


if __name__ == '__main__':
    main()
