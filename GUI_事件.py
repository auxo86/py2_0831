#  encoding=utf-8
import Tkinter
from tkFont import Font

def lefSingle(ev):
    label.config(text='left single', fg='#F00')
def leftDouble(ev):
    label.config(text='left double click', fg='#0F0')
def move(ev):
    label.config(text='left drag', fg='#00F')

top = Tkinter.Tk()
myFont = Font(family='Ariel', size=32)

label = Tkinter.Label(top, text='More Event', font=myFont, padx=40)
button = Tkinter.Button(top, text='btn1', font=myFont)

label.pack()
button.pack()

button.bind('<Button-1>', lefSingle)
button.bind('<Double-1>', leftDouble)
button.bind('<B1-Motion>', move)

top.mainloop()