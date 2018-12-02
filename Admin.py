import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk


class Admin:
    def __init__(self):
        self.win = tk.Tk()

        # 타이틀 설정
        self.win.title("admin")

        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.win)

        console_tab = ttk.Frame(tab_control)
        tab_control.add(console_tab, text='console')

        refill_tab = ttk.Frame(tab_control)
        tab_control.add(refill_tab, text='refill')

        tab_control.pack(expand=1, fill='both')

        scrolled_text = scrolledtext.ScrolledText(console_tab, width=80, height=30, wrap=tk.WORD)
        scrolled_text.grid(column=0, row=0)


admin = Admin()
admin.win.mainloop()
