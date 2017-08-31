#  encoding=utf-8
import Tkinter
from tkFont import  Font

def func_enter(ev):
    label.config(text=u'進入')
def func_leave(ev):
    label.config(text=u'離開')
def func_click():
    label.config(text=u'按下')

top = Tkinter.Tk()
myFont = Font(family='Ariel', size=32)
label = Tkinter.Label(top, text='Sample', font=myFont, padx=30, pady=20,
                      fg='#098', bg='#6ff')
button =  Tkinter.Button(top, text='按我', padx='30', pady='20', font=myFont,
                         fg='#040', bg='#F6F', command=func_click)
# <Enter>和<Leave>是關鍵字
button.bind('<Enter>', func_enter)
button.bind('<Leave>', func_leave)

label.pack()
button.pack()
top.mainloop()