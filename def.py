import os
os.system("cls")

#Imprimir 2 saludos sin argumento y sin retorno 
def saludo():
    print("Hola estudiantes")
    print("Bienvenidos a funciones")
saludo()
saludo()

#Imprimir saludos personalizados con argumento y sin retorno
def saludo(nombre):
    print("Hola {}".format(nombre)) # 2 maneras de llamar un definicion
    print(f"Hola {nombre}")
    print("Bienvenido a funciones")
saludo("Andres")
saludo("Felipe")

#Funcion de restar, en caso de colocar un solo numero mandar mensaje y repetir, con argumento y con retorno
def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos numeros a la funcion")
        return
    return a - b

c = resta(10)
print("La resta es {}".format(c)) # 2 maneras de llamar un definicion
print(f"La resta es {c}")

#Funcion de restar, con argumento y con retorno
def resta(a, b):
    return a - b
c = resta(10, 6)
print("La resta es {}".format(c)) # 2 maneras de llamar un definicion
print(f"La resta es {c}")

#Funcion de restas, se invierten los numeros dados, con argumento y con retorno
c = resta(b = 10,a = 6)
print("La resta es {}".format(c)) # 2 maneras de llamar un definicion
print(f"La resta es {c}")

#Convertil fahrenheir o Kelvil a Celcius, con argumento y con retorno
def convertirCelcius(temperatura, unidad):
    if unidad == "f" or unidad == "F":
        c = (temperatura*9/5)+32
    elif unidad == "k" or unidad == "K":
        c = temperatura+273.15
    else:
        print("Unidad no valida k o f")
        return
    return c
    
c = convertirCelcius(30, "c")
print("Temperatura = ", c )
