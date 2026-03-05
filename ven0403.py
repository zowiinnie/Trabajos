import tkinter as tk
from tkinter import messagebox

# Funciones para manejar las acciones de los menús
def nuevo_archivo():
    messagebox.showinfo("Nuevo Archivo", "Has seleccionado 'Nuevo Archivo'.")

def abrir_archivo():
    messagebox.showinfo("Abrir Archivo", "Has seleccionado 'Abrir Archivo'.")

def guardar_archivo():
    messagebox.showinfo("Guardar Archivo", "Has seleccionado 'Guardar Archivo'.")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Este es un ejemplo de menú en Tkinter.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Menús")

# Crear la barra de menú
barra_menu = tk.Menu(root)

# Crear el menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear el menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

# Agregar los menús a la barra de menú
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la ventana principal para usar la barra de menú
root.config(menu=barra_menu)

# Iniciar el bucle principal de la ventana
root.mainloop()