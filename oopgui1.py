from tkinter import *
class MyGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("An OOP Based GUI")
        self.root.geometry("400x400")
        self.lbl=Label(self.root,text="Click the button")
        self.btn=Button(self.root,text="Click me",Command=self.show)
        self.btn2=Button(self.root,text="Quit",command=self.root.destroy)
        self.lbl.pack()
        self.btn.pack()
        self.btn1.pack()
    def show(self):
        self.lbl.config(text="Welcome to OOP based GUI")

        
root=Tk()
my_gui=MyGUI(root)
root.mainloop()
