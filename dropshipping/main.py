# INTERFACES
from interfaces.interface_login import *
from interfaces.interface_options import *
from interfaces.interface_shipping import *
from interfaces.interface_confirm import *
# JSON
from json_controller.json_actions import *
# LOGINS
from login.create_account import *
# FEATURES
from features.clean_interface import *
from features.tracker_generator import *
from features.add_csv import *
# ACTIONS
from actions.cost_value import *
from actions.calculate_date import *

#PATHS
USER_DATA  = 'data/user_data.json'
CSV_DATA = 'data/csv_data.csv'

# CONSTANTES
COSTO_POR_KG = 2.5



if __name__ == '__main__':
    """
    csv -> user_name, addressee_details_list, peso, precio, fecha_envio, fecha_llegada
    """

    # INTERFACE LOGIN
    option = interface_login_fn(clean_interface_fn)
    if option == 1:
        user_name = login_account_fn(read_json_fn, USER_DATA, clean_interface_fn)
    elif option == 2:
        user_name = create_account_fn(read_json_fn, write_json_fn, USER_DATA, clean_interface_fn)
    else:
        exit()

    # INTERFACE OPTIONS
    clean_interface_fn(1.5)
    option = interface_options_fn()
    # Process 
    if option == 1:
        clean_interface_fn(1)
        print("Enviar paquete\n")
        # Obtener los datos del destinatario
        addressee_details_list = addressee_details_fn()
        """
        addressee_details_list = [name, last_name, city, country]
        """
        # Generar el tracker
        tracker_id = tracker_generator_fn()
        # Obtener el peso del paquete y los días de envío
        clean_interface_fn(1)
        weight, days = input_weight_fn()
        # Calcular el costo total
        total_cost = cost_value_fn(weight, COSTO_POR_KG)
        # Calcular la fecha de envío y llegada
        fecha_envio, fecha_llegada = calculate_date_fn(days)
        # INTERFACE CONFIRM
        clean_interface_fn(1)
        option = interface_confirm_fn(total_cost, fecha_envio, fecha_llegada)
        # Confirmar envío
        if option == 1:
            print("Paquete enviado")
            # Exportar a CSV
            create_csv_file(CSV_DATA)
            export_csv(user_name, addressee_details_list, weight, total_cost, fecha_envio, fecha_llegada, CSV_DATA)
        else:
            clean_interface_fn(2)
            print("Envío cancelado")
            exit()


    else:
        exit()

    

