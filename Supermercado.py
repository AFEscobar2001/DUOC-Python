import os
os.system("cls")

#Agregar a canasta productos y saber el valor
valorProducto = [0, 1800, 2000, 1500, 1300, 1000]
productos = ["", "takis", "doritos", "coca-cola", "pepsi", "trencito"]
maximo = len(valorProducto)
cantidad = 0
total = 0
cantidadProductos = [0, 0, 0, 0, 0, 0]


menu = 0
while menu == 0:
    print("\tMENU\n1)Agregar Productos\n2)Ver Canasta\n3)Ver Total\n4)Salir")
    try:
        opcion = int(input("Elija una opcion\n"))
    except:
        print("Opcion no valida")
        menu = 0
        
    if opcion == 1:
        print("Elija sus productos")
        print("\tMENU")
        for i in range(1,maximo):
            print(f"{i}. {productos[i]} ${valorProducto[i]} ")
        print(f"{maximo}. Salir")  
        try:
            opcionProducto = int(input("Seleccione el producto a agregar\n"))
        except:
            print("Opcion no valida")
            opcion = 1
        if opcionProducto < 1 or opcion > maximo :

            print(f"Opcion no valida, por favor seleccione del 1 al {maximo}")

        elif opcionProducto >= 1 and opcion <= maximo : 
            print(f"{productos[opcionProducto]} se agrego a la canasta")
            cantidadProductos[opcionProducto] = cantidadProductos[opcionProducto] + 1
            cantidad = cantidad + 1
            total = total + valorProducto[opcionProducto]
            print("Producto agregado")
    elif opcion == 2:
        for i in range(1,maximo):
            print(f"{i}. {productos[i]} {cantidadProductos[i]} ")
                
    elif opcion == 3:
        print(f"Total: {total}")
        
    elif opcion == 4:
        print("Adios")
        break
        
    else:
        print("Opcion no valida")
        menu = 0
            
            
              
        