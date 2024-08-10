"""
@author rain
@date 8/10/2024 9:09 AM
"""

import pyautogui
from loguru import logger

from pyautopanel.zzz.cnocr_ctl import CnOcrCtl
from pyautopanel.zzz.constants import *
from pyautopanel.zzz.fighter import *
from pyautopanel.zzz.pyautogui_ctl import GuiCtl

ocr_ctl = CnOcrCtl()
gui_ctl = GuiCtl()

fighter = 'No.11'


# continue
def _continue_do_func(x, y):
    pyautogui.click(x, y)


# text
def _find_text_step(step):
    return ocr_ctl.find_target(step['value'])


def _do_text_step(step, x, y):
    pyautogui.click(x, y)


# image

# keyboard
def _do_press_step(step, x, y):
    pydirectinput.keyDown(step['value'])
    time.sleep(0.1)
    pydirectinput.keyUp(step['value'])


def _do_long_press_step(step, x, y):
    pydirectinput.keyDown(step['value'])
    time.sleep(1)
    pydirectinput.keyUp(step['value'])


# mission
def _do_mission_select_situation(step, x, y):
    find, x, y = gui_ctl.find_position(IMG_ME)
    find2, x2, y2 = gui_ctl.find_position(IMG_EXIT)
    if find and find2:
        if x2 > x and y2 < y:
            return 'floor1.1'
        if x2 > x and y2 > y:
            return 'floor1.2'
    else:
        logger.warning('none find me or exit, continue find')
        _do_mission_select_situation(step, x, y)


def _do_mission_fight(step, x, y):
    while True:
        find, x1, y1 = ocr_ctl.find_target("总计用时")
        if find:
            break
        if fighter == 'No.11':
            number11()
        elif fighter == 'IceWolf':
            ice_wolf()
        elif fighter == 'BoomSister':
            boom_sister()
        else:
            logger.warning('none matching fighter: {}'.format(fighter))
            break


def _do_mission_select_help(step, x, y):
    find, x, y = gui_ctl.find_position(IMG_HELP)
    if find:
        pyautogui.click(x, y)


func_map = {
    'text': [_find_text_step, _do_text_step],
    'press': [lambda x: (True, None, None), _do_press_step],
    'longPress': [lambda x: (True, None, None), _do_long_press_step],
    'mission_select_situation': [lambda x: (True, None, None), _do_mission_select_situation],
    'mission_fight': [lambda x: (True, None, None), _do_mission_fight],
    'mission_select_help': [lambda x: (True, None, None), _do_mission_select_help],
}


def do_step(step):
    logger.debug('do step: {}'.format(step))
    if not step or not step['type']:
        logger.warning('step and step.type can not be empty')
        time.sleep(1)
        return False, None

    step_find_func = func_map[step['type']][0]
    step_do_func = func_map[step['type']][1]
    if not step_find_func or not step_do_func:
        logger.warning('none matching func for type: {}'.format(step['type']))
        time.sleep(1)
        return False, None

    # find continue text
    c_find, c_x, c_y = ocr_ctl.find_continue()

    # find step target
    s_find, s_x, s_y = step_find_func(step)

    # do step target first
    next_stage = None
    if s_find and s_x and s_y:
        next_stage = step_do_func(step, s_x, s_y)
    elif c_find:
        _continue_do_func(c_x, c_y)
        s_find = False
    else:
        next_stage = step_do_func(step, s_x, s_y)

    # sleep after step action
    if s_find:
        time.sleep(step.get('sleep', 1))

    return s_find, next_stage
