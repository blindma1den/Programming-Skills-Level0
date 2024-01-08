#1. Create an online banking system with the following features:

#* Users must be able to log in with a username and password.
#* If the user enters the wrong credentials three times, the system must lock them out.
#* The initial balance in the bank account is $2000.
#* The system must allow users to deposit, withdraw, view, and transfer money.
#* The system must display a menu for users to perform transactions.


#Variables iniciales: 

counter = 3
balance_init = 2000
transfer_user = ''
account = int

while counter > 0:
   
    username = input('Escribe tu usuario: ')
    valid_users = ['laura','andrea','maria']
      
    if username in valid_users:
        password = input('Ingresa tu contraseña: ')
        valid_password = ('1234')
    if password == valid_password:
        print('¡Bienvenido a tu sistema bancario!')
        break
    counter = counter -1
    print('usuario inválido')
          
else:
    print('usuario inválido, comunícate con el administrador')


while True:
    print('MENÚ')
    print('1. Depositar')
    print('2. Retirar')
    print('3. Ver saldo')
    print('4. Transferir')
    
    opcion = int(input('Ingrese el número de la opción a realizar: '))

    if opcion == 1:
            depositar = float(input('¿Cuánto dinero desea depositar?: $'))  
            balance_init += depositar
            print(f'Nuevo saldo disponible en la cuenta: ${balance_init}')
            print(f'Gracias por utilizar nuestros servicios')
            break
            
    elif opcion == 2:
        retirar = float(input('¿Cuánto dinero desea retirar?: $'))  
                               
        if retirar > balance_init:
            print('Fondos insuficientes para realizar el retiro.')
           
        else:
            balance_init -= retirar  
            print(f'Nuevo saldo disponible en la cuenta: ${balance_init}')
            print(f'Gracias por utilizar nuestros servicios')
            break
          
    elif opcion == 3:
        print(f'Saldo disponible en la cuenta: ${balance_init}')
        print(f'Gracias por utilizar nuestros servicios')
        break

    elif opcion == 4:
        print('Recuerde que el saldo máximo para transferir es de $1000')
        print("Ingrese los datos para la transferencia: ")
        transfer_user = input('Nombre a quién transfiere: ')
        account = int = input('Numero de cuenta a transferir: ')
        tranferir = float(input('Valor a transferir: $'))
                      
        if tranferir > balance_init:
            print('Fondos insuficientes para realizar la transferencia.')
                    
        elif tranferir > 1000:
            print('La transferencia maxima es $1000, elija otra cantidad')
        
        else:
            balance_init -= tranferir   
            print(f'La transferencia se realizó correctamente a nombre de: {transfer_user}')      
            print(f'Número de cuenta {account}') 
            print(f'Monto de la transferencia ${tranferir}')  
            print(f'Nuevo saldo disponible en la cuenta: ${balance_init}')     
            print(f'Gracias por utilizar nuestros servicios')
            break           

    else: 
        print('Opción incorrecta')