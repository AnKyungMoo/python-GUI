import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import strings


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return

        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)

        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tohoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


def create_ToolTip(widget, text):
    tool_tip = ToolTip(widget)

    def enter(event):
        tool_tip.show_tip(text)

    def leave(event):
        tool_tip.hide_tip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class Client:
    def __init__(self):
        # window instance 생성
        self.win = tk.Toplevel()

        # 타이틀 설정
        self.win.title("경무네 과자가게_손님")

        # 변수
        self.snackList = []
        self.snacks = ['Shrimp', 'Potato', 'Squid', 'Butter', 'Strawberry', 'Orange']
        self.remain_snacks = {self.snacks[0]: 3, self.snacks[1]: 3, self.snacks[2]: 3, self.snacks[3]: 3,
                              self.snacks[4]: 3, self.snacks[5]: 3}
        self.own_snacks_dictionary = {self.snacks[0]: 0, self.snacks[1]: 0, self.snacks[2]: 0, self.snacks[3]: 0,
                           self.snacks[4]: 0, self.snacks[5]: 0}

        self.radio_buttons = []
        self.radio_var = tk.IntVar()

        self.create_widgets()

    # 관리자 전화번호 확인하는 콜백 함수
    def check_number(self):
        msg.showinfo('전화번호', strings.number)

    # 구매버튼을 클릭했을 때 동작을 구성한 콜백 함수
    def purchase(self):
        index = self.radio_var.get()

        if self.remain_snacks[self.snacks[index]] > 0:
            self.snackList.append(self.snacks[index])
            self.own_snacks_dictionary[self.snacks[index]] += 1
            self.remain_snacks[self.snacks[index]] -= 1

            self.message_label.configure(text=self.snacks[index] + ' 과자를 샀다!')
            self.radio_buttons[index].configure(
                text=self.snacks[index] + ' x' + str(self.remain_snacks[self.snacks[index]]))
        else:
            msg.showwarning('SOLD OUT!!', self.snacks[index] + '는 매진입니다.')

    # 가지고 있는 과자 확인 함수
    def own_snack(self):
        temp_string = ''
        for i in range(len(self.snackList)):
            temp_string += (self.snackList[i] + '과자\n')

        msg.showinfo('가지고 있는 과자 확인', temp_string)

    # 과자의 구매 동향 확인하는 차트
    def show_chart(self):
        x = self.snacks
        y = [self.own_snacks_dictionary[self.snacks[0]], self.own_snacks_dictionary[self.snacks[1]],
             self.own_snacks_dictionary[self.snacks[2]], self.own_snacks_dictionary[self.snacks[3]],
             self.own_snacks_dictionary[self.snacks[4]], self.own_snacks_dictionary[self.snacks[5]]]
        plt.bar(x, y, width=0.7)
        plt.show()

    def create_widgets(self):

        # 메뉴를 winow에 적용
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # 기본 메뉴 생성
        basic_menu = Menu(menu_bar, tearoff=0)
        basic_menu.add_command(label='관리자 전화번호', command=self.check_number)
        menu_bar.add_cascade(label='메뉴', menu=basic_menu)

        # 사용자 메뉴 생성
        user_menu = Menu(menu_bar, tearoff=0)
        user_menu.add_command(label='가지고 있는 과자 확인', command=self.own_snack)
        menu_bar.add_cascade(label='사용자', menu=user_menu)

        # 통계 메뉴 생성
        statistics_menu = Menu(menu_bar, tearoff=0)
        statistics_menu.add_command(label='구매 차트 보기', command=self.show_chart)
        menu_bar.add_cascade(label='통계', menu=statistics_menu)

        # window instance 대신에 사용할 mighty Frame 생성
        mighty = ttk.LabelFrame(self.win, text='자판기')
        mighty.grid(column=0, row=0)

        # 무엇을 구매했는지를 알려주기 위한 Label
        self.message_label = ttk.Label(mighty, text="Click the Purchase!")
        self.message_label.grid(column=0, row=4)

        # 구매 버튼 생성
        purchase_button = ttk.Button(mighty, text="Purchase!", command=self.purchase)
        purchase_button.grid(column=2, row=4)

        # 라디오 버튼 초기 설정
        self.radio_var.set(99)

        # 2중 loop를 이용하여 라디오 버튼 생성
        for ro in range(0, 3, 2):
            for col in range(3):
                # 2차원 배열의 index를 계산
                index = int(ro + (col + (ro / 2)))

                # 이미지 display
                img = ImageTk.PhotoImage(Image.open(self.snacks[index] + '.png'))
                aa = tk.Label(mighty, image=img)
                aa.image = img
                aa.grid(column=col, row=ro)

                # 라디오 버튼 생성
                current_radio_button = tk.Radiobutton(mighty, text=self.snacks[index] + ' x' + str(
                    self.remain_snacks[self.snacks[index]]), variable=self.radio_var, value=index)
                self.radio_buttons.append(current_radio_button)
                self.radio_buttons[index].grid(column=col, row=ro + 1, sticky=tk.W)

                create_ToolTip(self.radio_buttons[index], self.snacks[index] + '과자입니다.')

        # for loop를 이용하여 컴포넌트들을 모두 정렬
        for child in mighty.winfo_children():
            child.grid_configure(sticky='E')


if __name__ == '__main__':
    # oop 인스턴스 생성
    client = Client()
    # 메인 루프 시작
    client.win.mainloop()
