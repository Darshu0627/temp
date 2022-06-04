from tkinter import *
from tkinter import colorchooser, messagebox

def showopen():
  chosen_color=colorchooser.askcolor(color="#ff0000",title="Select a color")
  if chosen_color[0] is None:
    messagebox.showinfo("Color","No color selected")
  else:
    root.configure(bg=chosen_color[1])
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Choose Color",command=showopen)
btn.pack()
root.mainloop()