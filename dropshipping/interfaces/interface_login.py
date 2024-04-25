
def interface_login_fn(clean_interface_fn, attemps = 3):

    if attemps == 0:
        print("Demasiados intentos fallidos")
        exit()

    clean_interface_fn(1)
    print("Bienvenidos al registro de envíos de paquetes")
    print("-" * len("Bienvenidos al registro de envíos de paquetes") + "    👉 Intentos: " + str(attemps))
    print("Por favor, ingrese su usuario y contraseña")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir\n")

    try:
        option = int(input("Ingrese una opción: "))
        if option < 1 or option > 3:
            clean_interface_fn(.8)
            print("⚠️ Ingrese una opción válida\n")
            clean_interface_fn(2)
            interface_login_fn(clean_interface_fn, attemps-1)
    except ValueError:
        clean_interface_fn(.8)
        print("⚠️ Ingrese un número válido\n")
        clean_interface_fn(2)
        return interface_login_fn(clean_interface_fn, attemps-1)

    return option


