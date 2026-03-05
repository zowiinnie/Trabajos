import tkinter as tk
from tkinter import messagebox


def estatus():
    if var.get() == 1:
       messagebox.showinfo("Estado", "Checkbutton seleccionado")
    
    else:
        messagebox.showinfo("Estado", "Checkbutton no esta seleccionado") 


ven1 = tk.Tk()
ven1.title()
ven1.geometry("16090x500")

etiqueta1 = tk.Label (ven1, text = "Aqui voy a poner un chekbutton",
font = ("Arial", 14, "bold"), fg = "black", bg = "sky blue", padx=20, pady =10)
etiqueta1.pack()

var = tk.IntVar()
bcheck = tk.Checkbutton(ven1, text="Elegir opción", variable = var)
bcheck.pack(pady = 10)

boton1 = tk.Button(ven1,text = "Verificar estatus", command = estatus)
boton1.pack()



ven1.mainloop()