from tkinter import *
from tkinter import simpledialog,messagebox

def show_item():
  pos=simpledialog.askinteger("Input","Enter item no",minvalue=1,maxvalue=lb1.size())
  if type(pos) is int:
    item=lb1.get(pos-1)
    l1.configure(text="You selected:"+item)
  else:
    messagebox.showinfo("Cancel Pressed!","You didn't input any value")
root = Tk()
root.geometry("300x300")
l1=Label(root,text="Your selection will appear here")
b1=Button(root,text="show item",command=show_item)
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]
for x in sports:
  lb1.insert(END,x)

lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop()
