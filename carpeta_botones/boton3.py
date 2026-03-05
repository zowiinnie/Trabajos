import tkinter as tk
from tkinter import messagebox

def opcion():
    if var2.get()== 1:
        messagebox.showinfo("Vnetana de información", "Información de ususario")

    elif var2.get() == 2:
        messagebox.showinfo("Vnentana de advertencias", "Esto es una alerta")
    
    elif var2.get() == 3:
           messagebox.showinfo("Ventana de error", "Has cometido un error")

    elif var2.get() == 4:
           respuesta = messagebox.askyesno("Ventana de opcion", "Te gusta la clase")
           if respuesta:
                respuesta = messagebox.showinfo("Ventana de respuesta", "Te gusta la clase")
           else:
                respuesta = messagebox.showinfo("Ventana de respuesta", "No te gusta eta clase")

    elif var2.get()==5:
         respuesta = messagebox.askokcancel("Ventana de respuesta", "Eres bueno en esto?")
         if respuesta:
                respuesta = messagebox.showinfo("Ventana de respuesta", "Si claro")
         else:
                respuesta = messagebox.showinfo("No elegiste ninguna respuesta")
         


ven3 = tk.Tk()
ven3.title()
ven3.geometry("16090x500")
ven3.config(bg = "sky blue")

etiqueta1 = tk.Label(ven3, text = "Tipos de messagebox")
etiqueta1.pack(pady = 20)

var2 = tk.IntVar()
mes1 = tk.Radiobutton(ven3, text = "Mostrar información", variable = var2, value = 1)
mes1.pack()

mes2 = tk.Radiobutton(ven3, text = "Advertencia", variable = var2, value = 2)
mes2.pack()

mes3 = tk.Radiobutton(ven3, text = "Error", variable = var2, value = 3)
mes3.pack()

mes4 = tk.Radiobutton(ven3, text = "Preguntar si o no", variable = var2, value = 4)
mes1.pack()

mes4 = tk.Radiobutton(ven3, text = "Preguntar aceptar o cancelar", variable = var2, value = 5)
mes4.pack()

boton1=tk.Button(ven3,text="Verificar",command=opcion)
boton1.pack(pady=30)

ven3.mainloop()