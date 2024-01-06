'''Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt. 
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.'''

from banking_system import login, search_user, User
import random

shipment_logs = []
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
            

def send_package(userid, dest_userid, weight):
    if type(search_user(userid)) == User and type(search_user(dest_userid)) == User:
        search_user(userid).balance -= shipping_price(weight)
        shipment_logs.append({"sender":userid, "recipient":dest_userid, "shipment fee":shipping_price(weight), "package number": random.randint(10000,99999)})
        print("success!")
    else: 
        print("error!")

def shipping_price(weight, min_price=2):

    if weight >0 and weight <=1:
        return min_price
    return weight*min_price

def menu(userid):
    control=int(input("Welcome to th shipment system! choose your option:\n1. Send a package.\n2. Exit.\n"))
    again="y"
    while again=="y":
        match(control):
            case 1:
                weight=int(input("type your package's weight."))
                option=input(f"the shipping fee is {shipping_price(weight)}, do you want to continue? y/n").lower()
                if option == 'y':
                    dest_userid=input("type the recipient's ID")
                    send_package(userid,dest_userid, weight)
                if option == 'n':
                    print("thanks for using the shipment system")
            case 2:
                print("thanks for using the shipment system")
            case _:
                print("invalid option")
        again = input("do you want to perform another operation? y/n").lower()

if __name__=="__main__":
    main()