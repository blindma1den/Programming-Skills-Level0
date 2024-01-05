# Ejericio 3
# The system has a login with a username and password.
# Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
# The user must input their first name, last name, and chosen program.
# Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
# If login information is incorrect three times, the system should be locked.
# The user must choose a campus from three cities: London, Manchester, Liverpool.
# In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
# If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
from os import system

# Listas de programas
computer_science = []
medicina = []
marketing = []
artes = []
# Función inicio de sesión
def inicio_sesion():
    usuario = 'admin'
    password = 'python'
    intentos = 0
    while True:
        try:
            usuario_input = input('Ingrese un usuario: ')
            contrasena_input = input('Ingrese una contraseña: ')
            [usuario].index(usuario_input)
            [password].index(contrasena_input)

        except ValueError:
            intentos += 1
            system('cls')
            print('Ingresa las credenciales correctas.')

        else:
            system('cls')
            return True

        finally:
            if intentos == 3:
                system('cls')
                print('El sistema ha sido bloqueado debido a que ha hecho muchos intentos')
                return False


# Función de menu
def menu():
    datos_estudiante = {}
    print('*' * 50)
    print('Bienvenido al sistema de inscripción. Estas son los programas disponibles:')
    print('[Computer science] [Medicina] [Marketing] [Artes]')
    try:
        nombre = input('Ingrese su primer nombre: ')
        segundo_nombre = input('Ingrese su segundo nombre: ')
        programa = input('Elija a que programa se quiere inscribir: ').capitalize()
        ['Computer science', 'Medicina', 'Marketing', 'Artes'].index(programa)
    except ValueError:
        system('cls')
        print('Ingresa un programa que exista')
    else:
        datos_estudiante['nombre'] = nombre
        datos_estudiante['segundo nombre'] = segundo_nombre
        datos_estudiante['programa'] = programa
        return datos_estudiante


# Selección de campus
def campus(estudiante):
    london = []
    manchester = []
    liverpool = []
    zonas = [london, manchester, liverpool]
    print('*' * 50)
    try:
        print('Opciones: London, Manchester, Liverpool')
        zona = input('¿A que campus quiere inscribirse?: ').lower()
        indice = ['london', 'manchester', 'liverpool'].index(zona)
    except:
        system('cls')
        print('El campus elegido no existe')
    else:
        zonas[indice].append(estudiante)
        print(zonas)


# Función principal
def main():
    validacion = inicio_sesion()
    while validacion:
        datos_estudiante = menu()
        system('cls')
        campus(datos_estudiante)




if __name__ == '__main__':
    main()
