import time

import pyautogui
from cnocr import CnOcr
from loguru import logger

'''
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
'''

screen_region = (0, 0, 1920, 1080)


class CnOcrCtl:
    def __init__(self):
        self.ocr = CnOcr()
        self.continue_text = [
            '确定',
            '完成',
            '选择',
            '下一步',
            '假面研究者',
            '异化检疫门',
            '零号银行',
        ]
        self.confirm_click_text = [
            '旧都列车·前线',
            '旧都列车',
            '出战',
            '拒绝他的好意',

            '确认继续',
            '完成关卡',

            '恢复身体',
            '做好降压准备',
            '拿点垃圾物资',

            '强行闯入通道',
            '存款',
            '存入齿轮硬币',
            '存款0次',
            '离开',
            '放弃',
            '完成',
        ]

    def click_continue(self, click=True):
        screenshot = pyautogui.screenshot(region=screen_region)
        results: List[Dict[str, Any]] = self.ocr.ocr(screenshot)
        for result in results:
            for text in self.continue_text:
                if text in result['text']:
                    x, y = self._center(result['position'])
                    logger.debug('find continue text: {}, position: {}, {}'.format(text, x, y))
                    if click:
                        pyautogui.click(x, y)
                    return True
        logger.debug('none find continue text')
        return False

    def click_target(self, target, click=True):
        screenshot = pyautogui.screenshot(region=screen_region)
        results: List[Dict[str, Any]] = self.ocr.ocr(screenshot)
        for result in results:
            if target in result['text']:
                x, y = self._center(result['position'])
                logger.debug('find target text: {}, position: {}, {}'.format(target, x, y))
                if click:
                    pyautogui.click(x, y)
                return True
        logger.debug('none find target text: {}'.format(target))
        return False

    @staticmethod
    def _center(position: list[any]) -> (int, int):
        x = (position[0][0] + position[2][0]) / 2
        y = (position[0][1] + position[2][1]) / 2
        return x, y


def main():
    ctl = CnOcrCtl()
    while True:
        ctl.click_continue(click=False)
        time.sleep(1)
    pass


if __name__ == '__main__':
    main()
