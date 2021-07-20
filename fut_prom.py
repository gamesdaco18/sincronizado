from tkinter import *

root= Tk()
root.title("Fut Players %")
root.geometry("400x300")
root.config(bg="Gray17")
root.iconbitmap("python.ico")
root.resizable(0,0)

opcion = IntVar()
num = IntVar()

def operacion():
    numero = num.get()
    if opcion.get()==1:
        total = (numero*10)/100
    elif opcion.get()==2:
        total = (numero*15)/100
    elif opcion.get()==3:
        total = (numero*20)/100
    else:
        total = numero + numero
    etiqueta3=Label(root,text= f"Precio de venta: {str(total + numero)}",bg="Gray17",font="Console 10 bold ", fg="Green2")
    etiqueta3.place(x=20, y=180)



etiqueta1 = Label(root, text="Valor compra: ",bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow")
etiqueta1.place(x=20, y=20)

entrada1 = Entry(root,textvariable=num,bg="snow", bd=4, font="Console 10 bold ")
entrada1.place(x=150, y=20)


etiqueta2 = Label(root, text="Incrementar en un : ",bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow")
etiqueta2.place(x=20, y=50)


x10 = Radiobutton(root,text="10%", value=1, bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow",activeforeground="gray16",activebackground="grey",selectcolor="grey", variable=opcion)
x10.place(x=20, y=80)

x15 = Radiobutton(root,text="15%", value=2,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="grey",selectcolor="grey", variable=opcion)
x15.place(x=70, y=80)

x20 = Radiobutton(root,text="20%", value=3,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="grey",selectcolor="grey", variable=opcion)
x20.place(x=120, y=80)

boton1 = Button(root, text="Realizar operacion", font="Console 10 bold", bg="Snow",fg="Gray7", bd=4, command=operacion)
boton1.place(x=20, y=140)

root.mainloop()