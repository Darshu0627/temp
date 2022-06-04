from distutils.command.config import config
from tkinter import *

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
b1.pack()
b1.bind("<Button>",lambda e:root.config(bg="red"))
root.mainloop()