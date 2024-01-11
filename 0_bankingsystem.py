""" 1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions. """

auth = False
username = input("Please, insert your username: ")
password = input("Please, insert your password: ")


if username == "eb" and password == "2024":
    auth = True 
else:
    print("Wrong credentials. You have two attempts")
    print("Please, insert your username: ")
    username = input()
    print("Please, insert your password: ")
    password = input()

    if username == "eb" and password == "2024":
        auth = True 
    else:
        print("Wrong credentials. You have one attempt")
        print("Please, insert your username: ")
        username = input()
        print("Please, insert your password: ")
        password = input()
        if username == "eb" and password == "2024":
            auth = True 
        else:
            print("Wrong credentials. Your user has been blocked")

if auth:
    print(f"Welcome, Mr. "+ username + ", to the Manchester Bank")
    balance = 2000
    
    print("What do you want to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View")
    print("4. Transfer")
    print("5. Exit")

    option = input()

    if option == "1":
        print("How much do you want to deposit?")
        deposit = int(input())
        balance += deposit
        print(f"Your balance is {balance}")
    elif option == "2":
        print("How much do you want to withdraw?")
        withdraw = int(input())
        balance -= withdraw
        print(f"Your balance is {balance}")
    elif option == "3":
        print(f"Your balance is {balance}")
    elif option == "4":
        print("How much do you want to transfer?")
        transfer = int(input())
        balance -= transfer
        print(f"Your balance is {balance}")
    elif option == "5":
        print("Bye")
