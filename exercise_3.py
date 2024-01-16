"""3. Create an university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing,
 and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user,
 and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool,
 there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots,
 the system should display the option to enroll in the program at another campus."""

print("university enrollment system")

class SistemaInscripcion:
    def __init__(self):
        self.programas = {
            'Ciencias de la Computación': {'Londres': 1, 'Manchester': 3, 'Liverpool': 1},
            'Medicina': {'Londres': 1, 'Manchester': 3, 'Liverpool': 1},
            'Marketing': {'Londres': 1, 'Manchester': 3, 'Liverpool': 1},
            'Artes': {'Londres': 1, 'Manchester': 3, 'Liverpool': 1},
        }
        self.usuarios = {}
        self.intentos_inicio_sesion = 0
        self.max_intentos_inicio_sesion = 3

    def inicio_sesion(self):
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario == "lucas" and contrasena == "12345":
            self.mostrar_menu_programas()
        elif usuario == "martin" and contrasena == "123":
            self.mostrar_menu_programas()
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            self.intentos_inicio_sesion += 1
            if self.intentos_inicio_sesion >= self.max_intentos_inicio_sesion:
                print("Demasiados intentos de inicio de sesión. El sistema está bloqueado.")
                exit()
            self.inicio_sesion()

    def mostrar_menu_programas(self):
        while True:
            print("Programas disponibles:")
            for programa in self.programas:
                print(f"- {programa}")

            programa_elegido = input("Ingrese el nombre del programa en el que desea inscribirse: ")

            if programa_elegido not in self.programas:
                print("Programa inválido. Por favor, elija entre los programas disponibles.")
                continue

            campus = input("Elija un campus (Londres, Manchester, Liverpool): ")
            if campus not in ['Londres', 'Manchester', 'Liverpool']:
                print("Campus inválido. Por favor, elija entre Londres, Manchester o Liverpool.")
                continue

            if self.programas[programa_elegido][campus] > 0:
                self.inscribir_usuario(programa_elegido, campus)
            else:
                print(f"No hay espacios disponibles para {programa_elegido} en {campus}.")
                self.inscribir_en_otro_campus(programa_elegido)

    def inscribir_usuario(self, programa, campus):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        if programa not in self.usuarios:
            self.usuarios[programa] = {}

        if campus not in self.usuarios[programa]:
            self.usuarios[programa][campus] = []

        if len(self.usuarios[programa][campus]) < 5: 
            self.usuarios[programa][campus].append({'Nombre': nombre, 'Apellido': apellido})
            print(f"Inscripción exitosa para {nombre} {apellido} en {programa} en {campus}.")
            self.preguntar_otro_usuario()
        else:
            print(f"Lo siento, no hay espacios disponibles para {programa} en {campus}.")
            self.inscribir_en_otro_campus(programa)

    def inscribir_en_otro_campus(self, programa):
        while True:
            cambiar_campus = input(f"¿Desea inscribirse en {programa} en otro campus? (sí/no): ").lower()
            if cambiar_campus == 'sí':
                break  
            elif cambiar_campus == 'no':
                print("Volviendo al menú principal.")
                return  
            else:
                print("Por favor, ingrese 'sí' o 'no'.")

    def preguntar_otro_usuario(self):
        while True:
            otro_usuario = input("¿Desea registrar a otro usuario? (sí/no): ").lower()
            if otro_usuario == 'sí':
                self.inicio_sesion()  
            elif otro_usuario == 'no':
                print("Gracias por usar el sistema de inscripción.")
                exit()
            else:
                print("Por favor, ingrese 'sí' o 'no'.")


if __name__ == "__main__":
    sistema_inscripcion = SistemaInscripcion()
    sistema_inscripcion.inicio_sesion()

    