## Ejercicio 1

diccUsers={"Mena":"1234", "Fidel":"ojos"}
diccBalance= dict.fromkeys(diccUsers.keys(), 2000)


def loguearUsuario():
    auth=0
    oportunidades=3
    while (auth==0 and oportunidades>0):
        name=input("Ingrese su usuario: ")
        clave=input ("Ingrese su contrasenia: ")
        if clave==diccUsers.get(name):
            auth=1
            print(" ")
            print ("Usuario logueado correctamente")
            print(" ")
        else:
            print(" ")
            print ("Clave Incorrecta")
            print(" ")
            oportunidades = oportunidades-1

    return auth==1, name

def mostrarMenu():
    eleccion=0
    lista=["1","2","3","4","5"]
    while not (eleccion in lista):
        print(" ")
        print ("1. Deposit")
        print("2. Withdraw")
        print("3. View")
        print ("4. Transfer")
        print("5. Salir")
        print(" ")
        eleccion=input("Elija la opción deseada: ")
    return eleccion

def depositos(emisor, receptor):
    monto=int(input("Ingrese monto a depositar: "))
    nuevo=diccBalance.get(name)+monto
    diccBalance[name]=nuevo
    print(" ")
    print("Su nuevo saldo es: ", nuevo)
    return

def retiros(name):
    monto=int(input("Ingrese monto a retirar: "))
    saldo=diccBalance.get(name)
    if saldo>=monto:
        diccBalance[name]=saldo-monto
        print(" ")
        print("Su nuevo saldo es: ", diccBalance.get(name))

    else:
        print(" ")
        print("No posee suficiente saldo")
        print(" ")
    return

def consultaDeSaldos(name):
    print ("Su saldo actual es: ",diccBalance.get(name))
    return 

def transferencias(name):
    recep=input("Ingrese el nombre del receptor: ")
    nuevo=diccBalance.get(recep)
    if nuevo is not None:
        print("")
        monto=int(input("Ingrese el monto a transferir: "))
        saldo=diccBalance.get(name)
        if saldo>=monto:
            diccBalance[name]=saldo-monto
            print(" ")
            print("Le ha transferido", monto, " a ",recep)
            print("Su nuevo saldo es: ", diccBalance.get(name))
            diccBalance[recep]=nuevo+monto
        else:
            print(" ")
            print("No posee suficiente saldo")
            print(" ")
    else:
        print("Ese usuario no existe.")
    return

print("Bienvenidos al Banco de pruebas")

log, nombre= loguearUsuario()

if log:
    print("Bienvenido ", nombre)
    opcion=int(mostrarMenu())
    while opcion!=5:
        if opcion==1:
            depositos(nombre)
            opcion=int(mostrarMenu())
        else:
            if opcion==2:
                retiros(nombre)
                opcion=int(mostrarMenu())
            else:
                if opcion==3:
                    consultaDeSaldos(nombre)
                    opcion=int(mostrarMenu())
                else:
                    if opcion==4:
                        transferencias(nombre)
                        opcion=int(mostrarMenu())
                
else:
    print ("No se ha podido validar el usuario, intente nuevamente en unos minutos")