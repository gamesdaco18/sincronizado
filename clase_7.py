from tkinter import *

root = Tk()
root.config(bd=20,bg="gray17")
root.title("Casa de comidas")
root.iconbitmap("python.ico")

def orden():
    lista= ""
    if (queso.get()):
        lista +=" Con Queso "
    else:
        lista +=" Sin Queso"

    if (lechuga.get()):
        lista += " Y Con Lechuga"
    else:
        lista += " Y Sin Lechuga"
    imprimir.config(text=lista)





queso = IntVar()
lechuga = IntVar()


imagen = PhotoImage(file="hamburguesas.png")
Label(root, image=imagen, bg="gray17").pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="gray17")

Label(frame, text="Como quieres tu hamburguesa?", bg="gray17", font="Console 15 bold", fg="Snow").pack(anchor="w")

Checkbutton(frame, text="Con Queso", variable=queso, onvalue=1,offvalue=0, bg="gray17", font="Console 15",fg="Snow",selectcolor="gray", command=orden).pack(anchor="w")
Checkbutton(frame, text="Con Lechuga", variable=lechuga, onvalue=1,offvalue=0, bg="gray17", font="Console 15",fg="Snow",selectcolor="gray", command=orden).pack(anchor="w")

imprimir = Label(frame, bg="Gray17", font="Console 15", fg="green3" )
imprimir.pack()


root.mainloop()
