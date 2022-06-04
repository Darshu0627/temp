
from tkinter import*
import sys
def finish():
    sys.exit(0)
def show():
    fname=e1.get()
    lname=e2.get()
    l3.config(text=fname+" "+lname)

root=Tk()
l1=Label(root,text="First Name")
l2=Label(root,text="Last Name")
l3=Label(root,width=20,anchor=W,font="Arial 10 bold")
e1=Entry(root)
e2=Entry(root)
b1=Button(root,text='Show',command=show)
b2=Button(root,text='Quit',command=finish)
root.geometry('300x200')
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
l3.grid(row=3,columnspan=2,sticky=W)
b1.grid(row=4,column=0,sticky=W,pady=4)
b2.grid(row=4,column=1,sticky=W,pady=4)
e1.insert(0,"Darshana")
e1.delete(0,END)
e1.insert(0,"Bhikonde")

root.mainloop()