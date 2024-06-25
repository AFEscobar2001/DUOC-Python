def ingresar_nombre(alumnos):
    while True:
        nombre = input("Ingrese el nombre del alumno: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío o contener solo espacios en blanco.")
        elif nombre in alumnos:
            print("El nombre ya está en la lista de alumnos.")
        else:
            return nombre

def ingresar_notas():
    while True:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de notas (1, 2, 3 o 4): "))
            if cantidad_notas not in [1, 2, 3, 4]:
                print("Debe ingresar un número entre 1 y 4.")
                continue
            notas = []
            for i in range(cantidad_notas):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i + 1} (valor entre 1.0 y 7.0): "))
                        if 1.0 <= nota <= 7.0:
                            notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 1.0 y 7.0.")
                    except ValueError:
                        print("Debe ingresar un valor decimal.")
            return notas
        except ValueError:
            print("Debe ingresar un número válido.")

def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 1)

def determinar_estado(promedio):
    return "aprueba" if promedio >= 4.0 else "reprueba"

def sistema_notas():
    alumnos = {}
    while True:
        nombre = ingresar_nombre(alumnos)
        notas = ingresar_notas()
        promedio = calcular_promedio(notas)
        estado = determinar_estado(promedio)
        alumnos[nombre] = {
            "notas": notas,
            "promedio": promedio,
            "estado": estado
        }
        print(f"El alumno {nombre} {estado} la asignatura con un promedio de {promedio}.")

        continuar = input("¿Desea ingresar datos de otro alumno? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nResumen de alumnos:")
    for nombre, datos in alumnos.items():
        print(f"Alumno: {nombre}, Notas: {datos['notas']}, Promedio: {datos['promedio']}, Estado: {datos['estado']}")

if __name__ == "__main__":
    sistema_notas()