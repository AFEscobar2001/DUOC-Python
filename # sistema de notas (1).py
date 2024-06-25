# sistema de notas

# para una asignatura

# ingresar un nombre valido ( no vacio, ni espacios en blanco y que este repetido )

# solicitar la cantidad de notas ( 1, 2, 3 o 4 notas parciales 

# se pide leer el nombre de un alumno

# se debe validar que no se ingrese vacío o solamente espacios en blanco

# se debe validar que no esté repetido 

# ingresar cada una de estas notas ( valor válido es decimal entre 1.0 y 7.0 )

# calcular el promedio de las notas ingresadas (redondear a 1 decimal )

# determinar si el alumno aprueba (promedio >= 4.0) o reprueba la asignatura

# si el usuario desea continuar , volver a leer datos de otro alumno 

# al terminar guardar en un archivo CSV los datos ingresados , 

# como si fuera una planilla, ejemplo :

# nombre,parcial1,parcial2,parcial3,promedio,situacion

# juan,2.8,4.5,6.7,4.7,aprobado

# eugenia,6.8,5.5,6.7,5.7,aprobado

# ... etc ...
import os
os.system("cls")
import csv

encabezado = ["Alumno","nota1","nota2","nota3","promedio","sitiacion"]
alumno = []

menu = 0
while menu == 0:
    try:
        nombre = input("Ingrese nombre\n")
    except:
        menu = 0
        


# sistema de notas



# para una asignatura

# ingresar un nombre valido ( no vacio, ni espacios en blanco )



asignatura=['programacion','matematicas','lenguaje','cloud','innovacion']

while True :

    nombre_asignatura = input("ingrese nombre de la asignatura : ")

    validacion = nombre_asignatura.replace(" ","")

    if len(validacion) == 0 :

        print("no es un nombre válido ")

    else :

        if nombre_asignatura.lower() not in asignatura :

            print("no es un nombre válido ")

        else :

            break



print(nombre_asignatura)



# solicitar la cantidad de notas ( 1, 2, 3 o 4 notas parciales )



cantidad_de_notas = 0





while True : 

    try: 

        cantidad_de_notas = int( input("ingrese cantidad de notas de la asignatura : ") )

    except :

        cantidad_de_notas = 0

    

    if cantidad_de_notas < 1 or cantidad_de_notas > 4 :

        print("la cantidad de notas ingresadas no es válida ")

    else :

        break



# leer muchas veces, porque tengo muchos alumnos



matriz_alumno=[]



alumnos=[]



while True :



    # se pide leer el nombre de un alumno

    # se debe validar que no se ingrese vacío o solamente espacios en blanco

    # se debe validar que no esté repetido 



    while True :

        nombre_alumno = input("ingrese nombre del alumno : ")

        validacion = nombre_alumno.replace(" ","")

        if len(validacion) == 0 :

            print("no es un nombre válido ")

        else :

            if nombre_alumno.lower() in alumnos :

                print("el alumno ya existe")

            else :

                break



    print(nombre_alumno)

    alumnos.append(nombre_alumno)



    # ingresar cada una de estas notas ( valor válido es decimal entre 1.0 y 7.0 )

    lista_de_notas=[]



    for x in range(cantidad_de_notas) :

        nota = 0.0

        while True : 

            try: 

                nota = int( input(f"ingrese la nota de la prueba parcial: {1+x}") )

            except :

                notas = 0.0

            

            if nota < 1.0 or nota > 7.0 :

                print("la nota ingresada no es válida ")

            else :

                break

        lista_de_notas.append(nota)

    

# calcular el promedio de las notas ingresadas (redondear a 1 decimal )

# determinar si el alumno aprueba (promedio >= 4.0) o reprueba la asignatura

    

    promedio = round ( sum(lista_de_notas) / cantidad_de_notas, 1 )



    if promedio >= 4 :

        situacion = 'aprobado'

    else :

        situacion = 'reprobado'





    nuevo = ( nombre_alumno, lista_de_notas, promedio, situacion)

    

    matriz_alumno.append(nuevo)



# si el usuario desea continuar , volver a leer datos de otro alumno 



    continuar = input("desea ingresar otro alumno si/no").lower()



    if continuar != 'si' :

        break

#





# al terminar guardar en un archivo CSV los datos ingresados , 

# como si fuera una planilla, ejemplo :



# nombre,parcial1,parcial2,parcial3,promedio,situacion

# juan,2.8,4.5,6.7,4.7,aprobado

# eugenia,6.8,5.5,6.7,5.7,aprobado