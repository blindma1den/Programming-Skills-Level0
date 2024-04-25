

def iu_user_fn(user_logged, read_json, track) -> int:
    data = read_json(track)
    #Para que sea actulice la información del usuario en pantalla
    for user in data:
        if user['user'] == user_logged['user']:
            user_logged = user
            break
    head = f"Bienvenido {user_logged['nombre']}"
    print(head)
    print("-" * len(head))
    print(f"Nombre: {user_logged['nombre']} {user_logged['apellido']}")
    print("-" * len(head))
    print(f"Saldo: {user_logged['saldo']}")
    print("-" * len(head))
    print("1. Depositar")
    print("2. Retirar")
    print("3. Transferir")
    print("4. Salir")

    option = int(input("Ingrese una opción: "))

    return option