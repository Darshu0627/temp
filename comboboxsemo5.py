import tkinter as tk 
import tkinter.ttk as ttk
import tkinter.messagebox

def showselection(event):
    tkinter.messagebox.showinfo("Your Choise","You Selected:"+combo.get())

def additem(event):
    currvalues=combo['values']
    currvalues=list(currvalues)
    if str.get() in currvalues:
        tkinter.messagebox.showinfo("Failed ","Item already present")
        return

    currvalues.append(str.get())
    combo['values']=currvalues
    str.set("")
    tkinter.messagebox.showinfo("Sucess ","Item added")


    

root=tk.Tk()
str=tk.StringVar()
root.geometry('500x400')
lbl=tk.Label(root, text="Chose your fevorite month")
combo=ttk.Combobox(root,values=['January','February','March','April'],textvariable=str)

lbl.grid(column=0,row=0)
combo.grid(column=0,row=1)

combo.current(0)
combo.bind("<<ComboboxSelected>>",showselection )
combo.bind("<Return>",additem)

root.mainloop()