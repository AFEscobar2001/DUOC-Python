import os, time
os.system("cls")

pikaRoll = 4500
otakuRoll = 5000
pulpoRoll = 5200
anguilaRoll = 4800

cantRoll1 = 0
cantRoll2 = 0
cantRoll3 = 0
cantRoll4 = 0

descuento = 0.1
subTotal = 0
descuentoxcodigo = 0
totalProductos = 0
total = 0

pedido = 1
while pedido == 1:
    print("\tBienvedido al sushi Otaku\nMenu\n1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800\n5. Salir")
    try:
        sushi = int(input("Elija una opcion\n"))
    except:
        print("Opcion no valida")
        sushi = 0
    if sushi == 1:
        print("Pikachu Roll ha sido agregado al carrito")
        cantRoll1 = cantRoll1 + 1
        subTotal = subTotal + 1
        totalProductos = totalProductos + 1
        print(f"Subtotal{subTotal}")

    elif sushi == 2:
        print("Otaku Roll ha sido agregado al carrito")
        cantRoll2 = cantRoll2 + 1
        subTotal = subTotal + 1
        totalProductos = totalProductos + 1
        print(f"Subtotal{subTotal}")  

    elif sushi == 3:
        print("Pulpo Venenoso Roll ha sido agregado al carrito")
        cantRoll3 = cantRoll3 + 1
        subTotal = subTotal + 1
        totalProductos = totalProductos + 1
        print(f"Subtotal{subTotal}")    

    elif sushi == 4:
        print("Anguila Eléctrica Roll ha sido agregado al carrito")
        cantRoll4 = cantRoll4 + 1
        subTotal = subTotal + 1
        totalProductos = totalProductos + 1
        print(f"Subtotal{subTotal}")       

    elif sushi == 5:
        try:
            opcionDes = input("Ingrese codigo de descuento\n")
        except:
            print("Opcion no valida")
            sushi = 5
        if opcionDes == "soyotaku":
            descuentoxcodigo = subTotal * descuento
            total = subTotal - descuentoxcodigo

        else:
            descuentoxcodigo = 0

        print("************************")
        print(f"Total productos {total}")
        print("************************")
        print(f"Pikachu Roll {cantRoll1}")
        print(f"Otaku Roll {cantRoll2}")
        print(f"Pulpo Venenoso Roll {cantRoll3}")
        print(f"Anguila Eléctrica Roll {cantRoll4}")
        print("************************")
        print(f"Subtotal {subTotal}")
        print(f"Descuento {descuentoxcodigo}")
        print(f"Total {total}")

        try:
            otroPedido = int(input("¿Desea realizar otro pedido? 1. Si 2. No\n"))
        except:
            otroPedido = int(input("Opcion no valida debe ser 1 o 2\n"))
        if otroPedido == 1:
            pedido = 1
        elif otroPedido == 2:
            print("Adios")
            break
        else:
            otroPedido = int(input("Opcion no valida debe ser 1 o 2\n"))

    else:
        print("Elija una opcion valida")
        pedido = 1      

