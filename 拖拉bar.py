#  encoding=utf-8
import Tkinter
from tkFont import Font


def func(scale):
    label.config(text=formattedString%int(scale))

top = Tkinter.Tk()
formattedString = 'value=%d'

myFont = Font(family='Ariel', size=24)
value = Tkinter.IntVar()
value.set(0)

label = Tkinter.Label(top, text=formattedString%value.get(),
                      padx=30, font=myFont)
scale = Tkinter.Scale(top, label='Volumn', orient='h', from_=0, command=func,
                      to=100, font=myFont, variable=value)
label.pack()
scale.pack()
top.mainloop()