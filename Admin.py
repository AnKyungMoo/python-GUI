import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk


class Admin:
    def __init__(self):
        self.win = tk.Tk()

        # 타이틀 설정
        self.win.title("admin")

        # 변수
        self.snacks = ['Shrimp', 'Potato', 'Squid', 'Butter', 'Strawberry', 'Orange']
        self.check_button_var = []

        # 위젯 생성
        self.create_widgets()

    def click_refill(self):
        for ro in range(2):
            for col in range(3):
                index = ro + (col + (ro * 2))

                if self.check_button_var[index].get() == 1:
                    # TODO: 서버로 보내자
                    print(self.snacks[index] + ' refill')

    def create_widgets(self):
        tab_control = ttk.Notebook(self.win)

        console_tab = ttk.Frame(tab_control)
        tab_control.add(console_tab, text='console')

        refill_tab = ttk.Frame(tab_control)
        tab_control.add(refill_tab, text='refill')

        tab_control.pack(expand=1, fill='both')

        scrolled_text = scrolledtext.ScrolledText(console_tab, width=80, height=30, wrap=tk.WORD)
        scrolled_text.grid(column=0, row=0)

        # 체크박스 생성
        for ro in range(2):
            for col in range(3):
                index = ro + (col + (ro * 2))

                self.check_button_var.append(tk.IntVar())

                check_button = tk.Checkbutton(refill_tab, text=self.snacks[index], variable=self.check_button_var[index])
                check_button.grid(column=col, row=ro, sticky=tk.W)

        refill_button = ttk.Button(refill_tab, text='refill!', command=self.click_refill)
        refill_button.grid(column=2, row=2)


admin = Admin()
admin.win.mainloop()
