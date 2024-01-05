import punto_uno_banking
import punto_dos_currency_converter

if __name__ == '__main__':

    op = int(input("Ingrese una opción: "))

    while True:
        if op == 1:
            punto_uno_banking.banking_management()

        elif op == 2:
            punto_dos_currency_converter.converter_manager()

        elif op == 3:
            continue

        elif op == 4:
            continue

        elif op == 5:
            continue

        elif op == 0:
            break

        else:
            print("El valor seleccionado no es válido.")

        op = int(input("Ingrese una opción: "))