import time
import os
import platform

sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


def register_new_user():
    print("Registro de usuario")
    print("-" * len("Registro de usuario"))
    print("Cargando...")
    time.sleep(2)
    os.system(delete)
    nombre = input("Ingrese su nombre: ")
    time.sleep(1)
    os.system(delete)
    apellido = input("Ingrese su apellido: ")
    time.sleep(1)
    os.system(delete)
    dni = int(input("Ingrese su DNI: "))
    time.sleep(1)
    os.system(delete)
    password = input("Ingrese su contraseña: ")
    time.sleep(1)
    os.system(delete)
    
    while True:
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"DNI: {dni}")
        print(f"Contraseña: {password}")
        print("-" * len("Registro de usuario"))
        print("¿Están correctos los datos?")
        print("1. Sí")
        print("2. No")
        option = int(input("Ingrese una opción: "))
        if option == 1:
            print("Usuario registrado con éxito")
            break
        elif option == 2:
            print("Usuario no registrado")
            time.sleep(1)
            os.system(delete)
            register_new_user()
            break # si no pongo break, al ejecutar la opcion 2 y luego la opcion 1 se vuelve a ejecutar el while
        else:
            print("Opción incorrecta")
            time.sleep(1)
            os.system(delete)

    user = nombre[:2] + apellido[:2] + str(dni)[-3:]

    print(f"\nTu usuario es: {user}\n")
    time.sleep(5)

    return (nombre, apellido, dni, user, password)