'''
Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions. 
'''
class User:
    userid:str
    password:str
    balance:int

    def __init__(self, userid, password, balance=2000):
        self.userid = userid
        self.password = password
        self.balance = balance       

user_credentials = [User(userid="user", password="password"), User(userid="Mayber", password="codingchallenge")]

    
def create_account(userid,password):
    return {"Error": "El usuario ya existe"} if search_user(userid) else user_credentials.update({userid:password})
def menu(userid):
    control = "n"
    
    while control == "n":
        print("Welcome.\n")
        print("1. ver saldo.")
        print("2. depositar dinero.")
        print("3. retirar dinero.")
        print("4. transferir dinero.")
        opcion= int(input())

        match(opcion):
            case 1:
                print(view(userid))
            case 2:
                sum= int(input("ingrese monto a depositar.\n"))
                deposit(userid, sum)
            case 3:
                sum= int(input("ingrese monto a retirar.\n"))
                withdraw(userid,sum)
            case 4:
                dest_userid=input("ingrese el ID del usuario destino.\n")
                sum = int(input("ingrese monto a transferir.\n"))
                transfer(userid, sum, dest_userid)
            case _:
                print("Please insert a Valid option.")

        control=input("Desea salir? y/n\n")
        
        if control == 'y':
            print("Hasta luego. Vuelva pronto!")
    
def search_user(userid:str)->User | bool:
    '''
    hace una búsqueda del usuario en las credenciales almacenadas si el usuario existe.
    
    :param: userid:str - ID proporcionado por el usuario.
    :return: object or error - objeto resultante contiene datos del usuario.

    '''
    user= filter(lambda user: user.userid == userid, user_credentials)
    try:
        return list(user)[0]
    except:
        return False
    
def login(userid:str, password:str)->bool:
    '''
    valida que las credenciales pertenezcan al usuario.

    :param: userid, password: str - ID y Password proporcionados por el usuario.
    :return: bool - son correctas ambas credenciales?
    '''
    user= search_user(userid)
    if not user: return False
    if userid == user.userid and password == user.password: return True 
    

def deposit(userid:str,sum):
    '''sumar cantidad actual mas deposito'''
    user=search_user(userid)
    if type(user) == User:
        user.balance += sum
        print("Success.\n")
        return 

def withdraw(userid,sum):
    '''restar cantidad actual menos deposito'''
    user=search_user(userid)
    if type(user) == User:
        if sum > user.balance:
            print("Not enough funds.")
            return
        user.balance -= sum
        print (f"success.\n {view(userid)}")
    return

def view(userid):
    '''mostrar balance actual.
    :param: userid: str - usuario actual.
    :return: str - balance de cuenta.
    '''
    user=search_user(userid)
    if type(user) == User:
        return f"Balance actual: {user.balance}"
    
def transfer(userid:str,sum:int, dest_userid:str):
    '''
    validar userid del cliente destino, 
    validar que la cantidad a transferir sea menor o igual a la disponible,
    restar del balance del usuario actual la cantidad a transferir.

    :param: userid, dest_userid: str, sum: int - id del usuario que envia, 
    usuario que recibe y suma a enviar.
    :return: str - success or failure.
    '''
    
    if type(search_user(userid)) == User and type(search_user(dest_userid)) == User:
        withdraw(userid,sum)
        deposit(dest_userid,sum)
        return
    else: 
        print("error!")
        return
    
        
    

def main():
    print("bienvenido! Por favor ingrese sus datos.")
    
    userid = input("ingrese su ID: ")
    password = input("ingrese su contraseña: ")
    limit = 2

    while not login(userid, password)and limit >0:
        print("wrong credentials!")
        limit -=1
        userid = input("ingrese su ID: ")
        password = input("ingrese su contraseña: ")
    if limit == 0:
        print("sorry, you're suspended")
    else:  
        menu(userid)


if __name__ == "__main__":
    main()
        