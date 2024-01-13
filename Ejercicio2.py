#Ejercicio 2

def cambio(monInic,monFin, cantidad):
    valorIn=currencies.get(monInic)
    valorFin=currencies.get(monFin)
    res=cantidad * valorIn / valorFin
    return res

currencies={"CLP":0.0011, "ARS":0.0012 , "USD":1, "EUR":1.10 , "TRY":0.033 , "GBP":1.27 }
topes={"CLP":[1,1000], "ARS":[10,10000] , "USD":[10,1000], "EUR":[100,2310] , "TRY":[99,42910], "GBP":[15,300]}
withdra="N"
print("\nCasa de cambio\n")

while withdra=="N" or withdra=="n":
    initC=""
    finishC=""
    #Eleccion de moneda inicial validada
    while initC not in currencies.keys():
        print("\nPara realizar una nueva conversión:")
        print("\nMonedas disponibles: CLP, ARS, USD, EUR, TRY, GBP")
        initC=input("Elija la moneda inicial o escriba 'salir': ")
        if initC=="salir":
            print("\nGracias por operar con nosotros.\nQue tenga un buen dia.")
            exit()
    #Eleccion de moneda a cambiar
    while finishC not in currencies.keys():
        print("\nMonedas disponibles: CLP, ARS, USD, EUR, TRY, GBP")
        finishC=input("Elija la moneda final: ")

    #Cambio
    monto=0
    while monto<=0:
        monto=int(input("\nElija el monto a cambiar expresado en la moneda inicial: "))
        min,max = topes.get(initC)
        if monto<min or monto>max:
            print("El rango va de ", min, " a ", max)

            monto=0 

    valorFin=cambio(initC, finishC, monto)

    print("\n Ahora usted tiene ", valorFin, " ", finishC)

    #Se ofrece el retiro
    withdra=""
    while withdra not in ["Y","N", "y","n"]:
        withdra=input("\nQuisiera usted retirar los fondos? (Y/N)  ")

    if withdra=="Y" or withdra=="y":
        print("\nRecuerde que el retiro tiene un costo del 1%")
        print("Usted puede retirar: ", valorFin * 0.99 , " ", finishC)
    
        nueva=""
        while nueva not in ["Y","N", "y","n"]:
            nueva=input("\nDesea realizar otra operacion: (Y/N)")        
            if nueva=="Y" or nueva=="y":
                withdra="N"
            else:
                print("\nGracias por operar con nosotros.\nQue tenga un buen dia.")

