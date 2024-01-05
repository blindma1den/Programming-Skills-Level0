'''
1. Create an online banking system with the following features:
    * Users must be able to log in with a username and password.
    * If the user enters the wrong credentials three times, the system must lock them out.
    * The initial balance in the bank account is $2000.
    * The system must allow users to deposit, withdraw, view, and transfer money.
    * The system must display a menu for users to perform transactions.
'''

# Funcion para acceso al sistema
def login(): 
    # Se definen las credenciales iniciales
    username = "greg"
    password = "1234"
    attempts = 3

    # Login para entrar al sistema
    while attempts > 0:
        username_input = input("Por favor inserte su usuario: ")
        password_input = input("Por favor inserte su contraseña: ")
        if username_input == username and password_input == password:
            print("Bienvenido a tu Banca en Linea")
            break
        else:
            attempts -= 1
            print(f"Datos incorrectos. Tiene {attempts} intentos restantes")
    else: 
        print(f"El sistema esta bloqueado")

# Funcion para el menu principal
def menu(balance):
    # Despliegue de las opciones
    while True:
        menu_transactions = ["Ver Saldo", "Deposito", "Retiro", "Transferencia"]
        for i, transaction in enumerate(menu_transactions):
            print(f"{i+1}. {transaction}")
        
        choice = input("Que operacion desea realizar: ")
        # Muestra el saldo en cuenta
        if choice == '1':
            print(f"Tu Saldo es: {balance}")
        #Operacion de Deposito
        elif choice == '2':
            amount = float(input("Indica cantidad a depositar: "))
            balance += amount
            print(f"Depositado: {amount}, tu nuevo saldo es: {balance}")
        # Operacion de Retiro
        elif choice == '3':
            amount = float(input("Indica cantidad a retirar: "))
            if balance >= amount:
                balance -= amount
                print (f"Retirado {amount}, tu nuevo saldo es: {balance}")
            else:
                print("Fondos Insuficientes")
        # Operacion de Transferencia
        elif choice == '4':
            recipient = input("Ingrese el nombre de usuario del receptor: ")
            amount = float(input("Ingrese la cantidad a transferir: "))
            if balance >= amount:
                balance -= amount
                print(f'Transferido {amount} a {recipient}. Tu Saldo es {balance}.')
                
        else:
            print("Opcion invalida, Intenta de nuevo")

        while True:
            restart = input("Desea hacer otra operacion (s/n): ")
            # Volver a menu principal
            if restart.lower() == "s":
                break
            elif restart.lower() == "n":
                print("Gracias por usar tu banca en linea")
                exit()
            else:
                print("Opcion invalida, Intente de nuevo")
                continue

login()
menu(2000)

