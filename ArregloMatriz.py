import os
os.system("cls")

#Arreglo ir agregando numeros a matriz
filas = 3
columnas = 4

matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for fi in range(filas):
    for co in range(columnas):
        matriz[fi][co] = int(input(f"Elemento [{fi}][{co}]: "))
        
for fi in range(filas):
    for co in range(columnas):
        print(f"{matriz[fi][co]:}", end=" ")
    print()