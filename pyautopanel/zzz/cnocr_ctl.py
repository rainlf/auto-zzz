import time

import pyautogui
import yaml
from cnocr import CnOcr
from loguru import logger

from pyautopanel.zzz.constants import *

'''
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
'''

# 应用窗口可能存在的位置偏移
# screen_region = (0, 0, 1920, 1080)
screen_region = (0, 0, 1940, 1100)


class CnOcrCtl:
    def __init__(self):
        self.ocr = CnOcr()
        self._load_config()

    def _load_config(self):
        with open(TASK_CONFIG, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            self.continue_word_eq = data['continueWordsQe']
            self.continue_word_in = data['continueWordsIn']

    def find_continue(self):
        screenshot = pyautogui.screenshot(region=screen_region)
        results: List[Dict[str, Any]] = self.ocr.ocr(screenshot)
        for result in results:
            for text in self.continue_word_eq:
                if text == result['text']:
                    x, y = self._center(result['position'])
                    logger.debug('find continue text: {}, position: {}, {}'.format(text, x, y))
                    return True, x, y

            for text in self.continue_word_in:
                if text in result['text']:
                    x, y = self._center(result['position'])
                    logger.debug('find continue text: {}, position: {}, {}'.format(text, x, y))
                    return True, x, y
        logger.debug('none find continue text')
        return False, None, None

    def find_target(self, target, click=True):
        screenshot = pyautogui.screenshot(region=screen_region)
        results: List[Dict[str, Any]] = self.ocr.ocr(screenshot)
        for result in results:
            if target in result['text']:
                x, y = self._center(result['position'])
                logger.debug('find target text: {}, position: {}, {}'.format(target, x, y))
                return True, x, y
        logger.debug('none find target text: {}'.format(target))
        return False, None, None

    @staticmethod
    def _center(position: list[any]) -> (int, int):
        x = (position[0][0] + position[2][0]) / 2
        y = (position[0][1] + position[2][1]) / 2
        return x, y


def main():
    ctl = CnOcrCtl()
    while True:
        x, y = ctl.find_continue()
        pyautogui.moveTo(x, y)
        time.sleep(1)
    pass


if __name__ == '__main__':
    main()
