import os
os.system("cls")

#Suma
def suma(a, b):
    resultado = a + b
    return resultado

#Numero par o impar
def esPar():
    numero = int(input("Por favor, ingrese un número: "))
    if numero % 2 == 0:
        return True
    else:
        return False
    
#Fahrenheit
def celsiusFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Numero mayor
def maxTres(a, b, c):
    return max(a, b, c)

#Validar no venga vacio
def validarNombre():
    nombre = input("Ingrese su nombre: ").strip()
    if nombre:
        return nombre
    else:
        print("El nombre no puede estar vacío.")
        return None