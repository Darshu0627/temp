from tkinter import *
from tkinter.ttk import *

from time import strftime
root =Tk()
root.title("Clock")
def time():
    string=strftime('%H:%M:%S %p')
    Label.config(text=string)
    label.after(1000,time)

lable =Label(root,font=25,background="black",foreground ="cyan")
lable.pack(anchor='center')
time()

mainloop()
