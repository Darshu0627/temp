import tkinter as tk 
import tkinter.ttk as ttk
import tkinter.messagebox

def showselection(event):
    tkinter.messagebox.showinfo("Your Choise","You Selected:"+combo.get())

root=tk.Tk()


root.geometry('500x400')
lbl=tk.Label(root, text="Chose your fevorite month")
combo=ttk.Combobox(root,values=['January','February','March','April'])

lbl.grid(column=0,row=0)
combo.grid(column=0,row=1)

combo.current(0)
combo.bind("<<ComboboxSelected>>",showselection )

root.mainloop()