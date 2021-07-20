from tkinter import *
from tkinter import messagebox

root= Tk()
root.geometry("400x300")

w = Spinbox(root, values=("Python","HTML","Java","JavaScript"))
w.pack()


e = Spinbox(root, values=("Carne","Verdura","Pasta","Gaseosa"))
e.pack()

root.mainloop()