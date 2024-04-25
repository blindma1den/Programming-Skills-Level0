


def addressee_details_fn():
    print("Ingrese los datos del destinatario")
    name = input("Nombre: ").strip().capitalize()
    last_name = input("Apellido: ").strip().capitalize()
    city = input("Ciudad: ").strip().capitalize()
    country = input("País: ").strip().capitalize()

    addressee_details_list = [name, last_name, city, country]

    return addressee_details_list