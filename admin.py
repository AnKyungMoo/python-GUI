import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

win = tk.Tk()

tabControl = ttk.Notebook(win)

console_tab = ttk.Frame(tabControl)
tabControl.add(console_tab, text='console')

refill_tab = ttk.Frame(tabControl)
tabControl.add(refill_tab, text='refill')

tabControl.pack(expand=1, fill='both')

scrolled_text = scrolledtext.ScrolledText(console_tab, width=80, height=30, wrap=tk.WORD)
scrolled_text.grid(column=0, row=0)

win.mainloop()
