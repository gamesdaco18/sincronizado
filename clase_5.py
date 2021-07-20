from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("300x300")
root.config(bg="gray17")
root.iconbitmap("python.ico")
root.resizable(0,0)

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()



def saludar():
    saludo.set("Hola "+nombre.get()+ "  "+apellido.get())





etiqueta1 = Label(root, text="Escribe tu nombre: ", bg="gray17", font="Console 10 bold", fg="Snow")
etiqueta1.place(x=10, y=10)

entrada1 = Entry(root,textvariable=nombre, font="Console 10 bold", bd=2)
entrada1.place(x=140, y=10)

etiqueta2 = Label(root, text="Escribe tu apellido: ", bg="gray17", font="Console 10 bold", fg="Snow")
etiqueta2.place(x=10, y=40)

entrada2 = Entry(root, textvariable=apellido, font="Console 10 bold", bd=2)
entrada2.place(x=140, y=40)

boton = Button(root, text="Saludar ahora", command=saludar, bg="#ffcc66",fg="#141414", font="Console 10 bold", border=0)
boton.place(x=100, y=80)

entrada3 = Entry(root, font="Console 8 bold",bd=10, textvariable=saludo, state="disable")
entrada3.place(x=80, y=120)


root.mainloop()