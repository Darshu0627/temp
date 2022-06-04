from tkinter import *
import sys

def finish():
  	sys.exit(0)
def show():
	fname=e1.get()
	lname=e2.get()
	e3.delete(0,END)
	e3.insert(0,fname+" "+lname)

root = Tk()
l1=Label(root, text="First Name")
l2=Label(root, text="Last Name")
l3=Label(root,text="You Typed")
e1 = Entry(root)
e2 = Entry(root)
e3=Entry(root)

b1=Button(root, text='Show', command=show)
b2=Button(root, text='Quit', command=finish)
l1.grid(row=0,column=0,sticky=W)
l2.grid(row=1,column=0,sticky=W)
l3.grid(row=2,column=0,sticky=W)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
b1.grid(row=3, column=0, sticky=W, pady=4)
b2.grid(row=3, column=1, sticky=W, pady=4)
root.mainloop( )
