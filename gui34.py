from operator import index
from tkinter import *

def show_item(e):
  index_tuple=lb1.curselection()
  item=lb1.get(index_tuple[0])
  l1.config(text="Youselected:"+item)

root = Tk()
root.geometry("300x300")
l1=Label(root,text="Your selection will appear here")
lb1=Listbox(root)

sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]

for x in sports:
  lb1.insert(END,x)
lb1.bind("<<ListboxSelect>>",show_item)
lb1.grid(row=0,column=0,sticky=W)
l1.grid(row=1,column=0,sticky=W)
root.mainloop()
