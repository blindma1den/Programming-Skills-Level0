#Ejercicio 1
#Angel alcántar	

"""
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
"""
#para terminos prácticos usaré variables globales (no recomendado por seguridad).
usuarios = {
	"usuario1": "password"
}
saldo = 2000
intentos = 0
#funciones
def verificar_usuario(usuario, contrasena):
	global intentos
	if usuarios.get(usuario) == contrasena:
		intentos = 0
		return True
	else:
		intentos += 1
		return False

def depositar(monto):
	global saldo
	saldo += monto
	print("Depósito exitoso.")
def retirar(monto):
	global saldo
	if monto <= saldo:
		saldo-=monto
		return True
	else:
		return False
def mostrar_saldo():
	print(f"Saldo actual: ${saldo}")

#función para hacer transacciones.
def transferir(monto, usuario):
	global saldo
	if monto <= saldo:
		saldo -= monto
		print(f"Transferencia exitosa a {usuario}.")
	else:
		print("Saldo insuficiente.")
def menu():
	while True:
		print("1. Ver saldo")
		print("2. Depositar dinero")
		print("3. Retirar dinero")
		print("4. transferir dinero")
		print("5. Salir")
		opcion = int(input("Seleccione una opción: "))

		if opcion == 1:
			mostrar_saldo()
		elif opcion == 2:
			monto = float(input("Ingrese el monto a depositar: "))
			depositar(monto)
		elif opcion == 3:
			monto = float(input("Ingrese el monto a retirar: "))
			if not retirar(monto):
				print("Saldo insuficiente.")
		elif opcion == 4:
			monto = float(input("Ingrese el monto a transferir: "))
			usuario = input("Ingrese el nombre de usuario: ")
			transferir(monto, usuario)
		elif opcion == 5:
			print("Gracias por usar nuestro sistema bancario.")
			break
		else:
			print("Opción inválida. Por favor, intente de nuevo.")

def main():
	usuario = input("Nombre de usuario")
	password = input("password")
	if verificar_usuario(usuario, password) and intentos <3:
		menu()
	else:
		print("Usuario bloqueado.")
		return
if __name__ == "__main__":
	main()