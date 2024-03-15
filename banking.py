class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.intentos = 0  # Número de intentos de inicio de sesión fallidos
        self.saldo = 2000  # Saldo inicial en la cuenta bancaria

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.intentos = 0  # Restablecer el contador de intentos de inicio de sesión
            return True
        else:
            self.intentos += 1  # Incrementar el contador de intentos fallidos
            if self.intentos >= 3:
                print("¡Cuenta bloqueada por demasiados intentos fallidos de inicio de sesión!")
                return False

    def depositar(self, monto):
        self.saldo += monto
        print("¡Depósito exitoso! Nuevo saldo:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("¡Retiro exitoso! Nuevo saldo:", self.saldo)
        else:
            print("Fondos insuficientes")

    def transferir(self, monto, destinatario):
        if monto <= self.saldo:
            self.saldo -= monto
            destinatario.depositar(monto)  # Utilizamos el método depositar del destinatario
            print("¡Transferencia exitosa! Nuevo saldo:", self.saldo)
        else:
            print("Fondos insuficientes")

    def ver_saldo(self):
        print("Saldo actual:", self.saldo)


def main():
    # Crear usuarios
    usuarios = [
        Usuario("ManchesterU", "Cr7TheBest"),
        Usuario("Snowman", "1234")
    ]

    print("¡Bienvenid@ al Banco de La Secta!")

    while True:
        print("\n1. Iniciar sesión")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")

            usuario_actual = None
            for usuario in usuarios:
                if usuario.login(username, password):
                    usuario_actual = usuario
                    print("¡Inicio de sesión exitoso!")
                    break
            else:
                print("Credenciales incorrectas. Inténtelo de nuevo.")
                continue

            while True:
                print("\n1. Depositar")
                print("2. Retirar")
                print("3. Transferir")
                print("4. Ver saldo")
                print("5. Salir")

                opcion_transaccion = input("Seleccione una opción de transacción: ")

                if opcion_transaccion == "1":
                    monto = float(input("Ingrese el monto a depositar: "))
                    usuario_actual.depositar(monto)
                elif opcion_transaccion == "2":
                    monto = float(input("Ingrese el monto a retirar: "))
                    usuario_actual.retirar(monto)
                elif opcion_transaccion == "3":
                    monto = float(input("Ingrese el monto a transferir: "))
                    destinatario_username = input("Ingrese el nombre de usuario del destinatario: ")
                    destinatario = None
                    for u in usuarios:
                        if u.username == destinatario_username:
                            destinatario = u
                            break
                    else:
                        print("Destinatario no encontrado.")
                        continue
                    usuario_actual.transferir(monto, destinatario)
                elif opcion_transaccion == "4":
                    usuario_actual.ver_saldo()
                elif opcion_transaccion == "5":
                    break
                else:
                    print("Opción no válida")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
