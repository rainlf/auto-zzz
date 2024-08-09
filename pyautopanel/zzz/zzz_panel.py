import threading

import ttkbootstrap as ttk
from PIL import Image
from loguru import logger
from ttkbootstrap.constants import *

from pyautopanel.zzz.timer import Timer

Image.CUBIC = Image.BICUBIC


class ZzzPanel:
    def __init__(self):
        self._timer = Timer(self._time_update)
        self._create_panel()

    def disable_start_button(self):
        self.start_button.config(state=DISABLED)

    def enable_start_button(self):
        self.start_button.config(state=ACTIVE)

    def set_meter(self, value):
        self.meter.configure(amountused=value)

    def run(self):
        self.app.mainloop()

    def _create_panel(self):
        self.app = ttk.Window(
            title='RainAutoTools',
            themename='litera',  # 设置主题
            size=(380, 480),  # 窗口的大小 （宽, 高）
            position=(1100, 480),  # 窗口所在的位置
            minsize=(0, 0),  # 窗口的最小宽高
            maxsize=(1920, 1080),  # 窗口的最大宽高
            resizable=None,  # 设置窗口是否可以更改大小
            alpha=1.0,  # 设置窗口的透明度(0.0完全透明）
        )
        self.app.resizable(False, False)

        # root
        root = ttk.Frame(self.app, padding=(20, 10, 20, 5))
        root.pack(side=TOP, fill=BOTH)

        # title
        title_frame = ttk.Frame(root)
        title_frame.pack(side=TOP, fill=BOTH, pady=10)
        title = ttk.Label(title_frame, text='ZZZ', font=('Segoe UI', 18, 'bold'), bootstyle=PRIMARY)
        title.pack(side=LEFT)
        stop_button = ttk.Button(title_frame, text='STOP', bootstyle=DANGER)
        stop_button.pack(side=RIGHT)
        restart_button = ttk.Button(title_frame, text='RESTART', bootstyle=SUCCESS)
        restart_button.pack(side=RIGHT, padx=5)
        pause_button = ttk.Button(title_frame, text='PAUSE', bootstyle=WARNING)
        pause_button.pack(side=RIGHT)
        # test_button = ttk.Button(title_frame, text='Test', bootstyle=(PRIMARY, OUTLINE))
        # test_button.pack(side=RIGHT, padx=10)
        # test_button.configure(command=self._test)

        # separator
        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(side=TOP, fill=BOTH, pady=10)

        # button frame
        button_frame = ttk.Frame(root)
        button_frame.pack(side=TOP, fill=BOTH, pady=10)
        # start button
        self.start_button = ttk.Button(button_frame, text='Start Hollow Explore', bootstyle=(PRIMARY, OUTLINE))
        self.start_button.pack(side=LEFT)
        # combo box button
        self.combo = ttk.Combobox(button_frame, values=["IceWolf", "No.11", "BoomSister"], width=14, state='readonly')
        self.combo.pack(side=RIGHT, pady=10)
        self.combo.current(0)

        # meter frame
        meter_frame = ttk.Frame(root)
        meter_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.meter = ttk.Meter(
            master=meter_frame,
            metersize=235,  # 直径
            amounttotal=50,  # 总值
            amountused=22,  # 当前值
            subtext='Round',  # 子文本
            metertype=ARC,  # 类型为弧形
            stripethickness=6,  # 条纹厚度
            bootstyle=SUCCESS,  # 样式
            textright='')  # 右边的文字
        self.meter.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10)

        # timer frame
        time_frame = ttk.Frame(root)
        time_frame.pack(side=TOP, fill=BOTH, pady=10)
        self.time_label = ttk.Label(time_frame, text='00:00:00', font=('Segoe UI', 12), bootstyle=PRIMARY)
        self.time_label.pack(side=RIGHT)

        # command
        stop_button.configure(command=self._click_stop_button)
        restart_button.configure(command=self._click_restart_button)
        pause_button.configure(command=self._click_pause_button)
        self.start_button.configure(command=self._click_start_button)


    def _test(self):
        logger.info(self.combo.get())
        self.combo.current(1)
        self.meter.configure(amountused=110)
        self.start_button.config(state=ACTIVE)
        self.time_label.configure(text='00:10:10')

    def _time_update(self, time_str):
        self.time_label.configure(text=time_str)

    def _click_start_button(self):
        threading.Thread(target=lambda x: x.run(), args=(self._timer,)).start()
        self.disable_start_button()

    def _click_stop_button(self):
        self._timer.stop()
        self.enable_start_button()
        self.set_meter(0)
        self.time_label.configure(text='00:00:00')

    def _click_restart_button(self):
        self._timer.restart()

    def _click_pause_button(self):
        self._timer.pause()


def main():
    app = ZzzPanel()
    app.run()


if __name__ == '__main__':
    main()
