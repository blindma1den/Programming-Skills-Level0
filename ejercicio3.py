# Ejercicio 3
# University enrollment system

diccUsers={"Mena":"1234", "Fidel":"ojos"}
diccPrograms={"1":["Computer Science",0, 0 ,0,0 ],"2":["Medicine",5, 0 ,3,1],"3":["Marketing",5, 1 ,3,1],"4":["Arts",5, 1 ,3,1]}

diccDatos=dict.fromkeys(diccUsers.keys(), ["", 0, 0])

def login():
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
    if oportunidades==0:
        salida(0)
    return name


def salida(motivo):
    if motivo==0:
        print ("\nNo es posible loguearlo.")
        exit()
    else:
        if motivo==1:
            print("Gracias ", diccDatos[nickname][0],  "\npor inscribirse en ", diccPrograms[program][0])
    return    

def menuProgramas():
    choise=None
    while choise not in ["1","2","3","4"]:
        print("\nProgramas posibles.")    
        print("\n1. Computer Science\n2. Medicine \n3. Marketing \n4. Arts")
        choise=input("\nElija el programa deseado: ")
    return choise

def ingresarDatos(nick):
    name=input("\nIngrese su nombre y apellido completos:\n")
    diccDatos[nick][0]=name
    return 

def chequearVacantes(program):
    return diccPrograms.get(program)[1]>0
      
def menuCampus():
    camp="0"
    while camp not in ["2","3", "4"]:
        print("\nIngrese el campus: \n2.London. \n3.Manchester \n4. Liverpool")
        camp=input("\n")
    return camp

nickname =login() # Login

ingresarDatos(nickname)
program=menuProgramas()
vacantes=chequearVacantes(program)
while vacantes==0:
    print("\nEn ese programa no quedan vacantes. Elija otra:\n")
    program=menuProgramas()
    vacantes=chequearVacantes(program)
diccDatos[nickname][1]=program
campus=menuCampus()
while diccPrograms[program][int(campus)]==0:
    print("En ese campus no quedan vacantes, elija otro.")
    campus=menuCampus()

diccPrograms[program][int(campus)]-=1
diccDatos[nickname][2]==int(campus)

salida(1)