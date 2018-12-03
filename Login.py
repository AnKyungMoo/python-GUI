import tkinter as tk
from tkinter import ttk
import Admin
import Client
import requests
import strings
from tkinter import messagebox as msg


class Login:
    def __init__(self):
        # window instance 생성
        self.win = tk.Tk()

        # 타이틀 설정
        self.win.title("경무네 과자가게_Login")

        self.create_widgets()

    def click_login(self):
        uid = self.user_id.get()
        upw = self.password.get()

        if uid == 'admin' and upw == '1234':
            Admin.Admin().win.mainloop()
        else:
            Client.Client().win.mainloop()

    def click_sign_up(self):
        uid = self.user_id.get()
        upw = self.password.get()

        params = {'id':uid, 'pw':upw}

        response = requests.get(url=strings.url + '/join', data=params).json()

        if (response['success']):
            msg.showinfo('성공', '회원가입되었습니다.');
        else:
            msg.showwarning('실패', '회원가입에 실패하였습니다.');

    def create_widgets(self):
        ttk.Label(self.win, text='과자 가게 들어가기').grid(column=0, row=0, columnspan=3)

        ttk.Label(self.win, text='id').grid(column=0, row=1)
        self.user_id = tk.StringVar()
        id_entry = ttk.Entry(self.win, width=20, textvariable=self.user_id)
        id_entry.grid(column=1, row=1)

        ttk.Label(self.win, text='password').grid(column=0, row=2)
        self.password = tk.StringVar()
        password_entry = ttk.Entry(self.win, show='*', width=20, textvariable=self.password)
        password_entry.grid(column=1, row=2)

        login_button = ttk.Button(self.win, text="Login", command=self.click_login)
        login_button.grid(column=1, row=3, sticky=tk.E)

        sign_button = ttk.Button(self.win, text="Sign Up", command=self.click_sign_up)
        sign_button.grid(column=0, row=3)


if __name__ == '__main__':
    login = Login()
    login.win.mainloop()
