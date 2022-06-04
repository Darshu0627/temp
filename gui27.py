from tkinter import *

def changecolor():
  if x.get()==1:
    root.configure(bg="#ff0000")
  else:
    root.configure(bg=old_color)

root = Tk()
root.geometry("200x200")
old_color=root["bg"]
x=IntVar()
cb=Checkbutton(root,text="red",command=changecolor,variable=x)
cb.pack()
root.mainloop()