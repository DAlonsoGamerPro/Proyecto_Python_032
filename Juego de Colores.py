from tkinter import *
import random
root = Tk()
root.title("Juego de Colores")
root.geometry("500x400")
root.config(bg="CadetBlue1")

label_score = Label(root,text="Puntos: 0",font=("Bahnschrift Light",15,"bold"),bg="CadetBlue1")
label_score.place(relx=0.1,rely=0.1,anchor=CENTER)

label_name = Label(root,font=("Arial",40),bg="CadetBlue1")
label_name.place(relx=0.5,rely=0.3,anchor=CENTER)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5,anchor=CENTER)

btn = Button(root,text="Verificar",bg="firebrick2",padx=10,pady=1,font=("Arial",15))
btn.place(relx=0.35,rely=0.65,anchor=CENTER)

btn1 = Button(root,text="Iniciar",bg="goldenrod1",padx=10,pady=1,font=("Arial",15))
btn1.place(relx=0.65,rely=0.65,anchor=CENTER)

root.mainloop()