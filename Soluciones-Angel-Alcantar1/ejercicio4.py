#ejercicio4
#Angel alcántar
#python.

"""
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.


* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
"""
import random
#datos de login
usuarios = {"admin": "password"}
def login(usuarios):
  intentos = 0
  while(intentos<3):
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    if usuarios.get(usuario) == password:
      return True
    else:
      intentos += 1
      print("Usuario o contraseña incorrectos.")
  return False

#función para enviar un paquete
def enviar_paquete():
  #recpilar nombre del remitente, destinatario, peso del paquete, randomizar el número de paquete y calcular a la vez que se muestra el precio.
  nombre_remitente = input("Ingrese el nombre del remitente: ")
  nombre_destinatario = input("Ingrese el nombre del destinatario: ")
  peso = float(input("Ingrese el peso del paquete: "))
  numero_paquete = random.randint(1000, 9999)
  precio = calcular_precio_envio(peso)
  print(f"Paquete #{numero_paquete} enviado. Precio a pagar: ${precio}")
  #función para calcular el precio del envío
def calcular_precio_envio(peso):
  return peso * 2

#función para el menú
def sistema_envio():
    while True:
        if login(usuarios):
            while True:  # Añadir un bucle para volver al menú después de cada operación
                print("1. Enviar paquete")
                print("2. Salir")
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    enviar_paquete()
                elif opcion == "2":
                    print("Gracias por usar nuestro sistema de envío.")
                    break
                    exit()
                else:
                    print("Opción no válida.")

                otra_operacion = input("¿Desea realizar otra operación? (sí/no): ").lower()
                if otra_operacion != "sí":
                    break
                
        else:
            print("Ha excedido el número de intentos de inicio de sesión.")
            break

if __name__ == "__main__":
  sistema_envio()