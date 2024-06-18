import os
os.system("cls")

#Crear arreglo bus (10, 4)
bus = []
maxFilas = 10
maxColumnas = 4

for i in range(maxFilas):
    bus.append([10]*maxColumnas)

numeroAsiento = 1
for i in range(10):
    for j in range(4):
        bus[i][j] = numeroAsiento
        numeroAsiento += 1

for fila in bus:
    for asiento in fila:
        print(asiento, end=" ")
    print()