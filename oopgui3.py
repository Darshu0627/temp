from tkinter import *
class MyGUI:
    def __init__(self,root):
        self.root=root
	   self.root.geometry('200x200')
        self.b1 = Button(root, text="Click Me", command=self.incrementcount)
        self.l1 = Label(root, text="0")
        self.b1.pack()
        self.l1.pack()
	   self.count=0
    def incrementcount(self):
        self.count+=1
        self.l1.configure(text=str(self.count))
root = Tk()
obj=MyGUI(root)
root.mainloop()
