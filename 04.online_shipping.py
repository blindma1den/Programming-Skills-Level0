import os
import sys
import uuid

option = 0
login_attempts = 0
username = "mitnick"
password = "god"
login_success = False
shipping_kg = 2
shipping_cost = 0
shipping_id = ""

#list_packages = [{"uuid": 123456, "sender": "Mick Dallas", "buyer": "James Fast", "address": "1600 Amphitheatre Parkway Mountain View, CA 94043, USA", "weight": 1.3},{"id": 345632, "sender": "Mark Potter", "buyer": "Daniela Wever", "address": "17 Hacker Wy, Menlo Park, CA 94025, USA", "weight": 0.7}]
#print(list_packages[0]["id"])

os.system('clear')
print("WELCOME TO ONLINE SHIPPING SYSTEM")
print("=================================")
while login_attempts !=3:
    user_login = input("Username: ")
    pass_login = input("Password: ")
    if username == user_login and password == pass_login:
        login_success = True
        break
    else:
        login_attempts += 1
        if login_attempts == 3:
            print("Better luck next time! Bye.")
            sys.exit()
        print("Sorry, try again.")

while option != 2 and login_success == True:
    os.system('clear')
    print("WELCOME TO ONLINE SHIPPING SYSTEM")
    print("=================================")
    print("1. Send a package")
    print("2. Exit")
    option = int(input("Choose an option: "))
    if option == 1:
        print("\n")
        print("**** Sender info ****")
        sender_name = input("Sender name: ")
        sender_address = input("Sender address (full address): ")
        print("**** Recipient info ****")
        recipient_name = input("Sender name: ")
        recipient_address = input("Sender address (full address): ")
        print("**** Package info ****")
        package_weight = float(input("Weight of the package? (Kg): "))
        print("\n")
        shipping_cost = package_weight * shipping_kg
        print("Thanks for the info, your shipping costs {}".format(shipping_cost))
        shipping_answer = input("Is that OK? (Y/N) ")
        if shipping_answer == "Y" or shipping_answer == "y":
            # Here You can save the info to a db for future operations
            shipping_id = uuid.uuid4()
            print("\n")
            print("**** Shipping Summary ****")
            print("Shipping Id: {}". format(shipping_id))
            print("Shipping Weight: {}".format(package_weight))
            print("Shipping Cost: {}".format(shipping_cost))
            print("Sender Name: {}".format(sender_name))
            print("Sender Address: {}".format(sender_address))
            print("Recipient Name: {}".format(recipient_name))
            print("Recipient Address: {}".format(recipient_address))
            print("\n")
        answer = input("Would you like to perform another operation? (Y/N) ")
        if answer == "N" or answer == "n":
            print("Good Bye!")
            sys.exit()
