import ctypes
import os

import pygetwindow
import ttkbootstrap as ttk
from loguru import logger

from pyautopanel.zzz.notify import Notify


class Window:
    check_success = False

    @classmethod
    def admin_check(cls):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            Notify.info('管理员权限检测', '管理员权限确认，开始执行任务')
            Window.check_success = True
        else:
            Notify.warn('管理员权限检测', '失败，请以管理员权限运行此程序')
            Window.check_success = False

    @classmethod
    def game_check(cls):
        zzz = pygetwindow.getWindowsWithTitle("绝区零")[0]
        if zzz == 0:
            zzz = pygetwindow.getWindowsWithTitle("ZenlessZoneZero")[0]
        if not zzz:
            Notify.warn('游戏窗口检测', '失败，未找到游戏窗口，请先打开游戏')
            Window.check_success = False
        # move window to left top corner
        zzz.activate()
        zzz.resizeTo(1920, 1080)
        zzz.moveTo(0, 0)
        Window.check_success = True


def main():
    app = ttk.Window()

    Window.admin_check()
    Window.game_check()

    logger.info('check success: {}'.format(Window.check_success))
    app.mainloop()


if __name__ == '__main__':
    main()
