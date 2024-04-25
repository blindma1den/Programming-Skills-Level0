import os
import time


def login_user_fn(read_json_fn, track, delete, attemps= 0):
    if attemps == 3:
        print("Demasiados intentos fallidos")
        return (False, None)
    data = read_json_fn(track)
    print("-" * 20)
    user = input("Ingrese su usuario: ").strip()
    password = input("Ingrese su contraseña: ").strip()
    for user_data in data:
        if user_data["user"] == user and user_data["password"] == password:
            print("Bienvenido")
            return (True, user_data)
    
    print("Usuario o contraseña incorrectos")
    print(f"Intentos {attemps}")
    attemps += 1
    time.sleep(1)
    os.system(delete)
    return login_user_fn(read_json_fn, track, delete, attemps=attemps)