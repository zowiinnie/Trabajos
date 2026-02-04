class persona():
    lista=[]

    def __init__(self, nombre, correo):
        self.nombre=nombre
        self.correo=correo

    def registrar(self):
        persona.lista.append(self)
        print(f"La persona {self.nombre} ha registrado con el correo {self.correo}")
    
    def actualizar_datos(self, nombre, correo):
       self.nombre=nombre
       self.correo=correo
       print(f"Los datos han sido actualizados")

    @classmethod
    def personas_registradas(cls):
        print ("Personas registradas")
        for Persona in cls.lista:
            print(f"-{Persona.nombre} - {Persona.correo}")