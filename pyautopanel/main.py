import tkinter as tk
from tkinter import ttk
import threading
import time

def print_numbers(button):
    # 在这里执行长时间运行的任务
    for i in range(1, 4):
        print(i)
        time.sleep(1)  # 模拟耗时操作


    # 任务完成后重新激活按钮

def on_click(button):
    # 禁用按钮
    button.config(state='disabled')

    # 在子线程中执行任务
    thread = threading.Thread(target=print_numbers, args=(button,))
    thread.start()
    thread.join()
    button.config(state='normal')



root = tk.Tk()
root.title("TTK Button Example")

# 创建一个 ttk.Button 实例
button = ttk.Button(root, text="Click me!", command=lambda: on_click(button))
button.pack(pady=20)

root.mainloop()