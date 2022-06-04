from tkinter import *
from tkinter import filedialog, messagebox
def showopen():
  fname=filedialog.askopenfilenames(initialdir="C:/",title="Choose a file",filetypes=[("mp3 files","*.mp3"),("text files","*.txt")])
  if type(fnames) is tuple:
      str=""
      for f in fnames:
          str=str+f+"\n"
      lbl.config(text=str)

  else:
      messagebox.showinf("Your Selection","No file  selected")

root = Tk()
root.geometry("600x300")
btn=Button(root,text="Open Files",command=showopen)
lbl=Label(root,text="Your selected file names will appear here")
btn.pack()
lbl.pack()
root.mainloop()