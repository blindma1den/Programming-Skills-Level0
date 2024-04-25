import getpass


def create_account_fn(read_json_fn, write_json_fn, file_path, clean): 

    """
    Solo permite 2 itentos para crear la cuenta,
    en caso sea creada la cuenta con éxito se ejecuta la fn login
    """

    data = read_json_fn(file_path)
    attemps = 2

    while True:
        if attemps == 0:
            print("Demasiados intentos fallidos")
            exit()
        
        print(f"👉 Intentos: {attemps}")
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')

        # Interface
        clean(1.5)
        print('Confirm your new account:')
        print('-' * len('Confirm your new account:'))
        print(f"Account: {username}\nPassword: {password}")
        print(f"\n1. Confirmar\n2. Cancelar\n3. Salir\n")


        option = int(input('Option: '))
        if option == 1:
            break

        elif option == 2:
            attemps -= 1
            
            print("Reiniciando...")
            clean(1.5)
            continue
        
        elif option == 3:
            exit()

    clean(1.5)
    print("Usuario creado con éxito")
    new_user = {
            'user': username,
            'password': password,
            'paquetes_activos': 0,
            'paquetes_enviados': 0
        }
    data.append(new_user)
    write_json_fn(data, file_path)

    return username

def login_account_fn(read_json_fn, file_path, clean, attemps=3):
    # Carga
    clean(1.5)
    # Control de acceso
    status_login = False

    # Cargar datos
    data = read_json_fn(file_path)

    # Intentos
    if attemps == 0:
        print("Demasiados intentos fallidos")
        return status_login

    # Inputs e interface
    print(f"{"-" * 100} Intentos: {attemps}")
    print("Iniciar sesión")
    print("-" * len("Iniciar sesión"))
    
    user_name = input('Enter username: ').strip()
    password = getpass.getpass('Enter password: ').strip()

    # Verificar datos
    for user in data:
        if user['user'] == user_name and user['password'] == password:
            status_login = True
            return user_name
        
        
    return login_account_fn(read_json_fn, file_path, clean, attemps-1)
        

        









