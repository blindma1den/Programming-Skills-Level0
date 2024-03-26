#Exercise 1#
#!Create an online banking system!#
#|Users must be able to log in with a username and password
#|If the user enters the wrong credentials three times, the system must lock them out
#|The initial balance in the bank account is $2000
#|The system must allow users to deposit, withdraw, view, and transfer money
#|The system must display a menu for users to perform transactions

users = {"admin": "12345", "admin2":"67890"}
balance = 2000

def login_screen():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    return username, password

print("Hello, welcome to our bank")
username_input, password_input = login_screen()

def deposit(balance):
    dep = input("Insert the amount you want to deposit: $")
    if(dep.isnumeric()):
        return main_screen(balance + int(dep))
    else:
        print("The amount is not valid")
        return main_screen(balance)

def withdraw(balance):
    wit = input("Insert the amount you want to withdraw: $")
    if(wit.isnumeric()):
        if(balance - int(wit) < 0):
            print("You can't withdraw that amount")
            return main_screen(balance)
        else:
            return main_screen(balance - int(wit))
    else:
        print("The amount is not valid")
        return main_screen(balance)

def transfer(balance):
    transfer_user = input("Insert the username you want to transfer to: ")
    if(transfer_user in users):
        print("The user was found")
        tra = input(f"Insert the amount you want to transfer to the user with the card \"{transfer_user}\": $")
        if(tra.isnumeric()):
            if(balance - int(tra) <= 0):
                print("You can't transfer that amount")
                return main_screen(balance)
            else:
                return main_screen(balance - int(tra))
        else:
            print("The amount is not valid")
            return main_screen(balance)
    else:
        print("The user wasn't found")
        return main_screen(balance)

def main_screen(actual_balance):
    print("You can do the next actions: \n1.Deposit \n2.Withdraw \n3.View \n4.Transfer \n5.Exit")
    action = input("What would you like to do?: ")
    match action:
        case "1":
            deposit(actual_balance)
        case "2":
            withdraw(actual_balance)
        case "3":
            print(f"Current balance: ${actual_balance}")
            main_screen(actual_balance)
        case "4":
            transfer(actual_balance)
        case "5":
            print("Thanks for using the online banking system")
        case _:
            print("This action doesn't exist. Please try with another action")
            main_screen()

failed_attempts = 3
while(failed_attempts > 1):
    if(username_input in users):
        if(password_input == users[username_input]):
            print("Welcome")
            main_screen(balance)
            break
        else:
            failed_attempts -= 1
            print("Incorrect password. Try Again")
            username_input, password_input = login_screen()
    else:
        failed_attempts -= 1
        print("Username doesn't exist. Try Again")
        username_input, password_input = login_screen()
else:
    print("Too many failed attempts, f**k off")