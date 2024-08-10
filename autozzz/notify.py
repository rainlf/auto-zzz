from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification


class Notify:
    @classmethod
    def info(cls, title, message):
        Notify._notify(title, message, INFO)

    @classmethod
    def warn(cls, title, message):
        Notify._notify(title, message, WARNING)

    @classmethod
    def _notify(cls, title, message, bootstyle):
        toast = ToastNotification(title=title, message=message, duration=3000, bootstyle=bootstyle)
        toast.show_toast()
