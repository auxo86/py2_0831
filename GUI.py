#  encoding=utf-8
import Tkinter
import tkFont


x=0


def buttonClick1():
    global x
    x += 1
    label.config(text='按了 %d 次'%x)
    print 'Hello World'


top = Tkinter.Tk()
# 位置很重要，要放在Tkinter.Tk後面
myFont = tkFont.Font(family='Arial', size=32)
label = Tkinter.Label(top, text = u'臨床資訊組', font = myFont,
                      padx=30, pady=50, fg='#FF0', bg='#006')

# buttonClick1是函式指標
button = Tkinter.Button(top, text='按鈕一', fg='#F0F', bg='#060, font=myFont'
                        , command=buttonClick1)
# 有pack才能加入主表單
label.pack()
button.pack()
top.mainloop()
