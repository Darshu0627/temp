import tkinter as tk 
import tkinter.ttk as ttk

root=tk.Tk()

root.geometry('500x400')
lbl=tk.Label(root, text="Chose your fevorite month")
combo=ttk.Combobox(root,values=['January','February','March','April'])

lbl.grid(column=0,row=0)
combo.grid(column=0,row=1)

root.mainloop()