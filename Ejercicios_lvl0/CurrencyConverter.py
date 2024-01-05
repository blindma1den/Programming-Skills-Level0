# Por Felipe (ZenTial)

# Ejericio 2
# Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# The user must choose their initial currency and the currency they want to exchange to.
# The user can choose whether or not to withdraw their funds.
# If they choose not to withdraw, it should return to the main menu.
# If the user decides to withdraw the funds, the system will charge a 1% commission.
# Set a minimum and maximum amount for each currency, it can be of your choice.
# The system should ask the user if they want to perform another operation.
# If they choose to do so, it should restart the process; otherwise, the system should close.
from os import system

# Tipos de monedas y su valor con el dolar como base

monedas = {'CLP': 887,
           'ARS': 811,
           'USD': 1,
           'EUR': 0.91,
           'TRY': 29.84,
           'GBP': 0.79}

# Monto minimo y maximo de retiro para cada moneda
montos = {'CLP': [1000, 500000],
          'ARS': [100, 1000000],
          'USD': [1, 10000],
          'EUR': [1, 10000],
          'TRY': [1, 10000],
          'GBP': [1, 10000]
          }


# Función de la conversión
def conversion(moneda_i, moneda_d, monto):
    if moneda_i == moneda_d:
        return monto
    else:
        return monto * monedas[moneda_d] / monedas[moneda_i]


# Función para retirar fondos
def retiro(monto, moneda_d):
    cantidades = list(montos[moneda_d])
    try:
        accion = input('¿Desea retirar sus fondos? [S/N]: ').upper()
        ['S', 'N'].index(accion)
    except ValueError:
        system('cls')
        print('Ingrese una opción correcta\n')
    else:
        if accion == 'N':
            return monto
        else:
            system('cls')
            while True:
                print('*' * 50)
                print(f'¿Cuanto dinero desea retirar? {cantidades} (Se le cobrara una comisión de un 1%):')
                print(f'Balance actual: {round(monto, 2)}{moneda_d}')
                monto_retirado = float(input(''))
                if monto_retirado <= monto:
                    system('cls')
                    print('Saldo insuficiente')
                    continue
                elif monto_retirado in range(min(cantidades), max(cantidades)):
                    monto_nuevo = (monto - (monto * 0.01)) - monto_retirado
                    system('cls')
                    print(f'Se ha retirado existosamente {monto_retirado}{moneda_d}')
                    return monto_nuevo
                else:
                    system('cls')
                    print('Ingrese un valor correcto')
                    continue


# Realizar otra transacción
def continuar():
    try:
        accion = input('¿Desea realizar otra operación? [S/N]: ').upper()
        ['S', 'N'].index(accion)
    except ValueError:
        system('cls')
        print('Ingrese una opción correcta')
    else:
        if accion == 'N':
            return False
        else:
            system('cls')
            return True


# Función principal del programa
def main():
    validacion = True
    balance = 0
    lista_monedas = list(monedas.keys())
    while validacion:
        print('*' * 50)
        print(f'Bienvenido al conversor de moneda, estos son los tipos de monedas disponibles: \n{lista_monedas}')
        print(f'Dinero actual: {balance}')
        try:
            moneda_inicial = input('Cual es su tipo de moneda?: ').upper()
            lista_monedas.index(moneda_inicial)
            moneda_deseada = input('¿A cual moneda desea cambiar?: ').upper()
            lista_monedas.index(moneda_deseada)
            cantidad_deseada = int(input('¿Cuanto dinero desea convertir?: '))
        except:
            system('cls')
            print('Elija un tipo de moneda correcta')
        else:
            monto_convertido = conversion(moneda_inicial, moneda_deseada, cantidad_deseada)
            balance = retiro(monto_convertido, moneda_deseada)
            validacion = continuar()
    print('El programa ha sido finalizado')


if __name__ == '__main__':
    main()
