from tkinter import *

import time

root = Tk()
root.title("Mi primer ventana")
root.geometry("500x300")
root.iconbitmap("python.ico")
root.config(bg="gray17")


boton1 = Button(root, text="Minimizar", command=root.iconify, bg="red", font=" Verdana 10 bold", fg="white")
boton1.pack(side=LEFT)

def imprimir():
    label_1 = Label(root,text="Imprimiendo....", bg="gray17", font=" Verdana 10 bold", fg="White")
    label_1.pack()

boton2 = Button(root, text="Imprimir", command=imprimir, bg="blue",font=" Verdana 10 bold", fg="white")
boton2.pack(side=RIGHT)







root.mainloop()