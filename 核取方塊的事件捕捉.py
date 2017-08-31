#  encoding=utf-8
import Tkinter
from tkFont import Font

def func1():
    label.config(text='button%d selected' % selector.get())
# def func2():
#     label.config(text='button%d selected' % selector.get())


top = Tkinter.Tk()
myFont = Font(family='Ariel', size=24)

selector = Tkinter.IntVar(); selector.set(2)

label = Tkinter.Label(top, text='Choice', font=myFont)
rb1 = Tkinter.Radiobutton(top, text='choice1', command=func1,
                          variable=selector, value=1, font=myFont)
rb2 = Tkinter.Radiobutton(top, text='choice2', command=func1,
                          variable=selector, value=2, font=myFont)

label.pack()
rb1.pack(); rb2.pack()

top.mainloop()
