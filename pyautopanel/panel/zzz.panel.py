import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ZzzPanel:
    def __init__(self):
        self.button_list = []
        self._create_panel()

    def _create_panel(self):
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

        # root
        root = ttk.Frame(self.app, padding=(20, 20, 20, 20))
        root.pack(side=TOP, fill=BOTH)

        # title
        title_frame = ttk.Frame(root)
        title_frame.pack(side=TOP, fill=BOTH)
        title = ttk.Label(title_frame, text='ZZZ', font=('Segoe UI', 18, 'bold'), bootstyle=PRIMARY)
        title.pack(side=LEFT)
        title_button = ttk.Button(title_frame, text='STOP', bootstyle=WARNING, command=self.enable_all_button)
        title_button.pack(side=RIGHT)

        # separator
        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(side=TOP, fill=BOTH, pady=10)

        # button
        button_frame = ttk.Frame(root)
        button_frame.pack(side=TOP, fill=BOTH, pady=10)
        start_button = ttk.Button(button_frame, text='Start Hollow Explore', bootstyle=(PRIMARY, OUTLINE),
                                  command=self.disable_all_button)
        start_button.pack(side=LEFT)
        self.combo = ttk.Combobox(button_frame, values=["IceWolf", "No.11"], width=14, state='readonly')
        self.combo.pack(side=RIGHT, pady=10)
        self.combo.current(0)
        self.button_list.append(start_button)

    def disable_all_button(self):
        for button in self.button_list:
            button.config(state=DISABLED)

    def enable_all_button(self):
        for button in self.button_list:
            button.config(state=NORMAL)

    def run(self):
        self.app.mainloop()


def main():
    app = ZzzPanel()
    app.run()


if __name__ == '__main__':
    main()
