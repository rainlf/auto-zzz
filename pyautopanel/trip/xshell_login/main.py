import os

import pyautogui

from pyautorain.module.trip.xshell_login.auth import get_auth_code
from pyautorain.tool import ctl

DIR = os.path.dirname(__file__)
SERVER_IMG = os.path.join(DIR, 'img', 'server.png')
OK_IMG = os.path.join(DIR, 'img', 'ok.png')


def main():
    ctl.find_click(SERVER_IMG)
    code = get_auth_code()
    print(code)
    pyautogui.write(code)
    ctl.find_click(OK_IMG)
    pass


if __name__ == '__main__':
    main()
    pass
