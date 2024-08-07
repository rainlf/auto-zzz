import os
import time

import pyautopanel.tool.ctl as ctl

IMAGE_DIR = os.path.dirname(__file__)
OLDCITYTRAM_IMG = os.path.join(IMAGE_DIR, 'image', 'oldcitytram.png')
OLDCITYTRAM_FRONTLINE_IMG = os.path.join(IMAGE_DIR, 'image', '1250.png')
NEXTSTEP_IMG = os.path.join(IMAGE_DIR, 'image', 'nextstep.png')
FIGHT_IMG = os.path.join(IMAGE_DIR, 'image', 'fight.png')
FAKEFACERERESEARCHER_IMG = os.path.join(IMAGE_DIR, 'image', 'fakefacereresearcher.png')
REFUSEHISKIND_IMG = os.path.join(IMAGE_DIR, 'image', 'refusehiskind.png')
ME_IMG = os.path.join(IMAGE_DIR, 'image', 'me.png')
BOX_IMG = os.path.join(IMAGE_DIR, 'image', 'box.png')
SELECT_IMG = os.path.join(IMAGE_DIR, 'image', 'select.png')
SURECONTINUE_IMG = os.path.join(IMAGE_DIR, 'image', 'surecontinue.png')
SURE_IMG = os.path.join(IMAGE_DIR, 'image', 'sure.png')
SURESMALL_IMG = os.path.join(IMAGE_DIR, 'image', 'sure2.png')
SURE3_IMG = os.path.join(IMAGE_DIR, 'image', 'sure3.png')
PEOPLE_IMG = os.path.join(IMAGE_DIR, 'image', 'person.png')
PEOPLE2_IMG = os.path.join(IMAGE_DIR, 'image', 'person2.png')
HEALTH_IMG = os.path.join(IMAGE_DIR, 'image', 'health.png')
SDOOR_IMG = os.path.join(IMAGE_DIR, 'image', 'sdoor.png')
SDOOR2_IMG = os.path.join(IMAGE_DIR, 'image', 'sdoor2.png')
SDOOR3_IMG = os.path.join(IMAGE_DIR, 'image', 'sdoor3.png')
SDOOR4_IMG = os.path.join(IMAGE_DIR, 'image', 'sdoor4.png')
TARGET_IMG = os.path.join(IMAGE_DIR, 'image', 'target.png')
TARGET2_IMG = os.path.join(IMAGE_DIR, 'image', 'target2.png')
TARGET3_IMG = os.path.join(IMAGE_DIR, 'image', 'target3.png')
GIVEUP_IMG = os.path.join(IMAGE_DIR, 'image', 'giveup.png')
COMPLETED_IMG = os.path.join(IMAGE_DIR, 'image', 'completed.png')
CASE1_IMG = os.path.join(IMAGE_DIR, 'image', 'case1.png')
EXIT_IMG = os.path.join(IMAGE_DIR, 'image', 'exit1.png')
EXIT2_IMG = os.path.join(IMAGE_DIR, 'image', 'exit2.png')
PHONE_IMG = os.path.join(IMAGE_DIR, 'image', 'phone2.png')
CALLHELP_IMG = os.path.join(IMAGE_DIR, 'image', 'callhelp.png')
GETCOIN_IMG = os.path.join(IMAGE_DIR, 'image', 'getcoin.png')
HOSPITAL_IMG = os.path.join(IMAGE_DIR, 'image', 'hospital.png')
GET2B_IMG = os.path.join(IMAGE_DIR, 'image', 'get2b.png')
COLDDOWN_IMG = os.path.join(IMAGE_DIR, 'image', 'colddown.png')
SHOP_IMG = os.path.join(IMAGE_DIR, 'image', 'shop.png')
OPENDOOR_IMG = os.path.join(IMAGE_DIR, 'image', 'opendoor.png')
BLUESHOP_IMG = os.path.join(IMAGE_DIR, 'image', 'blueshop.png')
BLUESHOP2_IMG = os.path.join(IMAGE_DIR, 'image', 'blueshop2.png')
STORE_IMG = os.path.join(IMAGE_DIR, 'image', 'store.png')
STOREMONEY_IMG = os.path.join(IMAGE_DIR, 'image', 'storemoney.png')
LEAVE_IMG = os.path.join(IMAGE_DIR, 'image', 'leave.png')
BANK_IMG = os.path.join(IMAGE_DIR, 'image', 'bank.png')


# 开始游戏，进入第一层
def enter_floor_one():
    ctl.find_click(OLDCITYTRAM_IMG)
    ctl.find_click(OLDCITYTRAM_FRONTLINE_IMG)
    ctl.find_click(NEXTSTEP_IMG)
    ctl.find_click(FIGHT_IMG)
    ctl.find_click(SURESMALL_IMG)


# 第一层初始对话
def do_floor_one():
    ctl.find_click_safe(SELECT_IMG)
    ctl.find_click(FAKEFACERERESEARCHER_IMG)
    ctl.click(5)
    ctl.find_click(REFUSEHISKIND_IMG)
    ctl.find_click(FAKEFACERERESEARCHER_IMG)
    ctl.click(5)


# 判断第一层分支
def switch_situation():
    x, y = ctl.find_position(ME_IMG)
    x2, y2 = ctl.find_position(EXIT_IMG, EXIT2_IMG)
    if x2 > x and y2 < y:
        return 'right_up'
    if x2 > x and y2 > y:
        return 'right_down'


# 第一层分支(右上)
def do_floor_one_one():
    ctl.press_key('r', 1)
    time.sleep(1)
    ctl.press_key('d')
    time.sleep(2)
    ctl.find_click(SELECT_IMG)
    time.sleep(1)
    ctl.press_key('d')
    ctl.press_key('w')
    ctl.press_key('w')
    ctl.find_click(SURECONTINUE_IMG)


# 第一层分支(右下)
def do_floor_one_two():
    ctl.find_click(PHONE_IMG)
    ctl.find_click(CALLHELP_IMG)
    ctl.click(10)
    ctl.find_click(GETCOIN_IMG)
    time.sleep(1)
    ctl.press_key('r', 1)
    time.sleep(2)
    ctl.press_key('s')
    time.sleep(2)
    ctl.find_click(SELECT_IMG)
    ctl.press_key('d')
    ctl.press_key('d')
    ctl.find_click(SURECONTINUE_IMG)


# 等待战斗结束
def wait_fight_done():
    print("start fight...")
    while not ctl.is_find_once(SURE_IMG):
        ctl.press_key('y', 0.5)
        ctl.press_key('e')
        ctl.press_key('y', 0.5)
        ctl.press_key('e')
        ctl.press_key('y', 0.5)
        ctl.press_key('e')
    print("fight done...")
    ctl.find_click(SURE_IMG, confidence=0.9)
    time.sleep(1)
    ctl.find_click(SELECT_IMG)


# 第二层
def do_floor_two():
    ctl.find_click(PEOPLE_IMG, PEOPLE2_IMG, confidence=0.7)
    ctl.find_click(FAKEFACERERESEARCHER_IMG)
    ctl.click(5)
    time.sleep(1)
    ctl.find_click(HOSPITAL_IMG, COLDDOWN_IMG, SHOP_IMG, GET2B_IMG)
    ctl.find_click_safe(SURE3_IMG, SURESMALL_IMG)
    ctl.click(3)
    ctl.find_click_safe(SURESMALL_IMG)
    ctl.find_click_safe(FAKEFACERERESEARCHER_IMG)
    ctl.click(5)
    time.sleep(2)
    ctl.find_click(SDOOR_IMG, SDOOR2_IMG, SDOOR3_IMG, SDOOR4_IMG)
    time.sleep(2)
    ctl.click(5)
    time.sleep(1)
    ctl.find_click(TARGET_IMG, TARGET2_IMG, TARGET3_IMG)
    ctl.find_click(SURESMALL_IMG)


# 存钱
def do_store_money():
    ctl.press_key('s')
    ctl.press_key('a')
    ctl.press_key('a')
    ctl.press_key('s')
    ctl.press_key('a')
    ctl.press_key('s')
    ctl.press_key('a')
    ctl.press_key('a')
    ctl.press_key('w')
    ctl.press_key('a')
    ctl.press_key('w')
    ctl.press_key('a')
    ctl.find_click(OPENDOOR_IMG)
    ctl.click(5)
    time.sleep(2)
    ctl.find_click(SURESMALL_IMG)
    time.sleep(4)
    ctl.find_click(BLUESHOP_IMG, BLUESHOP2_IMG)
    ctl.find_click(BANK_IMG)
    ctl.click(5)
    ctl.find_click(STORE_IMG)
    ctl.find_click(STOREMONEY_IMG, SELECT_IMG)
    ctl.find_click(STOREMONEY_IMG, SELECT_IMG)
    ctl.find_click(STOREMONEY_IMG, SELECT_IMG)
    ctl.find_click_safe(STOREMONEY_IMG, SELECT_IMG)
    ctl.find_click_safe(STOREMONEY_IMG, SELECT_IMG)
    ctl.click(3)
    ctl.find_click(LEAVE_IMG)
    ctl.click(3)


# 退出
def exit_search():
    time.sleep(1)
    ctl.press_key('esc')
    time.sleep(1)
    ctl.find_click(GIVEUP_IMG)
    ctl.find_click(SURESMALL_IMG)
    time.sleep(5)
    ctl.find_click(COMPLETED_IMG)
    print('exit search...')


def do_hollow_search_once():
    enter_floor_one()
    time.sleep(15)

    do_floor_one()
    time.sleep(5)

    situation = switch_situation()
    print(situation)
    if situation == 'right_up':
        do_floor_one_one()
    elif situation == 'right_down':
        do_floor_one_two()
    time.sleep(10)

    wait_fight_done()
    time.sleep(7)

    do_floor_two()
    time.sleep(3)

    do_store_money()
    time.sleep(3)

    exit_search()


# 空洞搜索
def do_hollow_search():
    i: int = 0
    while True:
        do_hollow_search_once()
        i = i + 1
        print("search {} times".format(i))
        time.sleep(5)


def test():
    pass


if __name__ == '__main__':
    do_hollow_search()
