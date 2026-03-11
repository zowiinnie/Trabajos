from backend import *

usuario1 = Usuario("Gabs", 18, "Enchiladas suizas")
usuario2 = Usuario("Sugs", 19, "Espagueti verde")
usuario3 = Usuario("Zoe", 18, "Huevo con jamón")

print(usuario1.mostrar_datos())
print(usuario2.mostrar_datos())
print(usuario3.mostrar_datos())

Usuario.mostrar_lista()