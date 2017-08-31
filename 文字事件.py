#  encoding=utf-8
import Tkinter
from tkFont import Font

top = Tkinter.Tk()

def display(event):
    label.config(text=entry.get())

myFont = Font(family='Courier', size=24)

label = Tkinter.Label(top, text='Input some text', font=myFont)
entry = Tkinter.Entry(top, font=myFont, bg='#400', fg='#AFF')

entry.bind('<Return>', display)

label.pack()
entry.pack()

top.mainloop()