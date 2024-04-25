
# IU 
from iu.welcome import print_welcome
from iu.iu_user import iu_user_fn
# LOGIN
from login.register import register_new_user
from login.add_user_to_data import add_new_user
from login.login_user import login_user_fn
# ACTIONS
from actions.user_actions import depositar, retirar, transferir, repeat
# JSON
from controller_json.read_json import read_json_fn
from controller_json.write_json import write_json_fn

# import json
import time
import os
import platform
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"



def doing():
    track = "users/all_users.json"
    opcion_de_usuario = print_welcome()

    # INGRESAR AL SISTEMA 
    if opcion_de_usuario == 1:
        status, user_logged = login_user_fn(read_json_fn, track, delete)
        time.sleep(1.5)
        os.system(delete)
        first_time = 0
        if status:
            while True:
                if first_time > 0:
                    os.system(delete)
                
                option_user = iu_user_fn(user_logged, read_json_fn, track)
                time.sleep(1.5)
                os.system(delete)
                if option_user == 1:
                    depositar(user_logged, read_json_fn, write_json_fn, track)
                elif option_user == 2:
                    retirar(user_logged, read_json_fn, write_json_fn, track)
                elif option_user == 3:
                    transferir(user_logged, read_json_fn, write_json_fn, track)
                elif option_user == 4:
                    print("Adiós, vuelva otro día")
                    break

                time.sleep(1.5)
                os.system(delete)
                
                if repeat() == None:
                    time.sleep(1.5)
                    os.system(delete)
                    break
                else:
                    time.sleep(1.5)
                    print("\nContinuando...\n")
                    os.system(delete)
                    continue
                

                first_time += 1
  
            

        else:
            print("Adiós, vuelva otro día")

    # REGISTRAR USUARIO NUEVO 
    elif opcion_de_usuario == 2:
        nombre, apellido, dni, user, password = register_new_user()
        add_new_user(nombre, apellido, dni, user, password, read_json_fn, write_json_fn, track)
        time.sleep(1.5)
        os.system(delete)
        doing()


if __name__ == '__main__':
    doing()