

def add_input_fn(attemps = 2):
    """
    Retona el valor de gasto ingresado por el usuario.
    """
    
    if attemps == 0:
        print("Demasiados intentos fallidos.")
        exit()

    mensaje = "Ingresar gasto"
    print(mensaje)
    print("=" * len(mensaje))
    print("\nIngrese el valor de un gasto")

    try:
        expense = float(input(">>>_ ").strip())
        return expense
    except ValueError:
        print("Por favor, ingrese un número.")
        add_input_fn(attemps -1)


def add_category_fn(read_json_fn, file_path, clean_interface_fn, time ,attemps = 2):
    """
    Muestra las categorías disponibles y permite al usuario escoger una.
    Retona la categoria escogida por el usuario.
    """

    if attemps == 0:
        print("Demasiados intentos fallidos.")
        exit()

    data = read_json_fn(file_path)

    # Dicionario para asociar el numero escogido con el valor de la categoria
    index_element = {}

    mensaje = "Escoge una categoría"

    # INTERFACE
    print("=" * len(mensaje))
    print(mensaje)
    print("=" * len(mensaje))

    for dictionary in data:
        for index, element in enumerate(dictionary):
            print(f"{index+1}- {element}")
            index_element[index+1] = element

    try:
        option = int(input(">>>_ ").strip())
        categoria = index_element[option]
        return categoria
    except (ValueError, KeyError):
        print("Por favor, ingrese un número válido.")
        clean_interface_fn(time)
        add_category_fn(read_json_fn, file_path, attemps - 1)

    
