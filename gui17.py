from cgitb import text
from tkinter import *
from tkinter import filedialog, messagebox
def showopen():
  fname=filedialog.askopenfilename(initialdir="C:/",title="Choose a file",filetypes=[("mp3 files","*.mp3"),("text files","*.txt")])
  if fname!="":
      messagebox.showinfo("Your Selection",fname)
  else:
      messagebox.showinfo("Your selection","No file Selected")
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=showopen)
btn.pack()
root.mainloop()