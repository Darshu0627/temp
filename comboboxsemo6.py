import tkinter as tk 
import tkinter.ttk as ttk
import tkinter.messagebox

def showselection(event):
    tkinter.messagebox.showinfo("Your Choise","You Selected:"+combo.get())

def removeitem(event):
    currvalues=combo['values']
    currvalues=list(currvalues)
    try:
        currvalues.remove(str.get())
        combo['values']=currvalues
        tkinter.messagebox.showinfo("Success", "Item  removed successfully!!")
    except ValueError:
         tkinter.messagebox.showinfo("Failed", "Item not present!!")
    str.set("")

root=tk.Tk()
str=tk.StringVar()
root.geometry('500x400')
lbl=tk.Label(root, text="Chose your fevorite month")
combo=ttk.Combobox(root,values=['January','February','March','April'],textvariable=str)

lbl.grid(column=0,row=0)
combo.grid(column=0,row=1)

combo.current(0)
combo.bind("<<ComboboxSelected>>",showselection )
combo.bind("<Return>",removeitem)

root.mainloop()