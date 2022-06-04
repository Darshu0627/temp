from tkinter import *
from tkinter import messagebox,simpledialog
class MyGUI:
    def __init__(self,root):
		self.root = root
        self.root.geometry('400x200+100+200')
        self.l1 = Label(root, text="Number Division Program", font="Arial 18 bold")
        self.l2 = Label(root, text="First No:")
        self.l3 = Label(root, text="Second No:")
        self.l4 = Label(root, text="Result:")
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        self.e3 = Entry(root,fg="green")
        self.b1 = Button(root, text="Divide", command=self.divide)
        self.b2 = Button(root, text="Clear", command=self.clear)
        self.b3 = Button(root, text="Quit", command=self.finish)
        self.l1.grid(row=0, column=0, columnspan=4)
        self.l2.grid(row=1, column=0, sticky=E)
        self.e1.grid(row=1, column=1)
        self.l3.grid(row=2, column=0, sticky=E)
        self.e2.grid(row=2, column=1)
        self.l4.grid(row=3, column=0, sticky=E)
        self.e3.grid(row=3, column=1)
        self.b1.grid(row=4, column=0, pady=5, padx=5, sticky=E + W)
        self.b2.grid(row=4, column=1, pady=5, padx=5, sticky=E + W)
        self.b3.grid(row=4, column=2, pady=5, padx=5, sticky=E + W)
	def divide(self):
         try:
             self.e3.delete(0,END)
             self.e3.config(fg="red")
             a=int(self.el.get())
             b=int(selg.e2.get())
             self.e3.insert(0,str(c))
              
         except ValueError:
             messagebox.showerror("conversion Error ","Plese input digit only")
         except ZeroDivisionError:
             messagebox.showerror("Division Error ","Plese pass non-zero denominator")
             c=a/b
	def clear(self):
		self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)set
        self.e1.focus()
	def finish(self):
		answer=messagebox.askyesno("Quitting","Are you sure?")
        if answer==True:
            name=simpledialog.askstring("Input","What is your name?")
            if name is None or name=="":
                name="userJee"
            messagebox.showinfo("Thank you ","Have a good day"+name+"!")
            self.root.destroy()
root = Tk()
obj=MyGUI(root)
root.mainloop()


