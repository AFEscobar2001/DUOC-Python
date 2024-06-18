import os
os.system("cls")

#Crear y borrar usuarios en diccionario
usuarios = {}

menu = 0

while menu == 0:
    print("\tMenu\n1) Inicio sesión\n2) Registrar usuario\n3) Eliminar usuario.\n4) Salir.")
    try:
        opcion = int(input("Ingrese una opcion\n"))
    except:
        print("Opcion no valida")
        menu = 0
    if opcion == 1:
        print("INICIO SESION")
        usuario = input("Ingrese usuario\n")
        contraseña = input("Ingrese contraseña\n")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("Inicio de sesion correcto")
        else:
            print("Usuario y/o Contraseña incorrecta")
        
    elif opcion == 2:
        print("REGISTRAR USUARIO\n")
        crearUsuario = input("Ingrese nuevo usuario\n")
        if crearUsuario in usuarios:
            print("Usuario ya existente")
            menu = 0
        else:
            crearContraseña = input("Ingrese nueva contraseña\n")
            usuarios[crearUsuario] = crearContraseña
            menu = 0
        
    elif opcion == 3:
        print("ELIMINAR USUARIO")
        borrarUsuario = input("Ingrese usuario a borrar\n")
        if borrarUsuario in usuarios:
            borrarContraseña = input("Ingrese contraseña\n")
            if usuarios[borrarUsuario] == borrarContraseña:
                del usuarios[borrarUsuario]
                print("Usuario borrado exitisamente")
            else:
                print("Contraseña incorrecta")
                menu = 0
        else:
            print("Usuario no registrado")
            menu = 0
    elif opcion == 4:
        print("ADIOS")
        print(usuarios)
        break
    else:
        print("Opcion no valida")
        menu = 0