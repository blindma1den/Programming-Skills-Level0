"""
Author: CodinEric.

This is the most basic implementation of this exercise. You only need to know variables, input, if statements and while loops.

Requirements:
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
"""

auth_tries = 3
auth = False

while auth_tries > 0 and auth is False:
    print("insert your username")
    username = input()

    print("insert your password")
    password = input()

    if username == "codineric" or password == "1234":
        auth = True
    else:
        auth_tries -= 1
        print(f"Wrong credentials you have {auth_tries} tries left")

if auth_tries == 0:
    print("You have been locked out")
else:
    print("Welcome to the banking system")

    balance = 2000
    menu = True
    while menu:
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
            print("Goodbye")
            menu = False
        else:
            print(f"{option} is an invalid option")
