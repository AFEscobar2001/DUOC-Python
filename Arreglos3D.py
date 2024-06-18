import os
os.system("cls")

#arreglo contador de misma palabra en matriz (3,2,3)
amarillo = 0
rojo = 0
naranja = 0
verde = 0
blanco = 0

matriz = [
[
    ["amarillo", "rojo", "naranja"],
    ["verde", "blanco", "verde"],
],
[
    ["blanco", "rojo", "blanco"],
    ["rojo", "amarillo", "verde"],
],
[
    ["amarillo", "blanco", "verde"],
    ["rojo", "naranja", "blanco"],
],
]

for capa in range(3):
    for fila in range(2):
        for elemento in range(3):
            if matriz[capa] [fila] [elemento] == "amarillo":
                amarillo += 1
            if matriz[capa] [fila] [elemento] == "rojo":
                rojo += 1
            if matriz[capa] [fila] [elemento] == "naranja":
                naranja += 1
            if matriz[capa] [fila] [elemento] == "verde":
                verde += 1
            if matriz[capa] [fila] [elemento] == "blanco":
                blanco += 1      
print(f"Número de elementos 'amarillo': {amarillo}")
print(f"Número de elementos 'rojo': {rojo}")
print(f"Número de elementos 'Naranja': {naranja}")
print(f"Número de elementos 'Verde': {verde}")
print(f"Número de elementos 'Blanco': {blanco}")                                                          