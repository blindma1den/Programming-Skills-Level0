value = {
    "CLP":887.89, 
    "ARS":811.58, 
    "USD":1, 
    "EUR": 0.91, 
    "TRY":29.75,
    "GBP":0.79
}

def conver():
    comission = 1.01

    print('*Convertidor de monedas*')

    money = {
    "CLP",
    "ARS",
    "USD",
    "EUR",
    "TRY",
    "GBP"
    }

    for date in money:
        print(date)

    print()
    initial = input('Elegi una moneda: ')
    cambio = input('¿A que moneda queres convertir?: ')

    cantidad = float(input('¿Cuanto dinero quieres convertir?: '))

    if(initial in value and cambio in value):
        valor1 = value[initial]
        valor2 = value[cambio]
        
        totalSinCom = cantidad * (valor2 / valor1)
        print(totalSinCom)
    else:
        print('No se encontro la moneda que elegiste.')

    print('Si deseas retirar los fondos se cobrara una comision de 1%')
    reti = input('Deseas retirar los fondos? Si / No: ').capitalize()

    if(reti == 'Si'):
        resto = totalSinCom % comission

        totalConCom = totalSinCom - resto

        print(f'Retirando: {totalConCom}')
    elif(reti == 'No'):
        conver()
    else: 
        print('No eligio una opción correcta. Indique Si o No')

conver()

conti = input('¿Desea seguir operando? Si / No: ').capitalize()

if(conti == 'Si'):
    conver()
elif(conti == 'No'):
    print('¡Gracias por usar nuestro sistema!')
else: 
    print('No eligio una opción correcta. Indique Si o No')