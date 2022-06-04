from cProfile import label
import tkinter as tk
from tkinter import Menu

root=tk.Tk()
root.title("Menu Demo")
root.geometry('500x400')

menubar=Menu(root)
root.config(menu=menubar)

file_menu=Menu(menubar)
file_menu.add_command(label='Exit',command=root.destroy)

menubar.add_cascade(label='File',menu=file_menu)

root.mainloop()