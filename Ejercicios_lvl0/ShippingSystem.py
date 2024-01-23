from os import system
from random import randint

# Por Felipe (ZenTial)

# Ejercicio 4
# Create an online shipping system with the following features:
# The system has a login that locks after the third failed attempt.
# Display a menu that allows: Sending a package, exiting the system.
# To send a package, sender and recipient details are required.
# The system assigns a random package number to each sent package.
# The system calculates the shipping price. $2 per kg.
# The user must input the total weight of their package, and the system should display the amount to pay.  
# The system should ask if the user wants to perform another operation.
# If the answer is yes, it should return to the main menu. If it's no, it should close the system.


# Función de inicio de sesión
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


# Función del envio
def envio():
    system('cls')
    print('*' * 50)
    emisor = input('¿Quien envia el paquete: ')
    receptor = input('¿Quien recibira el paquete?: ')
    objeto = input('¿Que objeto va a enviar?: ')
    numerodeserie = randint(1000000, 9999999)
    peso = int(input('¿Cuanto pesa el paquete?: '))
    system('cls')
    print('*' * 50)
    print(f'Emisor: {emisor}\nReceptor: {receptor}\nObjeto: {objeto}\nN°de serie: {numerodeserie}\nPeso: {peso}kg')
    return peso


# Función para calcular precio
def precio_paquete(peso):
    system('cls')
    precio = peso * 2
    print('*' * 50)
    print(f'Usted debera de pagar ${precio}USD')
    input('Presione para continuar')


# Función para confirma operación
def continuar():
    system('cls')
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


# Función del menu
def menu():
    while True:
        print('*' * 50)
        print('[1] Realizar un envío\n[2] Salir del programa')
        print('*' * 50)
        try:
            accion = input('¿Bienvenido usuario que desea hacer?: ')
            ['1', '2'].index(accion)
        except ValueError:
            system('cls')
            print('Ingrese una opción correcta')
        else:
            return accion


# Función principal del programa
def main():
    validacion = inicio_sesion()
    while validacion:
        accion = menu()
        if accion == '1':
            datos = envio()
            precio_paquete(datos)
            validacion = continuar()
        else:
            validacion = False
    system('cls')
    print('Se ha finalizado el programa')

if __name__ == '__main__':
    main()
