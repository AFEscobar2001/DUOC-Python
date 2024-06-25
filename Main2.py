import os
os.system("cls")
from Funciones2 import *

#Suma
num1 = int(input("Ingrese un numero\n"))
num2 = int(input("Ingrese un numero\n"))
print(f"El resultado de {num1} + {num2} es: {suma(num1, num2)} ")

#Numero par o impar
resultado = esPar()
if resultado:
    print("El número es par.")
else:
    print("El número es impar.")
    
#Fahrenheit
temperaturaCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperaturaFahrenheit = celsiusFahrenheit(temperaturaCelsius)
print(f"La temperatura en grados Fahrenheit es: {temperaturaFahrenheit:.2f}")

#Numero mayor
num3 = float(input("Ingrese el primer número: "))
num4 = float(input("Ingrese el segundo número: "))
num5 = float(input("Ingrese el tercer número: "))

mayor = maxTres(num3, num4, num5)
print(f"El mayor de los tres números es: {mayor}")

#Validar no venga vacio
nombre_validado = validarNombre()
if nombre_validado:
    print(f"Nombre ingresado: {nombre_validado}")