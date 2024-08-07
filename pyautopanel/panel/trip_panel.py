import threading

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification


def notify(title, message):
    toast = ToastNotification(title=title, message=message, duration=3000, bootstyle=PRIMARY)
    toast.show_toast()


class TripPanel:
    def __init__(self):
        self.button_list = []
        self._create_root()
        self._create_title()
        self._create_separator()
        self._create_captain()
        self._create_infosafe()
        self._create_separator()
        self._create_qconfig()
        self._create_xshell()

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

    def _create_title(self):
        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(side=TOP, fill=BOTH)
        self.title = ttk.Label(self.title_frame, text='Trip', font=('TkDefaultFont', 14, 'bold'), bootstyle=PRIMARY)
        self.title.pack(side=LEFT, fill=BOTH)

    def _create_separator(self):
        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.pack(side=TOP, fill=BOTH, pady=10)

    def _create_captain(self):
        self.captain_frame = ttk.Labelframe(self.root, text='Captain', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.captain_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.captain_button1 = ttk.Button(self.captain_frame, text='Publish B', bootstyle=(PRIMARY, OUTLINE), width=14,
                                          command=lambda: test2(self))
        self.captain_button1.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.captain_button2 = ttk.Button(self.captain_frame, text='Publish Test', bootstyle=(SUCCESS, OUTLINE),
                                          width=14)
        self.captain_button2.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.captain_button1)
        self.button_list.append(self.captain_button2)

    def _create_infosafe(self):
        self.infosafe_frame = ttk.Labelframe(self.root, text='InfoSafe', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.infosafe_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.infosafe_button = ttk.Button(self.infosafe_frame, text='Check', bootstyle=(PRIMARY, OUTLINE), width=14)
        self.infosafe_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.infosafe_button)

    def _create_qconfig(self):
        self.qconfig_frame = ttk.Labelframe(self.root, text='QConfig', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.qconfig_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.qconfig_button = ttk.Button(self.qconfig_frame, text='Review', bootstyle=(INFO, OUTLINE), width=14)
        self.qconfig_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.qconfig_button)

    def _create_xshell(self):
        self.xshell_frame = ttk.Labelframe(self.root, text='XShell', padding=(10, 10, 10, 10), bootstyle=DEFAULT)
        self.xshell_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.xshell_button = ttk.Button(self.xshell_frame, text='Login', bootstyle=(WARNING, OUTLINE), width=14)
        self.xshell_button.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)
        self.button_list.append(self.xshell_button)

    def _disable_all_button(self):
        for button in self.button_list:
            button.config(state=DISABLED)

    def _enable_all_button(self):
        for button in self.button_list:
            button.config(state=NORMAL)

    def _publish_b(self):
        self._enable_all_button()

    def _click_publish_b(self):
        self._disable_all_button()
        thread = threading.Thread(target=self._publish_b)
        thread.start()

    def run(self):
        self.app.mainloop()


def main():
    app = TripPanel()
    app.run()


if __name__ == '__main__':
    main()
