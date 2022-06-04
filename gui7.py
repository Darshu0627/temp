from tkinter import *
oldcolor=""
def anyKey(e):
    ch=e.char
    if ch=="r":
        root.config(bg="red")
    elif ch=="g":
        root.config(bg="green")
    elif ch=="b":
        root.config(bg="blue")
    elif ch=="k":
        root.config(bg="black")
    elif ch=="y":
        root.config(bg="yellow")
root = Tk()
root.geometry('200x200')
root.bind("<Key>",anyKey)

root.mainloop()