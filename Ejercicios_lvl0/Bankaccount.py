# Por Felipe (ZenTial)

# Ejercicio 1
# Users must be able to log in with a username and password.
# If the user enters the wrong credentials three times, the system must lock them out.
# The initial balance in the bank account is $2000.
# The system must allow users to deposit, withdraw, view, and transfer money.
# The system must display a menu for users to perform transactions.
from os import system


# Función para el ingreso a la cuenta bancaria
def inicio_sesion():
    usuario = 'admin'
    password = 'python'
    intentos = 0
    while True:
        try:
            usuario_input = input('Ingrese un usuario: ')
            contrasena_input = input('Ingrese una contraseña: ')
            [usuario].index(usuario_input)
            [password].index(contrasena_input)

        except ValueError:
            intentos += 1
            system('cls')
            print('Ingresa las credenciales correctas.')

        else:
            system('cls')
            return True

        finally:
            if intentos == 3:
                system('cls')
                print('El sistema ha sido bloqueado debido a que ha hecho muchos intentos')
                return False


# Funcíón para depositar
def depositar(din):
    system('cls')
    deposito = int(input('Ingrese la cantidad a depositar: '))
    din += deposito
    print('Su dinero ha sido depositado exitosamente.')
    input('Presione cualquier tecla para continuar')
    return din


# Función para retirar
def retirar(din):
    system('cls')
    retiro = int(input('Ingrese el dinero que desea retirar: '))
    if din >= retiro:
        din -= retiro
        print('Su retiro se ha realizado exitosamente')
        input('Presione cualquier tecla para continuar.')
        return din
    else:
        input('Saldo insuficiente. Presione cualquier tecla para continuar')
        return din


# Función para ver el saldo
def ver_saldo(din):
    system('cls')
    print(f'El saldo actual de tu cuenta es ${din}CLP')
    input('Presiona cualquier tecla para continuar')


# Función para transferir a otra cuenta bancaria
def transferir(din):
    system('cls')
    nombre = input('Ingrese el nombre de la persona a la que desea transferir: ')
    cantidad = int(input('Ingrese cuanto dinero desea transferir: '))
    if din >= cantidad:
        din -= cantidad
        print(f'Se han transferido exitosamente ${cantidad}CLP a {nombre}')
        input('Presione cualquier tecla para continuar.')
        return din
    else:
        input('Saldo insuficiente. Presione cualquier tecla para continuar')
        return din


# Función para el menu del programa
def menu(monto):
    print('Bienvenido usuario, elija una opción:')
    print('*' * 50)
    print('[D] Depositar\n[R] Retirar\n[V] Ver saldo actual\n[T] Transferir dinero\n[F] Finalizar programa')

    try:
        eleccion_usuario = input('').upper()
        ['D', 'R', 'V', 'T', 'F'].index(eleccion_usuario)

    except ValueError:
        system('cls')
        print('Ingrese una opción valida\n')

    else:
        return eleccion_usuario


def main():
    dinero = 2000
    validacion = inicio_sesion()
    while validacion:
        accion = menu(dinero)
        if accion == 'D':
            dinero = depositar(dinero)
            system('cls')
            continue
        elif accion == 'R':
            dinero = retirar(dinero)
            system('cls')
            continue
        elif accion == 'V':
            ver_saldo(dinero)
            system('cls')
            continue
        elif accion == 'T':
            dinero = transferir(dinero)
            system('cls')
            continue
        else:
            system('cls')
            print('Gracias por usar nuestro sistema bancario, nos vemos pronto')
            return False


if __name__ == '__main__':
    main()
