from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

app = ttk.Window()

sf = ttk.Meter(bootstyle="success", subtextstyle="warning")

sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()
