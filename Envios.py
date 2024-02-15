"""Cree un sistema de envío en línea con las siguientes características:

1. El sistema tiene un inicio de sesión que se bloquea después del tercer intento fallido.
2. Mostrar un menú que permite: Enviar un paquete, salir del sistema.
3. Para enviar un paquete, se requieren los datos del remitente y del destinatario.
4. El sistema asigna un número de paquete aleatorio a cada paquete enviado.
5. El sistema calcula el precio de envío. $2 por kg.
6. El usuario debe ingresar el peso total de su paquete y el sistema debe mostrar el monto a pagar.
7. El sistema debería preguntar si el usuario desea realizar otra operación. Si la respuesta es sí,
   debería volver al menú principal. Si es no, debería cerrar el sistema."""
import random

users = {
    'david22': 'miclave',
    'carlos53' : 'suclave'}

def login():
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

def clientes():
    remitente = dict()
    destinatario = dict()
    print('Por favor llene el siguiente formulario:')
    remitente['nombre'] = input('ingrese el nombre del remitente--->')
    remitente['telefono'] = int(input('Ingrese el numero de telefono del remitente--->'))
    remitente['direccion'] = input('Ingrese la direccion del remitente--->')
    print(f'los datos del remitente son:\n'
          f'Nombre---> {remitente['nombre']}\n'
          f'Telefono---> {remitente['telefono']}\n'
          f'Direccion---> {remitente['direccion']}\n')
    print('Por favor ingrese los datos de quien recibe el paquete:')
    destinatario['nombre'] = input('ingrese el nombre del destinatario--->')
    destinatario['telefono'] = int(input('Ingrese el numero de telefono del destinatario--->'))
    destinatario['direccion'] = input('Ingrese la direccion del destinatario--->')
    print(f'los datos del destinatario son:\n'
          f'Nombre---> {destinatario['nombre']}\n'
          f'Telefono---> {destinatario['telefono']}\n'
          f'Direccion---> {destinatario['direccion']}\n')
    return remitente,destinatario

def envio():
    paquete= list()
    descripcion = input('describa de forma breve su paquete--->>>')
    paquete.append(descripcion)
    peso = float(input('Cuanto pesa su paquete?\n'
                   'ingrese el pero en KG por favor--->>>'))
    paquete.append(peso)
    id_paquete= random.randint(1000,9999)
    paquete.append(id_paquete)
    costo_envio= peso*2
    paquete.append(costo_envio)
    return paquete

def menu():
    print('****Bienvenido a nuestra empresa de envios****\n'
          '****Que desea hacer?****\n'
          '1. Enviar paquete\n'
          '2. Salir')
    opcion = int(input('Escriba el numero de la opcion que quiere realizar:'))
    if opcion == 1:
        remitente, destinatario = clientes()
        paquete = envio()
        return remitente,destinatario,paquete
    elif opcion==2:
        print('gracias esperamos,vuelva pronto')
        return (None,None,None,False)


#remitente, destinatario, paquete = menu()
control= login()
while control:
    remitente, destinatario, paquete = menu()

    print('*********************************************************************')
    print(f'Los datos de su envio son:\n'
          f'<<<REMITENTE>>>'
          f'*Nombre---> {remitente['nombre']}\n'
          f'*Telefono---> {remitente['telefono']}\n'
          f'*Direccion---> {remitente['direccion']}\n')
    print('<<<DESTINATARIO>>>')
    print(f'los datos del destinatario son:\n'
          f'Nombre---> {destinatario['nombre']}\n'
          f'Telefono---> {destinatario['telefono']}\n'
          f'Direccion---> {destinatario['direccion']}\n')
    print('***********************************************************************')
    print('<<<INFORMACION DE PAQUETE>>>\n'
          f'Descripcion del paquete--->{paquete[0]}\n'
          f'Peso del paquete--->{paquete[1]}\n'
          f'ID del envio--->{paquete[2]}\n'
          f'Costo del envio--->${paquete[3]} USD')
    continuar= int(input('Confirma que desea enviar el paquete?\n'
                     '1.Si\n'
                     '2.No\n'
                     'Escoja un numero--->'))
    if continuar== 1:
        print('Su paquete sera enviado conforme a los datos ingresados, muchas gracias por usar nuestros servicios')
        control = False
    elif continuar==2:
        remitente, destinatario, paquete, control = menu()
    else:
        print('ha seleccionado una opcion incorrecta')
