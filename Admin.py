import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from PIL import ImageTk, Image


class Admin:
    def __init__(self):
        self.win = tk.Tk()

        # 타이틀 설정
        self.win.title("admin")
        self.win.resizable(False, False)

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
                    self.console.configure(state='normal')
                    self.console.insert(tk.INSERT, self.snacks[index] + ' refill\n')
                    self.console.configure(state='disabled')

    def create_widgets(self):
        tab_control = ttk.Notebook(self.win)

        console_tab = ttk.Frame(tab_control)
        tab_control.add(console_tab, text='console')

        refill_tab = ttk.Frame(tab_control)
        tab_control.add(refill_tab, text='refill')

        tab_control.pack(expand=1, fill='both')

        self.console = scrolledtext.ScrolledText(console_tab, width=75, height=37, wrap=tk.WORD, state='disabled')
        self.console.grid(column=0, row=0)

        # 체크박스 생성
        for ro in range(0, 3, 2):
            for col in range(3):
                index = int(ro + (col + (ro / 2)))

                # 이미지 display
                img = ImageTk.PhotoImage(Image.open(self.snacks[index] + '.png'))
                aa = tk.Label(refill_tab, image=img)
                aa.image = img
                aa.grid(column=col, row=ro, sticky=tk.W)

                self.check_button_var.append(tk.IntVar())

                check_button = tk.Checkbutton(refill_tab, text=self.snacks[index], variable=self.check_button_var[index])
                check_button.grid(column=col, row=ro+1, sticky=tk.E)

        refill_button = ttk.Button(refill_tab, text='refill!', command=self.click_refill)
        refill_button.grid(column=3, row=4, sticky=tk.E)


admin = Admin()
admin.win.mainloop()
