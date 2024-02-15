"""  Crear un sistema de matrícula universitaria con las siguientes características:

    * El sistema cuenta con un login con usuario y contraseña.
    * Al iniciar sesión, un menú muestra los programas disponibles: Informática, Medicina, Marketing y Artes.
    * El usuario debe ingresar su nombre, apellido y programa elegido.
    *Cada programa tiene sólo 5 espacios disponibles. El sistema almacenará los datos de cada usuario registrado,
     y si supera el límite, deberá mostrar un mensaje indicando que el programa no está disponible.
    * Si la información de inicio de sesión es incorrecta tres veces, el sistema debe bloquearse.
    * El usuario debe elegir un campus de tres ciudades: Londres, Manchester, Liverpool.
    * En Londres, hay 1 plaza por programa; en Manchester, hay 3 espacios por programa y en Liverpool, hay 1 espacio por programa.
    * Si el usuario selecciona un programa en un campus que no tiene cupos disponibles, el sistema deberá mostrar la
    opción de inscribirse en el programa en otro campus."""

users = {
    'david22': 'miclave',
    'carlos53' : 'suclave'
}

programas = {
    'Informatica':{'machester':3,
                   'londres':1,
                   'liverpool':1},
    'Medicina':{'machester':3,
                'londres':1,
                'liverpool':1},
    'Marketing':{'machester':3,
                 'londres':1,
                 'liverpool':1},
    'Artes':{'machester':3,
             'londres':1,
             'liverpool':1}
}


def login ():
    for i in range(3):
        usuario = input('ingrese su usuario: ')
        password = input('ingrese su contraseña: ')
        if usuario in users and password == users[usuario]:
            print('accediste correctamente')
            return True
            break
        elif i<2:
            print('usuario o contraseña incorrecto ingrese de nuevo.')
        else:
            print("ingresaste mal tu usuario o contraseña en 3 oportunidades, el programa se cerrara.")
            return False

def menu():
    pass

def eleccion_usuario():
    nombre = input('ingrese su nombre: ')
    apellido = input('ingrese su apellido: ')
    programa = int(input('seleccione el numero de su programa de interes:\n'
                     '1.Medicina\n'
                     '2.Informatica\n'
                     '3.Marketing\n'
                     '4.Artes\n'))
    campus = int(input('1. Manchester\n'
                       '2. Londres\n'
                       '3. Liverpool\n'
                       'escoja el campus al que se quiere inscribir(1-3):'))
    matricula(programa,campus)

def cupos (programa,campus):
    if programa in programas and programas[programa][campus]>0 :
        return True
    else:
        return False


def matricula (programa, campus):
    if sum(programas[programa].values()) == 0:
        print('no hay cupos disponibles en ese programa')
    elif cupos(programa, campus):
        programas[programa][campus]-=1
    else:
        print('el campus que has seleccionado no tiene cupos disponibles ')

if login():
    eleccion_usuario()
    cupos(programa,campus)
