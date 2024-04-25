
def interface_options_fn():
    """
    Interface donde estarán las opciones principales del programa.
    Una vez logeada la cuenta
    """
    mensaje_bienvenida = "Bienvenido al sistema de envíos de paquetes"

    print("-" * len(mensaje_bienvenida))
    print(mensaje_bienvenida)
    print("-" * len(mensaje_bienvenida))
    print("\n1. Enviar paquete")
    print("2. Salir\n")

    try:
        option = int(input("Ingrese una opción: "))
        if option < 1 or option > 2:
            print("⚠️ Opción inválida\n")
            exit()
    except ValueError:
        print("⚠️ Opción inválida\n")
        exit()

    return option
