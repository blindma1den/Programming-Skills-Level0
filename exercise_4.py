"""4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt. X
* 		Display a menu that allows: Sending a package, exiting the system. X
* 		To send a package, sender and recipient details are required. 
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package,
 and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes,
 it should return to the main menu. If it's no, it should close the system."""

import random

auth = False
username = input("Entry you username: ")
password = input("Entry you password: ")

if username == "Gabitoto" and password == "tortadericota":
    auth = True
else:
    print("Try again you have 2 trie left")
    print()
    print("Insert you username")
    username = input()
    print("Insert you password")
    password = input()
    if  username == "Gabitoto" and password == "tortadericota":
        auth = True
    else:
        print("Try again you have 1 trie left")
        print()
        print("Insert you username")
        username = input()
        print("Insert you password")
        password = input()
        if username == "Gabitoto" and password == "tortadericota":
            auth = True
        else:
            print("You are blocked!!!!")
if auth: 
    print("Welcome!!")            
    while True:
        print("---> Shipping System <---")
        print("1 <--- Sending a package")
        print("2 <--- exiting the system")
        choise = input("-------> ")
        if choise == "2":
            print("Goodbye, see you soon!!")
            break
        elif choise == "1":
            sender_details = input("Enter sender details: ")
            recipient_details = input("Enter recipient details: ")

            package_number = random.randint(1000, 9999)

            peso = int(input("wheight of product: "))
            
            costo_total = 2 * (peso)

            print(f"The sender is {sender_details} and this recipient is {recipient_details}")
            print(f"\nnumber of packeage: {package_number}")
            print(f"shipping price: ${costo_total:.2f}")
        else:
            print("not valid choise!!!!.\n")   

        another_operation = input("Do you want to perform another operation? (yes/no): ")
        if another_operation != 'yes':
            print("Goodbye, see you soon!!")
            break    