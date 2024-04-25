

def input_weight_fn(attemps=2):

    if attemps == 0:
        exit()

    print("Ingrese el peso del paquete")
    print("-> Peso máximo: 300kg")
    print("-" * len("Ingrese el peso del paquete"))

    try:
        weight = float(input("Peso: ").strip())
    except:
        print("Error en el ingreso de datos")
        return input_weight_fn(attemps-1)
    
    if weight <= 0:
        print("El peso debe ser mayor a 0")
        return input_weight_fn(attemps-1)
    elif weight <= 100: 
        dias = 2
        return weight, dias
    elif weight <= 100:
        dias = 4
        return weight, dias
    elif weight <= 200:
        dias = 7
        return weight, dias
    elif weight <= 300:
        dias = 15
        return weight, dias
    else:
        print("El peso no puede ser mayor a 300")
        return input_weight_fn(attemps-1)
    

def cost_value_fn(weight, cost):
    total_cost = weight * cost
    return total_cost
    

