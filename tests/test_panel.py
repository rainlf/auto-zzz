from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

app = ttk.Window()

sf = ttk.Meter(bootstyle="success", subtextstyle="warning")

sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()



import ttkbootstrap as ttkb
from abc import ABC, abstractmethod

# 定义一个观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, task):
        pass

# 定义一个任务类
class Task:
    def __init__(self):
        self.observers = []
        self.status = "Not Started"

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def start_task(self):
        self.status = "Running"
        self.notify_observers()
        # 执行任务逻辑...
        self.status = "Completed"
        self.notify_observers()

# 定义一个 UI 类
class UI(ttkb.Window):
    def __init__(self, task):
        super().__init__(themename='flatly')
        self.task = task
        self.init_ui()

    def init_ui(self):
        self.title("Task Status")
        self.geometry("300x200")

        self.label = ttkb.Label(self, text=self.task.status)
        self.label.pack(pady=10)

        self.start_button = ttkb.Button(self, text="Start Task", command=self.start_task)
        self.start_button.pack(pady=10)

        self.task.add_observer(self)

    def update(self, task):
        self.label.configure(text=task.status)
        self.update_idletasks()  # 强制更新界面

    def start_task(self):
        self.task.start_task()

# 创建任务实例
task = Task()

# 创建 UI 实例
ui = UI(task)
ui.mainloop()