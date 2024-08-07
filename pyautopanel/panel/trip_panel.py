import threading

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import pyautopanel.module.trip.captain_publish.publish_b as publish_b
import pyautopanel.module.trip.captain_publish.publish_test as publish_test
import pyautopanel.module.trip.infosafe_adjust.main as infosafe_adjust
import pyautopanel.module.trip.qconfig_publish.main as qconfig_publish
import pyautopanel.module.trip.xshell_login.main as xshell_login
from pyautopanel.tool.notify import Notify


class TripPanel:
    def __init__(self):
        self.button_list = []
        self.thread_list = []
        self._create_root()
        self._create_title()
        self._create_separator()
        self._create_captain()
        self._create_infosafe()
        self._create_separator()
        self._create_qconfig()
        self._create_xshell()

    def _on_closing(self):
        print("wait thread done")
        for thread in self.thread_list:
            pass
        print("close app")
        self.app.destroy()

    def _create_root(self):
        self.app = ttk.Window(
            title='RainAutoTools',
            themename='litera',  # 设置主题
            size=(380, 480),  # 窗口的大小 （宽, 高）
            position=(1500, 480),  # 窗口所在的位置
            minsize=(0, 0),  # 窗口的最小宽高
            maxsize=(1920, 1080),  # 窗口的最大宽高
            resizable=None,  # 设置窗口是否可以更改大小
            alpha=1.0,  # 设置窗口的透明度(0.0完全透明）
        )
        self.app.resizable(False, False)
        self.root = ttk.Frame(self.app, padding=(10, 10, 10, 10))
        self.root.pack(side=TOP, fill=BOTH)
        self.app.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_title(self):
        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(side=TOP, fill=BOTH)
        self.title = ttk.Label(self.title_frame, text='Trip', font=('Segoe UI', 18, 'bold'), bootstyle=PRIMARY)
        self.title.pack(side=LEFT, fill=BOTH)
        self.title_button = ttk.Button(self.title_frame, text='Refresh', bootstyle=WARNING,
                                       command=self.enable_all_button)
        self.title_button.pack(side=RIGHT, fill=BOTH)

    def _create_separator(self):
        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.pack(side=TOP, fill=BOTH, pady=10)

    def _create_captain(self):
        self.captain_frame = ttk.Labelframe(self.root, text='Captain', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.captain_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.captain_button1 = ttk.Button(self.captain_frame, text='Publish B', bootstyle=(PRIMARY, OUTLINE), width=14,
                                          command=self._click_publish_b)
        self.captain_button1.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.captain_button2 = ttk.Button(self.captain_frame, text='Publish Test', bootstyle=(SUCCESS, OUTLINE),
                                          width=14, command=self._click_publish_test)
        self.captain_button2.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.captain_button1)
        self.button_list.append(self.captain_button2)

    def _create_infosafe(self):
        self.infosafe_frame = ttk.Labelframe(self.root, text='InfoSafe', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.infosafe_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.infosafe_button = ttk.Button(self.infosafe_frame, text='Check', bootstyle=(PRIMARY, OUTLINE), width=14,
                                          command=self._click_infosafe_adjust)
        self.infosafe_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.infosafe_button)

    def _create_qconfig(self):
        self.qconfig_frame = ttk.Labelframe(self.root, text='QConfig', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.qconfig_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.qconfig_button = ttk.Button(self.qconfig_frame, text='Review', bootstyle=(INFO, OUTLINE), width=14,
                                         command=self._click_qconfig_publish)
        self.qconfig_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.qconfig_button)

    def _create_xshell(self):
        self.xshell_frame = ttk.Labelframe(self.root, text='XShell', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.xshell_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.xshell_button = ttk.Button(self.xshell_frame, text='Login', bootstyle=(WARNING, OUTLINE), width=14,
                                        command=self._click_xshell_login)
        self.xshell_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.xshell_button)

    def disable_all_button(self):
        for button in self.button_list:
            button.config(state=DISABLED)

    def enable_all_button(self):
        for button in self.button_list:
            button.config(state=NORMAL)

    def _click_publish_b(self):
        ButtonCommand(self, publish_b.main, 'Trip Captain', 'Publish B Environment').on_click()

    def _click_publish_test(self):
        ButtonCommand(self, publish_test.main, 'Trip Captain', 'Publish Test Environment').on_click()

    def _click_infosafe_adjust(self):
        ButtonCommand(self, infosafe_adjust.main, 'Trip Info Safe', 'InfoSafe Adjust').on_click()

    def _click_qconfig_publish(self):
        ButtonCommand(self, qconfig_publish.main, 'Trip QConfig', 'QConfig Publish').on_click()

    def _click_xshell_login(self):
        ButtonCommand(self, xshell_login.main, 'Trip XShell', 'XShell Login').on_click()

    def run(self):
        self.app.mainloop()


class ButtonCommand:
    def __init__(self, app, func, title, message):
        self.app = app
        self.func = func
        self.title = title
        self.message = message

    def _on_click(self):
        Notify.info(self.title, self.message + ' is running')
        self.func()
        Notify.info(self.title, self.message + ' is completed')

    def on_click(self):
        self.app.disable_all_button()
        thread = threading.Thread(target=self._on_click)
        thread.start()


def main():
    app = TripPanel()
    app.run()


if __name__ == '__main__':
    main()
