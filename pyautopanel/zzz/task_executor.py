"""
@author rain
@date 8/10/2024 9:09 AM
"""
import time

import pyautogui
from loguru import logger

from pyautopanel.zzz.cnocr_ocr import CnOcrCtl

ctl = CnOcrCtl()


def _find_text_step(step):
    return ctl.find_target(step['value'])


def _do_text_step(step, x, y):
    pyautogui.click(x, y)


def _do_sleep_step(sleep):
    pass


def _continue_do_func(x, y):
    pyautogui.click(x, y)


func_map = {
    'text': [_find_text_step, _do_text_step],
    'image': [_do_text_step, _do_text_step],
    'sleep': [_do_text_step, _do_text_step],
}


def do_step(step):
    logger.debug('do step: {}'.format(step))
    if not step or not step['type'] or not step['value']:
        logger.warning('step and step.type and step.value can not be empty')
        return

    step_find_func = func_map[step['type']][0]
    step_do_func = func_map[step['type']][1]
    if not step_find_func or not step_do_func:
        logger.warning('none matching func for type: {}'.format(step['type']))

    # find continue text
    c_find, c_x, c_y = ctl.find_continue()

    # find step target
    s_find, s_x, s_y = step_find_func(step)

    # do step target first
    if s_find:
        step_do_func(step, s_x, s_y)
    elif c_find:
        _continue_do_func(c_x, c_y)

    # find continue text and do continue, erase the effect fo step action
    if s_find:
        while True:
            c_find, c_x, c_y = ctl.find_continue()
            if c_find:
                _continue_do_func(c_x, c_y)
            else:
                break
            # after effect erased, sleep for next step
        time.sleep(step.get('sleep', 1))

    return s_find
