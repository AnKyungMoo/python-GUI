import tkinter as tk
from tkinter import ttk

# window instance 생성
win = tk.Tk()

# 타이틀 설정
win.title("과자 자판기")

## 과자의 종류를 담는 배열
snacks = ['새우', '감자', '오징어', '버터', '딸기', '오렌지']

## 구매버튼을 클릭했을 때 동작을 구성한 콜백 함수
def purchase():
    index = radioVar.get()

    messageLabel.configure(text=snacks[index] + ' 과자를 샀다!')
    
# 무엇을 구매했는지를 알려주기 위한 Label
messageLabel = ttk.Label(win, text="Click the Purchase!")
messageLabel.grid(column=0, row=3)

# 구매 버튼 생성
purchaseButton = ttk.Button(win, text="Purchase!", command=purchase)
purchaseButton.grid(column=3, row=3)

# 라디오 버튼에 바인딩할 정수타입의 변수
radioVar = tk.IntVar()

radioVar.set(99)

# 2중 loop를 이용하여 라디오 버튼 생성
for ro in range(2):
    for col in range(3):
        # 배열의 index를 관리해주기 위한 if 문
        if ro == 0:
            index = col + ro
        elif ro == 1:
            index = (col+1) + (ro+1)

        # 라디오 버튼 생성
        currentRadioButton = tk.Radiobutton(win, text=snacks[index], variable=radioVar, value=index)
        currentRadioButton.grid(column=col, row=ro, sticky=tk.W)

# 메인 루프 시작
win.mainloop()
