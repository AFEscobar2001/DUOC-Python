import os
os.system("cls")
from funciones import saludar, saludarNombre, multiplicar, despedir, restar
#from funciones import * con caracter "*" se traen todas la funciones sin tener que llamarlas una por una

print("**************************")
saludar()
nom = input("Ingrese nombre\n").lower()
saludarNombre(nom)

print("**************************")
num1 = int(input("Ingrese un numero\n"))
num2 = int(input("Ingrese un numero\n"))
num3 = int(input("Ingrese un numero\n"))
multiplicar(num1, num2, num3)

print("**************************")
print(f"forma 1: {despedir()}") #llamar funcion y imprimirla

despedir = despedir()
print(f"forma 2: {despedir}") #definir funcion y imprimirla

print("**************************")
num4 = int(input("Ingrese numero\n"))
num5 = int(input("Ingrese numero\n"))
if restar(num4, num5)%2 == 0:
    print(f"El numero es par ({restar(num4, num5)})")
else:
    print(f"El numero es impar ({restar(num4, num5)})")

