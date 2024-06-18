import os
os.system("cls")

#Ingresar nombres y imprimir el de mayor caracteres
"""
nom1 = input("Ingrese un nombre\n")
nom2 = input("Ingrese un nombre\n")
nom3 = input("Ingrese un nombre\n")

nombres = [nom1, nom2, nom3]

nombreMaslargo = ""
nombreCaracter = 0

for caracter in nombres:
    if len(caracter) > nombreCaracter:
        nombreMaslargo = caracter
        nombreCaracter = len(caracter)
        
print(nombreMaslargo)
"""

"""
nombres = ["Lina", "David", "Andres"]
apellidos = ["Escobar", "Velez", "Gomez"]

print(f"Sin ordenar: {nombres}\n\t     {apellidos}")

nombres.sort()
apellidos.sort()

print(f"Ordenado: {nombres}\n\t  {apellidos}")
"""

#Agregar nombres y  borrar el de menor caracteres
"""
nombres = []

nombre = 0
while nombre == 0:
    agregar = input("Ingrese un nombre\n")
    nombres.append(agregar)
    repetir = input("¿Desea agregar otro nombre?\n")
    if repetir.lower() == "no":
        print(f"Nombres mas corto sin eliminar: {nombres}")
        break
    elif repetir.lower() == "si":
        nombre = 0
    else:
        print("Debe responder si o no")
        
if nombres:
    nombreCorto = min(nombres, key=len)
    nombres.remove(nombreCorto)
        
        
print(f"Nombres mas corto eliminado: {nombres}")
"""
