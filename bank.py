from database import Database, User
import getpass

database = Database()
database.create_tables()
print('Welcome'.center(50,'-'))

def login():
    user = User()
    username = input('USUARIO: ')
    password = getpass.getpass('PASSWORD: ')
    connection = user.login(username, password)
    if connection:
        global log_in
        log_in = True
        return user
  

def record():
    print('Necesitas registrarte:')
    user = User()
    first_name = input('Nombre (usuario): ')
    last_name = input('Apellido: ')
    password = getpass.getpass('Clave: ')
    user.create_user(first_name, last_name, password)
  

log_in = False
while True:
    
    print('Seleccione una opcion:', '\n', '1. Loguearse.', '\n', '0. Salir')
    option = input('\n>>> ')
    
    if option == '1':
        user = login()
        if log_in:
            while True:
                print('\nOpciones')
                print('1. DEPOSITAR')
                print('2. RETIRAR')
                print('3. VER')
                print('4. TRANSFERIR')
                print('0. SALIR')
                select = input('>>>')
                if select == '1':
                    print('\n-'*50)
                    deposit = input('Monto a depositar: ')
                    new_amount = user.deposit(deposit)
                    print("Su nuevo saldo es de ", new_amount)

                if select == '2':
                    print('\n-'*50)
                    withdraw = input('Monto a retirar: ')
                    result = user.withdraw(withdraw)
                    print(result) if type(result) is str else print(f'Monto es {result}')

                if select == '3':
                    view = user.view()
                    print('\n-'*50)
                    print('Su saldo es de: ', str(view).rjust(33))
                    print('-'*50)

                if select == '4':
                    users = user.users()
                    disponible = user.view()
                    print('\n-'*50)
                    print('Usuarios a transferir')
                    print('-'*50)                    
                    for u in range(len(users)):
                        print(u + 1, users[u][0])
                    print('-'*50)
                    transferir_a = input('Seleccione un usuario: ')
                    print('Cantidad disponible: ', disponible)
                    monto = input('Cuanto desea transferir: ')
                    transferencia = user.transfer_money(transferir_a, monto)
                    print('su nuevo saldo es: ', transferencia)
                    
                if select == '0':
                    print('Adios')
                    break
        else:
            print('\nUsuario o clave invalida, intente nuevamente\n')
    elif option == '0':
        print('Adios')
        break
    else:
        print('Opcion no válida, intente nuevamente\n')


