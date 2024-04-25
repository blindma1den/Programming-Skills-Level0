
def extract_data(read_json_fn, file_path):
    data = read_json_fn(file_path)

    gastos_medicos = data[0]["Gasto medicos"]
    gasto_hogar = data[0]["Gasto del hogar"]
    ocio = data[0]["Ocio"]
    ahorro = data[0]["Ahorro"]
    educacion = data[0]["Educacion"]
    otros = data[0]["Otros"]

    data_list = [gastos_medicos, gasto_hogar, ocio, ahorro, educacion, otros]

    return data_list

def general_evaluation(extract_data, total_income, read_json_fn, DATA):
    data_list = extract_data(read_json_fn, DATA)
    total_expenses = 0
    for category in data_list:
        total_expenses += sum(category)

    if total_income == total_expenses:
        result =  "Los gastos son iguales a los ingresos."
        return (result, total_income, total_expenses)
    elif total_income > total_expenses:
        result =  "Los gastos son menores a los ingresos."
        return (result, total_income, total_expenses)
    else:
        result =  "Los gastos son mayores a los ingresos."
        return (result, total_income, total_expenses)




def mean_by_category(extract_data, read_json_fn, DATA):
    data_list = extract_data(read_json_fn, DATA)

    mean_gatos_medicos = sum(data_list[0]) / len(data_list[0]) if len(data_list[0]) > 0 else 0
    mean_gasto_hogar = sum(data_list[1]) / len(data_list[1]) if len(data_list[1]) > 0 else 0
    mean_ocio = sum(data_list[2]) / len(data_list[2]) if len(data_list[2]) > 0 else 0
    mean_ahorro = sum(data_list[3]) / len(data_list[3]) if len(data_list[3]) > 0 else 0
    mean_educacion = sum(data_list[4]) / len(data_list[4]) if len(data_list[4]) > 0 else 0
    mean_otros = sum(data_list[5]) / len(data_list[5]) if len(data_list[5]) > 0 else 0

    mean_list = [mean_gatos_medicos, mean_gasto_hogar, mean_ocio, mean_ahorro, mean_educacion, mean_otros]

    return mean_list
