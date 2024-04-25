import platform
import os
import time

sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


def clean_interface_fn(time_size:int):
    time.sleep(time_size)
    os.system(delete)
