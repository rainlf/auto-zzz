"""
@author rain
@date 8/10/2024 9:09 AM
"""
from loguru import logger

from pyautopanel.zzz.cnocr_ocr import CnOcrCtl

ctl = CnOcrCtl()


def _do_text_step(text):
    return ctl.click_target(text)


def _do_img_step(img):
    pass


def _do_sleep_step(sleep):
    pass


func_map = {
    'text': _do_text_step,
    'image': _do_text_step,
    'sleep': _do_text_step,
}


def do_continue():
    return ctl.click_continue()


def do_step(step):
    logger.debug('do step: {}'.format(step))
    if not step or not step['type'] or not step['value']:
        logger.warning('step and step.type and step.value can not be empty')
        return

    func = func_map[step['type']]
    if not func:
        logger.warning('none matching func for type: {}'.format(step['type']))

    return func(step['value'])
