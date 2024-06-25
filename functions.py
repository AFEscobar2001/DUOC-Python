import time, os, random, csv
estudiantes = []


#funcion para obtener id (validamos que venga AB o AM)
def obtener_id():
    grado = input("ingrese grado academico 'basica o media'\n").lower()
    while grado not in ['basica', 'media']:
        grado = input("ingrese grado academico 'basica o media'\n").lower()
    if grado == 'basica':
        grado_corto = 'AB'
    else:
        grado_corto = 'AM'
    while True:
        try:
            id_alumno = int(input("ingrese id\n"))
            break
        except:
            print("opcion ingresada no es valida")
    #ya tengo AB O AM y tengo el id
    id_str = str(id_alumno)
    id_final = id_str+ "-" + grado_corto
    return id_final

def obtener_nombre():
    nombre = input("ingrese nombre completo de alumno\n")
    while len(nombre) < 5:
        nombre = input("ingrese nombre completo de alumno\n")
    return nombre

def obtener_edad():
    edad = int(input("ingrese edad de alumno\n"))
    while edad < 12 or edad > 18:
        edad = int(input("ingrese edad de alumno (12 a 18)\n"))
    return edad

def registrar_estudiante():
    while True:
        id_estudiante = obtener_id()
        nombre_estudiante = obtener_nombre()
        edad_estudiante = obtener_edad()
        estudiante = [id_estudiante, nombre_estudiante, edad_estudiante]
        estudiantes.append(estudiante)
        otro = input("desea agregar otro estudiante?   'si o no'\n").lower()
        if otro == 'si':
            continue
        else:
            break
        
def mostrar_estudiante():
    id_buscar = input("ingrese ID a buscar\n")
    for estudiante in estudiantes:
        if id_buscar == estudiante[0]:
            print(f"ID: {estudiante[0]}")
            print(f"NOMBRE: {estudiante[1]}")
            print(f"EDAD: {estudiante[2]}")
        else:
            print("segun nuestros registros, estudiante no existe")
        input("enter para continuar...")
        
def imprimir_certificados():
    id_buscar = input("ingrese ID a buscar\n")
    for estudiante in estudiantes:
        if id_buscar == estudiante[0]:
            asistencia = random.randint(0, 100)
            notas = random.randint(1, 7)
            if asistencia < 70 or notas < 5:
                conducta = 'estudiante malo'
            else:
                conducta = 'estudiante bueno'
            print(f"NOMBRE: {estudiante[1]}")
            print(f"NOTAS: {notas}")
            print(f"ASISTENCIA: {asistencia}")
            print(f"CONDUCTA: {conducta}")
        else:
            print("alumno no existe")
        input("enter para continuar...")
        
#funcion que entrá si o si en el examen        
def descargar_archivo():
    #crear un archivo csv (excel)
    with open('reportes_estudiantes.csv', mode='w', newline='') as file:
        #crear objeto tipo writer, recuerde importar csv
        writer = csv.writer(file)
        #crear cabecera del documento
        writer.writerow(["id_alumno", "nombre_alumno", "edad_alumno"])
        #pintar el documento con los datos obtenidos
        for estudiante in estudiantes:
            #pintar documento
            writer.writerow(estudiante)
            #mostrar por consola
            print(f"{estudiante[0]}  {estudiante[1]}  {estudiante[2]}")
        print("Reporte generado y guardado en 'reportes_estudiantes.csv'")
        #PODRAS IMPRIMIR ARCHIVO SOLO DE ALUMNOS BASICA??
        
def menu():
    print("1) Registrar Estudiante ")
    print("2) Buscar Estudiante")
    print("3) Imprimir Certificados")
    print("4) Descargar Archivo")
    print("5) Salir")
    