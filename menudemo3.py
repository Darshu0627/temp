#from asyncore import file_dispatcher
#from cProfile import label
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
def showmsg():
    messagebox.showinfo("Hello","Good Morning")
#create the root window
root=tk.Tk()
root.title("Menu Demo")
root.geometry('500x400')

#Create the menubar
menubar=Menu(root)

#add menubar to the root
root.config(menu=menubar)

#create the file menu
file_menu=Menu(menubar)

#add menubar to the file menu
file_menu.add_command(label='Exit',command=root.destroy)

#add file to the menubar
menubar.add_cascade(label='File',menu=file_menu,underline=0)

root.mainloop()