users_dict = {"Juancito": "123", "Admin": "admin", "Error": "NoError"}


def login():
    attempts = 0
    while attempts < 3:
        user = input("Ingrese su usuario: ")
        password = input("Ingrese la contraseña: ")
        if user in users_dict and users_dict[user] == password:
            print("¡Usuario logueado!")
            return user
        else:
            print("El usuario y/o la contraseña son incorrectos")
            if attempts == 2:
                print("Ha ingresado demasiadas veces mal el usuario y/o la contraseña, reintente más tarde")
            attempts += 1


def banking_management():
    user = login()
    # Emulación de usuarios con su dinero correspondiente
    logged_user = {"Balance": 2000, "Name": user, "Alias": "LogUsr"}
    other_user = {"Balance": 2000, "Name": "Test", "Alias": "Test"}
    other_user2 = {"Balance": 2000, "Name": "Test2", "Alias": "Test2"}
    management_dict = [logged_user, other_user, other_user2]

    while True:
        print("Menú de HomeBanking:\n"
              "1. Ver saldo\n"
              "2. Transferir\n"
              "3. Depositar\n"
              "4. Retirar\n"
              "0. Salir\n")
        op = int(input("Ingrese una opción: "))
        if op == 1:
            print("Su saldo es", logged_user["Balance"])

        elif op == 2:
            alias = input("Ingrese el Alias del usuario a recibir la transferencia: ")
            for usr in management_dict:
                if usr["Alias"] == alias:
                    ammount = int(input("Ingrese la cantidad de dinero a transferir: "))
                    if ammount > logged_user["Balance"]:
                        print("La cantidad de dinero es superior a su saldo")
                    else:
                        logged_user["Balance"] -= ammount
                        usr["Balance"] += ammount

        elif op == 3:
            ammount = int(input("Ingrese la cantidad a depositar: "))
            logged_user["Balance"] += ammount
            print("Depósito exitoso")

        elif op == 4:
            ammount = int(input("Ingrese la cantidad a retirar: "))
            if logged_user["Balance"] < ammount:
                print("El monto a retirar es superior a su saldo")
            else:
                logged_user["Balance"] -= ammount
                print("Retiro realizado con éxito")

        elif op == 0:
            break

        else:
            print("La opción ingresada no es correcta.")
