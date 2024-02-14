"""1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.

"""

banco = {'david22': ['miclave', 2000],
         'liss97': ['suclave', 2000]
         }
c = 3


def depositar():  # funcion para hacer depositos a la cuenta
    deposito = int(input('Cuanto dinero va a depositar?\n$'))
    banco[user][1] = banco[user][1] + deposito
    print('su nuevo saldo es: $', banco[user][1])


def retirar():  # funcion para retirar dinero de la cuenta
    retiro = int(input('Cuanto dinero quiere retirar?\n$'))
    if retiro > banco[user][1]:
        print('fondos insuficientes')
    else:
        banco[user][1] = banco[user][1] - retiro
        print('su nuevo saldo es: ', banco[user][1])


def ver_saldo():  # funcion para ver el saldo en la cuenta
    print('su saldo es: ', banco[user][1])


def transferir():  # funcion para transferir dinero a otra cuenta
    cuenta = input('a que cuenta quiere transferir dinero?'
                     '--->>> '
                     )
    valor = int(input('cuanto quiere transferir?'
                  '--->>> '))
    if banco[user][1] >= valor:
        banco[user][1]-= valor
        banco[cuenta][1] += valor
        print('transferencia exitosa, el nuevo balance de su cuenta es: ', banco[user][1])
    else:
        print('no cuenta con fondos suficientes para hacer la transferencia')


for i in range(
        c):  # con este bucle estaremos haciendo la validacion el cual usa la Variable C como variable de control y tiene 3 intentos
    user = input('ingrese su usuario: ')  # solicitamos el nombre del usuario

    if user in banco:  # si esta dentro del diccionario le permite ingresar la contraseña
        password = input('ingrese su contraseña: ')  # solicitamos la contraseña

        if password in banco[
            user]:  # si la contraseña esta en la lista a la que apunta la clave de usuario en el diccionario le deja pasar
            print('***Ingreso correctamente***')  # informa del ingreso correcto
            print('Su saldo es: ', banco[user][1])  # muestra el saldo actual a modo de informacion
            print('*****************************************************************')

            control = True
            while control:

                print('¿Qué deseas hacer?:\n'  # este es nuestro menu de opciones luego de iniciar sesion 
                      '1.Depositar\n'  # cada una de estas opciones esta representado por funciones las cuales estan definidas desde el principio del codigo
                      '2.Retirar\n'
                      '3.Ver saldo\n'
                      '4.Transferir\n'
                      '5.Nada')
                opcion = int(input(
                    'Digita el numero de la opcion: '))  # pedimos al usuario ingresar el numero de la opcion que desea realizar

                match opcion:
                    case 1:
                        depositar()
                    case 2:
                        retirar()
                    case 3:
                        ver_saldo()
                    case 4:
                        transferir()
                    case 5:
                        print('hasta luego')
                        confirmacion = input('estas seguro?\n***********************************\n'
                                             '***escribe si o no***\n')
                        if confirmacion == 'si':
                            control = False
            break

        else:
            fallo = 2
            fallo = fallo - i
            print('usuario o contraseña incorrecto, intentos restantes:', fallo)
    else:
        fallo = 2
        fallo = fallo - i
        print('usuario o contraseña incorrecto, intentos restantes:', fallo)
