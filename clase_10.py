from tkinter import *

root=Tk()
root.title("Almacen")
root.geometry("400x400")
root.iconbitmap("python.ico")


def agregar():
    listaProductos.insert(END, entrada.get())
    entrada.delete(0,END)
    
def borrar():
    listaProductos.delete(listaProductos.curselection())


productos = Label(root,text="Productos")
productos.pack()


listaProductos = Listbox(root, width=50)
listaProductos.insert(0,"Carne")
listaProductos.insert(1,"Pollo")
listaProductos.insert(2,"Verdura")
listaProductos.insert(3,"Gaseosa")
listaProductos.pack()


#Eliminar productos

listaProductos.delete(0)


entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar Producto", bd=10, command=agregar)
boton.pack()

boton = Button(root, text="Quitar Producto", bd=10, command=borrar)
boton.pack()



root.mainloop()