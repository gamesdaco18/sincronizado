from tkinter import * 

root = Tk()
root.title("Entrada")
root.geometry("400x300")
root.config(bg="gray17")
root.iconbitmap("python.ico")

nombre = StringVar()
apellido = StringVar()

nombre.set("Nombre...")
apellido.set("Apellido...")


def saludar():
    print("Hola " + nombre.get()+ "  " +apellido.get())




etiqueta1 = Label(root, text="Escribe tu nombre: ", bg="gray17", font="Verdana 8 bold", fg="Snow")
etiqueta1.place(x=10, y=10)

entrada1 = Entry(root,textvariable=nombre, bd=2)
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text="Escribe tu apellido: ", bg="gray17", font="Verdana 8 bold", fg="Snow")
etiqueta2.place(x=10, y=40)

entrada2 = Entry(root, textvariable=apellido, bd=2)
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar ahora", command=saludar, bg="Royalblue3",fg="Snow", font="Verdana 8 bold", bd=2)
boton.place(x=10, y=100)

root.mainloop()