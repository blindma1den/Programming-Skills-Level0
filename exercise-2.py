# Establecer tasas de conversion
rates = {
    "CLP": 0.0013,
    "ARS": 0.010,
    "USD": 1.000,
    "EUR": 1.130,
    "TRY": 0.120,
    "GBP": 1.370,
}

# Menu principal
def menu():
    while True:
        print("Bienvenido a Tu Convertidor")
        print("Monedas disponibles:")
        currencies = ["CLP", "ARS", "USD", "EUR", "TRY", "GBP"]
        for i, currency in enumerate(currencies):
            print(f"{i+1}. {currency}")

        initial_currency = input("Selecciona una moneda inicial: ")
        if initial_currency not in ["1", "2", "3", "4", "5", "6"]:
            print("Opcion invalida, Intenta de nuevo")
            continue
        
        for i, currency in enumerate(currencies):
            print(f"{i+1}. {currency}")
    
        final_currency = input("Selecciona la moneda destino: ")
        if final_currency not in ["1", "2", "3", "4", "5", "6"]:
            print("Opcion invalida, Intenta de nuevo")
            continue
        
        amount = float(input("Por favor, introducir monto a convertir: "))
        #monto minimo y maximo
        if amount < 10 or amount > 100:
            print("Lo siento, el monto debe ser entre 10 y 100, Por favor, intenta de nuevo")
            continue

        #Funcion de conversion
        def convert_currency(amount, initial_currency, final_currency, withdraw):
            
            exchange_rate = rates[final_currency] / rates[initial_currency]
            
            amount_converted = amount * exchange_rate
            
            if withdraw:
                comission = amount_converted * 0.01
                amount_converted -= comission
            return f"El monto convertido es {amount_converted:.2f} {final_currency}"

        # Retiro de fondos y comisiones
        withdraw = input("¿Desea retirar los fondos? (s/n): ")
        if withdraw.lower() == "s":
            withdraw = True
        else:
            withdraw = False

        result = convert_currency(amount, ["CLP", "ARS", "USD", "EUR", "TRY", "GBP"] [int(initial_currency) -1], ["CLP", "ARS", "USD", "EUR", "TRY", "GBP"] [int(final_currency) -1], withdraw)
        print(result)


        if withdraw:
            print("Se cobro una comision de 1%")
        else:
            print("No se han retirado los fondos")
        while True:
            restart = input("Desea hacer otra operacion (s/n): ")
            # Volver a menu principal
            if restart.lower() == "s":
                break
            elif restart.lower() == "n":
                print("Gracias por usar el convertidor")
                exit()
            else:
                print("Opcion invalida, Intente de nuevo")
                continue

menu()