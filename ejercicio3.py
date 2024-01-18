# Ejercicio 3
# University enrollment system

diccUsers={"Mena":"1234", "Fidel":"ojos"}
diccPrograms={1:["Computer Science",5, 1 ,3,1 ],2:["Medicine",5, 1 ,3,1],3:["Marketing",5, 1 ,3,1],4:["Arts",5, 1 ,3,1]}

diccDatos={}

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
    return auth==1, name


def salida(motivo):
    if motivo==0:
        print ("\nNo es posible loguearlo.")
        exit()
    return    

def menuProgramas(nick):
    choise=None
    while choise in [1,2,3,4]:
        print("\nProgramas posibles.")    
        print("\n1. Computer Science\n2. Medicine \n3. Marketing \n 4. Arts")
        choise=int(input("\nElija el programa deseado: "))
        diccDatos[nick][1]=choise
    return choise

def ingresarDatos(nick):
    name=input("\nIngrese su nombre y apellido completos:\n")
    diccDatos[nick][0]=name
    return 

def chequearVacantes(program):
    return diccPrograms.get(program)[1]>0
      
    

def menuCampus():

    return 

log, nickname =login()
if log:
     ingresarDatos(nickname)
     program=menuProgramas(nickname)
     while not chequearVacantes(program):
        program=menuProgramas(nickname)

else:
    salida()