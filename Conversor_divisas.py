"""Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
	The user must choose their initial currency and the currency they want to exchange to.
	The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the
	 main menu.
	If the user decides to withdraw the funds, the system will charge a 1% commission.
	Set a minimum and maximum amount for each currency, it can be of your choice.
	The system should ask the user if they want to perform another operation. If they choose to do so, it should restart
	 the process; otherwise, the system should close.
"""




def trade_USD():
    match div_i:
        case 1:
            cambioUSD = monto * 0.0011
        case 2:
            cambioUSD = monto * 0.0012
        case 3:
            cambioUSD= monto
        case 4:
            cambioUSD = monto * 1.09
        case 5:
            cambioUSD = monto * 0.033
        case 6:
            cambioUSD = monto * 1.27
        case _:
            print('escogio una opcion no disponible')
            cambioUSD = None
    return cambioUSD



def trade_f(div_f,cambioUSD):
    conversion =0
    match div_f:
        case 1:
            conversion = cambioUSD * 1 / 0.0011
            print('usted tiene', conversion, 'en CPL')
        case 2:
            conversion = cambioUSD * 1 / 0.0012
            print('usted tiene', conversion, 'en ARS')
        case 3:
             conversion = cambioUSD * 1
             print('usted tiene', conversion, 'en USD')
        case 4:
            conversion = cambioUSD * 1 / 1.09
            print('usted tiene', conversion, 'en EUR')
        case 5:
            conversion = cambioUSD * 1 / 0.033
            print('usted tiene', conversion, 'en TRY')
        case 6:
            conversion = cambioUSD * 1 / 1.27
            print('usted tiene', conversion, 'en GBP')
        case _:
            print('escogio una opcion no disponible')
            conversion = None
    return conversion

control = True
while control:
    print('bienvenido a su conversor de divisas\n'
          '1.CLP (Peso Chileno)\n'
          '2.ARS (Peso Argentino)\n'
          '3.USD (Dolar Estadounidense)\n'
          '4.EUR (Euro)\n'
          '5.TRY (Lira Turca)\n'
          '6.GBP (Libra Esterlina)\n'
          )

    div_i = int(input('escoja por favor el numero de su divisa inicial: '))
    div_f = int(input('escoja por favor el numero de su divisa a convertir: '))
    monto = int(input('Cuanto dinero quiere cambiar?----->'))
    cambioUSD = trade_USD()
    resultado = trade_f(div_f,cambioUSD)
    retirar = int(input('Desea retirar sus fondos?\n'
                        '1.SI\n'
                        '2.NO\n'
                        'ESCOJA UN NUMERO:'))
    if retirar == 1:
        control = False
        print('Sus fondos son ', resultado)
        print('Por politicas de la empresa cobraremos 1% de comision por la operacion realizada quiere continuar?\n'
              'Seleccione\n'
              '1.SI\n'
              '2.NO\n')
        eleccion= int(input())
        if eleccion == 1:
            print ('su nuevo saldo es: ', resultado*0.99)
            c= int(input('desea hacer otra operacion?\n'
                         '1.SI\n'
                         '2.NO\n'))
            if c == 1:
                control = True
            elif c == 2:
                print('gracias por usar nuestros servicios, hasta luego')
        else:
            print('gracias por usar nuestros servicios, vuelva pronto')
            continue
    else:
        continue
