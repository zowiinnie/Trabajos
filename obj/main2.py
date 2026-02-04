from atributos import *

per1 = Nombre("Bernarda", 18, "Ciencias de la compu")
per2 = Nombre("Mich", 18, "Ciencias de datos")
per3 = Nombre("Lupita", 18, "Ciencias de la compu")

print(str(per1))
print(repr(per2))
print(per1 + per2)
print(per2 * per3)
print(per1 == per2)
print(per1 == per3)