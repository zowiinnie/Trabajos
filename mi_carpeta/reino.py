import tkinter as tk
from PIL import Image, ImageTk 

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("600x300")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Reino Animal",bg="lightblue",font=("Arial",23,"bold"))
    eti1.pack()
    frame1= tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("C:/Users/Rorsc/Downloads/reino/reino.jpg")
    imagen = imagen.resize((400, 200))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2,text="Elefante",variable=var,value=1)
    ele.pack()
    jirafa=tk.Radiobutton(frame2,text="Jirafa",variable=var,value=2)
    jirafa.pack()
    castor=tk.Radiobutton(frame2,text="Pez Beta",variable=var,value=3)
    castor.pack()
    leon=tk.Radiobutton(frame2,text="León",variable=var,value=4)
    leon.pack()

    def informacion():
        seleccion=var.get()
        if seleccion==1:
            ventana_elefante()
        elif seleccion==2:
            ventana_jirafa()
        elif seleccion==3:
            ventana_pez_beta()
        elif seleccion==4:
            ventana_leon()

    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() 
    ventana_principal()  

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("500x500")
    ven2.config(bg="gray")

    eti2 = tk.Label (ven2, text = "Elefante", bg = "gray", font = ("Algerian", 24, "bold"))
    eti2.pack(pady = 10)

    frame3=tk.Frame()
    frame3.pack(pady = 20)

    imagen2 = Image.open("C:/Users/Rorsc/Downloads/reino/elefante.jpg")
    imagen2 = imagen2.resize((400, 200))  
    imagen_tk2 = ImageTk.PhotoImage(imagen2) 
    label_imagen = tk.Label(frame3, image=imagen_tk2)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    eti2=tk.Label(ven2,text="Info",bg="gray",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)
    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() 
    ventana_principal()  

def ventana_jirafa():
    global ven3
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Información de Jirafa")
    ven3.geometry("500x500")
    ven3.config(bg="gray")

    eti3 = tk.Label (ven3, text = "Jirafa", bg = "light blue", font = ("Algerian", 24, "bold"))
    eti3.pack(pady = 10)

    frame4=tk.Frame()
    frame4.pack(pady = 20)

    imagen3 = Image.open("C:/Users/Rorsc/Downloads/reino/jirafa.jpg")
    imagen3 = imagen3.resize((400, 200))  
    imagen_tk3 = ImageTk.PhotoImage(imagen3) 
    label_imagen = tk.Label(frame4, image=imagen_tk3)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    boton3=tk.Button(ven3,text="ir a ventana principal",command=lambda: regresar_a_primera(ven3))
    boton3.pack(pady=30)

    ven3.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() 
    ventana_principal()  

def ventana_pez_beta():
    global ven4
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Información de Pez Beta")
    ven4.geometry("500x500")
    ven4.config(bg="gray")

    eti4 = tk.Label (ven4, text = "Pez Beta", bg = "light blue", font = ("Algerian", 24, "bold"))
    eti4.pack(pady = 10)

    frame5=tk.Frame()
    frame5.pack(pady = 20)

    imagen4 = Image.open("C:/Users/Rorsc/Downloads/reino/pez beta.jpg")
    imagen4 = imagen4.resize((400, 200))  
    imagen_tk4 = ImageTk.PhotoImage(imagen4) 
    label_imagen = tk.Label(frame5, image=imagen_tk4)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    boton4=tk.Button(ven4,text="ir a ventana principal",command=lambda: regresar_a_primera(ven4))
    boton4.pack(pady=30)

    ven4.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() 
    ventana_principal()  

def ventana_leon():
    global ven5
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Información de Leon")
    ven5.geometry("500x500")
    ven5.config(bg="gray")

    eti5 = tk.Label (ven5, text = "Leon", bg = "light blue", font = ("Algerian", 24, "bold"))
    eti5.pack(pady = 10)

    frame6=tk.Frame()
    frame6.pack(pady = 20)

    imagen5 = Image.open("C:/Users/Rorsc/Downloads/reino/leon.jpg")
    imagen5 = imagen5.resize((400, 200))  
    imagen_tk5 = ImageTk.PhotoImage(imagen5) 
    label_imagen = tk.Label(frame6, image=imagen_tk5)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    boton5=tk.Button(ven5,text="ir a ventana principal",command=lambda: regresar_a_primera(ven5))
    boton5.pack(pady=30)

    ven5.mainloop()


ventana_principal()