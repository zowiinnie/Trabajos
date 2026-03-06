import csv
import os

class Usuario():

    lista=[]
    ruta_cvs = r"C:/Users/DELL/Documents/hola/registro/personas.csv"
    def __init__(self, name, age, food):
        self.nombre = name
        self.edad = age
        self.comida = food
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} y le gusta {self.comida}"
    
    @classmethod #Método de clase
    def mostrar_lista(cls):
        for u in Usuario.lista:
            print(u.mostrar_datos())
        
    @classmethod
    def guardar_usuarios(cls):
        campos=["nombre","edad","comida"]  #Nombres de las columnas en la tabla

        # Crear el directorio si no existe
        directorio = os.path.dirname(cls.ruta_cvs)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"Directorio creado: {directorio}")
            except Exception as e:
                print(f"Error al crear directorio: {e}")
                return False

        #Guardar el archivo
        with open(cls.ruta_cvs, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=campos, delimiter=",")
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"comida":u.comida})