import tkinter as tk
from tkinter import ttk


class Login:
    def __init__(self):
        # window instance 생성
        self.win = tk.Tk()

        # 타이틀 설정
        self.win.title("경무네 과자가게_Login")

        self.create_widgets()

    def create_widgets(self):
        user_id = tk.StringVar()
        id_entry = ttk.Entry(self.win, width=20, textvariable=user_id)
        id_entry.grid(column=0, row=0)

        password = tk.StringVar()
        password_entry = ttk.Entry(self.win, width=20, textvariable=password)
        password_entry.grid(column=0, row=1)

        login_button = ttk.Button(self.win, text="Login")
        login_button.grid(column=1, row=0, rowspan=2)


login = Login()
login.win.mainloop()
