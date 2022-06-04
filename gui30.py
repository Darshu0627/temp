from tkinter import *
root = Tk()
root.geometry("200x200")
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]
i=0
for x in sports:
    lb1.insert(i,x)
    i+=1
lb1.grid(row=1,column=0,sticky=W)
root.mainloop()
