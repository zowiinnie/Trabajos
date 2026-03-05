import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get() == 1:
        messagebox.showinfo("Opcion elegida", "Te gustan los esquites")

    elif var.get()== 2:
        messagebox.showinfo("Opción elegida", "Te gusta el pozole")

    elif var.get()== 3:
        messagebox.showinfo("Opcion elegida", "Te gustan los camarones empanizados")

    elif var.get()== 4:
        messagebox.showinfo("Opcion elegida", "Te gustan los chilaquiles")

    else:
        messagebox.showinfo("Opcion no elegida", "No selecciono nada")

ven2 = tk.Tk()
ven2.title("")
ven2.geometry("16090x500")

etiqueta1 = tk.Label(ven2, text = "¿Cual es ti comida favorita?")
etiqueta1.pack(pady = 20)

var = tk.IntVar()
rad1 = tk.Radiobutton(ven2, text = "Esquites", variable = var, value = 1)
rad1.pack()

rad2 = tk.Radiobutton(ven2, text = "Pozole", variable = var, value = 2)
rad2.pack()

rad3 = tk.Radiobutton(ven2, text = "Camarones empanizados", variable = var, value = 3)
rad3.pack()

rad4 = tk.Radiobutton(ven2, text = "Chlaquiles", variable = var, value = 4)
rad4.pack()

boton1=tk.Button(ven2,text="Verificar",command=opcion)
boton1.pack(pady=30)

ven2.mainloop()