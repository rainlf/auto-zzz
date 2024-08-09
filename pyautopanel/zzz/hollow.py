import pyautogui
import pytesseract
import cv2

screen_region = (0, 0, 1920, 1080)  # 示例：整个屏幕


def main():
    screenshot = pyautogui.screenshot(region=screen_region)
    # # 将Pyautogui截图转换为OpenCV图像格式
    # image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    #
    # # 转换为灰度图像
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    # # 进行二值化处理
    # ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    extracted_text = pytesseract.image_to_string(screenshot)
    print(extracted_text)

if __name__ == '__main__':
    main()

