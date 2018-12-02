import tkinter as tk
from tkinter import scrolledtext

win = tk.Tk()

scroll_width = 80
scroll_height = 30
scrolled_text = scrolledtext.ScrolledText(win, width=scroll_width, height=scroll_height, wrap=tk.WORD)
scrolled_text.grid(column=0, columnspan=3)

win.mainloop()
