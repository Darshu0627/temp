from tkinter import *

def changecolor():
  root.configure(bg=x.get())

root = Tk()
root.geometry("200x200")
x=StringVar()
old_color=root["bg"]
cb=Checkbutton(root,text="Red",command=changecolor,variable=x, onvalue="#ff0000",offvalue=old_color)
cb.deselect()
cb.pack()

root.mainloop()
