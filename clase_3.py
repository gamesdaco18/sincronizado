from tkinter import *

root = Tk()
root.title("Posicionar")
root.geometry("400x200")
root.config(bg="gray17")
root.iconbitmap("python.ico")


def saludo():
    print("Hola te saludo")

def minimizar():
    root.iconify()


etiqueta1 = Label(root, text="Saluda desde aqui", bg="gray17", font="Verdana 10 bold", fg="SpringGreen3")
etiqueta1.place(x=30, y=50)

etiqueta2 = Label(root, text="Minimiza desde aqui",bg="gray17", font="Verdana 10 bold", fg="SpringGreen3")
etiqueta2.place(x=30, y=100)

bonton1 = Button(root, text="Haz click aqui para saludar", command=saludo,bg="SpringGreen4", font="Verdana 8 bold", fg="Snow")
bonton1.place(x=200, y=50)

bonton2 = Button(root, text="Haz click aqui para minimizar", command=minimizar,bg="SpringGreen4", font="Verdana 8 bold", fg="Snow")
bonton2.place(x=200, y=100)



root.mainloop()

