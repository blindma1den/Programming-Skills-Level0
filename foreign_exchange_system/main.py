# INTERFACE
from iu_user.interface import interface_iu_input, interface_iu_output, interface_iu_size_exchange, interface_completed, loading_fn, accepted_rate
# DATA
from data_exchanges.data import exchange_data_usd
# FUNCTIONS
from functions.exchange_functions import exchange_to_dollars

# IMPORTS
import platform
import time
import os
# Operating system
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


# MAIN
def doing():
    data = exchange_data_usd
    # Obtenemos el input del usuario
    input_user = interface_iu_input(data)
    # Actions
    time.sleep(1.5)
    os.system(delete)
    # Mostramos el output elimnando el input
    output_user = interface_iu_output(input_user, data)
    time.sleep(1)
    os.system(delete)
    # Obtenemos la cantidad a intercambiar
    size_exchange = interface_iu_size_exchange(input_user, output_user)
    time.sleep(1)
    os.system(delete)
    # Realizamos el intercambio e imprimos todo en pantalla
    exchange, rate, exchange_rate = exchange_to_dollars(input_user, output_user, size_exchange, data)
    interface_completed(input_user, output_user, size_exchange, exchange)
    time.sleep(3)
    accepted_rate(size_exchange, exchange, rate, exchange_rate, loading_fn, delete)
    time.sleep(1)



    


if __name__ == '__main__':
    doing()