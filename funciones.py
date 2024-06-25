import os, time
os.system("cls")

#1 funcion sin argumento y sin retorno
def saludar():
    print("Hola chic@s, cómo estan?")

#2 funcion con argumento y sin retorno
def saludarNombre(nombre):
    print(f"Hola {nombre}, que tengas un buen día!")
    
def multiplicar(a, b, c):
    resultado = a * b * c
    print(f"El producto de {a} x {b} x {c} es: {resultado}")
    
#3 funcion sin argumento y con retorno
def despedir():
    mensaje = "Chao chiquillos, buen finde!"
    return mensaje

#4 funcion con argumento y con retorno
def restar(a, b):
    resultado = a - b
    return resultado
