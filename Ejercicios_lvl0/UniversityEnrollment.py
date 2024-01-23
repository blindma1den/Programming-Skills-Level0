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

# Listas
london_1 = []
london_2 = []
london_3 = []
london_4 = []
manchester_1 = []
manchester_2 = []
manchester_3 = []
manchester_4 = []
liverpool_1 = []
liverpool_2 = []
liverpool_3 = []
liverpool_4 = []
computer_science = [london_1, manchester_1, liverpool_1]
medicina = [london_2, manchester_2, liverpool_2]
marketing = [london_3, manchester_3, liverpool_3]
artes = [london_4, manchester_4, liverpool_4]
estudiantes = [computer_science, medicina, marketing, artes]
lista_programas = ['computer science', 'medicina', 'marketing', 'artes']
lista_campus = ['london', 'manchester', 'liverpool']
valor_campus = [['london_1', 'manchester_1', 'liverpool_1'], ['london_2', 'manchester_2', 'liverpool_2'],
                ['london_3', 'manchester_3', 'liverpool_3'],
                ['london_4', 'manchester_4', 'liverpool_4']]
slots_disponible = {'london_1': 1, 'manchester_1': 3, 'liverpool_1': 1, 'london_2': 2, 'manchester_2': 3,
                    'liverpool_2': 1, 'london_3': 1, 'manchester_3': 3, 'liverpool_3': 1, 'london_4': 1,
                    'manchester_4': 3, 'liverpool_4': 1}


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


# Función para crear la ficha de un estudiante
def crear_estudiante():
    estudiante = {}
    while True:
        print('-' * 50)
        print('Ingrese los siguientes datos para crear su ficha de estudiante:')
        nombre = input('Escriba su nombre: ')
        segundo_nombre = input('Escriba su segundo nombre: ')
        try:
            for programa in lista_programas:
                print(programa.capitalize())
            programa = input('Escoge un programa de la lista anterior: ').lower()
            lista_programas.index(programa)
        except ValueError:
            system('cls')
            print('Error, el programa o campus elegido no existe')
        else:
            system('cls')
            estudiante['nombre'] = nombre
            estudiante['segundo nombre'] = segundo_nombre
            estudiante['programa'] = programa
            return estudiante


# Función para terminar la ficha de estudiante y elegir su campus
def elegir_campus(estudiante):
    textos_campus = ['london', 'manchester', 'liverpool']
    while True:
        print('-' * 50)
        for campus in textos_campus:
            print(campus.capitalize())
        try:
            campus = input('Escoge un campus de la lista anterior: ').lower()
            lista_campus.index(campus)
        except ValueError:
            system('cls')
            print('Error, el campus elegido no existe')
        else:
            estudiante_completo = verificar_disponibilidad(estudiante, campus)
            if estudiante_completo is not None:
                system('cls')
                print('Estudiante creado exitosamente')
                input('Presione cualquier tecla para continuar')
                system('cls')
                indice_campus = lista_campus.index(campus)
                indice_programa = lista_programas.index(estudiante['programa'])
                estudiantes[indice_programa][indice_campus].append(estudiante)
                return estudiante_completo
            else:
                textos_campus.remove(campus)
                continue


# Función para verificar si el campus elegido tiene slots disponible
def verificar_disponibilidad(estudiante, campus):
    programa_elegido = estudiante['programa']
    indice_programa = lista_programas.index(programa_elegido)
    indice_campus = lista_campus.index(campus)
    campus_elegido = valor_campus[indice_programa][indice_campus]
    if campus == 'london' and slots_disponible[campus_elegido] > 0:
        estudiante['campus'] = campus
        slots_disponible[campus_elegido] -= 1
        return estudiante
    elif campus == 'manchester' and slots_disponible[campus_elegido] > 0:
        estudiante['campus'] = campus
        slots_disponible[campus_elegido] -= 1
        return estudiante
    elif campus == 'liverpool' and slots_disponible[campus_elegido] > 0:
        estudiante['campus'] = campus
        slots_disponible[campus_elegido] -= 1
        return estudiante
    else:
        system('cls')
        print('No quedan slots disponible es este campus')
        return None


# Función para verificar si existen estudiantes
def verificar_estudiantes(indice_programa, indice_campus):
    lista = estudiantes[indice_programa][indice_campus]
    if len(lista) > 0:
        return True
    else:
        return False


# Función para selecciona menus
def mostrar_menus():
    while True:
        print('-' * 50)
        indice_menu = 1
        for programa in lista_programas:
            print(f'[{indice_menu}] {programa.capitalize()}')
            indice_menu += 1
        try:
            programa = input('Elige un programa: ')
            ['1', '2', '3', '4'].index(programa)
            system('cls')
            indice_campus = 1
            for campus in lista_campus:
                print(f'[{indice_campus}] {campus.capitalize()}')
                indice_campus += 1
            campus = input('Elige un campus: ')
            ['1', '2', '3'].index(campus)
        except ValueError:
            system('cls')
            print('Error, elige un programa o campus correcto')
        else:
            system('cls')
            indice_programa = int(programa) - 1
            indice_campus = int(campus) - 1
            ubicacion_estudiante = estudiantes[indice_programa][indice_campus]
            validacion = verificar_estudiantes(indice_programa, indice_campus)
            if validacion:
                for estudiante in ubicacion_estudiante:
                    system('cls')
                    for key, value in estudiante.items():
                        print(f'{key.capitalize()} : {value.capitalize()}')
                    input('Presione cualquier tecla para continuar')
                system('cls')
                return
            else:
                print('No existen estudiantes actualmente en este lugar')
                input('Presione cualquier tecla para continuar')
                system('cls')
                return


# Función del menu del programa
def menu():
    while True:
        print('Bienvenido al sistema de inscripción de Universidad')
        print('-' * 50)
        print('[1] Crear nuevo estudiante\n[2] Ver lista de estudiantes\n[3] Finalizar programa')
        try:
            accion = input('Elige una opción: ')
            ['1', '2', '3'].index(accion)
        except ValueError:
            system('cls')
            print('Error, escoge una opción correcta')
        else:
            system('cls')
            return accion


# Función principal
def main():
    system('cls')
    validacion = inicio_sesion()
    while validacion:
        accion = menu()
        if accion == '1':
            estudiante = crear_estudiante()
            elegir_campus(estudiante)
            continue
        elif accion == '2':
            mostrar_menus()
            continue
        else:
            system('cls')
            print('El programa ha sido finalizado')
            validacion = False


if __name__ == '__main__':
    main()
