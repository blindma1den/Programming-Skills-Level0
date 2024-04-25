import os

def login_user_fn(path, read_json_fn, attemps=3):

    if attemps == 0:
        print("Has excedido el número de intentos")
        return False

    data = read_json_fn(path)

    user_input = input("Ingrese su usuario: ").strip().lower()
    password = input("Ingrese su contraseña: ").strip().lower()

    for user in data:
        if user['user'] == user_input and user['password'] == password:
            return user_input
    
    attemps -= 1
    print(f"Usuario o contraseña incorrectos. Intentos restantes: {attemps}")
    login_user_fn(path, read_json_fn, attemps)


    

def register_user_fn(path, read_json_fn, write_json_fn, delete, attemps=3):

    if attemps == 0:
        print("Has excedido el número de intentos")
        return False

    data = read_json_fn(path)

    print(f"Registro de usuario          //[attemps: {attemps}]")
    user = input("Ingrese su usuario: ").strip().lower()
    password = input("Ingrese su contraseña: ").strip().lower()

    os.system(delete)

    print("Verificar los datos: ")
    print(f"Usuario: {user}")
    print(f"Contraseña: {password}")
    print("-" * 20)
    print("1. Confirmar")
    print("2. Registrar de nuevo")

    option = int(input("Opción: "))
    if option == 1:
        data.append({"user": user, "password": password, "programa": "", "ciudad": "", "estatus_matricula": False})
        write_json_fn(data, path)
        return True
    else:
        attemps -= 1
        register_user_fn(path, read_json_fn, write_json_fn, delete, attemps)

    