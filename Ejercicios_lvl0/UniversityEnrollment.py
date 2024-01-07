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
computer_science = []
medicina = []
marketing = []
artes = []
estudiantes = [computer_science, medicina, marketing, artes]
london = []
manchester = []
liverpool = []
zonas = [london, manchester, liverpool]
lista_contadores = [0, 0, 0]



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
def creacion_estudiante():
    while True:
        system('cls')
        datos_estudiante = {}
        print('*' * 50)
        print('Bienvenido al sistema de inscripción')
        try:
            nombre = input('Ingrese su primer nombre: ')
            segundo_nombre = input('Ingrese su segundo nombre: ')
            print('[Computer science] [Medicina] [Marketing] [Artes]')
            programa = input('Elija a que programa se quiere inscribir: ').lower()
            ['computer science', 'medicina', 'marketing', 'artes'].index(programa)
        except ValueError:
            system('cls')
            print('Ingresa un programa que exista')
        else:
            datos_estudiante['nombre'] = nombre
            datos_estudiante['segundo_nombre'] = segundo_nombre
            datos_estudiante['programa'] = programa
            return datos_estudiante


# Función para verificar cantidad en las listas
def verificar(cantidad_estudiante):
    if len(cantidad_estudiante) > 0:
        return True
    else:
        system('cls')
        print('No existen estudiantes actualmente')
        return False


# Función para verificar el maximo de estudiantes por campus
def verificar_cantidad(campues_elegido, contador_campus):
    if contador_campus[0] < 1 and campues_elegido == 'london':
        return True
    elif contador_campus[1] < 3 and campues_elegido == 'manchester':
        return True
    elif contador_campus[2] < 1 and campues_elegido == 'liverpool':
        return True
    else:
        system('cls')
        print('No quedan cupos en este campus')
        return False


# Función de muestra el menu de la lista de estudiantes
def lista_estudiantes():
    while True:
        system('cls')
        print('*' * 50)
        print('[1] Computer science\n[2] Medicina\n[3] Marketing\n[4] Artes')
        try:
            accion = input('Elija un programa: ')
            ['1', '2', '3', '4'].index(accion)
        except ValueError:
            system('cls')
            print('Ingrese una opción correcta')
        else:
            system('cls')
            return int(accion) - 1


# Función lista_campus
def lista_campus(accion):
    while True:
        system('cls')
        print('*' * 50)
        print('[1] London\n[2] Manchester\n[3] Liverpool')
        try:
            accion2 = input('Elija una opción: ').lower()
            ['1', '2', '3'].index(accion2)
        except ValueError:
            system('cls')
            print('Elija una opción correcta')
        else:
            accion2 = int(accion2) - 1
            contar = estudiantes[accion]
            if verificar(contar):
                system('cls')
                datos_estudiante = list(estudiantes[accion][accion2])
                for dato in datos_estudiante:
                    print(f'Nombre: {dato.get('nombre')}\nSegundo Nombre: {dato.get('segundo_nombre')}\n'
                          f'Programa: {dato.get('programa')}\nCampus: {dato.get('campus')}\n')
            input('Presione cualquier tecla para continuar ')
            system('cls')
            break


# Función para añadir a lista de programa
def anadir_estudiante(estudiante, programa_estudiante):
    indice = ['computer science', 'medicina', 'marketing', 'artes']
    programa_elegido = indice.index(programa_estudiante)
    estudiantes[programa_elegido].append(estudiante)
    print('Estudiante guardado exitosamente')
    input('Presione cualquier tecla para continuar ')


# Función para elegir campus
def elegir_campus(datos_estudiante):
    validacion = False
    campus_disponibles = ['london', 'manchester', 'liverpool']
    while not validacion:
        system('cls')
        print('*' * 50)
        print(f'Opoiones disponibles: {" ".join(campus_disponibles).title()}')
        try:
            campus = input('Elija un campus: ').lower()
            indice = campus_disponibles.index(campus)
        except ValueError:
            system('cls')
            print('Este campus no existe')
        else:
            validacion2 = verificar_cantidad(campus_disponibles[indice], lista_contadores)
            if validacion2:
                lista_contadores[indice] += 1
                datos_estudiante['campus'] = campus
                return datos_estudiante
            else:
                campus_disponibles.remove(campus)
                continue


# Selección de campus
def anadir_campus(estudiante, campus):
    system('cls')
    indice = ['london', 'manchester', 'liverpool']
    print('*' * 50)
    campus_elegido = indice.index(campus)
    zonas[campus_elegido].append(estudiante)
    return zonas[campus_elegido]


# Menu principal
def menu():
    while True:
        print('*' * 50)
        print('[1] Crear estudiante\n[2] Lista estudiantes\n[3] Finalizar programa')
        try:
            accion = input('Elija una opción: ')
            ['1', '2', '3'].index(accion)
        except ValueError:
            system('cls')
            print('Ingrese una opción valida')
        else:
            return accion


# Función principal
def main():
    system('cls')
    validacion = inicio_sesion()
    while validacion:
        system('cls')
        accion = menu()
        if accion == '2':
            siguiente_accion = lista_estudiantes()
            lista_campus(siguiente_accion)
            system('cls')
        elif accion == '3':
            system('cls')
            print('El programa ha sido finalizado')
            validacion = False
        else:
            datos_estudiante = creacion_estudiante()
            dato_programa = datos_estudiante['programa']
            datos_estudiante_campus = elegir_campus(datos_estudiante)
            datos_estudiante_final = anadir_campus(datos_estudiante_campus, datos_estudiante_campus['campus'])
            anadir_estudiante(datos_estudiante_final, dato_programa)


if __name__ == '__main__':
    main()
