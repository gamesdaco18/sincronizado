from tkinter import *

root = Tk()

root.title("Mi primer ventana") #Poniendo nuestro primer titulo

root.geometry("500x300") #Dandole las dimensiones a nuestra ventana

root.iconbitmap("python.ico") #Colocando nuestro logo

root.resizable(0,0) #hacemos que nuestra ventana no se modifique ni en el ancho, ni en el alto

root.config(bg="grey", cursor="pirate") #cambiamos color de fondo y cursor del mouse



root.mainloop()
