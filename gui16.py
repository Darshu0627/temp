from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
def accept():
  num=simpledialog.askinteger("Input","Enter voter's age",minvalue=18,maxvalue=122)
  messagebox.showinfo("Hello","You entered "+str(num))

root = Tk()
root.geometry("200x200")
btn=Button(root,text="Click Me",command=accept)
btn.pack()
root.mainloop()
