# MODULES
import os
# INTERFACES
from interfaces.interface_input import *
from interfaces.interface_statistics import *

# FEATURES
from features.clean_interface import *

# JSON ACTION
from json_actions.json_actions import *

# ACTIONS
from actions.add_input import *
from actions.write_data import *
from actions.add_expense import *

# STATISTICS
from statistics.eda import *


# FILES PATH
DATA = "data/data.json"



def ingresar_gastos():
    clean_interface_fn(1)
    expense = add_input_fn()
    category = add_category_fn(read_json_fn, DATA, clean_interface_fn, 2)
    add_expense_fn(category, expense, read_json_fn, write_json_fn, DATA)
    clean_interface_fn(2)



if __name__ == '__main__':
    # Backend
    if os.path.exists(DATA):
        os.remove(DATA)
    create_categories_fn(read_json_fn, write_json_fn, DATA)
    clean_interface_fn(1)
    # ----------------------------------------------------------

    # Frontend
    total_income = interface_input_fn(clean_interface_fn, 2)
    ingresar_gastos()
    while True:
        print("¿Desea agregar otro gasto? (s/n)")
        option = input(">>>_ ").strip().lower()
        if option == "s":
            ingresar_gastos()
        elif option == "n":
            break
        else:
            print("\nOpción no válida.")
    # ----------------------------------------------------------

    # Calcular estadísticas
    result, total_income, total_expenses = general_evaluation(extract_data, total_income, read_json_fn, DATA)
    mean_list = mean_by_category(extract_data, read_json_fn, DATA)
    # Mostrar estadísticas en pantalla
    clean_interface_fn(2)
    interface_general_evaluation(result, total_income, total_expenses)
    print("\n")
    interface_means(mean_list)
    # Salida
    print("Gracias por usar el sistema de finanzas.")
    input("Presione enter para salir...")
    os.remove(DATA)
    exit()



    
    
