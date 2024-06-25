import os
os.system("cls")

#Sacar promedio de 3 notas
def puntuacion(alumno1, alumno2, alumno3):
    suma = alumno1 + alumno2 + alumno3
    return suma / 3

media = puntuacion(7, 8, 9)
print("La puntuacion de esta clase es:", media)

media = puntuacion(6, 5, 7.5)
print("La puntuacion de esta clase es:", media)

#Sacar promedio de notas segun la lista
def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9]

media = puntuacion(clase)
print("La puntuacion de esta clase es:", media)

numero = 2
def mostrarLinea(num, linea):
    print(num, "x", linea, "=>", num*linea)

mostrarLinea(numero, 1)
mostrarLinea(numero, 2)
mostrarLinea(numero, 3)
mostrarLinea(numero, 4)
mostrarLinea(numero, 5)
mostrarLinea(numero, 6)
mostrarLinea(numero, 7)
mostrarLinea(numero, 8)
mostrarLinea(numero, 9)
mostrarLinea(numero, 10)