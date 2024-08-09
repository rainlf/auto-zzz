import os

import pyautogui

from pyautopanel.trip.xshell_login.auth import get_auth_code
from pyautopanel.trip.tool import ctl

DIR = os.path.dirname(__file__)
SERVER_IMG = os.path.join(DIR, 'img', 'server.png')
SERVER_IMG2 = os.path.join(DIR, 'img', 'server2.png')
OK_IMG = os.path.join(DIR, 'img', 'ok.png')


def main():
    ctl.find_click(SERVER_IMG, SERVER_IMG2)
    code = get_auth_code()
    print(code)
    pyautogui.write(code)
    ctl.find_click(OK_IMG)
    pass


if __name__ == '__main__':
    main()
    pass
