#Exercise 4#
#!Create an online shipping system with the following features:
#|The system has a login that locks after the third failed attempt.
#|Display a menu that allows: Sending a package, exiting the system.
#|To send a package, sender and recipient details are required.
#|The system assigns a random package number to each sent package.
#|The system calculates the shipping price. $2 per kg.
#|The user must input the total weight of their package, and the system should display the amount to pay.
#|The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.

import pycountry
import random
import string

users = {
    "Mike": "123",
    "Peter": "123",
    "Tony": "123",
    "1":"1"
}

def shipping():
    def repeat():
        selection = input("Would you like to perform another operation? (Y/N): ")
        match selection.upper():
            case "Y":
                return True
            case "N":
                return False
            case _:
                print("Invalid input.")
                return repeat()

    def random_package_number():
        characters = string.ascii_uppercase + string.digits
        tracking_number = ''.join(random.choice(characters) for i in range(8))
        return tracking_number
    
    def package_weight():
        weight = input("Insert the weight (in kg) of your package: ")
        print("=" * 100)
        if(weight.isnumeric()):
            return int(weight)
        else:
            print("Invalid input")
            return package_weight()

    while True:
        print("=" * 100)
        sender_details_country = input("To which country you're sending the package? ")
        if(pycountry.countries.get(name=sender_details_country)):
            print("=" * 100)
            print(f"Your total for the shipping is: ${package_weight() * 2} dollars")
            print(f"The tracking number of your package is: {random_package_number()}")

            if(repeat()):
                main()
                break
            else:
                break
        else:
            print("The country doesnt exists or is spelled incorrectly. Try Again")

def main():
    while True:
        print("=" * 100)
        print("Welcome to the online shipping system\n1.Send a package\n2.Exit the system")
        selection = input("What action would you like to do?: ")
        if selection.isnumeric():
            match selection:
                case "1":
                    shipping()
                    print("Thank you for using the system!")
                    break
                case "2":
                    print("Thank you for using the system!")
                    break
        else:
            print("Invalid input. Try again")

def validate_user(username, password):
    if(users[username] == password):
        return True
    else:
        return False

def login():
    attempts = 0
    while(attempts < 3):
        print("=================================")
        user_username = input("Enter your username: ")
        if(user_username in users):
            user_password = input("Enter your password: ")
            if(validate_user(user_username, user_password)):
                print("*Login succesfull*")
                main()
                break
            else:
                print("Incorrect password. Try again.")
                attempts += 1
        else:
            print("Username does not exist. Try again.")
    if(attempts == 3):
        print("Too many unsuccessful attempts. The program is now locked.")

login()