

def interface_confirm_fn(total_cost, fecha_envio, fecha_llegada, attemps = 2):

    if attemps == 0:
        print("Demasiados intentos")
        exit()

    print("¿Desea confirmar el envío?")
    print("-" * len("¿Desea confirmar el envío?"))
    print(f"Costo total: ${total_cost}")
    print(f"Fecha de envío: {fecha_envio}")
    print(f"Fecha de llegada: {fecha_llegada}")
    print(f"-" * len("¿Desea confirmar el envío?"))
    print("\n1. Confirmar")
    print("2. Cancelar")

    try:
        option = int(input("Opción: ").strip())
        return option
    except:
        print("Error en el ingreso de datos")
        return interface_confirm_fn(total_cost, fecha_envio, fecha_llegada, attemps-1)