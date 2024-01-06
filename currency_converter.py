from monedas import monedas, operaciones, clp, ars, usd, eur, tr, gbp, cambio
def _print():
    print('\n-'*50)
    print('-'*50)

def verificacion(_moneda):
    try:
        moneda = int(_moneda)
        if moneda in monedas.keys():
            return moneda 
    except:
        texto = _moneda
        if texto in monedas.values():
            moneda = [key for key, value in monedas.items() if value == texto][0]
            return int(moneda)

def init():
    menu = 0
    while True:
        if menu == 0:
            _print() 
            print('Bienvenido'.center(50,'-'))
        print('\nCual es su moneda: ')
        for key, value in monedas.items():
            print(key, value)
        moneda_local = input('>>> ')

        _verificacion = verificacion(moneda_local)
        if _verificacion:
            return _verificacion
        
        if moneda_local == 0:
            break

        menu = 1
        _print()
        print('LA MONEDA INGRESADA NO ESTA EN NUESTRA LISTA')

def moneda_a_cambiar(moneda_local):
    _print()
    while True:
        print('A que moneda desea cambiar:\n')
        for key, value in monedas.items():
            if key != moneda_local:
                print(key, value)
        _moneda_a_cambiar = input('>>> ')
        _verificacion = verificacion(_moneda_a_cambiar)
        if _verificacion != moneda_local:
            return _verificacion
        _print()
        print('LA MONEDA INGRESADA NO ESTA EN NUESTRA LISTA')

def cambiar(moneda, cambiar_a, cantidad):
    seleccionar_moneda = [value for key, value in monedas.items() if key == moneda][0]
    seleccionar_cambio = [value for key, value in monedas.items() if key == cambiar_a][0]
    
    proceso = [value for key, value in cambio.items() if key == seleccionar_moneda][0]
    recibir = cantidad * proceso[seleccionar_cambio]
    print(f'CAMBIASTE {cantidad} {seleccionar_moneda} Y RECIBISTE {recibir} {seleccionar_cambio}')
    

def retirar(monto):
    pass

def main(_moneda_local, _change):
    # global operaciones
    print(type(_moneda_local), type(_change))
    _print()
    contador = 0
    while True:
        if contador != 0:
            while True:
                otra_operacion = input('DESEA REALIZAR OTRA OPERACION? Y/N: ')
                if otra_operacion.upper() == 'Y':
                    break
                elif otra_operacion.upper() == 'N':
                    print('ADIOS')
                    return None
                else:
                    print('OPCION NO VALIDA, VUELVA A INTENTAR')

        print('QUE OPERACION DESEAS REALIZAR?')
        for key, value in operaciones.items():
            print(key, value)

        opcion = input('>>> ')
        
        if opcion == '1':
            print('min:200 | max:500')
            cantidad = int(input('Cuanto desea cambiar?: '))
            cambiar(_moneda_local, _change, cantidad)


        elif opcion == '2':
            print('OPCION 2')
        elif opcion == '0':
            break
        else:
            print('OPCION NO VALIDA')
        contador = 1

if __name__ == '__main__':    
    _moneda_local = init()
    _change = moneda_a_cambiar(_moneda_local)
    main(_moneda_local, _change)
    
