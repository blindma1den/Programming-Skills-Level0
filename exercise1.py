import sys
username = input('Registre el usuario:  ')
password = input('Cree la contraseña:  ')

balance_bank = 2000

#login
attemps = 0
while attemps < 3:
        loginUsername = input('Introduzca el Usuario:  ')
        loginPassword = input('Introduzca la Contraseña:  ')
        if loginUsername == username and loginPassword == password:
            attemps = 4
        else: print('El Usuario o la Contraseña es incorrecto')
        attemps = attemps + 1
        if attemps == 5:
          print('-------------------MENU-----------------')
          print('1- Depositar')
          print('2- Retirar')
          print('3- Ver Saldo')
          print('4- Transferir')
          print('5- Salir')
          print('')
          menu = 0
          while menu < 6:
               menu = int(input('Introduzca el número del módulo deseado:  '))
               if menu == 1:
                    dep = int(input('Introduzca el monto a depositar:  '))
                    balance_bank = balance_bank+dep
                    menu = 0
               if menu == 2:
                    withdraw = int(input('Introduzca el monto a retirar:  '))
                    balance_bank = balance_bank-withdraw
                    menu = 0
               if menu == 3:
                    print('El saldo es: ',balance_bank)
                    menu = 0
               if menu == 4:
                    (input('Introduzca el usuario a transferir:  '))
                    trans = int(input('Introduzca el monto a transferir'))
                    balance_bank = balance_bank-trans
                    menu = 0
               if menu == 5:
                    print('Gracias por todo <3. Vuelva prontos')
                    break
          if menu > 5:
               print('Ese módulo no existe.')