# Imports
import os
import time

# Json actions
from controller_json.json_actions import *
# Interface
from interface.escoger_programas_iu import *
from interface.login_interface import *
# Login
from login.login_user import *


# Constante de la ruta del archivo de datos
DATA_PROGRAMAS = "data/university_data.json"
DATA_USER = "data/users_data.json"

# Reconocer el sistema operativo
import platform
sistema_operativo = platform.system()
if sistema_operativo == "Windows":
    delete = "cls"
else: # Linux
    delete = "clear"

def time_out(seconds:int, delete=delete):
    time.sleep(seconds)
    os.system(delete)


if __name__ == '__main__':
    usuario_logeado = login_interface(login_user_fn, register_user_fn, DATA_USER, read_json_fn, write_json_fn, delete)
    time_out(1.5)
    programa_escogido = escoger_programas(DATA_PROGRAMAS, read_json_fn)
    time_out(1.5)
    ciudad_escogida = escoger_ciudad(DATA_PROGRAMAS, read_json_fn)
    time_out(1.5)

    analizar_opciones(usuario_logeado, programa_escogido, ciudad_escogida, DATA_PROGRAMAS, DATA_USER, read_json_fn, write_json_fn, escoger_ciudad, delete)

    

    
    