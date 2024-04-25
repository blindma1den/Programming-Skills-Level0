

def add_new_user(nombre, apellido, dni, user, password, read_json_fn, write_json_fn, track):
    data = read_json_fn(track)
    new_id = 0 if len(data) == 0 else len(data)
    new_user = {
        "id": new_id,
        "user": user,
        "password": password,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "saldo": 0
    }
    data.append(new_user)
    write_json_fn(data, track)

   

    return data