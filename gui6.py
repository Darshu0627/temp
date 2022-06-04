from tkinter import *
oldcolor=""
def enterKey(e):
    root.config(bg="red")
def escapeKey(e):
    root["bg"]=oldcolor
root = Tk()
root.geometry('200x200')
root.bind("<Return>",enterKey)
root.bind("<Escape>",escapeKey)
oldcolor=root["bg"]
root.mainloop()