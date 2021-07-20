from tkinter import *

root= Tk()
root.title("RadioButtons")
root.geometry("400x300")
root.config(bg="Gray17")
root.iconbitmap("python.ico")
root.resizable(0,0)

opcion = IntVar()
num = IntVar()

def operacion():
    numero = num.get()
    if opcion.get()==1:
        total = numero*5
    elif opcion.get()==2:
        total = numero*10
    elif opcion.get()==3:
        total = numero*20
    elif opcion.get()==4:
        total = numero*30
    elif opcion.get()==5:
        total = numero*40
    else:
        total = numero * numero
    # print(f"El total de la operacion es: {str(total)}")
    etiqueta3=Label(root,text= f"El total de la operacion es: {str(total)}",bg="Gray17",font="Console 10 bold ", fg="Green2")
    etiqueta3.place(x=70, y=180)






etiqueta1 = Label(root, text="Escriba su numero: ",bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow")
etiqueta1.place(x=20, y=20)

entrada1 = Entry(root,textvariable=num,bg="snow", bd=4, font="Console 10 bold ")
entrada1.place(x=150, y=20)


etiqueta2 = Label(root, text="Elija la cantidad: ",bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow")
etiqueta2.place(x=20, y=50)


x5 = Radiobutton(root,text="x5", value=1, bg="Gray17", bd=5, font="Console 10 bold ", fg="Snow",activeforeground="gray16",activebackground="Orange red",selectcolor="grey7", variable=opcion)
x5.place(x=20, y=80)


x10 = Radiobutton(root,text="x10", value=2,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="Orange red",selectcolor="grey7", variable=opcion)
x10.place(x=70, y=80)

x20 = Radiobutton(root,text="x20", value=3,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="Orange red",selectcolor="grey7", variable=opcion)
x20.place(x=120, y=80)

x30 = Radiobutton(root,text="x30", value=4,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="Orange red",selectcolor="grey7", variable=opcion)
x30.place(x=20, y=110)

x40 = Radiobutton(root,text="x40", value=5,bg="Gray17", bd=5, font="Console 10 bold", fg="Snow",activeforeground="gray16",activebackground="Orange red",selectcolor="grey7", variable=opcion)
x40.place(x=70, y=110)


boton1 = Button(root, text="Realizar operacion", font="Console 10 bold", bg="Snow",fg="Gray7", bd=4, command=operacion)
boton1.place(x=70, y="140")

root.mainloop()