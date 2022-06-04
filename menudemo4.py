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
file_menu=Menu(menubar,tearoff=0)

file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator
file_menu.add_command(label='Exit',command=root.destroy)

#add file menu to menubar
menubar.add_cascade(label='File',menu=file_menu)

#create help menu
help_menu=Menu(menubar,tearoff=0)

#add menuitem to help menu
help_menu.add_command(label='About Us')
help_menu.add_command(label='Contect Us')

#add help menu to the menubar+-
menubar.add_cascade(label='Help',menu=help_menu)
root.mainloop()