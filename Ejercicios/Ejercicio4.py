# 4. Create an online shipping system with the following features:
# * 		The system has a login that locks after the third failed attempt.
# * 		Display a menu that allows: Sending a package, exiting the system.
# * 		To send a package, sender and recipient details are required.
# * 		The system assigns a random package number to each sent package.
# * 		The system calculates the shipping price. $2 per kg.
# * 		The user must input the total weight of their package, and the system should display the amount to pay.
# * 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.

import sys
import random


class account:    
    def __init__(self):
        self.user = "a"
        self.password = "1"

class login(account):
    def __init__(self):
        super().__init__()
        self.failed_attempts = 0
    
    def verify_user(self, input_user, input_password):
        if input_user == self.user and input_password == self.password:
            print("Successful Login!!")

            return True
            
        else:
            print("Incorrect Password!")
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                print("error number 3. The program will close")
                sys.exit()
            return False

class menu(account):
    def select(self):
    
        print("1. Send package" )
        print("2. Exit")
    
    
    
        self.opcion = int(input(f"Enter option: "))
        return self.opcion
    


class actions(menu):
    
    def send_package(self):

        shipping_data.shipoing_values(self)
   
    def exit(self):
        print("exit")
        sys.exit()

    def numbers(self, opcion):
        if opcion == 1:
            self.send_package()
        elif opcion == 2:
            self.exit()
        else:
           print("Invalid option")


class shipping_data(actions):
    
    def shipoing_values(self):
        sender = input("enter sender name: ")
        addressee = input("enter recipient name: ")
        weight = input("Enter package weight: ")
        number = random.randint(1, 999999)
        shipping_price= weight * 2

        print("SHIP INFO")
        print(f"package number: {number}")
        print(f"sender details: {sender}")
        print(f"Adressee details: {addressee}")
        print(f"SHIPPING VALUE: ${shipping_price}")



    

    








if __name__ == "__main__":
    login_instance = login()

    logging = False
    while not logging:
        input_user = input("Enter your username: ")
        input_password = input("Enter your password: ")
        logging = login_instance.verify_user(input_user, input_password)

        menu_instance = menu()
        actions_instance = actions()
    while True:
        opcion = menu_instance.select()
        actions_instance.numbers(opcion)