import time
import os

def login_interface(login_user:callable, register_user:callable, path_usuarios, read_json_fn, write_json_fn, delete):
    print("Bienvenido al sistema de matrícula")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    option = int(input("Opción: "))

    if option == 1:
        time.sleep(1.5)
        os.system(delete)
        user = login_user(path_usuarios, read_json_fn)
        return user
    elif option == 2:
        """
        Creamos el usuario, limpiamos la pantalla y pedimos que inicie sesión
        """
        register_user(path_usuarios, read_json_fn, write_json_fn, delete)
        time.sleep(3)
        os.system(delete)
        user = login_user(path_usuarios, read_json_fn)
    elif option == 3:
        print("Gracias por usar el sistema de matrícula")
        exit()
