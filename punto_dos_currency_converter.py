# usando como referencia los valores desde USD a otras monedas
currency_types = {"CLP": 887.48, "ARS": 811.75, "USD": 1, "EUR": 0.91, "TRY": 29.85, "GBP": 0.79}


def change_currency():
    print(currency_types.keys())
    initial = input("Ingrese la moneda que quiere convertir: ")
    if initial in currency_types:
        print(currency_types.keys())
        exchange = input("Ingrese la moneda a la que quiere convertir: ")
        if exchange in currency_types:
            ammount = int(input("Ingrese el monto a convertir: "))
            return 1 / currency_types[initial] * currency_types[exchange] * ammount
        else:
            return "La moneda ingresada no es válida."
    else:
        return "La moneda ingresada no es válida."


def withdraw_funds(funds):
    # Este no lo entendí, creo
    withdraw_op = input("¿Desea retirar fondos?\nS: Si\nN: No")
    if withdraw_op in "Ss":
        print("Su saldo es", funds)
        ammount = int(input("Ingrese la cantidad de fondos a retirar: "))
        if ammount * 1.01 < funds:
            funds -= (ammount * 1.01)
            print("Operación exitosa\nSu nuevo saldo es", funds)
        else:
            print("El monto ingresado es superior a su sueldo + comisiones.")


def converter_manager():
    funds = 1000
    while True:
        print("Menú de Conversor de Monedas:\n"
              "1. Convertir monedas\n"
              "2. Retirar fondos\n"
              "0. Salir\n")
        op = int(input("Ingrese una opción: "))
        if op == 1:
            print(change_currency())

        elif op == 2:
            withdraw_funds(funds)

        elif op == 0:
            break

        else:
            print("La opción ingresada no es correcta.")