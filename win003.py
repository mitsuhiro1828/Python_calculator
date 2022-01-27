# YIC情報ビジネス専門学校
# 情報工学科 1年
# 受田 光弘 (b0021005@ib.yic.ac.jp)
#
#参考 https://rightcode.co.jp/blog/become-engineer/python-tkinter-simple-calculator

import tkinter as tk
from tkinter import ttk

class calculator(object):
    def __init__(self, root=None):

        Button_Value = [
            ['',  'B', 'C', '/',],
            ['7', '8', '9', '*',],
            ['4', '5', '6', '-',],
            ['1', '2', '3', '+',],
            ['', '0', '.', '=',],
        ]
        self.Disabled_button = ['1','2','3','4','5','6','7','8','9','+','-','*','/','.',]
        # 計算用の文字列
        self.Calc_Str = ''

        # 計算式と結果用のframe
        Calc_Frame = ttk.Frame(root, width=300, height=100)
        Calc_Frame.propagate(False)
        Calc_Frame.pack(side=tk.TOP, padx=10, pady=20)
        # ボタン用のframe
        Button_Frame = ttk.Frame(root, width=300, height=400)
        Button_Frame.propagate(0)
        Button_Frame.pack(side=tk.BOTTOM)
        
        self.Calc_Value = tk.StringVar()
        Calc_Label = ttk.Label(Calc_Frame, textvariable=self.Calc_Value, font=("",20))
        Calc_Label.pack(anchor=tk.E)

        # ボタンの作成
        for i, Row in enumerate(Button_Value, 1):
            for j, number in enumerate(Row):
                self.button = tk.Button(Button_Frame, text=number, font=('', 15), width=6, height=3)
                self.button.grid(row=i, column=j) #列、行ずつに配列
                self.button.bind('<ButtonPress>', self.inputValue) #ボタンが押されたとき関数を呼び出す
        
    def inputValue(self, event):
        #↓修正箇所
        try:
            if self.Calc_Str[-1] == '=':
                self.Calc_Str = ''
                self.Calc_Value.set(self.Calc_Str)
        except:
            pass



        check = event.widget['text'] # 押したボタンのCheck
        if check == '=':
            ans = str(eval(self.Calc_Str))
            self.Calc_Value.set(ans)
            self.Calc_Str += check
        elif check == 'B':
            self.Calc_Str = self.Calc_Str[:-1]
            self.Calc_Value.set(self.Calc_Str)
        elif check == 'C':
            self.Calc_Str = ''
            self.Calc_Value.set(self.Calc_Str)
        else:
            self.Calc_Str += check
            self.Calc_Value.set(self.Calc_Str)




def main():
    # ウィンドウの作成
    root = tk.Tk()
    root.title('電卓')
    root.geometry('300x500')
    calculator(root)
    # ウィンドウのループ処理
    root.mainloop()

if __name__ == '__main__':
    main()
