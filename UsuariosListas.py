
import os
os.system("cls")

#Crear y borrar usuarios en listas
usuarios = []

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
        for usser, passwd in usuarios:
            if usser == usuario and passwd == contraseña:
                print("Inicio de sesion correcto")    
            else:
                print("Usuario y/o Contraseña incorrecta")
        
    elif opcion == 2:
        print("REGISTRAR USUARIO\n")
        crearUsuario = input("Ingrese nuevo usuario\n")
        usuarioExiste = False
        for usser, _ in usuarios:
            if usser == crearUsuario:
                usuarioExiste = True
                break
        if usuarioExiste:
            print("Usuario ya existe")
        else:
            crearContraseña = input("Ingrese nueva contraseña\n")
            usuarios.append((crearUsuario, crearContraseña))

        
    elif opcion == 3:
        print("ELIMINAR USUARIO")
        borrarUsuario = input("Ingrese usuario a borrar\n")
        for usser, passwd in usuarios:
            if usser == borrarUsuario:
                borrarContraseña = input("Ingrese contraseña\n")
                if passwd == borrarContraseña:
                    usuarios.remove((borrarUsuario, borrarContraseña))
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