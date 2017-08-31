#  encoding=utf-8
import Tkinter
from tkFont import Font

def motion(ev):
    message.config(text='move to [%d, %d]' % (ev.x, ev.y))

top = Tkinter.Tk()
myFont = Font(family='Ariel', size=24)

message = Tkinter.Message(top, text='Title', font=myFont, padx=200, pady=200)

message.bind('<Motion>', motion)
message.pack()

top.mainloop()