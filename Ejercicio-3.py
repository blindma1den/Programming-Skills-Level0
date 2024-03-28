"""Crear un conversor de divisas entre CLP, ARS, USD, EUR, TRY, GBP con las siguientes características:

El usuario debe elegir su divisa inicial y la divisa a la que desea cambiar.
El usuario puede optar por retirar sus fondos o no. Si elige no retirarlos, debería regresar al menú principal.
Si el usuario decide retirar los fondos, el sistema cobrará una comisión del 1%.
Establecer un monto mínimo y máximo para cada divisa, puede ser de tu elección.
El sistema debe preguntar al usuario si desea realizar otra operación. 
Si elige hacerlo, debería reiniciar el proceso; de lo contrario, el sistema debería cerrarse."""

TasasDeDivisas = {

    "COP":3500,  # 1 Dolar = 3500 Pesos Colombiano
    "CLP":983,   # 1 Dolar = 983 Pesos Chilenos
    "VEN":38,    # 1 Dolar = 38 Bolivares
    "SOP":3,     # 1 Dolar = 3 soles
    "ARS":800,    # 1 Dolar = 800 Pesos Argentino
    "EUR":1.8    # 1 Dolar = 1,8 Euros
}

def Giro():
    
    Eleccion = input("Ingrese su seleccion: ")
    Dolares = int(input("ingrese la cantidad de dolares a cambiar: "))

    if Eleccion not in TasasDeDivisas:
        print("Divisia invalida")
        return
    
    comision = 0.01
    tasa_conversion = TasasDeDivisas[Eleccion]

    if Eleccion != "USD":
        dolares -= dolares * comision

    cambio = Dolares * tasa_conversion
    print(f"Usted va a recibir la cantidad de {cambio:.2f} {Eleccion}")

    if Eleccion == "1":
        Cambio = TasasDeDivisas["COP"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}COP")
    elif Eleccion == "2":
        Cambio = TasasDeDivisas["CLP"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}CLP")
    elif Eleccion == "3":
        Cambio = TasasDeDivisas["VEN"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}VEN")
    elif Eleccion == "4":
        Cambio = TasasDeDivisas["SOP"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}SOP")
    elif Eleccion == "5":
        Cambio = TasasDeDivisas["ARS"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}ARS")
    elif Eleccion == "6":
        Cambio = TasasDeDivisas["EUR"] * Dolares
        print(f"Usted va recibir la cantidad de {Cambio}EUR")
    else:
        print("Selecion invalida")
    
def main():
    while True:
        
        print("Seleccione la divisa que desea obtener: ")
        print("1. COP(Peso Colonbiano)")
        print("2. CLP(Peso Chileno)")
        print("3. VEN(Bolivar Venezolano)")
        print("4. SOP(Sol Peruano)")
        print("5. ARS(Peso Argentino)")
        print("6. EUR(Euro)")

        Giro()

        Continuar = input("Desea hacer otra transaccion? (si/no): ")
        if Continuar != "si":
            break


if __name__ == "__main__":
    main()


    